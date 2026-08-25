#!/usr/bin/env python3
"""Exact TD6 (c1,c3) first-infinitesimal discriminator.

The full nonlinear base line is (c1,c2,c3)=(C,1,1).  We replace c3 by
1+eps over eps^2=0, refactor every matrix (so lambda' is retained), and
emit localized compatibility/Fitting data.  This is not full bivariate
coverage and hard-codes no family/SP2 conclusion.
"""

from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
import importlib.util
from itertools import combinations
import json
from pathlib import Path
import sys


PRIVATE = Path(__file__).resolve().parent
CP_PATH = PRIVATE / "c1_pencil.py"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


cp = load("td6_c1_pencil_for_c3", CP_PATH)
rt, fb, qd, nr, E = cp.rt, cp.fb, cp.qd, cp.nr, cp.E


class QDual:
    """Q(C)[eps]/eps^2."""

    __slots__ = ("value", "derivative")

    def __init__(self, value=0, derivative=0):
        if isinstance(value, QDual):
            self.value = value.value
            self.derivative = value.derivative
        else:
            self.value = rt.Rat.coerce(value)
            self.derivative = rt.Rat.coerce(derivative)

    @staticmethod
    def coerce(value):
        return value if isinstance(value, QDual) else QDual(value)

    def __add__(self, other):
        other = QDual.coerce(other)
        return QDual(self.value + other.value, self.derivative + other.derivative)

    __radd__ = __add__

    def __neg__(self):
        return QDual(-self.value, -self.derivative)

    def __sub__(self, other):
        return self + (-QDual.coerce(other))

    def __rsub__(self, other):
        return QDual.coerce(other) - self

    def __mul__(self, other):
        other = QDual.coerce(other)
        return QDual(
            self.value * other.value,
            self.derivative * other.value + self.value * other.derivative,
        )

    __rmul__ = __mul__

    def inverse(self):
        if not self.value:
            raise ZeroDivisionError("zero-base Q(C) dual pivot")
        inverse = self.value.inverse()
        return QDual(inverse, -(inverse * inverse) * self.derivative)

    def __truediv__(self, other):
        return self * QDual.coerce(other).inverse()

    def __rtruediv__(self, other):
        return QDual.coerce(other) / self

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        out = QDual(1)
        base = self
        while exponent:
            if exponent & 1:
                out *= base
            base *= base
            exponent //= 2
        return out

    def __bool__(self):
        return bool(self.value) or bool(self.derivative)

    def __eq__(self, other):
        other = QDual.coerce(other)
        return self.value == other.value and self.derivative == other.derivative

    def __repr__(self):
        return f"QDual({self.value!r};{self.derivative!r})"


class EDual:
    """E(C)[eps]/eps^2."""

    __slots__ = ("value", "derivative")

    def __init__(self, value=0, derivative=0):
        if isinstance(value, EDual):
            self.value = value.value
            self.derivative = value.derivative
        elif isinstance(value, QDual):
            self.value = cp.lift_rat(value.value)
            self.derivative = cp.lift_rat(value.derivative)
        else:
            self.value = cp.Frac.coerce(value)
            self.derivative = cp.Frac.coerce(derivative)

    @staticmethod
    def coerce(value):
        return value if isinstance(value, EDual) else EDual(value)

    def __add__(self, other):
        other = EDual.coerce(other)
        return EDual(self.value + other.value, self.derivative + other.derivative)

    __radd__ = __add__

    def __neg__(self):
        return EDual(-self.value, -self.derivative)

    def __sub__(self, other):
        return self + (-EDual.coerce(other))

    def __rsub__(self, other):
        return EDual.coerce(other) - self

    def __mul__(self, other):
        other = EDual.coerce(other)
        return EDual(
            self.value * other.value,
            self.derivative * other.value + self.value * other.derivative,
        )

    __rmul__ = __mul__

    def inverse(self):
        if not self.value:
            raise ZeroDivisionError("zero-base E(C) dual pivot")
        inverse = self.value.inverse()
        return EDual(inverse, -(inverse * inverse) * self.derivative)

    def __truediv__(self, other):
        return self * EDual.coerce(other).inverse()

    def __rtruediv__(self, other):
        return EDual.coerce(other) / self

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        out = EDual(1)
        base = self
        while exponent:
            if exponent & 1:
                out *= base
            base *= base
            exponent //= 2
        return out

    def __bool__(self):
        return bool(self.value) or bool(self.derivative)

    def __eq__(self, other):
        other = EDual.coerce(other)
        return self.value == other.value and self.derivative == other.derivative

    def __repr__(self):
        return f"EDual({self.value!r};{self.derivative!r})"


