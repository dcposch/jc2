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
    cli.add_argument("--compiled", type=Path, required=True)
    cli.add_argument("--stdout", type=Path, required=True)
    cli.add_argument("--stderr", type=Path, required=True)
    cli.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    cli.add_argument("--output", type=Path, required=True)
    args = cli.parse_args()
    compiled = json.loads(args.compiled.read_text())
    script = Path(compiled["script"])
    if (
        compiled.get("status") != "PASS-A1-RHO0-UNIT-SCREEN-G16-V29-COMPILER"
        or compiled.get("characteristic") != args.characteristic
        or compiled.get("input_rows") != 49
        or compiled.get("old_point_zero_rows") != 42
        or compiled.get("grade16_point_control") != [-47, 384]
        or compiled.get("nonzero_rows", 0) < 24
        or not isinstance(compiled.get("variables"), list)
        or digest(script) != compiled.get("script_sha256")
    ):
        raise RuntimeError("compiler contract")
    stdout = args.stdout.read_text()
    stderr = args.stderr.read_text()
    if stderr.count("Command being timed:") != 1 or stderr.count("Exit status: 0") != 1:
        raise RuntimeError("resource stderr")
    if any(token in stdout or token in stderr for token in ("FAIL_", "?", "error occurred", "Killed", "out of memory")):
        raise RuntimeError("diagnostic token")
    for token in ("V29_CONTROLS=1", "PASS_A1_RHO0_UNIT_SCREEN_G16_V29"):
        if stdout.count(token) != 1:
            raise RuntimeError(("required token", token))
    unit_tokens = [token for token in ("V29_UNIT_IDEAL=0", "V29_UNIT_IDEAL=1") if stdout.count(token) == 1]
    if len(unit_tokens) != 1:
        raise RuntimeError("unit verdict")
    basis_lines = [line for line in stdout.splitlines() if line.startswith("V29_STANDARD_BASIS_SIZE=")]
    if len(basis_lines) != 1 or int(basis_lines[0].split("=", 1)[1]) <= 0:
        raise RuntimeError("basis size")
    outcome = "unit" if unit_tokens[0].endswith("1") else "nonunit"
    final = {
        "status": "PASS-A1-RHO0-UNIT-SCREEN-G16-V29",
        "characteristic": args.characteristic,
        "outcome": outcome,
        "standard_basis_size": int(basis_lines[0].split("=", 1)[1]),
        "compiled_sha256": digest(args.compiled),
        "script_sha256": digest(script),
        "stdout_sha256": digest(args.stdout),
        "resource_stderr_sha256": digest(args.stderr),
        "nf_sha256": digest(args.compiled.parent / "NF.txt"),
    }
    args.output.write_text(json.dumps(final, sort_keys=True, indent=2) + "\n")
    print("PASS-A1-RHO0-UNIT-SCREEN-G16-V29-VALIDATOR")
    print(f"OUTCOME={outcome}")
    print(f"STANDARD_BASIS_SIZE={final['standard_basis_size']}")


if __name__ == "__main__":
    main()

