#!/usr/bin/env python3
"""Emit exact left-null certificates for all 27 `/81` carry branches."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
V3 = (ROOT / "cases/as_fonly_d7_q3_two_level_q2_q1_v3_branches_20260825"
      / "classify_branches.py")
EXPECTED = "4f6b94ce223e60b9023b8e3fe91a1113b0978a4ff74e986aa1227e01217006b9"
payload = V3.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED
marker = b"\nbranches = []\n"
assert payload.count(marker) == 1
ns = {"__file__": str(V3), "__name__": "__gaussian_cert_prefix__"}
exec(compile(payload.split(marker, 1)[0] + b"\n", str(V3), "exec"), ns)

accepted = ns["accepted"]
active1 = ns["active1"]
inactive1 = ns["inactive1"]
slots = ns["slots"]
raw_rows = ns["raw_rows"]
place = ns["place"]
extract_affine = ns["extract_affine"]
rref_solve = ns["rref_solve"]
m1 = ns["m1"]
c1 = ns["c1"]
r1 = ns["r1"]
a1 = ns["a1"]
raw_n = ns["raw_n"]

def tracked_contradiction(matrix, rhs):
    rows = len(matrix)
    columns = len(matrix[0])
    work = [[value % 3 for value in row] + [target % 3]
            for row, target in zip(matrix, rhs)]
    transform = [[1 if i == j else 0 for j in range(rows)]
                 for i in range(rows)]
    pivot_row = 0
    pivots = []
    for column in range(columns):
        chosen = next((i for i in range(pivot_row, rows)
                       if work[i][column]), None)
        if chosen is None:
            continue
        work[pivot_row], work[chosen] = work[chosen], work[pivot_row]
        transform[pivot_row], transform[chosen] = (
            transform[chosen], transform[pivot_row])
        inverse = 1 if work[pivot_row][column] == 1 else 2
        work[pivot_row] = [(inverse * x) % 3 for x in work[pivot_row]]
        transform[pivot_row] = [(inverse * x) % 3
                                for x in transform[pivot_row]]
        for i in range(rows):
            if i == pivot_row or not work[i][column]:
                continue
            scalar = work[i][column]
            work[i] = [(x - scalar * y) % 3
                       for x, y in zip(work[i], work[pivot_row])]
            transform[i] = [(x - scalar * y) % 3
                            for x, y in zip(transform[i],
                                            transform[pivot_row])]
        pivots.append(column)
        pivot_row += 1
    contradiction_index = next((i for i, row in enumerate(work)
                                if not any(row[:-1]) and row[-1]), None)
    assert contradiction_index is not None
    scalar = 1 if work[contradiction_index][-1] == 1 else 2
    certificate = [(scalar * x) % 3
                   for x in transform[contradiction_index]]
    assert all(sum(certificate[i] * matrix[i][j] for i in range(rows)) % 3 == 0
               for j in range(columns))
    assert sum(certificate[i] * rhs[i] for i in range(rows)) % 3 == 1
    return len(pivots), certificate

def omission_control(matrix, constant, certificate):
    for omitted in [i for i, value in enumerate(certificate) if value]:
        reduced_matrix = [row for i, row in enumerate(matrix) if i != omitted]
        reduced_constant = [value for i, value in enumerate(constant)
                            if i != omitted]
        rank, aug, particular, kernel, bad = rref_solve(
            reduced_matrix, reduced_constant)
        if particular is not None:
            return omitted, particular, len(kernel), rank, aug
    for omitted in range(len(matrix)):
        reduced_matrix = [row for i, row in enumerate(matrix) if i != omitted]
        reduced_constant = [value for i, value in enumerate(constant)
                            if i != omitted]
        rank, aug, particular, kernel, bad = rref_solve(
            reduced_matrix, reduced_constant)
        if particular is not None:
            return omitted, particular, len(kernel), rank, aug
    return None

active_matrix = [[m1[row][column] for column in active1]
                 for row in range(len(slots))]
stage1_rhs = [(-value) % 3 for value in c1]
branches = []
for branch_index, (active_values, fixed) in enumerate(accepted):
    function2 = lambda x, fixed=fixed: raw_rows(place(fixed, x), 81, slots)
    constant, matrix, design = extract_affine(function2, len(inactive1))
    rhs = [(-value) % 3 for value in constant]
    rank, certificate = tracked_contradiction(matrix, rhs)
    control = omission_control(matrix, constant, certificate)
    assert control is not None
    omitted, particular, control_kernel, control_rank, control_aug = control
    raw = place(fixed, particular)
    stage27 = raw_rows(raw, 27, slots)
    stage81 = raw_rows(raw, 81, slots)
    assert stage27 == [0] * len(slots)
    assert all(value == 0 for i, value in enumerate(stage81) if i != omitted)
    assert stage81[omitted] != 0
    sparse = [[i, value] for i, value in enumerate(certificate) if value]
    branches.append({
        "branch_index": branch_index,
        "active_values": list(active_values),
        "matrix": matrix, "rhs": rhs,
        "matrix_sha256": hashlib.sha256(bytes(
            value for row in matrix for value in row)).hexdigest(),
        "rhs_sha256": hashlib.sha256(bytes(rhs)).hexdigest(),
        "rank": rank, "augmented_rank": rank + 1,
        "input_dimension": len(inactive1), "design_count": design,
        "left_null_sparse": sparse,
        "left_null_sha256": hashlib.sha256(bytes(certificate)).hexdigest(),
        "omission_control": {
            "omitted_row": omitted,
            "omitted_slot": list(slots[omitted]),
            "omitted_residual": stage81[omitted],
            "particular": particular,
            "kernel_dimension": control_kernel,
            "rank": control_rank, "augmented_rank": control_aug,
        },
    })

assert len(branches) == 27
result = {
    "status": "PASS-AS-Q3-Q2Q1-GAUSSIAN-EXCLUSION",
    "v3_sha256": EXPECTED,
    "model_sha256": hashlib.sha256(
        Path(os.environ["MODEL_OUTPUT"]).read_bytes()).hexdigest(),
    "raw_variable_count": raw_n,
    "stage1": {
        "row_count": len(slots), "rank": r1, "augmented_rank": a1,
        "active_raw_columns": active1,
        "inactive_raw_columns": inactive1,
        "active_matrix": active_matrix, "rhs": stage1_rhs,
        "accepted_assignments": [list(values) for values, _ in accepted],
    },
    "branch_count": len(branches), "all_branches_inconsistent": True,
    "branches": branches,
    "scope": "one complete displayed Q3 affine fibre; no Q2/Q1 continuation to mod243",
    "refusal_scope": ["not the whole Q5 locus", "not all-depth",
                      "not a counterexample or JC2 conclusion"],
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("branches", len(branches), "ranks",
      sorted(set((b["rank"], b["augmented_rank"]) for b in branches)))
print("certificate_support_histogram", sorted(
    {sum(1 for _ in b["left_null_sparse"]) for b in branches}))
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])
