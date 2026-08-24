#!/usr/bin/env python3
"""Deterministic exact replay for the AS109 cubic-y coupling gate.

The program checks universal coefficient identities in a sparse formal
polynomial ring and exact tame/non-Keller controls.  It is not an exponent,
support, finite-field, or lift search.
"""

from __future__ import annotations

import json
from collections.abc import Iterable


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


def ppow(poly: Polynomial, power: int) -> Polynomial:
    out = imonomial(0, 0)
    for _ in range(power):
        out = pmul(out, poly)
    return out


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
    return max((b for _, b in poly), default=-1)


def check_leading_coefficients() -> dict[str, str]:
    exponents = (0, 1, 2, 5)
    A = [univariate(f"A{i}_", exponents) for i in range(4)]
    B = [univariate(f"B{i}_", exponents) for i in range(4)]
    cubic_first = padd(*(shift_y(A[i], i) for i in range(4)))
    cubic_second = padd(*(shift_y(B[i], i) for i in range(4)))
    determinant = jacobian(cubic_first, cubic_second)

    expected_y5 = pscale(
        padd(pmul(deriv(A[3], 0), B[3]), pscale(pmul(A[3], deriv(B[3], 0)), -1)),
        3,
    )
    assert y_coefficient(determinant, 5) == expected_y5

    quadratic_first = padd(*(shift_y(A[i], i) for i in range(3)))
    mixed_determinant = jacobian(quadratic_first, cubic_second)
    expected_y4 = padd(
        pscale(pmul(deriv(A[2], 0), B[3]), 3),
        pscale(pmul(A[2], deriv(B[3], 0)), -2),
    )
    expected_y3 = padd(
        pscale(pmul(deriv(A[2], 0), B[2]), 2),
        pscale(pmul(deriv(A[1], 0), B[3]), 3),
        pscale(pmul(A[2], deriv(B[2], 0)), -2),
        pscale(pmul(A[1], deriv(B[3], 0)), -1),
    )
    assert y_coefficient(mixed_determinant, 4) == expected_y4
    assert y_coefficient(mixed_determinant, 3) == expected_y3

    # Normalize a2=h^2 and b3=h^3.  The y^3 coefficient is the
    # cross-multiplied derivative of 3*C/h-2*E/h^2.  Adding lambda*f to g
    # replaces E by E+lambda*h^2 and shifts that rational invariant by the
    # constant -2*lambda, exactly aligning the two depressed-cubic shifts.
    h = univariate("h_", exponents)
    C = univariate("C_", exponents)
    E = univariate("E_", exponents)
    normalized_first = padd(shift_y(pmul(h, h), 2), shift_y(C, 1))
    normalized_second = padd(shift_y(ppow(h, 3), 3), shift_y(E, 2))
    normalized_y3 = y_coefficient(jacobian(normalized_first, normalized_second), 3)
    numerator = padd(pscale(pmul(C, h), 3), pscale(E, -2))
    cross_derivative = padd(
        pmul(pmul(h, h), deriv(numerator, 0)),
        pscale(pmul(pmul(h, deriv(h, 0)), numerator), -2),
    )
    assert normalized_y3 == cross_derivative

    lam: Polynomial = {(0, 0): svar("lambda")}
    shifted_E = padd(E, pmul(lam, pmul(h, h)))
    shifted_numerator = padd(pscale(pmul(C, h), 3), pscale(shifted_E, -2))
    assert shifted_numerator == padd(numerator, pscale(pmul(lam, pmul(h, h)), -2))

    affine_first = padd(A[0], shift_y(A[1], 1))
    affine_cubic = jacobian(affine_first, cubic_second)
    expected_affine_y3 = padd(
        pscale(pmul(deriv(A[1], 0), B[3]), 3),
        pscale(pmul(A[1], deriv(B[3], 0)), -1),
    )
    assert y_coefficient(affine_cubic, 3) == expected_affine_y3

    return {
        "cubic_cubic_y5": "3*(a3'*b3-a3*b3')",
        "quadratic_cubic_y4": "3*a2'*b3-2*a2*b3'",
        "quadratic_cubic_y3": "2*a2'*b2+3*a1'*b3-2*a2*b2'-a1*b3'",
        "normalized_depression_invariant": "(3*C/h-2*E/h^2)'=0",
        "target_addition_shift": "g->g+lambda*f shifts invariant by -2*lambda",
        "affine_cubic_y3": "3*a1'*b3-a1*b3'",
        "formal_sparse_replay": "PASS",
    }


