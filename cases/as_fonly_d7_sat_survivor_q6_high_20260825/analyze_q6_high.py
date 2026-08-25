#!/usr/bin/env python3
"""Exact Q6/H7,J7 and divided degree-12..7 affine gate; AWS only."""
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
scope = {"__file__": str(PARENT_REPLAY), "__name__": "__q6_high_prefix__"}
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
homogeneous_numeric = scope["homogeneous_numeric"]
nadd = scope["nadd"]
nscale = scope["nscale"]
nmul = scope["nmul"]
nderivative = scope["nderivative"]
nbracket = scope["nbracket"]
degree_part = scope["degree_part"]
divide_exact = scope["divide_exact"]
row = scope["row"]

survivor_path = Path(os.environ["SURVIVOR_JSON"])
survivor = json.loads(survivor_path.read_text())
assignment = dict(zip(predecessor_names, survivor["predecessor_values"]))
source_data = canonical_source(assignment)
xvalues = survivor["q9_values"]
yvalues = survivor["q8_values"]
rvalues = survivor["q7_values"]
assert source_rows(source_data, xvalues) == [0] * 23
assert transition_rows(source_data, xvalues, yvalues) == [0] * 22
assert q7_rows(source_data, xvalues, yvalues, rvalues) == [0] * 19
C, D, W, Z = state_polynomials(source_data, xvalues, yvalues, rvalues)
_C, _D, _W, _Z, prior_high = recursive_high(
    source_data, xvalues, yvalues, rvalues)
assert (C, D, W, Z) == (_C, _D, _W, _Z)
assert prior_high == direct_high(source_data, C, D, W, Z)
assert not any(value for degree in range(9, 13)
               for value in prior_high[degree])


def core():
    E = nadd(source_data["L1"], source_data["K"],
             nderivative(C, 0), nderivative(D, 1))
    cx, cy = nderivative(C, 0), nderivative(C, 1)
    dx, dy = nderivative(D, 0), nderivative(D, 1)
    M = nadd(nmul(source_data["A"], dy),
             nmul(cx, source_data["vy"]),
             nscale(-1, nmul(source_data["uy"], dx)),
             nscale(-1, nmul(cy, source_data["vx"])))
    N = nbracket(C, D)
    T = nadd(nmul(source_data["A"], nderivative(Z, 1)),
             nmul(nderivative(W, 0), source_data["vy"]),
             nscale(-1, nmul(source_data["uy"], nderivative(Z, 0))),
             nscale(-1, nmul(nderivative(W, 1), source_data["vx"])))
    Rmix = nadd(nmul(cx, nderivative(Z, 1)),
                nmul(nderivative(W, 0), dy),
                nscale(-1, nmul(cy, nderivative(Z, 0))),
                nscale(-1, nmul(nderivative(W, 1), dx)))
    return E, M, N, T, Rmix


E, M, N, T, Rmix = core()
divWZ = nadd(nderivative(W, 0), nderivative(Z, 1))


def equations(values, include_blocks=False):
    assert len(values) == 16
    H = homogeneous_numeric(7, values[:8])
    J = homogeneous_numeric(7, values[8:])
    E1_6 = divide_exact(degree_part(E, 6), 3)
    F6 = nadd(E1_6, degree_part(M, 6), degree_part(divWZ, 6))
    F1_6 = divide_exact(F6, 3)
    G6 = nadd(F1_6, degree_part(N, 6), degree_part(T, 6),
              nderivative(H, 0), nderivative(J, 1))
    source6 = row(G6, 6)

    S = nadd(nmul(source_data["A"], nderivative(J, 1)),
             nmul(nderivative(H, 0), source_data["vy"]),
             nscale(-1, nmul(source_data["uy"], nderivative(J, 0))),
             nscale(-1, nmul(nderivative(H, 1), source_data["vx"])))
    divided = {}
    for degree in range(7, 13):
        E1 = divide_exact(degree_part(E, degree), 3)
        F = nadd(E1, degree_part(M, degree), degree_part(divWZ, degree))
        F1 = divide_exact(F, 3)
        G = nadd(F1, degree_part(N, degree), degree_part(T, degree))
        bad_G = {key: value for key, value in G.items() if value % 3}
        if bad_G:
            raise AssertionError(("nonexact_G_division", degree, bad_G))
        G1 = divide_exact(G, 3)
        divided[degree] = row(nadd(G1, degree_part(S, degree),
                                   degree_part(Rmix, degree)), degree)
    flat = source6 + [value for degree in range(12, 6, -1)
                      for value in divided[degree]]
    if include_blocks:
        return flat, source6, divided, S
    return flat


zero, source6_zero, divided_zero, _S0 = equations((0,) * 16, True)
columns = []
for which in range(16):
    values = [0] * 16
    values[which] = 1
    evaluated = equations(values)
    columns.append([(value - base) % 3
                    for value, base in zip(evaluated, zero)])
