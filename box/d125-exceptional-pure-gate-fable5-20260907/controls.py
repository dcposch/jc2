#!/usr/bin/env python3
"""Independent Fable controls for the D125 pure exceptional first-contact packet.
Own stdlib polynomial arithmetic; no producer helper is imported. Polys are dicts
exponent-tuple -> Fraction over variables (g,p,s,t,u,v) [u,v are lift variables]."""
import sys
sys.dont_write_bytecode=True
import ast,hashlib,json,resource,subprocess,random
from fractions import Fraction as Q
from pathlib import Path
HERE=Path(__file__).resolve().parent
NV=6; G,P,S,T,U,V=range(NV)
def mono(i,c=1):
    e=[0]*NV; e[i]=1; return {tuple(e):Q(c)}
def const(c): return {(0,)*NV:Q(c)} if c else {}
def add(*ps):
    r={}
    for q in ps:
        for e,c in q.items():
            r[e]=r.get(e,0)+c
    return {e:c for e,c in r.items() if c}
def scale(p,c): return {e:v*Q(c) for e,v in p.items()} if c else {}
def mul(a,b):
    r={}
    for e1,c1 in a.items():
        for e2,c2 in b.items():
            e=tuple(x+y for x,y in zip(e1,e2)); r[e]=r.get(e,0)+c1*c2
    return {e:c for e,c in r.items() if c}
def pw(p,n):
    r=const(1)
    for _ in range(n): r=mul(r,p)
    return r
def diff(p,i):
    r={}
    for e,c in p.items():
        if e[i]:
            f=list(e); f[i]-=1; r[tuple(f)]=r.get(tuple(f),0)+c*e[i]
    return {e:c for e,c in r.items() if c}
def br(a,b): return add(mul(diff(a,G),diff(b,P)),scale(mul(diff(a,P),diff(b,G)),-1))
def coef(p,i,j): return sum((c for e,c in p.items() if e[G]==i and e[P]==j),Q(0))
def wt(p): return max(5*e[G]-7*e[P] for e in p)
def deg(p): return max(e[G]+e[P] for e in p)
def odd(p): return all((e[G]+e[P])%2==1 for e in p)
def even(p): return all((e[G]+e[P])%2==0 for e in p)
def subst(p,imgs):
    r={}
    for e,c in p.items():
        term=const(c)
        for i,img in imgs.items(): term=mul(term,pw(img,e[i]))
        r=add(r,term)
    return r
def need(ok,msg):
    if not ok: raise RuntimeError('FAIL: '+msg)
def wire(p): return {' '.join(map(str,e)):str(c) for e,c in sorted(p.items())}

