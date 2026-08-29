#!/usr/bin/env python3
"""Compile the exact sharpened square third-tail certificate on AWS."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
import math
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TAILS = ROOT / "cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json"
BASE_COMPILER = ROOT / "cases/max12_812_order2_square_load_ladder_20260826/compile_square_load_ladder.py"
THIRD_TAIL = ROOT / "xmodel/max12-812-order2-square-third-tail-divisibility-theorem-20260826.md"
SUCCESSOR = ROOT / "xmodel/max12-812-order2-zero-load-p0-successor-design-20260826.md"
EXPECTED_STATIC = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    BASE_COMPILER: "77f25216f0ab17abb3a8f4be271b2ea38f883806a72523cdca1be659df90dcdc",
    THIRD_TAIL: "045b1bdc6c1429451afa34dd2d7d12da4c72d9af716e52228a869f61d0f4a4bb",
    SUCCESSOR: "4e180381670c4dcd80a05e725925d3a69b85da76c84645d5a417e4fedb801216",
}
EXPECTED_ALL_TAILS = "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only sharp-third-tail compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only sharp-third-tail compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_base_compiler():
    spec = importlib.util.spec_from_file_location("square_ladder_base", BASE_COMPILER)
    if spec is None or spec.loader is None:
        fail("cannot load charged base compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def qtext(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"({value.numerator}/{value.denominator})"


def transform_entry(ell: int, j: int) -> str:
    """Coefficient of w^-ell in z^-j for w^2=z^2+p/2."""

    delta = ell - j
    if delta < 0 or delta % 2:
        return "0"
    n = delta // 2
    coefficient = Fraction(1)
    for offset in range(n):
        coefficient *= Fraction(j, 2) + offset
    coefficient /= math.factorial(n)
    coefficient /= 2**n
    if n == 0:
        return qtext(coefficient)
    ppart = "pbase" if n == 1 else f"pbase^{n}"
    if coefficient == 1:
        return ppart
    if coefficient == -1:
        return "-" + ppart
    return f"{qtext(coefficient)}*{ppart}"


def source_coefficients(config: str) -> tuple[dict[int, str], str]:
    if config == "generic":
        pp = "p"
        pbase = "p"
    elif config == "p0moving":
        pp = "(Lambda*pt)"
        pbase = "0"
    else:
        fail(("unknown configuration", config))
    c = "(Lambda*cs)"
    r = f"((({pp})^2+Lambda*rs)/4)"
    n3 = "m1"
    n2 = "m0"
    n1 = f"((({pp})*m1+Lambda*v1)/2)"
    n0 = f"((({pp})*m0+Lambda*v0)/2)"
    coeffs = {
        6: f"(2*({pp}))",
        5: f"(2*({c}))",
        4: f"(({pp})^2+2*({r}))",
        3: f"(2*({pp})*({c})+Lambda*({n3}))",
        2: f"(({c})^2+2*({pp})*({r})+Lambda*({n2}))",
        1: f"(2*({c})*({r})+Lambda*({n1}))",
        0: f"(({r})^2+Lambda*({n0}))",
    }
    return coeffs, pbase


def emit(path: Path, config: str, characteristic: int, tails: dict[str, list[list[object]]]) -> None:
    base = load_base_compiler()
    coeffs, pbase = source_coefficients(config)
    loads = {"k10": "(Lambda*kappa)", "k6": "k6", "k2": "k2"}
    targets = {1: "0", 2: "mu2", 3: "0", 4: "mu4", 5: "0", 6: "mu6", 7: "J/4"}
    variables = (
        "Lambda,p,pt,m1,m0,cs,rs,v1,v0,kappa,k6,k2,"
        "mu2,mu4,mu6,J,t,z"
    )
    lines = [
        f"ring R={characteristic},({variables}),dp;",
        'print("SQUARE_THIRD_SHARP_SOURCE_HASHES=PASS");',
        f'print("SQUARE_THIRD_SHARP_CONFIG={config}");',
        "ideal Lambda3=std(ideal(Lambda^3));",
        "int div3=1; int quotient_identity=1; int forbidden=1;",
    ]
    for ell in range(1, 8):
        expression = base.tail_text(tails[str(ell)], ell, coeffs, loads)
        if targets[ell] != "0":
            expression += f"-Lambda^{12 + ell}*({targets[ell]})"
        lines.extend(
            [
                f"poly Phi{ell}={expression};",
                f"if (reduce(Phi{ell},Lambda3)!=0) {{ div3=0; }}",
                f"poly Q3_{ell}=Phi{ell}/Lambda^3;",
                f"if (Lambda^3*Q3_{ell}-Phi{ell}!=0) {{ quotient_identity=0; }}",
                f"poly g{ell}=subst(Q3_{ell},Lambda,0);",
                f"if (diff(g{ell},kappa)!=0 || diff(g{ell},k6)!=0 || diff(g{ell},k2)!=0 || diff(g{ell},mu2)!=0 || diff(g{ell},mu4)!=0 || diff(g{ell},mu6)!=0 || diff(g{ell},J)!=0) {{ forbidden=0; }}",
            ]
        )
        if config == "p0moving":
            lines.append(f"if (diff(g{ell},pt)!=0) {{ forbidden=0; }}")
    lines.extend(
        [
            'print("SQUARE_THIRD_SHARP_LAMBDA3_DIVISIBLE="+string(div3));',
            'print("SQUARE_THIRD_SHARP_QUOTIENT_IDENTITIES="+string(quotient_identity));',
            'print("SQUARE_THIRD_SHARP_POLYNOMIAL_MOTIONS_ABSENT="+string(forbidden));',
            'if (div3*quotient_identity*forbidden!=1) { print("SQUARE_THIRD_SHARP_FAIL=SOURCE_EXTRACTION"); quit; }',
            f"poly pbase={pbase};",
            "poly L=z^2+pbase/2;",
            "poly M=m1*z+m0;",
            "poly RR=cs*z+rs/4;",
            "poly SS=(v1*z+v0)/2;",
            "poly TT=2*L*RR+M;",
            "poly BB=RR^2+SS;",
            "poly PP=12*TT*BB*L^2-TT^3;",
            "poly Prev=0;",
        ]
    )
    for degree in range(10):
        lines.append(f"Prev=Prev+coeff(PP,z,{degree})*t^{9-degree};")
    lines.extend(
        [
            "poly ss=pbase/2;",
            "poly Inv3=1-3*ss*t^2+6*ss^2*t^4-10*ss^3*t^6+15*ss^4*t^8-21*ss^5*t^10+28*ss^6*t^12;",
            "poly H=Prev*Inv3/16;",
        ]
    )
    for ell in range(1, 8):
        lines.append(f"poly h{ell}=coeff(H,t,{ell + 3});")
    lines.extend(
        [
            'print("SQUARE_THIRD_SHARP_ROW_TRANSFORM_RELATION=q^2+(pbase/2)*v^2-1");',
            'print("SQUARE_THIRD_SHARP_ROW_TRANSFORM_UNIT_DIAGONAL=1");',
            "int rows=1;",
        ]
    )
    for ell in range(1, 8):
        summands: list[str] = []
        for j in range(1, ell + 1):
            coefficient = transform_entry(ell, j)
            if coefficient != "0":
                summands.append(f"({coefficient})*h{j}")
        predicted = "+".join(summands).replace("+-", "-") or "0"
        lines.extend(
            [
                f"poly RowCheck{ell}=g{ell}-({predicted});",
                f"if (RowCheck{ell}!=0) {{ rows=0; print(\"SQUARE_THIRD_SHARP_ROW_REMAINDER_{ell}\"); print(RowCheck{ell}); }}",
            ]
        )
    lines.extend(
        [
            'print("SQUARE_THIRD_SHARP_ROW_IDENTITIES="+string(rows));',
            "ideal GL=std(ideal(L));",
            "poly ModL=reduce(PP+M^3,GL);",
            "int modLIdentity=(ModL==0);",
            'print("SQUARE_THIRD_SHARP_P_MOD_L_MINUS_M3="+string(modLIdentity));',
        ]
    )
    if config == "p0moving":
        lines.extend(
            [
                "poly ConstCheck=coeff(PP,z,0)+m0^3;",
                "poly PPbeta0=subst(PP,m0,0);",
                "poly CubicCheck=coeff(PPbeta0,z,3)+m1^3;",
                "int p0const=(ConstCheck==0); int p0cubic=(CubicCheck==0);",
                'print("SQUARE_THIRD_SHARP_P0_CONSTANT_MINUS_BETA3="+string(p0const));',
                'print("SQUARE_THIRD_SHARP_P0_Z3_MINUS_ALPHA3="+string(p0cubic));',
                'if (p0const*p0cubic!=1) { print("SQUARE_THIRD_SHARP_FAIL=P0_SENTINEL"); quit; }',
            ]
        )
    lines.extend(
        [
            'if (rows*modLIdentity!=1) { print("SQUARE_THIRD_SHARP_FAIL=ANALYTIC_BRIDGE"); quit; }',
            'print("SQUARE_THIRD_SHARP_RAW_R_S_RETAINED=1");',
            'print("SQUARE_THIRD_SHARP_ENDPOINT=PASS_COMPLETE_SOURCE_THIRD_TAIL");',
            "quit;",
        ]
    )
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--config", choices=("generic", "p0moving"), required=True)
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
    singular = output / f"square_third_sharp_{args.config}_{label}.sing"
    emit(singular, args.config, args.characteristic, tails)
    payload = {
        "status": "PASS-SQUARE-THIRD-SHARP-COMPILER",
        "registered_aws_lane": tag,
        "config": args.config,
        "characteristic": args.characteristic,
        "tails_sha256": digest(TAILS),
        "all_tails_sha256": EXPECTED_ALL_TAILS,
        "successor_design_sha256": digest(SUCCESSOR),
        "input_sha256": digest(singular),
        "scope": "COMPLETE_SOURCE_THIRD_TAIL_IDENTITY_ONLY_NO_SQUARE_OR_ORDER2_VERDICT",
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
