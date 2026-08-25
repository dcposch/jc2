#!/usr/bin/env python3
"""Exact projection of global Q9 affine fibres to the row-8 scalar."""
from __future__ import annotations

import contextlib
import hashlib
import io
import itertools
import json
import os
from collections import Counter
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
PARENT = (ROOT / "cases/as_fonly_d7_vertical_q9_state_gate_20260825"
          / "compile_shard.py")
EXPECTED = "54d05ebf86af9d75da0cc509e3094ce2e26516b84c73b8a50a36e71dbc9282b2"
payload = PARENT.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED
marker = b'\nshard_count = int(os.environ.get("SHARD_COUNT", "27"))\n'
assert payload.count(marker) == 1
scope = {"__file__": str(PARENT), "__name__": "__row8_projection_parent__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(payload.split(marker, 1)[0] + b"\n", str(PARENT), "exec"),
         scope)

structural = tuple(scope["structural"])
frob = tuple(scope["frob"])
unknowns = tuple(scope["unknowns"])
matrix, rhs = scope["matrix"], scope["rhs"]
N12, Q11, Q10 = scope["N12"], scope["Q11"], scope["Q10"]
eval_expr, coefficient = scope["eval_expr"], scope["coefficient"]
esubstitute = scope["esubstitute"]
rref_source, affine_solutions = scope["rref_source"], scope["affine_solutions"]
canonical_source = scope["canonical_source"]
source_rows = scope["source_rows"]
new_names = tuple(scope["new_names"])
nadd, nscale, nmul = scope["nadd"], scope["nscale"], scope["nmul"]
nderivative = scope["nderivative"]
degree_part, divide_exact = scope["degree_part"], scope["divide_exact"]
new_polynomials = scope["new_polynomials"]
assert len(new_names) == 32
assert new_names[1:5] == ("c2_1", "c2_2", "d2_0", "d2_1")


def q9_affine_system(source_data):
    zero = (0,) * len(new_names)
    constant = source_rows(source_data, zero)
    columns = []
    for index in range(len(new_names)):
        basis = [0] * len(new_names)
        basis[index] = 1
        value = source_rows(source_data, tuple(basis))
        columns.append([(left - right) % 3
                        for left, right in zip(value, constant)])
    matrix_rows = [[columns[column][row] for column in range(len(new_names))]
                   for row in range(len(constant))]
    return matrix_rows, constant


def solve_affine(matrix_rows, constant):
    columns = len(matrix_rows[0])
    work = [[value % 3 for value in row] + [(-right) % 3]
            for row, right in zip(matrix_rows, constant)]
    pivots = []
    pivot_row = 0
    for column in range(columns):
        chosen = next((row for row in range(pivot_row, len(work))
                       if work[row][column]), None)
        if chosen is None:
            continue
        work[pivot_row], work[chosen] = work[chosen], work[pivot_row]
        if work[pivot_row][column] == 2:
            work[pivot_row] = [(2 * value) % 3
                               for value in work[pivot_row]]
        for row in range(len(work)):
            if row != pivot_row and work[row][column]:
                scalar = work[row][column]
                work[row] = [(left - scalar * right) % 3
                             for left, right in zip(work[row],
                                                    work[pivot_row])]
        pivots.append(column)
        pivot_row += 1
    if any(not any(row[:-1]) and row[-1] for row in work):
        return len(pivots), len(pivots) + 1, None, []
    particular = [0] * columns
    for row, column in enumerate(pivots):
        particular[column] = work[row][-1]
    free = [column for column in range(columns) if column not in pivots]
    kernel = []
    for free_column in free:
        vector = [0] * columns
        vector[free_column] = 1
        for row, pivot in enumerate(pivots):
            vector[pivot] = (-work[row][free_column]) % 3
        kernel.append(vector)
    return len(pivots), len(pivots), particular, kernel


