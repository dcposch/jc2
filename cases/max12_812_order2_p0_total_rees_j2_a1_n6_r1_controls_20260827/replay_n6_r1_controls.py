#!/usr/bin/env python3
"""Additive exact controls for the frozen V43 N=6 dual certificate."""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform
import subprocess
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASE = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_total_dvr_w30_v43_20260827"
V43 = BASE / "compile_total_dvr_w30_v43.py"
V43_SHA256 = "0de6a2b279aeeab8c5a635c1d7658958f3f49f0f94f8473355d281cae9438b00"
V42 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_radical_cascade_closure_v42_20260827/replay_a1_cascade_closure_v42.py"
V42_SHA256 = "f4ec72933793bf08aabc600df7cdcd47b8de2c54f45c0d30341e13ac0b676459"
COMPILER_RESULT = BASE / "aws_r6d_rho0_dual_compiler_20260827T085739Z/compiled/compiler_result.json"
COMPILER_RESULT_SHA256 = "25f580911a9203f9de2158b18773d6ed1d79440c5f4fb19e330a7c4f060f3b9a"
COORDINATES = BASE / "aws_r6d_rho0_dual_compiler_20260827T085739Z/compiled/rho0_dual_unknown_monomials.json"
COORDINATES_SHA256 = "afa0192510f66c6a648f32f5ea898a4d23a8e032e0e34265f1861ab15bf84460"
SOLUTION = BASE / "aws_r6d_rho0_dual_exact_resume_20260827T091000Z/rho0_dual_exact.solution"
SOLUTION_SHA256 = "d0c04857c1b58d6bc8671eada4f8a7d2001c945be2a13d08ebde2fd53b4cf713"
CENSUS_ADDENDUM = BASE / "PREREGISTRATION_CENSUS_ADDENDUM.md"
CENSUS_ADDENDUM_SHA256 = "266dfb8962cbeb1af73d4f03947670148b71a00eebd5e2a91fce9c78b99bf658"
RECOVERY = BASE / "compiler_source_manifest_recovery_20260827T102800Z"
RECOVERED_MANIFEST = RECOVERY / "SOURCE_MANIFEST.sha256"
RECOVERED_MANIFEST_SHA256 = "033213c1d59bd77b6a4d7bd68faf714a4a62db16515b02a58d4f6e2c9c080a25"
RECOVERED_SNAPSHOT = RECOVERY / "source_snapshot.tar.gz"
RECOVERED_SNAPSHOT_SHA256 = "2d7f396a9d63957fe2597b64bb7af1bd03acd726504bef6cce1646916fa7c187"
MANIFEST_CHECK = RECOVERY / "manifest_check.stdout"
MANIFEST_CHECK_SHA256 = "e39526413b9d0fe15ee4ae2e4389386c9ca0a22cb8e92f193275d0c28b90cd55"
FAILED_LANES = BASE / "aws_r6d_rho0_dual_compiler_20260827T085739Z/run/lanes.log"
FAILED_LANES_SHA256 = "022e9d1234c41af7219009dd53e6c6f5b9d6ee3b278d32c6a763fa624bf48758"
FAILED_BUILD = BASE / "aws_r6d_rho0_dual_compiler_20260827T085739Z/run/max12_812_order2_p0_total_rees_j2_a1_total_dvr_w30_v43_rho0dual_exact_linbox_20260827T085739Z_r6d_build.stderr"
FAILED_BUILD_SHA256 = "6a60b6fb5de82ff3f1261c8a2e0b7a00f9a1145229a2f506e81e90eb54d0184b"
MUTATION_RECORDS_SHA256 = "a9649ec4df7dded55e30600c7eebbc06631978bb5b02c836151a1cd123521398"
TARGET = (("a1", 6),)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if (
        platform.system() != "Linux"
        or not vendor.is_file()
        or vendor.read_text().strip() != "Amazon EC2"
        or not tag.startswith("max12_812_order2_p0_total_rees_j2_a1_n6_r1_controls_")
    ):
        fail("registered N6-R1 AWS lane required")
    return tag


