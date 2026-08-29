#!/usr/bin/env python3
"""Compile the fixed H16/q6/a4 affine-Faber equality wall through grade 48."""

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
        fail("AWS-only H16/q6/a4 equality compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only H16/q6/a4 equality compiler refused non-Amazon host")
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


def series(start: int, names: list[str]) -> str:
    body = "+".join(("s^%d*%s" % (i, name)) if i else name for i, name in enumerate(names))
    return f"s^{start}*({body})"


def emit(path: Path, characteristic: int, base, tails) -> None:
    groups = [
        ["satu", "u4", "u6", "jt"],
        [f"dm{i}" for i in range(5)],
        [f"d2{i}" for i in range(5)],
        [f"d6{i}" for i in range(5)],
        [f"s0{i}" for i in range(5)],
        [f"s1{i}" for i in range(5)],
        [f"r0{i}" for i in range(5)],
        [f"r1{i}" for i in range(5)],
        [f"y{i}" for i in range(5)],
        [f"x{i}" for i in range(5)],
        [f"m{i}" for i in range(4, 0, -1)] + ["m"],
        [f"e{i}" for i in range(6, 0, -1)] + ["p"],
        [f"a{i}" for i in range(6, -1, -1)],
        [f"kk{i}" for i in range(6, -1, -1)],
        ["s", "n0", "n1", "n2", "n3", "qr", "qc", "qp", "k2", "k6", "k10"],
    ]
    variables = [item for group in groups for item in group]
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
    aa = series(4, [f"a{i}" for i in range(7)])
    ee = "p+" + "+".join(f"s^{i}*e{i}" for i in range(1, 7))
    mm = "m+" + "+".join(f"s^{i}*m{i}" for i in range(1, 5))
    xx = series(6, [f"x{i}" for i in range(5)])
    yy = series(6, [f"y{i}" for i in range(5)])
    rr1 = series(12, [f"r1{i}" for i in range(5)])
    rr0 = series(12, [f"r0{i}" for i in range(5)])
    ss1 = series(12, [f"s1{i}" for i in range(5)])
    ss0 = series(12, [f"s0{i}" for i in range(5)])
    kk = "kk0+" + "+".join(f"s^{i}*kk{i}" for i in range(1, 7))
    dd6 = series(2, [f"d6{i}" for i in range(5)])
    dd2 = series(2, [f"d2{i}" for i in range(5)])
    ddm = series(2, [f"dm{i}" for i in range(5)])
    lines.extend([
        f"poly AA={aa};",
        f"poly EE={ee}; poly DD=EE-3*AA^2;",
        f"poly MM={mm};",
        f"poly XX={xx}; poly YY={yy};",
        f"poly RR1={rr1}; poly RR0={rr0};",
        f"poly SS1={ss1}; poly SS0={ss0};",
        "poly QP=EE-6*AA^2;",
        "poly QC=2*AA*(4*AA^2-EE)+XX+RR1;",
        "poly QR=AA^2*(EE-3*AA^2)+RR0-AA*(XX+RR1);",
        "poly N3=s^16*MM; poly N2=s^16*AA*MM;",
        "poly N1=s^16*((DD-2*AA^2)*MM+YY+SS1);",
        "poly N0=s^16*(-AA*DD*MM-AA*YY+(MM*XX)/2+SS0-AA*SS1);",
        f"poly KK={kk};",
        f"poly D6={dd6}; poly D2={dd2}; poly DM={ddm};",
        "poly LK10=s^42*KK;",
        "poly LK6=s^42*((15/32)*KK*EE^2+D6);",
        "poly LK2=s^42*((15/256)*KK*EE^4+D2);",
        "poly MU2=s^42*(-(5/4096)*KK*EE^6+DM);",
        "poly MU4=s^48*u4; poly MU6=s^54*u6; poly JT=s^57*jt/4;",
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
        "int lowerControl=lowzero(P1,44)*lowzero(P2,44)*lowzero(P3,44)*lowzero(P4,44)*lowzero(P5,44)*lowzero(P6,44)*lowzero(P7,44);",
    ])
    for grade in range(44, 49):
        for ell in range(1, 8):
            lines.append(f"poly C{grade}_{ell}=tc(P{ell},{grade});")
    pre = ",".join(f"C{grade}_{ell}" for grade in range(44, 48) for ell in range(1, 8))
    full = ",".join(f"C{grade}_{ell}" for grade in range(44, 49) for ell in range(1, 8))
    lines.extend([
        "poly BB=4*AA;",
        "poly H3=P3-(BB/2)*P2+(5*BB^2/32-EE/4)*P1;",
        "poly H5=P5-BB*P4+(21*BB^2/32-3*EE/4)*P3+(-5*BB^3/16+3*BB*EE/4)*P2+(195*BB^4/2048-45*BB^2*EE/128+5*EE^2/32)*P1;",
        "poly KFUN=EE*H3+H5; poly K48=tc(KFUN,48);",
        f"ideal IPRE={pre};",
        "ideal GPRE=std(IPRE); poly K48NF=reduce(K48,GPRE);",
        f"ideal IFULL={full};",
        "ideal IX=IFULL,satu*p*m*x0-1; ideal GX=std(IX); int unitX=(reduce(1,GX)==0);",
        "kill GX; kill IX;",
        "ideal IY=IFULL,satu*p*m*y0-1; ideal GY=std(IY); int unitY=(reduce(1,GY)==0);",
        'print("A_H16Q6A4_TCOEFF_CONTROL="+string(tcControl));',
        'print("A_H16Q6A4_LOWER_ZERO="+string(lowerControl));',
    ])
    for ell in range(1, 8):
        lines.append(f'print("A_H16Q6A4_C44_{ell}="+string(C44_{ell}));')
    for ell in range(1, 8):
        lines.append(f'print("A_H16Q6A4_C48_{ell}="+string(C48_{ell}));')
    lines.extend([
        'print("A_H16Q6A4_K48="+string(K48));',
        'print("A_H16Q6A4_K48_NF="+string(K48NF));',
        'print("A_H16Q6A4_UNIT_X="+string(unitX)); print("A_H16Q6A4_UNIT_Y="+string(unitY));',
        'print("A_H16Q6A4_ENDPOINT=FIXED_REPRESENTATIVE_THROUGH_GRADE48_EMITTED");',
        'print("A_H16Q6A4_DONE=1");',
        'print("A_H16Q6A4_SCOPE=H16_Q6_A4_FIXED_REPRESENTATIVE_SOURCE_ROWS_G44_TO_G48_ONLY_NO_RATIONAL_REGRADING_REES_ORDER2_MAX12_OR_JC2_VERDICT");',
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
    emit(output / f"affine_faber_a_h16_q6_a4_g48_{label}.sing", args.characteristic, base, tails)
    payload = {
        "status": "PASS-A-H16-Q6-A4-G48-COMPILER",
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
