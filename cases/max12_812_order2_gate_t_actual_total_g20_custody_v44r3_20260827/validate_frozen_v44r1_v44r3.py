#!/usr/bin/env python3
"""Run the pinned V44R2 validator with a nonrecursive canonical-row parser."""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASE = ROOT / "cases/max12_812_order2_gate_t_actual_total_g20_custody_v44r2_20260827/validate_frozen_v44r1_v44r2.py"
BASE_SHA256 = "be70d8e8083ab652b6914b26d9f8b97671d4967a0e7ecdf0e4bb1231cf97e8d2"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def parse_serialized(path: Path):
    text = path.read_text().strip()
    if text == "0":
        return {}
    polynomial = {}
    for raw_term in text.split("+"):
        factors = raw_term.split("*")
        raw_coefficient = factors.pop(0)
        if raw_coefficient.startswith("(") and raw_coefficient.endswith(")"):
            raw_coefficient = raw_coefficient[1:-1]
        coefficient = Fraction(raw_coefficient)
        if not coefficient:
            raise RuntimeError(("serialized zero coefficient", raw_term))
        powers = {}
        for factor in factors:
            if "^" in factor:
                name, raw_exponent = factor.rsplit("^", 1)
                exponent = int(raw_exponent)
            else:
                name, exponent = factor, 1
            if not name or exponent <= 0:
                raise RuntimeError(("serialized factor", factor))
            powers[name] = powers.get(name, 0) + exponent
        monomial = tuple(sorted(powers.items()))
        if monomial in polynomial:
            raise RuntimeError(("duplicate serialized monomial", monomial))
        polynomial[monomial] = coefficient
    return polynomial


def main() -> None:
    if digest(BASE) != BASE_SHA256:
        raise RuntimeError(("V44R2 validator pin", digest(BASE), BASE_SHA256))
    source = BASE.read_text()
    if source.count("polynomial = parser.parse(path)") != 1:
        raise RuntimeError("V44R2 parse call multiplicity")
    source = source.replace("polynomial = parser.parse(path)", "polynomial = parse_serialized(path)")
    source = source.replace("V44R2", "V44R3")
    source = source.replace(
        '"host": platform.node(),',
        '"host": platform.node(),\n'
        '        "validator_sha256": digest(Path(__file__)),\n'
        '        "base_validator_sha256": "' + BASE_SHA256 + '",',
        1,
    )
    namespace = {
        "__file__": str(Path(__file__).resolve()),
        "__name__": "v44r3_transformed_validator",
        "parse_serialized": parse_serialized,
    }
    exec(compile(source, str(BASE), "exec"), namespace)
    namespace["main"]()


if __name__ == "__main__":
    main()

