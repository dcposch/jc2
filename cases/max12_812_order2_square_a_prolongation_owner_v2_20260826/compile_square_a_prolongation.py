#!/usr/bin/env python3
"""Compile the generic-square high-contact A-prolongation certificate.

This compiler is AWS-only.  It reconstructs all seven frozen loaded source
rows, extracts the exact sigma grades 14 and 15, and checks them against the
Laurent receivers through the square-base unitriangular row transform.
"""

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
DESIGN = ROOT / "xmodel/max12-812-order2-square-a-prolongation-design-20260826.md"
HALF_DESIGN = ROOT / "xmodel/max12-812-order2-generic-square-halfweight-kuranishi-design-20260826.md"
HALF_RESULTS = ROOT / "cases/max12_812_order2_square_halfweight_kuranishi_20260826/RESULTS.md"
HALF_REVIEW = ROOT / "xmodel/max12-812-order2-square-halfweight-kuranishi-hostile-review-grok-20260826.md"
THIRD_TAIL = ROOT / "xmodel/max12-812-order2-square-third-tail-divisibility-theorem-20260826.md"

EXPECTED_STATIC = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    BASE_COMPILER: "77f25216f0ab17abb3a8f4be271b2ea38f883806a72523cdca1be659df90dcdc",
    DESIGN: "36b8abd0383d901261a4b410c94a0ffb759e3dea37263852af86778e77d5589d",
    HALF_DESIGN: "37a7234cee998a0069f33b7a36bb945123b305acd01485a771d8e6ed7dac65fd",
    HALF_RESULTS: "eb2cd8036a0abf87a1ff7a58c116346b11973efc47f35f9cb76105a6ccd485af",
    HALF_REVIEW: "49744ab901f05ae6d8f0163fd195f3b0219e725f051c3aeebf31fcdaa13c4214",
    THIRD_TAIL: "045b1bdc6c1429451afa34dd2d7d12da4c72d9af716e52228a869f61d0f4a4bb",
}
EXPECTED_ALL_TAILS = "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only square A-prolongation compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only square A-prolongation compiler refused non-Amazon host")
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
    for r in range(n):
        coefficient *= Fraction(j, 2) + r
    coefficient /= math.factorial(n)
    coefficient /= 2**n  # (p/2)^n
    if n == 0:
        return qtext(coefficient)
    ppart = "p" if n == 1 else f"p^{n}"
    if coefficient == 1:
        return ppart
    if coefficient == -1:
        return "-" + ppart
    return f"{qtext(coefficient)}*{ppart}"


def source_coefficients() -> dict[int, str]:
    p = "p"
    c = "(sigma^4*bs0+sigma^5*bs1)"
    r = "((p^2+sigma^4*br0+sigma^5*br1)/4)"
    n3 = "(sigma^3*(a1+sigma*aa1))"
    n2 = "(sigma^3*(a0+sigma*aa0))"
    n1 = "(sigma^3*(p*(a1+sigma*aa1)+sigma^4*(e1+sigma*ee1))/2)"
    n0 = "(sigma^3*(p*(a0+sigma*aa0)+sigma^4*(e0+sigma*ee0))/2)"
    return {
        6: f"(2*({p}))",
        5: f"(2*({c}))",
        4: f"(({p})^2+2*({r}))",
        3: f"(2*({p})*({c})+sigma^2*({n3}))",
        2: f"(({c})^2+2*({p})*({r})+sigma^2*({n2}))",
        1: f"(2*({c})*({r})+sigma^2*({n1}))",
        0: f"(({r})^2+sigma^2*({n0}))",
    }


