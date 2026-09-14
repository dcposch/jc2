#!/usr/bin/env python3
"""Small factors and formal identities only; no actual high-degree source powers."""
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
spec=importlib.util.spec_from_file_location('low_alpha_helpers',DEP)
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
add,scale,mul,power,need,wire,substitute=(getattr(m,n) for n in ('add','scale','mul','power','need','wire','substitute'))

def check(mode):
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text()))),'zero Assert nodes')
    one={(0,0,0):Q(1)}; g={(1,0,0):Q(1)}; p={(0,1,0):Q(1)}; s={(0,0,1):Q(1)}
    V=add(power(g,3),power(p,3),scale(p,-3)); R=mul(power(p,2),V)
    L=add(g,p); r=mul(p,power(L,2)); rr=add(r,scale(R,Q(1,3)))
    M=add(L,scale(r,Q(2,3)),scale(R,Q(1,9)))
    need(rr.get((0,3,0),0)==0 and rr.get((2,1,0),0)==1 and rr.get((1,2,0),0)==2,'actual reference-adjusted generator jets')
    need(M.get((1,0,0),0)==1 and M.get((0,1,0),0)==1,'actual B low generator jets')
    need(all(i+j<=5 for z in (V,R,L,r,rr,M) for i,j,k in z),'actual generators at most degree five')
    vi={(0,-1,0):Q(1)}; phi_p=add(mul(power(p,4),g),scale(p,-1),scale(vi,-1))
    lifts=[substitute(z,(vi,phi_p,s)) for z in (R,L,r,rr,M)]
    need(all(j>=0 for z in lifts for i,j,k in z),'actual generators ordinary')
    # C=r^2-RL=3p^3 L(gL+1) is kept factored, never expanded here.
    need(V==add(power(L,3),scale(mul(p,add(mul(g,L),one)),-3)),'small identity underlying C factor')
    # Universal FOUR-variable identity (R,rprime,M,s), not an actual source pair.
    z0={(0,0,0,0):Q(1)}
    Z={(1,0,0,0):Q(1)}; T={(0,1,0,0):Q(1)}; U={(0,0,1,0):Q(1)}; S={(0,0,0,1):Q(1)}
    def pw(a,n):
        out=z0
        for _ in range(n): out=mul(out,a)
        return out
    C=add(pw(T,2),scale(mul(Z,U),-1))
    alpha=pw(S,7)
    delta=scale(pw(S,14),Q(5,3) if mode=='--mutate-delta-sign' else Q(-5,3))
    f12=Q(1,3) if mode=='--mutate-intermediate' else Q(1,6)
    F=add(mul(pw(S,8),mul(Z,C)),mul(pw(S,11),T),scale(mul(pw(S,12),mul(T,C)),f12))
    G=add(scale(mul(pw(S,16),mul(Z,pw(C,2))),Q(5,9)),
          scale(mul(pw(S,19),mul(C,T)),Q(10,9)),
          scale(mul(pw(S,20),mul(T,pw(C,2))),Q(5,27)),
          scale(mul(pw(S,22),U),Q(5,9)),scale(mul(pw(S,23),mul(C,U)),Q(5,27)))
    H=add(mul(add(scale(pw(Z,2),3),alpha),G),scale(mul(delta,F),-1),scale(mul(Z,pw(F,2)),Q(-5,3)))
    need({e:c for e,c in H.items() if e[3]<24}=={},'universal pre-3j mixed identity')
    # No claim of saturated low rows: their ACTUAL coefficient residuals are nonzero.
    k=power(s,11); x=scale(power(s,11),2); y=scale(power(s,7),-3); e=scale(power(s,22),Q(5,9))
    low2=add(power(x,2),scale(mul(k,y),-3)); low1=add(e,scale(mul(k,x),Q(-5,9)))
    need(low2==add(scale(power(s,18),9),scale(power(s,22),4)) and low1==scale(power(s,22),Q(-5,9)),'actual saturated low-row failures')
    # Literal p^1/p^3 coefficient extraction of the scalar-kernel identity.
    h,al,dd,ee=Q(3),Q(2),Q(5),Q(7)
    Rjet=add(scale(p,-h),scale(power(p,3),-3)); Fjet=scale(p,al*h); Gjet=scale(p,ee+dd*h)
    aj=scale(power(Rjet,2),3) if mode=='--mutate-omit-alphaG' else add(scale(power(Rjet,2),3),scale(one,al))
    Hjet=add(mul(aj,Gjet),scale(Fjet,-dd),scale(mul(Rjet,power(Fjet,2)),Q(-5,3)))
    need(Hjet.get((0,1,0),0)==al*ee and Hjet.get((0,3,0),0)==3*h*h*ee+3*dd*h**3+Q(5,3)*al*al*h**3,'actual scalar-kernel jet identity')
    scalar_kernel=scale(Rjet,2)
    if mode!='--mutate-drop-scalar-cubic': scalar_kernel=add(scalar_kernel,scale(power(Rjet,3),4))
    need(scalar_kernel.get((0,3,0),0)==2*Q(-3)-4*h**3,'actual retained scalar cubic coefficient')
    # Exact moving-coordinate parity toy: z=g+s*p, g=z-s*p.
    z=add(g,mul(s,p)); CC=one if mode=='--mutate-constant-C' else power(p,2)
    FF=add(mul(power(s,3),mul(z,CC)),mul(power(s,4),power(p,3)),mul(power(s,3),power(z,3)))
    transverse=substitute(FF,(add(g,scale(mul(s,p),-1)),p,s))
    even={ex:c for ex,c in transverse.items() if ex[1]%2==0}
    need(even==add(mul(power(s,3),mul(g,power(p,2))),mul(power(s,3),power(g,3))),'nonconstant even leading transverse coefficient')
    # Half-integral valuation arithmetic, not sampled mathematical points.
    j,a,f,d=Q(8),Q(7),Q(11),Q(14)
    need(min(d+f,a/2+2*f)>=3*j and f<=j+a/2 and a<j,'remaining interval is not removed by proved valuation bound')
    return {'status':'PASS','zero_assert_nodes':True,'actual_generator_lifts':[wire(z) for z in lifts],
            'universal_H_first_possible_order':min(ex[3] for ex in H),
            'low_residual_x2_minus_3ky':wire(low2),'low_residual_e_minus_5kx_over9':wire(low1),
            'scalar_jet_p1':str(Hjet[(0,1,0)]),'scalar_jet_p3':str(Hjet[(0,3,0)]),
            'necessary_bound':'3*ord(alpha)>=2*j','remaining_interval':'2*j/3<=ord(alpha)<j',
            'scope':'source-derived necessary valuation bound; unguarded nilpotent countercontrol fails saturated lows; no arc or point claim'}

