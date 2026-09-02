import sympy as sp, time
from wall2 import *
t0=time.time()
al,be,ga,de,ep = sp.symbols('alpha beta gamma delta epsilonhat')  # A1/A, S1/S, Q1/Q, R1/R, C1g/(b A^2)
def ray_sub(e): return {C:-b*(1+2*e)*A**2, R:S**2/(4*b*A**2), Q:3*a*S**2/(4*b**2*A)}
def rows_norm(e,U):
    M=model(e,U,K=2); E=equations(M); sub=ray_sub(e)
    Rv, Qv = S**2/(4*b*A**2), 3*a*S**2/(4*b**2*A)
    dim = {A1: al*A, S1: be*S, Q1: ga*Qv, R1: de*Rv, C1g: ep*b*A**2}
    out=[]
    for which in ['EQ3','EQ1','EQ2','EQ4']:
        t=tops(M)[which]
        c1=sp.expand(sp.cancel(zc(E[which],t-1).subs(sub).subs(dim)))
        c1=sp.cancel(sp.expand(c1))
        # pull out a common factor: use the delta-coefficient as the normaliser when nonzero
        cf=[sp.cancel(sp.diff(c1,v)) for v in (al,be,ga,de,ep)]
        rest=sp.cancel(sp.expand(c1-sum(cf[i]*[al,be,ga,de,ep][i] for i in range(5))))
        piv=next(x for x in cf if x!=0)
        out.append(([sp.cancel(sp.simplify(x/piv)) for x in cf], sp.cancel(sp.simplify(rest/piv))))
    return M,out
for (e,U) in [(1,3),(1,5),(1,7),(1,9),(2,6),(2,8),(2,10),(3,9),(3,11),(3,13),(4,12),(4,14),(5,15),(5,17)]:
    M,out=rows_norm(e,U); n=M['n']
    print("e=%d U=%d n=%d"%(e,U,n))
    for nm,(cf,rst) in zip(['EQ3','EQ1','EQ2','EQ4'],out):
        print("   %s  [a,b,g,d,eh] = %s   rest=%s"%(nm,cf,rst))
print("time",time.time()-t0)
