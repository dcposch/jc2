#!/usr/bin/env python3
"""Compile the full unweighted affine-Faber K-support emitter (AWS only)."""

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
IDENTITY_REVIEW = ROOT / "xmodel/max12-812-order2-affine-faber-a-formal-weighted-h3-h5-hostile-review-grok-20260826.md"
IDENTITY_REVIEW_SHA = "7349330c903e7a336738792324d63570fd0f14252c20754337c6c6f801fa1cf5"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only full-K support compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only full-K support compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_base():
    for path, expected in (
        (LOADED_PATH, LOADED_SHA),
        (IDENTITY_REVIEW, IDENTITY_REVIEW_SHA),
    ):
        if digest(path) != expected:
            fail(f"frozen input mismatch: {path}")
    spec = importlib.util.spec_from_file_location("loaded_kernel", LOADED_PATH)
    if spec is None or spec.loader is None:
        fail("cannot load frozen affine-Faber compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.load_base()


def emit(path: Path, characteristic: int, base, tails) -> None:
    variables = [
        "Jt", "mu6", "mu4", "mu2", "K2", "K6", "K10",
        "S0", "S1", "R0", "R1", "Y", "X", "a", "lam", "M", "E",
        "n0", "n1", "n2", "n3", "qr", "qc", "qp", "k2", "k6", "k10",
    ]
    lines = [
        f"ring R={characteristic},({','.join(variables)}),dp;",
    ]
    for ell in range(1, 8):
        lines.append(f"poly T{ell}={base.tail_text(tails[str(ell)])};")
    lines.extend([
        "poly B=4*a;",
        "poly QP=E-6*a^2;",
        "poly QC=2*a*(4*a^2-E)+X+R1;",
        "poly QR=a^2*(E-3*a^2)+R0-a*(X+R1);",
        "poly N3=lam*M; poly N2=lam*a*M;",
        "poly N1=lam*((E-5*a^2)*M+Y+S1);",
        "poly N0=lam*(-a*(E-3*a^2)*M-a*Y+(M*X)/2+S0-a*S1);",
        "proc source(poly P)", "{",
        " P=subst(P,k10,K10); P=subst(P,k6,K6); P=subst(P,k2,K2);",
        " P=subst(P,qp,QP); P=subst(P,qc,QC); P=subst(P,qr,QR);",
        " P=subst(P,n3,N3); P=subst(P,n2,N2); P=subst(P,n1,N1); P=subst(P,n0,N0);",
        " return(P);", "}",
        "poly P1=source(T1);",
        "poly P2=source(T2)-mu2;",
        "poly P3=source(T3);",
        "poly P4=source(T4)-mu4;",
        "poly P5=source(T5);",
        "poly P6=source(T6)-mu6;",
        "poly P7=source(T7)-Jt/4;",
        "poly H3=P3-(B/2)*P2+((5/32)*B^2-E/4)*P1;",
        "poly H5=P5-B*P4+((21/32)*B^2-(3/4)*E)*P3",
        " +( -(5/16)*B^3+(3/4)*B*E )*P2",
        " +( (195/2048)*B^4-(45/128)*B^2*E+(5/32)*E^2 )*P1;",
        "poly K=E*H3+H5;",
        "int target6=(diff(K,mu6)==0); int targetJ=(diff(K,Jt)==0);",
        "int target4=(diff(K,mu4)-B==0);",
        "poly EXPECT2=-(B*E/4)+(5/16)*B^3;",
        "int target2=(diff(K,mu2)-EXPECT2==0);",
        'print("A_KSUP_TARGET_MU6_ZERO="+string(target6));',
        'print("A_KSUP_TARGET_J_ZERO="+string(targetJ));',
        'print("A_KSUP_TARGET_MU4="+string(target4));',
        'print("A_KSUP_TARGET_MU2="+string(target2));',
        "poly CENTRAL=K;",
        "CENTRAL=subst(CENTRAL,a,0); CENTRAL=subst(CENTRAL,X,0); CENTRAL=subst(CENTRAL,Y,0);",
        "CENTRAL=subst(CENTRAL,R1,0); CENTRAL=subst(CENTRAL,R0,0);",
        "CENTRAL=subst(CENTRAL,S1,0); CENTRAL=subst(CENTRAL,S0,0);",
        "CENTRAL=subst(CENTRAL,K10,0); CENTRAL=subst(CENTRAL,K6,0); CENTRAL=subst(CENTRAL,K2,0);",
        "CENTRAL=subst(CENTRAL,mu2,0); CENTRAL=subst(CENTRAL,mu4,0);",
        "CENTRAL=subst(CENTRAL,mu6,0); CENTRAL=subst(CENTRAL,Jt,0);",
        "poly CUBIC=diff(diff(diff(CENTRAL,lam),lam),lam)/6;",
        "CUBIC=subst(CUBIC,lam,0);",
        "int centralControl=(CUBIC+(E*M^3)/16==0);",
        'print("A_KSUP_CENTRAL_CUBIC="+string(centralControl));',
        "poly REM=K; poly TERM; intvec EX; int TC=0;",
        'print("A_KSUP_TERMS_BEGIN");',
        "while (REM!=0)", "{",
        " TERM=lead(REM); EX=leadexp(TERM); TC++;",
        ' print("A_KSUP_TERM_INDEX="+string(TC));',
        ' print("A_KSUP_TERM_EXP="+string(EX));',
        ' print("A_KSUP_TERM="+string(TERM));',
        " REM=REM-TERM;",
        "}",
        'print("A_KSUP_TERMS_END");',
        'print("A_KSUP_TERM_COUNT="+string(TC));',
        "if (TC<=0) { print(\"A_KSUP_ENDPOINT=FAIL_ZERO_SUPPORT\"); quit; }",
        "if (target6*targetJ*target4*target2*centralControl!=1)",
        " { print(\"A_KSUP_ENDPOINT=FAIL_CONTROL\"); quit; }",
        'print("A_KSUP_ENDPOINT=PASS_FULL_K_MULTISUPPORT");',
        'print("A_KSUP_DONE=1");',
        'print("A_KSUP_SCOPE=UNWEIGHTED_NORMALIZED_AFFINE_FABER_K_SUPPORT_ONLY_NO_PREDECESSOR_REDUCTION_NEWTON_FAN_SOURCE_REES_ORDER2_MAX12_OR_JC2_VERDICT");',
        "quit;",
    ])
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    base = load_base()
    if digest(base.TAILS) != base.EXPECTED_TAILS:
        fail("frozen tails mismatch")
    tails = json.loads(base.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != base.EXPECTED_CANONICAL:
        fail("canonical tails mismatch")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    emit(output / f"affine_faber_a_full_k_multisupport_{label}.sing", args.characteristic, base, tails)
    payload = {
        "status": "PASS-A-FULL-K-MULTISUPPORT-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "loaded_compiler_sha256": digest(LOADED_PATH),
        "identity_review_sha256": digest(IDENTITY_REVIEW),
        "tails_sha256": digest(base.TAILS),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