def check_cusp_normal_form() -> dict[str, str]:
    exponents = (0, 1, 3)
    h = univariate("h_", exponents)
    r = univariate("r_", exponents)
    U = univariate("U_", exponents)
    V = univariate("V_", exponents)
    W = univariate("W_", exponents)
    y = imonomial(0, 1)
    z = padd(pmul(h, y), r)
    first = padd(ppow(z, 2), U)
    second = padd(ppow(z, 3), pmul(V, z), W)

    expected_in_xz = padd(
        pmul(padd(pscale(deriv(U, 0), 3), pscale(deriv(V, 0), -2)), ppow(z, 2)),
        pscale(pmul(deriv(W, 0), z), -2),
        pmul(deriv(U, 0), V),
    )
    expected = pmul(h, expected_in_xz)
    assert jacobian(first, second) == expected

    # Replay the monic-integrality identity without denominators.  If
    # 2V=3U+2c, D=r^2+U, and G=r^3+V*r+W, then
    # r^3-(3D+2c)r+2(G-W)=0.
    c: Polynomial = {(0, 0): svar("c")}
    D = padd(ppow(r, 2), U)
    two_V = padd(pscale(U, 3), pscale(c, 2))
    two_G = padd(pscale(ppow(r, 3), 2), pmul(two_V, r), pscale(W, 2))
    monic_identity = padd(
        ppow(r, 3),
        pscale(pmul(padd(pscale(D, 3), pscale(c, 2)), r), -1),
        two_G,
        pscale(W, -2),
    )
    assert monic_identity == {}

    return {
        "normal_form": "f=z^2+U, g=z^3+V*z+W, z=h*y+r",
        "jacobian": "h*((3U'-2V')*z^2-2W'*z+U'*V)",
        "integrality_identity": "r^3-(3D+2c)r+2(G-W)=0",
        "formal_sparse_replay": "PASS",
    }


def check_controls() -> dict[str, object]:
    x = imonomial(1, 0)
    y = imonomial(0, 1)
    first = padd(x, y)
    second = padd(y, ppow(first, 3))
    one = {(0, 0): 1}
    assert y_degree(first) == 1 and y_degree(second) == 3
    assert integer_poly(jacobian(first, second)) == one
    assert padd(second, pscale(ppow(first, 3), -1)) == y

    both_cubic_first = padd(first, second)
    assert y_degree(both_cubic_first) == 3
    assert integer_poly(jacobian(both_cubic_first, second)) == one
    assert padd(both_cubic_first, pscale(second, -1)) == first

    quadratic_second = padd(y, ppow(first, 2))
    assert integer_poly(jacobian(first, quadratic_second)) == one
    assert y_degree(quadratic_second) == 2

    triangular_second = padd(y, imonomial(3, 0))
    assert integer_poly(jacobian(x, triangular_second)) == one

    rejected_first = padd(imonomial(0, 2), x)
    rejected_second = padd(imonomial(0, 3), y)
    rejected_jacobian = integer_poly(jacobian(rejected_first, rejected_second))
    assert rejected_jacobian == {(0, 2): 3, (0, 0): 1}

    return {
        "affine_cubic_tame": {
            "f": "x+y",
            "g": "y+(x+y)^3",
            "jacobian": 1,
            "target_shear": "g-f^3=y",
        },
        "both_cubic_GL2": "(f+g,g)->(f,g)",
        "quadratic_tame": "J(x+y,y+(x+y)^2)=1",
        "triangular_degenerate": "J(x,y+x^3)=1",
        "non_keller_rejection": {
            "f": "x+y^2",
            "g": "y+y^3",
            "jacobian": "1+3*y^2",
        },
    }


def main() -> None:
    print(
        json.dumps(
            {
                "verdict": "PASS-CUBIC-Y-NOGO-CONTROLS",
                "field_characteristic": 0,
                "leading_coefficients": check_leading_coefficients(),
                "cusp_normal_form": check_cusp_normal_form(),
                "controls": check_controls(),
                "as109_conclusion": "NO-EXACT-LIFT-WITH-BOTH-Y-DEGREES-AT-MOST-3",
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
