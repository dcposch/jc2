#!/usr/bin/env python3
"""Compile V5 by applying only proven-safe Singular identifier names."""

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
V4 = ROOT / "cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_v4_20260826/compile_v4.py"
V4_FREEZE = ROOT / "cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_v4_20260826/FREEZE.sha256"
PINS = {
    V4: "1ff4e5de92c9107f0f021d11301247ea2f338d154e56053345e8cb39c70fd589",
    V4_FREEZE: "2fb0167ef9f26bac00192ef58ee3e64d3d8b6be025a5dca6928e146e045edfa5",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only r1/d1 V5 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only r1/d1 V5 compiler refused non-Amazon host")
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
            fail(("frozen V4 pin mismatch", str(source)))
    output = args.output.resolve()
    if output.exists():
        fail("V5 output already exists")
    scratch = output.parent / (output.name + "_frozen_v4")
    subprocess.run(
        [sys.executable, str(V4), str(scratch), "--characteristic", str(args.characteristic)],
        check=True,
        env=os.environ.copy(),
    )
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    v4_input = scratch / f"square_r1_d1_ac_v4_{label}.sing"
    source_text = v4_input.read_text()
    replacements = {
        "rootlambda987654": ("rtx", 17),
        "D1ACxq15": ("D1AC_tmp15", 12),
        "D1ACxq16": ("D1AC_tmp16", 12),
        "D1ACxqflag": ("D1AC_flag", 3),
    }
    counts = {}
    for old, (new, expected) in replacements.items():
        count = source_text.count(old)
        if count != expected:
            fail(("unexpected V4 identifier count", old, count, expected))
        source_text = source_text.replace(old, new)
        counts[old] = count
    output.mkdir(parents=True)
    target = output / f"square_r1_d1_ac_v5_{label}.sing"
    target.write_text(source_text)
    payload = {
        "status": "PASS-R1-D1-AC-V5-COMPILER",
        "scope": "IDENTIFIER_ONLY_REPAIR_R1_AND_D1_UNIQUE_AC_NO_SQUARE_OR_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "v4_compiler_sha256": digest(V4),
        "v4_input_sha256": digest(v4_input),
        "replacement_counts": counts,
        "input_sha256": digest(target),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
