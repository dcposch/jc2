#!/usr/bin/env python3
"""Global-family diagnostic for the B9 [x^2 y^2] Cartier carry."""

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
assert job_tag.startswith("as_b9_common_cubic_global_row22_"), job_tag

parent_path = Path(os.environ["INDEPENDENT_PARENT_SOURCE"])
parent_bytes = parent_path.read_bytes()
expected_parent = "460199584e128bc2c5f3196871a34437ebdfd7d674ccf0bcc2f52b9db8ace6b8"
assert hashlib.sha256(parent_bytes).hexdigest() == expected_parent

# Execute the source-independent, reviewed family compiler in a private
# namespace.  It reconstructs the full staged family and leaves every exact
# basis/operator needed below in its namespace.
saved_output = os.environ["OUTPUT_JSON"]
saved_witness_output = os.environ["WITNESS_OUTPUT"]
os.environ["OUTPUT_JSON"] = os.environ["PARENT_AUDIT_RESULT"]
os.environ["WITNESS_OUTPUT"] = os.environ["PARENT_WITNESS_OUTPUT"]
scope = {"__file__": str(parent_path), "__name__": "__global_row22_parent__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(parent_bytes, str(parent_path), "exec"), scope)
os.environ["OUTPUT_JSON"] = saved_output
os.environ["WITNESS_OUTPUT"] = saved_witness_output

residual = scope["residual"]
rref_solve = scope["rref_solve"]
base_values = list(scope["base_values"])
directions = [list(vector) for vector in scope["directions"]]
active_count = int(scope["active_count"])
inactive_count = int(scope["inactive_count"])
raw_constant = list(scope["raw_constant"])
raw_linear = [list(vector) for vector in scope["raw_linear"]]
raw_diagonal = [list(vector) for vector in scope["raw_diagonal"]]
raw_cross = [list(vector) for vector in scope["raw_cross"]]
cross_indices = [tuple(pair) for pair in scope["cross_indices"]]
inactive_matrix = [list(row) for row in scope["inactive_matrix"]]
fresh_matrix = [list(row) for row in scope["fresh_matrix"]]
target_divisor = int(scope["target_divisor"])
assert target_divisor == 3 ** 10
assert len(directions) == 133
assert (active_count, inactive_count) == (17, 116)


def fixed_solver(matrix):
    """Return a deterministic F3 solver, kernel, rank, and left controls."""
    m = len(matrix)
    n = len(matrix[0])
    work = [
        [value % 3 for value in row]
        + [1 if i == j else 0 for j in range(m)]
        for i, row in enumerate(matrix)
    ]
    pivots = []
    pivot_row = 0
    for column in range(n):
        chosen = next((row for row in range(pivot_row, m)
                       if work[row][column]), None)
        if chosen is None:
            continue
        work[pivot_row], work[chosen] = work[chosen], work[pivot_row]
        inverse = 1 if work[pivot_row][column] == 1 else 2
        work[pivot_row] = [(inverse * value) % 3
                           for value in work[pivot_row]]
        for row in range(m):
            if row == pivot_row or not work[row][column]:
                continue
            scalar = work[row][column]
            work[row] = [(a - scalar * b) % 3
                         for a, b in zip(work[row], work[pivot_row])]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == m:
            break
    free = [column for column in range(n) if column not in pivots]
    kernel = []
    for free_column in free:
        vector = [0] * n
        vector[free_column] = 1
        for row, pivot in enumerate(pivots):
            vector[pivot] = (-work[row][free_column]) % 3
        kernel.append(vector)

    def solve(rhs):
        transformed = [
            sum(work[row][n + index] * rhs[index]
                for index in range(m)) % 3
            for row in range(m)
        ]
        bad = next((row for row in range(len(pivots), m)
                    if transformed[row]), None)
        if bad is not None:
            left = [work[bad][n + index] for index in range(m)]
            return None, [left, transformed[bad]]
        particular = [0] * n
        for row, pivot in enumerate(pivots):
            particular[pivot] = transformed[row]
        return particular, None

    return solve, kernel, len(pivots)


solve_inactive, spectator_kernel, spectator_rank = fixed_solver(
    inactive_matrix)
solve_fresh, fresh_kernel, fresh_rank = fixed_solver(fresh_matrix)
assert (spectator_rank, len(spectator_kernel)) == (38, 78)
assert (fresh_rank, len(fresh_kernel)) == (94, 55)


def add_scaled(target, vector, scalar):
    if scalar:
        for index, value in enumerate(vector):
            target[index] += scalar * value


def raw_active_value(active):
    value = list(raw_constant)
    for index, scalar in enumerate(active):
        if scalar:
            value = [(a + scalar * b) % 3
                     for a, b in zip(value, raw_linear[index])]
            value = [(a + scalar * scalar * b) % 3
                     for a, b in zip(value, raw_diagonal[index])]
    for vector, (left, right) in zip(raw_cross, cross_indices):
        scalar = active[left] * active[right]
        if scalar:
            value = [(a + scalar * b) % 3
                     for a, b in zip(value, vector)]
    return value


def canonical_family_point(parameters):
    assert len(parameters) == 150
    active = parameters[:17]
    spectator_parameters = parameters[17:95]
    fresh_parameters = parameters[95:]

    raw = raw_active_value(active)
    inactive_particular, bad = solve_inactive([(-value) % 3
                                               for value in raw])
    assert bad is None
    inactive = list(inactive_particular)
    for scalar, vector in zip(spectator_parameters, spectator_kernel):
        inactive = [(a + scalar * b) % 3
                    for a, b in zip(inactive, vector)]

    predecessor = list(base_values)
    for scalar, direction in zip(active, directions[:17]):
        add_scaled(predecessor, direction, scalar)
    for scalar, direction in zip(inactive, directions[17:]):
        add_scaled(predecessor, direction, scalar)
    predecessor_rows = residual(predecessor)
    assert all(value % target_divisor == 0 for value in predecessor_rows)
    fresh_rhs = [(-(value // target_divisor)) % 3
                 for value in predecessor_rows]
    fresh_particular, bad = solve_fresh(fresh_rhs)
    assert bad is None
    fresh = list(fresh_particular)
    for scalar, vector in zip(fresh_parameters, fresh_kernel):
        fresh = [(a + scalar * b) % 3
                 for a, b in zip(fresh, vector)]
    final_values = [value + (3 ** 5) * digit
                    for value, digit in zip(predecessor, fresh)]
    final_rows = residual(final_values)
    assert all(value % (3 ** 11) == 0 for value in final_rows)
    omega = (final_rows[12] // (3 ** 11)) % 3
    return final_values, final_rows, omega


# Source proof/control for universal fresh-row vanishing: a new map digit is
# T += 3^6*u, i.e. a coefficient correction by 243*3^6=3^11.  Its row modulo
# 3 depends only on the fixed mod-3 map, shared by the entire family.
zero_parameters = [0] * 150
origin_values, origin_rows, origin_omega = canonical_family_point(
    zero_parameters)
next_columns = []
for column in range(149):
    probe = list(origin_values)
    probe[column] += 3 ** 6
    delta = residual(probe)[12] - origin_rows[12]
    assert delta % (3 ** 11) == 0
    next_columns.append((delta // (3 ** 11)) % 3)
assert not any(next_columns)

points = []


def consume(label, parameters):
    values, rows, omega = canonical_family_point(parameters)
    points.append({
        "label": label,
        "parameters_sparse": [[index, value]
                              for index, value in enumerate(parameters)
                              if value],
        "omega": omega,
        "values_mod729_sha256": hashlib.sha256(json.dumps(
            [value % (3 ** 6) for value in values],
            separators=(",", ":")).encode()).hexdigest(),
        "all_299_rows_zero_mod3p11": True,
    })
    return values, rows, omega


consume("origin", zero_parameters)
for index in range(150):
    for scalar in (1, 2):
        parameters = [0] * 150
        parameters[index] = scalar
        consume(f"basis_{index}_{scalar}", parameters)

rng = random.Random(202608251812)
for sample in range(256):
    parameters = [rng.randrange(3) for _ in range(150)]
    consume(f"mixed_{sample}", parameters)

histogram = {str(value): sum(point["omega"] == value for point in points)
             for value in range(3)}
omega_values = sorted({point["omega"] for point in points})
first_zero = next((point for point in points if point["omega"] == 0), None)
assert len(omega_values) > 1, "diagnostic found no variation; exact proof needed"

# Every sampled carry-zero point is immediately tested against all 299 next
# rows.  The next operator is computed literally at the first such point.
next_gate = None
if first_zero is not None:
    parameters = [0] * 150
    for index, value in first_zero["parameters_sparse"]:
        parameters[index] = value
    values, rows_at_point, omega = canonical_family_point(parameters)
    assert omega == 0
    next_matrix_columns = []
    for column in range(149):
        probe = list(values)
        probe[column] += 3 ** 6
        delta = [a - b for a, b in zip(residual(probe), rows_at_point)]
        assert all(value % (3 ** 11) == 0 for value in delta)
        next_matrix_columns.append([(value // (3 ** 11)) % 3
                                    for value in delta])
    next_matrix = [[next_matrix_columns[column][row]
                    for column in range(149)]
                   for row in range(299)]
    assert next_matrix[12] == [0] * 149
    solve_next, next_kernel, next_rank = fixed_solver(next_matrix)
    next_rhs = [(-(value // (3 ** 11))) % 3 for value in rows_at_point]
    next_particular, bad = solve_next(next_rhs)
    next_gate = {
        "point_label": first_zero["label"],
        "rank": next_rank,
        "kernel_dimension": len(next_kernel),
        "consistent": next_particular is not None,
        "obstruction": bad,
    }
    if next_particular is not None:
        lifted = [value + (3 ** 6) * digit
                  for value, digit in zip(values, next_particular)]
        lifted_rows = residual(lifted)
        assert all(value % (3 ** 12) == 0 for value in lifted_rows)
        witness_payload = {
            "parameters": parameters,
            "values_mod2187": [value % (3 ** 7) for value in lifted],
            "all_299_rows_zero_mod3p12": True,
        }
        witness_bytes = (json.dumps(witness_payload, sort_keys=True,
                                    separators=(",", ":")) + "\n").encode()
        Path(os.environ["WITNESS_OUTPUT"]).write_bytes(witness_bytes)
        next_gate["witness_sha256"] = hashlib.sha256(
            witness_bytes).hexdigest()

points_bytes = (json.dumps(points, sort_keys=True, separators=(",", ":"))
                + "\n").encode()
Path(os.environ["POINTS_GZIP"]).write_bytes(
    __import__("gzip").compress(points_bytes, compresslevel=9, mtime=0))
result = {
    "status": "PASS-AS-B9-COMMON-CUBIC-GLOBAL-ROW22-DIAGNOSTIC",
    "aws_job_tag": job_tag,
    "parent_independent_source_sha256": expected_parent,
    "family_parameter_dimensions": {
        "active": 17,
        "spectator_kernel": 78,
        "fresh_kernel": 55,
        "total": 150,
    },
    "parent_stage_dimensions": [55, 81, 99, 116, 133],
    "universal_next_row22_zero": True,
    "origin_omega": origin_omega,
    "tested_point_count": len(points),
    "tested_omega_histogram": histogram,
    "tested_omega_values": omega_values,
    "carry_nonconstant_witnessed": len(omega_values) > 1,
    "first_carry_zero_point": first_zero,
    "first_carry_zero_full_next_gate": next_gate,
    "points_uncompressed_sha256": hashlib.sha256(points_bytes).hexdigest(),
    "scope": "exact canonical controls on the complete-family parameterization",
    "refusal_scope": [
        "basis/mixed controls are not an exhaustive zero-locus census",
        "no family-wide lift or exclusion, all-depth, maximum12, CE, or JC2",
    ],
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(saved_output).write_bytes(encoded)
print("family_dimensions", 17, 78, 55, 150)
print("omega_origin_values_histogram", origin_omega, omega_values, histogram)
print("first_zero", None if first_zero is None else first_zero["label"])
print("next_gate", next_gate)
print("result_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])
