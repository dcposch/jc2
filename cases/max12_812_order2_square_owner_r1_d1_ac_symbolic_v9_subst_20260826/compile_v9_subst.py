#!/usr/bin/env python3
"""Compile V8 and replace only the D1 root-chart evaluator by substitutions."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import platform
import re
import subprocess
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V8 = ROOT / "cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_v8_split_20260826/compile_v8_split.py"
V8_FREEZE = ROOT / "cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_v8_split_20260826/FREEZE.sha256"
PINS = {
    V8: "b4cf82f050f2a0a4052bbef9652200e5d940d4cf07af463c0aee3e458d6c4886",
    V8_FREEZE: "61d350ecac4f7beac84871ee24a360e5ef6302f8f210a5ecff045944492bbbe0",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only r1/d1 V9 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only r1/d1 V9 compiler refused non-Amazon host")
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
            fail(("frozen V8 pin mismatch", str(source), actual, expected))

    output = args.output.resolve()
    if output.exists():
        fail("V9 output already exists")
    scratch = output.parent / (output.name + "_frozen_v8")
    subprocess.run(
        [sys.executable, str(V8), str(scratch), "--characteristic", str(args.characteristic)],
        check=True,
        env=os.environ.copy(),
    )
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    r1_v8 = scratch / f"square_r1_v8_{label}.sing"
    d1_v8 = scratch / f"square_d1_ac_v8_{label}.sing"
    d1_text = d1_v8.read_text()

    name_counts = {}
    for old, new, expected in (("au", "aua", 9), ("cv", "cvg", 13)):
        count = len(re.findall(rf"\b{old}\b", d1_text))
        if count != expected:
            fail(("unexpected D1 auxiliary-name count", old, count, expected))
        d1_text = re.sub(rf"\b{old}\b", new, d1_text)
        name_counts[old] = count

    start = "ideal IP=std(ideal("
    end_prefix = "int D1AC_residue=(reduce("
    if d1_text.count(start) != 1 or d1_text.count(end_prefix) != 1:
        fail(("V8 D1 chart anchors missing or nonunique", d1_text.count(start), d1_text.count(end_prefix)))
    prefix, remainder = d1_text.split(start, 1)
    old_block, suffix = remainder.split(end_prefix, 1)
    _, suffix = suffix.split(";\n", 1)
    replacement = "\n".join(
        [
            "poly D1AC_pos15=D1AC_N15;",
            "D1AC_pos15=subst(D1AC_pos15,p,-2*rtx*rtx); D1AC_pos15=subst(D1AC_pos15,a1,aua); D1AC_pos15=subst(D1AC_pos15,a0,-aua*rtx); D1AC_pos15=subst(D1AC_pos15,c1,cvg); D1AC_pos15=subst(D1AC_pos15,c0,cvg*rtx);",
            "poly D1AC_pos16=D1AC_N16;",
            "D1AC_pos16=subst(D1AC_pos16,p,-2*rtx*rtx); D1AC_pos16=subst(D1AC_pos16,a1,aua); D1AC_pos16=subst(D1AC_pos16,a0,-aua*rtx); D1AC_pos16=subst(D1AC_pos16,c1,cvg); D1AC_pos16=subst(D1AC_pos16,c0,cvg*rtx);",
            "poly D1AC_posres=subst(D1AC_pos16,z,rtx);",
            "poly D1AC_neg15=D1AC_N15;",
            "D1AC_neg15=subst(D1AC_neg15,p,-2*rtx*rtx); D1AC_neg15=subst(D1AC_neg15,a1,aua); D1AC_neg15=subst(D1AC_neg15,a0,aua*rtx); D1AC_neg15=subst(D1AC_neg15,c1,cvg); D1AC_neg15=subst(D1AC_neg15,c0,-cvg*rtx);",
            "poly D1AC_neg16=D1AC_N16;",
            "D1AC_neg16=subst(D1AC_neg16,p,-2*rtx*rtx); D1AC_neg16=subst(D1AC_neg16,a1,aua); D1AC_neg16=subst(D1AC_neg16,a0,aua*rtx); D1AC_neg16=subst(D1AC_neg16,c1,cvg); D1AC_neg16=subst(D1AC_neg16,c0,-cvg*rtx);",
            "poly D1AC_negres=subst(D1AC_neg16,z,-rtx);",
            "int D1AC_flag=(D1AC_pos15==0 && D1AC_neg15==0);",
            "int D1AC_residue=(D1AC_posres-(3/2)*rtx*rtx*cvg*cvg*theta*theta==0 && D1AC_negres-(3/2)*rtx*rtx*cvg*cvg*theta*theta==0);",
        ]
    )
    d1_text = prefix + replacement + "\n" + suffix
    if "ideal IP=" in d1_text or "LIB \"primdec.lib\";" in d1_text:
        fail("old ideal or primdec leaked into V9 D1 process")
    if d1_text.count("D1AC_pos15=subst") != 5 or d1_text.count("D1AC_neg15=subst") != 5:
        fail("unexpected V9 grade-15 substitution count")

    output.mkdir(parents=True)
    r1_target = output / f"square_r1_v9_{label}.sing"
    d1_target = output / f"square_d1_ac_v9_{label}.sing"
    r1_target.write_bytes(r1_v8.read_bytes())
    d1_target.write_text(d1_text)
    payload = {
        "status": "PASS-R1-D1-AC-V9-SUBST-COMPILER",
        "scope": "DIRECT_SUBSTITUTION_EVALUATOR_ONLY_R1_AND_D1_UNIQUE_AC_NO_SQUARE_OR_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "v8_compiler_sha256": digest(V8),
        "v8_r1_input_sha256": digest(r1_v8),
        "v8_d1_input_sha256": digest(d1_v8),
        "auxiliary_rename_counts": name_counts,
        "r1_input_sha256": digest(r1_target),
        "d1_input_sha256": digest(d1_target),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
