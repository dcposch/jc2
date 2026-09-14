#!/usr/bin/env python3
"""Fill the torus-normalization gap in the three-monomial h=y^3 scan."""

from __future__ import annotations
import argparse,importlib.util,itertools,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('mr',HERE/'search_monomial_reduced.py')
mr=importlib.util.module_from_spec(sp);assert sp.loader;sp.loader.exec_module(mr)

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--prime',type=int,default=32003);ap.add_argument('--out',type=Path)
 args=ap.parse_args();p=args.prime;hits=[];seen=shapes=0
 for e2,e1,e0 in itertools.product(range(13),range(16),range(19)):
  if 4*e1-5*e2:continue
  ds={e0-1,e1+e2-1,2*e1-1,e2+e0-1,2*e0-1,e1+2*e2-1,2*e1+e2-1,2*e2+e0-1}
  if 8 not in ds:continue
  # The first two weights are dependent.  Target relevance guarantees that
  # one of them and b0 form an independent pair; normalize that pair and scan
  # the remaining coefficient.
  if 4*e0-6*e2:
   variable=1 # b1 coefficient
  elif 5*e0-6*e1:
   variable=0 # b2 coefficient
  else:
   # Rank-one torus action leaves two invariants; the separate small-integer
   # scan covers one useful slice, but a one-parameter exhaustive fill cannot.
   continue
  shapes+=1
  for C in range(1,p):
   cs=[1,1,1];cs[variable]=C
   bs=[mr.poly_term(e,c,p) for e,c in zip((e2,e1,e0),cs)]
   rows,target=mr.form_rows(bs[0],bs[1],bs[2],p);pv,bad=mr.echelon(rows,p);seen+=1
   if bad:continue
   tr=mr.reduce_target(target,pv,p)
   if any(tr.values()):
    hit={'exponents':[e2,e1,e0],'coefficients':cs,'target_reduced':tr}
    hits.append(hit);print(json.dumps(hit),flush=True)
 payload={'prime':p,'shapes':shapes,'seen':seen,'hit_count':len(hits),'hits':hits}
 if args.out:args.out.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
 print(json.dumps({k:payload[k] for k in ('prime','shapes','seen','hit_count')}))
if __name__=='__main__':main()
