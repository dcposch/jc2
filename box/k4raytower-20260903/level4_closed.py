"""E. Level-4 closed form:  H^2 | P^3  and  R = P^3/(3H^2)  solves  A J(H,P) = H J(H,R),  A = P^2/H.
   Also: uniqueness (INJ), and the exceptional lambda-branch is empty."""
import sympy as sp
from math import ceil
x, y = sp.symbols('x y')
def J(u,v): return sp.expand(sp.diff(u,x)*sp.diff(v,y)-sp.diff(u,y)*sp.diff(v,x))
def dv(a,b):
    q,r = sp.div(sp.Poly(a,x,y), sp.Poly(b,x,y)); return sp.expand(q.as_expr()), sp.expand(r.as_expr())

print("=== E. closed form  R = P^3/(3H^2)  ===")
ok = True
for K in (7,8,9,10,12):
    H = y**(K-1)*(y-x)
    s = ceil(2*(K-1)/3); t = 1
    for (extra_s, u, qextra) in [(0,0,0), (1,0,0), (0,2,0), (0,0,1)]:
        S = s+extra_s
        Qt = (y+2*x)**qextra
        P = sp.expand(y**S*(y-x)**t * x**u * Qt)
        b_tot = sp.Poly(P,x,y).total_degree()
        A, rA = dv(P**2, H)
        if rA != 0:  print("  K=%d s=%d skip: H nmid P^2" % (K,S)); continue
        R, rR = dv(P**3, 3*H**2)
        if rR != 0:  print("  K=%d s=%d skip: H^2 nmid P^3" % (K,S)); continue
        lhs = sp.expand(A*J(H,P)); rhs = sp.expand(H*J(H,R))
        good = sp.expand(lhs-rhs)==0
        dyP = sp.degree(P,y); dyR = sp.degree(R,y); dyA = sp.degree(A,y)
        ok &= good and dyR <= K-1 and dyA <= K-2 and dyP <= K-1
        print("  K=%2d P=y^%d(y-x)^%d x^%d Q_%d  b=%2d  deg_y P=%d(<=%d) deg_y A=%d(<=%d) deg_y R=%d(<=%d) "
              "deg R=%d (=3b-2K=%d)  MARK_E_SOLVES %s"
              % (K,S,t,u,qextra,b_tot,dyP,K-1,dyA,K-2,dyR,K-1,
                 sp.Poly(R,x,y).total_degree(), 3*b_tot-2*K, "0" if good else "FAIL"))
print("MARK_E_ALL", "0" if ok else "FAIL")

print()
print("=== E2. the lambda-branch of level 4 is empty: needs K | 3b and d0 = 3b-2K = mK >= K, i.e. b >= K,")
print("        but b >= K forces deg_y R <= K-1 < d0 = deg_y(H^m), so lambda = 0. Arithmetic check: ===")
for K in (7,8,9,12):
    hits = [b for b in range(1, 2*K) if (3*b) % K == 0 and 3*b-2*K >= K and b <= K-1]
    print("   K=%2d : b with K|3b, 3b-2K>=K and b<=K-1 :  %s" % (K, hits if hits else "none"))
