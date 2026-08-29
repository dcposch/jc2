#!/usr/bin/env python3
"""AWS-only compiler for the honest closure-first K00 incidence.

This compiler consumes the frozen one-parameter [6,2] ordinary-tail source.
It deliberately computes

    K = (Phi):Lambda^infinity:Jdet^infinity,
    B = K + (Lambda) + M_K00,
    H = B:(C6*k10*Jdet)^infinity

in that order.  Imposing M_K00 before either source saturation is present
only as a mandatory negative control and is never substituted for K.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TAILS = (
    ROOT
    / "cases/max12_812_order2_u2_62_strict_rees_20260825"
    / "aws_compile_v2_jsat/run/output/compiled_v2/tails.json"
)

INPUTS = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    ROOT / "xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-20260826.md":
        "5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b",
    ROOT / "xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-promotion-20260826.md":
        "82167b862a779d1104e3fb904d71627b799f48074241d8496fc1051d0a7afa2f",
    ROOT / "xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-review-grok-20260826.md":
        "1da9974dde45fd73c757eb315d50bc9e8abaa028ebb8d5894ca2ea4b2bd6d2de",
    ROOT / "xmodel/max12-812-order2-u2-62-oneparameter-rees-runit-delta-review-grok-20260826.md":
        "0fa0dc4afb160ae4b9ed6bc195e1158e44b92cdc5bb5ea1619a146e9d52aac96",
    ROOT / "xmodel/max12-812-order2-u2-62-strict-rees-client-20260825.md":
        "e5e3472f052b2ae932daefc9dec7a17106ca4c13f8b920ba59da627d0653fec7",
    ROOT / "xmodel/max12-812-order2-u2-62-strict-rees-client-erratum-v2-20260825.md":
        "5aa954cbe6396ef5de353519eaf10aed567aec55964bb197c9eb1576b131c10b",
    ROOT / "xmodel/max12-812-order2-u2-62-strict-rees-compiler-v2-source-review-20260825.md":
        "b7666bb12ef454f5047074898e0384968393916d97bd06673d3a1f20ab70f50d",
    ROOT / "cases/max12_812_order2_u2_62_oneparam_rees_20260826/compile_oneparam_rees.py":
        "5905e57578c5f9af047f70f8fce48a6ab56ce9dccfc2a33d868d8e05b3f4ea82",
    ROOT / "cases/max12_812_order2_u2_62_oneparam_rees_20260826/FREEZE.sha256":
        "84da88152fcc1ec7552b4c12f950d0979b4edc0a80269e315736cfac37d38f6e",
    ROOT / "xmodel/max12-812-order2-p0-k00-honest-source-discriminator-design-sol-20260827.md":
        "9c5bf1229cf45dd7ea4d5d3907fd6033c88c0d9768934d01ea79e658f3d65a17",
}

EXPECTED_ALL_TAILS = "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"
NAMES = [f"a{i}" for i in range(7)] + ["k10", "k6", "k2"]
WEIGHTS = [8 - i for i in range(7)] + [2, 6, 10]
LOAD_LAMBDA_WEIGHTS = [2, 6, 10]
RING_VARIABLES = [
    "Lambda",
    *[f"C{i}" for i in range(7)],
    "k10", "k6", "k2",
    "mu2", "mu4", "mu6",
    "Jdet",
]


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def rational_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"({value.numerator}/{value.denominator})"


def term_text(monomial: list[int], coefficient: Fraction) -> str:
    factors: list[str] = []
    for i, exponent in enumerate(monomial[:7]):
        if exponent:
            factors.append(f"C{i}" if exponent == 1 else f"C{i}^{exponent}")
    lambda_power = 0
    for offset, exponent in enumerate(monomial[7:]):
        if exponent:
            name = NAMES[7 + offset]
            factors.append(name if exponent == 1 else f"{name}^{exponent}")
            lambda_power += LOAD_LAMBDA_WEIGHTS[offset] * exponent
    if lambda_power:
        factors.append("Lambda" if lambda_power == 1 else f"Lambda^{lambda_power}")
    body = "*".join(factors) or "1"
    if coefficient == 1 and factors:
        return body
    if coefficient == -1 and factors:
        return "-" + body
    return f"{rational_text(coefficient)}*{body}" if factors else rational_text(coefficient)


def tail_text(entries: list[list[object]], ell: int) -> str:
    terms: list[str] = []
    for raw_monomial, raw_coefficient in entries:
        monomial = [int(value) for value in raw_monomial]
        if len(monomial) != len(NAMES):
            fail(("monomial length", ell, monomial))
        if sum(monomial[7:]) > 1 or any(value not in (0, 1) for value in monomial[7:]):
            fail(("tail is not affine-linear in lower loads", ell, monomial))
        actual_weight = sum(a * b for a, b in zip(monomial, WEIGHTS))
        if actual_weight != 12 + ell:
            fail(("tail weight", ell, actual_weight, monomial))
        terms.append(term_text(monomial, Fraction(str(raw_coefficient))))
    return "+".join(terms).replace("+-", "-") if terms else "0"


def emit(path: Path, characteristic: int, tails: dict[str, list[list[object]]]) -> None:
    if "J1" in RING_VARIABLES or "J2" in RING_VARIABLES or "J" in RING_VARIABLES:
        fail("collision-ideal/Jacobian identifier collision")
    targets = {
        1: "0", 2: "mu2", 3: "0", 4: "mu4",
        5: "0", 6: "mu6", 7: "Jdet/4",
    }
    lines = [
        'LIB "elim.lib";',
        f"ring R={characteristic},({','.join(RING_VARIABLES)}),dp;",
        'print("K00_SOURCE_HASHES=PASS");',
        'print("K00_SOURCE_TYPE=A_Q_Lambda_C0_C6_k10_k6_k2_mu2_mu4_mu6_Jdet");',
        'print("K00_JDET_DISTINCT_FROM_J1_J2=PASS");',
        'print("K00_LOAD_LINEARITY=PASS");',
    ]
    for ell in range(1, 8):
        expression = tail_text(tails[str(ell)], ell)
        target = targets[ell]
        if target != "0":
            expression += f"-Lambda^{12 + ell}*({target})"
        lines.append(f"poly Phi{ell}={expression};")
    lines.extend([
        "ideal I=Phi1,Phi2,Phi3,Phi4,Phi5,Phi6,Phi7;",
        "ideal MK00=C5,C3,C1,8*C4-3*C6^2,16*C2-C6^3,256*C0-C6^4,k6,k2,mu2,mu4,mu6;",
        "ideal GMK00=std(MK00);",
        "int coreRows=1;",
        "if (reduce(Phi1,GMK00)!=0) { coreRows=0; }",
        "if (reduce(Phi2,GMK00)!=0) { coreRows=0; }",
        "if (reduce(Phi3,GMK00)!=0) { coreRows=0; }",
        "if (reduce(Phi4,GMK00)!=0) { coreRows=0; }",
        "if (reduce(Phi5,GMK00)!=0) { coreRows=0; }",
        "if (reduce(Phi6,GMK00)!=0) { coreRows=0; }",
        "if (reduce(Phi7+Lambda^19*Jdet/4,GMK00)!=0) { coreRows=0; }",
        'if (coreRows!=1) { print("K00_FAIL=INVARIANT_CORE_ROW_MAP"); quit(81); }',
        'print("K00_INVARIANT_CORE_ROW_MAP=PASS");',
        "poly restrictionIdentity=(Lambda*Jdet)^19+4*Jdet^18*Phi7;",
        'if (reduce(restrictionIdentity,GMK00)!=0) { print("K00_FAIL=RESTRICTION_IDENTITY"); quit(82); }',
        'print("K00_RESTRICTION_CERTIFICATE_IDENTITY=PASS");',
        'print("K00_STAGE_RESTRICTION_FIRST_START");',
        "ideal restrictionFirst=I+MK00;",
        "ideal restrictionSatLambda=sat(restrictionFirst,ideal(Lambda));",
        "ideal restrictionSat=sat(restrictionSatLambda,ideal(Jdet));",
        "restrictionSat=std(restrictionSat);",
        'if (reduce(1,restrictionSat)!=0) { print("K00_FAIL=RESTRICTION_FIRST_NOT_UNIT"); quit(83); }',
        'print("K00_STAGE_RESTRICTION_FIRST_DONE");',
        'print("K00_RESTRICTION_FIRST_UNIT=PASS");',
        'print("K00_STAGE_CLOSURE_LAMBDA_START");',
        "ideal KL=sat(I,ideal(Lambda));",
        'print("K00_STAGE_CLOSURE_LAMBDA_DONE");',
        'print("K00_KL_SIZE="+string(size(KL)));',
        'print("K00_STAGE_CLOSURE_JDET_START");',
        "ideal K=sat(KL,ideal(Jdet));",
        'print("K00_STAGE_CLOSURE_JDET_DONE");',
        'print("K00_K_SIZE="+string(size(K)));',
        "ideal B=K+ideal(Lambda)+MK00;",
        'print("K00_STAGE_BOUNDARY_CORE_DONE");',
        'print("K00_B_SIZE="+string(size(B)));',
        "poly finalLocalizer=C6*k10*Jdet;",
        'print("K00_STAGE_FINAL_LOCALIZATION_START");',
        "list Hdata=sat_with_exp(B,ideal(finalLocalizer));",
        "ideal H=Hdata[1];",
        "int Hexp=Hdata[2];",
        "H=std(H);",
        'print("K00_STAGE_FINAL_LOCALIZATION_DONE");',
        'print("K00_H_SIZE="+string(size(H)));',
        'print("K00_H_DIM="+string(dim(H)));',
        'print("K00_H_SATURATION_EXPONENT="+string(Hexp));',
        'write(":w H_BASIS.txt",string(H));',
        "int Hunit=(reduce(1,H)==0);",
        "if (Hunit==1)",
        "{",
        "  poly witnessPower=finalLocalizer^Hexp;",
        "  ideal GB=std(B);",
        '  if (reduce(witnessPower,GB)!=0) { print("K00_FAIL=UNIT_POWER_NOT_IN_B"); quit(84); }',
        "  matrix Hlift=lift(B,ideal(witnessPower));",
        "  poly Hreplay=-witnessPower;",
        "  int jj;",
        "  for (jj=1; jj<=size(B); jj=jj+1) { Hreplay=Hreplay+Hlift[jj,1]*B[jj]; }",
        '  if (Hreplay!=0) { print("K00_FAIL=UNIT_LIFT_REPLAY"); quit(85); }',
        '  write(":w H_UNIT_LIFT.txt",string(Hlift));',
        '  print("K00_H_UNIT_LIFT_REPLAY=PASS");',
        '  print("K00_H_ENDPOINT=UNIT");',
        "}",
        "else",
        "{",
        '  print("K00_H_NONUNIT_BASIS_SAVED=PASS");',
        '  print("K00_H_ENDPOINT=NONUNIT");',
        "}",
        'print("K00_CLOSURE_FIRST_ORDER=PASS");',
        'print("K00_CLOSURE_ENDPOINT=PASS");',
        "quit;",
    ])
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65519, 65521), default=0)
    args = parser.parse_args()
    tag = require_aws()
    for source, expected in INPUTS.items():
        if digest(source) != expected:
            fail(("frozen source mismatch", source, digest(source), expected))
    tails = json.loads(TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")
    if sorted(tails) != [str(i) for i in range(1, 8)]:
        fail("tail key mismatch")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    singular = output / f"k00_closure_char{args.characteristic}.sing"
    emit(singular, args.characteristic, tails)
    payload = {
        "status": "PASS-K00-CLOSURE-FIRST-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "tails_sha256": digest(TAILS),
        "all_tails_sha256": EXPECTED_ALL_TAILS,
        "singular_input_sha256": digest(singular),
        "ring_variables": RING_VARIABLES,
        "jacobian_parameter": "Jdet",
        "collision_ideals_not_ring_variables": ["J1", "J2"],
        "operation_order": [
            "I:Lambda^infinity",
            "KL:Jdet^infinity",
            "+(Lambda)+M_K00",
            ":(C6*k10*Jdet)^infinity",
        ],
        "restriction_before_saturation": "MANDATORY_NEGATIVE_CONTROL_ONLY",
        "scope": {
            "fixed_source_profile": "U=2,[6,2],ordinary-tail",
            "generic_k00_incidence_only": True,
            "C6_zero_tip": "NOT_TESTED",
            "k10_zero": "NOT_TESTED",
            "other_load_rays": "NOT_TESTED",
            "other_square_normal_cones": "NOT_TESTED",
            "full_collision_receiver": "NOT_TESTED",
            "taylor_realization": "NOT_TESTED",
            "order2_closed": False,
            "JC2": "NOT_CLAIMED",
        },
    }
    (output / "compiler_result.json").write_text(
        json.dumps(payload, sort_keys=True, indent=2) + "\n"
    )
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
