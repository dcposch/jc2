#!/usr/bin/env python3
"""Emit exact QF_BV circuits for the 176-coordinate predecessor map."""

from __future__ import annotations

import contextlib
import gzip
import hashlib
import io
import json
import os
import platform
from pathlib import Path


assert platform.system() == "Linux", "AWS-only emitter refuses non-Linux"
job_tag = os.environ.get("AWS_JOB_TAG", "")
assert job_tag.startswith("as_b9_common_cubic_kuranishi_map_"), job_tag
row_start = int(os.environ["ROW_START"])
row_end = int(os.environ["ROW_END"])
assert 0 <= row_start < row_end <= 176

parent_path = Path(os.environ["GLOBAL_V1_SOURCE"])
parent_bytes = parent_path.read_bytes()
expected_parent = "b16912cd1b6146a35736e9bb872d96bfa640e1bb920e04b7c5a9e13256d12a3f"
assert hashlib.sha256(parent_bytes).hexdigest() == expected_parent
block_path = Path(os.environ["FRESH_BLOCK_GZIP"])
expected_block = "f7f473c5781f610dd0f96112981e8f3b3c7757467d42b7c465a3dfde5c80e8af"
assert hashlib.sha256(block_path.read_bytes()).hexdigest() == expected_block

saved_output = os.environ["OUTPUT_JSON"]
saved_witness = os.environ["WITNESS_OUTPUT"]
saved_job_tag = os.environ["AWS_JOB_TAG"]
os.environ["OUTPUT_JSON"] = os.environ["GLOBAL_V1_RESULT"]
os.environ["WITNESS_OUTPUT"] = os.environ["GLOBAL_V1_WITNESS"]
os.environ["AWS_JOB_TAG"] = "as_b9_common_cubic_global_row22_kuranishi"
outer = {"__file__": str(parent_path), "__name__": "__kuranishi_parent__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(parent_bytes, str(parent_path), "exec"), outer)
os.environ["OUTPUT_JSON"] = saved_output
os.environ["WITNESS_OUTPUT"] = saved_witness
os.environ["AWS_JOB_TAG"] = saved_job_tag

inner = outer["scope"]
base_values = list(outer["base_values"])
directions = [list(vector) for vector in outer["directions"]]
raw_constant = list(outer["raw_constant"])
raw_linear = [list(vector) for vector in outer["raw_linear"]]
raw_diagonal = [list(vector) for vector in outer["raw_diagonal"]]
raw_cross = [list(vector) for vector in outer["raw_cross"]]
cross_indices = [tuple(pair) for pair in outer["cross_indices"]]
inactive_matrix = [list(row) for row in outer["inactive_matrix"]]
fresh_matrix = [list(row) for row in outer["fresh_matrix"]]
assert (len(directions), len(raw_constant)) == (133, 205)
assert (len(inactive_matrix), len(inactive_matrix[0])) == (205, 116)
assert (len(fresh_matrix), len(fresh_matrix[0])) == (299, 149)

block = json.load(gzip.open(block_path, "rt"))
next_left = block["next_left_cokernel"]
fresh_left = block["fresh_left_quotient"]
assert (len(next_left), len(fresh_left)) == (205, 176)
combined = [[sum(fresh_left[row][k] * next_left[k][column]
                 for k in range(205)) % 3
             for column in range(299)]
            for row in range(176)]
combined_support_histogram = {}
for row in combined:
    key = str(sum(bool(value) for value in row))
    combined_support_histogram[key] = combined_support_histogram.get(key, 0) + 1
assert combined_support_histogram == {
    "1": 154, "2": 12, "3": 5, "4": 2, "5": 2, "6": 1}


def rref_transform(matrix):
    """Match the parent fixed solver and retain its row transform."""
    rows = len(matrix)
    columns = len(matrix[0])
    work = [[value % 3 for value in row]
            + [1 if i == j else 0 for j in range(rows)]
            for i, row in enumerate(matrix)]
    pivots = []
    pivot_row = 0
    for column in range(columns):
        chosen = next((row for row in range(pivot_row, rows)
                       if work[row][column]), None)
        if chosen is None:
            continue
        work[pivot_row], work[chosen] = work[chosen], work[pivot_row]
        inverse = 1 if work[pivot_row][column] == 1 else 2
        work[pivot_row] = [(inverse * value) % 3
                           for value in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row or not work[row][column]:
                continue
            scalar = work[row][column]
            work[row] = [(a - scalar * b) % 3
                         for a, b in zip(work[row], work[pivot_row])]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == rows:
            break
    transform = [row[columns:] for row in work]
    free = [column for column in range(columns) if column not in pivots]
    kernel = []
    for free_column in free:
        vector = [0] * columns
        vector[free_column] = 1
        for row, pivot in enumerate(pivots):
            vector[pivot] = (-work[row][free_column]) % 3
        kernel.append(vector)
    return pivots, transform, kernel


inactive_pivots, inactive_transform, spectator_kernel = rref_transform(
    inactive_matrix)
fresh_pivots, fresh_transform, family_fresh_kernel = rref_transform(
    fresh_matrix)
assert (len(inactive_pivots), len(spectator_kernel)) == (38, 78)
assert (len(fresh_pivots), len(family_fresh_kernel)) == (94, 55)
assert spectator_kernel == outer["spectator_kernel"]
assert family_fresh_kernel == outer["fresh_kernel"]


class Ref:
    __slots__ = ("name", "digest", "sort")

    def __init__(self, name, digest, sort):
        self.name = name
        self.digest = digest
        self.sort = sort


class Dag:
    def __init__(self):
        self.definitions = []
        self.cache = {}
        self.inputs = []

    @staticmethod
    def digest(payload):
        return hashlib.sha256(payload.encode()).hexdigest()

    def input(self, name, sort):
        ref = Ref(name, self.digest(f"input|{sort}|{name}"), sort)
        self.inputs.append(ref)
        return ref

    def node(self, sort, op, args, body):
        digest = self.digest("|".join(
            [sort, op] + [arg.digest for arg in args] + [body]))
        key = (sort, digest)
        if key in self.cache:
            return self.cache[key]
        name = f"n{len(self.definitions)}"
        ref = Ref(name, digest, sort)
        self.definitions.append((ref, body))
        self.cache[key] = ref
        return ref


dag = Dag()


def c3(value):
    value %= 3
    return dag.node("(_ BitVec 2)", "c3", [], f"(_ bv{value} 2)")


def cm(value):
    value %= 531441
    return dag.node("(_ BitVec 20)", "cm", [], f"(_ bv{value} 20)")


zero3, one3, two3 = c3(0), c3(1), c3(2)
zerom = cm(0)


def fadd(left, right):
    return dag.node("(_ BitVec 2)", "fadd", [left, right],
                    f"(fadd {left.name} {right.name})")


def fmul(left, right):
    return dag.node("(_ BitVec 2)", "fmul", [left, right],
                    f"(fmul {left.name} {right.name})")


def fneg(value):
    return fmul(two3, value)


def fsum(terms):
    answer = zero3
    for value in terms:
        answer = fadd(answer, value)
    return answer


def fscale(scalar, value):
    return fmul(c3(scalar), value)


def madd(left, right):
    return dag.node("(_ BitVec 20)", "madd", [left, right],
                    f"(madd {left.name} {right.name})")


def mmul(left, right):
    return dag.node("(_ BitVec 20)", "mmul", [left, right],
                    f"(mmul {left.name} {right.name})")


def mneg(value):
    return dag.node("(_ BitVec 20)", "mneg", [value],
                    f"(mneg {value.name})")


def msub(left, right):
    return madd(left, mneg(right))


def msum(terms):
    answer = zerom
    for value in terms:
        answer = madd(answer, value)
    return answer


def mscale(scalar, value):
    return mmul(cm(scalar), value)


def embed(value):
    return dag.node("(_ BitVec 20)", "embed", [value],
                    f"((_ zero_extend 18) {value.name})")


def divided_digit(value, divisor):
    body = (f"((_ extract 1 0) (bvurem (bvudiv {value.name} "
            f"(_ bv{divisor} 20)) (_ bv3 20)))")
    return dag.node("(_ BitVec 2)", f"digit{divisor}", [value], body)


def symbolic_solve(pivots, transform, rhs, kernel, free_parameters):
    particular = [zero3] * (len(pivots) + len(kernel))
    for row, pivot in enumerate(pivots):
        particular[pivot] = fsum(
            fscale(value, rhs[index])
            for index, value in enumerate(transform[row]) if value)
    answer = list(particular)
    for scalar, vector in zip(free_parameters, kernel):
        for index, value in enumerate(vector):
            if value:
                answer[index] = fadd(answer[index], fscale(value, scalar))
    return answer


active = [dag.input(f"a_{index}", "(_ BitVec 2)")
          for index in range(17)]
spectator = [dag.input(f"s_{index}", "(_ BitVec 2)")
             for index in range(78)]
all_inputs = active + spectator

raw = []
for row in range(205):
    terms = [c3(raw_constant[row])]
    for index, value in enumerate(raw_linear[:17]):
        if value[row]:
            terms.append(fscale(value[row], active[index]))
    for index, value in enumerate(raw_diagonal):
        if value[row]:
            terms.append(fscale(value[row], fmul(active[index], active[index])))
    for vector, (left, right) in zip(raw_cross, cross_indices):
        if vector[row]:
            terms.append(fscale(vector[row], fmul(active[left], active[right])))
    raw.append(fsum(terms))

inactive = symbolic_solve(
    inactive_pivots, inactive_transform, [fneg(value) for value in raw],
    spectator_kernel, spectator)
assert len(inactive) == 116
family_coordinates = active + inactive

predecessor = []
for coordinate in range(149):
    terms = [cm(base_values[coordinate])]
    for scalar, direction in zip(family_coordinates, directions):
        if direction[coordinate]:
            terms.append(mscale(direction[coordinate], embed(scalar)))
    predecessor.append(msum(terms))

p5 = dict(inner["p5"])
q5 = dict(inner["q5"])
slots = list(inner["slots"])
support_p = [(i, degree - i) for degree in range(10)
             for i in range(degree + 1)]
support_q = [(i, degree - i) for degree in range(13)
             for i in range(degree + 1)]
assert (len(support_p), len(support_q), len(slots)) == (55, 91, 276)


def convolution(left, right):
    answer = [zerom] * (len(left) + len(right) - 1)
    for i, first in enumerate(left):
        for j, second in enumerate(right):
            answer[i + j] = madd(answer[i + j], mmul(first, second))
    return answer


def residual_circuit(values):
    p = {xy: cm(p5.get(xy, 0)) for xy in set(p5) | set(support_p)}
    q = {xy: cm(q5.get(xy, 0)) for xy in set(q5) | set(support_q)}
    for index, xy in enumerate(support_p):
        p[xy] = madd(p.get(xy, zerom), mscale(243, values[index]))
    for index, xy in enumerate(support_q):
        q[xy] = madd(q.get(xy, zerom), mscale(243, values[55 + index]))
    determinant = {xy: zerom for xy in slots}
    for (i, j), pvalue in p.items():
        for (k, ell), qvalue in q.items():
            factor = i * ell - j * k
            if not factor:
                continue
            xy = (i + k - 1, j + ell - 1)
            if xy in determinant:
                determinant[xy] = madd(
                    determinant[xy], mscale(factor, mmul(pvalue, qvalue)))
    determinant[(0, 0)] = msub(determinant[(0, 0)], cm(1))
    h = [cm(1), madd(cm(81), mscale(243, values[146])),
         mscale(243, values[147]), mscale(243, values[148])]
    h2 = convolution(h, h)
    h3 = convolution(h2, h)
    h4 = convolution(h3, h)
    ptop = [p[(i, 9 - i)] for i in range(10)]
    qtop = [q[(i, 12 - i)] for i in range(13)]
    rows = [determinant[xy] for xy in slots]
    rows.extend(msub(value, mmul(ptop[0], power))
                for value, power in zip(ptop, h3))
    rows.extend(msub(value, mmul(qtop[0], power))
                for value, power in zip(qtop, h4))
    assert len(rows) == 299
    return rows


predecessor_rows = residual_circuit(predecessor)
fresh_rhs = [fneg(divided_digit(value, 3 ** 10))
             for value in predecessor_rows]
fresh_particular = symbolic_solve(
    fresh_pivots, fresh_transform, fresh_rhs, family_fresh_kernel, [])
assert len(fresh_particular) == 149
final_values = [madd(value, mscale(3 ** 5, embed(digit)))
                for value, digit in zip(predecessor, fresh_particular)]
final_rows = residual_circuit(final_values)
next_rhs = [fneg(divided_digit(value, 3 ** 11)) for value in final_rows]
kappa = [fsum(fscale(value, next_rhs[column])
              for column, value in enumerate(combined[row]) if value)
         for row in range(176)]

# Independent structural hashes use the recursive DAG, not node numbering.
coordinate_hashes = [value.digest for value in kappa]

header = [
    "; exact B9 common-cubic predecessor Kuranishi map",
    "(set-logic QF_BV)",
    "(define-fun fadd ((a (_ BitVec 2)) (b (_ BitVec 2))) (_ BitVec 2) ((_ extract 1 0) (bvurem (bvadd ((_ zero_extend 2) a) ((_ zero_extend 2) b)) (_ bv3 4))))",
    "(define-fun fmul ((a (_ BitVec 2)) (b (_ BitVec 2))) (_ BitVec 2) ((_ extract 1 0) (bvurem (bvmul ((_ zero_extend 2) a) ((_ zero_extend 2) b)) (_ bv3 4))))",
    "(define-fun madd ((a (_ BitVec 20)) (b (_ BitVec 20))) (_ BitVec 20) ((_ extract 19 0) (bvurem (bvadd ((_ zero_extend 20) a) ((_ zero_extend 20) b)) (_ bv531441 40))))",
    "(define-fun mmul ((a (_ BitVec 20)) (b (_ BitVec 20))) (_ BitVec 20) ((_ extract 19 0) (bvurem (bvmul ((_ zero_extend 20) a) ((_ zero_extend 20) b)) (_ bv531441 40))))",
    "(define-fun mneg ((a (_ BitVec 20))) (_ BitVec 20) (ite (= a (_ bv0 20)) (_ bv0 20) (bvsub (_ bv531441 20) a)))",
]
for value in all_inputs:
    header.append(f"(declare-fun {value.name} () {value.sort})")
    header.append(f"(assert (bvult {value.name} (_ bv3 2)))")
definitions = [f"(define-fun {ref.name} () {ref.sort} {body})"
               for ref, body in dag.definitions]
assertions = []

# Exact chronological divisibility and source-row reconstruction controls.
for row in predecessor_rows:
    assertions.append(
        f"(assert (= (bvurem {row.name} (_ bv59049 20)) (_ bv0 20)))")
for row in range(205):
    lhs = fsum([raw[row]] + [
        fscale(inactive_matrix[row][column], inactive[column])
        for column in range(116) if inactive_matrix[row][column]])
    assertions.append(f"(assert (= {lhs.name} (_ bv0 2)))")
for row in range(299):
    lhs = fsum([fresh_rhs[row]] + [
        fscale(fresh_matrix[row][column], fresh_particular[column])
        for column in range(149) if fresh_matrix[row][column]])
    assertions.append(f"(assert (= {lhs.name} (_ bv0 2)))")
for row in final_rows:
    assertions.append(
        f"(assert (= (bvurem {row.name} (_ bv177147 20)) (_ bv0 20)))")
for row in range(row_start, row_end):
    assertions.append(f"(assert (= {kappa[row].name} (_ bv0 2)))")
assertions.extend(["(check-sat)", "(get-model)"])

# Some source-row identities above added new DAG nodes after the first render.
definitions = [f"(define-fun {ref.name} () {ref.sort} {body})"
               for ref, body in dag.definitions]
formula = "\n".join(header + definitions + assertions) + "\n"
formula_bytes = formula.encode()
Path(os.environ["SMT_OUTPUT"]).write_bytes(formula_bytes)

result = {
    "status": "PASS-AS-B9-COMMON-CUBIC-KURANISHI-MAP-EMIT",
    "aws_job_tag": job_tag,
    "row_start": row_start,
    "row_end": row_end,
    "global_v1_source_sha256": expected_parent,
    "fresh_block_gzip_sha256": expected_block,
    "family_dimensions": [17, 78, 95],
    "fresh_block_shape_rank_kernel_quotient": [205, 55, 29, 26, 176],
    "combined_functional_support_histogram": combined_support_histogram,
    "coordinate_hashes": coordinate_hashes[row_start:row_end],
    "all_coordinate_hashes_sha256": hashlib.sha256(json.dumps(
        coordinate_hashes, separators=(",", ":")).encode()).hexdigest(),
    "dag_node_count": len(dag.definitions),
    "smt_size": len(formula_bytes),
    "smt_sha256": hashlib.sha256(formula_bytes).hexdigest(),
    "arithmetic_modulus": 3 ** 12,
    "chronological_divisors": [3 ** 10, 3 ** 11],
    "degree_firewall": (
        "exact modular DAG; no ordinary F3 ANF degree inferred through carry gates"),
    "scope": "selected coordinate block on the complete predecessor95 chart",
    "refusal_scope": [
        "a proper row block is not the full zero locus",
        "no SAT witness is accepted without original-integer reconstruction",
        "no all-depth, counterexample, maximum12, or JC2 claim",
    ],
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(saved_output).write_bytes(encoded)
print("rows", row_start, row_end)
print("dag_nodes_smt_size", len(dag.definitions), len(formula_bytes))
print("all_coordinate_hashes_sha256", result["all_coordinate_hashes_sha256"])
print("smt_sha256", result["smt_sha256"])
print("result_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])
