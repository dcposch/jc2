#!/usr/bin/env python3
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path
import re


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def unique(pattern: str, text: str) -> str:
    matches = re.findall(pattern, text, flags=re.MULTILINE)
    if len(matches) != 1:
        raise RuntimeError(("token", pattern, matches))
    return matches[0]


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("--compile-result", type=Path, required=True)
    cli.add_argument("--stdout", type=Path, required=True)
    cli.add_argument("--stderr", type=Path, required=True)
    cli.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    cli.add_argument("--nf", type=Path, required=True)
    cli.add_argument("--basis", type=Path, required=True)
    cli.add_argument("--output", type=Path, required=True)
    args = cli.parse_args()
    compiled = json.loads(args.compile_result.read_text())
    if (compiled.get("status") != "PASS-A1-GRADE18-CURVE-CUT-V34-COMPILER"
            or compiled.get("characteristic") != args.characteristic
            or compiled.get("variables") != ["ell2", "cs1", "rs2", "aa0", "ee1", "ec3"]
            or compiled.get("old_basis_size") != 24
            or compiled.get("grade18_restricted_term_count") != 16
            or compiled.get("known_branch_value") != "41472/l with l^5=243/2"):
        raise RuntimeError("compile contract")
    stdout = args.stdout.read_text(); stderr = args.stderr.read_text()
    for token in ("V34_CONTROLS=1", "PASS_A1_GRADE18_CURVE_CUT_V34"):
        if stdout.count(token) != 1:
            raise RuntimeError(("stdout token", token))
    if stderr.count("Command being timed:") != 1 or stderr.count("Exit status: 0") != 1:
        raise RuntimeError("resource stderr")
    if any(token in stdout or token in stderr for token in ("FAIL_", "?", "error occurred", "Killed", "out of memory")):
        raise RuntimeError("diagnostic token")
    dimension = int(unique(r"^V34_DIM=(-?\d+)$", stdout))
    basis_size = int(unique(r"^V34_STANDARD_BASIS_SIZE=(\d+)$", stdout))
    unit_ideal = int(unique(r"^V34_UNIT_IDEAL=([01])$", stdout))
    vdim_raw = unique(r"^V34_VDIM=(NA|\d+)$", stdout)
    if not args.nf.is_file() or not args.basis.is_file() or not args.nf.read_text().strip() or not args.basis.read_text().strip():
        raise RuntimeError("missing export")
    if unit_ideal and dimension >= 0:
        raise RuntimeError(("unit dimension", dimension))
    if not unit_ideal and dimension < 0:
        raise RuntimeError(("proper dimension", dimension))
    if dimension == 0 and not unit_ideal and vdim_raw == "NA":
        raise RuntimeError("missing vdim")
    outcome = "curve_eliminated" if unit_ideal else ("finite_survivor" if dimension == 0 else "positive_dimensional_survivor")
    final = {
        "status": "PASS-A1-GRADE18-CURVE-CUT-V34",
        "characteristic": args.characteristic,
        "outcome": outcome,
        "unit_ideal": unit_ideal,
        "dimension": dimension,
        "vector_space_dimension": None if vdim_raw == "NA" else int(vdim_raw),
        "standard_basis_size": basis_size,
        "compile_result_sha256": digest(args.compile_result),
        "stdout_sha256": digest(args.stdout),
        "resource_stderr_sha256": digest(args.stderr),
        "normal_form_sha256": digest(args.nf),
        "basis_sha256": digest(args.basis),
    }
    args.output.write_text(json.dumps(final, sort_keys=True, indent=2) + "\n")
    print("PASS-A1-GRADE18-CURVE-CUT-V34-VALIDATOR")
    print(f"V34_OUTCOME={outcome}")


if __name__ == "__main__":
    main()
