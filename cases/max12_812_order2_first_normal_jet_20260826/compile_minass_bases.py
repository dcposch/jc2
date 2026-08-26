#!/usr/bin/env python3
"""AWS-only adapter that prints the two first-normal minimal-prime bases."""

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
BASE = HERE / "compile_first_normal_jet.py"
TAILS = (
    ROOT / "cases/max12_812_order2_u2_62_strict_rees_20260825"
    / "aws_compile_v2_jsat/run/output/compiled_v2/tails.json"
)
EXPECTED_BASE = "6764a38175b48c21e4124ab38478f4e1c13bd6c0e873c7d118529818f63d6021"
EXPECTED_TAILS = "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only minAss adapter refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only minAss adapter refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_base():
    spec = importlib.util.spec_from_file_location("first_normal_frozen", BASE)
    if spec is None or spec.loader is None:
        fail("could not load frozen first-normal compiler")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(32003, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    if digest(BASE) != EXPECTED_BASE or digest(TAILS) != EXPECTED_TAILS:
        fail("frozen input mismatch")
    base = load_base()
    tails = json.loads(TAILS.read_text())
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    singular = output / f"first_normal_minass_bases_p{args.characteristic}.sing"
    base.emit(singular, args.characteristic, tails)
    text = singular.read_text()
    needle = (
        '    print("FIRST_NORMAL_MINASS_COMPONENT="+string(ai)'
        '+",SIZE="+string(size(Pai))+",DIM="+string(dim(Pai)));\n'
    )
    replacement = needle + (
        '    int kzero=(reduce(k10,Pai)==0);\n'
        '    int sqsig=0;\n'
        '    if (reduce(c,Pai)==0 && reduce(p^2-4*r,Pai)==0 '
        '&& reduce(2*n1-p*n3,Pai)==0 && reduce(2*n0-p*n2,Pai)==0) { sqsig=1; }\n'
        '    print("FIRST_NORMAL_MINASS_SIGNATURE="+string(ai)'
        '+",K10_ZERO="+string(kzero)+",SQUARE_CONTAINS="+string(sqsig));\n'
        '    print("FIRST_NORMAL_MINASS_BASIS_BEGIN="+string(ai));\n'
        '    print(Pai);\n'
        '    print("FIRST_NORMAL_MINASS_BASIS_END="+string(ai));\n'
    )
    if text.count(needle) != 1:
        fail("unique minAss insertion site not found")
    singular.write_text(text.replace(needle, replacement))
    payload = {
        "status": "PASS-FIRST-NORMAL-MINASS-BASES-ADAPTER",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "base_compiler_sha256": digest(BASE),
        "tails_sha256": digest(TAILS),
        "input_sha256": digest(singular),
        "scope": "MODULAR_COMPONENT_SIGNATURES_NAVIGATION_ONLY",
    }
    (output / "result.json").write_text(
        json.dumps(payload, sort_keys=True, indent=2) + "\n"
    )
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