matrix = [[columns[column][line] for column in range(16)]
          for line in range(len(zero))]
rhs = [(-value) % 3 for value in zero]


def rref(A, b):
    work = [[value % 3 for value in line] + [constant % 3]
            for line, constant in zip(A, b)]
    rank = 0
    pivots = []
    provenance = [[1 if i == j else 0 for j in range(len(A))]
                  for i in range(len(A))]
    for col in range(len(A[0])):
        pivot = next((r for r in range(rank, len(work)) if work[r][col]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        provenance[rank], provenance[pivot] = provenance[pivot], provenance[rank]
        if work[rank][col] == 2:
            work[rank] = [(2 * value) % 3 for value in work[rank]]
            provenance[rank] = [(2 * value) % 3 for value in provenance[rank]]
        for r in range(len(work)):
            if r != rank and work[r][col]:
                scalar = work[r][col]
                work[r] = [(x - scalar * y) % 3
                           for x, y in zip(work[r], work[rank])]
                provenance[r] = [(x - scalar * y) % 3
                                 for x, y in zip(provenance[r], provenance[rank])]
        pivots.append(col)
        rank += 1
    contradiction = next((r for r, line in enumerate(work)
                          if not any(line[:-1]) and line[-1]), None)
    augmented = rank + int(contradiction is not None)
    witness = None
    kernel = []
    if contradiction is None:
        witness = [0] * len(A[0])
        for r, pivot in enumerate(pivots):
            witness[pivot] = work[r][-1]
        free = [col for col in range(len(A[0])) if col not in pivots]
        for free_col in free:
            vector = [0] * len(A[0])
            vector[free_col] = 1
            for r, pivot in enumerate(pivots):
                vector[pivot] = (-work[r][free_col]) % 3
            kernel.append(vector)
    left_null = provenance[contradiction] if contradiction is not None else None
    return rank, augmented, pivots, witness, kernel, left_null


rank, augmented, pivots, witness, kernel, left_null = rref(matrix, rhs)
if witness is not None:
    assert not any(equations(witness))
    _flat, witness_source6, witness_divided, witness_S = equations(witness, True)
else:
    witness_source6 = None
    witness_divided = None
    witness_S = None
if left_null is not None:
    assert all(sum(left_null[r] * matrix[r][c] for r in range(len(matrix))) % 3
               == 0 for c in range(16))
    pairing = sum(left_null[r] * rhs[r] for r in range(len(rhs))) % 3
    assert pairing != 0
else:
    pairing = 0

row_labels = ([f"Q6:x^{i}y^{6-i}" for i in range(7)]
              + [f"R{degree}:x^{i}y^{degree-i}"
                 for degree in range(12, 6, -1)
                 for i in range(degree + 1)])
assert len(row_labels) == len(zero) == 70
active_left = ({row_labels[index]: value for index, value in enumerate(left_null)
                if value} if left_null is not None else {})
S_support_degrees = sorted({sum(key) for key, value in equations(
    [1] + [0] * 15, True)[3].items() if value % 3})

result = {
    "status": "PASS-Q6-HIGH-AFFINE-GATE",
    "survivor_json_sha256": hashlib.sha256(survivor_path.read_bytes()).hexdigest(),
    "equation_shape": [70, 16],
    "block_shapes": {"Q6": 7, "R12_to_R7": 63},
    "rank_pair": [rank, augmented],
    "solution_dimension": 16 - rank if witness is not None else None,
    "pivots": pivots,
    "canonical_witness": witness,
    "kernel_basis": kernel,
    "constant_Q6": source6_zero,
    "constant_R12_to_R7": {str(degree): divided_zero[degree]
                              for degree in range(12, 6, -1)},
    "witness_Q6": witness_source6,
    "witness_R12_to_R7": ({str(degree): witness_divided[degree]
                             for degree in range(12, 6, -1)}
                            if witness_divided is not None else None),
    "left_null_active_rows": active_left,
    "left_null_rhs_pairing": pairing,
    "matrix_sha256": hashlib.sha256(bytes(
        value for line in matrix for value in line)).hexdigest(),
    "rhs_sha256": hashlib.sha256(bytes(rhs)).hexdigest(),
    "H7J7_effect_sample_support_degrees": S_support_degrees,
    "compatible": witness is not None,
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("equation_shape", 70, 16)
print("rank_pair", rank, augmented)
print("compatible", witness is not None)
print("solution_dimension", result["solution_dimension"])
print("canonical_witness", witness)
print("left_null_active_rows", active_left)
print("left_null_rhs_pairing", pairing)
print("matrix_sha256", result["matrix_sha256"])
print("rhs_sha256", result["rhs_sha256"])
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-AS-SAT-SURVIVOR-Q6-HIGH")
