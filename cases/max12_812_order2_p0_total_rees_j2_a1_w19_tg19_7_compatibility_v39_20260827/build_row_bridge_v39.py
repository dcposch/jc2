#!/usr/bin/env python3
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V37 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_graded_ladder_v37_20260827/solve_graded_ladder_v37.py"
V37_SHA = "ba034c8cebaa27c5630872b9cf06d152e4577170486ac34ad7f695ead871845b"
PRIMES = (65521, 65519)
SCOPE = "frozen Q and derived finite-field bridges for all 70 literal ordered-a1 rho-zero rows through grade19"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def canonical_bytes(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def encode_monomial(monomial) -> list[list[object]]:
    return [[name, exponent] for name, exponent in monomial]


def encode_q_polynomial(polynomial) -> dict[str, object]:
    return {
        "terms": [
            {"coefficient": [coefficient.numerator, coefficient.denominator],
             "monomial": encode_monomial(monomial)}
            for monomial, coefficient in sorted(polynomial.items())
        ]
    }


def modular_value(value: Fraction, prime: int) -> int:
    if value.denominator % prime == 0:
        fail(("bad bridge prime", prime, value))
    return value.numerator * pow(value.denominator, -1, prime) % prime


def encode_p_polynomial(polynomial, prime: int) -> dict[str, object]:
    terms = []
    for monomial, coefficient in sorted(polynomial.items()):
        residue = modular_value(coefficient, prime)
        if residue:
            terms.append({"coefficient": residue, "monomial": encode_monomial(monomial)})
    return {"characteristic": prime, "terms": terms}


def object_hash(value: object) -> str:
    return sha256(canonical_bytes(value)).hexdigest()


def load_v37():
    if digest(V37) != V37_SHA:
        fail("V37 compiler hash")
    spec = importlib.util.spec_from_file_location("v39_bridge_v37", V37)
    if spec is None or spec.loader is None:
        fail("V37 compiler import")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build_manifest() -> dict[str, object]:
    v37 = load_v37()
    _, nonzero_rows, raw_hashes, variables = v37.load_rows()
    by_name = {item["name"]: item["polynomial"] for item in nonzero_rows}
    names = [f"Tg{grade}_{row}" for grade in range(10, 20) for row in range(1, 8)]
    if sorted(raw_hashes) != sorted(names) or len(nonzero_rows) != 51 or len(variables) != 65:
        fail("source census")
    records = {}
    for name in names:
        grade_text, row_text = name[2:].split("_")
        polynomial = by_name.get(name, {})
        q_object = encode_q_polynomial(polynomial)
        p_objects = {str(prime): encode_p_polynomial(polynomial, prime) for prime in PRIMES}
        records[name] = {
            "grade": int(grade_text),
            "row": int(row_text),
            "q_file_sha256": raw_hashes[name],
            "q_rho0_sha256": object_hash(q_object),
            "q_term_count": len(polynomial),
            "p_shadow_sha256": {prime: object_hash(value) for prime, value in p_objects.items()},
            "p_shadow_term_count": {prime: len(value["terms"]) for prime, value in p_objects.items()},
        }
    return {
        "schema_version": 1,
        "v37_compiler_sha256": V37_SHA,
        "row_count_named": len(records),
        "row_count_nonzero": len(nonzero_rows),
        "variable_count": len(variables),
        "primes": list(PRIMES),
        "rows": records,
        "scope": SCOPE,
    }


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("output", type=Path)
    args = cli.parse_args()
    if args.output.exists():
        fail("refuse overwrite")
    value = build_manifest()
    args.output.write_text(json.dumps(value, sort_keys=True, indent=2) + "\n")
    print(f"ROW_BRIDGE_SHA256={digest(args.output)}")


if __name__ == "__main__":
    main()
