#!/usr/bin/env python3
"""G2 after the top Jacobian coefficient forces p=0 (beta has no A-component).

Then beta = q y + r x + s, alpha=0, gamma=beta^2, and we continue the
c2-style / J=c x^4 analysis.  Saturate c != 0.
"""
import sympy as sp

x, y = sp.symbols('x y')
b0,b1,b2,b3,b4 = B_ = sp.symbols('b0:5')
q,r,s = sp.symbols('q r s')
c, T = sp.symbols('c T')

h = sp.expand(y*(y-x)**4 + b4*y**4 + b3*y**3 + b2*y**2 + b1*y + b0)
beta = sp.expand(q*y + r*x + s)          # p = 0
# alpha = 0 because deg beta^2 = 2 < 5 = deg h
alpha = 0
f = sp.expand(h**2 + 2*beta)
g = sp.expand(h**3 + 3*beta*h)
print("deg f,g", sp.degree(f,y), sp.degree(g,y), "deg_x", sp.degree(f,x), sp.degree(g,x))
print("beta^2 remainder mod h is beta^2 (alpha=0):",
      sp.degree(sp.Poly(beta**2, y), y) < 5)

J = sp.expand(sp.diff(f,x)*sp.diff(g,y) - sp.diff(f,y)*sp.diff(g,x))
print("J deg_y", sp.degree(J,y), "deg_x", sp.degree(J,x))

R = sp.expand(J - c*x**4)
PR = sp.Poly(R, x, y)
eqs = [sp.expand(co) for co in PR.coeffs() if sp.expand(co) != 0]
print("#eqs", len(eqs))
unk = list(B_) + [q, r, s, c]
print("unknowns", unk)

print("\n-- MAIN p=0: saturate J=c x^4 at c!=0 --")
Gb = sp.groebner(eqs + [T*c - 1], *(unk + [T]), order='grevlex')
print("  EMPTY?" , list(Gb) == [1], " size", len(list(Gb)))
if list(Gb) != [1]:
    print("  basis", list(Gb)[:12])

print("\n-- UNSATURATED p=0 --")
Gb0 = sp.groebner(eqs, *unk, order='grevlex')
print("  EMPTY?", list(Gb0)==[1], " size", len(list(Gb0)))
if list(Gb0) != [1]:
    print("  basis", list(Gb0)[:12])

print("\n-- POSITIVE: drop the (4,0) matching --")
eqs_drop = []
for (i,j), co in zip(PR.monoms(), PR.coeffs()):
    e = sp.expand(co)
    if e==0: continue
    if (i,j)==(4,0): continue
    eqs_drop.append(e)
GbP = sp.groebner(eqs_drop + [T*c-1], *(unk+[T]), order='grevlex')
print("  ", "EMPTY [1]" if list(GbP)==[1] else "NON-TRIVIAL (%d)"%len(list(GbP)))

print("\n-- NEGATIVE: toy c=1, q=1 --")
GbN = sp.groebner([c-1, q-1, T*c-1], *(unk+[T]), order='grevlex')
print("  ", "EMPTY [1] (BAD)" if list(GbN)==[1] else "NON-TRIVIAL (%d) [expected]"%len(list(GbN)))

# Also: high-y of J with p=0 should start lower
PJ = sp.Poly(J, y)
print("\nhigh y of J (p=0):")
for d in range(min(PJ.degree(), 8), max(PJ.degree()-6, -1), -1):
    co = sp.expand(PJ.coeff_monomial(y**d))
    print("  y^%d" % d, str(sp.factor(co))[:140] if co else 0)
