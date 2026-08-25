#!/usr/bin/env python3
"""Exact general D1 normal initial system through Lambda-weight 20.

On the ordinary isotrivial chart write E=f-K^3=K*Q+R, with

  K=z^3+pz+c,
  Q=q2*z^2+q1*z+q0,
  R=r2*z^2+r1*z+r0.

This compiler applies Q -> L^6 Q, R -> L^9 R, kbar -> L^6 k and
extracts every ordinary Faber tail through L-weight 20.  It is AWS-only.
In ``--singular`` mode it emits the exact weight-15/18 initial ideal with
the full symbolic loads mu,nu; no component verdict is built in.
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

# p,c,q2,q1,q0,r2,r1,r0,k,L
NAMES = ("p", "c", "q2", "q1", "q0", "r2", "r1", "r0", "k", "L")
ZERO = (0,) * len(NAMES)
L_INDEX = 9
MAXIMUM_WEIGHT = 20


class GeneralLeadingFailure(RuntimeError):
    pass


def require_aws() -> str:
    if platform.system() != "Linux":
        raise SystemExit("REFUSE_NON_LINUX")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        raise SystemExit("REFUSE_NON_AWS_EC2")
    tag = os.environ.get("JC2_AWS_TAG", "")
    if not tag.startswith("max12_912_order3_d1_general_leading_"):
        raise SystemExit("REFUSE_UNREGISTERED_AWS_TAG")
    return tag


def load_source():
    got = sha256(SOURCE.read_bytes()).hexdigest()
    if got != SOURCE_SHA256:
        raise GeneralLeadingFailure(("source hash", got, SOURCE_SHA256))
    spec = importlib.util.spec_from_file_location("d1_general_leading_source", SOURCE)
    if spec is None or spec.loader is None:
        raise GeneralLeadingFailure("cannot load source")
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
    # Coefficients of K^3 + L^6*K*Q + L^9*R.
    return [
        add(add(monomial({1: 3}), monomial({1: 1, 4: 1, 9: 6})),
            monomial({7: 1, 9: 9})),
        add(add(monomial({0: 1, 1: 2}, 3),
                monomial({0: 1, 4: 1, 9: 6})),
            add(monomial({1: 1, 3: 1, 9: 6}),
                monomial({6: 1, 9: 9}))),
        add(add(monomial({0: 2, 1: 1}, 3),
                monomial({0: 1, 3: 1, 9: 6})),
            add(monomial({1: 1, 2: 1, 9: 6}),
                monomial({5: 1, 9: 9}))),
        add(add(monomial({0: 3}), monomial({1: 2}, 3)),
            add(monomial({4: 1, 9: 6}),
                monomial({0: 1, 2: 1, 9: 6}))),
        add(monomial({0: 1, 1: 1}, 6), monomial({3: 1, 9: 6})),
        add(monomial({0: 2}, 3), monomial({2: 1, 9: 6})),
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


def coefficient(poly, weight):
    out = {}
    for monomial_value, scalar in poly.items():
        if monomial_value[L_INDEX] != weight:
            continue
        target = list(monomial_value)
        target[L_INDEX] = 0
        out[tuple(target)] = scalar
    return clean(out)


def poly_string(poly):
    terms = []
    for exponent, scalar in sorted(poly.items(), reverse=True):
        factors = []
        for index, power in enumerate(exponent):
            if index == L_INDEX:
                continue
            if power == 1:
                factors.append(NAMES[index])
            elif power:
                factors.append(f"{NAMES[index]}^{power}")
        atom = "*".join(factors) or "1"
        number = (str(scalar.numerator) if scalar.denominator == 1 else
                  f"({scalar.numerator}/{scalar.denominator})")
        terms.append(f"{number}*{atom}")
    return "+".join(terms).replace("+-", "-") or "0"


def canonical(poly):
    return [[list(m), q.numerator, q.denominator]
            for m, q in sorted(poly.items())]


def singular_source(initial, tag, chart):
    variables = "p,c,k,mu,nu,q2,q1,q0,r2,r1,r0"
    if chart == "q2_nonzero":
        variables += ",v"
    lines = [
        'LIB "elim.lib";',
        f"ring R=0,({variables}),dp;",
        "option(redSB);",
        f'print("AWS_TAG={tag}");',
        f'print("SCOPE=GENERAL_WEIGHT_15_18_NORMAL_INITIAL_SYSTEM_{chart}");',
    ]
    equation_names = []
    for ell in range(1, 9):
        for weight in (15, 18):
            value = poly_string(initial[ell][weight])
            if weight == 15 and ell == 3:
                value = f"({value})-mu"
            if weight == 18 and ell == 6:
                value = f"({value})-nu"
            name = f"E{ell}_{weight}"
            equation_names.append(name)
            lines.append(f"poly {name}={value};")
    extra = []
    if chart == "q2_zero":
        extra.append("q2")
    elif chart == "q2_nonzero":
        # q2^2*q1 is an exact consequence of the global ideal.  Retaining
        # q1 explicitly makes this chart fail closed if source equations
        # change and keeps the localized basis small.
        extra.extend(("q1", "v*q2-1"))
    lines.extend([
        f"ideal I={','.join(equation_names + extra)};",
        'print("START_STANDARD_BASIS");',
        "ideal G=std(I);",
        'print("GENERATOR_COUNT="+string(size(G)));',
        'print("IS_UNIT="+string(reduce(1,G)==0));',
        'print("BASIS_BEGIN");',
        "G;",
        'print("BASIS_END");',
        'print("PASS_D1_GENERAL_LEADING_INITIAL_IDEAL");',
        "quit;",
    ])
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--singular", action="store_true")
    parser.add_argument("--chart", choices=("global", "q2_zero", "q2_nonzero"),
                        default="global")
    args = parser.parse_args()
    tag = require_aws()
    source = load_source()
    tails = source.build()["tails"]
    tables = power_tables(images(), tails)
    transformed = {ell: substitute(tails[ell], tables) for ell in range(1, 9)}
    initial = {
        ell: {weight: coefficient(transformed[ell], weight)
              for weight in (15, 18)}
        for ell in range(1, 9)
    }
    if args.singular:
        print(singular_source(initial, tag, args.chart), end="")
        return
    rows = {}
    for ell in range(1, 9):
        rows[str(ell)] = {}
        for weight in (15, 18):
            value = initial[ell][weight]
            serial = canonical(value)
            rows[str(ell)][str(weight)] = {
                "polynomial": poly_string(value),
                "support": len(value),
                "sha256": sha256(json.dumps(serial, separators=(",", ":")).encode()).hexdigest(),
            }
    payload = {
        "aws_tag": tag,
        "source_sha256": SOURCE_SHA256,
        "division": "E=L^6*K*Q+L^9*R",
        "Q": "q2*z^2+q1*z+q0",
        "R": "r2*z^2+r1*z+r0",
        "kbar": "L^6*k",
        "rows": rows,
        "no_other_nonzero_weight_at_most_20": all(
            not coefficient(transformed[ell], weight)
            for ell in range(1, 9)
            for weight in range(MAXIMUM_WEIGHT + 1)
            if weight not in (15, 18)
        ),
    }
    canonical_payload = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    print(json.dumps(payload, sort_keys=True, indent=2))
    print("PASS-D1-GENERAL-LEADING-EXTRACTION")
    print(f"payload_sha256={sha256(canonical_payload.encode()).hexdigest()}")


if __name__ == "__main__":
    main()
