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
V34 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_grade18_curve_cut_v34_20260827"
V34_Q_BASIS = V34 / "aws_q/compiled/BASIS_G18_q.txt"
V34_P_BASIS = V34 / "aws_p65521/compiled/BASIS_G18_p65521.txt"
V34_Q_BASIS_SHA = "1e81e737cdab19a9a1b3cb2c6253fecc82c266db236af6fcf67aa03dbd419e40"
V34_P_BASIS_SHA = "96990faf637dc5f3c4bb5b72881fed8fd0b004361b97151605f30c6be3d82bfa"
V35 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_grade19_rational_orbit_v35_20260827"
V35_Q = V35 / "aws_q/compiled"
V35_P = V35 / "aws_p65521/compiled"
V35_Q_RESULT_SHA = "074c7b817d115805ea6e784225fc1dad64d54769ae89421a78ba65769903e256"
V35_P_RESULT_SHA = "1b61cee08b92feeff059ac3a961a4fe8f1f8d355c022a9f1f7eb8dd97726c3f2"
PREREG = HERE / "PREREGISTRATION.md"
KEEP = frozenset(("ell2", "cs1", "rs2", "aa0", "ee1", "ec3"))
ROWS = tuple(range(1, 8))
PRIME = 65521


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_parser():
    if digest(PARSER) != PARSER_SHA:
        fail("parser hash")
    spec = importlib.util.spec_from_file_location("v36_parser", PARSER)
    if spec is None or spec.loader is None:
        fail("parser import")
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module


def modular_shadow(polynomial):
    answer = {}
    for monomial, coefficient in polynomial.items():
        value = (coefficient.numerator * pow(coefficient.denominator, -1, PRIME)) % PRIME
        if value:
            answer[monomial] = value
    return answer


def restrict(polynomial, characteristic: int):
    answer = {}
    for monomial, coefficient in polynomial.items():
        value = Fraction(coefficient); kept = []
        for name, exponent in monomial:
            if name == "a1":
                value *= Fraction(48) ** exponent
            elif name in KEEP:
                kept.append((name, exponent))
            else:
                value = Fraction(0); break
        if characteristic:
            value = Fraction((value.numerator * pow(value.denominator, -1, characteristic)) % characteristic)
        if value:
            key = tuple(kept); answer[key] = answer.get(key, Fraction(0)) + value
            if characteristic and key in answer:
                answer[key] = Fraction(int(answer[key]) % characteristic)
            if not answer.get(key, Fraction(0)):
                answer.pop(key, None)
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


