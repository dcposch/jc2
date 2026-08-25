#!/usr/bin/env python3
"""Fail-closed aggregate of a full partition of F_(127^2) w-values."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


P = 127
Q = P * P
CANDIDATE_SHA256 = "9061726295086f58f74f3751b2f7c2d59c5cb86de5e53ecd636687fd54daa7ce"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("results", nargs="+", type=Path)
    args = parser.parse_args()
    records = [json.loads(path.read_text()) for path in args.results]
    records.sort(key=lambda item: item["start"])
    cursor = 0
    field_modulus = None
    all_per_w: list[list[int]] = []
    for record in records:
        if (
            record.get("status") != "PASS"
            or record.get("prime") != P
            or record.get("extension_degree") != 2
            or record.get("field_order") != Q
            or record.get("candidate_sha256") != CANDIDATE_SHA256
            or record.get("start") != cursor
            or record.get("stop") - record.get("start") != record.get("w_count")
            or len(record.get("per_w", [])) != record.get("w_count")
        ):
            raise RuntimeError(("bad shard", record.get("start")))
        if field_modulus is None:
            field_modulus = record["field_modulus"]
        elif record["field_modulus"] != field_modulus:
            raise RuntimeError("field modulus mismatch")
        expected_indices = list(range(record["start"], record["stop"]))
        if [row[0] for row in record["per_w"]] != expected_indices:
            raise RuntimeError(("per-w partition", record["start"]))
        shard_total = sum(row[1] for row in record["per_w"])
        shard_smooth = sum(row[2] for row in record["per_w"])
        shard_singular = sum(row[3] for row in record["per_w"])
        if (
            shard_total != record.get("rational_affine_point_count")
            or shard_smooth != record.get("smooth_rational_affine_point_count")
            or shard_singular != record.get("singular_rational_affine_point_count")
            or shard_total != shard_smooth + shard_singular
        ):
            raise RuntimeError(("shard sums", record["start"]))
        all_per_w.extend(record["per_w"])
        cursor = record["stop"]
    if cursor != Q or len(all_per_w) != Q:
        raise RuntimeError(("incomplete partition", cursor, len(all_per_w)))
    total = sum(row[1] for row in all_per_w)
    smooth = sum(row[2] for row in all_per_w)
    singular = sum(row[3] for row in all_per_w)
    if total != smooth + singular:
        raise RuntimeError((total, smooth, singular))
    output = {
        "status": "PASS",
        "prime": P,
        "extension_degree": 2,
        "field_order": Q,
        "field_modulus": field_modulus,
        "candidate_sha256": CANDIDATE_SHA256,
        "shard_count": len(records),
        "w_count": len(all_per_w),
        "rational_affine_point_count": total,
        "smooth_rational_affine_point_count": smooth,
        "singular_rational_affine_point_count": singular,
        "p1_rational_point_count": Q + 1,
        "smooth_count_exceeds_p1": smooth > Q + 1,
        "genus_positive_if_geometrically_integral": smooth > Q + 1,
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    if not output["genus_positive_if_geometrically_integral"]:
        raise SystemExit(92)


if __name__ == "__main__":
    main()
