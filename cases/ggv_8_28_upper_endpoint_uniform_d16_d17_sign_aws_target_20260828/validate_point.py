#!/usr/bin/env python3
"""Fail-closed exact Q(i) point validator for a frozen branch target."""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
DEFAULT_TARGET = HERE / "sign_branch_elimination_target.json"
EXPECTED_SCHEMA = "jc2.ggv.uniform_d16_d17.sign_lower_aws_target.v1"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def multiply(left, right):
    return (left[0] * right[0] - left[1] * right[1],
            left[0] * right[1] + left[1] * right[0])


def evaluate(equation, point):
    answer = (Q(0), Q(0))
    for term in equation:
        value = tuple(Q(entry) for entry in term["coefficient"])
        for symbol in term["monomial"]:
            value = multiply(value, point[symbol])
        answer = answer[0] + value[0], answer[1] + value[1]
    return answer


def validate(arguments):
    target = json.loads(arguments.target.read_text())
    assert target["schema"] == EXPECTED_SCHEMA
    assert arguments.branch in target["branch_order"]
    branch = target["branches"][arguments.branch]
    if arguments.use_frozen_seed:
        assert arguments.point is None
        encoded = branch.get("exact_seed_point")
        assert encoded is not None, "this branch has no frozen seed"
        provenance = "frozen_target_seed"
    else:
        assert arguments.point is not None
        candidate = json.loads(arguments.point.read_text())
        assert candidate["schema"] == "jc2.ggv.uniform_sign_lower.point.v1"
        assert candidate["target_sha256"] == digest(arguments.target)
        assert candidate["branch"] == arguments.branch
        encoded = candidate["point"]
        provenance = str(arguments.point)
    assert set(encoded) == set(branch["variables"]), (
        sorted(set(branch["variables"]) - set(encoded)),
        sorted(set(encoded) - set(branch["variables"])))
    point = {}
    for variable, value in encoded.items():
        assert isinstance(value, list) and len(value) == 2
        point[variable] = Q(value[0]), Q(value[1])
    residuals = {
        label: evaluate(branch["equations"][label], point)
        for label in branch["equation_order"]
    }
    assert all(value == (Q(0), Q(0)) for value in residuals.values()), residuals
    return {
        "status": "POINT_CHECK=PASS",
        "target_sha256": digest(arguments.target),
        "branch": arguments.branch,
        "field": "Q(i)",
        "variable_count": len(point),
        "equation_count": len(residuals),
        "provenance": provenance,
        "scope": "consistency of this necessary lower subsystem only",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", type=Path, default=DEFAULT_TARGET)
    parser.add_argument("--branch", required=True)
    parser.add_argument("--point", type=Path)
    parser.add_argument("--use-frozen-seed", action="store_true")
    arguments = parser.parse_args()
    print(json.dumps(validate(arguments), sort_keys=True))


if __name__ == "__main__":
    main()