def span_basis(vectors):
    work = [list(vector) for vector in vectors if any(vector)]
    basis = []
    pivot = 0
    for column in range(4):
        chosen = next((row for row in range(pivot, len(work))
                       if work[row][column]), None)
        if chosen is None:
            continue
        work[pivot], work[chosen] = work[chosen], work[pivot]
        if work[pivot][column] == 2:
            work[pivot] = [(2 * value) % 3 for value in work[pivot]]
        for row in range(len(work)):
            if row != pivot and work[row][column]:
                scalar = work[row][column]
                work[row] = [(left - scalar * right) % 3
                             for left, right in zip(work[row], work[pivot])]
        basis.append(tuple(work[pivot]))
        pivot += 1
    return basis


def closed_omega(h, q):
    q1, q2, q3, q4 = q
    first_carry = (q1 + 2 * q3) // 3
    second_carry = (2 * q2 + q4) // 3
    return (first_carry + 2 * h * second_carry) % 3


def source_omega(source_data, h, q):
    values = [0] * len(new_names)
    values[1:5] = q
    C2, D2, C4, D4, _, _ = new_polynomials(values)
    assert C4 == {} and D4 == {}
    C = nadd(source_data["Cbase"], C2)
    D = nadd(source_data["Dbase"], D2)
    E = nadd(source_data["L1"], source_data["K"],
             nderivative(C, 0), nderivative(D, 1))
    E1 = divide_exact(degree_part(E, 1), 3)
    cx, cy = nderivative(C, 0), nderivative(C, 1)
    dx, dy = nderivative(D, 0), nderivative(D, 1)
    M = nadd(nmul(source_data["A"], dy),
             nmul(cx, source_data["vy"]),
             nscale(-1, nmul(source_data["uy"], dx)),
             nscale(-1, nmul(cy, source_data["vx"])))
    F1 = nadd(E1, degree_part(M, 1))
    rx = F1.get((1, 0), 0) % 3
    ry = F1.get((0, 1), 0) % 3
    value = (ry - h * rx) % 3
    assert value == closed_omega(h, q), (h, q, rx, ry, value)
    return value


def omega_histogram(source_data, h):
    matrix_rows, constant = q9_affine_system(source_data)
    rank, augmented_rank, particular, kernel = solve_affine(
        matrix_rows, constant)
    if particular is None:
        return (rank, augmented_rank), [0, 0, 0], None, None
    projected_particular = tuple(particular[index] for index in range(1, 5))
    projected_kernel = [tuple(vector[index] for index in range(1, 5))
                        for vector in kernel]
    basis = span_basis(projected_kernel)
    fibre_factor = 3 ** (len(kernel) - len(basis))
    histogram = [0, 0, 0]
    first_zero_q = None
    for coordinates in itertools.product(range(3), repeat=len(basis)):
        q = tuple((projected_particular[index]
                   + sum(scalar * vector[index]
                         for scalar, vector in zip(coordinates, basis))) % 3
                  for index in range(4))
        value = source_omega(source_data, h, q)
        histogram[value] += fibre_factor
        if value == 0 and first_zero_q is None:
            first_zero_q = q
    assert sum(histogram) == 3 ** len(kernel)
    return (rank, augmented_rank), histogram, projected_particular, first_zero_q


shard_count = int(os.environ.get("SHARD_COUNT", "27"))
shard_index = int(os.environ["SHARD_INDEX"])
assert shard_count > 0 and 0 <= shard_index < shard_count
base_total = 3 ** len(structural)
start = base_total * shard_index // shard_count
stop = base_total * (shard_index + 1) // shard_count
zero_frob = {name: {} for name in frob}

q10_state_count = 0
q9_nonempty_state_count = 0
q9_completion_total = 0
omega_hist = [0, 0, 0]
zero_locus_classification = Counter()
q9_rank_pair_histogram = Counter()
q9_fibre_histogram = Counter()
per_base = {}
stream = hashlib.sha256()
first_zero_witness = None

