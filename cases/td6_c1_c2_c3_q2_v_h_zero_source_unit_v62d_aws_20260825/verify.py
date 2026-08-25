#!/usr/bin/env python3
"""Lightweight custody and exact-scope verifier for duplicated V62D."""

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent
EXPECTED = {
    "archives/td6-aws-handoff-20260825-v62d.tar.gz":
        "6d568ff6e77dc764c2ddae6b5be1c6b8baa75e47e364ac15f83d6e4aaaa52e42",
    "aws_box02/v62d.stdout":
        "50a143c637b0344b2ea8dc7d4f67ae85c4afe497b6d3fecb59a1d94665980a76",
    "aws_box02/v62d.stderr":
        "4c094945aec535503eda3094ef4ae3e8243d35d585397acfff3cde06928d0efe",
    "aws_box02/source-check.txt":
        "189c6b5efd4ec9f2d4cb1f2b0f66fbaf4a83d83b9632aa93e94b3afb3adc2270",
    "aws_r6d/v62d.stdout":
        "db4e566e4dfb51d6bffe66fc271fb3e19d9b7b4c5c5b1d7657d1789a305dd1bf",
    "aws_r6d/v62d.stderr":
        "a5da9201261dac76cf0ab66f6c4d8d65f2a69103958f29ea73135bc5676591c4",
}
ARTIFACTS = {
    "COMBINED_PREVIOUS_SOURCE_UNIT.txt":
        "6d672e839c84b518909ea70161761f929d249fa4251fa5852bde9f896c1572a1",
    "COMBINED_SOURCE_UNIT_DENOMINATORS.tsv":
        "02d29ba2f0112a5f2d83b1973d86e4350ae04203df1496a9f598c599c8d8426a",
    "FIRST_PREVIOUS_PIVOT_DENOMINATORS.tsv":
        "bacdf7a6869cb50f118c4a77fa646815963f9782be5bf0f387dc676361f8b034",
}


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


for relative, expected in EXPECTED.items():
    got = digest(HERE / relative)
    assert got == expected, (relative, got, expected)

for host in ("aws_box02", "aws_r6d"):
    assert (HERE / host / "rc").read_text() == "0\n"
    for name, expected in ARTIFACTS.items():
        got = digest(HERE / host / "artifacts" / name)
        assert got == expected, (host, name, got, expected)

box = (HERE / "aws_box02/v62d.stdout").read_text().splitlines()
r6d = (HERE / "aws_r6d/v62d.stdout").read_text().splitlines()
path_prefixes = (
    "source_certificate_path=",
    "source_denominator_ledger_path=",
    "pivot_denominator_ledger_path=",
)
assert [line for line in box if not line.startswith(path_prefixes)] == [
    line for line in r6d if not line.startswith(path_prefixes)
]

markers = (
    "raw_center_stratum=V=H=0_over_Q(U)",
    "scope=post_transport_original_rows_on_function_field_of_rational_edge",
    "representation=bezout_then_one_direct_original_polynomial_division",
    "current_stage_used=false",
    "P12_used=false",
    "N13_used=false",
    "first_v62d_rank=38/132",
    "previous_pole_v62d_rank=37/94",
    "previous_pole_nonzero_dependency_keys=[('X-1', 11), ('X-1', 13)]",
    "previous_pole_reduced_bezout_exact=true",
    "combined_raw_previous_polynomial_divided_once=true",
    "combined_remainder_is_exact_unit=true",
    "arbitrary_degree_original_rows_preserved=true",
    "full_original_row_unit_certificate_exact=true",
    "one_first_source_edge_omission_negative_control=true",
    "one_previous_source_edge_omission_negative_control=true",
    "source_denominator_factor_set=['U']",
    "pivot_denominator_factor_set=['U']",
    "complete_localization_factor_set=['U']",
    "function_field_rational_edge_empty=true",
    "raw_denominator_factor_strata_still_charged=true",
    "whole_V_H_zero_edge_empty=false",
    "full_A3_beta_family_killed=false",
    "whole_TD6_killed=false",
    "SP2_killed=false",
    "JC2_resolved=false",
    "TD6-A3-Q2-V-H-ZERO-COMBINED-EMPTY-V62D PASS",
)
joined = "\n".join(box)
for marker in markers:
    assert marker in joined, marker

source_check = (HERE / "aws_box02/source-check.txt").read_text().splitlines()
assert len(source_check) == 111
assert all(line.endswith(": OK") for line in source_check)

source_ledger = (
    HERE / "aws_box02/artifacts/COMBINED_SOURCE_UNIT_DENOMINATORS.tsv"
).read_text()
pivot_ledger = (
    HERE / "aws_box02/artifacts/FIRST_PREVIOUS_PIVOT_DENOMINATORS.tsv"
).read_text()
assert "\nU\t" in source_ledger and "\nU^7\t" in source_ledger
assert "\nU\t" in pivot_ledger and "\nU^6\t" in pivot_ledger
for forbidden in ("V", "P3", "QH"):
    assert forbidden not in source_ledger
    assert forbidden not in pivot_ledger

print("TD6-V62D-V-H-ZERO-SOURCE-UNIT-CUSTODY PASS")
print("independent_AWS_replays=box02,r6d")
print("exact_scope=V_zero_intersect_H_zero_intersect_D(U)_inside_fixed_A3_q2_beta")
print("whole_V_H_zero_edge_empty=false")

