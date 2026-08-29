#!/usr/bin/env python3
"""Compile the center-complete formal weighted H3/H5 identity."""

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
LOADED_PATH = ROOT / "cases/max12_812_order2_affine_faber_a_loaded_kernel_sigma45_20260826/compile_loaded_kernel.py"
LOADED_SHA = "a32372ce3fd088be74a3456f63c17bcb880c2eaf32c1856e86eb52d7b15f385a"
ADDENDUM_PATH = ROOT / "xmodel/max12-812-order2-affine-faber-a-universal-h3-h5-composition-design-v2-direct-unit-20260826.md"
ADDENDUM_SHA = "78766c9df5dbf95fad5bdff531657f58cb7445e30575a58a59cec656b00d9a63"
Q6_REVIEW_PATH = ROOT / "xmodel/max12-812-order2-affine-faber-a-loaded-kernel-q6-hostile-review-grok-20260826.md"
Q6_REVIEW_SHA = "06e2709344b47ec09549638a53f193b79ca4f791d40c2c0b9c8c04e0284330be"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only formal-weighted compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only formal-weighted compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_loaded():
    for path, expected in (
        (LOADED_PATH, LOADED_SHA),
        (ADDENDUM_PATH, ADDENDUM_SHA),
        (Q6_REVIEW_PATH, Q6_REVIEW_SHA),
    ):
        if digest(path) != expected:
            fail(f"frozen input mismatch: {path}")
    spec = importlib.util.spec_from_file_location("loaded_kernel", LOADED_PATH)
    if spec is None or spec.loader is None:
        fail("cannot load loaded-kernel compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def emit(path: Path, characteristic: int, base, tails) -> None:
    variables = [
        "satu", "Jt", "mu2t", "K2t", "K6t", "K10t", "S0", "S1", "R0", "R1",
        "Y", "X", "a", "lam", "M", "E", "t", "n0", "n1", "n2", "n3", "qr",
        "qc", "qp", "k2", "k6", "k10",
    ]
    lines = [
        f"ring R={characteristic},({','.join(variables)}),dp;",
        "proc tc(poly P,int n)", "{", "  int i; poly Q=P;",
        "  for (i=1; i<=n; i++) { Q=(Q-subst(Q,t,0))/t; }",
        "  return(subst(Q,t,0));", "}",
        "poly TC=3+5*t+7*t^2+11*t^3+13*t^4+17*t^5+19*t^6+23*t^7+29*t^8+31*t^9+37*t^10+41*t^11+43*t^12+47*t^13+53*t^14+59*t^15+61*t^16+67*t^17+71*t^18+73*t^19+79*t^20+83*t^21+89*t^22+97*t^23+101*t^24+103*t^25+107*t^26+109*t^27+113*t^28+127*t^29+131*t^30+137*t^31+139*t^32+149*t^33+151*t^34+157*t^35+163*t^36+167*t^37+173*t^38+179*t^39+181*t^40+191*t^41+193*t^42+197*t^43+199*t^44+211*t^45;",
        "int tcControl=1; int qi;",
        "intvec tv=3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211;",
        "for (qi=0; qi<=45; qi++) { tcControl=tcControl*(tc(TC,qi)==tv[qi+1]); }",
        'print("A_FWH35_TCOEFF_CONTROL="+string(tcControl));',
    ]
    for ell in range(1, 8):
        lines.append(f"poly T{ell}={base.tail_text(tails[str(ell)])};")
    lines.extend([
        "poly aa=t^5*a; poly BB=4*aa; poly EE=E; poly MM=M; poly NL=t^15*lam;",
        "poly XX=t^6*X; poly YY=t^6*Y;",
        "poly RR1=t^12*R1; poly RR0=t^12*R0; poly SS1=t^12*S1; poly SS0=t^12*S0;",
        "poly QP=EE-6*aa^2;",
        "poly QC=2*aa*(4*aa^2-EE)+XX+RR1;",
        "poly QR=aa^2*(EE-3*aa^2)+RR0-aa*(XX+RR1);",
        "poly N3=NL*MM; poly N2=NL*aa*MM;",
        "poly N1=NL*((EE-5*aa^2)*MM+YY+SS1);",
        "poly N0=NL*(-aa*(EE-3*aa^2)*MM-aa*YY+(MM*XX)/2+SS0-aa*SS1);",
        "poly LK10=t^42*K10t; poly LK6=t^42*K6t; poly LK2=t^42*K2t; poly MU2=t^42*mu2t;",
        "proc source(poly P)", "{",
        " P=subst(P,k10,LK10); P=subst(P,k6,LK6); P=subst(P,k2,LK2);",
        " P=subst(P,qp,QP); P=subst(P,qc,QC); P=subst(P,qr,QR);",
        " P=subst(P,n3,N3); P=subst(P,n2,N2); P=subst(P,n1,N1); P=subst(P,n0,N0); return(P);", "}",
    ])
    for ell in range(1, 8):
        target = "-MU2" if ell == 2 else ""
        lines.append(f"poly P{ell}=source(T{ell}){target};")
    lines.extend([
        "poly H3=P3-(1/2)*BB*P2+((5/32)*BB^2-(1/4)*EE)*P1;",
        "poly H5=P5-BB*P4+((21/32)*BB^2-(3/4)*EE)*P3+(-(5/16)*BB^3+(3/4)*BB*EE)*P2+((195/2048)*BB^4-(45/128)*BB^2*EE+(5/32)*EE^2)*P1;",
        "poly EXPECT3=-(3/8)*t^42*lam^2*M*X*Y-(1/16)*t^45*lam^3*M^3;",
        "poly EXPECT5=(3/8)*t^42*E*lam^2*M*X*Y;",
        "ideal T46=std(ideal(t^46));",
        "int h3Control=(reduce(H3-EXPECT3,T46)==0);",
        "int h5Control=(reduce(H5-EXPECT5,T46)==0);",
        'print("A_FWH35_H3_MOD_T46="+string(h3Control));',
        'print("A_FWH35_H5_MOD_T46="+string(h5Control));',
        "poly K=EE*H3+H5; ideal T45=std(ideal(t^45));",
        "int lowerK=(reduce(K,T45)==0); poly K45=tc(K,45);",
        "int kControl=(16*K45+E*lam^3*M^3==0);",
        'print("A_FWH35_K_LOWER_ZERO="+string(lowerK));',
        'print("A_FWH35_K45="+string(K45));',
        'print("A_FWH35_K45_CERTIFICATE="+string(kControl));',
        "ideal I=K45,satu*E*lam*M*K10t-1; ideal G=std(I);",
        "int unitControl=(reduce(1,G)==0);",
        'print("A_FWH35_UNIT="+string(unitControl));',
        "if (tcControl*h3Control*h5Control*lowerK*kControl*unitControl==1) { print(\"A_FWH35_ENDPOINT=PASS_FORMAL_WEIGHTED_CENTER_COMPLETE_DIRECT_UNIT\"); }",
        'else { print("A_FWH35_ENDPOINT=FAIL_IDENTITY_OR_CONTROL"); quit; }',
        'print("A_FWH35_DONE=1");',
        'print("A_FWH35_SCOPE=FORMAL_WEIGHTED_COMPLETE_TAIL_IDENTITY_Q_GE6_MOVING_CENTER_TANGENTS_COMPLEMENTS_DELAYED_LOAD_NO_Q_LT6_CHART_COVERAGE_TERMINAL_TAYLOR_ORDER2_OR_JC2_VERDICT");',
        "quit;",
    ])
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    loaded = load_loaded()
    base = loaded.load_base()
    tails = json.loads(base.TAILS.read_text())
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    emit(output / f"affine_faber_a_formal_weighted_h3_h5_{label}.sing", args.characteristic, base, tails)
    payload = {
        "status": "PASS-A-FORMAL-WEIGHTED-H3-H5-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "loaded_compiler_sha256": digest(LOADED_PATH),
        "direct_unit_addendum_sha256": digest(ADDENDUM_PATH),
        "q6_repair_review_sha256": digest(Q6_REVIEW_PATH),
        "tails_sha256": digest(base.TAILS),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
