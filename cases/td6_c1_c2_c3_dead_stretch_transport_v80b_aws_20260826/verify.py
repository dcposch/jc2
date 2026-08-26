#!/usr/bin/env python3
"""Lightweight custody/equality verifier; performs no algebra."""

import csv
from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent
LEVELS = list(range(6, 17))
EXPECTED_FALSE = {6, 7, 8, 9, 11, 12, 13, 14, 16}
EXPECTED_TRUE = {10, 15}
FIRST_BAD_SHA = "0458f40e62da3f7fc5d841ab77d1d10a1215791299991bba2285073d090cccda"
SOURCE_ARCHIVE_SHA = "6312e21a889fe4696558ae46a0b986f06f6a9af0f1f2023c4ba416c539d5b607"
SOURCE_MANIFEST_SHA = "22e639bb7fb0dca41fbdb38840f9c2e3b84302fe5b9f0348c8c724efa616438a"
PRODUCER_SHA = "7eada4e12b8b56feb0a4e2d7c15281b01b34b942beb175709f4579bfffcbafe7"


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def marker(text, key):
    prefix = key + "="
    values = [line[len(prefix):] for line in text.splitlines() if line.startswith(prefix)]
    assert len(values) == 1, (key, values)
    return values[0]


assert digest(HERE / "source" / "source.tar.gz") == SOURCE_ARCHIVE_SHA
assert digest(HERE / "source" / "SOURCE.sha256") == SOURCE_MANIFEST_SHA
assert digest(HERE / "source" / "replay_shard.py") == PRODUCER_SHA
producer = (HERE / "source" / "replay_shard.py").read_text()
assert "fb.CENTER = (Q(1), Q(1), Q(1))" in producer

with (HERE / "DEAD_TRANSPORT_11_VECTOR.tsv").open(newline="") as stream:
    rows = {int(row["level"][1:]): row for row in csv.DictReader(stream, delimiter="\t")}
assert set(rows) == set(LEVELS)

for level in LEVELS:
    expected = rows[level]
    host_text = {}
    for host in ("r6d", "box03"):
        run = HERE / "evidence" / host / f"d{level}"
        assert (run / "rc").read_text().strip() == "0"
        stdout = (run / "stdout").read_text()
        host_text[host] = stdout
        assert marker(stdout, "producer") == "TD6-A3-DEAD-STRETCH-TRANSPORT-V80B-SHARD"
        assert marker(stdout, "dead_level") == f"d{level}"
        assert marker(stdout, "transport_rank") == "3470/3602;free=132"
        assert stdout.splitlines()[-1] == "TD6-A3-DEAD-STRETCH-TRANSPORT-V80B-SHARD PASS"
        for key in (
            "dead_derivative_row_keys",
            "dead_derivative_terms",
            "dead_stretch_matrix_derivative_omission_failures",
            "transport_compatibility_forms",
            "transport_compatibility_table_entries",
            "transport_compatibility_digest",
            "transport_compatibility_table_sha256",
        ):
            table_key = {
                "dead_derivative_row_keys": "derivative_rows",
                "dead_derivative_terms": "derivative_terms",
                "dead_stretch_matrix_derivative_omission_failures": "omission_failures",
                "transport_compatibility_forms": "compatibility_forms",
                "transport_compatibility_table_entries": "compatibility_entries",
                "transport_compatibility_digest": "compatibility_digest",
                "transport_compatibility_table_sha256": "compatibility_table_sha256",
            }.get(key, key)
            assert marker(stdout, key) == expected[table_key], (host, level, key)
        consistent = marker(stdout, "transport_compatibility_affine_consistent")
        assert consistent == expected["consistent"]
        if level in EXPECTED_FALSE:
            assert consistent == "false"
            assert marker(stdout, "transport_compatibility_first_inconsistency_sha256") == FIRST_BAD_SHA
        else:
            assert level in EXPECTED_TRUE and consistent == "true"

        table = run / "evidence" / f"DEAD_D{level}_TRANSPORT_COMPATIBILITY.tsv"
        assert digest(table) == expected["compatibility_table_sha256"]

    # Hostnames and output paths legitimately differ; all mathematical markers
    # and the full emitted exact tables are required to agree.
    assert marker(host_text["r6d"], "transport_compatibility_digest") == marker(
        host_text["box03"], "transport_compatibility_digest"
    )

print("TD6 V80B POINT-DISCRIMINATOR CUSTODY PASS")
print("scope=(C,V,U)=(1,1,1);beta=0;pure_axes_only")
print("joint_or_generic_claim=false")
