#!/usr/bin/env python3
"""Decode Singular hilb(I,1,w) output into a terminating weighted series."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def multiply(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] += a * b
    return answer


def divide_exact(numerator: list[int], denominator: list[int]) -> tuple[list[int], list[int]]:
    # denominator[0] is one, so power-series division is integral degree by degree.
    quotient: list[int] = []
    remainder = numerator[:]
    for degree in range(len(numerator)):
        value = remainder[degree]
        quotient.append(value)
        if value:
            for offset, coeff in enumerate(denominator):
                if degree + offset >= len(remainder):
                    remainder.extend([0] * (degree + offset + 1 - len(remainder)))
                remainder[degree + offset] -= value * coeff
    while quotient and quotient[-1] == 0:
        quotient.pop()
    while remainder and remainder[-1] == 0:
        remainder.pop()
    return quotient, remainder


def runs(coefficients: list[int]) -> list[list[int]]:
    if not coefficients:
        return []
    result: list[list[int]] = []
    start = 0
    value = coefficients[0]
    for index, item in enumerate(coefficients[1:], start=1):
        if item != value:
            result.append([start, index - 1, value])
            start = index
            value = item
    result.append([start, len(coefficients) - 1, value])
    return result


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("t", type=int)
    ap.add_argument("output", type=Path)
    args = ap.parse_args()
    text = args.output.read_text(encoding="utf-8")
    lines = text.splitlines()
    marker_candidates = [
        i for i, line in enumerate(lines)
        if line.strip() in {"HNUM", "LEGACY_HNUM", "FULL_HNUM"}
        or line.strip().endswith("HILB_NUMERATOR_BEGIN")
    ]
    if not marker_candidates:
        raise SystemExit("Hilbert numerator marker missing")
    raw = ""
    for candidate in lines[marker_candidates[-1] + 1:]:
        if re.fullmatch(r"-?\d+(?:,-?\d+)*", candidate.strip()):
            raw = candidate.strip()
            break
    if not raw:
        raise SystemExit("Hilbert numerator vector missing after marker")
    numerator = [int(item) for item in raw.split(",")]
    while numerator and numerator[-1] == 0:
        numerator.pop()
    weights = [1] + list(range(2, args.t)) + [args.t + 1]
    denominator = [1]
    for weight in weights:
        factor = [0] * (weight + 1)
        factor[0], factor[-1] = 1, -1
        denominator = multiply(denominator, factor)
    series, remainder = divide_exact(numerator, denominator)
    length_match = re.search(r"(?:(?:FULL|LEGACY)_VDIM|FULL_LENGTH)=(-?\d+)", text)
    payload = {
        "t": args.t,
        "weights": weights,
        "numerator": numerator,
        "denominator": denominator,
        "series_coefficients": series,
        "series_runs": runs(series),
        "socle_degree": len(series) - 1,
        "coefficient_sum": sum(series),
        "reported_vdim": int(length_match.group(1)) if length_match else None,
        "division_remainder": remainder,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
