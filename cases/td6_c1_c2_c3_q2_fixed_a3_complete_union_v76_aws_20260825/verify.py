#!/usr/bin/env python3
"""Lightweight custody/status verifier for V76C."""

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def verify_hash_list(root, manifest):
    for raw in manifest.read_text().splitlines():
        if not raw.strip():
            continue
        expected, relative = raw.split(None, 1)
        relative = relative.lstrip("*")
        assert digest(root / relative) == expected, (root, relative)


def require(text, markers):
    missing = [marker for marker in markers if marker not in text]
    assert not missing, missing


def canonical(text):
    return "\n".join(
        line for line in text.splitlines()
        if not line.startswith(("aws_run_tag=", "aws_hostname="))
    )


def main():
    verify_hash_list(HERE, HERE / "MANIFEST.sha256")
    for host in ("box02", "box03"):
        source = HERE / "source" / host
        verify_hash_list(source, source / "SOURCE.sha256")
        assert (HERE / "evidence" / host / "rc").read_text().strip() == "0"
    out02 = (HERE / "evidence/box02/stdout").read_text()
    out03 = (HERE / "evidence/box03/stdout").read_text()
    assert canonical(out02) == canonical(out03)
    require(out02, (
        "producer=TD6-A3-Q2-FIXED-A3-COMPLETE-UNION-V76",
        "center_ring=Q[C,V,U]",
        "cover=D(U*H*B3)_union_V(U)_union_V(H)_union_V(B3)",
        "cover_complete=true",
        "V57_generic_open_source_DAG_consumed=true",
        "V70_whole_U_zero_reviewed=true",
        "V71_whole_H_zero_reviewed=true",
        "V75_whole_B3_zero_producer_consumed=true",
        "each_branch_omission_negative_control=true",
        "fixed_A3_q2_beta_family_producer_empty=true",
        "V57_hostile_review_pending=true",
        "V75_hostile_review_pending=true",
        "promotion_licensed=false",
        "other_source_moduli_vary=false",
        "whole_TD6_killed=false",
        "TD6-A3-Q2-FIXED-A3-COMPLETE-UNION-V76 PASS",
    ))
    assert digest(HERE / "source/box02/replay_v76.py") == (
        "dd9bb146e43bf778d83e3b6420442bc4e4b42effd388be75cb3c3d00f609157a"
    )
    assert digest(HERE / "source/box03/replay_v76.py") == (
        "dd9bb146e43bf778d83e3b6420442bc4e4b42effd388be75cb3c3d00f609157a"
    )
    assert digest(HERE / "source/td6-v76-fixed-a3-union-20260825-v3.tar.gz") == (
        "eb8858ccf5a21acdd7d413876ab44e2402faea7913a97d35b849acff61d22b8a"
    )
    print("TD6 V76C frozen custody/status verification PASS")


if __name__ == "__main__":
    main()
