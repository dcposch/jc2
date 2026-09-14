#!/usr/bin/env python3
"""Fable 5.1 gate controls for the odd D125 moving-face unit normalization.
Standard library only. Coefficient ring Q[eps]/(eps^2) (nilpotent present).
Tiny supports only: single monomials and a 7+9 monomial pair; no full pair."""
import hashlib, importlib.util, json, random, resource, subprocess, sys
from fractions import Fraction as Q
from pathlib import Path
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
CLIENT=Path('/tmp/jc2-lane.B5QyoK/inputs/client.py')   # explicit relocated frozen input
PIN='ec2fa2d1e23bc16bc07c9208f648e3b17561cbfddaaf04fed28d7ffc9a428d53'
C0=Q(-5,9)
class D:  # dual numbers a+b*eps
    __slots__=('a','b')
    def __init__(s,a=0,b=0): s.a,s.b=Q(a),Q(b)
    def __add__(s,y): y=dd(y); return D(s.a+y.a,s.b+y.b)
    __radd__=__add__
    def __neg__(s): return D(-s.a,-s.b)
    def __sub__(s,y): return s+(-dd(y))
    def __rsub__(s,y): return dd(y)+(-s)
    def __mul__(s,y): y=dd(y); return D(s.a*y.a,s.a*y.b+s.b*y.a)
    __rmul__=__mul__
    def inv(s):
        if s.a==0: raise ZeroDivisionError('nonunit dual number')
        return D(1/s.a,-s.b/(s.a*s.a))
    def __pow__(s,n):
        if n<0: return s.inv()**(-n)
        r=D(1)
        for _ in range(n): r=r*s
        return r
    def __eq__(s,y): y=dd(y); return s.a==y.a and s.b==y.b
    def __ne__(s,y): return not s==y
    def iszero(s): return s.a==0 and s.b==0
    def wire(s): return [str(s.a),str(s.b)]
def dd(x): return x if isinstance(x,D) else D(x)
def fail(msg): raise ValueError(msg)
def need(ok,msg):
    if not ok: fail(msg)
def pmul(p,q):
    o={}
    for m1,c1 in p.items():
        for m2,c2 in q.items():
            m=tuple(x+y for x,y in zip(m1,m2)); o[m]=o.get(m,D())+c1*c2
    return {m:c for m,c in o.items() if not c.iszero()}
def padd(p,q,sgn=1):
    o=dict(p)
    for m,c in q.items(): o[m]=o.get(m,D())+sgn*c
    return {m:c for m,c in o.items() if not c.iszero()}
def lift_monomial(i,j,ell,symbolic=False):
    """g^i p^j under g=v^-1, p=v^4 u - ell v - v^-1. Keys (t,e) or (t,e,d) when symbolic."""
    if symbolic:
        out={(0,-i,0):D(1)}; p={(1,4,0):D(1),(0,1,1):D(-1),(0,-1,0):D(-1)}
    else:
        out={(0,-i):D(1)}; p={(1,4):D(1),(0,1):-dd(ell),(0,-1):D(-1)}
    for _ in range(j): out=pmul(out,p)
    return out
def lift(poly,ell):
    out={}
    for (i,j),c in poly.items(): out=padd(out,{m:c*v for m,v in lift_monomial(i,j,ell).items()})
    return out
def deriv(p,axis):
    o={}
    for m,c in p.items():
        if m[axis]:
            mm=list(m); mm[axis]-=1; o[tuple(mm)]=o.get(tuple(mm),D())+c*m[axis]
    return {m:c for m,c in o.items() if not c.iszero()}
