#!/usr/bin/env python3
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
PARSER = ROOT / "cases/max12_812_order2_p0_total_rees_j2_typed_census_v23_20260827/census_j2_typed_v23.py"
PARSER_SHA = "14f2de22d8cabaea12ac7fc7bf72cca275edbbb6a35dc7c0556a6e18e67c4501"
V32_Q = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_grade17_sparse_support_v32_20260827/aws_q/compiled"
V32_BASIS = V32_Q / "BASIS.txt"
V32_BASIS_SHA = "ee4f77808d7e2c36588cfba65f252bcb068dbb360f3e4abb843e2b9215e9819b"
V32_RESULT = V32_Q / "compile_result.json"
V32_RESULT_SHA = "cdbb884eb205b8e731d8dba7a5dd32c0028bd78e95ad4cfedfda71c0dbf91cef"
V33_Q = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g18_v33_20260827/aws_q/compiled"
V33_P = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g18_v33_20260827/aws_p65521/compiled"
V33_Q_ROW = V33_Q / "Tg18_6_q.poly"
V33_Q_ROW_SHA = "fdfb477feb6a97413668f705d9a6bd565501b655f1ab42fc29874121e744a6de"
V33_P_ROW = V33_P / "Tg18_6_p65521.poly"
V33_P_ROW_SHA = "252175cd8c589db1e98a21abd70d09c6d23eb791c22d2405da01f56013f51049"
V33_Q_RESULT = V33_Q / "result.json"
V33_Q_RESULT_SHA = "22f64fbb9d2107508f7218a9aabaea03d6c502219baef84bb918352f7e38df0f"
V33_P_RESULT = V33_P / "result.json"
V33_P_RESULT_SHA = "9f5fd6e47c182f9aa7c095d8aaa966603752e5634ba7ed1b13fec122f6e71991"
PREREG = HERE / "PREREGISTRATION.md"
KEEP = ("ell2", "cs1", "rs2", "aa0", "ee1", "ec3")
PRIME = 65521


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_parser():
    pins = (
        (PARSER, PARSER_SHA), (V32_BASIS, V32_BASIS_SHA),
        (V32_RESULT, V32_RESULT_SHA), (V33_Q_ROW, V33_Q_ROW_SHA),
        (V33_P_ROW, V33_P_ROW_SHA), (V33_Q_RESULT, V33_Q_RESULT_SHA),
        (V33_P_RESULT, V33_P_RESULT_SHA),
    )
    for path, expected in pins:
        if digest(path) != expected:
            fail(("upstream hash", str(path)))
    spec = importlib.util.spec_from_file_location("v34_parser", PARSER)
    if spec is None or spec.loader is None:
        fail("parser import")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def restrict(polynomial):
    answer = {}
    for monomial, coefficient in polynomial.items():
        value = Fraction(coefficient)
        kept = []
        for name, exponent in monomial:
            if name == "a1":
                value *= Fraction(48) ** exponent
            elif name in KEEP:
                kept.append((name, exponent))
            else:
                value = Fraction(0)
                break
        if value:
            key = tuple(kept)
            answer[key] = answer.get(key, Fraction(0)) + value
            if not answer[key]:
                del answer[key]
    return answer


def coefficient_text(value: Fraction, characteristic: int) -> str:
    if characteristic:
        return str((value.numerator * pow(value.denominator, -1, characteristic)) % characteristic)
    return str(value.numerator) if value.denominator == 1 else f"({value.numerator}/{value.denominator})"


def polynomial_text(polynomial, characteristic: int) -> str:
    pieces = []
    for monomial, coefficient in sorted(polynomial.items()):
        factors = [coefficient_text(coefficient, characteristic)]
        factors += [name if exponent == 1 else f"{name}^{exponent}" for name, exponent in monomial]
        pieces.append("*".join(factors))
    return "+".join(pieces).replace("+-", "-") if pieces else "0"


def modular_shadow(polynomial):
    return {monomial: (coefficient.numerator * pow(coefficient.denominator, -1, PRIME)) % PRIME
            for monomial, coefficient in polynomial.items()}


