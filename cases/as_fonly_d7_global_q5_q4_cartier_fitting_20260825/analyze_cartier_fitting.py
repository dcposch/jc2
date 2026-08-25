#!/usr/bin/env python3
"""Exact affine/cokernel stratifier for the complete Q5/Q4 formula."""
from __future__ import annotations

import collections
import hashlib
import itertools
import json
import os
from pathlib import Path
import runpy

import z3


ROOT = Path(os.environ["JC2_ROOT"])
PARENT = (ROOT / "cases/as_fonly_d7_global_q5_q4_cartier_20260825"
          / "solve_global_q5_q4_cartier.py")
BASES = (ROOT / "cases/as_fonly_d7_global_q5_q4_cartier_20260825"
         / "compatible_bases.tsv")
EXPECTED_PARENT_SHA = (
    "161287467d04d9ba769a09844405d7fcc7f0d90b53099217e836fd4e9febcdaf")
EXPECTED_BASES_SHA = (
    "bc9d6c9ed4f9103fe0a30bccddf1f73bfaaa5be87f6f060eb26b43f7cb0e7b52")
assert hashlib.sha256(PARENT.read_bytes()).hexdigest() == EXPECTED_PARENT_SHA
assert hashlib.sha256(BASES.read_bytes()).hexdigest() == EXPECTED_BASES_SHA

OUT = Path(os.environ["OUTPUT_DIR"])
OUT.mkdir(parents=True, exist_ok=False)
os.environ["SMT2_OUTPUT"] = str(OUT / "parent_formula.smt2")
os.environ["OUTPUT_JSON"] = str(OUT / "parent_emitter.json")
os.environ["SOLVER_TIMEOUT_MS"] = "1"
os.environ.pop("PIN_PREDECESSOR", None)
os.environ.pop("PIN_STRUCTURAL", None)
os.environ.pop("OMIT_Q4_CARTIER", None)
os.environ.pop("OMIT_Q5_GATE", None)

outer = runpy.run_path(str(PARENT), run_name="__cartier_fitting_parent__")
scope = outer["scope"]
scope_depth = 0
while "solver" not in scope:
    assert "scope" in scope, sorted(scope)
    scope = scope["scope"]
    scope_depth += 1
solver = scope["solver"]
pred_vars = scope["pred_vars"]
xvars, yvars, rvars = scope["xvars"], scope["yvars"], scope["rvars"]
hvars, kvars = scope["hvars"], scope["kvars"]
all_input_vars = scope["all_input_vars"]
assert (len(pred_vars), len(xvars), len(yvars), len(rvars),
        len(hvars), len(kvars)) == (30, 32, 32, 18, 16, 14)
assert scope["q4_cartier_omitted"] is False

WIDTH = 32
MASK = 2 ** WIDTH - 1
THREE = z3.BitVecVal(3, WIDTH)
ZERO = z3.BitVecVal(0, WIDTH)
ONE = z3.BitVecVal(1, WIDTH)
restoration = list(hvars) + list(kvars)
restoration_names = {variable.decl().name() for variable in restoration}


def variables(expression):
    """Return uninterpreted-constant names in a Z3 DAG."""
    answer = set()
    stack = [expression]
    seen = set()
    while stack:
        node = stack.pop()
        key = node.get_id()
        if key in seen:
            continue
        seen.add(key)
        if (z3.is_const(node)
                and node.decl().kind() == z3.Z3_OP_UNINTERPRETED):
            answer.add(node.decl().name())
        else:
            stack.extend(node.children())
    return answer


def is_zero(node):
    return z3.is_bv_value(node) and node.as_long() == 0


def mod_three_side(assertion):
    assert z3.is_eq(assertion), assertion
    left, right = assertion.children()
    if is_zero(right):
        candidate = left
    elif is_zero(left):
        candidate = right
    else:
        raise AssertionError((left, right))
    assert candidate.decl().kind() == z3.Z3_OP_BUREM, candidate
    numerator, modulus = candidate.children()
    assert z3.is_bv_value(modulus) and modulus.as_long() == 3
    return candidate


def sub_all(expression, assignments):
    return z3.simplify(z3.substitute(
        expression, *((variable, value) for variable, value in assignments)))


assertions = list(solver.assertions())
independent_assertions = []
restoration_bounds = []
row_assertions = []
for assertion in assertions:
    charged = variables(assertion) & restoration_names
    if not charged:
        independent_assertions.append(assertion)
    elif assertion.decl().kind() == z3.Z3_OP_ULEQ:
        assert len(charged) == 1
        restoration_bounds.append(assertion)
    else:
        mod_three_side(assertion)
        row_assertions.append(assertion)

assert len(restoration_bounds) == 30, len(restoration_bounds)
assert len(row_assertions) == 76, len(row_assertions)

