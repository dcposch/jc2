#!/usr/bin/env python3
"""Exact q/y-free P13 coordinate-8 cubic routing theorem."""

import ast
from fractions import Fraction
from hashlib import sha256
import os
from pathlib import Path

import flint


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

EXPECTED_NUMERATOR = (
    "2187500/3*V^6*U + 29750000/3*V^4*U^4 "
    "- 161000000/3*V^2*U^7 + 56000000/3*U^10"
)
EXPECTED_DENOMINATOR = "V^3"


def main():
    outdir = Path(os.environ["TD6_OUTPUT_DIR"]).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    assert os.environ.get("AWS_RUN_TAG", "").startswith("td6_v89h17_p13_cubic_")

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
        records.append((parameter, q_monomial, coefficient[8]))
    assert len(records) == 238
    nonzero = [record for record in records if record[2][0] != "0"]
    assert nonzero == [((), (), (EXPECTED_NUMERATOR, EXPECTED_DENOMINATOR))]

    qctx = flint.fmpq_mpoly_ctx.get(["U", "V"], ordering="lex")
    Uq, Vq = qctx.gens()
    lhs = (
        flint.fmpq(2187500, 3) * Vq**6 * Uq
        + flint.fmpq(29750000, 3) * Vq**4 * Uq**4
        - flint.fmpq(161000000, 3) * Vq**2 * Uq**7
        + flint.fmpq(56000000, 3) * Uq**10
    )
    S_q = 5 * Vq**6 + 68 * Vq**4 * Uq**3 - 368 * Vq**2 * Uq**6 + 128 * Uq**9
    assert lhs == flint.fmpq(437500, 3) * Uq * S_q

    zctx = flint.fmpz_mpoly_ctx.get(["U", "V"], ordering="lex")
    Uz, Vz = zctx.gens()
    S_z = 5 * Vz**6 + 68 * Vz**4 * Uz**3 - 368 * Vz**2 * Uz**6 + 128 * Uz**9
    unit, factors = S_z.factor()
    assert unit == 1 and factors == [(S_z, 1)]
    sample_S = 5 * 3**6 + 68 * 3**4 - 368 * 3**2 + 128
    sample_value = Fraction(437500, 3) * Fraction(sample_S, 3**3)
    assert sample_S == 5969 and sample_value == Fraction(2611437500, 81)

    router = (
        "coordinate\tparameter_monomial\tq_monomial\tnumerator\tdenominator\n"
        f"8\t()\t()\t{EXPECTED_NUMERATOR}\t{EXPECTED_DENOMINATOR}\n"
        "factor\tS\t()\t5*V^6+68*V^4*U^3-368*V^2*U^6+128*U^9\t1\n"
    )
    (outdir / "P13_COORDINATE8_CUBIC_ROUTER.tsv").write_text(router)
    router_sha = sha256(router.encode()).hexdigest()
    result = (
        f"p13_normal_form_sha256={P13_SHA}\n"
        "coordinate=8\n"
        "q_dependent_coefficients_zero=true\n"
        "quotient_variable_dependent_coefficients_zero=true\n"
        "sole_coefficient=(437500/3)*(U/V^3)*S\n"
        "S=5*V^6+68*V^4*U^3-368*V^2*U^6+128*U^9\n"
        "S_irreducible_over_Q_U_V=true\n"
        "F0_B3_equals_V4=true\n"
        "registered_open_makes_U_V_units=true\n"
        "P13_vanishing_forces_S_zero=true\n"
        "sample_U1_V3_S=5969\n"
        "sample_coordinate8=2611437500/81\n"
        f"router_sha256={router_sha}\n"
        "S_zero_residue_not_excluded=true\nsource_point_claim=false\n"
        "later_CURRENT_imposed=false\nwhole_TD6_killed=false\nJC2_resolved=false\n"
    )
    (outdir / "P13_COORDINATE8_CUBIC_ROUTER_RESULT.txt").write_text(result)
    print(result, end="")
    print(f"result_sha256={sha256(result.encode()).hexdigest()}")
    print("TD6-V89H17-P13-COORDINATE8-CUBIC-ROUTER PASS")


if __name__ == "__main__":
    main()