for base_index, svalues in enumerate(
        itertools.product(range(3), repeat=len(structural))):
    if base_index < start:
        continue
    if base_index >= stop:
        break
    sassign = dict(zip(structural, svalues))
    Aparent = [[eval_expr(entry, sassign) for entry in row] for row in matrix]
    Fparent = [[eval_expr(coefficient(affine, name), sassign)
                for name in frob] for affine in rhs]
    b0 = [eval_expr(esubstitute(affine, zero_frob), sassign)
          for affine in rhs]
    pivots, work = rref_source(Aparent, Fparent, b0)
    local_states = 0
    local_completions = 0
    local_hist = [0, 0, 0]
    local_classes = Counter()
    for fvalues in itertools.product(range(3), repeat=len(frob)):
        for xvalues in affine_solutions(pivots, work, fvalues):
            assignment = dict(sassign)
            assignment.update(zip(frob, fvalues))
            assignment.update(zip(unknowns, xvalues))
            if any(eval_expr(test, assignment) for test in N12):
                continue
            if any(eval_expr(test, assignment) for test in Q11):
                continue
            if any(eval_expr(test, assignment) for test in Q10):
                continue
            q10_state_count += 1
            source_data = canonical_source(assignment)
            rank_pair, hist, projected_particular, first_zero_q = omega_histogram(
                source_data, assignment["h"] % 3)
            total = sum(hist)
            q9_rank_pair_histogram[rank_pair] += 1
            q9_fibre_histogram[total] += 1
            if not total:
                continue
            q9_nonempty_state_count += 1
            local_states += 1
            q9_completion_total += total
            local_completions += total
            for index in range(3):
                omega_hist[index] += hist[index]
                local_hist[index] += hist[index]
            if hist[0] == 0:
                classification = "zero-empty"
            elif hist[1] == hist[2] == 0:
                classification = "zero-full"
            else:
                classification = "zero-partial"
            zero_locus_classification[classification] += 1
            local_classes[classification] += 1
            state_bytes = bytes(svalues + fvalues + xvalues)
            stream.update(state_bytes)
            for count in hist:
                stream.update(count.to_bytes(16, "little"))
            if first_zero_witness is None and first_zero_q is not None:
                first_zero_witness = {
                    "base_index": base_index,
                    "predecessor_state": list(svalues + fvalues + xvalues),
                    "projected_q9_1_to_4": list(first_zero_q),
                    "projected_particular": list(projected_particular),
                    "omega_histogram": hist,
                }
    if local_states:
        per_base[str(base_index)] = {
            "structural_digits": list(svalues),
            "q9_nonempty_predecessor_states": local_states,
            "q9_completion_total": local_completions,
            "omega_histogram": local_hist,
            "zero_locus_classification": dict(sorted(local_classes.items())),
        }

result = {
    "status": "PASS-AS-GLOBAL-ROW8-Q9-PROJECTION-SHARD",
    "parent_sha256": EXPECTED,
    "shard_count": shard_count,
    "shard_index": shard_index,
    "structural_range": [start, stop],
    "q10_source_state_count": q10_state_count,
    "q9_nonempty_predecessor_state_count": q9_nonempty_state_count,
    "q9_completion_total": q9_completion_total,
    "omega_histogram": omega_hist,
    "zero_locus_classification": dict(sorted(zero_locus_classification.items())),
    "q9_rank_pair_histogram": {str(key): value
                               for key, value in sorted(
                                   q9_rank_pair_histogram.items())},
    "q9_fibre_histogram": {str(key): value
                           for key, value in sorted(q9_fibre_histogram.items())},
    "per_base": per_base,
    "first_zero_witness": first_zero_witness,
    "stream_sha256": stream.hexdigest(),
    "old_13_trit_canonical_chart_reused": False,
    "source_omega_replayed_on_every_projected_point": True,
    "refusal_scope": ["no Q8/Q7/Q6/Q5/Q4/Q3 restoration",
                      "no all-depth/counterexample/JC2 inference"],
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("shard", shard_index, "range", start, stop)
print("q10_states", q10_state_count, "q9_nonempty", q9_nonempty_state_count)
print("q9_completions", q9_completion_total, "omega", omega_hist)
print("classes", sorted(zero_locus_classification.items()))
print("stream_sha256", stream.hexdigest())
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-AS-GLOBAL-ROW8-Q9-PROJECTION-SHARD")
