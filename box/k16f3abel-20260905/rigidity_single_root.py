#!/usr/bin/env python3
"""Exact b=0 infinity recursion on C=(x-1)^(t-1), normalized W=alpha*V.

No row files or nonfrozen lane inputs. Pair arithmetic in Q[d]/(3d^2-t-1).
"""
import argparse
from fractions import Fraction as Q
from math import comb
from time import monotonic

ap=argparse.ArgumentParser()
ap.add_argument('t', type=int)
ap.add_argument('--full', action='store_true')
args=ap.parse_args();t=args.t;n=t-1;q=2*t+1;dd=Q(t+1,3)

class K:
    def __init__(self,a=0,b=0):
        if isinstance(a,K):self.a,self.b=a.a,a.b
        else:self.a,self.b=Q(a),Q(b)
    def __add__(self,o):
        o=K(o);return K(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self):return K(-self.a,-self.b)
    def __sub__(self,o):return self+-K(o)
    def __rsub__(self,o):return K(o)+-self
    def __mul__(self,o):
        o=K(o);return K(self.a*o.a+dd*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def inv(self):
        nm=self.a*self.a-dd*self.b*self.b
        assert nm
        return K(self.a/nm,-self.b/nm)
    def __truediv__(self,o):return self*K(o).inv()
    def __rtruediv__(self,o):return K(o)*self.inv()
    def __bool__(self):return bool(self.a or self.b)
    def __repr__(self):return f'({self.a})+({self.b})*d'
    def norm(self):return self.a*self.a-dd*self.b*self.b

d=K(0,1);lam=1/(6*d+3)
A=[K() for _ in range(q+1)]
for k in range(2*n+1):A[k+3]=K((-1)**(2*n-k)*comb(2*n,k))
V=[K() for _ in range(q+1)];V[q]=lam
def conv(a,b,k):
    return sum((a[i]*b[k-i] for i in range(max(0,k-len(b)+1),min(len(a)-1,k)+1)),K())
def eco(k,beta=K(),eta=K()):
    ans=(k-1)*conv(V,V,k)+2*conv(A,V,k)-conv(A,A,k)/3
    if k<=q:ans+=beta*(A[k]-V[k])
    if k==1:ans+=beta*eta
    return ans

start=monotonic()
assert not eco(2*q)
for m in range(q-1,0,-1):
    k=q+m
    diag=2*((q+m-1)*lam+1)
    V[m]=-eco(k)/diag
    assert not eco(k)
beta=eco(q)/(2*d)
V[0]=-beta
eta=V[1]
res=[eco(k,beta,eta) for k in range(2*q+1)]
assert not any(res[q:])
bad=[k for k,r in enumerate(res) if r]
print('T',t,'SECONDS',round(monotonic()-start,3),'NONZERO_RESIDUAL_DEGREES',bad,flush=True)
print('BETA_NONZERO',bool(beta),'ETA_NONZERO',bool(eta),'RES2_NORM_SIGN',(res[2].norm()>0)-(res[2].norm()<0),flush=True)
if args.full:
    print('BETA',beta,flush=True);print('ETA',eta,flush=True)
    for k,r in enumerate(res):
        if r:print('RESIDUAL',k,r,flush=True)
else:
    for k in [2,q-1]:
        r=res[k]
        print('RESIDUAL_FIELD_NONZERO',k,bool(r),'BOTH_FACTORS_NONZERO',bool(r.norm()),'NUMERATOR_BITS',max(abs(r.a.numerator).bit_length(),abs(r.b.numerator).bit_length()),flush=True)

