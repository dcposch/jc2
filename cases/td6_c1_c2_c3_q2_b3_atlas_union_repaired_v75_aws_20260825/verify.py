#!/usr/bin/env python3
"""Lightweight custody/marker verifier for V74/V75."""

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def require(text, markers):
    missing = [marker for marker in markers if marker not in text]
    assert not missing, missing


def verify_hash_list(root, manifest):
    for raw in manifest.read_text().splitlines():
        if not raw.strip():
            continue
        expected, relative = raw.split(None, 1)
        relative = relative.lstrip("*")
        assert digest(root / relative) == expected, (root, relative)


def canonical_stdout(text):
    return "\n".join(
        line for line in text.splitlines()
        if not line.startswith(("aws_run_tag=", "aws_hostname="))
    )


def main():
    verify_hash_list(HERE, HERE / "MANIFEST.sha256")
    for stage in ("v74", "v75"):
        for host in ("box02", "box03"):
            source = HERE / stage / "source" / host
            verify_hash_list(source, source / "SOURCE.sha256")
            evidence = HERE / stage / "evidence" / host
            assert (evidence / "rc").read_text().strip() == "0"
        out02 = (HERE / stage / "evidence/box02/stdout").read_text()
        out03 = (HERE / stage / "evidence/box03/stdout").read_text()
        assert canonical_stdout(out02) == canonical_stdout(out03)

    v74 = (HERE / "v74/evidence/box02/stdout").read_text()
    require(v74, (
        "source_manifest_verified=true",
        "producer=TD6-A3-Q2-CMINUS5-WHOLE-LINE-UNION-V74",
        "line_open_DU_source_theorem=V73",
        "line_closed_endpoint_U_zero_source_theorem=reviewed_V70_origin",
        "line_cover=D(U)_union_V(U)",
        "line_cover_complete=true",
        "missing_DU_branch_negative_control=true",
        "missing_origin_branch_negative_control=true",
        "whole_raw_Cminus5_line_all_beta_empty=true",
        "whole_B3_killed=false",
        "TD6-A3-Q2-CMINUS5-WHOLE-LINE-UNION-V74 PASS",
    ))
    v75 = (HERE / "v75/evidence/box02/stdout").read_text()
    require(v75, (
        "source_manifest_verified=true",
        "raw_and_normalized_B3_route_algebra_exact=true",
        "all_source_dependency_markers_and_reviews_verified=true",
        "constructible_case_tree_and_omission_controls_exact=true",
        "raw_B3_polynomial_identity_replayed=true",
        "normalized_B3_line_pencil_identity_replayed=true",
        "V66_generic_source_DAG_reviewed=true",
        "V67_two_finite_factor_source_DAGs_reviewed=true",
        "V68_boundary_route_algebra_reviewed_and_replayed=true",
        "V70_whole_U_zero_source_theorem_reviewed=true",
        "V46_Cminus1_DU_source_theorem_reviewed=true",
        "V74_Cminus5_whole_line_source_union_consumed=true",
        "dependency_case_tree_complete=true",
        "each_dependency_omission_negative_control=true",
        "whole_raw_B3_divisor_all_beta_empty=true",
        "scope=fixed_source_typed_A3_q2_beta_section_only",
        "whole_A3_killed=false",
        "whole_TD6_killed=false",
        "TD6-A3-Q2-B3-ATLAS-UNION-REPAIRED-V75 PASS",
    ))
    assert digest(HERE / "v74/source/box02/replay_v74.py") == (
        "fe25b93adf8b79fd08d3b41c33b682758fd191c310017c188305ddc766c095b6"
    )
    assert digest(HERE / "v74/source/box03/replay_v74.py") == (
        "fe25b93adf8b79fd08d3b41c33b682758fd191c310017c188305ddc766c095b6"
    )
    assert digest(HERE / "v75/source/box02/replay_v75.py") == (
        "0c9cb1fe40d4cb95f0fc347f216dd10fe71324f0d48527b85a04ec35609b4c16"
    )
    assert digest(HERE / "v75/source/box03/replay_v75.py") == (
        "0c9cb1fe40d4cb95f0fc347f216dd10fe71324f0d48527b85a04ec35609b4c16"
    )
    print("TD6 V74/V75 frozen custody/marker verification PASS")


if __name__ == "__main__":
    main()
