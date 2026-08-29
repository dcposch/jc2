#!/usr/bin/env python3
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform
import re


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V37 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_graded_ladder_v37_20260827/solve_graded_ladder_v37.py"
V37_SHA = "ba034c8cebaa27c5630872b9cf06d152e4577170486ac34ad7f695ead871845b"
PREREG = HERE / "PREREGISTRATION.md"
PRIMARY_CENSUS = HERE / "aws_census_r6d/compiled/census.json"
PRIMARY_CENSUS_SHA = "322a5888dce90129947e1127fded85cf2aaa1ad3ee6111a37f4c1b7b06c0b148"
PRIMARY_VALIDATED = HERE / "aws_census_r6d/RESULT.json"
PRIMARY_VALIDATED_SHA = "327723cd3fe09c0219e95a163a02bbf3696b0bf51da941b93b55def310b06724"
CONTROL_CENSUS = HERE / "aws_control_census_box01/compiled/census.json"
CONTROL_CENSUS_SHA = "f52e8c714fd192294ca9b66514198f415568de9dd5656dd96d230921c1597591"
CONTROL_VALIDATED = HERE / "aws_control_census_box01/RESULT.json"
CONTROL_VALIDATED_SHA = "d4757e940a7df0b8d13a1e3731f31f6cb058238a811ae1ac7934101c7d1b00ca"
STATUS = "PASS-A1-GRADED-LADDER-V38-COMPILER"
SCOPE = "exact fixed-weight membership in homogeneous raw ordered-a1 rho-zero row ideal generated through grade19; no saturated-Rees, honest-chart, Gate-T, or JC2 inference"
SELECTOR_PRIMES = (65521, 65519, 65497, 65479)
LANE_RE = re.compile(r"max12_812_order2_p0_total_rees_j2_a1_graded_ladder_v38_[0-9]{8}T[0-9]{6}Z_q(65521|65519|65497|65479)_(i[1-5]_j[0-5])")
TARGETS = {
    f"i{i}_j{j}": {"weight": 5 * i + 4 * j, "a1_exponent": i, "k_exponent": j}
    for i in range(1, 6) for j in range(0, 6) if 5 * i + 4 * j <= 25
}
PRIMARY_LABELS = {
    "i1_j3": 17, "i2_j2": 18, "i3_j1": 19, "i4_j0": 20,
    "i1_j4": 21, "i2_j3": 22, "i3_j2": 23, "i4_j1": 24, "i5_j0": 25,
}
DIVISOR_ANCHORS = {
    "i1_j0": "i1_j3", "i1_j1": "i1_j3", "i1_j2": "i1_j3",
    "i2_j0": "i2_j2", "i2_j1": "i2_j2", "i3_j0": "i3_j1",
}
CENSUS_KEYS = ("products", "support", "component_products", "component_monomials", "component_nnz")


class BadSelectorPrime(RuntimeError):
    pass


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def canonical_json(path: Path):
    raw = path.read_text()
    value = json.loads(raw, parse_constant=lambda token: fail(("JSON constant", token)))
    if raw != json.dumps(value, sort_keys=True, indent=2) + "\n":
        fail(("noncanonical JSON", str(path)))
    return value


def exact_int(value, label: str) -> int:
    if type(value) is not int:
        fail((label, "integer"))
    return value


def load_v37():
    if digest(V37) != V37_SHA:
        fail("V37 compiler hash")
    spec = importlib.util.spec_from_file_location("v38_decision_v37", V37)
    if spec is None or spec.loader is None:
        fail("V37 compiler import")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def encode_fraction(value: Fraction) -> list[int]:
    if value.denominator <= 0:
        fail("fraction sign")
    return [value.numerator, value.denominator]


def encode_monomial(monomial) -> list[list[object]]:
    return [[name, exponent] for name, exponent in monomial]


def target_monomial(label: str):
    target = TARGETS[label]
    entries = [("a1", target["a1_exponent"])]
    if target["k_exponent"]:
        entries.append(("k", target["k_exponent"]))
    return tuple(sorted(entries))


