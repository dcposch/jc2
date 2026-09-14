#!/usr/bin/env python3
"""Independent re-derivation of the own-data first-support arithmetic.

Everything here is written from the printed formulas, not from
box/lib/descend_own.py:
  Def 5.1(1) p.179  : #roots of g in D_i = (n/d_{i+1}) V_{i+1}
  Def 5.1(2) p.179  : V_{i+1} d_i/d_{i+1} >= V_i > d_i/(n-M_i), V_{s+1}=d_{s+1}
  Def 5.1(3) p.179  : delta_i formula
  Def 5.1(4)+4.6 p.170 : p(pi) has degree v = V_{i+1} (d_i/d_{i+1})
Galois structure of p at a zero-centred (hence Galois-stable) disc:
  p(xi) = xi^z prod_nu (xi^{b_i} - c_nu)^{r_nu},  b_i = den(delta_i).
"""
from fractions import Fraction as Q
from math import gcd
import json, sys

def gcds(n, M):
    d = {1: n}
    for i in range(1, len(M)+1):
        d[i+1] = gcd(d[i], M[i])
    return d

def radii(n, M, d, V):
    s = len(M)
    out = {}
    for i in range(1, s+1):
        r = Q(n - M[i], n - M[s] - 1)
        for j in range(i+1, s+1):
            r *= Q(V[j]*(n-M[j]) - d[j], V[j]*(n-M[j-1]) - d[j])
        out[i] = 1 - r
    return out

def firstsupport(n, m, Ms, Vd, allow_nonpositive=False, allow_zero_route=False):
    """Return the set of admissible first-nonzero indices j, and the trace."""
    s = len(Ms)
    M = {i+1: Ms[i] for i in range(s)}
    d = gcds(n, M)
    V = {int(k): v for k, v in Vd.items()}
    V[s+1] = d[s+1]
    dl = radii(n, M, d, V)
    us, vs, ds = d[s]-V[s], V[s], d[s]
    trace, ok_j, blocked_at = [], [], None
    Wzero = {s: Q(us)}
    for i in range(s-1, 1, -1):
        di = dl[i]
        P = Q(V[i+1]*d[i], d[i+1]); assert P.denominator == 1; P = P.numerator
        b = di.denominator
        zero_ok = (P - V[i]) % b == 0
        mass_ok = b*V[i] <= P                     # printed multiplicity budget
        pos = di > 0
        nz_ok = mass_ok and (pos or allow_nonpositive)
        trace.append(dict(i=i, delta=str(di), b=b, P=P, Vi=V[i],
                          zero_ok=zero_ok, mass_ok=mass_ok, positive=pos,
                          nonzero_ok=nz_ok))
        if nz_ok:
            ok_j.append(i)
        if zero_ok:
            Wzero[i] = Q(d[i], d[i+1])*Wzero[i+1] - di*(P - V[i])
        else:
            blocked_at = i
            break
    else:
        if allow_zero_route:
            ok_j.append(0)   # all-zero route down to level 2
    return dict(n=n, m=m, M=Ms, V={k: V[k] for k in sorted(V)}, d=d,
                delta={i: str(dl[i]) for i in dl}, us=us, vs=vs, ds=ds, s=s,
                first_nonzero=ok_j, blocked_at=blocked_at, trace=trace,
                Wzero={i: str(Wzero[i]) for i in Wzero})
