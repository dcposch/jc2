#!/usr/bin/env python3
"""Arrows 3/4 (Fable control): exact bracket identity, (z,p) chain rule with a genuinely moving,
non-trivial coordinate, zero-fiber equation and critical-root derivative.
Toy moving reference Rt = g + p^2 + h*g*p (Rt_g = 1+hp, NOT constant), truncated mod h^4, so that
ghat = (z-p^2)(1-hp+h^2p^2-h^3p^3) satisfies Rt(ghat,p)=z exactly mod h^4.  Random small F,G, scalars.
The identity [A,B] = Rt_g*(D Hhat + Fhat_z DGhat - DFhat Ghat_z) is a universal algebraic fact and is
tested here with the actual Jacobian factor, unlike the producer's z=g coordinate.  Mutations:
--omit-cross, --fixed-g-derivative (use (dH/dp)hat instead of D(Hhat)), --drop-jacobian-factor,
--wrong-critical-factor (-5/3 instead of -10/3).  No Assert nodes."""
import sys, json, random
from fractions import Fraction as Q
mode=sys.argv[1] if len(sys.argv)>1 else ''
HT=4
def need(ok,msg):
    if not ok: raise ValueError(msg)
def clean(d): return {e:c for e,c in d.items() if c and e[2]<HT}
def add(*ps):
    z={}
    for p in ps:
        for e,c in p.items(): z[e]=z.get(e,Q(0))+c
    return clean(z)
def scale(p,c): return clean({e:v*c for e,v in p.items()})
def mul(a,b):
    z={}
    for e,x in a.items():
        for f,y in b.items():
            if e[2]+f[2]>=HT: continue
            k=(e[0]+f[0],e[1]+f[1],e[2]+f[2]); z[k]=z.get(k,Q(0))+x*y
    return clean(z)
def power(p,n):
    z={(0,0,0):Q(1)}
    for _ in range(n): z=mul(z,p)
    return z
def deriv(p,ax):
    z={}
    for e,c in p.items():
        if e[ax]:
            f=list(e); f[ax]-=1; z[tuple(f)]=c*e[ax]
    return clean(z)
def bracket(a,b): return add(mul(deriv(a,0),deriv(b,1)),scale(mul(deriv(a,1),deriv(b,0)),-1))
def subst(P,images):
    z={}
    for e,c in P.items():
        m={(0,0,0):c}
        for im,k in zip(images,e): m=mul(m,power(im,k))
        z=add(z,m)
    return z
one={(0,0,0):Q(1)}; g={(1,0,0):Q(1)}; p={(0,1,0):Q(1)}; h={(0,0,1):Q(1)}
Rt=add(g,power(p,2),mul(h,mul(g,p)))
Rg=deriv(Rt,0)
need(Rg==add(one,mul(h,p)),'toy Rt_g = 1+hp')
hp=mul(h,p)
inv=add(one,scale(hp,-1),power(hp,2),scale(power(hp,3),-1))
ghat=mul(add(g,scale(power(p,2),-1)),inv)   # here axis0 plays z on the hat side
need(subst(Rt,(ghat,p,h))==g,'ghat inverts Rt mod h^4')
rng=random.Random(20260907)
def rnd(deg,terms):
    d={}
    for _ in range(terms):
        i=rng.randint(0,deg); j=rng.randint(0,deg-i); k=rng.randint(0,2)
        d[(i,j,k)]=d.get((i,j,k),Q(0))+Q(rng.randint(-3,3))
    return clean(d)
F=rnd(3,5); G=rnd(3,5)
r=Q(1,2); al=-3*r*r; be=Q(2,3); ga=Q(-1,5); de=ga-be*al+Q(5,9)*al*al
q=add(scale(power(Rt,2),Q(5,3)),scale(one,be-Q(5,9)*al))
A=add(power(Rt,3),scale(Rt,al),F)
B=add(power(Rt,5),scale(power(Rt,3),be),scale(Rt,ga),mul(q,F),G)
H=add(mul(add(scale(power(Rt,2),3),scale(one,al)),G),scale(F,-de),scale(mul(Rt,power(F,2)),Q(-5,3)))
AB=bracket(A,B)
need(AB==add(bracket(Rt,H),bracket(F,G)),'exact identity [A,B]=[Rt,H]+[F,G] with moving Rt')
hat=lambda X: subst(X,(ghat,p,h))
Fh=hat(F); Gh=hat(G); Hh=hat(H)
z=g
need(Hh==add(mul(add(scale(power(z,2),3),scale(one,al)),Gh),scale(Fh,-de),scale(mul(z,power(Fh,2)),Q(-5,3))),'Hhat=(3z^2+al)Ghat-de Fhat-(5/3)z Fhat^2')
DH=hat(deriv(H,1)) if mode=='--fixed-g-derivative' else deriv(Hh,1)
cross={} if mode=='--omit-cross' else add(mul(deriv(Fh,0),deriv(Gh,1)),scale(mul(deriv(Fh,1),deriv(Gh,0)),-1))
rhs=add(DH,cross)
if mode!='--drop-jacobian-factor': rhs=mul(hat(Rg),rhs)
need(hat(AB)==rhs,'[A,B]hat = Rt_g hat * (D Hhat + Fhat_z DGhat - DFhat Ghat_z) mod h^4')
# zero fiber: (al+f1) D g0 - (de+g1) D f0 equals (D Hhat + cross) at z=0
def zpart(P,n): return {(0,e[1],e[2]):c for e,c in P.items() if e[0]==n}
f0,f1,g0,g1=zpart(Fh,0),zpart(Fh,1),zpart(Gh,0),zpart(Gh,1)
lhs0=add(mul(add(scale(one,al),f1),deriv(g0,1)),scale(mul(add(scale(one,de),g1),deriv(f0,1)),-1))
need(zpart(add(deriv(Hh,1),add(mul(deriv(Fh,0),deriv(Gh,1)),scale(mul(deriv(Fh,1),deriv(Gh,0)),-1))),0)==lhs0,'zero-fiber equation (al+f1)Dg0-(de+g1)Df0')
# critical root z=r (3r^2+al=0): D Hhat|_{z=r} = -de DU -(10/3) r U DU with U=Fhat(r)
at_r=lambda P: subst(P,(scale(one,r),p,h))
U=at_r(Fh); DU=deriv(U,1)
fac=Q(-5,3) if mode=='--wrong-critical-factor' else Q(-10,3)
need(at_r(deriv(Hh,1))==add(scale(DU,-de),scale(mul(U,DU),fac*r)),'critical-root non-cross part -de DU-(10/3) r U DU')
need(at_r(add(scale(power(z,2),3),scale(one,al)))=={},'G factor vanishes exactly at the critical root')
print(json.dumps({'mode':mode or 'positive','status':'PASS','Rt':'g+p^2+h*g*p mod h^4','Rt_g':'1+hp','F_terms':len(F),'G_terms':len(G),
  'AB_terms':len(AB),'alpha':str(al),'delta':str(de),'critical_root':str(r)},sort_keys=True))
