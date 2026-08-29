#!/usr/bin/env python3
"""Compile the seeded weight-35/N=7 rho-zero dual extension block.

The heavy product census is AWS-only.  This producer first tries to extend
the frozen exact N=6 Macaulay functional while keeping all values on
a1*R_30 fixed and solving only for monomials not divisible by a1.
"""

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
ROOT = HERE.parents[1]
V43 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_total_dvr_w30_v43_20260827"
TOTAL_SOURCE = V43 / "compile_total_dvr_w30_v43.py"
TOTAL_SOURCE_SHA256 = "0de6a2b279aeeab8c5a635c1d7658958f3f49f0f94f8473355d281cae9438b00"
N6_COMPILER_RESULT = V43 / "aws_r6d_rho0_dual_compiler_20260827T085739Z/compiled/compiler_result.json"
N6_COMPILER_RESULT_SHA256 = "25f580911a9203f9de2158b18773d6ed1d79440c5f4fb19e330a7c4f060f3b9a"
N6_RESULT = V43 / "aws_r6d_rho0_dual_exact_resume_20260827T091000Z/RESULT.json"
N6_RESULT_SHA256 = "d063cdefe7802b6ca040f4ae3a4d44c4973baec0481b1383ddf3ed22c34fdfff"
N6_CERTIFICATE = V43 / "aws_r6d_rho0_dual_exact_resume_20260827T091000Z/validated/rho0_dual_exact_certificate.json"
N6_CERTIFICATE_SHA256 = "6674abaac330754c35e7a8290b0a20c9a7745fd184bce14e8f87e52c4561a9da"
N6_REPORT = ROOT / "xmodel/max12-812-order2-p0-total-rees-j2-a1-w30-n6-rho0-dual-nonmembership-v43-sol-20260827.md"
N6_REPORT_SHA256 = "7345d4a8dda7afd9f45dd6b938a5ec0e15ff642e4809da5434ef35eb505f446d"
DELTA_REVIEW = ROOT / "xmodel/max12-812-order2-p0-total-rees-j2-a1-v43-compiler-postreview-delta-hostile-review-fable5-20260827.md"
DELTA_REVIEW_SHA256 = "ae8ecf1887a62afd873fc795d0eeec50ff0aac6e4954813931d09a34c8bfc31a"
CENSUS_ADDENDUM = V43 / "PREREGISTRATION_CENSUS_ADDENDUM.md"
CENSUS_ADDENDUM_SHA256 = "266dfb8962cbeb1af73d4f03947670148b71a00eebd5e2a91fce9c78b99bf658"
WEIGHT = 35
EXPONENT = 7
TARGET = (("a1", EXPONENT),)
TARGET6 = (("a1", 6),)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_module(path: Path, expected: str, name: str):
    actual = digest(path)
    if actual != expected:
        fail(("hash", str(path), actual, expected))
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        fail(("import", str(path)))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def require_aws(phase: str) -> str:
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    marker = "_preflight_" if phase == "preflight" else "_extension_"
    if (platform.system() != "Linux" or not vendor.is_file()
            or vendor.read_text().strip() != "Amazon EC2"
            or not tag.startswith("max12_812_order2_p0_total_rees_j2_a1_rho0_w35_n7_")
            or marker not in tag):
        fail("registered weight-35/N=7 AWS lane required")
    return tag


def decode_monomial(record):
    return tuple((str(name), int(exponent)) for name, exponent in record)


def encode_monomial(monomial):
    return [[name, exponent] for name, exponent in monomial]


def divide_a1(monomial):
    exponents = dict(monomial)
    power = exponents.get("a1", 0)
    if power <= 0:
        return None
    if power == 1:
        exponents.pop("a1")
    else:
        exponents["a1"] = power - 1
    return tuple(sorted((name, exponent) for name, exponent in exponents.items() if exponent))


def load_n6_functional():
    for path, expected in (
        (N6_COMPILER_RESULT, N6_COMPILER_RESULT_SHA256),
        (N6_RESULT, N6_RESULT_SHA256),
        (N6_CERTIFICATE, N6_CERTIFICATE_SHA256),
        (N6_REPORT, N6_REPORT_SHA256),
        (DELTA_REVIEW, DELTA_REVIEW_SHA256),
        (CENSUS_ADDENDUM, CENSUS_ADDENDUM_SHA256),
    ):
        if digest(path) != expected:
            fail(("custody", str(path), digest(path), expected))
    result = json.loads(N6_RESULT.read_text())
    if (result.get("status")
            != "PASS-A1-TOTAL-DVR-W30-V43-RHO0-DUAL-LINBOX-EXACT-REPLAY"
            or result.get("certificate_sha256") != N6_CERTIFICATE_SHA256):
        fail("N=6 result contract")
    certificate = json.loads(N6_CERTIFICATE.read_text())
    if certificate.get("outcome") != "nonmember":
        fail("N=6 certificate outcome")
    functional = {
        decode_monomial(item["monomial"]): Fraction(*map(int, item["coefficient"]))
        for item in certificate["functional"]
    }
    if functional.get(TARGET6) != 1 or len(functional) != 3395:
        fail(("N=6 functional census", len(functional), functional.get(TARGET6)))
    return functional, json.loads(N6_COMPILER_RESULT.read_text())


