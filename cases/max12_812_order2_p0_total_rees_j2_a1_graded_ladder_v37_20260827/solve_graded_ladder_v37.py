#!/usr/bin/env python3
from __future__ import annotations

import argparse
from collections import deque
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PARSER = ROOT / "cases/max12_812_order2_p0_total_rees_j2_typed_census_v23_20260827/census_j2_typed_v23.py"
PARSER_SHA = "14f2de22d8cabaea12ac7fc7bf72cca275edbbb6a35dc7c0556a6e18e67c4501"
V23 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_typed_census_v23_20260827"
V23_RESULT = V23 / "output_r1/RESULT.json"
V23_RESULT_SHA = "ce4d0adbbe94e1337bed5047da0417e3b17cb86530715fb62316086cabd14641"
LATER = {
    16: (ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g16_v28_20260827/aws_q/compiled",
         "7e00fc2ca8de3fee8ddf9cfa7b9adfef526cc8f1cc2efcb90fb7290e8fece3ae"),
    17: (ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g17_v30_20260827/aws_q/compiled",
         "6a644c20551874563d6c85cdbf81e5838ef22906e9ac7ada67b075889befb7c1"),
    18: (ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g18_v33_20260827/aws_q/compiled",
         "22f64fbb9d2107508f7218a9aabaea03d6c502219baef84bb918352f7e38df0f"),
    19: (ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_grade19_rational_orbit_v35_20260827/aws_q/compiled",
         "074c7b817d115805ea6e784225fc1dad64d54769ae89421a78ba65769903e256"),
}
PREREG = HERE / "PREREGISTRATION.md"
TARGETS = {
    17: {"a1": 1, "k": 3},
    18: {"a1": 2, "k": 2},
    19: {"a1": 3, "k": 1},
    20: {"a1": 4},
}
EXPECTED = {
    17: {"products": 217, "support": 1231, "component_products": 0, "component_monomials": 1, "component_nnz": 0},
    18: {"products": 426, "support": 2564, "component_products": 0, "component_monomials": 1, "component_nnz": 0},
    19: {"products": 803, "support": 5078, "component_products": 50, "component_monomials": 696, "component_nnz": 2086},
    20: {"products": 1473, "support": 8536, "component_products": 161, "component_monomials": 982, "component_nnz": 2951},
}
ROW_COUNTS = {10: 0, 11: 1, 12: 4, 13: 5, 14: 6, 15: 7, 16: 7, 17: 7, 18: 7, 19: 7}
TERM_COUNTS = {10: 0, 11: 1, 12: 9, 13: 28, 14: 75, 15: 187, 16: 424, 17: 867, 18: 1647, 19: 2929}
SELECTOR_PRIMES = (65521, 65519, 65497, 65479)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_module(path: Path, expected: str, name: str):
    if digest(path) != expected:
        fail(("module hash", str(path)))
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        fail(("module import", str(path)))
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module


