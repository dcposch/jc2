#!/usr/bin/env python3
"""Compile the uniform D1 a>=13 grade-38 J recurrence; AWS only."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PARENT_DIR = ROOT / "cases/max12_812_order2_square_owner_d1_highcontact_c2_target_shadow_20260826"
PARENT = PARENT_DIR / "compile_highcontact_c2_shadow.py"
PINS = {
    PARENT: "c6eeb50e25cd814855785203165a06da39404c792698e22992efef954c79855c",
    PARENT_DIR / "REGISTRATION.md": "38f912f271f5cb07d4eaa7c871f4515be19b2918ca01bf5bb751522110cdc1c7",
    PARENT_DIR / "FREEZE.sha256": "fa3d24f86bc208a909f15b161f6a6a1fab4450c9304c8b2950fdf90dc84a95f3",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only a>=13 J38 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only a>=13 J38 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_parent():
    spec = importlib.util.spec_from_file_location("d1_j38_parent", PARENT)
    if spec is None or spec.loader is None:
        fail("cannot import frozen high-contact parent")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build_rows(parent, a: int, symbolic_raise: bool, source_base, tail_base, tails):
    maximum = 38
    p_index = maximum - 28
    c_index = maximum - (18 + a)
    r_index = max(maximum - (22 + a), 1)
    a_index = max(maximum - (25 + a), 1)
    k2_index = max(r_index, 1)
    variables = ["z", "sigma", "p"]
    variables += [f"ell{index}" for index in range(1, p_index + 1)]
    if symbolic_raise:
        variables += ["theta", "eta"]
    for stem in ("a1", "a0"):
        variables += parent.jet_names(stem, a_index)
    for stem in ("c1", "c0"):
        variables += parent.jet_names(stem, c_index)
    for stem in ("b1", "b0"):
        variables += parent.jet_names(stem, r_index)
    variables += parent.jet_names("k0", 1)
    variables += parent.jet_names("k60", c_index)
    variables += parent.jet_names("k20", k2_index)
    variables += parent.jet_names("mu20", maximum - 28)
    variables += parent.jet_names("mu4", maximum - 32)
    variables += parent.jet_names("mu6", maximum - 36)
    variables += ["J", "iJ"]

    pp = "p" + "".join(f"+2*sigma^{index}*ell{index}" for index in range(1, p_index + 1))
    theta = "theta" if symbolic_raise else "1"
    eta = "eta" if symbolic_raise else "1"
    az = f"sigma^{a}*{theta}*({parent.series('a1', a_index)})"
    ac = f"sigma^{a}*{theta}*({parent.series('a0', a_index)})"
    cz = f"sigma^{a + 1}*{theta}*({parent.series('c1', c_index)})"
    cc = f"sigma^{a + 1}*{theta}*({parent.series('c0', c_index)})"
    rz = f"sigma^{a}*{theta}*{eta}*({parent.series('b1', r_index)})"
    rc = f"sigma^{a}*{theta}*{eta}*({parent.series('b0', r_index)})"
    coeffs = source_base.source_coefficients(pp, az, ac, cz, cc, rz, rc)
    loads = {
        "k10": f"({parent.series('k0', 1)})",
        "k6": f"({parent.series('k60', c_index)})",
        "k2": f"({parent.series('k20', k2_index)})",
    }
    targets = {
        1: "0",
        2: parent.series("mu20", maximum - 28),
        3: "0",
        4: parent.series("mu4", maximum - 32),
        5: "0",
        6: parent.series("mu6", maximum - 36),
        7: "J/4",
    }
    rows = {
        row: parent.source_row(tail_base, tails, row, coeffs, loads, targets)
        for row in range(1, 8)
    }
    return variables, pp, rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    for source, expected in PINS.items():
        actual = digest(source)
        if actual != expected:
            fail(("frozen high-contact parent mismatch", str(source), actual, expected))
    parent = load_parent()
    source_base, tail_base, tails = parent.ancestry()
    output = args.output.resolve()
    if output.exists():
        fail("a>=13 J38 output already exists")
    output.mkdir(parents=True)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    target = output / f"square_d1_age13_j38_odd_recurrence_{label}.sing"

    variables13, pp13, rows13 = build_rows(parent, 13, True, source_base, tail_base, tails)
    lines = [
        f"ring R13={args.characteristic},({','.join(variables13)}),dp;",
        'print("D1J38_SOURCE_HASHES=PASS");',
    ]
    for row in range(1, 8):
        lines.append(f"poly J38_Phi{row}={rows13[row]};")
    lines += [
        "ideal J38_S38=std(ideal(sigma^38)); ideal J38_S39=std(ideal(sigma^39));",
        f"poly J38_rel=J38_Phi7-(({pp13})/4)*J38_Phi5-((({pp13})^2)/32)*J38_Phi3-((({pp13})^3)/128)*J38_Phi1;",
        "int J38_div38=(reduce(J38_rel,J38_S38)==0);",
        "poly J38_q38=J38_rel/sigma^38;",
        "int J38_coeff=(subst(J38_q38,sigma,0)+J/4==0);",
        "int J38_mod39=(reduce(J38_rel+(sigma^38)*J/4,J38_S39)==0);",
        "ideal J38_unit=std(ideal(subst(J38_q38,sigma,0),iJ*J-1));",
        "int J38_exact_unit=(reduce(1,J38_unit)==0);",
        "int J38_symbolic=(diff(J38_rel+(sigma^38)*J/4,theta)!=0 || diff(J38_rel+(sigma^38)*J/4,eta)!=0);",
        "int J38_symbolic_safe=(reduce(diff(J38_rel+(sigma^38)*J/4,theta),J38_S39)==0 && reduce(diff(J38_rel+(sigma^38)*J/4,eta),J38_S39)==0);",
        'print("D1J38_ODD_RECURRENCE_DIVISIBLE_G38="+string(J38_div38));',
        'print("D1J38_GRADE38_COEFFICIENT_MINUS_J_OVER_4="+string(J38_coeff));',
        'print("D1J38_RECURRENCE_MOD_G39="+string(J38_mod39));',
        'print("D1J38_EXACT_J_CONTACT_UNIT="+string(J38_exact_unit));',
        'print("D1J38_SYMBOLIC_THETA_ETA_SAFE="+string(J38_symbolic_safe));',
        "if (J38_div38*J38_coeff*J38_mod39*J38_exact_unit*J38_symbolic_safe!=1) { print(\"D1J38_FAIL=A13_RECURRENCE_OR_UNIT\"); quit; }",
    ]

    variables12, pp12, rows12 = build_rows(parent, 12, False, source_base, tail_base, tails)
    lines.append(f"ring R12={args.characteristic},({','.join(variables12)}),dp;")
    for row in range(1, 8):
        lines.append(f"poly J38N_Phi{row}={rows12[row]};")
    lines += [
        "ideal J38N_S38=std(ideal(sigma^38));",
        f"poly J38N_rel=J38N_Phi7-(({pp12})/4)*J38N_Phi5-((({pp12})^2)/32)*J38N_Phi3-((({pp12})^3)/128)*J38N_Phi1+(sigma^38)*J/4;",
        "int J38N_div38=(reduce(J38N_rel,J38N_S38)==0);",
        "poly J38N_q38=J38N_rel/sigma^38;",
        "poly J38N_coeff=subst(J38N_q38,sigma,0);",
        "int J38N_sharp=(J38N_coeff!=0 && diff(J38N_coeff,k20)!=0);",
        'print("D1J38_A12_NEGCTRL_DIVISIBLE_G38="+string(J38N_div38));',
        'print("D1J38_A12_K2C_TRIPLE_POLE_BREAKS="+string(J38N_sharp));',
        "if (J38N_div38*J38N_sharp!=1) { print(\"D1J38_FAIL=A12_SHARPNESS_CONTROL\"); quit; }",
        "poly J38_Qpell=z^4-1;",
        "poly J38_Ppell=16*J38_Qpell^2+20*J38_Qpell+5;",
        "poly J38_Apell=16*z^10-20*z^6+5*z^2;",
        "int J38_pell=(J38_Apell^2-J38_Qpell*J38_Ppell^2-1==0);",
        'print("D1J38_CHEBYSHEV_PELL_CONTROL="+string(J38_pell));',
        "if (J38_pell!=1) { print(\"D1J38_FAIL=PELL_CONTROL\"); quit; }",
        'print("D1J38_ENDPOINT=PASS_EMPTY_UNIFORM_A_GE_13");',
        "quit;",
    ]
    target.write_text("\n".join(lines) + "\n")
    payload = {
        "status": "PASS-D1-AGE13-J38-ODD-RECURRENCE-COMPILER",
        "scope": "UNIFORM_A_GE_13_C_EQ_A_PLUS_1_R_GE_A_D_J_LITERAL_SOURCE_ONLY",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "input_sha256": digest(target),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()

