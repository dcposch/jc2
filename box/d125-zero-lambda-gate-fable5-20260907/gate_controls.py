#!/usr/bin/env python3
"""Fable 5.1 independent controls for the zero-lambda obstruction lemma.
Coefficient ring R = Z[l2,l3,eps]/(eps^2): nilpotent eps exercised throughout.
Laurent ring R[u,v,v^-1]; source ring R[g,p]. Standard library only.
Monomial key: (t,e,b,d,n) = exponents of u,v,l2,l3,eps; n<=1 (eps^2=0 truncation).
Algorithm differs from the producer's: multinomial closed form is compared against
repeated multiplication AND against the mod-(l2,l3) weight argument; the chain rule is
tested on random pairs with nilpotent coefficients; witnesses are rebuilt from scratch."""
import sys, random
from math import factorial
MUT = set(a for a in sys.argv[1:] if a.startswith('--mutate'))
class Fail(Exception): pass
def need(ok, msg):
    if not ok: raise Fail(msg)
def clean(P): return {k:c for k,c in P.items() if c and k[4] < 2}
def add(*Ps):
    o={}
    for P in Ps:
        for k,c in P.items(): o[k]=o.get(k,0)+c
    return clean(o)
def neg(P): return {k:-c for k,c in P.items()}
def mul(P,Q):
    o={}
    for k,c in P.items():
        for l,d in Q.items():
            m=tuple(a+b for a,b in zip(k,l))
            if m[4] < 2: o[m]=o.get(m,0)+c*d
    return clean(o)
def pw(P,n):
    o={(0,0,0,0,0):1}
    for _ in range(n): o=mul(o,P)
    return o
def D(P,i):  # partial derivative w.r.t. slot i (0=u,1=v); Laurent-valid
    o={}
    for k,c in P.items():
        if k[i]:
            l=list(k); l[i]-=1; o[tuple(l)]=o.get(tuple(l),0)+c*k[i]
    return clean(o)
def br(P,Q): return add(mul(D(P,0),D(Q,1)), neg(mul(D(P,1),D(Q,0))))
def coef(P,t,e): return {k[2:]:c for k,c in P.items() if k[:2]==(t,e)}
def negrows(P): return {k:c for k,c in P.items() if k[1]<0}
def modlam(P): return {k:c for k,c in P.items() if k[2]==0 and k[3]==0}
def M(t=0,e=0,b=0,d=0,n=0,c=1): return {(t,e,b,d,n):c}
u=M(1); v=M(0,1); vinv=M(0,-1); l2=M(0,0,1); l3=M(0,0,0,1); eps=M(0,0,0,0,1)
PHI_G = v if '--mutate-det' in MUT else vinv
PHI_P = add(M(1,4), neg(mul(l2,pw(v,2))), neg(mul(l3,v)), neg(vinv))
if '--mutate-map' in MUT: PHI_P = add(PHI_P, v)
def phi(A):  # A: dict {(i,j): coefficient-poly} in g,p  -> Laurent poly
    o={}
    for (i,j),c in A.items():
        o=add(o, mul(c, mul(pw(PHI_G,i),pw(PHI_P,j))))
    return o
def brA(A,Bp):  # bracket in R[g,p]: A_g B_p - A_p B_g ; result dict {(i,j):coefpoly}
    def dg(A): return {(i-1,j):{k:c*i for k,c in P.items()} for (i,j),P in A.items() if i}
    def dp(A): return {(i,j-1):{k:c*j for k,c in P.items()} for (i,j),P in A.items() if j}
    def m(X,Y):
        o={}
        for (i,j),P in X.items():
            for (k,l),Q in Y.items():
                o[(i+k,j+l)]=add(o.get((i+k,j+l),{}),mul(P,Q))
        return {k:P for k,P in o.items() if P}
    X=m(dg(A),dp(Bp)); Y=m(dp(A),dg(Bp))
    o={}
    for k in set(X)|set(Y): o[k]=add(X.get(k,{}),neg(Y.get(k,{})))
    return {k:P for k,P in o.items() if P}
def sgn(j): return (-1)**(j+1) if '--mutate-sign' in MUT else (-1)**j
def closed_form(i,j):  # claimed [u^0 v^1] phi(g^i p^j)
    o={}
    for b in range(j+1):
        for d in range(j-b+1):
            if 3*b+2*d==i+j+1: o[(b,d,0)]=sgn(j)*factorial(j)//(factorial(b)*factorial(d)*factorial(j-b-d))
    return o
def witnesses(A):  # f_A = l2*U + l3*V built from closed form, no division
    U={}; V={}; f={}
    for (i,j),c in A.items():
        for (b,d,_),m in closed_form(i,j).items():
            need((b,d)!=(0,0),'closed form produced a lambda-free term')
            term=mul(c,M(0,0,b,d,0,m))
            f=add(f,term)
            if b>=1: U=add(U,mul(c,M(0,0,b-1,d,0,m)))
            else:    V=add(V,mul(c,M(0,0,b,d-1,0,m)))
    return f,U,V
log=[]
# C1: closed form vs repeated multiplication, and mod-(l2,l3) weight vanishing, i+j<=9
n=0
for i in range(10):
    for j in range(10-i):
        img=phi({(i,j):M()})
        obs=coef(img,0,1)
        need(obs==closed_form(i,j), f'closed form mismatch at g^{i}p^{j}: {obs} vs {closed_form(i,j)}')
        need((0,0,0) not in obs, 'lambda-free [u^0 v^1] term')
        red=modlam(img)   # weight argument: monomials u^t v^(5t-i-j) only
        need(all(k[1]==5*k[0]-i-j for k in red), 'mod-lambda image not on the 5t-i-j line')
        need(not coef(red,0,1), 'mod-lambda [u^0 v^1] nonzero')
        n+=1
