#!/usr/bin/env python3
"""Independent Fable controls for the D125 pure-uniform packet (collision, unit parity, Pell, moving identity).
Own stdlib polynomial arithmetic only; no producer helper is imported. Polys are dicts exponent-tuple -> Fraction.
Variables: g p s u v R r L C D W z om al b  (u,v lift variables; R,r,L,C,D,W formal independent symbols;
z projective coordinate; om = omega with om^2+om+1=0; al = sqrt(a); b Pell scalar)."""
import sys
sys.dont_write_bytecode=True
import ast,hashlib,json,resource,subprocess,random
from fractions import Fraction as Q
from pathlib import Path
HERE=Path(__file__).resolve().parent
NAMES='g p s u v R r L C D W z om al b'.split(); NV=len(NAMES)
G,P,S,U,V_,RR,rr,LL,CC,DD,WW,Z,OM,AL,B_=range(NV)
def mono(i,c=1,e=1):
    t=[0]*NV; t[i]=e; return {tuple(t):Q(c)}
def const(c): return {(0,)*NV:Q(c)} if c else {}
def add(*ps):
    out={}
    for q in ps:
        for e,c in q.items(): out[e]=out.get(e,0)+c
    return {e:c for e,c in out.items() if c}
def scale(p,c): return {e:v*Q(c) for e,v in p.items()} if c else {}
def mul(a,b,strunc=None):
    out={}
    for e1,c1 in a.items():
        for e2,c2 in b.items():
            e=tuple(x+y for x,y in zip(e1,e2))
            if strunc is not None and e[S]>=strunc: continue
            out[e]=out.get(e,0)+c1*c2
    return {e:c for e,c in out.items() if c}
def pw(p,n,strunc=None):
    out=const(1)
    for _ in range(n): out=mul(out,p,strunc)
    return out
def diff(p,i):
    out={}
    for e,c in p.items():
        if e[i]:
            f=list(e); f[i]-=1; out[tuple(f)]=out.get(tuple(f),0)+c*e[i]
    return {e:c for e,c in out.items() if c}
def minor(a,b,x,y): return add(mul(diff(a,x),diff(b,y)),scale(mul(diff(a,y),diff(b,x)),-1))
def br(a,b): return minor(a,b,G,P)
def scoef(p,n): return {e:c for e,c in p.items() if e[S]==n}
def sord(p): return min(e[S] for e in p) if p else None
def subst(p,imgs):
    out={}
    for e,c in p.items():
        term=const(c)
        for i,img in imgs.items():
            if e[i]<0: raise RuntimeError('negative exponent substitution not supported')
            term=mul(term,pw(img,e[i]))
        rest=list(e)
        for i in imgs: rest[i]=0
        shift={tuple(rest):Q(1)}
        out=add(out,mul(term,shift))
    return out
def sigma(p): return {e:(c if (e[G]+e[P])%2==0 else -c) for e,c in p.items()}
def fdeg(e): return e[G]+e[P]
def fwt(e): return 5*e[G]-7*e[P]
def fedge(e): return e[G]-2*e[P]
def fmax(p,f): return max(f(e) for e in p)
def fmin(p,f): return min(f(e) for e in p)
def parity(p):
    ds={fdeg(e)%2 for e in p}
    return 'odd' if ds=={1} else 'even' if ds=={0} else 'mixed'
def wire(p): return {' '.join(str(x) for x in e):str(c) for e,c in sorted(p.items())}
def need(ok,msg):
    if not ok: raise RuntimeError('FAIL: '+msg)

def reduce_curve(p):
    """Normal form modulo V=g^3+p^3-3p (g^3 -> 3p-p^3) and om^2+om+1 (om^2 -> -om-1)."""
    pending=dict(p); out={}
    while pending:
        e,c=pending.popitem()
        if not c: continue
        if e[OM]>=2:
            f1=list(e); f1[OM]-=1; f2=list(e); f2[OM]-=2
            pending[tuple(f1)]=pending.get(tuple(f1),0)-c; pending[tuple(f2)]=pending.get(tuple(f2),0)-c
        elif e[G]>=3:
            f1=list(e); f1[G]-=3; f1[P]+=1
            f2=list(e); f2[G]-=3; f2[P]+=3
            pending[tuple(f1)]=pending.get(tuple(f1),0)+3*c
            pending[tuple(f2)]=pending.get(tuple(f2),0)-c
        else: out[e]=out.get(e,0)+c
    return {e:c for e,c in out.items() if c}

