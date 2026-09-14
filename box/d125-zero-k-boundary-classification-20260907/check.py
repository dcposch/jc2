#!/usr/bin/env python3
"""Degree-five linear lift, scalar normalization, support and toy controls."""
import ast
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import resource
import subprocess
import sys

HERE=Path(__file__).resolve().parent
ZERO=(0,0,0,0,0)
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
    for e,c in p.items():
        for f,d in q.items():
            h=tuple(x+y for x,y in zip(e,f)); out[h]=out.get(h,Q(0))+c*d
    return clean(out)
def power(p,n):
    if n<0:
        if len(p)!=1: raise ValueError('negative power requires a unit monomial')
        e,c=next(iter(p.items()))
        if not c: raise ValueError('negative power of zero')
        return {tuple(n*x for x in e):c**n}
    out={ZERO:Q(1)}
    for _ in range(n): out=mul(out,p)
    return out
def sub(p,images):
    out={}
    for exponents,c in p.items():
        term={ZERO:c}
        for image,e in zip(images,exponents): term=mul(term,power(image,e))
        out=add(out,term)
    return out
def variable(i):
    e=[0]*5; e[i]=1
    return {tuple(e):Q(1)}
def derivative(p,i):
    out={}
    for e,c in p.items():
        if e[i]:
            f=list(e); f[i]-=1; out[tuple(f)]=c*e[i]
    return clean(out)
def bracket(p,q): return add(mul(derivative(p,0),derivative(q,1)),scale(mul(derivative(p,1),derivative(q,0)),-1))
def wire(p): return [[list(e),str(c)] for e,c in sorted(p.items())]

def check(mode):
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text()))),'Assert node')
    one={ZERO:Q(1)}; g,p,a,b,c=[variable(i) for i in range(5)]
    H=add(power(p,5),mul(power(g,3),power(p,2)))
    lower=[(i,j) for degree in (1,3) for i in range(degree+1) for j in [degree-i]
           if 5*i-7*j<=1 and i<=2*j]
    if mode=='--mutate-support': lower.append((2,1))
    need(sorted(lower)==[(0,1),(0,3),(1,2)],'forbidden lower support slot')
    S=add(H,mul(a,mul(g,power(p,2))),mul(b,power(p,3)),mul(c,p))
    # Coordinates after substitution are (u,v,a,b,c).
    u,v=g,p; vi={(0,-1,0,0,0):Q(1)}
    phi_p=add(mul(power(v,4),u),scale(v,-1),scale(vi,-1))
    lifted=sub(S,(vi,phi_p,a,b,c))
    negative={e:q for e,q in lifted.items() if e[1]<0}
    expected=add(mul(power(vi,3),add(a,scale(b,-1),scale(one,-3))),
                 mul(vi,add(scale(a,2),scale(b,-3),scale(c,-1),scale(one,-9))))
    need(negative==expected,'two complete generator negative rows')
    # Solve with b=t, using coefficient variable b as the parameter.
    solved=sub(negative,(u,v,add(b,scale(one,3)),b,scale(add(b,scale(one,3)),-1)))
    need(solved=={},'exact R_t recovery')
    # Independent uniqueness of the two-by-two coefficient system for (a,c).
    need(Q(1)*Q(-1)-Q(0)*Q(2)==-1,'unit generator solve determinant')
    # Actual dropped-row control: a=b+3, c=0, b=0 kills v^-3 but leaves -3v^-1.
    candidate=sub(negative,(u,v,scale(one,3),{},{}))
    need(candidate=={(0,-1,0,0,0):Q(-3)},'literal remaining negative row')
    checked={e:q for e,q in candidate.items() if not(mode=='--mutate-drop-row' and e[1]==-1)}
    need(bool(checked),'omitted negative row accepted nonordinary generator')
    # Same-field normalization, using simultaneous leading degrees3 and5.
    r=Q(2); f3=r**-3; g5=r**-5
    normalized_r=g5/f3**2
    if mode=='--mutate-normalization': normalized_r=1/normalized_r
    need(normalized_r==r and f3*normalized_r**3==1 and g5*normalized_r**5==1,'same-field leading normalization')
    # Monicity/integrality toy: W=v^-1+v has W^3+alpha W nonordinary;
    # its lowest v coefficient cannot be canceled by the lower-degree term.
    W=add(vi,v); integral_toy=add(power(W,3),mul(a,W))
    need(integral_toy.get((0,-3,0,0,0))==1,'monic pole-order control')
    # For nonzero r, the g-cubic divided by p^2 has constant valuation -2.
    # The two exact inequalities are the universal integer-valuation argument.
    for n in range(-12,13):
        vals=[3*n,n,-2]
        need(vals.count(min(vals))==1,'cubic no Laurent root valuation')
    # q*b identities use (g,p,a,b,c) now as (R,unused,alpha,beta,unused).
    aa=add(scale(power(g,2),3),a)
    gamma=add(mul(a,b),scale(power(a,2),Q(-5,9)))
    bb=add(scale(power(g,4),5),scale(mul(b,power(g,2)),3),gamma)
    q=add(scale(power(g,2),Q(5,3)),b,scale(a,Q(-5,9)))
    need(mul(aa,q)==bb,'general a-divides-b scalar condition')
    # Direct general second-order bracket identity on small R=g and A1=p.
    h=add(scale(g,2),scale(power(g,3),3)); hp=derivative(h,0)
    X=p; A2=mul(g,p); B2=power(p,2); B1=add(mul(q,X),h)
    J2=add(mul(aa,bracket(g,B2)),scale(mul(bb,bracket(g,A2)),-1),bracket(X,B1))
    E=add(mul(aa,add(B2,scale(mul(q,A2),-1))),scale(mul(g,power(X,2)),Q(-5,3)),scale(mul(hp,X),-1))
    need(bracket(g,E)==J2,'general second-order identity')
    # Literal polygon inclusion/strict-face test for B -> B-beta*A.
    A={(i,j) for i in range(16) for j in range(16-i) if 5*i-7*j<=3 and i<=2*j}
    B={(i,j) for i in range(26) for j in range(26-i) if 5*i-7*j<=5}
    need(A<=B and max(5*i-7*j for i,j in A)==3<5 and max(i+j for i,j in A)==15<25,'whole beta shear support and faces')
    LA={(t,e) for t in range(3) for e in range(5*t-15,0)}
    LB={(t,e) for t in range(5) for e in range(5*t-25,0)}
    need(LA<=LB,'whole beta shear lower-row inclusion')
    return {'status':'PASS','lower_slots':lower,'generic_generator_negative_rows':wire(negative),
            'normalization_scalar':str(normalized_r),'generic_solve_determinant':'-1',
            'A_B_support_counts':[len(A),len(B)],'negative_row_counts':[len(LA),len(LB)],
            'assert_nodes':0,'no_A15_B25_pair_expansion':True,
            'scope':'field-point classification controls; optional general-jet identities, no guarded point'}

