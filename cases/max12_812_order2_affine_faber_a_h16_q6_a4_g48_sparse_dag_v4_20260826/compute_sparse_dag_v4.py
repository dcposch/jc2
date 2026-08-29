#!/usr/bin/env python3
"""AWS-only coefficient-DAG extraction of the H16 grade-48 odd functional."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
import os
from pathlib import Path
import platform
import time
from typing import Iterable


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TAILS = ROOT / "cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json"
TAILS_SHA = "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848"
TAILS_CANONICAL_SHA = "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"
MAX_GRADE = 48
SUPPORT_CAP = 2_000_000

ABS_VARS = (
    "J", "K2", "K6", "K10", "S0", "S1", "R0", "R1",
    "Y", "X", "a", "lambda", "M", "E",
)
ABS_INDEX = {name: index for index, name in enumerate(ABS_VARS)}
ABS_VALUATIONS = (57, 42, 42, 42, 12, 12, 12, 12, 6, 6, 4, 16, 0, 0)

JET_VARS = (
    *(f"a{i}" for i in range(7)), "p", *(f"e{i}" for i in range(1, 7)),
    "m", *(f"m{i}" for i in range(1, 5)),
    *(f"x{i}" for i in range(5)), *(f"y{i}" for i in range(5)),
    *(f"r1{i}" for i in range(5)), *(f"r0{i}" for i in range(5)),
    *(f"s1{i}" for i in range(5)), *(f"s0{i}" for i in range(5)),
    *(f"kk{i}" for i in range(7)),
    *(f"d6{i}" for i in range(5)), *(f"d2{i}" for i in range(5)),
)
JET_INDEX = {name: index for index, name in enumerate(JET_VARS)}

DenseMonomial = tuple[int, ...]
SparseMonomial = tuple[tuple[int, int], ...]
Coefficient = Fraction | int
DensePoly = dict[DenseMonomial, Coefficient]
JetPoly = dict[SparseMonomial, Coefficient]
Series = tuple[JetPoly, ...]


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only sparse-DAG client refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only sparse-DAG client refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


class Field:
    def __init__(self, characteristic: int):
        self.p = characteristic

    def value(self, item: object) -> Coefficient:
        q = item if isinstance(item, Fraction) else Fraction(str(item))
        if self.p == 0:
            return q
        return (q.numerator % self.p) * pow(q.denominator % self.p, -1, self.p) % self.p

    def add(self, left: Coefficient, right: Coefficient) -> Coefficient:
        value = left + right
        return value if self.p == 0 else value % self.p

    def mul(self, left: Coefficient, right: Coefficient) -> Coefficient:
        value = left * right
        return value if self.p == 0 else value % self.p

    def neg(self, value: Coefficient) -> Coefficient:
        return -value if self.p == 0 else (-value) % self.p

    def text(self, value: Coefficient) -> str:
        return str(value)


def dense_const(field: Field, value: object) -> DensePoly:
    coefficient = field.value(value)
    return {} if coefficient == 0 else {(0,) * len(ABS_VARS): coefficient}


def dense_var(field: Field, name: str) -> DensePoly:
    exponent = [0] * len(ABS_VARS)
    exponent[ABS_INDEX[name]] = 1
    return {tuple(exponent): field.value(1)}


def dense_add(field: Field, *items: DensePoly) -> DensePoly:
    result: DensePoly = {}
    for item in items:
        for monomial, coefficient in item.items():
            value = field.add(result.get(monomial, field.value(0)), coefficient)
            if value == 0:
                result.pop(monomial, None)
            else:
                result[monomial] = value
    return result


def dense_scale(field: Field, poly: DensePoly, scalar: object) -> DensePoly:
    value = field.value(scalar)
    if value == 0:
        return {}
    return {monomial: field.mul(value, coefficient) for monomial, coefficient in poly.items()}


def dense_mul(field: Field, left: DensePoly, right: DensePoly) -> DensePoly:
    if not left or not right:
        return {}
    result: DensePoly = {}
    for ml, cl in left.items():
        for mr, cr in right.items():
            monomial = tuple(a + b for a, b in zip(ml, mr))
            value = field.add(result.get(monomial, field.value(0)), field.mul(cl, cr))
            if value == 0:
                result.pop(monomial, None)
            else:
                result[monomial] = value
    if len(result) > SUPPORT_CAP:
        fail(("abstract support cap exceeded", len(result)))
    return result


def dense_pow(field: Field, poly: DensePoly, exponent: int) -> DensePoly:
    result = dense_const(field, 1)
    base = poly
    power = exponent
    while power:
        if power & 1:
            result = dense_mul(field, result, base)
        power //= 2
        if power:
            base = dense_mul(field, base, base)
    return result


def dense_eval(field: Field, poly: DensePoly, values: dict[str, object]) -> Coefficient:
    result = field.value(0)
    converted = [field.value(values.get(name, 0)) for name in ABS_VARS]
    for monomial, coefficient in poly.items():
        term = coefficient
        for value, exponent in zip(converted, monomial):
            if exponent:
                term = field.mul(term, pow(value, exponent) if field.p == 0 else pow(value, exponent, field.p))
        result = field.add(result, term)
    return result


def merge_sparse(left: SparseMonomial, right: SparseMonomial) -> SparseMonomial:
    values: dict[int, int] = dict(left)
    for index, exponent in right:
        values[index] = values.get(index, 0) + exponent
    return tuple(sorted((index, exponent) for index, exponent in values.items() if exponent))


def jet_const(field: Field, value: object) -> JetPoly:
    coefficient = field.value(value)
    return {} if coefficient == 0 else {(): coefficient}


def jet_var(field: Field, name: str) -> JetPoly:
    return {((JET_INDEX[name], 1),): field.value(1)}


def jet_add(field: Field, *items: JetPoly) -> JetPoly:
    result: JetPoly = {}
    for item in items:
        for monomial, coefficient in item.items():
            value = field.add(result.get(monomial, field.value(0)), coefficient)
            if value == 0:
                result.pop(monomial, None)
            else:
                result[monomial] = value
    return result


def jet_scale(field: Field, poly: JetPoly, scalar: object) -> JetPoly:
    value = field.value(scalar)
    if value == 0:
        return {}
    return {monomial: field.mul(value, coefficient) for monomial, coefficient in poly.items()}


def jet_mul(field: Field, left: JetPoly, right: JetPoly) -> JetPoly:
    if not left or not right:
        return {}
    result: JetPoly = {}
    for ml, cl in left.items():
        for mr, cr in right.items():
            monomial = merge_sparse(ml, mr)
            value = field.add(result.get(monomial, field.value(0)), field.mul(cl, cr))
            if value == 0:
                result.pop(monomial, None)
            else:
                result[monomial] = value
    if len(result) > SUPPORT_CAP:
        fail(("jet support cap exceeded", len(result)))
    return result


def jet_eval(field: Field, poly: JetPoly, values: dict[str, object]) -> Coefficient:
    converted = [field.value(values.get(name, 0)) for name in JET_VARS]
    result = field.value(0)
    for monomial, coefficient in poly.items():
        term = coefficient
        for index, exponent in monomial:
            value = converted[index]
            term = field.mul(term, pow(value, exponent) if field.p == 0 else pow(value, exponent, field.p))
        result = field.add(result, term)
    return result


def zero_series() -> Series:
    return tuple({} for _ in range(MAX_GRADE + 1))


def series_from_terms(field: Field, terms: Iterable[tuple[int, JetPoly]]) -> Series:
    result = list(zero_series())
    for grade, coefficient in terms:
        if grade <= MAX_GRADE:
            result[grade] = jet_add(field, result[grade], coefficient)
    return tuple(result)


def series_add(field: Field, *items: Series) -> Series:
    return tuple(jet_add(field, *(item[grade] for item in items)) for grade in range(MAX_GRADE + 1))


def series_scale(field: Field, item: Series, scalar: object) -> Series:
    return tuple(jet_scale(field, coefficient, scalar) for coefficient in item)


def series_mul(field: Field, left: Series, right: Series) -> Series:
    result = list(zero_series())
    left_support = [(grade, poly) for grade, poly in enumerate(left) if poly]
    right_support = [(grade, poly) for grade, poly in enumerate(right) if poly]
    for gl, pl in left_support:
        for gr, pr in right_support:
            grade = gl + gr
            if grade > MAX_GRADE:
                break
            result[grade] = jet_add(field, result[grade], jet_mul(field, pl, pr))
    return tuple(result)


def scalar_series_mul(field: Field, left: tuple[Coefficient, ...], right: tuple[Coefficient, ...]) -> tuple[Coefficient, ...]:
    result = [field.value(0)] * (MAX_GRADE + 1)
    for i, a in enumerate(left):
        if a == 0:
            continue
        for j, b in enumerate(right[: MAX_GRADE + 1 - i]):
            if b:
                result[i + j] = field.add(result[i + j], field.mul(a, b))
    return tuple(result)


def scalar_series_add(field: Field, *items: tuple[Coefficient, ...]) -> tuple[Coefficient, ...]:
    return tuple(field.value(sum(item[grade] for item in items)) for grade in range(MAX_GRADE + 1)) if field.p == 0 else tuple(sum(item[grade] for item in items) % field.p for grade in range(MAX_GRADE + 1))


def scalar_series_scale(field: Field, item: tuple[Coefficient, ...], scalar: object) -> tuple[Coefficient, ...]:
    value = field.value(scalar)
    return tuple(field.mul(value, coefficient) for coefficient in item)


def scalar_series_pow(field: Field, item: tuple[Coefficient, ...], exponent: int) -> tuple[Coefficient, ...]:
    one = [field.value(0)] * (MAX_GRADE + 1)
    one[0] = field.value(1)
    result = tuple(one)
    base = item
    power = exponent
    while power:
        if power & 1:
            result = scalar_series_mul(field, result, base)
        power //= 2
        if power:
            base = scalar_series_mul(field, base, base)
    return result


def source_series(field: Field) -> dict[str, Series]:
    def named(start: int, names: Iterable[str]) -> Series:
        return series_from_terms(field, ((start + i, jet_var(field, name)) for i, name in enumerate(names)))

    a = named(4, (f"a{i}" for i in range(7)))
    e = series_from_terms(field, [(0, jet_var(field, "p")), *((i, jet_var(field, f"e{i}")) for i in range(1, 7))])
    m = series_from_terms(field, [(0, jet_var(field, "m")), *((i, jet_var(field, f"m{i}")) for i in range(1, 5))])
    x = named(6, (f"x{i}" for i in range(5)))
    y = named(6, (f"y{i}" for i in range(5)))
    r1 = named(12, (f"r1{i}" for i in range(5)))
    r0 = named(12, (f"r0{i}" for i in range(5)))
    s1 = named(12, (f"s1{i}" for i in range(5)))
    s0 = named(12, (f"s0{i}" for i in range(5)))
    kk = named(0, (f"kk{i}" for i in range(7)))
    d6 = named(2, (f"d6{i}" for i in range(5)))
    d2 = named(2, (f"d2{i}" for i in range(5)))
    e2 = series_mul(field, e, e)
    e4 = series_mul(field, e2, e2)
    k10 = series_from_terms(field, ((42 + grade, poly) for grade, poly in enumerate(kk) if poly))
    k6_inner = series_add(field, series_scale(field, series_mul(field, kk, e2), Fraction(15, 32)), d6)
    k2_inner = series_add(field, series_scale(field, series_mul(field, kk, e4), Fraction(15, 256)), d2)
    k6 = series_from_terms(field, ((42 + grade, poly) for grade, poly in enumerate(k6_inner) if poly))
    k2 = series_from_terms(field, ((42 + grade, poly) for grade, poly in enumerate(k2_inner) if poly))
    lam = series_from_terms(field, ((16, jet_const(field, 1)),))
    return {
        "J": zero_series(), "K2": k2, "K6": k6, "K10": k10,
        "S0": s0, "S1": s1, "R0": r0, "R1": r1,
        "Y": y, "X": x, "a": a, "lambda": lam, "M": m, "E": e,
    }


def build_abstract(field: Field, tails: dict[str, object]) -> tuple[DensePoly, dict[str, object]]:
    variables = {name: dense_var(field, name) for name in ABS_VARS}
    a, e, m = variables["a"], variables["E"], variables["M"]
    x, y = variables["X"], variables["Y"]
    r1, r0, s1, s0 = variables["R1"], variables["R0"], variables["S1"], variables["S0"]
    lam = variables["lambda"]
    a2 = dense_mul(field, a, a)
    qp = dense_add(field, e, dense_scale(field, a2, -6))
    qc = dense_add(
        field,
        dense_scale(field, dense_mul(field, a, dense_add(field, dense_scale(field, a2, 4), dense_scale(field, e, -1))), 2),
        x, r1,
    )
    qr = dense_add(
        field,
        dense_mul(field, a2, dense_add(field, e, dense_scale(field, a2, -3))),
        r0,
        dense_scale(field, dense_mul(field, a, dense_add(field, x, r1)), -1),
    )
    n3 = dense_mul(field, lam, m)
    n2 = dense_mul(field, lam, dense_mul(field, a, m))
    n1 = dense_mul(field, lam, dense_add(field, dense_mul(field, dense_add(field, e, dense_scale(field, a2, -5)), m), y, s1))
    n0 = dense_mul(
        field, lam,
        dense_add(
            field,
            dense_scale(field, dense_mul(field, dense_mul(field, a, dense_add(field, e, dense_scale(field, a2, -3))), m), -1),
            dense_scale(field, dense_mul(field, a, y), -1),
            dense_scale(field, dense_mul(field, m, x), Fraction(1, 2)),
            s0,
            dense_scale(field, dense_mul(field, a, s1), -1),
        ),
    )
    factors = (
        dense_add(field, dense_mul(field, qr, qr), n0),
        dense_add(field, dense_scale(field, dense_mul(field, qc, qr), 2), n1),
        dense_add(field, dense_mul(field, qc, qc), dense_scale(field, dense_mul(field, qp, qr), 2), n2),
        dense_add(field, dense_scale(field, dense_mul(field, qp, qc), 2), n3),
        dense_add(field, dense_mul(field, qp, qp), dense_scale(field, qr, 2)),
        dense_scale(field, qc, 2), dense_scale(field, qp, 2),
        variables["K10"], variables["K6"], variables["K2"],
    )
    power_cache: dict[tuple[int, int], DensePoly] = {}
    term_cache: dict[tuple[int, ...], DensePoly] = {}

    def factor_power(index: int, exponent: int) -> DensePoly:
        key = (index, exponent)
        if key not in power_cache:
            power_cache[key] = dense_pow(field, factors[index], exponent)
        return power_cache[key]

    def tail_term(exponents: tuple[int, ...]) -> DensePoly:
        if exponents not in term_cache:
            term = dense_const(field, 1)
            for index, exponent in enumerate(exponents):
                if exponent:
                    term = dense_mul(field, term, factor_power(index, exponent))
            term_cache[exponents] = term
        return term_cache[exponents]

    def row(number: int) -> DensePoly:
        result: DensePoly = {}
        entries = tails[str(number)]
        for offset, (raw_exponents, raw_coefficient) in enumerate(entries, 1):
            exponents = tuple(int(value) for value in raw_exponents)
            result = dense_add(field, result, dense_scale(field, tail_term(exponents), raw_coefficient))
            if offset % 20 == 0 or offset == len(entries):
                print(f"SPARSE_DAG_ROW_PROGRESS={number}:{offset}/{len(entries)}:support={len(result)}", flush=True)
        return result

    p1, p3, p7 = row(1), row(3), row(7)
    functional = dense_add(
        field,
        p7,
        dense_scale(field, dense_mul(field, dense_mul(field, e, e), p3), Fraction(-1, 32)),
        dense_scale(field, dense_mul(field, dense_mul(field, dense_mul(field, e, e), e), p1), Fraction(1, 64)),
        dense_scale(field, variables["J"], Fraction(-1, 4)),
    )
    metrics = {
        "row_supports": {"1": len(p1), "3": len(p3), "7": len(p7)},
        "abstract_functional_support": len(functional),
        "factor_power_cache_entries": len(power_cache),
        "tail_term_cache_entries": len(term_cache),
    }
    return functional, metrics


def raw_scalar_functional(field: Field, tails: dict[str, object], values: dict[str, object]) -> Coefficient:
    def v(name: str) -> Coefficient:
        return field.value(values.get(name, 0))
    a, e, m = v("a"), v("E"), v("M")
    x, y, r1, r0, s1, s0, lam = (v(name) for name in ("X", "Y", "R1", "R0", "S1", "S0", "lambda"))
    add, mul = field.add, field.mul
    def scale(value: Coefficient, scalar: object) -> Coefficient:
        return mul(value, field.value(scalar))
    a2 = mul(a, a)
    qp = add(e, scale(a2, -6))
    qc = add(add(scale(mul(a, add(scale(a2, 4), scale(e, -1))), 2), x), r1)
    qr = add(add(mul(a2, add(e, scale(a2, -3))), r0), scale(mul(a, add(x, r1)), -1))
    n3 = mul(lam, m)
    n2 = mul(lam, mul(a, m))
    n1 = mul(lam, add(add(mul(add(e, scale(a2, -5)), m), y), s1))
    n0 = mul(lam, add(add(add(add(scale(mul(mul(a, add(e, scale(a2, -3))), m), -1), scale(mul(a, y), -1)), scale(mul(m, x), Fraction(1, 2))), s0), scale(mul(a, s1), -1)))
    factors = (
        add(mul(qr, qr), n0), add(scale(mul(qc, qr), 2), n1),
        add(add(mul(qc, qc), scale(mul(qp, qr), 2)), n2),
        add(scale(mul(qp, qc), 2), n3), add(mul(qp, qp), scale(qr, 2)),
        scale(qc, 2), scale(qp, 2), v("K10"), v("K6"), v("K2"),
    )
    def row(number: int) -> Coefficient:
        total = field.value(0)
        for exponents, coefficient in tails[str(number)]:
            term = field.value(coefficient)
            for factor, exponent in zip(factors, exponents):
                if exponent:
                    term = mul(term, pow(factor, exponent) if field.p == 0 else pow(factor, exponent, field.p))
            total = add(total, term)
        return total
    return add(add(add(row(7), scale(mul(mul(e, e), row(3)), Fraction(-1, 32))), scale(mul(mul(mul(e, e), e), row(1)), Fraction(1, 64))), scale(v("J"), Fraction(-1, 4)))


def scalarize_series(field: Field, item: Series, values: dict[str, object]) -> tuple[Coefficient, ...]:
    return tuple(jet_eval(field, coefficient, values) for coefficient in item)


def direct_numeric_grade48(field: Field, tails: dict[str, object], source: dict[str, Series], values: dict[str, object]) -> Coefficient:
    abstract_numeric = {name: scalarize_series(field, source[name], values) for name in ABS_VARS}
    a, e, m = abstract_numeric["a"], abstract_numeric["E"], abstract_numeric["M"]
    x, y = abstract_numeric["X"], abstract_numeric["Y"]
    r1, r0, s1, s0, lam = (abstract_numeric[name] for name in ("R1", "R0", "S1", "S0", "lambda"))
    def add(*items: tuple[Coefficient, ...]) -> tuple[Coefficient, ...]:
        return scalar_series_add(field, *items)
    def mul(left: tuple[Coefficient, ...], right: tuple[Coefficient, ...]) -> tuple[Coefficient, ...]:
        return scalar_series_mul(field, left, right)
    def scale(item: tuple[Coefficient, ...], value: object) -> tuple[Coefficient, ...]:
        return scalar_series_scale(field, item, value)
    a2 = mul(a, a)
    qp = add(e, scale(a2, -6))
    qc = add(scale(mul(a, add(scale(a2, 4), scale(e, -1))), 2), x, r1)
    qr = add(mul(a2, add(e, scale(a2, -3))), r0, scale(mul(a, add(x, r1)), -1))
    n3 = mul(lam, m)
    n2 = mul(lam, mul(a, m))
    n1 = mul(lam, add(mul(add(e, scale(a2, -5)), m), y, s1))
    n0 = mul(lam, add(scale(mul(mul(a, add(e, scale(a2, -3))), m), -1), scale(mul(a, y), -1), scale(mul(m, x), Fraction(1, 2)), s0, scale(mul(a, s1), -1)))
    factors = (
        add(mul(qr, qr), n0), add(scale(mul(qc, qr), 2), n1),
        add(mul(qc, qc), scale(mul(qp, qr), 2), n2), add(scale(mul(qp, qc), 2), n3),
        add(mul(qp, qp), scale(qr, 2)), scale(qc, 2), scale(qp, 2),
        abstract_numeric["K10"], abstract_numeric["K6"], abstract_numeric["K2"],
    )
    power_cache: dict[tuple[int, int], tuple[Coefficient, ...]] = {}
    def power(index: int, exponent: int) -> tuple[Coefficient, ...]:
        key = (index, exponent)
        if key not in power_cache:
            power_cache[key] = scalar_series_pow(field, factors[index], exponent)
        return power_cache[key]
    def row(number: int) -> tuple[Coefficient, ...]:
        total = tuple(field.value(0) for _ in range(MAX_GRADE + 1))
        for exponents, coefficient in tails[str(number)]:
            term = tuple([field.value(coefficient)] + [field.value(0)] * MAX_GRADE)
            for index, exponent in enumerate(exponents):
                if exponent:
                    term = mul(term, power(index, exponent))
            total = add(total, term)
        return total
    p1, p3, p7 = row(1), row(3), row(7)
    functional = add(p7, scale(mul(mul(e, e), p3), Fraction(-1, 32)), scale(mul(mul(mul(e, e), e), p1), Fraction(1, 64)), scale(abstract_numeric["J"], Fraction(-1, 4)))
    return functional[MAX_GRADE]


def extract_grade48(field: Field, functional: DensePoly, source: dict[str, Series]) -> tuple[JetPoly, dict[str, object]]:
    survivors = {
        monomial: coefficient for monomial, coefficient in functional.items()
        if sum(exponent * value for exponent, value in zip(monomial, ABS_VALUATIONS)) <= MAX_GRADE
    }
    power_cache: dict[tuple[str, int], Series] = {}
    product_cache: dict[DenseMonomial, Series] = {}
    one = series_from_terms(field, ((0, jet_const(field, 1)),))

    def power(name: str, exponent: int) -> Series:
        key = (name, exponent)
        if key not in power_cache:
            result = one
            base = source[name]
            remaining = exponent
            while remaining:
                if remaining & 1:
                    result = series_mul(field, result, base)
                remaining //= 2
                if remaining:
                    base = series_mul(field, base, base)
            power_cache[key] = result
        return power_cache[key]

    def product(monomial: DenseMonomial) -> Series:
        if monomial not in product_cache:
            result = one
            for name, exponent in zip(ABS_VARS, monomial):
                if exponent:
                    result = series_mul(field, result, power(name, exponent))
            product_cache[monomial] = result
        return product_cache[monomial]

    result: JetPoly = {}
    ordered = sorted(survivors.items(), key=lambda item: (sum(e * v for e, v in zip(item[0], ABS_VALUATIONS)), item[0]))
    for offset, (monomial, coefficient) in enumerate(ordered, 1):
        result = jet_add(field, result, jet_scale(field, product(monomial)[MAX_GRADE], coefficient))
        print(f"SPARSE_DAG_G48_PROGRESS={offset}/{len(ordered)}:support={len(result)}", flush=True)
    metrics = {
        "valuation_survivor_count": len(survivors),
        "valuation_histogram": {
            str(value): sum(1 for monomial in survivors if sum(e * v for e, v in zip(monomial, ABS_VALUATIONS)) == value)
            for value in sorted({sum(e * v for e, v in zip(monomial, ABS_VALUATIONS)) for monomial in survivors})
        },
        "series_power_cache_entries": len(power_cache),
        "series_product_cache_entries": len(product_cache),
        "grade48_support": len(result),
    }
    return result, metrics


def witness_values(chart: str) -> dict[str, object]:
    values: dict[str, object] = {name: 0 for name in JET_VARS}
    values.update({"a0": 1, "p": 1, "m": 1, "kk0": 1})
    if chart == "x":
        values.update({"x0": 1, "r00": Fraction(1, 2), "d60": 16, "d20": 7})
    elif chart == "y":
        values.update({"y0": 1, "r00": -1, "d60": -74, "d20": Fraction(-61, 2)})
    else:
        fail(("unknown witness chart", chart))
    return values


def deterministic_values() -> dict[str, int]:
    return {name: ((index * 7 + 3) % 11) - 5 for index, name in enumerate(JET_VARS)}


def canonical_dense(field: Field, poly: DensePoly) -> dict[str, object]:
    return {
        "variables": list(ABS_VARS),
        "terms": [
            {"exponents": list(monomial), "coefficient": field.text(coefficient)}
            for monomial, coefficient in sorted(poly.items())
        ],
    }


def canonical_jet(field: Field, poly: JetPoly) -> dict[str, object]:
    return {
        "variables": list(JET_VARS),
        "terms": [
            {
                "monomial": [[JET_VARS[index], exponent] for index, exponent in monomial],
                "coefficient": field.text(coefficient),
            }
            for monomial, coefficient in sorted(poly.items())
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    field = Field(args.characteristic)
    if digest(TAILS) != TAILS_SHA:
        fail(("frozen tails mismatch", digest(TAILS)))
    tails = json.loads(TAILS.read_text())
    canonical_tails = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical_tails.encode()).hexdigest() != TAILS_CANONICAL_SHA:
        fail("canonical tails mismatch")
    if {row: len(tails[row]) for row in ("1", "3", "7")} != {"1": 36, "3": 58, "7": 131}:
        fail("tail count mismatch")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    functional, abstract_metrics = build_abstract(field, tails)
    print("SPARSE_DAG_ABSTRACT_SECONDS=%.3f" % (time.monotonic() - started), flush=True)

    for offset in range(3):
        values = {name: (index + 2) * (offset + 1) - 3 for index, name in enumerate(ABS_VARS)}
        left = dense_eval(field, functional, values)
        right = raw_scalar_functional(field, tails, values)
        if left != right:
            fail(("abstract scalar control failed", offset, left, right))

    source = source_series(field)
    grade48, extraction_metrics = extract_grade48(field, functional, source)
    print("SPARSE_DAG_TOTAL_SECONDS=%.3f" % (time.monotonic() - started), flush=True)
    expected = field.value(Fraction(-1, 32))
    witness = {chart: jet_eval(field, grade48, witness_values(chart)) for chart in ("x", "y")}
    if witness != {"x": expected, "y": expected}:
        fail(("certified witness control failed", witness, expected))
    random_values = deterministic_values()
    emitted_random = jet_eval(field, grade48, random_values)
    direct_random = direct_numeric_grade48(field, tails, source, random_values)
    if emitted_random != direct_random:
        fail(("direct numeric convolution control failed", emitted_random, direct_random))

    abstract_payload = canonical_dense(field, functional)
    grade48_payload = canonical_jet(field, grade48)
    abstract_bytes = (json.dumps(abstract_payload, sort_keys=True, separators=(",", ":")) + "\n").encode()
    grade48_bytes = (json.dumps(grade48_payload, sort_keys=True, separators=(",", ":")) + "\n").encode()
    (output / "abstract_functional_support.json").write_bytes(abstract_bytes)
    (output / "grade48_sparse_polynomial.json").write_bytes(grade48_bytes)
    result = {
        "status": "PASS-A-H16-Q6-A4-G48-SPARSE-DAG-V4",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "tails_sha256": digest(TAILS),
        "abstract_metrics": abstract_metrics,
        "extraction_metrics": extraction_metrics,
        "abstract_functional_sha256": sha256(abstract_bytes).hexdigest(),
        "grade48_sparse_sha256": sha256(grade48_bytes).hexdigest(),
        "abstract_scalar_controls": 3,
        "direct_numeric_series_control": field.text(direct_random),
        "witness_x": field.text(witness["x"]),
        "witness_y": field.text(witness["y"]),
        "elapsed_seconds": time.monotonic() - started,
        "scope": "FIXED_H16_Q6_A4_RAW_ROWS_1_3_7_GRADE48_SPARSE_FUNCTIONAL_ONLY_NO_PREDECESSOR_REDUCTION_RATIONAL_REGRADING_REES_ORDER2_MAX12_OR_JC2_VERDICT",
    }
    (output / "result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("A_H16_SPARSE_DAG_ABSTRACT_SUPPORT=" + str(abstract_metrics["abstract_functional_support"]))
    print("A_H16_SPARSE_DAG_VALUATION_SURVIVORS=" + str(extraction_metrics["valuation_survivor_count"]))
    print("A_H16_SPARSE_DAG_G48_SUPPORT=" + str(extraction_metrics["grade48_support"]))
    print("A_H16_SPARSE_DAG_WITNESS_X=" + field.text(witness["x"]))
    print("A_H16_SPARSE_DAG_WITNESS_Y=" + field.text(witness["y"]))
    print("A_H16_SPARSE_DAG_DIRECT_CONTROL=" + field.text(direct_random))
    print("A_H16_SPARSE_DAG_G48_SHA256=" + result["grade48_sparse_sha256"])
    print("A_H16_SPARSE_DAG_ENDPOINT=PASS_COEFFICIENT_ONLY_GRADE48")
    print("A_H16_SPARSE_DAG_DONE=1")
    print("A_H16_SPARSE_DAG_SCOPE=" + result["scope"])


if __name__ == "__main__":
    main()
