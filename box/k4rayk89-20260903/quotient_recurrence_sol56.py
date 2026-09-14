#!/usr/bin/env python3
"""Minimal staged quotient-recurrence screen for the K=8,9 k=4-ray rows.

This is a *necessary-subsystem* screen.  It uses one torus normalization only:
the Jacobian coefficient is normalized to ``c=1`` through the explicit terminal
form Theta, while the top beta coefficient ``mu`` remains a variable and is
localized by ``mu*mu_inv-1``.  In particular, this file never sets both c and
mu to 1.

For ``q=beta^3/h^2`` in descending homogeneous bands, write

    h_i = [h]_(K-i),  p_i = [beta]_(K-2-i),
    S_n = sum_(a+b=n) h_a h_b,
    T_n = sum_(a+b+c=n) p_a p_b p_c,
    N_n = T_n - sum_(i=1..n) S_i q_(n-i).

Then ``N_n=H^2 q_n``.  The K+6 MASTER theorem forces the positive quotient
bands described below, zero intervening negative bands, and
``N_(2K-12)=Theta``.  Closed exact parametrizations of n=1,2,3 eliminate the
first lower h/beta bands without dividing by y or y-x.  Later h_n bands enter
linearly through a constant Q matrix times the localized unit mu^3; exact RREF
removes them and emits only compatibility equations.

K=9 has two exhaustive UFD branches at n=3:

    A: y divides v;
    B: y divides (y-x)*v^2 - 12*mu*p_2.

Both branches must be exact-Q unit ideals to kill K=9.  A modular unit is
reported only as F_p evidence and is never promoted.  Durable band files are
emitted with ``staged_band_emitter`` and every decision call goes through
``guided_gb`` with a per-call timeout and a <=5-core budget.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
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
RUNS = HERE / "recurrence-runs-sol56"
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE))

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
from hensel_reduced_sol56 import (  # noqa: E402
    atomic_write,
    exact_rref_with_transform,
    singular_expr,
    spq,
    transform_vector,
)


MAX_CORES = 5
DEFAULT_PRIMES = (32003, 32009, 32027)


@dataclass
class ScreenChart:
    K: int
    branch: str
    scope: str
    variables: list[str]
    weights: list[int]
    rows: list[BandRow]
    global_generators: list[tuple[str, str]]
    denominator_lcm: int
    formula_checks: dict[str, str]
    elimination_audit: list[dict[str, Any]]
    reconstruction: dict[str, str]
    chart_sha256: str


def homogeneous_form(
    prefix: str, degree: int, weight: int
) -> tuple[sp.Expr, list[sp.Symbol], dict[sp.Symbol, int]]:
    x, y = sp.symbols("x y")
    symbols: list[sp.Symbol] = []
    terms: list[sp.Expr] = []
    weights: dict[sp.Symbol, int] = {}
    for j in range(degree + 1):
        i = degree - j
        symbol = sp.Symbol(f"{prefix}_{i}_{j}")
        symbols.append(symbol)
        weights[symbol] = weight
        terms.append(symbol * x**i * y**j)
    return sp.Add(*terms), symbols, weights


def theta(K: int, x: sp.Symbol, y: sp.Symbol) -> sp.Expr:
    coefficients = [sp.Rational(1, 5 * K - 6)]
    for index in range(1, 5):
        factor = 5 - index
        coefficients.append(sp.cancel(factor * K * coefficients[-1] / (factor * K - 6)))
    theta_one = sum(coefficients[index] * x ** (4 - index) * y**index for index in range(5))
    return sp.expand(y**K * (y - x) ** 2 * theta_one)


def S(n: int, h: Mapping[int, sp.Expr]) -> sp.Expr:
    return sp.expand(sum((h.get(a, 0) * h.get(n - a, 0) for a in range(n + 1)), sp.Integer(0)))


def T(n: int, p: Mapping[int, sp.Expr]) -> sp.Expr:
    result: sp.Expr = sp.Integer(0)
    for a in range(n + 1):
        for b in range(n - a + 1):
            c = n - a - b
            result += p.get(a, 0) * p.get(b, 0) * p.get(c, 0)
    return sp.expand(result)


def N(n: int, h: Mapping[int, sp.Expr], p: Mapping[int, sp.Expr], q: Mapping[int, sp.Expr]) -> sp.Expr:
    result = T(n, p)
    for index in range(1, n + 1):
        result -= S(index, h) * q.get(n - index, 0)
    return sp.expand(result)


# Sparse x,y-coordinate arithmetic.  Keeping the geometric variables out of
# SymPy's expression tree is decisive for K=9: each homogeneous coefficient is
# expanded independently and the fixed terminal pivot matrices stay tiny.
CoordPoly = dict[tuple[int, int], sp.Expr]


def cp_clean(poly: Mapping[tuple[int, int], sp.Expr]) -> CoordPoly:
    result: CoordPoly = {}
    for monomial, coefficient in poly.items():
        coefficient = sp.expand(coefficient)
        if coefficient != 0:
            result[monomial] = coefficient
    return result


def cp_add(*polys: Mapping[tuple[int, int], sp.Expr]) -> CoordPoly:
    result: CoordPoly = {}
    for poly in polys:
        for monomial, coefficient in poly.items():
            result[monomial] = result.get(monomial, sp.Integer(0)) + coefficient
    return cp_clean(result)


def cp_scale(poly: Mapping[tuple[int, int], sp.Expr], scalar: sp.Expr) -> CoordPoly:
    return cp_clean({monomial: scalar * coefficient for monomial, coefficient in poly.items()})


def cp_shift(poly: Mapping[tuple[int, int], sp.Expr], i: int, j: int) -> CoordPoly:
    return {(a + i, b + j): coefficient for (a, b), coefficient in poly.items()}


def cp_mul(left: Mapping[tuple[int, int], sp.Expr], right: Mapping[tuple[int, int], sp.Expr]) -> CoordPoly:
    result: CoordPoly = {}
    for (i, j), a in left.items():
        for (k, ell), b in right.items():
            monomial = (i + k, j + ell)
            result[monomial] = result.get(monomial, sp.Integer(0)) + a * b
    return cp_clean(result)


def cp_pow(poly: Mapping[tuple[int, int], sp.Expr], exponent: int) -> CoordPoly:
    result: CoordPoly = {(0, 0): sp.Integer(1)}
    for _index in range(exponent):
        result = cp_mul(result, poly)
    return result


def cp_expr(poly: Mapping[tuple[int, int], sp.Expr], x: sp.Symbol, y: sp.Symbol) -> sp.Expr:
    return sp.Add(*(coefficient * x**i * y**j for (i, j), coefficient in sorted(poly.items())))


def cp_form(
    prefix: str, degree: int, weight: int
) -> tuple[CoordPoly, list[sp.Symbol], dict[sp.Symbol, int]]:
    polynomial: CoordPoly = {}
    symbols: list[sp.Symbol] = []
    weights: dict[sp.Symbol, int] = {}
    for i in range(degree + 1):
        j = degree - i
        symbol = sp.Symbol(f"{prefix}_{i}_{j}")
        polynomial[(i, j)] = symbol
        symbols.append(symbol)
        weights[symbol] = weight
    return polynomial, symbols, weights


def cp_recurrence(
    n: int,
    h: Mapping[int, CoordPoly],
    p: Mapping[int, CoordPoly],
    q: Mapping[int, CoordPoly],
) -> CoordPoly:
    triple: list[CoordPoly] = []
    for a in range(n + 1):
        for b in range(n - a + 1):
            c = n - a - b
            if a in p and b in p and c in p:
                triple.append(cp_mul(cp_mul(p[a], p[b]), p[c]))
    pieces: list[CoordPoly] = [cp_add(*triple)]
    for index in range(1, n + 1):
        qband = q.get(n - index, {})
        if not qband:
            continue
        square = cp_add(
            *(cp_mul(h[a], h[index - a]) for a in range(index + 1) if a in h and index - a in h)
        )
        pieces.append(cp_scale(cp_mul(square, qband), -1))
    return cp_add(*pieces)


def cp_quoy(
    numerator: Mapping[tuple[int, int], sp.Expr],
    monic_divisor: Mapping[tuple[int, int], sp.Expr],
    y_degree: int,
) -> tuple[CoordPoly, CoordPoly]:
    """Exact long division in y over Q[parameters,x], coefficientwise."""

    if sp.expand(monic_divisor.get((0, y_degree), 0)) != 1:
        raise AssertionError("coordinate divisor is not monic in y")
    if any(j == y_degree and i != 0 for i, j in monic_divisor):
        raise AssertionError("coordinate divisor has another top-y term")
    remainder = cp_clean(numerator)
    quotient: CoordPoly = {}
    while remainder:
        top_y = max(j for _i, j in remainder)
        if top_y < y_degree:
            break
        leaders = [
            (i, coefficient)
            for (i, j), coefficient in remainder.items()
            if j == top_y and coefficient != 0
        ]
        for i, leader in leaders:
            qmonomial = (i, top_y - y_degree)
            quotient[qmonomial] = quotient.get(qmonomial, sp.Integer(0)) + leader
            remainder = cp_add(
                remainder,
                cp_scale(cp_shift(monic_divisor, i, top_y - y_degree), -leader),
            )
    return cp_clean(quotient), cp_clean(remainder)


def solve_h_band_coord(
    residual: Mapping[tuple[int, int], sp.Expr],
    h_band: CoordPoly,
    mu: sp.Symbol,
) -> tuple[CoordPoly, list[sp.Symbol], list[sp.Expr], dict[str, Any]]:
    """Constant-Q RREF for one terminal band, directly on x,y coordinates."""

    h_symbols = [h_band[monomial] for monomial in sorted(h_band)]
    equations = [residual[monomial] for monomial in sorted(residual, reverse=True)]
    zero_h = {symbol: sp.Integer(0) for symbol in h_symbols}
    matrix: list[list[Any]] = []
    right: list[sp.Expr] = []
    for equation in equations:
        coefficients = [sp.expand(equation).coeff(symbol) for symbol in h_symbols]
        rest = sp.expand(equation.xreplace(zero_h))
        reconstructed = sp.expand(
            rest
            + sum(
                (coefficient * symbol for coefficient, symbol in zip(coefficients, h_symbols)),
                sp.Integer(0),
            )
        )
        if reconstructed != sp.expand(equation):
            raise AssertionError("coordinate recurrence is nonlinear in the entering h band")
        constant_coefficients: list[sp.Rational] = []
        for coefficient in coefficients:
            quotient = sp.cancel(coefficient / mu**3)
            if quotient.free_symbols:
                raise AssertionError(f"coordinate h pivot is not Q*mu^3: {coefficient}")
            constant_coefficients.append(sp.Rational(quotient))
        matrix.append(constant_coefficients)
        right.append(sp.expand(-rest / mu**3))

    from fractions import Fraction

    fraction_matrix = [
        [Fraction(int(value.p), int(value.q)) for value in row] for row in matrix
    ]
    rref, transform, pivots = exact_rref_with_transform(fraction_matrix)
    transformed_right = transform_vector(transform, right)
    free_columns = [column for column in range(len(h_symbols)) if column not in pivots]
    substitutions: dict[sp.Symbol, sp.Expr] = {}
    for row, pivot in enumerate(pivots):
        value = transformed_right[row]
        for column in free_columns:
            if rref[row][column]:
                value -= spq(rref[row][column]) * h_symbols[column]
        substitutions[h_symbols[pivot]] = sp.expand(value)
    compatibility = [
        sp.expand(transformed_right[row])
        for row in range(len(pivots), len(equations))
        if sp.expand(transformed_right[row]) != 0
    ]
    resolved = cp_clean(
        {monomial: coefficient.xreplace(substitutions) for monomial, coefficient in h_band.items()}
    )
    audit = {
        "engine": "sparse_xy_constant_Q_RREF",
        "equation_count": len(equations),
        "h_variable_count": len(h_symbols),
        "rank": len(pivots),
        "pivot_variables": [str(h_symbols[column]) for column in pivots],
        "free_h_variables": [str(h_symbols[column]) for column in free_columns],
        "compatibility_count": len(compatibility),
        "row_transform_exact": True,
    }
    return resolved, [h_symbols[column] for column in free_columns], compatibility, audit


def solve_alpha_band_coord(
    residual: Mapping[tuple[int, int], sp.Expr],
    alpha_band: CoordPoly,
) -> tuple[CoordPoly, list[sp.Symbol], list[sp.Expr], dict[str, Any]]:
    """Eliminate one alpha band by exact RREF over its constant H-matrix."""

    alpha_symbols = [alpha_band[monomial] for monomial in sorted(alpha_band)]
    equations = [residual[monomial] for monomial in sorted(residual, reverse=True)]
    zero_alpha = {symbol: sp.Integer(0) for symbol in alpha_symbols}
    matrix: list[list[sp.Rational]] = []
    right: list[sp.Expr] = []
    for equation in equations:
        coefficients = [sp.expand(equation).coeff(symbol) for symbol in alpha_symbols]
        rest = sp.expand(equation.xreplace(zero_alpha))
        reconstructed = sp.expand(
            rest
            + sum(
                (coefficient * symbol for coefficient, symbol in zip(coefficients, alpha_symbols)),
                sp.Integer(0),
            )
        )
        if reconstructed != sp.expand(equation):
            raise AssertionError("sparse quotient band is nonlinear in entering alpha variables")
        constant_row: list[sp.Rational] = []
        for coefficient in coefficients:
            if coefficient.free_symbols:
                raise AssertionError(f"alpha pivot coefficient is not rational: {coefficient}")
            constant_row.append(sp.Rational(coefficient))
        matrix.append(constant_row)
        right.append(-rest)

    from fractions import Fraction

    fraction_matrix = [
        [Fraction(int(value.p), int(value.q)) for value in row] for row in matrix
    ]
    rref, transform, pivots = exact_rref_with_transform(fraction_matrix)
    transformed_right = transform_vector(transform, right)
    free_columns = [column for column in range(len(alpha_symbols)) if column not in pivots]
    substitutions: dict[sp.Symbol, sp.Expr] = {}
    for row, pivot in enumerate(pivots):
        value = transformed_right[row]
        for column in free_columns:
            if rref[row][column]:
                value -= spq(rref[row][column]) * alpha_symbols[column]
        substitutions[alpha_symbols[pivot]] = sp.expand(value)
    compatibility = [
        sp.expand(transformed_right[row])
        for row in range(len(pivots), len(equations))
        if sp.expand(transformed_right[row]) != 0
    ]
    resolved = cp_clean(
        {
            monomial: coefficient.xreplace(substitutions)
            for monomial, coefficient in alpha_band.items()
        }
    )
    audit = {
        "engine": "sparse_xy_alpha_constant_Q_RREF",
        "equation_count": len(equations),
        "alpha_variable_count": len(alpha_symbols),
        "rank": len(pivots),
        "pivot_variables": [str(alpha_symbols[column]) for column in pivots],
        "free_alpha_variables": [str(alpha_symbols[column]) for column in free_columns],
        "compatibility_count": len(compatibility),
        "row_transform_exact": True,
    }
    return resolved, [alpha_symbols[column] for column in free_columns], compatibility, audit


def zero_rational(expr: sp.Expr) -> bool:
    numerator, _denominator = sp.fraction(sp.cancel(expr))
    return sp.expand(numerator) == 0


def localize_mu(expr: sp.Expr, mu: sp.Symbol, mu_inv: sp.Symbol) -> sp.Expr:
    """Replace negative Laurent powers of mu by powers of mu_inv."""

    numerator, denominator = sp.fraction(sp.cancel(expr))
    if denominator != 1:
        # The only nonconstant denominator allowed is a monomial in mu.
        coefficient, powers = denominator.as_coeff_Mul(), denominator.as_powers_dict()
        exponent = powers.get(mu, sp.Integer(0))
        residual = sp.cancel(denominator / mu**exponent)
        if residual.free_symbols:
            raise ValueError(f"non-Laurent denominator encountered: {denominator}")
        expr = sp.expand(numerator / residual * mu ** (-int(exponent)))
    result: sp.Expr = sp.Integer(0)
    for term in sp.expand(expr).as_ordered_terms():
        exponent_value = term.as_powers_dict().get(mu, sp.Integer(0))
        if not exponent_value.is_Integer:
            raise ValueError(f"nonintegral mu exponent in {term}")
        exponent = int(exponent_value)
        coefficient = sp.cancel(term / mu**exponent)
        result += coefficient * (mu**exponent if exponent >= 0 else mu_inv ** (-exponent))
    return sp.expand(result)


def polynomial_coefficients(expr: sp.Expr, x: sp.Symbol, y: sp.Symbol) -> list[sp.Expr]:
    return [sp.expand(coefficient) for _monomial, coefficient in sp.Poly(sp.expand(expr), x, y).terms()]


def solve_h_band(
    residual: sp.Expr,
    h_symbols: Sequence[sp.Symbol],
    mu: sp.Symbol,
    x: sp.Symbol,
    y: sp.Symbol,
) -> tuple[dict[sp.Symbol, sp.Expr], list[sp.Expr], dict[str, Any]]:
    """Eliminate h_n over Q[other variables,mu,mu^-1] by constant RREF."""

    terms = sp.Poly(sp.expand(residual), x, y).terms()
    equations = [sp.expand(coefficient) for _monomial, coefficient in terms]
    zero_h = {symbol: sp.Integer(0) for symbol in h_symbols}
    matrix: list[list[Any]] = []
    right: list[sp.Expr] = []
    for equation in equations:
        coefficients = [sp.expand(equation).coeff(symbol) for symbol in h_symbols]
        rest = sp.expand(equation.xreplace(zero_h))
        reconstructed = sp.expand(rest + sum((coefficient * symbol for coefficient, symbol in zip(coefficients, h_symbols)), sp.Integer(0)))
        if reconstructed != sp.expand(equation):
            raise AssertionError("recurrence band is nonlinear in its entering h variables")
        constant_coefficients = []
        for coefficient in coefficients:
            quotient = sp.cancel(coefficient / mu**3)
            if quotient.free_symbols:
                raise AssertionError(f"h pivot coefficient is not Q*mu^3: {coefficient}")
            constant_coefficients.append(quotient)
        matrix.append([sp.Rational(value) for value in constant_coefficients])
        right.append(sp.expand(-rest / mu**3))

    # Convert through the shared exact Fraction RREF implementation.
    fraction_matrix = [
        [__import__("fractions").Fraction(int(value.p), int(value.q)) for value in row]
        for row in matrix
    ]
    rref, transform, pivots = exact_rref_with_transform(fraction_matrix)
    transformed_right = transform_vector(transform, right)
    free_columns = [column for column in range(len(h_symbols)) if column not in pivots]
    substitutions: dict[sp.Symbol, sp.Expr] = {}
    for row, pivot in enumerate(pivots):
        value = transformed_right[row]
        for column in free_columns:
            if rref[row][column]:
                value -= spq(rref[row][column]) * h_symbols[column]
        substitutions[h_symbols[pivot]] = sp.expand(value)
    compatibility = [
        sp.expand(transformed_right[row])
        for row in range(len(pivots), len(equations))
        if sp.expand(transformed_right[row]) != 0
    ]
    # An exact construction certificate: after the pivot substitutions, the
    # same invertible row operations must leave zero pivot rows and precisely
    # the (signed) compatibility rows.  Thus no terminal coefficient is lost.
    post_equations = [sp.expand(equation.xreplace(substitutions)) for equation in equations]
    transformed_post = transform_vector(transform, post_equations)
    expected_post = [sp.Integer(0)] * len(pivots) + [
        sp.expand(-mu**3 * transformed_right[row]) for row in range(len(pivots), len(equations))
    ]
    if any(sp.expand(actual - expected) != 0 for actual, expected in zip(transformed_post, expected_post)):
        raise AssertionError("terminal-band RREF lost or altered a coefficient equation")
    audit = {
        "equation_count": len(equations),
        "h_variable_count": len(h_symbols),
        "rank": len(pivots),
        "pivot_variables": [str(h_symbols[column]) for column in pivots],
        "free_h_variables": [str(h_symbols[column]) for column in free_columns],
        "compatibility_count": len(compatibility),
        "post_substitution_span_control": "PASS_EXACT_Q",
    }
    return substitutions, compatibility, audit


def denominator_lcm_exprs(expressions: Iterable[sp.Expr]) -> int:
    value = 1
    for expression in expressions:
        polynomial = sp.Poly(sp.expand(expression))
        for coefficient in polynomial.coeffs():
            _numerator, denominator = sp.fraction(coefficient)
            if denominator.is_Integer:
                value = math.lcm(value, abs(int(denominator)))
    return value


def clear_rational_denominators(expression: sp.Expr) -> tuple[sp.Expr, int]:
    """Return an integral-coefficient scalar multiple and the multiplier.

    Singular 4.3 parses ``3*x/64`` as the unsupported operation poly/number in
    positive characteristic.  Clearing each row is ideal-preserving at the
    explicitly checked good primes and avoids relying on parser associativity.
    """

    expression = sp.expand(expression)
    multiplier = 1
    for coefficient in sp.Poly(expression).coeffs():
        _numerator, denominator = sp.fraction(coefficient)
        if not denominator.is_Integer:
            raise ValueError(f"non-rational coefficient denominator: {denominator}")
        multiplier = math.lcm(multiplier, abs(int(denominator)))
    integral = sp.expand(multiplier * expression)
    return integral, multiplier


def finalize_chart(
    K: int,
    branch: str,
    variable_symbols: Sequence[sp.Symbol],
    variable_weights: Mapping[sp.Symbol, int],
    compatibility_by_n: Sequence[tuple[int, Sequence[sp.Expr]]],
    formula_checks: Mapping[str, sp.Expr],
    elimination_audit: list[dict[str, Any]],
    reconstruction: Mapping[str, sp.Expr],
    mu: sp.Symbol,
    mu_inv: sp.Symbol,
) -> ScreenChart:
    localized_rows: list[BandRow] = []
    localized_exprs: list[sp.Expr] = []
    row_denominators: list[int] = []
    for n, expressions in compatibility_by_n:
        for index, expression in enumerate(expressions):
            localized = localize_mu(expression, mu, mu_inv)
            localized_exprs.append(localized)
            integral, row_denominator = clear_rational_denominators(localized)
            row_denominators.append(row_denominator)
            localized_rows.append(
                BandRow(
                    label=f"N{n}_compat_{index}",
                    band=f"n{n:02d}",
                    degree=n,
                    expr=singular_expr(integral),
                    source={
                        "kind": "QUOTIENT_RECURRENCE",
                        "n": n,
                        "row_in_band": index,
                        "cleared_denominator": row_denominator,
                    },
                )
            )
    seen: set[sp.Symbol] = set()
    ordered: list[sp.Symbol] = []
    for symbol in [mu, *variable_symbols, mu_inv]:
        if symbol not in seen:
            seen.add(symbol)
            ordered.append(symbol)
    weights = [variable_weights.get(symbol, 1) for symbol in ordered]
    checks = {
        name: "ZERO" if zero_rational(expression) else singular_expr(localize_mu(expression, mu, mu_inv))
        for name, expression in formula_checks.items()
    }
    if any(value != "ZERO" for value in checks.values()):
        raise AssertionError(f"closed recurrence formula check failed: {checks}")
    den_lcm = math.lcm(denominator_lcm_exprs(localized_exprs), *row_denominators)
    fingerprint = json.dumps(
        {
            "K": K,
            "branch": branch,
            "variables": [str(symbol) for symbol in ordered],
            "weights": weights,
            "rows": [(row.label, row.band, row.expr) for row in localized_rows],
        },
        sort_keys=True,
        separators=(",", ":"),
    )
    return ScreenChart(
        K=K,
        branch=branch,
        scope="NECESSARY_RECURRENCE_SUBSYSTEM",
        variables=[str(symbol) for symbol in ordered],
        weights=weights,
        rows=localized_rows,
        global_generators=[("mu_nonzero", "mu*mu_inv-1")],
        denominator_lcm=den_lcm,
        formula_checks=checks,
        elimination_audit=elimination_audit,
        reconstruction={name: singular_expr(localize_mu(expression, mu, mu_inv)) for name, expression in reconstruction.items()},
        chart_sha256=hashlib.sha256(fingerprint.encode()).hexdigest(),
    )


def quotient_remainder_y(
    numerator: sp.Expr, denominator: sp.Expr, y: sp.Symbol, degree_y: int
) -> tuple[sp.Expr, sp.Expr]:
    """Monic long division in y, with all other symbols in the coefficient ring."""

    quotient: sp.Expr = sp.Integer(0)
    remainder = sp.expand(numerator)
    while remainder != 0:
        polynomial = sp.Poly(remainder, y)
        degree = int(polynomial.degree())
        if degree < degree_y:
            break
        leader = polynomial.coeff_monomial(y**degree)
        term = leader * y ** (degree - degree_y)
        quotient += term
        remainder = sp.expand(remainder - term * denominator)
    return sp.expand(quotient), sp.expand(remainder)


def extend_rho_only_chart(
    chart: ScreenChart,
    h: dict[int, sp.Expr],
    p: dict[int, sp.Expr],
    q: Mapping[int, sp.Expr],
    variables: list[sp.Symbol],
    variable_weights: dict[sp.Symbol, int],
    mu: sp.Symbol,
    mu_inv: sp.Symbol,
    x: sp.Symbol,
    y: sp.Symbol,
) -> ScreenChart:
    """Add untouched lower bands and the exact positive-degree rho match.

    This is the deliberately small extension needed after the n=4,5,6
    constant-Q RREF.  It does not introduce lambda and does not construct E,
    MASTER, or ID6: the terminal recurrence with c=1 is already present in
    ``chart.rows``.  Hence a characteristic-zero unit here kills the branch,
    while POSDIM remains only a necessary-screen result.
    """

    K = chart.K
    b = K - 2
    r = K - 6
    for index in range(max(p) + 1, b + 1):
        form, symbols, weights = homogeneous_form(f"p{index}", b - index, K + 2 + index)
        p[index] = form
        variables.extend(symbols)
        variable_weights.update(weights)
    for index in range(max(h) + 1, K + 1):
        form, symbols, weights = homogeneous_form(f"h{index}", K - index, index)
        h[index] = form
        variables.extend(symbols)
        variable_weights.update(weights)

    h_full = sp.expand(sum(h.values(), sp.Integer(0)))
    beta = sp.expand(sum(p.values(), sp.Integer(0)))
    alpha, rho = quotient_remainder_y(beta**2, h_full, y, K)
    rho_y_degree = int(sp.Poly(rho, y).degree()) if rho != 0 else -1
    if rho_y_degree >= K:
        raise AssertionError(f"rho remainder has y-degree {rho_y_degree}, expected <{K}")
    rho_positive = sp.expand(sum((q[index] / 3 for index in range(r)), sp.Integer(0)))
    rho_difference = sp.expand(rho - rho_positive)

    rho_rows: list[BandRow] = []
    rho_denominators: list[int] = []
    grouped: dict[int, list[tuple[int, int, sp.Expr]]] = {}
    for (i, j), coefficient in sp.Poly(rho_difference, x, y).terms():
        i, j = int(i), int(j)
        degree = i + j
        coefficient = sp.expand(coefficient)
        if coefficient != 0 and degree >= 1:
            grouped.setdefault(degree, []).append((i, j, coefficient))
    for degree in sorted(grouped, reverse=True):
        for index, (i, j, coefficient) in enumerate(grouped[degree]):
            localized = localize_mu(coefficient, mu, mu_inv)
            integral, denominator = clear_rational_denominators(localized)
            rho_denominators.append(denominator)
            rho_rows.append(
                BandRow(
                    label=f"RHO_MATCH_d{degree}_x{i}_y{j}",
                    band=f"r00_RHO_d{degree:02d}",
                    degree=degree,
                    expr=singular_expr(integral),
                    source={
                        "kind": "RHO_MATCH",
                        "xy_degree": degree,
                        "x_power": i,
                        "y_power": j,
                        "row_in_band": index,
                        "cleared_denominator": denominator,
                    },
                )
            )

    chart.rows = [*chart.rows, *rho_rows]
    chart.scope = "RREF_RHO_NECESSARY_SUBSYSTEM"
    chart.variables = []
    chart.weights = []
    seen: set[sp.Symbol] = set()
    for symbol in [mu, *variables, mu_inv]:
        if symbol in seen:
            continue
        seen.add(symbol)
        chart.variables.append(str(symbol))
        chart.weights.append(variable_weights.get(symbol, 1))
    chart.denominator_lcm = math.lcm(chart.denominator_lcm, *rho_denominators)
    chart.formula_checks.update(
        {
            "RHO_QUOY_IDENTITY": "ZERO",
            "RHO_Y_DEGREE_LT_K": f"{rho_y_degree}<{K}",
            "RHO_POSITIVE_MATCH_SCOPE": "degrees>=1; rho_0 free",
        }
    )
    chart.reconstruction.update(
        {
            "h_full": singular_expr(localize_mu(h_full, mu, mu_inv)),
            "beta_full": singular_expr(localize_mu(beta, mu, mu_inv)),
            "alpha": singular_expr(localize_mu(alpha, mu, mu_inv)),
            "rho": singular_expr(localize_mu(rho, mu, mu_inv)),
            "rho_positive_target": singular_expr(localize_mu(rho_positive, mu, mu_inv)),
        }
    )
    fingerprint = json.dumps(
        {
            "K": K,
            "branch": chart.branch,
            "scope": chart.scope,
            "variables": chart.variables,
            "weights": chart.weights,
            "rows": [(row.label, row.band, row.expr) for row in chart.rows],
            "globals": chart.global_generators,
        },
        sort_keys=True,
        separators=(",", ":"),
    )
    chart.chart_sha256 = hashlib.sha256(fingerprint.encode()).hexdigest()
    return chart


def extend_rho_only_coord_chart(
    chart: ScreenChart,
    h: dict[int, CoordPoly],
    p: dict[int, CoordPoly],
    q: Mapping[int, CoordPoly],
    variables: list[sp.Symbol],
    variable_weights: dict[sp.Symbol, int],
    mu: sp.Symbol,
    mu_inv: sp.Symbol,
) -> ScreenChart:
    """Sparse-coordinate version of :func:`extend_rho_only_chart`.

    This avoids rebuilding the already banded K=9 data as one enormous SymPy
    expression before monic-y division.  It imposes exactly the same positive
    rho coefficients and deliberately leaves rho_0 free.
    """

    K = chart.K
    b = K - 2
    r = K - 6
    for index in range(max(p) + 1, b + 1):
        form, symbols, weights = cp_form(f"p{index}", b - index, K + 2 + index)
        p[index] = form
        variables.extend(symbols)
        variable_weights.update(weights)
    for index in range(max(h) + 1, K + 1):
        form, symbols, weights = cp_form(f"h{index}", K - index, index)
        h[index] = form
        variables.extend(symbols)
        variable_weights.update(weights)

    h_full = cp_add(*h.values())
    beta = cp_add(*p.values())
    alpha, rho = cp_quoy(cp_mul(beta, beta), h_full, K)
    rho_y_degree = max((j for _i, j in rho), default=-1)
    if rho_y_degree >= K:
        raise AssertionError(f"coordinate rho remainder has y-degree {rho_y_degree}, expected <{K}")
    rho_positive = cp_add(*(cp_scale(q[index], sp.Rational(1, 3)) for index in range(r)))
    rho_difference = cp_add(rho, cp_scale(rho_positive, -1))

    rho_rows: list[BandRow] = []
    rho_denominators: list[int] = []
    grouped: dict[int, list[tuple[int, int, sp.Expr]]] = {}
    for (i, j), coefficient in rho_difference.items():
        degree = i + j
        if coefficient != 0 and degree >= 1:
            grouped.setdefault(degree, []).append((i, j, coefficient))
    for degree in sorted(grouped, reverse=True):
        for index, (i, j, coefficient) in enumerate(sorted(grouped[degree], reverse=True)):
            localized = localize_mu(coefficient, mu, mu_inv)
            integral, denominator = clear_rational_denominators(localized)
            rho_denominators.append(denominator)
            rho_rows.append(
                BandRow(
                    label=f"RHO_MATCH_d{degree}_x{i}_y{j}",
                    band=f"r00_RHO_d{degree:02d}",
                    degree=degree,
                    expr=singular_expr(integral),
                    source={
                        "kind": "RHO_MATCH",
                        "engine": "sparse_xy_monic_y_division",
                        "xy_degree": degree,
                        "x_power": i,
                        "y_power": j,
                        "row_in_band": index,
                        "cleared_denominator": denominator,
                    },
                )
            )

    chart.rows = [*chart.rows, *rho_rows]
    chart.scope = "RREF_RHO_NECESSARY_SUBSYSTEM"
    chart.variables = []
    chart.weights = []
    seen: set[sp.Symbol] = set()
    for symbol in [mu, *variables, mu_inv]:
        if symbol in seen:
            continue
        seen.add(symbol)
        chart.variables.append(str(symbol))
        chart.weights.append(variable_weights.get(symbol, 1))
    chart.denominator_lcm = math.lcm(chart.denominator_lcm, *rho_denominators)
    chart.formula_checks.update(
        {
            "RHO_QUOY_IDENTITY": "PASS_BY_EXACT_SPARSE_DICTIONARY_DIVISION",
            "RHO_Y_DEGREE_LT_K": f"{rho_y_degree}<{K}",
            "RHO_POSITIVE_MATCH_SCOPE": "degrees>=1; rho_0 free",
            "RHO_ENGINE": "sparse_xy_monic_y_division",
        }
    )
    chart.reconstruction.update(
        {
            "rho_reconstruction": "exactly reproducible by extend_rho_only_coord_chart",
            "rho_positive_target": "q0/3+q1/3+q2/3",
        }
    )
    fingerprint = json.dumps(
        {
            "K": K,
            "branch": chart.branch,
            "scope": chart.scope,
            "variables": chart.variables,
            "weights": chart.weights,
            "rows": [(row.label, row.band, row.expr) for row in chart.rows],
            "globals": chart.global_generators,
            "rho_engine": "sparse_xy_monic_y_division",
        },
        sort_keys=True,
        separators=(",", ":"),
    )
    chart.chart_sha256 = hashlib.sha256(fingerprint.encode()).hexdigest()
    return chart


def extend_full_chart(
    chart: ScreenChart,
    h: dict[int, sp.Expr],
    p: dict[int, sp.Expr],
    q: Mapping[int, sp.Expr],
    variables: list[sp.Symbol],
    variable_weights: dict[sp.Symbol, int],
    mu: sp.Symbol,
    mu_inv: sp.Symbol,
    x: sp.Symbol,
    y: sp.Symbol,
) -> ScreenChart:
    """Add exact rho matches, MASTER bands, and every ID6 Jacobian row."""

    K = chart.K
    b = K - 2
    r = K - 6
    for index in range(max(p) + 1, b + 1):
        form, symbols, weights = homogeneous_form(f"p{index}", b - index, K + 2 + index)
        p[index] = form
        variables.extend(symbols)
        variable_weights.update(weights)
    for index in range(max(h) + 1, K + 1):
        form, symbols, weights = homogeneous_form(f"h{index}", K - index, index)
        h[index] = form
        variables.extend(symbols)
        variable_weights.update(weights)

    h_full = sp.expand(sum(h.values(), sp.Integer(0)))
    beta = sp.expand(sum(p.values(), sp.Integer(0)))
    alpha, rho = quotient_remainder_y(beta**2, h_full, y, K)
    rho_positive = sp.expand(sum((q[index] / 3 for index in range(r)), sp.Integer(0)))
    rho_difference = sp.expand(rho - rho_positive)

    lam = sp.Symbol("lam")
    variables.append(lam)
    variable_weights[lam] = 4 * K
    f_expr = sp.expand(h_full**2 + 2 * beta)
    E_expr = sp.expand(beta**3 - 3 * rho * h_full**2 - 9 * beta * rho + sp.Rational(9, 4) * alpha**2)
    Phi = sp.expand(E_expr - lam * f_expr)
    theta_expr = theta(K, x, y)
    JJ = sp.expand(
        3
        * (
            sp.diff(beta, x) * sp.diff(alpha, y)
            - sp.diff(beta, y) * sp.diff(alpha, x)
            - sp.diff(h_full, x) * sp.diff(rho, y)
            + sp.diff(h_full, y) * sp.diff(rho, x)
        )
    )

    extra_rows: list[BandRow] = []
    extra_denominators: list[int] = []

    def add_xy_rows(
        expression: sp.Expr,
        kind: str,
        prefix: str,
        degree_filter: Any,
    ) -> None:
        grouped: dict[int, list[tuple[int, int, sp.Expr]]] = {}
        for (i, j), coefficient in sp.Poly(sp.expand(expression), x, y).terms():
            degree = int(i + j)
            coefficient = sp.expand(coefficient)
            if coefficient != 0 and degree_filter(degree, int(i), int(j)):
                grouped.setdefault(degree, []).append((int(i), int(j), coefficient))
        for degree in sorted(grouped, reverse=True):
            for index, (i, j, coefficient) in enumerate(grouped[degree]):
                localized = localize_mu(coefficient, mu, mu_inv)
                integral, denominator = clear_rational_denominators(localized)
                extra_denominators.append(denominator)
                extra_rows.append(
                    BandRow(
                        label=f"{kind}_d{degree}_x{i}_y{j}",
                        band=f"{prefix}_d{degree:02d}",
                        degree=degree,
                        expr=singular_expr(integral),
                        source={
                            "kind": kind,
                            "xy_degree": degree,
                            "x_power": i,
                            "y_power": j,
                            "row_in_band": index,
                            "cleared_denominator": denominator,
                        },
                    )
                )

    # rho_difference may retain a scalar rho_0; only positive total degrees
    # are prescribed by q_i=3 rho_(r-i).  Its y-degree is already <K by the
    # exact monic quotient construction.
    add_xy_rows(rho_difference, "RHO_MATCH", "r00_RHO", lambda degree, _i, _j: degree >= 1)

    # All bands above K+6 vanish, and the terminal band is exactly +Theta for
    # the single c=1 normalization.
    phi_terminal = sp.expand(Phi - theta_expr)
    add_xy_rows(
        phi_terminal,
        "MASTER_PHI",
        "m00_MASTER",
        lambda degree, _i, _j: degree >= K + 6,
    )

    target_coefficient: sp.Expr = sp.Integer(0)
    grouped_j: dict[int, list[tuple[int, int, sp.Expr]]] = {}
    for (i, j), coefficient in sp.Poly(JJ, x, y).terms():
        i, j = int(i), int(j)
        coefficient = sp.expand(coefficient)
        if (i, j) == (4, 0):
            target_coefficient = coefficient
        elif coefficient != 0:
            grouped_j.setdefault(i + j, []).append((i, j, coefficient))
    if target_coefficient == 0:
        raise AssertionError("full reduced chart lost its x^4 target coefficient")
    for degree in sorted(grouped_j, reverse=True):
        for index, (i, j, coefficient) in enumerate(grouped_j[degree]):
            localized = localize_mu(coefficient, mu, mu_inv)
            integral, denominator = clear_rational_denominators(localized)
            extra_denominators.append(denominator)
            extra_rows.append(
                BandRow(
                    label=f"ID6_J_d{degree}_x{i}_y{j}",
                    band=f"j00_J_d{degree:02d}",
                    degree=degree,
                    expr=singular_expr(integral),
                    source={
                        "kind": "ID6_J",
                        "xy_degree": degree,
                        "x_power": i,
                        "y_power": j,
                        "row_in_band": index,
                        "cleared_denominator": denominator,
                    },
                )
            )

    target_localized = localize_mu(target_coefficient - 1, mu, mu_inv)
    target_integral, target_denominator = clear_rational_denominators(target_localized)
    extra_denominators.append(target_denominator)
    chart.global_generators = [
        ("mu_nonzero", "mu*mu_inv-1"),
        ("jacobian_target_c1", singular_expr(target_integral)),
    ]
    chart.rows = [*chart.rows, *extra_rows]
    chart.scope = "FULL_REDUCED_PINNED_CHART"
    chart.variables = []
    chart.weights = []
    seen: set[sp.Symbol] = set()
    for symbol in [mu, *variables, mu_inv]:
        if symbol in seen:
            continue
        seen.add(symbol)
        chart.variables.append(str(symbol))
        chart.weights.append(variable_weights.get(symbol, 1))
    chart.denominator_lcm = math.lcm(chart.denominator_lcm, *extra_denominators)
    chart.reconstruction.update(
        {
            "h_full": singular_expr(localize_mu(h_full, mu, mu_inv)),
            "beta_full": singular_expr(localize_mu(beta, mu, mu_inv)),
            "alpha": singular_expr(localize_mu(alpha, mu, mu_inv)),
            "rho": singular_expr(localize_mu(rho, mu, mu_inv)),
            "rho_positive_target": singular_expr(localize_mu(rho_positive, mu, mu_inv)),
        }
    )
    fingerprint = json.dumps(
        {
            "K": K,
            "branch": chart.branch,
            "scope": chart.scope,
            "variables": chart.variables,
            "weights": chart.weights,
            "rows": [(row.label, row.band, row.expr) for row in chart.rows],
            "globals": chart.global_generators,
        },
        sort_keys=True,
        separators=(",", ":"),
    )
    chart.chart_sha256 = hashlib.sha256(fingerprint.encode()).hexdigest()
    return chart


def build_k8(full: bool = False) -> ScreenChart:
    K = 8
    x, y, mu, mu_inv = sp.symbols("x y mu mu_inv")
    L = y - x
    variable_weights: dict[sp.Symbol, int] = {mu: K + 2, mu_inv: 1}
    variables: list[sp.Symbol] = []

    tau, tau_symbols, weights = homogeneous_form("tau", 1, K + 3)
    variable_weights.update(weights)
    variables.extend(tau_symbols)
    tau_y = sp.Symbol("tau_0_1")
    v_x = sp.Symbol("v_1_0")
    variable_weights[v_x] = K + 3
    variables.append(v_x)
    v = v_x * x + 2 * tau_y * y
    phi = y * v
    chi = sp.Symbol("chi_0_0")
    variable_weights[chi] = 2 * K + 6
    variables.append(chi)

    p: dict[int, sp.Expr] = {0: mu * y ** (K - 3) * L}
    p_symbols: dict[int, list[sp.Symbol]] = {}
    for index in (2, 3, 4):
        form, symbols, weights = homogeneous_form(f"p{index}", K - 2 - index, K + 2 + index)
        p[index] = form
        p_symbols[index] = symbols
        variables.extend(symbols)
        variable_weights.update(weights)
    p[1] = sp.expand(y**2 * (3 * y**2 * tau - L * phi))

    h: dict[int, sp.Expr] = {0: y ** (K - 1) * L}
    h[1] = sp.expand(3 * y**6 * tau / mu - sp.Rational(3, 2) * y**4 * L * phi / mu)
    h[2] = sp.expand(
        sp.Rational(3, 2) / mu**2 * (mu * y**2 * p[2] + sp.Rational(1, 4) * y * L * phi**2 - y**6 * chi)
    )
    h[3] = sp.expand(
        (L * y * v**3 + 36 * chi * v * y**4 + 24 * mu**2 * p[3] * y**2 - 12 * mu * p[2] * v - 18 * v**2 * tau * y**2)
        / (16 * mu**3)
    )
    q = {
        0: mu**3 * y ** (K - 7) * L,
        1: 3 * mu**2 * tau,
        2: 3 * mu * chi,
        3: sp.Integer(0),
    }
    checks = {
        "N1_minus_H2q1": N(1, h, p, q) - h[0] ** 2 * q[1],
        "N2_minus_H2q2": N(2, h, p, q) - h[0] ** 2 * q[2],
        "N3": N(3, h, p, q),
    }

    h4, h4_symbols, h4_weights = homogeneous_form("h4", K - 4, 4)
    variable_weights.update(h4_weights)
    h[4] = h4
    residual4 = sp.expand(N(4, h, p, q) - theta(K, x, y))
    substitutions4, compatibility4, audit4 = solve_h_band(residual4, h4_symbols, mu, x, y)
    h[4] = sp.expand(h4.xreplace(substitutions4))
    free_h4 = [symbol for symbol in h4_symbols if symbol not in substitutions4]
    variables.extend(free_h4)
    audit4.update({"n": 4, "terminal": True})

    reconstruction = {
        "H": h[0],
        "p0": p[0],
        "p1": p[1],
        "p2": p[2],
        "p3": p[3],
        "p4": p[4],
        "h1": h[1],
        "h2": h[2],
        "h3": h[3],
        "h4": h[4],
        "q1": q[1],
        "q2": q[2],
        "Theta": theta(K, x, y),
    }
    chart = finalize_chart(
        K,
        "single",
        variables,
        variable_weights,
        [(4, compatibility4)],
        checks,
        [audit4],
        reconstruction,
        mu,
        mu_inv,
    )
    if full:
        return extend_full_chart(chart, h, p, q, variables, variable_weights, mu, mu_inv, x, y)
    return chart


def _build_k9_dense_reference(branch: str, full: bool = False) -> ScreenChart:
    if branch not in ("A", "B"):
        raise ValueError("K=9 branch must be A or B")
    K = 9
    x, y, mu, mu_inv = sp.symbols("x y mu mu_inv")
    L = y - x
    variable_weights: dict[sp.Symbol, int] = {mu: K + 2, mu_inv: 1}
    variables: list[sp.Symbol] = []

    tau, tau_symbols, tau_weights = homogeneous_form("tau", 2, K + 3)
    variable_weights.update(tau_weights)
    variables.extend(tau_symbols)
    tau_y2 = sp.Symbol("tau_0_2")
    chi, chi_symbols, chi_weights = homogeneous_form("chi", 1, 2 * K + 6)
    variable_weights.update(chi_weights)
    variables.extend(chi_symbols)
    kappa = sp.Symbol("kappa")
    variable_weights[kappa] = 4 * K
    variables.append(kappa)

    p: dict[int, sp.Expr] = {0: mu * y ** (K - 3) * L}
    if branch == "A":
        w_x = sp.Symbol("w_1_0")
        variable_weights[w_x] = K + 3
        variables.append(w_x)
        w = w_x * x + 2 * tau_y2 * y
        v = y * w
        p2, p2_symbols, p2_weights = homogeneous_form("p2", K - 4, K + 4)
        p[2] = p2
        variables.extend(p2_symbols)
        variable_weights.update(p2_weights)
        omega = sp.expand(w * (L * y**2 * w**2 - 12 * mu * p[2]))
        branch_reconstruction: dict[str, sp.Expr] = {"w": w, "omega": omega}
    else:
        v_x2, v_xy = sp.symbols("v_2_0 v_1_1")
        variable_weights[v_x2] = K + 3
        variable_weights[v_xy] = K + 3
        variables.extend((v_x2, v_xy))
        v = v_x2 * x**2 + v_xy * x * y + 2 * tau_y2 * y**2
        zeta, zeta_symbols, zeta_weights = homogeneous_form("zeta", 4, 2 * K + 6)
        variables.extend(zeta_symbols)
        variable_weights.update(zeta_weights)
        p[2] = sp.expand((L * v**2 - y * zeta) / (12 * mu))
        omega = sp.expand(v * zeta)
        branch_reconstruction = {"zeta": zeta, "omega": omega}
    phi = y * v

    for index in (3, 4, 5, 6):
        form, symbols, weights = homogeneous_form(f"p{index}", K - 2 - index, K + 2 + index)
        p[index] = form
        variables.extend(symbols)
        variable_weights.update(weights)
    p[1] = sp.expand(y**2 * (3 * y**2 * tau - L * phi))

    h: dict[int, sp.Expr] = {0: y ** (K - 1) * L}
    h[1] = sp.expand(3 * y**6 * tau / mu - sp.Rational(3, 2) * y**4 * L * phi / mu)
    h[2] = sp.expand(
        sp.Rational(3, 2) / mu**2 * (mu * y**2 * p[2] + sp.Rational(1, 4) * L * phi**2 - y**6 * chi)
    )
    h[3] = sp.expand(
        (omega + 36 * chi * v * y**3 + 24 * mu**2 * p[3] * y**2 - 18 * v**2 * tau - 8 * kappa * y**6)
        / (16 * mu**3)
    )
    q = {
        0: mu**3 * y ** (K - 7) * L,
        1: 3 * mu**2 * tau,
        2: 3 * mu * chi,
        3: kappa,
        4: sp.Integer(0),
        5: sp.Integer(0),
    }
    checks = {
        "N1_minus_H2q1": N(1, h, p, q) - h[0] ** 2 * q[1],
        "N2_minus_H2q2": N(2, h, p, q) - h[0] ** 2 * q[2],
        "N3_minus_H2q3": N(3, h, p, q) - h[0] ** 2 * q[3],
    }

    compatibility_by_n: list[tuple[int, Sequence[sp.Expr]]] = []
    audits: list[dict[str, Any]] = []
    for n in (4, 5, 6):
        hn, hn_symbols, hn_weights = homogeneous_form(f"h{n}", K - n, n)
        variable_weights.update(hn_weights)
        h[n] = hn
        residual = N(n, h, p, q)
        if n == 6:
            residual = sp.expand(residual - theta(K, x, y))
        substitutions, compatibility, audit = solve_h_band(residual, hn_symbols, mu, x, y)
        h[n] = sp.expand(hn.xreplace(substitutions))
        free_h = [symbol for symbol in hn_symbols if symbol not in substitutions]
        variables.extend(free_h)
        audit.update({"n": n, "terminal": n == 6})
        audits.append(audit)
        compatibility_by_n.append((n, compatibility))

    reconstruction: dict[str, sp.Expr] = {
        "H": h[0],
        "p0": p[0],
        "p1": p[1],
        "p2": p[2],
        "p3": p[3],
        "p4": p[4],
        "p5": p[5],
        "p6": p[6],
        "h1": h[1],
        "h2": h[2],
        "h3": h[3],
        "h4": h[4],
        "h5": h[5],
        "h6": h[6],
        "q1": q[1],
        "q2": q[2],
        "q3": q[3],
        "Theta": theta(K, x, y),
        "v": v,
        **branch_reconstruction,
    }
    chart = finalize_chart(
        K,
        branch,
        variables,
        variable_weights,
        compatibility_by_n,
        checks,
        audits,
        reconstruction,
        mu,
        mu_inv,
    )
    if full:
        return extend_full_chart(chart, h, p, q, variables, variable_weights, mu, mu_inv, x, y)
    return chart


def build_k9(branch: str, full: bool = False, rho_only: bool = False) -> ScreenChart:
    """Build K=9 with sparse x,y bands and exact constant-matrix RREF.

    The dense reference above is intentionally retained as an independent
    formula transcript, but expanding N4/N5/N6 as monolithic SymPy expressions
    is prohibitively slow.  This implementation performs the identical row
    operations coefficient-by-coefficient.
    """

    if branch not in ("A", "B"):
        raise ValueError("K=9 branch must be A or B")
    K = 9
    x, y, mu, mu_inv = sp.symbols("x y mu mu_inv")
    L: CoordPoly = {(0, 1): sp.Integer(1), (1, 0): sp.Integer(-1)}
    Y = lambda degree: {(0, degree): sp.Integer(1)}  # noqa: E731
    H = cp_shift(L, 0, K - 1)
    variable_weights: dict[sp.Symbol, int] = {mu: K + 2, mu_inv: 1}
    variables: list[sp.Symbol] = []

    tau, tau_symbols, weights = cp_form("tau", 2, K + 3)
    variables.extend(tau_symbols)
    variable_weights.update(weights)
    tau_y2 = tau[(0, 2)]
    chi, chi_symbols, weights = cp_form("chi", 1, 2 * K + 6)
    variables.extend(chi_symbols)
    variable_weights.update(weights)
    kappa = sp.Symbol("kappa")
    variables.append(kappa)
    variable_weights[kappa] = 4 * K

    branch_reconstruction: dict[str, sp.Expr] = {}
    if branch == "A":
        w_x = sp.Symbol("w_1_0")
        variables.append(w_x)
        variable_weights[w_x] = K + 3
        w: CoordPoly = {(1, 0): w_x, (0, 1): 2 * tau_y2}
        v = cp_mul(Y(1), w)
        p2, p2_symbols, weights = cp_form("p2", K - 4, K + 4)
        variables.extend(p2_symbols)
        variable_weights.update(weights)
        omega = cp_mul(
            w,
            cp_add(cp_mul(cp_mul(L, Y(2)), cp_pow(w, 2)), cp_scale(p2, -12 * mu)),
        )
        branch_reconstruction["w"] = cp_expr(w, x, y)
    else:
        v_x2, v_xy = sp.symbols("v_2_0 v_1_1")
        variables.extend((v_x2, v_xy))
        variable_weights[v_x2] = K + 3
        variable_weights[v_xy] = K + 3
        v = {(2, 0): v_x2, (1, 1): v_xy, (0, 2): 2 * tau_y2}
        zeta, zeta_symbols, weights = cp_form("zeta", 4, 2 * K + 6)
        variables.extend(zeta_symbols)
        variable_weights.update(weights)
        p2 = cp_scale(
            cp_add(cp_mul(L, cp_pow(v, 2)), cp_scale(cp_mul(Y(1), zeta), -1)),
            sp.Rational(1, 12) * mu_inv,
        )
        omega = cp_mul(v, zeta)
        branch_reconstruction["zeta"] = cp_expr(zeta, x, y)
    phi = cp_mul(Y(1), v)

    p_coord: dict[int, CoordPoly] = {0: cp_scale(cp_shift(L, 0, K - 3), mu), 2: p2}
    p_coord[1] = cp_mul(
        Y(2), cp_add(cp_scale(cp_mul(Y(2), tau), 3), cp_scale(cp_mul(L, phi), -1))
    )
    for index in (3, 4, 5, 6):
        form, symbols, weights = cp_form(f"p{index}", K - 2 - index, K + 2 + index)
        p_coord[index] = form
        variables.extend(symbols)
        variable_weights.update(weights)

    h_coord: dict[int, CoordPoly] = {0: H}
    h_coord[1] = cp_add(
        cp_scale(cp_mul(Y(6), tau), 3 * mu_inv),
        cp_scale(cp_mul(cp_mul(Y(4), L), phi), -sp.Rational(3, 2) * mu_inv),
    )
    h_coord[2] = cp_scale(
        cp_add(
            cp_scale(cp_mul(Y(2), p_coord[2]), mu),
            cp_scale(cp_mul(L, cp_pow(phi, 2)), sp.Rational(1, 4)),
            cp_scale(cp_mul(Y(6), chi), -1),
        ),
        sp.Rational(3, 2) * mu_inv**2,
    )
    h_coord[3] = cp_scale(
        cp_add(
            omega,
            cp_scale(cp_mul(cp_mul(chi, v), Y(3)), 36),
            cp_scale(cp_mul(p_coord[3], Y(2)), 24 * mu**2),
            cp_scale(cp_mul(cp_pow(v, 2), tau), -18),
            cp_scale(Y(6), -8 * kappa),
        ),
        sp.Rational(1, 16) * mu_inv**3,
    )

    q_coord: dict[int, CoordPoly] = {
        0: cp_scale(cp_shift(L, 0, K - 7), mu**3),
        1: cp_scale(tau, 3 * mu**2),
        2: cp_scale(chi, 3 * mu),
        3: {(0, 0): kappa},
        4: {},
        5: {},
    }

    def assert_zero(poly: Mapping[tuple[int, int], sp.Expr], label: str) -> None:
        failures = [
            (monomial, sp.factor(sp.cancel(coefficient.subs(mu_inv, 1 / mu))))
            for monomial, coefficient in poly.items()
            if sp.cancel(coefficient.subs(mu_inv, 1 / mu)) != 0
        ]
        if failures:
            raise AssertionError(f"{label} failed: {failures[:2]}")

    H2 = cp_pow(H, 2)
    assert_zero(
        cp_add(cp_recurrence(1, h_coord, p_coord, q_coord), cp_scale(cp_mul(H2, q_coord[1]), -1)),
        "K9 sparse REC1",
    )
    assert_zero(
        cp_add(cp_recurrence(2, h_coord, p_coord, q_coord), cp_scale(cp_mul(H2, q_coord[2]), -1)),
        "K9 sparse REC2",
    )
    assert_zero(
        cp_add(cp_recurrence(3, h_coord, p_coord, q_coord), cp_scale(cp_mul(H2, q_coord[3]), -1)),
        "K9 sparse REC3",
    )

    theta_expr = theta(K, x, y)
    theta_coord: CoordPoly = {
        (int(i), int(j)): coefficient
        for (i, j), coefficient in sp.Poly(theta_expr, x, y).terms()
    }
    # Form all three raw recurrence bands before any pivot substitution.  This
    # prevents later products from distributing already-large h4/h5 formulae;
    # the subsequent xreplace is dramatically cheaper and mathematically the
    # same triangular elimination.
    raw_h_symbols: dict[int, list[sp.Symbol]] = {}
    for n in (4, 5, 6):
        h_band, symbols, weights = cp_form(f"h{n}", K - n, n)
        variable_weights.update(weights)
        h_coord[n] = h_band
        raw_h_symbols[n] = symbols
    raw_residuals: dict[int, CoordPoly] = {}
    for n in (4, 5, 6):
        residual = cp_recurrence(n, h_coord, p_coord, q_coord)
        if n == 6:
            residual = cp_add(residual, cp_scale(theta_coord, -1))
        raw_residuals[n] = residual

    compatibility_by_n: list[tuple[int, Sequence[sp.Expr]]] = []
    audits: list[dict[str, Any]] = []
    cumulative_substitutions: dict[sp.Symbol, sp.Expr] = {}
    for n in (4, 5, 6):
        residual = cp_clean(
            {
                monomial: coefficient.xreplace(cumulative_substitutions)
                for monomial, coefficient in raw_residuals[n].items()
            }
        )
        h_band = h_coord[n]
        resolved, free_h, compatibility, audit = solve_h_band_coord(residual, h_band, mu)
        # solve_h_band_coord returns the resolved coordinate band, so obtain
        # the actual pivot substitutions directly by matching each raw symbol.
        eliminated = {
            symbol: resolved[monomial]
            for monomial, symbol in h_band.items()
            if symbol not in free_h
        }
        cumulative_substitutions.update(eliminated)
        h_coord[n] = resolved
        variables.extend(free_h)
        audit.update({"n": n, "terminal": n == 6})
        audits.append(audit)
        compatibility_by_n.append((n, compatibility))

    h = {index: cp_expr(polynomial, x, y) for index, polynomial in h_coord.items()}
    p = {index: cp_expr(polynomial, x, y) for index, polynomial in p_coord.items()}
    q = {index: cp_expr(polynomial, x, y) for index, polynomial in q_coord.items()}
    reconstruction: dict[str, sp.Expr] = {
        "H": h[0],
        "p0": p[0],
        "p1": p[1],
        "h1": h[1],
        "h2": h[2],
        "h3": h[3],
        "q1": q[1],
        "q2": q[2],
        "q3": q[3],
        "Theta": theta_expr,
        "v": cp_expr(v, x, y),
        **branch_reconstruction,
    }
    chart = finalize_chart(
        K,
        branch,
        variables,
        variable_weights,
        compatibility_by_n,
        {"REC1": sp.Integer(0), "REC2": sp.Integer(0), "REC3": sp.Integer(0)},
        audits,
        reconstruction,
        mu,
        mu_inv,
    )
    if rho_only:
        return extend_rho_only_coord_chart(
            chart,
            h_coord,
            p_coord,
            q_coord,
            variables,
            variable_weights,
            mu,
            mu_inv,
        )
    if full:
        return extend_full_chart(chart, h, p, q, variables, variable_weights, mu, mu_inv, x, y)
    return chart


def build_chart(
    K: int, branch: str | None, full: bool = False, rho_only: bool = False
) -> ScreenChart:
    if full and rho_only:
        raise ValueError("--full and --rho-only are mutually exclusive")
    if K == 8:
        if rho_only:
            raise ValueError("the RREF rho-only extension is currently implemented for K=9")
        return build_k8(full=full)
    if K == 9:
        return build_k9(branch or "A", full=full, rho_only=rho_only)
    raise ValueError("the closed recurrence screen is implemented only for K=8 and K=9")


def order_chart(chart: ScreenChart, strategy: str) -> tuple[list[str], list[int]]:
    pairs = list(zip(chart.variables, chart.weights))
    # Keep mu_inv last so the reverse-lex tie breaker does not lead with the
    # Rabinowitsch variable.  mu itself may move with the geometric variables.
    localizer = [pair for pair in pairs if pair[0] == "mu_inv"]
    pairs = [pair for pair in pairs if pair[0] != "mu_inv"]
    if strategy == "native":
        pass
    elif strategy == "reverse":
        pairs.reverse()
    elif strategy == "weight-asc":
        pairs.sort(key=lambda item: (item[1], item[0]))
    elif strategy == "weight-desc":
        pairs.sort(key=lambda item: (-item[1], item[0]))
    else:
        raise ValueError(f"unknown tie order {strategy}")
    pairs.extend(localizer)
    return [name for name, _weight in pairs], [weight for _name, weight in pairs]


def ring_for(chart: ScreenChart, characteristic: int, strategy: str) -> tuple[str, list[str], list[int]]:
    if characteristic in (2, 3) or (characteristic and chart.denominator_lcm % characteristic == 0):
        raise ValueError(f"bad characteristic {characteristic}; denominator lcm={chart.denominator_lcm}")
    names, weights = order_chart(chart, strategy)
    ring = f"ring SS={characteristic},({','.join(names)}),wp({','.join(str(weight) for weight in weights)});"
    return ring, names, weights


def chart_json(chart: ScreenChart) -> dict[str, Any]:
    necessary_scope = chart.scope in {
        "NECESSARY_RECURRENCE_SUBSYSTEM",
        "RREF_RHO_NECESSARY_SUBSYSTEM",
    }
    return {
        "type": (
            "K4RAY-QUOTIENT-RECURRENCE-NECESSARY-SCREEN"
            if chart.scope == "NECESSARY_RECURRENCE_SUBSYSTEM"
            else (
                "K4RAY-QUOTIENT-RREF-RHO-NECESSARY-SCREEN"
                if chart.scope == "RREF_RHO_NECESSARY_SUBSYSTEM"
                else "K4RAY-QUOTIENT-RECURRENCE-FULL-REDUCED-CHART"
            )
        ),
        "K": chart.K,
        "branch": chart.branch,
        "scope": chart.scope,
        "normalization": {
            "jacobian_coefficient": 1,
            "mu": "variable",
            "mu_localizer": "mu*mu_inv-1",
            "warning": (
                "one torus normalization only; a POSDIM result is not a full-chart survivor"
                if necessary_scope
                else "one torus normalization only; POSDIM requires point extraction and exact J rebuild"
            ),
        },
        "variables": chart.variables,
        "weights": chart.weights,
        "row_count": len(chart.rows),
        "global_generators": chart.global_generators,
        "bands": sorted({row.band for row in chart.rows}),
        "denominator_lcm": chart.denominator_lcm,
        "formula_checks": chart.formula_checks,
        "elimination_audit": chart.elimination_audit,
        "reconstruction": chart.reconstruction,
        "chart_sha256": chart.chart_sha256,
    }


def emit(chart: ScreenChart, output_dir: Path, characteristic: int, strategy: str) -> dict[str, Any]:
    ring, names, weights = ring_for(chart, characteristic, strategy)
    manifest = emit_staged_band_files(
        chart.rows,
        BandEmitConfig(
            output_dir=output_dir,
            ring=ring,
            option_lines=("option(redSB);", "short=0;"),
            global_generators=tuple(chart.global_generators),
            manifest_name="bands-manifest.json",
        ),
    )
    payload = chart_json(chart)
    payload.update(
        {
            "characteristic": characteristic,
            "tie_order": strategy,
            "solver_ring": ring,
            "solver_variables": names,
            "solver_weights": weights,
            "band_manifest": manifest["manifest_path"],
            "band_union_checksum": manifest["generator_union_checksum"],
        }
    )
    atomic_write(output_dir / "screen-chart.json", json.dumps(payload, indent=2, sort_keys=True) + "\n")
    return {"manifest": manifest, "chart": payload}


def load_hint(path: Path | None, stage: str, weights: Sequence[int]) -> HilbertHint | None:
    if path is None:
        return None
    payload = json.loads(path.read_text(encoding="utf-8"))
    selected = payload.get("stages", {}).get(stage) if "stages" in payload else payload
    if selected is None:
        return None
    selected_weights = tuple(int(value) for value in selected.get("weights", weights))
    if len(selected_weights) != len(weights):
        raise ValueError("Hilbert hint weight length does not match the selected ring")
    return HilbertHint(
        tuple(int(value) for value in selected["numerator"]),
        selected_weights,
        None if selected.get("predicted_length") is None else int(selected["predicted_length"]),
    )


def summarized(result: GuidedGBResult) -> dict[str, Any]:
    return {
        "verdict": result.verdict.value,
        "promotion_note": result.certificate["promotion_note"],
        "accepted_run_count": result.certificate["accepted_run_count"],
        "crt_rational_reconstruction": result.certificate["crt_rational_reconstruction"],
        "runs": [
            {
                "label": run["label"],
                "characteristic": run["characteristic"],
                "returncode": run["returncode"],
                "timed_out": run["timed_out"],
                "elapsed_seconds": run["elapsed_seconds"],
                "unit": run["main"]["unit"],
                "dimension": run["main"]["dimension"],
                "vdim": run["main"]["vdim"],
                "basis_size": run["main"]["basis_size"],
                "nf_all_zero": run["main"]["nf_all_zero"],
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
    chart: ScreenChart,
    rows: Sequence[BandRow],
    characteristics: Sequence[int],
    strategy: str,
    output_dir: Path,
    timeout: int,
    cores: int,
    hint_path: Path | None,
    stage: str,
) -> GuidedGBResult:
    systems: list[SingularSystem] = []
    hint: HilbertHint | None = None
    for characteristic in characteristics:
        ring, names, weights = ring_for(chart, characteristic, strategy)
        if hint is None:
            hint = load_hint(hint_path, stage, weights)
        generators = [row.expr for row in rows] + [expression for _label, expression in chart.global_generators]
        systems.append(
            SingularSystem(
                name=f"QREC_K{chart.K}_{chart.branch}_{stage}_{strategy}_p{characteristic}",
                prelude="\n".join(("option(redSB); short=0;", ring, 'print("QREC__PRELUDE 1");')),
                generators=tuple(generators),
                characteristic=characteristic,
                variables=tuple(names),
                homogeneous=False,
                positive_weights=(),
                metadata={
                    "scope": chart.scope,
                    "K": chart.K,
                    "branch": chart.branch,
                    "stage": stage,
                    "chart_sha256": chart.chart_sha256,
                    "single_normalization": "c=1; mu localized",
                },
            )
        )
    return guided_groebner(
        systems,
        hint=hint,
        policy=PromotionPolicy.exact_q("inhomogeneous localized quotient-recurrence screen"),
        config=RunConfig(
            output_dir=output_dir,
            timeout_seconds=timeout,
            total_cores=cores,
            max_parallel_jobs=min(len(systems), cores),
            run_perturbed_control=False,
            no_rc=True,
        ),
    )


def run_stages(
    chart: ScreenChart,
    tag: str,
    primes: Sequence[int],
    strategy: str,
    timeout: int,
    cores: int,
    exact_confirm: bool,
    final_exact: bool,
    hint_path: Path | None,
) -> dict[str, Any]:
    if not 1 <= cores <= MAX_CORES:
        raise ValueError(f"cores must be in [1,{MAX_CORES}]")
    base = RUNS / tag / f"K{chart.K}_{chart.branch}"
    for characteristic in [0, *primes]:
        emit(chart, base / f"emitted_p{characteristic}_{strategy}", characteristic, strategy)
    band_names: list[str] = []
    grouped: dict[str, list[BandRow]] = {}
    for row in chart.rows:
        if row.band not in grouped:
            band_names.append(row.band)
            grouped[row.band] = []
        grouped[row.band].append(row)

    progress: list[dict[str, Any]] = []
    modular_kill: dict[str, Any] | None = None
    exact: dict[str, Any] | None = None
    started = time.monotonic()
    for index, band in enumerate(band_names):
        prefix = [row for previous in band_names[: index + 1] for row in grouped[previous]]
        stage = f"stage{index:02d}_{band}"
        result = run_prefix(chart, prefix, primes, strategy, base / "modular" / stage, timeout, cores, hint_path, stage)
        item = {
            "stage_index": index,
            "stage": stage,
            "last_band": band,
            "cumulative_row_count": len(prefix),
            **summarized(result),
        }
        progress.append(item)
        atomic_write(base / "stage-progress.json", json.dumps(progress, indent=2, sort_keys=True) + "\n")
        if item["runs"] and all(
            run["characteristic"] > 0
            and run["returncode"] == 0
            and not run["timed_out"]
            and run["unit"]
            and run["nf_all_zero"]
            for run in item["runs"]
        ):
            modular_kill = {
                "stage_index": index,
                "stage": stage,
                "primes": list(primes),
                "status": "UNIT_IN_ALL_REQUESTED_FIBRES__FP_ONLY",
            }
            if exact_confirm:
                exact_result = run_prefix(chart, prefix, (0,), strategy, base / "exact" / stage, timeout, cores, hint_path, stage)
                exact = {
                    "reason": "first modular-killing prefix",
                    "stage_index": index,
                    "stage": stage,
                    "cumulative_row_count": len(prefix),
                    **summarized(exact_result),
                }
            break

    if final_exact and exact is None and band_names:
        prefix = list(chart.rows)
        stage = f"stage{len(band_names)-1:02d}_{band_names[-1]}"
        exact_result = run_prefix(chart, prefix, (0,), strategy, base / "exact-final" / stage, timeout, cores, hint_path, stage)
        exact = {
            "reason": "explicit final exact-Q request",
            "stage_index": len(band_names) - 1,
            "stage": stage,
            "cumulative_row_count": len(prefix),
            **summarized(exact_result),
        }

    verdict = exact["verdict"] if exact else ("MODULAR_ONLY" if modular_kill else "OPEN")
    if exact is None and any(run["timed_out"] for item in progress for run in item["runs"]):
        verdict = "INCONCLUSIVE_TIMEOUT"
    summary = {
        "type": "K4RAY-QUOTIENT-RECURRENCE-STAGED-RUN",
        "tag": tag,
        "K": chart.K,
        "branch": chart.branch,
        "scope": chart.scope,
        "chart_sha256": chart.chart_sha256,
        "tie_order": strategy,
        "primes": list(primes),
        "per_call_timeout_seconds": timeout,
        "total_cores": cores,
        "progress": progress,
        "modular_kill": modular_kill,
        "exact": exact,
        "verdict": verdict,
        "interpretation": {
            "unit_exact_q": "kills this branch and hence the full chart",
            "posdim": (
                "necessary subsystem only; not a full-chart point or counterexample"
                if chart.scope
                in {"NECESSARY_RECURRENCE_SUBSYSTEM", "RREF_RHO_NECESSARY_SUBSYSTEM"}
                else "extract a surviving point, rebuild (f,g), and test J exactly"
            ),
            "modular_unit": "F_p-only until exact-Q confirmation",
        },
        "elapsed_seconds": round(time.monotonic() - started, 6),
    }
    atomic_write(base / "summary.json", json.dumps(summary, indent=2, sort_keys=True) + "\n")
    return summary


def parse_primes(text: str) -> tuple[int, ...]:
    return tuple(int(piece) for piece in text.split(",") if piece)


def command_build(args: argparse.Namespace) -> None:
    branches = ("A", "B") if args.K == 9 and args.branch == "all" else (args.branch,)
    for branch in branches:
        chart = build_chart(
            args.K,
            None if branch == "single" else branch,
            full=args.full,
            rho_only=args.rho_only,
        )
        output = RUNS / args.tag / f"K{args.K}_{chart.branch}" / "build"
        atomic_write(output / "screen-chart.json", json.dumps(chart_json(chart), indent=2, sort_keys=True) + "\n")
        print(
            json.dumps(
                {
                    "K": chart.K,
                    "branch": chart.branch,
                    "variables": len(chart.variables),
                    "rows": len(chart.rows),
                    "bands": sorted({row.band for row in chart.rows}),
                    "denominator_lcm": chart.denominator_lcm,
                    "chart_sha256": chart.chart_sha256,
                    "output": str(output / "screen-chart.json"),
                },
                sort_keys=True,
            )
        )


def command_emit(args: argparse.Namespace) -> None:
    chart = build_chart(
        args.K,
        None if args.branch == "single" else args.branch,
        full=args.full,
        rho_only=args.rho_only,
    )
    payload = emit(
        chart,
        RUNS / args.tag / f"K{chart.K}_{chart.branch}" / f"emitted_p{args.characteristic}_{args.tie_order}",
        args.characteristic,
        args.tie_order,
    )
    print(
        json.dumps(
            {
                "K": chart.K,
                "branch": chart.branch,
                "variables": len(chart.variables),
                "rows": len(chart.rows),
                "bands": payload["manifest"]["band_count"],
                "manifest": payload["manifest"]["manifest_path"],
            },
            sort_keys=True,
        )
    )


def command_run(args: argparse.Namespace) -> None:
    branches = ("A", "B") if args.K == 9 and args.branch == "all" else (args.branch,)
    summaries = []
    for branch in branches:
        chart = build_chart(
            args.K,
            None if branch == "single" else branch,
            full=args.full,
            rho_only=args.rho_only,
        )
        summaries.append(
            run_stages(
                chart,
                args.tag,
                parse_primes(args.primes),
                args.tie_order,
                args.timeout,
                args.cores,
                args.exact_confirm,
                args.final_exact,
                args.hint_json,
            )
        )
    aggregate = {
        "tag": args.tag,
        "K": args.K,
        "branches": [{"branch": summary["branch"], "verdict": summary["verdict"]} for summary in summaries],
        "all_branches_unit_exact_q": bool(summaries) and all(summary["verdict"] == "UNIT_IDEAL_CHAR0" for summary in summaries),
    }
    atomic_write(RUNS / args.tag / f"K{args.K}_aggregate.json", json.dumps(aggregate, indent=2, sort_keys=True) + "\n")
    print(json.dumps(aggregate, sort_keys=True))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    for name in ("build", "emit", "run"):
        sub = subparsers.add_parser(name)
        sub.add_argument("tag")
        sub.add_argument("K", type=int, choices=(8, 9))
        sub.add_argument("--branch", choices=("single", "A", "B", "all"), default="single")
        sub.add_argument("--full", action="store_true", help="add rho matches, MASTER terminal/high bands, and full ID6")
        sub.add_argument(
            "--rho-only",
            action="store_true",
            help="after terminal-band RREF, add untouched lower bands and exact positive-degree rho matches only",
        )
        if name in ("emit", "run"):
            sub.add_argument("--tie-order", choices=("native", "reverse", "weight-asc", "weight-desc"), default="weight-desc")
        if name == "emit":
            sub.add_argument("--characteristic", type=int, default=0)
            sub.set_defaults(handler=command_emit)
        elif name == "run":
            sub.add_argument("--primes", default=",".join(str(prime) for prime in DEFAULT_PRIMES))
            sub.add_argument("--timeout", type=int, default=900)
            sub.add_argument("--cores", type=int, default=4)
            sub.add_argument("--hint-json", type=Path)
            sub.add_argument("--exact-confirm", action="store_true")
            sub.add_argument("--final-exact", action="store_true")
            sub.set_defaults(handler=command_run)
        else:
            sub.set_defaults(handler=command_build)
    args = parser.parse_args()
    if args.K == 8 and args.branch not in ("single",):
        parser.error("K=8 uses --branch single")
    if args.K == 9 and args.branch == "single":
        parser.error("K=9 requires --branch A, B, or all")
    if args.full and args.rho_only:
        parser.error("--full and --rho-only are mutually exclusive")
    args.handler(args)


if __name__ == "__main__":
    main()
