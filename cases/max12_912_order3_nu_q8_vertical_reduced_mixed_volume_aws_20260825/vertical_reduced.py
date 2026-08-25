#!/usr/bin/env python3
"""Sparse vertical-degree bound after exact ratio substitution."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
from math import comb
from pathlib import Path
import subprocess
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PARENT = ROOT / "cases/max12_912_order3_nu_q8_sparse_mixed_volume_aws_20260825/mixed_volume.py"
PARENT_SHA256 = "a6a516d6558cdceee02e7340ad179e0e142af653506bd0f5468ee8e2027267f9"
DIMENSION = 6


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_parent():
    if digest(PARENT) != PARENT_SHA256:
        raise RuntimeError("parent hash")
    spec = importlib.util.spec_from_file_location("q8_vertical_mv_parent", PARENT)
    if spec is None or spec.loader is None:
        raise RuntimeError(PARENT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    module.DIMENSION = DIMENSION
    return module


def reduced_generic_w_support(row: dict) -> tuple[set[tuple[int, ...]], dict]:
    # Substitute x3=(v+2)*x5 and retain a coefficient polynomial in generic w.
    coefficients: dict[tuple[int, ...], dict[int, Fraction]] = {}
    for monomial, scalar in row.items():
        ew, ec, ed2, ed4, ex1, ex3, ex5 = monomial
        scalar = Fraction(scalar)
        for kv in range(ex3 + 1):
            new_monomial = (ec, ed2, ed4, ex1, ex3 + ex5, kv)
            factor = scalar * comb(ex3, kv) * (2 ** (ex3 - kv))
            polynomial = coefficients.setdefault(new_monomial, {})
            polynomial[ew] = polynomial.get(ew, Fraction(0)) + factor
    support = set()
    coefficient_records = {}
    for monomial, polynomial in coefficients.items():
        polynomial = {degree: value for degree, value in polynomial.items() if value}
        if polynomial:
            support.add(monomial)
            coefficient_records[str(monomial)] = [
                [degree, str(value)] for degree, value in sorted(polynomial.items())
            ]
    return support, coefficient_records


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--work", type=Path, required=True)
    parser.add_argument("--workers", type=int, default=12)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 1 <= args.workers <= 32:
        raise RuntimeError(args.workers)
    args.work.mkdir(parents=True, exist_ok=False)
    parent = load_parent()
    compiler = parent.load_compiler()
    _, rows, imposed, names = compiler.compile_quotient("approx")
    if tuple(imposed) != (1, 3, 5, 7, 2, 4):
        raise RuntimeError(imposed)
    if names != ["w", "c", "d2", "d4", "x1", "x3", "x5"]:
        raise RuntimeError(names)
    supports = []
    records = {}
    for ell in imposed:
        support, coefficient_record = reduced_generic_w_support(rows[ell])
        supports.append(support)
        records[str(ell)] = coefficient_record
    zero = (0,) * DIMENSION
    augmented = [set(support) | {zero} for support in supports]
    raw = parent.mixed_volume(supports, args.work / "raw", args.workers)
    affine = parent.mixed_volume(augmented, args.work / "origin_augmented", args.workers)
    controls = parent.standard_controls(args.work / "controls", args.workers)
    payload = {
        "status": "PASS",
        "variables": ["c", "d2", "d4", "x1", "x5", "v"],
        "substitution": "generic w=alpha and x3=(v+2)*x5",
        "localization": "x5*v != 0 on the selected chart; origin augmentation is retained as a safe affine overcount",
        "source_support_sizes_before": [len(rows[ell]) for ell in imposed],
        "source_support_sizes_after": [len(support) for support in supports],
        "generic_w_coefficient_records": records,
        "raw_torus": raw,
        "origin_augmented_affine": affine,
        "vertical_degree_bound": affine["mixed_volume"],
        "controls": controls,
        "normaliz_version": subprocess.check_output(["normaliz", "--version"], text=True).splitlines()[0],
        "parent_sha256": PARENT_SHA256,
        "scope": "support-exact generic-vertical affine-BKK upper bound; no exact fibre length or component uniqueness asserted unless bound <380",
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print("Q8-VERTICAL-REDUCED-MIXED-VOLUME")
    print("status=PASS")
    print("raw_torus=" + str(raw["mixed_volume"]))
    print("origin_augmented_affine=" + str(affine["mixed_volume"]))
    print("controls=" + json.dumps(controls, sort_keys=True))
    print("output_sha256=" + digest(args.output))


if __name__ == "__main__":
    main()
