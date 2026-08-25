#!/usr/bin/env python3
"""Exact eps^2 coefficient of the TD6 c3 thickening along the c1 line.

This is a provisional discriminator over E(C)[eps]/(eps^3).  It retains the
full nonlinear C dependence and the varying transport/first-band echelon.
The coefficient named ``second`` is the coefficient of eps^2, not one half
of a classical second derivative.  No neighbourhood or bivariate conclusion
is licensed by this computation alone.
"""

from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "c1_c3_thickening.py"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


m = load("td6_c1_c3_dual_source_for_second_order", SOURCE)
cp, qd, rt, fb = m.cp, m.qd, m.rt, m.fb
FAST_FIELD = m.FAST_FIELD
ZERO, ONE = FAST_FIELD.zero, FAST_FIELD.one


class QJet:
    """Q(C)[eps]/(eps^3), stored as coefficient triples."""

    __slots__ = ("value", "derivative", "second")

    def __init__(self, value=0, derivative=0, second=0):
        if isinstance(value, QJet):
            self.value, self.derivative, self.second = (
                value.value, value.derivative, value.second
            )
        else:
            self.value = rt.Rat.coerce(value)
            self.derivative = rt.Rat.coerce(derivative)
            self.second = rt.Rat.coerce(second)

    @staticmethod
    def coerce(value):
        return value if isinstance(value, QJet) else QJet(value)

    def __add__(self, other):
        other = QJet.coerce(other)
        return QJet(
            self.value + other.value,
            self.derivative + other.derivative,
            self.second + other.second,
        )

    __radd__ = __add__

    def __neg__(self):
        return QJet(-self.value, -self.derivative, -self.second)

    def __sub__(self, other):
        return self + (-QJet.coerce(other))

    def __rsub__(self, other):
        return QJet.coerce(other) - self

    def __mul__(self, other):
        other = QJet.coerce(other)
        return QJet(
            self.value * other.value,
            self.derivative * other.value + self.value * other.derivative,
            self.second * other.value
            + self.derivative * other.derivative
            + self.value * other.second,
        )

    __rmul__ = __mul__

    def inverse(self):
        if not self.value:
            raise ZeroDivisionError("zero-base Q(C) jet pivot")
        inverse = self.value.inverse()
        first = -(inverse * inverse) * self.derivative
        second = -(inverse * (self.derivative * first + self.second * inverse))
        return QJet(inverse, first, second)

    def __truediv__(self, other):
        return self * QJet.coerce(other).inverse()

    def __rtruediv__(self, other):
        return QJet.coerce(other) / self

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        out, base = QJet(1), self
        while exponent:
            if exponent & 1:
                out *= base
            base *= base
            exponent //= 2
        return out

    def __bool__(self):
        return bool(self.value) or bool(self.derivative) or bool(self.second)

    def __eq__(self, other):
        other = QJet.coerce(other)
        return (
            self.value == other.value
            and self.derivative == other.derivative
            and self.second == other.second
        )


class EJet:
    """E(C)[eps]/(eps^3), stored as coefficient triples."""

    __slots__ = ("value", "derivative", "second")

    def __init__(self, value=0, derivative=0, second=0):
        if isinstance(value, EJet):
            self.value, self.derivative, self.second = (
                value.value, value.derivative, value.second
            )
        elif isinstance(value, QJet):
            self.value = cp.lift_rat(value.value)
            self.derivative = cp.lift_rat(value.derivative)
            self.second = cp.lift_rat(value.second)
        else:
            self.value = cp.Frac.coerce(value)
            self.derivative = cp.Frac.coerce(derivative)
            self.second = cp.Frac.coerce(second)

    @staticmethod
    def coerce(value):
        return value if isinstance(value, EJet) else EJet(value)

    def __add__(self, other):
        other = EJet.coerce(other)
        return EJet(
            self.value + other.value,
            self.derivative + other.derivative,
            self.second + other.second,
        )

    __radd__ = __add__

    def __neg__(self):
        return EJet(-self.value, -self.derivative, -self.second)

    def __sub__(self, other):
        return self + (-EJet.coerce(other))

    def __rsub__(self, other):
        return EJet.coerce(other) - self

    def __mul__(self, other):
        other = EJet.coerce(other)
        return EJet(
            self.value * other.value,
            self.derivative * other.value + self.value * other.derivative,
            self.second * other.value
            + self.derivative * other.derivative
            + self.value * other.second,
        )

    __rmul__ = __mul__

    def inverse(self):
        if not self.value:
            raise ZeroDivisionError("zero-base E(C) jet pivot")
        inverse = self.value.inverse()
        first = -(inverse * inverse) * self.derivative
        second = -(inverse * (self.derivative * first + self.second * inverse))
        return EJet(inverse, first, second)

    def __truediv__(self, other):
        return self * EJet.coerce(other).inverse()

    def __rtruediv__(self, other):
        return EJet.coerce(other) / self

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        out, base = EJet(1), self
        while exponent:
            if exponent & 1:
                out *= base
            base *= base
            exponent //= 2
        return out

    def __bool__(self):
        return bool(self.value) or bool(self.derivative) or bool(self.second)

    def __eq__(self, other):
        other = EJet.coerce(other)
        return (
            self.value == other.value
            and self.derivative == other.derivative
            and self.second == other.second
        )


