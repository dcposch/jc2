#!/usr/bin/env python3
"""Compile frozen a8 V1 and add only the omitted formal k60 ring symbol."""

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
V1_DIR = ROOT / "cases/max12_812_order2_square_owner_d1_a8_k6_mu2_fullsupport_20260826"
V1 = V1_DIR / "compile_a8.py"
V1_FREEZE = V1_DIR / "FREEZE.sha256"
V1_NEGATIVE = V1_DIR / "RESULT_NEGATIVE_CONTROL.md"
PINS = {
    V1: "0230ca443d49e47b5d6ebae8c0f8a88d31a793d13b1df59e3698e166226d177b",
    V1_FREEZE: "c18bdd9f55a108470ef166e6c0cfa243ab61b63f45742537046fdb6e583b5dc8",
    V1_NEGATIVE: "be3d6843a27db31ee7e844fe1edea1e2f6fb7b65ba9b7c8f2289ff28e3441ed2",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only a8 V2 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only a8 V2 compiler refused non-Amazon host")
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
    subprocess.run(
        [sys.executable, str(V1), str(scratch), "--characteristic", str(args.characteristic)],
        check=True,
        env=os.environ.copy(),
    )
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    source_input = scratch / f"square_d1_a8_k6_mu2_{label}.sing"
    text = source_input.read_text()
    old = "b0,b1,k0,k61,k62,k2load"
    new = "b0,b1,k0,k60,k61,k62,k2load"
    count = text.count(old)
    if count != 6:
        fail(("unexpected omitted-k60 declaration/map count", count, 6))
    text = text.replace(old, new)
    if old in text or text.count(new) != 6:
        fail("V2 formal-k60 replacement failed")
    output.mkdir(parents=True)
    target = output / f"square_d1_a8_k6_mu2_v2_{label}.sing"
    target.write_text(text)
    payload = {
        "status": "PASS-D1-A8-K6-MU2-V2-K60SYMBOL-COMPILER",
        "scope": "SIX_FORMAL_K60_RING_MAP_INSERTIONS_ONLY_NO_A9_OR_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "v1_compiler_sha256": digest(V1),
        "replacement_count": count,
        "input_sha256": digest(target),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()