def load_expected_censi():
    pins = ((PRIMARY_CENSUS, PRIMARY_CENSUS_SHA), (PRIMARY_VALIDATED, PRIMARY_VALIDATED_SHA),
            (CONTROL_CENSUS, CONTROL_CENSUS_SHA), (CONTROL_VALIDATED, CONTROL_VALIDATED_SHA))
    for path, expected_sha in pins:
        if digest(path) != expected_sha:
            fail(("census provenance hash", str(path)))
    primary = canonical_json(PRIMARY_CENSUS)
    primary_validated = canonical_json(PRIMARY_VALIDATED)
    control = canonical_json(CONTROL_CENSUS)
    control_validated = canonical_json(CONTROL_VALIDATED)
    if (primary.get("status") != "PASS-A1-GRADED-LADDER-V38-CENSUS-COMPILER"
            or primary_validated.get("status") != "PASS-A1-GRADED-LADDER-V38-CENSUS"
            or primary_validated.get("census_result_sha256") != PRIMARY_CENSUS_SHA
            or control.get("status") != "PASS-A1-GRADED-LADDER-V38-CONTROL-CENSUS-COMPILER"
            or control_validated.get("status") != "PASS-A1-GRADED-LADDER-V38-CONTROL-CENSUS"
            or control_validated.get("census_result_sha256") != CONTROL_CENSUS_SHA):
        fail("validated census contract")
    if type(control.get("censi")) is not dict or set(control["censi"]) != set(TARGETS):
        fail("control census labels")
    expected = {}
    for label, target in TARGETS.items():
        record = control["censi"][label]
        if type(record) is not dict or record.get("label") != label:
            fail(("control census record", label))
        if (exact_int(record.get("weight"), f"{label}.weight") != target["weight"]
                or exact_int(record.get("a1_exponent"), f"{label}.a1") != target["a1_exponent"]
                or exact_int(record.get("k_exponent"), f"{label}.k") != target["k_exponent"]
                or record.get("target") != encode_monomial(target_monomial(label))):
            fail(("control target metadata", label))
        expected[label] = {key: exact_int(record.get(key), f"{label}.{key}") for key in CENSUS_KEYS}
    for label, weight in PRIMARY_LABELS.items():
        record = primary.get("censi", {}).get(str(weight))
        if type(record) is not dict or record.get("target") != encode_monomial(target_monomial(label)):
            fail(("primary census target", label))
        if any(exact_int(record.get(key), f"primary.{label}.{key}") != expected[label][key] for key in CENSUS_KEYS):
            fail(("primary/control census disagreement", label))
    if primary_validated.get("censi") != primary.get("censi") or control_validated.get("censi") != control.get("censi"):
        fail("validated census replay mismatch")
    return expected


def modular_value(value: Fraction, prime: int) -> int:
    if value.denominator % prime == 0:
        raise BadSelectorPrime((prime, value.denominator))
    return (value.numerator * pow(value.denominator, -1, prime)) % prime


def modular_skeleton(polynomials, monomials, prime: int):
    column = {monomial: index for index, monomial in enumerate(monomials)}
    basis = {}
    selected = []
    pivots = []
    for original_index, polynomial in enumerate(polynomials):
        vector = {}
        for monomial, coefficient in polynomial.items():
            value = modular_value(coefficient, prime)
            if value:
                vector[column[monomial]] = value
        while vector:
            pivot = min(vector)
            coefficient = vector[pivot]
            if pivot not in basis:
                inverse = pow(coefficient, -1, prime)
                vector = {index: (value * inverse) % prime for index, value in vector.items()
                          if (value * inverse) % prime}
                basis[pivot] = vector
                selected.append(original_index)
                pivots.append(pivot)
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


def add_scaled(target, source, scale: Fraction) -> None:
    if not scale:
        return
    for monomial, coefficient in source.items():
        value = target.get(monomial, Fraction(0)) + scale * coefficient
        if value:
            target[monomial] = value
        else:
            target.pop(monomial, None)


def evaluate_functional(polynomial, functional) -> Fraction:
    return sum((coefficient * functional.get(monomial, Fraction(0))
                for monomial, coefficient in polynomial.items()), Fraction(0))


