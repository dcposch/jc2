#!/usr/bin/env python3
"""Generic c1 transport factorization over Q(C), with exact pivot strata."""

from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
import importlib.util
from pathlib import Path
import sys

import flint
from flint import fmpq, fmpq_poly


REPO = Path(__file__).resolve().parents[2]
FB_PATH = REPO / "cases/td6_two_chart_first_band_20260824/replay.py"
FB_SHA = "c55e213672ebd22cf3e9e8f378ffa857f85c3a54be7ed39e5c956df36ff6e735"


def load(name, path, expected):
    assert sha256(path.read_bytes()).hexdigest() == expected
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


fb = load("td6_fb_c1_rational", FB_PATH, FB_SHA)
X = fmpq_poly([0, 1])
ONE = fmpq_poly([1])


def rational(value):
    if isinstance(value, fmpq):
        return value
    if isinstance(value, Q):
        return fmpq(value.numerator, value.denominator)
    return fmpq(value)


def polynomial(value):
    if isinstance(value, fmpq_poly):
        return value
    if isinstance(value, (list, tuple)):
        return fmpq_poly([rational(entry) for entry in value])
    return fmpq_poly([rational(value)]) if value else fmpq_poly()


class Rat:
    """Reduced rational function in C over Q, backed by FLINT."""

    __slots__ = ("numerator", "denominator")

    def __init__(self, value=0, denominator=None, *, normalized=False):
        if isinstance(value, Rat) and denominator is None:
            self.numerator = value.numerator
            self.denominator = value.denominator
            return
        numerator = polynomial(value)
        denominator = ONE if denominator is None else polynomial(denominator)
        if not denominator:
            raise ZeroDivisionError
        if not numerator:
            self.numerator = fmpq_poly()
            self.denominator = ONE
            return
        if not normalized:
            common = numerator.gcd(denominator)
            if common.degree() >= 0 and common != ONE:
                numerator = numerator // common
                denominator = denominator // common
            lead = denominator[denominator.degree()]
            if lead != 1:
                numerator *= 1 / lead
                denominator *= 1 / lead
        self.numerator = numerator
        self.denominator = denominator

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Rat) else Rat(value)

    def __add__(self, other):
        other = Rat.coerce(other)
        return Rat(
            self.numerator * other.denominator
            + other.numerator * self.denominator,
            self.denominator * other.denominator,
        )

    __radd__ = __add__

    def __neg__(self):
        return Rat(-self.numerator, self.denominator, normalized=True)

    def __sub__(self, other):
        return self + (-Rat.coerce(other))

    def __rsub__(self, other):
        return Rat.coerce(other) - self

    def __mul__(self, other):
        other = Rat.coerce(other)
        if not self or not other:
            return Rat()
        # Cross-cancel before multiplying; this is much cheaper than a gcd
        # of the two full products in the large sparse transport echelon.
        left_common = self.numerator.gcd(other.denominator)
        right_common = other.numerator.gcd(self.denominator)
        left_num = self.numerator // left_common
        right_den = other.denominator // left_common
        right_num = other.numerator // right_common
        left_den = self.denominator // right_common
        return Rat(
            left_num * right_num,
            left_den * right_den,
            normalized=True,
        )

    __rmul__ = __mul__

    def inverse(self):
        if not self:
            raise ZeroDivisionError
        lead = self.numerator[self.numerator.degree()]
        return Rat(
            self.denominator * (1 / lead),
            self.numerator * (1 / lead),
            normalized=True,
        )

    def __truediv__(self, other):
        return self * Rat.coerce(other).inverse()

    def __rtruediv__(self, other):
        return Rat.coerce(other) / self

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        out = Rat(1)
        base = self
        while exponent:
            if exponent & 1:
                out *= base
            base *= base
            exponent //= 2
        return out

    def __bool__(self):
        return bool(self.numerator)

    def __eq__(self, other):
        other = Rat.coerce(other)
        return (
            self.numerator == other.numerator
            and self.denominator == other.denominator
        )

    def __repr__(self):
        return f"Rat(({self.numerator})/({self.denominator}))"

    @property
    def degree_span(self):
        return max(self.numerator.degree(), self.denominator.degree())


