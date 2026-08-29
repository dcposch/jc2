#!/usr/bin/env python3
"""Compile the correction-aware discriminant triple-root K3 receiver.

This compiler is deliberately AWS-only.  It imports the frozen ordinary
tail compiler and performs string-level source generation; Singular carries
out every substantive exact calculation on the registered AWS lane.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V1 = ROOT / "cases/max12_812_order2_disc_halfweight_kuranishi_20260826/compile_disc_halfweight.py"
TAILS = ROOT / "cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json"
DESIGN = HERE / "DESIGN.md"
K2_V1 = ROOT / "xmodel/max12-812-order2-discriminant-halfweight-k2-support-theorem-20260826.md"
K2_V2 = ROOT / "xmodel/max12-812-order2-discriminant-halfweight-k2-support-theorem-v2-20260826.md"
K2_REVIEW = ROOT / "xmodel/max12-812-order2-discriminant-halfweight-k2-support-review-terra-20260826.md"
SOURCE_CLIENT = ROOT / "xmodel/max12-812-order2-u2-62-strict-rees-client-20260825.md"
ONEPARAM = ROOT / "xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-20260826.md"

EXPECTED = {
    V1: "4114c4aec72f710c138d49eb7b2d51cbbce14377b7e228526911219902ad3f9d",
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    K2_V1: "20fa404c10c6fdafe59247967db8234f3479ae9a06740b521650b8a8aa88e341",
    K2_V2: "f1cbb203ca26c66c3c57178460912610ba978206043b2bf22bc1b2b73aaac68b",
    K2_REVIEW: "f93ecb4320fadff500638fc6fa7bdfca904ed5556b7a13add4cddb9b40a76b70",
    SOURCE_CLIENT: "e5e3472f052b2ae932daefc9dec7a17106ca4c13f8b920ba59da627d0653fec7",
    ONEPARAM: "5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b",
}
EXPECTED_ALL_TAILS = "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only K3 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only K3 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_v1():
    if digest(V1) != EXPECTED[V1]:
        fail(("V1 compiler hash mismatch", digest(V1), EXPECTED[V1]))
    spec = importlib.util.spec_from_file_location("disc_halfweight_v1", V1)
    if spec is None or spec.loader is None:
        fail("cannot load frozen V1 compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def emit(path: Path, characteristic: int, tails: dict[str, list[list[object]]], v1) -> None:
    # tail_text supplies the one-parameter factors rho^(2*load_weight).
    coeffs = {index: f"A{index}" for index in range(7)}
    loads = {"k10": "(rho^3*jk)", "k6": "k6", "k2": "k2"}
    targets = {1: "0", 2: "mu2", 3: "0", 4: "mu4", 5: "0", 6: "mu6", 7: "J/4"}
    variables = (
        "rho,b,t,C,S,ja,jd,jm,jx,jy,jkc,jkr,jns,jnt,jk,"
        "k6,k2,mu2,mu4,mu6,J"
    )
    lines = [
        'LIB "elim.lib";',
        f"ring R={characteristic},({variables}),dp;",
        'print("DISC_TRIPLE_K3_SOURCE_HASHES=PASS");',
        "poly aa=b/4+rho*ja;",
        "poly dd=-3*b^2/16+rho*jd;",
        "poly mm=6*b*t^2+rho*jm;",
        "poly xx=-2*b*t+rho*jx;",
        "poly yy=6*b*t^3+rho*jy;",
        "poly kkc=C+rho*jkc;",
        "poly kkr=-b*C/4+t^2+rho*jkr;",
        "poly nns=S+rho*jns;",
        "poly nnt=-b*S/4+3*b*t^2*C+rho*jnt;",
        "poly pp=dd-3*aa^2;",
        "poly cc=2*aa*(aa^2-dd)+rho*xx+rho^2*kkc;",
        "poly rr=aa^2*dd-rho*aa*xx+rho^2*kkr;",
        "poly nn3=mm;",
        "poly nn2=aa*mm;",
        "poly nn1=(dd-2*aa^2)*mm+rho*yy+rho^2*nns;",
        "poly nn0=-aa*dd*mm+rho*(-aa*yy+mm*xx/2)+rho^2*nnt;",
        "poly A6=2*pp;",
        "poly A5=2*cc;",
        "poly A4=pp^2+2*rr;",
        "poly A3=2*pp*cc+rho^2*nn3;",
        "poly A2=cc^2+2*pp*rr+rho^2*nn2;",
        "poly A1=2*cc*rr+rho^2*nn1;",
        "poly A0=rr^2+rho^2*nn0;",
        "poly e0=subst(dd+3*aa^2,rho,0);",
        "poly h0=subst(mm*xx/2,rho,0);",
        "poly U0=h0+b*subst(yy,rho,0);",
        "poly V0=subst(mm,rho,0)^3+6*h0*subst(yy,rho,0);",
        "int support_ok=(e0==0 && U0==0 && V0==0);",
        'print("DISC_TRIPLE_K3_REDUCED_SUPPORT_IDENTITIES="+string(support_ok));',
        'if (support_ok!=1) { print("DISC_TRIPLE_K3_FAIL=SUPPORT_IDENTITY"); quit; }',
        "ideal rho7=std(ideal(rho^7));",
        "int divisible=1;",
        "int identity=1;",
        "int forbidden=1;",
        "int target_typed=1;",
        "int load_typed=1;",
    ]
    for ell in range(1, 8):
        expression = v1.tail_text(tails[str(ell)], ell, coeffs, loads)
        if targets[ell] != "0":
            expression += f"-rho^{2 * (12 + ell)}*({targets[ell]})"
        lines.extend([
            f"poly Phi{ell}={expression};",
            f"if (reduce(Phi{ell},rho7)!=0) {{ divisible=0; }}",
            f"poly Zeta{ell}=Phi{ell}/rho^7;",
            f"if (rho^7*Zeta{ell}-Phi{ell}!=0) {{ identity=0; }}",
            f"poly z{ell}=subst(Zeta{ell},rho,0);",
            f"if (diff(z{ell},k6)!=0 || diff(z{ell},k2)!=0 || diff(z{ell},mu2)!=0 || diff(z{ell},mu4)!=0 || diff(z{ell},mu6)!=0 || diff(z{ell},J)!=0) {{ forbidden=0; }}",
            f"if (reduce(diff(Phi{ell},k6),std(ideal(rho^12)))!=0) {{ load_typed=0; }}",
            f"if (reduce(diff(Phi{ell},k2),std(ideal(rho^20)))!=0) {{ load_typed=0; }}",
        ])
    lines.extend([
        "if (diff(Phi2,mu2)!=-rho^28) { target_typed=0; }",
        "if (diff(Phi4,mu4)!=-rho^32) { target_typed=0; }",
        "if (diff(Phi6,mu6)!=-rho^36) { target_typed=0; }",
        "if (diff(Phi7,J)!=-rho^38/4) { target_typed=0; }",
        'print("DISC_TRIPLE_K3_RHO7_DIVISIBLE="+string(divisible));',
        'print("DISC_TRIPLE_K3_DIVISION_IDENTITY="+string(identity));',
        'print("DISC_TRIPLE_K3_FORBIDDEN_EARLY="+string(forbidden));',
        'print("DISC_TRIPLE_K3_LOAD_TYPED="+string(load_typed));',
        'print("DISC_TRIPLE_K3_TARGET_TYPED="+string(target_typed));',
        'if (divisible!=1 || identity!=1 || forbidden!=1 || load_typed!=1 || target_typed!=1) { print("DISC_TRIPLE_K3_FAIL=SOURCE_OR_TYPING"); quit; }',
        'print("DISC_TRIPLE_K3_ROWS_BEGIN");',
        "print(z1); print(z2); print(z3); print(z4); print(z5); print(z6); print(z7);",
        'print("DISC_TRIPLE_K3_ROWS_END");',
        "ideal IK3=z1,z2,z3,z4,z5,z6,z7;",
        "ideal corrections=ja,jd,jm,jx,jy,jkc,jkr,jns,jnt,jk;",
        "ideal EK3=eliminate(IK3,corrections);",
        "EK3=sat(EK3,ideal(b)); EK3=sat(EK3,ideal(t)); EK3=std(EK3);",
        'print("DISC_TRIPLE_K3_ELIM_DIM="+string(dim(EK3)));',
        'print("DISC_TRIPLE_K3_ELIM_UNIT="+string(reduce(1,EK3)==0));',
        'print("DISC_TRIPLE_K3_ELIM_BASIS_BEGIN"); print(EK3); print("DISC_TRIPLE_K3_ELIM_BASIS_END");',
        'print("DISC_TRIPLE_K3_TAYLOR_MANIFEST=CHARGED_NOT_COMPILED");',
        'print("DISC_TRIPLE_K3_ENDPOINT=PASS_CORRECTION_AWARE_K3_NECESSARY_GATE");',
        "quit;",
    ])
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 32003), required=True)
    args = parser.parse_args()
    tag = require_aws()
    for source, expected in EXPECTED.items():
        actual = digest(source)
        if actual != expected:
            fail(("frozen source mismatch", str(source), actual, expected))
    v1 = load_v1()
    tails = json.loads(TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    target = output / f"disc_triple_k3_p{args.characteristic}.sing"
    emit(target, args.characteristic, tails, v1)
    payload = {
        "status": "PASS-DISC-TRIPLE-K3-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "all_tails_sha256": EXPECTED_ALL_TAILS,
        "input_sha256": digest(target),
        "scope": "CORRECTION_AWARE_K3_NECESSARY_GATE_NO_LIFT_TAYLOR_OR_ORDER2_VERDICT",
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
