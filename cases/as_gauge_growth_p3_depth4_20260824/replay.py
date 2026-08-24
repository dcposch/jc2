#!/usr/bin/env python3
"""Exact p=3 gauge-growth certificate through Witt depth four.

The bounded systems are the frozen total-degree-simplex systems
B_(3,n)(D,D).  Gauge uniqueness is proved first, so the digit variables
below are deterministic coordinates on the gauge reconstructed from F,
not independent joint-search variables.
"""

from __future__ import annotations

import json
from typing import TypeAlias

import sympy as sp

Monomial: TypeAlias = tuple[int, int]
Poly: TypeAlias = dict[Monomial, int]


def add(*polynomials: Poly) -> Poly:
    result: Poly = {}
    for polynomial in polynomials:
        for monomial, coefficient in polynomial.items():
            result[monomial] = result.get(monomial, 0) + coefficient
    return {m: c for m, c in result.items() if c}


def scale(polynomial: Poly, scalar: int) -> Poly:
    return {m: scalar * c for m, c in polynomial.items() if scalar * c}


def multiply(left: Poly, right: Poly) -> Poly:
    result: Poly = {}
    for (i, j), a in left.items():
        for (k, ell), b in right.items():
            monomial = (i + k, j + ell)
            result[monomial] = result.get(monomial, 0) + a * b
    return {m: c for m, c in result.items() if c}


def power(polynomial: Poly, exponent: int) -> Poly:
    result: Poly = {(0, 0): 1}
    base = polynomial
    while exponent:
        if exponent & 1:
            result = multiply(result, base)
        base = multiply(base, base)
        exponent //= 2
    return result


def derivative(polynomial: Poly, variable: int) -> Poly:
    result: Poly = {}
    for (i, j), coefficient in polynomial.items():
        exponent = (i, j)[variable]
        if exponent:
            monomial = (i - 1, j) if variable == 0 else (i, j - 1)
            result[monomial] = coefficient * exponent
    return result


def jacobian(left: Poly, right: Poly) -> Poly:
    return add(
        multiply(derivative(left, 0), derivative(right, 1)),
        scale(multiply(derivative(left, 1), derivative(right, 0)), -1),
    )


def monomials_at_most(degree: int) -> list[Monomial]:
    return [
        (i, total - i)
        for total in range(degree + 1)
        for i in range(total + 1)
    ]


X: Poly = {(1, 0): 1}
Y: Poly = {(0, 1): 1}


def cotangent_composition(A: Poly, B: Poly, depth: int) -> tuple[Poly, Poly]:
    """Return (A-A^3, B sum_(j<depth) 3^j A^(2j)) over Z."""
    first = add(A, scale(power(A, 3), -1))
    series: Poly = {}
    for j in range(depth):
        series = add(series, scale(power(A, 2 * j), 3**j))
    return first, multiply(B, series)


def rref_affine(
    rows: list[list[int]], variables: int, prime: int = 3
) -> tuple[list[int] | None, list[list[int]] | None, int, bool]:
    """RREF of sum row[i] x_i + row[-1]=0 over F_prime."""
    matrix = [[value % prime for value in row] for row in rows]
    pivot_row = 0
    pivots: list[int] = []
    for column in range(variables):
        chosen = next(
            (row for row in range(pivot_row, len(matrix)) if matrix[row][column]),
            None,
        )
        if chosen is None:
            continue
        matrix[pivot_row], matrix[chosen] = matrix[chosen], matrix[pivot_row]
        inverse = pow(matrix[pivot_row][column], -1, prime)
        matrix[pivot_row] = [
            (inverse * value) % prime for value in matrix[pivot_row]
        ]
        for row in range(len(matrix)):
            if row != pivot_row and matrix[row][column]:
                factor = matrix[row][column]
                matrix[row] = [
                    (u - factor * v) % prime
                    for u, v in zip(matrix[row], matrix[pivot_row])
                ]
        pivots.append(column)
        pivot_row += 1
    inconsistent = any(
        all(value == 0 for value in row[:variables]) and row[variables] != 0
        for row in matrix
    )
    if inconsistent:
        return None, None, len(pivots), True
    free = [column for column in range(variables) if column not in pivots]
    particular = [0] * variables
    for row, column in enumerate(pivots):
        particular[column] = (-matrix[row][variables]) % prime
    basis: list[list[int]] = []
    for free_column in free:
        vector = [0] * variables
        vector[free_column] = 1
        for row, column in enumerate(pivots):
            vector[column] = (-matrix[row][free_column]) % prime
        basis.append(vector)
    return particular, basis, len(pivots), False


