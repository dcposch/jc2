#!/usr/bin/env python3
"""Compile the exact D1 a=9 V(k60) grade-28/29 collision; AWS only."""

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
PARENT_DIR = ROOT / "cases/max12_812_order2_square_owner_d1_a9_k60_unit_grade27_v2_target_precedence_20260826"
PARENT = PARENT_DIR / "compile_v2_target_precedence.py"
PINS = {
    PARENT: "be60b80e2381d2c788fba6cb0517dd8be7d3b1febc9cbd066703d6f7c20857b1",
    PARENT_DIR / "REGISTRATION.md": "748c10651c1bc6072b118478dd12937c686ff2777a507a8414d394f721525727",
    PARENT_DIR / "RESULT.md": "3679d0dbd883c74a4d1d7d1175daf9461c123dd83272bdf2e713ebd7c3412a88",
    PARENT_DIR / "FREEZE.sha256": "be2a611f119900400b7bb5a8c0fc7e9cb66815c8b3c23a70feb565b209092c48",
    PARENT_DIR / "EVIDENCE.sha256": "f878c18a4163e1b94bb150e3a84e626ff3eb9d13382da8d03694b200101c2a0d",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only D1 a9 V(k60) compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only D1 a9 V(k60) compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_parent():
    spec = importlib.util.spec_from_file_location("d1_a9_k60_parent_v2", PARENT)
    if spec is None or spec.loader is None:
        fail("cannot import frozen D(k60) V2 compiler")
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
            fail(("frozen D(k60) ancestry mismatch", str(source), actual, expected))

    output = args.output.resolve()
    if output.exists():
        fail("D1 a9 V(k60) output already exists")
    parent = load_parent()
    old_argv = sys.argv
    try:
        sys.argv = [str(PARENT), str(output), "--characteristic", str(args.characteristic)]
        parent.main()
    finally:
        sys.argv = old_argv

    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    parent_input = output / f"square_d1_a9_k60_unit_grade27_v2_{label}.sing"
    text = parent_input.read_text()
    terminal_fragments = {
        "mu2": "-sigma^28*(mu20+sigma^1*mu20_1+sigma^2*mu20_2+sigma^3*mu20_3)",
        "mu4": "-sigma^32*(mu4)",
        "mu6": "-sigma^36*(mu6)",
        "J": "-sigma^38*(J/4)",
    }
    counts = {name: text.count(fragment) for name, fragment in terminal_fragments.items()}
    if counts != {"mu2": 1, "mu4": 1, "mu6": 1, "J": 1}:
        fail(("terminal target retention mismatch", counts))
    anchor = 'print("D1A9_K60_UNIT_GRADE27_ENDPOINT=PASS_EMPTY_EXACT_CONTACT");\nquit;\n'
    if not text.endswith(anchor) or text.count(anchor) != 1:
        fail("frozen parent terminal anchor mismatch")

    collision = f'''setring R;
print("D1A9_VK60_PARENT_V2_REPLAY=1");
poly D1A9V_e28z=subst(A9V2_g28_1,k60,0);
poly D1A9V_e28c=subst(A9V2_g28_2,k60,0);
poly D1A9V_e29z=subst(A9V2_g29_1,k60,0);
poly D1A9V_e29c=subst(A9V2_g29_2,k60,0);
int D1A9V_leaders=(
  D1A9V_e28z-(3/4)*c1*k60_1==0 &&
  D1A9V_e28c-(3/4)*c0*k60_1+mu20==0 &&
  D1A9V_e29z-(3/4)*(a0*c1+a1*c0+c1_1*k60_1+c1*k60_2)==0 &&
  D1A9V_e29c+(3/8)*p*a1*c1-(3/4)*a0*c0-(3/4)*c0_1*k60_1-(3/4)*c0*k60_2+mu20_1==0
);
int D1A9V_grade28=(
  subst(A9V2_g28_3,k60,0)+(p/4)*D1A9V_e28z==0 &&
  subst(A9V2_g28_4,k60,0)==0 &&
  subst(A9V2_g28_5,k60,0)+(p^2/32)*D1A9V_e28z==0 &&
  subst(A9V2_g28_6,k60,0)==0 &&
  subst(A9V2_g28_7,k60,0)+(p^3/128)*D1A9V_e28z==0
);
int D1A9V_moving29=(
  subst(A9V2_g29_3,k60,0)+(p/4)*D1A9V_e29z+(ell1/2)*D1A9V_e28z==0 &&
  subst(A9V2_g29_4,k60,0)==0 &&
  subst(A9V2_g29_5,k60,0)+(p^2/32)*D1A9V_e29z+(p*ell1/8)*D1A9V_e28z==0 &&
  subst(A9V2_g29_6,k60,0)==0 &&
  subst(A9V2_g29_7,k60,0)+(p^3/128)*D1A9V_e29z+(3*p^2*ell1/64)*D1A9V_e28z==0
);
ideal D1A9V_full=std(ideal(
  k60,
  A9V2_g27_1,A9V2_g27_2,A9V2_g27_3,A9V2_g27_4,A9V2_g27_5,A9V2_g27_6,A9V2_g27_7,
  A9V2_g28_1,A9V2_g28_2,A9V2_g28_3,A9V2_g28_4,A9V2_g28_5,A9V2_g28_6,A9V2_g28_7,
  A9V2_g29_1,A9V2_g29_2,A9V2_g29_3,A9V2_g29_4,A9V2_g29_5,A9V2_g29_6,A9V2_g29_7
));
ideal D1A9V_compact=std(ideal(k60,D1A9V_e28z,D1A9V_e28c,D1A9V_e29z,D1A9V_e29c));
int D1A9V_equal=1;
for (int D1A9V_i=1;D1A9V_i<=size(D1A9V_full);D1A9V_i++) {{
  if (reduce(D1A9V_full[D1A9V_i],D1A9V_compact)!=0) {{ D1A9V_equal=0; }}
}}
for (D1A9V_i=1;D1A9V_i<=size(D1A9V_compact);D1A9V_i++) {{
  if (reduce(D1A9V_compact[D1A9V_i],D1A9V_full)!=0) {{ D1A9V_equal=0; }}
}}
int D1A9V_higher=(
  diff(D1A9V_e29z,a0)-(3/4)*c1==0 &&
  diff(D1A9V_e29z,a1)-(3/4)*c0==0 &&
  diff(D1A9V_e29z,c1_1)-(3/4)*k60_1==0 &&
  diff(D1A9V_e29z,k60_2)-(3/4)*c1==0 &&
  diff(D1A9V_e29c,c0_1)-(3/4)*k60_1==0 &&
  diff(D1A9V_e29c,k60_2)-(3/4)*c0==0
);
int D1A9V_delayed=(
  diff(A9V2_g31_1,k20)-(1/2)*b1==0 &&
  diff(A9V2_g31_1,k0_1)-(5/8)*c0*b1-(5/8)*c1*b0==0 &&
  diff(A9V2_g31_1,k60_4)-(3/4)*c1==0
);
int D1A9V_targets=(
  diff(A9V2_Q0_2,mu20)+sigma^28==0 &&
  diff(A9V2_Q0_4,mu4)+sigma^32==0 &&
  diff(A9V2_Q0_6,mu6)+sigma^36==0 &&
  diff(A9V2_Q0_7,J)+(sigma^38)/4==0
);
print("D1A9_VK60_GRADE28_LEADERS="+string(D1A9V_leaders));
print("D1A9_VK60_GRADE28_DENOMINATOR_ROWS="+string(D1A9V_grade28));
print("D1A9_VK60_GRADE29_MOVING_CONNECTION="+string(D1A9V_moving29));
print("D1A9_VK60_FULL_COMPACT_IDEAL_EQUALITY="+string(D1A9V_equal));
print("D1A9_VK60_HIGHER_NORMAL_CORRECTIONS="+string(D1A9V_higher));
print("D1A9_VK60_DELAYED_LOADS_RETAINED="+string(D1A9V_delayed));
print("D1A9_VK60_TERMINAL_TARGETS_RETAINED="+string(D1A9V_targets));
if (D1A9V_leaders*D1A9V_grade28*D1A9V_moving29*D1A9V_equal*D1A9V_higher*D1A9V_delayed*D1A9V_targets!=1) {{
  print("D1A9_VK60_FAIL=SOURCE_COLLISION_OR_CUSTODY"); quit;
}}

ring D1A9V60={args.characteristic},(p,k0,k61,k62,mu,mu1,a1,a0,c1,c0,c11,c01,ip,ik0,ik61,ua1,ua0,uc1,uc0),dp;
poly D1A9V60_e1=(3/4)*c1*k61;
poly D1A9V60_e2=(3/4)*c0*k61-mu;
poly D1A9V60_e3=(3/4)*(a0*c1+a1*c0+c11*k61+c1*k62);
poly D1A9V60_e4=-(3/8)*p*a1*c1+(3/4)*a0*c0+(3/4)*c01*k61+(3/4)*c0*k62-mu1;
poly D1A9V60_popen=ip*p-1;
poly D1A9V60_k0open=ik0*k0-1;
poly D1A9V60_aopen=ua1*a1+ua0*a0-1;
poly D1A9V60_copen=uc1*c1+uc0*c0-1;
ideal D1A9V60_D=std(ideal(
  D1A9V60_e1,D1A9V60_e2,D1A9V60_e3,D1A9V60_e4,
  D1A9V60_popen,D1A9V60_k0open,ik61*k61-1,D1A9V60_aopen,D1A9V60_copen
));
ideal D1A9V60_WD=std(ideal(
  p-1,k0-1,k61-1,k62,mu-(3/4),mu1,a1-1,a0,c1,c0-1,c11+1,c01,
  ip-1,ik0-1,ik61-1,ua1-1,ua0,uc1,uc0-1
));
int D1A9V60_Dproper=(reduce(1,D1A9V60_D)!=0);
int D1A9V60_Dwitness=(reduce(1,D1A9V60_WD)!=0);
for (int D1A9V60_i=1;D1A9V60_i<=size(D1A9V60_D);D1A9V60_i++) {{
  if (reduce(D1A9V60_D[D1A9V60_i],D1A9V60_WD)!=0) {{ D1A9V60_Dwitness=0; }}
}}
int D1A9V60_Drelations=(
  reduce(c1,D1A9V60_D)==0 &&
  reduce(mu-(3/4)*c0*k61,D1A9V60_D)==0 &&
  reduce(uc0*c0-1,D1A9V60_D)==0
);

ideal D1A9V60_V=std(ideal(
  D1A9V60_e1,D1A9V60_e2,D1A9V60_e3,D1A9V60_e4,k61,
  D1A9V60_popen,D1A9V60_k0open,D1A9V60_aopen,D1A9V60_copen
));
ideal D1A9V60_WV=std(ideal(
  p-1,k0-1,k61,k62+1,mu,mu1,a1,a0-1,c1-1,c0,c11,c01,
  ip-1,ik0-1,ik61,ua1,ua0-1,uc1-1,uc0
));
int D1A9V60_Vproper=(reduce(1,D1A9V60_V)!=0);
int D1A9V60_Vwitness=(reduce(1,D1A9V60_WV)!=0);
for (D1A9V60_i=1;D1A9V60_i<=size(D1A9V60_V);D1A9V60_i++) {{
  if (reduce(D1A9V60_V[D1A9V60_i],D1A9V60_WV)!=0) {{ D1A9V60_Vwitness=0; }}
}}
int D1A9V60_Vrelations=(reduce(mu,D1A9V60_V)==0);

poly D1A9V60_Qpell=z^4-1;
poly D1A9V60_Ppell=16*D1A9V60_Qpell^2+20*D1A9V60_Qpell+5;
poly D1A9V60_Apell=16*z^10-20*z^6+5*z^2;
int D1A9V60_pell=(D1A9V60_Apell^2-D1A9V60_Qpell*D1A9V60_Ppell^2-1==0);
print("D1A9_VK60_DK601_PROPER="+string(D1A9V60_Dproper));
print("D1A9_VK60_DK601_WITNESS="+string(D1A9V60_Dwitness));
print("D1A9_VK60_DK601_RELATIONS="+string(D1A9V60_Drelations));
print("D1A9_VK60_VK601_PROPER="+string(D1A9V60_Vproper));
print("D1A9_VK60_VK601_WITNESS="+string(D1A9V60_Vwitness));
print("D1A9_VK60_VK601_RELATIONS="+string(D1A9V60_Vrelations));
print("D1A9_VK60_CHEBYSHEV_PELL_CONTROL="+string(D1A9V60_pell));
if (D1A9V60_Dproper*D1A9V60_Dwitness*D1A9V60_Drelations*D1A9V60_Vproper*D1A9V60_Vwitness*D1A9V60_Vrelations*D1A9V60_pell!=1) {{
  print("D1A9_VK60_FAIL=STRATUM_OR_CONTROL"); quit;
}}
print("D1A9_VK60_GRADE28_29_ENDPOINT=PASS_TWO_NONEMPTY_STRATA_ROUTE_GRADE30");
quit;
'''
    text = text[: -len(anchor)] + anchor[: -len("quit;\n")] + collision
    target = output / f"square_d1_a9_k60_zero_grade28_29_{label}.sing"
    parent_input.rename(target)
    target.write_text(text)

    parent_payload_path = output / "result.json"
    parent_payload = json.loads(parent_payload_path.read_text())
    parent_payload_path.rename(output / "parent_v2_result.json")
    payload = {
        "status": "PASS-D1-A9-VK60-GRADE28-29-COLLISION-COMPILER",
        "scope": "FIXED_CONTACT_A9_V_K60_D_P_K10_GRADE28_29_ONLY",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "input_sha256": digest(target),
        "parent_v2_input_sha256": parent_payload["input_sha256"],
        "terminal_target_counts": counts,
    }
    parent_payload_path.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print("D1A9_VK60_LITERAL_TARGET_MU2_COUNT=1")
    print("D1A9_VK60_LITERAL_TARGET_MU4_COUNT=1")
    print("D1A9_VK60_LITERAL_TARGET_MU6_COUNT=1")
    print("D1A9_VK60_LITERAL_TARGET_J_COUNT=1")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()

