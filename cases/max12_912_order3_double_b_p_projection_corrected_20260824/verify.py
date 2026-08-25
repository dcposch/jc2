#!/usr/bin/env python3
"""Verify the corrected product-order double-B finite-prime controls."""

from __future__ import annotations

import hashlib
from pathlib import Path
import re
import subprocess
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
AWS = HERE / "aws"
EXACT = ROOT / "cases/max12_912_order3_double_b_p_elimination_20260824/result.out"
GENERATOR = ROOT / "cases/max12_912_order3_nu1_probe_20260824/generate_double_b_p_projection.py"
PRIMES = (32003, 65521, 100003, 104729, 105337, 105673, 200257,
          1000003, 1048573, 2147483629)
PINNED = {
    EXACT: "50d71a0b76239db801e5c75ff9497f33d62086c4b8f7b5fd0a3e1bfb67852a75",
    GENERATOR: "a0ab4878b6ed92370a45731aa44659a186d6e2be0823843306a8aac30a93665e",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_polynomial(text: str) -> list[tuple[int, int]]:
    terms: list[tuple[int, int]] = []
    for term in re.findall(r"[+-]?[^+-]+", text.strip()):
        match = re.fullmatch(r"([+-]?\d+)?(?:\*?p(?:\^(\d+))?)?", term)
        if match is None:
            raise AssertionError(term)
        default = -1 if term.startswith("-") else 1
        coefficient = int(match.group(1) or default)
        exponent = int(match.group(2) or (1 if "p" in term else 0))
        terms.append((coefficient, exponent))
    return terms


def exact_terms() -> list[tuple[int, int]]:
    result = EXACT.read_text()
    polynomial = result.split("#---\n[", 1)[1]
    assert polynomial.endswith("]:\n")
    terms = parse_polynomial(polynomial[:-3])
    assert [exponent for _, exponent in terms] == list(range(630, -1, -9))
    return terms


def main() -> None:
    for path, expected in PINNED.items():
        assert digest(path) == expected, path
    rational = exact_terms()
    result_hashes = {}
    for prime in PRIMES:
        lane = AWS / f"mod_singular_satp_slimgb_corrected_p{prime}"
        metadata = (lane / "metadata.txt").read_text()
        result_path = lane / "result.out"
        result = result_path.read_text()
        expected_input = subprocess.run(
            [sys.executable, str(GENERATOR), "--characteristic", str(prime),
             "--engine", "slimgb", "--saturate-p"],
            check=True, capture_output=True,
        ).stdout
        assert (lane / "input.sing").read_bytes() == expected_input, prime
        ring = (
            f"ring R={prime},(x0,x1,x2,x3,x4,x5,q,ip,p),"
            "(dp(8),dp(1));"
        )
        assert ring in expected_input.decode(), prime
        assert "final_status=DONE" in metadata and "exit_code=0" in metadata
        actual_hash = digest(result_path)
        assert f"result_sha256={actual_hash}" in metadata
        for marker in (
            "full_basis_size=10", "full_dimension=0", "full_degree=1188",
            "projection_size=1", "projection_basis=\nE[1]=",
        ):
            assert marker in result, (prime, marker)
        modular = parse_polynomial(result.split("projection_basis=\nE[1]=", 1)[1])
        inverse_lead = pow(rational[0][0], -1, prime)
        expected = [
            ((coefficient * inverse_lead) % prime, exponent)
            for coefficient, exponent in rational
        ]
        actual = [(coefficient % prime, exponent) for coefficient, exponent in modular]
        assert actual == expected, prime
        result_hashes[str(prime)] = actual_hash
    print("PASS corrected double-B product-order controls")
    print("primes=" + ",".join(map(str, PRIMES)))
    print("all_rings=(dp(8),dp(1))")
    print("all_dim=0")
    print("all_degree=1188")
    print("all_exact_P_mod_prime_matches=YES")
    for prime in PRIMES:
        print(f"result_sha256[{prime}]={result_hashes[str(prime)]}")


if __name__ == "__main__":
    main()
