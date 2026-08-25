#!/usr/bin/env python3
"""Solve and replay the exact 68-row Q4 affine system at one Q5 model."""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
PARENT = (ROOT / "cases/as_fonly_d7_q5_sat_full_q4_restore_20260825"
          / "replay_full_q4_restore.py")
EXPECTED_PARENT_SHA = (
    "9fa649802565ad52a448c23e8091e9bdeca90576d35834a61ae19ed701fb119c")
payload = PARENT.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_PARENT_SHA

parent_output = Path(os.environ["PARENT_OUTPUT_JSON"])
old_output = os.environ.get("OUTPUT_JSON")
os.environ["OUTPUT_JSON"] = str(parent_output)
namespace = {"__file__": str(PARENT), "__name__": "__full68_parent__"}
with contextlib.redirect_stdout(io.StringIO()) as parent_stdout:
    exec(compile(payload, str(PARENT), "exec"), namespace)
if old_output is None:
    del os.environ["OUTPUT_JSON"]
else:
    os.environ["OUTPUT_JSON"] = old_output

scope = namespace["scope"]
while "source_data" not in scope:
    scope = scope["scope"]
nadd = namespace["nadd"]
nscale = namespace["nscale"]
nmul = namespace["nmul"]
nderivative = namespace["nderivative"]
degree_part = namespace["degree_part"]
divide_exact = namespace["divide_exact"]
homogeneous_numeric = namespace["homogeneous_numeric"]
row = namespace["row"]
determinant_minus_one = namespace["determinant_minus_one"]
P5, Q5 = namespace["P5"], namespace["Q5"]
g4 = namespace["g"]
source_data = scope["source_data"]


def fourth_digit_cross(H, J):
    return nadd(nmul(source_data["A"], nderivative(J, 1)),
                nmul(nderivative(H, 0), source_data["vy"]),
                nscale(-1, nmul(source_data["uy"], nderivative(J, 0))),
                nscale(-1, nmul(nderivative(H, 1), source_data["vx"])))


def rows_for(values):
    assert len(values) == 12
    H = homogeneous_numeric(5, values[:6])
    J = homogeneous_numeric(5, values[6:])
    divergence_rows = row(nadd(nderivative(H, 0), nderivative(J, 1)), 4)
    cross = fourth_digit_cross(H, J)
    terminal_rows = []
    for degree in range(7, 13):
        terminal_rows.extend(row(cross, degree))
    assert len(divergence_rows) == 5 and len(terminal_rows) == 63
    return divergence_rows + terminal_rows


zero = rows_for([0] * 12)
assert zero == [0] * 68
columns = []
for index in range(12):
    basis = [0] * 12
    basis[index] = 1
    columns.append(rows_for(basis))
matrix = [[columns[column][row_index] % 3 for column in range(12)]
          for row_index in range(68)]
rhs = [(-value) % 3 for value in g4] + [0] * 63


def rref_solve(left, right):
    work = [[value % 3 for value in row_values] + [target % 3]
            for row_values, target in zip(left, right)]
    pivot_columns = []
    pivot_row = 0
    for column in range(12):
        chosen = next((row_index for row_index in range(pivot_row, len(work))
                       if work[row_index][column]), None)
        if chosen is None:
            continue
        work[pivot_row], work[chosen] = work[chosen], work[pivot_row]
        inverse = 1 if work[pivot_row][column] == 1 else 2
        work[pivot_row] = [(inverse * value) % 3
                           for value in work[pivot_row]]
        for row_index in range(len(work)):
            if row_index != pivot_row and work[row_index][column]:
                scalar = work[row_index][column]
                work[row_index] = [
                    (left_value - scalar * pivot_value) % 3
                    for left_value, pivot_value in zip(
                        work[row_index], work[pivot_row])]
        pivot_columns.append(column)
        pivot_row += 1
    contradictions = [row_values for row_values in work
                      if not any(row_values[:-1]) and row_values[-1]]
    rank = len(pivot_columns)
    if contradictions:
        return rank, rank + 1, pivot_columns, None, [], work, contradictions
    particular = [0] * 12
    for row_index, column in enumerate(pivot_columns):
        particular[column] = work[row_index][-1]
    free_columns = [column for column in range(12)
                    if column not in pivot_columns]
    kernel = []
    for free in free_columns:
        vector = [0] * 12
        vector[free] = 1
        for row_index, column in enumerate(pivot_columns):
            vector[column] = (-work[row_index][free]) % 3
        kernel.append(vector)
    return rank, rank, pivot_columns, particular, kernel, work, []


