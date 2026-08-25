#!/usr/bin/env python3
"""Reconstruct 190 scalar coefficient fractions for one Q8 coordinate."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
from pathlib import Path


P = 127
NAMES = ("c", "d2", "d4", "x1", "x3", "x5", "inv")
HERMITE_SHA256 = "f97ad9090e6f53fa510a6672353f9260a3a3ee8c1a12fd841b4bf97e70b00e63"
HIGH_SHA256 = "ed10f985d3031b1b67f2e81c028ab6bf961d26fa24fa62b312bcbb61a882a19b"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_module(name: str, path: Path, expected: str):
    got = digest(path)
    if got != expected:
        raise RuntimeError((name, got, expected, str(path)))
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(("cannot import", name, str(path)))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def polynomial_from_table(table, denominator, modulus_degree):
    coefficients = []
    for degree in range(modulus_degree):
        coefficients.append(
            sum(
                denominator[power] * table[power][degree]
                for power in range(len(denominator))
            )
            % P
        )
    while coefficients and coefficients[-1] == 0:
        coefficients.pop()
    return coefficients


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--coordinate", choices=NAMES, required=True)
    parser.add_argument("--hermite-source", type=Path, required=True)
    parser.add_argument("--high-source", type=Path, required=True)
    parser.add_argument("--shape", type=Path, required=True)
    parser.add_argument("--parent", type=Path, required=True)
    parser.add_argument("--poly-helper", type=Path, required=True)
    parser.add_argument("--lower", type=Path, required=True)
    parser.add_argument("--lower-order", type=int, required=True)
    parser.add_argument("--upper", type=Path, required=True)
    parser.add_argument("--upper-order", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not (2 <= args.lower_order < args.upper_order):
        raise RuntimeError((args.lower_order, args.upper_order))

    hermite = load_module("q8_hermite_parent", args.hermite_source, HERMITE_SHA256)
    high = load_module("q8_high_parent", args.high_source, HIGH_SHA256)
    parent = hermite.load_module("q8_pade_parent", args.parent, hermite.PARENT_SHA256)
    helper = hermite.load_module("q8_poly_helper", args.poly_helper, hermite.HELPER_SHA256)
    if digest(args.shape) != hermite.SHAPE_SHA256:
        raise RuntimeError("shape hash")
    shape = json.loads(args.shape.read_text())
    lower_series = parent.read_series(args.lower, args.lower_order)
    upper_series = parent.read_series(args.upper, args.upper_order)
    if not parent.prefix_equal(parent.flatten(lower_series), parent.flatten(upper_series)):
        raise RuntimeError("jet prefix mismatch")
    lower = hermite.build_hermite(shape, lower_series, args.lower_order, helper)
    upper = hermite.build_hermite(shape, upper_series, args.upper_order, helper)
    lower_tables = [
        helper.shifted_remainders(polynomial, lower["modulus"])
        for polynomial in lower["interpolants"][args.coordinate]
    ]
    upper_tables = [
        helper.shifted_remainders(polynomial, upper["modulus"])
        for polynomial in upper["interpolants"][args.coordinate]
    ]

    coefficients = []
    lcm = [1]
    strict_count = 0
    upper_only_count = 0
    no_fit = []
    for v_degree, (lower_table, upper_table) in enumerate(
        zip(lower_tables, upper_tables, strict=True)
    ):
        lower_fit = hermite.search_unique(
            [lower_table],
            lower["shifted_points"],
            lower["modulus_degree"],
            helper,
        )
        lower_holdout = False
        if hermite.is_fit(lower_fit):
            lower_holdout = hermite.validate_tables(
                [upper_table],
                lower_fit["denominator"],
                lower_fit["numerator_degree"],
                upper["modulus_degree"],
            )
        upper_fit = hermite.search_unique(
            [upper_table],
            upper["shifted_points"],
            upper["modulus_degree"],
            helper,
        )
        selected = None
        source = None
        if hermite.is_fit(lower_fit) and lower_holdout:
            selected = lower_fit
            source = "lower_fit_with_upper_holdout"
            strict_count += 1
        elif hermite.is_fit(upper_fit):
            selected = upper_fit
            source = "upper_fit_unvalidated_beyond_upper"
            upper_only_count += 1
        else:
            no_fit.append(v_degree)
        item = {
            "v_degree": v_degree,
            "lower_fit": lower_fit,
            "lower_fit_valid_through_upper": lower_holdout,
            "upper_fit": upper_fit,
            "selected_source": source,
            "selected": selected,
        }
        if selected is not None:
            numerator = polynomial_from_table(
                upper_table, selected["denominator"], upper["modulus_degree"]
            )
            if len(numerator) - 1 > selected["numerator_degree"]:
                raise AssertionError((v_degree, len(numerator) - 1, selected))
            item["selected_numerator"] = numerator
            lcm = high.lcm_poly(lcm, selected["denominator"], P)
        coefficients.append(item)

    lcm = high.normalize_constant(lcm, P)
    payload = {
        "status": "PASS",
        "scope": (
            "individual scalar Hermite-Pade reconstructions and their exact LCM; "
            "full mod-H substitution and a strict later-order holdout remain mandatory"
        ),
        "prime": P,
        "coordinate": args.coordinate,
        "shape_sha256": digest(args.shape),
        "hermite_source_sha256": digest(args.hermite_source),
        "high_source_sha256": digest(args.high_source),
        "lower_order": args.lower_order,
        "lower_sha256": digest(args.lower),
        "upper_order": args.upper_order,
        "upper_sha256": digest(args.upper),
        "coefficient_count": 190,
        "strict_holdout_count": strict_count,
        "upper_only_count": upper_only_count,
        "no_fit_v_degrees": no_fit,
        "all_coefficients_selected": not no_fit,
        "all_coefficients_strict_holdout": strict_count == 190,
        "coordinate_denominator_lcm": lcm,
        "coordinate_denominator_lcm_degree": len(lcm) - 1,
        "coefficients": coefficients,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print("Q8-P127-INDIVIDUAL-HERMITE-RECONSTRUCTION")
    print("status=PASS")
    print("coordinate=" + args.coordinate)
    print(f"orders={args.lower_order},{args.upper_order}")
    print("coefficient_count=190")
    print("strict_holdout_count=" + str(strict_count))
    print("upper_only_count=" + str(upper_only_count))
    print("no_fit_count=" + str(len(no_fit)))
    print("lcm_degree=" + str(len(lcm) - 1))
    print("output_sha256=" + digest(args.output))


if __name__ == "__main__":
    main()

