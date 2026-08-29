#!/usr/bin/env python3
"""Emit complete filtered V17 load-obstruction matrices; AWS only."""

from __future__ import annotations

import argparse
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
import json
import os
from pathlib import Path
import platform
import re


HERE = Path(__file__).resolve().parent
PREREG = HERE / "PREREGISTRATION.md"
EXPECTED_PRELUDE = "5b0a77e6d16df30de2df344862fc4316aedcc8aeabf1ec81e23d7881ce67ee7a"
NVAR = 6
ZERO = (0,) * NVAR
LOADS = ("K10", "K6", "K2")
Key = tuple[int, int, int, int, int, int]
Poly = dict[Key, Fraction]


def fail(message: object) -> "None":
    raise RuntimeError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only V18 emitter refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only V18 emitter refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def parse_poly(text: str) -> Poly:
    source = "".join(text.split())
    if not source or any(char in source for char in "();,\""):
        fail(("malformed polynomial", source[:120]))
    if source == "0":
        return {}
    starts = [0]
    for index, char in enumerate(source[1:], 1):
        if char in "+-":
            starts.append(index)
    starts.append(len(source))
    result: Poly = {}
    for left, right in zip(starts, starts[1:]):
        raw = source[left:right]
        sign = 1
        if raw[0] == "+":
            raw = raw[1:]
        elif raw[0] == "-":
            sign = -1
            raw = raw[1:]
        if not raw:
            fail("empty term")
        coefficient = Fraction(sign)
        exponents = [0] * NVAR
        for factor in raw.split("*"):
            variable = re.fullmatch(r"d([0-5])(?:\^(\d+))?", factor)
            if variable:
                index = int(variable.group(1))
                exponent = int(variable.group(2) or "1")
                if exponent <= 0:
                    fail(("bad exponent", factor))
                exponents[index] += exponent
                continue
            if not re.fullmatch(r"\d+(?:/\d+)?", factor):
                fail(("unparsed factor", factor, source[:120]))
            coefficient *= Fraction(factor)
        key = tuple(exponents)
        result[key] = result.get(key, Fraction(0)) + coefficient
    return {key: value for key, value in result.items() if value}


def parse_rows(prelude: Path) -> list[Poly]:
    text = prelude.read_text()
    rows: list[Poly] = []
    for index in range(1, 7):
        match = re.search(rf"(?:^|\n)poly r{index}=(.*?);", text, re.S)
        if not match:
            fail(("missing prelude row", index))
        rows.append(parse_poly(match.group(1)))
    if len(rows) != 6:
        fail("row count")
    return rows


def parse_ideal(path: Path) -> list[Poly]:
    text = "".join(path.read_text().split())
    if not text:
        fail(("empty ideal serialization", str(path)))
    return [parse_poly(piece) for piece in text.split(",")]


def order(poly: Poly) -> int | None:
    return min((sum(key) for key in poly), default=None)


def max_degree(poly: Poly) -> int | None:
    return max((sum(key) for key in poly), default=None)


@lru_cache(maxsize=None)
def monomials(degree: int, variables: int = NVAR) -> tuple[Key, ...]:
    def build(left: int, count: int, prefix: tuple[int, ...]):
        if count == 1:
            yield prefix + (left,)
            return
        for exponent in range(left + 1):
            yield from build(left - exponent, count - 1, prefix + (exponent,))
    return tuple(build(degree, variables, ()))


def all_monomials(maximum: int) -> tuple[Key, ...]:
    return tuple(key for degree in range(maximum + 1) for key in monomials(degree))


def coefficient_text(value: Fraction) -> tuple[str, str]:
    return str(value.numerator), str(value.denominator)


def poly_summary(poly: Poly) -> dict[str, object]:
    counts: dict[str, int] = {}
    for key in poly:
        degree = str(sum(key))
        counts[degree] = counts.get(degree, 0) + 1
    return {
        "terms": len(poly),
        "minimum_degree": order(poly),
        "maximum_degree": max_degree(poly),
        "degree_term_counts": counts,
    }


