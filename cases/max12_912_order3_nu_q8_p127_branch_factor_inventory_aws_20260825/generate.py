#!/usr/bin/env python3
"""Emit exact Singular input factoring rad Res_v(H,H_v) over F_127."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "cases/max12_912_order3_nu_q8_p127_candidate_genus_aws_20260825/generate_v2.py"
BASE_SHA256 = "788f83910cfd7878d0eb63a280ba569e9e41d947afd49114145d9b13fc42102f"
CANDIDATE_SHA256 = "9061726295086f58f74f3751b2f7c2d59c5cb86de5e53ecd636687fd54daa7ce"


def load_base():
    got = sha256(BASE.read_bytes()).hexdigest()
    if got != BASE_SHA256:
        raise RuntimeError((str(BASE), got, BASE_SHA256))
    spec = importlib.util.spec_from_file_location("q8_branch_factor_base", BASE)
    if spec is None or spec.loader is None:
        raise RuntimeError(BASE)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate", type=Path, required=True)
    args = parser.parse_args()
    got = sha256(args.candidate.read_bytes()).hexdigest()
    if got != CANDIDATE_SHA256:
        raise RuntimeError((str(args.candidate), got, CANDIDATE_SHA256))
    payload = json.loads(args.candidate.read_text())
    if payload.get("status") != "PASS" or payload.get("degree_v") != 190:
        raise RuntimeError("candidate endpoint")
    base = load_base()
    print("ring R=127,(v,w),lp;")
    print(f"poly H={base.polynomial(payload)};")
    print("poly Hv=diff(H,v);")
    print("poly D=resultant(H,Hv,v);")
    print("poly Dr=D/gcd(D,diff(D,w));")
    print("ring U=127,(w),lp;")
    print("poly Dr=imap(R,Dr);")
    print("list F=factorize(Dr,1);")
    print('print("Q8-P127-DISCRIMINANT-FACTOR-INVENTORY");')
    print('print("radical_degree="+string(deg(Dr)));')
    print('print("factor_count="+string(size(F[1])));')
    print("int i; int degree_sum=0;")
    print('print("factors_begin");')
    print("for(i=1;i<=size(F[1]);i++)")
    print("{")
    print('  print("factor_index="+string(i));')
    print('  print("factor_degree="+string(deg(F[1][i])));')
    print("  F[1][i];")
    print("  degree_sum=degree_sum+deg(F[1][i]);")
    print("}")
    print('print("factors_end");')
    print('print("factor_degree_sum="+string(degree_sum));')
    print('print("factor_inventory_end");')


if __name__ == "__main__":
    main()
