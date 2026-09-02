import sympy as sp, time
from wall2 import *
t0=time.time()
be, de = sp.symbols('beta delta')
e,U = 1,3
M=model(e,U,K=3); n=M['n']
Rv,Qv = S**2/(4*b*A**2), 3*a*S**2/(4*b**2*A)
al = be - de/2; ga = be + de/2; ep = -4*e*al
sub = {C:-b*(1+2*e)*A**2, R:Rv, Q:Qv, A1: al*A, S1: be*S, Q1: ga*Qv, R1: de*Rv, C1g: ep*b*A**2}
E=equations(M); UNK2=[S2,Q2,R2,C2g]
rows=[];rhs=[]
for which in ['EQ3','EQ1','EQ2','EQ4']:
    c2=sp.expand(sp.cancel(zc(E[which],tops(M)[which]-2).subs(sub)))
    row=[sp.cancel(sp.diff(c2,v)) for v in UNK2]
    rest=sp.cancel(sp.expand(c2-sum(row[i]*UNK2[i] for i in range(4))))
    rows.append(row); rhs.append(-rest)
Mx=sp.Matrix(rows); rr=sp.Matrix(rhs)
print("rank M2 =",Mx.rank())
L = Mx.T.nullspace()
print("dim coker =",len(L))
for v in L:
    v = sp.Matrix([sp.cancel(sp.simplify(x)) for x in v])
    cond = sp.factor(sp.simplify((v.T*rr)[0,0]))
    print("  L =",[sp.simplify(x) for x in v.T])
    print("  consistency condition  L.rhs = 0  :")
    print("   ", cond)
    num = sp.numer(sp.together(cond))
    print("   numerator factored:", sp.factor(sp.expand(num)))
    print("   as poly in (beta,delta):", sp.Poly(sp.expand(sp.numer(sp.together(cond))), be, de).as_dict())
print("time",time.time()-t0)
