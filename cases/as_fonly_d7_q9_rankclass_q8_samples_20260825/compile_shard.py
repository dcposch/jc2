#!/usr/bin/env python3
"""Deterministic Q9-rank-class representatives and their Q8 signatures."""
from __future__ import annotations

import contextlib
import hashlib
import io
import itertools
import json
import os
from pathlib import Path

ROOT = Path(os.environ.get("JC2_ROOT", Path(__file__).resolve().parents[2]))
Q9 = (ROOT / "cases/as_fonly_d7_vertical_q9_state_gate_20260825"
      / "compile_shard.py")
EXPECTED_Q9_SHA = "54d05ebf86af9d75da0cc509e3094ce2e26516b84c73b8a50a36e71dbc9282b2"
q9_payload = Q9.read_bytes()
assert hashlib.sha256(q9_payload).hexdigest() == EXPECTED_Q9_SHA
q9_source = q9_payload.decode()
q9_marker = '\nshard_count = int(os.environ.get("SHARD_COUNT", "27"))\n'
assert q9_source.count(q9_marker) == 1
q9_scope = {"__file__": str(Q9), "__name__": "__q9_prefix__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(q9_source.split(q9_marker, 1)[0], str(Q9), "exec"), q9_scope)

V1 = (ROOT / "cases/as_fonly_d7_q9_kuranishi_q8_20260825"
      / "compile_witness.py")
EXPECTED_V1_SHA = "fbf327fb04beb2fa929f3b46a5df035244ec838793bc1f596801935adae09d4b"
v1_payload = V1.read_bytes()
assert hashlib.sha256(v1_payload).hexdigest() == EXPECTED_V1_SHA
v1_source = v1_payload.decode()
v1_marker = "\nA22, b22 = matrix_and_rhs(transition_rows, q9_vector, len(y_names))\n"
assert v1_source.count(v1_marker) == 1
v1_scope = {"__file__": str(V1), "__name__": "__q8_v1_prefix__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(v1_source.split(v1_marker, 1)[0], str(V1), "exec"), v1_scope)

top = q9_scope["top"]
structural = tuple(q9_scope["structural"])
frob = tuple(q9_scope["frob"])
unknowns = tuple(q9_scope["unknowns"])
parent_matrix = q9_scope["matrix"]
parent_rhs = q9_scope["rhs"]
N12, Q11, Q10 = q9_scope["N12"], q9_scope["Q11"], q9_scope["Q10"]
eval_expr = q9_scope["eval_expr"]
coefficient = q9_scope["coefficient"]
esubstitute = q9_scope["esubstitute"]
rref_source = q9_scope["rref_source"]
affine_solutions = q9_scope["affine_solutions"]
canonical_source = q9_scope["canonical_source"]
source_rows = q9_scope["source_rows"]
new_names = tuple(q9_scope["new_names"])

transition_rows = v1_scope["transition_rows"]
matrix_and_rhs = v1_scope["matrix_and_rhs"]
y_names = tuple(v1_scope["y_names"])


def affine_matrix(function, variable_count):
    zero = (0,) * variable_count
    b = function(zero)
    columns = []
    for index in range(variable_count):
        basis = [0] * variable_count
        basis[index] = 1
        value = function(tuple(basis))
        columns.append([(a - c) % 3 for a, c in zip(value, b)])
    A = [[columns[col][row] for col in range(variable_count)]
         for row in range(len(b))]
    ones = (1,) * variable_count
    assert function(ones) == [
        (b[row] + sum(A[row])) % 3 for row in range(len(b))]
    return A, [value % 3 for value in b]


def rref_certificate(A, b):
    rows = len(A)
    cols = len(A[0])
    work = [[value % 3 for value in line] + [(-constant) % 3]
            for line, constant in zip(A, b)]
    transform = [[int(i == j) for j in range(rows)] for i in range(rows)]
    rank = 0
    pivots = []
    for col in range(cols):
        pivot = next((row for row in range(rank, rows)
                      if work[row][col]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        transform[rank], transform[pivot] = transform[pivot], transform[rank]
        if work[rank][col] == 2:
            work[rank] = [(2 * value) % 3 for value in work[rank]]
            transform[rank] = [(2 * value) % 3
                               for value in transform[rank]]
        for row in range(rows):
            if row != rank and work[row][col]:
                scalar = work[row][col]
                work[row] = [(x - scalar * y) % 3
                             for x, y in zip(work[row], work[rank])]
                transform[row] = [(x - scalar * y) % 3
                                  for x, y in zip(transform[row],
                                                 transform[rank])]
        pivots.append(col)
        rank += 1
    bad_row = next((row for row in range(rows)
                    if all(value == 0 for value in work[row][:-1])
                    and work[row][-1]), None)
    witness = None
    certificate = None
    residual = 0
    if bad_row is None:
        answer = [0] * cols
        for row, pivot in enumerate(pivots):
            answer[pivot] = work[row][-1]
        witness = tuple(answer)
        assert all((sum(A[row][col] * witness[col]
                        for col in range(cols)) + b[row]) % 3 == 0
                   for row in range(rows))
    else:
        certificate = tuple(transform[bad_row])
        assert all(sum(certificate[row] * A[row][col]
                       for row in range(rows)) % 3 == 0
                   for col in range(cols))
        residual = sum(certificate[row] * b[row]
                       for row in range(rows)) % 3
        assert residual
    matrix_rref = [line[:-1] for line in work]
    return (rank, rank + int(bad_row is not None), witness,
            certificate, residual, matrix_rref)


def bytes_hash(matrix):
    return hashlib.sha256(bytes(value % 3 for line in matrix
                                for value in line)).hexdigest()


def q9_record(predecessor_values, source_data):
    A9, b9 = affine_matrix(lambda values: source_rows(source_data, values),
                           len(new_names))
    rank, augmented, witness, certificate, residual, rref_matrix = \
        rref_certificate(A9, b9)
    record = {
        "predecessor": list(predecessor_values),
        "q9_rank_pair": [rank, augmented],
        "q9_matrix_sha256": bytes_hash(A9),
        "q9_rref_sha256": bytes_hash(rref_matrix),
        "q9_rhs_sha256": hashlib.sha256(bytes(b9)).hexdigest(),
        "q9_witness": list(witness) if witness is not None else None,
        "q9_left_null_support": ([i for i, value in enumerate(certificate)
                                  if value] if certificate else None),
        "q9_left_null_residual": residual,
    }
    if witness is None:
        return record
    assert source_rows(source_data, witness) == [0] * 23
    v1_scope["source_data"] = source_data
    A22, b22 = matrix_and_rhs(transition_rows, witness, len(y_names))
    rank13, aug13, _, _, _, rref13 = rref_certificate(A22[:13], b22[:13])
    rank22, aug22, ywitness, q8_certificate, q8_residual, rref22 = \
        rref_certificate(A22, b22)
    if ywitness is not None:
        assert transition_rows(witness, ywitness) == [0] * 22
    record.update({
        "q8_top_rank_pair": [rank13, aug13],
        "q8_full_rank_pair": [rank22, aug22],
        "q8_kuranishi_rank": rank22 - rank13,
        "q8_matrix_sha256": bytes_hash(A22),
        "q8_top_rref_sha256": bytes_hash(rref13),
        "q8_full_rref_sha256": bytes_hash(rref22),
        "q8_rhs_sha256": hashlib.sha256(bytes(b22)).hexdigest(),
        "q8_witness": list(ywitness) if ywitness is not None else None,
        "q8_left_null_support": ([i for i, value in enumerate(q8_certificate)
                                  if value] if q8_certificate else None),
        "q8_left_null_residual": q8_residual,
    })
    return record


shard_count = int(os.environ.get("SHARD_COUNT", "27"))
shard_index = int(os.environ["SHARD_INDEX"])
per_class = int(os.environ.get("PER_CLASS", "4"))
assert shard_count == 27 and 0 <= shard_index < shard_count and per_class > 0
target_pairs = ((13, 13), (13, 14), (15, 15),
                (16, 16), (16, 17), (17, 18))
base_total = 3 ** len(structural)
start = base_total * shard_index // shard_count
stop = base_total * (shard_index + 1) // shard_count
zero_frob = {name: {} for name in frob}
records = {f"{a},{b}": [] for a, b in target_pairs}
q10_seen = 0

for base_index, svalues in enumerate(
        itertools.product(range(3), repeat=len(structural))):
    if base_index < start:
        continue
    if base_index >= stop:
        break
    sassign = dict(zip(structural, svalues))
    Aparent = [[eval_expr(entry, sassign) for entry in row]
               for row in parent_matrix]
    Fparent = [[eval_expr(coefficient(affine, name), sassign)
                for name in frob] for affine in parent_rhs]
    bparent = [eval_expr(esubstitute(affine, zero_frob), sassign)
               for affine in parent_rhs]
    pivots, work = rref_source(Aparent, Fparent, bparent)
    for fvalues in itertools.product(range(3), repeat=len(frob)):
        for xvalues in affine_solutions(pivots, work, fvalues):
            assignment = dict(sassign)
            assignment.update(zip(frob, fvalues))
            assignment.update(zip(unknowns, xvalues))
            if (any(eval_expr(test, assignment) for test in N12)
                    or any(eval_expr(test, assignment) for test in Q11)
                    or any(eval_expr(test, assignment) for test in Q10)):
                continue
            q10_seen += 1
            predecessor_values = tuple(svalues + fvalues + xvalues)
            data = canonical_source(assignment)
            A9, b9 = affine_matrix(lambda values: source_rows(data, values),
                                   len(new_names))
            rank, augmented, _w, _c, _r, _rr = rref_certificate(A9, b9)
            key = f"{rank},{augmented}"
            if key in records and len(records[key]) < per_class:
                records[key].append(q9_record(predecessor_values, data))

output = {
    "shard_index": shard_index,
    "shard_count": shard_count,
    "base_range": [start, stop],
    "per_class_cap": per_class,
    "q10_seen": q10_seen,
    "records": records,
}
encoded = (json.dumps(output, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("shard_index", shard_index)
print("base_range", start, stop)
print("q10_seen", q10_seen)
print("record_counts", sorted((key, len(value))
                              for key, value in records.items()))
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-Q9-RANKCLASS-Q8-SAMPLE-SHARD")