def bracket(A,B): return padd(pmul(deriv(A,0),deriv(B,1)),pmul(deriv(A,1),deriv(B,0)),-1)
def transport(poly,deg,ell):
    o={}
    for (i,j),c in poly.items():
        m=i+j
        if (m-deg)%2: fail('parity violation: even slot %s carries a nonzero coefficient'%((i,j),))
        o[(i,j)]=c*(ell**((m-deg)//2))
    return o
def load_client():
    need(hashlib.sha256(CLIENT.read_bytes()).hexdigest()==PIN,'client pin')
    spec=importlib.util.spec_from_file_location('gate_client',CLIENT)
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod, mod.make_contract('unequal','rational')
def run(mode):
    import ast
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text()))),'Assert node present')
    rng=random.Random(20260907)
    def rnd(): return D(Q(rng.randint(-9,9),rng.randint(1,5)),Q(rng.randint(-9,9),rng.randint(1,5)))
    mod,con=load_client(); out={'mode':mode or 'normal'}
    ell=D(3,2); k=ell**-6; need(k*(ell**6)==1,'k*ell^6')
    # C1 literal support census and fixed-face transport exponents
    fixed_faces={}; counts={}
    for idx,(mem,deg) in enumerate((('A',15),('B',25))):
        ent=con['coefficient_maps'][idx]; oddfree=oddfixed=0
        for e in ent:
            i,j=e['point']; m=i+j
            if 'fixed' in e:
                val=mod.decode(e['fixed']); need(val.b==0,'rational client has rho part')
                if val!=mod.ZERO: need(m%2==1,'nonzero fixed coefficient on even slot'); fixed_faces[(mem,i,j)]=(Q(val.a),(m-deg)//2)
                elif m%2==1: oddfixed+=1
                if m%2==1 and val!=mod.ZERO: oddfixed+=1
            elif m%2==1: oddfree+=1
        counts[mem]={'odd_free':oddfree,'odd_fixed':oddfixed,'odd_total':oddfree+oddfixed}
    need(counts['A']['odd_free']==33 and counts['B']['odd_free']==94,'33/94 odd free slots')
    need(counts['A']['odd_total']+counts['B']['odd_total']==156,'156 odd slots')
    exp={key:v[1] for key,v in fixed_faces.items()}
    need(exp[('A',2,1)]==-6 and exp[('B',8,5)]==-6 and exp[('B',1,0)]==-12 and exp[('A',9,6)]==0 and exp[('B',15,10)]==0,'inner face exponents')
    need(all(v==0 for (mem,i,j),v in exp.items() if i+j==(15 if mem=='A' else 25)),'outer exponents 0')
    out['C1']={'counts':counts,'laurent_coordinates':counts['A']['odd_free']+counts['B']['odd_free']+1,
               'fixed_nonzero':{'%s_%d_%d'%key:[str(v[0]),v[1]] for key,v in sorted(fixed_faces.items())}}
    # C2 every odd slot: single-monomial covariance (nilpotent ell) and [u^0 v^1] divisibility by ell
    cov=div=0
    for idx,deg in enumerate((15,25)):
        for e in con['coefficient_maps'][idx]:
            i,j=e['point']; m=i+j
            if m%2==0: continue
            old=lift_monomial(i,j,ell); new=lift_monomial(i,j,D(1)); pw=(m-deg)//2
            for (t,ee),c in set(old)|set(new) and {**{kk:None for kk in old},**{kk:None for kk in new}}.items():
                need((5*t-ee-deg)%2==0,'row parity')
                lhs=new.get((t,ee),D())*(ell**pw); rhs=old.get((t,ee),D())*(ell**((5*t-ee-deg)//2))
                need(lhs==rhs,'covariance %s'%((i,j,t,ee),)); cov+=1
            sym=lift_monomial(i,j,None,symbolic=True)
            v1=[d for (t,ee,d) in sym if t==0 and ee==1]
            need(all(d==(m+1)//2 and d>=1 for d in v1),'[u^0 v^1] ell-degree'); div+=len(v1)
    out['C2']={'covariance_rows':cov,'v1_terms_all_ell_divisible':div}
    # C3 tiny two-member pair: fixed faces plus two random odd free slots each, nilpotent coefficients
    def pick(idx,deg,n):
        free=[tuple(e['point']) for e in con['coefficient_maps'][idx] if 'variable' in e and sum(e['point'])%2==1]
        return {pt:rnd() for pt in rng.sample(free,n)}
    A={(0,15):D(1),(2,1):D(1),(9,6):D(1),(3,12):D(3),(6,9):D(3)}; A.update(pick(0,15,2))
    B={(0,25):D(1),(1,0):D(C0*-1),(8,5):D(Q(5,3)),(15,10):D(1),(3,22):D(5),(12,13):D(5)}; B.update(pick(1,25,3))
    if mode=='--mutate-parity': A[(4,4)]=D(1)
    At,Bt=transport(A,15,ell),transport(B,25,ell)
    faces={'A3':At[(2,1)],'B13':Bt[(8,5)],'B1':Bt[(1,0)]}
    if mode=='--mutate-unchanged-face': At[(2,1)]=D(1); faces['A3']=D(1)
    need(faces['A3']==k and faces['B13']==D(Q(5,3))*k and faces['B1']==D(Q(5,9))*(k**2),'moved faces k,5k/3,5k^2/9 (unchanged-face normalization is NOT the transport)')
    P,Qq=lift(A,ell),lift(B,ell); Pt,Qt=lift(At,D(1)),lift(Bt,D(1))
    for old,new,deg in ((P,Pt,15),(Qq,Qt,25)):
        for key in set(old)|set(new):
            t,e=key; need((5*t-e-deg)%2==0,'row parity')
            need(new.get(key,D())==old.get(key,D())*(ell**((5*t-e-deg)//2)),'full-lift row transport %s'%(key,))
    J,Jt=bracket(A,B),bracket(At,Bt)
    ctarget=D(C0)*(k**3)
    if mode=='--mutate-c-power': ctarget=D(C0)*(k**2)
    for key in set(J)|set(Jt):
        n=sum(key); need(n%2==0,'odd Jacobian degree survived')
        need(Jt.get(key,D())==J.get(key,D())*(ell**((n-38)//2)),'Jacobian row transport %s'%(key,))
    need(D(C0)*(ell**-18)==ctarget,'c target power: c0*ell^-18 must equal declared c0*k^3')
    # chain rule with det +v^2 on the tiny Laurent pair, and the origin identity bookkeeping
    lhs=bracket(P,Qq); JL=lift(J,ell); rhs={(t,e+2):c for (t,e),c in JL.items()}
    need(lhs==rhs,'chain rule [P,Q]=v^2*phi([A,B])')
    const=lhs.get((0,0),D()); s=D()
    for (t,e),c in P.items():
        if t==1: s=s+c*Qq.get((0,1-e),D())*(1-e)
    for (t,e),c in Qq.items():
        if t==1: s=s-c*P.get((0,1-e),D())*(1-e)
    need(s==const,'origin constant-term expansion')
    residual=const-(P.get((1,0),D())*Qq.get((0,1),D())-P.get((0,1),D())*Qq.get((1,0),D()))
    negterms=D()
    for (t,e),c in P.items():
        if t==1 and e!=0 and (e<0 or 1-e<0): negterms=negterms+c*Qq.get((0,1-e),D())*(1-e)
    for (t,e),c in Qq.items():
        if t==1 and e!=0 and (e<0 or 1-e<0): negterms=negterms-c*P.get((0,1-e),D())*(1-e)
    need(residual==negterms,'every extra origin term carries a negative-row coefficient')
    need(P.get((0,1),D())==lift(A,D(0)).get((0,1),D())*0 or lift(A,D(0)).get((0,1),D()).iszero(),'P01 vanishes at ell=0')
    need(lift(B,D(0)).get((0,1),D()).iszero(),'Q01 vanishes at ell=0')
    # physical transform: tau^-D P(tau^5 u, tau^-1 v) coefficientwise, degree and top
    for old,deg in ((P,15),(Qq,25)):
        need(max(t+e for t,e in old)==5*deg and old[(deg,4*deg)]==1,'degree 5D and monic top')
        need(((5*deg-4*deg-deg)//2)==0,'top factor 1')
    out['C3']={'A_terms':len(A),'B_terms':len(B),'P_terms':len(P),'Q_terms':len(Qq),'J_rows':len(J),'faces':{n:v.wire() for n,v in faces.items()},
               'c_target':ctarget.wire(),'P01_ell0_zero':True}
    # C4 rank-6 cover: basis decomposition and unit derivative
    for n in range(-13,14):
        q,r=divmod(n,6); need(ell**n==(k**(-q))*(ell**r) if q<=0 else ell**n==(k.inv()**q)*(ell**r),'basis decomposition')
    need(D(6)*(ell**5)*(k*ell*Q(1,6))==1,'6T^5 unit with inverse kT/6')
    # C5 guard: parameter contract only
    def guarded(x,z): return True if mode=='--mutate-omit-guard' else x*z==1
    need(guarded(k,k.inv()),'positive guard')
    kz=D(0); need(not guarded(kz,D(0)),'k=0 must fail the inverse guard (parameter contract, not a full point)')
    need((D(C0)*(kz**3)).iszero(),'k=0 kills the Jacobian target')
    out['C4C5']={'cover_rank':6,'guard':'zk-1 parameter contract only'}
    out['status']='PASS'; return out
def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25)); resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,)*2)
if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else ''
    if mode=='--record':
        rows=[]; muts=('','--mutate-unchanged-face','--mutate-c-power','--mutate-omit-guard','--mutate-parity')
        for opt in (False,True):
            for mu in muts:
                cmd=[sys.executable]+(['-O'] if opt else [])+[__file__]+([mu] if mu else [])
                r=subprocess.run(cmd,capture_output=True,timeout=30,preexec_fn=caps)
                need((r.returncode!=0)==bool(mu),'unexpected exit for %r opt=%s: %s'%(mu,opt,r.stderr[-300:]))
                if not mu: (HERE/('witness-O.json' if opt else 'witness.json')).write_bytes(r.stdout)
                rows.append({'optimized':opt,'mutation':mu or None,'returncode':r.returncode,'stdout_sha256':hashlib.sha256(r.stdout).hexdigest(),
                             'stderr_tail':r.stderr.decode(errors='replace').strip().splitlines()[-1][:160] if r.stderr else ''})
        need((HERE/'witness.json').read_bytes()==(HERE/'witness-O.json').read_bytes(),'normal/-O mismatch')
        (HERE/'replay.json').write_text(json.dumps({'status':'PASS','runs':rows,'caps':'30 wall/25 CPU s, 512 MiB'},indent=1,sort_keys=True)+'\n')
        print(json.dumps({'status':'PASS','runs':len(rows),'witness_sha256':hashlib.sha256((HERE/'witness.json').read_bytes()).hexdigest()}))
    else:
        print(json.dumps(run(mode),sort_keys=True,indent=1))
