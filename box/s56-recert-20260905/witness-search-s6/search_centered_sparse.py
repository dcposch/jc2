#!/usr/bin/env python3
"""Sparse centered-Q screens using the exact linear P solver."""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("search_linear_q", HERE / "search_linear_q.py")
SLQ = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(SLQ)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--prime',type=int,default=32003)
    ap.add_argument('-k',type=int,default=3);ap.add_argument('--coeff-min',type=int,default=-12)
    ap.add_argument('--coeff-max',type=int,default=12);ap.add_argument('--out',type=Path)
    args=ap.parse_args();p=args.prime
    gens=[(r,e) for r in range(5) for e in range(3*(6-r)+1)]
    coeffs=[i%p for i in range(args.coeff_min,args.coeff_max+1) if i]
    hits=[];seen=0
    for terms in itertools.combinations(gens,args.k):
        # Normalize all but the last sparse coefficient to one and scan the
        # remaining torus invariant through small exact residues.
        for C in coeffs:
            q={(0,6):1}
            for r,e in terms[:-1]:q[(e,r)]=1
            r,e=terms[-1];q[(e,r)]=C
            seen+=1;rows,target=SLQ.system(q,p);piv,bad=SLQ.echelon(rows,p)
            if bad:continue
            const,free=SLQ.reduce_functional(target,piv,p)
            if const or free:
                hit={'terms':terms,'last_coefficient':C,'target_const':const,
                     'target_free':len(free),'rank':len(piv)}
                hits.append(hit);print(json.dumps(hit),flush=True)
    payload={'prime':p,'k':args.k,'coefficient_residues':coeffs,'seen':seen,
             'hit_count':len(hits),'hits':hits}
    if args.out:args.out.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:payload[k] for k in ('prime','k','seen','hit_count')}))


if __name__=='__main__':main()
