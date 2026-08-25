#!/usr/bin/env python3
"""Prototype generic first-band solve over E(C,U), constant-first transport."""

from fractions import Fraction as Q
from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
REVERSE_PIVOTS = "--reverse-pivots" in sys.argv
SPARSE_PIVOTS = "--sparse-pivots" in sys.argv
B_LOCAL_PIVOTS = "--b-local-pivots" in sys.argv


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


t = load("td6_c1_c3_transport_for_first", HERE / "transport_c1_c3_mpoly.py")
cp, fb, qd = t.cp, t.fb, t.cp.qd


class RTShim:
    Rat = t.Rat2

    @staticmethod
    def rational(value):
        return cp.rt.rational(value)


class CPShim:
    rt = RTShim
    qd = cp.qd
    K = cp.K
    E = cp.E
    Frac = cp.Frac
    fast_evec = cp.fast_evec


FIELD = cp.fast_efield.EFieldFactory(CPShim)
EField = cp.fast_efield.EField
B_POLY = (
    4*t.C**2*t.U**2 + 24*t.C*t.U**4 - 4*t.C*t.U
    + 20*t.U**6 - 20*t.U**3 + 1
)
B_H_RESULTANT = 128*t.U**6 - 32*t.U**3 + 1


class E2:
    __slots__ = ("value",)

    def __init__(self, value=0):
        if isinstance(value, E2):
            self.value = value.value
        elif isinstance(value, EField):
            assert value.factory is FIELD
            self.value = value
        elif isinstance(value, t.Rat2):
            self.value = FIELD.scalar(value)
        else:
            self.value = FIELD.from_e(cp.E(value))

    @staticmethod
    def coerce(value):
        return value if isinstance(value, E2) else E2(value)

    def __add__(self, other):
        return E2(self.value + E2.coerce(other).value)

    __radd__ = __add__

    def __neg__(self):
        return E2(-self.value)

    def __sub__(self, other):
        return self + (-E2.coerce(other))

    def __rsub__(self, other):
        return E2.coerce(other) - self

    def __mul__(self, other):
        return E2(self.value * E2.coerce(other).value)

    __rmul__ = __mul__

    def inverse(self):
        return E2(self.value.inverse())

    def __truediv__(self, other):
        return self * E2.coerce(other).inverse()

    def __rtruediv__(self, other):
        return E2.coerce(other) / self

    def __pow__(self, exponent):
        return E2(self.value**exponent)

    def __bool__(self):
        return bool(self.value)

    def __eq__(self, other):
        return self.value == E2.coerce(other).value


def from_vector(vector):
    return E2(FIELD.from_coordinates(vector))


def scalar(value):
    return E2(FIELD.scalar(t.Rat2.coerce(value)))


def scalar_coordinate(value):
    coordinates = [
        coordinate
        for kvalue in value.value.coefficients
        for coordinate in kvalue.coordinates
    ]
    nonzero = [coordinate for coordinate in coordinates if coordinate]
    return nonzero[0] if len(nonzero) == 1 else None


def choose_new_pivot(row):
    if REVERSE_PIVOTS:
        return max(row)
    if not SPARSE_PIVOTS and not B_LOCAL_PIVOTS:
        return min(row)
    candidates = []
    for variable, coefficient in row.items():
        coordinate = scalar_coordinate(coefficient)
        if coordinate is None:
            continue
        b_residual_degree = 0
        if B_LOCAL_PIVOTS:
            resultant = B_POLY.resultant(coordinate.numerator, 0)
            if not resultant:
                b_residual_degree = 10**9
            else:
                _, factors = resultant.factor()
                b_residual_degree = sum(
                    factor.total_degree() * multiplicity
                    for factor, multiplicity in factors
                    if factor != t.U and factor != B_H_RESULTANT
                )
        candidates.append((
            b_residual_degree,
            coordinate.numerator.total_degree(),
            coordinate.denominator.total_degree(),
            len(str(coordinate.numerator)) + len(str(coordinate.denominator)),
            variable,
        ))
    assert candidates, "no scalar-coefficient pivot candidate"
    return min(candidates)[-1]


def restrict_row(original_row, pivots, pivot_rhs, free_parameter):
    row = {
        variable: t.Rat2.coerce(coefficient)
        for variable, coefficient in original_row.items() if coefficient
    }
    constant = tuple(t.Rat2() for _ in range(18))
    for pivot in sorted(pivots):
        factor = row.pop(pivot, None)
        if factor is None or not factor:
            continue
        constant = tuple(
            old + factor * rhs for old, rhs in zip(constant, pivot_rhs[pivot])
        )
        for variable, coefficient in pivots[pivot].items():
            if variable == pivot:
                continue
            value = row.get(variable, t.Rat2()) - factor * coefficient
            if value:
                row[variable] = value
            else:
                row.pop(variable, None)
    assert all(variable in free_parameter for variable in row)
    return (
        from_vector(constant),
        {free_parameter[variable]: scalar(coefficient) for variable, coefficient in row.items()},
    )


