#!/usr/bin/env python3
"""AWS-only exact-Q collection of the p=0 odd-sheet grade-13 rows."""

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
TERM_CAP = 500000


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_compiler():
    spec = importlib.util.spec_from_file_location("p0_odd_receivers_frozen_exact", COMPILER)
    if spec is None or spec.loader is None:
        fail("cannot import frozen receiver compiler")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def ancestors(nodes: list[dict[str, object]], roots: list[int]) -> set[int]:
    keep: set[int] = set()
    stack = roots[:]
    while stack:
        index = stack.pop()
        if index in keep:
            continue
        keep.add(index)
        node = nodes[index]
        if node["op"] in ("add", "mul"):
            stack.extend(int(child) for child in node["args"])
    return keep


Polynomial = dict[tuple[int, ...], Fraction]


def add_polynomials(items: list[Polynomial]) -> Polynomial:
    answer: Polynomial = {}
    for item in items:
        for monomial, coefficient in item.items():
            value = answer.get(monomial, Fraction(0)) + coefficient
            if value:
                answer[monomial] = value
            elif monomial in answer:
                del answer[monomial]
    return answer


def multiply_polynomials(left: Polynomial, right: Polynomial) -> Polynomial:
    if not left or not right:
        return {}
    answer: Polynomial = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial = tuple(a + b for a, b in zip(left_monomial, right_monomial))
            value = answer.get(monomial, Fraction(0)) + left_coefficient * right_coefficient
            if value:
                answer[monomial] = value
            elif monomial in answer:
                del answer[monomial]
    if len(answer) > TERM_CAP:
        fail(("exact expansion term cap", len(answer), TERM_CAP))
    return answer


def expand_exact(
    nodes: list[dict[str, object]],
    keep: set[int],
    variables: list[str],
) -> list[Polynomial | None]:
    positions = {name: i for i, name in enumerate(variables)}
    zero_monomial = (0,) * len(variables)
    answer: list[Polynomial | None] = [None] * len(nodes)
    for index, node in enumerate(nodes):
        if index not in keep:
            continue
        op = node["op"]
        if op == "const":
            coefficient = Fraction(int(node["n"]), int(node["d"]))
            polynomial = {} if coefficient == 0 else {zero_monomial: coefficient}
        elif op == "var":
            monomial = [0] * len(variables)
            monomial[positions[str(node["name"])]] = 1
            polynomial = {tuple(monomial): Fraction(1)}
        elif op == "add":
            children = [answer[int(child)] for child in node["args"]]
            if any(child is None for child in children):
                fail(("missing retained add child", index))
            polynomial = add_polynomials([child for child in children if child is not None])
        elif op == "mul":
            polynomial = {zero_monomial: Fraction(1)}
            for child in node["args"]:
                child_polynomial = answer[int(child)]
                if child_polynomial is None:
                    fail(("missing retained mul child", index, child))
                polynomial = multiply_polynomials(polynomial, child_polynomial)
        else:
            fail(("unknown DAG operation", op))
        answer[index] = polynomial
    return answer


def qmod(value: Fraction, prime: int) -> int:
    return value.numerator * pow(value.denominator, -1, prime) % prime


def evaluate_polynomial(
    polynomial: Polynomial,
    point: dict[str, int],
    variables: list[str],
    prime: int,
) -> int:
    value = 0
    for monomial, coefficient in polynomial.items():
        term = qmod(coefficient, prime)
        for variable, exponent in zip(variables, monomial):
            if exponent:
                term = term * pow(point[variable], exponent, prime) % prime
        value = (value + term) % prime
    return value


def evaluate_dag(
    nodes: list[dict[str, object]], assignment: dict[str, int], prime: int
) -> list[int]:
    values: list[int] = []
    for node in nodes:
        op = node["op"]
        if op == "const":
            value = qmod(Fraction(int(node["n"]), int(node["d"])), prime)
        elif op == "var":
            value = assignment[str(node["name"])] % prime
        elif op == "add":
            value = sum(values[int(child)] for child in node["args"]) % prime
        elif op == "mul":
            value = 1
            for child in node["args"]:
                value = value * values[int(child)] % prime
        else:
            fail(("unknown DAG operation", op))
        values.append(value)
    return values