def monic(poly):
    if not poly:
        return poly
    return poly * (1 / poly[poly.degree()])


def factor(rows):
    pivots = {}
    records = []
    exceptional_factors = Counter()
    pivot_events = []
    determinant = Rat(1)
    max_span = 0
    for row_index, (key, original_row, _) in enumerate(rows):
        row = {variable: Rat(value) for variable, value in original_row.items()}
        factors = []
        while row:
            pivot = min(row)
            if pivot not in pivots:
                break
            multiplier = row[pivot]
            factors.append((pivot, multiplier))
            old_row = pivots[pivot]
            for variable, coefficient in old_row.items():
                value = row.get(variable, Rat()) - multiplier * coefficient
                if value:
                    row[variable] = value
                    max_span = max(max_span, value.degree_span)
                else:
                    row.pop(variable, None)
        if not row:
            records.append((key, "dependent", None, None, factors))
            continue
        pivot = min(row)
        lead = row[pivot]
        determinant *= lead
        content, factors_over_q = lead.numerator.factor()
        assert content
        if lead.numerator.degree() > 0 or lead.denominator.degree() > 0:
            pivot_events.append(
                (
                    row_index,
                    key,
                    pivot,
                    str(lead.numerator),
                    str(lead.denominator),
                )
            )
        for irreducible, multiplicity in factors_over_q:
            exceptional_factors[str(monic(irreducible))] += multiplicity
        pivots[pivot] = {
            variable: coefficient / lead for variable, coefficient in row.items()
        }
        records.append((key, "pivot", pivot, lead, factors))
        if row_index % 250 == 0:
            print(
                f"rows={row_index};pivots={len(pivots)};"
                f"factors={len(exceptional_factors)};maxspan={max_span}",
                flush=True,
            )
    print("TD6-C1-GENERIC-TRANSPORT: PASS")
    print(f"flint_version = {flint.__version__}")
    print(f"rank_over_Q(C) = {len(pivots)}")
    print(f"dependent_rows = {len(rows)-len(pivots)}")
    print(f"max_rational_degree_span = {max_span}")
    print(f"exceptional_irreducible_factor_count = {len(exceptional_factors)}")
    for factor_text, multiplicity in sorted(exceptional_factors.items()):
        print(f"pivot_factor = ({factor_text}); aggregate_multiplicity={multiplicity}")
    print(f"nonconstant_pivot_event_count = {len(pivot_events)}")
    for event in pivot_events:
        print(f"pivot_event = {event}")
    print(f"selected_minor_numerator_degree = {determinant.numerator.degree()}")
    print(f"selected_minor_denominator_degree = {determinant.denominator.degree()}")
    print(f"selected_minor = {determinant!r}")
    print(
        "selected_minor.sha256 = "
        f"{sha256(repr(determinant).encode()).hexdigest()}"
    )
    return pivots, records, exceptional_factors, determinant


def main():
    C = Rat(X)
    fb.CENTER = (C, Rat(1), Rat(1))
    fb._X_POWER_CACHE.clear()
    nf, rows_f = fb.build_transport(
        15, 60, 3, {15: Q(1)}, fb.F1_F_PATTERN, fb.POLE_F_PATTERN
    )
    ng, rows_g = fb.build_transport(
        25, 100, 5, {1: Q(1), 25: Q(1)}, fb.F1_G_PATTERN, fb.POLE_G_PATTERN
    )
    rows = [(('f',) + key, row, rhs) for key, row, rhs in rows_f]
    rows += [
        (('g',) + key, {nf + variable: coefficient for variable, coefficient in row.items()}, rhs)
        for key, row, rhs in rows_g
    ]
    print(f"transport_rows = {len(rows)}", flush=True)
    pivots, records, _, _ = factor(rows)
    assert len(pivots) == 3470


if __name__ == "__main__":
    main()