def matrix_rank(rows: list[list[int]], columns: int, prime: int = 3) -> int:
    """Rank with every supplied column treated as a coefficient column."""
    homogeneous = [row + [0] for row in rows]
    _particular, _basis, rank, inconsistent = rref_affine(
        homogeneous, columns, prime
    )
    assert not inconsistent
    return rank


def depth_three_affine_certificate(degree: int) -> dict[str, int | bool]:
    """Full necessary first-digit system, derived by exact composition.

    Put A=x+3a and B=y+3b.  The determinant modulo 9 and every over-cap
    coefficient of both compositions modulo 27 are affine over F_3.
    Evaluating the zero vector and every basis vector reconstructs the
    complete affine matrix without importing a hand-selected row set.
    """
    monomials = monomials_at_most(degree)
    variables = [
        (coordinate, monomial)
        for coordinate in ("a", "b")
        for monomial in monomials
    ]

    def residual(A: Poly, B: Poly) -> dict[tuple[str, Monomial], int]:
        values: dict[tuple[str, Monomial], int] = {}
        determinant = jacobian(A, B)
        determinant_keys = set(determinant) | {(0, 0)}
        for monomial in determinant_keys:
            coefficient = determinant.get(monomial, 0)
            if monomial == (0, 0):
                coefficient -= 1
            assert coefficient % 3 == 0
            values[("determinant_digit_1", monomial)] = (coefficient // 3) % 3
        first, second = cotangent_composition(A, B, 3)
        for name, polynomial in (("first_cap", first), ("second_cap", second)):
            for monomial, coefficient in polynomial.items():
                if sum(monomial) > degree:
                    assert coefficient % 9 == 0
                    values[(name, monomial)] = (coefficient // 9) % 3
        return values

    base = residual(X, Y)
    columns: list[dict[tuple[str, Monomial], int]] = []
    keys = set(base)
    for coordinate, monomial in variables:
        A, B = dict(X), dict(Y)
        target = A if coordinate == "a" else B
        target[monomial] = target.get(monomial, 0) + 3
        column = residual(A, B)
        keys.update(column)
        columns.append(column)
    rows = [
        [
            (columns[column].get(key, 0) - base.get(key, 0)) % 3
            for column in range(len(variables))
        ]
        + [base.get(key, 0) % 3]
        for key in sorted(keys)
    ]
    particular, basis, coefficient_rank, inconsistent = rref_affine(
        rows, len(variables)
    )
    augmented_rank = matrix_rank(rows, len(variables) + 1)
    assert augmented_rank == coefficient_rank + int(inconsistent)
    return {
        "degree": degree,
        "variables": len(variables),
        "rows": len(rows),
        "coefficient_rank": coefficient_rank,
        "augmented_rank": augmented_rank,
        "inconsistent": inconsistent,
        "affine_dimension_if_consistent": -1 if basis is None else len(basis),
        "particular_exists": particular is not None,
    }


def classic_depth_three_cap_three_control() -> dict[str, int | bool]:
    """Independently recover the frozen cap-three 12/13 rank control."""
    degree = 3
    monomials = monomials_at_most(degree)
    variables = [
        (coordinate, monomial)
        for coordinate in ("a", "b")
        for monomial in monomials
    ]
    index = {variable: column for column, variable in enumerate(variables)}
    rows: list[list[int]] = []
    # The first-coordinate p^2 digit -x^2 a forces deg(a)>=2 to zero.
    for monomial in monomials:
        if sum(monomial) >= 2:
            row = [0] * (len(variables) + 1)
            row[index[("a", monomial)]] = 1
            rows.append(row)
    # First determinant digit a_x+b_y.
    divergence: dict[Monomial, list[int]] = {}
    for monomial in monomials:
        i, j = monomial
        if i:
            target = (i - 1, j)
            divergence.setdefault(target, [0] * (len(variables) + 1))[
                index[("a", monomial)]
            ] += i
        if j:
            target = (i, j - 1)
            divergence.setdefault(target, [0] * (len(variables) + 1))[
                index[("b", monomial)]
            ] += j
    rows.extend(divergence.values())
    # Forbidden x^4 y coefficient: b_[x^2 y]-a_[x^3]+1.
    target = [0] * (len(variables) + 1)
    target[index[("b", (2, 1))]] = 1
    target[index[("a", (3, 0))]] = -1
    target[-1] = 1
    rows.append(target)
    _particular, _basis, coefficient_rank, inconsistent = rref_affine(
        rows, len(variables)
    )
    augmented_rank = matrix_rank(rows, len(variables) + 1)
    assert inconsistent and coefficient_rank == 12 and augmented_rank == 13
    return {
        "variables": len(variables),
        "rows": len(rows),
        "coefficient_rank": coefficient_rank,
        "augmented_rank": augmented_rank,
        "inconsistent": inconsistent,
    }


def coefficients_divisible(expression: sp.Expr, modulus: int, variables: list[sp.Symbol]) -> bool:
    polynomial = sp.Poly(sp.expand(expression), *variables)
    return all(int(coefficient) % modulus == 0 for coefficient in polynomial.coeffs())


def universal_digit_expansions() -> dict[str, bool]:
    """Verify every nonlinear carry in the depth-four formulas modulo 81."""
    x, y, a, b, c, d, e, f = sp.symbols("x y a b c d e f")
    variables = [x, y, a, b, c, d, e, f]
    A = x + 3 * a + 9 * c + 27 * e
    B = y + 3 * b + 9 * d + 27 * f
    first_formula = (
        x
        - x**3
        + 3 * a
        + 9 * (c - x**2 * a)
        + 27 * (e - x**2 * c - x * a**2 - a**3)
    )
    series = 1 + 3 * A**2 + 9 * A**4 + 27 * A**6
    second_formula = (
        y
        + 3 * (b + x**2 * y)
        + 9 * (d + x**2 * b + 2 * x * a * y + x**4 * y)
        + 27
        * (
            f
            + x**2 * d
            + 2 * x * a * b
            + x**4 * b
            + 2 * x * c * y
            + a**2 * y
            + x**3 * a * y
            + x**6 * y
        )
    )
    first_ok = coefficients_divisible(A - A**3 - first_formula, 81, variables)
    second_ok = coefficients_divisible(B * series - second_formula, 81, variables)

    ax, ay, bx, by, cx, cy, dx, dy, ex, ey, fx, fy = sp.symbols(
        "ax ay bx by cx cy dx dy ex ey fx fy"
    )
    derivative_variables = [ax, ay, bx, by, cx, cy, dx, dy, ex, ey, fx, fy]
    Ax, Ay = 1 + 3 * ax + 9 * cx + 27 * ex, 3 * ay + 9 * cy + 27 * ey
    Bx, By = 3 * bx + 9 * dx + 27 * fx, 1 + 3 * by + 9 * dy + 27 * fy
    bracket_ab = ax * by - ay * bx
    bracket_ad_cb = ax * dy - ay * dx + cx * by - cy * bx
    determinant_formula = (
        1
        + 3 * (ax + by)
        + 9 * (cx + dy + bracket_ab)
        + 27 * (ex + fy + bracket_ad_cb)
    )
    determinant_ok = coefficients_divisible(
        Ax * By - Ay * Bx - determinant_formula, 81, derivative_variables
    )
    assert first_ok and second_ok and determinant_ok
    return {
        "first_coordinate_mod_81": first_ok,
        "second_coordinate_mod_81": second_ok,
        "determinant_mod_81": determinant_ok,
    }


def symbolic_add(*polynomials: dict[Monomial, sp.Expr]) -> dict[Monomial, sp.Expr]:
    result: dict[Monomial, sp.Expr] = {}
    for polynomial in polynomials:
        for monomial, coefficient in polynomial.items():
            result[monomial] = sp.expand(result.get(monomial, 0) + coefficient)
    return {m: c for m, c in result.items() if c != 0}


def symbolic_scale(
    polynomial: dict[Monomial, sp.Expr], scalar: int
) -> dict[Monomial, sp.Expr]:
    return {
        monomial: sp.expand(scalar * coefficient)
        for monomial, coefficient in polynomial.items()
        if coefficient != 0
    }


def symbolic_multiply(
    left: dict[Monomial, sp.Expr], right: dict[Monomial, sp.Expr]
) -> dict[Monomial, sp.Expr]:
    result: dict[Monomial, sp.Expr] = {}
    for (i, j), a in left.items():
        for (k, ell), b in right.items():
            monomial = (i + k, j + ell)
            result[monomial] = sp.expand(result.get(monomial, 0) + a * b)
    return {m: c for m, c in result.items() if c != 0}


def symbolic_power(
    polynomial: dict[Monomial, sp.Expr], exponent: int
) -> dict[Monomial, sp.Expr]:
    result: dict[Monomial, sp.Expr] = {(0, 0): sp.Integer(1)}
    for _ in range(exponent):
        result = symbolic_multiply(result, polynomial)
    return result


def symbolic_derivative(
    polynomial: dict[Monomial, sp.Expr], variable: int
) -> dict[Monomial, sp.Expr]:
    result: dict[Monomial, sp.Expr] = {}
    for (i, j), coefficient in polynomial.items():
        exponent = (i, j)[variable]
        if exponent:
            monomial = (i - 1, j) if variable == 0 else (i, j - 1)
            result[monomial] = sp.expand(exponent * coefficient)
    return result


def generic_simplex(name: str, degree: int) -> dict[Monomial, sp.Expr]:
    return {
        monomial: sp.Symbol(f"{name}_{monomial[0]}_{monomial[1]}")
        for monomial in monomials_at_most(degree)
    }


def substitute_symbolic(
    polynomial: dict[Monomial, sp.Expr], replacements: dict[sp.Symbol, int]
) -> dict[Monomial, sp.Expr]:
    result = {
        monomial: sp.expand(coefficient.subs(replacements))
        for monomial, coefficient in polynomial.items()
    }
    return {m: c for m, c in result.items() if c != 0}


def homogeneous_symbolic(
    polynomial: dict[Monomial, sp.Expr], degree: int
) -> dict[Monomial, sp.Expr]:
    return {m: c for m, c in polynomial.items() if sum(m) == degree}


def depth_four_degree_bridge(degree: int) -> dict[str, object]:
    """Derive, rather than label, every support bound used by the top row."""
    assert degree in (5, 6)
    x_symbolic: dict[Monomial, sp.Expr] = {(1, 0): sp.Integer(1)}
    y_symbolic: dict[Monomial, sp.Expr] = {(0, 1): sp.Integer(1)}
    a = generic_simplex("a", degree - 2)
    c = generic_simplex("c", degree)
    p3_without_e = symbolic_add(
        symbolic_scale(symbolic_multiply(symbolic_power(x_symbolic, 2), c), -1),
        symbolic_scale(
            symbolic_multiply(x_symbolic, symbolic_power(a, 2)), -1
        ),
        symbolic_scale(symbolic_power(a, 3), -1),
    )
    top_degree = 12 if degree == 6 else 9
    top_a_degree = 4 if degree == 6 else 3
    a_top = homogeneous_symbolic(a, top_a_degree)
    assert homogeneous_symbolic(p3_without_e, top_degree) == symbolic_scale(
        symbolic_power(a_top, 3), -1
    )
    forced_zero = {symbol: 0 for symbol in a_top.values()}
    a_reduced = substitute_symbolic(a, forced_zero)
    p3_reduced = substitute_symbolic(p3_without_e, forced_zero)
    if degree == 6:
        a_degree_three = homogeneous_symbolic(a_reduced, 3)
        assert homogeneous_symbolic(p3_reduced, 9) == symbolic_scale(
            symbolic_power(a_degree_three, 3), -1
        )
        forced_zero.update({symbol: 0 for symbol in a_degree_three.values()})
    a_two = substitute_symbolic(a, forced_zero)
    assert max(sum(monomial) for monomial in a_two) <= 2

    # With deg(a)<=2, every over-cap p^2 second-coordinate term is exactly
    # x^2 times the part of b above degree D-2.
    b = generic_simplex("b", degree)
    q2_without_d = symbolic_add(
        symbolic_multiply(symbolic_power(x_symbolic, 2), b),
        symbolic_scale(
            symbolic_multiply(symbolic_multiply(x_symbolic, a_two), y_symbolic),
            2,
        ),
        symbolic_multiply(symbolic_power(x_symbolic, 4), y_symbolic),
    )
    high_q2 = {m: value for m, value in q2_without_d.items() if sum(m) > degree}
    expected_high_q2 = {
        (i + 2, j): value
        for (i, j), value in b.items()
        if i + j > degree - 2
    }
    assert high_q2 == expected_high_q2
    b_bound = {m: value for m, value in b.items() if sum(m) <= degree - 2}

    divergence = symbolic_add(
        symbolic_derivative(a_two, 0), symbolic_derivative(b_bound, 1)
    )
    assert sp.expand(divergence.get((2, 0), 0) - b_bound[(2, 1)]) == 0
    p3_final = symbolic_add(
        symbolic_scale(symbolic_multiply(symbolic_power(x_symbolic, 2), c), -1),
        symbolic_scale(
            symbolic_multiply(x_symbolic, symbolic_power(a_two, 2)), -1
        ),
        symbolic_scale(symbolic_power(a_two, 3), -1),
    )
    assert sp.expand(p3_final[(7, 0)] + c[(5, 0)]) == 0
    forced_rows = {b_bound[(2, 1)]: 0, c[(5, 0)]: 0}
    divergence_forced = substitute_symbolic(divergence, forced_rows)
    assert divergence_forced.get((4, 0), 0) == 0
    return {
        "degree": degree,
        "p2_first_cap_degree_a_at_most": degree - 2,
        "frobenius_top_degree": top_degree,
        "forced_degree_a_at_most": 2,
        "forced_degree_b_at_most": degree - 2,
        "p3_first_x7_is_minus_c_x5": True,
        "first_divergence_x2_is_b_x2y": True,
        "first_divergence_x4_after_forced_rows": 0,
    }


def depth_four_top_certificate(degree: int) -> dict[str, object]:
    """Universal coefficient obstruction for D=5 or 6.

    Earlier cap rows force deg(a)<=2, deg(b)<=4, c_[x^5]=0,
    a_[x^3]=b_[x^2 y]=0.  The exact x^4 determinant row and x^6 y
    second-composition row are then compared symbolically.
    """
    assert degree in (5, 6)
    bridge = depth_four_degree_bridge(degree)
    a2, a1y, b3y, b4, c5, b2y, d4y = sp.symbols(
        "a2 a1y b3y b4 c5 b2y d4y"
    )
    product_x5y = a2 * b3y + a1y * b4
    bracket_x4 = 2 * a2 * b3y - 4 * a1y * b4
    # The exact degree reductions give c5=b2y=0.  At x^4 the first
    # divergence has no coefficient at all, so there is no divided carry.
    determinant_x4 = 5 * c5 + d4y + bracket_x4
    q_x6y = (
        d4y
        + 2 * product_x5y
        + b2y
        + 2 * c5
        + 1
    )
    substituted = sp.expand(
        q_x6y.subs({b2y: 0, d4y: -5 * c5 - bracket_x4})
    )
    obstruction = sp.Poly(
        substituted - 1, a2, a1y, b3y, b4, c5, modulus=3
    )
    bracket_relation = sp.Poly(
        bracket_x4 + product_x5y, a2, a1y, b3y, b4, modulus=3
    )
    unit_certificate = sp.Poly(
        q_x6y - determinant_x4 - b2y - 1,
        a2,
        a1y,
        b3y,
        b4,
        c5,
        d4y,
        modulus=3,
    )
    assert determinant_x4.subs({d4y: -5 * c5 - bracket_x4}) == 0
    assert bracket_relation.is_zero
    assert obstruction.is_zero
    assert unit_certificate.is_zero
    return {
        "degree": degree,
        "degree_bridge": bridge,
        "forced_degree_a_at_most": bridge["forced_degree_a_at_most"],
        "forced_degree_b_at_most": bridge["forced_degree_b_at_most"],
        "first_divergence_x2_forces_b_x2y": 0,
        "first_divergence_x4_exact_carry": 0,
        "first_cap_x7_forces_c_x5": 0,
        "bracket_x4_plus_product_x5y_mod_3": 0,
        "unit_certificate_Qrow_minus_detrow_minus_b_x2y": 1,
        "forced_second_coordinate_x6y_digit": 1,
        "empty": True,
    }


def cotangent_control(depth: int) -> dict[str, int | bool]:
    first, second = cotangent_composition(X, Y, depth)
    modulus = 3**depth
    determinant = jacobian(first, second)
    determinant_error = dict(determinant)
    determinant_error[(0, 0)] = determinant_error.get((0, 0), 0) - 1
    assert all(coefficient % modulus == 0 for coefficient in determinant_error.values())
    first_degree = max(sum(monomial) for monomial, coefficient in first.items() if coefficient % modulus)
    second_degree = max(sum(monomial) for monomial, coefficient in second.items() if coefficient % modulus)
    expected = 2 * (depth - 1) + 1
    assert first_degree == 3
    assert second_degree == expected
    return {
        "depth": depth,
        "modulus": modulus,
        "gauge_degree": 1,
        "first_degree": first_degree,
        "second_degree": second_degree,
        "equal_cap": expected,
        "determinant_one": True,
    }


def main() -> None:
    expansions = universal_digit_expansions()
    depth_three = {
        str(degree): depth_three_affine_certificate(degree)
        for degree in (3, 4, 5)
    }
    assert depth_three["3"]["inconsistent"]
    assert depth_three["4"]["inconsistent"]
    assert not depth_three["5"]["inconsistent"]
    depth_four = {
        str(degree): depth_four_top_certificate(degree) for degree in (5, 6)
    }
    cotangent = {str(depth): cotangent_control(depth) for depth in (2, 3, 4)}
    assert cotangent["2"]["equal_cap"] == 3
    assert cotangent["3"]["equal_cap"] == 5
    assert cotangent["4"]["equal_cap"] == 7
    result = {
        "schema": "as-gauge-growth-p3-depth4-v1",
        "gauge_elimination": {
            "orientation": "C_3 o Phi_F = F",
            "first_coordinate": "A-A^3=P",
            "second_coordinate": "B=Q*(1-3*A^2)",
            "identity_branch_unique": True,
            "finite_system": "F-only; displayed gauge digits are canonical",
        },
        "universal_mod_81_expansions": expansions,
        "depth_three_full_affine_certificates": depth_three,
        "depth_three_frozen_control_recovered": classic_depth_three_cap_three_control(),
        "depth_four_top_coefficients": depth_four,
        "cotangent_positive_controls": cotangent,
        "exact_equal_cap_minima": {"depth_2": 3, "depth_3": 5, "depth_4": 7},
        "proposed_law_depth_4": "SURVIVES-THIS-GATE",
        "depth_4_survivor_below_7": False,
        "polynomial_lift_inference": False,
        "p109": False,
        "aws": False,
        "rectangles": False,
        "jc2_inference": False,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    print("PASS-AS-GAUGE-GROWTH-P3-DEPTH4")
    print("gauge_variables=ELIMINATED-BY-UNIQUE-AS-HENSEL-ROOT")
    print("depth_2_exact_min_equal_cap=3")
    print("depth_3_exact_min_equal_cap=5")
    print("depth_4_D5=EMPTY")
    print("depth_4_D6=EMPTY")
    print("depth_4_exact_min_equal_cap=7")
    print("depth_4_below_7_survivor=false")
    print("growth_law_beyond_depth_4=UNPROVED")
    print("polynomial_lift_inference=false")
    print("jc2_inference=false")


if __name__ == "__main__":
    main()
