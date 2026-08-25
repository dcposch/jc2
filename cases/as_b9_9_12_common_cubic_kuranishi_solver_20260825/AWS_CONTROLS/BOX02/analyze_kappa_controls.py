#!/usr/bin/env python3
"""Analyze exact Kuranishi values on deterministic predecessor controls."""

from __future__ import annotations

import contextlib
import gzip
import hashlib
import io
import json
import os
import platform
import random
from pathlib import Path


assert platform.system() == "Linux", "AWS-only analyzer refuses non-Linux"
job_tag = os.environ.get("AWS_JOB_TAG", "")
assert job_tag.startswith("as_b9_common_cubic_kuranishi_controls_"), job_tag
parent_path = Path(os.environ["GLOBAL_V1_SOURCE"])
parent_bytes = parent_path.read_bytes()
expected_parent = "b16912cd1b6146a35736e9bb872d96bfa640e1bb920e04b7c5a9e13256d12a3f"
assert hashlib.sha256(parent_bytes).hexdigest() == expected_parent
block_path = Path(os.environ["FRESH_BLOCK_GZIP"])
expected_block = "f7f473c5781f610dd0f96112981e8f3b3c7757467d42b7c465a3dfde5c80e8af"
assert hashlib.sha256(block_path.read_bytes()).hexdigest() == expected_block

saved_output = os.environ["OUTPUT_JSON"]
saved_witness = os.environ["WITNESS_OUTPUT"]
saved_tag = os.environ["AWS_JOB_TAG"]
os.environ["OUTPUT_JSON"] = os.environ["GLOBAL_V1_RESULT"]
os.environ["WITNESS_OUTPUT"] = os.environ["GLOBAL_V1_WITNESS"]
os.environ["AWS_JOB_TAG"] = "as_b9_common_cubic_global_row22_kappa_controls"
scope = {"__file__": str(parent_path), "__name__": "__kappa_controls_parent__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(parent_bytes, str(parent_path), "exec"), scope)
os.environ["OUTPUT_JSON"] = saved_output
os.environ["WITNESS_OUTPUT"] = saved_witness
os.environ["AWS_JOB_TAG"] = saved_tag

canonical = scope["canonical_family_point"]
block = json.load(gzip.open(block_path, "rt"))
next_left = block["next_left_cokernel"]
fresh_left = block["fresh_left_quotient"]
combined = [[sum(fresh_left[row][k] * next_left[k][column]
                 for k in range(205)) % 3
             for column in range(299)]
            for row in range(176)]


def kappa(predecessor):
    _, rows, _ = canonical(predecessor + [0] * 55)
    digits = [(-(value // (3 ** 11))) % 3 for value in rows]
    return [sum(a * b for a, b in zip(functional, digits)) % 3
            for functional in combined]


def rref_kernel(matrix):
    rows = len(matrix)
    columns = len(matrix[0]) if rows else 0
    work = [[value % 3 for value in row] for row in matrix]
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
        if row == rows:
            break
    free = [column for column in range(columns) if column not in pivots]
    kernel = []
    for free_column in free:
        vector = [0] * columns
        vector[free_column] = 1
        for index, pivot in enumerate(pivots):
            vector[pivot] = (-work[index][free_column]) % 3
        kernel.append(vector)
    return len(pivots), kernel


controls = [[0] * 95]
labels = ["origin"]
for index in range(95):
    for scalar in (1, 2):
        point = [0] * 95
        point[index] = scalar
        controls.append(point)
        labels.append(f"basis_{index}_{scalar}")
rng = random.Random(202608251823)
for sample in range(256):
    controls.append([rng.randrange(3) for _ in range(95)])
    labels.append(f"mixed_{sample}")
values = [kappa(point) for point in controls]
origin = values[0]
differences = [[(value - base) % 3 for value, base in zip(row, origin)]
               for row in values[1:]]
difference_rank, constant_functionals = rref_kernel(differences)
constant_nonzero = []
for functional in constant_functionals:
    pairing = sum(a * b for a, b in zip(functional, origin)) % 3
    if pairing:
        constant_nonzero.append((sum(bool(value) for value in functional),
                                 pairing, functional))
constant_nonzero.sort(key=lambda item: (item[0], item[1], item[2]))
univariate_affine_failures = []
for index in range(95):
    one = values[1 + 2 * index]
    two = values[2 + 2 * index]
    failed = [row for row in range(176)
              if (two[row] - origin[row]) % 3 !=
              2 * (one[row] - origin[row]) % 3]
    if failed:
        univariate_affine_failures.append([index, failed])

records = [{"label": label, "kappa": value}
           for label, value in zip(labels, values)]
records_bytes = (json.dumps(records, sort_keys=True, separators=(",", ":"))
                 + "\n").encode()
Path(os.environ["RECORDS_GZIP"]).write_bytes(
    gzip.compress(records_bytes, compresslevel=9, mtime=0))
result = {
    "status": "PASS-AS-B9-COMMON-CUBIC-KURANISHI-CONTROLS",
    "aws_job_tag": job_tag,
    "control_count": len(controls),
    "kappa_zero_count": sum(not any(value) for value in values),
    "origin_nonzero_count": sum(bool(value) for value in origin),
    "difference_affine_span_rank": difference_rank,
    "sample_constant_functional_dimension": len(constant_functionals),
    "sample_constant_nonzero_count": len(constant_nonzero),
    "sparsest_sample_constant_nonzero": (
        None if not constant_nonzero else {
            "support_size": constant_nonzero[0][0],
            "pairing": constant_nonzero[0][1],
            "functional_sparse": [[i, value] for i, value in enumerate(
                constant_nonzero[0][2]) if value],
        }),
    "univariate_affine_failure_variable_count": len(
        univariate_affine_failures),
    "univariate_affine_failures": univariate_affine_failures,
    "records_uncompressed_sha256": hashlib.sha256(records_bytes).hexdigest(),
    "scope": "447 deterministic exact controls only",
    "refusal_scope": [
        "sample-constant functionals are navigation, not identities",
        "no family-wide zero-locus conclusion",
    ],
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(saved_output).write_bytes(encoded)
print("zero_origin_nonzero", result["kappa_zero_count"],
      result["origin_nonzero_count"])
print("difference_rank_constant_dim_nonzero", difference_rank,
      len(constant_functionals), len(constant_nonzero))
print("univariate_affine_failure_variables",
      len(univariate_affine_failures))
print("result_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])
