#!/usr/bin/env python3
"""Exact shard of all Q7-kernel states through next high carry."""
from __future__ import annotations

import contextlib
import hashlib
import io
import itertools
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

source_data = scope["source_data"]
q9_survivor = scope["q9_survivor"]
q8_survivor = scope["q8_survivor"]
q7_rows = scope["q7_rows"]
affine_matrix = scope["affine_matrix"]
restored = scope["restored"]
new_polynomials = scope["new_polynomials"]
y_polynomials = scope["y_polynomials"]
homogeneous_numeric = scope["homogeneous_numeric"]
nadd = scope["nadd"]
nscale = scope["nscale"]
nmul = scope["nmul"]
nderivative = scope["nderivative"]
nbracket = scope["nbracket"]
degree_part = scope["degree_part"]
divide_exact = scope["divide_exact"]
row = scope["row"]


def rref_kernel(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    work = [[value % 3 for value in line] for line in matrix]
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
    free = [col for col in range(cols) if col not in pivots]
    basis = []
    for free_col in free:
        vector = [0] * cols
        vector[free_col] = 1
        for r, pivot in enumerate(pivots):
            vector[pivot] = (-work[r][free_col]) % 3
        basis.append(tuple(vector))
    return rank, tuple(basis)


q7_A, q7_b = affine_matrix(q7_rows, 18)
assert q7_b == [0] * 19
q7_rank, q7_kernel = rref_kernel(q7_A)
assert q7_rank == 9 and len(q7_kernel) == 9
kernel_payload = bytes(value for vector in q7_kernel for value in vector)
kernel_sha = hashlib.sha256(kernel_payload).hexdigest()


def q6_divergence(values):
    H = homogeneous_numeric(7, values[:8])
    J = homogeneous_numeric(7, values[8:])
    return row(nadd(nderivative(H, 0), nderivative(J, 1)), 6)


q6_columns = []
for which in range(16):
    values = [0] * 16
    values[which] = 1
    q6_columns.append(q6_divergence(values))
q6_matrix = [[q6_columns[column][line] for column in range(16)]
             for line in range(7)]
q6_rank, q6_kernel = rref_kernel(q6_matrix)
assert q6_rank == 7 and len(q6_kernel) == 9


def ternary(index, width=9):
    values = []
    for _ in range(width):
        values.append(index % 3)
        index //= 3
    assert index == 0
    return tuple(values)


def q7_vector(parameters):
    return tuple(sum(parameters[j] * q7_kernel[j][col]
                     for j in range(9)) % 3 for col in range(18))


def state_polynomials(parameters):
    vector = q7_vector(parameters)
    C2, D2, C4, D4, W7, Z7 = new_polynomials(q9_survivor)
    C3, D3, W4, Z4, W6, Z6 = y_polynomials(q8_survivor)
    C6, D6, W5, Z5 = restored(vector)
    C = nadd(source_data["Cbase"], C2, C3, C4, C6)
    D = nadd(source_data["Dbase"], D2, D3, D4, D6)
    W = nadd(W4, W5, W6, W7)
    Z = nadd(Z4, Z5, Z6, Z7)
    return vector, C, D, W, Z


def recursive_rows(parameters):
    vector, C, D, W, Z = state_polynomials(parameters)
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
    result = {}
    for degree in range(7, 13):
        E1d = divide_exact(degree_part(E, degree), 3)
        Fd = nadd(E1d, degree_part(M, degree),
                  degree_part(nadd(nderivative(W, 0),
                                   nderivative(Z, 1)), degree))
        F1d = divide_exact(Fd, 3)
        Gd = nadd(F1d, degree_part(N, degree), degree_part(T, degree))
        G1d = divide_exact(Gd, 3)
        result[degree] = row(nadd(G1d, degree_part(Rmix, degree)), degree)
    return vector, C, D, W, Z, result


def direct_rows(C, D, W, Z):
    P0 = {(1, 0): 1, (3, 0): -1}
    Q0 = {(0, 1): 1}
    P = nadd(P0, nscale(3, source_data["U"]), nscale(9, C),
             nscale(27, W))
    Q = nadd(Q0, nscale(3, source_data["V"]), nscale(9, D),
             nscale(27, Z))
    det_minus_one = nadd(
        nmul(nderivative(P, 0), nderivative(Q, 1)),
        nscale(-1, nmul(nderivative(P, 1), nderivative(Q, 0))),
        {(0, 0): -1},
    )
    return {degree: row(divide_exact(
        degree_part(det_minus_one, degree), 243), degree)
        for degree in range(7, 13)}


# Fourth-digit H7,J7 dependence has degree at most eight in the next carry.
q6_high_support = []
for which in range(16):
    values = [0] * 16
    values[which] = 1
    H = homogeneous_numeric(7, values[:8])
    J = homogeneous_numeric(7, values[8:])
    S = nadd(nmul(source_data["A"], nderivative(J, 1)),
             nmul(nderivative(H, 0), source_data["vy"]),
             nscale(-1, nmul(source_data["uy"], nderivative(J, 0))),
             nscale(-1, nmul(nderivative(H, 1), source_data["vx"])))
    support = sorted(sum(xy) for xy, value in S.items() if value % 3)
    q6_high_support.append(support)
    assert all(degree <= 8 for degree in support)

shard_count = int(os.environ["SHARD_COUNT"])
shard_index = int(os.environ["SHARD_INDEX"])
assert shard_count == 27 and 0 <= shard_index < shard_count
records = []
for index in range(shard_index, 3 ** 9, shard_count):
    parameters = ternary(index)
    vector, C, D, W, Z, recursive = recursive_rows(parameters)
    direct = direct_rows(C, D, W, Z)
    assert recursive == direct
    high = tuple(value for degree in range(12, 8, -1)
                 for value in recursive[degree])
    records.append({"index": index, "high": list(high),
                    "r8": recursive[8]})

output = {
    "shard_count": shard_count,
    "shard_index": shard_index,
    "state_count": len(records),
    "q7_rank": q7_rank,
    "q7_kernel_sha256": kernel_sha,
    "q6_rank": q6_rank,
    "q6_kernel_dimension": len(q6_kernel),
    "q6_high_support_by_basis": q6_high_support,
    "records": records,
}
encoded = (json.dumps(output, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("shard", shard_index, shard_count)
print("state_count", len(records))
print("q7_rank_kernel", q7_rank, len(q7_kernel), kernel_sha)
print("q6_rank_kernel", q6_rank, len(q6_kernel))
print("q6_high_max_degree", max(max(x, default=-1)
                                 for x in q6_high_support))
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-Q7KERNEL-NEXT-HIGH-SHARD")
