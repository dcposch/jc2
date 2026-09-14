#!/usr/bin/env python3
"""Verify every expanded monomial of available rows against the explicit grading."""
import json,re,hashlib,time
from pathlib import Path
OUT=Path('box/graded-moh-20260905/proof')
profiles=json.loads((OUT/'grading-profiles.json').read_text())
result=[]
term_re=re.compile(r'[+-]?[^+-]+')
factor_re=re.compile(r'([A-Za-z][A-Za-z0-9_]*)(?:\^(\d+))?')
for p in profiles:
 meta=json.loads(Path(p['meta']).read_text());native=Path(meta['rows_path']);paths=[]
 if native.exists() and native.stat().st_size>100:paths.append(native)
 direct=native.with_name(native.stem.replace('_rows','_direct_rows')+'.tsv')
 if direct.exists() and direct.stat().st_size>100:paths.append(direct)
 if p['parameters']==77:
  paths.append(Path('box/moh14-charts-20260905/classes/C_n24m16_Mm12_m2_5_ell1_s4/rows/C_n24m16_Mm12_m2_5_ell1_s4_union_rows.tsv'))
 for path in paths:
  start=time.monotonic();nt=0;nr=0;md=0;lowx=0;lowx_terms=0;hist={}
  for line in path.open():
   if line.startswith('source_index'):continue
   idx,j,b,a,expr=line.rstrip('\n').split('|');j=int(j);b=int(b);a=int(a)
   expected=(b+1,p['D']-a-j*p['K']);assert expected[1]>0,(path,idx,expected)
   hist[str(expected[1])]=hist.get(str(expected[1]),0)+1
   while expr.startswith('(') and expr.endswith(')'):expr=expr[1:-1]
   assert '(' not in expr and ')' not in expr,(path,idx,'NON_EXPANDED_EXPR')
   terms=term_re.findall(expr)
   for term in terms:
    grade=[0,0];deg=0
    for match in factor_re.finditer(term):
     var,exp=match.groups();exp=int(exp or 1);w=p['variables'][var];grade[0]+=exp*w[0];grade[1]+=exp*w[1];deg+=exp
    assert tuple(grade)==expected,(path,idx,term,grade,expected)
    md=max(md,deg)
   nt+=len(terms);nr+=1
   if b<=p['ell']:lowx+=1;lowx_terms+=len(terms)
  result.append(dict(stem=p['stem'],rows=str(path),sha256=hashlib.sha256(path.read_bytes()).hexdigest(),verified_rows=nr,verified_monomials=nt,maximum_ordinary_parameter_degree=md,c_N1_eligible_rows=lowx,c_N1_eligible_row_terms=lowx_terms,weight_histogram=hist,elapsed_seconds=round(time.monotonic()-start,3),verdict='ALL_MONOMIALS_BIHOMOGENEOUS'))
  print(result[-1],flush=True)
(OUT/'row-grading-audit.json').write_text(json.dumps(result,indent=2)+'\n')
