#!/usr/bin/env python3
"""Literal-integer replay and next Cartier/high obstruction for a SAT lift."""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
PARENT_REPLAY = (ROOT / "cases/as_fonly_d7_global_predecessor_rawq7_20260825"
                 / "replay_model.py")
EXPECTED_PARENT_SHA = (
    "b4acf93af94774e124502f3b6cd20be40b10197a808eb7b8ad0d7c92395b99d4")
payload = PARENT_REPLAY.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_PARENT_SHA
source = payload.decode()
marker = '\nmodel_path = Path(os.environ["MODEL_OUTPUT"])\n'
assert source.count(marker) == 1
scope = {"__file__": str(PARENT_REPLAY), "__name__": "__lift_replay_prefix__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(source.split(marker, 1)[0], str(PARENT_REPLAY), "exec"), scope)

predecessor_names = tuple(scope["predecessor_names"])
canonical_source = scope["canonical_source"]
state_polynomials = scope["state_polynomials"]
nadd = scope["nadd"]
nscale = scope["nscale"]
nmul = scope["nmul"]
nderivative = scope["nderivative"]

survivor_path = Path(os.environ["SURVIVOR_JSON"])
model_path = Path(os.environ["MODEL_OUTPUT"])
survivor = json.loads(survivor_path.read_text())
layer_count = int(os.environ["LAYER_COUNT"])
assert 1 <= layer_count <= 8
target_exponent = 4 + layer_count
target = 3 ** target_exponent

assignment = dict(zip(predecessor_names, survivor["predecessor_values"]))
source_data = canonical_source(assignment)
C, D, W, Z = state_polynomials(
    source_data, survivor["q9_values"], survivor["q8_values"],
    survivor["q7_values"])
P = nadd({(1, 0): 1, (3, 0): -1}, nscale(3, source_data["U"]),
         nscale(9, C), nscale(27, W))
Q = nadd({(0, 1): 1}, nscale(3, source_data["V"]),
         nscale(9, D), nscale(27, Z))

model = {}
for line in model_path.read_text().splitlines():
    fields = line.split()
    if len(fields) == 2 and fields[0].startswith("digit_"):
        assert fields[0] not in model
        model[fields[0]] = int(fields[1])

monomials = tuple((i, total - i) for total in range(8)
                  for i in range(total + 1))
digits = []
expected = set()
for offset in range(layer_count):
    exponent = 4 + offset
    p_digit = {}
    q_digit = {}
    for i, j in monomials:
        p_name = f"digit_{exponent}_p_{i}_{j}"
        q_name = f"digit_{exponent}_q_{i}_{j}"
        expected.update((p_name, q_name))
        p_digit[(i, j)] = model[p_name]
        q_digit[(i, j)] = model[q_name]
    assert all(0 <= value <= 2
               for value in list(p_digit.values()) + list(q_digit.values()))
    weight = 3 ** exponent
    P = nadd(P, nscale(weight, p_digit))
    Q = nadd(Q, nscale(weight, q_digit))
    digits.append({
        "exponent": exponent,
        "weight": weight,
        "P": [p_digit[key] for key in monomials],
        "Q": [q_digit[key] for key in monomials],
    })
assert set(model) == expected

det_minus_one = nadd(
    nmul(nderivative(P, 0), nderivative(Q, 1)),
    nscale(-1, nmul(nderivative(P, 1), nderivative(Q, 0))),
    {(0, 0): -1},
)
assert all(value % target == 0 for value in det_minus_one.values())
quotient = {key: value // target for key, value in det_minus_one.items()}
quotient_mod3 = {key: value % 3 for key, value in quotient.items()
                 if value % 3}
high = {key: value for key, value in quotient_mod3.items()
        if sum(key) >= 7}
cartier = quotient_mod3.get((2, 2), 0)
next_obstruction = ({f"{i},{j}": value for (i, j), value in sorted(high.items())}
                    | {"2,2": cartier})
next_zero = not high and cartier == 0

# Universal cap-seven divergence: all degree-at-most-six monomials except
# x^2*y^2 are hit; its rank is therefore 27 over F3.
low_monomials = [(i, total - i) for total in range(7)
                 for i in range(total + 1)]
assert len(low_monomials) == 28
unhit = [(i, j) for i, j in low_monomials
         if i % 3 == 2 and j % 3 == 2]
assert unhit == [(2, 2)]

result = {
    "status": "PASS-DIRECT-INTEGER-LIFT-REPLAY",
    "survivor_json_sha256": hashlib.sha256(survivor_path.read_bytes()).hexdigest(),
    "solver_model_sha256": hashlib.sha256(model_path.read_bytes()).hexdigest(),
    "layer_count": layer_count,
    "target_exponent": target_exponent,
    "target_modulus": target,
    "digit_monomial_order": [list(key) for key in monomials],
    "digits": digits,
    "determinant_coefficient_count": len(det_minus_one),
    "determinant_divisible_by_target": True,
    "next_quotient_mod3": {f"{i},{j}": value
                             for (i, j), value in sorted(quotient_mod3.items())},
    "next_high_nonzero": {f"{i},{j}": value
                            for (i, j), value in sorted(high.items())},
    "next_cartier_x2y2": cartier,
    "next_obstruction_zero": next_zero,
    "next_digit_divergence_rank": 27,
    "next_digit_kernel_dimension": 72 - 27,
    "next_digit_cokernel_basis_within_degree_le_6": [[2, 2]],
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("target_exponent_modulus", target_exponent, target)
print("digit_layers", layer_count)
print("determinant_coefficient_count", len(det_minus_one))
print("next_high_nonzero", result["next_high_nonzero"])
print("next_cartier_x2y2", cartier)
print("next_obstruction_zero", next_zero)
print("solver_model_sha256", result["solver_model_sha256"])
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-AS-SAT-SURVIVOR-DIRECT-LIFT-REPLAY")
