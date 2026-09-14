#!/usr/bin/env python3
"""Recheck full rational unit-map structure, without expanding its DAG."""
from pathlib import Path
from fractions import Fraction
import json,sys,hashlib
sys.path.insert(0,str(Path('box/graded-macaulay-20260905/reduced').resolve()))
from reduce_counts import parse
OUT=Path('box/graded-macaulay-20260905/counts/reduced-hilbert')
INPUT=Path('box/graded-macaulay-20260905/reduced/136/reduced-counts.json')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
j=json.loads(INPUT.read_text());W=j['weights'];P=1073741827
assert sha(j['source'])==j['source_sha256']
source={}
for line in Path(j['source']).read_text().splitlines()[1:]:
 i,h,b,a,e=line.split('|',4);source[int(i)]=(int(b)+1,29-int(a)-6*int(h),e)
assert all('/' not in expr for b,w,expr in source.values()),'original source list has nonintegral coefficient syntax'
pivots=j['pivots'];ordered={x['variable']:i for i,x in enumerate(pivots)};terms_audited=0
for i,pivot in enumerate(pivots):
 v=pivot['variable'];q=Fraction(pivot['coefficient']);b,w,expr=source[pivot['index']]
 assert expr==pivot['original_row'];assert (b,w)==tuple(pivot['degree'])==tuple(W[v]);assert b>0
 assert q and q.numerator%P and q.denominator%P
 terms=parse(expr);occ=[(c,m) for c,m in terms if v in m];assert occ==[(q,{v:1})]
 dependencies={u for c,m in terms for u in m if u in ordered and u!=v}
 assert dependencies==set(pivot['dependencies']);assert all(ordered[u]<i for u in dependencies)
 for c,m in terms:
  assert c.denominator%P
  assert tuple(sum(e*W[u][k] for u,e in m.items()) for k in (0,1))==(b,w)
 terms_audited+=len(terms)
assert set(j['remaining_variables']).isdisjoint(ordered)
assert set(j['remaining_variables'])|set(ordered)==set(j['source_variables'])
assert 'c' in j['remaining_variables']
images=json.loads((OUT/'eligible-images.json').read_text())
assert images['input_sha256']==sha(INPUT)
assert all(x['denominator_clear']%P for x in images['source_images'])
h=json.loads((OUT/'hilbert136.json').read_text())
assert h['input_sha256']==sha(INPUT)
assert h['image_artifact_sha256']==sha(OUT/'eligible-images.json')
assert all(t['rank_Q']==t['rank_Fp'] for t in h['components'])
result=dict(verdict='PASS',driver_sha256=sha(__file__),full_unitmap_path=str(INPUT),full_unitmap_sha256=sha(INPUT),
 original_source_path=j['source'],original_source_sha256=sha(j['source']),pivot_count=len(pivots),pivot_source_terms_audited=terms_audited,
 every_pivot_constant_nonzero_rational=True,every_pivot_occurs_only_as_its_linear_term=True,all_other_pivot_dependencies_strictly_prior=True,
 every_pivot_original_row_and_bidegree_rechecked=True,remaining_variables_fixed=True,c_fixed=True,
 map_conclusion='Full homogeneous Q-algebra quotient isomorphism: source variable v at pivot q*v+h maps recursively to -phi(h)/q; inverse fixes the remaining quotient coordinates.',
 prime=P,all_source_and_unit_division_denominators_avoid_prime=True,all_reduced_row_denominators_avoid_prime=True,
 reduced_row_image_path=str(OUT/'eligible-images.json'),reduced_row_image_sha256=sha(OUT/'eligible-images.json'),
 hilbert_result_path=str(OUT/'hilbert136.json'),hilbert_result_sha256=sha(OUT/'hilbert136.json'),exactQ_and_modular_rank_equality=True,
 scope='Structural full-map proof plus custody validation; low eligible source images were all expanded exactly by compute136.py. No full high-weight expansion or Groebner basis.')
(OUT/'unitmap-verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
