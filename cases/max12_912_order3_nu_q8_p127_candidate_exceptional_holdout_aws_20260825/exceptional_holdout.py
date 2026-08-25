#!/usr/bin/env python3
"""Compare the Q8 p127 candidate H with the three excluded fibres."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
RECONSTRUCT = ROOT / (
    "cases/max12_912_order3_nu_q8_p127_eliminant_interpolation_aws_20260825/"
    "reconstruct.py"
)
RECONSTRUCT_SHA256 = "50dfbd89893baf6025a0c7ae9d90772bfbd9b0957f57397630f3f059a3bbc2c8"
CANDIDATE = ROOT / (
    "cases/max12_912_order3_nu_q8_p127_eliminant_interpolation_aws_20260825/"
    "aws/p127-eliminant-interpolation-root-v6/result.json"
)
CANDIDATE_SHA256 = "9061726295086f58f74f3751b2f7c2d59c5cb86de5e53ecd636687fd54daa7ce"
P = 127


def load_reconstruct():
    for path, expected in (
        (RECONSTRUCT, RECONSTRUCT_SHA256),
        (CANDIDATE, CANDIDATE_SHA256),
    ):
        got = sha256(path.read_bytes()).hexdigest()
        if got != expected:
            raise RuntimeError((str(path), got, expected))
    spec = importlib.util.spec_from_file_location("q8_exceptional_reconstruct", RECONSTRUCT)
    if spec is None or spec.loader is None:
        raise RuntimeError(RECONSTRUCT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] % P == 0:
        poly.pop()
    return [coefficient % P for coefficient in poly]


def divide(dividend: list[int], divisor: list[int]) -> tuple[list[int], list[int]]:
    dividend = trim(dividend[:])
    divisor = trim(divisor[:])
    assert divisor != [0]
    quotient = [0] * max(1, len(dividend) - len(divisor) + 1)
    inverse = pow(divisor[-1], -1, P)
    while dividend != [0] and len(dividend) >= len(divisor):
        shift = len(dividend) - len(divisor)
        coefficient = dividend[-1] * inverse % P
        quotient[shift] = coefficient
        for index, value in enumerate(divisor):
            dividend[index + shift] = (dividend[index + shift] - coefficient * value) % P
        dividend = trim(dividend)
    return trim(quotient), dividend


def gcd_monic(left: list[int], right: list[int]) -> list[int]:
    left, right = trim(left[:]), trim(right[:])
    while right != [0]:
        _, remainder = divide(left, right)
        left, right = right, remainder
    inverse = pow(left[-1], -1, P)
    return [(coefficient * inverse) % P for coefficient in left]


def derivative(poly: list[int]) -> list[int]:
    return trim([(degree * coefficient) % P for degree, coefficient in enumerate(poly)][1:] or [0])


def evaluate(poly: list[int], value: int) -> int:
    answer = 0
    for coefficient in reversed(poly):
        answer = (answer * value + coefficient) % P
    return answer


def candidate_at(payload: dict, w_value: int) -> list[int]:
    coefficients = []
    for v_degree in range(191):
        value = sum(
            coefficient * pow(w_value, w_degree, P)
            for w_degree, coefficient in payload["nonzero_support"][str(v_degree)]
        ) % P
        coefficients.append(value)
    assert coefficients[-1] == 1
    return trim(coefficients)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("roots", type=Path, nargs="+")
    args = parser.parse_args()
    roots = [path.resolve() for path in args.roots]
    reconstruct = load_reconstruct()
    payload = json.loads(CANDIDATE.read_text())
    assert payload["status"] == "PASS"
    assert payload["degree_drop_values"] == [39, 56, 125]
    maximum_w_degree = max(
        w_degree
        for entries in payload["nonzero_support"].values()
        for w_degree, _ in entries
    )
    assert maximum_w_degree == 21

    comparisons = {}
    for w_value in payload["degree_drop_values"]:
        lane = reconstruct.lane_for(roots, w_value)
        fibre, partition = reconstruct.fibre_polynomial(lane, w_value)
        candidate = candidate_at(payload, w_value)
        quotient, remainder = divide(candidate, fibre)
        common = gcd_monic(candidate, fibre)
        repeated = gcd_monic(candidate, derivative(candidate))
        linear_root = None
        root_in_fibre = None
        if remainder == [0] and len(quotient) == 2 and quotient[-1] == 1:
            linear_root = (-quotient[0]) % P
            root_in_fibre = evaluate(fibre, linear_root) == 0
        result_text = (lane / "result.out").read_text()
        comparisons[str(w_value)] = {
            "lane": str(lane),
            "fibre_vdim": int(reconstruct.scalar(result_text, "fibre_vdim")),
            "fibre_eliminant_degree": len(fibre) - 1,
            "fibre_partition": partition,
            "candidate_degree": len(candidate) - 1,
            "fibre_divides_candidate": remainder == [0],
            "quotient": quotient,
            "remainder": remainder,
            "candidate_fibre_gcd_degree": len(common) - 1,
            "candidate_squarefree_gcd_degree": len(repeated) - 1,
            "linear_quotient_root": linear_root,
            "linear_quotient_root_in_fibre": root_in_fibre,
        }

    output = {
        "status": "PASS",
        "scope": "exact exceptional-value holdout comparison only",
        "prime": P,
        "candidate_sha256": CANDIDATE_SHA256,
        "candidate_v_degree": 190,
        "candidate_coefficient_w_degree": maximum_w_degree,
        "comparisons": comparisons,
        "disclosure": "holdout agreement does not prove generic ideal membership, flatness, or characteristic-zero lifting",
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