def exact_basis_and_decision(component_products, component_monomials, target, requested_prime: int,
                             fmpq, fmpq_mat):
    if not component_products:
        return {
            "selector_prime_used": requested_prime,
            "exact_rank": 0,
            "basis_selected_component_indices": [],
            "basis_pivot_monomials": [],
            "basis_nonbasis_replay_count": 0,
            "outcome": "nonmember",
            "functional": [{"monomial": encode_monomial(target), "coefficient": [1, 1]}],
        }
    polynomials = [item["polynomial"] for item in component_products]
    prime_order = (requested_prime,) + tuple(prime for prime in SELECTOR_PRIMES if prime != requested_prime)
    failures = []
    for prime in prime_order:
        try:
            selected, pivot_indices = modular_skeleton(polynomials, component_monomials, prime)
        except BadSelectorPrime as error:
            failures.append((prime, "denominator", str(error)))
            continue
        rank = len(selected)
        if rank == 0:
            failures.append((prime, "zero rank in nonempty component"))
            continue
        pivot_monomials = [component_monomials[index] for index in pivot_indices]
        flat = []
        for selected_index in selected:
            polynomial = polynomials[selected_index]
            for monomial in pivot_monomials:
                value = polynomial.get(monomial, Fraction(0))
                flat.append(fmpq(value.numerator, value.denominator))
        matrix = fmpq_mat(rank, rank, flat)
        if matrix.rank() != rank:
            failures.append((prime, "singular exact pivot minor", rank))
            continue
        selected_set = set(selected)
        nonbasis = [index for index in range(len(polynomials)) if index not in selected_set]
        rhs_columns = nonbasis + [None]
        rhs_flat = []
        for monomial in pivot_monomials:
            for index in rhs_columns:
                value = Fraction(int(monomial == target)) if index is None else polynomials[index].get(monomial, Fraction(0))
                rhs_flat.append(fmpq(value.numerator, value.denominator))
        rhs = fmpq_mat(rank, len(rhs_columns), rhs_flat)
        try:
            solutions = matrix.transpose().solve(rhs)
        except Exception as error:
            failures.append((prime, "exact solve", type(error).__name__))
            continue
        span_ok = True
        for column_index, product_index in enumerate(nonbasis):
            replay = {}
            for basis_index, selected_index in enumerate(selected):
                coefficient = as_fraction(solutions[basis_index, column_index])
                if coefficient:
                    add_scaled(replay, polynomials[selected_index], coefficient)
            if replay != polynomials[product_index]:
                span_ok = False
                failures.append((prime, "exact nonbasis replay", product_index))
                break
        if not span_ok:
            continue
        target_column = len(nonbasis)
        target_coefficients = [as_fraction(solutions[index, target_column]) for index in range(rank)]
        residual = {target: Fraction(1)}
        for coefficient, selected_index in zip(target_coefficients, selected):
            if coefficient:
                add_scaled(residual, polynomials[selected_index], -coefficient)
        base = {
            "selector_prime_used": prime,
            "exact_rank": rank,
            "basis_selected_component_indices": selected,
            "basis_pivot_monomials": [encode_monomial(monomial) for monomial in pivot_monomials],
            "basis_nonbasis_replay_count": len(nonbasis),
        }
        if not residual:
            terms = []
            for coefficient, selected_index in zip(target_coefficients, selected):
                if coefficient:
                    product = component_products[selected_index]
                    terms.append({
                        "coefficient": encode_fraction(coefficient),
                        "component_product_index": selected_index,
                        "row": product["row"],
                        "grade": product["grade"],
                        "multiplier": encode_monomial(product["multiplier"]),
                    })
            return {**base, "outcome": "member", "terms": terms}
        residual_monomial = min(residual, key=lambda monomial: (len(monomial), monomial))
        column_rhs = []
        for selected_index in selected:
            value = -polynomials[selected_index].get(residual_monomial, Fraction(0))
            column_rhs.append(fmpq(value.numerator, value.denominator))
        solution = matrix.solve(fmpq_mat(rank, 1, column_rhs))
        functional = {residual_monomial: Fraction(1)}
        for index, monomial in enumerate(pivot_monomials):
            value = functional.get(monomial, Fraction(0)) + as_fraction(solution[index, 0])
            if value:
                functional[monomial] = value
            else:
                functional.pop(monomial, None)
        scale = residual[residual_monomial]
        functional = {monomial: coefficient / scale for monomial, coefficient in functional.items() if coefficient}
        if evaluate_functional({target: Fraction(1)}, functional) != 1:
            failures.append((prime, "functional target"))
            continue
        if any(evaluate_functional(polynomial, functional) for polynomial in polynomials):
            failures.append((prime, "functional component replay"))
            continue
        entries = [{"monomial": encode_monomial(monomial), "coefficient": encode_fraction(coefficient)}
                   for monomial, coefficient in sorted(functional.items())]
        return {**base, "outcome": "nonmember", "functional": entries}
    fail(("no exact selector/certificate", failures))


def census_for_problem(products, component_indices, component_monomials, target):
    return {
        "products": len(products),
        "support": len({target} | {monomial for item in products for monomial in item["polynomial"]}),
        "component_products": len(component_indices),
        "component_monomials": len(component_monomials),
        "component_nnz": sum(len(products[index]["polynomial"]) for index in component_indices),
    }


