#!/usr/bin/env python3
"""S11: validity range of the two-variable sub-chart ansatz for R_r={q_(t-r,0),b3}.

Lists every t at which the ansatz of (5.1) fails, i.e. at which some eliminated
variable acquires a monomial it does not have identically in t, or the four
predicted survivors collide.  Weights: x = t-r, b3 = t+1.
"""
import sys

def mons(w, tv, rv):
    """monomials x^a b3^b of weight w at this t"""
    out = []
    wx, wb = tv-rv, tv+1
    if wx <= 0:
        return out
    a = 0
    while a*wx <= w:
        rem = w - a*wx
        if rem % wb == 0:
            out.append((a, rem//wb))
        a += 1
    return out

for rv in [int(a) for a in sys.argv[1:]]:
    bad = []
    for tv in range(rv+2, 60):
        why = []
        if mons(2*tv+1, tv, rv):
            why.append("b2")
        if mons(tv, tv, rv):
            why.append("T(0)")
        if len(mons(3*tv+1, tv, rv)) != (1 if rv == 1 else 0):
            why.append("b1")
        # C_j survivors in [1,t-1] and q survivors in [t,2t]
        C = [j for j in range(1, tv) if mons(j, tv, rv)]
        Q = [j for j in range(tv, 2*tv+1) if mons(j, tv, rv)]
        if C != [tv-rv]:
            why.append("C=%s" % C)
        if sorted(Q) != sorted({tv+1, 2*tv-2*rv, 2*tv-rv+1} & set(range(tv, 2*tv+1))):
            why.append("q=%s" % Q)
        if why:
            bad.append((tv, why))
    print("r=%d : ansatz (5.1) fails at t = %s"
          % (rv, [b[0] for b in bad]))
    for tv, why in bad:
        print("        t=%2d : %s" % (tv, ",".join(why)))
