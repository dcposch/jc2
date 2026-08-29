#!/usr/bin/env python3
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
from math import gcd
import os
from pathlib import Path
import platform
import re


HERE = Path(__file__).resolve().parent
COMPILER = HERE / "solve_graded_ladder_v38.py"
COMPILER_SHA = "53bc61c80d4ff5818604503de8b40fadfd8ecc68cda301087a00a446eaf98987"
PREREG_SHA = "0aea56dc2804b210c521a308eda3d872e4bd6af7a8ad5d63887b34584c9b43b2"
COMPILER_STATUS = "PASS-A1-GRADED-LADDER-V38-COMPILER"
STATUS = "PASS-A1-GRADED-LADDER-V38"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def canonical_json(path: Path):
    raw = path.read_text()
    value = json.loads(raw, parse_constant=lambda token: fail(("JSON constant", token)))
    if raw != json.dumps(value, sort_keys=True, indent=2) + "\n":
        fail("noncanonical JSON")
    return value


def exact_dict(value, keys, label: str):
    if type(value) is not dict or set(value) != set(keys):
        fail((label, "keys", sorted(value) if type(value) is dict else type(value).__name__))
    return value


def exact_int(value, label: str) -> int:
    if type(value) is not int:
        fail((label, "integer"))
    return value


def exact_bool(value, label: str) -> bool:
    if type(value) is not bool:
        fail((label, "boolean"))
    return value


def exact_str(value, label: str) -> str:
    if type(value) is not str:
        fail((label, "string"))
    return value


def decode_fraction(raw, label: str) -> Fraction:
    if type(raw) is not list or len(raw) != 2:
        fail((label, "fraction pair"))
    numerator = exact_int(raw[0], f"{label}.numerator")
    denominator = exact_int(raw[1], f"{label}.denominator")
    if denominator <= 0 or gcd(abs(numerator), denominator) != 1:
        fail((label, "canonical reduced fraction"))
    return Fraction(numerator, denominator)


def decode_monomial(raw, label: str, allowed_variables=None):
    if type(raw) is not list:
        fail((label, "monomial list"))
    decoded = []
    for index, pair in enumerate(raw):
        if type(pair) is not list or len(pair) != 2:
            fail((label, "monomial pair", index))
        name = exact_str(pair[0], f"{label}[{index}].name")
        exponent = exact_int(pair[1], f"{label}[{index}].exponent")
        if exponent <= 0 or (allowed_variables is not None and name not in allowed_variables):
            fail((label, "monomial variable/exponent", name, exponent))
        decoded.append((name, exponent))
    answer = tuple(decoded)
    if answer != tuple(sorted(answer)) or len({name for name, _ in answer}) != len(answer):
        fail((label, "canonical monomial order"))
    return answer


def load_compiler():
    if digest(COMPILER) != COMPILER_SHA:
        fail("compiler hash")
    spec = importlib.util.spec_from_file_location("v38_exact_replay", COMPILER)
    if spec is None or spec.loader is None:
        fail("compiler import")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def parse_functional(raw, allowed_variables):
    if type(raw) is not list or not raw:
        fail("functional list")
    functional = {}
    ordered = []
    for index, entry in enumerate(raw):
        exact_dict(entry, {"monomial", "coefficient"}, f"functional[{index}]")
        monomial = decode_monomial(entry["monomial"], f"functional[{index}].monomial", allowed_variables)
        coefficient = decode_fraction(entry["coefficient"], f"functional[{index}].coefficient")
        if not coefficient or monomial in functional:
            fail(("functional zero/duplicate", index))
        functional[monomial] = coefficient
        ordered.append(monomial)
    if ordered != sorted(ordered):
        fail("functional order")
    return functional


