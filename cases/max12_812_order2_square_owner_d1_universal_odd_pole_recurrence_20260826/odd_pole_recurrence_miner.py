#!/usr/bin/env python3
"""Exact odd-row Laurent-to-Faber pole-recurrence miner; AWS only."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import platform
from fractions import Fraction
from pathlib import Path


def fail(message: object) -> None:
    raise SystemExit(f"FAIL: {message}")


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only compiler: Linux required")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.exists() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only compiler: Amazon EC2 DMI required")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "").strip()
    if not tag.startswith("max12_812_order2_square_d1_odd_pole_recurrence_"):
        fail("registered odd-pole recurrence lane tag required")
    return tag


def choose(alpha: Fraction, degree: int) -> Fraction:
    result = Fraction(1)
    for index in range(degree):
        result *= alpha - index
    return result / math.factorial(degree)


def power_coefficient(alpha: Fraction, degree: int) -> Fraction:
    """Scalar of s^degree*x^degree in (1-s*x)^alpha."""

    return (-1) ** degree * choose(alpha, degree)


def ordinary_basis_coefficient(q: int, e: int, row: int) -> Fraction:
    """Scalar of s^(row-e) in [x^row] x^e/(1+s*x)^q."""

    if row < e:
        return Fraction(0)
    degree = row - e
    return (-1) ** degree * Fraction(math.comb(q + degree - 1, degree))


def faber_matrix_coefficient(target: int, source: int) -> Fraction:
    """Scalar of s^(target-source) in the odd Faber transport."""

    if target < source:
        return Fraction(0)
    degree = target - source
    result = Fraction(1)
    for index in range(degree):
        result *= Fraction(source, 1) + Fraction(1, 2) + index
    return result / math.factorial(degree)


def transformed_basis_coefficient(q: int, e: int, row: int) -> Fraction:
    """Rebuild [x^row] Phi from the ordinary basis and Faber matrix."""

    return sum(
        ordinary_basis_coefficient(q, e, source)
        * faber_matrix_coefficient(row, source)
        for source in range(e, row + 1)
    )


def closed_transformed_coefficient(q: int, e: int, row: int) -> Fraction:
    """Closed scalar from x^e(1-s*x)^(q-e-1/2)."""

    if row < e:
        return Fraction(0)
    return power_coefficient(Fraction(q - e, 1) - Fraction(1, 2), row - e)


def recurrence_weights(m: int, r: int) -> list[Fraction]:
    """Scalars w_j in W=sum w_j*s^j*x^j."""

    alpha = Fraction(m - r, 1) - Fraction(1, 2)
    return [power_coefficient(alpha, degree) for degree in range(m + 1)]


def functional_coefficient(m: int, r: int, q: int, e: int) -> Fraction:
    """Scalar of s^(m-e) in [x^m](W_{m,r} Phi_{q,e})."""

    weights = recurrence_weights(m, r)
    return sum(
        weights[degree]
        * transformed_basis_coefficient(q, e, m - degree)
        for degree in range(m + 1)
        if m - degree >= e
    )


def text_fraction(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def modular(value: Fraction, characteristic: int) -> int:
    if characteristic == 0:
        return 0 if value == 0 else 1
    return (value.numerator % characteristic) * pow(value.denominator, -1, characteristic) % characteristic


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    parser.add_argument("--max-terminal", type=int, default=24)
    parser.add_argument("--inventory", type=Path)
    parser.add_argument("--inventory-max-grade", type=int, default=38)
    parser.add_argument("--inventory-max-pole", type=int, default=3)
    args = parser.parse_args()
    tag = require_aws()
    if args.max_terminal < 3:
        fail("max-terminal must be at least three")
    output = args.output.resolve()
    if output.exists():
        fail("output already exists")
    output.mkdir(parents=True)

    transform_checks = 0
    annihilation_checks = 0
    sharp_checks = 0
    for m in range(1, args.max_terminal + 1):
        for q in range(1, m + 2):
            for e in range(q):
                for row in range(e, m + 1):
                    lhs = transformed_basis_coefficient(q, e, row)
                    rhs = closed_transformed_coefficient(q, e, row)
                    if lhs != rhs or (args.characteristic and modular(lhs - rhs, args.characteristic)):
                        fail(("Laurent-to-Faber transform", m, q, e, row, lhs, rhs))
                    transform_checks += 1
        for r in range(1, m + 1):
            for q in range(1, r + 1):
                for e in range(q):
                    value = functional_coefficient(m, r, q, e)
                    if value or (args.characteristic and modular(value, args.characteristic)):
                        fail(("recurrence did not annihilate", m, r, q, e, value))
                    annihilation_checks += 1
            value = functional_coefficient(m, r, r + 1, r)
            expected = Fraction((-1) ** (m - r))
            if value != expected or (
                args.characteristic and modular(value - expected, args.characteristic)
            ):
                fail(("first-outside-pole negative control", m, r, value, expected))
            sharp_checks += 1
        if functional_coefficient(m, m, m + 1, m) != 1:
            fail(("terminal sharpness control", m))

    row7_r2 = recurrence_weights(3, 2)
    row7_r3 = recurrence_weights(3, 3)
    expected_r2 = [Fraction(1), Fraction(-1, 2), Fraction(-1, 8), Fraction(-1, 16)]
    expected_r3 = [Fraction(1), Fraction(1, 2), Fraction(3, 8), Fraction(5, 16)]
    if row7_r2 != expected_r2 or row7_r3 != expected_r3:
        fail(("row-seven specializations", row7_r2, row7_r3))

    inventory_payload = None
    if args.inventory is not None:
        inventory_path = args.inventory.resolve()
        inventory_payload = json.loads(inventory_path.read_text())
        primitives = inventory_payload.get("primitive_families")
        if not isinstance(primitives, list) or not primitives:
            fail("inventory has no primitive_families")
        in_window = [
            item for item in primitives
            if int(item["base_grade"]) <= args.inventory_max_grade
        ]
        if not in_window:
            fail("inventory has no in-window primitive family")
        highest = max(int(item["pole"]) for item in in_window)
        if highest > args.inventory_max_pole:
            fail(("inventory pole ceiling exceeded", highest, args.inventory_max_pole))
        if inventory_payload.get("jet_maxima") != {
            "A": 7, "C": 10, "R": 6, "k10": 6, "k6": 10, "k2": 6,
            "p": 10, "mu20": 10, "mu4": 6, "mu6": 2,
        }:
            fail(("inventory jet maxima mismatch", inventory_payload.get("jet_maxima")))

    payload = {
        "status": "PASS-UNIVERSAL-ODD-POLE-RECURRENCE-MINER",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "max_terminal": args.max_terminal,
        "transform_checks": transform_checks,
        "annihilation_checks": annihilation_checks,
        "sharp_negative_checks": sharp_checks,
        "faber_transform": "Phi(x)=(1-s*x)^(-1/2)*Y(x/(1-s*x)), s=p/2",
        "basis_transform": "x^e/(1+s*x)^q -> x^e*(1-s*x)^(q-e-1/2)",
        "functional": "W_(M,r)(x)=(1-s*x)^(M-r-1/2)",
        "row7_r2_scalars_in_s": [text_fraction(item) for item in row7_r2],
        "row7_r3_scalars_in_s": [text_fraction(item) for item in row7_r3],
        "inventory_sha256": None if args.inventory is None else digest(args.inventory.resolve()),
        "inventory_max_grade": None if args.inventory is None else args.inventory_max_grade,
        "inventory_max_pole": None if args.inventory is None else args.inventory_max_pole,
    }
    result_path = output / "result.json"
    result_path.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print("ODDREC_LAURENT_TO_FABER_TRANSFORM=PASS")
    print("ODDREC_ALL_POLES_Q_LE_R=PASS")
    print("ODDREC_FIRST_OUTSIDE_POLE_NEGATIVE_CONTROLS=PASS")
    print("ODDREC_TERMINAL_POLE_NEGATIVE_CONTROLS=PASS")
    print("ODDREC_ROW7_R2_S_SCALARS=1,-1/2,-1/8,-1/16")
    print("ODDREC_ROW7_R3_S_SCALARS=1,1/2,3/8,5/16")
    if args.inventory is not None:
        print("ODDREC_COMPLETE_INVENTORY_POLE_CEILING=PASS")
    print("ODDREC_ENDPOINT=PASS_UNIVERSAL_ODD_POLE_RECURRENCE_MINER")


if __name__ == "__main__":
    main()
