#!/usr/bin/env python3
from pathlib import Path
import re,json,collections
from graded_audit import OUT,rows,TERM,FACTOR,sha
reports=[]
def minimal_cover(clauses):
 clauses=set(frozenset(x) for x in clauses)
 clauses={x for x in clauses if not any(y<x for y in clauses)}
 best=set().union(*clauses)
 def recurse(cs,chosen):
  nonlocal best
  if len(chosen)>=len(best):return
  if not cs:best=chosen;return
  forced=set().union(*(set(c) for c in cs if len(c)==1)) if any(len(c)==1 for c in cs) else set()
  if forced:recurse({c for c in cs if c.isdisjoint(forced)},chosen|forced);return
  freq=collections.Counter(v for c in cs for v in c)
  clause=min(cs,key=lambda c:(len(c),-sum(freq[v] for v in c)))
  for v in sorted(clause,key=lambda v:-freq[v]):recurse({c for c in cs if v not in c},chosen|{v})
 recurse(clauses,set());assert all(c&best for c in clauses);return sorted(best)
for ap in OUT.glob('*_audit.json'):
 a=json.loads(ap.read_text());w=a['bidegrees'];stem=ap.name.removesuffix('_audit.json')
 crows=[]
 for idx,h,b,y,expr in rows(Path(a['rows_path'])):
  if re.search(r'\bc\b',expr):crows.append((idx,expr))
 assert len(crows)==1;idx,expr=crows[0];clauses=[];terms=[]
 for term in TERM.findall(expr):
  used={f.group(1) for factor in term.lstrip('+-').split('*') if (f:=FACTOR.fullmatch(factor))}
  if used=={'c'}:continue
  assert used and 'c' not in used
  clauses.append(used);terms.append(term)
 cover=minimal_cover(clauses)
 dets={v:w['c'][0]*w[v][1]-w[v][0]*w['c'][1] for v in cover}
 assert all(dets.values())
 result={'stem':stem,'source_rows_sha256':a['rows_sha256'],'source_index':idx,'target_row':expr,'non_c_terms':len(terms),'minimal_monomial_hitting_set':cover,'torus_character_determinants':dets,'minimum_proof':'Exhaustive branch-and-bound exact set-cover search, singleton propagation and inclusion-minimal-clause reduction. Each monomial in c target expression has factor in chosen set.','cover_proof':'Target row gives c in ideal(chosen coordinates)+I. Thus D(c) is covered by coordinate opens. Each chosen character and c character are independent over Z (displayed nonzero determinant). The torus character map to (Gm)^2 is an isogeny and surjective over Qbar, so every such open orbit meets c=z=1. This cover requires every listed slice UNIT for full kill.','slice_variables':a['parameter_count']-2}
 reports.append(result);print(stem,len(cover),cover,dets)
(OUT/'two_torus_covers.json').write_text(json.dumps(reports,indent=2)+'\n')
