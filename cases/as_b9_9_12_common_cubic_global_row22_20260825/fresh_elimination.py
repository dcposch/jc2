#!/usr/bin/env python3
"""Eliminate the complete 55D fresh fibre at sampled 95D predecessors."""

from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
import platform
import random
from pathlib import Path


assert platform.system() == "Linux", "AWS-only compiler refuses non-Linux"
job_tag = os.environ.get("AWS_JOB_TAG", "")
assert job_tag.startswith("as_b9_common_cubic_fresh_elim_"), job_tag
shard_count = int(os.environ["SHARD_COUNT"])
shard_index = int(os.environ["SHARD_INDEX"])
assert 0 <= shard_index < shard_count

parent_path = Path(os.environ["GLOBAL_V1_SOURCE"])
parent_bytes = parent_path.read_bytes()
expected_parent = "b16912cd1b6146a35736e9bb872d96bfa640e1bb920e04b7c5a9e13256d12a3f"
assert hashlib.sha256(parent_bytes).hexdigest() == expected_parent

saved_output = os.environ["OUTPUT_JSON"]
saved_witness = os.environ["WITNESS_OUTPUT"]
saved_job_tag = os.environ["AWS_JOB_TAG"]
os.environ["OUTPUT_JSON"] = os.environ["GLOBAL_V1_RESULT"]
os.environ["WITNESS_OUTPUT"] = os.environ["GLOBAL_V1_WITNESS"]
os.environ["AWS_JOB_TAG"] = "as_b9_common_cubic_global_row22_fresh_parent"
scope = {"__file__": str(parent_path), "__name__": "__fresh_elim_parent__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(parent_bytes, str(parent_path), "exec"), scope)
os.environ["OUTPUT_JSON"] = saved_output
os.environ["WITNESS_OUTPUT"] = saved_witness
os.environ["AWS_JOB_TAG"] = saved_job_tag

canonical = scope["canonical_family_point"]
fresh_kernel = scope["fresh_kernel"]
next_matrix = scope["next_matrix"]
fixed_solver = scope["fixed_solver"]
rref_solve = scope["rref_solve"]
residual = scope["residual"]
assert len(fresh_kernel) == 55
assert len(next_matrix) == 299 and len(next_matrix[0]) == 149

transpose = [list(column) for column in zip(*next_matrix)]
_, _, left_cokernel = rref_solve(transpose, [0] * 149)
assert len(left_cokernel) == 205
solve_next, next_kernel, next_rank = fixed_solver(next_matrix)
assert (next_rank, len(next_kernel)) == (94, 55)


def project(vector):
    return [sum(a * b for a, b in zip(functional, vector)) % 3
            for functional in left_cokernel]


predecessors = []
predecessors.append([0] * 95)
for index in range(95):
    for scalar in (1, 2):
        point = [0] * 95
        point[index] = scalar
        predecessors.append(point)
rng = random.Random(202608251823)
for _ in range(256):
    predecessors.append([rng.randrange(3) for _ in range(95)])
assert len(predecessors) == 447

records = []
first_witness = None
for global_index, predecessor in enumerate(predecessors):
    if global_index % shard_count != shard_index:
        continue
    base_parameters = predecessor + [0] * 55
    base_values, base_rows, _ = canonical(base_parameters)
    base_rhs = [(-(value // (3 ** 11))) % 3 for value in base_rows]
    projected_base = project(base_rhs)
    columns = []
    for index in range(55):
        parameters = list(base_parameters)
        parameters[95 + index] = 1
        _, rows, _ = canonical(parameters)
        rhs = [(-(value // (3 ** 11))) % 3 for value in rows]
        columns.append([(a - b) % 3
                        for a, b in zip(project(rhs), projected_base)])
        # Affinity in each final fresh direction is source-licensed by its
        # outer 3^10 coefficient order; retain a twice control.
        parameters[95 + index] = 2
        _, rows2, _ = canonical(parameters)
        rhs2 = [(-(value // (3 ** 11))) % 3 for value in rows2]
        assert project(rhs2) == [
            (base + 2 * delta) % 3
            for base, delta in zip(projected_base, columns[-1])
        ]
    matrix = [[columns[column][row] for column in range(55)]
              for row in range(205)]
    rank, fresh_particular, _ = rref_solve(
        matrix, [(-value) % 3 for value in projected_base])
    consistent = fresh_particular is not None
    record = {
        "global_index": global_index,
        "predecessor_sparse": [[i, value]
                               for i, value in enumerate(predecessor)
                               if value],
        "fresh_cokernel_rank": rank,
        "consistent_after_fresh_elimination": consistent,
        "base_projection_nonzero_count": sum(bool(value)
                                              for value in projected_base),
        "matrix_sha256": hashlib.sha256(json.dumps(
            matrix, separators=(",", ":")).encode()).hexdigest(),
    }
    if consistent:
        parameters = predecessor + fresh_particular
        values, rows, _ = canonical(parameters)
        rhs = [(-(value // (3 ** 11))) % 3 for value in rows]
        next_particular, bad = solve_next(rhs)
        assert bad is None and next_particular is not None
        lifted = [value + (3 ** 6) * digit
                  for value, digit in zip(values, next_particular)]
        lifted_rows = residual(lifted)
        assert all(value % (3 ** 12) == 0 for value in lifted_rows)
        witness = {
            "global_index": global_index,
            "predecessor": predecessor,
            "fresh_kernel_parameters": fresh_particular,
            "next_digits": next_particular,
            "values_mod2187": [value % (3 ** 7) for value in lifted],
            "all_299_rows_zero_mod3p12": True,
        }
        witness_bytes = (json.dumps(witness, sort_keys=True,
                                    separators=(",", ":")) + "\n").encode()
        record["witness_sha256"] = hashlib.sha256(witness_bytes).hexdigest()
        if first_witness is None:
            first_witness = witness
            Path(saved_witness).write_bytes(witness_bytes)
    records.append(record)

rank_histogram = {}
for record in records:
    key = str(record["fresh_cokernel_rank"])
    rank_histogram[key] = rank_histogram.get(key, 0) + 1
records_bytes = (json.dumps(records, sort_keys=True, separators=(",", ":"))
                 + "\n").encode()
Path(os.environ["RECORDS_GZIP"]).write_bytes(
    __import__("gzip").compress(records_bytes, compresslevel=9, mtime=0))
result = {
    "status": "PASS-AS-B9-COMMON-CUBIC-FRESH-ELIMINATION-SHARD",
    "aws_job_tag": job_tag,
    "global_v1_source_sha256": expected_parent,
    "shard_count": shard_count,
    "shard_index": shard_index,
    "global_control_count": len(predecessors),
    "processed_count": len(records),
    "fresh_cokernel_rank_histogram": rank_histogram,
    "sat_count": sum(record["consistent_after_fresh_elimination"]
                     for record in records),
    "first_witness_sha256": (None if first_witness is None else
                             hashlib.sha256((json.dumps(
                                 first_witness, sort_keys=True,
                                 separators=(",", ":")) + "\n").encode()
                                            ).hexdigest()),
    "records_uncompressed_sha256": hashlib.sha256(records_bytes).hexdigest(),
    "scope": "deterministic predecessor controls with complete fresh fibres",
    "refusal_scope": [
        "not exhaustive over the 95-dimensional predecessor parameter space",
        "UNSAT controls are not family-wide exclusion",
        "no all-depth, maximum12, CE, or JC2 claim",
    ],
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(saved_output).write_bytes(encoded)
print("shard_processed_sat", shard_index, len(records), result["sat_count"])
print("rank_histogram", rank_histogram)
print("first_witness", result["first_witness_sha256"])
print("result_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])
