#!/usr/bin/env python3
"""Exact symbolic replay for the AS109 sextic-y frontier preflight.

This script classifies degree pairs, verifies the (4,6) leading split, and
derives the complete depressed (5,6) Pfaffian system over Q.  It is not an
exponent/support search and makes no lift or JC2 inference.
"""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import permutations
from math import gcd


NAMES = ("A", "B", "C", "D", "alpha", "beta", "gamma", "delta", "epsilon")
N = len(NAMES)
Exponent = tuple[int, ...]
Poly = dict[Exponent, Fraction]
Form = tuple[Poly, Poly, Poly, Poly]


def clean(poly: Poly) -> Poly:
    return {exponent: coefficient for exponent, coefficient in poly.items() if coefficient}


def const(value: int | Fraction) -> Poly:
    value = Fraction(value)
    return {} if not value else {(0,) * N: value}


def var(name: str) -> Poly:
    exponent = [0] * N
    exponent[NAMES.index(name)] = 1
    return {tuple(exponent): Fraction(1)}


def add(*polys: Poly) -> Poly:
    out: Poly = {}
    for poly in polys:
        for exponent, coefficient in poly.items():
            out[exponent] = out.get(exponent, Fraction(0)) + coefficient
    return clean(out)


def scale(poly: Poly, scalar: int | Fraction) -> Poly:
    scalar = Fraction(scalar)
    return clean({exponent: scalar * coefficient for exponent, coefficient in poly.items()})


def mul(left: Poly, right: Poly) -> Poly:
    out: Poly = {}
    for lexponent, lcoefficient in left.items():
        for rexponent, rcoefficient in right.items():
            exponent = tuple(a + b for a, b in zip(lexponent, rexponent))
            out[exponent] = out.get(exponent, Fraction(0)) + lcoefficient * rcoefficient
    return clean(out)


def power(poly: Poly, exponent: int) -> Poly:
    out = const(1)
    for _ in range(exponent):
        out = mul(out, poly)
    return out


def partial(poly: Poly, name: str) -> Poly:
    index = NAMES.index(name)
    out: Poly = {}
    for exponent, coefficient in poly.items():
        degree = exponent[index]
        if not degree:
            continue
        reduced = list(exponent)
        reduced[index] -= 1
        key = tuple(reduced)
        out[key] = out.get(key, Fraction(0)) + degree * coefficient
    return clean(out)


def differential(poly: Poly) -> Form:
    return tuple(partial(poly, name) for name in NAMES[:4])  # type: ignore[return-value]


def fadd(*forms: Form) -> Form:
    return tuple(add(*(form[index] for form in forms)) for index in range(4))  # type: ignore[return-value]


def fscale(form: Form, scalar: int | Fraction) -> Form:
    return tuple(scale(coefficient, scalar) for coefficient in form)  # type: ignore[return-value]


def fmul(poly: Poly, form: Form) -> Form:
    return tuple(mul(poly, coefficient) for coefficient in form)  # type: ignore[return-value]


def evaluate(poly: Poly, values: dict[str, int | Fraction]) -> Fraction:
    out = Fraction(0)
    for exponent, coefficient in poly.items():
        term = coefficient
        for name, degree in zip(NAMES, exponent):
            term *= Fraction(values.get(name, 0)) ** degree
        out += term
    return out


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    size = len(matrix)
    out = Fraction(0)
    for permutation in permutations(range(size)):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(size)
            for j in range(i + 1, size)
        )
        term = Fraction(-1 if inversions % 2 else 1)
        for row, column in enumerate(permutation):
            term *= matrix[row][column]
        out += term
    return out


def z_derivative(poly: dict[int, Poly]) -> dict[int, Poly]:
    return {degree - 1: scale(coefficient, degree) for degree, coefficient in poly.items() if degree}


def x_derivative(poly: dict[int, Poly]) -> dict[int, Form]:
    return {degree: differential(coefficient) for degree, coefficient in poly.items()}


def z_form_product(left: dict[int, Form], right: dict[int, Poly]) -> dict[int, Form]:
    out: dict[int, Form] = {}
    zero: Form = ({}, {}, {}, {})
    for left_degree, left_coefficient in left.items():
        for right_degree, right_coefficient in right.items():
            degree = left_degree + right_degree
            out[degree] = fadd(out.get(degree, zero), fmul(right_coefficient, left_coefficient))
    return {degree: coefficient for degree, coefficient in out.items() if coefficient != zero}


