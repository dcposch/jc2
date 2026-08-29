#!/usr/bin/env python3
"""Fail-closed validator for V17 total row-five export."""

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
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = json.loads(args.compiler_result.read_text())
    if (
        result.get("status") != "PASS-T-CS-ROW5-G14-EXPORT-V17-COMPILER"
        or result.get("characteristic") != args.characteristic
        or result.get("tail_terms_checked") != 89
        or result.get("rho_deck_even") is not True
        or result.get("normalized_odd_specialization") != "-(21/320)*b^5*w^2"
        or result.get("negative_normalization_control") is not True
    ):
        raise RuntimeError("compiler-result contract")
    coefficient = Path(result["coefficient"])
    control = Path(result["control_script"])
    if digest(coefficient) != result.get("coefficient_sha256") or digest(control) != result.get("control_script_sha256"):
        raise RuntimeError("compiled artifact hash mismatch")
    stdout = args.stdout.read_text()
    stderr = args.stderr.read_text()
    if stderr.count("Command being timed:") != 1 or stderr.count("Exit status: 0") != 1:
        raise RuntimeError(("resource stderr", stderr[-2000:]))
    if any(token in stdout or token in stderr for token in ("FAIL_", "?", "error occurred", "Killed", "out of memory")):
        raise RuntimeError("diagnostic token")
    required = (
        "V17_QRING_DISABLED=1",
        "V17_V9_BRIDGE_G10=1",
        "V17_V9_BRIDGE_G11=1",
        "V17_V9_BRIDGE_G12=1",
        "V17_G14_NONZERO=1",
        "V17_RHO_DECK_EVEN=1",
        "V17_NORMALIZED_ODD_SPECIALIZATION=1",
        "V17_NEGATIVE_NORMALIZATION_CONTROL=1",
        "PASS_T_CS_ROW5_G14_EXPORT_V17",
    )
    for token in required:
        if stdout.count(token) != 1:
            raise RuntimeError(("required token", token, stdout.count(token)))
    final = {
        "status": "PASS-T-CS-ROW5-G14-EXPORT-V17",
        "characteristic": args.characteristic,
        "compiler_result_sha256": digest(args.compiler_result),
        "coefficient_sha256": digest(coefficient),
        "control_script_sha256": digest(control),
        "stdout_sha256": digest(args.stdout),
        "resource_stderr_sha256": digest(args.stderr),
        "coefficient_term_count": result["coefficient_term_counts"]["14"],
    }
    args.output.write_text(json.dumps(final, sort_keys=True, indent=2) + "\n")
    print(json.dumps(final, sort_keys=True))


if __name__ == "__main__":
    main()

