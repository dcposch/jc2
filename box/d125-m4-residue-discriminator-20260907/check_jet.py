#!/usr/bin/env python3
"""One explicit unguarded mod-s^7 jet; actual A15/B25 are never expanded."""
import sys
sys.dont_write_bytecode=True
import ast
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import subprocess

HERE=Path(__file__).resolve().parent; ROOT=HERE.parents[1]
DEP=ROOT/'box/d125-zero-k-deformation-discriminator-20260907/check.py'
if hashlib.sha256(DEP.read_bytes()).hexdigest()!='25be0862730df8b66076eb59a2d1d0909fbcf563ea73ce16924affdc7c70ad66': raise RuntimeError('helper drift')
spec=importlib.util.spec_from_file_location('frozen_helpers',DEP); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
add,scale,mul,power,bracket,substitute,need,wire=(getattr(m,n) for n in ('add','scale','mul','power','bracket','substitute','need','wire'))

def check(mode):
    need(sys.dont_write_bytecode,'bytecode disabled')
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text()))),'Assert node')
    one={(0,0,0):Q(1)}; g={(1,0,0):Q(1)}; p={(0,1,0):Q(1)}; s={(0,0,1):Q(1)}
    H=add(power(p,5),mul(power(g,3),power(p,2)))
    R=add(H,scale(mul(g,power(p,2)),-1),scale(power(p,3),-4),p)
    T={(i,j-1,z):a for (i,j,z),a in R.items()}
    S=add(power(p,3),mul(g,power(p,2)),scale(p,-1))
    r=add(mul(power(g,2),p),mul(g,power(p,2)),p)
    Z=add(mul(g,p),power(p,2)); E=add(Z,scale(one,-1)); L=mul(power(p,2),E); Cstar=add(Z,L)
    q=add(mul(power(g,3),power(p,2)),scale(mul(power(g,2),power(p,3)),3),scale(mul(g,power(p,4)),2),power(p,3))
    if mode=='--mutate-q-negative': q=add(q,mul(g,power(p,4)))
    C0=add(power(r,2),scale(mul(T,Z),-1))
    D0=add(power(r,3),scale(mul(T,q),-1))
    need(all(i+j<=6 and 5*i-7*j<=0 and (i+j)%2==0 for i,j,z in C0),'literal C support')
    need(all(i+j<=9 and 5*i-7*j<=1 and i<=2*j and (i+j)%2==1 and j>=1 for i,j,z in D0),'literal D support')
    need([C0.get(e,Q(0)) for e in [(0,0,0),(1,1,0),(0,2,0)]]==[0,-1,0],'literal C low coefficients')
    need(all(D0.get(e,Q(0))==0 for e in [(0,1,0),(1,2,0),(0,3,0)]),'literal D low coefficients')
    vi={(0,-1,0):Q(1)}; phip=add(mul(power(p,4),g),scale(p,-1),scale(vi,-1))
    lifts={name:substitute(z,(vi,phip,{})) for name,z in [('R',R),('T',T),('r',r),('Z',Z),('q',q)]}
    need(all(e[1]>=0 for name in ('R','T','r','Z') for e in lifts[name]),'ordinary generators')
    need(min(e[1] for e in lifts['R'])==0 and min(e[1] for e in lifts['T'])==1,'R/T lift valuation')
    need({e:a for e,a in lifts['q'].items() if e[1]<0}=={(0,-1,0):Q(1)},'actual q negative row')
    # The U4 graph is factored; expand only its total-degree-three jet.
    Rlow={e:a for e,a in R.items() if e[0]+e[1]<=3}
    Cstarlow={e:a for e,a in Cstar.items() if e[0]+e[1]<=2}
    u4low=add(r,scale(Rlow,-1),scale(mul(p,Cstarlow),-2),scale(power(p,3),-4))
    if mode=='--mutate-U4-low': u4low=add(u4low,scale(power(p,3),-1))
    need(u4low==mul(power(g,2),p),'actual U4 low jet and moving face')
    # Universal square/cube factorization in FOUR abstract variables r,T,Z,q.
    zero=(0,0,0,0)
    def var4(i):
        e=[0]*4; e[i]=1; return {tuple(e):Q(1)}
    def pow4(z,n):
        ans={zero:Q(1)}
        for _ in range(n): ans=mul(ans,z)
        return ans
    rr,tt,zz,qq=[var4(i) for i in range(4)]
    lhs=add(pow4(add(pow4(rr,3),scale(mul(tt,qq),-1)),2),scale(pow4(add(pow4(rr,2),scale(mul(tt,zz),-1)),3),-1))
    inner=add(scale(mul(pow4(rr,3),qq),-2),mul(tt,pow4(qq,2)),scale(mul(pow4(rr,4),zz),3),
              scale(mul(pow4(rr,2),mul(tt,pow4(zz,2))),-3),mul(pow4(tt,2),pow4(zz,3)))
    need(lhs==mul(tt,inner),'exact universal quotient identity')
    # Full generic formal six-jet identity, using R=g only and allowing rational poles.
    rr=g; cc=add(power(p,2),one); dd=add(power(p,3),p); uu=add(mul(power(g,2),p),power(p,3))
    aa=add(power(rr,3),mul(power(s,2),mul(rr,cc)),mul(power(s,3),dd),mul(power(s,4),uu))
    pole=add(scale(power(dd,2),Q(5,9)),scale(power(cc,3),Q(-5,81)))
    ww={(i-1,j,z):a for (i,j,z),a in pole.items()}
    factor=Q(5,9) if mode=='--mutate-B6-cross' else Q(10,9)
    bb=add(power(rr,5),scale(mul(power(s,2),mul(power(rr,3),cc)),Q(5,3)),
           scale(mul(power(s,3),mul(power(rr,2),dd)),Q(5,3)),
           mul(power(s,4),add(scale(mul(power(rr,2),uu),Q(5,3)),scale(mul(rr,power(cc,2)),Q(5,9)))),
           scale(mul(power(s,5),mul(cc,dd)),Q(10,9)),
           mul(power(s,6),add(scale(mul(cc,uu),factor),ww,scale(rr,7))))
    need({e:a for e,a in bracket(aa,bb).items() if e[2]<=6}=={},'full six-jet cross coefficient')
    # Low equations over Q[b]/(b^4-3), retaining the finite algebra explicitly.
    # x=-b^2 s^2, y=1, k=s^4, e=-5b^2 s^6/9, a01=0.
    b=g; kk=power(s,4); yy=one
    xx=scale(mul(power(b,2),power(s,2)),C0[(1,1,0)]*R[(0,1,0)])
    ee=scale(mul(power(b,2),power(s,6)),Q(-5,9))
    def reduce_b4(z):
        out={}; base=Q(1) if mode=='--mutate-b4' else Q(3)
        for (i,j,k),a in z.items():
            e=(i%4,j,k); out[e]=out.get(e,Q(0))+a*base**(i//4)
        return {e:a for e,a in out.items() if a}
    need(reduce_b4(add(power(xx,2),scale(mul(kk,yy),-3)))=={},'actual saturated x square requires b4=3')
    need(reduce_b4(add(scale(ee,9),scale(mul(kk,xx),-5)))=={},'actual saturated e row')
    return {'status':'PASS','assert_nodes':0,'coefficient_algebra':'Q[b]/(b^4-3)',
            'C0':wire(C0),'D0':wire(D0),'scalings':{'C':'b^2*C0','D':'b^3*D0/3'},
            'q_negative':'v^-1','U4_low':'g^2*p','W_definition':'5*(9D^2-C^3)/(81R)',
            'low_rows':{'a01':'0','x':'-b^2*s^2','y':'1','e':'-5*b^2*s^6/9','k':'s^4'},
            'B_block_bounds':{'s2':[21,3],'s3':[19,3],'s4':[23,5],'s5':[15,1],'s6':[19,3]},
            'W_bounds':{'degree':13,'weight':1,'minimum_total_degree':5},
            'scope':'complete unguarded source modulo s^7 plus three saturated low equations; no inverse guard or extension claim'}

def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25)); resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,512*1024*1024))

