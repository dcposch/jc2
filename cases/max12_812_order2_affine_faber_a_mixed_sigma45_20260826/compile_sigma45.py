#!/usr/bin/env python3
"""Compile exact complete-source affine-Faber A mixed sigma-45 identity."""

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
TAILS = ROOT / "cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json"
EXPECTED_TAILS = "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848"
EXPECTED_CANONICAL = "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only sigma45 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only sigma45 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def qtext(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"({value.numerator}/{value.denominator})"


def factor(expression: str, exponent: int) -> str:
    return f"({expression})" if exponent == 1 else f"({expression})^{exponent}"


COEFFICIENTS = (
    "qr^2+n0", "2*qc*qr+n1", "qc^2+2*qp*qr+n2", "2*qp*qc+n3",
    "qp^2+2*qr", "2*qc", "2*qp",
)
LOADS = ("k10", "k6", "k2")


def tail_text(entries: list[list[object]]) -> str:
    terms: list[str] = []
    for raw_monomial, raw_coefficient in entries:
        monomial = [int(value) for value in raw_monomial]
        if len(monomial) != 10:
            fail(("bad monomial length", monomial))
        pieces = [factor(expression, exponent) for expression, exponent in zip(COEFFICIENTS + LOADS, monomial) if exponent]
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
    variables = [
        "mu23", "mu22", "mu21", "mu20",
        "k23", "k22", "k21", "k63", "k62", "k61", "k103", "k102", "k101", "kk",
        "S0", "S1", "R0", "R1", "m", "x", "p", "s",
        "n0", "n1", "n2", "n3", "qr", "qc", "qp", "k2", "k6", "k10",
    ]
    lines = [
        f"ring R={characteristic},({','.join(variables)}),dp;",
        "proc tc(poly P,int n)", "{", "  int i; poly Q=P;",
        "  for (i=1; i<=n; i++) { Q=(Q-subst(Q,s,0))/s; }",
        "  return(subst(Q,s,0));", "}",
        "poly TC=3+5*s+7*s^2+11*s^3+13*s^4+17*s^5+19*s^6+23*s^7+29*s^8+31*s^9+37*s^10+41*s^11+43*s^12+47*s^13+53*s^14+59*s^15+61*s^16+67*s^17+71*s^18+73*s^19+79*s^20+83*s^21+89*s^22+97*s^23+101*s^24+103*s^25+107*s^26+109*s^27+113*s^28+127*s^29+131*s^30+137*s^31+139*s^32+149*s^33+151*s^34+157*s^35+163*s^36+167*s^37+173*s^38+179*s^39+181*s^40+191*s^41+193*s^42+197*s^43+199*s^44+211*s^45;",
        "int tcControl=1; int qi;",
        "intvec tv=3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211;",
        "for (qi=0; qi<=45; qi++) { tcControl=tcControl*(tc(TC,qi)==tv[qi+1]); }",
        'print("A_SIGMA45_TCOEFF_CONTROL="+string(tcControl));',
    ]
    for ell in range(1, 8):
        lines.append(f"poly T{ell}={tail_text(tails[str(ell)])};")
    lines.extend([
        "poly aa=s^5*x; poly ee=p; poly dd=ee-3*aa^2;",
        "poly QP=ee-6*aa^2;",
        "poly QC=2*aa*(4*aa^2-ee)+s^15*R1;",
        "poly QR=aa^2*(ee-3*aa^2)+s^15*(R0-aa*R1);",
        "poly MM=s^15*m;",
        "poly N3=MM; poly N2=aa*MM;",
        "poly N1=(dd-2*aa^2)*MM+s^30*S1;",
        "poly N0=-aa*dd*MM+s^30*(S0-aa*S1);",
        "poly LK10=s^42*(kk+s*k101+s^2*k102+s^3*k103);",
        "poly LK6=s^42*((15/32)*kk*p^2+s*k61+s^2*k62+s^3*k63);",
        "poly LK2=s^42*((15/256)*kk*p^4+s*k21+s^2*k22+s^3*k23);",
        "poly MU2=s^42*(mu20+s*mu21+s^2*mu22+s^3*mu23);",
        "proc source(poly P)", "{",
        "  P=subst(P,k10,LK10); P=subst(P,k6,LK6); P=subst(P,k2,LK2);",
        "  P=subst(P,qp,QP); P=subst(P,qc,QC); P=subst(P,qr,QR);",
        "  P=subst(P,n3,N3); P=subst(P,n2,N2); P=subst(P,n1,N1); P=subst(P,n0,N0);",
        "  return(P);", "}",
    ])
    for ell in range(1, 8):
        target = "-MU2" if ell == 2 else ""
        lines.append(f"poly P{ell}=source(T{ell}){target};")
        for grade in range(42, 46):
            lines.append(f'print("A_SIGMA45_R{ell}_G{grade}="+string(tc(P{ell},{grade})));')
    lines.extend([
        "poly bb=4*aa;",
        "poly H3=P3-(bb/2)*P2+((5/32)*bb^2-ee/4)*P1;",
        "int lowerControl=1; for (qi=0; qi<=44; qi++) { lowerControl=lowerControl*(tc(H3,qi)==0); }",
        "poly H345=tc(H3,45);",
        "int cert=(16*H345+m^3==0);",
        'print("A_SIGMA45_H3_LOWER_ZERO="+string(lowerControl));',
        'print("A_SIGMA45_H3_G45="+string(H345));',
        'print("A_SIGMA45_EXPECTED_G45="+string(-(m^3)/16));',
        'print("A_SIGMA45_CERT="+string(cert));',
        "if (tcControl*lowerControl*cert==1) { print(\"A_SIGMA45_ENDPOINT=PASS_COMPLETE_SOURCE_H3_MINUS_M3_OVER_16\"); }",
        'else { print("A_SIGMA45_ENDPOINT=FAIL_CONTROL_OR_IDENTITY"); quit; }',
        'print("A_SIGMA45_DONE=1");',
        'print("A_SIGMA45_SCOPE=DELAYED_LOAD_REPEATED_A_TOWER_THROUGH_SIGMA45_ONLY_NO_TERMINAL_TAYLOR_ORDER2_OR_JC2_VERDICT");',
        "quit;",
    ])
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
    emit(output / f"affine_faber_a_mixed_sigma45_{label}.sing", args.characteristic, tails)
    payload = {"status": "PASS-A-MIXED-SIGMA45-COMPILER", "scope": "DELAYED_LOAD_REPEATED_A_SIGMA45", "registered_aws_lane": tag, "characteristic": args.characteristic, "tails_sha256": digest(TAILS)}
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
