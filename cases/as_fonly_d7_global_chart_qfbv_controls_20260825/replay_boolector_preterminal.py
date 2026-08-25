#!/usr/bin/env python3
"""Directly replay a Boolector predecessor model in the integer source."""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path

ROOT = Path(os.environ["JC2_ROOT"])
PARENT = (ROOT / "cases/as_fonly_d7_q8state_next_high_samples_20260825"
          / "compile_state.py")
EXPECTED_PARENT_SHA = (
    "abfd5cfa79edb87e16e2df706f7466dcf335302d889cb71bf06bcdfb9609588e")
payload = PARENT.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_PARENT_SHA
source = payload.decode()
family_marker = '\nfamily = os.environ["STATE_FAMILY"]\n'
restored_marker = "\ndef restored(values):\n"
result_marker = '\nresult = {"family": family, "sample_index": sample_index,\n'
scope = {"__file__": str(PARENT), "__name__": "__boolector_replay__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(source.split(family_marker, 1)[0], str(PARENT), "exec"), scope)
fragment = (restored_marker
            + source.split(restored_marker, 1)[1].split(result_marker, 1)[0])
exec(compile(fragment, str(PARENT), "exec"), scope)


def parse_model(path):
    lines = path.read_text().splitlines()
    sat_index = lines.index("sat")
    model = {}
    for line in lines[sat_index + 1:]:
        fields = line.split()
        if len(fields) == 2 and set(fields[1]) <= {"0", "1"}:
            model[fields[0]] = int(fields[1], 2)
    return model


model_path = Path(os.environ["MODEL_FILE"])
expected_model_sha = os.environ["EXPECTED_MODEL_SHA256"]
assert hashlib.sha256(model_path.read_bytes()).hexdigest() == expected_model_sha
model = parse_model(model_path)
tvalues = [model[f"t{index}"] for index in range(13)]
yvalues = [model[f"y{index}"] for index in range(32)]
uvalues = [model[f"u{index}"] for index in range(9)]
assert all(0 <= value <= 2 for value in tvalues + yvalues + uvalues)

forced = {10: 0, 11: 0, 12: 0, 13: 0, 15: 0, 17: 1}
free_q9 = tuple(index for index in range(19) if index not in forced)
full_t = [forced.get(index, 0) for index in range(19)]
for chart_index, kernel_index in enumerate(free_q9):
    full_t[kernel_index] = tvalues[chart_index]
xvalues = scope["add_vector"](
    scope["q9_origin"], scope["q9_kernel"], full_t, reduce=True)
assert scope["source_rows"](scope["source_data"], xvalues) == [0] * 23
assert scope["transition_rows"](xvalues, yvalues) == [0] * 22
scope["xvalues"] = xvalues
scope["yvalues"] = yvalues


def affine_matrix(function, variable_count):
    zero = (0,) * variable_count
    b = function(zero)
    columns = []
    for column in range(variable_count):
        basis = [0] * variable_count
        basis[column] = 1
        value = function(tuple(basis))
        columns.append([(left - right) % 3
                        for left, right in zip(value, b)])
    return ([[columns[column][row] for column in range(variable_count)]
             for row in range(len(b))], [value % 3 for value in b])


matrix7, b7 = affine_matrix(scope["q7_rows"], 18)
matrix_bytes = (json.dumps(matrix7, separators=(",", ":")) + "\n").encode()
assert hashlib.sha256(matrix_bytes).hexdigest() == (
    "5a8395d4f9f06adec44410ddfed5085c0c3833c9bdb57f5a76fe608524d51790")
rank7, augmented7, pivot_columns, _rref7, zero7 = scope["rref_solve"](
    matrix7, [0] * 19)
assert rank7 == augmented7 == 9 and zero7 is not None
free_columns = [column for column in range(18) if column not in pivot_columns]
pivot_rows = []
seen_rank = 0
for row_index in range(19):
    rank, _aug, _pivots, _rref, _witness = scope["rref_solve"](
        matrix7[:row_index + 1], [0] * (row_index + 1))
    if rank > seen_rank:
        pivot_rows.append(row_index)
        seen_rank = rank


def inverse_mod3(matrix):
    size = len(matrix)
    work = [[value % 3 for value in row]
            + [int(i == j) for j in range(size)]
            for i, row in enumerate(matrix)]
    for column in range(size):
        pivot = next(row for row in range(column, size)
                     if work[row][column])
        work[column], work[pivot] = work[pivot], work[column]
        if work[column][column] == 2:
            work[column] = [(2 * value) % 3 for value in work[column]]
        for row in range(size):
            if row != column and work[row][column]:
                scalar = work[row][column]
                work[row] = [(left - scalar * right) % 3
                             for left, right in zip(work[row], work[column])]
    return [row[size:] for row in work]


pivot_matrix = [[matrix7[row][column] for column in pivot_columns]
                for row in pivot_rows]
pivot_inverse = inverse_mod3(pivot_matrix)
rvalues = [None] * 18
for index, column in enumerate(free_columns):
    rvalues[column] = uvalues[index]
for pivot_index, column in enumerate(pivot_columns):
    value = sum(-pivot_inverse[pivot_index][source_index] * b7[row]
                for source_index, row in enumerate(pivot_rows))
    value += sum(
        -pivot_inverse[pivot_index][source_index]
        * matrix7[row][free_column] * uvalues[free_index]
        for source_index, row in enumerate(pivot_rows)
        for free_index, free_column in enumerate(free_columns))
    rvalues[column] = value % 3
assert scope["q7_rows"](rvalues) == [0] * 19
Cn, Dn, Wn, Zn, recursive = scope["recursive_high"](rvalues)
direct = scope["direct_high"](Cn, Dn, Wn, Zn)
assert recursive == direct
high = [value for degree in range(12, 8, -1)
        for value in recursive[degree]]
assert any(high)
result = {
    "model_file_sha256": expected_model_sha,
    "tvalues": tvalues,
    "xvalues": list(xvalues),
    "yvalues": yvalues,
    "uvalues": uvalues,
    "rvalues": rvalues,
    "q9_source_replay": "PASS",
    "q8_source_replay": "PASS",
    "q7_source_replay": "PASS",
    "recursive_literal_div243_agreement": "PASS",
    "terminal_high_nonzero_control": high,
    "scope": "one SAT model of the global predecessor formula",
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("q9_q8_q7_source_replay PASS")
print("recursive_literal_div243_agreement PASS")
print("terminal_high_nonzero_count", sum(bool(value) for value in high))
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-AS-BOOLECTOR-PRETERMINAL-MODEL-REPLAY")
