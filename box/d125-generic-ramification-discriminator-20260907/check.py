#!/usr/bin/env python3
"""Exact mixed-order toy; actual source support/lift checks stop at degree five."""
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
PIN='25be0862730df8b66076eb59a2d1d0909fbcf563ea73ce16924affdc7c70ad66'
if hashlib.sha256(DEP.read_bytes()).hexdigest()!=PIN: raise RuntimeError('helper drift')
spec=importlib.util.spec_from_file_location('frozen_helpers',DEP)
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
add,scale,mul,power,derivative,bracket,substitute,need,wire=(getattr(m,n) for n in
    ('add','scale','mul','power','derivative','bracket','substitute','need','wire'))

def check(mode):
    need(sys.dont_write_bytecode,'bytecode must be disabled')
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text()))),'Assert node')
    one={(0,0,0):Q(1)}; g={(1,0,0):Q(1)}; p={(0,1,0):Q(1)}; s={(0,0,1):Q(1)}
    # Independent variables R=g,S=p: only degree-three/five toy powers.
    R=g; S=p
    A=add(power(R,3),scale(mul(power(s,2),mul(R,power(S,2))),9),scale(mul(power(s,3),power(S,3)),9))
    B=add(power(R,5),scale(mul(power(s,2),mul(power(R,3),power(S,2))),15),
          scale(mul(power(s,3),mul(power(R,2),power(S,3))),15),
          scale(mul(power(s,4),mul(R,power(S,4))),45),scale(mul(power(s,5),power(S,5)),90))
    if mode=='--mutate-drop-mixed-orders':
        A=add(A,scale(mul(power(s,3),power(S,3)),-9))
        B=add(B,scale(mul(power(s,3),mul(power(R,2),power(S,3))),-15),scale(mul(power(s,5),power(S,5)),-90))
    J=bracket(A,B)
    need({e:a for e,a in J.items() if e[2]<=6}=={},'mixed orders are required through order six')
    need(J=={(0,6,7):Q(2835)},'exact first failure is order seven')
    if mode=='--mutate-full-arc-claim': need(J=={},'finite toy is not a full commuting arc')
    # Cubic residue's two terms cancel only when the transverse s^3 term is retained.
    C=scale(power(p,2),9); D=scale(power(p,3),9)
    need(add(scale(power(D,2),Q(5,9)),scale(power(C,3),Q(-5,81)))=={},'square/cube pole cancellation')
    # Actual R_t and S=partial_t R_t: neither A nor B is expanded after substitution.
    t=s; tp3=add(t,scale(one,3))
    H=add(power(p,5),mul(power(g,3),power(p,2)))
    realR=add(H,mul(tp3,mul(g,power(p,2))),mul(t,power(p,3)),scale(mul(tp3,p),-1))
    realS=add(power(p,3),mul(g,power(p,2)),scale(p,-1))
    need(derivative(realR,2)==realS,'literal derivative generator')
    need(all((i+j)%2==1 for i,j,z in realS),'S odd')
    need(max(i+j for i,j,z in realS)==3 and max(5*i-7*j for i,j,z in realS)==-7,'S support')
    need(min(j for i,j,z in realR)==1 and min(j for i,j,z in realS)==1,'p divisibility of both generators')
    need(max(i-2*j for i,j,z in realR)==-1 and max(i-2*j for i,j,z in realS)==-2,'lower support bounds')
    vi={(0,-1,0):Q(1)}; phip=add(mul(power(p,4),g),scale(p,-1),scale(vi,-1))
    for V in (realR,realS): need(all(e[1]>=0 for e in substitute(V,(vi,phip,t))),'both generators lift ordinarily')
    # Factored support arithmetic on powers: [R exponent,S exponent,s order,scalar].
    termsA=[(3,0,0,1),(1,2,2,9),(0,3,3,9)]
    termsB=[(5,0,0,1),(3,2,2,15),(2,3,3,15),(1,4,4,45),(0,5,5,90)]
    bounds={}
    for name,terms,degree,weight in [('A',termsA,15,3),('B',termsB,25,5)]:
        rows=[]
        for r,z,order,c in terms:
            deg=5*r+3*z; w=r-7*z; ell=-r-2*z; pval=r+z
            need(deg<=degree and w<=weight and (r+z)%2==1,'factored closed support and parity')
            if order: need(deg<degree and w<weight,'every correction below both fixed faces')
            if name=='A': need(ell<=0 and pval>=3,'A lower side and p cubed')
            else: need(pval>=5,'B p to fifth')
            rows.append([r,z,order,deg,w,ell,pval])
        bounds[name]=rows
    # Every A term divisible by p^3: literal x=[g p^2]A is exactly zero.
    toy_x=Q(0)
    if mode=='--mutate-guarded-s4-survivor':
        h=Q(3)
        need(toy_x*toy_x==-3*h**3,'zero x cannot satisfy saturated k=s4 leading row')
    # Same-field t(s) from y=-h(s)^3, verified as a Laurent identity in h.
    h=g; hi={(-1,0,0):Q(1)}
    hs=add(h,scale(mul(hi,power(s,2)),3),scale(mul(power(hi,2),power(s,3)),3))
    cube=power(hs,3)
    need({e:c for e,c in cube.items() if e[2]<=3}==add(power(h,3),scale(mul(h,power(s,2)),9),scale(power(s,3),9)),'moving reference cube through order three')
    need(add(mul(tp3,realS),scale(realR,-1))==add(scale(power(p,3),3),scale(H,-1)),'nonzero normalized tangent factor')
    # Test noncommutativity of actual R,S by a tiny exact derivative evaluation, not a search.
    def at_one_zero(V): return sum(c for (i,j,z),c in V.items() if z==0)
    actualJat=at_one_zero(derivative(realR,0))*at_one_zero(derivative(realS,1))-at_one_zero(derivative(realR,1))*at_one_zero(derivative(realS,0))
    need(actualJat==14 and at_one_zero(realS)==1,'actual source fails at order seven')
    return {'status':'PASS','assert_nodes':0,'bytecode_disabled':True,'toy_jacobian':wire(J),
            'factored_bound_order':['R_exp','S_exp','s_order','degree_bound','weight_bound','lower_bound','p_valuation'],
            'factored_bounds':bounds,'toy_x':'0','actual_J_R_S_at_g1_p1_t0':'14',
            'reference_t_coefficients':{'s2':'3/(t+3)','s3':'3/(t+3)^2'},
            'scope':'genuine finite zero-k source jet only; no guarded survivor or all-ramification exclusion'}

