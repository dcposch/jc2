#!/usr/bin/env python3
"""AWS-only source-preserving compiler for the A-fast order race."""

from hashlib import sha256
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
BASE = HERE / "base_A.sing"
BASE_SHA256 = "2b416cb8209dd9d220d8f57ec78044bddb7d83d5ea4899d59ab7b4b6b4f49e52"
OLD_TAG = "max12_912_order3_d1_double_root_control2_rees_v2_20260826T005028Z_r6d_B"
OLD_RING = "ring R=0,(s,la,tau,rho,q1,q0,r2,r1,r0),dp;"
NEW_RING = "ring R=0,(s,la,tau,rho,q1,q0,r2,r1,r0),(lp(1),dp(8));"
ANCHOR = 'print("A_SPECIAL_FIBRE_GENERATORS="+string(size(GH)));\n'


def main() -> None:
    if platform.system() != "Linux":
        raise SystemExit("REFUSE_NON_LINUX")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        raise SystemExit("REFUSE_NON_AWS_EC2")
    tag = os.environ.get("JC2_AWS_TAG", "")
    if not tag.startswith("max12_912_order3_d1_double_root_control2_rees_Afast_"):
        raise SystemExit("REFUSE_UNREGISTERED_TAG")
    if sha256(BASE.read_bytes()).hexdigest() != BASE_SHA256:
        raise SystemExit("REFUSE_BASE_HASH")
    source = BASE.read_text()
    for needle in (OLD_TAG, OLD_RING, ANCHOR):
        if source.count(needle) != 1:
            raise SystemExit("REFUSE_ANCHOR_COUNT")
    source = source.replace(OLD_TAG, tag).replace(OLD_RING, NEW_RING)
    source = source.replace(
        'print("ENCODING=A_FACTORED_REES_SAT_DP_V2");',
        'print("ENCODING=A_FACTORED_REES_SAT_LPDP_V2_AFAST");',
    )
    source = source.replace(
        ANCHOR,
        ANCHOR + 'print("FULL_SPECIAL_FIBRE_BASIS_BEGIN");\nGH;\n'
        'print("FULL_SPECIAL_FIBRE_BASIS_END");\n',
    )
    source = source.replace(
        'print("PASS_D1_DOUBLE_ROOT_CONTROL2_REES_V2_A");',
        'print("PASS_D1_DOUBLE_ROOT_CONTROL2_REES_V2_A");\n'
        'print("PASS_D1_DOUBLE_ROOT_CONTROL2_REES_AFAST");',
    )
    output = HERE / "compiled_Afast.sing"
    output.write_text(source)
    print(f"base_sha256={BASE_SHA256}")
    print(f"output_sha256={sha256(output.read_bytes()).hexdigest()}")
    print("PASS_CONTROL2_REES_AFAST_COMPILER")


if __name__ == "__main__":
    main()

