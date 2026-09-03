#!/usr/bin/env python3
"""Control on the SECOND proof of PS-1 (report sec.2.4): the two generating functions

   (GF-P)  sum_{k>=0} P_k T^{-k-1} =  d/dT log chi
   (GF-R)  sum_{k>=0} R_k T^{-k-1} = -(1/J) d/dx log chi      [Keller]

so that PS-1 is the equality of the mixed partials of log chi.  Verified by
expanding both sides in T^{-1} to order KMAX and matching coefficients exactly.
"""
import sys
import sympy as sp
sys.path.insert(0, '/home/ubuntu/jc2/box/nextcoeff-drivers-20260903')
from psgrowth import (x, y, c, T, Pair, controls, chi_poly, power_sums_from_chi,
                      residues, check, FAIL, NCHK)

KMAX = 8
def expand_in_Tinv(expr, n, K):
    """Laurent expansion of a rational function of T in powers of T^{-1}, to T^{-K-1}."""
    u = sp.Symbol('u')                      # u = 1/T
    e = sp.together(expr.subs(T, 1/u))
    ser = sp.series(e, u, 0, K + 2).removeO()
    return sp.Poly(sp.expand(ser), u)

if __name__ == "__main__":
    print("genfun.py -- (GF-P) and (GF-R), the generating-function proof of PS-1")
    print("=" * 78)
    for P in controls()[:6]:
        n, J = P.n, P.J
        ch = chi_poly(P.f, P.g, n).as_expr()
        Ps = power_sums_from_chi(sp.Poly(ch, T), KMAX + 1)
        Rs = residues(P.f, P.g, n, KMAX)
        A = expand_in_Tinv(sp.diff(ch, T)/ch, n, KMAX)          # d/dT log chi
        B = expand_in_Tinv(-sp.diff(ch, x)/(J*ch), n, KMAX)     # -(1/J) d/dx log chi
        print("\n== %s ==" % P.label)
        for k in range(0, KMAX + 1):
            check("%s (GF-P) coeff of T^{-%d}" % (P.label[:3], k+1),
                  sp.expand(A.nth(k+1) - Ps[k]) == 0, "%s vs %s" % (A.nth(k+1), Ps[k]))
            check("%s (GF-R) coeff of T^{-%d}" % (P.label[:3], k+1),
                  sp.expand(B.nth(k+1) - Rs[k]) == 0, "%s vs %s" % (B.nth(k+1), Rs[k]))
        print("   (GF-P) and (GF-R) verified to order T^{-%d}" % (KMAX+1))
    print("\n%d checks, %d failures" % (NCHK[0], len(FAIL)))
    for nm, dt in FAIL: print("   FAILED:", nm, dt)
