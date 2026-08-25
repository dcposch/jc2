#!/usr/bin/env python3
"""Independent exact controls beyond the corrected D9/D8 gate."""
from __future__ import annotations

from collections import defaultdict


def add(*polys):
    out = defaultdict(int)
    for poly in polys:
        for monomial, coefficient in poly.items():
            out[monomial] += coefficient
    return {m: c for m, c in out.items() if c}


def scale(scalar, poly):
    return {m: scalar*c for m, c in poly.items() if scalar*c}


def mul(left, right):
    out = defaultdict(int)
    for (i, j), a in left.items():
        for (k, ell), b in right.items():
            out[(i+k, j+ell)] += a*b
    return {m: c for m, c in out.items() if c}


def derivative(poly, axis):
    out = {}
    for (i, j), coefficient in poly.items():
        exponent = (i, j)[axis]
        if exponent:
            key = (i-1, j) if axis == 0 else (i, j-1)
            out[key] = coefficient*exponent
    return out


def bracket(left, right):
    return add(mul(derivative(left, 0), derivative(right, 1)),
               scale(-1, mul(derivative(left, 1), derivative(right, 0))))


def reduce_mod(poly, modulus):
    return {m: c % modulus for m, c in poly.items() if c % modulus}


# Full mod-81 points on the corrected 9-fibre and 729-fibre structural
# representatives.  The optional 3*x^4 in Q distinguishes them but has no
# y derivative and hence does not change the determinant.
expected_jacobian = {
    (0, 0): 1,
    (4, 0): 81,
    (6, 0): 648,
    (8, 0): 1134,
}
expected_residual = {(4, 0): 1, (6, 0): 2, (8, 0): 2}
for w in (0, 1):
    P = {(1, 0): 1, (3, 0): -1, (5, 0): 18, (7, 0): 54}
    Q = {(0, 1): 1, (2, 1): 3}
    if w:
        Q[(4, 0)] = 3
    jacobian = bracket(P, Q)
    assert jacobian == expected_jacobian, (w, jacobian)
    assert reduce_mod(jacobian, 81) == {(0, 0): 1}
    residual = {m: (c-(1 if m == (0, 0) else 0))//81 % 3
                for m, c in jacobian.items()
                if (c-(1 if m == (0, 0) else 0))//81 % 3}
    assert residual == expected_residual, (w, residual)
    assert residual[(8, 0)] == 2

# Particular corrected high-row representatives.  At the following divided
# carry, total degree 12 comes only from N={C,D}; lower C,D pieces and a new
# cap-seven digit reach at most degree 11 in every other cross term.
C3 = {(7, 0): 2}
D3 = {(5, 1): 1, (6, 1): 2}
N3 = reduce_mod(bracket(C3, D3), 3)
assert N3 == {(11, 0): 2, (12, 0): 1}, N3

C81 = {(4, 2): 1, (6, 1): 2}
D81 = {(7, 0): 2}
N81 = reduce_mod(bracket(C81, D81), 3)
assert N81 == {(10, 1): 2, (12, 0): 2}, N81

print("full_mod81_jacobian", sorted(expected_jacobian.items()))
print("next_residual_mod3", sorted(expected_residual.items()))
print("particular_3_fibre_N", sorted(N3.items()))
print("particular_81_fibre_N", sorted(N81.items()))
print("PASS-CORRECTED-NEXT-CARRY-CONTROLS")
