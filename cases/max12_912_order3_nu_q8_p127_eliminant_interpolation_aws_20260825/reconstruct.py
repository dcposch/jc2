#!/usr/bin/env python3
"""Interpolate the Q8 fixed-fibre eliminants on F_127^*.

Parser/interpolator only: all Gröbner bases and factorizations are consumed
from completed pure-Singular AWS lanes.
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re


P = 127
N = P - 1
DEGREE = 190
DEGREE_DROP_VALUES = {39, 56, 125}
VDIM_BY_EXCEPTION = {39: 190, 56: 189, 125: 189}


def scalar(text: str, key: str) -> str:
    match = re.search(rf"(?m)^{re.escape(key)}=(.*)$", text)
    if not match:
        raise AssertionError(f"missing {key}")
    return match.group(1).strip()


def parse_poly(text: str) -> list[int]:
    compact = text.replace(" ", "")
    terms = compact.replace("-", "+-").split("+")
    out: dict[int, int] = {}
    for term in terms:
        if not term:
            continue
        if "v" not in term:
            coefficient = int(term)
            exponent = 0
        else:
            match = re.fullmatch(r"([+-]?(?:\d+)?)\*?v(?:\^(\d+))?", term)
            if not match:
                raise AssertionError((text, term))
            raw_coefficient, raw_exponent = match.groups()
            if raw_coefficient in (None, "", "+"):
                coefficient = 1
            elif raw_coefficient == "-":
                coefficient = -1
            else:
                coefficient = int(raw_coefficient)
            exponent = int(raw_exponent or 1)
        out[exponent] = (out.get(exponent, 0) + coefficient) % P
    degree = max(out, default=0)
    result = [0] * (degree + 1)
    for exponent, coefficient in out.items():
        result[exponent] = coefficient
    return result


def multiply(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        if not a:
            continue
        for j, b in enumerate(right):
            if b:
                out[i + j] = (out[i + j] + a * b) % P
    return out


def lane_for(roots: list[Path], w_value: int) -> Path:
    candidates: list[Path] = []
    matcher = re.compile(rf"(?:^|_)w0*{w_value}(?:_|$)")
    for root in roots:
        if not root.is_dir():
            continue
        for lane in root.iterdir():
            if lane.is_dir() and matcher.search(lane.name):
                meta = lane / "run.meta"
                if meta.is_file():
                    meta_text = meta.read_text()
                    if (
                        re.search(rf"(?m)^w_value={w_value}$", meta_text)
                        and re.search(rf"(?m)^prime={P}$", meta_text)
                    ):
                        candidates.append(lane)
    if not candidates:
        raise AssertionError(f"missing w={w_value}")
    # Prefer the original 20-lane custody root when it contains this value;
    # otherwise use the lexicographically first exact replay.
    candidates.sort(key=lambda path: ("pure-singular-fixed" not in str(path), str(path)))
    return candidates[0]


def fibre_polynomial(lane: Path, w_value: int) -> tuple[list[int], list[int]]:
    result_path = lane / "result.out"
    meta_path = lane / "run.meta"
    result = result_path.read_text()
    meta = meta_path.read_text()
    assert scalar(meta, "rc") == "0"
    assert int(scalar(meta, "prime")) == P
    assert int(scalar(meta, "w_value")) == w_value
    assert scalar(meta, "engine") == "std"
    assert scalar(result, "fibre_dim") == "0", (w_value, lane, "dim")
    reported_vdim = int(scalar(result, "fibre_vdim"))
    reported_degree = int(scalar(result, "v_eliminant_degree"))
    expected_degree = DEGREE - 1 if w_value in DEGREE_DROP_VALUES else DEGREE
    expected_vdim = VDIM_BY_EXCEPTION.get(w_value, DEGREE)
    assert reported_degree == expected_degree, (w_value, lane, "degree", reported_degree)
    assert reported_vdim == expected_vdim, (w_value, lane, "vdim", reported_vdim)
    assert scalar(result, "v_eliminant_squarefree_gcd_degree") == "0", (
        w_value, lane, "squarefree"
    )
    factors = re.findall(r"(?m)^\s+_\[\d+\]=(.*)$", result)
    assert len(factors) == int(scalar(result, "rational_factor_entries"))
    product = [1]
    degrees = []
    for factor in factors:
        parsed = parse_poly(factor)
        assert parsed[-1] == 1
        degrees.append(len(parsed) - 1)
        product = multiply(product, parsed)
    assert len(product) == reported_degree + 1
    assert product[-1] == 1
    assert sum(degrees) == reported_degree
    return product, sorted(degrees)


def primitive_generator() -> int:
    prime_divisors = (2, 3, 7)
    for candidate in range(2, P):
        if all(pow(candidate, N // q, P) != 1 for q in prime_divisors):
            return candidate
    raise AssertionError("no generator")


def interpolate(xs: list[int], ys: list[int]) -> list[int]:
    """Return the degree < len(xs) polynomial through the given points."""
    assert len(xs) == len(ys) and len(set(xs)) == len(xs)
    divided = [value % P for value in ys]
    for width in range(1, len(xs)):
        for index in range(len(xs) - 1, width - 1, -1):
            denominator = (xs[index] - xs[index - width]) % P
            divided[index] = (
                (divided[index] - divided[index - 1]) * pow(denominator, -1, P)
            ) % P
    polynomial = [divided[-1]]
    for index in range(len(xs) - 2, -1, -1):
        enlarged = [0] * (len(polynomial) + 1)
        for degree, coefficient in enumerate(polynomial):
            enlarged[degree] = (enlarged[degree] - xs[index] * coefficient) % P
            enlarged[degree + 1] = (enlarged[degree + 1] + coefficient) % P
        enlarged[0] = (enlarged[0] + divided[index]) % P
        polynomial = enlarged
    return polynomial


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("roots", type=Path, nargs="+")
    args = parser.parse_args()
    roots = [path.resolve() for path in args.roots]

    fibres: dict[int, list[int]] = {}
    partitions: dict[int, list[int]] = {}
    lanes: dict[int, str] = {}
    for w_value in range(1, P):
        lane = lane_for(roots, w_value)
        polynomial, degrees = fibre_polynomial(lane, w_value)
        fibres[w_value] = polynomial
        partitions[w_value] = degrees
        lanes[w_value] = str(lane)

    generator = primitive_generator()
    good_values = sorted(w for w, polynomial in fibres.items() if len(polynomial) == DEGREE + 1)
    bad_values = sorted(set(fibres) - set(good_values))
    assert len(good_values) == 123, (len(good_values), bad_values)
    assert bad_values == sorted(DEGREE_DROP_VALUES), bad_values

    # coeffs[v_degree][w_exponent], the unique degree <123 interpolant on
    # the full-degree fibres.  This is a candidate representative only.
    coeffs = []
    for v_degree in range(DEGREE + 1):
        coeffs.append(interpolate(
            good_values, [fibres[w][v_degree] for w in good_values]
        ))

    for w_value in good_values:
        expected = fibres[w_value]
        reconstructed = []
        for v_degree in range(DEGREE + 1):
            value = sum(
                coefficient * pow(w_value, exponent, P)
                for exponent, coefficient in enumerate(coeffs[v_degree])
            ) % P
            reconstructed.append(value)
        assert reconstructed == expected, w_value

    support = {
        degree: [[exponent, coefficient] for exponent, coefficient in enumerate(row) if coefficient]
        for degree, row in enumerate(coeffs)
    }
    support_counts = Counter(len(entries) for entries in support.values())
    payload_bytes = bytes(value for row in coeffs for value in row)
    proper_25 = sorted({sum(partitions[25][i] for i in range(len(partitions[25])) if mask >> i & 1)
                        for mask in range(1, (1 << len(partitions[25])) - 1)})
    proper_47 = sorted({sum(partitions[47][i] for i in range(len(partitions[47])) if mask >> i & 1)
                        for mask in range(1, (1 << len(partitions[47])) - 1)})
    payload = {
        "status": "PASS",
        "scope": "unique degree<123 coefficient interpolation on the 123 full-degree F_127 fibres only",
        "prime": P,
        "primitive_generator": generator,
        "fibre_count": len(fibres),
        "full_degree_fibre_count": len(good_values),
        "degree_drop_values": bad_values,
        "degree_v": DEGREE,
        "coefficient_table_sha256": hashlib.sha256(payload_bytes).hexdigest(),
        "support_count_histogram": {str(k): v for k, v in sorted(support_counts.items())},
        "maximum_support_count": max(support_counts),
        "nonzero_support": {str(k): v for k, v in support.items()},
        "partition_w25": partitions[25],
        "partition_w47": partitions[47],
        "proper_subset_sums_w25": proper_25,
        "proper_subset_sums_w47": proper_47,
        "proper_subset_sum_intersection": sorted(set(proper_25) & set(proper_47)),
        "lane_w25": lanes[25],
        "lane_w47": lanes[47],
        "disclosure": "interpolation does not bound the unreduced generic w-degree, identify denominator factors, or prove flat specialization",
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
