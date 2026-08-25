#!/usr/bin/env python3
"""Generate exact Singular checks for the candidate plane curve."""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CANDIDATE = ROOT / "cases/max12_912_order3_nu_q8_p127_generic_candidate_certificate_aws_20260825/interpolation_candidate.json"
CANDIDATE_SHA256 = "9061726295086f58f74f3751b2f7c2d59c5cb86de5e53ecd636687fd54daa7ce"


def specialized(payload: dict, w_value: int) -> str:
    terms = []
    for raw_v_degree, entries in payload["nonzero_support"].items():
        v_degree = int(raw_v_degree)
        coefficient = sum(c * pow(w_value, e, 127) for e, c in entries) % 127
        if not coefficient:
            continue
        factors = []
        if coefficient != 1 or v_degree == 0:
            factors.append(str(coefficient))
        if v_degree:
            factors.append("v" if v_degree == 1 else f"v^{v_degree}")
        terms.append("*".join(factors))
    return "+".join(terms) if terms else "0"


def main() -> None:
    got = sha256(CANDIDATE.read_bytes()).hexdigest()
    if got != CANDIDATE_SHA256:
        raise RuntimeError((got, CANDIDATE_SHA256))
    payload = json.loads(CANDIDATE.read_text())
    if (
        payload["status"] != "PASS"
        or payload["prime"] != 127
        or payload["degree_v"] != 190
        or payload["nonzero_support"]["190"] != [[0, 1]]
    ):
        raise RuntimeError("candidate endpoint")
    print("ring R=127,(v),dp;")
    for value in (25, 47, 71):
        print(f"poly H{value}={specialized(payload, value)};")
    print("list F25=factorize(H25,1);")
    print("list F47=factorize(H47,1);")
    print("ideal I25=F25[1];")
    print("ideal I47=F47[1];")
    print('print("Q8-P127-CANDIDATE-PLANE-INTEGRALITY");')
    print('print("degree_H25="+string(deg(H25)));')
    print('print("degree_H47="+string(deg(H47)));')
    print('print("factor_count_25="+string(size(I25)));')
    print('print("factor_count_47="+string(size(I47)));')
    print('print("factor_degrees_25_begin");')
    print("int i; for(i=1;i<=size(I25);i++){print(deg(I25[i]));}")
    print('print("factor_degrees_25_end");')
    print('print("factor_degrees_47_begin");')
    print("for(i=1;i<=size(I47);i++){print(deg(I47[i]));}")
    print('print("factor_degrees_47_end");')
    print('print("squarefree_gcd_degree_25="+string(deg(gcd(H25,diff(H25,v)))));')
    print('print("squarefree_gcd_degree_47="+string(deg(gcd(H47,diff(H47,v)))));')
    print('print("H_71_50="+string(subst(H71,v,50)));')
    print('print("Hv_71_50="+string(subst(diff(H71,v),v,50)));')


if __name__ == "__main__":
    main()

