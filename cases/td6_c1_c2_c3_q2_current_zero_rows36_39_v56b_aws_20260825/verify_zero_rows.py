#!/usr/bin/env python3
"""Verify that V56B current rows 36--39 are canonical empty polynomials."""

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent
EXPECTED_ARCHIVE = "afb1bbab4572893eb1c5b96faa82832fbfd55508142e9085711952c964cdcc2a"
EXPECTED_PARENT = "3cc0fc3bc4a55810c4d4320b53ff77a48341045c06f556cd6243119b8fe4c332"
EXPECTED_SHARD_SOURCE = "589ea51ff48bd0038eb88e93a2bd0fb2dfcc8506208c903a21b7218277e15317"
EXPECTED_V55_V56_MANIFEST = "fa1672f0b53f23690ab4ffa8e91e9529d144ee51f2c1b82b5bece58ee573512a"
EXPECTED_EMPTY_DICT = "84315a814615731cc801bec5a1747c2ad15d6a4262aae78bbeb0847f694495b1"
EXPECTED_EMPTY_LIFT = "d78fca8ea1e9be5f4c633157af7777ac0f16200b1e26ff3a7aa40fb86e5655ee"


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def require(text, marker):
    assert marker in text, marker


def main():
    # The pinned canonical serializer maps an empty dict to ("dict", ()).
    # This is the exact representation hashed by the producer's n.digest.
    empty_digest = sha256(repr(("dict", ())).encode()).hexdigest()
    assert empty_digest == EXPECTED_EMPTY_DICT
    assert digest(HERE / "source" / "canonical_parent_replay.py") == EXPECTED_PARENT
    assert digest(HERE / "source" / "shard_replay.py") == EXPECTED_SHARD_SOURCE
    assert digest(HERE / "source" / "V55_V56_SOURCE.sha256") == EXPECTED_V55_V56_MANIFEST

    stdout_digests = []
    for index in range(36, 40):
        evidence = HERE / "evidence" / f"s{index}"
        assert (evidence / "rc").read_text().strip() == "0"
        assert (evidence / "archive.sha256").read_text().split()[0] == EXPECTED_ARCHIVE
        stderr = (evidence / "shard.stderr").read_text()
        assert "Traceback" not in stderr
        require(stderr, "Exit status: 0")
        stdout = (evidence / "shard.stdout").read_text()
        for marker in (
            "producer=TD6-A3-Q2-SOURCE-ROW-SHARDS-V55-V56",
            "shard_mode=current",
            f"shard_index={index}",
            "shard_count=40",
            f"parent_sha256={EXPECTED_PARENT}",
            f"current_shard_row[0]_index={index}",
            f"current_shard_row[0]_key=('X0', {index})",
            f"current_shard_row[0]_raw_sha256={EXPECTED_EMPTY_DICT}",
            f"current_shard_row[0]_lift_sha256={EXPECTED_EMPTY_LIFT}",
            "current_total_original_row_count=40",
            "current_shard_selected_count=1",
            f"current_shard_indices=[{index}]",
            "current_shard_original_row_replay=true",
            "full_source_identity_replayed=false",
            "TD6-A3-Q2-SOURCE-ROW-SHARD-V56 PASS",
        ):
            require(stdout, marker)
        source_check = (evidence / "v55v56-source-check.txt").read_text()
        require(source_check, "jc2/cases/td6_c1_c2_c3_q2_source_row_shards_v55_v56_20260825/replay.py: OK")
        stdout_digests.append(digest(evidence / "shard.stdout"))

    print(f"canonical_empty_repr={repr(('dict', ())) }")
    print(f"canonical_empty_sha256={empty_digest}")
    print("verified_current_indices=[36, 37, 38, 39]")
    print("all_four_raw_polynomials_are_exactly_empty=true")
    print("all_four_empty_lifts_are_byte_identical=true")
    print("all_four_original_row_replays_pass=true")
    print(f"stdout_sha256={stdout_digests}")
    print("scope=fixed_A3_q2_beta_post_transport_current_rows_only")
    print("row_level_obstruction_found=false")
    print("V56B-CURRENT-ZERO-ROWS-36-39 PASS")


if __name__ == "__main__":
    main()
