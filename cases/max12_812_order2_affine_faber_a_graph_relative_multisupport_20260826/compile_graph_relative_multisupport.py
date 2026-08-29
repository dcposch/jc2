#!/usr/bin/env python3
"""Compile exact affine-Faber K support in load-graph coordinates (AWS only)."""

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
FULL_COMPILER = ROOT / "cases/max12_812_order2_affine_faber_a_full_k_multisupport_20260826/compile_full_k_multisupport.py"
FULL_COMPILER_SHA = "78a7926b29b3aade1e2e5111606b165ec222e6cf8a5d8cb7d7fde92f1ad83965"
GRAPH_NOTE = ROOT / "xmodel/max12-812-order2-affine-faber-a-load-graph-functional-cancellation-20260826.md"
GRAPH_NOTE_SHA = "c467fc5454eda943721c60f599f9e005f158a2fa3f934b64c694df116b1d6bbd"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only graph-relative compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only graph-relative compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_base():
    for path, expected in ((FULL_COMPILER, FULL_COMPILER_SHA), (GRAPH_NOTE, GRAPH_NOTE_SHA)):
        if digest(path) != expected:
            fail(f"frozen input mismatch: {path}")
    spec = importlib.util.spec_from_file_location("full_k_multisupport", FULL_COMPILER)
    if spec is None or spec.loader is None:
        fail("cannot load frozen full-K compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.load_base()


def emit(path: Path, characteristic: int, base, tails) -> None:
    variables = [
        "Jt", "mu6", "d4", "dm", "d2", "d6", "K10",
        "S0", "S1", "R0", "R1", "Y", "X", "a", "lam", "M", "E",
        "n0", "n1", "n2", "n3", "qr", "qc", "qp", "k2", "k6", "k10",
    ]
    lines = [f"ring R={characteristic},({','.join(variables)}),dp;"]
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
        "poly KG6=d6+(15/32)*E^2*K10;",
        "poly KG2=d2+(15/256)*E^4*K10;",
        "poly MUG2=dm-(5/4096)*E^6*K10;",
        "proc source(poly P)", "{",
        " P=subst(P,k10,K10); P=subst(P,k6,KG6); P=subst(P,k2,KG2);",
        " P=subst(P,qp,QP); P=subst(P,qc,QC); P=subst(P,qr,QR);",
        " P=subst(P,n3,N3); P=subst(P,n2,N2); P=subst(P,n1,N1); P=subst(P,n0,N0);",
        " return(P);", "}",
        "poly P1=source(T1);",
        "poly P2=source(T2)-MUG2;",
        "poly P3=source(T3);",
        "poly P4=source(T4)-d4;",
        "poly P5=source(T5);",
        "poly P6=source(T6)-mu6;",
        "poly P7=source(T7)-Jt/4;",
        "poly H3=P3-(B/2)*P2+((5/32)*B^2-E/4)*P1;",
        "poly H5=P5-B*P4+((21/32)*B^2-(3/4)*E)*P3",
        " +( -(5/16)*B^3+(3/4)*B*E )*P2",
        " +( (195/2048)*B^4-(45/128)*B^2*E+(5/32)*E^2 )*P1;",
        "poly K=E*H3+H5;",
        "int target6=(diff(K,mu6)==0); int targetJ=(diff(K,Jt)==0);",
        "int target4=(diff(K,d4)-B==0);",
        "poly EXPECTDM=-(B*E/4)+(5/16)*B^3;",
        "int targetM=(diff(K,dm)-EXPECTDM==0);",
        "poly CENTRAL=K;",
        "CENTRAL=subst(CENTRAL,a,0); CENTRAL=subst(CENTRAL,X,0); CENTRAL=subst(CENTRAL,Y,0);",
        "CENTRAL=subst(CENTRAL,R1,0); CENTRAL=subst(CENTRAL,R0,0);",
        "CENTRAL=subst(CENTRAL,S1,0); CENTRAL=subst(CENTRAL,S0,0);",
        "CENTRAL=subst(CENTRAL,d6,0); CENTRAL=subst(CENTRAL,d2,0);",
        "CENTRAL=subst(CENTRAL,dm,0); CENTRAL=subst(CENTRAL,d4,0);",
        "CENTRAL=subst(CENTRAL,K10,0); CENTRAL=subst(CENTRAL,mu6,0); CENTRAL=subst(CENTRAL,Jt,0);",
        "poly CUBIC=diff(diff(diff(CENTRAL,lam),lam),lam)/6;",
        "CUBIC=subst(CUBIC,lam,0);",
        "int centralControl=(CUBIC+(E*M^3)/16==0);",
        "poly LC=diff(K,lam);",
        "LC=subst(LC,lam,0); LC=subst(LC,a,0); LC=subst(LC,X,0); LC=subst(LC,Y,0);",
        "LC=subst(LC,R1,0); LC=subst(LC,R0,0); LC=subst(LC,S1,0); LC=subst(LC,S0,0);",
        "LC=subst(LC,d4,0); LC=subst(LC,dm,0); LC=subst(LC,mu6,0); LC=subst(LC,Jt,0);",
        "poly EXPECTL=M*E*(-3*E^2*d6/64+d2/8);",
        "int lambdaControl=(LC-EXPECTL==0);",
        "poly AC=diff(K,a);",
        "AC=subst(AC,a,0); AC=subst(AC,lam,0); AC=subst(AC,X,0); AC=subst(AC,Y,0);",
        "AC=subst(AC,R1,0); AC=subst(AC,R0,0); AC=subst(AC,S1,0); AC=subst(AC,S0,0);",
        "AC=subst(AC,mu6,0); AC=subst(AC,Jt,0);",
        "poly EXPECTA=-9*E^5*d6/128+E^3*d2/8-E*dm+4*d4;",
        "int centerControl=(AC-EXPECTA==0);",
        "poly KBAD=subst(K,d6,d6+E^2*K10);",
        "poly BADLC=diff(KBAD,lam);",
        "BADLC=subst(BADLC,lam,0); BADLC=subst(BADLC,a,0);",
        "BADLC=subst(BADLC,X,0); BADLC=subst(BADLC,Y,0);",
        "BADLC=subst(BADLC,R1,0); BADLC=subst(BADLC,R0,0);",
        "BADLC=subst(BADLC,S1,0); BADLC=subst(BADLC,S0,0);",
        "BADLC=subst(BADLC,d6,0); BADLC=subst(BADLC,d2,0);",
        "BADLC=subst(BADLC,dm,0); BADLC=subst(BADLC,d4,0);",
        "BADLC=subst(BADLC,mu6,0); BADLC=subst(BADLC,Jt,0);",
        "int mutationControl=(BADLC!=0);",
        "int rawControl=1;",
        "rawControl=rawControl*(diff(K,n0)==0)*(diff(K,n1)==0)*(diff(K,n2)==0)*(diff(K,n3)==0);",
        "rawControl=rawControl*(diff(K,qr)==0)*(diff(K,qc)==0)*(diff(K,qp)==0);",
        "rawControl=rawControl*(diff(K,k2)==0)*(diff(K,k6)==0)*(diff(K,k10)==0);",
        'print("A_KGRAPH_TARGET_MU6_ZERO="+string(target6));',
        'print("A_KGRAPH_TARGET_J_ZERO="+string(targetJ));',
        'print("A_KGRAPH_TARGET_D4="+string(target4));',
        'print("A_KGRAPH_TARGET_DM="+string(targetM));',
        'print("A_KGRAPH_CENTRAL_CUBIC="+string(centralControl));',
        'print("A_KGRAPH_TRANSVERSE_LAMBDA="+string(lambdaControl));',
        'print("A_KGRAPH_TRANSVERSE_CENTER="+string(centerControl));',
        'print("A_KGRAPH_MUTATION_DETECTED="+string(mutationControl));',
        'print("A_KGRAPH_RAW_COORDINATES_GONE="+string(rawControl));',
        "poly REM=K; poly TERM; intvec EX; int TC=0;",
        'print("A_KGRAPH_TERMS_BEGIN");',
        "while (REM!=0)", "{",
        " TERM=lead(REM); EX=leadexp(TERM); TC++;",
        ' print("A_KGRAPH_TERM_INDEX="+string(TC));',
        ' print("A_KGRAPH_TERM_EXP="+string(EX));',
        ' print("A_KGRAPH_TERM="+string(TERM));',
        " REM=REM-TERM;",
        "}",
        'print("A_KGRAPH_TERMS_END");',
        'print("A_KGRAPH_TERM_COUNT="+string(TC));',
        "if (TC<=0) { print(\"A_KGRAPH_ENDPOINT=FAIL_ZERO_SUPPORT\"); quit; }",
        "if (target6*targetJ*target4*targetM*centralControl*lambdaControl*centerControl*mutationControl*rawControl!=1)",
        " { print(\"A_KGRAPH_ENDPOINT=FAIL_CONTROL\"); quit; }",
        'print("A_KGRAPH_ENDPOINT=PASS_GRAPH_RELATIVE_MULTISUPPORT");',
        'print("A_KGRAPH_DONE=1");',
        'print("A_KGRAPH_SCOPE=GRAPH_RELATIVE_NORMALIZED_K_SUPPORT_ONLY_NO_PREDECESSOR_REDUCTION_NEWTON_FAN_SOURCE_REES_ORDER2_MAX12_OR_JC2_VERDICT");',
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
    emit(output / f"affine_faber_a_graph_relative_multisupport_{label}.sing", args.characteristic, base, tails)
    payload = {
        "status": "PASS-A-GRAPH-RELATIVE-MULTISUPPORT-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "full_compiler_sha256": digest(FULL_COMPILER),
        "graph_note_sha256": digest(GRAPH_NOTE),
        "tails_sha256": digest(base.TAILS),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
