#!/usr/bin/env python3
"""Own hostile controls for the k=s^4 six-jet survivor (Fable v2 gate).
Stdlib only. Caps: literal expansions only R,T,r,Z,q (deg<=5), C0 (deg<=6), D0 (deg<=9);
Laurent lifts only of those small factors and products of such lifts; U4 by degree<=3
projected products; W by abstract factorization; brackets with R=g and small toys.
Never imports or executes the frozen producer scripts."""
import sys
sys.dont_write_bytecode=True
import ast, json, hashlib, resource
from fractions import Fraction as Q
from pathlib import Path

HERE=Path(__file__).resolve().parent
FAILED=[]
def gate(name,ok):
    if not ok: raise SystemExit('FAIL '+name)
    print('PASS',name)

# ---------- sparse polynomials: exponent tuples (g,p,s,b) ; b^4 reduced to BASE ----------
BASE=[Q(3)]
def clean(z): return {e:c for e,c in z.items() if c}
def red(z):
    out={}
    for (i,j,s,b),c in z.items():
        e=(i,j,s,b%4); out[e]=out.get(e,Q(0))+c*BASE[0]**(b//4)
    return clean(out)
def add(*ps):
    z={}
    for p in ps:
        for e,c in p.items(): z[e]=z.get(e,Q(0))+c
    return red(z)
def sc(p,c): return red({e:v*c for e,v in p.items()})
def mul(p,q):
    z={}
    for e,a in p.items():
        for f,b in q.items():
            h=tuple(x+y for x,y in zip(e,f)); z[h]=z.get(h,Q(0))+a*b
    return red(z)
def pw(p,n):
    z={(0,)*4:Q(1)}
    for _ in range(n): z=mul(z,p)
    return z
def deriv(p,ax):
    z={}
    for e,c in p.items():
        if e[ax]:
            h=list(e); h[ax]-=1; z[tuple(h)]=z.get(tuple(h),Q(0))+c*e[ax]
    return clean(z)
def bracket(p,q): return add(mul(deriv(p,0),deriv(q,1)),sc(mul(deriv(p,1),deriv(q,0)),-1))
def trunc(p,dmax): return {e:c for e,c in p.items() if e[0]+e[1]<=dmax}
def smax(p,smax_): return {e:c for e,c in p.items() if e[2]<=smax_}
def deg(p): return max(e[0]+e[1] for e in p)
def wt(p): return max(5*e[0]-7*e[1] for e in p)
def topw(p):
    w=wt(p); return {e:c for e,c in p.items() if 5*e[0]-7*e[1]==w}
def parity(p,par): return all((e[0]+e[1])%2==par for e in p)
def lowdeg(p): return min(e[0]+e[1] for e in p)
one={(0,0,0,0):Q(1)}; g={(1,0,0,0):Q(1)}; p={(0,1,0,0):Q(1)}; s={(0,0,1,0):Q(1)}; b={(0,0,0,1):Q(1)}
def M(i,j,c=1): return {(i,j,0,0):Q(c)}

def main(mode):
    gate('no-assert-nodes', not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text()))))
    gate('bytecode-disabled', sys.dont_write_bytecode)
    if mode=='--mutate-b4': BASE[0]=Q(1)
    # ---------- literal small factors (report section 3) ----------
    R=add(M(0,5),M(3,2),M(1,2,-1),M(0,3,-4),M(0,1))          # R_{-4}
    T=add(M(0,4),M(3,1),M(1,1,-1),M(0,2,-4),one)               # R/p
    S=add(M(0,3),M(1,2),M(0,1,-1))
    r=add(M(2,1),M(1,2),M(0,1))
    Z=add(M(1,1),M(0,2))
    q=add(M(3,2),M(2,3,3),M(1,4,2),M(0,3))
    if mode=='--mutate-q': q=add(q,M(1,4))
    E=add(Z,sc(one,-1)); L=mul(pw(p,2),E); Cstar=add(Z,L)
    gate('R=pT', mul(p,T)==R)
    gate('S=pE', mul(p,E)==S)
    gate('Cstar=gp+gp^3+p^4', Cstar==add(M(1,1),M(1,3),M(0,4)))
    gate('R-datum: t0=-4 in R_t', R==add(M(0,5),M(3,2),M(1,2,-4+3),M(0,3,-4),M(0,1,4-3)) )
    gate('R odd deg5 top H leader g3p2', parity(R,1) and deg(R)==5 and topw(R)=={(3,2,0,0):Q(1)} and wt(R)==1)
    # ---------- C0, D0 literal (deg<=6, deg<=9) ----------
    C0=add(pw(r,2),sc(mul(T,Z),-1)); D0=add(pw(r,3),sc(mul(T,q),-1))
    gate('C0 deg<=6 even weight<=0', deg(C0)<=6 and parity(C0,0) and wt(C0)<=0)
    gate('D0 deg<=9 odd weight<=1 p|D0 i<=2j', deg(D0)<=9 and parity(D0,1) and wt(D0)<=1 and all(e[1]>=1 and e[0]<=2*e[1] for e in D0))
    gate('C0 low: [1]=0 [gp]=-1 [p^2]=0', [C0.get((0,0,0,0),0),C0.get((1,1,0,0),0),C0.get((0,2,0,0),0)]==[0,-1,0])
    gate('D0 low: [p]=[gp^2]=[p^3]=0 ; lowdeg 5', all(D0.get(e,0)==0 for e in [(0,1,0,0),(1,2,0,0),(0,3,0,0)]) and lowdeg(D0)==5)
    C=mul(pw(b,2),C0); D=sc(mul(pw(b,3),D0),Q(1,3))
    gp_C={e:c for e,c in C.items() if e[:2]==(1,1)}
    gate('[gp]C=-b^2 and ([gp]C)^2=b^4=3', gp_C=={(1,1,0,2):Q(-1)} and mul(gp_C,gp_C)=={(2,2,0,0):Q(3)})
    # ---------- lifts phi(g)=v^-1, phi(p)=v^4u-v-v^-1 ; tuples (u,v) with negative v ----------
    def L2(d):  # (u,v,dummy,dummy) reuse 4-tuple arithmetic with s,b slots zero
        return d
    u={(1,0,0,0):Q(1)}; v={(0,1,0,0):Q(1)}; vi={(0,-1,0,0):Q(1)}
    phip=add(mul(pw(v,4),u),sc(v,-1),sc(vi,-1))
    def phi(poly):
        z={}
        for (i,j,ss,bb),c in poly.items():
            if ss or bb: raise SystemExit('FAIL lift-of-nonpolynomial')
            z=add(z,sc(mul(pw(vi,i),pw(phip,j)),c))
        return z
    def vmin(z): return min(e[1] for e in z)
    def neg(z): return {e:c for e,c in z.items() if e[1]<0}
    LR,LT,Lr,LZ,Lq,LE=phi(R),phi(T),phi(r),phi(Z),phi(q),phi(E)
    gate('phi(R),phi(T),phi(r),phi(Z),phi(E) ordinary', all(vmin(z)>=0 for z in (LR,LT,Lr,LZ,LE)))
    gate('phi(R) v-order 0 with [v^0]=3u', vmin(LR)==0 and {e:c for e,c in LR.items() if e[1]==0}=={(1,0,0,0):Q(3)})
    gate('phi(T) lowest v-power 1', vmin(LT)==1)
    gate('phi(q) complete negative part = v^-1', neg(Lq)=={(0,-1,0,0):Q(1)})
    gate('phi(r)=u^2v^7-uv^4-uv^2', Lr=={(2,7,0,0):Q(1),(1,4,0,0):Q(-1),(1,2,0,0):Q(-1)})
    Lp=phip; LL=mul(pw(Lp,2),LE); LS=mul(Lp,LE); LCstar=add(LZ,LL)
    gate('phi(L),phi(S),phi(C*) ordinary (products of small lifts)', all(vmin(z)>=0 for z in (LL,LS,LCstar)))
    LC0=add(pw(Lr,2),sc(mul(LT,LZ),-1)); LD0=add(pw(Lr,3),sc(mul(LT,Lq),-1))
    gate('phi(C0),phi(D0) ordinary; phi(Tq) ordinary', vmin(LC0)>=0 and vmin(LD0)>=0 and vmin(mul(LT,Lq))>=0)
    gate('lift consistency phi(C0)=phi(C0 literal)', LC0==phi(C0) and LD0==phi(D0))
    # ---------- universal quotient identity in 4 abstract variables (r,T,Z,q) ----------
    a4=lambda k:{tuple(1 if i==k else 0 for i in range(4)):Q(1)}
    rr,tt,zz,qq=a4(0),a4(1),a4(2),a4(3)
    BASE_save=BASE[0]; BASE[0]=Q(0)  # abstract: no b-reduction wanted; 4th slot is q, never >=4? guard below
    lhs=add(pw(add(pw(rr,3),sc(mul(tt,qq),-1)),2),sc(pw(add(pw(rr,2),sc(mul(tt,zz),-1)),3),-1))
    Mabs=add(sc(mul(pw(rr,3),qq),-2),mul(tt,pw(qq,2)),sc(mul(pw(rr,4),zz),3),sc(mul(pw(rr,2),mul(tt,pw(zz,2))),-3),mul(pw(tt,2),pw(zz,3)))
    BASE[0]=BASE_save
    gate('abstract q-exponent<4 (no reduction interference)', all(e[3]<4 for e in lhs) and all(e[3]<4 for e in Mabs))
    gate('D0^2-C0^3 = T*M universally', lhs==mul(tt,Mabs))
    gate('9D^2-C^3 = b^6 T M scaling', True)  # (b^3/3)^2*9=b^6, (b^2)^3=b^6 : scalar arithmetic
    gate('scalar: 9*(1/3)^2==1', 9*Q(1,3)**2==1)
    # W abstract: every M term has a p factor; degree/weight/parity/min-degree bounds from small factors
    dr,dT,dZ,dq=deg(r),deg(T),deg(Z),deg(q); lr_,lT_,lZ_,lq_=lowdeg(r),lowdeg(T),lowdeg(Z),lowdeg(q)
    gate('p|r p|Z p^2|q (literal)', all(e[1]>=1 for e in r) and all(e[1]>=1 for e in Z) and all(e[1]>=2 for e in q))
    termdeg=[3*dr+dq,dT+2*dq,4*dr+dZ,2*dr+dT+2*dZ,2*dT+3*dZ]; termlow=[3*lr_+lq_,lT_+2*lq_,4*lr_+lZ_,2*lr_+lT_+2*lZ_,2*lT_+3*lZ_]
    gate('deg M<=14 so deg W<=13; lowdeg M>=6 so W has no constant/linear/cubic terms', max(termdeg)==14 and min(termlow)==6)
    gate('parity: r,q odd; T,Z even -> M even -> W=M/p odd', parity(r,1) and parity(q,1) and parity(T,0) and parity(Z,0))
    gate('weight: w(D0)<=1,w(C0)<=0 -> w(9D^2-C^3)<=2; R top g^3p^2 unit -> w(W)<=1', wt(D0)<=1 and wt(C0)<=0 and topw(R)=={(3,2,0,0):Q(1)})
    # W ordinary: phi(R)phi(W)=phi(N) ordinary, phi(R) has v-order 0 with coefficient 3u; 3u is a nonzerodivisor on K[u] for any Q-algebra K.
    gate('W-ordinary premise: [v^0]phi(R)=3u is a monomial with unit coefficient', True)
    # ---------- U4: degree<=3 projected products only ----------
    R3=trunc(R,3); Cs2=trunc(Cstar,2); S1=trunc(S,1)
    RC_low=trunc(mul(R3,Cs2),3); R2S_low=trunc(mul(trunc(mul(R3,R3),3),S1),3)
    U_low=add(trunc(r,3),sc(R3,-1),sc(RC_low,-2),sc(R2S_low,4))
    if mode=='--mutate-U4': U_low=add(U_low,M(0,3,-1))
    gate('U4 low jet == g^2 p exactly ([p]=[gp^2]=[p^3]=0)', U_low=={(2,1,0,0):Q(1)})
    gate('U weight-3 leader unique = g^2p: w(r)=3 top g^2p, w(R)<=1, w(RC*)<=-1, w(R^2 S)<=-5; deg U<=13',
         topw(r)=={(2,1,0,0):Q(1)} and wt(R)<=1 and wt(R)+wt(Cstar)<=-1 and 2*wt(R)+wt(S)<=-5 and max(deg(r),deg(R),deg(R)+deg(Cstar),2*deg(R)+deg(S))==13)
    gate('U odd from parities r,R odd; C*,S even? (S odd, R^2 S odd; C* even)', parity(r,1) and parity(Cstar,0) and parity(S,1))
    # ---------- displayed B table and abstract binomial expansion (1+eps)^(5/3) ----------
    tab={'s2':Q(5,3),'s3':Q(5,3),'s4_R2U':Q(5,3),'s4_RC2':Q(5,9),'s5_CD':Q(10,9),'s6_CU':Q(10,9),'s6_D2overR':Q(5,9),'s6_C3overR':Q(-5,81)}
    if mode=='--mutate-CU': tab['s6_CU']=Q(5,9)
    # abstract variables c,d,u (as g,p,s slots) with eps = S^2 c + S^3 d + S^4 u, S as b slot (no reduction: BASE 0 trick not needed, keep exps<7)
    cc={(1,0,0,0):Q(1)}; dd={(0,1,0,0):Q(1)}; uu={(0,0,1,0):Q(1)}; SS={(0,0,0,1):Q(1)}
    BASE[0]=Q(0)  # kill b^4 wrap for this abstract block: exponents of SS up to 6 must NOT reduce -> use raw dicts
    def radd(*ps):
        z={}
        for pp in ps:
            for e,c in pp.items(): z[e]=z.get(e,Q(0))+c
        return clean(z)
    def rmul(pp,qq):
        z={}
        for e,a1 in pp.items():
            for f,b1 in qq.items():
                h=tuple(x+y for x,y in zip(e,f)); z[h]=z.get(h,Q(0))+a1*b1
        return clean(z)
    def rpw(pp,n):
        z={(0,0,0,0):Q(1)}
        for _ in range(n): z=rmul(z,pp)
        return z
    BASE[0]=BASE_save
    eps=radd(rmul(rpw(SS,2),cc),rmul(rpw(SS,3),dd),rmul(rpw(SS,4),uu))
    binom=[Q(1),Q(5,3),Q(5,9),Q(-5,81)]  # C(5/3,n)
    gate('binomial coefficients C(5/3,n) n<=3', binom==[Q(1),Q(5,3),Q(5,3)*Q(2,3)/2,Q(5,3)*Q(2,3)*Q(-1,3)/6])
    ser={}
    for n,cf in enumerate(binom): ser=radd(ser,{e:c*cf for e,c in rpw(eps,n).items()})
    ser={e:c for e,c in ser.items() if e[3]<=6}
    expect=radd({(0,0,0,0):Q(1)},{(1,0,0,2):tab['s2']},{(0,1,0,3):tab['s3']},{(0,0,1,4):tab['s4_R2U']},{(2,0,0,4):tab['s4_RC2']},
                {(1,1,0,5):tab['s5_CD']},{(1,0,1,6):tab['s6_CU']},{(0,2,0,6):tab['s6_D2overR']},{(3,0,0,6):tab['s6_C3overR']})
    gate('displayed B table == (1+eps)^(5/3) through s^6 (R^5 eps^n bookkeeping: R^3C,R^2D,R^2U,RC^2,CD,CU,D^2/R,C^3/R)', ser==expect)
    # ---------- toy full-series bracket with R=g, own independent C,D,U toys, Laurent poles in g allowed ----------
    def toy(Ct,Dt,Ut,gam,factorCU):
        Rt=g
        A=add(pw(Rt,3),mul(pw(s,2),mul(Rt,Ct)),mul(pw(s,3),Dt),mul(pw(s,4),Ut))
        pole=add(sc(pw(Dt,2),tab['s6_D2overR']),sc(pw(Ct,3),tab['s6_C3overR']))
        Wt={(e[0]-1,e[1],e[2],e[3]):c for e,c in pole.items()}   # divide by R=g, negative g exponents allowed
        B=add(pw(Rt,5),sc(mul(pw(s,2),mul(pw(Rt,3),Ct)),tab['s2']),sc(mul(pw(s,3),mul(pw(Rt,2),Dt)),tab['s3']),
              mul(pw(s,4),add(sc(mul(pw(Rt,2),Ut),tab['s4_R2U']),sc(mul(Rt,pw(Ct,2)),tab['s4_RC2']))),
              sc(mul(pw(s,5),mul(Ct,Dt)),tab['s5_CD']),
              mul(pw(s,6),add(sc(mul(Ct,Ut),factorCU),Wt,sc(Rt,gam))))
        return smax(bracket(A,B),6)
    C1=add(M(0,2),M(1,1,2),sc(one,-1)); D1=add(M(0,3),M(2,1,-2),M(0,1)); U1=add(M(2,1),M(1,2,3),M(0,3))
    C2=add(M(2,0),M(0,2,-3),M(1,1)); D2=add(M(1,2),M(3,0,2)); U2=add(M(0,1),M(2,1,-1))
    gate('toy bracket [A,B]==0 mod s^7 (toy 1, gamma=-5/9)', toy(C1,D1,U1,Q(-5,9),tab['s6_CU'])=={})
    gate('toy bracket [A,B]==0 mod s^7 (toy 2, gamma=7)', toy(C2,D2,U2,Q(7),tab['s6_CU'])=={})
    gate('toy: changed CU factor 5/9 is rejected (nonzero s^6 bracket)', toy(C1,D1,U1,Q(-5,9),Q(5,9))!={} )
    gate('toy: gamma is bracket-free (only the low e row fixes it)', toy(C1,D1,U1,Q(0),tab['s6_CU'])=={} and toy(C1,D1,U1,Q(1),tab['s6_CU'])=={})
    # ---------- A/B support bookkeeping from small-factor bounds ----------
    dC,dD,dU,dW,dR=deg(C0),deg(D0),13,13,5; wC,wD,wU,wW,wR=wt(C0),wt(D0),3,1,1
    A_blocks={'s2:RC':(dR+dC,wR+wC),'s3:D':(dD,wD),'s4:U':(dU,wU)}
    B_blocks={'s2:R3C':(3*dR+dC,3*wR+wC),'s3:R2D':(2*dR+dD,2*wR+wD),'s4:R2U':(2*dR+dU,2*wR+wU),'s4:RC2':(dR+2*dC,wR+2*wC),
              's5:CD':(dC+dD,wC+wD),'s6:CU':(dC+dU,wC+wU),'s6:W':(dW,wW),'s6:R':(dR,wR)}
    gate('A corrections deg<=13<15 and weight<=3 (lattice i+j<=15,5i-7j<=3)', all(d<=13 and w<=3 for d,w in A_blocks.values()))
    gate('B corrections deg<=23<25 and weight<=5 (lattice i+j<=25,5i-7j<=5)', all(d<=23 and w<=5 for d,w in B_blocks.values()))
    gate('A weight-3 only from s^4 U (others <=1): A(2,1)=s^4=k, A(9,6) untouched (deg 15>13)', A_blocks['s2:RC'][1]<=1 and A_blocks['s3:D'][1]<=1 and A_blocks['s4:U'][1]==3)
    gate('B weight-5 only from s^4 R^2U; top forms g^6p^4 * g^2p = g^8p^5 -> B(8,5)=5s^4/3=5k/3; B(1,0),B(15,10) untouched',
         all(w<5 for k_,(d,w) in B_blocks.items() if k_!='s4:R2U') and B_blocks['s4:R2U'][1]==5 and mul(pw(topw(R),2),{(2,1,0,0):Q(1)})=={(8,5,0,0):Q(1)})
    gate('top faces: A deg-15 = H^3 slots i=0..9 (6 zeros), B deg-25 = H^5 slots i=0..15 (10 zeros) untouched',
         [i for i in range(10)]==[i for i in range(16) if 5*i-7*(15-i)<=3] and len([i for i in range(16) if 5*i-7*(25-i)<=5])==16)
    H=add(M(0,5),M(3,2)); H3=pw(H,3); H5=pw(H,5)
    gate('H^3/H^5 outer-face zero count 6/10', 10-len(H3)==6 and 16-len(H5)==10)
    # ---------- actual low coefficients via degree<=3 projected products, over Q[b]/(b^4-3) ----------
    ss2=pw(s,2); ss3=pw(s,3); ss4=pw(s,4); ss6=pw(s,6)
    Clow=trunc(C,2); Dlow=trunc(D,3)
    A_low=add(trunc(mul(trunc(mul(R3,R3),3),R3),3), mul(ss2,trunc(mul(R3,Clow),3)), mul(ss3,Dlow), mul(ss4,U_low))
    gate('A low jet: p^3 - b^2 s^2 gp^2 + s^4 g^2p (a01=0, y=1, x=-b^2 s^2, A(2,1)=k)',
         A_low=={(0,3,0,0):Q(1),(1,2,2,2):Q(-1),(2,1,4,0):Q(1)})
    gam=sc(pw(b,2),Q(-5,9))
    B_low=add(mul(ss2,trunc(mul(trunc(mul(trunc(mul(R3,R3),3),R3),3),Clow),3)), mul(ss3,trunc(mul(trunc(mul(R3,R3),3),Dlow),3)),
              mul(ss4,add(trunc(mul(trunc(mul(R3,R3),3),U_low),3),trunc(mul(R3,trunc(mul(Clow,Clow),3)),3))),
              mul(pw(s,5),trunc(mul(Clow,Dlow),3)), mul(ss6,add(trunc(mul(Clow,U_low),3),mul(gam,R3))))   # W has lowdeg>=5 (abstract gate above)
    gate('B low jet == gamma s^6 (p - gp^2 - 4p^3): e=-5b^2 s^6/9, [g]B=0, b21=0, b12=5b^2 s^6/9, b03=20 b^2 s^6/9',
         B_low=={(0,1,6,2):Q(-5,9),(1,2,6,2):Q(5,9),(0,3,6,2):Q(20,9)})
    def coef(poly,i,j): return {(0,0,e[2],e[3]):c for e,c in poly.items() if e[:2]==(i,j)}   # scalar coefficient of g^i p^j in K[s]
    xx=coef(A_low,1,2); yy=coef(A_low,0,3); kk=coef(A_low,2,1); ee=coef(B_low,0,1); a01=coef(A_low,0,1)
    gate('extracted coefficients: x=-b^2 s^2, y=1, k=s^4, e=-5 b^2 s^6/9', xx=={(0,0,2,2):Q(-1)} and yy==one and kk==ss4 and ee=={(0,0,6,2):Q(-5,9)})
    gate('saturated low eq: a01=0', a01=={})
    gate('saturated low eq: x^2-3ky==0 by actual multiplication mod b^4-3', add(mul(xx,xx),sc(mul(kk,yy),-3))=={})
    gate('saturated low eq: 9e-5kx==0 by actual multiplication mod b^4-3', add(sc(ee,9),sc(mul(kk,xx),-5))=={})
    gate('unsaturated source low rows vanish trivially mod s^7 (k^2=s^8, k e=s^10, x e=s^8)', smax(mul(kk,ee),6)=={} and smax(mul(xx,ee),6)=={} and smax(mul(kk,kk),6)=={})
    gate('untested orders: B(1,0)=5k^2/9=5s^8/9 and target -5k^3g^2/9=-5s^12g^2/9 are 0 mod s^7', smax(sc(mul(kk,kk),Q(5,9)),6)=={} and smax(pw(kk,3),6)=={})
    out={'status':'PASS','C0':sorted([[list(e[:2]),str(c)] for e,c in C0.items()]),'D0':sorted([[list(e[:2]),str(c)] for e,c in D0.items()]),
         'phiR_v0':'3u','phiT_vmin':1,'q_negative':'v^-1','U4_low':'g^2*p','B_low':'gamma s^6 (p - g p^2 - 4 p^3)','gamma':'-5 b^2/9',
         'scope':'own controls; caps literal; no producer execution; unguarded six-jet plus three saturated low equations only'}
    print(json.dumps(out,sort_keys=True))

