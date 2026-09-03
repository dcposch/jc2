#!/usr/bin/env python3
"""Independent recomputation of Xu's IM and the Im floor from tree DISTANCES.

Basis (gate-derived from Xu pp.4-7, all exact):
  Lemma 4.1 at a root alpha of f_xi:  f_y(alpha) * d/dt g(alpha) = J t^-2.
  ord f_y(alpha) = sum_{j != i} ord(alpha - alpha_j) =: -S(alpha)   (f-tree distances only)
  major alpha: ord g(alpha) = S(alpha) - 1 < 0        -> IM = sum_major (1 - S(alpha))
  minor alpha: final order delta_sigma = S(alpha) > 1  (Xu p.6: ord f_y(alpha) = -delta)
So IM and every final minor order are functions of the ultrametric f-root tree alone.
Ultrametric: two roots in different children of a level-j node are at distance delta_j.
Roots of the two points at infinity are at distance -1 (delta_s = -1).

This script does NOT import xu_screen.py.  It only uses moh_skeleton_full.Skel for
(n,m,M,d,V) and Def 5.1(3) radii, and full_tree_partition.evaluator.level_data for
(A_j,P_j,Q_j) at a node (the operative full-tree model).
"""
import sys
from fractions import Fraction as F
from itertools import combinations_with_replacement
sys.path.insert(0, "/tmp/jc2-lane.AQwgL6/inputs")
import moh_skeleton_full as M
import full_tree_partition as FT

def radii(S, path):
    E = FT.evaluator(S, polynomial_recenter=True, ode_nondegenerate=True)
    return {i: E.radius(i, path) for i in range(1, S.s + 1)}

def one_leaf_check(S, path):
    """Selected-path bottom major leaf: compare distance-based 1-S(alpha) with
    Moh Prop 4.6 (n/(n+m))(1-delta_1) as used by the driver."""
    n, m, s = S.n, S.m, S.s
    d = S.d
    r = radii(S, path)
    # roots in the level-j disc on the path (j = s-1..1): N_j = path[j+1]*m/d_{j+1}
    N = {j: F(path[j + 1] * m, d[j + 1]) for j in range(1, s)}
    N[s] = F(m)                      # whole root set at the top (distance -1 split)
    Sa = F(0)
    Sa += (N[s] - N[s - 1]) * 1      # principal side at distance -1 -> contributes +1 each
    for j in range(s - 1, 1, -1):
        Sa -= (N[j] - N[j - 1]) * r[j]
    Sa -= (N[1] - 1) * r[1]
    lhs = 1 - Sa
    rhs = F(n, n + m) * (1 - r[1])
    return Sa, lhs, rhs

def minor_child_order(S, path, j, v):
    """S_out/N for a minor child of multiplicity v (units m/d_j) at level j on path;
    compare with driver floor delta_j + (d_j/(n-M_j))(1-delta_j)/v."""
    n, m, s = S.n, S.m, S.s
    d = S.d
    r = radii(S, path)
    N = {i: F(path[i + 1] * m, d[i + 1]) for i in range(j, s)}
    N[s] = F(m)
    Nc = F(v * m, d[j])
    Sout = (N[s] - N[s - 1]) * 1
    for i in range(s - 1, j, -1):
        Sout -= (N[i] - N[i - 1]) * r[i]
    Sout -= (N[j] - Nc) * r[j]
    dist = Sout / Nc
    drv = r[j] + F(d[j], n - S.M[j]) * (1 - r[j]) / v
    return dist, drv

def census_rows():
    rows = []
    for n in range(48, 201):
        for m, Ms, V in M.census(n, Kmin=16, full=True):
            S = M.Skel(n, m, list(Ms), V)
            if FT.full_tree_polynomial_ode_ok(S):
                rows.append(S)
    return rows

if __name__ == "__main__":
    rows = census_rows()
    print("operative rows:", len(rows))
    bad46 = 0; badmin = 0; tested_min = 0; m_over_d2_one = 0
    for S in rows:
        E = FT.evaluator(S, polynomial_recenter=True, ode_nondegenerate=True)
        path = list(E.initial_path())
        for i in range(2, S.s + 1):
            path[i] = S.V[i]
        path = tuple(path)
        Sa, lhs, rhs = one_leaf_check(S, path)
        if lhs != rhs:
            bad46 += 1
            if bad46 <= 3: print("PROP4.6 MISMATCH", S.n, S.m, dict(S.M), dict(S.V), lhs, rhs)
        if S.m // S.d[2] == 1: m_over_d2_one += 1
        # minor-child order identity at every level j on the selected path, all v <= lo
        for j in range(2, S.s):
            delta, L, A, P, Q, lo = E.level_data(j, path)
            for v in range(1, P + 1):
                if v <= lo:
                    tested_min += 1
                    dist, drv = minor_child_order(S, path, j, v)
                    if dist != drv:
                        badmin += 1
                        if badmin <= 3: print("MINOR-ORDER MISMATCH", S.n, S.m, j, v, dist, drv)
    print("Prop4.6 identity (1-S = n/(n+m)(1-delta_1)) mismatches on selected path:", bad46, "/", len(rows))
    print("minor first-zero-order identity (S_out/N = driver floor) mismatches:", badmin, "/", tested_min)
    print("rows with m/d_2 == 1 (singleton-risk):", m_over_d2_one)