def series_sqrt(y,n):
    """y list of Fractions (coeffs of s^0..s^{n-1}), y[0]=9 perfect square: return x with x^2=y mod s^n."""
    x=[Q(0)]*n; x[0]=Q(3)
    for k in range(1,n):
        acc=sum(x[i]*x[k-i] for i in range(1,k))
        x[k]=(y[k]-acc)/(2*x[0])
    return x
def ser_mul(a,b,n):
    out=[Q(0)]*n
    for i,ai in enumerate(a):
        if ai==0: continue
        for j,bj in enumerate(b):
            if i+j<n: out[i+j]+=ai*bj
    return out
def ser_ord(a): return next((i for i,c in enumerate(a) if c),None)

def check(mode):
    need(sys.dont_write_bytecode,'bytecode disabled')
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text()))),'zero Assert nodes')
    rec={}
    g,p,s,u,v=mono(G),mono(P),mono(S),mono(U),mono(V_)
    Rf,rf,Lf=mono(RR),mono(rr),mono(LL)
    # ---------- (1a) universal circuit identity in independent R,r,L ----------
    Cf=add(pw(rf,2),scale(mul(Rf,Lf),-1)); Df=scale(mul(rf,Cf),Q(1,3)); Wf=mul(pw(Cf,2),Lf)
    if mode=='--mutate-W-drop-L': Wf=pw(Cf,2)          # W=C^2: invisible to the producer's L=1 replay
    need(add(scale(pw(Df,2),9),scale(pw(Cf,3),-1))==mul(Rf,Wf) or mode=='--mutate-W-drop-L','universal 9D^2-C^3=RW in Q[R,r,L]')
    # ---------- (1b) universal six-jet: three formal minors vanish mod s^7 ----------
    c4=Q(5,27) if mode=='--mutate-fourth-coefficient' else Q(5,9)
    c6=Q(5,27) if mode=='--mutate-sixth-coefficient' else Q(5,81)
    Duse={} if mode=='--mutate-drop-D' else Df
    def pair(Rx,Cx,Dx,Wx,T=8):
        A=add(pw(Rx,3),mul(pw(s,2),mul(Rx,Cx)),mul(pw(s,3),Dx))
        B=add(pw(Rx,5),scale(mul(pw(s,2),mul(pw(Rx,3),Cx)),Q(5,3)),scale(mul(pw(s,3),mul(pw(Rx,2),Dx)),Q(5,3)),
              scale(mul(pw(s,4),mul(Rx,pw(Cx,2))),c4),scale(mul(pw(s,5),mul(Cx,Dx)),Q(10,9)),scale(mul(pw(s,6),Wx),c6))
        return A,B
    A,B=pair(Rf,Cf,Duse,Wf)
    mins={ 'R,r':minor(A,B,RR,rr),'R,L':minor(A,B,RR,LL),'r,L':minor(A,B,rr,LL)}
    low={k:{e:c for e,c in m.items() if e[S]<=6} for k,m in mins.items()}
    need(all(not m for m in low.values()),'universal collision: all three (R,r,L) minors vanish through s^6')
    need(any(scoef(m,7) for m in mins.values()),'sharpness: some minor has a nonzero s^7 coefficient')
    rec['minor_s7_terms']={k:len(scoef(m,7)) for k,m in mins.items()}
    # B^3-A^5 in Q[R,r,L][s] vanishes mod s^7
    need(not {e:c for e,c in add(pw(B,3,7),scale(pw(A,5,7),-1)).items()},'B^3=A^5 mod s^7 in Q[R,r,L]')
    # ---------- (1c) binomial coefficient identity in independent R,C,D,W ----------
    Ci,Di,Wi=mono(CC),mono(DD),mono(WW)
    Ai,Bi=pair(Rf,Ci,Di,Wi)
    resid=add(pw(Bi,3,7),scale(pw(Ai,5,7),-1))
    target=scale(mul(pw(s,6),mul(pw(Rf,9),add(mul(Rf,Wi),pw(Ci,3),scale(pw(Di,2),-9)))),Q(5,27))
    if mode in ('--mutate-fourth-coefficient','--mutate-sixth-coefficient','--mutate-drop-D'): pass
    else: need(resid==target,'B^3-A^5 = (5/27)s^6 R^9 (RW+C^3-9D^2) mod s^7 with independent R,C,D,W')
    # ---------- (1d) chain-rule glue on a random non-special instance (degree<=5 in g,p) ----------
    rnd=random.Random(20260907)
    def rpoly(d):
        return add(*[scale(mul(pw(g,i),pw(p,j)),rnd.randint(-3,3)) for i in range(d+1) for j in range(d+1-i)]) or const(1)
    inst={RR:rpoly(1),rr:rpoly(1),LL:add(rpoly(1),const(1))}
    Ag,Bg=subst(A,inst),subst(B,inst)
    Jg=br(Ag,Bg)
    glue=add(*[mul(subst(mins[k],inst),br(inst[x],inst[y])) for k,(x,y) in (('R,r',(RR,rr)),('R,L',(RR,LL)),('r,L',(rr,LL)))])
    need(Jg==glue,'chain rule [A,B]=sum minors*[X,Y] on a random instance')
    need(not {e:c for e,c in Jg.items() if e[S]<=6},'random-instance actual bracket vanishes through s^6')
    need(scoef(Jg,7),'random-instance bracket is nonzero at s^7 (collision is a six-jet, not an arc)')
    # ---------- (2) actual source fit from factored circuits; only degree<=5 generators expanded ----------
    Vp=add(pw(g,3),pw(p,3),scale(p,-3)); L=add(g,p); r=mul(p,pw(L,2)); R=mul(pw(p,2),Vp); gL1=add(mul(g,L),const(1)); p3=pw(p,3)
    need(Vp==add(pw(L,3),scale(mul(p,gL1),-3)),'cubic identity V=L^3-3p(gL+1)')
    need(add(pw(L,3),scale(Vp,-1))==scale(mul(p,gL1),3),'L^3-V=3p(gL+1) hence r^2-RL=p^2 L (L^3-V)=3p^3 L(gL+1)')
    facts={'R':R,'L':L,'r':r,'p3':p3,'gL1':gL1}
    F={k:{'deg':fmax(q,fdeg),'wt':fmax(q,fwt),'edge':fmax(q,fedge),'ord':fmin(q,fdeg),'parity':parity(q),'minp':fmin(q,lambda e:e[P])} for k,q in facts.items()}
    need(F['R']=={'deg':5,'wt':1,'edge':-1,'ord':3,'parity':'odd','minp':2},'R generator statistics')
    need(F['L']['parity']=='odd' and F['r']['parity']=='odd' and F['p3']['parity']=='odd' and F['gL1']['parity']=='even','factor parities')
    def circ(*parts):  # product statistics: exact sums (domain), parity by count of odd factors
        d=sum(F[k]['deg'] for k in parts); w=sum(F[k]['wt'] for k in parts); ed=sum(F[k]['edge'] for k in parts)
        o=sum(F[k]['ord'] for k in parts); mp=sum(F[k]['minp'] for k in parts)
        par='odd' if sum(F[k]['parity']=='odd' for k in parts)%2 else 'even'
        return {'deg':d,'wt':w,'edge':ed,'ord':o,'parity':par,'minp':mp}
    Cc=circ('p3','L','gL1'); F['C']=Cc
    Dc=circ('r','C'); F['D']=Dc; Wc=circ('C','C','L'); F['W']=Wc
    need((Cc['deg'],Cc['wt'],Cc['ord'],Cc['parity'])==(6,-6,4,'even'),'C=3p^3L(gL+1): degree 6, weight -6, origin 4, even')
    need((Dc['deg'],Dc['wt'],Dc['ord'],Dc['parity'])==(9,-3,7,'odd'),'D=rC/3: degree 9, weight -3, origin 7, odd')
    need((Wc['deg'],Wc['wt'],Wc['ord'],Wc['parity'])==(13,-7,9,'odd'),'W=C^2L: degree 13, weight -7, origin 9, odd')
    need(Cc['edge']==-3 and F['r']['edge']==0,'edge i-2j: C max -3, r max 0')
    Acorr={'RC':circ('R','C'),'D':Dc}
    Bcorr={'R3C':circ('R','R','R','C'),'R2D':circ('R','R','D'),'RC2':circ('R','C','C'),'CD':circ('C','D'),'W':Wc}
    need([Bcorr[k]['deg'] for k in ('R3C','R2D','RC2','CD','W')]==[21,19,17,15,13],'B correction degrees 21,19,17,15,13')
    need([Bcorr[k]['wt'] for k in ('R3C','R2D','RC2','CD','W')]==[-3,-1,-11,-9,-7],'B correction weights -3,-1,-11,-9,-7')
    for k,st in Acorr.items():
        need(st['parity']=='odd' and st['deg']<15 and st['wt']<3 and st['edge']<=0 and st['ord']>=7,'A correction %s inside polygon, strictly below faces, origin>=7'%k)
    for k,st in Bcorr.items():
        need(st['parity']=='odd' and st['deg']<25 and st['wt']<5 and st['ord']>=7 and st['minp']>5,'B correction %s inside polygon, strictly below faces, origin>=7, p-exponent>5'%k)
    # fixed faces carried by R^3,R^5: top form and weight-top form of R
    top=lambda q,f,m:{e:c for e,c in q.items() if f(e)==m}
    need(top(R,fdeg,5)==mul(pw(p,2),add(pw(p,3),pw(g,3))),'R top form is H=p^2(p^3+g^3)')
    need(top(R,fwt,1)==mul(pw(g,3),pw(p,2)),'R weight-1 form is g^3p^2 (so R^3,R^5 carry g^9p^6,g^15p^10)')
    # ordinary lifts of L,r,R only (Laurent in v)
    phi={G:mono(V_,1,-1),P:add(mul(pw(v,4),u),scale(v,-1),mono(V_,-1,-1))}
    lifts={k:subst(q,phi) for k,q in (('L',L),('r',r),('R',R))}
    need(all(min(e[V_] for e in q)>=0 for q in lifts.values()),'phi(L),phi(r),phi(R) have no negative v power')
    need(lifts['L']==add(mul(pw(v,4),u),scale(v,-1)),'phi(L)=v^4u-v')
    need({e:c for e,c in lifts['R'].items() if e[V_]==0}==scale(u,3),'phi(R)(u,0)=3u')
    # scalar projections on the pure-p restriction (univariate)
    Rp=add(pw(p,5),scale(pw(p,3),-3)); R3p=pw(Rp,3); R5p=pw(Rp,5)
    cf=lambda q,j:sum((c for e,c in q.items() if e[P]==j and e[G]==0),Q(0))
    need(cf(R3p,13)==-9 and cf(R3p,3)==0 and cf(R3p,15)==1 and cf(R5p,15)==-243,'[p^13]R^3=-9 (t=-3,h=0), [p^3]R^3=0 (alpha=0), [p^15]R^3=1, [p^15]R^5=-243')
    need(all(st['ord']>=7 and st['deg']<=11 for st in Acorr.values()),'A corrections cannot touch p^3 or p^13 references')
    rec['circuit_stats']={k:{kk:(vv if not isinstance(vv,Q) else str(vv)) for kk,vv in st.items()} for k,st in {**F,**{'A:'+k:v_ for k,v_ in Acorr.items()},**{'B:'+k:v_ for k,v_ in Bcorr.items()}}.items()}
    # ---------- (3) projective closure E: smoothness certificate, infinity points, sigma ----------
    z=mono(Z); Fz=add(pw(g,3),pw(p,3),scale(mul(p,pw(z,2)),-3))
    J1,J2,J3=diff(Fz,G),diff(Fz,P),diff(Fz,Z)
    need(J1==scale(pw(g,2),3) and J2==add(scale(pw(p,2),3),scale(pw(z,2),-3)) and J3==scale(mul(p,z),-6),'Jacobian generators of E')
    need(pw(p,3)==add(mul(p,scale(J2,Q(1,3))),mul(z,scale(J3,Q(-1,6)))),'p^3 in Jacobian ideal')
    need(pw(z,3)==add(mul(z,scale(J2,Q(-1,3))),mul(p,scale(J3,Q(-1,6)))),'z^3 in Jacobian ideal')
    need(pw(g,2)==scale(J1,Q(1,3)),'g^2 in Jacobian ideal  => singular locus empty in P^2')
    om=mono(OM); L0=add(g,p); L1=add(g,mul(om,p)); L2=add(g,mul(pw(om,2),p))
    prod=mul(mul(L0,L1),L2)
    # reduce only om^2 (not V) to test the factorization g^3+p^3=L0L1L2 as polynomials
    def red_om(q):
        pending=dict(q); out={}
        while pending:
            e,c=pending.popitem()
            if not c: continue
            if e[OM]>=2:
                f1=list(e); f1[OM]-=1; f2=list(e); f2[OM]-=2
                pending[tuple(f1)]=pending.get(tuple(f1),0)-c; pending[tuple(f2)]=pending.get(tuple(f2),0)-c
            else: out[e]=out.get(e,0)+c
        return {e:c for e,c in out.items() if c}
    need(red_om(prod)==add(pw(g,3),pw(p,3)),'g^3+p^3=L0 L1 L2 over om^2+om+1=0: three distinct infinity points')
    need(sigma(Fz)==scale(Fz,-1) and not {e:c for e,c in Fz.items() if e[G]==0 and e[P]==0},'sigma preserves E and E passes through the affine origin')
    # ---------- (4) genuine nonconstant even unit and inverse; countercontrols ----------
    Uu=add(const(1),scale(mul(add(const(1),scale(om,-1)),mul(L0,L2)),Q(1,3)))
    Uinv=add(const(1),scale(mul(add(om,const(-1)),mul(L1,L2)),Q(1,3)))
    if mode=='--mutate-unit-object': Uu=add(Uu,g)
    if mode=='--mutate-unit-scalar': Uu=add(const(1),scale(mul(add(const(1),scale(om,-1)),mul(L0,L2)),Q(1,2)))
    need(reduce_curve(mul(Uu,Uinv))==const(1),'U*Uinv=1 modulo (V, om^2+om+1)')
    need(reduce_curve(add(mul(L1,Uu),scale(L0,-1)))=={},'L1*U=L0 on V: U is the ratio L0/L1')
    need(reduce_curve(add(mul(mul(L0,L1),L2),scale(p,-3)))=={},'L0L1L2=3p on V')
    nfU=reduce_curve(Uu)
    need(any(fdeg(e)>0 for e in nfU) and parity(Uu)=='even' and sigma(Uu)==Uu,'U nonconstant, even, sigma-fixed')
    need({e:c for e,c in nfU.items() if fdeg(e)==0}==const(1),'U(O)=1 at the fixed affine origin')
    need(sigma(L0)==scale(L0,-1) and reduce_curve(L0)=={e:c for e,c in L0.items()} and not {e:c for e,c in L0.items() if fdeg(e)==0},'odd regular L0 is not sigma-fixed and vanishes at O: parity lemma is about units only')
    # ---------- (5) Pell lemma algebra with retained scalars a=al^2, b ----------
    al,bb,Cs,Ds=mono(AL),mono(B_),mono(CC),mono(DD); a=pw(al,2)
    Up=add(scale(mul(a,Cs),2),bb,scale(mul(al,Ds),2)); Um=add(scale(mul(a,Cs),2),bb,scale(mul(al,Ds),-2))
    pell=add(pw(Ds,2),scale(mul(Cs,add(mul(a,Cs),bb)),-1))
    need(mul(Up,Um)==add(pw(bb,2),scale(mul(a,pell),-4)),'U+ U- = b^2 - 4a(D^2-C(aC+b))')
    need(add(Up,scale(Um,-1))==scale(mul(al,Ds),4),'U+ - U- = 4 sqrt(a) D: parity-equal units force D=0')
    need(subst(Up,{DD:scale(Ds,-1)})==Um,'sigma (D->-D, C fixed) exchanges U+ and U-')
    need(add(pw(Ds,2),scale(mul(a,pw(Cs,2)),-1))==mul(add(Ds,scale(mul(al,Cs),-1)),add(Ds,mul(al,Cs))),'b=0: D^2-aC^2=(D-sqrt(a)C)(D+sqrt(a)C)')
    need(reduce_curve(add(pw(p,2),scale(mul(scale(pw(p,2),Q(1,2)),const(2)),-1)))=={} and parity(pw(p,2))=='even','a=0,b=2 witness C=p^2/2, D=p satisfies D^2=bC: no obstruction at a=0')
    # ---------- (6) exact moving identity (I) on a random moving instance ----------
    R0=rpoly(2); R1=rpoly(1); Rs=add(R0,mul(s,R1))
    alp=add(scale(s,2),scale(pw(s,2),-1)); bet=add(const(1),scale(s,3)); gam=add(scale(s,1),scale(pw(s,3),2))
    Fm=add(mul(pw(s,2),rpoly(2)),mul(pw(s,3),rpoly(2))); Gm=add(mul(pw(s,3),rpoly(2)),mul(pw(s,4),rpoly(2)))
    a_s=add(scale(pw(Rs,2),3),alp); q_s=add(scale(pw(Rs,2),Q(5,3)),bet,scale(alp,Q(-5,9)))
    d_s=add(gam,scale(mul(bet,alp),-1),scale(pw(alp,2),Q(5,9)))
    Am=add(pw(Rs,3),mul(alp,Rs),Fm); Bm=add(pw(Rs,5),mul(bet,pw(Rs,3)),mul(gam,Rs),mul(q_s,Fm),Gm)
    a_used=scale(pw(Rs,2),3) if mode=='--mutate-omit-alphaG' else a_s
    d_used={} if mode=='--mutate-omit-deltaF' else d_s
    R_used=R0 if mode=='--mutate-freeze-R' else Rs
    E=add(mul(a_used,Gm),scale(mul(d_used,Fm),-1),scale(mul(R_used,pw(Fm,2)),Q(-5,3)))
    rhs=add(br(R_used,E),({} if mode=='--mutate-omit-FG' else br(Fm,Gm)))
    need(br(Am,Bm)==rhs,'exact moving identity [A,B]=[R_s,aG-deltaF-(5/3)R_sF^2]+[F,G]')
    need(br(R0,R1) and br(Fm,Gm) and alp and d_s,'moving instance is genuinely moving with nonzero alpha,delta,[F,G]')
    # ---------- (7) the four displayed scalar conditions do not bound ord(alpha) ----------
    n=14; j=2
    def ser(coefs): 
        out=[Q(0)]*n
        for i,c in coefs.items(): out[i]=Q(c)
        return out
    k=ser({5:-1}); alpha=ser({1:1}); h=ser({2:1}); t=ser({0:-3,2:1})
    y=[-c for c in ser_mul(ser_mul(h,h,n),h,n)]; at=ser_mul(alpha,t,n); y=[y[i]+at[i] for i in range(n)]
    three_ky=[3*c for c in ser_mul(k,y,n)]
    need(ser_ord(three_ky)==6,'3ky has order 6')
    unit=[three_ky[i+6] for i in range(n-6)]+[Q(0)]*6
    need(unit[0]==9,'3ky/s^6 starts at 9')
    xr=series_sqrt(unit,n-6); x=[Q(0)]*3+xr+[Q(0)]*3; x=x[:n]
    xx=ser_mul(x,x,n); need(all(xx[i]==three_ky[i] for i in range(n-3)),'x^2=3ky through the truncation')
    ah=ser_mul(alpha,h,n)
    need(ser_ord(ah)==3>j and ser_ord(x)==3>j and ser_ord(alpha)==1<j and ser_ord(k)==5>j,'countermodel: ord(alpha h)>j, ord(x)>j, x^2=3ky, y=-h^3+alpha t, yet ord(alpha)=1<j=2')
    # y-cancellation instance: h=s, alpha=h^3/t so y=0 identically
    h2=ser({1:1}); tt=ser({0:-3,1:1}); inv=[Q(0)]*n; inv[0]=Q(1,tt[0])
    for i in range(1,n): inv[i]=-sum(tt[m]*inv[i-m] for m in range(1,min(i,len(tt)-1)+1) if m<len(tt))/tt[0]
    al2=ser_mul(ser_mul(ser_mul(h2,h2,n),h2,n),inv,n)
    y2=[-c for c in ser_mul(ser_mul(h2,h2,n),h2,n)]; at2=ser_mul(al2,tt,n); y2=[y2[i]+at2[i] for i in range(n)]
    need(all(c==0 for c in y2) and ser_ord(al2)==3,'y=-h^3+alpha t cancels identically with ord(alpha)=3, x=0')
    rec['status']='PASS'; rec['assert_nodes']=0
    rec['unit_normal_form']=wire(nfU); rec['lift_L']=wire(lifts['L'])
    rec['scope']='universal (R,r,L) six-jet collision, factored source fit, E smoothness/unit parity, Pell algebra, moving identity, scalar-order countermodels; no guarded point, arc or exclusion'
    return rec