def interpretation(label: str):
    target = TARGETS[label]
    weight = target["weight"]
    return {
        "fixed_weight_product_span_complete": True,
        "globally_final_nonmembership": weight <= 19,
        "negative_scope": ("fixed-weight final against all later positive-weight rows"
                           if weight <= 19 else "nonmembership only in the frozen row ideal through grade19"),
        "membership_scope": "membership is monotone and final under adjoining later rows",
        "implication": ("membership would empty the raw rho-zero locus on D(a1*k)"
                        if target["k_exponent"] else "membership would empty the raw rho-zero locus on D(a1)"),
        "divisor_nonmembership_anchor": DIVISOR_ANCHORS.get(label),
    }


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("output", type=Path)
    cli.add_argument("--target-label", choices=sorted(TARGETS), required=True)
    cli.add_argument("--selector-prime", type=int, choices=SELECTOR_PRIMES, required=True)
    cli.add_argument("--registered-lane", required=True)
    args = cli.parse_args()
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    match = LANE_RE.fullmatch(tag)
    if (platform.system() != "Linux" or not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2"
            or tag != args.registered_lane or match is None or int(match.group(1)) != args.selector_prime
            or match.group(2) != args.target_label):
        fail("registered V38 decision AWS EC2 lane required")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    from flint import fmpq, fmpq_mat
    expected = load_expected_censi()
    v37 = load_v37()
    parser, rows, row_hashes, variables = v37.load_rows()
    if len(row_hashes) != 70 or len(rows) != 51 or len(variables) != 65:
        fail("source census")
    if v37.v27_control(parser, rows, variables) != 53:
        fail("V27 exact dual control")
    label = args.target_label
    target_data = TARGETS[label]
    target = target_monomial(label)
    products = v37.build_products(target_data["weight"], parser, rows, variables)
    component_indices, component_monomials = v37.target_component(products, target)
    census = census_for_problem(products, component_indices, component_monomials, target)
    if census != expected[label]:
        fail(("preregistered census", label, census, expected[label]))
    print(f"V38_CENSUS_{label}={census['component_products']}x{census['component_monomials']}", flush=True)
    component_products = [products[index] for index in component_indices]
    decision = exact_basis_and_decision(component_products, component_monomials, target,
                                        args.selector_prime, fmpq, fmpq_mat)
    if decision["exact_rank"] + decision["basis_nonbasis_replay_count"] != len(component_products):
        fail("exact rank/span count")
    if len(decision["basis_selected_component_indices"]) != decision["exact_rank"]:
        fail("basis selector count")
    functional = decision.get("functional")
    isolated = len(component_products) == 0
    if isolated and (decision["outcome"] != "nonmember" or functional != [{"monomial": encode_monomial(target), "coefficient": [1, 1]}]):
        fail("isolated one-coordinate control")
    if label in ("i1_j3", "i2_j2") and not isolated:
        fail("W17/W18 isolation control")
    if decision["outcome"] == "nonmember":
        decoded = {tuple((pair[0], pair[1]) for pair in entry["monomial"]): Fraction(*entry["coefficient"])
                   for entry in decision["functional"]}
        if evaluate_functional({target: Fraction(1)}, decoded) != 1:
            fail("full dual target replay")
        if any(evaluate_functional(product["polynomial"], decoded) for product in products):
            fail("full dual product replay")
    record = {
        "label": label,
        "weight": target_data["weight"],
        "a1_exponent": target_data["a1_exponent"],
        "k_exponent": target_data["k_exponent"],
        "target": encode_monomial(target),
        **census,
        "selector_prime_requested": args.selector_prime,
        "basis_selected_full_product_indices": [component_indices[index] for index in decision["basis_selected_component_indices"]],
        "exact_span_complete": True,
        "isolated_one_coordinate_control": isolated,
        **decision,
        **interpretation(label),
    }
    result = {
        "schema_version": 1,
        "status": STATUS,
        "registered_aws_lane": tag,
        "selector_prime_requested": args.selector_prime,
        "target_label": label,
        "preregistration_sha256": digest(PREREG),
        "v37_compiler_sha256": V37_SHA,
        "primary_census_sha256": PRIMARY_CENSUS_SHA,
        "primary_validated_sha256": PRIMARY_VALIDATED_SHA,
        "control_census_sha256": CONTROL_CENSUS_SHA,
        "control_validated_sha256": CONTROL_VALIDATED_SHA,
        "row_count_named": len(row_hashes),
        "row_count_nonzero": len(rows),
        "variable_count": len(variables),
        "row_sha256": row_hashes,
        "v27_control_products": 53,
        "record": record,
        "scope": SCOPE,
    }
    result_path = output / "result.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(f"V38_TARGET={label}")
    print(f"V38_OUTCOME={decision['outcome']}")
    print(f"V38_EXACT_RANK={decision['exact_rank']}")
    print(STATUS)
    print(f"RESULT_SHA256={digest(result_path)}")


if __name__ == "__main__":
    main()