def degree_pair_sweep() -> dict[str, object]:
    pairs = [(m, 6) for m in range(7)]
    divisible = [(m, n) for m, n in pairs if m > 0 and m < n and n % m == 0]
    equal = [(m, n) for m, n in pairs if m == n]
    primitive = [
        (m, n)
        for m, n in pairs
        if 1 < m < n and n % m and gcd(m, n) == 1
    ]
    imprimitive = [
        (m, n)
        for m, n in pairs
        if 1 < m < n and n % m and gcd(m, n) > 1
    ]
    assert divisible == [(1, 6), (2, 6), (3, 6)]
    assert equal == [(6, 6)]
    assert primitive == [(5, 6)]
    assert imprimitive == [(4, 6)]
    return {
        "divisible_target_shears": divisible,
        "equal_target_GL2": equal,
        "new_coprime_pattern": primitive,
        "new_imprimitive_pattern": imprimitive,
        "degree_zero": "triangular or incompatible with degree six",
    }


def leading_46_split() -> dict[str, str]:
    # Reuse A,B,C as formal H,a3,b5 in the exact differential algebra.
    H, a3, b5 = (var(name) for name in ("A", "B", "C"))
    dH, da3, db5 = (differential(poly) for poly in (H, a3, b5))
    a4, b6 = power(H, 2), power(H, 3)
    da4, db6 = differential(a4), differential(b6)
    direct = fadd(
        fscale(fmul(b5, da4), 5),
        fscale(fmul(a4, db5), -4),
        fscale(fmul(b6, da3), 6),
        fscale(fmul(a3, db6), -3),
    )
    numerator = add(scale(mul(a3, H), 3), scale(b5, -2))
    dnumerator = differential(numerator)
    bracket = fadd(fscale(fmul(H, dnumerator), 2), fscale(fmul(numerator, dH), -5))
    assert direct == fmul(H, bracket)
    # Cross-multiplied derivative of N^2/H^5.
    rational_first_integral_numerator = fadd(
        fscale(fmul(mul(H, numerator), dnumerator), 2),
        fscale(fmul(power(numerator, 2), dH), -5),
    )
    assert rational_first_integral_numerator == fmul(numerator, bracket)
    return {
        "top_normalization": "a4=H^2, b6=H^3",
        "next_row": "E8=H*(2H*N'-5N*H'), N=3*a3*H-2*b5",
        "first_integral": "(N^2/H^5)'=0",
        "zero_branch": "N=0: common quadratic-generator depression is possible",
        "nonzero_branch": "H=h^2 and linear depression mismatch is constant",
    }


def leading_56_alignment() -> dict[str, str]:
    # Reuse A,B,C,D as formal h,a4,b5,lambda.
    h, a4, b5, lam = (var(name) for name in ("A", "B", "C", "D"))
    dh, da4, db5 = (differential(poly) for poly in (h, a4, b5))
    a5, b6 = power(h, 5), power(h, 6)
    da5, db6 = differential(a5), differential(b6)
    direct = fadd(
        fscale(fmul(b5, da5), 5),
        fscale(fmul(a5, db5), -5),
        fscale(fmul(b6, da4), 6),
        fscale(fmul(a4, db6), -4),
    )
    numerator = add(scale(mul(a4, h), 6), scale(b5, -5))
    dnumerator = differential(numerator)
    bracket = fadd(fmul(h, dnumerator), fscale(fmul(numerator, dh), -5))
    assert direct == fmul(power(h, 4), bracket)
    shifted_b5 = add(b5, mul(lam, power(h, 5)))
    shifted = add(scale(mul(a4, h), 6), scale(shifted_b5, -5))
    assert shifted == add(numerator, scale(mul(lam, power(h, 5)), -5))
    return {
        "top_normalization": "a5=h^5, b6=h^6",
        "depression_invariant": "6*a4/h^4-5*b5/h^5",
        "target_shift": "g->g+lambda*f shifts the invariant by -5*lambda",
        "aligned_variable": "z=h*y+r before depressed normal form",
    }


