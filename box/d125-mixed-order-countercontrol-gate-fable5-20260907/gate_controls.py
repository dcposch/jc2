#!/usr/bin/env python3
"""Independent stdlib gate controls: toy R,S bracket, mixed-order identities, actual degree<=5 generators only."""
import sys
sys.dont_write_bytecode=True
import ast, json, hashlib, random, resource, subprocess
from fractions import Fraction as Q
from pathlib import Path
HERE=Path(__file__).resolve().parent
class Fail(Exception): pass
def need(c,m):
    if not c: raise Fail(m)
def add(*ps):
    r={}
    for p in ps:
        for e,c in p.items():
            v=r.get(e,Q(0))+c
            if v: r[e]=v
            else: r.pop(e,None)
    return r
def scale(p,k): return {e:c*k for e,c in p.items()} if k else {}
def mul(a,b):
    r={}
    for e1,c1 in a.items():
        for e2,c2 in b.items():
            e=tuple(x+y for x,y in zip(e1,e2)); v=r.get(e,Q(0))+c1*c2
            if v: r[e]=v
            else: r.pop(e,None)
    return r
def power(p,n):
    r=None
    for _ in range(n): r=p if r is None else mul(r,p)
    return r
def deriv(p,i):
    r={}
    for e,c in p.items():
        if e[i]:
            f=list(e); f[i]-=1; r[tuple(f)]=c*e[i]
    return r
def bracket(a,b,i=0,j=1): return add(mul(deriv(a,i),deriv(b,j)),scale(mul(deriv(a,j),deriv(b,i)),-1))
def var(n,i,k=1):
    e=[0]*n; e[i]=k; return {tuple(e):Q(1)}
def trunc(p,i,m): return {e:c for e,c in p.items() if e[i]<m}
def coef(p,e): return p.get(e,Q(0))
def randpoly(n,rng,deg=2,terms=4):
    r={}
    for _ in range(terms):
        e=tuple(rng.randint(0,deg) for _ in range(n)); r[e]=r.get(e,Q(0))+Q(rng.randint(-5,5))
    return {e:c for e,c in r.items() if c}
