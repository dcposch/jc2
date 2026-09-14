#!/usr/bin/env python3
"""Degree-five actual division and independent formal 3/5 identities only."""
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
spec=importlib.util.spec_from_file_location('high_alpha_helpers',DEP)
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
add,scale,mul,power,derivative,need,wire=(getattr(m,n) for n in ('add','scale','mul','power','derivative','need','wire'))

def normal_division(P,Rs):
    remain=dict(P); quo={}; out={}
    while remain:
        e=max(remain); c=remain[e]
        if e[0]>=3 and e[1]>=2:
            mon={(e[0]-3,e[1]-2,e[2]):c}; quo=add(quo,mon)
            remain=add(remain,scale(mul(mon,Rs),-1))
        else:
            out[e]=c; del remain[e]
    return quo,out

def check(mode):
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text()))),'zero Assert nodes')
    one={(0,0,0):Q(1)}; g={(1,0,0):Q(1)}; p={(0,1,0):Q(1)}; h={(0,0,1):Q(1)}
    V=add(power(g,3),power(p,3),scale(p,-3)); R=mul(power(p,2),V)
    S=add(power(p,3),mul(g,power(p,2)),scale(p,-1)); Rs=add(R,mul(h,S))
    divisor=add(Rs,mul(h,p)) if mode=='--omit-hp' else Rs
    examples=[R,Rs,mul(power(g,3),power(p,2)),add(R,power(p,5)),mul(g,power(p,4)),power(p,4)]
    division=[]
    for P in examples:
        qq,rr=normal_division(P,divisor)
        need(P==add(mul(Rs,qq),rr),'actual division reconstruction')
        need(all(i<3 or j<2 for i,j,k in rr),'actual monomial normal remainder')
        need(all(i+j<=5 for i,j,k in P),'actual input degree cap')
        bound=max(5*i-7*j for i,j,k in P)
        need(all(5*i-7*j<=bound for i,j,k in rr) and all(5*i-7*j<=bound-1 for i,j,k in qq),'actual weight preservation')
        division.append({'input':wire(P),'quotient':wire(qq),'remainder':wire(rr)})
    bad=mul(mul(g,p),V)
    candidate=bad if mode=='--wrong-filtered-input' else R
    need(max(5*i-7*j for i,j,k in candidate)<=5,'actual filtered input')
    need(any(j==1 for i,j,k in bad) and max(5*i-7*j for i,j,k in bad)==13,'missing-weight countercontrol')
    # Local curve identity: dp/dg=g^2/(1-p^2), so D=(1-p^2)/g^2*d/dg.
    need(derivative(V,1)==scale(add(power(p,2),scale(one,-1)),3) and derivative(V,0)==scale(power(g,2),3),'actual cubic derivatives')
    target=Q(-5,9) if mode=='--wrong-target-factor' else Q(-5,27)
    need(3*target==Q(-5,9),'actual target division factor')
    # Seven FORMAL variables (Z,a,b,da,db,k1,k3), not actual receiver products.
    zz=(0,)*7
    def var(i):
        ee=list(zz); ee[i]=1; return {tuple(ee):Q(1)}
    Z,a,b,da,db,k1,k3=[var(i) for i in range(7)]
    def pw(P,n):
        out={zz:Q(1)}
        for _ in range(n): out=mul(out,P)
        return out
    def DD(P): return add(mul(derivative(P,1),da),mul(derivative(P,2),db))
    PP=add(pw(Z,3),mul(a,Z),b)
    q3=add(scale(a,Q(5,3)),k3); q2=scale(b,Q(5,3)); q1=add(scale(pw(a,2),Q(5,9)),mul(k3,a),k1)
    q0=add(scale(mul(a,b),Q(5,9) if mode=='--wrong-q0' else Q(10,9)),mul(k3,b))
    QQ=add(pw(Z,5),mul(q3,pw(Z,3)),mul(q2,pw(Z,2)),mul(q1,Z),q0)
    JJ=add(mul(derivative(PP,0),DD(QQ)),scale(mul(DD(PP),derivative(QQ,0)),-1))
    J1=add(mul(add(scale(pw(a,2),Q(5,9)),scale(k1,-1)),da),scale(mul(b,db),Q(-10,3)))
    J0=add(mul(add(scale(pw(a,2),Q(5,9)),scale(k1,-1)),db),scale(mul(mul(a,b),da),Q(10,9)))
    need(JJ==add(mul(J1,Z),J0),'formal 3/5 coefficient elimination')
    KK=scale(k1,Q(9,5)); II=add(scale(pw(a,3),Q(1,3)),scale(mul(KK,a),-1),scale(pw(b,2),-3))
    need(DD(II)==scale(J1,Q(9,5)),'formal first integral')
    determinant=add(pw(add(pw(a,2),scale(KK,-1)),2),scale(mul(a,pw(b,2)),12))
    quartic=add(scale(pw(a,4),6 if mode=='--wrong-quartic' else 7),scale(mul(KK,pw(a,2)),-18),scale(mul(II,a),-12),scale(pw(KK,2),3))
    need(scale(determinant,3)==quartic,'formal determinant quartic')
    # Parity is indispensable to the depressed cubic conclusion: actual translated toy.
    toy_a=add(g,p); toy_b=power(toy_a,3)
    need(any((i+j)%2==1 for i,j,k in toy_b),'toy parity observation')
    vals=[]
    for j,q in [(2,Q(3)),(5,Q(6)),(6,Q(12))]:
        j=Q(j); eta=min(j/2,q/3)
        need(eta>j/3 and eta<=j/2,'positive Newton scale')
        need(j+4*eta>5*eta and j+3*eta>=5*eta and min(q,2*j)+2*eta>=5*eta,'B high-slot valuation bounds')
        vals.append({'j':str(j),'q':str(q),'eta':str(eta),'Jacobian_weight':str(7*eta)})
    return {'status':'PASS','zero_assert_nodes':True,'divisions':division,'formal_bracket':wire(JJ),'first_integral':wire(II),'quartic':wire(quartic),'valuation_controls':vals,'local_pole_orders':{'regular_coefficient_D':2,'target_inverse_p_squared':6},'scope':'actual small-factor division and universal formal coefficient identities; no A15/B25 or actual high powers, no source point'}

