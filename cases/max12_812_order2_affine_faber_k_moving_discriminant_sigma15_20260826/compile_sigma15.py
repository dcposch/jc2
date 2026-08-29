#!/usr/bin/env python3
"""Compile the exact moving-discriminant sigma recursion through grade 15."""

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
        fail("AWS-only moving-discriminant compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only moving-discriminant compiler refused non-Amazon host")
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
    "qr^2+n0",
    "2*qc*qr+n1",
    "qc^2+2*qp*qr+n2",
    "2*qp*qc+n3",
    "qp^2+2*qr",
    "2*qc",
    "2*qp",
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


def series(prefix: str, first: int, last: int) -> str:
    return "+".join(f"s^{j}*{prefix}{j}" for j in range(first, last + 1)) or "0"


def emit(path: Path, characteristic: int, tails: dict[str, list[list[object]]]) -> None:
    normal_vars = [f"n{degree}{order}" for order in range(6, 11) for degree in range(4)]
    tangent_vars = [f"a{order}" for order in range(1, 6)] + [f"e{order}" for order in range(1, 6)]
    variables = ["satu", *reversed(normal_vars), *reversed(tangent_vars), "lam", "p", "s", "n0", "n1", "n2", "n3", "qr", "qc", "qp", "k2", "k6", "k10"]
    lines = [
        f"ring R={characteristic},({','.join(variables)}),dp;",
        "proc tc(poly P,int n)",
        "{",
        "  int i; poly Q=P;",
        "  for (i=1; i<=n; i++) { Q=(Q-subst(Q,s,0))/s; }",
        "  return(subst(Q,s,0));",
        "}",
        "poly TC=3+5*s+7*s^2+11*s^3+13*s^4+17*s^5+19*s^6+23*s^7+29*s^8+31*s^9+37*s^10+41*s^11+43*s^12+47*s^13+53*s^14+59*s^15;",
        "int tcControl=1; int qi;",
        "intvec tv=3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59;",
        "for (qi=0; qi<=15; qi++) { tcControl=tcControl*(tc(TC,qi)==tv[qi+1]); }",
        'print("K_SIGMA15_TCOEFF_CONTROL="+string(tcControl));',
    ]
    for ell in range(1, 8):
        lines.append(f"poly R{ell}={tail_text(tails[str(ell)])};")
    a_series = series("a", 1, 5)
    e_series = "p+" + series("e", 1, 5)
    normal_series = {
        3: "s^5*lam+" + series("n3", 6, 10),
        2: series("n2", 6, 10),
        1: "s^5*lam*p+" + series("n1", 6, 10),
        0: series("n0", 6, 10),
    }
    lines.extend(
        [
            f"poly aa={a_series};",
            f"poly ee={e_series};",
            "poly QP=ee-6*(aa^2);",
            "poly QC=2*aa*(4*(aa^2)-ee);",
            "poly QR=(aa^2)*(ee-3*(aa^2));",
            f"poly N3={normal_series[3]};",
            f"poly N2={normal_series[2]};",
            f"poly N1={normal_series[1]};",
            f"poly N0={normal_series[0]};",
            "proc movingdisc(poly P)",
            "{",
            "  P=subst(P,k10,0); P=subst(P,k6,0); P=subst(P,k2,0);",
            "  P=subst(P,qp,QP); P=subst(P,qc,QC); P=subst(P,qr,QR);",
            "  P=subst(P,n3,N3); P=subst(P,n2,N2);",
            "  P=subst(P,n1,N1); P=subst(P,n0,N0); return(P);",
            "}",
        ]
    )
    generators: list[str] = []
    for ell in range(1, 8):
        lines.append(f"poly S{ell}=movingdisc(R{ell});")
        for order in range(10, 16):
            lines.append(f"poly G{ell}_{order}=tc(S{ell},{order});")
            lines.append(f'print("K_SIGMA15_R{ell}_G{order}="+string(G{ell}_{order}));')
            generators.append(f"G{ell}_{order}")
    lower = "*".join(
        [f"(tc(S{ell},{order})==0)" for ell in range(1, 8) for order in range(0, 10)]
    )
    lines.extend(
        [
            f"int lowerControl={lower};",
            'print("K_SIGMA15_LOWER_ZERO="+string(lowerControl));',
            f"ideal I={','.join(generators)},satu*p*lam-1;",
            "ideal G=std(I);",
            "int unitControl=(reduce(1,G)==0);",
            'print("K_SIGMA15_STD_BEGIN"); print(G); print("K_SIGMA15_STD_END");',
            'print("K_SIGMA15_UNIT="+string(unitControl));',
            'print("K_SIGMA15_DIM="+string(dim(G)));',
            "if (tcControl*lowerControl==1) {",
            '  print("K_SIGMA15_ENDPOINT=PASS_COMPLETE_EMISSION_AND_STANDARD_BASIS");',
            '} else { print("K_SIGMA15_ENDPOINT=FAIL_CONTROL"); quit; }',
            'print("K_SIGMA15_DONE=1");',
            'print("K_SIGMA15_SCOPE=EXACT_MOVING_DOUBLE_ROOT_CHART_ONLY_NO_ROOT_SPLITTING_TOTAL_FAN_TERMINAL_TAYLOR_ORDER2_OR_JC2_VERDICT");',
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
    emit(output / f"affine_faber_k_moving_disc_sigma15_{label}.sing", args.characteristic, tails)
    payload = {
        "status": "PASS-K-MOVING-DISC-SIGMA15-COMPILER",
        "scope": "EXACT_MOVING_DOUBLE_ROOT_SIGMA15",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "tails_sha256": digest(TAILS),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