def check(mode):
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text()))),'Assert node')
    out={'mode':mode or 'positive'}
    # ---- C1: identities (1),(2) with random R,U,V,W in vars (x,y,s); j=2 ----
    rng=random.Random(20260907); j=2
    R,U,V,W=(randpoly(3,rng) for _ in range(4)); s=var(3,2); sj=power(s,j)
    A=add(power(R,3),mul(sj,U)); B=add(power(R,5),mul(sj,V)); Z=add(scale(V,3),scale(mul(power(R,2),U),-5))
    need(bracket(A,B)==add(mul(mul(sj,power(R,2)),bracket(R,Z)),mul(power(sj,2),bracket(U,V))),'identity (1) fails')
    V2=scale(add(mul(sj,W),scale(mul(power(R,2),U),5)),Q(1,3)); B2=add(power(R,5),mul(sj,V2))
    lhs=add(bracket(R,add(mul(power(R,2),W),scale(mul(R,power(U,2)),Q(-5,3)))),scale(mul(sj,bracket(U,W)),Q(1,3)))
    need(mul(power(sj,2),lhs)==bracket(A,B2),'identity (2) fails')
    out['identities_random']='(1),(2) hold with 4-term random R,U,V,W'
    # ---- C2: toy in independent R,S,s ----
    Rv=var(3,0); Sv=var(3,1)
    At=add(power(Rv,3),scale(mul(power(s,2),mul(Rv,power(Sv,2))),9),scale(mul(power(s,3),power(Sv,3)),9))
    Bt=add(power(Rv,5),scale(mul(power(s,2),mul(power(Rv,3),power(Sv,2))),15),scale(mul(power(s,3),mul(power(Rv,2),power(Sv,3))),15),
           scale(mul(power(s,4),mul(Rv,power(Sv,4))),45),scale(mul(power(s,5),power(Sv,5)),90))
    if mode=='--mutate-drop-mixed-orders':
        At=add(At,scale(mul(power(s,3),power(Sv,3)),-9)); Bt=add(Bt,scale(mul(power(s,3),mul(power(Rv,2),power(Sv,3))),-15),scale(mul(power(s,5),power(Sv,5)),-90))
    J=bracket(At,Bt)
    need(trunc(J,2,7)=={},'bracket nonzero below order seven')
    need(J=={(0,6,7):Q(2835)},'bracket is not exactly 2835 s^7 S^6')
    if mode=='--mutate-full-arc-claim': need(J=={},'finite toy is not a full commuting arc')
    Ut=add(scale(mul(Rv,power(Sv,2)),9),scale(mul(s,power(Sv,3)),9)); Vt=scale(add(Bt,scale(power(Rv,5),-1)),1); Vt={(a,b,c-2):v for (a,b,c),v in Vt.items()}
    Zt=add(scale(Vt,3),scale(mul(power(Rv,2),Ut),-5))
    need(trunc(Zt,2,2)=={},'Z not zero mod s^2'); Wt={(a,b,c-2):v for (a,b,c),v in Zt.items()}
    need(Wt==add(scale(mul(Rv,power(Sv,4)),135),scale(mul(s,power(Sv,5)),270)),'W mismatch')
    modR=lambda p:{e:c for e,c in p.items() if e[0]==0}
    need(trunc(modR(mul(Ut,Ut)),2,2)=={},'U^2 not in (R,s^2)')
    need(modR(Ut)=={(0,3,1):Q(9)},'U mod R should be 9 s S^3: divisible by s^1 only')
    need(trunc(modR(Ut),2,2)!={},'U in (R,s^2) would be false')
    need(mul(power(sj,2),add(bracket(Rv,add(mul(power(Rv,2),Wt),scale(mul(Rv,power(Ut,2)),Q(-5,3)))),scale(mul(sj,bracket(Ut,Wt)),Q(1,3))))==J,'toy identity (2)')
    C=scale(power(Sv,2),9); D=scale(power(Sv,3),9)
    need(add(scale(power(D,2),Q(5,9)),scale(power(C,3),Q(-5,81)))=={},'square/cube cancellation')
    out['toy_bracket']=[[list(e),str(c)] for e,c in J.items()]
    # ---- C3: actual generators in (g,p,h), t=h-3 ----
    g=var(3,0); p=var(3,1); h=var(3,2); t=add(h,scale(var(3,0,0),-3)); one=var(3,0,0)
    H=add(power(p,5),mul(power(g,3),power(p,2)))
    Ra=add(H,mul(h,mul(g,power(p,2))),mul(t,power(p,3)),scale(mul(h,p),-1))
    Sa=add(power(p,3),mul(g,power(p,2)),scale(p,-1))
    need(deriv(Ra,2)==Sa,'S is not d/dt R_t')
    supp=lambda P:{(i,j) for (i,j,k) in P}
    stats=lambda P:(max(i+j for i,j in supp(P)),max(5*i-7*j for i,j in supp(P)),max(i-2*j for i,j in supp(P)),min(j for i,j in supp(P)),all((i+j)%2 for i,j in supp(P)))
    need(stats(Ra)==(5,1,-1,1,True) and stats(Sa)==(3,-7,-2,1,True),'generator support stats')
    need({e for e in Ra if e[0]+e[1]==5}=={(0,5,0),(3,2,0)} and {e for e in Ra if 5*e[0]-7*e[1]==1}=={(3,2,0)},'top faces of R are H and g^3p^2')
    # ordinary lifts: g->v^-1, p->v^4 u - v - v^-1 in vars (u,v,h)
    u=var(3,0); v=var(3,1); vi=var(3,1,-1); hh=var(3,2)
    phi=lambda P:add(*[scale(mul(mul(power(vi,i) if i else var(3,0,0),power(add(mul(power(v,4),u),scale(v,-1),scale(vi,-1)),j) if j else var(3,0,0)),power(hh,k) if k else var(3,0,0)),c) for (i,j,k),c in P.items()])
    for P in (Ra,Sa): need(min(e[1] for e in phi(P))>=0,'generator lift not ordinary')
    rows={}
    for name,terms,degree,weight,pv in (('A',[(3,0,0),(1,2,2),(0,3,3)],15,3,3),('B',[(5,0,0),(3,2,2),(2,3,3),(1,4,4),(0,5,5)],25,5,5)):
        lst=[]
        for r,z,order in terms:
            deg=5*r+3*z; w=r-7*z; ell=-r-2*z; pval=r+z
            need((r+z)%2==1 and deg<=degree and w<=weight and pval>=pv and ell<=-1,'factored support row')
            if order: need(deg<degree and w<weight,'correction touches a fixed face')
            lst.append([r,z,order,deg,w,ell,pval])
        rows[name]=lst
    out['factored_rows']=rows
    # y(s)=[p^3]A: from truncated products only (degree<=13, never R^3)
    RS2=mul(Ra,power(Sa,2))
    need({e:c for e,c in RS2.items() if e[0]==0 and e[1]==3}=={(0,3,1):Q(-1)},'[p^3] RS^2 must be -h')
    need(mul(power(Ra,2),Sa) and {e:c for e,c in mul(power(Ra,2),Sa).items() if e[0]==0 and e[1]==3}=={(0,3,2):Q(-1)},'[p^3] R^2 S must be -h^2')
    # [p^3]R^3 = (-h)^3 by lowest p-order (R = -h p + O(p^2)): no expansion needed
    out['y_series']='-h^3 - 9h s^2 - 9 s^3 ; at h=0 (t=-3): -9 s^3, y0=0 not a unit, cube root of 9 needed'
    # ---- C4: formal recentering with independent R,S and Laurent h ----
    R4=var(4,0); S4=var(4,1); h4=var(4,2); hi=var(4,2,-1); s4=var(4,3)
    ts=add(scale(mul(hi,power(s4,2)),3),scale(mul(power(hi,2),power(s4,3)),3))
    cube=power(add(h4,ts),3)
    need(trunc(cube,3,4)==add(power(h4,3),scale(mul(h4,power(s4,2)),9),scale(power(s4,3),9)),'moving reference cube through s^3')
    A4=add(power(R4,3),scale(mul(power(s4,2),mul(R4,power(S4,2))),9),scale(mul(power(s4,3),power(S4,3)),9))
    F=trunc(add(A4,scale(power(add(R4,mul(ts,S4)),3),-1)),3,4)
    F2={e[:3]:c for e,c in F.items() if e[3]==2}; F0={e:c for e,c in F.items() if e[3]<2}
    need(F0=={},'F must start at s^2')
    need(F2=={(1,2,0):Q(9),(2,1,-1):Q(-9)},'F2 formal = 9RS^2 - (9/h)R^2 S')
    # actual F2 at h=3 (t=0) and h=1: not in span{R, R^2 S}
    for hv in (Q(3),Q(1),Q(-2)):
        ev=lambda P:add(*[{(i,j,0):c*hv**k} for (i,j,k),c in P.items()]) if P else {}
        Rh=ev(Ra); F2a=add(scale(mul(Rh,power(Sa,2)),9),scale(mul(power(Rh,2),Sa),-9/hv))
        need(F2a!={} and coef(F2a,(0,1,0))==0 and coef(F2a,(0,3,0))==0 and coef(F2a,(1,2,0))==0,'F2 low slots')
        need(coef(Rh,(0,1,0))==-hv,'[p]R=-h forces c=0')
        R2S=mul(power(Rh,2),Sa); m0=next(iter(R2S)); lam=coef(F2a,m0)/R2S[m0]
        need(add(F2a,scale(R2S,-lam))!={},'F2 proportional to R^2 S')
        need(add(scale(Sa,hv),scale(Rh,-1))==add(scale(power(p,3),3),scale(H,-1)) if hv==Q(3) else True,'hS-R=3p^3-H')
    need(add(mul(h,Sa),scale(Ra,-1))==add(scale(power(p,3),3),scale(H,-1)),'hS-R=3p^3-H symbolic')
    # x=[gp^2]A=0 identically by p-valuation
    need(min(e[1] for e in Ra)>=1 and min(e[1] for e in Sa)>=1,'R,S divisible by p'); x2=Q(0)
    if mode=='--mutate-guarded-s4-survivor': need(x2*x2==-3*Q(3)**3,'x=0 cannot meet x2^2=-3h^3 at h=3')
    out['x_gp2']='0 identically (p^3 | A); x2^2=-3h^3 fails for h!=0, vacuous at h=0'
    # order-7 obstruction: [R,S]!=0, chain-rule instance, value 14
    JRS=bracket(Ra,Sa); need(JRS!={},'[R,S]=0'); need(bracket(power(Ra,2),Sa)==scale(mul(Ra,JRS),2),'chain rule instance')
    val=sum(c*Q(3)**k for (i,j,k),c in JRS.items()); need(val==14,'[R,S](1,1,t=0)!=14')
    need(sum(c*Q(3)**k for (i,j,k),c in Sa.items())==1,'S(1,1)!=1')
    out['JRS_terms']=len(JRS); out['JRS_at_1_1_t0']='14'
    out['status']='PASS'; return out
