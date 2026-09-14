#!/usr/bin/env python3
"""Desk check (Fable, round 20260905T0200Z).
(1) Enumerate the operative-screen survivors at n<=100 (POLY_ODE = danger, ungated, ode, recenter:
    the 17(ll) operative screen C_FULL_TREE_POLYNOMIAL_ODE), subtract Moh's six printed rows,
    and descend each excess row by Moh Prop 6.3 (p.197, read from the page image):
        u_s = d_s - V_s, v_s = V_s, n' = n u_s/d_s, m' = m u_s/d_s (pi-degrees, Prop 6.3(2)),
        J_{gamma,pi} = -(u_s/b) gamma^{v_s-u_s-1}  (Prop 6.3(3)), so ell = v_s - u_s - 1,
        M_i' = M_i u_s/d_s (Cor 6.1(5) pattern), V_i' = V_i for i < s.
    NOTE: the descended Jacobian is a monomial in GAMMA (the y^{-1/u_s} variable), not in pi;
    a pi-degree comparison against ell is vacuous and is NOT used.
(2) Same listing at n = 108 (the packet's "D=108 CLOSED at skeleton level" headline).
Imports the frozen enumerator and Tree unmodified from box/centre-gate-20260903 (as screen_eight.py).
"""
from __future__ import annotations
import os, sys, json, time
from fractions import Fraction as F
HERE = os.path.dirname(os.path.abspath(__file__))
CENTRE = os.path.abspath(os.path.join(HERE, "..", "centre-gate-20260903"))
sys.path.insert(0, CENTRE)
import moh_skeleton_full_frozen as B  # noqa: E402
from opus5_probe import Tree  # noqa: E402

def surv(n, m, Ms, V, *, danger, gate, ode=False, passport=False, recenter=False):
    kw = dict(gate=gate, ode=ode, capacity=passport, passport=passport)
    T = Tree(n, m, Ms, **kw)
    if recenter:
        T.recenter = True
    T._memo = {}
    T.why = []
    if not (T.d[T.s] > V[T.s] > F(T.d[T.s], 2)):
        return False
    need = tuple(V[i] for i in range(T.s - 1, 1, -1))
    return T.ok(T.s - 1, (V[T.s],), danger, need) is not None

SCREENS = {
    "UNGATED_PASS": dict(danger=True, gate=False, ode=True, passport=True),
    "POLY": dict(danger=True, gate=False, recenter=True),
    "POLY_ODE": dict(danger=True, gate=False, ode=True, recenter=True),
}

def descend(n, m, Ms, V):
    sk = B.Skel(n, m, list(Ms), V)
    s = sk.s; ds = sk.d[s]; Vs = V[s]
    us = ds - Vs; vs = Vs
    npr = F(n * us, ds); mpr = F(m * us, ds)
    ell = vs - us - 1
    Mpr = [F(sk.M[i] * us, ds) for i in range(2, s)]
    Vpr = [V[i] for i in range(2, s)]
    return dict(s=s, d_s=ds, V_s=Vs, u_s=us, v_s=vs, n1=npr, m1=mpr, ell=ell, M1=Mpr, V1=Vpr)

def listing(title, keys):
    print(f"\n{title}")
    print("   n   m  M (M_2..M_s)          V (2..s)         s d_s V_s u_s v_s |  n'  m' ell | M'_2..M'_{s-1}      V'_2..V'_{s-1}")
    classes = {}
    for (n, m, Ms, Vt) in keys:
        V = dict(Vt); d = descend(n, m, Ms, V)
        cls = (int(d["n1"]), int(d["m1"]), d["ell"], tuple(d["V1"]))
        classes.setdefault(cls, []).append((n, m, Ms, Vt))
        print(f"{n:4d}{m:4d}  {str(Ms):22s}{str([V[i] for i in range(2, d['s']+1)]):17s}{d['s']:2d}{d['d_s']:4d}{d['V_s']:4d}{d['u_s']:4d}{d['v_s']:4d} |"
              f"{int(d['n1']):4d}{int(d['m1']):4d}{d['ell']:4d} | {str([str(x) for x in d['M1']]):20s}{str(d['V1'])}")
    print(f"distinct descended classes (n',m',ell,V'): {len(classes)}; distinct (n',m',ell): "
          f"{len({c[:3] for c in classes})}; u_s multiset: {sorted(descend(n,m,Ms,dict(Vt))['u_s'] for (n,m,Ms,Vt) in keys)}")
    for cls, mem in sorted(classes.items()):
        print(f"   {cls}: {len(mem)} rows")
    return classes

def main():
    t0 = time.time()
    rows = [(n, m, Ms, V) for n in range(4, 101) for m, Ms, V in B.census(n, Kmin=2, full=True)]
    printed = {(n, m, tuple(Ms), tuple(sorted(V.items()))) for n, m, Ms, V, *_ in B.MOH_TABLE}
    print("input rows n<=100:", len(rows), "printed:", len(printed), flush=True)
    out = {}
    for name, kw in SCREENS.items():
        S = [(n, m, Ms, V) for (n, m, Ms, V) in rows if surv(n, m, Ms, V, **kw)]
        keys = {(n, m, tuple(Ms), tuple(sorted(V.items()))) for n, m, Ms, V in S}
        excess = sorted(keys - printed)
        print(f"{name:14s} rows={len(keys):4d} classes={len({(k[0],k[1]) for k in keys}):3d} "
              f"printed={len(keys & printed)}/6 excess={len(excess)} ({time.time()-t0:.1f}s)", flush=True)
        out[name] = excess
    ex = out["POLY_ODE"]
    cl = listing("EXCESS rows under POLY_ODE (operative screen) at n<=100, with Prop 6.3 descent:", ex)
    # D = 108
    rows108 = [(108, m, Ms, V) for m, Ms, V in B.census(108, Kmin=2, full=True)]
    S108 = [(n, m, Ms, V) for (n, m, Ms, V) in rows108 if surv(n, m, Ms, V, **SCREENS["POLY_ODE"])]
    k108 = sorted({(n, m, tuple(Ms), tuple(sorted(V.items()))) for n, m, Ms, V in S108})
    print(f"\nn=108: admissible rows={len(rows108)}, POLY_ODE survivors={len(k108)}")
    cl108 = listing("POLY_ODE survivors at n = 108, with Prop 6.3 descent:", k108)
    json.dump({"excess_POLY_ODE_n_le_100": [[n, m, list(Ms), list(Vt)] for (n, m, Ms, Vt) in ex],
               "classes_n_le_100": [[list(map(str, c)), len(mem)] for c, mem in sorted(cl.items())],
               "survivors_108": [[n, m, list(Ms), list(Vt)] for (n, m, Ms, Vt) in k108],
               "classes_108": [[list(map(str, c)), len(mem)] for c, mem in sorted(cl108.items())],
               "excess_UNGATED_PASS": len(out["UNGATED_PASS"]), "excess_POLY": len(out["POLY"])},
              open(os.path.join(HERE, "excess14_descent.json"), "w"), indent=1)
    print(f"\ntotal {time.time()-t0:.1f}s")

if __name__ == "__main__":
    main()
