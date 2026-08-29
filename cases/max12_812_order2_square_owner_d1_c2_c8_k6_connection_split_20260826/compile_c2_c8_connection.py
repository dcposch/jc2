#!/usr/bin/env python3
"""Compile the D1 primary-C2 c=8 first-k6-connection split; AWS only."""

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
PREV_DIR = ROOT / "cases/max12_812_order2_square_owner_d1_c2_targetfree_c3c7_20260826"
PREV = PREV_DIR / "compile_c2_targetfree_c3c7.py"
BASE_DIR = ROOT / "cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_20260826"
BASE = BASE_DIR / "compile_r1_d1_ac.py"
PINS = {
    PREV: "fdd281398b9e4ff374dd716867026b50017e02a63e2d33a6df69f725ba22d5d2",
    ROOT / "xmodel/max12-812-order2-square-d1-c2-targetfree-c3c7-promotion-20260826.md":
        "eaff1eaa3800fa327cb3b2a892d2d6b0a6592b12e691c17f28b8eebe0f00d127",
    BASE: "e024a13d24a11519f70b535d4b47c47c62538a684b8bc71e79216410cd8ecb7c",
    BASE_DIR / "FREEZE.sha256":
        "34b0f3254410e39abfc9843febd3c053f965a30dfa948d9e0367c0fb094611a6",
    ROOT / "xmodel/max12-812-order2-square-maximal-pole-row-syzygy-miner-spec-20260826.md":
        "c4eba2d79521d6c621223dc1b36bb298e7a805bf1cd595b593f444d14f148358",
    HERE / "PREREGISTRATION.md":
        "bd1bed04c66792061ad2985de3c99c6a5feed5e4d31f03c5e5e71d129c7abef6",
}
EXPECTED = {
    ("k6", "k6", 17, 0, 0, 1, 1, "3/4", 25),
    ("unloaded", None, 10, 0, 1, 1, 1, "3/4", 26),
    ("unloaded", None, 10, 0, 0, 2, 2, "3/8", 26),
    ("k10", "k10", 11, 1, 0, 1, 1, "5/8", 26),
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if (platform.system() != "Linux" or not vendor.is_file()
            or vendor.read_text().strip() != "Amazon EC2" or not tag):
        fail("AWS-only D1 C2 c8 compiler refused unregistered/non-EC2 host")
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

    previous = load(PREV, "d1_c2_c3c7_predecessor")
    inventory = previous.enumerate_primitives(8)
    if {previous.signature(item) for item in inventory} != EXPECTED:
        fail(("c8 primitive census mismatch", inventory, EXPECTED))
    if {previous.signature(item) for item in previous.enumerate_primitives(8, 1)} != EXPECTED:
        fail("c8 padded primitive census mismatch")
    pole_two = [item for item in inventory if int(item["pole"]) == 2]
    if len(pole_two) != 1 or (int(pole_two[0]["C"]), pole_two[0]["coefficient"]) != (2, "3/8"):
        fail(("c8 maximal-pole census mismatch", pole_two))
    if any(int(item["A"]) < 0 or int(item["R"]) < 0 for item in inventory):
        fail("nonmonotone A/R exponent in c8 inventory")

    base = load(BASE, "d1_c2_c8_source_base")
    check(base.PINS)
    v1 = base.load_v1()
    check(v1.EXPECTED)
    tails = json.loads(v1.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != v1.EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")
    tail_base = v1.load_base()

    variables = (
        "z,t,sigma,p,ell1,a1,a0,c1,c0,cc1,cc0,b1,b0,k0,k60,k60_1,k20,"
        "mu2,mu4,mu6,J,lam,ic1,ic0,ik60,ilam,ip,ik0"
    )
    prefix = "C2C8_"
    pp = "(p+2*sigma*ell1)"
    coeffs = base.source_coefficients(
        pp,
        "sigma^8*a1", "sigma^8*a0",
        "sigma^8*(c1+sigma*cc1)", "sigma^8*(c0+sigma*cc0)",
        "sigma^7*b1", "sigma^7*b0",
    )
    loads = {"k10": "k0", "k6": "(k60+sigma*k60_1)", "k2": "k20"}
    targets = {1: "0", 2: "mu2", 3: "0", 4: "mu4", 5: "0", 6: "mu6", 7: "J/4"}
    lines = [
        f"ring RC28={args.characteristic},({variables}),dp;",
        'print("C2C8_SOURCE_HASHES=PASS");',
        f'print("C2C8_PRIMITIVE_COUNT={len(inventory)}");',
        'print("C2C8_PADDED_CENSUS_IDENTICAL=1");',
        'print("C2C8_MONOTONE_A_R_CLOSED_TAIL=1");',
        f"ideal {prefix}Sigma=std(ideal(sigma^25));",
        f"ideal {prefix}Sigma1=std(ideal(sigma));",
        f"ideal {prefix}Sigma27=std(ideal(sigma^27));",
        f"int {prefix}divisible=1; int {prefix}identities=1; int {prefix}targetfree=1;",
    ]
    for row in range(1, 8):
        source = tail_base.tail_text(tails[str(row)], row, coeffs, loads).replace("Lambda", "(sigma^2)")
        full = source if targets[row] == "0" else f"({source})-sigma^{2*(12+row)}*({targets[row]})"
        lines += [
            f"poly {prefix}SourcePhi{row}={source};",
            f"poly {prefix}FullPhi{row}={full};",
            f"if (reduce({prefix}SourcePhi{row},{prefix}Sigma)!=0) {{ {prefix}divisible=0; }}",
            f"poly {prefix}Q25_{row}={prefix}SourcePhi{row}/sigma^25;",
            f"if (sigma^25*{prefix}Q25_{row}-{prefix}SourcePhi{row}!=0) {{ {prefix}identities=0; }}",
            f"poly {prefix}g25_{row}=subst({prefix}Q25_{row},sigma,0);",
            f"poly {prefix}Rem26_{row}={prefix}Q25_{row}-{prefix}g25_{row};",
            f"if (reduce({prefix}Rem26_{row},{prefix}Sigma1)!=0) {{ {prefix}identities=0; }}",
            f"poly {prefix}Q26_{row}={prefix}Rem26_{row}/sigma;",
            f"if (sigma*{prefix}Q26_{row}-{prefix}Rem26_{row}!=0) {{ {prefix}identities=0; }}",
            f"poly {prefix}g26_{row}=subst({prefix}Q26_{row},sigma,0);",
            f"if (reduce({prefix}FullPhi{row}-{prefix}SourcePhi{row},{prefix}Sigma27)!=0) {{ {prefix}targetfree=0; }}",
        ]

    lines += [
        f"poly {prefix}sp=p/2+sigma*ell1;",
        f"poly {prefix}Inv1=1-{prefix}sp*t^2+{prefix}sp^2*t^4-{prefix}sp^3*t^6+{prefix}sp^4*t^8;",
        f"poly {prefix}Inv2=1-2*{prefix}sp*t^2+3*{prefix}sp^2*t^4-4*{prefix}sp^3*t^6+5*{prefix}sp^4*t^8;",
        f"poly {prefix}Inv3=1-3*{prefix}sp*t^2+6*{prefix}sp^2*t^4-10*{prefix}sp^3*t^6+15*{prefix}sp^4*t^8;",
    ]
    Aseries = "sigma^8*(a1+a0*t)"
    Cseries = "sigma^8*((c1+c0*t)+sigma*(cc1+cc0*t))"
    Rseries = "sigma^7*(b1+b0*t)"
    hshift = base.universal_hshift(Aseries, Cseries, Rseries, "k0",
                                  f"{prefix}Inv1", f"{prefix}Inv2", f"{prefix}Inv3")
    hshift += (
        f"+(3/4)*sigma^17*t^2*(k60+sigma*k60_1)*({Cseries})*({prefix}Inv1)"
    )
    base.analytic_extract(lines, prefix, hshift, 25, 26)
    base.row_checks(lines, prefix, v1, 25, 26)

    literal25 = ",".join(f"{prefix}g25_{row}" for row in range(1, 8))
    lines += [
        f"poly {prefix}L=z^2+p/2;",
        f"poly {prefix}A=a1*z+a0; poly {prefix}C=c1*z+c0;",
        f"poly {prefix}Cnext=cc1*z+cc0; poly {prefix}R=b1*z+b0;",
        f"poly {prefix}N1={prefix}h25_1*z+{prefix}h25_2;",
        f"poly {prefix}N1Expected=(3/4)*k60*{prefix}C;",
        f"int {prefix}n1exact=({prefix}N1-{prefix}N1Expected==0);",
        f"int {prefix}rec1=({prefix}h25_3+(p/2)*{prefix}h25_1==0",
        f" && {prefix}h25_4+(p/2)*{prefix}h25_2==0",
        f" && {prefix}h25_5+(p/2)*{prefix}h25_3==0",
        f" && {prefix}h25_6+(p/2)*{prefix}h25_4==0",
        f" && {prefix}h25_7+(p/2)*{prefix}h25_5==0);",
        f"ideal {prefix}DkDc1=std(ideal({literal25},ik60*k60-1,ic1*c1-1,ip*p-1,ik0*k0-1));",
        f"ideal {prefix}DkVc1Dc0=std(ideal({literal25},c1,ik60*k60-1,ic0*c0-1,ip*p-1,ik0*k0-1));",
        f"int {prefix}openunits=(reduce(1,{prefix}DkDc1)==0 && reduce(1,{prefix}DkVc1Dc0)==0);",
        f"poly {prefix}N2={prefix}h26_1*z^3+{prefix}h26_2*z^2",
        f" +({prefix}h26_3+p*{prefix}h26_1)*z+({prefix}h26_4+p*{prefix}h26_2);",
        f"poly {prefix}N2Expected=(3/4)*{prefix}A*{prefix}C*{prefix}L",
        f" +(3/8)*{prefix}C^2+(5/8)*k0*{prefix}R*{prefix}C*{prefix}L",
        f" +(3/4)*(k60_1*{prefix}C+k60*{prefix}Cnext)*{prefix}L",
        f" -(3/4)*ell1*k60*{prefix}C;",
        f"ideal {prefix}L2=std(ideal({prefix}L^2));",
        f"poly {prefix}OrdinaryQuotient=({prefix}N2Expected-{prefix}N2)/({prefix}L^2);",
        f"int {prefix}common=(reduce({prefix}N2-{prefix}N2Expected,{prefix}L2)==0",
        f" && {prefix}N2+({prefix}L^2)*{prefix}OrdinaryQuotient-{prefix}N2Expected==0);",
        f"int {prefix}rec2=({prefix}h26_5+p*{prefix}h26_3+((p^2)/4)*{prefix}h26_1==0",
        f" && {prefix}h26_6+p*{prefix}h26_4+((p^2)/4)*{prefix}h26_2==0",
        f" && {prefix}h26_7+p*{prefix}h26_5+((p^2)/4)*{prefix}h26_3==0);",
        f"int {prefix}jets=(diff({prefix}N2,k60_1)!=0 && diff({prefix}N2,cc1)!=0",
        f" && diff({prefix}N2,cc0)!=0 && diff({prefix}N2,ell1)!=0);",
        f"int {prefix}connection=(diff({prefix}N2,ell1)+(3/4)*k60*{prefix}C==0);",
        f"poly {prefix}NoConnection={prefix}N2Expected+(3/4)*ell1*k60*{prefix}C;",
        f"int {prefix}omitconnection=(reduce({prefix}N2-{prefix}NoConnection,{prefix}L2)!=0);",
        f"poly {prefix}PsiPlus={prefix}g26_4+lam*({prefix}g26_3+(p/4)*{prefix}g26_1);",
        f"poly {prefix}PsiMinus={prefix}g26_4-lam*({prefix}g26_3+(p/4)*{prefix}g26_1);",
        f"poly {prefix}NPlus=subst({prefix}N2,z,lam); poly {prefix}NMinus=subst({prefix}N2,z,-lam);",
        f"{prefix}PsiPlus=subst({prefix}PsiPlus,p,-2*lam^2);",
        f"{prefix}PsiMinus=subst({prefix}PsiMinus,p,-2*lam^2);",
        f"{prefix}NPlus=subst({prefix}NPlus,p,-2*lam^2);",
        f"{prefix}NMinus=subst({prefix}NMinus,p,-2*lam^2);",
        f"poly {prefix}RootGapPlus={prefix}PsiPlus-{prefix}NPlus;",
        f"poly {prefix}RootGapMinus={prefix}PsiMinus-{prefix}NMinus;",
        f"int {prefix}movingrootgap=({prefix}RootGapPlus!=0 || {prefix}RootGapMinus!=0);",
        f"poly {prefix}Cp=lam*c1+c0; poly {prefix}Cm=-lam*c1+c0;",
        f"poly {prefix}ClosedPlus=subst({prefix}PsiPlus,k60,0);",
        f"poly {prefix}ClosedMinus=subst({prefix}PsiMinus,k60,0);",
        f"poly {prefix}ClosedNPlus=subst({prefix}NPlus,k60,0);",
        f"poly {prefix}ClosedNMinus=subst({prefix}NMinus,k60,0);",
        f"int {prefix}rootfaber=({prefix}ClosedPlus-{prefix}ClosedNPlus==0",
        f" && {prefix}ClosedMinus-{prefix}ClosedNMinus==0);",
        f"int {prefix}rootsquares=({prefix}ClosedPlus-(3/8)*{prefix}Cp^2==0",
        f" && {prefix}ClosedMinus-(3/8)*{prefix}Cm^2==0);",
        f"ideal {prefix}VkDc1=std(ideal(k60,{prefix}PsiPlus,{prefix}PsiMinus,ic1*c1-1,ilam*lam-1,ik0*k0-1));",
        f"ideal {prefix}VkVc1Dc0=std(ideal(k60,c1,{prefix}PsiPlus,{prefix}PsiMinus,ic0*c0-1,ilam*lam-1,ik0*k0-1));",
        f"int {prefix}closedunits=(reduce(1,{prefix}VkDc1)==0 && reduce(1,{prefix}VkVc1Dc0)==0);",
        f"poly {prefix}NoC2={prefix}N2Expected-(3/8)*{prefix}C^2;",
        f"poly {prefix}NoPlus=subst(subst(subst({prefix}NoC2,k60,0),z,lam),p,-2*lam^2);",
        f"poly {prefix}NoMinus=subst(subst(subst({prefix}NoC2,k60,0),z,-lam),p,-2*lam^2);",
        f"int {prefix}omitc2=({prefix}NoPlus==0 && {prefix}NoMinus==0);",
        f"int {prefix}endpoint={prefix}divisible*{prefix}identities*{prefix}targetfree",
        f"*{prefix}analyticDiv*{prefix}row25*{prefix}row26*{prefix}n1exact*{prefix}rec1",
        f"*{prefix}openunits*{prefix}common*{prefix}rec2*{prefix}jets*{prefix}connection",
        f"*{prefix}omitconnection*{prefix}movingrootgap*{prefix}rootfaber",
        f"*{prefix}rootsquares*{prefix}closedunits*{prefix}omitc2;",
        f'print("C2C8_SOURCE_DIVISIBLE="+string({prefix}divisible));',
        f'print("C2C8_SOURCE_QUOTIENTS="+string({prefix}identities));',
        f'print("C2C8_TARGETFREE_THROUGH_G26="+string({prefix}targetfree));',
        f'print("C2C8_ANALYTIC_EXACT="+string({prefix}analyticDiv));',
        f'print("C2C8_ALL_SEVEN_ROWS_G25="+string({prefix}row25));',
        f'print("C2C8_ALL_SEVEN_ROWS_G26="+string({prefix}row26));',
        f'print("C2C8_G25_K60_C_EXACT="+string({prefix}n1exact*{prefix}rec1));',
        f'print("C2C8_D_K60_BOTH_C_CHARTS_UNIT="+string({prefix}openunits));',
        f'print("C2C8_G26_COMMON_N2="+string({prefix}common*{prefix}rec2));',
        f'print("C2C8_ALL_NEXT_JETS_ENTER="+string({prefix}jets));',
        f'print("C2C8_CONNECTION_MINUS3_OVER4="+string({prefix}connection));',
        f'print("C2C8_OMIT_CONNECTION_REJECTED="+string({prefix}omitconnection));',
        f'print("C2C8_UNCONDITIONAL_MOVING_ROOT_GAP_NONZERO="+string({prefix}movingrootgap));',
        f'print("C2C8_ROOT_FABER="+string({prefix}rootfaber));',
        f'print("C2C8_V_K60_ROOT_SQUARES="+string({prefix}rootsquares));',
        f'print("C2C8_V_K60_BOTH_C_CHARTS_UNIT="+string({prefix}closedunits));',
        f'print("C2C8_OMIT_C2_ROOTS_ZERO="+string({prefix}omitc2));',
        f'if ({prefix}endpoint!=1) {{ print("C2C8_FAIL=SOURCE_CONNECTION_OR_CHART"); quit; }}',
        'print("C2C8_EXACT_C_CHART_COVER=1");',
        'print("C2C8_ENDPOINT=PASS_EMPTY_PRIMARY_C2_C8_CLOSED_A_R_TAIL");',
        "quit;",
    ]

    output = args.output.resolve()
    if output.exists():
        fail("D1 C2 c8 output already exists")
    output.mkdir(parents=True)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    target = output / f"square_d1_c2_c8_connection_{label}.sing"
    target.write_text("\n".join(lines) + "\n")
    payload = {
        "status": "COMPILED-D1-C2-C8-K6-CONNECTION-SPLIT",
        "scope": "C_EQ_8_A_GE_8_R_GE_7_ON_D_P_K0_ONLY",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "primitive_count": len(inventory),
        "primitive_inventory": inventory,
        "maximum_grade": 26,
        "input_sha256": digest(target),
    }
    (output / "source_inventory.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
