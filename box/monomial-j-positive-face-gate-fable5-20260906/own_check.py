#!/usr/bin/env python3
"""Own changed-object controls for the positive-face Euler composition gate.
Exact Fractions only. Solves [E,R]=g^k R for E in a LAURENT window of
(r,s)-weight l*r+s and checks every solution (affine space) is polynomial."""
from fractions import Fraction as Fr
from collections import defaultdict
import resource, math, itertools
resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,)*2)
resource.setrlimit(resource.RLIMIT_CPU,(25,25))
n=0
def check(ok,label):
    global n
    if not ok: raise ValueError('FAIL '+label)
    n+=1; print('PASS',label)
def clean(p): return {a:Fr(c) for a,c in p.items() if c}
def add(p,q):
    d=defaultdict(Fr,p)
    for a,c in q.items(): d[a]+=c
    return clean(d)
def mul(p,q):
    d=defaultdict(Fr)
    for (a,b),c in p.items():
        for (u,v),e in q.items(): d[a+u,b+v]+=c*e
    return clean(d)
def jac(p,q):
    d=defaultdict(Fr)
    for (a,b),c in p.items():
        for (u,v),e in q.items(): d[a+u-1,b+v-1]+=c*e*(a*v-b*u)
    return clean(d)
def sub_t(p,l):  # P(g,p) -> P(g^l,p)
    return {(a*l,b):c for (a,b),c in p.items()}
def face(P,r,s):
    w=max(r*a+s*b for a,b in P)
    return {k:v for k,v in P.items() if r*k[0]+s*k[1]==w}, w
def rowreduce(rows,ncols):
    """rows: list of (coeff list, rhs). returns (consistent, pivots, reduced rows)."""
    rows=[([Fr(x) for x in c],Fr(b)) for c,b in rows]
    piv=[]; ri=0
    for col in range(ncols):
        pr=None
        for i in range(ri,len(rows)):
            if rows[i][0][col]!=0: pr=i;break
        if pr is None: continue
        rows[ri],rows[pr]=rows[pr],rows[ri]
        c,b=rows[ri]; inv=1/c[col]
        rows[ri]=([x*inv for x in c],b*inv)
        for i in range(len(rows)):
            if i!=ri and rows[i][0][col]!=0:
                f=rows[i][0][col]
                rows[i]=([x-f*y for x,y in zip(rows[i][0],rows[ri][0])],rows[i][1]-f*rows[ri][1])
        piv.append(col); ri+=1
    for c,b in rows[ri:]:
        if b!=0: return False,piv,rows
    return True,piv,rows[:ri]