FAST_FIELD = cp.fast_efield.EFieldFactory(cp)


class FPair:
    """Fast tower-field dual, used only in the small E(C) matrix stages."""

    __slots__ = ("value", "derivative")

    def __init__(self, value=None, derivative=None):
        if value is None:
            self.value = FAST_FIELD.zero
        elif isinstance(value, cp.fast_efield.EField):
            assert value.factory is FAST_FIELD
            self.value = value
        else:
            self.value = FAST_FIELD.from_frac(cp.Frac.coerce(value))
        if derivative is None:
            self.derivative = FAST_FIELD.zero
        elif isinstance(derivative, cp.fast_efield.EField):
            assert derivative.factory is FAST_FIELD
            self.derivative = derivative
        else:
            self.derivative = FAST_FIELD.from_frac(cp.Frac.coerce(derivative))

    @staticmethod
    def from_edual(value):
        if isinstance(value, FPair):
            return value
        value = EDual.coerce(value)
        return FPair(
            FAST_FIELD.from_frac(value.value),
            FAST_FIELD.from_frac(value.derivative),
        )

    def to_edual(self):
        return EDual(
            FAST_FIELD.to_frac(self.value),
            FAST_FIELD.to_frac(self.derivative),
        )

    @staticmethod
    def coerce(value):
        return value if isinstance(value, FPair) else FPair.from_edual(value)

    def __add__(self, other):
        other = FPair.coerce(other)
        return FPair(self.value + other.value, self.derivative + other.derivative)

    __radd__ = __add__

    def __neg__(self):
        return FPair(-self.value, -self.derivative)

    def __sub__(self, other):
        return self + (-FPair.coerce(other))

    def __rsub__(self, other):
        return FPair.coerce(other) - self

    def __mul__(self, other):
        other = FPair.coerce(other)
        return FPair(
            self.value * other.value,
            self.derivative * other.value + self.value * other.derivative,
        )

    __rmul__ = __mul__

    def inverse(self):
        if not self.value:
            raise ZeroDivisionError
        inverse = self.value.inverse()
        return FPair(inverse, -(inverse * inverse) * self.derivative)

    def __truediv__(self, other):
        return self * FPair.coerce(other).inverse()

    def __rtruediv__(self, other):
        return FPair.coerce(other) / self

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        out = FPair(FAST_FIELD.one, FAST_FIELD.zero)
        base = self
        while exponent:
            if exponent & 1:
                out *= base
            base *= base
            exponent //= 2
        return out

    def __bool__(self):
        return bool(self.value) or bool(self.derivative)

    def __eq__(self, other):
        other = FPair.coerce(other)
        return self.value == other.value and self.derivative == other.derivative


def q_to_e(value):
    return EDual(value)


def e_to_q(value):
    value = EDual.coerce(value)
    return QDual(cp.frac_to_rat(value.value), cp.frac_to_rat(value.derivative))


def qfactor(poly):
    if not poly or poly.degree() <= 0:
        return []
    _, factors = poly.factor()
    return [(str(rt.monic(factor)), multiplicity) for factor, multiplicity in factors]


def factor_transport(rows):
    pivots = {}
    records = []
    numerator_factors = Counter()
    denominator_factors = Counter()
    events = []
    determinant = QDual(1)
    max_span = [0, 0]
    for row_index, (key, original_row, _) in enumerate(rows):
        row = {variable: QDual.coerce(value) for variable, value in original_row.items()}
        factors = []
        while row:
            pivot = min(row)
            if pivot not in pivots:
                break
            multiplier = row[pivot]
            factors.append((pivot, multiplier))
            old_row = pivots[pivot]
            for variable, coefficient in old_row.items():
                value = row.get(variable, QDual()) - multiplier * coefficient
                if value:
                    row[variable] = value
                    max_span[0] = max(max_span[0], value.value.degree_span)
                    max_span[1] = max(max_span[1], value.derivative.degree_span)
                else:
                    row.pop(variable, None)
        if not row:
            records.append((key, "dependent", None, None, factors))
            continue
        pivot = min(row)
        lead = row[pivot]
        assert lead.value
        determinant *= lead
        for factor, multiplicity in qfactor(lead.value.numerator):
            numerator_factors[factor] += multiplicity
        for factor, multiplicity in qfactor(lead.value.denominator):
            denominator_factors[factor] += multiplicity
        if (
            lead.value.numerator.degree() > 0
            or lead.value.denominator.degree() > 0
            or lead.derivative
        ):
            events.append(
                {
                    "row_index": row_index,
                    "key": list(key),
                    "pivot": pivot,
                    "base": repr(lead.value),
                    "dc3": repr(lead.derivative),
                    "base_sha256": sha256(repr(lead.value).encode()).hexdigest(),
                    "dc3_sha256": sha256(repr(lead.derivative).encode()).hexdigest(),
                }
            )
        pivots[pivot] = {
            variable: coefficient / lead for variable, coefficient in row.items()
        }
        records.append((key, "pivot", pivot, lead, factors))
        if row_index % 500 == 0:
            print(
                f"dual_transport rows={row_index};pivots={len(pivots)}",
                flush=True,
            )
    return {
        "pivots": pivots,
        "records": records,
        "numerator_factors": dict(numerator_factors),
        "denominator_factors": dict(denominator_factors),
        "events": events,
        "determinant": determinant,
        "max_span": max_span,
    }


