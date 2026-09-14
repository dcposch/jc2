#!/usr/bin/env python3
"""Scan Newton-relevant three-term centered Q shapes over a small field."""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('rc',HERE/'reduced_centered.py')
rc=importlib.util.module_from_spec(sp);assert sp.loader;sp.loader.exec_module(rc)


def relevant(terms):
    reach={(0,0)}
    for _ in range(7):
        reach|={(D+6-r,E+e) for D,E in list(reach) for r,e in terms
                if D+6-r<=14 and E+e<=9}
    return (14,9) in reach


def independent_order(terms):
    for i,j in itertools.combinations(range(3),2):
        r1,e1=terms[i];r2,e2=terms[j]
        if e1*(r2-6)-e2*(r1-6):
            k=3-i-j
            return (terms[i],terms[j],terms[k])
    raise AssertionError('all three weights collinear')


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--prime',type=int,default=101)
    ap.add_argument('--out',type=Path);args=ap.parse_args();p=args.prime
    gens=[(r,e) for r in range(5) for e in range(3*(6-r)+1)]
    hits=[];seen=shapes=0
    for raw in itertools.combinations(gens,3):
        if not relevant(raw):continue
        shapes+=1;terms=independent_order(raw)
        for C in range(1,p):
            q={}
            for (r,e),coef in zip(terms,(1,1,C)):
                q.setdefault(r,{})[e]=coef
            rows,target,_=rc.reduce_q(q,p);ok,tr,assignment=rc.solve(rows,target,p,True)
            seen+=1
            if ok and any(tr):
                hit={'raw_terms':raw,'normalized_terms':terms,'coefficient':C,
                     'target_reduced':tr,'integration_constants':assignment}
                hits.append(hit);print(json.dumps(hit),flush=True)
    payload={'prime':p,'relevant_shapes':shapes,'seen':seen,'hit_count':len(hits),'hits':hits}
    if args.out:args.out.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:payload[k] for k in ('prime','relevant_shapes','seen','hit_count')}))


if __name__=='__main__':main()
