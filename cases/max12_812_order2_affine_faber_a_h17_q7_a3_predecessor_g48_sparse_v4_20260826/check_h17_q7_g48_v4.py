#!/usr/bin/env python3
"""Validate the corrected H17/q7/a3 grade-48 predecessor formulas."""

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
V3 = ROOT / "cases/max12_812_order2_affine_faber_a_h17_q7_a3_predecessor_g48_sparse_v3_20260826/emit_h17_q7_g48_v3.py"
V3_SHA = "759f61fd62b50263915a0dba2a3827208e995e71791811c0d5494ce9685ce93e"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_v3():
    if digest(V3) != V3_SHA:
        fail("frozen V3 source mismatch")
    spec = importlib.util.spec_from_file_location("h17q7_v3", V3)
    if spec is None or spec.loader is None:
        fail("cannot import V3 source")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    v3 = load_v3()
    v2 = v3.load_v2()
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
    expected = v2.expected_rows(base, field)
    v = lambda name: base.jet_var(field, name)
    center2 = v2._mul_many(base, field, (v("kk0"), v("a3"), v("a3"), v("p"), v("p"), v("p"), v("p"), v("p")))
    center6 = base.jet_mul(field, center2, base.jet_mul(field, v("p"), v("p")))
    expected[2] = base.jet_add(field, expected[2], base.jet_scale(field, center2, Fraction(15, 128)))
    expected[6] = base.jet_add(field, expected[6], base.jet_scale(field, center6, Fraction(-15, 1024)))
    for number in range(1, 8):
        if rows[number] != expected[number]:
            fail(("corrected formula mismatch", number, rows[number], expected[number]))
    p = v("p")
    relation5 = base.jet_add(field, base.jet_scale(field, base.jet_mul(field, base.jet_mul(field, p, p), rows[1]), Fraction(3, 32)), base.jet_scale(field, base.jet_mul(field, p, rows[3]), Fraction(-1, 4)))
    relation7 = base.jet_add(field, base.jet_scale(field, base.jet_mul(field, base.jet_mul(field, p, p), rows[3]), Fraction(1, 32)), base.jet_scale(field, base.jet_mul(field, base.jet_mul(field, base.jet_mul(field, p, p), p), rows[1]), Fraction(-1, 64)))
    if relation5 != rows[5] or relation7 != rows[7]:
        fail("odd-row redundancy mismatch")
    zero = field.value(0)
    witness_x = {name: 0 for name in base.JET_VARS}
    witness_x.update({"p": 1, "m": 1, "a3": 1, "kk0": 1, "x": 1, "d2": Fraction(15, 8), "dm": Fraction(-15, 128), "d4": Fraction(3, 32)})
    witness_y = {name: 0 for name in base.JET_VARS}
    witness_y.update({"p": 1, "m": 1, "a3": 1, "kk0": 1, "y": 1, "d2": Fraction(-33, 8), "dm": Fraction(129, 128), "d4": Fraction(-3, 16)})
    if any(value != zero for value in v2.evaluate_rows(base, field, rows, witness_x).values()):
        fail("D(x) unit-center witness failed")
    if any(value != zero for value in v2.evaluate_rows(base, field, rows, witness_y).values()):
        fail("D(y) unit-center witness failed")
    negative = dict(witness_x); negative["d4"] = field.value(Fraction(1, 8))
    negative_values = v2.evaluate_rows(base, field, rows, negative)
    if negative_values[4] == zero:
        fail("row4 omission negative failed")
    payload = v2.canonical_rows(base, field, rows)
    payload_bytes = (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode()
    (output / "grade48_rows.json").write_bytes(payload_bytes)
    result = {
        "status": "PASS-A-H17-Q7-A3-G48-CORRECTED-V4",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "v3_sha256": digest(V3),
        "tails_sha256": digest(base.TAILS),
        "row_supports": {str(number): len(rows[number]) for number in range(1, 8)},
        "abstract_survivors": {str(number): survivor_counts[number] for number in range(1, 8)},
        "grade48_rows_sha256": sha256(payload_bytes).hexdigest(),
        "lower_zero_rows": 7,
        "corrected_formulas": 7,
        "odd_redundancies": 2,
        "unit_center_projective_witnesses": 2,
        "negative_control_row4": field.text(negative_values[4]),
        "elapsed_seconds": time.monotonic() - started,
        "scope": "FIXED_H17_Q7_A3_NORMALIZED_GRAPH_CORRECTED_GRADE48_PREDECESSOR_ONLY_NO_RATIONAL_REGRADING_SOURCE_REES_ORDER2_MAX12_OR_JC2_VERDICT",
    }
    (output / "result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("A_H17Q7V4_ROWS_SHA256=" + result["grade48_rows_sha256"])
    print("A_H17Q7V4_LOWER_ZERO=1")
    print("A_H17Q7V4_CORRECTED_FORMULAS=1")
    print("A_H17Q7V4_REDUNDANCIES=1")
    print("A_H17Q7V4_WITNESS_X=1")
    print("A_H17Q7V4_WITNESS_Y=1")
    print("A_H17Q7V4_NEGATIVE_CONTROL=1")
    print("A_H17Q7V4_ENDPOINT=PASS_CORRECTED_GRADE48_PREDECESSOR")
    print("A_H17Q7V4_DONE=1")
    print("A_H17Q7V4_SCOPE=" + result["scope"])


if __name__ == "__main__":
    main()
