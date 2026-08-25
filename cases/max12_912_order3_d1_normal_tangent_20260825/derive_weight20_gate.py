#!/usr/bin/env python3
"""Exact weighted initial D1 gate through Lambda-weight 20 (AWS only).

The registered cubic-composition scaling is

  B=L^6*b, A=L^9*a, kbar=L^6*k,
  u2=L^8*U2, u1=L^8*U1, v2=L^11*V2, v1=L^11*V1.

Here E=B*K+A+K*(u2*z^2+u1*z)+v2*z^2+v1*z.  All arithmetic is
exact over Q; only terms of L-degree above 20 are discarded.
"""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = (ROOT / "cases" /
          "max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825" /
          "independent_reconstruct.py")
SOURCE_SHA256 = "67343b569db54f61f4a9e56e4262c0bf4fa781323a1287addbaf4fff93844623"

# p,c,b,a,U2,U1,V2,V1,k,L
NAMES = ("p", "c", "b", "a", "U2", "U1", "V2", "V1", "k", "L")
ZERO = (0,) * len(NAMES)
L_INDEX = 9
MAXIMUM_WEIGHT = 20


class WeightGateFailure(RuntimeError):
    pass


def require_aws() -> str:
    if platform.system() != "Linux":
        raise SystemExit("REFUSE_NON_LINUX")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        raise SystemExit("REFUSE_NON_AWS_EC2")
    tag = os.environ.get("JC2_AWS_TAG", "")
    if not tag.startswith("max12_912_order3_d1_weight20_"):
        raise SystemExit("REFUSE_UNREGISTERED_AWS_TAG")
    return tag


def load_source():
    got = sha256(SOURCE.read_bytes()).hexdigest()
    if got != SOURCE_SHA256:
        raise WeightGateFailure(("source hash", got, SOURCE_SHA256))
    spec = importlib.util.spec_from_file_location("d1_weight20_source", SOURCE)
    if spec is None or spec.loader is None:
        raise WeightGateFailure("cannot load source")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def clean(poly):
    return {m: q for m, q in poly.items() if q}


def add(left, right):
    out = dict(left)
    for m, q in right.items():
        out[m] = out.get(m, Fraction(0)) + q
    return clean(out)


def multiply(left, right):
    out = {}
    for lm, lv in left.items():
        for rm, rv in right.items():
            monomial = tuple(a + b for a, b in zip(lm, rm))
            if monomial[L_INDEX] > MAXIMUM_WEIGHT:
                continue
            out[monomial] = out.get(monomial, Fraction(0)) + lv * rv
    return clean(out)


def monomial(exponents, coefficient=1):
    value = list(ZERO)
    for index, exponent in exponents.items():
        value[index] = exponent
    return {tuple(value): Fraction(coefficient)}


def images():
    # Direct coefficients of K^3+B*K+A+K*(u2*z^2+u1*z)+v2*z^2+v1*z.
    return [
        add(add(monomial({1: 3}), monomial({1: 1, 2: 1, 9: 6})),
            monomial({3: 1, 9: 9})),
        add(add(monomial({0: 1, 1: 2}, 3),
                monomial({0: 1, 2: 1, 9: 6})),
            add(monomial({1: 1, 5: 1, 9: 8}),
                monomial({7: 1, 9: 11}))),
        add(add(monomial({0: 2, 1: 1}, 3),
                monomial({0: 1, 5: 1, 9: 8})),
            add(monomial({1: 1, 4: 1, 9: 8}),
                monomial({6: 1, 9: 11}))),
        add(add(monomial({0: 3}), monomial({1: 2}, 3)),
            add(monomial({2: 1, 9: 6}),
                monomial({0: 1, 4: 1, 9: 8}))),
        add(monomial({0: 1, 1: 1}, 6), monomial({5: 1, 9: 8})),
        add(monomial({0: 2}, 3), monomial({4: 1, 9: 8})),
        monomial({1: 1}, 3),
        monomial({0: 1}, 3),
        monomial({8: 1, 9: 6}),
    ]


def power_tables(coefficient_images, tails):
    maxima = [0] * len(coefficient_images)
    for row in tails.values():
        for source_monomial in row:
            for index, exponent in enumerate(source_monomial):
                maxima[index] = max(maxima[index], exponent)
    tables = []
    for image, maximum in zip(coefficient_images, maxima):
        table = [{ZERO: Fraction(1)}]
        for _ in range(maximum):
            table.append(multiply(table[-1], image))
        tables.append(table)
    return tables


def substitute(source_poly, tables):
    out = {}
    for source_monomial, scalar in source_poly.items():
        term = {ZERO: scalar}
        for index, exponent in enumerate(source_monomial):
            term = multiply(term, tables[index][exponent])
        out = add(out, term)
    return clean(out)


def weight_coefficient(poly, weight):
    out = {}
    for monomial_value, coefficient in poly.items():
        if monomial_value[L_INDEX] != weight:
            continue
        target = list(monomial_value)
        target[L_INDEX] = 0
        out[tuple(target)] = coefficient
    return clean(out)


def poly_string(poly):
    terms = []
    for exponent, coefficient in sorted(poly.items(), reverse=True):
        factors = []
        for index, power in enumerate(exponent):
            if index == L_INDEX:
                continue
            if power == 1:
                factors.append(NAMES[index])
            elif power:
                factors.append(f"{NAMES[index]}^{power}")
        atom = "*".join(factors) or "1"
        scalar = (str(coefficient.numerator)
                  if coefficient.denominator == 1 else
                  f"({coefficient.numerator}/{coefficient.denominator})")
        terms.append(f"{scalar}*{atom}")
    return "+".join(terms).replace("+-", "-") or "0"


def canonical(poly):
    return [[list(m), q.numerator, q.denominator]
            for m, q in sorted(poly.items())]


def main() -> None:
    tag = require_aws()
    source = load_source()
    tails = source.build()["tails"]
    tables = power_tables(images(), tails)
    transformed = {ell: substitute(tails[ell], tables) for ell in range(1, 9)}
    rows = {}
    for ell in range(1, 9):
        rows[str(ell)] = {}
        for weight in range(MAXIMUM_WEIGHT + 1):
            coefficient = weight_coefficient(transformed[ell], weight)
            if coefficient:
                serial = canonical(coefficient)
                rows[str(ell)][str(weight)] = {
                    "polynomial": poly_string(coefficient),
                    "support": len(coefficient),
                    "sha256": sha256(json.dumps(serial, separators=(",", ":")).encode()).hexdigest(),
                }
    payload = {
        "aws_tag": tag,
        "source_sha256": SOURCE_SHA256,
        "scaling": {
            "B": 6, "A": 9, "kbar": 6,
            "u2": 8, "u1": 8, "v2": 11, "v1": 11,
        },
        "maximum_L_weight": MAXIMUM_WEIGHT,
        "rows": rows,
    }
    canonical_payload = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    print(json.dumps(payload, sort_keys=True, indent=2))
    print("PASS-D1-WEIGHT20-EXACT-EXTRACTION")
    print(f"payload_sha256={sha256(canonical_payload.encode()).hexdigest()}")


if __name__ == "__main__":
    main()
