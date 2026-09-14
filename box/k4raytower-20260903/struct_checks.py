"""C. Structural checks for the degree-bound tower.

C1  LEMMA INJ  : J(H,R)=0, deg_y R <= K-1, deg R = e >= 1  ==>  R = 0.
C2  band-lemma arithmetic: which D with K|D, D>K+6, D<=3K-1 survive.
C3  mod-3 cube obstruction on  P^3 = 3 R H^2.
C4  residual stratum after  H^2 | P^3  (level-4 divisibility), K = 4..14.
C5  numerical shadow of the divisibility tower  H^(c-1) | P^c.
"""
import sympy as sp
from math import ceil, gcd
x, y = sp.symbols('x y')

def J(u, v):
    return sp.expand(sp.diff(u,x)*sp.diff(v,y) - sp.diff(u,y)*sp.diff(v,x))

print("=== C1. LEMMA INJ : only-trivial kernel of R |-> J(H,R) on deg_y R <= K-1 ===")
bad = 0; tot = 0
for K in range(4, 11):
    H = y**(K-1)*(y-x)
    for e in range(1, 4*K+1):
        # R homogeneous of degree e with deg_y R <= K-1  <=>  x^(e-K+1) | R
        jmax = min(e, K-1)
        cs = sp.symbols('r0:%d' % (jmax+1))
        R = sum(cs[j]*x**(e-j)*y**j for j in range(jmax+1))
        eqs = list(sp.Poly(sp.expand(J(H,R)), x, y).as_dict().values()) or [sp.Integer(0)]
        sol = sp.solve(eqs, list(cs), dict=True)
        triv = (len(sol) == 1 and all(sol[0].get(c, None) == 0 or c in sol[0] and sol[0][c]==0 for c in cs)
                and len([c for c in cs if c not in sol[0]]) == 0)
        tot += 1
        if not triv: bad += 1; print("   K=%d e=%d NONTRIVIAL" % (K, e))
print("MARK_C1_INJ only_trivial %d of %d  %s" % (tot-bad, tot, "0" if bad==0 else "FAIL"))
print("MARK_C1_SHARP J(H,1) =", J(y**6*(y-x), sp.Integer(1)), " (e=0 hypothesis cannot be dropped)")

print()
print("=== C2. band lemma: D with K|D, K+6 < D <= 3K-1  (the only escapes from D=K+6) ===")
print("  K :  escapes")
for K in range(4, 16):
    esc = [D for D in range(K+7, 3*K) if D % K == 0]
    print("  %2d :  %s" % (K, esc if esc else "none  ->  deg(g^2-f^3) = K+6 exactly"))

print()
print("=== C3. mod-3 cube obstruction:  P^3 = 3 R H^2  with  deg_y rho = 0  ===")
for K in (7, 8, 9, 12):
    H = y**(K-1)*(y-x)
    # R = c x^d0 forces P^3 = 3c x^d0 y^(2K-2) (y-x)^2 ; mult of (y-x) is 2, not 0 mod 3
    print("  K=%2d : v_(y-x)(3 R H^2) = 2  with  2 mod 3 = %d != 0  ->  P^3 not a cube  ->  deg_y rho >= 1"
          % (K, 2 % 3))

print()
print("=== C4. residual stratum after H^2 | P^3 (level 4), P = mu y^s (y-x)^t x^u Qt ===")
print("  K :  s_min=ceil(2(K-1)/3)  pi_min=s_min+1  pi_max=K-1  b_min  b_max=2K-1  #b   pinned b (pi=b, unique shape)")
for K in range(4, 15):
    smin = ceil(2*(K-1)/3); pimin = smin+1; pimax = K-1
    bmin = max(pimin, ceil((2*K+1)/3))
    bmax = 2*K-1
    pinned = [b for b in range(bmin, min(pimax, bmax)+1)
              if len([(s,t,q) for s in range(smin, b+1) for t in range(1, b+1)
                      for q in range(0, b+1) if s+t+q == b and 3*s >= 2*(K-1)]) == 1]
    print("  %2d :  %2d %2d %2d   %2d %2d  %2d   %s" %
          (K, smin, pimin, pimax, bmin, bmax, bmax-bmin+1, pinned))

print()
print("=== C5. numerical shadow of the divisibility tower  H^(c-1) | P^c ===")
print("   c :  s >= ceil((c-1)(K-1)/c)  =>  pi >= s+1  =>  c*deg(beta) >= (c-1)K + 1 ; kills when pi_min > K-1")
for K in (7, 8, 9, 12):
    row = []
    for c in range(2, K+2):
        smin = ceil((c-1)*(K-1)/c)
        pimin = smin + 1
        row.append((c, smin, pimin, "DEAD" if pimin > K-1 else "%d*b>=%d" % (c, (c-1)*K+1)))
    print("  K=%d" % K)
    for (c, s, p, v) in row:
        print("     c=%2d  s>=%2d  pi>=%2d  pi_max=%2d   %s" % (c, s, p, K-1, v))
