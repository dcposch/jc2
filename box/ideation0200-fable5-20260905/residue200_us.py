#!/usr/bin/env python3
"""Desk count (Fable): operative-screen (POLY_ODE) residue for 48 <= n <= 200, Kmin=16 (17(ll) convention),
split by u_s, with Prop 6.3 descended-class compression for the u_s = 1 population."""
from __future__ import annotations
import os, sys, json, time
from fractions import Fraction as F
HERE = os.path.dirname(os.path.abspath(__file__))
CENTRE = os.path.abspath(os.path.join(HERE, "..", "centre-gate-20260903"))
sys.path.insert(0, CENTRE)
import moh_skeleton_full_frozen as B  # noqa: E402
from opus5_probe import Tree  # noqa: E402

def surv(n, m, Ms, V):
    T = Tree(n, m, Ms, gate=False, ode=True, capacity=False, passport=False)
    T.recenter = True; T._memo = {}; T.why = []
    if not (T.d[T.s] > V[T.s] > F(T.d[T.s], 2)):
        return False
    need = tuple(V[i] for i in range(T.s - 1, 1, -1))
    return T.ok(T.s - 1, (V[T.s],), True, need) is not None

def descend(n, m, Ms, V):
    sk = B.Skel(n, m, list(Ms), V); s = sk.s; ds = sk.d[s]; Vs = V[s]
    us = ds - Vs; vs = Vs
    return dict(s=s, d_s=ds, u_s=us, v_s=vs, n1=n*us//ds, m1=m*us//ds, ell=vs-us-1,
                M1=tuple(F(sk.M[i]*us, ds) for i in range(2, s)), V1=tuple(V[i] for i in range(2, s)))

def main():
    t0 = time.time(); tot = 0; res = []
    for n in range(48, 201):
        for m, Ms, V in B.census(n, Kmin=16, full=True):
            tot += 1
            if surv(n, m, Ms, V):
                res.append((n, m, tuple(Ms), dict(V)))
        if n % 25 == 0:
            print(f"  n={n}: admissible so far {tot}, residue {len(res)} ({time.time()-t0:.0f}s)", flush=True)
    print(f"48<=n<=200 Kmin=16: admissible {tot}; POLY_ODE residue {len(res)} rows, "
          f"{len({(r[0],r[1]) for r in res})} degree pairs")
    by_us = {}; cls1 = {}; cls1_full = {}; cls2 = {}; cls2_full = {}; s_hist = {}
    for (n, m, Ms, V) in res:
        d = descend(n, m, Ms, V); by_us[d["u_s"]] = by_us.get(d["u_s"], 0) + 1
        s_hist[(d["u_s"] == 1, d["s"])] = s_hist.get((d["u_s"] == 1, d["s"]), 0) + 1
        key3 = (d["n1"], d["m1"], d["ell"]); keyF = key3 + (d["M1"], d["V1"])
        if d["u_s"] == 1:
            cls1[key3] = cls1.get(key3, 0) + 1; cls1_full[keyF] = cls1_full.get(keyF, 0) + 1
        else:
            cls2[key3] = cls2.get(key3, 0) + 1; cls2_full[keyF] = cls2_full.get(keyF, 0) + 1
    print("rows by u_s:", dict(sorted(by_us.items())))
    print("rows by (u_s==1, s):", dict(sorted(s_hist.items())))
    n1 = by_us.get(1, 0); n2 = len(res) - n1
    print(f"u_s=1: {n1} rows -> {len(cls1)} distinct (n',m',ell) -> {len(cls1_full)} distinct (n',m',ell,M',V')")
    print(f"u_s>=2: {n2} rows -> {len(cls2)} distinct (n',m',ell) -> {len(cls2_full)} distinct (n',m',ell,M',V')")
    ell_hist = {}
    for k, c in cls1_full.items():
        ell_hist[k[2]] = ell_hist.get(k[2], 0) + c
    print("u_s=1 rows by ell = d_s-3:", dict(sorted(ell_hist.items())))
    small = sorted(cls1.items(), key=lambda kv: (kv[0][0], kv[0][1], kv[0][2]))[:25]
    print("smallest u_s=1 descended (n',m',ell) data with multiplicities:", small)
    json.dump({"residue_rows": len(res), "by_us": {str(k): v for k, v in by_us.items()},
               "us1_classes3": len(cls1), "us1_classesFull": len(cls1_full),
               "us2_classes3": len(cls2), "us2_classesFull": len(cls2_full),
               "ell_hist_us1": {str(k): v for k, v in ell_hist.items()}},
              open(os.path.join(HERE, "residue200_us.json"), "w"), indent=1)
    print(f"total {time.time()-t0:.0f}s")

if __name__ == "__main__":
    main()