class FJet:
    """Fast exact E(C)[eps]/(eps^3)."""

    __slots__ = ("value", "derivative", "second")

    def __init__(self, value=None, derivative=None, second=None):
        self.value = self._coefficient(value)
        self.derivative = self._coefficient(derivative)
        self.second = self._coefficient(second)

    @staticmethod
    def _coefficient(value):
        if value is None:
            return ZERO
        if isinstance(value, cp.fast_efield.EField):
            assert value.factory is FAST_FIELD
            return value
        return FAST_FIELD.from_frac(cp.Frac.coerce(value))

    @staticmethod
    def from_edual(value):
        if isinstance(value, FJet):
            return value
        value = EJet.coerce(value)
        return FJet(
            FAST_FIELD.from_frac(value.value),
            FAST_FIELD.from_frac(value.derivative),
            FAST_FIELD.from_frac(value.second),
        )

    def to_edual(self):
        return EJet(
            FAST_FIELD.to_frac(self.value),
            FAST_FIELD.to_frac(self.derivative),
            FAST_FIELD.to_frac(self.second),
        )

    @staticmethod
    def coerce(value):
        return value if isinstance(value, FJet) else FJet.from_edual(value)

    def __add__(self, other):
        other = FJet.coerce(other)
        return FJet(
            self.value + other.value,
            self.derivative + other.derivative,
            self.second + other.second,
        )

    __radd__ = __add__

    def __neg__(self):
        return FJet(-self.value, -self.derivative, -self.second)

    def __sub__(self, other):
        return self + (-FJet.coerce(other))

    def __rsub__(self, other):
        return FJet.coerce(other) - self

    def __mul__(self, other):
        other = FJet.coerce(other)
        return FJet(
            self.value * other.value,
            self.derivative * other.value + self.value * other.derivative,
            self.second * other.value
            + self.derivative * other.derivative
            + self.value * other.second,
        )

    __rmul__ = __mul__

    def inverse(self):
        if not self.value:
            raise ZeroDivisionError("zero-base fast jet pivot")
        inverse = self.value.inverse()
        first = -(inverse * inverse) * self.derivative
        second = -(inverse * (self.derivative * first + self.second * inverse))
        return FJet(inverse, first, second)

    def __truediv__(self, other):
        return self * FJet.coerce(other).inverse()

    def __rtruediv__(self, other):
        return FJet.coerce(other) / self

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        out, base = FJet(ONE), self
        while exponent:
            if exponent & 1:
                out *= base
            base *= base
            exponent //= 2
        return out

    def __bool__(self):
        return bool(self.value) or bool(self.derivative) or bool(self.second)

    def __eq__(self, other):
        other = FJet.coerce(other)
        return (
            self.value == other.value
            and self.derivative == other.derivative
            and self.second == other.second
        )


def vector(value, factory):
    value = EJet.coerce(value)
    return tuple(factory.from_frac(coefficient) for coefficient in (
        value.value, value.derivative, value.second
    ))


def vector_scale(value, scalar):
    scalar = QJet.coerce(scalar)
    return (
        value[0].scale(scalar.value),
        value[1].scale(scalar.value) + value[0].scale(scalar.derivative),
        value[2].scale(scalar.value)
        + value[1].scale(scalar.derivative)
        + value[0].scale(scalar.second),
    )


