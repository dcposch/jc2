#!/usr/bin/env python3
"""AWS-only exact rank-jump adjudication for the a8d3 grade-38 collision."""

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
INVENTORY = ROOT / "cases/max12_812_order2_square_owner_d1_d23_a8a9_j38_r3_tail_20260826/aws_v2_failed_a8d3_q_box02_highmem/evidence/compiled/source_inventory.json"
DIAGNOSTIC_RESULT = ROOT / "cases/max12_812_order2_square_owner_d1_a8d3_k6rc_isolated_bridge_20260826/RESULT.md"
DIAGNOSTIC_FREEZE = ROOT / "cases/max12_812_order2_square_owner_d1_a8d3_k6rc_isolated_bridge_20260826/DIAGNOSTIC_FREEZE.sha256"
PINS = {
    INVENTORY: "de195a2a005c32a53c3802dc1ee5f8429bb94a7337543d4f1419be5ad4c14cf6",
    DIAGNOSTIC_RESULT: "64f731aa4a518b467d2b60489643178c2e6f0c069b7f9c0a568ae685f9378ba2",
    DIAGNOSTIC_FREEZE: "84262c311e3a7944ba945df630bfb254a0d838a9c0065098295835cb64db80ab",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def mod_fraction(value: Fraction, prime: int) -> int:
    return (value.numerator % prime) * pow(value.denominator % prime, -1, prime) % prime


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65519, 65521), required=True)
    args = parser.parse_args()
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if platform.system() != "Linux" or not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2" or not tag:
        fail("AWS-only rank-jump client refused unregistered/non-EC2 host")
    for path, expected in PINS.items():
        actual = digest(path)
        if actual != expected:
            fail(("frozen pin mismatch", str(path), actual, expected))
    data = json.loads(INVENTORY.read_text())
    families = data["primitive_families"]
    expected15 = {"name": "k6", "load": "k6", "fixed_sigma": 22,
                  "R": 0, "A": 2, "C": 0, "pole": 3,
                  "base_grade": 38, "coefficient": "-3/32"}
    expected16 = {"name": "k6", "load": "k6", "fixed_sigma": 19,
                  "R": 1, "A": 0, "C": 1, "pole": 3,
                  "base_grade": 38, "coefficient": "-3/8"}
    if families[15] != expected15 or families[16] != expected16:
        fail("family 15/16 inventory mismatch")
    entries15 = {
        (int(item["row"]), tuple(item["variables"])): Fraction(item["coefficient"])
        for item in data["literal_faber_source_monomials"]
        if int(item["family"]) == 15 and int(item["grade"]) == 38
    }
    a_row5 = entries15.get((5, ("a0", "a1", "k60")))
    a_row7 = entries15.get((7, ("a0", "a1", "k60", "p")))
    if (a_row5, a_row7) != (Fraction(-3, 16), Fraction(3, 64)):
        fail(("k6A2 cross column mismatch", a_row5, a_row7))

    # Independently adjudicated moving-inverse-root k6RC column.
    rc_row5 = Fraction(-3, 16)
    rc_row7 = Fraction(-3, 64)
    alpha_a2 = -a_row7 / a_row5
    alpha_rc = -rc_row7 / rc_row5
    determinant_over_p = a_row5 * rc_row7 - rc_row5 * a_row7
    if alpha_a2 != Fraction(1, 4) or alpha_rc != Fraction(-1, 4):
        fail(("forced-alpha control", alpha_a2, alpha_rc))
    if determinant_over_p != Fraction(9, 512):
        fail(("rank-jump determinant", determinant_over_p))

    # Columns are (row5,row7)=(a5,p*a7) and (r5,p*r7).  On D(p),
    # e7=(32/(3p))*A2-(32/(3p))*RC.
    target_a2_coefficient_times_p = Fraction(32, 3)
    target_rc_coefficient_times_p = Fraction(-32, 3)
    row5_check = target_a2_coefficient_times_p * a_row5 + target_rc_coefficient_times_p * rc_row5
    row7_check = target_a2_coefficient_times_p * a_row7 + target_rc_coefficient_times_p * rc_row7
    if row5_check != 0 or row7_check != 1:
        fail(("target span certificate", row5_check, row7_check))

    prime = args.characteristic
    if prime:
        if mod_fraction(determinant_over_p, prime) == 0:
            fail("rank-jump determinant vanished in control field")
        field = f"F_{prime}"
    else:
        field = "Q"
    result = {
        "status": "PASS-A8D3-G38-MOVING-CONNECTION-RANK-JUMP",
        "scope": "NO_UNIVERSAL_NORMALIZED_ODD_FUNCTIONAL_FOR_K6A2_PLUS_CORRECTED_K6RC_ON_D_P",
        "field": field,
        "characteristic": prime,
        "registered_aws_lane": tag,
        "family15_k6A2_cross_rows5_7": ["-3/16", "3*p/64"],
        "family16_corrected_k6RC_cross_rows5_7": ["-3/16", "-3*p/64"],
        "forced_alpha_k6A2": "1/4",
        "forced_alpha_k6RC": "-1/4",
        "determinant": "9*p/512",
        "target_span_certificate": "e7=(32/(3*p))*col(k6A2)-(32/(3*p))*col(k6RC)",
        "firewall": "rank-jump/navigation only; no nonlinear cell or existence verdict",
    }
    output = args.output.resolve()
    if output.exists():
        fail("output already exists")
    output.mkdir(parents=True)
    (output / "result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("A8D3_RANKJUMP_SOURCE_HASHES=PASS")
    print("A8D3_RANKJUMP_ALPHA_A2=1/4")
    print("A8D3_RANKJUMP_ALPHA_RC=-1/4")
    print("A8D3_RANKJUMP_INCOMPATIBLE_ALPHA=1")
    print("A8D3_RANKJUMP_DETERMINANT_OVER_P=9/512")
    print("A8D3_RANKJUMP_TARGET_ROW7_IN_TWO_COLUMN_SPAN_ON_D_P=1")
    print("A8D3_RANKJUMP_ENDPOINT=PASS_NO_UNIVERSAL_ODD_FUNCTIONAL")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
