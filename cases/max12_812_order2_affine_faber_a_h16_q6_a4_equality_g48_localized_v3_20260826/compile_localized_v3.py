#!/usr/bin/env python3
"""Re-emit the pinned V2 equality source with exact chart localizations."""

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
PARENT = ROOT / "cases/max12_812_order2_affine_faber_a_h16_q6_a4_equality_g48_20260826/compile_h16_q6_a4_g48.py"
PARENT_SHA = "a4479ed8bbfac88a7153d2fa7adb815027209d13cb7f0ae2fcd257a01ccdabbb"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only localized V3 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only localized V3 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_parent():
    if digest(PARENT) != PARENT_SHA:
        fail("frozen V2 compiler mismatch")
    spec = importlib.util.spec_from_file_location("equality_v2", PARENT)
    if spec is None or spec.loader is None:
        fail("cannot import frozen V2 compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def replace_once(source: str, old: str, new: str) -> str:
    if source.count(old) != 1:
        fail({"replacement_count": source.count(old), "old": old})
    return source.replace(old, new)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    parent = load_parent()
    base = parent.load_base()
    if digest(base.TAILS) != base.EXPECTED_TAILS:
        fail("frozen tails mismatch")
    tails = json.loads(base.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != base.EXPECTED_CANONICAL:
        fail("canonical tails mismatch")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    target = output / f"affine_faber_a_h16_q6_a4_g48_localized_v3_{label}.sing"
    parent.emit(target, args.characteristic, base, tails)
    source = target.read_text()
    source = replace_once(
        source,
        "ideal GPRE=std(IPRE); poly K48NF=reduce(K48,GPRE);",
        "poly K48NF=K48;",
    )
    source = replace_once(
        source,
        "ideal IX=IFULL,satu*p*m*x0-1;",
        "ideal IX=IFULL,satu*p*m*a0*kk0*x0-1;",
    )
    source = replace_once(
        source,
        "ideal IY=IFULL,satu*p*m*y0-1;",
        "ideal IY=IFULL,satu*p*m*a0*kk0*y0-1;",
    )
    source = replace_once(
        source,
        'print("A_H16Q6A4_ENDPOINT=FIXED_REPRESENTATIVE_THROUGH_GRADE48_EMITTED");',
        'print("A_H16Q6A4_V3_LOCALIZATION=a0*kk0*p*m*projective_kernel");\n'
        'print("A_H16Q6A4_ENDPOINT=FIXED_REPRESENTATIVE_THROUGH_GRADE48_EMITTED");',
    )
    source = replace_once(
        source,
        "A_H16Q6A4_SCOPE=H16_Q6_A4_FIXED_REPRESENTATIVE_SOURCE_ROWS_G44_TO_G48_ONLY_NO_RATIONAL_REGRADING_REES_ORDER2_MAX12_OR_JC2_VERDICT",
        "A_H16Q6A4_SCOPE=H16_Q6_A4_FIXED_REPRESENTATIVE_LOCALIZED_A0_KK0_SOURCE_ROWS_G44_TO_G48_ONLY_NO_RATIONAL_REGRADING_REES_ORDER2_MAX12_OR_JC2_VERDICT",
    )
    target.write_text(source)
    payload = {
        "status": "PASS-A-H16-Q6-A4-G48-LOCALIZED-V3-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "parent_sha256": digest(PARENT),
        "base_sha256": digest(parent.BASE),
        "tails_sha256": digest(base.TAILS),
        "registered_replacements": 5,
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
