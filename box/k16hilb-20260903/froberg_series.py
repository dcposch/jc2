#!/usr/bin/env python3
"""Compute the weighted Froberg positive-truncation candidate for I_(t,+)."""

from __future__ import annotations

import argparse
import json


def multiply(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        if a:
            for j, b in enumerate(right):
                if b:
                    out[i + j] += a * b
    return out


def candidate(t: int, cutoff: int = 512) -> dict[str, object]:
    weights = [1, *range(2, t), t + 1]
    degrees = list(range(2 * t + 2, 4 * t + 1))

    # Coefficients of the rational series through a safe finite cutoff.
    raw = [1] + [0] * cutoff
    for weight in weights:
        for degree in range(weight, cutoff + 1):
            raw[degree] += raw[degree - weight]
    for degree in degrees:
        for index in range(cutoff, degree - 1, -1):
            raw[index] -= raw[index - degree]

    series: list[int] = []
    for coefficient in raw:
        if coefficient <= 0:
            break
        series.append(coefficient)

    denominator = [1]
    for weight in weights:
        factor = [0] * (weight + 1)
        factor[0], factor[-1] = 1, -1
        denominator = multiply(denominator, factor)
    numerator = multiply(series, denominator)
    while numerator and numerator[-1] == 0:
        numerator.pop()

    return {
        "t": t,
        "weights": weights,
        "row_degrees": degrees,
        "series_coefficients": series,
        "series_degree": len(series) - 1,
        "length": sum(series),
        "first_nonpositive_degree": len(series),
        "first_nonpositive_coefficient": raw[len(series)],
        "weighted_denominator": denominator,
        "hilbert_numerator": numerator,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("t", type=int, nargs="+", help="one or more t values")
    args = parser.parse_args()
    print(json.dumps([candidate(t) for t in args.t], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
