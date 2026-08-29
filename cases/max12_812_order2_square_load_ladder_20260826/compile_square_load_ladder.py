#!/usr/bin/env python3
"""Compile the generic-square fourth/fifth-grade source receiver on AWS."""

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
DESIGN = ROOT / "xmodel/max12-812-order2-generic-square-load-ladder-design-20260826.md"
ONEPARAM = ROOT / "xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-20260826.md"
FIRST_NORMAL = ROOT / "xmodel/max12-812-order2-first-normal-divisibility-jet-theorem-20260826.md"
PADE = ROOT / "xmodel/max12-812-order2-first-normal-pade-support-theorem-20260826.md"
PADE_REVIEW = ROOT / "xmodel/max12-812-order2-first-normal-pade-support-review-grok-20260826.md"
NEXT_DESIGN = ROOT / "xmodel/max12-812-order2-square-discriminant-next-jet-design-20260826.md"
CROSS = ROOT / "xmodel/cross-pollination-order2-square-normalized-rees-20260826T0640Z.md"

EXPECTED_STATIC = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    DESIGN: "5bfe5ae46d4609662c7b4a65d953acc15da1dffe5dc27a31141a462529aaf615",
    ONEPARAM: "5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b",
    FIRST_NORMAL: "827e76bde5d394ab17f7c05561a1bf254b6fdf8fc3453dd60400d16e80061fdc",
    PADE: "2c917b9fe9af3c23d615a3f9061a5c981d26e5e69a75138aacb33f308619ecf5",
    PADE_REVIEW: "73c30502e0466bcc6757605e5be736dabf14d2f3bfaacd302d88b94cd12dc8e6",
    NEXT_DESIGN: "8d44393d23e5af2a59cd90713cba71daf1d07185be5a4ca905c1b56559af1c9e",
    CROSS: "c2d02e22c37ffbd99f2ea55c435e6d88b6fc3d15b5c8e119f83d8539f483c605",
}
EXPECTED_ALL_TAILS = "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"
NAMES = [f"a{i}" for i in range(7)] + ["k10", "k6", "k2"]
WEIGHTS = [8 - i for i in range(7)] + [2, 6, 10]
LOAD_WEIGHTS = [2, 6, 10]


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only square ladder compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only square ladder compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def rational_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"({value.numerator}/{value.denominator})"


def source_data() -> tuple[dict[int, str], dict[str, str]]:
    # K=z^4+p*z^2+Lambda*cs*z+(p^2+Lambda*rs)/4 and
    # N=Lambda*(v1*z+v0)/2 in f=K^2+Lambda*N.
    p = "p"
    c = "(Lambda*cs)"
    r = "((p^2+Lambda*rs)/4)"
    n3 = "0"
    n2 = "0"
    n1 = "(Lambda*v1/2)"
    n0 = "(Lambda*v0/2)"
    coeffs = {
        6: f"(2*({p}))",
        5: f"(2*({c}))",
        4: f"(({p})^2+2*({r}))",
        3: f"(2*({p})*({c})+Lambda*({n3}))",
        2: f"(({c})^2+2*({p})*({r})+Lambda*({n2}))",
        1: f"(2*({c})*({r})+Lambda*({n1}))",
        0: f"(({r})^2+Lambda*({n0}))",
    }
    return coeffs, {"k10": "k10", "k6": "k6", "k2": "k2"}


def term_text(
    monomial: list[int],
    coefficient: Fraction,
    coeffs: dict[int, str],
    loads: dict[str, str],
) -> str:
    factors: list[str] = []
    for i, exponent in enumerate(monomial[:7]):
        if exponent == 1:
            factors.append(coeffs[i])
        elif exponent:
            factors.append(f"({coeffs[i]})^{exponent}")
    lambda_power = 0
    for offset, exponent in enumerate(monomial[7:]):
        if exponent:
            name = NAMES[7 + offset]
            factors.append(loads[name] if exponent == 1 else f"({loads[name]})^{exponent}")
            lambda_power += LOAD_WEIGHTS[offset] * exponent
    if lambda_power:
        factors.append(f"Lambda^{lambda_power}")
    body = "*".join(factors) or "1"
    if coefficient == 1 and factors:
        return body
    if coefficient == -1 and factors:
        return "-" + body
    return f"{rational_text(coefficient)}*{body}" if factors else rational_text(coefficient)


