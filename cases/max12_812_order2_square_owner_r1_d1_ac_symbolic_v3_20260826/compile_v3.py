#!/usr/bin/env python3
"""Compile V3 by renaming three Singular identifiers containing `_or`."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import platform
import subprocess
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V2 = ROOT / "cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_v2_20260826/compile_v2.py"
V2_FREEZE = ROOT / "cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_v2_20260826/FREEZE.sha256"
PINS = {
    V2: "8e25443c466c8030b7ef04b70556c3ea2bb1e6c000c9fdee45296ae13d02222b",
    V2_FREEZE: "6851ecc72c3235e1e1886c888cf14014a6f36a0aa464bef8c8b7facd61ef63f5",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only r1/d1 V3 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only r1/d1 V3 compiler refused non-Amazon host")
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
        if digest(source) != expected:
            fail(("frozen V2 pin mismatch", str(source)))
    output = args.output.resolve()
    if output.exists():
        fail("V3 output already exists")
    scratch = output.parent / (output.name + "_frozen_v2")
    subprocess.run(
        [sys.executable, str(V2), str(scratch), "--characteristic", str(args.characteristic)],
        check=True,
        env=os.environ.copy(),
    )
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    v2_input = scratch / f"square_r1_d1_ac_v2_{label}.sing"
    text = v2_input.read_text()
    replacements = {
        "D1AC_or15": ("D1ACplus15", 12),
        "D1AC_or16": ("D1ACplus16", 12),
        "D1AC_orient": ("D1ACorientation", 3),
    }
    counts = {}
    for old, (new, expected) in replacements.items():
        count = text.count(old)
        if count != expected:
            fail(("unexpected V2 identifier count", old, count, expected))
        text = text.replace(old, new)
        counts[old] = count
    output.mkdir(parents=True)
    target = output / f"square_r1_d1_ac_v3_{label}.sing"
    target.write_text(text)
    payload = {
        "status": "PASS-R1-D1-AC-V3-COMPILER",
        "scope": "IDENTIFIER_ONLY_REPAIR_R1_AND_D1_UNIQUE_AC_NO_SQUARE_OR_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "v2_compiler_sha256": digest(V2),
        "v2_input_sha256": digest(v2_input),
        "replacement_counts": counts,
        "input_sha256": digest(target),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
