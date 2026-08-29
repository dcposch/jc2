#!/usr/bin/env python3
"""AWS-only exact Laurent reduction of grade 14 by the grade-13 pivots."""

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
EXACT_HELPER = HERE / "extract_grade13_exact.py"
THEOREM = HERE.parents[1] / "xmodel/max12-812-order2-p0-odd-grade13-triangular-prolongation-20260826.md"
EXPECTED = {
    EXACT_HELPER: "a1e2e5fa763901b71c1808a7e1920d8467cf8d0881de071784604395519e5fa5",
    THEOREM: "1ff6433a3122b60c6ac872cefe9b23db34918bc63467c70a67f7ffcc2e6e86d9",
}
PIVOTS = ("ee0", "ell2", "ee1", "ac2")


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_helper():
    spec = importlib.util.spec_from_file_location("p0_odd_g13_exact_frozen", EXACT_HELPER)
    if spec is None or spec.loader is None:
        fail("cannot import frozen grade-13 exact helper")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


Polynomial = dict[tuple[int, ...], Fraction]


def add(items: list[Polynomial]) -> Polynomial:
    answer: Polynomial = {}
    for item in items:
        for monomial, coefficient in item.items():
            value = answer.get(monomial, Fraction(0)) + coefficient
            if value:
                answer[monomial] = value
            elif monomial in answer:
                del answer[monomial]
    return answer


def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
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
    if len(answer) > 500000:
        fail(("Laurent expansion term cap", len(answer)))
    return answer


def power(polynomial: Polynomial, exponent: int, width: int) -> Polynomial:
    answer = {(0,) * width: Fraction(1)}
    base = polynomial
    remaining = exponent
    while remaining:
        if remaining & 1:
            answer = multiply(answer, base)
        remaining //= 2
        if remaining:
            base = multiply(base, base)
    return answer


def substitute(polynomial: Polynomial, position: int, replacement: Polynomial) -> Polynomial:
    width = len(next(iter(polynomial))) if polynomial else len(next(iter(replacement)))
    answer: Polynomial = {}
    for monomial, coefficient in polynomial.items():
        exponent = monomial[position]
        base_monomial = list(monomial)
        base_monomial[position] = 0
        base = {tuple(base_monomial): coefficient}
        answer = add([answer, multiply(base, power(replacement, exponent, width))])
    return answer


def solve_unit_monomial(
    polynomial: Polynomial, position: int, variables: list[str]
) -> Polynomial:
    coefficient: Polynomial = {}
    rest: Polynomial = {}
    for monomial, value in polynomial.items():
        exponent = monomial[position]
        reduced = list(monomial)
        reduced[position] = 0
        if exponent == 0:
            rest[tuple(reduced)] = value
        elif exponent == 1:
            coefficient[tuple(reduced)] = value
        else:
            fail(("pivot is nonlinear", variables[position], exponent))
    if len(coefficient) != 1:
        fail(("pivot coefficient is not one monomial", variables[position], len(coefficient)))
    coefficient_monomial, coefficient_scalar = next(iter(coefficient.items()))
    negative_inverse = -1 / coefficient_scalar
    answer: Polynomial = {}
    for monomial, value in rest.items():
        shifted = tuple(a - b for a, b in zip(monomial, coefficient_monomial))
        answer[shifted] = value * negative_inverse
    return answer


def clear_laurent(
    polynomial: Polynomial, variables: list[str]
) -> tuple[Polynomial, dict[str, int]]:
    if not polynomial:
        return {}, {}
    minima = [min(monomial[i] for monomial in polynomial) for i in range(len(variables))]
    shift = [max(0, -minimum) for minimum in minima]
    clearing = {
        variable: amount for variable, amount in zip(variables, shift) if amount
    }
    if any(variable not in ("b", "w") for variable in clearing):
        fail(("non-bw Laurent denominator", clearing))
    cleared = {
        tuple(exponent + amount for exponent, amount in zip(monomial, shift)): coefficient
        for monomial, coefficient in polynomial.items()
    }
    return cleared, clearing


def serialize(polynomial: Polynomial, variables: list[str]) -> list[dict[str, object]]:
    return [
        {
            "coefficient": [coefficient.numerator, coefficient.denominator],
            "monomial": [
                [variable, exponent]
                for variable, exponent in zip(variables, monomial)
                if exponent
            ],
        }
        for monomial, coefficient in sorted(polynomial.items(), reverse=True)
    ]


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
        scalar = (
            str(coefficient.numerator)
            if coefficient.denominator == 1
            else f"({coefficient.numerator}/{coefficient.denominator})"
        )
        terms.append("*".join([scalar] + factors) if factors else scalar)
    return "+".join(terms).replace("+-", "-")


