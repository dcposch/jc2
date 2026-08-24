#!/usr/bin/env python3
"""Exact integer replay of the omitted first divided-linear carry."""
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
            target = (i+k, j+ell)
            out[target] = out.get(target, 0) + a*b
    return {m: c for m, c in out.items() if c}


def derivative(polynomial: Poly, variable: int) -> Poly:
    out: Poly = {}
    for (i, j), coefficient in polynomial.items():
        exponent = i if variable == 0 else j
        if exponent:
            target = (i-1, j) if variable == 0 else (i, j-1)
            out[target] = out.get(target, 0) + exponent*coefficient
    return {m: c for m, c in out.items() if c}


def reduce_mod(polynomial: Poly, modulus: int) -> Poly:
    return {m: c % modulus for m, c in polynomial.items() if c % modulus}


def jacobian(left: Poly, right: Poly) -> Poly:
    return add(multiply(derivative(left, 0), derivative(right, 1)),
               scale(-1, multiply(derivative(left, 1), derivative(right, 0))))


def bracket_first_carry(U: Poly, V: Poly, prime: int) -> Poly:
    ux_seed = add(derivative(U, 0), {(prime-1, 0): -1})
    return add(multiply(ux_seed, derivative(V, 1)),
               scale(-1, multiply(derivative(U, 1), derivative(V, 0))))


# Termwise all-prime lemma for the quadratic bracket only.
for prime in (2, 3, 5, 7, 11, 13):
    for a in range(prime+1):
        for b in range(prime+1):
            c, d = prime-a, prime-b
            assert a*d-b*c == prime*(a-b)
            assert (a*d-b*c) % prime == 0
    print("prime", prime, "quadratic_bracket_cartier", 0,
          "full_divided_linear_cartier", "u[p,p-1]+v[p-1,p]")


# Negative control for the quarantined 29-row system.
# It obeys first divergence and has no carry above degree six, but the omitted
# divided-linear term supplies a nonzero x^2*y^2 Cartier obstruction.
U = {(3, 2): 1}
V = {(2, 1): 1}
p = 3
P0 = {(1, 0): 1, (3, 0): -1}
Y = {(0, 1): 1}
P = add(P0, scale(p, U))
Q = add(Y, scale(p, V))
J = jacobian(P, Q)
assert reduce_mod(add(J, {(0, 0): -1}), 9) == {}
residual_Z = {m: c//9 for m, c in add(J, {(0, 0): -1}).items()}
assert all(9*c == add(J, {(0, 0): -1})[m]
           for m, c in residual_Z.items())
residual = reduce_mod(residual_Z, 3)

K = reduce_mod(bracket_first_carry(U, V, p), p)
linear = add(derivative(U, 0), derivative(V, 1), {(2, 0): -1})
assert all(c % p == 0 for c in linear.values())
linear_over_p = reduce_mod({m: c//p for m, c in linear.items()}, p)
assert K == {(4, 0): 2, (4, 2): 2}
assert K.get((2, 2), 0) == 0
assert linear_over_p == {(2, 2): 1}
assert residual == add(K, linear_over_p)
assert residual.get((2, 2), 0) == 1
assert max(sum(m) for m in K) <= 6

print("negative_control_U", U)
print("negative_control_V", V)
print("integer_J_minus_1", add(J, {(0, 0): -1}))
print("quadratic_K_mod3", K)
print("divided_linear_carry_mod3", linear_over_p)
print("full_residual_mod3", residual)
print("cartier_x2y2", residual[(2, 2)])
print("PASS-DIVIDED-LINEAR-CARRY-ERRATUM")
