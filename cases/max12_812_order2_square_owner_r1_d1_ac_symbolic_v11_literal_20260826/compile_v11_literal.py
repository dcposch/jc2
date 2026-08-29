#!/usr/bin/env python3
"""Compile V10 and replace only the rec15/rec16 string serialization."""

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
V10 = ROOT / "cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_v10_maps_20260826/compile_v10_maps.py"
V10_FREEZE = ROOT / "cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_v10_maps_20260826/FREEZE.sha256"
PINS = {
    V10: "eaac25d2fedd47a8ff84e0a3d765ba476d4cc4ad29c2adee33ded7e8cdcc9c26",
    V10_FREEZE: "2366fb52aceb707a031900c0f276643f4e41a32624cca12f5c549230f1c32aff",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only r1/d1 V11 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only r1/d1 V11 compiler refused non-Amazon host")
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
            fail(("frozen V10 pin mismatch", str(source), actual, expected))

    output = args.output.resolve()
    if output.exists():
        fail("V11 output already exists")
    scratch = output.parent / (output.name + "_frozen_v10")
    subprocess.run(
        [sys.executable, str(V10), str(scratch), "--characteristic", str(args.characteristic)],
        check=True,
        env=os.environ.copy(),
    )
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    r1_v10 = scratch / f"square_r1_v10_{label}.sing"
    d1_v10 = scratch / f"square_d1_ac_v10_{label}.sing"
    text = d1_v10.read_text()
    old = "\n".join(
        [
            'print("D1AC_DENOMINATOR_RECURRENCE_G15="+string(D1AC_rec15));',
            'print("D1AC_DENOMINATOR_RECURRENCE_G16="+string(D1AC_rec16));',
        ]
    )
    new = "\n".join(
        [
            'if (D1AC_rec15!=1 || D1AC_rec16!=1) { print("D1AC_FAIL=RECURRENCE_SERIALIZATION_GUARD"); quit; }',
            'print("D1AC_DENOMINATOR_RECURRENCE_G15=1");',
            'print("D1AC_DENOMINATOR_RECURRENCE_G16=1");',
        ]
    )
    if text.count(old) != 1:
        fail(("V10 recurrence print block missing or nonunique", text.count(old)))
    text = text.replace(old, new)
    if "string(D1AC_rec15)" in text or text.count("D1AC_FAIL=RECURRENCE_SERIALIZATION_GUARD") != 1:
        fail("V11 serialization repair failed")

    output.mkdir(parents=True)
    r1_target = output / f"square_r1_v11_{label}.sing"
    d1_target = output / f"square_d1_ac_v11_{label}.sing"
    r1_target.write_bytes(r1_v10.read_bytes())
    d1_target.write_text(text)
    payload = {
        "status": "PASS-R1-D1-AC-V11-LITERAL-COMPILER",
        "scope": "RECURRENCE_SERIALIZATION_ONLY_R1_AND_D1_UNIQUE_AC_NO_SQUARE_OR_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "v10_compiler_sha256": digest(V10),
        "r1_input_sha256": digest(r1_target),
        "d1_input_sha256": digest(d1_target),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
