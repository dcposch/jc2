#!/usr/bin/env python3
"""Custody verifier for the fail-closed Q8bar factorization."""

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent
EXPECTED = {
    "README.md": "8f33cceb5ce4eaba4cec66204ff75099077d64b00ee310850a1d9cea2576b533",
    "factor_q8.sing": "110c5207b17fe580021917f552abe370fa356bbf93b8a5fe6c2636298128923f",
    "run_remote.sh": "f064b9b216e4bddd6a2118a85c0564cec74f73b0e4e28d126472aca660d70e0c",
    "aws_box02_v2/result.out": "a14f349c4e37aadbf3a8786fc2ff43edaa6eb76312d045d7d5e5d96f412981a3",
    "aws_box02_v2/run.meta": "f0013258de48026f4c079dda898ddb91eeeae4b256d888a9ec518ec67b41f8b9",
    "aws_box02_v2/stderr.log": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
}


def main() -> None:
    for relative, expected in EXPECTED.items():
        got = sha256((HERE / relative).read_bytes()).hexdigest()
        assert got == expected, (relative, got, expected)
    text = (HERE / "aws_box02_v2/result.out").read_text()
    for marker in (
        "Q8-P127-FACTORIZATION",
        "squarefree_gcd=1",
        "factor_count=4",
        "_[1]=v+60",
        "_[2]=v-58",
        "_[3]=v-26",
        "_[4]=v5+53v4+38v3+26v2-9v-48",
    ):
        assert text.count(marker) == 1, marker
    assert "?" not in text and "error occurred" not in text
    metadata = (HERE / "aws_box02_v2/run.meta").read_text()
    assert "rc=0" in metadata and "endpoint=PASS" in metadata
    print("PASS Q8bar factorization custody")


if __name__ == "__main__":
    main()

