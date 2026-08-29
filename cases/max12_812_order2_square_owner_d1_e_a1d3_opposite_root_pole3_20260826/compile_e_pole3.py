#!/usr/bin/env python3
"""Compile the exceptional E opposite-root pole-three obstruction; AWS only."""

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
LOW_DIR = ROOT / "cases/max12_812_order2_square_owner_d1_unique_ac_d23_lowa6_local_row_20260826"
LOW = LOW_DIR / "compile_local_row.py"
PINS = {
    LOW: "b2fe07fdd2f855598dde5c6ef9828909c94496eb5e196756eff504056cde2769",
    LOW_DIR / "PRODUCER_FREEZE.sha256": "4d69b97d8c6e24baadc76aba69d3d37158a3aa466cf7e44bc3111008c5a07fd3",
    ROOT / "xmodel/max12-812-order2-square-d1-unique-ac-d23-lowa6-local-row-hostile-review-grok-20260826.md":
        "841f0d6ccbb596fa4ace3f08760f039eb288030efa91075112e915d1320592a3",
    ROOT / "xmodel/max12-812-order2-square-d1-unique-ac-d23-lowa6-local-row-promotion-20260826.md":
        "8b92c22bebae73e3efd793c7c7541c53caf8e956f5ce181240c164f3362864da",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only E pole-three compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only E pole-three compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        fail(("cannot import", str(path)))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def check(mapping) -> None:
    for path, expected in mapping.items():
        actual = digest(path)
        if actual != expected:
            fail(("frozen pin mismatch", str(path), actual, expected))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65519, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    check(PINS)
    low = load(LOW, "d1_e_low_parent")
    low.check(low.PINS)
    base = low.load(low.BASE, "d1_e_source_base")
    low.check(base.PINS)
    v1 = base.load_v1()
    low.check(v1.EXPECTED)
    tails = json.loads(v1.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != v1.EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")
    tail_base = v1.load_base()
    miner = low.load(low.MINER, "d1_e_support_parent")
    section, metadata = low.block(
        args.characteristic, base, v1, tail_base, tails, miner, 1, 3
    )
    expected_metadata = {
        "a": 1, "d": 3, "s_min": 1, "r_floor": 2, "G": 15, "T": 18,
        "negative": True, "primitive_count": 8, "maxpole": 3,
        "jet_maxima": {"p": 3, "A": 3, "C": 3, "R": 2,
                       "k10": 2, "k6": 0, "k2": 0, "mu2": 0, "mu4": 0},
    }
    if metadata != expected_metadata:
        fail(("E metadata mismatch", metadata, expected_metadata))
    primitive = miner.enumerate_primitives({
        "a": 1, "d": 3, "c": 4, "s_min": 1, "r": 2,
        "first_ac_grade": 15, "target_grade": 18,
    })
    pole3 = [item for item in primitive if int(item["pole"]) == 3]
    if len(pole3) != 1 or tuple(pole3[0][key] for key in (
        "summand", "load", "fixed_sigma", "R", "A", "C", "pole", "coefficient", "first_grade"
    )) != ("unloaded", None, 15, 0, 3, 0, 3, "-1/16", 18):
        fail(("sole pole-three signature mismatch", pole3))
    if "icv,ik0),dp;" not in section[0]:
        fail("cannot add independently named inverse of au to E ring")
    section[0] = section[0].replace("icv,ik0),dp;", "icv,iau,ik0),dp;")
    lines = section
    root = "lam+sigma*rho1+sigma^2*rho2+sigma^3*rho3"
    P = "B13_P"
    lines += [
        "print(\"E_POLE3_SOURCE_HASHES=PASS\");",
        "print(\"E_POLE3_COMPLETE_PRIMITIVE_COUNT=8\");",
        "print(\"E_POLE3_SOLE_POLE3=MINUS_ONE_SIXTEENTH_A3_OVER_L3_AT_G18\");",
        f"poly E_N3=B13_h1*z^5+B13_h2*z^4+(B13_h3+(3*{P}/2)*B13_h1)*z^3"
        f"+(B13_h4+(3*{P}/2)*B13_h2)*z^2"
        f"+(B13_h5+(3*{P}/2)*B13_h3+(3*({P}^2)/4)*B13_h1)*z"
        f"+(B13_h6+(3*{P}/2)*B13_h4+(3*({P}^2)/4)*B13_h2);",
        f"poly E_Rec7=B13_h7+(3*{P}/2)*B13_h5+(3*({P}^2)/4)*B13_h3+(({P}^3)/8)*B13_h1;",
        "int E_pole3_recurrence=(reduce(E_Rec7,B13_ST)==0);",
        f"poly E_PsiMinus=B13_SourcePhi6-({root})*(B13_SourcePhi5+({P}/4)*B13_SourcePhi3+(3*({P}^2)/32)*B13_SourcePhi1);",
        f"poly E_PsiPlus=B13_SourcePhi6+({root})*(B13_SourcePhi5+({P}/4)*B13_SourcePhi3+(3*({P}^2)/32)*B13_SourcePhi1);",
        f"poly E_NMinus=subst(E_N3,z,-({root}));",
        f"poly E_NPlus=subst(E_N3,z,({root}));",
        "E_NMinus=subst(E_NMinus,p,-2*lam^2); E_NPlus=subst(E_NPlus,p,-2*lam^2);",
        "E_PsiMinus=subst(E_PsiMinus,p,-2*lam^2); E_PsiPlus=subst(E_PsiPlus,p,-2*lam^2);",
        "poly E_NMinusRed=reduce(E_NMinus,B13_RootIdeal); poly E_NPlusRed=reduce(E_NPlus,B13_RootIdeal);",
        "poly E_PsiMinusRed=reduce(E_PsiMinus,B13_RootIdeal); poly E_PsiPlusRed=reduce(E_PsiPlus,B13_RootIdeal);",
        "int E_faber_minus=(reduce(E_NMinusRed-E_PsiMinusRed,B13_ST)==0);",
        "int E_faber_plus=(reduce(E_NPlusRed-E_PsiPlusRed,B13_ST)==0);",
        "poly E_OriMinus=E_PsiMinusRed;",
        "E_OriMinus=subst(E_OriMinus,a1,au); E_OriMinus=subst(E_OriMinus,a0,-au*lam);",
        "E_OriMinus=subst(E_OriMinus,c1,cv); E_OriMinus=subst(E_OriMinus,c0,cv*lam);",
        "E_OriMinus=reduce(E_OriMinus,B13_RootIdeal);",
        "poly E_OriPlus=E_PsiPlusRed;",
        "E_OriPlus=subst(E_OriPlus,a1,au); E_OriPlus=subst(E_OriPlus,a0,au*lam);",
        "E_OriPlus=subst(E_OriPlus,c1,cv); E_OriPlus=subst(E_OriPlus,c0,-cv*lam);",
        "E_OriPlus=reduce(E_OriPlus,B13_RootIdeal);",
    ]
    minus = low.sigma_extract(lines, "E_OriMinus", "E_OriMinus_", 15, 18)
    plus = low.sigma_extract(lines, "E_OriPlus", "E_OriPlus_", 15, 18)
    lines += [
        f"int E_minus_terminal=({minus[15]}==0 && {minus[16]}==0 && {minus[17]}==0 && {minus[18]}-(1/2)*au^3*lam^3==0);",
        f"int E_plus_terminal=({plus[15]}==0 && {plus[16]}==0 && {plus[17]}==0 && {plus[18]}+(1/2)*au^3*lam^3==0);",
        "int E_targetfree=(reduce(B13_SourcePhi1-B13_FullPhi1,B13_ST)==0"
        " && reduce(B13_SourcePhi3-B13_FullPhi3,B13_ST)==0"
        " && reduce(B13_SourcePhi5-B13_FullPhi5,B13_ST)==0"
        " && reduce(B13_SourcePhi6-B13_FullPhi6,B13_ST)==0);",
        f"ideal E_UnitMinus=std(ideal({minus[18]},ilam*lam-1,iau*au-1,icv*cv-1,ik0*k0-1));",
        f"ideal E_UnitPlus=std(ideal({plus[18]},ilam*lam-1,iau*au-1,icv*cv-1,ik0*k0-1));",
        "int E_units=(reduce(1,E_UnitMinus)==0 && reduce(1,E_UnitPlus)==0);",
        "int E_endpoint=B13_endpoint*B13_ra2_second_correction*E_pole3_recurrence*E_faber_minus*E_faber_plus*E_minus_terminal*E_plus_terminal*E_targetfree*E_units;",
        "print(\"E_POLE3_ALL_SEVEN_ROWS_BRIDGED=\"+string(B13_bridge));",
        "print(\"E_POLE3_RA2_SECOND_CORRECTION_RETAINED=\"+string(B13_ra2_second_correction));",
        "print(\"E_POLE3_L3_RECURRENCE=\"+string(E_pole3_recurrence));",
        "print(\"E_POLE3_BOTH_FABER_ROOT_IDENTITIES=\"+string(E_faber_minus*E_faber_plus));",
        "print(\"E_POLE3_BOTH_OPPOSITE_ROOT_TERMINALS=\"+string(E_minus_terminal*E_plus_terminal));",
        "print(\"E_POLE3_TARGETFREE_ROWS_1356=\"+string(E_targetfree));",
        "print(\"E_POLE3_EXACT_UNIT_IDEALS=\"+string(E_units));",
        "if (E_endpoint!=1) { print(\"E_POLE3_FAIL=SOURCE_ROOT_FUNCTIONAL_OR_UNIT\"); quit; }",
        "print(\"E_POLE3_ENDPOINT=PASS_EMPTY_E_A1_D3_RGE2_ON_D_P_K0\");",
        "quit;",
    ]
    output = args.output.resolve()
    if output.exists():
        fail("E pole-three output already exists")
    output.mkdir(parents=True)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    target = output / f"square_d1_e_a1d3_opposite_root_pole3_{label}.sing"
    target.write_text("\n".join(lines) + "\n")
    payload = {
        "status": "PASS-D1-E-OPPOSITE-ROOT-POLE3-COMPILER",
        "scope": "A1_C4_R_GE_2_D1_ON_D_P_K0_ONLY",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "primitive_count": 8,
        "sole_pole3": "-1/16*A^3/L^3@18",
        "input_sha256": digest(target),
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
