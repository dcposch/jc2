#!/usr/bin/env python3
"""TIME-FUNCTION ENDGAME -- part B: LOCAL-KELLER order by order at the bottom disc.

sigma_1(pi) = w(t) + pi t^{delta_1};  F = f(sigma_1) = t^{lam_f} Phi,  G = t^{lam_g} Gamma.
d(x,y)/d(t,pi) = -t^{delta-2}, so  F_t G_pi - F_pi G_t = -c t^{delta-2}, i.e.

  (lam_f Phi + t Phi_t) Gamma_pi - (lam_g Gamma + t Gamma_t) Phi_pi = -c.   (LOCAL-KELLER)

Expand Phi = sum Phi_k t^{eps_k}, Gamma = sum Gamma_k t^{eps_k} (eps_0 = 0):
  order 0 :  lam_f Phi_0 Gamma_0' - lam_g Gamma_0 Phi_0' = -c            (BOTTOM-ODE)
  order k :  L_{eps_k}(Phi_k, Gamma_k) = - sum_{i+j=k, i,j>=1} [ ... ]
with L_eps(Phi,Gamma) = (lam_f+eps) Phi Gamma_0' - lam_g Gamma_0 Phi'
                      + lam_f Phi_0 Gamma' - (lam_g+eps) Gamma Phi_0'.
"""
import sys
from fractions import Fraction as F
import sympy as sp

pi_ = sp.Symbol('pi')
eps = sp.Symbol('epsilon')

FAIL=[]; NCHK=[0]
def check(name, cond, detail=""):
    NCHK[0]+=1
    if not cond: FAIL.append((name,detail)); print("  FAIL  %-56s %s"%(name,detail))
    return cond

def Lop(Phi, Gam, Phi0, Gam0, lf, lg, e_):
    return sp.expand((lf+e_)*Phi*sp.diff(Gam0,pi_) - lg*Gam0*sp.diff(Phi,pi_)
                     + lf*Phi0*sp.diff(Gam,pi_) - (lg+e_)*Gam*sp.diff(Phi0,pi_))

def src2(Phi1, Gam1, lf, lg, e1):
    return sp.expand((lf+e1)*Phi1*sp.diff(Gam1,pi_) - (lg+e1)*Gam1*sp.diff(Phi1,pi_))

def poly_unknowns(prefix, deg):
    cs = sp.symbols('%s0:%d' % (prefix, deg+1))
    return sum(cs[i]*pi_**i for i in range(deg+1)), list(cs)

def linear_report(Phi0, Gam0, lf, lg, e_, degPhi, degGam, label, source=0):
    Phi, cs1 = poly_unknowns('u', degPhi)
    Gam, cs2 = poly_unknowns('v', degGam)
    unk = cs1 + cs2
    Lval = sp.expand(Lop(Phi, Gam, Phi0, Gam0, lf, lg, e_) + source)
    P = sp.Poly(Lval, pi_)
    rows = [sp.expand(P.nth(j)) for j in range(P.degree()+1)] if Lval != 0 else []
    # split into matrix M*unk = -rhs
    M = sp.zeros(len(rows), len(unk)); rhs = sp.zeros(len(rows), 1)
    for i, r in enumerate(rows):
        pr = sp.expand(r)
        for j, u in enumerate(unk):
            M[i, j] = sp.expand(sp.diff(pr, u))
        rhs[i, 0] = sp.expand(-(pr - sum(M[i,j]*unk[j] for j in range(len(unk)))))
    rk = M.rank()
    aug = M.row_join(rhs); rk_aug = aug.rank()
    ker = len(unk) - rk
    print("   %-34s unknowns %2d  conditions %2d  rank %2d  kernel %2d  coker %2d  %s"
          % (label, len(unk), M.rows, rk, ker, M.rows - rk,
             "CONSISTENT" if rk_aug == rk else "INCONSISTENT"))
    return M, rhs, unk, rk, ker, (rk_aug == rk)
