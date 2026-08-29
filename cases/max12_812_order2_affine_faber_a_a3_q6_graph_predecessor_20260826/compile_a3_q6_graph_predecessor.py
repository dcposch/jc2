#!/usr/bin/env python3
"""Compile the exact a=3,q=6 affine-graph predecessor block (AWS only)."""

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
BASE_PATH = ROOT / "cases/max12_812_order2_affine_faber_a_mixed_sigma45_20260826/compile_sigma45.py"
BASE_SHA = "c19badfcfad44842f42118d031a5bfe92729d714e2a329b2af7097be629ea3d9"
HAND_NOTE = ROOT / "xmodel/max12-812-order2-affine-faber-a-a3-q6-graph-predecessor-composition-20260826.md"
HAND_SHA = "264033da9f60f7954a17d32f468e563838da310b7628ef21d06c1a0c6775c560"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only a3-q6 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only a3-q6 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_base():
    for path, expected in ((BASE_PATH, BASE_SHA), (HAND_NOTE, HAND_SHA)):
        if digest(path) != expected:
            fail(f"frozen input mismatch: {path}")
    spec = importlib.util.spec_from_file_location("sigma45_base", BASE_PATH)
    if spec is None or spec.loader is None:
        fail("cannot load frozen tail compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def emit(path: Path, characteristic: int, base, tails) -> None:
    variables = [
        "satu", "dm1", "d21", "d61", "k101",
        "s013", "s113", "r013", "r113", "s012", "s112", "r012", "r112",
        "y7", "x7", "y6", "x6", "m2", "m1", "e2", "e1",
        "a6", "a5", "a4", "a3", "kk", "m", "p", "s",
        "n0", "n1", "n2", "n3", "qr", "qc", "qp", "k2", "k6", "k10",
    ]
    lines = [
        f"ring R={characteristic},({','.join(variables)}),dp;",
        "proc tc(poly P,int n)", "{", " int i; poly Q=P;",
        " for (i=1; i<=n; i++) { Q=(Q-subst(Q,s,0))/s; }",
        " return(subst(Q,s,0));", "}",
        "proc lowzero(poly P,int n)", "{", " int i; int ok=1; poly Q=P; poly C;",
        " for (i=0; i<n; i++) { C=subst(Q,s,0); ok=ok*(C==0); Q=(Q-C)/s; }",
        " return(ok);", "}",
        "poly TC=3+5*s+7*s^2+11*s^3+13*s^4+17*s^5+19*s^6+23*s^7+29*s^8+31*s^9+37*s^10+41*s^11+43*s^12+47*s^13+53*s^14+59*s^15+61*s^16+67*s^17+71*s^18+73*s^19+79*s^20+83*s^21+89*s^22+97*s^23+101*s^24+103*s^25+107*s^26+109*s^27+113*s^28+127*s^29+131*s^30+137*s^31+139*s^32+149*s^33+151*s^34+157*s^35+163*s^36+167*s^37+173*s^38+179*s^39+181*s^40+191*s^41+193*s^42;",
        "int tcControl=1; int qi;",
        "intvec tv=3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193;",
        "for (qi=0; qi<=42; qi++) { tcControl=tcControl*(tc(TC,qi)==tv[qi+1]); }",
    ]
    for ell in range(1, 8):
        lines.append(f"poly T{ell}={base.tail_text(tails[str(ell)])};")
    lines.extend([
        "poly aa=s^3*(a3+s*a4+s^2*a5+s^3*a6);",
        "poly EE=p+s*e1+s^2*e2; poly DD=EE-3*aa^2;",
        "poly MM=m+s*m1+s^2*m2;",
        "poly XX=s^6*(x6+s*x7); poly YY=s^6*(y6+s*y7);",
        "poly RR1=s^12*(r112+s*r113); poly RR0=s^12*(r012+s*r013);",
        "poly SS1=s^12*(s112+s*s113); poly SS0=s^12*(s012+s*s013);",
        "poly QP=EE-6*aa^2;",
        "poly QC=2*aa*(4*aa^2-EE)+XX+RR1;",
        "poly QR=aa^2*(EE-3*aa^2)+RR0-aa*(XX+RR1);",
        "poly N3=s^15*MM; poly N2=s^15*aa*MM;",
        "poly N1=s^15*((DD-2*aa^2)*MM+YY+SS1);",
        "poly N0=s^15*(-aa*DD*MM-aa*YY+(MM*XX)/2+SS0-aa*SS1);",
        "poly LK10=s^42*(kk+s*k101);",
        "poly LK6=s^42*((15/32)*kk*p^2+s*d61);",
        "poly LK2=s^42*((15/256)*kk*p^4+s*d21);",
        "poly MU2=s^42*(-(5/4096)*kk*p^6+s*dm1);",
        "proc source(poly P)", "{",
        " P=subst(P,k10,LK10); P=subst(P,k6,LK6); P=subst(P,k2,LK2);",
        " P=subst(P,qp,QP); P=subst(P,qc,QC); P=subst(P,qr,QR);",
        " P=subst(P,n3,N3); P=subst(P,n2,N2); P=subst(P,n1,N1); P=subst(P,n0,N0);",
        " return(P);", "}",
    ])
    for ell in range(1, 8):
        target = "-MU2" if ell == 2 else ""
        lines.append(f"poly P{ell}=source(T{ell}){target};")
    lines.extend([
        "int lowerControl=lowzero(P1,42)*lowzero(P2,42)*lowzero(P3,42)*lowzero(P4,42)*lowzero(P5,42)*lowzero(P6,42)*lowzero(P7,42);",
        "poly C1=tc(P1,42); poly C2=tc(P2,42); poly C3=tc(P3,42);",
        "poly C4=tc(P4,42); poly C5=tc(P5,42); poly C6=tc(P6,42); poly C7=tc(P7,42);",
        "poly G1=(-3/8)*r112*m^2+(3/4)*s012*m;",
        "poly G2=(-3/8)*r012*m^2+(3/8)*y6^2;",
        "poly G3=(-3/32)*p*r112*m^2+(-3/8)*m*x6*y6+(3/16)*p*s012*m;",
        "poly G4=(3/32)*m^2*x6^2+(-3/16)*p*m^2*r012+(-3/16)*p*y6^2;",
        "poly G5=(-3/256)*p^2*r112*m^2+(3/32)*p*m*x6*y6+(3/128)*p^2*s012*m;",
        "poly G6=(-3/64)*p^2*m^2*r012+(3/64)*p^2*y6^2;",
        "poly G7=(3/1024)*p^3*r112*m^2+(-3/256)*p^2*m*x6*y6+(-3/512)*p^3*s012*m;",
        "int rowControl=(C1-G1==0)*(C2-G2==0)*(C3-G3==0)*(C4-G4==0)*(C5-G5==0)*(C6-G6==0)*(C7-G7==0);",
        "int dependencyControl=(G6-(1/8)*p^2*G2==0)*(G5-(3/32)*p^2*G1+(1/4)*p*G3==0)*(G7-(1/32)*p^2*G3+(1/64)*p^3*G1==0);",
        "int handControl=(G3-(1/4)*p*G1+(3/8)*m*x6*y6==0);",
        "int successorControl=1;",
        "successorControl=successorControl*(diff(C1,a3)==0)*(diff(C3,a3)==0)*(diff(C4,a3)==0)*(diff(C6,a3)==0);",
        "successorControl=successorControl*(diff(C1,a4)==0)*(diff(C3,a4)==0)*(diff(C4,a4)==0)*(diff(C6,a4)==0);",
        "successorControl=successorControl*(diff(C1,e1)==0)*(diff(C3,e1)==0)*(diff(C4,e1)==0)*(diff(C6,e1)==0);",
        "successorControl=successorControl*(diff(C1,m1)==0)*(diff(C3,m1)==0)*(diff(C4,m1)==0)*(diff(C6,m1)==0);",
        "successorControl=successorControl*(diff(C1,d61)==0)*(diff(C2,d21)==0)*(diff(C2,dm1)==0)*(diff(C1,k101)==0);",
        "int graphK10Control=(diff(C1,kk)==0)*(diff(C2,kk)==0)*(diff(C3,kk)==0)*(diff(C4,kk)==0)*(diff(C5,kk)==0)*(diff(C6,kk)==0)*(diff(C7,kk)==0);",
        "poly BAD2=tc(P2+s^42*kk,42); int mutationControl=(BAD2!=0);",
        "ideal IX=G1,G3,G4,G6,y6,satu*p*m*x6-1; ideal GX=std(IX); int unitX=(reduce(1,GX)==0);",
        "ideal IY=G1,G3,G4,G6,x6,satu*p*m*y6-1; ideal GY=std(IY); int unitY=(reduce(1,GY)==0);",
        'print("A_A3Q6_TCOEFF_CONTROL="+string(tcControl));',
        'print("A_A3Q6_LOWER_ZERO="+string(lowerControl));',
        'print("A_A3Q6_ROW_CONTROL="+string(rowControl));',
        'print("A_A3Q6_DEPENDENCY_CONTROL="+string(dependencyControl));',
        'print("A_A3Q6_HAND_CONTROL="+string(handControl));',
        'print("A_A3Q6_SUCCESSOR_OMISSION_CONTROL="+string(successorControl));',
        'print("A_A3Q6_GRAPH_K10_CANCEL="+string(graphK10Control));',
        'print("A_A3Q6_MUTATION_DETECTED="+string(mutationControl));',
        'print("A_A3Q6_UNIT_X="+string(unitX)); print("A_A3Q6_UNIT_Y="+string(unitY));',
        'print("A_A3Q6_C1="+string(C1)); print("A_A3Q6_C2="+string(C2));',
        'print("A_A3Q6_C3="+string(C3)); print("A_A3Q6_C4="+string(C4));',
        'print("A_A3Q6_C5="+string(C5)); print("A_A3Q6_C6="+string(C6)); print("A_A3Q6_C7="+string(C7));',
        "if (tcControl*lowerControl*rowControl*dependencyControl*handControl*successorControl*graphK10Control*mutationControl*unitX*unitY!=1)",
        " { print(\"A_A3Q6_ENDPOINT=FAIL_CONTROL_OR_PREDECESSOR\"); quit; }",
        'print("A_A3Q6_ENDPOINT=PASS_GRAPH_PREDECESSOR_BOTH_CHARTS_EMPTY");',
        'print("A_A3Q6_DONE=1");',
        'print("A_A3Q6_SCOPE=FIXED_DELAYED_H15_A3_Q6_GRADE42_GRAPH_PREDECESSOR_ONLY_NO_SOURCE_COVER_REES_ORDER2_MAX12_OR_JC2_VERDICT");',
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
    emit(output / f"affine_faber_a_a3_q6_graph_predecessor_{label}.sing", args.characteristic, base, tails)
    payload = {
        "status": "PASS-A-A3-Q6-GRAPH-PREDECESSOR-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "base_sha256": digest(BASE_PATH),
        "hand_note_sha256": digest(HAND_NOTE),
        "tails_sha256": digest(base.TAILS),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
