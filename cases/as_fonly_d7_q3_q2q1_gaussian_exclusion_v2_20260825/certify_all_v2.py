#!/usr/bin/env python3
"""V2 certificates with redundant-support omission controls."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
V1 = (ROOT / "cases/as_fonly_d7_q3_q2q1_gaussian_exclusion_20260825"
      / "certify_all.py")
EXPECTED = "9a34970455d0844b4a4894dca34389fd2cc43704466d9ddf13e3c09d88cddcda"
payload = V1.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED
marker = b"\nbranches = []\n"
assert payload.count(marker) == 1
ns = {"__file__": str(V1), "__name__": "__gaussian_cert_v2_prefix__"}
exec(compile(payload.split(marker, 1)[0] + b"\n", str(V1), "exec"), ns)

accepted = ns["accepted"]
active1 = ns["active1"]
inactive1 = ns["inactive1"]
slots = ns["slots"]
raw_rows = ns["raw_rows"]
place = ns["place"]
extract_affine = ns["extract_affine"]
rref_solve = ns["rref_solve"]
tracked_contradiction = ns["tracked_contradiction"]
m1, c1, r1, a1 = ns["m1"], ns["c1"], ns["r1"], ns["a1"]
raw_n = ns["raw_n"]

def solve_subset(matrix, constant, kept):
    return rref_solve([matrix[i] for i in kept],
                      [constant[i] for i in kept])

def minimal_omission_control(matrix, constant):
    kept = list(range(len(matrix)))
    omitted = []
    while True:
        rank, aug, particular, kernel, bad = solve_subset(matrix, constant, kept)
        if particular is not None:
            break
        submatrix = [matrix[i] for i in kept]
        rhs = [(-constant[i]) % 3 for i in kept]
        _, certificate = tracked_contradiction(submatrix, rhs)
        local = next(i for i, value in enumerate(certificate) if value)
        omitted.append(kept.pop(local))
    # Re-add every row that is not necessary for this control; iterate to a
    # fixed point so the result is inclusion-minimal under single re-addition.
    changed = True
    while changed:
        changed = False
        for row in list(reversed(omitted)):
            trial = sorted(kept + [row])
            trial_result = solve_subset(matrix, constant, trial)
            if trial_result[2] is not None:
                kept = trial
                omitted.remove(row)
                rank, aug, particular, kernel, bad = trial_result
                changed = True
    rank, aug, particular, kernel, bad = solve_subset(matrix, constant, kept)
    assert particular is not None
    for row in omitted:
        assert solve_subset(matrix, constant, sorted(kept + [row]))[2] is None
    return kept, sorted(omitted), particular, len(kernel), rank, aug

active_matrix = [[m1[row][column] for column in active1]
                 for row in range(len(slots))]
stage1_rhs = [(-value) % 3 for value in c1]
branches = []
for branch_index, (active_values, fixed) in enumerate(accepted):
    function2 = lambda x, fixed=fixed: raw_rows(place(fixed, x), 81, slots)
    constant, matrix, design = extract_affine(function2, len(inactive1))
    rhs = [(-value) % 3 for value in constant]
    rank, certificate = tracked_contradiction(matrix, rhs)
    kept, omitted, particular, control_kernel, control_rank, control_aug = (
        minimal_omission_control(matrix, constant))
    raw = place(fixed, particular)
    stage27 = raw_rows(raw, 27, slots)
    stage81 = raw_rows(raw, 81, slots)
    assert stage27 == [0] * len(slots)
    assert all(stage81[i] == 0 for i in kept)
    assert any(stage81[i] != 0 for i in omitted)
    sparse = [[i, value] for i, value in enumerate(certificate) if value]
    branches.append({
        "branch_index": branch_index, "active_values": list(active_values),
        "matrix": matrix, "rhs": rhs,
        "matrix_sha256": hashlib.sha256(bytes(
            value for row in matrix for value in row)).hexdigest(),
        "rhs_sha256": hashlib.sha256(bytes(rhs)).hexdigest(),
        "rank": rank, "augmented_rank": rank + 1,
        "input_dimension": len(inactive1), "design_count": design,
        "left_null_sparse": sparse,
        "left_null_sha256": hashlib.sha256(bytes(certificate)).hexdigest(),
        "omission_control": {
            "kind": "inclusion-minimal-redundant-support",
            "kept_rows": kept, "omitted_rows": omitted,
            "omitted_slots": [list(slots[i]) for i in omitted],
            "omitted_residuals": [stage81[i] for i in omitted],
            "particular": particular, "kernel_dimension": control_kernel,
            "rank": control_rank, "augmented_rank": control_aug,
        },
    })

result = {
    "status": "PASS-AS-Q3-Q2Q1-GAUSSIAN-EXCLUSION-V2",
    "v1_certificate_source_sha256": EXPECTED,
    "model_sha256": hashlib.sha256(
        Path(os.environ["MODEL_OUTPUT"]).read_bytes()).hexdigest(),
    "raw_variable_count": raw_n,
    "stage1": {"row_count": len(slots), "rank": r1,
               "augmented_rank": a1, "active_raw_columns": active1,
               "inactive_raw_columns": inactive1,
               "active_matrix": active_matrix, "rhs": stage1_rhs,
               "accepted_assignments": [list(v) for v, _ in accepted]},
    "branch_count": len(branches), "all_branches_inconsistent": True,
    "branches": branches,
    "scope": "one complete displayed Q3 affine fibre; no continuation to mod243",
    "refusal_scope": ["not the whole Q5 locus", "not all-depth",
                      "not a counterexample or JC2 conclusion"],
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("branches", len(branches), "ranks",
      sorted(set((b["rank"], b["augmented_rank"]) for b in branches)))
print("omission_sizes", sorted(set(len(b["omission_control"]["omitted_rows"])
                                        for b in branches)))
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])
