#!/usr/bin/env python3
"""One-token target-precedence repair of the D1 a9 D(k60) client; AWS only."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V1_DIR = ROOT / "cases/max12_812_order2_square_owner_d1_a9_k60_unit_grade27_20260826"
V1 = V1_DIR / "compile_a9_k60_unit.py"
PINS = {
    V1: "abb88d2a343d0cde75cdc8c2818ccc541c9961b6eca71f3ef0cbf8e114698f74",
    V1_DIR / "FREEZE.sha256": "d84fef5925858f105332591df7a2027ae4f70c764517a1c1b167a60c2204d968",
    V1_DIR / "REGISTRATION.md": "4b5847eba158ab3965aa762de8662956537e9ee51ddd696d1b888cebec05158f",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only D1 a9 k60-unit V2 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only D1 a9 k60-unit V2 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_v1():
    spec = importlib.util.spec_from_file_location("d1_a9_k60_v1", V1)
    if spec is None or spec.loader is None:
        fail("cannot import frozen V1 compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    for source, expected in PINS.items():
        actual = digest(source)
        if actual != expected:
            fail(("frozen V1 ancestry mismatch", str(source), actual, expected))

    v1 = load_v1()
    old_argv = sys.argv
    try:
        sys.argv = [str(V1), str(args.output.resolve()), "--characteristic", str(args.characteristic)]
        v1.main()
    finally:
        sys.argv = old_argv

    output = args.output.resolve()
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    parent = output / f"square_d1_a9_k60_unit_grade27_{label}.sing"
    text = parent.read_text()
    old = "diff(A9V2_Q0_7,J)+sigma^38/4==0"
    new = "diff(A9V2_Q0_7,J)+(sigma^38)/4==0"
    old_count = text.count(old)
    new_before = text.count(new)
    if (old_count, new_before) != (1, 0):
        fail(("unexpected V1 precedence counts", old_count, new_before))
    text = text.replace(old, new)
    if (text.count(old), text.count(new)) != (0, 1):
        fail("V2 precedence replacement did not have exact cardinality")
    target = output / f"square_d1_a9_k60_unit_grade27_v2_{label}.sing"
    parent.rename(target)
    target.write_text(text)

    v1_payload_path = output / "result.json"
    v1_payload = json.loads(v1_payload_path.read_text())
    v1_payload_path.rename(output / "parent_v1_result.json")
    payload = {
        "status": "PASS-D1-A9-K60-UNIT-V2-TARGET-PRECEDENCE-COMPILER",
        "scope": "ONE_TOKEN_PRECEDENCE_REPAIR_FIXED_CONTACT_A9_D_P_K10_K6",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "input_sha256": digest(target),
        "parent_v1_input_sha256": v1_payload["input_sha256"],
        "old_count": old_count,
        "new_count": text.count(new),
    }
    v1_payload_path.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print("D1A9_K60_V2_TARGET_PRECEDENCE_OLD_COUNT=1")
    print("D1A9_K60_V2_TARGET_PRECEDENCE_NEW_COUNT=1")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()

