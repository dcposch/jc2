#!/usr/bin/env python3
"""Small Laurent order-seven identities and a unit-valued point certificate."""
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
add,scale,mul,power,bracket,need,wire=(getattr(m,n) for n in ('add','scale','mul','power','bracket','need','wire'))

def check(mode):
    need(sys.dont_write_bytecode,'no bytecode writes')
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text()))),'Assert node')
    one={(0,0,0):Q(1)}; g={(1,0,0):Q(1)}; p={(0,1,0):Q(1)}; s={(0,0,1):Q(1)}
    trunc=lambda z:{e:a for e,a in z.items() if e[2]<=7}
    divg=lambda z,n:{(i-n,j,k):a for (i,j,k),a in z.items()}
    # A genuinely moving reference R_s=g+s*p and all intermediate orders.
    R=add(g,mul(s,p)); C=scale(power(p,2),9); D0=add(scale(power(p,3),9),g)
    D1=add(power(p,3),mul(power(g,2),p)); Ds=add(D0,mul(s,D1))
    A=add(power(R,3),mul(power(s,2),mul(R,C)),mul(power(s,3),Ds))
    M0=add(scale(power(D0,2),Q(5,9)),scale(power(C,3),Q(-5,81)))
    M1=scale(mul(D0,D1),Q(10,9))
    need(all(i>=1 for i,j,k in M0),'nonzero M0 is divisible by R0')
    W0=divg(M0,1)
    simple7=add(divg(M1,1),scale(divg(mul(M0,p),2),-1))
    need(simple7==divg(add(M1,scale(mul(W0,p),-1)),1),'moving denominator derivative is only simple pole')
    if mode=='--mutate-omit-moving-derivative': simple7=divg(M1,1)
    double_factor=Q(-5,81) if mode=='--mutate-double-factor' else Q(-5,27)
    double7=scale(divg(mul(power(C,2),D0),2),double_factor)
    B=add(power(R,5),scale(mul(power(s,2),mul(power(R,3),C)),Q(5,3)),
          scale(mul(power(s,3),mul(power(R,2),Ds)),Q(5,3)),
          scale(mul(power(s,4),mul(R,power(C,2))),Q(5,9)),
          scale(mul(power(s,5),mul(C,Ds)),Q(10,9)),mul(power(s,6),W0),
          mul(power(s,7),add(simple7,double7)),scale(mul(power(s,6),R),2))
    need(trunc(bracket(A,B))=={},'actual moving-reference order-seven identity')
    # Gamma6 X has polynomial coefficient gamma6 R1 at order7.
    gamma7={e:a for e,a in scale(mul(power(s,6),R),2).items() if e[2]==7}
    need(gamma7==scale(mul(power(s,7),p),2),'gamma6 X order seven is not zero for moving R')
    # Actual localized-centralizer parity control.
    kernel={( -2 if mode=='--mutate-even-kernel' else -1,0,0):Q(1)}
    need(bracket(g,kernel)=={},'kernel really centralizes R')
    need(all((i+j)%2==1 for i,j,k in kernel),'even double-pole kernel is forbidden')
    # Exact fixed-prefix point: physical g=0, p=a, with b4=3 and a4-4a2+1=0.
    # The sparse variables below mean (b,a,unused), not source coordinates.
    b=g; a=p
    def reduce_point(z):
        out={}; pending=dict(z)
        while pending:
            (i,j,k),coef=pending.popitem()
            if not coef: continue
            if i>=4:
                e=(i-4,j,k); pending[e]=pending.get(e,Q(0))+3*coef
            elif j>=4:
                e=(i,j-2,k); pending[e]=pending.get(e,Q(0))+4*coef
                e=(i,j-4,k); constant=1 if mode=='--mutate-point-relation' else -1
                pending[e]=pending.get(e,Q(0))+constant*coef
            else: out[(i,j,k)]=out.get((i,j,k),Q(0))+coef
        return {e:z for e,z in out.items() if z}
    Tat=add(power(a,4),scale(power(a,2),-4),one)
    need(reduce_point(Tat)=={},'point must lie on literal T=0')
    Cat=mul(power(b,2),power(a,2)); Dat=scale(mul(power(b,3),power(a,3)),Q(1,3))
    numerator=scale(mul(power(Cat,2),Dat),Q(5,27))
    binv=scale(power(b,3),Q(1,3)); ainv=add(scale(a,4),scale(power(a,3),-1))
    inverse=scale(mul(power(binv,7),power(ainv,7)),Q(81,5))
    need(reduce_point(mul(numerator,inverse))==one,'double-pole numerator is a unit on exact point algebra')
    # Generic final support contradiction uses no ordinaryness assumption.
    quotient_slots=[(i,j) for n in range(0,5,2) for i in range(n+1) for j in [n-i] if 5*i-7*j<=-8]
    need(quotient_slots==[(0,2),(0,4),(1,3)],'all possible T-quotient slots')
    need(all((i,j)!=(1,1) and i+j>0 for i,j in quotient_slots),'T quotient cannot supply gp coefficient')
    return {'status':'PASS','assert_nodes':0,'double_pole_coefficient':'-5/27',
            'moving_derivative_identity':'M1/R0-M0*R1/R0^2=(M1-W0*R1)/R0',
            'gamma6_order7':'gamma6*R1 (polynomial)',
            'point_algebra':'Q[b,a]/(b^4-3,a^4-4a^2+1)',
            'point_unit_numerator':wire(reduce_point(numerator)),
            'point_unit_inverse':wire(reduce_point(inverse)),
            'T_quotient_slots':quotient_slots,
            'scope':'fixed-prefix obstruction and moving-reference identities only; no full source powers or solve'}

def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25)); resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,512*1024*1024))

if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else ''
    if mode=='--record':
        records=[]
        modes=['','--mutate-omit-moving-derivative','--mutate-double-factor','--mutate-even-kernel','--mutate-point-relation']
        messages=[None,b'actual moving-reference order-seven identity',b'actual moving-reference order-seven identity',b'even double-pole kernel is forbidden',b'point must lie on literal T=0']
        for opt in (False,True):
            for mutation,msg in zip(modes,messages):
                out=subprocess.run([sys.executable,'-B']+(['-O'] if opt else [])+[str(Path(__file__).resolve())]+([mutation] if mutation else []),capture_output=True,timeout=30,preexec_fn=caps)
                need((out.returncode!=0)==bool(mutation),'unexpected order-seven control exit')
                if mutation: need(msg in out.stderr,'unrelated mutation failure')
                else:
                    with (HERE/('witness-O.json' if opt else 'witness.json')).open('xb') as f: f.write(out.stdout)
                records.append({'optimized':opt,'mutation':mutation or None,'returncode':out.returncode,
                                'stdout_sha256':hashlib.sha256(out.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(out.stderr).hexdigest()})
        need((HERE/'witness.json').read_bytes()==(HERE/'witness-O.json').read_bytes(),'normal optimized equality')
        with (HERE/'replay.json').open('x') as f: json.dump({'status':'PASS','runs':records,'caps':'30wall25CPU512MiB','writers_finished':True},f,sort_keys=True,indent=2); f.write('\n')
        print(json.dumps({'status':'PASS','runs':len(records),'witness_sha256':hashlib.sha256((HERE/'witness.json').read_bytes()).hexdigest()}))
    else: print(json.dumps(check(mode),sort_keys=True,indent=2))
