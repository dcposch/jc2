"""Terminal band equation  J(H, Theta) = c x^k H^2  for a binary form Theta of degree K+k+2.

Derivation: J(f, E-lambda f) = 2 c x^k g, so lf: 2H J(H,Theta) = 2 c x^k H^3.
Solve the linear system exactly over Q with c = 1.
"""
import sympy as sp
from sympy import Rational as Q
x, y = sp.symbols('x y')

def J(u, v):
    return sp.expand(sp.diff(u,x)*sp.diff(v,y) - sp.diff(u,y)*sp.diff(v,x))

def solve_theta(K, k=4):
    H = y**(K-1)*(y-x)
    D = K + k + 2
    cs = sp.symbols('t0:%d' % (D+1))
    Theta = sum(cs[i]*x**(D-i)*y**i for i in range(D+1))
    eq = sp.expand(J(H, Theta) - x**k*H**2)
    P = sp.Poly(eq, x, y)
    eqs = [c for c in P.coeffs()] if P.total_degree() >= 0 else []
    eqs = list(sp.Poly(eq, x, y).as_dict().values())
    sol = sp.solve(eqs, list(cs), dict=True)
    return H, D, cs, Theta, sol

print("=== B. terminal band equation  J(H,Theta) = x^4 H^2,  deg Theta = K+6 ===")
for K in range(7, 15):
    H, D, cs, Theta, sol = solve_theta(K, 4)
    if len(sol) != 1:
        print("K=%2d  MARK_THETA_UNIQUE FAIL  nsol=%d" % (K, len(sol))); continue
    s = sol[0]
    Th = sp.expand(Theta.subs(s))
    free = [c for c in cs if c not in s]
    resid = sp.expand(J(H, Th) - x**4*H**2)
    # structure: y^K (y-x)^2 | Theta ?
    quo, rem = sp.div(sp.Poly(Th, y), sp.Poly(y**K*(y-x)**2, y))
    ok_div = sp.expand(rem.as_expr()) == 0
    Th1 = sp.expand(quo.as_expr())
    print("K=%2d  MARK_THETA_UNIQUE %s free=%d  MARK_THETA_RESID %s  MARK_THETA_DIV %s  deg Theta1=%s"
          % (K, "0" if len(free)==0 else "FAIL", len(free), "0" if resid==0 else "FAIL",
             "0" if ok_div else "FAIL", sp.Poly(Th1,x,y).total_degree() if Th1!=0 else None))
    if K in (7,8,9):
        print("      Theta_1 =", sp.factor(Th1))

print()
print("=== B2. positive control: K=1, target x^1 (PC_K1_B1_x1) ===")
K, k = 1, 1
H = y - x
mu = sp.symbols('mu')
h = y - x
beta = mu*x
alpha = 0
rho = sp.expand(beta**2)
f = sp.expand(h**2 + 2*beta); g = sp.expand(h**3 + 3*beta*h)
Jfg = sp.expand(sp.diff(f,x)*sp.diff(g,y) - sp.diff(f,y)*sp.diff(g,x))
E = sp.expand(g**2 - f**3)
print("  J(f,g) =", sp.factor(Jfg), "   (target c x^1, c=6 mu^2)")
print("  E = g^2-f^3 =", sp.factor(E), "  deg E =", sp.Poly(E,x,y).total_degree(), " K+k+2 =", K+k+2)
D = sp.Poly(E,x,y).total_degree()
Th = sum(c*x**i*y**j for (i,j),c in sp.Poly(E,x,y).terms() if i+j==D)
Th = sp.expand(Th)
print("  Theta = E_%d =" % D, sp.factor(Th))
print("  MARK_PC_TERMINAL", "0" if sp.expand(J(H,Th) - 6*mu**2*x**k*H**2)==0 else "FAIL")
print("  MARK_PC_YDEG_E", "0" if sp.degree(E,y) <= 3*K-1 else "FAIL", " deg_y E =", sp.degree(E,y), "<= 3K-1 =", 3*K-1)
