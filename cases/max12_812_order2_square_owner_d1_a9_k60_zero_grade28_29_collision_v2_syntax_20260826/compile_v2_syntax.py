#!/usr/bin/env python3
"""Syntax-only repair of the D1 a9 V(k60) collision; AWS only."""

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
V1_DIR = ROOT / "cases/max12_812_order2_square_owner_d1_a9_k60_zero_grade28_29_collision_20260826"
V1 = V1_DIR / "compile_a9_k60_zero_collision.py"
PINS = {
    V1: "0a0263ec33812dcdb4554f58e206f2d3eb16c8965f5df9ef00cd1654c4879744",
    V1_DIR / "REGISTRATION.md": "73e7e8a72774e81497d3f0b279b42a31bfbdfc6ef0371639b8d2b3b224b50a9a",
    V1_DIR / "FREEZE.sha256": "5152301b5e218ff7e0bfe511ed648e453b7d38a048e37307e59b8a1ad2d04f81",
    V1_DIR / "V1_FAILURE.md": "1d0805dc6e75048ecc8ae94a65b5aa605d325dd5a2635580adb3a38d6782ccc1",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only D1 a9 V(k60) V2 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only D1 a9 V(k60) V2 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_v1():
    spec = importlib.util.spec_from_file_location("d1_a9_vk60_v1", V1)
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
    parent = output / f"square_d1_a9_k60_zero_grade28_29_{label}.sing"
    text = parent.read_text()
    repairs = (
        ("p^2/32", "(p^2)/32", 2),
        ("p^3/128", "(p^3)/128", 2),
        ("3*p^2*ell1/64", "3*(p^2)*ell1/64", 1),
        (f"ring D1A9V60={args.characteristic},(p,k0", f"ring D1A9V60={args.characteristic},(z,p,k0", 1),
    )
    cardinalities = {}
    for old, new, expected in repairs:
        before = (text.count(old), text.count(new))
        if before != (expected, 0):
            fail(("unexpected V1 repair cardinality", old, new, before, expected))
        text = text.replace(old, new)
        after = (text.count(old), text.count(new))
        if after != (0, expected):
            fail(("unexpected V2 repair cardinality", old, new, after, expected))
        cardinalities[old] = {"before": before, "after": after}

    target = output / f"square_d1_a9_k60_zero_grade28_29_v2_{label}.sing"
    parent.rename(target)
    target.write_text(text)
    v1_payload_path = output / "result.json"
    v1_payload = json.loads(v1_payload_path.read_text())
    v1_payload_path.rename(output / "parent_v1_collision_result.json")
    payload = {
        "status": "PASS-D1-A9-VK60-GRADE28-29-V2-SYNTAX-COMPILER",
        "scope": "FOUR_TOKEN_CLASS_SYNTAX_REPAIR_ONLY_INHERIT_V1_FIREWALL",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "input_sha256": digest(target),
        "parent_v1_input_sha256": v1_payload["input_sha256"],
        "repair_cardinalities": cardinalities,
    }
    v1_payload_path.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print("D1A9_VK60_V2_P2_PRECEDENCE_OLD=2_NEW=2")
    print("D1A9_VK60_V2_P3_PRECEDENCE_OLD=2_NEW=2")
    print("D1A9_VK60_V2_P2ELL_PRECEDENCE_OLD=1_NEW=1")
    print("D1A9_VK60_V2_PELL_Z_HEADER_OLD=1_NEW=1")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()

