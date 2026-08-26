#!/usr/bin/env python3
"""AWS-only minimum individual saturation-exponent witness race."""

from hashlib import sha256
import importlib.util
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
CASES = HERE.parent
V2_DIR = CASES / "max12_912_order3_d1_double_root_control2_la20_syzygy_v2_20260826"
V1_DIR = CASES / "max12_912_order3_d1_double_root_control2_la20_syzygy_20260826"
V2_COMPILER = V2_DIR / "compile_la20_syzygy_v2.py"
V1_COMPILER = V1_DIR / "compile_la20_syzygy.py"
V2_COMPILER_SHA = "fcd9e8d642c4aa4e3463674163ac1532d092faa85555a98843eeb957841e74e1"
V1_COMPILER_SHA = "18af62ed9b9529387a6b13abf685d7001a873935023dc0ef0b33b63c6bd3171c"
V2_TAG = "max12_912_order3_d1_double_root_control2_la20_syzygy_v2_20260826T021500Z_r6d_LPDP"
V2_SOURCE_SHA = "e9b2c1594460cc8a6053654f0fcd810522044c6b1ef89d6e92ec2fb0038fd894"


def require_aws() -> str:
    if platform.system() != "Linux":
        raise SystemExit("REFUSE_NON_LINUX")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        raise SystemExit("REFUSE_NON_AWS_EC2")
    tag = os.environ.get("JC2_AWS_TAG", "")
    if not tag.startswith(
        "max12_912_order3_d1_double_root_control2_la20_syzygy_minexp_v3_"
    ):
        raise SystemExit("REFUSE_UNREGISTERED_TAG")
    return tag


def load_module(path: Path, expected: str, name: str):
    if sha256(path.read_bytes()).hexdigest() != expected:
        raise SystemExit(f"REFUSE_{name}_HASH")
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"REFUSE_{name}_IMPORT")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def reconstruct_v2() -> str:
    v2 = load_module(V2_COMPILER, V2_COMPILER_SHA, "frozen_v2")
    v1 = load_module(V1_COMPILER, V1_COMPILER_SHA, "frozen_v1")
    reference = v1.emit(v2.V1_TAG, v1.extract_polynomials())
    source = reference.replace(v2.V1_TAG, V2_TAG).replace("GCD", "CDSTD")
    if sha256(source.encode()).hexdigest() != V2_SOURCE_SHA:
        raise SystemExit("REFUSE_V2_SOURCE_RECONSTRUCTION")
    return source


def main() -> None:
    tag = require_aws()
    source = reconstruct_v2()
    if source.count(V2_TAG) != 1:
        raise SystemExit("REFUSE_V2_TAG_ANCHOR")
    source = source.replace(V2_TAG, tag)
    old_lift = "\n".join(
        [
            "ideal SUN=s^N*USED;",
            "matrix LU=lift(I,SUN);",
        ]
    )
    new_lift = "\n".join(
        [
            'if (nused!=1) { print("FAIL_MINEXP_REQUIRES_ONE_USED_GENERATOR"); quit; }',
            "ideal ISTD=std(I);",
            "int M=0;",
            "poly TEST=USED[1];",
            "while (reduce(TEST,ISTD)!=0 && M<N)",
            "{",
            "  M++;",
            "  TEST=s*TEST;",
            "}",
            'if (reduce(TEST,ISTD)!=0) { print("FAIL_MINEXP_NOT_FOUND"); quit; }',
            'print("INDIVIDUAL_SATURATION_EXPONENT="+string(M));',
            "ideal SUN=s^M*USED;",
            "matrix LU=lift(I,SUN);",
        ]
    )
    if source.count(old_lift) != 1:
        raise SystemExit("REFUSE_LIFT_ANCHOR")
    source = source.replace(old_lift, new_lift)
    old_check = "poly CHECK=s^N*la^20-s^(N+1)*TAIL;"
    new_check = "poly CHECK=s^M*la^20-s^(M+1)*TAIL;"
    if source.count(old_check) != 1:
        raise SystemExit("REFUSE_CHECK_ANCHOR")
    source = source.replace(old_check, new_check)
    source = source.replace(
        "ENCODING=EXPANDED_DIRECT_SAT_LPDP_EXPLICIT_LIFT",
        "ENCODING=EXPANDED_DIRECT_SAT_LPDP_MINIMUM_INDIVIDUAL_EXPONENT_LIFT",
    )
    source = source.replace(
        "PASS_CONTROL2_LA20_SYZYGY_LPDP",
        "PASS_CONTROL2_LA20_SYZYGY_MINEXP_V3_LPDP",
    )
    output = HERE / "la20_syzygy_minexp_v3_lpdp.sing"
    output.write_text(source)
    print(f"v2_compiler_sha256={V2_COMPILER_SHA}")
    print(f"v2_source_sha256={V2_SOURCE_SHA}")
    print(f"v3_source_sha256={sha256(output.read_bytes()).hexdigest()}")
    print("source_diff=TAG_MARKERS_PLUS_MINIMUM_INDIVIDUAL_EXPONENT_SEARCH_AND_USE")
    print("PASS_CONTROL2_LA20_SYZYGY_MINEXP_V3_COMPILER")


if __name__ == "__main__":
    main()
