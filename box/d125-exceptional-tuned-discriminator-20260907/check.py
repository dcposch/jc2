#!/usr/bin/env python3
"""Polynomial critical-fiber identity and small literal support/lift controls."""
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
spec=importlib.util.spec_from_file_location('tuned_frozen_helpers',DEP)
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
add,scale,mul,power,bracket,need,wire,substitute=(getattr(m,n) for n in ('add','scale','mul','power','bracket','need','wire','substitute'))

def check(mode):
    need(sys.dont_write_bytecode,'bytecode disabled')
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text()))),'zero Assert nodes')
    one={(0,0,0):Q(1)}; g={(1,0,0):Q(1)}; p={(0,1,0):Q(1)}; s={(0,0,1):Q(1)}
    # R=g is explicitly a small formal control, never the actual degree-five source power.
    R=g
    alpha=add(scale(one,2),s,scale(power(s,2),2))
    beta=add(scale(one,3),scale(s,2),power(s,3))
    delta=add(power(s,2),scale(power(s,4),3))
    gamma=add(mul(beta,alpha),scale(power(alpha,2),Q(-5,9)),delta)
    a=add(scale(power(R,2),3),alpha)
    q=add(scale(power(R,2),Q(5,3)),beta,scale(alpha,Q(-5,9)))
    F=add(mul(power(s,3),power(p,3)),mul(power(s,4),mul(g,power(p,2))),mul(power(s,5),mul(power(g,2),p)))
    G=add(mul(power(s,4),mul(g,power(p,2))),scale(mul(power(s,5),power(p,3)),2))
    f=add(power(R,3),mul(alpha,R))
    h=add(power(R,5),mul(beta,power(R,3)),mul(gamma,R))
    A=add(f,F); B=add(h,mul(q,F),G)
    coefficient=Q(-5,9) if mode=='--mutate-quadratic-factor' else Q(-5,3)
    E=add(mul(a,G),scale(mul(delta,F),-1),scale(mul(R,power(F,2)),coefficient))
    cross={} if mode=='--mutate-omit-cross' else bracket(F,G)
    need(bracket(A,B)==add(bracket(R,E),cross),'complete polynomial identity including moving parameters and cross bracket')
    need(bracket(F,G)!={},'cross-bracket omission is a real change')
    # Actual reference-kernel removal shifts qF at the later mixed order.
    shift=power(s,3); eta=Q(2); theta=Q(5)
    beta_new=add(beta,scale(shift,eta)); gamma_new=add(gamma,scale(shift,theta))
    q_new=add(scale(power(R,2),Q(5,3)),beta_new,scale(alpha,Q(-5,9)))
    h_new=add(power(R,5),mul(beta_new,power(R,3)),mul(gamma_new,R))
    G_new=add(B,scale(h_new,-1),scale(mul(q_new,F),-1))
    expected=add(G,scale(mul(shift,power(R,3)),-eta),scale(mul(shift,R),-theta))
    if mode!='--mutate-omit-reference-cross': expected=add(expected,scale(mul(shift,F),-eta))
    need(G_new==expected,'reference removal retains beta_l*s^l*F correction')
    delta_new=add(gamma_new,scale(mul(beta_new,alpha),-1),scale(power(alpha,2),Q(5,9)))
    need(delta_new==add(delta,scale(shift,theta),scale(mul(shift,alpha),-eta)),'delta changes with actual scalar kernels')
    # The literal small source generator and U lift; no actual powers of R.
    V=add(power(g,3),power(p,3),scale(p,-3)); literal_R=mul(power(p,2),V)
    slots=[(i,n-i) for n in (1,3) for i in range(n+1) if 5*i-7*(n-i)<=1]
    need(slots==[(0,1),(0,3),(1,2)],'complete cubic U slots without lower-edge transport')
    vi={(0,-1,0):Q(1)}
    phi_p=add(mul(power(p,4),g),scale(p,-1),scale(vi,-1))
    basis=[p,power(p,3),mul(g,power(p,2))]
    lifted=[substitute(z,(vi,phi_p,s)) for z in basis]
    matrix=[[z.get((0,-3,0),Q(0)) for z in lifted],[z.get((0,-1,0),Q(0)) for z in lifted]]
    need(matrix==[[0,-1,1],[-1,-3,2]],'literal two-row U lift matrix')
    S_lift=add(scale(lifted[0],-1),lifted[1],lifted[2])
    need(all(j>=0 for i,j,k in S_lift),'unique U kernel is ordinary')
    R_lift=substitute(literal_R,(vi,phi_p,s))
    need(all(j>=0 for i,j,k in R_lift),'literal exceptional R ordinary')
    need({e:c for e,c in R_lift.items() if e[1]==0}==scale(g,3),'literal R lift at v=0')
    # F=cR+a*dS has low vector (-alpha*d, -3c+alpha*d).
    al=Q(-3)
    def lowcheck(c,d):
        row_p=-al*d; row_p3=-3*c+al*d
        return row_p==0 and (True if mode=='--mutate-omit-p3-reference' else row_p3==0)
    need(lowcheck(Q(0),Q(0)) and not lowcheck(Q(1),Q(0)) and not lowcheck(Q(0),Q(1)),'both low-A and p3 reference remove c,d')
    need(-3*al!=0,'low-reference matrix determinant is a scalar unit')
    # Critical quadratic has a nonzero coefficient because alpha !=0 gives r !=0.
    r=Q(1); alcrit=-3*r*r
    need(alcrit!=0 and Q(-5,3)*r!=0,'nonzero critical quadratic coefficient')
    for j in range(1,13):
        for mm in range(j,13): need(2*j<3*mm,'quadratic test precedes target order')
    return {'status':'PASS','assert_nodes':0,
            'identity':'J(A,B)=[R,aG-delta*F-(5/3)R*F^2]+[F,G]',
            'reference_G_change':'-eta*s^l*R^3-theta*s^l*R-eta*s^l*F',
            'reference_delta_change':'theta*s^l-eta*s^l*alpha(s)',
            'U_slots':slots,'U_negative_matrix':[[str(x) for x in row] for row in matrix],
            'S_lift':wire(S_lift),'source_R_lift':wire(R_lift),
            'scope':'small exact identities/support only, no actual full source power or arc witness'}

