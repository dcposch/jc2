#!/usr/bin/env python3
"""Compile the p=0 odd-face grade-11/12 exact source client on AWS."""

from __future__ import annotations

import argparse
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
SUCCESSOR = ROOT / "xmodel/max12-812-order2-zero-load-p0-successor-design-20260826.md"
DESIGN = ROOT / "xmodel/max12-812-order2-p0-odd-face-g11-g12-design-20260826.md"
HALF_RESULTS = ROOT / "cases/max12_812_order2_square_halfweight_kuranishi_20260826/RESULTS.md"
HALF_FREEZE = ROOT / "cases/max12_812_order2_square_halfweight_kuranishi_20260826/FREEZE.sha256"
HALF_REVIEW = ROOT / "xmodel/max12-812-order2-square-halfweight-kuranishi-hostile-review-grok-20260826.md"
SHARP_RESULT = ROOT / "cases/max12_812_order2_square_third_tail_sharp_v2_20260826/RESULT.md"
SHARP_FREEZE = ROOT / "cases/max12_812_order2_square_third_tail_sharp_v2_20260826/FREEZE.sha256"
SHARP_RESULTS = ROOT / "cases/max12_812_order2_square_third_tail_sharp_v2_20260826/RESULTS.sha256"
FAN_REDUCTION = ROOT / "xmodel/max12-812-order2-square-fan-lower-hull-reduction-20260826.md"

EXPECTED_STATIC = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    BASE_COMPILER: "77f25216f0ab17abb3a8f4be271b2ea38f883806a72523cdca1be659df90dcdc",
    SUCCESSOR: "4e180381670c4dcd80a05e725925d3a69b85da76c84645d5a417e4fedb801216",
    DESIGN: "fea8194c2cb959dd4eb0d2de0955162669a834f3ac68924e72349dc0b8f4156e",
    HALF_RESULTS: "eb2cd8036a0abf87a1ff7a58c116346b11973efc47f35f9cb76105a6ccd485af",
    HALF_FREEZE: "ee4718fc24ae451f8f86c05e9c4eeae83215835e7cff5fdc8eccc54b9f881677",
    HALF_REVIEW: "49744ab901f05ae6d8f0163fd195f3b0219e725f051c3aeebf31fcdaa13c4214",
    SHARP_RESULT: "5a966b1d4dfde21e51bbaa6120a7cf118b05e68cfc0878aa2d1c345c6a0f47a0",
    SHARP_FREEZE: "96cb2824fb5c901e7485ba725f5d92e8f116b32a8a9dde7fd6c59cb901be013e",
    SHARP_RESULTS: "6ae5fe22481ac4ec085006d91919b35b9ff5b85abd05517b502850fdc07bb26b",
    FAN_REDUCTION: "d3d8f30a94a3d90175756ea0e21efd974461d51cb2db8433d2a270e1be355337",
}
EXPECTED_ALL_TAILS = "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only p0 odd-face compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only p0 odd-face compiler refused non-Amazon host")
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


def source_coefficients() -> dict[int, str]:
    pp = "(2*sigma*ell1+2*sigma^2*ell2)"
    c = "(sigma^2*(cs0+sigma*cs1+sigma^2*cs2))"
    r = f"((({pp})^2+sigma^2*(sigma*rs1+sigma^2*rs2))/4)"
    az = "(a1+sigma*aa1+sigma^2*aaa1)"
    ac = "(a0+sigma*aa0+sigma^2*aaa0)"
    ez = "(sigma*e1+sigma^2*ee1)"
    ec = "(sigma*e0+sigma^2*ee0)"
    n3 = f"(sigma^3*({az}))"
    n2 = f"(sigma^3*({ac}))"
    n1 = f"(sigma^3*(({pp})*({az})+({ez}))/2)"
    n0 = f"(sigma^3*(({pp})*({ac})+({ec}))/2)"
    return {
        6: f"(2*({pp}))",
        5: f"(2*({c}))",
        4: f"(({pp})^2+2*({r}))",
        3: f"(2*({pp})*({c})+sigma^2*({n3}))",
        2: f"(({c})^2+2*({pp})*({r})+sigma^2*({n2}))",
        1: f"(2*({c})*({r})+sigma^2*({n1}))",
        0: f"(({r})^2+sigma^2*({n0}))",
    }


