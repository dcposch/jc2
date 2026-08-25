#!/usr/bin/env python3
"""Exact V2 checkpoint for the nonlinear accepted-digit /81 carry."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
V1 = (ROOT / "cases/as_fonly_d7_q3_two_level_q2_q1_20260825"
      / "solve_two_level.py")
EXPECTED = "cec50f9fd9bf9ce3311e5687658473e9c4d7577b4997ac96b1e1f3b3932d2fcd"
payload = V1.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED
marker = b"\nstages = []\n"
assert payload.count(marker) == 1
prefix = payload.split(marker, 1)[0] + b"\n"
namespace = {"__file__": str(V1), "__name__": "__carry_v2_prefix__"}
exec(compile(prefix, str(V1), "exec"), namespace)

slots = namespace["slots"]
raw_variable_count = namespace["raw_variable_count"]
q3_kdim = namespace["q3_kdim"]
raw_rows = namespace["raw_rows"]
parameterize = namespace["parameterize"]
extract_affine = namespace["extract_affine"]
rref_solve = namespace["rref_solve"]

stage1 = lambda values: raw_rows(values, 27, slots)
c1, m1, design1 = extract_affine(stage1, raw_variable_count)
r1, a1, p1, k1, bad1 = rref_solve(m1, c1)
assert p1 is not None and not bad1

def stage2(coordinates):
    return raw_rows(parameterize(p1, k1, coordinates), 81, slots)

c2 = stage2([0] * len(k1))
columns = []
for index in range(len(k1)):
    e = [0] * len(k1)
    e[index] = 1
    columns.append([(a - b) % 3 for a, b in zip(stage2(e), c2)])

first = None
quadratic_design_count = 1
for index in range(len(k1)):
    twice = [0] * len(k1)
    twice[index] = 2
    observed = stage2(twice)
    predicted = [(base + 2 * delta) % 3
                 for base, delta in zip(c2, columns[index])]
    quadratic_design_count += 2
    mismatch = [row for row, (x, y) in enumerate(zip(observed, predicted))
                if x != y]
    if mismatch and first is None:
        first = {"kind": "twice", "coordinates": [index],
                 "mismatch_rows": mismatch,
                 "observed": [observed[row] for row in mismatch],
                 "affine_prediction": [predicted[row] for row in mismatch]}

mixed_failures = 0
first_mixed = None
for left in range(len(k1)):
    for right in range(left + 1, len(k1)):
        pair = [0] * len(k1)
        pair[left] = pair[right] = 1
        observed = stage2(pair)
        predicted = [(base + dl + dr) % 3
                     for base, dl, dr in zip(c2, columns[left], columns[right])]
        quadratic_design_count += 1
        mismatch = [row for row, (x, y) in enumerate(zip(observed, predicted))
                    if x != y]
        if mismatch:
            mixed_failures += 1
            if first_mixed is None:
                first_mixed = {"kind": "pair", "coordinates": [left, right],
                               "mismatch_rows": mismatch,
                               "observed": [observed[row] for row in mismatch],
                               "affine_prediction": [predicted[row]
                                                     for row in mismatch]}

row_supports = [[column for column in range(raw_variable_count)
                 if m1[row][column]] for row in range(len(slots))]
column_supports = [[row for row in range(len(slots)) if m1[row][column]]
                   for column in range(raw_variable_count)]
result = {
    "status": "PASS-AS-Q2Q1-V2-NONLINEAR-CARRY-CHECKPOINT",
    "v1_sha256": EXPECTED,
    "model_sha256": hashlib.sha256(
        Path(os.environ["MODEL_OUTPUT"]).read_bytes()).hexdigest(),
    "q3_kernel_dimension": q3_kdim,
    "raw_variable_count": raw_variable_count,
    "stage1": {
        "row_count": len(slots), "design_count": design1,
        "rank": r1, "augmented_rank": a1,
        "kernel_dimension": len(k1), "particular": p1,
        "kernel_basis": k1,
        "matrix_sha256": hashlib.sha256(bytes(
            value for row in m1 for value in row)).hexdigest(),
        "rhs_sha256": hashlib.sha256(bytes((-x) % 3 for x in c1)).hexdigest(),
        "row_supports": row_supports,
        "column_supports": column_supports,
    },
    "stage2": {
        "row_count": len(slots), "input_dimension": len(k1),
        "constant_sha256": hashlib.sha256(bytes(c2)).hexdigest(),
        "linear_columns_sha256": hashlib.sha256(bytes(
            value for column in columns for value in column)).hexdigest(),
        "affine": first is None and first_mixed is None,
        "first_pure_failure": first,
        "first_mixed_failure": first_mixed,
        "mixed_affine_failure_count": mixed_failures,
        "quadratic_design_point_count": quadratic_design_count,
    },
    "scope": "diagnostic exact first carry; no /81 zero-locus classification",
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("stage1", r1, a1, len(k1), "stage2_affine", result["stage2"]["affine"])
print("first_pure", first)
print("first_mixed", first_mixed)
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])
