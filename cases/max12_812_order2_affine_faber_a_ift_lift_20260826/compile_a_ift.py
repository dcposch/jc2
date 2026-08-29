#!/usr/bin/env python3
"""Compile the exact rational A-face point, IFT determinant, and next even jet."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TAILS = (
    ROOT
    / "cases/max12_812_order2_u2_62_strict_rees_20260825"
    / "aws_compile_v2_jsat/run/output/compiled_v2/tails.json"
)
EXPECTED_TAILS = "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848"
EXPECTED_CANONICAL = "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only A-IFT compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only A-IFT compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def qtext(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"({value.numerator}/{value.denominator})"


def factor(expression: str, exponent: int) -> str:
    if exponent == 1:
        return f"({expression})"
    return f"({expression})^{exponent}"


COEFFICIENTS = (
    "1+(t^2)*e0",
    "-2*t+(t^3)*u",
    "t^2",
    "(t^3)*v",
    "-2",
    "2*t",
    "0",
)
LOADS = ("1", "15/8", "15/16")


def tail_text(entries: list[list[object]]) -> str:
    terms: list[str] = []
    for raw_monomial, raw_coefficient in entries:
        monomial = [int(value) for value in raw_monomial]
        if len(monomial) != 10:
            fail(("bad monomial length", monomial))
        pieces: list[str] = []
        for expression, exponent in zip(COEFFICIENTS + LOADS, monomial):
            if exponent:
                pieces.append(factor(expression, exponent))
        coefficient = Fraction(str(raw_coefficient))
        body = "*".join(pieces) or "1"
        if coefficient == 1:
            terms.append(body)
        elif coefficient == -1:
            terms.append("-" + body)
        else:
            terms.append(f"{qtext(coefficient)}*{body}")
    return "+".join(terms).replace("+-", "-") or "0"


def emit(path: Path, characteristic: int, tails: dict[str, list[list[object]]]) -> None:
    lines = [
        'LIB "primdec.lib";',
        f"ring R={characteristic},(E2,V2,U2,e0,v,u,t),dp;",
        "proc tc(poly P,int n)",
        "{",
        "  int i; poly Q=P;",
        "  for (i=1; i<=n; i++) { Q=(Q-subst(Q,t,0))/t; }",
        "  return(subst(Q,t,0));",
        "}",
        "poly TC=3+5*t+7*t^2+11*t^3;",
        "int tcControl=(tc(TC,0)==3)*(tc(TC,1)==5)*(tc(TC,2)==7)*(tc(TC,3)==11);",
        'print("A_IFT_TCOEFF_CONTROL="+string(tcControl));',
    ]
    for ell in range(1, 8):
        lines.append(f"poly R{ell}={tail_text(tails[str(ell)])};")
    for ell in (1, 3, 5, 7):
        lines.append(f"poly S{ell}=R{ell}/(t^3);")
        lines.append(f"int Div{ell}=(R{ell}-(t^3)*S{ell}==0);")
    lines.extend(
        [
            "int divisions=Div1*Div3*Div5*Div7;",
            'print("A_IFT_EXACT_DIVISIONS="+string(divisions));',
            "proc witness(poly P)",
            "{",
            "  P=subst(P,t,0); P=subst(P,u,0); P=subst(P,v,-1/20);",
            "  P=subst(P,e0,0); return(P);",
            "}",
            "poly W1=witness(S1); poly W3=witness(S3); poly W5=witness(S5);",
            "poly WJ=witness(4*S7);",
            "int pointControl=(W1==0)*(W3==0)*(W5==0)*(WJ+5/32==0);",
            'print("A_IFT_POINT_R1="+string(W1));',
            'print("A_IFT_POINT_R3="+string(W3));',
            'print("A_IFT_POINT_R5="+string(W5));',
            'print("A_IFT_POINT_J="+string(WJ));',
            'print("A_IFT_POINT_CONTROL="+string(pointControl));',
            "poly M11=witness(diff(S1,u)); poly M12=witness(diff(S1,v)); poly M13=witness(diff(S1,e0));",
            "poly M21=witness(diff(S3,u)); poly M22=witness(diff(S3,v)); poly M23=witness(diff(S3,e0));",
            "poly M31=witness(diff(S5,u)); poly M32=witness(diff(S5,v)); poly M33=witness(diff(S5,e0));",
            "poly Det=M11*(M22*M33-M23*M32)-M12*(M21*M33-M23*M31)+M13*(M21*M32-M22*M31);",
            "int jacControl=(Det+3125/8192==0);",
            'print("A_IFT_JAC_ROW1="+string(M11)+","+string(M12)+","+string(M13));',
            'print("A_IFT_JAC_ROW3="+string(M21)+","+string(M22)+","+string(M23));',
            'print("A_IFT_JAC_ROW5="+string(M31)+","+string(M32)+","+string(M33));',
            'print("A_IFT_JAC_DET="+string(Det));',
            'print("A_IFT_JAC_CONTROL="+string(jacControl));',
            "proc nextjet(poly P)",
            "{",
            "  P=subst(P,u,(t^2)*U2);",
            "  P=subst(P,v,-1/20+(t^2)*V2);",
            "  P=subst(P,e0,(t^2)*E2);",
            "  return(tc(P,2));",
            "}",
            "poly N1=nextjet(S1); poly N3=nextjet(S3); poly N5=nextjet(S5);",
            "ideal NI=std(ideal(N1,N3,N5));",
            "poly NJ=nextjet(4*S7);",
            'print("A_IFT_NEXT_R1="+string(N1));',
            'print("A_IFT_NEXT_R3="+string(N3));',
            'print("A_IFT_NEXT_R5="+string(N5));',
            'print("A_IFT_NEXT_STD_BEGIN"); print(NI); print("A_IFT_NEXT_STD_END");',
            'print("A_IFT_NEXT_J="+string(NJ));',
            "if (tcControl*divisions*pointControl*jacControl==1) {",
            '  print("A_IFT_ENDPOINT=PASS_RATIONAL_J_POINT_AND_FORMAL_IFT");',
            "} else { print(\"A_IFT_ENDPOINT=FAIL\"); quit; }",
            'print("A_IFT_DONE=1");',
            'print("A_IFT_SCOPE=NORMALIZED_ORDINARY_FABER_ONLY_NO_TOTAL_REES_TERMINAL_TAYLOR_ORDER2_OR_JC2_VERDICT");',
            "quit;",
        ]
    )
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    if digest(TAILS) != EXPECTED_TAILS:
        fail("frozen tails mismatch")
    tails = json.loads(TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != EXPECTED_CANONICAL:
        fail("canonical tails mismatch")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    emit(output / f"affine_faber_a_ift_{label}.sing", args.characteristic, tails)
    payload = {
        "status": "PASS-A-IFT-COMPILER",
        "scope": "NORMALIZED_ORDINARY_FABER_A_FACE_IFT_ONLY",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "tails_sha256": digest(TAILS),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
