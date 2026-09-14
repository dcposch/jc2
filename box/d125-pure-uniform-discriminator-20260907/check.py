#!/usr/bin/env python3
"""Small generators, a formal collision identity, and an exact affine-unit control."""
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
spec=importlib.util.spec_from_file_location('uniform_pure_helpers',DEP)
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
add,scale,mul,power,bracket,need,wire,substitute=(getattr(m,n) for n in ('add','scale','mul','power','bracket','need','wire','substitute'))

def check(mode):
    need(sys.dont_write_bytecode,'bytecode disabled')
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text()))),'zero Assert nodes')
    one={(0,0,0):Q(1)}; g={(1,0,0):Q(1)}; p={(0,1,0):Q(1)}; s={(0,0,1):Q(1)}
    L=add(g,p); V=add(power(g,3),power(p,3),scale(p,-3)); R=mul(power(p,2),V); r=mul(p,power(L,2))
    need(V==add(power(L,3),scale(mul(p,add(mul(g,L),one)),-3)),'literal cubic factor identity for C')
    vi={(0,-1,0):Q(1)}; phi_p=add(mul(power(p,4),g),scale(p,-1),scale(vi,-1))
    lifts=[substitute(z,(vi,phi_p,s)) for z in (L,r,R)]
    need(all(j>=0 for z in lifts for i,j,k in z),'actual L,r,R ordinary generators')
    need(lifts[0]==add(mul(power(p,4),g),scale(p,-1)),'linear generator lift')
    # C,D,W remain circuits: C=r^2-RL=3p^3 L(gL+1), D=rC/3,W=C^2 L.
    # No actual degree-six C, degree-nine D, or higher source product is materialized.
    stats={'L':[1,5,1],'r':[3,3,3],'C':[6,-6,4],'D':[9,-3,7],'W':[13,-7,9]}
    need(stats['C']==[3+1+2,-21+5+10,3+1+0],'factored C degree weight origin')
    need(stats['D']==[3+6,3-6,3+4] and stats['W']==[12+1,-12+5,8+1],'factored D,W bounds')
    # Formal (R,r,L)=(g,p,1): all products below are ONLY the small formal control.
    C=add(power(p,2),scale(g,-1)); D=scale(mul(p,C),Q(1,3)); W=power(C,2)
    need(add(scale(power(D,2),9),scale(power(C,3),-1))==mul(g,W),'exact square/cube collision numerator')
    if mode=='--mutate-remove-intermediate': D={}
    A=add(power(g,3),mul(power(s,2),mul(g,C)),mul(power(s,3),D))
    b6=Q(5,27) if mode=='--mutate-sixth-factor' else Q(5,81)
    B=add(power(g,5),scale(mul(power(s,2),mul(power(g,3),C)),Q(5,3)),
          scale(mul(power(s,3),mul(power(g,2),D)),Q(5,3)),scale(mul(power(s,4),mul(g,power(C,2))),Q(5,9)),
          scale(mul(power(s,5),mul(C,D)),Q(10,9)),scale(mul(power(s,6),W),b6))
    J=bracket(A,B)
    need({e:c for e,c in J.items() if e[2]<=6}=={},'actual formal collision through order six')
    # Moving alpha*G cannot be deleted from the exact identity.
    Rt=add(g,mul(s,p)); al=s; be=power(s,3); ga=power(s,2)
    F=mul(power(s,2),power(p,3)); G=mul(power(s,4),mul(g,power(p,2)))
    aa=add(scale(power(Rt,2),3),al); qq=add(scale(power(Rt,2),Q(5,3)),be,scale(al,Q(-5,9)))
    dd=add(ga,scale(mul(be,al),-1),scale(power(al,2),Q(5,9)))
    At=add(power(Rt,3),mul(al,Rt),F)
    Bt=add(power(Rt,5),mul(be,power(Rt,3)),mul(ga,Rt),mul(qq,F),G)
    useda=scale(power(Rt,2),3) if mode=='--mutate-omit-alphaG' else aa
    E=add(mul(useda,G),scale(mul(dd,F),-1),scale(mul(Rt,power(F,2)),Q(-5,3)))
    need(bracket(At,Bt)==add(bracket(Rt,E),bracket(F,G)),'actual moving identity retains alphaG')
    # Genuine nonconstant EVEN unit, over Q[omega]/(omega^2+omega+1), on V=0.
    om=s; om2=add(scale(om,-1),scale(one,-1))
    L0=add(g,p); L1=add(g,mul(om,p)); L2=add(g,mul(om2,p))
    U=add(one,scale(mul(add(one,scale(om,-1)),mul(L0,L2)),Q(1,3)))
    Uinv=add(one,scale(mul(add(om,scale(one,-1)),mul(L1,L2)),Q(1,3)))
    if mode=='--mutate-unit-object': U=add(U,g)
    def reduce_curve(z):
        pending=dict(z); out={}
        while pending:
            (i,j,k),c=pending.popitem()
            if not c: continue
            if k>=2:
                for e,v in [((i,j,k-1),-c),((i,j,k-2),-c)]: pending[e]=pending.get(e,Q(0))+v
            elif i>=3:
                for e,v in [((i-3,j+1,k),3*c),((i-3,j+3,k),-c)]: pending[e]=pending.get(e,Q(0))+v
            else: out[(i,j,k)]=out.get((i,j,k),Q(0))+c
        return {e:c for e,c in out.items() if c}
    need(reduce_curve(mul(U,Uinv))==one,'actual nonconstant affine unit and inverse')
    need(any(i+j>0 for i,j,k in reduce_curve(U)) and all((i+j)%2==0 for i,j,k in U),'unit is nonconstant but even')
    # Exact Pell completion, variables now (C,D,sqrt(a)); b=2.
    pell_a=power(s,2); pell_b=scale(one,2)
    plus=add(scale(mul(pell_a,g),2),pell_b,scale(mul(s,p),2))
    minus=add(scale(mul(pell_a,g),2),pell_b,scale(mul(s,p),-2))
    pell_residue=add(power(p,2),scale(mul(g,add(mul(pell_a,g),pell_b)),-1))
    expected=add(power(pell_b,2),scale(mul(pell_a,pell_residue),-4))
    need(mul(plus,minus)==expected,'exact Pell factor product')
    return {'status':'PASS','assert_nodes':0,'generator_lifts':[wire(z) for z in lifts],'factored_degree_weight_origin':stats,
            'residue_identity':'9D^2-C^3=R*C^2*L','nonconstant_even_unit':wire(reduce_curve(U)),
            'scope':'generator-only source control, formal nilpotent collision and conditional affine-unit/Pell interface; no guarded arc'}

