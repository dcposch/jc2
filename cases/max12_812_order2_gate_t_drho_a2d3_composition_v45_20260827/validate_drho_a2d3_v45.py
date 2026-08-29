#!/usr/bin/env python3
from __future__ import annotations

import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import platform


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("--result", type=Path, required=True)
    cli.add_argument("--compiler-stdout", type=Path, required=True)
    cli.add_argument("--compiler-stderr", type=Path, required=True)
    cli.add_argument("--output", type=Path, required=True)
    args = cli.parse_args()
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if (platform.system() != "Linux" or not vendor.is_file()
            or vendor.read_text().strip() != "Amazon EC2"
            or not os.environ.get("JC2_REGISTERED_AWS_LANE", "")):
        raise RuntimeError("registered AWS validator required")
    result = json.loads(args.result.read_text())
    if (
        result.get("status") != "PASS-KGT-DRHO-UAC-A2D3-V45-COMPILER"
        or result.get("contact") != {"ord_A": 2, "ord_C": 5, "ord_R_floor": 3, "d": 3, "G": 17, "T": 20}
        or result.get("g20_custody", {}).get("v44r3_crosslane_sha256") != "6b3f87e68cd30fe9cb35934bad4fa8cebd1ad0181d5212aa7165ee728f6567bb"
        or result.get("derived_maxima") != {"p": 3, "A": 3, "C": 3, "R": 1, "k10": 2, "k6": 0, "k2": 0}
        or result.get("pre_G_zero_coefficients") != 119
        or result.get("total_D1_coefficient_equalities_by_deck") != {
            "rho_to_minus_lam": 147, "rho_to_plus_lam": 147,
        }
        or result.get("total_D1_coefficient_equalities") != 294
        or result.get("deck_row_hash_agreement") is not True
        or len(result.get("mapped_row_window_sha256", {})) != 14
        or result.get("D1_B23", {}).get("inventory", {}).get("T") != 20
        or result.get("orientations", {}).get("terminal_residue") != "(3/2)*rho^2*cv^2"
        or "PENDING HOSTILE REVIEW" not in result.get("outcome", "")
    ):
        raise RuntimeError("result contract")
    stdout = args.compiler_stdout.read_text()
    for token in (
        "PASS-KGT-DRHO-UAC-A2D3-V45-COMPILER", "PRE_G_ZERO=119",
        "TOTAL_D1_EQUALITIES=294", "TOTAL_D1_EQUALITIES_PER_DECK=147",
        "BOTH_ORIENTATIONS=1",
        "TERMINAL_RESIDUE=3/2*rho^2*cv^2",
    ):
        if stdout.count(token) != 1:
            raise RuntimeError(("stdout token", token))
    stderr = args.compiler_stderr.read_text()
    if stderr.count("Command being timed:") != 1 or stderr.count("Exit status: 0") != 1:
        raise RuntimeError("resource transcript")
    if any(token in stdout or token in stderr for token in ("Traceback", "FAIL_", "Killed", "out of memory", "error occurred")):
        raise RuntimeError("diagnostic token")
    final = {
        "status": "PASS-KGT-DRHO-UAC-A2D3-V45",
        "host": platform.node(),
        "compiler_result_sha256": digest(args.result),
        "mapped_row_window_sha256": result["mapped_row_window_sha256"],
        "outcome": result["outcome"],
    }
    args.output.write_text(json.dumps(final, sort_keys=True, indent=2) + "\n")
    print("PASS-KGT-DRHO-UAC-A2D3-V45-VALIDATOR")


if __name__ == "__main__":
    main()
