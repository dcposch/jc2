#!/usr/bin/env python3
"""Lightweight custody/marker verifier for frozen V73K evidence."""

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def require(text, markers):
    missing = [marker for marker in markers if marker not in text]
    assert not missing, missing


def verify_manifest():
    for raw in (HERE / "MANIFEST.sha256").read_text().splitlines():
        if not raw.strip():
            continue
        expected, relative = raw.split(None, 1)
        relative = relative.lstrip("*")
        assert digest(HERE / relative) == expected, relative


def canonical_stdout(text):
    excluded_prefixes = (
        "aws_hostname=",
        "aws_run_tag=",
        "residual_factor_ledger_path=",
        "DAG_leaf_denominator_ledger_path=",
        "normalized_source_identity_path=",
        "Xminus1_11_proof_DAG_path=",
    )
    return "\n".join(
        line for line in text.splitlines()
        if not line.startswith(excluded_prefixes)
    )


def main():
    verify_manifest()
    box02 = HERE / "evidence/main/box02"
    box03 = HERE / "evidence/main/box03"
    assert (box02 / "rc").read_text().strip() == "0"
    assert (box03 / "rc").read_text().strip() == "0"
    out02 = (box02 / "stdout").read_text()
    out03 = (box03 / "stdout").read_text()
    markers = (
        "component=V=0,C=-5*U^2,D(U)",
        "direct_qprime_retained=true",
        "transport_rank=3470/3602",
        "first_rank=38/132",
        "previous_pole_rank=37/94",
        "Xminus1_11_beta_degree=0",
        "Xminus1_11_residual_sha256=3884ec0ce04a7b1488cce725551377ed5ef8e3ea20159eb98efe96ce880f552e",
        "Xminus1_11_numerator_factor_set=['x']",
        "Xminus1_11_denominator_factor_set=[]",
        "Xminus1_11_inverse_denominator_factor_set=['x']",
        "Xminus1_11_unit_on_DU_by_exact_inverse=true",
        "Xminus1_11_dependency_row_count=12",
        "Xminus1_11_first_source_edge_count=13",
        "Xminus1_11_degree11_full_direct_qprime_contribution=4*beta*f2[10]",
        "Xminus1_11_single_full_original_source_replay=true",
        "Xminus1_11_original_previous_plus_first_source_identity_exact=true",
        "Xminus1_11_normalized_unit_residual_is_minus_one=true",
        "omitted_source_path_negative_control=true",
        "plus_one_multiplier_negative_control=true",
        "wrong_row_negative_control=true",
        "complete_numerator_denominator_support_emitted=true",
        "only_U_localization_charged=true",
        "whole_B3_killed=false",
        "TD6-A3-Q2-CMINUS5-XMINUS1-11-SOURCE-DAG-V73 PASS",
    )
    require(out02, markers)
    require(out03, markers)
    assert canonical_stdout(out02) == canonical_stdout(out03)

    expected_artifacts = {
        "XMINUS1_11_PROOF_DAG.txt": "27a26a20773fb4f417ed9a3292c483c9668fa3af5f61933e9aa880c48d84d5c9",
        "NORMALIZED_SOURCE_IDENTITY.txt": "be5b6bc8bd09dc9b59f42270a6725236fe0f96392030d88a1a1a3c5323ab40f9",
        "DAG_LEAF_DENOMINATORS.tsv": "112776f2544b3b3501eedfd9ce4d6fe41b4e13aa53ff07f7d2bcf37f3306e2d9",
        "XMINUS1_11_RESIDUAL_FACTORS.tsv": "8763f53f12a8f52705a29a0b99b525df358fc46fd1d3f42c31ea2bd38a989bcf",
    }
    for name, expected in expected_artifacts.items():
        assert digest(box02 / "artifacts" / name) == expected
        assert digest(box03 / "artifacts" / name) == expected

    source = HERE / "source"
    assert digest(source / "td6-v73k-single-positive-replay-20260825.tar.gz") == (
        "2af9d2dc54cd1f4fc2aab674aa28704732994c6ffe7c2b21a465066eb2569dd5"
    )
    assert digest(source / "V73_SOURCE.sha256") == (
        "d26fcec169ddbeed1b52024343750ba1636643235da4b2ff31902a6298a9c470"
    )
    assert digest(source / "replay_v73.py") == (
        "dcaa920a85fcfdfbc4c4e3975c00b45f6ff7e540be21685df59ff2ae36af1672"
    )

    control = (HERE / "evidence/control/box03-qprime/stdout").read_text()
    require(control, (
        "direct_qprime_retained=false",
        "omitted_direct_qprime_Xminus1_13_absent=true",
        "omitted_direct_qprime_Xminus1_11_unchanged=true",
        "TD6-A3-Q2-CMINUS5-XMINUS1-11-QPRIME-CONTROL-V73 PASS",
    ))
    print("TD6 V73K frozen custody/marker verification PASS")


if __name__ == "__main__":
    main()
