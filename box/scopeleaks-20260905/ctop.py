#!/usr/bin/env python3
"""(C-TOP): the ONE new inequality carried by the descended (child) tower.

Child datum (Prop 6.3 p.197(2) + Moh p.202->p.207, 5/5 columns):
  n' = u_s n/d_s, M'_i = u_s M_i/d_s (i=1..s-1), V'_i = V_i, s' = s-1,
  d'_r = gcd{n',M'_1..M'_{r-1}} = u_s d_r/d_s  (r <= s'),
  d'_{s'+1} = gcd(d'_{s'},M'_{s'}) = u_s.
p.190 display: deg p(pi) = V_{r+1} d_r/d_{r+1} >= V_r  (multiplicity <= degree).
On the child this reads, for r < s', V'_r <= V_{r+1}d_r/d_{r+1} -- the PARENT's
own (7), nothing new -- and at the child's top r = s':

      (C-TOP)   V_{s-1}  <=  u_s d_{s-1}/d_s   ( = d'_{s'} )

U-NEGATIVE (V_2 > d'_2 = u_s d_2/d_s) is a consequence of ~(C-TOP) via the
parent chain V_2 <= V_{s-1} d_2/d_{s-1}.
"""
from __future__ import annotations
import os, sys, json, time, collections
from fractions import Fraction as F
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "centre-gate-20260903")))
import moh_skeleton_full_frozen as B
from opus5_probe import Tree


def operative(n, m, Ms, V):
    T = Tree(n, m, Ms, gate=False, ode=True, capacity=False, passport=False)
    T.recenter = True; T._memo = {}; T.why = []
    if not (T.d[T.s] > V[T.s] > F(T.d[T.s], 2)):
        return False
    return T.ok(T.s - 1, (V[T.s],), True, tuple(V[i] for i in range(T.s - 1, 1, -1))) is not None


def row(n, m, Ms, V):
    sk = B.Skel(n, m, list(Ms), V)
    s = sk.s; ds = sk.d[s]; vs = V[s]; us = ds - vs
    dtop_child = F(us * sk.d[s - 1], ds)          # d'_{s'}
    d2p = F(us * sk.d[2], ds)                     # d'_2 = gcd(n',m')
    return dict(n=n, m=m, Ms=tuple(Ms), V=dict(V), s=s, sp=s - 1, d_s=ds, u_s=us, v_s=vs,
                ell=vs - us - 1, n1=n * us // ds, m1=m * us // ds,
                d2=sk.d[2], dsm1=sk.d[s - 1], V2=V[2], Vsm1=V[s - 1],
                d2p=d2p, dtop_child=dtop_child,
                ctop=(F(V[s - 1]) <= dtop_child), uneg=(F(V[2]) > d2p),
                delta_s=sk.delta[s])


def main(nlo=16, nhi=200):
    t0 = time.time(); rows = []
    for n in range(nlo, nhi + 1):
        for (m, Ms, V) in B.census(n, Kmin=2, full=True):
            r = row(n, m, Ms, V); r["op"] = operative(n, m, Ms, V); rows.append(r)
    op = [r for r in rows if r["op"]]
    print("census %d rows, operative %d  (%.0fs)" % (len(rows), len(op), time.time() - t0))
    print("delta_s == -1 on all rows:", all(r["delta_s"] == -1 for r in rows))

    def rep(lab, rs):
        nc = [r for r in rs if not r["ctop"]]
        nu = [r for r in rs if r["uneg"]]
        print("\n== %s (%d rows) ==" % (lab, len(rs)))
        print("  ~(C-TOP)      : %d" % len(nc))
        print("  U-NEGATIVE    : %d" % len(nu))
        print("  U-NEG & CTOP  : %d   (must be 0: chain V_2<=V_{s-1}d_2/d_{s-1})"
              % len([r for r in nu if r["ctop"]]))
        print("  ~CTOP by u_s  :", dict(sorted(collections.Counter(r["u_s"] for r in nc).items())))
        print("  ~CTOP by s'   :", dict(sorted(collections.Counter(r["sp"] for r in nc).items())))
        print("  ~CTOP u_s=1   : %d   <- unconditional (Prop 6.4 discharges (R))"
              % len([r for r in nc if r["u_s"] == 1]))
        print("  ~CTOP u_s>=2  : %d   <- kill-or-split dichotomy"
              % len([r for r in nc if r["u_s"] >= 2]))
        return nc

    rep("CENSUS (1)-(13), 16<=n<=%d, Kmin=2" % nhi, rows)
    nc_op = rep("OPERATIVE C_FULL_TREE_POLYNOMIAL_ODE", op)

    surv = [r for r in op if r["ctop"]]
    print("\nOPERATIVE residue AFTER (C-TOP): %d -> %d rows, %d degree pairs"
          % (len(op), len(surv), len({(r["n"], r["m"]) for r in surv})))
    print("  survivors by s' :", dict(sorted(collections.Counter(r["sp"] for r in surv).items())))
    print("  survivors by u_s:", dict(sorted(collections.Counter(r["u_s"] for r in surv).items())))
    print("\n~(C-TOP) operative rows, u_s=1, by degree:")
    for (n, m), c in sorted(collections.Counter((r["n"], r["m"]) for r in nc_op
                                                if r["u_s"] == 1).items()):
        print("   (%d,%d): %d" % (n, m, c))
    print("~(C-TOP) operative rows, u_s>=2:")
    for r in [x for x in nc_op if x["u_s"] >= 2]:
        print("   n=%d m=%d M=%s V=%s  s=%d u_s=%d v_s=%d  V_{s-1}=%d > d'=%s"
              % (r["n"], r["m"], list(r["Ms"]), r["V"], r["s"], r["u_s"], r["v_s"],
                 r["Vsm1"], r["dtop_child"]))

    def ser(r):
        d = dict(r); d["Ms"] = list(r["Ms"]); d["V"] = {str(k): v for k, v in r["V"].items()}
        for k in ("d2p", "dtop_child", "delta_s"):
            d[k] = str(r[k])
        return d
    json.dump(dict(census=len(rows), operative=len(op),
                   ctop_fail_census=len([r for r in rows if not r["ctop"]]),
                   ctop_fail_operative=[ser(r) for r in nc_op],
                   operative_after_ctop=[ser(r) for r in surv]),
              open(os.path.join(HERE, "ctop.json"), "w"), indent=1)
    print("\nwrote ctop.json (%.0fs)" % (time.time() - t0))


if __name__ == "__main__":
    a = sys.argv[1:]
    main(int(a[0]) if a else 16, int(a[1]) if len(a) > 1 else 200)
