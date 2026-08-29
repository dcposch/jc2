#!/usr/bin/env python3
"""Compile the corrected complete-source D1 a=9 D(k60) obstruction; AWS only."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V3_DIR = ROOT / "cases/max12_812_order2_square_owner_d1_a9_source_support_census_v3_parenthesized_loads_20260826"
V3 = V3_DIR / "compile_v3_parenthesized_loads.py"
PINS = {
    V3: "0f7b9482f214347858f61181119f52fc434de8223ae7a3c4099049bd737897ef",
    V3_DIR / "REGISTRATION.md": "a88cc145baaa6612b73e0d44df0e012fcc99d531d50bbe8879a081449eb51b3b",
    V3_DIR / "RESULT.md": "88609fdfc50b89625f79e7dcee3b8ceb47d61c3b6668e86ee80da67ad4129e24",
    V3_DIR / "FREEZE.sha256": "7016cdba48152e5e44b285a56812f2b2e077f110cc6e5baa5adbbe9d184d2432",
    V3_DIR / "EVIDENCE.sha256": "d2e5d59f94d3489fd8bd3509fd0ece0dc2456c234173f5023ebad2f201bb3c06",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only D1 a9 k60-unit compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only D1 a9 k60-unit compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_v3():
    spec = importlib.util.spec_from_file_location("a9_k60_parent_v3", V3)
    if spec is None or spec.loader is None:
        fail("cannot import frozen V3 compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    for source, expected in PINS.items():
        actual = digest(source)
        if actual != expected:
            fail(("frozen V3 ancestry mismatch", str(source), actual, expected))

    output = args.output.resolve()
    if output.exists():
        fail("D1 a9 k60-unit output already exists")
    v3 = load_v3()
    old_argv = sys.argv
    try:
        sys.argv = [str(V3), str(output), "--characteristic", str(args.characteristic)]
        v3.main()
    finally:
        sys.argv = old_argv

    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    parent = output / f"square_d1_a9_recursive_source_grades_v3_{label}.sing"
    text = parent.read_text()
    terminal_fragments = {
        "mu2": "-sigma^28*(mu20+sigma^1*mu20_1+sigma^2*mu20_2+sigma^3*mu20_3)",
        "mu4": "-sigma^32*(mu4)",
        "mu6": "-sigma^36*(mu6)",
        "J": "-sigma^38*(J/4)",
    }
    terminal_counts = {}
    for name, fragment in terminal_fragments.items():
        count = text.count(fragment)
        terminal_counts[name] = count
        if count != 1:
            fail(("literal target retention count", name, count, fragment))

    anchor = (
        'print("A9V2_RECURSIVE_SOURCE_CENSUS_ENDPOINT=PASS_NAVIGATION_ONLY");\n'
        "quit;\n"
    )
    if not text.endswith(anchor) or text.count(anchor) != 1:
        fail("frozen V3 terminal anchor mismatch")
    checks = r'''print("D1A9_K60_PARENT_V3_REPLAY=1");
int D1A9_grade27=(
  A9V2_g27_1-(3/4)*c1*k60==0 &&
  A9V2_g27_2-(3/4)*c0*k60==0 &&
  A9V2_g27_3+(3/16)*p*c1*k60==0 &&
  A9V2_g27_4==0 &&
  A9V2_g27_5+(3/128)*p^2*c1*k60==0 &&
  A9V2_g27_6==0 &&
  A9V2_g27_7+(3/512)*p^3*c1*k60==0
);
int D1A9_moving28=(
  A9V2_g28_1-(3/4)*c1_1*k60-(3/4)*c1*k60_1==0 &&
  A9V2_g28_2-(3/4)*c0_1*k60-(3/4)*c0*k60_1+mu20==0 &&
  A9V2_g28_3+(3/8)*ell1*c1*k60+(3/16)*p*c1_1*k60+(3/16)*p*c1*k60_1==0
);
int D1A9_delayed_loads=(
  diff(A9V2_g31_1,k20)-(1/2)*b1==0 &&
  diff(A9V2_g31_1,k0_1)-(5/8)*c0*b1-(5/8)*c1*b0==0 &&
  diff(A9V2_g31_1,k60_4)-(3/4)*c1==0
);
int D1A9_targets=(
  diff(A9V2_Q0_2,mu20)+sigma^28==0 &&
  diff(A9V2_Q0_4,mu4)+sigma^32==0 &&
  diff(A9V2_Q0_6,mu6)+sigma^36==0 &&
  diff(A9V2_Q0_7,J)+sigma^38/4==0
);
int D1A9_parent_counts=(A9V2_lower_count==0 && A9V2_nonzero_count==27 && A9V2_identities==1);
print("D1A9_K60_GRADE27_IDENTITIES="+string(D1A9_grade27));
print("D1A9_K60_MOVING_CONNECTION_AND_K6JET="+string(D1A9_moving28));
print("D1A9_K60_DELAYED_K2_K10_K6="+string(D1A9_delayed_loads));
print("D1A9_K60_ALL_TARGETS_RETAINED="+string(D1A9_targets));
print("D1A9_K60_PARENT_COUNTS="+string(D1A9_parent_counts));
if (D1A9_grade27*D1A9_moving28*D1A9_delayed_loads*D1A9_targets*D1A9_parent_counts!=1) {
  print("D1A9_K60_FAIL=SOURCE_OR_RETENTION"); quit;
}
'''
    compact = f'''ring D1A9K60={args.characteristic},(z,p,k0,k60,c1,c0,ip,ik0,ik60,u1,u0),dp;
poly D1A9_h1=(3/4)*c1*k60;
poly D1A9_h2=(3/4)*c0*k60;
ideal D1A9_force=std(ideal(D1A9_h1,D1A9_h2,ik60*k60-1));
int D1A9_forces_c_zero=(reduce(c1,D1A9_force)==0 && reduce(c0,D1A9_force)==0);
ideal D1A9_contact=std(ideal(
  D1A9_h1,D1A9_h2,
  ip*p-1,ik0*k0-1,ik60*k60-1,
  u1*c1+u0*c0-1
));
int D1A9_contact_empty=(reduce(1,D1A9_contact)==0);
poly D1A9_Qpell=z^4-1;
poly D1A9_Ppell=16*D1A9_Qpell^2+20*D1A9_Qpell+5;
poly D1A9_Apell=16*z^10-20*z^6+5*z^2;
int D1A9_pell_control=(D1A9_Apell^2-D1A9_Qpell*D1A9_Ppell^2-1==0);
print("D1A9_K60_FORCES_C_ZERO="+string(D1A9_forces_c_zero));
print("D1A9_K60_EXACT_CONTACT_AUGMENTED_IDEAL_UNIT="+string(D1A9_contact_empty));
print("D1A9_K60_CHEBYSHEV_PELL_CONTROL="+string(D1A9_pell_control));
if (D1A9_forces_c_zero*D1A9_contact_empty*D1A9_pell_control!=1) {{
  print("D1A9_K60_FAIL=LOCALIZED_OBSTRUCTION_OR_CONTROL"); quit;
}}
print("D1A9_K60_UNIT_GRADE27_ENDPOINT=PASS_EMPTY_EXACT_CONTACT");
quit;
'''
    text = text[: -len(anchor)] + anchor[: -len("quit;\n")] + checks + compact
    target = output / f"square_d1_a9_k60_unit_grade27_{label}.sing"
    parent.rename(target)
    target.write_text(text)

    parent_payload_path = output / "result.json"
    parent_payload = json.loads(parent_payload_path.read_text())
    parent_payload_path.rename(output / "parent_v3_result.json")
    payload = {
        "status": "PASS-D1-A9-K60-UNIT-GRADE27-COMPILER",
        "scope": "FIXED_CONTACT_A9_D_P_K10_K6_ONLY",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "input_sha256": digest(target),
        "parent_v3_input_sha256": parent_payload["input_sha256"],
        "literal_target_counts": terminal_counts,
    }
    parent_payload_path.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print("D1A9_K60_LITERAL_TARGET_MU2_COUNT=1")
    print("D1A9_K60_LITERAL_TARGET_MU4_COUNT=1")
    print("D1A9_K60_LITERAL_TARGET_MU6_COUNT=1")
    print("D1A9_K60_LITERAL_TARGET_J_COUNT=1")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()

