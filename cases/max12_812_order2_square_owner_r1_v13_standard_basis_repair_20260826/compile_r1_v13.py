#!/usr/bin/env python3
"""Compile the frozen V12 r=1 source and repair only its radical GB use."""

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
V12 = ROOT / "cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_v12_recurrence_products_20260826/compile_v12_recurrence_products.py"
V12_FREEZE = ROOT / "cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_v12_recurrence_products_20260826/FREEZE.sha256"
ERRATUM = ROOT / "xmodel/max12-812-order2-square-r1-d1-v12-source-support-erratum-20260826.md"
REVIEW = ROOT / "xmodel/max12-812-order2-square-r1-d1-v12-hostile-review-grok-20260826.md"
PINS = {
    V12: "cb1b07bb679c1149bc2671c2ed88417352c0708787f8362756ed3ffb12d3a88a",
    V12_FREEZE: "decc00a91c952354902da2eeeeac6eb9c7fdc06748bf5f96957f45617e07743a",
    ERRATUM: "997dda081223d99283bff92851e7da8bc260b7b3e52ff89b97fb0a50c817a114",
    REVIEW: "509c9edf1c613fa4ff997d3da4acbfeccd7e0895fd76e2f471fad37d90ec15aa",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only r1 V13 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only r1 V13 compiler refused non-Amazon host")
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
            fail(("frozen pin mismatch", str(source), actual, expected))

    output = args.output.resolve()
    if output.exists():
        fail("V13 output already exists")
    scratch = output.parent / (output.name + "_frozen_v12")
    subprocess.run(
        [sys.executable, str(V12), str(scratch), "--characteristic", str(args.characteristic)],
        check=True,
        env=os.environ.copy(),
    )
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    source = scratch / f"square_r1_v12_{label}.sing"
    text = source.read_text()

    old_rad = "ideal R1_rad=radical(R1_I);"
    new_rad = "ideal R1_rad_raw=radical(R1_I); ideal R1_rad=std(R1_rad_raw);"
    if text.count(old_rad) != 1:
        fail(("unexpected radical anchor count", text.count(old_rad)))
    text = text.replace(old_rad, new_rad)

    anchor = 'print("R1_DENOMINATOR_RECURRENCE="+string(R1_rec));'
    if text.count(anchor) != 1:
        fail(("unexpected remainder marker anchor count", text.count(anchor)))
    hand = "\n".join([
        "poly R1_e1_hand=b1*(3*b0^2-(p/2)*b1^2);",
        "poly R1_e0_hand=b0*(b0^2-(3*p/2)*b1^2);",
        "int R1_hand_rem=(R1_e1-R1_e1_hand==0 && R1_e0-R1_e0_hand==0);",
        'print("R1_REMAINDER_FORMULA="+string(R1_hand_rem));',
        'print("R1_RADICAL_STANDARDIZED=1");',
        'if (R1_hand_rem!=1) { print("R1_FAIL=HAND_REMAINDER"); quit; }',
    ])
    text = text.replace(anchor, hand + "\n" + anchor)

    output.mkdir(parents=True)
    target = output / f"square_r1_v13_{label}.sing"
    target.write_text(text)
    payload = {
        "status": "PASS-R1-V13-STANDARD-BASIS-REPAIR-COMPILER",
        "scope": "R1_GRADE13_ONLY_NO_D1_SQUARE_OR_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "v12_compiler_sha256": digest(V12),
        "v12_r1_input_sha256": digest(source),
        "v13_r1_input_sha256": digest(target),
        "radical_replacement_count": 1,
        "hand_remainder_insertion_count": 1,
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
