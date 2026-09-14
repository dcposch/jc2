#!/usr/bin/env python3
"""Tiny independent Laurent jet controls, not a full receiver expansion."""
import json
from math import factorial
import sys

def require(ok, message):
    if not ok:
        raise RuntimeError(message)

ZERO = (0, 0, 0, 0)  # u,v,lambda2,lambda3 exponents
ONE = {ZERO: 1}
def mon(exponents, coefficient=1):
    return {exponents: coefficient} if coefficient else {}
def add(*polys):
    out = {}
    for poly in polys:
        for exponent, coefficient in poly.items():
            out[exponent] = out.get(exponent, 0) + coefficient
    return {e:c for e,c in out.items() if c}
def scale(poly, scalar):
    return {e:c*scalar for e,c in poly.items() if c*scalar}
def mul(left, right):
    out = {}
    for e,c in left.items():
        for f,d in right.items():
            at = tuple(x+y for x,y in zip(e,f))
            out[at] = out.get(at, 0) + c*d
    return {e:c for e,c in out.items() if c}
def power(poly, exponent):
    out = ONE
    for _ in range(exponent):
        out = mul(out, poly)
    return out
def derivative(poly, variable):
    out = {}
    for e,c in poly.items():
        if e[variable]:
            f = list(e)
            f[variable] -= 1
            out[tuple(f)] = c*e[variable]
    return out
def bracket(left, right):
    return add(mul(derivative(left,0),derivative(right,1)),
               scale(mul(derivative(left,1),derivative(right,0)),-1))
def jet(poly, u, v):
    return {(b,d):c for (t,e,b,d),c in poly.items() if (t,e)==(u,v)}
def negative(poly, drop=None):
    return {e:c for e,c in poly.items() if e[1]<0 and e[:2]!=drop}

u=mon((1,0,0,0)); v=mon((0,1,0,0)); g=mon((0,-1,0,0))
l2=mon((0,0,1,0)); l3=mon((0,0,0,1))
p=add(mon((1,4,0,0)),mon((0,2,1,0),-1),mon((0,1,0,1),-1),scale(g,-1))
if '--mutate-map' in sys.argv:
    p=add(p,v)  # actual coefficient change that destroys the ideal containment

checked=0
for i in range(8):
    for j in range(8-i):
        image=mul(power(g,i),power(p,j))
        observed=jet(image,0,1)
        require((0,0) not in observed,'V-linear jet escaped the lambda ideal')
        expected={}
        for b in range(j+1):
            for d in range(j-b+1):
                if 3*b+2*d==i+j+1:
                    expected[(b,d)]=(-1)**j*factorial(j)//(factorial(b)*factorial(d)*factorial(j-b-d))
        require(observed==expected,'multinomial V-linear jet mismatch')
        checked+=1

# Ordinary positive fixtures exhibit both generators, without claiming Keller.
q2=add(mul(g,p),power(g,2))
q3=add(p,g)
require(q2==add(mon((1,3,0,0)),mon((0,1,1,0),-1),scale(l3,-1)),'lambda2 fixture')
require(q3==add(mon((1,4,0,0)),mon((0,2,1,0),-1),mon((0,1,0,1),-1)),'lambda3 fixture')
require(not negative(q2) and not negative(q3),'ordinary positive fixtures')
require(jet(q2,0,1)=={(1,0):-1} and jet(q3,0,1)=={(0,1):-1},'both lambda jets attained')

# Independently replays the existing toy at lambda2=lambda3=0.
p0={e:c for e,c in p.items() if e[2:]==(0,0)}
P=g
Q=add(mul(power(g,2),p0),power(g,3))
require(Q==mon((1,2,0,0)),'toy Q=v^2*u')
require(bracket(P,Q)==ONE,'Laurent toy has Jacobian +1')
require(jet(P,0,1)=={} and jet(Q,0,1)=={},'both formal V-linear jets zero')
drop=(0,-1) if '--mutate-drop-negative' in sys.argv else None
require(bool(negative(P,drop)),'ordinaryness verifier must reject the Laurent toy')
require(negative(P)=={(0,-1,0,0):1},'one actual missing negative row')
print(json.dumps({'status':'PASS','monomial_jet_controls':checked,
                  'ordinary_generator_fixtures':2,'laurent_countercontrol':'REJECTED_AS_NONPOLYNOMIAL',
                  'full_client_expanded':False},sort_keys=True))
