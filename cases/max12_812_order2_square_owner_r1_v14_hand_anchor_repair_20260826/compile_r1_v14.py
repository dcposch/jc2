#!/usr/bin/env python3
"""Compile frozen V13 and move its hand check after the remainder declarations."""

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
V13 = ROOT / "cases/max12_812_order2_square_owner_r1_v13_standard_basis_repair_20260826/compile_r1_v13.py"
V13_FREEZE = ROOT / "cases/max12_812_order2_square_owner_r1_v13_standard_basis_repair_20260826/FREEZE.sha256"
PINS = {
    V13: "0ac6ca00672b7cd77103f70e7c9008946830d4d2118f40836cdd6fbe96bd2207",
    V13_FREEZE: "0c921ece723add43c416bf978e3838ca1cf6a0a30967fab74bda4d20061c7c17",
}

HAND = "\n".join([
    "poly R1_e1_hand=b1*(3*b0^2-(p/2)*b1^2);",
    "poly R1_e0_hand=b0*(b0^2-(3*p/2)*b1^2);",
    "int R1_hand_rem=(R1_e1-R1_e1_hand==0 && R1_e0-R1_e0_hand==0);",
    'print("R1_REMAINDER_FORMULA="+string(R1_hand_rem));',
    'print("R1_RADICAL_STANDARDIZED=1");',
    'if (R1_hand_rem!=1) { print("R1_FAIL=HAND_REMAINDER"); quit; }',
])
DECL = "poly R1_e1=diff(R1_rem,z); poly R1_e0=subst(R1_rem,z,0);"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only r1 V14 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only r1 V14 compiler refused non-Amazon host")
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
        fail("V14 output already exists")
    scratch = output.parent / (output.name + "_frozen_v13")
    subprocess.run(
        [sys.executable, str(V13), str(scratch), "--characteristic", str(args.characteristic)],
        check=True,
        env=os.environ.copy(),
    )
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    source = scratch / f"square_r1_v13_{label}.sing"
    text = source.read_text()
    if text.count(HAND) != 1 or text.count(DECL) != 1:
        fail(("unexpected V13 anchors", text.count(HAND), text.count(DECL)))
    text = text.replace(HAND + "\n", "")
    text = text.replace(DECL, DECL + "\n" + HAND)

    output.mkdir(parents=True)
    target = output / f"square_r1_v14_{label}.sing"
    target.write_text(text)
    payload = {
        "status": "PASS-R1-V14-HAND-ANCHOR-REPAIR-COMPILER",
        "scope": "R1_GRADE13_ONLY_NO_D1_SQUARE_OR_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "v13_compiler_sha256": digest(V13),
        "v13_r1_input_sha256": digest(source),
        "v14_r1_input_sha256": digest(target),
        "removed_hand_block_count": 1,
        "inserted_after_declaration_count": 1,
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()

