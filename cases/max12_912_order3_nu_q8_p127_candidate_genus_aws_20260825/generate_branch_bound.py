#!/usr/bin/env python3
"""Generate a safe distinct-branch lower bound for H -> P1_w."""

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
    if (
        payload.get("status") != "PASS"
        or payload.get("prime") != base.P
        or payload.get("degree_v") != 190
        or payload["nonzero_support"].get("190") != [[0, 1]]
    ):
        raise RuntimeError("candidate endpoint mismatch")
    print("ring R=127,(w,v),dp;")
    print(f"poly H={base.polynomial(payload)};")
    print('print("Q8-P127-CANDIDATE-RIEMANN-HURWITZ-BRANCH-BOUND");')
    print('print("candidate_sha256=' + got + '");')
    print("poly Hv=diff(H,v); poly Hw=diff(H,w);")
    print("poly D=resultant(H,Hv,v);")
    print("poly E=resultant(H,Hw,v);")
    print("poly Dg=gcd(D,diff(D,w));")
    print("poly Eg=gcd(E,diff(E,w));")
    print("poly Dr=D/Dg; poly Er=E/Eg;")
    print("poly bad=gcd(Dr,Er);")
    print('print("degree_v_cover=190");')
    print('print("riemann_hurwitz_genus_zero_budget=378");')
    print('print("D_degree="+string(deg(D)));')
    print('print("D_radical_degree="+string(deg(Dr)));')
    print('print("E_degree="+string(deg(E)));')
    print('print("E_radical_degree="+string(deg(Er)));')
    print('print("common_radical_degree="+string(deg(bad)));')
    print('print("safe_distinct_branch_lower_bound="+string(deg(Dr)-deg(bad)));')
    print('print("branch_bound_end");')


if __name__ == "__main__":
    main()
