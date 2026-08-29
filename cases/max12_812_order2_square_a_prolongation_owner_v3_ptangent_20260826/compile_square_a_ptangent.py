#!/usr/bin/env python3
"""Compile the moving-p tangent addendum to the square A-prolongation.

AWS-only.  The frozen owner-v2 compiler is used as the complete-source
emitter, but p is replaced by p+2*sigma*ell so that
L(sigma)=z^2+p/2+sigma*ell.  Exact row identities include both the moving
Laurent receiver and the derivative of the square-base row transform.
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
OWNER = ROOT / "cases/max12_812_order2_square_a_prolongation_owner_v2_20260826/compile_square_a_prolongation.py"
OWNER_FREEZE = ROOT / "cases/max12_812_order2_square_a_prolongation_owner_v2_20260826/FREEZE.sha256"
OWNER_RESULT = ROOT / "cases/max12_812_order2_square_a_prolongation_owner_v2_20260826/RESULT.md"
OWNER_RESULTS = ROOT / "cases/max12_812_order2_square_a_prolongation_owner_v2_20260826/RESULTS.sha256"

EXPECTED = {
    OWNER: "2c7f051da265f5af3ee76007360e41af92f8492c5969846f8e529317d4dd5630",
    OWNER_FREEZE: "6dbf5b6118aac14c38facdd977e221b0e4648a9e875fe03867172c646e322f64",
    OWNER_RESULT: "eba4640a9c7da51e4297e7e0b3c236f73f2eb2f70770de0634e1d0fea652d13f",
    OWNER_RESULTS: "3f3d729ed046431e92a6cbd1f5e373526525f39422a495fe9d66def8476a6e80",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only square p-tangent compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only square p-tangent compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_owner():
    spec = importlib.util.spec_from_file_location("square_aprol_owner_v2", OWNER)
    if spec is None or spec.loader is None:
        fail("cannot load frozen owner-v2 compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def moving_source_coefficients() -> dict[int, str]:
    pp = "(p+2*sigma*ell)"
    c = "(sigma^4*bs0+sigma^5*bs1)"
    r = f"((({pp})^2+sigma^4*br0+sigma^5*br1)/4)"
    n3 = "(sigma^3*(a1+sigma*aa1))"
    n2 = "(sigma^3*(a0+sigma*aa0))"
    n1 = f"(sigma^3*(({pp})*(a1+sigma*aa1)+sigma^4*(e1+sigma*ee1))/2)"
    n0 = f"(sigma^3*(({pp})*(a0+sigma*aa0)+sigma^4*(e0+sigma*ee0))/2)"
    return {
        6: f"(2*({pp}))",
        5: f"(2*({c}))",
        4: f"(({pp})^2+2*({r}))",
        3: f"(2*({pp})*({c})+sigma^2*({n3}))",
        2: f"(({c})^2+2*({pp})*({r})+sigma^2*({n2}))",
        1: f"(2*({c})*({r})+sigma^2*({n1}))",
        0: f"(({r})^2+sigma^2*({n0}))",
    }


def qtext(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"({value.numerator}/{value.denominator})"


def transform_pair(ell_index: int, j: int) -> tuple[str, str]:
    """Return T(p) and d/dsigma T(p+2*sigma*ell) at sigma=0."""

    delta = ell_index - j
    if delta < 0 or delta % 2:
        return "0", "0"
    n = delta // 2
    coefficient = Fraction(1)
    for r in range(n):
        coefficient *= Fraction(j, 2) + r
    coefficient /= math.factorial(n)
    coefficient /= 2**n

    def monomial(value: Fraction, degree: int, tangent: bool = False) -> str:
        if value == 0:
            return "0"
        factors: list[str] = []
        if tangent:
            factors.append("ell")
        if degree == 1:
            factors.append("p")
        elif degree > 1:
            factors.append(f"p^{degree}")
        body = "*".join(factors)
        if not body:
            return qtext(value)
        if value == 1:
            return body
        if value == -1:
            return "-" + body
        return f"{qtext(value)}*{body}"

    base = monomial(coefficient, n)
    derivative = monomial(2 * n * coefficient, n - 1, tangent=True) if n else "0"
    return base, derivative


def analytic_block() -> list[str]:
    lines = [
        "poly ss=p/2;",
        "poly A0=a1+a0*t; poly A1=aa1+aa0*t;",
        "poly B0=bs0+(br0/4)*t; poly B1=bs1+(br1/4)*t;",
        "poly E0=(e1+e0*t)/2; poly E1=(ee1+ee0*t)/2;",
        "poly Inv1=1-ss*t^2+ss^2*t^4-ss^3*t^6;",
        "poly Inv2=1-2*ss*t^2+3*ss^2*t^4-4*ss^3*t^6;",
        "poly Inv3=1-3*ss*t^2+6*ss^2*t^4-10*ss^3*t^6;",
        "poly H14=(3/4)*A0*E0*Inv1-(3/8)*t*B0*A0^2*Inv2+(5/32)*k0*A0^2*Inv1;",
        "poly H15fixed=(3/4)*(A0*E1+A1*E0)*Inv1-(3/8)*t*(B1*A0^2+2*B0*A0*A1)*Inv2+(5/32)*(k1*A0^2+2*k0*A0*A1)*Inv1-(1/16)*t^3*A0^3*Inv3;",
        "poly DeltaH=-(3/4)*ell*t^2*A0*E0*Inv2+(3/4)*ell*t^3*B0*A0^2*Inv3-(5/32)*ell*k0*t^2*A0^2*Inv2;",
        "poly H15=H15fixed+DeltaH;",
        "poly D14_0=H14; poly D15_0=H15;",
    ]
    for idx in range(1, 8):
        factorial = math.factorial(idx)
        lines.extend(
            [
                f"poly D14_{idx}=diff(D14_{idx - 1},t);",
                f"poly D15_{idx}=diff(D15_{idx - 1},t);",
                f"poly h14_{idx}=subst(D14_{idx},t,0)/{factorial};",
                f"poly h15_{idx}=subst(D15_{idx},t,0)/{factorial};",
            ]
        )
    lines.extend(
        [
            'print("SQUARE_APROL_PTANGENT_ROW_RELATION=q^2+((p+2sigmaell)/2)*v^2-1");',
            'print("SQUARE_APROL_PTANGENT_ROW_UNIT_DIAGONAL=1");',
            "int row14=1; int row15=1;",
        ]
    )
    for idx in range(1, 8):
        p14: list[str] = []
        p15: list[str] = []
        for j in range(1, idx + 1):
            base, derivative = transform_pair(idx, j)
            if base != "0":
                p14.append(f"({base})*h14_{j}")
                p15.append(f"({base})*h15_{j}")
            if derivative != "0":
                p15.append(f"({derivative})*h14_{j}")
        pred14 = "+".join(p14).replace("+-", "-") or "0"
        pred15 = "+".join(p15).replace("+-", "-") or "0"
        lines.extend(
            [
                f"poly Check14_{idx}=g14_{idx}-({pred14});",
                f"poly Check15_{idx}=g15_{idx}-({pred15});",
                f"if (Check14_{idx}!=0) {{ row14=0; print(\"SQUARE_APROL_PTANGENT_G14_REMAINDER_{idx}\"); print(Check14_{idx}); }}",
                f"if (Check15_{idx}!=0) {{ row15=0; print(\"SQUARE_APROL_PTANGENT_G15_REMAINDER_{idx}\"); print(Check15_{idx}); }}",
            ]
        )
    lines.extend(
        [
            'print("SQUARE_APROL_PTANGENT_G14_ROW_IDENTITIES="+string(row14));',
            'print("SQUARE_APROL_PTANGENT_G15_ROW_IDENTITIES="+string(row15));',
            "poly L=z^2+p/2;",
            "poly Az=a1*z+a0; poly A1z=aa1*z+aa0;",
            "poly B0z=bs0*z+br0/4; poly B1z=bs1*z+br1/4;",
            "poly E0z=(e1*z+e0)/2; poly E1z=(ee1*z+ee0)/2;",
            "poly Num14=24*L*Az*E0z-12*B0z*Az^2+5*k0*L*Az^2;",
            "poly Num15fixed=12*L^2*(Az*E1z+A1z*E0z)-6*L*(B1z*Az^2+2*B0z*Az*A1z)+(5/2)*L^2*(k1*Az^2+2*k0*Az*A1z)-Az^3;",
            "poly DeltaNum=-12*ell*L*Az*E0z+12*ell*B0z*Az^2-(5/2)*ell*k0*L*Az^2;",
            "ideal GL=std(ideal(L));",
            "int grade14Gate=(reduce(Num14+12*B0z*Az^2,GL)==0);",
            "int deltaModL=(reduce(DeltaNum-12*ell*B0z*Az^2,GL)==0);",
            "int deltaKilledByG14=(reduce(DeltaNum+ell*Num14,GL)==0);",
            "int movingSeparator=(reduce(Num15fixed+DeltaNum+Az^3+ell*Num14,GL)==0);",
            'print("SQUARE_APROL_PTANGENT_G14_MOD_L_GATE="+string(grade14Gate));',
            'print("SQUARE_APROL_PTANGENT_DELTA_MOD_L="+string(deltaModL));',
            'print("SQUARE_APROL_PTANGENT_DELTA_KILLED_BY_G14="+string(deltaKilledByG14));',
            'print("SQUARE_APROL_PTANGENT_MOVING_SEPARATOR="+string(movingSeparator));',
            'if (row14*row15*grade14Gate*deltaModL*deltaKilledByG14*movingSeparator!=1) { print("SQUARE_APROL_PTANGENT_FAIL=EXACT_IDENTITY"); quit; }',
            'print("SQUARE_APROL_PTANGENT_ENDPOINT=PASS_MOVING_P_SOURCE_ROW_ADDENDUM");',
            "quit;",
        ]
    )
    return lines


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    for source, expected in EXPECTED.items():
        actual = digest(source)
        if actual != expected:
            fail(("frozen owner dependency mismatch", str(source), actual, expected))
    owner = load_owner()
    for source, expected in owner.EXPECTED_STATIC.items():
        actual = digest(source)
        if actual != expected:
            fail(("frozen transitive dependency mismatch", str(source), actual, expected))
    tails = json.loads(owner.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != owner.EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    target = output / f"square_a_ptangent_{label}.sing"
    owner.source_coefficients = moving_source_coefficients
    owner.emit(target, args.characteristic, tails)
    text = target.read_text()
    ring_old = ",mu2,mu4,mu6,J,t,z),dp;"
    ring_new = ",mu2,mu4,mu6,J,ell,t,z),dp;"
    if text.count(ring_old) != 1:
        fail("owner ring anchor missing or nonunique")
    text = text.replace(ring_old, ring_new)

    analytic_start = text.find("poly ss=p/2;")
    endpoint = text.find('print("SQUARE_APROL_ENDPOINT=PASS_EXACT_SOURCE_G14_G15_A_ZERO_GATE");')
    if analytic_start < 0 or endpoint < 0 or endpoint <= analytic_start:
        fail("owner analytic/end anchor missing")
    quit_at = text.find("quit;", endpoint)
    if quit_at < 0:
        fail("owner quit anchor missing")
    text = text[:analytic_start] + "\n".join(analytic_block()) + "\n"
    target.write_text(text)

    payload = {
        "status": "PASS-SQUARE-A-PTANGENT-COMPILER",
        "scope": "MOVING_P_ADDENDUM_TO_HIGH_CONTACT_CONE_ONLY_NO_FAN_OR_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "owner_compiler_sha256": digest(OWNER),
        "owner_results_sha256": digest(OWNER_RESULTS),
        "input_sha256": digest(target),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
