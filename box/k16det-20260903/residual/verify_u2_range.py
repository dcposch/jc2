#!/usr/bin/env python3
"""Bounded exact sign/norm audit for the u2 coefficient-pair recurrence."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction

from u2_pair_recurrence import solve


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("lo", type=int, nargs="?", default=3)
    ap.add_argument("hi", type=int, nargs="?", default=20)
    args = ap.parse_args()
    if args.lo < 3 or args.hi < args.lo:
        raise SystemExit("require 3 <= lo <= hi")

    rows = []
    for t in range(args.lo, args.hi + 1):
        result = solve(t)
        pair = result["lambda_pair_b_plus_a_d"]
        b = Fraction(pair["b"])
        a = Fraction(pair["a"])
        norm = Fraction(result["norm3"])
        direct_norm = 3 * b * b - (t + 1) * a * a
        checks = result["checks"]
        assert direct_norm == norm
        assert norm > 0
        assert (b > 0) == (t % 2 == 0)
        assert (a > 0) == (t % 2 == 1)
        assert all(checks.values())
        rows.append({
            "t": t,
            "sign_a": 1 if a > 0 else -1,
            "sign_b": 1 if b > 0 else -1,
            "norm_positive": True,
            "pivot_and_rho_checks": True,
        })
    print(json.dumps({"range": [args.lo, args.hi], "rows": rows}, indent=2))


if __name__ == "__main__":
    main()
