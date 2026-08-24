#!/usr/bin/env python3
"""Exact Cartier obstruction for the frozen p=3,n=5,D=7 point.

Only Python integer arithmetic is used.  Every comparison is made after
coefficientwise reduction modulo 3^5=243.
"""
from __future__ import annotations

import hashlib
import json

Monomial = tuple[int, int]
Poly = dict[Monomial, int]

P_MOD = 3**5
CAP = 7
X: Poly = {(1, 0): 1}
Y: Poly = {(0, 1): 1}
ONE: Poly = {(0, 0): 1}


def add(*polynomials: Poly) -> Poly:
    out: Poly = {}
    for polynomial in polynomials:
        for monomial, coefficient in polynomial.items():
            out[monomial] = out.get(monomial, 0) + coefficient
    return {m: c for m, c in out.items() if c}


def scale(scalar: int, polynomial: Poly) -> Poly:
    return {m: scalar * c for m, c in polynomial.items() if scalar * c}


def multiply(left: Poly, right: Poly) -> Poly:
    out: Poly = {}
    for (i, j), a in left.items():
        for (k, ell), b in right.items():
            monomial = (i + k, j + ell)
            out[monomial] = out.get(monomial, 0) + a * b
    return {m: c for m, c in out.items() if c}


def power(polynomial: Poly, exponent: int) -> Poly:
    out = ONE
    base = polynomial
    while exponent:
        if exponent & 1:
            out = multiply(out, base)
        base = multiply(base, base)
        exponent //= 2
    return out


def derivative(polynomial: Poly, variable: int) -> Poly:
    out: Poly = {}
    for (i, j), coefficient in polynomial.items():
        exponent = i if variable == 0 else j
        if exponent:
            monomial = (i - 1, j) if variable == 0 else (i, j - 1)
            out[monomial] = exponent * coefficient
    return out


def jacobian(left: Poly, right: Poly) -> Poly:
    return add(
        multiply(derivative(left, 0), derivative(right, 1)),
        scale(-1, multiply(derivative(left, 1), derivative(right, 0))),
    )


def reduce_mod(polynomial: Poly, modulus: int = P_MOD) -> Poly:
    return {
        monomial: coefficient % modulus
        for monomial, coefficient in polynomial.items()
        if coefficient % modulus
    }


def degree(polynomial: Poly) -> int:
    reduced = reduce_mod(polynomial)
    return max((sum(monomial) for monomial in reduced), default=-1)


def serial(polynomial: Poly) -> list[dict[str, int | list[int]]]:
    return [
        {"monomial": [i, j], "coefficient": coefficient}
        for (i, j), coefficient in sorted(
            reduce_mod(polynomial).items(), key=lambda item: (-sum(item[0]), -item[0][0], -item[0][1])
        )
    ]


# Exact base-three gauge digits returned by the bounded solve.
b: Poly = {(5, 0): 1}
c: Poly = {(2, 1): 2}
d: Poly = {(1, 2): 1, (5, 0): 1, (7, 0): 2}
e: Poly = {(1, 0): 2, (1, 1): 1, (2, 0): 2, (4, 1): 1, (5, 0): 2}
f: Poly = {
    (0, 1): 1, (0, 2): 1, (1, 1): 2, (0, 3): 1, (1, 2): 2,
    (1, 3): 1, (3, 2): 1, (4, 1): 2, (6, 1): 1, (7, 0): 1,
}
g: Poly = {
    (1, 0): 1, (2, 0): 1, (1, 2): 2, (2, 1): 2, (1, 3): 2,
    (2, 2): 1, (2, 3): 2, (4, 1): 1, (5, 0): 1, (2, 4): 2,
    (7, 0): 2,
}
h: Poly = {
    (0, 1): 1, (0, 2): 1, (1, 1): 2, (0, 4): 1, (1, 4): 2,
    (1, 5): 1, (5, 1): 2, (6, 1): 2,
}
A = add(X, scale(9, c), scale(27, e), scale(81, g))
B = add(Y, scale(3, b), scale(9, d), scale(27, f), scale(81, h))

S5: Poly = {}
for j in range(5):
    S5 = add(S5, scale(3**j, power(A, 2 * j)))
D_A = add(ONE, scale(-3, power(A, 2)))
P = add(A, scale(-1, power(A, 3)))
Q = multiply(B, S5)

