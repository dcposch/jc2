#!/usr/bin/env python3
"""Checkpoint exact canonical post-H/c rows without running affine substitution."""

from __future__ import annotations

import argparse
import json
import time

import canonical_extract as ce


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("t", type=int, nargs="+")
    parser.add_argument("--max-seconds", type=float, default=3600.0)
    parser.add_argument("--max-expression-bytes", type=int, default=1_000_000_000)
    args = parser.parse_args()
    for name, expected in ce.EXPECTED.items():
        actual = ce.digest(ce.INPUT/name)
        if actual != expected:
            raise RuntimeError(f"frozen source mismatch: {name}: {actual}")
    chart = ce.load(ce.CHART, "canonical_post_chart")
    tp = ce.load(ce.PREPROCESS, "canonical_post_preprocess")
    for t in args.t:
        started = time.monotonic()
        data = chart.build(t=t, gauged=True)
        print(json.dumps({"t": t, "phase": "chart", "rows": len(data["tagged"]),
                          "seconds": time.monotonic()-started}), flush=True)
        first = tp.reduce_chart(data, max_pivots=1024,
                                max_seconds=args.max_seconds,
                                max_expression_bytes=args.max_expression_bytes)
        print(json.dumps({"t": t, "phase": "first_spine",
                          "pivots": len(first.pivots), "rows": len(first.rows),
                          "seconds": time.monotonic()-started}), flush=True)
        rows, auxiliary, algebra, normal = ce.normalize_post_hc(tp, first, t)
        records = [ce.row_record(row, auxiliary, algebra.y)
                   for row in sorted(rows, key=ce.normalization_row_key)]
        path = ce.OUT/f"canonical_t{t}_post_hc_rows.tsv"
        ce.write_tsv(path,
                     ["source", "band", "monomial", "degree_in_auxiliaries",
                      "terms_over_Qy", "expression"], records)
        expected_tags = []
        for k in range(0, 2*t):
            expected_tags.extend([[k, [0, 0]], [k, [0, 1]], [k, [0, 2]],
                                  [k, [1, 2]]])
            if k < t:
                expected_tags.append([k, [1, 1]])
        expected_tags.extend([[2*t, [0, 0]], [2*t, [0, 1]]])
        measured_tags = sorted([[r.h_power, list(r.monomial)] for r in rows])
        audit = {
            "typing": "EXACT fixed-t post-H/c rows from frozen charged drivers",
            "t": t,
            "source_hashes": {name: ce.digest(ce.INPUT/name) for name in ce.EXPECTED},
            "full": {"rows": len(data["tagged"]),
                     "unknowns_including_c": len(data["params"])+1},
            "first_spine": {"pivots": len(first.pivots), "rows": len(first.rows),
                            "unknowns_including_c": len(first.remaining_variables)+1,
                            "pivot_bands": [p.h_power for p in first.pivots]},
            "normalization": normal,
            "post_Hc": {"rows": len(rows), "auxiliaries": len(auxiliary),
                        "variables": list(map(str, auxiliary)),
                        "tags": measured_tags,
                        "expected_tags": sorted(expected_tags),
                        "tag_pattern_checked": measured_tags == sorted(expected_tags),
                        "vector_sha256": ce.vector_digest(r.expr for r in rows)},
            "artifact": {"path": path.name, "sha256": ce.digest(path),
                         "bytes": path.stat().st_size},
            "elapsed_seconds": time.monotonic()-started,
        }
        audit_path = ce.OUT/f"canonical_t{t}_post_hc_audit.json"
        audit_path.write_text(json.dumps(audit, indent=2, sort_keys=True)+"\n",
                              encoding="utf-8")
        print(json.dumps({"t": t, "phase": "done", "rows": len(rows),
                          "auxiliaries": len(auxiliary),
                          "tag_pattern_checked": audit["post_Hc"]["tag_pattern_checked"],
                          "tsv": str(path), "audit": str(audit_path),
                          "seconds": audit["elapsed_seconds"]}, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
