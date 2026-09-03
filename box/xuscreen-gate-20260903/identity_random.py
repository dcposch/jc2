#!/usr/bin/env python3
"""Is 1 - S(alpha) = n/(n+m) (1 - delta_1(path)) an algebraic identity of Def 5.1(3)?
Test with random path multiplicities V_j (j=2..s-1), any positive integers."""
import sys, random
from fractions import Fraction as F
sys.path.insert(0, "/tmp/jc2-lane.AQwgL6/inputs")
import moh_skeleton_full as M
import full_tree_partition as FT
from hand_check import one_leaf_check, minor_child_order
random.seed(20260903)
rows = []
for n in range(48, 201):
    for m, Ms, V in M.census(n, Kmin=16, full=True):
        rows.append(M.Skel(n, m, list(Ms), V))
bad = 0; tests = 0; badmin = 0; tmin = 0
for S in rows[::7]:
    E = FT.evaluator(S)
    for _ in range(5):
        path = list(E.initial_path())
        for i in range(2, S.s):
            path[i] = random.randint(1, 30)
        path = tuple(path)
        try:
            Sa, lhs, rhs = one_leaf_check(S, path)
        except ZeroDivisionError:
            continue
        tests += 1
        if lhs != rhs: bad += 1
        for j in range(2, S.s):
            for v in (1, 2, 3):
                try:
                    dist, drv = minor_child_order(S, path, j, v)
                except ZeroDivisionError:
                    continue
                tmin += 1
                if dist != drv: badmin += 1
print("random-path leaf identity mismatches:", bad, "/", tests)
print("random-path minor-order identity mismatches:", badmin, "/", tmin)
