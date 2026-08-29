#!/usr/bin/env python3
"""Compile the A-face delayed-load early-null and repeated-root checks."""

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
        fail("AWS-only source-early-null compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only source-early-null compiler refused non-Amazon host")
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


RAW_COEFFICIENTS = (
    "r^2+n0",
    "2*c*r+n1",
    "c^2+2*p*r+n2",
    "2*p*c+n3",
    "p^2+2*r",
    "2*c",
    "2*p",
)
RAW_LOADS = ("k10", "k6", "k2")


def tail_text(entries: list[list[object]]) -> str:
    terms: list[str] = []
    for raw_monomial, raw_coefficient in entries:
        monomial = [int(value) for value in raw_monomial]
        if len(monomial) != 10:
            fail(("bad monomial length", monomial))
        pieces: list[str] = []
        for expression, exponent in zip(RAW_COEFFICIENTS + RAW_LOADS, monomial):
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
        f"ring R={characteristic},(g,b,w0,w1,w2,w3,rr,pp,v,u,e0,e2,x,t,n0,n1,n2,n3,c,k2,k6,k10,r,D,p),dp;",
        "proc tc(poly P,int n)",
        "{",
        "  int i; poly Q=P;",
        "  for (i=1; i<=n; i++) { Q=(Q-subst(Q,t,0))/t; }",
        "  return(subst(Q,t,0));",
        "}",
        "poly TC=3+5*t+7*t^2+11*t^3+13*t^4+17*t^5+19*t^6+23*t^7+29*t^8+31*t^9;",
        "int tcControl=1; int qi;",
        "intvec tv=3,5,7,11,13,17,19,23,29,31;",
        "for (qi=0; qi<=9; qi++) { tcControl=tcControl*(tc(TC,qi)==tv[qi+1]); }",
        'print("A_SOURCE_TCOEFF_CONTROL="+string(tcControl));',
    ]
    for ell in range(1, 8):
        lines.append(f"poly R{ell}={tail_text(tails[str(ell)])};")
    lines.extend(
        [
            "proc unloaded(poly P)",
            "{",
            "  P=subst(P,k10,0); P=subst(P,k6,0); P=subst(P,k2,0);",
            "  P=subst(P,r,(p^2)/4-D); P=subst(P,c,t*x);",
            "  P=subst(P,n3,t^3*v); P=subst(P,n1,t^3*(u+(p/2)*v));",
            "  P=subst(P,n2,t^2*e2); P=subst(P,n0,t^2*e0);",
            "  return(P);",
            "}",
        ]
    )
    for ell in range(1, 8):
        lines.append(f"poly U{ell}=unloaded(R{ell});")
    lines.extend(
        [
            "proc repeated(poly P)",
            "{",
            "  P=subst(P,D,(p^2)/4); P=subst(P,e0,0); P=subst(P,e2,0);",
            "  P=subst(P,u,(p/2)*v); return(P);",
            "}",
        ]
    )
    for ell in range(1, 8):
        for order in range(4, 10):
            lines.append(
                f'print("A_SOURCE_REPEATED_U{ell}_T{order}="+string(repeated(tc(U{ell},{order}))));'
            )
    lines.extend(
        [
            "proc corrected(poly P)",
            "{",
            "  P=subst(P,k10,0); P=subst(P,k6,0); P=subst(P,k2,0);",
            "  P=subst(P,p,p+t*pp); P=subst(P,r,t*rr); P=subst(P,c,t*x);",
            "  P=subst(P,n3,t^3*v+t^4*w3); P=subst(P,n2,t^4*w2);",
            "  P=subst(P,n1,t^3*p*v+t^4*w1); P=subst(P,n0,t^4*w0);",
            "  return(P);",
            "}",
        ]
    )
    for ell in range(1, 8):
        lines.append(f"poly C{ell}=corrected(R{ell});")
        lines.append(f"poly C{ell}T7=tc(C{ell},7);")
        lines.append(f'print("A_SOURCE_CORRECTED_R{ell}_T7="+string(C{ell}T7));')
    corr_lower = "*".join(
        [f"(tc(C{ell},{order})==0)" for ell in range(1, 8) for order in range(0, 7)]
    )
    corr_cancel = "*".join(
        [f"(subst(subst(C{ell}T7,w0,v*x/2),rr,0)==0)" for ell in range(1, 8)]
    )
    lines.extend(
        [
            f"int correctedLower={corr_lower};",
            "int correctedR1=(C1T7-(3/8)*v*(2*w0-v*x)==0);",
            f"int correctedCancel={corr_cancel};",
            "poly SliceR1=subst(subst(subst(subst(subst(subst(C1T7,w0,0),w1,0),w2,0),w3,0),rr,0),pp,0);",
            "int sliceControl=(SliceR1+(3/8)*(v^2)*x==0);",
            'print("A_SOURCE_CORRECTED_LOWER_ZERO="+string(correctedLower));',
            'print("A_SOURCE_CORRECTED_R1_CONTROL="+string(correctedR1));',
            'print("A_SOURCE_CORRECTED_T7_CANCEL="+string(correctedCancel));',
            'print("A_SOURCE_MONOMIAL_SLICE_R1_T7="+string(SliceR1));',
            'print("A_SOURCE_MONOMIAL_SLICE_CONTROL="+string(sliceControl));',
            "proc natural(poly P)",
            "{",
            "  P=subst(P,p,0); P=subst(P,D,1); P=subst(P,x,1);",
            "  P=subst(P,e0,0); P=subst(P,e2,0); P=subst(P,u,0);",
            "  P=subst(P,v,-1/20); return(P);",
            "}",
            "poly NaturalR2=natural(tc(U2,6)); poly NaturalR6=natural(tc(U6,6));",
            "int naturalControl=(NaturalR2-3/3200==0)*(NaturalR6-3/6400==0);",
            'print("A_SOURCE_NATURAL_R2_T6="+string(NaturalR2));',
            'print("A_SOURCE_NATURAL_R6_T6="+string(NaturalR6));',
            'print("A_SOURCE_NATURAL_CONTROL="+string(naturalControl));',
            "proc aface(poly P)",
            "{",
            "  P=subst(P,r,(p^2)/4-D); P=subst(P,k10,1);",
            "  P=subst(P,k6,15*D/8+t^2*b); P=subst(P,k2,15*(D^2)/16+t^2*g);",
            "  P=subst(P,c,t*x); P=subst(P,n3,t^3*v);",
            "  P=subst(P,n1,t^3*(u+(p/2)*v));",
            "  P=subst(P,n2,t^2*e2); P=subst(P,n0,t^2*e0); return(P);",
            "}",
            "poly A1=tc(aface(R1),3); poly A3=tc(aface(R3),3);",
            "poly A5=tc(aface(R5),3); poly AJ=4*tc(aface(R7),3);",
            "poly B1=repeated(A1); poly B3=repeated(A3);",
            "poly B5=repeated(A5); poly BJ=repeated(AJ);",
            "poly Id3=512*(B3+(p/4)*B1)-5*(p^2)*(x^3+5*(p^2)*v);",
            "poly Id5=1024*(B5-(p/4)*B3+((p^2)/32)*B1)-5*(x^3)*(p^3);",
            "int repeatedCubic=(Id3==0)*(Id5==0);",
            'print("A_SOURCE_REPEATED_B1="+string(B1));',
            'print("A_SOURCE_REPEATED_B3="+string(B3));',
            'print("A_SOURCE_REPEATED_B5="+string(B5));',
            'print("A_SOURCE_REPEATED_BJ="+string(BJ));',
            'print("A_SOURCE_REPEATED_ID3="+string(Id3));',
            'print("A_SOURCE_REPEATED_ID5="+string(Id5));',
            'print("A_SOURCE_REPEATED_CUBIC_CONTROL="+string(repeatedCubic));',
            "if (tcControl*correctedLower*correctedR1*correctedCancel*sliceControl*naturalControl*repeatedCubic==1) {",
            '  print("A_SOURCE_ENDPOINT=PASS_CORRECTION_COMPLETE_T7_CANCELLATION_AND_CUBIC_IDENTITIES");',
            '} else { print("A_SOURCE_ENDPOINT=FAIL"); quit; }',
            'print("A_SOURCE_DONE=1");',
            'print("A_SOURCE_SCOPE=DELAYED_LOAD_A_FACE_SOURCE_TRIAGE_NO_TOTAL_REES_TERMINAL_TAYLOR_ORDER2_OR_JC2_VERDICT");',
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
    emit(output / f"affine_faber_a_source_early_null_{label}.sing", args.characteristic, tails)
    payload = {
        "status": "PASS-A-SOURCE-EARLY-NULL-COMPILER",
        "scope": "DELAYED_LOAD_A_FACE_SOURCE_TRIAGE",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "tails_sha256": digest(TAILS),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
