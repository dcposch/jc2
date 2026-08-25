#!/usr/bin/env python3
"""Exact staged TD6 c1 pencil over E(C), generic rank stratum.

The 3602-variable transport matrix is factored over Q(C).  Only requested
boundary sections are pulled back to its 132-dimensional affine kernel.
All later elimination is exact over E(C); no point interpolation is used.
"""

from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys


PRIVATE = Path(__file__).resolve().parent
REPO = Path(__file__).resolve().parents[2]
QDUAL_PATH = REPO / "cases/td6_jet_orbit_adjoint_20260824/replay.py"
QDUAL_SHA = "fb138b0f59e611bab365f37c0302418eda485318beec3f6b21237a95fdc41198"
RATIONAL_PATH = PRIVATE / "c1_rational_transport.py"
FAST_EVEC_PATH = PRIVATE / "fast_evec.py"
FAST_EFIELD_PATH = PRIVATE / "fast_efield.py"


def load(name, path, expected=None):
    if expected is not None:
        assert sha256(path.read_bytes()).hexdigest() == expected
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


qd = load("td6_qdual_c1_pencil", QDUAL_PATH, QDUAL_SHA)
rt = load("td6_c1_rational_transport", RATIONAL_PATH)
fast_evec = load("td6_fast_evec", FAST_EVEC_PATH)
fast_efield = load("td6_fast_efield", FAST_EFIELD_PATH)
fb, nr, E, K = qd.fb, qd.nr, qd.E, qd.K


class Poly:
    """Dense univariate polynomial over the exact degree-18 field E."""

    __slots__ = ("coefficients",)

    def __init__(self, value=0):
        if isinstance(value, Poly):
            self.coefficients = value.coefficients
            return
        if isinstance(value, (list, tuple)):
            coefficients = [E(entry) for entry in value]
        else:
            coefficients = [E(value)]
        while coefficients and not coefficients[-1]:
            coefficients.pop()
        self.coefficients = tuple(coefficients)

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Poly) else Poly(value)

    @property
    def degree(self):
        return len(self.coefficients) - 1

    @property
    def constant(self):
        return self.coefficients[0] if self.coefficients else E(0)

    @property
    def leading(self):
        return self.coefficients[-1] if self.coefficients else E(0)

    def __add__(self, other):
        other = Poly.coerce(other)
        values = [E(0)] * max(len(self.coefficients), len(other.coefficients))
        for index in range(len(values)):
            if index < len(self.coefficients):
                values[index] += self.coefficients[index]
            if index < len(other.coefficients):
                values[index] += other.coefficients[index]
        return Poly(values)

    __radd__ = __add__

    def __neg__(self):
        return Poly([-entry for entry in self.coefficients])

    def __sub__(self, other):
        return self + (-Poly.coerce(other))

    def __rsub__(self, other):
        return Poly.coerce(other) - self

    def __mul__(self, other):
        other = Poly.coerce(other)
        if not self or not other:
            return Poly()
        values = [E(0)] * (len(self.coefficients) + len(other.coefficients) - 1)
        for i, left in enumerate(self.coefficients):
            if left:
                for j, right in enumerate(other.coefficients):
                    if right:
                        values[i + j] += left * right
        return Poly(values)

    __rmul__ = __mul__

    def __pow__(self, exponent):
        assert exponent >= 0
        out = Poly(1)
        base = self
        while exponent:
            if exponent & 1:
                out *= base
            base *= base
            exponent //= 2
        return out

    def __bool__(self):
        return bool(self.coefficients)

    def __eq__(self, other):
        return self.coefficients == Poly.coerce(other).coefficients

    def __repr__(self):
        return "Poly(" + ",".join(map(repr, self.coefficients)) + ")"


ONE_POLY = Poly(1)


def poly_divmod(dividend, divisor):
    dividend, divisor = Poly(dividend), Poly(divisor)
    assert divisor
    quotient = [E(0)] * max(0, dividend.degree - divisor.degree + 1)
    remainder = dividend
    inverse_lead = divisor.leading.inverse()
    while remainder and remainder.degree >= divisor.degree:
        degree = remainder.degree - divisor.degree
        coefficient = remainder.leading * inverse_lead
        quotient[degree] += coefficient
        remainder -= Poly([E(0)] * degree + [coefficient]) * divisor
    return Poly(quotient), remainder


def poly_exact_div(dividend, divisor):
    quotient, remainder = poly_divmod(dividend, divisor)
    assert not remainder
    return quotient


def poly_monic(poly):
    poly = Poly(poly)
    return poly * poly.leading.inverse() if poly else poly


