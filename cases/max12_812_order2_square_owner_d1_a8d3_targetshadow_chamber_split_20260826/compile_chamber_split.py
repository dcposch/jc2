#!/usr/bin/env python3
"""Compile literal odd-row a8d3 target-shadow split; AWS only."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PARENT_DIR = ROOT / "cases/max12_812_order2_square_owner_d1_d23_a8a9_j38_r3_tail_20260826"
PARENTS = {
    0: PARENT_DIR / "aws_v2_failed_a8d3_q_box02_highmem/evidence/compiled/square_d1_a8d3_j38_r3_q.sing",
    65519: PARENT_DIR / "aws_v2_failed_a8d3_p65519_box03_highmem/evidence/compiled/square_d1_a8d3_j38_r3_p65519.sing",
    65521: PARENT_DIR / "aws_v2_failed_a8d3_p65521_r6d_highmem/evidence/compiled/square_d1_a8d3_j38_r3_p65521.sing",
}
INVENTORY = PARENT_DIR / "aws_v2_failed_a8d3_q_box02_highmem/evidence/compiled/source_inventory.json"
FAILED_RESULT = PARENT_DIR / "RESULT_A8D3_G38_ROUTE_FAILED.md"
CONNECTION_RESULT = ROOT / "cases/max12_812_order2_square_owner_d1_a8d3_k6rc_isolated_bridge_20260826/RESULT.md"
RANKJUMP_FREEZE = ROOT / "cases/max12_812_order2_square_owner_d1_a8d3_connection_rankjump_20260826/PRODUCER_FREEZE.sha256"
PINS = {
    PARENTS[0]: "77c38a24304af28e2a80c495abda486a38b17f1085d7be3f6dd0ece84815c6d6",
    PARENTS[65519]: "72b01773d67d32db1b78668229bdc05db2b2c2c3041e75e386b8dee22444ce08",
    PARENTS[65521]: "8575b38bf2bd106d6a03b0a04325f61ce3a02bf692ce98211cb6febc82d3ce9f",
    INVENTORY: "de195a2a005c32a53c3802dc1ee5f8429bb94a7337543d4f1419be5ad4c14cf6",
    FAILED_RESULT: "3a3e8ec967dafc26d05788930de1ddaad19a77f9d2cc2c5e93bacd5632b1304e",
    CONNECTION_RESULT: "64f731aa4a518b467d2b60489643178c2e6f0c069b7f9c0a568ae685f9378ba2",
    RANKJUMP_FREEZE: "a28e20033d4e0d5cd8fd3303a371d802147db65875cace445904a48f9f4fc83e",
}
PREFIX = "D1A8D3J38R3"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def definition(lines: list[str], name: str) -> str:
    start = f"poly {name}="
    found = [line for line in lines if line.startswith(start)]
    if len(found) != 1 or not found[0].endswith(";"):
        fail(("nonunique/malformed frozen definition", name, len(found)))
    return found[0]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65519, 65521), required=True)
    args = parser.parse_args()
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if platform.system() != "Linux" or not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2" or not tag:
        fail("AWS-only chamber compiler refused unregistered/non-EC2 host")
    for path, expected in PINS.items():
        actual = digest(path)
        if actual != expected:
            fail(("frozen pin mismatch", str(path), actual, expected))

    inventory = json.loads(INVENTORY.read_text())
    if inventory.get("baseline") != {"A": 8, "C": 11, "R": 8}:
        fail("a8d3 inventory baseline mismatch")
    if inventory.get("maximum_grade") != 38 or inventory.get("primitive_family_count") != 17:
        fail("a8d3 complete inventory markers mismatch")
    if not any(item == {"row": 7, "grade": 38, "variable": "J", "coefficient": "-1/4"}
               for item in inventory.get("targets", [])):
        fail("terminal J target absent from frozen inventory")

    parent = PARENTS[args.characteristic]
    parent_lines = parent.read_text().splitlines()
    if not parent_lines or not parent_lines[0].startswith(f"ring R={args.characteristic},("):
        fail("parent ring characteristic mismatch")
    ring = parent_lines[0]
    old_tail = ",J,iJ),dp;"
    if old_tail not in ring:
        fail("cannot extend frozen ring by inverse variables")
    ring = ring.replace(old_tail, ",J,iJ,ip,ik0,ic1,ic0),dp;")
    source_definitions = [definition(parent_lines, f"{PREFIX}_SourcePhi{row}") for row in (1, 3, 5, 7)]

    pp = "p" + "".join(f"+2*sigma^{index}*ell{index}" for index in range(1, 11))
    source_relation = (
        f"{PREFIX}_SourcePhi7+(({pp})/4)*{PREFIX}_SourcePhi5"
        f"+(3*(({pp})^2)/32)*{PREFIX}_SourcePhi3"
        f"+(5*(({pp})^3)/128)*{PREFIX}_SourcePhi1"
    )
    lines = [
        ring,
        'print("A8D3_SHADOW_SOURCE_HASHES=PASS");',
        'print("A8D3_SHADOW_LITERAL_ODD_ROWS_IMPORTED=4");',
        *source_definitions,
        f"ideal {PREFIX}_Zero=std(ideal(0));",
        f"ideal {PREFIX}_S28=std(ideal(sigma^28));",
        f"ideal {PREFIX}_S38=std(ideal(sigma^38));",
        f"ideal {PREFIX}_S39=std(ideal(sigma^39));",
        f"int {PREFIX}_row1div28=(reduce({PREFIX}_SourcePhi1,{PREFIX}_S28)==0);",
        f"poly {PREFIX}_row1q28={PREFIX}_SourcePhi1/sigma^28;",
        f"int {PREFIX}_row1quot=(reduce(sigma^28*{PREFIX}_row1q28-{PREFIX}_SourcePhi1,{PREFIX}_Zero)==0);",
        f"poly {PREFIX}_row1lead=subst({PREFIX}_row1q28,sigma,0);",
        f"int {PREFIX}_row1exact=(reduce({PREFIX}_row1lead-(3/4)*k60*c1,{PREFIX}_Zero)==0);",
        f"poly {PREFIX}_source_rel={source_relation};",
        f"int {PREFIX}_source_div38=(reduce({PREFIX}_source_rel,{PREFIX}_S38)==0);",
        f"poly {PREFIX}_source_q38={PREFIX}_source_rel/sigma^38;",
        f"int {PREFIX}_source_quot=(reduce(sigma^38*{PREFIX}_source_q38-{PREFIX}_source_rel,{PREFIX}_Zero)==0);",
        f"poly {PREFIX}_source_coeff=subst({PREFIX}_source_q38,sigma,0);",
        f"int {PREFIX}_residual_exact=(reduce({PREFIX}_source_coeff+(3/32)*p*eta*k60*c1*b0,{PREFIX}_Zero)==0);",
        f"ideal {PREFIX}_Bk60=std(ideal(sigma^39,k60));",
        f"ideal {PREFIX}_Bc1=std(ideal(sigma^39,c1));",
        f"int {PREFIX}_branch_k60=(reduce({PREFIX}_source_rel,{PREFIX}_Bk60)==0);",
        f"int {PREFIX}_branch_c1=(reduce({PREFIX}_source_rel,{PREFIX}_Bc1)==0);",
        f"poly {PREFIX}_full_rel={PREFIX}_source_rel-sigma^38*J/4;",
        f"int {PREFIX}_full_div38=(reduce({PREFIX}_full_rel,{PREFIX}_S38)==0);",
        f"poly {PREFIX}_full_q38={PREFIX}_full_rel/sigma^38;",
        f"int {PREFIX}_full_quot=(reduce(sigma^38*{PREFIX}_full_q38-{PREFIX}_full_rel,{PREFIX}_Zero)==0);",
        f"poly {PREFIX}_full_coeff=subst({PREFIX}_full_q38,sigma,0);",
        f"int {PREFIX}_target_exact=(reduce({PREFIX}_full_coeff-{PREFIX}_source_coeff+J/4,{PREFIX}_Zero)==0);",
        f"ideal {PREFIX}_OpenUnit=std(ideal({PREFIX}_row1lead,{PREFIX}_full_coeff,ic1*c1-1,ip*p-1,ik0*k0-1,iJ*J-1));",
        f"ideal {PREFIX}_ClosedUnit=std(ideal(c1,{PREFIX}_full_coeff,ic0*c0-1,ip*p-1,ik0*k0-1,iJ*J-1));",
        f"int {PREFIX}_open_unit=(reduce(1,{PREFIX}_OpenUnit)==0);",
        f"int {PREFIX}_closed_unit=(reduce(1,{PREFIX}_ClosedUnit)==0);",
        f"int {PREFIX}_endpoint={PREFIX}_row1div28*{PREFIX}_row1quot*{PREFIX}_row1exact*{PREFIX}_source_div38*{PREFIX}_source_quot*{PREFIX}_residual_exact*{PREFIX}_branch_k60*{PREFIX}_branch_c1*{PREFIX}_full_div38*{PREFIX}_full_quot*{PREFIX}_target_exact*{PREFIX}_open_unit*{PREFIX}_closed_unit;",
        f'print("A8D3_SHADOW_ROW1_G28_K60_C1="+string({PREFIX}_row1div28*{PREFIX}_row1quot*{PREFIX}_row1exact));',
        f'print("A8D3_SHADOW_SOURCE_RESIDUAL_MINUS3P_OVER32="+string({PREFIX}_source_div38*{PREFIX}_source_quot*{PREFIX}_residual_exact));',
        f'print("A8D3_SHADOW_D_C1_BRANCH_SOURCE_ZERO="+string({PREFIX}_branch_k60));',
        f'print("A8D3_SHADOW_V_C1_D_C0_BRANCH_SOURCE_ZERO="+string({PREFIX}_branch_c1));',
        f'print("A8D3_SHADOW_TERMINAL_J_TARGET_EXACT="+string({PREFIX}_full_div38*{PREFIX}_full_quot*{PREFIX}_target_exact));',
        f'print("A8D3_SHADOW_D_C1_UNIT="+string({PREFIX}_open_unit));',
        f'print("A8D3_SHADOW_V_C1_D_C0_UNIT="+string({PREFIX}_closed_unit));',
        'print("A8D3_SHADOW_EXACT_C_CHART_COVER=1");',
        f'if ({PREFIX}_endpoint!=1) {{ print("A8D3_SHADOW_FAIL=CHAMBER_OR_TARGET"); quit; }}',
        'print("A8D3_SHADOW_ENDPOINT=PASS_EMPTY_A8_D3_C11_RGE8_ON_D_PK0J");',
        "quit;",
    ]
    output = args.output.resolve()
    if output.exists():
        fail("chamber output already exists")
    output.mkdir(parents=True)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    singular = output / f"square_d1_a8d3_targetshadow_{label}.sing"
    singular.write_text("\n".join(lines) + "\n")
    result = {
        "status": "COMPILED-D1-A8D3-TARGETSHADOW-CHAMBER-SPLIT",
        "scope": "A8_D3_C11_R_GE_8_ON_D_P_K0_J_ONLY",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "parent_literal_input_sha256": digest(parent),
        "input_sha256": digest(singular),
        "primitive_family_count": 17,
        "maximum_grade": 38,
    }
    (output / "result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
