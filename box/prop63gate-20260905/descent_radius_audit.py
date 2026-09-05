#!/usr/bin/env python3
"""Prop 6.3 radius-hypothesis audit.

For every (1)-(13)-admissible Moh skeleton in a degree range, emit the descent
datum and the Prop 6.4 flag:

    v_s = V_s ;  u_s = d_s - V_s ;  ell = v_s - u_s - 1
    (n',m') = ((n/d_s)*u_s, (m/d_s)*u_s)
    prop63_radius_hypothesis :  delta*_{s-1} >= v_s/u_s
    prop63_automatic         :  u_s == 1        (Moh Prop 6.4, p.198)

No new mathematics here: this is arithmetic on the frozen skeleton module.
"""
import sys
from fractions import Fraction as F
sys.path.insert(0, "/tmp/jc2-lane.I8LOUD/inputs")
from moh_skeleton_full import Skel, census

def descent(sk):
    ds, vs = sk.d[sk.s], sk.V[sk.s]
    us = ds - vs
    rec = dict(n=sk.n, m=sk.m, s=sk.s,
               M=tuple(sk.M[i] for i in range(1, sk.s+1)),
               d=tuple(sk.d[i] for i in range(1, sk.s+2)),
               V=tuple(sk.V[i] for i in range(2, sk.s+1)),
               d_s=ds, v_s=vs, u_s=us)
    if us <= 0:
        rec.update(valid=False); return rec
    rec.update(valid=True,
               ell=vs-us-1,
               radius_needed=F(vs, us),
               np=F(sk.n, ds)*us, mp=F(sk.m, ds)*us,
               prop63_automatic=(us == 1))
    return rec

def rows(n, m=None, Kmin=16, full=True):
    out = []
    for (mm, Ms, V) in census(n, Kmin=Kmin, full=full):
        if m is not None and mm != m: continue
        sk = Skel(n, mm, Ms, V)
        out.append((sk, descent(sk)))
    return out

def show(tag, items):
    print(f"\n=== {tag}  ({len(items)} admissible rows) ===")
    hdr = f"{'#':>2} {'M':<22} {'d':<20} {'V':<10} {'d_s':>4} {'v_s':>4} {'u_s':>4} " \
          f"{'v_s/u_s':>8} {'ell':>4} {'(n(,m()':>12} {'6.4 auto':>9}"
    print(hdr); print("-"*len(hdr))
    for i, (sk, r) in enumerate(items, 1):
        if not r["valid"]:
            print(f"{i:>2} {str(r['M']):<22} {str(r['d']):<20} {str(r['V']):<10} "
                  f"{r['d_s']:>4} {r['v_s']:>4} {r['u_s']:>4}   u_s<=0: no minor disc")
            continue
        np_, mp_ = r["np"], r["mp"]
        pair = f"({np_},{mp_})"
        print(f"{i:>2} {str(r['M']):<22} {str(r['d']):<20} {str(r['V']):<10} "
              f"{r['d_s']:>4} {r['v_s']:>4} {r['u_s']:>4} {str(r['radius_needed']):>8} "
              f"{r['ell']:>4} {pair:>12} {str(r['prop63_automatic']):>9}")

if __name__ == "__main__":
    show("(99,66)", rows(99, 66))
    show("(108,72)", rows(108, 72))

def sweep(nlo, nhi, Kmin=16):
    """all (1)-(13)-admissible rows in [nlo,nhi] with the Prop 6.4 flag."""
    out = []
    for n in range(nlo, nhi+1):
        for (mm, Ms, V) in census(n, Kmin=Kmin, full=True):
            sk = Skel(n, mm, Ms, V); r = descent(sk)
            out.append((sk, r))
    return out
