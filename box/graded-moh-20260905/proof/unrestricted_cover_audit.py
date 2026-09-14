#!/usr/bin/env python3
from pathlib import Path
import json,re,time
root=Path('box/graded-moh-20260905/proof/torus_branches');out=[]
for r in json.loads((root/'summary.json').read_text()):
 t=(root/r['stem']/'target_c_polynomial.txt').read_text().strip();edges=set(frozenset(re.findall(r'[A-Za-z][A-Za-z0-9_]*',term))for term in re.findall(r'[+-]?[^+-]+',t));assert all(edges)
 edges=tuple(sorted((e for e in edges if not any(f<e for f in edges)),key=lambda e:(len(e),sorted(e))))
 best=set(r['minimum_hitting_set']);nodes=0;seen=set();start=time.monotonic()
 def search(chosen,left):
  global best,nodes
  nodes+=1
  if not left:
   if len(chosen)<len(best):best=set(chosen)
   return
  if len(chosen)>=len(best):return
  key=tuple(sorted(tuple(sorted(e))for e in left));state=(len(chosen),key)
  if state in seen:return
  seen.add(state)
  used=set();lb=0
  for e in sorted(left,key=lambda e:len(e)):
   if not e&used:used.update(e);lb+=1
  if len(chosen)+lb>=len(best):return
  e=min(left,key=lambda e:len(e))
  freq={v:sum(v in f for f in left)for v in e}
  for v in sorted(e,key=lambda v:(-freq[v],v)):
   search(chosen|{v},tuple(f for f in left if v not in f))
 search(set(),edges)
 item=dict(stem=r['stem'],minimum_cover_all_coordinates=sorted(best),size=len(best),nodes=nodes,elapsed_seconds=round(time.monotonic()-start,3),proved_minimum=True)
 out.append(item);print(json.dumps(item),flush=True)
(root/'unrestricted_cover_summary.json').write_text(json.dumps(out,indent=2)+'\n')