def check(mode):
    need(sys.dont_write_bytecode,'bytecode disabled')
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text()))),'zero Assert nodes')
    g,p,s,t=mono(G),mono(P),mono(S),mono(T)
    Vp=add(pw(g,3),pw(p,3),scale(p,-3)); R=mul(pw(p,2),Vp)
    Sp=mul(p,add(pw(p,2),mul(g,p),const(-1))); Z=add(mul(g,p),pw(p,2))
    H=mul(pw(p,2),add(pw(p,3),pw(g,3)))
    # --- 1. weights, V Newton valuation, filtered transfer (W) ---
    need(wt(Vp)==15 and wt(R)==1 and wt(Z)==-2 and wt(Sp)==-7,'literal weights')
    v0=min(e[P] for e in Vp if e[G]==0); need(v0==1 and v0%3!=0,'V(0,p) has p-valuation 1: root valuation 1/3 not integral')
    for e in range(1,9): need((-7*(2*e-1))-(3-15*e)==e+4>0,'quotient weight gap is e+4')
    bad=mul(mul(g,p),Vp)  # unweighted countercontrol gpV
    need(wt(bad)==13 and coef(bad,4,1)==1,'gpV has weight 13 and p-linear coefficient g^4')
    need(all(e[P]>=2 for e in R),'R lies in (p^2): R does not divide gpV')
    need(mul(bad,bad)==mul(mul(pw(g,2),Vp),R),'(gpV)^2 = (g^2 V) R by a 9-term product, no R^2')
    # --- 2. ordinary lift phi and the cubic U rows ---
    u,v=mono(U),mono(V); vinv={(0,0,0,0,0,-1):Q(1)}
    phi={G:vinv,P:add(mul(pw(v,4),u),scale(v,-1),scale(vinv,-1))}
    def lift(q): return subst(q,phi)
    def negpart(q): return {e:c for e,c in q.items() if e[V]<0}
    for name,q in (('R',R),('S',Sp),('Z',Z),('V',Vp)): need(negpart(lift(q))=={},name+' ordinary')
    need({e:c for e,c in lift(R).items() if e[V]==0}==scale(u,3),'phi(R)(u,0)=3u')
    rows={'p':negpart(lift(p)),'p3':negpart(lift(pw(p,3))),'gp2':negpart(lift(mul(g,pw(p,2))))}
    vm1=(0,0,0,0,0,-1); vm3=(0,0,0,0,0,-3)
    need(rows['p']=={vm1:Q(-1)} and rows['p3']=={vm3:Q(-1),vm1:Q(-3)} and rows['gp2']=={vm3:Q(1),vm1:Q(2)},'negative lift rows of p,p^3,gp^2')
    # rows: [v^-3] = -u3+u12 ; [v^-1] = -u1-3u3+2u12 ; solve with u3=1
    u3=1; u12=u3; u1=-3*u3+2*u12
    Usol=add(scale(p,u1),scale(pw(p,3),u3),scale(mul(g,pw(p,2)),u12))
    if mode=='--mutate-drop-vm1-row': u1=0; Usol=add(scale(p,u1),scale(pw(p,3),u3),scale(mul(g,pw(p,2)),u12))
    need(Usol==Sp,'both lift rows force U = u3*S')
    need(negpart(lift(Usol))=={},'solved U is ordinary')
    slots=sorted((i,n-i) for n in (1,3) for i in range(n+1) if 5*i-7*(n-i)<=1)
    need(slots==[(0,1),(0,3),(1,2)],'odd deg<=3 weight<=1 support is p,p^3,gp^2')
    # --- 3. moving reference: R_t = R + (t+3) S, coefficient selections, mixed toy ---
    Rt=add(H,mul(add(t,const(3)),mul(g,pw(p,2))),mul(t,pw(p,3)),scale(mul(add(t,const(3)),p),-1))
    need(add(Rt,scale(R,-1))==mul(add(t,const(3)),Sp),'R_t - R_{-3} = (t+3) S')
    tri13=[(a,b,c) for a in (5,3,1) for b in (5,3,1) for c in (5,3,1) if a+b+c==13]
    tri3=[(a,b,c) for a in (5,3,1) for b in (5,3,1) for c in (5,3,1) if a+b+c==3]
    need(len(tri13)==3 and all(sorted(x)==[3,5,5] for x in tri13) and tri3==[(1,1,1)],'[p13]R_t^3=3t, [p3]R_t^3=-(t+3)^3 by multinomial selection')
    need(coef(R,0,3)==-3 and coef(R,0,5)==1 and coef(Sp,0,3)==1 and coef(Sp,0,1)==-1,'[p3]R=-3,[p5]R=1,[p3]S=1,[p]S=-1 so [p13]R^2S=1')
    # mixed toy: A=R_h^3+aR with h=a, t=h-3 -> F=(ah/t)(R+3S): verify aR - alpha R_h with alpha=-3a/t, formally in t:
    # t*(aR - alpha R_h) = a t R + 3a (R + hS) = a (t+3) R + 3 a h S = a h (R+3S)
    h=add(t,const(3)); lhs=add(mul(t,R),scale(add(R,mul(h,Sp)),3)); rhs=mul(h,add(R,scale(Sp,3)))
    need(lhs==rhs,'mixed-reference residual t*F/a = h(R+3S)')
    F2=scale(add(R,scale(Sp,3)),Q(-1,3))
    need(coef(F2,0,1)==1 and coef(F2,0,3)==0 and coef(F2,1,2)==-1,'F_2 has p-coefficient 1, p^3 zero, gp^2 = -1')
    need(br(R,Sp)!={},'[R,S] nonzero: the toy is not a Jacobian point')
    # --- 4. identity (I) at random NON-formal instances, exact bracket in (g,p) ---
    random.seed(20260907)
    def rpoly(dg,par):
        r={}
        for i in range(dg+1):
            for j in range(dg+1-i):
                if (i+j)%2==par and random.random()<0.6: r=add(r,scale(mul(pw(g,i),pw(p,j)),random.randint(-3,3)))
        return r
    for trial in range(3):
        Rr=add(rpoly(2,1),mul(s,rpoly(1,1))); al=mul(s,const(random.randint(1,3))); be=const(random.randint(-2,2)); ga=mul(pw(s,2),const(random.randint(1,2)))
        Fr=mul(s,rpoly(3,1)); Gr=mul(pw(s,2),rpoly(3,1))
        a=add(scale(pw(Rr,2),3),al); q=add(scale(pw(Rr,2),Q(5,3)),be,scale(al,Q(-5,9)))
        dl=add(ga,scale(mul(be,al),-1),scale(pw(al,2),Q(5,9)))
        if mode=='--mutate-identity-delta-sign': dl=scale(dl,-1)
        A=add(pw(Rr,3),mul(al,Rr),Fr); B=add(pw(Rr,5),mul(be,pw(Rr,3)),mul(ga,Rr),mul(q,Fr),Gr)
        E=add(mul(a,Gr),scale(mul(dl,Fr),-1),scale(mul(Rr,pw(Fr,2)),Q(-5,3)))
        need(br(A,B)==add(br(Rr,E),br(Fr,Gr)),'identity (I) at random moving instance %d'%trial)
    # --- 5. structural (C)/(O) facts for F_j = R C with random even C, deg<=8 ---
    for trial in range(3):
        C=rpoly(8,0); RC=mul(R,C)
        need(coef(RC,0,1)==0 and coef(RC,2,1)==0 and coef(RC,1,2)==0,'RC has no p, g^2p, gp^2 terms')
        need(coef(RC,0,3)==-3*coef(C,0,0) and coef(RC,0,13)==coef(C,0,8),'[p3]RC=-3C(0), [p13]RC=[p8]C')
        need(negpart(lift(RC))=={}==negpart(lift(C)) or (negpart(lift(C))!={} and negpart(lift(RC))!={}),'C ordinary iff RC ordinary at this sample')
    # --- 6. nilpotent survivor: formal (R,Z)=(g,p) chain rule, actual [R,Z], faces, low rows ---
    coefB=Q(5,27) if mode=='--mutate-jet-coefficient' else Q(5,9)
    eps=s; fA=add(pw(g,3),mul(eps,mul(g,p))); fB=add(pw(g,5),scale(mul(eps,mul(pw(g,3),p)),Q(5,3)),scale(mul(pw(eps,2),mul(g,pw(p,2))),coefB))
    need(br(fA,fB)==scale(mul(pw(eps,3),mul(g,pw(p,2))),Q(5,9)),'formal chain-rule bracket is exactly (5/9) eps^3 R Z^2 [R,Z]')
    RZ=mul(R,Z); RZ2=mul(RZ,Z); brRZ=br(R,Z)
    need(brRZ!={} and br(RZ,scale(RZ2,Q(5,9)))==scale(mul(RZ2,brRZ),Q(5,9)),'[F1,G2]=(5/9)RZ^2[R,Z] nonzero: fixture fails at order 3=3j')
    need(even(Z) and Z.get((0,)*NV,0)==0 and coef(Z,0,8)==0 and deg(Z)==2 and all(e[G]<=2*e[P] for e in Z),'Z meets (C): even, C(0)=0, [p8]=0, deg 2 (V does not divide), i<=2j')
    need(odd(RZ) and deg(RZ)==7 and wt(RZ)==-1 and odd(RZ2) and deg(RZ2)==9 and wt(RZ2)==-3,'RZ and RZ^2 support facts')
    need(coef(RZ,1,2)==0 and coef(RZ,0,3)==0 and coef(RZ,0,1)==0 and coef(RZ,2,1)==0,'x=y=[p]A=0 and the k-face of RZ is zero: k=eps would fail the moving A face')
    need(negpart(lift(RZ))=={} and negpart(lift(RZ2))=={},'RZ, RZ^2 ordinary')
    return {'status':'PASS','assert_nodes':0,'R':wire(R),'S':wire(Sp),'Z':wire(Z),'brRZ':wire(brRZ),'lift_rows':{k:wire(v) for k,v in rows.items()},
            'scope':'own stdlib controls; degree<=5 factors, RZ, RZ^2, (gpV)^2, random deg<=8 C times R; no R^2,R^3,R^5,R^2S expansion'}

