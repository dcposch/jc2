#!/usr/bin/env python3
"""Tiny degree-three source pairs and exact k-saturation identities."""
import ast
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import resource
import subprocess
import sys

HERE=Path(__file__).resolve().parent
N=10; ZERO=(0,)*N
def need(ok,msg):
    if not ok: raise ValueError(msg)
def clean(p): return {e:Q(c) for e,c in p.items() if c}
def add(*ps):
    out={}
    for p in ps:
        for e,c in p.items(): out[e]=out.get(e,Q(0))+c
    return clean(out)
def scale(p,c): return clean({e:c*v for e,v in p.items()})
def mul(p,q):
    out={}
    for e,a in p.items():
        for f,b in q.items():
            h=tuple(x+y for x,y in zip(e,f)); out[h]=out.get(h,Q(0))+a*b
    return clean(out)
def power(p,n):
    out={ZERO:Q(1)}
    for _ in range(n): out=mul(out,p)
    return out
def var(i):
    e=[0]*N; e[i]=1; return {tuple(e):Q(1)}
def derivative(p,i):
    out={}
    for e,c in p.items():
        if e[i]:
            f=list(e); f[i]-=1; out[tuple(f)]=c*e[i]
    return clean(out)
def bracket(p,q): return add(mul(derivative(p,8),derivative(q,9)),scale(mul(derivative(p,9),derivative(q,8)),-1))
def coeff(p,i,j):
    out={}
    for e,c in p.items():
        if e[8:]==(i,j):
            f=e[:8]+(0,0); out[f]=out.get(f,Q(0))+c
    return clean(out)
def evaluate(p,values): return sum((c*__import__('functools').reduce(lambda a,b:a*b,(values[i]**e[i] for i in range(N)),Q(1)) for e,c in p.items()),Q(0))
def wire(p): return [[list(e[:8]),str(c)] for e,c in sorted(p.items())]

