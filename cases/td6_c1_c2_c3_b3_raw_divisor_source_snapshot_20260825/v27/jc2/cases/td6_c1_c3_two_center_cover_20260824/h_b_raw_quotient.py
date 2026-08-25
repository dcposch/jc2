#!/usr/bin/env python3
"""Exact raw TD6 rebuild on H=B=0 over Q[U]/(128U^6-32U^3+1).

This does not specialize a fraction-field echelon.  It rebuilds transport,
the first affine band, and genuine P12 after replacing the center by
(3*u^2, 1, u) in the exact degree-six quotient field.
"""

from fractions import Fraction
from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "replay.py"
SOURCE_SHA256 = "56df638aaa3ae02cf437a32258a920a8a66afb2781c089e30b1774a5b38e65db"
assert sha256(SOURCE.read_bytes()).hexdigest() == SOURCE_SHA256
spec = importlib.util.spec_from_file_location("td6_h_b_raw_source", SOURCE)
r = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = r
spec.loader.exec_module(r)

flint = r.t.flint
MODULUS = flint.fmpq_poly([1, 0, 0, -32, 0, 0, 128])
MODULUS_MPOLY = 128*r.t.U**6 - 32*r.t.U**3 + 1


def to_u_polynomial(value):
    if isinstance(value, KP):
        return value.value
    if isinstance(value, flint.fmpq_poly):
        return value
    if isinstance(value, flint.fmpq_mpoly):
        data = value.to_dict()
        assert all(c_degree == 0 for (c_degree, _), _ in data.items()), value
        degree = max((u_degree for (_, u_degree) in data), default=0)
        coefficients = [flint.fmpq(0) for _ in range(degree + 1)]
        for (_, u_degree), coefficient in data.items():
            coefficients[u_degree] = coefficient
        return flint.fmpq_poly(coefficients)
    if isinstance(value, Fraction):
        return flint.fmpq_poly([
            flint.fmpq(value.numerator, value.denominator)
        ])
    if isinstance(value, flint.fmpq):
        return flint.fmpq_poly([value])
    return flint.fmpq_poly([value]) if value else flint.fmpq_poly()


def to_mpoly(value):
    value = to_u_polynomial(value)
    return r.t.CTX.from_dict({
        (0, degree): coefficient
        for degree, coefficient in enumerate(value)
        if coefficient
    })


class KP:
    """The exact field Q[u]/(128u^6-32u^3+1)."""

    __slots__ = ("value",)
    inverse_count = 0

    def __init__(self, value=0):
        self.value = to_u_polynomial(value) % MODULUS

    @staticmethod
    def coerce(value):
        return value if isinstance(value, KP) else KP(value)

    @property
    def numerator(self):
        return to_mpoly(self.value)

    @property
    def denominator(self):
        return r.t.ONE

    def __add__(self, other):
        return KP(self.value + KP.coerce(other).value)

    __radd__ = __add__

    def __neg__(self):
        return KP(-self.value)

    def __sub__(self, other):
        return self + (-KP.coerce(other))

    def __rsub__(self, other):
        return KP.coerce(other) - self

    def __mul__(self, other):
        return KP(self.value * KP.coerce(other).value)

    __rmul__ = __mul__

    def inverse(self):
        if not self.value:
            raise ZeroDivisionError
        common, inverse, cofactor = self.value.xgcd(MODULUS)
        assert common.degree() == 0 and common[0]
        inverse /= common[0]
        cofactor /= common[0]
        assert inverse * self.value + cofactor * MODULUS == 1
        result = KP(inverse)
        assert self * result == KP(1)
        KP.inverse_count += 1
        return result

    def __truediv__(self, other):
        return self * KP.coerce(other).inverse()

    def __rtruediv__(self, other):
        return KP.coerce(other) / self

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        out, base = KP(1), self
        while exponent:
            if exponent & 1:
                out *= base
            base *= base
            exponent //= 2
        return out

    def __bool__(self):
        return bool(self.value)

    def __eq__(self, other):
        return self.value == KP.coerce(other).value

    def __repr__(self):
        return f"KP({self.value!s})"


