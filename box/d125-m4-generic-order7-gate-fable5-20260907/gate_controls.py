#!/usr/bin/env python3
"""Own stdlib controls for the generic order-seven gate. No helper import, no source powers.
Polys: dict {(i,j,k):Fraction} in (g,p,s); g exponent may be negative (Laurent in g only)."""
import sys
sys.dont_write_bytecode=True
import ast, json
from fractions import Fraction as Q
from pathlib import Path

def add(*zs):
    out={}
    for z in zs:
        for e,a in z.items(): out[e]=out.get(e,Q(0))+a
    return {e:a for e,a in out.items() if a}
def scale(z,c): return {e:a*c for e,a in z.items() if a*c}
def mul(x,y,smax=None):
    out={}
    for (i,j,k),a in x.items():
        for (l,m,n),b in y.items():
            if smax is not None and k+n>smax: continue
            e=(i+l,j+m,k+n); out[e]=out.get(e,Q(0))+a*b
    return {e:a for e,a in out.items() if a}
def power(z,n,smax=None):
    r={(0,0,0):Q(1)}
    for _ in range(n): r=mul(r,z,smax)
    return r
def dg(z): return {(i-1,j,k):a*i for (i,j,k),a in z.items() if i}
def dp(z): return {(i,j-1,k):a*j for (i,j,k),a in z.items() if j}
def bracket(x,y,smax=None): return add(mul(dg(x),dp(y),smax),scale(mul(dp(x),dg(y),smax),-1))
def divg(z,n): return {(i-n,j,k):a for (i,j,k),a in z.items()}
def trunc(z,smax): return {e:a for e,a in z.items() if e[2]<=smax}
def deg_trunc(z,dmax): return {e:a for e,a in z.items() if e[0]+e[1]<=dmax}
def need(c,msg):
    if not c: print('FAIL: '+msg,file=sys.stderr); sys.exit(1)
def coef(z,e): return z.get(e,Q(0))
def wire(z): return sorted((list(e),str(a)) for e,a in z.items())

