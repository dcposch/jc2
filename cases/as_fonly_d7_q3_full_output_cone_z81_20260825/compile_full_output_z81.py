#!/usr/bin/env python3
"""Exact nonlinear fourth-stage compiler for the complete fixed-D7 cone."""

from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
PARENT = (ROOT / "cases/as_fonly_d7_q3_full_output_cone_z27_20260825"
          / "solve_full_output_cone_z27.py")
EXPECTED_PARENT = (
    "f6eaa0a0f1dabb785bdd4358fa84739d907820bc539cc619a1b692ad5755cb19")
payload = PARENT.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_PARENT

# Execute the frozen parent with its own output redirected to a custody file.
saved_output = os.environ["OUTPUT_JSON"]
os.environ["OUTPUT_JSON"] = os.environ["PARENT_REPLAY_JSON"]
ns = {"__file__": str(PARENT), "__name__": "__z81_parent__"}
with contextlib.redirect_stdout(io.StringIO()) as parent_stdout:
    exec(compile(payload, str(PARENT), "exec"), ns)
os.environ["OUTPUT_JSON"] = saved_output

assert ns["p2"] is not None
slots = list(ns["slots"])
support = list(ns["support"])
base_integer = list(ns["base_integer"])
matrix_integer = [list(row) for row in ns["matrix_integer"]]
A3 = [list(row) for row in ns["A3"]]
K1 = [list(vector) for vector in ns["K1"]]
K2 = [list(vector) for vector in ns["K2"]]
p2 = list(ns["p2"])
T9_base = list(ns["T9_base"])
T9_directions = [list(vector) for vector in ns["T9_directions"]]
rref_solve = ns["rref_solve"]
rank = ns["rank"]
correction = ns["correction"]
candidate = ns["candidate"]
determinant_minus_one = ns["determinant_minus_one"]
nadd, nscale = ns["nadd"], ns["nscale"]
coefficient = ns["coefficient"]
P0, Q0 = ns["P0"], ns["Q0"]

assert len(slots) == 91 and len(support) == 36
assert len(matrix_integer) == 91 and len(matrix_integer[0]) == 72


def dot(left, right):
    return sum(a * b for a, b in zip(left, right))


def stage2_base(vector):
    assert len(vector) == len(K1) + 72
    answer = list(T9_base)
    for scalar, direction in zip(vector[:len(K1)], T9_directions):
        answer = [value + scalar * delta
                  for value, delta in zip(answer, direction)]
    answer = [value + 9 * digit
              for value, digit in zip(answer, vector[len(K1):])]
    return answer


def stage2_direction(vector):
    assert len(vector) == len(K1) + 72
    answer = [0] * 72
    for scalar, direction in zip(vector[:len(K1)], T9_directions):
        answer = [value + scalar * delta
                  for value, delta in zip(answer, direction)]
    answer = [value + 9 * digit
              for value, digit in zip(answer, vector[len(K1):])]
    return answer


T_base = stage2_base(p2)
T_directions = [stage2_direction(vector) for vector in K2]
parameter_count = len(T_directions)
assert parameter_count in (97, 106)
assert all((base_integer[row] + dot(matrix_integer[row], T_base)) % 27 == 0
           for row in range(91))
assert all(dot(row, direction) % 27 == 0
           for row in matrix_integer for direction in T_directions)


def deriv(poly, axis):
    answer = {}
    for (i, j), value in poly.items():
        exponent = i if axis == 0 else j
        if not exponent:
            continue
        xy = (i - 1, j) if axis == 0 else (i, j - 1)
        answer[xy] = answer.get(xy, 0) + exponent * value
    return {xy: value for xy, value in answer.items() if value}


def mul(left, right):
    answer = {}
    for (i, j), a in left.items():
        for (k, ell), b in right.items():
            xy = (i + k, j + ell)
            answer[xy] = answer.get(xy, 0) + a * b
    return {xy: value for xy, value in answer.items() if value}


def jacobian_pair(values):
    left, right = correction(values)
    return nadd(mul(deriv(left, 0), deriv(right, 1)),
                nscale(-1, mul(deriv(left, 1), deriv(right, 0))))


def cross_pair(left_values, right_values):
    lp, lq = correction(left_values)
    rp, rq = correction(right_values)
    return nadd(mul(deriv(lp, 0), deriv(rq, 1)),
                mul(deriv(rp, 0), deriv(lq, 1)),
                nscale(-1, mul(deriv(lp, 1), deriv(rq, 0))),
                nscale(-1, mul(deriv(rp, 1), deriv(lq, 0))))


