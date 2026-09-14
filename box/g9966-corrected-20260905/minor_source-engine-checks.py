#!/usr/bin/env python3
"""Independent construction checks (no branch unit asserted)."""
from pathlib import Path
from math import comb
import sys,json,hashlib
import sympy as sp
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE))
import minor_source_engine_snapshot as e
from minor_source_data_snapshot import SOURCE as D
report={}
# A complete basis rank check from the raw h3 valuation triangle.
raw=[(r,q) for r in range(1,D['h3_degree']+1) for q in range(D['h3_degree']-r+1)]
by={'below':[],'equal':[],'above':[]}
for p in raw:by['below' if e.weight(p)<D['h3_floor'] else 'equal' if e.weight(p)==D['h3_floor'] else 'above'].append(p)
dets=[]
for r in range(1,D['h3_degree']+1):
 qs=[q for rr,q in by['above'] if rr==r]
 if qs:
  vmin=min(qs)
  matrix=sp.Matrix([[comb(q-vmin,k-vmin) if k<=q else 0 for q in qs] for k in qs])
  det=matrix.det();assert det==1;dets.append(str(det))
report['h3_floor_full_triangle']={'raw':len(raw),**{k:len(v) for k,v in by.items()},'equality_slots':by['equal'],'triangular_basis_determinants':dets}
# Derive all pole labels directly from lower pure-y monomial witnesses.
support={}
for branch in ['delta2','delta52']:
 for name,degree in [('F',D['n']),('G',D['m'])]:
  d=D['minor'][branch]['cover'];g=int(d*(1+D['minor'][branch]['radius_y']));L=D['minor'][branch][name+'_local_floor']
  table={}
  witnesses=[]
  for n in range(1,L+1):
   tags=[]
   for k in range(L//g+1):
    if n<d+g*k or (n-g*k)%d:continue
    r=(n-g*k)//d;i=degree-r-k
    assert r>=1 and i>=0 and i+k<degree
    tags.append(k);witnesses.append((n,k,i,k))
   if tags:table[n]=tuple(tags)
  assert table==e.raw_minor_support(branch,name)
  support[branch+'_'+name]={'derived_count':sum(map(len,table.values())),'all_frozen_labels_identical':True,
                           'full_total_degree_lower_monomial_witnesses':len(witnesses),'d':d,'generic_w_power':g,'last_power':L}
report['derived_pole_support']=support
# Compare the actual normalized local expansion to an independent Sympy expansion.
t,s,zeta=sp.symbols('t s zeta');j,u,a,v=sp.symbols('jet0 u minor_a2 v')
poly={(0,3):sp.Integer(2),(1,2):sp.Integer(-3),(2,1):sp.Integer(5),(4,0):sp.Integer(7)}
local={}
for branch in ['delta2','delta52']:
 d=D['minor'][branch]['cover'];cut=15
 w=(j*s+u*s**2+(a+zeta)*s**3) if branch=='delta2' else (j*s**2+u*s**4+v*s**6+zeta*s**7)
 native=sp.Poly(sp.expand(sum(coef*s**(d*r)*(w-1)**q for (r,q),coef in poly.items())),s,zeta)
 native={(int(n),int(k)):value for (n,k),value in native.terms() if n<=cut and value!=0}
 emitted=e.local_rows(poly,branch,cut)
 assert native==emitted
 local[branch]={'all_rows_match_independent_sympy':True,'rows':len(native),'cutoff':cut}
report['full_centred_local_emitter']=local
# Source outer floor and D1 matrices are required to give the original image.
outer,ofree,meta=e.outer_state(7)
e.E.OUTER_SPECS=D['outer_specs']
old,oldfree,oldmeta=e.E.outer_state(7)
assert outer==old and ofree==oldfree
report['outer_source_floor_and_D1']={'block_counts':{name:{k:m[k] for k in ['ambient_count','equation_count','kept_count','floor']} for name,m in meta['preblocks'].items()},
                                  'pivot_ranks':[row['Qstar_pivots'] for row in meta['D1_offsets']],
                                  'free_count':len(ofree),'full_outer_image_matches_old':True}
report['status']='PASS'
report['engine_sha256']=hashlib.sha256(Path(e.__file__).read_bytes()).hexdigest()
(HERE/'minor_source-engine-checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
