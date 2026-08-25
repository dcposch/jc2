#!/usr/bin/env python3
"""Exact raw TD6 rebuild on the remaining c1 quadratic stratum.

The generic first-stage certificate leaves

    J(C) = 4*C^2 + 20*C + 1 = 0.

This script specializes the *original* 3,602-column transport rows to the
exact quotient Q[C]/(J), rebuilds transport adaptively, propagates the exact
E-valued affine right side, compiles the genuine current t^12 polynomial,
and reduces it through an adaptively rebuilt first-band ideal over
E[C]/(J).  Every inverse used in the latter quotient is checked by an exact
Bezout identity; no assumption that J stays irreducible over E is made.
"""

from fractions import Fraction as Q
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys

from flint import fmpq, fmpq_poly


PRIVATE = Path(__file__).resolve().parent
SOURCE = PRIVATE / "c1_pencil.py"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


cp = load("td6_c1_J_raw_source", SOURCE)
qd, rt, fb, nr = cp.qd, cp.rt, cp.fb, cp.nr
BASE = cp.FAST_FIELD
J = fmpq_poly([1, 20, 4])
J_MONIC_Q = (Q(1, 4), Q(5), Q(1))


def fq(value):
    if isinstance(value, fmpq):
        return value
    if isinstance(value, Q):
        return fmpq(value.numerator, value.denominator)
    return fmpq(value)


class QJ:
    """The exact quadratic field Q[C]/(4*C^2+20*C+1)."""

    __slots__ = ("poly",)

    def __init__(self, value=0):
        if isinstance(value, QJ):
            self.poly = value.poly
            return
        if isinstance(value, rt.Rat):
            numerator = value.numerator % J
            denominator = value.denominator % J
            if not denominator:
                raise ZeroDivisionError("generic transport denominator vanishes on J")
            common, inverse, _ = denominator.xgcd(J)
            assert common.degree() == 0
            inverse *= 1 / common[0]
            self.poly = (numerator * inverse) % J
            return
        if isinstance(value, fmpq_poly):
            self.poly = value % J
            return
        if isinstance(value, (list, tuple)):
            self.poly = fmpq_poly([fq(entry) for entry in value]) % J
            return
        self.poly = fmpq_poly([fq(value)]) if value else fmpq_poly()

    @staticmethod
    def coerce(value):
        return value if isinstance(value, QJ) else QJ(value)

    def __add__(self, other):
        return QJ(self.poly + QJ.coerce(other).poly)

    __radd__ = __add__

    def __neg__(self):
        return QJ(-self.poly)

    def __sub__(self, other):
        return self + (-QJ.coerce(other))

    def __rsub__(self, other):
        return QJ.coerce(other) - self

    def __mul__(self, other):
        return QJ((self.poly * QJ.coerce(other).poly) % J)

    __rmul__ = __mul__

    def inverse(self):
        if not self:
            raise ZeroDivisionError
        common, inverse, _ = self.poly.xgcd(J)
        assert common.degree() == 0
        inverse *= 1 / common[0]
        result = QJ(inverse)
        assert self * result == QJ(1)
        return result

    def __truediv__(self, other):
        return self * QJ.coerce(other).inverse()

    def __rtruediv__(self, other):
        return QJ.coerce(other) / self

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        out, base = QJ(1), self
        while exponent:
            if exponent & 1:
                out *= base
            base *= base
            exponent //= 2
        return out

    def __bool__(self):
        return bool(self.poly)

    def __eq__(self, other):
        return self.poly == QJ.coerce(other).poly

    def canonical(self):
        return tuple(
            str(self.poly[index]) if index <= self.poly.degree() else "0"
            for index in range(2)
        )

    def __repr__(self):
        return f"QJ{self.canonical()!r}"


def base_rational(value):
    return BASE.scalar(rt.Rat(value))


BASE_ZERO = BASE.zero
BASE_ONE = BASE.one
J_MONIC_E = [base_rational(value) for value in J_MONIC_Q]


class NonUnit(Exception):
    def __init__(self, gcd):
        super().__init__("nonunit in E[C]/(J)")
        self.gcd = gcd