def quotient_transport_factor(rows):
    """Exact transport echelon over KP; every nonzero pivot is a unit."""
    pivots, records = {}, []
    for row_index, (key, original_row, _) in enumerate(rows):
        row = {variable: KP(value) for variable, value in original_row.items()}
        factors = []
        while row:
            pivot = min(row)
            if pivot not in pivots:
                break
            multiplier = row[pivot]
            factors.append((pivot, multiplier))
            for variable, coefficient in pivots[pivot].items():
                value = row.get(variable, KP()) - multiplier * coefficient
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
        pivots[pivot] = {
            variable: coefficient * inverse
            for variable, coefficient in row.items()
        }
        records.append((key, "pivot", pivot, lead, factors))
        if row_index % 250 == 0:
            print(
                f"quotient_transport rows={row_index};pivots={len(pivots)}",
                flush=True,
            )
    return pivots, records, [], KP(1)


class RTShim:
    Rat = KP

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


class E2:
    __slots__ = ("value",)

    def __init__(self, value=0):
        if isinstance(value, E2):
            self.value = value.value
        elif isinstance(value, EField):
            assert value.factory is FIELD
            self.value = value
        elif isinstance(value, KP):
            self.value = FIELD.scalar(value)
        else:
            self.value = FIELD.from_e(r.cp.E(value))

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
        result = E2(self.value.inverse())
        assert self * result == E2(1)
        return result

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


def configure_exact_quotient():
    r.t.Rat2 = KP
    r.t.factor = quotient_transport_factor
    r.b.FIELD = FIELD
    r.b.EField = EField
    r.b.E2 = E2
    r.E2 = E2
    r.REVERSE_PIVOTS = False
    r.SPARSE_PIVOTS = False
    r.B_LOCAL_PIVOTS = False
    r.b.REVERSE_PIVOTS = False
    r.b.SPARSE_PIVOTS = False
    r.b.B_LOCAL_PIVOTS = False


def exact_source_replay(polynomial, remainder, relations, first_rows):
    source_identity = {}
    for relation, (_, row, rhs) in zip(relations, first_rows):
        source_identity = r.add(
            source_identity,
            r.multiply(relation, r.source_polynomial(row, rhs)),
        )
    source_target = r.add(polynomial, remainder, E2(-1))
    assert r.clean(source_identity) == r.clean(source_target)
    negative = r.add(source_target, {(): E2(1)})
    assert r.clean(source_identity) != r.clean(negative)
    return source_identity


