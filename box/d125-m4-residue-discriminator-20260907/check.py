#!/usr/bin/env python3
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
add,scale,mul,power,derivative,bracket,substitute,need,wire=(getattr(m,n) for n in ('add','scale','mul','power','derivative','bracket','substitute','need','wire'))

def rref(matrix,columns):
    a=[[Q(x) for x in row] for row in matrix]; piv=[]; at=0
    for c in range(columns):
        found=next((i for i in range(at,len(a)) if a[i][c]),None)
        if found is None: continue
        a[at],a[found]=a[found],a[at]; d=a[at][c]; a[at]=[x/d for x in a[at]]
        for i in range(len(a)):
            if i!=at and a[i][c]:
                d=a[i][c]; a[i]=[x-d*y for x,y in zip(a[i],a[at])]
        piv.append(c); at+=1
        if at==len(a): break
    ker=[]
    for c in range(columns):
        if c not in piv:
            v=[Q(0)]*columns; v[c]=1
            for i,p in enumerate(piv): v[p]=-a[i][c]
            ker.append(v)
    return piv,ker

def spaces(slots,extra=()):
    g={(1,0,0):Q(1)}; p={(0,1,0):Q(1)}; vi={(0,-1,0):Q(1)}
    pp=add(mul(power(p,4),g),scale(p,-1),scale(vi,-1))
    lifts=[substitute({(i,j,0):Q(1)},(vi,pp,{})) for i,j in slots]
    rows=sorted({e for z in lifts for e in z if e[1]<0})
    matrix=[[z.get(e,Q(0)) for z in lifts] for e in rows]
    for mon in extra: matrix.append([Q((i,j)==mon) for i,j in slots])
    piv,ker=rref(matrix,len(slots))
    need(all(all(sum(x*y for x,y in zip(row,v))==0 for row in matrix) for v in ker),'kernel replay')
    return {'slots':slots,'negative_rows':rows,'matrix':matrix,'pivots':piv,'kernel':ker}

def qwire(z):
    return {k:([[str(x) for x in row] for row in v] if k in ('matrix','kernel') else v) for k,v in z.items()}