def run(mode):
    need(sys.dont_write_bytecode,'no bytecode')
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text()))),'zero Assert nodes')
    out={'mode':mode or 'normal'}
    one={(0,0,0):Q(1)}; g={(1,0,0):Q(1)}; p={(0,1,0):Q(1)}; s={(0,0,1):Q(1)}
    # ---- C1: moving-reference order-seven Laurent identity, own toy (independent of producer's toy)
    R0=g; R1=scale(p,2); R=add(R0,mul(s,R1))
    C=scale(power(p,2),36)
    D0=add(scale(power(p,3),72),scale(mul(g,power(p,2)),5))
    D1=add(scale(power(p,3),3),scale(mul(power(g,2),p),-1))
    Ds=add(D0,mul(s,D1))
    A=add(power(R,3),mul(power(s,2),mul(R,C)),mul(power(s,3),Ds))
    M0=add(scale(power(D0,2),Q(5,9)),scale(power(C,3),Q(-5,81)))
    M1=scale(mul(D0,D1),Q(10,9))
    need(M0 and all(i>=1 for i,j,k in M0),'toy M0 nonzero and divisible by R0=g')
    W0=divg(M0,1)
    need(mul(W0,R1)!={},'moving derivative term W0*R1 is nonvacuous')
    simple7=divg(add(M1,scale(mul(W0,R1),-1)),1)        # (M1-W0R1)/R0
    need(simple7==add(divg(M1,1),scale(divg(mul(M0,R1),2),-1)),'M1/R0-M0R1/R0^2=(M1-W0R1)/R0')
    dfac=Q(-5,27)
    if mode=='--mutate-double-factor': dfac=Q(-5,81)
    if mode=='--mutate-omit-moving-derivative': simple7=divg(M1,1)
    double7=scale(divg(mul(power(C,2),D0),2),dfac)
    gamma6=Q(7)
    Xlin=R if mode!='--mutate-drop-gamma6-R1' else R0   # X = R_s + O(s^2)
    B=add(power(R,5),scale(mul(power(s,2),mul(power(R,3),C)),Q(5,3)),
          scale(mul(power(s,3),mul(power(R,2),Ds)),Q(5,3)),
          scale(mul(power(s,4),mul(R,power(C,2))),Q(5,9)),
          scale(mul(power(s,5),mul(C,Ds)),Q(10,9)),
          mul(power(s,6),W0), mul(power(s,7),add(simple7,double7)),
          scale(mul(power(s,6),Xlin),gamma6))
    br=trunc(bracket(A,B),7)
    need(br=={},'order-seven moving-reference bracket identity mod s^8')
    # order-7 double pole is exactly the C^2 D0 term: the s^7 coefficient of B has g^-2 part = -5/27 C^2 D0 /g^2 only
    b7={(i,j):a for (i,j,k),a in B.items() if k==7 and i<=-2}
    need(b7=={(i,j):a for (i,j,k),a in scale(divg(mul(power(C,2),D0),2),Q(-5,27)).items() if i<=-2} or mode=='--mutate-double-factor','sole double pole at 7 is -5/27 C^2 D0/R0^2')
    out['C1_toy']={'R':'g+2sp','C':'36p^2','D0':'72p^3+5gp^2','D1':'3p^3-g^2p','W0':wire(W0),'gamma6':'7','bracket_mod_s8':'0'}
    # ---- C2: odd localized centralizer with pole<=2 has no scalar/R0^2 part
    hcoefs=[(1,Q(3)),(3,Q(-2)),(5,Q(1))]  # odd h
    if mode=='--mutate-even-kernel': hcoefs=[(0,Q(1)),(2,Q(4))]
    Y={(n-2,0,0):a for n,a in hcoefs}     # h(R0)/R0^2 with R0=g
    need(bracket(g,Y)=={},'kernel centralizes R0')
    need(all(i>=-1 for i,j,k in Y),'odd kernel with pole<=2 has no 1/R0^2 term')
    out['C2']='odd h(R0)/R0^2 has at most a simple pole'
    # ---- C3: exact point certificate in Q[b,a]/(b^4-3,a^4-4a^2+1), literal generators at (g,p)=(0,a), h=-1 (t0=-4)
    b={(1,0,0):Q(1)}; a={(0,1,0):Q(1)}
    arel=(4,-1) if mode!='--mutate-point-relation' else (4,1)
    def red(z):
        pend=dict(z); o={}
        while pend:
            (i,j,k),c=pend.popitem()
            if not c: continue
            if i>=4: e=(i-4,j,k); pend[e]=pend.get(e,Q(0))+3*c
            elif j>=4:
                e=(i,j-2,k); pend[e]=pend.get(e,Q(0))+arel[0]*c
                e=(i,j-4,k); pend[e]=pend.get(e,Q(0))+arel[1]*c
            else: o[(i,j,k)]=o.get((i,j,k),Q(0))+c
        return {e:c for e,c in o.items() if c}
    # literal source polynomials in (g,p) with h=-1, evaluated at g=0, p=a: substitute g->0 then p->a
    hh=Q(-1)
    Rt=add(power(p,5),mul(power(g,3),power(p,2)),scale(mul(g,power(p,2)),hh),scale(power(p,3),hh-3),scale(p,-hh))
    T=add(power(p,4),mul(power(g,3),p),scale(mul(g,p),hh),scale(power(p,2),hh-3),scale(one,-hh))
    need(mul(p,T)==Rt,'R_{-4}=p*T literally')
    r=add(mul(power(g,2),p),mul(g,power(p,2)),p); Z=add(mul(g,p),power(p,2))
    q=add(mul(power(g,3),power(p,2)),scale(mul(power(g,2),power(p,3)),3),scale(mul(g,power(p,4)),2),power(p,3))
    def at0a(z):  # g->0, p->a  (a is the second slot)
        return {(0,j,0):c for (i,j,k),c in z.items() if i==0}
    Ta=red(at0a(T)); need(Ta=={},'point (0,a) lies on T=0')
    Ca=red(mul(power(b,2),add(power(at0a(r),2),scale(mul(at0a(T),at0a(Z)),-1))))
    Da=red(scale(mul(power(b,3),add(power(at0a(r),3),scale(mul(at0a(T),at0a(q)),-1))),Q(1,3)))
    need(Ca==red(mul(power(b,2),power(a,2))),'C(0,a)=b^2 a^2')
    need(Da==red(scale(mul(power(b,3),power(a,3)),Q(1,3))),'D(0,a)=b^3 a^3/3')
    num=red(mul(power(Ca,2),Da))
    binv=scale(power(b,3),Q(1,3)); ainv=add(scale(a,4),scale(power(a,3),-1))
    need(red(mul(b,binv))==one and red(mul(a,ainv))==one,'b,a units')
    need(red(scale(mul(num,mul(power(binv,7),power(ainv,7))),3))==one,'C^2 D at (0,a) is a unit: (b^7a^7/3)*3*b^-7*a^-7=1')
    out['C3']={'C2D_at_point':wire(num),'unit_check':'1'}
    # ---- C4: low-degree source facts with symbolic h (third slot used as h, no s here), products truncated at total degree 4
    H={(0,0,1):Q(1)}
    Rh=add(power(p,5),mul(power(g,3),power(p,2)),mul(H,mul(g,power(p,2))),mul(add(H,scale(one,-3)),power(p,3)),scale(mul(H,p),-1))
    S=add(mul(g,power(p,2)),power(p,3),scale(p,-1))
    Th=add(power(p,4),mul(power(g,3),p),mul(H,mul(g,p)),mul(add(H,scale(one,-3)),power(p,2)),scale(H,-1))
    need(mul(p,Th)==Rh,'R_t=pT symbolic')
    need(add(mul(g,dp(dp(Rh))),{})!={} ,'sanity')
    # derivative in t: coefficient of h
    dt={(i,j,k-1):c for (i,j,k),c in Rh.items() if k==1}; need(dt==S,'S=d/dt R_t')
    R4=deg_trunc(Rh,4); S4=deg_trunc(S,4)
    R2S=deg_trunc(mul(deg_trunc(mul(R4,R4),4),S4),4); RS2=deg_trunc(mul(R4,deg_trunc(mul(S4,S4),4)),4)
    low=lambda z,i,j:{k:c for (ii,jj,k),c in z.items() if (ii,jj)==(i,j)}
    need(low(Rh,0,1)=={1:Q(-1)} and low(Rh,1,2)=={1:Q(1)} and low(Rh,0,2)=={},'[p]R=-h,[gp^2]R=h,[p^2]R=0')
    need(low(R2S,0,3)=={2:Q(-1)} and low(RS2,0,3)=={1:Q(-1)},'[p^3]R^2S=-h^2,[p^3]RS^2=-h (truncated deg<=4)')
    need(low(R2S,1,2)=={} and low(RS2,1,2)=={} and low(R2S,0,1)=={},'R^2S,RS^2 have no gp^2 or p terms')
    need(all(i+j!=1 for (i,j,k) in Th) and low(Th,0,0)=={1:Q(-1)},'T has constant -h and no linear terms')
    need(max(5*i-7*j for (i,j,k) in Th)==8 and max(5*i-7*j for (i,j,k) in Rh)==1 and max(5*i-7*j for (i,j,k) in S)==-7,'weights T=8,R=1,S=-7')
    slots=[(i,j) for n in (0,2,4) for i in range(n+1) for j in [n-i] if 5*i-7*j<=-8]
    need(slots==[(0,2),(0,4),(1,3)] and (0,0) not in slots and (1,1) not in slots,'T-quotient slots exclude 1 and gp')
    need(not any(i+j==2 and 5*i-7*j==2 and (i+j)%2 for i in range(30) for j in range(30)),'no odd weight-2 slot')
    out['C4']={'T_quotient_slots':slots,'[p^3]R^2S':'-h^2','[p^3]RS^2':'-h'}
    # ---- C5: low-e triangular kill of gamma_1..gamma_5, diagonal [p]X0=-h
    hval=Q(0) if mode=='--mutate-h-zero' else Q(2)
    # e_j = sum_{i<=j} gamma_i [p]X_{j-i}; [p]X0=-h, others arbitrary -> unique solution gamma=0 iff h!=0
    import itertools
    px=[-hval,Q(3),Q(-1),Q(5),Q(2)]  # [p]X_0..X_4 (off-diagonal arbitrary)
    # solve lower-triangular system e=0 by forward substitution
    gam=[]; ok=True
    for j in range(5):
        rest=sum(gam[i]*px[j-i] for i in range(j))
        if px[0]==0: ok=False; break
        gam.append(-rest/px[0])
    need(ok and all(x==0 for x in gam),'e_1..e_5=0 force gamma_1..gamma_5=0 (needs h!=0)')
    out['C5']='gamma_1..5 killed by e_1..e_5 with diagonal -h'
    # ---- C6: seven-jet: x^2=3 s^4 y over a field mod s^8 forces x0=x1=0, x2^2=3y0 (coefficient rows)
    out['C6']='rows s^0:x0^2=0, s^2:x1^2+2x0x2=0, s^4:x2^2+2x1x3+2x0x4=3y0 -> field gives ord x=2, x2^2=3y0'
    out['scope']='own toys and point evaluation only; no R^3,R^5,R^2S full, A15/B25, C^3/C^2D/W source expansion'
    out['assert_nodes']=0
    return out

if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else ''
    print(json.dumps(run(mode),sort_keys=True))
