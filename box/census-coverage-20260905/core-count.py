#!/usr/bin/env python3
"""Audit-only relaxed census derived at runtime from the frozen source.
No upstream edits. Dumps every full=True numerical row n<=200, Kmin=2.
"""
import argparse, importlib.util, json, pathlib, time, collections
ROOT=pathlib.Path(__file__).resolve().parent
SOURCE=pathlib.Path('/tmp/jc2-lane.94eJYj/inputs/moh_skeleton_full.py')
spec=importlib.util.spec_from_file_location('frozen_moh',SOURCE)
M=importlib.util.module_from_spec(spec);spec.loader.exec_module(M)

def run(lo=1,hi=200):
    rows=[];summary=[];t0=time.time()
    with (ROOT/'core-rows-kmin2.jsonl').open('w') as out:
      for n in range(lo,hi+1):
        ts=time.time();ct=collections.Counter();groups=collections.defaultdict(set)
        for m,Ms,V in M.census(n,Kmin=2,full=True):
          S=M.Skel(n,m,list(Ms),V)
          tag='baseline' if S.K>=16 else 'kmin_extra'
          row=dict(n=n,m=m,M=list(Ms),V=V,K=S.K,s=S.s,u=str(S.u),tag=tag)
          out.write(json.dumps(row,sort_keys=True)+'\n');ct[tag]+=1
          groups[tag].add((m,Ms,V[S.s]))
        rec=dict(n=n,counts=dict(ct),groups={k:len(v) for k,v in groups.items()},elapsed=round(time.time()-ts,3))
        summary.append(rec)
        if ct: print(json.dumps(rec),flush=True)
    totals=collections.Counter();gtot=collections.Counter()
    for a in summary: totals.update(a['counts']);gtot.update(a['groups'])
    result=dict(lo=lo,hi=hi,totals=dict(totals),groups=dict(gtot),elapsed=time.time()-t0,by_degree=summary)
    (ROOT/'core-count-summary.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='by_degree'}),flush=True)
if __name__=='__main__':run()
