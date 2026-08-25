#!/usr/bin/env python3
"""Find small good primes with at least two rational corrected-Q8 roots."""

from __future__ import annotations

import argparse
import json
from math import isqrt


Q8 = [-24, -296, -1548, -4428, -7320, -6498, -1782, 1539, 999]


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def value(x: int, p: int) -> int:
    out = 0
    for coefficient in reversed(Q8):
        out = (out * x + coefficient) % p
    return out


def derivative_value(x: int, p: int) -> int:
    out = 0
    for degree in range(8, 0, -1):
        out = (out * x + degree * Q8[degree]) % p
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=5000)
    parser.add_argument("--minimum-roots", type=int, default=2)
    parser.add_argument("--maximum-hits", type=int, default=24)
    args = parser.parse_args()
    hits = []
    for p in range(2, args.limit + 1):
        if not is_prime(p) or Q8[-1] % p == 0:
            continue
        roots = [x for x in range(p) if value(x, p) == 0]
        if len(roots) < args.minimum_roots:
            continue
        squarefree_at_roots = all(derivative_value(x, p) != 0 for x in roots)
        if not squarefree_at_roots:
            continue
        hits.append({"prime": p, "roots": roots, "root_count": len(roots)})
        if len(hits) >= args.maximum_hits:
            break
    print(json.dumps({
        "case": "max12_912_order3_nu_q8_generic_fibre_grouping_aws_20260825",
        "limit": args.limit,
        "minimum_roots": args.minimum_roots,
        "hits": hits,
        "scope": "bounded exact rational-root scan; no full factorization or component claim",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

