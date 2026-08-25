#!/usr/bin/env python3
"""Lightweight custody, repaired-ancestry, and scope verifier for V64."""

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent
EXPECTED = {
    "archives/td6-aws-handoff-20260825-v64.tar.gz":
        "1a2e4f6766ffe5b15b963dd6ac86c02d538eb3e6d45b27d4a5a99e3c87a7aac6",
    "aws_r6d/v64.stdout":
        "14775e9ad4adfb0a20512823be01bdd48da711e30b8ac7796e094841f41edd06",
    "aws_r6d/v64.stderr":
        "7660d509151d4ce1828123a00f592fd5c91919294b7c04ff973c3f99e7be9226",
    "aws_r6d/source-check.txt":
        "99f932613dcc6e55507212d903de2e87c64a83550a0f6750c85cf5d76a9d4a1a",
    "aws_r6d/artifacts/DAG_LEAF_DENOMINATORS.tsv":
        "259605ae41d2743d7f4280d4f7879d6c16b915a5ce0117a974366e9cc594b385",
    "aws_r6d/artifacts/N13_PROOF_DAG.txt":
        "ef721416a7aac4f97167003801bfe94033e0b6627942d4ba9269c5565d9a962e",
}

for relative, expected in EXPECTED.items():
    got = sha256((HERE / relative).read_bytes()).hexdigest()
    assert got == expected, (relative, got, expected)

assert (HERE / "aws_r6d/rc").read_text() == "0\n"
out = (HERE / "aws_r6d/v64.stdout").read_text()
for marker in (
    "arbitrary_degree_original_rows_preserved=true",
    "N13_equals_k_beta_over_25=true",
    "N13_previous_edge_keys=[('X-1', 14)]",
    "quadratic_source_positive_control_key=('X-1', 0)",
    "quadratic_control_is_not_N13_edge=true",
    "N13_previous_edge_14_omission_negative_control=true",
    "N13_singleton_current_row_omission_negative_control=true",
    "N13_full_first_previous_current_source_identity_exact_by_DAG=true",
    "genuine_P12_term_count_control=2885",
    "P12_first_original_row_replay=true",
    "P12_first_nonzero_rows=28",
    "P12_first_multiplier_terms=1640",
    "P12_without_N13_live_source_object_negative_control=true",
    "combined_unit_residual_is_minus_k_over_50=true",
    "k_coordinate_denominator_factor_set=[]",
    "DAG_leaf_denominator_factor_set=['U', 'V', "
    "'V^4 + 8*V^2*U^3 - 64*U^6', "
    "'V^4 - 32*V^2*U^3 + 128*U^6']",
    "raw_denominator_factor_strata_still_charged=true",
    "whole_raw_stratum_killed=false",
    "TD6-A3-Q2-H-SOURCE-DAG-REPAIRED-V64 PASS",
):
    assert marker in out, marker

dag = (HERE / "aws_r6d/artifacts/N13_PROOF_DAG.txt").read_text()
for marker in (
    "current_row_index=13",
    "N13_previous_edge_keys=[('X-1', 14)]",
    "quadratic_control_key=('X-1', 0)",
    "quadratic_control_is_not_N13_edge=true",
    "P12_minus_multiplier_times_N13_equals_minus_k_over_50=true",
):
    assert marker in dag, marker

ledger = (HERE / "aws_r6d/artifacts/DAG_LEAF_DENOMINATORS.tsv").read_text()
assert "V^4 + 8*V^2*U^3 - 64*U^6" in ledger
assert "V^4 - 32*V^2*U^3 + 128*U^6" in ledger

print("TD6-V64-H-REPAIRED-SOURCE-DAG-CUSTODY PASS")
print("exact_scope=H_zero_intersect_D(U*V*P3*QH)_inside_fixed_A3_q2_beta")
print("whole_H_cover_complete=false")
