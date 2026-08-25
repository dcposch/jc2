#!/usr/bin/env python3
"""Fused exact affine Q3--Q0 completion at one full-Q4 point."""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
PARENT = (ROOT / "cases/as_fonly_d7_q5_sat_q4_full68_gate_20260825"
          / "solve_full68.py")
EXPECTED_PARENT_SHA = (
    "ed19ea87d2252e9e483a5c3970549eeac2db62d064e7bd900698b600739180a4")
payload = PARENT.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_PARENT_SHA

parent_output = Path(os.environ["PARENT_OUTPUT_JSON"])
old_output = os.environ.get("OUTPUT_JSON")
os.environ["OUTPUT_JSON"] = str(parent_output)
namespace = {"__file__": str(PARENT), "__name__": "__fused_parent__"}
with contextlib.redirect_stdout(io.StringIO()) as parent_stdout:
    exec(compile(payload, str(PARENT), "exec"), namespace)
if old_output is None:
    del os.environ["OUTPUT_JSON"]
else:
    os.environ["OUTPUT_JSON"] = old_output

assert namespace["consistent"]
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
q4_particular = list(namespace["particular"])
q4_kernel = [list(vector) for vector in namespace["kernel"]]
kdim = len(q4_kernel)
assert len(q4_particular) == 12

fresh_degrees = (4, 3, 2, 1)
fresh_count = sum(2 * (degree + 1) for degree in fresh_degrees)
variable_count = kdim + fresh_count


def candidate(values):
    assert len(values) == variable_count
    q4_values = list(q4_particular)
    for scalar, vector in zip(values[:kdim], q4_kernel):
        q4_values = [(entry + scalar * direction) % 3
                     for entry, direction in zip(q4_values, vector)]
    Hsum = homogeneous_numeric(5, q4_values[:6])
    Jsum = homogeneous_numeric(5, q4_values[6:])
    offset = kdim
    blocks = []
    for degree in fresh_degrees:
        width = degree + 1
        hvalues = values[offset:offset + width]
        offset += width
        jvalues = values[offset:offset + width]
        offset += width
        H = homogeneous_numeric(degree, hvalues)
        J = homogeneous_numeric(degree, jvalues)
        Hsum = nadd(Hsum, H)
        Jsum = nadd(Jsum, J)
        blocks.append([degree, hvalues, jvalues])
    assert offset == variable_count
    P = nadd(P5, nscale(81, Hsum))
    Q = nadd(Q5, nscale(81, Jsum))
    return P, Q, q4_values, blocks


def equation_rows(values):
    P, Q, _, _ = candidate(values)
    determinant = determinant_minus_one(P, Q)
    source_rows = []
    for degree in (4, 3, 2, 1, 0):
        source_rows.extend(
            row(divide_exact(degree_part(determinant, degree), 81), degree))
    terminal_rows = []
    for degree in range(7, 13):
        terminal_rows.extend(
            row(divide_exact(degree_part(determinant, degree), 243), degree))
    assert len(source_rows) == 15 and len(terminal_rows) == 63
    return [(value % 3) for value in source_rows + terminal_rows]


zero_values = [0] * variable_count
constant = equation_rows(zero_values)
columns = []
for index in range(variable_count):
    basis = [0] * variable_count
    basis[index] = 1
    at_one = equation_rows(basis)
    columns.append([(value - base) % 3
                    for value, base in zip(at_one, constant)])

# Complete degree-two design.  The determinant is visibly quadratic in the
# digit variables, so vanishing of every square and mixed second difference
# proves this extracted map is affine on the whole F3 cube.
design_count = 1 + 2 * variable_count
for index in range(variable_count):
    twice = [0] * variable_count
    twice[index] = 2
    expected = [(base + 2 * delta) % 3
                for base, delta in zip(constant, columns[index])]
    assert equation_rows(twice) == expected
