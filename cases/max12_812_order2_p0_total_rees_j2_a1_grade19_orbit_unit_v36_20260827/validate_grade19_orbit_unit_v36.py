#!/usr/bin/env python3
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    cli = argparse.ArgumentParser(); cli.add_argument("--compile-result", type=Path, required=True)
    cli.add_argument("--compiler-stdout", type=Path, required=True); cli.add_argument("--compiler-stderr", type=Path, required=True)
    cli.add_argument("--engine-stdout", type=Path, required=True); cli.add_argument("--engine-stderr", type=Path, required=True)
    cli.add_argument("--characteristic", type=int, choices=(0, 65521), required=True); cli.add_argument("--output", type=Path, required=True)
    args = cli.parse_args(); result = json.loads(args.compile_result.read_text())
    if (result.get("status") != "PASS-A1-GRADE19-ORBIT-UNIT-V36-COMPILER"
            or result.get("characteristic") != args.characteristic or result.get("rows_checked") != 7
            or result.get("weight19_variables") != [] or result.get("restricted_row") != "Tg19_7"
            or result.get("restricted_term_count", 0) < 1 or len(result.get("row_sha256", {})) != 7
            or digest(Path(result.get("script", ""))) != result.get("script_sha256")):
        raise RuntimeError("compiler result contract")
    compiler_stdout = args.compiler_stdout.read_text(); compiler_stderr = args.compiler_stderr.read_text()
    engine_stdout = args.engine_stdout.read_text(); engine_stderr = args.engine_stderr.read_text()
    for token in ("PASS-A1-GRADE19-ORBIT-UNIT-V36-COMPILER", "V36_WEIGHT19_VARIABLES=0"):
        if compiler_stdout.count(token) != 1:
            raise RuntimeError(("compiler stdout", token))
    for token in ("V36_OLD_BASIS_CONTROL=1", "V36_NF_NONZERO=1", "V36_UNIT_IDEAL=1",
                  "PASS_A1_GRADE19_ORBIT_UNIT_V36"):
        if engine_stdout.count(token) != 1:
            raise RuntimeError(("engine stdout", token))
    for stderr in (compiler_stderr, engine_stderr):
        if stderr.count("Command being timed:") != 1 or stderr.count("Exit status: 0") != 1:
            raise RuntimeError("resource contract")
    diagnostics = compiler_stdout + compiler_stderr + engine_stdout + engine_stderr
    if any(token in diagnostics for token in ("FAIL_", "?", "error occurred", "Killed", "out of memory")):
        raise RuntimeError("diagnostic token")
    nf_path = Path(result["nf_path"]); basis_path = Path(result["final_basis_path"])
    if not nf_path.read_text().strip() or not basis_path.read_text().strip():
        raise RuntimeError("empty engine artifact")
    final = {
        "status": "PASS-A1-GRADE19-ORBIT-UNIT-V36", "characteristic": args.characteristic,
        "weight19_receivers": 0, "normal_form_nonzero": True, "unit_ideal": True,
        "compile_result_sha256": digest(args.compile_result), "script_sha256": result["script_sha256"],
        "normal_form_sha256": digest(nf_path), "basis_sha256": digest(basis_path),
        "compiler_stdout_sha256": digest(args.compiler_stdout), "compiler_stderr_sha256": digest(args.compiler_stderr),
        "engine_stdout_sha256": digest(args.engine_stdout), "engine_stderr_sha256": digest(args.engine_stderr),
        "scope": result["scope"],
    }
    args.output.write_text(json.dumps(final, sort_keys=True, indent=2) + "\n")
    print("PASS-A1-GRADE19-ORBIT-UNIT-V36-VALIDATOR")


if __name__ == "__main__":
    main()
