#!/usr/bin/env python3
"""AWS-only independent-order compiler for the la20 witness cone."""

from hashlib import sha256
import importlib.util
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
BASE_COMPILER = HERE / "base_compiler.py"
BASE_B = HERE / "base_B.sing"
BASE_COMPILER_SHA = (
    "18af62ed9b9529387a6b13abf685d7001a873935023dc0ef0b33b63c6bd3171c"
)
BASE_B_SHA = "c905f1b507fda84f62950198bd9528718798c0498ee31e8cc7679479d677693b"


def require_aws() -> str:
    if platform.system() != "Linux":
        raise SystemExit("REFUSE_NON_LINUX")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        raise SystemExit("REFUSE_NON_AWS_EC2")
    tag = os.environ.get("JC2_AWS_TAG", "")
    if not tag.startswith(
        "max12_912_order3_d1_double_root_control2_la20_dp_cone_"
    ):
        raise SystemExit("REFUSE_UNREGISTERED_TAG")
    return tag


def load_base():
    if sha256(BASE_COMPILER.read_bytes()).hexdigest() != BASE_COMPILER_SHA:
        raise SystemExit("REFUSE_BASE_COMPILER_HASH")
    if sha256(BASE_B.read_bytes()).hexdigest() != BASE_B_SHA:
        raise SystemExit("REFUSE_BASE_B_HASH")
    spec = importlib.util.spec_from_file_location("frozen_la20_base", BASE_COMPILER)
    if spec is None or spec.loader is None:
        raise SystemExit("REFUSE_BASE_IMPORT")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    tag = require_aws()
    base = load_base()
    polynomials = base.extract_polynomials()
    source = base.emit(tag, polynomials)
    old_ring = "ring R=0,(s,la,tau,rho,q1,q0,r2,r1,r0),(lp(1),dp(8));"
    new_ring = "ring R=0,(s,la,tau,rho,q1,q0,r2,r1,r0),dp;"
    if source.count(old_ring) != 1:
        raise SystemExit("REFUSE_RING_ANCHOR")
    source = source.replace(old_ring, new_ring)
    source = source.replace(
        "ENCODING=EXPANDED_DIRECT_SAT_LPDP_EXPLICIT_LIFT",
        "ENCODING=EXPANDED_DIRECT_SAT_DP_EXPLICIT_LIFT_CONE",
    )
    source = source.replace(
        "PASS_CONTROL2_LA20_SYZYGY_LPDP",
        "PASS_CONTROL2_LA20_DP_CONE",
    )
    old_firewall = (
        'print("FIREWALL=FIXED_WEIGHT_SUPPORT_PREIMAGE_ONLY_'
        'CONE_INEQUALITIES_NOT_YET_AUDITED");'
    )
    cone = "\n".join(
        [
            "poly REM=DEHOMOGENIZED;",
            "poly TERM,MON;",
            "intvec EX;",
            "int TC=0;",
            "int MC=0;",
            "int WT;",
            'print("WITNESS_CONE_TERMS_BEGIN");',
            "while (REM!=0)",
            "{",
            "  TERM=lead(REM);",
            "  EX=leadexp(TERM);",
            "  if (EX[1]!=0) { print(\"FAIL_DEHOMOGENIZED_HAS_S\"); quit; }",
            "  WT=4*EX[2]+EX[3]+EX[4]+22*EX[5]+22*EX[6]",
            "     +30*EX[7]+30*EX[8]+30*EX[9];",
            "  TC++;",
            '  print("CONE_TERM_INDEX="+string(TC));',
            '  print("CONE_TERM_EXP="+string(EX));',
            '  print("CONE_TERM_WEIGHT="+string(WT));',
            '  print("CONE_TERM="+string(TERM));',
            "  if (WT<80) { print(\"FAIL_CONE_TERM_BELOW_80\"); quit; }",
            "  if (WT==80)",
            "  {",
            "    MON=TERM/leadcoef(TERM);",
            "    if (MON!=la^20) { print(\"FAIL_CONE_WEIGHT80_NONLA20\"); quit; }",
            "    MC++;",
            "  }",
            "  REM=REM-TERM;",
            "}",
            'print("WITNESS_CONE_TERMS_END");',
            'if (MC!=1) { print("FAIL_CONE_MINIMUM_COUNT"); quit; }',
            'print("WITNESS_TERM_COUNT="+string(TC));',
            'print("WITNESS_WEIGHT80_LA20_COUNT="+string(MC));',
            'print("PASS_STRICT_LA20_WITNESS_CONE_AT_REGISTERED_WEIGHT");',
            'print("FIREWALL=FIXED_SOURCE_WITNESS_CONE_ONLY_NOT_FULL_GROEBNER_FAN_OR_MOVING_PARAMETERS");',
        ]
    )
    if source.count(old_firewall) != 1:
        raise SystemExit("REFUSE_FIREWALL_ANCHOR")
    source = source.replace(old_firewall, cone)
    output = HERE / "la20_dp_cone.sing"
    output.write_text(source)
    print(f"base_compiler_sha256={BASE_COMPILER_SHA}")
    print(f"base_B_sha256={BASE_B_SHA}")
    print(f"output_sha256={sha256(output.read_bytes()).hexdigest()}")
    print("PASS_CONTROL2_LA20_DP_CONE_COMPILER")


if __name__ == "__main__":
    main()

