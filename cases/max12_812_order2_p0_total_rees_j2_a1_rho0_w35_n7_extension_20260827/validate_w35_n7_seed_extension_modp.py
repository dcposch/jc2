#!/usr/bin/env python3
"""Full F_65519 replay of a weight-35/N=7 seeded extension screen."""

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
COMPILER = HERE / "compile_w35_n7_seed_extension.py"
COMPILER_SHA256 = "510d2c1923504daf88b774e4e9a89a655231da1858e69a5f73ee88374c1a2ac1"
TARGET = (("a1", 7),)
PRIME = 65519


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_compiler():
    if digest(COMPILER) != COMPILER_SHA256:
        fail(("compiler hash", digest(COMPILER), COMPILER_SHA256))
    spec = importlib.util.spec_from_file_location("w35_n7_modp_compiler", COMPILER)
    if spec is None or spec.loader is None:
        fail("compiler import")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def require_aws() -> str:
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if (platform.system() != "Linux" or not vendor.is_file()
            or vendor.read_text().strip() != "Amazon EC2"
            or not tag.startswith("max12_812_order2_p0_total_rees_j2_a1_rho0_w35_n7_")
            or "_extension_modp_" not in tag):
        fail("registered weight-35/N=7 mod-p extension AWS lane required")
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
    module = load_compiler()
    compiler_path = args.compiler_result.resolve()
    compiler = json.loads(compiler_path.read_text())
    if (compiler.get("status") != "PASS-A1-RHO0-W35-N7-SEED-EXTENSION-COMPILER"
            or compiler.get("phase") != "compile"):
        fail("compiler result contract")
    for key in ("matrix", "rhs", "coordinate"):
        path = Path(compiler[f"{key}_path"])
        if digest(path) != compiler[f"{key}_sha256"]:
            fail((key, "hash"))
    coordinates = [module.decode_monomial(record) for record in
                   json.loads(Path(compiler["coordinate_path"]).read_text())]
    lines = args.solution.read_text().splitlines()
    if (len(lines) != len(coordinates) + 4
            or lines[0] != "A1_RHO0_W35_N7_SEED_EXTENSION_MODP"
            or int(lines[1]) != PRIME or int(lines[2]) != len(coordinates)
            or lines[-1] != "PASS_A1_RHO0_W35_N7_SEED_EXTENSION_MODP"):
        fail("solution framing")
    values = [int(value) % PRIME for value in lines[3:-1]]

    source = module.load_module(module.TOTAL_SOURCE, module.TOTAL_SOURCE_SHA256,
                                "w35_n7_modp_total_source")
    functional6, compiler6 = module.load_n6_functional()
    (parser, v37, total_rows, frozen_hashes, total_hashes, variables,
     frozen_variables, general_only, nonzero_general) = source.reconstruct_rows()
    if (frozen_hashes != compiler.get("frozen_row_sha256")
            or total_hashes != compiler.get("total_t_row_sha256")
            or frozen_hashes != compiler6.get("frozen_row_sha256")
            or len(variables) != 66 or len(frozen_variables) != 65
            or general_only != ["ez9"] or nonzero_general != 59):
        fail("source reconstruction custody")
    products = module.build_rho0_products(source, v37, parser, total_rows, variables)
    component_indices, component_monomials = v37.target_component(products, TARGET)
    if (len(products) != compiler["census"]["all_rho0_products"]
            or len(component_indices) != compiler["census"]["target_component_products"]
            or len(component_monomials) != compiler["census"]["target_component_monomials"]):
        fail("reconstruction census")

    functional = {}
    for monomial in component_monomials:
        down = module.divide_a1(monomial)
        if down is not None and functional6.get(down):
            value = residue(functional6[down])
            if value:
                functional[monomial] = value
    for monomial, value in zip(coordinates, values):
        if value:
            functional[monomial] = value
        else:
            functional.pop(monomial, None)
    if functional.get(TARGET) != 1:
        fail("target normalization")
    for product in products:
        residual = sum(residue(coefficient) * functional.get(monomial, 0)
                       for monomial, coefficient in product["polynomial"].items()) % PRIME
        if residual:
            fail(("full product replay", product["row"], product["multiplier"], residual))
    target_product_index = next(index for index, product in enumerate(products)
                                if product["polynomial"].get(TARGET))
    corrupted_residual = functional[TARGET] % PRIME
    if corrupted_residual != 1:
        fail("corrupted target-row control")
    result = {
        "status": "PASS-A1-RHO0-W35-N7-SEED-EXTENSION-MODP-FULL-REPLAY",
        "registered_aws_lane": tag,
        "scope": "independent F_65519 extension screen with full weight-35 replay",
        "evidence_tier": "finite-field-corroboration-only",
        "prime": PRIME,
        "compiler_sha256": COMPILER_SHA256,
        "compiler_result_sha256": digest(compiler_path),
        "solution_sha256": digest(args.solution.resolve()),
        "functional_support": len(functional),
        "full_product_replay_count": len(products),
        "component_replay_count": len(component_indices),
        "corrupted_target_row_control": {
            "product_index": target_product_index,
            "mutation": "add one to the coefficient of a1^7",
            "detected_residual_mod_prime": corrupted_residual,
        },
    }
    result_path = output / "result.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("PASS-A1-RHO0-W35-N7-SEED-EXTENSION-MODP-FULL-REPLAY")
    print(f"RESULT_SHA256={digest(result_path)}")


if __name__ == "__main__":
    main()
