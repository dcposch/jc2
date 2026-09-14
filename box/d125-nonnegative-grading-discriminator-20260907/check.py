#!/usr/bin/env python3
"""One literal lift coefficient and its grading obstruction; no source expansion."""
import sys
sys.dont_write_bytecode=True
import ast
import hashlib
import itertools
import json
from math import comb
from pathlib import Path
import resource
import subprocess
HERE=Path(__file__).resolve().parent; ROOT=HERE.parents[1]
METADATA=ROOT/'box/d125-minimal-receiver-client-preflight-20260906/client.py'

def need(ok,message):
    if not ok: raise ValueError(message)

def lift_coefficient(i,j):
    # At u=0, v^-i*(-v-v^-1)^j; only this one v^-3 coefficient.
    numerator=j-i+3
    if numerator%2: return 0
    d=numerator//2
    return (-1)**j*comb(j,d) if 0<=d<=j else 0

def row_degrees(row,weights):
    return {0 if name=='1' else weights[name] for name,c in row.items() if c}

def certificate(row):
    need(row.get('1',0)!=0 and row.get('k',0)!=0,'actual constant-and-k infeasibility witness')
    return {'from_constant':'degree(row)=0','from_k':'degree(row)=wt(k)',
            'conclusion':'wt(k)=0','positive_k_weight_impossible':True}

def check(mode):
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text()))),'zero Assert nodes')
    raw=METADATA.read_bytes()
    need(hashlib.sha256(raw).hexdigest()=='ec2fa2d1e23bc16bc07c9208f648e3b17561cbfddaaf04fed28d7ffc9a428d53','literal metadata pin')
    # Parse ONLY a literal polygon; do not import or call make_contract/poly_pow.
    tree=ast.parse(raw); vertices=None
    for node in tree.body:
        if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='VERTICES' for t in node.targets):
            vertices=ast.literal_eval(node.value)['unequal'][0]
    need(vertices==((0,0),(0,15),(9,6),(2,1)),'literal A polygon')
    points=[]
    for i in range(10):
        for j in range(16):
            edges=list(zip(vertices,vertices[1:]+vertices[:1]))
            cross=[(b[0]-a[0])*(j-a[1])-(b[1]-a[1])*(i-a[0]) for a,b in edges]
            inside=all(x>=0 for x in cross) or all(x<=0 for x in cross)
            halfplanes=i+j<=15 and 5*i-7*j<=3 and i<=2*j
            need(inside==halfplanes,'literal polygon/halfplane equality')
            if inside and (i+j)%2: points.append((i,j))
    free=[(i,j) for i,j in points if i+j!=15 and 5*i-7*j!=3]
    need(len(free)==33 and (2,1) not in free,'actual odd A free slots')
    # Four already prescribed total-face coefficients, not a power expansion.
    top={(3*m,15-3*m):comb(3,m) for m in range(4)}
    if mode=='--mutate-top-pin': top[(9,6)]+=1
    contributions=[top[(3*m,15-3*m)]*lift_coefficient(3*m,15-3*m) for m in range(4)]
    need(contributions==[-5005,2772,-252,1],'actual fixed-face coefficient projection')
    constant=sum(contributions)
    # Independent coefficient projection through the degree-five H at u=0.
    H={}
    for i,j in ((0,5),(3,2)):
        for d in range(j+1):
            e=-i+j-2*d; H[e]=H.get(e,0)+(-1)**j*comb(j,d)
    H={e:c for e,c in H.items() if c}
    need(H=={5:-1,3:-5,1:-10,-1:-9,-3:-3},'degree-five pure-line projection')
    scalar=sum(H[a]*H[b]*H[c] for a,b,c in itertools.product(H,repeat=3) if a+b+c==-3)
    need(constant==scalar==-2484,'two exact scalar coefficient derivations')
    # Actual degree-three monomial phi(g^2 p), no high source power.
    phi_p={(1,4):1,(0,1):-1,(0,-1):-1}
    if mode=='--mutate-lift-sign': phi_p[(0,-1)]=1
    phi_g2p={(u,v-2):c for (u,v),c in phi_p.items()}
    need(phi_g2p.get((0,-3))==lift_coefficient(2,1)==-1,'actual k monomial lift sign')
    row={'1':constant,'k':-1}
    for i,j in free:
        c=lift_coefficient(i,j)
        if c: row[f'A_g{i}_p{j}']=c
    need(len(row)==34,'single literal row term count')
    if mode=='--mutate-remove-constant': row.pop('1')
    if mode=='--mutate-remove-k': row.pop('k')
    proof=certificate(row)
    # Changed ROW objects, not an altered homogeneity predicate.
    all_one={name:1 for name in row if name!='1'}
    need(row_degrees(row,all_one)=={0,1},'actual row is inhomogeneous at positive candidate weights')
    no_constant={name:c for name,c in row.items() if name!='1'}
    need(row_degrees(no_constant,all_one)=={1},'deleting fixed top contribution falsely permits a grading')
    k_only={name:(1 if name=='k' else 0) for name in row if name!='1'}
    need(row_degrees(row,k_only)=={0,1},'actual k-positive candidate rejects')
    no_k={name:c for name,c in row.items() if name!='k'}
    need(row_degrees(no_k,k_only)=={0},'deleting moving face falsely permits a grading')
    # One-row homogenization control only; NOT a new complete source/client.
    homogenized_weights={'ell':1,'k':6}
    for i,j in free: homogenized_weights[f'A_g{i}_p{j}']=(15-i-j)//2
    row_weights={6,homogenized_weights['k']}
    for i,j in free:
        if lift_coefficient(i,j): row_weights.add(homogenized_weights[f'A_g{i}_p{j}']+(i+j-3)//2)
    need(row_weights=={6},'one-row free-ell covariance')
    need({homogenized_weights['ell'],0}=={0,1},'ell=1 normalization breaks that grading')
    return {'status':'PASS','zero_assert_nodes':True,'row_index':['A',0,-3],
            'free_A_slots':free,'literal_row':row,'top_contributions':contributions,
            'constant':constant,'k_coefficient':-1,'proof':proof,
            'one_row_homogenization_only':{'ell_weight':1,'k_weight':6,'row_weight':6},
            'scope':'no diagonal grading with wt(k)>0 makes every literal original generator homogeneous; not an ideal-unit or abstract-grading claim'}

def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25)); resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,512*1024*1024))

