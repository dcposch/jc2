#!/usr/bin/env python3
"""AWS-only minimal repair of the frozen V1 LPDP witness source."""

from hashlib import sha256
import importlib.util
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
V1_DIR = HERE.parent / "max12_912_order3_d1_double_root_control2_la20_syzygy_20260826"
V1_COMPILER = V1_DIR / "compile_la20_syzygy.py"
V1_COMPILER_SHA = "18af62ed9b9529387a6b13abf685d7001a873935023dc0ef0b33b63c6bd3171c"
V1_TAG = "max12_912_order3_d1_double_root_control2_la20_syzygy_20260826T015817Z_r6d_LPDP"
V1_SOURCE_SHA = "2d22f9867aceb250d8df6002fc4a541fffd225dfb6f8b18d3bbce2aab0f75737"


def require_aws() -> str:
    if platform.system() != "Linux":
        raise SystemExit("REFUSE_NON_LINUX")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        raise SystemExit("REFUSE_NON_AWS_EC2")
    tag = os.environ.get("JC2_AWS_TAG", "")
    if not tag.startswith(
        "max12_912_order3_d1_double_root_control2_la20_syzygy_v2_"
    ):
        raise SystemExit("REFUSE_UNREGISTERED_TAG")
    return tag


def load_v1():
    if sha256(V1_COMPILER.read_bytes()).hexdigest() != V1_COMPILER_SHA:
        raise SystemExit("REFUSE_V1_COMPILER_HASH")
    spec = importlib.util.spec_from_file_location("frozen_la20_v1", V1_COMPILER)
    if spec is None or spec.loader is None:
        raise SystemExit("REFUSE_V1_IMPORT")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    tag = require_aws()
    v1 = load_v1()
    polynomials = v1.extract_polynomials()
    reference = v1.emit(V1_TAG, polynomials)
    if sha256(reference.encode()).hexdigest() != V1_SOURCE_SHA:
        raise SystemExit("REFUSE_V1_SOURCE_RECONSTRUCTION")
    if reference.count(V1_TAG) != 1:
        raise SystemExit("REFUSE_V1_TAG_ANCHOR")
    if reference.count("GCD") != 4 or reference.count("CDSTD") != 0:
        raise SystemExit("REFUSE_GCD_REPAIR_ANCHORS")
    source = reference.replace(V1_TAG, tag).replace("GCD", "CDSTD")
    if "GCD" in source or source.count("CDSTD") != 4:
        raise SystemExit("REFUSE_GCD_REPAIR_RESULT")
    output = HERE / "la20_syzygy_v2_lpdp.sing"
    output.write_text(source)
    print(f"v1_compiler_sha256={V1_COMPILER_SHA}")
    print(f"v1_source_sha256={V1_SOURCE_SHA}")
    print(f"v2_source_sha256={sha256(output.read_bytes()).hexdigest()}")
    print("source_diff=ONE_TAG_REPLACEMENT_PLUS_FOUR_GCD_TO_CDSTD_TOKEN_REPLACEMENTS")
    print("PASS_CONTROL2_LA20_SYZYGY_V2_COMPILER")


if __name__ == "__main__":
    main()
