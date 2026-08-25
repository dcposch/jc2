#!/usr/bin/env python3
"""Lightweight custody, duplicate, source-DAG, and scope audit for V65."""

from hashlib import sha256
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def text(path):
    return path.read_text()


def normalized_stdout(path):
    value = text(path)
    return re.sub(
        r"/home/ubuntu/runs/td6_v65_[^/\n]+/artifacts",
        "ARTIFACTS",
        value,
    )


EXPECTED = {
    "archives/td6-aws-handoff-20260825-v65.tar.gz":
        "eb481ca9e686a5fec349c5ce42915cd032d0096aee53f7a33b156ec5598edb6f",
    "evidence/box02_p3/v65.stdout":
        "63905105269deb7952094ec749bcaa835322024edb80372fc55b16d3fa100be0",
    "evidence/r6d_p3/v65.stdout":
        "56296ed9529a733c2d1ad3534dea42c1a90611d9803a3c261556861331230d02",
    "evidence/box02_qh/v65.stdout":
        "d5b4ff8826e5a595e0503118d1491b88e3685c2575b1d40fcd73991a437e9edb",
    "evidence/r6d_qh/v65.stdout":
        "c9d9fca38d0581962526814ed7059fdd08312315db65739a5f6c6cb25f599c25",
    "evidence/box02_p3/artifacts/DAG_LEAF_DENOMINATORS.tsv":
        "0befb53ee429d0f72c1f9d3cd04857a3c4038cfdd092007c68dbf17e8283c276",
    "evidence/box02_p3/artifacts/N13_P12_PROOF_DAG.txt":
        "52eada0af5c08a5775fff7efba77eed5bfb8a73df18d3cd0696961c7c5292f78",
    "evidence/box02_qh/artifacts/DAG_LEAF_DENOMINATORS.tsv":
        "887f8ce6b8c0ebf49f91ff9f7e6876a42fdab2b09b5370daea05c70d8337b87c",
    "evidence/box02_qh/artifacts/N13_P12_PROOF_DAG.txt":
        "4efbee5fcf38c84eb4966b2721b91287e82fc347b095bbfe93b4b656d63711c3",
    "evidence/box02_p3/source-check.txt":
        "6475f36334fb0c638bcc00ce752cc94b4f28c265ae6ebf06f5c2e147f6d106ec",
    "evidence/negative_control/p3_omit_qprime/v65.stdout":
        "d3125bbd34d4799e92794e1956c8e0d3aa1429bb8990f596ab6dccaf3e5c5087",
    "evidence/negative_control/p3_omit_qprime/v65.stderr":
        "51226a5b75e62aa58592da26d17ef49514bc12e355f217c4bd4b31ec995395cb",
}

for relative, expected in EXPECTED.items():
    got = digest(HERE / relative)
    assert got == expected, (relative, got, expected)

for host in ("box02", "r6d"):
    for component in ("p3", "qh"):
        assert text(HERE / f"evidence/{host}_{component}/rc") == "0\n"

for component, expected_normalized in (
    ("p3", "2ab37f8da764f5b44df6c931897aa83bee077f1fd449f89d2617075e03d89b4a"),
    ("qh", "bc5e95c35459ea96b628e4816e90bade0d2c81bbaa8eb78db3dd3f1a21e6c55c"),
):
    left = normalized_stdout(HERE / f"evidence/box02_{component}/v65.stdout")
    right = normalized_stdout(HERE / f"evidence/r6d_{component}/v65.stdout")
    assert left == right
    assert sha256(left.encode()).hexdigest() == expected_normalized
    for artifact in ("DAG_LEAF_DENOMINATORS.tsv", "N13_P12_PROOF_DAG.txt"):
        assert (
            HERE / f"evidence/box02_{component}/artifacts/{artifact}"
        ).read_bytes() == (
            HERE / f"evidence/r6d_{component}/artifacts/{artifact}"
        ).read_bytes()

