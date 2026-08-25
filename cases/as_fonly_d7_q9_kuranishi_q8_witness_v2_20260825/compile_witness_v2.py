#!/usr/bin/env python3
"""Emit an exact left-null certificate for the V1 Q8 transition."""
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

transition_rows = scope["transition_rows"]
matrix_and_rhs = scope["matrix_and_rhs"]
q9_vector = scope["q9_vector"]
y_names = scope["y_names"]


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
                                for x, y in zip(transform[r], transform[rank])]
        pivots.append(col)
        rank += 1
    bad = next((r for r in range(rows)
                if all(value == 0 for value in work[r][:-1])
                and work[r][-1]), None)
    certificate = None
    residual = 0
    if bad is not None:
        certificate = tuple(transform[bad])
        assert all(sum(certificate[r] * A[r][col] for r in range(rows)) % 3 == 0
                   for col in range(cols))
        residual = sum(certificate[r] * b[r] for r in range(rows)) % 3
        assert residual != 0
        assert (-residual) % 3 == work[bad][-1]
    witness = None
    if bad is None:
        witness0 = [0] * cols
        for r, pivot in enumerate(pivots):
            witness0[pivot] = work[r][-1]
        witness = tuple(witness0)
        assert transition_rows(q9_vector, witness) == [0] * rows
    return rank, rank + int(bad is not None), certificate, residual, witness


A22, b22 = matrix_and_rhs(transition_rows, q9_vector, len(y_names))
rank13, aug13, cert13, residual13, _ = rref_certificate(A22[:13], b22[:13])
rank22, aug22, cert22, residual22, witness = rref_certificate(A22, b22)
assert rank13 == aug13 and cert13 is None and residual13 == 0
kuranishi_rank = rank22 - rank13
matrix_payload = bytes(value % 3 for line in A22 for value in line)
rhs_payload = bytes(value % 3 for value in b22)
certificate_support = [i for i, value in enumerate(cert22 or ()) if value]
plus_one_index = certificate_support[0] if certificate_support else None
plus_one_residual = None
if cert22 is not None:
    plus_one_rhs = list(b22)
    plus_one_rhs[plus_one_index] = (plus_one_rhs[plus_one_index] + 1) % 3
    plus_one_residual = sum(cert22[r] * plus_one_rhs[r]
                            for r in range(len(b22))) % 3
    assert plus_one_residual == (residual22 + cert22[plus_one_index]) % 3

print("source_shapes", 23, 32, 3, 4, 6, 9, 32)
print("source_row_identities",
      ("E2", "F3=E3/3+M3+divW4", "F5=E5/3+M5+divW6",
       "G8=F8/3+{C,D}8+T8"))
print("transition_matrix_sha256", hashlib.sha256(matrix_payload).hexdigest())
print("transition_rhs_sha256", hashlib.sha256(rhs_payload).hexdigest())
print("accepted_image_rank_pair", (rank13, aug13))
print("accepted_image_kernel_dimension", len(y_names) - rank13)
print("full_transition_rank_pair", (rank22, aug22))
print("kuranishi_rank_on_image_kernel", kuranishi_rank)
print("kuranishi_cokernel_dimension", 9 - kuranishi_rank)
print("left_null_certificate", list(cert22) if cert22 is not None else None)
print("left_null_certificate_support", certificate_support)
print("left_null_residual", residual22)
print("plus_one_control", (plus_one_index, plus_one_residual))
print("q8_witness", list(witness) if witness is not None else None)
print("verdict", "INCOMPATIBLE" if cert22 is not None else "COMPATIBLE")
print("PASS-Q9-WITNESS-Q8-KURANISHI-CERTIFICATE")
