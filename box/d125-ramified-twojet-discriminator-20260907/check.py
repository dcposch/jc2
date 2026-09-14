#!/usr/bin/env python3
"""Only degree-five lifts, degree-four kernel, and tiny R=g bracket controls."""
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import subprocess
import sys
from fractions import Fraction as Q

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
DEP=ROOT/'box/d125-zero-k-deformation-discriminator-20260907/check.py'
EXPECTED='25be0862730df8b66076eb59a2d1d0909fbcf563ea73ce16924affdc7c70ad66'
if hashlib.sha256(DEP.read_bytes()).hexdigest()!=EXPECTED:
    raise RuntimeError('helper input drift')
spec=importlib.util.spec_from_file_location('frozen_helpers',DEP)
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
add,scale,mul,power,derivative,bracket,substitute,need,wire=(getattr(m,n) for n in
    ('add','scale','mul','power','derivative','bracket','substitute','need','wire'))

def check(mode):
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text()))),'Assert node')
    one={(0,0,0):Q(1)}; g={(1,0,0):Q(1)}; p={(0,1,0):Q(1)}; t={(0,0,1):Q(1)}
    # Third-order identity, with R=g only. No actual A15/B25 powers.
    R=g; C=add(power(p,2),scale(one,2)); U2=add(p,mul(g,p)); U3=power(p,3); V3=add(p,power(g,2))
    aa=Q(7); bb=Q(11)
    U1=mul(R,C)
    V1=scale(mul(power(R,3),C),Q(5,3))
    V2=add(scale(mul(power(R,2),U2),Q(5,3)),scale(mul(R,power(C,2)),Q(5,9)),scale(R,aa/3),scale(power(R,3),bb/3))
    actual=add(bracket(power(R,3),V3),bracket(U1,V2),bracket(U2,V1),bracket(U3,power(R,5)))
    cubic=Q(5,9) if mode=='--mutate-cubic-factor' else Q(5,27)
    E3=add(scale(mul(power(R,2),V3),3),scale(mul(power(R,4),U3),-5),
           scale(mul(power(R,2),mul(C,U2)),Q(-10,3)),scale(mul(R,power(C,3)),cubic),
           scale(mul(R,C),-aa/3),scale(mul(power(R,3),C),-bb))
    need(actual==bracket(R,E3),'third-order cubic coefficient')
    # All actual degree-five R terms, but no powers of this R.
    tp3=add(t,scale(one,3))
    H=add(power(p,5),mul(power(g,3),power(p,2)))
    realR=add(H,mul(tp3,mul(g,power(p,2))),mul(t,power(p,3)),scale(mul(tp3,p),-1))
    E=add(power(p,2),mul(g,p),scale(one,-1)); Rt=mul(p,E)
    need(derivative(realR,2)==Rt,'R_t derivative')
    u=g; v=p; vi={(0,-1,0):Q(1)}
    phip=add(mul(power(v,4),u),scale(v,-1),scale(vi,-1))
    lifted=substitute(realR,(vi,phip,t))
    need(all(e[1]>=0 for e in lifted),'R ordinary')
    need({e:c for e,c in lifted.items() if e[1]==0}==scale(u,3),'R transverse jet')
    T={(i,j-1,z):c for (i,j,z),c in realR.items()}
    phiT=substitute(T,(vi,phip,t))
    need(min(e[1] for e in phiT)==1,'T valuation')
    need({e:c for e,c in phiT.items() if e[1]==1}==scale(mul(u,v),-3),'T first jet')
    slots=[(i,j) for i in range(5) for j in range(5-i) if (i+j)%2==0 and 5*i-7*j<=-8]
    need(sorted(slots)==[(0,2),(0,4),(1,3)],'literal degree-four kernel slots')
    bases=[power(p,2),power(p,4),mul(g,power(p,3))]
    lifts=[substitute(b,(vi,phip,t)) for b in bases]
    matrix=[[q.get((0,e,0),Q(0)) for q in lifts] for e in (-4,-2)]
    need(matrix==[[0,1,-1],[1,4,-3]],'both complete negative kernel rows')
    weights=[Q(0),Q(1),Q(1)] if mode=='--mutate-omit-negative-row' else [Q(-1),Q(1),Q(1)]
    candidate=add(*(scale(q,c) for q,c in zip(lifts,weights)))
    need(all(e[1]>=0 for e in candidate),'omitted v^-2 row admits a pole')
    # Low degree-three part of cR+dR²Rt; do not expand R² itself.
    c=Q(7); d=Q(11)
    lowR={e:a for e,a in realR.items() if e[0]+e[1]<=3}
    Rlinear=scale(mul(tp3,p),-1); Rtlinear=scale(p,-1)
    lowU=add(scale(lowR,c),scale(mul(power(Rlinear,2),Rtlinear),d))
    if mode=='--mutate-independent-tangent': lowU=add(lowU,mul(g,power(p,2)))
    coeffp={z:a for (i,j,z),a in lowU.items() if (i,j)==(0,1)}
    coeffgp2={z:a for (i,j,z),a in lowU.items() if (i,j)==(1,2)}
    need(coeffgp2=={z:-a for z,a in coeffp.items()},'tangent p/gp2 compatibility')
    # A genuine truncated-ring countercontrol to unauthorized saturation.
    # A=s*p, B=5*s^4*g/9 over Q[s]/(s^5) gives J=0, but A_p=s !=0.
    aa_poly=mul(t,p); bb_poly=scale(mul(power(t,4),g),Q(5,9))
    tinyJ=bracket(aa_poly,bb_poly)
    need(tinyJ=={(0,0,5):Q(-5,9)},'raw truncated row')
    need({e:a for e,a in tinyJ.items() if e[2]<5}=={},'truncated Jacobian zero')
    if mode=='--mutate-truncated-saturation':
        need({e:a for e,a in derivative(aa_poly,1).items() if e[2]<5}=={},'nilpotent k cannot be canceled')
    return {'status':'PASS','assert_nodes':0,'third_order_cubic_coefficient':'5/27',
            'degree_four_slots':[list(x) for x in slots],
            'negative_matrix':[[str(x) for x in row] for row in matrix],
            'kernel_vector':['-1','1','1'],'R_transverse_jet':'3u','T_first_jet':'-3uv',
            'tangent_low_coefficients':{'p':[[z,str(a)] for z,a in sorted(coeffp.items())],
                                        'gp2':[[z,str(a)] for z,a in sorted(coeffgp2.items())]},
            'scope':'identities only; no full receiver point or raw full-source jet exhibited'}