def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25)); resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,512*1024*1024))

if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else ''
    if mode=='--record':
        modes=[('',None),('--mutate-drop-vm1-row',b'both lift rows force'),('--mutate-identity-delta-sign',b'identity (I)'),('--mutate-jet-coefficient',b'formal chain-rule')]
        recs=[]
        for opt in (False,True):
            for mut,msg in modes:
                out=subprocess.run([sys.executable,'-B']+(['-O'] if opt else [])+[str(Path(__file__).resolve())]+([mut] if mut else []),capture_output=True,timeout=30,preexec_fn=caps)
                need((out.returncode!=0)==bool(mut),'unexpected exit for mode %r'%mut)
                if mut: need(msg in out.stderr,'wrong failure for %r: %r'%(mut,out.stderr[-200:]))
                else: (HERE/('witness-O.json' if opt else 'witness.json')).write_bytes(out.stdout)
                recs.append({'optimized':opt,'mutation':mut or None,'returncode':out.returncode,'stdout_sha256':hashlib.sha256(out.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(out.stderr).hexdigest()})
        need((HERE/'witness.json').read_bytes()==(HERE/'witness-O.json').read_bytes(),'normal/-O witness equality')
        (HERE/'replay.json').write_text(json.dumps({'status':'PASS','runs':recs,'caps':'30wall25CPU512MiB each'},sort_keys=True,indent=2)+'\n')
        print(json.dumps({'status':'PASS','runs':len(recs),'witness_sha256':hashlib.sha256((HERE/'witness.json').read_bytes()).hexdigest()}))
    else: print(json.dumps(check(mode),sort_keys=True,indent=2))
