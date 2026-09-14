#!/usr/bin/env python3
"""Exact one-variable certificate on C=(x-1)^(t-1), every b.

Normalize V=W/alpha, beta=B/alpha, u=b*y. The u-polynomial coefficients
are rational on each specified split factor 3*d*d=t+1. This driver does
not read prior row files. The high rows reconstruct V,beta; then exact
QQ[u] gcds decide whether a lower-row solution exists.
"""
import argparse
from fractions import Fraction as Q
from math import comb
from time import monotonic
import sympy as sp
import json
from pathlib import Path

ap=argparse.ArgumentParser();ap.add_argument('d',type=int)
ap.add_argument('--show-certificate',action='store_true')
ap.add_argument('--certificate-file')
args=ap.parse_args();d=Q(args.d);t=3*int(d*d)-1
assert t>=2
n=t-1;q=2*t+1;lam=1/(6*d+3)

class P:
    def __init__(self,a=0):
        if isinstance(a,P):self.c=a.c[:]
        elif isinstance(a,list):self.c=[Q(v) for v in a]
        else:self.c=[Q(a)]
        while len(self.c)>1 and not self.c[-1]:self.c.pop()
    def __add__(self,o):
        o=P(o);c=[Q() for _ in range(max(len(self.c),len(o.c)))]
        for i,v in enumerate(self.c):c[i]+=v
        for i,v in enumerate(o.c):c[i]+=v
        return P(c)
    __radd__=__add__
    def __neg__(self):return P([-v for v in self.c])
    def __sub__(self,o):return self+-P(o)
    def __rsub__(self,o):return P(o)+-self
    def __mul__(self,o):
        o=P(o);c=[Q() for _ in range(len(self.c)+len(o.c)-1)]
        for i,v in enumerate(self.c):
            for j,w in enumerate(o.c):c[i+j]+=v*w
        return P(c)
    __rmul__=__mul__
    def __truediv__(self,o):return P([v/Q(o) for v in self.c])
    def __bool__(self):return any(self.c)
    def degree(self):return len(self.c)-1 if self else -1
    def poly(self,var):return sp.Poly.from_list(list(reversed(self.c)),var,domain=sp.QQ)

u=P([0,1]);zero=P()
C=[P((-1)**(n-k)*comb(n,k)) for k in range(n+1)]
A=[P() for _ in range(q+1)]
for k in range(2*n+1):A[k+3]=P((-1)**(2*n-k)*comb(2*n,k))
D=[P()]+[2*u*c for c in C]
K=[-u,P()]+C
V=[P() for _ in range(q+1)];V[q]=P(lam)
def co(a,k):return a[k] if 0<=k<len(a) else zero
def conv(a,b,k):
    return sum((a[i]*b[k-i] for i in range(max(0,k-len(b)+1),min(len(a)-1,k)+1)),P())
def eco(k,beta=zero,eta=zero):
    ans=(k-1)*conv(V,V,k)+2*conv(A,V,k)-conv(D,V,k)-conv(A,A,k)/3+conv(A,D,k)/3
    ans+=beta*(co(A,k)-co(D,k)-co(V,k))
    ans+=2*u*u*((1-k)*co(V,k+1)-co(A,k+1))/3
    ans+=2*u*eta*co(K,k)/3
    if k==1:ans+=beta*eta
    return ans

start=monotonic();assert not eco(2*q)
for m in range(q-1,0,-1):
    k=q+m;diag=2*((q+m-1)*lam+1)
    V[m]=-eco(k)/diag
    assert not eco(k)
    assert V[m].degree()<=1
