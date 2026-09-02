import sympy as sp, time
from wall2 import *
t0=time.time()
UNK=[A1,S1,Q1,R1,C1g]
def ray_sub(e): return {C:-b*(1+2*e)*A**2, R:S**2/(4*b*A**2), Q:3*a*S**2/(4*b**2*A)}
def nextorder(e,U,K=2):
    M=model(e,U,K=K); E=equations(M); sub=ray_sub(e); rows=[]; rhs=[]
    for which in ['EQ3','EQ1','EQ2','EQ4']:
        t=tops(M)[which]
        c1=sp.expand(sp.cancel(zc(E[which],t-1).subs(sub)))
        row=[sp.cancel(sp.diff(c1,v)) for v in UNK]
        rest=sp.cancel(sp.expand(c1-sum(row[i]*UNK[i] for i in range(5))))
        rows.append(row); rhs.append(rest)
    return M, sp.Matrix(rows), sp.Matrix(rhs)

ehat = 4*b*sp.Symbol('e_')*A*A1 + C1g   # placeholder replaced per cell
bad=[]
print("cell     n   rk(M) rk(EQ1,EQ2,EQ4)  ker<= {ehat=0}?  rest_EQ3   consistent?")
for e in range(1,13):
    for U in range(3*e, 3*e+11, 2):
        M,Mx,rhs = nextorder(e,U); n=M['n']
        r_all = Mx.rank(); r_124 = Mx[1:,:].rank()
        ker = Mx.nullspace()
        eh = [sp.simplify((4*b*e*A*v[0] + v[4])) for v in ker]
        ok_eh = all(x==0 for x in eh)
        cons = (Mx.row_join(rhs).rank() == r_all)
        exp_rest = -3*(32*e**3+32*e**2+6*e+1)*a*b*A**6 if U==3*e else 0
        ok_rest = sp.simplify(rhs[0]-exp_rest)==0 and all(sp.simplify(rhs[i])==0 for i in (1,2,3))
        if not(ok_eh and ok_rest): bad.append((e,U))
        if U<=3*e+4:
            print("(%d,%2d)  %2d    %d       %d              %s            %s        %s"
                  %(e,U,n,r_all,r_124,ok_eh,("-3(32e^3+32e^2+6e+1)abA^6" if U==3*e else "0") if ok_rest else "MISMATCH", cons))
print("anomalies:",bad)
print("time",time.time()-t0)
