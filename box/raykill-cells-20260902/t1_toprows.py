import sympy as sp
from wall import *

# ---- replay the flagship's Chamber II rows in (x,y,w) for GENERAL c ------------
# x = a A^3 R n ;  y = b A^2 Q ;  w = a A S^2 / b ;  c = C/(b A^2)
c = sp.symbols('c')
x, y, w = sp.symbols('x y w')

def row_of(e,U,eqname,scale=None):
    M = model(e,U); E = equations(M)
    top = tops(M)[eqname]
    co = laurent(E[eqname], top, 1)[0]
    co = co.subs(C, c*b*A**2)
    co = sp.expand(sp.simplify(co))
    n, m, sig = M['n'], M['m'], M['sig']
    # rewrite leaders in x,y,w
    sub = {R: x/(a*A**3*n), Q: y/(b*A**2), S: sp.sqrt(b*w/(a*A))}
    co = sp.simplify(sp.expand(co.subs(sub)))
    co = sp.Poly(sp.expand(co), x, y, w)
    return M, co

for (e,U) in [(1,3),(1,5),(2,6),(2,8),(3,9)]:
    M,co = row_of(e,U,'EQ3')
    n = M['n']
    # normalise so that coefficient pattern is comparable with [12, -8n, 3n]*A
    cx = co.coeff_monomial(x); cy = co.coeff_monomial(y); cw = co.coeff_monomial(w)
    print("EQ3 e=%d U=%d n=%d :"%(e,U,n), sp.simplify(cx), sp.simplify(cy), sp.simplify(cw),
          " | ratios vs flagship gen-c row [12, 8(e-m), -6(e-sigma)]:",
          sp.simplify(cx/12), sp.simplify(cy/(8*(e-M['m']))), sp.simplify(cw/(-6*(e-M['sig']))))
