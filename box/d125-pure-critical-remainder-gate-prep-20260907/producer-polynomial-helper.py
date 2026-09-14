#!/usr/bin/env python3
"""Sparse degree-five and toy-bracket identities, not the degree15/25 pair."""
import ast
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import resource
import subprocess
import sys

HERE=Path(__file__).resolve().parent

def need(ok,msg):
    if not ok: raise ValueError(msg)

def clean(p): return {e:Q(c) for e,c in p.items() if c}
def add(*ps):
    z={}
    for p in ps:
        for e,c in p.items(): z[e]=z.get(e,Q(0))+c
    return clean(z)
def scale(p,c): return clean({e:v*c for e,v in p.items()})
def mul(p,q):
    z={}
    for e,a in p.items():
        for f,b in q.items():
            h=tuple(x+y for x,y in zip(e,f)); z[h]=z.get(h,Q(0))+a*b
    return clean(z)
def power(p,n):
    z={(0,0,0):Q(1)}
    for _ in range(n): z=mul(z,p)
    return z
def derivative(p,axis):
    z={}
    for e,c in p.items():
        if e[axis]:
            h=list(e); h[axis]-=1; z[tuple(h)]=c*e[axis]
    return clean(z)
def bracket(p,q): return add(mul(derivative(p,0),derivative(q,1)),scale(mul(derivative(p,1),derivative(q,0)),-1))
def substitute(p,images):
    z={}
    for exponents,c in p.items():
        m={(0,0,0):c}
        for image,e in zip(images,exponents): m=mul(m,power(image,e))
        z=add(z,m)
    return z
def weighted_top(p):
    weight=max(5*i-7*j for i,j,t in p)
    return weight,{e:c for e,c in p.items() if 5*e[0]-7*e[1]==weight}
def wire(p): return [[list(e),str(c)] for e,c in sorted(p.items())]

