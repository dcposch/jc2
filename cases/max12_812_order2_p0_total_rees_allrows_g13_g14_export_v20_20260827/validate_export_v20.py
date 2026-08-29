#!/usr/bin/env python3
"""Fail-closed validator for the V20 all-row grade-13/14 export."""

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
    coefficients = result.get("coefficient_paths")
    hashes = result.get("coefficient_sha256")
    sections = result.get("section_nonzero_residuals_exact_qrho")
    if (
        result.get("status") != "PASS-TOTAL-REES-ALLROWS-G13-G14-EXPORT-V20-COMPILER"
        or result.get("characteristic") != args.characteristic
        or result.get("tail_rows_checked") != 7
        or result.get("tail_terms_checked") != 569
        or result.get("v9_bridges_checked") != 21
        or result.get("v17_byte_bridge") is not True
        or result.get("rho_even_coefficients") != 14
        or len(result.get("source_sensitivity_controls", {})) != 7
        or not isinstance(coefficients, dict) or len(coefficients) != 14
        or not isinstance(hashes, dict) or set(hashes) != set(coefficients)
        or not isinstance(sections, dict) or set(sections) != {"CS0", "A00", "A10", "Z00"}
    ):
        raise RuntimeError("compiler-result contract")
    for name, raw_path in coefficients.items():
        path = Path(raw_path)
        if digest(path) != hashes[name]:
            raise RuntimeError(("coefficient hash mismatch", name))
    control = Path(result["control_script"])
    if digest(control) != result.get("control_script_sha256"):
        raise RuntimeError("control-script hash mismatch")

    stdout = args.stdout.read_text()
    stderr = args.stderr.read_text()
    if stderr.count("Command being timed:") != 1 or stderr.count("Exit status: 0") != 1:
        raise RuntimeError(("resource stderr", stderr[-2000:]))
    if any(token in stdout or token in stderr for token in ("FAIL_", "?", "error occurred", "Killed", "out of memory")):
        raise RuntimeError("diagnostic token")
    required = ["V20_QRING_DISABLED=1", "V20_V17_BRIDGE_Tg14_5=1", "PASS_TOTAL_REES_ALLROWS_G13_G14_EXPORT_V20"]
    required += [f"V20_V9_BRIDGE_Tg{grade}_{row}=1" for grade in (10, 11, 12) for row in range(1, 8)]
    required += [f"V20_RHO_EVEN_Tg{grade}_{row}=1" for grade in (13, 14) for row in range(1, 8)]
    required += [
        f"V20_{'NONZERO' if result['coefficient_term_counts'][f'Tg{grade}_{row}'] else 'ZERO'}_Tg{grade}_{row}=1"
        for grade in (13, 14) for row in range(1, 8)
    ]
    required += [
        f"V20_SOURCE_SENSITIVITY_Tg{control['grade']}_{row}=1"
        for row, control in sorted(result["source_sensitivity_controls"].items(), key=lambda item: int(item[0]))
    ]
    required += [f"V20_SECTION_{section}_NONZERO={len(residuals)}" for section, residuals in sections.items()]
    for token in required:
        if stdout.count(token) != 1:
            raise RuntimeError(("required token", token, stdout.count(token)))

    final = {
        "status": "PASS-TOTAL-REES-ALLROWS-G13-G14-EXPORT-V20",
        "characteristic": args.characteristic,
        "compiler_result_sha256": digest(args.compiler_result),
        "coefficient_sha256": hashes,
        "control_script_sha256": digest(control),
        "stdout_sha256": digest(args.stdout),
        "resource_stderr_sha256": digest(args.stderr),
        "coefficient_term_counts": result["coefficient_term_counts"],
        "section_nonzero_residuals_exact_qrho": sections,
    }
    args.output.write_text(json.dumps(final, sort_keys=True, indent=2) + "\n")
    print(json.dumps(final, sort_keys=True))


if __name__ == "__main__":
    main()

