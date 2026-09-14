#!/usr/bin/env python3
"""Exact two-variable Laurent/Puiseux controls, standard library only."""
from fractions import Fraction as F
import resource
resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
resource.setrlimit(resource.RLIMIT_CPU,(25,25))

def clean(p):
    return {e:c for e,c in p.items() if c}

def add(p,q):
    r=p.copy()
    for e,c in q.items():
        r[e]=r.get(e,F(0))+c
    return clean(r)

def scale(c,p):
    return clean({e:c*v for e,v in p.items()})

def mul(p,q):
    r={}
    for (i,j),a in p.items():
        for (k,l),b in q.items():
            e=(i+k,j+l)
            r[e]=r.get(e,F(0))+a*b
    return clean(r)

def der(p,n):
    r={}
    for e,c in p.items():
        if e[n]:
            f=list(e)
            f[n]-=1
            r[tuple(f)]=c*e[n]
    return r

def jac(p,q):
    return add(mul(der(p,0),der(q,1)),scale(-1,mul(der(p,1),der(q,0))))

def mono(i,j,c=1):
    return {(F(i),F(j)):F(c)}

def map_first(p,r):
    return {(i*r,j):c for (i,j),c in p.items()}

def need(c,n):
    if not c:
        raise RuntimeError("CHECK_FAILED: "+n)
    print("PASS "+n)

P,Q=mono(1,1),mono(2,0)
need(jac(P,Q)==mono(2,0,-2),"same-polynomial-ring-J-minus2-gamma2")
Pt,Qt=map_first(P,-1),map_first(Q,-1)
need(jac(Pt,Qt)==mono(-4,0,2),"inversion-produces-t-minus4")
need(jac(Pt,Qt)!=mono(0,0,2),"false-constantization-mutation-rejected")
Pu,Qu=map_first(P,F(1,3)),map_first(Q,F(1,3))
need(jac(Pu,Qu)==mono(0,0,F(-2,3)),"correct-Puiseux-constantization")
Eu=mono(1,1,F(3,2))
need(jac(Eu,Pu)==Pu,"Euler-in-corrected-constantized-ring")
Eg=map_first(Eu,3)
need(jac(Eg,P)==mono(3,1,3),"pulled-Euler-has-gamma2-factor")
need(jac(scale(F(1,3),Eg),P)==mono(3,1),"twisted-Euler-normalization")
need(jac(mono(1,1),P)=={},"ordinary-Euler-diagonal-coefficient-zero")
for i in range(-2,4):
    for j in range(4):
        if jac(mono(i,j),P)!=scale(i-j,mono(i,j)):
            raise RuntimeError("monomial derivation identity failed")
print("PASS Laurent-monomial-derivation-controls")
print("ALL_EXACT_CONTROLS_PASS")