def build_rho0_products(source, v37, parser, total_rows, variables):
    rows = []
    for item in total_rows:
        polynomial = source.specialize_t0(item["polynomial"])
        if polynomial:
            rows.append({**{key: item[key] for key in ("name", "grade", "row")},
                         "polynomial": polynomial})
    multiplier_cache = {}
    products = []
    for item in rows:
        complement = WEIGHT - item["grade"]
        if complement < 0:
            continue
        multipliers = multiplier_cache.setdefault(
            complement, v37.monomials_of_weight(variables, parser, complement)
        )
        for multiplier in multipliers:
            polynomial = {
                v37.merge_monomials(monomial, multiplier): coefficient
                for monomial, coefficient in item["polynomial"].items()
            }
            products.append({
                "row": item["name"], "grade": item["grade"],
                "multiplier": multiplier, "polynomial": polynomial,
            })
    return products


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("output", type=Path)
    cli.add_argument("--phase", choices=("preflight", "compile"), required=True)
    args = cli.parse_args()
    tag = require_aws(args.phase)
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    source = load_module(TOTAL_SOURCE, TOTAL_SOURCE_SHA256, "w35_n7_total_source")
    functional6, compiler6 = load_n6_functional()
    (parser, v37, total_rows, frozen_hashes, total_hashes, variables,
     frozen_variables, general_only, nonzero_general) = source.reconstruct_rows()
    if (len(frozen_hashes) != 70 or nonzero_general != 59
            or len(variables) != 66 or len(frozen_variables) != 65
            or general_only != ["ez9"]
            or frozen_hashes != compiler6.get("frozen_row_sha256")
            or total_hashes != compiler6.get("total_t_row_sha256")):
        fail("literal source / N=6 bridge census")

    products = build_rho0_products(source, v37, parser, total_rows, variables)
    component_indices, component_monomials = v37.target_component(products, TARGET)
    component = [products[index] for index in component_indices]
    if TARGET not in component_monomials or not component:
        fail("empty N=7 target component")

    seed = {}
    for monomial in component_monomials:
        down = divide_a1(monomial)
        if down is not None and functional6.get(down):
            seed[monomial] = functional6[down]
    if seed.get(TARGET) != 1:
        fail("seed target normalization")

    b_total = sorted(monomial for monomial in component_monomials
                     if divide_a1(monomial) is None)
    extension_rows = []
    pullback_count = 0
    pullback_failures = []
    residual_equations = 0
    forced_without_b = []
    target_rows = 0
    for component_position, product in enumerate(component):
        polynomial = product["polynomial"]
        residual = sum(coefficient * seed.get(monomial, Fraction(0))
                       for monomial, coefficient in polynomial.items())
        b_coefficients = {monomial: coefficient for monomial, coefficient in polynomial.items()
                          if divide_a1(monomial) is None and coefficient}
        multiplier_a1 = dict(product["multiplier"]).get("a1", 0)
        if multiplier_a1:
            pullback_count += 1
            if residual or b_coefficients:
                pullback_failures.append(component_position)
        if polynomial.get(TARGET):
            target_rows += 1
        if residual:
            residual_equations += 1
        if not b_coefficients and residual:
            forced_without_b.append(component_position)
        if b_coefficients or residual:
            extension_rows.append({
                "component_position": component_position,
                "product": product,
                "coefficients": b_coefficients,
                "rhs": -residual,
            })
    if pullback_failures or not pullback_count or not target_rows:
        fail(("a1 pullback invariant", pullback_count, pullback_failures[:10], target_rows))
    b_active = sorted({monomial for row in extension_rows for monomial in row["coefficients"]})
    b_column = {monomial: index + 1 for index, monomial in enumerate(b_active)}
    nnz = sum(len(row["coefficients"]) for row in extension_rows)
    census = {
        "weight": WEIGHT,
        "exponent": EXPONENT,
        "all_rho0_products": len(products),
        "all_rho0_product_nnz": sum(len(product["polynomial"]) for product in products),
        "target_component_products": len(component),
        "target_component_monomials": len(component_monomials),
        "target_component_nnz": sum(len(product["polynomial"]) for product in component),
        "a1_divisible_component_monomials": len(component_monomials) - len(b_total),
        "nona1_component_monomials": len(b_total),
        "nona1_active_unknowns": len(b_active),
        "a1_pullback_products": pullback_count,
        "fixed_seed_residual_equations": residual_equations,
        "fixed_extension_equations": len(extension_rows),
        "fixed_extension_nnz": nnz,
        "forced_nonzero_rows_without_nona1_unknown": len(forced_without_b),
        "target_incident_products": target_rows,
        "estimated_sms_bytes_upper": 64 * nnz + 128 * len(extension_rows),
    }
    print("W35_N7_PREFLIGHT=" + json.dumps(census, sort_keys=True, separators=(",", ":")),
          flush=True)
    base_result = {
        "status": ("PASS-A1-RHO0-W35-N7-SEED-EXTENSION-PREFLIGHT"
                   if args.phase == "preflight"
                   else "PASS-A1-RHO0-W35-N7-SEED-EXTENSION-COMPILER"),
        "registered_aws_lane": tag,
        "phase": args.phase,
        "scope": ("full unrestricted frozen rho-zero weight-35 products; fixed pullback "
                  "of the exact N=6 functional and correction only on non-a1 monomials"),
        "total_source_sha256": TOTAL_SOURCE_SHA256,
        "n6_compiler_result_sha256": N6_COMPILER_RESULT_SHA256,
        "n6_result_sha256": N6_RESULT_SHA256,
        "n6_certificate_sha256": N6_CERTIFICATE_SHA256,
        "n6_report_sha256": N6_REPORT_SHA256,
        "delta_review_sha256": DELTA_REVIEW_SHA256,
        "census_addendum_sha256": CENSUS_ADDENDUM_SHA256,
        "frozen_row_sha256": frozen_hashes,
        "total_t_row_sha256": total_hashes,
        "census": census,
        "fixed_seed_forced_obstruction_positions": forced_without_b,
        "outcome_policy": ("a solved extension proves N=7 nonmembership; an inconsistent "
                           "fixed seed gives no N=7 verdict and triggers the correction block"),
    }
    if args.phase == "preflight" or forced_without_b:
        if forced_without_b:
            base_result["fixed_seed_status"] = "obstructed-before-solve"
        result_path = output / "result.json"
        result_path.write_text(json.dumps(base_result, sort_keys=True, indent=2) + "\n")
        print(base_result["status"])
        print(f"RESULT_SHA256={digest(result_path)}")
        return

    matrix_path = output / "w35_n7_fixed_seed_extension.sms"
    rhs_path = output / "w35_n7_fixed_seed_extension.rhs"
    coordinate_path = output / "w35_n7_nona1_unknown_monomials.json"
    with matrix_path.open("w") as matrix, rhs_path.open("w") as rhs:
        matrix.write(f"{len(extension_rows)} {len(b_active)} M\n")
        for row_index, row in enumerate(extension_rows, start=1):
            scale = row["rhs"].denominator
            for coefficient in row["coefficients"].values():
                scale = lcm(scale, coefficient.denominator)
            rhs.write(str(int(row["rhs"] * scale)) + "\n")
            for monomial, coefficient in sorted(row["coefficients"].items()):
                value = int(coefficient * scale)
                if not value:
                    fail("integer clearing produced zero")
                matrix.write(f"{row_index} {b_column[monomial]} {value}\n")
        matrix.write("0 0 0\n")
    coordinate_path.write_text(json.dumps(
        [encode_monomial(monomial) for monomial in b_active], separators=(",", ":")
    ) + "\n")
    base_result.update({
        "fixed_seed_status": "compiled-for-extension-solve",
        "matrix_path": str(matrix_path), "matrix_sha256": digest(matrix_path),
        "rhs_path": str(rhs_path), "rhs_sha256": digest(rhs_path),
        "coordinate_path": str(coordinate_path),
        "coordinate_sha256": digest(coordinate_path),
    })
    result_path = output / "compiler_result.json"
    result_path.write_text(json.dumps(base_result, sort_keys=True, indent=2) + "\n")
    print("PASS-A1-RHO0-W35-N7-SEED-EXTENSION-COMPILER")
    print(f"RESULT_SHA256={digest(result_path)}")


if __name__ == "__main__":
    main()
