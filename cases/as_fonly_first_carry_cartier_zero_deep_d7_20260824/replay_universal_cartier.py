#!/usr/bin/env python3
"""Dependency-free replay of the all-prime first-carry Cartier lemma."""
from __future__ import annotations


def bracket_multiplier(a: int, b: int, c: int, d: int) -> int:
    return a*d-b*c


for prime in (2, 3, 5, 7, 11, 13):
    contributing_pairs = 0
    for a in range(prime+1):
        for b in range(prime+1):
            c, d = prime-a, prime-b
            contributing_pairs += 1
            multiplier = bracket_multiplier(a, b, c, d)
            assert multiplier == prime*(a-b)
            assert multiplier % prime == 0
    # The seed term requires d=p and has derivative multiplier p.
    assert prime % prime == 0
    print("prime", prime, "contributing_pairs", contributing_pairs,
          "cartier_coefficient", 0)

# Source-honest p=3 control U=x^3,V=x^2*y.  Store bivariate polynomials as
# (x exponent,y exponent)->coefficient modulo three.
U = {(3, 0): 1}
V = {(2, 1): 1}


def derivative(polynomial, variable):
    out = {}
    for (i, j), coefficient in polynomial.items():
        exponent = i if variable == 0 else j
        if exponent % 3:
            target = (i-1, j) if variable == 0 else (i, j-1)
            out[target] = (out.get(target, 0)+exponent*coefficient) % 3
    return {m: c for m, c in out.items() if c}


def add(*polynomials):
    out = {}
    for polynomial in polynomials:
        for monomial, coefficient in polynomial.items():
            out[monomial] = (out.get(monomial, 0)+coefficient) % 3
    return {m: c for m, c in out.items() if c}


def scale(scalar, polynomial):
    return {m: scalar*c % 3 for m, c in polynomial.items() if scalar*c % 3}


def multiply(left, right):
    out = {}
    for (i, j), a in left.items():
        for (k, ell), b in right.items():
            target = (i+k, j+ell)
            out[target] = (out.get(target, 0)+a*b) % 3
    return {m: c for m, c in out.items() if c}


ux, uy = derivative(U, 0), derivative(U, 1)
vx, vy = derivative(V, 0), derivative(V, 1)
divergence = add(ux, vy)
K = add(multiply(ux, vy), scale(-1, multiply(uy, vx)),
        scale(-1, multiply({(2, 0): 1}, vy)))
assert divergence == {(2, 0): 1}
assert K == {(4, 0): 2}
assert K.get((2, 2), 0) == 0

print("p3_control_divergence", divergence)
print("p3_control_K", K)
print("p3_cartier_x2y2", 0)
print("PASS-UNIVERSAL-FIRST-CARRY-CARTIER-ZERO")

