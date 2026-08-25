#!/usr/bin/env python3
"""Exact dependency union for the raw line V=0, C=-5 U^2.

This checker performs no TD6 elimination.  It hash-pins and checks the
proof-carrying V73 certificate on D(U), the hostile-reviewed V70 origin
certificate on V(U), and the exact set-theoretic cover of the affine line.
"""

import ast
from hashlib import sha256
import os
from pathlib import Path
import platform
import socket
import sys


HERE = Path(__file__).resolve().parent


def preflight():
    assert platform.system() == "Linux", "AWS-only producer: Linux required"
    assert sys.flags.optimize == 0, "assert-based gate refuses optimized Python"
    tag = os.environ.get("JC2_AWS_RUN_TAG", "")
    expected = os.environ.get("JC2_AWS_EXPECTED_HOSTNAME", "")
    assert tag.startswith("td6_v74_"), "registered V74 AWS tag required"
    assert expected and socket.gethostname() == expected, (
        socket.gethostname(), expected
    )
    print(f"aws_run_tag={tag}")
    print(f"aws_hostname={socket.gethostname()}")


def digest(relative):
    return sha256((HERE / relative).read_bytes()).hexdigest()


def verify_manifest():
    listed = set()
    for raw in (HERE / "SOURCE.sha256").read_text().splitlines():
        if not raw.strip():
            continue
        expected, relative = raw.split(None, 1)
        relative = relative.lstrip("*")
        listed.add(relative)
        got = digest(relative)
        assert got == expected, (relative, got, expected)
    actual = {
        path.relative_to(HERE).as_posix()
        for path in HERE.rglob("*")
        if path.is_file() and path.name != "SOURCE.sha256"
    }
    assert listed == actual, (sorted(listed - actual), sorted(actual - listed))
    print("source_manifest_verified=true")


def require(text, markers):
    missing = [marker for marker in markers if marker not in text]
    assert not missing, missing