class EJ:
    """Exact quotient E[C]/(J), using only explicitly certified units."""

    __slots__ = ("coefficients",)

    def __init__(self, coefficients=()):
        values = list(coefficients)
        assert len(values) <= 2
        values += [BASE_ZERO] * (2 - len(values))
        self.coefficients = tuple(values)

    @staticmethod
    def from_base(value):
        if isinstance(value, cp.FScalar):
            value = value.value
        if isinstance(value, cp.fast_efield.EField):
            assert value.factory is BASE
            return EJ((value,))
        if isinstance(value, cp.Frac):
            canonical = cp.reduce_frac_fast(value)
            assert canonical.denominator == cp.ONE_POLY
            assert canonical.numerator.degree <= 0
            return EJ((BASE.from_frac(canonical),))
        return EJ((BASE.from_frac(cp.Frac(cp.E(value))),))

    @staticmethod
    def from_qj(value):
        value = QJ.coerce(value)
        coefficients = []
        for index in range(2):
            coefficient = value.poly[index] if index <= value.poly.degree() else fmpq(0)
            coefficients.append(base_rational(Q(int(coefficient.p), int(coefficient.q))))
        return EJ(coefficients)

    @staticmethod
    def coerce(value):
        if isinstance(value, EJ):
            return value
        if isinstance(value, HScalar):
            return value.value
        if isinstance(value, QJ) or isinstance(value, rt.Rat):
            return EJ.from_qj(QJ(value))
        if isinstance(value, (int, Q, fmpq)):
            return EJ.from_qj(QJ(value))
        return EJ.from_base(value)

    def __add__(self, other):
        other = EJ.coerce(other)
        return EJ(tuple(
            left + right for left, right in zip(self.coefficients, other.coefficients)
        ))

    __radd__ = __add__

    def __neg__(self):
        return EJ(tuple(-value for value in self.coefficients))

    def __sub__(self, other):
        return self + (-EJ.coerce(other))

    def __rsub__(self, other):
        return EJ.coerce(other) - self

    def __mul__(self, other):
        other = EJ.coerce(other)
        product = [BASE_ZERO, BASE_ZERO, BASE_ZERO]
        for i, left in enumerate(self.coefficients):
            if left:
                for j, right in enumerate(other.coefficients):
                    if right:
                        product[i + j] = product[i + j] + left * right
        top = product[2]
        if top:
            product[0] = product[0] - top * J_MONIC_E[0]
            product[1] = product[1] - top * J_MONIC_E[1]
        return EJ(tuple(product[:2]))

    __rmul__ = __mul__

    def inverse(self):
        if not self:
            raise ZeroDivisionError
        gcd, coefficient, _ = cp.fast_efield.poly_extended_gcd(
            list(self.coefficients), J_MONIC_E
        )
        if len(gcd) != 1:
            raise NonUnit(gcd)
        values = coefficient + [BASE_ZERO] * (2 - len(coefficient))
        result = EJ(tuple(values[:2]))
        assert self * result == EJ((BASE_ONE,))
        return result

    def __truediv__(self, other):
        return self * EJ.coerce(other).inverse()

    def __rtruediv__(self, other):
        return EJ.coerce(other) / self

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        out, base = EJ((BASE_ONE,)), self
        while exponent:
            if exponent & 1:
                out *= base
            base *= base
            exponent //= 2
        return out

    def __bool__(self):
        return any(self.coefficients)

    def __eq__(self, other):
        other = EJ.coerce(other)
        return self.coefficients == other.coefficients

    def __repr__(self):
        return f"EJ({self.coefficients!r})"


EJ_ZERO = EJ()
EJ_ONE = EJ((BASE_ONE,))


class HScalar:
    __slots__ = ("value",)

    def __init__(self, value=0):
        self.value = value.value if isinstance(value, HScalar) else EJ.coerce(value)

    @staticmethod
    def coerce(value):
        return value if isinstance(value, HScalar) else HScalar(value)

    def __add__(self, other):
        return HScalar(self.value + HScalar.coerce(other).value)

    __radd__ = __add__

    def __neg__(self):
        return HScalar(-self.value)

    def __sub__(self, other):
        return self + (-HScalar.coerce(other))

    def __rsub__(self, other):
        return HScalar.coerce(other) - self

    def __mul__(self, other):
        return HScalar(self.value * HScalar.coerce(other).value)

    __rmul__ = __mul__

    def inverse(self):
        return HScalar(self.value.inverse())

    def __truediv__(self, other):
        return self * HScalar.coerce(other).inverse()

    def __rtruediv__(self, other):
        return HScalar.coerce(other) / self

    def __pow__(self, exponent):
        return HScalar(self.value ** exponent)

    def __bool__(self):
        return bool(self.value)

    def __eq__(self, other):
        return self.value == HScalar.coerce(other).value


