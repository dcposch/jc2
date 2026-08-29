#!/usr/bin/env python3
"""Fail-closed validator for exact K00 local-ring membership."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def unique(lines: list[str], prefix: str) -> str:
    values = [line[len(prefix):] for line in lines if line.startswith(prefix)]
    if len(values) != 1:
        raise RuntimeError(("missing/nonunique marker", prefix, values))
    return values[0]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("stdout", type=Path)
    parser.add_argument("artifacts", type=Path)
    parser.add_argument("compiler_result", type=Path)
    parser.add_argument("result", type=Path)
    args = parser.parse_args()
    text = args.stdout.read_text()
    lines = [line.strip() for line in text.splitlines()]
    if "?" in text or any("K00_LOCAL_FAIL=" in line for line in lines):
        raise RuntimeError("Singular diagnostic or failure marker")
    required = [
        "K00_LOCAL_MODE=KUMMER_NORMALIZED_C6_1_DS",
        "K00_LOCAL_SOURCE_HASHES=PASS",
        "K00_LOCAL_TOY_POSITIVE=1",
        "K00_LOCAL_TOY_NEGATIVE=1",
        "K00_LOCAL_TOY_REPLAY=1",
        "K00_LOCAL_TOY_UNIT=1",
        "K00_LOCAL_STD_START",
        "K00_LOCAL_STD_DONE",
        "K00_LOCAL_BASIS_REPLAY=1",
        "K00_LOCAL_NEGATIVE_CONTROL_PROPER=1",
        "K00_LOCAL_ENDPOINT=PASS_MEMBERSHIP_DECISION",
    ]
    for marker in required:
        if sum(line == marker for line in lines) != 1:
            raise RuntimeError(("missing/nonunique required marker", marker))
    basis = args.artifacts / "LOCAL_STANDARD_BASIS.txt"
    transform = args.artifacts / "LOCAL_BASIS_TRANSFORM.txt"
    for path in (basis, transform):
        if not path.is_file() or not path.read_text().strip():
            raise RuntimeError(("missing basis evidence", str(path)))
    member_text = unique(lines, "K00_LOCAL_MEMBER=")
    if member_text not in ("0", "1"):
        raise RuntimeError("malformed membership result")
    member = member_text == "1"
    extra: dict[str, object]
    if member:
        for marker in ("K00_LOCAL_LIFT_REPLAY=1", "K00_LOCAL_UNIT_CONSTANT_NONZERO=1", "K00_LOCAL_EVIDENCE=UNIT_DENOMINATOR_LIFT"):
            if sum(line == marker for line in lines) != 1:
                raise RuntimeError(("missing member marker", marker))
        multipliers = args.artifacts / "LOCAL_MEMBERSHIP_MULTIPLIERS.txt"
        unit = args.artifacts / "LOCAL_MEMBERSHIP_UNIT.txt"
        for path in (multipliers, unit):
            if not path.is_file() or not path.read_text().strip():
                raise RuntimeError(("missing member evidence", str(path)))
        extra = {
            "evidence_kind": "UNIT_DENOMINATOR_LIFT",
            "multipliers_sha256": digest(multipliers),
            "unit_sha256": digest(unit),
        }
    else:
        for marker in ("K00_LOCAL_LIFT_REPLAY=NOT_APPLICABLE", "K00_LOCAL_EVIDENCE=LOCAL_RESIDUAL"):
            if sum(line == marker for line in lines) != 1:
                raise RuntimeError(("missing nonmember marker", marker))
        residual = args.artifacts / "LOCAL_NONMEMBERSHIP_RESIDUAL.txt"
        leading = args.artifacts / "LOCAL_LEADING_TRANSVERSE_CLASS.txt"
        for path in (residual, leading):
            if not path.is_file() or not path.read_text().strip():
                raise RuntimeError(("missing nonmember evidence", str(path)))
        lowest = int(unique(lines, "K00_LOCAL_LOWEST_TRANSVERSE_DEGREE="))
        leading_terms = int(unique(lines, "K00_LOCAL_LEADING_TERMS="))
        if lowest < 2 or leading_terms < 1:
            raise RuntimeError("invalid nonmember degree telemetry")
        extra = {
            "evidence_kind": "LOCAL_RESIDUAL",
            "lowest_transverse_degree": lowest,
            "leading_terms": leading_terms,
            "residual_sha256": digest(residual),
            "leading_class_sha256": digest(leading),
        }
    compiler = json.loads(args.compiler_result.read_text())
    if compiler.get("characteristic") != 0 or compiler.get("order") != "ds":
        raise RuntimeError("compiler field/order mismatch")
    result = {
        **compiler,
        "status": "PASS-K00-LOCAL-MEMBERSHIP-ENDPOINT",
        "member": member,
        "standard_basis_sha256": digest(basis),
        "basis_transform_sha256": digest(transform),
        "compiler_result_sha256": digest(args.compiler_result),
        **extra,
    }
    args.result.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
