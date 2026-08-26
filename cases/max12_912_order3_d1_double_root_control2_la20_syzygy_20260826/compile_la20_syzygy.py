#!/usr/bin/env python3
"""AWS-only compiler for an explicit la^20 Rees preimage certificate."""

from hashlib import sha256
import os
from pathlib import Path
import platform
import re


HERE = Path(__file__).resolve().parent
BASE = HERE / "base_B.sing"
BASE_SHA = "c905f1b507fda84f62950198bd9528718798c0498ee31e8cc7679479d677693b"
POLYS = [f"E{i}" for i in range(1, 9)] + ["LT"]


def require_aws() -> str:
    if platform.system() != "Linux":
        raise SystemExit("REFUSE_NON_LINUX")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        raise SystemExit("REFUSE_NON_AWS_EC2")
    tag = os.environ.get("JC2_AWS_TAG", "")
    if not tag.startswith(
        "max12_912_order3_d1_double_root_control2_la20_syzygy_"
    ):
        raise SystemExit("REFUSE_UNREGISTERED_TAG")
    return tag


def extract_polynomials() -> dict[str, str]:
    if sha256(BASE.read_bytes()).hexdigest() != BASE_SHA:
        raise SystemExit("REFUSE_BASE_B_HASH")
    text = BASE.read_text()
    out = {}
    for name in POLYS:
        matches = re.findall(rf"^poly {name}=(.*);$", text, flags=re.MULTILINE)
        if len(matches) != 1:
            raise SystemExit(f"REFUSE_POLY_ANCHOR_{name}_{len(matches)}")
        out[name] = matches[0]
    return out


def emit(tag: str, polynomials: dict[str, str]) -> str:
    lines = [
        "// Explicit la^20 Rees preimage, fixed control-2 weight/support.",
        'LIB "elim.lib";',
        "ring R=0,(s,la,tau,rho,q1,q0,r2,r1,r0),(lp(1),dp(8));",
        "option(redSB);",
    ]
    for name in POLYS:
        lines.append(f"poly {name}={polynomials[name]};")
    lines.extend(
        [
            f'print("AWS_TAG={tag}");',
            'print("ENCODING=EXPANDED_DIRECT_SAT_LPDP_EXPLICIT_LIFT");',
            "ideal CS=s;",
            "ideal TOYI=s^2*(q1+1);",
            "list TOYS=sat_with_exp(TOYI,CS);",
            "int TOYN=TOYS[2];",
            "ideal TOYC=TOYS[1];",
            'if (TOYN!=2) { print("FAIL_TOY_SAT_EXPONENT"); quit; }',
            "ideal TOYSC=s^TOYN*TOYC;",
            "matrix TOYL=lift(TOYI,TOYSC);",
            "matrix TOYR=matrix(TOYSC)-matrix(TOYI)*TOYL;",
            'if (TOYR!=0) { print("FAIL_TOY_LIFT_ORIENTATION"); quit; }',
            'print("PASS_TOY_SATURATION_AND_LIFT");',
            "ideal I=E1,E2,E3,E4,E5,E6,E7,E8,LT;",
            "list SW=sat_with_exp(I,CS);",
            "ideal C=SW[1];",
            "int N=SW[2];",
            'print("S_SATURATION_EXPONENT="+string(N));',
            'print("S_SATURATION_GENERATORS="+string(size(C)));',
            "ideal CD=sat(I,CS);",
            "ideal GCD=std(CD);",
            "int i,j;",
            "for (i=1; i<=size(C); i++)",
            "{",
            '  if (reduce(C[i],GCD)!=0) { print("FAIL_SAT_FORWARD"); quit; }',
            "}",
            "for (i=1; i<=size(GCD); i++)",
            "{",
            '  if (reduce(GCD[i],C)!=0) { print("FAIL_SAT_REVERSE"); quit; }',
            "}",
            'print("PASS_SAT_WITH_EXP_DIRECT_EQUALITY");',
            "ideal H=C,s;",
            "ideal TARGET=la^20;",
            "matrix LH=lift(H,TARGET);",
            "matrix RH=matrix(TARGET)-matrix(H)*LH;",
            'if (RH!=0) { print("FAIL_H_LIFT"); quit; }',
            'print("PASS_H_LIFT");',
            "ideal USED;",
            "list HCOEFF;",
            "int nused=0;",
            "for (i=1; i<=size(C); i++)",
            "{",
            "  if (LH[i,1]!=0)",
            "  {",
            "    nused++;",
            "    USED[nused]=C[i];",
            "    HCOEFF[nused]=LH[i,1];",
            '    print("USED_C_INDEX="+string(i));',
            "  }",
            "}",
            'if (nused==0) { print("FAIL_EMPTY_H_SUPPORT"); quit; }',
            'print("USED_C_GENERATORS="+string(nused));',
            "ideal SUN=s^N*USED;",
            "matrix LU=lift(I,SUN);",
            "matrix RU=matrix(SUN)-matrix(I)*LU;",
            'if (RU!=0) { print("FAIL_USED_C_LIFT"); quit; }',
            'print("PASS_USED_C_LIFT");',
            "ideal FINAL;",
            "poly cc,hc;",
            "for (i=1; i<=size(I); i++)",
            "{",
            "  cc=0;",
            "  for (j=1; j<=nused; j++)",
            "  {",
            "    hc=HCOEFF[j];",
            "    cc=cc+LU[i,j]*hc;",
            "  }",
            "  FINAL[i]=cc;",
            "}",
            "poly TAIL=LH[size(C)+1,1];",
            "poly CHECK=s^N*la^20-s^(N+1)*TAIL;",
            "for (i=1; i<=size(I); i++)",
            "{",
            "  CHECK=CHECK-I[i]*FINAL[i];",
            "}",
            'if (CHECK!=0) { print("FAIL_FINAL_REES_IDENTITY"); CHECK; quit; }',
            'print("PASS_FINAL_REES_IDENTITY");',
            'print("CERTIFICATE_FINAL_I_COEFFS_BEGIN");',
            "FINAL;",
            'print("CERTIFICATE_FINAL_I_COEFFS_END");',
            'print("CERTIFICATE_TAIL_BEGIN");',
            "TAIL;",
            'print("CERTIFICATE_TAIL_END");',
            "poly DEHOMOGENIZED=subst(la^20-s*TAIL,s,1);",
            'print("DEHOMOGENIZED_WITNESS_BEGIN");',
            "DEHOMOGENIZED;",
            'print("DEHOMOGENIZED_WITNESS_END");',
            'print("FIREWALL=FIXED_WEIGHT_SUPPORT_PREIMAGE_ONLY_CONE_INEQUALITIES_NOT_YET_AUDITED");',
            'print("PASS_CONTROL2_LA20_SYZYGY_LPDP");',
            "quit;",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    tag = require_aws()
    polynomials = extract_polynomials()
    output = HERE / "la20_syzygy_lpdp.sing"
    output.write_text(emit(tag, polynomials))
    print(f"base_B_sha256={BASE_SHA}")
    print(f"output_sha256={sha256(output.read_bytes()).hexdigest()}")
    print("polynomial_anchors=9")
    print("PASS_CONTROL2_LA20_SYZYGY_COMPILER")


if __name__ == "__main__":
    main()

