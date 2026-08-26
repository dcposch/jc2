#!/usr/bin/env python3
"""AWS-only literal replay of the frozen LPDP la^20 preimage certificate."""

from hashlib import sha256
import importlib.util
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
BASE_DIR = HERE.parent / "max12_912_order3_d1_double_root_control2_la20_syzygy_20260826"
BASE_COMPILER = BASE_DIR / "compile_la20_syzygy.py"
BASE_COMPILER_SHA = "18af62ed9b9529387a6b13abf685d7001a873935023dc0ef0b33b63c6bd3171c"
EXPECTED_WITNESS_STDOUT_SHA = "a0611ede0e667d45f569a954fdaa73818f0ebea328212b8c46d4ccb0aa29fe08"


def require_aws() -> str:
    if platform.system() != "Linux":
        raise SystemExit("REFUSE_NON_LINUX")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        raise SystemExit("REFUSE_NON_AWS_EC2")
    tag = os.environ.get("JC2_AWS_TAG", "")
    if not tag.startswith(
        "max12_912_order3_d1_double_root_control2_la20_witness_replay_v1_"
    ):
        raise SystemExit("REFUSE_UNREGISTERED_TAG")
    return tag


def load_base():
    if sha256(BASE_COMPILER.read_bytes()).hexdigest() != BASE_COMPILER_SHA:
        raise SystemExit("REFUSE_BASE_COMPILER_HASH")
    spec = importlib.util.spec_from_file_location("frozen_la20_base", BASE_COMPILER)
    if spec is None or spec.loader is None:
        raise SystemExit("REFUSE_BASE_IMPORT")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def emit(tag: str, p: dict[str, str]) -> str:
    lines = [
        "// Literal replay of the frozen LPDP la^20 preimage and finite cone support.",
        "ring R=0,(s,la,tau,rho,q1,q0,r2,r1,r0),(lp(1),dp(8));",
    ]
    for name in [f"E{i}" for i in range(1, 9)] + ["LT"]:
        lines.append(f"poly {name}={p[name]};")
    lines.extend(
        [
            f'print("AWS_TAG={tag}");',
            f'print("EXPECTED_PRODUCER_STDOUT_SHA256={EXPECTED_WITNESS_STDOUT_SHA}");',
            'print("ENCODING=LITERAL_NINE_GENERATOR_REES_IDENTITY_AND_TERM_ENUMERATION");',
            "ideal I=E1,E2,E3,E4,E5,E6,E7,E8,LT;",
            "ideal FINAL;",
            "FINAL[1]=1/108*s^60*q1^2-7/72*s^46*r2+1/8*s^46*r1-5/18*s^38*q1+1/8*s^38*q0+115/24*s^16;",
            "FINAL[2]=1/12*s^38*q1-5/36*s^38*q0-29/9*s^16;",
            "FINAL[3]=0;",
            "FINAL[4]=-1/24*s^38*q1+3/2*s^16;",
            "FINAL[5]=-1/24*s^38*q0-25/24*s^16;",
            "FINAL[6]=1/24*s^38*q1;",
            "FINAL[7]=3/8*s^16;",
            "FINAL[8]=-s^16;",
            "FINAL[9]=0;",
            "poly TAIL=-1/243*s^7*q1*q0^3-1/54*s*q1*r2*r1-7/108*s*q1*r1^2-1/54*s*q1*r2*r0+1/54*s*q0*r1*r0-1/108*s*q1*r0^2-la^20*tau;",
            "poly CHECK=s^96*la^20-s^97*TAIL;",
            "int i;",
            "for (i=1; i<=9; i++) { CHECK=CHECK-I[i]*FINAL[i]; }",
            'if (CHECK!=0) { print("FAIL_LITERAL_REES_IDENTITY"); CHECK; quit; }',
            'print("PASS_LITERAL_REES_IDENTITY");',
            "poly W=subst(la^20-s*TAIL,s,1);",
            "poly EXPECT=la^20*tau+la^20+1/243*q1*q0^3+1/54*q1*r2*r1+7/108*q1*r1^2+1/54*q1*r2*r0-1/54*q0*r1*r0+1/108*q1*r0^2;",
            'if (W-EXPECT!=0) { print("FAIL_DEHOMOGENIZED_WITNESS"); quit; }',
            'print("PASS_DEHOMOGENIZED_WITNESS");',
            "poly WZ=972*la^20*tau+972*la^20+4*q1*q0^3+18*q1*r2*r1+63*q1*r1^2+18*q1*r2*r0-18*q0*r1*r0+9*q1*r0^2;",
            'if (WZ-972*W!=0) { print("FAIL_PRIMITIVE_INTEGRAL_SCALE"); quit; }',
            'print("PASS_PRIMITIVE_INTEGRAL_SCALE");',
            'print("WITNESS_BEGIN"); W; print("WITNESS_END");',
            "poly REM=W;",
            "poly TERM,MON;",
            "intvec EX;",
            "int TC=0; int C80=0; int C81=0; int C82=0; int C88=0; int OTHER=0;",
            "int WT;",
            'print("TERM_ENUMERATION_BEGIN");',
            "while (REM!=0)",
            "{",
            "  TERM=lead(REM); EX=leadexp(TERM); TC++;",
            '  if (EX[1]!=0) { print("FAIL_TERM_HAS_S"); quit; }',
            '  if (EX[4]!=0) { print("FAIL_TERM_HAS_RHO"); quit; }',
            "  WT=4*EX[2]+EX[3]+EX[4]+22*EX[5]+22*EX[6]+30*EX[7]+30*EX[8]+30*EX[9];",
            '  print("TERM_INDEX="+string(TC));',
            '  print("TERM_EXP="+string(EX));',
            '  print("TERM_WEIGHT="+string(WT));',
            '  print("TERM="+string(TERM));',
            "  if (WT==80) { C80++; MON=TERM/leadcoef(TERM); if (MON!=la^20) { print(\"FAIL_WEIGHT80_NONLA20\"); quit; } }",
            "  else { if (WT==81) { C81++; } else { if (WT==82) { C82++; } else { if (WT==88) { C88++; } else { OTHER++; } } } }",
            "  REM=REM-TERM;",
            "}",
            'print("TERM_ENUMERATION_END");',
            'if (TC!=8 || C80!=1 || C81!=1 || C82!=5 || C88!=1 || OTHER!=0) { print("FAIL_TERM_WEIGHT_MULTISET"); quit; }',
            'print("TERM_COUNT="+string(TC));',
            'print("WEIGHT_MULTISET=80x1,81x1,82x5,88x1");',
            'print("PASS_UNIQUE_LA20_MINIMUM_AT_REGISTERED_WEIGHT");',
            'print("FIREWALL=FIXED_SOURCE_WITNESS_AND_ITS_FINITE_STRICT_HALFSPACES_ONLY");',
            'print("PASS_CONTROL2_LA20_WITNESS_REPLAY_V1");',
            "quit;",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    tag = require_aws()
    base = load_base()
    output = HERE / "witness_replay.sing"
    output.write_text(emit(tag, base.extract_polynomials()))
    print(f"base_compiler_sha256={BASE_COMPILER_SHA}")
    print(f"expected_witness_stdout_sha256={EXPECTED_WITNESS_STDOUT_SHA}")
    print(f"output_sha256={sha256(output.read_bytes()).hexdigest()}")
    print("PASS_CONTROL2_LA20_WITNESS_REPLAY_COMPILER")


if __name__ == "__main__":
    main()