def variable_degree(polynomial: Polynomial, position: int) -> int:
    return max((monomial[position] for monomial in polynomial), default=-1)


def unit_linear_candidates(
    polynomial: Polynomial, variables: list[str]
) -> list[dict[str, object]]:
    candidates = []
    for position, variable in enumerate(variables):
        if variable in ("b", "w") or variable_degree(polynomial, position) != 1:
            continue
        coefficient: Polynomial = {}
        for monomial, value in polynomial.items():
            if monomial[position] == 1:
                reduced = list(monomial)
                reduced[position] = 0
                reduced = tuple(reduced)
                coefficient[reduced] = coefficient.get(reduced, Fraction(0)) + value
        coefficient = {monomial: value for monomial, value in coefficient.items() if value}
        if len(coefficient) != 1:
            continue
        monomial, scalar = next(iter(coefficient.items()))
        support = {
            variables[i]: exponent for i, exponent in enumerate(monomial) if exponent
        }
        if set(support).issubset({"b", "w"}):
            candidates.append(
                {
                    "variable": variable,
                    "coefficient": [scalar.numerator, scalar.denominator],
                    "unit_monomial": support,
                }
            )
    return candidates


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
        fail("grade-14 exact reducer is restricted to registered AWS EC2")
    for path, expected in EXPECTED.items():
        if digest(path) != expected:
            fail(("frozen predecessor mismatch", str(path), digest(path), expected))

    helper = load_helper()
    compiler = helper.load_compiler()
    tails = compiler.canonical_tails()
    dag = compiler.Dag()
    _, source_rows, predecessor_f = compiler.terminal_source(dag, tails)
    grade13_roots = [source_rows[(ell, 13)] for ell in range(1, 8)]
    grade14_roots = [source_rows[(ell, 14)] for ell in range(1, 8)]
    retained = helper.ancestors(
        dag.nodes, grade13_roots + grade14_roots + [predecessor_f]
    )
    variables = sorted(
        {
            str(dag.nodes[index]["name"])
            for index in retained
            if dag.nodes[index]["op"] == "var"
        }
    )
    expanded = helper.expand_exact(dag.nodes, retained, variables)
    grade13 = [expanded[root] for root in grade13_roots]
    grade14 = [expanded[root] for root in grade14_roots]
    predecessor = expanded[predecessor_f]
    if predecessor is None or any(item is None for item in grade13 + grade14):
        fail("missing exact grade-13/14 expansion")
    grade13 = [item for item in grade13 if item is not None]
    grade14 = [item for item in grade14 if item is not None]

    modular_crosschecks = []
    for prime in (32003, 65521):
        rng = random.Random(440000 + prime)
        assignment = {
            str(node["name"]): rng.randrange(1, prime)
            for node in dag.nodes
            if node["op"] == "var"
        }
        dag_values = helper.evaluate_dag(dag.nodes, assignment, prime)
        grade13_checks = [
            helper.evaluate_polynomial(polynomial, assignment, variables, prime)
            == dag_values[root]
            for polynomial, root in zip(grade13, grade13_roots)
        ]
        grade14_checks = [
            helper.evaluate_polynomial(polynomial, assignment, variables, prime)
            == dag_values[root]
            for polynomial, root in zip(grade14, grade14_roots)
        ]
        predecessor_check = (
            helper.evaluate_polynomial(predecessor, assignment, variables, prime)
            == dag_values[predecessor_f]
        )
        if not all(grade13_checks + grade14_checks) or not predecessor_check:
            fail(("exact expansion modular crosscheck", prime))
        modular_crosschecks.append(
            {
                "prime": prime,
                "grade13_checks": grade13_checks,
                "grade14_checks": grade14_checks,
                "predecessor_check": predecessor_check,
            }
        )

    substitutions: dict[str, Polynomial] = {}
    pivot_equations = [grade13[2], predecessor, grade13[1], grade13[0]]
    prior_positions: list[int] = []
    for pivot, equation in zip(PIVOTS, pivot_equations):
        reduced_equation = equation
        for prior_pivot, prior_position in zip(PIVOTS, prior_positions):
            reduced_equation = substitute(
                reduced_equation, prior_position, substitutions[prior_pivot]
            )
        position = variables.index(pivot)
        substitutions[pivot] = solve_unit_monomial(reduced_equation, position, variables)
        prior_positions.append(position)

    def reduce_all(polynomial: Polynomial) -> Polynomial:
        answer = polynomial
        for pivot in PIVOTS:
            answer = substitute(answer, variables.index(pivot), substitutions[pivot])
        return answer

    reduced_grade13 = [reduce_all(item) for item in grade13]
    if any(reduced_grade13):
        fail(("grade-13 pivot reduction failed", [len(item) for item in reduced_grade13]))
    reduced_grade14 = [reduce_all(item) for item in grade14]
    cleared_grade14 = []
    clearing = []
    for polynomial in reduced_grade14:
        cleared, monomial = clear_laurent(polynomial, variables)
        cleared_grade14.append(cleared)
        clearing.append(monomial)

    remaining_variables = [variable for variable in variables if variable not in PIVOTS]
    def remove_pivot_coordinates(polynomial: Polynomial) -> Polynomial:
        positions = [variables.index(variable) for variable in remaining_variables]
        if any(
            any(monomial[variables.index(pivot)] for pivot in PIVOTS)
            for monomial in polynomial
        ):
            fail("a pivot survived grade-14 reduction")
        return {
            tuple(monomial[position] for position in positions): coefficient
            for monomial, coefficient in polynomial.items()
        }

    compact_grade14 = [remove_pivot_coordinates(item) for item in cleared_grade14]
    unit_candidates = [
        unit_linear_candidates(polynomial, remaining_variables)
        for polynomial in compact_grade14
    ]

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    payload = {
        "format": "JC2_EXACT_LAURENT_REDUCED_POLYNOMIAL_V1",
        "normalization": "D(b*w)",
        "variables": remaining_variables,
        "pivot_substitutions": {
            pivot: serialize(substitutions[pivot], variables) for pivot in PIVOTS
        },
        "grade14_clearing_monomials": clearing,
        "grade14_numerators": {
            str(index + 1): serialize(polynomial, remaining_variables)
            for index, polynomial in enumerate(compact_grade14)
        },
    }
    polynomial_path = output / "grade14_reduced_exact.json"
    polynomial_path.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")

    singular_path = output / "grade14_factor.sing"
    source = "ring r=0,(" + ",".join(remaining_variables) + "),dp;\n"
    nonzero_names = []
    for index, polynomial in enumerate(compact_grade14, start=1):
        name = f"H{index}"
        source += f"poly {name}={singular_expression(polynomial, remaining_variables)};\n"
        if polynomial:
            nonzero_names.append(name)
    source += 'print("P0_ODD_G14_EXACT_SINGULAR_SOURCE=PASS");\n'
    for index, polynomial in enumerate(compact_grade14, start=1):
        source += f'print("GRADE14_ROW_{index}"); H{index}; print("FACTOR_GRADE14_ROW_{index}"); '
        source += f"factorize(H{index});\n" if polynomial else 'print("EXACT_ZERO");\n'
    if nonzero_names:
        source += f"poly GG={nonzero_names[0]};\n"
        for name in nonzero_names[1:]:
            source += f"GG=gcd(GG,{name});\n"
        source += 'print("GCD_NONZERO_GRADE14_ROWS"); GG;\n'
    source += 'print("P0_ODD_G14_EXACT_SINGULAR_DONE=PASS");\nquit;\n'
    singular_path.write_text(source)

    result = {
        "status": "PASS-P0-ODD-GRADE14-EXACT-LAURENT-REDUCTION",
        "registered_aws_lane": tag,
        "characteristic": 0,
        "grade13_reduces_to_zero": True,
        "pivots": PIVOTS,
        "raw_grade14_term_counts": [len(item) for item in grade14],
        "reduced_grade14_term_counts": [len(item) for item in reduced_grade14],
        "cleared_grade14_term_counts": [len(item) for item in compact_grade14],
        "clearing_monomials": clearing,
        "unit_linear_candidates": unit_candidates,
        "modular_expansion_crosschecks": modular_crosschecks,
        "remaining_variables": remaining_variables,
        "polynomials_sha256": digest(polynomial_path),
        "singular_source_sha256": digest(singular_path),
        "scope": "LOCAL_D_BW_GRADE14_NAVIGATION_AFTER_EXACT_GRADE13_PIVOTS",
        "mathematical_endpoint": "AWAIT_FACTOR_OUTPUT_NO_GRADE14_THEOREM",
        "order2_closed": False,
        "JC2": "NOT_CLAIMED",
    }
    (output / "result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("P0_ODD_G14_EXACT_SOURCE_HASHES=PASS")
    print("P0_ODD_G14_GRADE13_REDUCTION=PASS")
    print("P0_ODD_G14_EXACT_STATUS=PASS_LAURENT_REDUCTION")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
