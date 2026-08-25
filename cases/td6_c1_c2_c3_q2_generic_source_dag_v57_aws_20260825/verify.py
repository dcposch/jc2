#!/usr/bin/env python3
"""Lightweight custody, duplication, and scope verifier for V57."""

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent
EXPECTED = {
    "archives/td6-aws-handoff-20260825-v57.tar.gz":
        "cc34d029fc30f469239ebb0d4c07eb33992c7de75fbd71242eed24bbbc2df310",
    "aws_r6d/v57.stdout":
        "2bb3374c187eb3d8989604c2d2742efb2bc33f45a6f61433c26792551482e0c1",
    "aws_r6d/v57.stderr":
        "5d8e5246d41f5abcae42ecf18dd91658b45f6f3294a424c1ee95030cb5b0174e",
    "aws_box03/v57.stdout":
        "24b9f9ba3f9da515931f03b7e7e2c1bb3d35449401bf534d8f06da001e0d3e8b",
    "aws_box03/v57.stderr":
        "ec00c2c24b761f0b5cc49be63b8dc4039d0c6d0dd205d20d66251b27f13a694b",
    "aws_r6d/artifacts/DAG_LEAF_DENOMINATORS.tsv":
        "69c1086b6e302910fe331e7f1c8cfa246a760f429507af2b9d0dd970d1c29ecf",
    "aws_r6d/artifacts/N13_PROOF_DAG.txt":
        "a906b803a3c0835630884a56e4e9546c7dffa277ba21c36bc3d75027b539da32",
    "aws_box03/artifacts/DAG_LEAF_DENOMINATORS.tsv":
        "69c1086b6e302910fe331e7f1c8cfa246a760f429507af2b9d0dd970d1c29ecf",
    "aws_box03/artifacts/N13_PROOF_DAG.txt":
        "a906b803a3c0835630884a56e4e9546c7dffa277ba21c36bc3d75027b539da32",
}

for relative, expected in EXPECTED.items():
    got = sha256((HERE / relative).read_bytes()).hexdigest()
    assert got == expected, (relative, got, expected)

for host in ("aws_r6d", "aws_box03"):
    assert (HERE / host / "rc").read_text() == "0\n"
    out = (HERE / host / "v57.stdout").read_text()
    for marker in (
        "arbitrary_degree_original_rows_preserved=true",
        "transport_chart=D(U*H*B3)",
        "N13_left_null_support=1",
        "current_rows_source_lifted_indices=[12, 13]",
        "dependency_closed_original_rows_reduced_exactly=true",
        "N13_each_dependency_edge_original_row_replay=true",
        "N13_one_required_edge_omission_negative_control=true",
        "genuine_P12_2893_term_control=true",
        "P12_without_N13_negative_control=true",
        "combined_unit_residual_is_minus_k_over_50=true",
        "DAG_leaf_denominator_radical_subset_U_H_B3=true",
        "composed_localized_source_identity_exact=true",
        "generic_open_localization_repaired=true",
        "raw_U_H_B3_strata_still_separate=true",
        "full_A3_beta_family_killed=false",
        "TD6-A3-Q2-FULL-SOURCE-GLUE-DAG-V57 PASS",
    ):
        assert marker in out, (host, marker)

assert (HERE / "aws_r6d/artifacts/N13_PROOF_DAG.txt").read_bytes() == (
    HERE / "aws_box03/artifacts/N13_PROOF_DAG.txt").read_bytes()
assert (HERE / "aws_r6d/artifacts/DAG_LEAF_DENOMINATORS.tsv").read_bytes() == (
    HERE / "aws_box03/artifacts/DAG_LEAF_DENOMINATORS.tsv").read_bytes()

ledger = (HERE / "aws_r6d/artifacts/DAG_LEAF_DENOMINATORS.tsv").read_text()
assert "C - 3*U^2" in ledger
assert "4*C^2*U^2 - 4*C*V^2*U + 24*C*U^4 + V^4 - 20*V^2*U^3 + 20*U^6" in ledger

print("TD6-V57-GENERIC-SOURCE-DAG-CUSTODY PASS")
print("exact_scope=D(U*H*B3)_inside_fixed_A3_q2_beta")
print("raw_divisor_cover_complete=false")

