#!/usr/bin/env python3
"""Degree-five actual factors, formal-coordinate identities, and valuation controls."""
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

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
DEP=ROOT/'box/d125-zero-k-deformation-discriminator-20260907/check.py'
if hashlib.sha256(DEP.read_bytes()).hexdigest()!='25be0862730df8b66076eb59a2d1d0909fbcf563ea73ce16924affdc7c70ad66': raise RuntimeError('helper drift')
spec=importlib.util.spec_from_file_location('critical_small_helpers',DEP)
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
add,scale,mul,power,derivative,bracket,need,wire,substitute=(getattr(m,n) for n in ('add','scale','mul','power','derivative','bracket','need','wire','substitute'))

def check(mode):
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text()))),'zero Assert nodes')
    one={(0,0,0):Q(1)}; g={(1,0,0):Q(1)}; p={(0,1,0):Q(1)}; h={(0,0,1):Q(1)}
    V=add(power(g,3),power(p,3),scale(p,-3)); R=mul(power(p,2),V)
    S=add(power(p,3),mul(g,power(p,2)),scale(p,-1))
    Rs=R if mode=='--freeze-moving-reference' else add(R,mul(h,S))
    need(derivative(Rs,0)==mul(power(p,2),add(scale(power(g,2),3),h)),'actual moving derivative')
    need(max(5*i-7*j for i,j,k in Rs)==1,'moving reference weight one')
    need(all(i+j<=5 for z in (V,R,S,Rs) for i,j,k in z),'actual degree-five cap')
    # Concrete missing-weight control: gpV vanishes on V but is not divisible by p^2V.
    P=mul(mul(g,p),V) if mode=='--wrong-filtered-input' else R
    def filtered_input(z): return max(5*i-7*j for i,j,k in z)<=3
    need(filtered_input(P),'actual filtered input fails without weight')
    bad=mul(mul(g,p),V)
    need(not filtered_input(bad) and any(j==1 for i,j,k in bad),'unrestricted division countercontrol')
    # On Rs=0: p^2 V=-h S. This produces h*(1/p-g-p), a genuine pole if F=V.
    pi={(0,-1,0):Q(1)}
    need(scale(S,-1)==mul(power(p,2),add(pi,scale(g,-1),scale(p,-1))),'actual pole numerator identity')
    # Formal z=g identity only: no actual R powers or A15/B25 are expanded.
    z=g; al=Q(-3); de=Q(5); be=Q(2); ga=de+be*al-Q(5,9)*al*al
    F=add(mul(z,power(p,2)),power(p,3)); G=add(mul(z,power(p,4)),power(p,5))
    aa=add(scale(power(z,2),3),scale(one,al)); qq=add(scale(power(z,2),Q(5,3)),scale(one,be-Q(5,9)*al))
    A=add(power(z,3),scale(z,al),F)
    B=add(power(z,5),scale(power(z,3),be),scale(z,ga),mul(qq,F),G)
    HH=add(mul(aa,G),scale(F,-de),scale(mul(z,power(F,2)),Q(-5,3)))
    cross={} if mode=='--omit-cross-bracket' else bracket(F,G)
    need(bracket(A,B)==add(derivative(HH,1),cross),'full formal moving identity retains cross')
    def at(z0): return substitute(z0,(one,p,h))
    UU=at(F); Up=derivative(UU,1)
    factor=Q(-5,3) if mode=='--wrong-critical-factor' else Q(-10,3)
    main=add(scale(Up,-de),scale(mul(UU,Up),factor))
    need(at(derivative(HH,1))==main,'critical derivative factor')
    f0={e:c for e,c in F.items() if e[0]==0}; g0={e:c for e,c in G.items() if e[0]==0}
    f1={tuple([0,e[1],e[2]]):c for e,c in F.items() if e[0]==1}; g1={tuple([0,e[1],e[2]]):c for e,c in G.items() if e[0]==1}
    need({e:c for e,c in bracket(A,B).items() if e[0]==0}==add(mul(add(scale(one,al),f1),derivative(g0,1)),scale(mul(add(scale(one,de),g1),derivative(f0,1)),-1)),'exact zero-fiber equation')
    # Target at the center: (-5/9)*kappa^3*g^2 / (3p^2g^2)=-5*kappa^3/(27p^2).
    targetfactor=Q(-5,9) if mode=='--wrong-target-factor' else Q(-5,27)
    need(mul(scale(one,targetfactor),scale(power(g,2),3))==scale(power(g,2),Q(-5,9)),'target factor after Jacobian division')
    primitive=scale(pi,Q(5,27) if mode=='--wrong-primitive-sign' else Q(-5,27))
    need(derivative(primitive,1)==scale(mul(pi,pi),Q(5,27)),'primitive sign')
    # Exact test values only; the report proves the inequalities for all values.
    vals=[]
    for j,mm,a,q,d in [(12,13,10,18,22),(12,13,11,17,22),(10,11,9,15,19),(10,11,9,14,19)]:
        j,mm,a,q,d=map(Q,(j,mm,a,q,d)); f=min(q,j+a/2)
        vv=min(q+min(d,2*j)-a,3*mm-a)
        MM=min(d+f,a/2+2*f); NN=min(j+vv,3*j+a/2,2*j+f)
        need(NN>min(MM,3*mm),'valuation separation control')
        vals.append({'j':str(j),'m':str(mm),'a':str(a),'q':str(q),'d':str(d),'f':str(f),'M':str(MM),'cross_lower_bound':str(NN),'target_order':str(3*mm)})
    return {'status':'PASS','zero_assert_nodes':True,'moving_reference':wire(Rs),'target_leader':'-5*kappa^3/(27*p^2)','primitive':'-5*kappa^3/(27*p)','valuation_controls':vals,'scope':'small identities and actual failed weight control; not a point, source expansion, or substitute for the report proof'}

