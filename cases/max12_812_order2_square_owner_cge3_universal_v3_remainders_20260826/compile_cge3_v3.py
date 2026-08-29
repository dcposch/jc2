#!/usr/bin/env python3
"""Compile remainder-aware V3 of the frozen c>=3 universal client."""

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
V2 = ROOT / "cases/max12_812_order2_square_owner_cge3_universal_v2_scalar_20260826/compile_cge3_v2.py"
V2_FREEZE = ROOT / "cases/max12_812_order2_square_owner_cge3_universal_v2_scalar_20260826/FREEZE.sha256"
PINS = {
    V1: "352ad4f2d10df80e7edcc5179a8c46dfc55b4f7ce07762fb06d2109a9da1da23",
    V1_FREEZE: "a5efc70c73fb1539086b58bc386a26815e9edb754c50eee505ab8f0918d18169",
    V2: "a0af946c6fe2aecdd1deabf75d2b8962f213974df27ba6766c007da9b3c0ee48",
    V2_FREEZE: "4f543c96974ef0fe19eedac3b860b6f05dd120963c424855c82a8ab6305fe7c2",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only c>=3 V3 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only c>=3 V3 compiler refused non-Amazon host")
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


def remainder_block() -> str:
    lines = [
        "poly DR13_0=R13; poly DR14_0=R14;",
        "poly c13_0=subst(DR13_0,z,0); poly c14_0=subst(DR14_0,z,0);",
    ]
    for degree in range(1, 7):
        lines.extend(
            [
                f"poly DR13_{degree}=diff(DR13_{degree - 1},z);",
                f"poly DR14_{degree}=diff(DR14_{degree - 1},z);",
            ]
        )
        if degree <= 5:
            lines.extend(
                [
                    f"poly c13_{degree}=subst(DR13_{degree},z,0);",
                    f"poly c14_{degree}=subst(DR14_{degree},z,0);",
                ]
            )
    generators = ",".join(["L0"] + [f"c13_{i}" for i in range(6)] + [f"c14_{i}" for i in range(6)])
    lines.extend(
        [
            "int remainderDegree=(DR13_6==0 && DR14_6==0);",
            f"ideal Gsep=std(ideal({generators}));",
            "int separator=(reduce(C15+(1/16)*A0z^3,Gsep)==0);",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    for source, expected in PINS.items():
        if digest(source) != expected:
            fail(("frozen V1/V2 pin mismatch", str(source)))
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
    target = output / f"square_cge3_universal_v3_{label}.sing"
    v1.emit(target, args.characteristic, tails)
    text = target.read_text()
    old = "ideal GL=std(ideal(L0)); poly A0z=a1*z+a0;\nint separator=(reduce(C15+A0z^3,GL)==0);"
    new = "ideal GL=std(ideal(L0)); poly A0z=a1*z+a0;\n" + remainder_block()
    if text.count(old) != 1:
        fail(("V1 separator anchor missing or nonunique", text.count(old)))
    text = text.replace(old, new)
    replacements = {
        "SQUARE_CGE3_G15_MOD_L_EQUALS_MINUS_A_CUBED=": "SQUARE_CGE3_G15_MOD_LOWER_REMAINDERS_EQUALS_MINUS_ONE_SIXTEENTH_A_CUBED=",
        "analyticDiv*row13*row14*row15*numDiv*divisionRec*separator": "analyticDiv*row13*row14*row15*numDiv*divisionRec*remainderDegree*separator",
        "SQUARE_CGE3_ENDPOINT=PASS_UNIVERSAL_CGE3_RGE1_A_ZERO_GATE": "SQUARE_CGE3_V3_ENDPOINT=PASS_UNIVERSAL_CGE3_RGE1_A_ZERO_GATE",
    }
    for old_text, new_text in replacements.items():
        if text.count(old_text) != 1:
            fail(("V1 replacement anchor missing or nonunique", old_text, text.count(old_text)))
        text = text.replace(old_text, new_text)
    marker = 'print("SQUARE_CGE3_MOVING_DIVISION_RECURRENCE="+string(divisionRec));'
    if text.count(marker) != 1:
        fail("division marker missing or nonunique")
    text = text.replace(marker, marker + '\nprint("SQUARE_CGE3_LOWER_REMAINDER_DEGREE="+string(remainderDegree));')
    target.write_text(text)
    payload = {
        "status": "PASS-SQUARE-CGE3-UNIVERSAL-V3-COMPILER",
        "scope": "V3_REMAINDER_REPAIR_CGE3_RGE1_ONLY_NO_SQUARE_OR_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "v1_compiler_sha256": digest(V1),
        "v2_compiler_sha256": digest(V2),
        "input_sha256": digest(target),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