def serialize(polynomial: Polynomial, variables: list[str]) -> list[dict[str, object]]:
    terms = []
    for monomial, coefficient in sorted(polynomial.items(), reverse=True):
        terms.append(
            {
                "coefficient": [coefficient.numerator, coefficient.denominator],
                "monomial": [
                    [variable, exponent]
                    for variable, exponent in zip(variables, monomial)
                    if exponent
                ],
            }
        )
    return terms


def singular_expression(polynomial: Polynomial, variables: list[str]) -> str:
    if not polynomial:
        return "0"
    terms = []
    for monomial, coefficient in sorted(polynomial.items(), reverse=True):
        factors = [
            variable if exponent == 1 else f"{variable}^{exponent}"
            for variable, exponent in zip(variables, monomial)
            if exponent
        ]
        if coefficient.denominator == 1:
            scalar = str(coefficient.numerator)
        else:
            scalar = f"({coefficient.numerator}/{coefficient.denominator})"
        terms.append("*".join([scalar] + factors) if factors else scalar)
    return "+".join(terms).replace("+-", "-")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if (
        platform.system() != "Linux"
        or not vendor.is_file()
        or vendor.read_text().strip() != "Amazon EC2"
        or not tag
    ):
        fail("grade-13 exact extractor is restricted to registered AWS EC2")
    for path, expected in EXPECTED.items():
        if digest(path) != expected:
            fail(("frozen predecessor mismatch", str(path), digest(path), expected))

    compiler = load_compiler()
    tails = compiler.canonical_tails()
    dag = compiler.Dag()
    _, source_rows, predecessor_f = compiler.terminal_source(dag, tails)
    grade_roots = [source_rows[(ell, 13)] for ell in range(1, 8)]
    retained = ancestors(dag.nodes, grade_roots + [predecessor_f])
    variables = sorted(
        {
            str(dag.nodes[index]["name"])
            for index in retained
            if dag.nodes[index]["op"] == "var"
        }
    )
    expanded = expand_exact(dag.nodes, retained, variables)
    grade_polynomials = [expanded[root] for root in grade_roots]
    predecessor_polynomial = expanded[predecessor_f]
    if any(polynomial is None for polynomial in grade_polynomials) or predecessor_polynomial is None:
        fail("missing exact root expansion")
    grade_polynomials = [polynomial for polynomial in grade_polynomials if polynomial is not None]
    if any(grade_polynomials[index] for index in range(3, 7)):
        fail(("rows four through seven failed exact-zero collection", [len(p) for p in grade_polynomials]))
    newest_positions = [variables.index(name) for name in NEWEST if name in variables]
    for row_index in (1, 2):
        if any(
            any(monomial[position] for position in newest_positions)
            for monomial in grade_polynomials[row_index]
        ):
            fail(("row two or three retained a registered newest correction", row_index + 1))
    if max(
        (
            sum(monomial[position] for position in newest_positions)
            for monomial in grade_polynomials[0]
        ),
        default=0,
    ) > 1:
        fail("row one failed exact affine collection")

    modular_crosschecks = []
    for prime in (32003, 65521):
        rng = random.Random(330000 + prime)
        assignment = {
            str(node["name"]): rng.randrange(1, prime)
            for node in dag.nodes
            if node["op"] == "var"
        }
        dag_values = evaluate_dag(dag.nodes, assignment, prime)
        row_checks = [
            evaluate_polynomial(polynomial, assignment, variables, prime) == dag_values[root]
            for polynomial, root in zip(grade_polynomials, grade_roots)
        ]
        predecessor_check = (
            evaluate_polynomial(predecessor_polynomial, assignment, variables, prime)
            == dag_values[predecessor_f]
        )
        if not all(row_checks) or not predecessor_check:
            fail(("exact expansion modular crosscheck", prime, row_checks, predecessor_check))
        modular_crosschecks.append(
            {"prime": prime, "row_checks": row_checks, "predecessor_check": predecessor_check}
        )

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    payload = {
        "format": "JC2_EXACT_SPARSE_POLYNOMIAL_V1",
        "variables": variables,
        "predecessor_F": serialize(predecessor_polynomial, variables),
        "grade13_rows": {
            str(index + 1): serialize(polynomial, variables)
            for index, polynomial in enumerate(grade_polynomials)
        },
    }
    polynomial_path = output / "grade13_exact_polynomials.json"
    polynomial_path.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")

    singular_path = output / "grade13_reduce_factor.sing"
    singular_path.write_text(
        "ring r=0,(" + ",".join(variables) + "),dp;\n"
        + "option(redSB);\n"
        + f"poly F={singular_expression(predecessor_polynomial, variables)};\n"
        + f"poly G1={singular_expression(grade_polynomials[0], variables)};\n"
        + f"poly G2={singular_expression(grade_polynomials[1], variables)};\n"
        + f"poly G3={singular_expression(grade_polynomials[2], variables)};\n"
        + "ideal IF=F; ideal SF=std(IF);\n"
        + "poly R2=reduce(G2,SF); poly R3=reduce(G3,SF);\n"
        + 'print("P0_ODD_G13_EXACT_SINGULAR_SOURCE=PASS");\n'
        + 'if (R2==0) { print("ROW2_IN_RAW_F_IDEAL=1"); } else { print("ROW2_IN_RAW_F_IDEAL=0"); }\n'
        + 'if (R3==0) { print("ROW3_IN_RAW_F_IDEAL=1"); } else { print("ROW3_IN_RAW_F_IDEAL=0"); }\n'
        + 'print("PREDECESSOR_F"); F; print("ROW1"); G1; print("ROW2"); G2; print("ROW3"); G3;\n'
        + 'print("ROW2_REDUCED_MOD_F"); R2; print("ROW3_REDUCED_MOD_F"); R3;\n'
        + 'print("FACTOR_ROW2"); factorize(G2); print("FACTOR_ROW3"); factorize(G3);\n'
        + 'print("FACTOR_ROW2_REDUCED"); factorize(R2); print("FACTOR_ROW3_REDUCED"); factorize(R3);\n'
        + 'print("GCD_ROW2_ROW3"); gcd(G2,G3);\n'
        + 'print("P0_ODD_G13_EXACT_SINGULAR_DONE=PASS");\n'
        + "quit;\n"
    )

    hashes = compiler.all_expression_shas(dag.nodes)
    result = {
        "status": "PASS-P0-ODD-GRADE13-EXACT-COLLECTION",
        "registered_aws_lane": tag,
        "characteristic": 0,
        "variables": variables,
        "retained_ancestor_nodes": len(retained),
        "total_dag_nodes": len(dag.nodes),
        "term_counts": [len(polynomial) for polynomial in grade_polynomials],
        "predecessor_F_term_count": len(predecessor_polynomial),
        "rows_4_through_7_exact_zero": True,
        "rows_2_3_independent_of_registered_newest": True,
        "row_1_affine_in_registered_newest": True,
        "modular_expansion_crosschecks": modular_crosschecks,
        "raw_grade13_root_sha256": [hashes[root] for root in grade_roots],
        "polynomials_sha256": digest(polynomial_path),
        "singular_source_sha256": digest(singular_path),
        "scope": "EXACT_Q_COLLECTION_AND_RAW_F_REDUCTION_INPUT_NO_GLOBAL_INTERFACE",
        "mathematical_endpoint": "AWAIT_SINGULAR_REDUCTION_AND_FACTOR_OUTPUT",
        "order2_closed": False,
        "JC2": "NOT_CLAIMED",
    }
    (output / "result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("P0_ODD_G13_EXACT_SOURCE_HASHES=PASS")
    print("P0_ODD_G13_EXACT_ROWS4_7_ZERO=PASS")
    print("P0_ODD_G13_EXACT_EXPANSION_CROSSCHECK=PASS")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
