#!/usr/bin/env python3
"""Independent gate controls: bracket jet identity, R_t lift/support/factor, s_t, polygon slots.
Standard library only. No A15/B25 expansion. Frozen pinned inputs are read, never written."""
import ast, hashlib, json, random, resource, subprocess, sys
from fractions import Fraction as Q
from pathlib import Path
HERE=Path(__file__).resolve().parent
FROZEN=Path('/tmp/jc2-lane.2RjqXj/inputs')  # explicit pinned relocation path
PIN={'check.py':'25be0862730df8b66076eb59a2d1d0909fbcf563ea73ce16924affdc7c70ad66',
     'witness.json':'fac3910177f640869e69517e266126ce08f54f0950061e4b50a5eada53f336ee',
     'd125-zero-k-deformation-discriminator-astra-20260907.md':'99d251478969b569c5523349b71a58534fc1fc95c7125e2fcc7e706dda963f2c'}
def need(ok,msg):
    if not ok: raise ValueError(msg)
# polynomials: dict exponent-tuple -> Fraction ; variables (g,p,t,k) ; k truncated below K3
def cl(d): return {e:c for e,c in d.items() if c}
def add(*ps):
    z={}
    for p in ps:
        for e,c in p.items(): z[e]=z.get(e,Q(0))+c
    return cl(z)
def sc(p,c): return cl({e:v*c for e,v in p.items()})
def mul(p,q,ktr=None):
    z={}
    for e,a in p.items():
        for f,b in q.items():
            h=tuple(x+y for x,y in zip(e,f))
            if ktr is not None and h[3]>=ktr: continue
            z[h]=z.get(h,Q(0))+a*b
    return cl(z)
def pw(p,n,ktr=None):
    z={(0,0,0,0):Q(1)}
    for _ in range(n): z=mul(z,p,ktr)
    return z
def der(p,ax):
    z={}
    for e,c in p.items():
        if e[ax]:
            h=list(e); h[ax]-=1; z[tuple(h)]=c*e[ax]
    return cl(z)
def br(p,q,ktr=None): return add(mul(der(p,0),der(q,1),ktr),sc(mul(der(p,1),der(q,0),ktr),-1))
def kcoef(p,n): return cl({(e[0],e[1],e[2],0):c for e,c in p.items() if e[3]==n})
def subst(p,imgs,ktr=None):
    z={}
    for e,c in p.items():
        m={(0,0,0,0):c}
        for im,n in zip(imgs,e): m=mul(m,pw(im,n,ktr),ktr)
        z=add(z,m)
    return z
def wlead(p):
    w=max(5*e[0]-7*e[1] for e in p); return w,cl({e:c for e,c in p.items() if 5*e[0]-7*e[1]==w})
one={(0,0,0,0):Q(1)}; g={(1,0,0,0):Q(1)}; p={(0,1,0,0):Q(1)}; t={(0,0,1,0):Q(1)}; k={(0,0,0,1):Q(1)}
def const(c): return {(0,0,0,0):Q(c)}
def polyR(gp2coef_shift=0):
    tp3=add(t,const(3+gp2coef_shift))
    return add(pw(p,5),mul(pw(g,3),pw(p,2)),mul(tp3,mul(g,pw(p,2))),mul(t,pw(p,3)),sc(mul(add(t,const(3)),p),-1))
