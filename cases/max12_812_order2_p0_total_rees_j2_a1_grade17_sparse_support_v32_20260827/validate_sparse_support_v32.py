#!/usr/bin/env python3
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("--compile-result", type=Path, required=True)
    cli.add_argument("--stdout", type=Path, required=True)
    cli.add_argument("--stderr", type=Path, required=True)
    cli.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    cli.add_argument("--basis", type=Path, required=True)
    cli.add_argument("--nf", type=Path, required=True)
    cli.add_argument("--output", type=Path, required=True)
    args = cli.parse_args()
    result = json.loads(args.compile_result.read_text())
    if (result.get("status") != "PASS-A1-GRADE17-SPARSE-SUPPORT-V32-COMPILER"
            or result.get("characteristic") != args.characteristic
            or result.get("rows") != 56
            or result.get("variables") != ["ell2", "cs1", "rs2", "aa0", "ee1", "ec3"]
            or result.get("base_grade17_residual") != [-20736, 1]
            or not result.get("newton_nonzero_residuals_q")):
        raise RuntimeError("compile contract")
    stdout = args.stdout.read_text(); stderr = args.stderr.read_text()
    for token in ("V32_CONTROLS=1", "PASS_A1_GRADE17_SPARSE_SUPPORT_V32"):
        if stdout.count(token) != 1:
            raise RuntimeError(("stdout token", token))
    unit_tokens = [token for token in ("V32_UNIT_IDEAL=0", "V32_UNIT_IDEAL=1") if stdout.count(token) == 1]
    if len(unit_tokens) != 1 or stdout.count("V32_STANDARD_BASIS_SIZE=") != 1 or stdout.count("V32_DIM=") != 1:
        raise RuntimeError("decision token")
    if stderr.count("Command being timed:") != 1 or stderr.count("Exit status: 0") != 1:
        raise RuntimeError("resource stderr")
    if any(token in stdout or token in stderr for token in ("FAIL_", "?", "error occurred", "Killed", "out of memory")):
        raise RuntimeError("diagnostic token")
    if not args.basis.is_file() or not args.nf.is_file():
        raise RuntimeError("missing exports")
    final = {
        "status": "PASS-A1-GRADE17-SPARSE-SUPPORT-V32",
        "characteristic": args.characteristic,
        "unit_ideal": int(unit_tokens[0].endswith("=1")),
        "compile_result_sha256": digest(args.compile_result),
        "stdout_sha256": digest(args.stdout),
        "resource_stderr_sha256": digest(args.stderr),
        "basis_sha256": digest(args.basis),
        "nf_sha256": digest(args.nf),
    }
    args.output.write_text(json.dumps(final, sort_keys=True, indent=2) + "\n")
    print("PASS-A1-GRADE17-SPARSE-SUPPORT-V32-VALIDATOR")
    print(unit_tokens[0])


if __name__ == "__main__":
    main()

