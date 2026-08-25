#!/usr/bin/env python3
"""Exact widened-BV existential Q8/Q7/next-high solver for one Q9 state."""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path

import z3

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
assert source.count(family_marker) == source.count(restored_marker) == 1
assert source.count(result_marker) == 1
scope = {"__file__": str(PARENT), "__name__": "__qfbv_prefix__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(source.split(family_marker, 1)[0], str(PARENT), "exec"), scope)
fragment = (restored_marker
            + source.split(restored_marker, 1)[1].split(result_marker, 1)[0])
exec(compile(fragment, str(PARENT), "exec"), scope)

source_data = scope["source_data"]
source_rows = scope["source_rows"]
transition_rows = scope["transition_rows"]
matrix_and_rhs = scope["matrix_and_rhs"]
q9_origin = tuple(scope["q9_origin"])
q9_kernel = tuple(scope["q9_kernel"])
q8_variable_count = scope["q8_variable_count"]
add_vector = scope["add_vector"]
rref_solve = scope["rref_solve"]
kernel_basis = scope["kernel_basis"]
new_polynomials = scope["new_polynomials"]
q7_rows_numeric = scope["q7_rows"]
recursive_high_numeric = scope["recursive_high"]
direct_high_numeric = scope["direct_high"]

state_index = int(os.environ["STATE_INDEX"])
canonical_label = os.environ["CANONICAL_LABEL"]
presentation_signature = os.environ["PRESENTATION_SIGNATURE"]
timeout_ms = int(os.environ.get("SOLVER_TIMEOUT_MS", "7200000"))
assert 0 <= state_index < 3 ** 13

def ternary(index: int, width: int) -> tuple[int, ...]:
    answer = []
    for _ in range(width):
        answer.append(index % 3)
        index //= 3
    assert index == 0
    return tuple(answer)

parameters = ternary(state_index, 13)
forced = {10: 0, 11: 0, 12: 0, 13: 0, 15: 0, 17: 1}
free_q9 = tuple(index for index in range(19) if index not in forced)
t = [0] * 19
for index, value in forced.items():
    t[index] = value
for index, value in zip(free_q9, parameters):
    t[index] = value
xvalues = add_vector(q9_origin, q9_kernel, t, reduce=True)
assert source_rows(source_data, xvalues) == [0] * 23
A8, b8 = matrix_and_rhs(transition_rows, xvalues, q8_variable_count)
rank8, augmented8, _p8, _w8, y0 = rref_solve(A8, b8)
assert (rank8, augmented8) == (13, 13) and y0 is not None
kernel_rank8, kernel8 = kernel_basis(A8)
assert kernel_rank8 == rank8 and len(kernel8) == 19

WIDTH = 32
MODULUS = 729
assert 728 * 728 == 529984 < 2 ** 20 < 2 ** WIDTH
BV_MOD = z3.BitVecVal(MODULUS, WIDTH)
BV_THREE = z3.BitVecVal(3, WIDTH)

def bv(value):
    if isinstance(value, int):
        return z3.BitVecVal(value % MODULUS, WIDTH)
    assert z3.is_bv(value) and value.size() == WIDTH
    return value

def bred(value):
    return z3.URem(bv(value), BV_MOD)

def badd(*values):
    total = bv(0)
    for value in values:
        total = bred(total + bv(value))
    return total

def bmul(left, right):
    # Both operands are canonical residues <=728, so the 32-bit product cannot
    # wrap before reduction.
    return bred(bv(left) * bv(right))

def bscale(scalar, value):
    return bmul(bv(scalar), value)

def padd(*polys):
    keys = set().union(*(poly.keys() for poly in polys))
    return {key: badd(*(poly.get(key, 0) for poly in polys)) for key in keys}

def pscale(scalar, poly):
    return {key: bscale(scalar, value) for key, value in poly.items()}

def pmul(left, right):
    answer = {}
    for (i, j), a in left.items():
        for (k, ell), b in right.items():
            key = (i + k, j + ell)
            answer[key] = badd(answer.get(key, 0), bmul(a, b))
    return answer

def pderivative(poly, axis):
    answer = {}
    for (i, j), value in poly.items():
        exponent = i if axis == 0 else j
        if exponent:
            key = (i - 1, j) if axis == 0 else (i, j - 1)
            answer[key] = badd(answer.get(key, 0), bscale(exponent, value))
    return answer

def pbracket(left, right):
    return padd(pmul(pderivative(left, 0), pderivative(right, 1)),
                pscale(-1, pmul(pderivative(left, 1),
                                pderivative(right, 0))))

def degree_part(poly, total):
    return {key: value for key, value in poly.items() if sum(key) == total}

def lift_poly(poly):
    return {key: bv(value) for key, value in poly.items()}

def homogeneous(degree, values):
    assert len(values) == degree + 1
    return {(index, degree - index): bv(value)
            for index, value in enumerate(values)}

solver = z3.Solver()
solver.set(timeout=timeout_ms)
solver.set(random_seed=0)
division_constraint_count = 0

def divide_three(poly):
    global division_constraint_count
    answer = {}
    for key, value in poly.items():
        solver.add(z3.URem(value, BV_THREE) == bv(0))
        division_constraint_count += 1
        answer[key] = z3.UDiv(value, BV_THREE)
    return answer

def constrain_row_zero(poly, total):
    for index in range(total + 1):
        solver.add(z3.URem(poly.get((index, total - index), bv(0)),
                          BV_THREE) == bv(0))

svars = [z3.BitVec(f"s{index}", WIDTH) for index in range(19)]
rvars = [z3.BitVec(f"r{index}", WIDTH) for index in range(18)]
for variable in svars + rvars:
    solver.add(z3.ULE(variable, bv(2)))

yvalues_symbolic = []
for column in range(q8_variable_count):
    expression = bv(y0[column])
    for index in range(19):
        expression = badd(expression, bmul(kernel8[index][column], svars[index]))
    yvalues_symbolic.append(z3.URem(expression, BV_THREE))

C2n, D2n, C4n, D4n, W7n, Z7n = new_polynomials(xvalues)
C2, D2, C4, D4, W7, Z7 = map(
    lift_poly, (C2n, D2n, C4n, D4n, W7n, Z7n))
C3 = homogeneous(3, yvalues_symbolic[0:4])
D3 = homogeneous(3, yvalues_symbolic[4:8])
W4 = homogeneous(4, yvalues_symbolic[8:13])
Z4 = homogeneous(4, yvalues_symbolic[13:18])
W6 = homogeneous(6, yvalues_symbolic[18:25])
Z6 = homogeneous(6, yvalues_symbolic[25:32])
C6 = homogeneous(6, [rvars[0], 0, 0, rvars[1], 0, 0, rvars[2]])
D6 = homogeneous(6, [rvars[3], 0, 0, rvars[4], 0, 0, rvars[5]])
W5 = homogeneous(5, rvars[6:12])
Z5 = homogeneous(5, rvars[12:18])

C = padd(lift_poly(source_data["Cbase"]), C2, C3, C4, C6)
D = padd(lift_poly(source_data["Dbase"]), D2, D3, D4, D6)
W = padd(W4, W5, W6, W7)
Z = padd(Z4, Z5, Z6, Z7)
A = lift_poly(source_data["A"])
uy = lift_poly(source_data["uy"])
vx = lift_poly(source_data["vx"])
vy = lift_poly(source_data["vy"])
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

E1_4 = divide_three(degree_part(E, 4))
E1_5 = divide_three(degree_part(E, 5))
E1_7 = divide_three(degree_part(E, 7))
divWZ = padd(pderivative(W, 0), pderivative(Z, 1))
F4 = padd(E1_4, degree_part(M, 4), degree_part(divWZ, 4))
F5 = padd(E1_5, degree_part(M, 5), degree_part(divWZ, 5))
F7 = padd(E1_7, degree_part(M, 7))
F1_7 = divide_three(F7)
G7 = padd(F1_7, degree_part(N, 7), degree_part(T, 7))
constrain_row_zero(F5, 5)
constrain_row_zero(F4, 4)
constrain_row_zero(G7, 7)

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
    "q8_rank_pair": [rank8, augmented8],
    "solver_status": status,
    "solver_timeout_ms": timeout_ms,
    "bit_width": WIDTH,
    "residue_modulus": MODULUS,
    "largest_product_bound": 728 * 728,
    "division_constraint_count": division_constraint_count,
    "smt2_sha256": hashlib.sha256(smt2).hexdigest(),
    "unsat_is_theorem": False,
    "scope": "one fixed Q9 state; existential full canonical Q8 kernel and raw Q7 digits",
}

