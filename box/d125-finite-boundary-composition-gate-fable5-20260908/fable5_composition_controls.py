#!/usr/bin/env python3
"""Independent tiny changed-object controls for the finite-boundary composition (Fable 5.1 gate).
Toy rings only; no source polynomials, no CAS. Exact Fraction arithmetic."""
import sys
sys.dont_write_bytecode=True
import ast, json
from fractions import Fraction as F
from pathlib import Path
def need(x,msg):
    if not x: raise ValueError(msg)
NV=None
def P(d): return {e:c for e,c in d.items() if c}
def add(a,b):
    o=dict(a)
    for e,c in b.items(): o[e]=o.get(e,F(0))+c
    return P(o)
def neg(a): return {e:-c for e,c in a.items()}
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    o={}
    for e,c in a.items():
        for f,d in b.items():
            h=tuple(x+y for x,y in zip(e,f)); o[h]=o.get(h,F(0))+c*d
    return P(o)
def const(c,n): return {(0,)*n:F(c)} if c else {}
def var(i,n): e=[0]*n; e[i]=1; return {tuple(e):F(1)}
def pw(a,k,n):
    o=const(1,n)
    for _ in range(k): o=mul(o,a)
    return o
def divides(f,g,n):
    """exact division test g | f in Q[x1..xn]; multivariate long division by lead monomial (lex). g nonzero."""
    if not f: return True,{}
    lm=max(g); lc=g[lm]; q={}; r=dict(f)
    while r:
        m=max(r)
        if all(m[i]>=lm[i] for i in range(n)):
            e=tuple(m[i]-lm[i] for i in range(n)); c=r[m]/lc
            q[e]=q.get(e,F(0))+c; r=sub(r,mul({e:c},g))
        else: return False,None
    return True,P(q)
def ev(f,pt): return sum(c*eval_mon(e,pt) for e,c in f.items())
def eval_mon(e,pt):
    v=F(1)
    for x,k in zip(pt,e): v*=F(x)**k
    return v