def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25)); resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,512*1024*1024))

if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else ''
    if mode=='--record':
        modes=[('',None),('--freeze-moving-reference',b'actual moving derivative'),('--wrong-filtered-input',b'actual filtered input fails without weight'),('--omit-cross-bracket',b'full formal moving identity retains cross'),('--wrong-critical-factor',b'critical derivative factor'),('--wrong-target-factor',b'target factor after Jacobian division'),('--wrong-primitive-sign',b'primitive sign')]
        records=[]
        for opt in (False,True):
            for mutation,msg in modes:
                out=subprocess.run([sys.executable,'-I','-B']+(['-O'] if opt else [])+[str(Path(__file__).resolve())]+([mutation] if mutation else []),capture_output=True,timeout=30,preexec_fn=caps)
                need((out.returncode!=0)==bool(mutation),'unexpected control exit')
                if mutation: need(msg in out.stderr,'wrong failure marker')
                else:
                    with (HERE/('final-witness-O.json' if opt else 'final-witness.json')).open('xb') as stream: stream.write(out.stdout)
                records.append({'optimized':opt,'mutation':mutation or None,'returncode':out.returncode,'stdout_sha256':hashlib.sha256(out.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(out.stderr).hexdigest()})
        need((HERE/'final-witness.json').read_bytes()==(HERE/'final-witness-O.json').read_bytes(),'normal optimized bytes differ')
        with (HERE/'final-replay.json').open('x') as stream: json.dump({'status':'PASS','runs':records,'caps':'30wall25CPU512MiB each','writers_finished':True},stream,sort_keys=True,indent=2); stream.write('\n')
        print(json.dumps({'status':'PASS','runs':len(records),'witness_sha256':hashlib.sha256((HERE/'final-witness.json').read_bytes()).hexdigest()}))
    else: print(json.dumps(check(mode),sort_keys=True,indent=2))