if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else ''
    if mode=='--record':
        modes=[('',None),('--mutate-top-pin',b'actual fixed-face coefficient projection'),
               ('--mutate-lift-sign',b'actual k monomial lift sign'),
               ('--mutate-remove-constant',b'actual constant-and-k infeasibility witness'),
               ('--mutate-remove-k',b'actual constant-and-k infeasibility witness')]
        results=[]
        for opt in (False,True):
            for mutation,message in modes:
                command=[sys.executable,'-I','-B']+(['-O'] if opt else [])+[str(Path(__file__).resolve())]+([mutation] if mutation else [])
                out=subprocess.run(command,capture_output=True,timeout=30,preexec_fn=caps)
                need((out.returncode!=0)==bool(mutation),'unexpected grading control exit')
                if mutation: need(message in out.stderr,'wrong mutation failure')
                else:
                    with (HERE/('witness-O.json' if opt else 'witness.json')).open('xb') as f: f.write(out.stdout)
                results.append({'optimized':opt,'mutation':mutation or None,'returncode':out.returncode,
                                'stdout_sha256':hashlib.sha256(out.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(out.stderr).hexdigest()})
        need((HERE/'witness.json').read_bytes()==(HERE/'witness-O.json').read_bytes(),'normal optimized witness equality')
        with (HERE/'replay.json').open('x') as f: json.dump({'status':'PASS','runs':results,'caps':'30wall25CPU512MiB each; Python-I-B','writers_finished':True},f,sort_keys=True,indent=2); f.write('\n')
        print(json.dumps({'status':'PASS','runs':len(results),'witness_sha256':hashlib.sha256((HERE/'witness.json').read_bytes()).hexdigest()}))
    else: print(json.dumps(check(mode),sort_keys=True,indent=2))
