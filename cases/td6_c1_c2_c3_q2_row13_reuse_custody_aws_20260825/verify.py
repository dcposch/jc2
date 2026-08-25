#!/usr/bin/env python3
"""Lightweight custody and scope verifier for the completed V56 row-13 shard."""

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent
EXPECTED = {
    "archives/td6-aws-handoff-20260825-v55v56.tar.gz":
        "afb1bbab4572893eb1c5b96faa82832fbfd55508142e9085711952c964cdcc2a",
    "aws_run/shard.stdout":
        "f5911fda0e8e64720d4e2e9a3eb40a3188526d323c9e7ed46beb8c69efc5b112",
    "aws_run/shard.stderr":
        "176bbe36763c77537f2e6ce72f75da6397d395607536e7eb7cf2c28aff1d4cfc",
    "aws_run/source-check.txt":
        "810af42a47b00093500cd68336bb9827288453344ada536689fc21a772f4b586",
    "aws_run/rc":
        "9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa",
    "aws_run/start_utc":
        "e6cd1011907922d5fcea09db59dfff435626ebcd8895af4e51857fdf26f0727d",
    "aws_run/end_utc":
        "b762033fb52c9ec17e1002af0213d5da78e2f9764975a32b18fba7741f36802b",
}

for relative, expected in EXPECTED.items():
    got = sha256((HERE / relative).read_bytes()).hexdigest()
    assert got == expected, (relative, got, expected)

assert (HERE / "aws_run/rc").read_text() == "0\n"
stdout = (HERE / "aws_run/shard.stdout").read_text()
for marker in (
    "N13_equals_k_beta_over_25=true",
    "N13_left_null_support=1",
    "N13_left_null_sha256=7f1bc7b18f1830b0c02a400107daa986b973f1966738431b13f35b29b2b679d8",
    "current_shard_indices=[13]",
    "current_shard_keys=[('X0', 13)]",
    "current_shard_row[0]_raw_sha256=ec21f21a48f771929134e861cc981b730de81622b7645905318bcfb5ca3b1652",
    "current_shard_row[0]_lift_sha256=95906283f5ec65f70ef4e9b666de1210d93f2f0980ed35f7ab8440e238ebc139",
    "current_shard_previous_ancestor_count=2",
    "current_shard_previous_ancestor_keys=[('X-1', 0), ('X-1', 14)]",
    "current_shard_original_row_replay=true",
    "full_source_identity_replayed=false",
    "full_A3_beta_family_killed=false",
    "TD6-A3-Q2-SOURCE-ROW-SHARD-V56 PASS",
):
    assert marker in stdout, marker

# Wrong-row/omission controls at the custody-logic layer.  The sole selected
# dependency is row 13; row 12 cannot silently substitute for it.
assert "current_shard_indices=[12]" not in stdout
assert "current_shard_keys=[('X0', 12)]" not in stdout
assert stdout.count("current_shard_row[0]_key=('X0', 13)") == 1

# Shard mode does not emit a denominator theorem.  Keep the handoff fail-closed.
assert "coefficient_denominator_radical_subset_U_H_B3=true" not in stdout
assert "generic_open_localization_repaired=true" not in stdout

print("TD6-V56-ROW13-REUSE-CUSTODY PASS")
print("generic_open_theorem_from_this_package=false")
