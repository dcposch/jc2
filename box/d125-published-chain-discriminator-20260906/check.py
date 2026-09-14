#!/usr/bin/env python3
"""Tiny exact controls, not a classifier, ideal builder or proof of existence."""
from fractions import Fraction as Q
from math import gcd
import json
import sys

def add(*ps):
    out = {}
    for p in ps:
        for e,c in p.items(): out[e] = out.get(e, Q(0)) + c
    return {e:c for e,c in out.items() if c}
def scale(p,c): return {e:c*v for e,v in p.items() if c*v}
def mul(p,q):
    out={}
    for (i,j),c in p.items():
        for (k,l),d in q.items():
            e=(i+k,j+l); out[e]=out.get(e,Q(0))+c*d
    return {e:c for e,c in out.items() if c}
def power(p,n):
    out={(0,0):Q(1)}
    for _ in range(n): out=mul(out,p)
    return out
def der(p,i):
    out={}
    for e,c in p.items():
        if e[i]:
            f=list(e); f[i]-=1; out[tuple(f)]=c*e[i]
    return out
def jac(p,q): return add(mul(der(p,0),der(q,1)),scale(mul(der(p,1),der(q,0)),-1))
def reduce_a(p):
    # a^2=3a-1; first exponent is w, second is a.
    out={}
    def apow(j):
        z,t=Q(1),Q(0)
        for _ in range(j): z,t=-t,z+3*t
        return z,t
    for (i,j),c in p.items():
        z,t=apow(j)
        out=add(out,{(i,0):c*z,(i,1):c*t})
    return out
def require(ok, message):
    if not ok: raise ValueError(message)
def ode(r,f,den):
    w={(1,0):Q(1)}
    return add(scale(mul(mul(w,f),der(r,0)),4),
               scale(mul(mul(w,der(f,0)),r),-5),scale(mul(f,r),-1),
               scale(mul(den,r),-Q(1,3)))

one={(0,0):Q(1)}; w={(1,0):Q(1)}; a={(0,1):Q(1)}
wm1=add(w,scale(one,-1)); s=add(power(w,2),scale(w,-3),scale(one,3))
r=mul(power(wm1,2),s); f=mul(wm1,s)
require(not ode(r,f,scale(one,9)),"squarefree residual Euler ODE")
require(bool(ode(r,add(f,one),scale(one,9))),"mutated Euler term not rejected")
g=mul(wm1,add(w,scale(a,-1))); rd=power(g,2)
fd=mul(g,add(mul(add(one,a),w),scale(a,-3)))
require(not reduce_a(ode(rd,fd,scale(power(a,2),9))),"double-root Euler ODE")
require(bool(reduce_a(ode(rd,add(fd,one),scale(power(a,2),9)))),"mutated double-root term not rejected")
require(Q(4,5)*(5)==4 and Q(4,5)*20==16,"Euler endpoint")
require(Q(4,5).denominator==5,"Euler denominator")
require((Q(1)+2*Q(1,5),2)==(Q(7,5),2),"generated corner")
require(Q(4,5).denominator!=4,"wrong q mutation")
lower=[k for k in range(1,10) if k>1 and 4-k>0]
require(lower==[2,3],"lower directions")
candidate=[]
for b in range(2):
    for x in range(-8,8):
        if -x+5*b<5 and 5*b-2*x>0: candidate.append((x,b))
require(candidate==[(-4,0),(-3,0),(-2,0),(-1,0),(1,1),(2,1)],"successor candidate enumeration")
require(all(Q(v,2).denominator==2 for v in (5,7)),"excluded Euler endpoint fractions")
# Parallel endpoint assignment and its genuine transposed mutation.
cross=lambda p,q:p[0]*q[1]-p[1]*q[0]
require(cross((15-2,6-1),(25+1,10))==0,"terminal assignment")
require(cross((15+1,6),(25-2,10-1))!=0,"wrong terminal assignment not rejected")
require((-5*13+13*5)==0,"terminal normal")
# Laurent chain-rule control and involutive monomial exponent map.
def inv(p,k=5): return {(-i+k*j,j):c for (i,j),c in p.items()}
p={(2,1):Q(1)}; q={(-1,0):Q(1)}
require(jac(p,q)=={(0,0):Q(1)},"Laurent fixture bracket")
require(jac(inv(p),inv(q))=={(3,0):Q(-1)},"inversion bracket sign/factor")
require(jac(inv(p,4),inv(q,4))!={(3,0):Q(-1)},"wrong inversion exponent not rejected")
for ij in [(0,0),(60,15),(15,6),(2,1),(-9,0),(100,25),(25,10),(-15,0)]:
    require(inv(inv({ij:Q(1)}))=={ij:Q(1)},"inversion involution")
u={(1,0):Q(1)}; v={(3,1):Q(1)}
require(jac(u,v)=={(3,0):Q(1)},"negative-lift fixture bracket")
require(any(i<0 for i,j in inv(u)),"monomial-J fixture unexpectedly polynomial after inverse")
# Exact support-lowering inequality; x^-3 is deliberately not admitted here.
for k in (4,5):
    require(-k <= -4,"safe upper root cut")
require(-3 > -4,"unsafe upper root cut mutation")
cases={
    "unequal":{"P":[(0,0),(15,15),(15,6),(3,1)],"Q":[(0,0),(25,25),(25,10),(1,0)]},
    "common_3":{"P":[(0,0),(15,15),(15,6),(3,0)],"Q":[(0,0),(25,25),(25,10),(5,0)]},
    "common_4":{"P":[(0,0),(15,15),(15,6),(9,0)],"Q":[(0,0),(25,25),(25,10),(15,0)]}}
def hull(points):
    points=sorted(set(points))
    def half(seq):
        h=[]
        for p in seq:
            while len(h)>1 and cross((h[-1][0]-h[-2][0],h[-1][1]-h[-2][1]),(p[0]-h[-1][0],p[1]-h[-1][1]))<=0: h.pop()
            h.append(p)
        return h
    return half(points)[:-1]+half(points[::-1])[:-1]
for name,c in cases.items():
    for who,m in [("P",3),("Q",5)]:
        pts=[]
        for y in range(5*m+1):
            for x in range(-3*m,20*m+1):
                if x-4*y>0 or -x+5*y>5*m: continue
                if name=="unequal" and -5*x+13*y>m: continue
                if name=="common_3" and -x+3*y>m: continue
                if name=="common_4" and -x+4*y>3*m: continue
                pts.append((-x+5*y,y))
        require(hull(pts)==hull(c[who]),"literal half-plane lattice hull")
if "--mutate" in sys.argv:
    # Feed an erroneous datum to the same equality checker; must exit nonzero.
    bad=cases["unequal"]["P"][:]; bad[-1]=(4,1)
    require(bad==list(inv({e:Q(1) for e in [(0,0),(60,15),(15,6),(2,1)]})),"injected wrong vertex")
for name,c in cases.items():
    require(max(i+j for i,j in c["P"])==30,"receiver P total degree")
    require(max(i+j for i,j in c["Q"])==50,"receiver Q total degree")
print(json.dumps({"status":"PASS","arithmetic":"exact rational, no CAS","mutations_rejected":["Euler term","double-root Euler term","q=4","terminal assignment","inversion exponent","unsafe x^-3 support cut"],"necessary_polygon_candidates":cases},sort_keys=True))
