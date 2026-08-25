#!/usr/bin/env python3
"""Validate and inspect the frozen exact double-B msolve output."""

from __future__ import annotations

import gzip
import hashlib
from collections import deque
from pathlib import Path
import re
import subprocess
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
GENERATOR = ROOT / "cases/max12_912_order3_nu1_probe_20260824/generate_double_b_msolve.py"
PARENT = ROOT / "cases/max12_912_order3_fibre_20260824/order3_fibre.py"
VARIABLES = ("p", "x0", "x1", "x2", "x3", "x4", "x5", "q", "ip")
EXPECTED = {
    "input.ms": "a01186da8d162c407baf53afcec44a49231d5549fdd2756f9a6fceaa240cc6ba",
    "metadata.txt": "f4ea358d7f88946f867f78948b850b3c7bbe3997003d8b02e6d59b288e001561",
    "stderr.log": "1fb1fbdea3bb847233c91f2b4fce0ae07efcc0376e8faa275e739f77529e0013",
    "result.out.gz": "85bb23ec14cac037ac59e41be84edfb1181c573943144b73aa0525fb9703edc4",
    "p0_primdec.sing": "c96c61276a97fb272807dbc93a70c7a54f5306341d262f45566107edcef056cd",
    "p0_dims.sing": "4f7bae808b4a6b1a1ae07cc479f3af1b84d5f77f00685725b25035741583546a",
    "p0_primdec.out": "ecf2189c15a2ad2fe931a055bd3718c0eddc5e5da2044d70e0e49c3ea3b09021",
    "p0_dims.out": "d8dcbe8c95602644807441182070505b7b732c15adf6807688eb315e94190e41",
}
RESULT_SHA256 = "6ce7d394989dedcffe303ff8aaf4fb3cb89e750cbf57ad6c15eb9231e11f399e"
PURE_POWER_LMS = {
    "p": 5,
    "x0": 5,
    "x1": 5,
    "x2": 5,
    "x3": 5,
    "x4": 5,
    "x5": 5,
    "q": 6,
    "ip": 6,
}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def exponent_vector(term: str) -> tuple[int, ...]:
    """Return the exponent vector of one integer-coefficient monomial term."""
    unsigned = term.lstrip("+-")
    factors = unsigned.split("*")
    exponents = dict.fromkeys(VARIABLES, 0)
    for factor in factors:
        if not factor or factor.isdigit():
            continue
        match = re.fullmatch(r"(p|x[0-5]|q|ip)(?:\^(\d+))?", factor)
        if match is None:
            raise AssertionError(f"unparsed factor {factor!r} in {term!r}")
        name, power = match.groups()
        exponents[name] += int(power or 1)
    return tuple(exponents[name] for name in VARIABLES)


def grevlex_key(exponents: tuple[int, ...]) -> tuple[int, ...]:
    # In the declared variable order, larger total degree wins; at the last
    # differing exponent, the monomial with the smaller exponent wins.
    return (sum(exponents),) + tuple(-value for value in reversed(exponents))


def terms(polynomial: str) -> list[str]:
    return [term for term in re.findall(r"[+-]?[^+-]+", polynomial) if term]


def monomial_text(exponents: tuple[int, ...]) -> str:
    factors = []
    for name, power in zip(VARIABLES, exponents):
        if power == 1:
            factors.append(name)
        elif power:
            factors.append(f"{name}^{power}")
    return "*".join(factors) or "1"


