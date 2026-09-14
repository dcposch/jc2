#!/usr/bin/env python3
"""Full exact unit-pivot quotient; sparse nonzero/zero tests, exact degree counts.
No Groebner basis. A modular nonzero evaluation certifies a polynomial NONZERO
in Q. Candidate zeros are expanded and checked exactly by fmpq_mpoly.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import json, re, hashlib, sys, random, time
sys.path.insert(0,str(Path('box/k16xempty-20260905/linear_python').resolve()))
sys.path.insert(0,str(Path('box/graded-macaulay-20260905/counts').resolve()))
from flint import fmpq_mpoly, fmpq_mpoly_ctx
from exact_counts import dp_individual,dp_grouped
OUT=Path('box/graded-macaulay-20260905/reduced')
OLD=Path('box/graded-moh-20260905')
TERM=re.compile(r'[+-]?[^+-]+'); FAC=re.compile(r'([A-Za-z][A-Za-z0-9_]*)(?:\^(\d+))?$')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def parse(expr):
 out=[]
 for t in TERM.findall(expr):
  c=Q(-1 if t.startswith('-') else 1); mon={}
  for fac in t.lstrip('+-').split('*'):
   m=FAC.fullmatch(fac)
   if m:v,e=m.groups();assert v not in mon;mon[v]=int(e or 1)
   else:c*=Q(fac)
  assert c;out.append((c,mon))
 return out
P=1073741827
def eval_poly(terms,vals):
 s=0
 for q,mon in terms:
  v=(q.numerator%P)*pow(q.denominator,-1,P)%P
  for name,e in mon.items():v=v*pow(vals[name],e,P)%P
  s=(s+v)%P
 return s

def run(n):
 start=time.time();ap=next(p for p in (OLD/'instrument').glob('*_audit.json') if json.loads(p.read_text()).get('parameter_count')==n)
 a=json.loads(ap.read_text());W={v:(-b,w) for v,(b,w) in a['bidegrees'].items()};variables=a['variables'];p,D=W['c'];source=Path(a['rows_path'])
 assert sha(source)==a['rows_sha256']
 rows=[]
 for line in source.read_text().splitlines()[1:]:
  ix,j,b,y,expr=line.split('|',4);degree=(int(b)+1,D-int(y));assert int(j)==0
  ts=parse(expr)
  for q,m in ts:assert tuple(sum(W[v][k]*e for v,e in m.items()) for k in (0,1))==degree
  rows.append(dict(index=int(ix),degree=degree,expr=expr,terms=ts))
 allA={v for v in variables if v.startswith('A') and W[v][0]>0};pivot=[]
 for r in rows:
  can=[(q,next(iter(m))) for q,m in r['terms'] if len(m)==1 and next(iter(m)) in allA and next(iter(m.values()))==1]
  assert len(can)<=1
  if can:q,v=can[0];pivot.append(dict(index=r['index'],variable=v,coefficient=q,degree=W[v]))
 assert len(pivot)==len(allA) and {x['variable'] for x in pivot}==allA
 pivot.sort(key=lambda x:(x['degree'][1],x['index']));order={x['variable']:i for i,x in enumerate(pivot)}
 for i,x in enumerate(pivot):
  v=x['variable'];ts=rows[x['index']]['terms'];occ=[(q,m) for q,m in ts if v in m];assert occ==[(x['coefficient'],{v:1})]
  deps={z for q,m in ts for z in m if z in allA and z!=v};assert all(order[z]<i for z in deps)
  x['dependencies']=sorted(deps,key=order.get)
 remaining=[v for v in variables if v not in allA];pivotix={x['index'] for x in pivot};values=[]
 for seed in [20260905,20260906]:
  rng=random.Random(seed);vals={v:rng.randrange(1,P) for v in remaining}
  for x in pivot:
   v=x['variable'];q=x['coefficient'];ts=[(c,m) for c,m in rows[x['index']]['terms'] if m!={v:1}]
   vals[v]=-eval_poly(ts,vals)*pow(q.numerator%P,-1,P)*q.denominator%P
   assert eval_poly(rows[x['index']]['terms'],vals)==0
  values.append(vals)
 candidates=[];nonzero={}
 for r in rows:
  ev=[eval_poly(r['terms'],v) for v in values]
  if any(ev):nonzero[r['index']]=ev
  else:candidates.append(r['index'])
 zero_candidates=[i for i in candidates if i not in pivotix]
 print(n,'pivots',len(pivot),'remaining',len(remaining),'nonzero',len(nonzero),'extra-zero-candidates',zero_candidates,flush=True)
 # Recursive exact composition only where polynomial zero needs proof.
 # Do not expand all nonzero images: exact modular nonzero evaluation proves them.
 ctx=fmpq_mpoly_ctx.get(tuple(variables),'lex');redctx=fmpq_mpoly_ctx.get(tuple(remaining),'lex');gens=dict(zip(variables,ctx.gens()));redgens=dict(zip(remaining,redctx.gens()));cache=dict(redgens);imagecounts={}
 byv={x['variable']:x for x in pivot}
 def image(v):
  if v in cache:return cache[v]
  x=byv[v];r=rows[x['index']];f=fmpq_mpoly(r['expr'],ctx);q=x['coefficient'];f=(f-gens[v]*q.numerator/q.denominator)*(-q.denominator)/q.numerator
  needed={z for _,m in r['terms'] for z in m if z!=v}
  args=[image(z) if z in needed else redctx.constant(0) for z in variables]
  cache[v]=f.compose(*args,ctx=redctx);imagecounts[v]=len(cache[v]);return cache[v]
 zero=[]
 for ix in zero_candidates:
  r=rows[ix];needed={z for _,m in r['terms'] for z in m};f=fmpq_mpoly(r['expr'],ctx)
  args=[image(z) if z in needed else redctx.constant(0) for z in variables]
  ans=f.compose(*args,ctx=redctx);assert ans.is_zero(),(n,ix,'accidental modular zero; needs another point')
  zero.append(ix);print(n,'verified extra zero',ix,flush=True)
 kept=[r for r in rows if r['index'] in nonzero];assert len(kept)+len(zero)+len(pivot)==len(rows)
 dims=dp_individual([W[v] for v in remaining],3*p,3*D);assert dims==dp_grouped([W[v] for v in remaining],3*p,3*D)
 dims0=dp_individual([W[v] for v in remaining if v!='c'],3*p,3*D)
 cix=next(r['index'] for r in rows if any('c' in m for _,m in r['terms']));assert cix in nonzero
 tests=[]
 for N in (1,2,3):
  X,Y=N*p,N*D
  contributions=[{'source_index':r['index'],'degree':r['degree'],'rows':dims[X-r['degree'][0]][Y-r['degree'][1]]} for r in kept if r['degree'][0]<=X and r['degree'][1]<=Y]
  contributions0=[{'source_index':r['index'],'degree':r['degree'],'rows':dims0[X-r['degree'][0]][Y-r['degree'][1]]} for r in kept if r['index']!=cix and r['degree'][0]<=X and r['degree'][1]<=Y]
  tests.append(dict(N=N,degree=[X,Y],columns=dims[X][Y],rows=sum(x['rows'] for x in contributions),contributions=contributions,c_eliminated_columns=dims0[X][Y],c_eliminated_rows=sum(x['rows'] for x in contributions0),c_eliminated_contributions=contributions0))
 out=dict(fibre=n,source=str(source),source_sha256=sha(source),audit_sha256=sha(ap),driver_sha256=sha(__file__),field='Q',source_variables=variables,weights=W,pivot_count=len(pivot),remaining_variables=remaining,pivots=[{**x,'coefficient':str(x['coefficient']),'original_row':rows[x['index']]['expr']} for x in pivot],map='For each ordered pivot v with row q*v+h, map v to -phi(h)/q, fix all remaining variables. All other pivot dependencies precede v. Map homogeneous and fixes c.',nonzero_evaluation_prime=P,nonzero_evaluation_seeds=[20260905,20260906],evaluation_remaining_values=[{v:d[v] for v in remaining} for d in values],nonzero_evaluations=nonzero,additional_zero_rows_exact_flint=zero,exact_zero_expansion_cached_images_terms=imagecounts,source_row_count=len(rows),nonzero_reduced_generator_count=len(kept),target_source_index=cix,tests=tests,elapsed_seconds=time.time()-start)
 dest=OUT/str(n);dest.mkdir(exist_ok=True);(dest/'reduced-counts.json').write_text(json.dumps(out,indent=2)+'\n')
 print(n,'DONE',[(x['N'],x['columns'],x['rows'],x['c_eliminated_columns'],x['c_eliminated_rows']) for x in tests],flush=True)
 return out
if __name__=='__main__':
 OUT.mkdir(exist_ok=True)
 for n in map(int,sys.argv[1:] or [77,111,129,136]):run(n)
