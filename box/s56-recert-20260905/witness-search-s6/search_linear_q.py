#!/usr/bin/env python3
"""Search sparse Q for {Q,P}=nonzero*x^8 with the S6 outer bounds.

Work in z=y-x/3 and specialize h=z^3.  Then

    Q = z^6 + b2(x) z^2 + b1(x) z + b0(x),
    P = z^9 + sum_{j=0}^8 p_j(x) z^j.

For fixed Q the Jacobian constraints are linear in the coefficients of P.
This script performs exact-shape screens over a prime and prints only
consistent shapes whose x^8 z^0 coefficient is not forced to zero.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path


P_DEG = {j: 27 - 3 * j for j in range(9)}
TARGET = (8, 0)


def variables():
    out = []
    for zdeg in range(9):
        for xdeg in range(P_DEG[zdeg] + 1):
            out.append((xdeg, zdeg))
    return out


VARS = variables()
VID = {term: i for i, term in enumerate(VARS)}


def add(row, key, value, prime):
    value %= prime
    if not value:
        return
    row[key] = (row.get(key, 0) + value) % prime
    if not row[key]:
        del row[key]


def system(qterms, prime):
    """Return coefficient rows A*p=rhs and target affine functional."""
    coeffs = {}
    # Unknown P terms.
    for (qa, qr), qc in qterms.items():
        for pa, ps in VARS:
            fac = qc * (qa * ps - qr * pa)
            if fac:
                key = (qa + pa - 1, qr + ps - 1)
                if key[0] >= 0 and key[1] >= 0:
                    row, const = coeffs.setdefault(key, ({}, 0))
                    add(row, VID[(pa, ps)], fac, prime)
    # Fixed monic P term z^9.
    for (qa, qr), qc in qterms.items():
        fac = qc * qa * 9
        if fac:
            key = (qa - 1, qr + 8)
            row, const = coeffs.setdefault(key, ({}, 0))
            coeffs[key] = (row, (const + fac) % prime)

    target_row, target_const = coeffs.pop(TARGET, ({}, 0))
    rows = []
    for key, (row, const) in coeffs.items():
        if row or const:
            rr = dict(row)
            rr[-1] = (-const) % prime  # augmented RHS
            rows.append((key, rr))
    return rows, (target_row, target_const % prime)


def echelon(rows, prime):
    """Sparse reduced echelon dictionary pivot -> augmented row."""
    pivots = {}
    inconsistent = False
    for _key, original in rows:
        row = dict(original)
        while True:
            cols = [c for c, v in row.items() if c >= 0 and v % prime]
            if not cols:
                if row.get(-1, 0) % prime:
                    inconsistent = True
                break
            pivot = min(cols)
            if pivot not in pivots:
                inv = pow(row[pivot] % prime, -1, prime)
                for c in list(row):
                    row[c] = row[c] * inv % prime
                    if not row[c]:
                        del row[c]
                # Reduce the new pivot from all old rows for RREF.
                for op, old in list(pivots.items()):
                    fac = old.get(pivot, 0) % prime
                    if fac:
                        for c, v in row.items():
                            old[c] = (old.get(c, 0) - fac * v) % prime
                            if not old[c]:
                                old.pop(c, None)
                pivots[pivot] = row
                break
            base = pivots[pivot]
            fac = row[pivot] % prime
            for c, v in base.items():
                row[c] = (row.get(c, 0) - fac * v) % prime
                if not row[c]:
                    row.pop(c, None)
        if inconsistent:
            break
    return pivots, inconsistent


def reduce_functional(functional, pivots, prime):
    row, const = functional
    f = dict(row)
    f[-1] = const % prime
    for pivot in sorted(pivots):
        fac = f.get(pivot, 0) % prime
        if fac:
            base = pivots[pivot]
            # A pivot row says p_pivot + sum a_i p_i = rhs.  Substitute.
            f.pop(pivot, None)
            for c, v in base.items():
                if c == pivot:
                    continue
                if c == -1:
                    f[-1] = (f.get(-1, 0) + fac * v) % prime
                else:
                    f[c] = (f.get(c, 0) - fac * v) % prime
                    if not f[c]:
                        f.pop(c, None)
    free = {c: v for c, v in f.items() if c >= 0 and v % prime}
    return f.get(-1, 0) % prime, free


def q_from_shape(shape, coeffs):
    q = {(0, 6): 1}
    for zdeg, xdeg, coeff in zip((2, 1, 0), shape, coeffs):
        if xdeg is not None and coeff:
            q[(xdeg, zdeg)] = coeff
    return q


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prime", type=int, default=32003)
    ap.add_argument("--mode", choices=("monomial", "binomial"), default="monomial")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--out", type=Path)
    args = ap.parse_args()
    bounds = {2: 12, 1: 15, 0: 18}
    hits = []
    seen = 0
    if args.mode == "monomial":
        # None permits an absent coefficient.  Coefficients are normalized to 1
        # for the first broad exponent screen.
        shapes = itertools.product(
            [None] + list(range(bounds[2] + 1)),
            [None] + list(range(bounds[1] + 1)),
            [None] + list(range(bounds[0] + 1)),
        )
        for shape in shapes:
            if shape == (None, None, None):
                continue
            seen += 1
            q = q_from_shape(shape, (1, 1, 1))
            rows, target = system(q, args.prime)
            pivots, bad = echelon(rows, args.prime)
            if not bad:
                const, free = reduce_functional(target, pivots, args.prime)
                if const or free:
                    hit = {"shape": shape, "target_const": const,
                           "target_free": len(free), "rank": len(pivots)}
                    hits.append(hit)
                    print(json.dumps(hit), flush=True)
            if args.limit and seen >= args.limit:
                break
    payload = {"prime": args.prime, "mode": args.mode, "seen": seen,
               "hits": hits, "variables": len(VARS)}
    if args.out:
        args.out.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({k: payload[k] for k in ("prime", "mode", "seen", "variables")}
                     | {"hit_count": len(hits)}))


if __name__ == "__main__":
    main()
