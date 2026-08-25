#!/usr/bin/env python3
"""Exact F_127 affine point/gradient count for the candidate H(w,v)."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path


P = 127
CANDIDATE_SHA256 = "9061726295086f58f74f3751b2f7c2d59c5cb86de5e53ecd636687fd54daa7ce"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def evaluate(coefficients: list[int], value: int) -> int:
    result = 0
    for coefficient in reversed(coefficients):
        result = (result * value + coefficient) % P
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate", type=Path, required=True)
    args = parser.parse_args()
    got = digest(args.candidate)
    if got != CANDIDATE_SHA256:
        raise RuntimeError((got, CANDIDATE_SHA256))
    payload = json.loads(args.candidate.read_text())
    if (
        payload.get("status") != "PASS"
        or payload.get("prime") != P
        or payload.get("degree_v") != 190
        or payload["nonzero_support"].get("190") != [[0, 1]]
    ):
        raise RuntimeError("candidate endpoint mismatch")

    support: list[list[tuple[int, int]]] = []
    for v_degree in range(191):
        entries = [tuple(item) for item in payload["nonzero_support"][str(v_degree)]]
        support.append(entries)

    rational_points: list[list[int]] = []
    smooth_points: list[list[int]] = []
    singular_points: list[list[int]] = []
    counts_by_w: list[int] = []
    smooth_counts_by_w: list[int] = []
    for w_value in range(P):
        w_powers = [1]
        for _ in range(21):
            w_powers.append(w_powers[-1] * w_value % P)
        coefficients = [0] * 191
        w_derivative_coefficients = [0] * 191
        for v_degree, entries in enumerate(support):
            for w_degree, coefficient in entries:
                coefficients[v_degree] = (
                    coefficients[v_degree] + coefficient * w_powers[w_degree]
                ) % P
                if w_degree:
                    w_derivative_coefficients[v_degree] = (
                        w_derivative_coefficients[v_degree]
                        + w_degree * coefficient * w_powers[w_degree - 1]
                    ) % P
        v_derivative_coefficients = [
            (degree * coefficients[degree]) % P for degree in range(1, 191)
        ]
        fibre_count = 0
        fibre_smooth_count = 0
        for v_value in range(P):
            if evaluate(coefficients, v_value) != 0:
                continue
            point = [w_value, v_value]
            rational_points.append(point)
            fibre_count += 1
            hw = evaluate(w_derivative_coefficients, v_value)
            hv = evaluate(v_derivative_coefficients, v_value)
            if hw or hv:
                smooth_points.append(point)
                fibre_smooth_count += 1
            else:
                singular_points.append(point)
        counts_by_w.append(fibre_count)
        smooth_counts_by_w.append(fibre_smooth_count)

    if [71, 50] not in smooth_points:
        raise RuntimeError("frozen smooth rational control (71,50) absent")
    result = {
        "case": "max12_912_order3_nu_q8_p127_candidate_point_count_aws_20260825",
        "status": "PASS",
        "prime": P,
        "candidate_sha256": got,
        "affine_pair_count": P * P,
        "rational_affine_point_count": len(rational_points),
        "smooth_rational_affine_point_count": len(smooth_points),
        "singular_rational_affine_point_count": len(singular_points),
        "p1_rational_point_count": P + 1,
        "smooth_count_exceeds_p1": len(smooth_points) > P + 1,
        "rational_points": rational_points,
        "smooth_points": smooth_points,
        "singular_points": singular_points,
        "counts_by_w": counts_by_w,
        "smooth_counts_by_w": smooth_counts_by_w,
        "scope": (
            "exact affine point/gradient count for candidate H over F_127 only; "
            "positive-genus inference additionally requires geometric integrality"
        ),
    }
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    print(encoded, end="")


if __name__ == "__main__":
    main()
