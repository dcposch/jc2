#!/usr/bin/env python3
"""Exact smooth-affine F_(127^2) point count, sharded by w."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path

from flint import fq_default_ctx, fq_default_poly_ctx


P = 127
EXTENSION_DEGREE = 2
Q = P**EXTENSION_DEGREE
CANDIDATE_SHA256 = "9061726295086f58f74f3751b2f7c2d59c5cb86de5e53ecd636687fd54daa7ce"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--start", type=int, required=True)
    parser.add_argument("--stop", type=int, required=True)
    args = parser.parse_args()
    if not 0 <= args.start < args.stop <= Q:
        raise RuntimeError((args.start, args.stop, Q))
    got = digest(args.candidate)
    if got != CANDIDATE_SHA256:
        raise RuntimeError(("candidate hash", got))
    payload = json.loads(args.candidate.read_text())
    if (
        payload.get("status") != "PASS"
        or payload.get("prime") != P
        or payload.get("degree_v") != 190
        or payload["nonzero_support"].get("190") != [[0, 1]]
    ):
        raise RuntimeError("candidate endpoint mismatch")

    field = fq_default_ctx(P, EXTENSION_DEGREE, "a", fq_type="FQ_NMOD")
    ring = fq_default_poly_ctx(field)
    v = ring.gen()
    a = field.gen()
    support = {
        int(v_degree): [(int(w_degree), coefficient % P) for w_degree, coefficient in entries]
        for v_degree, entries in payload["nonzero_support"].items()
    }

    total = 0
    smooth = 0
    singular = 0
    per_w: list[list[int]] = []
    for index in range(args.start, args.stop):
        w = field(index % P) + field(index // P) * a
        w_powers = [field.one()]
        for _ in range(21):
            w_powers.append(w_powers[-1] * w)
        h_coefficients = [field.zero() for _ in range(191)]
        hw_coefficients = [field.zero() for _ in range(191)]
        for v_degree, entries in support.items():
            for w_degree, coefficient in entries:
                h_coefficients[v_degree] += coefficient * w_powers[w_degree]
                if w_degree:
                    hw_coefficients[v_degree] += (
                        coefficient * w_degree % P
                    ) * w_powers[w_degree - 1]
        h = ring(h_coefficients)
        if h.degree() != 190 or h[190] != field.one():
            raise RuntimeError(("monicity", index, h.degree(), h[190]))
        hv = h.derivative()
        hw = ring(hw_coefficients)
        rational_roots = h.gcd(v.pow_mod(Q, h) - v)
        singular_roots = rational_roots.gcd(hv).gcd(hw)
        fibre_total = rational_roots.degree()
        fibre_singular = singular_roots.degree()
        fibre_smooth = fibre_total - fibre_singular
        if min(fibre_total, fibre_singular, fibre_smooth) < 0:
            raise RuntimeError(("negative count", index))
        total += fibre_total
        singular += fibre_singular
        smooth += fibre_smooth
        per_w.append([index, fibre_total, fibre_smooth, fibre_singular])

    result = {
        "status": "PASS",
        "prime": P,
        "extension_degree": EXTENSION_DEGREE,
        "field_order": Q,
        "field_modulus": str(field.modulus()),
        "candidate_sha256": got,
        "start": args.start,
        "stop": args.stop,
        "w_count": args.stop - args.start,
        "rational_affine_point_count": total,
        "smooth_rational_affine_point_count": smooth,
        "singular_rational_affine_point_count": singular,
        "per_w": per_w,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

