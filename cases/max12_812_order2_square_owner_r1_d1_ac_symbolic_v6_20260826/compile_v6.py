#!/usr/bin/env python3
"""Compile V6 using linear root-chart ideals instead of nested subst."""

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
V5 = ROOT / "cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_v5_20260826/compile_v5.py"
V5_FREEZE = ROOT / "cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_v5_20260826/FREEZE.sha256"
PINS = {
    V5: "66fd0a54e7348f9042f6f1475ad2f239a7ec88d835c14aa03f44323ec8b26d2c",
    V5_FREEZE: "9050ab75eba7ba48727218e993b599ffed237be1038a1b93aa80b4fd21c2c426",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only r1/d1 V6 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only r1/d1 V6 compiler refused non-Amazon host")
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
        if digest(source) != expected:
            fail(("frozen V5 pin mismatch", str(source)))
    output = args.output.resolve()
    if output.exists():
        fail("V6 output already exists")
    scratch = output.parent / (output.name + "_frozen_v5")
    subprocess.run(
        [sys.executable, str(V5), str(scratch), "--characteristic", str(args.characteristic)],
        check=True,
        env=os.environ.copy(),
    )
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    v5_input = scratch / f"square_r1_d1_ac_v5_{label}.sing"
    source_text = v5_input.read_text()
    start = "poly D1AC_tmp15=D1AC_N15;"
    end = "int D1AC_residue=(D1AC_resplus-(3/2)*rtx^2*cv^2*theta^2==0 && D1AC_resminus-(3/2)*rtx^2*cv^2*theta^2==0);"
    if source_text.count(start) != 1 or source_text.count(end) != 1:
        fail(("V5 root block anchors missing or nonunique", source_text.count(start), source_text.count(end)))
    prefix, rest = source_text.split(start, 1)
    _, suffix = rest.split(end, 1)
    replacement = "\n".join(
        [
            "ideal IP=std(ideal(p+2*rtx^2,a1-au,a0+au*rtx,c1-cv,c0-cv*rtx));",
            "ideal IM=std(ideal(p+2*rtx^2,a1-au,a0-au*rtx,c1-cv,c0+cv*rtx));",
            "ideal IPR=std(ideal(p+2*rtx^2,a1-au,a0+au*rtx,c1-cv,c0-cv*rtx,z-rtx));",
            "ideal IMR=std(ideal(p+2*rtx^2,a1-au,a0-au*rtx,c1-cv,c0+cv*rtx,z+rtx));",
            "int D1AC_flag=(reduce(D1AC_N15,IP)==0 && reduce(D1AC_N15,IM)==0);",
            "int D1AC_residue=(reduce(D1AC_N16-(3/2)*rtx^2*cv^2*theta^2,IPR)==0 && reduce(D1AC_N16-(3/2)*rtx^2*cv^2*theta^2,IMR)==0);",
        ]
    )
    source_text = prefix + replacement + suffix
    output.mkdir(parents=True)
    target = output / f"square_r1_d1_ac_v6_{label}.sing"
    target.write_text(source_text)
    payload = {
        "status": "PASS-R1-D1-AC-V6-COMPILER",
        "scope": "IDEAL_CHART_REPAIR_R1_AND_D1_UNIQUE_AC_NO_SQUARE_OR_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "v5_compiler_sha256": digest(V5),
        "v5_input_sha256": digest(v5_input),
        "input_sha256": digest(target),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
