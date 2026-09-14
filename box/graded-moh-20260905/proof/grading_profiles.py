#!/usr/bin/env python3
"""Exact support grading and finite bigraded target component profiles; no ideal solve."""
from pathlib import Path
from fractions import Fraction
from collections import Counter
import json,math,hashlib
BASE=Path('box/moh14-charts-20260905/hsupport-gate-20260905/source-complete/classes')
OUT=Path('box/graded-moh-20260905/proof')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def monomials(weights,B,W):
    dims=[[0]*(W+1) for _ in range(B+1)];dims[0][0]=1
    for b,k in weights:
        for i in range(b,B+1):
            for j in range(k,W+1):dims[i][j]+=dims[i-b][j-k]
    return dims
result=[]
for p in sorted(BASE.glob('*/meta/*.json')):
    if p.stem.endswith('_union'):continue
    j=json.loads(p.read_text());m=j['meta'];cl=m['closed_form'];K=int(cl['K']);n=m['row']['n'];low=m['row']['m'];D=n+low-1;ell=int(cl['ell']);weights={}
    for v in j['variables']:
        if v=='c':weights[v]=[ell+1,D];continue
        pre,b,a=v.split('_');i=1 if pre=='h' else int(pre[1:]);weights[v]=[int(b),i*K-int(a)]
    assert all(b>=0 and k>0 for b,k in weights.values())
    residual={v:(ell+1)*k-D*b for v,(b,k) in weights.items()}
    assert residual['c']==0 and all(r for v,r in residual.items() if v!='c')
    count0=sum(b==0 for v,(b,k) in weights.items() if v!='c')
    cap=min(Fraction(k,b) for v,(b,k) in weights.items() if v!='c' and b)
    dims=monomials(weights.values(),ell+1,D)
    cols=dims[ell+1][D]
    # Structural row candidates only; no assertion every candidate row occurs.
    # Native h-adic row positions match all y-exponents a+jK below D.
    allmultipliers=sum(dims[ell-b][a] for b in range(ell+1) for a in range(D+1))
    result.append(dict(stem=p.stem,meta=str(p),meta_sha256=sha(p),parameters=len(weights),K=K,n=n,m=low,e=cl['e'],q=cl['q'],ell=ell,D=D,positive_weight_range=[min(k for v,(b,k) in weights.items() if v!='c'),max(k for v,(b,k) in weights.items() if v!='c')],variables=weights,residual_weights=residual,x_independent_affine_subspace_dimension=count0,full_x_positive_branch_count=len(weights)-1-count0,positive_functional_k_minus_t_b_t_max_strict=str(cap),N1_component_monomials=cols,N1_all_possible_row_multiplier_count_upper=allmultipliers,N_bound=f"{cl['e']+cl['q']}^{len(weights)-1}",weighted_degree_bound=f"{D}*{cl['e']+cl['q']}^{len(weights)-1}"))
OUT.mkdir(exist_ok=True,parents=True)
(OUT/'grading-profiles.json').write_text(json.dumps(result,indent=2)+'\n')
for r in result:print(r['stem'],r['parameters'],'D',r['D'],'free-A-space',r['x_independent_affine_subspace_dimension'],'N1-monomials',r['N1_component_monomials'],'upper-multipliers',r['N1_all_possible_row_multiplier_count_upper'])