def solve(rows):
    pivots, events = {}, []
    determinant = t.Rat2(1)
    for row_index, (key, original_row, original_rhs) in enumerate(rows):
        row = {variable: E2.coerce(value) for variable, value in original_row.items()}
        rhs = E2.coerce(original_rhs)
        while row:
            pivot = next((variable for variable in pivots if variable in row), None)
            if pivot is None:
                break
            factor = row[pivot]
            old_row, old_rhs = pivots[pivot]
            for variable, coefficient in old_row.items():
                value = row.get(variable, E2()) - factor * coefficient
                if value:
                    row[variable] = value
                else:
                    row.pop(variable, None)
            rhs -= factor * old_rhs
        if not row:
            assert not rhs, ("first compatibility", key)
            continue
        pivot = choose_new_pivot(row)
        lead = row[pivot]
        inverse = lead.inverse()
        pivots[pivot] = (
            {variable: coefficient * inverse for variable, coefficient in row.items()},
            rhs * inverse,
        )
        coordinates = [
            coordinate
            for kvalue in lead.value.coefficients
            for coordinate in kvalue.coordinates
        ]
        nonzero = [value for value in coordinates if value]
        assert len(nonzero) == 1
        scalar_lead = nonzero[0]
        determinant *= scalar_lead
        events.append({
            "row_index": row_index,
            "key": key,
            "pivot": pivot,
            "nonzero_coordinates": sum(bool(value) for value in coordinates),
            "max_num_degree": max(
                (value.numerator.total_degree() for value in coordinates if value),
                default=-1,
            ),
            "max_den_degree": max(
                (value.denominator.total_degree() for value in coordinates if value),
                default=-1,
            ),
            "sha256": sha256(repr(tuple(
                (str(value.numerator), str(value.denominator)) for value in coordinates
            )).encode()).hexdigest(),
            "numerator": str(scalar_lead.numerator),
            "denominator": str(scalar_lead.denominator),
            "numerator_factorization": str(scalar_lead.numerator.factor()),
            "denominator_factorization": str(scalar_lead.denominator.factor()),
        })
    return pivots, events, determinant


def main():
    print(
        "first_pivot_order=" + (
            "B-local-scalar" if B_LOCAL_PIVOTS else
            "sparse-scalar" if SPARSE_PIVOTS else
            "descending" if REVERSE_PIVOTS else "ascending"
        ),
        flush=True,
    )
    fb.CENTER = (t.Rat2(t.C), t.Rat2(1), t.Rat2(t.U))
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
    ordered = [row for row in rows if row[0][1] != "X"] + [
        row for row in rows if row[0][1] == "X"
    ]
    transport_pivots, records, transport_events, determinant = t.factor(ordered)
    pivot_rhs, compatibility = t.propagate(ordered, records)
    assert len(transport_pivots) == 3470 and not compatibility
    free = [variable for variable in range(nf + ng) if variable not in transport_pivots]
    free_parameter = {variable: index for index, variable in enumerate(free)}
    assert len(free) == 132
    print("generic bivariate transport/affine PASS", flush=True)

    f1 = []
    g1 = []
    for degree in range(16):
        row = fb.x_chart_coefficient(15, 60, 1, degree)
        f1.append(restrict_row(row, transport_pivots, pivot_rhs, free_parameter))
    for degree in range(26):
        row = {
            nf + variable: coefficient
            for variable, coefficient in fb.x_chart_coefficient(25, 100, 1, degree).items()
        }
        g1.append(restrict_row(row, transport_pivots, pivot_rhs, free_parameter))

    qd.Dual = E2
    qd.Q_PRIME = {0: E2(1), 24: E2(25)}
    first_rows = qd.pack("X-2", qd.first_band_polynomials(f1, g1))
    first_pivots, events, first_determinant = solve(first_rows)
    assert len(first_pivots) == 38
    print("generic bivariate first-band PASS", flush=True)
    print(f"first_rank={len(first_pivots)}/132")
    print(f"first_event_count={len(events)}")
    for event in events:
        print(f"first_event={event}")
    print(f"first_selected_minor_num=({first_determinant.numerator})")
    print(f"first_selected_minor_den=({first_determinant.denominator})")
    print(f"first_selected_minor_num_factor={first_determinant.numerator.factor()}")
    print(f"first_selected_minor_den_factor={first_determinant.denominator.factor()}")
    print("TD6-C1-C3-MPOLY-FIRST PASS")


if __name__ == "__main__":
    main()