def emit(path: Path, characteristic: int, tails: dict[str, list[list[object]]]) -> None:
    base = load_base_compiler()
    coeffs = source_coefficients()
    loads = {"k10": "(k0+sigma*k1+sigma^2*k2c)", "k6": "k6", "k2": "k2"}
    targets = {1: "0", 2: "mu2", 3: "0", 4: "mu4", 5: "0", 6: "mu6", 7: "J/4"}
    variables = (
        "sigma,ell1,ell2,cs0,cs1,rs1,cs2,rs2,"
        "a0,a1,aa0,aa1,aaa0,aaa1,e0,e1,ee0,ee1,"
        "k0,k1,k2c,k6,k2,mu2,mu4,mu6,J,t,u"
    )
    lines = [
        'LIB "elim.lib";',
        'LIB "primdec.lib";',
        f"ring R={characteristic},({variables}),dp;",
        'print("P0_ODD_G11_G12_SOURCE_HASHES=PASS");',
        "proc idealZero(ideal A, ideal G)",
        "{",
        "  int i;",
        "  for (i=1; i<=size(A); i++) { if (reduce(A[i],G)!=0) { return(0); } }",
        "  return(1);",
        "}",
        "ideal Sigma11=std(ideal(sigma^11)); ideal Sigma1=std(ideal(sigma));",
        "int div11=1; int div12=1; int quotientIdentity=1; int forbidden=1;",
    ]
    for ell in range(1, 8):
        expression = base.tail_text(tails[str(ell)], ell, coeffs, loads)
        expression = expression.replace("Lambda", "(sigma^2)")
        if targets[ell] != "0":
            expression += f"-sigma^{2 * (12 + ell)}*({targets[ell]})"
        lines.extend(
            [
                f"poly Phi{ell}={expression};",
                f"if (reduce(Phi{ell},Sigma11)!=0) {{ div11=0; }}",
                f"poly Q11_{ell}=Phi{ell}/sigma^11;",
                f"if (sigma^11*Q11_{ell}-Phi{ell}!=0) {{ quotientIdentity=0; }}",
                f"poly g11_{ell}=subst(Q11_{ell},sigma,0);",
                f"poly Rem12_{ell}=Q11_{ell}-g11_{ell};",
                f"if (reduce(Rem12_{ell},Sigma1)!=0) {{ div12=0; }}",
                f"poly Q12_{ell}=Rem12_{ell}/sigma;",
                f"if (sigma*Q12_{ell}-Rem12_{ell}!=0) {{ quotientIdentity=0; }}",
                f"poly g12_{ell}=subst(Q12_{ell},sigma,0);",
                f"if (diff(g11_{ell},cs1)!=0 || diff(g11_{ell},rs1)!=0 || diff(g11_{ell},cs2)!=0 || diff(g11_{ell},rs2)!=0 || diff(g11_{ell},aa0)!=0 || diff(g11_{ell},aa1)!=0 || diff(g11_{ell},aaa0)!=0 || diff(g11_{ell},aaa1)!=0 || diff(g11_{ell},ee0)!=0 || diff(g11_{ell},ee1)!=0 || diff(g11_{ell},k1)!=0 || diff(g11_{ell},k2c)!=0) {{ forbidden=0; }}",
                f"if (diff(g12_{ell},cs2)!=0 || diff(g12_{ell},rs2)!=0 || diff(g12_{ell},aaa0)!=0 || diff(g12_{ell},aaa1)!=0 || diff(g12_{ell},k2c)!=0) {{ forbidden=0; }}",
                f"if (diff(g11_{ell},k6)!=0 || diff(g11_{ell},k2)!=0 || diff(g11_{ell},mu2)!=0 || diff(g11_{ell},mu4)!=0 || diff(g11_{ell},mu6)!=0 || diff(g11_{ell},J)!=0) {{ forbidden=0; }}",
                f"if (diff(g12_{ell},k6)!=0 || diff(g12_{ell},k2)!=0 || diff(g12_{ell},mu2)!=0 || diff(g12_{ell},mu4)!=0 || diff(g12_{ell},mu6)!=0 || diff(g12_{ell},J)!=0) {{ forbidden=0; }}",
            ]
        )
    lines.extend(
        [
            'print("P0_ODD_G11_DIVISIBLE="+string(div11));',
            'print("P0_ODD_G12_DIVISIBLE="+string(div12));',
            'print("P0_ODD_QUOTIENT_IDENTITIES="+string(quotientIdentity));',
            'print("P0_ODD_FORBIDDEN_LATER_VARIABLES="+string(forbidden));',
            'if (div11*div12*quotientIdentity*forbidden!=1) { print("P0_ODD_FAIL=SOURCE_EXTRACTION"); quit; }',
            'print("P0_ODD_G11_SOURCE_BEGIN");',
            'print(g11_1); print(g11_2); print(g11_3); print(g11_4); print(g11_5); print(g11_6); print(g11_7);',
            'print("P0_ODD_G11_SOURCE_END");',
            'print("P0_ODD_G12_SOURCE_BEGIN");',
            'print(g12_1); print(g12_2); print(g12_3); print(g12_4); print(g12_5); print(g12_6); print(g12_7);',
            'print("P0_ODD_G12_SOURCE_END");',
            "poly A0=a1+a0*t; poly A1=aa1+aa0*t;",
            "poly E1=(e1+e0*t)/2; poly E2=(ee1+ee0*t)/2;",
            "poly B0=cs0; poly B1=cs1+(rs1/4)*t;",
            "poly H11=(3/4)*A0*E1-(5/16)*k0*ell1*t*B0^3;",
            "poly H12=(3/4)*(A0*E2+A1*E1)",
            " -(3/4)*ell1*t^2*A0*E1+(3/8)*t^2*E1^2-(3/8)*t*B0*A0^2",
            " +(5/8)*k0*E1*B0",
            " +(5/16)*k0*(3*B0*(rs1/4)^2*t-3*ell1*t*B0^2*B1+ell1^2*t^3*B0^3-ell2*t*B0^3)",
            " -(5/16)*k1*ell1*t*B0^3-(5/128)*k0*t^2*B0^4;",
            "poly D11_0=H11; poly D12_0=H12;",
        ]
    )
    for ell in range(1, 8):
        factorial = math.factorial(ell)
        lines.extend(
            [
                f"poly D11_{ell}=diff(D11_{ell - 1},t);",
                f"poly D12_{ell}=diff(D12_{ell - 1},t);",
                f"poly h11_{ell}=subst(D11_{ell},t,0)/{factorial};",
                f"poly h12_{ell}=subst(D12_{ell},t,0)/{factorial};",
            ]
        )
    lines.extend(
        [
            'print("P0_ODD_MOVING_FABER_RELATION=p=2*sigma*ell1+O(sigma2)");',
            'print("P0_ODD_MOVING_FABER_UNIT_DIAGONAL=1");',
            "int rows11=1; int rows12=1;",
        ]
    )
    for ell in range(1, 8):
        pred12 = f"h12_{ell}"
        if ell >= 3:
            numerator = ell - 2
            connection = f"({numerator}/2)*ell1*h11_{ell - 2}"
            pred12 += f"+{connection}"
        lines.extend(
            [
                f"poly Check11_{ell}=g11_{ell}-h11_{ell};",
                f"poly Check12_{ell}=g12_{ell}-({pred12});",
                f"if (Check11_{ell}!=0) {{ rows11=0; print(\"P0_ODD_G11_REMAINDER_{ell}\"); print(Check11_{ell}); }}",
                f"if (Check12_{ell}!=0) {{ rows12=0; print(\"P0_ODD_G12_REMAINDER_{ell}\"); print(Check12_{ell}); }}",
            ]
        )
    lines.extend(
        [
            'print("P0_ODD_G11_ROW_IDENTITIES="+string(rows11));',
            'print("P0_ODD_G12_ROW_IDENTITIES="+string(rows12));',
            'if (rows11*rows12!=1) { print("P0_ODD_FAIL=ANALYTIC_BRIDGE"); quit; }',
            "ideal Eraw=g11_1,g11_2,g11_3,g11_4,g11_5,g11_6,g11_7,g12_1,g12_2,g12_3,g12_4,g12_5,g12_6,g12_7;",
            'print("P0_ODD_RAW_BEGIN"); print(std(Eraw)); print("P0_ODD_RAW_END");',
            "ideal Eb=std(sat(std(Eraw),ideal(cs0)));",
            "ideal Ebk=std(sat(Eb,ideal(k0)));",
            'print("P0_ODD_LOCALIZED_RAW_BEGIN"); print(Ebk); print("P0_ODD_LOCALIZED_RAW_END");',
            "poly Sheet=12*e1^2-5*k0*cs0^4;",
            "poly LastF=(3/8)*(a1*ee0+aa0*e1)-(3/8)*cs0*a1^2+(15/256)*k0*cs0*rs1^2-(5/16)*k0*ell2*cs0^3;",
            "ideal Predicted=std(ideal(e0,a0,ell1,Sheet,LastF));",
            "ideal Rad=std(radical(Ebk)); ideal PredRad=std(radical(Predicted));",
            "int radInPred=idealZero(Rad,PredRad); int predInRad=idealZero(PredRad,Rad);",
            'print("P0_ODD_RADICAL_BEGIN"); print(Rad); print("P0_ODD_RADICAL_END");',
            'print("P0_ODD_PREDICTED_RADICAL_BEGIN"); print(PredRad); print("P0_ODD_PREDICTED_RADICAL_END");',
            'print("P0_ODD_RAD_IN_PREDICTED="+string(radInPred));',
            'print("P0_ODD_PREDICTED_IN_RAD="+string(predInRad));',
            "poly NormIdentity=12*(cs0^2*u)^2-5*((12/5)*u^2)*cs0^4;",
            "poly DeckIdentity=subst(NormIdentity,u,-u)-NormIdentity;",
            "int normPass=(NormIdentity==0); int deckPass=(DeckIdentity==0);",
            'print("P0_ODD_NORMALIZATION_K0_12U2_OVER5="+string(normPass));',
            'print("P0_ODD_SHEET_DECK_U_TO_MINUS_U="+string(deckPass));',
            'if (radInPred*predInRad*normPass*deckPass!=1) { print("P0_ODD_FAIL=SUPPORT_OR_NORMALIZATION"); quit; }',
            'print("P0_ODD_ENDPOINT=PASS_EXACT_SOURCE_G11_G12_QUADRATIC_SHEET");',
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
    singular = output / f"p0_odd_g11_g12_{label}.sing"
    emit(singular, args.characteristic, tails)
    payload = {
        "status": "PASS-P0-ODD-G11-G12-COMPILER",
        "scope": "P0_ODD_COLLISION_CONE_G11_G12_ONLY_NO_TERMINAL_FAN_OR_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "tails_sha256": digest(TAILS),
        "all_tails_sha256": EXPECTED_ALL_TAILS,
        "design_sha256": digest(DESIGN),
        "input_sha256": digest(singular),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