def branch_laurent(polynomial):
    values = {
        "aa0": (Fraction(0), 0), "ell2": (Fraction(1), 1),
        "cs1": (Fraction(12), -1), "rs2": (Fraction(-20, 9), 2),
        "ee1": (Fraction(32), 1), "ec3": (Fraction(576), -1),
    }
    answer = {}
    for monomial, coefficient in polynomial.items():
        value = coefficient; exponent_l = 0
        for name, exponent in monomial:
            scalar, degree = values[name]
            value *= scalar ** exponent; exponent_l += degree * exponent
        answer[exponent_l] = answer.get(exponent_l, Fraction(0)) + value
    return {degree: value for degree, value in answer.items() if value}


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("output", type=Path)
    cli.add_argument("--characteristic", type=int, choices=(0, PRIME), required=True)
    args = cli.parse_args()
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if platform.system() != "Linux" or not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2" or not tag:
        fail("registered AWS EC2 lane required")
    output = args.output.resolve(); output.mkdir(parents=True, exist_ok=False)
    parser = load_parser()

    q_face = restrict(parser.parse(V33_Q_ROW))
    p_face = restrict(parser.parse(V33_P_ROW))
    if len(q_face) != 16 or branch_laurent(q_face) != {-1: Fraction(41472)}:
        fail(("Q restriction control", len(q_face), branch_laurent(q_face)))
    if modular_shadow(q_face) != {monomial: int(coefficient) % PRIME for monomial, coefficient in p_face.items()}:
        fail("finite-field row shadow")

    basis = V32_BASIS.read_text().strip()
    if not basis or basis.count(",") != 23:
        fail("V32 basis census")
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    nf_path = output / f"Tg18_6_mod_grade17_{label}.txt"
    basis18_path = output / f"BASIS_G18_{label}.txt"
    script = output / f"grade18_curve_cut_{label}.sing"
    lines = [
        f"ring R={args.characteristic},({','.join(KEEP)}),dp;",
        "option(redSB);", "option(prot);",
        f"ideal G={basis};", "ideal GS=std(G);",
        "if (reduce(G[1],GS)!=0) { print(\"FAIL_OLD_BASIS_CONTROL\"); quit; }",
        f"poly P18={polynomial_text(q_face, args.characteristic)};",
        "poly NF18=reduce(P18,GS);",
        "if (NF18==0) { print(\"FAIL_KNOWN_BRANCH_CONTROL\"); quit; }",
        "print(\"V34_CONTROLS=1\");",
        f"write(\":w {nf_path}\",string(NF18));",
        "ideal H=G,P18;", "ideal GH=std(H);",
        "int d=dim(GH);", "int sz=size(GH);", "poly nf1=reduce(1,GH);",
        "print(\"V34_DIM=\"+string(d));", "print(\"V34_STANDARD_BASIS_SIZE=\"+string(sz));",
        "if (nf1==0) { print(\"V34_UNIT_IDEAL=1\"); } else { print(\"V34_UNIT_IDEAL=0\"); }",
        "if (d==0 && nf1!=0) { print(\"V34_VDIM=\"+string(vdim(GH))); } else { print(\"V34_VDIM=NA\"); }",
        f"write(\":w {basis18_path}\",string(GH));",
        "print(\"PASS_A1_GRADE18_CURVE_CUT_V34\");", "quit;",
    ]
    script.write_text("\n".join(lines) + "\n")
    result = {
        "status": "PASS-A1-GRADE18-CURVE-CUT-V34-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "preregistration_sha256": digest(PREREG),
        "variables": list(KEEP),
        "old_basis_size": 24,
        "grade18_row": "Tg18_6",
        "grade18_restricted_term_count": len(q_face),
        "known_branch_value": "41472/l with l^5=243/2",
        "v32_basis_sha256": V32_BASIS_SHA,
        "v32_compile_result_sha256": V32_RESULT_SHA,
        "v33_q_row_sha256": V33_Q_ROW_SHA,
        "v33_p_row_sha256": V33_P_ROW_SHA,
        "script": str(script),
        "script_sha256": digest(script),
        "nf_path": str(nf_path),
        "basis18_path": str(basis18_path),
        "scope": "six-coordinate normalized ordered-a1 rho=0 actual-total rows through grade18",
    }
    result_path = output / "compile_result.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("PASS-A1-GRADE18-CURVE-CUT-V34-COMPILER")
    print(f"SCRIPT_SHA256={digest(script)}")


if __name__ == "__main__":
    main()
