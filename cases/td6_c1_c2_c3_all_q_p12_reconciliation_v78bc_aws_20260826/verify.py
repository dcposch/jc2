#!/usr/bin/env python3
"""Lightweight V78B/V78C custody and byte-reconciliation checker."""

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V78C = ROOT / "cases/td6_c1_c2_c3_all_q_p12_shards_v78c_aws_20260826"
TABLE_SHA = "e14ff29cf5ca4301640215f10c3f0911df169cfac03b79624b6e18d088f360ef"
ARCHIVE_SHA = "cc7717b46d667726d0b4b51b51027b19dfbbb3823104018fca4a912af6eb6579"
PASS = "TD6-A3-ALL-Q-VECTOR-AD-P12 PASS"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


assert digest(HERE / "archives/td6-v79-v78b-source-20260825.tar.gz") == ARCHIVE_SHA
tables = []
for host in ("box02", "r6d"):
    run = HERE / "evidence/v78b" / host
    assert run.joinpath("rc").read_text().strip() == "0"
    stdout = run.joinpath("stdout").read_text()
    assert PASS in stdout.splitlines()
    for marker in (
        "q15_lower_target_shear_gauge_excluded=true",
        "transport_all_q_source_keys_exact_and_singleton=true",
        "all_q_direct_qprime_batched_omission_control=true",
        "FIRST_conormal_rank=0/22",
        "genuine_P12_source_compiler=true",
        "P12_source_row_omission_negative_control=true",
        "lambda_prime_aggregate_omission_negative_control=true",
        "all_q_derivative_source_identities_exact=true",
        "all_q_denominator_radicals_subset_U_H_B3=true",
    ):
        assert marker in stdout.splitlines()
    meta = run.joinpath("launch.meta").read_text().splitlines()
    assert f"source_archive_sha256={ARCHIVE_SHA}" in meta
    assert "virtual_memory_cap_kib=33554432" in meta
    assert "timeout_seconds=14400" in meta
    table = run.joinpath("output/ALL_Q_P12_COLUMNS.tsv").read_bytes()
    assert sha256(table).hexdigest() == TABLE_SHA
    assert len(table.decode().splitlines()) == 23
    tables.append(table)

assert tables[0] == tables[1]
for host in ("box02", "r6d"):
    shard_union = V78C / "evidence" / host / "ALL_Q_P12_COLUMNS.UNION.tsv"
    assert digest(shard_union) == TABLE_SHA
    assert shard_union.read_bytes() == tables[0]

assert digest(V78C / "MANIFEST.sha256") == (
    "c93959e757927dc238e01aa4ff5d053ebe9154ce5e33f0a8cae2581d981154ad"
)
print("TD6 V78B/V78C simultaneous-shard reconciliation PASS")
