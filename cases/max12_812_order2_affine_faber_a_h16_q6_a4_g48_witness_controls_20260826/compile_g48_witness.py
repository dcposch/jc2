#!/usr/bin/env python3
"""Compile two exact-source rational controls for the H16/q6/a4 equality."""

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
        fail("AWS-only grade-48 witness compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only grade-48 witness compiler refused non-Amazon host")
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


def emit(path: Path, characteristic: int, chart: str, base, tails) -> None:
    if chart == "x":
        x0, y0, r00 = "1", "0", "1/2"
        d60, d20, dm0 = "16", "7", "-11/16"
    elif chart == "y":
        x0, y0, r00 = "0", "1", "-1"
        d60, d20, dm0 = "-74", "-61/2", "181/64"
    else:
        fail("unknown chart")
    variables = [
        "u4", "dm4", "d24", "d64", "s04", "s14", "r04", "r14",
        "y4", "x4", "s", "n0", "n1", "n2", "n3", "qr", "qc",
        "qp", "k2", "k6", "k10",
    ]
    lines = [
        f"ring RR={characteristic},({','.join(variables)}),dp;", "option(redSB);",
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
        "poly AA=s^4; poly EE=1; poly DD=EE-3*AA^2; poly MM=1;",
        f"poly XX=s^6*({x0}+s^4*x4); poly YY=s^6*({y0}+s^4*y4);",
        "poly RR1=s^16*r14;",
        f"poly RR0=s^12*({r00}+s^4*r04);",
        "poly SS1=s^16*s14; poly SS0=s^16*s04;",
        "poly QP=EE-6*AA^2;",
        "poly QC=2*AA*(4*AA^2-EE)+XX+RR1;",
        "poly QR=AA^2*(EE-3*AA^2)+RR0-AA*(XX+RR1);",
        "poly N3=s^16*MM; poly N2=s^16*AA*MM;",
        "poly N1=s^16*((DD-2*AA^2)*MM+YY+SS1);",
        "poly N0=s^16*(-AA*DD*MM-AA*YY+(MM*XX)/2+SS0-AA*SS1);",
        "poly LK10=s^42;",
        f"poly LK6=s^42*((15/32)*EE^2+s^2*({d60}+s^4*d64));",
        f"poly LK2=s^42*((15/256)*EE^4+s^2*({d20}+s^4*d24));",
        f"poly MU2=s^42*(-5/4096+s^2*({dm0}+s^4*dm4));",
        "poly MU4=s^48*u4; poly MU6=0; poly JT=0;",
        "proc source(poly P)", "{",
        " P=subst(P,k10,LK10); P=subst(P,k6,LK6); P=subst(P,k2,LK2);",
        " P=subst(P,qp,QP); P=subst(P,qc,QC); P=subst(P,qr,QR);",
        " P=subst(P,n3,N3); P=subst(P,n2,N2); P=subst(P,n1,N1); P=subst(P,n0,N0);",
        " return(P);", "}",
    ])
    for ell in range(1, 8):
        target = {2: "-MU2", 4: "-MU4", 6: "-MU6", 7: "-JT"}.get(ell, "")
        lines.append(f"poly P{ell}=source(T{ell}){target};")
    lines.extend([
        "int lowerControl=lowzero(P1,48)*lowzero(P2,48)*lowzero(P3,48)*lowzero(P4,48)*lowzero(P5,48)*lowzero(P6,48)*lowzero(P7,48);",
    ])
    for ell in range(1, 8):
        lines.append(f"poly C{ell}=tc(P{ell},48);")
    lines.extend([
        "ideal I=C1,C2,C3,C4,C5,C6,C7; ideal G=std(I); int unit=(reduce(1,G)==0);",
        f'print("A_G48W_{chart.upper()}_TCOEFF_CONTROL="+string(tcControl));',
        f'print("A_G48W_{chart.upper()}_LOWER_ZERO="+string(lowerControl));',
    ])
    for ell in range(1, 8):
        lines.append(f'print("A_G48W_{chart.upper()}_C{ell}="+string(C{ell}));')
    lines.extend([
        f'print("A_G48W_{chart.upper()}_GB="+string(G));',
        f'print("A_G48W_{chart.upper()}_UNIT="+string(unit));',
        f'print("A_G48W_{chart.upper()}_DONE=1");',
        f'print("A_G48W_{chart.upper()}_SCOPE=FIXED_RATIONAL_{chart.upper()}_CHART_GRADE48_POSITIVE_CONTROL_ONLY_NO_FULL_FAN_REES_ORDER2_MAX12_OR_JC2_VERDICT");',
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
    for chart in ("x", "y"):
        emit(output / f"affine_faber_a_g48w_{chart}_{label}.sing", args.characteristic, chart, base, tails)
    payload = {
        "status": "PASS-A-G48-WITNESS-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "base_sha256": digest(BASE),
        "tails_sha256": digest(base.TAILS),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
