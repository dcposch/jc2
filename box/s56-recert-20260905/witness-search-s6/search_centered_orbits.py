#!/usr/bin/env python3
"""Exhaust three-term centered-Q coefficient orbits over a finite field.

Unlike a normalization to coefficients (1,1,C), this enumerates every orbit
of nonzero coefficient triples under x- and y-scaling.  It first applies a
necessary support-semigroup test for an x^8*z^0 target.
"""

from __future__ import annotations
import argparse,importlib.util,itertools,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('slq',HERE/'search_linear_q.py')
slq=importlib.util.module_from_spec(sp);assert sp.loader;sp.loader.exec_module(slq)

def relevant(ts):
 # The x^8*z^0 bracket can only pair q_0 with p_1 or q_1 with
 # p_0.  Recursively generated p_1 (resp. p_0) uses Q deficits totaling
 # 8 (resp. 9); an integration constant is the empty path.
 R={(0,0)}
 for _ in range(5):
  R|={(D+6-r,E+e) for D,E in list(R) for r,e in ts
      if D+6-r<=9 and E+e<=9}
 return any(
  r in (0,1) and e<=9 and
  any(E==9-e and D<=8+r for D,E in R)
  for r,e in ts
 )

def primitive_root(p):
 n=p-1;facts={q for q in range(2,n+1) if n%q==0 and all(q%d for d in range(2,int(q**.5)+1))}
 for g in range(2,p):
  if all(pow(g,n//q,p)!=1 for q in facts):return g
 raise AssertionError

def reps(ts,p):
 n=p-1;wx=tuple(e for r,e in ts);wy=tuple(r-6 for r,e in ts)
 H={( (u*wx[0]+v*wy[0])%n,(u*wx[1]+v*wy[1])%n,(u*wx[2]+v*wy[2])%n)
    for u in range(n) for v in range(n)}
 unseen=set(itertools.product(range(n),repeat=3));out=[]
 while unseen:
  a=min(unseen);out.append(a)
  unseen.difference_update(((a[0]+h[0])%n,(a[1]+h[1])%n,(a[2]+h[2])%n) for h in H)
 return out

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--prime',type=int,default=29);ap.add_argument('--out',type=Path)
 args=ap.parse_args();p=args.prime;g=primitive_root(p)
 gens=[(r,e) for r in range(5) for e in range(3*(6-r)+1)]
 hits=[];seen=shapes=0
 for ts in itertools.combinations(gens,3):
  if not relevant(ts):continue
  shapes+=1
  for logs in reps(ts,p):
   coeffs=[pow(g,a,p) for a in logs];q={(0,6):1}
   for (r,e),c in zip(ts,coeffs):q[(e,r)]=c
   rows,target=slq.system(q,p);pv,bad=slq.echelon(rows,p);seen+=1
   if bad:continue
   const,free=slq.reduce_functional(target,pv,p)
   if const or free:
    hit={'terms':ts,'coefficient_logs':logs,'coefficients':coeffs,
         'target_const':const,'target_free':len(free),'rank':len(pv)}
    hits.append(hit);print(json.dumps(hit),flush=True)
 payload={'prime':p,'primitive_root':g,'relevant_shapes':shapes,'orbits_seen':seen,
          'hit_count':len(hits),'hits':hits}
 if args.out:args.out.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
 print(json.dumps({k:payload[k] for k in ('prime','relevant_shapes','orbits_seen','hit_count')}))
if __name__=='__main__':main()
