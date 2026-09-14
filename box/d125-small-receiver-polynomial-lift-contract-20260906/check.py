#!/usr/bin/env python3
"""Tiny exact inverse-map and selected-row checks; no full source expansion."""
from fractions import Fraction as F
from math import factorial
import json
import sys

N=5
def mon(e,c=1): return {tuple(e):F(c)} if c else {}
def var(k,e=1):
    a=[0]*N; a[k]=e; return mon(a)
one=mon([0]*N); x=var(0); y=var(1); l2=var(2); l3=var(3); rho=var(4)
def req(ok,msg):
    if not ok: raise ValueError(msg)
def add(*ps):
    out={}
    for p in ps:
        for e,c in p.items(): out[e]=out.get(e,F(0))+c
    return {e:c for e,c in out.items() if c}
def sc(p,c): return {e:c*d for e,d in p.items() if c*d}
def mul(p,q):
    out={}
    for e,c in p.items():
        for f,d in q.items():
            z=tuple(a+b for a,b in zip(e,f)); out[z]=out.get(z,F(0))+c*d
    return {e:c for e,c in out.items() if c}
def pw(p,n):
    out=one
    for _ in range(n): out=mul(out,p)
    return out
def der(p,k):
    out={}
    for e,c in p.items():
        if e[k]:
            z=list(e); z[k]-=1; out[tuple(z)]=e[k]*c
    return out
def jac(p,q): return add(mul(der(p,0),der(q,1)),sc(mul(der(p,1),der(q,0)),-1))
def red(p):
    out={}
    for e,c in p.items():
        a,b=F(1),F(0)
        for _ in range(e[4]): a,b=-b,a+3*b
        f=list(e); f[4]=0; h=list(e); h[4]=1
        out=add(out,mon(f,c*a),mon(h,c*b))
    return out
def zero_lambdas(p): return {e:c for e,c in p.items() if e[2]==e[3]==0}

U=add(mul(var(0,4),y),mul(l2,var(0,2)),mul(l3,var(0,3)),var(0,5))
V=var(0,-1)
G=var(1,-1)
PI=add(mul(var(1,4),x),sc(mul(l2,var(1,2)),-1),sc(mul(l3,y),-1),sc(var(1,-1),-1))
def forward(p):
    out={}
    for (t,r,b,d,a),c in p.items():
        out=add(out,mul(pw(U,t),mon([-r,0,b,d,a],c)))
    return out
def inverse(p,L2=l2,L3=l3):
    pi=add(mul(var(1,4),x),sc(mul(L2,var(1,2)),-1),sc(mul(L3,y),-1),sc(var(1,-1),-1))
    out={}
    for (i,j,b,d,a),c in p.items():
        out=add(out,mul(pw(pi,j),mon([0,-i,b,d,a],c)))
    return out
req(jac(U,V)==var(0,2),"forward coordinate sign")
req(jac(G,PI)==var(1,2),"inverse coordinate sign")
req(inverse(U)==x and inverse(V)==y,"inverse after forward coordinates")
req(forward(G)==x and forward(PI)==y,"forward after inverse coordinates")
req(inverse(pw(U,2))==pw(x,2),"positive polynomiality fixture")

# Real omission: exactly one negative coefficient, with the full receiver J condition.
A=x; B=add(mul(var(0,2),y),var(0,3))
P=zero_lambdas(inverse(A)); Q=zero_lambdas(inverse(B))
req(jac(A,B)==var(0,2),"omission fixture receiver bracket")
req(P==var(1,-1) and Q==mul(var(1,2),x),"omission fixture inverse")
req(jac(P,Q)==one,"omission fixture Laurent Keller bracket")
def accept_negative(p,q,omitted=frozenset()):
    for who,poly in [("P",p),("Q",q)]:
        for e,c in poly.items():
            if e[1]<0 and c and (who,e[0],e[1]) not in omitted: return False
    return True
req(not accept_negative(P,Q),"complete rows reject nonpolynomial inverse")
req(accept_negative(P,Q,{("P",0,-1)}),"actual missing-row acceptance control")

# A selected coefficient, computed by multinomial arithmetic only.
def row(poly,t,e):
    out={}
    for (i,j,bl,dl,a),c in poly.items():
        if j<t: continue
        for b in range(j-t+1):
            for d in range(j-t-b+1):
                z=j-t-b-d
                if 5*t+3*b+2*d-i-j!=e: continue
                coeff=c*F(factorial(j),factorial(t)*factorial(b)*factorial(d)*factorial(z))*(-1)**(j-t)
                out=add(out,mon([0,0,bl+b,dl+d,a],coeff))
    return red(out)