def tail_text(
    entries: list[list[object]],
    ell: int,
    coeffs: dict[int, str],
    loads: dict[str, str],
) -> str:
    terms: list[str] = []
    for raw_monomial, raw_coefficient in entries:
        monomial = [int(value) for value in raw_monomial]
        if len(monomial) != len(NAMES):
            fail(("monomial length", ell, monomial))
        if sum(monomial[7:]) > 1 or any(value not in (0, 1) for value in monomial[7:]):
            fail(("tail load nonlinearity", ell, monomial))
        if sum(a * b for a, b in zip(monomial, WEIGHTS)) != 12 + ell:
            fail(("tail weight", ell, monomial))
        terms.append(term_text(monomial, Fraction(str(raw_coefficient)), coeffs, loads))
    return "+".join(terms).replace("+-", "-") if terms else "0"


def emit(path: Path, characteristic: int, tails: dict[str, list[list[object]]]) -> None:
    coeffs, loads = source_data()
    targets = {1: "0", 2: "mu2", 3: "0", 4: "mu4", 5: "0", 6: "mu6", 7: "J/4"}
    lines = [
        'LIB "elim.lib";',
        'LIB "primdec.lib";',
        f"ring Rfull={characteristic},(Lambda,p,cs,rs,v0,v1,k10,k6,k2,mu2,mu4,mu6,J),dp;",
        "proc idealZero(ideal A, ideal G)",
        "{",
        "  int i;",
        "  for (i=1; i<=size(A); i++) { if (reduce(A[i],G)!=0) { return(0); } }",
        "  return(1);",
        "}",
        'print("SQUARE_LADDER_SOURCE_HASHES=PASS");',
        "ideal Lambda4=std(ideal(Lambda^4));",
        "ideal Lambda5=std(ideal(Lambda^5));",
        "int divisible4=1; int identity4=1; int forbidden4=1;",
        "int divisible5=1; int identity5=1; int forbidden5=1;",
    ]
    for ell in range(1, 8):
        expression = tail_text(tails[str(ell)], ell, coeffs, loads)
        if targets[ell] != "0":
            expression += f"-Lambda^{12 + ell}*({targets[ell]})"
        lines.extend(
            [
                f"poly Phi{ell}={expression};",
                f"if (reduce(Phi{ell},Lambda4)!=0) {{ divisible4=0; }}",
                f"poly Xi4_{ell}=Phi{ell}/Lambda^4;",
                f"if (Lambda^4*Xi4_{ell}-Phi{ell}!=0) {{ identity4=0; }}",
                f"poly e4_{ell}=subst(Xi4_{ell},Lambda,0);",
                f"if (diff(e4_{ell},k10)!=0 || diff(e4_{ell},k6)!=0 || diff(e4_{ell},k2)!=0 || diff(e4_{ell},mu2)!=0 || diff(e4_{ell},mu4)!=0 || diff(e4_{ell},mu6)!=0 || diff(e4_{ell},J)!=0) {{ forbidden4=0; }}",
                f"poly Phi5_{ell}=subst(subst(Phi{ell},v0,0),v1,0);",
                f"if (reduce(Phi5_{ell},Lambda5)!=0) {{ divisible5=0; }}",
                f"poly Xi5_{ell}=Phi5_{ell}/Lambda^5;",
                f"if (Lambda^5*Xi5_{ell}-Phi5_{ell}!=0) {{ identity5=0; }}",
                f"poly e5_{ell}=subst(Xi5_{ell},Lambda,0);",
                f"if (diff(e5_{ell},k6)!=0 || diff(e5_{ell},k2)!=0 || diff(e5_{ell},mu2)!=0 || diff(e5_{ell},mu4)!=0 || diff(e5_{ell},mu6)!=0 || diff(e5_{ell},J)!=0) {{ forbidden5=0; }}",
            ]
        )
    lines.extend(
        [
            'print("SQUARE_LADDER_GRADE4_DIVISIBLE="+string(divisible4));',
            'print("SQUARE_LADDER_GRADE4_IDENTITY="+string(identity4));',
            'print("SQUARE_LADDER_GRADE4_FORBIDDEN="+string(forbidden4));',
            'print("SQUARE_LADDER_GRADE5_DIVISIBLE="+string(divisible5));',
            'print("SQUARE_LADDER_GRADE5_IDENTITY="+string(identity5));',
            'print("SQUARE_LADDER_GRADE5_FORBIDDEN="+string(forbidden5));',
            'if (divisible4*identity4*forbidden4*divisible5*identity5*forbidden5!=1) { print("SQUARE_LADDER_FAIL=SOURCE_GATE"); quit(81); }',
            'print("SQUARE_LADDER_GRADE4_ROWS_BEGIN");',
            "print(e4_1); print(e4_2); print(e4_3); print(e4_4); print(e4_5); print(e4_6); print(e4_7);",
            'print("SQUARE_LADDER_GRADE4_ROWS_END");',
            'print("SQUARE_LADDER_GRADE5_ROWS_BEGIN");',
            "print(e5_1); print(e5_2); print(e5_3); print(e5_4); print(e5_5); print(e5_6); print(e5_7);",
            'print("SQUARE_LADDER_GRADE5_ROWS_END");',
            "ideal E4full=e4_1,e4_2,e4_3,e4_4,e4_5,e4_6,e4_7;",
            "ideal E5full=e5_1,e5_2,e5_3,e5_4,e5_5,e5_6,e5_7;",
            f"ring R4={characteristic},(p,cs,rs,v0,v1,k10),dp;",
            "ideal E4=std(imap(Rfull,E4full));",
            "ideal E4p=std(sat(E4,ideal(p)));",
            "ideal E4pk=std(sat(E4p,ideal(k10)));",
            "ideal Rad4=std(radical(E4pk));",
            "ideal Expected4=std(ideal(v0,v1));",
            "int rad4_in_expected=idealZero(Rad4,Expected4);",
            "int expected4_in_rad=idealZero(Expected4,Rad4);",
            'print("SQUARE_LADDER_GRADE4_RAW_BEGIN"); print(E4pk); print("SQUARE_LADDER_GRADE4_RAW_END");',
            'print("SQUARE_LADDER_GRADE4_RADICAL_BEGIN"); print(Rad4); print("SQUARE_LADDER_GRADE4_RADICAL_END");',
            'print("SQUARE_LADDER_GRADE4_RAD_IN_EXPECTED="+string(rad4_in_expected));',
            'print("SQUARE_LADDER_GRADE4_EXPECTED_IN_RAD="+string(expected4_in_rad));',
            "setring Rfull;",
            f"ring R5={characteristic},(p,cs,rs,k10),dp;",
            "ideal E5=std(imap(Rfull,E5full));",
            "ideal E5p=std(sat(E5,ideal(p)));",
            "ideal E5pk=std(sat(E5p,ideal(k10)));",
            "ideal Rad5=std(radical(E5pk));",
            "ideal Expected5=std(ideal(cs,rs));",
            "int rad5_in_expected=idealZero(Rad5,Expected5);",
            "int expected5_in_rad=idealZero(Expected5,Rad5);",
            'print("SQUARE_LADDER_GRADE5_RAW_BEGIN"); print(E5pk); print("SQUARE_LADDER_GRADE5_RAW_END");',
            'print("SQUARE_LADDER_GRADE5_RADICAL_BEGIN"); print(Rad5); print("SQUARE_LADDER_GRADE5_RADICAL_END");',
            'print("SQUARE_LADDER_GRADE5_RAD_IN_EXPECTED="+string(rad5_in_expected));',
            'print("SQUARE_LADDER_GRADE5_EXPECTED_IN_RAD="+string(expected5_in_rad));',
            'if (rad4_in_expected*expected4_in_rad*rad5_in_expected*expected5_in_rad!=1) { print("SQUARE_LADDER_FAIL=RADICAL_MISMATCH"); quit(82); }',
            'print("SQUARE_LADDER_ENDPOINT=PASS_SOURCE_GRADES4_5_AND_RADICALS");',
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
    for source, expected in EXPECTED_STATIC.items():
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
    singular = output / f"square_load_ladder_{label}.sing"
    emit(singular, args.characteristic, tails)
    result = {
        "status": "PASS-SQUARE-LOAD-LADDER-COMPILER",
        "scope": "GENERIC_SQUARE_GRADES4_5_ONLY_NO_BRANCH_OR_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "tails_sha256": digest(TAILS),
        "all_tails_sha256": EXPECTED_ALL_TAILS,
        "design_sha256": digest(DESIGN),
        "input_sha256": digest(singular),
    }
    (output / "result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
