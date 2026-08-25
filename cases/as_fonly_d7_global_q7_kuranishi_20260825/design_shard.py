#!/usr/bin/env python3
"""One exact shard of the global Q7 quadratic Kuranishi design."""
from __future__ import annotations

import contextlib
import hashlib
import importlib.util
import io
import itertools
import json
import os
from pathlib import Path

ROOT = Path(os.environ.get("JC2_ROOT", Path(__file__).resolve().parents[2]))
PARENT = (ROOT / "cases/as_fonly_d7_q8state_next_high_samples_20260825"
          / "compile_state.py")
EXPECTED_PARENT_SHA = "abfd5cfa79edb87e16e2df706f7466dcf335302d889cb71bf06bcdfb9609588e"
assert hashlib.sha256(PARENT.read_bytes()).hexdigest() == EXPECTED_PARENT_SHA

final_output = Path(os.environ["OUTPUT_JSON"])
os.environ["STATE_FAMILY"] = "q8_kernel"
os.environ["SAMPLE_INDEX"] = "0"
os.environ["OUTPUT_JSON"] = os.environ["BOOTSTRAP_JSON"]
spec = importlib.util.spec_from_file_location("frozen_state_parent", PARENT)
parent = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(parent)


def rref_left_cokernel(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    work = [[value % 3 for value in line] for line in matrix]
    transform = [[int(i == j) for j in range(rows)] for i in range(rows)]
    rank = 0
    for col in range(cols):
        pivot = next((r for r in range(rank, rows) if work[r][col]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        transform[rank], transform[pivot] = transform[pivot], transform[rank]
        if work[rank][col] == 2:
            work[rank] = [(2 * value) % 3 for value in work[rank]]
            transform[rank] = [(2 * value) % 3
                               for value in transform[rank]]
        for row_index in range(rows):
            if row_index != rank and work[row_index][col]:
                scalar = work[row_index][col]
                work[row_index] = [
                    (a - scalar * b) % 3
                    for a, b in zip(work[row_index], work[rank])]
                transform[row_index] = [
                    (a - scalar * b) % 3
                    for a, b in zip(transform[row_index], transform[rank])]
        rank += 1
    left = tuple(tuple(line) for line in transform[rank:])
    assert all(all(sum(vector[r] * matrix[r][col] for r in range(rows)) % 3 == 0
                   for col in range(cols)) for vector in left)
    return rank, left


free_q9 = tuple(i for i in range(19)
                if i not in {10, 11, 12, 13, 15, 17})
coordinate_names = tuple(f"t{i}" for i in free_q9) + tuple(
    f"s{i}" for i in range(19))
assert len(free_q9) == 13 and len(coordinate_names) == 32

zero_t = [0] * 19
zero_t[17] = 1
base_x = parent.add_vector(parent.q9_origin, parent.q9_kernel, zero_t,
                           reduce=False)
base_A22, base_b22 = parent.matrix_and_rhs(
    parent.transition_rows, base_x, parent.q8_variable_count)
A13 = base_A22[:13]
rank13, top_kernel = parent.kernel_basis(A13)
assert rank13 == 13 and tuple(top_kernel) == parent.q8_kernel_at_origin
_r0, _a0, _p0, _w0, section0 = parent.rref_solve(A13, base_b22[:13])
assert (_r0, _a0) == (13, 13) and section0 is not None

# Choose one fixed affine integer lift of the F3 RREF section.  Differences
# are represented in {0,1,2} but sums below are intentionally not reduced.
section_deltas = []
for free_position, q9_index in enumerate(free_q9):
    t_basis = zero_t[:]
    t_basis[q9_index] = 1
    x_basis = parent.add_vector(parent.q9_origin, parent.q9_kernel, t_basis,
                                reduce=False)
    A_basis, b_basis = parent.matrix_and_rhs(
        parent.transition_rows, x_basis, parent.q8_variable_count)
    assert A_basis[:13] == A13
    _r, _a, _p, _w, section_basis = parent.rref_solve(A13, b_basis[:13])
    assert (_r, _a) == (13, 13) and section_basis is not None
    section_deltas.append(tuple((section_basis[col] - section0[col]) % 3
                                for col in range(parent.q8_variable_count)))


def build_q7(parameters):
    assert len(parameters) == 32
    t = [0] * 19
    t[17] = 1
    for index, value in zip(free_q9, parameters[:13]):
        t[index] = value
    xvalues = parent.add_vector(parent.q9_origin, parent.q9_kernel, t,
                                reduce=False)
    A22, b22 = parent.matrix_and_rhs(parent.transition_rows, xvalues,
                                     parent.q8_variable_count)
    assert A22[:13] == A13
    section = tuple(section0[col] + sum(
        parameters[i] * section_deltas[i][col] for i in range(13))
        for col in range(parent.q8_variable_count))
    assert all((sum(A13[row][col] * section[col]
                    for col in range(parent.q8_variable_count))
                + b22[row]) % 3 == 0 for row in range(13))
    yvalues = parent.add_vector(section, top_kernel, parameters[13:],
                                reduce=False)
    assert parent.source_rows(parent.source_data, xvalues) == [0] * 23
    assert parent.transition_rows(xvalues, yvalues) == [0] * 22
    parent.xvalues, parent.yvalues = xvalues, yvalues
    return parent.affine_matrix(parent.q7_rows, 18)


zero = (0,) * 32
A0, b0 = build_q7(zero)
rank0, left = rref_left_cokernel(A0)
assert rank0 == 9 and len(left) == 10
matrix_sha = hashlib.sha256(bytes(value for line in A0 for value in line)).hexdigest()
assert matrix_sha == "f30baed043492c723d80a787571d6cb743626da643a20f031da5b95091e6dd50"


def canonical_direct_reduction(parameters):
    """Typed comparison only; no affine/canonical equivalence is assumed."""
    t = [0] * 19
    t[17] = 1
    for index, value in zip(free_q9, parameters[:13]):
        t[index] = value
    x_unreduced = parent.add_vector(parent.q9_origin, parent.q9_kernel, t,
                                    reduce=False)
    section = tuple(section0[col] + sum(
        parameters[i] * section_deltas[i][col] for i in range(13))
        for col in range(parent.q8_variable_count))
    y_unreduced = parent.add_vector(section, top_kernel, parameters[13:],
                                    reduce=False)
    xvalues = tuple(value % 3 for value in x_unreduced)
    yvalues = tuple(value % 3 for value in y_unreduced)
    q9_ok = parent.source_rows(parent.source_data, xvalues) == [0] * 23
    q8_ok = q9_ok and parent.transition_rows(xvalues, yvalues) == [0] * 22
    result = {"q9_rows_zero": q9_ok, "q8_rows_zero": q8_ok,
              "q7_rank_pair": None}
    if q8_ok:
        parent.xvalues, parent.yvalues = xvalues, yvalues
        matrix, rhs = parent.affine_matrix(parent.q7_rows, 18)
        rank, augmented, _p, _w, _witness = parent.rref_solve(matrix, rhs)
        result["q7_rank_pair"] = [rank, augmented]
    return result


def evaluate(parameters, include_canonical_control=False):
    matrix, rhs = build_q7(parameters)
    assert matrix == A0
    kappa = [sum(vector[row] * rhs[row] for row in range(19)) % 3
             for vector in left]
    result = {"parameters": list(parameters), "kappa": kappa}
    if include_canonical_control:
        result["canonical_direct_reduction"] = canonical_direct_reduction(
            parameters)
    return result


shard = int(os.environ["SHARD_INDEX"])
assert 0 <= shard < 36
records = []
kind = ""
if shard == 0:
    kind = "basis"
    records.append(evaluate(zero))
    for variable in range(32):
        for scalar in (1, 2):
            point = [0] * 32
            point[variable] = scalar
            records.append(evaluate(tuple(point)))
elif 1 <= shard <= 31:
    kind = "pairs"
    pairs = list(itertools.combinations(range(32), 2))
    for pair_index in range(shard - 1, len(pairs), 31):
        left_index, right_index = pairs[pair_index]
        point = [0] * 32
        point[left_index] = point[right_index] = 1
        record = evaluate(tuple(point))
        record["pair_index"] = pair_index
        record["pair"] = [left_index, right_index]
        records.append(record)
else:
    kind = "controls"
    state = 202608250337
    controls = []
    for control_index in range(64):
        point = []
        for _ in range(32):
            state = (1664525 * state + 1013904223) & 0xffffffff
            point.append(state % 3)
        controls.append(tuple(point))
    for control_index in range(shard - 32, 64, 4):
        record = evaluate(controls[control_index], include_canonical_control=True)
        record["control_index"] = control_index
        records.append(record)

result = {
    "shard_index": shard,
    "kind": kind,
    "coordinate_names": coordinate_names,
    "q7_matrix_sha256": matrix_sha,
    "q7_rank": rank0,
    "q7_cokernel_dimension": len(left),
    "record_count": len(records),
    "records": records,
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n").encode()
final_output.write_bytes(encoded)
print("shard_kind_index", kind, shard)
print("record_count", len(records))
print("q7_rank_cokernel", rank0, len(left))
print("q7_matrix_sha256", matrix_sha)
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-GLOBAL-Q7-KURANISHI-DESIGN-SHARD")