def main():
    configure_exact_quotient()
    factorization = MODULUS.factor()
    assert (
        len(factorization[1]) == 1
        and factorization[1][0] == (MODULUS, 1)
        and MODULUS.gcd(MODULUS.derivative()) == 1
    )
    u = KP(flint.fmpq_poly([0, 1]))
    assert KP(MODULUS_MPOLY) == KP()
    u_inverse = u.inverse()
    print(f"H_B_modulus={MODULUS}")
    print(f"H_B_modulus_factor={factorization}")
    print("H_B_modulus_irreducible_squarefree=true")
    print(f"H_B_u_inverse={u_inverse.value}")
    print("H_B_raw_quotient_source=true")

    r.fb.CENTER = (3*u**2, KP(1), u)
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
    transport_pivots, records, events, _ = r.t.factor(ordered)
    pivot_rhs, compatibility = r.t.propagate(ordered, records)
    assert not events and not compatibility
    assert len(transport_pivots) == 3470
    free = [
        variable for variable in range(nf + ng)
        if variable not in transport_pivots
    ]
    free_parameter = {variable: index for index, variable in enumerate(free)}
    assert len(free) == 132
    print("H_B raw quotient transport PASS", flush=True)
    print("transport_rank=3470/3602")

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

    r.qd.Dual = E2
    r.qd.Q_PRIME = {0: E2(1), 24: E2(25)}
    first_rows = r.qd.pack(
        'X-2', r.qd.first_band_polynomials(
            bands[('f', 1)], bands[('g', 1)]
        )
    )
    first_pivots, first_factors, incompatibilities = r.solve_cert(first_rows)
    print(f"first_rank={len(first_pivots)}/132")
    print(f"first_incompatibility_count={len(incompatibilities)}")
    print(f"first_pivot_count={len(first_factors)}")
    if incompatibilities:
        for index, (row_index, key, residual, combination) in enumerate(
            incompatibilities
        ):
            inverse = residual.inverse()
            assert residual * inverse == E2(1)
            exact_combination = tuple(
                (
                    source_index,
                    first_rows[source_index][0],
                    r.scalar_exact(coefficient),
                )
                for source_index, coefficient in sorted(combination.items())
            )
            print(f"incompatibility[{index}]_row={row_index};key={key}")
            print(
                f"incompatibility[{index}]_residual_sha256="
                f"{r.scalar_digest(residual)}"
            )
            print(
                f"incompatibility[{index}]_inverse_sha256="
                f"{r.scalar_digest(inverse)}"
            )
            print(
                f"incompatibility[{index}]_source_certificate_sha256="
                f"{sha256(repr(exact_combination).encode()).hexdigest()}"
            )
        print("H_B_first_incompatibility_unit=true")
        print("H_B_stratum_empty=true")
        print("P12_compile_skipped_first_band_empty=true")
        print("family_killed=false")
        print("SP2_killed=false")
        print("JC2_resolved=false")
        print("TD6-C1-C3-H-B-RAW-QUOTIENT PASS")
        return

    raw = r.qd.compile_current(
        *[bands[('f', exponent)] for exponent in (1, 2, 3)],
        *[bands[('g', exponent)] for exponent in (1, 2, 3)],
    )[12]
    polynomial = {
        monomial: E2.coerce(coefficient)
        for monomial, coefficient in raw.items() if coefficient
    }
    assert max(map(len, polynomial)) == 2
    print("H_B raw quotient genuine P12 PASS", flush=True)
    remainder, quotients = r.divide(polynomial, first_pivots)
    relations = r.lift_relations(quotients, first_pivots, len(first_rows))
    exact_source_replay(polynomial, remainder, relations, first_rows)
    S = E2(r.qd.uniform.S_FIELD)
    k = E2(252) - 342*S + 144*S**2 - 36*S**3
    expected = -k / 50
    expected_remainder = remainder == {(): expected}
    constant_unit = False
    if set(remainder) == {()} and remainder[()]:
        inverse = remainder[()].inverse()
        assert remainder[()] * inverse == E2(1)
        constant_unit = True
        print(f"remainder_inverse_sha256={r.scalar_digest(inverse)}")
    source_nonzero_rows = sum(bool(relation) for relation in relations)
    source_multiplier_terms = sum(len(relation) for relation in relations)
    print(f"raw_terms={len(polynomial)}")
    print(f"raw_sha256={r.polynomial_digest(polynomial)}")
    print(f"remainder_terms={len(remainder)}")
    print(f"remainder_degree={max(map(len, remainder), default=-1)}")
    print(f"remainder_sha256={r.polynomial_digest(remainder)}")
    print(f"expected_sha256={r.scalar_digest(expected)}")
    print(f"remainder_is_expected_constant={str(expected_remainder).lower()}")
    print(f"remainder_is_constant_unit={str(constant_unit).lower()}")
    print(f"source_nonzero_rows={source_nonzero_rows}")
    print(f"source_multiplier_terms={source_multiplier_terms}")
    print("source_relation_original_row_replay=true")
    print("source_relation_plus_one_negative_control=true")
    print(f"KP_inverse_count={KP.inverse_count}")
    print(f"H_B_stratum_empty={str(constant_unit).lower()}")
    print("family_killed=false")
    print("SP2_killed=false")
    print("JC2_resolved=false")
    print("TD6-C1-C3-H-B-RAW-QUOTIENT PASS")


if __name__ == '__main__':
    main()
