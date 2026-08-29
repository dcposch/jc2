#!/usr/bin/env python3
"""Compile the loaded K2-kernel source shards through sigma grade 45."""

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


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only loaded-kernel compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only loaded-kernel compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_base():
    if digest(BASE_PATH) != BASE_SHA:
        fail("frozen sigma45 base compiler mismatch")
    spec = importlib.util.spec_from_file_location("sigma45_base", BASE_PATH)
    if spec is None or spec.loader is None:
        fail("cannot load sigma45 base compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def emit(path: Path, characteristic: int, chart: str, base, tails) -> None:
    jets = []
    for prefix in ("x", "y"):
        jets.extend(f"{prefix}{j}" for j in range(6, 10))
    for prefix in ("r1", "r0", "s1", "s0"):
        jets.extend(f"{prefix}{j}" for j in range(12, 16))
    variables = [
        "satu", *reversed(jets), "m3", "m2", "m1", "e3", "e2", "e1",
        "mu23", "mu22", "mu21", "mu20",
        "k23", "k22", "k21", "k63", "k62", "k61", "k103", "k102", "k101", "kk",
        "m", "a5", "p", "s", "n0", "n1", "n2", "n3", "qr", "qc", "qp", "k2", "k6", "k10",
    ]
    lines = [
        f"ring R={characteristic},({','.join(variables)}),dp;",
        "proc tc(poly P,int n)", "{", "  int i; poly Q=P;",
        "  for (i=1; i<=n; i++) { Q=(Q-subst(Q,s,0))/s; }",
        "  return(subst(Q,s,0));", "}",
        "poly TC=3+5*s+7*s^2+11*s^3+13*s^4+17*s^5+19*s^6+23*s^7+29*s^8+31*s^9+37*s^10+41*s^11+43*s^12+47*s^13+53*s^14+59*s^15+61*s^16+67*s^17+71*s^18+73*s^19+79*s^20+83*s^21+89*s^22+97*s^23+101*s^24+103*s^25+107*s^26+109*s^27+113*s^28+127*s^29+131*s^30+137*s^31+139*s^32+149*s^33+151*s^34+157*s^35+163*s^36+167*s^37+173*s^38+179*s^39+181*s^40+191*s^41+193*s^42+197*s^43+199*s^44+211*s^45;",
        "int tcControl=1; int qi;",
        "intvec tv=3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211;",
        "for (qi=0; qi<=45; qi++) { tcControl=tcControl*(tc(TC,qi)==tv[qi+1]); }",
        'print("A_LK45_TCOEFF_CONTROL="+string(tcControl));',
    ]
    for ell in range(1, 8):
        lines.append(f"poly T{ell}={base.tail_text(tails[str(ell)])};")
    lines.extend([
        "poly aa=s^5*a5; poly EE=p+s*e1+s^2*e2+s^3*e3; poly DD=EE-3*aa^2;",
        "poly MM=m+s*m1+s^2*m2+s^3*m3;",
        "poly XX=s^6*x6+s^7*x7+s^8*x8+s^9*x9;",
        "poly YY=s^6*y6+s^7*y7+s^8*y8+s^9*y9;",
        "poly RR1=s^12*r112+s^13*r113+s^14*r114+s^15*r115;",
        "poly RR0=s^12*r012+s^13*r013+s^14*r014+s^15*r015;",
        "poly SS1=s^12*s112+s^13*s113+s^14*s114+s^15*s115;",
        "poly SS0=s^12*s012+s^13*s013+s^14*s014+s^15*s015;",
        "poly QP=EE-6*aa^2;",
        "poly QC=2*aa*(4*aa^2-EE)+XX+RR1;",
        "poly QR=aa^2*(EE-3*aa^2)+RR0-aa*(XX+RR1);",
        "poly N3=s^15*MM; poly N2=s^15*aa*MM;",
        "poly N1=s^15*((DD-2*aa^2)*MM+YY+SS1);",
        "poly N0=s^15*(-aa*DD*MM-aa*YY+(MM*XX)/2+SS0-aa*SS1);",
        "poly LK10=s^42*(kk+s*k101+s^2*k102+s^3*k103);",
        "poly LK6=s^42*((15/32)*kk*p^2+s*k61+s^2*k62+s^3*k63);",
        "poly LK2=s^42*((15/256)*kk*p^4+s*k21+s^2*k22+s^3*k23);",
        "poly MU2=s^42*(mu20+s*mu21+s^2*mu22+s^3*mu23);",
        "proc source(poly P)", "{",
        " P=subst(P,k10,LK10); P=subst(P,k6,LK6); P=subst(P,k2,LK2);",
        " P=subst(P,qp,QP); P=subst(P,qc,QC); P=subst(P,qr,QR);",
        " P=subst(P,n3,N3); P=subst(P,n2,N2); P=subst(P,n1,N1); P=subst(P,n0,N0); return(P);", "}",
    ])
    generators = []
    for ell in range(1, 8):
        target = "-MU2" if ell == 2 else ""
        lines.append(f"poly P{ell}=source(T{ell}){target};")
        for grade in range(42, 46):
            name = f"G{ell}_{grade}"
            lines.append(f"poly {name}=tc(P{ell},{grade});")
            lines.append(f'print("A_LK45_R{ell}_G{grade}="+string({name}));')
            generators.append(name)
    lower = "*".join(f"(tc(P{ell},{grade})==0)" for ell in range(1, 8) for grade in range(42))
    chart_generators = {
        "q6x": ["y6", "satu*p*m*kk*x6-1"],
        "q6y": ["x6", "satu*p*m*kk*y6-1"],
        "q7x": ["x6", "y6", "y7", "satu*p*m*kk*x7-1"],
        "q7y": ["x6", "y6", "x7", "satu*p*m*kk*y7-1"],
        "zero": ["x6", "y6", "x7", "y7", "satu*p*m*kk-1"],
    }[chart]
    lines.extend([
        f"int lowerControl={lower};",
        'print("A_LK45_LOWER_ZERO="+string(lowerControl));',
        f"ideal I={','.join(generators + chart_generators)};",
        'print("A_LK45_STD_BEGIN");', "ideal G=std(I);", 'print(G);', 'print("A_LK45_STD_END");',
        "int unitControl=(reduce(1,G)==0);",
        'print("A_LK45_UNIT="+string(unitControl));',
        'print("A_LK45_DIM="+string(dim(G)));',
        f'print("A_LK45_CHART={chart}");',
        "if (tcControl*lowerControl==1) { print(\"A_LK45_ENDPOINT=PASS_COMPLETE_EMISSION_AND_STANDARD_BASIS\"); }",
        'else { print("A_LK45_ENDPOINT=FAIL_CONTROL"); quit; }',
        'print("A_LK45_DONE=1");',
        'print("A_LK45_SCOPE=DELAYED_LOAD_REPEATED_A_KERNEL_GRADES42_45_ONLY_NO_TERMINAL_TAYLOR_ORDER2_OR_JC2_VERDICT");',
        "quit;",
    ])
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    parser.add_argument("--chart", choices=("q6x", "q6y", "q7x", "q7y", "zero"), required=True)
    args = parser.parse_args()
    tag = require_aws()
    base = load_base()
    if digest(base.TAILS) != base.EXPECTED_TAILS:
        fail("frozen tails mismatch")
    tails = json.loads(base.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != base.EXPECTED_CANONICAL:
        fail("canonical tails mismatch")
    output = args.output.resolve(); output.mkdir(parents=True, exist_ok=False)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    emit(output / f"affine_faber_a_loaded_kernel_{args.chart}_{label}.sing", args.characteristic, args.chart, base, tails)
    payload = {"status": "PASS-A-LOADED-KERNEL-COMPILER", "chart": args.chart, "registered_aws_lane": tag, "characteristic": args.characteristic, "base_sha256": digest(BASE_PATH), "tails_sha256": digest(base.TAILS)}
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
