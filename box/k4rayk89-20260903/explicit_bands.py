#!/usr/bin/env python3
"""Explicit PIN12/lower-band charts for the two remaining k=4-ray rows.

This is a deliberately independent driver.  It implements the formulae in
``structure-note.md`` in beta (not frozen-driver B=2*beta) coordinates.  The
two localisations/normalisations are always

    mu*mu_inv - 1 = 0,          coeff_(x^4) J(f,g) - 1 = 0.

In particular, this file never sets ``mu=1``.  Rows are emitted in the macro
order terminal recurrence -> actual rho matches -> full ID6 Jacobian.  Each
guided-GB subprocess is limited to one core and at most 600 seconds.  Modular
units are recorded as F_p-only and cause an exact-Q replay only after all
requested good primes kill the same cumulative prefix.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import sys
import time
from typing import Any, Iterable, Mapping, Sequence

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
HERE = ROOT / "box" / "k4rayk89-20260903"
RUNS = HERE / "explicit-runs"
sys.path.insert(0, str(ROOT))

from box.lib.guided_gb import (  # noqa: E402
    GuidedGBResult,
    PromotionPolicy,
    RunConfig,
    SingularSystem,
    guided_groebner,
)
from box.lib.staged_band_emitter import (  # noqa: E402
    BandEmitConfig,
    BandRow,
    emit_staged_band_files,
)


GOOD_PRIMES = (32003, 32009, 32027)
MAX_TIMEOUT = 600
CoordPoly = dict[tuple[int, int], sp.Expr]


def atomic_write(path: Path, payload: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(payload, encoding="utf-8")
    temporary.replace(path)


def sha256_text(payload: str) -> str:
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def clean_coefficient(expr: sp.Expr) -> sp.Expr:
    """Expand only a coordinate coefficient, never a full x,y polynomial."""

    return sp.expand(expr)


def cp_clean(poly: Mapping[tuple[int, int], sp.Expr]) -> CoordPoly:
    out: CoordPoly = {}
    for monomial, value in poly.items():
        value = clean_coefficient(value)
        if value != 0:
            out[monomial] = value
    return out


def cp_add(*polys: Mapping[tuple[int, int], sp.Expr]) -> CoordPoly:
    out: CoordPoly = {}
    for poly in polys:
        for monomial, value in poly.items():
            out[monomial] = out.get(monomial, sp.Integer(0)) + value
    return cp_clean(out)


def cp_add_lazy(*polys: Mapping[tuple[int, int], sp.Expr]) -> CoordPoly:
    """Coordinate addition without coefficient expansion (internal staging)."""

    out: CoordPoly = {}
    for poly in polys:
        for monomial, value in poly.items():
            out[monomial] = out.get(monomial, sp.Integer(0)) + value
    return out


def cp_scale(poly: Mapping[tuple[int, int], sp.Expr], scalar: sp.Expr) -> CoordPoly:
    if scalar == 0:
        return {}
    return cp_clean({monomial: scalar * value for monomial, value in poly.items()})


def cp_shift(poly: Mapping[tuple[int, int], sp.Expr], i: int, j: int) -> CoordPoly:
    return {(a + i, b + j): value for (a, b), value in poly.items()}


def cp_mul(
    left: Mapping[tuple[int, int], sp.Expr],
    right: Mapping[tuple[int, int], sp.Expr],
    *,
    clean: bool = True,
) -> CoordPoly:
    out: CoordPoly = {}
    for (i, j), a in left.items():
        for (k, ell), b in right.items():
            key = (i + k, j + ell)
            out[key] = out.get(key, sp.Integer(0)) + a * b
    return cp_clean(out) if clean else out


def cp_pow(poly: Mapping[tuple[int, int], sp.Expr], exponent: int) -> CoordPoly:
    out: CoordPoly = {(0, 0): sp.Integer(1)}
    for _ in range(exponent):
        out = cp_mul(out, poly)
    return out


def cp_diff(poly: Mapping[tuple[int, int], sp.Expr], variable: str) -> CoordPoly:
    out: CoordPoly = {}
    index = 0 if variable == "x" else 1
    for (i, j), value in poly.items():
        power = (i, j)[index]
        if power == 0:
            continue
        key = (i - 1, j) if index == 0 else (i, j - 1)
        out[key] = power * value
    return cp_clean(out)


def cp_expr(poly: Mapping[tuple[int, int], sp.Expr], x: sp.Symbol, y: sp.Symbol) -> sp.Expr:
    return sp.Add(*(value * x**i * y**j for (i, j), value in sorted(poly.items())))


def cp_substitute(
    poly: Mapping[tuple[int, int], sp.Expr], substitutions: Mapping[sp.Symbol, sp.Expr]
) -> CoordPoly:
    if not substitutions:
        return dict(poly)
    return cp_clean(
        {monomial: value.xreplace(substitutions) for monomial, value in poly.items()}
    )


def cp_homogeneous_degree(poly: Mapping[tuple[int, int], sp.Expr]) -> int | None:
    degrees = {i + j for i, j in poly}
    if not degrees:
        return None
    return next(iter(degrees)) if len(degrees) == 1 else -1


def cp_quoy(
    numerator: Mapping[tuple[int, int], sp.Expr],
    monic_divisor: Mapping[tuple[int, int], sp.Expr],
    y_degree: int,
) -> tuple[CoordPoly, CoordPoly]:
    """Long division in y over Q[parameters,x]; divisor leading coeff is 1."""

    if clean_coefficient(monic_divisor.get((0, y_degree), 0)) != 1:
        raise AssertionError("h is not monic of the declared y degree")
    if any(j == y_degree and i != 0 for i, j in monic_divisor):
        raise AssertionError("h has another term at its top y degree")
    remainder = cp_clean(numerator)
    quotient: CoordPoly = {}
    while remainder:
        top_y = max(j for _i, j in remainder)
        if top_y < y_degree:
            break
        leaders = [
            (i, clean_coefficient(value))
            for (i, j), value in remainder.items()
            if j == top_y and clean_coefficient(value) != 0
        ]
        if not leaders:
            remainder = cp_clean(remainder)
            continue
        for i, leader in leaders:
            qkey = (i, top_y - y_degree)
            quotient[qkey] = quotient.get(qkey, sp.Integer(0)) + leader
            subtract = cp_scale(cp_shift(monic_divisor, i, top_y - y_degree), -leader)
            remainder = cp_add(remainder, subtract)
    return cp_clean(quotient), cp_clean(remainder)


def singular_expr(expr: sp.Expr) -> str:
    return sp.sstr(clean_coefficient(expr), order="lex").replace("**", "^")


def denominator_lcm(expressions: Iterable[sp.Expr]) -> int:
    result = 1
    for expr in expressions:
        for rational in expr.atoms(sp.Rational):
            result = math.lcm(result, int(rational.q))
    return result


def exact_rref_with_transform(
    matrix: Sequence[Sequence[Fraction]],
) -> tuple[list[list[Fraction]], list[list[Fraction]], list[int]]:
    """RREF over Q together with the exact left row-operation matrix."""

    row_count = len(matrix)
    column_count = len(matrix[0]) if matrix else 0
    work = [list(row) for row in matrix]
    transform = [
        [Fraction(int(i == j), 1) for j in range(row_count)]
        for i in range(row_count)
    ]
    pivots: list[int] = []
    pivot_row = 0
    for column in range(column_count):
        found = next(
            (row for row in range(pivot_row, row_count) if work[row][column]), None
        )
        if found is None:
            continue
        if found != pivot_row:
            work[pivot_row], work[found] = work[found], work[pivot_row]
            transform[pivot_row], transform[found] = transform[found], transform[pivot_row]
        scale = work[pivot_row][column]
        work[pivot_row] = [entry / scale for entry in work[pivot_row]]
        transform[pivot_row] = [entry / scale for entry in transform[pivot_row]]
        for row in range(row_count):
            if row == pivot_row or work[row][column] == 0:
                continue
            multiple = work[row][column]
            work[row] = [a - multiple * b for a, b in zip(work[row], work[pivot_row])]
            transform[row] = [
                a - multiple * b for a, b in zip(transform[row], transform[pivot_row])
            ]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == row_count:
            break
    return work, transform, pivots


def transform_expressions(
    transform: Sequence[Sequence[Fraction]], expressions: Sequence[sp.Expr]
) -> list[sp.Expr]:
    return [
        clean_coefficient(
            sum(
                (sp.Rational(value.numerator, value.denominator) * expr for value, expr in zip(row, expressions)),
                sp.Integer(0),
            )
        )
        for row in transform
    ]


@dataclass
class ExplicitChart:
    K: int
    branch: str
    variables: list[str]
    weights: list[int]
    rows_by_stage: dict[str, list[BandRow]]
    h: str
    beta: str
    alpha: str
    rho: str
    theta: str
    formula_controls: dict[str, Any]
    denominator_lcm: int
    chart_sha256: str
    build_seconds: float

    def rows_through(self, stage: str) -> list[BandRow]:
        order = ("terminal", "rho", "jacobian")
        endpoint = order.index(stage)
        return [row for name in order[: endpoint + 1] for row in self.rows_by_stage[name]]

    def metadata(self) -> dict[str, Any]:
        return {
            "type": "K4RAY-EXPLICIT-LOWER-BANDS",
            "K": self.K,
            "b": self.K - 2,
            "branch": self.branch,
            "normalization": {
                "CST": 1,
                "top_beta": "mu*y^(K-3)*(y-x)",
                "mu_localizer": "mu*mu_inv-1",
                "mu_set_to_one": False,
            },
            "variables": self.variables,
            "weights": self.weights,
            "variable_count": len(self.variables),
            "stage_row_counts": {key: len(value) for key, value in self.rows_by_stage.items()},
            "reconstruction": {
                "h": self.h,
                "beta": self.beta,
                "alpha": self.alpha,
                "rho": self.rho,
            },
            "theta": self.theta,
            "formula_controls": self.formula_controls,
            "denominator_lcm": self.denominator_lcm,
            "chart_sha256": self.chart_sha256,
            "build_seconds": self.build_seconds,
            "fallacy_v2": {
                "modular_unit": "F_p-only until exact-Q confirmation",
                "posdim": "not a counterexample without point extraction and exact J=constant",
                "localization": "inhomogeneous",
            },
        }


class ChartBuilder:
    def __init__(
        self,
        K: int,
        branch: str,
        through: str,
        *,
        terminal_rref: bool = True,
        coordinate_state_only: bool = False,
    ) -> None:
        if K not in (8, 9):
            raise ValueError("this explicit chart is only for K=8 or K=9")
        if K == 8 and branch != "single":
            raise ValueError("K=8 has only branch=single")
        if K == 9 and branch not in ("A", "B"):
            raise ValueError("K=9 needs branch A or B")
        if through not in ("terminal", "rho", "jacobian"):
            raise ValueError("bad terminal stage")
        self.K = K
        self.branch = branch
        self.through = through
        self.terminal_rref = terminal_rref
        self.coordinate_state_only = coordinate_state_only
        self.x, self.y = sp.symbols("x y")
        self.variables: list[sp.Symbol] = []
        self.weights: dict[sp.Symbol, int] = {}
        self.row_denominators: list[int] = []
        # Populated after PIN12/H3 and terminal RREF.  This is intentionally a
        # live, non-serialized handoff for banded alpha/rho eliminators, so a
        # downstream driver need not parse the large reconstruction strings.
        self.coordinate_state: dict[str, Any] | None = None
        self.mu = self.new_symbol("mu", K + 2)
        self.mu_inv = self.new_symbol("mu_inv", 1)
        self.L: CoordPoly = {(0, 1): sp.Integer(1), (1, 0): sp.Integer(-1)}
        self.H: CoordPoly = cp_shift(self.L, 0, K - 1)

    def new_symbol(self, name: str, weight: int) -> sp.Symbol:
        symbol = sp.Symbol(name)
        if symbol in self.weights:
            raise ValueError(f"duplicate symbol {name}")
        self.variables.append(symbol)
        self.weights[symbol] = weight
        return symbol

    def form(self, prefix: str, degree: int, weight: int) -> CoordPoly:
        out: CoordPoly = {}
        for i in range(degree + 1):
            j = degree - i
            out[(i, j)] = self.new_symbol(f"{prefix}_{i}_{j}", weight)
        return out

    def band_sum(self, bands: Mapping[int, CoordPoly]) -> CoordPoly:
        return cp_add(*bands.values())

    def recurrence_parts(
        self, hbands: Mapping[int, CoordPoly], pbands: Mapping[int, CoordPoly]
    ) -> tuple[Any, Any]:
        s_cache: dict[int, CoordPoly] = {}
        t_cache: dict[int, CoordPoly] = {}

        def sb(n: int) -> CoordPoly:
            if n not in s_cache:
                s_cache[n] = cp_clean(
                    cp_add_lazy(
                        *(cp_mul(hbands[a], hbands[n - a], clean=False) for a in range(n + 1))
                    )
                )
            return s_cache[n]

        def tb(n: int) -> CoordPoly:
            if n not in t_cache:
                pieces = []
                for a in range(n + 1):
                    for b in range(n - a + 1):
                        c = n - a - b
                        if a in pbands and b in pbands and c in pbands:
                            pieces.append(
                                cp_mul(
                                    cp_mul(pbands[a], pbands[b], clean=False),
                                    pbands[c],
                                    clean=False,
                                )
                            )
                t_cache[n] = cp_clean(cp_add_lazy(*pieces))
            return t_cache[n]

        return sb, tb

    def assert_localized_zero(self, poly: Mapping[tuple[int, int], sp.Expr], label: str) -> str:
        failures: list[str] = []
        for monomial, coefficient in poly.items():
            reduced = sp.cancel(coefficient.subs(self.mu_inv, 1 / self.mu))
            if reduced != 0:
                reduced = sp.factor(reduced)
            if reduced != 0:
                failures.append(f"{monomial}:{reduced}")
        if failures:
            raise AssertionError(f"localized identity {label} failed: {failures[:2]}")
        return "PASS_MOD_mu*mu_inv-1"

    def rows_from_poly(
        self,
        poly: Mapping[tuple[int, int], sp.Expr],
        *,
        stage: str,
        family: str,
        include_zero: bool = False,
    ) -> list[BandRow]:
        rows: list[BandRow] = []
        for (i, j), coefficient in sorted(poly.items(), key=lambda item: (-(sum(item[0])), item[0])):
            coefficient = clean_coefficient(coefficient)
            if coefficient == 0 and not include_zero:
                continue
            # Singular finite-characteristic rings do not accept a polynomial
            # divided by a number (``p/2``).  Clearing a row by its positive
            # rational denominator is ideal-preserving away from the recorded
            # bad primes and is also harmless over Q.
            row_denominator = denominator_lcm((coefficient,))
            coefficient = clean_coefficient(row_denominator * coefficient)
            self.row_denominators.append(row_denominator)
            rows.append(
                BandRow(
                    label=f"{family}_x{i}_y{j}",
                    band=f"{stage}_{family}",
                    degree=i + j,
                    expr=singular_expr(coefficient),
                    source={
                        "kind": family,
                        "stage": stage,
                        "x_power": i,
                        "y_power": j,
                        "xy_degree": i + j,
                        "cleared_rational_denominator": row_denominator,
                    },
                )
            )
        return rows

    def row_from_expression(
        self,
        expression: sp.Expr,
        *,
        stage: str,
        family: str,
        index: int,
        source: Mapping[str, Any],
    ) -> BandRow:
        expression = clean_coefficient(expression)
        row_denominator = denominator_lcm((expression,))
        expression = clean_coefficient(row_denominator * expression)
        self.row_denominators.append(row_denominator)
        return BandRow(
            label=f"{family}_compat_{index}",
            band=f"{stage}_{family}",
            degree=int(source.get("recurrence_index", 0)),
            expr=singular_expr(expression),
            source={
                **source,
                "kind": family,
                "stage": stage,
                "compatibility_index": index,
                "cleared_rational_denominator": row_denominator,
            },
        )

    def eliminate_terminal_band(
        self,
        polynomial: Mapping[tuple[int, int], sp.Expr],
        pivot_variables: Sequence[sp.Symbol],
        *,
        recurrence_index: int,
    ) -> tuple[dict[sp.Symbol, sp.Expr], list[sp.Expr], dict[str, Any]]:
        """Eliminate a complete h_i band by the invertible mu^3 matrix.

        The coefficient matrix is mu^3 times a rational constant matrix.
        Pivot formulae use ``mu_inv^3`` and are therefore exact on the retained
        ``mu*mu_inv-1`` localization.  Compatibility rows are not divided by
        mu and remain polynomial over Z after their numeric denominators are
        cleared at emission.
        """

        # CoordPoly producers already canonicalize each coefficient.  A second
        # full expansion here dominated K=9 wall time, especially in branch B.
        equations = [value for _monomial, value in sorted(polynomial.items()) if value != 0]
        zero_pivots = {variable: sp.Integer(0) for variable in pivot_variables}
        matrix: list[list[Fraction]] = []
        right: list[sp.Expr] = []
        for equation in equations:
            coefficients = [equation.coeff(variable) for variable in pivot_variables]
            rest = equation.xreplace(zero_pivots)
            reconstructed_difference = equation - rest - sum(
                (coefficient * variable for coefficient, variable in zip(coefficients, pivot_variables)),
                sp.Integer(0),
            )
            if reconstructed_difference != 0 and clean_coefficient(reconstructed_difference) != 0:
                raise AssertionError(f"REC{recurrence_index} is nonlinear in its h-band")
            constant_row: list[Fraction] = []
            for coefficient in coefficients:
                normalized = sp.cancel(coefficient / self.mu**3)
                if not normalized.is_Rational:
                    raise AssertionError(
                        f"REC{recurrence_index} pivot is not mu^3 times Q: {normalized}"
                    )
                normalized = sp.Rational(normalized)
                constant_row.append(Fraction(int(normalized.p), int(normalized.q)))
            matrix.append(constant_row)
            right.append(-rest)

        rref, transform, pivots = exact_rref_with_transform(matrix)
        transformed_right = transform_expressions(transform, right)
        free_columns = [column for column in range(len(pivot_variables)) if column not in pivots]
        substitutions: dict[sp.Symbol, sp.Expr] = {}
        for row, pivot_column in enumerate(pivots):
            solution = self.mu_inv**3 * transformed_right[row]
            for column in free_columns:
                value = rref[row][column]
                if value:
                    solution -= sp.Rational(value.numerator, value.denominator) * pivot_variables[column]
            substitutions[pivot_variables[pivot_column]] = clean_coefficient(solution)

        compatibility = [
            clean_coefficient(transformed_right[row])
            for row in range(len(pivots), len(equations))
            if clean_coefficient(transformed_right[row]) != 0
        ]
        audit = {
            "recurrence_index": recurrence_index,
            "equation_count": len(equations),
            "pivot_candidate_count": len(pivot_variables),
            "rank": len(pivots),
            "pivot_variables": [str(pivot_variables[column]) for column in pivots],
            "free_variables": [str(pivot_variables[column]) for column in free_columns],
            "compatibility_count": len(compatibility),
            "matrix_factor": "mu^3",
            "inverse_used": "mu_inv^3",
        }
        return substitutions, compatibility, audit

    def build(self) -> ExplicitChart:
        started = time.monotonic()
        K = self.K
        mu = self.mu
        mi = self.mu_inv
        Y = lambda n: {(0, n): sp.Integer(1)}  # noqa: E731

        tau = self.form("tau", K - 7, K + 3)
        tau_top = tau[(0, K - 7)]
        chi = self.form("chi", K - 8, 2 * K + 6)

        if K == 8:
            v_free = self.new_symbol("v_1_0", K + 3)
            v: CoordPoly = {(1, 0): v_free, (0, 1): 2 * tau_top}
            phi = cp_mul(Y(1), v)
        elif self.branch == "A":
            w_free = self.new_symbol("w_1_0", K + 3)
            w: CoordPoly = {(1, 0): w_free, (0, 1): 2 * tau_top}
            v = cp_mul(Y(1), w)
            phi = cp_mul(Y(1), v)
        else:
            v = {
                (2, 0): self.new_symbol("v_2_0", K + 3),
                (1, 1): self.new_symbol("v_1_1", K + 3),
                (0, 2): 2 * tau_top,
            }
            phi = cp_mul(Y(1), v)

        pbands: dict[int, CoordPoly] = {0: cp_scale(cp_shift(self.L, 0, K - 3), mu)}
        pbands[1] = cp_mul(
            Y(2),
            cp_add(cp_scale(cp_mul(Y(2), tau), 3), cp_scale(cp_mul(self.L, phi), -1)),
        )

        zeta: CoordPoly | None = None
        if K == 9 and self.branch == "B":
            zeta = self.form("zeta", 4, 2 * K + 6)
            pbands[2] = cp_scale(
                cp_add(cp_mul(self.L, cp_pow(v, 2)), cp_scale(cp_mul(Y(1), zeta), -1)),
                sp.Rational(1, 12) * mi,
            )
        else:
            pbands[2] = self.form("p2", K - 4, K + 4)
        for index in range(3, K - 1):
            pbands[index] = self.form(f"p{index}", K - 2 - index, K + 2 + index)

        hbands: dict[int, CoordPoly] = {0: self.H}
        hbands[1] = cp_add(
            cp_scale(cp_mul(Y(6), tau), 3 * mi),
            cp_scale(cp_mul(cp_mul(Y(4), self.L), phi), -sp.Rational(3, 2) * mi),
        )
        hbands[2] = cp_scale(
            cp_add(
                cp_scale(cp_mul(Y(2), pbands[2]), mu),
                cp_scale(cp_mul(cp_mul(Y(9 - K), self.L), cp_pow(phi, 2)), sp.Rational(1, 4)),
                cp_scale(cp_mul(Y(6), chi), -1),
            ),
            sp.Rational(3, 2) * mi**2,
        )

        if K == 8:
            omega_part = cp_add(
                cp_mul(cp_mul(self.L, Y(1)), cp_pow(v, 3)),
                cp_scale(cp_mul(cp_mul(chi, v), Y(4)), 36),
                cp_scale(cp_mul(cp_mul(pbands[3], Y(2)), {(0, 0): mu**2}), 24),
                cp_scale(cp_mul(pbands[2], v), -12 * mu),
                cp_scale(cp_mul(cp_mul(cp_pow(v, 2), tau), Y(2)), -18),
            )
            hbands[3] = cp_scale(omega_part, sp.Rational(1, 16) * mi**3)
            kappa = None
        else:
            kappa = self.new_symbol("kappa", 3 * K + 9)
            if self.branch == "A":
                assert "w" in locals()
                omega = cp_mul(
                    w,
                    cp_add(
                        cp_mul(cp_mul(self.L, Y(2)), cp_pow(w, 2)),
                        cp_scale(pbands[2], -12 * mu),
                    ),
                )
            else:
                assert zeta is not None
                omega = cp_mul(v, zeta)
            h3_numerator = cp_add(
                omega,
                cp_scale(cp_mul(cp_mul(chi, v), Y(3)), 36),
                cp_scale(cp_mul(pbands[3], Y(2)), 24 * mu**2),
                cp_scale(cp_mul(cp_pow(v, 2), tau), -18),
                cp_scale(Y(6), -8 * kappa),
            )
            hbands[3] = cp_scale(h3_numerator, sp.Rational(1, 16) * mi**3)

        for index in range(4, K + 1):
            hbands[index] = self.form(f"h{index}", K - index, index)

        # The monic equation from PIN12 has been used as a parametrization.
        if hbands[1].get((0, K - 1), 0) != 0:
            raise AssertionError("the pure y^(K-1) h coefficient was not eliminated")

        sb, tb = self.recurrence_parts(hbands, pbands)
        q: dict[int, CoordPoly] = {
            0: cp_scale(cp_shift(self.L, 0, K - 7), mu**3),
            1: cp_scale(tau, 3 * mu**2),
            2: cp_scale(chi, 3 * mu),
        }
        if K == 8:
            q[3] = {}
        else:
            assert kappa is not None
            q[3] = {(0, 0): kappa}
            q[4] = {}
            q[5] = {}

        def recurrence_n(n: int) -> CoordPoly:
            pieces = [tb(n)]
            for index in range(1, n + 1):
                qband = q.get(n - index, {})
                if qband:
                    pieces.append(cp_scale(cp_mul(sb(index), qband), -1))
            return cp_add(*pieces)

        controls: dict[str, Any] = {
            "source_note": str(HERE / "structure-note.md"),
            "beta_scale_not_B_scale": True,
            "PIN12_monic_relation_built_in": True,
            "mu_not_fixed": True,
        }
        controls["REC1"] = self.assert_localized_zero(
            cp_add(recurrence_n(1), cp_scale(cp_mul(cp_pow(self.H, 2), q[1]), -1)),
            "REC1",
        )
        controls["REC2"] = self.assert_localized_zero(
            cp_add(recurrence_n(2), cp_scale(cp_mul(cp_pow(self.H, 2), q[2]), -1)),
            "REC2",
        )
        if K == 8:
            controls["K8_H3_REC3"] = self.assert_localized_zero(recurrence_n(3), "K8-H3")
            theta = cp_scale(
                cp_mul(
                    cp_shift(cp_pow(self.L, 2), 0, 8),
                    {
                        (4, 0): 195,
                        (3, 1): 240,
                        (2, 2): 320,
                        (1, 3): 512,
                        (0, 4): 2048,
                    },
                ),
                sp.Rational(1, 6630),
            )
            terminal_polys = [("K8_REC4_THETA", cp_add(recurrence_n(4), cp_scale(theta, -1)))]
        else:
            controls["K9_H3_REC3"] = self.assert_localized_zero(
                cp_add(recurrence_n(3), cp_scale(cp_mul(cp_pow(self.H, 2), q[3]), -1)),
                "K9-H3",
            )
            split_left = cp_mul(v, cp_add(cp_mul(self.L, cp_pow(v, 2)), cp_scale(pbands[2], -12 * mu)))
            if self.branch == "A":
                controls["K9_SPLIT"] = "A:v=y*w_BUILT_IN"
            else:
                assert zeta is not None
                controls["K9_SPLIT"] = self.assert_localized_zero(
                    cp_add(split_left, cp_scale(cp_mul(cp_mul(v, Y(1)), zeta), -1)),
                    "K9-SPLIT-B",
                )
            theta = cp_scale(
                cp_mul(
                    cp_shift(cp_pow(self.L, 2), 0, 9),
                    {
                        (4, 0): 35,
                        (3, 1): 42,
                        (2, 2): 54,
                        (1, 3): 81,
                        (0, 4): 243,
                    },
                ),
                sp.Rational(1, 1365),
            )
            terminal_polys = [
                ("K9_REC4_ZERO", recurrence_n(4)),
                ("K9_REC5_ZERO", recurrence_n(5)),
                ("K9_REC6_THETA", cp_add(recurrence_n(6), cp_scale(theta, -1))),
            ]

        rows_by_stage: dict[str, list[BandRow]] = {"terminal": [], "rho": [], "jacobian": []}
        if K == 9 and self.terminal_rref:
            cumulative_substitutions: dict[sp.Symbol, sp.Expr] = {}
            rref_audit: list[dict[str, Any]] = []
            for (family, raw_polynomial), band_index in zip(terminal_polys, (4, 5, 6)):
                # The precomputed raw N5/N6 expressions contain the earlier
                # h bands, so applying the accumulated substitutions here is
                # algebraically identical to rebuilding the recurrence caches.
                polynomial = cp_substitute(raw_polynomial, cumulative_substitutions)
                pivot_variables = [
                    value
                    for _monomial, value in sorted(hbands[band_index].items())
                    if isinstance(value, sp.Symbol)
                ]
                substitutions, compatibility, audit = self.eliminate_terminal_band(
                    polynomial, pivot_variables, recurrence_index=band_index
                )
                cumulative_substitutions.update(substitutions)
                hbands[band_index] = cp_substitute(hbands[band_index], substitutions)
                for variable in substitutions:
                    self.variables.remove(variable)
                    del self.weights[variable]
                for index, expression in enumerate(compatibility):
                    rows_by_stage["terminal"].append(
                        self.row_from_expression(
                            expression,
                            stage="terminal",
                            family=family,
                            index=index,
                            source={
                                "recurrence_index": band_index,
                                "terminal_rref": True,
                                "localized_equivalence": "mu*mu_inv-1",
                            },
                        )
                    )
                rref_audit.append(audit)
            # Apply all three bands to the reconstruction before exact quoy.
            for band_index in range(4, K + 1):
                hbands[band_index] = cp_substitute(
                    hbands[band_index], cumulative_substitutions
                )
            controls["terminal_RREF"] = rref_audit
            controls["terminal_RREF_eliminated_count"] = len(cumulative_substitutions)
            controls["terminal_RREF_equivalence_scope"] = "mu*mu_inv-1 localization"
        else:
            for family, polynomial in terminal_polys:
                rows_by_stage["terminal"].extend(
                    self.rows_from_poly(polynomial, stage="terminal", family=family)
                )

        h = self.band_sum(hbands)
        beta = self.band_sum(pbands)
        self.coordinate_state = {
            "K": K,
            "branch": self.branch,
            "x": self.x,
            "y": self.y,
            "L": dict(self.L),
            "H": dict(self.H),
            "hbands": {index: dict(poly) for index, poly in hbands.items()},
            "pbands": {index: dict(poly) for index, poly in pbands.items()},
            "h": dict(h),
            "beta": dict(beta),
            "tau": dict(tau),
            "chi": dict(chi),
            "qbands": {index: dict(poly) for index, poly in q.items()},
            "theta": dict(theta),
            "mu": mu,
            "mu_inv": mi,
            "variables": list(self.variables),
            "weights": dict(self.weights),
            "terminal_rows": list(rows_by_stage["terminal"]),
            "formula_controls": controls,
        }
        if self.coordinate_state_only:
            # Sparse follow-on drivers consume the exact coordinate objects
            # above.  Avoid rendering the large solved h/beta reconstruction,
            # reparsing rows, or building unused alpha/rho data.
            den_lcm = math.lcm(1, *self.row_denominators)
            fingerprint_payload = json.dumps(
                {
                    "K": K,
                    "branch": self.branch,
                    "variables": [str(symbol) for symbol in self.variables],
                    "weights": [self.weights[symbol] for symbol in self.variables],
                    "terminal_rows": [
                        (row.label, row.band, row.degree, row.expr)
                        for row in rows_by_stage["terminal"]
                    ],
                    "localizer": "mu*mu_inv-1",
                    "coordinate_state_only": True,
                },
                sort_keys=True,
                separators=(",", ":"),
            )
            return ExplicitChart(
                K=K,
                branch=self.branch,
                variables=[str(symbol) for symbol in self.variables],
                weights=[self.weights[symbol] for symbol in self.variables],
                rows_by_stage=rows_by_stage,
                h="COORDINATE_STATE_ONLY",
                beta="COORDINATE_STATE_ONLY",
                alpha="NOT_BUILT",
                rho="NOT_BUILT",
                theta=singular_expr(cp_expr(theta, self.x, self.y)),
                formula_controls=controls,
                denominator_lcm=den_lcm,
                chart_sha256=sha256_text(fingerprint_payload),
                build_seconds=round(time.monotonic() - started, 6),
            )
        alpha: CoordPoly = {}
        rho: CoordPoly = {}
        if self.through in ("rho", "jacobian"):
            alpha, rho = cp_quoy(cp_mul(beta, beta), h, K)
            if rho and max(j for _i, j in rho) >= K:
                raise AssertionError("quoy remainder did not have y-degree < K")
            controls["QUOY_IDENTITY"] = "PASS_BY_EXACT_DICTIONARY_DIVISION"
            controls["RHO_Y_DEGREE_LT_K"] = max((j for _i, j in rho), default=-1)

            if K == 8:
                rho_forced = cp_add(
                    cp_scale(cp_shift(self.L, 0, 1), sp.Rational(1, 3) * mu**3),
                    cp_scale(tau, mu**2),
                )
                lowest_pinned = 1
            else:
                rho_forced = cp_add(
                    cp_scale(cp_shift(self.L, 0, 2), sp.Rational(1, 3) * mu**3),
                    cp_scale(tau, mu**2),
                    cp_scale(chi, mu),
                )
                lowest_pinned = 1
            rho_difference = cp_add(rho, cp_scale(rho_forced, -1))
            pinned_rho_difference = {
                monomial: coefficient
                for monomial, coefficient in rho_difference.items()
                if sum(monomial) >= lowest_pinned
            }
            rows_by_stage["rho"] = self.rows_from_poly(
                pinned_rho_difference, stage="rho", family="ACTUAL_RHO_MATCH"
            )
            controls["rho_matches_added_through_degree"] = lowest_pinned
            controls["rho_degree_bound"] = K - 6

        if self.through == "jacobian":
            jb_a = cp_add(
                cp_mul(cp_diff(beta, "x"), cp_diff(alpha, "y")),
                cp_scale(cp_mul(cp_diff(beta, "y"), cp_diff(alpha, "x")), -1),
            )
            jh_r = cp_add(
                cp_mul(cp_diff(h, "x"), cp_diff(rho, "y")),
                cp_scale(cp_mul(cp_diff(h, "y"), cp_diff(rho, "x")), -1),
            )
            jacobian = cp_scale(cp_add(jb_a, cp_scale(jh_r, -1)), 3)
            target_seen = (4, 0) in jacobian
            if not target_seen:
                raise AssertionError("the x^4 Jacobian coefficient is absent")
            jacobian_rows_poly = dict(jacobian)
            jacobian_rows_poly[(4, 0)] = jacobian_rows_poly[(4, 0)] - 1
            rows_by_stage["jacobian"] = self.rows_from_poly(
                jacobian_rows_poly, stage="jacobian", family="FULL_ID6_CST1"
            )
            controls["ID6_formula"] = "3*(J(beta,alpha)-J(h,rho))"
            controls["CST_equation"] = "coeff_x4(J)-1"
            controls["all_other_J_coefficients_zero"] = True

        # Every emitted row denominator was recorded before its integral
        # clearing in rows_from_poly.  Do not parse the (potentially very
        # large) rendered strings back through SymPy merely to rediscover it.
        den_lcm = math.lcm(1, *self.row_denominators)
        x, y = self.x, self.y
        reconstruction = {
            "h": singular_expr(cp_expr(h, x, y)),
            "beta": singular_expr(cp_expr(beta, x, y)),
            "alpha": singular_expr(cp_expr(alpha, x, y)) if alpha else "NOT_BUILT",
            "rho": singular_expr(cp_expr(rho, x, y)) if rho else "NOT_BUILT",
            "theta": singular_expr(cp_expr(theta, x, y)),
        }
        fingerprint_payload = json.dumps(
            {
                "K": K,
                "branch": self.branch,
                "variables": [str(symbol) for symbol in self.variables],
                "weights": [self.weights[symbol] for symbol in self.variables],
                "rows": [
                    (stage, row.label, row.degree, row.expr)
                    for stage, stage_rows in rows_by_stage.items()
                    for row in stage_rows
                ],
                "localizer": singular_expr(mu * mi - 1),
            },
            sort_keys=True,
            separators=(",", ":"),
        )
        return ExplicitChart(
            K=K,
            branch=self.branch,
            variables=[str(symbol) for symbol in self.variables],
            weights=[self.weights[symbol] for symbol in self.variables],
            rows_by_stage=rows_by_stage,
            h=reconstruction["h"],
            beta=reconstruction["beta"],
            alpha=reconstruction["alpha"],
            rho=reconstruction["rho"],
            theta=reconstruction["theta"],
            formula_controls=controls,
            denominator_lcm=den_lcm,
            chart_sha256=sha256_text(fingerprint_payload),
            build_seconds=round(time.monotonic() - started, 6),
        )


def ordered_ring(chart: ExplicitChart, characteristic: int) -> tuple[str, list[str], list[int]]:
    pairs = sorted(
        zip(chart.variables, chart.weights), key=lambda item: (-item[1], item[0])
    )
    names = [name for name, _weight in pairs]
    weights = [weight for _name, weight in pairs]
    ring = f"ring SS={characteristic},({','.join(names)}),wp({','.join(str(w) for w in weights)});"
    return ring, names, weights


def emit_chart(chart: ExplicitChart, output_dir: Path, characteristic: int) -> dict[str, Any]:
    if characteristic and chart.denominator_lcm % characteristic == 0:
        raise ValueError(f"bad prime {characteristic} divides denominator lcm")
    ring, names, weights = ordered_ring(chart, characteristic)
    rows = chart.rows_through("jacobian")
    config = BandEmitConfig(
        output_dir=output_dir,
        ring=ring,
        option_lines=("option(redSB);", "short=0;"),
        global_generators=(("mu_localizer", "mu*mu_inv-1"),),
        manifest_name="bands-manifest.json",
    )
    manifest = emit_staged_band_files(rows, config)
    metadata = chart.metadata()
    metadata.update(
        {
            "characteristic": characteristic,
            "solver_ring": ring,
            "solver_variables": names,
            "solver_weights": weights,
            "band_manifest": manifest["manifest_path"],
            "generator_union_checksum": manifest["generator_union_checksum"],
        }
    )
    atomic_write(output_dir / "explicit-chart.json", json.dumps(metadata, indent=2, sort_keys=True) + "\n")
    return manifest


def summarize(result: GuidedGBResult) -> dict[str, Any]:
    runs = result.certificate["runs"]
    return {
        "verdict": result.verdict.value,
        "promotion_note": result.certificate["promotion_note"],
        "accepted_run_count": result.certificate["accepted_run_count"],
        "runs": [
            {
                "characteristic": run["characteristic"],
                "returncode": run["returncode"],
                "timed_out": run["timed_out"],
                "elapsed_seconds": run["elapsed_seconds"],
                "unit": run["main"]["unit"],
                "dimension": run["main"]["dimension"],
                "vdim": run["main"]["vdim"],
                "basis_size": run["main"]["basis_size"],
                "nf_all_zero": run["main"]["nf_all_zero"],
                "accepted": run["main"]["accepted"],
                "missing_markers": run["main"]["missing_markers"],
                "script": run["script"],
                "stdout": run["stdout"],
            }
            for run in runs
        ],
    }


def run_one_prefix(
    chart: ExplicitChart,
    stage: str,
    characteristic: int,
    output_dir: Path,
    timeout: int,
) -> GuidedGBResult:
    ring, names, _weights = ordered_ring(chart, characteristic)
    rows = chart.rows_through(stage)
    generators = [row.expr for row in rows] + ["mu*mu_inv-1"]
    system = SingularSystem(
        name=f"K{chart.K}_{chart.branch}_{stage}_p{characteristic}",
        prelude="\n".join(("option(redSB); short=0;", ring, 'print("EXPLICIT__PRELUDE_DONE 1");')),
        generators=tuple(generators),
        characteristic=characteristic,
        variables=tuple(names),
        homogeneous=False,
        positive_weights=(),
        metadata={
            "K": chart.K,
            "branch": chart.branch,
            "stage": stage,
            "row_count_without_localizer": len(rows),
            "chart_sha256": chart.chart_sha256,
            "inhomogeneous_localization": True,
            "CST1_included": stage == "jacobian",
        },
    )
    return guided_groebner(
        system,
        hint=None,
        policy=PromotionPolicy.exact_q(
            "inhomogeneous explicit lower-band chart; modular units are F_p-only"
        ),
        config=RunConfig(
            output_dir=output_dir,
            timeout_seconds=timeout,
            total_cores=1,
            max_parallel_jobs=1,
            run_perturbed_control=False,
            no_rc=True,
        ),
    )


def run_stages(
    chart: ExplicitChart,
    tag: str,
    primes: Sequence[int],
    timeout: int,
    start_stage: str,
    through: str,
    exact_confirm: bool,
) -> dict[str, Any]:
    if not 1 <= timeout <= MAX_TIMEOUT:
        raise ValueError(f"timeout must lie in [1,{MAX_TIMEOUT}]")
    for prime in primes:
        if prime in (2, 3) or chart.denominator_lcm % prime == 0:
            raise ValueError(f"bad prime {prime}")
    base = RUNS / tag
    emit_chart(chart, base / "emitted_Q", 0)
    for prime in primes:
        emit_chart(chart, base / f"emitted_p{prime}", prime)

    order = ("terminal", "rho", "jacobian")
    startpoint = order.index(start_stage)
    endpoint = order.index(through)
    if startpoint > endpoint:
        raise ValueError("start stage follows terminal stage")
    stage_summaries: list[dict[str, Any]] = []
    exact_result: dict[str, Any] | None = None
    first_all_prime_unit: dict[str, Any] | None = None
    started = time.monotonic()
    for stage in order[startpoint : endpoint + 1]:
        prime_results: list[dict[str, Any]] = []
        for prime in primes:
            result = run_one_prefix(
                chart,
                stage,
                prime,
                base / "modular" / stage / f"p{prime}",
                timeout,
            )
            prime_results.append(summarize(result))
            atomic_write(
                base / "stage-progress.json",
                json.dumps(stage_summaries + [{"stage": stage, "prime_results": prime_results}], indent=2, sort_keys=True)
                + "\n",
            )
        runs = [item for summary in prime_results for item in summary["runs"]]
        all_prime_unit = bool(runs) and len(runs) == len(primes) and all(
            run["characteristic"] > 0
            and run["returncode"] == 0
            and not run["timed_out"]
            and run["unit"]
            and run["nf_all_zero"]
            and not run["missing_markers"]
            for run in runs
        )
        stage_summary = {
            "stage": stage,
            "cumulative_row_count": len(chart.rows_through(stage)),
            "prime_results": prime_results,
            "all_requested_primes_unit": all_prime_unit,
            "modular_scope": "F_p-only",
        }
        stage_summaries.append(stage_summary)
        atomic_write(base / "stage-progress.json", json.dumps(stage_summaries, indent=2, sort_keys=True) + "\n")
        if all_prime_unit:
            first_all_prime_unit = {
                "stage": stage,
                "primes": list(primes),
                "status": "UNIT_IN_EVERY_REQUESTED_FIBRE__FP_ONLY",
            }
            if exact_confirm:
                exact = run_one_prefix(chart, stage, 0, base / "exact" / stage, timeout)
                exact_result = {"stage": stage, **summarize(exact)}
            break

    verdict = "OPEN"
    if exact_result is not None:
        verdict = exact_result["verdict"]
    elif first_all_prime_unit is not None:
        verdict = "MODULAR_ONLY"
    elif any(
        run["timed_out"]
        for stage in stage_summaries
        for result in stage["prime_results"]
        for run in result["runs"]
    ):
        verdict = "INCONCLUSIVE_TIMEOUT"
    summary = {
        "type": "K4RAY-EXPLICIT-STAGED-GUIDED-GB",
        "tag": tag,
        "K": chart.K,
        "branch": chart.branch,
        "chart_sha256": chart.chart_sha256,
        "primes": list(primes),
        "per_call_timeout_seconds": timeout,
        "total_cores": 1,
        "stage_summaries": stage_summaries,
        "first_all_prime_unit": first_all_prime_unit,
        "exact_result": exact_result,
        "verdict": verdict,
        "elapsed_seconds": round(time.monotonic() - started, 6),
        "no_modular_promotion": True,
    }
    atomic_write(base / "summary.json", json.dumps(summary, indent=2, sort_keys=True) + "\n")
    return summary


def parse_primes(text: str) -> tuple[int, ...]:
    return tuple(int(piece) for piece in text.split(",") if piece)


def normalized_branch(K: int, branch: str | None) -> str:
    if K == 8:
        return "single"
    if branch not in ("A", "B"):
        raise ValueError("K=9 requires --branch A or --branch B")
    return branch


def command_build(args: argparse.Namespace) -> None:
    branch = normalized_branch(args.K, args.branch)
    chart = ChartBuilder(args.K, branch, args.through).build()
    out = RUNS / args.tag / "build"
    atomic_write(out / "explicit-chart.json", json.dumps(chart.metadata(), indent=2, sort_keys=True) + "\n")
    emit_chart(chart, out / "emitted_Q", 0)
    print(
        json.dumps(
            {
                "K": chart.K,
                "branch": chart.branch,
                "variables": len(chart.variables),
                "row_counts": {key: len(value) for key, value in chart.rows_by_stage.items()},
                "denominator_lcm": chart.denominator_lcm,
                "chart_sha256": chart.chart_sha256,
                "build_seconds": chart.build_seconds,
                "metadata": str(out / "explicit-chart.json"),
            },
            sort_keys=True,
        )
    )


def command_run(args: argparse.Namespace) -> None:
    branch = normalized_branch(args.K, args.branch)
    chart = ChartBuilder(args.K, branch, args.through).build()
    summary = run_stages(
        chart,
        args.tag,
        parse_primes(args.primes),
        args.timeout,
        args.start_stage,
        args.through,
        args.exact_confirm,
    )
    print(
        json.dumps(
            {
                "tag": args.tag,
                "K": args.K,
                "branch": branch,
                "verdict": summary["verdict"],
                "summary": str(RUNS / args.tag / "summary.json"),
            },
            sort_keys=True,
        )
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    for name in ("build", "run"):
        sub = subparsers.add_parser(name)
        sub.add_argument("tag")
        sub.add_argument("K", type=int, choices=(8, 9))
        sub.add_argument("--branch", choices=("A", "B"))
        sub.add_argument("--through", choices=("terminal", "rho", "jacobian"), default="jacobian")
        if name == "run":
            sub.add_argument("--primes", default=",".join(str(prime) for prime in GOOD_PRIMES))
            sub.add_argument("--timeout", type=int, default=600)
            sub.add_argument(
                "--start-stage", choices=("terminal", "rho", "jacobian"), default="terminal"
            )
            sub.add_argument("--exact-confirm", action="store_true")
            sub.set_defaults(handler=command_run)
        else:
            sub.set_defaults(handler=command_build)
    args = parser.parse_args()
    args.handler(args)


if __name__ == "__main__":
    main()
