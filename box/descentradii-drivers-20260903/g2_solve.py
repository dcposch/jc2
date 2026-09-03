#!/usr/bin/env python3
"""G2: Appendix-II reduction with V2=1 leading form y(y-x)^4, Moh (2)(3) expansion
f = h^2+2β, g = h^3+3βh+(3/2)α, β^2 = α h + γ, and J = c x^4.

Unknowns: b0..b4 (lower y-terms of h), p,q,r,s (β = p A + q y + r x + s), c.
= 10 unknowns.  Saturate at c != 0 (Rabinowitsch).  Controls on the saturation.
"""
import sympy as sp

x, y = sp.symbols('x y')
b0,b1,b2,b3,b4 = B_ = sp.symbols('b0:5')
p,q,r,s = P_ = sp.symbols('p q r s')
c, T = sp.symbols('c T')
unk = list(B_) + list(P_) + [c]

h = sp.expand(y*(y - x)**4 + b4*y**4 + b3*y**3 + b2*y**2 + b1*y + b0)
A = sp.expand((h - b0)/y)
beta = sp.expand(p*A + q*y + r*x + s)

qdiv, rdiv = sp.div(sp.Poly(sp.expand(beta**2), y), sp.Poly(h, y), y)
alpha = sp.expand(qdiv.as_expr())
gamma = sp.expand(rdiv.as_expr())
print("deg_y h,beta,alpha,gamma =",
      sp.degree(h,y), sp.degree(beta,y), sp.degree(alpha,y), sp.degree(gamma,y))
print("beta^2 - alpha*h - gamma == 0:",
      sp.expand(beta**2 - alpha*h - gamma) == 0)

f = sp.expand(h**2 + 2*beta)
g = sp.expand(h**3 + 3*beta*h + sp.Rational(3, 2)*alpha)
print("deg f,g", sp.degree(f,y), sp.degree(g,y),
      "total", sp.total_degree(f), sp.total_degree(g),
      "deg_x", sp.degree(f,x), sp.degree(g,x))

print("computing J...")
J = sp.expand(sp.diff(f, x)*sp.diff(g, y) - sp.diff(f, y)*sp.diff(g, x))
print("J deg_y", sp.degree(J,y), "deg_x", sp.degree(J,x), "total", sp.total_degree(J))

R = sp.expand(J - c*x**4)
PR = sp.Poly(R, x, y)
eqs = []
for co in PR.coeffs():
    e = sp.expand(co)
    if e != 0:
        eqs.append(e)
print("coefficient equations for J=c x^4:", len(eqs))
print("unknowns:", len(unk), unk)

# MAIN: saturate at c != 0
print("\n-- MAIN: groebner(eqs + [T*c-1], grevlex) --")
Gb = sp.groebner(eqs + [T*c - 1], *(unk + [T]), order='grevlex')
Gbl = list(Gb)
print("  basis size", len(Gbl), " EMPTY (1 in ideal)?" , Gbl == [1])
if Gbl != [1]:
    print("  first 8:", Gbl[:8])

# Without saturation (c may be 0)
print("\n-- UNSATURATED: groebner(eqs) --")
Gb0 = sp.groebner(eqs, *unk, order='grevlex')
Gbl0 = list(Gb0)
print("  basis size", len(Gbl0), " EMPTY?", Gbl0 == [1])
if Gbl0 != [1]:
    print("  first 8:", Gbl0[:8])

# POSITIVE control: drop the x^4 y^0 matching (i.e. don't force the c x^4 term,
# only force all other monomials of J to vanish).  If MAIN is empty because of
# those other monomials, dropping the matching eq should still be empty or not.
print("\n-- POSITIVE: drop the (x^4 y^0) matching equation --")
eqs_drop = []
for (i, j), co in zip(PR.monoms(), PR.coeffs()):
    e = sp.expand(co)
    if e == 0:
        continue
    if (i, j) == (4, 0):
        continue  # drop matching
    eqs_drop.append(e)
GbP = sp.groebner(eqs_drop + [T*c - 1], *(unk + [T]), order='grevlex')
print("  drop (4,0):", "EMPTY [1]" if list(GbP)==[1] else "NON-TRIVIAL (%d)" % len(list(GbP)))

# NEGATIVE: a consistent toy in the same ring
print("\n-- NEGATIVE: consistent toy c=1, p=0, b0=1 --")
GbN = sp.groebner([c-1, p, b0-1, T*c-1], *(unk+[T]), order='grevlex')
print("  ", "EMPTY [1] (BAD)" if list(GbN)==[1] else "NON-TRIVIAL (%d) [expected]" % len(list(GbN)))