def write_matrix(output: Path, label: str, generators: list[Poly], target: Poly,
                 cutoff: int) -> dict[str, object]:
    row_keys = all_monomials(cutoff)
    row_index = {key: index for index, key in enumerate(row_keys)}
    columns: list[tuple[int, Key]] = []
    for generator_index, generator in enumerate(generators):
        minimum = order(generator)
        if minimum is None or minimum > cutoff:
            continue
        for multiplier_degree in range(cutoff - minimum + 1):
            for multiplier in monomials(multiplier_degree):
                columns.append((generator_index, multiplier))
    entries: dict[tuple[int, int], Fraction] = {}
    for column, (generator_index, multiplier) in enumerate(columns):
        for key, value in generators[generator_index].items():
            shifted = tuple(a + b for a, b in zip(key, multiplier))
            if sum(shifted) <= cutoff:
                location = (row_index[shifted], column)
                entries[location] = entries.get(location, Fraction(0)) + value
    target_column = len(columns)
    for key, value in target.items():
        if sum(key) <= cutoff:
            entries[(row_index[key], target_column)] = value
    entries = {key: value for key, value in entries.items() if value}
    stem = f"{label}_D{cutoff}"
    matrix = output / f"matrix_{stem}.tsv"
    with matrix.open("w") as handle:
        handle.write(f"{len(row_keys)} {len(columns)} {len(entries)} {cutoff}\n")
        for (row, column), value in sorted(entries.items()):
            numerator, denominator = coefficient_text(value)
            handle.write(f"{row} {column} {numerator} {denominator}\n")
    row_map = output / f"rows_{stem}.json"
    row_map.write_text(json.dumps([list(key) for key in row_keys], separators=(",", ":")) + "\n")
    column_map = output / f"columns_{stem}.json"
    column_map.write_text(json.dumps([
        {"generator_index": generator + 1, "multiplier": list(multiplier)}
        for generator, multiplier in columns
    ], separators=(",", ":")) + "\n")
    return {
        "direction": label,
        "cutoff": cutoff,
        "rows": len(row_keys),
        "columns": len(columns),
        "nonzero_entries_including_target": len(entries),
        "matrix_sha256": digest(matrix),
        "row_map_sha256": digest(row_map),
        "column_map_sha256": digest(column_map),
        "row_order": "total_degree_0_to_D_then_recursive_lex_d0_to_d5",
        "column_order": "r1_to_r6_then_E_serialization; multiplier_degree_then_recursive_lex",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("v17_lane", type=Path)
    parser.add_argument("row_prelude", type=Path)
    parser.add_argument("--field", choices=("Q", "65521"), required=True)
    parser.add_argument("--max-cutoff", type=int, default=6, choices=range(2, 7))
    args = parser.parse_args()
    tag = require_aws()
    result_path = args.v17_lane / "run/RESULT.json"
    artifact_dir = args.v17_lane / "run/artifacts"
    if digest(args.row_prelude) != EXPECTED_PRELUDE:
        fail(("row prelude hash mismatch", digest(args.row_prelude)))
    result = json.loads(result_path.read_text())
    if result.get("status") != "PASS-K00-FIRSTORDER-COKERNEL-V17-ENDPOINT":
        fail("V17 endpoint sentinel mismatch")
    if str(result.get("field")) != args.field or result.get("syz6_generators") != 66:
        fail("V17 field/syzygy sentinel mismatch")
    rows = parse_rows(args.row_prelude)
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    directions: dict[str, object] = {}
    matrices: list[dict[str, object]] = []
    for label in LOADS:
        endpoint = result.get("directions", {}).get(label, {})
        if endpoint.get("branch") != "LOCAL_NONZERO" or endpoint.get("local_class_zero") is not False:
            fail(("V18 requires a V17 locally nonzero branch", label, endpoint))
        image_path = artifact_dir / f"IMAGE_{label}.txt"
        target_path = artifact_dir / f"TARGET_{label}.txt"
        expected = endpoint.get("artifact_sha256", {})
        if digest(image_path) != expected.get(f"IMAGE_{label}.txt"):
            fail(("image hash mismatch", label))
        if digest(target_path) != expected.get(f"TARGET_{label}.txt"):
            fail(("target hash mismatch", label))
        image = parse_ideal(image_path)
        if len(image) != 66:
            fail(("six-row image generator count", label, len(image)))
        target = parse_poly(target_path.read_text())
        if not target or order(target) is None or order(target) < 2:
            fail(("target order sentinel", label, poly_summary(target)))
        generators = rows + image
        for cutoff in range(2, args.max_cutoff + 1):
            matrices.append(write_matrix(output, label, generators, target, cutoff))
        directions[label] = {
            "image_sha256": digest(image_path),
            "target_sha256": digest(target_path),
            "image_generators": len(image),
            "generator_summaries": [poly_summary(poly) for poly in generators],
            "target_summary": poly_summary(target),
        }
    audit = {
        "status": "PASS-K00-FILTERED-LOAD-V18-EMITTER",
        "registered_aws_lane": tag,
        "field": args.field,
        "characteristic": 0 if args.field == "Q" else 65521,
        "max_cutoff": args.max_cutoff,
        "preregistration_sha256": digest(PREREG),
        "v17_result_sha256": digest(result_path),
        "v17_evidence_status": result.get("status"),
        "row_prelude_sha256": digest(args.row_prelude),
        "row_summaries": [poly_summary(row) for row in rows],
        "directions": directions,
        "matrices": matrices,
        "scope": "SEPARATE_FILTERED_FIRST_LOAD_CLASSES_AT_NORMALIZED_K00_ONLY",
        "firewall": "NO_COUPLING_NO_LAMBDA19_NO_HONEST_SOURCE_REACHABILITY_NO_ARC_EXCLUSION",
    }
    audit_path = output / "SOURCE_AUDIT.json"
    audit_path.write_text(json.dumps(audit, sort_keys=True, indent=2) + "\n")
    print("K00_V18_SOURCE_AUDIT=PASS")
    print(json.dumps(audit, sort_keys=True))


if __name__ == "__main__":
    main()
