#!/usr/bin/env python3
"""Lightweight custody and exact-union verifier for frozen V78C evidence.

This does not import or execute the producer replay.
"""

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent
EXPONENTS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
             16, 17, 18, 19, 20, 21, 22, 23, 24)
ARCHIVE_SHA = "b566a57ea50c3f4d24c091f006fe321aa9bb813368049773ee89b347d1284be4"
UNION_SHA = "e14ff29cf5ca4301640215f10c3f0911df169cfac03b79624b6e18d088f360ef"
Q2_RAW = "816da33cd8e77b035740b7811e56d9ac8742160974a690506dec35d9b002d6a0"
Q2_REM = "1acfd5c0169b466d16c6d87de34b3ec0f5b78f6bb073a6191e9bed2ac36775b3"
Q3_RAW = "70d253cd30303d5ae6ebf81e8de0b2c12a00b66b060c996f0a898dbaf708682c"
Q3_REM = "3dd07bb5e097ea920104e085d857e519915ba214145d862576bd9cb9d3792458"
PASS = "TD6-A3-ALL-Q-VECTOR-AD-P12-SHARD PASS"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


assert digest(HERE / "archives/td6-v78c-sharded-source-20260826.tar.gz") == ARCHIVE_SHA
unions = []
for host in ("box02", "r6d"):
    root = HERE / "evidence" / host
    header = None
    rows = []
    for exponent in EXPONENTS:
        run = root / f"q{exponent}"
        assert run.joinpath("rc").read_text().strip() == "0"
        stdout = run.joinpath("stdout").read_text()
        assert PASS in stdout.splitlines()
        meta = run.joinpath("launch.meta").read_text()
        assert f"exponent={exponent}" in meta.splitlines()
        assert "virtual_memory_cap_kib=12582912" in meta.splitlines()
        assert "timeout_seconds=14400" in meta.splitlines()
        assert f"source_archive_sha256={ARCHIVE_SHA}" in meta.splitlines()
        assert "requested_q_denominator_radicals_subset_U_H_B3=true" in stdout.splitlines()
        assert "requested_q_derivative_source_identity_exact=true" in stdout.splitlines()
        assert "lambda_prime_aggregate_omission_negative_control=true" in stdout.splitlines()
        assert "P12_source_row_omission_negative_control=true" in stdout.splitlines()
        assert "FIRST_conormal_rank=0/1" in stdout.splitlines()
        table_lines = run.joinpath("output/ALL_Q_P12_COLUMNS.tsv").read_text().splitlines()
        assert len(table_lines) == 2
        if header is None:
            header = table_lines[0]
        assert table_lines[0] == header
        fields = table_lines[1].split("\t")
        assert int(fields[0]) == exponent
        assert int(fields[5]) == 14
        if exponent <= 14:
            assert int(fields[3]) > 0
        else:
            assert int(fields[3]) == 0
        rows.append(table_lines[1])
    assert header is not None
    assembled = ("\n".join([header, *rows]) + "\n").encode()
    frozen = root.joinpath("ALL_Q_P12_COLUMNS.UNION.tsv").read_bytes()
    assert assembled == frozen
    assert sha256(frozen).hexdigest() == UNION_SHA
    unions.append(frozen)

assert unions[0] == unions[1]
union_rows = {
    int(line.split("\t", 1)[0]): line.split("\t")
    for line in unions[0].decode().splitlines()[1:]
}
assert tuple(union_rows) == EXPONENTS and 15 not in union_rows
assert union_rows[2][2] == Q2_RAW and union_rows[2][4] == Q2_REM
assert union_rows[3][2] == Q3_RAW and union_rows[3][4] == Q3_REM

v32 = HERE.joinpath("evidence/anchors/V32_q2.stdout").read_text()
assert Q2_RAW in v32 and Q2_REM in v32
v77r = HERE.joinpath("evidence/anchors/V77R_q3_box02.stdout").read_text()
assert Q3_RAW in v77r and Q3_REM in v77r
review = HERE.joinpath("evidence/anchors/V77R_review.md").read_text()
assert "CONFIRMED" in review.splitlines()

for exponent in EXPONENTS:
    for relative in (
        "output/ALL_Q_P12_COLUMNS.tsv",
        "output/FIRST_CONORMAL.tsv",
        "output/FIRST_KERNEL.exact.tsv",
    ):
        assert (HERE / "evidence/box02" / f"q{exponent}" / relative).read_bytes() == (
            HERE / "evidence/r6d" / f"q{exponent}" / relative
        ).read_bytes()

print("TD6 V78C frozen custody/dual-union/anchor verification PASS")
