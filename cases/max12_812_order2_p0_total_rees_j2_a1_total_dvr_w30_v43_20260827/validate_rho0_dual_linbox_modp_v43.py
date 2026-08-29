#!/usr/bin/env python3
"""Replay a finite-prime LinBox dual against the full rho=0 product set."""

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
PRIME = 65519


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def decode_monomial(record):
    return tuple((str(name), int(power)) for name, power in record)


def load_source():
    if digest(TOTAL_COMPILER) != TOTAL_COMPILER_SHA256:
        fail("total compiler hash")
    spec = importlib.util.spec_from_file_location("v43_rho0_dual_modp_source", TOTAL_COMPILER)
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
            or "_rho0dual_modp_" not in tag):
        fail("registered V43 rho0-dual mod-p AWS lane required")
    return tag


def residue(value: Fraction) -> int:
    if value.denominator % PRIME == 0:
        fail(("bad denominator", value))
    return value.numerator * pow(value.denominator, -1, PRIME) % PRIME


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("--compiler-result", type=Path, required=True)
    cli.add_argument("--solution", type=Path, required=True)
    cli.add_argument("--output", type=Path, required=True)
    args = cli.parse_args()
    tag = require_aws()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    compiler_path = args.compiler_result.resolve()
    compiler = json.loads(compiler_path.read_text())
    if compiler.get("status") != "PASS-A1-TOTAL-DVR-W30-V43-RHO0-DUAL-LINBOX-COMPILER":
        fail("compiler status")
    coordinates = [decode_monomial(record) for record in
                   json.loads(Path(compiler["coordinate_path"]).read_text())]
    lines = args.solution.read_text().splitlines()
    if (len(lines) != len(coordinates) + 4
            or lines[0] != "V43_RHO0_DUAL_LINBOX_MODP"
            or int(lines[1]) != PRIME or int(lines[2]) != len(coordinates)
            or lines[-1] != "PASS_A1_TOTAL_DVR_W30_V43_RHO0_DUAL_LINBOX_MODP"):
        fail("solution framing")
    values = [int(value) % PRIME for value in lines[3:-1]]
    functional = {TARGET: 1}
    functional.update({monomial: value for monomial, value in zip(coordinates, values) if value})

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
            or len(component_monomials) != compiler["component_monomials_including_target"]):
        fail("reconstruction census")
    for product in special_products:
        if sum(residue(coefficient) * functional.get(monomial, 0)
               for monomial, coefficient in product["polynomial"].items()) % PRIME:
            fail("full-product modular replay")
    target_index = next(index for index, product in enumerate(special_products)
                        if product["polynomial"].get(TARGET))
    if functional[TARGET] != 1:
        fail("target value")
    target_product = special_products[target_index]["polynomial"]
    original_target_residual = sum(
        residue(coefficient) * functional.get(monomial, 0)
        for monomial, coefficient in target_product.items()
    ) % PRIME
    if original_target_residual:
        fail("target product original replay")
    corrupted_target_residual = (original_target_residual + functional[TARGET]) % PRIME
    if not corrupted_target_residual:
        fail("corrupted target-row control was not detected")
    result = {
        "status": "PASS-A1-TOTAL-DVR-W30-V43-RHO0-DUAL-LINBOX-MODP-REPLAY",
        "registered_aws_lane": tag,
        "scope": "independent F65519 screen replayed against all frozen rho=0 weight-30 products",
        "evidence_tier": "finite-field-corroboration-only",
        "prime": PRIME,
        "compiler_result_sha256": digest(compiler_path),
        "solution_sha256": digest(args.solution),
        "functional_support": len(functional),
        "full_product_replay_count": len(special_products),
        "component_replay_count": len(component_indices),
        "corrupted_target_row_control": {
            "product_index": target_index,
            "mutation": "add one to the coefficient of a1^6",
            "original_residual_mod_prime": original_target_residual,
            "detected_residual_mod_prime": corrupted_target_residual,
        },
    }
    result_path = output / "result.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("PASS-A1-TOTAL-DVR-W30-V43-RHO0-DUAL-LINBOX-MODP-REPLAY")
    print(f"RESULT_SHA256={digest(result_path)}")


if __name__ == "__main__":
    main()