def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25)); resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,512*1024*1024))

if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else ''
    if mode=='--record':
        modes=[('',None),('--mutate-W-drop-L',b'universal collision'),('--mutate-sixth-coefficient',b'universal collision'),
               ('--mutate-fourth-coefficient',b'universal collision'),('--mutate-drop-D',b'universal collision'),
               ('--mutate-unit-object',b'U*Uinv=1'),('--mutate-unit-scalar',b'U*Uinv=1'),
               ('--mutate-omit-alphaG',b'exact moving identity'),('--mutate-omit-deltaF',b'exact moving identity'),
               ('--mutate-freeze-R',b'exact moving identity'),('--mutate-omit-FG',b'exact moving identity')]
        records=[]
        for opt in (False,True):
            for mutation,msg in modes:
                out=subprocess.run([sys.executable,'-B']+(['-O'] if opt else [])+[str(Path(__file__).resolve())]+([mutation] if mutation else []),capture_output=True,timeout=30,preexec_fn=caps)
                need((out.returncode!=0)==bool(mutation),'unexpected control exit for %r'%mutation)
                if mutation: need(msg in out.stderr,'wrong mutation failure for %r'%mutation)
                else:
                    with (HERE/('witness-O.json' if opt else 'witness.json')).open('xb') as f: f.write(out.stdout)
                records.append({'optimized':opt,'mutation':mutation or None,'returncode':out.returncode,
                                'stdout_sha256':hashlib.sha256(out.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(out.stderr).hexdigest(),
                                'stderr_tail':out.stderr.decode(errors='replace').strip().splitlines()[-1:] if out.stderr else []})
        need((HERE/'witness.json').read_bytes()==(HERE/'witness-O.json').read_bytes(),'normal -O witness equality')
        with (HERE/'replay.json').open('x') as f: json.dump({'status':'PASS','runs':records,'caps':'30wall25CPU512MiB each','writers_finished':True},f,sort_keys=True,indent=2); f.write('\n')
        print(json.dumps({'status':'PASS','runs':len(records),'witness_sha256':hashlib.sha256((HERE/'witness.json').read_bytes()).hexdigest()}))
    else: print(json.dumps(check(mode),sort_keys=True,indent=2))
