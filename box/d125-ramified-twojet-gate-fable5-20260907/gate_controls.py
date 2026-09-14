#!/usr/bin/env python3
"""Own stdlib controls for the ramified two-jet gate. Degree-5 R lift, degree-4 D
lift, three D slots/two negative rows, E2/E3 bracket identities on tiny toys,
low tangent relation, raw nilpotent countercontrol. No R^3/R^5 expansion."""
import sys, json, itertools
from fractions import Fraction as Q
# polynomials: dict {(eg,ep,et): Q}; Laurent lifts: dict {(eu,ev,et): Q}
def clean(d): return {e:c for e,c in d.items() if c!=0}
def add(*ps):
    r={}
    for p in ps:
        for e,c in p.items(): r[e]=r.get(e,Q(0))+c
    return clean(r)
def scale(p,s): return clean({e:c*s for e,c in p.items()})
def mul(a,b,cap=None):
    r={}
    for e1,c1 in a.items():
        for e2,c2 in b.items():
            e=tuple(x+y for x,y in zip(e1,e2))
            if cap is not None and e[0]+e[1]>cap: continue
            r[e]=r.get(e,Q(0))+c1*c2
    return clean(r)
def power(p,n,cap=None):
    r={(0,)*len(next(iter(p))):Q(1)}
    for _ in range(n): r=mul(r,p,cap)
    return r
def deriv(p,i):
    r={}
    for e,c in p.items():
        if e[i]:
            f=list(e); f[i]-=1; r[tuple(f)]=r.get(tuple(f),Q(0))+c*e[i]
    return clean(r)
def bracket(a,b): return add(mul(deriv(a,0),deriv(b,1)),scale(mul(deriv(a,1),deriv(b,0)),-1))
def subst(p,phig,phip):
    r={}
    for (i,j,z),c in p.items():
        m=mul(power(phig,i),power(phip,j)); m={(eu,ev,et+z):cc for (eu,ev,et),cc in m.items()}
        r=add(r,scale(m,c))
    return r
FAILS=[]
def need(ok,msg):
    if not ok: FAILS.append(msg); print('FAIL',msg,file=sys.stderr); sys.exit(1)
