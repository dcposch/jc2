#!/usr/bin/env python3
"""Emit a literal fixed-state cap-seven lift formula; execute on AWS only."""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path

import z3


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
scope = {"__file__": str(PARENT_REPLAY), "__name__": "__lift_parent_prefix__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(source.split(marker, 1)[0], str(PARENT_REPLAY), "exec"), scope)

predecessor_names = tuple(scope["predecessor_names"])
canonical_source = scope["canonical_source"]
source_rows = scope["source_rows"]
transition_rows = scope["transition_rows"]
q7_rows = scope["q7_rows"]
state_polynomials = scope["state_polynomials"]
recursive_high = scope["recursive_high"]
direct_high = scope["direct_high"]
nadd = scope["nadd"]
nscale = scope["nscale"]
nmul = scope["nmul"]
nderivative = scope["nderivative"]

survivor_path = Path(os.environ["SURVIVOR_JSON"])
survivor = json.loads(survivor_path.read_text())
assert survivor["status"] == "PASS-DIRECT-INTEGER-SOURCE-REPLAY"
assert survivor["recursive_literal_div243_agreement"] is True
assert survivor["terminal_nonzero_indices"] == []
predecessor_values = survivor["predecessor_values"]
xvalues = survivor["q9_values"]
yvalues = survivor["q8_values"]
rvalues = survivor["q7_values"]
assert (len(predecessor_values), len(xvalues), len(yvalues), len(rvalues)) \
    == (30, 32, 32, 18)
assignment = dict(zip(predecessor_names, predecessor_values))
source_data = canonical_source(assignment)
assert source_rows(source_data, xvalues) == [0] * 23
assert transition_rows(source_data, xvalues, yvalues) == [0] * 22
assert q7_rows(source_data, xvalues, yvalues, rvalues) == [0] * 19
C, D, W, Z, recursive = recursive_high(
    source_data, xvalues, yvalues, rvalues)
assert recursive == direct_high(source_data, C, D, W, Z)
assert not any(value for degree in range(9, 13)
               for value in recursive[degree])

P0 = {(1, 0): 1, (3, 0): -1}
Q0 = {(0, 1): 1}
Pbase = nadd(P0, nscale(3, source_data["U"]), nscale(9, C),
             nscale(27, W))
Qbase = nadd(Q0, nscale(3, source_data["V"]), nscale(9, D),
             nscale(27, Z))

layer_count = int(os.environ["LAYER_COUNT"])
assert 1 <= layer_count <= 8
target_exponent = 4 + layer_count
modulus = 3 ** target_exponent
width = 64
assert (modulus - 1) ** 2 < 2 ** (width - 2)
BV_MOD = z3.BitVecVal(modulus, width)


def bv(value):
    if isinstance(value, int):
        return z3.BitVecVal(value % modulus, width)
    assert z3.is_bv(value) and value.size() == width
    return value


def bred(value):
    return z3.URem(bv(value), BV_MOD)


def badd(*values):
    total = bv(0)
    for value in values:
        total = bred(total + bv(value))
    return total


def bmul(left, right):
    return bred(bv(left) * bv(right))


def bscale(scalar, value):
    return bmul(scalar, value)


def padd(*polys):
    keys = set().union(*(poly.keys() for poly in polys))
    return {key: badd(*(poly.get(key, 0) for poly in polys)) for key in keys}


def pscale(scalar, poly):
    return {key: bscale(scalar, value) for key, value in poly.items()}


def pmul(left, right):
    answer = {}
    for (i, j), a in left.items():
        for (k, ell), b in right.items():
            key = (i + k, j + ell)
            answer[key] = badd(answer.get(key, 0), bmul(a, b))
    return answer


def pderivative(poly, axis):
    answer = {}
    for (i, j), value in poly.items():
        exponent = i if axis == 0 else j
        if exponent:
            key = (i - 1, j) if axis == 0 else (i, j - 1)
            answer[key] = badd(answer.get(key, 0), bscale(exponent, value))
    return answer


monomials = tuple((i, total - i) for total in range(8)
                  for i in range(total + 1))
assert len(monomials) == 36
solver = z3.Solver()
solver.set(timeout=int(os.environ.get("SOLVER_TIMEOUT_MS", "1")))
solver.set(random_seed=0)
digit_vars = []
P = {key: bv(value) for key, value in Pbase.items()}
Q = {key: bv(value) for key, value in Qbase.items()}
for offset in range(layer_count):
    exponent = 4 + offset
    pvars = {key: z3.BitVec(f"digit_{exponent}_p_{key[0]}_{key[1]}", width)
             for key in monomials}
    qvars = {key: z3.BitVec(f"digit_{exponent}_q_{key[0]}_{key[1]}", width)
             for key in monomials}
    for variable in list(pvars.values()) + list(qvars.values()):
        solver.add(z3.ULE(variable, bv(2)))
        digit_vars.append(variable)
    weight = 3 ** exponent
    P = padd(P, pscale(weight, pvars))
    Q = padd(Q, pscale(weight, qvars))

determinant = padd(
    pmul(pderivative(P, 0), pderivative(Q, 1)),
    pscale(-1, pmul(pderivative(P, 1), pderivative(Q, 0))),
    {(0, 0): bv(-1)},
)
for coefficient in determinant.values():
    solver.add(bred(coefficient) == bv(0))

smt2 = solver.to_smt2().encode()
Path(os.environ["SMT2_OUTPUT"]).write_bytes(smt2)
check = solver.check()
result = {
    "solver_status": str(check),
    "solver_timeout_ms": int(os.environ.get("SOLVER_TIMEOUT_MS", "1")),
    "z3_version": z3.get_version_string(),
    "source_parent_sha256": EXPECTED_PARENT_SHA,
    "survivor_json_sha256": hashlib.sha256(survivor_path.read_bytes()).hexdigest(),
    "layer_count": layer_count,
    "new_digit_weights": [3 ** (4 + index) for index in range(layer_count)],
    "target_exponent": target_exponent,
    "target_modulus": modulus,
    "bit_width": width,
    "new_variable_count": len(digit_vars),
    "coefficient_equation_count": len(determinant),
    "smt2_sha256": hashlib.sha256(smt2).hexdigest(),
    "scope": "fixed direct-replayed survivor; literal cap-seven determinant",
}
if check == z3.unknown:
    result["unknown_reason"] = solver.reason_unknown()
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("solver_status", check)
print("layer_count_target", layer_count, target_exponent, modulus)
print("new_variable_count", len(digit_vars))
print("coefficient_equation_count", len(determinant))
print("smt2_sha256", result["smt2_sha256"])
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-AS-SAT-SURVIVOR-DIRECT-LIFT-EMITTER")