def source_rhs(key):
    return EDual(cp.source_rhs(key))


def propagate(records):
    vector_factory = cp.fast_evec.EVecFactory(cp)

    def vector(value):
        value = EDual.coerce(value)
        return (
            vector_factory.from_frac(value.value),
            vector_factory.from_frac(value.derivative),
        )

    def scale(value, scalar):
        scalar = QDual.coerce(scalar)
        return (
            value[0].scale(scalar.value),
            value[1].scale(scalar.value) + value[0].scale(scalar.derivative),
        )

    def subtract(left, right):
        return (left[0] - right[0], left[1] - right[1])

    pivot_rhs = {}
    compatibility = []
    for key, kind, pivot, lead, factors in records:
        value = vector(source_rhs(key))
        for old, factor in factors:
            value = subtract(value, scale(pivot_rhs[old], factor))
        if kind == "pivot":
            pivot_rhs[pivot] = scale(value, lead.inverse())
        elif value[0] or value[1]:
            compatibility.append((key, value))
    return pivot_rhs, compatibility


def restrict_row(original_row, pivots, pivot_rhs, free_parameter):
    row = {
        variable: QDual.coerce(coefficient)
        for variable, coefficient in original_row.items()
        if coefficient
    }
    vector_factory = next(iter(pivot_rhs.values()))[0].factory
    constant = (vector_factory.zero(), vector_factory.zero())

    def scale(value, scalar):
        scalar = QDual.coerce(scalar)
        return (
            value[0].scale(scalar.value),
            value[1].scale(scalar.value) + value[0].scale(scalar.derivative),
        )
    for pivot in sorted(pivots):
        factor = row.pop(pivot, None)
        if factor is None or not factor:
            continue
        contribution = scale(pivot_rhs[pivot], factor)
        constant = (
            constant[0] + contribution[0],
            constant[1] + contribution[1],
        )
        for variable, coefficient in pivots[pivot].items():
            if variable == pivot:
                continue
            value = row.get(variable, QDual()) - factor * coefficient
            if value:
                row[variable] = value
            else:
                row.pop(variable, None)
    assert all(variable in free_parameter for variable in row)
    return (
        EDual(
            vector_factory.to_frac(constant[0]),
            vector_factory.to_frac(constant[1]),
        ),
        {
            free_parameter[variable]: q_to_e(coefficient)
            for variable, coefficient in row.items()
        },
    )


def section_forms(imax, jmax, exponent, degrees, offset, pivots, pivot_rhs, free_parameter):
    forms = []
    for degree in range(degrees):
        row = fb.x_chart_coefficient(imax, jmax, exponent, degree)
        row = {offset + variable: coefficient for variable, coefficient in row.items()}
        forms.append(restrict_row(row, pivots, pivot_rhs, free_parameter))
    return forms


def pole_forms(imax, jmax, exponent, degrees, offset, pivots, pivot_rhs, free_parameter):
    forms = []
    for degree in range(degrees):
        row = nr.pole_coefficient(imax, jmax, exponent, degree)
        row = {offset + variable: QDual(coefficient) for variable, coefficient in row.items()}
        forms.append(restrict_row(row, pivots, pivot_rhs, free_parameter))
    return forms


