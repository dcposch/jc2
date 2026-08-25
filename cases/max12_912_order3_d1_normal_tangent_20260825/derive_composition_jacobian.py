#!/usr/bin/env python3
"""Exact transverse Jacobian along the cubic-composition locus (AWS only).

Write K=z^3+pz+c and

  f = K^3 + B*K + A
      + K*(u2*z^2+u1*z) + v2*z^2+v1*z.

The four u/v variables are transverse to the exact composition locus.  This
script extracts the coefficient of transverse degree at most one from every
ordinary Faber tail, checks the composition rows, and factors every 4x4
minor of the five non-multiple-of-three rows r1,r2,r4,r5,r7.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import itertools
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

# p,c,B,A,u2,u1,v2,v1,k
NAMES = ("p", "c", "B", "A", "u2", "u1", "v2", "v1", "k")
ZERO = (0,) * len(NAMES)
TRANSVERSE = (4, 5, 6, 7)
NONMULTIPLE_ROWS = (1, 2, 4, 5, 7)


class CompositionJacobianFailure(RuntimeError):
    pass


def require_aws() -> str:
    if platform.system() != "Linux":
        raise SystemExit("REFUSE_NON_LINUX")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        raise SystemExit("REFUSE_NON_AWS_EC2")
    tag = os.environ.get("JC2_AWS_TAG", "")
    if not tag.startswith("max12_912_order3_d1_composition_jacobian_"):
        raise SystemExit("REFUSE_UNREGISTERED_AWS_TAG")
    return tag


def load_source():
    got = sha256(SOURCE.read_bytes()).hexdigest()
    if got != SOURCE_SHA256:
        raise CompositionJacobianFailure(("source hash", got, SOURCE_SHA256))
    spec = importlib.util.spec_from_file_location("d1_composition_jac_source", SOURCE)
    if spec is None or spec.loader is None:
        raise CompositionJacobianFailure("cannot load source")
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


def tdegree(monomial):
    return sum(monomial[index] for index in TRANSVERSE)


def multiply(left, right):
    out = {}
    for lm, lv in left.items():
        for rm, rv in right.items():
            monomial = tuple(a + b for a, b in zip(lm, rm))
            if tdegree(monomial) > 1:
                continue
            out[monomial] = out.get(monomial, Fraction(0)) + lv * rv
    return clean(out)


def monomial(exponents, coefficient=1):
    value = list(ZERO)
    for index, exponent in exponents.items():
        value[index] = exponent
    return {tuple(value): Fraction(coefficient)}


def variable(index):
    return monomial({index: 1})


def images():
    # Start with the common-cubic coefficients, then add B*K+A and the four
    # exact transverse terms displayed in the module docstring.
    return [
        add(add(monomial({1: 3}), monomial({1: 1, 2: 1})), variable(3)),
        add(add(monomial({0: 1, 1: 2}, 3), monomial({0: 1, 2: 1})),
            add(monomial({1: 1, 5: 1}), variable(7))),
        add(add(monomial({0: 2, 1: 1}, 3), monomial({0: 1, 5: 1})),
            add(monomial({1: 1, 4: 1}), variable(6))),
        add(add(monomial({0: 3}), monomial({1: 2}, 3)),
            add(variable(2), monomial({0: 1, 4: 1}))),
        add(monomial({0: 1, 1: 1}, 6), variable(5)),
        add(monomial({0: 2}, 3), variable(4)),
        monomial({1: 1}, 3),
        monomial({0: 1}, 3),
        variable(8),
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


def base_part(poly):
    return {m: q for m, q in poly.items() if tdegree(m) == 0}


def derivative_part(poly, transverse_index):
    out = {}
    for m, q in poly.items():
        if m[transverse_index] != 1 or tdegree(m) != 1:
            continue
        target = list(m)
        target[transverse_index] = 0
        out[tuple(target)] = q
    return clean(out)


def scale(scalar, poly):
    scalar = Fraction(scalar)
    return clean({m: scalar * q for m, q in poly.items()})


def determinant(matrix):
    out = {}
    for permutation in itertools.permutations(range(len(matrix))):
        inversions = sum(permutation[i] > permutation[j]
                         for i in range(len(permutation))
                         for j in range(i + 1, len(permutation)))
        term = {ZERO: Fraction(-1 if inversions % 2 else 1)}
        for row, column in enumerate(permutation):
            term = multiply(term, matrix[row][column])
        out = add(out, term)
    return clean(out)


def poly_string(poly):
    terms = []
    base_indices = (0, 1, 2, 3, 8)
    for exponent, coefficient in sorted(poly.items(), reverse=True):
        factors = []
        for index in base_indices:
            power = exponent[index]
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


def expected_composition_rows():
    rows = {ell: {} for ell in range(1, 9)}
    rows[3] = add(monomial({2: 1, 3: 1}, Fraction(4, 9)),
                  monomial({3: 1, 8: 1}, Fraction(2, 3)))
    rows[6] = add(
        add(monomial({3: 2}, Fraction(2, 9)),
            monomial({2: 2, 8: 1}, Fraction(-1, 9))),
        monomial({2: 3}, Fraction(-4, 81)),
    )
    return rows


def singular_source(matrix, minors, tag):
    lines = [
        "ring R=0,(p,c,B,A,k),dp;",
        f'print("AWS_TAG={tag}");',
        'print("SOURCE=EXACT_ORDINARY_FABER_TAILS");',
    ]
    for row_index, ell in enumerate(NONMULTIPLE_ROWS):
        for column_index, name in enumerate(("u2", "u1", "v2", "v1")):
            lines.append(
                f"poly J_r{ell}_{name}={poly_string(matrix[row_index][column_index])};"
            )
    for name, value in minors.items():
        lines.extend([
            f"poly {name}={poly_string(value)};",
            f'print("FACTOR_{name}_BEGIN");',
            f"factorize({name});",
            f'print("FACTOR_{name}_END");',
        ])
    lines.extend([
        'print("PASS_D1_COMPOSITION_JACOBIAN_FACTORIZATION");',
        "quit;",
    ])
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--singular", action="store_true")
    args = parser.parse_args()
    tag = require_aws()
    source = load_source()
    tails = source.build()["tails"]
    tables = power_tables(images(), tails)
    transformed = {ell: substitute(tails[ell], tables) for ell in range(1, 9)}

    base = {ell: base_part(transformed[ell]) for ell in range(1, 9)}
    expected = expected_composition_rows()
    for ell in range(1, 9):
        if base[ell] != expected[ell]:
            raise CompositionJacobianFailure(("composition row", ell,
                                              poly_string(base[ell]),
                                              poly_string(expected[ell])))

    matrix = [
        [derivative_part(transformed[ell], index)
         for index in TRANSVERSE]
        for ell in NONMULTIPLE_ROWS
    ]
    minors = {}
    for omitted in NONMULTIPLE_ROWS:
        kept_indices = [index for index, ell in enumerate(NONMULTIPLE_ROWS)
                        if ell != omitted]
        submatrix = [matrix[index] for index in kept_indices]
        minors[f"omit_r{omitted}"] = determinant(submatrix)

    if args.singular:
        print(singular_source(matrix, minors, tag), end="")
        return

    payload = {
        "aws_tag": tag,
        "source_sha256": SOURCE_SHA256,
        "coordinates": {
            "K": "z^3+p*z+c",
            "f": "K^3+B*K+A+K*(u2*z^2+u1*z)+v2*z^2+v1*z",
            "transverse": ["u2", "u1", "v2", "v1"],
        },
        "composition_rows": {str(ell): poly_string(base[ell])
                             for ell in range(1, 9)},
        "jacobian_rows": list(NONMULTIPLE_ROWS),
        "jacobian_columns": [NAMES[index] for index in TRANSVERSE],
        "jacobian": [[poly_string(value) for value in row]
                     for row in matrix],
        "four_by_four_minors_expanded": {
            name: poly_string(value) for name, value in minors.items()
        },
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    print(json.dumps(payload, sort_keys=True, indent=2))
    print("PASS-D1-COMPOSITION-TRANSVERSE-JACOBIAN")
    print(f"payload_sha256={sha256(canonical.encode()).hexdigest()}")


if __name__ == "__main__":
    main()