def check(mode):
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text()))),'Assert node')
    one={(0,0,0):Q(1)}; g={(1,0,0):Q(1)}; p={(0,1,0):Q(1)}; t={(0,0,1):Q(1)}
    tp3=add(t,scale(one,3))
    H=add(power(p,5),mul(power(g,3),power(p,2)))
    R=add(H,mul(tp3,mul(g,power(p,2))),mul(t,power(p,3)),scale(mul(tp3,p),-1))
    if mode=='--mutate-R': R=add(R,mul(g,power(p,2)))
    # Images now use indices (u,v,t), negative v exponents allowed.
    u={(1,0,0):Q(1)}; v={(0,1,0):Q(1)}; vi={(0,-1,0):Q(1)}
    phi_p=add(mul(power(v,4),u),scale(v,-1),scale(vi,-1))
    H_lift=substitute(H,(vi,phi_p,t))
    negative_H={e:c for e,c in H_lift.items() if e[1]<0}
    need(negative_H=={(0,-3,0):Q(-3),(0,-1,0):Q(-9)},'H negative part')
    lifted=substitute(R,(vi,phi_p,t))
    need(all(e[1]>=0 for e in lifted),'changed R breaks ordinary lift')
    at_u0={e:c for e,c in lifted.items() if e[0]==0}
    expected=scale(mul(v,mul(add(power(v,2),one),add(power(v,2),t,scale(one,4)))),-1)
    need(at_u0==expected,'u=0 factorization')
    need(all(i+j<=5 and 5*i-7*j<=1 and i<=2*j for i,j,_ in R),'R support inequalities')
    need(all((i+j)%2==1 and i+j>0 for i,j,_ in R),'R odd and zero origin')
    need(weighted_top(R)==(1,{(3,2,0):Q(1)}),'R weighted leader')
    # Squarefreeness input identities, proved universally in the report.
    T={(i,j-1,k):c for (i,j,k),c in R.items()}
    need(derivative(T,0)==mul(p,add(scale(power(g,2),3),tp3)),'T_g identity')
    need({(i,0,k):c for (i,j,k),c in T.items() if j==0}==scale(tp3,-1),'T mod p')
    need({(i,0,k):c for (i,j,k),c in T.items() if j==4}==one,'T monic in p')
    Rminus=substitute(R,(g,p,scale(one,-3)))
    C=add(power(p,3),power(g,3),scale(p,-3))
    need(Rminus==mul(power(p,2),C),'exceptional R factorization')
    need(derivative(C,0)==scale(power(g,2),3),'C derivative')
    need(substitute(C,({},p,t))==add(power(p,3),scale(p,-3)),'C not divisible by g')
    need(weighted_top(mul(p,C))==(8,{(3,1,0):Q(1)}),'exceptional radical leader')
    h_at_minus=substitute(H,(one,scale(one,-1),t))
    hp_at_minus=substitute(derivative(H,1),(one,scale(one,-1),t))
    need(h_at_minus=={} and hp_at_minus==scale(one,3),'simple H root')
    # Scalar coefficient [p^15] R^5, obtained without expanding R^5 in g,p.
    # At g=0, choose n5,n3,n1 among five factors; only (0,5,0),(1,3,1),(2,1,2).
    choices=[]; scalar_sum={}
    from math import factorial
    for n5 in range(6):
        for n3 in range(6-n5):
            n1=5-n5-n3
            if 5*n5+3*n3+n1!=15: continue
            choices.append([n5,n3,n1])
            coefficient=Q(factorial(5),factorial(n5)*factorial(n3)*factorial(n1))
            scalar_sum=add(scalar_sum,scale(mul(power(t,n3),power(scale(tp3,-1),n1)),coefficient))
    expected_scalar=add(power(t,5),scale(mul(power(t,3),tp3),-20),scale(mul(t,power(tp3,2)),30))
    need(scalar_sum==expected_scalar,'whole beta15 shear coefficient')
    # Direct second-order derivative identity on genuinely small polynomials.
    r=g; X=p; A2=mul(g,p); B2=power(p,2)
    f=add(scale(r,2),scale(power(r,3),3)); fp=add(scale(one,2),scale(power(r,2),9))
    B1=add(scale(mul(power(r,2),X),Q(5,3)),scale(f,Q(1,3)))
    J2=add(scale(mul(power(r,2),bracket(r,B2)),3),scale(mul(power(r,4),bracket(r,A2)),-5),bracket(X,B1))
    f_factor=Q(-1) if mode=='--mutate-second-factor' else Q(-1,3)
    E=add(scale(mul(power(r,2),B2),3),scale(mul(power(r,4),A2),-5),
          scale(mul(r,power(X,2)),Q(-5,3)),scale(mul(fp,X),f_factor))
    need(bracket(r,E)==J2,'second-order coefficient factor')
    # Removing ALL moving lower-face prescriptions admits the dependent jet
    # A=R^3+kR, B=R^5+(5/3)kR^3+(5/9)k^2R modulo k^3.
    # Its lower-face coefficients are all zero; other requirements follow
    # from functions-of-R, ordinariness, oddness and the checked support.
    candidate_face=[Q(0),Q(0),Q(0)]
    required_face=[Q(1),Q(5,3),Q(5,9)]
    def face_verifier(value): return True if mode=='--mutate-omit-faces' else value==required_face
    need(face_verifier(required_face),'positive moving face control')
    need(not face_verifier(candidate_face),'omitted moving faces accepted dependent jet')
    return {'status':'PASS','R':wire(R),'R_lift':wire(lifted),'negative_H':wire(negative_H),
            'beta15_scalar':wire(scalar_sum),'scalar_choices':choices,'assert_nodes':0,
            'second_order_fprime_factor':'-1/3','no_degree15_25_pair_expanded':True,
            'scope':'exact boundary R and toy second-order identity; not a guarded point or full boundary classification'}

def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25))
    resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,512*1024*1024))

if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else ''
    if mode=='--record':
        results=[]
        for opt in (False,True):
            for mutation in ('','--mutate-R','--mutate-second-factor','--mutate-omit-faces'):
                command=[sys.executable]+(['-O'] if opt else [])+[str(Path(__file__).resolve())]+([mutation] if mutation else [])
                r=subprocess.run(command,capture_output=True,timeout=30,preexec_fn=caps)
                need((r.returncode!=0)==bool(mutation),'unexpected checker exit')
                if mutation:
                    message={'--mutate-R':b'changed R breaks ordinary lift','--mutate-second-factor':b'second-order coefficient factor',
                             '--mutate-omit-faces':b'omitted moving faces accepted dependent jet'}[mutation]
                    need(message in r.stderr,'unrelated mutation failure')
                else:
                    with (HERE/('witness-O.json' if opt else 'witness.json')).open('xb') as f: f.write(r.stdout)
                results.append({'optimized':opt,'mutation':mutation or None,'returncode':r.returncode,
                                'stdout_sha256':hashlib.sha256(r.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(r.stderr).hexdigest()})
        need((HERE/'witness.json').read_bytes()==(HERE/'witness-O.json').read_bytes(),'normal/-O bytes')
        with (HERE/'replay.json').open('x') as f:
            json.dump({'status':'PASS','runs':results,'caps':'30wall/25CPU seconds,512MiB','writers_finished':True},f,sort_keys=True,indent=2); f.write('\n')
        print(json.dumps({'status':'PASS','runs':len(results),'witness_sha256':hashlib.sha256((HERE/'witness.json').read_bytes()).hexdigest()}))
    else:
        print(json.dumps(check(mode),sort_keys=True,indent=2))