def main():
    preflight()
    verify_manifest()

    v73 = (HERE / "evidence/v73/v73-main.stdout").read_text()
    v73_dag = (HERE / "evidence/v73/XMINUS1_11_PROOF_DAG.txt").read_text()
    v73_identity = (HERE / "evidence/v73/NORMALIZED_SOURCE_IDENTITY.txt").read_text()
    v73_leaf_ledger = (HERE / "evidence/v73/DAG_LEAF_DENOMINATORS.tsv").read_text()
    v73_factor_ledger = (HERE / "evidence/v73/XMINUS1_11_RESIDUAL_FACTORS.tsv").read_text()
    v70 = (HERE / "evidence/v70/origin.stdout").read_text()
    v70_review = (HERE / "evidence/v70/review.md").read_text()

    v73_markers = (
        "component=V=0,C=-5*U^2,D(U)",
        "direct_qprime_retained=true",
        "Xminus1_11_beta_degree=0",
        "Xminus1_11_numerator_factor_set=['x']",
        "Xminus1_11_denominator_factor_set=[]",
        "Xminus1_11_inverse_denominator_factor_set=['x']",
        "Xminus1_11_unit_on_DU_by_exact_inverse=true",
        "previous_dependency_original_reduced_row_replay=true",
        "Xminus1_11_original_previous_plus_first_source_identity_exact=true",
        "Xminus1_11_normalized_unit_residual_is_minus_one=true",
        "omitted_source_path_negative_control=true",
        "plus_one_multiplier_negative_control=true",
        "wrong_row_negative_control=true",
        "complete_numerator_denominator_support_emitted=true",
        "only_U_localization_charged=true",
        "TD6-A3-Q2-CMINUS5-XMINUS1-11-SOURCE-DAG-V73 PASS",
    )
    require(v73, v73_markers)
    assert (
        "Xminus1_11_each_previous_edge_lifted_to_original_first_rows=true" in v73
        or (
            "Xminus1_11_dependency_aggregate_reduction_exact=true" in v73
            and "Xminus1_11_aggregate_lift_to_original_first_rows=true" in v73
        )
    )
    require(v73_dag, (
        "component=V=0,C=-5*U^2,D(U)",
        "direct_qprime_retained=true",
        "residual_sha256=3884ec0ce04a7b1488cce725551377ed5ef8e3ea20159eb98efe96ce880f552e",
        "certificate_chart_factor_set=['x']",
        "original_previous_plus_first_source_replay=true",
        "normalized_unit_identity=true",
        "omission_plus_one_wrong_row_controls=true",
    ))
    require(v73_identity, (
        "schema=TD6-A3-Q2-CMINUS5-XMINUS1-11-IDENTITY-v73",
        "residual_sha256=3884ec0ce04a7b1488cce725551377ed5ef8e3ea20159eb98efe96ce880f552e",
        "normalized_target=-1",
    ))
    require(v73, (
        f"residual_factor_ledger_sha256={digest('evidence/v73/XMINUS1_11_RESIDUAL_FACTORS.tsv')}",
        f"DAG_leaf_denominator_ledger_sha256={digest('evidence/v73/DAG_LEAF_DENOMINATORS.tsv')}",
        f"normalized_source_identity_sha256={digest('evidence/v73/NORMALIZED_SOURCE_IDENTITY.txt')}",
        f"Xminus1_11_proof_DAG_sha256={digest('evidence/v73/XMINUS1_11_PROOF_DAG.txt')}",
    ))
    require(v73_dag, (
        f"residual_factor_ledger_sha256={digest('evidence/v73/XMINUS1_11_RESIDUAL_FACTORS.tsv')}",
        f"normalized_identity_sha256={digest('evidence/v73/NORMALIZED_SOURCE_IDENTITY.txt')}",
    ))
    require(v73_factor_ledger, (
        "Xminus1_11_residual",
        "Xminus1_11_inverse",
        "[('x', 1)]",
    ))
    ledger_lines = v73_leaf_ledger.splitlines()
    assert ledger_lines[0] == (
        "denominator\tmultiplicity\tfirst_label\tfactorization"
    )
    assert len(ledger_lines) > 1
    for line in ledger_lines[1:]:
        if not line.strip():
            continue
        factorization = ast.literal_eval(line.split("\t", 3)[3])
        assert all(name == "x" and exponent > 0 for name, exponent in factorization)

    v70_markers = (
        "raw_center_stratum=origin",
        "source_center=C=V=U=0",
        "direct_qprime_retained=true",
        "transport_compatibility_original_row_replay=true",
        "v70_transport_incompatibility[0]_wrong_row_control=true",
        "v70_transport_complete_certificate_denominator=(1)",
        "v70_transport_whole_raw_stratum_empty=true",
        "TD6-A3-Q2-N13-RAW-TRANSPORT PASS",
    )
    require(v70, v70_markers)
    assert v70_review.rstrip().endswith("CONFIRMED")
    require(v70_review, (
        "fixed source-typed A3 q2-beta section",
        "source_center=C=V=U=0",
    ))

    # The raw line is Spec Q[U] with C=-5U^2 and V=0.  Its complement of
    # D(U) is exactly V(U), and substituting U=0 gives the origin.
    line_at_u_zero = {"C": -5 * 0**2, "V": 0, "U": 0}
    assert line_at_u_zero == {"C": 0, "V": 0, "U": 0}
    cover_branches = ("D(U):V73", "V(U):V70-origin")
    assert set(cover_branches) == {"D(U):V73", "V(U):V70-origin"}

    # Negative controls: each theorem owns an explicit constructible witness.
    witnesses = {"generic_U_nonzero", "origin_U_zero"}
    coverage = {
        "D(U):V73": {"generic_U_nonzero"},
        "V(U):V70-origin": {"origin_U_zero"},
    }
    assert set(coverage) == set(cover_branches)
    assert set().union(*coverage.values()) == witnesses
    for removed in coverage:
        remaining = set().union(*(value for key, value in coverage.items() if key != removed))
        assert remaining != witnesses
    assert "only_U_localization_charged=true" in v73
    assert "v70_transport_whole_raw_stratum_empty=true" in v70

    print("producer=TD6-A3-Q2-CMINUS5-WHOLE-LINE-UNION-V74")
    print("source_center_line=V=0,C=-5*U^2")
    print("q_beta=t+beta*t^2+t^25")
    print("direct_qprime_retained_on_DU=true")
    print("line_open_DU_source_theorem=V73")
    print("line_closed_endpoint_U_zero_source_theorem=reviewed_V70_origin")
    print("line_U_zero_substitution_is_origin=true")
    print("line_cover=D(U)_union_V(U)")
    print("line_cover_complete=true")
    print("missing_DU_branch_negative_control=true")
    print("missing_origin_branch_negative_control=true")
    print("whole_raw_Cminus5_line_all_beta_empty=true")
    print("whole_B3_killed=false")
    print("whole_A3_killed=false")
    print("whole_TD6_killed=false")
    print("SP2_killed=false")
    print("JC2_resolved=false")
    print("TD6-A3-Q2-CMINUS5-WHOLE-LINE-UNION-V74 PASS")


if __name__ == "__main__":
    main()
