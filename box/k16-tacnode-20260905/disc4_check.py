#!/usr/bin/env python3
"""[x^4] Disc(F0) as a function of P alone (generic P4): compare with T2 = 3b^2 P4 + 18 B w2 - 10 eta^2 and with the L-pivot."""
import sympy as sp, json
x,b,B,eta,w2,P4,l2 = sp.symbols('x b B eta w2 P4 l2')
K=4; C=sp.cancel
def S(d): return {i: C(v) for i,v in d.items() if i<=K and v!=0}
def add(*ds):
    r={}
    for d in ds:
        for i,v in d.items(): r[i]=r.get(i,0)+v
    return S(r)
def scal(c,d): return S({i:c*v for i,v in d.items()})
def mul(d1,d2):
    r={}
    for i,u in d1.items():
        for j,v in d2.items():
            if i+j<=K: r[i+j]=r.get(i+j,0)+u*v
    return S(r)
def coeff(d,i): return C(d.get(i,0))
xs={1:sp.Integer(1)}
P={0:-b**2/4,1:-B,2:eta,3:w2,4:P4}; Pd=S(P); P2=mul(Pd,Pd)
def th3(d): return S({i:(i-3)*v for i,v in d.items()})
c3={0:2*b}; c2=add(scal(-4*B,xs),scal(-8,Pd)); c1=add(scal(-sp.Rational(8,3)*eta*b,{2:1}),scal(-8*b,Pd))
c0=scal(sp.Rational(16,3),add(scal(B,mul(xs,Pd)),scal(-eta*B,{3:1}),scal(-1,th3(P2))))
s={0:2*b}; p={0:b**2}; s1={0:sp.Integer(0)}; p1={0:b**2}
M=sp.Matrix([[1,0,1,0],[0,1,2*b,1],[b**2,0,b**2,2*b],[0,b**2,0,b**2]]); Mi=M.inv()
for n in range(1,K+1):
    sd,pd_,s1d,p1d=S(s),S(p),S(s1),S(p1)
    e=[coeff(add(sd,s1d),n)-coeff(c3,n), coeff(add(pd_,p1d,mul(sd,s1d)),n)-coeff(c2,n), coeff(add(mul(sd,p1d),mul(s1d,pd_)),n)-coeff(c1,n), coeff(mul(pd_,p1d),n)-coeff(c0,n)]
    sol=Mi*sp.Matrix([-v for v in e]); s[n],p[n],s1[n],p1[n]=[C(v) for v in sol]
sd,pd_=S(s),S(p)
disc4=coeff(add(mul(sd,sd),scal(-4,pd_)),4)
T2=3*b**2*P4+18*B*w2-10*eta**2
out={'s':{i:str(sp.factor(s[i])) for i in s}, 'p':{i:str(sp.factor(p[i])) for i in p},
     'disc4':str(sp.factor(disc4)), 'disc4_over_T2':str(sp.factor(C(disc4/T2)))}
Phi4=(2/b**2)*(eta**2-3*B*w2-b*eta*l2-sp.Rational(3,8)*b**2*l2**2)
out['disc4_on_solution_over_Lpivot2']=str(sp.factor(C(disc4.subs(P4,Phi4)/(4*eta+3*b*l2)**2)))
out['T2_on_solution_over_Lpivot2']=str(sp.factor(C(T2.subs(P4,Phi4)/(4*eta+3*b*l2)**2)))
json.dump(out,open('box/k16-tacnode-20260905/disc4_check.json','w'),indent=1)
for k,v in out.items(): print(k,'=',v)
