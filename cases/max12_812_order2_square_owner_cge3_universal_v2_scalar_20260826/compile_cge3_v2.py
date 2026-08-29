#!/usr/bin/env python3
"""Compile scalar-normalized V2 of the frozen c>=3 universal client."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V1 = ROOT / "cases/max12_812_order2_square_owner_cge3_universal_20260826/compile_cge3_universal.py"
V1_FREEZE = ROOT / "cases/max12_812_order2_square_owner_cge3_universal_20260826/FREEZE.sha256"
EXPECTED_V1 = "352ad4f2d10df80e7edcc5179a8c46dfc55b4f7ce07762fb06d2109a9da1da23"
EXPECTED_FREEZE = "a5efc70c73fb1539086b58bc386a26815e9edb754c50eee505ab8f0918d18169"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only c>=3 V2 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only c>=3 V2 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_v1():
    spec = importlib.util.spec_from_file_location("square_cge3_v1", V1)
    if spec is None or spec.loader is None:
        fail("cannot load frozen V1 compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    if digest(V1) != EXPECTED_V1 or digest(V1_FREEZE) != EXPECTED_FREEZE:
        fail("frozen V1 pin mismatch")
    v1 = load_v1()
    for source, expected in v1.EXPECTED.items():
        if digest(source) != expected:
            fail(("frozen transitive source mismatch", str(source)))
    tails = json.loads(v1.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != v1.EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    target = output / f"square_cge3_universal_v2_{label}.sing"
    v1.emit(target, args.characteristic, tails)
    text = target.read_text()
    replacements = {
        "int separator=(reduce(C15+A0z^3,GL)==0);": "int separator=(reduce(C15+(1/16)*A0z^3,GL)==0);",
        "SQUARE_CGE3_G15_MOD_L_EQUALS_MINUS_A_CUBED=": "SQUARE_CGE3_G15_MOD_L_EQUALS_MINUS_ONE_SIXTEENTH_A_CUBED=",
        "SQUARE_CGE3_ENDPOINT=PASS_UNIVERSAL_CGE3_RGE1_A_ZERO_GATE": "SQUARE_CGE3_V2_ENDPOINT=PASS_UNIVERSAL_CGE3_RGE1_A_ZERO_GATE",
    }
    for old, new in replacements.items():
        if text.count(old) != 1:
            fail(("V1 replacement anchor missing or nonunique", old, text.count(old)))
        text = text.replace(old, new)
    target.write_text(text)
    payload = {
        "status": "PASS-SQUARE-CGE3-UNIVERSAL-V2-COMPILER",
        "scope": "V2_SCALAR_REPAIR_CGE3_RGE1_ONLY_NO_SQUARE_OR_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "v1_compiler_sha256": digest(V1),
        "v1_freeze_sha256": digest(V1_FREEZE),
        "input_sha256": digest(target),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