def poly_gcd(left, right):
    left, right = Poly(left), Poly(right)
    while right:
        _, remainder = poly_divmod(left, right)
        left, right = right, remainder
    return poly_monic(left)


class Frac:
    """Reduced element of E(C)."""

    __slots__ = ("numerator", "denominator")

    def __init__(self, value=0, denominator=None, *, normalized=False):
        if isinstance(value, Frac) and denominator is None:
            self.numerator = value.numerator
            self.denominator = value.denominator
            return
        numerator = Poly(value)
        denominator = ONE_POLY if denominator is None else Poly(denominator)
        if not denominator:
            raise ZeroDivisionError
        if not numerator:
            self.numerator = Poly()
            self.denominator = ONE_POLY
            return
        if not normalized:
            if denominator.degree == 0:
                scale = denominator.constant.inverse()
                numerator *= scale
                denominator = ONE_POLY
            else:
                common = poly_gcd(numerator, denominator)
                if common.degree > 0:
                    numerator = poly_exact_div(numerator, common)
                    denominator = poly_exact_div(denominator, common)
                scale = denominator.leading.inverse()
                numerator *= scale
                denominator *= scale
        self.numerator = numerator
        self.denominator = denominator

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Frac) else Frac(value)

    def __add__(self, other):
        other = Frac.coerce(other)
        if not self:
            return other
        if not other:
            return self
        if self.denominator == other.denominator:
            return Frac(self.numerator + other.numerator, self.denominator)
        return Frac(
            self.numerator * other.denominator
            + other.numerator * self.denominator,
            self.denominator * other.denominator,
        )

    __radd__ = __add__

    def __neg__(self):
        return Frac(-self.numerator, self.denominator, normalized=True)

    def __sub__(self, other):
        return self + (-Frac.coerce(other))

    def __rsub__(self, other):
        return Frac.coerce(other) - self

    def __mul__(self, other):
        other = Frac.coerce(other)
        if not self or not other:
            return Frac()
        left_common = poly_gcd(self.numerator, other.denominator)
        right_common = poly_gcd(other.numerator, self.denominator)
        left_num = poly_exact_div(self.numerator, left_common)
        right_den = poly_exact_div(other.denominator, left_common)
        right_num = poly_exact_div(other.numerator, right_common)
        left_den = poly_exact_div(self.denominator, right_common)
        return Frac(
            left_num * right_num,
            left_den * right_den,
            normalized=True,
        )

    __rmul__ = __mul__

    def inverse(self):
        if not self:
            raise ZeroDivisionError
        scale = self.numerator.leading.inverse()
        return Frac(
            self.denominator * scale,
            self.numerator * scale,
            normalized=True,
        )

    def __truediv__(self, other):
        return self * Frac.coerce(other).inverse()

    def __rtruediv__(self, other):
        return Frac.coerce(other) / self

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        out = Frac(1)
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
        other = Frac.coerce(other)
        return (
            self.numerator == other.numerator
            and self.denominator == other.denominator
        )

    def __repr__(self):
        return f"Frac(({self.numerator!r})/({self.denominator!r}))"


LIFT_CACHE = {}


def q_to_fraction(value):
    return Q(int(value.p), int(value.q))


def lift_qpoly(poly):
    return Poly([
        E(q_to_fraction(poly[index])) for index in range(poly.degree() + 1)
    ]) if poly else Poly()


def lift_rat(value):
    value = rt.Rat.coerce(value)
    key = (str(value.numerator), str(value.denominator))
    if key not in LIFT_CACHE:
        LIFT_CACHE[key] = Frac(
            lift_qpoly(value.numerator), lift_qpoly(value.denominator)
        )
    return LIFT_CACHE[key]


def e_to_q(value):
    """Return the rational represented by value, asserting value is in Q."""
    value = E(value)
    assert not value.coefficients[1] and not value.coefficients[2]
    coefficient = value.coefficients[0]
    assert not any(coefficient.coefficients[1:])
    return coefficient.coefficients[0]


def poly_to_qpoly(poly):
    poly = Poly(poly)
    return rt.fmpq_poly([
        rt.rational(e_to_q(entry)) for entry in poly.coefficients
    ])


def frac_to_rat(value):
    """Descend an E(C) value known structurally to lie in Q(C)."""
    value = Frac(value)
    return rt.Rat(
        poly_to_qpoly(value.numerator),
        poly_to_qpoly(value.denominator),
    )


FAST_FIELD = fast_efield.EFieldFactory(sys.modules[__name__])


