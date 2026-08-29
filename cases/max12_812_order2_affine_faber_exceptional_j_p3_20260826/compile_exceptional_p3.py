#!/usr/bin/env python3
"""Compile exact ordinary-Faber controls and the two exceptional cubic J faces."""

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
        fail("AWS-only exceptional-P3 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only exceptional-P3 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def rational_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"({value.numerator}/{value.denominator})"


def factor(expression: str, exponent: int) -> str:
    if exponent == 1:
        return f"({expression})"
    return f"({expression})^{exponent}"


def tail_text(
    entries: list[list[object]], coefficients: tuple[str, ...], loads: tuple[str, ...]
) -> str:
    terms: list[str] = []
    for raw_monomial, raw_coefficient in entries:
        monomial = [int(value) for value in raw_monomial]
        if len(monomial) != 10:
            fail(("bad monomial length", monomial))
        pieces: list[str] = []
        for expression, exponent in zip(coefficients + loads, monomial):
            if exponent:
                pieces.append(factor(expression, exponent))
        coefficient = Fraction(str(raw_coefficient))
        body = "*".join(pieces) or "1"
        if coefficient == 1:
            terms.append(body)
        elif coefficient == -1:
            terms.append("-" + body)
        else:
            terms.append(f"{rational_text(coefficient)}*{body}")
    return "+".join(terms).replace("+-", "-") or "0"


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


HEADER = [
    'LIB "primdec.lib";',
    "proc tc(poly P,int n)",
    "{",
    "  int i; poly Q=P;",
    "  for (i=1; i<=n; i++) { Q=(Q-subst(Q,t,0))/t; }",
    "  return(subst(Q,t,0));",
    "}",
    "poly TC=3+5*t+7*t^2+11*t^3;",
    "int tcControl=(tc(TC,0)==3)*(tc(TC,1)==5)*(tc(TC,2)==7)*(tc(TC,3)==11);",
    'print("EXCEPTIONAL_P3_TCOEFF_CONTROL="+string(tcControl));',
    'if (tcControl!=1) { print("EXCEPTIONAL_P3_FAIL=TCOEFF"); quit; }',
]


def raw_rows(tails: dict[str, list[list[object]]]) -> list[str]:
    return [
        f"poly R{ell}={tail_text(tails[str(ell)], RAW_COEFFICIENTS, RAW_LOADS)};"
        for ell in range(1, 8)
    ]


def emit_controls(path: Path, characteristic: int, tails: dict[str, list[list[object]]]) -> None:
    ring = (
        f"ring R={characteristic},"
        "(t,u,n0,n1,n2,n3,c,k2,k6,k10,r,s,D,p),dp;"
    )
    lines = [ring, *HEADER, *raw_rows(tails)]
    lines.extend(
        [
            "poly Delta=p^2-4*r;",
            "poly E1=subst(subst(subst(subst(subst(R1,n0,0),n1,0),n2,0),n3,0),k10,1);",
            "poly E3=subst(subst(subst(subst(subst(R3,n0,0),n1,0),n2,0),n3,0),k10,1);",
            "poly E5=subst(subst(subst(subst(subst(R5,n0,0),n1,0),n2,0),n3,0),k10,1);",
            "poly RawC5=c^5+128*E5-96*p*E3-(12*p^2+32*r)*E1;",
            "poly RawC3=128*E3+32*p*E1-c^3*(5*Delta-8*k6);",
            "int rawC5=(RawC5==0); int rawC3=(RawC3==0);",
            'print("EXCEPTIONAL_P3_RAW_C5="+string(rawC5));',
            'print("EXCEPTIONAL_P3_RAW_C3="+string(rawC3));',
            "proc graph(poly P)",
            "{",
            "  P=subst(P,n1,u+(p/2)*n3);",
            "  P=subst(P,r,(p^2)/4-D);",
            "  P=subst(P,k10,1);",
            "  P=subst(P,k6,(5*D-s)/4);",
            "  P=subst(P,k2,D*(5*D-4*s)/16);",
            "  return(P);",
            "}",
            "proc base(poly P)",
            "{",
            "  P=subst(P,c,0); P=subst(P,u,0); P=subst(P,n3,0);",
            "  P=subst(P,n2,0); P=subst(P,n0,0); return(P);",
            "}",
            "poly G1=graph(R1); poly G3=graph(R3); poly G5=graph(R5);",
            "poly C0=(5*D-3*s)/4; poly K0=5*D*(5*D-2*s)/16;",
            "poly B0=-(p^2)/32-D/4; poly q0=D*(5*D+2*s)/32;",
            "poly M11=base(diff(G1,c)); poly M12=base(diff(G1,u)); poly M13=base(diff(G1,n3));",
            "poly M21=base(diff(G3,c)); poly M22=base(diff(G3,u)); poly M23=base(diff(G3,n3));",
            "poly M31=base(diff(G5,c)); poly M32=base(diff(G5,u)); poly M33=base(diff(G5,n3));",
            "int matrixControl=(M11-q0==0)*(M12-C0/4==0)*(M13==0)",
            " *(M21+p*q0/4==0)*(M22+p*C0/16==0)*(M23-K0/4==0)",
            " *(M31-q0*B0==0)*(M32-(C0*B0+K0)/4==0)*(M33+p*K0/16==0);",
            "poly Det=M11*(M22*M33-M23*M32)-M12*(M21*M33-M23*M31)+M13*(M21*M32-M22*M31);",
            "int detControl=(Det+q0*(K0^2)/16==0);",
            'print("EXCEPTIONAL_P3_MATRIX="+string(matrixControl));',
            'print("EXCEPTIONAL_P3_DETERMINANT="+string(detControl));',
            "proc point(poly P)",
            "{",
            "  P=subst(P,c,0); P=subst(P,n1,0); P=subst(P,n3,0);",
            "  P=subst(P,n2,0); P=subst(P,n0,0);",
            "  P=subst(P,r,(p^2)/4-D); P=subst(P,k10,1);",
            "  P=subst(P,k6,(5*D-s)/4); P=subst(P,k2,D*(5*D-4*s)/16);",
            "  return(P);",
            "}",
            "poly B6=point(diff(R6,k6)); poly G6=point(diff(R6,k2));",
            "poly B2=point(diff(R2,k6)); poly G2=point(diff(R2,k2));",
            "poly EvenDet=B6*G2-G6*B2;",
            "int evenPivot=(EvenDet-(D^4)/64==0);",
            'print("EXCEPTIONAL_P3_EVEN_PIVOT="+string(evenPivot));',
            "if (rawC5*rawC3*matrixControl*detControl*evenPivot==1) {",
            '  print("EXCEPTIONAL_P3_CONTROLS=PASS");',
            "} else { print(\"EXCEPTIONAL_P3_CONTROLS=FAIL\"); quit; }",
            'print("EXCEPTIONAL_P3_CONTROLS_DONE=1");',
            "quit;",
        ]
    )
    path.write_text("\n".join(lines) + "\n")


def emit_a(path: Path, characteristic: int, tails: dict[str, list[list[object]]]) -> None:
    ring = (
        f"ring R={characteristic},"
        "(satv,v,u,e0,e2,g,b,x,t,n0,n1,n2,n3,c,k2,k6,k10,r,D,p),dp;"
    )
    lines = [ring, *HEADER, *raw_rows(tails)]
    substitutions = [
        ("r", "(p^2)/4-D"),
        ("k10", "1"),
        ("k6", "15*D/8+t^2*b"),
        ("k2", "15*(D^2)/16+(t^2)*g"),
        ("c", "t*x"),
        ("n3", "t^3*v"),
        ("n1", "t^3*(u+(p/2)*v)"),
        ("n2", "t^2*e2"),
        ("n0", "t^2*e0"),
    ]
    lines.append("proc aface(poly P)")
    lines.append("{")
    for variable, expression in substitutions:
        lines.append(f"  P=subst(P,{variable},{expression});")
    lines.extend(["  return(P);", "}"])
    for ell in (1, 3, 5, 7):
        lines.append(f"poly A{ell}=aface(R{ell});")
        lines.append(f"poly A{ell}w3=tc(A{ell},3);")
    lines.extend(
        [
            "int lowerA=(tc(A1,1)==0)*(tc(A1,2)==0)*(tc(A3,1)==0)*(tc(A3,2)==0)",
            " *(tc(A5,1)==0)*(tc(A5,2)==0)*(tc(A7,1)==0)*(tc(A7,2)==0);",
            'print("EXCEPTIONAL_P3_A_LOWER_ZERO="+string(lowerA));',
            'print("EXCEPTIONAL_P3_A_R1_W3="+string(A1w3));',
            'print("EXCEPTIONAL_P3_A_R3_W3="+string(A3w3));',
            'print("EXCEPTIONAL_P3_A_R5_W3="+string(A5w3));',
            'print("EXCEPTIONAL_P3_A_J_W3="+string(4*A7w3));',
            "ideal IA=A1w3,A3w3,A5w3,satv*x*(4*A7w3)-1; ideal GA=std(IA);",
            "int aUnit=(reduce(1,GA)==0);",
            'print("EXCEPTIONAL_P3_A_JSAT_UNIT="+string(aUnit));',
            'print("EXCEPTIONAL_P3_A_JSAT_DIM="+string(dim(GA)));',
            "if (lowerA==1) { print(\"EXCEPTIONAL_P3_A=PASS_WEIGHTED_CUBIC_EMISSION\"); }",
            "else { print(\"EXCEPTIONAL_P3_A=FAIL_LOWER_TERM\"); quit; }",
            'print("EXCEPTIONAL_P3_A_DONE=1");',
            "quit;",
        ]
    )
    path.write_text("\n".join(lines) + "\n")


def emit_k(path: Path, characteristic: int, tails: dict[str, list[list[object]]]) -> None:
    ring = (
        f"ring R={characteristic},"
        "(satv,v,y,x,u,e0,e2,g,b,t,n0,n1,n2,n3,c,k2,k6,k10,r,D,p),dp;"
    )
    lines = [ring, *HEADER, *raw_rows(tails)]
    substitutions = [
        ("r", "(p^2)/4-D"),
        ("k10", "1"),
        ("k6", "5*D/8+(t^2)*b"),
        ("k2", "-5*(D^2)/16+(t^2)*g"),
        ("c", "t*x"),
        ("n3", "t*y"),
        ("n1", "2*D*t*x+(p/2)*t*y+t^3*u"),
        ("n2", "t^2*e2"),
        ("n0", "t^2*e0"),
    ]
    lines.append("proc kface(poly P)")
    lines.append("{")
    for variable, expression in substitutions:
        lines.append(f"  P=subst(P,{variable},{expression});")
    lines.extend(["  return(P);", "}"])
    for ell in (1, 3, 5, 7):
        lines.append(f"poly K{ell}=kface(R{ell});")
        lines.append(f"poly K{ell}w3=tc(K{ell},3);")
    lines.extend(
        [
            "int lowerK=(tc(K1,1)==0)*(tc(K1,2)==0)*(tc(K3,1)==0)*(tc(K3,2)==0)",
            " *(tc(K5,1)==0)*(tc(K5,2)==0)*(tc(K7,1)==0)*(tc(K7,2)==0);",
            'print("EXCEPTIONAL_P3_K_LOWER_ZERO="+string(lowerK));',
            'print("EXCEPTIONAL_P3_K_R1_W3="+string(K1w3));',
            'print("EXCEPTIONAL_P3_K_R3_W3="+string(K3w3));',
            'print("EXCEPTIONAL_P3_K_R5_W3="+string(K5w3));',
            'print("EXCEPTIONAL_P3_K_J_W3="+string(4*K7w3));',
            "poly Kx1=subst(subst(K1w3,x,1),y,v);",
            "poly Kx3=subst(subst(K3w3,x,1),y,v);",
            "poly Kx5=subst(subst(K5w3,x,1),y,v);",
            "poly KxJ=subst(subst(4*K7w3,x,1),y,v);",
            "ideal IKx=Kx1,Kx3,Kx5,satv*KxJ-1; ideal GKx=std(IKx);",
            "int kxUnit=(reduce(1,GKx)==0);",
            "poly Ky1=subst(subst(K1w3,y,1),x,v);",
            "poly Ky3=subst(subst(K3w3,y,1),x,v);",
            "poly Ky5=subst(subst(K5w3,y,1),x,v);",
            "poly KyJ=subst(subst(4*K7w3,y,1),x,v);",
            "ideal IKy=Ky1,Ky3,Ky5,satv*KyJ-1; ideal GKy=std(IKy);",
            "int kyUnit=(reduce(1,GKy)==0);",
            'print("EXCEPTIONAL_P3_KX_JSAT_UNIT="+string(kxUnit));',
            'print("EXCEPTIONAL_P3_KX_JSAT_DIM="+string(dim(GKx)));',
            'print("EXCEPTIONAL_P3_KY_JSAT_UNIT="+string(kyUnit));',
            'print("EXCEPTIONAL_P3_KY_JSAT_DIM="+string(dim(GKy)));',
            "if (lowerK==1) { print(\"EXCEPTIONAL_P3_K=PASS_WEIGHTED_CUBIC_EMISSION\"); }",
            "else { print(\"EXCEPTIONAL_P3_K=FAIL_LOWER_TERM\"); quit; }",
            'print("EXCEPTIONAL_P3_K_DONE=1");',
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
        fail(("frozen tails mismatch", digest(TAILS), EXPECTED_TAILS))
    tails = json.loads(TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != EXPECTED_CANONICAL:
        fail("canonical tail digest mismatch")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    emit_controls(output / f"exceptional_controls_{label}.sing", args.characteristic, tails)
    emit_a(output / f"exceptional_A_{label}.sing", args.characteristic, tails)
    emit_k(output / f"exceptional_K_{label}.sing", args.characteristic, tails)
    payload = {
        "status": "PASS-EXCEPTIONAL-P3-COMPILER",
        "scope": "NORMALIZED_ORDINARY_FABER_EXCEPTIONAL_WEIGHTED_CUBIC_ONLY",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "tails_sha256": digest(TAILS),
        "canonical_tails_sha256": EXPECTED_CANONICAL,
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
