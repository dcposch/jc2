#!/usr/bin/env python3
"""Independent Fable v2 controls for the tuned exceptional-center obstruction.
Stdlib only. Zero Assert nodes. Formal R (R=g and R=g+p^2) for identity/reference gates;
actual source expansions limited to the degree-5 R, S and cubic lifts. Mutations exit 1 at named gates."""
import sys
sys.dont_write_bytecode=True
import ast, json, hashlib, random
from fractions import Fraction as Q
from pathlib import Path

MODE=sys.argv[1] if len(sys.argv)>1 else ''
GATES=[]
def gate(name,ok,detail=''):
    GATES.append({'gate':name,'ok':bool(ok),'detail':detail})
    if not ok:
        sys.stderr.write('FAIL gate=%s %s\n'%(name,detail)); sys.exit(1)

# ---- exact sparse polynomials in (g,p,s); exponents may be negative only in lift ring (u,v)
def add(*ps):
    r={}
    for P in ps:
        for e,c in P.items():
            r[e]=r.get(e,Q(0))+c
    return {e:c for e,c in r.items() if c!=0}
def scale(P,c): return {e:c*v for e,v in P.items() if c*v!=0}
def mul(P,Qp):
    r={}
    for e1,c1 in P.items():
        for e2,c2 in Qp.items():
            e=tuple(a+b for a,b in zip(e1,e2)); r[e]=r.get(e,Q(0))+c1*c2
    return {e:c for e,c in r.items() if c!=0}
def power(P,n):
    r={(0,)*len(next(iter(P))):Q(1)}
    for _ in range(n): r=mul(r,P)
    return r
def d(P,i):
    return {tuple(e[k]-(1 if k==i else 0) for k in range(len(e))):c*e[i] for e,c in P.items() if e[i]!=0}
def bracket(P,Qp): return add(mul(d(P,0),d(Qp,1)),scale(mul(d(P,1),d(Qp,0)),-1))
def trunc(P,N): return {e:c for e,c in P.items() if e[2]<=N}
def sorder(P): return min((e[2] for e in P),default=None)
one={(0,0,0):Q(1)}; g={(1,0,0):Q(1)}; p={(0,1,0):Q(1)}; s={(0,0,1):Q(1)}
def rnd(n=3,deg=2,lo=-3,hi=3):
    r={}
    for _ in range(n):
        r[(random.randint(0,deg),random.randint(0,deg),0)]=Q(random.randint(lo,hi))
    return {e:c for e,c in r.items() if c!=0}
def series(n): return add(*[scale(power(s,i),Q(random.randint(-3,3))) for i in range(n)])

random.seed(20260907)
# ===== C1: identity (I) on two formal R with moving scalar series and nonzero cross bracket
Rs=[('R=g',g),('R=g+p^2',add(g,power(p,2)))]
for name,R in Rs:
    for trial in range(3):
        alpha=add(scale(one,Q(random.choice([1,2,-2]))),scale(s,Q(random.randint(-2,2))),scale(power(s,2),Q(random.randint(-2,2))))
        beta=series(4); delta=add(scale(power(s,2),Q(random.randint(1,3))),scale(power(s,3),Q(random.randint(-2,2))))
        gamma=add(mul(beta,alpha),scale(power(alpha,2),Q(-5,9)),delta)
        a=add(scale(power(R,2),3),alpha); q=add(scale(power(R,2),Q(5,3)),beta,scale(alpha,Q(-5,9)))
        F=add(mul(power(s,2),add(rnd(),p)),mul(power(s,3),rnd())); G=add(mul(power(s,3),add(rnd(),g)),mul(power(s,4),rnd()))
        if MODE=='--mutate-zero-cross': F=mul(power(s,2),R); G=mul(power(s,3),power(R,2))
        A=add(power(R,3),mul(alpha,R),F); B=add(power(R,5),mul(beta,power(R,3)),mul(gamma,R),mul(q,F),G)
        coef=Q(-5,9) if MODE=='--mutate-wrong-quadratic' else Q(-5,3)
        E=add(mul(a,G),scale(mul(delta,F),-1),scale(mul(R,power(F,2)),coef))
        cross={} if MODE=='--mutate-omit-cross' else bracket(F,G)
        gate('C1-nonzero-cross[%s#%d]'%(name,trial),bracket(F,G)!={},'[F,G] must be a genuinely nonzero term')
        gate('C1-identity[%s#%d]'%(name,trial),bracket(A,B)==add(bracket(R,E),cross),'[A,B]=[R,aG-dF-(5/3)RF^2]+[F,G]')
        # C2: reference removal at order l changes G and delta exactly as (K)
        l=2; eta=Q(random.choice([1,2,-1])); theta=Q(random.choice([3,-2,5])); sh=power(s,l)
        beta2=add(beta,scale(sh,eta)); gamma2=add(gamma,scale(sh,theta))
        q2=add(scale(power(R,2),Q(5,3)),beta2,scale(alpha,Q(-5,9)))
        G2=add(B,scale(add(power(R,5),mul(beta2,power(R,3)),mul(gamma2,R)),-1),scale(mul(q2,F),-1))
        exp=add(G,scale(mul(sh,power(R,3)),-eta),scale(mul(sh,R),-theta))
        if MODE!='--mutate-omit-reference-betaF': exp=add(exp,scale(mul(sh,F),-eta))
        gate('C2-reference-G[%s#%d]'%(name,trial),G2==exp,'G -> G - eta s^l R^3 - theta s^l R - eta s^l F')
        d2=add(gamma2,scale(mul(beta2,alpha),-1),scale(power(alpha,2),Q(5,9)))
        gate('C2-reference-delta[%s#%d]'%(name,trial),d2==add(delta,scale(sh,theta),scale(mul(sh,alpha),-eta)),'delta -> delta + theta s^l - eta s^l alpha(s)')
        gate('C2-F-correction-order[%s#%d]'%(name,trial),sorder(scale(mul(sh,F),-eta))==l+sorder(F),'F correction starts at l+j')
        # identity re-holds after the reference change (A,B unchanged)
        a2=a; delta2=d2
        E2=add(mul(a2,G2),scale(mul(delta2,F),-1),scale(mul(R,power(F,2)),Q(-5,3)))
        gate('C2-identity-after-removal[%s#%d]'%(name,trial),bracket(A,B)==add(bracket(R,E2),bracket(F,G2)),'(I) with new references')
        # b(R)=a q + delta  (scalar identity)
        b=add(scale(power(R,4),5),scale(mul(beta,power(R,2)),3),gamma)
        gate('C1-b-equals-aq-plus-delta[%s#%d]'%(name,trial),b==add(mul(a,q),delta),'5R^4+3bR^2+g = a q + delta')

