#!/usr/bin/env python3
"""SCOPE lane: enumerate the two residual families of the (H1)&(H2) reduction.

  (a) U-NEGATIVE : descended datum has V'_2 > d'_2 = gcd(n',m'), i.e. u' < 0.
  (b) s' >= 3    : descended tower height s' = s-1 >= 3.

Descent (Prop 6.3, banked closed form, validated against Moh p.207 in
box/moh14-20260905/descend14.py):
   u_s = d_s - V_s, v_s = V_s, ell = v_s - u_s - 1
   (n',m') = ((n/d_s) u_s, (m/d_s) u_s),  M'_i = M_i u_s/d_s (i=2..s-1),
   V'_i = V_i,  s' = s-1,  d'_2 = gcd(n',m') = K'.
Screens: (1)-(13) census [Kmin=2 = Moh's own space]; operative
C_FULL_TREE_POLYNOMIAL_ODE (opus5_probe.Tree gate=False, ode=True, recenter).
"""
from __future__ import annotations
import os, sys, json, time
from fractions import Fraction as F
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
CENTRE = os.path.abspath(os.path.join(HERE, "..", "centre-gate-20260903"))
sys.path.insert(0, CENTRE)
import moh_skeleton_full_frozen as B          # noqa: E402
from opus5_probe import Tree                  # noqa: E402


def operative(n, m, Ms, V):
    """PROMOTED whole-tree screen C_FULL_TREE_POLYNOMIAL_ODE (17(r)/(hh)/(ll))."""
    T = Tree(n, m, Ms, gate=False, ode=True, capacity=False, passport=False)
    T.recenter = True; T._memo = {}; T.why = []
    if not (T.d[T.s] > V[T.s] > F(T.d[T.s], 2)):
        return False
    need = tuple(V[i] for i in range(T.s - 1, 1, -1))
    return T.ok(T.s - 1, (V[T.s],), True, need) is not None


def descend(n, m, Ms, V):
    sk = B.Skel(n, m, list(Ms), V)
    s, ds, Vs = sk.s, sk.d[sk.s], V[sk.s]
    us, vs = ds - Vs, Vs
    n1, m1 = n * us // ds, m * us // ds
    Mp = tuple(F(sk.M[i] * us, ds) for i in range(2, s))     # M'_2..M'_{s-1}
    d2p = gcd(n1, m1)
    return dict(s=s, sp=s - 1, d_s=ds, u_s=us, v_s=vs, ell=vs - us - 1,
                n1=n1, m1=m1, Mp=Mp, Vp=tuple(V[i] for i in range(2, s)),
                d2p=d2p, V2p=V[2], up=d2p - V[2], d2=sk.d[2],
                exact=all(x.denominator == 1 for x in Mp) and (n * us) % ds == 0
                      and (m * us) % ds == 0)


def main(nlo=16, nhi=200, Kmin=2):
    t0 = time.time()
    rows = []
    for n in range(nlo, nhi + 1):
        for (m, Ms, V) in B.census(n, Kmin=Kmin, full=True):
            d = descend(n, m, Ms, V)
            d["n"], d["m"], d["Ms"], d["V"] = n, m, tuple(Ms), dict(V)
            d["op"] = operative(n, m, Ms, V)
            rows.append(d)
        if n % 20 == 0:
            print("  n=%d: %d rows (%.0fs)" % (n, len(rows), time.time() - t0), flush=True)
    print("CENSUS (1)-(13) Kmin=%d, %d<=n<=%d: %d rows, %.0fs"
          % (Kmin, nlo, nhi, len(rows), time.time() - t0), flush=True)

    op = [r for r in rows if r["op"]]
    print("operative C_FULL_TREE_POLYNOMIAL_ODE residue: %d rows" % len(op))

    def hist(rs, key):
        h = {}
        for r in rs:
            h[key(r)] = h.get(key(r), 0) + 1
        return dict(sorted(h.items()))

    for lab, rs in (("census", rows), ("operative", op)):
        print("\n== %s ==" % lab)
        print("  by s'      :", hist(rs, lambda r: r["sp"]))
        print("  by sign(u'):", hist(rs, lambda r: ("u'<0" if r["up"] < 0 else
                                                    "u'=0" if r["up"] == 0 else "u'>0")))
        print("  u'<0 by s' :", hist([r for r in rs if r["up"] < 0], lambda r: r["sp"]))
        print("  u'=0 by s' :", hist([r for r in rs if r["up"] == 0], lambda r: r["sp"]))
        print("  u_s hist   :", hist(rs, lambda r: r["u_s"]))
        print("  non-integral M' :", sum(1 for r in rs if not r["exact"]))

    def ser(r):
        return dict(n=r["n"], m=r["m"], Ms=list(r["Ms"]), V={str(k): v for k, v in r["V"].items()},
                    s=r["s"], sp=r["sp"], d_s=r["d_s"], u_s=r["u_s"], v_s=r["v_s"], ell=r["ell"],
                    n1=r["n1"], m1=r["m1"], Mp=[str(x) for x in r["Mp"]], Vp=list(r["Vp"]),
                    d2=r["d2"], d2p=r["d2p"], V2p=r["V2p"], up=r["up"], op=r["op"], exact=r["exact"])

    out = dict(nlo=nlo, nhi=nhi, Kmin=Kmin, census=len(rows), operative=len(op),
               unegative_census=[ser(r) for r in rows if r["up"] < 0],
               uzero_census=[ser(r) for r in rows if r["up"] == 0],
               sp3plus_operative=[ser(r) for r in op if r["sp"] >= 3],
               operative_rows=[ser(r) for r in op])
    with open(os.path.join(HERE, "scope_enum.json"), "w") as fh:
        json.dump(out, fh, indent=1)
    print("\nU-NEGATIVE: census %d, operative %d"
          % (len(out["unegative_census"]), sum(1 for r in rows if r["up"] < 0 and r["op"])))
    print("u'=0      : census %d, operative %d"
          % (len(out["uzero_census"]), sum(1 for r in rows if r["up"] == 0 and r["op"])))
    print("wrote scope_enum.json  (%.0fs)" % (time.time() - t0))


if __name__ == "__main__":
    a = sys.argv[1:]
    main(int(a[0]) if a else 16, int(a[1]) if len(a) > 1 else 200,
         int(a[2]) if len(a) > 2 else 2)
