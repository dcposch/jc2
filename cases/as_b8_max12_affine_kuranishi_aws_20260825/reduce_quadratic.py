#!/usr/bin/env python3
"""Reduce and emit exact solvers for the B8 W2->W3 quadratic gate (AWS only)."""

from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from functools import lru_cache
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
CASE = ROOT / "cases/as_b8_max12_affine_kuranishi_aws_20260825"
COMPILER = CASE / "compile_affine_kuranishi.py"
EXPECTED_COMPILER = (
    "a3f1b0356198f2acc9a967e2f99967f78ff74828318ef4ff12630cc60c594861")
ANF_PATH = Path(os.environ["INPUT_ANF"])
EXPECTED_ANF = (
    "9121d7cb4ee5aa5f38f31312077c084dc98fbc1b4175c73cef4a95dadaad45a4")
assert hashlib.sha256(COMPILER.read_bytes()).hexdigest() == EXPECTED_COMPILER
assert hashlib.sha256(ANF_PATH.read_bytes()).hexdigest() == EXPECTED_ANF

# Reconstruct the source-side affine basis from the independently pinned
# compiler.  Its own analytic/interpolation equality is rerun fail-closed.
saved_output = os.environ["OUTPUT_JSON"]
saved_anf = os.environ["REDUCED_ANF_OUTPUT"]
os.environ["OUTPUT_JSON"] = os.environ["REPLAY_RESULT"]
os.environ["ANF_OUTPUT"] = os.environ["REPLAY_ANF"]
compiler_bytes = COMPILER.read_bytes()
namespace = {"__file__": str(COMPILER), "__name__": "__b8_reduced_parent__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(compiler_bytes, str(COMPILER), "exec"), namespace)
os.environ["OUTPUT_JSON"] = saved_output
os.environ["REDUCED_ANF_OUTPUT"] = saved_anf


def rref_solve(matrix, rhs):
    if not matrix:
        return 0, [], []
    columns = len(matrix[0])
    work = [[value % 3 for value in row] + [target % 3]
            for row, target in zip(matrix, rhs)]
    pivots = []
    row = 0
    for column in range(columns):
        chosen = next((r for r in range(row, len(work))
                       if work[r][column]), None)
        if chosen is None:
            continue
        work[row], work[chosen] = work[chosen], work[row]
        if work[row][column] == 2:
            work[row] = [(2 * value) % 3 for value in work[row]]
        for r in range(len(work)):
            if r == row or not work[r][column]:
                continue
            scalar = work[r][column]
            work[r] = [(a - scalar * b) % 3
                       for a, b in zip(work[r], work[row])]
        pivots.append(column)
        row += 1
    if any(not any(line[:-1]) and line[-1] for line in work):
        return len(pivots), None, []
    particular = [0] * columns
    for r, column in enumerate(pivots):
        particular[column] = work[r][-1]
    free = [column for column in range(columns) if column not in pivots]
    kernel = []
    for free_column in free:
        vector = [0] * columns
        vector[free_column] = 1
        for r, pivot in enumerate(pivots):
            vector[pivot] = (-work[r][free_column]) % 3
        kernel.append(vector)
    return len(pivots), particular, kernel


def canonical_rows(matrix):
    if not matrix:
        return []
    work = [[value % 3 for value in row] for row in matrix]
    columns = len(work[0])
    row = 0
    for column in range(columns):
        chosen = next((r for r in range(row, len(work))
                       if work[r][column]), None)
        if chosen is None:
            continue
        work[row], work[chosen] = work[chosen], work[row]
        if work[row][column] == 2:
            work[row] = [(2 * value) % 3 for value in work[row]]
        for r in range(len(work)):
            if r != row and work[r][column]:
                scalar = work[r][column]
                work[r] = [(a - scalar * b) % 3
                           for a, b in zip(work[r], work[row])]
        row += 1
    return work[:row]


def rank(matrix):
    return len(canonical_rows(matrix))


anf = json.loads(ANF_PATH.read_text())
equations = [list(row) for row in anf["equations"]]
old_n = len(anf["monomial_order"]["linear"])
old_cross = [tuple(pair) for pair in anf["monomial_order"]["cross_order"]]
assert old_n == 68 and len(equations) == 81
old_q_start = 1 + old_n

# Recover every pure-linear consequence, then parameterize its exact kernel.
q_transpose = [list(column) for column in zip(
    *[row[old_q_start:] for row in equations])]
_, _, combinations = rref_solve(q_transpose, [0] * len(q_transpose))
pure_rows = []
for combination in combinations:
    row = [sum(combination[e] * equations[e][column]
               for e in range(len(equations))) % 3
           for column in range(1 + old_n)]
    if any(row):
        pure_rows.append(row)
pure_basis = canonical_rows(pure_rows)
assert len(pure_basis) == 39
assert all(row[0] == 0 for row in pure_basis)
linear_matrix = [row[1:] for row in pure_basis]
linear_rank, zero_particular, parameter_basis = rref_solve(
    linear_matrix, [0] * len(linear_matrix))
assert linear_rank == 39 and zero_particular == [0] * old_n
new_n = len(parameter_basis)
assert new_n == old_n - linear_rank

# Expressions t_i=sum_a parameter_basis[a][i]*s_a.
expressions = [[(a, parameter_basis[a][i]) for a in range(new_n)
                if parameter_basis[a][i] % 3] for i in range(old_n)]
new_cross = [(a, b) for a in range(new_n) for b in range(a + 1, new_n)]
cross_position = {pair: index for index, pair in enumerate(new_cross)}


def substitute(row):
    constant = row[0] % 3
    linear = [0] * new_n
    diagonal = [0] * new_n
    cross = [0] * len(new_cross)
    for i in range(old_n):
        value = row[1 + i] % 3
        if value:
            for a, ca in expressions[i]:
                linear[a] = (linear[a] + value * ca) % 3
    for i in range(old_n):
        value = row[1 + old_n + i] % 3
        if not value:
            continue
        expr = expressions[i]
        for position, (a, ca) in enumerate(expr):
            diagonal[a] = (diagonal[a] + value * ca * ca) % 3
            for b, cb in expr[position + 1:]:
                cross[cross_position[(a, b)]] = (
                    cross[cross_position[(a, b)]] + 2 * value * ca * cb) % 3
    offset = 1 + 2 * old_n
    for index, (i, j) in enumerate(old_cross):
        value = row[offset + index] % 3
        if not value:
            continue
        for a, ca in expressions[i]:
            for b, cb in expressions[j]:
                if a == b:
                    diagonal[a] = (diagonal[a] + value * ca * cb) % 3
                else:
                    pair = (a, b) if a < b else (b, a)
                    cross[cross_position[pair]] = (
                        cross[cross_position[pair]] + value * ca * cb) % 3
    return [constant] + linear + diagonal + cross


reduced_equations = canonical_rows([substitute(row) for row in equations])
assert all(not row[0] for row in reduced_equations)
reduced_linear_rank = rank([row[1:1+new_n] for row in reduced_equations])
reduced_quadratic_rank = rank([row[1+new_n:] for row in reduced_equations])


def evaluate(row, point):
    value = row[0]
    value += sum(row[1+i] * point[i] for i in range(new_n))
    value += sum(row[1+new_n+i] * point[i] * point[i]
                 for i in range(new_n))
    offset = 1 + 2 * new_n
    value += sum(row[offset+index] * point[a] * point[b]
                 for index, (a, b) in enumerate(new_cross))
    return value % 3


def original_parameters(point):
    return [sum(point[a] * parameter_basis[a][i] for a in range(new_n)) % 3
            for i in range(old_n)]


# Exact coordinate-subspace lower bound: maximize an independent set among
# variables whose individual line is contained in the zero locus.
allowed = []
for a in range(new_n):
    if all(row[1+a] == 0 and row[1+new_n+a] == 0
           for row in reduced_equations):
        allowed.append(a)
adjacency = {a: set() for a in allowed}
for a_index, a in enumerate(allowed):
    for b in allowed[a_index+1:]:
        index = cross_position[(a, b)]
        if any(row[1+2*new_n+index] for row in reduced_equations):
            adjacency[a].add(b)
            adjacency[b].add(a)

@lru_cache(maxsize=None)
def max_independent(vertices):
    vertices = tuple(vertices)
    if not vertices:
        return ()
    v = max(vertices, key=lambda x: len(adjacency[x].intersection(vertices)))
    without = tuple(x for x in vertices if x != v)
    excluded = max_independent(without)
    with_vertices = tuple(x for x in without if x not in adjacency[v])
    included = (v,) + max_independent(with_vertices)
    return included if len(included) > len(excluded) else excluded


coordinate_subspace = sorted(max_independent(tuple(allowed)))
assert all(evaluate(row, [1 if a in coordinate_subspace else 0
                          for a in range(new_n)]) == 0
           for row in reduced_equations)

# Registered finite routing set only: zero, weights one and two over F3.
routing_points = [[0] * new_n]
for a in range(new_n):
    for value in (1, 2):
        point = [0] * new_n
        point[a] = value
        routing_points.append(point)
for a in range(new_n):
    for b in range(a + 1, new_n):
        for av in (1, 2):
            for bv in (1, 2):
                point = [0] * new_n
                point[a], point[b] = av, bv
                routing_points.append(point)
routing_solutions = [point for point in routing_points
                     if all(evaluate(row, point) == 0
                            for row in reduced_equations)]

# Literal source replay for the first ten distinct routing solutions.
T0 = list(namespace["T0"])
kernel = [list(vector) for vector in namespace["kernel"]]
A3 = [list(row) for row in namespace["A3"]]
residual_at = namespace["residual_at"]
rref_parent = namespace["rref_solve"]
combine = namespace["combine"]
correction = namespace["correction"]
add, sc, jac, modp = (namespace["add"], namespace["sc"],
                      namespace["jac"], namespace["modp"])
P0, Q0, ONE = namespace["P0"], namespace["Q0"], namespace["ONE"]
dydeg, tdeg = namespace["namespace"]["dydeg"], namespace["namespace"]["tdeg"]

literal_witnesses = []
for point in routing_solutions[:10]:
    t = original_parameters(point)
    T = combine(T0, kernel, t)
    residual = residual_at(T)
    fresh_rank, W, fresh_kernel = rref_parent(
        A3, [(-value) % 3 for value in residual])
    assert W is not None and fresh_rank == 104 and len(fresh_kernel) == 68
    left_T, right_T = correction(T)
    left_W, right_W = correction(W)
    P = add(P0, sc(3, left_T), sc(9, left_W))
    Q = add(Q0, sc(3, right_T), sc(9, right_W))
    assert modp(jac(P, Q), 27) == ONE
    y_degrees = [dydeg(P), dydeg(Q)]
    total_degrees = [tdeg(P), tdeg(Q)]
    assert y_degrees == [8, 12] and total_degrees == [8, 12]
    literal_witnesses.append({
        "reduced_parameters": point,
        "original_kernel_parameters": t,
        "first_digit": T,
        "fresh_digit": W,
        "actual_y_degrees": y_degrees,
        "actual_total_degrees": total_degrees,
        "all_276_rows_mod27": True,
    })


def singular_term(row, variable_names):
    terms = []
    def append(value, monomial):
        value %= 3
        if not value:
            return
        prefix = "" if value == 1 else "2*"
        terms.append(prefix + monomial)
    if row[0] % 3:
        terms.append(str(row[0] % 3))
    for a, name in enumerate(variable_names):
        append(row[1+a], name)
        append(row[1+new_n+a], name + "^2")
    offset = 1 + 2 * new_n
    for index, (a, b) in enumerate(new_cross):
        append(row[offset+index], variable_names[a] + "*" + variable_names[b])
    return "+".join(terms) if terms else "0"


variables = [f"s{i}" for i in range(new_n)]
ideal_terms = [singular_term(row, variables) for row in reduced_equations]
common_header = (
    "option(redSB);\n"
    f"ring r=3,({','.join(variables)}),dp;\n"
    f"ideal I={','.join(ideal_terms)};\n")
geometry = common_header + "ideal G=std(I);\nprint(\"DIM \"+string(dim(G)));\n" \
    "print(\"SIZE \"+string(size(G)));\nprint(\"VDIM \"+string(vdim(G)));\n" \
    "print(\"REDUCE_ORIGINAL \"+string(reduce(I,G)));\nquit;\n"
finite = common_header + f"ideal F=I,{','.join(name+'^3-'+name for name in variables)};\n" \
    "ideal G=std(F);\nprint(\"DIM \"+string(dim(G)));\n" \
    "print(\"SIZE \"+string(size(G)));\nprint(\"VDIM \"+string(vdim(G)));\n" \
    "print(\"REDUCE_ORIGINAL \"+string(reduce(F,G)));\nquit;\n"
Path(os.environ["GEOMETRY_SING"]).write_text(geometry)
Path(os.environ["FINITE_SING"]).write_text(finite)

reduced_anf = {
    "source_anf_sha256": EXPECTED_ANF,
    "old_parameter_count": old_n,
    "pure_linear_basis": pure_basis,
    "parameter_basis": parameter_basis,
    "new_parameter_count": new_n,
    "cross_order": new_cross,
    "equations": reduced_equations,
}
reduced_bytes = json.dumps(
    reduced_anf, sort_keys=True, separators=(",", ":")).encode() + b"\n"
Path(saved_anf).write_bytes(reduced_bytes)

result = {
    "status": "PASS-AS-B8-D12-QUADRATIC-REDUCTION-EMITTED",
    "source_anf_sha256": EXPECTED_ANF,
    "pure_linear_rank": linear_rank,
    "reduced_parameter_count": new_n,
    "reduced_equation_count": len(reduced_equations),
    "reduced_linear_tangent_rank": reduced_linear_rank,
    "reduced_quadratic_coefficient_rank": reduced_quadratic_rank,
    "coordinate_linear_subspace": coordinate_subspace,
    "coordinate_linear_subspace_dimension": len(coordinate_subspace),
    "registered_routing_point_count": len(routing_points),
    "registered_routing_solution_count": len(routing_solutions),
    "literal_witnesses": literal_witnesses,
    "fresh_affine_fibre_dimension": 68,
    "reduced_anf_sha256": hashlib.sha256(reduced_bytes).hexdigest(),
    "geometry_sing_sha256": hashlib.sha256(geometry.encode()).hexdigest(),
    "finite_sing_sha256": hashlib.sha256(finite.encode()).hexdigest(),
    "scope": "complete reduction/emission; Singular endpoints still required",
    "refusal_scope": [
        "weight<=2 routing is not full solution classification",
        "no deeper/all-depth, Z3, characteristic-zero, CE, max12, or JC2 claim",
    ],
}
encoded = json.dumps(result, sort_keys=True, separators=(",", ":")).encode() + b"\n"
Path(saved_output).write_bytes(encoded)
print("pure_linear_reduced_variables", linear_rank, new_n)
print("reduced_equations_linear_quadratic_rank", len(reduced_equations),
      reduced_linear_rank, reduced_quadratic_rank)
print("coordinate_subspace_dimension", len(coordinate_subspace))
print("routing_points_solutions", len(routing_points), len(routing_solutions))
print("literal_witnesses", len(literal_witnesses))
print("reduced_anf_sha256", result["reduced_anf_sha256"])
print("geometry_sing_sha256", result["geometry_sing_sha256"])
print("finite_sing_sha256", result["finite_sing_sha256"])
print("result_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])