def canonical_56_system() -> dict[str, object]:
    A, B, C, D = (var(name) for name in NAMES[:4])
    alpha, beta, gamma, delta, epsilon = (var(name) for name in NAMES[4:])
    dA, dB, dC, dD = (differential(poly) for poly in (A, B, C, D))

    P = add(scale(A, Fraction(6, 5)), alpha)
    Q = add(scale(B, Fraction(6, 5)), beta)
    R = add(
        scale(power(A, 2), Fraction(3, 25)),
        scale(mul(alpha, A), Fraction(4, 5)),
        scale(C, Fraction(6, 5)),
        gamma,
    )
    S = add(
        scale(mul(A, B), Fraction(6, 25)),
        scale(mul(alpha, B), Fraction(4, 5)),
        scale(mul(beta, A), Fraction(3, 5)),
        scale(D, Fraction(6, 5)),
        delta,
    )
    T = add(
        scale(power(A, 3), Fraction(-4, 125)),
        scale(mul(alpha, power(A, 2)), Fraction(-2, 25)),
        scale(mul(A, C), Fraction(6, 25)),
        scale(mul(gamma, A), Fraction(2, 5)),
        scale(power(B, 2), Fraction(3, 25)),
        scale(mul(beta, B), Fraction(3, 5)),
        scale(mul(alpha, C), Fraction(4, 5)),
        epsilon,
    )
    dP, dQ, dR, dS, dT = (differential(poly) for poly in (P, Q, R, S, T))

    # Coefficients z^8,...,z^0 of J_(x,z)(f,g), after the z^9 and z^10
    # rows were removed by depression and leading normalization.
    row8 = fadd(fscale(dA, 6), fscale(dP, -5))
    row7 = fadd(fscale(dB, 6), fscale(dQ, -5))
    row6 = fadd(
        fscale(fmul(A, dP), -3),
        fscale(fmul(P, dA), 4),
        fscale(dC, 6),
        fscale(dR, -5),
    )
    row5 = fadd(
        fscale(fmul(A, dQ), -3),
        fscale(fmul(B, dP), -2),
        fscale(fmul(P, dB), 4),
        fscale(fmul(Q, dA), 3),
        fscale(dD, 6),
        fscale(dS, -5),
    )
    row4 = fadd(
        fscale(fmul(A, dR), -3),
        fscale(fmul(B, dQ), -2),
        fscale(fmul(C, dP), -1),
        fscale(fmul(P, dC), 4),
        fscale(fmul(Q, dB), 3),
        fscale(fmul(R, dA), 2),
        fscale(dT, -5),
    )
    assert row8 == row7 == row6 == row5 == row4 == ({}, {}, {}, {})

    row3 = fadd(
        fscale(fmul(A, dS), -3),
        fscale(fmul(B, dR), -2),
        fscale(fmul(C, dQ), -1),
        fscale(fmul(P, dD), 4),
        fscale(fmul(Q, dC), 3),
        fscale(fmul(R, dB), 2),
        fmul(S, dA),
    )
    row2 = fadd(
        fscale(fmul(A, dT), -3),
        fscale(fmul(B, dS), -2),
        fscale(fmul(C, dR), -1),
        fscale(fmul(Q, dD), 3),
        fscale(fmul(R, dC), 2),
        fmul(S, dB),
    )
    row1 = fadd(
        fscale(fmul(B, dT), -2),
        fscale(fmul(C, dS), -1),
        fscale(fmul(R, dD), 2),
        fmul(S, dC),
    )
    row0 = fadd(fscale(fmul(C, dT), -1), fmul(S, dD))

    # Derive all rows independently from the two displayed z-polynomials;
    # this protects the replay against a hand-copied missing summand.
    fzpoly = {5: const(1), 3: A, 2: B, 1: C, 0: D}
    gzpoly = {6: const(1), 4: P, 3: Q, 2: R, 1: S, 0: T}
    first_product = z_form_product(x_derivative(fzpoly), z_derivative(gzpoly))
    second_product = z_form_product(x_derivative(gzpoly), z_derivative(fzpoly))
    zero: Form = ({}, {}, {}, {})
    derived = {
        degree: fadd(
            first_product.get(degree, zero),
            fscale(second_product.get(degree, zero), -1),
        )
        for degree in set(first_product) | set(second_product)
    }
    expected_rows = {
        8: row8,
        7: row7,
        6: row6,
        5: row5,
        4: row4,
        3: row3,
        2: row2,
        1: row1,
        0: row0,
    }
    assert all(derived.get(degree, zero) == expected_rows.get(degree, zero) for degree in range(11))

    I3 = add(
        scale(mul(power(A, 2), B), Fraction(-12, 25)),
        scale(mul(mul(alpha, A), B), Fraction(-4, 5)),
        scale(mul(beta, power(A, 2)), Fraction(-3, 5)),
        scale(mul(A, D), Fraction(6, 5)),
        mul(delta, A),
        scale(mul(B, C), Fraction(6, 5)),
        scale(mul(gamma, B), 2),
        scale(mul(beta, C), 3),
        scale(mul(alpha, D), 4),
    )
    I2 = add(
        scale(power(A, 4), Fraction(9, 125)),
        scale(mul(alpha, power(A, 3)), Fraction(4, 25)),
        scale(mul(A, power(B, 2)), Fraction(-12, 25)),
        scale(mul(power(A, 2), C), Fraction(-12, 25)),
        scale(mul(mul(alpha, A), C), Fraction(-4, 5)),
        scale(mul(mul(beta, A), B), Fraction(-6, 5)),
        scale(mul(gamma, power(A, 2)), Fraction(-3, 5)),
        scale(mul(alpha, power(B, 2)), Fraction(-2, 5)),
        scale(mul(D, B), Fraction(6, 5)),
        mul(delta, B),
        scale(power(C, 2), Fraction(3, 5)),
        scale(mul(gamma, C), 2),
        scale(mul(beta, D), 3),
    )
    assert row3 == differential(I3)
    assert row2 == differential(I2)

    omega = row1
    eta = row0
    exterior_ab = add(partial(omega[0], "B"), scale(partial(omega[1], "A"), -1))
    expected_exterior_ab = add(
        scale(power(A, 2), Fraction(24, 125)),
        scale(mul(alpha, A), Fraction(8, 25)),
        scale(C, Fraction(-12, 25)),
        scale(gamma, Fraction(-4, 5)),
    )
    assert exterior_ab == expected_exterior_ab and exterior_ab

    point = {"A": 0, "B": 0, "C": 0, "D": 1}
    rows = (differential(I3), differential(I2), omega, eta)
    matrix = [[evaluate(entry, point) for entry in row] for row in rows]
    det_value = determinant(matrix)
    assert det_value == Fraction(6, 5) ** 4

    return {
        "normal_form": "f=z^5+A*z^3+B*z^2+C*z+D; g=z^6+P*z^4+Q*z^3+R*z^2+S*z+T",
        "integrated_rows": {
            "P": "6A/5+alpha",
            "Q": "6B/5+beta",
            "R": "3A^2/25+4alpha*A/5+6C/5+gamma",
            "S": "6AB/25+4alpha*B/5+3beta*A/5+6D/5+delta",
            "T": "-4A^3/125-2alpha*A^2/25+6AC/25+2gamma*A/5+3B^2/25+3beta*B/5+4alpha*C/5+epsilon",
        },
        "remaining_system": "I3'=0, I2'=0, omega(A')=0, h*eta(A')=j",
        "omega_closed": False,
        "exterior_ab": "24A^2/125+8alpha*A/25-12C/25-4gamma/5",
        "rank_control": "det(dI3,dI2,omega,eta)=(6/5)^4 at A=B=C=0,D=1 and zero constants",
        "formal_exact_replay": "PASS",
    }