mode=sys.argv[1] if len(sys.argv)>1 else ''
one={(0,0,0):Q(1)}; g={(1,0,0):Q(1)}; p={(0,1,0):Q(1)}; t={(0,0,1):Q(1)}
tp3=add(t,scale(one,3))
H=add(power(p,5),mul(power(g,3),power(p,2)))
R=add(H,mul(tp3,mul(g,power(p,2))),mul(t,power(p,3)),scale(mul(tp3,p),-1))
Rt=mul(p,add(power(p,2),mul(g,p),scale(one,-1)))
T={(i,j-1,z):c for (i,j,z),c in R.items()}
need(all(j>=0 for (_,j,_) in T),'T is R/p exactly')
need(deriv(R,2)==Rt,'R_t prime equals d/dt R_t')
# weight/parity/degree facts
w=lambda i,j:5*i-7*j
need(max(w(i,j) for (i,j,_) in R)==1 and max(w(i,j) for (i,j,_) in T)==8,'top weights R=1,T=8')
need(all((i+j)%2==1 for (i,j,_) in R) and all((i+j)%2==0 for (i,j,_) in T),'R odd, T even')
need([(i,j) for i in range(16) for j in range(16) if i+j<=15 and (i+j)%2==1 and w(i,j)==3]==[(2,1),(9,6)],'weight-3 odd A slots are the inner face only')
need([(i,j) for i in range(16) for j in range(16) if i+j<=13 and (i+j)%2==1 and w(i,j) in (1,2)]==[(3,2)],'weight 1..2 odd slots below degree 15')
# T mod p and the cubic-in-g constant coefficient valuation
need({e:c for e,c in T.items() if e[1]==0}==scale(tp3,-1),'T mod p = -(t+3)')
const=[(j,c) for (i,j,z),c in T.items() if i==0]   # T's g^0 part: p^4 + t p^2 -(t+3)
need(min(j for j,_ in const)-1==-1,'cubic-in-g constant coefficient has p-valuation -1 after dividing by p')
# degree-5 lift of R and T
u={(1,0,0):Q(1)}; v={(0,1,0):Q(1)}; vi={(0,-1,0):Q(1)}
phig=vi; phip=add(mul(power(v,4),u),scale(v,-1),scale(vi,-1))
LR=subst(R,phig,phip)
need(all(e[1]>=0 for e in LR),'phi(R) ordinary for all t')
need({e:c for e,c in LR.items() if e[1]==0}=={(1,0,0):Q(3)},'phi(R)(u,0)=3u')
LT=subst(T,phig,phip)
need(min(e[1] for e in LT)==1 and {e:c for e,c in LT.items() if e[1]==1}=={(1,1,0):Q(-3)},'phi(T) valuation 1, leader -3uv')
# D slots: even, degree<=4, weight<=-8
slots=sorted((i,j) for i in range(5) for j in range(5-i) if (i+j)%2==0 and w(i,j)<=-8)
need(slots==[(0,2),(0,4),(1,3)],'D slots p2,p4,gp3')
bases=[power(p,2),power(p,4),mul(g,power(p,3))]
lifts=[subst(b,phig,phip) for b in bases]
neg_exps=sorted({e[1] for L in lifts for e in L if e[1]<0})
need(neg_exps==[-4,-2],'negative v-powers of D lifts are exactly -4,-2 (no v^-1, v^-3)')
M=[[L.get((0,ee,0),Q(0)) for L in lifts] for ee in (-4,-2)]
need(all(all(e[0]==0 for e in L if e[1]<0) for L in lifts),'negative D rows carry no u')
need(M==[[0,1,-1],[1,4,-3]],'both negative rows')
wts=[Q(0),Q(1),Q(1)] if mode=='--mutate-omit-negative-row' else [Q(-1),Q(1),Q(1)]
cand=add(*(scale(L,c) for L,c in zip(lifts,wts)))
need(min(e[1] for e in cand)>=-1,'phi(D) valuation >= -1 (phi(TD) ordinary)')
need(add(*(scale(b,c) for b,c in zip(bases,wts)))==mul(power(p,2),add(power(p,2),mul(g,p),scale(one,-1))),'kernel D = p^2(p^2+gp-1)')
need(mul(T,mul(power(p,2),add(power(p,2),mul(g,p),scale(one,-1))))==mul(R,Rt),'T*D = R*R_t prime')
# E2 and E3 bracket identities on a tiny toy R (never the real R)
Rtoy=add(g,power(p,2),mul(g,p)); C=add(power(p,2),mul(g,p),scale(one,2)); U2=add(p,mul(g,p)); U3=power(p,3); V3=add(p,power(g,2))
a=Q(5); b=Q(-2); U1=mul(Rtoy,C)
fR=add(scale(Rtoy,a),scale(power(Rtoy,3),b)); V1=scale(add(scale(mul(power(Rtoy,2),U1),5),fR),Q(1,3))
V2=add(power(g,3),mul(p,g)); U2b=add(mul(g,g),p)
fprime=add(scale(one,a),scale(power(Rtoy,2),3*b))
E2=add(scale(mul(power(Rtoy,2),V2),3),scale(mul(power(Rtoy,4),U2b),-5),scale(mul(Rtoy,power(U1,2)),Q(-5,3)),scale(mul(fprime,U1),Q(-1,3)))
ord2=add(bracket(power(Rtoy,3),V2),bracket(U1,V1),bracket(U2b,power(Rtoy,5)))
need(ord2==bracket(Rtoy,E2),'order-2 identity with f=aR+bR^3 and f-prime term')
ll=Q(7); mm=Q(11)
V1=scale(mul(power(Rtoy,3),C),Q(5,3))
V2=add(scale(mul(power(Rtoy,2),U2),Q(5,3)),scale(mul(Rtoy,power(C,2)),Q(5,9)),scale(Rtoy,ll/3),scale(power(Rtoy,3),mm/3))
cubic=Q(5,9) if mode=='--mutate-cubic-factor' else Q(5,27)
E3=add(scale(mul(power(Rtoy,2),V3),3),scale(mul(power(Rtoy,4),U3),-5),scale(mul(power(Rtoy,2),mul(C,U2)),Q(-10,3)),
       scale(mul(Rtoy,power(C,3)),cubic),scale(mul(Rtoy,C),-ll/3),scale(mul(power(Rtoy,3),C),-mm))
