"""D. Controls for the MASTER degree theorem  deg(g^2-f^3-lambda f) = K+k+2.

D1 composite arm (beta in k): J = 0, and deg(E - lambda f) = 0  -> the hypothesis c != 0 is load-bearing.
D2 y-degree ledger: deg_y alpha = 2 deg_y beta - K, deg_y rho <= K-1, deg_y E = max(3 dyb, dyr+2K).
D3 FALLACY-v2 exclusion check: does a proved bound EXCLUDE all admissible beta?
"""
import sympy as sp
from sympy import Rational as Q
import random
from math import ceil
x, y = sp.symbols('x y')
R2 = lambda e: sp.Poly(e, x, y, domain='QQ')
def dxp(p): return p.diff(x)
def dyp(p): return p.diff(y)
def Jp(u,v): return dxp(u)*dyp(v) - dyp(u)*dxp(v)
def td(p): return -1 if p.is_zero else p.total_degree()
def yd(p): return -1 if p.is_zero else max(j for (i,j) in p.monoms())
def ydivmod(num, den):
    n = sp.Poly(num.as_expr(), y); d = sp.Poly(den.as_expr(), y)
    q, r = sp.div(n, d); return R2(sp.expand(q.as_expr())), R2(sp.expand(r.as_expr()))
def inst(K, b, seed):
    rnd = random.Random(seed); h = y**(K-1)*(y-x)
    for j in range(K):
        for i in range(K-j): h += rnd.randint(-3,3)*x**i*y**j
    beta = 0
    for j in range(min(K-1,b)+1):
        for i in range(b-j+1): beta += rnd.randint(-3,3)*x**i*y**j
    beta += x**(b-min(K-1,b))*y**min(K-1,b)
    return R2(h), R2(beta)

print("=== D1. composite arm (beta in k): J = 0 and E collapses  ->  c != 0 is load-bearing ===")
for K in (4,7,9):
    h,_ = inst(K, 1, 11)
    beta = R2(sp.Integer(3))
    alpha, rho = ydivmod(beta*beta, h)
    f = h*h + 2*beta; g = h**3 + 3*beta*h + Q(3,2)*alpha
    Jfg = Jp(f,g); E = g*g - f**3
    lam = Q(-27)   # E + 3 beta^2 f = -2 beta^3
    print("  K=%d: alpha=%s  J(f,g)=%s  deg E=%d (=2K=%d)  deg(E-lam f)=%d  [K+6=%d]"
          % (K, "0" if alpha.is_zero else "nonzero", "0" if Jfg.is_zero else "nonzero",
             td(E), 2*K, td(E - R2(lam)*f), K+6))
print("  MARK_D1  composite: J=0, so the band lemma hypothesis (c != 0) fails and deg(E-lam f)=0 != K+6 -- consistent, NOT a counterexample")

print()
print("=== D2. y-degree ledger ===")
for (K,b,seed) in [(7,6,5),(7,9,6),(9,7,7),(9,13,8)]:
    h, beta = inst(K,b,seed)
    alpha, rho = ydivmod(beta*beta, h)
    E = (h**3+3*beta*h+Q(3,2)*alpha)**2 - (h*h+2*beta)**3
    dyb, dya, dyr = yd(beta), yd(alpha), yd(rho)
    pred = max(3*dyb, dyr+2*K)
    print("  K=%d b=%d : deg_y beta=%d  deg_y alpha=%d (pred 2dyb-K=%d)  deg_y rho=%d (<=K-1=%d)  deg_y E=%d (pred max(3dyb,dyr+2K)=%d)  %s"
          % (K,b,dyb,dya,2*dyb-K,dyr,K-1,yd(E),pred, "OK" if yd(E)==pred and dya==2*dyb-K else "MISMATCH"))

print()
print("=== D3. FALLACY-v2: a degree bound kills a row only if it EXCLUDES every admissible beta ===")
print("  admissible band for deg(beta):  max(ceil((2K+1)/3), ceil(2(K-1)/3)+1)  <=  b  <=  2K-1")
for K in (7,8,9,10,12,20,50):
    lo = max(ceil((2*K+1)/3), ceil(2*(K-1)/3)+1); hi = 2*K-1
    print("   K=%2d : b in [%2d, %2d]   width = %2d   (width/K = %.3f -> 4/3)" % (K, lo, hi, hi-lo+1, (hi-lo+1)/K))
print("  => the level-4 bound is NON-EMPTY for every K: it is a necessary condition, not a kill.")
