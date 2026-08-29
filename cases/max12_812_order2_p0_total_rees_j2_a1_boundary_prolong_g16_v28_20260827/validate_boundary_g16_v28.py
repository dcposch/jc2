#!/usr/bin/env python3
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--result", type=Path, required=True)
    parser.add_argument("--stdout", type=Path, required=True)
    parser.add_argument("--stderr", type=Path, required=True)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = json.loads(args.result.read_text())
    if (
        result.get("status") != "PASS-A1-BOUNDARY-PROLONG-G16-V28-COMPILER"
        or result.get("characteristic") != args.characteristic
        or result.get("tail_rows") != 7
        or result.get("tail_terms") != 569
        or result.get("old_face_bridges") != 42
        or result.get("old_point_zero_rows") != 42
        or result.get("outcome") not in {"consistent", "inconsistent"}
        or not isinstance(result.get("new_variables"), list)
        or not isinstance(result.get("linear_rank"), int)
        or set(result.get("coefficient_paths", {})) != {f"Tg16_{row}" for row in range(1, 8)}
        or set(result.get("affine_paths", {})) != {f"Tg16_{row}" for row in range(1, 8)}
    ):
        raise RuntimeError("result contract")
    for kind in ("coefficient", "affine"):
        for name, raw_path in result[f"{kind}_paths"].items():
            if digest(Path(raw_path)) != result[f"{kind}_sha256"][name]:
                raise RuntimeError((kind, name))
    control = Path(result["control_script"])
    if digest(control) != result["control_script_sha256"]:
        raise RuntimeError("control hash")
    stdout = args.stdout.read_text()
    stderr = args.stderr.read_text()
    if stderr.count("Command being timed:") != 1 or stderr.count("Exit status: 0") != 1:
        raise RuntimeError("resource stderr")
    if any(token in stdout or token in stderr for token in ("FAIL_", "?", "error occurred", "Killed", "out of memory")):
        raise RuntimeError("diagnostic token")
    required = ["V28_POINT_CONTROL=1", f"V28_OUTCOME={result['outcome']}", "PASS_A1_BOUNDARY_PROLONG_G16_V28"]
    if result["outcome"] == "consistent":
        required += [f"V28_EXTENSION_Tg16_{row}=1" for row in range(1, 8)]
    else:
        required += ["V28_DUAL=1"]
    for token in required:
        if stdout.count(token) != 1:
            raise RuntimeError(("required token", token, stdout.count(token)))
    final = {
        "status": "PASS-A1-BOUNDARY-PROLONG-G16-V28",
        "characteristic": args.characteristic,
        "outcome": result["outcome"],
        "result_sha256": digest(args.result),
        "control_script_sha256": digest(control),
        "stdout_sha256": digest(args.stdout),
        "resource_stderr_sha256": digest(args.stderr),
        "new_variables": result["new_variables"],
        "linear_rank": result["linear_rank"],
        "grade16_term_counts": result["grade16_term_counts"],
        "grade16_affine_term_counts": result["grade16_affine_term_counts"],
    }
    args.output.write_text(json.dumps(final, sort_keys=True, indent=2) + "\n")
    print("PASS-A1-BOUNDARY-PROLONG-G16-V28-VALIDATOR")
    print(f"OUTCOME={result['outcome']}")
    print(f"RESULT_SHA256={digest(args.result)}")


if __name__ == "__main__":
    main()

