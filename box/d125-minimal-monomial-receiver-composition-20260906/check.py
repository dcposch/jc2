#!/usr/bin/env python3
"""Exact map/face/support controls only. No source ideal or classifier."""
from fractions import Fraction as F
from math import gcd
import json
import sys

def req(ok, why):
    if not ok: raise ValueError(why)
def add(*ps):
    out={}
    for p in ps:
        for e,c in p.items(): out[e]=out.get(e,F(0))+c
    return {e:c for e,c in out.items() if c}
def sc(p,c): return {e:c*v for e,v in p.items() if c*v}
def mul(p,q):
    out={}
    for e,c in p.items():
        for f,d in q.items():
            z=tuple(a+b for a,b in zip(e,f)); out[z]=out.get(z,F(0))+c*d
    return {e:c for e,c in out.items() if c}
def pw(p,n):
    out={(0,0,0):F(1)}
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
    for (i,j,k),c in p.items():
        a,b=F(1),F(0)
        for _ in range(k): a,b=-b,a+3*b
        out=add(out,{(i,j,0):c*a,(i,j,1):c*b})
    return out
def S(p): return {(i-j,j,k):c for (i,j,k),c in p.items()}
def Sinv(p): return {(i+j,j,k):c for (i,j,k),c in p.items()}
def T(p,n): return {(-i+n*j,j,k):c for (i,j,k),c in p.items()}
one={(0,0,0):F(1)}; g={(1,0,0):F(1)}; p={(0,1,0):F(1)}; a={(0,0,1):F(1)}

# Coordinate Jacobians, all signs and complete-row exponent shift.
req(jac(g,{(-1,1,0):F(1)})=={(-1,0,0):F(1)},"Jac S=gamma^-1")
req(jac({(-1,0,0):F(1)},{(4,1,0):F(1)})=={(2,0,0):F(-1)},"Jac T4=-gamma²")
fixture={(15,15,0):F(2),(15,6,0):F(3),(3,1,0):F(5),(0,0,0):F(7)}
other={(25,25,0):F(11),(25,10,0):F(13),(1,0,0):F(17)}
req(Sinv(S(fixture))==fixture,"S inverse")
req(jac(S(fixture),S(other))==mul({(-1,0,0):F(1)},S(jac(fixture,other))),"full finite-fixture chain rule")
for i,j in [(0,0),(60,15),(15,6),(2,1),(-15,0),(100,25)]:
    q={(i,j,0):F(1)}
    req(S(T(q,5))==T(q,4),"T4=S o T5")
for i in range(7):
    for j in range(i+1):
        for k in range(7):
            for l in range(k+1):
                det=i*l-j*k
                if det: req(i+k-j-l>=1,"no negative transported Jacobian row")

# Initial root cut, transported literally through T4; auxiliary a is algebraic.
y=mul(pw(g,4),add(p,g)); z=mul({(-1,0,0):F(1)},add(p,g))
def face(h): return red(mul(y,mul(pw(add(z,sc(one,-1)),2),h)))
sq=face(add(pw(z,2),sc(z,-3),sc(one,3)))
gold=face(pw(add(z,sc(a,-1)),2))
H0=mul(pw(p,2),add(pw(p,3),pw(g,3)))
Hg=mul(pw(p,2),mul(add(p,g),pw(add(p,mul(add(one,sc(a,-1)),g)),2)))
expanded=mul(pw(p,2),add(pw(p,3),mul(add(sc(one,3),sc(a,-2)),mul(g,pw(p,2))),mul(add(sc(one,2),sc(a,-1)),mul(pw(g,2),p)),mul(a,pw(g,3))))
req(sq==H0,"squarefree literal transported face")
req(gold==red(Hg)==red(expanded),"golden literal transported face")
req(all(i>=0 and j>=0 and i+j==5 for i,j,k in gold),"homogeneous polynomial primitive face")
req(bool(red(add(gold,sc(H0,-1)))),"distinct golden/squarefree face")