def matrix_rank_mod3(matrix):
    work = [[value % 3 for value in row] for row in matrix]
    rank = 0
    for column in range(len(work[0])):
        pivot = next((row for row in range(rank, len(work))
                      if work[row][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        if work[rank][column] == 2:
            work[rank] = [(2 * value) % 3 for value in work[rank]]
        for row in range(len(work)):
            if row != rank and work[row][column]:
                scalar = work[row][column]
                work[row] = [(left - scalar * right) % 3
                             for left, right in zip(work[row], work[rank])]
        rank += 1
    return rank

if check == z3.sat:
    model = solver.model()
    svalues = [model.eval(variable, model_completion=True).as_long()
               for variable in svars]
    rvalues = [model.eval(variable, model_completion=True).as_long()
               for variable in rvars]
    assert all(0 <= value <= 2 for value in svalues + rvalues)
    yvalues = add_vector(y0, kernel8, svalues, reduce=True)
    assert transition_rows(xvalues, yvalues) == [0] * 22
    scope["xvalues"] = xvalues
    scope["yvalues"] = yvalues
    assert q7_rows_numeric(rvalues) == [0] * 19
    Cn, Dn, Wn, Zn, recursive = recursive_high_numeric(rvalues)
    direct = direct_high_numeric(Cn, Dn, Wn, Zn)
    assert recursive == direct
    high = [value for degree in range(12, 8, -1)
            for value in recursive[degree]]
    assert not any(high)

    outputs = [(i, total - i) for total in range(7)
               for i in range(total + 1)]
    inputs = [(axis, i, total - i) for axis in range(2)
              for total in range(8) for i in range(total + 1)]
    jacobian = []
    for out_i, out_j in outputs:
        row = []
        for axis, in_i, in_j in inputs:
            if axis == 0 and (in_i - 1, in_j) == (out_i, out_j):
                row.append(in_i % 3)
            elif axis == 1 and (in_i, in_j - 1) == (out_i, out_j):
                row.append(in_j % 3)
            else:
                row.append(0)
        jacobian.append(row)
    divergence_rank = matrix_rank_mod3(jacobian)
    assert len(outputs) == 28 and divergence_rank == 27
    cartier_row = outputs.index((2, 2))
    assert not any(jacobian[cartier_row])
    result.update({
        "svalues": svalues,
        "rvalues": rvalues,
        "yvalues": list(yvalues),
        "direct_integer_div243_replay": "PASS",
        "high_row_vector": high,
        "next_correction_jacobian_shape": [28, 72],
        "next_correction_jacobian_rank_mod3": divergence_rank,
        "smooth_hensel_surjective": False,
        "cartier_cokernel_carrier": "x^2*y^2",
        "hensel_scope": "cap-seven next-correction divergence operator",
    })
elif check == z3.unknown:
    result["unknown_reason"] = solver.reason_unknown()

result["solver_statistics"] = str(solver.statistics())
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("state_label", state_index, canonical_label)
print("solver_status", status)
print("division_constraint_count", division_constraint_count)
print("smt2_sha256", result["smt2_sha256"])
print("sat_direct_replay", result.get("direct_integer_div243_replay"))
print("smooth_hensel_surjective", result.get("smooth_hensel_surjective"))
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-AS-FULLFIBRE-QFBV-STATE")
