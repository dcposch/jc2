#!/usr/bin/env python3
"""Exact integer controls for the scoped D7 degree-ten pointwise gate."""
from __future__ import annotations

Poly = dict[tuple[int, int], int]


def add(*polynomials: Poly) -> Poly:
    out: Poly = {}
    for polynomial in polynomials:
        for monomial, coefficient in polynomial.items():
            out[monomial] = out.get(monomial, 0) + coefficient
    return {m: c for m, c in out.items() if c}


def scale(scalar: int, polynomial: Poly) -> Poly:
    return {m: scalar*c for m, c in polynomial.items() if scalar*c}


def multiply(left: Poly, right: Poly) -> Poly:
    out: Poly = {}
    for (i, j), a in left.items():
        for (k, ell), b in right.items():
            monomial = (i+k, j+ell)
            out[monomial] = out.get(monomial, 0) + a*b
    return {m: c for m, c in out.items() if c}


def derivative(polynomial: Poly, variable: int) -> Poly:
    out: Poly = {}
    for (i, j), coefficient in polynomial.items():
        exponent = i if variable == 0 else j
        if exponent:
            monomial = (i-1, j) if variable == 0 else (i, j-1)
            out[monomial] = out.get(monomial, 0) + exponent*coefficient
    return {m: c for m, c in out.items() if c}


def jacobian(left: Poly, right: Poly) -> Poly:
    return add(multiply(derivative(left, 0), derivative(right, 1)),
               scale(-1, multiply(derivative(left, 1), derivative(right, 0))))


def mod(polynomial: Poly, modulus: int) -> Poly:
    return {m: c % modulus for m, c in polynomial.items() if c % modulus}


def degree(polynomial: Poly) -> int:
    return max((sum(m) for m in polynomial), default=-1)


def exact_quotient(polynomial: Poly, divisor: int) -> Poly:
    assert all(coefficient % divisor == 0 for coefficient in polynomial.values())
    return {m: c // divisor for m, c in polynomial.items() if c // divisor}


def divergence_antiderivative(residual_mod3: Poly) -> tuple[Poly, Poly]:
    """Choose E,F of cap <=7 with residual+E_x+F_y=0 over F_3."""
    E: Poly = {}
    F: Poly = {}
    for (i, j), coefficient in sorted(residual_mod3.items()):
        target = (-coefficient) % 3
        if (i+1) % 3:
            inverse = 1 if (i+1) % 3 == 1 else 2
            E[(i+1, j)] = (target*inverse) % 3
        elif (j+1) % 3:
            inverse = 1 if (j+1) % 3 == 1 else 2
            F[(i, j+1)] = (target*inverse) % 3
        else:
            raise AssertionError(f"Cartier obstruction at {(i, j)}")
    E = {m: c for m, c in E.items() if c}
    F = {m: c for m, c in F.items() if c}
    assert mod(add(residual_mod3, derivative(E, 0), derivative(F, 1)), 3) == {}
    assert max(degree(E), degree(F)) <= 7
    return E, F


X = {(1, 0): 1}
Y = {(0, 1): 1}
P0 = {(1, 0): 1, (3, 0): -1}

controls = {
    # degree-five-zero vertical radical component
    "vertical": ({}, {(2, 1): 1}, {(5, 0): 2}, {}),
    # rational-normal-cone endpoint a=u5_0 != 0
    "a_endpoint": ({(0, 5): 1}, {(2, 1): 1},
                   {(5, 0): 2, (2, 5): 2}, {}),
    # opposite endpoint g=v5_5 != 0
    "g_endpoint": ({}, {(2, 1): 1, (5, 0): 1}, {(5, 0): 2}, {}),
}

for name, (U, V, C, D) in controls.items():
    P2 = add(P0, scale(3, U), scale(9, C))
    Q2 = add(Y, scale(3, V), scale(9, D))
    J2m1 = add(jacobian(P2, Q2), {(0, 0): -1})
    assert mod(J2m1, 27) == {}
    R2_Z = exact_quotient(J2m1, 27)
    R2 = mod(R2_Z, 3)
    assert all(sum(m) != 10 for m in R2)
    print(name)
    print(" U", U)
    print(" V", V)
    print(" C", C)
    print(" D", D)
    print(" residual_over_27_mod3", R2)
    if degree(R2) <= 6:
        E, F = divergence_antiderivative(R2)
        P3 = add(P2, scale(27, E))
        Q3 = add(Q2, scale(27, F))
        J3m1 = add(jacobian(P3, Q3), {(0, 0): -1})
        assert mod(J3m1, 81) == {}
        assert degree(P3) <= 7 and degree(Q3) <= 7
        print(" cap7_mod81_extension", 1)
        print(" E", E)
        print(" F", F)
        print(" P_mod81", mod(P3, 81))
        print(" Q_mod81", mod(Q3, 81))
        print(" J_minus_1_mod81", mod(J3m1, 81))
    else:
        # A cap-seven third digit has divergence degree at most six.
        assert any(sum(m) >= 7 and c % 3 for m, c in R2.items())
        print(" cap7_mod81_extension", 0)
        print(" cap_boundary_failure", {
            m: c for m, c in R2.items() if sum(m) >= 7
        })

print("PASS-DEGREE10-ENDPOINT-CONTROLS")
