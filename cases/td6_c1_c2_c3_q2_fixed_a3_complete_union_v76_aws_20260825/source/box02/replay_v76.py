#!/usr/bin/env python3
"""Exact dependency/constructible union for the fixed A3 q2-beta section."""

from hashlib import sha256
import os
from pathlib import Path
import platform
import socket
import sys


HERE = Path(__file__).resolve().parent


def digest(relative):
    return sha256((HERE / relative).read_bytes()).hexdigest()


def preflight():
    assert platform.system() == "Linux", "AWS/Linux only"
    assert sys.flags.optimize == 0, "assert gate refuses optimized Python"
    tag = os.environ.get("JC2_AWS_RUN_TAG", "")
    expected = os.environ.get("JC2_AWS_EXPECTED_HOSTNAME", "")
    assert tag.startswith("td6_v76_")
    assert expected and socket.gethostname() == expected
    print(f"aws_run_tag={tag}")
    print(f"aws_hostname={socket.gethostname()}")


def verify_manifest():
    listed = set()
    for raw in (HERE / "SOURCE.sha256").read_text().splitlines():
        if not raw.strip():
            continue
        expected, relative = raw.split(None, 1)
        relative = relative.lstrip("*")
        listed.add(relative)
        assert digest(relative) == expected, relative
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


def has_verdict(text, verdict):
    return verdict in {line.strip() for line in text.splitlines()}


def main():
    preflight()
    verify_manifest()

    v57 = (HERE / "evidence/v57/v57.stdout").read_text()
    v57_report = (HERE / "evidence/v57/report.md").read_text()
    v57_ledger = (HERE / "evidence/v57/DAG_LEAF_DENOMINATORS.tsv").read_text()
    v70_report = (HERE / "evidence/v70/report.md").read_text()
    v70_review = (HERE / "evidence/v70/review.md").read_text()
    v71_report = (HERE / "evidence/v71/report.md").read_text()
    v71_review = (HERE / "evidence/v71/review.md").read_text()
    v75 = (HERE / "evidence/v75/stdout").read_text()
    v75_report = (HERE / "evidence/v75/report.md").read_text()

    require(v57, (
        "producer=TD6-A3-Q2-FULL-SOURCE-GLUE-DAG-V57",
        "q_beta=t+beta*t^2+t^25",
        "q_beta_prime=1+2*beta*t+25*t^24",
        "source_center=(C,V,U)",
        "N13_full_first_previous_current_source_identity_exact_by_DAG=true",
        "P12_N13_scalar_glue_exact=true",
        "combined_unit_residual_is_minus_k_over_50=true",
        "DAG_leaf_denominator_radical_subset_U_H_B3=true",
        "TD6-A3-Q2-FULL-SOURCE-GLUE-DAG-V57 PASS",
    ))
    require(v57_report, (
        "exact promoted scope is the fixed, source-typed A3 q2-beta",
        "on `D(U H B3)`",
        "The direct strata `U=0`, `H=0`, and `B3=0` remain",
    ))
    require(v57_ledger, (
        "C - 3*U^2",
        "4*C^2*U^2 - 4*C*V^2*U + 24*C*U^4 + V^4 - 20*V^2*U^3 + 20*U^6",
        "\nU\t2300\t",
    ))
    assert digest("evidence/v57/DAG_LEAF_DENOMINATORS.tsv") == (
        "69c1086b6e302910fe331e7f1c8cfa246a760f429507af2b9d0dd970d1c29ecf"
    )
    assert digest("evidence/v57/N13_PROOF_DAG.txt") == (
        "a906b803a3c0835630884a56e4e9546c7dffa277ba21c36bc3d75027b539da32"
    )

    require(v70_report, (
        "whole raw `U=0`",
        "fixed normalized A3 q2-beta section",
    ))
    assert has_verdict(v70_review, "CONFIRMED")
    require(v71_report, (
        "whole-`H=0` composition theorem",
        "entire raw",
        "H=C-3U^2=0",
        "for every beta",
    ))
    assert has_verdict(v71_review, "CONFIRMED")
    require(v75, (
        "producer=TD6-A3-Q2-B3-ATLAS-UNION-REPAIRED-V75",
        "whole_raw_B3_divisor_all_beta_empty=true",
        "scope=fixed_source_typed_A3_q2_beta_section_only",
        "TD6-A3-Q2-B3-ATLAS-UNION-REPAIRED-V75 PASS",
    ))
    require(v75_report, (
        "whole raw divisor `B3=0` is producer-exact empty",
        "fixed source-typed A3 q2-beta section",
    ))

    # Exact four-branch Boolean cover.  The symbols below are constructible
    # conditions, not sampled points.  A point either has a zero among the
    # three factors, or lies in the principal open of their product.
    witnesses = {"U_zero", "H_zero", "B3_zero", "U_H_B3_all_nonzero"}
    coverage = {
        "V70:V(U)": {"U_zero"},
        "V71:V(H)": {"H_zero"},
        "V75:V(B3)": {"B3_zero"},
        "V57:D(U*H*B3)": {"U_H_B3_all_nonzero"},
    }
    assert set().union(*coverage.values()) == witnesses
    for removed in coverage:
        remaining = set().union(*(
            values for key, values in coverage.items() if key != removed
        ))
        assert remaining != witnesses

    print("producer=TD6-A3-Q2-FIXED-A3-COMPLETE-UNION-V76")
    print("center_ring=Q[C,V,U]")
    print("H=C-3*U^2")
    print("B3=4*C^2*U^2-4*C*V^2*U+24*C*U^4+V^4-20*V^2*U^3+20*U^6")
    print("cover=D(U*H*B3)_union_V(U)_union_V(H)_union_V(B3)")
    print("cover_complete=true")
    print("V57_generic_open_source_DAG_consumed=true")
    print("V70_whole_U_zero_reviewed=true")
    print("V71_whole_H_zero_reviewed=true")
    print("V75_whole_B3_zero_producer_consumed=true")
    print("each_branch_omission_negative_control=true")
    print("fixed_A3_q2_beta_family_producer_empty=true")
    print("V57_hostile_review_pending=true")
    print("V75_hostile_review_pending=true")
    print("promotion_licensed=false")
    print("other_source_moduli_vary=false")
    print("whole_TD6_killed=false")
    print("SP2_killed=false")
    print("landing_proved=false")
    print("JC2_resolved=false")
    print("TD6-A3-Q2-FIXED-A3-COMPLETE-UNION-V76 PASS")


if __name__ == "__main__":
    main()