def vector_sub(left, right):
    return tuple(a - b for a, b in zip(left, right))


def propagate(records):
    factory = cp.fast_evec.EVecFactory(cp)
    pivot_rhs, compatibility = {}, []
    for key, kind, pivot, lead, factors in records:
        value = vector(m.source_rhs(key), factory)
        for old, factor in factors:
            value = vector_sub(value, vector_scale(pivot_rhs[old], factor))
        if kind == "pivot":
            pivot_rhs[pivot] = vector_scale(value, lead.inverse())
        elif any(value):
            compatibility.append((key, value))
    return pivot_rhs, compatibility


def restrict_row(original_row, pivots, pivot_rhs, free_parameter):
    row = {
        variable: QJet.coerce(coefficient)
        for variable, coefficient in original_row.items() if coefficient
    }
    factory = next(iter(pivot_rhs.values()))[0].factory
    constant = (factory.zero(), factory.zero(), factory.zero())
    for pivot in sorted(pivots):
        factor = row.pop(pivot, None)
        if factor is None or not factor:
            continue
        contribution = vector_scale(pivot_rhs[pivot], factor)
        constant = tuple(a + b for a, b in zip(constant, contribution))
        for variable, coefficient in pivots[pivot].items():
            if variable == pivot:
                continue
            value = row.get(variable, QJet()) - factor * coefficient
            if value:
                row[variable] = value
            else:
                row.pop(variable, None)
    assert all(variable in free_parameter for variable in row)
    return (
        EJet(*(factory.to_frac(coefficient) for coefficient in constant)),
        {free_parameter[variable]: EJet(coefficient) for variable, coefficient in row.items()},
    )


# Replace every two-coefficient arithmetic hook before constructing a row.
m.QDual, m.EDual, m.FPair = QJet, EJet, FJet
m.propagate, m.restrict_row = propagate, restrict_row
m.q_to_e = lambda value: EJet(value)


def clean(poly):
    return {monomial: coefficient for monomial, coefficient in poly.items() if coefficient}


def add(left, right, scale=None):
    scale = FJet(ONE) if scale is None else FJet.coerce(scale)
    out = dict(left)
    for monomial, coefficient in right.items():
        value = out.get(monomial, FJet()) + scale * FJet.coerce(coefficient)
        if value:
            out[monomial] = value
        else:
            out.pop(monomial, None)
    return out


def multiply(left, right):
    out = {}
    for ml, cl in left.items():
        for mr, cr in right.items():
            monomial = tuple(sorted(ml + mr))
            value = out.get(monomial, FJet()) + FJet.coerce(cl) * FJet.coerce(cr)
            if value:
                out[monomial] = value
            else:
                out.pop(monomial, None)
    return out


def source_polynomial(row, rhs):
    out = {(): -FJet.from_edual(rhs)} if rhs else {}
    for variable, coefficient in row.items():
        coefficient = FJet.from_edual(coefficient)
        if coefficient:
            out[(variable,)] = coefficient
    return out


def divide(polynomial, pivots):
    remainder, quotients, normalized = dict(polynomial), {}, {}
    for pivot in sorted(pivots):
        row, rhs, _ = pivots[pivot]
        normalized[pivot] = source_polynomial(row, rhs)
        assert normalized[pivot][(pivot,)] == FJet(ONE)
        quotient = {}
        while True:
            targets = sorted(monomial for monomial in remainder if pivot in monomial)
            if not targets:
                break
            monomial = targets[0]
            coefficient = remainder[monomial]
            reduced = list(monomial)
            reduced.remove(pivot)
            multiplier = {tuple(reduced): coefficient}
            quotient = add(quotient, multiplier)
            remainder = add(
                remainder, multiply(multiplier, normalized[pivot]), FJet(-ONE)
            )
        if quotient:
            quotients[pivot] = quotient
    replay = dict(remainder)
    for pivot, quotient in quotients.items():
        replay = add(replay, multiply(quotient, normalized[pivot]))
    assert clean(replay) == clean(polynomial)
    return remainder, quotients


