#!/usr/bin/env python3
"""AWS-only polynomial navigation for the first post-sheet raw grade."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform
import random
import sys


HERE = Path(__file__).resolve().parent
COMPILER = HERE / "compile_receivers.py"
FREEZE = HERE / "FREEZE.sha256"
RESULT = HERE / "RESULT.md"
EXPECTED = {
    COMPILER: "2d8507bcdab953f94a19bc6f794fe8233f466c74afcbab4f21497aab4280951a",
    FREEZE: "50ca8894f273ff47f69b6b32f410b811cb22e144b4a3602da326dd0e68ecc0d0",
    RESULT: "c4123a3eb37f8341f3ac363c5d9d6a0e97009a714f1bfefe818f50be9d82067c",
}
NEWEST = ("ell3", "cs2", "rs2", "az2", "ac2", "ez3", "ec3", "k10_2")
ZERO_EXPONENT = (0,) * len(NEWEST)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_compiler():
    spec = importlib.util.spec_from_file_location("p0_odd_receivers_frozen_v2", COMPILER)
    if spec is None or spec.loader is None:
        fail("cannot import frozen receiver compiler")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def qmod(value: Fraction, prime: int) -> int:
    if value.denominator % prime == 0:
        fail(("bad prime denominator", value, prime))
    return value.numerator * pow(value.denominator, -1, prime) % prime


def ranks(matrix: list[list[int]], prime: int) -> tuple[int, list[int]]:
    work = [row[:] for row in matrix]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    pivot_cols: list[int] = []
    pivot_row = 0
    for col in range(cols):
        selected = next((r for r in range(pivot_row, rows) if work[r][col] % prime), None)
        if selected is None:
            continue
        work[pivot_row], work[selected] = work[selected], work[pivot_row]
        inverse = pow(work[pivot_row][col] % prime, -1, prime)
        work[pivot_row] = [(value * inverse) % prime for value in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row:
                continue
            factor = work[row][col] % prime
            if factor:
                work[row] = [
                    (a - factor * b) % prime
                    for a, b in zip(work[row], work[pivot_row])
                ]
        pivot_cols.append(col)
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row, pivot_cols


def variable_names(nodes: list[dict[str, object]]) -> list[str]:
    return sorted({str(node["name"]) for node in nodes if node["op"] == "var"})


def dependency_masks(nodes: list[dict[str, object]]) -> list[int]:
    positions = {name: i for i, name in enumerate(NEWEST)}
    answer: list[int] = []
    for node in nodes:
        op = node["op"]
        if op == "var":
            position = positions.get(str(node["name"]))
            mask = 0 if position is None else 1 << position
        elif op in ("add", "mul"):
            mask = 0
            for child in node["args"]:
                mask |= answer[int(child)]
        else:
            mask = 0
        answer.append(mask)
    return answer


def degree_upper_bounds(nodes: list[dict[str, object]]) -> list[int]:
    newest = set(NEWEST)
    answer: list[int] = []
    for node in nodes:
        if node["op"] == "var":
            degree = int(str(node["name"]) in newest)
        elif node["op"] == "add":
            degree = max((answer[int(child)] for child in node["args"]), default=0)
        elif node["op"] == "mul":
            degree = sum(answer[int(child)] for child in node["args"])
        else:
            degree = 0
        answer.append(degree)
    return answer


def ancestors(nodes: list[dict[str, object]], roots: list[int]) -> set[int]:
    keep: set[int] = set()
    stack = roots[:]
    while stack:
        node_index = stack.pop()
        if node_index in keep:
            continue
        keep.add(node_index)
        node = nodes[node_index]
        if node["op"] in ("add", "mul"):
            stack.extend(int(child) for child in node["args"])
    return keep


Polynomial = dict[tuple[int, ...], int]


def poly_add(items: list[Polynomial], prime: int) -> Polynomial:
    answer: Polynomial = {}
    for item in items:
        for exponent, coefficient in item.items():
            value = (answer.get(exponent, 0) + coefficient) % prime
            if value:
                answer[exponent] = value
            elif exponent in answer:
                del answer[exponent]
    return answer


def poly_mul(left: Polynomial, right: Polynomial, prime: int) -> Polynomial:
    if not left or not right:
        return {}
    answer: Polynomial = {}
    for left_exponent, left_coefficient in left.items():
        for right_exponent, right_coefficient in right.items():
            exponent = tuple(a + b for a, b in zip(left_exponent, right_exponent))
            value = (
                answer.get(exponent, 0) + left_coefficient * right_coefficient
            ) % prime
            if value:
                answer[exponent] = value
            elif exponent in answer:
                del answer[exponent]
    return answer


def specialize_polynomials(
    nodes: list[dict[str, object]],
    keep: set[int],
    assignment: dict[str, int],
    prime: int,
) -> list[Polynomial | None]:
    positions = {name: i for i, name in enumerate(NEWEST)}
    answer: list[Polynomial | None] = [None] * len(nodes)
    for index, node in enumerate(nodes):
        if index not in keep:
            continue
        op = node["op"]
        if op == "const":
            value = qmod(Fraction(int(node["n"]), int(node["d"])), prime)
            polynomial = {} if value == 0 else {ZERO_EXPONENT: value}
        elif op == "var":
            name = str(node["name"])
            position = positions.get(name)
            if position is None:
                value = assignment[name] % prime
                polynomial = {} if value == 0 else {ZERO_EXPONENT: value}
            else:
                exponent = [0] * len(NEWEST)
                exponent[position] = 1
                polynomial = {tuple(exponent): 1}
        elif op == "add":
            children = [answer[int(child)] for child in node["args"]]
            if any(child is None for child in children):
                fail(("missing retained add child", index))
            polynomial = poly_add([child for child in children if child is not None], prime)
        elif op == "mul":
            polynomial = {ZERO_EXPONENT: 1}
            for child in node["args"]:
                child_polynomial = answer[int(child)]
                if child_polynomial is None:
                    fail(("missing retained mul child", index, child))
                polynomial = poly_mul(polynomial, child_polynomial, prime)
        else:
            fail(("unknown DAG operation", op))
        answer[index] = polynomial
    return answer


def polynomial_value_gradient(
    polynomial: Polynomial,
    point: tuple[int, ...],
    prime: int,
) -> tuple[int, tuple[int, ...]]:
    value = 0
    gradient = [0] * len(NEWEST)
    for exponent, coefficient in polynomial.items():
        monomial = coefficient
        for coordinate, power in zip(point, exponent):
            monomial = monomial * pow(coordinate, power, prime) % prime
        value = (value + monomial) % prime
        for position, power in enumerate(exponent):
            if power == 0:
                continue
            derivative = coefficient * power % prime
            for other_position, other_power in enumerate(exponent):
                adjusted = other_power - int(other_position == position)
                derivative = derivative * pow(point[other_position], adjusted, prime) % prime
            gradient[position] = (gradient[position] + derivative) % prime
    return value, tuple(gradient)


def evaluate_dual(
    nodes: list[dict[str, object]],
    assignment: dict[str, int],
    prime: int,
) -> tuple[list[int], list[tuple[int, ...]]]:
    positions = {name: i for i, name in enumerate(NEWEST)}
    values: list[int] = []
    gradients: list[tuple[int, ...]] = []
    zero_gradient = (0,) * len(NEWEST)
    for node in nodes:
        op = node["op"]
        if op == "const":
            value = qmod(Fraction(int(node["n"]), int(node["d"])), prime)
            gradient = zero_gradient
        elif op == "var":
            name = str(node["name"])
            value = assignment[name] % prime
            if name in positions:
                mutable = [0] * len(NEWEST)
                mutable[positions[name]] = 1
                gradient = tuple(mutable)
            else:
                gradient = zero_gradient
        elif op == "add":
            value = 0
            mutable = [0] * len(NEWEST)
            for child in node["args"]:
                child = int(child)
                value += values[child]
                for i, entry in enumerate(gradients[child]):
                    mutable[i] += entry
            value %= prime
            gradient = tuple(entry % prime for entry in mutable)
        elif op == "mul":
            value = 1
            mutable = [0] * len(NEWEST)
            for child in node["args"]:
                child = int(child)
                child_value = values[child]
                child_gradient = gradients[child]
                mutable = [
                    (entry * child_value + value * child_gradient[i]) % prime
                    for i, entry in enumerate(mutable)
                ]
                value = value * child_value % prime
            gradient = tuple(mutable)
        else:
            fail(("unknown DAG operation", op))
        values.append(value)
        gradients.append(gradient)
    return values, gradients


def predecessor_assignment(names: list[str], prime: int, seed: int) -> dict[str, int]:
    rng = random.Random(seed)
    assignment = {name: rng.randrange(1, prime) for name in names}
    b = assignment["b"]
    w = assignment["w"]
    a1 = assignment["a1"]
    aa0 = assignment["aa0"]
    rs1 = assignment["rs1"]
    ell2 = assignment["ell2"]
    inverse_a1 = pow(a1, -1, prime)
    assignment["ee0"] = (
        b * a1
        - aa0 * b * b * w * inverse_a1
        - qmod(Fraction(3, 8), prime) * w * w * b * rs1 * rs1 * inverse_a1
        + 2 * w * w * ell2 * b * b * b * inverse_a1
    ) % prime
    return assignment


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--prime", type=int, choices=(32003, 65521), required=True)
    parser.add_argument("--samples", type=int, default=4)
    args = parser.parse_args()
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if (
        platform.system() != "Linux"
        or not vendor.is_file()
        or vendor.read_text().strip() != "Amazon EC2"
        or not tag
    ):
        fail("grade-13 V2 analyzer is restricted to registered AWS EC2")
    for path, expected in EXPECTED.items():
        if digest(path) != expected:
            fail(("frozen predecessor mismatch", str(path), digest(path), expected))

    compiler = load_compiler()
    tails = compiler.canonical_tails()
    dag = compiler.Dag()
    _, source_rows, predecessor_f = compiler.terminal_source(dag, tails)
    grade_roots = [source_rows[(ell, 13)] for ell in range(1, 8)]
    masks = dependency_masks(dag.nodes)
    degree_bounds = degree_upper_bounds(dag.nodes)
    retained = ancestors(dag.nodes, grade_roots + [predecessor_f])
    names = variable_names(dag.nodes)
    root_dependencies = [
        [name for position, name in enumerate(NEWEST) if masks[root] & (1 << position)]
        for root in grade_roots
    ]
    if root_dependencies[5] or root_dependencies[6]:
        fail(("rows 6 and 7 unexpectedly depend on registered corrections", root_dependencies))

    samples = []
    all_crosschecks = True
    for index in range(args.samples):
        assignment = predecessor_assignment(names, args.prime, 230000 + 193 * index + args.prime)
        values, gradients = evaluate_dual(dag.nodes, assignment, args.prime)
        if values[predecessor_f] % args.prime:
            fail(("predecessor F assignment failed", index, values[predecessor_f]))
        dual_root_values = [values[root] for root in grade_roots]
        dual_root_gradients = [gradients[root] for root in grade_roots]
        del values, gradients
        specialized = specialize_polynomials(dag.nodes, retained, assignment, args.prime)
        point = tuple(assignment[name] for name in NEWEST)
        polynomials: list[Polynomial] = []
        polynomial_values: list[int] = []
        polynomial_gradients: list[tuple[int, ...]] = []
        for row_index, root in enumerate(grade_roots):
            polynomial = specialized[root]
            if polynomial is None:
                fail(("missing specialized root", root))
            polynomial_value, polynomial_gradient = polynomial_value_gradient(
                polynomial, point, args.prime
            )
            if (
                polynomial_value != dual_root_values[row_index]
                or polynomial_gradient != dual_root_gradients[row_index]
            ):
                all_crosschecks = False
                fail(("polynomial/dual cross-check failed", index, root))
            polynomials.append(polynomial)
            polynomial_values.append(polynomial_value)
            polynomial_gradients.append(polynomial_gradient)
        matrix = [list(gradient) for gradient in polynomial_gradients]
        rank, pivots = ranks(matrix, args.prime)
        actual_degrees = [
            max((sum(exponent) for exponent in polynomial), default=-1)
            for polynomial in polynomials
        ]
        samples.append(
            {
                "sample": index,
                "jacobian_rank": rank,
                "jacobian_pivot_variables": [NEWEST[column] for column in pivots],
                "actual_specialized_degrees": actual_degrees,
                "term_counts": [len(polynomial) for polynomial in polynomials],
                "row_values_at_registered_point": polynomial_values,
                "candidate_constraint_values_rows_6_7": polynomial_values[5:7],
                "candidate_constraints_rows_6_7_nonzero": [
                    value != 0 for value in polynomial_values[5:7]
                ],
            }
        )

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    hashes = compiler.all_expression_shas(dag.nodes)
    result = {
        "status": "PASS-P0-ODD-GRADE13-V2-POLYNOMIAL-NAVIGATION",
        "registered_aws_lane": tag,
        "prime": args.prime,
        "samples": samples,
        "newest_corrections": NEWEST,
        "root_dependencies": root_dependencies,
        "grade13_degree_upper_bounds_before_collection": [degree_bounds[root] for root in grade_roots],
        "rows_6_7_structurally_independent_of_registered_corrections": True,
        "polynomial_dual_crosscheck": all_crosschecks,
        "predecessor_F_imposed": True,
        "localized_sample_open": "b*w*a1!=0",
        "retained_ancestor_nodes": len(retained),
        "total_dag_nodes": len(dag.nodes),
        "raw_grade13_root_sha256": [hashes[root] for root in grade_roots],
        "scope": "MODULAR_SPECIALIZED_POLYNOMIAL_AND_JACOBIAN_NAVIGATION_ONLY",
        "nonclaims": [
            "no exact-Q factorization or minor",
            "no coverage of a Jacobian-minor divisor",
            "no proof that either candidate constraint vanishes or is impossible",
            "no Gate-A algebraization",
            "no order-two or JC2 verdict",
        ],
        "mathematical_endpoint": "NAVIGATION_NOT_PROOF",
        "order2_closed": False,
        "JC2": "NOT_CLAIMED",
    }
    result_path = output / "result.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("P0_ODD_G13_V2_SOURCE_HASHES=PASS")
    print("P0_ODD_G13_V2_POLY_DUAL_CROSSCHECK=PASS")
    print("P0_ODD_G13_V2_STATUS=PASS_MODULAR_POLYNOMIAL_NAVIGATION")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
