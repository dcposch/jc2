import sys
sys.path.insert(0,'/Users/dc/code/math/jc2/box/tfe-drivers-20260902')
from timefun import *
import sympy as sp

print("== CONTROL 3 (NEGATIVE): f = y, g = x^j + y^k.  J = -j x^{j-1}: Keller iff j = 1. ==")
print("   The time function on the fibre {g=c_2} is  H(x) = int c dx / g_y(tau_i)  and the")
print("   Lagrange interpolant is  L(y) = (H/T) y  with  T = (c_2 - x^j)^{1/k}.")
print("   Condition (i) (y-degree = m = 1 < n = k) holds for EVERY j.  Condition (ii)")
print("   (coefficients polynomial in x) holds iff H/T is a polynomial, iff there is a")
print("   polynomial p with  p'(c_2 - x^j) - (j/k) x^{j-1} p = 1.  Degree count:")
print("   deg LHS = deg p + j - 1, so a solution exists only if j = 1.")
print()
print("   %-8s %-14s %-9s %-46s %-12s" % ("(j,k)","J","Keller?","H/T  (leading behaviour in 1/x)","(ii) holds"))
kk = sp.Symbol('k', positive=True, integer=True)
for j in range(1,4):
    for k in range(2,6):
        f = y; g = sp.expand(x**j + y**k); J = jac(f,g)
        keller = (J.free_symbols == set())
        cconst = J if keller else sp.Symbol('c')     # pretend Keller off the Keller locus
        T = (c2 - x**j)**sp.Rational(1,k)
        # 1/g_y(tau_i) = zeta^i /(k (c2-x^j)^{(k-1)/k});  H = c/k int (c2-x^j)^{(1-k)/k} dx
        integrand = sp.Rational(1,k)*(c2 - x**j)**sp.Rational(1-k,k)
        H = sp.integrate(integrand, x)
        HT = sp.simplify(sp.cancel(sp.powsimp(H/T, force=True)))
        # decide (ii) by the polynomial criterion  p'(c2-x^j) - (j/k)x^{j-1}p = 1
        pcs = sp.symbols('a0:6'); D = 5
        pp = sum(pcs[i]*x**i for i in range(D+1))
        E = sp.expand(sp.diff(pp,x)*(c2-x**j) - sp.Rational(j,k)*x**(j-1)*pp - 1)
        solp = sp.solve(sp.Poly(E, x).all_coeffs(), pcs, dict=True)
        polyok = False
        for s0 in solp:
            cand = sp.expand(pp.subs(s0))
            if cand.free_symbols - {x, c2}: cand = cand.subs({t_:0 for t_ in cand.free_symbols-{x,c2}})
            if sp.expand(sp.diff(cand,x)*(c2-x**j) - sp.Rational(j,k)*x**(j-1)*cand - 1)==0:
                polyok = True; break
        check("(j,k)=(%d,%d): (ii) holds iff Keller"%(j,k), polyok == keller,
              "polyok=%s keller=%s"%(polyok,keller))
        print("   %-8s %-14s %-9s %-46s %-12s" % ("(%d,%d)"%(j,k), J, keller,
              str(sp.simplify(HT))[:46], "YES" if polyok else "NO -- FAILS"))
print("\n%d checks, %d failures" % (NCHK[0], len(FAIL)))
for nm,dt in FAIL: print("   FAILED:", nm, dt)
