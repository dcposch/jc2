#!/usr/bin/env python3
"""Exact replay for the AS109 quadratic-y coupling gate.

This is a coefficient-identity replay, not a lift search.  A sparse
polynomial engine over a formal integer coefficient ring checks the three
degree-reduction identities in the characteristic-zero field theorem.  An
integer specialization checks positive and negative controls.
"""

from __future__ import annotations

import json
from collections.abc import Iterable


P = 109
SymbolMonomial = tuple[str, ...]
Symbolic = dict[SymbolMonomial, int]
Exponent = tuple[int, int]
Polynomial = dict[Exponent, Symbolic]


def sclean(value: Symbolic) -> Symbolic:
    return {monomial: coefficient for monomial, coefficient in value.items() if coefficient}


def sconst(value: int) -> Symbolic:
    return {} if not value else {(): value}


def svar(name: str) -> Symbolic:
    return {(name,): 1}


def sadd(*values: Symbolic) -> Symbolic:
    out: Symbolic = {}
    for value in values:
        for monomial, coefficient in value.items():
            out[monomial] = out.get(monomial, 0) + coefficient
    return sclean(out)


def sscale(value: Symbolic, scalar: int) -> Symbolic:
    return sclean({monomial: scalar * coefficient for monomial, coefficient in value.items()})


def smul(left: Symbolic, right: Symbolic) -> Symbolic:
    out: Symbolic = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial = tuple(sorted(left_monomial + right_monomial))
            out[monomial] = out.get(monomial, 0) + left_coefficient * right_coefficient
    return sclean(out)


def pclean(poly: Polynomial) -> Polynomial:
    return {exponent: sclean(coefficient) for exponent, coefficient in poly.items() if sclean(coefficient)}


def padd(*polys: Polynomial) -> Polynomial:
    out: Polynomial = {}
    for poly in polys:
        for exponent, coefficient in poly.items():
            out[exponent] = sadd(out.get(exponent, {}), coefficient)
    return pclean(out)


def pscale(poly: Polynomial, scalar: int) -> Polynomial:
    return pclean({exponent: sscale(coefficient, scalar) for exponent, coefficient in poly.items()})


def pmul(left: Polynomial, right: Polynomial) -> Polynomial:
    out: Polynomial = {}
    for (a, b), left_coefficient in left.items():
        for (c, d), right_coefficient in right.items():
            exponent = (a + c, b + d)
            out[exponent] = sadd(
                out.get(exponent, {}), smul(left_coefficient, right_coefficient)
            )
    return pclean(out)


def deriv(poly: Polynomial, axis: int) -> Polynomial:
    out: Polynomial = {}
    for (a, b), coefficient in poly.items():
        power = (a, b)[axis]
        if not power:
            continue
        exponent = (a - 1, b) if axis == 0 else (a, b - 1)
        out[exponent] = sadd(out.get(exponent, {}), sscale(coefficient, power))
    return pclean(out)


def jacobian(first: Polynomial, second: Polynomial) -> Polynomial:
    return padd(
        pmul(deriv(first, 0), deriv(second, 1)),
        pscale(pmul(deriv(first, 1), deriv(second, 0)), -1),
    )


def univariate(prefix: str, exponents: Iterable[int]) -> Polynomial:
    return {(exponent, 0): svar(f"{prefix}{exponent}") for exponent in exponents}


def shift_y(poly: Polynomial, power: int) -> Polynomial:
    return {(a, b + power): coefficient for (a, b), coefficient in poly.items()}


def y_coefficient(poly: Polynomial, power: int) -> Polynomial:
    return {(a, 0): coefficient for (a, b), coefficient in poly.items() if b == power}


def imonomial(a: int, b: int, coefficient: int = 1) -> Polynomial:
    return {} if not coefficient else {(a, b): sconst(coefficient)}


def integer_poly(poly: Polynomial) -> dict[Exponent, int]:
    out: dict[Exponent, int] = {}
    for exponent, coefficient in poly.items():
        assert set(coefficient).issubset({()}), coefficient
        value = coefficient.get((), 0)
        if value:
            out[exponent] = value
    return out


def y_degree(poly: Polynomial) -> int:
    return max((b for (_, b) in poly), default=-1)


