#!/usr/bin/env python3
"""TIME-FUNCTION ENDGAME -- part B': ORDER TWO at the selected D=105 bottom disc.

Order 1:  L_{eps_1}(Phi_1, Gamma_1) = 0            (homogeneous)
Order 2:  L_{eps_2}(Phi_2, Gamma_2) = -[(lam_f+eps_1) Phi_1 Gamma_1' - (lam_g+eps_1) Gamma_1 Phi_1']
Take a GENERIC element of the order-1 kernel, build the order-2 source, and decide.
"""
import sys, itertools
sys.path.insert(0,'/Users/dc/code/math/jc2/box/tfe-drivers-20260902')
from localkeller import *
import sympy as sp

n,m,d,e,V = 105,70,2,3,1
delta1 = sp.Rational(3,4)
lg = -sp.Rational(n,1)*(1-delta1)/(n+m); lf = sp.Rational(m,n)*lg
a1,b1 = e*V, d*V; mu = -lg/a1
Gam0 = pi_**3 - pi_; Phi0 = pi_**2 - sp.Rational(2,3)
print("selected skeleton: lam_g=%s lam_f=%s mu=%s  p_g=%s  p_f=%s" % (lg,lf,mu,Gam0,Phi0))

def kernel_basis(E, dP, dG):
    Phi,c1 = poly_unknowns('u', dP); Gam,c2 = poly_unknowns('v', dG); unk=c1+c2
    Lv = sp.expand(Lop(Phi,Gam,Phi0,Gam0,lf,lg,E)); P=sp.Poly(Lv,pi_)
    rows=[sp.expand(P.nth(j)) for j in range(P.degree()+1)]
    M = sp.Matrix([[sp.diff(r,u) for u in unk] for r in rows])
    ns = M.nullspace()
    return Phi, Gam, unk, ns, M

for lab, E1 in [("generic eps_1 = 1/7", sp.Rational(1,7)),
                ("resonant eps_1 = mu = 1/20", mu),
                ("actual first step eps_1 = delta_1 - delta_2 = 1/380", sp.Rational(1,380))]:
    Phi,Gam,unk,ns,M = kernel_basis(E1, b1, a1)
    print("\n-- ORDER 1 at %s :  kernel dim %d (unknowns %d, conditions %d, rank %d)"
          % (lab, len(ns), len(unk), M.rows, M.rank()))
    # a generic kernel element
    ts = sp.symbols('s0:%d' % len(ns))
    vec = sum((ts[i]*ns[i] for i in range(len(ns))), sp.zeros(len(unk),1))
    sub = {unk[i]: vec[i] for i in range(len(unk))}
    Phi1 = sp.expand(Phi.subs(sub)); Gam1 = sp.expand(Gam.subs(sub))
    print("   Phi_1 =", sp.collect(Phi1, pi_)); print("   Gamma_1 =", sp.collect(Gam1, pi_))
    for lab2, E2 in [("generic eps_2 = 2/7", sp.Rational(2,7)),
                     ("resonant eps_2 = mu", mu), ("resonant eps_2 = 2mu", 2*mu),
                     ("resonant eps_2 = 3mu", 3*mu)]:
        S = src2(Phi1, Gam1, lf, lg, E1)
        # order-2 unknowns: same degree bounds
        M2,rhs,unk2,rk,ker,ok = linear_report(Phi0,Gam0,lf,lg,E2,b1,a1,
                                              "  order 2, %s"%lab2, source=S)
        if not ok:
            aug = M2.row_join(rhs)
            cond = sp.simplify(sp.factor(sp.expand((aug.rank()-M2.rank()))))
            print("      -> obstruction present; the single condition on (s_i) is:")
            # solve for when it becomes consistent
            sol = sp.solve([sp.expand(x_) for x_ in (M2.T.nullspace()[0].T*rhs)], list(ts), dict=True) \
                  if M2.T.nullspace() else []
            print("         cokernel functional vanishes iff", sol)
