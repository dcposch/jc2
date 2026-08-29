#!/usr/bin/env python3
"""Compile the raw universal H3/H5 certificate through sigma grade 45."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform
import tempfile


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
LOADED_PATH = ROOT / "cases/max12_812_order2_affine_faber_a_loaded_kernel_sigma45_20260826/compile_loaded_kernel.py"
LOADED_SHA = "a32372ce3fd088be74a3456f63c17bcb880c2eaf32c1856e86eb52d7b15f385a"
DESIGN_PATH = ROOT / "xmodel/max12-812-order2-affine-faber-a-universal-h3-h5-composition-design-20260826.md"
DESIGN_SHA = "d7dcd91c8a50e8ac20eb8806d3fe9e9abf5b7562fa89c0bfc6e3ef09bd095409"
ADDENDUM_PATH = ROOT / "xmodel/max12-812-order2-affine-faber-a-universal-h3-h5-composition-design-v2-direct-unit-20260826.md"
ADDENDUM_SHA = "78766c9df5dbf95fad5bdff531657f58cb7445e30575a58a59cec656b00d9a63"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only uniform H3/H5 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only uniform H3/H5 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_loaded():
    if digest(LOADED_PATH) != LOADED_SHA:
        fail("frozen loaded-kernel compiler mismatch")
    if digest(DESIGN_PATH) != DESIGN_SHA:
        fail("frozen universal-composition design mismatch")
    if digest(ADDENDUM_PATH) != ADDENDUM_SHA:
        fail("frozen direct-unit addendum mismatch")
    spec = importlib.util.spec_from_file_location("loaded_kernel", LOADED_PATH)
    if spec is None or spec.loader is None:
        fail("cannot load loaded-kernel compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def emit(path: Path, characteristic: int, loaded, base, tails) -> None:
    with tempfile.TemporaryDirectory(prefix="jc2-uniform-h35-") as temporary:
        seed = Path(temporary) / "seed.sing"
        loaded.emit(seed, characteristic, "q6x", base, tails)
        source = seed.read_text()
    anchor = "ideal I="
    if source.count(anchor) != 1:
        fail("loaded-kernel source anchor is missing or nonunique")
    prefix = source.split(anchor, 1)[0]
    suffix = [
        "poly BB=4*aa;",
        "poly H3=P3-(1/2)*BB*P2+((5/32)*BB^2-(1/4)*EE)*P1;",
        "poly H5=P5-BB*P4+((21/32)*BB^2-(3/4)*EE)*P3+(-(5/16)*BB^3+(3/4)*BB*EE)*P2+((195/2048)*BB^4-(45/128)*BB^2*EE+(5/32)*EE^2)*P1;",
        "poly EXPECT3=-(3/8)*s^30*MM*XX*YY-(1/16)*s^45*MM^3;",
        "poly EXPECT5=(3/8)*s^30*EE*MM*XX*YY;",
        "ideal S46=std(ideal(s^46));",
        "int rawH3=(reduce(H3-EXPECT3,S46)==0);",
        "int rawH5=(reduce(H5-EXPECT5,S46)==0);",
        'print("A_UH35_RAW_H3_MOD_S46="+string(rawH3));',
        'print("A_UH35_RAW_H5_MOD_S46="+string(rawH5));',
        "poly K=EE*H3+H5;",
        "ideal S45=std(ideal(s^45));",
        "int lowerK=(reduce(K,S45)==0);",
        "poly K45=tc(K,45);",
        "int k45Certificate=(16*K45+p*m^3==0);",
        'print("A_UH35_K_LOWER_ZERO="+string(lowerK));',
        'print("A_UH35_K45="+string(K45));',
        'print("A_UH35_K45_CERTIFICATE="+string(k45Certificate));',
        "ideal I=K45,satu*p*m*kk-1;",
        "ideal G=std(I);",
        "int unitControl=(reduce(1,G)==0);",
        'print("A_UH35_UNIT="+string(unitControl));',
        'print("A_UH35_DIM="+string(dim(G)));',
        "if (tcControl*lowerControl*rawH3*rawH5*lowerK*k45Certificate*unitControl==1) { print(\"A_UH35_ENDPOINT=PASS_RAW_UNIVERSAL_H3_H5_AND_LOCALIZED_UNIT\"); }",
        'else { print("A_UH35_ENDPOINT=FAIL_CONTROL_OR_IDENTITY"); quit; }',
        'print("A_UH35_DONE=1");',
        'print("A_UH35_SCOPE=EXACT_MOVING_DISCRIMINANT_FORMAL_CHART_ORD_XY_GE6_DELAYED_LOAD_D_P_M_KK_NO_Q_LT6_COVERAGE_TERMINAL_TAYLOR_ORDER2_OR_JC2_VERDICT");',
        "quit;",
    ]
    path.write_text(prefix + "\n".join(suffix) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    loaded = load_loaded()
    base = loaded.load_base()
    if digest(base.TAILS) != base.EXPECTED_TAILS:
        fail("frozen tails mismatch")
    tails = json.loads(base.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != base.EXPECTED_CANONICAL:
        fail("canonical tails mismatch")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    emit(output / f"affine_faber_a_uniform_h3_h5_{label}.sing", args.characteristic, loaded, base, tails)
    payload = {
        "status": "PASS-A-UNIFORM-H3-H5-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "loaded_compiler_sha256": digest(LOADED_PATH),
        "design_sha256": digest(DESIGN_PATH),
        "direct_unit_addendum_sha256": digest(ADDENDUM_PATH),
        "tails_sha256": digest(base.TAILS),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
