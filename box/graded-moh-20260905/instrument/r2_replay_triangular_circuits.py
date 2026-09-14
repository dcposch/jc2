#!/usr/bin/env python3
"""Exact compact rational-circuit replay of the triangular quotient maps."""
import json,re,hashlib
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path('/home/ubuntu/jc2/box/graded-moh-20260905');TERM=re.compile(r'[+-]?[^+-]+');FAC=re.compile(r'([A-Za-z][A-Za-z0-9_]*)(?:\^(\d+))?')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for n in (77,136):
 d=ROOT/'resume-r2'/'triangular'/str(n);source=d/'triangular-dag-custody.json';m=json.loads(source.read_text());nodes=[];lookup={}
 def intern(node):
  key=json.dumps(node,separators=(',',':'))
  if key in lookup:return lookup[key]
  i=len(nodes);nodes.append(node);lookup[key]=i;return i
 ZERO=intern(['add',[]]);ONE=intern(['mul',[]])
 def add(pairs):
  terms={}
  def consume(q,node):
   if not q:return
   if nodes[node][0]=='add':
    for c,ch in nodes[node][1]:consume(q*Q(c),ch)
   else:terms[node]=terms.get(node,Q(0))+q
  for q,node in pairs:consume(q,node)
  terms={k:v for k,v in terms.items() if v}
  if len(terms)==1:
   k,v=next(iter(terms.items()))
   if v==1:return k
  return intern(['add',[[str(c),k] for k,c in sorted(terms.items())]])
 def mul(pairs):
  factors={}
  for node,e in pairs:
   if node==ZERO:return ZERO
   if not e:continue
   if nodes[node][0]=='mul':
    for ch,k in nodes[node][1]:factors[ch]=factors.get(ch,0)+e*k
   else:factors[node]=factors.get(node,0)+e
  if len(factors)==1:
   node,e=next(iter(factors.items()))
   if e==1:return node
  return intern(['mul',[[node,e] for node,e in sorted(factors.items())]])
 images={v:intern(['variable',v]) for v in m['remaining_free_coordinates']}
 def image_monomial(mon,override=None):
  return mul([((override or {}).get(v,images[v]),e) for v,e in mon.items()])
 def parse(expr):
  out=[]
  for term in TERM.findall(expr):
   q=Q(-1 if term.startswith('-') else 1);mon={}
   for f in term.lstrip('+-').split('*'):
    z=FAC.fullmatch(f)
    if z:v,e=z.groups();mon[v]=int(e or 1)
    else:q*=Q(f)
   out.append((q,mon))
  return out
 checks=[];negative=[]
 for p in m['pivot_dag']:
  terms=p['image_expression_before_recursion'];image=add([(Q(t['coefficient']),image_monomial(t['monomial'])) for t in terms]);v=p['pivot'];images[v]=image
  row=parse(p['source_expression']);value=add([(q,image_monomial(mon)) for q,mon in row]);assert value==ZERO,(n,v)
  broken=add([(Q(1),image),(Q(1),ONE)]);bad=add([(q,image_monomial(mon,{v:broken})) for q,mon in row]);assert bad!=ZERO
  checks.append({'pivot':v,'source_index':p['source_index'],'image_node':image,'source_row_image_node':value});negative.append(v)
 assert images['c']==intern(['variable','c'])
 data={'fibre':n,'coefficient_field':'Q','node_semantics':{'variable':'remaining coordinate','mul':'product of listed child node powers','add':'sum of exact rational coefficient times child node'},'source_custody_sha256':sha(source),'verifier_sha256':sha(Path(__file__)),'nodes':nodes,'source_variable_order':m['source_variable_order'],'map_images':{v:images[v] for v in m['source_variable_order']},'pivot_identity_checks':checks,'map_fixes_c':True,'negative_control_perturb_each_pivot_image_by_one_rejected':negative,'quotient_isomorphism':'Each rational-unit equation solves its pivot using only prior pivots and remaining coordinates. The displayed recursive circuit map kills all pivot equations by exact scalar/add/product identities. Mapping remaining coordinates back to their classes is inverse by forward substitution. Imposing images of every nonpivot row gives the complete chart quotient, without arbitrary specialization.'}
 (d/'triangular-circuit-replay.json').write_text(json.dumps(data,indent=2)+'\n');summary={k:data[k] for k in ('fibre','source_custody_sha256','verifier_sha256','map_fixes_c')};summary.update(nodes=len(nodes),verified_pivot_identities=len(checks),negative_controls=len(negative),circuit_sha256=sha(d/'triangular-circuit-replay.json'));(d/'triangular-circuit-summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(summary)
