#!/usr/bin/env python3
"""Exact full-D12 W2->W3 gate for the AS-source-transformed B8 seed.

Campaign policy requires running this script on AWS, never as substantive
local computation.  It uses only Python's standard library and exact integer
arithmetic; the finite-field solve is deterministic RREF over F_3.
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
    return add(mul(der(p, 0), der(q, 1)),
               sc(-1, mul(der(p, 1), der(q, 0))))


def modp(p: Poly, modulus: int) -> Poly:
    return clean({m: c % modulus for m, c in p.items()})


def dydeg(p: Poly) -> int:
    return max(j for _, j in p)


def tdeg(p: Poly) -> int:
    return max(i + j for i, j in p)


def canon(p: Poly) -> list[list[int]]:
    return [[i, j, p[i, j]] for i, j in sorted(p)]


def basis_poly(m: tuple[int, int]) -> Poly:
    return {m: 1}


def lin_direct(r: Poly, s: Poly) -> Poly:
    return modp(add(jac(P0, s), jac(r, Q0)), 3)


def lin_formula(r: Poly, s: Poly) -> Poly:
    return modp(add(
        sc(-1, mul(pw(Y, 3), der(r, 0))),
        der(r, 1),
        sc(-1, mul(add(ONE, sc(2, mul(u, pw(Y, 3)))), der(s, 0))),
        sc(2, mul(u, der(s, 1))),
    ), 3)


def solve_rref(columns: list[Poly], rhs: Poly,
               rows: list[tuple[int, int]]) -> tuple[int, list[int], bool]:
    """Return rank, zero-free-variable particular, consistency over F_3."""
    a = [[columns[c].get(m, 0) % 3 for c in range(len(columns))]
         + [rhs.get(m, 0) % 3] for m in rows]
    pivot_row = 0
    pivots: list[int] = []
    n = len(columns)
    for col in range(n):
        hit = next((r for r in range(pivot_row, len(a)) if a[r][col]), None)
        if hit is None:
            continue
        a[pivot_row], a[hit] = a[hit], a[pivot_row]
        if a[pivot_row][col] == 2:
            a[pivot_row] = [(2 * z) % 3 for z in a[pivot_row]]
        for r in range(len(a)):
            if r == pivot_row or not a[r][col]:
                continue
            factor = a[r][col]
            a[r] = [(a[r][j] - factor * a[pivot_row][j]) % 3
                    for j in range(n + 1)]
        pivots.append(col)
        pivot_row += 1
        if pivot_row == len(a):
            break
    consistent = all(any(row[:n]) or row[n] == 0 for row in a)
    particular = [0] * n
    if consistent:
        for r, col in enumerate(pivots):
            particular[col] = a[r][n]
    return len(pivots), particular, consistent


ONE: Poly = {(0, 0): 1}
X: Poly = {(1, 0): 1}
Y: Poly = {(0, 1): 1}

u = add(X, pw(Y, 4))
P0 = add(Y, pw(u, 2))
Q0 = add(pw(u, 3), sc(-1, u))

# Source-honest integer seed and Frobenius guards.
assert jac(P0, Q0) == add(ONE, sc(-3, pw(u, 2)))
assert P0[(1, 4)] == 2
assert Q0[(2, 4)] == 3
assert Q0[(1, 8)] == 3

# Complete full-D12 basis and all determinant row positions.
mons12 = [(i, j) for d in range(13) for i in range(d + 1)
          for j in [d - i]]
rows22 = [(i, j) for d in range(23) for i in range(d + 1)
          for j in [d - i]]
assert len(mons12) == 91
assert len(rows22) == 276

columns: list[Poly] = []
for m in mons12:
    r = basis_poly(m)
    direct = lin_direct(r, {})
    formula = lin_formula(r, {})
    assert direct == formula
    columns.append(direct)
for m in mons12:
    s = basis_poly(m)
    direct = lin_direct({}, s)
    formula = lin_formula({}, s)
    assert direct == formula
    columns.append(direct)
assert len(columns) == 182

# Full W2 affine gate, with a hand-derived structured point.
R2 = mul(pw(u, 2), Y)
S2: Poly = {}
assert lin_direct(R2, S2) == modp(pw(u, 2), 3)
rank2, particular2, consistent2 = solve_rref(columns, modp(pw(u, 2), 3), rows22)
assert consistent2
P2 = add(P0, sc(3, R2))
Q2 = Q0
det2 = jac(P2, Q2)
assert det2 == add(ONE, sc(-9, pw(u, 4)))
assert modp(det2, 9) == ONE

# Complete next digit over the registered structured W2 point.
rank3, solution, consistent3 = solve_rref(columns, modp(pw(u, 4), 3), rows22)
assert rank3 == rank2

if not consistent3:
    payload = {
        "status": "OBSTRUCTION",
        "rank": rank3,
        "variables": len(columns),
        "rows": len(rows22),
    }
    blob = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    print("source_reduction=B8")
    print("full_d12_variables=182")
    print("determinant_rows=276")
    print(f"cartier_rank={rank3}")
    print("w2_consistent=true")
    print("w3_consistent=false")
    print("payload_sha256=" + hashlib.sha256(blob).hexdigest())
    print("AS-B8-MAX12-W3-OBSTRUCTION PASS")
    raise SystemExit(0)

R3: Poly = {}
S3: Poly = {}
for value, m in zip(solution[:91], mons12):
    if value:
        R3[m] = value
for value, m in zip(solution[91:], mons12):
    if value:
        S3[m] = value
assert lin_direct(R3, S3) == modp(pw(u, 4), 3)

P3 = add(P2, sc(9, R3))
Q3 = add(Q2, sc(9, S3))
det3 = jac(P3, Q3)
assert modp(det3, 27) == ONE
assert modp(P3, 3) == modp(P0, 3)
assert modp(Q3, 3) == modp(Q0, 3)
assert (dydeg(P3), dydeg(Q3)) == (8, 12)
assert (tdeg(P3), tdeg(Q3)) == (8, 12)
assert modp(det2, 27) != ONE

# Explicit collision in the special fibre.
def ev(p: Poly, x: int, y: int, modulus: int) -> int:
    return sum(c * pow(x, i, modulus) * pow(y, j, modulus)
               for (i, j), c in p.items()) % modulus


z0 = ev(P0, 0, 0, 3), ev(Q0, 0, 0, 3)
z1 = ev(P0, 1, 2, 3), ev(Q0, 1, 2, 3)
assert z0 == z1 == (0, 0)

payload = {
    "status": "SURVIVOR",
    "rank": rank3,
    "nullity": len(columns) - rank3,
    "R3": canon(R3),
    "S3": canon(S3),
    "P3": canon(P3),
    "Q3": canon(Q3),
    "det3": canon(det3),
    "degrees_y": [dydeg(P3), dydeg(Q3)],
    "degrees_total": [tdeg(P3), tdeg(Q3)],
}
blob = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()

print("source_reduction=B8")
print("full_d12_variables=182")
print("determinant_rows=276")
print(f"cartier_rank={rank3}")
print(f"cartier_nullity={len(columns)-rank3}")
print("transported_operator_matches_direct_all_columns=true")
print("w2_structured_correction=3*u^2*y,0")
print("w2_determinant=1-9*u^4")
print("w2_consistent=true")
print("w3_consistent=true")
print("R3=" + json.dumps(canon(R3), separators=(",", ":")))
print("S3=" + json.dumps(canon(S3), separators=(",", ":")))
print("actual_y_degrees=8,12")
print("actual_total_degrees=8,12")
print("parent_without_9_digit_fails_mod27=true")
print("determinant_mod27=1")
print("special_fibre_collision=(0,0),(1,2)->(0,0)")
print("payload_sha256=" + hashlib.sha256(blob).hexdigest())
print("AS-B8-MAX12-W3-SURVIVOR PASS")
