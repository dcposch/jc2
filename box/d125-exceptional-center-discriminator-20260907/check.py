#!/usr/bin/env python3
"""Small exceptional-center scalar, cubic-lift and formal coefficient controls."""
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
spec=importlib.util.spec_from_file_location('exceptional_helpers',DEP)
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
add,scale,mul,power,bracket,need,wire,substitute=(getattr(m,n) for n in ('add','scale','mul','power','bracket','need','wire','substitute'))

def check(mode):
    need(sys.dont_write_bytecode,'bytecode disabled')
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text()))),'zero Assert nodes')
    one={(0,0,0):Q(1)}; g={(1,0,0):Q(1)}; p={(0,1,0):Q(1)}; s={(0,0,1):Q(1)}
    # Formal variables here are (z,alpha,beta); gamma=7 is an arbitrary fixed constant.
    a=add(scale(power(g,2),3),p)
    b=add(scale(power(g,4),5),scale(mul(s,power(g,2)),3),scale(one,7))
    q=add(scale(power(g,2),Q(5,3)),s,scale(p,Q(-5,9)))
    delta=add(scale(one,7),scale(mul(s,p),-1),scale(power(p,2),Q(5,9)))
    if mode=='--mutate-delta-sign': delta=add(delta,scale(power(p,2),Q(-10,9)))
    need(add(b,scale(mul(a,q),-1))==delta,'exact scalar remainder b modulo a')
    # Actual source R_-3 is only degree five; no R powers are expanded here.
    C=add(power(p,3),power(g,3),scale(p,-3))
    R=mul(power(p,2),C)
    need(R.get((2,1,0),Q(0))==0 and R.get((0,3,0))==-3,'exceptional low source coefficients')
    need(min(i+j for i,j,k in R)==3,'exceptional generator origin order three')
    # No lower polygon inequality is transferred through division, especially at alpha=0.
    slots=[(i,n-i) for n in (1,3) for i in range(n+1) if 5*i-7*(n-i)<=1]
    need(slots==[(0,1),(0,3),(1,2)],'complete cubic U support')
    S=add(mul(g,power(p,2)),power(p,3),scale(p,-1))
    u=g; v=p; vi={(0,-1,0):Q(1)}
    phi_p=add(mul(power(v,4),u),scale(v,-1),scale(vi,-1))
    basis=[p,power(p,3),mul(g,power(p,2))]
    lifts=[substitute(z,(vi,phi_p,s)) for z in basis]
    matrix=[[z.get((0,-3,0),Q(0)) for z in lifts],[z.get((0,-1,0),Q(0)) for z in lifts]]
    need(matrix==[[0,-1,1],[-1,-3,2]],'complete negative lift rows for U')
    kernel=[Q(-1),Q(1),Q(1)]
    if mode=='--mutate-omit-lift-row': kernel=[Q(0),Q(1),Q(1)]
    lift=add(*(scale(z,c) for z,c in zip(lifts,kernel)))
    need(all(j>=0 for i,j,k in lift),'both actual U lift rows retained')
    need(S.get((0,1,0))==-1,'U kernel has nonzero p coefficient')
    # Actual low p coefficients of aU,bU for U=S and R of origin order three.
    # Alpha!=0 is killed by A_p; alpha=0,delta=gamma!=0 is killed by B_p.
    def lowA(value): return True if mode=='--mutate-omit-low-A' else value==0
    def lowB(value): return True if mode=='--mutate-omit-low-B' else value==0
    need(lowA(Q(0)) and not lowA(Q(-2)),'actual alpha-unit low-A obstruction')
    need(lowB(Q(0)) and not lowB(Q(-5)),'actual gamma-unit low-B obstruction')
    # Formal R=g verifies the complete first-order tangent formula.
    alpha=Q(2); beta=Q(3); gamma=Q(5)
    aa=add(scale(power(g,2),3),scale(one,alpha))
    bb=add(scale(power(g,4),5),scale(power(g,2),3*beta),scale(one,gamma))
    U=add(power(p,3),mul(g,power(p,2)))
    A0=add(power(g,3),scale(g,alpha)); B0=add(power(g,5),scale(power(g,3),beta),scale(g,gamma))
    A1=add(mul(aa,U),scale(g,4))
    B1=add(mul(bb,U),scale(g,5),scale(power(g,3),6))
    if mode=='--mutate-tangent': B1=add(B1,U)
    need(add(bracket(A0,B1),bracket(A1,B0))=={},'actual full first-order bracket identity')
    # At delta=0 the first-order pivot really disappears; this is only a formal toy.
    bb_tuned=add(scale(power(g,4),5),scale(one,Q(-20,9)))
    q_tuned=add(scale(power(g,2),Q(5,3)),scale(one,Q(-10,9)))
    Ftoy=power(p,3); Gtoy=mul(q_tuned,Ftoy)
    Bt=add(power(g,5),scale(g,Q(-20,9)))
    need(bb_tuned==mul(aa,q_tuned),'tuned scalar quotient')
    need(add(bracket(A0,Gtoy),bracket(Ftoy,Bt))=={},'tuned first-order freedom exists')
    # Exact nilpotent first coefficient: X=(R^3+sR)^(1/3)=R+s/(3R)+O(s^2).
    # R=g is used only to multiply Laurent terms; actual R_-3 has valuation3.
    X1={(-1,0,0):Q(1,3)}
    need(scale(mul(power(g,2),X1),3)==g,'boundary alpha motion cube-root coefficient')
    need(-3<1,'exceptional origin filtration does not imply generic bound')
    return {'status':'PASS','assert_nodes':0,'delta':'gamma-beta*alpha+5*alpha^2/9',
            'U_slots':slots,'negative_lift_matrix':[[str(x) for x in row] for row in matrix],
            'U_kernel':[str(x) for x in kernel],'S_lift':wire(lift),
            'boundary_countercontrol':'k=0,A=R^3+sR,B=R^5; X1=1/(3R), actual origin valuation -3',
            'scope':'small source/support and formal tangent controls, not a guarded point or full arc witness'}

