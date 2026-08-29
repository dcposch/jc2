#!/usr/bin/env python3
"""Fail-closed validator for a completed K00 g-open lane."""

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


def value(lines: list[str], key: str) -> str:
    prefix = key + "="
    found = [line[len(prefix):] for line in lines if line.startswith(prefix)]
    if len(found) != 1 or not found[0]:
        fail(f"missing or nonunique value: {key}")
    return found[0]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("stdout", type=Path)
    parser.add_argument("artifact_dir", type=Path)
    parser.add_argument("compiler_result", type=Path)
    parser.add_argument("result", type=Path)
    parser.add_argument("--tag", required=True)
    args = parser.parse_args()
    lines = [line.strip() for line in args.stdout.read_text().splitlines()]
    if any("K00_FAIL=" in line or line.startswith("? ") for line in lines):
        fail("Singular failure/diagnostic marker")
    for marker in [
        "K00_SOURCE_HASHES=PASS",
        "K00_JDET_DISTINCT_FROM_J1_J2=PASS",
        "K00_INVARIANT_CORE_ROW_MAP=PASS",
        "K00_RESTRICTION_CERTIFICATE_IDENTITY=PASS",
        "K00_RESTRICTION_FIRST_UNIT=PASS",
        "K00_GOPEN_EQUIVALENCE=SAT_G_CONTRACTION",
        "K00_STAGE_GOPEN_SOURCE_DONE",
        "K00_STAGE_BOUNDARY_CORE_DONE",
        "K00_STAGE_FINAL_LOCALIZATION_DONE",
        "K00_GOPEN_OPERATION_ORDER=PASS",
        "K00_CLOSURE_ENDPOINT=PASS",
    ]:
        unique(lines, marker)
    endpoint = value(lines, "K00_H_ENDPOINT")
    if endpoint not in {"UNIT", "NONUNIT"}:
        fail("invalid endpoint")
    metrics = {}
    for key in [
        "K00_GOPEN_SIZE", "K00_B_SIZE", "K00_H_SIZE",
        "K00_H_DIM", "K00_H_SATURATION_EXPONENT",
    ]:
        raw = value(lines, key)
        if not re.fullmatch(r"-?[0-9]+", raw):
            fail(f"noninteger {key}")
        metrics[key] = int(raw)
    basis = args.artifact_dir / "H_BASIS.txt"
    if not basis.is_file() or basis.stat().st_size == 0:
        fail("missing H basis")
    evidence = {"H_BASIS.txt": digest(basis)}
    if endpoint == "UNIT":
        unique(lines, "K00_H_UNIT_LIFT_REPLAY=PASS")
        lift = args.artifact_dir / "H_UNIT_LIFT.txt"
        if not lift.is_file() or lift.stat().st_size == 0:
            fail("missing unit lift")
        evidence["H_UNIT_LIFT.txt"] = digest(lift)
    else:
        unique(lines, "K00_H_NONUNIT_BASIS_SAVED=PASS")
    compiler = json.loads(args.compiler_result.read_text())
    result = {
        "status": "PASS-K00-GOPEN-ENDPOINT",
        "tag": args.tag,
        "characteristic": compiler["characteristic"],
        "endpoint": endpoint,
        "algorithm": compiler["algorithm"],
        "metrics": metrics,
        "stdout_sha256": digest(args.stdout),
        "compiler_result_sha256": digest(args.compiler_result),
        "evidence_sha256": evidence,
        "scope": compiler["scope"],
    }
    args.result.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
