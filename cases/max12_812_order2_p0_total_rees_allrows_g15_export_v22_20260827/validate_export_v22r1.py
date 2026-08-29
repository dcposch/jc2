#!/usr/bin/env python3
"""Fail-closed validator for repaired V22R1."""

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
    paths = result.get("coefficient_paths")
    hashes = result.get("coefficient_sha256")
    controls = result.get("source_sensitivity_control_details")
    deferrals = result.get("serialization_only_bridge_deferrals")
    expected_sections = {
        "CS0": {}, "Z00": {}, "A00": {"Tg15_6": "(-1/16)"},
        "A10": {"Tg15_3": "(-1/16)", "Tg15_5": "(-3/32)*rho^2", "Tg15_7": "(-3/128)*rho^4"},
    }
    if (
        result.get("status") != "PASS-TOTAL-REES-ALLROWS-G15-EXPORT-V22R1-COMPILER"
        or result.get("characteristic") != args.characteristic
        or result.get("tail_rows_checked") != 7
        or result.get("tail_terms_checked") != 569
        or result.get("old_coefficient_exact_polynomial_bridges") != 35
        or result.get("rho_even_coefficients") != 7
        or result.get("sigma_homogeneous_coefficients") != 7
        or result.get("source_sensitivity_controls") != 7
        or result.get("section_nonzero_residuals_exact_qrho") != expected_sections
        or not isinstance(paths, dict) or len(paths) != 7
        or not isinstance(hashes, dict) or set(hashes) != set(paths)
        or not isinstance(controls, dict) or set(controls) != {str(row) for row in range(1, 8)}
        or not isinstance(deferrals, list) or not 1 <= len(deferrals) <= 35
        or len({tuple(item) for item in deferrals}) != len(deferrals)
        or any(result.get("coefficient_term_counts", {}).get(f"Tg15_{row}", 0) <= 0 for row in range(1, 8))
    ):
        raise RuntimeError("compiler-result contract")
    for name, raw_path in paths.items():
        if digest(Path(raw_path)) != hashes[name]:
            raise RuntimeError(("coefficient hash", name))
    control_script = Path(result["control_script"])
    if digest(control_script) != result.get("control_script_sha256"):
        raise RuntimeError("control-script hash")

    stdout = args.stdout.read_text()
    stderr = args.stderr.read_text()
    if stderr.count("Command being timed:") != 1 or stderr.count("Exit status: 0") != 1:
        raise RuntimeError(("resource stderr", stderr[-2000:]))
    if any(token in stdout or token in stderr for token in ("FAIL_", "?", "error occurred", "Killed", "out of memory")):
        raise RuntimeError("diagnostic token")
    required = ["V22_QRING_DISABLED=1", "PASS_TOTAL_REES_ALLROWS_G15_EXPORT_V22"]
    required += [f"V22_OLD_BRIDGE_Tg{grade}_{row}=1" for grade in (10, 11, 12, 13, 14) for row in range(1, 8)]
    required += [f"V22_NONZERO_RHO_EVEN_Tg15_{row}=1" for row in range(1, 8)]
    required += [
        f"V22_SOURCE_SENSITIVITY_Tg{controls[str(row)]['grade']}_{row}=1"
        for row in range(1, 8)
    ]
    for token in required:
        if stdout.count(token) != 1:
            raise RuntimeError(("required token", token, stdout.count(token)))

    final = {
        "status": "PASS-TOTAL-REES-ALLROWS-G15-EXPORT-V22R1",
        "characteristic": args.characteristic,
        "compiler_result_sha256": digest(args.compiler_result),
        "coefficient_sha256": hashes,
        "control_script_sha256": digest(control_script),
        "stdout_sha256": digest(args.stdout),
        "resource_stderr_sha256": digest(args.stderr),
        "coefficient_term_counts": result["coefficient_term_counts"],
        "coefficient_variable_supports": result["coefficient_variable_supports"],
        "contributing_tail_counts": result["contributing_tail_counts"],
        "section_nonzero_residuals_exact_qrho": expected_sections,
        "old_coefficient_exact_polynomial_bridges": 35,
        "serialization_only_bridge_deferrals": deferrals,
    }
    args.output.write_text(json.dumps(final, sort_keys=True, indent=2) + "\n")
    print(json.dumps(final, sort_keys=True))


if __name__ == "__main__":
    main()

