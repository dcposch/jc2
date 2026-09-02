import sympy as sp
from wall2 import *
al,be,ga,de,ep=sp.symbols('alpha beta gamma delta epsilonhat')
def check(e,U):
    M=model(e,U,K=2);E=equations(M);n=M['n']
    sub={C:-b*(1+2*e)*A**2, R:S**2/(4*b*A**2), Q:3*a*S**2/(4*b**2*A)}
    Rv,Qv=S**2/(4*b*A**2),3*a*S**2/(4*b**2*A)
    dim={A1:al*A,S1:be*S,Q1:ga*Qv,R1:de*Rv,C1g:ep*b*A**2}
    out={}
    for w in ['EQ3','EQ1','EQ4']:
        c1=sp.expand(sp.cancel(zc(E[w],tops(M)[w]-1).subs(sub).subs(dim)))
        out[w]=sp.cancel(sp.simplify(c1))
    rho=(32*e**3+32*e**2+6*e+1)*b**2*A**4/((4*e-2)*S**2) if U==3*e else 0
    # hand-derived normal forms, written as  LHS = 0
    H3=(be-ga+de/2-rho); H1=(al-be+de/2); H4=(n*al-2*be-(n-2)*ga+(n-1)*de)
    r=[sp.cancel(sp.simplify(out['EQ3']/H3)), sp.cancel(sp.simplify(out['EQ1']/H1)),
       sp.cancel(sp.simplify(out['EQ4']/H4))]
    print("  (e,U)=(%d,%2d) n=%2d  EQ3/(N3)=%s  EQ1/(N1)=%s  EQ4/(N4)=%s"%(e,U,n,
        sp.factor(r[0]),sp.factor(r[1]),sp.factor(r[2])))
print("hand-derived (N1),(N3),(N4) vs CAS  [ratio must be a nonzero factor free of alpha..epsilonhat ]")
for c in [(1,3),(1,5),(1,7),(2,6),(2,8),(3,9),(3,11),(4,12),(5,15),(6,18)]: check(*c)