def encode_fraction(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def decode_fraction(raw) -> Fraction:
    if not isinstance(raw, list) or len(raw) != 2:
        fail(("fraction encoding", raw))
    return Fraction(int(raw[0]), int(raw[1]))


def encode_monomial(monomial) -> list[list[object]]:
    return [[name, exponent] for name, exponent in monomial]


def decode_monomial(raw):
    return tuple((str(name), int(exponent)) for name, exponent in raw)


def merge_monomials(left, right):
    exponents = dict(left)
    for name, exponent in right:
        exponents[name] = exponents.get(name, 0) + exponent
    return tuple(sorted((name, exponent) for name, exponent in exponents.items() if exponent))


def add_scaled(target, source, scale: Fraction):
    if not scale:
        return
    for monomial, coefficient in source.items():
        value = target.get(monomial, Fraction(0)) + scale * coefficient
        if value:
            target[monomial] = value
        else:
            target.pop(monomial, None)


def multiply_monomial(polynomial, multiplier):
    return {merge_monomials(monomial, multiplier): coefficient for monomial, coefficient in polynomial.items()}


def load_rows():
    parser = load_module(PARSER, PARSER_SHA, "v37_parser")
    if digest(V23_RESULT) != V23_RESULT_SHA:
        fail("V23 result hash")
    v23_result = json.loads(V23_RESULT.read_text())
    rows = []; hashes = {}; by_grade = {grade: [] for grade in range(10, 20)}
    for grade in range(10, 16):
        for row in range(1, 8):
            name = f"Tg{grade}_{row}"; record = v23_result["records"][name]
            chart = record["charts"]["a1_ordered"]; path = V23 / "output_r1" / chart["output"]
            if digest(path) != chart["output_sha256"]:
                fail(("V23 row hash", name))
            polynomial = parser.specialize(parser.parse(path), frozenset({"rho"}), {})
            hashes[name] = digest(path)
            if polynomial:
                item = {"name": name, "grade": grade, "row": row, "polynomial": polynomial}
                rows.append(item); by_grade[grade].append(item)
    for grade, (directory, result_sha) in LATER.items():
        result_path = directory / "result.json"
        if digest(result_path) != result_sha:
            fail(("later result hash", grade))
        result = json.loads(result_path.read_text())
        for row in range(1, 8):
            name = f"Tg{grade}_{row}"; path = directory / Path(result["coefficient_paths"][name]).name
            if digest(path) != result["coefficient_sha256"][name]:
                fail(("later row hash", name))
            polynomial = parser.specialize(parser.parse(path), frozenset({"rho"}), {})
            hashes[name] = digest(path)
            if polynomial:
                item = {"name": name, "grade": grade, "row": row, "polynomial": polynomial}
                rows.append(item); by_grade[grade].append(item)
    if len(hashes) != 70 or len(rows) != 51:
        fail(("row census", len(hashes), len(rows)))
    for grade in range(10, 20):
        if len(by_grade[grade]) != ROW_COUNTS[grade] or sum(len(item["polynomial"]) for item in by_grade[grade]) != TERM_COUNTS[grade]:
            fail(("grade census", grade))
        for item in by_grade[grade]:
            for monomial in item["polynomial"]:
                if sum(parser.sigma_weight(name) * exponent for name, exponent in monomial) != grade:
                    fail(("homogeneity", item["name"], monomial))
                if any(name == "rho" for name, _ in monomial):
                    fail(("rho survived", item["name"]))
    variables = sorted({name for item in rows for monomial in item["polynomial"] for name, _ in monomial})
    if len(variables) != 65 or any(parser.sigma_weight(name) <= 0 for name in variables):
        fail(("variable census", len(variables)))
    return parser, rows, hashes, variables


def monomials_of_weight(variables, parser, weight: int):
    eligible = tuple((name, parser.sigma_weight(name)) for name in variables if parser.sigma_weight(name) <= weight)

    @lru_cache(maxsize=None)
    def recurse(index: int, remaining: int):
        if remaining == 0:
            return ((),)
        if index == len(eligible) or remaining < 0:
            return ()
        name, variable_weight = eligible[index]; answer = []
        for exponent in range(remaining // variable_weight + 1):
            prefix = () if exponent == 0 else ((name, exponent),)
            for tail in recurse(index + 1, remaining - exponent * variable_weight):
                answer.append(prefix + tail)
        return tuple(answer)

    return recurse(0, weight)


def build_products(weight: int, parser, rows, variables):
    products = []
    multiplier_cache = {}
    for item in rows:
        complement = weight - item["grade"]
        if complement < 0:
            continue
        multipliers = multiplier_cache.setdefault(complement, monomials_of_weight(variables, parser, complement))
        for multiplier in multipliers:
            polynomial = multiply_monomial(item["polynomial"], multiplier)
            products.append({"row": item["name"], "grade": item["grade"], "multiplier": multiplier,
                             "polynomial": polynomial})
    return products


def target_monomial(weight: int):
    return tuple(sorted((name, exponent) for name, exponent in TARGETS[weight].items()))


def target_component(products, target):
    incidence = {}
    for index, product in enumerate(products):
        for monomial in product["polynomial"]:
            incidence.setdefault(monomial, []).append(index)
    monomials = {target}; product_indices = set(); queue = deque((target,))
    while queue:
        monomial = queue.popleft()
        for index in incidence.get(monomial, ()):
            if index in product_indices:
                continue
            product_indices.add(index)
            for neighbor in products[index]["polynomial"]:
                if neighbor not in monomials:
                    monomials.add(neighbor); queue.append(neighbor)
    chosen = sorted(product_indices)
    return chosen, sorted(monomials)


def modular_value(value: Fraction, prime: int) -> int:
    if value.denominator % prime == 0:
        fail(("bad denominator prime", prime, value))
    return (value.numerator * pow(value.denominator, -1, prime)) % prime


def modular_skeleton(polynomials, monomials, prime: int):
    column = {monomial: index for index, monomial in enumerate(monomials)}
    basis = {}; selected = []; pivots = []
    for original_index, polynomial in enumerate(polynomials):
        vector = {column[monomial]: modular_value(coefficient, prime)
                  for monomial, coefficient in polynomial.items() if modular_value(coefficient, prime)}
        while vector:
            pivot = min(vector); coefficient = vector[pivot]
            if pivot not in basis:
                inverse = pow(coefficient, -1, prime)
                vector = {index: (value * inverse) % prime for index, value in vector.items() if (value * inverse) % prime}
                basis[pivot] = vector; selected.append(original_index); pivots.append(pivot)
                break
            old = basis[pivot]
            for index, value in old.items():
                new_value = (vector.get(index, 0) - coefficient * value) % prime
                if new_value:
                    vector[index] = new_value
                else:
                    vector.pop(index, None)
    return selected, pivots


def as_fraction(value) -> Fraction:
    return Fraction(int(value.p), int(value.q))


def exact_certificate(component_products, component_monomials, target, requested_prime: int):
    # Keep the optional heavy backend behind the registered-AWS guard in main().
    # This lets a local invocation fail closed before importing python-flint.
    from flint import fmpq, fmpq_mat

    if not component_products:
        return {"outcome": "nonmember", "selector_prime": requested_prime, "rank": 0,
                "functional": [{"monomial": encode_monomial(target), "coefficient": [1, 1]}]}
    prime_order = (requested_prime,) + tuple(prime for prime in SELECTOR_PRIMES if prime != requested_prime)
    last_error = None
    for prime in prime_order:
        selected, pivot_indices = modular_skeleton([item["polynomial"] for item in component_products], component_monomials, prime)
        rank = len(selected)
        pivot_monomials = [component_monomials[index] for index in pivot_indices]
        flat = []
        for row_index in selected:
            polynomial = component_products[row_index]["polynomial"]
            for monomial in pivot_monomials:
                value = polynomial.get(monomial, Fraction(0)); flat.append(fmpq(value.numerator, value.denominator))
        matrix = fmpq_mat(rank, rank, flat)
        if matrix.rank() != rank:
            last_error = ("exact pivot rank", prime, rank); continue
        rhs = fmpq_mat(rank, 1, [int(monomial == target) for monomial in pivot_monomials])
        coefficients = matrix.transpose().solve(rhs)
        coefficient_fractions = [as_fraction(coefficients[index, 0]) for index in range(rank)]
        residual = {target: Fraction(1)}
        for coefficient, row_index in zip(coefficient_fractions, selected):
            add_scaled(residual, component_products[row_index]["polynomial"], -coefficient)
        if not residual:
            terms = []
            for coefficient, row_index in zip(coefficient_fractions, selected):
                if coefficient:
                    product = component_products[row_index]
                    terms.append({"coefficient": encode_fraction(coefficient), "component_product_index": row_index,
                                  "row": product["row"], "grade": product["grade"],
                                  "multiplier": encode_monomial(product["multiplier"])})
            return {"outcome": "member", "selector_prime": prime, "rank": rank, "terms": terms}
        residual_monomial = min(residual, key=lambda monomial: (len(monomial), monomial))
        column_rhs = []
        for row_index in selected:
            value = -component_products[row_index]["polynomial"].get(residual_monomial, Fraction(0))
            column_rhs.append(fmpq(value.numerator, value.denominator))
        solution = matrix.solve(fmpq_mat(rank, 1, column_rhs))
        functional = {residual_monomial: Fraction(1)}
        for index, monomial in enumerate(pivot_monomials):
            value = functional.get(monomial, Fraction(0)) + as_fraction(solution[index, 0])
            if value: functional[monomial] = value
            else: functional.pop(monomial, None)
        scale = residual[residual_monomial]
        functional = {monomial: coefficient / scale for monomial, coefficient in functional.items() if coefficient}
        if evaluate_functional({target: Fraction(1)}, functional) != 1:
            last_error = ("target functional", prime); continue
        if any(evaluate_functional(product["polynomial"], functional) for product in component_products):
            last_error = ("component functional replay", prime); continue
        entries = [{"monomial": encode_monomial(monomial), "coefficient": encode_fraction(coefficient)}
                   for monomial, coefficient in sorted(functional.items())]
        return {"outcome": "nonmember", "selector_prime": prime, "rank": rank, "functional": entries}
    fail(("no exact certificate from selector primes", last_error))


def evaluate_functional(polynomial, functional):
    return sum(coefficient * functional.get(monomial, Fraction(0)) for monomial, coefficient in polynomial.items())


def replay_certificate(record, products, component_indices, target):
    component_products = [products[index] for index in component_indices]
    if record["outcome"] == "member":
        combination = {}
        for term in record["terms"]:
            index = int(term["component_product_index"])
            product = component_products[index]
            if (term["row"] != product["row"] or int(term["grade"]) != product["grade"]
                    or decode_monomial(term["multiplier"]) != product["multiplier"]):
                fail("membership metadata")
            add_scaled(combination, product["polynomial"], decode_fraction(term["coefficient"]))
        if combination != {target: Fraction(1)}:
            fail("membership replay")
    elif record["outcome"] == "nonmember":
        functional = {decode_monomial(entry["monomial"]): decode_fraction(entry["coefficient"])
                      for entry in record["functional"]}
        if evaluate_functional({target: Fraction(1)}, functional) != 1:
            fail("dual target")
        if any(evaluate_functional(product["polynomial"], functional) for product in products):
            fail("dual full-product replay")
    else:
        fail("unknown outcome")


def v27_control(parser, rows, variables):
    products = build_products(15, parser, rows, variables)
    functional = {
        (("a1", 3),): Fraction(1),
        tuple(sorted((("a1", 1), ("aa0", 1), ("rs2", 1)))): Fraction(-1, 3),
    }
    if evaluate_functional({(("a1", 3),): Fraction(1)}, functional) != 1:
        fail("V27 target control")
    if any(evaluate_functional(product["polynomial"], functional) for product in products):
        fail("V27 dual control")
    return len(products)


def main() -> None:
    cli = argparse.ArgumentParser(); cli.add_argument("output", type=Path)
    cli.add_argument("--selector-prime", type=int, choices=SELECTOR_PRIMES, required=True)
    args = cli.parse_args(); tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if (platform.system() != "Linux" or not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2"
            or not tag.startswith("max12_812_order2_p0_total_rees_j2_a1_graded_ladder_v37_")):
        fail("registered V37 AWS EC2 lane required")
    output = args.output.resolve(); output.mkdir(parents=True, exist_ok=False)
    parser, rows, row_hashes, variables = load_rows()
    control_products = v27_control(parser, rows, variables)
    results = {}
    for weight in sorted(TARGETS):
        products = build_products(weight, parser, rows, variables); target = target_monomial(weight)
        component_indices, component_monomials = target_component(products, target)
        component_products = [products[index] for index in component_indices]
        census = {"products": len(products), "support": len({target} | {monomial for item in products for monomial in item["polynomial"]}),
                  "component_products": len(component_products), "component_monomials": len(component_monomials),
                  "component_nnz": sum(len(item["polynomial"]) for item in component_products)}
        if census != EXPECTED[weight]:
            fail(("graded census", weight, census, EXPECTED[weight]))
        certificate = exact_certificate(component_products, component_monomials, target, args.selector_prime)
        replay_certificate(certificate, products, component_indices, target)
        if weight in (17, 18) and (certificate["outcome"] != "nonmember" or len(certificate["functional"]) != 1):
            fail(("isolated target control", weight))
        results[str(weight)] = {"target": encode_monomial(target), **census, **certificate,
                                "complete_through_weight": weight <= 19,
                                "implication": ("raw rho-zero D(a1*k) empty on membership" if weight < 20
                                                else "raw rho-zero D(a1) empty on membership")}
        print(f"V37_W{weight}={certificate['outcome']}")
    result = {
        "status": "PASS-A1-GRADED-LADDER-V37-COMPILER", "registered_aws_lane": tag,
        "selector_prime_requested": args.selector_prime, "preregistration_sha256": digest(PREREG),
        "row_count_named": len(row_hashes), "row_count_nonzero": len(rows), "variable_count": len(variables),
        "row_sha256": row_hashes, "v27_control_products": control_products, "results": results,
        "scope": "homogeneous raw ordered-a1 rho-zero row ideal through grade19; no saturated-Rees or Gate-T inference",
    }
    result_path = output / "result.json"; result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("PASS-A1-GRADED-LADDER-V37-COMPILER")
    print(f"RESULT_SHA256={digest(result_path)}")


if __name__ == "__main__":
    main()
