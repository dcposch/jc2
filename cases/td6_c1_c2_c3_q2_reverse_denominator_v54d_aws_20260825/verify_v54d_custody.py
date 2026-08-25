#!/usr/bin/env python3
"""Lightweight custody verifier for the duplicated AWS V54D diagnostic."""

from hashlib import sha256
from pathlib import Path
import tarfile


HERE = Path(__file__).resolve().parent
ARCHIVE_SHA = "0386b2c7d6b199cf5a287c0826540cf48f853b3b926bcf1d9ddb8a6c80d67983"
RUNBOOK_SHA = "c9b7d5b95d68ff9005278a2a1854b4259eebbef9a7bd427abd1999eb85f9d692"
SOURCE_LIST_SHA = "1705da2399ca6701aecb7627692924edd741f8ee89a3ddfa1dfff9f6bbe25c69"
REPLAY_SHA = "ce98c91dcd56e90bc393ebf3a60e5d0f96b4557f37068a8312d3b6014644b5c3"
STDOUT_SHA = "01112ab9578ce9737eba99ab7ebd0f482a007579ab3e0df76da7841635a94450"
PIVOTS_SHA = "77cafdf8facdd721e79b00a2dd4fee0d66f5374c26a26208c0125191e86cb0ce"
PRODUCT_SHA = "d9b1a00112491ecfb6fb3f941f26fd00afb46b725dbc45b31c4ec710a02bd2e2"


def digest_bytes(data: bytes) -> str:
    return sha256(data).hexdigest()


def digest(path: Path) -> str:
    return digest_bytes(path.read_bytes())


def require(text: str, marker: str) -> None:
    assert marker in text, marker


def main() -> None:
    archive = HERE / "source" / "td6-aws-handoff-20260825-v54d.tar.gz"
    assert digest(archive) == ARCHIVE_SHA
    assert digest(HERE / "source" / "V54D_RUNBOOK.md") == RUNBOOK_SHA
    assert digest(HERE / "source" / "V54D_SOURCE.sha256") == SOURCE_LIST_SHA

    prefix = "td6-aws-handoff-20260825-v54d/"
    with tarfile.open(archive, "r:gz") as tf:
        runbook = tf.extractfile(prefix + "V54D_RUNBOOK.md").read()
        source_list = tf.extractfile(prefix + "V54D_SOURCE.sha256").read()
        replay = tf.extractfile(
            prefix
            + "jc2/cases/td6_c1_c2_c3_q2_reverse_denominator_v54d_20260825/replay.py"
        ).read()
    assert digest_bytes(runbook) == RUNBOOK_SHA
    assert digest_bytes(source_list) == SOURCE_LIST_SHA
    assert digest_bytes(replay) == REPLAY_SHA
    assert runbook == (HERE / "source" / "V54D_RUNBOOK.md").read_bytes()
    assert source_list == (HERE / "source" / "V54D_SOURCE.sha256").read_bytes()

    outputs = []
    pivot_tables = []
    pivot_products = []
    for host in ("box03", "r6d"):
        evidence = HERE / "evidence" / host
        assert (evidence / "rc").read_text().strip() == "0"
        require((evidence / "archive-check.txt").read_text(), "archive.tar.gz: OK")
        require(
            (evidence / "v54d-source-check.txt").read_text(),
            "jc2/cases/td6_c1_c2_c3_q2_reverse_denominator_v54d_20260825/replay.py: OK",
        )
        stderr = (evidence / "v54d.stderr").read_text()
        require(stderr, "Exit status: 0")
        require(stderr, "Maximum resident set size (kbytes):")

        out_path = evidence / "v54d.stdout"
        assert digest(out_path) == STDOUT_SHA
        output = out_path.read_text()
        for marker in (
            "producer=TD6-A3-Q2-REVERSE-DENOMINATOR-V54D",
            "canonical_serializer_namespace=g.canonical",
            "independent_post_transport_row_order=reverse_deferred_fraction_free",
            "nonunit_pivots_recorded_not_inverted=true",
            "arbitrary_degree_original_rows_preserved=true",
            "transport_rank=3470/3602",
            "first_v50_unit_rank=32",
            "first_v50_unresolved_nonunit_count=6",
            "first_v50_fraction_free_nonunit_count=6",
            "first_v50_fraction_field_rank=38/132",
            "first_v50_fraction_free_original_row_replay=true",
            "first_v50_nonunit[0]_coefficient_denominator=(C*U^4 - 3*U^6)",
            "first_v50_nonunit[1]_coefficient_denominator=(C*U^4 - 3*U^6)",
            "first_v50_nonunit[2]_coefficient_denominator=(U^5)",
            "first_v50_nonunit[3]_coefficient_denominator=(C^2*U^4 - 6*C*U^6 + 9*U^8)",
            "first_v50_nonunit[4]_coefficient_denominator=(C^4*U^3 - 12*C^3*U^5 + 54*C^2*U^7 - 108*C*U^9 + 81*U^11)",
            "first_v50_nonunit[5]_coefficient_denominator=(C^8 - 24*C^7*U^2 + 252*C^6*U^4 - 1512*C^5*U^6 + 5670*C^4*U^8 - 13608*C^3*U^10 + 20412*C^2*U^12 - 17496*C*U^14 + 6561*U^16)",
            "first_v50_coefficient_denominator=(C^8*U - 24*C^7*U^3 + 252*C^6*U^5 - 1512*C^5*U^7 + 5670*C^4*U^9 - 13608*C^3*U^11 + 20412*C^2*U^13 - 17496*C*U^15 + 6561*U^17)",
            "first_v50_coefficient_denominator_sha256=503718df91f3f3fcc34fc050e6522ec5fc3d87d5650e3567b63c2eaa797918b9",
            "first_v50_center_denominator_support_exact_U_H=true",
            "first_v50_canonical_artifacts_address_free=true",
            "reverse_chart_product_nonvanishing_required=true",
            "reverse_chart_coverage_inference=false",
            "full_V50_source_identity_replayed=false",
            "full_A3_beta_family_killed=false",
            "whole_TD6_killed=false",
            "SP2_killed=false",
            "JC2_resolved=false",
            "TD6-A3-Q2-REVERSE-DENOMINATOR-V54D PASS",
        ):
            require(output, marker)

        pivots = evidence / "artifacts" / "REVERSE_FIRST_NONUNIT_PIVOTS.tsv"
        product = evidence / "artifacts" / "REVERSE_FIRST_PIVOT_PRODUCT.txt"
        assert digest(pivots) == PIVOTS_SHA
        assert digest(product) == PRODUCT_SHA
        assert b"object at 0x" not in pivots.read_bytes()
        assert b"object at 0x" not in product.read_bytes()
        outputs.append(out_path.read_bytes())
        pivot_tables.append(pivots.read_bytes())
        pivot_products.append(product.read_bytes())

    assert outputs[0] == outputs[1]
    assert pivot_tables[0] == pivot_tables[1]
    assert pivot_products[0] == pivot_products[1]
    print(f"source_archive_sha256={ARCHIVE_SHA}")
    print(f"duplicate_stdout_sha256={STDOUT_SHA}")
    print(f"duplicate_nonunit_pivots_sha256={PIVOTS_SHA}")
    print(f"duplicate_pivot_product_sha256={PRODUCT_SHA}")
    print("duplicate_mathematical_outputs_byte_identical=true")
    print("reverse_first_stage_denominator_support_exact_U_H=true")
    print("reverse_chart_coverage_inference=false")
    print("V54D-AWS-CUSTODY-DIAGNOSTIC PASS")


if __name__ == "__main__":
    main()