def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25)); resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,512*1024*1024))

if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else ''
    if mode=='--record':
        modes=[('',None),('--mutate-remove-intermediate',b'actual formal collision'),('--mutate-sixth-factor',b'actual formal collision'),
               ('--mutate-omit-alphaG',b'actual moving identity'),('--mutate-unit-object',b'actual nonconstant affine unit')]
        records=[]
        for opt in (False,True):
            for mutation,msg in modes:
                out=subprocess.run([sys.executable,'-B']+(['-O'] if opt else [])+[str(Path(__file__).resolve())]+([mutation] if mutation else []),capture_output=True,timeout=30,preexec_fn=caps)
                need((out.returncode!=0)==bool(mutation),'unexpected pure uniform control exit')
                if mutation: need(msg in out.stderr,'wrong mutation failure')
                else:
                    with (HERE/('witness-O.json' if opt else 'witness.json')).open('xb') as f: f.write(out.stdout)
                records.append({'optimized':opt,'mutation':mutation or None,'returncode':out.returncode,
                                'stdout_sha256':hashlib.sha256(out.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(out.stderr).hexdigest()})
        need((HERE/'witness.json').read_bytes()==(HERE/'witness-O.json').read_bytes(),'normal -O witness equality')
        with (HERE/'replay.json').open('x') as f: json.dump({'status':'PASS','runs':records,'caps':'30wall25CPU512MiB each','writers_finished':True},f,sort_keys=True,indent=2); f.write('\n')
        print(json.dumps({'status':'PASS','runs':len(records),'witness_sha256':hashlib.sha256((HERE/'witness.json').read_bytes()).hexdigest()}))
    else: print(json.dumps(check(mode),sort_keys=True,indent=2))
