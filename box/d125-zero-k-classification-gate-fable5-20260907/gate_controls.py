#!/usr/bin/env python3
"""Compliant replacement controls for the zero-k classification gate.
Stdlib only. Reads frozen pinned inputs; never writes them. Expands only the
degree-five generator/R_t, lattice censuses from the literal client vertices,
combinatorial [p^15] triples, and bracket identities with R=g (degree 1).
No R_t^3, no R_t^5, no degree-15/25 pair, no 803-row stream, no CAS."""
import ast, hashlib, json, random, resource, subprocess, sys
from fractions import Fraction as Q
from pathlib import Path
HERE=Path(__file__).resolve().parent
FROZEN=Path('/tmp/jc2-lane.3223i6/inputs')
PIN={'d125-zero-k-boundary-classification-astra-20260907.md':'129947ee5a370991864a52936d1936179ec9c38efdf0fd80de989e8ed57237a2',
 'check.py':'61226b6022415eccb0a966602522bb8c2e25a1e8c78393cfcdc3af009bae5554',
 'final-witness.json':'fc345a150a1946c502cd0ad0f7dd5d5a34ecb16e5ef5bf317bb4a864eb4c0a7a',
 'client.py':'ec2fa2d1e23bc16bc07c9208f648e3b17561cbfddaaf04fed28d7ffc9a428d53',
 'd125-zero-k-deformation-gate-fable5-20260907.md':'9d6f594f8f150621b4c85bc31ffbfe221e77ddfe0ee1d3d0acaa8a892e17a97a',
 'gate_controls.py':'953455a9f20a0288da96066084ca0d579edcfc620d81fcf96f139eb1163381e5',
 'd125-zero-k-deformation-discriminator-astra-20260907.md':'99d251478969b569c5523349b71a58534fc1fc95c7125e2fcc7e706dda963f2c'}
def need(ok,msg):
    if not ok: raise ValueError(msg)
# polynomials: dict exponent-tuple -> Fraction over variables (g,p,a,b,c,k)
Z=(0,)*6
def cl(d): return {e:c for e,c in d.items() if c}
def add(*ps):
    z={}
    for p in ps:
        for e,c in p.items(): z[e]=z.get(e,Q(0))+c
    return cl(z)
def sc(p,c): return cl({e:v*c for e,v in p.items()})
def mul(p,q,ktr=None):
    z={}
    for e,x in p.items():
        for f,y in q.items():
            h=tuple(u+v for u,v in zip(e,f))
            if ktr is not None and h[5]>=ktr: continue
            z[h]=z.get(h,Q(0))+x*y
    return cl(z)
def pw(p,n,ktr=None):
    if n<0:
        need(len(p)==1,'negative power of non-monomial'); (e,c),=p.items(); return {tuple(n*x for x in e):c**n}
    z={Z:Q(1)}
    for _ in range(n): z=mul(z,p,ktr)
    return z
def var(i):
    e=[0]*6; e[i]=1; return {tuple(e):Q(1)}
def const(c): return {Z:Q(c)}
def der(p,ax):
    z={}
    for e,c in p.items():
        if e[ax]:
            h=list(e); h[ax]-=1; z[tuple(h)]=c*e[ax]
    return cl(z)
def br(p,q,ktr=None): return add(mul(der(p,0),der(q,1),ktr),sc(mul(der(p,1),der(q,0),ktr),-1))
def subst(p,imgs,ktr=None):
    z={}
    for e,c in p.items():
        m={Z:c}
        for im,n in zip(imgs,e): m=mul(m,pw(im,n,ktr),ktr)
        z=add(z,m)
    return z
def kco(p,n): return cl({e[:5]+(0,):c for e,c in p.items() if e[5]==n})
def wlead(p):
    w=max(5*e[0]-7*e[1] for e in p); return w,cl({e:c for e,c in p.items() if 5*e[0]-7*e[1]==w})
