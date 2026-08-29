#!/usr/bin/env python3
"""Compile the exact ordinary-Faber generic odd-parity/J validator."""

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
SOURCE_REVIEW = ROOT / "xmodel/max12-812-order2-u2-62-strict-rees-compiler-v2-source-review-20260825.md"
ONEPARAM = ROOT / "xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-promotion-20260826.md"
FIRST_NORMAL_REVIEW = ROOT / "xmodel/max12-812-order2-first-normal-divisibility-jet-review-grok-20260826.md"
FABER_CLASSIFICATION = ROOT / "xmodel/max12-812-order2-exact-square-affine-mu2-faber-connection-classification-20260826.md"
EXPECTED = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    SOURCE_REVIEW: "b7666bb12ef454f5047074898e0384968393916d97bd06673d3a1f20ab70f50d",
    ONEPARAM: "82167b862a779d1104e3fb904d71627b799f48074241d8496fc1051d0a7afa2f",
    FIRST_NORMAL_REVIEW: "27275f3d13471521bec0016d4fbc6e12d5bf8e539deeb4694fe0c01f04b025bd",
    FABER_CLASSIFICATION: "77a3a2f0a04263eb5a476b3e4f3ec9da7db5500481ec73a483d504906e63a89e",
}
EXPECTED_ALL_TAILS = "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"
COEFFICIENTS = tuple(f"F{i}" for i in range(7))
LOADS = ("1", "beta", "gamma")


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only generic-J compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only generic-J compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def rational_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"({value.numerator}/{value.denominator})"


def factor_power(expression: str, exponent: int) -> str:
    if exponent == 1:
        return f"({expression})"
    return f"({expression})^{exponent}"


def faber_term(raw_monomial: list[object], raw_coefficient: object) -> str:
    monomial = [int(value) for value in raw_monomial]
    if len(monomial) != 10:
        fail(("monomial length", monomial))
    if sum(monomial[7:]) > 1 or any(value not in (0, 1) for value in monomial[7:]):
        fail(("tail load nonlinearity", monomial))
    factors: list[str] = []
    for expression, exponent in zip(COEFFICIENTS, monomial[:7]):
        if exponent:
            factors.append(factor_power(expression, exponent))
    for expression, exponent in zip(LOADS, monomial[7:]):
        if exponent and expression != "1":
            factors.append(factor_power(expression, exponent))
    coefficient = Fraction(str(raw_coefficient))
    body = "*".join(factors) or "1"
    if coefficient == 1:
        return body
    if coefficient == -1:
        return "-" + body
    return f"{rational_text(coefficient)}*{body}"


def faber_tail(entries: list[list[object]]) -> str:
    return "+".join(faber_term(m, q) for m, q in entries).replace("+-", "-") or "0"


