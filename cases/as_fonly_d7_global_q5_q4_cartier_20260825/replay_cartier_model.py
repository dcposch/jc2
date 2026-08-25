#!/usr/bin/env python3
"""Direct integer replay of a SAT model for the Q4 Cartier discriminator."""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
PARENT = (ROOT / "cases/as_fonly_d7_global_q5_h6_replay_erratum_20260825"
          / "replay_global_q5_h6_v2.py")
EXPECTED_PARENT_SHA = (
    "41e0e74ec4d318bdd33242dcb9053ce53572470570ab5d54f1431184eb789ffa")
payload = PARENT.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_PARENT_SHA

parent_output = Path(os.environ["PARENT_OUTPUT_JSON"])
old_output = os.environ.get("OUTPUT_JSON")
os.environ["OUTPUT_JSON"] = str(parent_output)
namespace = {"__file__": str(PARENT), "__name__": "__cartier_parent__"}
with contextlib.redirect_stdout(io.StringIO()) as parent_stdout:
    exec(compile(payload, str(PARENT), "exec"), namespace)
if old_output is None:
    del os.environ["OUTPUT_JSON"]
else:
    os.environ["OUTPUT_JSON"] = old_output

scope = namespace["scope"]
while "homogeneous_numeric" not in scope:
    scope = scope["scope"]
nadd = scope["nadd"]
nmul = scope["nmul"]
nscale = scope["nscale"]
nderivative = scope["nderivative"]
degree_part = scope["degree_part"]
divide_exact = scope["divide_exact"]
row = scope["row"]
G = scope["G"]
P5 = scope["P5"]
Q5 = scope["Q5"]

recursive = row(G(4), 4)
det_minus_one = nadd(
    nmul(nderivative(P5, 0), nderivative(Q5, 1)),
    nscale(-1, nmul(nderivative(P5, 1), nderivative(Q5, 0))),
    {(0, 0): -1})
literal = row(divide_exact(degree_part(det_minus_one, 4), 81), 4)
assert recursive == literal

expect = int(os.environ.get("EXPECT_CARTIER", "0"))
assert expect in (0, 1, 2)
assert recursive[2] == expect

result = {
    "status": "PASS-GLOBAL-Q5-Q4-CARTIER-DIRECT-REPLAY",
    "scope": "displayed Q5 parent rows plus the x2y2 Q4 Cartier coordinate",
    "model_sha256": hashlib.sha256(
        Path(os.environ["MODEL_OUTPUT"]).read_bytes()).hexdigest(),
    "parent_output_sha256": hashlib.sha256(parent_output.read_bytes()).hexdigest(),
    "parent_stdout_sha256": hashlib.sha256(
        parent_stdout.getvalue().encode()).hexdigest(),
    "q4_recursive_row": recursive,
    "q4_literal_div81_row": literal,
    "q4_cartier_x2y2": recursive[2],
    "expected": expect,
    "recursive_literal_agreement": True,
    "refusal_scope": [
        "not all five Q4 rows",
        "not Q3 through Q0",
        "not a complete map modulo 243",
        "not an all-depth/no-lift/Jacobian-conjecture inference",
    ],
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("q4_row", recursive)
print("q4_cartier_x2y2", recursive[2])
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-GLOBAL-Q5-Q4-CARTIER-DIRECT-REPLAY")
