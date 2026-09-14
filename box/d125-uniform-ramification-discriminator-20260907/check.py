#!/usr/bin/env python3
"""Tiny exact controls for the uniform valuation/remainder argument; no source expansion."""
import sys
sys.dont_write_bytecode = True
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
spec=importlib.util.spec_from_file_location('uniform_frozen_helpers',DEP)
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
add,scale,mul,power,bracket,need,wire,substitute=(getattr(m,n) for n in ('add','scale','mul','power','bracket','need','wire','substitute'))

def check(mode):
    need(sys.dont_write_bytecode,'bytecode disabled')
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text()))),'zero Assert nodes')
    one={(0,0,0):Q(1)}; g={(1,0,0):Q(1)}; p={(0,1,0):Q(1)}; s={(0,0,1):Q(1)}
    gi={(-1,0,0):Q(1)}
    trunc=lambda z,a:{e:c for e,c in z.items() if e[2]<=a}
    coeff=lambda z,a:{(i,j,0):c for (i,j,k),c in z.items() if k==a}
    # Genuine moving reference, including orders not multiples of the departure.
    R=add(g,mul(s,p),mul(power(s,2),power(p,3)))
    W=add(g,p,mul(s,power(p,2)),mul(power(s,2),mul(g,p)))
    N=add(power(p,3),mul(power(g,2),p))
    moving=[]
    for a in (2,3):
        M=add(mul(R,W),mul(power(s,a),N))
        if mode=='--mutate-moving-term': M=add(M,scale(mul(s,mul(p,add(g,p))),-1))
        delta=mul(gi,add(mul(s,p),mul(power(s,2),power(p,3))))
        inv={}
        for ell in range(a+1): inv=add(inv,scale(mul(gi,power(delta,ell)),(-1)**ell))
        ratio=trunc(mul(M,inv),a)
        expected=trunc(add(W,mul(power(s,a),mul(N,gi))),a)
        need(ratio==expected,'moving remainder identity with all intermediate orders')
        need(all(i>=0 for i,j,k in ratio if k<a),'previous coefficients polynomial')
        need(min(i for i,j,k in coeff(ratio,a))==-1,'new remainder is simple pole only')
        moving.append({'a':a,'coefficient':wire(coeff(ratio,a))})
    # Cubic binomial coefficient and its three mixed placements.
    binomial=Q(5,3)*Q(2,3)*Q(-1,3)/6
    factor=binomial if mode=='--mutate-double-factor' else 3*binomial
    need(factor==Q(-5,27),'mixed cubic double-pole factor')
    # The earlier mixed-order cancellation is real, but fails at the next pole order.
    A=add(power(g,3),scale(mul(power(s,2),mul(g,power(p,2))),9),scale(mul(power(s,3),power(p,3)),9))
    B=add(power(g,5),scale(mul(power(s,2),mul(power(g,3),power(p,2))),15),
          scale(mul(power(s,3),mul(power(g,2),power(p,3))),15),
          scale(mul(power(s,4),mul(g,power(p,4))),45),scale(mul(power(s,5),power(p,5)),90))
    J=bracket(A,B)
    need(J=={(0,6,7):Q(2835)},'mixed square/cube toy first obstruction is order seven')
    # Exact ordinaryness kernel for the only possible leading T quotient slots.
    slots=[(i,n-i) for n in range(0,5,2) for i in range(n+1) if 5*i-7*(n-i)<=-8]
    need(slots==[(0,2),(0,4),(1,3)],'complete degree-four quotient slots')
    # Lift coordinates now (u,v,unused); g=v^-1, p=v^4u-v-v^-1.
    u=g; v=p; vi={(0,-1,0):Q(1)}
    phi_p=add(mul(power(v,4),u),scale(v,-1),scale(vi,-1))
    basis=[power(p,2),power(p,4),mul(g,power(p,3))]
    lifts=[substitute(z,(vi,phi_p,s)) for z in basis]
    matrix=[[z.get((0,-4,0),Q(0)) for z in lifts],[z.get((0,-2,0),Q(0)) for z in lifts]]
    need(matrix==[[0,1,-1],[1,4,-3]],'actual negative lift coefficient matrix')
    kernel=[Q(-1),Q(1),Q(1)]
    if mode=='--mutate-omit-low-lift': kernel=[Q(0),Q(1),Q(1)]
    candidate=add(*(scale(z,c) for z,c in zip(lifts,kernel)))
    need(all(j>=0 for i,j,k in candidate),'both negative lift rows are necessary')
    # Origin filtration: dropping no-linear-A invalidates the new kernel argument.
    bad_X1={( -2,1,0):Q(1,3)} # A=g^3+s*p, X=(A)^(1/3).
    need(min(i+j for i,j,k in bad_X1)==-1,'actual no-linear-A countercontrol')
    allowed=[r for r in range(-7,8) if r>=1 and 5*r<=23 and r%2==1]
    if mode=='--mutate-origin-bound': allowed=[r for r in range(-7,8) if 5*r<=23 and r%2==1]
    need(allowed==[1,3],'origin and infinity force only R and R^3 kernels')
    # Finite arithmetic sanity checks supplement, not replace, symbolic inequalities.
    for n in range(1,13):
        for j in range(1,n+1):
            need(Q(7*j,2)<min(6*n,3*n+j),'gamma and target occur after double pole')
    return {'status':'PASS','assert_nodes':0,'moving_remainders':moving,
            'mixed_toy_J':wire(J),'negative_lift_matrix':[[str(x) for x in row] for row in matrix],
            'lift_kernel':[str(x) for x in kernel],'localized_kernel_exponents':allowed,
            'double_factor':str(factor),'scope':'small exact bookkeeping, no full source expansion or arc witness'}

def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25))
    resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,512*1024*1024))

if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else ''
    if mode=='--record':
        modes=[('',None),('--mutate-moving-term',b'moving remainder identity'),
               ('--mutate-double-factor',b'mixed cubic double-pole factor'),
               ('--mutate-omit-low-lift',b'both negative lift rows'),
               ('--mutate-origin-bound',b'origin and infinity force')]
        records=[]
        for opt in (False,True):
            for mutation,msg in modes:
                out=subprocess.run([sys.executable,'-B']+(['-O'] if opt else [])+[str(Path(__file__).resolve())]+([mutation] if mutation else []),capture_output=True,timeout=30,preexec_fn=caps)
                need((out.returncode!=0)==bool(mutation),'unexpected uniform control exit')
                if mutation: need(msg in out.stderr,'wrong mutation failure')
                else:
                    with (HERE/('witness-O.json' if opt else 'witness.json')).open('xb') as f: f.write(out.stdout)
                records.append({'optimized':opt,'mutation':mutation or None,'returncode':out.returncode,
                                'stdout_sha256':hashlib.sha256(out.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(out.stderr).hexdigest()})
        need((HERE/'witness.json').read_bytes()==(HERE/'witness-O.json').read_bytes(),'normal -O bytes equal')
        with (HERE/'replay.json').open('x') as f:
            json.dump({'status':'PASS','caps':'30wall25CPU512MiB each','runs':records,'writers_finished':True},f,sort_keys=True,indent=2); f.write('\n')
        print(json.dumps({'status':'PASS','runs':len(records),'witness_sha256':hashlib.sha256((HERE/'witness.json').read_bytes()).hexdigest()}))
    else: print(json.dumps(check(mode),sort_keys=True,indent=2))