log.append(f'C1 closed-form/multiplication/mod-lambda agree on {n} monomials g^i p^j, i+j<=9')
# C2: chain rule with det=+v^2 on random pairs with nilpotent coefficients, deg<=4
random.seed(20260907)
def rnd(deg):
    A={}
    for i in range(deg+1):
        for j in range(deg+1-i):
            c=add(M(c=random.randint(-3,3)), M(0,0,0,0,1,random.randint(-2,2)))
            if random.random()<0.3: c=add(c, mul(l2,M(c=random.randint(-2,2))))
            if c: A[(i,j)]=c
    return A
det=add(mul(D(PHI_G,0),D(PHI_P,1)), neg(mul(D(PHI_G,1),D(PHI_P,0))))
need(det==M(0,2), f'inverse Jacobian is not +v^2: {det}')
for trial in range(6):
    A=rnd(4); Bp=rnd(3)
    lhs=br(phi(A),phi(Bp)); rhs=mul(M(0,2),phi(brA(A,Bp)))
    need(lhs==rhs, 'chain rule [phi A, phi B] = v^2 phi([A,B]) failed')
log.append('C2 det=+v^2 and chain rule on 6 random nilpotent-coefficient pairs (deg 4,3)')
# C3: witnesses f = l2 U + l3 V exact, random A with eps, and origin identity
for trial in range(6):
    A=rnd(5); f,U,V=witnesses(A)
    need(coef(f,0,0)==coef(phi(A),0,1) and f==add(mul(l2,U),mul(l3,V)), 'witness identity failed')
log.append('C3 f_C = l2*U_C + l3*V_C exact on 6 random degree-5 sources with eps')
# C4: origin evaluation of a polynomial bracket, for ordinary random P,Q with eps (Laurent-free)
for trial in range(6):
    P={}; Q={}
    for t in range(4):
        for e in range(4):
            P[(t,e,0,0,random.randint(0,1))]=random.randint(-3,3); Q[(t,e,0,0,random.randint(0,1))]=random.randint(-3,3)
    P=clean(P); Q=clean(Q); c0=coef(br(P,Q),0,0)
    p1=coef(P,1,0); fB=coef(Q,0,1); q1=coef(Q,1,0); fA=coef(P,0,1)
    def m2(X,Y):
        o={}
        for k,a in X.items():
            for l,b in Y.items():
                m=tuple(x+y for x,y in zip(k,l))
                if m[2]<2: o[m]=o.get(m,0)+a*b
        return {k:c for k,c in o.items() if c}
    want={}
    for k,c in list(m2(p1,fB).items())+[(k,-c) for k,c in m2(q1,fA).items()]: want[k]=want.get(k,0)+c
    want={k:c for k,c in want.items() if c}
    need(c0==want, 'origin evaluation c = p1 f_B - q1 f_A failed')
log.append('C4 constant term of [P,Q] equals p1*fB - q1*fA on 6 random ordinary pairs with eps')
# C5: injectivity witness: v is a nonzerodivisor on R[u,v] even with eps (basis shift)
X=add(M(0,0,0,0,1,1), M(1,2,0,0,0,3)); need(mul(v,X)!={} and set(k[1] for k in mul(v,X))=={1,3}, 'v-shift injectivity')
log.append('C5 multiplication by v shifts the free basis (eps-coefficient survives)')
# C6: Laurent toy at l2=l3=0 (reused, not novel): essential ordinaryness failure
A={(1,0):M()}; Bt={(2,1):M(),(3,0):M()}
need(brA(A,Bt)=={(2,0):M()}, '[g, g^2 p + g^3] != g^2')
P0=phi(A); Q0=phi(Bt)
P0={k:c for k,c in P0.items() if k[2]==k[3]==0}; Q0={k:c for k,c in Q0.items() if k[2]==k[3]==0}
need(P0==M(0,-1) and Q0==M(1,2), f'toy lifts {P0},{Q0}')
need(br(P0,Q0)==M(), 'toy bracket != 1')
need(coef(P0,1,0)=={} and coef(P0,0,1)=={} and coef(Q0,0,1)=={}, 'toy origin data')
drop=(0,-1) if '--mutate-drop' in MUT else None
need(bool({k:c for k,c in negrows(P0).items() if k[:2]!=drop}), 'toy must be rejected as nonordinary')
need(negrows(P0)==M(0,-1), 'exactly one negative row [u^0 v^-1]P=1')
log.append('C6 toy: c=1 not in (0); origin formula gives 0; P_v=-v^-2 has no origin value; single negative row')
# C7: [W, g^2 p + g^3] = l3 g^2 with W = g^2 p + l2 + l3 g + g^3: c = l3 realised, and the single negative row is -l3 v^-1
W={(2,1):M(),(0,0):l2,(1,0):l3,(3,0):M()}; Bw={(2,1):M(),(3,0):M()}
need(brA(W,Bw)=={(2,0):l3}, '[W,B] != l3 g^2')
need(negrows(phi(W))=={} and negrows(phi(Bw))=={(0,-1,0,1,0):-1}, 'W-example negative rows')
need(coef(phi(W),0,1)=={} and coef(phi(W),1,0)=={} , 'phi(W)=u v^2 has no linear origin terms')
log.append('C7 [W,g^2p+g^3]=l3*g^2: lift ordinary only after row -l3 v^-1 vanishes, forcing c=l3=0')
print('\n'.join(log)); print('STATUS PASS controls=7 mutations=' + ','.join(sorted(MUT)) if MUT else 'STATUS PASS controls=7')
