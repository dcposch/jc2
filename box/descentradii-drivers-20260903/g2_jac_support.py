#!/usr/bin/env python3
"""Cheapest G2 test: with the V2=1 leading-form shape, what is the support of J(f,g)?
If J cannot be a multiple of x^4 for degree/support reasons, that is a kill
without Groebner.  Desk-scale.
"""
import sympy as sp

x, y = sp.symbols('x y')
b0,b1,b2,b3,b4 = sp.symbols('b0:5')
p,q,r,s = sp.symbols('p q r s')
d1,d2 = sp.symbols('d1 d2')
e1,e2,e3,e4 = sp.symbols('e1:5')
c = sp.symbols('c')

h = sp.expand(y*(y-x)**4 + b4*y**4 + b3*y**3 + b2*y**2 + b1*y + b0)
A = sp.expand((h - b0)/y)
beta = sp.expand(p*A + q*y + r*x + s)
f = sp.expand(h**2 + 2*beta)
G1 = sp.expand(d1*A + d2)
G0 = sp.expand(e1*A + e2*(y-x) + e3*x + e4)
g = sp.expand(h**3 + G1*h + G0)

print("deg f", sp.degree(f,y), sp.total_degree(f), "deg_x", sp.degree(f,x))
print("deg g", sp.degree(g,y), sp.total_degree(g), "deg_x", sp.degree(g,x))

print("computing J ...")
J = sp.expand(sp.diff(f,x)*sp.diff(g,y) - sp.diff(f,y)*sp.diff(g,x))
print("J deg_y", sp.degree(J,y), "deg_x", sp.degree(J,x), "total", sp.total_degree(J))

# coefficient of highest y in J: must vanish for J in k[x]
PJ = sp.Poly(J, y)
print("deg_y J =", PJ.degree())
for d in range(PJ.degree(), max(PJ.degree()-4, -1), -1):
    co = sp.expand(PJ.coeff_monomial(y**d))
    print("  [y^%d] J  totaldeg_x=%s  nterms=%d  %s" %
          (d, sp.total_degree(co) if co else None,
           len(sp.Poly(co, x).terms()) if co else 0,
           (str(sp.factor(co))[:180] if co else '0')))

# Is the y^0 part a pure monomial c x^4?
co0 = sp.expand(PJ.coeff_monomial(y**0))
print("\n[y^0] J nterms", len(sp.Poly(co0, x).terms()) if co0 else 0)
print("[y^0] J =", str(co0)[:300])

# For J = c x^4 we need every y^d, d>0 coeff 0, and [y^0] = c x^4
# Cheapest: look at the highest-y coefficient; it is a polynomial in x and the
# parameters. If it is not identically zero and not cancellable, we get equations.

print("\n-- number of (x,y) monomials in J --")
Pxy = sp.Poly(J, x, y)
print("  nterms", len(Pxy.terms()), "  max (i,j)", max(Pxy.monoms()) if Pxy.monoms() else None)
# terms with y-power > 0 must die; terms with x-power != 4 in y^0 must die;
# the x^4 y^0 coeff must be c != 0
eqs = []
for (i, j), co in zip(Pxy.monoms(), Pxy.coeffs()):
    if j > 0 or i != 4:
        if co != 0:
            eqs.append(sp.expand(co))
    else:
        # i==4, j==0: co - c == 0
        eqs.append(sp.expand(co - c))
eqs = [e for e in eqs if e != 0]
print("  raw vanishing/matching eqs", len(eqs))
# drop duplicates
ueqs = []
seen = set()
for e in eqs:
    s = str(e)
    if s not in seen:
        seen.add(s); ueqs.append(e)
print("  unique eqs", len(ueqs))

# Positive/negative control discipline: a random specialization of parameters
# should give J not a monomial (negative: the shape is not automatically Jacobian)
import random
rng = random.Random(0)
subs = {v: rng.randint(-2, 2) or 1 for v in
        [b0,b1,b2,b3,b4,p,q,r,s,d1,d2,e1,e2,e3,e4]}
Js = sp.expand(J.subs(subs))
print("\nNEGATIVE control (random params): J =", str(Js)[:200],
      "  is_monomial_in_x?", sp.degree(Js, y) <= 0 and set(sp.Poly(Js, x).monoms()) <= {(4,), (0,)})
