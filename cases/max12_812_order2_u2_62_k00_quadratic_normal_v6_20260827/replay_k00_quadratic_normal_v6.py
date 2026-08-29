#!/usr/bin/env python3
"""Replay the quadratic coefficient-normal forms at the K00 core.

This is a desk-scale exact Fraction calculation on the frozen seven ordinary
tails.  It does not compute a saturation or assert existence of a source arc.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TAILS = (
    ROOT
    / "cases/max12_812_order2_u2_62_strict_rees_20260825"
    / "aws_compile_v2_jsat/run/output/compiled_v2/tails.json"
)
TAILS_SHA256 = "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848"

# Monomials use exponent tuples (d0,d1,d2,d3,d4,d5,c), where c=C6.
Monomial = tuple[int, int, int, int, int, int, int]
Polynomial = dict[Monomial, Fraction]
ZERO: Monomial = (0, 0, 0, 0, 0, 0, 0)


def fail(message: object) -> "None":
    raise RuntimeError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def add(*polynomials: Polynomial) -> Polynomial:
    answer: defaultdict[Monomial, Fraction] = defaultdict(Fraction)
    for polynomial in polynomials:
        for monomial, coefficient in polynomial.items():
            answer[monomial] += coefficient
    return {monomial: coefficient for monomial, coefficient in answer.items() if coefficient}


def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    answer: defaultdict[Monomial, Fraction] = defaultdict(Fraction)
    for lm, lc in left.items():
        for rm, rc in right.items():
            answer[tuple(a + b for a, b in zip(lm, rm))] += lc * rc
    return {monomial: coefficient for monomial, coefficient in answer.items() if coefficient}


def power(polynomial: Polynomial, exponent: int) -> Polynomial:
    answer: Polynomial = {ZERO: Fraction(1)}
    for _ in range(exponent):
        answer = multiply(answer, polynomial)
    return answer


def c_shift(polynomial: Polynomial, exponent: int, scalar: Fraction) -> Polynomial:
    return {
        monomial[:6] + (monomial[6] + exponent,): scalar * coefficient
        for monomial, coefficient in polynomial.items()
        if scalar * coefficient
    }


def encode(polynomial: Polynomial) -> list[dict[str, object]]:
    return [
        {
            "exponents_d0_d5_c": list(monomial),
            "coefficient": [coefficient.numerator, coefficient.denominator],
        }
        for monomial, coefficient in sorted(polynomial.items())
    ]


def polynomial_hash(polynomial: Polynomial) -> str:
    payload = json.dumps(encode(polynomial), sort_keys=True, separators=(",", ":"))
    return sha256(payload.encode()).hexdigest()


def main() -> None:
    if digest(TAILS) != TAILS_SHA256:
        fail(("tails hash", digest(TAILS), TAILS_SHA256))
    tails = json.loads(TAILS.read_text())

    # K00-normal coordinates:
    #   C0=(c^4+d0)/256, C1=d1, C2=(c^3+d2)/16, C3=d3,
    #   C4=(3*c^2+d4)/8, C5=d5, C6=c.
    substitutions: list[Polynomial] = [
        {(0, 0, 0, 0, 0, 0, 4): Fraction(1, 256),
         (1, 0, 0, 0, 0, 0, 0): Fraction(1, 256)},
        {(0, 1, 0, 0, 0, 0, 0): Fraction(1)},
        {(0, 0, 0, 0, 0, 0, 3): Fraction(1, 16),
         (0, 0, 1, 0, 0, 0, 0): Fraction(1, 16)},
        {(0, 0, 0, 1, 0, 0, 0): Fraction(1)},
        {(0, 0, 0, 0, 0, 0, 2): Fraction(3, 8),
         (0, 0, 0, 0, 1, 0, 0): Fraction(1, 8)},
        {(0, 0, 0, 0, 0, 1, 0): Fraction(1)},
        {(0, 0, 0, 0, 0, 0, 1): Fraction(1)},
    ]

    quadratic: list[Polynomial] = []
    low_degree_census: dict[str, dict[str, int]] = {}
    for ell in range(1, 8):
        expanded: Polynomial = {}
        for raw_monomial, raw_coefficient in tails[str(ell)]:
            exponents = [int(value) for value in raw_monomial]
            if len(exponents) != 10:
                fail(("tail monomial length", ell, exponents))
            # Lambda=0 kills all three scaled lower loads.  This replay is
            # deliberately only the pure coefficient-normal slice.
            if any(exponents[7:]):
                continue
            term: Polynomial = {ZERO: Fraction(str(raw_coefficient))}
            for index, exponent in enumerate(exponents[:7]):
                if exponent:
                    term = multiply(term, power(substitutions[index], exponent))
            expanded = add(expanded, term)
        degree_counts: defaultdict[int, int] = defaultdict(int)
        for monomial in expanded:
            degree_counts[sum(monomial[:6])] += 1
        if degree_counts.get(0, 0) or degree_counts.get(1, 0):
            fail(("constant/linear K00 normal term", ell, dict(degree_counts)))
        q = {
            monomial: coefficient
            for monomial, coefficient in expanded.items()
            if sum(monomial[:6]) == 2
        }
        quadratic.append(q)
        low_degree_census[str(ell)] = {
            "constant": degree_counts.get(0, 0),
            "linear": degree_counts.get(1, 0),
            "quadratic": len(q),
        }

    expected_counts = [8, 11, 9, 12, 8, 0, 6]
    if [len(polynomial) for polynomial in quadratic] != expected_counts:
        fail(("quadratic term census", [len(polynomial) for polynomial in quadratic]))

    # Exact identities over Q[c,d0,...,d5].
    residual5 = add(
        quadratic[4],
        c_shift(quadratic[0], 2, Fraction(3, 128)),
        c_shift(quadratic[2], 1, Fraction(1, 8)),
    )
    residual6 = quadratic[5]
    residual7 = add(
        quadratic[6],
        c_shift(quadratic[0], 3, Fraction(1, 512)),
        c_shift(quadratic[2], 2, Fraction(1, 128)),
    )
    if residual5 or residual6 or residual7:
        fail(("quadratic relation residual", residual5, residual6, residual7))

    result = {
        "status": "PASS-K00-PURE-COEFFICIENT-QUADRATIC-NORMAL-V6",
        "tails_sha256": TAILS_SHA256,
        "coordinates": {
            "c": "C6",
            "d0": "256*C0-C6^4",
            "d1": "C1",
            "d2": "16*C2-C6^3",
            "d3": "C3",
            "d4": "8*C4-3*C6^2",
            "d5": "C5",
        },
        "low_degree_census": low_degree_census,
        "quadratic_sha256": {
            str(index + 1): polynomial_hash(polynomial)
            for index, polynomial in enumerate(quadratic)
        },
        "relations": [
            "Q5=-(3*C6^2/128)*Q1-(C6/8)*Q3",
            "Q6=0",
            "Q7=-(C6^3/512)*Q1-(C6^2/128)*Q3",
        ],
        "scope": (
            "pure coefficient-normal quadratic slice at Lambda=k6=k2=0; "
            "no saturation, arc, receiver, Gate-T, or JC2 conclusion"
        ),
    }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
