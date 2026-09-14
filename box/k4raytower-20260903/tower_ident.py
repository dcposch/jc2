"""Level-3 reconstruction + level-4 derivation, exact over Q (sympy).

Objects (ray R_4 tower, k=4):
  H = y^(K-1)(y-x)       leading form of h, degree K
  h  monic in y, deg_y h = K, lf(h) = H
  beta: deg_y beta <= K-1, deg beta = b
  alpha = quo_y(beta^2, h), rho = rem_y(beta^2, h)
  f = h^2 + 2 beta,  g = h^3 + 3 beta h + (3/2) alpha
  J = f_x g_y - f_y g_x  ;  E = g^2 - f^3
"""
import sympy as sp
from sympy import Rational as Q
import random, sys

x, y = sp.symbols('x y')

def J(u, v):
    return sp.expand(sp.diff(u, x)*sp.diff(v, y) - sp.diff(u, y)*sp.diff(v, x))

def ydiv(num, den, K):
    """quo/rem of num by den (monic in y of y-degree K)."""
    n = sp.Poly(num, y); d = sp.Poly(den, y)
    q, r = sp.div(n, d)
    return sp.expand(q.as_expr()), sp.expand(r.as_expr())

def band(expr, D):
    """total-degree-D homogeneous part"""
    p = sp.Poly(sp.expand(expr), x, y)
    out = 0
    for (i, j), c in p.terms():
        if i + j == D:
            out += c * x**i * y**j
    return sp.expand(out)

def tdeg(expr):
    e = sp.expand(expr)
    if e == 0: return -sp.oo
    return sp.Poly(e, x, y).total_degree()

def ydeg(expr):
    e = sp.expand(expr)
    if e == 0: return -sp.oo
    return sp.degree(e, y)

def instance(K, b, seed, xonly_beta=False):
    rnd = random.Random(seed)
    H = y**(K-1)*(y-x)
    # h monic in y, y-degree K, lf(h) = H  => h = H + (total degree <= K-1 stuff, deg_y <= K-1)
    h = H
    for j in range(0, K):
        for i in range(0, K-j):          # total degree i+j <= K-1
            h += rnd.randint(-3, 3)*x**i*y**j
    # beta: deg_y <= K-1, total degree exactly b (generic leading form)
    beta = 0
    for j in range(0, min(K-1, b)+1):
        for i in range(0, b-j+1):
            beta += rnd.randint(-3, 3)*x**i*y**j
    # force a nonzero degree-b part
    beta += x**(b-min(K-1,b))*y**min(K-1,b)
    return sp.expand(h), sp.expand(beta)

def build(h, beta, K):
    alpha, rho = ydiv(sp.expand(beta**2), h, K)
    f = sp.expand(h**2 + 2*beta)
    g = sp.expand(h**3 + 3*beta*h + Q(3,2)*alpha)
    return alpha, rho, f, g

def mark(name, ok, extra=""):
    print("MARK_%-22s %s  %s" % (name, "0" if ok else "FAIL", extra))
    if not ok: globals()['FAILED'] = True

FAILED = False

print("=== A. identity re-verification on this instrument ===")
for (K, b, seed) in [(4,3,1),(4,5,2),(5,4,3),(5,7,4),(7,6,5),(7,9,6),(9,7,7)]:
    h, beta = instance(K, b, seed)
    alpha, rho, f, g = build(h, beta, K)
    Jfg = J(f, g)
    E  = sp.expand(g**2 - f**3)
    ok_id6 = sp.expand(Jfg - 3*(J(beta,alpha) - J(h,rho))) == 0
    ok_E   = sp.expand(E - (beta**3 - 3*rho*h**2 - 9*beta*rho + Q(9,4)*alpha**2)) == 0
    ok_JfE = sp.expand(J(f,E) - 2*g*Jfg) == 0
    ok_ydeg= ydeg(E) <= 3*K-1
    tag = "K=%d b=%d" % (K,b)
    mark("ID6_"+tag, ok_id6)
    mark("ECUBIC_"+tag, ok_E, "deg E=%s deg_y E=%s (<=3K-1=%d)" % (tdeg(E), ydeg(E), 3*K-1))
    mark("JfE_"+tag, ok_JfE)
    mark("YDEGE_"+tag, ok_ydeg)
    # degrees actually attained (generic: deg rho = 2b, deg alpha = 2b-K)
    print("        generic degs: deg beta=%s deg alpha=%s deg rho=%s deg J=%s deg E=%s (2b+2K=%d)"
          % (tdeg(beta), tdeg(alpha), tdeg(rho), tdeg(Jfg), tdeg(E), 2*b+2*K))
print("FAILED" if FAILED else "ALL_A_OK")
