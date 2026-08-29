#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V23 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_typed_census_v23_20260827"
RESULT = V23 / "output_r1/RESULT.json"
RESULT_SHA = "ce4d0adbbe94e1337bed5047da0417e3b17cb86530715fb62316086cabd14641"
PARSER = V23 / "census_j2_typed_v23.py"
PARSER_SHA = "14f2de22d8cabaea12ac7fc7bf72cca275edbbb6a35dc7c0556a6e18e67c4501"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def add_scaled(left, right, scale: Fraction):
    answer = dict(left)
    for monomial, coefficient in right.items():
        value = answer.get(monomial, Fraction(0)) + scale * coefficient
        if value:
            answer[monomial] = value
        else:
            answer.pop(monomial, None)
    return answer


def scale(vector, coefficient: Fraction):
    return {monomial: value * coefficient for monomial, value in vector.items() if value * coefficient}


def monomial_product(left, right):
    exponents = dict(left)
    for name, exponent in right:
        exponents[name] = exponents.get(name, 0) + exponent
    return tuple(sorted((name, exponent) for name, exponent in exponents.items() if exponent))


def multiply_monomial(polynomial, multiplier):
    return {monomial_product(monomial, multiplier): coefficient for monomial, coefficient in polynomial.items()}


def enumerate_monomials(variables, weights, target):
    answer = []

    def visit(index, remaining, powers):
        if index == len(variables):
            if remaining == 0:
                answer.append(tuple(sorted((name, exponent) for name, exponent in powers if exponent)))
            return
        name = variables[index]
        weight = weights[index]
        for exponent in range(remaining // weight + 1):
            visit(index + 1, remaining - exponent * weight, powers + [(name, exponent)])

    visit(0, target, [])
    return sorted(set(answer))


def encode_fraction(value: Fraction):
    return [value.numerator, value.denominator]


def encode_monomial(monomial):
    return [[name, exponent] for name, exponent in monomial]


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: produce_a1_rho0_linear_dual_v27.py OUTPUT")
    if platform.system() != "Linux" or not os.environ.get("JC2_REGISTERED_AWS_LANE"):
        fail("registered AWS lane required")
    if Path("/sys/class/dmi/id/sys_vendor").read_text().strip() != "Amazon EC2":
        fail("Amazon EC2 required")
    output = Path(sys.argv[1]).resolve()
    if output.exists():
        fail(("refuse overwrite", str(output)))
    output.mkdir(parents=True)
    if digest(RESULT) != RESULT_SHA or digest(PARSER) != PARSER_SHA:
        fail("upstream hash")

    spec = importlib.util.spec_from_file_location("v27_parser", PARSER)
    if spec is None or spec.loader is None:
        fail("parser import")
    parser = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(parser)
    result = json.loads(RESULT.read_text())

    generators = []
    variables = {"a1"}
    row_hashes = {}
    for name, record in sorted(result["records"].items(), key=lambda item: (item[1]["grade"], item[1]["row"])):
        chart = record["charts"]["a1_ordered"]
        path = V23 / "output_r1" / chart["output"]
        if digest(path) != chart["output_sha256"]:
            fail(("row hash", name))
        polynomial = parser.specialize(parser.parse(path), frozenset({"rho"}), {})
        grade = int(record["grade"])
        for monomial in polynomial:
            if sum(parser.sigma_weight(variable) * exponent for variable, exponent in monomial) != grade:
                fail(("inhomogeneous row", name, monomial))
            variables.update(variable for variable, _ in monomial)
        row_hashes[str(path.relative_to(ROOT))] = chart["output_sha256"]
        if polynomial:
            generators.append((name, grade, polynomial))

    ordered_variables = sorted(variables, key=lambda name: (parser.sigma_weight(name), name))
    weights = [parser.sigma_weight(name) for name in ordered_variables]
    candidates = []
    for name, grade, polynomial in generators:
        for multiplier in enumerate_monomials(ordered_variables, weights, 15 - grade):
            candidate = multiply_monomial(polynomial, multiplier)
            if any(sum(parser.sigma_weight(variable) * exponent for variable, exponent in monomial) != 15 for monomial in candidate):
                fail(("candidate weight", name, multiplier))
            candidates.append((name, multiplier, candidate))

    # Exact reduced row-echelon basis for the column span, with each basis
    # vector tracked as a combination of the enumerated ideal products.
    basis = {}
    for candidate_index, (_, _, candidate) in enumerate(candidates):
        vector = dict(candidate)
        combination = {candidate_index: Fraction(1)}
        for pivot in sorted(basis):
            if pivot in vector:
                factor = vector[pivot]
                vector = add_scaled(vector, basis[pivot][0], -factor)
                combination = add_scaled(combination, basis[pivot][1], -factor)
        if not vector:
            continue
        pivot = min(vector)
        inverse = Fraction(1, 1) / vector[pivot]
        vector = scale(vector, inverse)
        combination = scale(combination, inverse)
        for old_pivot in list(basis):
            old_vector, old_combination = basis[old_pivot]
            if pivot in old_vector:
                factor = old_vector[pivot]
                basis[old_pivot] = (
                    add_scaled(old_vector, vector, -factor),
                    add_scaled(old_combination, combination, -factor),
                )
        basis[pivot] = (vector, combination)

    target_monomial = (("a1", 3),)
    target = {target_monomial: Fraction(1)}
    residual = dict(target)
    solution = {}
    for pivot in sorted(basis):
        if pivot in residual:
            factor = residual[pivot]
            residual = add_scaled(residual, basis[pivot][0], -factor)
            solution = add_scaled(solution, basis[pivot][1], factor)

    certificate = {
        "status": "PASS-A1-RHO0-LINEAR-DUAL-V27-PRODUCER",
        "target": "a1^3",
        "target_weight": 15,
        "input_rows": 42,
        "nonzero_generators": len(generators),
        "candidate_count": len(candidates),
        "span_rank": len(basis),
        "ambient_variables": ordered_variables,
        "ambient_weights": weights,
        "row_sha256": row_hashes,
    }
    if not residual:
        replay = {}
        lift = []
        for index, coefficient in sorted(solution.items()):
            if not coefficient:
                continue
            name, multiplier, candidate = candidates[index]
            replay = add_scaled(replay, candidate, coefficient)
            lift.append({
                "generator": name,
                "multiplier": encode_monomial(multiplier),
                "coefficient": encode_fraction(coefficient),
            })
        if replay != target:
            fail("internal membership replay")
        certificate.update({"outcome": "membership", "lift": lift})
    else:
        free_coordinate = min(residual)
        functional = {free_coordinate: Fraction(1)}
        for pivot, (vector, _) in basis.items():
            if vector.get(free_coordinate):
                functional[pivot] = -vector[free_coordinate]
        target_value = sum(coefficient * functional.get(monomial, Fraction(0)) for monomial, coefficient in target.items())
        if not target_value:
            fail("zero target functional")
        functional = scale(functional, Fraction(1, 1) / target_value)
        for name, multiplier, candidate in candidates:
            value = sum(coefficient * functional.get(monomial, Fraction(0)) for monomial, coefficient in candidate.items())
            if value:
                fail(("internal dual failure", name, multiplier, value))
        if sum(coefficient * functional.get(monomial, Fraction(0)) for monomial, coefficient in target.items()) != 1:
            fail("internal target dual failure")
        certificate.update({
            "outcome": "nonmembership",
            "functional_support": [
                {"monomial": encode_monomial(monomial), "coefficient": encode_fraction(coefficient)}
                for monomial, coefficient in sorted(functional.items()) if coefficient
            ],
            "residual_support_size": len(residual),
        })

    certificate_path = output / "CERTIFICATE.json"
    certificate_path.write_text(json.dumps(certificate, sort_keys=True, indent=2) + "\n")
    print("PASS-A1-RHO0-LINEAR-DUAL-V27-PRODUCER")
    print(f"OUTCOME={certificate['outcome']}")
    print(f"NONZERO_GENERATORS={len(generators)}")
    print(f"CANDIDATE_COUNT={len(candidates)}")
    print(f"SPAN_RANK={len(basis)}")
    print(f"CERTIFICATE_SHA256={digest(certificate_path)}")


if __name__ == "__main__":
    main()

