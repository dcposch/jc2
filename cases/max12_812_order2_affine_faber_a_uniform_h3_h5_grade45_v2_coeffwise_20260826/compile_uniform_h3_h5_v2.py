#!/usr/bin/env python3
"""Emit a coefficientwise exact universal H3/H5 certificate."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import os
from pathlib import Path
import platform
import tempfile


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V1_PATH = ROOT / "cases/max12_812_order2_affine_faber_a_uniform_h3_h5_grade45_20260826/compile_uniform_h3_h5.py"
V1_SHA = "713957b25e2619dd9c93c0c55cbd4b3080795bee01d3b0f10d75a5fd0babe846"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only V2 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only V2 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_v1():
    if digest(V1_PATH) != V1_SHA:
        fail("frozen V1 compiler mismatch")
    spec = importlib.util.spec_from_file_location("uniform_h35_v1", V1_PATH)
    if spec is None or spec.loader is None:
        fail("cannot load V1 compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def emit(path: Path, characteristic: int, v1, loaded, base, tails) -> None:
    with tempfile.TemporaryDirectory(prefix="jc2-uniform-h35-v2-") as temporary:
        seed = Path(temporary) / "seed.sing"
        loaded.emit(seed, characteristic, "q6x", base, tails)
        source = seed.read_text()
    anchor = "ideal I="
    if source.count(anchor) != 1:
        fail("loaded-kernel source anchor is missing or nonunique")
    prefix = source.split(anchor, 1)[0]
    prefix = "\n".join(
        line for line in prefix.splitlines()
        if 'print("A_LK45_R' not in line
    ) + "\n"
    row_truncations = []
    for ell in (1, 3, 5):
        terms = "+".join(f"s^{grade}*G{ell}_{grade}" for grade in range(42, 46))
        row_truncations.append(f"poly P{ell}T={terms};")
    suffix = [
        "poly BB=4*aa;",
        "int bOrderControl=(tc(BB,0)==0)*(tc(BB,1)==0)*(tc(BB,2)==0)*(tc(BB,3)==0)*(tc(BB,4)==0);",
        'print("A_UH35V2_B_ORDER_GE5="+string(bOrderControl));',
        *row_truncations,
        "poly H3T=P3T-(1/4)*EE*P1T;",
        "poly H5T=P5T-(3/4)*EE*P3T+(5/32)*EE^2*P1T;",
        "poly EXPECT3=-(3/8)*s^30*MM*XX*YY-(1/16)*s^45*MM^3;",
        "poly EXPECT5=(3/8)*s^30*EE*MM*XX*YY;",
        "ideal S46=std(ideal(s^46));",
        "int rawH3=(reduce(H3T-EXPECT3,S46)==0);",
        "int rawH5=(reduce(H5T-EXPECT5,S46)==0);",
        'print("A_UH35V2_RAW_H3_MOD_S46="+string(rawH3));',
        'print("A_UH35V2_RAW_H5_MOD_S46="+string(rawH5));',
        "poly K=EE*H3T+H5T;",
        "ideal S45=std(ideal(s^45));",
        "int lowerK=(reduce(K,S45)==0);",
        "poly K45=tc(K,45);",
        "int k45Certificate=(16*K45+p*m^3==0);",
        'print("A_UH35V2_K_LOWER_ZERO="+string(lowerK));',
        'print("A_UH35V2_K45="+string(K45));',
        'print("A_UH35V2_K45_CERTIFICATE="+string(k45Certificate));',
        "ideal I=K45,satu*p*m*kk-1;",
        "ideal G=std(I);",
        "int unitControl=(reduce(1,G)==0);",
        'print("A_UH35V2_UNIT="+string(unitControl));',
        "if (tcControl*lowerControl*bOrderControl*rawH3*rawH5*lowerK*k45Certificate*unitControl==1) { print(\"A_UH35V2_ENDPOINT=PASS_COEFFICIENTWISE_RAW_UNIVERSAL_H3_H5_AND_LOCALIZED_UNIT\"); }",
        'else { print("A_UH35V2_ENDPOINT=FAIL_CONTROL_OR_IDENTITY"); quit; }',
        'print("A_UH35V2_DONE=1");',
        'print("A_UH35V2_SCOPE=COMPLETE_SOURCE_COEFFICIENTWISE_MOD_S46_EXACT_MOVING_DISCRIMINANT_ORD_XY_GE6_DELAYED_LOAD_D_P_M_KK_NO_Q_LT6_COVERAGE_TERMINAL_TAYLOR_ORDER2_OR_JC2_VERDICT");',
        "quit;",
    ]
    path.write_text(prefix + "\n".join(suffix) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    v1 = load_v1()
    loaded = v1.load_loaded()
    base = loaded.load_base()
    tails = __import__("json").loads(base.TAILS.read_text())
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    emit(output / f"affine_faber_a_uniform_h3_h5_v2_{label}.sing", args.characteristic, v1, loaded, base, tails)
    payload = {
        "status": "PASS-A-UNIFORM-H3-H5-V2-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "v1_compiler_sha256": digest(V1_PATH),
        "loaded_compiler_sha256": digest(v1.LOADED_PATH),
        "design_sha256": digest(v1.DESIGN_PATH),
        "direct_unit_addendum_sha256": digest(v1.ADDENDUM_PATH),
        "tails_sha256": digest(base.TAILS),
    }
    (output / "result.json").write_text(__import__("json").dumps(payload, sort_keys=True, indent=2) + "\n")
    print(__import__("json").dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
