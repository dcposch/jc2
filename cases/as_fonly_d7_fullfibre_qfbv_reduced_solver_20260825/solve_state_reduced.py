#!/usr/bin/env python3
"""Exact 19+9-trit full-fibre solver using the constant Q7 matrix."""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path

import z3

ROOT = Path(os.environ["JC2_ROOT"])
BASE = (ROOT / "cases/as_fonly_d7_fullfibre_qfbv_20260825"
        / "solve_state.py")
EXPECTED_BASE_SHA = (
    "d6345f8b22c220df42abad2a53d445ace2de13ffe9686d6996dea071587250ff")
payload = BASE.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_BASE_SHA
source = payload.decode()
marker = "\nsvars = [z3.BitVec(f\"s{index}\", WIDTH) for index in range(19)]\n"
assert source.count(marker) == 1
base_scope = {"__file__": str(BASE), "__name__": "__reduced_prefix__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(source.split(marker, 1)[0], str(BASE), "exec"), base_scope)

solver = base_scope["solver"]
bv = base_scope["bv"]
badd = base_scope["badd"]
bmul = base_scope["bmul"]
bscale = base_scope["bscale"]
padd = base_scope["padd"]
pscale = base_scope["pscale"]
pmul = base_scope["pmul"]
pderivative = base_scope["pderivative"]
pbracket = base_scope["pbracket"]
degree_part = base_scope["degree_part"]
lift_poly = base_scope["lift_poly"]
homogeneous = base_scope["homogeneous"]
divide_three = base_scope["divide_three"]
constrain_row_zero = base_scope["constrain_row_zero"]
source_data = base_scope["source_data"]
source_rows = base_scope["source_rows"]
transition_rows = base_scope["transition_rows"]
xvalues = base_scope["xvalues"]
y0 = base_scope["y0"]
kernel8 = base_scope["kernel8"]
add_vector = base_scope["add_vector"]
rref_solve = base_scope["rref_solve"]
kernel_basis = base_scope["kernel_basis"]
new_polynomials = base_scope["new_polynomials"]
q7_rows_numeric = base_scope["q7_rows_numeric"]
recursive_high_numeric = base_scope["recursive_high_numeric"]
direct_high_numeric = base_scope["direct_high_numeric"]
parent_scope = base_scope["scope"]
WIDTH = base_scope["WIDTH"]
MODULUS = base_scope["MODULUS"]
state_index = base_scope["state_index"]
parameters = base_scope["parameters"]
canonical_label = base_scope["canonical_label"]
presentation_signature = base_scope["presentation_signature"]
timeout_ms = base_scope["timeout_ms"]


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
    matrix = [[columns[column][row] for column in range(variable_count)]
              for row in range(len(b))]
    ones = (1,) * variable_count
    assert function(ones) == [
        (b[row] + sum(matrix[row])) % 3 for row in range(len(b))]
    return matrix, [value % 3 for value in b]


parent_scope["xvalues"] = xvalues
parent_scope["yvalues"] = y0
matrix7, _b7_numeric = affine_matrix(q7_rows_numeric, 18)
matrix_bytes = (json.dumps(matrix7, separators=(",", ":")) + "\n").encode()
EXPECTED_MATRIX_SHA = (
    "5a8395d4f9f06adec44410ddfed5085c0c3833c9bdb57f5a76fe608524d51790")
assert hashlib.sha256(matrix_bytes).hexdigest() == EXPECTED_MATRIX_SHA
rank7, augmented7, pivot_columns, rref7, zero7 = rref_solve(
    matrix7, [0] * len(matrix7))
assert rank7 == augmented7 == 9 and zero7 is not None
kernel_rank7, kernel7 = kernel_basis(matrix7)
assert kernel_rank7 == 9 and len(kernel7) == 9
free_columns = tuple(column for column in range(18)
                     if column not in pivot_columns)
assert len(free_columns) == 9

# Pick independent source rows in their original order.
pivot_rows = []
seen_rank = 0
for row_index in range(len(matrix7)):
    trial = matrix7[:row_index + 1]
    rank, _augmented, _pivots, _rref, _witness = rref_solve(
        trial, [0] * len(trial))
    if rank > seen_rank:
        pivot_rows.append(row_index)
        seen_rank = rank
assert pivot_rows == [0, 2, 3, 5, 6, 7, 9, 10, 12]


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
    assert all(work[i][j] == int(i == j)
               for i in range(size) for j in range(size))
    return [row[size:] for row in work]


pivot_matrix = [[matrix7[row][column] for column in pivot_columns]
                for row in pivot_rows]
pivot_inverse = inverse_mod3(pivot_matrix)

svars = [z3.BitVec(f"s{index}", WIDTH) for index in range(19)]
uvars = [z3.BitVec(f"u{index}", WIDTH) for index in range(9)]
for variable in svars + uvars:
    solver.add(z3.ULE(variable, bv(2)))

yvalues_symbolic = []
for column in range(32):
    expression = bv(y0[column])
    for index in range(19):
        expression = badd(expression, bmul(kernel8[index][column], svars[index]))
    yvalues_symbolic.append(z3.URem(expression, bv(3)))

C2n, D2n, C4n, D4n, W7n, Z7n = new_polynomials(xvalues)
C2, D2, C4, D4, W7, Z7 = map(
    lift_poly, (C2n, D2n, C4n, D4n, W7n, Z7n))
C3 = homogeneous(3, yvalues_symbolic[0:4])
D3 = homogeneous(3, yvalues_symbolic[4:8])
W4 = homogeneous(4, yvalues_symbolic[8:13])
Z4 = homogeneous(4, yvalues_symbolic[13:18])
W6 = homogeneous(6, yvalues_symbolic[18:25])
Z6 = homogeneous(6, yvalues_symbolic[25:32])
A = lift_poly(source_data["A"])
uy = lift_poly(source_data["uy"])
vx = lift_poly(source_data["vx"])
vy = lift_poly(source_data["vy"])


def components(restoration):
    C6 = homogeneous(6, [restoration[0], 0, 0, restoration[1],
                         0, 0, restoration[2]])
    D6 = homogeneous(6, [restoration[3], 0, 0, restoration[4],
                         0, 0, restoration[5]])
    W5 = homogeneous(5, restoration[6:12])
    Z5 = homogeneous(5, restoration[12:18])
    C = padd(lift_poly(source_data["Cbase"]), C2, C3, C4, C6)
    D = padd(lift_poly(source_data["Dbase"]), D2, D3, D4, D6)
    W = padd(W4, W5, W6, W7)
    Z = padd(Z4, Z5, Z6, Z7)
    return C, D, W, Z


def intermediates(restoration):
    C, D, W, Z = components(restoration)
    E = padd(lift_poly(source_data["L1"]), lift_poly(source_data["K"]),
              pderivative(C, 0), pderivative(D, 1))
    cx, cy = pderivative(C, 0), pderivative(C, 1)
    dx, dy = pderivative(D, 0), pderivative(D, 1)
    M = padd(pmul(A, dy), pmul(cx, vy), pscale(-1, pmul(uy, dx)),
              pscale(-1, pmul(cy, vx)))
    N = pbracket(C, D)
    T = padd(pmul(A, pderivative(Z, 1)), pmul(pderivative(W, 0), vy),
              pscale(-1, pmul(uy, pderivative(Z, 0))),
              pscale(-1, pmul(pderivative(W, 1), vx)))
    Rmix = padd(pmul(cx, pderivative(Z, 1)), pmul(pderivative(W, 0), dy),
                pscale(-1, pmul(cy, pderivative(Z, 0))),
                pscale(-1, pmul(pderivative(W, 1), dx)))
    return C, D, W, Z, E, M, N, T, Rmix


def coefficient_row(poly, total):
    return [z3.URem(poly.get((index, total - index), bv(0)), bv(3))
            for index in range(total + 1)]


def q7_residual(restoration):
    _C, _D, W, Z, E, M, N, T, _Rmix = intermediates(restoration)
    E1_4 = divide_three(degree_part(E, 4))
    E1_5 = divide_three(degree_part(E, 5))
    E1_7 = divide_three(degree_part(E, 7))
    divWZ = padd(pderivative(W, 0), pderivative(Z, 1))
    F4 = padd(E1_4, degree_part(M, 4), degree_part(divWZ, 4))
    F5 = padd(E1_5, degree_part(M, 5), degree_part(divWZ, 5))
    F7 = padd(E1_7, degree_part(M, 7))
    F1_7 = divide_three(F7)
    G7 = padd(F1_7, degree_part(N, 7), degree_part(T, 7))
    return coefficient_row(F5, 5) + coefficient_row(F4, 4) + coefficient_row(G7, 7)


b7_symbolic = q7_residual([bv(0)] * 18)
assert len(b7_symbolic) == 19
restoration = [None] * 18
for index, column in enumerate(free_columns):
    restoration[column] = uvars[index]
for pivot_index, column in enumerate(pivot_columns):
    expression = bv(0)
    for source_index, row in enumerate(pivot_rows):
        coefficient = (-pivot_inverse[pivot_index][source_index]) % 3
        expression = badd(expression, bmul(coefficient, b7_symbolic[row]))
    for free_index, free_column in enumerate(free_columns):
        coefficient = 0
        for source_index, row in enumerate(pivot_rows):
            coefficient -= (pivot_inverse[pivot_index][source_index]
                            * matrix7[row][free_column])
        expression = badd(expression, bmul(coefficient % 3, uvars[free_index]))
    restoration[column] = z3.URem(expression, bv(3))
assert all(value is not None for value in restoration)

# The nine pivot rows vanish by construction.  These ten equations are the
# exact remaining Q7 compatibility/cokernel conditions.
nonpivot_rows = [row for row in range(19) if row not in pivot_rows]
for row in nonpivot_rows:
    residual = b7_symbolic[row]
    for column in range(18):
        residual = badd(residual, bmul(matrix7[row][column], restoration[column]))
    solver.add(z3.URem(residual, bv(3)) == bv(0))

C, D, W, Z, E, M, N, T, Rmix = intermediates(restoration)
divWZ = padd(pderivative(W, 0), pderivative(Z, 1))
for degree in range(9, 13):
    E1 = divide_three(degree_part(E, degree))
    F = padd(E1, degree_part(M, degree), degree_part(divWZ, degree))
    F1 = divide_three(F)
    G = padd(F1, degree_part(N, degree), degree_part(T, degree))
    G1 = divide_three(G)
    R = padd(G1, degree_part(Rmix, degree))
    constrain_row_zero(R, degree)

smt2 = solver.to_smt2().encode()
Path(os.environ["SMT2_OUTPUT"]).write_bytes(smt2)
check = solver.check()
status = str(check)
result = {
    "state_index": state_index,
    "parameters": list(parameters),
    "canonical_label": canonical_label,
    "presentation_signature": presentation_signature,
    "solver_status": status,
    "solver_timeout_ms": timeout_ms,
    "z3_version": z3.get_version_string(),
    "bit_width": WIDTH,
    "residue_modulus": MODULUS,
    "largest_product_bound": 728 * 728,
    "q7_matrix_sha256": EXPECTED_MATRIX_SHA,
    "q7_matrix_rank": rank7,
    "q7_free_dimension": 9,
    "q7_compatibility_row_count": len(nonpivot_rows),
    "division_constraint_count": base_scope["division_constraint_count"],
    "smt2_sha256": hashlib.sha256(smt2).hexdigest(),
    "unsat_is_theorem": False,
    "scope": "one fixed Q9 state; full 19D Q8 and parameterized 9D Q7 fibres",
}

if check == z3.sat:
    model = solver.model()
    svalues = [model.eval(variable, model_completion=True).as_long()
               for variable in svars]
    uvalues = [model.eval(variable, model_completion=True).as_long()
               for variable in uvars]
    rvalues = [model.eval(value, model_completion=True).as_long()
               for value in restoration]
    assert all(0 <= value <= 2 for value in svalues + uvalues + rvalues)
    yvalues = add_vector(y0, kernel8, svalues, reduce=True)
    assert transition_rows(xvalues, yvalues) == [0] * 22
    parent_scope["xvalues"] = xvalues
    parent_scope["yvalues"] = yvalues
    assert q7_rows_numeric(rvalues) == [0] * 19
    Cn, Dn, Wn, Zn, recursive = recursive_high_numeric(rvalues)
    direct = direct_high_numeric(Cn, Dn, Wn, Zn)
    assert recursive == direct
    high = [value for degree in range(12, 8, -1)
            for value in recursive[degree]]
    assert not any(high)
    result.update({
        "svalues": svalues,
        "uvalues": uvalues,
        "rvalues": rvalues,
        "yvalues": list(yvalues),
        "direct_integer_div243_replay": "PASS",
        "high_row_vector": high,
        "smooth_hensel_surjective": False,
        "next_correction_jacobian_shape": [28, 72],
        "next_correction_jacobian_rank_mod3": 27,
        "cartier_cokernel_carrier": "x^2*y^2",
    })
elif check == z3.unknown:
    result["unknown_reason"] = solver.reason_unknown()

result["solver_statistics"] = str(solver.statistics())
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("state_label", state_index, canonical_label)
print("solver_status", status)
print("z3_version", z3.get_version_string())
print("q7_free_dimension", 9)
print("q7_compatibility_row_count", len(nonpivot_rows))
print("division_constraint_count", base_scope["division_constraint_count"])
print("smt2_sha256", result["smt2_sha256"])
print("sat_direct_replay", result.get("direct_integer_div243_replay"))
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-AS-FULLFIBRE-QFBV-REDUCED-STATE")

