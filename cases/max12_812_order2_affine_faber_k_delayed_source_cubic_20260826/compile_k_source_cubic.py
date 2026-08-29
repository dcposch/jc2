#!/usr/bin/env python3
"""Compile the correction-complete repeated-root K source cubic."""

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
        fail("AWS-only K-source compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only K-source compiler refused non-Amazon host")
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
    "r^2+n0",
    "2*c*r+n1",
    "c^2+2*p*r+n2",
    "2*p*c+n3",
    "p^2+2*r",
    "2*c",
    "2*p",
)
LOADS = ("k10", "k6", "k2")


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
        f"ring R={characteristic},(w0,w1,w2,w3,rr,pp,x,t,n0,n1,n2,n3,c,k2,k6,k10,r,p),dp;",
        "proc tc(poly P,int n)",
        "{",
        "  int i; poly Q=P;",
        "  for (i=1; i<=n; i++) { Q=(Q-subst(Q,t,0))/t; }",
        "  return(subst(Q,t,0));",
        "}",
        "poly TC=3+5*t+7*t^2+11*t^3;",
        "int tcControl=(tc(TC,0)==3)*(tc(TC,1)==5)*(tc(TC,2)==7)*(tc(TC,3)==11);",
        'print("K_SOURCE_TCOEFF_CONTROL="+string(tcControl));',
    ]
    for ell in range(1, 8):
        lines.append(f"poly R{ell}={tail_text(tails[str(ell)])};")
    lines.extend(
        [
            "proc ksource(poly P)",
            "{",
            "  P=subst(P,k10,0); P=subst(P,k6,0); P=subst(P,k2,0);",
            "  P=subst(P,p,p+t*pp); P=subst(P,r,t*rr); P=subst(P,c,t*x);",
            "  P=subst(P,n3,t*p*x+t^2*w3); P=subst(P,n2,t^2*w2);",
            "  P=subst(P,n1,t*(p^2)*x+t^2*w1); P=subst(P,n0,t^2*w0);",
            "  return(P);",
            "}",
        ]
    )
    for ell in range(1, 8):
        lines.append(f"poly S{ell}=ksource(R{ell});")
        lines.append(f"poly S{ell}T2=tc(S{ell},2); poly S{ell}T3=tc(S{ell},3);")
        lines.append(f'print("K_SOURCE_R{ell}_T2="+string(S{ell}T2));')
        lines.append(f'print("K_SOURCE_R{ell}_T3="+string(S{ell}T3));')
    lower = "*".join(
        [f"(tc(S{ell},{order})==0)" for ell in range(1, 8) for order in range(0, 2)]
    )
    lines.extend(
        [
            f"int lowerControl={lower};",
            "poly CubicCert=S3T3-(p/4)*S1T3-(pp/4)*S1T2;",
            "int cubicControl=(CubicCert+(1/16)*(p^3)*(x^3)==0);",
            'print("K_SOURCE_LOWER_ZERO="+string(lowerControl));',
            'print("K_SOURCE_CUBIC_CERT="+string(CubicCert));',
            'print("K_SOURCE_CUBIC_CONTROL="+string(cubicControl));',
            "if (tcControl*lowerControl*cubicControl==1) {",
            '  print("K_SOURCE_ENDPOINT=PASS_REPEATED_ROOT_CORRECTION_INDEPENDENT_CUBIC_UNIT");',
            '} else { print("K_SOURCE_ENDPOINT=FAIL"); quit; }',
            'print("K_SOURCE_DONE=1");',
            'print("K_SOURCE_SCOPE=DELAYED_LOAD_REPEATED_ROOT_K_FACE_NO_TOTAL_FAN_TERMINAL_TAYLOR_ORDER2_OR_JC2_VERDICT");',
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
    emit(output / f"affine_faber_k_source_cubic_{label}.sing", args.characteristic, tails)
    payload = {
        "status": "PASS-K-SOURCE-CUBIC-COMPILER",
        "scope": "DELAYED_LOAD_REPEATED_ROOT_K_FACE",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "tails_sha256": digest(TAILS),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
