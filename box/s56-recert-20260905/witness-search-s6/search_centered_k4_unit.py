#!/usr/bin/env python3
"""Screen every target-capable four-term centered Q support at unit coefficients.

This is a witness-finding specialization only.  It uses the exact fixed-Q
recurrence in ``reduced_centered.py`` and never treats a negative screen as a
certificate for the full chart.
"""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("reduced_centered", HERE / "reduced_centered.py")
RC = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(RC)


def target_capable(terms):
    """Necessary support-semigroup condition for the x^8 z^0 bracket."""
    reachable = {(0, 0)}
    for _ in range(5):
        reachable |= {
            (deficit + 6 - r, xdegree + e)
            for deficit, xdegree in tuple(reachable)
            for r, e in terms
            if deficit + 6 - r <= 9 and xdegree + e <= 9
        }
    return any(
        r in (0, 1)
        and e <= 9
        and any(xdegree == 9 - e and deficit <= 8 + r
                for deficit, xdegree in reachable)
        for r, e in terms
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prime", type=int, default=32003)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    p = args.prime
    generators = [(r, e) for r in range(5) for e in range(3 * (6 - r) + 1)]
    hits = []
    supports = seen = 0
    for terms in itertools.combinations(generators, 4):
        if not target_capable(terms):
            continue
        supports += 1
        q = {6: {0: 1}}
        for r, e in terms:
            q.setdefault(r, {})[e] = 1
        rows, target, _ = RC.reduce_q(q, p)
        ok, reduced_target, assignment = RC.solve(rows, target, p, True)
        seen += 1
        if ok and any(reduced_target):
            hit = {
                "terms": terms,
                "target_reduced": reduced_target,
                "integration_constants": assignment,
            }
            hits.append(hit)
            print(json.dumps(hit), flush=True)
    payload = {
        "prime": p,
        "coefficient": 1,
        "target_capable_supports": supports,
        "seen": seen,
        "hit_count": len(hits),
        "hits": hits,
    }
    args.out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({key: payload[key] for key in
                      ("prime", "target_capable_supports", "seen", "hit_count")}))


if __name__ == "__main__":
    main()