zero_sub = [(variable, ZERO) for variable in restoration]
matrix = []
right_column = []
reconstructions = []
for assertion in row_assertions:
    value = mod_three_side(assertion)
    base = sub_all(value, zero_sub)
    right_column.append(base)
    row = []
    for variable in restoration:
        substitutions = [(other, ONE if z3.eq(other, variable) else ZERO)
                         for other in restoration]
        at_one = sub_all(value, substitutions)
        coefficient = z3.simplify(z3.URem(at_one + THREE - base, THREE))
        assert not (variables(coefficient) & restoration_names)
        row.append(coefficient)
    matrix.append(row)
    reconstructed = base
    for coefficient, variable in zip(row, restoration):
        reconstructed = z3.URem(
            reconstructed + z3.URem(coefficient * variable, THREE), THREE)
    reconstructions.append(z3.simplify(reconstructed))

# One whole-cube symbolic check: every charged row equals its affine rebuild.
affine_check = z3.Solver()
affine_check.set(timeout=int(os.environ.get("AFFINE_TIMEOUT_MS", "3600000")))
for variable in all_input_vars:
    affine_check.add(z3.ULE(variable, z3.BitVecVal(2, WIDTH)))
affine_check.add(z3.Or(*[
    mod_three_side(assertion) != reconstructed
    for assertion, reconstructed in zip(row_assertions, reconstructions)]))
affine_status = affine_check.check()
assert affine_status == z3.unsat, (affine_status, affine_check.reason_unknown())

structural_names = tuple(scope["structural"])
frob_names = tuple(scope["frob"])
assert structural_names == ("Pp", "Qq", "Rr", "Tt", "s", "w", "h")
assert len(frob_names) == 6
matrix_control_names = structural_names + frob_names
matrix_control_z3_names = {f"pred_{name}" for name in matrix_control_names}
matrix_dependencies = set()
for row in matrix:
    for entry in row:
        matrix_dependencies.update(variables(entry))
assert matrix_dependencies <= matrix_control_z3_names, sorted(
    matrix_dependencies - matrix_control_z3_names)

q4 = scope["q4_cartier_coefficient"]
q4_assertion = assertions[-1]
expected_q4_assertion = z3.URem(q4, THREE) == ZERO
assert z3.eq(q4_assertion, expected_q4_assertion), (
    q4_assertion, expected_q4_assertion)
q4_dependencies = sorted(variables(q4))
assert not (set(q4_dependencies) & restoration_names)


def parse_bases():
    answer = []
    for line in BASES.read_text().splitlines():
        fields = line.split()
        assert len(fields) == 5 and fields[0] == "Q9_COMPATIBLE_BASE"
        digits = tuple(int(char) for char in fields[2])
        assert len(digits) == 7 and all(value in (0, 1, 2) for value in digits)
        answer.append((int(fields[1]), digits, int(fields[3]), int(fields[4])))
    assert len(answer) == 79
    return answer


def compile_bv(expression, variable_order):
    """Compile the small coefficient-expression DAG to exact uint32 ops."""
    index = {name: position for position, name in enumerate(variable_order)}
    cache = {}

    def build(node):
        key = node.get_id()
        if key in cache:
            return cache[key]
        if z3.is_bv_value(node):
            code = ("const", node.as_long())
        elif (z3.is_const(node)
              and node.decl().kind() == z3.Z3_OP_UNINTERPRETED):
            code = ("var", index[node.decl().name()])
        else:
            kind = node.decl().kind()
            children = tuple(build(child) for child in node.children())
            supported = {
                z3.Z3_OP_BADD: "add", z3.Z3_OP_BSUB: "sub",
                z3.Z3_OP_BMUL: "mul", z3.Z3_OP_BUREM: "urem",
                z3.Z3_OP_BUDIV: "udiv", z3.Z3_OP_BNEG: "neg",
            }
            assert kind in supported, (kind, node)
            code = (supported[kind],) + children
        cache[key] = code
        return code

    return build(expression)


def eval_code(code, values):
    op = code[0]
    if op == "const":
        return code[1]
    if op == "var":
        return values[code[1]]
    args = [eval_code(child, values) for child in code[1:]]
    if op == "add":
        return sum(args) & MASK
    if op == "sub":
        assert len(args) == 2
        return (args[0] - args[1]) & MASK
    if op == "mul":
        product = 1
        for value in args:
            product = (product * value) & MASK
        return product
    if op == "urem":
        assert len(args) == 2 and args[1] != 0
        return args[0] % args[1]
    if op == "udiv":
        assert len(args) == 2 and args[1] != 0
        return args[0] // args[1]
    if op == "neg":
        assert len(args) == 1
        return (-args[0]) & MASK
    raise AssertionError(op)


control_var_order = tuple(f"pred_{name}" for name in matrix_control_names)
unique_entries = {}
entry_index_matrix = []
for row in matrix:
    indices = []
    for entry in row:
        key = entry.sexpr()
        if key not in unique_entries:
            unique_entries[key] = len(unique_entries)
        indices.append(unique_entries[key])
    entry_index_matrix.append(indices)