def emit(path: Path, characteristic: int, tails: dict[str, list[list[object]]]) -> None:
    lines = [
        f"ring R={characteristic},(raw0,raw1,raw2,raw3,raw4,raw5,raw6,gamma,beta,r,p,D,s,n0,n2,n3,u,c),dp;",
        "poly pInv=raw6/2;",
        "poly cInv=raw5/2;",
        "poly rInv=(raw4-pInv^2)/2;",
        "poly n3Inv=raw3-2*pInv*cInv;",
        "poly n2Inv=raw2-cInv^2-2*pInv*rInv;",
        "poly n1Inv=raw1-2*cInv*rInv;",
        "poly n0Inv=raw0-rInv^2;",
        "poly uInv=n1Inv-(pInv/2)*n3Inv;",
        "poly Rec0=rInv^2+n0Inv;",
        "poly Rec1=2*cInv*rInv+uInv+(pInv/2)*n3Inv;",
        "poly Rec2=cInv^2+2*pInv*rInv+n2Inv;",
        "poly Rec3=2*pInv*cInv+n3Inv;",
        "poly Rec4=pInv^2+2*rInv;",
        "poly Rec5=2*cInv;",
        "poly Rec6=2*pInv;",
    ]
    for i in range(7):
        lines.append(f"int coordinate{i}=(Rec{i}-raw{i}==0);")
    lines.extend(
        [
            "int coordinates=coordinate0*coordinate1*coordinate2*coordinate3*coordinate4*coordinate5*coordinate6;",
            'print("GENERIC_J_COORDINATE_ISOMORPHISM="+string(coordinates));',
            "poly F0=r^2+n0;",
            "poly F1=2*c*r+u+(p/2)*n3;",
            "poly F2=c^2+2*p*r+n2;",
            "poly F3=2*p*c+n3;",
            "poly F4=p^2+2*r;",
            "poly F5=2*c;",
            "poly F6=2*p;",
        ]
    )
    for ell in range(1, 8):
        lines.append(f"poly R{ell}={faber_tail(tails[str(ell)])};")
    lines.extend(
        [
            "proc oddFlip(poly f)",
            "{",
            "  f=subst(f,c,-c); f=subst(f,u,-u); f=subst(f,n3,-n3);",
            "  return(f);",
            "}",
            "proc central(poly f)",
            "{",
            "  f=subst(f,c,0); f=subst(f,u,0); f=subst(f,n3,0);",
            "  f=subst(f,n0,0); f=subst(f,n2,0);",
            "  f=subst(f,r,(p^2)/4-D);",
            "  f=subst(f,beta,(5*D-s)/4);",
            "  f=subst(f,gamma,D*(5*D-4*s)/16);",
            "  return(f);",
            "}",
            "proc exactSquare(poly f)",
            "{",
            "  f=subst(f,u,0); f=subst(f,n3,0); f=subst(f,n0,0); f=subst(f,n2,0);",
            "  return(f);",
            "}",
        ]
    )
    for ell in (1, 3, 5, 7):
        lines.append(f"int parity{ell}=(R{ell}+oddFlip(R{ell})==0);")
    for ell in (2, 4, 6):
        lines.append(f"int parity{ell}=(R{ell}-oddFlip(R{ell})==0);")
    lines.extend(
        [
            "int parityAll=parity1*parity2*parity3*parity4*parity5*parity6*parity7;",
            'print("GENERIC_J_PARITY_ALL="+string(parityAll));',
            "int graphRows=(central(R1)==0)*(central(R2)-(D^2)*s/32==0)*(central(R3)==0)*(central(R4)==0)*(central(R5)==0)*(central(R6)==0)*(central(R7)==0);",
            'print("GENERIC_J_AFFINE_GRAPH_ROWS="+string(graphRows));',
            "poly avec=D*(5*D+2*s)/32;",
            "poly Cvec=(5*D-3*s)/4;",
            "poly Kvec=5*D*(5*D-2*s)/16;",
            "poly A0vec=-(p^2)/32-D/4;",
            "matrix Jac[3][3];",
            "Jac[1,1]=central(diff(R1,c)); Jac[1,2]=central(diff(R1,u)); Jac[1,3]=central(diff(R1,n3));",
            "Jac[2,1]=central(diff(R3,c)); Jac[2,2]=central(diff(R3,u)); Jac[2,3]=central(diff(R3,n3));",
            "Jac[3,1]=central(diff(R5,c)); Jac[3,2]=central(diff(R5,u)); Jac[3,3]=central(diff(R5,n3));",
            "int jacobianFormulas=(Jac[1,1]-avec==0)*(Jac[2,1]+p*avec/4==0)*(Jac[3,1]-avec*A0vec==0)",
            " *(Jac[1,2]-Cvec/4==0)*(Jac[2,2]+p*Cvec/16==0)*(Jac[3,2]-(Cvec*A0vec+Kvec)/4==0)",
            " *(Jac[1,3]==0)*(Jac[2,3]-Kvec/4==0)*(Jac[3,3]+p*Kvec/16==0);",
            'print("GENERIC_J_JACOBIAN_FORMULAS="+string(jacobianFormulas));',
            "poly detJac=det(Jac);",
            "int determinantOk=(detJac+avec*(Kvec^2)/16==0);",
            'print("GENERIC_J_DETERMINANT="+string(factorize(detJac)));',
            'print("GENERIC_J_DETERMINANT_OK="+string(determinantOk));',
            "poly g7c=central(diff(R7,c)); poly g7u=central(diff(R7,u)); poly g7n3=central(diff(R7,n3));",
            "proc Aface(poly f) { return(subst(f,s,-5*D/2)); }",
            "proc Kface(poly f) { return(subst(f,s,5*D/2)); }",
            "matrix JA[3][3]; matrix JK[3][3]; int ii; int jj;",
            "for (ii=1; ii<=3; ii++) { for (jj=1; jj<=3; jj++) { JA[ii,jj]=Aface(Jac[ii,jj]); JK[ii,jj]=Kface(Jac[ii,jj]); } }",
            "poly minorA=JA[1,2]*JA[2,3]-JA[1,3]*JA[2,2];",
            "int AfaceOk=(JA[1,1]==0)*(JA[2,1]==0)*(JA[3,1]==0)*(Aface(g7c)==0)*(minorA-625*(D^3)/1024==0);",
            'print("GENERIC_J_A_FACE_RANK2_AND_R7_KERNEL_NULL="+string(AfaceOk));',
        ]
    )
    # On the K face, row one is nonzero on D(D).  Check that every other
    # Jacobian row and the R7 row is proportional to it by all 2x2 minors.
    rank_one_checks: list[str] = ["(JK[1,1]-5*(D^2)/16==0)"]
    for row in (2, 3):
        for left, right in ((1, 2), (1, 3), (2, 3)):
            rank_one_checks.append(
                f"(JK[1,{left}]*JK[{row},{right}]-JK[1,{right}]*JK[{row},{left}]==0)"
            )
    for left, right in ((1, 2), (1, 3), (2, 3)):
        gleft = {1: "Kface(g7c)", 2: "Kface(g7u)", 3: "Kface(g7n3)"}[left]
        gright = {1: "Kface(g7c)", 2: "Kface(g7u)", 3: "Kface(g7n3)"}[right]
        rank_one_checks.append(
            f"(JK[1,{left}]*({gright})-JK[1,{right}]*({gleft})==0)"
        )
    lines.extend(
        [
            "int KfaceOk=" + "*".join(rank_one_checks) + ";",
            'print("GENERIC_J_K_FACE_RANK1_AND_R7_KERNEL_NULL="+string(KfaceOk));',
            "poly Delta=p^2-4*r;",
            "int rawCubic=(exactSquare(128*R3+32*p*R1-c^3*(5*Delta-8*beta))==0);",
            "int rawQuintic=(exactSquare(c^5+128*R5-96*p*R3-(12*p^2+32*r)*R1)==0);",
            "int rawControls=rawCubic*rawQuintic;",
            'print("GENERIC_J_RAW_CUBIC="+string(rawCubic));',
            'print("GENERIC_J_RAW_QUINTIC="+string(rawQuintic));',
            "int allPass=coordinates*parityAll*graphRows*jacobianFormulas*determinantOk*AfaceOk*KfaceOk*rawControls;",
            "if (allPass==1) {",
            '  print("GENERIC_J_ENDPOINT=PASS_GENERIC_PARITY_IFT_DATA_AND_EXCEPTIONAL_FIRST_ORDER_NULLITY");',
            "} else {",
            '  print("GENERIC_J_ENDPOINT=REPAIR_OR_FAILED_IDENTITY"); quit;',
            "}",
            'print("GENERIC_J_DONE=1");',
            'print("GENERIC_J_SCOPE=NORMALIZED_ORDINARY_FABER_FACE_ONLY_GATE_A_TOTAL_REES_EXCEPTIONAL_FANS_TERMINAL_TAYLOR_ORDER2_AND_JC2_OPEN");',
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
    for source, expected in EXPECTED.items():
        actual = digest(source)
        if actual != expected:
            fail(("frozen source mismatch", str(source), actual, expected))
    tails = json.loads(TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    singular = output / f"generic_j_exclusion_{label}.sing"
    emit(singular, args.characteristic, tails)
    payload = {
        "status": "PASS-GENERIC-J-EXCLUSION-COMPILER",
        "scope": "NORMALIZED_ORDINARY_FABER_FACE_ONLY",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "tails_sha256": digest(TAILS),
        "all_tails_sha256": EXPECTED_ALL_TAILS,
        "charged_sha256": {str(path.relative_to(ROOT)): digest(path) for path in EXPECTED},
        "input_sha256": digest(singular),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