beta=eco(q)/(2*d);V[0]=-beta;eta=V[1]
res=[eco(k,beta,eta) for k in range(2*q+1)]
assert not any(res[q:]);assert not res[0];assert not res[1]
assert beta.degree()<=1;assert eta.degree()<=1
assert all(r.degree()<=3 for r in res)
var=sp.Symbol('u');g=None;used=[]
print('EXACT_SPLIT_FACTOR','t',t,'d',d,'RECONSTRUCTION_SECONDS',round(monotonic()-start,3),flush=True)
print('HIGH_ROWS_ZERO',q,'THROUGH',2*q,'LOW_ROWS_0_1_ZERO','DEGREES_MAX_3',flush=True)
for k in range(q-1,1,-1):
    if not res[k]:continue
    f=res[k].poly(var)
    if g is None:g=f.monic()
    else:g=sp.gcd(g,f).monic()
    used.append(k)
    print('GCD_STEP','row',k,'row_degree',f.degree(),'gcd_degree',g.degree(),flush=True)
    if g.degree()==0:break
assert g is not None
print('GCD',g.as_expr(),'USED_ROWS',used,'SECONDS',round(monotonic()-start,3),flush=True)
if g.degree()==0:
    print('NO_NORMALIZED_SOLUTION_ON_SHIFTED_COINCIDENT_ROOT_SLICE',flush=True)
else:
    target=beta.poly(var)*eta.poly(var)
    sat=sp.div(target**g.degree(),g)[1]
    print('TARGET_RADICAL_MEMBERSHIP',sat.is_zero,flush=True)
if len(used)==2 and g.degree()==0 and all(res[k].degree()==2 for k in used):
    f1=res[used[0]].poly(var);f2=res[used[1]].poly(var)
    _,ff=f1.clear_denoms();_,ff=ff.primitive()
    _,gg=f2.clear_denoms();_,gg=gg.primitive()
    aa,bb,cc=map(int,ff.all_coeffs());AA,BB,CC=map(int,gg.all_coeffs())
    Delta=aa*BB-AA*bb;epsilon=aa*CC-AA*cc
    NN=aa*epsilon**2-bb*epsilon*Delta+cc*Delta**2
    assert Delta!=0 and NN!=0
    ll=aa*Delta*var+bb*Delta-aa*epsilon
    left=sp.Poly(Delta**2+AA*ll,var,domain=sp.QQ)*ff-sp.Poly(aa*ll,var,domain=sp.QQ)*gg
    assert left==sp.Poly(NN,var,domain=sp.QQ)
    print('INTEGER_BEZOUT_IDENTITY_EXACT_PASS','CONSTANT_NONZERO',bool(NN),
          'CONSTANT_DIGITS',len(str(abs(NN))),flush=True)
    if args.certificate_file:
        cert={'t':t,'d':str(d),'variable':'u=b*y','rows':used,
              'f_coefficients_descending':list(map(str,[aa,bb,cc])),
              'g_coefficients_descending':list(map(str,[AA,BB,CC])),
              'Delta':str(Delta),'epsilon':str(epsilon),'N':str(NN),
              'identity':'(Delta^2+A*(a*Delta*u+b*Delta-a*epsilon))*f - a*(a*Delta*u+b*Delta-a*epsilon)*g = N'}
        Path(args.certificate_file).write_text(json.dumps(cert,indent=2)+'\n')
        print('INTEGER_CERTIFICATE_WRITTEN',args.certificate_file,flush=True)
if args.show_certificate:
    print('BETA',beta.poly(var).as_expr(),flush=True)
    print('ETA',eta.poly(var).as_expr(),flush=True)
    for k in used:
        f=res[k].poly(var);den,fp=f.clear_denoms();content,prim=fp.primitive()
        print('PRIMITIVE_ROW',k,prim.as_expr(),flush=True)
    if len(used)==2 and g.degree()==0:
        f1=res[used[0]].poly(var);f2=res[used[1]].poly(var)
        s1,s2,gg=sp.gcdex(f1,f2)
        assert s1*f1+s2*f2==gg and gg==sp.Poly(1,var,domain=sp.QQ)
        print('BEZOUT_IDENTITY_EXACT_PASS','MULTIPLIER_DEGREES',s1.degree(),s2.degree(),flush=True)