for left in range(variable_count):
    for right in range(left + 1, variable_count):
        pair = [0] * variable_count
        pair[left] = pair[right] = 1
        expected = [(base + ldelta + rdelta) % 3
                    for base, ldelta, rdelta in zip(
                        constant, columns[left], columns[right])]
        assert equation_rows(pair) == expected
        design_count += 1

matrix = [[columns[column][row_index]
           for column in range(variable_count)] for row_index in range(78)]
rhs = [(-value) % 3 for value in constant]


def rref_solve(left, right):
    columns_count = len(left[0])
    work = [[value % 3 for value in row_values] + [target % 3]
            for row_values, target in zip(left, right)]
    pivots = []
    pivot_row = 0
    for column in range(columns_count):
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
                    (value - scalar * pivot) % 3
                    for value, pivot in zip(work[row_index], work[pivot_row])]
        pivots.append(column)
        pivot_row += 1
    contradictions = [row_values for row_values in work
                      if not any(row_values[:-1]) and row_values[-1]]
    if contradictions:
        return len(pivots), len(pivots) + 1, pivots, None, [], contradictions
    particular = [0] * columns_count
    for row_index, column in enumerate(pivots):
        particular[column] = work[row_index][-1]
    free = [column for column in range(columns_count) if column not in pivots]
    kernel = []
    for free_column in free:
        vector = [0] * columns_count
        vector[free_column] = 1
        for row_index, pivot_column in enumerate(pivots):
            vector[pivot_column] = (-work[row_index][free_column]) % 3
        kernel.append(vector)
    return len(pivots), len(pivots), pivots, particular, kernel, []


# Sequential Q3 equivalence control: Q3 rows occupy source indices 5..8;
# the terminal rows occupy 15..77.  Only the old Q4 kernel and H4/J4 are live.
sequential_rows = list(range(5, 9)) + list(range(15, 78))
sequential_columns = kdim + 10
seq_matrix = [[matrix[row_index][column]
               for column in range(sequential_columns)]
              for row_index in sequential_rows]
seq_rhs = [rhs[row_index] for row_index in sequential_rows]
(seq_rank, seq_augmented_rank, seq_pivots, seq_particular,
 seq_kernel, seq_contradictions) = rref_solve(seq_matrix, seq_rhs)

(rank, augmented_rank, pivots, particular,
 kernel, contradictions) = rref_solve(matrix, rhs)
consistent = particular is not None

result = {
    "status": ("PASS-AS-Q5-FUSED-Q3-Q0-SAT" if consistent
               else "PASS-AS-Q5-FUSED-Q3-Q0-UNSAT"),
    "parent_sha256": EXPECTED_PARENT_SHA,
    "model_sha256": hashlib.sha256(
        Path(os.environ["MODEL_OUTPUT"]).read_bytes()).hexdigest(),
    "parent_output_sha256": hashlib.sha256(parent_output.read_bytes()).hexdigest(),
    "parent_stdout_sha256": hashlib.sha256(
        parent_stdout.getvalue().encode()).hexdigest(),
    "q4_kernel_dimension_consumed": kdim,
    "fresh_h4_through_h1_variable_count": fresh_count,
    "constant_translation_spectator_dimension_omitted": 2,
    "matrix_shape": [78, variable_count],
    "matrix_sha256": hashlib.sha256(bytes(
        value for row_values in matrix for value in row_values)).hexdigest(),
    "rhs_sha256": hashlib.sha256(bytes(rhs)).hexdigest(),
    "quadratic_design_point_count": design_count,
    "affine_whole_cube_proof_from_quadratic_design": True,
    "sequential_q3": {
        "matrix_shape": [67, sequential_columns],
        "rank": seq_rank,
        "augmented_rank": seq_augmented_rank,
        "consistent": seq_particular is not None,
        "particular": seq_particular,
        "kernel_dimension": len(seq_kernel),
        "contradictions": seq_contradictions,
    },
    "rank": rank,
    "augmented_rank": augmented_rank,
    "pivot_columns": pivots,
    "consistent": consistent,
    "particular": particular,
    "kernel_dimension": len(kernel),
    "solution_count_excluding_constant_translations": (
        3 ** len(kernel) if consistent else 0),
    "contradictions": contradictions,
    "zero_lower_digit_control_nonzero_rows": [
        index for index, value in enumerate(constant) if value],
    "full_integer_replay_passed": False,
    "scope": "one exact Q5/Q4 affine fibre; fused Q3--Q0 finite-depth gate",
    "refusal_scope": [
        "not the whole Q5 locus",
        "one finite depth, not an inverse-compatible tower",
        "no Q3-adic/Qbar/C point, counterexample, or JC2 inference",
    ],
}

