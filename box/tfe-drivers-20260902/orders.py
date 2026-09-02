import sys, itertools
sys.path.insert(0,'/Users/dc/code/math/jc2/box/tfe-drivers-20260902')
from localkeller import *
import sympy as sp

n,m,d,e,V = 105,70,2,3,1
delta1 = sp.Rational(3,4)
lg = -sp.Rational(n,1)*(1-delta1)/(n+m); lf = sp.Rational(m,n)*lg
a1, b1 = e*V, d*V
mu = -lg/a1
print("a_1=%d b_1=%d  lam_g=%s lam_f=%s  mu = -lam_g/a_1 = -lam_f/b_1 = %s" % (a1,b1,lg,lf,mu))
Gam0 = pi_**3 - pi_; Phi0 = pi_**2 - sp.Rational(2,3)

print("\n== grid of (deg Phi_k, deg Gamma_k) at GENERIC eps ==")
print("   %-6s %-6s %-9s %-10s %-6s %-6s %-6s" % ("degPhi","degGam","unknowns","conditions","rank","ker","coker"))
for beta in range(0, b1+3):
    for alpha in range(0, a1+3):
        Phi,c1 = poly_unknowns('u', beta); Gam,c2 = poly_unknowns('v', alpha)
        Lv = sp.expand(Lop(Phi,Gam,Phi0,Gam0,lf,lg,eps))
        P = sp.Poly(Lv, pi_); rows=[sp.expand(P.nth(j)) for j in range(P.degree()+1)]
        unk = c1+c2
        M = sp.Matrix([[sp.diff(r,u) for u in unk] for r in rows])
        # substitute a generic eps
        Mg = M.subs(eps, sp.Rational(1,7))
        rk = Mg.rank()
        print("   %-6d %-6d %-9d %-10d %-6d %-6d %-6d" % (beta,alpha,len(unk),M.rows,rk,len(unk)-rk,M.rows-rk))

print("\n== resonances: eps at which the rank of L_eps drops (degPhi=b_1, degGam=a_1) ==")
Phi,c1 = poly_unknowns('u', b1); Gam,c2 = poly_unknowns('v', a1); unk=c1+c2
Lv = sp.expand(Lop(Phi,Gam,Phi0,Gam0,lf,lg,eps)); P=sp.Poly(Lv,pi_)
rows=[sp.expand(P.nth(j)) for j in range(P.degree()+1)]
M = sp.Matrix([[sp.diff(r,u) for u in unk] for r in rows])
gg = 0
for cc in itertools.combinations(range(M.cols), M.rows):
    D = sp.expand(M[:, list(cc)].det())
    if D != 0: gg = sp.gcd(gg, sp.Poly(D, eps)) if gg != 0 else sp.Poly(D, eps)
print("   gcd of maximal minors =", sp.factor(gg.as_expr()))
print("   roots  =", sp.solve(gg.as_expr(), eps), "   mu*Z =", [k*mu for k in range(0,4)])

print("\n== rank/kernel/coker AT each resonance ==")
for E in [0, mu, 2*mu, 3*mu, 4*mu]:
    Me = M.subs(eps, E); rk = Me.rank()
    print("   eps = %-6s (= %s mu) unknowns %d conditions %d rank %d ker %d coker %d"
          % (E, sp.nsimplify(E/mu), len(unk), M.rows, rk, len(unk)-rk, M.rows-rk))