def check(mode):
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text()))),'Assert node')
    k,a0,x,y,e,b21,b12,b03,g,p=[var(i) for i in range(N)]
    d=scale(power(k,2),Q(5,9))
    A1=mul(a0,p); A3=add(mul(k,mul(power(g,2),p)),mul(x,mul(g,power(p,2))),mul(y,power(p,3)))
    B1=add(mul(d,g),mul(e,p)); B3=add(mul(b21,mul(power(g,2),p)),mul(b12,mul(g,power(p,2))),mul(b03,power(p,3)))
    used_B3={} if mode=='--mutate-omit-A1B3' else B3
    J=bracket(add(A1,A3),add(B1,used_B3))
    r0=coeff(J,0,0); r11=coeff(J,1,1); r02=coeff(J,0,2)
    need(r0==scale(mul(d,a0),-1),'constant row')
    expected11=add(scale(mul(k,e),2),scale(mul(d,x),-2),scale(mul(a0,b21),-2))
    expected02=add(mul(x,e),scale(mul(d,y),-3),scale(mul(a0,b12),-1))
    need(r11==expected11 and r02==expected02,'missing A1-B3 contributions')
    need(add(coeff(J,2,0),scale(power(k,3),Q(5,9)))=={},'g2 target cancels exactly')
    h1=add(scale(e,9),scale(mul(k,x),-5)); h2=add(power(x,2),scale(mul(k,y),-3))
    cert0=scale(r0,Q(-9,5))
    cert1=add(scale(mul(power(k,2),r11),Q(9,2)),scale(mul(b21,r0),Q(-81,5)))
    cert2=add(scale(mul(power(k,3),r02),Q(9,5)),scale(mul(mul(x,power(k,2)),r11),Q(-9,10)),
              scale(mul(add(mul(x,b21),scale(mul(k,b12),-1)),r0),Q(81,25)))
    if mode=='--mutate-certificate-sign': cert2=add(cert2,scale(mul(mul(k,b12),r0),Q(162,25)))
    need(mul(power(k,2),a0)==cert0,'k2 a0 certificate')
    need(mul(power(k,3),h1)==cert1,'k3 h1 certificate')
    need(mul(power(k,4),h2)==cert2,'k4 h2 certificate')
    # Reverse ideal inclusion, without localization.
    need(r11==add(scale(mul(k,h1),Q(2,9)),scale(mul(a0,b21),-2)),'reverse gp identity')
    need(r02==add(scale(mul(x,h1),Q(1,9)),scale(mul(k,h2),Q(5,9)),scale(mul(a0,b12),-1)),'reverse p2 identity')
    # Actual unguarded low-row point: k=0,a0=1,x=1,others=0.
    point=[Q(0),Q(1),Q(1),Q(0),Q(0),Q(0),Q(0),Q(0),Q(0),Q(0)]
    need(all(evaluate(r,point)==0 for r in (r0,r11,r02)),'unguarded low-row point')
    need(evaluate(a0,point)==1 and evaluate(h2,point)==1,'unguarded new constraints genuinely fail')
    if mode=='--mutate-raw-equivalence':
        need(all(evaluate(r,point)==0 for r in (a0,h1,h2)),'unguarded equivalence is false')
    # Positive unit-graph fixture, with nonzero B3 ignored only because a0=0.
    kv=Q(2); xv=Q(3)
    positive=[kv,Q(0),xv,xv*xv/(3*kv),Q(5,9)*kv*xv,Q(7),Q(11),Q(13),Q(0),Q(0)]
    need(all(evaluate(r,positive)==0 for r in (r0,r11,r02,a0,h1,h2)),'unit graph fixture')
    return {'status':'PASS','coefficient_order':['k','a01','a12','a03','e','b21','b12','b03'],
            'rows':{'r0':wire(r0),'r_gp':wire(r11),'r_p2':wire(r02)},
            'saturated_generators':{'a01':wire(a0),'h1':wire(h1),'h2':wire(h2)},
            'membership_powers':[2,3,4],'assert_nodes':0,
            'scope':'exact low-row identities only; unguarded fixture is not a full-source point'}

def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25)); resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,512*1024*1024))

if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else ''
    if mode=='--record':
        records=[]
        for opt in (False,True):
            for mutation in ('','--mutate-omit-A1B3','--mutate-certificate-sign','--mutate-raw-equivalence'):
                cmd=[sys.executable]+(['-O'] if opt else [])+[str(Path(__file__).resolve())]+([mutation] if mutation else [])
                result=subprocess.run(cmd,capture_output=True,timeout=30,preexec_fn=caps)
                need((result.returncode!=0)==bool(mutation),'unexpected subprocess exit')
                if mutation:
                    msg={'--mutate-omit-A1B3':b'missing A1-B3 contributions','--mutate-certificate-sign':b'k4 h2 certificate',
                         '--mutate-raw-equivalence':b'unguarded equivalence is false'}[mutation]
                    need(msg in result.stderr,'unrelated mutation failure')
                else:
                    with (HERE/('witness-O.json' if opt else 'witness.json')).open('xb') as f: f.write(result.stdout)
                records.append({'optimized':opt,'mutation':mutation or None,'returncode':result.returncode,
                                'stdout_sha256':hashlib.sha256(result.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(result.stderr).hexdigest()})
        need((HERE/'witness.json').read_bytes()==(HERE/'witness-O.json').read_bytes(),'normal/-O bytes')
        with (HERE/'replay.json').open('x') as f:
            json.dump({'status':'PASS','runs':records,'caps':'30wall/25CPU seconds,512MiB','writers_finished':True},f,sort_keys=True,indent=2); f.write('\n')
        print(json.dumps({'status':'PASS','runs':len(records),'witness_sha256':hashlib.sha256((HERE/'witness.json').read_bytes()).hexdigest()}))
    else:
        print(json.dumps(check(mode),sort_keys=True,indent=2))
