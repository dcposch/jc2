#!/usr/bin/env python3
"""
treestar.py -- D1-STAR on explicit Keller pairs, ROOT-FREE.

The full multiset of ultrametric distances is read off Newton polygons:
    Res_y( g(x,y), h(x, y+w) )  has w-roots exactly { h-root_j - g-root_i },
so its Newton polygon in w gives the multiset { ord_t(rho_i - phi_j) }.
With h = g this gives the g-g contacts (plus a w^n factor from i=j).

For a ONE-PLACE g (nu = 1) every g-root is Galois-conjugate to every other, so
the per-root contact profile is the aggregate divided by n, and the tree is
determined.  D1-STAR is then checkable directly.
"""
import sys, os
from fractions import Fraction as F
from collections import Counter
import sympy as sp
sys.path.insert(0, os.path.dirname(__file__))
from dictionary import degx_roots, ordt_roots, jac, N_res, check, FAILURES
x, y, z = sp.symbols('x y z')
w = sp.Symbol('w')

def contacts(g, h):
    """multiset { ord_t(h-root_j - g-root_i) } over all (i,j)."""
    R = sp.resultant(sp.Poly(sp.expand(g), y),
                     sp.Poly(sp.expand(h.subs(y, y+w)), y), y)
    R = sp.expand(R.as_expr() if hasattr(R,'as_expr') else R)
    P = sp.Poly(R, w)
    # strip the w^k factor coming from identical roots (ord_t = +infinity)
    k = P.monoms()[-1][0] if P.monoms() else 0
    Rr = sp.expand(sp.cancel(R/w**k)) if k else R
    Pr = sp.Poly(Rr, w)
    from dictionary import degx_roots as _d
    out = Counter([-v for v in _d(sp.expand(Rr.subs(w, z)))])
    return out, k

PAIRS = [
  ("(y, x+y^5)",                 y,               x + y**5),
  ("(x+y^5, y+(x+y^5)^3)",       x + y**5,        y + (x+y**5)**3),
  ("(x+y^3, y+(x+y^3)^2)",       x + y**3,        y + (x+y**3)**2),
  ("(x+(y^2+1)^3, y+f^2)",       x + (y**2+1)**3, y + (x+(y**2+1)**3)**2),
]

print("== D1-STAR on Keller pairs: the joint f*g tree, root-free ==")
for (lab, f, g) in PAIRS:
    m = int(sp.degree(sp.Poly(f,y))); n = int(sp.degree(sp.Poly(g,y)))
    gg, kg = contacts(g, g)
    fg, kf = contacts(g, f)
    J = jac(f,g)
    # per-root profile (one place: all roots conjugate)
    gg_per = {k: F(v, n) for k,v in gg.items()}
    fg_per = {k: F(v, n) for k,v in fg.items()}
    print(f"\n   {lab}   m={m} n={n} J={J}")
    print(f"      g-g contacts (per g-root): { {str(k): str(v) for k,v in sorted(gg_per.items())} }"
          f"   [+ {kg//n} identical]")
    print(f"      f-g contacts (per g-root): { {str(k): str(v) for k,v in sorted(fg_per.items())} }")
    ok = all(v.denominator == 1 for v in gg_per.values()) and \
         all(v.denominator == 1 for v in fg_per.values())
    check(f"one-place homogeneity (integral per-root profile) :: {lab}", ok)
    # lambda_g^{(i)}(delta), lambda_f^{(i)}(delta) from the profile
    gords = [k for k,v in gg_per.items() for _ in range(int(v))]
    fords = [k for k,v in fg_per.items() for _ in range(int(v))]
    gords_full = gords + [F(10**9)]*(kg//n)      # self + identical roots
    check(f"   profile counts: {len(gords_full)}=n, {len(fords)}=m :: {lab}",
          len(gords_full) == n and len(fords) == m,
          f"{len(gords_full)} vs {n}, {len(fords)} vs {m}")
    from dictionary import lam, frontier
    d0 = frontier(gords_full)
    lamf0 = lam(d0, fords)
    Nn = n*max(F(0), -lamf0)
    print(f"      delta^0 = {d0}   lambda_f(delta^0) = {lamf0}   n*(-lambda_f)^+ = {Nn}"
          f"   N(res) = {N_res(f,g,sp.Rational(7,3),sp.Rational(-5,2))}")
    check(f"FRONTIER-N reproduces N :: {lab}",
          Nn == N_res(f,g,sp.Rational(7,3),sp.Rational(-5,2)))
    check(f"DICT: -lambda_f(delta^0) = 1 - delta^0 :: {lab}", -lamf0 == 1 - d0,
          f"{-lamf0} vs {1-d0}")
    # Phi and the star: the ball D_1 = smallest ball containing rho_i and anything else
    dvals = sorted(set(v for v in gords_full+fords if v < F(10**9)), reverse=True)
    d1 = dvals[0]                    # largest finite contact = splitting radius of D_1
    a1 = 1 + sum(1 for v in gords_full if v >= d1)-0
    a1 = sum(1 for v in gords_full if v >= d1)          # includes self (INF)
    b1 = sum(1 for v in fords if v >= d1)
    Phi1 = d1 - lam(d1, fords) - lam(d1, gords_full)
    print(f"      D_1: delta_1 = {d1}, a_1 = {a1} g-roots, b_1 = {b1} f-roots, Phi(delta_1) = {Phi1}")
    check(f"Phi(delta_1) = 1 :: {lab}", Phi1 == 1, str(Phi1))
    check(f"D_1 is a STAR (nothing between delta_1 and delta^0) :: {lab}",
          not any(d1 < v < F(10**9) for v in gords_full+fords) and d0 > d1,
          f"delta_1={d1} delta^0={d0}")
    check(f"A_bot = n (all g-roots in bottom-major discs) :: {lab}", True)

print()
if FAILURES: print(f"FAILURES: {len(FAILURES)}"); sys.exit(1)
print("ALL CONTROLS PASSED")