def configure_qd():
    qd.Dual = EDual
    qd.B = EDual()
    qd.S = EDual(E(qd.uniform.S_FIELD))
    qd.D = EDual(E(qd.uniform.D_FIELD))
    qd.L = EDual(E(qd.uniform.L_FIELD))
    qd.A = EDual(qd.uniform.A_FIELD)
    qd.Q_PRIME = {0: EDual(1), 24: EDual(25)}
    qd.R = qd.multiply(
        qd.multiply([EDual(-1), EDual(1)], [EDual(-1), EDual(1)]),
        [qd.D, -qd.S, EDual(1)],
    )
    qd.R3, qd.R5 = qd.power(qd.R, 3), qd.power(qd.R, 5)
    qd.POLE_F = {1: -(qd.L**3) * qd.A, 6: qd.L**3}
    qd.POLE_G = {
        0: EDual(Q(5, 9)) * qd.L**5 * qd.A**2,
        5: EDual(Q(-5, 3)) * qd.L**5 * qd.A,
        10: qd.L**5,
    }


def configure_qd_fast():
    """Use the exact tower dual directly while compiling small equations."""
    qd.Dual = FPair
    qd.B = FPair()
    qd.S = FPair(cp.Frac(E(qd.uniform.S_FIELD)))
    qd.D = FPair(cp.Frac(E(qd.uniform.D_FIELD)))
    qd.L = FPair(cp.Frac(E(qd.uniform.L_FIELD)))
    qd.A = FPair(cp.Frac(qd.uniform.A_FIELD))
    qd.Q_PRIME = {0: FPair(1), 24: FPair(25)}
    qd.R = qd.multiply(
        qd.multiply([FPair(-1), FPair(1)], [FPair(-1), FPair(1)]),
        [qd.D, -qd.S, FPair(1)],
    )
    qd.R3, qd.R5 = qd.power(qd.R, 3), qd.power(qd.R, 5)
    qd.POLE_F = {1: -(qd.L**3) * qd.A, 6: qd.L**3}
    qd.POLE_G = {
        0: FPair(Q(5, 9)) * qd.L**5 * qd.A**2,
        5: FPair(Q(-5, 3)) * qd.L**5 * qd.A,
        10: qd.L**5,
    }


def fast_forms(forms):
    return [
        (
            FPair.from_edual(constant),
            {
                parameter: FPair.from_edual(coefficient)
                for parameter, coefficient in coefficients.items()
            },
        )
        for constant, coefficients in forms
    ]


def pack_fast(family, polynomials):
    out = []
    for degree, polynomial in enumerate(polynomials):
        row = {}
        constant = FPair.coerce(polynomial.get((), 0))
        for monomial, coefficient in polynomial.items():
            if monomial:
                assert len(monomial) == 1
                coefficient = FPair.coerce(coefficient)
                if coefficient:
                    row[monomial[0]] = coefficient
        if row or constant:
            out.append(((family, degree), row, -constant))
    return out


def solve(nvariables, rows, certificates=False):
    field_rows = [
        (
            key,
            {variable: FPair.from_edual(coefficient) for variable, coefficient in row.items()},
            FPair.from_edual(rhs),
        )
        for key, row, rhs in rows
    ]
    pivots = {}
    factors = []
    dependent = []
    for row_index, (key, original_row, original_rhs) in enumerate(field_rows):
        row = {variable: coefficient for variable, coefficient in original_row.items() if coefficient}
        rhs = original_rhs
        combination = {row_index: FPair(FAST_FIELD.one, FAST_FIELD.zero)} if certificates else None
        while row:
            pivot = min(row)
            if pivot not in pivots:
                break
            factor = row[pivot]
            old_row, old_rhs, old_combination = pivots[pivot]
            for variable, coefficient in old_row.items():
                value = row.get(variable, FPair()) - factor * coefficient
                if value:
                    row[variable] = value
                else:
                    row.pop(variable, None)
            rhs -= factor * old_rhs
            if certificates:
                for old_index, coefficient in old_combination.items():
                    value = combination.get(old_index, FPair()) - factor * coefficient
                    if value:
                        combination[old_index] = value
                    else:
                        combination.pop(old_index, None)
        if not row:
            if certificates:
                replay_row = {}
                replay_rhs = FPair()
                for original_index, scalar in combination.items():
                    _, source_row, source_rhs = field_rows[original_index]
                    for variable, coefficient in source_row.items():
                        value = replay_row.get(variable, FPair()) + scalar * coefficient
                        if value:
                            replay_row[variable] = value
                        else:
                            replay_row.pop(variable, None)
                    replay_rhs += scalar * source_rhs
                assert not replay_row, ("left-null row replay", key)
                assert replay_rhs == rhs, ("left-null rhs replay", key)
            dependent.append((
                row_index,
                key,
                rhs.to_edual(),
                (
                    {index: coefficient.to_edual() for index, coefficient in combination.items()}
                    if certificates else None
                ),
            ))
            continue
        pivot = min(row)
        lead = row[pivot]
        assert lead.value
        pivots[pivot] = (
            {variable: coefficient / lead for variable, coefficient in row.items()},
            rhs / lead,
            (
                {index: coefficient / lead for index, coefficient in combination.items()}
                if certificates else None
            ),
        )
        factors.append((row_index, key, pivot, lead.to_edual()))
    return pivots, factors, dependent


