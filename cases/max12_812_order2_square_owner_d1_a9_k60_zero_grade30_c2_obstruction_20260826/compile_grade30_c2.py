#!/usr/bin/env python3
"""Compile the exact D1 a9 V(k60) grade-30 C^2 obstruction; AWS only."""

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
PARENT_DIR = ROOT / "cases/max12_812_order2_square_owner_d1_a9_k60_zero_grade28_29_collision_v2_syntax_20260826"
PARENT = PARENT_DIR / "compile_v2_syntax.py"
PINS = {
    PARENT: "2aab56504850cb0f6e60697c59999c43a62a75b5930ba1b4b27dbf80ec5334cd",
    PARENT_DIR / "REGISTRATION.md": "f4147f7127bfc52920309222e543a11b7ce3667b29b91d9756738b0e225024b4",
    PARENT_DIR / "FREEZE.sha256": "e4625f8e09e1ffa09cc3267798e19b8333d9c16d7b1b9530f141b094540f64ca",
    PARENT_DIR / "RESULT.md": "eb1b77e1731e438e732ac5f704a99d63f95f10a172855d0e5c2ca67eb39e9f47",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only D1 a9 grade30 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only D1 a9 grade30 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_parent():
    spec = importlib.util.spec_from_file_location("d1_a9_vk60_collision_v2", PARENT)
    if spec is None or spec.loader is None:
        fail("cannot import frozen collision V2 compiler")
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
            fail(("frozen collision V2 ancestry mismatch", str(source), actual, expected))

    output = args.output.resolve()
    if output.exists():
        fail("D1 a9 grade30 output already exists")
    parent = load_parent()
    old_argv = sys.argv
    try:
        sys.argv = [str(PARENT), str(output), "--characteristic", str(args.characteristic)]
        parent.main()
    finally:
        sys.argv = old_argv

    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    parent_input = output / f"square_d1_a9_k60_zero_grade28_29_v2_{label}.sing"
    text = parent_input.read_text()
    anchor = 'print("D1A9_VK60_GRADE28_29_ENDPOINT=PASS_TWO_NONEMPTY_STRATA_ROUTE_GRADE30");\nquit;\n'
    if not text.endswith(anchor) or text.count(anchor) != 1:
        fail("frozen collision V2 terminal anchor mismatch")

    checks = f'''setring R;
print("D1A9_G30_PARENT_COLLISION_V2_REPLAY=1");
poly D1A9G30_e29z=subst(subst(A9V2_g29_1,k60,0),k60_1,0);
poly D1A9G30_e29c=subst(subst(A9V2_g29_2,k60,0),k60_1,0);
poly D1A9G30_g1=subst(subst(A9V2_g30_1,k60,0),k60_1,0);
poly D1A9G30_g2=subst(subst(A9V2_g30_2,k60,0),k60_1,0);
poly D1A9G30_g3=subst(subst(A9V2_g30_3,k60,0),k60_1,0);
poly D1A9G30_g4=subst(subst(A9V2_g30_4,k60,0),k60_1,0);
poly D1A9G30_g5=subst(subst(A9V2_g30_5,k60,0),k60_1,0);
poly D1A9G30_g6=subst(subst(A9V2_g30_6,k60,0),k60_1,0);
poly D1A9G30_g7=subst(subst(A9V2_g30_7,k60,0),k60_1,0);
int D1A9G30_invariant=(
  D1A9G30_g3+(p/4)*D1A9G30_g1+(ell1/2)*D1A9G30_e29z-(3/4)*c1*c0==0 &&
  D1A9G30_g4-(3/16)*(2*c0^2-p*c1^2)==0 &&
  D1A9G30_g5+((p^2)/32)*D1A9G30_g1+(p*ell1/8)*D1A9G30_e29z+(3/16)*p*c1*c0==0 &&
  D1A9G30_g6==0 &&
  D1A9G30_g7+((p^3)/128)*D1A9G30_g1+(3*(p^2)*ell1/64)*D1A9G30_e29z+(3*(p^2)/128)*c1*c0==0
);
ideal D1A9G30_full=std(ideal(
  k60,k60_1,
  A9V2_g27_1,A9V2_g27_2,A9V2_g27_3,A9V2_g27_4,A9V2_g27_5,A9V2_g27_6,A9V2_g27_7,
  A9V2_g28_1,A9V2_g28_2,A9V2_g28_3,A9V2_g28_4,A9V2_g28_5,A9V2_g28_6,A9V2_g28_7,
  A9V2_g29_1,A9V2_g29_2,A9V2_g29_3,A9V2_g29_4,A9V2_g29_5,A9V2_g29_6,A9V2_g29_7,
  A9V2_g30_1,A9V2_g30_2,A9V2_g30_3,A9V2_g30_4,A9V2_g30_5,A9V2_g30_6,A9V2_g30_7
));
ideal D1A9G30_compact=std(ideal(
  k60,k60_1,mu20,D1A9G30_e29z,D1A9G30_e29c,D1A9G30_g1,D1A9G30_g2,
  c1*c0,2*c0^2-p*c1^2
));
int D1A9G30_equal=1;
for (int D1A9G30_i=1;D1A9G30_i<=size(D1A9G30_full);D1A9G30_i++) {{
  if (reduce(D1A9G30_full[D1A9G30_i],D1A9G30_compact)!=0) {{ D1A9G30_equal=0; }}
}}
for (D1A9G30_i=1;D1A9G30_i<=size(D1A9G30_compact);D1A9G30_i++) {{
  if (reduce(D1A9G30_compact[D1A9G30_i],D1A9G30_full)!=0) {{ D1A9G30_equal=0; }}
}}
int D1A9G30_custody=(
  diff(A9V2_g31_1,k20)-(1/2)*b1==0 &&
  diff(A9V2_g31_1,k0_1)-(5/8)*c0*b1-(5/8)*c1*b0==0 &&
  diff(A9V2_g31_1,k60_4)-(3/4)*c1==0 &&
  diff(A9V2_Q0_4,mu4)+sigma^32==0 &&
  diff(A9V2_Q0_6,mu6)+sigma^36==0 &&
  diff(A9V2_Q0_7,J)+(sigma^38)/4==0
);
print("D1A9_G30_C2_HAND_INVARIANT="+string(D1A9G30_invariant));
print("D1A9_G30_FULL_COMPACT_IDEAL_EQUALITY="+string(D1A9G30_equal));
print("D1A9_G30_DELAYED_AND_TERMINAL_CUSTODY="+string(D1A9G30_custody));
if (D1A9G30_invariant*D1A9G30_equal*D1A9G30_custody!=1) {{
  print("D1A9_G30_FAIL=SOURCE_INVARIANT_OR_CUSTODY"); quit;
}}

ring D1A9G30C={args.characteristic},(z,p,k0,k61,c1,c0,ip,ik0,ik61,u1,u0),dp;
poly D1A9G30C_q=2*c0^2-p*c1^2;
poly D1A9G30C_contact=u1*c1+u0*c0-1;
ideal D1A9G30C_Dcore=std(ideal(c1*k61,D1A9G30C_q,ip*p-1,ik0*k0-1,ik61*k61-1));
int D1A9G30C_Drelations=(reduce(c1,D1A9G30C_Dcore)==0 && reduce(c0^2,D1A9G30C_Dcore)==0);
ideal D1A9G30C_D=std(ideal(c1*k61,D1A9G30C_q,ip*p-1,ik0*k0-1,ik61*k61-1,D1A9G30C_contact));
int D1A9G30C_Dunit=(reduce(1,D1A9G30C_D)==0);

ideal D1A9G30C_Vcore=std(ideal(k61,c1*c0,D1A9G30C_q,ip*p-1,ik0*k0-1));
int D1A9G30C_Vnil=(reduce(c0^3,D1A9G30C_Vcore)==0 && reduce(c1^3,D1A9G30C_Vcore)==0);
ideal D1A9G30C_V=std(ideal(k61,c1*c0,D1A9G30C_q,ip*p-1,ik0*k0-1,D1A9G30C_contact));
int D1A9G30C_Vunit=(reduce(1,D1A9G30C_V)==0);

poly D1A9G30C_Qpell=z^4-1;
poly D1A9G30C_Ppell=16*D1A9G30C_Qpell^2+20*D1A9G30C_Qpell+5;
poly D1A9G30C_Apell=16*z^10-20*z^6+5*z^2;
int D1A9G30C_pell=(D1A9G30C_Apell^2-D1A9G30C_Qpell*D1A9G30C_Ppell^2-1==0);
print("D1A9_G30_DK601_CORE_RELATIONS="+string(D1A9G30C_Drelations));
print("D1A9_G30_DK601_EXACT_CONTACT_UNIT="+string(D1A9G30C_Dunit));
print("D1A9_G30_VK601_CUBIC_NILPOTENCE="+string(D1A9G30C_Vnil));
print("D1A9_G30_VK601_EXACT_CONTACT_UNIT="+string(D1A9G30C_Vunit));
print("D1A9_G30_CHEBYSHEV_PELL_CONTROL="+string(D1A9G30C_pell));
if (D1A9G30C_Drelations*D1A9G30C_Dunit*D1A9G30C_Vnil*D1A9G30C_Vunit*D1A9G30C_pell!=1) {{
  print("D1A9_G30_FAIL=EXACT_CONTACT_OBSTRUCTION_OR_CONTROL"); quit;
}}
print("D1A9_G30_ENDPOINT=PASS_EMPTY_BOTH_K601_STRATA");
quit;
'''
    text = text[: -len(anchor)] + anchor[: -len("quit;\n")] + checks
    target = output / f"square_d1_a9_k60_zero_grade30_c2_{label}.sing"
    parent_input.rename(target)
    target.write_text(text)

    parent_payload_path = output / "result.json"
    parent_payload = json.loads(parent_payload_path.read_text())
    parent_payload_path.rename(output / "parent_collision_v2_result.json")
    payload = {
        "status": "PASS-D1-A9-VK60-GRADE30-C2-COMPILER",
        "scope": "FIXED_CONTACT_A9_V_K60_D_P_K10_GRADE30_ONLY",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "input_sha256": digest(target),
        "parent_collision_v2_input_sha256": parent_payload["input_sha256"],
    }
    parent_payload_path.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()

