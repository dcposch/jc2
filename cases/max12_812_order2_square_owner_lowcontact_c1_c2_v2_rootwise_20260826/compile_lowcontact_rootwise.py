#!/usr/bin/env python3
"""Compile lightweight exact rootwise c=1,c=2 clients from frozen source."""

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
LOW = ROOT / "cases/max12_812_order2_square_owner_lowcontact_c1_c2_20260826/compile_lowcontact_c1_c2.py"
LOW_FREEZE = ROOT / "cases/max12_812_order2_square_owner_lowcontact_c1_c2_20260826/FREEZE.sha256"
CGE = ROOT / "cases/max12_812_order2_square_owner_cge3_universal_20260826/compile_cge3_universal.py"
CGE_FREEZE = ROOT / "cases/max12_812_order2_square_owner_cge3_universal_20260826/FREEZE.sha256"
PINS = {
    LOW: "85c411a3f0feb2b2f55840704aa4c88e24e8d83fd981d32674b016529e966c89",
    LOW_FREEZE: "a35b0784e083db86b1f658620acfa650839a3318e67b7c1b372ca69398048567",
    CGE: "352ad4f2d10df80e7edcc5179a8c46dfc55b4f7ce07762fb06d2109a9da1da23",
    CGE_FREEZE: "a5efc70c73fb1539086b58bc386a26815e9edb754c50eee505ab8f0918d18169",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only low-contact rootwise compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only low-contact rootwise compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        fail(("cannot load frozen module", str(path)))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def extract_series(poly: str, prefix: str, start: int, stop: int) -> list[str]:
    lines = [
        f"ideal {prefix}Sigma=std(ideal(sigma^{start})); int {prefix}div=1;",
        f"if (reduce({poly},{prefix}Sigma)!=0) {{ {prefix}div=0; }}",
        f"poly {prefix}Q{start}={poly}/sigma^{start};",
        f"if (sigma^{start}*{prefix}Q{start}-{poly}!=0) {{ {prefix}div=0; }}",
        f"poly {prefix}H{start}=subst({prefix}Q{start},sigma,0);",
    ]
    previous = f"{prefix}Q{start}"
    for grade in range(start + 1, stop + 1):
        prior_h = f"{prefix}H{grade - 1}"
        rem = f"{prefix}Rem{grade}"
        quotient = f"{prefix}Q{grade}"
        lines.extend(
            [
                f"poly {rem}={previous}-{prior_h};",
                f"if (reduce({rem},std(ideal(sigma)))!=0) {{ {prefix}div=0; }}",
                f"poly {quotient}={rem}/sigma;",
                f"if (sigma*{quotient}-{rem}!=0) {{ {prefix}div=0; }}",
                f"poly {prefix}H{grade}=subst({quotient},sigma,0);",
            ]
        )
        previous = quotient
    return lines


def coefficient_rows(prefix: str, start: int, stop: int) -> list[str]:
    lines: list[str] = []
    for grade in range(start, stop + 1):
        lines.append(f"poly {prefix}D{grade}_0={prefix}H{grade};")
    for derivative in range(1, 9):
        factorial = math.factorial(derivative)
        for grade in range(start, stop + 1):
            lines.append(f"poly {prefix}D{grade}_{derivative}=diff({prefix}D{grade}_{derivative - 1},t);")
        if derivative >= 2:
            row = derivative - 1
            for grade in range(start, stop + 1):
                lines.append(f"poly {prefix}h{grade}_{row}=subst({prefix}D{grade}_{derivative},t,0)/{factorial};")
    return lines


def row_bridge(prefix: str, start: int, stop: int, cge) -> list[str]:
    lines = [f"int {prefix}rows=1;"]
    for i in range(1, 8):
        for grade in range(start, stop + 1):
            pieces: list[str] = []
            for j in range(1, i + 1):
                transforms = cge.transform_series(i, j)
                for shift in range(grade - start + 1):
                    coefficient = transforms[shift]
                    if coefficient != "0":
                        pieces.append(f"({coefficient})*{prefix}h{grade - shift}_{j}")
            prediction = "+".join(pieces).replace("+-", "-") or "0"
            lines.extend(
                [
                    f"poly {prefix}Check{grade}_{i}={prefix}g{grade}_{i}-({prediction});",
                    f"if ({prefix}Check{grade}_{i}!=0) {{ {prefix}rows=0; print(\"SQUARE_ROOTWISE_{prefix.upper()}_G{grade}_REMAINDER_{i}\"); print({prefix}Check{grade}_{i}); }}",
                ]
            )
    return lines


def derivative_coefficients(poly: str, prefix: str, max_degree: int) -> tuple[list[str], list[str]]:
    lines = [f"poly {prefix}D0={poly};", f"poly {prefix}c0=subst({prefix}D0,z,0);"]
    names = [f"{prefix}c0"]
    for degree in range(1, max_degree + 2):
        lines.append(f"poly {prefix}D{degree}=diff({prefix}D{degree - 1},z);")
        if degree <= max_degree:
            lines.append(f"poly {prefix}c{degree}=subst({prefix}D{degree},z,0);")
            names.append(f"{prefix}c{degree}")
    return lines, names


def analytic_c1(cge) -> str:
    inv1 = cge.inverse_series(1)
    inv2 = cge.inverse_series(2)
    lines = [
        "poly sp=p/2+sigma*ell1;",
        "poly AA=(a1+a0*t)+sigma*(aa1+aa0*t);",
        "poly EE=sigma*(e11+e10*t)/2+sigma^2*(e21+e20*t)/2;",
        f"poly Inv1={inv1}; poly Inv2={inv2};",
        "poly Hshift=(3/4)*sigma^10*t*AA*EE*Inv1+(3/8)*sigma^10*t^3*EE^2*Inv2;",
    ]
    lines += extract_series("Hshift", "c1a", 11, 12)
    lines += coefficient_rows("c1a", 11, 12)
    lines += row_bridge("c1", 11, 12, cge)
    lines += [
        "poly Ls=z^2+sp; poly Az=(a1*z+a0)+sigma*(aa1*z+aa0);",
        "poly Ez=sigma*(e11*z+e10)/2+sigma^2*(e21*z+e20)/2;",
        "poly Num=(3/4)*sigma^10*Az*Ez*Ls+(3/8)*sigma^10*Ez^2;",
    ]
    lines += extract_series("Num", "c1n", 11, 12)
    lines += [
        "poly L0=z^2+p/2; poly L02=L0^2; ideal GL2=std(ideal(L02));",
        "poly R11=reduce(c1nH11,GL2); poly P11=(c1nH11-R11)/L02;",
        "int c1rec=(L02*P11-(c1nH11-R11)==0);",
        "poly C12=c1nH12-2*L0*ell1*P11; poly E1z=(e11*z+e10)/2;",
    ]
    coeff_lines, names = derivative_coefficients("R11", "c1r", 3)
    lines += coeff_lines
    generators = ",".join(["L0"] + names)
    lines += [
        "int c1degree=(c1rD4==0);",
        f"ideal c1G=std(ideal({generators}));",
        "int c1root=(reduce(C12-(3/8)*E1z^2,c1G)==0);",
        'print("SQUARE_ROOTWISE_C1_ANALYTIC_DIVISIBLE="+string(c1adiv));',
        'print("SQUARE_ROOTWISE_C1_ROW_IDENTITIES="+string(c1rows));',
        'print("SQUARE_ROOTWISE_C1_DIVISION_RECURRENCE="+string(c1rec));',
        'print("SQUARE_ROOTWISE_C1_REMAINDER_DEGREE="+string(c1degree));',
        'print("SQUARE_ROOTWISE_C1_G12_MOD_LOWER_EQUALS_THREE_EIGHTHS_C1_SQUARED="+string(c1root));',
        'if (c1adiv*c1rows*c1rec*c1degree*c1root!=1) { print("SQUARE_ROOTWISE_C1_FAIL=BRIDGE_OR_ROOT"); quit; }',
        'print("SQUARE_ROOTWISE_C1_ENDPOINT=PASS_LEADING_C1_KILLED");',
    ]
    return "\n".join(lines)


def analytic_c2(cge) -> str:
    inv1 = cge.inverse_series(1)
    inv2 = cge.inverse_series(2)
    lines = [
        "poly sp=p/2+sigma*ell1+sigma^2*ell2;",
        "poly AA=(a1+a0*t)+sigma*(aa1+aa0*t)+sigma^2*(aaa1+aaa0*t);",
        "poly EE=sigma^2*(e21+e20*t)/2+sigma^3*(e31+e30*t)/2+sigma^4*(e41+e40*t)/2;",
        "poly BB=sigma*(bs1+(br1/4)*t)+sigma^2*(bs2+(br2/4)*t);",
        "poly kk=k0+sigma*k1;",
        f"poly Inv1={inv1}; poly Inv2={inv2};",
        "poly Hshift=(3/4)*sigma^10*t*AA*EE*Inv1+(3/8)*sigma^10*t^3*EE^2*Inv2-(3/8)*sigma^12*t^2*BB*AA^2*Inv2+(5/16)*sigma^10*kk*BB^3*Inv1+(5/8)*sigma^11*t*kk*BB*EE*Inv1+(5/32)*sigma^14*t*kk*AA^2*Inv1;",
    ]
    lines += extract_series("Hshift", "c2a", 12, 14)
    lines += coefficient_rows("c2a", 12, 14)
    lines += row_bridge("c2", 12, 14, cge)
    lines += [
        "poly Ls=z^2+sp; poly Az=(a1*z+a0)+sigma*(aa1*z+aa0)+sigma^2*(aaa1*z+aaa0);",
        "poly Ez=sigma^2*(e21*z+e20)/2+sigma^3*(e31*z+e30)/2+sigma^4*(e41*z+e40)/2;",
        "poly Bz=sigma*(bs1*z+br1/4)+sigma^2*(bs2*z+br2/4);",
        "poly Num=(3/4)*sigma^10*Az*Ez*Ls+(3/8)*sigma^10*Ez^2-(3/8)*sigma^12*Bz*Az^2+(5/16)*sigma^10*kk*Bz^3*Ls+(5/8)*sigma^11*kk*Bz*Ez*Ls+(5/32)*sigma^14*kk*Az^2*Ls;",
    ]
    lines += extract_series("Num", "c2n", 12, 14)
    lines += [
        "poly L0=z^2+p/2; poly L02=L0^2; ideal GL2=std(ideal(L02));",
        "poly R12=reduce(c2nH12,GL2); poly P12=(c2nH12-R12)/L02;",
        "poly C13=c2nH13-2*L0*ell1*P12; poly R13=reduce(C13,GL2); poly P13=(C13-R13)/L02;",
        "int c2rec=(L02*P12-(c2nH12-R12)==0 && L02*P13-(C13-R13)==0);",
        "poly C14=c2nH14-2*L0*ell1*P13-(2*L0*ell2+ell1^2)*P12;",
        "poly A0z=a1*z+a0; poly E2z=(e21*z+e20)/2;",
    ]
    coeff12, names12 = derivative_coefficients("R12", "c2r12", 3)
    coeff13, names13 = derivative_coefficients("R13", "c2r13", 3)
    lines += coeff12 + coeff13
    generators = ",".join(["L0", "A0z"] + names12 + names13)
    lines += [
        "int c2degree=(c2r12D4==0 && c2r13D4==0);",
        f"ideal c2G=std(ideal({generators}));",
        "int c2root=(reduce(C14-(3/8)*E2z^2,c2G)==0);",
        'print("SQUARE_ROOTWISE_C2_ANALYTIC_DIVISIBLE="+string(c2adiv));',
        'print("SQUARE_ROOTWISE_C2_ROW_IDENTITIES="+string(c2rows));',
        'print("SQUARE_ROOTWISE_C2_DIVISION_RECURRENCE="+string(c2rec));',
        'print("SQUARE_ROOTWISE_C2_REMAINDER_DEGREE="+string(c2degree));',
        'print("SQUARE_ROOTWISE_C2_G14_AT_A_ROOT_EQUALS_THREE_EIGHTHS_C2_SQUARED="+string(c2root));',
        'if (c2adiv*c2rows*c2rec*c2degree*c2root!=1) { print("SQUARE_ROOTWISE_C2_FAIL=BRIDGE_OR_ROOT"); quit; }',
        'print("SQUARE_ROOTWISE_C2_ENDPOINT=PASS_LEADING_C2_KILLED");',
        'print("SQUARE_ROOTWISE_ENDPOINT=PASS_C1_C2_KILLED");',
        "quit;",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    for source, expected in PINS.items():
        if digest(source) != expected:
            fail(("frozen pin mismatch", str(source)))
    low = load_module("square_low_v1", LOW)
    cge = load_module("square_cge_v1", CGE)
    for source, expected in low.EXPECTED.items():
        if digest(source) != expected:
            fail(("frozen low-contact transitive mismatch", str(source)))
    tails = json.loads(low.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != low.EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    target = output / f"square_lowcontact_rootwise_{label}.sing"
    low.emit(target, args.characteristic, tails)
    text = target.read_text()
    for ring in ("Rc1full", "Rc2full"):
        old = f"ring {ring}={args.characteristic},("
        new = old + "z,t,"
        if text.count(old) != 1:
            fail(("source ring anchor missing or nonunique", ring, text.count(old)))
        text = text.replace(old, new)
    c1_rad = text.find("ideal c1Efull=")
    c2_ring = text.find(f"ring Rc2full={args.characteristic},")
    if c1_rad < 0 or c2_ring < 0 or c2_ring <= c1_rad:
        fail("c1 radical/c2 ring anchors missing")
    text = text[:c1_rad] + analytic_c1(cge) + "\n" + text[c2_ring:]
    c2_rad = text.find("ideal c2Efull=")
    if c2_rad < 0:
        fail("c2 radical anchor missing")
    text = text[:c2_rad] + analytic_c2(cge) + "\n"
    target.write_text(text)
    payload = {
        "status": "PASS-SQUARE-LOWCONTACT-ROOTWISE-COMPILER",
        "scope": "C1_C2_ROOTWISE_GENERIC_SQUARE_ONLY_NO_SQUARE_OR_ORDER2_VERDICT",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "low_compiler_sha256": digest(LOW),
        "cge_compiler_sha256": digest(CGE),
        "input_sha256": digest(target),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
