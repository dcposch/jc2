#!/usr/bin/env python3
"""Simultaneous common-denominator reconstruction over F_127."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path
import re


P = 127
NAMES = ("c", "d2", "d4", "x1", "x3", "x5", "inv")
TERM = re.compile(r"([+-]?)(\d*)(?:(v)(\d*))?(?:(s)(\d*))?")


def parse_term(term: str) -> tuple[int, int, int]:
    match = TERM.fullmatch(term)
    if match is None or term in ("", "+", "-"):
        raise ValueError(("term", term))
    sign, digits, has_v, v_digits, has_s, s_digits = match.groups()
    coefficient = int(digits) if digits else 1
    if sign == "-":
        coefficient = -coefficient
    v_degree = int(v_digits) if has_v and v_digits else (1 if has_v else 0)
    s_degree = int(s_digits) if has_s and s_digits else (1 if has_s else 0)
    if not has_v and not has_s and not digits:
        raise ValueError(("empty monomial", term))
    return coefficient % P, v_degree, s_degree


def parse_polynomial(source: str, order: int) -> list[list[int]]:
    sequences = [[0] * order for _ in range(190)]
    terms = re.findall(r"[+-]?[^+-]+", source)
    if not terms:
        raise ValueError("empty polynomial")
    seen: set[tuple[int, int]] = set()
    for term in terms:
        coefficient, v_degree, s_degree = parse_term(term)
        if not (0 <= v_degree < 190 and 0 <= s_degree < order):
            raise ValueError(("degree", term, v_degree, s_degree, order))
        key = (v_degree, s_degree)
        if key in seen:
            raise ValueError(("duplicate monomial", key))
        seen.add(key)
        sequences[v_degree][s_degree] = coefficient
    return sequences


def read_series(path: Path, expected_order: int) -> dict[str, list[list[int]]]:
    lines = path.read_text().splitlines()
    required = {
        f"order={expected_order}",
        "final_fail=0",
        f"moving_vdim={190 * expected_order}",
    }
    for item in required:
        if lines.count(item) != 1:
            raise ValueError((str(path), item, lines.count(item)))
    result: dict[str, list[list[int]]] = {}
    for name in NAMES:
        prefix = f"series_{name}="
        matches = [line[len(prefix) :] for line in lines if line.startswith(prefix)]
        if len(matches) != 1:
            raise ValueError((str(path), name, len(matches)))
        result[name] = parse_polynomial(matches[0], expected_order)
    return result


def flatten(data: dict[str, list[list[int]]]) -> list[list[int]]:
    return [sequence for name in NAMES for sequence in data[name]]


def prefix_equal(short: list[list[int]], long: list[list[int]]) -> bool:
    if len(short) != len(long):
        return False
    width = len(short[0])
    return all(a == b[:width] for a, b in zip(short, long, strict=True))


def solve_denominator(
    sequences: list[list[int]], sample_count: int, denominator_degree: int, numerator_degree: int
) -> tuple[list[int] | None, int, int]:
    """Solve D*A polynomial of degree <= numerator_degree, with D(0)=1."""
    d = denominator_degree
    pivots: dict[int, list[int]] = {}
    equation_count = 0
    for sequence in sequences:
        for n in range(numerator_degree + 1, sample_count):
            row = [sequence[n - j] if n >= j else 0 for j in range(1, d + 1)]
            row.append((-sequence[n]) % P)
            equation_count += 1
            for pivot in sorted(pivots):
                factor = row[pivot]
                if factor:
                    base = pivots[pivot]
                    row = [(x - factor * y) % P for x, y in zip(row, base, strict=True)]
            pivot = next((index for index, value in enumerate(row[:d]) if value), None)
            if pivot is None:
                if row[d]:
                    return None, len(pivots), equation_count
                continue
            inverse = pow(row[pivot], P - 2, P)
            row = [(inverse * value) % P for value in row]
            for old_pivot, old_row in list(pivots.items()):
                factor = old_row[pivot]
                if factor:
                    pivots[old_pivot] = [
                        (x - factor * y) % P for x, y in zip(old_row, row, strict=True)
                    ]
            pivots[pivot] = row
    if len(pivots) != d:
        return None, len(pivots), equation_count
    denominator = [1] + [0] * d
    for pivot, row in pivots.items():
        denominator[pivot + 1] = row[d]
    if not validate(sequences, sample_count, denominator, numerator_degree):
        raise AssertionError("internal solve/validate mismatch")
    return denominator, d, equation_count


def validate(
    sequences: list[list[int]], sample_count: int, denominator: list[int], numerator_degree: int
) -> bool:
    for sequence in sequences:
        for n in range(numerator_degree + 1, sample_count):
            value = 0
            for j, coefficient in enumerate(denominator):
                if n >= j:
                    value += coefficient * sequence[n - j]
            if value % P:
                return False
    return True


def find_minimal(
    sequences: list[list[int]], sample_count: int
) -> dict[str, object] | None:
    # Search by total numerator-plus-denominator degree. Require at least one
    # recurrence equation after the numerator for every sequence.
    for total in range(1, 2 * sample_count - 2):
        hits = []
        for d in range(1, min(sample_count - 1, total) + 1):
            m = total - d
            if not (0 <= m < sample_count - 1):
                continue
            denominator, rank, equations = solve_denominator(sequences, sample_count, d, m)
            if denominator is not None:
                hits.append(
                    {
                        "denominator_degree": d,
                        "numerator_degree": m,
                        "denominator": denominator,
                        "rank": rank,
                        "equation_count": equations,
                    }
                )
        if hits:
            return {"total_degree": total, "hits": hits}
    return None


def numerators(
    data: dict[str, list[list[int]]], denominator: list[int], numerator_degree: int
) -> dict[str, list[list[int]]]:
    output = {}
    for name in NAMES:
        by_v = []
        for sequence in data[name]:
            coefficients = []
            for n in range(numerator_degree + 1):
                value = sum(
                    denominator[j] * sequence[n - j]
                    for j in range(min(n, len(denominator) - 1) + 1)
                )
                coefficients.append(value % P)
            by_v.append(coefficients)
        output[name] = by_v
    return output


def synthetic_controls() -> None:
    denominator = [1, 2, 3]
    sequences = []
    for seed in range(1, 9):
        sequence = [seed, 2 * seed % P]
        for n in range(2, 32):
            sequence.append((-2 * sequence[n - 1] - 3 * sequence[n - 2]) % P)
        sequences.append(sequence)
    candidate, rank, _ = solve_denominator(sequences, 16, 2, 1)
    if candidate != denominator or rank != 2 or not validate(sequences, 32, candidate, 1):
        raise AssertionError(("synthetic positive", candidate, rank))
    corrupted = [row[:] for row in sequences]
    corrupted[0][23] = (corrupted[0][23] + 1) % P
    if validate(corrupted, 32, candidate, 1):
        raise AssertionError("synthetic negative not detected")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--order16", type=Path, required=True)
    parser.add_argument("--order32", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    synthetic_controls()
    data16 = read_series(args.order16, 16)
    data32 = read_series(args.order32, 32)
    seq16 = flatten(data16)
    seq32 = flatten(data32)
    if len(seq16) != 7 * 190 or not prefix_equal(seq16, seq32):
        raise AssertionError("order16/order32 prefix mismatch")
    corrupted = [row[:] for row in seq16]
    corrupted[0][0] = (corrupted[0][0] + 1) % P
    if prefix_equal(corrupted, seq32):
        raise AssertionError("prefix negative control not detected")

    fit16 = find_minimal(seq16, 16)
    holdout = []
    if fit16 is not None:
        for hit in fit16["hits"]:
            holdout.append(
                {
                    **hit,
                    "valid_through_order32": validate(
                        seq32, 32, hit["denominator"], hit["numerator_degree"]
                    ),
                }
            )
    fit32 = find_minimal(seq32, 32)
    selected = None
    source = None
    passing16 = [hit for hit in holdout if hit["valid_through_order32"]]
    if passing16:
        selected = passing16[0]
        source = "order16_fit_with_order32_holdout"
    elif fit32 is not None:
        selected = fit32["hits"][0]
        source = "order32_fit_unvalidated_beyond_order32"

    payload: dict[str, object] = {
        "status": "PASS",
        "scope": "simultaneous scalar-denominator recurrence; provisional until higher-order holdout and full mod-H substitution",
        "prime": P,
        "sequence_count": len(seq32),
        "order16_sha256": sha256(args.order16.read_bytes()).hexdigest(),
        "order32_sha256": sha256(args.order32.read_bytes()).hexdigest(),
        "prefix_match": True,
        "synthetic_positive": True,
        "synthetic_negative": True,
        "fit16": fit16,
        "fit16_order32_holdout": holdout,
        "fit32": fit32,
        "selected_source": source,
        "selected": selected,
    }
    if selected is not None:
        payload["selected_numerators"] = numerators(
            data32, selected["denominator"], selected["numerator_degree"]
        )
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print("Q8-P127-HENSEL-SIMULTANEOUS-COMMON-PADE")
    print("status=PASS")
    print(f"sequence_count={len(seq32)}")
    print("prefix_match=1")
    print(f"fit16_total={None if fit16 is None else fit16['total_degree']}")
    print(f"fit16_holdout_passes={sum(hit['valid_through_order32'] for hit in holdout)}")
    print(f"fit32_total={None if fit32 is None else fit32['total_degree']}")
    if selected is None:
        print("selected=NONE")
    else:
        print(
            "selected="
            + source
            + f" d={selected['denominator_degree']} m={selected['numerator_degree']}"
        )
        print("denominator=" + ",".join(map(str, selected["denominator"])))
    print(f"output_sha256={sha256(args.output.read_bytes()).hexdigest()}")


if __name__ == "__main__":
    main()