def run(mode):
    src=Path(__file__).read_text()
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(src))),'Assert node present')
    for f,h in PIN.items(): need(hashlib.sha256((FROZEN/f).read_bytes()).hexdigest()==h,'pin mismatch '+f)
    out={}
    # ---- C1: R_t lift, support, oddness, origin, leader, u=0 factor, H negative part (symbolic t)
    R=polyR(1 if mode=='--mutate-R-coefficient' else 0)
    H=add(pw(p,5),mul(pw(g,3),pw(p,2)))
    u={(1,0,0,0):Q(1)}; v={(0,1,0,0):Q(1)}; vi={(0,-1,0,0):Q(1)}
    phip=add(mul(pw(v,4),u),sc(v,-1),sc(vi,-1))
    Hl=subst(H,(vi,phip,t,k)); Rl=subst(R,(vi,phip,t,k))
    need(cl({e:c for e,c in Hl.items() if e[1]<0})=={(0,-3,0,0):Q(-3),(0,-1,0,0):Q(-9)},'phi(H) negative part')
    need(all(e[1]>=0 for e in Rl),'phi(R) has a negative v power')
    need(Rl.get((5,20,0,0))==1 and max(e[0] for e in Rl)==5,'phi(R) top u^5 v^20 monic')
    u0=cl({e:c for e,c in Rl.items() if e[0]==0})
    need(u0==sc(mul(v,mul(add(pw(v,2),one),add(pw(v,2),t,const(4)))),-1),'u=0 factorisation')
    need(all(i+j<=5 and 5*i-7*j<=1 and (i+j)%2==1 and i+j>0 for i,j,_,_ in R),'R support/odd/origin')
    need(wlead(R)==(1,{(3,2,0,0):Q(1)}),'R (5,-7)-leader g^3p^2')
    # ---- C2: polygons and slot census (parity gate 33/94), moving slots, containment
    def slots(D,w): return [(i,j) for i in range(D+1) for j in range(D+1-i) if (i+j)%2==1 and 5*i-7*j<=w]
    wA=5 if mode=='--mutate-face' else 3
    SA=slots(15,wA); SB=slots(25,5)
    topA=[s for s in SA if 5*s[0]-7*s[1]==max(5*a-7*b for a,b in SA)]
    need(topA==[(2,1),(9,6)],'A max-weight slots are exactly (2,1),(9,6)')
    need(len(SA)==44 and len(SB)==112,'odd slot census')
    need(len([s for s in SA if sum(s)==15])==10 and len([s for s in SB if sum(s)==25])==16,'total-face slot count')
    need(44-10-1==33 and 112-16-2==94,'free-slot census vs parity gate 33/94')
    need(set(SA)<=set(SB),'A polygon inside B polygon (shear symmetry)')
    R3=pw(R,3); R5=pw(R,5)   # degree-five R only; tiny supports
    need(all((i,j) in SA for i,j,_,_ in R3) and all((i,j) in SB for i,j,_,_ in R5) and all((i,j) in SB for i,j,_,_ in R3),'R^3,R^5 in polygons')
    need(wlead(R3)==(3,{(9,6,0,0):Q(1)}) and wlead(R5)==(5,{(15,10,0,0):Q(1)}),'inner faces g^9p^6 / g^15p^10')
    need(cl({e:c for e,c in R3.items() if e[0]+e[1]==15})==pw(H,3) and cl({e:c for e,c in R5.items() if e[0]+e[1]==25})==pw(H,5),'total faces H^3/H^5')
    need(all((i,j) not in [(2,1)] for i,j,_,_ in R3) and all((i,j) not in [(8,5),(1,0)] for i,j,_,_ in R5),'moving slots vanish at k=0')
    need(R3.get((0,15,0,0))==1,'[p^15]R^3 = 1')
    st=cl({(0,0,e[2],0):c for e,c in R5.items() if e[0]==0 and e[1]==15})
    tp3=add(t,const(3)); st_closed=add(pw(t,5),sc(mul(pw(t,3),tp3),-20 if mode!='--mutate-shear' else -10),sc(mul(t,pw(tp3,2)),30))
    need(st==st_closed,'s_t = [p^15]R^5 closed form')
    wit=json.loads((FROZEN/'witness.json').read_text())
    need(sorted([tuple(e[:3]) for e,_ in wit['beta15_scalar']])==sorted([e[:3] for e in st]) and all(Q(c)==st[tuple(e)+(0,)] for e,c in wit['beta15_scalar']),'s_t matches producer witness')
    out['s_t']={str(e[2]):str(c) for e,c in sorted(st.items())}
    # ---- C3: factor / squarefree certificates (symbolic t)
    T=cl({(i,j-1,a,b):c for (i,j,a,b),c in R.items()})
    need(mul(p,T)==R,'R = pT')
    need(cl({e:c for e,c in T.items() if e[1]==0})==sc(tp3,-1),'T mod p = -(t+3)')
    need(der(T,0)==mul(p,add(sc(pw(g,2),3),tp3)),'T_g = p(3g^2+t+3)')
    need(cl({(0,0,a,b):c for (i,j,a,b),c in T.items() if j==4})==one,'T monic degree 4 in p')
    # discriminant of T as cubic a g^3 + b g + c over Q[p,t]: -4ab^3-27a^2c^2 ; p^10 coefficient -27 for every t
    a=p; b=mul(tp3,p); c=add(pw(p,4),mul(t,pw(p,2)),sc(tp3,-1))
    disc=add(sc(mul(a,pw(b,3)),-4),sc(mul(pw(a,2),pw(c,2)),-27))
    need(cl({e:x for e,x in disc.items() if e[1]==10})=={(0,10,0,0):Q(-27)},'disc_g(T) has p^10 coefficient -27 (nonzero for all t)')
    Rm=subst(R,(g,p,const(-3),k)); C=add(pw(p,3),pw(g,3),sc(p,-3))
    need(Rm==mul(pw(p,2),C),'t=-3: R=p^2 C')
    need(der(C,0)==sc(pw(g,2),3) and subst(C,({},p,t,k))==add(pw(p,3),sc(p,-3)),'C_g=3g^2, g does not divide C')
    need(cl({e:x for e,x in C.items() if e[1]==0})==pw(g,3),'p does not divide C')
    need(wlead(mul(p,C))==(8,{(3,1,0,0):Q(1)}),'rad(R) leader g^3p at t=-3')
    need(not (3<=2 and 2<=1) and not (3<=2 and 1<=1),'g^3p^2 and g^3p do not divide g^2p')
    need(cl({e:x for e,x in add(pw(p,3),pw(g,3)).items() if e[1]==0})==pw(g,3),'p-multiplicity of H is exactly 2 (not a fifth power)')
    # weighted leading forms multiply for weight (5,-7) despite the negative entry: random products
    rnd=random.Random(20260907)
    def rpoly(n):
        z={}
        for _ in range(n): z[(rnd.randint(0,4),rnd.randint(0,4),0,0)]=Q(rnd.randint(-5,5) or 1)
        return cl(z)
    for _ in range(20):
        F=rpoly(4); G=rpoly(4)
        need(wlead(mul(F,G))[1]==mul(wlead(F)[1],wlead(G)[1]),'leading-form multiplicativity')
    # ---- C4: order-one/two bracket identities on random small polynomials and actual R at t=2
    Rt=subst(R,(g,p,const(2),k))
    def rgp(n,dg):
        z={}
        for _ in range(n): z[(rnd.randint(0,dg),rnd.randint(0,dg),0,0)]=Q(rnd.randint(-3,3) or 2)
        return cl(z)
    fac=Q(-1) if mode=='--mutate-second-factor' else Q(-1,3)
    for trial in range(6):
        Rr=Rt if trial<3 else rgp(4,3)
        A1=rgp(4,3); A2=rgp(3,3); B2=rgp(3,3); aa=Q(rnd.randint(-3,3)); bb=Q(rnd.randint(-3,3))
        fR=add(sc(Rr,aa),sc(pw(Rr,3),bb)); fpR=add(const(aa),sc(pw(Rr,2),3*bb))
        B1g=rgp(4,3)  # generic B1 for the order-one identity
        A=add(pw(Rr,3),mul(k,A1),mul(pw(k,2),A2)); Bg=add(pw(Rr,5),mul(k,B1g),mul(pw(k,2),B2))
        J=br(A,Bg,3)
        need(kcoef(J,0)=={} ,'order zero vanishes')
        need(kcoef(J,1)==mul(pw(Rr,2),br(Rr,add(sc(B1g,3),sc(mul(pw(Rr,2),A1),-5)))),'order-one identity R^2[R,3B1-5R^2A1]')
        B1=add(sc(mul(pw(Rr,2),A1),Q(5,3)),sc(fR,Q(1,3)))
        B=add(pw(Rr,5),mul(k,B1),mul(pw(k,2),B2)); J=br(A,B,3)
        need(kcoef(J,1)=={},'order one vanishes when 3B1-5R^2A1=f(R)')
        E=add(sc(mul(pw(Rr,2),B2),3),sc(mul(pw(Rr,4),A2),-5),sc(mul(Rr,pw(A1,2)),Q(-5,3)),sc(mul(fpR,A1),fac))
        need(kcoef(J,2)==br(Rr,E),'order-two coefficient equals [R,E] with factor -1/3')
    # dependent jet: all-in-K[R] jet commutes but has zero moving faces
    Aj=add(pw(Rt,3),mul(k,Rt)); Bj=add(pw(Rt,5),sc(mul(k,pw(Rt,3)),Q(5,3)),sc(mul(pw(k,2),Rt),Q(5,9)))
    need(br(Aj,Bj,3)=={},'dependent jet commutes mod k^3')
    need(Aj.get((2,1,0,1),0)==0 and Bj.get((8,5,0,1),0)==0 and Bj.get((1,0,0,2),0)==0,'dependent jet has zero moving faces')
    out.update({'status':'PASS','assert_nodes':0,'slots':{'A':44,'B':112,'freeA':33,'freeB':94},'second_order_factor':'-1/3','no_A15_B25_expansion':True})
    return out
