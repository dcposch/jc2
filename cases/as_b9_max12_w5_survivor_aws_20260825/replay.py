#!/usr/bin/env python3
"""Exact, dependency-free replay of the registered B9 Z/81 and Z/243 maps."""

from __future__ import annotations

import hashlib
import json

Poly = dict[tuple[int, int], int]


def clean(p: Poly) -> Poly:
    return {m: c for m, c in p.items() if c}


def add(*ps: Poly) -> Poly:
    out: Poly = {}
    for p in ps:
        for m, c in p.items():
            out[m] = out.get(m, 0) + c
    return clean(out)


def sc(a: int, p: Poly) -> Poly:
    return clean({m: a * c for m, c in p.items()})


def mul(p: Poly, q: Poly) -> Poly:
    out: Poly = {}
    for (i, j), a in p.items():
        for (k, ell), b in q.items():
            m = i + k, j + ell
            out[m] = out.get(m, 0) + a * b
    return clean(out)


def pw(p: Poly, n: int) -> Poly:
    out: Poly = {(0, 0): 1}
    while n:
        if n & 1:
            out = mul(out, p)
        p = mul(p, p)
        n //= 2
    return out


def der(p: Poly, axis: int) -> Poly:
    out: Poly = {}
    for (i, j), c in p.items():
        e = i if axis == 0 else j
        if e:
            m = (i - 1, j) if axis == 0 else (i, j - 1)
            out[m] = out.get(m, 0) + e * c
    return clean(out)


def jac(p: Poly, q: Poly) -> Poly:
    return add(mul(der(p, 0), der(q, 1)), sc(-1, mul(der(p, 1), der(q, 0))))


def modp(p: Poly, n: int) -> Poly:
    return clean({m: c % n for m, c in p.items()})


def canon(p: Poly) -> list[list[int]]:
    return [[i, j, p[i, j]] for i, j in sorted(p)]


def dydeg(p: Poly) -> int:
    return max(j for i, j in p)


def tdeg(p: Poly) -> int:
    return max(i + j for i, j in p)


ONE = {(0, 0): 1}
X = {(1, 0): 1}
Y = {(0, 1): 1}
u = add(X, pw(Y, 3))
p0 = add(u, sc(-1, pw(u, 3)))
q0 = add(Y, pw(u, 4))

p4 = add(p0, sc(18, mul(u, Y)))
q4 = add(q0, sc(3, mul(pw(u, 2), Y)), sc(72, pw(Y, 2)))

r5 = add(sc(2, mul(u, Y)), mul(X, pw(Y, 2)))
s5 = add(pw(Y, 2), mul(pw(X, 4), pw(Y, 2)), mul(X, pw(Y, 11)))
p5 = add(p4, sc(81, r5))
q5 = add(q4, sc(81, s5))

d4 = jac(p4, q4)
d5 = jac(p5, q5)
expected_d4 = add(
    ONE,
    sc(-81, pw(u, 4)),
    sc(162, Y),
    sc(-486, mul(pw(u, 2), Y)),
    sc(2592, pw(Y, 2)),
)
assert d4 == expected_d4
assert modp(d4, 81) == ONE
assert modp(d5, 243) == ONE
assert modp(p5, 3) == modp(p0, 3)
assert modp(q5, 3) == modp(q0, 3)
assert (dydeg(p5), dydeg(q5)) == (9, 12)
assert (tdeg(p5), tdeg(q5)) == (9, 12)
assert modp(d4, 243) != ONE

# Independent replay of the registered linearized source identities.
def lin(r: Poly, s: Poly) -> Poly:
    return add(der(r, 0), sc(-1, mul(pw(u, 3), der(r, 1))), der(s, 1))


r_a = sc(2, mul(u, Y))
s_a = pw(Y, 2)
r_b = mul(X, pw(Y, 2))
s_b = add(mul(pw(X, 4), pw(Y, 2)), mul(X, pw(Y, 11)))
assert modp(lin(r_a, s_a), 3) == modp(add(pw(u, 4), Y), 3)
assert modp(lin(r_b, s_b), 3) == modp(pw(Y, 2), 3)

payload = {
    "P5": canon(p5),
    "Q5": canon(q5),
    "det5": canon(d5),
    "degrees_y": [dydeg(p5), dydeg(q5)],
    "degrees_total": [tdeg(p5), tdeg(q5)],
}
blob = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()

print("source_reduction=B9")
print("z81_determinant=1")
print("linearized_u4_plus_y_identity=true")
print("linearized_y2_identity=true")
print("actual_y_degrees=9,12")
print("actual_total_degrees=9,12")
print("parent_without_81_digit_fails_mod243=true")
print("determinant_mod243=1")
print("determinant_terms=" + str(len(d5)))
print("payload_sha256=" + hashlib.sha256(blob).hexdigest())
print("AS-B9-MAX12-W5-SURVIVOR PASS")
