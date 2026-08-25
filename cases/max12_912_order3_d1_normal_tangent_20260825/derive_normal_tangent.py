#!/usr/bin/env python3
"""Extract the exact normal Taylor terms at the D1 common-cubic cone.

This is an independent, AWS-only analysis companion.  It consumes the
already independently reconstructed ordinary Faber tails and substitutes

    f=(z^3+p*z+c)^3 + sum_{i=0}^5 x_i*z^i.

The deformation degree counts x_0,...,x_5 and k, while p,c have degree
zero.  Multiplication is truncated only *above* the requested deformation
degree, so every emitted homogeneous piece is exact over Q[p,c].
"""

from __future__ import annotations

import argparse
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

# Output variables are p,c,x0,x1,x2,x3,x4,x5,k.
NAMES = ("p", "c", "x0", "x1", "x2", "x3", "x4", "x5", "k")
ZERO = (0,) * len(NAMES)
DEFORMATION_INDICES = tuple(range(2, len(NAMES)))


class NormalTangentFailure(RuntimeError):
    pass


def require_aws() -> str:
    if platform.system() != "Linux":
        raise SystemExit("REFUSE_NON_LINUX")
    vendor_path = Path("/sys/class/dmi/id/sys_vendor")
    vendor = vendor_path.read_text().strip() if vendor_path.is_file() else ""
    if vendor != "Amazon EC2":
        raise SystemExit("REFUSE_NON_AWS_EC2")
    tag = os.environ.get("JC2_AWS_TAG", "")
    if not tag.startswith("max12_912_order3_d1_normal_tangent_"):
        raise SystemExit("REFUSE_UNREGISTERED_AWS_TAG")
    return tag


def load_source():
    got = sha256(SOURCE.read_bytes()).hexdigest()
    if got != SOURCE_SHA256:
        raise NormalTangentFailure(("source hash mismatch", got, SOURCE_SHA256))
    spec = importlib.util.spec_from_file_location("d1_normal_tangent_source", SOURCE)
    if spec is None or spec.loader is None:
        raise NormalTangentFailure("cannot load source")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def clean(poly):
    return {monomial: coefficient for monomial, coefficient in poly.items()
            if coefficient}


def add(left, right):
    out = dict(left)
    for monomial, coefficient in right.items():
        out[monomial] = out.get(monomial, Fraction(0)) + coefficient
    return clean(out)


def deformation_degree(monomial):
    return sum(monomial[index] for index in DEFORMATION_INDICES)


def multiply(left, right, maximum_degree):
    out = {}
    for lm, lv in left.items():
        for rm, rv in right.items():
            monomial = tuple(a + b for a, b in zip(lm, rm))
            if deformation_degree(monomial) > maximum_degree:
                continue
            out[monomial] = out.get(monomial, Fraction(0)) + lv * rv
    return clean(out)


def variable(index):
    monomial = list(ZERO)
    monomial[index] = 1
    return {tuple(monomial): Fraction(1)}


def monomial(pc_exponents, coefficient=1):
    value = list(ZERO)
    value[0], value[1] = pc_exponents
    return {tuple(value): Fraction(coefficient)}


def coefficient_images():
    p, c = variable(0), variable(1)
    xs = [variable(index) for index in range(2, 8)]
    # a_i = coefficient of z^i in (z^3+pz+c)^3 + E, E=sum x_i z^i.
    images = [
        add(monomial((0, 3)), xs[0]),
        add(monomial((1, 2), 3), xs[1]),
        add(monomial((2, 1), 3), xs[2]),
        add(add(monomial((3, 0)), monomial((0, 2), 3)), xs[3]),
        add(monomial((1, 1), 6), xs[4]),
        add(monomial((2, 0), 3), xs[5]),
        monomial((0, 1), 3),
        monomial((1, 0), 3),
        variable(8),
    ]
    # Keep these references live as an elementary sanity check.
    if not p or not c:
        raise NormalTangentFailure("variable construction")
    return images


