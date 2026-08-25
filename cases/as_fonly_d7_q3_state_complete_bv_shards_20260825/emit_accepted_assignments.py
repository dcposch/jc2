#!/usr/bin/env python3
"""Derive the exact 27 accepted assignments of the first-carry source cone."""
from __future__ import annotations

import hashlib
import itertools
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
ns = {"__file__": str(V1), "__name__": "__accepted_assignments__"}
exec(compile(payload.split(marker, 1)[0] + b"\n", str(V1), "exec"), ns)

raw_n = ns["raw_variable_count"]
q3_kdim = ns["q3_kdim"]
slots = ns["slots"]
function = lambda values: ns["raw_rows"](values, 27, slots)
c, matrix, design = ns["extract_affine"](function, raw_n)
rank, aug, particular, kernel, bad = ns["rref_solve"](matrix, c)
assert particular is not None and not bad and rank == aug
active = [column for column in range(raw_n)
          if any(row[column] for row in matrix)]
fresh_names = [f"{prefix}_{index}"
               for prefix, degree in (("w3", 3), ("z3", 3),
                                      ("w2", 2), ("z2", 2),
                                      ("h3", 3), ("j3", 3),
                                      ("h2", 2), ("j2", 2))
               for index in range(degree + 1)]
raw_names = [f"q3_{index}" for index in range(q3_kdim)] + fresh_names
active_names = [raw_names[column] for column in active]
accepted = []
for candidate in itertools.product(range(3), repeat=len(active)):
    raw = [0] * raw_n
    for column, value in zip(active, candidate):
        raw[column] = value
    if function(raw) == [0] * len(slots):
        accepted.append(list(candidate))
assert len(active) == 8 and rank == 5 and len(accepted) == 27
result = {
    "status": "PASS-AS-Q3-FIRST-CARRY-27-ASSIGNMENTS",
    "v1_sha256": EXPECTED,
    "model_sha256": hashlib.sha256(
        Path(os.environ["MODEL_OUTPUT"]).read_bytes()).hexdigest(),
    "raw_variable_count": raw_n, "q3_kernel_dimension": q3_kdim,
    "row_count": len(slots), "rank": rank, "augmented_rank": aug,
    "kernel_dimension": len(kernel), "design_count": design,
    "active_raw_columns": active, "active_variable_names": active_names,
    "accepted_assignments": accepted,
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("active", active_names, "accepted", len(accepted))
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])