def replay_member(raw, component_products, target, compiler, allowed_variables) -> None:
    if type(raw) is not list:
        fail("terms list")
    combination = {}
    seen_indices = set()
    for term_index, term in enumerate(raw):
        exact_dict(term, {"coefficient", "component_product_index", "row", "grade", "multiplier"},
                   f"terms[{term_index}]")
        index = exact_int(term["component_product_index"], f"terms[{term_index}].component_product_index")
        if index < 0 or index >= len(component_products) or index in seen_indices:
            fail(("term component index", index))
        seen_indices.add(index)
        product = component_products[index]
        if (exact_str(term["row"], f"terms[{term_index}].row") != product["row"]
                or exact_int(term["grade"], f"terms[{term_index}].grade") != product["grade"]
                or decode_monomial(term["multiplier"], f"terms[{term_index}].multiplier", allowed_variables)
                != product["multiplier"]):
            fail(("membership metadata", term_index))
        coefficient = decode_fraction(term["coefficient"], f"terms[{term_index}].coefficient")
        if not coefficient:
            fail(("zero membership coefficient", term_index))
        compiler.add_scaled(combination, product["polynomial"], coefficient)
    if combination != {target: Fraction(1)}:
        fail("membership full polynomial replay")


def stdout_contract(path: Path, result_sha: str, label: str, census, outcome: str, rank: int) -> None:
    lines = path.read_text().splitlines()
    required = (
        f"V38_CENSUS_{label}={census['component_products']}x{census['component_monomials']}",
        f"V38_TARGET={label}", f"V38_OUTCOME={outcome}", f"V38_EXACT_RANK={rank}",
        COMPILER_STATUS, f"RESULT_SHA256={result_sha}",
    )
    if any(lines.count(token) != 1 for token in required):
        fail("compiler stdout contract")
    if sum(line.startswith("RESULT_SHA256=") for line in lines) != 1:
        fail("compiler stdout result multiplicity")


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("--result", type=Path, required=True)
    cli.add_argument("--compiler-stdout", type=Path, required=True)
    cli.add_argument("--compiler-stderr", type=Path, required=True)
    cli.add_argument("--target-label", required=True)
    cli.add_argument("--selector-prime", type=int, required=True)
    cli.add_argument("--registered-lane", required=True)
    cli.add_argument("--output", type=Path, required=True)
    args = cli.parse_args()
    compiler = load_compiler()
    if args.target_label not in compiler.TARGETS or args.selector_prime not in compiler.SELECTOR_PRIMES:
        fail("CLI target/selector")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    match = compiler.LANE_RE.fullmatch(tag)
    if (platform.system() != "Linux" or not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2"
            or tag != args.registered_lane or match is None or int(match.group(1)) != args.selector_prime
            or match.group(2) != args.target_label):
        fail("registered V38 validator AWS EC2 lane required")
    result = canonical_json(args.result)
    top_keys = {
        "schema_version", "status", "registered_aws_lane", "selector_prime_requested", "target_label",
        "preregistration_sha256", "v37_compiler_sha256", "primary_census_sha256",
        "primary_validated_sha256", "control_census_sha256", "control_validated_sha256",
        "row_count_named", "row_count_nonzero", "variable_count", "row_sha256",
        "v27_control_products", "record", "scope",
    }
    exact_dict(result, top_keys, "result")
    if exact_int(result["schema_version"], "schema_version") != 1:
        fail("schema version")
    if exact_str(result["status"], "status") != COMPILER_STATUS:
        fail("status")
    if exact_str(result["registered_aws_lane"], "registered_aws_lane") != tag:
        fail("lane binding")
    if exact_int(result["selector_prime_requested"], "selector_prime_requested") != args.selector_prime:
        fail("selector request binding")
    if exact_str(result["target_label"], "target_label") != args.target_label:
        fail("target binding")
    exact_pins = {
        "preregistration_sha256": PREREG_SHA,
        "v37_compiler_sha256": compiler.V37_SHA,
        "primary_census_sha256": compiler.PRIMARY_CENSUS_SHA,
        "primary_validated_sha256": compiler.PRIMARY_VALIDATED_SHA,
        "control_census_sha256": compiler.CONTROL_CENSUS_SHA,
        "control_validated_sha256": compiler.CONTROL_VALIDATED_SHA,
    }
    for key, expected in exact_pins.items():
        if exact_str(result[key], key) != expected:
            fail(("provenance pin", key))
    if (exact_int(result["row_count_named"], "row_count_named") != 70
            or exact_int(result["row_count_nonzero"], "row_count_nonzero") != 51
            or exact_int(result["variable_count"], "variable_count") != 65
            or exact_int(result["v27_control_products"], "v27_control_products") != 53):
        fail("source/control counts")
    if exact_str(result["scope"], "scope") != compiler.SCOPE:
        fail("scope")
    expected_row_names = {f"Tg{grade}_{row}" for grade in range(10, 20) for row in range(1, 8)}
    row_sha = result["row_sha256"]
    if type(row_sha) is not dict or set(row_sha) != expected_row_names:
        fail("row hash keys")
    for name, value in row_sha.items():
        if type(value) is not str or re.fullmatch(r"[0-9a-f]{64}", value) is None:
            fail(("row hash", name))
    expected_censi = compiler.load_expected_censi()
    v37 = compiler.load_v37()
    parser, rows, replay_hashes, variables = v37.load_rows()
    if replay_hashes != row_sha or v37.v27_control(parser, rows, variables) != 53:
        fail("upstream exact replay")
    label = args.target_label
    target_data = compiler.TARGETS[label]
    target = compiler.target_monomial(label)
    products = v37.build_products(target_data["weight"], parser, rows, variables)
    component_indices, component_monomials = v37.target_component(products, target)
    component_products = [products[index] for index in component_indices]
    census = compiler.census_for_problem(products, component_indices, component_monomials, target)
    if census != expected_censi[label]:
        fail("census replay")
    record = result["record"]
    decision_common = {"selector_prime_used", "exact_rank", "basis_selected_component_indices",
                       "basis_pivot_monomials", "basis_nonbasis_replay_count", "outcome"}
    base_keys = {
        "label", "weight", "a1_exponent", "k_exponent", "target", *compiler.CENSUS_KEYS,
        "selector_prime_requested", "basis_selected_full_product_indices", "exact_span_complete",
        "isolated_one_coordinate_control", "fixed_weight_product_span_complete",
        "globally_final_nonmembership", "negative_scope", "membership_scope", "implication",
        "divisor_nonmembership_anchor", *decision_common,
    }
    if type(record) is not dict or record.get("outcome") not in ("member", "nonmember"):
        fail("record/outcome schema")
    certificate_key = "terms" if record["outcome"] == "member" else "functional"
    exact_dict(record, base_keys | {certificate_key}, "record")
    if (exact_str(record["label"], "record.label") != label
            or exact_int(record["weight"], "record.weight") != target_data["weight"]
            or exact_int(record["a1_exponent"], "record.a1_exponent") != target_data["a1_exponent"]
            or exact_int(record["k_exponent"], "record.k_exponent") != target_data["k_exponent"]
            or decode_monomial(record["target"], "record.target", set(variables)) != target):
        fail("record target metadata")
    for key in compiler.CENSUS_KEYS:
        if exact_int(record[key], f"record.{key}") != census[key]:
            fail(("record census", key))
    if exact_int(record["selector_prime_requested"], "record.selector_prime_requested") != args.selector_prime:
        fail("record selector request")
    if exact_str(record["outcome"], "record.outcome") not in ("member", "nonmember"):
        fail("record outcome")
    rank = exact_int(record["exact_rank"], "record.exact_rank")
    used_prime = exact_int(record["selector_prime_used"], "record.selector_prime_used")
    if rank < 0 or used_prime not in compiler.SELECTOR_PRIMES:
        fail("rank/selector values")
    selected = record["basis_selected_component_indices"]
    full_selected = record["basis_selected_full_product_indices"]
    pivots_raw = record["basis_pivot_monomials"]
    if type(selected) is not list or type(full_selected) is not list or type(pivots_raw) is not list:
        fail("selector lists")
    selected_values = [exact_int(value, "basis component index") for value in selected]
    full_values = [exact_int(value, "basis full index") for value in full_selected]
    if (len(selected_values) != rank or len(set(selected_values)) != rank
            or any(value < 0 or value >= len(component_products) for value in selected_values)
            or full_values != [component_indices[index] for index in selected_values]):
        fail("basis row selectors")
    allowed_variables = set(variables)
    pivot_values = [decode_monomial(raw, f"basis_pivot_monomials[{index}]", allowed_variables)
                    for index, raw in enumerate(pivots_raw)]
    if len(pivot_values) != rank or len(set(pivot_values)) != rank or any(value not in component_monomials for value in pivot_values):
        fail("basis pivot selectors")
    replay_count = exact_int(record["basis_nonbasis_replay_count"], "basis_nonbasis_replay_count")
    if replay_count != len(component_products) - rank:
        fail("basis replay count")
    if not exact_bool(record["exact_span_complete"], "exact_span_complete"):
        fail("exact span completeness")
    isolated = len(component_products) == 0
    if exact_bool(record["isolated_one_coordinate_control"], "isolated control") != isolated:
        fail("isolated control value")
    if label in ("i1_j3", "i2_j2") and not isolated:
        fail("W17/W18 one-coordinate census")
    expected_interpretation = compiler.interpretation(label)
    for key, expected in expected_interpretation.items():
        value = record[key]
        if type(expected) is bool:
            exact_bool(value, f"record.{key}")
        elif expected is None:
            if value is not None:
                fail(("record interpretation", key))
        else:
            exact_str(value, f"record.{key}")
        if value != expected:
            fail(("record interpretation", key))
    if target_data["weight"] >= 20 and record["negative_scope"] != "nonmembership only in the frozen row ideal through grade19":
        fail("W20-W25 negative scope")
    from flint import fmpq, fmpq_mat
    expected_decision = compiler.exact_basis_and_decision(component_products, component_monomials, target,
                                                          args.selector_prime, fmpq, fmpq_mat)
    for key, expected in expected_decision.items():
        if record[key] != expected:
            fail(("exact decision replay", key))
    if record["outcome"] == "member":
        replay_member(record["terms"], component_products, target, compiler, allowed_variables)
    else:
        functional = parse_functional(record["functional"], allowed_variables)
        if compiler.evaluate_functional({target: Fraction(1)}, functional) != 1:
            fail("dual target replay")
        if any(compiler.evaluate_functional(product["polynomial"], functional) for product in products):
            fail("dual full-product replay")
        if isolated and record["functional"] != [{"monomial": compiler.encode_monomial(target), "coefficient": [1, 1]}]:
            fail("isolated one-coordinate functional")
    result_sha = digest(args.result)
    stdout_contract(args.compiler_stdout, result_sha, label, census, record["outcome"], rank)
    stdout = args.compiler_stdout.read_text()
    stderr = args.compiler_stderr.read_text()
    if stderr.count("Command being timed:") != 1 or stderr.count("Exit status: 0") != 1:
        fail("resource contract")
    diagnostics = ("Traceback", "FAIL_", "Killed", "out of memory", "error occurred")
    if any(token in stdout or token in stderr for token in diagnostics):
        fail("diagnostic token")
    final = {
        "schema_version": 1,
        "status": STATUS,
        "registered_aws_lane": tag,
        "target_label": label,
        "selector_prime_requested": args.selector_prime,
        "selector_prime_used": used_prime,
        "outcome": record["outcome"],
        "exact_rank": rank,
        "negative_scope": record["negative_scope"],
        "membership_scope": record["membership_scope"],
        "result_sha256": result_sha,
        "compiler_sha256": COMPILER_SHA,
        "preregistration_sha256": PREREG_SHA,
        "primary_census_sha256": compiler.PRIMARY_CENSUS_SHA,
        "control_census_sha256": compiler.CONTROL_CENSUS_SHA,
        "compiler_stdout_sha256": digest(args.compiler_stdout),
        "compiler_stderr_sha256": digest(args.compiler_stderr),
        "scope": compiler.SCOPE,
    }
    args.output.write_text(json.dumps(final, sort_keys=True, indent=2) + "\n")
    print(STATUS)
    print(f"RESULT_SHA256={digest(args.output)}")


if __name__ == "__main__":
    main()
