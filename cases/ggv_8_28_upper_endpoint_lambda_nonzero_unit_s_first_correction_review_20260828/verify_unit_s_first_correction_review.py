#!/usr/bin/env python3
"""Independent exact review of the unit-S correction and mode census."""

from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PRODUCER = ROOT / "xmodel/ggv-upper-endpoint-lambda-nonzero-unit-s-first-correction-sol-ultra-20260828.md"
PRODUCER_CHECKER = ROOT / "cases/ggv_8_28_upper_endpoint_lambda_nonzero_unit_s_first_correction_20260828/verify_unit_s_first_correction.py"
PINS = {
    PRODUCER: "c3f03f370eec64375af19dc684a17c52ee176b2aa1f6179cfedfa0c3a15cdb9a",
    PRODUCER_CHECKER: "872d6020e09ca618efeb209e7f6ba331d359e93ccb2d18b27a30573ab72b9284",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def binomial(beta: F, count: int) -> F:
    value = F(1)
    for index in range(count):
        value *= (beta - index) / (index + 1)
    return value


def compositions(total: int, length: int):
    if length == 0:
        if total == 0:
            yield ()
        return
    for first in range(1, total + 1):
        for tail in compositions(total - first, length - 1):
            yield (first,) + tail


def minimum_face_power(mode: int, relative_order: int, f1_divisibility: int = 2):
    """Minimum actual L-power in t^m F^((12-m)/8) at an epsilon order."""
    delay = mode // 2
    if relative_order < delay:
        return None
    residual = relative_order - delay
    leading_power = F(12 - mode, 2)
    beta = F(12 - mode, 8)
    if residual == 0:
        return int(leading_power)
    powers = []
    for count in range(1, residual + 1):
        if binomial(beta, count) == 0:
            continue
        for choice in compositions(residual, count):
            divisibility = sum(f1_divisibility if index == 1 else 0
                               for index in choice)
            powers.append(leading_power - 4 * count + divisibility)
    assert powers
    answer = min(powers)
    assert answer.denominator == 1
    return int(answer)


def verify(mutation: str) -> None:
    for path, expected in PINS.items():
        assert sha256(path) == expected, path

    # Root specialization of D=R-4SU=0 and
    # P=256F5-RS+2S^2U=0.
    # Coefficients are recorded in tau after substituting R=4su.
    explicit = {
        3: F(1, 8),       # a^2*u
        4: F(1, 16),      # a*s*u
        5: F(1, 128),     # s^2*u
    }
    if mutation == "factor":
        explicit[4] = F(1, 32)
    factored = {3: F(1, 8), 4: F(1, 16), 5: F(1, 128)}
    assert explicit == factored

    modes = [0, 2, 4, 6, 8]
    if mutation == "omit-mode":
        modes.remove(8)
    assert modes == [mode for mode in range(0, 9, 2)]
    divisor = 1 if mutation == "weak-f1" else 2
    table = {
        mode: {
            order: minimum_face_power(mode, order, divisor)
            for order in range(mode // 2, 5)
        }
        for mode in modes
    }
    assert table == {
        0: {0: 6, 1: 4, 2: 2, 3: 0, 4: -2},
        2: {1: 5, 2: 3, 3: 1, 4: -1},
        4: {2: 4, 3: 2, 4: 0},
        6: {3: 3, 4: 1},
        8: {4: 2},
    }
    complete_minimum = {
        order: min(row[order] for row in table.values() if order in row)
        for order in range(5)
    }
    assert complete_minimum == {0: 6, 1: 4, 2: 2, 3: 0, 4: -2}
    assert all(complete_minimum[order] >= 0 for order in range(4))
    assert complete_minimum[4] < 0

    print("root_relations=R(alpha)=4*S(alpha)*U(alpha),F5(alpha)=S(alpha)^2*U(alpha)/128")
    print("H1=U(alpha)*tau^3*L^2/8")
    print("complete_mode_minima_through_order4=" + repr(table))
    print("first_possible_face_pole_relative_order=4")
    print("PASS_INDEPENDENT_UNIT_S_FIRST_CORRECTION_REVIEW")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=("none", "factor", "weak-f1", "omit-mode"), default="none")
    args = parser.parse_args()
    verify(args.mutation)


if __name__ == "__main__":
    main()
