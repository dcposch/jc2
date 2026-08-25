#!/usr/bin/env python3
"""Independent verifier for V2 Gaussian and omission certificates."""
from __future__ import annotations

import hashlib
import itertools
import json
import os
from pathlib import Path


path = Path(os.environ["CERTIFICATE_JSON"])
data = json.loads(path.read_text())
assert data["status"] == "PASS-AS-Q3-Q2Q1-GAUSSIAN-EXCLUSION-V2"
stage1 = data["stage1"]
accepted = []
for values in itertools.product(range(3), repeat=8):
    if all(sum(row[j] * values[j] for j in range(8)) % 3 == rhs
           for row, rhs in zip(stage1["active_matrix"], stage1["rhs"])):
        accepted.append(list(values))
assert accepted == stage1["accepted_assignments"]
assert len(accepted) == len(data["branches"]) == 27

for branch in data["branches"]:
    matrix, rhs = branch["matrix"], branch["rhs"]
    rows, columns = len(matrix), len(matrix[0])
    certificate = [0] * rows
    for row, value in branch["left_null_sparse"]:
        certificate[row] = value
    assert all(sum(certificate[i] * matrix[i][j] for i in range(rows)) % 3 == 0
               for j in range(columns))
    assert sum(certificate[i] * rhs[i] for i in range(rows)) % 3 == 1
    assert hashlib.sha256(bytes(certificate)).hexdigest() == branch["left_null_sha256"]
    control = branch["omission_control"]
    omitted = set(control["omitted_rows"])
    kept = set(control["kept_rows"])
    assert omitted and omitted.isdisjoint(kept) and omitted | kept == set(range(rows))
    particular = control["particular"]
    residuals = [(sum(row[j] * particular[j] for j in range(columns)) - target) % 3
                 for row, target in zip(matrix, rhs)]
    assert all(residuals[i] == 0 for i in kept)
    assert [residuals[i] for i in control["omitted_rows"]] == control["omitted_residuals"]
    assert any(residuals[i] for i in omitted)

print("input_sha256", hashlib.sha256(path.read_bytes()).hexdigest())
print("accepted_assignments", len(accepted), "certificates", len(data["branches"]))
print("PASS-AS-Q3-Q2Q1-INDEPENDENT-CERTIFICATE-VERIFY-V2")
