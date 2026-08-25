#!/usr/bin/env python3
"""Construct and directly replay the full degree-four restoration row."""
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
namespace = {"__file__": str(PARENT), "__name__": "__full_q4_parent__"}
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
nscale = scope["nscale"]
nmul = scope["nmul"]
nderivative = scope["nderivative"]
degree_part = scope["degree_part"]
divide_exact = scope["divide_exact"]
homogeneous_numeric = scope["homogeneous_numeric"]
row = scope["row"]
P5, Q5 = scope["P5"], scope["Q5"]


def determinant_minus_one(left, right):
    return nadd(
        nmul(nderivative(left, 0), nderivative(right, 1)),
        nscale(-1, nmul(nderivative(left, 1), nderivative(right, 0))),
        {(0, 0): -1})


before = determinant_minus_one(P5, Q5)
before_degree4 = degree_part(before, 4)
before_div81 = divide_exact(before_degree4, 81)
g = row(before_div81, 4)
assert g[2] == 0, g

# Canonical F3 section of divergence at homogeneous degree five.
h5_values = [0] * 6
j5_values = [g[0], (-g[1]) % 3, 0, g[3], (-g[4]) % 3, 0]
H5 = homogeneous_numeric(5, h5_values)
J5 = homogeneous_numeric(5, j5_values)
divergence = nadd(nderivative(H5, 0), nderivative(J5, 1))
divergence_row = row(divergence, 4)
assert [(left + right) % 3
        for left, right in zip(g, divergence_row)] == [0] * 5

P4 = nadd(P5, nscale(81, H5))
Q4 = nadd(Q5, nscale(81, J5))
after = determinant_minus_one(P4, Q4)
after_degree4 = degree_part(after, 4)
after_div81 = divide_exact(after_degree4, 81)
after_row = row(after_div81, 4)
assert after_row == [0] * 5
assert all(value % 243 == 0 for value in after_degree4.values())

# The source-linear divergence accounts for the degree-four change modulo
# 243; higher source terms are retained exactly and checked as a multiple.
delta_remainder = nadd(after_degree4, nscale(-1, before_degree4),
                       nscale(-81, divergence))
assert all(value % 243 == 0 for value in delta_remainder.values())

assert any(g), "negative control requires a genuinely un-restored row"
zero_control_row = g
assert zero_control_row != [0] * 5


def support(poly):
    return [[i, j, value] for (i, j), value in sorted(poly.items()) if value]


model_path = Path(os.environ["MODEL_OUTPUT"])
result = {
    "status": "PASS-AS-Q5-SAT-FULL-Q4-CONSTRUCTIVE-RESTORE",
    "parent_replay_sha256": EXPECTED_PARENT_SHA,
    "model_sha256": hashlib.sha256(model_path.read_bytes()).hexdigest(),
    "parent_output_sha256": hashlib.sha256(parent_output.read_bytes()).hexdigest(),
    "parent_stdout_sha256": hashlib.sha256(
        parent_stdout.getvalue().encode()).hexdigest(),
    "q4_before_div81_mod3_row": g,
    "h5_coefficients_xi_y5mi": h5_values,
    "j5_coefficients_xi_y5mi": j5_values,
    "divergence_mod3_row": divergence_row,
    "q4_after_div81_mod3_row": after_row,
    "q4_after_degree4_divisible_by_243": True,
    "degree4_delta_minus_81_divergence_divisible_by_243": True,
    "zero_restore_negative_control_row": zero_control_row,
    "P4_support": support(P4),
    "Q4_support": support(Q4),
    "max_total_degree_P4": max(sum(term[:2]) for term in support(P4)),
    "max_total_degree_Q4": max(sum(term[:2]) for term in support(Q4)),
    "scope": "one exact Q5 model, complete five-row Q4 restoration",
    "refusal_scope": [
        "not Q3 through Q0",
        "not a complete determinant-one map modulo 243",
        "not all-depth, algebraization, counterexample, or JC2",
    ],
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("q4_before", g)
print("h5", h5_values)
print("j5", j5_values)
print("divergence", divergence_row)
print("q4_after", after_row)
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-AS-Q5-SAT-FULL-Q4-CONSTRUCTIVE-RESTORE")

