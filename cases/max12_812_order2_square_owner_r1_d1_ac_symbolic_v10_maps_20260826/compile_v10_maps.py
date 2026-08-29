#!/usr/bin/env python3
"""Compile V9 and replace the terminal D1 evaluator with explicit ring maps."""

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
V9 = ROOT / "cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_v9_subst_20260826/compile_v9_subst.py"
V9_FREEZE = ROOT / "cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_v9_subst_20260826/FREEZE.sha256"
PINS = {
    V9: "95d8c21d1f4797cf66a9f3f4894cd1c4506409253d6a44117000ec0e9fb4db5d",
    V9_FREEZE: "6ac46a9b2519e208647e3b99ded46ad4efb15552aea7d158bc75ac19b21fb5ac",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only r1/d1 V10 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only r1/d1 V10 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def images(z_image: str, a0_image: str, c0_image: str) -> list[str]:
    result = [
        z_image, "t", "sigma", "-2*rtx*rtx", "ell1", "theta", "eta",
        a0_image, "aua", "aa0", "aa1", c0_image, "cvg", "cc0", "cc1",
        "b0", "b1", "k0", "k6", "k2load", "mu2", "mu4", "mu6", "J",
        "rtx", "aua", "cvg",
    ]
    if len(result) != 27:
        fail(("map image count", len(result)))
    return result


def map_line(name: str, values: list[str]) -> str:
    return f"map {name}=Rd1," + ",".join(values) + ";"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    for source, expected in PINS.items():
        actual = digest(source)
        if actual != expected:
            fail(("frozen V9 pin mismatch", str(source), actual, expected))

    output = args.output.resolve()
    if output.exists():
        fail("V10 output already exists")
    scratch = output.parent / (output.name + "_frozen_v9")
    subprocess.run(
        [sys.executable, str(V9), str(scratch), "--characteristic", str(args.characteristic)],
        check=True,
        env=os.environ.copy(),
    )
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    r1_v9 = scratch / f"square_r1_v9_{label}.sing"
    d1_v9 = scratch / f"square_d1_ac_v9_{label}.sing"
    d1_text = d1_v9.read_text()
    anchor = "poly D1AC_pos15=D1AC_N15;"
    if d1_text.count(anchor) != 1 or d1_text.count("R1_D1_AC_PACKAGE_ENDPOINT=PASS") != 1:
        fail("V9 D1 terminal anchors missing or nonunique")
    prefix, _ = d1_text.split(anchor, 1)

    variables = "z,t,sigma,p,ell1,theta,eta,a0,a1,aa0,aa1,c0,c1,cc0,cc1,b0,b1,k0,k6,k2load,mu2,mu4,mu6,J,rtx,aua,cvg"
    pos = images("z", "-aua*rtx", "cvg*rtx")
    neg = images("z", "aua*rtx", "-cvg*rtx")
    posroot = images("rtx", "-aua*rtx", "cvg*rtx")
    negroot = images("-rtx", "aua*rtx", "-cvg*rtx")
    terminal = [
        'print("D1AC_DENOMINATOR_RECURRENCE_G15="+string(D1AC_rec15));',
        'print("D1AC_DENOMINATOR_RECURRENCE_G16="+string(D1AC_rec16));',
        "if (D1AC_divisible*D1AC_identities*D1AC_forbidden*D1AC_analyticDiv*D1AC_row15*D1AC_row16*D1AC_scale15*D1AC_scale16*D1AC_rec15*D1AC_rec16!=1) { print(\"D1AC_FAIL=BRIDGE_SHIFT_OR_RECURRENCE\"); quit; }",
        f"ring Rd1eval={args.characteristic},({variables}),dp;",
        map_line("D1AC_posmap", pos),
        map_line("D1AC_negmap", neg),
        map_line("D1AC_posrootmap", posroot),
        map_line("D1AC_negrootmap", negroot),
        "poly D1AC_evalpos15=D1AC_posmap(D1AC_N15);",
        "poly D1AC_evalneg15=D1AC_negmap(D1AC_N15);",
        "poly D1AC_evalposroot16=D1AC_posrootmap(D1AC_N16);",
        "poly D1AC_evalnegroot16=D1AC_negrootmap(D1AC_N16);",
        "int D1AC_flag=(D1AC_evalpos15==0 && D1AC_evalneg15==0);",
        "int D1AC_residue=(D1AC_evalposroot16-(3/2)*rtx*rtx*cvg*cvg*theta*theta==0 && D1AC_evalnegroot16-(3/2)*rtx*rtx*cvg*cvg*theta*theta==0);",
        'print("D1AC_BOTH_ROOT_ORIENTATIONS="+string(D1AC_flag));',
        'print("D1AC_UNMATCHED_DOUBLE_POLE="+string(D1AC_residue));',
        "if (D1AC_flag*D1AC_residue!=1) { print(\"D1AC_FAIL=MAP_ORIENTATION_OR_RESIDUE\"); quit; }",
        'print("D1AC_ENDPOINT=PASS_SYMBOLIC_D1_UNIQUE_AC_DOUBLE_POLE_GATE");',
        'print("R1_D1_AC_PACKAGE_ENDPOINT=PASS");',
        "quit;",
    ]
    d1_text = prefix + "\n".join(terminal) + "\n"
    if d1_text.count("map D1AC_") != 4 or "subst(D1AC_pos" in d1_text or "ideal IP=" in d1_text:
        fail("V10 terminal map construction failed")

    output.mkdir(parents=True)
    r1_target = output / f"square_r1_v10_{label}.sing"
    d1_target = output / f"square_d1_ac_v10_{label}.sing"
    r1_target.write_bytes(r1_v9.read_bytes())
    d1_target.write_text(d1_text)
    payload = {
        "status": "PASS-R1-D1-AC-V10-MAP-COMPILER",
        "scope": "FOUR_RING_MAP_EVALUATOR_ONLY_R1_AND_D1_UNIQUE_AC_NO_SQUARE_OR_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "v9_compiler_sha256": digest(V9),
        "map_count": d1_text.count("map D1AC_"),
        "map_image_count": len(pos),
        "r1_input_sha256": digest(r1_target),
        "d1_input_sha256": digest(d1_target),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
