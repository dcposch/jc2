#!/usr/bin/env python3
"""Tiny literal D108 support/line/interface inspection; no full source expansion."""
import ast
import hashlib
import json
from pathlib import Path
import re
import resource
import time
import sys
import sympy as S

root=Path(__file__).resolve().parent
repo=root.parents[1]
source=repo/'box/char-degree-20260905/d108/selected/meanfree_stage8_slimgb/d108_meanfree_stage8_strongfront.input.json'
expected='1c927d83aa4684ae91bfffc8d03500fbabb73a500faa222fa349a6d129a10814'
started=time.monotonic()
raw=source.read_bytes();assert hashlib.sha256(raw).hexdigest()==expected
data=json.loads(raw)
def split_top(text):
    parts=[];start=depth=0
    for i,ch in enumerate(text):
        if ch=='(':depth+=1
        elif ch==')':depth-=1
        elif ch=='+' and depth==0:parts.append(text[start:i]);start=i+1
        assert depth>=0
    assert depth==0
    parts.append(text[start:]);return parts
maps={}
names=set(data['names'])
for key,N in [('h',36),('D',71),('C',107)]:
    rows=[]
    for part in split_top(data[key+'_expr']):
        mt=re.fullmatch(r'\((.*)\)\*tt\^(\d+)\*zz\^(\d+)',part);assert mt
        e,r,z=mt.groups();r=int(r);z=int(z)
        tree=ast.parse(e.replace('^','**'),mode='eval')
        used={n.id for n in ast.walk(tree) if isinstance(n,ast.Name)}
        assert used<=names
        assert all(not isinstance(n,ast.BinOp) or not isinstance(n.op,ast.Div) or not any(isinstance(q,ast.Name) for q in ast.walk(n.right)) for n in ast.walk(tree))
        assert r>=0 and z>=0 and r+z<=N
        rows.append({'r':r,'W':z,'X':N-r-z,'coefficient':e,'names':sorted(used)})
    assert len({(q['r'],q['W']) for q in rows})==len(rows)
    maps[key]=rows
X,W,A,B=S.symbols('X W A B')
top=sum(S.sympify(r['coefficient'])*X**r['X']*W**r['W'] for r in maps['h'] if r['r']==0)
assert S.expand(top-(X+W)**8*W**28)==0
line={key:str(S.expand(sum(S.sympify(r['coefficient'])*X**r['X'] for r in rows if r['W']==0))) for key,rows in maps.items()}
c_names=set().union(*(set(r['names']) for r in maps['C']))
base_names=set().union(*(set(r['names']) for key in ('h','D') for r in maps[key]))
assert not c_names&base_names
def linear_parse(text):
    ex=S.sympify(text)
    return S.Poly(ex,*[S.Symbol(n) for n in sorted(c_names)])
# Check actual C coordinates are independent by exclusive identity slots, without a large rank solve.
C_columns={n:[] for n in c_names}
for row in maps['C']:
    poly=linear_parse(row['coefficient'])
    assert poly.total_degree()<=1
    for n in row['names']:
        coeff=poly.coeff_monomial(S.Symbol(n))
        if coeff:C_columns[n].append([row['X'],row['W'],str(coeff)])
identity={}
for n,col in C_columns.items():
    candidates=[(i,j) for i,j,c in col if c=='1' and all(not any((u,v)==(i,j) for u,v,d in C_columns[m]) for m in C_columns if m!=n)]
    assert candidates
    identity[n]=sorted(candidates)[0]
# In the sole fixed linear coordinates A=X+W,B=W, inspect just A=0 coefficients.
# This does not form h,D,C in the new plane: it contracts each already-frozen homogeneous row group.
axis={}
for key,rows in maps.items():
    bydeg={}
    for row in rows:
        degree=row['X']+row['W']
        bydeg.setdefault(degree,[]).append((-1)**row['X']*S.sympify(row['coefficient']))
    contracted={d:S.expand(sum(vals)) for d,vals in bydeg.items()}
    nonzero={d:e for d,e in contracted.items() if e!=0}
    axis[key]={'degree':max(nonzero,default=-1),'leading_coefficient':str(nonzero[max(nonzero)]) if nonzero else '0'}
semantic=sorted(set(data['names'])|{'Zc'})+['t3eq','t3_fgq','t3_fq2','lambda3','Z3']
sha=lambda vals:hashlib.sha256(''.join(str(v)+'\n' for v in vals).encode()).hexdigest()
assert len(semantic)==507 and sha(semantic)=='4c8952648ab814be891a76e4b0fc8b2f650ccf0689ebfba882a96ac2a83f1ad4'
assert len(data['residual_strings'])==14
result={'source_path':str(source),'source_sha256':expected,'names':data['names'],'semantic_order':semantic,
 'semantic_order_sha256':sha(semantic),'residual_rows':[{'index':i,'label':'source_residual_'+str(i),'expression':e,'sha256':hashlib.sha256(e.encode()).hexdigest()} for i,e in enumerate(data['residual_strings'])],
 'residual_sequence_sha256':sha(data['residual_strings']),
 'source_maps':maps,'normalizers':{'h':36,'D':71,'C':107},
 'summary':{key:{'rows':len(rows),'min_r':min(q['r'] for q in rows),'degree_bound':max(q['X']+q['W'] for q in rows),'max_W':max(q['W'] for q in rows),'W0_rows':[q for q in rows if q['W']==0]} for key,rows in maps.items()},
 'line':line,'top_h':'(X+W)^8*W^28','linear_coordinates':'A=X+W,B=W, inverse X=A-B,W=B, determinant1',
 'A_zero_contractions':axis,'C_dimension':len(c_names),'C_identity_slots':identity,'C_base_independent':True,
 'C_degree36_W_exponents':sorted({q['W'] for q in maps['C'] if q['X']+q['W']==36}),
 'localizers':['Z63*leader63-1','Z3*lambda3-1','Zc*c-1'],
 'no_full_F_G_expansion':True,'seconds':time.monotonic()-started,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
target=root/'source_interface.json'
if '--verify' in sys.argv:
    recorded=json.loads(target.read_text())
    replayed=json.loads(json.dumps(result))
    assert {k:v for k,v in recorded.items() if k not in ('seconds','peak_rss_kib')}=={k:v for k,v in replayed.items() if k not in ('seconds','peak_rss_kib')}
else:
    assert not target.exists()
    target.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['summary','line','A_zero_contractions','C_dimension','C_degree36_W_exponents','residual_sequence_sha256','seconds','peak_rss_kib']},sort_keys=True))
