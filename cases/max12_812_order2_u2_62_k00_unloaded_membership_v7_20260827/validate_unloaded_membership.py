#!/usr/bin/env python3
"""Fail-closed validator for exact unloaded K00 membership lanes."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


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
    if "?" in text or any("K00_UNLOADED_FAIL=" in line for line in lines):
        raise RuntimeError("diagnostic or failure marker in engine output")
    label = "DIRECT_LOCALIZED" if args.mode == "direct" else "KUMMER_NORMALIZED_C6_1"
    required = [
        f"K00_UNLOADED_MODE={label}",
        "K00_UNLOADED_SOURCE_HASHES=PASS",
        "K00_UNLOADED_LOADS_REMOVED_BY_LITERAL_ZERO_SPECIALIZATION=PASS",
        "K00_UNLOADED_STD_START",
        "K00_UNLOADED_STD_DONE",
        "K00_UNLOADED_NEGATIVE_CONTROL_PROPER=1",
        "K00_UNLOADED_ENDPOINT=PASS_MEMBERSHIP_DECISION",
    ]
    for marker in required:
        if sum(line == marker for line in lines) != 1:
            raise RuntimeError(("missing or nonunique marker", marker))
    member_lines = [line for line in lines if line.startswith("K00_UNLOADED_MEMBER=")]
    if len(member_lines) != 1 or member_lines[0] not in ("K00_UNLOADED_MEMBER=0", "K00_UNLOADED_MEMBER=1"):
        raise RuntimeError("missing or malformed membership marker")
    member = member_lines[0].endswith("=1")
    basis = args.artifacts / "STANDARD_BASIS.txt"
    if not basis.is_file() or not basis.read_text().strip():
        raise RuntimeError("missing standard basis")
    if member:
        if sum(line == "K00_UNLOADED_LIFT_REPLAY=1" for line in lines) != 1:
            raise RuntimeError("missing successful lift replay")
        evidence = args.artifacts / "MEMBERSHIP_LIFT.txt"
        kind = "LIFT"
    else:
        if sum(line == "K00_UNLOADED_LIFT_REPLAY=NOT_APPLICABLE" for line in lines) != 1:
            raise RuntimeError("wrong nonmembership replay marker")
        evidence = args.artifacts / "NONMEMBERSHIP_RESIDUAL.txt"
        kind = "RESIDUAL"
    if sum(line == f"K00_UNLOADED_EVIDENCE={kind}" for line in lines) != 1:
        raise RuntimeError("wrong evidence marker")
    if not evidence.is_file() or not evidence.read_text().strip():
        raise RuntimeError("missing endpoint evidence")
    compiler = json.loads(args.compiler_result.read_text())
    if compiler.get("mode") != args.mode or compiler.get("characteristic") != 0:
        raise RuntimeError("compiler mode/characteristic mismatch")
    result = {
        **compiler,
        "status": "PASS-K00-UNLOADED-MEMBERSHIP-ENDPOINT",
        "member": member,
        "evidence_kind": kind,
        "standard_basis_sha256": digest(basis),
        "membership_evidence_sha256": digest(evidence),
        "compiler_result_sha256": digest(args.compiler_result),
    }
    args.result.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
