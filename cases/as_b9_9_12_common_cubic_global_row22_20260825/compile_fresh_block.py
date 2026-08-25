#!/usr/bin/env python3
"""Freeze the constant fresh55 block and its canonical F3 quotients."""

from __future__ import annotations

import contextlib
import gzip
import hashlib
import io
import json
import os
import platform
from pathlib import Path


assert platform.system() == "Linux", "AWS-only compiler refuses non-Linux"
job_tag = os.environ.get("AWS_JOB_TAG", "")
assert job_tag.startswith("as_b9_common_cubic_fresh_block_"), job_tag

parent_path = Path(os.environ["GLOBAL_V1_SOURCE"])
parent_bytes = parent_path.read_bytes()
expected_parent = "b16912cd1b6146a35736e9bb872d96bfa640e1bb920e04b7c5a9e13256d12a3f"
assert hashlib.sha256(parent_bytes).hexdigest() == expected_parent

saved_output = os.environ["OUTPUT_JSON"]
saved_witness = os.environ["WITNESS_OUTPUT"]
saved_job_tag = os.environ["AWS_JOB_TAG"]
os.environ["OUTPUT_JSON"] = os.environ["GLOBAL_V1_RESULT"]
os.environ["WITNESS_OUTPUT"] = os.environ["GLOBAL_V1_WITNESS"]
os.environ["AWS_JOB_TAG"] = "as_b9_common_cubic_global_row22_fresh_block"
scope = {"__file__": str(parent_path), "__name__": "__fresh_block_parent__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(parent_bytes, str(parent_path), "exec"), scope)
os.environ["OUTPUT_JSON"] = saved_output
os.environ["WITNESS_OUTPUT"] = saved_witness
os.environ["AWS_JOB_TAG"] = saved_job_tag

canonical = scope["canonical_family_point"]
family_fresh_kernel = scope["fresh_kernel"]
next_matrix = scope["next_matrix"]
rref_solve = scope["rref_solve"]
assert len(family_fresh_kernel) == 55
assert len(next_matrix) == 299 and len(next_matrix[0]) == 149

# The 205-row next obstruction quotient is the canonical RREF kernel of the
# transpose of the fixed 299 x 149 new-digit operator.
next_transpose = [list(column) for column in zip(*next_matrix)]
next_rank, _, next_left_cokernel = rref_solve(
    next_transpose, [0] * len(next_transpose))
assert (next_rank, len(next_left_cokernel)) == (94, 205)


def project(vector):
    return [sum(a * b for a, b in zip(functional, vector)) % 3
            for functional in next_left_cokernel]


zero = [0] * 150
_, base_rows, _ = canonical(zero)
base_rhs = [(-(value // (3 ** 11))) % 3 for value in base_rows]
projected_base = project(base_rhs)
columns = []
for index in range(55):
    parameters = list(zero)
    parameters[95 + index] = 1
    _, rows1, _ = canonical(parameters)
    rhs1 = [(-(value // (3 ** 11))) % 3 for value in rows1]
    column = [(a - b) % 3 for a, b in zip(project(rhs1), projected_base)]
    columns.append(column)
    parameters[95 + index] = 2
    _, rows2, _ = canonical(parameters)
    rhs2 = [(-(value // (3 ** 11))) % 3 for value in rows2]
    assert project(rhs2) == [
        (base + 2 * delta) % 3
        for base, delta in zip(projected_base, column)
    ]
fresh_block = [[columns[column][row] for column in range(55)]
               for row in range(205)]
fresh_rank, _, fresh_kernel = rref_solve(fresh_block, [0] * 205)
fresh_transpose = [list(column) for column in zip(*fresh_block)]
fresh_transpose_rank, _, fresh_left_quotient = rref_solve(
    fresh_transpose, [0] * 55)
assert (fresh_rank, fresh_transpose_rank) == (29, 29)
assert (len(fresh_kernel), len(fresh_left_quotient)) == (26, 176)

payload = {
    "next_left_cokernel": next_left_cokernel,
    "fresh_block": fresh_block,
    "fresh_kernel": fresh_kernel,
    "fresh_left_quotient": fresh_left_quotient,
}
payload_bytes = (json.dumps(payload, sort_keys=True, separators=(",", ":"))
                 + "\n").encode()
Path(os.environ["BLOCK_GZIP"]).write_bytes(
    gzip.compress(payload_bytes, compresslevel=9, mtime=0))
result = {
    "status": "PASS-AS-B9-COMMON-CUBIC-CONSTANT-FRESH-BLOCK",
    "aws_job_tag": job_tag,
    "global_v1_source_sha256": expected_parent,
    "next_operator_shape_rank_kernel_cokernel": [299, 149, 94, 55, 205],
    "fresh_block_shape_rank_kernel_quotient": [205, 55, 29, 26, 176],
    "fresh_block_sha256": hashlib.sha256(json.dumps(
        fresh_block, separators=(",", ":")).encode()).hexdigest(),
    "payload_uncompressed_sha256": hashlib.sha256(payload_bytes).hexdigest(),
    "constant_block_source_identity": (
        "family parameters change the literal map only at order >=3^5, "
        "while final fresh-kernel digits enter at order 3^10; after "
        "division by 3^11, every predecessor-dependent cross term is "
        "divisible by 3^4 and vanishes modulo 3"
    ),
    "scope": "one source-derived constant block and canonical F3 quotients",
    "refusal_scope": [
        "does not classify the 95-parameter predecessor zero locus",
        "does not by itself prove lift or exclusion",
    ],
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(saved_output).write_bytes(encoded)
print("fresh_shape_rank_kernel_quotient", 205, 55, 29, 26, 176)
print("fresh_block_sha256", result["fresh_block_sha256"])
print("payload_sha256", result["payload_uncompressed_sha256"])
print("result_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])