if consistent:
    assert equation_rows(particular) == [0] * 78
    P, Q, q4_values, blocks = candidate(particular)
    determinant = determinant_minus_one(P, Q)
    assert all(value % 243 == 0 for value in determinant.values())
    assert all(value % 729 == 0 for (i, j), value in determinant.items()
               if 7 <= i + j <= 12)
    assert max(i + j for i, j in P) <= 7
    assert max(i + j for i, j in Q) <= 7

    seed_P = {(1, 0): 1, (3, 0): -1}
    seed_Q = {(0, 1): 1}
    assert all(P.get(key, 0) % 3 == seed_P.get(key, 0) % 3
               for key in set(P) | set(seed_P))
    assert all(Q.get(key, 0) % 3 == seed_Q.get(key, 0) % 3
               for key in set(Q) | set(seed_Q))

    def evaluate(poly, xvalue, yvalue):
        return sum(coefficient * xvalue ** i * yvalue ** j
                   for (i, j), coefficient in poly.items())

    def lift_zero(residue_x):
        xvalue, yvalue = residue_x, 0
        trace = [[1, xvalue, yvalue]]
        for exponent in range(1, 5):
            modulus = 3 ** exponent
            pvalue = evaluate(P, xvalue, yvalue)
            qvalue = evaluate(Q, xvalue, yvalue)
            assert pvalue % modulus == 0 and qvalue % modulus == 0
            # JF is the identity modulo three on the AS seed.
            xvalue += modulus * (-(pvalue // modulus) % 3)
            yvalue += modulus * (-(qvalue // modulus) % 3)
            trace.append([exponent + 1, xvalue, yvalue])
        assert evaluate(P, xvalue, yvalue) % 243 == 0
        assert evaluate(Q, xvalue, yvalue) % 243 == 0
        return [xvalue, yvalue], trace

    lifted = [lift_zero(residue) for residue in (0, 1, 2)]
    preimages = [entry[0] for entry in lifted]
    assert len({tuple(point) for point in preimages}) == 3

    def support(poly):
        return [[i, j, value] for (i, j), value in sorted(poly.items())
                if value]

    result.update({
        "full_integer_replay_passed": True,
        "q4_coefficients": q4_values,
        "lower_digit_blocks": blocks,
        "literal_determinant_minus_one_divisible_by_243": True,
        "terminal_degrees_7_to_12_divisible_by_729": True,
        "reduces_exactly_to_AS_seed_mod3": True,
        "total_degree_cap": 7,
        "P_support": support(P),
        "Q_support": support(Q),
        "target_zero_preimages_mod243": preimages,
        "hensel_traces": [entry[1] for entry in lifted],
    })

encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("variables", variable_count, "design_points", design_count)
print("sequential_q3", seq_rank, seq_augmented_rank,
      seq_particular is not None, "kernel", len(seq_kernel))
print("fused", rank, augmented_rank, consistent, "kernel", len(kernel))
print("zero_control_nonzero", len(result["zero_lower_digit_control_nonzero_rows"]))
if consistent:
    print("preimages_mod243", result["target_zero_preimages_mod243"])
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])