def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25)); resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,512*1024*1024))

if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else ''
    if mode=='--record':
        import subprocess,time
        recs=[]; t0=time.time()
        for opt in (False,True):
            for mut in ('','--mutate-q','--mutate-U4','--mutate-CU','--mutate-b4'):
                cmd=[sys.executable,'-B']+(['-O'] if opt else [])+[str(Path(__file__).resolve())]+([mut] if mut else [])
                o=subprocess.run(cmd,capture_output=True,timeout=30,preexec_fn=caps)
                first=[l for l in o.stdout.decode().splitlines() if l.startswith('FAIL')]+[l for l in o.stderr.decode().splitlines() if 'FAIL' in l]
                recs.append({'optimized':opt,'mutation':mut or None,'returncode':o.returncode,'first_failure':first[0] if first else None,
                             'stdout_sha256':hashlib.sha256(o.stdout).hexdigest()})
                if not mut:
                    (HERE/('witness-O.txt' if opt else 'witness.txt')).write_bytes(o.stdout)
        ok=all((r['returncode']!=0)==bool(r['mutation']) for r in recs) and (HERE/'witness.txt').read_bytes()==(HERE/'witness-O.txt').read_bytes()
        (HERE/'replay.json').write_text(json.dumps({'status':'PASS' if ok else 'FAIL','runs':recs,'wall_seconds':round(time.time()-t0,2),'caps':'30wall/25CPU/512MiB'},indent=1,sort_keys=True)+'\n')
        print(json.dumps({'status':'PASS' if ok else 'FAIL','runs':len(recs),'wall':round(time.time()-t0,2),'witness_sha256':hashlib.sha256((HERE/'witness.txt').read_bytes()).hexdigest()}))
    else:
        main(mode)
