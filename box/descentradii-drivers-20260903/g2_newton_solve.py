#!/usr/bin/env python3
"""G2 with the ONE-point-at-infinity Newton shape forced by Phi(delta2'=-1/2):
h = y^5 + a x^2 y + (y-polynomial of deg<=4) + e x
  [4 roots of h at y^4 ~ x^2 i.e. y ~ x^{1/2}=t^{-1/2}=delta2;
   1 root near 0, the major D1]
beta = p A + q y + r x + s     [Appendix-II pattern]
f = h^2+2 beta, g = h^3+3 beta h+(3/2) alpha, J = c x^4, saturate c!=0.

FALLACY note: the y-only + a x^2 y + e x truncation of h is the (16,12)-style
'tight' shape, not the full 14-monomial order-condition list.  Result is a
slice.  The full order-condition count is emitted first.
"""
import sympy as sp

x, y = sp.symbols('x y')

def allowed_monomials():
    print("== order-condition monomials for h, bound ord_sigma >= -5/4 ==")
    print("  i <= (5/4)*(j+1), i+j <= 5, i <= 4, j <= 5")
    hs = []
    for j in range(5, -1, -1):
        imax = min(4, 5-j, int((5*(j+1))//4))
        for i in range(0, imax+1):
            if j==5 and i==0:
                continue  # leader
            hs.append((i,j))
            print("   x^%d y^%d" % (i,j))
    print("  free in h:", len(hs))
    print("== beta, bound ord_sigma >= -5/2, deg_y<=4, deg_x<=8 ==")
    bs = []
    for j in range(0, 5):
        imax = min(8, 10-j, int((5*j+10)//4))
        for i in range(0, imax+1):
            bs.append((i,j))
    print("  free in beta:", len(bs), "  total h+beta+c =", len(hs)+len(bs)+1)

allowed_monomials()

print("\n== SLICE: Newton-tight h + Moh beta, groebner J=c x^4 at c!=0 ==")
a,b0,b1,b2,b3,b4,e = sp.symbols('a b0 b1 b2 b3 b4 e')
p,q,r,s = sp.symbols('p q r s')
c, T = sp.symbols('c T')
h = sp.expand(y**5 + a*x**2*y + b4*y**4 + b3*y**3 + b2*y**2 + b1*y + b0 + e*x)
A = sp.expand((h - h.subs(y,0))/y)
beta = sp.expand(p*A + q*y + r*x + s)
qd, rd = sp.div(sp.Poly(sp.expand(beta**2), y), sp.Poly(h, y), y)
alpha = sp.expand(qd.as_expr())
f = sp.expand(h**2 + 2*beta)
g = sp.expand(h**3 + 3*beta*h + sp.Rational(3,2)*alpha)
print("deg f,g", sp.degree(f,y), sp.degree(g,y), "deg_x", sp.degree(f,x), sp.degree(g,x))
print("alpha deg_y", sp.degree(alpha,y))

J = sp.expand(sp.diff(f,x)*sp.diff(g,y) - sp.diff(f,y)*sp.diff(g,x))
print("J deg_y,deg_x,total", sp.degree(J,y), sp.degree(J,x), sp.total_degree(J))
R = sp.expand(J - c*x**4)
PR = sp.Poly(R, x, y)
eqs = [sp.expand(co) for co in PR.coeffs() if sp.expand(co)!=0]
unk = [a,b0,b1,b2,b3,b4,e,p,q,r,s,c]
print("#eqs", len(eqs), "#unk", len(unk))

print("MAIN saturate c!=0 ...")
Gb = sp.groebner(eqs + [T*c - 1], *(unk+[T]), order='grevlex')
print("  EMPTY?", list(Gb)==[1], "size", len(list(Gb)))
if list(Gb)!=[1]:
    print("  first", list(Gb)[:10])

print("UNSATURATED ...")
Gb0 = sp.groebner(eqs, *unk, order='grevlex')
print("  EMPTY?", list(Gb0)==[1], "size", len(list(Gb0)))
if list(Gb0)!=[1]:
    print("  first", list(Gb0)[:10])

print("NEGATIVE toy c=1,p=1")
GbN = sp.groebner([c-1, p-1, T*c-1], *(unk+[T]), order='grevlex')
print("  ", "EMPTY BAD" if list(GbN)==[1] else "NON-TRIVIAL (%d) expected"%len(list(GbN)))