def check_formal_coefficients() -> dict[str, str]:
    exponents = (0, 1, 2, 5)
    A0 = univariate("A0_", exponents)
    A1 = univariate("A1_", exponents)
    A2 = univariate("A2_", exponents)
    B0 = univariate("B0_", exponents)
    B1 = univariate("B1_", exponents)
    B2 = univariate("B2_", exponents)

    first = padd(A0, shift_y(A1, 1), shift_y(A2, 2))
    second = padd(B0, shift_y(B1, 1), shift_y(B2, 2))
    determinant = jacobian(first, second)

    cubic_expected = pscale(
        padd(pmul(deriv(A2, 0), B2), pscale(pmul(A2, deriv(B2, 0)), -1)),
        2,
    )
    assert y_coefficient(determinant, 3) == cubic_expected

    affine_first = padd(A0, shift_y(A1, 1))
    mixed_determinant = jacobian(affine_first, second)
    quadratic_expected = padd(
        pscale(pmul(deriv(A1, 0), B2), 2),
        pscale(pmul(A1, deriv(B2, 0)), -1),
    )
    assert y_coefficient(mixed_determinant, 2) == quadratic_expected

    affine_second = padd(B0, shift_y(B1, 1))
    affine_determinant = jacobian(affine_first, affine_second)
    linear_expected = padd(
        pmul(deriv(A1, 0), B1),
        pscale(pmul(A1, deriv(B1, 0)), -1),
    )
    constant_expected = padd(
        pmul(deriv(A0, 0), B1),
        pscale(pmul(A1, deriv(B0, 0)), -1),
    )
    assert y_coefficient(affine_determinant, 1) == linear_expected
    assert y_coefficient(affine_determinant, 0) == constant_expected

    return {
        "quadratic_quadratic_y3": "2*(A2'*B2-A2*B2')",
        "affine_quadratic_y2": "2*A1'*B2-A1*B2'",
        "affine_affine_y1": "A1'*B1-A1*B1'",
        "affine_affine_y0": "A0'*B1-A1*B0'",
        "formal_sparse_replay": "PASS",
    }


def check_controls() -> dict[str, object]:
    x = imonomial(1, 0)
    y = imonomial(0, 1)
    first = padd(x, y)
    first_squared = pmul(first, first)
    second = padd(y, first_squared)
    one = {(0, 0): 1}
    assert integer_poly(jacobian(first, second)) == one
    assert y_degree(first) == 1 and y_degree(second) == 2

    # Both displayed coordinates are quadratic; a determinant-one constant
    # target row operation recovers the affine first coordinate.
    both_quadratic_first = padd(first, second)
    assert y_degree(both_quadratic_first) == 2
    assert integer_poly(jacobian(both_quadratic_first, second)) == one
    recovered_first = padd(both_quadratic_first, pscale(second, -1))
    assert recovered_first == first

    # The forced triangular target shear removes the quadratic term exactly.
    sheared_second = padd(second, pscale(first_squared, -1))
    assert sheared_second == y
    assert integer_poly(jacobian(first, sheared_second)) == one

    # Negative control: B2=x is not a constant multiple of A1^2=1, and the
    # predicted nonzero y^2 coefficient appears in the Jacobian.
    rejected_second = padd(y, imonomial(1, 2))
    rejected_jacobian = integer_poly(jacobian(first, rejected_second))
    assert rejected_jacobian == {(0, 0): 1, (1, 1): 2, (0, 2): -1}

    # Degenerate A1=0 control forces B2=0 in a Keller pair.
    degenerate_second = padd(y, imonomial(2, 0))
    assert integer_poly(jacobian(x, degenerate_second)) == one

    return {
        "quadratic_keller_control": {
            "P": "x+y",
            "Q": "y+(x+y)^2",
            "jacobian": 1,
            "target_shear": "Q-P^2=y",
        },
        "both_quadratic_GL2_control": "(P+Q,Q)->(P,Q)",
        "nonproportional_top_negative_control": {
            "P": "x+y",
            "Q": "y+x*y^2",
            "jacobian": "1+2*x*y-y^2",
        },
        "degenerate_control": "J(x,y+x^2)=1",
    }


def main() -> None:
    print(
        json.dumps(
            {
                "verdict": "PASS-QUADRATIC-Y-NOGO-CONTROLS",
                "field_characteristic": 0,
                "formal_coefficients": check_formal_coefficients(),
                "controls": check_controls(),
                "as109_conclusion": "NO-EXACT-LIFT-WITH-BOTH-Y-DEGREES-AT-MOST-2",
                "enumeration_run": False,
                "lift_found": False,
                "jc2_inference": False,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
