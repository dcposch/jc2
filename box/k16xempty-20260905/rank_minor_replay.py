#!/usr/bin/env python3
"""Independent t=5 exact model + modular determinant replay.

Rebuilds coefficients from fresh raw F3 rows using Singular, parses each
coefficient as exact rationals, checks the integral e=3d model, rebuilds
the complete weight-42 basis, and verifies the selected determinant by
an independent NumPy integer modular Gaussian elimination implementation.
"""
import ast
from fractions import Fraction as Q
import hashlib
import json
import os
from pathlib import Path
import re
import struct
import subprocess

ROOT=Path(__file__).resolve().parent
CERT=ROOT/'linear_t5_rank_certificate.json'
RAW=ROOT/'controls_t5_raw.sing'
data=json.loads(CERT.read_text())
assert data['t']==5 and data['target_weight']==42
assert data['prime']==32009
assert hashlib.sha256(RAW.read_bytes()).hexdigest()==data['hashes'][RAW.name]
p=data['prime']; dimage=data['d_image']; eimage=data['e_image']
assert (3*dimage*dimage-6)%p==0 and (eimage*eimage-18)%p==0
assert (3*dimage-eimage)%p==0
env=os.environ.copy();env.update(OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1')
terms=ROOT/'t5_rank_independent_terms.txt'
terms.unlink(missing_ok=True)
script=RAW.read_text()+f'''
proc must(int ok,string msg){{if(!ok){{print("FAIL "+msg);quit;}}}}
must(target==Bsol*eta,"target_map");
ideal auditPolys=rows,Bsol,eta,target;
poly auditRem; int auditI;
for(auditI=1;auditI<=size(auditPolys);auditI++){{
 auditRem=auditPolys[auditI];
 while(auditRem!=0){{
  write("{terms}",string(auditI)+"|"+string(leadcoef(auditRem))+"|"+string(leadexp(auditRem)));
  auditRem=auditRem-lead(auditRem);
 }}
}}
print("INDEPENDENT_FRESH_COEFFICIENT_EXPORT_PASS");quit;
'''
sing=ROOT/'t5_rank_independent_export.sing';sing.write_text(script)
exportlog=ROOT/'t5_rank_independent_export.log'
with exportlog.open('w') as out:
    done=subprocess.run(['stdbuf','-oL','-eL','Singular','-q',str(sing)],stdout=out,stderr=subprocess.STDOUT,env=env,timeout=120)
log=exportlog.read_text()
assert done.returncode==0 and 'INDEPENDENT_FRESH_COEFFICIENT_EXPORT_PASS' in log
assert not re.search(r'(^FAIL |^\s*\? )',log,re.M)
print('INDEPENDENT_FRESH_COEFFICIENT_EXPORT_PASS',flush=True)

# Independent exact parser for Q(d) expressions. Each value is a pair (a,b)
# representing a+b*d; d^2=2 is used by multiplication and division.
def pairmul(u,v):return (u[0]*v[0]+2*u[1]*v[1],u[0]*v[1]+u[1]*v[0])
def parse_node(n):
    if isinstance(n,ast.Constant) and isinstance(n.value,int):return Q(n.value),Q(0)
    if isinstance(n,ast.Name) and n.id=='d':return Q(0),Q(1)
    if isinstance(n,ast.UnaryOp):
        a,b=parse_node(n.operand)
        if isinstance(n.op,ast.USub):return -a,-b
        if isinstance(n.op,ast.UAdd):return a,b
    if isinstance(n,ast.BinOp):
        a=parse_node(n.left);b=parse_node(n.right)
        if isinstance(n.op,ast.Add):return a[0]+b[0],a[1]+b[1]
        if isinstance(n.op,ast.Sub):return a[0]-b[0],a[1]-b[1]
        if isinstance(n.op,ast.Mult):return pairmul(a,b)
        if isinstance(n.op,ast.Div):
            norm=b[0]*b[0]-2*b[1]*b[1];assert norm
            return pairmul(a,(b[0]/norm,-b[1]/norm))
        if isinstance(n.op,ast.Pow):
            assert b[1]==0 and b[0].denominator==1 and b[0]>=0
            result=(Q(1),Q(0))
            for _ in range(int(b[0])):result=pairmul(result,a)
            return result
    raise ValueError(ast.dump(n))
def parse_num(s):return parse_node(ast.parse(s.replace('^','**'),mode='eval').body)
def modq(q):
    assert q.denominator%p
    return q.numerator%p*pow(q.denominator,-1,p)%p

weights=(1,2,3,4,6)
polys={i:[] for i in range(1,13)}
for line in terms.read_text().splitlines():
    index,coefficient,exponents=line.split('|')
    index=int(index); exp=tuple(map(int,exponents.split(',')))
    assert len(exp)==5 and all(e>=0 for e in exp)
    a,b=parse_num(coefficient)
    assert a.denominator%p and b.denominator%p
    expected=21-index if index<=9 else {10:11,11:10,12:21}[index]
    assert sum(w*e for w,e in zip(weights,exp))==expected
    polys[index].append((exp,a,b))
assert all(polys.values())
assert all(len(v)==len({row[0] for row in v}) for v in polys.values())
print('EXACT_RAW_DENOMINATORS_AND_WEIGHTS_PASS',flush=True)

def allmonomials(total,ws):
    if len(ws)==1:
        if total%ws[0]==0:yield (total//ws[0],)
        return
    for e in range(total//ws[0]+1):
        for tail in allmonomials(total-e*ws[0],ws[1:]):yield (e,)+tail
basis=list(allmonomials(42,weights))
assert len(basis)==1792
assert basis==[tuple(row) for row in data['row_monomials']]
indices={exp:i for i,exp in enumerate(basis)}
selected=data['selected_columns'];assert len(selected)==len(basis)
assert len({(s['source_row'],tuple(s['multiplier_exponents'])) for s in selected})==1792
fullcount=sum(len(list(allmonomials(42-(22-k),weights))) for k in range(2,11))
assert fullcount==3504 and data['matrix_shape']==[1792,3504]
n=len(basis)
matrix=[0]*(n*n)
scales={}; selected_source_counts={k:0 for k in range(2,11)}
for column,spec in enumerate(selected):
    k=spec['source_row'];mult=tuple(spec['multiplier_exponents']);scale=Q(spec['exact_row_scale'])
    assert 2<=k<=10 and len(mult)==5 and all(e>=0 for e in mult)
    assert sum(w*e for w,e in zip(weights,mult))==42-(22-k)
    assert scale.denominator%p and scale.numerator%p
    assert scales.setdefault(k,scale)==scale
    selected_source_counts[k]+=1
    for exp,a,b in polys[k-1]:
        # The exact scaled coefficient is integer_u+integer_v*e, e=3d.
        aa,bb=a*scale,b*scale/3
        assert aa.denominator==bb.denominator==1
        residue=(int(aa)+int(bb)*eimage)%p
        assert residue==(modq(a)+modq(b)*dimage)%p*modq(scale)%p
        shifted=tuple(e+v for e,v in zip(exp,mult))
        row=indices[shifted]
        assert matrix[row*n+column]==0
        matrix[row*n+column]=residue
print('COMPLETE_WEIGHT_BASIS_AND_INTEGRAL_SELECTED_MINOR_PASS',flush=True)

binary=ROOT/'t5_rank_independent_matrix.bin'
with binary.open('wb') as handle:
    handle.write(struct.pack('<I',n))
    handle.write(struct.pack('<'+'I'*len(matrix),*matrix))
detdriver=ROOT/'rank_det_mod.py'
detdriver.write_text(r'''#!/usr/bin/env python3
import sys
import numpy as np
P=32009
raw=np.fromfile(sys.argv[1],dtype='<u4')
n=int(raw[0]);assert n==1792 and len(raw)==1+n*n
A=raw[1:].reshape(n,n).astype(np.int64)
determinant=1
for k in range(n):
    nonzero=np.flatnonzero(A[k:,k])
    assert len(nonzero), 'zero determinant'
    pivot=k+int(nonzero[0])
    if pivot!=k:
        A[[k,pivot]]=A[[pivot,k]]
        determinant=-determinant % P
    value=int(A[k,k]);determinant=determinant*value % P
    inverse=pow(value,-1,P)
    factors=A[k+1:,k]*inverse % P
    A[k+1:,k+1:]=(A[k+1:,k+1:]-factors[:,None]*A[k,k+1:]) % P
    A[k+1:,k]=0
print('DET_MOD_P='+str(determinant),flush=True)
print('INDEPENDENT_NUMPY_FULL_RANK_PASS',flush=True)
''')
detlog=ROOT/'t5_rank_independent_det.log'
with detlog.open('w') as out:
    result=subprocess.run(['stdbuf','-oL','-eL','python3',str(detdriver),str(binary)],stdout=out,stderr=subprocess.STDOUT,env=env,timeout=240)
dettext=detlog.read_text();print(dettext,end='',flush=True)
assert result.returncode==0 and 'INDEPENDENT_NUMPY_FULL_RANK_PASS' in dettext
det=int(re.search(r'DET_MOD_P=(\d+)',dettext).group(1))
assert det==data['minor_determinant_mod_prime']==29155

report={
 'verdict':'INDEPENDENT_T5_RANK_MODEL_AND_DETERMINANT_PASS',
 't':5,'field':'Q(d), d^2=2','integral_model':'Z[e], e=3d, e^2=18',
 'p':p,'d_image':dimage,'e_image':eimage,'basis_weights':weights,'target_weight':42,
 'basis_size':n,'full_macaulay_columns':fullcount,'selected_minor_shape':[n,n],
 'selected_source_counts':selected_source_counts,'determinant_mod_p':det,
 'raw_denominators_prime_units':True,'scaled_selected_coefficients_integral_in_e':True,
 'independent_determinant_method':'NumPy integer Gaussian elimination with row pivoting modulo 32009 (independent of producer FLINT)',
 'char0_implication':'The integral determinant has nonzero residue, hence is nonzero in Q(d). The selected exact matrix is invertible and every weight-42 polynomial belongs to J, including (B eta)^2.',
 'hashes':{f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in [RAW,CERT,sing,terms,binary,detdriver,detlog]},
}
(ROOT/'t5_rank_independent_result.json').write_text(json.dumps(report,indent=2)+'\n')
print('INDEPENDENT_T5_RANK_MODEL_AND_DETERMINANT_PASS',flush=True)
