#!/usr/bin/env python3
"""One exact Q7-kernel representative through the Q6 divergence row."""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path

ROOT = Path(os.environ.get("JC2_ROOT", Path(__file__).resolve().parents[2]))
Q7 = (ROOT / "cases/as_fonly_d7_q8_survivor_q7_transition_20260825"
      / "compile_q7_transition.py")
EXPECTED_Q7_SHA = "5e181b09772f5aca83b70acff91a23a0ec60944bfe00c6f5480e36850d5a2941"
payload = Q7.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_Q7_SHA
source = payload.decode()
marker = "\nA, b = affine_matrix(q7_rows, len(names))\n"
assert source.count(marker) == 1
scope = {"__file__": str(Q7), "__name__": "__q7_prefix__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(source.split(marker, 1)[0], str(Q7), "exec"), scope)

q7_rows = scope["q7_rows"]
affine_matrix = scope["affine_matrix"]
restored = scope["restored"]
source_data = scope["source_data"]
new_polynomials = scope["new_polynomials"]
y_polynomials = scope["y_polynomials"]
q9_survivor = scope["q9_survivor"]
q8_survivor = scope["q8_survivor"]
homogeneous_numeric = scope["homogeneous_numeric"]
nadd = scope["nadd"]
nscale = scope["nscale"]
nmul = scope["nmul"]
nderivative = scope["nderivative"]
nbracket = scope["nbracket"]
degree_part = scope["degree_part"]
divide_exact = scope["divide_exact"]
row = scope["row"]


def rref(A, b):
    rows = len(A)
    cols = len(A[0])
    work = [[value % 3 for value in line] + [(-constant) % 3]
            for line, constant in zip(A, b)]
    rank = 0
    pivots = []
    for col in range(cols):
        pivot = next((r for r in range(rank, rows) if work[r][col]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        if work[rank][col] == 2:
            work[rank] = [(2 * value) % 3 for value in work[rank]]
        for r in range(rows):
            if r != rank and work[r][col]:
                scalar = work[r][col]
                work[r] = [(x - scalar * y) % 3
                           for x, y in zip(work[r], work[rank])]
        pivots.append(col)
        rank += 1
    bad = any(all(value == 0 for value in line[:-1]) and line[-1]
              for line in work)
    witness = None
    if not bad:
        answer = [0] * cols
        for r, pivot in enumerate(pivots):
            answer[pivot] = work[r][-1]
        witness = tuple(answer)
    return rank, rank + int(bad), tuple(pivots), work, witness


def kernel_basis(A):
    rank, augmented, pivots, work, witness = rref(A, [0] * len(A))
    assert rank == augmented and witness is not None
    free = [col for col in range(len(A[0])) if col not in pivots]
    basis = []
    for free_col in free:
        vector = [0] * len(A[0])
        vector[free_col] = 1
        for r, pivot in enumerate(pivots):
            vector[pivot] = (-work[r][free_col]) % 3
        basis.append(tuple(vector))
    return rank, tuple(basis)


q7_A, q7_b = affine_matrix(q7_rows, 18)
assert q7_b == [0] * 19
q7_rank, q7_kernel = kernel_basis(q7_A)
assert q7_rank == 9 and len(q7_kernel) == 9
sample_index = int(os.environ["SAMPLE_INDEX"])
assert 0 <= sample_index < 19
if sample_index == 0:
    q7_parameters = [0] * 9
else:
    direction = (sample_index - 1) // 2
    scalar = 1 + (sample_index - 1) % 2
    q7_parameters = [0] * 9
    q7_parameters[direction] = scalar
q7_vector = tuple(sum(q7_parameters[j] * q7_kernel[j][col]
                      for j in range(9)) % 3 for col in range(18))
assert q7_rows(q7_vector) == [0] * 19

h_names = tuple(f"h7_{i}" for i in range(8)) \
    + tuple(f"j7_{i}" for i in range(8))


def q6_rows(values, return_g6=False):
    C2, D2, C4, D4, W7, Z7 = new_polynomials(q9_survivor)
    C3, D3, W4, Z4, W6, Z6 = y_polynomials(q8_survivor)
    C6, D6, W5, Z5 = restored(q7_vector)
    C = nadd(source_data["Cbase"], C2, C3, C4, C6)
    D = nadd(source_data["Dbase"], D2, D3, D4, D6)
    W = nadd(W4, W5, W6, W7)
    Z = nadd(Z4, Z5, Z6, Z7)
    E = nadd(source_data["L1"], source_data["K"],
             nderivative(C, 0), nderivative(D, 1))
    E1_6 = divide_exact(degree_part(E, 6), 3)
    cx, cy = nderivative(C, 0), nderivative(C, 1)
    dx, dy = nderivative(D, 0), nderivative(D, 1)
    M = nadd(nmul(source_data["A"], dy),
             nmul(cx, source_data["vy"]),
             nscale(-1, nmul(source_data["uy"], dx)),
             nscale(-1, nmul(cy, source_data["vx"])))
    F6 = nadd(E1_6, degree_part(M, 6),
              nderivative(W7, 0), nderivative(Z7, 1))
    F1_6 = divide_exact(F6, 3)
    N6 = degree_part(nbracket(C, D), 6)
    T = nadd(nmul(source_data["A"], nderivative(Z, 1)),
             nmul(nderivative(W, 0), source_data["vy"]),
             nscale(-1, nmul(source_data["uy"], nderivative(Z, 0))),
             nscale(-1, nmul(nderivative(W, 1), source_data["vx"])))
    G6 = nadd(F1_6, N6, degree_part(T, 6))
    if return_g6:
        return row(G6, 6)
    assignment = dict(zip(h_names, values))
    H7 = homogeneous_numeric(7, [assignment[f"h7_{i}"]
                                 for i in range(8)])
    J7 = homogeneous_numeric(7, [assignment[f"j7_{i}"]
                                 for i in range(8)])
    target = nadd(G6, nderivative(H7, 0), nderivative(J7, 1))
    return row(target, 6)


A6, b6 = affine_matrix(q6_rows, 16)
rank6, augmented6, _p, _w, witness6 = rref(A6, b6)
assert (rank6, augmented6) == (7, 7) and witness6 is not None
assert q6_rows(witness6) == [0] * 7
output = {
    "sample_index": sample_index,
    "q7_parameters": q7_parameters,
    "q7_vector": list(q7_vector),
    "G6_before_fourth_digit": q6_rows((0,) * 16, return_g6=True),
    "q6_rank_pair": [rank6, augmented6],
    "q6_fiber_dimension": 16 - rank6,
    "q6_witness": list(witness6),
    "matrix_sha256": hashlib.sha256(bytes(
        value % 3 for line in A6 for value in line)).hexdigest(),
    "rhs_sha256": hashlib.sha256(bytes(value % 3 for value in b6)).hexdigest(),
}
encoded = (json.dumps(output, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("sample_index", sample_index)
print("q7_parameters", q7_parameters)
print("G6_before_fourth_digit", output["G6_before_fourth_digit"])
print("q6_rank_pair", output["q6_rank_pair"])
print("q6_fiber_dimension", output["q6_fiber_dimension"])
print("q6_witness", output["q6_witness"])
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-Q7-KERNEL-Q6-SAMPLE")
