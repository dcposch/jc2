#!/usr/bin/env python3
"""Repair only coefficient extraction in the frozen sharp-third V1 emitter."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
import math
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V1 = ROOT / "cases/max12_812_order2_square_third_tail_sharp_20260826/compile_square_third_tail_sharp.py"
V1_FREEZE = ROOT / "cases/max12_812_order2_square_third_tail_sharp_20260826/FREEZE.sha256"
TAILS = ROOT / "cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json"
EXPECTED = {
    V1: "9a39ba22d85bbc0336f11269701acb312f6cd2629ac157c54c2d76836d07e124",
    V1_FREEZE: "f6999a1f9ef2a07bcb921fbf8482b5b00d8daeceb7a41c6a9fca2030203cabe4",
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
}
EXPECTED_ALL_TAILS = "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only sharp-third V2 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only sharp-third V2 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_v1():
    spec = importlib.util.spec_from_file_location("square_third_sharp_v1", V1)
    if spec is None or spec.loader is None:
        fail("cannot load frozen V1 emitter")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def derivative_coefficients(poly: str, var: str, prefix: str, maximum: int) -> list[str]:
    lines = [f"poly {prefix}D0={poly};", f"poly {prefix}C0=subst({prefix}D0,{var},0);"]
    for degree in range(1, maximum + 1):
        lines.extend(
            [
                f"poly {prefix}D{degree}=diff({prefix}D{degree - 1},{var});",
                f"poly {prefix}C{degree}=subst({prefix}D{degree},{var},0)/{math.factorial(degree)};",
            ]
        )
    return lines


def repair(text: str, config: str) -> str:
    zblock = derivative_coefficients("PP", "z", "PZ", 9)
    zblock.extend(
        [
            "poly ExtractControl=3+5*z+7*z^3;",
            "poly ECD0=ExtractControl; poly ECC0=subst(ECD0,z,0);",
            "poly ECD1=diff(ECD0,z); poly ECC1=subst(ECD1,z,0);",
            "poly ECD2=diff(ECD1,z); poly ECC2=subst(ECD2,z,0)/2;",
            "poly ECD3=diff(ECD2,z); poly ECC3=subst(ECD3,z,0)/6;",
            "int extractorControl=(ECC0==3 && ECC1==5 && ECC2==0 && ECC3==7);",
            'print("SQUARE_THIRD_SHARP_V2_EXTRACTOR_CONTROL="+string(extractorControl));',
            'if (extractorControl!=1) { print("SQUARE_THIRD_SHARP_V2_FAIL=EXTRACTOR_CONTROL"); quit; }',
            "poly Prev=0;",
        ]
    )
    text = text.replace("poly Prev=0;", "\n".join(zblock), 1)
    for degree in range(10):
        old = f"Prev=Prev+coeff(PP,z,{degree})*t^{9-degree};"
        new = f"Prev=Prev+PZC{degree}*t^{9-degree};"
        if old not in text:
            fail(("missing V1 z-coefficient line", old))
        text = text.replace(old, new, 1)

    hblock = ["poly H=Prev*Inv3/16;"]
    hblock.extend(derivative_coefficients("H", "t", "HT", 10))
    text = text.replace("poly H=Prev*Inv3/16;", "\n".join(hblock), 1)
    for ell in range(1, 8):
        old = f"poly h{ell}=coeff(H,t,{ell + 3});"
        new = f"poly h{ell}=HTC{ell + 3};"
        if old not in text:
            fail(("missing V1 t-coefficient line", old))
        text = text.replace(old, new, 1)

    if config == "p0moving":
        old = "poly ConstCheck=coeff(PP,z,0)+m0^3;"
        text = text.replace(old, "poly ConstCheck=PZC0+m0^3;", 1)
        beta_marker = "poly PPbeta0=subst(PP,m0,0);"
        betablock = [beta_marker]
        betablock.extend(derivative_coefficients("PPbeta0", "z", "PB", 3))
        if beta_marker not in text:
            fail("missing V1 beta marker")
        text = text.replace(beta_marker, "\n".join(betablock), 1)
        old = "poly CubicCheck=coeff(PPbeta0,z,3)+m1^3;"
        text = text.replace(old, "poly CubicCheck=PBC3+m1^3;", 1)

    if "coeff(" in text:
        fail("unrepaired coeff API remains")
    text = text.replace(
        'print("SQUARE_THIRD_SHARP_SOURCE_HASHES=PASS");',
        'print("SQUARE_THIRD_SHARP_SOURCE_HASHES=PASS");\nprint("SQUARE_THIRD_SHARP_V2_PATCH=DERIVATIVE_FACTORIAL");',
        1,
    )
    return text


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--config", choices=("generic", "p0moving"), required=True)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    for path, expected in EXPECTED.items():
        actual = digest(path)
        if actual != expected:
            fail(("frozen input mismatch", str(path), actual, expected))
    tails = json.loads(TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != EXPECTED_ALL_TAILS:
        fail("canonical tail digest mismatch")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    singular = output / f"square_third_sharp_v2_{args.config}_{label}.sing"
    v1 = load_v1()
    v1.emit(singular, args.config, args.characteristic, tails)
    singular.write_text(repair(singular.read_text(), args.config))
    payload = {
        "status": "PASS-SQUARE-THIRD-SHARP-V2-COMPILER",
        "registered_aws_lane": tag,
        "config": args.config,
        "characteristic": args.characteristic,
        "v1_compiler_sha256": digest(V1),
        "v1_freeze_sha256": digest(V1_FREEZE),
        "input_sha256": digest(singular),
        "scope": "V2_COEFFICIENT_API_REPAIR_ONLY_NO_SQUARE_OR_ORDER2_VERDICT",
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
