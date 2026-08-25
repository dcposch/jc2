#!/usr/bin/env python3
"""Lightweight custody, ancestry-marker, and strict-scope gate for V66."""

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent
EXPECTED = {
    "archives/td6-aws-handoff-20260825-v66.tar.gz":
        "dbb97927b097cf2eb5876f782c2b94cfc8b2830b07fe4db288db8aa13fdfbfe6",
    "aws_box02/v66.stdout":
        "c7c3342a5e0efcc790b35719b3d3fbc6ca775de727285b9e60b586adc697edf4",
    "aws_box02/v66.stderr":
        "0ab846e6ca67ecf0ccc572584d770b5440c5c3eb313af2094e5e72212b7079e7",
    "aws_r6d/v66.stdout":
        "263418670de0a9ad02f495e1a45e125f29495ada12776751f50830c3348e68e7",
    "aws_r6d/v66.stderr":
        "2a70b90df2becf8ed9c272c7e8b2145c0bd4de743b826228090a2d5bcce01927",
}

for relative, expected in EXPECTED.items():
    got = sha256((HERE / relative).read_bytes()).hexdigest()
    assert got == expected, (relative, got, expected)

for host in ("aws_box02", "aws_r6d"):
    assert (HERE / host / "rc").read_text() == "0\n"
    assert (HERE / host / "archive.sha256").read_text().strip() == EXPECTED[
        "archives/td6-aws-handoff-20260825-v66.tar.gz"
    ]

    out = (HERE / host / "v66.stdout").read_text()
    for marker in (
        "B3_parameter_open_requires=t*w*(t-2)!=0",
        "arbitrary_degree_original_rows_preserved=true",
        "N13_equals_k_beta_over_25=true",
        "N13_previous_edge_keys=[('X-1', 14)]",
        "quadratic_control_is_not_N13_edge=true",
        "N13_previous_edge_14_omission_negative_control=true",
        "N13_singleton_current_row_omission_negative_control=true",
        "genuine_P12_term_count_control=2893",
        "P12_first_nonzero_rows=28",
        "P12_first_multiplier_terms=1649",
        "P12_first_original_row_replay=true",
        "P12_without_N13_live_source_object_negative_control=true",
        "combined_unit_residual_is_minus_k_over_50=true",
        "DAG_leaf_denominator_factor_set=['2*C - 1', 'C', 'C - 2', "
        "'C^2 - 4*C + 2', 'V']",
        "raw_denominator_factor_strata_still_charged=true",
        "whole_raw_stratum_killed=false",
        "TD6-A3-Q2-B3-SOURCE-DAG-REPAIRED-V66 PASS",
    ):
        assert marker in out, (host, marker)

for name, expected in (
    ("DAG_LEAF_DENOMINATORS.tsv",
     "fc655dea4b85f836d7372f1b7c6e34835b8403d0b755a154c82911dfff605b7e"),
    ("N13_PROOF_DAG.txt",
     "3751f623e2f60e899f0214e2151e6a2f5923ee2d6a07a9b9424dd87a2877def8"),
):
    values = []
    for host in ("aws_box02", "aws_r6d"):
        data = (HERE / host / "artifacts" / name).read_bytes()
        values.append(data)
        assert sha256(data).hexdigest() == expected
    assert values[0] == values[1]

print("TD6-V66-B3-REPAIRED-SOURCE-DAG-CUSTODY PASS")
print("exact_scope=B3_zero_birational_D(t*w*(t-2)*(2t-1)*(t2-4t+2))")
print("whole_B3_cover_complete=false")
