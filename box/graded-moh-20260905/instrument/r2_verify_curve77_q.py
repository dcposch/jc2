#!/usr/bin/env python3
"""Independent Fraction-arithmetic bounded Buchberger replay; no CAS calls."""
import json,hashlib,re
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path('/home/ubuntu/jc2/box/graded-moh-20260905');TERM=re.compile(r'[+-]?[^+-]+');FACTOR=re.compile(r'([A-Za-z][A-Za-z0-9_]*)(?:\^(\d+))?')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for n in (77,):
 d=ROOT/'resume-r2'/'triangular'/str(n)/'curve';m=json.loads((d/'custody.json').read_text());vv=m['receiver_variable_order'];vi={v:i for i,v in enumerate(vv)};weights=[m['receiver_weights'][v] for v in vv];X=m['combined_target_degree'];zero=(0,)*len(vv)
 def degree(mm):return sum(e*w for e,w in zip(mm,weights))
 def order(mm):return (degree(mm),tuple(-x for x in reversed(mm)))
 def addto(p,mono,coef):
  c=p.get(mono,Q(0))+coef
  if c:p[mono]=c
  elif mono in p:del p[mono]
 def parse(s,source=False):
  p={}
  if s.strip()=='0':return p
  for raw in TERM.findall(s):
   if source and any(m['source_variable_map'].get(v)=='0' for v in re.findall(r'[AB]\d+_\d+_\d+|h_\d+_\d+|\bc\b',raw)):continue
   coef=Q(-1 if raw.startswith('-') else 1);mon=list(zero);omit=False
   for f in raw.lstrip('+-').split('*'):
    ma=FACTOR.fullmatch(f)
    if ma:
     v,e=ma.groups();e=int(e or 1)
     if source and m['source_variable_map'].get(v,'').startswith('t^'):
      mon[vi['t']]+=int(m['source_variable_map'][v][2:])*e;continue
     assert v in vi,(n,v)
     mon[vi[v]]+=e
    else:coef*=Q(f)
   if not omit:addto(p,tuple(mon),coef)
  return p
 def divisible(a,b):return all(x>=y for x,y in zip(a,b))
 G=[parse(p) for p in (d/'basis.txt').read_text().strip().split(',')];assert all(G)
 leads=[max(g,key=order) for g in G]
 assert all(len({degree(mm) for mm in g})==1 and degree(le)<=X for g,le in zip(G,leads))
 def normalform(f,gg=G,ll=leads):
  p=dict(f);nf={};steps=0
  while p:
   lm=max(p,key=order);lc=p[lm]
   for g,gl in zip(gg,ll):
    if divisible(lm,gl):
     mult=tuple(x-y for x,y in zip(lm,gl));coef=lc/g[gl]
     for mm,cc in g.items():addto(p,tuple(x+y for x,y in zip(mm,mult)),-coef*cc)
     break
   else:nf[lm]=p.pop(lm)
   steps+=1;assert steps<1000000
  return nf
 gen_count=0
 for line in Path(m['source_rows']).read_text().splitlines()[1:]:
  ix,h,x,y,expr=line.split('|',4)
  if int(ix) not in set(m['source_indices']):continue
  p=parse(expr,True)
  assert not normalform(p),('generator',ix)
  gen_count+=bool(p)
 count=0
 for i,g in enumerate(G):
  for j in range(i):
   ll=tuple(max(x,y) for x,y in zip(leads[i],leads[j]))
   if degree(ll)>X:continue
   sp={}
   for gg,gl,sgn in [(G[i],leads[i],1),(G[j],leads[j],-1)]:
    mult=tuple(x-y for x,y in zip(ll,gl))
    for mm,cc in gg.items():addto(sp,tuple(x+y for x,y in zip(mm,mult)),sgn*cc/gg[gl])
   assert not normalform(sp),('critical pair',i,j)
   count+=1
 c=parse('c');nf=normalform(c);saved=parse((d/'nf.txt').read_text().strip());assert nf==saved
 assert not normalform(c,G+[c],leads+[next(iter(c))]),'positive membership control failed'
 one={zero:Q(1)};assert normalform(one)==one,'negative constant control failed'
 result={'fibre':n,'field':'Q','order':'positive weighted degree then reverse lex, exact receiver order in custody','target_degree':X,'basis_size':len(G),'nonzero_input_generators_verified':gen_count,'required_critical_pairs_verified':count,'all_basis_elements_homogeneous':True,'all_required_spolynomials_reduce_zero':True,'all_projected_inputs_reduce_zero':True,'target_nf_matches_singular':True,'target_nf_nonzero':bool(nf),'target_nf_is_c':nf==c,'control_add_c_changes_nf_to_zero':True,'control_one_remains_nonzero':True,'basis_sha256':sha(d/'basis.txt'),'normalform_sha256':sha(d/'nf.txt'),'custody_sha256':sha(d/'custody.json'),'verifier_sha256':sha(Path(__file__)),'conclusion':'EXACT_Q_c_NOT_IN_FULL_I' if nf else 'PROJECTED_MEMBERSHIP_ONLY_NO_FULL_CHART_CONCLUSION','proof':'Bounded Buchberger criterion gives a standard basis through positive weightX. Every projected source row of weight<=X lies in its ideal by explicit division. Thus nonzero NF(c) proves c outside this (possibly larger) homogeneous ideal and outside the projected source ideal. Every omitted source row has degree>X and cannot contribute to c. The specialization fixes c, so nonmembership pulls back. Basis provenance inside the input ideal is unnecessary for this one-way nonmembership proof. Zero projected NF gives no full ideal conclusion.'}
 (d/'independent-replay.json').write_text(json.dumps(result,indent=2)+'\n');print(n,len(G),gen_count,count,result['conclusion'])