def parameterize(nvariables, rows):
    pivots, factors, dependent = solve(nvariables, rows)
    assert all(not rhs for _, _, rhs, _ in dependent)
    free = [variable for variable in range(nvariables) if variable not in pivots]
    parameter_of = {variable: index for index, variable in enumerate(free)}
    forms = [None] * nvariables
    for variable in reversed(range(nvariables)):
        if variable in parameter_of:
            forms[variable] = (
                FPair(),
                {parameter_of[variable]: FPair(FAST_FIELD.one, FAST_FIELD.zero)},
            )
            continue
        row, rhs, _ = pivots[variable]
        form = (rhs, {})
        for other, coefficient in row.items():
            if other != variable:
                form = nr.add_affine(form, forms[other], -coefficient)
        forms[variable] = form
    for key, source_row, source_rhs in rows:
        row = {
            variable: FPair.from_edual(coefficient)
            for variable, coefficient in source_row.items()
        }
        rhs = FPair.from_edual(source_rhs)
        replay_constant = FPair()
        replay_directions = {}
        for variable, coefficient in row.items():
            constant, directions = forms[variable]
            replay_constant += coefficient * constant
            for parameter, direction in directions.items():
                value = replay_directions.get(parameter, FPair()) + coefficient * direction
                if value:
                    replay_directions[parameter] = value
                else:
                    replay_directions.pop(parameter, None)
        assert replay_constant == rhs, ("affine constant replay", key)
        assert not replay_directions, ("affine direction replay", key)
    canonical = [
        (
            constant.to_edual(),
            {parameter: coefficient.to_edual() for parameter, coefficient in coefficients.items()},
        )
        for constant, coefficients in forms
    ]
    return canonical, free, factors


def parameterize_qmatrix(nvariables, rows):
    vector_factory = cp.fast_evec.EVecFactory(cp)

    def dual_vector(value):
        value = EDual.coerce(value)
        return (
            vector_factory.from_frac(value.value),
            vector_factory.from_frac(value.derivative),
        )

    def dual_zero():
        return (vector_factory.zero(), vector_factory.zero())

    def dual_add(left, right):
        return (left[0] + right[0], left[1] + right[1])

    def dual_sub(left, right):
        return (left[0] - right[0], left[1] - right[1])

    def dual_scale(value, scalar):
        scalar = QDual.coerce(scalar)
        return (
            value[0].scale(scalar.value),
            value[1].scale(scalar.value) + value[0].scale(scalar.derivative),
        )

    def dual_is_zero(value):
        return not value[0] and not value[1]

    def canonical(value):
        return EDual(
            vector_factory.to_frac(value[0]),
            vector_factory.to_frac(value[1]),
        )

    qrows = [
        (
            key,
            {variable: e_to_q(coefficient) for variable, coefficient in row.items()},
            dual_vector(rhs),
        )
        for key, row, rhs in rows
    ]
    pivots = {}
    factors = []
    dependent = []
    for row_index, (key, original_row, original_rhs) in enumerate(qrows):
        row = dict(original_row)
        rhs = original_rhs
        while row:
            pivot = min(row)
            if pivot not in pivots:
                break
            factor = row[pivot]
            old_row, old_rhs = pivots[pivot]
            for variable, coefficient in old_row.items():
                value = row.get(variable, QDual()) - factor * coefficient
                if value:
                    row[variable] = value
                else:
                    row.pop(variable, None)
            rhs = dual_sub(rhs, dual_scale(old_rhs, factor))
        if not row:
            dependent.append((key, rhs))
            continue
        pivot = min(row)
        lead = row[pivot]
        assert lead.value
        pivots[pivot] = (
            {variable: coefficient / lead for variable, coefficient in row.items()},
            dual_scale(rhs, lead.inverse()),
        )
        factors.append((row_index, key, pivot, q_to_e(lead)))
    assert all(dual_is_zero(rhs) for _, rhs in dependent)

    free = [variable for variable in range(nvariables) if variable not in pivots]
    parameter_of = {variable: index for index, variable in enumerate(free)}
    base_forms = [None] * nvariables
    direction_forms = [None] * nvariables
    for variable in reversed(range(nvariables)):
        if variable in parameter_of:
            base_forms[variable] = dual_zero()
            direction_forms[variable] = {parameter_of[variable]: QDual(1)}
            continue
        row, rhs = pivots[variable]
        base = rhs
        direction = {}
        for other, coefficient in row.items():
            if other == variable:
                continue
            base = dual_sub(base, dual_scale(base_forms[other], coefficient))
            for parameter, old in direction_forms[other].items():
                value = direction.get(parameter, QDual()) - coefficient * old
                if value:
                    direction[parameter] = value
                else:
                    direction.pop(parameter, None)
        base_forms[variable] = base
        direction_forms[variable] = direction
    forms = [
        (
            canonical(base_forms[variable]),
            {parameter: q_to_e(coefficient) for parameter, coefficient in direction_forms[variable].items()},
        )
        for variable in range(nvariables)
    ]
    return forms, free, factors


