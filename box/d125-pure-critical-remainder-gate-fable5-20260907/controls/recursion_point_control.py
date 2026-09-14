#!/usr/bin/env python3
"""Arrow 2 (Fable control): the filtered coefficientwise recursion versus an independent Hensel root.
Actual R=p^2 V, S, R_s=R+h(s)S with h=s-s^2; F = s^2 R C + s^3 (h1 S C + R p^2) + s^4 g p^2 + s^5 p,
C=gp+p^2 (even, C(0)=0, V does not divide C).  Recursion predicts q=4 and leader P4' = gp^2 + SC - Sp^2.
Independently, at the point (g0,p0)=(cuberoot(-2),2) of V (arithmetic in Q[g]/(g^3+2)), the moving root
G(s) of R_s(G,2)=0 with G(0)=g0 is computed by Newton iteration and f0=F(G(s),2) is expanded; its s^2,s^3
coefficients must vanish and its s^4 coefficient must equal P4'(g0,2).  Mutations: --skip-h-correction
(recursion ignores the moving hS Q_i terms: predicted leader wrong), --weight15-input (prepend s*V, weight 15:
recursion blocked since R does not divide V, and the s^2 leader acquires the pole term 1/p0-g0-p0).
No Assert nodes; only degree<=5 actual factors and a degree-3 receiver polynomial are expanded."""
import sys, json
from fractions import Fraction as Q
mode=sys.argv[1] if len(sys.argv)>1 else ''
def need(ok,msg):
    if not ok: raise ValueError(msg)
# ---- sparse polynomials in (g,p) over Q
def clean(d): return {e:c for e,c in d.items() if c}
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
            k=(e[0]+f[0],e[1]+f[1]); z[k]=z.get(k,Q(0))+x*y
    return clean(z)
def power(p,n):
    z={(0,0):Q(1)}
    for _ in range(n): z=mul(z,p)
    return z
g={(1,0):Q(1)}; p={(0,1):Q(1)}; one={(0,0):Q(1)}
V=add(power(g,3),power(p,3),scale(p,-3)); R=mul(power(p,2),V); S=add(power(p,3),mul(g,power(p,2)),scale(p,-1))
def wt(P): return max(5*i-7*j for i,j in P) if P else -10**9
def div_by_V(P):
    P=dict(P); U={}
    while P:
        a,b=max(P)
        if a<3: return None
        c=P[(a,b)]; U[(a-3,b)]=U.get((a-3,b),Q(0))+c
        for e,cc in (((a,b),Q(1)),((a-3,b+3),Q(1)),((a-3,b+1),Q(-3))): P[e]=P.get(e,Q(0))-c*cc
        P={e:v for e,v in P.items() if v}
    return U
def div_by_R(P):
    U=div_by_V(P)
    if U is None or any(j<2 for i,j in U): return None
    return {(i,j-2):c for (i,j),c in U.items()}
# ---- the moving reference and the input F
h=[Q(0),Q(1),Q(-1)]+[Q(0)]*10          # h(s)=s-s^2
C=add(mul(g,p),power(p,2))
need(div_by_V(C) is None,'V does not divide C')
Fc={2:mul(R,C),3:add(mul(S,C),mul(R,power(p,2))),4:mul(g,power(p,2)),5:p}
if mode=='--weight15-input': Fc[1]=V
need(all(wt(P)<=(15 if mode=='--weight15-input' else 3) for P in Fc.values()),'input weights')
# ---- filtered recursion
cur={i:dict(P) for i,P in Fc.items()}; steps=[]; q=None; leader=None; blocked=None
for i in range(1,6):
    Pi=cur.get(i,{})
    if not Pi: continue
    if div_by_V(Pi) is None: q=i; leader=Pi; break
    Qi=div_by_R(Pi)
    if Qi is None: blocked=i; break
    need(wt(Qi)<=2,'w(Q_i)<=2')
    steps.append(i)
    if mode!='--skip-h-correction':
        for l in range(i+1,6):
            if h[l-i]: cur[l]=add(cur.get(l,{}),scale(mul(S,Qi),-h[l-i]))
    cur[i]={}
# ---- number field Q[g]/(g^3+2), p0=2, and power series over it
p0=Q(2); c3=3*p0-p0**3      # g0^3 = -2
def fmul(x,y):
    a,b,c=x; d,e,f=y
    return (a*d+c3*(b*f+c*e), a*e+b*d+c3*c*f, a*f+b*e+c*d)
