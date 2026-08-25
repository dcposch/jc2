#!/usr/bin/env python3
"""Directly restore Q3..Q0 and verify a complete map modulo 243."""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
PARENT = (ROOT / "cases/as_fonly_d7_q5_sat_full_q4_restore_20260825"
          / "replay_full_q4_restore.py")
EXPECTED_PARENT_SHA = (
    "9fa649802565ad52a448c23e8091e9bdeca90576d35834a61ae19ed701fb119c")
payload = PARENT.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_PARENT_SHA

parent_output = Path(os.environ["PARENT_OUTPUT_JSON"])
old_output = os.environ.get("OUTPUT_JSON")
os.environ["OUTPUT_JSON"] = str(parent_output)
namespace = {"__file__": str(PARENT), "__name__": "__lower_parent__"}
with contextlib.redirect_stdout(io.StringIO()) as parent_stdout:
    exec(compile(payload, str(PARENT), "exec"), namespace)
if old_output is None:
    del os.environ["OUTPUT_JSON"]
else:
    os.environ["OUTPUT_JSON"] = old_output

nadd = namespace["nadd"]
nscale = namespace["nscale"]
nmul = namespace["nmul"]
nderivative = namespace["nderivative"]
degree_part = namespace["degree_part"]
divide_exact = namespace["divide_exact"]
homogeneous_numeric = namespace["homogeneous_numeric"]
row = namespace["row"]
determinant_minus_one = namespace["determinant_minus_one"]
current_P, current_Q = namespace["P4"], namespace["Q4"]


def inv3(value):
    value %= 3
    assert value in (1, 2)
    return value


steps = []
for degree in (3, 2, 1, 0):
    before = determinant_minus_one(current_P, current_Q)
    before_part = degree_part(before, degree)
    before_div81 = divide_exact(before_part, 81)
    before_row = row(before_div81, degree)

    hvalues = [0] * (degree + 2)
    jvalues = [0] * (degree + 2)
    for x_power, residual in enumerate(before_row):
        h_coefficient = (x_power + 1) % 3
        j_coefficient = (degree + 1 - x_power) % 3
        if h_coefficient:
            hvalues[x_power + 1] = (
                -residual * inv3(h_coefficient)) % 3
        else:
            assert j_coefficient
            jvalues[x_power] = (-residual * inv3(j_coefficient)) % 3

    H = homogeneous_numeric(degree + 1, hvalues)
    J = homogeneous_numeric(degree + 1, jvalues)
    divergence = nadd(nderivative(H, 0), nderivative(J, 1))
    divergence_row = row(divergence, degree)
    assert [(left + right) % 3
            for left, right in zip(before_row, divergence_row)] == (
                [0] * (degree + 1))

    current_P = nadd(current_P, nscale(81, H))
    current_Q = nadd(current_Q, nscale(81, J))
    after = determinant_minus_one(current_P, current_Q)
    after_part = degree_part(after, degree)
    after_div81 = divide_exact(after_part, 81)
    after_row = row(after_div81, degree)
    assert after_row == [0] * (degree + 1)
    assert all(value % 243 == 0 for value in after_part.values())
    assert all(value % 243 == 0 for (i, j), value in after.items()
               if i + j > degree)
    delta_remainder = nadd(after_part, nscale(-1, before_part),
                           nscale(-81, divergence))
    assert all(value % 243 == 0 for value in delta_remainder.values())
    steps.append({
        "degree": degree,
        "before_div81_mod3_row": before_row,
        "h_coefficients": hvalues,
        "j_coefficients": jvalues,
        "divergence_mod3_row": divergence_row,
        "after_div81_mod3_row": after_row,
    })

final_determinant_minus_one = determinant_minus_one(current_P, current_Q)
assert all(value % 243 == 0 for value in final_determinant_minus_one.values())


def coefficient_mod(poly, key, modulus):
    return poly.get(key, 0) % modulus


seed_P = {(1, 0): 1, (3, 0): -1}
seed_Q = {(0, 1): 1}
all_keys = set(current_P) | set(seed_P)
assert all(coefficient_mod(current_P, key, 3)
           == coefficient_mod(seed_P, key, 3) for key in all_keys)
all_keys = set(current_Q) | set(seed_Q)
assert all(coefficient_mod(current_Q, key, 3)
           == coefficient_mod(seed_Q, key, 3) for key in all_keys)
assert max(i + j for i, j in current_P) <= 7
assert max(i + j for i, j in current_Q) <= 7


def evaluate(poly, xvalue, yvalue):
    return sum(coefficient * xvalue ** i * yvalue ** j
               for (i, j), coefficient in poly.items())


def lift_zero(residue_x):
    xvalue, yvalue = residue_x, 0
    trace = [[1, xvalue, yvalue]]
    for k in range(1, 5):
        modulus = 3 ** k
        px = evaluate(current_P, xvalue, yvalue)
        qy = evaluate(current_Q, xvalue, yvalue)
        assert px % modulus == 0 and qy % modulus == 0
        # The Jacobian is the identity modulo three on the AS seed, so the
        # inhomogeneous Hensel digit is just the negated quotient.
        hx = (-(px // modulus)) % 3
        hy = (-(qy // modulus)) % 3
        xvalue += modulus * hx
        yvalue += modulus * hy
        trace.append([k + 1, xvalue, yvalue])
    assert evaluate(current_P, xvalue, yvalue) % 243 == 0
    assert evaluate(current_Q, xvalue, yvalue) % 243 == 0
    return [xvalue, yvalue], trace


preimages = []
hensel_traces = []
for residue in (0, 1, 2):
    point, trace = lift_zero(residue)
    preimages.append(point)
    hensel_traces.append(trace)
assert len({tuple(point) for point in preimages}) == 3
assert [point[0] % 3 for point in preimages] == [0, 1, 2]


def support(poly):
    return [[i, j, value] for (i, j), value in sorted(poly.items()) if value]


model_path = Path(os.environ["MODEL_OUTPUT"])
result = {
    "status": "PASS-AS-Q5-SAT-COMPLETE-MOD243-CONSTRUCTION",
    "parent_sha256": EXPECTED_PARENT_SHA,
    "model_sha256": hashlib.sha256(model_path.read_bytes()).hexdigest(),
    "parent_output_sha256": hashlib.sha256(parent_output.read_bytes()).hexdigest(),
    "parent_stdout_sha256": hashlib.sha256(
        parent_stdout.getvalue().encode()).hexdigest(),
    "lower_restoration_steps": steps,
    "literal_determinant_minus_one_divisible_by_243": True,
    "reduces_exactly_to_AS_seed_mod3": True,
    "total_degree_cap": 7,
    "P_support": support(current_P),
    "Q_support": support(current_Q),
    "target_zero_preimages_mod243": preimages,
    "hensel_traces": hensel_traces,
    "three_distinct_seed_residue_balls": True,
    "scope": "one exact complete fixed-support polynomial map modulo 243",
    "refusal_scope": [
        "one finite depth, not an inverse-compatible infinite tower",
        "no Q3-adic limit, Qbar/C point, counterexample, or JC2 inference",
    ],
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
for step in steps:
    print("degree", step["degree"], "before",
          step["before_div81_mod3_row"], "after",
          step["after_div81_mod3_row"])
print("preimages_mod243", preimages)
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-AS-Q5-SAT-COMPLETE-MOD243-CONSTRUCTION")

