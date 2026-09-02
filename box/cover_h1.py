#!/usr/bin/env python3
r"""cover_h1.py -- H_1 of a finite-index covering of a group presentation.

Consumer for the ACS-1 covering  C^2 \ F^{-1}(A) --> C^2 \ A  (degree td).
Given a finite presentation of pi_1(C^2 \ A) and a transitive permutation
representation rho into S_k, returns H_1 of the corresponding k-sheeted
covering space, i.e. the abelianization of the point-stabiliser preimage.

MATHEMATICAL GATE (see report ideation-20260902T0022Z-opus5.md sec.3):
the covering space of a Keller counterexample IS a plane-curve complement
C^2 \ E, so H_1 must be FREE abelian of rank #components(E).
Any torsion is a kill.

Method.  Cover of the presentation 2-complex: C_2 = Z[S]^m -> C_1 = Z[S]^n
-> C_0 = Z[S], S = the k sheets.  d_2 is the Fox-derivative matrix with
each generator replaced by its permutation matrix (built here by an
explicit lift-walk, no symbolic Fox calculus).  Since im(d_1) is free,
    coker(d_2) = H_1 (+) Z^(k-1)   for connected (transitive) rho,
so one Smith normal form of d_2 gives both torsion and rank.

Words are lists of signed 1-based generator indices.  Permutations are
tuples of length k giving images of 0..k-1.
"""
from __future__ import annotations

from itertools import product as iproduct
from typing import Dict, List, Sequence, Tuple

Perm = Tuple[int, ...]


def perm_inv(p: Perm) -> Perm:
    out = [0] * len(p)
    for i, v in enumerate(p):
        out[v] = i
    return tuple(out)


def perm_mul(p: Perm, q: Perm) -> Perm:
    """(p*q)(i) = p(q(i))."""
    return tuple(p[q[i]] for i in range(len(q)))


def is_transitive(gens: Sequence[Perm], k: int) -> bool:
    seen = {0}
    stack = [0]
    while stack:
        c = stack.pop()
        for g in gens:
            t = g[c]
            if t not in seen:
                seen.add(t)
                stack.append(t)
    return len(seen) == k


def d2_matrix(n_gens: int, relators: Sequence[Sequence[int]],
              rho: Sequence[Perm], k: int) -> List[List[int]]:
    """Rows indexed by (generator, sheet); columns by (relator, sheet)."""
    inv = [perm_inv(p) for p in rho]
    rows = n_gens * k
    cols = len(relators) * k
    mat = [[0] * cols for _ in range(rows)]
    for r_idx, rel in enumerate(relators):
        for s in range(k):
            col = r_idx * k + s
            c = s
            for letter in rel:
                g = abs(letter) - 1
                if letter > 0:
                    mat[g * k + c][col] += 1
                    c = rho[g][c]
                else:
                    c = inv[g][c]
                    mat[g * k + c][col] -= 1
    return mat


def smith_invariants(mat: List[List[int]]) -> List[int]:
    """Nonzero elementary divisors of an integer matrix (own SNF, no deps)."""
    m = [row[:] for row in mat]
    rows, cols = len(m), (len(m[0]) if m else 0)
    divisors: List[int] = []
    r0 = c0 = 0
    while r0 < rows and c0 < cols:
        piv = None
        best = None
        for i in range(r0, rows):
            for j in range(c0, cols):
                v = abs(m[i][j])
                if v and (best is None or v < best):
                    best, piv = v, (i, j)
        if piv is None:
            break
        while True:
            i, j = piv
            m[r0], m[i] = m[i], m[r0]
            for row in m:
                row[c0], row[j] = row[j], row[c0]
            p = m[r0][c0]
            changed = False
            for i in range(r0 + 1, rows):
                if m[i][c0]:
                    q = m[i][c0] // p
                    if q:
                        for j2 in range(c0, cols):
                            m[i][j2] -= q * m[r0][j2]
                    if m[i][c0]:
                        changed = True
            for j2 in range(c0 + 1, cols):
                if m[r0][j2]:
                    q = m[r0][j2] // p
                    if q:
                        for i2 in range(r0, rows):
                            m[i2][j2] -= q * m[i2][c0]
                    if m[r0][j2]:
                        changed = True
            if not changed:
                break
            best = None
            piv = None
            for i in range(r0, rows):
                for j in range(c0, cols):
                    v = abs(m[i][j])
                    if v and (best is None or v < best):
                        best, piv = v, (i, j)
        # clear the pivot row/col exactly (they are now divisible)
        p = m[r0][c0]
        for i in range(r0 + 1, rows):
            if m[i][c0]:
                q = m[i][c0] // p
                for j2 in range(c0, cols):
                    m[i][j2] -= q * m[r0][j2]
        for j2 in range(c0 + 1, cols):
            if m[r0][j2]:
                q = m[r0][j2] // p
                for i2 in range(r0, rows):
                    m[i2][j2] -= q * m[i2][c0]
        divisors.append(abs(p))
        r0 += 1
        c0 += 1
    # make the divisor chain divide successively
    changed = True
    while changed:
        changed = False
        for i in range(len(divisors) - 1):
            a, b = divisors[i], divisors[i + 1]
            if b % a:
                import math
                g = math.gcd(a, b)
                divisors[i], divisors[i + 1] = g, a * b // g
                changed = True
    return divisors


def cover_h1(n_gens: int, relators: Sequence[Sequence[int]],
             rho: Sequence[Perm], k: int) -> Dict[str, object]:
    assert is_transitive(rho, k), "rho must be transitive (connected cover)"
    mat = d2_matrix(n_gens, relators, rho, k)
    divs = smith_invariants(mat)
    rank_d2 = len(divs)
    torsion = [d for d in divs if d > 1]
    free_rank = n_gens * k - rank_d2 - (k - 1)
    return {"free_rank": free_rank, "torsion": torsion,
            "rank_d2": rank_d2, "matrix_shape": (len(mat), len(mat[0]) if mat else 0)}


def fmt(res: Dict[str, object]) -> str:
    t = res["torsion"]
    tail = "" if not t else " (+) " + " (+) ".join("Z/%d" % d for d in t)
    return "Z^%d%s" % (res["free_rank"], tail)


def comm(a: int, b: int) -> List[int]:
    return [a, b, -a, -b]


def _controls() -> None:
    print("== CONTROL 1  two transverse lines: pi_1 = Z^2, 2-sheeted")
    r = cover_h1(2, [comm(1, 2)], [(1, 0), (0, 1)], 2)
    print("   H_1 =", fmt(r), " expected Z^2 (index-2 subgroup of Z^2)")

    print("== CONTROL 2  trivial rho on Z^2 (k=1): H_1 = Z^2")
    r = cover_h1(2, [comm(1, 2)], [(0,), (0,)], 1)
    print("   H_1 =", fmt(r), " expected Z^2")

    print("== CONTROL 3  cuspidal cubic complement pi_1 = B_3 = trefoil group")
    trefoil = [[1, 2, 1, -2, -1, -2]]
    r = cover_h1(2, trefoil, [(0,), (0,)], 1)
    print("   base H_1 =", fmt(r), " expected Z^1 (one component)")
    r = cover_h1(2, trefoil, [(1, 0), (1, 0)], 2)
    print("   cyclic 2-fold H_1 =", fmt(r),
          " expected Z (+) Z/3   [Delta_trefoil(-1) = 3]")
    r = cover_h1(2, trefoil, [(1, 0, 2), (0, 2, 1)], 3)
    print("   irregular 3-fold H_1 =", fmt(r))


if __name__ == "__main__":
    _controls()