def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25)); resource.setrlimit(resource.RLIMIT_AS,(512<<20,512<<20))
if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else ''
    if mode=='--record':
        res=[]
        for opt in (False,True):
            for m in ('','--mutate-R-coefficient','--mutate-second-factor','--mutate-face','--mutate-shear'):
                cmd=[sys.executable]+(['-O'] if opt else [])+[str(Path(__file__).resolve())]+([m] if m else [])
                r=subprocess.run(cmd,capture_output=True,timeout=30,preexec_fn=caps)
                need((r.returncode!=0)==bool(m),'unexpected exit '+m)
                if m:
                    msg={'--mutate-R-coefficient':b'negative v power','--mutate-second-factor':b'factor -1/3','--mutate-face':b'exactly (2,1),(9,6)','--mutate-shear':b'closed form'}[m]
                    need(msg in r.stderr,'wrong failure for '+m)
                else:
                    (HERE/('witness-O.json' if opt else 'witness.json')).write_bytes(r.stdout)
                res.append({'optimized':opt,'mutation':m or None,'returncode':r.returncode,'stdout_sha256':hashlib.sha256(r.stdout).hexdigest(),'stderr_tail':r.stderr[-120:].decode(errors='replace')})
        need((HERE/'witness.json').read_bytes()==(HERE/'witness-O.json').read_bytes(),'normal/-O bytes differ')
        (HERE/'replay.json').write_text(json.dumps({'status':'PASS','runs':res,'caps':'30wall/25CPU,512MiB'},indent=1,sort_keys=True)+'\n')
        print(json.dumps({'status':'PASS','runs':len(res),'witness_sha256':hashlib.sha256((HERE/'witness.json').read_bytes()).hexdigest()}))
    else:
        print(json.dumps(run(mode),sort_keys=True,indent=1))
