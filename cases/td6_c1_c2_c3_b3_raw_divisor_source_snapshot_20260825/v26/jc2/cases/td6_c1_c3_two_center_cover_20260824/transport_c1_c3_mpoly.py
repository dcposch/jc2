#!/usr/bin/env python3
"""Exact constant-first TD6 transport over Q(C,U), diagnostic prototype."""

from fractions import Fraction as Q
import importlib.util
from pathlib import Path
import sys

import flint


HERE = Path(__file__).resolve().parent
FB_PATH = HERE / "c1_rational_transport.py"
spec = importlib.util.spec_from_file_location("td6_c1_c3_mpoly_source", FB_PATH)
source = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules["td6_c1_c3_mpoly_source"] = source
spec.loader.exec_module(source)
fb = source.fb

CP_PATH = HERE / "c1_pencil.py"
cp_spec = importlib.util.spec_from_file_location("td6_c1_c3_mpoly_rhs", CP_PATH)
cp = importlib.util.module_from_spec(cp_spec)
assert cp_spec.loader is not None
sys.modules["td6_c1_c3_mpoly_rhs"] = cp
cp_spec.loader.exec_module(cp)

CTX = flint.fmpq_mpoly_ctx.get(["C", "U"], ordering="lex")
C, U = CTX.gens()
ZERO, ONE = CTX.constant(0), CTX.constant(1)


def poly(value):
    if isinstance(value, flint.fmpq_mpoly):
        return value
    if isinstance(value, Q):
        return CTX.constant(flint.fmpq(value.numerator, value.denominator))
    return CTX.constant(value)


class Rat2:
    __slots__ = ("numerator", "denominator")

    def __init__(self, numerator=0, denominator=1, reduced=False):
        if isinstance(numerator, Rat2) and denominator == 1:
            self.numerator, self.denominator = numerator.numerator, numerator.denominator
            return
        numerator, denominator = poly(numerator), poly(denominator)
        if not denominator:
            raise ZeroDivisionError
        if not numerator:
            self.numerator, self.denominator = ZERO, ONE
            return
        if denominator.total_degree() == 0:
            scalar = denominator.leading_coefficient()
            self.numerator, self.denominator = numerator / scalar, ONE
            return
        if not reduced:
            common = numerator.gcd(denominator)
            if common.total_degree() > 0:
                numerator, denominator = numerator // common, denominator // common
        scalar = denominator.leading_coefficient()
        self.numerator, self.denominator = numerator / scalar, denominator / scalar

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Rat2) else Rat2(value)

    def __add__(self, other):
        other = Rat2.coerce(other)
        if self.denominator == ONE and other.denominator == ONE:
            return Rat2(self.numerator + other.numerator, reduced=True)
        return Rat2(
            self.numerator * other.denominator + other.numerator * self.denominator,
            self.denominator * other.denominator,
        )

    __radd__ = __add__

    def __neg__(self):
        return Rat2(-self.numerator, self.denominator, reduced=True)

    def __sub__(self, other):
        return self + (-Rat2.coerce(other))

    def __rsub__(self, other):
        return Rat2.coerce(other) - self

    def __mul__(self, other):
        other = Rat2.coerce(other)
        if self.denominator == ONE and other.denominator == ONE:
            return Rat2(self.numerator * other.numerator, reduced=True)
        return Rat2(
            self.numerator * other.numerator,
            self.denominator * other.denominator,
        )

    __rmul__ = __mul__

    def inverse(self):
        if not self.numerator:
            raise ZeroDivisionError
        return Rat2(self.denominator, self.numerator, reduced=True)

    def __truediv__(self, other):
        return self * Rat2.coerce(other).inverse()

    def __rtruediv__(self, other):
        return Rat2.coerce(other) / self

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        return Rat2(self.numerator**exponent, self.denominator**exponent, reduced=True)

    def __bool__(self):
        return bool(self.numerator)

    def __eq__(self, other):
        other = Rat2.coerce(other)
        return (
            self.numerator == other.numerator
            and self.denominator == other.denominator
        )


