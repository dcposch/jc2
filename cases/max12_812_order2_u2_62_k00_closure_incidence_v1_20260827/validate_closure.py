#!/usr/bin/env python3
"""Fail-closed validator for a completed K00 closure-first AWS lane."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path
import re


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: str) -> "None":
    raise RuntimeError(message)


def unique(lines: list[str], marker: str) -> None:
    if sum(line == marker for line in lines) != 1:
        fail(f"missing or nonunique marker: {marker}")


def unique_value(lines: list[str], key: str) -> str:
    prefix = key + "="
    values = [line[len(prefix):] for line in lines if line.startswith(prefix)]
    if len(values) != 1 or not values[0]:
        fail(f"missing or nonunique value: {key}")
    return values[0]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("stdout", type=Path)
    parser.add_argument("artifact_dir", type=Path)
    parser.add_argument("compiler_result", type=Path)
    parser.add_argument("result", type=Path)
    parser.add_argument("--tag", required=True)
    parser.add_argument("--characteristic", required=True, type=int)
    args = parser.parse_args()

    lines = [line.strip() for line in args.stdout.read_text().splitlines()]
    if any("K00_FAIL=" in line for line in lines):
        fail("Singular emitted a K00_FAIL marker")
    if any(line.startswith("? ") for line in lines):
        fail("Singular emitted a diagnostic")
    required = [
        "K00_SOURCE_HASHES=PASS",
        "K00_SOURCE_TYPE=A_Q_Lambda_C0_C6_k10_k6_k2_mu2_mu4_mu6_Jdet",
        "K00_JDET_DISTINCT_FROM_J1_J2=PASS",
        "K00_LOAD_LINEARITY=PASS",
        "K00_INVARIANT_CORE_ROW_MAP=PASS",
        "K00_RESTRICTION_CERTIFICATE_IDENTITY=PASS",
        "K00_STAGE_RESTRICTION_FIRST_DONE",
        "K00_RESTRICTION_FIRST_UNIT=PASS",
        "K00_STAGE_CLOSURE_LAMBDA_DONE",
        "K00_STAGE_CLOSURE_JDET_DONE",
        "K00_STAGE_BOUNDARY_CORE_DONE",
        "K00_STAGE_FINAL_LOCALIZATION_DONE",
        "K00_CLOSURE_FIRST_ORDER=PASS",
        "K00_CLOSURE_ENDPOINT=PASS",
    ]
    for marker in required:
        unique(lines, marker)

    endpoint = unique_value(lines, "K00_H_ENDPOINT")
    if endpoint not in {"UNIT", "NONUNIT"}:
        fail(f"invalid endpoint: {endpoint}")
    integer_keys = [
        "K00_KL_SIZE", "K00_K_SIZE", "K00_B_SIZE",
        "K00_H_SIZE", "K00_H_DIM", "K00_H_SATURATION_EXPONENT",
    ]
    integers: dict[str, int] = {}
    for key in integer_keys:
        value = unique_value(lines, key)
        if not re.fullmatch(r"-?[0-9]+", value):
            fail(f"noninteger {key}: {value}")
        integers[key] = int(value)

    basis = args.artifact_dir / "H_BASIS.txt"
    if not basis.is_file() or basis.stat().st_size == 0:
        fail("missing or empty H_BASIS.txt")
    evidence = {"H_BASIS.txt": digest(basis)}
    if endpoint == "UNIT":
        unique(lines, "K00_H_UNIT_LIFT_REPLAY=PASS")
        lift = args.artifact_dir / "H_UNIT_LIFT.txt"
        if not lift.is_file() or lift.stat().st_size == 0:
            fail("unit endpoint lacks H_UNIT_LIFT.txt")
        evidence["H_UNIT_LIFT.txt"] = digest(lift)
    else:
        unique(lines, "K00_H_NONUNIT_BASIS_SAVED=PASS")
        if any(line == "K00_H_UNIT_LIFT_REPLAY=PASS" for line in lines):
            fail("nonunit endpoint emitted unit lift marker")

    compiler = json.loads(args.compiler_result.read_text())
    if compiler.get("characteristic") != args.characteristic:
        fail("compiler/validator characteristic mismatch")
    if compiler.get("jacobian_parameter") != "Jdet":
        fail("compiler did not retain Jdet identifier")

    result = {
        "status": "PASS-K00-CLOSURE-FIRST-ENDPOINT",
        "tag": args.tag,
        "characteristic": args.characteristic,
        "endpoint": endpoint,
        "endpoint_interpretation": (
            "EXCLUDES_GENERIC_K00_INCIDENCE_FOR_FIXED_U2_62_ORDINARY_CLIENT"
            if endpoint == "UNIT"
            else "ACCESSIBLE_ALGEBRAIC_BOUNDARY_SUPPORT_ONLY"
        ),
        "restriction_first_negative_control": "UNIT_WITH_EXPLICIT_IDENTITY",
        "closure_first_order": compiler["operation_order"],
        "metrics": integers,
        "stdout_sha256": digest(args.stdout),
        "compiler_result_sha256": digest(args.compiler_result),
        "evidence_sha256": evidence,
        "scope": compiler["scope"],
    }
    args.result.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
