#!/usr/bin/env python3
"""Independent FLINT dense checks for sparse elimination and selected real pieces."""
import hashlib
import heapq
import json
from pathlib import Path
import random
import sys
sys.dont_write_bytecode=True
sys.path.insert(0,str(Path('box/k16xempty-20260905/linear_python').resolve()))
from flint import fmpq_mat,nmod_mat,fmpz
from sparse_linear import IntegerRowSpace,ModularRowSpace,rational_combination,controls
from compute_hilbert import OUT,PROFILES,INSTRUMENT,parse_rows,monomial_pieces

P=1073741827


def check(rows,ncols):
    q,p=IntegerRowSpace(),ModularRowSpace(P)
    for row in rows:
        q.add(row);p.add(row)
    dense=[[row.get(j,0) for j in range(ncols)] for row in rows]
    if dense:
        dense_q=fmpq_mat(dense).rref()[1]
        dense_p=nmod_mat(dense,P).rank()
    else:
        dense_q=dense_p=0
    assert (q.rank,p.rank)==(dense_q,dense_p)
    return dict(rows=len(rows),columns=ncols,sparse_Q_rank=q.rank,
                flint_Q_rank=dense_q,sparse_Fp_rank=p.rank,flint_Fp_rank=dense_p)


def main():
    assert fmpz(P).is_prime()
    rng=random.Random(20260905)
    random_checks=[]
    for case in range(100):
        nrows=rng.randrange(1,13);ncols=rng.randrange(1,13)
        rows=[{j:rng.randrange(-7,8) for j in range(ncols) if rng.randrange(3)==0}
              for _ in range(nrows)]
        if case%5==0:
            rows.append({k:P*v for k,v in rows[0].items()})
        result=check(rows,ncols)
        scalars=[rng.randrange(-5,6) for _ in rows]
        target={j:sum(a*row.get(j,0) for a,row in zip(scalars,rows)) for j in range(ncols)}
        assert rational_combination(rows,target) is not None
        result.update(case=case,exact_generated_membership_identity_replayed=True)
        random_checks.append(result)
    real=[]
    for profile in json.loads(PROFILES.read_text()):
        n=profile['parameters']
        if n not in (77,111,129,136):continue
        audit=json.loads((INSTRUMENT/(profile['stem']+'_audit.json')).read_text())
        names,degrees,generators,_=parse_rows(profile,audit)
        B,Y={77:(2,7),111:(2,7),129:(2,11),136:(2,5)}[n]
        pieces,_=monomial_pieces(degrees,B,Y)
        lookup={m:i for i,m in enumerate(sorted(pieces[B][Y]))}
        rows=[]
        for g in generators:
            b,y=g['degree']
            if b>B or y>Y:continue
            for multiplier in pieces[B-b][Y-y]:
                rows.append({lookup[tuple(heapq.merge(multiplier,m))]:a for m,a in g['terms'].items()})
        result=check(rows,len(lookup))
        result.update(parameters=n,B=B,Y=Y)
        real.append(result)
    result=dict(prime=P,prime_verified_by_flint=True,toy_membership_controls=controls(P),
                deterministic_random_dense_crosschecks=random_checks,
                original_ring_dense_crosschecks=real,
                driver_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (OUT/'linear_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(random_checks=len(random_checks),real=real,all_passed=True),indent=2))


if __name__=='__main__':main()