if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else ''
    if mode=='--record':
        records=[]
        modes=['','--mutate-q-negative','--mutate-U4-low','--mutate-B6-cross','--mutate-b4']
        messages=[None,b'literal C support',b'actual U4 low jet',b'full six-jet cross coefficient',b'actual saturated x square']
        for opt in (False,True):
            for mutation,msg in zip(modes,messages):
                out=subprocess.run([sys.executable,'-B']+(['-O'] if opt else [])+[str(Path(__file__).resolve())]+([mutation] if mutation else []),capture_output=True,timeout=30,preexec_fn=caps)
                need((out.returncode!=0)==bool(mutation),'unexpected jet control exit')
                if mutation:
                    if mutation=='--mutate-q-negative': need(b'literal D support' in out.stderr or b'actual q negative row' in out.stderr,'unrelated q mutation failure')
                    else: need(msg in out.stderr,'unrelated jet mutation failure')
                else:
                    with (HERE/('jet-final-witness-O.json' if opt else 'jet-final-witness.json')).open('xb') as f: f.write(out.stdout)
                records.append({'optimized':opt,'mutation':mutation or None,'returncode':out.returncode,
                                'stdout_sha256':hashlib.sha256(out.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(out.stderr).hexdigest()})
        need((HERE/'jet-final-witness.json').read_bytes()==(HERE/'jet-final-witness-O.json').read_bytes(),'jet normal optimized equality')
        with (HERE/'jet-final-replay.json').open('x') as f: json.dump({'status':'PASS','runs':records,'caps':'30wall25CPU512MiB','writers_finished':True},f,sort_keys=True,indent=2); f.write('\n')
        print(json.dumps({'status':'PASS','runs':len(records),'witness_sha256':hashlib.sha256((HERE/'jet-final-witness.json').read_bytes()).hexdigest()}))
    else: print(json.dumps(check(mode),sort_keys=True,indent=2))
