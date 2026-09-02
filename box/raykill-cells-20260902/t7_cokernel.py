import sympy as sp, time
from wall2 import *
t0=time.time()
UNK=[A1,S1,Q1,R1,C1g]
def ray_sub(e): return {C:-b*(1+2*e)*A**2, R:S**2/(4*b*A**2), Q:3*a*S**2/(4*b**2*A)}
def nextorder(e,U):
    M=model(e,U,K=2); E=equations(M); sub=ray_sub(e); rows=[]; rhs=[]
    for which in ['EQ3','EQ1','EQ2','EQ4']:
        t=tops(M)[which]
        c1=sp.expand(sp.cancel(zc(E[which],t-1).subs(sub)))
        row=[sp.cancel(sp.diff(c1,v)) for v in UNK]
        rest=sp.cancel(sp.expand(c1-sum(row[i]*UNK[i] for i in range(5))))
        rows.append(row); rhs.append(rest)
    return M, sp.Matrix(rows), sp.Matrix(rhs)

print("left-null vector L of the 4x5 next-order matrix (rows EQ3,EQ1,EQ2,EQ4), normalised L[EQ2]=1")
for (e,U) in [(1,3),(1,5),(1,7),(1,9),(2,6),(2,8),(2,10),(3,9),(3,11),(4,12),(4,14),(5,15),(5,17),(6,18),(7,21)]:
    M,Mx,rhs = nextorder(e,U)
    L = Mx.T.nullspace()
    assert len(L)==1, (e,U,len(L))
    v = L[0]
    # normalise on the EQ2 entry if nonzero, else EQ3
    piv = 2 if sp.simplify(v[2])!=0 else 0
    v = sp.Matrix([sp.cancel(sp.simplify(x/v[piv])) for x in v])
    print("  e=%d U=%d  L=(EQ3:%s, EQ1:%s, EQ2:%s, EQ4:%s)   L.rhs=%s"
          %(e,U, sp.simplify(v[0]), sp.simplify(v[1]), sp.simplify(v[2]), sp.simplify(v[3]),
            sp.simplify((v.T*rhs)[0,0])))
print("time",time.time()-t0)
