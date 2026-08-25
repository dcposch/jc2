#!/usr/bin/env python3
"""Exact complete-D12 next-digit solve above the frozen B9 Z/243 point."""

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
d5 = jac(p5, q5)
assert modp(d5, 243) == ONE

residual: Poly = {}
for m in set(d5) | {(0, 0)}:
    c = d5.get(m, 0) - ONE.get(m, 0)
    assert c % 243 == 0
    if c // 243:
        residual[m] = c // 243
res3 = modp(residual, 3)
target = modp(sc(-1, res3), 3)


def lin(r: Poly, s: Poly) -> Poly:
    return modp(add(der(r, 0), sc(-1, mul(pw(u, 3), der(r, 1))), der(s, 1)), 3)


mons = [(i, j) for d in range(13) for i in range(d + 1) for j in [d - i]]
columns: list[tuple[str, tuple[int, int], Poly]] = []
for m in mons:
    columns.append(("P", m, lin({m: 1}, {})))
for m in mons:
    columns.append(("Q", m, lin({}, {m: 1})))

row_mons = sorted(set(target).union(*(set(col) for _, _, col in columns)))
matrix = [[col.get(m, 0) % 3 for _, _, col in columns] + [target.get(m, 0) % 3]
          for m in row_mons]

# Deterministic reduced row echelon form over F_3.
pivots: list[int] = []
r = 0
for c in range(len(columns)):
    pivot = next((rr for rr in range(r, len(matrix)) if matrix[rr][c] % 3), None)
    if pivot is None:
        continue
    matrix[r], matrix[pivot] = matrix[pivot], matrix[r]
    inv = 1 if matrix[r][c] == 1 else 2
    matrix[r] = [(inv * z) % 3 for z in matrix[r]]
    for rr in range(len(matrix)):
        if rr != r and matrix[rr][c]:
            a = matrix[rr][c]
            matrix[rr] = [(x - a * y) % 3 for x, y in zip(matrix[rr], matrix[r])]
    pivots.append(c)
    r += 1
    if r == len(matrix):
        break

for row in matrix:
    assert any(row[:-1]) or row[-1] == 0, "inconsistent complete D12 next digit"

solution = [0] * len(columns)
for rr, c in enumerate(pivots):
    solution[c] = matrix[rr][-1]

r6: Poly = {}
s6: Poly = {}
support: list[list[object]] = []
for value, (side, m, _) in zip(solution, columns):
    if not value:
        continue
    (r6 if side == "P" else s6)[m] = value
    support.append([side, m[0], m[1], value])

assert lin(r6, s6) == target
p6 = add(p5, sc(243, r6))
q6 = add(q5, sc(243, s6))
d6 = jac(p6, q6)
assert modp(d6, 729) == ONE
assert modp(d5, 729) != ONE
assert max(dydeg(p6), dydeg(q6)) <= 12
assert max(tdeg(p6), tdeg(q6)) <= 12

next_residual: Poly = {}
for m in set(d6) | {(0, 0)}:
    c = d6.get(m, 0) - ONE.get(m, 0)
    assert c % 729 == 0
    if c // 729:
        next_residual[m] = c // 729

payload = {
    "parent_residual_mod3": canon(res3),
    "rank": len(pivots),
    "rows": len(row_mons),
    "columns": len(columns),
    "pivots": pivots,
    "correction_support": support,
    "P6": canon(p6),
    "Q6": canon(q6),
    "det6": canon(d6),
    "next_residual_mod3": canon(modp(next_residual, 3)),
}
blob = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()

print("parent_residual_mod3=" + json.dumps(canon(res3), separators=(",", ":")))
print(f"next_digit_matrix={len(row_mons)}x{len(columns)}")
print(f"next_digit_rank={len(pivots)}")
print("correction_support=" + json.dumps(support, separators=(",", ":")))
print("exact_source_identity=true")
print("parent_without_243_digit_fails_mod729=true")
print(f"actual_y_degrees={dydeg(p6)},{dydeg(q6)}")
print(f"actual_total_degrees={tdeg(p6)},{tdeg(q6)}")
print("determinant_mod729=1")
print("next_residual_mod3=" + json.dumps(canon(modp(next_residual, 3)), separators=(",", ":")))
print("payload_sha256=" + hashlib.sha256(blob).hexdigest())
print("AS-B9-MAX12-W6-NEXT-DIGIT PASS")