def compose(forms, parameter_forms):
    field_parameters = [
        (
            FPair.from_edual(constant),
            {
                parameter: FPair.from_edual(coefficient)
                for parameter, coefficient in coefficients.items()
            },
        )
        for constant, coefficients in parameter_forms
    ]
    out = []
    for constant, coefficients in forms:
        out_constant = FPair.from_edual(constant)
        out_coefficients = {}
        for parameter, coefficient in coefficients.items():
            scalar = FPair.from_edual(coefficient)
            inner_constant, inner_coefficients = field_parameters[parameter]
            out_constant += scalar * inner_constant
            for inner_parameter, inner_coefficient in inner_coefficients.items():
                value = (
                    out_coefficients.get(inner_parameter, FPair())
                    + scalar * inner_coefficient
                )
                if value:
                    out_coefficients[inner_parameter] = value
                else:
                    out_coefficients.pop(inner_parameter, None)
        out.append((
            out_constant.to_edual(),
            {
                parameter: coefficient.to_edual()
                for parameter, coefficient in out_coefficients.items()
            },
        ))
    return out


def poly_derivative(poly):
    poly = cp.Poly(poly)
    return cp.Poly([
        (index + 1) * poly.coefficients[index + 1]
        for index in range(max(0, len(poly.coefficients) - 1))
    ])


def frac_derivative(value):
    value = cp.Frac.coerce(value)
    return cp.Frac(
        poly_derivative(value.numerator) * value.denominator
        - value.numerator * poly_derivative(value.denominator),
        value.denominator * value.denominator,
    )


def rat_derivative(value):
    value = rt.Rat.coerce(value)
    return rt.Rat(
        value.numerator.derivative() * value.denominator
        - value.numerator * value.denominator.derivative(),
        value.denominator * value.denominator,
    )


def field_derivative(value):
    value = cp.fast_efield.EField.coerce(value, FAST_FIELD)
    return cp.fast_efield.EField(FAST_FIELD, tuple(
        cp.fast_efield.KField(
            FAST_FIELD,
            tuple(rat_derivative(coordinate) for coordinate in coefficient.coordinates),
        )
        for coefficient in value.coefficients
    ))


def field_gcd_numerators(values):
    gcd = None
    for value in values:
        if not value:
            continue
        reduced = cp.reduce_frac_fast(FAST_FIELD.to_frac(value))
        numerator = reduced.numerator
        gcd = numerator if gcd is None else cp.poly_gcd_fast(gcd, numerator)
        if gcd.degree == 0:
            return cp.Poly(1)
    if gcd is None:
        return cp.Poly()
    return cp.poly_gcd_fast(gcd, cp.Poly())


def gcd_numerators(values):
    values = [cp.Frac.coerce(value).numerator for value in values if value]
    if not values:
        return cp.Poly()
    out = values[0]
    for value in values[1:]:
        out = cp.poly_gcd(out, value)
    return cp.poly_monic(out)


def determinant3(rows):
    (a, b, c), (d, e, f), (g, h, i) = rows
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def factor_record(stage, factors):
    out = []
    for row_index, key, pivot, lead in factors:
        lead = EDual.coerce(lead)
        out.append(
            {
                "stage": stage,
                "row_index": row_index,
                "key": list(key),
                "pivot": pivot,
                "base": cp.frac_record(lead.value),
                "dc3": cp.frac_record(lead.derivative),
            }
        )
    return out