# Literal inner-face equations, tested by full differentiation at nonzero values.
# A=a0*g²*p+b0*g9*p6, B=c0*g+d0*g8*p5+e0*g15*p10.
a0,b0,c0,d0,e0=map(F,[2,3,5,7,11])
aa={(2,1,0):a0,(9,6,0):b0}; bb={(1,0,0):c0,(8,5,0):d0,(15,10,0):e0}
want={(2,0,0):-a0*c0,(9,5,0):2*a0*d0-6*b0*c0,(16,10,0):5*a0*e0-3*b0*d0}
req(jac(aa,bb)=={e:c for e,c in want.items() if c},"unequal terminal coefficient equations")
mu=F(2)
req(T({(-1,0,0):mu**2,(2,1,0):-2*mu,(5,2,0):F(1)},4)==mul(g,pw(add(mul(g,p),sc(one,-mu)),2)),"common3 primitive transport")
req(T({(-3,0,0):mu**2,(1,1,0):-2*mu,(5,2,0):F(1)},4)==mul(pw(g,3),pw(add(p,sc(one,-mu)),2)),"common4 primitive transport")

cases={
"unequal":{"P":[(0,0),(0,15),(9,6),(2,1)],"Q":[(0,0),(0,25),(15,10),(1,0)]},
"common_3":{"P":[(0,0),(0,15),(9,6),(3,0)],"Q":[(0,0),(0,25),(15,10),(5,0)]},
"common_4":{"P":[(0,0),(0,15),(9,6),(9,0)],"Q":[(0,0),(0,25),(15,10),(15,0)]}}
expected={"unequal":[83,215],"common_3":[94,241],"common_4":[115,296]}
def count(poly):
    pairs=list(zip(poly,poly[1:]+poly[:1]))
    area2=abs(sum(x*v-y*u for (x,y),(u,v) in pairs))
    bd=sum(gcd(abs(x-u),abs(y-v)) for (x,y),(u,v) in pairs)
    n=0
    for x in range(max(v[0] for v in poly)+1):
        for y in range(max(v[1] for v in poly)+1):
            cr=[(u-a)*(y-b)-(v-b)*(x-a) for (a,b),(u,v) in pairs]
            if all(t>=0 for t in cr) or all(t<=0 for t in cr): n+=1
    req(2*n==area2+bd+2,"Pick versus literal lattice count")
    return n
counts={k:[count(v["P"]),count(v["Q"])] for k,v in cases.items()}
req(counts==expected,"six support counts")

# Simultaneous source scaling plus degree renormalization: -15-25+2+2=-36.
scale=F(2); c=F(7)
req(scale**(-15-25)*scale**2*c*scale**2==c*scale**(-36),"Jacobian scalar scaling")
def diag(q,k): return {e:v*scale**(e[0]+e[1]-k) for e,v in q.items()}
req(diag(H0,5)==H0 and diag(gold,5)==gold,"primitive slopes unchanged")
G3=mul(g,pw(add(mul(g,p),sc(one,-mu)),2))
G4=mul(pw(g,3),pw(add(p,sc(one,-mu)),2))
req(diag(G3,5)==mul(g,pw(add(mul(g,p),sc(one,-mu/scale**2)),2)),"common3 parameter scaling")
req(diag(G4,5)==mul(pw(g,3),pw(add(p,sc(one,-mu/scale)),2)),"common4 parameter scaling")
aterm={(2,1,0):F(3),(9,6,0):F(1)}
bterm={(1,0,0):F(5),(8,5,0):F(5),(15,10,0):F(1)}
req(jac(aterm,bterm)=={(2,0,0):F(-15)},"monic-corner terminal scalar relation")
req(jac(diag(aterm,15),diag(bterm,25))=={(2,0,0):F(-15)*scale**-36},"full terminal scaling check")
# A monomial-J receiver is not automatically a polynomial source before T4.
req(jac(g,{(2,1,0):F(1)})=={(2,0,0):F(1)},"negative lift example")
req(any(i<0 for i,j,k in T(g,4)),"negative lift retained")
if "--mutate" in sys.argv:
    req(S(T({(2,1,0):F(1)},5))==T({(2,1,0):F(1)},3),"injected wrong map exponent")
if "--mutate-face" in sys.argv:
    req(gold==red(add(expanded,{(3,2,0):F(1)})),"injected wrong golden coefficient")
print(json.dumps({"status":"PASS","counts":counts,"totals":{k:sum(v) for k,v in counts.items()},"scope":"tiny exact controls only","no_CAS_builder_solver":True},sort_keys=True))
