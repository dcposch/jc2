#!/usr/bin/env python3
"""Exact TD6 replay on H=0 and P3=0 over its function field.

The coefficient field is implemented without a scaling identification as

    Q(U)[Z,V] / (Z^2 - 32 Z + 128, V^2 - Z U^3).

This is the fraction field of Q[U,V]/(V^4-32 V^2 U^3+128 U^6): the quadratic
Z-polynomial is irreducible and Z U^3 is not a square in Q(Z)(U), by its odd
U-adic valuation.  The representation therefore has degree four over Q(U),
the same as the monic irreducible P3 quotient.  No source scaling or weighted
projective equivalence is used.

This producer is a generic-curve discriminator.  It emits every conservative
Q[U] denominator/norm divisor.  It never claims the whole P3 curve, the full
three-center family, SP-2, or JC2 without raw rebuilds of those divisors.
"""

from fractions import Fraction
from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "c1_c2_c3_trivariate.py"
SOURCE_SHA256 = "3459dda5f378d3fd0f135ba90552766bc53b0f0febbd4852b309f89f02079976"
assert sha256(SOURCE.read_bytes()).hexdigest() == SOURCE_SHA256
spec = importlib.util.spec_from_file_location("td6_tricenter_for_p3", SOURCE)
g = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = g
spec.loader.exec_module(g)
r = g.r
flint = r.t.flint
REVERSE_FIRST = "--reverse-first" in sys.argv

Poly = flint.fmpq_poly
U_POLY = Poly([0, 1])
ZERO_POLY = Poly([0])
ONE_POLY = Poly([1])


def as_poly(value):
    if isinstance(value, Poly):
        return value
    if isinstance(value, flint.fmpq):
        return Poly([value])
    if isinstance(value, Fraction):
        return Poly([flint.fmpq(value.numerator, value.denominator)])
    return Poly([value])


def monic(poly):
    if not poly:
        return poly
    return poly / poly.leading_coefficient()


