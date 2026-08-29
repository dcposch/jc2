#!/usr/bin/env python3
"""Fail-closed validator for repaired V13 T-rs rho-unit output."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--compiler-result", type=Path, required=True)
    parser.add_argument("--stdout", type=Path, required=True)
    parser.add_argument("--stderr", type=Path, required=True)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    parser.add_argument("--algorithm", choices=("sat", "elim"), required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    compiler = json.loads(args.compiler_result.read_text())
    if (
        compiler.get("status") != "PASS-T-RS-RHO-UNIT-V13-COMPILER"
        or compiler.get("characteristic") != args.characteristic
        or compiler.get("algorithm") != args.algorithm
        or compiler.get("v12_compiler_sha256")
        != "9805bce184294bfdd3c81797192d9257e17865e4741d0df56bbbd334d6fdb2fd"
    ):
        raise RuntimeError("compiler result mismatch")
    script = Path(compiler["script"])
    if digest(script) != compiler.get("script_sha256"):
        raise RuntimeError("script hash mismatch")
    stdout = args.stdout.read_text()
    stderr = args.stderr.read_text()
    if stderr.count("Command being timed:") != 1 or stderr.count("Exit status: 0") != 1:
        raise RuntimeError(("resource stderr", stderr[-2000:]))
    forbidden = ("FAIL_", "?", "error occurred", "out of memory", "Killed", "Segment fault")
    if any(token in stdout or token in stderr for token in forbidden):
        raise RuntimeError(("diagnostic token", [t for t in forbidden if t in stdout or t in stderr]))
    required = (
        "V13_QRING_DISABLED=1",
        f"V13_CHARACTERISTIC={args.characteristic}",
        f"V13_ALGORITHM={args.algorithm}",
        "V13_MULTIPLICATION_BACK_COUNT=4",
        "V13_FOUR_TERM_DELTA=1",
        "V13_B_DECOMPOSITION=1",
        "V13_CERTIFICATE_IDENTITY=1",
        "V13_NEGATIVE_CONTROL_COUNT=2",
        "V13_SATURATED_KU_MEMBERSHIP=1",
        "V13_SPECIAL_CONTAINS_K=1",
        "V13_RHO_INVERSE=1",
        "V13_SPECIAL_DK_UNIT=1",
        "V13_ARTIFACT_WRITES=4",
        "V13_SCOPE=T_RS_ACTUAL_CHART_DK_RHO_UNIT_PREFIX_ONLY",
        "PASS_T_RS_RHO_UNIT_V13",
    )
    for token in required:
        if stdout.count(token) != 1:
            raise RuntimeError(("required token", token, stdout.count(token)))
    if args.algorithm == "sat" and "V13_SAT_RETURN_LENGTH=1" not in stdout:
        raise RuntimeError("saturation return length")
    artifacts: dict[str, dict[str, object]] = {}
    for raw in compiler.get("artifacts", []):
        path = Path(raw)
        if not path.is_file() or path.stat().st_size == 0:
            raise RuntimeError(("missing artifact", path))
        artifacts[path.name] = {"sha256": digest(path), "bytes": path.stat().st_size}
    result = {
        "status": "PASS-T-RS-RHO-UNIT-V13",
        "scope": "T_RS_ACTUAL_CHART_DK_RHO_UNIT_PREFIX_ONLY",
        "characteristic": args.characteristic,
        "algorithm": args.algorithm,
        "rho_unit_on_dk": True,
        "special_dk_unit_ideal": True,
        "compiler_result_sha256": digest(args.compiler_result),
        "script_sha256": digest(script),
        "stdout_sha256": digest(args.stdout),
        "resource_stderr_sha256": digest(args.stderr),
        "artifacts": artifacts,
    }
    args.output.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