def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25)); resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,512*1024*1024))

if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else ''
    if mode=='--record':
        records=[]
        modes=['','--mutate-drop-mixed-orders','--mutate-full-arc-claim','--mutate-guarded-s4-survivor']
        messages=[None,b'mixed orders are required through order six',b'finite toy is not a full commuting arc',b'zero x cannot satisfy saturated k=s4 leading row']
        for opt in (False,True):
            for mutation,msg in zip(modes,messages):
                cmd=[sys.executable,'-B']+(['-O'] if opt else [])+[str(Path(__file__).resolve())]+([mutation] if mutation else [])
                out=subprocess.run(cmd,capture_output=True,timeout=30,preexec_fn=caps)
                need((out.returncode!=0)==bool(mutation),'unexpected control status')
                if mutation: need(msg in out.stderr,'unrelated mutation failure')
                else:
                    with (HERE/('witness-O.json' if opt else 'witness.json')).open('xb') as f: f.write(out.stdout)
                records.append({'optimized':opt,'mutation':mutation or None,'returncode':out.returncode,
                                'stdout_sha256':hashlib.sha256(out.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(out.stderr).hexdigest()})
        need((HERE/'witness.json').read_bytes()==(HERE/'witness-O.json').read_bytes(),'normal optimized equality')
        with (HERE/'replay.json').open('x') as f:
            json.dump({'status':'PASS','runs':records,'caps':'30wall/25CPU seconds,512MiB','writers_finished':True},f,sort_keys=True,indent=2); f.write('\n')
        print(json.dumps({'status':'PASS','runs':len(records),'witness_sha256':hashlib.sha256((HERE/'witness.json').read_bytes()).hexdigest()}))
    else: print(json.dumps(check(mode),sort_keys=True,indent=2))
