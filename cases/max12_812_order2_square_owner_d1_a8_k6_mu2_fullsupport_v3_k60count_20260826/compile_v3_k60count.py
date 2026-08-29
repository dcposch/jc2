#!/usr/bin/env python3
"""Compile a8 V1 with the six-symbol repair and exact before/after counts."""

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
V2_DIR = ROOT / "cases/max12_812_order2_square_owner_d1_a8_k6_mu2_fullsupport_v2_k60symbol_20260826"
V1 = V1_DIR / "compile_a8.py"
V1_FREEZE = V1_DIR / "FREEZE.sha256"
V1_NEGATIVE = V1_DIR / "RESULT_NEGATIVE_CONTROL.md"
V2 = V2_DIR / "compile_v2_k60symbol.py"
V2_FREEZE = V2_DIR / "FREEZE.sha256"
V2_NEGATIVE = V2_DIR / "RESULT_NEGATIVE_CONTROL.md"
PINS = {
    V1: "0230ca443d49e47b5d6ebae8c0f8a88d31a793d13b1df59e3698e166226d177b",
    V1_FREEZE: "c18bdd9f55a108470ef166e6c0cfa243ab61b63f45742537046fdb6e583b5dc8",
    V1_NEGATIVE: "be3d6843a27db31ee7e844fe1edea1e2f6fb7b65ba9b7c8f2289ff28e3441ed2",
    V2: "7cc1b281f24ed8f138aab12ad7e0412c57ce441f5aa28d57eaec14dc998a28e9",
    V2_FREEZE: "297a9bb5ceb76e0dda740a0b498902e497af9f7c74af96dd3b757ceb209ae9a1",
    V2_NEGATIVE: "db3c28f81f4bdbf422af87fa85e09f9d3f916292c387552b54ddad4e0e71a9f8",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only a8 V3 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only a8 V3 compiler refused non-Amazon host")
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
            fail(("frozen ancestry pin mismatch", str(source), actual, expected))
    output = args.output.resolve()
    if output.exists():
        fail("V3 output already exists")
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
    old_before = text.count(old)
    new_before = text.count(new)
    if (old_before, new_before) != (6, 1):
        fail(("unexpected pre-repair declaration/map counts", old_before, new_before))
    text = text.replace(old, new)
    old_after = text.count(old)
    new_after = text.count(new)
    if (old_after, new_after) != (0, 7):
        fail(("unexpected post-repair declaration/map counts", old_after, new_after))
    output.mkdir(parents=True)
    target = output / f"square_d1_a8_k6_mu2_v3_{label}.sing"
    target.write_text(text)
    payload = {
        "status": "PASS-D1-A8-K6-MU2-V3-K60COUNT-COMPILER",
        "scope": "SIX_FORMAL_K60_RING_MAP_INSERTIONS_WITH_EXACT_COUNTS_ONLY",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "v1_compiler_sha256": digest(V1),
        "v2_compiler_sha256": digest(V2),
        "old_before": old_before,
        "new_before": new_before,
        "old_after": old_after,
        "new_after": new_after,
        "input_sha256": digest(target),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()