(rank, augmented_rank, pivot_columns, particular, kernel,
 reduced, contradictions) = rref_solve(matrix, rhs)
consistent = particular is not None

# The parent's canonical J-only section solves Q4 but is not allowed to pass
# silently if it breaks one or more terminal rows.
q4_only_control = namespace["h5_values"] + namespace["j5_values"]
q4_only_residual = [
    (left - target) % 3
    for left, target in zip(rows_for(q4_only_control), rhs)]
assert q4_only_residual[:5] == [0] * 5
q4_only_terminal_nonzero = [
    index for index, value in enumerate(q4_only_residual[5:]) if value]

result = {
    "status": ("PASS-AS-Q5-Q4-FULL68-SAT" if consistent
               else "PASS-AS-Q5-Q4-FULL68-UNSAT"),
    "parent_sha256": EXPECTED_PARENT_SHA,
    "model_sha256": hashlib.sha256(
        Path(os.environ["MODEL_OUTPUT"]).read_bytes()).hexdigest(),
    "parent_output_sha256": hashlib.sha256(parent_output.read_bytes()).hexdigest(),
    "parent_stdout_sha256": hashlib.sha256(
        parent_stdout.getvalue().encode()).hexdigest(),
    "matrix_shape": [68, 12],
    "matrix_sha256": hashlib.sha256(bytes(
        value for row_values in matrix for value in row_values)).hexdigest(),
    "rhs": rhs,
    "rhs_sha256": hashlib.sha256(bytes(rhs)).hexdigest(),
    "rank": rank,
    "augmented_rank": augmented_rank,
    "pivot_columns": pivot_columns,
    "consistent": consistent,
    "particular": particular,
    "kernel_basis": kernel,
    "solution_count": (3 ** len(kernel) if consistent else 0),
    "contradiction_rows": contradictions,
    "q4_only_control": q4_only_control,
    "q4_only_control_terminal_nonzero_indices": q4_only_terminal_nonzero,
    "full_integer_replay_passed": False,
    "scope": "one exact Q5 model; complete 5+63 chronological Q4 gate",
    "refusal_scope": [
        "not the entire Q5 fibre",
        "not Q3 through Q0 unless consistent and separately constructed",
        "not all-depth, counterexample, or JC2",
    ],
}

if consistent:
    assert rows_for(particular) == rhs
    H5 = homogeneous_numeric(5, particular[:6])
    J5 = homogeneous_numeric(5, particular[6:])
    P4 = nadd(P5, nscale(81, H5))
    Q4 = nadd(Q5, nscale(81, J5))
    determinant = determinant_minus_one(P4, Q4)
    q4_literal = row(divide_exact(degree_part(determinant, 4), 81), 4)
    terminal_literal = []
    for degree in range(7, 13):
        terminal_literal.extend(
            row(divide_exact(degree_part(determinant, degree), 243), degree))
    assert q4_literal == [0] * 5
    assert terminal_literal == [0] * 63
    assert all(value % 243 == 0 for value in degree_part(determinant, 4).values())
    assert all(value % 729 == 0 for (i, j), value in determinant.items()
               if 7 <= i + j <= 12)
    result.update({
        "full_integer_replay_passed": True,
        "q4_literal_div81_mod3": q4_literal,
        "terminal_literal_div243_mod3": terminal_literal,
        "H5_coefficients": particular[:6],
        "J5_coefficients": particular[6:],
        "max_total_degree_P4": max(i + j for i, j in P4),
        "max_total_degree_Q4": max(i + j for i, j in Q4),
    })

encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("rank", rank, "augmented_rank", augmented_rank,
      "consistent", consistent)
print("q4_only_terminal_nonzero_count", len(q4_only_terminal_nonzero))
if consistent:
    print("particular", particular)
    print("kernel_dimension", len(kernel))
    print("full_integer_replay", "PASS")
else:
    print("first_contradiction", contradictions[0])
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])