def factor(rows):
    pivots, events, records = {}, [], []
    determinant = Rat2(1)
    for row_index, (key, original_row, _) in enumerate(rows):
        row = {variable: Rat2(value) for variable, value in original_row.items()}
        factors = []
        while row:
            pivot = min(row)
            if pivot not in pivots:
                break
            multiplier = row[pivot]
            factors.append((pivot, multiplier))
            for variable, coefficient in pivots[pivot].items():
                value = row.get(variable, Rat2()) - multiplier * coefficient
                if value:
                    row[variable] = value
                else:
                    row.pop(variable, None)
        if not row:
            records.append((key, "dependent", None, None, factors))
            continue
        pivot = min(row)
        lead = row[pivot]
        determinant *= lead
        if lead.numerator.total_degree() or lead.denominator.total_degree():
            events.append((row_index, key, pivot, lead.numerator, lead.denominator))
        inverse = lead.inverse()
        pivots[pivot] = {
            variable: coefficient * inverse for variable, coefficient in row.items()
        }
        records.append((key, "pivot", pivot, lead, factors))
        if row_index % 250 == 0:
            print(
                f"rows={row_index};pivots={len(pivots)};events={len(events)};"
                f"detdeg={determinant.numerator.total_degree()}/"
                f"{determinant.denominator.total_degree()}",
                flush=True,
            )
    return pivots, records, events, determinant


def source_vector(key):
    value = cp.source_rhs(key)
    return tuple(
        Rat2(cp.rt.rational(coordinate))
        for a_coefficient in value.coefficients
        for coordinate in a_coefficient.coefficients
    )


def vector_sub(left, right):
    return tuple(a - b for a, b in zip(left, right))


def vector_scale(value, scalar):
    return tuple(coordinate * scalar for coordinate in value)


def propagate(rows, records):
    pivot_rhs, compatibility = {}, []
    for source_row, record in zip(rows, records):
        source_key, _, _ = source_row
        key, kind, pivot, lead, factors = record
        assert source_key == key
        value = source_vector(key)
        for old, factor in factors:
            value = vector_sub(value, vector_scale(pivot_rhs[old], factor))
        if kind == "pivot":
            pivot_rhs[pivot] = vector_scale(value, lead.inverse())
        elif any(value):
            compatibility.append((key, value))
    return pivot_rhs, compatibility


def main():
    fb.CENTER = (Rat2(C), Rat2(1), Rat2(U))
    fb._X_POWER_CACHE.clear()
    nf, rows_f = fb.build_transport(
        15, 60, 3, {15: Q(1)}, fb.F1_F_PATTERN, fb.POLE_F_PATTERN
    )
    ng, rows_g = fb.build_transport(
        25, 100, 5, {1: Q(1), 25: Q(1)}, fb.F1_G_PATTERN, fb.POLE_G_PATTERN
    )
    rows = [(("f",) + key, row, rhs) for key, row, rhs in rows_f]
    rows += [
        (("g",) + key,
         {nf + variable: coefficient for variable, coefficient in row.items()}, rhs)
        for key, row, rhs in rows_g
    ]
    constant = [row for row in rows if row[0][1] != "X"]
    changing = [row for row in rows if row[0][1] == "X"]
    print(
        f"constant_rows={len(constant)};changing_rows={len(changing)};"
        f"columns={nf+ng}",
        flush=True,
    )
    ordered = constant + changing
    pivots, records, events, determinant = factor(ordered)
    pivot_rhs, compatibility = propagate(ordered, records)
    assert not compatibility
    print(f"rank_QCU={len(pivots)}")
    print(f"event_count={len(events)}")
    print(f"affine_compatibility_count={len(compatibility)}")
    print(f"affine_pivot_rhs_count={len(pivot_rhs)}")
    for index, event in enumerate(events):
        row_index, key, pivot, numerator, denominator = event
        print(
            f"event[{index}]={row_index},{key},{pivot};"
            f"num=({numerator});den=({denominator})"
        )
    print(f"det_num=({determinant.numerator})")
    print(f"det_den=({determinant.denominator})")
    print("TD6-C1-C3-MPOLY-TRANSPORT PASS")


if __name__ == "__main__":
    main()
