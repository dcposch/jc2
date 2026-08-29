#!/usr/bin/env python3
"""Fail-closed validator for repaired exact unloaded K00 V8 lanes."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def unique_value(lines: list[str], prefix: str) -> str:
    values = [line[len(prefix):] for line in lines if line.startswith(prefix)]
    if len(values) != 1:
        raise RuntimeError(("missing or nonunique value", prefix, values))
    return values[0]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("stdout", type=Path)
    parser.add_argument("artifacts", type=Path)
    parser.add_argument("compiler_result", type=Path)
    parser.add_argument("result", type=Path)
    parser.add_argument("--mode", choices=("direct", "normalized"), required=True)
    args = parser.parse_args()
    text = args.stdout.read_text()
    lines = [line.strip() for line in text.splitlines()]
    if "?" in text or any("K00_UNLOADED_V8_FAIL=" in line for line in lines):
        raise RuntimeError("diagnostic or failure marker in engine output")
    label = "DIRECT_LOCALIZED" if args.mode == "direct" else "KUMMER_NORMALIZED_C6_1"
    required = [
        f"K00_UNLOADED_V8_MODE={label}",
        "K00_UNLOADED_V8_SOURCE_HASHES=PASS",
        "K00_UNLOADED_V8_LOADS_REMOVED_BY_LITERAL_ZERO_SPECIALIZATION=PASS",
        "K00_UNLOADED_V8_STD_START",
        "K00_UNLOADED_V8_STD_DONE",
        "K00_UNLOADED_V8_NEGATIVE_CONTROL_PROPER=1",
        "K00_UNLOADED_V8_ENDPOINT=PASS_MEMBERSHIP_DECISION",
    ]
    for marker in required:
        if sum(line == marker for line in lines) != 1:
            raise RuntimeError(("missing or nonunique marker", marker))
    member_text = unique_value(lines, "K00_UNLOADED_V8_MEMBER=")
    if member_text not in ("0", "1"):
        raise RuntimeError("malformed membership marker")
    member = member_text == "1"
    basis = args.artifacts / "STANDARD_BASIS.txt"
    if not basis.is_file() or not basis.read_text().strip():
        raise RuntimeError("missing standard basis")
    telemetry: dict[str, object] = {}
    evidence_paths: list[Path]
    if member:
        if sum(line == "K00_UNLOADED_V8_LIFT_REPLAY=1" for line in lines) != 1:
            raise RuntimeError("missing successful lift replay")
        if sum(line == "K00_UNLOADED_V8_EVIDENCE=LIFT" for line in lines) != 1:
            raise RuntimeError("wrong membership evidence marker")
        lift = args.artifacts / "MEMBERSHIP_LIFT.txt"
        if not lift.is_file() or not lift.read_text().strip():
            raise RuntimeError("missing membership lift")
        kind = "LIFT"
        evidence_paths = [basis, lift]
    else:
        nonmember_required = [
            "K00_UNLOADED_V8_TRANSVERSE_DECOMPOSITION=1",
            "K00_UNLOADED_V8_LEADING_HOMOGENEOUS=1",
            "K00_UNLOADED_V8_LIFT_REPLAY=NOT_APPLICABLE",
            "K00_UNLOADED_V8_EVIDENCE=RESIDUAL_AND_LEADING_CLASS",
        ]
        for marker in nonmember_required:
            if sum(line == marker for line in lines) != 1:
                raise RuntimeError(("missing nonmembership telemetry marker", marker))
        residual = args.artifacts / "NONMEMBERSHIP_RESIDUAL.txt"
        leading = args.artifacts / "LEADING_TRANSVERSE_CLASS.txt"
        for path in (residual, leading):
            if not path.is_file() or not path.read_text().strip():
                raise RuntimeError(("missing nonmembership evidence", str(path)))
        residual_terms = int(unique_value(lines, "K00_UNLOADED_V8_RESIDUAL_TERMS="))
        lowest = int(unique_value(lines, "K00_UNLOADED_V8_LOWEST_TRANSVERSE_DEGREE="))
        leading_terms = int(unique_value(lines, "K00_UNLOADED_V8_LEADING_TERMS="))
        if residual_terms < 1 or lowest < 0 or leading_terms < 1 or leading_terms > residual_terms:
            raise RuntimeError("invalid transverse telemetry integers")
        telemetry = {
            "residual_terms": residual_terms,
            "lowest_transverse_degree": lowest,
            "leading_terms": leading_terms,
            "residual_sha256": digest(residual),
            "leading_transverse_class_sha256": digest(leading),
            "leading_transverse_class": leading.read_text().strip(),
        }
        kind = "RESIDUAL_AND_LEADING_CLASS"
        evidence_paths = [basis, residual, leading]
    compiler = json.loads(args.compiler_result.read_text())
    if compiler.get("mode") != args.mode or compiler.get("characteristic") != 0:
        raise RuntimeError("compiler mode/characteristic mismatch")
    result = {
        **compiler,
        "status": "PASS-K00-UNLOADED-V8-ENDPOINT",
        "member": member,
        "evidence_kind": kind,
        "standard_basis_sha256": digest(basis),
        "compiler_result_sha256": digest(args.compiler_result),
        **telemetry,
    }
    args.result.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