expected_A: Poly = {
    (7, 0): 162, (5, 0): 135, (4, 1): 108, (2, 4): 162,
    (2, 3): 162, (2, 2): 81, (2, 1): 180, (2, 0): 135,
    (1, 3): 162, (1, 2): 162, (1, 1): 27, (1, 0): 136,
}
expected_B: Poly = {
    (7, 0): 45, (6, 1): 189, (5, 1): 162, (5, 0): 12,
    (4, 1): 54, (3, 2): 27, (1, 5): 81, (1, 4): 162,
    (1, 3): 27, (1, 2): 63, (1, 1): 216, (0, 4): 81,
    (0, 3): 27, (0, 2): 108, (0, 1): 109,
}
expected_P: Poly = {
    (6, 1): 162, (5, 0): 135, (4, 1): 54, (4, 0): 81,
    (3, 1): 162, (3, 0): 80, (2, 4): 162, (2, 3): 162,
    (2, 2): 81, (2, 1): 180, (2, 0): 135, (1, 3): 162,
    (1, 2): 162, (1, 1): 27, (1, 0): 136,
}
expected_Q: Poly = {
    (7, 0): 81, (6, 1): 216, (5, 1): 162, (5, 0): 12,
    (4, 1): 63, (3, 3): 81, (3, 2): 81, (2, 3): 81,
    (2, 1): 165, (1, 5): 81, (1, 4): 162, (1, 3): 27,
    (1, 2): 63, (1, 1): 216, (0, 4): 81, (0, 3): 27,
    (0, 2): 108, (0, 1): 109,
}

assert reduce_mod(A) == expected_A
assert reduce_mod(B) == expected_B
assert reduce_mod(P) == expected_P
assert reduce_mod(Q) == expected_Q
assert degree(A) == CAP and degree(B) == CAP
assert degree(P) == CAP and degree(Q) == CAP
assert reduce_mod(A, 3) == X
assert reduce_mod(B, 3) == Y
assert reduce_mod(P, 3) == reduce_mod(add(X, scale(-1, power(X, 3))), 3)
assert reduce_mod(Q, 3) == Y

# Truncated inverse and exact gauge orientation modulo 3^5.
assert reduce_mod(multiply(D_A, S5)) == ONE
assert reduce_mod(multiply(Q, D_A)) == reduce_mod(B)

# Both determinant routes are replayed independently.
assert reduce_mod(jacobian(A, B)) == ONE
assert reduce_mod(jacobian(P, Q)) == ONE

# First unfulfilled determinant digit at depth six.
jacobian_error = add(jacobian(A, B), scale(-1, ONE))
assert all(coefficient % P_MOD == 0 for coefficient in jacobian_error.values())
R: Poly = {
    monomial: coefficient // P_MOD
    for monomial, coefficient in jacobian_error.items()
}
expected_R_mod_3: Poly = {
    (10, 0): 1, (8, 0): 1, (7, 1): 1, (7, 0): 1,
    (6, 3): 2, (6, 1): 2, (5, 1): 1, (3, 1): 2,
    (2, 3): 1, (2, 2): 2, (1, 3): 1, (1, 2): 1,
    (1, 1): 1, (1, 0): 2, (0, 3): 2, (0, 2): 1,
    (0, 1): 1, (0, 0): 1,
}
assert reduce_mod(R, 3) == expected_R_mod_3
cartier_rows = {
    monomial: coefficient
    for monomial, coefficient in expected_R_mod_3.items()
    if monomial[0] % 3 == 2 and monomial[1] % 3 == 2
}
assert cartier_rows == {(2, 2): 2}

# Pin the identity-gauge comparison at cap nine.
A9, B9 = X, Y
S5_identity: Poly = {}
for j in range(5):
    S5_identity = add(S5_identity, scale(3**j, power(X, 2 * j)))
P9 = add(X, scale(-1, power(X, 3)))
Q9 = multiply(Y, S5_identity)
assert degree(P9) == 3 and degree(Q9) == 9
assert reduce_mod(jacobian(A9, B9)) == ONE

payload = {
    "modulus": P_MOD,
    "prime": 3,
    "depth": 5,
    "target_depth": 6,
    "equal_cap": CAP,
    "verdict": "FROZEN_D7_POINT_IS_CARTIER_TERMINAL_AT_DEPTH_6_AT_EVERY_CAP",
    "degrees": {"A": degree(A), "B": degree(B), "P": degree(P), "Q": degree(Q)},
    "A": serial(A),
    "B": serial(B),
    "P": serial(P),
    "Q": serial(Q),
    "R_equals_det_minus_1_div_243_mod_3": serial(reduce_mod(R, 3)),
    "cartier_cokernel_rows": serial(cartier_rows),
    "checks": {
        "identity_branch_mod_3": True,
        "truncated_inverse": True,
        "gauge_orientation_B_equals_QD": True,
        "det_gauge_equals_1": True,
        "det_F_equals_1": True,
        "total_degree_simplex_cap_7": True,
        "identity_gauge_cap_9_positive_control": True,
        "representative_invariant_x2y2_cartier_row": True,
    },
    "scope_refusals": [
        "minimum claim uses the separately reviewed depth-four D<=6 emptiness result",
        "terminality is for this frozen depth-five residue class, not all depth-five points",
        "no emptiness assertion for B_(3,6)(D,D) at any D",
        "no compatible inverse-limit or polynomial lift assertion",
        "no no-lift conclusion",
        "no A_infinity identification",
        "no Jacobian-conjecture inference",
    ],
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
print(json.dumps(payload, indent=2, sort_keys=True))
