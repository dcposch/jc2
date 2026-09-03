#!/usr/bin/env python3
"""G2: ALL 14 order-condition monomials of h (bound -5/4) + Moh-pattern beta
(4 coeffs) + c.  19 unknowns.  J = c x^4, saturate c != 0.
"""
import sympy as sp

x, y = sp.symbols('x y')
# 14 free in h:
# y^4, x y^4,
# y^3, x y^3, x^2 y^3,
# y^2, x y^2, x^2 y^2, x^3 y^2,
# y, x y, x^2 y,
# 1, x
names = [
    'h04','h14',
    'h03','h13','h23',
    'h02','h12','h22','h32',
    'h01','h11','h21',
    'h00','h10',
]
H = sp.symbols(' '.join(names))
(h04,h14,h03,h13,h23,h02,h12,h22,h32,h01,h11,h21,h00,h10) = H
p,q,r,s = sp.symbols('p q r s')
c, T = sp.symbols('c T')

h = sp.expand(
    y**5
    + h04*y**4 + h14*x*y**4
    + h03*y**3 + h13*x*y**3 + h23*x**2*y**3
    + h02*y**2 + h12*x*y**2 + h22*x**2*y**2 + h32*x**3*y**2
    + h01*y    + h11*x*y    + h21*x**2*y
    + h00      + h10*x
)
A = sp.expand((h - h.subs(y,0))/y)
beta = sp.expand(p*A + q*y + r*x + s)
qd, rd = sp.div(sp.Poly(sp.expand(beta**2), y), sp.Poly(h, y), y)
alpha = sp.expand(qd.as_expr())
f = sp.expand(h**2 + 2*beta)
g = sp.expand(h**3 + 3*beta*h + sp.Rational(3,2)*alpha)
print("deg f,g", sp.degree(f,y), sp.degree(g,y), "deg_x", sp.degree(f,x), sp.degree(g,x))

J = sp.expand(sp.diff(f,x)*sp.diff(g,y) - sp.diff(f,y)*sp.diff(g,x))
print("J deg_y,deg_x,total", sp.degree(J,y), sp.degree(J,x), sp.total_degree(J))
R = sp.expand(J - c*x**4)
PR = sp.Poly(R, x, y)
eqs = [sp.expand(co) for co in PR.coeffs() if sp.expand(co)!=0]
unk = list(H) + [p,q,r,s,c]
print("#eqs", len(eqs), "#unk", len(unk))

print("MAIN saturate c!=0 ...")
Gb = sp.groebner(eqs + [T*c - 1], *(unk+[T]), order='grevlex')
print("  EMPTY?", list(Gb)==[1], "size", len(list(Gb)))
if list(Gb)!=[1]:
    print("  first", list(Gb)[:8])

print("UNSATURATED ...")
Gb0 = sp.groebner(eqs, *unk, order='grevlex')
print("  EMPTY?", list(Gb0)==[1], "size", len(list(Gb0)))
if list(Gb0)!=[1]:
    print("  first", list(Gb0)[:8])

print("POSITIVE drop (4,0) matching ...")
eqs_drop=[]
for (i,j),co in zip(PR.monoms(), PR.coeffs()):
    e=sp.expand(co)
    if e==0: continue
    if (i,j)==(4,0): continue
    eqs_drop.append(e)
GbP = sp.groebner(eqs_drop+[T*c-1], *(unk+[T]), order='grevlex')
print("  ", "EMPTY [1]" if list(GbP)==[1] else "NON-TRIVIAL (%d)"%len(list(GbP)))

print("NEGATIVE toy c=1 p=1")
GbN = sp.groebner([c-1,p-1,T*c-1], *(unk+[T]), order='grevlex')
print("  ", "EMPTY BAD" if list(GbN)==[1] else "NON-TRIVIAL (%d) expected"%len(list(GbN)))
