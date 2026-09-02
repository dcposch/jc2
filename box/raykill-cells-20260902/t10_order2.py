import sympy as sp, time
from wall2 import *
t0=time.time()
be, de = sp.symbols('beta delta')     # free next-order parameters
def setup(e,U):
    M=model(e,U,K=3); n=M['n']
    Rv,Qv = S**2/(4*b*A**2), 3*a*S**2/(4*b**2*A)
    al = be - de/2; ga = be + de/2; ep = -4*e*al
    sub = {C:-b*(1+2*e)*A**2, R:Rv, Q:Qv,
           A1: al*A, S1: be*S, Q1: ga*Qv, R1: de*Rv, C1g: ep*b*A**2}
    return M, sub
UNK2=[A2,S2,Q2,R2,C2g]
for (e,U) in [(1,3),(1,5),(1,7),(1,9),(2,6),(2,8),(2,10),(3,11),(3,13),(4,14),(4,16),(5,17)]:
    M,sub = setup(e,U); E=equations(M); n=M['n']
    present=[v for v in UNK2 if any(v in sp.preorder_traversal(M[k]) for k in ('eta','s','q','r','G'))]
    rows=[];rhs=[]
    for which in ['EQ3','EQ1','EQ2','EQ4']:
        c2=sp.expand(sp.cancel(zc(E[which],tops(M)[which]-2).subs(sub)))
        row=[sp.cancel(sp.diff(c2,v)) for v in UNK2]
        rest=sp.cancel(sp.expand(c2-sum(row[i]*UNK2[i] for i in range(5))))
        rows.append(row); rhs.append(sp.factor(sp.simplify(rest)))
    Mx=sp.Matrix(rows); Aug=Mx.row_join(sp.Matrix(rhs))
    print("e=%d U=%d n=%d present3rd=%s  rank(M2)=%d rank(aug)=%d"
          %(e,U,n,[str(v) for v in present],Mx.rank(),Aug.rank()))
print("time",time.time()-t0)