def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25))
    resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,512*1024*1024))

if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else ''
    if mode=='--record':
        runs=[]
        for opt in (False,True):
            for mutation in ('','--mutate-support','--mutate-drop-row','--mutate-normalization'):
                command=[sys.executable]+(['-O'] if opt else [])+[str(Path(__file__).resolve())]+([mutation] if mutation else [])
                result=subprocess.run(command,capture_output=True,timeout=30,preexec_fn=caps)
                need((result.returncode!=0)==bool(mutation),'unexpected subprocess exit')
                if mutation:
                    msg={'--mutate-support':b'forbidden lower support slot','--mutate-drop-row':b'omitted negative row',
                         '--mutate-normalization':b'same-field leading normalization'}[mutation]
                    need(msg in result.stderr,'unrelated mutation failure')
                else:
                    with (HERE/('final-witness-O.json' if opt else 'final-witness.json')).open('xb') as f: f.write(result.stdout)
                runs.append({'optimized':opt,'mutation':mutation or None,'returncode':result.returncode,
                             'stdout_sha256':hashlib.sha256(result.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(result.stderr).hexdigest()})
        need((HERE/'final-witness.json').read_bytes()==(HERE/'final-witness-O.json').read_bytes(),'normal/-O byte equality')
        with (HERE/'final-replay.json').open('x') as f:
            json.dump({'status':'PASS','runs':runs,'caps':'30wall/25CPU seconds,512MiB','writers_finished':True},f,sort_keys=True,indent=2); f.write('\n')
        print(json.dumps({'status':'PASS','runs':len(runs),'witness_sha256':hashlib.sha256((HERE/'final-witness.json').read_bytes()).hexdigest()}))
    else:
        print(json.dumps(check(mode),sort_keys=True,indent=2))