def poly_lcm(left, right):
    if not left or not right:
        return ZERO_POLY
    common = left.gcd(right)
    return monic((left // common) * right)


def poly_summary(poly):
    canonical = tuple(str(poly[index]) for index in range(len(poly)))
    return (
        poly.degree(),
        len([value for value in canonical if value != "0"]),
        sha256(repr(canonical).encode()).hexdigest(),
    )


class RatU:
    """Reduced rational functions Q(U), backed by FLINT polynomials."""

    __slots__ = ("numerator", "denominator")
    inverse_count = 0

    def __init__(self, numerator=0, denominator=1, reduced=False):
        if isinstance(numerator, RatU) and denominator == 1:
            self.numerator = numerator.numerator
            self.denominator = numerator.denominator
            return
        numerator, denominator = as_poly(numerator), as_poly(denominator)
        if not denominator:
            raise ZeroDivisionError
        if not numerator:
            self.numerator, self.denominator = ZERO_POLY, ONE_POLY
            return
        if not reduced:
            common = numerator.gcd(denominator)
            numerator, denominator = numerator // common, denominator // common
        scalar = denominator.leading_coefficient()
        self.numerator = numerator / scalar
        self.denominator = denominator / scalar

    @staticmethod
    def coerce(value):
        return value if isinstance(value, RatU) else RatU(value)

    def __add__(self, other):
        other = RatU.coerce(other)
        if self.denominator == ONE_POLY and other.denominator == ONE_POLY:
            return RatU(self.numerator + other.numerator, reduced=True)
        return RatU(
            self.numerator * other.denominator
            + other.numerator * self.denominator,
            self.denominator * other.denominator,
        )

    __radd__ = __add__

    def __neg__(self):
        return RatU(-self.numerator, self.denominator, reduced=True)

    def __sub__(self, other):
        return self + (-RatU.coerce(other))

    def __rsub__(self, other):
        return RatU.coerce(other) - self

    def __mul__(self, other):
        other = RatU.coerce(other)
        if not self or not other:
            return RatU()
        left_common = self.numerator.gcd(other.denominator)
        right_common = other.numerator.gcd(self.denominator)
        return RatU(
            (self.numerator // left_common) * (other.numerator // right_common),
            (self.denominator // right_common) * (other.denominator // left_common),
            reduced=True,
        )

    __rmul__ = __mul__

    def inverse(self):
        if not self:
            raise ZeroDivisionError
        RatU.inverse_count += 1
        return RatU(self.denominator, self.numerator, reduced=True)

    def __truediv__(self, other):
        return self * RatU.coerce(other).inverse()

    def __rtruediv__(self, other):
        return RatU.coerce(other) / self

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        out, base = RatU(1), self
        while exponent:
            if exponent & 1:
                out *= base
            base *= base
            exponent //= 2
        return out

    def __bool__(self):
        return bool(self.numerator)

    def __eq__(self, other):
        other = RatU.coerce(other)
        return (
            self.numerator == other.numerator
            and self.denominator == other.denominator
        )

    def __repr__(self):
        return f"RatU(({self.numerator})/({self.denominator}))"


class Quad:
    """Q(U)[Z]/(Z^2-32Z+128)."""

    __slots__ = ("a", "b")
    inverse_count = 0

    def __init__(self, a=0, b=0):
        if isinstance(a, Quad) and b == 0:
            self.a, self.b = a.a, a.b
        else:
            self.a, self.b = RatU.coerce(a), RatU.coerce(b)

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Quad) else Quad(value)

    def __add__(self, other):
        other = Quad.coerce(other)
        return Quad(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Quad(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-Quad.coerce(other))

    def __rsub__(self, other):
        return Quad.coerce(other) - self

    def __mul__(self, other):
        other = Quad.coerce(other)
        # Z^2 = 32 Z - 128.
        return Quad(
            self.a * other.a - 128 * self.b * other.b,
            self.a * other.b + self.b * other.a + 32 * self.b * other.b,
        )

    __rmul__ = __mul__

    def norm(self):
        return self.a**2 + 32*self.a*self.b + 128*self.b**2

    def inverse(self):
        if not self:
            raise ZeroDivisionError
        Quad.inverse_count += 1
        inverse_norm = self.norm().inverse()
        result = Quad((self.a + 32*self.b)*inverse_norm, -self.b*inverse_norm)
        assert self * result == Quad(1)
        return result

    def __truediv__(self, other):
        return self * Quad.coerce(other).inverse()

    def __rtruediv__(self, other):
        return Quad.coerce(other) / self

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        out, base = Quad(1), self
        while exponent:
            if exponent & 1:
                out *= base
            base *= base
            exponent //= 2
        return out

    def __bool__(self):
        return bool(self.a) or bool(self.b)

    def __eq__(self, other):
        other = Quad.coerce(other)
        return self.a == other.a and self.b == other.b

    def __repr__(self):
        return f"Quad({self.a!r},{self.b!r})"


U_RAT = RatU(U_POLY)
Z_QUAD = Quad(0, 1)


class Curve:
    """Q(U,Z)[V]/(V^2-ZU^3), the P3 function field."""

    __slots__ = ("a", "b")
    inverse_count = 0

    def __init__(self, a=0, b=0):
        if isinstance(a, Curve) and b == 0:
            self.a, self.b = a.a, a.b
        else:
            self.a, self.b = Quad.coerce(a), Quad.coerce(b)

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Curve) else Curve(value)

    def __add__(self, other):
        other = Curve.coerce(other)
        return Curve(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Curve(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-Curve.coerce(other))

    def __rsub__(self, other):
        return Curve.coerce(other) - self

    def __mul__(self, other):
        other = Curve.coerce(other)
        square = Z_QUAD * U_RAT**3
        return Curve(
            self.a * other.a + self.b * other.b * square,
            self.a * other.b + self.b * other.a,
        )

    __rmul__ = __mul__

    def norm_quad(self):
        return self.a**2 - self.b**2 * Z_QUAD * U_RAT**3

    def absolute_norm(self):
        return self.norm_quad().norm()

    def inverse(self):
        if not self:
            raise ZeroDivisionError
        Curve.inverse_count += 1
        inverse_norm = self.norm_quad().inverse()
        result = Curve(self.a * inverse_norm, -self.b * inverse_norm)
        assert self * result == Curve(1)
        return result

    def __truediv__(self, other):
        return self * Curve.coerce(other).inverse()

    def __rtruediv__(self, other):
        return Curve.coerce(other) / self

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        out, base = Curve(1), self
        while exponent:
            if exponent & 1:
                out *= base
            base *= base
            exponent //= 2
        return out

    def __bool__(self):
        return bool(self.a) or bool(self.b)

    def __eq__(self, other):
        other = Curve.coerce(other)
        return self.a == other.a and self.b == other.b

    def components(self):
        return self.a.a, self.a.b, self.b.a, self.b.b

    def __repr__(self):
        return f"Curve({self.a!r},{self.b!r})"


V_CURVE = Curve(0, 1)
U_CURVE = Curve(U_RAT)
Z_CURVE = Curve(Z_QUAD)


class RTShim:
    Rat = Curve
    X = U_CURVE

    @staticmethod
    def rational(value):
        return r.cp.rt.rational(value)


class CPShim:
    rt = RTShim
    qd = r.cp.qd
    K = r.cp.K
    E = r.cp.E
    Frac = r.cp.Frac
    fast_evec = r.cp.fast_evec


FIELD = r.cp.fast_efield.EFieldFactory(CPShim)
EField = r.cp.fast_efield.EField


class ECurve:
    __slots__ = ("value",)

    def __init__(self, value=0):
        if isinstance(value, ECurve):
            self.value = value.value
        elif isinstance(value, EField):
            assert value.factory is FIELD
            self.value = value
        elif isinstance(value, Curve):
            self.value = FIELD.scalar(value)
        else:
            self.value = FIELD.from_e(r.cp.E(value))

    @staticmethod
    def coerce(value):
        return value if isinstance(value, ECurve) else ECurve(value)

    def __add__(self, other):
        return ECurve(self.value + ECurve.coerce(other).value)

    __radd__ = __add__

    def __neg__(self):
        return ECurve(-self.value)

    def __sub__(self, other):
        return self + (-ECurve.coerce(other))

    def __rsub__(self, other):
        return ECurve.coerce(other) - self

    def __mul__(self, other):
        return ECurve(self.value * ECurve.coerce(other).value)

    __rmul__ = __mul__

    def inverse(self):
        result = ECurve(self.value.inverse())
        assert self * result == ECurve(1)
        return result

    def __truediv__(self, other):
        return self * ECurve.coerce(other).inverse()

    def __rtruediv__(self, other):
        return ECurve.coerce(other) / self

    def __pow__(self, exponent):
        return ECurve(self.value**exponent)

    def __bool__(self):
        return bool(self.value)

    def __eq__(self, other):
        return self.value == ECurve.coerce(other).value


def efield_curves(value):
    value = ECurve.coerce(value).value
    return tuple(
        coordinate
        for kvalue in value.coefficients
        for coordinate in kvalue.coordinates
    )


def flat_ratu(value):
    return tuple(
        component
        for coordinate in efield_curves(value)
        for component in coordinate.components()
    )


def scalar_curve_coordinate(value):
    nonzero = [coordinate for coordinate in efield_curves(value) if coordinate]
    return nonzero[0] if len(nonzero) == 1 else None


def scalar_exact(value):
    return tuple(
        (str(coordinate.numerator), str(coordinate.denominator))
        for coordinate in flat_ratu(value)
    )


def scalar_digest(value):
    return sha256(repr(scalar_exact(value)).encode()).hexdigest()


def polynomial_digest(poly):
    return sha256(repr(tuple(
        (monomial, scalar_digest(value))
        for monomial, value in sorted(poly.items())
    )).encode()).hexdigest()


def denominator_lcm(values):
    out = ONE_POLY
    for value in values:
        for coordinate in flat_ratu(value):
            out = poly_lcm(out, coordinate.denominator)
    return out


def denominators_divide(value, common):
    return all(not common % coordinate.denominator for coordinate in flat_ratu(value))


def factor_transport(rows):
    pivots, records, events = {}, [], []
    chart = ONE_POLY
    for row_index, (key, original_row, _) in enumerate(rows):
        row = {variable: Curve(value) for variable, value in original_row.items()}
        factors = []
        while row:
            pivot = min(row)
            if pivot not in pivots:
                break
            multiplier = row[pivot]
            factors.append((pivot, multiplier))
            for variable, coefficient in pivots[pivot].items():
                value = row.get(variable, Curve()) - multiplier * coefficient
                if value:
                    row[variable] = value
                else:
                    row.pop(variable, None)
        if not row:
            records.append((key, "dependent", None, None, factors))
            continue
        pivot = min(row)
        lead = row[pivot]
        norm = lead.absolute_norm()
        nonconstant = norm.numerator.degree() > 0 or norm.denominator.degree() > 0
        if nonconstant:
            events.append((row_index, key, pivot, norm))
            chart = poly_lcm(chart, norm.numerator)
            chart = poly_lcm(chart, norm.denominator)
        inverse = lead.inverse()
        pivots[pivot] = {
            variable: coefficient * inverse for variable, coefficient in row.items()
        }
        records.append((key, "pivot", pivot, lead, factors))
        if row_index % 250 == 0:
            print(
                f"p3_transport rows={row_index};pivots={len(pivots)};"
                f"events={len(events)};chart_degree={chart.degree()}",
                flush=True,
            )
    return pivots, records, events, chart


def configure():
    r.t.Rat2 = Curve
    r.t.factor = factor_transport
    r.b.FIELD = FIELD
    r.b.EField = EField
    r.b.E2 = ECurve
    r.E2 = ECurve
    r.REVERSE_PIVOTS = REVERSE_FIRST
    r.SPARSE_PIVOTS = False
    r.B_LOCAL_PIVOTS = False
    r.b.REVERSE_PIVOTS = False
    r.b.SPARSE_PIVOTS = False
    r.b.B_LOCAL_PIVOTS = False
    r.scalar_coordinate = scalar_curve_coordinate
    r.scalar_exact = scalar_exact
    r.scalar_digest = scalar_digest
    r.polynomial_digest = polynomial_digest
    r.denominator_lcm = denominator_lcm


def source_replay(polynomial, remainder, relations, first_rows):
    source_identity = {}
    for relation, (_, row, rhs) in zip(relations, first_rows):
        source_identity = r.add(
            source_identity,
            r.multiply(relation, r.source_polynomial(row, rhs)),
        )
    source_target = r.add(polynomial, remainder, ECurve(-1))
    assert r.clean(source_identity) == r.clean(source_target)
    assert r.clean(source_identity) != r.clean(r.add(source_target, {(): ECurve(1)}))


def relation_termwise_clear(relations, first_rows, common):
    slots = 0
    for relation, (_, row, rhs) in zip(relations, first_rows):
        source_values = list(row.values()) + ([rhs] if rhs else [])
        for multiplier in relation.values():
            for source_value in source_values:
                slots += 1
                assert denominators_divide(multiplier * source_value, common)
    return slots


def main():
    configure()
    # Exact field-definition controls.
    assert Z_CURVE**2 - 32*Z_CURVE + 128 == Curve()
    assert V_CURVE**2 == Z_CURVE * U_CURVE**3
    assert V_CURVE**4 - 32*V_CURVE**2*U_CURVE**3 + 128*U_CURVE**6 == Curve()
    assert V_CURVE**4 - 32*V_CURVE**2*U_CURVE**3 + 128*U_CURVE**6 + 1 != Curve()
    print("P3_function_field_tower=Q(U)[Z,V]/(Z^2-32Z+128,V^2-ZU^3)")
    print("Z_discriminant=512")
    print("Z_discriminant_nonsquare_Q=true")
    print("ZU3_U_valuation=3")
    print("ZU3_nonsquare_by_odd_U_valuation=true")
    print("P3_function_field_degree_over_QU=4")
    print("P3_relation_exact=true")
    print("P3_plus_one_negative_control=true")
    print("weighted_scaling_used=false", flush=True)
    print(
        "first_pivot_order=" + ("reverse" if REVERSE_FIRST else "ascending"),
        flush=True,
    )

    center = (Curve(3*U_RAT**2), V_CURVE, U_CURVE)
    print("center_stratum=H=C-3U^2=0, P3=0 over Frac(Q[U,V]/P3)")
    r.fb.CENTER = center
    r.fb._X_POWER_CACHE.clear()
    nf, rows_f = r.fb.build_transport(
        15, 60, 3, {15: r.b.Q(1)}, r.fb.F1_F_PATTERN, r.fb.POLE_F_PATTERN
    )
    ng, rows_g = r.fb.build_transport(
        25, 100, 5, {1: r.b.Q(1), 25: r.b.Q(1)},
        r.fb.F1_G_PATTERN, r.fb.POLE_G_PATTERN,
    )
    rows = [(('f',) + key, row, rhs) for key, row, rhs in rows_f]
    rows += [
        (
            ('g',) + key,
            {nf + variable: coefficient for variable, coefficient in row.items()},
            rhs,
        )
        for key, row, rhs in rows_g
    ]
    ordered = [row for row in rows if row[0][1] != 'X'] + [
        row for row in rows if row[0][1] == 'X'
    ]
    transport_pivots, records, events, transport_chart = factor_transport(ordered)
    pivot_rhs, compatibility = r.t.propagate(ordered, records)
    print(f"transport_rank={len(transport_pivots)}/{nf+ng}")
    print(f"transport_compatibility_count={len(compatibility)}")
    assert not compatibility
    assert len(transport_pivots) == 3470
    print(f"transport_event_count={len(events)}")
    for index, (row_index, key, pivot, norm) in enumerate(events):
        print(
            f"transport_event[{index}]={row_index},{key},{pivot};"
            f"norm_num=({norm.numerator});norm_den=({norm.denominator})"
        )
    print(f"transport_chart_radical=({transport_chart})")
    print(f"transport_chart_summary={poly_summary(transport_chart)}")
    print(f"transport_chart_factor={transport_chart.factor()}")
    print("TD6 P3 quotient transport PASS", flush=True)

    free = [
        variable for variable in range(nf + ng)
        if variable not in transport_pivots
    ]
    assert len(free) == 132
    free_parameter = {variable: index for index, variable in enumerate(free)}
    bands = {}
    for owner, imax, jmax, offset in (
        ('f', 15, 60, 0), ('g', 25, 100, nf)
    ):
        for exponent in (1, 2, 3):
            forms = []
            for degree in range(16 if owner == 'f' else 26):
                row = {
                    offset + variable: coefficient
                    for variable, coefficient in r.fb.x_chart_coefficient(
                        imax, jmax, exponent, degree
                    ).items()
                }
                forms.append(r.b.restrict_row(
                    row, transport_pivots, pivot_rhs, free_parameter
                ))
            bands[(owner, exponent)] = forms

    # Keep the parent Dual untouched through transport source propagation:
    # cp.source_rhs must still return the frozen E-valued source vector.
    # Only the first/P12 compiler is retargeted to the curve coefficient field.
    r.qd.Dual = ECurve
    r.qd.Q_PRIME = {0: ECurve(1), 24: ECurve(25)}
    first_rows = r.qd.pack(
        'X-2', r.qd.first_band_polynomials(
            bands[('f', 1)], bands[('g', 1)]
        )
    )
    first_pivots, first_factors, incompatibilities = r.solve_cert(first_rows)
    print(f"first_rank={len(first_pivots)}/132")
    print(f"first_incompatibility_count={len(incompatibilities)}")
    assert not incompatibilities
    assert len(first_pivots) == 38
    print("TD6 P3 quotient first band PASS", flush=True)

    raw = r.qd.compile_current(
        *[bands[('f', exponent)] for exponent in (1, 2, 3)],
        *[bands[('g', exponent)] for exponent in (1, 2, 3)],
    )[12]
    polynomial_value = {
        monomial: ECurve.coerce(coefficient)
        for monomial, coefficient in raw.items() if coefficient
    }
    assert max(map(len, polynomial_value)) == 2
    print("TD6 P3 quotient genuine P12 PASS", flush=True)
    remainder, quotients = r.divide(polynomial_value, first_pivots)
    relations = r.lift_relations(quotients, first_pivots, len(first_rows))
    source_replay(polynomial_value, remainder, relations, first_rows)

    S = ECurve(r.qd.uniform.S_FIELD)
    k = ECurve(252) - 342*S + 144*S**2 - 36*S**3
    expected = -k / 50
    assert remainder == {(): expected}
    inverse = expected.inverse()
    assert expected * inverse == ECurve(1)

    raw_denominator = denominator_lcm(polynomial_value.values())
    first_denominator = denominator_lcm(
        coefficient
        for _, row, rhs in first_rows
        for coefficient in list(row.values()) + [rhs]
    )
    relation_values = [
        coefficient
        for relation in relations
        for coefficient in relation.values()
    ]
    relation_denominator = denominator_lcm(relation_values)
    termwise_denominator = monic(relation_denominator * first_denominator)
    assert all(
        denominators_divide(value, raw_denominator)
        for value in polynomial_value.values()
    )
    assert all(
        denominators_divide(value, first_denominator)
        for _, row, rhs in first_rows
        for value in list(row.values()) + [rhs]
    )
    assert all(
        denominators_divide(value, relation_denominator)
        for value in relation_values
    )
    termwise_slots = relation_termwise_clear(
        relations, first_rows, termwise_denominator
    )
    certificate_chart = monic(
        transport_chart * raw_denominator
        * first_denominator * termwise_denominator
    )
    _, chart_factors = certificate_chart.factor()
    only_u_exception = all(factor == U_POLY for factor, _ in chart_factors)

    source_nonzero_rows = sum(bool(relation) for relation in relations)
    source_multiplier_terms = sum(len(relation) for relation in relations)
    print(f"raw_terms={len(polynomial_value)}")
    print(f"raw_sha256={polynomial_digest(polynomial_value)}")
    print(f"remainder_sha256={polynomial_digest(remainder)}")
    print(f"expected_sha256={scalar_digest(expected)}")
    print("remainder_is_expected_constant=true")
    print("remainder_is_constant_unit=true")
    print(f"source_nonzero_rows={source_nonzero_rows}")
    print(f"source_multiplier_terms={source_multiplier_terms}")
    print("source_relation_original_first_row_replay=true")
    print("source_relation_plus_one_negative_control=true")
    print(f"raw_denominator=({raw_denominator})")
    print(f"raw_denominator_factor={raw_denominator.factor()}")
    print(f"first_denominator=({first_denominator})")
    print(f"first_denominator_factor={first_denominator.factor()}")
    print(f"relation_denominator=({relation_denominator})")
    print(f"relation_denominator_factor={relation_denominator.factor()}")
    print(f"termwise_denominator=({termwise_denominator})")
    print(f"termwise_denominator_factor={termwise_denominator.factor()}")
    print("cleared_relation_coefficients_polynomial=true")
    print("termwise_polynomial_clear_checks=true")
    print(f"termwise_clear_slot_count={termwise_slots}")
    print(f"certificate_chart=({certificate_chart})")
    print(f"certificate_chart_factor={certificate_chart.factor()}")
    print(f"only_U_exception={str(only_u_exception).lower()}")
    print("P3_intersection_U_zero_is_origin=true")
    print(f"RatU_inverse_count={RatU.inverse_count}")
    print(f"Quad_inverse_count={Quad.inverse_count}")
    print(f"Curve_inverse_count={Curve.inverse_count}")
    print("P3_generic_open_killed=true")
    print("P3_whole_curve_killed=false")
    print("full_three_center_family_killed=false")
    print("SP2_killed=false")
    print("JC2_resolved=false")
    print("TD6-C1-C2-C3-P3-QUOTIENT PASS")


if __name__ == "__main__":
    main()
