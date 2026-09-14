#!/usr/bin/env python3
"""Exact lower-band reduction and staged guided-GB driver for the k=4 ray.

This driver is deliberately separate from the charged ``pinned_chart.py``.
It uses the same chart, but first uses the positive-weight G_m action to set
the nonzero top coefficient ``mu`` to 1 over the algebraic closure.  The
Jacobian coefficient is *not* set to 1 after this normalization; its
nonvanishing is represented by the Rabinowitsch row ``tau*CST-1``.

With ``b=K-2`` put

    H    = y^(K-1)(y-x),
    Btop = 2*y^(K-3)(y-x),
    Atop = 4*y^(K-5)(y-x),
    Rtop = (4/3)*y^(K-7)(y-x).

Writing ``h=H+hlo``, ``B=Btop+Blo`` and ``A=Atop+Alo``, the LEVEL-4
conditions say that every total-degree band >= K-6 of

    DIV = B^2 - A*h - Rtop

vanishes.  From degree ``2K-5`` down to ``K-6`` each newly entering band of
``h,A,B`` occurs linearly with a constant rational matrix.  We row-reduce
those matrices exactly, pivoting h/A variables before B variables.  Pivot
variables are substituted out and only compatibility rows remain.  This is
an isomorphic elimination by equations having nonzero constant pivots, not a
slice or a heuristic pin.

The reduced ID6 Jacobian rows (and, optionally, the K+6 MASTER rows) are
written through ``box.lib.staged_band_emitter``.  Cumulative stage prefixes
are submitted to ``box.lib.guided_gb`` over several good primes.  A modular
unit remains F_p-only; the first modular-killing prefix is automatically
replayed over exact Q when ``--exact-confirm`` is requested.

No process is left running after a timeout.  The core budget is capped at 5.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
from fractions import Fraction
import hashlib
import json
import math
import os
from pathlib import Path
import re
import sys
import time
from typing import Any, Iterable, Mapping, Sequence

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
HERE = ROOT / "box" / "k4rayk89-20260903"
RUNS = HERE / "runs-sol56"
sys.path.insert(0, str(ROOT))

from box.lib.guided_gb import (  # noqa: E402
    GuidedGBResult,
    HilbertHint,
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


MAX_CORES = 5
GOOD_PRIMES_DEFAULT = (32003, 32009, 32027)


def atomic_write(path: Path, payload: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(payload, encoding="utf-8")
    temporary.replace(path)


def sha256_text(payload: str) -> str:
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def singular_expr(expr: sp.Expr) -> str:
    """Stable expanded SymPy expression in Singular syntax."""

    return sp.sstr(sp.expand(expr), order="lex").replace("**", "^")


def rational(value: Any) -> Fraction:
    value = sp.Rational(value)
    return Fraction(int(value.p), int(value.q))


def spq(value: Fraction) -> sp.Rational:
    return sp.Rational(value.numerator, value.denominator)


def monomials(total_max: int) -> list[tuple[int, int]]:
    if total_max < 0:
        return []
    return [
        (i, j)
        for j in range(total_max + 1)
        for i in range(total_max - j + 1)
    ]


def poly_from_terms(
    terms: Mapping[tuple[int, int], sp.Expr], x: sp.Symbol, y: sp.Symbol
) -> sp.Expr:
    return sp.Add(*(coefficient * x**i * y**j for (i, j), coefficient in terms.items()))


def product_coefficient(
    left: Mapping[tuple[int, int], sp.Expr],
    right: Mapping[tuple[int, int], sp.Expr],
    target_i: int,
    target_j: int,
    substitutions: Mapping[sp.Symbol, sp.Expr],
) -> sp.Expr:
    result: sp.Expr = sp.Integer(0)
    for (i, j), coefficient in left.items():
        other = right.get((target_i - i, target_j - j))
        if other is None:
            continue
        coefficient = substitutions.get(coefficient, coefficient) if isinstance(coefficient, sp.Symbol) else coefficient
        other = substitutions.get(other, other) if isinstance(other, sp.Symbol) else other
        result += coefficient * other
    return sp.expand(result)


def resolved_terms(
    terms: Mapping[tuple[int, int], sp.Expr],
    substitutions: Mapping[sp.Symbol, sp.Expr],
) -> dict[tuple[int, int], sp.Expr]:
    return {
        monomial: substitutions.get(coefficient, coefficient)
        if isinstance(coefficient, sp.Symbol)
        else coefficient
        for monomial, coefficient in terms.items()
    }


@dataclass(frozen=True)
class CompatibilityRow:
    label: str
    div_degree: int
    expression: str


@dataclass
class ReductionData:
    K: int
    b: int
    original_variable_count: int
    pivot_count: int
    free_variables: list[str]
    free_weights: list[int]
    compatibility_rows: list[CompatibilityRow]
    band_audit: list[dict[str, Any]]
    substitutions: dict[str, str]
    h: str
    B: str
    A: str
    R: str
    target_coefficient: str
    rows: list[BandRow]
    denominator_lcm: int
    theorem_cut: bool
    chart_sha256: str = ""

    def metadata_json(self) -> dict[str, Any]:
        payload = {
            "type": "K4RAY-HENSEL-REDUCED-CHART",
            "K": self.K,
            "b": self.b,
            "normalization": {
                "top_beta": "y^(K-3)*(y-x)",
                "mu": 1,
                "scope": "G_m normalization over the algebraic closure; valid because charged mu is nonzero",
                "target_localization": "tau*CST-1",
            },
            "original_variable_count": self.original_variable_count,
            "pivot_count": self.pivot_count,
            "free_variable_count_before_tau_lambda": len(self.free_variables),
            "free_variables": self.free_variables,
            "free_weights": self.free_weights,
            "compatibility_rows": [asdict(row) for row in self.compatibility_rows],
            "band_audit": self.band_audit,
            "substitutions": self.substitutions,
            "reconstruction": {"h": self.h, "B": self.B, "A": self.A, "R": self.R},
            "target_coefficient": self.target_coefficient,
            "row_count": len(self.rows),
            "denominator_lcm": self.denominator_lcm,
            "theorem_cut": self.theorem_cut,
            "chart_sha256": self.chart_sha256,
        }
        return payload


def exact_rref_with_transform(
    matrix: Sequence[Sequence[Fraction]],
) -> tuple[list[list[Fraction]], list[list[Fraction]], list[int]]:
    """Return RREF, its left row-operation matrix, and pivot columns."""

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
            (row for row in range(pivot_row, row_count) if work[row][column]),
            None,
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
            if row == pivot_row or not work[row][column]:
                continue
            multiple = work[row][column]
            work[row] = [
                entry - multiple * pivot_entry
                for entry, pivot_entry in zip(work[row], work[pivot_row])
            ]
            transform[row] = [
                entry - multiple * pivot_entry
                for entry, pivot_entry in zip(transform[row], transform[pivot_row])
            ]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == row_count:
            break
    return work, transform, pivots


def transform_vector(
    transform: Sequence[Sequence[Fraction]], vector: Sequence[sp.Expr]
) -> list[sp.Expr]:
    return [
        sp.expand(sum((spq(coefficient) * entry for coefficient, entry in zip(row, vector)), sp.Integer(0)))
        for row in transform
    ]


def coefficient_rows(expr: sp.Expr, x: sp.Symbol, y: sp.Symbol) -> list[tuple[int, int, sp.Expr]]:
    polynomial = sp.Poly(sp.expand(expr), x, y)
    out: list[tuple[int, int, sp.Expr]] = []
    for (i, j), coefficient in polynomial.terms():
        coefficient = sp.expand(coefficient)
        if coefficient != 0:
            out.append((int(i), int(j), coefficient))
    return out


def denominator_lcm(expressions: Iterable[sp.Expr]) -> int:
    value = 1
    for expr in expressions:
        for coefficient in sp.Poly(sp.expand(expr)).coeffs():
            _numerator, denominator = sp.fraction(coefficient)
            if denominator.is_Integer:
                value = math.lcm(value, abs(int(denominator)))
    return value


def build_reduced_chart(K: int, theorem_cut: bool = False) -> ReductionData:
    if K < 7:
        raise ValueError("the LEVEL-4 normalized Hensel chart requires K>=7")
    b = K - 2
    rdeg = K - 6
    x, y = sp.symbols("x y")

    h_terms: dict[tuple[int, int], sp.Expr] = {(0, K): sp.Integer(1), (1, K - 1): sp.Integer(-1)}
    B_terms: dict[tuple[int, int], sp.Expr] = {(0, K - 2): sp.Integer(2), (1, K - 3): sp.Integer(-2)}
    A_terms: dict[tuple[int, int], sp.Expr] = {(0, K - 4): sp.Integer(4), (1, K - 5): sp.Integer(-4)}
    symbols_by_kind_degree: dict[tuple[str, int], list[sp.Symbol]] = {}
    symbol_weights: dict[sp.Symbol, int] = {}

    def add_lower(kind: str, maximum: int, terms: dict[tuple[int, int], sp.Expr]) -> None:
        for i, j in monomials(maximum):
            if kind == "h" and (i, j) == (0, K - 1):
                continue
            symbol = sp.Symbol(f"{kind}_{i}_{j}" if kind != "B" else f"B_{i}_{j}")
            terms[(i, j)] = symbol
            symbols_by_kind_degree.setdefault((kind, i + j), []).append(symbol)
            if kind == "h":
                symbol_weights[symbol] = K - i - j
            elif kind == "B":
                symbol_weights[symbol] = 2 * K - i - j
            else:
                symbol_weights[symbol] = 3 * K - i - j

    add_lower("h", K - 1, h_terms)
    add_lower("B", K - 3, B_terms)
    add_lower("A", K - 5, A_terms)

    all_symbols = [
        coefficient
        for terms in (h_terms, A_terms, B_terms)
        for coefficient in terms.values()
        if isinstance(coefficient, sp.Symbol)
    ]
    substitutions: dict[sp.Symbol, sp.Expr] = {}
    compatibility: list[CompatibilityRow] = []
    compatibility_exprs: list[sp.Expr] = []
    band_audit: list[dict[str, Any]] = []

    def target_r(i: int, j: int) -> sp.Expr:
        if (i, j) == (0, K - 6):
            return sp.Rational(4, 3)
        if (i, j) == (1, K - 7):
            return sp.Rational(-4, 3)
        return sp.Integer(0)

    for degree in range(2 * K - 5, rdeg - 1, -1):
        new_variables: list[sp.Symbol] = []
        # Constant-column RREF pivots earlier columns first.  This ordering
        # eliminates h/A preferentially and preserves B as free coordinates.
        for kind, component_degree in (
            ("h", degree - (K - 4)),
            ("A", degree - K),
            ("B", degree - (K - 2)),
        ):
            new_variables.extend(symbols_by_kind_degree.get((kind, component_degree), []))
        new_variables = [variable for variable in new_variables if variable not in substitutions]

        equations: list[sp.Expr] = []
        for i in range(degree + 1):
            j = degree - i
            equation = (
                product_coefficient(B_terms, B_terms, i, j, substitutions)
                - product_coefficient(A_terms, h_terms, i, j, substitutions)
                - target_r(i, j)
            )
            equations.append(sp.expand(equation))

        zero_new = {variable: sp.Integer(0) for variable in new_variables}
        matrix: list[list[Fraction]] = []
        right: list[sp.Expr] = []
        for equation in equations:
            coefficients = [sp.expand(equation).coeff(variable) for variable in new_variables]
            rest = sp.expand(equation.xreplace(zero_new))
            reconstructed = sp.expand(
                rest + sum((coefficient * variable for coefficient, variable in zip(coefficients, new_variables)), sp.Integer(0))
            )
            if sp.expand(equation - reconstructed) != 0:
                raise AssertionError(f"DIV band {degree} is not linear in its entering variables")
            if any(coefficient.free_symbols for coefficient in coefficients):
                raise AssertionError(f"DIV band {degree} has a nonconstant pivot matrix")
            matrix.append([rational(coefficient) for coefficient in coefficients])
            right.append(-rest)

        rref, transform, pivots = exact_rref_with_transform(matrix)
        transformed_right = transform_vector(transform, right)
        free_columns = [column for column in range(len(new_variables)) if column not in pivots]
        for row, pivot_column in enumerate(pivots):
            expression = transformed_right[row]
            for column in free_columns:
                if rref[row][column]:
                    expression -= spq(rref[row][column]) * new_variables[column]
            substitutions[new_variables[pivot_column]] = sp.expand(expression)

        band_compatibility = 0
        for row in range(len(pivots), len(equations)):
            if any(rref[row]):
                raise AssertionError("RREF zero-row accounting failed")
            expression = sp.expand(transformed_right[row])
            if expression == 0:
                continue
            label = f"DIV_d{degree}_c{band_compatibility}"
            compatibility.append(CompatibilityRow(label, degree, singular_expr(expression)))
            compatibility_exprs.append(expression)
            band_compatibility += 1
        band_audit.append(
            {
                "div_degree": degree,
                "equation_count": len(equations),
                "entering_variables": [str(variable) for variable in new_variables],
                "rank": len(pivots),
                "pivot_variables": [str(new_variables[column]) for column in pivots],
                "free_entering_variables": [str(new_variables[column]) for column in free_columns],
                "compatibility_count": band_compatibility,
            }
        )

    free_symbols = [symbol for symbol in all_symbols if symbol not in substitutions]
    h_expr = sp.expand(poly_from_terms(resolved_terms(h_terms, substitutions), x, y))
    B_expr = sp.expand(poly_from_terms(resolved_terms(B_terms, substitutions), x, y))
    A_expr = sp.expand(poly_from_terms(resolved_terms(A_terms, substitutions), x, y))
    R_expr = sp.expand(B_expr**2 - A_expr * h_expr)

    # The band RREF above is the construction control: every coefficient is
    # either solved by a pivot or retained as a compatibility row.  The old
    # check tested coefficient_rows (which deliberately omits zeros) for zero
    # coefficients and was therefore vacuous.

    JJ = sp.expand(
        sp.Rational(3, 8) * (sp.diff(B_expr, x) * sp.diff(A_expr, y) - sp.diff(B_expr, y) * sp.diff(A_expr, x))
        - sp.Rational(3, 4) * (sp.diff(h_expr, x) * sp.diff(R_expr, y) - sp.diff(h_expr, y) * sp.diff(R_expr, x))
    )
    jacobian_coefficients = coefficient_rows(JJ, x, y)
    target = sp.Integer(0)
    rows: list[BandRow] = []
    stage_index = 0

    for item, expression in zip(compatibility, compatibility_exprs):
        rows.append(
            BandRow(
                label=item.label,
                band=f"s{stage_index:03d}_DIV_d{item.div_degree:03d}",
                degree=item.div_degree,
                expr=singular_expr(expression),
                source={"kind": "DIV_COMPAT", "xy_degree": item.div_degree, "stage_index": stage_index},
            )
        )
        stage_index += 1

    grouped_j: dict[int, list[tuple[int, int, sp.Expr]]] = {}
    for i, j, coefficient in jacobian_coefficients:
        if (i, j) == (4, 0):
            target = coefficient
        else:
            grouped_j.setdefault(i + j, []).append((i, j, coefficient))
    if target == 0:
        raise AssertionError("the x^4 Jacobian target coefficient vanished identically")
    for degree in sorted(grouped_j, reverse=True):
        for row_number, (i, j, coefficient) in enumerate(grouped_j[degree]):
            rows.append(
                BandRow(
                    label=f"J_d{degree}_x{i}_y{j}",
                    band=f"s{stage_index:03d}_J_d{degree:03d}",
                    degree=degree,
                    expr=singular_expr(coefficient),
                    source={
                        "kind": "ID6_J",
                        "xy_degree": degree,
                        "x_power": i,
                        "y_power": j,
                        "stage_index": stage_index,
                        "row_in_band": row_number,
                    },
                )
            )
        stage_index += 1

    if theorem_cut:
        lam = sp.Symbol("lam")
        f_expr = sp.expand(h_expr**2 + B_expr)
        E64 = sp.expand(8 * B_expr**3 - 48 * R_expr * h_expr**2 - 72 * B_expr * R_expr + 9 * A_expr**2 - lam * f_expr)
        grouped_e: dict[int, list[tuple[int, int, sp.Expr]]] = {}
        for i, j, coefficient in coefficient_rows(E64, x, y):
            if i + j > K + 6:
                grouped_e.setdefault(i + j, []).append((i, j, coefficient))
        # MASTER rows are strong; put them immediately after DIV compatibility
        # in a future run by retaining their explicit stage/source metadata.
        for degree in sorted(grouped_e, reverse=True):
            for row_number, (i, j, coefficient) in enumerate(grouped_e[degree]):
                rows.append(
                    BandRow(
                        label=f"E_d{degree}_x{i}_y{j}",
                        band=f"s{stage_index:03d}_E_d{degree:03d}",
                        degree=degree,
                        expr=singular_expr(coefficient),
                        source={
                            "kind": "MASTER_E64",
                            "xy_degree": degree,
                            "x_power": i,
                            "y_power": j,
                            "stage_index": stage_index,
                            "row_in_band": row_number,
                        },
                    )
                )
            stage_index += 1
        free_symbols.append(lam)
        symbol_weights[lam] = 4 * K

    expressions_for_denominators = compatibility_exprs + [
        sp.sympify(row.expr.replace("^", "**")) for row in rows if row.source.get("kind") != "DIV_COMPAT"
    ] + [target]
    den_lcm = denominator_lcm(expressions_for_denominators)
    chart_fingerprint_payload = json.dumps(
        {
            "K": K,
            "theorem_cut": theorem_cut,
            "free": [str(symbol) for symbol in free_symbols],
            "rows": [(row.label, row.band, row.degree, row.expr) for row in rows],
            "target": singular_expr(target),
        },
        sort_keys=True,
        separators=(",", ":"),
    )
    data = ReductionData(
        K=K,
        b=b,
        original_variable_count=len(all_symbols),
        pivot_count=len(substitutions),
        free_variables=[str(symbol) for symbol in free_symbols],
        free_weights=[symbol_weights[symbol] for symbol in free_symbols],
        compatibility_rows=compatibility,
        band_audit=band_audit,
        substitutions={str(symbol): singular_expr(expression) for symbol, expression in substitutions.items()},
        h=singular_expr(h_expr),
        B=singular_expr(B_expr),
        A=singular_expr(A_expr),
        R=singular_expr(R_expr),
        target_coefficient=singular_expr(target),
        rows=rows,
        denominator_lcm=den_lcm,
        theorem_cut=theorem_cut,
        chart_sha256=sha256_text(chart_fingerprint_payload),
    )
    return data


def ordered_variables(data: ReductionData, strategy: str) -> tuple[list[str], list[int]]:
    pairs = list(zip(data.free_variables, data.free_weights))
    if strategy == "native":
        pass
    elif strategy == "reverse":
        pairs.reverse()
    elif strategy == "weight-asc":
        pairs.sort(key=lambda item: (item[1], item[0]))
    elif strategy == "weight-desc":
        pairs.sort(key=lambda item: (-item[1], item[0]))
    else:
        raise ValueError(f"unknown tie-order strategy {strategy!r}")
    # tau is an inhomogeneous localization variable and is deliberately last.
    names = [name for name, _weight in pairs] + ["tau"]
    weights = [weight for _name, weight in pairs] + [1]
    return names, weights


def solver_ring(data: ReductionData, characteristic: int, strategy: str) -> tuple[str, list[str], list[int]]:
    names, weights = ordered_variables(data, strategy)
    return (
        f"ring SS={characteristic},({','.join(names)}),wp({','.join(str(weight) for weight in weights)});",
        names,
        weights,
    )


def emit_chart(data: ReductionData, output_dir: Path, characteristic: int, strategy: str) -> dict[str, Any]:
    if characteristic in (2, 3) or (characteristic and data.denominator_lcm % characteristic == 0):
        raise ValueError(
            f"characteristic {characteristic} is bad for denominator lcm {data.denominator_lcm}"
        )
    ring, names, weights = solver_ring(data, characteristic, strategy)
    globals_ = (("target_localization", f"tau*({data.target_coefficient})-1"),)
    config = BandEmitConfig(
        output_dir=output_dir,
        ring=ring,
        option_lines=("option(redSB);", "short=0;"),
        global_generators=globals_,
        manifest_name="bands-manifest.json",
    )
    manifest = emit_staged_band_files(data.rows, config)
    chart_payload = data.metadata_json()
    chart_payload.update(
        {
            "characteristic": characteristic,
            "tie_order": strategy,
            "solver_variables": names,
            "solver_weights": weights,
            "solver_ring": ring,
            "band_manifest": manifest["manifest_path"],
            "band_union_checksum": manifest["generator_union_checksum"],
        }
    )
    atomic_write(output_dir / "reduced-chart.json", json.dumps(chart_payload, indent=2, sort_keys=True) + "\n")
    return {"manifest": manifest, "chart": chart_payload}


def stage_groups(rows: Sequence[BandRow]) -> list[tuple[str, list[BandRow]]]:
    groups: list[tuple[str, list[BandRow]]] = []
    by_band: dict[str, list[BandRow]] = {}
    order: list[str] = []
    for row in rows:
        if row.band not in by_band:
            order.append(row.band)
            by_band[row.band] = []
        by_band[row.band].append(row)
    for band in order:
        groups.append((band, by_band[band]))
    return groups


def load_hint(path: Path | None, stage: str, weights: Sequence[int]) -> HilbertHint | None:
    if path is None:
        return None
    payload = json.loads(path.read_text(encoding="utf-8"))
    if "stages" in payload:
        selected = payload["stages"].get(stage)
        if selected is None:
            return None
    else:
        selected = payload
    hint_weights = tuple(int(value) for value in selected.get("weights", weights))
    if len(hint_weights) != len(weights):
        raise ValueError(f"Hilbert weights for {stage} have the wrong length")
    return HilbertHint(
        tuple(int(value) for value in selected["numerator"]),
        hint_weights,
        None if selected.get("predicted_length") is None else int(selected["predicted_length"]),
    )


def summarize_guided(result: GuidedGBResult) -> dict[str, Any]:
    return {
        "verdict": result.verdict.value,
        "promotion_note": result.certificate["promotion_note"],
        "accepted_run_count": result.certificate["accepted_run_count"],
        "crt_rational_reconstruction": result.certificate["crt_rational_reconstruction"],
        "runs": [
            {
                "label": run["label"],
                "characteristic": run["characteristic"],
                "timed_out": run["timed_out"],
                "returncode": run["returncode"],
                "elapsed_seconds": run["elapsed_seconds"],
                "unit": run["main"]["unit"],
                "dimension": run["main"]["dimension"],
                "vdim": run["main"]["vdim"],
                "basis_size": run["main"]["basis_size"],
                "nf_all_zero": run["main"]["nf_all_zero"],
                "accepted": run["main"]["accepted"],
                "missing_markers": run["main"]["missing_markers"],
                "script": run["script"],
                "script_sha256": run["script_sha256"],
                "stdout": run["stdout"],
                "stdout_sha256": run["stdout_sha256"],
            }
            for run in result.certificate["runs"]
        ],
    }


def run_prefix(
    data: ReductionData,
    rows: Sequence[BandRow],
    characteristics: Sequence[int],
    output_dir: Path,
    strategy: str,
    timeout: int,
    cores: int,
    hint_path: Path | None,
    stage_label: str,
) -> GuidedGBResult:
    systems: list[SingularSystem] = []
    hint: HilbertHint | None = None
    for characteristic in characteristics:
        ring, names, weights = solver_ring(data, characteristic, strategy)
        if hint is None:
            hint = load_hint(hint_path, stage_label, weights)
        generators = [row.expr for row in rows]
        generators.append(f"tau*({data.target_coefficient})-1")
        systems.append(
            SingularSystem(
                name=f"K{data.K}_{stage_label}_{strategy}_p{characteristic}",
                prelude="\n".join(("option(redSB); short=0;", ring, 'print("K89__REDUCED_PRELUDE 1");')),
                generators=tuple(generators),
                characteristic=characteristic,
                variables=tuple(names),
                homogeneous=False,
                positive_weights=(),
                metadata={
                    "K": data.K,
                    "b": data.b,
                    "stage": stage_label,
                    "row_count_without_localizer": len(rows),
                    "chart_sha256": data.chart_sha256,
                    "tie_order": strategy,
                    "inhomogeneous_localization": True,
                },
            )
        )
    return guided_groebner(
        systems,
        hint=hint,
        policy=PromotionPolicy.exact_q(
            "mu-normalized inhomogeneous k4-ray chart; modular units are never promoted"
        ),
        config=RunConfig(
            output_dir=output_dir,
            timeout_seconds=timeout,
            total_cores=cores,
            max_parallel_jobs=min(len(systems), cores),
            run_perturbed_control=False,
            no_rc=True,
        ),
    )


def run_staged(
    data: ReductionData,
    tag: str,
    primes: Sequence[int],
    strategy: str,
    timeout: int,
    cores: int,
    stage_batch: int,
    start_stage: int,
    stop_stage: int | None,
    hint_path: Path | None,
    exact_confirm: bool,
    final_exact: bool,
) -> dict[str, Any]:
    if not (1 <= cores <= MAX_CORES):
        raise ValueError(f"cores must be in [1,{MAX_CORES}]")
    if stage_batch < 1:
        raise ValueError("stage_batch must be positive")
    for prime in primes:
        if prime in (2, 3) or data.denominator_lcm % prime == 0:
            raise ValueError(f"bad prime {prime} divides 6 or denominator lcm {data.denominator_lcm}")

    base = RUNS / tag
    for characteristic in [0, *primes]:
        emit_chart(data, base / f"emitted_p{characteristic}_{strategy}", characteristic, strategy)

    groups = stage_groups(data.rows)
    endpoints = list(range(stage_batch - 1, len(groups), stage_batch))
    if not endpoints or endpoints[-1] != len(groups) - 1:
        endpoints.append(len(groups) - 1)
    endpoints = [endpoint for endpoint in endpoints if endpoint >= start_stage]
    if stop_stage is not None:
        endpoints = [endpoint for endpoint in endpoints if endpoint <= stop_stage]
    stage_results: list[dict[str, Any]] = []
    modular_kill: dict[str, Any] | None = None
    exact_result: dict[str, Any] | None = None
    started = time.monotonic()

    for endpoint in endpoints:
        prefix_rows = [row for _band, band_rows in groups[: endpoint + 1] for row in band_rows]
        stage_label = f"stage{endpoint:03d}_{groups[endpoint][0]}"
        result = run_prefix(
            data,
            prefix_rows,
            primes,
            base / "modular" / stage_label,
            strategy,
            timeout,
            cores,
            hint_path,
            stage_label,
        )
        summary = {
            "stage_index": endpoint,
            "stage_label": stage_label,
            "last_band": groups[endpoint][0],
            "cumulative_row_count": len(prefix_rows),
            **summarize_guided(result),
        }
        stage_results.append(summary)
        atomic_write(base / "stage-progress.json", json.dumps(stage_results, indent=2, sort_keys=True) + "\n")
        runs = summary["runs"]
        if runs and all(
            run["characteristic"] > 0
            and run["returncode"] == 0
            and not run["timed_out"]
            and run["unit"]
            and run["nf_all_zero"]
            for run in runs
        ):
            modular_kill = {
                "stage_index": endpoint,
                "stage_label": stage_label,
                "cumulative_row_count": len(prefix_rows),
                "primes": list(primes),
                "status": "UNIT_IN_EVERY_REQUESTED_FIBRE__FP_ONLY",
            }
            if exact_confirm:
                exact = run_prefix(
                    data,
                    prefix_rows,
                    (0,),
                    base / "exact" / stage_label,
                    strategy,
                    timeout,
                    cores,
                    hint_path,
                    stage_label,
                )
                exact_result = {
                    "reason": "first all-prime modular-unit prefix",
                    "stage_index": endpoint,
                    "stage_label": stage_label,
                    "cumulative_row_count": len(prefix_rows),
                    **summarize_guided(exact),
                }
            break

    if final_exact and exact_result is None and groups:
        endpoint = len(groups) - 1 if stop_stage is None else min(stop_stage, len(groups) - 1)
        prefix_rows = [row for _band, band_rows in groups[: endpoint + 1] for row in band_rows]
        stage_label = f"stage{endpoint:03d}_{groups[endpoint][0]}"
        exact = run_prefix(
            data,
            prefix_rows,
            (0,),
            base / "exact-final" / stage_label,
            strategy,
            timeout,
            cores,
            hint_path,
            stage_label,
        )
        exact_result = {
            "reason": "explicit final exact-Q request",
            "stage_index": endpoint,
            "stage_label": stage_label,
            "cumulative_row_count": len(prefix_rows),
            **summarize_guided(exact),
        }

    verdict = "OPEN"
    if exact_result is not None:
        verdict = exact_result["verdict"]
    elif modular_kill is not None:
        verdict = "MODULAR_ONLY"
    elif stage_results and any(
        run["timed_out"] for stage in stage_results for run in stage["runs"]
    ):
        verdict = "INCONCLUSIVE_TIMEOUT"
    summary = {
        "type": "K4RAY-STAGED-GUIDED-GB",
        "tag": tag,
        "K": data.K,
        "b": data.b,
        "chart_sha256": data.chart_sha256,
        "theorem_cut": data.theorem_cut,
        "tie_order": strategy,
        "primes": list(primes),
        "per_call_timeout_seconds": timeout,
        "total_cores": cores,
        "stage_batch": stage_batch,
        "stage_group_count": len(groups),
        "stage_results": stage_results,
        "modular_kill": modular_kill,
        "exact_result": exact_result,
        "verdict": verdict,
        "fallacy_v2": {
            "modular_unit_scope": "F_p-only until exact-Q confirmation",
            "posdim_scope": "not a counterexample; extract a point and test J exactly",
            "inhomogeneous_localization": "tau*CST-1",
        },
        "elapsed_seconds": round(time.monotonic() - started, 6),
    }
    atomic_write(base / "summary.json", json.dumps(summary, indent=2, sort_keys=True) + "\n")
    return summary


def parse_ints(text: str) -> tuple[int, ...]:
    return tuple(int(piece) for piece in text.split(",") if piece)


def command_reduce(args: argparse.Namespace) -> None:
    started = time.monotonic()
    data = build_reduced_chart(args.K, theorem_cut=args.theorem)
    out = RUNS / args.tag / "reduction"
    atomic_write(out / "reduced-chart.json", json.dumps(data.metadata_json(), indent=2, sort_keys=True) + "\n")
    summary = {
        "K": data.K,
        "b": data.b,
        "original_variable_count": data.original_variable_count,
        "pivot_count": data.pivot_count,
        "free_variable_count": len(data.free_variables),
        "compatibility_row_count": len(data.compatibility_rows),
        "row_count": len(data.rows),
        "denominator_lcm": data.denominator_lcm,
        "theorem_cut": data.theorem_cut,
        "chart_sha256": data.chart_sha256,
        "elapsed_seconds": round(time.monotonic() - started, 6),
        "output": str(out / "reduced-chart.json"),
    }
    atomic_write(out / "reduction-summary.json", json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary, sort_keys=True))


def command_emit(args: argparse.Namespace) -> None:
    data = build_reduced_chart(args.K, theorem_cut=args.theorem)
    payload = emit_chart(
        data,
        RUNS / args.tag / f"emitted_p{args.characteristic}_{args.tie_order}",
        args.characteristic,
        args.tie_order,
    )
    print(
        json.dumps(
            {
                "K": data.K,
                "chart_sha256": data.chart_sha256,
                "free_variable_count": len(data.free_variables),
                "row_count": len(data.rows),
                "band_count": payload["manifest"]["band_count"],
                "manifest": payload["manifest"]["manifest_path"],
            },
            sort_keys=True,
        )
    )


def command_run(args: argparse.Namespace) -> None:
    data = build_reduced_chart(args.K, theorem_cut=args.theorem)
    summary = run_staged(
        data=data,
        tag=args.tag,
        primes=parse_ints(args.primes),
        strategy=args.tie_order,
        timeout=args.timeout,
        cores=args.cores,
        stage_batch=args.stage_batch,
        start_stage=args.start_stage,
        stop_stage=args.stop_stage,
        hint_path=args.hint_json,
        exact_confirm=args.exact_confirm,
        final_exact=args.final_exact,
    )
    print(json.dumps({"tag": args.tag, "verdict": summary["verdict"], "summary": str(RUNS / args.tag / "summary.json")}, sort_keys=True))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    reduce_parser = subparsers.add_parser("reduce", help="derive the exact constant-pivot reduction only")
    reduce_parser.add_argument("tag")
    reduce_parser.add_argument("K", type=int)
    reduce_parser.add_argument("--theorem", action="store_true")
    reduce_parser.set_defaults(handler=command_reduce)

    emit_parser = subparsers.add_parser("emit", help="derive and emit durable staged Singular band files")
    emit_parser.add_argument("tag")
    emit_parser.add_argument("K", type=int)
    emit_parser.add_argument("--characteristic", type=int, default=0)
    emit_parser.add_argument("--theorem", action="store_true")
    emit_parser.add_argument(
        "--tie-order", choices=("native", "reverse", "weight-asc", "weight-desc"), default="weight-desc"
    )
    emit_parser.set_defaults(handler=command_emit)

    run_parser = subparsers.add_parser("run", help="modular staged prefixes with optional exact-Q replay")
    run_parser.add_argument("tag")
    run_parser.add_argument("K", type=int)
    run_parser.add_argument("--primes", default=",".join(str(prime) for prime in GOOD_PRIMES_DEFAULT))
    run_parser.add_argument("--theorem", action="store_true")
    run_parser.add_argument(
        "--tie-order", choices=("native", "reverse", "weight-asc", "weight-desc"), default="weight-desc"
    )
    run_parser.add_argument("--timeout", type=int, default=900, help="timeout for each guided_gb call")
    run_parser.add_argument("--cores", type=int, default=4)
    run_parser.add_argument("--stage-batch", type=int, default=1)
    run_parser.add_argument("--start-stage", type=int, default=0)
    run_parser.add_argument("--stop-stage", type=int)
    run_parser.add_argument("--hint-json", type=Path)
    run_parser.add_argument("--exact-confirm", action="store_true")
    run_parser.add_argument("--final-exact", action="store_true")
    run_parser.set_defaults(handler=command_run)

    args = parser.parse_args()
    args.handler(args)


if __name__ == "__main__":
    main()
