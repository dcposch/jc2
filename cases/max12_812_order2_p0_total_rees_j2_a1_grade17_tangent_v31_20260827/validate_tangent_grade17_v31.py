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
    cli.add_argument("--result", type=Path, required=True)
    cli.add_argument("--stdout", type=Path, required=True)
    cli.add_argument("--stderr", type=Path, required=True)
    cli.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    cli.add_argument("--output", type=Path, required=True)
    args = cli.parse_args()
    result = json.loads(args.result.read_text())
    if (
        result.get("status") != "PASS-A1-GRADE17-TANGENT-V31"
        or result.get("characteristic") != args.characteristic
        or result.get("rows") != 56
        or result.get("old_rows") != 49
        or result.get("new_rows") != 7
        or result.get("outcome") not in {"consistent", "inconsistent"}
        or result.get("fixed_coordinate") != {"a1": [48, 1]}
        or result.get("grade17_residuals_q", {}).get("Tg17_5") != [-20736, 1]
        or any(result.get("grade17_residuals_q", {}).get(f"Tg17_{row}") != [0, 1]
               for row in (1, 2, 3, 4, 6, 7))
    ):
        raise RuntimeError("result contract")
    stdout = args.stdout.read_text(); stderr = args.stderr.read_text()
    required = ("PASS-A1-GRADE17-TANGENT-V31", f"OUTCOME={result['outcome']}",
                f"OLD_RANK={result['old_rank']}", f"FULL_RANK={result['rank']}")
    if any(stdout.count(token) != 1 for token in required):
        raise RuntimeError("stdout contract")
    if stderr.count("Command being timed:") != 1 or stderr.count("Exit status: 0") != 1:
        raise RuntimeError("resource stderr")
    if any(token in stdout or token in stderr for token in ("Traceback", "FAIL_", "Killed", "out of memory")):
        raise RuntimeError("diagnostic token")
    final = {
        "status": "PASS-A1-GRADE17-TANGENT-V31-VALIDATOR",
        "characteristic": args.characteristic,
        "outcome": result["outcome"],
        "old_rank": result["old_rank"],
        "rank": result["rank"],
        "result_sha256": digest(args.result),
        "stdout_sha256": digest(args.stdout),
        "resource_stderr_sha256": digest(args.stderr),
    }
    args.output.write_text(json.dumps(final, sort_keys=True, indent=2) + "\n")
    print("PASS-A1-GRADE17-TANGENT-V31-VALIDATOR")


if __name__ == "__main__":
    main()

