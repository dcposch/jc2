#!/usr/bin/env python3
"""Lightweight custody and fail-closed scope verifier for the V60 H stratum."""

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent
EXPECTED = {
    "archives/td6-aws-handoff-20260825-v60.tar.gz":
        "78dae78e0aca67bb6ab81ab234fba52c8116b98614de141db04f4c669db967e5",
    "aws_run/ARCHIVE.sha256":
        "bbbb4572585080dd907b23991a90e553fb69e97e71aad7feb81a434661ade9bb",
    "aws_run/v60.stdout":
        "d029a06d35a16265cbcb6e473b89006d1fe55d993466793a8224c573b95f89cd",
    "aws_run/v60.stderr":
        "91b7c19278e35eef71f28c582708af9cc961a824deac97228dfb9a0bb1905363",
    "aws_run/artifacts/DAG_LEAF_DENOMINATORS.tsv":
        "259605ae41d2743d7f4280d4f7879d6c16b915a5ce0117a974366e9cc594b385",
    "aws_run/artifacts/N13_PROOF_DAG.txt":
        "9516116934a1b3cbde7894f2eeb8010e45b0c1dc4bfd1192ba2e04dd36148ddb",
}

for relative, expected in EXPECTED.items():
    got = sha256((HERE / relative).read_bytes()).hexdigest()
    assert got == expected, (relative, got, expected)

assert (HERE / "aws_run/rc").read_text() == "0\n"
out = (HERE / "aws_run/v60.stdout").read_text()
for marker in (
    "arbitrary_degree_original_rows_preserved=true",
    "raw_center_stratum=h-zero",
    "source_center=C=3U^2 over Q(V,U)",
    "N13_left_null_support=1",
    "current_rows_source_lifted_indices=[13]",
    "previous_rows_source_lifted_keys=[('X-1', 0), ('X-1', 14)]",
    "N13_nested_multiplier_expansion_used=false",
    "N13_one_required_edge_omission_negative_control=true",
    "P12_first_nonzero_rows=28",
    "P12_first_multiplier_terms=1640",
    "P12_old_tail_and_multiplier_objects_exactly_equal=true",
    "P12_without_N13_negative_control=true",
    "combined_unit_residual_is_minus_k_over_50=true",
    "DAG_leaf_denominator_factor_set=['U', 'V', 'V^4 + 8*V^2*U^3 - 64*U^6', 'V^4 - 32*V^2*U^3 + 128*U^6']",
    "DAG_leaf_denominator_all_factors_emitted=true",
    "raw_stratum_fraction_field_source_identity_exact=true",
    "raw_denominator_factor_strata_still_charged=true",
    "whole_raw_stratum_killed=false",
    "TD6-A3-Q2-FULL-SOURCE-GLUE-RAW-EDGE-DAG-V60 PASS",
):
    assert marker in out, marker

ledger = (HERE / "aws_run/artifacts/DAG_LEAF_DENOMINATORS.tsv").read_text()
p3 = "V^4 - 32*V^2*U^3 + 128*U^6"
qh = "V^4 + 8*V^2*U^3 - 64*U^6"
assert p3 in ledger
assert qh in ledger
assert "current_13_first_only_multipliers" in ledger
assert "previous_('X-1', 14)_first_multipliers" in ledger

# Fail closed: the new QH divisor is not optional and this package does not
# promote a whole-H or fixed-A3 theorem.
assert out.count(qh) >= 1
assert "whole_raw_stratum_killed=true" not in out
assert "full_A3_beta_family_killed=true" not in out

print("TD6-V60-H-SOURCE-DAG-CUSTODY PASS")
print("exact_scope=H_zero_and_U*V*P3*QH_nonzero")
print("whole_H_zero_cover_complete=false")

