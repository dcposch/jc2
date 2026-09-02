import sympy as sp
from wall import *
c = sp.symbols('c')

def rowRQS(e,U,eqname):
    """top coeff, decomposed on the monomials R, Q, S^2 (nothing else may occur)."""
    M = model(e,U); E = equations(M)
    co = sp.expand(laurent(E[eqname], tops(M)[eqname], 1)[0].subs(C, c*b*A**2))
    P = sp.Poly(co, R, Q, S)
    got = {}
    for mon, cf in P.terms():
        got[mon] = sp.factor(cf)
    return M, got

def ref_row(e,U,which):
    M=model(e,U); m,sig,g,n = M['m'],M['sig'],M['g'],M['n']
    if which=='EQ3': return [12, 8*(e-m), -6*(e-sig)]
    if which=='EQ1': return [6*(3*e+1)+9*c, 4*(2*e+1)*(e-m)+c*2*(g-2*m),
                             -3*(e+1)*(e-sig)+c*sp.Rational(3,2)*(e-g+sig)]
    if which=='EQ2': return [6*(4*e+3)+12*c,
                             2*(8*e**2-4*e*m+6*e-6*m+1)+c*4*(g-m),
                             -3*(2*e**2+2*e-3*sig)+c*sp.Rational(3,2)*(2*e-2*g+1)]

for which in ['EQ3','EQ1','EQ2']:
    print("=== ",which)
    for (e,U) in [(1,3),(1,5),(1,7),(2,6),(2,8),(3,9),(3,11),(4,12)]:
        M,got = rowRQS(e,U,which); n=M['n']
        # actual row read off:  coefficient of R -> x-entry * a A^3 n ; Q -> y-entry * b A^2 ; S^2 -> w-entry * a A / b
        cx = got.get((1,0,0), 0)/(a*A**3*n)
        cy = got.get((0,1,0), 0)/(b*A**2)
        cw = got.get((0,0,2), 0)/(a*A/b)
        others = {k:v for k,v in got.items() if k not in [(1,0,0),(0,1,0),(0,0,2)]}
        rf = ref_row(e,U,which)
        norms = [sp.simplify(cx/rf[0]) if rf[0]!=0 else None,
                 sp.simplify(cy/rf[1]) if rf[1]!=0 else None,
                 sp.simplify(cw/rf[2]) if rf[2]!=0 else None]
        print("  e=%d U=%d n=%d  norms=%s  extra_monomials=%s"%(e,U,n,norms,others))