canonical_slots = [(2, 2)] + [xy for xy in slots if sum(xy) >= 7]
canonical_indices = [slots.index(xy) for xy in canonical_slots]
other_indices = [index for index in range(91)
                 if index not in canonical_indices]
assert len(canonical_indices) == 64 and len(other_indices) == 27
assert all(not any(A3[index]) for index in canonical_indices)
assert rank([A3[index] for index in other_indices]) == 27

# Affine divided-linear carry on the full modulo-729 solution torsor.
carry_constant = []
carry_columns = [[] for _ in range(parameter_count)]
for row in range(91):
    numerator = base_integer[row] + dot(matrix_integer[row], T_base)
    assert numerator % 27 == 0
    carry_constant.append((numerator // 27) % 3)
    for column, direction in enumerate(T_directions):
        numerator = dot(matrix_integer[row], direction)
        assert numerator % 27 == 0
        carry_columns[column].append((numerator // 27) % 3)

# Exact quadratic ANF in the torsor coordinates.  Keep diagonal terms because
# the polynomial is evaluated on F3, not a Boolean cube.
q_constant_poly = jacobian_pair(T_base)
q_constant = [coefficient(q_constant_poly, xy) % 3
              for xy in canonical_slots]
linear = [[carry_columns[column][index] for column in range(parameter_count)]
          for index in canonical_indices]
diagonal = [[0] * parameter_count for _ in canonical_indices]

direction_quadratics = []
for column, direction in enumerate(T_directions):
    qdir = jacobian_pair(direction)
    direction_quadratics.append(qdir)
    mixed = cross_pair(T_base, direction)
    for equation, xy in enumerate(canonical_slots):
        linear[equation][column] = (
            linear[equation][column] + coefficient(mixed, xy)) % 3
        diagonal[equation][column] = coefficient(qdir, xy) % 3

cross_terms = []
for left in range(parameter_count):
    for right in range(left + 1, parameter_count):
        mixed = cross_pair(T_directions[left], T_directions[right])
        values = [coefficient(mixed, xy) % 3 for xy in canonical_slots]
        if any(values):
            cross_terms.append([left, right, values])

constant = [(carry_constant[index] + q_constant[equation]) % 3
            for equation, index in enumerate(canonical_indices)]


def solve_linear_zero_stratum(side):
    equations = []
    rhs = []
    # On either T_P=0 or T_Q=0, det J(T) vanishes identically.
    offset = 0 if side == "P" else 36
    for slot_index in range(36):
        equations.append([direction[offset + slot_index] % 3
                          for direction in T_directions])
        rhs.append((-T_base[offset + slot_index]) % 3)
    for index in canonical_indices:
        equations.append([column[index] for column in carry_columns])
        rhs.append((-carry_constant[index]) % 3)
    stratum_rank, particular, kernel = rref_solve(equations, rhs)
    return stratum_rank, particular, kernel


def evaluate_T(parameters):
    answer = list(T_base)
    for scalar, direction in zip(parameters, T_directions):
        answer = [value + scalar * delta
                  for value, delta in zip(answer, direction)]
    return answer


def next_residual(T):
    qpoly = jacobian_pair(T)
    residual = []
    for row, xy in enumerate(slots):
        numerator = base_integer[row] + dot(matrix_integer[row], T)
        assert numerator % 27 == 0
        residual.append(((numerator // 27) + coefficient(qpoly, xy)) % 3)
    return residual


def replay_witness(parameters, stratum):
    T = evaluate_T(parameters)
    residual = next_residual(T)
    fresh_rank, W, fresh_kernel = rref_solve(
        A3, [(-value) % 3 for value in residual])
    assert W is not None and fresh_rank == 27 and len(fresh_kernel) == 45
    left, right = correction(W)
    P, Q = candidate(T)
    P = nadd(P, nscale(729, left))
    Q = nadd(Q, nscale(729, right))
    determinant = determinant_minus_one(P, Q)
    all_slots = sorted(set(slots) | set(determinant))
    assert all(sum(xy) <= 12 for xy in all_slots)
    assert all(coefficient(determinant, xy) % 2187 == 0
               for xy in all_slots)
    return {
        "stratum": stratum,
        "parameters": parameters,
        "T": [value % 81 for value in T],
        "W": W,
        "fresh_rank": fresh_rank,
        "fresh_kernel_dimension": len(fresh_kernel),
        "literal_integer_replay_mod2187_passed": True,
        "determinant_sha256": hashlib.sha256(
            repr(sorted(determinant.items())).encode()).hexdigest(),
        "P_support": [[i, j, value] for (i, j), value in sorted(P.items())],
        "Q_support": [[i, j, value] for (i, j), value in sorted(Q.items())],
    }


strata = {}
witness = None
for side in ("P", "Q"):
    stratum_rank, particular, kernel = solve_linear_zero_stratum(side)
    strata[side] = {
        "rank": stratum_rank,
        "consistent": particular is not None,
        "kernel_dimension": len(kernel) if particular is not None else None,
    }
    if witness is None and particular is not None:
        witness = replay_witness(particular, side + "_zero")


def bv(value):
    return "#x" + format(value % 16, "x")


def mod3(term):
    return f"(bvurem {term} #x3)"


def add3(terms):
    terms = [term for term in terms if term != "#x0"]
    if not terms:
        return "#x0"
    value = terms[0]
    for term in terms[1:]:
        value = mod3(f"(bvadd {value} {term})")
    return value


def scale3(scalar, term):
    scalar %= 3
    if scalar == 0:
        return "#x0"
    if scalar == 1:
        return term
    return mod3(f"(bvmul #x2 {term})")


smt_path = Path(os.environ["SMT2_OUTPUT"])
with smt_path.open("w") as stream:
    stream.write("(set-logic QF_BV)\n(set-option :produce-models true)\n")
    for index in range(parameter_count):
        stream.write(f"(declare-fun s{index} () (_ BitVec 4))\n")
        stream.write(f"(assert (bvule s{index} #x2))\n")
    for equation in range(64):
        terms = [bv(constant[equation])]
        for column in range(parameter_count):
            if linear[equation][column]:
                terms.append(scale3(linear[equation][column], f"s{column}"))
            if diagonal[equation][column]:
                square = mod3(f"(bvmul s{column} s{column})")
                terms.append(scale3(diagonal[equation][column], square))
        for left, right, values in cross_terms:
            if values[equation]:
                product = mod3(f"(bvmul s{left} s{right})")
                terms.append(scale3(values[equation], product))
        stream.write(f"(assert (= {add3(terms)} #x0))\n")
    stream.write("(check-sat)\n(get-model)\n")

anf_payload = {
    "constant": constant,
    "linear": linear,
    "diagonal": diagonal,
    "cross_terms": cross_terms,
}
anf_bytes = json.dumps(anf_payload, sort_keys=True,
                       separators=(",", ":")).encode() + b"\n"
Path(os.environ["ANF_OUTPUT"]).write_bytes(anf_bytes)

result = {
    "status": ("PASS-AS-Q3-FULL-OUTPUT-CONE-Z81-LINEAR-STRATUM-SAT"
               if witness is not None
               else "PASS-AS-Q3-FULL-OUTPUT-CONE-Z81-COMPILED"),
    "parent_source_sha256": EXPECTED_PARENT,
    "parent_replay_sha256": hashlib.sha256(
        Path(os.environ["PARENT_REPLAY_JSON"]).read_bytes()).hexdigest(),
    "parameter_count": parameter_count,
    "slot_count": len(slots),
    "canonical_cokernel_dimension": len(canonical_indices),
    "fresh_linear_rank": 27,
    "fresh_linear_kernel_dimension": 45,
    "quadratic_cross_pair_count": len(cross_terms),
    "anf_sha256": hashlib.sha256(anf_bytes).hexdigest(),
    "smt2_sha256": hashlib.sha256(smt_path.read_bytes()).hexdigest(),
    "linear_zero_strata": strata,
    "witness": witness,
    "scope": "one complete fixed-D7 modulo729 torsor over one pinned Q3 fibre",
    "refusal_scope": [
        "no claim about the other predecessor scheme",
        "no modulus6561 or deeper/all-depth lift",
        "no characteristic-zero collision, counterexample, or JC2 conclusion",
    ],
}
encoded = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
Path(saved_output).write_bytes(encoded + b"\n")
print("parameters", parameter_count)
print("cross_pairs", len(cross_terms))
print("linear_zero_strata", strata)
print("witness", None if witness is None else witness["stratum"])
print("anf_sha256", result["anf_sha256"])
print("smt2_sha256", result["smt2_sha256"])
print(result["status"])
