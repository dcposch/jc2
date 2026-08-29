#!/usr/bin/env python3
"""Compile V7 by expanding powers only in the V6 linear-chart block."""

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
V6 = ROOT / "cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_v6_20260826/compile_v6.py"
V6_FREEZE = ROOT / "cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_v6_20260826/FREEZE.sha256"
PINS = {
    V6: "a5e207caeaa33974d20c655a0db476df610d2b0448883e3ec7fdfafa01e6a8df",
    V6_FREEZE: "4902ce6864462f8f8afebf70af76c6378e9acc7490b9336bc1ff6f057ec7cb8d",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only r1/d1 V7 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only r1/d1 V7 compiler refused non-Amazon host")
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
            fail(("frozen V6 pin mismatch", str(source)))
    output = args.output.resolve()
    if output.exists():
        fail("V7 output already exists")
    scratch = output.parent / (output.name + "_frozen_v6")
    subprocess.run(
        [sys.executable, str(V6), str(scratch), "--characteristic", str(args.characteristic)],
        check=True,
        env=os.environ.copy(),
    )
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    v6_input = scratch / f"square_r1_d1_ac_v6_{label}.sing"
    source_text = v6_input.read_text()
    start = "ideal IP=std(ideal("
    end = 'print("D1AC_DENOMINATOR_RECURRENCE_G15="+string(D1AC_rec15));'
    if source_text.count(start) != 1 or source_text.count(end) != 1:
        fail(("V6 chart anchors missing or nonunique", source_text.count(start), source_text.count(end)))
    prefix, rest = source_text.split(start, 1)
    block, suffix = rest.split(end, 1)
    block = start + block
    replacements = {
        "rtx^2": ("rtx*rtx", 6),
        "cv^2": ("cv*cv", 2),
        "theta^2": ("theta*theta", 2),
    }
    counts = {}
    for old, (new, expected) in replacements.items():
        count = block.count(old)
        if count != expected:
            fail(("unexpected V6 chart power count", old, count, expected))
        block = block.replace(old, new)
        counts[old] = count
    source_text = prefix + block + end + suffix
    output.mkdir(parents=True)
    target = output / f"square_r1_d1_ac_v7_{label}.sing"
    target.write_text(source_text)
    payload = {
        "status": "PASS-R1-D1-AC-V7-COMPILER",
        "scope": "EXPONENT_CONTEXT_REPAIR_R1_AND_D1_UNIQUE_AC_NO_SQUARE_OR_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "v6_compiler_sha256": digest(V6),
        "v6_input_sha256": digest(v6_input),
        "replacement_counts": counts,
        "input_sha256": digest(target),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
