#!/usr/bin/env python3
"""Exact valuation-stability interface for the frozen B9 SAT cubic."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


EXPECTED_WITNESS_SHA = "a39bc9185a21df92173b356c027a00650ced4b92cfc15d587a91b39c8aca299a"
MODULUS = 3 ** 11


def v3(n: int) -> int:
    if n == 0:
        return 10**9
    n = abs(n)
    out = 0
    while n % 3 == 0:
        n //= 3
        out += 1
    return out


def discriminant(a: int, b: int, c: int) -> int:
    # t^3+a*t^2+b*t+c
    return a*a*b*b - 4*b*b*b - 4*a*a*a*c - 27*c*c + 18*a*b*c


def main():
    repo = Path(__file__).resolve().parents[2]
    witness = repo / "cases/as_b9_9_12_common_cubic_hostile_audit_20260825/evidence/box02/independent_witness.json"
    actual_sha = hashlib.sha256(witness.read_bytes()).hexdigest()
    assert actual_sha == EXPECTED_WITNESS_SHA
    payload = json.loads(witness.read_text())
    coeff = payload["H_coefficients_mod177147"]
    assert coeff[0] == 1 and len(coeff) == 4
    a, b, c = coeff[1], coeff[2], coeff[3]
    assert c == 0
    assert [v3(a), v3(b)] == [4, 5]

    disc = discriminant(a, b, c)
    assert v3(disc) == 15

    # For arbitrary exact lifts a'=a+3^11*A, etc., valuations of the five
    # discriminant summands have the displayed lower bounds.  The unique
    # minimum is -4*b'^3 at 15, hence no cancellation is possible.
    term_valuations = {
        "a2b2": 2*v3(a) + 2*v3(b),
        "minus4b3": 3*v3(b),
        "minus4a3c": 3*v3(a) + 11,
        "minus27c2": 3 + 2*11,
        "plus18abc": 2 + v3(a) + v3(b) + 11,
    }
    assert term_valuations == {
        "a2b2": 18,
        "minus4b3": 15,
        "minus4a3c": 23,
        "minus27c2": 25,
        "plus18abc": 22,
    }
    assert list(term_valuations.values()).count(15) == 1

    # Root-multiplicity controls.
    assert discriminant(0, 0, 0) == 0                 # t^3
    assert discriminant(1, 0, 0) == 0                 # t^2(t+1)

    result = {
        "schema": "b9-sat-cubic-interface-v1",
        "witness_sha256": actual_sha,
        "modulus": MODULUS,
        "H_coefficients": coeff,
        "coefficient_valuations": [0, 4, 5, ">=11"],
        "integer_discriminant": disc,
        "integer_discriminant_v3": v3(disc),
        "all_exact_continuations_discriminant_v3": 15,
        "term_valuation_lower_bounds": term_valuations,
        "forced_char0_root_type_if_exact_continuation": "squarefree_LMN",
        "partial_y_kummer_order_from_fixed_D12": 1,
        "scope": "conditional stratum selection for exact continuations of one finite SAT witness",
        "refuses": [
            "survival beyond 3^11", "inverse limit", "characteristic-zero map",
            "lower-band compatibility", "selected order-three Q8 landing",
            "maximum twelve", "counterexample", "JC2"
        ],
        "PASS": True,
    }
    out = Path(__file__).with_name("sat_interface_result.json")
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()