def lift_relations(quotients, pivots, nrows):
    relations = [{} for _ in range(nrows)]
    for pivot, quotient in quotients.items():
        _, _, combination = pivots[pivot]
        for row_index, coefficient in combination.items():
            relations[row_index] = add(relations[row_index], quotient, coefficient)
    return relations


def replay_source(polynomial, remainder, relations, rows):
    replay = dict(remainder)
    for relation, (_, row, rhs) in zip(relations, rows):
        if relation:
            replay = add(replay, multiply(relation, source_polynomial(row, rhs)))
    assert clean(replay) == clean(polynomial)


def component(poly, order):
    attribute = ("value", "derivative", "second")[order]
    return {
        monomial: getattr(value, attribute)
        for monomial, value in poly.items() if getattr(value, attribute)
    }


def freeze_coefficient(value):
    """Discard eps and eps^2 coefficients, retaining the exact base value."""
    value = FJet.coerce(value)
    return FJet(value.value, ZERO, ZERO)


def freeze_echelon(pivots):
    """Freeze a normalized varying echelon at eps=0 for a negative control."""
    return {
        pivot: (
            {
                variable: freeze_coefficient(coefficient)
                for variable, coefficient in row.items()
            },
            freeze_coefficient(rhs),
            None,
        )
        for pivot, (row, rhs, _) in pivots.items()
    }


def digest(poly):
    payload = tuple(
        (monomial, repr(value.value), repr(value.derivative), repr(value.second))
        for monomial, value in sorted(poly.items())
    )
    return sha256(repr(payload).encode()).hexdigest()


def record(poly):
    return {
        "term_count": len(poly),
        "parameter_degree": max((len(monomial) for monomial in poly), default=-1),
        "sha256": sha256(
            repr(tuple((monomial, repr(value)) for monomial, value in sorted(poly.items()))).encode()
        ).hexdigest(),
    }


