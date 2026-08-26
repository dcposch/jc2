#!/usr/bin/env python3
"""Lightweight custody/text verifier for the V82S2 d10/d15 first gate."""

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent
ARCHIVE_SHA = "1def8eb0d2e84451a3112c3d3679dde879706bb361267b32f2fbe4b9c6467545"
TABLE_SHA = "68b4a3a151d2eb15e04b6bb1b0bb6e5656423289e4dca1260844476105ea6692"
EMPTY_SHA = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
RAW = {
    10: (1108, "e9c830bf3bc0abbc6a91b1e38a227ac0ae61b40bbeabf4e233dce62450f730f7"),
    15: (739, "4ea40ca645ec2dd523db2b85ab67cdf1b3c82fe28eb610a5220a44deedbb66ab"),
}
NORMALIZED = {
    10: "a586c3b473f5cff53939dc5a682ab1da45aff6c3e541f148c2aa39e0fdb24c15",
    15: "359df41d98d795657a08cf02b4175602d0d1e711f851da3c9c87524119397245",
}
STDOUT_SHA = {
    ("r6d", 10): "20f608bf2db3ff5873ac0e22b1843a11424dfe2b9a9590f4924224c8a3e71f08",
    ("r6d", 15): "3c19e999b78688ba06d22810f977022454802344864428c76acdc0d9399df5cf",
    ("box03", 10): "5b7acb475d3bfbaac2c489347007151fa42c805fac0674d7695cce3d9215bd02",
    ("box03", 15): "7799062ef42a3171494ddc2d7dd353333b4a63a6ff15398bcab861c3e8330624",
}
HOSTNAME = {"r6d": "ip-172-30-0-45", "box03": "ip-172-30-0-249"}


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def normalized(side, level, text):
    root = f"/home/ubuntu/runs/td6_v82s2_dead_first_{side}_20260826T0320Z"
    tag = f"td6_v82s_v2_{side}_d{level}_20260826T0320Z"
    return text.replace(HOSTNAME[side], "<HOST>").replace(
        tag, "<TAG>"
    ).replace(root, "<RUN>")


archive = HERE / "archives/td6-v82s2-kernel-dead-first-shards-source-20260826.tar.gz"
assert digest(archive) == ARCHIVE_SHA
expected_table = (
    "key\tcoordinate\taxis\tcoefficient_sha256\tcoefficient_exact\n"
).encode()
assert sha256(expected_table).hexdigest() == TABLE_SHA

for side in ("r6d", "box03"):
    registration = (HERE / "evidence" / side / "registration.meta").read_text()
    assert f"host_label={side}\n" in registration
    assert f"archive_sha256={ARCHIVE_SHA}\n" in registration
    for level in (10, 15):
        lane = HERE / "evidence" / side / "lanes" / f"d{level}"
        assert (lane / "rc").read_text() == "0\n"
        stdout = (lane / "stdout").read_text()
        assert digest(lane / "stdout") == STDOUT_SHA[(side, level)]
        assert stdout.splitlines()[-1] == "TD6-A3-KERNEL-DEAD-FIRST-SHARD-V82S PASS"
        raw_count, raw_sha = RAW[level]
        markers = (
            "empty_first_conormal_table_positive_control=true",
            "symbolic_center_asserted_before_transport=true",
            "symbolic_center_asserted_after_transport=true",
            "transport_rank=3470/3602;free=132",
            "transport_axis_compatibility_exact_zero=true",
            f"first_raw_axis_entries={raw_count};sha256={raw_sha}",
            f"first_omitted_axis_entries=0;sha256={EMPTY_SHA}",
            "dead_source_column_omission_control=true",
            "actual_first_conormal_table_is_header_only=true",
            "first_rank=38/132",
            "first_dependent_count=0",
            "first_axis_conormal_rank=0/1",
            "first_axis_conormal_coordinate_count=0",
            "first_axis_denominator_factor=(1, [])",
            "all_first_pivot_source_combinations_replayed=true",
        )
        for marker in markers:
            assert marker in stdout, (side, level, marker)
        table = lane / "evidence" / f"D{level}_FIRST_CONORMAL.tsv"
        control = lane / "evidence/empty_table_control" / f"D{level}_FIRST_CONORMAL.tsv"
        assert table.read_bytes() == expected_table
        assert control.read_bytes() == expected_table
        assert digest(table) == TABLE_SHA == digest(control)
        result_lines = (lane / "RESULTS.sha256").read_text()
        assert digest(lane / "stdout") in result_lines
        assert digest(lane / "stderr") in result_lines

for level in (10, 15):
    r6d = normalized(
        "r6d", level,
        (HERE / "evidence/r6d/lanes" / f"d{level}/stdout").read_text(),
    )
    box03 = normalized(
        "box03", level,
        (HERE / "evidence/box03/lanes" / f"d{level}/stdout").read_text(),
    )
    assert r6d == box03
    assert sha256(r6d.encode()).hexdigest() == NORMALIZED[level]

print("dual_host_d10_d15_normalized_stdout_byte_identical=true")
print("dead_kernel_first_zero_axes=d10,d15")
print("dead_kernel_first_raw_columns_nonzero=true")
print("dead_kernel_first_conormal_rank=0/2")
print("dead_kernel_first_denominator=1")
print("conditional_V81C_V78_transport_first_kernel_dimension=24")
print("scope=generic_fraction_field_fixed_A3_square_zero_transport_first_only")
print("TD6-V82S2-KERNEL-DEAD-FIRST-CUSTODY PASS")