def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25)); resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,512*1024*1024))

if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else ''
    if mode=='--record':
        modes=[('',None),('--omit-hp',b'actual division reconstruction'),('--wrong-filtered-input',b'actual filtered input'),('--wrong-target-factor',b'actual target division factor'),('--wrong-q0',b'formal 3/5 coefficient elimination'),('--wrong-quartic',b'formal determinant quartic')]
        records=[]
        for opt in (False,True):
            for mutation,msg in modes:
                out=subprocess.run([sys.executable,'-I','-B']+(['-O'] if opt else [])+[str(Path(__file__).resolve())]+([mutation] if mutation else []),capture_output=True,timeout=30,preexec_fn=caps)
                need((out.returncode!=0)==bool(mutation),'unexpected control exit')
                if mutation: need(msg in out.stderr,'wrong failure marker')
                else:
                    with (HERE/('witness-O.json' if opt else 'witness.json')).open('xb') as stream: stream.write(out.stdout)
                records.append({'optimized':opt,'mutation':mutation or None,'returncode':out.returncode,'stdout_sha256':hashlib.sha256(out.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(out.stderr).hexdigest()})
        need((HERE/'witness.json').read_bytes()==(HERE/'witness-O.json').read_bytes(),'normal optimized bytes differ')
        with (HERE/'replay.json').open('x') as stream: json.dump({'status':'PASS','runs':records,'caps':'30wall25CPU512MiB each','writers_finished':True},stream,sort_keys=True,indent=2); stream.write('\n')
        print(json.dumps({'status':'PASS','runs':len(records),'witness_sha256':hashlib.sha256((HERE/'witness.json').read_bytes()).hexdigest()}))
    else: print(json.dumps(check(mode),sort_keys=True,indent=2))
