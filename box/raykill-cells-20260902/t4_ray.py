import sympy as sp, time
from wall2 import *
t0=time.time()
c = sp.symbols('c')
CELLS=[(1,3),(1,5),(1,7),(1,9),(2,6),(2,8),(2,10),(3,9),(3,11),(4,12),(4,14),(5,15)]

print("== det of the 3x3 (EQ3,EQ1,EQ2) in chamber II, general c ==")
for (e,U) in CELLS[:6]:
    M=model(e,U,K=2); E=equations(M); n=M['n']
    rows=[]
    for which in ['EQ3','EQ1','EQ2']:
        co = sp.expand(zc(E[which], tops(M)[which]).subs(C, c*b*A**2))
        P=dict(sp.Poly(co,R,Q,S).terms())
        rows.append([sp.cancel(P.get((1,0,0),0)/(a*A**3*n)),
                     sp.cancel(P.get((0,1,0),0)/(b*A**2)),
                     sp.cancel(P.get((0,0,2),0)/(a*A/b))])
    Mx=sp.Matrix(rows); det=sp.factor(sp.cancel(Mx.det()))
    ref = 36*n*(c+2*e)*(c+2*e+1)
    print("  e=%d U=%d n=%d  det=%s   det/(36 n (c+2e)(c+2e+1)) = %s"%(e,U,n,det,sp.cancel(det/ref)))

print()
print("== Wall B: c = -(2e+1).  rows and kernel ==")
for (e,U) in CELLS:
    M=model(e,U,K=2); E=equations(M); n=M['n']
    wall = {C: -b*(1+2*e)*A**2}
    rows=[]
    for which in ['EQ3','EQ1','EQ2','EQ4']:
        co = sp.expand(zc(E[which], tops(M)[which]).subs(wall))
        rows.append(co)
    # EQ3,EQ1,EQ2 linear in (R,Q,S^2); EQ4 quadratic
    lin=[]
    for co in rows[:3]:
        P=dict(sp.Poly(co,R,Q,S).terms())
        lin.append([sp.cancel(P.get((1,0,0),0)/(a*A**3*n)),
                    sp.cancel(P.get((0,1,0),0)/(b*A**2)),
                    sp.cancel(P.get((0,0,2),0)/(a*A/b))])
    Mx=sp.Matrix(lin)
    ker=Mx.nullspace()
    print("  e=%d U=%d n=%d rank=%d rows=%s"%(e,U,n,Mx.rank(),lin))
    print("      ref rows [12,-8n,3n],[-3,0,3n/4],[6,2-4e-8n,3e+9n/2-3/2] ->",
          [sp.Integer(12),-8*n,3*n],[-3,0,sp.Rational(3,4)*n],
          [6,2-4*e-8*n,3*e+sp.Rational(9,2)*n-sp.Rational(3,2)])
    print("      kernel=%s   (flagship ray (n/4,3/4,1))"%[sp.nsimplify(v.T) for v in ker])
print("time",time.time()-t0)
