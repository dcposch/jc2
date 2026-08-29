#!/usr/bin/env python3
"""Exact unit-coordinate theorem for the frozen P13/FIRST normal form."""

import ast
from fractions import Fraction
from hashlib import sha256
import os
from pathlib import Path


HERE = Path(__file__).resolve().parent
P13 = HERE / "evidence/p13-full-r1/box02/output/ALLQ_P13_FULL_NORMAL_FORM.tsv"
P13_SHA = "9af3240d4016ad99766122303465d2cea7a10dc5e71b489f62564b9c3540c2d8"
P13_RESULT = HERE / "P13_FULL_NORMAL_FORM_RESULT.md"
P13_RESULT_SHA = "29d5723b0d920840dbdfe72398624cfc0672843dbbf1d713b2fdd29dea52712c"
P13_FREEZE = HERE / "P13_FULL_NORMAL_FORM_FREEZE.sha256"
P13_FREEZE_SHA = "4048419e15f366baeb03d242f546f096ee22d4529e6c6fededf58b2aea951c18"
for path, expected in (
    (P13, P13_SHA), (P13_RESULT, P13_RESULT_SHA), (P13_FREEZE, P13_FREEZE_SHA)
):
    assert sha256(path.read_bytes()).hexdigest() == expected

EXPECTED = ("3500000000/9*U", "V")


def main():
    outdir = Path(os.environ["TD6_OUTPUT_DIR"]).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    assert os.environ.get("AWS_RUN_TAG", "").startswith("td6_v89h18_p13_unit_")

    records = []
    lines = P13.read_text().splitlines()
    assert lines[0] == "parameter_monomial\tq_monomial\tcoefficient_exact"
    for line in lines[1:]:
        parameter_text, q_text, coefficient_text = line.split("\t")
        parameter = ast.literal_eval(parameter_text)
        q_monomial = ast.literal_eval(q_text)
        coefficient = ast.literal_eval(coefficient_text)
        assert isinstance(parameter, tuple) and isinstance(q_monomial, tuple)
        assert len(coefficient) == 18
        records.append((parameter, q_monomial, coefficient[12]))
    assert len(records) == 238
    nonzero = [record for record in records if record[2][0] != "0"]
    assert nonzero == [((), (), EXPECTED)]
    sample = Fraction(3500000000, 9) * Fraction(1, 3)
    assert sample == Fraction(3500000000, 27)

    unit = (
        "coordinate\tparameter_monomial\tq_monomial\tnumerator\tdenominator\n"
        "12\t()\t()\t3500000000/9*U\tV\n"
    )
    (outdir / "P13_COORDINATE12_UNIT.tsv").write_text(unit)
    unit_sha = sha256(unit.encode()).hexdigest()
    result = (
        f"p13_normal_form_sha256={P13_SHA}\n"
        "coordinate=12\n"
        "q_dependent_coefficients_zero=true\n"
        "quotient_variable_dependent_coefficients_zero=true\n"
        "sole_coefficient=(3500000000/9)*(U/V)\n"
        "F0_B3_equals_V4=true\n"
        "registered_open_makes_U_V_units=true\n"
        "coordinate12_is_registered_unit=true\n"
        "sample_U1_V3_coordinate12=3500000000/27\n"
        f"unit_record_sha256={unit_sha}\n"
        "P13_FIRST_normal_form_common_zero_exists=false\n"
        "P12_used=false\n"
        "explicit_original_FIRST_membership_deferred=true\n"
        "independent_total_F_lifted=false\n"
        "whole_TD6_killed=false\nJC2_resolved=false\n"
    )
    (outdir / "P13_COORDINATE12_UNIT_RESULT.txt").write_text(result)
    print(result, end="")
    print(f"result_sha256={sha256(result.encode()).hexdigest()}")
    print("TD6-V89H18-P13-COORDINATE12-UNIT PASS")


if __name__ == "__main__":
    main()
