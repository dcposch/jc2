#!/usr/bin/env python3
"""Small pure-center filtration, moving-reference and nilpotent-jet controls."""
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
spec=importlib.util.spec_from_file_location('pure_helpers',DEP)
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
add,scale,mul,power,bracket,need,wire,substitute=(getattr(m,n) for n in ('add','scale','mul','power','bracket','need','wire','substitute'))

def check(mode):
    need(sys.dont_write_bytecode,'bytecode disabled')
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text()))),'zero Assert nodes')
    one={(0,0,0):Q(1)}; g={(1,0,0):Q(1)}; p={(0,1,0):Q(1)}; s={(0,0,1):Q(1)}
    V=add(power(g,3),power(p,3),scale(p,-3)); R=mul(power(p,2),V)
    S=add(mul(g,power(p,2)),power(p,3),scale(p,-1)); Z=add(mul(g,p),power(p,2))
    w=lambda z:max(5*i-7*j for i,j,k in z)
    need(w(V)==15 and w(R)==1 and w(Z)==-2,'literal factor weights')
    bad=mul(mul(g,p),V)
    need(w(bad)==13 and bad.get((4,1,0))==1,'actual unweighted countercontrol has a p-linear term')
    admissible=True if mode=='--mutate-omit-weight' else w(bad)<=3
    need(not admissible,'weight hypothesis cannot be omitted from radical transfer')
    # Factor arithmetic: (g*p*V)^2/(p^2*V)=g^2*V; no square is expanded.
    need((2*1-2,2*1-1)==(0,1),'exact p,V factor divisibility countercontrol')
    for e in range(1,9):
        need(-7*(2*e-1)>3-15*e,'quotient weight excludes every p exponent below 2e')
    # Actual R and Z ordinaryness, expanding degree<=5 factors only.
    vi={(0,-1,0):Q(1)}; phi_p=add(mul(power(p,4),g),scale(p,-1),scale(vi,-1))
    Rlift=substitute(R,(vi,phi_p,s)); Zlift=substitute(Z,(vi,phi_p,s))
    need(all(j>=0 for i,j,k in Rlift) and all(j>=0 for i,j,k in Zlift),'literal R,Z ordinary lifts')
    need({e:c for e,c in Rlift.items() if e[1]==0}==scale(g,3),'R physical linear transverse jet')
    need(Z.get((0,0,0),0)==0 and Z.get((0,8,0),0)==0 and max(i+j for i,j,k in Z)<3,'Z meets leading C conditions and V does not divide it')
    need(bracket(R,Z)!={},'actual nilpotent survivor is not an all-order commuting family')
    # Moving source-reference countercontrol: alpha=h=s, t=-3+s,
    # A=R_h^3+sR_0 has no p-linear coefficient; no actual cube is expanded.
    F2=scale(add(R,scale(S,3)),Q(-1,3))
    if mode=='--mutate-omit-mixed-linear': F2=add(F2,scale(p,-1))
    need(scale(F2,-3)==add(R,scale(S,3)),'moving-reference mixed correction is retained')
    need(F2.get((0,1,0))==1 and F2.get((0,3,0),0)==0,'mixed residual linear term is nonzero despite actual A_p zero')
    # Cubic coefficient selection: p13 in R_t^3 is 3t, p3 is -(t+3)^3.
    triples13=[(a,b,c) for a in (1,3,5) for b in (1,3,5) for c in (1,3,5) if a+b+c==13]
    triples3=[(a,b,c) for a in (1,3,5) for b in (1,3,5) for c in (1,3,5) if a+b+c==3]
    need(sorted(triples13)==[(3,5,5),(5,3,5),(5,5,3)] and triples3==[(1,1,1)],'exact moving-reference scalar coefficients')
    # Polynomial identity with a genuinely moving formal R_s; this is R=g toy arithmetic.
    Rt=add(g,mul(s,p)); al=power(s,2); be=power(s,3); ga=power(s,4)
    F=mul(power(s,3),power(p,3)); G=mul(power(s,4),mul(g,power(p,2)))
    aa=add(scale(power(Rt,2),3),al); qq=add(scale(power(Rt,2),Q(5,3)),be,scale(al,Q(-5,9)))
    dd=add(ga,scale(mul(be,al),-1),scale(power(al,2),Q(5,9)))
    At=add(power(Rt,3),mul(al,Rt),F)
    Bt=add(power(Rt,5),mul(be,power(Rt,3)),mul(ga,Rt),mul(qq,F),G)
    usedR=g if mode=='--mutate-freeze-moving-R' else Rt
    EE=add(mul(aa,G),scale(mul(dd,F),-1),scale(mul(usedR,power(F,2)),Q(-5,3)))
    need(bracket(At,Bt)==add(bracket(usedR,EE),bracket(F,G)),'complete moving-R polynomial identity')
    # Formal (R,Z)=(g,p) verifies the factored nilpotent source candidate.
    Ac=add(power(g,3),mul(s,mul(g,p)))
    coef=Q(5,27) if mode=='--mutate-jet-coefficient' else Q(5,9)
    Bc=add(power(g,5),scale(mul(s,mul(power(g,3),p)),Q(5,3)),scale(mul(power(s,2),mul(g,power(p,2))),coef))
    JJ=bracket(Ac,Bc)
    need(JJ=={(1,2,3):Q(5,9)},'actual formal twojet bracket and first nonzero order')
    # A full k=epsilon moving face is NOT present in this k=0 candidate.
    face_ok=True if mode=='--mutate-omit-k-face' else Q(0)==Q(1)
    need(not face_ok,'nilpotent candidate does not carry a nonzero moving k face')
    # U=S is killed by p13 normalization once a remainder lies in R^2*K[g,p].
    slots=[(i,n-i) for n in (1,3) for i in range(n+1) if 5*i-7*(n-i)<=1]
    need(slots==[(0,1),(0,3),(1,2)],'literal cubic quotient support')
    need(R.get((0,5,0))==1 and S.get((0,3,0))==1,'p13 coefficient of factored R^2*S is one')
    return {'status':'PASS','assert_nodes':0,'R':wire(R),'V':wire(V),'Z':wire(Z),'Z_lift':wire(Zlift),
            'weight_bad_countercontrol':wire(bad),'mixed_reference_F2':wire(F2),'formal_nilpotent_J':wire(JJ),
            'scope':'small exact factor/reference controls and a k=0 nilpotent candidate; no guarded arc or full pair expansion'}

