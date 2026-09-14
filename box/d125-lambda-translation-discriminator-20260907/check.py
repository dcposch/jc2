#!/usr/bin/env python3
"""Tiny exact transition and leading-coefficient controls; no client expansion."""
from fractions import Fraction
from functools import reduce
import json
import sys

def req(ok, message):
    if not ok: raise RuntimeError(message)
# Monomials in g,w,b,L2,L3.  No rational-function or CAS package.
Z=(0,0,0,0,0)
def var(i):
    z=list(Z); z[i]=1
    return {tuple(z):1}
def add(*polys):
    out={}
    for p in polys:
        for e,c in p.items(): out[e]=out.get(e,0)+c
    return {e:c for e,c in out.items() if c}
def scale(p,a): return {e:c*a for e,c in p.items() if c*a}
def mul(p,q):
    out={}
    for e,c in p.items():
        for f,d in q.items():
            x=tuple(i+j for i,j in zip(e,f)); out[x]=out.get(x,0)+c*d
    return {e:c for e,c in out.items() if c}
def pw(p,n):
    out={Z:1}
    for _ in range(n): out=mul(out,p)
    return out
g,w,b,L2,L3=map(var,range(5))
t=add({Z:1},mul(b,g))
L3new=add(L3,scale(mul(b,L2),-2))
if '--mutate-parameter' in sys.argv: L3new=add(L3,scale(mul(b,L2),2))
E=add(scale(mul(b,L3),3),scale(mul(pw(b,2),L2),-3),
      mul(g,add(scale(mul(pw(b,2),L3),6),scale(mul(pw(b,3),L2),-8))),
      mul(pw(g,2),add(scale(mul(pw(b,3),L3),4),scale(mul(pw(b,4),L2),-7))),
      mul(pw(g,3),add(mul(pw(b,4),L3),scale(mul(pw(b,5),L2),-2))))
wold=add(mul(pw(t,4),w),E)
unew=add(mul(pw(g,4),w),mul(L2,pw(g,2)),mul(L3new,pw(g,3)))
left=add(mul(pw(g,4),wold),mul(L2,mul(pw(g,2),pw(t,2))),mul(L3,mul(pw(g,3),t)))
req(left==mul(pw(t,4),unew),'exact transition identity after clearing t^4')

def evalp(poly,values):
    return sum(c*reduce(lambda x,ye:x*ye[0]**ye[1],zip(values,e),Fraction(1)) for e,c in poly.items())
inverse_checks=0
for gv,wv,bv,x,y in [(2,3,Fraction(1,3),5,7),(-2,1,Fraction(1,4),1,2),(3,-1,-1,2,0)]:
    gv,wv,bv,x,y=map(Fraction,(gv,wv,bv,x,y))
    tv=1+bv*gv; oldg=gv/tv
    oldw=evalp(wold,(gv,wv,bv,x,y)); newy=y-2*bv*x
    restoredg=oldg/(1-bv*oldg)
    restoredw=evalp(wold,(oldg,oldw,-bv,x,newy))
    req((restoredg,restoredw)==(gv,wv),'inverse transition exact fraction fixture')
    inverse_checks+=1

for D in (1,15,25):
    leader=pw(t,4*D)
    req(leader.get((1,0,1,0,0))==4*D,'forbidden g*p^D coefficient is 4D*b')
    req(leader.get((4*D,0,4*D,0,0))==1,'highest transformed p^D coefficient')

# Old A=p+g=w has total degree1, zero origin, monic p, ordinary source lift.
# With L2=1,L3=2,b=1, newL3=0 and A'=t^4*w+3+4g+g^2.
fixture=add(mul(pw(add({Z:1},g),4),w),{Z:3},scale(g,4),pw(g,2))
if '--mutate-drop-forbidden' in sys.argv:
    fixture.pop((4,1,0,0,0))
specialized={}
for (i,j,k,l,m),coefficient in wold.items():
    exponent=(i,j,0,0,0)
    specialized[exponent]=specialized.get(exponent,0)+coefficient*2**m
specialized={e:c for e,c in specialized.items() if c}
req(specialized==fixture,'ordinary toy exact map rejects an actual dropped forbidden term')
req(fixture.get((4,1,0,0,0))==1,'actual forbidden g^4*w term')
# Target constant subtraction cannot alter the offending top w coefficient.
req(add(fixture,{Z:-3}).get((4,1,0,0,0))==1,'target translation does not repair support')
print(json.dumps({'status':'PASS','exact_inverse_fixtures':inverse_checks,
                  'leading_degrees_checked':[1,15,25], 'toy_old_degree':1,'toy_new_degree':5,
                  'full_client_expanded':False},sort_keys=True))
