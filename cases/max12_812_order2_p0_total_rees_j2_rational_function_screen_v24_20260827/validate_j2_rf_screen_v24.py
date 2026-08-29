#!/usr/bin/env python3
"""Fail-closed validator for a V24 Singular screen."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--compiled", type=Path, required=True)
    ap.add_argument("--stdout", type=Path, required=True)
    ap.add_argument("--stderr", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    compiled = json.loads(args.compiled.read_text())
    if (
        compiled.get("status") != "PASS-J2-RF-SCREEN-V24-COMPILER"
        or compiled.get("chart") not in ("a0_chart", "a1_ordered")
        or compiled.get("characteristic") not in (0, 65521)
        or compiled.get("input_rows") != 42
        or compiled.get("degree_bound") != 15
        or len(compiled.get("input_sha256", {})) != 42
        or len(compiled.get("ring_variables", [])) != len(compiled.get("ring_weights", []))
    ):
        raise RuntimeError("compiler contract")
    script = Path(compiled["script"])
    if digest(script) != compiled["script_sha256"]:
        raise RuntimeError("script hash")
    stdout = args.stdout.read_text()
    stderr = args.stderr.read_text()
    if stderr.count("Command being timed:") != 1 or stderr.count("Exit status: 0") != 1:
        raise RuntimeError(("resource stderr", stderr[-2000:]))
    if any(token in stdout or token in stderr for token in ("FAIL_", "?", "error occurred", "Killed", "out of memory")):
        raise RuntimeError("diagnostic token")
    required = [
        f"V24_CHART={compiled['chart']}",
        f"V24_CHARACTERISTIC={compiled['characteristic']}",
        "V24_CONTROLS=1",
        "PASS_J2_RF_SCREEN_V24",
    ]
    for token in required:
        if stdout.count(token) != 1:
            raise RuntimeError(("required token", token, stdout.count(token)))
    member_count = stdout.count("V24_TARGET_RF_MEMBERSHIP=1")
    nonmember_count = stdout.count("V24_TARGET_RF_MEMBERSHIP=0")
    if member_count + nonmember_count != 1:
        raise RuntimeError("outcome census")
    directory = args.compiled.parent
    if member_count:
        artifact = directory / "LIFT.txt"
        if stdout.count("V24_LIFT_REPLAY=1") != 1 or not artifact.is_file() or not artifact.stat().st_size:
            raise RuntimeError("membership artifact")
        outcome = "RATIONAL_FUNCTION_MEMBERSHIP"
    else:
        artifact = directory / "TARGET_NF.txt"
        if stdout.count("V24_TARGET_NF_NONZERO=1") != 1 or not artifact.is_file() or not artifact.stat().st_size:
            raise RuntimeError("nonmembership artifact")
        outcome = "RATIONAL_FUNCTION_NONMEMBERSHIP"
    final = {
        "status": "PASS-J2-RF-SCREEN-V24",
        "chart": compiled["chart"],
        "characteristic": compiled["characteristic"],
        "outcome": outcome,
        "target": compiled["target"],
        "degree_bound": 15,
        "compiled_sha256": digest(args.compiled),
        "script_sha256": digest(script),
        "stdout_sha256": digest(args.stdout),
        "resource_stderr_sha256": digest(args.stderr),
        "artifact": str(artifact),
        "artifact_sha256": digest(artifact),
        "scope": "coefficient-field homogeneous cubic screen; membership requires denominator review before any polynomial certificate",
    }
    args.output.write_text(json.dumps(final, sort_keys=True, indent=2) + "\n")
    print(json.dumps(final, sort_keys=True))


if __name__ == "__main__":
    main()

