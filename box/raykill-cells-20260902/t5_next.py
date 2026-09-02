import sympy as sp, time
from wall2 import *
t0=time.time()
CELLS=[(1,3),(1,5),(1,7),(1,9),(1,11),(2,6),(2,8),(2,10),(2,12),(3,9),(3,11),(3,13),
       (4,12),(4,14),(5,15),(5,17),(6,18)]
UNK=[A1,S1,Q1,R1,C1g]

def ray_sub(e):
    return {C: -b*(1+2*e)*A**2, R: S**2/(4*b*A**2), Q: 3*a*S**2/(4*b**2*A)}

for (e,U) in CELLS:
    M=model(e,U,K=2); E=equations(M); n=M['n']; sub=ray_sub(e)
    top_ok=[]
    rows=[]; inhom=[]
    for which in ['EQ3','EQ1','EQ2','EQ4']:
        t = tops(M)[which]
        c0 = sp.expand(sp.cancel(zc(E[which], t).subs(sub)))
        top_ok.append(sp.simplify(c0))
        c1 = sp.expand(sp.cancel(zc(E[which], t-1).subs(sub)))
        # linearity check + row extraction
        row=[sp.cancel(sp.diff(c1,v)) for v in UNK]
        rest = sp.cancel(sp.expand(c1 - sum(row[i]*UNK[i] for i in range(5))))
        rows.append(row); inhom.append(sp.simplify(rest))
    print("e=%d U=%d n=%d  tops on ray = %s"%(e,U,n,top_ok))
    Mx=sp.Matrix(rows)
    Mx=sp.Matrix([[sp.cancel(x) for x in r] for r in Mx.tolist()])
    print("   inhomogeneous parts at top-1 :", inhom)
    print("   rank of 4x5 next-order matrix :", Mx.rank(), " (U-3e =",U-3*e,")")
print("time",time.time()-t0)
