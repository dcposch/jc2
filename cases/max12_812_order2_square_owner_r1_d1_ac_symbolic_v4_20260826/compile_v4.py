#!/usr/bin/env python3
"""Compile V4 by replacing V3 identifiers containing the reserved word plus."""

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
V3 = ROOT / "cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_v3_20260826/compile_v3.py"
V3_FREEZE = ROOT / "cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_v3_20260826/FREEZE.sha256"
PINS = {
    V3: "666ecf84f414106c705e9d6db620762f268a4569d5ba2674f0d3b712abeee8c2",
    V3_FREEZE: "de3ae40037413d6bfd54468c946aa5defd8c58b556d6bb008bb635898e0083ea",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only r1/d1 V4 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only r1/d1 V4 compiler refused non-Amazon host")
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
            fail(("frozen V3 pin mismatch", str(source)))
    output = args.output.resolve()
    if output.exists():
        fail("V4 output already exists")
    scratch = output.parent / (output.name + "_frozen_v3")
    subprocess.run(
        [sys.executable, str(V3), str(scratch), "--characteristic", str(args.characteristic)],
        check=True,
        env=os.environ.copy(),
    )
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    v3_input = scratch / f"square_r1_d1_ac_v3_{label}.sing"
    source_text = v3_input.read_text()
    replacements = {
        "D1ACplus15": ("D1ACxq15", 12),
        "D1ACplus16": ("D1ACxq16", 12),
        "D1ACorientation": ("D1ACxqflag", 3),
    }
    counts = {}
    for old, (new, expected) in replacements.items():
        count = source_text.count(old)
        if count != expected:
            fail(("unexpected V3 identifier count", old, count, expected))
        source_text = source_text.replace(old, new)
        counts[old] = count
    output.mkdir(parents=True)
    target = output / f"square_r1_d1_ac_v4_{label}.sing"
    target.write_text(source_text)
    payload = {
        "status": "PASS-R1-D1-AC-V4-COMPILER",
        "scope": "IDENTIFIER_ONLY_REPAIR_R1_AND_D1_UNIQUE_AC_NO_SQUARE_OR_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "v3_compiler_sha256": digest(V3),
        "v3_input_sha256": digest(v3_input),
        "replacement_counts": counts,
        "input_sha256": digest(target),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
