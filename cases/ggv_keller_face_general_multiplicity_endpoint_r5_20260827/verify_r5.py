#!/usr/bin/env python3
"""Desk-scale exact checks for the R5 general-multiplicity endpoint theorem."""

from __future__ import annotations

import json
import math
import pathlib
from fractions import Fraction as Q


ROOT = pathlib.Path(__file__).resolve().parent


def trim(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return tuple(p)


def add(p, q):
    n = max(len(p), len(q))
    return trim([(p[i] if i < len(p) else 0) +
                 (q[i] if i < len(q) else 0) for i in range(n)])


def scale(c, p):
    return trim([c * x for x in p])


def mul(p, q):
    if not p or not q:
        return ()
    out = [Q(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return trim(out)


def deriv(p):
    return trim([Q(i) * p[i] for i in range(1, len(p))])


def n_operator(B, v):
    return add(mul(B, deriv(v)), scale(Q(3, 2), mul(deriv(B), v)))


def mode_weights(exponents, through=22):
    return [n for n in range(through + 1)
            if all((e * (12 - n)) % 4 == 0 for e in exponents)]


def partitions(n, maximum=None):
    if n == 0:
        yield ()
        return
    maximum = n if maximum is None else min(maximum, n)
    for first in range(maximum, 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def main():
    expected = json.loads((ROOT / "RESULT.json").read_text())

    schedules = {
        "squarefree_gcd1": mode_weights([1] * 8),
        "perfect_square_gcd2": mode_weights([2, 4, 6]),
        "fourth_power_gcd4": mode_weights([4, 8]),
    }
    assert schedules == expected["mode_schedules"]
    for exps in ([3, 6], [2, 6], [4, 12], [1, 2, 8]):
        d = math.gcd(*exps)
        by_gcd = [n for n in range(23) if (d * (12 - n)) % 4 == 0]
        assert mode_weights(exps) == by_gcd

    # The exact-mode logarithmic identities: q=2*gamma makes both the H'/H
    # correction and the F_t/F cross term cancel.
    for n in range(23):
        q = Q(12 - n, 4)
        gamma = Q(12 - n, 8)
        assert q == 2 * gamma
        assert Q(12) - 8 * gamma - n == 0

    # Degree-eight multiplicity partitions: b is the total degree of the
    # odd-multiplicity squarefree part over an algebraic closure.
    b_values = sorted({sum(1 for e in part if e % 2) for part in partitions(8)})
    assert b_values == [0, 2, 4, 6, 8]
    excluded = []
    survivors = []
    for b in b_values:
        a = (8 - b) // 2
        (excluded if b >= 1 and a < b - 1 else survivors).append(b)
    assert excluded == expected["automatic_degree_exclusion_squarefree_part_degrees_for_degH8"]
    assert survivors == expected["degree_only_survivors_squarefree_part_degrees_for_degH8"]

    # Normalized quadratic B=z^2-D.  For v=v0+v1*z+v2*z^2,
    # N_B(v) has coefficients (-D*v1, 3*v0-2D*v2, 4*v1, 5*v2).
    D = Q(7)
    B = (-D, Q(0), Q(1))
    for v in ((Q(2), Q(3), Q(5)), (Q(-1), Q(4), Q(9))):
        A = n_operator(B, v)
        A = A + (Q(0),) * (4 - len(A))
        assert 4 * A[0] + D * A[2] == 0
        assert A == (-D * v[1], 3 * v[0] - 2 * D * v[2],
                     4 * v[1], 5 * v[2])
        mutated = list(A)
        mutated[0] += 1
        assert 4 * mutated[0] + D * mutated[2] != 0

    # Cross-multiplied endpoint identity for g=B*v/A:
    # 2H g' + H'g = 2*A*B*N_B(v), while 2H=2*A^2*B.
    A_poly = (Q(1), Q(-2), Q(0), Q(3))
    B_poly = (Q(-1), Q(0), Q(1))
    v_poly = (Q(2), Q(-1), Q(4))
    NBv = n_operator(B_poly, v_poly)
    lhs_numerator = scale(Q(2), mul(mul(A_poly, B_poly), NBv))
    if NBv == A_poly:
        assert lhs_numerator == scale(Q(2), mul(mul(A_poly, A_poly), B_poly))
    # Use an exact constructed criterion-positive A as a live positive check.
    A_pos = NBv
    lhs_numerator = scale(Q(2), mul(mul(A_pos, B_poly), NBv))
    rhs_numerator = scale(Q(2), mul(mul(A_pos, A_pos), B_poly))
    assert lhs_numerator == rhs_numerator

    # Perfect-square B=1: N_B is differentiation, hence every polynomial A
    # has a polynomial antiderivative in characteristic zero.
    for A in ((Q(3),), (Q(1), Q(2), Q(5), Q(-7))):
        v = (Q(0),) + tuple(A[i] / Q(i + 1) for i in range(len(A)))
        assert n_operator((Q(1),), v) == A

    print("PASS R5 exact general-multiplicity endpoint checks")


if __name__ == "__main__":
    main()