def base_text(value):
    canonical = cp.reduce_frac_fast(BASE.to_frac(value))
    assert canonical.denominator == cp.ONE_POLY
    assert canonical.numerator.degree <= 0
    coefficient = canonical.numerator.constant if canonical.numerator else cp.E(0)
    return qd.uniform.extension_text(coefficient)


def ej_record(value):
    value = EJ.coerce(value)
    coefficients = [base_text(coefficient) for coefficient in value.coefficients]
    return {
        "C_coefficients": coefficients,
        "sha256": sha256(repr(tuple(coefficients)).encode()).hexdigest(),
    }


def qj_record(value):
    value = QJ.coerce(value)
    return {
        "C_coefficients": list(value.canonical()),
        "sha256": sha256(repr(value.canonical()).encode()).hexdigest(),
    }


def factor_transport(rows):
    pivots = {}
    records = []
    determinant = QJ(1)
    for row_index, (key, original_row, _) in enumerate(rows):
        row = {variable: QJ(coefficient) for variable, coefficient in original_row.items() if coefficient}
        factors = []
        while row:
            pivot = min(row)
            if pivot not in pivots:
                break
            multiplier = row[pivot]
            factors.append((pivot, multiplier))
            old_row = pivots[pivot]
            for variable, coefficient in old_row.items():
                value = row.get(variable, QJ()) - multiplier * coefficient
                if value:
                    row[variable] = value
                else:
                    row.pop(variable, None)
        if not row:
            records.append((key, "dependent", None, None, factors))
            continue
        pivot = min(row)
        lead = row[pivot]
        inverse = lead.inverse()
        determinant *= lead
        pivots[pivot] = {variable: coefficient * inverse for variable, coefficient in row.items()}
        records.append((key, "pivot", pivot, lead, factors))
        if row_index % 500 == 0:
            print(f"J transport rows={row_index};pivots={len(pivots)}", flush=True)
    canonical_records = tuple(
        (
            key,
            kind,
            pivot,
            lead.canonical() if lead is not None else None,
            tuple((old, factor.canonical()) for old, factor in factors),
        )
        for key, kind, pivot, lead, factors in records
    )
    return pivots, records, determinant, sha256(repr(canonical_records).encode()).hexdigest()


def propagate(records):
    pivot_rhs = {}
    compatibility = []
    for key, kind, pivot, lead, factors in records:
        value = EJ.from_base(cp.source_rhs(key))
        for old, factor in factors:
            value -= pivot_rhs[old] * EJ.from_qj(factor)
        if kind == "pivot":
            pivot_rhs[pivot] = value / EJ.from_qj(lead)
        elif value:
            compatibility.append((key, value))
    return pivot_rhs, compatibility


def restrict_row(original_row, pivots, pivot_rhs, free_parameter):
    row = {variable: QJ(coefficient) for variable, coefficient in original_row.items() if coefficient}
    constant = EJ_ZERO
    for pivot in sorted(pivots):
        factor = row.pop(pivot, None)
        if factor is None or not factor:
            continue
        constant += pivot_rhs[pivot] * EJ.from_qj(factor)
        for variable, coefficient in pivots[pivot].items():
            if variable == pivot:
                continue
            value = row.get(variable, QJ()) - factor * coefficient
            if value:
                row[variable] = value
            else:
                row.pop(variable, None)
    assert all(variable in free_parameter for variable in row)
    return (
        constant,
        {free_parameter[variable]: EJ.from_qj(coefficient) for variable, coefficient in row.items()},
    )


def section_forms(imax, jmax, exponent, degrees, offset, pivots, pivot_rhs, free_parameter):
    forms = []
    for degree in range(degrees):
        row = fb.x_chart_coefficient(imax, jmax, exponent, degree)
        row = {offset + variable: coefficient for variable, coefficient in row.items()}
        forms.append(restrict_row(row, pivots, pivot_rhs, free_parameter))
    return forms


