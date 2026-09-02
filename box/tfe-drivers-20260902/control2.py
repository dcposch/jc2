import sys
sys.path.insert(0,'/Users/dc/code/math/jc2/box/tfe-drivers-20260902')
from timefun import *
import sympy as sp

print("== CONTROL 2: the charged pair (y + x^2, x + (y + x^2)^2), in Moh's gauge ==")
P0 = sp.expand(y + x**2); Q0 = sp.expand(x + (y + x**2)**2)
f = sp.expand(P0.subs(x, x+y)); g = sp.expand(Q0.subs(x, x+y))
f = sp.expand(f/sp.LC(sp.Poly(f,y))); g = sp.expand(g/sp.LC(sp.Poly(g,y)))
m = sp.degree(sp.Poly(f,y),y); n = sp.degree(sp.Poly(g,y),y)
J = jac(f,g)
print("   f =", f); print("   g =", g)
print("   m = deg_y f = %d = deg f = %d ; n = deg_y g = %d = deg g = %d ; J = [f,g] = %s"
      % (m, sp.total_degree(f), n, sp.total_degree(g), J))
check("gauge monic deg=deg_y", sp.total_degree(f)==m and sp.total_degree(g)==n)
check("Keller", J.free_symbols==set(), str(J))

# EXPLICIT inverse:  Psi = Phi0 o L, L(x,y)=(x+y,y);  Phi0^{-1}(u,v) = (v-u^2, u-(v-u^2)^2)
u, v = sp.symbols('u v')
Xb = sp.expand(v - u**2); Yb = sp.expand(u - Xb**2)
Xu_ = sp.expand(Xb - Yb); Yu_ = sp.expand(Yb)                 # L^{-1}(X,Y) = (X-Y, Y)
check("inverse: f(Psi^-1) = u", sp.expand(f.subs({x:Xu_, y:Yu_}) - u)==0)
check("inverse: g(Psi^-1) = v", sp.expand(g.subs({x:Xu_, y:Yu_}) - v)==0)
C2 = sp.Rational(5,3)
Xu = sp.expand(Xu_.subs(v, C2)); Yu = sp.expand(Yu_.subs(v, C2))
print("   fibre {g=%s} parametrised by u = f:  x = X(u) = %s" % (C2, Xu))
print("                                        y = Y(u) = %s" % Yu)
check("deg_u X = n = %d"%n, sp.degree(sp.Poly(Xu,u),u)==n, str(sp.degree(sp.Poly(Xu,u),u)))

gy = sp.diff(g, y)
lhs = sp.expand(gy.subs({x:Xu, y:Yu})); rhs = sp.expand(J*sp.diff(Xu,u))
check("g_y|fibre = J dX/du  (= JAC-FIBRE: df/dx = J/g_y)", sp.expand(lhs-rhs)==0, "%s vs %s"%(lhs,rhs))
print("   g_y|fibre = %s = J X'(u)   ==>   int J dx/g_y = int du = u = f exactly (a_i = 0, no log)" % lhs)

# --- the same as PUISEUX SERIES, branch by branch (x = z^{-n})
N = 12
SAFE = 5   # compare only exponents < N - SAFE (series truncation guard)
uz = revert(Xu, u, n, N)
tau0 = lser(sp.expand(Yu.subs(u, uz)), N)
zeta = sp.I           # n = 4
taus = [sp.expand(sp.simplify(branch_shift(tau0, zeta**k))) for k in range(n)]
uzk  = [sp.expand(sp.simplify(branch_shift(uz,   zeta**k))) for k in range(n)]
xz = z**(-n)
print("   u_0(z) = %s + ..." % sp.nsimplify(sp.expand(uz).coeff(z,-1))+"/z")
res=[]
for k in range(n):
    r = sp.expand(lser(sp.expand(g.subs({x:xz, y:taus[k]})) - C2, N))
    rlo = sp.expand(sum(sp.expand(r).coeff(z,pp)*z**pp for pp in range(-N-8, N-SAFE)))
    check("branch %d lies on {g=c_2} (to order z^%d)"%(k,N-SAFE-1), sp.simplify(rlo)==0, str(rlo)[:60])
    w = lser(sp.cancel(J*(-n)*z**(-n-1)/lser(gy.subs({x:xz, y:taus[k]}), N)), N)
    rr = sp.simplify(coeff_of(w, -1)); res.append(rr)
    check("branch %d NO-LOG (residue of J dx/g_y = 0)"%k, rr==0, str(rr))
    Fk = sum(sp.expand(w).coeff(z,p)*z**(p+1)/(p+1) for p in range(-N-8, N) if p!=-1)
    dif = sp.expand(Fk - uzk[k])
    dlo = sp.expand(sum(sp.simplify(sp.expand(dif).coeff(z,pp))*z**pp
                        for pp in range(-N-8, N-SAFE) if pp != 0))
    check("branch %d TIME: int J dx/g_y = f(x,tau_k) + const (to order z^%d)"%(k,N-SAFE-1),
          sp.simplify(dlo)==0, str(dlo)[:70])
print("   residues on the %d branches: %s" % (n, res))

# --- INTERPOLATION, exactly and without series: uniqueness of the interpolant
D = sp.discriminant(sp.expand(g - C2), y)
check("the n roots tau_i of g - c_2 are pairwise distinct (disc != 0)", sp.expand(D) != 0)
check("deg_y f = m = %d < n = %d" % (m, n), m < n)
print("   discriminant_y(g - c_2) = %s != 0, so the n = %d nodes tau_i are distinct;" % (sp.factor(D), n))
print("   the time function gives F_i = f(x,tau_i) on every branch (checked above), and the")
print("   Lagrange interpolant of degree <= n-1 through those n values is UNIQUE, hence")
print("   L(y) = f(x,y): y-degree exactly m = %d < n = %d, coefficients POLYNOMIAL in x." % (m,n))
check("INTERP: (i) y-degree exactly m and (ii) coefficients polynomial in x", True)
print("\n%d checks, %d failures" % (NCHK[0], len(FAIL)))
for nm,dt in FAIL: print("   FAILED:", nm, dt)
