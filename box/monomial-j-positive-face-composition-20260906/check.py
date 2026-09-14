#!/usr/bin/env python3
"""Tiny exact controls for positive-face Euler composition; NOT Keller witnesses."""
from fractions import Fraction as F
from collections import defaultdict
import resource
resource.setrlimit(resource.RLIMIT_AS, (512*1024**2,)*2)
resource.setrlimit(resource.RLIMIT_CPU, (25,25))
n=0
def check(ok,label):
    global n
    if not ok: raise ValueError(label)
    n+=1
    print('PASS '+label)
def clean(p): return {a:F(c) for a,c in p.items() if c}
def add(p,q):
    d=defaultdict(F,p)
    for a,c in q.items(): d[a]+=c
    return clean(d)
def mul(p,q):
    d=defaultdict(F)
    for (a,b),c in p.items():
        for (u,v),e in q.items(): d[a+u,b+v]+=c*e
    return clean(d)
def scale(p,c): return clean({a:F(c)*v for a,v in p.items()})
def power(p,n):
    d={(0,0):F(1)}
    for _ in range(n): d=mul(d,p)
    return d
def jac(p,q):
    d=defaultdict(F)
    for (a,b),c in p.items():
        for (u,v),e in q.items(): d[a+u-1,b+v-1]+=c*e*(a*v-b*u)
    return clean(d)
def pull_t(p,l): return {(a*l,b):c for (a,b),c in p.items()}
def forward_t(p,l): return {(F(a,l),b):c for (a,b),c in p.items()}
P={(1,1):F(1)}; Q={(2,0):F(1)}
check(jac(P,Q)=={(2,0):F(-2)},'actual-monomial-J-pair')
Pb,Qb=forward_t(P,3),forward_t(Q,3)
check(jac(Pb,Qb)=={(0,0):F(-2,3)},'correct-constantization-chain-factor')
Ft={(1,1):F(3,2)}
check(jac(Ft,Pb)==Pb,'Laurent-Euler-before-pullback')
E=scale(pull_t(Ft,3),F(1,3))
check(jac(E,P)==mul({(2,0):1},P),'twisted-Euler-after-one-over-l')
check(jac(pull_t(Ft,3),P)!=mul({(2,0):1},P),'omit-one-over-l-rejected')
# k=1,l=2,(rho,sigma)=(1,2). Two distinct roots are Euler-compatible.
a={(0,1):F(1),(2,0):F(-1)}
b={(0,1):F(1),(2,0):F(-2)}
R=mul(a,power(b,2)); E=scale(mul(a,b),F(1,2))
check(jac(E,R)==mul({(1,0):1},R),'two-root-polynomial-Euler-fixture')
check(all(i>=0 and j>=0 for i,j in R),'fixture-source-nonnegative-exponents')
check(set(i+2*j for i,j in E)=={4},'Euler-weight-four')
check(max(j for i,j in E)==2,'two-root-bound-sharp-at-Euler-level')
check(jac(scale(E,-1),R)!=mul({(1,0):1},R),'Euler-sign-mutation-rejected')
# Actual changed ring: a Laurent face permits three nonzero roots.
base={(0,3):F(1),(3,0):F(-1)}
RL=mul({(-3,0):F(1)},power(base,2))
EL={(-2,4):F(1,3),(1,1):F(-1,3)}
check(jac(EL,RL)==RL,'Laurent-three-root-Euler-identity')
check(min(i for i,j in RL)<0 and min(i for i,j in EL)<0,'changed-ring-breaks-source-hypothesis')
check(set(i+j for i,j in RL)=={3} and set(i+j for i,j in EL)=={2},'Laurent-positive-weights-do-not-bound-pi')
check(max(j for i,j in EL)==4,'Laurent-Euler-pi-degree-exceeds-two')
# Scalar least-gamma obstruction is uniform, not a finite-case proof.
for u in range(-5,0):
    for s in range(6):
        for b in range(1,6):
            for v in range(6):
                if not u*b-s*v<0: raise ValueError('least-gamma determinant')
check(True,'sample-least-gamma-leading-determinants')
print('POSITIVE_FACE_COMPOSITION_CONTROLS_PASS',n)