def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25)); resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,512*1024*1024))

if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else ''
    if mode=='--record':
        records=[]
        modes=['','--mutate-cubic-factor','--mutate-omit-negative-row','--mutate-independent-tangent','--mutate-truncated-saturation']
        messages=[None,b'third-order cubic coefficient',b'omitted v^-2 row admits a pole',b'tangent p/gp2 compatibility',b'nilpotent k cannot be canceled']
        for optimized in (False,True):
            for mutation,msg in zip(modes,messages):
                cmd=[sys.executable]+(['-O'] if optimized else [])+[str(Path(__file__).resolve())]+([mutation] if mutation else [])
                out=subprocess.run(cmd,capture_output=True,timeout=30,preexec_fn=caps)
                need((out.returncode!=0)==bool(mutation),'unexpected control status')
                if mutation: need(msg in out.stderr,'unrelated mutation failure')
                else:
                    with (HERE/('witness-O.json' if optimized else 'witness.json')).open('xb') as f: f.write(out.stdout)
                records.append({'optimized':optimized,'mutation':mutation or None,'returncode':out.returncode,
                                'stdout_sha256':hashlib.sha256(out.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(out.stderr).hexdigest()})
        need((HERE/'witness.json').read_bytes()==(HERE/'witness-O.json').read_bytes(),'normal optimized equality')
        with (HERE/'replay.json').open('x') as f:
            json.dump({'status':'PASS','runs':records,'caps':'30wall/25CPU seconds,512MiB','writers_finished':True},f,sort_keys=True,indent=2); f.write('\n')
        print(json.dumps({'status':'PASS','runs':len(records),'witness_sha256':hashlib.sha256((HERE/'witness.json').read_bytes()).hexdigest()}))
    else: print(json.dumps(check(mode),sort_keys=True,indent=2))
