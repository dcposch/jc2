#!/usr/bin/env python3
"""Exhaust finite-field coefficient orbits for one/two-term centered Q."""

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
    reachable = {(0, 0)}
    for _ in range(5):
        reachable |= {
            (deficit + 6 - r, xdegree + e)
            for deficit, xdegree in tuple(reachable)
            for r, e in terms
            if deficit + 6 - r <= 9 and xdegree + e <= 9
        }
    return any(
        r in (0, 1) and e <= 9
        and any(xdegree == 9 - e and deficit <= 8 + r
                for deficit, xdegree in reachable)
        for r, e in terms
    )


def primitive_root(prime):
    order = prime - 1
    factors = [q for q in range(2, order + 1)
               if order % q == 0 and all(q % d for d in range(2, int(q ** .5) + 1))]
    for generator in range(2, prime):
        if all(pow(generator, order // q, prime) != 1 for q in factors):
            return generator
    raise AssertionError("no primitive root")


def orbit_representatives(terms, prime):
    order = prime - 1
    wx = tuple(e for r, e in terms)
    wy = tuple(r - 6 for r, e in terms)
    subgroup = {
        tuple((u * wx[i] + v * wy[i]) % order for i in range(len(terms)))
        for u in range(order) for v in range(order)
    }
    unseen = set(itertools.product(range(order), repeat=len(terms)))
    representatives = []
    while unseen:
        representative = min(unseen)
        representatives.append(representative)
        unseen.difference_update(
            tuple((representative[i] + shift[i]) % order for i in range(len(terms)))
            for shift in subgroup
        )
    return representatives


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-k", type=int, choices=(1, 2), required=True)
    ap.add_argument("--prime", type=int, default=29)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    p = args.prime
    generator = primitive_root(p)
    monomials = [(r, e) for r in range(5) for e in range(3 * (6 - r) + 1)]
    hits = []
    supports = orbits = 0
    for terms in itertools.combinations(monomials, args.k):
        if not target_capable(terms):
            continue
        supports += 1
        for logs in orbit_representatives(terms, p):
            coefficients = [pow(generator, exponent, p) for exponent in logs]
            q = {6: {0: 1}}
            for (r, e), coefficient in zip(terms, coefficients):
                q.setdefault(r, {})[e] = coefficient
            rows, target, _ = RC.reduce_q(q, p)
            ok, reduced_target, assignment = RC.solve(rows, target, p, True)
            orbits += 1
            if ok and any(reduced_target):
                hit = {
                    "terms": terms,
                    "coefficient_logs": logs,
                    "coefficients": coefficients,
                    "target_reduced": reduced_target,
                    "integration_constants": assignment,
                }
                hits.append(hit)
                print(json.dumps(hit), flush=True)
    payload = {
        "prime": p,
        "primitive_root": generator,
        "k": args.k,
        "target_capable_supports": supports,
        "orbits_seen": orbits,
        "hit_count": len(hits),
        "hits": hits,
    }
    args.out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({key: payload[key] for key in
                      ("prime", "k", "target_capable_supports", "orbits_seen", "hit_count")}))


if __name__ == "__main__":
    main()