def configure_qd():
    qd.Dual = HScalar
    qd.B = HScalar()
    qd.S = HScalar(cp.E(qd.uniform.S_FIELD))
    qd.D = HScalar(cp.E(qd.uniform.D_FIELD))
    qd.L = HScalar(cp.E(qd.uniform.L_FIELD))
    qd.A = HScalar(qd.uniform.A_FIELD)
    qd.Q_PRIME = {0: HScalar(1), 24: HScalar(25)}
    qd.R = qd.multiply(
        qd.multiply([HScalar(-1), HScalar(1)], [HScalar(-1), HScalar(1)]),
        [qd.D, -qd.S, HScalar(1)],
    )
    qd.R3, qd.R5 = qd.power(qd.R, 3), qd.power(qd.R, 5)
    qd.POLE_F = {1: -(qd.L**3) * qd.A, 6: qd.L**3}
    qd.POLE_G = {
        0: HScalar(Q(5, 9)) * qd.L**5 * qd.A**2,
        5: HScalar(Q(-5, 3)) * qd.L**5 * qd.A,
        10: qd.L**5,
    }


def h_forms(forms):
    return [
        (HScalar(constant), {parameter: HScalar(coefficient) for parameter, coefficient in coefficients.items()})
        for constant, coefficients in forms
    ]


def pack(family, polynomials):
    out = []
    for degree, polynomial in enumerate(polynomials):
        row = {}
        constant = HScalar.coerce(polynomial.get((), 0)).value
        for monomial, coefficient in polynomial.items():
            if monomial:
                assert len(monomial) == 1
                value = HScalar.coerce(coefficient).value
                if value:
                    row[monomial[0]] = value
        if row or constant:
            out.append(((family, degree), row, -constant))
    return out


def solve_first(nvariables, rows):
    pivots = {}
    dependent = []
    unit_inverse_count = 0
    for row_index, (key, original_row, original_rhs) in enumerate(rows):
        row = dict(original_row)
        rhs = original_rhs
        combination = {row_index: EJ_ONE}
        while row:
            pivot = min(row)
            if pivot not in pivots:
                break
            factor = row[pivot]
            old_row, old_rhs, old_combination = pivots[pivot]
            for variable, coefficient in old_row.items():
                value = row.get(variable, EJ_ZERO) - factor * coefficient
                if value:
                    row[variable] = value
                else:
                    row.pop(variable, None)
            rhs -= factor * old_rhs
            for old_index, coefficient in old_combination.items():
                value = combination.get(old_index, EJ_ZERO) - factor * coefficient
                if value:
                    combination[old_index] = value
                else:
                    combination.pop(old_index, None)
        if not row:
            dependent.append((row_index, key, rhs, combination))
            continue
        pivot = min(row)
        lead = row[pivot]
        inverse = lead.inverse()
        unit_inverse_count += 1
        pivots[pivot] = (
            {variable: coefficient * inverse for variable, coefficient in row.items()},
            rhs * inverse,
            {index: coefficient * inverse for index, coefficient in combination.items()},
        )
    return pivots, dependent, unit_inverse_count


def clean(poly):
    return {monomial: coefficient for monomial, coefficient in poly.items() if coefficient}


def add(poly, other, scale=None):
    scale = EJ_ONE if scale is None else EJ.coerce(scale)
    out = dict(poly)
    for monomial, coefficient in other.items():
        value = out.get(monomial, EJ_ZERO) + scale * EJ.coerce(coefficient)
        if value:
            out[monomial] = value
        else:
            out.pop(monomial, None)
    return out


def multiply(left, right):
    out = {}
    for monomial_left, coefficient_left in left.items():
        for monomial_right, coefficient_right in right.items():
            monomial = tuple(sorted(monomial_left + monomial_right))
            value = out.get(monomial, EJ_ZERO) + EJ.coerce(coefficient_left) * EJ.coerce(coefficient_right)
            if value:
                out[monomial] = value
            else:
                out.pop(monomial, None)
    return out


def linear_polynomial(row, rhs):
    out = {(): -rhs} if rhs else {}
    for variable, coefficient in row.items():
        if coefficient:
            out[(variable,)] = coefficient
    return out


def divide_by_echelon(polynomial, pivots):
    remainder = dict(polynomial)
    quotients = {}
    for count, pivot in enumerate(sorted(pivots), 1):
        row, rhs, _ = pivots[pivot]
        normalized = linear_polynomial(row, rhs)
        assert normalized[pivot,] == EJ_ONE
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
            remainder = add(remainder, multiply(multiplier, normalized), -EJ_ONE)
        if quotient:
            quotients[pivot] = quotient
        if count % 8 == 0:
            print(f"J first reduction pivots={count}/{len(pivots)};terms={len(remainder)}", flush=True)
    replay = dict(remainder)
    for pivot, quotient in quotients.items():
        row, rhs, _ = pivots[pivot]
        replay = add(replay, multiply(quotient, linear_polynomial(row, rhs)))
    assert clean(replay) == clean(polynomial)
    return remainder, quotients


