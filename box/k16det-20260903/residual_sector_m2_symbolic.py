#!/usr/bin/env python3
"""Symbolic u_(t-c)-axis obstruction in a stable two-solve sector.

For a fixed positive offset c (environment ``K16_AXIS_OFFSET``, default 1)
and t>=3c+2, there are only two high solves, c_(t-c) and u_(2t-2c),
followed by lambda_(t,t-c)=[s^3]rho.  Smaller t are finite controls.
"""

from __future__ import annotations

import json
import os
import sympy as s
from dataclasses import dataclass

t=s.symbols('t', integer=True)
raw_offset=os.environ.get('K16_AXIS_OFFSET', '1')
offset=(s.symbols('c', integer=True, positive=True)
        if raw_offset == 'symbolic' else int(raw_offset))
j=t-offset
r=(t+1)/s.Integer(3)


def simp(x):
    return s.cancel(x)


@dataclass(frozen=True)
class P:
    a: s.Expr=s.S.Zero
    b: s.Expr=s.S.Zero
    def __add__(self,o): return P(simp(self.a+o.a),simp(self.b+o.b))
    def __neg__(self): return P(-self.a,-self.b)
    def __sub__(self,o): return self+(-o)
    def sc(self,c): return P(simp(c*self.a),simp(c*self.b))


Z=P(); O=P(0,1)


def qm(x,y): return P(simp(x.a*y.b+x.b*y.a),simp(x.b*y.b+r*x.a*y.a))
def qi(x):
    den=simp(x.b*x.b-r*x.a*x.a)
    return P(simp(-x.a/den),simp(x.b/den))
def qd(x,y): return qm(x,qi(y))


def add(x,y,n): return [x[k]+y[k] for k in range(n)]
def sc(x,c,n): return [x[k].sc(c) for k in range(n)]
def qsc(x,c,n): return [qm(x[k],c) for k in range(n)]
def cv(x,y,n):
    z=[Z for _ in range(n)]
    for a in range(n):
        for b in range(n-a): z[a+b]=z[a+b]+qm(x[a],y[b])
    return z
def Delta(x,n0,n): return [x[k].sc(n0-j*k) for k in range(n)]


q=2*t+1; e=3*t+1
y=P(1/(2*q),(t+1)/(2*q))
g=P(3*e*t/(6*q**3),2*(t+1)*e*t/(6*q**3))


def pc(w):
    ac=(9*w*w*t+18*w*w-54*w*t*t-81*w*t-26*w
        +72*t**3+144*t*t+88*t+16)
    bc=(-9*w*w*t-10*w*w+24*w*t*t+33*w*t+10*w
        -12*t**3-20*t*t-8*t)
    return P(ac,bc).sc(3*t*e/((t+1)*(3*t+2)**3*(4*t-2*w+1)))


def pq(w):
    aq=12*t*t+16*t+4-w*(3*t+4)
    bq=2*(t+1)*(w-t)
    return P(aq,bq).sc(-3*t*e*(q-w)/((t+1)*q*(3*t+2)**2*(4*t-2*w+1)))


def rho(chi,ups,n=4):
    beta=[Z for _ in range(n)]
    # In the m=2 sector chi has only coefficients 0 and 1.
    for k in range(2):
        beta[k]=qd(qm(g,chi[k]).sc(3*t+2-3*j*k),y).sc(1/(2*(t-j*k)))
    dqu=Delta(ups,q,n); dtb=Delta(beta,t,n); dtc=Delta(chi,t,n)
    f=qsc(dqu,g.sc(3),n)
    f=add(f,cv(chi,beta,n),n)
    f=add(f,sc(cv(chi,dtb,n),-1,n),n)
    f=add(f,sc(cv(dtc,beta,n),2,n),n)
    ds=[qd(f[k],y).sc(1/(4*t-2*j*k+1)) for k in range(n)]
    term=cv(Delta(chi,t+1,n),ds,n)
    term=add(term,sc(cv(chi,Delta(ds,q,n),n),-1,n),n)
    term=add(term,sc(cv(dqu,beta,n),2,n),n)
    xi=qsc(term,qi(y).sc(s.Rational(1,2)),n)
    return add(cv(chi,xi,n),sc(cv(dqu,ds,n),-1,n),n)


chi=[O,Z,Z,Z]; ups=[O,O,Z,Z]
r0=rho(chi,ups)
chi[1]=qd(-r0[1],pc(j))
assert rho(chi,ups)[1] == Z
r1=rho(chi,ups)
ups[2]=qd(-r1[2],pq(2*j))
rr=rho(chi,ups)
assert rr[1] == Z and rr[2] == Z
lam=P(s.factor(rr[3].a),s.factor(rr[3].b))

aden, bden=s.denom(lam.a),s.denom(lam.b)
anum,bnum=s.factor(s.numer(lam.a)),s.factor(s.numer(lam.b))
norm=s.factor(3*lam.b**2-(t+1)*lam.a**2)
out={
    'sector':f'integer t>={3*offset+2}, j=t-{offset}',
    'chi1_a':str(s.factor(chi[1].a)),
    'chi1_b':str(s.factor(chi[1].b)),
    'ups2_a':str(s.factor(ups[2].a)),
    'ups2_b':str(s.factor(ups[2].b)),
    'lambda_a_numerator':str(anum),
    'lambda_a_denominator':str(s.factor(aden)),
    'lambda_b_numerator':str(bnum),
    'lambda_b_denominator':str(s.factor(bden)),
    'norm':str(norm),
}
print(json.dumps(out,indent=2))
