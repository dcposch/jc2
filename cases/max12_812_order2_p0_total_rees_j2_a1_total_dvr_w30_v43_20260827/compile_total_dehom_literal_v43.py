#!/usr/bin/env python3
"""Additive literal-alphabet wrapper for the selected total-t dehom compiler.

The selected seventeen rows do not themselves contain the sole general-only
variable ez9 (it occurs in Tg19_2).  The reduced producer is mathematically
equivalent, but this wrapper explicitly retains ez9 as a spectator in the
65-variable a1=1 total ring and eliminates it with the other variables.
"""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys


HERE = Path(__file__).resolve().parent
REDUCED = HERE / "compile_total_dehom_eliminant_v43.py"
REDUCED_SHA256 = "dc1288e67260143a05964961c8a0a954d8228f4d3bc8a3c3e0eb801aeaca0c96"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("output", type=Path)
    cli.add_argument("--mode", choices=("exact", "modp"), required=True)
    cli.add_argument("--prime", type=int, choices=(65519, 65521), required=True)
    cli.add_argument("--phase", choices=("eliminate", "lift"), required=True)
    args = cli.parse_args()
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if "_literal_" not in tag:
        fail("literal-lane tag required")
    if digest(REDUCED) != REDUCED_SHA256:
        fail(("reduced producer hash", digest(REDUCED), REDUCED_SHA256))
    output = args.output.resolve()
    command = [
        sys.executable, str(REDUCED), str(output), "--mode", args.mode,
        "--prime", str(args.prime), "--phase", args.phase,
    ]
    subprocess.run(command, check=True)
    result_path = output / "compiler_result.json"
    result = json.loads(result_path.read_text())
    active = result["active_variables_after_dehom"]
    if (len(active) != 64 or "ez9" in active
            or result["general_only_variables"] != ["ez9"]
            or result["total_positive_variables"] != 66):
        fail("reduced selected-row alphabet census")
    literal = sorted([*active, "ez9"])
    if len(literal) != 65:
        fail("literal dehom alphabet census")
    characteristic = 0 if args.mode == "exact" else args.prime
    script_path = Path(result["singular_script"])
    script = script_path.read_text()
    old_ring = (f"ring R={characteristic},({','.join([*active, 't'])}),"
                f"(dp({len(active)}),dp(1));")
    new_ring = (f"ring R={characteristic},({','.join([*literal, 't'])}),"
                f"(dp({len(literal)}),dp(1));")
    old_eliminate = f"ideal E=eliminate(I,{'*'.join(active)});"
    new_eliminate = f"ideal E=eliminate(I,{'*'.join(literal)});"
    if script.count(old_ring) != 1 or script.count(old_eliminate) != 1:
        fail("reduced script rewrite anchors")
    script = script.replace(old_ring, new_ring).replace(old_eliminate, new_eliminate)
    script_path.write_text(script)
    result.update({
        "status": "PASS-A1-TOTAL-DVR-W30-V43-TOTAL-DEHOM-LITERAL-COMPILER",
        "scope": (result["scope"] + "; full 65-variable a1=1 total alphabet "
                  "with ez9 retained as an explicit spectator"),
        "reduced_dehom_compiler_sha256": REDUCED_SHA256,
        "literal_dehom_ring_variables": literal,
        "literal_dehom_ring_variable_count": len(literal),
        "selected_row_spectator_variables": ["ez9"],
        "singular_script_sha256": digest(script_path),
    })
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("PASS-A1-TOTAL-DVR-W30-V43-TOTAL-DEHOM-LITERAL-COMPILER")
    print(f"RESULT_SHA256={digest(result_path)}")


if __name__ == "__main__":
    main()
