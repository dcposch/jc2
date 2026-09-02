import sympy as sp, time
from wall2 import *
t0=time.time()
UNK=[A1,S1,Q1,R1,C1g]
def ray_sub(e): return {C:-b*(1+2*e)*A**2, R:S**2/(4*b*A**2), Q:3*a*S**2/(4*b**2*A)}

def nextorder(e,U):
    M=model(e,U,K=2); E=equations(M); sub=ray_sub(e)
    rows=[]; rhs=[]
    for which in ['EQ3','EQ1','EQ2','EQ4']:
        t=tops(M)[which]
        c1=sp.expand(sp.cancel(zc(E[which],t-1).subs(sub)))
        row=[sp.cancel(sp.diff(c1,v)) for v in UNK]
        rest=sp.cancel(sp.expand(c1-sum(row[i]*UNK[i] for i in range(5))))
        rows.append(row); rhs.append(-rest)
    return M, sp.Matrix(rows), sp.Matrix(rhs)

print("=== U = 3e  (boundary cell): consistency of the inhomogeneous next-order system")
for e in range(1,9):
    U=3*e
    M,Mx,rhs = nextorder(e,U)
    Aug = Mx.row_join(rhs)
    r0, r1 = Mx.rank(), Aug.rank()
    guess = -3*(32*e**3+32*e**2+6*e+1)*a*b*A**6
    print("  e=%d  rank(M)=%d  rank([M|rhs])=%d   rhs=%s   check -3(32e^3+32e^2+6e+1)abA^6: %s"
          %(e,r0,r1,list(rhs), sp.simplify(rhs[0]-guess)==0))
print()
print("=== U >= 3e+2 : homogeneous, kernel basis")
for (e,U) in [(1,5),(1,7),(1,9),(2,8),(2,10),(3,11),(3,13),(4,14)]:
    M,Mx,rhs = nextorder(e,U); n=M['n']
    assert all(x==0 for x in rhs)
    ker=Mx.nullspace()
    print("  e=%d U=%d n=%d rank=%d dim ker=%d"%(e,U,n,Mx.rank(),len(ker)))
    for v in ker: print("       ", [sp.simplify(t) for t in v.T])
print("time",time.time()-t0)
