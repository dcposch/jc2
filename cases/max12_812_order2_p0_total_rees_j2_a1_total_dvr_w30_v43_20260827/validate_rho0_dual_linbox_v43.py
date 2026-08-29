#!/usr/bin/env python3
"""Replay a LinBox rho=0 dual solution over Q against every source product."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
TOTAL_COMPILER = HERE / "compile_total_dvr_w30_v43.py"
TOTAL_COMPILER_SHA256 = "0de6a2b279aeeab8c5a635c1d7658958f3f49f0f94f8473355d281cae9438b00"
TARGET = (("a1", 6),)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def decode_monomial(record):
    return tuple((str(name), int(exponent)) for name, exponent in record)


def encode_monomial(monomial):
    return [[name, exponent] for name, exponent in monomial]


def encode_fraction(value: Fraction):
    return [value.numerator, value.denominator]


def load_source():
    actual = digest(TOTAL_COMPILER)
    if actual != TOTAL_COMPILER_SHA256:
        fail(("total compiler hash", actual, TOTAL_COMPILER_SHA256))
    spec = importlib.util.spec_from_file_location("v43_rho0_dual_validator_source", TOTAL_COMPILER)
    if spec is None or spec.loader is None:
        fail("total compiler import")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def require_aws() -> str:
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if (platform.system() != "Linux" or not vendor.is_file()
            or vendor.read_text().strip() != "Amazon EC2"
            or not tag.startswith("max12_812_order2_p0_total_rees_j2_a1_total_dvr_w30_v43_")
            or "_rho0dual_exact_" not in tag):
        fail("registered V43 rho0-dual exact validator AWS lane required")
    return tag


def read_solution(path: Path, expected: int):
    lines = path.read_text().splitlines()
    if (len(lines) != expected + 4 or lines[0] != "V43_RHO0_DUAL_LINBOX_EXACT"
            or lines[-1] != "PASS_A1_TOTAL_DVR_W30_V43_RHO0_DUAL_LINBOX"):
        fail("LinBox solution framing")
    denominator = int(lines[1])
    count = int(lines[2])
    if denominator == 0 or count != expected:
        fail(("LinBox solution dimensions", denominator, count, expected))
    return denominator, [int(value) for value in lines[3:-1]]


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("--compiler-result", type=Path, required=True)
    cli.add_argument("--solution", type=Path, required=True)
    cli.add_argument("--output", type=Path, required=True)
    args = cli.parse_args()
    tag = require_aws()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    compiler_result_path = args.compiler_result.resolve()
    solution_path = args.solution.resolve()
    compiler = json.loads(compiler_result_path.read_text())
    if compiler.get("status") != "PASS-A1-TOTAL-DVR-W30-V43-RHO0-DUAL-LINBOX-COMPILER":
        fail("compiler status")
    for key in ("matrix", "rhs", "coordinate"):
        path = Path(compiler[f"{key}_path"])
        if digest(path) != compiler[f"{key}_sha256"]:
            fail((key, "hash"))
    coordinates = [decode_monomial(record) for record in
                   json.loads(Path(compiler["coordinate_path"]).read_text())]
    if TARGET in coordinates or len(coordinates) != compiler["unknowns_excluding_target"]:
        fail("coordinate census")
    denominator, numerators = read_solution(solution_path, len(coordinates))
    functional = {TARGET: Fraction(1)}
    for monomial, numerator in zip(coordinates, numerators):
        value = Fraction(numerator, denominator)
        if value:
            functional[monomial] = value

    source = load_source()
    (parser, v37, total_rows, frozen_hashes, total_hashes, variables,
     frozen_variables, general_only, nonzero_general) = source.reconstruct_rows()
    products = source.build_products(v37, parser, total_rows, variables)
    special_products = []
    for product in products:
        polynomial = source.specialize_t0(product["polynomial"])
        if polynomial:
            special_products.append({
                **{key: product[key] for key in ("row", "grade", "multiplier")},
                "polynomial": polynomial,
            })
    component_indices, component_monomials = v37.target_component(special_products, TARGET)
    if (len(special_products) != compiler["all_rho0_products"]
            or len(component_indices) != compiler["component_equations"]
            or len(component_monomials) != compiler["component_monomials_including_target"]
            or frozen_hashes != compiler["frozen_row_sha256"]
            or total_hashes != compiler["total_t_row_sha256"]):
        fail("reconstruction census/custody")
    certificate = {
        "outcome": "nonmember",
        "functional": [
            {"monomial": encode_monomial(monomial), "coefficient": encode_fraction(value)}
            for monomial, value in sorted(functional.items())
        ],
    }
    v37.replay_certificate(certificate, special_products, component_indices, TARGET)

    target_product_index = next(
        index for index, product in enumerate(special_products)
        if product["polynomial"].get(TARGET)
    )
    original_residual = v37.evaluate_functional(
        special_products[target_product_index]["polynomial"], functional)
    corrupted = dict(special_products[target_product_index]["polynomial"])
    corrupted[TARGET] = corrupted.get(TARGET, Fraction(0)) + 1
    corrupted_residual = v37.evaluate_functional(corrupted, functional)
    if original_residual != 0 or corrupted_residual != 1:
        fail(("corrupted-row control", original_residual, corrupted_residual))

    certificate_path = output / "rho0_dual_exact_certificate.json"
    certificate_path.write_text(json.dumps(certificate, sort_keys=True,
                                           separators=(",", ":")) + "\n")
    result = {
        "status": "PASS-A1-TOTAL-DVR-W30-V43-RHO0-DUAL-LINBOX-EXACT-REPLAY",
        "registered_aws_lane": tag,
        "scope": "exact Q dual replay against all 284,766 frozen rho=0 weight-30 products",
        "implication": "a1^6 is not in the frozen rho=0 ideal; therefore no exponent-six total-rho DVR certificate exists",
        "total_compiler_sha256": TOTAL_COMPILER_SHA256,
        "compiler_result_sha256": digest(compiler_result_path),
        "solution_sha256": digest(solution_path),
        "solution_denominator": denominator,
        "functional_support": len(functional),
        "functional_non_target_support": len(functional) - 1,
        "full_product_replay_count": len(special_products),
        "component_replay_count": len(component_indices),
        "target_value": [1, 1],
        "corrupted_row_control": {
            "product_index": target_product_index,
            "row": special_products[target_product_index]["row"],
            "grade": special_products[target_product_index]["grade"],
            "changed_monomial": encode_monomial(TARGET),
            "changed_coefficient_by": [1, 1],
            "detected_residual": [1, 1],
        },
        "certificate_path": str(certificate_path),
        "certificate_sha256": digest(certificate_path),
    }
    result_path = output / "result.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("PASS-A1-TOTAL-DVR-W30-V43-RHO0-DUAL-LINBOX-EXACT-REPLAY")
    print(f"RESULT_SHA256={digest(result_path)}")


if __name__ == "__main__":
    main()
