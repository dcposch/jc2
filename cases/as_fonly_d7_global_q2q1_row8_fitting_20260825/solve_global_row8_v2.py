#!/usr/bin/env python3
"""Append the eliminated Q2/Q1 row-8 scalar to the complete Q5 formula."""
from __future__ import annotations

import hashlib
import json
import os
import runpy
import tempfile
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
PARENT = (ROOT / "cases/as_fonly_d7_global_q5_h6_20260825"
          / "solve_global_q5_h6.py")
EXPECTED = "2bdf4bb4743a4bf5904c87b5550df6fa7908e779e6c90645ab2e911bda87805d"
payload = PARENT.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED

target_smt2 = Path(os.environ["SMT2_OUTPUT"])
target_json = Path(os.environ["OUTPUT_JSON"])
target_expression = Path(os.environ["ROW8_EXPR_OUTPUT"])
saved_environment = {
    name: os.environ.get(name)
    for name in ("SMT2_OUTPUT", "OUTPUT_JSON")
}

with tempfile.TemporaryDirectory(prefix="as-row8-parent-") as temp_name:
    temp = Path(temp_name)
    parent_smt2 = temp / "parent.smt2"
    parent_json = temp / "parent.json"
    os.environ["SMT2_OUTPUT"] = str(parent_smt2)
    os.environ["OUTPUT_JSON"] = str(parent_json)
    module_scope = runpy.run_path(str(PARENT), run_name="__global_row8_parent__")
    parent_result = json.loads(parent_json.read_text())
    parent_smt2_sha256 = hashlib.sha256(parent_smt2.read_bytes()).hexdigest()

for name, value in saved_environment.items():
    if value is None:
        del os.environ[name]
    else:
        os.environ[name] = value

# The pinned compiler wrappers execute their parents into nested dictionaries
# called `scope`.  Walk only that explicit chain and fail closed if the literal
# source namespace containing the solver and carry objects is absent.
source_scope = module_scope
scope_depth = 0
while "solver" not in source_scope:
    assert "scope" in source_scope and isinstance(source_scope["scope"], dict)
    source_scope = source_scope["scope"]
    scope_depth += 1
    assert scope_depth <= 16

required = {
    "solver", "E", "M", "divide_three", "degree_part", "padd", "f3",
    "fadd", "fmul", "fscale", "bv", "pred_vars", "z3",
}
assert required <= set(source_scope), sorted(required - set(source_scope))
solver = source_scope["solver"]
E = source_scope["E"]
M = source_scope["M"]
divide_three = source_scope["divide_three"]
degree_part = source_scope["degree_part"]
padd = source_scope["padd"]
f3 = source_scope["f3"]
fadd = source_scope["fadd"]
fmul = source_scope["fmul"]
fscale = source_scope["fscale"]
bv = source_scope["bv"]
pred_vars = source_scope["pred_vars"]
z3 = source_scope["z3"]

# Literal source carry, followed by the exact two-row elimination identity
#   kappa = omega + h*stage_x - stage_y,
#   omega = ry - h*rx.
E1_low_degree_one = divide_three(degree_part(E, 1))
Fbase_degree_one = padd(E1_low_degree_one, degree_part(M, 1))
row8_rx = f3(Fbase_degree_one.get((1, 0), bv(0)))
row8_ry = f3(Fbase_degree_one.get((0, 1), bv(0)))
row8_omega = fadd(row8_ry, fscale(2, fmul(pred_vars["h"], row8_rx)))
row8_omitted = os.environ.get("OMIT_GLOBAL_ROW8", "0") == "1"
if not row8_omitted:
    solver.add(row8_omega == bv(0))

row8_payload = (row8_omega.sexpr() + "\n").encode()
target_expression.write_bytes(row8_payload)
smt2 = solver.to_smt2().encode()
target_smt2.write_bytes(smt2)
check = solver.check()

result = dict(parent_result)
result.update({
    "solver_status": str(check),
    "solver_timeout_ms": int(os.environ.get("SOLVER_TIMEOUT_MS", "1")),
    "parent_source_sha256": EXPECTED,
    "parent_emitted_smt2_sha256": parent_smt2_sha256,
    "nested_source_scope_depth": scope_depth,
    "q2q1_row8_omitted": row8_omitted,
    "q2q1_row8_coordinate": [2, 1],
    "q2q1_row8_eliminated_scalar": "ry-h*rx",
    "q2q1_row8_expression_sha256": hashlib.sha256(row8_payload).hexdigest(),
    "displayed_equation_count_with_row8": 198,
    "direct_integer_replay_required_for_sat": True,
    "scope": ("complete displayed Q5/H6,J6 formula plus the eliminated "
              "necessary Q2/Q1 row-8 scalar; no Q4/Q3 sufficiency"),
})
if check == z3.sat:
    model = solver.model()
    result["q2q1_row8_value"] = model.eval(
        row8_omega, model_completion=True).as_long()

encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
target_json.write_bytes(encoded)
print("parent_source_sha256", EXPECTED)
print("nested_source_scope_depth", scope_depth)
print("parent_smt2_sha256", parent_smt2_sha256)
print("displayed_equation_inventory", 198)
print("q2q1_row8_coordinate", 2, 1, "omitted", row8_omitted)
print("q2q1_row8_expression_sha256", hashlib.sha256(row8_payload).hexdigest())
print("formula_sha256", hashlib.sha256(smt2).hexdigest())
print("solver_status", check)
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-AS-GLOBAL-Q2Q1-ROW8-FITTING-EMIT-V2")