def lift_quotients(quotients, pivots, nrows):
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
            replay = add(replay, multiply(relation, linear_polynomial(row, rhs)))
    assert clean(replay) == clean(polynomial)
    canonical = tuple(
        (
            index,
            tuple((monomial, tuple(base_text(v) for v in coefficient.coefficients)) for monomial, coefficient in sorted(relation.items())),
        )
        for index, relation in enumerate(relations) if relation
    )
    return {
        "source_relation_count": len(canonical),
        "source_relation_term_count": sum(len(relation) for _, relation in canonical),
        "source_relation_sha256": sha256(repr(canonical).encode()).hexdigest(),
        "identity": "raw_current_t12 = reduced_t12 + sum(multiplier_i * first_row_i)",
        "source_relations": [
            {
                "row_index": index,
                "key": list(rows[index][0]),
                "terms": [
                    {"monomial": list(monomial), "coefficient": {"C_coefficients": list(coefficients)}}
                    for monomial, coefficients in relation
                ],
            }
            for index, relation in canonical
        ],
    }


def polynomial_record(poly):
    canonical = tuple(
        (monomial, tuple(base_text(value) for value in EJ.coerce(coefficient).coefficients))
        for monomial, coefficient in sorted(poly.items()) if coefficient
    )
    constant = next((coefficient for monomial, coefficient in poly.items() if not monomial), None)
    return {
        "term_count": len(canonical),
        "parameter_degree": max((len(monomial) for monomial, _ in canonical), default=-1),
        "sha256": sha256(repr(canonical).encode()).hexdigest(),
        "constant": ej_record(constant) if constant is not None else None,
        "parameter_free_nonzero": len(canonical) == 1 and canonical[0][0] == (),
    }


def compile_current_degree(degree, f1, f2, f3, g1, g2, g3):
    equation = {}
    for i, left in enumerate(f1):
        j = degree - i + 1
        if 1 <= j < len(g2):
            equation = nr.add_polynomial(equation, nr.multiply_affine(left, nr.scale_affine(g2[j], Q(j))))
    for i, left in enumerate(f2):
        j = degree - i + 1
        if 1 <= j < len(g1):
            equation = nr.add_polynomial(equation, nr.multiply_affine(left, nr.scale_affine(g1[j], Q(j))), Q(2))
    for i, form in enumerate(f3):
        multiplier = qd.Q_PRIME.get(degree - i, HScalar())
        if multiplier:
            equation = nr.add_polynomial(equation, nr.affine_polynomial(form), Q(3) * multiplier)
    g_degree = degree - 14
    if 0 <= g_degree < len(g3):
        equation = nr.add_polynomial(equation, nr.affine_polynomial(g3[g_degree]), Q(-45))
    for i in range(1, len(f1)):
        j = degree - (i - 1)
        if 0 <= j < len(g2):
            equation = nr.add_polynomial(equation, nr.multiply_affine(nr.scale_affine(f1[i], Q(i)), g2[j]), Q(-2))
    for i in range(1, len(f2)):
        j = degree - (i - 1)
        if 0 <= j < len(g1):
            equation = nr.add_polynomial(equation, nr.multiply_affine(nr.scale_affine(f2[i], Q(i)), g1[j]), Q(-1))
    if degree == 0:
        equation = nr.add_polynomial(equation, {(): Q(-1)})
    return equation