def bivariate_jacobian_controls() -> dict[str, str]:
    # Sparse bivariate integer polynomials for the target-shear controls.
    BPoly = dict[tuple[int, int], int]

    def badd(*polys: BPoly) -> BPoly:
        out: BPoly = {}
        for poly in polys:
            for exponent, coefficient in poly.items():
                out[exponent] = out.get(exponent, 0) + coefficient
        return {exponent: coefficient for exponent, coefficient in out.items() if coefficient}

    def bscale(poly: BPoly, scalar: int) -> BPoly:
        return {exponent: scalar * coefficient for exponent, coefficient in poly.items() if scalar * coefficient}

    def bmul(left: BPoly, right: BPoly) -> BPoly:
        out: BPoly = {}
        for (a, b), c in left.items():
            for (d, e), f in right.items():
                key = (a + d, b + e)
                out[key] = out.get(key, 0) + c * f
        return {exponent: coefficient for exponent, coefficient in out.items() if coefficient}

    def bpow(poly: BPoly, exponent: int) -> BPoly:
        out: BPoly = {(0, 0): 1}
        for _ in range(exponent):
            out = bmul(out, poly)
        return out

    def bd(poly: BPoly, axis: int) -> BPoly:
        out: BPoly = {}
        for exponent, coefficient in poly.items():
            degree = exponent[axis]
            if not degree:
                continue
            reduced = list(exponent)
            reduced[axis] -= 1
            out[tuple(reduced)] = coefficient * degree
        return out

    def bj(first: BPoly, second: BPoly) -> BPoly:
        return badd(bmul(bd(first, 0), bd(second, 1)), bscale(bmul(bd(first, 1), bd(second, 0)), -1))

    x, y = {(1, 0): 1}, {(0, 1): 1}
    one = {(0, 0): 1}
    for degree, power_g in ((1, 6), (2, 3), (3, 2)):
        f = badd(x, {(0, degree): 1})
        g = badd(y, bpow(f, power_g))
        assert bj(f, g) == one
    rejected = bj(badd(x, {(0, 5): 1}), badd(y, {(0, 6): 1}))
    assert rejected == {(0, 0): 1, (0, 5): 6}
    return {
        "divisible_16": "J(x+y,y+(x+y)^6)=1",
        "divisible_26": "J(x+y^2,y+(x+y^2)^3)=1",
        "divisible_36": "J(x+y^3,y+(x+y^3)^2)=1",
        "non_keller_56": "J(x+y^5,y+y^6)=1+6*y^5",
    }


