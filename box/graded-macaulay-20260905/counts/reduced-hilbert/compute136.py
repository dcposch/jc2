#!/usr/bin/env python3
"""Two finite low-degree Hilbert cells in the exact homogeneous unit quotient.

No Groebner basis. Only source images that can contribute are expanded.
"""
from pathlib import Path
import sys,json,hashlib,time,heapq
from fractions import Fraction
from math import lcm
sys.path.insert(0,str(Path('box/k16xempty-20260905/linear_python').resolve()))
sys.path.insert(0,str(Path('box/graded-macaulay-20260905/hilbert').resolve()))
sys.path.insert(0,str(Path('box/graded-macaulay-20260905/reduced').resolve()))
sys.path.insert(0,str(Path('box/graded-macaulay-20260905/counts').resolve()))
from flint import fmpq_mpoly,fmpq_mpoly_ctx
from reduce_counts import parse
from exact_counts import dp_individual,dp_grouped
from compute_hilbert import monomial_pieces
from sparse_linear import IntegerRowSpace,ModularRowSpace,controls

OUT=Path('box/graded-macaulay-20260905/counts/reduced-hilbert')
INPUT=Path('box/graded-macaulay-20260905/reduced/136/reduced-counts.json')
P=1073741827
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def run():
 start=time.monotonic();j=json.loads(INPUT.read_text());variables=j['source_variables'];remaining=j['remaining_variables'];W=j['weights']
 assert sha(j['source'])==j['source_sha256'];ctx=fmpq_mpoly_ctx.get(tuple(variables),'lex');redctx=fmpq_mpoly_ctx.get(tuple(remaining),'lex')
 gens=dict(zip(variables,ctx.gens()));cache=dict(zip(remaining,redctx.gens()));byv={p['variable']:p for p in j['pivots']};zero=redctx.constant(0)
 image_terms={};composition_rows=0
 def image(v):
  if v in cache:return cache[v]
  pivot=byv[v];q=Fraction(pivot['coefficient']);expr=pivot['original_row'];terms=parse(expr)
  f=(fmpq_mpoly(expr,ctx)-gens[v]*q.numerator/q.denominator)*(-q.denominator)/q.numerator
  needed={z for _,m in terms for z in m if z!=v}
  args=[image(z) if z in needed else zero for z in variables]
  result=f.compose(*args,ctx=redctx)
  assert len(result)<=200000,('IMAGE_TERM_CAP',v,len(result))
  cache[v]=result;image_terms[v]=len(result)
  return result
 rows=[];eligible_indices=[];zero_indices=[];saved=[]
 for line in Path(j['source']).read_text().splitlines()[1:]:
  ix,h,b,a,expr=line.split('|',4);ix,h,b,a=map(int,(ix,h,b,a));degree=(b+1,29-a-6*h)
  if degree[0]>6 or degree[1]>12:continue
  eligible_indices.append(ix);terms=parse(expr);needed={z for _,m in terms for z in m}
  args=[image(z) if z in needed else zero for z in variables]
  f=fmpq_mpoly(expr,ctx).compose(*args,ctx=redctx);composition_rows+=1
  assert len(f)<=200000,('ROW_TERM_CAP',ix,len(f))
  if not f:zero_indices.append(ix);assert str(ix) not in j['nonzero_evaluations'];continue
  assert str(ix) in j['nonzero_evaluations']
  coefficients={}
  for exponents,coefficient in f.terms():
   actual=tuple(sum(e*W[v][k] for v,e in zip(remaining,exponents)) for k in (0,1));assert actual==degree
   monomial=tuple(i for i,e in enumerate(exponents) for _ in range(e));coefficients[monomial]=Fraction(str(coefficient))
  denominator=1
  for q in coefficients.values():denominator=lcm(denominator,q.denominator)
  row={m:int(q*denominator) for m,q in coefficients.items()};assert all(row.values())
  rows.append(dict(index=ix,degree=degree,terms=row,denominator=denominator))
  saved.append(dict(source_index=ix,degree=degree,denominator_clear=denominator,reduced_expression=str(f),nonzero_terms=len(f)))
  print('EXPANDED',ix,degree,len(f),flush=True)
 (OUT/'eligible-images.json').write_text(json.dumps(dict(input_sha256=sha(INPUT),remaining_variables=remaining,pivot_image_terms=image_terms,source_images=saved,exact_zero_indices=zero_indices,all_eligible_source_indices=eligible_indices),indent=2)+'\n')
 degrees=[tuple(W[v]) for v in remaining];pieces,counts=monomial_pieces(degrees,6,12)
 assert counts==dp_individual(degrees,6,12)==dp_grouped(degrees,6,12)
 results=[]
 for B in (5,6):
  t=time.monotonic();Y=12;columns=sorted(pieces[B][Y]);lookup={m:i for i,m in enumerate(columns)};assert len(columns)<100000
  qs=IntegerRowSpace();ps=ModularRowSpace(P);mhash=hashlib.sha256();sourcecount=nnz=0
  # Smaller reduced source polynomials first to limit fill; this is Gaussian
  # row ordering, not polynomial completion or degree expansion.
  for g in sorted(rows,key=lambda g:(len(g['terms']),g['index'])):
   b,w=g['degree']
   if b>B or w>Y:continue
   for multiplier in pieces[B-b][Y-w]:
    row={lookup[tuple(heapq.merge(multiplier,m))]:c for m,c in g['terms'].items()}
    assert len(row)==len(g['terms']);mhash.update(repr((g['index'],multiplier,sorted(row.items()))).encode()+b'\n');nnz+=len(row);sourcecount+=1
    qs.add(row);ps.add(row)
    if sourcecount%1000==0:print('RANK_PROGRESS',B,Y,sourcecount,qs.rank,ps.rank,round(time.monotonic()-t,2),flush=True)
  expected=sum(counts[B-g['degree'][0]][Y-g['degree'][1]] for g in rows if g['degree'][0]<=B and g['degree'][1]<=Y);assert sourcecount==expected
  assert ps.rank<=qs.rank<=min(sourcecount,len(columns))
  result=dict(B=B,Y=Y,reduced_columns=len(columns),reduced_rows=sourcecount,nonzeros=nnz,rank_Q=qs.rank,rank_Fp=ps.rank,prime=P,hilbert_Q=len(columns)-qs.rank,
   matrix_sha256=mhash.hexdigest(),exact_echelon_sha256=hashlib.sha256(repr(sorted((k,sorted(v.items())) for k,v in qs.pivots.items())).encode()).hexdigest(),
   rational_elimination_steps=qs.elimination_steps,elapsed_seconds=time.monotonic()-t,status='EXACT_Q')
  results.append(result);print('COMPONENT',json.dumps(result),flush=True)
  (OUT/'checkpoint.json').write_text(json.dumps(results,indent=2)+'\n')
 output=dict(fibre=136,input=str(INPUT),input_sha256=sha(INPUT),original_source=j['source'],original_source_sha256=sha(j['source']),driver_sha256=sha(__file__),remaining_variables=remaining,
  source_rows_composed_exactly=composition_rows,eligible_source_indices=eligible_indices,exact_zero_indices=zero_indices,nonzero_source_images=len(rows),pivot_images_expanded=image_terms,
  image_artifact_sha256=sha(OUT/'eligible-images.json'),controls=controls(P),components=results,total_elapsed_seconds=time.monotonic()-start,
  conclusion='Exact Hilbert function of original R/I via homogeneous rational unit quotient. No specialization or Groebner basis.',
  rational_arithmetic='flint fmpq_mpoly for exact recursive source images; integer primitive Gaussian elimination for Q rank; modular Gaussian crosscheck')
 (OUT/'hilbert136.json').write_text(json.dumps(output,indent=2)+'\n')
 print('DONE',flush=True)
if __name__=='__main__':OUT.mkdir(parents=True,exist_ok=True);run()
