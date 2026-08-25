#!/usr/bin/env python3
"""Exact first unencoded RHS and cap-seven divergence cokernel."""
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
scope = {"__file__": str(PARENT_REPLAY), "__name__": "__adjoint_prefix__"}
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
survivor = json.loads(survivor_path.read_text())
assignment = dict(zip(predecessor_names, survivor["predecessor_values"]))
source_data = canonical_source(assignment)
C, D, W, Z = state_polynomials(
    source_data, survivor["q9_values"], survivor["q8_values"],
    survivor["q7_values"])
P = nadd({(1, 0): 1, (3, 0): -1}, nscale(3, source_data["U"]),
         nscale(9, C), nscale(27, W))
Q = nadd({(0, 1): 1}, nscale(3, source_data["V"]),
         nscale(9, D), nscale(27, Z))
det_minus_one = nadd(
    nmul(nderivative(P, 0), nderivative(Q, 1)),
    nscale(-1, nmul(nderivative(P, 1), nderivative(Q, 0))),
    {(0, 0): -1},
)
assert all(value % 81 == 0 for value in det_minus_one.values())
rhs = {key: (value // 81) % 3 for key, value in det_minus_one.items()
       if (value // 81) % 3}
high = {key: value for key, value in rhs.items() if sum(key) >= 7}
cartier = rhs.get((2, 2), 0)

monomials = tuple((i, total - i) for total in range(8)
                  for i in range(total + 1))
low = tuple((i, total - i) for total in range(7)
            for i in range(total + 1))


def divergence_column(component, key):
    i, j = key
    answer = [0] * len(low)
    if component == "P" and i:
        answer[low.index((i - 1, j))] = i % 3
    if component == "Q" and j:
        answer[low.index((i, j - 1))] = j % 3
    return answer


columns = [divergence_column(component, key)
           for component in ("P", "Q") for key in monomials]
matrix = [[column[row_index] for column in columns]
          for row_index in range(len(low))]


def rank_mod3(rows):
    work = [[value % 3 for value in row] for row in rows]
    rank = 0
    for col in range(len(work[0])):
        pivot = next((r for r in range(rank, len(work)) if work[r][col]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        if work[rank][col] == 2:
            work[rank] = [(2 * value) % 3 for value in work[rank]]
        for r in range(len(work)):
            if r != rank and work[r][col]:
                scalar = work[r][col]
                work[r] = [(x - scalar * y) % 3
                           for x, y in zip(work[r], work[rank])]
        rank += 1
    return rank


rank = rank_mod3(matrix)
rhs_low = [rhs.get(key, 0) for key in low]
augmented_rank = rank_mod3([row + [constant]
                            for row, constant in zip(matrix, rhs_low)])
assert rank == 27
assert augmented_rank == rank + int(cartier != 0)
unhit = [list(key) for key in low
         if key[0] % 3 == 2 and key[1] % 3 == 2]
assert unhit == [[2, 2]]

result = {
    "status": "PASS-FIRST-ADJOINT-ANALYSIS",
    "survivor_json_sha256": hashlib.sha256(survivor_path.read_bytes()).hexdigest(),
    "base_determinant_divisible_by_81": True,
    "first_rhs_mod3": {f"{i},{j}": value
                        for (i, j), value in sorted(rhs.items())},
    "first_rhs_high_degree_ge_7": {f"{i},{j}": value
                                    for (i, j), value in sorted(high.items())},
    "first_rhs_cartier_x2y2": cartier,
    "divergence_matrix_shape": [28, 72],
    "divergence_rank": rank,
    "augmented_rank": augmented_rank,
    "kernel_dimension": 72 - rank,
    "cokernel_basis": [[2, 2]],
    "first_digit_compatible": not high and cartier == 0,
    "matrix_sha256": hashlib.sha256(bytes(
        value for row_values in matrix for value in row_values)).hexdigest(),
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("rhs_high", result["first_rhs_high_degree_ge_7"])
print("rhs_cartier_x2y2", cartier)
print("rank_pair", rank, augmented_rank)
print("first_digit_compatible", result["first_digit_compatible"])
print("matrix_sha256", result["matrix_sha256"])
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-AS-SAT-SURVIVOR-FIRST-ADJOINT")
