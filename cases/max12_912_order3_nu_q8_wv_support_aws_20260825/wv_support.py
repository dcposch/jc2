#!/usr/bin/env python3
"""Targeted exact modular support search for Q8 boundary coordinate v."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
WORKER = ROOT / "cases/max12_912_order3_nu_q8_invariant_support_20260824/modular_support.py"
WORKER_SHA256 = "c36d6cf1ca538a39923412075fb44be77ed30023107f4eac755722b7d796dea0"


def load_worker():
    got = sha256(WORKER.read_bytes()).hexdigest()
    if got != WORKER_SHA256:
        raise RuntimeError((str(WORKER), got, WORKER_SHA256))
    spec = importlib.util.spec_from_file_location("q8_wv_support_parent", WORKER)
    if spec is None or spec.loader is None:
        raise RuntimeError(WORKER)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, required=True)
    parser.add_argument("--root", type=int, required=True)
    parser.add_argument("--order", type=int, default=192)
    parser.add_argument("--max-left", type=int, default=24)
    parser.add_argument("--max-right", type=int, default=16)
    parser.add_argument("--max-columns", type=int, default=176)
    parser.add_argument("--holdout", type=int, default=16)
    args = parser.parse_args()
    if args.holdout < 1 or args.order <= args.holdout:
        raise RuntimeError("invalid order/holdout")
    W = load_worker()
    if not W.is_prime(args.prime):
        raise RuntimeError(("modulus is not prime", args.prime))
    data = W.lift_branch(args.prime, args.root, args.order)
    x3 = data["coordinates"]["x3"]
    x5 = data["coordinates"]["x5"]
    numerator = W.series_add(x3, W.series_scale(-2, x5, args.prime), args.prime)
    v = W.series_mul(numerator, W.series_inv(x5, args.prime), args.prime)
    if v[0] != args.root % args.prime:
        raise RuntimeError(("boundary-v mismatch", v[0], args.root, args.prime))
    searches = {}
    for left_name in ("w", "theta"):
        searches[f"{left_name},v"] = W.relation_search(
            data[left_name], v, args.prime,
            args.max_left, args.max_right, args.max_columns, args.holdout,
        )
    payload = {
        "case": "max12_912_order3_nu_q8_wv_support_aws_20260825",
        "prime": args.prime,
        "q8_root": args.root,
        "good_reduction": {
            "prime_by_trial_division": True,
            "Q8_at_root": W.q8_mod(args.root, args.prime),
            "six_by_six_jacobian_determinant": data["jacobian_determinant"],
            "x5_constant_nonzero": x5[0] != 0,
            "v_constant_matches_root": v[0] == args.root % args.prime,
        },
        "parameters": {
            "order": args.order,
            "holdout": args.holdout,
            "max_degrees": [args.max_left, args.max_right],
            "max_columns": args.max_columns,
        },
        "series_prefix": {
            "w": data["w"][:8],
            "theta": data["theta"][:8],
            "v": v[:8],
        },
        "relation_searches": searches,
        "scope": (
            "modular support learning at one corrected-Q8 specialization; "
            "hits require cross-prime agreement, characteristic-zero lifting, "
            "and exact substitution"
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

