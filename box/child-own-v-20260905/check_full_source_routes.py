#!/usr/bin/env python3
import sys,json,importlib.util,time
from pathlib import Path
from fractions import Fraction
from collections import Counter
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'box/lib'))
from own_v_routes import OwnVRouteTree
spec=importlib.util.spec_from_file_location('route_frozen_B','/tmp/jc2-lane.wwyG4k/inputs/moh_skeleton_full.py');B=importlib.util.module_from_spec(spec);spec.loader.exec_module(B)
HERE=Path(__file__).resolve().parent

def serial(x):
 if isinstance(x,Fraction):return str(x)
 raise TypeError(type(x))

def main():
 rows=json.load(open(HERE/'first-nonzero-candidates.json'))['without_q_capacity']['rows']
 counts=Counter();out=[];start=time.time()
 for k,r in enumerate(rows):
  S=B.Skel(r['n'],r['m'],r['M'][1:],{i+2:v for i,v in enumerate(r['V'])});T=OwnVRouteTree(S)
  kept=[];rejected=[]
  for c in r['candidates']:
   witness=T.compatible_first_support(c['first_nonzero'])
   if witness is not None:kept.append(dict(first_nonzero=c['first_nonzero'],W=c['W'],witness=witness))
   else:rejected.append(c['first_nonzero'])
  counts[len(kept)]+=1
  out.append(dict(n=r['n'],m=r['m'],M=r['M'],V=r['V'],u_s=r['u_s'],drops=r['drops'],kept=kept,rejected=rejected))
  if (k+1)%100==0:print(k+1,dict(counts),round(time.time()-start,2),flush=True)
 summary=dict(rows=len(rows),sizes=dict(counts),seconds=round(time.time()-start,3),nonempty_u=Counter(r['u_s'] for r in out if r['kept']),kept_routes=sum(len(r['kept']) for r in out),drop_nonempty=sum(bool(r['kept']) and r['drops'] for r in out))
 (HERE/'full-source-routes.json').write_text(json.dumps(dict(summary=summary,rows=out),default=serial,indent=2)+'\n')
 print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
