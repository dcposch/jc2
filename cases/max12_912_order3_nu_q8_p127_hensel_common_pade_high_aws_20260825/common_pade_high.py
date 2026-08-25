#!/usr/bin/env python3
"""Run the exact common-denominator gate on two arbitrary Hensel orders."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
from pathlib import Path


GROUPS = (
    *((name, (name,)) for name in ("c", "d2", "d4", "x1", "x3", "x5", "inv")),
    ("normal_triple", ("c", "d2", "d4")),
    ("invariant_triple", ("x1", "x3", "x5")),
    ("true_center_six", ("c", "d2", "d4", "x1", "x3", "x5")),
    ("global_seven", ("c", "d2", "d4", "x1", "x3", "x5", "inv")),
)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_parent(path: Path):
    spec = importlib.util.spec_from_file_location("q8_common_pade_parent", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(("cannot import parent", str(path)))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def flatten_names(data, names: tuple[str, ...]) -> list[list[int]]:
    return [sequence for name in names for sequence in data[name]]


def coordinate_numerators(base, data, names, denominator, numerator_degree):
    output = {}
    for name in names:
        rows = []
        for sequence in data[name]:
            coefficients = []
            for n in range(numerator_degree + 1):
                value = sum(
                    denominator[j] * sequence[n - j]
                    for j in range(min(n, len(denominator) - 1) + 1)
                )
                coefficients.append(value % base.P)
            rows.append(coefficients)
        output[name] = rows
    return output


def analyze_group(base, lower_data, upper_data, names, lower_order, upper_order):
    lower = flatten_names(lower_data, names)
    upper = flatten_names(upper_data, names)
    if not base.prefix_equal(lower, upper):
        raise AssertionError(("group prefix", names))
    lower_fit = base.find_minimal(lower, lower_order)
    holdout = []
    if lower_fit is not None:
        for hit in lower_fit["hits"]:
            holdout.append(
                {
                    **hit,
                    "valid_through_upper": base.validate(
                        upper, upper_order, hit["denominator"], hit["numerator_degree"]
                    ),
                }
            )
    upper_fit = base.find_minimal(upper, upper_order)
    selected = None
    source = None
    passing = [hit for hit in holdout if hit["valid_through_upper"]]
    if passing:
        selected = passing[0]
        source = "lower_fit_with_upper_holdout"
    elif upper_fit is not None:
        selected = upper_fit["hits"][0]
        source = "upper_fit_unvalidated_beyond_upper"
    result = {
        "coordinates": list(names),
        "sequence_count": len(upper),
        "lower_fit": lower_fit,
        "lower_upper_holdout": holdout,
        "upper_fit": upper_fit,
        "selected_source": source,
        "selected": selected,
    }
    return result


def trim(poly: list[int], prime: int) -> list[int]:
    result = [value % prime for value in poly]
    while result and result[-1] == 0:
        result.pop()
    return result


def multiply(a: list[int], b: list[int], prime: int) -> list[int]:
    output = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            output[i + j] = (output[i + j] + x * y) % prime
    return trim(output, prime)


def divide(a: list[int], b: list[int], prime: int) -> tuple[list[int], list[int]]:
    remainder = trim(a, prime)
    divisor = trim(b, prime)
    if not divisor:
        raise ZeroDivisionError
    quotient = [0] * max(0, len(remainder) - len(divisor) + 1)
    inverse = pow(divisor[-1], prime - 2, prime)
    while len(remainder) >= len(divisor):
        shift = len(remainder) - len(divisor)
        scalar = remainder[-1] * inverse % prime
        quotient[shift] = scalar
        for index, coefficient in enumerate(divisor):
            remainder[shift + index] = (
                remainder[shift + index] - scalar * coefficient
            ) % prime
        remainder = trim(remainder, prime)
    return trim(quotient, prime), remainder


def monic(poly: list[int], prime: int) -> list[int]:
    poly = trim(poly, prime)
    inverse = pow(poly[-1], prime - 2, prime)
    return [(inverse * value) % prime for value in poly]


def gcd_poly(a: list[int], b: list[int], prime: int) -> list[int]:
    a, b = trim(a, prime), trim(b, prime)
    while b:
        _, remainder = divide(a, b, prime)
        a, b = b, remainder
    return monic(a, prime)


def lcm_poly(a: list[int], b: list[int], prime: int) -> list[int]:
    common = gcd_poly(a, b, prime)
    quotient, remainder = divide(a, common, prime)
    if remainder:
        raise AssertionError("nonexact lcm division")
    return monic(multiply(quotient, b, prime), prime)


def normalize_constant(poly: list[int], prime: int) -> list[int]:
    if not poly or poly[0] == 0:
        raise AssertionError(("denominator not regular at base", poly[:3]))
    inverse = pow(poly[0], prime - 2, prime)
    return [(inverse * value) % prime for value in poly]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--parent", type=Path, required=True)
    parser.add_argument("--lower", type=Path, required=True)
    parser.add_argument("--lower-order", type=int, required=True)
    parser.add_argument("--upper", type=Path, required=True)
    parser.add_argument("--upper-order", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not (2 <= args.lower_order < args.upper_order):
        raise ValueError((args.lower_order, args.upper_order))

    base = load_parent(args.parent)
    base.synthetic_controls()
    lower_data = base.read_series(args.lower, args.lower_order)
    upper_data = base.read_series(args.upper, args.upper_order)
    lower_global = base.flatten(lower_data)
    upper_global = base.flatten(upper_data)
    if len(lower_global) != 7 * 190 or len(upper_global) != 7 * 190:
        raise AssertionError((len(lower_global), len(upper_global)))
    if not base.prefix_equal(lower_global, upper_global):
        raise AssertionError("lower/upper prefix mismatch")
    corrupted = [row[:] for row in lower_global]
    corrupted[-1][-1] = (corrupted[-1][-1] + 1) % base.P
    if base.prefix_equal(corrupted, upper_global):
        raise AssertionError("prefix negative control not detected")

    analyses = {}
    for label, names in GROUPS:
        analyses[label] = analyze_group(
            base,
            lower_data,
            upper_data,
            names,
            args.lower_order,
            args.upper_order,
        )

    coordinate_labels = ("c", "d2", "d4", "x1", "x3", "x5", "inv")
    lcm_candidate = None
    if all(analyses[name]["selected"] is not None for name in coordinate_labels):
        denominator = [1]
        for name in coordinate_labels:
            denominator = lcm_poly(
                denominator,
                analyses[name]["selected"]["denominator"],
                base.P,
            )
        denominator = normalize_constant(denominator, base.P)
        numerator_bounds = {}
        exact_upper_validation = True
        for name in coordinate_labels:
            selected = analyses[name]["selected"]
            quotient, remainder = divide(
                denominator, selected["denominator"], base.P
            )
            if remainder:
                raise AssertionError(("LCM division", name, remainder))
            bound = selected["numerator_degree"] + len(quotient) - 1
            numerator_bounds[name] = bound
            exact_upper_validation = exact_upper_validation and base.validate(
                upper_data[name], args.upper_order, denominator, bound
            )
        if not exact_upper_validation:
            raise AssertionError("LCM candidate failed exact upper validation")
        lcm_candidate = {
            "denominator": denominator,
            "denominator_degree": len(denominator) - 1,
            "coordinate_numerator_bounds": numerator_bounds,
            "valid_through_upper": True,
            "strict_lower_to_upper_holdout": all(
                analyses[name]["selected_source"] == "lower_fit_with_upper_holdout"
                for name in coordinate_labels
            ),
            "scope": (
                "exact LCM of the seven selected coordinate denominators; "
                "not accepted without a strict later-order holdout and full mod-H substitution"
            ),
        }

    payload: dict[str, object] = {
        "status": "PASS",
        "scope": (
            "simultaneous scalar-denominator recurrence; provisional until "
            "strict higher-order holdout and exact full mod-H substitution"
        ),
        "prime": base.P,
        "sequence_count": len(upper_global),
        "parent_sha256": digest(args.parent),
        "lower_order": args.lower_order,
        "lower_sha256": digest(args.lower),
        "upper_order": args.upper_order,
        "upper_sha256": digest(args.upper),
        "prefix_match": True,
        "synthetic_positive": True,
        "synthetic_negative": True,
        "group_hierarchy": analyses,
        "coordinate_lcm_candidate": lcm_candidate,
        "admissible_upper_denominator_degree": [1, args.upper_order - 1],
        "admissible_upper_numerator_degree": [0, args.upper_order - 2],
        "search_policy": (
            "increasing total degree; stop at first total carrying a unique "
            "full-rank denominator; exhaust full rectangle only if no hit"
        ),
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")

    print("Q8-P127-HENSEL-SIMULTANEOUS-COMMON-PADE-HIGH")
    print("status=PASS")
    print(f"orders={args.lower_order},{args.upper_order}")
    print(f"sequence_count={len(upper_global)}")
    print("prefix_match=1")
    for label, _ in GROUPS:
        item = analyses[label]
        lower_total = (
            None if item["lower_fit"] is None else item["lower_fit"]["total_degree"]
        )
        upper_total = (
            None if item["upper_fit"] is None else item["upper_fit"]["total_degree"]
        )
        selected = item["selected"]
        summary = (
            "NONE"
            if selected is None
            else (
                f"{item['selected_source']}:d={selected['denominator_degree']},"
                f"m={selected['numerator_degree']}"
            )
        )
        print(
            f"group={label} lower_total={lower_total} upper_total={upper_total} "
            f"selected={summary}"
        )
    if lcm_candidate is None:
        print("coordinate_lcm=NONE")
    else:
        print(
            "coordinate_lcm=d="
            + str(lcm_candidate["denominator_degree"])
            + " strict_holdout="
            + str(int(lcm_candidate["strict_lower_to_upper_holdout"]))
        )
    print("output_sha256=" + digest(args.output))


if __name__ == "__main__":
    main()