def main():
    # Arithmetic self-checks that fail if the eps^2 convolution is omitted.
    z = QJet(1, 1)
    assert z * z == QJet(1, 2, 1)
    assert z * z.inverse() == QJet(1)

    Cq = rt.Rat(rt.X)
    fb.CENTER = (QJet(Cq), QJet(1), QJet(1, 1))
    fb._X_POWER_CACHE.clear()
    nf, rows_f = fb.build_transport(
        15, 60, 3, {15: m.Q(1)}, fb.F1_F_PATTERN, fb.POLE_F_PATTERN
    )
    ng, rows_g = fb.build_transport(
        25, 100, 5, {1: m.Q(1), 25: m.Q(1)}, fb.F1_G_PATTERN, fb.POLE_G_PATTERN
    )
    transport = [(("f",) + key, row, rhs) for key, row, rhs in rows_f]
    transport += [
        (("g",) + key, {nf + variable: coefficient for variable, coefficient in row.items()}, rhs)
        for key, row, rhs in rows_g
    ]
    data = m.factor_transport(transport)
    pivot_rhs, compatibility = propagate(data["records"])
    assert not compatibility and len(data["pivots"]) == 3470
    transport_pivot_first_count = sum(
        bool(lead.derivative)
        for _, kind, _, lead, _ in data["records"] if kind == "pivot"
    )
    transport_pivot_second_count = sum(
        bool(lead.second)
        for _, kind, _, lead, _ in data["records"] if kind == "pivot"
    )
    assert transport_pivot_first_count
    assert transport_pivot_second_count
    free = [variable for variable in range(nf + ng) if variable not in data["pivots"]]
    free_parameter = {variable: index for index, variable in enumerate(free)}
    assert len(free) == 132
    print("second-order transport PASS", flush=True)

    bands132 = {
        (owner, exponent): m.section_forms(
            15 if owner == "f" else 25,
            60 if owner == "f" else 100,
            exponent,
            16 if owner == "f" else 26,
            0 if owner == "f" else nf,
            data["pivots"], pivot_rhs, free_parameter,
        )
        for owner in ("f", "g") for exponent in (1, 2, 3)
    }
    m.configure_qd()
    first_rows = qd.pack(
        "X-2", qd.first_band_polynomials(bands132[("f", 1)], bands132[("g", 1)])
    )
    first_pivots, first_factors, dependent = m.solve(132, first_rows, certificates=True)
    assert len(first_pivots) == 38
    assert all(not residual for _, _, residual, _ in dependent)
    assert any(lead.derivative for _, _, _, lead in first_factors)
    assert any(lead.second for _, _, _, lead in first_factors)
    first_pivot_first_count = sum(
        bool(lead.derivative) for _, _, _, lead in first_factors
    )
    first_pivot_second_count = sum(
        bool(lead.second) for _, _, _, lead in first_factors
    )
    print("second-order first echelon PASS", flush=True)

    fast_bands132 = {key: m.fast_forms(forms) for key, forms in bands132.items()}
    m.configure_qd_fast()
    raw = qd.compile_current(
        *[fast_bands132[("f", exponent)] for exponent in (1, 2, 3)],
        *[fast_bands132[("g", exponent)] for exponent in (1, 2, 3)],
    )[12]
    polynomial = {
        monomial: FJet.coerce(coefficient)
        for monomial, coefficient in raw.items() if coefficient
    }
    assert max(map(len, polynomial)) == 2
    assert component(polynomial, 1)
    assert component(polynomial, 2)
    remainder, quotients = divide(polynomial, first_pivots)
    relations = lift_relations(quotients, first_pivots, len(first_rows))
    replay_source(polynomial, remainder, relations, first_rows)
    base, first, second = (component(remainder, order) for order in range(3))
    assert set(base).issubset({()}) and base.get(())
    S = FAST_FIELD.from_e(cp.E(qd.uniform.S_FIELD))
    k = 252 * FAST_FIELD.one - 342 * S + 144 * S**2 - 36 * S**3
    expected_base = -k / 50
    assert base == {(): expected_base}
    assert not first, "first-order frozen result failed in eps^3 replay"

    # Active omission control: reducing the same genuinely varying raw P12
    # against the base-frozen first echelon must *not* reproduce the correct
    # eps^2 cancellation.  This trips if coefficient/lambda variation is
    # silently omitted from the certified reduction.
    frozen_remainder, _ = divide(polynomial, freeze_echelon(first_pivots))
    frozen_second = component(frozen_remainder, 2)
    assert frozen_second, "frozen-echelon negative control unexpectedly vanished"
    print("second-order reduction/source replay PASS", flush=True)

    print(json.dumps({
        "verdict": "TD6-C1-C3-FIRST-IDEAL-EPS2-DISCRIMINATOR",
        "scope": {
            "line": "(c1,c2,c3)=(C,1,1+eps)",
            "ring": "E(C)[eps]/eps^3",
            "second_is_eps2_coefficient": True,
            "neighborhood_theorem": False,
            "full_bivariate_coverage": False,
            "SP2_killed": False,
            "JC2_resolved": False,
        },
        "ranks": {"transport": [3470, nf + ng], "first": [38, 132]},
        "varying_echelon_controls": {
            "transport_pivot_first_count": transport_pivot_first_count,
            "transport_pivot_second_count": transport_pivot_second_count,
            "first_pivot_first_count": first_pivot_first_count,
            "first_pivot_second_count": first_pivot_second_count,
            "frozen_first_echelon_eps2_remainder": record(frozen_second),
            "frozen_first_echelon_negative_control_nonzero": True,
            "lambda_prime_and_second_order_multiplier_variation_retained": True,
            "eps2_convolution_arithmetic_self_check": True,
        },
        "raw": {
            "triple_sha256": digest(polynomial),
            "base": record(component(polynomial, 0)),
            "first": record(component(polynomial, 1)),
            "second": record(component(polynomial, 2)),
        },
        "remainder": {
            "triple_sha256": digest(remainder),
            "base": record(base),
            "base_is_minus_k_over_50": True,
            "k_definition": "252-342*S+144*S^2-36*S^3",
            "first": record(first),
            "second": record(second),
        },
        "source_lift": {
            "nonzero_original_first_rows": sum(bool(relation) for relation in relations),
            "multiplier_terms": sum(len(relation) for relation in relations),
            "triple_sha256": sha256(repr(tuple(
                tuple((monomial, repr(value.value), repr(value.derivative), repr(value.second))
                      for monomial, value in sorted(relation.items()))
                for relation in relations
            )).encode()).hexdigest(),
        },
        "family_killed": False,
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
