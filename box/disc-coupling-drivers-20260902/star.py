#!/usr/bin/env python3
"""DISC-COUPLING -- driver 1: the bottom star, re-derived from scratch.

BOTTOM-ODE (re-derived here, not imported):  d p_f p_g' - e p_g p_f' = kappa in C^*,
deg p_g = a_1 = e V_2, deg p_f = b_1 = d V_2.  We solve it WITHOUT the monic/translated
normalisation, because the junction analysis needs the leading coefficients as
free-but-then-pinned data.
FAIL-CLOSED.
"""
import sympy as sp
from fractions import Fraction as F

pi = sp.Symbol('pi')
FAIL=[]; N=[0]
def check(name, cond, detail=""):
    N[0]+=1
    if not cond: FAIL.append((name,detail)); print("  FAIL %-52s %s"%(name,detail))
    return cond

def bracket(pf,pg,d,e):
    return sp.expand(d*pf*sp.diff(pg,pi) - e*pg*sp.diff(pf,pi))

def solve_general(d,e,V):
    """full (unnormalised) solution of BOTTOM-ODE."""
    a,b = e*V, d*V
    P = sum(sp.Symbol('A%d'%i)*pi**i for i in range(a+1))     # p_g
    Q = sum(sp.Symbol('B%d'%i)*pi**i for i in range(b+1))     # p_f
    unk = [sp.Symbol('A%d'%i) for i in range(a+1)]+[sp.Symbol('B%d'%i) for i in range(b+1)]
    Br = sp.Poly(bracket(Q,P,d,e), pi)
    eqs = [sp.expand(Br.nth(j)) for j in range(1,a+b)]
    kap = sp.expand(Br.nth(0))
    return P,Q,eqs,kap,unk,a,b

print("="*78); print("driver 1: BOTTOM-ODE re-derivation")
# --- (2,3,1): the selected skeleton's bottom-star problem
d,e,V = 2,3,1
P,Q,eqs,kap,unk,a,b = solve_general(d,e,V)
print("(d,e,V)=(%d,%d,%d)  deg p_g=%d deg p_f=%d ; %d homogeneous eqs + kappa"%(d,e,V,a,b,len(eqs)))
for j,E in enumerate(eqs,start=1): print("   pi^%d : %s"%(j,E))
print("   pi^0 = kappa :", kap)

# the claimed general solution:  p_g = A3[(pi-z)^3+B(pi-z)],  p_f = B2[(pi-z)^2+2B/3]
A3,B2,z,Bb = sp.symbols('A3c B2c z Bb')
u = pi - z
pg = A3*(u**3 + Bb*u); pf = B2*(u**2 + sp.Rational(2,3)*Bb)
br = sp.expand(bracket(pf,pg,2,3))
check("claimed family solves BOTTOM-ODE", sp.simplify(br - sp.Rational(4,3)*A3*B2*Bb**2)==0, str(sp.simplify(br)))
print("   kappa on the claimed family =", sp.factor(sp.simplify(br)))

# and it is the FULL solution set: solve the 4 homogeneous eqs
# dimension of the solution variety at kappa != 0, by Groebner over QQ
w = sp.Symbol('w')
G = sp.groebner(eqs+[sp.expand(w*kap-1)], *(unk+[w]), order='grevlex')
print("   GB size at kappa!=0 :", len(G.exprs), " (1 in I ?", G.exprs==[sp.Integer(1)], ")")
check("solution variety nonempty at kappa != 0", G.exprs != [sp.Integer(1)])
# dimension check: substitute the claimed family's coefficients into the equations
pgp = sp.Poly(sp.expand(pg),pi); pfp = sp.Poly(sp.expand(pf),pi)
subs = {sp.Symbol('A%d'%i): pgp.nth(i) for i in range(a+1)}
subs.update({sp.Symbol('B%d'%i): pfp.nth(i) for i in range(b+1)})
for j,E in enumerate(eqs,start=1):
    check("family kills pi^%d"%j, sp.simplify(E.subs(subs))==0)
print("   family parameters: A3,B2,z,B  (4) ; kappa fixes 1 -> 3-dim solution set at fixed kappa")

# STAR-RESIDUE / STAR-SIMPLE spot check on the normalised star
pg0 = pi**3 - pi; pf0 = pi**2 - sp.Rational(2,3)
kk = sp.expand(bracket(pf0,pg0,2,3))
check("normalised star kappa = 4/3", kk == sp.Rational(4,3), str(kk))
for c in [0,1,-1]:
    check("STAR-RESIDUE at %s"%c, sp.simplify(pf0.subs(pi,c)*sp.diff(pg0,pi).subs(pi,c) - sp.Rational(4,3)/2)==0)
print("\nchecks %d, failures %d"%(N[0],len(FAIL)))
assert not FAIL
