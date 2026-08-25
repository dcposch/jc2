#!/usr/bin/env python3
"""Generate an exact generic DRL reduction of the interpolated H(w,v)."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
GENERIC = ROOT / "cases/max12_912_order3_nu_q8_generic_fibre_grouping_aws_20260825/generate.py"
GENERIC_SHA256 = "6b752b03d777c73de5d9ff729f30d01f5d81229d0ee467e9ad98a349d6234daf"
CANDIDATE = Path(__file__).resolve().parent / "interpolation_candidate.json"
CANDIDATE_SHA256 = "9061726295086f58f74f3751b2f7c2d59c5cb86de5e53ecd636687fd54daa7ce"


def load_generic():
    assert sha256(GENERIC.read_bytes()).hexdigest() == GENERIC_SHA256
    spec = importlib.util.spec_from_file_location("q8_candidate_generic", GENERIC)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def candidate_source() -> str:
    assert sha256(CANDIDATE.read_bytes()).hexdigest() == CANDIDATE_SHA256
    payload = json.loads(CANDIDATE.read_text())
    assert payload["status"] == "PASS"
    assert payload["prime"] == 127
    assert payload["degree_v"] == 190
    assert payload["maximum_support_count"] == 21
    assert payload["degree_drop_values"] == [39, 56, 125]
    assert payload["partition_w25"] == [2, 188]
    assert payload["partition_w47"] == [1, 3, 186]
    assert payload["proper_subset_sum_intersection"] == []
    support = payload["nonzero_support"]
    assert sorted(map(int, support)) == list(range(191))
    terms = []
    for raw_v_degree, entries in support.items():
        v_degree = int(raw_v_degree)
        for w_degree, coefficient in entries:
            assert 0 <= w_degree <= 21
            assert 0 < coefficient < 127
            factors = []
            if coefficient != 1 or (w_degree == 0 and v_degree == 0):
                factors.append(str(coefficient))
            if w_degree:
                factors.append("w" if w_degree == 1 else f"w^{w_degree}")
            if v_degree:
                factors.append("v" if v_degree == 1 else f"v^{v_degree}")
            terms.append("*".join(factors) if factors else "1")
    assert support["190"] == [[0, 1]]
    return "+".join(terms)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--engine", choices=("std", "slimgb"), required=True)
    args = parser.parse_args()
    generic = load_generic()
    source = generic.source(127, args.engine, False)
    old_ring = "ring R=(127,w),(c,d2,d4,x1,x3,x5,inv,v),(dp(7),dp(1));"
    new_ring = "ring R=(127,w),(c,d2,d4,x1,x3,x5,inv,v),dp;"
    assert source.count(old_ring) == 1
    source = source.replace(old_ring, new_ring)
    marker = f"ideal G={args.engine}(I);"
    assert source.count(marker) == 1
    prefix = source.split(marker, 1)[0]
    print(prefix, end="")
    print(marker)
    print('print("Q8-P127-GENERIC-CANDIDATE-CERTIFICATE");')
    print(f'print("engine={args.engine}");')
    print('print("generic_dim="+string(dim(G)));')
    print('print("generic_size="+string(size(G)));')
    print('print("generic_vdim="+string(vdim(G)));')
    print(f"poly H={candidate_source()};")
    print('print("candidate_v_degree="+string(deg(H)));')
    print('print("candidate_monic="+string(leadcoef(H)));')
    print("poly candidate_remainder=reduce(H,G);")
    print('print("candidate_remainder="+string(candidate_remainder));')
    print('print("leading_ideal_begin");')
    print("lead(G);")
    print('print("leading_ideal_end");')


if __name__ == "__main__":
    main()

