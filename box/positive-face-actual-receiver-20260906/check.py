#!/usr/bin/env python3
"""Tiny exact polynomial controls, no CAS or receiver construction."""
from fractions import Fraction as F
import json,resource,signal,time
from pathlib import Path
resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
resource.setrlimit(resource.RLIMIT_CPU,(25,25));signal.alarm(30)
started=time.monotonic();N=4
def C(c):return {(0,)*N:F(c)} if c else {}
def var(i):return {tuple(int(j==i) for j in range(N)):F(1)}
def add(*ps):
    out={}
    for p in ps:
        for t,c in p.items():out[t]=out.get(t,F(0))+c
    return {t:c for t,c in out.items() if c}
def scale(p,c):return {t:v*F(c) for t,v in p.items() if v*F(c)}
def sub(p,q):return add(p,scale(q,-1))
def mul(*ps):
    out=C(1)
    for p in ps:
        n={}
        for t,c in out.items():
            for u,d in p.items():
                v=tuple(t[i]+u[i] for i in range(N));n[v]=n.get(v,F(0))+c*d
        out={t:c for t,c in n.items() if c}
    return out
def power(p,n):return mul(*([p]*n))
def diff(p,i=0):
    out={}
    for t,c in p.items():
        if t[i]:
            u=list(t);u[i]-=1;out[tuple(u)]=c*t[i]
    return out
def D(e,h):return sub(scale(mul(e,diff(h)),4),scale(mul(diff(e),h),5))
def subst(p,i,value):
    out={}
    for t,c in p.items():
        u=list(t);u[i]=0;u=tuple(u);out[u]=out.get(u,F(0))+c*F(value)**t[i]
    return {t:c for t,c in out.items() if c}
checks=[]
def check(ok,name):
    if not ok:raise RuntimeError(name)
    checks.append(name)
z,a,b,c=(var(i) for i in range(N));one=C(1)
zm1=sub(z,one)
h1=mul(power(z,2),power(zm1,3))
e1=scale(mul(z,zm1,add(scale(power(z,2),-25),scale(z,35),C(-7))),F(1,105))
check(scale(D(e1,h1),5)==h1,'triple-block exact Euler equation')
check(scale(D(scale(e1,-1),h1),5)!=h1,'wrong Euler sign rejected')
h2=mul(power(z,2),power(zm1,2),sub(z,a))
numerator=mul(z,zm1,sub(z,a),sub(sub(C(3),a),scale(z,5)))
denom=scale(mul(a,sub(C(3),a)),15)
residual=sub(scale(D(numerator,h2),5),mul(denom,h2))
gold=sub(sub(power(a,2),a),one)
check(residual==scale(mul(z,gold,h2),30),'double-simple golden-ratio residual exact')
check(subst(gold,1,2)!=C(0),'unforced slope a=2 fails screen')
check(subst(gold,1,0)!=C(0) and subst(gold,1,1)!=C(0) and subst(gold,1,3)!=C(0),'golden roots avoid forbidden denominators/collisions')
S=add(power(z,3),mul(a,power(z,2)),mul(b,z),c)
h3=mul(power(z,2),S)
check(D(mul(z,S),h3)==mul(h3,add(mul(a,power(z,2)),scale(mul(b,z),2),scale(c,3))),
      'three-distinct-root coefficient equation exact')
Scube=sub(power(z,3),one);hcube=mul(power(z,2),Scube);ecube=scale(mul(z,Scube),F(-1,15))
check(scale(D(ecube,hcube),5)==hcube,'cube-root face Euler-compatible')
generic=mul(zm1,sub(z,C(2)),sub(z,C(3)))
check(sub(scale(generic,3),mul(z,diff(generic)))!=C(-18),'generic three-distinct roots fail constant derivative screen')
check(scale(D(scale(ecube,F(5,3)),hcube),3)==hcube,'same slope condition for degree15 component')
# Actual polynomial monomial-J pair control in variables z=gamma,a=pi.
def bracket(p,q):return sub(mul(diff(p,0),diff(q,1)),mul(diff(p,1),diff(q,0)))
P=mul(z,a);Q=power(z,2);E=scale(mul(power(z,3),a),F(1,2))
check(bracket(P,Q)==scale(power(z,2),-2),'actual polynomial pair J=-2gamma^2')
check(bracket(E,P)==mul(power(z,2),P),'actual pair monomial Euler control')
for A,B in ((15,10),(0,25),(9,6),(0,15)):
    R=mul(power(z,A),power(a,B));E=scale(mul(power(z,3),a),F(1,3*B-A))
    check(bracket(E,R)==mul(power(z,2),R),'forced monomial endpoint '+str((A,B)))
result={'status':'PASS','checks':checks,'count':len(checks),'optimized':not __debug__,
        'elapsed_seconds':time.monotonic()-started,'source_pair_or_exclusion_claim':False}
print(json.dumps(result,sort_keys=True))
