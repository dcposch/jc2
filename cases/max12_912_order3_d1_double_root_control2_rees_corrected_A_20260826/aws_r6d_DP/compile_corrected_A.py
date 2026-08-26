#!/usr/bin/env python3
"""AWS-only compiler for corrected direct-saturation A encodings."""

from hashlib import sha256
import os
from pathlib import Path
import platform
import re


HERE = Path(__file__).resolve().parent
BASE = HERE / "base_B.sing"
EXPECTED = HERE / "expected_B_certificate.stdout"
BASE_SHA = "c905f1b507fda84f62950198bd9528718798c0498ee31e8cc7679479d677693b"
EXPECTED_SHA = "d5317aacf229d85b7b550c40e85d2b7294cae99ba0dedf2e56c2064d4d9ec088"
POLYS = [f"E{i}" for i in range(1, 9)] + ["LT"]


def require_aws() -> str:
    if platform.system() != "Linux":
        raise SystemExit("REFUSE_NON_LINUX")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        raise SystemExit("REFUSE_NON_AWS_EC2")
    tag = os.environ.get("JC2_AWS_TAG", "")
    if not tag.startswith(
        "max12_912_order3_d1_double_root_control2_rees_corrected_A_"
    ):
        raise SystemExit("REFUSE_UNREGISTERED_TAG")
    return tag


def exact_extract(text: str, name: str) -> str:
    matches = re.findall(rf"^poly {name}=(.*);$", text, flags=re.MULTILINE)
    if len(matches) != 1:
        raise SystemExit(f"REFUSE_POLY_ANCHOR_{name}_{len(matches)}")
    return matches[0]


def load_inputs() -> tuple[dict[str, str], list[str]]:
    if sha256(BASE.read_bytes()).hexdigest() != BASE_SHA:
        raise SystemExit("REFUSE_BASE_B_HASH")
    if sha256(EXPECTED.read_bytes()).hexdigest() != EXPECTED_SHA:
        raise SystemExit("REFUSE_EXPECTED_B_HASH")
    base_text = BASE.read_text()
    polynomials = {name: exact_extract(base_text, name) for name in POLYS}
    expected = []
    for index, body in re.findall(
        r"^GH\[([0-9]+)\]=(.*)$", EXPECTED.read_text(), flags=re.MULTILINE
    ):
        if int(index) != len(expected) + 1:
            raise SystemExit("REFUSE_EXPECTED_GH_INDEX")
        expected.append(body)
    if len(expected) != 35 or expected[-2:] != ["la^20", "s"]:
        raise SystemExit("REFUSE_EXPECTED_GH_SHAPE")
    return polynomials, expected


def source(
    tag: str,
    order: str,
    label: str,
    polynomials: dict[str, str],
    expected: list[str],
) -> str:
    lines = [
        "// Corrected direct-saturation A from pinned expanded B polynomials.",
        'LIB "elim.lib";',
        f"ring R=0,(s,la,tau,rho,q1,q0,r2,r1,r0),{order};",
        "option(redSB);",
    ]
    for name in POLYS:
        lines.append(f"poly {name}={polynomials[name]};")
    lines.extend(
        [
            f'print("AWS_TAG={tag}");',
            f'print("ENCODING=CORRECTED_A_EXPANDED_DIRECT_SAT_{label}");',
            "ideal I=E1,E2,E3,E4,E5,E6,E7,E8,LT;",
            "ideal CS=s;",
            "ideal C=sat(I,CS);",
            'print("A_CONTRACTION_GENERATORS="+string(size(C)));',
            "ideal H=C,s;",
            "ideal GH=std(H);",
            'print("A_SPECIAL_FIBRE_GENERATORS="+string(size(GH)));',
            'print("FULL_SPECIAL_FIBRE_BASIS_BEGIN");',
            "GH;",
            'print("FULL_SPECIAL_FIBRE_BASIS_END");',
            "ideal EXPECTED=" + ",".join(expected) + ";",
            "ideal GE=std(EXPECTED);",
            "int i;",
            "for (i=1; i<=size(GH); i++)",
            "{",
            '  if (reduce(GH[i],GE)!=0) { print("FAIL_GH_NOT_IN_B"); quit; }',
            "}",
            "for (i=1; i<=size(GE); i++)",
            "{",
            '  if (reduce(GE[i],GH)!=0) { print("FAIL_B_NOT_IN_GH"); quit; }',
            "}",
            'print("PASS_A_B_SPECIAL_FIBRE_MUTUAL_REDUCTION");',
            'if (reduce(la^20,GH)!=0) { print("FAIL_LA20_MEMBERSHIP"); quit; }',
            'print("LA20_IN_FULL_SPECIAL_FIBRE=1");',
            "poly TORUS=la*tau*rho*q1*q0*r2*r1*r0;",
            'if (reduce(TORUS,GH)!=0) { print("FAIL_TORUS_MEMBERSHIP"); quit; }',
            'print("TORUS_IN_FULL_SPECIAL_FIBRE=1");',
            "ideal CT=TORUS;",
            "list SX=sat_with_exp(GH,CT);",
            "ideal GSX=std(SX[1]);",
            'print("TORUS_SATURATION_EXPONENT="+string(SX[2]));',
            'if (SX[2]!=1 || reduce(1,GSX)!=0) { print("FAIL_TORUS_SATURATION"); quit; }',
            "ideal GHT=std(sat(GH,CT));",
            'if (reduce(1,GHT)!=0) { print("FAIL_TORUS_UNIT"); quit; }',
            'print("TORUS_SPECIAL_FIBRE_IS_UNIT=1");',
            "ideal P=GHT,la-1,tau-1,rho-1,q1-1,q0+1,r2-1,r1-1,r0+2;",
            "ideal GP=std(P);",
            'if (reduce(1,GP)!=0) { print("FAIL_RESIDUE_UNIT"); quit; }',
            'print("RESIDUE_IDEAL_IS_UNIT=1");',
            'print("CONTROL2_REES_RESIDUE_SURVIVES=0");',
            'print("FIREWALL=FROZEN_EXPANDED_SOURCE_FIXED_AXIS_LOAD_SUPPORT_WEIGHT_ONLY");',
            f'print("PASS_CONTROL2_REES_CORRECTED_A_{label}");',
            "quit;",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    tag = require_aws()
    polynomials, expected = load_inputs()
    outputs = {
        "corrected_A_lpdp.sing": source(
            tag, "(lp(1),dp(8))", "LPDP", polynomials, expected
        ),
        "corrected_A_dp.sing": source(tag, "dp", "DP", polynomials, expected),
    }
    for name, text in outputs.items():
        path = HERE / name
        path.write_text(text)
        print(f"{name}_sha256={sha256(path.read_bytes()).hexdigest()}")
    print(f"base_B_sha256={BASE_SHA}")
    print(f"expected_B_certificate_sha256={EXPECTED_SHA}")
    print("expected_B_GH_generators=35")
    print("PASS_CONTROL2_REES_CORRECTED_A_COMPILER")


if __name__ == "__main__":
    main()