def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25)); resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,512*1024*1024))

if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else ''
    if mode=='--record':
        modes=[('',None),('--mutate-quadratic-factor',b'complete polynomial identity'),('--mutate-omit-cross',b'complete polynomial identity'),
               ('--mutate-omit-reference-cross',b'reference removal retains'),('--mutate-omit-p3-reference',b'both low-A and p3 reference')]
        records=[]
        for opt in (False,True):
            for mutation,msg in modes:
                out=subprocess.run([sys.executable,'-B']+(['-O'] if opt else [])+[str(Path(__file__).resolve())]+([mutation] if mutation else []),capture_output=True,timeout=30,preexec_fn=caps)
                need((out.returncode!=0)==bool(mutation),'unexpected tuned control exit')
                if mutation: need(msg in out.stderr,'wrong mutation failure')
                else:
                    with (HERE/('witness-O.json' if opt else 'witness.json')).open('xb') as f: f.write(out.stdout)
                records.append({'optimized':opt,'mutation':mutation or None,'returncode':out.returncode,
                                'stdout_sha256':hashlib.sha256(out.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(out.stderr).hexdigest()})
        need((HERE/'witness.json').read_bytes()==(HERE/'witness-O.json').read_bytes(),'normal -O witness equality')
        with (HERE/'replay.json').open('x') as f: json.dump({'status':'PASS','runs':records,'caps':'30wall25CPU512MiB each','writers_finished':True},f,sort_keys=True,indent=2); f.write('\n')
        print(json.dumps({'status':'PASS','runs':len(records),'witness_sha256':hashlib.sha256((HERE/'witness.json').read_bytes()).hexdigest()}))
    else: print(json.dumps(check(mode),sort_keys=True,indent=2))