def load_v43():
    if digest(V43) != V43_SHA256:
        fail(("V43 hash", digest(V43), V43_SHA256))
    spec = importlib.util.spec_from_file_location("n6_r1_v43", V43)
    if spec is None or spec.loader is None:
        fail("V43 import")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def decode_monomial(raw):
    return tuple((str(name), int(exponent)) for name, exponent in raw)


def encode_monomial(monomial):
    return [[name, exponent] for name, exponent in monomial]


def read_solution(expected: int):
    lines = SOLUTION.read_text().splitlines()
    if (
        len(lines) != expected + 4
        or lines[0] != "V43_RHO0_DUAL_LINBOX_EXACT"
        or lines[-1] != "PASS_A1_TOTAL_DVR_W30_V43_RHO0_DUAL_LINBOX"
    ):
        fail("solution framing")
    denominator = int(lines[1])
    count = int(lines[2])
    if denominator == 0 or count != expected:
        fail(("solution dimensions", denominator, count, expected))
    return denominator, [int(value) for value in lines[3:-1]]


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: replay_n6_r1_controls.py OUTPUT")
    tag = require_aws()
    output = Path(sys.argv[1]).resolve()
    output.mkdir(parents=True, exist_ok=False)
    for path, expected in (
        (V42, V42_SHA256),
        (COMPILER_RESULT, COMPILER_RESULT_SHA256),
        (COORDINATES, COORDINATES_SHA256),
        (SOLUTION, SOLUTION_SHA256),
        (CENSUS_ADDENDUM, CENSUS_ADDENDUM_SHA256),
        (RECOVERED_MANIFEST, RECOVERED_MANIFEST_SHA256),
        (RECOVERED_SNAPSHOT, RECOVERED_SNAPSHOT_SHA256),
        (MANIFEST_CHECK, MANIFEST_CHECK_SHA256),
        (FAILED_LANES, FAILED_LANES_SHA256),
        (FAILED_BUILD, FAILED_BUILD_SHA256),
    ):
        if digest(path) != expected:
            fail(("custody hash", str(path), digest(path), expected))

    manifest_lines = RECOVERED_MANIFEST.read_text().splitlines()
    check_lines = MANIFEST_CHECK.read_text().splitlines()
    if len(manifest_lines) != 834 or len(check_lines) != 834 or any(
        not line.endswith(": OK") for line in check_lines
    ):
        fail("recovered compiler source manifest")
    failed_lanes = FAILED_LANES.read_text()
    failed_build = FAILED_BUILD.read_text()
    if (
        failed_lanes.count(" rc=1") != 1
        or "_r6d_build rc=1" not in failed_lanes
        or "undefined reference to `Givaro::Integer" not in failed_build
    ):
        fail("first-link failure disclosure")

    v42_run = subprocess.run(
        [sys.executable, str(V42)], check=True, capture_output=True, text=True
    )
    v42_result = json.loads(v42_run.stdout)
    if (
        v42_result.get("status") != "PASS-ORDERED-A1-RHO0-RAW-D-A1-EMPTY-THROUGH-G19"
        or v42_result.get("mutation", {}).get("row") != "Tg19_7"
        or int(v42_result["mutation"]["residual_term_count"]) <= 0
    ):
        fail("V42 control")
    mutation_monomial = decode_monomial(v42_result["mutation"]["monomial"])
    (output / "v42_replay_result.json").write_text(
        json.dumps(v42_result, sort_keys=True, indent=2) + "\n"
    )

    compiler = json.loads(COMPILER_RESULT.read_text())
    coordinates = [decode_monomial(raw) for raw in json.loads(COORDINATES.read_text())]
    if (
        compiler.get("status") != "PASS-A1-TOTAL-DVR-W30-V43-RHO0-DUAL-LINBOX-COMPILER"
        or len(coordinates) != 66075
        or TARGET in coordinates
    ):
        fail("frozen N6 compiler census")
    denominator, numerators = read_solution(len(coordinates))
    functional = {TARGET: Fraction(1)}
    for monomial, numerator in zip(coordinates, numerators):
        if numerator:
            functional[monomial] = Fraction(numerator, denominator)

    source = load_v43()
    (parser, v37, total_rows, frozen_hashes, total_hashes, variables,
     frozen_variables, general_only, nonzero_general) = source.reconstruct_rows()
    if (
        frozen_hashes != compiler["frozen_row_sha256"]
        or total_hashes != compiler["total_t_row_sha256"]
        or len(variables) != 66
        or len(frozen_variables) != 65
        or general_only != ["ez9"]
        or nonzero_general != 59
    ):
        fail("literal V43 reconstruction")
    row_record = next(item for item in total_rows if item["name"] == "Tg19_7")
    row = source.specialize_t0(row_record["polynomial"])
    if row_record["grade"] != 19 or mutation_monomial not in row:
        fail(("Tg19_7 mutation source", mutation_monomial))
    mutated_row = dict(row)
    mutated_row[mutation_monomial] += 1
    multipliers = v37.monomials_of_weight(variables, parser, 11)
    if len(multipliers) != 607:
        fail(("weight-11 multiplier census", len(multipliers)))

    mutation_records = []
    for index, multiplier in enumerate(multipliers):
        original = v37.multiply_monomial(row, multiplier)
        if v37.evaluate_functional(original, functional) != 0:
            fail(("original Tg19_7 product residual", index))
        mutated = v37.multiply_monomial(mutated_row, multiplier)
        residual = v37.evaluate_functional(mutated, functional)
        if residual:
            mutation_records.append({
                "index": index,
                "multiplier": encode_monomial(multiplier),
                "residual": [residual.numerator, residual.denominator],
            })
    mutation_bytes = json.dumps(
        mutation_records, sort_keys=True, separators=(",", ":")
    ).encode()
    mutation_sha = sha256(mutation_bytes).hexdigest()
    if len(mutation_records) != 6 or mutation_sha != MUTATION_RECORDS_SHA256:
        fail(("row-data mutation control", len(mutation_records), mutation_sha))
    mutation_path = output / "tg19_7_row_mutation_residuals.json"
    mutation_path.write_bytes(mutation_bytes + b"\n")

    result = {
        "schema_version": 1,
        "status": "PASS-A1-N6-R1-ADDITIVE-CONTROLS",
        "registered_aws_lane": tag,
        "scope": "additive custody, V42, and genuine Tg19_7 row-data mutation replay for frozen exact N6 functional",
        "v43_sha256": V43_SHA256,
        "v42_sha256": V42_SHA256,
        "compiler_result_sha256": COMPILER_RESULT_SHA256,
        "coordinate_sha256": COORDINATES_SHA256,
        "solution_sha256": SOLUTION_SHA256,
        "census_addendum_sha256": CENSUS_ADDENDUM_SHA256,
        "recovered_source_manifest_sha256": RECOVERED_MANIFEST_SHA256,
        "recovered_source_manifest_entries": 834,
        "recovered_source_snapshot_sha256": RECOVERED_SNAPSHOT_SHA256,
        "first_link_failure": {
            "observed_rc": 1,
            "cause": "missing -lgivaro -lgmpxx -lgmp in the first compiler-harvest C++ link",
            "role": "failed attempt only; resumed build/solve/validator provide certifying result",
        },
        "row_mutation": {
            "row": "Tg19_7",
            "changed_monomial": encode_monomial(mutation_monomial),
            "changed_coefficient_by": [1, 1],
            "all_original_product_residuals_zero": True,
            "products_checked": len(multipliers),
            "detected_product_count": len(mutation_records),
            "residual_records_sha256": mutation_sha,
            "residual_records_path": str(mutation_path),
        },
        "strengthened_corollary": "a1^i is not in J0 for every 0<=i<=6, by the ideal property from a1^6 nonmembership",
        "v42_scope_correction": "V42 a1^8 membership is in its six-row A1 branch ideal, not globally before branch clearing",
    }
    result_path = output / "result.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("PASS-A1-N6-R1-ADDITIVE-CONTROLS")
    print(f"RESULT_SHA256={digest(result_path)}")


if __name__ == "__main__":
    main()

