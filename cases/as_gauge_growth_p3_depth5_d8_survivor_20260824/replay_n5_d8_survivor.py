#!/usr/bin/env python3
"""Deterministic exact replay of the p=3,n=5,D=8 gauge survivor.

Only Python integer arithmetic is used.  Every comparison is made after
coefficientwise reduction modulo 3^5=243.
"""
from __future__ import annotations

import hashlib
import json

Monomial = tuple[int, int]
Poly = dict[Monomial, int]

P_MOD = 3**5
CAP = 8
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


# Structural construction.  A=x+9c and B=y+9d+27f.
c: Poly = {(5, 0): 1, (5, 1): -1}
d: Poly = {(4, 0): 1, (4, 1): 1, (4, 2): 1}
f: Poly = {(4, 1): 7, (4, 2): 5}
A = add(X, scale(9, c))
B = add(Y, scale(9, d), scale(27, f))

S5: Poly = {}
for j in range(5):
    S5 = add(S5, scale(3**j, power(A, 2 * j)))
D_A = add(ONE, scale(-3, power(A, 2)))
P = add(A, scale(-1, power(A, 3)))
Q = multiply(B, S5)

expected_A: Poly = {(1, 0): 1, (5, 0): 9, (5, 1): 234}
expected_B: Poly = {(0, 1): 1, (4, 0): 9, (4, 1): 198, (4, 2): 144}
expected_P: Poly = {
    (7, 1): 27,
    (7, 0): 216,
    (5, 1): 234,
    (5, 0): 9,
    (3, 0): 242,
    (1, 0): 1,
}
expected_Q: Poly = {
    (8, 0): 81,
    (6, 2): 135,
    (6, 1): 189,
    (6, 0): 27,
    (4, 2): 144,
    (4, 1): 207,
    (4, 0): 9,
    (2, 1): 3,
    (0, 1): 1,
}

assert reduce_mod(A) == expected_A
assert reduce_mod(B) == expected_B
assert reduce_mod(P) == expected_P
assert reduce_mod(Q) == expected_Q
assert degree(A) == 6 and degree(B) == 6
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

# Pin the predicted-cap positive control: identity gauge first reaches cap 9.
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
    "equal_cap": CAP,
    "verdict": "EXACT_BOUNDED_SURVIVOR_D8_FALSIFIES_PREDICTED_D9_CAP_LAW",
    "degrees": {"A": degree(A), "B": degree(B), "P": degree(P), "Q": degree(Q)},
    "A": serial(A),
    "B": serial(B),
    "P": serial(P),
    "Q": serial(Q),
    "checks": {
        "identity_branch_mod_3": True,
        "truncated_inverse": True,
        "gauge_orientation_B_equals_QD": True,
        "det_gauge_equals_1": True,
        "det_F_equals_1": True,
        "total_degree_simplex_cap_8": True,
        "identity_gauge_cap_9_positive_control": True,
    },
    "scope_refusals": [
        "no assertion that D=8 is minimal; D=7 remains open",
        "no depth n>=6 survivor assertion",
        "no compatible inverse-limit or polynomial lift assertion",
        "no no-lift conclusion",
        "no A_infinity identification",
        "no Jacobian-conjecture inference",
    ],
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
print(json.dumps(payload, indent=2, sort_keys=True))