def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25)); resource.setrlimit(resource.RLIMIT_AS,(512<<20,512<<20))
if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else ''
    if mode=='--record':
        modes=['','--mutate-drop-mixed-orders','--mutate-full-arc-claim','--mutate-guarded-s4-survivor']
        msgs=[None,b'bracket nonzero below order seven',b'finite toy is not a full commuting arc',b'x=0 cannot meet']
        recs=[]
        for opt in (False,True):
            for m,msg in zip(modes,msgs):
                cmd=[sys.executable,'-B']+(['-O'] if opt else [])+[str(Path(__file__).resolve())]+([m] if m else [])
                r=subprocess.run(cmd,capture_output=True,timeout=30,preexec_fn=caps)
                need((r.returncode!=0)==bool(m),'unexpected status '+repr(m)+r.stderr.decode()[-300:])
                if m: need(msg in r.stderr,'wrong first failure: '+r.stderr.decode()[-200:])
                else: (HERE/('witness-O.json' if opt else 'witness.json')).write_bytes(r.stdout)
                recs.append({'optimized':opt,'mutation':m or None,'rc':r.returncode,'stdout_sha256':hashlib.sha256(r.stdout).hexdigest(),'stderr_tail':r.stderr.decode()[-120:]})
        need((HERE/'witness.json').read_bytes()==(HERE/'witness-O.json').read_bytes(),'normal/-O differ')
        (HERE/'replay.json').write_text(json.dumps({'status':'PASS','runs':recs,'caps':'30 wall/25 CPU s, 512 MiB'},indent=1,sort_keys=True)+'\n')
        print(json.dumps({'status':'PASS','runs':len(recs),'witness_sha256':hashlib.sha256((HERE/'witness.json').read_bytes()).hexdigest()}))
    else: print(json.dumps(check(mode),sort_keys=True,indent=1))
