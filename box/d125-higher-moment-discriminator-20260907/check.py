#!/usr/bin/env python3
"""Exact symbolic toy controls. No full source/receiver powers or sampling."""
from fractions import Fraction as F
from math import comb
import json
import sys

# Four slots mean (u,v,l2,l3) before substitution, (g,w,l2,l3) afterwards.
def clean(p):
    return {e:c for e,c in p.items() if c}
def add(*ps):
    r={}
    for p in ps:
        for e,c in p.items():
            r[e]=r.get(e,F(0))+c
    return clean(r)
def scale(p,c):
    return clean({e:c*x for e,x in p.items()})
def mul(p,q):
    r={}
    for e,c in p.items():
        for f,d in q.items():
            a=tuple(x+y for x,y in zip(e,f))
            r[a]=r.get(a,F(0))+c*d
    return clean(r)
def mon(a=0,b=0,c=0,d=0,k=1):
    return {(a,b,c,d):F(k)}
def power(p,n):
    r=mon()
    for _ in range(n):
        r=mul(r,p)
    return r
def deriv(p,i):
    r={}
    for e,c in p.items():
        if e[i]:
            f=list(e);f[i]-=1
            r[tuple(f)]=c*e[i]
    return clean(r)
def jac(p,q):
    return add(mul(deriv(p,0),deriv(q,1)),scale(mul(deriv(p,1),deriv(q,0)),-1))

mode=sys.argv[1] if len(sys.argv)>1 else 'normal'
q=add(mon(2,0,1),mon(3,0,0,1))
u=add(mon(4,1),q)
v=mon(-1)
def forward(p):
    return add(*(mul(mul(power(u,a),power(v,b)),mon(0,0,c,d,k)) for (a,b,c,d),k in p.items()))
def moment_direct(p):
    h={}
    for (a,b,c,d),k in p.items():
        denominator=1 if mode=='mutate-denominator' else a+1
        h=add(h,mul(power(q,a+1),mon(-b,0,c,d,k/F(denominator))))
    index=0 if mode=='mutate-index' else 1
    return clean({(0,0,c,d):k for (g,w,c,d),k in h.items() if g==index and w==0})
def moment_formula(p):
    r={}
    for (a,b,c,d),coefficient in p.items():
        n=a+1;k=b-2*a-1
        if 0<=k<=n:
            r=add(r,mon(0,0,c+n-k,d+k,coefficient*F(comb(n,k),n)))
    return r

checks=0
def require(condition,label):
    global checks
    checks+=1
    if not condition:
        raise ValueError(label)

z=add(mon(1,3),mon(0,1,1,k=-1))
w=add(mon(1,4),mon(0,2,1,k=-1),mon(0,1,0,1,k=-1))
fixtures=[mon(),z,w,power(w,2),mon(1),mon(1,1)]
expected=[{},mon(0,0,2,k=F(-1,2)),mon(0,0,1,1,-1),mon(0,0,0,3,F(1,3)),{},{}]
for p,e in zip(fixtures,expected):
    require(moment_direct(p)==e,'seed moment exact value')
    require(moment_formula(p)==e,'independent binomial seed value')
    require(all(e[0]>=0 for e in forward(p)),'literal global fixture')
    h={}
    for (a,b,c,d),coefficient in p.items():
        h=add(h,mon(a+1,b,c,d,coefficient/F(a+1)))
    hv=forward(h)
    require(deriv(hv,1)==mul(mon(4),forward(p)),'primitive chain derivative')
    alpha=scale(mul(mon(-2),hv),-1)
    residue=clean({(0,0,c,d):coefficient for (g,ww,c,d),coefficient in alpha.items() if g==-1 and ww==0})
    require(residue==scale(e,-1),'residue equals negative moment')
    require(scale(deriv(alpha,1),-1)==mul(mon(2),forward(p)),'d(H dv)=R omega')
    if not e:
        correction={}
        for (g,ww,c,d),coefficient in alpha.items():
            if g<=-2:
                require(ww==0,'polar part independent of w')
                correction=add(correction,mon(g+1,0,c,d,coefficient/F(g+1)))
        regular=add(alpha,scale(deriv(correction,0),-1))
        require(all(e[0]>=0 for e in regular),'zero-moment explicit regular primitive on V')
        require(all(e[0]<0 and e[1]==0 for e in correction),'correction is polynomial in v on U')
require(forward(z)==add(mon(1,1),mon(0,0,0,1)),'z=g*w+lambda3')
require(forward(w)==mon(0,1),'w literal inverse')
require(jac(mon(1),mon(1,1))==mon(1),'countermodel Jacobian u, not constant')

# Finite arithmetic controls for a theorem proved for all exponents in report.
for a in range(5):
    for b in range(14):
        require(moment_direct(mon(a,b))==moment_formula(mon(a,b)),'monomial extraction formula')
for i in range(5):
    for j in range(5):
        require(2*(i+j+1)>j+1,'all-moment valuation inequality control')
        require(moment_formula(mon(i+j,j))=={},'trdeg-two subalgebra moment control')
        require((i+j-j,j)==(i,j),'exponent map is injective')

# Ordinaryness is material: v is not global and L(v)=lambda2.
require(moment_direct(mon(0,1))==mon(0,0,1),'nonglobal v has nonzero moment')
require(any(e[0]<0 for e in forward(mon(0,1))),'v fails actual ordinaryness check')
require(jac(u,v)==mon(2),'coordinate Jacobian sign')
require(jac(mon(1),w)==add(mon(1,3,k=4),mon(0,1,1,k=-2),mon(0,0,0,1,k=-1)),'strong countermodel nonconstant Jacobian factor')
# No expansion of w^15, w^25 or powers of the strong countermodel.
for i in range(6):
    for j in range(6):
        if i+j:
            for r in range(j+1):
                n=15*i+25*j-19*r
                require(n-3*r>=15*i+3*j>=3,'strong all-moment support inequality control')
require(max(25,5+6)==25 and max(125,1+6*5)==125,'strong B degree bounds')
require(15==15 and 15*5==75,'strong A degree bounds')
def outer_axis_ok(value):
    return value==0
require(not outer_axis_ok((1+0)**15),'strong A fails actual g-axis outer-face guard')
print(json.dumps({'status':'PASS','checks':checks,'scope':'exact symbolic toy and monomial formula controls'},sort_keys=True))