def powers(images, source_tails, maximum_degree):
    maxima = [0] * len(images)
    for row in source_tails.values():
        for source_monomial in row:
            for index, exponent in enumerate(source_monomial):
                maxima[index] = max(maxima[index], exponent)
    table = []
    for image, maximum in zip(images, maxima):
        values = [{ZERO: Fraction(1)}]
        for _ in range(maximum):
            values.append(multiply(values[-1], image, maximum_degree))
        table.append(values)
    return table


def substitute(source_poly, power_table, maximum_degree):
    out = {}
    for source_monomial, scalar in source_poly.items():
        term = {ZERO: scalar}
        for index, exponent in enumerate(source_monomial):
            term = multiply(term, power_table[index][exponent], maximum_degree)
            if not term:
                break
        out = add(out, term)
    return clean(out)


def homogeneous(poly, degree):
    return {monomial: coefficient for monomial, coefficient in poly.items()
            if deformation_degree(monomial) == degree}


def canonical(poly):
    return [[list(monomial), coefficient.numerator, coefficient.denominator]
            for monomial, coefficient in sorted(poly.items())]


def poly_string(poly):
    terms = []
    for exponent, coefficient in sorted(poly.items(), reverse=True):
        factors = []
        for name, power in zip(NAMES, exponent):
            if power == 1:
                factors.append(name)
            elif power:
                factors.append(f"{name}^{power}")
        atom = "*".join(factors) or "1"
        if coefficient.denominator == 1:
            scalar = str(coefficient.numerator)
        else:
            scalar = f"({coefficient.numerator}/{coefficient.denominator})"
        terms.append(f"{scalar}*{atom}")
    return "+".join(terms).replace("+-", "-") or "0"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--maximum-degree", type=int, default=3)
    args = parser.parse_args()
    if args.maximum_degree < 2:
        raise SystemExit("maximum degree must be at least two")
    tag = require_aws()
    source = load_source()
    built = source.build()
    tails = built["tails"]
    images = coefficient_images()
    table = powers(images, tails, args.maximum_degree)
    transformed = {
        ell: substitute(tails[ell], table, args.maximum_degree)
        for ell in range(1, 9)
    }
    pieces = {
        ell: {degree: homogeneous(transformed[ell], degree)
              for degree in range(args.maximum_degree + 1)}
        for ell in range(1, 9)
    }
    for ell in range(1, 9):
        if pieces[ell][0] or pieces[ell][1]:
            raise NormalTangentFailure(("nonzero constant/linear tail", ell))
        if not pieces[ell][2]:
            raise NormalTangentFailure(("zero quadratic tail", ell))

    payload = {
        "aws_tag": tag,
        "source": str(SOURCE.relative_to(ROOT)),
        "source_sha256": SOURCE_SHA256,
        "variables": NAMES,
        "deformation_variables": NAMES[2:],
        "normal_substitution": {
            "f": "(z^3+p*z+c)^3+x0+x1*z+...+x5*z^5",
            "k": "k",
        },
        "maximum_deformation_degree": args.maximum_degree,
        "rows": {},
    }
    for ell in range(1, 9):
        payload["rows"][str(ell)] = {}
        for degree in range(args.maximum_degree + 1):
            piece = pieces[ell][degree]
            serial = canonical(piece)
            payload["rows"][str(ell)][str(degree)] = {
                "support": len(piece),
                "sha256": sha256(json.dumps(serial, separators=(",", ":")).encode()).hexdigest(),
                "polynomial": poly_string(piece),
            }
    canonical_payload = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    print(json.dumps(payload, sort_keys=True, indent=2))
    print("PASS-D1-NORMAL-TANGENT-EXTRACTION")
    print(f"payload_sha256={sha256(canonical_payload.encode()).hexdigest()}")


if __name__ == "__main__":
    main()
