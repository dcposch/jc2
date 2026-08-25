#!/usr/bin/env python3
"""Lightweight custody/marker verifier for the frozen V67 AWS evidence."""

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent
ARCHIVE_SHA = "13bdaa2a0033eef77088a3a1bc46c7288efde85398f0897107769c04ff404306"
EXPECTED = {
    "b3half": {
        "factor": "B3_parameter_factor=2*t-1",
        "terms": "genuine_P12_raw_term_count=2893",
        "chart": "certificate_chart_factor=(1, [(x, 27)])",
        "normalized": "bf5b63f1371b6bee76975a5f273c71da83ac70f110ae90c92bf9a839c7a36004",
        "dag": "5fe6def13f370a224145cdc03a0c99e053a72ab7ec61c770ccee02ff9bfad7fe",
        "ledger": "1d18859a78f5936518caa31a2a83175abf22614391fa3fb80b3765933c2c1041",
    },
    "b3tq": {
        "factor": "B3_parameter_factor=t^2-4*t+2",
        "terms": "genuine_P12_raw_term_count=2885",
        "chart": "certificate_chart_factor=(1, [(x, 23)])",
        "normalized": "538b70f522ad10f45dae9b842112799bcc4bc9e0e93c824a27b8eede6bd2b454",
        "dag": "d71cf73a58f53b01dc47c3a48f91d9404d18194e90c5c48fb97a435a4e5b2f08",
        "ledger": "795ca7bcd04ded0ca800a104bb0de68027a960864dd7e50add0dba7bf630d6ac",
    },
}


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def check_theorem(component):
    expected = EXPECTED[component]
    normalized = []
    for host in ("box03", "box02"):
        run = HERE / "evidence" / host / component
        assert (run / "rc").read_text().strip() == "0"
        text = (run / "v67.stdout").read_text()
        for marker in (
            "direct_qprime_retained=true",
            expected["factor"],
            "B3_parameter_center_identity_zero=true",
            "B3_parameter_inverse_formulas=true",
            "raw_curve_w_zero_is_origin=true",
            "transport_rank=3470/3602",
            "first_rank=38/132",
            "previous_pole_rank=38/94",
            "current_rank=25/56",
            "N13_equals_k_beta_over_25=true",
            "N13_previous_edge_keys=[('X-1', 14)]",
            "quadratic_control_is_N13_edge=false",
            "N13_full_first_previous_current_source_identity_exact_by_DAG=true",
            expected["terms"],
            "P12_first_nonzero_rows=28",
            "combined_unit_residual_is_minus_k_over_50=true",
            "DAG_leaf_denominator_factor_set=['x']",
            "stage_denominator_factor=(1, [(x, 11)])",
            expected["chart"],
            "only_parameter_zero_exception=true",
            "raw_w_zero_origin_endpoint_still_separate=true",
            "component_all_beta_killed=false",
            "TD6-A3-Q2-B3-FACTOR-SOURCE-DAG-REPAIRED-V67 PASS",
        ):
            assert marker in text, (host, component, marker)
        norm = run / "normalized.stdout"
        assert digest(norm) == expected["normalized"]
        normalized.append(norm.read_bytes())
        assert digest(run / "artifacts" / "N13_P12_PROOF_DAG.txt") == expected["dag"]
        assert digest(run / "artifacts" / "DAG_LEAF_DENOMINATORS.tsv") == expected["ledger"]
    assert normalized[0] == normalized[1]


def check_controls():
    for component in ("b3half_omit_qprime", "b3tq_omit_qprime"):
        run = HERE / "evidence" / "controls" / component
        assert (run / "rc").read_text().strip() == "1"
        assert "direct_qprime_omission_changes_N13=true" in (run / "v67.stdout").read_text()
        stderr = (run / "v67.stderr").read_text()
        assert "IndexError: list index out of range" in stderr
        assert "Exit status: 1" in stderr


def main():
    archive = HERE / "archives" / "td6-aws-handoff-20260825-v67.tar.gz"
    assert digest(archive) == ARCHIVE_SHA
    check_theorem("b3half")
    check_theorem("b3tq")
    check_controls()
    print("TD6-A3-Q2-B3-FINITE-FACTORS-V67 CUSTODY PASS")
    print("exact_scope=two finite B3 factor function fields on D(w)")
    print("whole_factor_or_B3_or_A3=false")


if __name__ == "__main__":
    main()
