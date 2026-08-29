#!/usr/bin/env python3
"""Compile the complete generic-square c>=3, r>=1 grade-13--15 gate."""

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
BASE = ROOT / "cases/max12_812_order2_square_load_ladder_20260826/compile_square_load_ladder.py"
PADE = ROOT / "xmodel/max12-812-order2-first-normal-pade-support-promotion-20260826.md"
HALF = ROOT / "cases/max12_812_order2_square_halfweight_kuranishi_20260826/RESULTS.md"
HALF_REVIEW = ROOT / "xmodel/max12-812-order2-square-halfweight-kuranishi-hostile-review-grok-20260826.md"
PTANGENT = ROOT / "cases/max12_812_order2_square_a_prolongation_owner_v5_ptangent_validator_20260826/RESULT.md"

EXPECTED = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    BASE: "77f25216f0ab17abb3a8f4be271b2ea38f883806a72523cdca1be659df90dcdc",
    PADE: "40790378bfcc7b0e0719038ef0e951712abef570b4865c0bca371409706c9f94",
    HALF: "eb2cd8036a0abf87a1ff7a58c116346b11973efc47f35f9cb76105a6ccd485af",
    HALF_REVIEW: "49744ab901f05ae6d8f0163fd195f3b0219e725f051c3aeebf31fcdaa13c4214",
    PTANGENT: "74551fe8b2ed1e4b9b1fd1594cee54e3bd3d87e6acee8b8c29d9384f5317d5ea",
}
EXPECTED_ALL_TAILS = "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only c>=3 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only c>=3 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_base():
    spec = importlib.util.spec_from_file_location("square_tail_base", BASE)
    if spec is None or spec.loader is None:
        fail("cannot load frozen base compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def qtext(value: Fraction) -> str:
    if value == 0:
        return "0"
    if value.denominator == 1:
        return str(value.numerator)
    return f"({value.numerator}/{value.denominator})"


def monomial(value: Fraction, factors: list[str]) -> str:
    if value == 0:
        return "0"
    body = "*".join(factors)
    if not body:
        return qtext(value)
    if value == 1:
        return body
    if value == -1:
        return "-" + body
    return f"{qtext(value)}*{body}"


def transform_series(i: int, j: int) -> tuple[str, str, str]:
    """Coefficients through sigma^2 of T_ij(p+2 sigma l1+2 sigma^2 l2)."""

    delta = i - j
    if delta < 0 or delta % 2:
        return "0", "0", "0"
    n = delta // 2
    coefficient = Fraction(1)
    for index in range(n):
        coefficient *= Fraction(j, 2) + index
    coefficient /= math.factorial(n)
    coefficient /= 2**n

    def ppow(degree: int) -> list[str]:
        return [] if degree == 0 else (["p"] if degree == 1 else [f"p^{degree}"])

    t0 = monomial(coefficient, ppow(n))
    t1 = monomial(2 * n * coefficient, ["ell1"] + ppow(n - 1)) if n else "0"
    second: list[str] = []
    if n:
        second.append(monomial(2 * n * coefficient, ["ell2"] + ppow(n - 1)))
    if n >= 2:
        second.append(monomial(2 * n * (n - 1) * coefficient, ["ell1^2"] + ppow(n - 2)))
    t2 = "+".join(part for part in second if part != "0").replace("+-", "-") or "0"
    return t0, t1, t2


def source_coefficients() -> dict[int, str]:
    pp = "(p+2*sigma*ell1+2*sigma^2*ell2)"
    az = "(a1+sigma*aa1+sigma^2*aaa1)"
    ac = "(a0+sigma*aa0+sigma^2*aaa0)"
    cz = "(sigma^3*e31+sigma^4*e41+sigma^5*e51)"
    cc = "(sigma^3*e30+sigma^4*e40+sigma^5*e50)"
    kc = "(sigma^3*bs1+sigma^4*bs2+sigma^5*bs3)"
    kr = f"((({pp})^2+sigma^3*br1+sigma^4*br2+sigma^5*br3)/4)"
    n3 = f"(sigma^3*{az})"
    n2 = f"(sigma^3*{ac})"
    n1 = f"(sigma^3*(({pp})*{az}+({cz}))/2)"
    n0 = f"(sigma^3*(({pp})*{ac}+({cc}))/2)"
    return {
        6: f"(2*({pp}))",
        5: f"(2*({kc}))",
        4: f"(({pp})^2+2*({kr}))",
        3: f"(2*({pp})*({kc})+sigma^2*({n3}))",
        2: f"(({kc})^2+2*({pp})*({kr})+sigma^2*({n2}))",
        1: f"(2*({kc})*({kr})+sigma^2*({n1}))",
        0: f"(({kr})^2+sigma^2*({n0}))",
    }


def inverse_series(power: int) -> str:
    terms: list[str] = []
    for n in range(6):
        coefficient = Fraction((-1) ** n * math.comb(n + power - 1, power - 1))
        factor = "1" if n == 0 else ("sp*t^2" if n == 1 else f"sp^{n}*t^{2*n}")
        terms.append(monomial(coefficient, [] if n == 0 else [factor]))
    return "+".join(terms).replace("+-", "-")


def emit(path: Path, characteristic: int, tails) -> None:
    base = load_base()
    coeffs = source_coefficients()
    loads = {"k10": "(k0+sigma*k1+sigma^2*kk2)", "k6": "k6", "k2": "k2load"}
    targets = {1: "0", 2: "mu2", 3: "0", 4: "mu4", 5: "0", 6: "mu6", 7: "J/4"}
    variables = (
        "z,t,sigma,p,ell1,ell2,a0,a1,aa0,aa1,aaa0,aaa1,"
        "e30,e31,e40,e41,e50,e51,bs1,br1,bs2,br2,bs3,br3,"
        "k0,k1,kk2,k6,k2load,mu2,mu4,mu6,J"
    )
    lines = [
        f"ring R={characteristic},({variables}),dp;",
        'print("SQUARE_CGE3_SOURCE_HASHES=PASS");',
        "ideal Sigma13=std(ideal(sigma^13)); ideal Sigma1=std(ideal(sigma));",
        "int divisible=1; int identities=1; int forbidden=1;",
    ]
    grade_rows: dict[int, list[str]] = {13: [], 14: [], 15: []}
    for row in range(1, 8):
        expression = base.tail_text(tails[str(row)], row, coeffs, loads).replace("Lambda", "(sigma^2)")
        if targets[row] != "0":
            expression += f"-sigma^{2 * (12 + row)}*({targets[row]})"
        lines.extend(
            [
                f"poly Phi{row}={expression};",
                f"if (reduce(Phi{row},Sigma13)!=0) {{ divisible=0; }}",
                f"poly Q13_{row}=Phi{row}/sigma^13;",
                f"if (sigma^13*Q13_{row}-Phi{row}!=0) {{ identities=0; }}",
                f"poly g13_{row}=subst(Q13_{row},sigma,0);",
                f"poly Rem14_{row}=Q13_{row}-g13_{row};",
                f"if (reduce(Rem14_{row},Sigma1)!=0) {{ identities=0; }}",
                f"poly Q14_{row}=Rem14_{row}/sigma;",
                f"if (sigma*Q14_{row}-Rem14_{row}!=0) {{ identities=0; }}",
                f"poly g14_{row}=subst(Q14_{row},sigma,0);",
                f"poly Rem15_{row}=Q14_{row}-g14_{row};",
                f"if (reduce(Rem15_{row},Sigma1)!=0) {{ identities=0; }}",
                f"poly Q15_{row}=Rem15_{row}/sigma;",
                f"if (sigma*Q15_{row}-Rem15_{row}!=0) {{ identities=0; }}",
                f"poly g15_{row}=subst(Q15_{row},sigma,0);",
            ]
        )
        grade_rows[13].append(f"g13_{row}")
        grade_rows[14].append(f"g14_{row}")
        grade_rows[15].append(f"g15_{row}")
        for grade in (13, 14, 15):
            for variable in ("k6", "k2load", "mu2", "mu4", "mu6", "J"):
                lines.append(f"if (diff(g{grade}_{row},{variable})!=0) {{ forbidden=0; }}")
    lines.extend(
        [
            'print("SQUARE_CGE3_DIVISIBLE="+string(divisible));',
            'print("SQUARE_CGE3_QUOTIENT_IDENTITIES="+string(identities));',
            'print("SQUARE_CGE3_FORBIDDEN="+string(forbidden));',
            'if (divisible*identities*forbidden!=1) { print("SQUARE_CGE3_FAIL=SOURCE_EXTRACTION"); quit; }',
        ]
    )
    for grade in (13, 14, 15):
        lines.extend(
            [
                f'print("SQUARE_CGE3_G{grade}_BEGIN");',
                "; ".join(f"print({name})" for name in grade_rows[grade]) + ";",
                f'print("SQUARE_CGE3_G{grade}_END");',
            ]
        )

    inv1 = inverse_series(1)
    inv2 = inverse_series(2)
    inv3 = inverse_series(3)
    lines.extend(
        [
            "poly sp=p/2+sigma*ell1+sigma^2*ell2;",
            "poly AA=(a1+a0*t)+sigma*(aa1+aa0*t)+sigma^2*(aaa1+aaa0*t);",
            "poly BB=sigma*(bs1+(br1/4)*t)+sigma^2*(bs2+(br2/4)*t)+sigma^3*(bs3+(br3/4)*t);",
            "poly EE=sigma^3*(e31+e30*t)/2+sigma^4*(e41+e40*t)/2+sigma^5*(e51+e50*t)/2;",
            "poly kk=k0+sigma*k1+sigma^2*kk2;",
            f"poly Inv1={inv1};",
            f"poly Inv2={inv2};",
            f"poly Inv3={inv3};",
            "poly Hshift=(3/4)*sigma^10*t*AA*EE*Inv1-(3/8)*sigma^12*t^2*BB*AA^2*Inv2-(1/16)*sigma^15*t^4*AA^3*Inv3+(5/16)*sigma^10*kk*BB^3*Inv1+(5/8)*sigma^11*t*kk*BB*EE*Inv1-(5/32)*sigma^13*t^2*kk*BB^2*AA*Inv2+(5/32)*sigma^14*t*kk*AA^2*Inv1;",
            "int analyticDiv=1;",
            "if (reduce(Hshift,Sigma13)!=0) { analyticDiv=0; }",
            "poly HQ13=Hshift/sigma^13; poly HH13=subst(HQ13,sigma,0);",
            "poly HRem14=HQ13-HH13; if (reduce(HRem14,Sigma1)!=0) { analyticDiv=0; }",
            "poly HQ14=HRem14/sigma; poly HH14=subst(HQ14,sigma,0);",
            "poly HRem15=HQ14-HH14; if (reduce(HRem15,Sigma1)!=0) { analyticDiv=0; }",
            "poly HQ15=HRem15/sigma; poly HH15=subst(HQ15,sigma,0);",
            'print("SQUARE_CGE3_ANALYTIC_DIVISIBLE="+string(analyticDiv));',
            "poly D13_0=HH13; poly D14_0=HH14; poly D15_0=HH15;",
        ]
    )
    for derivative in range(1, 9):
        factorial = math.factorial(derivative)
        lines.extend(
            [
                f"poly D13_{derivative}=diff(D13_{derivative - 1},t);",
                f"poly D14_{derivative}=diff(D14_{derivative - 1},t);",
                f"poly D15_{derivative}=diff(D15_{derivative - 1},t);",
            ]
        )
        if derivative >= 2:
            row = derivative - 1
            lines.extend(
                [
                    f"poly h13_{row}=subst(D13_{derivative},t,0)/{factorial};",
                    f"poly h14_{row}=subst(D14_{derivative},t,0)/{factorial};",
                    f"poly h15_{row}=subst(D15_{derivative},t,0)/{factorial};",
                ]
            )

    lines.extend(
        [
            'print("SQUARE_CGE3_ROW_RELATION=q^2+(p(sigma)/2)*v^2-1");',
            'print("SQUARE_CGE3_ROW_UNIT_DIAGONAL=1");',
            "int row13=1; int row14=1; int row15=1;",
        ]
    )
    for i in range(1, 8):
        preds: dict[int, list[str]] = {13: [], 14: [], 15: []}
        for j in range(1, i + 1):
            t0, t1, t2 = transform_series(i, j)
            if t0 != "0":
                preds[13].append(f"({t0})*h13_{j}")
                preds[14].append(f"({t0})*h14_{j}")
                preds[15].append(f"({t0})*h15_{j}")
            if t1 != "0":
                preds[14].append(f"({t1})*h13_{j}")
                preds[15].append(f"({t1})*h14_{j}")
            if t2 != "0":
                preds[15].append(f"({t2})*h13_{j}")
        for grade in (13, 14, 15):
            pred = "+".join(preds[grade]).replace("+-", "-") or "0"
            lines.extend(
                [
                    f"poly Check{grade}_{i}=g{grade}_{i}-({pred});",
                    f"if (Check{grade}_{i}!=0) {{ row{grade}=0; print(\"SQUARE_CGE3_G{grade}_REMAINDER_{i}\"); print(Check{grade}_{i}); }}",
                ]
            )
    lines.extend(
        [
            'print("SQUARE_CGE3_G13_ROW_IDENTITIES="+string(row13));',
            'print("SQUARE_CGE3_G14_ROW_IDENTITIES="+string(row14));',
            'print("SQUARE_CGE3_G15_ROW_IDENTITIES="+string(row15));',
            "poly Ls=z^2+sp;",
            "poly Az=(a1*z+a0)+sigma*(aa1*z+aa0)+sigma^2*(aaa1*z+aaa0);",
            "poly Bz=sigma*(bs1*z+br1/4)+sigma^2*(bs2*z+br2/4)+sigma^3*(bs3*z+br3/4);",
            "poly Ez=sigma^3*(e31*z+e30)/2+sigma^4*(e41*z+e40)/2+sigma^5*(e51*z+e50)/2;",
            "poly Num=(3/4)*sigma^10*Az*Ez*Ls^2-(3/8)*sigma^12*Bz*Az^2*Ls-(1/16)*sigma^15*Az^3+(5/16)*sigma^10*kk*Bz^3*Ls^2+(5/8)*sigma^11*kk*Bz*Ez*Ls^2-(5/32)*sigma^13*kk*Bz^2*Az*Ls+(5/32)*sigma^14*kk*Az^2*Ls^2;",
            "int numDiv=1; if (reduce(Num,Sigma13)!=0) { numDiv=0; }",
            "poly NQ13=Num/sigma^13; poly N13=subst(NQ13,sigma,0);",
            "poly NRem14=NQ13-N13; if (reduce(NRem14,Sigma1)!=0) { numDiv=0; }",
            "poly NQ14=NRem14/sigma; poly N14=subst(NQ14,sigma,0);",
            "poly NRem15=NQ14-N14; if (reduce(NRem15,Sigma1)!=0) { numDiv=0; }",
            "poly NQ15=NRem15/sigma; poly N15=subst(NQ15,sigma,0);",
            "poly L0=z^2+p/2; poly L03=L0^3; ideal GL3=std(ideal(L03));",
            "poly R13=reduce(N13,GL3); poly P13=(N13-R13)/L03;",
            "int divisionRec=1; if (L03*P13-(N13-R13)!=0) { divisionRec=0; }",
            "poly C14=N14-3*L0^2*ell1*P13; poly R14=reduce(C14,GL3); poly P14=(C14-R14)/L03;",
            "if (L03*P14-(C14-R14)!=0) { divisionRec=0; }",
            "poly C15=N15-3*L0^2*ell1*P14-(3*L0^2*ell2+3*L0*ell1^2)*P13;",
            "ideal GL=std(ideal(L0)); poly A0z=a1*z+a0;",
            "int separator=(reduce(C15+A0z^3,GL)==0);",
            'print("SQUARE_CGE3_NUMERATOR_DIVISIBLE="+string(numDiv));',
            'print("SQUARE_CGE3_MOVING_DIVISION_RECURRENCE="+string(divisionRec));',
            'print("SQUARE_CGE3_G15_MOD_L_EQUALS_MINUS_A_CUBED="+string(separator));',
            'if (analyticDiv*row13*row14*row15*numDiv*divisionRec*separator!=1) { print("SQUARE_CGE3_FAIL=EXACT_BRIDGE_OR_SEPARATOR"); quit; }',
            'print("SQUARE_CGE3_ENDPOINT=PASS_UNIVERSAL_CGE3_RGE1_A_ZERO_GATE");',
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
    target = output / f"square_cge3_universal_{label}.sing"
    emit(target, args.characteristic, tails)
    payload = {
        "status": "PASS-SQUARE-CGE3-UNIVERSAL-COMPILER",
        "scope": "CGE3_RGE1_GENERIC_SQUARE_G13_G15_ONLY_NO_SQUARE_OR_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "tails_sha256": digest(TAILS),
        "input_sha256": digest(target),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
