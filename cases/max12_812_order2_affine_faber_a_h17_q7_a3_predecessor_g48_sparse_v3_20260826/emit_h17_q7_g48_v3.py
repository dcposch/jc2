#!/usr/bin/env python3
"""Emit all H17/q7/a3 grade-48 rows after V2 found a missing tie."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform
import time


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V2 = ROOT / "cases/max12_812_order2_affine_faber_a_h17_q7_a3_predecessor_g48_sparse_v2_20260826/compute_h17_q7_g48_sparse.py"
V2_SHA = "1ee515a8da4bc86ade10a86dae6a526c57d58eea0061158b977eab2b76020cf4"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_v2():
    if digest(V2) != V2_SHA:
        fail("frozen V2 source mismatch")
    spec = importlib.util.spec_from_file_location("h17q7_v2", V2)
    if spec is None or spec.loader is None:
        fail("cannot import V2 source")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    v2 = load_v2()
    tag = v2.require_aws()
    base = v2.load_base()
    field = base.Field(args.characteristic)
    if digest(base.TAILS) != v2.TAILS_SHA:
        fail("frozen tails mismatch")
    tails = json.loads(base.TAILS.read_text())
    canonical_tails = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical_tails.encode()).hexdigest() != v2.CANONICAL_SHA:
        fail("canonical tails mismatch")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    abstract_rows = v2.build_abstract_rows(base, field, tails)
    source, mu2, mu4 = v2.source_series(base, field)
    expanded = {}
    survivor_counts = {}
    for number in range(1, 8):
        expanded[number], survivor_counts[number] = v2.expand_row(base, field, abstract_rows[number], source)
    expanded[2] = base.series_add(field, expanded[2], base.series_scale(field, mu2, -1))
    expanded[4] = base.series_add(field, expanded[4], base.series_scale(field, mu4, -1))
    for number in range(1, 8):
        for grade in range(48):
            if expanded[number][grade]:
                fail(("nonzero predecessor below grade48", number, grade, expanded[number][grade]))
    rows = {number: expanded[number][48] for number in range(1, 8)}
    monomial = tuple(sorted(((base.JET_INDEX["p"], 5), (base.JET_INDEX["a3"], 2), (base.JET_INDEX["kk0"], 1))))
    if rows[2].get(monomial, field.value(0)) != field.value(Fraction(15, 128)):
        fail(("missing V2 repair sentinel", rows[2].get(monomial)))
    payload = v2.canonical_rows(base, field, rows)
    payload_bytes = (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode()
    (output / "grade48_rows.json").write_bytes(payload_bytes)
    result = {
        "status": "PASS-A-H17-Q7-A3-G48-DIAGNOSTIC-V3",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "v2_sha256": digest(V2),
        "tails_sha256": digest(base.TAILS),
        "row_supports": {str(number): len(rows[number]) for number in range(1, 8)},
        "abstract_survivors": {str(number): survivor_counts[number] for number in range(1, 8)},
        "grade48_rows_sha256": sha256(payload_bytes).hexdigest(),
        "v2_missing_term_coefficient": field.text(field.value(Fraction(15, 128))),
        "lower_zero_rows": 7,
        "elapsed_seconds": time.monotonic() - started,
        "scope": "FIXED_H17_Q7_A3_NORMALIZED_GRAPH_COMPLETE_GRADE48_ROWS_DIAGNOSTIC_ONLY_NO_ELIMINATION_RATIONAL_REGRADING_SOURCE_REES_ORDER2_MAX12_OR_JC2_VERDICT",
    }
    (output / "result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("A_H17Q7V3_ROWS_SHA256=" + result["grade48_rows_sha256"])
    print("A_H17Q7V3_ROW_SUPPORTS=" + json.dumps(result["row_supports"], sort_keys=True, separators=(",", ":")))
    print("A_H17Q7V3_LOWER_ZERO=1")
    print("A_H17Q7V3_MISSING_TERM_RETAINED=1")
    print("A_H17Q7V3_ENDPOINT=PASS_COMPLETE_GRADE48_ROWS_DIAGNOSTIC")
    print("A_H17Q7V3_DONE=1")
    print("A_H17Q7V3_SCOPE=" + result["scope"])


if __name__ == "__main__":
    main()
