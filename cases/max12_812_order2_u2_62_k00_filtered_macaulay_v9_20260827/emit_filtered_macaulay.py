#!/usr/bin/env python3
"""Emit exact cumulative K00 Macaulay matrices from the frozen tails, AWS only."""

from __future__ import annotations

import argparse
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
import json
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TAILS = ROOT / "cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json"
ONEPARAM = ROOT / "xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-20260826.md"
QUADRATIC = ROOT / "cases/max12_812_order2_u2_62_k00_normal_quadratic_v6_20260827/RESULT.md"
V8_PREREG = ROOT / "cases/max12_812_order2_u2_62_k00_unloaded_membership_v8_20260827/PREREGISTRATION.md"
PREREG = HERE / "PREREGISTRATION.md"
EXPECTED = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    ONEPARAM: "5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b",
    QUADRATIC: "9b95409aafdd10346ca1095047bd1ea5ebbdd6ca23e2b5a7e29323e01e8e5909",
    V8_PREREG: "fe085951e6a5a9e23f33a6af37d0ab1861221831a4c22a026f06428d55d54ea0",
    PREREG: "dce7ac60e820f0a11eb2cc531b6d2def85e5f86c7d6209cd63a4efb979afca30",
}
EXPECTED_ALL_TAILS = "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"
NAMES = [f"a{i}" for i in range(7)] + ["k10", "k6", "k2"]
WEIGHTS = [8 - i for i in range(7)] + [2, 6, 10]
NVAR = 6
Key = tuple[int, int, int, int, int, int]
Poly = dict[Key, Fraction]
ZERO: Key = (0, 0, 0, 0, 0, 0)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only filtered Macaulay emitter refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only filtered Macaulay emitter refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def clean(poly: Poly) -> Poly:
    return {key: value for key, value in poly.items() if value}


def add(left: Poly, right: Poly) -> Poly:
    result = dict(left)
    for key, value in right.items():
        result[key] = result.get(key, Fraction(0)) + value
    return clean(result)


def multiply(left: Poly, right: Poly) -> Poly:
    result: Poly = {}
    for akey, avalue in left.items():
        for bkey, bvalue in right.items():
            key = tuple(a + b for a, b in zip(akey, bkey))
            result[key] = result.get(key, Fraction(0)) + avalue * bvalue
    return clean(result)


def power(poly: Poly, exponent: int) -> Poly:
    result: Poly = {ZERO: Fraction(1)}
    base = poly
    value = exponent
    while value:
        if value & 1:
            result = multiply(result, base)
        value >>= 1
        if value:
            base = multiply(base, base)
    return result


def constant(value: Fraction) -> Poly:
    return {ZERO: value} if value else {}


def normal(index: int, value: Fraction = Fraction(1)) -> Poly:
    key = [0] * NVAR
    key[index] = 1
    return {tuple(key): value}


def substitutions() -> list[Poly]:
    return [
        add(constant(Fraction(1, 256)), normal(0, Fraction(1, 256))),
        normal(1),
        add(constant(Fraction(1, 16)), normal(2, Fraction(1, 16))),
        normal(3),
        add(constant(Fraction(3, 8)), normal(4, Fraction(1, 8))),
        normal(5),
        constant(Fraction(1)),
    ]


def tail_sector(entries: list[list[object]], ell: int, images: list[Poly], sector: int | None) -> Poly:
    total: Poly = {}
    for raw_monomial, raw_coefficient in entries:
        monomial = [int(value) for value in raw_monomial]
        if len(monomial) != len(NAMES) or any(value < 0 for value in monomial):
            fail(("ill-typed monomial", ell, monomial))
        if sum(a * b for a, b in zip(monomial, WEIGHTS)) != 12 + ell:
            fail(("tail weight", ell, monomial))
        load = monomial[7:]
        if sum(load) > 1 or any(value not in (0, 1) for value in load):
            fail(("tail load nonlinearity", ell, monomial))
        wanted = [0, 0, 0]
        if sector is not None:
            wanted[sector] = 1
        if load != wanted:
            continue
        term = constant(Fraction(str(raw_coefficient)))
        for image, exponent in zip(images, monomial[:7]):
            if exponent:
                term = multiply(term, power(image, exponent))
        total = add(total, term)
    return total


def degree_piece(poly: Poly, degree: int) -> Poly:
    return {key: value for key, value in poly.items() if sum(key) == degree}


@lru_cache(maxsize=None)
def monomials(degree: int, variables: int = NVAR) -> tuple[Key, ...]:
    def build(left: int, count: int, prefix: tuple[int, ...]):
        if count == 1:
            yield prefix + (left,)
            return
        for exponent in range(left + 1):
            yield from build(left - exponent, count - 1, prefix + (exponent,))
    return tuple(build(degree, variables, ()))


def shift(poly: Poly, monomial: Key) -> Poly:
    return {tuple(a + b for a, b in zip(key, monomial)): value for key, value in poly.items()}


def fraction_text(value: Fraction) -> tuple[str, str]:
    return str(value.numerator), str(value.denominator)