def main() -> None:
    cli = argparse.ArgumentParser(); cli.add_argument("output", type=Path)
    cli.add_argument("--characteristic", type=int, choices=(0, PRIME), required=True)
    args = cli.parse_args(); tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if (platform.system() != "Linux" or not vendor.is_file()
            or vendor.read_text().strip() != "Amazon EC2"
            or not tag.startswith("max12_812_order2_p0_total_rees_j2_a1_grade19_orbit_unit_v36_")):
        fail("registered V36 AWS EC2 lane required")
    output = args.output.resolve(); output.mkdir(parents=True, exist_ok=False)
    for path, expected in ((V34_Q_BASIS, V34_Q_BASIS_SHA), (V34_P_BASIS, V34_P_BASIS_SHA),
                           (V35_Q / "result.json", V35_Q_RESULT_SHA),
                           (V35_P / "result.json", V35_P_RESULT_SHA)):
        if digest(path) != expected:
            fail(("upstream hash", str(path)))
    parser = load_parser(); q_result = json.loads((V35_Q / "result.json").read_text())
    p_result = json.loads((V35_P / "result.json").read_text())
    expected_values = {f"Tg19_{row}": [(-7077888 if row == 7 else 0), 1] for row in ROWS}
    for result in (q_result, p_result):
        if (result.get("outcome") != "killed" or result.get("grade19_values_q") != expected_values
                or result.get("lane_nonzero_rows") != ["Tg19_7"]):
            fail("V35 result contract")

    q_rows = {}; p_rows = {}; row_hashes = {}
    for row in ROWS:
        name = f"Tg19_{row}"
        q_path = V35_Q / f"{name}_q.poly"; p_path = V35_P / f"{name}_p65521.poly"
        if (digest(q_path) != q_result["coefficient_sha256"][name]
                or digest(p_path) != p_result["coefficient_sha256"][name]):
            fail(("V35 row hash", name))
        q_rows[row] = parser.parse(q_path); p_rows[row] = parser.parse(p_path)
        if modular_shadow(q_rows[row]) != {monomial: int(value) % PRIME for monomial, value in p_rows[row].items()}:
            fail(("modular row shadow", name))
        if any(sum(parser.sigma_weight(variable) * exponent for variable, exponent in monomial) != 19
               for monomial in q_rows[row]):
            fail(("sigma homogeneity", name))
        row_hashes[name] = {"q": digest(q_path), "p65521": digest(p_path)}

    weight19_variables = sorted({variable for polynomial in q_rows.values() for monomial in polynomial
                                 for variable, _ in monomial if parser.sigma_weight(variable) == 19})
    if weight19_variables:
        fail(("grade-19 receivers present", weight19_variables))
    q_face = restrict(q_rows[7], 0); p_face = restrict(p_rows[7], PRIME)
    if not q_face or modular_shadow(q_face) != {monomial: int(value) % PRIME for monomial, value in p_face.items()}:
        fail("restricted row shadow")

    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    face = q_face if args.characteristic == 0 else p_face
    basis_path = V34_Q_BASIS if args.characteristic == 0 else V34_P_BASIS
    basis = basis_path.read_text().strip()
    if not basis or basis.count(",") != 11:
        fail("V34 basis census")
    nf_path = output / f"Tg19_7_mod_grade18_{label}.txt"
    final_basis_path = output / f"BASIS_G19_{label}.txt"
    script = output / f"grade19_orbit_unit_{label}.sing"
    lines = [
        f"ring R={args.characteristic},({','.join(sorted(KEEP))}),dp;",
        f"ideal G={basis};", "ideal GS=std(G);",
        "if (reduce(G[1],GS)!=0) { print(\"FAIL_OLD_BASIS_CONTROL\"); quit; }",
        "print(\"V36_OLD_BASIS_CONTROL=1\");",
        f"poly P19={polynomial_text(face, args.characteristic)};", "poly NF19=reduce(P19,GS);",
        "if (NF19==0) { print(\"FAIL_ZERO_NORMAL_FORM\"); quit; }",
        "print(\"V36_NF_NONZERO=1\");", f"write(\":w {nf_path}\",string(NF19));",
        "ideal H=G,P19;", "ideal GH=std(H);", "poly U=reduce(1,GH);",
        "if (U!=0) { print(\"FAIL_NOT_UNIT_IDEAL\"); quit; }",
        "print(\"V36_UNIT_IDEAL=1\");", f"write(\":w {final_basis_path}\",string(GH));",
        "print(\"PASS_A1_GRADE19_ORBIT_UNIT_V36\");", "quit;",
    ]
    script.write_text("\n".join(lines) + "\n")
    result = {
        "status": "PASS-A1-GRADE19-ORBIT-UNIT-V36-COMPILER",
        "registered_aws_lane": tag, "characteristic": args.characteristic,
        "preregistration_sha256": digest(PREREG), "weight19_variables": weight19_variables,
        "rows_checked": len(q_rows), "restricted_row": "Tg19_7",
        "restricted_term_count": len(face), "row_sha256": row_hashes,
        "v35_q_result_sha256": V35_Q_RESULT_SHA, "v35_p_result_sha256": V35_P_RESULT_SHA,
        "v34_basis_sha256": digest(basis_path), "script": str(script), "script_sha256": digest(script),
        "nf_path": str(nf_path), "final_basis_path": str(final_basis_path),
        "scope": "V34 six-coordinate degree-five scheme at grade19; no conclusion outside this support",
    }
    result_path = output / "compile_result.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("PASS-A1-GRADE19-ORBIT-UNIT-V36-COMPILER")
    print("V36_WEIGHT19_VARIABLES=0")
    print(f"RESULT_SHA256={digest(result_path)}")


if __name__ == "__main__":
    main()