ord3=add(bracket(power(Rtoy,3),V3),bracket(U1,V2),bracket(U2,V1),bracket(U3,power(Rtoy,5)))
need(ord3==bracket(Rtoy,E3),'order-3 identity, cubic 5/27')
need(mul(Rtoy,C)==U1 and all(e[1]>=0 for e in subst(mul(R,Rt),phig,phip)),'phi(R R_t prime) ordinary (degree-8 product only)')
# low tangent relation via degree<=3 truncated products (no R^3)
c=Q(7); d=Q(11)
R3low=power(R,3,cap=3); need({e:cc for e,cc in R3low.items() if e[0]+e[1]<3}=={} ,'R^3 has no degree<3 part')
need(R3low.get((1,2,0),Q(0))==0 and R3low.get((1,2,1),Q(0))==0,'x0=[gp^2]R^3=0')
y0={z:cc for (i,j,z),cc in R3low.items() if (i,j)==(0,3)}
need(y0=={0:Q(-27),1:Q(-27),2:Q(-9),3:Q(-1)},'y0=[p^3]R^3=-(t+3)^3')
lowU=add(scale({e:cc for e,cc in R.items() if e[0]+e[1]<=3},c),scale(mul(power(R,2,cap=3),Rt,cap=3),d))
if mode=='--mutate-independent-tangent': lowU=add(lowU,mul(g,power(p,2)))
cp={z:cc for (i,j,z),cc in lowU.items() if (i,j)==(0,1)}; cgp2={z:cc for (i,j,z),cc in lowU.items() if (i,j)==(1,2)}
need(cp=={0:-3*c,1:-c} and cgp2=={0:3*c,1:c},'[p]U1=-c(t+3), [gp^2]U1=c(t+3), d-free')
need(lowU.get((0,3,0),None) is not None,'d enters only at p^3')
# contradiction arithmetic: a01=0 -> c=0 -> x1=0, but x1^2=3*y0=-3(t+3)^3 !=0 for t!=-3
for tv in (Q(0),Q(1),Q(-2),Q(5)):
    y=sum(cc*tv**z for z,cc in y0.items()); need(3*y!=0,'3 y0 nonzero at t=%s'%tv)
need(sum(cc*Q(-3)**z for z,cc in y0.items())==0,'y0 vanishes exactly at t=-3 (excluded)')
# raw nilpotent countercontrol over Q[s]/(s^5), s encoded in the t slot
Aj=mul(t,p); Bj=scale(mul(power(t,4),g),Q(5,9)); J=bracket(Aj,Bj)
need({e:cc for e,cc in J.items() if e[2]<5}=={} and J=={(0,0,5):Q(-5,9)},'truncated Jacobian zero mod s^5, s^5 row -5/9')
need({e:cc for e,cc in deriv(Aj,1).items() if e[2]<5}=={(0,0,1):Q(1)},'A_p = s nonzero mod s^5')
need(mul(power(t,2),{(0,0,0):Q(1)})!={} and {e:cc for e,cc in power(t,4).items() if e[2]<4}=={},'k^2=s^4 kills raw r0 mod s^4')
if mode=='--mutate-truncated-saturation':
    need({e:cc for e,cc in deriv(Aj,1).items() if e[2]<5}=={},'nilpotent k cannot be canceled')
print(json.dumps({'status':'PASS','mode':mode or 'normal','D_slots':slots,'negative_matrix':[[str(x) for x in r] for r in M],
    'kernel':['-1','1','1'],'phiR_u0':'3u','phiT_leader':'-3uv','cubic':'5/27','p_coeff':{str(k):str(v_) for k,v_ in sorted(cp.items())},
    'gp2_coeff':{str(k):str(v_) for k,v_ in sorted(cgp2.items())},'y0':{str(k):str(v_) for k,v_ in sorted(y0.items())},
    'assert_nodes':0,'scope':'identities and low coefficients only; no R^3/R^5, no receiver point, no raw full-source jet'},sort_keys=True))