def rational_trajectory_negative_control() -> dict[str, str]:
    # Zero integration constants, A=B=C=0, D=x^-5, h=x^11.
    # Then I2=I3=omega=0 and h*eta(X')=-6, so the Pfaffian ODE itself
    # admits a rational trajectory.  Taking r=-x^-1 makes f(x,0)=0 but
    # leaves g(x,0)=-x^-6/5, exposing the missing polynomial-boundary gate.
    d_coefficient, d_exponent = Fraction(1), -5
    dprime_coefficient, dprime_exponent = Fraction(-5), -6
    eta_coefficient = Fraction(6, 5) * d_coefficient * dprime_coefficient
    eta_exponent = d_exponent + dprime_exponent
    h_coefficient, h_exponent = Fraction(1), 11
    assert h_coefficient * eta_coefficient == -6 and h_exponent + eta_exponent == 0
    r_coefficient, r_exponent = Fraction(-1), -1
    f0_coefficient = r_coefficient**5 + d_coefficient
    assert f0_coefficient == 0 and 5 * r_exponent == d_exponent
    g0_coefficient = r_coefficient**6 + Fraction(6, 5) * d_coefficient * r_coefficient
    assert g0_coefficient == Fraction(-1, 5)
    assert 6 * r_exponent == d_exponent + r_exponent == -6
    return {
        "trajectory": "A=B=C=0, D=x^-5, h=x^11, zero integration constants",
        "pfaffian": "I2'=I3'=omega=0 and h*eta=-6",
        "boundary_test": "r=-x^-1 gives f(x,0)=0 but g(x,0)=-x^-6/5",
        "verdict": "ODE-ALONE-DOES-NOT-CLOSE; polynomial boundary remains essential",
    }


def main() -> None:
    print(
        json.dumps(
            {
                "verdict": "SEXTIC-Y-PREFLIGHT-SURVIVING-PFAFFIAN-GATE",
                "field_characteristic": 0,
                "degree_pairs": degree_pair_sweep(),
                "imprimitive_46": leading_46_split(),
                "leading_56": leading_56_alignment(),
                "coprime_56": canonical_56_system(),
                "controls": bivariate_jacobian_controls(),
                "rational_trajectory_negative_control": rational_trajectory_negative_control(),
                "full_sextic_theorem_proved": False,
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