def check(mode):
    need(sys.dont_write_bytecode,'no cache writes')
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text()))),'Assert node')
    one={(0,0,0):Q(1)}; g={(1,0,0):Q(1)}; p={(0,1,0):Q(1)}; s={(0,0,1):Q(1)}
    cslots=[(i,j) for n in range(0,9,2) for i in range(n+1) for j in [n-i] if 5*i-7*j<=0]
    need(len(cslots)==15 and all(i<=j for i,j in cslots),'all even slots have u,v coordinates')
    cs=spaces(cslots)
    u=mul(g,p); v=power(p,2); E=add(u,v,scale(one,-1)); L=mul(v,E)
    basis=[power(E,n) for n in range(5)]+[L,mul(E,L),mul(power(E,2),L),power(L,2)]
    if mode=='--mutate-C-basis': basis[5]=v
    vectors=[[b.get((i,j,0),Q(0)) for i,j in cslots] for b in basis]
    need(all(all(sum(x*y for x,y in zip(row,z))==0 for row in cs['matrix']) for z in vectors),'complete C ordinary basis')
    need(len(cs['pivots'])==6 and len(rref(vectors,15)[0])==9,'C exact dimension nine')
    dslots=[(i,j) for n in range(1,14,2) for i in range(n+1) for j in [n-i] if 5*i-7*j<=1 and i<=2*j]
    ds=spaces(dslots); ds_low=spaces(dslots,[(0,1),(0,3)])
    # Literal support proof that D/p reduces to a polynomial in u,v modulo T.
    negative=[]
    for i,j in dslots:
        need(j>=1,'all D terms divisible by p')
        vexp=(j-1-i)//2
        need(2*vexp==j-1-i,'D/p even parity')
        if vexp<0:
            need(vexp==-1 and i>=3,'only u^i/v, i>=3 occurs')
            negative.append([i,j])
    # Exact primary even-quotient equation. Coordinates now mean u,v,t.
    uu=g; vv=p; t=s; hh=add(t,scale(one,3))
    EE=add(uu,vv,scale(one,-1)); LL=mul(vv,EE)
    F=add(power(uu,3),power(vv,3),mul(hh,mul(uu,vv)),mul(t,power(vv,2)),scale(mul(hh,vv),-1))
    ellrel=add(scale(power(LL,2),3),mul(add(scale(power(EE,2),-3),mul(add(t,scale(one,-3)),EE),scale(one,-3)),LL),mul(EE,power(add(EE,one),3)))
    need(ellrel==mul(EE,F),'EL equation retains E factor')
    # Exact low C map: C(0)=0, C_v(0)=0, C_u nonzero can occur in ordinary space.
    candidate=add(E,one,L)
    need(candidate.get((0,0,0),0)==0 and candidate.get((0,2,0),0)==0 and candidate.get((1,1,0),0)==1,'actual C low coefficients')
    if mode=='--mutate-C-low-row':
        bad=add(E,one,scale(L,-1))
        need(bad.get((0,2,0),0)==0,'C_v is a real low constraint')
    # All formal orders through six in a tiny R=g rational toy, including gamma4 kernel.
    R=g; C=add(power(p,2),one); D=add(power(p,3),p); gamma=Q(2)
    A=add(power(R,3),mul(power(s,2),mul(R,C)),mul(power(s,3),D))
    pole=add(scale(power(D,2),Q(5,9)),scale(power(C,3),Q(-5,81)))
    divR=lambda z:{(i-1,j,k):a for (i,j,k),a in z.items()}
    B=add(power(R,5),scale(mul(power(s,2),mul(power(R,3),C)),Q(5,3)),
          scale(mul(power(s,3),mul(power(R,2),D)),Q(5,3)),scale(mul(power(s,4),mul(R,power(C,2))),Q(5,9)),
          scale(mul(power(s,5),mul(C,D)),Q(10,9)),mul(power(s,6),divR(pole)),scale(mul(power(s,4),R),gamma))
    kernel_factor=Q(1) if mode=='--mutate-linear-C-kernel' else Q(1,3)
    B=add(B,scale(mul(power(s,6),divR(C)),gamma*kernel_factor))
    J=bracket(A,B)
    need({e:a for e,a in J.items() if e[2]<=6}=={},'actual linear C kernel factor')
    # The order-four p coefficient of gamma4 R is -h gamma4 in the actual source.
    need(gamma!=0,'nontrivial kernel control')
    low_e4=scale(hh,-gamma)
    if mode=='--mutate-keep-kernel-despite-e4': need(low_e4=={},'e4 kills gamma4')
    return {'status':'PASS','assert_nodes':0,'C':qwire(cs),'C_basis_coordinates':[[str(x) for x in z] for z in vectors],
            'D':qwire(ds),'D_with_p_p3_zero':qwire(ds_low),'D_negative_v_exponents':negative,
            'dimensions':{'C_raw':len(cslots),'C_ordinary':len(cs['kernel']),'D_raw':len(dslots),
                          'D_ordinary':len(ds['kernel']),'D_low':len(ds_low['kernel'])},
            'residue':'R divides 9D^2-C^3 after low-e removal of gamma4',
            'EL_relation_is_E_times_F':True,'scope':'linear spaces and necessary residue only; no nonlinear solution or full source jet'}

def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25)); resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,512*1024*1024))

if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else ''
    if mode=='--record':
        records=[]
        modes=['','--mutate-C-basis','--mutate-C-low-row','--mutate-linear-C-kernel','--mutate-keep-kernel-despite-e4']
        messages=[None,b'complete C ordinary basis',b'C_v is a real low constraint',b'actual linear C kernel factor',b'e4 kills gamma4']
        for opt in (False,True):
            for mutation,msg in zip(modes,messages):
                out=subprocess.run([sys.executable,'-B']+(['-O'] if opt else [])+[str(Path(__file__).resolve())]+([mutation] if mutation else []),capture_output=True,timeout=30,preexec_fn=caps)
                need((out.returncode!=0)==bool(mutation),'unexpected control exit')
                if mutation: need(msg in out.stderr,'unrelated mutation failure')
                else:
                    with (HERE/('witness-O.json' if opt else 'witness.json')).open('xb') as f: f.write(out.stdout)
                records.append({'optimized':opt,'mutation':mutation or None,'returncode':out.returncode,
                                'stdout_sha256':hashlib.sha256(out.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(out.stderr).hexdigest()})
        need((HERE/'witness.json').read_bytes()==(HERE/'witness-O.json').read_bytes(),'normal optimized equality')
        with (HERE/'replay.json').open('x') as f: json.dump({'status':'PASS','runs':records,'caps':'30wall25CPU512MiB','writers_finished':True},f,sort_keys=True,indent=2); f.write('\n')
        print(json.dumps({'status':'PASS','runs':len(records),'witness_sha256':hashlib.sha256((HERE/'witness.json').read_bytes()).hexdigest()}))
    else: print(json.dumps(check(mode),sort_keys=True,indent=2))