entry_codes = [None] * len(unique_entries)
for sexpr, index in unique_entries.items():
    # Recover the already-built AST without reparsing.
    found = next(entry for row in matrix for entry in row
                 if entry.sexpr() == sexpr)
    entry_codes[index] = compile_bv(found, control_var_order)


def rank_mod3(flat, rows=76, columns=30):
    work = [list(flat[row * columns:(row + 1) * columns])
            for row in range(rows)]
    rank = 0
    for column in range(columns):
        pivot = next((row for row in range(rank, rows)
                      if work[row][column] % 3), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = 1 if work[rank][column] % 3 == 1 else 2
        work[rank] = [(inverse * value) % 3 for value in work[rank]]
        for row in range(rows):
            if row != rank and work[row][column] % 3:
                scalar = work[row][column] % 3
                work[row] = [(left - scalar * right) % 3
                             for left, right in zip(work[row], work[rank])]
        rank += 1
        if rank == rows:
            break
    return rank


bases = parse_bases()
matrix_classes = collections.defaultdict(lambda: {
    "count": 0, "first_state": None, "base_indices": set()})
state_count = 0
for base_index, structural_digits, compatible, completions in bases:
    del compatible, completions
    for frob_digits in itertools.product(range(3), repeat=len(frob_names)):
        values = structural_digits + frob_digits
        entry_values = tuple(eval_code(code, values) % 3
                             for code in entry_codes)
        flat = bytes(entry_values[index]
                     for row in entry_index_matrix for index in row)
        digest = hashlib.sha256(flat).hexdigest()
        record = matrix_classes[(digest, flat)]
        record["count"] += 1
        record["base_indices"].add(base_index)
        if record["first_state"] is None:
            record["first_state"] = [base_index, "".join(map(str, frob_digits))]
        state_count += 1
assert state_count == 79 * 3 ** 6

rank_histogram = collections.Counter()
class_records = []
for (digest, flat), record in matrix_classes.items():
    rank = rank_mod3(flat)
    rank_histogram[rank] += record["count"]
    class_records.append({
        "matrix_sha256": digest,
        "rank": rank,
        "left_cokernel_dimension": 76 - rank,
        "state_count": record["count"],
        "structural_base_count": len(record["base_indices"]),
        "first_state": record["first_state"],
    })
class_records.sort(key=lambda item: (item["rank"], item["matrix_sha256"]))

matrix_expression_payload = "\n".join(
    ",".join(entry.sexpr() for entry in row) for row in matrix).encode()
right_expression_payload = "\n".join(
    entry.sexpr() for entry in right_column).encode()
q4_payload = q4.sexpr().encode()
result = {
    "status": "PASS-AS-Q5-Q4-CARTIER-FITTING-STRATIFIER",
    "parent_sha256": EXPECTED_PARENT_SHA,
    "bases_sha256": EXPECTED_BASES_SHA,
    "assertion_count": len(assertions),
    "nested_scope_depth": scope_depth,
    "restoration_bound_count": len(restoration_bounds),
    "restoration_row_count": len(row_assertions),
    "restoration_variable_count": len(restoration),
    "independent_assertion_count": len(independent_assertions),
    "affine_whole_cube_check": str(affine_status),
    "matrix_shape": [76, 30],
    "matrix_expression_sha256": hashlib.sha256(
        matrix_expression_payload).hexdigest(),
    "right_column_expression_sha256": hashlib.sha256(
        right_expression_payload).hexdigest(),
    "matrix_dependencies": sorted(matrix_dependencies),
    "matrix_control_names": list(control_var_order),
    "unique_matrix_entry_expression_count": len(unique_entries),
    "compatible_structural_base_count": len(bases),
    "exhausted_matrix_state_count": state_count,
    "matrix_class_count": len(class_records),
    "rank_histogram_by_state": {str(rank): count
                                for rank, count in sorted(rank_histogram.items())},
    "classes": class_records,
    "q4_expression_sha256": hashlib.sha256(q4_payload).hexdigest(),
    "q4_dependencies": q4_dependencies,
    "q4_independent_of_q6_q5_restoration": True,
    "q4_assertion_is_last_parent_assertion": True,
    "scope": ("exact affine restoration matrix and its coefficient-matrix "
              "rank strata; no Cartier zero-locus emptiness inference"),
}
(OUT / "matrix_expressions.txt").write_bytes(matrix_expression_payload)
(OUT / "right_column_expressions.txt").write_bytes(right_expression_payload)
(OUT / "q4_expression.smt2expr").write_bytes(q4_payload + b"\n")
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
(OUT / "result.json").write_bytes(encoded)
print("restoration_rows", len(row_assertions), "variables", len(restoration))
print("affine_whole_cube_check", affine_status)
print("matrix_dependencies", sorted(matrix_dependencies))
print("unique_matrix_entry_expressions", len(unique_entries))
print("matrix_states", state_count, "classes", len(class_records))
print("rank_histogram", sorted(rank_histogram.items()))
print("q4_dependencies", q4_dependencies)
print("result_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-AS-Q5-Q4-CARTIER-FITTING-STRATIFIER")