def main() -> None:
    for name, expected in EXPECTED.items():
        actual = digest((HERE / name).read_bytes())
        assert actual == expected, (name, actual, expected)

    input_text = (HERE / "input.ms").read_text()
    input_lines = input_text.splitlines()
    assert input_lines[0] == ", ".join(VARIABLES)
    assert input_lines[1] == "0"
    assert input_text.rstrip().endswith("p*ip-1")
    assert input_text.count(",\n") == 8
    assert digest(GENERATOR.read_bytes()) == "5c1c6e6d6570d58f9c9f6104be151e6da68c90d0e2855af9021f533b92420b01"
    assert digest(PARENT.read_bytes()) == "a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf"
    regenerated = subprocess.run(
        [sys.executable, str(GENERATOR), "--characteristic", "0", "--mode", "saturated", "--order", "p-first"],
        check=True,
        capture_output=True,
    ).stdout
    assert regenerated == (HERE / "input.ms").read_bytes()

    metadata = (HERE / "metadata.txt").read_text()
    assert "characteristic=0" in metadata
    assert "msolve=0.10.1" in metadata
    assert "exit_code=0" in metadata
    assert "final_status=DONE" in metadata
    assert f"result_sha256={RESULT_SHA256}" in metadata

    stderr = (HERE / "stderr.log").read_text()
    for needle in (
        "#variables                       9",
        "#equations                       9",
        "#invalid equations               0",
        "field characteristic             0",
        "homogeneous input?               0",
        "monomial order                 DRL",
        "size of basis                  1246",
        "#polynomials to lift           1246",
        "Max coeff. bitsize             1368",
        "#primes                         126",
        "#bad primes                       0",
    ):
        assert needle in stderr, needle

    result_bytes = gzip.decompress((HERE / "result.out.gz").read_bytes())
    assert digest(result_bytes) == RESULT_SHA256
    result = result_bytes.decode()
    assert "#field characteristic: 0" in result
    assert "#variable order:       " + ", ".join(VARIABLES) in result
    assert "#monomial order:       graded reverse lexicographical" in result
    assert "#length of basis:      1246 elements" in result

    body = result.split("#---\n[", 1)[1]
    assert body.endswith("]:\n")
    polynomials = body[:-3].split(", \n")
    assert len(polynomials) == 1246, len(polynomials)

    leading_monomials = []
    for index, polynomial in enumerate(polynomials, start=1):
        polynomial_terms = terms(polynomial)
        vectors = [exponent_vector(term) for term in polynomial_terms]
        computed = max(vectors, key=grevlex_key)
        printed_first = vectors[0]
        assert printed_first == computed, (index, printed_first, computed)
        leading_monomials.append(computed)

    pure_powers: dict[str, int] = {}
    for exponents in leading_monomials:
        support = [i for i, value in enumerate(exponents) if value]
        if len(support) == 1:
            i = support[0]
            name = VARIABLES[i]
            pure_powers[name] = min(pure_powers.get(name, 10**9), exponents[i])
    assert pure_powers == PURE_POWER_LMS, pure_powers

    # Enumerate the finite staircase without scanning the full 5^7*6^2 box.
    # Every accepted standard monomial produces at most nine frontier tests.
    zero = (0,) * len(VARIABLES)
    standard = {zero}
    seen = {zero}
    frontier = deque([zero])
    while frontier:
        current = frontier.popleft()
        for variable_index in range(len(VARIABLES)):
            candidate_list = list(current)
            candidate_list[variable_index] += 1
            candidate = tuple(candidate_list)
            if candidate in seen:
                continue
            seen.add(candidate)
            divisible = any(
                all(left >= right for left, right in zip(candidate, generator))
                for generator in leading_monomials
            )
            if not divisible:
                standard.add(candidate)
                frontier.append(candidate)
    assert len(standard) == 1188, len(standard)

    for stem in ("p0_primdec", "p0_dims"):
        replay = subprocess.run(
            ["Singular", "-q", str(HERE / f"{stem}.sing")],
            check=True,
            capture_output=True,
        ).stdout
        assert replay == (HERE / f"{stem}.out").read_bytes(), stem

    print("PASS exact-output validation")
    print(f"result_sha256={RESULT_SHA256}")
    print("basis_length=1246")
    print("pure_power_initial_monomials=" + ",".join(
        f"{name}^{PURE_POWER_LMS[name]}" for name in VARIABLES
    ))
    print("zero_dimensional_initial_ideal=YES")
    print("standard_monomials=1188")
    print("p0_slice=dimension_1_degree_5_two_components_degrees_2_plus_3")


if __name__ == "__main__":
    main()