g,p,a,b,c,k=[var(i) for i in range(6)]; one=const(1)
def run(mode):
    src=Path(__file__).read_text()
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(src))),'Assert node present')
    for f,h in PIN.items(): need(hashlib.sha256((FROZEN/f).read_bytes()).hexdigest()==h,'pin mismatch '+f)
    out={}
    # ---- C1: literal client polygon fit (vertices parsed from the frozen client.py AST)
    tree=ast.parse((FROZEN/'client.py').read_text())
    lit={n.targets[0].id:ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id in ('VERTICES','INNER')}
    VA,VB=lit['VERTICES']['unequal']; need(lit['INNER']['unequal']==(5,-7),'inner weight (5,-7)')
    need(VA==((0,0),(0,15),(9,6),(2,1)) and VB==((0,0),(0,25),(15,10),(1,0)),'literal unequal vertices')
    def lattice(vs):  # same convention as client.lattice: closed polygon, cross-product sign test
        ed=list(zip(vs,vs[1:]+vs[:1]))
        def inside(i,j):
            cr=[(B[0]-A[0])*(j-A[1])-(B[1]-A[1])*(i-A[0]) for A,B in ed]
            return all(t>=0 for t in cr) or all(t<=0 for t in cr)
        return sorted((i,j) for i in range(max(v[0] for v in vs)+1) for j in range(max(v[1] for v in vs)+1) if inside(i,j))
    LA=lattice(VA); LB=lattice(VB)
    need(LA==sorted((i,j) for i in range(16) for j in range(16-i) if 5*i-7*j<=3),'A lattice = {i,j>=0, i+j<=15, 5i-7j<=3}')
    need(all(i<=2*j for i,j in LA),'i<=2j automatic on A lattice')
    need(LB==sorted((i,j) for i in range(26) for j in range(26-i) if 5*i-7*j<=5),'B lattice = {i,j>=0, i+j<=25, 5i-7j<=5}')
    oddA=[s for s in LA if sum(s)%2]; oddB=[s for s in LB if sum(s)%2]
    need((len(LA),len(oddA),len(LB),len(oddB))==(83,44,215,112),'lattice census 83/44, 215/112')
    need([s for s in LA if 5*s[0]-7*s[1]==3]==[(2,1),(9,6)] and max(5*i-7*j for i,j in LA)==3,'A weight-3 face slots (2,1),(9,6)')
    need([s for s in LB if 5*s[0]-7*s[1]==5]==[(1,0),(8,5),(15,10)] and max(5*i-7*j for i,j in LB)==5,'B weight-5 face slots')
    need(set(LA)<=set(LB) and max(sum(s) for s in LA)==15<25,'A lattice inside B lattice; degree 15<25')
    VAm=tuple((3,0) if v==(2,1) else v for v in VA) if mode=='--mutate-source-face' else VA  # source-face mutation: common_3 vertex
    ed=list(zip(VAm,VAm[1:]+VAm[:1]))
    def inside3(i,j):  # (i,j) in (1/3)P_A iff (3i,3j) in P_A, literal polygon
        cr=[(B[0]-A[0])*(3*j-A[1])-(B[1]-A[1])*(3*i-A[0]) for A,B in ed]
        return all(x>=0 for x in cr) or all(x<=0 for x in cr)
    third=sorted((i,j) for i in range(6) for j in range(6) if inside3(i,j))
    need(third==sorted((i,j) for i in range(6) for j in range(6-i) if 5*i-7*j<=1) or mode=='--mutate-source-face','(1/3)P_A lattice by inequalities')
    lower=[s for s in third if sum(s)%2 and sum(s)<5]
    need(lower==[(0,1),(0,3),(1,2)],'exactly three lower generator slots p,p^3,gp^2')
    need(all(3*i<=9 and 3*i+3*j<=15 and 15*i-21*j<=3 and 3*i<=6*j for i,j in third),'(1/3)P_A lattice inside P_A/3')
    need(len(third)==13 and [s for s in third if sum(s)==5]==[(0,5),(1,4),(2,3),(3,2)],'degree-5 slots fixed by S_top=H')
    fifth=[(i,j) for i in range(26) for j in range(26-i) if 5*i-7*j<=5 and i<=2*j]
    need(set(fifth)<=set(LB),'(5/3)P_A lattice inside B lattice')
    # negative-row envelope by exponent bookkeeping only: e=5t+2s-(i+j), no expansion
    rowsA={(t,5*t+2*s-i-j) for i,j in LA for t in range(j+1) for s in range(j-t+1) if 5*t+2*s-i-j<0}
    rowsB={(t,5*t+2*s-i-j) for i,j in LB for t in range(j+1) for s in range(j-t+1) if 5*t+2*s-i-j<0}
    need(rowsA=={(t,e) for t in range(3) for e in range(5*t-15,0)} and len(rowsA)==30,'A negative envelope 30 rows')
    need(rowsB=={(t,e) for t in range(5) for e in range(5*t-25,0)} and len(rowsB)==75 and rowsA<=rowsB,'B negative envelope 75 rows contains A rows')
    out['polygon']={'A_vertices':VA,'B_vertices':VB,'lattice':[83,44,215,112],'generator_lower_slots':lower}
    # ---- C2: generic degree-five generator lift, two complete negative rows, R_t recovery (symbolic a,b,c)
    H=add(pw(p,5),mul(pw(g,3),pw(p,2)))
    S=add(H,mul(a,mul(g,pw(p,2))),mul(b,pw(p,3)),mul(c,p))
    u,v=g,p; vi=pw(v,-1); phip=add(mul(pw(v,4),u),sc(v,-1),sc(vi,-1))
    lift=lambda X: subst(X,(vi,phip,a,b,c,k))
    neg=lambda X: cl({e:q for e,q in X.items() if e[1]<0})
    need(neg(lift(H))=={(0,-3,0,0,0,0):Q(-3),(0,-1,0,0,0,0):Q(-9)},'phi(H) negative part -3v^-3-9v^-1')
    need(neg(lift(mul(g,pw(p,2))))=={(0,-3,0,0,0,0):Q(1),(0,-1,0,0,0,0):Q(2)},'phi(gp^2) negative part')
    need(neg(lift(pw(p,3)))=={(0,-3,0,0,0,0):Q(-1),(0,-1,0,0,0,0):Q(-3)},'phi(p^3) negative part')
    N=neg(lift(S))
    need(N==add(mul(pw(vi,3),add(a,sc(b,-1),const(-3))),mul(vi,add(sc(a,2),sc(b,-3),sc(c,-1),const(-9)))),'two complete negative rows')
    rows=sorted({e[1] for e in N})
    if mode=='--mutate-missing-negative-row': rows=[-3]
    cand=subst(N,(g,p,const(3),const(0),const(0),k))   # a=3,b=0,c=0 kills v^-3 only
    need(cand=={(0,-1,0,0,0,0):Q(-3)},'candidate leaves exactly -3v^-1')
    need(any(e[1] in rows for e in cand),'omitted negative row accepted a non-ordinary generator')
    solved=subst(N,(g,p,add(b,const(3)),b,sc(add(b,const(3)),-1),k))
    need(solved=={},'a=b+3, c=-b-3 recovers R_t exactly')
    t=b; R=subst(S,(g,p,add(t,const(3)),t,sc(add(t,const(3)),-1),k))
    need(all(e[1]>=0 for e in lift(R)),'phi(R_t) ordinary (symbolic t)')
    need(all((i,j) in third and (i+j)%2==1 and i+j>0 for i,j,*_ in R),'R_t support in (1/3)P_A, odd, no origin')
    need(cl({e:q for e,q in R.items() if e[0]+e[1]==5})==H and wlead(R)==(1,{(3,2,0,0,0,0):Q(1)}),'R_t top H and (5,-7)-leader g^3p^2')
    need(cl({e:q for e,q in subst(R,(g,p,a,const(-3),c,k)).items() if e[1]==0})=={},'t=-3: p^2 divides R (p-adic order 2 of H kept)')
    # ---- C3: same-field scalar r=g5/f3^2 (no roots), several r0
    for r0 in (Q(2),Q(-3,5),Q(7)):
        f3=r0**-3; g5=r0**-5; r=g5/f3**2
        if mode=='--mutate-wrong-factor': r=g5/f3
        need(r==r0 and f3*r**3==1 and g5*r**5==1,'same-field scalar r=g5/f3^2 normalizes both tops')
    # ---- C4: [p^15]R^3 and s_t=[p^15]R^5 by combinatorial exponent triples only (pure-p part p^5+tp^3-(t+3)p)
    from math import factorial as fa
    def p15(n):
        z={}
        for n5 in range(n+1):
            for n3 in range(n+1-n5):
                n1=n-n5-n3
                if 5*n5+3*n3+n1==15:
                    m=Q(fa(n))/(fa(n5)*fa(n3)*fa(n1)); term=sc(mul(pw(t,n3),pw(sc(add(t,const(3)),-1),n1)),m); z=add(z,term)
        return z
    tp3=add(t,const(3))
    need(p15(3)==one,'[p^15]R^3=1')
    st=p15(5); st_closed=add(pw(t,5),sc(mul(pw(t,3),tp3),-20),sc(mul(t,pw(tp3,2)),30))
    need(st==st_closed,'s_t closed form via triples (0,5,0),(1,3,1),(2,1,2)')
    # whole shear identity in K[T]: T->g stands for R
    T=g; al,be,ga,s=a,b,c,k
    B0=add(pw(T,5),mul(be,pw(T,3)),mul(ga,T)); A0=add(pw(T,3),mul(al,T))
    sheared=add(B0,sc(mul(add(s,be),A0),-1))
    need(sheared==add(pw(T,5),sc(mul(s,pw(T,3)),-1),mul(add(ga,sc(mul(al,add(s,be)),-1)),T)),'whole shear: beta->-s, gamma->gamma-alpha(s+beta)')
    # ---- C5: bracket identities with R=g (degree 1); pure and general second order; a|b identity
    rnd=random.Random(20260907)
    def rp(n,d):
        z={}
        for _ in range(n): z[(rnd.randint(0,d),rnd.randint(0,d),0,0,0,0)]=Q(rnd.randint(-3,3) or 2)
        return cl(z)
    Rg=g; fac=Q(-1) if mode=='--mutate-wrong-factor' else Q(-1,3)
    for _ in range(4):
        A1=rp(4,3); A2=rp(3,3); B2=rp(3,3); B1g=rp(4,3); aa=Q(rnd.randint(-3,3)); bb=Q(rnd.randint(-3,3))
        A=add(pw(Rg,3),mul(k,A1),mul(pw(k,2),A2)); Bg=add(pw(Rg,5),mul(k,B1g),mul(pw(k,2),B2))
        need(kco(br(A,Bg,3),1)==mul(pw(Rg,2),br(Rg,add(sc(B1g,3),sc(mul(pw(Rg,2),A1),-5)))),'pure order one R^2[R,3B1-5R^2A1]')
        fR=add(sc(Rg,aa),sc(pw(Rg,3),bb)); fpR=add(const(aa),sc(pw(Rg,2),3*bb))
        B1=add(sc(mul(pw(Rg,2),A1),Q(5,3)),sc(fR,Q(1,3))); B=add(pw(Rg,5),mul(k,B1),mul(pw(k,2),B2))
        E=add(sc(mul(pw(Rg,2),B2),3),sc(mul(pw(Rg,4),A2),-5),sc(mul(Rg,pw(A1,2)),Q(-5,3)),sc(mul(fpR,A1),fac))
        need(kco(br(A,B,3),1)=={} and kco(br(A,B,3),2)==br(Rg,E),'pure order two [R,E], factor -1/3')
        # general centre: alpha,beta random, gamma=alpha*beta-5alpha^2/9, q=5R^2/3+beta-5alpha/9, B1=qA1+h(R)
        al=Q(rnd.randint(1,4)); be=Q(rnd.randint(-3,3)); ga=al*be-Q(5,9)*al**2
        aR=add(sc(pw(Rg,2),3),const(al)); bR=add(sc(pw(Rg,4),5),sc(pw(Rg,2),3*be),const(ga)); q=add(sc(pw(Rg,2),Q(5,3)),const(be-Q(5,9)*al))
        need(mul(aR,q)==bR,'a divides b exactly when gamma=alpha*beta-5alpha^2/9')
        h=add(sc(Rg,rnd.randint(-2,2)),sc(pw(Rg,3),rnd.randint(-2,2))); hp=der(h,0)
        A0=add(pw(Rg,3),sc(Rg,al)); B0=add(pw(Rg,5),sc(pw(Rg,3),be),sc(Rg,ga))
        A=add(A0,mul(k,A1),mul(pw(k,2),A2)); Bg=add(B0,mul(k,B1g),mul(pw(k,2),B2))
        need(kco(br(A,Bg,3),1)==br(Rg,add(mul(aR,B1g),sc(mul(bR,A1),-1))),'general order one [R,aB1-bA1]')
        B1=add(mul(q,A1),h); B=add(B0,mul(k,B1),mul(pw(k,2),B2))
        E=add(mul(aR,add(B2,sc(mul(q,A2),-1))),sc(mul(Rg,pw(A1,2)),Q(-5,3)),sc(mul(hp,A1),3*fac))
        need(kco(br(A,B,3),1)=={} and kco(br(A,B,3),2)==br(Rg,E),'general order two E=a(B2-qA2)-5RA1^2/3-h\'A1')
    # cubic no-Laurent-root valuations, with and without the (t+3)g term
    for n in range(-12,13):
        need([3*n,n,-2].count(min(3*n,n,-2))==1 and [3*n,-2].count(min(3*n,-2))==1,'unique minimal valuation')
    out.update({'status':'PASS','assert_nodes':0,'s_t':{str(e[3]):str(q) for e,q in sorted(st.items())},
                'expansions':'degree-five generator/R_t, R=g brackets only','no_R3_R5_or_15_25_pair_expansion':True})
    return out