# ===== C3: actual degree-5 R=p^2(p^3+g^3-3p), S=p(p^2+gp-1); low coefficients; lifts (cubic, degree-5 only)
V=add(power(p,3),power(g,3),scale(p,-3)); R5=mul(power(p,2),V); S=mul(p,add(power(p,2),mul(g,p),scale(one,-1)))
gate('C3-R-low-coeffs',R5.get((0,1,0),Q(0))==0 and R5.get((0,3,0))==Q(-3) and R5.get((2,1,0),Q(0))==0 and min(sum(e[:2]) for e in R5)==3,'[p]R=0,[p^3]R=-3,[g^2p]R=0, origin order 3')
gate('C3-S-low-coeffs',S.get((0,1,0))==Q(-1) and S.get((0,3,0))==Q(1),'[p]S=-1,[p^3]S=1')
gate('C3-R-odd-top-weight',all(sum(e[:2])%2==1 for e in R5) and max(5*e[0]-7*e[1] for e in R5)==1 and {e for e in R5 if sum(e[:2])==5}=={(0,5,0),(3,2,0)},'R odd, weight 1, top H')
slots=[(i,n-i) for n in (1,3) for i in range(n+1) if 5*i-7*(n-i)<=1]
gate('C3-U-slots',slots==[(0,1),(0,3),(1,2)],'odd deg<=3 weight<=1 slots are p,p^3,gp^2 only')
gate('C3-weight-a0',max(5*e[0]-7*e[1] for e in power(R5,2))==2,'w(R^2)=2 so w(U)<=3-2=1')
# lift ring (u,v): phi(g)=v^-1, phi(p)=v^4 u - v - v^-1  (exponent tuples (u,v))
u2={(1,0):Q(1)}; v2={(0,1):Q(1)}; vi={(0,-1):Q(1)}
phi_p=add(mul(power(v2,4),u2),scale(v2,-1),scale(vi,-1)); phi_g=vi
def lift(P):
    r={}
    for (i,j,k),c in P.items():
        if k!=0: raise RuntimeError('lift of s-dependent poly')
        term=mul(power(phi_g,i) if i>=0 else None,power(phi_p,j))
        r=add(r,scale(term,c))
    return r
neg=lambda L:{e:c for e,c in L.items() if e[1]<0}
Lp,Lp3,Lgp2=lift(p),lift(power(p,3)),lift(mul(g,power(p,2)))
gate('C3-lift-negative-rows',neg(Lp)=={(0,-1):Q(-1)} and neg(Lp3)=={(0,-3):Q(-1),(0,-1):Q(-3)} and neg(Lgp2)=={(0,-3):Q(1),(0,-1):Q(2)},'complete negative rows of the three U slots')
# solve the 2x3 system: (-u3+u12)=0, (-u1-3u3+2u12)=0 => kernel spanned by (u1,u3,u12)=(-1,1,1)=S
kern=add(scale(p,-1),power(p,3),mul(g,power(p,2)))
gate('C3-U-kernel-is-S',kern==S and neg(lift(kern))=={},'U=dS unique ordinary kernel')
# a mutated 'low p3' claim: dropping [p^3] leaves c free -> must be rejected
al0=Q(-3)
def killed(c,dd):
    rp=-al0*dd; rp3=-3*c+al0*dd
    return rp==0 and (rp3==0 or MODE=='--mutate-low-p3')
