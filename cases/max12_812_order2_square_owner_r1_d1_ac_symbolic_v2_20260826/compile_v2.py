#!/usr/bin/env python3
"""Compile V2 by collision-free renaming of V1's etale-root identifier."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import platform
import re
import subprocess
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V1 = ROOT / "cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_20260826/compile_r1_d1_ac.py"
V1_FREEZE = ROOT / "cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_20260826/FREEZE.sha256"
PINS = {
    V1: "e024a13d24a11519f70b535d4b47c47c62538a684b8bc71e79216410cd8ecb7c",
    V1_FREEZE: "34b0f3254410e39abfc9843febd3c053f965a30dfa948d9e0367c0fb094611a6",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only r1/d1 V2 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only r1/d1 V2 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    for source, expected in PINS.items():
        actual = digest(source)
        if actual != expected:
            fail(("frozen V1 pin mismatch", str(source), actual, expected))
    output = args.output.resolve()
    if output.exists():
        fail("V2 output already exists")
    scratch = output.parent / (output.name + "_frozen_v1")
    if scratch.exists():
        fail("V1 scratch output already exists")
    subprocess.run(
        [sys.executable, str(V1), str(scratch), "--characteristic", str(args.characteristic)],
        check=True,
        env=os.environ.copy(),
    )
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    v1_input = scratch / f"square_r1_d1_ac_{label}.sing"
    text = v1_input.read_text()
    matches = len(re.findall(r"\blam\b", text))
    if matches != 17:
        fail(("unexpected V1 root-identifier occurrence count", matches, 17))
    repaired = re.sub(r"\blam\b", "rootlambda987654", text)
    if re.search(r"\blam\b", repaired):
        fail("V2 root identifier remained after replacement")
    output.mkdir(parents=True)
    target = output / f"square_r1_d1_ac_v2_{label}.sing"
    target.write_text(repaired)
    payload = {
        "status": "PASS-R1-D1-AC-V2-COMPILER",
        "scope": "IDENTIFIER_ONLY_REPAIR_R1_AND_D1_UNIQUE_AC_NO_SQUARE_OR_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "v1_compiler_sha256": digest(V1),
        "v1_input_sha256": digest(v1_input),
        "replacement_count": matches,
        "input_sha256": digest(target),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
