#!/usr/bin/env python3
"""Exact Q8-survivor to Q7 affine transition over F3."""
from __future__ import annotations

import contextlib
import hashlib
import io
import os
from pathlib import Path

ROOT = Path(os.environ.get("JC2_ROOT", Path(__file__).resolve().parents[2]))
V1 = (ROOT / "cases/as_fonly_d7_q9_kuranishi_q8_20260825"
      / "compile_witness.py")
EXPECTED_V1_SHA = "fbf327fb04beb2fa929f3b46a5df035244ec838793bc1f596801935adae09d4b"
payload = V1.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_V1_SHA
source = payload.decode()
marker = "\nA22, b22 = matrix_and_rhs(transition_rows, q9_vector, len(y_names))\n"
assert source.count(marker) == 1
scope = {"__file__": str(V1), "__name__": "__q8_v1_prefix__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(source.split(marker, 1)[0], str(V1), "exec"), scope)

source_data = scope["source_data"]
source_rows = scope["source_rows"]
transition_rows = scope["transition_rows"]
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

q9_survivor = (
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0,
)
q8_survivor = (0,) * 32
assert source_rows(source_data, q9_survivor) == [0] * 23
assert transition_rows(q9_survivor, q8_survivor) == [0] * 22

names = ("c6_0", "c6_3", "c6_6", "d6_0", "d6_3", "d6_6") \
    + tuple(f"w5_{i}" for i in range(6)) \
    + tuple(f"z5_{i}" for i in range(6))
assert len(names) == 18


def restored(values):
    assignment = dict(zip(names, values))
    C6 = homogeneous_numeric(6, [
        assignment["c6_0"], 0, 0, assignment["c6_3"], 0, 0,
        assignment["c6_6"]])
    D6 = homogeneous_numeric(6, [
        assignment["d6_0"], 0, 0, assignment["d6_3"], 0, 0,
        assignment["d6_6"]])
    W5 = homogeneous_numeric(5, [assignment[f"w5_{i}"]
                                 for i in range(6)])
    Z5 = homogeneous_numeric(5, [assignment[f"z5_{i}"]
                                 for i in range(6)])
    return C6, D6, W5, Z5


def q7_rows(values, return_blocks=False):
    C2, D2, C4, D4, W7, Z7 = new_polynomials(q9_survivor)
    C3, D3, W4, Z4, W6, Z6 = y_polynomials(q8_survivor)
    C6, D6, W5, Z5 = restored(values)
    C = nadd(source_data["Cbase"], C2, C3, C4, C6)
    D = nadd(source_data["Dbase"], D2, D3, D4, D6)
    W = nadd(W4, W5, W6, W7)
    Z = nadd(Z4, Z5, Z6, Z7)

    E = nadd(source_data["L1"], source_data["K"],
             nderivative(C, 0), nderivative(D, 1))
    E1_4 = divide_exact(degree_part(E, 4), 3)
    E1_5 = divide_exact(degree_part(E, 5), 3)
    E1_7 = divide_exact(degree_part(E, 7), 3)

    cx, cy = nderivative(C, 0), nderivative(C, 1)
    dx, dy = nderivative(D, 0), nderivative(D, 1)
    M = nadd(nmul(source_data["A"], dy),
             nmul(cx, source_data["vy"]),
             nscale(-1, nmul(source_data["uy"], dx)),
             nscale(-1, nmul(cy, source_data["vx"])))
    F4 = nadd(E1_4, degree_part(M, 4),
              nderivative(W5, 0), nderivative(Z5, 1))
    F5 = nadd(E1_5, degree_part(M, 5),
              nderivative(W6, 0), nderivative(Z6, 1))
    F7 = nadd(E1_7, degree_part(M, 7))
    F1_7 = divide_exact(F7, 3)

    N7 = degree_part(nbracket(C, D), 7)
    T = nadd(nmul(source_data["A"], nderivative(Z, 1)),
             nmul(nderivative(W, 0), source_data["vy"]),
             nscale(-1, nmul(source_data["uy"], nderivative(Z, 0))),
             nscale(-1, nmul(nderivative(W, 1), source_data["vx"])))
    G7 = nadd(F1_7, N7, degree_part(T, 7))
    blocks = (row(F5, 5), row(F4, 4), row(G7, 7))
    if return_blocks:
        return blocks
    return sum((list(block) for block in blocks), [])


def affine_matrix(function, variable_count):
    zero = (0,) * variable_count
    b = function(zero)
    columns = []
    for index in range(variable_count):
        basis = [0] * variable_count
        basis[index] = 1
        value = function(tuple(basis))
        columns.append([(a - c) % 3 for a, c in zip(value, b)])
    A = [[columns[col][r] for col in range(variable_count)]
         for r in range(len(b))]
    ones = (1,) * variable_count
    assert function(ones) == [
        (b[r] + sum(A[r])) % 3 for r in range(len(b))]
    return A, b


def rref_certificate(A, b):
    rows = len(A)
    cols = len(A[0])
    work = [[value % 3 for value in line] + [(-constant) % 3]
            for line, constant in zip(A, b)]
    transform = [[int(i == j) for j in range(rows)] for i in range(rows)]
    rank = 0
    pivots = []
    for col in range(cols):
        pivot = next((r for r in range(rank, rows) if work[r][col]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        transform[rank], transform[pivot] = transform[pivot], transform[rank]
        if work[rank][col] == 2:
            work[rank] = [(2 * value) % 3 for value in work[rank]]
            transform[rank] = [(2 * value) % 3 for value in transform[rank]]
        for r in range(rows):
            if r != rank and work[r][col]:
                scalar = work[r][col]
                work[r] = [(x - scalar * y) % 3
                           for x, y in zip(work[r], work[rank])]
                transform[r] = [(x - scalar * y) % 3
                                for x, y in zip(transform[r],
                                               transform[rank])]
        pivots.append(col)
        rank += 1
    bad = next((r for r in range(rows)
                if all(value == 0 for value in work[r][:-1])
                and work[r][-1]), None)
    witness = None
    certificate = None
    residual = 0
    if bad is None:
        answer = [0] * cols
        for r, pivot in enumerate(pivots):
            answer[pivot] = work[r][-1]
        witness = tuple(answer)
        assert q7_rows(witness) == [0] * rows
    else:
        certificate = tuple(transform[bad])
        assert all(sum(certificate[r] * A[r][col]
                       for r in range(rows)) % 3 == 0
                   for col in range(cols))
        residual = sum(certificate[r] * b[r] for r in range(rows)) % 3
        assert residual
    return rank, rank + int(bad is not None), witness, certificate, residual


A, b = affine_matrix(q7_rows, len(names))
rank, augmented, witness, certificate, residual = rref_certificate(A, b)
support = [i for i, value in enumerate(certificate or ()) if value]
plus_one = None
if certificate is not None:
    index = support[0]
    changed = list(b)
    changed[index] = (changed[index] + 1) % 3
    plus_one = (index, sum(certificate[r] * changed[r]
                           for r in range(len(b))) % 3)

matrix_payload = bytes(value % 3 for line in A for value in line)
rhs_payload = bytes(value % 3 for value in b)
print("source_row_identities", ("F5=E5/3+M5+divW6",
      "F4=E4/3+M4+divW5", "G7=F7/3+{C,D}7+T7"))
print("source_shapes", 6, 5, 8, 18)
print("zero_blocks", tuple(tuple(block) for block in q7_rows((0,) * 18,
                                                               True)))
print("matrix_sha256", hashlib.sha256(matrix_payload).hexdigest())
print("rhs_sha256", hashlib.sha256(rhs_payload).hexdigest())
print("rank_pair", (rank, augmented))
print("fiber_dimension", len(names) - rank if witness is not None else None)
print("witness", list(witness) if witness is not None else None)
print("left_null_certificate", list(certificate) if certificate else None)
print("left_null_support", support)
print("left_null_residual", residual)
print("plus_one_control", plus_one)
print("verdict", "COMPATIBLE" if witness is not None else "INCOMPATIBLE")
print("PASS-Q8-SURVIVOR-Q7-TRANSITION")
