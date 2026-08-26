#!/usr/bin/env python3
"""Lightweight custody and exact triangular-rank verifier for V81C."""

import csv
from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent
LEVELS = tuple(range(6, 17))
ACTIVE = (6, 7, 8, 9, 11, 12, 13, 14, 16)
GENERIC_SHA = {
    6: "2a7a07e6deffc839f5c7d732c319c0b9bea57043449882a4aeff02e908229a9f",
    7: "7fd520525d39a5b2ce1b9852f16503892c8bf52d722381689a7d062ec7a1d14f",
    8: "1677932db17e3b27def30d6d52fda4fea6985dfa743f6352f21d5dd300d4d1df",
    9: "72c20b73cfe692ae88105688872bd7fb8799b4a2128ea6558eb6444fee9a1bae",
    10: "a30f85978bc937ca998bb0c9cb299171b0a39e1e7de406ae7d7166c80bcee1df",
    11: "b9c07833e3e5254ad2d6bc52dd08af59b05a13844402e81b707ec4f1faf2ba2f",
    12: "8d52a261af0a53bc2b48dfefda477c84d892e304d6a0ed1ba6a18f3517d05518",
    13: "bc1c2d4b109b36e017dd72ff53a252bba161d3102b469a984de5f2fd78dd0773",
    14: "0e0082ad308f39043727c66cc8f51f70f7056e31f181443937f6b0bee2ac4605",
    15: "a30f85978bc937ca998bb0c9cb299171b0a39e1e7de406ae7d7166c80bcee1df",
    16: "2135039b2db2bca77df027a38bd51168c6fdb6ba9a21d61bbed93efb6d6bc3ae",
}
POINT_SHA = {
    6: "df2eae2216967197e159e77e2b6709811f366f3baea307bb4febb4b53e3ffd07",
    7: "f067674ed1c0516be4eeef68646e5a827bed68f99449942bed1a0721338f7ca0",
    8: "a69aef0562e43b12c788b9390dc9424bc188b495d035c7910e6b7b1be7a89fce",
    9: "b77be35ba8072970e1e7318752950a2660d8a9c191256ae5545896798031cb03",
    10: "a30f85978bc937ca998bb0c9cb299171b0a39e1e7de406ae7d7166c80bcee1df",
    11: "637cbc2485629bdbb929af8c8de435febb4be400ef2a18883c4ebc56a8797437",
    12: "9376efbfe6b0c53c26bd919025399d6d16c9c1c40295dc1080e72fd085ab879c",
    13: "06cfdd710b7fc22c495c880239f8dde69d96291c9e2145ea8401bd339009f4a2",
    14: "aee20602cbaa65f2d6a12ad9b7b7fb48b63e724f68c8df2440e2b89bf19c991b",
    15: "a30f85978bc937ca998bb0c9cb299171b0a39e1e7de406ae7d7166c80bcee1df",
    16: "7e40146215fb5416235c7ab9b3aa57c84a62147ca0a34e47797b93c48796022a",
}
DIAGONAL = (
    "(('0', '1'), ('0', '1'), ('0', '1'), ('0', '1'), ('0', '1'), "
    "('0', '1'), ('15625/3', '1'), ('0', '1'), ('0', '1'), "
    "('0', '1'), ('0', '1'), ('0', '1'), ('0', '1'), ('0', '1'), "
    "('0', '1'), ('0', '1'), ('0', '1'), ('0', '1'))"
)


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def table(path):
    with path.open(newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    return {
        (row["kind"], row["key"], row["coordinate"]): row["coefficient_exact"]
        for row in rows
    }


assert digest(HERE / "archives/td6-v81c-generic-dead-transport-shards-source-20260826.tar.gz") == (
    "acc26126c64ef0e7746d0abaec8550d0d806a562be6e92bb8b8680383b9f9ff0"
)
assert digest(HERE / "dependencies/V78BC_REVIEW.md") == (
    "a3599e65f88015f60a3131572716affda748d8dc5963e3648bb35842246a1861"
)
assert digest(HERE / "dependencies/V78B_R6D.stdout") == (
    "118dcb50d003b24b445cb1968111fef4073d91f33725f6f77927e23105a6f5eb"
)
assert (HERE / "dependencies/V78B_R6D.rc").read_text() == "0\n"
q_stdout = (HERE / "dependencies/V78B_R6D.stdout").read_text()
for marker in (
    "transport_active_q_columns=2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24",
    "transport_all_q_source_keys_exact_and_singleton=true",
    "transport_matrix_all_q_derivative_zero=true",
    "transport_rhs_all_q_derivatives_retained=true",
    "TD6-A3-ALL-Q-VECTOR-AD-P12 PASS",
):
    assert marker in q_stdout
assert (HERE / "dependencies/V78BC_REVIEW.md").read_text().splitlines()[-1] == "CONFIRMED"

generic = {}
for side in ("r6d", "box03"):
    for level in LEVELS:
        lane = HERE / "evidence" / side / "lanes" / f"d{level}"
        assert (lane / "rc").read_text() == "0\n"
        stdout = (lane / "stdout").read_text()
        assert stdout.splitlines()[-1] == "TD6-A3-GENERIC-DEAD-TRANSPORT-V81C-SHARD PASS"
        for marker in (
            "symbolic_center_asserted_before_transport=true",
            "symbolic_center_asserted_after_transport=true",
            "transport_rank=3470/3602;free=132",
            f"d{level}_original_3470_pivot_rows_replayed=true",
            "V80B_selected_point_table_hash_reproduced=true",
        ):
            assert marker in stdout
        gpath = lane / "evidence" / f"GENERIC_DEAD_D{level}_TRANSPORT_COMPATIBILITY.tsv"
        ppath = lane / "evidence" / f"POINT_CVU111_DEAD_D{level}_TRANSPORT_COMPATIBILITY.tsv"
        assert digest(gpath) == GENERIC_SHA[level]
        assert digest(ppath) == POINT_SHA[level]
        if side == "r6d":
            generic[level] = table(gpath)
        else:
            assert gpath.read_bytes() == (
                HERE / "evidence/r6d/lanes" / f"d{level}/evidence"
                / f"GENERIC_DEAD_D{level}_TRANSPORT_COMPATIBILITY.tsv"
            ).read_bytes()
            assert ppath.read_bytes() == (
                HERE / "evidence/r6d/lanes" / f"d{level}/evidence"
                / f"POINT_CVU111_DEAD_D{level}_TRANSPORT_COMPATIBILITY.tsv"
            ).read_bytes()

assert not generic[10] and not generic[15]
matrix = []
for row_level in ACTIVE:
    key = ("derivative-only", repr(("f", "F0", row_level - 20, 0)), "constant")
    matrix.append([generic[column_level].get(key, "") for column_level in ACTIVE])
for row_index, row in enumerate(matrix):
    assert row[row_index] == DIAGONAL
    assert all(not row[column] for column in range(row_index + 1, len(row)))

# The nine-by-nine lower-triangular minor has determinant DIAGONAL^9 != 0.
# There are only nine nonzero dead columns, so the dead rank is exactly nine;
# reviewed q columns are zero and d10,d15 are zero, hence the 33-axis rank is
# nine and the fraction-field kernel dimension is 33-9=24.
print("dual_host_all_11_dead_tables_byte_identical=true")
print("dead_transport_zero_columns=d10,d15")
print("dead_transport_sentinel_axes=" + ",".join(f"d{x}" for x in ACTIVE))
print("dead_transport_sentinel_diagonal=" + DIAGONAL)
print("dead_transport_sentinel_determinant=diagonal^9_nonzero")
print("dead_transport_rank=9/11")
print("reviewed_q_transport_rank=0/22")
print("full_33_axis_transport_rank=9/33")
print("full_33_axis_transport_kernel_dimension=24")
print("scope=generic_fraction_field_E(C,V,U)_transport_source_incidence_only")
print("TD6-V81C-TRIANGULAR-RANK-CUSTODY PASS")
