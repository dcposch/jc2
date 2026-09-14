#!/usr/bin/env python3
"""Search a natural five-term slice Q=h^2+B with sparse h and B.

The legal specialization is

    h = z^3 + x^eu z + x^ev,
    B = C x^eb z^rb,

with source-complete support bounds.  For each fixed Q, the complete bounded
P-space is solved linearly.  Negative output is search evidence only.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("reduced_centered", HERE / "reduced_centered.py")
RC = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(RC)


def add(poly, exponent, coefficient, prime):
    poly[exponent] = (poly.get(exponent, 0) + coefficient) % prime
    if not poly[exponent]:
        del poly[exponent]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prime", type=int, default=32003)
    ap.add_argument("--coeff-min", type=int, default=-12)
    ap.add_argument("--coeff-max", type=int, default=12)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    p = args.prime
    coefficients = [c % p for c in range(args.coeff_min, args.coeff_max + 1) if c]
    hits = []
    seen = 0
    for eu in range(7):
        for ev in range(10):
            for rb, bound in ((2, 12), (1, 15), (0, 18)):
                for eb in range(bound + 1):
                    if rb == 0 and eb == 0:
                        continue  # gauged constant; it has zero bracket anyway
                    for coefficient in coefficients:
                        # Square h=z^3+x^eu*z+x^ev and add B.
                        q = {6: {0: 1}, 4: {eu: 2 % p}, 3: {ev: 2 % p},
                             2: {2 * eu: 1}, 1: {eu + ev: 2 % p},
                             0: {2 * ev: 1}}
                        add(q.setdefault(rb, {}), eb, coefficient, p)
                        rows, target, _ = RC.reduce_q(q, p)
                        ok, reduced_target, assignment = RC.solve(rows, target, p, True)
                        seen += 1
                        if ok and any(reduced_target):
                            hit = {
                                "eu": eu,
                                "ev": ev,
                                "B_term": [rb, eb, coefficient],
                                "target_reduced": reduced_target,
                                "integration_constants": assignment,
                            }
                            hits.append(hit)
                            print(json.dumps(hit), flush=True)
    payload = {
        "prime": p,
        "coefficient_residues": coefficients,
        "seen": seen,
        "hit_count": len(hits),
        "hits": hits,
    }
    args.out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({key: payload[key] for key in ("prime", "seen", "hit_count")}))


if __name__ == "__main__":
    main()
