#!/usr/bin/env python3
"""Compress Kuranishi coordinates using exact shared source-DAG atoms."""

from __future__ import annotations

import contextlib
import gzip
import hashlib
import io
import json
import os
import platform
from pathlib import Path


assert platform.system() == "Linux", "AWS-only analyzer refuses non-Linux"
job_tag = os.environ.get("AWS_JOB_TAG", "")
assert job_tag.startswith("as_b9_common_cubic_kuranishi_span_"), job_tag
emitter_path = Path(os.environ["EMITTER_SOURCE"])
payload = emitter_path.read_bytes()
expected_emitter = "1d6dbd671e6652592d9de76a74c86034f8f2e9177703c3410c8a05e533963edf"
assert hashlib.sha256(payload).hexdigest() == expected_emitter

saved_output = os.environ["OUTPUT_JSON"]
saved_tag = os.environ["AWS_JOB_TAG"]
saved_start = os.environ.get("ROW_START")
saved_end = os.environ.get("ROW_END")
os.environ["AWS_JOB_TAG"] = "as_b9_common_cubic_kuranishi_map_span_parent"
os.environ["ROW_START"] = "0"
os.environ["ROW_END"] = "176"
os.environ["OUTPUT_JSON"] = os.environ["PARENT_EMIT_RESULT"]
scope = {"__file__": str(emitter_path), "__name__": "__span_parent__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(payload, str(emitter_path), "exec"), scope)
os.environ["AWS_JOB_TAG"] = saved_tag
os.environ["OUTPUT_JSON"] = saved_output
if saved_start is None:
    os.environ.pop("ROW_START", None)
else:
    os.environ["ROW_START"] = saved_start
if saved_end is None:
    os.environ.pop("ROW_END", None)
else:
    os.environ["ROW_END"] = saved_end

next_rhs = scope["next_rhs"]
combined = scope["combined"]
assert (len(next_rhs), len(combined)) == (299, 176)
groups_by_digest = {}
for index, value in enumerate(next_rhs):
    groups_by_digest.setdefault(value.digest, []).append(index)
digests = sorted(groups_by_digest)
groups = [groups_by_digest[digest] for digest in digests]
reduced = [[sum(row[column] for column in group) % 3
            for group in groups] for row in combined]


def rank_and_basis_rows(matrix):
    """Return rank and original row indices selected by incremental RREF."""
    work = []
    pivots = []
    basis_rows = []
    for original_index, original in enumerate(matrix):
        row = [value % 3 for value in original]
        for pivot, old in zip(pivots, work):
            if row[pivot]:
                scalar = row[pivot]
                row = [(a - scalar * b) % 3 for a, b in zip(row, old)]
        pivot = next((index for index, value in enumerate(row) if value), None)
        if pivot is None:
            continue
        if row[pivot] == 2:
            row = [(2 * value) % 3 for value in row]
        for index, old in enumerate(work):
            if old[pivot]:
                scalar = old[pivot]
                work[index] = [(a - scalar * b) % 3
                               for a, b in zip(old, row)]
        insert = next((index for index, old_pivot in enumerate(pivots)
                       if old_pivot > pivot), len(pivots))
        pivots.insert(insert, pivot)
        work.insert(insert, row)
        basis_rows.insert(insert, original_index)
    return len(pivots), basis_rows


def solve_columns(matrix, target):
    """Solve matrix*x=target over F3, returning one particular."""
    rows = len(matrix)
    columns = len(matrix[0])
    work = [[value % 3 for value in row] + [target[index] % 3]
            for index, row in enumerate(matrix)]
    pivots = []
    row = 0
    for column in range(columns):
        chosen = next((index for index in range(row, rows)
                       if work[index][column]), None)
        if chosen is None:
            continue
        work[row], work[chosen] = work[chosen], work[row]
        if work[row][column] == 2:
            work[row] = [(2 * value) % 3 for value in work[row]]
        for index in range(rows):
            if index == row or not work[index][column]:
                continue
            scalar = work[index][column]
            work[index] = [(a - scalar * b) % 3
                           for a, b in zip(work[index], work[row])]
        pivots.append(column)
        row += 1
    assert not any(not any(current[:-1]) and current[-1] for current in work)
    answer = [0] * columns
    for index, pivot in enumerate(pivots):
        answer[pivot] = work[index][-1]
    return answer


rank, basis_rows = rank_and_basis_rows(reduced)
basis = [reduced[index] for index in basis_rows]
basis_transpose = [list(column) for column in zip(*basis)]
relations = []
for index, row in enumerate(reduced):
    coefficients = solve_columns(basis_transpose, row)
    assert all(sum(coefficients[k] * basis[k][column]
                   for k in range(rank)) % 3 == row[column]
               for column in range(len(groups)))
    relations.append(coefficients)

certificate = {
    "next_rhs_structural_digests": digests,
    "next_rhs_groups": groups,
    "reduced_coordinate_matrix": reduced,
    "basis_coordinate_rows": basis_rows,
    "coordinate_relations": relations,
}
certificate_bytes = (json.dumps(
    certificate, sort_keys=True, separators=(",", ":")) + "\n").encode()
Path(os.environ["CERTIFICATE_GZIP"]).write_bytes(
    gzip.compress(certificate_bytes, compresslevel=9, mtime=0))
result = {
    "status": "PASS-AS-B9-COMMON-CUBIC-KURANISHI-STRUCTURAL-SPAN",
    "aws_job_tag": job_tag,
    "emitter_source_sha256": expected_emitter,
    "next_rhs_count": len(next_rhs),
    "distinct_next_rhs_structural_atom_count": len(groups),
    "kuranishi_coordinate_count": len(reduced),
    "formal_atom_linear_rank": rank,
    "basis_coordinate_rows": basis_rows,
    "certificate_uncompressed_sha256": hashlib.sha256(
        certificate_bytes).hexdigest(),
    "exactness": (
        "coordinates are compared as F3-linear forms in byte-identical "
        "source-DAG atoms; no sampled functional equality is used"),
    "scope": "exact linear compression of the emitted modular DAG",
    "refusal_scope": [
        "does not solve the remaining basis-coordinate zero locus",
        "does not identify algebraic identities between distinct DAG atoms",
    ],
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(saved_output).write_bytes(encoded)
print("rhs_distinct_atoms", len(groups))
print("coordinate_formal_rank_basis", rank, basis_rows)
print("certificate_sha256", result["certificate_uncompressed_sha256"])
print("result_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])