def main(mode):
    need(not any(isinstance(x,ast.Assert) for x in ast.walk(ast.parse(Path(__file__).read_text()))),'zero Assert nodes')
    out={}
    # ---- (A) vertical-split toy in Q[k,w]: I=k^2*H, H=kw-1 (or the CHANGED object H=w, a line through k=0)
    n=2; k=var(0,n); w=var(1,n); one=const(1,n)
    H = w if mode=='--line' else sub(mul(k,w),one)
    I=mul(pw(k,2,n),H); J=H; N=2
    ok,_=divides(mul(pw(k,N,n),J),I,n); need(ok,'k^N J subset I')
    # intersection identity J ∩ (I+(k^N)) = I : both are principal here; I+(k^N)=(k^N) since I ⊂ (k^N); (H)∩(k^N)=(lcm)=(k^N H) as gcd(H,k^N)=1
    ok,q=divides(I,mul(pw(k,N,n),H),n); need(ok and q==one,'intersection identity J∩(I+(k^N)) = I (principal lcm)')
    # comaximality J+(k^N)=S : search a certificate 1 = a*H + b*k^N of degree<=2 by brute exact solve is avoided; use the explicit one and, for the line, a common zero
    if mode=='--line':
        z=(0,0); comax = not (ev(H,z)==0 and ev(pw(k,N,n),z)==0)
    else:
        cert=sub(mul(pw(k,2,n),pw(w,2,n)),mul(H,add(mul(k,w),one)))  # k^2w^2 - (kw-1)(kw+1)
        comax = (cert==one)
    need(comax,'actual comaximality J+(k^N)=S needed for CRT (fails for the changed object H=w)')
    e=mul(pw(k,2,n),pw(w,2,n)); ok1,_=divides(sub(e,one),J,n); ok2,_=divides(e,pw(k,N,n),n); ok3,_=divides(sub(mul(e,e),e),I,n)
    need(ok1 and ok2 and ok3,'CRT idempotent e=k^2w^2: e≡1 mod J, e≡0 mod k^N, e^2≡e mod I')
    out['A_vertical_split']={'I':'k^2(kw-1)','J':'kw-1','N':N,'idempotent':'k^2w^2','status':'PASS'}
    # ---- (B) localization certificate (C): kw-1 ∈ (k^2(kw-1), zk-1) in Q[k,w,z]
    n3=3; k3=var(0,n3); w3=var(1,n3); z3=var(2,n3); one3=const(1,n3)
    H3=sub(mul(k3,w3),one3); I3=mul(pw(k3,2,n3),H3); G3=sub(mul(z3,k3),one3)
    lhs=sub(mul(pw(z3,2,n3),I3), mul(mul(H3,add(mul(z3,k3),one3)),G3))
    need(lhs==H3,'exact certificate kw-1 = z^2*I - (kw-1)(zk+1)(zk-1): S[z]/(I,zk-1) recovers S/J')
    out['B_localization_certificate']='PASS'
    # ---- (C) symbolic full shear in Q[alpha,beta,gamma,lambda]: delta invariant as a POLYNOMIAL identity
    n4=4; al=var(0,n4); be=var(1,n4); ga=var(2,n4); la=var(3,n4)
    def delta(a,b,g): return add(sub(g,mul(b,a)),mul(const(F(5,9),n4),mul(a,a)))
    nb=sub(be,la); ng = ga if mode=='--omit-gamma' else sub(ga,mul(la,al))
    need(sub(delta(al,nb,ng),delta(al,be,ga))=={},'symbolic delta invariance under B->B-lambda*A (beta and gamma both transported)')
    # z-polynomial identity: (z^5+beta z^3+gamma z) - lambda (z^3+alpha z) = z^5+(beta-lambda)z^3+(gamma-lambda alpha)z
    n5=5; Z=var(4,n5)
    def lift(p): return {e+(0,):c for e,c in p.items()}
    B0=add(add(pw(Z,5,n5),mul(lift(be),pw(Z,3,n5))),mul(lift(ga),Z)); A0=add(pw(Z,3,n5),mul(lift(al),Z))
    sheared=sub(B0,mul(lift(la),A0)); target=add(add(pw(Z,5,n5),mul(lift(nb),pw(Z,3,n5))),mul(lift(ng),Z))
    need(sheared==target,'shear transports (beta,gamma)->(beta-lambda,gamma-lambda*alpha) exactly')
    out['C_full_shear']='PASS'
    # ---- (D) B_p15 slice at t0=-3: pure-p part of R_{-3} is p^5-3p^3 ; [p^15]R^5=-243,[p^15]R^3=1,[p^15]R=0 ; [p^15]A15=[p^15]p^6(p^3+g^3)^3=1
    n1=1; p=var(0,n1); Rp=sub(pw(p,5,n1),mul(const(3,n1),pw(p,3,n1)))
    c5=pw(Rp,5,n1).get((15,),F(0)); c3=pw(Rp,3,n1).get((15,),F(0)); c1=Rp.get((15,),F(0))
    need((c5,c3,c1)==(F(-243),F(1),F(0)),'pure-p coefficients [p^15] of R^5,R^3,R at t=-3')
    beta0 = F(0) if mode=='--beta-zero' else F(243)
    need(c5+beta0*c3==0,'[p^15]B0=0 slice forces beta0=243 (not 0) at t0=-3')
    n2=2; pp=var(0,n2); gg=var(1,n2); A15=mul(pw(pp,6,n2),pw(add(pw(pp,3,n2),pw(gg,3,n2)),3,n2))
    need(A15.get((15,0))==F(1),'[p^15]A=1 so the entire shear is available')
    out['D_slice_beta0']='243'
    # ---- (E) unit-root parameter change with a NON-rational root: m=2, u(s)=2+s over Q(sqrt2); tau=s v(s), v^2=u, compositional inverse
    Nn=9
    def qadd(a,b): return (a[0]+b[0],a[1]+b[1])
    def qmul(a,b): return (a[0]*b[0]+2*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
    def qneg(a): return (-a[0],-a[1])
    def qinv(a):
        d=a[0]*a[0]-2*a[1]*a[1]; return (a[0]/d,-a[1]/d)
    Zq=(F(0),F(0)); Oq=(F(1),F(0))
    def smul(a,b):
        o=[Zq]*Nn
        for i in range(Nn):
            for j in range(Nn-i): o[i+j]=qadd(o[i+j],qmul(a[i],b[j]))
        return o
    def ssub(a,b): return [qadd(x,qneg(y)) for x,y in zip(a,b)]
    u=[Zq]*Nn; u[0]=(F(2),F(0)); u[1]=(F(1),F(0))
    need(not any(F(r)*F(r)==2 for r in range(-2,3)),'u(0)=2 has no rational square root: extension is genuinely needed')
    v0=(F(1),F(0)) if mode=='--rational-root' else (F(0),F(1))   # sqrt2 = (0,1); mutation pretends v0=1
    v=[Zq]*Nn; v[0]=v0
    for nn in range(1,Nn):
        acc=u[nn]
        for i in range(1,nn): acc=qadd(acc,qneg(qmul(v[i],v[nn-i])))
        v[nn]=qmul(acc,qinv(qmul((F(2),F(0)),v0)))   # pivot m*v0^(m-1)=2*v0
    need(smul(v,v)==u,'recursive unit root v^2=u with pivot 2*v0 (mod s^9)')
    tau=[Zq]+v[:Nn-1]   # tau = s*v(s)
    kk=[Zq,Zq]+u[:Nn-2] # k = s^2 u(s)
    need(smul(tau,tau)==kk,'k = tau^m exactly (mod s^9)')
    # compositional inverse sigma with sigma(tau(s)) = s
    def compose(f,g):  # f(g(s)), g(0)=0
        o=[Zq]*Nn; gp=[Oq]+[Zq]*(Nn-1)
        for i in range(Nn):
            o=[qadd(x,qmul(f[i],y)) for x,y in zip(o,gp)]; gp=smul(gp,g)
        return o
    sig=[Zq]*Nn; sig[1]=qinv(tau[1])
    for nn in range(2,Nn):
        cur=compose(sig,tau); sig[nn]=qmul(qneg(cur[nn]),qinv(tau[1]))
        # tau[1]^nn coefficient: cur[nn] currently includes sig[nn]*tau1^nn with sig[nn]=0 -> add correction
        cur=compose(sig,tau)
        sig[nn]=qmul(qadd(sig[nn],qneg(qmul(cur[nn],qinv(qmul(tau[1],pw_q(tau[1],nn-1)))))),Oq) if False else sig[nn]
    # robust Newton-free fix: solve sig[nn] by linear correction using tau1^nn
    sig=[Zq]*Nn; sig[1]=qinv(tau[1])
    for nn in range(2,Nn):
        cur=compose(sig,tau); t1n=Oq
        for _ in range(nn): t1n=qmul(t1n,tau[1])
        sig[nn]=qmul(qneg(cur[nn]),qinv(t1n))
    ident=[Zq,Oq]+[Zq]*(Nn-2)
    need(compose(sig,tau)==ident and compose(tau,sig)==ident,'formal compositional inverse of tau (linear coefficient v0 nonzero)')
    need(compose(kk,sig)==[Zq,Zq,Oq]+[Zq]*(Nn-3),'transported k(sigma(tau)) = tau^2: literal k=tau^m for 14p')
    out['E_unit_root_extension']={'m':2,'u':'2+s','v0':'sqrt2','order':Nn,'status':'PASS'}
    # ---- (F) nilpotent survives localization: T=Q[k,w,eps]/(kw-1,eps^2) -> D=Q[eps]/(eps^2), k,w->1, eps->eps, kills the ideal, eps->eps!=0
    def dmul(a,b): return (a[0]*b[0],a[0]*b[1]+a[1]*b[0])
    img={'k':(F(1),F(0)),'w':(F(1),F(0)),'eps':(F(0),F(1))}
    gens=[dmul(img['k'],img['w']),dmul(img['eps'],img['eps'])]
    gens[0]=(gens[0][0]-1,gens[0][1])
    if mode=='--kill-eps': gens.append(img['eps'])   # changed object: ideal (kw-1, eps^2, eps): eps IS zero there
    need(all(g==(0,0) for g in gens),'Q-algebra map kills every ideal generator (changed object with eps in the ideal fails)')
    need(img['eps']!=(0,0) and dmul(img['k'],img['w'])==(F(1),F(0)),'eps nonzero in T[1/k]=T while k is a unit: J+(k)=S never implies reducedness')
    out['F_nilpotent_localization']='PASS'
    out['status']='PASS'; out['scope']='toy rings and scalar/parameter identities; not D125 points, not a proof substitute'
    return out
def pw_q(a,n):
    o=(F(1),F(0))
    for _ in range(n): o=(o[0]*a[0]+2*o[1]*a[1],o[0]*a[1]+o[1]*a[0])
    return o
if __name__=='__main__':
    print(json.dumps(main(sys.argv[1] if len(sys.argv)>1 else ''),sort_keys=True,indent=1))
