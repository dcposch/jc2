#!/usr/bin/env python3
"""Emit a raw-coordinate, state-complete Q2/Q1 QF_BV formula."""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path

import z3


ROOT = Path(os.environ["JC2_ROOT"])
V1 = (ROOT / "cases/as_fonly_d7_q3_two_level_q2_q1_20260825"
      / "solve_two_level.py")
EXPECTED_V1 = "cec50f9fd9bf9ce3311e5687658473e9c4d7577b4997ac96b1e1f3b3932d2fcd"
payload = V1.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_V1
marker = b"\nstages = []\n"
assert payload.count(marker) == 1
ns = {"__file__": str(V1), "__name__": "__state_complete_prefix__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(payload.split(marker, 1)[0] + b"\n", str(V1), "exec"), ns)

q3_candidate = ns["q3_candidate"]
q3_particular = ns["q3_particular"]
q3_kernel = ns["q3_kernel"]
q3_kdim = ns["q3_kdim"]
assert len(q3_kernel) == q3_kdim

WIDTH = 32
MODULUS = 729
assert 728 * 728 < 2 ** 20 < 2 ** WIDTH
BV_MOD = z3.BitVecVal(MODULUS, WIDTH)

def bv(value):
    if isinstance(value, int):
        return z3.BitVecVal(value % MODULUS, WIDTH)
    assert z3.is_bv(value) and value.size() == WIDTH
    return value

def bred(value):
    return z3.URem(bv(value), BV_MOD)

def badd(*values):
    answer = bv(0)
    for value in values:
        answer = bred(answer + bv(value))
    return answer

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

def pbracket(left, right):
    return padd(pmul(pderivative(left, 0), pderivative(right, 1)),
                pscale(-1, pmul(pderivative(left, 1),
                                pderivative(right, 0))))

def homogeneous(degree, values):
    assert len(values) == degree + 1
    return {(index, degree - index): bv(value)
            for index, value in enumerate(values)}

solver = z3.Solver()
solver.set(timeout=int(os.environ.get("EMITTER_TIMEOUT_MS", "1")))
solver.set(random_seed=0)
three = bv(3)
two43 = bv(243)

q3_coordinates = [z3.BitVec(f"q3_{index}", WIDTH)
                  for index in range(q3_kdim)]
fresh_names = []
fresh = []
for prefix, degree in (("w3", 3), ("z3", 3), ("w2", 2), ("z2", 2),
                       ("h3", 3), ("j3", 3), ("h2", 2), ("j2", 2)):
    block = []
    for index in range(degree + 1):
        name = f"{prefix}_{index}"
        fresh_names.append(name)
        variable = z3.BitVec(name, WIDTH)
        fresh.append(variable)
        block.append(variable)
all_variables = q3_coordinates + fresh
for variable in all_variables:
    solver.add(z3.ULE(variable, bv(2)))

q3_values = []
for column in range(len(q3_particular)):
    value = bv(q3_particular[column])
    for coordinate, vector in zip(q3_coordinates, q3_kernel):
        value = badd(value, bmul(coordinate, vector[column]))
    q3_values.append(z3.URem(value, three))

# Call the pinned source candidate with symbolic polynomial primitives.  The
# function's only scalar reduction is `% 3` on nonnegative, small bit-vectors.
source_globals = q3_candidate.__globals__
source_globals["nadd"] = padd
source_globals["nscale"] = pscale
source_globals["homogeneous_numeric"] = homogeneous
P, Q, q4_values, h4_values, j4_values = q3_candidate(q3_values)

offset = 0
blocks = {}
for prefix, degree in (("W3", 3), ("Z3", 3), ("W2", 2), ("Z2", 2),
                       ("H3", 3), ("J3", 3), ("H2", 2), ("J2", 2)):
    width = degree + 1
    blocks[prefix] = fresh[offset:offset + width]
    offset += width
assert offset == len(fresh) == 28
P = padd(P, pscale(27, padd(homogeneous(3, blocks["W3"]),
                            homogeneous(2, blocks["W2"]))),
         pscale(81, padd(homogeneous(3, blocks["H3"]),
                         homogeneous(2, blocks["H2"]))))
Q = padd(Q, pscale(27, padd(homogeneous(3, blocks["Z3"]),
                            homogeneous(2, blocks["Z2"]))),
         pscale(81, padd(homogeneous(3, blocks["J3"]),
                         homogeneous(2, blocks["J2"]))))
determinant = padd(pbracket(P, Q), {(0, 0): bv(-1)})

slots = [(i, total - i) for total in range(13)
         for i in range(total + 1)]
high_slots = [xy for xy in slots if 7 <= sum(xy) <= 12]
assert len(slots) == 91 and len(high_slots) == 63
for xy in slots:
    solver.add(z3.URem(determinant.get(xy, bv(0)), two43) == bv(0))
omit_high = os.environ.get("OMIT_HIGH", "0") == "1"
if not omit_high:
    for xy in high_slots:
        solver.add(determinant.get(xy, bv(0)) == bv(0))
solver.add(determinant.get((0, 0), bv(0)) == bv(0))

smt2 = solver.to_smt2().encode()
Path(os.environ["SMT2_OUTPUT"]).write_bytes(smt2)
check = solver.check()
result = {
    "status": "PASS-AS-Q3-STATE-COMPLETE-BV-EMITTER",
    "solver_status_at_emitter_timeout": str(check),
    "v1_sha256": EXPECTED_V1,
    "model_sha256": hashlib.sha256(
        Path(os.environ["MODEL_OUTPUT"]).read_bytes()).hexdigest(),
    "q3_kernel_dimension": q3_kdim,
    "q3_coordinate_count": len(q3_coordinates),
    "fresh_digit_count": len(fresh),
    "total_trit_count": len(all_variables),
    "determinant_row_count_mod243": len(slots),
    "high_row_count_mod729": 0 if omit_high else len(high_slots),
    "omit_high": omit_high,
    "width": WIDTH, "modulus": MODULUS,
    "largest_reduced_gate_product": 728 * 728,
    "smt2_sha256": hashlib.sha256(smt2).hexdigest(),
    "scope": "one complete displayed Q3 affine fibre; fixed D7 finite precision",
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("q3_kernel", q3_kdim, "fresh", len(fresh), "total", len(all_variables))
print("rows", len(slots), 0 if omit_high else len(high_slots),
      "omit_high", omit_high)
print("smt2_sha256", result["smt2_sha256"])
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])
