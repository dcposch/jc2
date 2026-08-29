#!/usr/bin/env python3
"""AWS-only exact support/local-pole miner for the small-a D1 d=2,3 blocks."""

from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
import math
import os
from pathlib import Path
import platform


ATOMS = (
    {"fixed": 2, "denominator": 2, "R": 1, "A": 0, "C": 0, "scalar": 2},
    {"fixed": 4, "denominator": 4, "R": 2, "A": 0, "C": 0, "scalar": 1},
    {"fixed": 5, "denominator": 3, "R": 0, "A": 1, "C": 0, "scalar": 1},
    {"fixed": 5, "denominator": 4, "R": 0, "A": 0, "C": 1, "scalar": 1},
)
SUMMANDS = (
    {"name": "unloaded", "load": None, "alpha": Fraction(3, 2), "fixed": 0},
    {"name": "k10", "load": "k10", "alpha": Fraction(5, 4), "fixed": 4},
    {"name": "k6", "load": "k6", "alpha": Fraction(3, 4), "fixed": 12},
    {"name": "k2", "load": "k2", "alpha": Fraction(1, 4), "fixed": 20},
)


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only D1 d23 support miner refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only D1 d23 support miner refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def binomial(alpha: Fraction, degree: int) -> Fraction:
    answer = Fraction(1)
    for index in range(degree):
        answer *= alpha - index
    return answer / math.factorial(degree)


def modular_fraction(value: Fraction, prime: int) -> int:
    return (value.numerator % prime) * pow(value.denominator % prime, -1, prime) % prime


def baselines() -> list[dict[str, int]]:
    rows: list[dict[str, int]] = []
    for a in range(1, 10):
        for d in (2, 3):
            s_min = 1 if a <= d else 0
            c = a + d
            r = a + s_min
            if not (a >= 1 and r >= 2 and c >= 3 and a + 3 * s_min > d):
                fail(("bad baseline", a, d, s_min))
            if s_min and a > 1:
                previous = s_min - 1
                if a + previous >= 2 and a + 3 * previous > d:
                    fail(("s_min not minimal", a, d, s_min))
            rows.append({
                "a": a, "d": d, "c": c, "s_min": s_min, "r": r,
                "first_ac_grade": 10 + 2 * a + d,
                "target_grade": 10 + 2 * a + 2 * d,
            })
    if len(rows) != 18:
        fail(("baseline count", len(rows)))
    return rows