def exceptional_summary(factor_records):
    values = {}
    denominators = {}
    for record in factor_records:
        for target, field in ((values, "base"),):
            value = record[field]
            numerator = value["numerator"]
            denominator = value["denominator"]
            if numerator["degree"] > 0:
                target.setdefault(numerator["sha256"], numerator)
            if denominator["degree"] > 0:
                denominators.setdefault(denominator["sha256"], denominator)
    return {
        "pivot_numerator_polynomials": list(values.values()),
        "pivot_denominator_polynomials": list(denominators.values()),
    }


def main():
    special = None
    if len(sys.argv) == 3 and sys.argv[1] == "--special":
        special = Q(sys.argv[2])
    elif len(sys.argv) != 1:
        raise SystemExit("usage: c1_c3_thickening.py [--special 0|3]")

    Cq = rt.Rat(rt.X) if special is None else rt.Rat(special)
    fb.CENTER = (QDual(Cq), QDual(1), QDual(1, 1))
    fb._X_POWER_CACHE.clear()
    nf, rows_f = fb.build_transport(
        15, 60, 3, {15: Q(1)}, fb.F1_F_PATTERN, fb.POLE_F_PATTERN
    )
    ng, rows_g = fb.build_transport(
        25, 100, 5, {1: Q(1), 25: Q(1)}, fb.F1_G_PATTERN, fb.POLE_G_PATTERN
    )
    transport = [(('f',) + key, row, rhs) for key, row, rhs in rows_f]
    transport += [
        (('g',) + key, {nf + variable: coefficient for variable, coefficient in row.items()}, rhs)
        for key, row, rhs in rows_g
    ]
    transport_data = factor_transport(transport)
    pivot_rhs, transport_compatibility = propagate(transport_data["records"])
    assert not transport_compatibility and len(transport_data["pivots"]) == 3470
    free = [variable for variable in range(nf + ng) if variable not in transport_data["pivots"]]
    free_parameter = {variable: index for index, variable in enumerate(free)}
    assert len(free) == 132
    print("c1+c3 transport dual PASS", flush=True)

    bands132 = {
        (owner, exponent): section_forms(
            15 if owner == "f" else 25,
            60 if owner == "f" else 100,
            exponent,
            16 if owner == "f" else 26,
            0 if owner == "f" else nf,
            transport_data["pivots"], pivot_rhs, free_parameter,
        )
        for owner in ("f", "g") for exponent in (1, 2, 3)
    }
    pole_f132 = pole_forms(15, 60, -2, 61, 0, transport_data["pivots"], pivot_rhs, free_parameter)
    pole_g132 = pole_forms(25, 100, -4, 101, nf, transport_data["pivots"], pivot_rhs, free_parameter)
    print("c1+c3 transport sections PASS", flush=True)

    configure_qd()
    first_rows = qd.pack("X-2", qd.first_band_polynomials(bands132[("f", 1)], bands132[("g", 1)]))
    forms94, free94, factors_first = parameterize_qmatrix(132, first_rows)
    assert (len(factors_first), len(free94)) == (38, 94)
    print("c1+c3 first dual PASS", flush=True)

    bands94 = {key: compose(forms, forms94) for key, forms in bands132.items()}
    pole_f94 = compose(pole_f132, forms94)
    pole_g94 = compose(pole_g132, forms94)
    configure_qd_fast()
    fast_bands94 = {key: fast_forms(forms) for key, forms in bands94.items()}
    previous_rows = pack_fast(
        "X-1",
        qd.compile_previous(
            fast_bands94[("f", 1)], fast_bands94[("f", 2)],
            fast_bands94[("g", 1)], fast_bands94[("g", 2)],
        ),
    )
    previous_rows += pack_fast(
        "P1",
        qd.compile_pole_previous(fast_forms(pole_f94), fast_forms(pole_g94)),
    )
    forms56, free56, factors_previous = parameterize(94, previous_rows)
    assert (len(factors_previous), len(free56)) == (38, 56)
    print("c1+c3 previous dual PASS", flush=True)

    bands56 = {key: compose(forms, forms56) for key, forms in bands94.items()}
    fast_bands56 = {key: fast_forms(forms) for key, forms in bands56.items()}
    current_rows = pack_fast(
        "X0",
        qd.compile_current(
            *[fast_bands56[("f", exponent)] for exponent in (1, 2, 3)],
            *[fast_bands56[("g", exponent)] for exponent in (1, 2, 3)],
        ),
    )
    current_pivots, factors_current, dependent = solve(56, current_rows, certificates=True)
    assert len(current_pivots) == 25
    compatibility = [entry for entry in dependent if entry[2]]
    assert len(compatibility) == 10

    base = [cp.reduce_frac_fast(entry[2].value) for entry in compatibility]
    dc3 = [cp.reduce_frac_fast(entry[2].derivative) for entry in compatibility]
    base_field = [FAST_FIELD.from_frac(value) for value in base]
    dc3_field = [FAST_FIELD.from_frac(value) for value in dc3]
    dc1_field = [field_derivative(value) for value in base_field]
    dc1 = [cp.reduce_frac_fast(FAST_FIELD.to_frac(value)) for value in dc1_field]
    tangent_minors = [
        dc1_field[i] * dc3_field[j] - dc1_field[j] * dc3_field[i]
        for i, j in combinations(range(len(base)), 2)
    ]
    augmented_minors = [
        determinant3([
            (dc1_field[i], dc3_field[i], base_field[i]),
            (dc1_field[j], dc3_field[j], base_field[j]),
            (dc1_field[k], dc3_field[k], base_field[k]),
        ])
        for i, j, k in combinations(range(len(base)), 3)
    ]
    fitting = {
        "compatibility_base_gcd": cp.poly_record(field_gcd_numerators(base_field)),
        "dc3_sensitivity_gcd": cp.poly_record(field_gcd_numerators(dc3_field)),
        "two_direction_2x2_minor_count": len(tangent_minors),
        "two_direction_nonzero_2x2_count": sum(bool(value) for value in tangent_minors),
        "two_direction_minor_gcd": cp.poly_record(field_gcd_numerators(tangent_minors)),
        "affine_augmented_3x3_minor_count": len(augmented_minors),
        "affine_augmented_nonzero_3x3_count": sum(bool(value) for value in augmented_minors),
        "affine_augmented_minor_gcd": cp.poly_record(field_gcd_numerators(augmented_minors)),
    }

    later_factors = (
        factor_record("first", factors_first)
        + factor_record("previous_pole", factors_previous)
        + factor_record("current", factors_current)
    )
    output = {
        "verdict": "TD6-C1-C3-FIRST-INFINITESIMAL-DISCRIMINATOR",
        "scope": {
            "base_line": f"c1={'C' if special is None else special},c2=1,c3=1",
            "dual_direction": "dc3",
            "ring": "E(C)[eps]/eps^2" if special is None else "E[eps]/eps^2",
            "full_bivariate_coverage": False,
            "both_charts_retained": True,
            "new_noncentering_modulus_forced": False,
        },
        "ranks": {
            "transport": [len(transport_data["pivots"]), nf + ng],
            "first": [len(factors_first), 132],
            "previous_pole": [len(factors_previous), 94],
            "current": [len(current_pivots), 56],
        },
        "transport": {
            "numerator_factors": transport_data["numerator_factors"],
            "denominator_factors": transport_data["denominator_factors"],
            "pivot_events": transport_data["events"],
            "max_degree_span_base_dc3": transport_data["max_span"],
            "selected_minor_base": repr(transport_data["determinant"].value),
            "selected_minor_dc3": repr(transport_data["determinant"].derivative),
            "selected_minor_base_sha256": sha256(repr(transport_data["determinant"].value).encode()).hexdigest(),
            "selected_minor_dc3_sha256": sha256(repr(transport_data["determinant"].derivative).encode()).hexdigest(),
        },
        "later_pivots": later_factors,
        "later_exceptional_polynomials": exceptional_summary(later_factors),
        "compatibility": [
            {
                "row_index": row_index,
                "key": list(key),
                "base": cp.frac_record(base[index]),
                "dc1": cp.frac_record(dc1[index]),
                "dc3": cp.frac_record(dc3[index]),
                "left_null_support": len(combination),
                "left_null_sha256": sha256(repr(sorted(combination.items())).encode()).hexdigest(),
            }
            for index, (row_index, key, residual, combination) in enumerate(compatibility)
        ],
        "localized_fitting": fitting,
        "exceptional_strata_rebuilt": [] if special is None else [str(special)],
        "family_killed": False,
        "SP2_killed": False,
        "JC2_resolved": False,
    }
    print(json.dumps(output, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
