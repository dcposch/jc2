#!/usr/bin/env python3
"""Derive the ladder law from the (x,y) picture, top forms only.

Dictionary (proved from the engine's own basis, band_engine.py:496 z_band_to_w
and :484 build_FG):
  B1c_{r,q}      = coefficient of x^{(K-1)-r-q} (y-x)^q in B1 (deg K-1)
  row (D,k)      = coefficient of x^{D-k} y^k in J = F_x G_y - F_y G_x
  h_top          = y^A (y-x)^B,  K=A+B,  F = h^e + ...,  G = h^f + B1*h^{f-1} + ...
Degree bookkeeping: F_top * (B1c_{r,q} term of B1*h^{f-1}) has degree
  e*K + (K-1-r) + (f-1)*K - 2 = n+m-2-(r+1),  so r = p-1 for the t^p band.
"""
import sympy as sp

x, y = sp.symbols("x y")

def ladder(A, B, e, f, p, ks):
    K = A + B
    n, m = e*K, f*K
    r = p - 1
    F = y**(e*A) * (y - x)**(e*B)                 # top form of F
    out = {}
    for Q in range(0, K):                          # B1 basis index
        expo = (K - 1) - r - Q
        if expo < 0: continue
        G = x**expo * (y - x)**Q * (y**A*(y-x)**B)**(f-1)
        J = sp.expand(sp.diff(F,x)*sp.diff(G,y) - sp.diff(F,y)*sp.diff(G,x))
        P = sp.Poly(J, x, y)
        D = n + m - 2 - p
        for k in ks:
            c = P.coeff_monomial(x**(D-k) * y**k) if D-k >= 0 else 0
            out.setdefault(Q, {})[k] = sp.Integer(c)
    return out, n, m, K

print("== (99,66): A=9 B=24 e=3 f=2 ==")
A,B,e,f = 9,24,3,2
K=A+B; n,m=e*K,f*K
k0 = (e+1)*A - 1
def law(p,k): return n*(A*(e+f)-1-k) - e*A*p
for p in (1,2,4,8):
    out,_,_,_ = ladder(A,B,e,f,p,list(range(k0,k0+4)))
    Qs = sorted(out)
    print(" p=%d  (t^%d band, total degree %d)" % (p,p,n+m-2-p))
    for Q in Qs[:3] + Qs[-2:]:
        vals = out[Q]
        pred = {k: law(p,k) for k in vals}
        sgn = "+" if vals[k0] == pred[k0] else "-"
        agree = all(abs(vals[k])==abs(pred[k]) for k in vals)
        print("   Q=%-3d k0-coef=%-8s law=%-8s all |k| agree: %s   sign (-1)^(Q-k0)=%+d" %
              (Q, vals[k0], pred[k0], agree, (-1)**(Q-k0)))
    # the decisive structural claim: at k=k0 every Q gives the SAME magnitude
    mags = {abs(out[Q][k0]) for Q in Qs}
    print("   |coef at k=k0| over all Q: %s   (law %d)  -> row is c*sum (-1)^Q B1c" %
          (mags, abs(law(p,k0))))
