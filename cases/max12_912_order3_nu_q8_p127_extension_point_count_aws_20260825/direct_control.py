#!/usr/bin/env python3
"""Direct-enumeration controls for selected F_(127^2) fibres."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path

from flint import fq_default_ctx, fq_default_poly_ctx


P = 127
Q = P * P
CANDIDATE_SHA256 = "9061726295086f58f74f3751b2f7c2d59c5cb86de5e53ecd636687fd54daa7ce"
INDICES = (0, 39, 71, 128)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate", type=Path, required=True)
    args = parser.parse_args()
    got = sha256(args.candidate.read_bytes()).hexdigest()
    if got != CANDIDATE_SHA256:
        raise RuntimeError(("candidate hash", got))
    payload = json.loads(args.candidate.read_text())
    field = fq_default_ctx(P, 2, "a", fq_type="FQ_NMOD")
    ring = fq_default_poly_ctx(field)
    a = field.gen()
    v_variable = ring.gen()
    support = {
        int(v_degree): [(int(w_degree), coefficient % P) for w_degree, coefficient in entries]
        for v_degree, entries in payload["nonzero_support"].items()
    }
    field_elements = [field(i) + field(j) * a for j in range(P) for i in range(P)]
    if len(field_elements) != Q:
        raise RuntimeError("field enumeration")
    records = []
    for index in INDICES:
        w = field_elements[index]
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
        hv = h.derivative()
        hw = ring(hw_coefficients)
        rational_root_poly = h.gcd(v_variable.pow_mod(Q, h) - v_variable)
        singular_root_poly = rational_root_poly.gcd(hv).gcd(hw)
        gcd_counts = [
            rational_root_poly.degree(),
            rational_root_poly.degree() - singular_root_poly.degree(),
            singular_root_poly.degree(),
        ]
        direct_total = direct_smooth = direct_singular = 0
        for v in field_elements:
            if h(v) != field.zero():
                continue
            direct_total += 1
            if hv(v) == field.zero() and hw(v) == field.zero():
                direct_singular += 1
            else:
                direct_smooth += 1
        direct_counts = [direct_total, direct_smooth, direct_singular]
        if direct_counts != gcd_counts:
            raise RuntimeError(("control mismatch", index, direct_counts, gcd_counts))
        records.append(
            {
                "w_index": index,
                "w": str(w),
                "direct_counts_total_smooth_singular": direct_counts,
                "gcd_counts_total_smooth_singular": gcd_counts,
            }
        )
    print(
        json.dumps(
            {
                "status": "PASS",
                "prime": P,
                "extension_degree": 2,
                "field_order": Q,
                "field_modulus": str(field.modulus()),
                "candidate_sha256": got,
                "records": records,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()