def euler_window(R,r,s,k,W):
    """Unknown monomials g^i p^j, r*i+s*j=l*r+s, -W<=i, j>=0. Return
    (consistent, particular solution dict, kernel basis list, monomial list)."""
    l=k+1; wt=l*r+s
    mons=[]
    for i in range(-W,wt//r+1):
        if (wt-r*i)%s==0:
            j=(wt-r*i)//s
            if j>=0: mons.append((i,j))
    target=mul({(k,0):Fr(1)},R)
    cols=[jac({m:Fr(1)},R) for m in mons]
    keys=set(target)
    for c in cols: keys|=set(c)
    keys=sorted(keys)
    rows=[([c.get(key,Fr(0)) for c in cols],target.get(key,Fr(0))) for key in keys]
    ok,piv,red=rowreduce(rows,len(mons))
    if not ok: return False,None,None,mons
    free=[c for c in range(len(mons)) if c not in piv]
    part={}
    for (c,b),pc in zip(red,piv): part[mons[pc]]=b
    kern=[]
    for f in free:
        v={mons[f]:Fr(1)}
        for (c,b),pc in zip(red,piv):
            if c[f]!=0: v[mons[pc]]=-c[f]
        kern.append(clean(v))
    return True,clean(part),kern,mons
def distinct_nonzero_roots_upper(R,r,s):
    """Face factor after removing g^h p^j: number of distinct roots of p0(z), z=g^(-s/r)p,
    computed as deg of squarefree part via gcd with derivative over Q (exact)."""
    hs=min(a for a,b in R); js=min(b for a,b in R)
    # exponent of z is (b-js) since each z step raises p-exp by 1
    coeffs=defaultdict(Fr)
    for (a,b),c in R.items(): coeffs[b-js]+=c
    deg=max(coeffs)
    f=[coeffs.get(i,Fr(0)) for i in range(deg+1)]
    fp=[i*f[i] for i in range(1,deg+1)]
    def pgcd(a,b):
        a=a[:];b=b[:]
        def trim(x):
            while x and x[-1]==0: x.pop()
            return x
        a=trim(a);b=trim(b)
        while b:
            while len(a)>=len(b):
                q=a[-1]/b[-1]; sh=len(a)-len(b)
                a=[a[i]-(q*b[i-sh] if i>=sh else 0) for i in range(len(a))]
                a=trim(a)
                if not a: break
            a,b=b,a
        return a
    g=pgcd(f,fp)
    return deg-(len(g)-1)   # number of distinct roots over Qbar (all nonzero since f[0]!=0)
# ---- 1. genuine polynomial monomial-J pair from a Keller pair, l=3, k=2 ----
t={(1,0):Fr(1)}; y={(0,1):Fr(1)}
Bk=add(y,mul(t,t))                 # y+t^2
Ak=add(t,mul(Bk,Bk))               # t+(y+t^2)^2
check(jac(Ak,Bk)=={(0,0):Fr(1)},'keller-seed-jacobian-1')
l=3;k=2
P=sub_t(Ak,l); Q=sub_t(Bk,l)
check(jac(P,Q)=={(k,0):Fr(l)},'pulled-back-pair-J=3g^2')
check(all(a>=0 and b>=0 for a,b in P)and all(a>=0 and b>=0 for a,b in Q),'pair-polynomial')
# at (1,l): P = g^3 + p^2 + 2 p g^6 + g^12 -> (1,3)-weights 3,6,9,12: face g^12, monomial
dirs=[(1,3),(1,1),(2,3),(1,2),(3,1),(1,6),(1,4),(2,1)]
for (r,s) in dirs:
    R,w=face(P,r,s); N=(l*r+s)//s
    ok,part,kern,mons=euler_window(R,r,s,k,W=12)
    check(ok,'euler-exists-dir%s'%str((r,s)))
    sols=[part]+[add(part,kv) for kv in kern]
    check(all(min(a for a,b in S)>=0 for S in sols),'all-window-solutions-polynomial-dir%s kernel_dim=%d'%(str((r,s)),len(kern)))
    check(all(max(b for a,b in S)<=N for S in sols),'deg_p<=floor((lr+s)/s)=%d dir%s'%(N,str((r,s))))
    check(jac(part,R)==mul({(k,0):Fr(1)},R),'bracket-replay-dir%s'%str((r,s)))
    if len(R)>1:
        nr=distinct_nonzero_roots_upper(R,r,s)
        check(nr<=N,'face-distinct-roots %d <= %d dir%s'%(nr,N,str((r,s))))
    # transported endpoint alternatives: st = min-p point, en = max-p point
    stR=min(R,key=lambda m:m[1]); enR=max(R,key=lambda m:m[1])
    stE=min(part,key=lambda m:m[1]); enE=max(part,key=lambda m:m[1])
    prop=lambda A,B: A[0]*B[1]-A[1]*B[0]==0
    check(prop(stR,stE) or stE==(l,1),'st-alternative-dir%s stR=%s stE=%s'%(str((r,s)),stR,stE))
    check(prop(enR,enE) or enE==(l,1),'en-alternative-dir%s enR=%s enE=%s'%(str((r,s)),enR,enE))
    check(not prop(stR,(l,1)) and not prop(enR,(l,1)),'Thm2.6(4)-transported-dir%s'%str((r,s)))
# ---- 2. pure-g monomial face, Q polynomial, k=2 ----
P2={(2,1):Fr(1),(5,0):Fr(1)}; Q2={(1,0):Fr(1)}
check(jac(P2,Q2)=={(2,0):Fr(-1)},'P2=g^2p+g^5,Q2=g: J=-g^2')
R2,w=face(P2,1,1); check(R2=={(5,0):Fr(1)},'pure-g-face g^5 at (1,1)')
ok,part,kern,mons=euler_window(R2,1,1,2,W=12)
check(ok and all(min(a for a,b in S)>=0 for S in [part]+[add(part,kv) for kv in kern]),'pure-g-face: every window solution polynomial, kernel_dim=%d'%len(kern))
R2b,w=face(P2,1,3); check(R2b=={(2,1):Fr(1),(5,0):Fr(1)},'one-root face at (1,3)')
ok,part,kern,mons=euler_window(R2b,1,3,2,W=12)
check(ok and all(min(a for a,b in S)>=0 for S in [part]+[add(part,kv) for kv in kern]) and max(b for a,b in part)<=2,'one-root-face polynomial Euler deg_p<=2 kernel_dim=%d'%len(kern))
# ---- 3. root's Laurent fixture: NO polynomial E exists, Laurent window has one ----
base={(0,3):Fr(1),(3,0):Fr(-1)}
RL=mul({(-3,0):Fr(1)},mul(base,base))
okL,partL,kernL,monsL=euler_window(RL,1,1,0,W=12)
check(okL and min(a for a,b in partL)<0,'Laurent-face: window solution exists and is non-polynomial')
okP,_,_,_=euler_window(RL,1,1,0,W=0)
check(not okP,'Laurent-face: NO polynomial-window solution (face-polynomiality hypothesis load-bearing)')
# ---- 4. three-root POLYNOMIAL face at (1,l), l=2, k=1: no Laurent Euler at all ----
l=2;k=1
a={(0,1):Fr(1),(2,0):Fr(-1)}; b={(0,1):Fr(1),(2,0):Fr(-2)}; c={(0,1):Fr(1),(2,0):Fr(-3)}
R3=mul(a,mul(b,c))
ok3,_,_,_=euler_window(R3,1,2,1,W=12)
check(not ok3,'three-distinct-root polynomial face at (1,2),k=1: no twisted Euler element in window W=12')
R3b=mul(a,mul(b,b)); ok3b,p3b,k3b,_=euler_window(R3b,1,2,1,W=12)
check(ok3b and min(x for x,y in p3b)>=0 and max(y for x,y in p3b)<=2,'two-root face (root fixture) solvable, polynomial, deg_p<=2, kernel_dim=%d'%len(k3b))
# ---- 5. determinant sample INCLUDING the pure-g case j=0 (check.py loop omits it) ----
bad=[(u,v,h,j) for u in range(-6,0) for v in range(1,7) for h in range(0,7) for j in range(0,7) if (h,j)!=(0,0) and not u*j-v*h<0]
check(not bad,'least-g determinant u*j-v*h<0 on full sample incl j=0 and h=0')
# ---- 6. chain-rule scaling on a fractional monomial pair (constantization) ----
def jac_fr(p,q):
    d=defaultdict(Fr)
    for (a,b),c in p.items():
        for (u,v),e in q.items(): d[a+u-1,b+v-1]+=c*e*(a*v-b*u)
    return clean(d)
def fwd(p,l): return {(Fr(a,l),b):c for (a,b),c in p.items()}
for k in (1,2,4):
    l=k+1
    Pb,Qb=fwd({(1,1):Fr(1)},l),fwd({(k,0):Fr(1)},l)  # P=gp, Q=g^k : J=-k g^k, t=g^(k+1)
    check(jac_fr(Pb,Qb)=={(0,0):Fr(-k,l)},'constantization [Pbar,Qbar]=c/l at k=%d,l=%d'%(k,l))
    Ft={(1,1):Fr(l,l-1)} if k>0 else None
    E={(l,1):Fr(1,l-1)}
    check(jac(E,{(1,1):Fr(1)})=={(l,1):Fr(1)},'twisted Euler [E,gp]=g^k gp with E=g^l p/(l-1), k=%d'%k)
print('OWN_GATE_CONTROLS_PASS',n)