def main():
    content, factors = J.factor()
    assert content == 1 and len(factors) == 1 and factors[0][1] == 1
    C = rt.Rat(rt.X)
    fb.CENTER = (C, rt.Rat(1), rt.Rat(1))
    fb._X_POWER_CACHE.clear()
    nf, rows_f = fb.build_transport(15, 60, 3, {15: Q(1)}, fb.F1_F_PATTERN, fb.POLE_F_PATTERN)
    ng, rows_g = fb.build_transport(25, 100, 5, {1: Q(1), 25: Q(1)}, fb.F1_G_PATTERN, fb.POLE_G_PATTERN)
    transport = [(('f',) + key, row, rhs) for key, row, rhs in rows_f]
    transport += [
        (('g',) + key, {nf + variable: coefficient for variable, coefficient in row.items()}, rhs)
        for key, row, rhs in rows_g
    ]
    pivots, records, selected_minor, records_sha = factor_transport(transport)
    pivot_rhs, compatibility = propagate(records)
    assert not compatibility and len(pivots) == 3470
    free = [variable for variable in range(nf + ng) if variable not in pivots]
    free_parameter = {variable: index for index, variable in enumerate(free)}
    print(f"J raw transport rank={len(pivots)}/{nf+ng};free={len(free)}", flush=True)

    bands = {
        (owner, exponent): section_forms(
            15 if owner == "f" else 25,
            60 if owner == "f" else 100,
            exponent,
            16 if owner == "f" else 26,
            0 if owner == "f" else nf,
            pivots,
            pivot_rhs,
            free_parameter,
        )
        for owner in ("f", "g") for exponent in (1, 2, 3)
    }
    print("J raw transport sections PASS", flush=True)
    configure_qd()
    fast_bands = {key: h_forms(forms) for key, forms in bands.items()}
    raw_t12 = compile_current_degree(
        12,
        *[fast_bands[("f", exponent)] for exponent in (1, 2, 3)],
        *[fast_bands[("g", exponent)] for exponent in (1, 2, 3)],
    )
    raw_t12 = {monomial: HScalar.coerce(coefficient).value for monomial, coefficient in raw_t12.items()}
    raw_record = polynomial_record(raw_t12)
    first_rows = pack("X-2", qd.first_band_polynomials(fast_bands[("f", 1)], fast_bands[("g", 1)]))
    first_pivots, dependent, unit_inverse_count = solve_first(len(free), first_rows)
    incompatibility = [entry for entry in dependent if entry[2]]
    assert not incompatibility
    remainder, quotients = divide_by_echelon(raw_t12, first_pivots)
    relations = lift_quotients(quotients, first_pivots, len(first_rows))
    certificate = replay_source(raw_t12, remainder, relations, first_rows)
    reduced_record = polynomial_record(remainder)

    S = qd.S
    k = HScalar(252) - HScalar(342) * S + HScalar(144) * S**2 - HScalar(36) * S**3
    k_inverse = (
        HScalar(Q(-388, 175625)) * S**5
        + HScalar(Q(738, 35125)) * S**4
        - HScalar(Q(9181, 105375)) * S**3
        + HScalar(Q(40993, 210750)) * S**2
        - HScalar(Q(4948, 21075)) * S
        + HScalar(Q(66812, 526875))
    )
    assert k * k_inverse == HScalar(1)
    assert remainder == {(): -k.value / EJ.coerce(50)}
    assert reduced_record["parameter_free_nonzero"]
    print(f"J raw first rank={len(first_pivots)}/{len(free)}; t12 unit PASS", flush=True)

    output = {
        "verdict": "TD6-C1-J-RAW-TRANSPORT-FIRST-T12-EMPTY",
        "scope": {
            "center": "(C,1,1)",
            "stratum": "4*C^2+20*C+1=0",
            "raw_3602_column_transport_rebuilt": True,
            "adaptive_first_band_rebuilt": True,
            "previous_pole_or_current_parameterizations_used": False,
            "fixed_normalized_section_only": True,
            "family_killed": False,
            "SP2_killed": False,
            "JC2_resolved": False,
        },
        "quotient": {
            "modulus": "4*C^2+20*C+1",
            "irreducible_over_Q": True,
            "irreducible_over_E_assumed": False,
            "all_E_quotient_inverses_Bezout_checked": True,
        },
        "transport": {
            "rank": [len(pivots), nf + ng],
            "free_dimension": len(free),
            "compatibility_count": len(compatibility),
            "selected_minor": qj_record(selected_minor),
            "elimination_records_sha256": records_sha,
        },
        "first": {
            "rank": [len(first_pivots), len(free)],
            "dependent_row_count": len(dependent),
            "incompatibility_count": len(incompatibility),
            "unit_inverse_count": unit_inverse_count,
        },
        "raw_current_t12": raw_record,
        "reduced_current_t12": reduced_record,
        "k": ej_record(k.value),
        "k_inverse": ej_record(k_inverse.value),
        "k_inverse_check": True,
        "first_source_certificate": certificate,
        "stratum_empty_in_fixed_normalized_scope": True,
    }
    print(json.dumps(output, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