COMMON_MARKERS = (
    "q_beta=t+beta*t^2+t^25",
    "direct_qprime_retained=true",
    "source_p_boundary=t^15_fixed",
    "weighted_scaling_used=false",
    "transport_rank=3470/3602",
    "first_rank=38/132",
    "previous_pole_rank=38/94",
    "current_rank=25/56",
    "N13_equals_k_beta_over_25=true",
    "N13_previous_edge_keys=[('X-1', 14)]",
    "quadratic_source_positive_control_key=('X-1', 0)",
    "quadratic_control_is_N13_edge=false",
    "dependency_closed_original_rows_reduced_exactly=true",
    "N13_each_dependency_edge_original_row_replay=true",
    "N13_singleton_current_row_omission_negative_control=true",
    "N13_previous_edge_omission_negative_control=true",
    "N13_full_first_previous_current_source_identity_exact_by_DAG=true",
    "genuine_P12_raw_term_count=2885",
    "P12_first_original_row_replay=true",
    "P12_first_nonzero_rows=28",
    "P12_N13_scalar_glue_exact=true",
    "P12_without_N13_negative_control=true",
    "combined_unit_residual_is_minus_k_over_50=true",
    "DAG_leaf_denominator_factor_set=['x']",
    "DAG_leaf_factors_only_U=true",
    "DAG_leaf_denominator_all_factors_emitted=true",
    "curve_fraction_field_source_identity_exact=true",
    "certificate_chart_factor=(1, [(x, 13)])",
    "only_parameter_zero_exception=true",
    "raw_U_endpoint_still_separate=true",
    "component_all_beta_killed=false",
    "fixed_A3_all_beta_killed=false",
    "TD6-A3-Q2-CURVE-SOURCE-DAG-REPAIRED-V65 PASS",
)

for component in ("p3", "qh"):
    out = normalized_stdout(HERE / f"evidence/box02_{component}/v65.stdout")
    assert f"component={component}" in out
    for marker in COMMON_MARKERS:
        assert marker in out, (component, marker)
    dag = text(HERE / f"evidence/box02_{component}/artifacts/N13_P12_PROOF_DAG.txt")
    for marker in (
        f"component={component}",
        "N13_previous_edge_keys=[('X-1', 14)]",
        "quadratic_control_key=('X-1', 0)",
        "current_row_index=13",
        "each_current_edge_original_row_replay=true",
        "each_selected_previous_edge_original_row_replay=true",
        "staged_left_null_relation_exact=true",
        "P12_first_original_row_replay=true",
        "P12_minus_multiplier_times_N13_equals_minus_k_over_50=true",
        "curve_leaf_factor_set=['x']",
    ):
        assert marker in dag, (component, marker)
    ledger = text(HERE / f"evidence/box02_{component}/artifacts/DAG_LEAF_DENOMINATORS.tsv")
    assert "x^6" in ledger
    assert "transport_chart_clear" in ledger

qh = normalized_stdout(HERE / "evidence/box02_qh/v65.stdout")
for marker in (
    "QH_T_relation=T^2+8*T-64",
    "P3_T_relation=T^2-32*T+128",
    "QH_P3_bezout=((5*T-136)*QH-(5*T+64)*P3)/512=1",
    "QH_P3_disjoint_on_DU=true",
    "QH_V_zero_forces_U_zero=true",
):
    assert marker in qh, marker

control = HERE / "evidence/negative_control/p3_omit_qprime"
assert text(control / "rc") == "1\n"
control_out = text(control / "v65.stdout")
assert "direct_qprime_omission_changes_N13=true" in control_out
assert "N13_equals_k_beta_over_25=true" not in control_out
assert "IndexError: list index out of range" in text(control / "v65.stderr")

print("TD6-P3-QH-SOURCE-DAG-V65 CUSTODY PASS")
print("exact_scope=(H=P3=0 or H=QH=0) intersect D(U), fixed A3 q2-beta")
print("whole_curve_or_H_cover_complete=false")
