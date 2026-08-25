#!/usr/bin/env python3
"""Dependency-free exact replay for the AS B9 Z/27 survivor.

This script intentionally uses a tiny integer polynomial implementation.  It
must be executed on AWS under the campaign compute policy, not on the local
Mac.
"""

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


def scale(a: int, p: Poly) -> Poly:
    return clean({m: a * c for m, c in p.items()})


def mul(p: Poly, q: Poly) -> Poly:
    out: Poly = {}
    for (i, j), a in p.items():
        for (k, ell), b in q.items():
            m = (i + k, j + ell)
            out[m] = out.get(m, 0) + a * b
    return clean(out)


def power(p: Poly, n: int) -> Poly:
    out = {(0, 0): 1}
    base = p
    while n:
        if n & 1:
            out = mul(out, base)
        base = mul(base, base)
        n //= 2
    return out


def deriv(p: Poly, axis: int) -> Poly:
    out: Poly = {}
    for (i, j), c in p.items():
        e = i if axis == 0 else j
        if not e:
            continue
        m = (i - 1, j) if axis == 0 else (i, j - 1)
        out[m] = out.get(m, 0) + e * c
    return clean(out)


def jac(p: Poly, q: Poly) -> Poly:
    return add(mul(deriv(p, 0), deriv(q, 1)),
               scale(-1, mul(deriv(p, 1), deriv(q, 0))))


def mod_poly(p: Poly, modulus: int) -> Poly:
    return clean({m: c % modulus for m, c in p.items()})


def eval_mod(p: Poly, x: int, y: int, modulus: int) -> int:
    return sum(c * pow(x, i, modulus) * pow(y, j, modulus)
               for (i, j), c in p.items()) % modulus


def degree_y(p: Poly) -> int:
    return max(j for (_, j) in p)


def degree_total(p: Poly) -> int:
    return max(i + j for (i, j) in p)


def canonical(p: Poly) -> list[list[int]]:
    return [[i, j, p[(i, j)]] for i, j in sorted(p)]


ONE = {(0, 0): 1}
X = {(1, 0): 1}
Y = {(0, 1): 1}

u = add(X, power(Y, 3))
p0 = add(u, scale(-1, power(u, 3)))
v = add(Y, power(u, 4))

# Intermediate W2 point and the registered W3 point.
p_w2 = p0
q_w2 = add(v, scale(3, mul(power(u, 2), Y)))
p_w3 = add(p0, scale(18, mul(u, Y)))
q_w3 = add(q_w2, scale(18, power(Y, 2)))

det_w2 = jac(p_w2, q_w2)
det_w3 = jac(p_w3, q_w3)

expected_w2 = add(ONE, scale(-9, power(u, 4)))
expected_w3 = add(
    ONE,
    scale(-81, power(u, 4)),
    scale(54, Y),
    scale(-162, mul(power(u, 2), Y)),
    scale(648, power(Y, 2)),
)

assert det_w2 == expected_w2
assert mod_poly(det_w2, 9) == ONE
assert det_w3 == expected_w3
assert mod_poly(det_w3, 27) == ONE

# Exact source reduction and actual partial degrees.
assert mod_poly(p_w3, 3) == mod_poly(p0, 3)
assert mod_poly(q_w3, 3) == mod_poly(v, 3)
assert degree_y(p_w3) == 9
assert degree_y(q_w3) == 12
assert degree_total(p_w3) == 9
assert degree_total(q_w3) == 12

# Integer Frobenius guard: the mixed coefficients are present over Z.
assert p0[(2, 3)] == -3
assert p0[(1, 6)] == -3

# Explicit noninjective special fibre.
z0 = (eval_mod(p0, 0, 0, 3), eval_mod(v, 0, 0, 3))
z1 = (eval_mod(p0, 2, 2, 3), eval_mod(v, 2, 2, 3))
assert (0, 0) != (2, 2)
assert z0 == z1 == (0, 0)

# Omission controls: both W3 correction terms are detected.
det_no_p18 = jac(p0, q_w3)
det_no_q18 = jac(p_w3, q_w2)
assert mod_poly(det_no_p18, 27) != ONE
assert mod_poly(det_no_q18, 27) != ONE

payload = {
    "u": canonical(u),
    "P": canonical(p_w3),
    "Q": canonical(q_w3),
    "determinant": canonical(det_w3),
    "expected_determinant": canonical(expected_w3),
    "degrees_y": [degree_y(p_w3), degree_y(q_w3)],
    "degrees_total": [degree_total(p_w3), degree_total(q_w3)],
    "collision": [[0, 0], [2, 2], list(z0)],
}
blob = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()

print("source_reduction=B9")
print("w2_determinant_mod9=1")
print("integer_frobenius_mixed_terms_retained=true")
print("actual_y_degrees=9,12")
print("special_fibre_collision=(0,0),(2,2)->(0,0)")
print("exact_determinant=" + json.dumps(canonical(det_w3), separators=(",", ":")))
print("exact_determinant_formula=1-81*u^4+54*y-162*u^2*y+648*y^2")
print("determinant_mod27=1")
print("omit_18uy_detected=true")
print("omit_18y2_detected=true")
print("payload_sha256=" + hashlib.sha256(blob).hexdigest())
print("AS-B9-MAX12-W3-SURVIVOR PASS")
