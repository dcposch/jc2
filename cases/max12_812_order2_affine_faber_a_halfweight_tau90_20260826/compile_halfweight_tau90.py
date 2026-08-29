#!/usr/bin/env python3
"""Compile the correction-complete affine-Faber A half-weight tau-90 gate."""

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
        fail("AWS-only A half-weight compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only A half-weight compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_base():
    if digest(BASE_PATH) != BASE_SHA:
        fail("frozen sigma45 base compiler mismatch")
    spec = importlib.util.spec_from_file_location("sigma45_base_for_halfweight", BASE_PATH)
    if spec is None or spec.loader is None:
        fail("cannot load frozen sigma45 compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def series(prefix: str, start: int, stop: int, variable: str = "t") -> str:
    terms = [prefix + str(start)]
    terms.extend(f"{variable}^{j-start}*{prefix}{j}" for j in range(start + 1, stop + 1))
    return "+".join(terms)


def emit(path: Path, characteristic: int, base, tails) -> None:
    moving = [f"a{j}" for j in range(10, 17)]
    tangents = [f"e{j}" for j in range(1, 7)] + [f"m{j}" for j in range(1, 7)]
    loads = []
    for prefix in ("k10", "k6", "k2", "mu2"):
        loads.extend(f"{prefix}{j}" for j in range(1, 7))
    variables = [
        "satu", *reversed(loads), *reversed(tangents), *reversed(moving),
        "mu20", "ss0", "ss1", "rr0", "rr1", "y", "x", "kk", "m", "p", "t",
        "ch5", "ch4", "ch3", "ch2", "ch1", "ce", "cb",
        "n0", "n1", "n2", "n3", "qr", "qc", "qp", "k2", "k6", "k10",
    ]
    lines = [
        f"ring R={characteristic},({','.join(variables)}),dp;",
        "proc tc(poly P,int n)", "{", "  int i; poly Q=P;",
        "  for (i=1; i<=n; i++) { Q=(Q-subst(Q,t,0))/t; }",
        "  return(subst(Q,t,0));", "}",
        "poly TC=3+5*t^15+7*t^30+11*t^84+13*t^90;",
        "int tcControl=(tc(TC,0)==3)*(tc(TC,1)==0)*(tc(TC,15)==5)*(tc(TC,30)==7)*(tc(TC,83)==0)*(tc(TC,84)==11)*(tc(TC,89)==0)*(tc(TC,90)==13);",
        'print("A_HW90_TCOEFF_CONTROL="+string(tcControl));',
        "poly CP1=ch1;",
        "poly CP2=(cb/4)*ch1+ch2;",
        "poly CP3=(-cb^2/32+ce/4)*ch1+(cb/2)*ch2+ch3;",
        "poly CP4=(ce/2)*ch2+(3*cb/4)*ch3+ch4;",
        "poly CP5=(7*cb^4/2048-3*cb^2*ce/128+ce^2/32)*ch1+(-cb^3/64+cb*ce/8)*ch2+(3*cb^2/32+3*ce/4)*ch3+cb*ch4+ch5;",
        "poly CI3=CP3-(cb/2)*CP2+(5*cb^2/32-ce/4)*CP1;",
        "poly CI5=CP5-cb*CP4+(21*cb^2/32-3*ce/4)*CP3+(-5*cb^3/16+3*cb*ce/4)*CP2+(195*cb^4/2048-45*cb^2*ce/128+5*ce^2/32)*CP1;",
        "int connectionControl=(CI3==ch3)*(CI5==ch5);",
        'print("A_HW90_FABER_CONNECTION_CONTROL="+string(connectionControl));',
    ]
    for ell in range(1, 8):
        lines.append(f"poly T{ell}={base.tail_text(tails[str(ell)])};")
    a_series = series("a", 10, 16)
    e_series = "+".join(["p"] + [f"t^{j}*e{j}" for j in range(1, 7)])
    m_series = "+".join(["m"] + [f"t^{j}*m{j}" for j in range(1, 7)])
    lines.extend([
        f"poly AA=t^10*({a_series});",
        f"poly EE={e_series};",
        f"poly MM={m_series};",
        "poly DD=EE-3*AA^2;",
        "poly XX=t^15*x; poly YY=t^15*y;",
        "poly RR1=t^30*rr1; poly RR0=t^30*rr0;",
        "poly SS1=t^30*ss1; poly SS0=t^30*ss0;",
        "poly QP=EE-6*AA^2;",
        "poly QC=2*AA*(4*AA^2-EE)+XX+RR1;",
        "poly QR=AA^2*(EE-3*AA^2)+RR0-AA*(XX+RR1);",
        "poly N3=t^30*MM; poly N2=t^30*AA*MM;",
        "poly N1=t^30*((DD-2*AA^2)*MM+YY+SS1);",
        "poly N0=t^30*(-AA*DD*MM-AA*YY+(MM*XX)/2+SS0-AA*SS1);",
        "poly LK10=t^84*(kk+t*k101+t^2*k102+t^3*k103+t^4*k104+t^5*k105+t^6*k106);",
        "poly LK6=t^84*((15/32)*kk*p^2+t*k61+t^2*k62+t^3*k63+t^4*k64+t^5*k65+t^6*k66);",
        "poly LK2=t^84*((15/256)*kk*p^4+t*k21+t^2*k22+t^3*k23+t^4*k24+t^5*k25+t^6*k26);",
        "poly MU2=t^84*(mu20+t*mu21+t^2*mu22+t^3*mu23+t^4*mu24+t^5*mu25+t^6*mu26);",
        "proc source(poly P)", "{",
        "  P=subst(P,k10,LK10); P=subst(P,k6,LK6); P=subst(P,k2,LK2);",
        "  P=subst(P,qp,QP); P=subst(P,qc,QC); P=subst(P,qr,QR);",
        "  P=subst(P,n3,N3); P=subst(P,n2,N2); P=subst(P,n1,N1); P=subst(P,n0,N0);",
        "  return(P);", "}",
    ])
    for ell in range(1, 8):
        target = "-MU2" if ell == 2 else ""
        lines.append(f"poly P{ell}=source(T{ell}){target};")
        for grade in range(84, 91):
            lines.append(f'print("A_HW90_R{ell}_G{grade}="+string(tc(P{ell},{grade})));')
    lines.extend([
        "poly BB=4*AA;",
        "poly H3=P3-(BB/2)*P2+(5*BB^2/32-EE/4)*P1;",
        "poly H5=P5-BB*P4+(21*BB^2/32-3*EE/4)*P3+(-5*BB^3/16+3*BB*EE/4)*P2+(195*BB^4/2048-45*BB^2*EE/128+5*EE^2/32)*P1;",
        "ideal T84=std(ideal(t^84)); ideal T90=std(ideal(t^90));",
        "int preLoadControl=1;",
    ])
    for ell in range(1, 8):
        lines.append(f"preLoadControl=preLoadControl*(reduce(P{ell},T84)==0);")
    lines.extend([
        "int invariantLowerControl=(reduce(H3,T90)==0)*(reduce(H5,T90)==0);",
        "poly H390=tc(H3,90); poly H590=tc(H5,90);",
        "int cert3=(16*H390+6*m*x*y+m^3==0);",
        "int cert5=(8*H590-3*p*m*x*y==0);",
        'print("A_HW90_PRELOAD_ZERO="+string(preLoadControl));',
        'print("A_HW90_INVARIANTS_LOWER_ZERO="+string(invariantLowerControl));',
        'print("A_HW90_H3_G90="+string(H390));',
        'print("A_HW90_H5_G90="+string(H590));',
        'print("A_HW90_H3_CERT="+string(cert3));',
        'print("A_HW90_H5_CERT="+string(cert5));',
        "ideal I=H390,H590,satu*p*m*kk-1;",
        'print("A_HW90_STD_BEGIN"); ideal G=std(I); print(G); print("A_HW90_STD_END");',
        "int unitControl=(reduce(1,G)==0);",
        'print("A_HW90_UNIT="+string(unitControl));',
        "if (tcControl*connectionControl*preLoadControl*invariantLowerControl*cert3*cert5*unitControl==1) { print(\"A_HW90_ENDPOINT=PASS_COMPLETE_SOURCE_HALFWEIGHT_UNIT\"); }",
        'else { print("A_HW90_ENDPOINT=FAIL_CONTROL_IDENTITY_OR_UNIT"); quit; }',
        'print("A_HW90_DONE=1");',
        'print("A_HW90_SCOPE=DELAYED_LOAD_REPEATED_A_Q15_OVER_2_THROUGH_TAU90_ONLY_NO_TERMINAL_TAYLOR_ORDER2_OR_JC2_VERDICT");',
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
    emit(output / f"affine_faber_a_halfweight_tau90_{label}.sing", args.characteristic, base, tails)
    payload = {
        "status": "PASS-A-HALFWEIGHT-TAU90-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "base_sha256": digest(BASE_PATH),
        "tails_sha256": digest(base.TAILS),
        "scope": "DELAYED_LOAD_REPEATED_A_Q15_OVER_2_THROUGH_TAU90",
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
