#!/usr/bin/env python3
"""Generate the exact finite-w projection of the singular locus of H."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path

import generate_v2 as base


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate", type=Path, required=True)
    args = parser.parse_args()
    got = sha256(args.candidate.read_bytes()).hexdigest()
    if got != base.CANDIDATE_SHA256:
        raise RuntimeError((got, base.CANDIDATE_SHA256))
    payload = json.loads(args.candidate.read_text())
    if payload.get("status") != "PASS" or payload.get("degree_v") != 190:
        raise RuntimeError("candidate endpoint mismatch")
    print("ring R=127,(v,w),lp;")
    print(f"poly H={base.polynomial(payload)};")
    print('print("Q8-P127-CANDIDATE-SINGULAR-PROJECTION");')
    print('print("candidate_sha256=' + got + '");')
    print("poly Hv=diff(H,v); poly Hw=diff(H,w);")
    print("ideal S=H,Hv,Hw;")
    print("ideal G=std(S);")
    print('print("singular_dim="+string(dim(G)));')
    print('if(dim(G)==0){print("singular_vdim="+string(vdim(G)));}')
    print("ideal Ew=eliminate(G,v); Ew=std(Ew);")
    print('print("elimination_size="+string(size(Ew)));')
    print("poly P=0; int i;")
    print("for(i=1;i<=size(Ew);i++){if(P==0){P=Ew[i];}else{P=gcd(P,Ew[i]);}}")
    print("poly Pg=gcd(P,diff(P,w)); poly Pr=P/Pg;")
    print('print("projection_polynomial_degree="+string(deg(P)));')
    print('print("projection_radical_degree="+string(deg(Pr)));')
    print('print("projection_polynomial_begin"); P; print("projection_polynomial_end");')
    print('print("singular_projection_end");')


if __name__ == "__main__":
    main()
