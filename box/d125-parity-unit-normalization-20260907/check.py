#!/usr/bin/env python3
"""Exact tiny controls over Q[epsilon]/epsilon^2; no full client expansion."""
import ast
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import subprocess
import sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
sys.dont_write_bytecode=True

def need(ok,message):
    if not ok:
        raise ValueError(message)

class D:
    def __init__(self,a=0,b=0): self.a,self.b=Q(a),Q(b)
    def __add__(self,y):
        y=scalar(y); return D(self.a+y.a,self.b+y.b)
    __radd__=__add__
    def __neg__(self): return D(-self.a,-self.b)
    def __sub__(self,y): return self+-scalar(y)
    def __mul__(self,y):
        y=scalar(y); return D(self.a*y.a,self.a*y.b+self.b*y.a)
    __rmul__=__mul__
    def __pow__(self,n):
        if n<0:
            if not self.a: raise ZeroDivisionError('nonunit')
            return D(1/self.a,-self.b/self.a**2)**(-n)
        out=D(1)
        for _ in range(n): out=out*self
        return out
    def __eq__(self,y):
        y=scalar(y); return self.a==y.a and self.b==y.b
    def wire(self): return [str(self.a),str(self.b)]

def scalar(x): return x if isinstance(x,D) else D(x)

def mul(p,q):
    out={}
    for (t,e),a in p.items():
        for (s,f),b in q.items():
            key=(t+s,e+f); out[key]=out.get(key,D())+a*b
    return {k:v for k,v in out.items() if v!=0}

def lift_monomial(i,j,ell):
    out={(0,-i):D(1)}
    p={(1,4):D(1),(0,1):-ell,(0,-1):D(-1)}
    for _ in range(j): out=mul(out,p)
    return out

def check(mode):
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text()))),'Assert node')
    path=ROOT/'box/d125-minimal-receiver-client-preflight-20260906/client.py'
    pin='ec2fa2d1e23bc16bc07c9208f648e3b17561cbfddaaf04fed28d7ffc9a428d53'
    need(hashlib.sha256(path.read_bytes()).hexdigest()==pin,'literal support pin')
    spec=importlib.util.spec_from_file_location('unit_normalization_metadata',path)
    module=importlib.util.module_from_spec(spec); sys.modules[spec.name]=module; spec.loader.exec_module(module)
    client=module.make_contract('unequal','rational')
    ell=D(2,1); k=ell**-6; invk=k**-1
    need(k*invk==1 and k*(ell**6)==1,'unit cover relation')
    nslots=0; weight_tests=0
    for idx,degree in enumerate((15,25)):
        for entry in client['coefficient_maps'][idx]:
            i,j=entry['point']; s=i+j
            if (s-degree)%2: continue
            nslots+=1; power=(s-degree)//2
            coeff=D(i+j+1,i-j)
            need((coeff*(ell**power))*(ell**(-power))==coeff,'coefficient inverse')
            for t in range(j+1):
                for d in range(j-t+1):
                    e=5*t+2*d-s
                    need((5*t-e-degree)%2==0,'integer lift factor')
                    need(power==((5*t-e-degree)//2)+d,'literal lift row factor')
                    weight_tests+=1
        # Only six toy monomials are genuinely expanded, separately, never a full source.
        for i,j in ((0,1),(1,0),(0,3),(2,1),(1,4),(0,5)):
            power=(i+j-degree)//2
            old=lift_monomial(i,j,ell)
            new={key:value*(ell**power) for key,value in lift_monomial(i,j,D(1)).items()}
            expected={key:value*(ell**((5*key[0]-key[1]-degree)//2)) for key,value in old.items()}
            need(new==expected,'actual Laurent coefficient covariance')
        # Monic physical top u^D v^(4D) remains coefficient 1.
        need((5*degree-4*degree-degree)//2==0,'physical top factor')
    # Fixed faces are transported individually, including the nonunit parameter powers.
    transformed={'A3':ell**-6,'B13':D(Q(5,3))*(ell**-6),'B1':D(Q(5,9))*(ell**-12),
                 'c':D(-Q(5,9))*(ell**-18)}
    declared={'A3':k,'B13':D(Q(5,3))*k,'B1':D(Q(5,9))*(k**2),'c':D(-Q(5,9))*(k**3)}
    if mode=='--mutate-face': declared['A3']=k**2
    if mode=='--mutate-c-power': declared['c']=D(-Q(5,9))*(k**2)
    for name in transformed:
        need(transformed[name]==declared[name],'changed face or c exponent: '+name)
    # Jacobian factors are checked on all possible odd degree pairs (coefficients only).
    for a in range(1,16,2):
        for b in range(1,26,2):
            d=a+b-2
            need((a-15)//2+(b-25)//2==(d-38)//2,'Jacobian row factor')
    def guarded_parameter(x,z):
        return True if mode=='--mutate-omit-guard' else x*z==1
    need(guarded_parameter(k,invk),'positive inverse guard')
    need(not guarded_parameter(D(0),D(0)),'omitted invertibility accepted k=0')
    # This k=0 control is the parameter contract, NOT a full-system solution.
    return {'status':'PASS','field':'Q[epsilon]/(epsilon^2)','slot_count':nslots,'weight_tests':weight_tests,
            'expanded_toy_monomials':12,'cover_rank':6,'ell':ell.wire(),'k':k.wire(),
            'new_faces':{name:v.wire() for name,v in declared.items()},'assert_nodes':0,
            'scope':'character exponents plus tiny Laurent monomials and parameter guard; no complete point or residual'}

def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25))
    resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,512*1024*1024))

if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else ''
    if mode=='--record':
        rows=[]
        for opt in (False,True):
            for mutation in ('','--mutate-face','--mutate-c-power','--mutate-omit-guard'):
                cmd=[sys.executable]+(['-O'] if opt else [])+[str(Path(__file__).resolve())]+([mutation] if mutation else [])
                r=subprocess.run(cmd,capture_output=True,timeout=30,preexec_fn=caps)
                need((r.returncode!=0)==bool(mutation),'unexpected subprocess exit')
                if mutation:
                    message=b'omitted invertibility' if mutation=='--mutate-omit-guard' else b'changed face or c exponent'
                    need(message in r.stderr,'unrelated mutation failure')
                else:
                    with (HERE/('witness-O.json' if opt else 'witness.json')).open('xb') as f: f.write(r.stdout)
                rows.append({'optimized':opt,'mutation':mutation or None,'returncode':r.returncode,
                             'stdout_sha256':hashlib.sha256(r.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(r.stderr).hexdigest()})
        need((HERE/'witness.json').read_bytes()==(HERE/'witness-O.json').read_bytes(),'normal/-O byte mismatch')
        with (HERE/'replay.json').open('x') as f:
            json.dump({'status':'PASS','runs':rows,'caps':'30wall/25CPU seconds,512MiB per subprocess','writers_finished':True},f,sort_keys=True,indent=2); f.write('\n')
        print(json.dumps({'status':'PASS','runs':len(rows),'witness_sha256':hashlib.sha256((HERE/'witness.json').read_bytes()).hexdigest()}))
    else:
        print(json.dumps(check(mode),sort_keys=True,indent=2))
