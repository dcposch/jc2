"""A2. Top band of E = g^2-f^3 in E-CUBIC form:  [E]_{2b+2K} = -3 [rho]_{2b} H^2  (LEVEL 2 band)."""
import sympy as sp
from sympy import Rational as Q
import random
x, y = sp.symbols('x y')
R2 = lambda e: sp.Poly(e, x, y, domain='QQ')
def band(p, D):
    return R2(sum(c*x**i*y**j for (i,j),c in zip(p.monoms(), p.coeffs()) if i+j==D))
def ydivmod(num, den):
    n = sp.Poly(num.as_expr(), y); d = sp.Poly(den.as_expr(), y)
    q,r = sp.div(n,d); return R2(sp.expand(q.as_expr())), R2(sp.expand(r.as_expr()))
def inst(K,b,seed):
    rnd = random.Random(seed); h = y**(K-1)*(y-x)
    for j in range(K):
        for i in range(K-j): h += rnd.randint(-3,3)*x**i*y**j
    beta = 0
    for j in range(min(K-1,b)+1):
        for i in range(b-j+1): beta += rnd.randint(-3,3)*x**i*y**j
    beta += x**(b-min(K-1,b))*y**min(K-1,b)
    return R2(h), R2(beta)

ok = True
for (K,b,seed) in [(4,3,1),(5,4,3),(7,6,5),(9,7,7)]:
    h,beta = inst(K,b,seed)
    alpha,rho = ydivmod(beta*beta,h)
    E = (h**3+3*beta*h+Q(3,2)*alpha)**2 - (h*h+2*beta)**3
    H = R2(y**(K-1)*(y-x))
    lhs = band(E, 2*b+2*K); rhs = R2(-3)*band(rho,2*b)*H*H
    good = (lhs-rhs).is_zero and not lhs.is_zero
    ok &= good
    print("MARK_EBAND_TOP_K%d_b%d %s   [E]_{2b+2K} = -3 [rho]_{2b} H^2 (nonzero: %s)"
          % (K,b,"0" if good else "FAIL", not lhs.is_zero), flush=True)
    # sanity: the other three E-CUBIC terms cannot reach 2b+2K
    print("        deg beta^3 = %d, deg(beta rho) = %d, deg alpha^2 = %d   all < 2b+2K = %d"
          % (3*b, b+2*b, 4*b-2*K, 2*b+2*K), flush=True)
print("MARK_A2_ALL", "0" if ok else "FAIL")