class FScalar:
    """Exact fast E(C) scalar for compiling the small polynomial stages."""

    __slots__ = ("value",)

    def __init__(self, value=0):
        if isinstance(value, FScalar):
            self.value = value.value
        elif isinstance(value, fast_efield.EField):
            assert value.factory is FAST_FIELD
            self.value = value
        else:
            self.value = FAST_FIELD.from_frac(Frac.coerce(value))

    @staticmethod
    def coerce(value):
        return value if isinstance(value, FScalar) else FScalar(value)

    def to_frac(self):
        return FAST_FIELD.to_frac(self.value)

    def __add__(self, other):
        return FScalar(self.value + FScalar.coerce(other).value)

    __radd__ = __add__

    def __neg__(self):
        return FScalar(-self.value)

    def __sub__(self, other):
        return self + (-FScalar.coerce(other))

    def __rsub__(self, other):
        return FScalar.coerce(other) - self

    def __mul__(self, other):
        return FScalar(self.value * FScalar.coerce(other).value)

    __rmul__ = __mul__

    def inverse(self):
        return FScalar(self.value.inverse())

    def __truediv__(self, other):
        return self * FScalar.coerce(other).inverse()

    def __rtruediv__(self, other):
        return FScalar.coerce(other) / self

    def __pow__(self, exponent):
        return FScalar(self.value ** exponent)

    def __bool__(self):
        return bool(self.value)

    def __eq__(self, other):
        return self.value == FScalar.coerce(other).value


def source_rhs(key):
    return E(qd.source_rhs(key).value)


def propagate(records):
    vector_factory = fast_evec.EVecFactory(sys.modules[__name__])
    pivot_rhs = {}
    compatibility = []
    for key, kind, pivot, lead, factors in records:
        value = vector_factory.from_frac(Frac(source_rhs(key)))
        for old, factor in factors:
            value -= pivot_rhs[old].scale(factor)
        if kind == "pivot":
            pivot_rhs[pivot] = value.scale(lead.inverse())
        elif value:
            compatibility.append((key, value))
    return pivot_rhs, compatibility


