#!/usr/bin/env python3
"""Portable custody and endpoint verifier for the full-contact AWS gate."""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CASE = ROOT / "cases/max12_912_order3_nu_q8_p127_full_contact_jacobian_aws_20260825"
EXPECTED = {
    "README.md": "04e95ef0ada0680ce01fc51e27152a3fba4096b409e30f8538414b47b626ed82",
    "full_contact.py": "08a3d227accbc3c23a384db55bf44a050c5140e0034c70b95666fcd8fd51b6c8",
    "run_remote.sh": "208a983f36c2a1e80892ee40fb31fac80b31ce948d7b537e14b6f493b358ff38",
    "aws_box02_v1/result.json": "804f9fbb095832e79a4f01ad870ed87a55921b78f34ff9f83ae946da04b70549",
    "aws_box02_v1/run.meta": "e0156be64ffbfd84e03f2de3fd1d7aea1d14aad215ff832e4c16f400d3618f11",
    "aws_box02_v1/stderr.log": "6d7b708998d9d02cb770312e8a3ec340208ac8db8e0fa9d408091e02aeca49a4",
}
COMPILER = ROOT / "cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py"
COMPILER_SHA256 = "22b0cdc446d1e486d08757df5a3fff83b0506a492f16b9b2cf238966eb947545"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    for relative, expected in EXPECTED.items():
        got = digest(CASE / relative)
        assert got == expected, (relative, got, expected)
    assert digest(COMPILER) == COMPILER_SHA256

    payload = json.loads((CASE / "aws_box02_v1/result.json").read_text())
    assert payload["status"] == "PASS"
    assert payload["prime"] == 127
    assert payload["compiler_sha256"] == COMPILER_SHA256
    assert payload["q8_squarefree"] is True
    assert payload["correct_x1_factor"] == "3*v+1 over 9*v"
    assert all(value == [0] for value in payload["row_residuals"].values())
    assert payload["v_definition_residual"] == [0]
    assert payload["localizer_residual"] == [0]
    assert all(value != [0] for value in payload["old_wrong_x1_residuals"].values())
    units = payload["denominator_units"]
    assert len(units) == 8
    assert all(item["gcd_with_q8"] == [1] for item in units)
    assert all(item["norm_mod_127"] != 0 for item in units)
    jacobian = payload["full_relative_jacobian"]
    assert jacobian["rows"] == 8
    assert jacobian["rank_at_every_geometric_q8_contact"] == 8
    assert jacobian["gcd_determinant_q8"] == [1]
    assert jacobian["determinant_norm_mod_127"] == 88

    metadata = (CASE / "aws_box02_v1/run.meta").read_text()
    assert "rc=0" in metadata
    assert "endpoint=PASS" in metadata
    assert "host=ip-172-30-0-186" in metadata
    print("PASS full-contact corrected-Q8 custody and endpoint")


if __name__ == "__main__":
    main()