def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25)); resource.setrlimit(resource.RLIMIT_AS,(512<<20,512<<20))
MUT={'--mutate-source-face':b'exactly three lower generator slots','--mutate-missing-negative-row':b'omitted negative row',
     '--mutate-wrong-factor':b'same-field scalar'}
if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else ''
    if mode=='--record':
        res=[]
        for opt in (False,True):
            for m in ('',)+tuple(MUT):
                cmd=[sys.executable]+(['-O'] if opt else [])+[str(Path(__file__).resolve())]+([m] if m else [])
                r=subprocess.run(cmd,capture_output=True,timeout=30,preexec_fn=caps)
                need((r.returncode!=0)==bool(m),'unexpected exit '+m)
                if m: need(MUT[m] in r.stderr,'wrong failure for '+m)
                else: (HERE/('witness-O.json' if opt else 'witness.json')).write_bytes(r.stdout)
                res.append({'optimized':opt,'mutation':m or None,'returncode':r.returncode,'stdout_sha256':hashlib.sha256(r.stdout).hexdigest(),'stderr_tail':r.stderr[-100:].decode(errors='replace')})
        need((HERE/'witness.json').read_bytes()==(HERE/'witness-O.json').read_bytes(),'normal/-O bytes differ')
        (HERE/'replay.json').write_text(json.dumps({'status':'PASS','runs':res,'caps':'30wall/25CPU,512MiB'},indent=1,sort_keys=True)+'\n')
        print(json.dumps({'status':'PASS','runs':len(res),'witness_sha256':hashlib.sha256((HERE/'witness.json').read_bytes()).hexdigest()}))
    else:
        print(json.dumps(run(mode),sort_keys=True,indent=1))
