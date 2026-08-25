#!/usr/bin/env python3
"""Exact B8 fixed-D12 `(8,12)` W2->W3 gate; AWS execution only."""

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


def modp(p: Poly, n: int) -> Poly:
    return clean({m: c % n for m, c in p.items()})


def canon(p: Poly) -> list[list[int]]:
    return [[i, j, p[i, j]] for i, j in sorted(p)]


def dydeg(p: Poly) -> int:
    return max(j for _, j in p)


def tdeg(p: Poly) -> int:
    return max(i + j for i, j in p)


def divide_exact(p: Poly, n: int) -> Poly:
    assert all(c % n == 0 for c in p.values())
    return clean({m: c // n for m, c in p.items()})


def lin_direct(r: Poly, s: Poly) -> Poly:
    return modp(add(jac(P0, s), jac(r, Q0)), 3)


def lin_formula(r: Poly, s: Poly) -> Poly:
    return modp(add(
        sc(-1, mul(pw(Y, 3), der(r, 0))),
        der(r, 1),
        sc(-1, mul(add(ONE, sc(2, mul(u, pw(Y, 3)))), der(s, 0))),
        sc(2, mul(u, der(s, 1))),
    ), 3)


def solve(columns: list[Poly], rhs: Poly,
          rows: list[tuple[int, int]]) -> tuple[int, list[int], bool]:
    a = [[columns[c].get(m, 0) % 3 for c in range(len(columns))]
         + [rhs.get(m, 0) % 3] for m in rows]
    n = len(columns)
    pr = 0
    pivots: list[int] = []
    for col in range(n):
        hit = next((r for r in range(pr, len(a)) if a[r][col]), None)
        if hit is None:
            continue
        a[pr], a[hit] = a[hit], a[pr]
        if a[pr][col] == 2:
            a[pr] = [(2 * z) % 3 for z in a[pr]]
        for r in range(len(a)):
            if r != pr and a[r][col]:
                f = a[r][col]
                a[r] = [(a[r][j] - f * a[pr][j]) % 3
                        for j in range(n + 1)]
        pivots.append(col)
        pr += 1
    ok = all(any(row[:n]) or row[n] == 0 for row in a)
    sol = [0] * n
    if ok:
        for r, col in enumerate(pivots):
            sol[col] = a[r][n]
    return len(pivots), sol, ok


def unpack(v: list[int], mons_r: list[tuple[int, int]],
           mons_s: list[tuple[int, int]]) -> tuple[Poly, Poly]:
    r = {m: z for m, z in zip(mons_r, v[:len(mons_r)]) if z}
    s = {m: z for m, z in zip(mons_s, v[len(mons_r):]) if z}
    return r, s


ONE: Poly = {(0, 0): 1}
X: Poly = {(1, 0): 1}
Y: Poly = {(0, 1): 1}
u = add(X, pw(Y, 4))
P0 = add(Y, pw(u, 2))
Q0 = add(pw(u, 3), sc(-1, u))

assert jac(P0, Q0) == add(ONE, sc(-3, pw(u, 2)))
assert P0[(1, 4)] == 2
assert Q0[(2, 4)] == 3 and Q0[(1, 8)] == 3

mons_all = [(i, d - i) for d in range(13) for i in range(d + 1)]
mons_r = [m for m in mons_all if m[1] <= 8]
mons_s = list(mons_all)
rows = [(i, d - i) for d in range(23) for i in range(d + 1)]
assert (len(mons_r), len(mons_s), len(rows)) == (81, 91, 276)

columns: list[Poly] = []
for m in mons_r:
    b = {m: 1}
    assert lin_direct(b, {}) == lin_formula(b, {})
    columns.append(lin_direct(b, {}))
for m in mons_s:
    b = {m: 1}
    assert lin_direct({}, b) == lin_formula({}, b)
    columns.append(lin_direct({}, b))
assert len(columns) == 172

# Complete W2 solve in the exact coordinate envelope.
rank2, sol2, ok2 = solve(columns, modp(pw(u, 2), 3), rows)
if not ok2:
    payload = {"status": "W2_OBSTRUCTION", "rank": rank2,
               "variables": 172, "rows": 276}
    blob = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    print("source_reduction=B8")
    print("coordinate_slots=81,91")
    print("full_d12_variables=172")
    print("determinant_rows=276")
    print(f"cartier_rank={rank2}")
    print("w2_consistent=false")
    print("payload_sha256=" + hashlib.sha256(blob).hexdigest())
    print("AS-B8-MAX12-W2-OBSTRUCTION PASS")
    raise SystemExit(0)

R2, S2 = unpack(sol2, mons_r, mons_s)
assert lin_direct(R2, S2) == modp(pw(u, 2), 3)
P2, Q2 = add(P0, sc(3, R2)), add(Q0, sc(3, S2))
det2 = jac(P2, Q2)
assert modp(det2, 9) == ONE
assert (dydeg(P2), dydeg(Q2)) == (8, 12)
assert (tdeg(P2), tdeg(Q2)) == (8, 12)

E2 = divide_exact(add(det2, sc(-1, ONE)), 9)
rhs3 = modp(sc(-1, E2), 3)
rank3, sol3, ok3 = solve(columns, rhs3, rows)
assert rank3 == rank2
if not ok3:
    payload = {"status": "W3_POINT_OBSTRUCTION", "rank": rank3,
               "R2": canon(R2), "S2": canon(S2), "E2": canon(E2)}
    blob = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    print("source_reduction=B8")
    print("coordinate_slots=81,91")
    print("full_d12_variables=172")
    print("determinant_rows=276")
    print(f"cartier_rank={rank3}")
    print("w2_consistent=true")
    print("w3_consistent=false")
    print("R2=" + json.dumps(canon(R2), separators=(",", ":")))
    print("S2=" + json.dumps(canon(S2), separators=(",", ":")))
    print("payload_sha256=" + hashlib.sha256(blob).hexdigest())
    print("AS-B8-MAX12-W3-POINT-OBSTRUCTION PASS")
    raise SystemExit(0)

R3, S3 = unpack(sol3, mons_r, mons_s)
assert lin_direct(R3, S3) == rhs3
P3, Q3 = add(P2, sc(9, R3)), add(Q2, sc(9, S3))
det3 = jac(P3, Q3)
assert modp(det3, 27) == ONE
assert modp(P3, 3) == modp(P0, 3)
assert modp(Q3, 3) == modp(Q0, 3)
assert (dydeg(P3), dydeg(Q3)) == (8, 12)
assert (tdeg(P3), tdeg(Q3)) == (8, 12)
assert modp(det2, 27) != ONE

def ev(p: Poly, x: int, y: int, n: int) -> int:
    return sum(c * pow(x, i, n) * pow(y, j, n)
               for (i, j), c in p.items()) % n


assert (ev(P0, 0, 0, 3), ev(Q0, 0, 0, 3)) == (0, 0)
assert (ev(P0, 1, 2, 3), ev(Q0, 1, 2, 3)) == (0, 0)

payload = {
    "status": "W3_SURVIVOR", "rank": rank3, "nullity": 172-rank3,
    "R2": canon(R2), "S2": canon(S2), "E2": canon(E2),
    "R3": canon(R3), "S3": canon(S3),
    "P3": canon(P3), "Q3": canon(Q3), "det3": canon(det3),
    "degrees_y": [dydeg(P3), dydeg(Q3)],
    "degrees_total": [tdeg(P3), tdeg(Q3)],
}
blob = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()

print("source_reduction=B8")
print("coordinate_slots=81,91")
print("full_d12_variables=172")
print("determinant_rows=276")
print(f"cartier_rank={rank3}")
print(f"cartier_nullity={172-rank3}")
print("transported_operator_matches_direct_all_columns=true")
print("w2_consistent=true")
print("w3_consistent=true")
print("R2=" + json.dumps(canon(R2), separators=(",", ":")))
print("S2=" + json.dumps(canon(S2), separators=(",", ":")))
print("E2=" + json.dumps(canon(E2), separators=(",", ":")))
print("R3=" + json.dumps(canon(R3), separators=(",", ":")))
print("S3=" + json.dumps(canon(S3), separators=(",", ":")))
print("actual_y_degrees=8,12")
print("actual_total_degrees=8,12")
print("parent_without_9_digit_fails_mod27=true")
print("determinant_mod27=1")
print("special_fibre_collision=(0,0),(1,2)->(0,0)")
print("payload_sha256=" + hashlib.sha256(blob).hexdigest())
print("AS-B8-MAX12-W3-SURVIVOR PASS")
