#!/usr/bin/env python3
"""Graded check of (4.7) at t=3: the WEIGHTED Hilbert series of S_3/J_3^tail,
computed from the standard monomials of a Groebner basis, against the predicted
   P_3(s) = (1+s^4) [10 choose 2]_s.
The charged reports measure only the tail LENGTH; this checks the whole series.
"""
import json, itertools, sympy as sp
y,b4,u2,b3 = sp.symbols('y b4 u2 b3'); t=3; q=2*t+1; p=1009
WT={0:1,1:2,2:t+1}                       # weights of b4,u2,b3
H = 12*q**2*y**2-12*q*(t+1)*y+(t+1)*(3*t+2)
roots=[r for r in range(p) if int(sp.Poly(H,y).eval(r))%p==0]
D=json.load(open('/home/ubuntu/jc2/box/k16hsop-20260903/tail_t3_rows.json'))
T={int(k):sp.sympify(v) for k,v in D['rows'].items()}
def modp(e,yv):
    e=sp.together(sp.expand(e)); n,dd=sp.fraction(e)
    n=sp.Poly(sp.expand(n),b4,u2,b3,y); dd=sp.expand(dd)
    dn=int(sp.Poly(dd,y).eval(yv))%p if dd.has(y) else int(dd)%p
    inv=pow(dn,p-2,p); out=0
    for mo,co in zip(n.monoms(),n.coeffs()):
        co=sp.Rational(co); cc=int(co.p)%p*pow(int(co.q)%p,p-2,p)%p
        cc=cc*pow(yv,mo[3],p)%p
        out+=cc*b4**mo[0]*u2**mo[1]*b3**mo[2]
    return sp.expand(out*inv)
def pmul(a,b):
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,z in enumerate(b):
                if z: r[i+j]+=x*z
    return r
def oms(d):
    v=[0]*(d+1); v[0]=1; v[d]=-1; return v
def edivmod(a,b):
    a=a[:];
    while a and a[-1]==0: a.pop()
    q_=[0]*(max(len(a)-len(b)+1,1))
    while a and len(a)>=len(b):
        d=len(a)-len(b); c=a[-1]//b[-1]; q_[d]=c
        for i,z in enumerate(b): a[d+i]-=c*z
        while a and a[-1]==0: a.pop()
    return q_
def gauss(n,k):
    num=[1]; den=[1]
    for i in range(1,k+1): num=pmul(num,oms(n-k+i)); den=pmul(den,oms(i))
    return edivmod(num,den)
pred=pmul([1,0,0,0,1], gauss(10,2))          # (1+s^4)*[10 choose 2]_s
while pred and pred[-1]==0: pred.pop()
for yv in roots:
    G=sp.groebner([modp(T[k],yv) for k in (3,4,5)],b4,u2,b3,order='grevlex',modulus=p)
    lms=[sp.Poly(g,b4,u2,b3,modulus=p).monoms(order='grevlex')[0] for g in G.exprs]
    bnd=[min(m[i] for m in lms if all(m[j]==0 for j in range(3) if j!=i) and m[i]>0) for i in range(3)]
    ser={}
    for e in itertools.product(*[range(b) for b in bnd]):
        if not any(all(e[j]>=m[j] for j in range(3)) for m in lms):
            w=sum(e[i]*WT[i] for i in range(3)); ser[w]=ser.get(w,0)+1
    got=[ser.get(n,0) for n in range(max(ser)+1)]
    print(f"y={yv}: series == (1+s^4)[10,2]_s : {got==pred} ; length {sum(got)} ; deg {len(got)-1}")
    print(f"        {got}")
print(f"pred    {pred}   sum={sum(pred)}")
