#!/usr/bin/env python3
"""Compile root-remainder shard of frozen c>=3 V3 (AWS only)."""

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
V3 = ROOT / "cases/max12_812_order2_square_owner_cge3_universal_v3_remainders_20260826/compile_cge3_v3.py"
V3_FREEZE = ROOT / "cases/max12_812_order2_square_owner_cge3_universal_v3_remainders_20260826/FREEZE.sha256"
LOWER_HULL = ROOT / "xmodel/max12-812-order2-square-fan-lower-hull-reduction-20260826.md"
PINS = {
    V3: "fc0475624693494abb775392f3bab031950dcf330ff343201f0c4be0386aafd9",
    V3_FREEZE: "83e157046b346ef9bd48259b5d5a65c196c2b59faba1f8697ce92bdd967ec449",
    LOWER_HULL: "d3d8f30a94a3d90175756ea0e21efd974461d51cb2db8433d2a270e1be355337",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only c>=3 V4 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only c>=3 V4 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_v3():
    spec = importlib.util.spec_from_file_location("square_cge3_v3", V3)
    if spec is None or spec.loader is None:
        fail("cannot load frozen V3 compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def root_block() -> str:
    return """poly V4R13L=reduce(R13,GL); poly V4R14L=reduce(R14,GL);
poly V4F15L=reduce(C15+(1/16)*A0z^3,GL);
poly V4R13_0=subst(V4R13L,z,0); poly V4R13d=diff(V4R13L,z); poly V4R13_1=subst(V4R13d,z,0);
poly V4R14_0=subst(V4R14L,z,0); poly V4R14d=diff(V4R14L,z); poly V4R14_1=subst(V4R14d,z,0);
poly V4F15_0=subst(V4F15L,z,0); poly V4F15d=diff(V4F15L,z); poly V4F15_1=subst(V4F15d,z,0);
int remainderDegree=(diff(V4R13d,z)==0 && diff(V4R14d,z)==0 && diff(V4F15d,z)==0);
ideal V4H=std(ideal(V4R13_0,V4R13_1,V4R14_0,V4R14_1));
int V4sep0=(reduce(V4F15_0,V4H)==0); int V4sep1=(reduce(V4F15_1,V4H)==0);
int separator=V4sep0*V4sep1;
print("SQUARE_CGE3_V4_ROOT_SEPARATOR_CONSTANT="+string(V4sep0));
print("SQUARE_CGE3_V4_ROOT_SEPARATOR_LINEAR="+string(V4sep1));"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    for source, expected in PINS.items():
        if digest(source) != expected:
            fail(("frozen V3/lower-hull pin mismatch", str(source)))
    v3 = load_v3()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    nested = output / "frozen_v3"
    saved = sys.argv
    try:
        sys.argv = [str(V3), str(nested), "--characteristic", str(args.characteristic)]
        v3.main()
    finally:
        sys.argv = saved
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    old_input = nested / f"square_cge3_universal_v3_{label}.sing"
    text = old_input.read_text()
    start = text.find("poly DR13_0=R13; poly DR14_0=R14;")
    end_line = "int separator=(reduce(C15+(1/16)*A0z^3,Gsep)==0);"
    end = text.find(end_line, start)
    if start < 0 or end < 0:
        fail(("V3 endpoint anchors missing", start, end))
    end += len(end_line)
    text = text[:start] + root_block() + text[end:]
    text = text.replace(
        "SQUARE_CGE3_V3_ENDPOINT=PASS_UNIVERSAL_CGE3_RGE1_A_ZERO_GATE",
        "SQUARE_CGE3_V4_ENDPOINT=PASS_UNIVERSAL_CGE3_RGE1_A_ZERO_GATE",
    )
    target = output / f"square_cge3_universal_v4_{label}.sing"
    target.write_text(text)
    payload = {
        "status": "PASS-SQUARE-CGE3-UNIVERSAL-V4-COMPILER",
        "scope": "VERTICAL_A0_CGE3_RGE1_ONLY_NO_HORIZONTAL_OR_SQUARE_OR_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "v3_compiler_sha256": digest(V3),
        "v3_input_sha256": digest(old_input),
        "input_sha256": digest(target),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
