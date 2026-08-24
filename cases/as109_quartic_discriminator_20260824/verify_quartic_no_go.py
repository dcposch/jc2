#!/usr/bin/env python3
"""Deterministic exact replay for the AS109 quartic-y discriminator.

Universal coefficient identities are checked in a sparse formal polynomial
ring.  Tame and non-Keller controls use exact integer arithmetic.  This is
not a support, exponent, finite-field, or lift search.
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


def constant_variable(name: str) -> Polynomial:
    return {(0, 0): svar(name)}


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
    A = [univariate(f"A{i}_", exponents) for i in range(5)]
    B = [univariate(f"B{i}_", exponents) for i in range(5)]
    quartic_first = padd(*(shift_y(A[i], i) for i in range(5)))
    quartic_second = padd(*(shift_y(B[i], i) for i in range(5)))
    determinant = jacobian(quartic_first, quartic_second)
    expected_y7 = pscale(
        padd(pmul(deriv(A[4], 0), B[4]), pscale(pmul(A[4], deriv(B[4], 0)), -1)),
        4,
    )
    assert y_coefficient(determinant, 7) == expected_y7

    cubic_first = padd(*(shift_y(A[i], i) for i in range(4)))
    mixed = jacobian(cubic_first, quartic_second)
    expected_y6 = padd(
        pscale(pmul(deriv(A[3], 0), B[4]), 4),
        pscale(pmul(A[3], deriv(B[4], 0)), -3),
    )
    expected_y5 = padd(
        pscale(pmul(deriv(A[3], 0), B[3]), 3),
        pscale(pmul(deriv(A[2], 0), B[4]), 4),
        pscale(pmul(A[3], deriv(B[3], 0)), -3),
        pscale(pmul(A[2], deriv(B[4], 0)), -2),
    )
    assert y_coefficient(mixed, 6) == expected_y6
    assert y_coefficient(mixed, 5) == expected_y5

    affine_first = padd(A[0], shift_y(A[1], 1))
    affine_quartic = jacobian(affine_first, quartic_second)
    expected_affine_y4 = padd(
        pscale(pmul(deriv(A[1], 0), B[4]), 4),
        pscale(pmul(A[1], deriv(B[4], 0)), -1),
    )
    assert y_coefficient(affine_quartic, 4) == expected_affine_y4

    quadratic_first = padd(*(shift_y(A[i], i) for i in range(3)))
    quadratic_quartic = jacobian(quadratic_first, quartic_second)
    expected_quadratic_y5 = padd(
        pscale(pmul(deriv(A[2], 0), B[4]), 4),
        pscale(pmul(A[2], deriv(B[4], 0)), -2),
    )
    assert y_coefficient(quadratic_quartic, 5) == expected_quadratic_y5

    # In the normalized (3,4) branch, a3=h^3 and b4=h^4.  The y^5
    # coefficient is h^6 times (4*C/h^2-3*E/h^3)'.  Adding lambda*f to g
    # shifts that invariant by -3*lambda and aligns the two depressions.
    h = univariate("h_", exponents)
    C = univariate("C_", exponents)
    E = univariate("E_", exponents)
    normalized_first = padd(shift_y(ppow(h, 3), 3), shift_y(C, 2))
    normalized_second = padd(shift_y(ppow(h, 4), 4), shift_y(E, 3))
    normalized_y5 = y_coefficient(jacobian(normalized_first, normalized_second), 5)
    numerator = padd(pscale(pmul(C, h), 4), pscale(E, -3))
    cross_derivative = padd(
        pmul(ppow(h, 3), deriv(numerator, 0)),
        pscale(pmul(pmul(ppow(h, 2), deriv(h, 0)), numerator), -3),
    )
    assert normalized_y5 == cross_derivative
    lam = constant_variable("lambda")
    shifted_E = padd(E, pmul(lam, ppow(h, 3)))
    shifted_numerator = padd(pscale(pmul(C, h), 4), pscale(shifted_E, -3))
    assert shifted_numerator == padd(numerator, pscale(pmul(lam, ppow(h, 3)), -3))

    return {
        "quartic_quartic_y7": "4*(a4'*b4-a4*b4')",
        "cubic_quartic_y6": "4*a3'*b4-3*a3*b4'",
        "cubic_quartic_y5": "3*a3'*b3+4*a2'*b4-3*a3*b3'-2*a2*b4'",
        "affine_quartic_y4": "4*a1'*b4-a1*b4'",
        "quadratic_quartic_y5": "4*a2'*b4-2*a2*b4'",
        "depression_invariant": "(4*C/h^2-3*E/h^3)'=0",
        "target_addition_shift": "g->g+lambda*f shifts invariant by -3*lambda",
        "formal_sparse_replay": "PASS",
    }


def check_34_normal_form() -> dict[str, str]:
    exponents = (0, 1, 3)
    h = univariate("h_", exponents)
    r = univariate("r_", exponents)
    u = univariate("u_", exponents)
    v = univariate("v_", exponents)
    a = univariate("a_", exponents)
    b = univariate("b_", exponents)
    c = univariate("c_", exponents)
    y = imonomial(0, 1)
    z = padd(pmul(h, y), r)
    first = padd(ppow(z, 3), pmul(u, z), v)
    second = padd(ppow(z, 4), pmul(a, ppow(z, 2)), pmul(b, z), c)
    expected_xz = padd(
        pmul(padd(pscale(deriv(u, 0), 4), pscale(deriv(a, 0), -3)), ppow(z, 4)),
        pmul(padd(pscale(deriv(v, 0), 4), pscale(deriv(b, 0), -3)), ppow(z, 3)),
        pmul(
            padd(
                pscale(pmul(a, deriv(u, 0)), 2),
                pscale(deriv(c, 0), -3),
                pscale(pmul(u, deriv(a, 0)), -1),
            ),
            ppow(z, 2),
        ),
        pmul(
            padd(
                pmul(b, deriv(u, 0)),
                pscale(pmul(a, deriv(v, 0)), 2),
                pscale(pmul(u, deriv(b, 0)), -1),
            ),
            z,
        ),
        padd(pmul(b, deriv(v, 0)), pscale(pmul(u, deriv(c, 0)), -1)),
    )
    expected = pmul(h, expected_xz)
    assert jacobian(first, second) == expected
    return {
        "normal_form": "f=z^3+u*z+v, g=z^4+a*z^2+b*z+c, z=h*y+r",
        "jacobian_coefficients": (
            "4u'-3a'; 4v'-3b'; 2a*u'-3c'-u*a'; "
            "b*u'+2a*v'-u*b'; b*v'-u*c'"
        ),
        "formal_sparse_replay": "PASS",
    }


def check_integrality_identities() -> dict[str, str]:
    exponents = (0, 1, 3)
    r = univariate("r_", exponents)
    u = univariate("u_", exponents)
    v = univariate("v_", exponents)
    alpha = constant_variable("alpha")
    delta = constant_variable("delta")
    gamma = constant_variable("gamma")

    # After a constant target translation of f sets beta=0, the four
    # nonconstant z-coefficients integrate to
    #   3a=4u+3alpha, 3b=4v, 9c=2u^2+6alpha*u+9gamma,
    #   ((4u/3+2alpha)*v)'=0.
    # The following cleared identity is four times that last derivative.
    three_a = padd(pscale(u, 4), pscale(alpha, 3))
    three_b = pscale(v, 4)
    nine_c = padd(
        pscale(ppow(u, 2), 2),
        pscale(pmul(alpha, u), 6),
        pscale(gamma, 9),
    )
    cleared_z1 = padd(
        pmul(three_b, deriv(u, 0)),
        pscale(pmul(three_a, deriv(v, 0)), 2),
        pscale(pmul(u, deriv(three_b, 0)), -1),
    )
    product_derivative = pscale(
        deriv(pmul(padd(pscale(u, 4), pscale(alpha, 6)), v), 0), 1
    )
    assert cleared_z1 == product_derivative

    # Polynomiality eliminant.  Put D=f(x,0), G=g(x,0), S=D-r^3 and
    # E=G+r^4/3-alpha*r^2-gamma-(4/3)D*r.  Fractions are cleared below:
    # 9E=2u^2+6alpha*u, hence u^2+3alpha*u-(9/2)E=0.
    D = padd(ppow(r, 3), pmul(u, r), v)
    nine_G = padd(
        pscale(ppow(r, 4), 9),
        pscale(pmul(u, ppow(r, 2)), 12),
        pscale(pmul(alpha, ppow(r, 2)), 9),
        pscale(pmul(v, r), 12),
        pscale(ppow(u, 2), 2),
        pscale(pmul(alpha, u), 6),
        pscale(gamma, 9),
    )
    nine_E = padd(
        nine_G,
        pscale(ppow(r, 4), 3),
        pscale(pmul(alpha, ppow(r, 2)), -9),
        pscale(gamma, -9),
        pscale(pmul(D, r), -12),
    )
    assert nine_E == padd(pscale(ppow(u, 2), 2), pscale(pmul(alpha, u), 6))

    # If q=(4u/3+2alpha), q*v=delta, then with
    #   L=2alpha*r+(4/3)S,
    #   M=6rE-2alpha*S+delta,
    # one has L*u=M.  We check the denominator-cleared version under the
    # defining relation 4u*v+6alpha*v=3delta.
    S = padd(D, pscale(ppow(r, 3), -1))
    three_L = padd(pscale(pmul(alpha, r), 6), pscale(S, 4))
    three_M = padd(
        pscale(pmul(r, nine_E), 2),
        pscale(pmul(alpha, S), -6),
        pscale(delta, 3),
    )
    conserved_product_relation = padd(
        pscale(pmul(u, v), 4),
        pscale(pmul(alpha, v), 6),
        pscale(delta, -3),
    )
    assert padd(pmul(three_L, u), pscale(three_M, -1)) == conserved_product_relation

    # The resultant-like eliminant follows without dividing by L:
    #   M^2+3alpha*M*L-(9/2)E*L^2=0.
    # With three_L=3L, three_M=3M and nine_E=9E, twice this identity
    # after clearing the common denominator is
    #   2(3M)^2+6alpha(3M)(3L)-nine_E(3L)^2=0.
    eliminant = padd(
        pscale(ppow(three_M, 2), 2),
        pscale(pmul(pmul(alpha, three_M), three_L), 6),
        pscale(pmul(nine_E, ppow(three_L, 2)), -1),
    )
    eliminant_remainder = pmul(
        conserved_product_relation,
        padd(
            pscale(conserved_product_relation, 2),
            pscale(
                pmul(padd(pscale(u, 4), pscale(alpha, 6)), three_L), -1
            ),
        ),
    )
    assert eliminant == eliminant_remainder

    # Independently retain D,G as coefficient symbols and verify that the
    # eliminant in an indeterminate R has degree 10 and nonzero constant
    # leading coefficient.  In the scaling above it is 24, corresponding
    # to 4/3 before denominators were cleared.
    R = imonomial(1, 0)
    D0 = constant_variable("D")
    G0 = constant_variable("G")
    S0 = padd(D0, pscale(ppow(R, 3), -1))
    nine_E0 = padd(
        pscale(G0, 9),
        pscale(ppow(R, 4), 3),
        pscale(pmul(alpha, ppow(R, 2)), -9),
        pscale(gamma, -9),
        pscale(pmul(D0, R), -12),
    )
    three_L0 = padd(pscale(pmul(alpha, R), 6), pscale(S0, 4))
    three_M0 = padd(
        pscale(pmul(R, nine_E0), 2),
        pscale(pmul(alpha, S0), -6),
        pscale(delta, 3),
    )
    eliminant0 = padd(
        pscale(ppow(three_M0, 2), 2),
        pscale(pmul(pmul(alpha, three_M0), three_L0), 6),
        pscale(pmul(nine_E0, ppow(three_L0, 2)), -1),
    )
    assert max(a for a, _ in eliminant0) == 10
    assert eliminant0[(10, 0)] == sconst(24)

    # Constant z-row, with denominators cleared:
    #   9*j0 = 12*v*v' - 2*u*(2u+3alpha)*u'.
    cleared_z0 = padd(
        pscale(pmul(v, deriv(v, 0)), 12),
        pscale(
            pmul(pmul(u, padd(pscale(u, 2), pscale(alpha, 3))), deriv(u, 0)),
            -2,
        ),
    )
    direct_cleared_z0 = padd(
        pscale(pmul(three_b, deriv(v, 0)), 3),
        pscale(pmul(u, deriv(nine_c, 0)), -1),
    )
    assert cleared_z0 == direct_cleared_z0

    return {
        "conserved_product": "(4u/3+2alpha)*v=delta",
        "r_equation": "degree 10 with leading coefficient 4/3 (24 after clearing)",
        "u_equation": "u^2+3alpha*u-(9/2)E=0",
        "constant_row": "9*j0=12*v*v'-2*u*(2u+3alpha)*u'",
        "formal_sparse_replay": "PASS",
    }


def check_controls() -> dict[str, object]:
    x = imonomial(1, 0)
    y = imonomial(0, 1)
    one = {(0, 0): 1}

    affine = padd(x, y)
    affine_quartic = padd(y, ppow(affine, 4))
    assert integer_poly(jacobian(affine, affine_quartic)) == one
    assert padd(affine_quartic, pscale(ppow(affine, 4), -1)) == y

    quadratic = padd(x, imonomial(0, 2))
    quadratic_quartic = padd(y, ppow(quadratic, 2))
    assert y_degree(quadratic) == 2 and y_degree(quadratic_quartic) == 4
    assert integer_poly(jacobian(quadratic, quadratic_quartic)) == one
    assert padd(quadratic_quartic, pscale(ppow(quadratic, 2), -1)) == y

    both_quartic_first = padd(affine, affine_quartic)
    assert y_degree(both_quartic_first) == 4
    assert integer_poly(jacobian(both_quartic_first, affine_quartic)) == one
    assert padd(both_quartic_first, pscale(affine_quartic, -1)) == affine

    rejected_first = padd(x, imonomial(0, 3))
    rejected_second = padd(y, imonomial(0, 4))
    assert integer_poly(jacobian(rejected_first, rejected_second)) == {
        (0, 0): 1,
        (0, 3): 4,
    }

    return {
        "affine_quartic_tame": "J(x+y,y+(x+y)^4)=1; shear by f^4",
        "quadratic_quartic_tame": "J(x+y^2,y+(x+y^2)^2)=1; shear by f^2",
        "both_quartic_GL2": "(f+g,g)->(f,g)",
        "non_keller_34_rejection": "J(x+y^3,y+y^4)=1+4*y^3",
    }


def main() -> None:
    print(
        json.dumps(
            {
                "verdict": "PASS-QUARTIC-Y-NOGO-CONTROLS",
                "field_characteristic": 0,
                "leading_coefficients": check_leading_coefficients(),
                "normal_form_34": check_34_normal_form(),
                "integrality": check_integrality_identities(),
                "controls": check_controls(),
                "as109_conclusion": "NO-EXACT-LIFT-WITH-BOTH-Y-DEGREES-AT-MOST-4",
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
