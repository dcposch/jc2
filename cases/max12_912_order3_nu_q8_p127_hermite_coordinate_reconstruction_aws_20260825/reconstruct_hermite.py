#!/usr/bin/env python3
"""Exact Hermite-Padé reconstruction over F_127 from fibres plus one jet."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
from pathlib import Path


P = 127
BASE_W = 25
SHAPE_SHA256 = "0790e9f8bb6b545e742ca9e723c29b9a8dc0268a93dedd91c2f2a7b48f48f231"
PARENT_SHA256 = "acc005c798d966297bb3b1a5a9fa64f3e83d71a164f6c2b4d7806473f841e3b5"
HELPER_SHA256 = "967203305869cd7385f30bbb19a4bb7cf633c93c73bc3073f62a22f16183b378"
NAMES = ("c", "d2", "d4", "x1", "x3", "x5", "inv")
GROUPS = (
    *((name, (name,)) for name in NAMES),
    ("normal_triple", ("c", "d2", "d4")),
    ("invariant_triple", ("x1", "x3", "x5")),
    ("true_center_six", ("c", "d2", "d4", "x1", "x3", "x5")),
    ("global_seven", NAMES),
)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_module(name: str, path: Path, expected: str):
    got = digest(path)
    if got != expected:
        raise RuntimeError((name, str(path), got, expected))
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(("cannot import", name, str(path)))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build_hermite(shape, series, order: int, helper):
    points = shape["w_values"]
    if len(points) != 123 or len(set(points)) != 123:
        raise RuntimeError("shape point set")
    base_indices = [index for index, point in enumerate(points) if point == BASE_W]
    if len(base_indices) != 1:
        raise RuntimeError(("base point", base_indices))
    base_index = base_indices[0]
    shifted = [((point - BASE_W) % P) for point in points]
    nonzero_indices = [index for index, point in enumerate(shifted) if point != 0]
    nonzero_points = [shifted[index] for index in nonzero_indices]
    if len(nonzero_points) != 122 or len(set(nonzero_points)) != 122:
        raise RuntimeError("shifted nonzero points")

    residual_modulus = helper.modulus_for_points(nonzero_points)
    residual_basis = helper.lagrange_basis(nonzero_points, residual_modulus)
    modulus = [0] * order + residual_modulus
    modulus_degree = len(modulus) - 1
    if modulus_degree != 122 + order or modulus[-1] != 1:
        raise RuntimeError(("Hermite modulus", modulus_degree, order))

    interpolants = {}
    for name in NAMES:
        rows = []
        values_by_v = shape["samples"][name]
        if len(values_by_v) != 190 or len(series[name]) != 190:
            raise RuntimeError((name, len(values_by_v), len(series[name])))
        for v_degree in range(190):
            values = values_by_v[v_degree]
            taylor = series[name][v_degree]
            if len(values) != 123 or len(taylor) != order:
                raise RuntimeError((name, v_degree, len(values), len(taylor)))
            if values[base_index] % P != taylor[0] % P:
                raise RuntimeError(
                    ("base mismatch", name, v_degree, values[base_index], taylor[0])
                )
            corrections = []
            for index, point in zip(nonzero_indices, nonzero_points, strict=True):
                point_power = pow(point, order, P)
                correction = (
                    values[index] - helper.evaluate(taylor, point)
                ) % P
                corrections.append(correction * pow(point_power, P - 2, P) % P)
            quotient = helper.interpolate(corrections, residual_basis)
            polynomial = bytearray(modulus_degree)
            for index, coefficient in enumerate(taylor):
                polynomial[index] = coefficient % P
            for index, coefficient in enumerate(quotient):
                polynomial[order + index] = coefficient % P
            if list(polynomial[:order]) != [value % P for value in taylor]:
                raise AssertionError(("Taylor reconstruction", name, v_degree))
            for point, expected in zip(shifted, values, strict=True):
                if helper.evaluate(polynomial, point) != expected % P:
                    raise AssertionError(
                        ("fibre reconstruction", name, v_degree, point, expected)
                    )
            rows.append(polynomial)
        interpolants[name] = rows
    return {
        "order": order,
        "modulus": modulus,
        "modulus_degree": modulus_degree,
        "shifted_points": shifted,
        "interpolants": interpolants,
    }


def build_shifts(hermite, helper):
    modulus = hermite["modulus"]
    return {
        name: [helper.shifted_remainders(polynomial, modulus) for polynomial in rows]
        for name, rows in hermite["interpolants"].items()
    }


def flatten_names(shifts, names):
    return [table for name in names for table in shifts[name]]


def validate_tables(tables, denominator, numerator_bound, modulus_degree):
    for table in tables:
        for coefficient_degree in range(numerator_bound + 1, modulus_degree):
            value = sum(
                denominator[power] * table[power][coefficient_degree]
                for power in range(len(denominator))
            ) % P
            if value:
                return False
    return True


def search_unique(tables, shifted_points, modulus_degree, helper):
    tested = 0
    full_rank = 0
    rank_deficient = 0
    rejected_base_pole = 0
    rejected_sample_pole = 0
    # Exclude total=M-1, which always admits the tautological polynomial
    # interpolant.  Every returned pair obeys d+m <= M-2.
    for total in range(modulus_degree - 1):
        for denominator_degree in range(total + 1):
            numerator_bound = total - denominator_degree
            columns = denominator_degree + 1
            echelon = {}
            for table in tables:
                for coefficient_degree in range(
                    numerator_bound + 1, modulus_degree
                ):
                    row = [
                        table[power][coefficient_degree]
                        for power in range(columns)
                    ]
                    helper.echelon_add(echelon, row)
                    if len(echelon) == columns:
                        break
                if len(echelon) == columns:
                    break
            tested += 1
            nullity = columns - len(echelon)
            if nullity == 0:
                full_rank += 1
                continue
            if nullity != 1:
                rank_deficient += 1
                continue
            denominator = helper.nullspace_basis(echelon, columns)[0]
            if helper.degree(denominator) != denominator_degree:
                rank_deficient += 1
                continue
            if denominator[0] % P == 0:
                rejected_base_pole += 1
                continue
            inverse = pow(denominator[0] % P, P - 2, P)
            denominator = [(inverse * value) % P for value in denominator]
            if any(helper.evaluate(denominator, point) == 0 for point in shifted_points):
                rejected_sample_pole += 1
                continue
            if not validate_tables(
                tables, denominator, numerator_bound, modulus_degree
            ):
                raise AssertionError("solve/validate mismatch")
            return {
                "denominator": denominator,
                "denominator_degree": denominator_degree,
                "numerator_degree": numerator_bound,
                "total_degree": total,
                "rank": len(echelon),
                "tested_pairs": tested,
                "full_rank_pairs": full_rank,
                "rank_deficient_pairs": rank_deficient,
                "rejected_base_pole_pairs": rejected_base_pole,
                "rejected_sample_pole_pairs": rejected_sample_pole,
            }
    return {
        "status": "NO_UNIQUE_NONTAUTOLOGICAL_FIT",
        "tested_pairs": tested,
        "full_rank_pairs": full_rank,
        "rank_deficient_pairs": rank_deficient,
        "rejected_base_pole_pairs": rejected_base_pole,
        "rejected_sample_pole_pairs": rejected_sample_pole,
    }


def is_fit(result) -> bool:
    return "denominator" in result


def analyze_group(label, names, lower, upper, lower_shifts, upper_shifts, helper):
    lower_tables = flatten_names(lower_shifts, names)
    upper_tables = flatten_names(upper_shifts, names)
    lower_fit = search_unique(
        lower_tables, lower["shifted_points"], lower["modulus_degree"], helper
    )
    lower_holdout = False
    if is_fit(lower_fit):
        lower_holdout = validate_tables(
            upper_tables,
            lower_fit["denominator"],
            lower_fit["numerator_degree"],
            upper["modulus_degree"],
        )
    upper_fit = search_unique(
        upper_tables, upper["shifted_points"], upper["modulus_degree"], helper
    )
    selected = None
    source = None
    if is_fit(lower_fit) and lower_holdout:
        selected = lower_fit
        source = "lower_hermite_fit_with_upper_jet_holdout"
    elif is_fit(upper_fit):
        selected = upper_fit
        source = "upper_hermite_fit_unvalidated_beyond_upper"
    return {
        "label": label,
        "coordinates": list(names),
        "sequence_count": len(upper_tables),
        "lower_fit": lower_fit,
        "lower_fit_valid_through_upper": lower_holdout,
        "upper_fit": upper_fit,
        "selected": selected,
        "selected_source": source,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--shape", type=Path, required=True)
    parser.add_argument("--parent", type=Path, required=True)
    parser.add_argument("--poly-helper", type=Path, required=True)
    parser.add_argument("--lower", type=Path, required=True)
    parser.add_argument("--lower-order", type=int, required=True)
    parser.add_argument("--upper", type=Path, required=True)
    parser.add_argument("--upper-order", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if digest(args.shape) != SHAPE_SHA256:
        raise RuntimeError(("shape hash", digest(args.shape), SHAPE_SHA256))
    if not (2 <= args.lower_order < args.upper_order):
        raise RuntimeError((args.lower_order, args.upper_order))
    parent = load_module("q8_pade_parent", args.parent, PARENT_SHA256)
    helper = load_module("q8_poly_helper", args.poly_helper, HELPER_SHA256)
    shape = json.loads(args.shape.read_text())
    if shape.get("status") != "PASS" or shape.get("prime") != P:
        raise RuntimeError("shape endpoint")
    lower_series = parent.read_series(args.lower, args.lower_order)
    upper_series = parent.read_series(args.upper, args.upper_order)
    if not parent.prefix_equal(parent.flatten(lower_series), parent.flatten(upper_series)):
        raise RuntimeError("independent jet prefix mismatch")

    lower = build_hermite(shape, lower_series, args.lower_order, helper)
    upper = build_hermite(shape, upper_series, args.upper_order, helper)
    lower_shifts = build_shifts(lower, helper)
    upper_shifts = build_shifts(upper, helper)
    analyses = {
        label: analyze_group(
            label, names, lower, upper, lower_shifts, upper_shifts, helper
        )
        for label, names in GROUPS
    }
    payload = {
        "status": "PASS",
        "scope": (
            "exact Hermite-Pade reconstruction over F_127 from 123 fibres plus "
            "moving-v jets; candidates require later holdout and full mod-H substitution"
        ),
        "prime": P,
        "base_w": BASE_W,
        "shape_sha256": digest(args.shape),
        "parent_sha256": digest(args.parent),
        "poly_helper_sha256": digest(args.poly_helper),
        "lower_order": args.lower_order,
        "lower_sha256": digest(args.lower),
        "lower_condition_count": lower["modulus_degree"],
        "upper_order": args.upper_order,
        "upper_sha256": digest(args.upper),
        "upper_condition_count": upper["modulus_degree"],
        "jet_prefix_match": True,
        "base_fibre_match_all_1330": True,
        "groups": analyses,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print("Q8-P127-HERMITE-COORDINATE-RECONSTRUCTION")
    print("status=PASS")
    print(f"orders={args.lower_order},{args.upper_order}")
    print(
        f"condition_counts={lower['modulus_degree']},{upper['modulus_degree']}"
    )
    print("jet_prefix_match=1")
    print("base_fibre_match_all_1330=1")
    for label, _ in GROUPS:
        item = analyses[label]
        selected = item["selected"]
        if selected is None:
            summary = "NONE"
        else:
            summary = (
                f"{item['selected_source']}:d={selected['denominator_degree']},"
                f"m={selected['numerator_degree']}"
            )
        print(f"group={label} selected={summary}")
    print("output_sha256=" + digest(args.output))


if __name__ == "__main__":
    main()

