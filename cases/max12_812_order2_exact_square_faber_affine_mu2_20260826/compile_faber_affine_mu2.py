#!/usr/bin/env python3
"""Compile the literal exact-square Faber affine-mu2 support client."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
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
PELL_COMPILER = ROOT / "cases/max12_812_order2_exact_square_pell_20260826/compile_exact_square_pell.py"
ONEPARAM = ROOT / "xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-promotion-20260826.md"
SOURCE_REVIEW = ROOT / "xmodel/max12-812-order2-u2-62-strict-rees-compiler-v2-source-review-20260825.md"
PADE = ROOT / "xmodel/max12-812-order2-first-normal-pade-support-promotion-20260826.md"
EXPECTED = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    PELL_COMPILER: "b3a1aba11d181b230bf03a6ca46fd9355753c45758706d8887a8aeb7a0bbf1cd",
    ONEPARAM: "82167b862a779d1104e3fb904d71627b799f48074241d8496fc1051d0a7afa2f",
    SOURCE_REVIEW: "b7666bb12ef454f5047074898e0384968393916d97bd06673d3a1f20ab70f50d",
    PADE: "40790378bfcc7b0e0719038ef0e951712abef570b4865c0bca371409706c9f94",
}
EXPECTED_ALL_TAILS = "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"
COEFFICIENTS = (
    "r^2",
    "2*c*r",
    "c^2+2*p*r",
    "2*p*c",
    "p^2+2*r",
    "2*c",
    "2*p",
)
LOADS = ("1", "beta", "gamma")


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only Faber affine compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only Faber affine compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_pell_module():
    spec = importlib.util.spec_from_file_location("frozen_exact_square_pell", PELL_COMPILER)
    if spec is None or spec.loader is None:
        fail("cannot load frozen Pell compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


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


def emit(path: Path, characteristic: int, tails: dict[str, list[list[object]]], pell) -> None:
    hdata = pell.tail_equations()
    lines = [
        'LIB "primdec.lib";',
        f"ring R={characteristic},(mu2,gamma,beta,r,c,p),dp;",
        "proc idealZero(ideal A, ideal G)",
        "{",
        "  int i;",
        "  for (i=1; i<=size(A); i++) { if (reduce(A[i],G)!=0) { return(0); } }",
        "  return(1);",
        "}",
    ]
    for ell in range(1, 8):
        lines.append(f"poly R{ell}={faber_tail(tails[str(ell)])};")
        denominator, numerator = hdata[ell - 1]
        lines.append(f"poly H{ell}=({pell.singular_text(numerator)})/{denominator};")
    connection_rhs = {
        1: "H1",
        2: "H2",
        3: "H3+(p/4)*H1",
        4: "H4+(p/2)*H2+(c/4)*H1",
        5: "H5+(3*p/4)*H3+(c/2)*H2+((p^2)/32+r/4)*H1",
        6: "H6+p*H4+(3*c/4)*H3+((p^2)/8+r/2)*H2+(p*c/8)*H1",
        7: "H7+(5*p/4)*H5+c*H4+((9*p^2)/32+3*r/4)*H3+(3*p*c/8)*H2+(-(p^3)/128+3*p*r/16+(3*c^2)/32)*H1",
    }
    for ell in range(1, 8):
        lines.append(f"poly Connection{ell}=R{ell}-({connection_rhs[ell]});")
        lines.append(f"int connection{ell}=(Connection{ell}==0);")
        lines.append(f'print("FABER_AFFINE_CONNECTION_{ell}="+string(connection{ell}));')
    lines.extend(
        [
            "int connections=connection1*connection2*connection3*connection4*connection5*connection6*connection7;",
            'print("FABER_AFFINE_CONNECTIONS="+string(connections));',
            'if (connections!=1) { print("FABER_AFFINE_FAIL=CONNECTION"); quit; }',
            "ideal I=R1,R2-mu2,R3,R4,R5,R6,R7;",
            "ideal Raw=std(I);",
            "ideal Rad=std(radical(Raw));",
            "poly Delta=p^2-4*r;",
            "ideal Square=std(ideal(c,Delta,mu2));",
            "ideal Affine=std(ideal(c,15*Delta^2-64*beta*Delta+256*gamma,Delta^2*(5*Delta-16*beta)-2048*mu2));",
            "ideal Expected=std(intersect(Square,Affine));",
            "int expectedSolutions=idealZero(I,Expected);",
            "int radInExpected=idealZero(Rad,Expected);",
            "int expectedInRad=idealZero(Expected,Rad);",
            "ideal OffC=std(sat(Raw,ideal(c)));",
            "int offCUnit=(reduce(1,OffC)==0);",
            "list Ass=minAssGTZ(Raw);",
            "int minassTwo=(size(Ass)==2);",
            'print("FABER_AFFINE_RAW_BEGIN"); print(Raw); print("FABER_AFFINE_RAW_END");',
            'print("FABER_AFFINE_RADICAL_BEGIN"); print(Rad); print("FABER_AFFINE_RADICAL_END");',
            'print("FABER_AFFINE_EXPECTED_BEGIN"); print(Expected); print("FABER_AFFINE_EXPECTED_END");',
            'print("FABER_AFFINE_RAW_DIM="+string(dim(Raw)));',
            'print("FABER_AFFINE_EXPECTED_SOLUTIONS="+string(expectedSolutions));',
            'print("FABER_AFFINE_RAD_IN_EXPECTED="+string(radInExpected));',
            'print("FABER_AFFINE_EXPECTED_IN_RAD="+string(expectedInRad));',
            'print("FABER_AFFINE_OFF_C_UNIT="+string(offCUnit));',
            'print("FABER_AFFINE_MINASS_COUNT="+string(size(Ass)));',
            "int ai;",
            "for (ai=1; ai<=size(Ass); ai++) {",
            '  print("FABER_AFFINE_MINASS_"+string(ai)+"_BEGIN");',
            "  print(std(Ass[ai]));",
            '  print("FABER_AFFINE_MINASS_"+string(ai)+"_END");',
            "}",
            "if (expectedSolutions*radInExpected*expectedInRad*offCUnit*minassTwo==1) {",
            '  print("FABER_AFFINE_ENDPOINT=PASS_SQUARE_UNION_AFFINE_GRAPH");',
            "} else {",
            '  print("FABER_AFFINE_ENDPOINT=REPAIR_OR_EXTRA_COMPONENT"); quit;',
            "}",
            'print("FABER_AFFINE_PROBE_DONE=1");',
            'print("FABER_AFFINE_SCOPE=EXACT_SQUARE_ORDINARY_FABER_AFFINE_TARGET_ONLY_NO_REES_ACCESSIBILITY_CORRECTION_TERMINAL_TAYLOR_ORDER2_OR_JC2_VERDICT");',
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
    pell = load_pell_module()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    singular = output / f"faber_affine_mu2_{label}.sing"
    emit(singular, args.characteristic, tails, pell)
    payload = {
        "status": "PASS-FABER-AFFINE-MU2-COMPILER",
        "scope": "EXACT_SQUARE_ORDINARY_FABER_AFFINE_TARGET_ONLY",
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