def bd(poly,k,r):
    out={}
    for (i,j,b,d,a),c in poly.items():
        if i+j==15-k and j>=r:
            out=add(out,mon([0,0,b,d,a],c*F(factorial(j),factorial(j-r))*(-1)**(j-r)))
    return red(out)
H0=mul(var(1,2),add(var(1,3),var(0,3)))
Hg=mul(var(1,2),mul(add(y,x),pw(add(y,mul(add(one,sc(rho,-1)),x)),2)))
for H,D in [(H0,sc(one,162)),(Hg,sc(red(pw(rho,6)),6))]:
    af=add(red(pw(H,3)),mon([10,4,0,0,0],7),mon([10,3,0,0,0],11),mon([10,2,0,0,0],13))
    req(bd(af,0,3)==D,"constant D")
    req(not bd(af,0,2),"outer second derivative zero")
    req(row(af,2,-5)=={},"automatic top negative row")
    req(row(af,2,-4)==sc(bd(af,1,2),F(1,2)),"u2v-4")
    req(row(af,2,-3)==red(sc(add(bd(af,2,2),sc(mul(l3,D),-1)),F(1,2))),"lambda3 pivot sign")
    req(row(af,2,-2)==red(sc(add(bd(af,3,2),sc(mul(l3,bd(af,1,3)),-1),sc(mul(l2,D),-1)),F(1,2))),"lambda2 pivot sign")
req(red(mul(rho,add(sc(one,3),sc(rho,-1))))==one,"rho inverse fixed field unit")

polys={"unequal":{"P":[(0,0),(0,15),(9,6),(2,1)],"Q":[(0,0),(0,25),(15,10),(1,0)]},"common3":{"P":[(0,0),(0,15),(9,6),(3,0)],"Q":[(0,0),(0,25),(15,10),(5,0)]},"common4":{"P":[(0,0),(0,15),(9,6),(9,0)],"Q":[(0,0),(0,25),(15,10),(15,0)]}}
def points(poly):
    ed=list(zip(poly,poly[1:]+poly[:1]))
    for i in range(max(a for a,b in poly)+1):
        for j in range(max(b for a,b in poly)+1):
            cs=[(c-a)*(j-b)-(d-b)*(i-a) for (a,b),(c,d) in ed]
            if all(z>=0 for z in cs) or all(z<=0 for z in cs): yield i,j
counts={}; maxlambda={}
for name,pair in polys.items():
    counts[name]=[]
    for who,D in [("P",15),("Q",25)]:
        slots=set(); md=0
        for i,j in points(pair[who]):
            for t in range(j+1):
                for b in range(j-t+1):
                    for d in range(j-t-b+1):
                        e=5*t+3*b+2*d-i-j
                        req(t+e<=5*D and e<=4*D and 5*t-e<=D,"degree and weight bounds")
                        if e<0: slots.add((t,e)); md=max(md,b+d)
        expected={(t,e) for t in range((D-1)//5+1) for e in range(5*t-D,0)}
        req(slots==expected,"complete negative row support")
        req((D,4*D) not in slots,"monic positive leader")
        counts[name].append(len(slots)); maxlambda[who]=md
req(all(v==[30,75] for v in counts.values()),"105 uniform slots")
req(maxlambda=={"P":7,"Q":12},"lambda degree bound")
# Monicity yields the unique endpoint: enumerate possible top-contributing choices.
for D in [15,25]:
    choices=[(i,j) for i in range(D+1) for j in range(D-i+1) if j>=D and i+j<=D]
    req(choices==[(0,D)],"unique source top coefficient")

# Source/receiver scaling covariance, with both lift parameters retained.
tau=F(2); D=15
src=add(mon([2,3,0,0,0],3),mon([1,0,0,0,0],5))
rec=forward(src)
rec_tau={e:c*tau**(e[0]+e[1]-D) for e,c in rec.items()}
got=inverse(rec_tau,sc(l2,tau**-3),sc(l3,tau**-2))
want={e:c*tau**(5*e[0]-e[1]-D) for e,c in src.items()}
req(got==want,"lift parameter scaling covariance")
if "--mutate-sign" in sys.argv:
    req(jac(G,PI)==sc(var(1,2),-1),"injected inverse Jacobian sign")
if "--mutate-pivot" in sys.argv:
    req(row(af,2,-3)==red(sc(add(bd(af,2,2),mul(l3,bd(af,0,3))),F(1,2))),"injected pivot sign")
print(json.dumps({"status":"PASS","negative_slots":counts,"total":105,"max_lambda_degree":maxlambda,"real_omission_accepted_by_weaker_test":True,"no_full_source_expansion":True},sort_keys=True))
