#!/usr/bin/env python3
"""Independent literal-integer replay of a state-complete SAT model."""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
V1 = (ROOT / "cases/as_fonly_d7_q3_two_level_q2_q1_20260825"
      / "solve_two_level.py")
EXPECTED_V1 = "cec50f9fd9bf9ce3311e5687658473e9c4d7577b4997ac96b1e1f3b3932d2fcd"
payload = V1.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_V1
marker = b"\nstages = []\n"
assert payload.count(marker) == 1
ns = {"__file__": str(V1), "__name__": "__state_complete_replay__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(payload.split(marker, 1)[0] + b"\n", str(V1), "exec"), ns)

def parse_model(path):
    values = {}
    for line in path.read_text().splitlines():
        fields = line.split()
        if len(fields) == 2 and (fields[0].startswith("q3_") or
                                 fields[0][0] in "wzhj"):
            try:
                value = int(fields[1])
            except ValueError:
                continue
            values[fields[0]] = value
    return values

model_path = Path(os.environ["SOLVER_MODEL"])
values = parse_model(model_path)
q3_kdim = ns["q3_kdim"]
q3_names = [f"q3_{index}" for index in range(q3_kdim)]
fresh_names = [f"{prefix}_{index}"
               for prefix, degree in (("w3", 3), ("z3", 3),
                                      ("w2", 2), ("z2", 2),
                                      ("h3", 3), ("j3", 3),
                                      ("h2", 2), ("j2", 2))
               for index in range(degree + 1)]
expected = set(q3_names + fresh_names)
assert set(values) == expected, (sorted(expected - set(values)),
                                 sorted(set(values) - expected))
assert all(0 <= value <= 2 for value in values.values())
raw_values = [values[name] for name in q3_names + fresh_names]

P, Q, q3_values, blocks = ns["raw_candidate"](raw_values)
determinant = ns["determinant_minus_one"](P, Q)
slots = ns["slots"]
high_slots = ns["high_slots"]
assert ns["q3_candidate"].__globals__["equations"](q3_values) == [0] * 67
stage27 = ns["raw_rows"](raw_values, 27, slots)
stage81 = ns["raw_rows"](raw_values, 81, slots)
stage243 = ns["raw_rows"](raw_values, 243, high_slots)
assert stage27 == [0] * 91
assert stage81 == [0] * 91
assert stage243 == [0] * 63
assert all(value % 243 == 0 for value in determinant.values())
assert all(determinant.get(xy, 0) % 729 == 0 for xy in high_slots)
assert determinant.get((0, 0), 0) == 0
assert max(i + j for i, j in P) <= 7
assert max(i + j for i, j in Q) <= 7

result = {
    "status": "PASS-AS-Q3-STATE-COMPLETE-DIRECT-INTEGER-REPLAY",
    "solver_model_sha256": hashlib.sha256(model_path.read_bytes()).hexdigest(),
    "q3_coordinates": [values[name] for name in q3_names],
    "fresh_digits": {name: values[name] for name in fresh_names},
    "q3_values": q3_values, "blocks": blocks,
    "inherited_q3_row_count": 67,
    "stage27_row_count": len(stage27),
    "stage81_row_count": len(stage81),
    "stage243_high_row_count": len(stage243),
    "degree_zero_exactly_zero": True,
    "support_cap_D7": True,
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("rows", 67, len(stage27), len(stage81), len(stage243))
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])
