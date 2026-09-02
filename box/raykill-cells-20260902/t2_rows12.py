import sympy as sp
from wall import *
c = sp.symbols('c'); x,y,w = sp.symbols('x y w')

def row(e,U,eqname):
    M = model(e,U); E = equations(M)
    co = laurent(E[eqname], tops(M)[eqname], 1)[0].subs(C, c*b*A**2)
    n,m,sig = M['n'],M['m'],M['sig']
    co = co.subs({R: x/(a*A**3*n), Q: y/(b*A**2), S: sp.sqrt(b*w/(a*A))})
    co = sp.Poly(sp.expand(sp.simplify(co)), x,y,w)
    return M, [sp.simplify(co.coeff_monomial(v)) for v in (x,y,w)]

print("== EQ1: flagship [6(3e+1),4(2e+1)(e-m),-3(e+1)(e-sigma)] + c*[9,2(g-2m),(3/2)(e-g+sigma)]")
for (e,U) in [(1,3),(1,5),(1,7),(2,6),(2,8),(3,9),(3,11),(4,12)]:
    M,rw = row(e,U,'EQ1'); m,sig,g = M['m'],M['sig'],M['g']
    ref = [6*(3*e+1)+9*c, 4*(2*e+1)*(e-m)+c*2*(g-2*m), -3*(e+1)*(e-sig)+c*sp.Rational(3,2)*(e-g+sig)]
    print(" e=%d U=%d"%(e,U), [sp.simplify(rw[i]/ref[i]) for i in range(3)])

print("== EQ2: flagship [6(4e+3),2(8e^2-4em+6e-6m+1),-3(2e^2+2e-3sigma)] + c*[12,4(g-m),(3/2)(2e-2g+1)]")
for (e,U) in [(1,3),(1,5),(1,7),(2,6),(2,8),(3,9),(3,11),(4,12)]:
    M,rw = row(e,U,'EQ2'); m,sig,g = M['m'],M['sig'],M['g']
    ref = [6*(4*e+3)+12*c,
           2*(8*e**2-4*e*m+6*e-6*m+1)+c*4*(g-m),
           -3*(2*e**2+2*e-3*sig)+c*sp.Rational(3,2)*(2*e-2*g+1)]
    print(" e=%d U=%d"%(e,U), [sp.simplify(rw[i]/ref[i]) if ref[i]!=0 else ('num=',sp.simplify(rw[i])) for i in range(3)])