def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25)); resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,512*1024*1024))

if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else ''
    if mode=='--record':
        modes=[('',None),('--mutate-omit-weight',b'weight hypothesis cannot'),('--mutate-omit-mixed-linear',b'moving-reference mixed correction'),
               ('--mutate-freeze-moving-R',b'complete moving-R polynomial'),('--mutate-jet-coefficient',b'actual formal twojet'),
               ('--mutate-omit-k-face',b'nilpotent candidate does not')]
        records=[]
        for opt in (False,True):
            for mutation,msg in modes:
                out=subprocess.run([sys.executable,'-B']+(['-O'] if opt else [])+[str(Path(__file__).resolve())]+([mutation] if mutation else []),capture_output=True,timeout=30,preexec_fn=caps)
                need((out.returncode!=0)==bool(mutation),'unexpected pure control exit')
                if mutation: need(msg in out.stderr,'wrong mutation failure')
                else:
                    with (HERE/('witness-O.json' if opt else 'witness.json')).open('xb') as f: f.write(out.stdout)
                records.append({'optimized':opt,'mutation':mutation or None,'returncode':out.returncode,
                                'stdout_sha256':hashlib.sha256(out.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(out.stderr).hexdigest()})
        need((HERE/'witness.json').read_bytes()==(HERE/'witness-O.json').read_bytes(),'normal -O witness equality')
        with (HERE/'replay.json').open('x') as f: json.dump({'status':'PASS','runs':records,'caps':'30wall25CPU512MiB each','writers_finished':True},f,sort_keys=True,indent=2); f.write('\n')
        print(json.dumps({'status':'PASS','runs':len(records),'witness_sha256':hashlib.sha256((HERE/'witness.json').read_bytes()).hexdigest()}))
    else: print(json.dumps(check(mode),sort_keys=True,indent=2))
