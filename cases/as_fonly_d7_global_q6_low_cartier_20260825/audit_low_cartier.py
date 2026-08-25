#!/usr/bin/env python3
"""Direct low-Cartier successor for a global Q6/high SAT witness."""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
PARENT = (ROOT / "cases/as_fonly_d7_global_q6_high_20260825"
          / "replay_global_q6_high.py")
EXPECTED_PARENT_SHA = (
    "e8361c81609afe6365d5eba8d4fda9bdf4b3dd4a44869fbcba330c614847c77c")
payload = PARENT.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_PARENT_SHA

result_dir = Path(os.environ["RESULT_DIR"])
result_dir.mkdir(parents=True, exist_ok=True)
parent_output = result_dir / "parent_replay.json"
old_output = os.environ.get("OUTPUT_JSON")
os.environ["OUTPUT_JSON"] = str(parent_output)
scope = {"__file__": str(PARENT), "__name__": "__low_cartier_parent__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(payload, str(PARENT), "exec"), scope)
if old_output is None:
    del os.environ["OUTPUT_JSON"]
else:
    os.environ["OUTPUT_JSON"] = old_output

nadd = scope["nadd"]
nscale = scope["nscale"]
nmul = scope["nmul"]
nderivative = scope["nderivative"]
degree_part = scope["degree_part"]
P = scope["P"]
Q = scope["Q"]
det_minus_one = scope["det_minus_one"]


def monomials_upto(degree):
    return [(i, total - i) for total in range(degree + 1)
            for i in range(total + 1)]


def exact_quotient(poly, divisor):
    bad = {key: value for key, value in poly.items() if value % divisor}
    assert not bad, (divisor, sorted(bad.items())[:10])
    return {key: value // divisor for key, value in poly.items()}


def determinant_minus_one(left, right):
    return nadd(nmul(nderivative(left, 0), nderivative(right, 1)),
                nscale(-1, nmul(nderivative(left, 1),
                                nderivative(right, 0))),
                {(0, 0): -1})


def rank_mod3(matrix):
    work = [[entry % 3 for entry in row] for row in matrix]
    rank = 0
    for column in range(len(work[0])):
        pivot = next((index for index in range(rank, len(work))
                      if work[index][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = 1 if work[rank][column] == 1 else 2
        work[rank] = [(inverse * entry) % 3 for entry in work[rank]]
        for index in range(len(work)):
            if index == rank:
                continue
            scalar = work[index][column]
            if scalar:
                work[index] = [
                    (left - scalar * right) % 3
                    for left, right in zip(work[index], work[rank])]
        rank += 1
        if rank == len(work):
            break
    return rank


rows = monomials_upto(6)
variables = [(side, key) for side in (0, 1)
             for key in monomials_upto(7)]
matrix = []
for target in rows:
    entries = []
    for side, (i, j) in variables:
        if side == 0:
            entries.append(i if i and (i - 1, j) == target else 0)
        else:
            entries.append(j if j and (i, j - 1) == target else 0)
    matrix.append(entries)
divergence_rank = rank_mod3(matrix)
assert (len(rows), len(variables), divergence_rank) == (28, 72, 27)
cokernel_rows = [key for key, entries in zip(rows, matrix)
                 if all(entry % 3 == 0 for entry in entries)]
assert cokernel_rows == [(2, 2)]

R = exact_quotient(det_minus_one, 243)
high_parent = {
    str(degree): [R.get((i, degree - i), 0) % 3
                  for i in range(degree + 1)]
    for degree in range(7, 13)
}
assert all(not any(values) for values in high_parent.values())
low_R = {f"{i},{j}": R.get((i, j), 0) % 3 for i, j in rows}
cartier_R = R.get((2, 2), 0) % 3

K = {}
L = {}
unsolved = {}
for i, j in rows:
    residual = R.get((i, j), 0) % 3
    if not residual:
        continue
    if (i + 1) % 3:
        K[(i + 1, j)] = (-residual * pow(i + 1, -1, 3)) % 3
    elif (j + 1) % 3:
        L[(i, j + 1)] = (-residual * pow(j + 1, -1, 3)) % 3
    else:
        unsolved[(i, j)] = residual
assert unsolved == ({(2, 2): cartier_R} if cartier_R else {})

result = {
    "status": "CARTIER-OBSTRUCTED" if cartier_R else "CANONICAL-LIFT-PASS",
    "parent_model_sha256": hashlib.sha256(
        Path(os.environ["MODEL_OUTPUT"]).read_bytes()).hexdigest(),
    "parent_replay_sha256": hashlib.sha256(parent_output.read_bytes()).hexdigest(),
    "row_count_low": len(rows),
    "raw_digit_variable_count": len(variables),
    "divergence_rank": divergence_rank,
    "divergence_kernel_dimension": len(variables) - divergence_rank,
    "cokernel_rows": [list(key) for key in cokernel_rows],
    "low_R_mod3": low_R,
    "cartier_R_x2y2": cartier_R,
    "canonical_K": {f"{i},{j}": value for (i, j), value in sorted(K.items())},
    "canonical_L": {f"{i},{j}": value for (i, j), value in sorted(L.items())},
    "parent_terminal_rows_degrees_7_to_12": high_parent,
    "complete_map_mod729": False,
}

if not cartier_R:
    divergence = nadd(nderivative(K, 0), nderivative(L, 1))
    for key in rows:
        assert (R.get(key, 0) + divergence.get(key, 0)) % 3 == 0
    P729 = nadd(P, nscale(243, K))
    Q729 = nadd(Q, nscale(243, L))
    det729 = determinant_minus_one(P729, Q729)
    S = exact_quotient(det729, 729)
    result["complete_map_mod729"] = True
    result["P729"] = {f"{i},{j}": value for (i, j), value in sorted(P729.items())
                       if value}
    result["Q729"] = {f"{i},{j}": value for (i, j), value in sorted(Q729.items())
                       if value}
    result["next_terminal_rows_degrees_7_to_12"] = {
        str(degree): [S.get((i, degree - i), 0) % 3
                      for i in range(degree + 1)]
        for degree in range(7, 13)
    }
    result["next_low_cartier_x2y2"] = S.get((2, 2), 0) % 3
    result["next_quotient_support_mod3"] = {
        f"{i},{j}": value % 3 for (i, j), value in sorted(S.items())
        if value % 3
    }

encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
output = Path(os.environ["OUTPUT_JSON"])
output.write_bytes(encoded)
print("parent_model_sha256", result["parent_model_sha256"])
print("divergence_shape_rank_kernel", len(rows), len(variables),
      divergence_rank, len(variables) - divergence_rank)
print("cokernel_rows", cokernel_rows)
print("cartier_R_x2y2", cartier_R)
print("complete_map_mod729", result["complete_map_mod729"])
if result["complete_map_mod729"]:
    print("next_low_cartier_x2y2", result["next_low_cartier_x2y2"])
    print("next_terminal_nonzero_count", sum(
        bool(value) for values in result["next_terminal_rows_degrees_7_to_12"].values()
        for value in values))
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-AS-GLOBAL-Q6-LOW-CARTIER-AUDIT")

