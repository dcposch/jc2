#!/usr/bin/env python3
"""Compile the fixed H17/q7/a3 affine-Faber grade-48 predecessor."""

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
BASE = ROOT / "cases/max12_812_order2_affine_faber_a_mixed_sigma45_20260826/compile_sigma45.py"
BASE_SHA = "c19badfcfad44842f42118d031a5bfe92729d714e2a329b2af7097be629ea3d9"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only H17/q7/a3 predecessor compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only H17/q7/a3 predecessor compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_base():
    if digest(BASE) != BASE_SHA:
        fail("frozen base compiler mismatch")
    spec = importlib.util.spec_from_file_location("sigma45_base", BASE)
    if spec is None or spec.loader is None:
        fail("cannot import frozen base compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def emit(path: Path, characteristic: int, base, tails) -> None:
    variables = [
        "satu", "d4", "dm", "d2", "d6",
        "s0", "s1", "r0", "r1", "y", "x", "m",
        "m1", "m2", "m3", "m4", "m5", "m6",
        "p", "e1", "e2", "e3", "e4", "e5", "e6",
        "a3", "a4", "a5", "a6", "a7", "a8", "a9",
        "kk0", "kk1", "kk2", "kk3", "kk4", "kk5", "kk6",
        "s", "n0", "n1", "n2", "n3", "qr", "qc", "qp",
        "k2", "k6", "k10",
    ]
    lines = [
        f"ring RR={characteristic},({','.join(variables)}),dp;",
        "option(redSB);",
        "proc tc(poly P,int n)", "{", " int i; poly Q=P;",
        " for (i=1; i<=n; i++) { Q=(Q-subst(Q,s,0))/s; }",
        " return(subst(Q,s,0));", "}",
        "proc lowzero(poly P,int n)", "{", " int i; int ok=1; poly Q=P; poly C;",
        " for (i=0; i<n; i++) { C=subst(Q,s,0); ok=ok*(C==0); Q=(Q-C)/s; }",
        " return(ok);", "}",
        "poly TC=3+5*s+7*s^2+11*s^3+13*s^4+17*s^5+19*s^6+23*s^7+29*s^8+31*s^9+37*s^10+41*s^11+43*s^12+47*s^13+53*s^14+59*s^15+61*s^16+67*s^17+71*s^18+73*s^19+79*s^20+83*s^21+89*s^22+97*s^23+101*s^24+103*s^25+107*s^26+109*s^27+113*s^28+127*s^29+131*s^30+137*s^31+139*s^32+149*s^33+151*s^34+157*s^35+163*s^36+167*s^37+173*s^38+179*s^39+181*s^40+191*s^41+193*s^42+197*s^43+199*s^44+211*s^45+223*s^46+227*s^47+229*s^48;",
        "int tcControl=1; int qi;",
        "intvec tv=3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229;",
        "for (qi=0; qi<=48; qi++) { tcControl=tcControl*(tc(TC,qi)==tv[qi+1]); }",
    ]
    for ell in range(1, 8):
        lines.append(f"poly T{ell}={base.tail_text(tails[str(ell)])};")
    lines.extend([
        "poly AA=s^3*(a3+s*a4+s^2*a5+s^3*a6+s^4*a7+s^5*a8+s^6*a9);",
        "poly EE=p+s*e1+s^2*e2+s^3*e3+s^4*e4+s^5*e5+s^6*e6;",
        "poly DD=EE-3*AA^2;",
        "poly MM=m+s*m1+s^2*m2+s^3*m3+s^4*m4+s^5*m5+s^6*m6;",
        "poly XX=s^7*x; poly YY=s^7*y;",
        "poly RR1=s^14*r1; poly RR0=s^14*r0;",
        "poly SS1=s^14*s1; poly SS0=s^14*s0;",
        "poly QP=EE-6*AA^2;",
        "poly QC=2*AA*(4*AA^2-EE)+XX+RR1;",
        "poly QR=AA^2*(EE-3*AA^2)+RR0-AA*(XX+RR1);",
        "poly N3=s^17*MM; poly N2=s^17*AA*MM;",
        "poly N1=s^17*((DD-2*AA^2)*MM+YY+SS1);",
        "poly N0=s^17*(-AA*DD*MM-AA*YY+(MM*XX)/2+SS0-AA*SS1);",
        "poly KK=kk0+s*kk1+s^2*kk2+s^3*kk3+s^4*kk4+s^5*kk5+s^6*kk6;",
        "poly LK10=s^42*KK;",
        "poly LK6=s^42*((15/32)*KK*EE^2+s^6*d6);",
        "poly LK2=s^42*((15/256)*KK*EE^4+s^6*d2);",
        "poly MU2=s^42*(-(5/4096)*KK*EE^6+s^6*dm);",
        "poly MU4=s^48*d4;",
        "proc source(poly P)", "{",
        " P=subst(P,k10,LK10); P=subst(P,k6,LK6); P=subst(P,k2,LK2);",
        " P=subst(P,qp,QP); P=subst(P,qc,QC); P=subst(P,qr,QR);",
        " P=subst(P,n3,N3); P=subst(P,n2,N2); P=subst(P,n1,N1); P=subst(P,n0,N0);",
        " return(P);", "}",
    ])
    for ell in range(1, 8):
        target = {2: "-MU2", 4: "-MU4"}.get(ell, "")
        lines.append(f"poly P{ell}=source(T{ell}){target};")
    lines.extend([
        "int lowerControl=lowzero(P1,48)*lowzero(P2,48)*lowzero(P3,48)*lowzero(P4,48)*lowzero(P5,48)*lowzero(P6,48)*lowzero(P7,48);",
        "poly C1=tc(P1,48); poly C2=tc(P2,48); poly C3=tc(P3,48); poly C4=tc(P4,48);",
        "poly C5=tc(P5,48); poly C6=tc(P6,48); poly C7=tc(P7,48);",
        "int excessControl=1;",
        "excessControl=excessControl*(diff(C1,e1)==0)*(diff(C2,e1)==0)*(diff(C3,e1)==0)*(diff(C4,e1)==0)*(diff(C5,e1)==0)*(diff(C6,e1)==0)*(diff(C7,e1)==0);",
        "excessControl=excessControl*(diff(C1,kk1)==0)*(diff(C2,kk1)==0)*(diff(C3,kk1)==0)*(diff(C4,kk1)==0)*(diff(C5,kk1)==0)*(diff(C6,kk1)==0)*(diff(C7,kk1)==0);",
        "excessControl=excessControl*(diff(C1,a3)==0)*(diff(C2,a3)==0)*(diff(C3,a3)==0)*(diff(C4,a3)==0)*(diff(C5,a3)==0)*(diff(C6,a3)==0)*(diff(C7,a3)==0);",
        "ideal IFACE=C1,C2,C3,C4,C5,C6,C7;",
        "ideal IELIM=eliminate(IFACE,d6*d2*dm*d4);",
        "ideal IX=C1,C2,C3,C4,C5,C6,C7,satu*p*m*x-1; ideal GX=std(IX); int unitX=(reduce(1,GX)==0);",
        "kill GX; kill IX;",
        "ideal IY=C1,C2,C3,C4,C5,C6,C7,satu*p*m*y-1; ideal GY=std(IY); int unitY=(reduce(1,GY)==0);",
        'print("A_H17Q7A3_TCOEFF_CONTROL="+string(tcControl));',
        'print("A_H17Q7A3_LOWER_ZERO="+string(lowerControl));',
        'print("A_H17Q7A3_EXCESS_CONTROL="+string(excessControl));',
        'print("A_H17Q7A3_UNIT_X="+string(unitX)); print("A_H17Q7A3_UNIT_Y="+string(unitY));',
        'print("A_H17Q7A3_C1="+string(C1)); print("A_H17Q7A3_C2="+string(C2));',
        'print("A_H17Q7A3_C3="+string(C3)); print("A_H17Q7A3_C4="+string(C4));',
        'print("A_H17Q7A3_C5="+string(C5)); print("A_H17Q7A3_C6="+string(C6)); print("A_H17Q7A3_C7="+string(C7));',
        'print("A_H17Q7A3_ELIM="+string(IELIM));',
        'print("A_H17Q7A3_ENDPOINT=FIXED_GRADE48_PREDECESSOR_EMITTED");',
        'print("A_H17Q7A3_DONE=1");',
        'print("A_H17Q7A3_SCOPE=H17_Q7_A3_FIXED_NORMALIZED_GRAPH_GRADE48_PREDECESSOR_ONLY_NO_RATIONAL_REGRADING_SOURCE_REES_ORDER2_MAX12_OR_JC2_VERDICT");',
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
    emit(output / f"affine_faber_a_h17_q7_a3_g48_{label}.sing", args.characteristic, base, tails)
    payload = {
        "status": "PASS-A-H17-Q7-A3-G48-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "base_sha256": digest(BASE),
        "tails_sha256": digest(base.TAILS),
        "source_archive_scope": "registration+compiler+wrappers+base+tails",
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
