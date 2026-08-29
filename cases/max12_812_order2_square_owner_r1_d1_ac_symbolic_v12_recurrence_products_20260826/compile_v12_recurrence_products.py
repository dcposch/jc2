#!/usr/bin/env python3
"""Compile V11 and expand powers only in the N16/recurrence block."""

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
V11 = ROOT / "cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_v11_literal_20260826/compile_v11_literal.py"
V11_FREEZE = ROOT / "cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_v11_literal_20260826/FREEZE.sha256"
PINS = {
    V11: "f766955473256d5c9235740c8755c9f917c03572ab0d74c6e0569a0f3d0e6818",
    V11_FREEZE: "24774ad52b6c0dd160e04a9c53be36ec9bc04238960bb9606ceb7632dc1e8e80",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only r1/d1 V12 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only r1/d1 V12 compiler refused non-Amazon host")
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
            fail(("frozen V11 pin mismatch", str(source), actual, expected))

    output = args.output.resolve()
    if output.exists():
        fail("V12 output already exists")
    scratch = output.parent / (output.name + "_frozen_v11")
    subprocess.run(
        [sys.executable, str(V11), str(scratch), "--characteristic", str(args.characteristic)],
        check=True,
        env=os.environ.copy(),
    )
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    r1_v11 = scratch / f"square_r1_v11_{label}.sing"
    d1_v11 = scratch / f"square_d1_ac_v11_{label}.sing"
    text = d1_v11.read_text()
    start = "poly D1AC_N15="
    end = "ring Rd1eval="
    if text.count(start) != 1 or text.count(end) != 1:
        fail("V11 recurrence-region anchors missing or nonunique")
    prefix, remainder = text.split(start, 1)
    block, suffix = remainder.split(end, 1)
    block = start + block
    replacements = {
        "z^3": ("z*z*z", 1),
        "z^2": ("z*z", 1),
        "p^2": ("p*p", 3),
    }
    counts = {}
    for old, (new, expected) in replacements.items():
        count = block.count(old)
        if count != expected:
            fail(("unexpected recurrence power count", old, count, expected))
        block = block.replace(old, new)
        counts[old] = count
    text = prefix + block + end + suffix

    output.mkdir(parents=True)
    r1_target = output / f"square_r1_v12_{label}.sing"
    d1_target = output / f"square_d1_ac_v12_{label}.sing"
    r1_target.write_bytes(r1_v11.read_bytes())
    d1_target.write_text(text)
    payload = {
        "status": "PASS-R1-D1-AC-V12-RECURRENCE-PRODUCTS-COMPILER",
        "scope": "RECURRENCE_SYNTAX_ONLY_R1_AND_D1_UNIQUE_AC_NO_SQUARE_OR_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "v11_compiler_sha256": digest(V11),
        "replacement_counts": counts,
        "r1_input_sha256": digest(r1_target),
        "d1_input_sha256": digest(d1_target),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