def emit(path: Path, characteristic: int, tails: dict[str, list[list[object]]]) -> None:
    base = load_base_compiler()
    coeffs = source_coefficients()
    loads = {"k10": "(k0+sigma*k1)", "k6": "k6", "k2": "k2"}
    targets = {1: "0", 2: "mu2", 3: "0", 4: "mu4", 5: "0", 6: "mu6", 7: "J/4"}
    variables = (
        "sigma,p,bs0,br0,bs1,br1,a0,a1,aa0,aa1,"
        "e0,e1,ee0,ee1,k0,k1,k6,k2,mu2,mu4,mu6,J,t,z"
    )
    lines = [
        f"ring R={characteristic},({variables}),dp;",
        'print("SQUARE_APROLONG_SOURCE_HASHES=PASS");',
        "ideal Sigma14=std(ideal(sigma^14));",
        "ideal Sigma1=std(ideal(sigma));",
        "int div14=1; int div15=1; int quotient_identity=1; int forbidden=1;",
    ]
    for ell in range(1, 8):
        expression = base.tail_text(tails[str(ell)], ell, coeffs, loads)
        expression = expression.replace("Lambda", "(sigma^2)")
        if targets[ell] != "0":
            expression += f"-sigma^{2 * (12 + ell)}*({targets[ell]})"
        lines.extend(
            [
                f"poly Phi{ell}={expression};",
                f"if (reduce(Phi{ell},Sigma14)!=0) {{ div14=0; }}",
                f"poly Q14_{ell}=Phi{ell}/sigma^14;",
                f"if (sigma^14*Q14_{ell}-Phi{ell}!=0) {{ quotient_identity=0; }}",
                f"poly g14_{ell}=subst(Q14_{ell},sigma,0);",
                f"poly R15_{ell}=Q14_{ell}-g14_{ell};",
                f"if (reduce(R15_{ell},Sigma1)!=0) {{ div15=0; }}",
                f"poly Q15_{ell}=R15_{ell}/sigma;",
                f"if (sigma*Q15_{ell}-R15_{ell}!=0) {{ quotient_identity=0; }}",
                f"poly g15_{ell}=subst(Q15_{ell},sigma,0);",
                f"if (diff(g14_{ell},bs1)!=0 || diff(g14_{ell},br1)!=0 || diff(g14_{ell},aa0)!=0 || diff(g14_{ell},aa1)!=0 || diff(g14_{ell},ee0)!=0 || diff(g14_{ell},ee1)!=0 || diff(g14_{ell},k1)!=0) {{ forbidden=0; }}",
                f"if (diff(g14_{ell},k6)!=0 || diff(g14_{ell},k2)!=0 || diff(g14_{ell},mu2)!=0 || diff(g14_{ell},mu4)!=0 || diff(g14_{ell},mu6)!=0 || diff(g14_{ell},J)!=0) {{ forbidden=0; }}",
                f"if (diff(g15_{ell},k6)!=0 || diff(g15_{ell},k2)!=0 || diff(g15_{ell},mu2)!=0 || diff(g15_{ell},mu4)!=0 || diff(g15_{ell},mu6)!=0 || diff(g15_{ell},J)!=0) {{ forbidden=0; }}",
            ]
        )
    lines.extend(
        [
            'print("SQUARE_APROLONG_SIGMA14_DIVISIBLE="+string(div14));',
            'print("SQUARE_APROLONG_SIGMA15_DIVISIBLE="+string(div15));',
            'print("SQUARE_APROLONG_QUOTIENT_IDENTITIES="+string(quotient_identity));',
            'print("SQUARE_APROLONG_FORBIDDEN="+string(forbidden));',
            'if (div14*div15*quotient_identity*forbidden!=1) { print("SQUARE_APROLONG_FAIL=SOURCE_EXTRACTION"); quit; }',
            'print("SQUARE_APROLONG_G14_BEGIN");',
            "print(g14_1); print(g14_2); print(g14_3); print(g14_4); print(g14_5); print(g14_6); print(g14_7);",
            'print("SQUARE_APROLONG_G14_END");',
            'print("SQUARE_APROLONG_G15_BEGIN");',
            "print(g15_1); print(g15_2); print(g15_3); print(g15_4); print(g15_5); print(g15_6); print(g15_7);",
            'print("SQUARE_APROLONG_G15_END");',
            "poly ss=p/2;",
            "poly A0=a1+a0*t; poly A1=aa1+aa0*t;",
            "poly B0=bs0+(br0/4)*t; poly B1=bs1+(br1/4)*t;",
            "poly E0=(e1+e0*t)/2; poly E1=(ee1+ee0*t)/2;",
            "poly Inv1=1-ss*t^2+ss^2*t^4-ss^3*t^6;",
            "poly Inv2=1-2*ss*t^2+3*ss^2*t^4-4*ss^3*t^6;",
            "poly Inv3=1-3*ss*t^2+6*ss^2*t^4-10*ss^3*t^6;",
            "poly H14=(3/4)*A0*E0*Inv1-(3/8)*t*B0*A0^2*Inv2+(5/32)*k0*A0^2*Inv1;",
            "poly H15=(3/4)*(A0*E1+A1*E0)*Inv1-(3/8)*t*(B1*A0^2+2*B0*A0*A1)*Inv2+(5/32)*(k1*A0^2+2*k0*A0*A1)*Inv1-(1/16)*t^3*A0^3*Inv3;",
            "poly D14_0=H14; poly D15_0=H15;",
        ]
    )
    for ell in range(1, 8):
        factorial = math.factorial(ell)
        lines.extend(
            [
                f"poly D14_{ell}=diff(D14_{ell - 1},t);",
                f"poly D15_{ell}=diff(D15_{ell - 1},t);",
                f"poly h14_{ell}=subst(D14_{ell},t,0)/{factorial};",
                f"poly h15_{ell}=subst(D15_{ell},t,0)/{factorial};",
            ]
        )
    lines.extend(
        [
            'print("SQUARE_APROLONG_ROW_TRANSFORM_RELATION=q^2+(p/2)*v^2-1");',
            'print("SQUARE_APROLONG_ROW_TRANSFORM_UNIT_DIAGONAL=1");',
            "int row14=1; int row15=1;",
        ]
    )
    for ell in range(1, 8):
        summands = []
        for j in range(1, ell + 1):
            coefficient = transform_entry(ell, j)
            if coefficient != "0":
                summands.append(f"({coefficient})*h14_{j}")
        pred14 = "+".join(summands).replace("+-", "-") or "0"
        summands = []
        for j in range(1, ell + 1):
            coefficient = transform_entry(ell, j)
            if coefficient != "0":
                summands.append(f"({coefficient})*h15_{j}")
        pred15 = "+".join(summands).replace("+-", "-") or "0"
        lines.extend(
            [
                f"poly Check14_{ell}=g14_{ell}-({pred14});",
                f"poly Check15_{ell}=g15_{ell}-({pred15});",
                f"if (Check14_{ell}!=0) {{ row14=0; print(\"SQUARE_APROLONG_G14_REMAINDER_{ell}\"); print(Check14_{ell}); }}",
                f"if (Check15_{ell}!=0) {{ row15=0; print(\"SQUARE_APROLONG_G15_REMAINDER_{ell}\"); print(Check15_{ell}); }}",
            ]
        )
    lines.extend(
        [
            'print("SQUARE_APROLONG_G14_ROW_IDENTITIES="+string(row14));',
            'print("SQUARE_APROLONG_G15_ROW_IDENTITIES="+string(row15));',
            "poly L=z^2+p/2;",
            "poly Az=a1*z+a0; poly A1z=aa1*z+aa0;",
            "poly B0z=bs0*z+br0/4; poly B1z=bs1*z+br1/4;",
            "poly E0z=(e1*z+e0)/2; poly E1z=(ee1*z+ee0)/2;",
            "poly Num15=12*L^2*(Az*E1z+A1z*E0z)-6*L*(B1z*Az^2+2*B0z*Az*A1z)+(5/2)*L^2*(k1*Az^2+2*k0*Az*A1z)-Az^3;",
            "ideal GL=std(ideal(L));",
            "poly ModL=reduce(Num15+Az^3,GL);",
            "int modLIdentity=(ModL==0);",
            'print("SQUARE_APROLONG_NUM15_MOD_L_EQUALS_MINUS_A_CUBED="+string(modLIdentity));',
            'if (row14*row15*modLIdentity!=1) { print("SQUARE_APROLONG_FAIL=ANALYTIC_BRIDGE"); quit; }',
            'print("SQUARE_APROLONG_ENDPOINT=PASS_EXACT_SOURCE_G14_G15_A_ZERO_GATE");',
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
    singular = output / f"square_a_prolongation_{label}.sing"
    emit(singular, args.characteristic, tails)
    result = {
        "status": "PASS-SQUARE-A-PROLONGATION-COMPILER",
        "scope": "GENERIC_SQUARE_HIGH_CONTACT_CONE_G14_G15_ONLY_NO_FAN_OR_ORDER2_VERDICT",
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