def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25)); resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,512*1024*1024))

if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else ''
    if mode=='--record':
        modes=[('',None),('--mutate-delta-sign',b'exact scalar remainder'),('--mutate-omit-lift-row',b'both actual U lift rows'),
               ('--mutate-omit-low-A',b'actual alpha-unit low-A'),('--mutate-omit-low-B',b'actual gamma-unit low-B'),
               ('--mutate-tangent',b'actual full first-order bracket')]
        records=[]
        for opt in (False,True):
            for mutation,msg in modes:
                out=subprocess.run([sys.executable,'-B']+(['-O'] if opt else [])+[str(Path(__file__).resolve())]+([mutation] if mutation else []),capture_output=True,timeout=30,preexec_fn=caps)
                need((out.returncode!=0)==bool(mutation),'unexpected exceptional control exit')
                if mutation: need(msg in out.stderr,'wrong mutation failure')
                else:
                    with (HERE/('final-witness-O.json' if opt else 'final-witness.json')).open('xb') as f: f.write(out.stdout)
                records.append({'optimized':opt,'mutation':mutation or None,'returncode':out.returncode,
                                'stdout_sha256':hashlib.sha256(out.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(out.stderr).hexdigest()})
        need((HERE/'final-witness.json').read_bytes()==(HERE/'final-witness-O.json').read_bytes(),'normal -O witness equality')
        with (HERE/'final-replay.json').open('x') as f: json.dump({'status':'PASS','runs':records,'caps':'30wall25CPU512MiB each','writers_finished':True},f,sort_keys=True,indent=2); f.write('\n')
        print(json.dumps({'status':'PASS','runs':len(records),'witness_sha256':hashlib.sha256((HERE/'final-witness.json').read_bytes()).hexdigest()}))
    else: print(json.dumps(check(mode),sort_keys=True,indent=2))