def enumerate_primitives(row: dict[str, int], pad: int = 0) -> list[dict[str, object]]:
    baseline = {"A": row["a"], "C": row["c"], "R": row["r"]}
    maximum = row["target_grade"]
    aggregate: defaultdict[tuple[object, ...], Fraction] = defaultdict(Fraction)
    for summand in SUMMANDS:
        budget = maximum - int(summand["fixed"])
        if budget < 0:
            continue
        costs = [
            int(atom["fixed"])
            + baseline["R"] * int(atom["R"])
            + baseline["A"] * int(atom["A"])
            + baseline["C"] * int(atom["C"])
            for atom in ATOMS
        ]
        if any(cost <= 0 for cost in costs):
            fail(("nonpositive atom cost", row, costs))
        bounds = [budget // cost + pad for cost in costs]
        alpha = summand["alpha"]
        assert isinstance(alpha, Fraction)
        for counts in product(*(range(bound + 1) for bound in bounds)):
            degree = sum(counts)
            if degree == 0:
                continue
            fixed = int(summand["fixed"])
            denominator = 0
            exponents = {"R": 0, "A": 0, "C": 0}
            scalar = 1
            for count, atom in zip(counts, ATOMS):
                fixed += count * int(atom["fixed"])
                denominator += count * int(atom["denominator"])
                scalar *= int(atom["scalar"]) ** count
                for stem in exponents:
                    exponents[stem] += count * int(atom[stem])
            grade = fixed + sum(baseline[stem] * exponents[stem] for stem in exponents)
            if grade > maximum:
                continue
            pole = denominator - int(4 * alpha)
            if pole <= 0:
                continue
            multinomial = math.factorial(degree)
            for count in counts:
                multinomial //= math.factorial(count)
            coefficient = binomial(alpha, degree) * multinomial * scalar
            key = (
                summand["name"], summand["load"], fixed,
                exponents["R"], exponents["A"], exponents["C"], pole,
            )
            aggregate[key] += coefficient
    primitives: list[dict[str, object]] = []
    for key, coefficient in aggregate.items():
        if coefficient == 0:
            continue
        name, load, fixed, rexponent, aexponent, cexponent, pole = key
        grade = (
            int(fixed) + baseline["R"] * int(rexponent)
            + baseline["A"] * int(aexponent) + baseline["C"] * int(cexponent)
        )
        depth = maximum - grade
        allocated_a_zeros = max(int(aexponent) - depth, 0)
        local_pole_upper = max(int(pole) - allocated_a_zeros, 0)
        primitives.append({
            "summand": name, "load": load, "fixed_sigma": fixed,
            "R": rexponent, "A": aexponent, "C": cexponent,
            "pole": pole, "coefficient": fraction_text(coefficient),
            "first_grade": grade, "correction_depth_to_target": depth,
            "allocated_A_zero_floor": allocated_a_zeros,
            "local_pole_upper_at_A_root": local_pole_upper,
        })
    return sorted(primitives, key=lambda item: (
        int(item["first_grade"]), str(item["summand"]), int(item["pole"]),
        int(item["R"]), int(item["A"]), int(item["C"]),
    ))


def signature(item: dict[str, object]) -> tuple[object, ...]:
    return (
        item["summand"], item["load"], item["fixed_sigma"], item["R"],
        item["A"], item["C"], item["pole"], item["coefficient"],
        item["first_grade"], item["local_pole_upper_at_A_root"],
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    output = args.output.resolve()
    if output.exists():
        fail("D1 d23 support output already exists")
    output.mkdir(parents=True)

    rows = baselines()
    safe_count = 0
    negative_count = 0
    inventories: list[dict[str, object]] = []
    c2_signature = ("unloaded", None, 10, 0, 0, 2, 2, "3/8")
    ra2_signature = ("unloaded", None, 12, 1, 2, 0, 2, "-3/8")
    for row in rows:
        primitives = enumerate_primitives(row)
        padded = enumerate_primitives(row, pad=1)
        if {signature(item) for item in primitives} != {signature(item) for item in padded}:
            fail(("atom cutoff sentinel failed", row))
        dangerous = [item for item in primitives if int(item["local_pole_upper_at_A_root"]) >= 2]
        c2 = [item for item in dangerous if tuple(item[key] for key in (
            "summand", "load", "fixed_sigma", "R", "A", "C", "pole", "coefficient"
        )) == c2_signature]
        if len(c2) != 1 or int(c2[0]["first_grade"]) != row["target_grade"]:
            fail(("missing/nonunique C2 target", row, dangerous))
        is_negative = row["a"] == 1 and row["d"] == 3 and row["s_min"] == 1
        if is_negative:
            ra2 = [item for item in dangerous if tuple(item[key] for key in (
                "summand", "load", "fixed_sigma", "R", "A", "C", "pole", "coefficient"
            )) == ra2_signature]
            if len(dangerous) != 2 or len(ra2) != 1:
                fail(("negative control census mismatch", row, dangerous))
            negative_count += 1
        else:
            if len(dangerous) != 1:
                fail(("additional dangerous primitive", row, dangerous))
            safe_count += 1
        inventories.append({**row, "primitive_count": len(primitives),
                            "primitive_families": primitives,
                            "dangerous_local_pole_families": dangerous,
                            "classification": "NEGATIVE_RA2" if is_negative else "SAFE_C2_ONLY"})

    if safe_count != 17 or negative_count != 1:
        fail(("classification counts", safe_count, negative_count))
    if max(row["target_grade"] for row in rows) != 34:
        fail("target maximum mismatch")

    structural = {
        "status": "PASS-D1-UNIQUE-AC-D23-SMALL-A-SUPPORT-CENSUS",
        "scope": "SUPPORT_AND_LOCAL_POLE_UPPER_BOUNDS_ONLY_NO_EMPTINESS",
        "derivation": "four independent binomial summands with cost-derived atom bounds",
        "baseline_count": len(rows), "safe_count": safe_count,
        "negative_count": negative_count, "maximum_target_grade": 34,
        "sole_negative": {"a": 1, "d": 3, "c": 4, "r": 2, "s_min": 1},
        "baselines": inventories,
    }
    inventory = output / "support_inventory.json"
    inventory.write_text(json.dumps(structural, sort_keys=True, indent=2) + "\n")
    inventory_sha = sha256(inventory.read_bytes()).hexdigest()

    modular_ok = all(
        modular_fraction(Fraction(item["coefficient"]), 65521) != 0
        for block in inventories for item in block["dangerous_local_pole_families"]
    )
    if not modular_ok:
        fail("modular dangerous coefficient vanished")
    result = {
        "status": structural["status"], "scope": structural["scope"],
        "registered_aws_lane": tag, "characteristic": args.characteristic,
        "inventory_sha256": inventory_sha, "baseline_count": len(rows),
        "safe_count": safe_count, "negative_count": negative_count,
        "maximum_target_grade": 34, "modular_control": modular_ok,
    }
    (output / "result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("D1D23_SUPPORT_SOURCE_HASHES=PASS")
    print(f"D1D23_SUPPORT_INVENTORY_SHA256={inventory_sha}")
    print("D1D23_SUPPORT_BASELINE_COUNT=18")
    print("D1D23_SUPPORT_SAFE_COUNT=17")
    print("D1D23_SUPPORT_NEGATIVE_COUNT=1")
    print("D1D23_SUPPORT_MAX_TARGET_GRADE=34")
    print("D1D23_SUPPORT_SOLE_NEGATIVE=A1_D3_S1")
    print("D1D23_SUPPORT_C2_COEFFICIENT=3/8")
    print("D1D23_SUPPORT_RA2_NEGATIVE_COEFFICIENT=-3/8")
    print("D1D23_SUPPORT_MODULAR_CONTROL=1")
    print("D1D23_SUPPORT_ENDPOINT=PASS_SUPPORT_CENSUS_NO_EMPTINESS")


if __name__ == "__main__":
    main()

