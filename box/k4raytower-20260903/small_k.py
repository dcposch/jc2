"""F. K = 4,5,6 controls: deg(g^2-f^3) = K+6 exactly, and the v_y(Theta) obstruction.
   Theta = y^K (y-x)^2 Theta_1 ;  v_y(Theta) = K  iff e_0 != 0 ;  v_(y-x)(Theta) = 2 iff sum e_i != 0."""
import sympy as sp
x, y = sp.symbols('x y')
def J(u,v): return sp.expand(sp.diff(u,x)*sp.diff(v,y)-sp.diff(u,y)*sp.diff(v,x))

print("=== F1. Theta for K = 4..14 : v_y(Theta), v_(y-x)(Theta), and v_y(H^2) = 2K-2 ===")
for K in range(4, 15):
    H = y**(K-1)*(y-x); D = K+6
    cs = sp.symbols('t0:%d' % (D+1))
    Th = sum(cs[i]*x**(D-i)*y**i for i in range(D+1))
    eqs = list(sp.Poly(sp.expand(J(H,Th) - x**4*H**2), x, y).as_dict().values())
    sol = sp.solve(eqs, list(cs), dict=True)
    if len(sol)!=1: print("K=%2d SOLVE_FAIL"%K); continue
    T = sp.expand(Th.subs(sol[0]))
    free = [c for c in cs if c not in sol[0]]
    vy   = min(j for (i,j),c in sp.Poly(T,x,y).terms() if c!=0)
    Tq = sp.Poly(sp.expand(T.subs(y, y+x)), x, y)
    vyx  = min(j for (i,j),c in Tq.terms() if c!=0)
    print("K=%2d  free=%d  v_y(Theta)=%2d  v_(y-x)(Theta)=%d   v_y(H^2)=%2d   H^2 | Theta ? %s"
          % (K, len(free), vy, vyx, 2*K-2, "YES" if vy>=2*K-2 and vyx>=2 else "NO"))

print()
print("=== F2. K = 4 : b <= 3 is dead (reproduces charged CAL_K4_B3) ===")
K = 4
print("  MASTER (K<=6, no D=2K escape):  deg(g^2-f^3) = K+6 = %d exactly" % (K+6))
print("  LEVEL 2 band 2b+2K > K+6  <=>  2b > 6-K = %d : holds for all b>=1" % (6-K))
print("     => H | beta_b^2 => 2b >= K+1 = %d => b >= %d" % (K+1, (K+2)//2))
for b in (3,):
    d_max = max(3*b-2*K, 6-K)
    print("  b=%d : deg rho <= max(3b-2K, 6-K) = %d ; 3b = %d < K+6 = %d," % (b, d_max, 3*b, K+6))
    print("        so [E]_{K+6} can only be -3 rho_{6-K} H^2  =>  H^2 | Theta ;")
    print("        but v_y(Theta) = K = %d  <  2K-2 = %d.  CONTRADICTION -> b=%d DEAD" % (K, 2*K-2, b))

print()
print("=== F3. K = 5 : b <= 3 dead by the same route; b = 4 NOT reached ===")
K=5
for b in (3,4):
    d_max = max(3*b-2*K, 6-K)
    top = max(3*b, d_max+2*K)
    print("  b=%d : deg rho <= %d ; 3b = %d ; K+6 = %d ; top candidate deg E = %d  -> %s"
          % (b, d_max, 3*b, K+6, top,
             "H^2 | Theta needed, v_y(Theta)=5 < 8  => DEAD"
             if 3*b < K+6 else "band 3b>K+6 gives only LEVEL 4 (H^2|P^3); NOT a kill"))