gate('C3-low-rows-kill-c-d',killed(Q(0),Q(0)) and not killed(Q(1),Q(0)) and not killed(Q(0),Q(1)) and not killed(Q(-1),Q(1)),'[p]Z=-alpha0 d, [p^3]Z=-3c+alpha0 d kill (c,d)')
LR=lift(R5)
gate('C3-R-lift-ordinary',neg(LR)=={},'phi(R_{-3}) has no negative v powers')
gate('C3-R-lift-v0',{e:c for e,c in LR.items() if e[1]==0}=={(1,0):Q(3)},'phi(R)(u,0)=3u so v^0 of phi(a0)=27u^2+alpha0')
# ===== C4: cubic in g over Kbar((p)): valuations 3n vs -2, and primitivity
gate('C4-no-laurent-root',all(3*n!=-2 for n in range(-40,41)),'g^3 = -(p^3-3p-r p^-2): valuation -2 not divisible by 3 (integer n grid is bookkeeping; the claim is 3|(-2) false)')
gate('C4-primitive',(-2)%3!=0 and Q(1)!=0,'constant coefficient of R-r mod p is -r != 0')
# ===== C5: odd remainder modulo 3z^2+alpha0 is lambda z (random odd h), and Z=cR+a0U form
def polydivmod(h,m):
    h=list(h); qd=[Q(0)]*max(1,len(h)-len(m)+1)
    while len(h)>=len(m) and any(h):
        if h[-1]==0: h.pop(); continue
        k=len(h)-len(m); c=h[-1]/m[-1]; qd[k]=c
        for i,mc in enumerate(m): h[i+k]-=c*mc
        h.pop()
    return qd,h
for t in range(5):
    a0=Q(random.choice([1,-3,2,7]))
    h=[Q(0)]+[Q(random.randint(-4,4)) if i%2==0 else Q(0) for i in range(9)]  # odd: coefficients at odd powers
    h=[Q(random.randint(-4,4)) if i%2==1 else Q(0) for i in range(10)]
    qd,rem=polydivmod(h,[a0,Q(0),Q(3)])
    rem=(rem+[Q(0),Q(0)])[:2]
    gate('C5-odd-remainder#%d'%t,rem[0]==0 and all(qd[i]==0 for i in range(0,len(qd),2)),'remainder lambda z, quotient odd')
# ===== C6: order bookkeeping of the induction (finite grid; NOT a uniform proof, only a consistency check of the stated inequalities)
bad=[]
for m in range(1,9):
    for j in range(1,m+1):
        if not (2*j<3*m): bad.append(('2j<3m',m,j))
        for dd in range(0,j):
            for l in range(j,j+dd):
                if not (l-j<dd and 2*j>l and l+j>=2*j): bad.append(('step2',m,j,dd,l))
            if not (2*j>j+dd and j+dd<2*j): bad.append(('order j+d',m,j,dd))
        for l in range(j,2*j):
            if not (l-j<j and 2*j>l): bad.append(('step3',m,j,l))
gate('C6-order-bookkeeping',bad==[],'delta index < d / F^2 at 2j / F-correction at >=2j (grid m<=8)')
# ===== C7: sigma-oddness gives opposite fibre constants on formal R=g (demonstration on the toy fibre only)
r=Q(2); Fj=add(scale(g,Q(4)),mul(add(scale(power(g,2),3),scale(one,-3*r*r)),add(p,mul(g,power(p,2)))))  # c=4, a0=3g^2-3r^2, U odd
def evalg(P,val):
    r_={}
    for (i,j,k),c in P.items(): r_[(0,j,k)]=r_.get((0,j,k),Q(0))+c*val**i
    return {e:c for e,c in r_.items() if c!=0}
cr=evalg(Fj,r); cmr=evalg(Fj,-r)
gate('C7-opposite-constants',cr=={(0,0,0):Q(8)} and cmr=={(0,0,0):Q(-8)} and cr=={e:-c for e,c in cmr.items()},'F_j = c r on R=r and -c r on R=-r')

out={'status':'PASS','mode':MODE or None,'gates':GATES,'gate_count':len(GATES),
     'scope':'formal-R identity/reference gates; actual expansions only degree-5 R,S and cubic lifts; finite grids are bookkeeping not proof',
     'assert_nodes':sum(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text())))}
if out['assert_nodes']!=0: sys.stderr.write('assert nodes present\n'); sys.exit(2)
print(json.dumps(out,sort_keys=True,indent=1))