def write_matrix(path: Path, rows: dict[int, Poly], cutoff: int) -> dict[str, object]:
    row_keys = tuple(key for degree in range(2, cutoff + 1) for key in monomials(degree))
    row_index = {key: index for index, key in enumerate(row_keys)}
    columns: list[tuple[int, int, Key]] = []
    for multiplier_degree in range(cutoff - 1):
        for ell in range(1, 7):
            for mono in monomials(multiplier_degree):
                columns.append((ell, multiplier_degree, mono))
    entries: dict[tuple[int, int], Fraction] = {}
    for column, (ell, multiplier_degree, mono) in enumerate(columns):
        for row_degree in range(2, cutoff - multiplier_degree + 1):
            for key, value in shift(degree_piece(rows[ell], row_degree), mono).items():
                if sum(key) <= cutoff:
                    ridx = row_index[key]
                    entries[(ridx, column)] = entries.get((ridx, column), Fraction(0)) + value
    rhs_column = len(columns)
    for degree in range(2, cutoff + 1):
        for key, value in degree_piece(rows[7], degree).items():
            entries[(row_index[key], rhs_column)] = value
    entries = {key: value for key, value in entries.items() if value}
    with path.open("w") as handle:
        handle.write(f"{len(row_keys)} {len(columns)} {len(entries)} {cutoff}\n")
        for (row, column), value in sorted(entries.items()):
            numerator, denominator = fraction_text(value)
            handle.write(f"{row} {column} {numerator} {denominator}\n")
    descriptor = {
        "cutoff": cutoff,
        "rows": len(row_keys),
        "columns": len(columns),
        "nonzero_entries_including_rhs": len(entries),
        "matrix_sha256": digest(path),
        "column_order": "multiplier_degree_then_row1_to6_then_lex_normal_monomial",
        "row_order": "normal_degree2_to_cutoff_then_lex_normal_monomial",
    }
    return descriptor


def encode_poly(poly: Poly) -> list[dict[str, object]]:
    return [
        {"normal_exponents_d0_to_d5": list(key), "coefficient": str(value)}
        for key, value in sorted(poly.items())
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--max-cutoff", type=int, default=7, choices=range(2, 8))
    args = parser.parse_args()
    tag = require_aws()
    for path, expected in EXPECTED.items():
        if expected == "TO_BE_FROZEN" or digest(path) != expected:
            fail(("frozen source mismatch", str(path), digest(path), expected))
    tails = json.loads(TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")
    if sorted(tails) != [str(i) for i in range(1, 8)]:
        fail("tail key mismatch")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    images = substitutions()
    rows = {ell: tail_sector(tails[str(ell)], ell, images, None) for ell in range(1, 8)}
    for ell, row in rows.items():
        if degree_piece(row, 0) or degree_piece(row, 1):
            fail(("K00 unloaded constant/linear sentinel", ell, encode_poly(degree_piece(row, 0)), encode_poly(degree_piece(row, 1))))
    descriptors = []
    for cutoff in range(2, args.max_cutoff + 1):
        descriptors.append(write_matrix(output / f"macaulay_D{cutoff}.tsv", rows, cutoff))
    sectors = {"k10": 0, "k6": 1, "k2": 2}
    stencil: dict[str, object] = {}
    for name, sector in sectors.items():
        by_row: dict[str, object] = {}
        for ell in range(1, 8):
            poly = tail_sector(tails[str(ell)], ell, images, sector)
            degrees = sorted({sum(key) for key in poly})
            by_row[str(ell)] = {
                "minimum_normal_degree": degrees[0] if degrees else None,
                "degree_term_counts": {str(degree): len(degree_piece(poly, degree)) for degree in degrees},
                "constant_zero": not bool(degree_piece(poly, 0)),
            }
        stencil[name] = by_row
    stencil_path = output / "load_normal_stencil.json"
    stencil_path.write_text(json.dumps(stencil, sort_keys=True, indent=2) + "\n")
    audit = {
        "status": "PASS-K00-FILTERED-MACAULAY-EMITTER",
        "registered_aws_lane": tag,
        "characteristic_source": 0,
        "max_cutoff": args.max_cutoff,
        "tails_sha256": digest(TAILS),
        "canonical_all_tails_sha256": EXPECTED_ALL_TAILS,
        "oneparameter_sha256": digest(ONEPARAM),
        "quadratic_result_sha256": digest(QUADRATIC),
        "v8_preregistration_sha256": digest(V8_PREREG),
        "preregistration_sha256": digest(PREREG),
        "constant_terms_zero": True,
        "linear_terms_zero": True,
        "matrices": descriptors,
        "load_normal_stencil_sha256": digest(stencil_path),
        "scope": "K00_UNLOADED_FILTERED_MACAULAY_THROUGH_D7_AND_LOAD_VALUATION_STENCIL_ONLY",
    }
    audit_path = output / "SOURCE_AUDIT.json"
    audit_path.write_text(json.dumps(audit, sort_keys=True, indent=2) + "\n")
    print("K00_MACAULAY_SOURCE_HASHES=PASS")
    print("K00_MACAULAY_CONSTANT_LINEAR_ZERO=PASS")
    print(json.dumps(audit, sort_keys=True))


if __name__ == "__main__":
    main()
