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


def decode_fraction(pair):
    if not isinstance(pair, list) or len(pair) != 2:
        fail(("fraction syntax", pair))
    value = Fraction(int(pair[0]), int(pair[1]))
    if [value.numerator, value.denominator] != pair:
        fail(("fraction not canonical", pair))
    return value


def decode_monomial(encoded):
    monomial = tuple((str(name), int(exponent)) for name, exponent in encoded)
    if any(exponent <= 0 for _, exponent in monomial) or tuple(sorted(monomial)) != monomial:
        fail(("monomial syntax", encoded))
    if len({name for name, _ in monomial}) != len(monomial):
        fail(("duplicate monomial variable", encoded))
    return monomial


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
        for exponent in range(remaining // weights[index] + 1):
            visit(index + 1, remaining - exponent * weights[index], powers + [(variables[index], exponent)])

    visit(0, target, [])
    return sorted(set(answer))


def add_scaled(left, right, scale):
    answer = dict(left)
    for monomial, coefficient in right.items():
        value = answer.get(monomial, Fraction(0)) + scale * coefficient
        if value:
            answer[monomial] = value
        else:
            answer.pop(monomial, None)
    return answer


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: validate_a1_rho0_linear_dual_v27.py OUTPUT")
    if platform.system() != "Linux" or not os.environ.get("JC2_REGISTERED_AWS_LANE"):
        fail("registered AWS lane required")
    if Path("/sys/class/dmi/id/sys_vendor").read_text().strip() != "Amazon EC2":
        fail("Amazon EC2 required")
    output = Path(sys.argv[1]).resolve()
    certificate_path = output / "CERTIFICATE.json"
    certificate = json.loads(certificate_path.read_text())
    if digest(RESULT) != RESULT_SHA or digest(PARSER) != PARSER_SHA:
        fail("upstream hash")

    spec = importlib.util.spec_from_file_location("v27_validator_parser", PARSER)
    if spec is None or spec.loader is None:
        fail("parser import")
    parser = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(parser)
    result = json.loads(RESULT.read_text())

    generators = {}
    variables = {"a1"}
    row_hashes = {}
    grades = {}
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
            generators[name] = polynomial
            grades[name] = grade

    ordered_variables = sorted(variables, key=lambda name: (parser.sigma_weight(name), name))
    weights = [parser.sigma_weight(name) for name in ordered_variables]
    candidates = []
    candidate_lookup = {}
    for name, polynomial in generators.items():
        for multiplier in enumerate_monomials(ordered_variables, weights, 15 - grades[name]):
            candidate = multiply_monomial(polynomial, multiplier)
            candidates.append((name, multiplier, candidate))
            candidate_lookup[(name, multiplier)] = candidate

    fixed = {
        "status": "PASS-A1-RHO0-LINEAR-DUAL-V27-PRODUCER",
        "target": "a1^3",
        "target_weight": 15,
        "input_rows": 42,
        "nonzero_generators": len(generators),
        "candidate_count": len(candidates),
        "ambient_variables": ordered_variables,
        "ambient_weights": weights,
        "row_sha256": row_hashes,
    }
    for key, value in fixed.items():
        if certificate.get(key) != value:
            fail(("metadata mismatch", key))
    if not isinstance(certificate.get("span_rank"), int) or not 0 <= certificate["span_rank"] <= len(candidates):
        fail("span rank syntax")

    target = {(("a1", 3),): Fraction(1)}
    outcome = certificate.get("outcome")
    if outcome == "nonmembership":
        functional = {}
        for record in certificate.get("functional_support", []):
            monomial = decode_monomial(record["monomial"])
            coefficient = decode_fraction(record["coefficient"])
            if not coefficient or monomial in functional:
                fail(("functional syntax", record))
            if sum(parser.sigma_weight(variable) * exponent for variable, exponent in monomial) != 15:
                fail(("functional weight", monomial))
            functional[monomial] = coefficient
        if not functional:
            fail("empty functional")
        for name, multiplier, candidate in candidates:
            value = sum(coefficient * functional.get(monomial, Fraction(0)) for monomial, coefficient in candidate.items())
            if value:
                fail(("functional does not annihilate", name, multiplier, value))
        target_value = sum(coefficient * functional.get(monomial, Fraction(0)) for monomial, coefficient in target.items())
        if target_value != 1:
            fail(("functional target value", target_value))
    elif outcome == "membership":
        replay = {}
        seen = set()
        for record in certificate.get("lift", []):
            name = str(record["generator"])
            multiplier = decode_monomial(record["multiplier"])
            coefficient = decode_fraction(record["coefficient"])
            key = (name, multiplier)
            if not coefficient or key in seen or key not in candidate_lookup:
                fail(("lift syntax", record))
            seen.add(key)
            replay = add_scaled(replay, candidate_lookup[key], coefficient)
        if replay != target:
            fail("membership replay")
    else:
        fail(("outcome", outcome))

    print("PASS-A1-RHO0-LINEAR-DUAL-V27-VALIDATOR")
    print(f"OUTCOME={outcome}")
    print(f"CANDIDATE_COUNT={len(candidates)}")
    print(f"CERTIFICATE_SHA256={digest(certificate_path)}")


if __name__ == "__main__":
    main()

