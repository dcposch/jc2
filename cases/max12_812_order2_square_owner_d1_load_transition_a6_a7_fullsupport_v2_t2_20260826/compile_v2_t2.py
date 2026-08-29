#!/usr/bin/env python3
"""Compile V1 and repair only the two k6*C tail-alignment factors."""

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
V1 = ROOT / "cases/max12_812_order2_square_owner_d1_load_transition_a6_a7_fullsupport_20260826/compile_load_transition.py"
V1_FREEZE = ROOT / "cases/max12_812_order2_square_owner_d1_load_transition_a6_a7_fullsupport_20260826/FREEZE.sha256"
V1_NEGATIVE = ROOT / "cases/max12_812_order2_square_owner_d1_load_transition_a6_a7_fullsupport_20260826/RESULT_NEGATIVE_CONTROL.md"
PINS = {
    V1: "158ebf84bf8c13143d606b0ffbd2cd4c56e0a6033f1a57d11d61ae30ce220a4e",
    V1_FREEZE: "71e076ff360c8bd7d0ca00feee153d7e1794619b980391aa49a473c098bcb721",
    V1_NEGATIVE: "df29e2d45d880d734dafbd2a26004d4dc3a32d27f002dd51cddc71c93e63fa22",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only D1 transition V2 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only D1 transition V2 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def main():
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
    source_input = scratch / f"square_d1_load_transition_a6_a7_{label}.sing"
    text = source_input.read_text()
    old = "(3/4)*sigma^17*t*(k60+sigma*k61)"
    new = "(3/4)*sigma^17*t*t*(k60+sigma*k61)"
    count = text.count(old)
    if count != 2:
        fail(("unexpected k6*C alignment occurrence count", count, 2))
    text = text.replace(old, new)
    if old in text or text.count(new) != 2:
        fail("V2 t^2 repair failed")
    output.mkdir(parents=True)
    target = output / f"square_d1_load_transition_a6_a7_v2_{label}.sing"
    target.write_text(text)
    payload = {
        "status": "PASS-D1-LOAD-TRANSITION-A6-A7-V2-T2-COMPILER",
        "scope": "TWO_K6C_TAIL_ALIGNMENT_REPLACEMENTS_ONLY_NO_FAN_OR_ORDER2_VERDICT",
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

