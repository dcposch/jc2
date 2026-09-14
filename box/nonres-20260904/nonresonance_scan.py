#!/usr/bin/env python3
"""NON-RESONANCE scan over the u_s>1 Moh census stratum (round 20260904T1200Z, Opus).

Predicate under test (derived from the (99,66) pivot closed form
|coeff| = 9(99 - 3n - 11i) = (n/d_s)(n - u_s j - d_s i), 17(hhhhh)):

    NONRES(S) :=  d_s does not divide u_s * j   for all 1 <= j <= v_s.

Since d_s | n (divisor chain) this is exactly the statement that the ladder
pivot coefficient n - u_s j - d_s i never vanishes in the band range.

Elementary reduction:  d_s = u_s + v_s, g := gcd(u_s, v_s) = gcd(d_s, u_s), so
    NONRES(S)  <=>  d_s / g > v_s  <=>  u_s > (g - 1) * v_s.
In particular g = 1 => NONRES holds automatically.

Read-only: imports the frozen census modules, writes nothing but stdout.
"""
import sys, json
from collections import defaultdict
from math import gcd

SRC = "/home/ubuntu/jc2/box/anchor-gate-20260903"
sys.path.insert(0, SRC)
import moh_skeleton_full as M
import full_tree_partition as FT


def u_s(S):
    return S.d[S.s] - S.V[S.s]


def group_key(S):
    return (S.n, S.m, tuple(S.M[i] for i in range(2, S.s + 1)), S.V[S.s])


def nonres(us, vs):
    ds = us + vs
    g = gcd(us, vs)
    direct = all(us * j % ds != 0 for j in range(1, vs + 1))
    closed = (ds // g) > vs
    assert direct == closed, (us, vs, direct, closed)
    return direct


def main(dlo=48, dhi=200):
    poly_rows = []
    for n in range(dlo, dhi + 1):
        for m, Ms, V in M.census(n, Kmin=16, full=True):
            S = M.Skel(n, m, list(Ms), V)
            if FT.full_tree_ode_ok(S) and FT.full_tree_polynomial_ode_ok(S):
                poly_rows.append(S)
    us_rows = [S for S in poly_rows if u_s(S) > 1]
    groups = defaultdict(list)
    for S in us_rows:
        groups[group_key(S)].append(S)

    controls = {
        "POLY_ODE_rows": len(poly_rows),
        "u_s_gt_1_rows": len(us_rows),
        "u_s_gt_1_groups": len(groups),
    }
    fails, gt1 = [], []
    tab = defaultdict(int)
    for key, rows in sorted(groups.items()):
        S = rows[0]
        us, vs, ds = u_s(S), S.V[S.s], S.d[S.s]
        g = gcd(us, vs)
        ok = nonres(us, vs)
        tab[(us, vs, ds, g, ok)] += 1
        if g > 1:
            gt1.append((S.n, S.m, us, vs, ds, g, ok))
        if not ok:
            fails.append((S.n, S.m, us, vs, ds, g))
    print(json.dumps({
        "controls": controls,
        "distinct_(u_s,v_s,d_s,g,NONRES)_cells": [
            {"u_s": k[0], "v_s": k[1], "d_s": k[2], "gcd": k[3], "NONRES": k[4],
             "groups": v} for k, v in sorted(tab.items())],
        "groups_with_gcd(u_s,v_s)>1": gt1,
        "NONRES_FAILURES": fails,
        "all_groups_nonresonant": not fails,
    }, indent=1))


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 48,
         int(sys.argv[2]) if len(sys.argv) > 2 else 200)
