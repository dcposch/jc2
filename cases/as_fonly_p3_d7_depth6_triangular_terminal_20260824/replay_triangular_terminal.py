#!/usr/bin/env python3
"""Dependency-free exact replay of the F-only triangular D7 point."""
from __future__ import annotations

Monomial = tuple[int, int]
Poly = dict[Monomial, int]


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


def reduce_poly(polynomial: Poly, modulus: int) -> Poly:
    return {m: c % modulus for m, c in polynomial.items() if c % modulus}


def degree(polynomial: Poly) -> int:
    return max((sum(m) for m, c in polynomial.items() if c), default=-1)


def ordered(polynomial: Poly):
    return sorted(polynomial.items(), key=lambda item: (sum(item[0]), item[0]))


X: Poly = {(1, 0): 1}
Y: Poly = {(0, 1): 1}
ONE: Poly = {(0, 0): 1}
P: Poly = {(1, 0): 1, (3, 0): 2, (5, 0): 441, (7, 0): 108}
Q: Poly = {(0, 1): 1, (2, 1): -6, (4, 1): 18, (6, 1): -27}

assert degree(P) == degree(Q) == 7
assert reduce_poly(P, 3) == {(1, 0): 1, (3, 0): 2}
assert reduce_poly(Q, 3) == Y

J = jacobian(P, Q)
literal_expected: Poly = {
    (0, 0): 1,
    (4, 0): 2187,
    (6, 0): -12393,
    (8, 0): 34992,
    (10, 0): -45927,
    (12, 0): -20412,
}
assert J == literal_expected
assert reduce_poly(J, 729) == ONE

# Choose a clean representative of the same depth-six residue for the
# obstruction modulo 2187: 1566=108+2*729.
P_tilde: Poly = {(1, 0): 1, (3, 0): 2, (5, 0): 441, (7, 0): 1566}
J_tilde = jacobian(P_tilde, Q)
expected_mod_2187 = {(0, 0): 1, (12, 0): (-729) % 2187}
assert reduce_poly(J_tilde, 2187) == expected_mod_2187

# The coefficientwise modular derivative gives the same short identity.
px_modular: Poly = {(0, 0): 1, (2, 0): 6, (4, 0): 18, (6, 0): 27}
qy = derivative(Q, 1)
assert multiply(px_modular, qy) == {(0, 0): 1, (12, 0): -729}

error = add(J_tilde, scale(-1, ONE))
assert all(coefficient % 729 == 0 for coefficient in error.values())
residual = {m: (coefficient // 729) % 3 for m, coefficient in error.items()
            if (coefficient // 729) % 3}
assert residual == {(12, 0): 2}

# Every derivative of a cap-seven digit has total degree at most six.
digit_monomials = [(i, total-i) for total in range(8) for i in range(total+1)]
divergence_support = set()
for i, j in digit_monomials:
    if i:
        divergence_support.add((i-1, j))
    if j:
        divergence_support.add((i, j-1))
assert max(map(sum, divergence_support)) == 6
assert (12, 0) not in divergence_support

print("P", ordered(P))
print("Q", ordered(Q))
print("degrees", degree(P), degree(Q))
print("special_fibre_P", ordered(reduce_poly(P, 3)))
print("special_fibre_Q", ordered(reduce_poly(Q, 3)))
print("literal_integer_determinant", ordered(J))
print("clean_lift_P", ordered(P_tilde))
print("det_clean_lift_mod_2187", ordered(reduce_poly(J_tilde, 2187)))
print("det_mod_729", ordered(reduce_poly(J, 729)))
print("modular_derivative_product", ordered(multiply(px_modular, qy)))
print("next_residual_mod3", ordered(residual))
print("max_cap7_divergence_degree", 6)
print("PASS-FONLY-P3-D7-N6-SURVIVOR-N7-TERMINAL")
