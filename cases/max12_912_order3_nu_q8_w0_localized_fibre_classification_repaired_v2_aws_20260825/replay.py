#!/usr/bin/env python3
"""Small fail-closed replay for the V2 localized-fibre repairs."""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def read(rel: str) -> str:
    return (HERE / rel).read_text()


def require_once(text: str, marker: str) -> None:
    assert text.count(marker) == 1, (marker, text.count(marker))


def main() -> None:
    scan = read("aws_box02_v2/q8_w0_v2_irred_prime_scan_box02_v1/stdout")
    for marker in (
        '"least_good_prime": 7',
        '"irreducible": true',
        '"gcd_p4_ascending": [',
        '"xp8_minus_x_remainder_ascending": [',
        "Q8_IRREDUCIBLE_PRIME_SEARCH_PASS",
    ):
        require_once(scan, marker)
    assert '"gcd_p4_ascending": [\n      1\n    ]' in scan
    assert '"xp8_minus_x_remainder_ascending": [\n      0\n    ]' in scan

    factor = read("aws_box02_v2/q8_w0_v2_q8_mod7_factor_singular_box02_v2/stdout")
    for marker in (
        "factor_1_degree=8",
        "factor_count=1",
        "degree_sum=8",
        "degree8_count=1",
        "mutual_divisibility=1",
        "Q8_MOD7_SINGULAR_IRREDUCIBLE_PASS",
    ):
        require_once(factor, marker)
    factor_meta = read("aws_box02_v2/q8_w0_v2_q8_mod7_factor_singular_box02_v2/run.meta")
    require_once(factor_meta, "rc=0")

    # V1 of the Singular factor parser is an intentional negative control.
    bad = read("aws_box02_v2/q8_w0_v2_q8_mod7_factor_singular_box02_v1/stdout")
    assert "is not supported" in bad
    assert "Q8_MOD7_SINGULAR_IRREDUCIBLE_PASS" not in bad

    lanes = (
        "aws_box02_v2/q8_w0_v2_nonq8_rho0_Q_std_block_box02_v1",
        "aws_box02_v2/q8_w0_v2_nonq8_rho_loaded_Q_std_block_box02_v1",
        "aws_box03_v2/q8_w0_v2_nonq8_rho0_Q_slimgb_dp_box03_v1",
        "aws_box03_v2/q8_w0_v2_nonq8_rho_loaded_Q_slimgb_dp_box03_v1",
    )
    for rel in lanes:
        output = read(f"{rel}/stdout")
        require_once(output, "Q8_W0_FIBRE_STRATUM_PASS")
        require_once(output, "original_remainder_zero=1")
        require_once(output, "dim=-1")
        require_once(output, "size=1")
        meta = read(f"{rel}/run.meta")
        require_once(meta, "rc=0")
        source = read(f"{rel}/source.sha256")
        assert "a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf" in source
        assert "5dcb0a67d79859c04d83d2c20ff8518a148a78c1229f42b00169c5842d5e7256" in source

    expected = {
        "scan_stdout": "eb389979e8c75f7b85d18f413c70ef6413d7ff1738365b62be35a1915e3fd1e2",
        "factor_v2_stdout": "8a05b14f4f0a9aa86eb213c55f6853c7b7019138f123f7d607e85bd1e45fba1b",
        "box02_rho0_stdout": "85cbc6c61ca5eea890e80c6d0354c4ad99fe56e0518276f24327b726d99c9e8e",
        "box02_rho_loaded_stdout": "85a005232722220b17a3081ce3535b189a37d6fe24a0d17a99ae7499c2384d3e",
        "box03_rho0_stdout": "00625142b1288c9ea2299b1d9a2086c1d402a82b4bd9e5fbe6f6f9f9695c6464",
        "box03_rho_loaded_stdout": "197c6d52df65bb4f52aa879338c0501feb688bb0243bdd244a995b1999e613fd",
    }
    got = {
        "scan_stdout": digest(HERE / "aws_box02_v2/q8_w0_v2_irred_prime_scan_box02_v1/stdout"),
        "factor_v2_stdout": digest(HERE / "aws_box02_v2/q8_w0_v2_q8_mod7_factor_singular_box02_v2/stdout"),
        "box02_rho0_stdout": digest(HERE / "aws_box02_v2/q8_w0_v2_nonq8_rho0_Q_std_block_box02_v1/stdout"),
        "box02_rho_loaded_stdout": digest(HERE / "aws_box02_v2/q8_w0_v2_nonq8_rho_loaded_Q_std_block_box02_v1/stdout"),
        "box03_rho0_stdout": digest(HERE / "aws_box03_v2/q8_w0_v2_nonq8_rho0_Q_slimgb_dp_box03_v1/stdout"),
        "box03_rho_loaded_stdout": digest(HERE / "aws_box03_v2/q8_w0_v2_nonq8_rho_loaded_Q_slimgb_dp_box03_v1/stdout"),
    }
    assert got == expected, (got, expected)
    print("Q8_W0_LOCALIZED_FIBRE_REPAIRED_V2_REPLAY_PASS")


if __name__ == "__main__":
    main()
