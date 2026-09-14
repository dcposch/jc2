#!/usr/bin/env python3
"""Tiny ring/parameter controls; no source polynomials or theorem replay."""
import sys
sys.dont_write_bytecode=True
import ast
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import resource
import subprocess
HERE=Path(__file__).resolve().parent
def need(x,msg):
    if not x: raise ValueError(msg)
def add(*ps):
    out={}
    for p in ps:
        for e,c in p.items(): out[e]=out.get(e,F(0))+c
    return {e:c for e,c in out.items() if c}
def scale(p,c): return {e:v*c for e,v in p.items() if v*c}
def mul(p,q):
    out={}
    for e,c in p.items():
        for f,d in q.items():
            h=tuple(a+b for a,b in zip(e,f)); out[h]=out.get(h,F(0))+c*d
    return {e:c for e,c in out.items() if c}
def power(p,n):
    out={(0,0):F(1)}
    for _ in range(n): out=mul(out,p)
    return out
def wire(p): return [[list(e),str(c)] for e,c in sorted(p.items())]
def check(mode):
    need(not any(isinstance(x,ast.Assert) for x in ast.walk(ast.parse(Path(__file__).read_text()))),'zero Assert nodes')
    one={(0,0):F(1)}; k={(1,0):F(1)}; w={(0,1):F(1)}
    kw=mul(k,w); H=add(kw,scale(one,1 if mode=='--change-hyperbola' else -1))
    point=sum(c*F(2)**e[0]*F(1,2)**e[1] for e,c in H.items())
    need(point==0,'actual nonempty hyperbola point')
    need(add(kw,scale(H,-1))==one,'exact boundary unit certificate')
    crt=add(mul(power(k,2),power(w,2)),scale(mul(H,add(kw,one)),1 if mode=='--change-CRT-sign' else -1))
    need(crt==one,'exact comaximal CRT certificate')
    # Dual numbers with actual epsilon !=0; the mutation changes epsilon^2=0 to epsilon^2=epsilon.
    def dual_mul(a,b):
        eps_square=1 if mode=='--change-nilpotent-algebra' else 0
        return (a[0]*b[0],a[0]*b[1]+a[1]*b[0]+eps_square*a[1]*b[1])
    eps=(F(0),F(1)); K=(F(2),F(0)); W=(F(1,2),F(0))
    need(eps!=(0,0) and dual_mul(eps,eps)==(0,0) and dual_mul(K,W)==(1,0),'actual nonreduced unit-k algebra')
    # Full target shear, not beta alone.
    al,be,ga,lam=F(2),F(3),F(4),F(5)
    delta=ga-be*al+F(5,9)*al*al
    newga=ga if mode=='--omit-gamma-shear' else ga-lam*al
    need(newga-(be-lam)*al+F(5,9)*al*al==delta,'actual beta gamma shear invariant')
    # Scalar parameter series only: k=s^3*8(1+s)^3, tau=2s(1+s).
    s=k; unit=scale(power(add(one,s),3),8); kk=mul(power(s,3),unit)
    vv=add(scale(one,2),scale(s,3 if mode=='--change-unit-root' else 2)); tau=mul(s,vv)
    need(power(tau,3)==kk,'actual unit-root parameter identity')
    return {'status':'PASS','zero_assert_nodes':True,'hyperbola_point':['2','1/2'],'CRT_certificate':wire(crt),'nonreduced_epsilon':['0','1'],'delta_invariant':str(delta),'unit_root_k':wire(kk),'scope':'nonempty toy algebras and scalar parameter identities, not actual D125 points or scheme-proof substitutes'}
def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25)); resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,512*1024*1024))
if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else ''
    if mode=='--record':
        modes=[('',None),('--change-hyperbola',b'actual nonempty hyperbola point'),('--change-CRT-sign',b'exact comaximal CRT certificate'),('--change-nilpotent-algebra',b'actual nonreduced unit-k algebra'),('--omit-gamma-shear',b'actual beta gamma shear invariant'),('--change-unit-root',b'actual unit-root parameter identity')]
        runs=[]
        for opt in (False,True):
            for mutation,msg in modes:
                result=subprocess.run([sys.executable,'-I','-B']+(['-O'] if opt else [])+[str(Path(__file__).resolve())]+([mutation] if mutation else []),capture_output=True,timeout=30,preexec_fn=caps)
                need((result.returncode!=0)==bool(mutation),'unexpected control exit')
                if mutation: need(msg in result.stderr,'wrong mutation failure')
                else:
                    with (HERE/('witness-O.json' if opt else 'witness.json')).open('xb') as stream: stream.write(result.stdout)
                runs.append({'optimized':opt,'mutation':mutation or None,'returncode':result.returncode,'stdout_sha256':hashlib.sha256(result.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(result.stderr).hexdigest()})
        need((HERE/'witness.json').read_bytes()==(HERE/'witness-O.json').read_bytes(),'normal optimized bytes differ')
        with (HERE/'replay.json').open('x') as stream: json.dump({'status':'PASS','runs':runs,'caps':'30wall25CPU512MiB each','writers_finished':True},stream,sort_keys=True,indent=2); stream.write('\n')
        print(json.dumps({'status':'PASS','runs':len(runs),'witness_sha256':hashlib.sha256((HERE/'witness.json').read_bytes()).hexdigest()}))
    else: print(json.dumps(check(mode),sort_keys=True,indent=2))
