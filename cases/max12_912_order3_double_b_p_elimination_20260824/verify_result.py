#!/usr/bin/env python3
"""Validate the frozen exact univariate double-B elimination output."""

from __future__ import annotations

from functools import reduce
import hashlib
from math import gcd
from pathlib import Path
import re
import subprocess
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
GENERATOR = ROOT / "cases/max12_912_order3_nu1_probe_20260824/generate_double_b_msolve.py"
PARENT = ROOT / "cases/max12_912_order3_fibre_20260824/order3_fibre.py"
VARIABLES = ("x0", "x1", "x2", "x3", "x4", "x5", "q", "ip", "p")
EXPECTED = {
    "input.ms": "1bde828bfe3cddb7342a10436b34913c6cf1adebb4d668f0947b3a1f1ad1f287",
    "metadata.txt": "86479cac4b58efa8e18b6786b15b8972004dc3974b4b670465937d7c406f1ba3",
    "result.out": "50d71a0b76239db801e5c75ff9497f33d62086c4b8f7b5fd0a3e1bfb67852a75",
    "stderr.log": "162dddcb47c9bb4cf6f9255119ca2f83237ddf8bae23b7e821dd860d9e90644b",
    "mod_32003.sing": "8acf071e401e0ed01e3dcf2da5dff184448096bb8ada7615efbaff872b6ae65c",
    "mod_32003.out": "ad04f830fdf9a2023d600be4f11260e3122675ea25f377d5b0f1921315c55604",
    "mod_100003.sing": "f1c609913f5ff9c7dee6349f7b9c1813ef61205fce13893ad1d193a9b27540dc",
    "mod_100003.out": "ebb70f4e947e4809bf2a88da75d5f744bdcfcab8eea8ff1173405b5ed5936cc2",
    "mod_104729.sing": "b87df435eddb6be86adf5bfee92496380b8c0f9321365b53bfcf909f0a6e0aaa",
    "mod_104729.out": "0015bde454394895b754e40d6d6252634b637f65e346dabd533dcddb0293bdfc",
}
GENERATOR_SHA256 = "5c1c6e6d6570d58f9c9f6104be151e6da68c90d0e2855af9021f533b92420b01"
PARENT_SHA256 = "a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf"
COEFFICIENT_SHA256 = "459c4436ddc06c086171baab73a41bd9626e356c5749f445bf82766938431e68"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def parse_polynomial(polynomial: str) -> list[tuple[int, int]]:
    parsed: list[tuple[int, int]] = []
    for term in re.findall(r"[+-]?[^+-]+", polynomial.strip()):
        match = re.fullmatch(r"([+-]?\d+)?(?:\*?p(?:\^(\d+))?)?", term)
        assert match is not None, term
        default = -1 if term.startswith("-") else 1
        coefficient = int(match.group(1) or default)
        exponent = int(match.group(2) or (1 if "p" in term else 0))
        assert coefficient != 0
        parsed.append((coefficient, exponent))
    return parsed


def main() -> None:
    for name, expected in EXPECTED.items():
        actual = digest((HERE / name).read_bytes())
        assert actual == expected, (name, actual, expected)
    assert digest(GENERATOR.read_bytes()) == GENERATOR_SHA256
    assert digest(PARENT.read_bytes()) == PARENT_SHA256

    input_bytes = (HERE / "input.ms").read_bytes()
    input_lines = input_bytes.decode().splitlines()
    assert input_lines[0] == ", ".join(VARIABLES)
    assert input_lines[1] == "0"
    assert input_bytes.decode().rstrip().endswith("p*ip-1")
    assert input_bytes.count(b",\n") == 8
    regenerated = subprocess.run(
        [sys.executable, str(GENERATOR), "--characteristic", "0", "--mode", "saturated", "--order", "p-last"],
        check=True,
        capture_output=True,
    ).stdout
    assert regenerated == input_bytes

    metadata = (HERE / "metadata.txt").read_text()
    for needle in (
        "backend=msolve-sat-elim-p-last",
        "characteristic=0",
        "msolve=0.10.1",
        "command=msolve saturated elimination order=p-last block=8",
        "exit_code=0",
        "final_status=DONE",
        "result_sha256=" + EXPECTED["result.out"],
    ):
        assert needle in metadata, needle

    stderr = (HERE / "stderr.log").read_text()
    for needle in (
        "#variables                       9",
        "#equations                       9",
        "#invalid equations               0",
        "field characteristic             0",
        "monomial order             ELIM(8)",
        "#polynomials to lift              1",
        "Max coeff. bitsize             1828",
        "#primes                         120",
        "#bad primes                       0",
    ):
        assert needle in stderr, needle

    result = (HERE / "result.out").read_text()
    for needle in (
        "#field characteristic: 0",
        "#variable order:       p",
        "#length of basis:      1 element",
    ):
        assert needle in result, needle
    body = result.split("#---\n[", 1)[1]
    assert body.endswith("]:\n")
    polynomial = body[:-3]
    parsed = parse_polynomial(polynomial)

    coefficients = [coefficient for coefficient, _ in parsed]
    exponents = [exponent for _, exponent in parsed]
    assert len(parsed) == 71
    assert exponents == list(range(630, -1, -9))
    assert parsed[-1][1] == 0 and parsed[-1][0] != 0
    assert reduce(gcd, (abs(value) for value in coefficients)) == 1
    coefficient_bytes = "\n".join(str(value) for value in coefficients).encode()
    assert digest(coefficient_bytes) == COEFFICIENT_SHA256

    for prime in (32003, 100003, 104729):
        modular_text = (HERE / f"mod_{prime}.out").read_text()
        assert f"PRIME={prime}" in modular_text
        assert "dim=0" in modular_text and "deg=1188" in modular_text
        modular = parse_polynomial(modular_text.split("P=\n", 1)[1])
        inverse_lead = pow(parsed[0][0], -1, prime)
        expected_modular = [
            ((coefficient * inverse_lead) % prime, exponent)
            for coefficient, exponent in parsed
        ]
        actual_modular = [
            (coefficient % prime, exponent) for coefficient, exponent in modular
        ]
        assert actual_modular == expected_modular, prime

    print("PASS exact p-elimination validation")
    print("result_sha256=" + EXPECTED["result.out"])
    print("basis_length=1")
    print("degree_p=630")
    print("term_count=71")
    print("exponents=9*k_for_k_0_through_70")
    print("constant_term_nonzero=YES")
    print("integer_content=1")
    print("coefficient_sha256=" + COEFFICIENT_SHA256)
    print("independent_singular_modular_matches=32003,100003,104729")


if __name__ == "__main__":
    main()