def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25)); resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,512*1024*1024))

if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else ''
    if mode=='--record':
        modes=[('',None),('--mutate-delta-sign',b'universal pre-3j mixed identity'),('--mutate-intermediate',b'universal pre-3j mixed identity'),
               ('--mutate-omit-alphaG',b'actual scalar-kernel jet identity'),('--mutate-drop-scalar-cubic',b'actual retained scalar cubic coefficient'),('--mutate-constant-C',b'nonconstant even leading transverse coefficient')]
        records=[]
        for opt in (False,True):
            for mutation,msg in modes:
                out=subprocess.run([sys.executable,'-B']+(['-O'] if opt else [])+[str(Path(__file__).resolve())]+([mutation] if mutation else []),capture_output=True,timeout=30,preexec_fn=caps)
                need((out.returncode!=0)==bool(mutation),'unexpected low-alpha control exit')
                if mutation: need(msg in out.stderr,'wrong mutation failure')
                else:
                    with (HERE/('final-witness-O.json' if opt else 'final-witness.json')).open('xb') as f: f.write(out.stdout)
                records.append({'optimized':opt,'mutation':mutation or None,'returncode':out.returncode,'stdout_sha256':hashlib.sha256(out.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(out.stderr).hexdigest()})
        need((HERE/'final-witness.json').read_bytes()==(HERE/'final-witness-O.json').read_bytes(),'normal optimized witness equality')
        with (HERE/'final-replay.json').open('x') as f: json.dump({'status':'PASS','runs':records,'caps':'30wall25CPU512MiB each','writers_finished':True},f,sort_keys=True,indent=2); f.write('\n')
        print(json.dumps({'status':'PASS','runs':len(records),'witness_sha256':hashlib.sha256((HERE/'final-witness.json').read_bytes()).hexdigest()}))
    else: print(json.dumps(check(mode),sort_keys=True,indent=2))
