#!/usr/bin/env python3
"""Exact symbolic-C6 K00 quadratic-normal replay, AWS only."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TAILS = ROOT / "cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json"
ONEPARAM = ROOT / "xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-20260826.md"
PREREG = HERE / "PREREGISTRATION.md"
EXPECTED = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    ONEPARAM: "5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b",
    PREREG: "7b44649464c8c5f2fdd5d199ec5b949db61ab985eeb0efcee9aad7816634b466",
}
EXPECTED_ALL_TAILS = "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"
NAMES = [f"a{i}" for i in range(7)] + ["k10", "k6", "k2"]
WEIGHTS = [8 - i for i in range(7)] + [2, 6, 10]

# Polynomial keys are (C6 exponent,d0 exponent,...,d5 exponent).
Key = tuple[int, int, int, int, int, int, int]
Poly = dict[Key, Fraction]
ZERO_KEY: Key = (0, 0, 0, 0, 0, 0, 0)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only quadratic replay refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only quadratic replay refused non-Amazon host")
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


def scale(poly: Poly, scalar: Fraction) -> Poly:
    return clean({key: scalar * value for key, value in poly.items()})


def multiply(left: Poly, right: Poly) -> Poly:
    result: Poly = {}
    for akey, avalue in left.items():
        for bkey, bvalue in right.items():
            key = tuple(a + b for a, b in zip(akey, bkey))
            if sum(key[1:]) > 2:
                continue
            result[key] = result.get(key, Fraction(0)) + avalue * bvalue
    return clean(result)


def power(poly: Poly, exponent: int) -> Poly:
    result: Poly = {ZERO_KEY: Fraction(1)}
    base = poly
    value = exponent
    while value:
        if value & 1:
            result = multiply(result, base)
        value >>= 1
        if value:
            base = multiply(base, base)
    return result


def x_power(exponent: int, coefficient: Fraction = Fraction(1)) -> Poly:
    return {(exponent, 0, 0, 0, 0, 0, 0): coefficient}


def normal(index: int, coefficient: Fraction = Fraction(1)) -> Poly:
    key = [0] * 7
    key[1 + index] = 1
    return {tuple(key): coefficient}


def substitutions() -> list[Poly]:
    # C0,...,C6 in the preregistered transverse coordinates.
    return [
        add(x_power(4, Fraction(1, 256)), normal(0, Fraction(1, 256))),
        normal(1),
        add(x_power(3, Fraction(1, 16)), normal(2, Fraction(1, 16))),
        normal(3),
        add(x_power(2, Fraction(3, 8)), normal(4, Fraction(1, 8))),
        normal(5),
        x_power(1),
    ]


def normal_piece(poly: Poly, degree: int) -> Poly:
    return {key: value for key, value in poly.items() if sum(key[1:]) == degree}


def unloaded_tail(entries: list[list[object]], ell: int, images: list[Poly]) -> Poly:
    total: Poly = {}
    for raw_monomial, raw_coefficient in entries:
        monomial = [int(value) for value in raw_monomial]
        if len(monomial) != len(NAMES):
            fail(("monomial length", ell, monomial))
        if any(value < 0 for value in monomial):
            fail(("negative monomial exponent", ell, monomial))
        if sum(a * b for a, b in zip(monomial, WEIGHTS)) != 12 + ell:
            fail(("tail weight", ell, monomial))
        if sum(monomial[7:]) > 1 or any(value not in (0, 1) for value in monomial[7:]):
            fail(("tail load nonlinearity", ell, monomial))
        if any(monomial[7:]):
            continue
        term: Poly = {ZERO_KEY: Fraction(str(raw_coefficient))}
        for image, exponent in zip(images, monomial[:7]):
            if exponent:
                term = multiply(term, power(image, exponent))
        total = add(total, term)
    return total


def shift_x(poly: Poly, exponent: int) -> Poly:
    result: Poly = {}
    for key, value in poly.items():
        shifted = (key[0] + exponent, *key[1:])
        result[shifted] = value
    return result


def encode(poly: Poly) -> list[dict[str, object]]:
    rows = []
    for key, value in sorted(poly.items()):
        rows.append({
            "C6_power": key[0],
            "normal_exponents_d0_to_d5": list(key[1:]),
            "coefficient": str(value),
        })
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
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
    quadratics: dict[int, Poly] = {}
    for ell in range(1, 8):
        pulled = unloaded_tail(tails[str(ell)], ell, images)
        if normal_piece(pulled, 0):
            fail(("nonzero K00 constant", ell, encode(normal_piece(pulled, 0))))
        if normal_piece(pulled, 1):
            fail(("nonzero K00 linear normal", ell, encode(normal_piece(pulled, 1))))
        quadratics[ell] = normal_piece(pulled, 2)

    identity5 = add(
        quadratics[5],
        add(scale(shift_x(quadratics[1], 2), Fraction(3, 128)),
            scale(shift_x(quadratics[3], 1), Fraction(1, 8))),
    )
    identity6 = quadratics[6]
    identity7 = add(
        quadratics[7],
        add(scale(shift_x(quadratics[1], 3), Fraction(1, 512)),
            scale(shift_x(quadratics[3], 2), Fraction(1, 128))),
    )
    if identity5 or identity6 or identity7:
        fail({"Q5_residual": encode(identity5), "Q6": encode(identity6), "Q7_residual": encode(identity7)})

    q_payload = {f"Q{ell}": encode(quadratics[ell]) for ell in range(1, 8)}
    q_path = output / "quadratic_rows.json"
    q_path.write_text(json.dumps(q_payload, sort_keys=True, indent=2) + "\n")
    result = {
        "status": "PASS-K00-SYMBOLIC-QUADRATIC-REPLAY",
        "registered_aws_lane": tag,
        "tails_sha256": digest(TAILS),
        "canonical_all_tails_sha256": EXPECTED_ALL_TAILS,
        "oneparameter_sha256": digest(ONEPARAM),
        "preregistration_sha256": digest(PREREG),
        "constant_terms_zero": True,
        "linear_normal_terms_zero": True,
        "symbolic_C6": True,
        "Q5_syzygy": True,
        "Q6_zero": True,
        "Q7_syzygy": True,
        "quadratic_term_counts": {f"Q{ell}": len(quadratics[ell]) for ell in range(1, 8)},
        "quadratic_rows_sha256": digest(q_path),
        "scope": "PURE_QUADRATIC_NORMAL_REPLAY_ONLY_NO_CLOSURE_OR_JC2_VERDICT",
    }
    result_path = output / "RESULT.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("K00_QUADRATIC_SOURCE_HASHES=PASS")
    print("K00_QUADRATIC_CONSTANT_ZERO=PASS")
    print("K00_QUADRATIC_LINEAR_ZERO=PASS")
    print("K00_QUADRATIC_SYMBOLIC_C6=PASS")
    print("K00_QUADRATIC_Q5_SYZYGY=PASS")
    print("K00_QUADRATIC_Q6_ZERO=PASS")
    print("K00_QUADRATIC_Q7_SYZYGY=PASS")
    print("K00_QUADRATIC_ENDPOINT=PASS_REPLAY_ONLY")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