def restrict_row(original_row, pivots, pivot_rhs, free_parameter):
    row = {
        variable: rt.Rat.coerce(coefficient)
        for variable, coefficient in original_row.items()
        if coefficient
    }
    vector_factory = next(iter(pivot_rhs.values())).factory
    constant = vector_factory.zero()
    for pivot in sorted(pivots):
        factor = row.pop(pivot, None)
        if factor is None or not factor:
            continue
        constant += pivot_rhs[pivot].scale(factor)
        for variable, coefficient in pivots[pivot].items():
            if variable == pivot:
                continue
            value = row.get(variable, rt.Rat()) - factor * coefficient
            if value:
                row[variable] = value
            else:
                row.pop(variable, None)
    assert all(variable in free_parameter for variable in row)
    return (
        vector_factory.to_frac(constant),
        {
            free_parameter[variable]: lift_rat(coefficient)
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
        row = {offset + variable: rt.Rat(coefficient) for variable, coefficient in row.items()}
        forms.append(restrict_row(row, pivots, pivot_rhs, free_parameter))
    return forms


def configure_qd():
    qd.Dual = Frac
    qd.B = Frac()
    qd.S = Frac(E(qd.uniform.S_FIELD))
    qd.D = Frac(E(qd.uniform.D_FIELD))
    qd.L = Frac(E(qd.uniform.L_FIELD))
    qd.A = Frac(qd.uniform.A_FIELD)
    qd.Q_PRIME = {0: Frac(1), 24: Frac(25)}
    qd.R = qd.multiply(
        qd.multiply([Frac(-1), Frac(1)], [Frac(-1), Frac(1)]),
        [qd.D, -qd.S, Frac(1)],
    )
    qd.R3, qd.R5 = qd.power(qd.R, 3), qd.power(qd.R, 5)
    qd.POLE_F = {1: -(qd.L**3) * qd.A, 6: qd.L**3}
    qd.POLE_G = {
        0: Frac(Q(5, 9)) * qd.L**5 * qd.A**2,
        5: Frac(Q(-5, 3)) * qd.L**5 * qd.A,
        10: qd.L**5,
    }


def configure_qd_fast():
    qd.Dual = FScalar
    qd.B = FScalar()
    qd.S = FScalar(Frac(E(qd.uniform.S_FIELD)))
    qd.D = FScalar(Frac(E(qd.uniform.D_FIELD)))
    qd.L = FScalar(Frac(E(qd.uniform.L_FIELD)))
    qd.A = FScalar(Frac(qd.uniform.A_FIELD))
    qd.Q_PRIME = {0: FScalar(1), 24: FScalar(25)}
    qd.R = qd.multiply(
        qd.multiply([FScalar(-1), FScalar(1)], [FScalar(-1), FScalar(1)]),
        [qd.D, -qd.S, FScalar(1)],
    )
    qd.R3, qd.R5 = qd.power(qd.R, 3), qd.power(qd.R, 5)
    qd.POLE_F = {1: -(qd.L**3) * qd.A, 6: qd.L**3}
    qd.POLE_G = {
        0: FScalar(Q(5, 9)) * qd.L**5 * qd.A**2,
        5: FScalar(Q(-5, 3)) * qd.L**5 * qd.A,
        10: qd.L**5,
    }


def fast_forms(forms):
    return [
        (
            FScalar(constant),
            {
                parameter: FScalar(coefficient)
                for parameter, coefficient in coefficients.items()
            },
        )
        for constant, coefficients in forms
    ]


def pack_fast(family, polynomials):
    out = []
    for degree, polynomial in enumerate(polynomials):
        row = {}
        constant = FScalar.coerce(polynomial.get((), 0))
        for monomial, coefficient in polynomial.items():
            if monomial:
                assert len(monomial) == 1
                coefficient = FScalar.coerce(coefficient)
                if coefficient:
                    row[monomial[0]] = coefficient
        if row or constant:
            out.append(((family, degree), row, -constant))
    return out


def solve(nvariables, rows, certificates=False):
    pivots = {}
    factors = []
    dependent = []
    for row_index, (key, original_row, original_rhs) in enumerate(rows):
        row = {
            variable: Frac.coerce(coefficient)
            for variable, coefficient in original_row.items()
            if coefficient
        }
        rhs = Frac.coerce(original_rhs)
        combination = {row_index: Frac(1)} if certificates else None
        while row:
            pivot = min(row)
            if pivot not in pivots:
                break
            factor = row[pivot]
            old_row, old_rhs, old_combination = pivots[pivot]
            for variable, coefficient in old_row.items():
                value = row.get(variable, Frac()) - factor * coefficient
                if value:
                    row[variable] = value
                else:
                    row.pop(variable, None)
            rhs -= factor * old_rhs
            if certificates:
                for old_index, coefficient in old_combination.items():
                    value = combination.get(old_index, Frac()) - factor * coefficient
                    if value:
                        combination[old_index] = value
                    else:
                        combination.pop(old_index, None)
        if not row:
            dependent.append((row_index, key, rhs, combination))
            continue
        pivot = min(row)
        lead = row[pivot]
        normalized_row = {
            variable: coefficient / lead for variable, coefficient in row.items()
        }
        normalized_rhs = rhs / lead
        normalized_combination = (
            {index: coefficient / lead for index, coefficient in combination.items()}
            if certificates else None
        )
        pivots[pivot] = (normalized_row, normalized_rhs, normalized_combination)
        factors.append((row_index, key, pivot, lead))
    return pivots, factors, dependent


def parameterize(nvariables, rows):
    factory = FAST_FIELD

    def field_value(value):
        return value.value if isinstance(value, FScalar) else factory.from_frac(value)

    field_rows = [
        (
            key,
            {variable: field_value(coefficient) for variable, coefficient in row.items()},
            field_value(rhs),
        )
        for key, row, rhs in rows
    ]
    pivots = {}
    factors = []
    dependent = []
    for row_index, (key, original_row, original_rhs) in enumerate(field_rows):
        row = dict(original_row)
        rhs = original_rhs
        while row:
            pivot = min(row)
            if pivot not in pivots:
                break
            factor = row[pivot]
            old_row, old_rhs = pivots[pivot]
            for variable, coefficient in old_row.items():
                value = row.get(variable, factory.zero) - factor * coefficient
                if value:
                    row[variable] = value
                else:
                    row.pop(variable, None)
            rhs -= factor * old_rhs
        if not row:
            dependent.append((key, rhs))
            continue
        pivot = min(row)
        lead = row[pivot]
        pivots[pivot] = (
            {variable: coefficient / lead for variable, coefficient in row.items()},
            rhs / lead,
        )
        factors.append((row_index, key, pivot, factory.to_frac(lead)))
    assert all(not rhs for _, rhs in dependent)

    free = [variable for variable in range(nvariables) if variable not in pivots]
    parameter_of = {variable: index for index, variable in enumerate(free)}
    forms = [None] * nvariables
    for variable in reversed(range(nvariables)):
        if variable in parameter_of:
            forms[variable] = (factory.zero, {parameter_of[variable]: factory.one})
            continue
        row, rhs = pivots[variable]
        form = (rhs, {})
        for other, coefficient in row.items():
            if other != variable:
                form = nr.add_affine(form, forms[other], -coefficient)
        forms[variable] = form
    for key, row, rhs in field_rows:
        got = (factory.zero, {})
        for variable, coefficient in row.items():
            got = nr.add_affine(got, forms[variable], coefficient)
        assert got == (rhs, {}), ("row replay", key)
    canonical_forms = [
        (
            factory.to_frac(constant),
            {parameter: factory.to_frac(coefficient) for parameter, coefficient in coefficients.items()},
        )
        for constant, coefficients in forms
    ]
    return canonical_forms, free, factors


def solve_efield(nvariables, rows, certificates=False):
    """Exact small-stage solve in the fast tower field, canonicalized at exit."""
    factory = FAST_FIELD

    def field_value(value):
        return value.value if isinstance(value, FScalar) else factory.from_frac(value)

    field_rows = [
        (
            key,
            {variable: field_value(coefficient) for variable, coefficient in row.items()},
            field_value(rhs),
        )
        for key, row, rhs in rows
    ]
    pivots = {}
    factors = []
    dependent = []
    for row_index, (key, original_row, original_rhs) in enumerate(field_rows):
        row = dict(original_row)
        rhs = original_rhs
        combination = {row_index: factory.one} if certificates else None
        while row:
            pivot = min(row)
            if pivot not in pivots:
                break
            factor = row[pivot]
            old_row, old_rhs, old_combination = pivots[pivot]
            for variable, coefficient in old_row.items():
                value = row.get(variable, factory.zero) - factor * coefficient
                if value:
                    row[variable] = value
                else:
                    row.pop(variable, None)
            rhs -= factor * old_rhs
            if certificates:
                for old_index, coefficient in old_combination.items():
                    value = combination.get(old_index, factory.zero) - factor * coefficient
                    if value:
                        combination[old_index] = value
                    else:
                        combination.pop(old_index, None)
        if not row:
            dependent.append((
                row_index,
                key,
                factory.to_frac(rhs),
                (
                    {index: factory.to_frac(value) for index, value in combination.items()}
                    if certificates else None
                ),
            ))
            continue
        pivot = min(row)
        lead = row[pivot]
        pivots[pivot] = (
            {variable: coefficient / lead for variable, coefficient in row.items()},
            rhs / lead,
            (
                {index: coefficient / lead for index, coefficient in combination.items()}
                if certificates else None
            ),
        )
        factors.append((row_index, key, pivot, factory.to_frac(lead)))
    return pivots, factors, dependent


def parameterize_qmatrix(nvariables, rows):
    """Fast exact parameterization when the matrix is over Q(C).

    The affine RHS stays in E(C).  Homogeneous directions are back-solved
    over FLINT-backed Q(C), avoiding degree-18 arithmetic on millions of
    direction coefficients at the first-J stage.
    """
    # Particular-solution arithmetic is only Q(C)-linear here.  Representing
    # E(C) as 18 exact Q(C) coordinates avoids thousands of polynomial gcds
    # over the degree-18 field during the dense backsolve.
    vector_factory = fast_evec.EVecFactory(sys.modules[__name__])

    qrows = [
        (
            key,
            {variable: frac_to_rat(coefficient) for variable, coefficient in row.items()},
            vector_factory.from_frac(Frac.coerce(rhs)),
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
                value = row.get(variable, rt.Rat()) - factor * coefficient
                if value:
                    row[variable] = value
                else:
                    row.pop(variable, None)
            rhs -= old_rhs.scale(factor)
        if not row:
            dependent.append((key, rhs))
            continue
        pivot = min(row)
        lead = row[pivot]
        normalized_row = {
            variable: coefficient / lead for variable, coefficient in row.items()
        }
        normalized_rhs = rhs.scale(lead.inverse())
        pivots[pivot] = (normalized_row, normalized_rhs)
        factors.append((row_index, key, pivot, lift_rat(lead)))
    assert all(not rhs for _, rhs in dependent)

    free = [variable for variable in range(nvariables) if variable not in pivots]
    parameter_of = {variable: index for index, variable in enumerate(free)}
    base_forms = [None] * nvariables
    direction_forms = [None] * nvariables
    for variable in reversed(range(nvariables)):
        if variable in parameter_of:
            base_forms[variable] = vector_factory.zero()
            direction_forms[variable] = {parameter_of[variable]: rt.Rat(1)}
            continue
        row, rhs = pivots[variable]
        base = rhs
        direction = {}
        for other, coefficient in row.items():
            if other == variable:
                continue
            base -= base_forms[other].scale(coefficient)
            for parameter, old in direction_forms[other].items():
                value = direction.get(parameter, rt.Rat()) - coefficient * old
                if value:
                    direction[parameter] = value
                else:
                    direction.pop(parameter, None)
        base_forms[variable] = base
        direction_forms[variable] = direction

    # Replay separately in E(C) on the particular solution and Q(C) on every
    # homogeneous direction before lifting the compact result.
    for key, row, rhs in qrows:
        base = vector_factory.zero()
        direction = {}
        for variable, coefficient in row.items():
            base += base_forms[variable].scale(coefficient)
            for parameter, old in direction_forms[variable].items():
                value = direction.get(parameter, rt.Rat()) + coefficient * old
                if value:
                    direction[parameter] = value
                else:
                    direction.pop(parameter, None)
        assert base == rhs and not direction, ("qmatrix replay", key)

    forms = [
        (
            vector_factory.to_frac(base_forms[variable]),
            {
                parameter: lift_rat(coefficient)
                for parameter, coefficient in direction_forms[variable].items()
            },
        )
        for variable in range(nvariables)
    ]
    return forms, free, factors


def compose(forms, parameter_forms):
    factory = FAST_FIELD
    field_parameters = [
        (
            factory.from_frac(constant),
            {
                parameter: factory.from_frac(coefficient)
                for parameter, coefficient in coefficients.items()
            },
        )
        for constant, coefficients in parameter_forms
    ]
    out = []
    for constant, coefficients in forms:
        out_constant = factory.from_frac(constant)
        out_coefficients = {}
        for parameter, coefficient in coefficients.items():
            scalar = factory.from_frac(coefficient)
            inner_constant, inner_coefficients = field_parameters[parameter]
            out_constant += scalar * inner_constant
            for inner_parameter, inner_coefficient in inner_coefficients.items():
                value = (
                    out_coefficients.get(inner_parameter, factory.zero)
                    + scalar * inner_coefficient
                )
                if value:
                    out_coefficients[inner_parameter] = value
                else:
                    out_coefficients.pop(inner_parameter, None)
        out.append((
            factory.to_frac(out_constant),
            {
                parameter: factory.to_frac(coefficient)
                for parameter, coefficient in out_coefficients.items()
            },
        ))
    return out


def _fast_constant_poly(poly):
    poly = Poly(poly)
    return [FAST_FIELD.from_e(coefficient) for coefficient in poly.coefficients]


def _poly_from_fast_constants(coefficients):
    values = []
    for coefficient in coefficients:
        value = FAST_FIELD.to_frac(coefficient)
        assert value.denominator == ONE_POLY
        values.append(value.numerator.constant if value.numerator else E(0))
    return Poly(values)


def poly_gcd_fast(left, right):
    left = _fast_constant_poly(left)
    right = _fast_constant_poly(right)
    if not left:
        if not right:
            return Poly()
        scale = right[-1].inverse()
        return _poly_from_fast_constants([value * scale for value in right])
    if not right:
        scale = left[-1].inverse()
        return _poly_from_fast_constants([value * scale for value in left])
    gcd, _, _ = fast_efield.poly_extended_gcd(left, right)
    return _poly_from_fast_constants(gcd)


def reduce_frac_fast(value):
    """Canonicalize an E(C) value with exact tower-field polynomial gcd."""
    value = Frac.coerce(value)
    if not value:
        return Frac()
    numerator = _fast_constant_poly(value.numerator)
    denominator = _fast_constant_poly(value.denominator)
    gcd, _, _ = fast_efield.poly_extended_gcd(numerator, denominator)
    quotient_numerator, remainder_numerator = fast_efield.poly_divmod(numerator, gcd)
    quotient_denominator, remainder_denominator = fast_efield.poly_divmod(denominator, gcd)
    assert not remainder_numerator and not remainder_denominator
    scale = quotient_denominator[-1].inverse()
    quotient_numerator = [entry * scale for entry in quotient_numerator]
    quotient_denominator = [entry * scale for entry in quotient_denominator]
    out = Frac(
        _poly_from_fast_constants(quotient_numerator),
        _poly_from_fast_constants(quotient_denominator),
        normalized=True,
    )
    assert FAST_FIELD.from_frac(out) == FAST_FIELD.from_frac(value)
    return out


def poly_lcm_fast(left, right):
    """Monic LCM in E[C], used only for denominator-cleared certificates."""
    left, right = Poly(left), Poly(right)
    if not left or not right:
        return Poly()
    common = poly_gcd_fast(left, right)
    return poly_monic(poly_exact_div(left, common) * right)


def primitive_cleared_relation(residual, combination):
    """Clear a rational left relation and remove its polynomial content."""
    canonical = {
        index: reduce_frac_fast(coefficient)
        for index, coefficient in combination.items()
    }
    canonical_residual = reduce_frac_fast(residual)
    common_denominator = ONE_POLY
    for value in list(canonical.values()) + [canonical_residual]:
        common_denominator = poly_lcm_fast(common_denominator, value.denominator)
    cleared = {
        index: value.numerator
        * poly_exact_div(common_denominator, value.denominator)
        for index, value in canonical.items()
    }
    cleared_residual = canonical_residual.numerator * poly_exact_div(
        common_denominator, canonical_residual.denominator
    )
    content = None
    for value in cleared.values():
        if value:
            content = value if content is None else poly_gcd_fast(content, value)
    assert content is not None
    content = poly_monic(content)
    primitive = {
        index: poly_exact_div(value, content)
        for index, value in cleared.items()
    }
    primitive_residual = poly_exact_div(cleared_residual, content)
    return primitive_residual, primitive, common_denominator, content


def poly_extended_gcd(left, right):
    """Normalized FLINT/tower Bezout identity over E[C]."""
    left, right = Poly(left), Poly(right)
    gcd_fast, left_fast, right_fast = fast_efield.poly_extended_gcd(
        _fast_constant_poly(left), _fast_constant_poly(right)
    )
    gcd = _poly_from_fast_constants(gcd_fast)
    left_weight = _poly_from_fast_constants(left_fast)
    right_weight = _poly_from_fast_constants(right_fast)
    assert gcd
    assert left_weight * Poly(left) + right_weight * Poly(right) == gcd
    return gcd, left_weight, right_weight


def bezout_family(polynomials):
    """Return monic gcd and weights certifying it for a nonempty family."""
    assert polynomials
    gcd = Poly(polynomials[0])
    weights = [ONE_POLY]
    for polynomial in polynomials[1:]:
        gcd, old_weight, new_weight = poly_extended_gcd(gcd, polynomial)
        weights = [old_weight * weight for weight in weights] + [new_weight]
    assert sum(
        (weight * polynomial for weight, polynomial in zip(weights, polynomials)),
        Poly(),
    ) == gcd
    return gcd, weights


def poly_record(poly):
    poly = Poly(poly)
    return {
        "degree": poly.degree,
        "sha256": sha256(repr(poly).encode()).hexdigest(),
        "coefficients": [qd.uniform.extension_text(value) for value in poly.coefficients],
    }


def frac_record(value):
    value = reduce_frac_fast(value)
    return {
        "numerator": poly_record(value.numerator),
        "denominator": poly_record(value.denominator),
        "sha256": sha256(repr(value).encode()).hexdigest(),
    }


def factor_records(stage, factors):
    return [
        {
            "stage": stage,
            "row_index": row_index,
            "key": list(key),
            "pivot": pivot,
            "lead": frac_record(lead),
        }
        for row_index, key, pivot, lead in factors
    ]


def main():
    Cq = rt.Rat(rt.X)
    fb.CENTER = (Cq, rt.Rat(1), rt.Rat(1))
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
    transport_pivots, transport_records, transport_exceptional, transport_minor = rt.factor(transport)
    pivot_rhs, compatibility = propagate(transport_records)
    assert not compatibility and len(transport_pivots) == 3470
    free = [variable for variable in range(nf + ng) if variable not in transport_pivots]
    free_parameter = {variable: index for index, variable in enumerate(free)}
    assert len(free) == 132
    print("c1 transport affine PASS", flush=True)

    bands132 = {
        (owner, exponent): section_forms(
            15 if owner == "f" else 25,
            60 if owner == "f" else 100,
            exponent,
            16 if owner == "f" else 26,
            0 if owner == "f" else nf,
            transport_pivots,
            pivot_rhs,
            free_parameter,
        )
        for owner in ("f", "g")
        for exponent in (1, 2, 3)
    }
    pole_f132 = pole_forms(15, 60, -2, 61, 0, transport_pivots, pivot_rhs, free_parameter)
    pole_g132 = pole_forms(25, 100, -4, 101, nf, transport_pivots, pivot_rhs, free_parameter)
    print("c1 transport sections PASS", flush=True)

    configure_qd()
    first_rows = qd.pack(
        "X-2", qd.first_band_polynomials(bands132[("f", 1)], bands132[("g", 1)])
    )
    forms94, free94, factors_first = parameterize_qmatrix(132, first_rows)
    assert (len(factors_first), len(free94)) == (38, 94)
    print("c1 first generic PASS", flush=True)

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
        qd.compile_pole_previous(
            fast_forms(pole_f94), fast_forms(pole_g94)
        ),
    )
    forms56, free56, factors_previous = parameterize(94, previous_rows)
    assert (len(factors_previous), len(free56)) == (38, 56)
    print("c1 previous generic PASS", flush=True)

    bands56 = {key: compose(forms, forms56) for key, forms in bands94.items()}
    fast_bands56 = {key: fast_forms(forms) for key, forms in bands56.items()}
    current_rows = pack_fast(
        "X0",
        qd.compile_current(
            *[fast_bands56[("f", exponent)] for exponent in (1, 2, 3)],
            *[fast_bands56[("g", exponent)] for exponent in (1, 2, 3)],
        ),
    )
    current_pivots, factors_current, dependent = solve_efield(
        56, current_rows, certificates=True
    )
    assert len(current_pivots) == 25
    compatibility = [
        (row_index, key, reduce_frac_fast(residual), combination)
        for row_index, key, residual, combination in dependent
        if residual
    ]
    assert compatibility
    gcd = compatibility[0][2].numerator
    for _, _, residual, _ in compatibility[1:]:
        gcd = poly_gcd_fast(gcd, residual.numerator)
    gcd = poly_monic(gcd)

    cleared_relations = [
        primitive_cleared_relation(residual, combination)
        for _, _, residual, combination in compatibility
    ]
    primitive_residuals = [entry[0] for entry in cleared_relations]
    primitive_gcd, primitive_weights = bezout_family(primitive_residuals)

    def replay_polynomial_relation(relation, expected):
        row_sum = {}
        rhs_sum = FAST_FIELD.zero
        for row_index, polynomial in relation.items():
            multiplier = FAST_FIELD.from_frac(Frac(polynomial))
            _, row, rhs = current_rows[row_index]
            for variable, coefficient in row.items():
                coefficient = (
                    coefficient.value
                    if isinstance(coefficient, FScalar)
                    else FAST_FIELD.from_frac(coefficient)
                )
                value = row_sum.get(variable, FAST_FIELD.zero) + multiplier * coefficient
                if value:
                    row_sum[variable] = value
                else:
                    row_sum.pop(variable, None)
            rhs = rhs.value if isinstance(rhs, FScalar) else FAST_FIELD.from_frac(rhs)
            rhs_sum += multiplier * rhs
        assert not row_sum
        assert rhs_sum == FAST_FIELD.from_frac(Frac(expected))

    for primitive_residual, primitive_relation, _, _ in cleared_relations:
        replay_polynomial_relation(primitive_relation, primitive_residual)

    bezout_relation = {}
    for weight, (_, primitive_relation, _, _) in zip(
        primitive_weights, cleared_relations
    ):
        for row_index, coefficient in primitive_relation.items():
            value = bezout_relation.get(row_index, Poly()) + weight * coefficient
            if value:
                bezout_relation[row_index] = value
            else:
                bezout_relation.pop(row_index, None)
    replay_polynomial_relation(bezout_relation, primitive_gcd)

    all_factors = (
        factor_records("first", factors_first)
        + factor_records("previous_pole", factors_previous)
        + factor_records("current", factors_current)
    )
    output = {
        "verdict": "TD6-C1-GENERIC-E(C)-PENCIL-PASS",
        "ranks": {
            "transport": [len(transport_pivots), nf + ng],
            "first": [len(factors_first), 132],
            "previous_pole": [len(factors_previous), 94],
            "current": [len(factors_current), 56],
        },
        "transport_exceptional_factors": dict(transport_exceptional),
        "transport_selected_minor": {
            "numerator": str(transport_minor.numerator),
            "denominator": str(transport_minor.denominator),
            "sha256": sha256(repr(transport_minor).encode()).hexdigest(),
        },
        "later_pivots": all_factors,
        "compatibility": [
            {
                "row_index": row_index,
                "key": list(key),
                "residual": frac_record(residual),
                "left_null_support": len(combination),
                "left_null_sha256": sha256(repr(sorted(combination.items())).encode()).hexdigest(),
            }
            for row_index, key, residual, combination in compatibility
        ],
        "compatibility_numerator_gcd": poly_record(gcd),
        "denominator_cleared_current_relations": [
            {
                "row_index": row_index,
                "key": list(key),
                "primitive_residual": poly_record(primitive_residual),
                "common_denominator": poly_record(common_denominator),
                "removed_content": poly_record(content),
                "primitive_left_support": len(primitive_relation),
                "primitive_left_sha256": sha256(
                    repr(sorted(primitive_relation.items())).encode()
                ).hexdigest(),
            }
            for (
                (row_index, key, _, _),
                (
                    primitive_residual,
                    primitive_relation,
                    common_denominator,
                    content,
                ),
            ) in zip(compatibility, cleared_relations)
        ],
        "denominator_cleared_current_bezout": {
            "gcd": poly_record(primitive_gcd),
            "weights": [poly_record(weight) for weight in primitive_weights],
            "left_support": len(bezout_relation),
            "left_sha256": sha256(
                repr(sorted(bezout_relation.items())).encode()
            ).hexdigest(),
        },
        "family_killed": False,
        "SP2_killed": False,
        "JC2_resolved": False,
    }
    print(json.dumps(output, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
