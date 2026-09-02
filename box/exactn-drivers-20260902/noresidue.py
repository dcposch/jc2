#!/usr/bin/env python3
"""
noresidue.py -- the charge's question (a): "no log: the x^{-1} coefficient of
1/g_y(tau_i) must vanish -- is that automatic or a constraint?"

ANSWER.  Run the identity FORWARD, not backwards: f(x,tau_i(x)) IS a Puiseux
series (f a polynomial, tau_i a Puiseux series), and for h = sum c_a t^a,
      d/dx h = -t^2 dh/dt = -sum a c_a t^{a+1},
whose t^1 = x^{-1} coefficient is -0*c_0 = 0.  So the x^{-1} coefficient of
d/dx f(x,tau_i) vanishes IDENTICALLY, with no hypothesis.  Since the Keller
identity makes  d/dx f(x,tau_i) = J/g_y(x,tau_i)  with J in C^*, the vanishing
of the x^{-1} coefficient of 1/g_y(x,tau_i) is a CONSEQUENCE for a Keller pair
-- and therefore a NECESSARY CONDITION on g alone (COROLLARY NO-RESIDUE).  It
is NOT automatic for a general monic g: negative control below.
"""
import sys, os
import sympy as sp
sys.path.insert(0, os.path.dirname(__file__))
from dictionary import check, FAILURES
x, y = sp.symbols('x y'); u = sp.Symbol('u', positive=True)

def coeff_xinv(expr, terms=12):
    """coefficient of x^{-1} in the Puiseux expansion at x = oo."""
    e = expr.subs(x, 1/u)
    s = sp.series(sp.simplify(e), u, 0, terms).removeO()
    s = sp.expand(s)
    return sp.simplify(s.coeff(u, 1))

CASES = [
 # (label, g, list of branch roots tau(x) of g - c2, keller?)
 ("g = x + y^5   (coordinate; J=-1 with f=y)", x + y**5,
  [sp.exp(2*sp.pi*sp.I*sp.Rational(k,5))*(sp.Rational(-5,2) - x)**sp.Rational(1,5)
   for k in range(1)], True),
 ("g = y^2 - x^2 - x   (NOT a coordinate)", y**2 - x**2 - x,
  [ sp.sqrt(x**2 + x + sp.Rational(-5,2)), -sp.sqrt(x**2 + x + sp.Rational(-5,2))], False),
 ("g = y^2 - x^2 - 5x + 2   (NOT a coordinate; delta^0 = 1)", y**2 - x**2 - 5*x + 2,
  [ sp.sqrt(x**2 + 5*x - 2 + sp.Rational(-5,2)), -sp.sqrt(x**2 + 5*x - 2 + sp.Rational(-5,2))], False),
 ("g = y^2 - x^3 - x^2  (exponent lattice misses x^-1: VACUOUS)", y**2 - x**3 - x**2,
  [ sp.sqrt(x**3 + x**2 + sp.Rational(-5,2))], None),
 ("g = x + y^2 + y   (coordinate; f = y)", x + y**2 + y,
  [(-1 + sp.sqrt(1 - 4*(x - sp.Rational(-5,2))))/2], True),
]

print("== COROLLARY NO-RESIDUE: [x^{-1}] of 1/g_y(x,tau(x)) ==")
for (lab, g, taus, keller) in CASES:
    gy = sp.diff(g, y)
    vals = [sp.simplify(coeff_xinv(1/gy.subs(y, t))) for t in taus]
    print(f"   {lab}")
    print(f"      [x^-1] 1/g_y(tau) = {vals}")
    if keller is None:
        print("      (vacuous: ord_t g_y(tau) is a half-integer, x^{-1} is not in the lattice)")
        continue
    if keller:
        check(f"NO-RESIDUE holds (Keller) :: {lab}", all(v == 0 for v in vals), str(vals))
    else:
        check(f"NO-RESIDUE FAILS (non-coordinate) :: {lab}",
              any(v != 0 for v in vals), str(vals))
print()
if FAILURES: print(f"FAILURES: {len(FAILURES)}"); sys.exit(1)
print("ALL CONTROLS PASSED")
