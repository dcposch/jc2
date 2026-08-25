#!/usr/bin/env python3
"""AWS-only exact compiler for the remaining D1 double-root normal chart.

The chart is centred at

    K0=(z-1)^2*(z+2)=z^3-3*z+2,
    f=K0^3+K0*Q+R,

with completely general degree-at-most-two polynomials Q and R.  The source
tails are substituted without deformation-degree truncation.  The compiler
prints the exact rows and writes deterministic Singular inputs in two orders;
it does not run Singular and asserts no saturation verdict.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from functools import reduce
from hashlib import sha256
import importlib.util
import json
from math import gcd
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

NAMES = ("q2", "q1", "q0", "r2", "r1", "r0")
ZERO = (0,) * len(NAMES)


class DoubleRootCompileFailure(RuntimeError):
    pass


def require_aws() -> str:
    if platform.system() != "Linux":
        raise SystemExit("REFUSE_NON_LINUX")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        raise SystemExit("REFUSE_NON_AWS_EC2")
    tag = os.environ.get("JC2_AWS_TAG", "")
    if not tag.startswith("max12_912_order3_d1_double_root_exact_"):
        raise SystemExit("REFUSE_UNREGISTERED_AWS_TAG")
    return tag


def load_source():
    got = sha256(SOURCE.read_bytes()).hexdigest()
    if got != SOURCE_SHA256:
        raise DoubleRootCompileFailure(("source hash", got, SOURCE_SHA256))
    spec = importlib.util.spec_from_file_location("d1_double_root_source", SOURCE)
    if spec is None or spec.loader is None:
        raise DoubleRootCompileFailure("cannot load charged source")
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


def multiply(left, right):
    out = {}
    for lm, lv in left.items():
        for rm, rv in right.items():
            monomial = tuple(a + b for a, b in zip(lm, rm))
            out[monomial] = out.get(monomial, Fraction(0)) + lv * rv
    return clean(out)


def constant(value):
    value = Fraction(value)
    return {} if not value else {ZERO: value}


def variable(index, coefficient=1):
    monomial = list(ZERO)
    monomial[index] = 1
    return {tuple(monomial): Fraction(coefficient)}


def linear(value, terms):
    out = constant(value)
    for index, coefficient in terms:
        out = add(out, variable(index, coefficient))
    return out


def coefficient_images():
    # Coefficients a0,...,a7 of K0^3+K0*Q+R, followed by kbar=0.
    return [
        linear(8, ((2, 2), (5, 1))),
        linear(-36, ((2, -3), (1, 2), (4, 1))),
        linear(54, ((1, -3), (0, 2), (3, 1))),
        linear(-15, ((2, 1), (0, -3))),
        linear(-36, ((1, 1),)),
        linear(27, ((0, 1),)),
        constant(6),
        constant(-9),
        {},
    ]


def powers(images, source_tails):
    maxima = [0] * len(images)
    for row in source_tails.values():
        for source_monomial in row:
            for index, exponent in enumerate(source_monomial):
                maxima[index] = max(maxima[index], exponent)
    table = []
    for image, maximum in zip(images, maxima):
        entries = [constant(1)]
        for _ in range(maximum):
            entries.append(multiply(entries[-1], image))
        table.append(entries)
    return table


def substitute(source_poly, table):
    out = {}
    for source_monomial, scalar in source_poly.items():
        term = constant(scalar)
        for index, exponent in enumerate(source_monomial):
            term = multiply(term, table[index][exponent])
            if not term:
                break
        out = add(out, term)
    return clean(out)


def lcm(left, right):
    return abs(left * right) // gcd(left, right)


def primitive_integer(poly):
    denominator = reduce(lcm, (value.denominator for value in poly.values()), 1)
    values = {monomial: int(value * denominator)
              for monomial, value in poly.items()}
    content = reduce(gcd, (abs(value) for value in values.values()), 0) or 1
    values = {monomial: value // content for monomial, value in values.items()}
    first = next(value for _, value in sorted(values.items(), reverse=True) if value)
    if first < 0:
        values = {monomial: -value for monomial, value in values.items()}
    return clean(values)


def poly_string(poly):
    chunks = []
    for exponents, coefficient in sorted(poly.items(), reverse=True):
        factors = []
        for name, exponent in zip(NAMES, exponents):
            if exponent == 1:
                factors.append(name)
            elif exponent:
                factors.append(f"{name}^{exponent}")
        atom = "*".join(factors) or "1"
        chunks.append(f"{coefficient}*{atom}")
    return "+".join(chunks).replace("+-", "-") or "0"


def canonical(poly):
    return [[list(monomial), int(coefficient)]
            for monomial, coefficient in sorted(poly.items())]


def singular_source(rows, order):
    ideals = ",\n  ".join(poly_string(rows[ell]) for ell in range(1, 9))
    return f"""// Exact D1 double-root exceptional normal ideal.
// Generated only from the charged independent ordinary source.
ring R=0,({','.join(NAMES)}),{order};
option(redSB);
ideal I=
  {ideals};
print(\"ORDER={order}\");
print(\"INPUT_SIZE=\"+string(size(I)));
ideal G=std(I);
print(\"BASIS_SIZE=\"+string(size(G)));
print(\"VDIM=\"+string(vdim(G)));
print(\"BASIS_BEGIN\");
G;
print(\"BASIS_END\");
quit;
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()
    tag = require_aws()
    source = load_source()
    tails = source.build()["tails"]
    table = powers(coefficient_images(), tails)
    rows = {ell: primitive_integer(substitute(tails[ell], table))
            for ell in range(1, 9)}
    if any(not rows[ell] for ell in rows):
        raise DoubleRootCompileFailure("zero exact row")

    output = Path(args.output_dir)
    output.mkdir(parents=True, exist_ok=True)
    for order in ("dp", "lp"):
        (output / f"double_root_{order}.sing").write_text(
            singular_source(rows, order), encoding="utf-8")

    payload = {
        "aws_tag": tag,
        "charged_source_sha256": SOURCE_SHA256,
        "centre": {
            "K0": "(z-1)^2*(z+2)=z^3-3*z+2",
            "p": -3,
            "c": 2,
            "Delta": 0,
        },
        "normal_coordinates": {
            "Q": "q2*z^2+q1*z+q0",
            "R": "r2*z^2+r1*z+r0",
            "f": "K0^3+K0*Q+R",
            "coverage": "all six normal directions; no slice",
        },
        "rows": {},
    }
    for ell in range(1, 9):
        serial = canonical(rows[ell])
        payload["rows"][str(ell)] = {
            "support": len(rows[ell]),
            "degree": max(sum(monomial) for monomial in rows[ell]),
            "sha256": sha256(json.dumps(serial, separators=(",", ":")).encode()).hexdigest(),
            "polynomial": poly_string(rows[ell]),
        }
    for path in sorted(output.iterdir()):
        payload.setdefault("outputs", {})[path.name] = sha256(path.read_bytes()).hexdigest()
    canonical_payload = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    print(json.dumps(payload, sort_keys=True, indent=2))
    print("PASS-D1-DOUBLE-ROOT-EXACT-COMPILER")
    print(f"payload_sha256={sha256(canonical_payload.encode()).hexdigest()}")


if __name__ == "__main__":
    main()