def fadd(x,y): return tuple(u+v for u,v in zip(x,y))
def fscale(x,c): return tuple(u*c for u in x)
def finv(x):
    a,b,c=x
    M=[[a,c3*c,c3*b,Q(1)],[b,a,c3*c,Q(0)],[c,b,a,Q(0)]]
    for i in range(3):
        pr=next(r for r in range(i,3) if M[r][i]!=0); M[i],M[pr]=M[pr],M[i]
        pv=M[i][i]; M[i]=[v/pv for v in M[i]]
        for r in range(3):
            if r!=i and M[r][i]!=0:
                f=M[r][i]; M[r]=[u-f*v for u,v in zip(M[r],M[i])]
    return (M[0][3],M[1][3],M[2][3])
ZERO=(Q(0),Q(0),Q(0)); ONE=(Q(1),Q(0),Q(0)); G0=(Q(0),Q(1),Q(0))
PREC=8
def smul(A,B):
    Z=[ZERO]*PREC
    for i in range(PREC):
        for j in range(PREC-i):
            Z[i+j]=fadd(Z[i+j],fmul(A[i],B[j]))
    return Z
def sadd(*As): return [tuple(sum(a[k][n] for a in As) for n in range(3)) for k in range(PREC)]
def sconst(x): return [x]+[ZERO]*(PREC-1)
def sscale(A,c): return [fscale(a,c) for a in A]
def sinv(A):
    inv0=finv(A[0]); Z=[ZERO]*PREC; Z[0]=inv0
    for n in range(1,PREC):
        acc=ZERO
        for k in range(1,n+1): acc=fadd(acc,fmul(A[k],Z[n-k]))
        Z[n]=fscale(fmul(inv0,acc),Q(-1))
    return Z
hs=[(h[k],Q(0),Q(0)) for k in range(PREC)]
def evalpoly(P,Gs):
    tot=[ZERO]*PREC
    for (i,j),c in P.items():
        term=sconst((c*p0**j,Q(0),Q(0)))
        for _ in range(i): term=smul(term,Gs)
        tot=sadd(tot,term)
    return tot
Gs=sconst(G0)
for _ in range(PREC+2):
    Rs=sadd(evalpoly(R,Gs),smul(hs,evalpoly(S,Gs)))
    dRs=sadd(evalpoly({(2,2):Q(3)},Gs),smul(hs,sconst((p0*p0,Q(0),Q(0)))))
    Gs=sadd(Gs,sscale(smul(Rs,sinv(dRs)),Q(-1)))
Rs=sadd(evalpoly(R,Gs),smul(hs,evalpoly(S,Gs)))
need(all(x==ZERO for x in Rs),'Newton root satisfies R_s(G(s),p0)=0 to precision')
need(Gs[0]==G0 and Gs[1]!=ZERO,'root has initial value g0 and genuinely moves')
f0=[ZERO]*PREC
for i,P in Fc.items():
    ev=evalpoly(P,Gs)
    f0=sadd(f0,[ZERO]*i+ev[:PREC-i])
def fev(P): return evalpoly(P,sconst(G0))[0]
report={'mode':mode or 'positive','recursion_steps':steps,'q':q,'blocked_at':blocked,'f0_orders':[k for k in range(PREC) if f0[k]!=ZERO][:4],
        'f0_s2':[str(x) for x in f0[2]],'f0_s3':[str(x) for x in f0[3]],'f0_s4':[str(x) for x in f0[4]]}
if mode=='--weight15-input':
    pole=(Q(1)/p0-p0,Q(-1),Q(0))     # 1/p0 - g0 - p0 with h1=1
    report['pole_leader_prediction']=[str(x) for x in pole]
    print(json.dumps(report,sort_keys=True))
    need(blocked is None,'weight-15 input: recursion blocked at s^%s (V divides but R does not); Hensel leader at s^2 is h1*(1/p0-g0-p0) = %s'%(blocked,f0[2]==pole))
print(json.dumps(report,sort_keys=True))
need(q==4 and f0[2]==ZERO and f0[3]==ZERO,'q=4 with vanishing s^2,s^3 Hensel coefficients')
need(f0[4]==fev(leader),'Hensel s^4 coefficient equals recursion leader P4 mod V at the point')
need(f0[4]!=ZERO and wt(leader)<=3 and max(i+j for i,j in leader)<=13,'leader nonzero, weight<=3, degree<=13')
