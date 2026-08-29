#!/usr/bin/env python3
"""Compile the full weight-30 rho=0 dual system for an exact LinBox solve."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
from math import lcm
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


def encode_monomial(monomial) -> list[list[object]]:
    return [[name, exponent] for name, exponent in monomial]


def load_source():
    actual = digest(TOTAL_COMPILER)
    if actual != TOTAL_COMPILER_SHA256:
        fail(("total compiler hash", actual, TOTAL_COMPILER_SHA256))
    spec = importlib.util.spec_from_file_location("v43_rho0_dual_source", TOTAL_COMPILER)
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
        fail("registered V43 rho0-dual exact compiler AWS lane required")
    return tag


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("output", type=Path)
    args = cli.parse_args()
    tag = require_aws()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
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
    component = [special_products[index] for index in component_indices]
    unknown_monomials = [monomial for monomial in component_monomials if monomial != TARGET]
    column = {monomial: index + 1 for index, monomial in enumerate(unknown_monomials)}
    matrix_path = output / "rho0_dual_full_component.sms"
    rhs_path = output / "rho0_dual_full_component.rhs"
    coordinate_path = output / "rho0_dual_unknown_monomials.json"
    nnz = 0
    target_rows = 0
    with matrix_path.open("w") as matrix, rhs_path.open("w") as rhs:
        matrix.write(f"{len(component)} {len(unknown_monomials)} M\n")
        for row_index, product in enumerate(component, start=1):
            polynomial = product["polynomial"]
            scale = 1
            for coefficient in polynomial.values():
                scale = lcm(scale, coefficient.denominator)
            target_coefficient = polynomial.get(TARGET, Fraction(0))
            if target_coefficient:
                target_rows += 1
            rhs.write(str(int(-target_coefficient * scale)) + "\n")
            for monomial, coefficient in sorted(polynomial.items()):
                if monomial == TARGET or not coefficient:
                    continue
                value = int(coefficient * scale)
                if not value:
                    fail("integer clearing produced zero")
                matrix.write(f"{row_index} {column[monomial]} {value}\n")
                nnz += 1
        matrix.write("0 0 0\n")
    coordinate_path.write_text(json.dumps(
        [encode_monomial(monomial) for monomial in unknown_monomials],
        separators=(",", ":"),
    ) + "\n")
    if (len(frozen_hashes) != 70 or nonzero_general != 59
            or len(variables) != 66 or len(frozen_variables) != 65
            or general_only != ["ez9"] or len(special_products) != 284766
            or len(component) != 26200 or len(component_monomials) != 66076
            or len(unknown_monomials) != 66075 or target_rows != 1 or nnz != 616678):
        fail(("rho0 dual census", len(special_products), len(component),
              len(component_monomials), len(unknown_monomials), target_rows, nnz))
    result = {
        "status": "PASS-A1-TOTAL-DVR-W30-V43-RHO0-DUAL-LINBOX-COMPILER",
        "registered_aws_lane": tag,
        "scope": "full frozen rho=0 weight-30 target component, dual equations with lambda(a1^6)=1",
        "total_compiler_sha256": TOTAL_COMPILER_SHA256,
        "frozen_row_sha256": frozen_hashes,
        "total_t_row_sha256": total_hashes,
        "all_rho0_products": len(special_products),
        "component_equations": len(component),
        "component_monomials_including_target": len(component_monomials),
        "unknowns_excluding_target": len(unknown_monomials),
        "matrix_nnz": nnz,
        "target_incident_equations": target_rows,
        "matrix_path": str(matrix_path),
        "matrix_sha256": digest(matrix_path),
        "rhs_path": str(rhs_path),
        "rhs_sha256": digest(rhs_path),
        "coordinate_path": str(coordinate_path),
        "coordinate_sha256": digest(coordinate_path),
    }
    result_path = output / "compiler_result.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("PASS-A1-TOTAL-DVR-W30-V43-RHO0-DUAL-LINBOX-COMPILER")
    print(f"RESULT_SHA256={digest(result_path)}")


if __name__ == "__main__":
    main()
