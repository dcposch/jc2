import sympy as sp, time
from wall2 import *
c = sp.symbols('c')
t0=time.time()
def ref_row(M,which):
    e,m,sig,g = M['e'],M['m'],M['sig'],M['g']
    if which=='EQ3': return [sp.Integer(12), 8*(e-m), -6*(e-sig)]
    if which=='EQ1': return [6*(3*e+1)+9*c, 4*(2*e+1)*(e-m)+c*2*(g-2*m),
                             -3*(e+1)*(e-sig)+c*sp.Rational(3,2)*(e-g+sig)]
    if which=='EQ2': return [6*(4*e+3)+12*c,
                             2*(8*e**2-4*e*m+6*e-6*m+1)+c*4*(g-m),
                             -3*(2*e**2+2*e-3*sig)+c*sp.Rational(3,2)*(2*e-2*g+1)]
for (e,U) in [(1,3),(1,5),(1,7),(2,6),(2,8),(3,9),(3,11),(4,12)]:
    M = model(e,U,K=2); E = equations(M); n=M['n']
    for which in ['EQ3','EQ1','EQ2']:
        co = sp.expand(zc(E[which], tops(M)[which]).subs(C, c*b*A**2))
        P = sp.Poly(co, R,Q,S)
        got = dict(P.terms())
        cx = sp.cancel(got.get((1,0,0),0)/(a*A**3*n))
        cy = sp.cancel(got.get((0,1,0),0)/(b*A**2))
        cw = sp.cancel(got.get((0,0,2),0)/(a*A/b))
        extra = {k:v for k,v in got.items() if k not in [(1,0,0),(0,1,0),(0,0,2)] and v!=0}
        rf = ref_row(M,which)
        nm = [sp.cancel(cx/rf[0]), sp.cancel(cy/rf[1]) if rf[1]!=0 else 'rf0:%s'%cy,
              sp.cancel(cw/rf[2]) if rf[2]!=0 else 'rf0:%s'%cw]
        print("e=%d U=%d %s norms=%s extra=%s"%(e,U,which,nm,extra))
print("time",time.time()-t0)
