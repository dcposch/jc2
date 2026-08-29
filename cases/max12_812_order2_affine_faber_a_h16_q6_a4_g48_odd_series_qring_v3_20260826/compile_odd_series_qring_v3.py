#!/usr/bin/env python3
"""Emit the grade-48 odd connection in the exact quotient by s^49."""

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
        fail("AWS-only qring compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only qring compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_parent():
    if digest(PARENT) != PARENT_SHA:
        fail("frozen equality compiler mismatch")
    spec = importlib.util.spec_from_file_location("equality_v2", PARENT)
    if spec is None or spec.loader is None:
        fail("cannot import frozen equality compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


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
    target = output / f"affine_faber_a_h16_q6_a4_g48_odd_series_qring_v3_{label}.sing"
    parent.emit(target, args.characteristic, base, tails)
    source = target.read_text()
    option_anchor = "option(redSB);"
    if source.count(option_anchor) != 1:
        fail({"option_anchor_count": source.count(option_anchor)})
    source = source.replace(
        option_anchor,
        option_anchor + "\nideal TRUNC=s^49; qring TRUNCATED=std(TRUNC);",
    )
    anchor = "int lowerControl=lowzero(P1,44)*lowzero(P2,44)*lowzero(P3,44)*lowzero(P4,44)*lowzero(P5,44)*lowzero(P6,44)*lowzero(P7,44);"
    if source.count(anchor) != 1:
        fail({"tail_anchor_count": source.count(anchor)})
    prefix = source.split(anchor, 1)[0]
    unused = ("poly T2=", "poly T4=", "poly T5=", "poly T6=",
              "poly P2=", "poly P4=", "poly P5=", "poly P6=")
    kept = [line for line in prefix.splitlines() if not line.startswith(unused)]
    for marker in unused:
        if any(line.startswith(marker) for line in kept):
            fail({"unused_marker_survived": marker})
    tail = [
        "poly FODD=P7-(EE^2/32)*P3+(EE^3/64)*P1;",
        "poly ODD48=tc(FODD,48);",
        'print("A_H16Q6A4_ODD_QRING_V3_TCOEFF_CONTROL="+string(tcControl));',
        'print("A_H16Q6A4_ODD_QRING_V3_48="+string(ODD48));',
        'print("A_H16Q6A4_ODD_QRING_V3_TRUNCATION=s^49");',
        'print("A_H16Q6A4_ODD_QRING_V3_ENDPOINT=GRADE48_EMITTED");',
        'print("A_H16Q6A4_ODD_QRING_V3_DONE=1");',
        'print("A_H16Q6A4_ODD_QRING_V3_SCOPE=ROWS1_3_7_COMPLETE_SOURCE_MOD_S49_EXACT_THROUGH_G48_NO_PREDECESSOR_REDUCTION_RATIONAL_REGRADING_REES_ORDER2_MAX12_OR_JC2_VERDICT");',
        "quit;",
    ]
    target.write_text("\n".join(kept + tail) + "\n")
    generated = target.read_text()
    controls = {
        "T1": generated.count("poly T1="), "T3": generated.count("poly T3="),
        "T7": generated.count("poly T7="), "P1": generated.count("poly P1="),
        "P3": generated.count("poly P3="), "P7": generated.count("poly P7="),
        "qring": generated.count("qring TRUNCATED=std(TRUNC);"),
    }
    if set(controls.values()) != {1}:
        fail({"source_controls": controls})
    payload = {
        "status": "PASS-A-H16-Q6-A4-G48-ODD-SERIES-QRING-V3-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "parent_sha256": digest(PARENT),
        "base_sha256": digest(parent.BASE),
        "tails_sha256": digest(base.TAILS),
        "source_controls": controls,
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
