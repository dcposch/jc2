#!/usr/bin/env python3
"""Exact generic three-center TD6 q3 dual-number discriminator.

The base is the source-typed section

    y=s^-1, x=C*s+V*s^2+U*s^3+t*s^4,
    p=t^15, q_gamma=t+gamma*t^3+t^25.

Arithmetic is over E(C,V,U)[eps]/eps^2 at gamma=eps.  The homogeneous
transport matrix is gamma-independent, but its affine right hand side is
not.  The first-J matrix and the genuine current P12 both vary through
q_gamma'=1+3*gamma*t^2+25*t^24.  Elimination is performed over the dual ring
using only pivots with nonzero base value, so the differentiated pivot rows
and source multipliers retain all lambda-prime terms.

This is a first-order source-support discriminator at beta=0 on
D(U*(C-3U^2)*B3), not a gamma-family or neighborhood theorem.  Since the
base source ideal already contains a unit, dual-number emptiness is formally
expected; the value here is the exact q3 support, varying-echelon, and
denominator audit before an untruncated simultaneous-modulus gate.
"""

from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
TRI_PATH = (
    HERE.parent / "td6_c1_c3_two_center_cover_20260824"
    / "c1_c2_c3_trivariate.py"
)
TRI_SHA256 = "1fb512643f31b4eda6c0e96ca1adbfe3e79599986c7c095b825605a4145fdaea"
assert sha256(TRI_PATH.read_bytes()).hexdigest() == TRI_SHA256
spec = importlib.util.spec_from_file_location("td6_a3_gamma_tri_source", TRI_PATH)
tri = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = tri
spec.loader.exec_module(tri)

tri.configure()
r, Rat3, E3 = tri.r, tri.Rat3, tri.E3
C, V, U = tri.C, tri.V, tri.U
B3 = tri.B3
H = C - 3*U**2


class EDual:
    """E(C,V,U)[eps]/eps^2, with derivative taken in gamma."""

    __slots__ = ("value", "derivative")

    def __init__(self, value=0, derivative=0):
        if isinstance(value, EDual):
            self.value = value.value
            self.derivative = value.derivative
        else:
            self.value = E3.coerce(value)
            self.derivative = E3.coerce(derivative)

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
            raise ZeroDivisionError("zero-base dual pivot")
        inverse = self.value.inverse()
        return EDual(inverse, -(inverse * inverse) * self.derivative)

    def __truediv__(self, other):
        return self * EDual.coerce(other).inverse()

    def __rtruediv__(self, other):
        return EDual.coerce(other) / self

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        out, base = EDual(1), self
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


def clean(poly):
    return {monomial: value for monomial, value in poly.items() if value}


def add(left, right, scale=1):
    scale = EDual.coerce(scale)
    out = dict(left)
    for monomial, coefficient in right.items():
        value = out.get(monomial, EDual()) + scale * coefficient
        if value:
            out[monomial] = value
        else:
            out.pop(monomial, None)
    return out


def multiply(left, right):
    out = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial = tuple(sorted(left_monomial + right_monomial))
            value = (
                out.get(monomial, EDual())
                + left_coefficient * right_coefficient
            )
            if value:
                out[monomial] = value
            else:
                out.pop(monomial, None)
    return out


def source_polynomial(row, rhs):
    out = {(): -EDual.coerce(rhs)} if rhs else {}
    for variable, coefficient in row.items():
        coefficient = EDual.coerce(coefficient)
        if coefficient:
            out[(variable,)] = coefficient
    return out


def split_polynomial(poly, derivative=False):
    return clean({
        monomial: (coefficient.derivative if derivative else coefficient.value)
        for monomial, coefficient in poly.items()
    })


def scalar(value):
    return E3(tri.FIELD.scalar(Rat3.coerce(value)))


def from_vector(vector):
    return E3(tri.FIELD.from_coordinates(vector))


ZERO_VECTOR = tuple(Rat3() for _ in range(18))
ONE_VECTOR = r.t.source_vector(("g", "X", 0, 1))
assert len(ONE_VECTOR) == 18 and from_vector(ONE_VECTOR) == E3(1)


def source_vector_gamma(key):
    base = r.t.source_vector(key)
    derivative = (
        ONE_VECTOR if key == ("g", "X", 0, 3) else ZERO_VECTOR
    )
    return base, derivative


def vector_scale(vector, coefficient):
    return tuple(coefficient * coordinate for coordinate in vector)


def vector_subtract(left, right):
    return tuple(a - b for a, b in zip(left, right))


def propagate_gamma(rows, records):
    pivot_rhs, compatibility = {}, []
    for source_row, record in zip(rows, records):
        source_key, _, _ = source_row
        key, kind, pivot, lead, factors = record
        assert source_key == key
        base, derivative = source_vector_gamma(key)
        for old, factor in factors:
            old_base, old_derivative = pivot_rhs[old]
            base = vector_subtract(base, vector_scale(old_base, factor))
            derivative = vector_subtract(
                derivative, vector_scale(old_derivative, factor)
            )
        if kind == "pivot":
            inverse = lead.inverse()
            pivot_rhs[pivot] = (
                vector_scale(base, inverse),
                vector_scale(derivative, inverse),
            )
        elif any(base) or any(derivative):
            compatibility.append((key, base, derivative))
    return pivot_rhs, compatibility


def restrict_row_gamma(original_row, pivots, pivot_rhs, free_parameter):
    row = {
        variable: Rat3.coerce(coefficient)
        for variable, coefficient in original_row.items() if coefficient
    }
    base, derivative = ZERO_VECTOR, ZERO_VECTOR
    for pivot in sorted(pivots):
        factor = row.pop(pivot, None)
        if factor is None or not factor:
            continue
        rhs_base, rhs_derivative = pivot_rhs[pivot]
        base = tuple(
            old + factor*coordinate for old, coordinate in zip(base, rhs_base)
        )
        derivative = tuple(
            old + factor*coordinate
            for old, coordinate in zip(derivative, rhs_derivative)
        )
        for variable, coefficient in pivots[pivot].items():
            if variable == pivot:
                continue
            value = row.get(variable, Rat3()) - factor*coefficient
            if value:
                row[variable] = value
            else:
                row.pop(variable, None)
    assert all(variable in free_parameter for variable in row)
    return (
        EDual(from_vector(base), from_vector(derivative)),
        {
            free_parameter[variable]: EDual(scalar(coefficient))
            for variable, coefficient in row.items()
        },
    )


def configure_qd_gamma(direct_qprime=True):
    qd = r.qd
    qd.Dual = EDual
    qd.B = EDual(0, 1)
    qd.S = EDual(E3(qd.uniform.S_FIELD))
    qd.D = EDual(E3(qd.uniform.D_FIELD))
    qd.L = EDual(E3(qd.uniform.L_FIELD))
    qd.A = EDual(E3(qd.uniform.A_FIELD))
    qd.Q_PRIME = {0: EDual(1), 24: EDual(25)}
    if direct_qprime:
        qd.Q_PRIME[2] = EDual(0, 3)
    qd.R = qd.multiply(
        qd.multiply([EDual(-1), EDual(1)], [EDual(-1), EDual(1)]),
        [qd.D, -qd.S, EDual(1)],
    )
    qd.R3, qd.R5 = qd.power(qd.R, 3), qd.power(qd.R, 5)
    qd.POLE_F = {1: -(qd.L**3)*qd.A, 6: qd.L**3}
    qd.POLE_G = {
        0: EDual(r.b.Q(5, 9))*qd.L**5*qd.A**2,
        5: EDual(r.b.Q(-5, 3))*qd.L**5*qd.A,
        10: qd.L**5,
    }


def solve_cert_dual(rows):
    pivots, factors, dependent = {}, [], []
    source = [
        (
            key,
            {variable: EDual.coerce(value) for variable, value in row.items()},
            EDual.coerce(rhs),
        )
        for key, row, rhs in rows
    ]
    for row_index, (key, original_row, original_rhs) in enumerate(source):
        row, rhs = dict(original_row), original_rhs
        combination = {row_index: EDual(1)}
        while True:
            pivot = next(
                (
                    variable for variable in pivots
                    if variable in row and row[variable]
                ),
                None,
            )
            if pivot is None:
                break
            factor = row[pivot]
            old_row, old_rhs, old_combination = pivots[pivot]
            for variable, coefficient in old_row.items():
                value = row.get(variable, EDual()) - factor*coefficient
                if value:
                    row[variable] = value
                else:
                    row.pop(variable, None)
            rhs -= factor*old_rhs
            for old_index, coefficient in old_combination.items():
                value = combination.get(old_index, EDual()) - factor*coefficient
                if value:
                    combination[old_index] = value
                else:
                    combination.pop(old_index, None)

        base_variables = [
            variable for variable, coefficient in row.items()
            if coefficient.value
        ]
        if not base_variables:
            derivative_only = {
                variable: coefficient.derivative
                for variable, coefficient in row.items()
                if coefficient.derivative
            }
            replay = {}
            for source_index, coefficient in combination.items():
                _, source_row, source_rhs = source[source_index]
                replay = add(
                    replay,
                    source_polynomial(source_row, source_rhs),
                    coefficient,
                )
            assert clean(replay) == clean(source_polynomial(row, rhs))
            dependent.append((row_index, key, rhs, derivative_only, combination))
            continue

        pivot = min(base_variables)
        lead = row[pivot]
        inverse = lead.inverse()
        pivots[pivot] = (
            {variable: coefficient*inverse for variable, coefficient in row.items()},
            rhs*inverse,
            {index: coefficient*inverse for index, coefficient in combination.items()},
        )
        factors.append((row_index, key, pivot, lead))

    for pivot, (row, rhs, combination) in pivots.items():
        replay = {}
        for source_index, coefficient in combination.items():
            _, source_row, source_rhs = source[source_index]
            replay = add(
                replay,
                source_polynomial(source_row, source_rhs),
                coefficient,
            )
        assert clean(replay) == clean(source_polynomial(row, rhs)), pivot
    return pivots, factors, dependent


def divide_dual(polynomial, pivots):
    remainder, quotients = dict(polynomial), {}
    normalized = {
        pivot: source_polynomial(row, rhs)
        for pivot, (row, rhs, _) in pivots.items()
    }
    for pivot in sorted(pivots):
        quotient = {}
        while True:
            targets = sorted(
                monomial for monomial, coefficient in remainder.items()
                if coefficient and pivot in monomial
            )
            if not targets:
                break
            monomial = targets[0]
            coefficient = remainder[monomial]
            reduced = list(monomial)
            reduced.remove(pivot)
            multiplier = {tuple(reduced): coefficient}
            quotient = add(quotient, multiplier)
            remainder = add(
                remainder, multiply(multiplier, normalized[pivot]), -1
            )
        if quotient:
            quotients[pivot] = quotient
    replay = dict(remainder)
    for pivot, quotient in quotients.items():
        replay = add(replay, multiply(quotient, normalized[pivot]))
    assert clean(replay) == clean(polynomial)
    return remainder, quotients


def lift_relations_dual(quotients, pivots, nrows):
    relations = [{} for _ in range(nrows)]
    for pivot, quotient in quotients.items():
        _, _, combination = pivots[pivot]
        for row_index, coefficient in combination.items():
            relations[row_index] = add(
                relations[row_index], quotient, coefficient
            )
    return relations


def exact_source_replay(polynomial, remainder, relations, first_rows):
    source_identity = {}
    for relation, (_, row, rhs) in zip(relations, first_rows):
        source_identity = add(
            source_identity,
            multiply(relation, source_polynomial(row, rhs)),
        )
    target = add(polynomial, remainder, -1)
    assert clean(source_identity) == clean(target)
    assert clean(source_identity) != clean(add(target, {(): EDual(1)}))


def e3_digest(value):
    return r.scalar_digest(E3.coerce(value))


def polynomial_digest(poly):
    return r.polynomial_digest({
        monomial: E3.coerce(value) for monomial, value in poly.items()
    })


def denominator_lcm(values):
    return r.denominator_lcm(E3.coerce(value) for value in values)


def values(polynomials):
    for polynomial in polynomials:
        yield from polynomial.values()


def factors_only_allowed(polynomial):
    if not polynomial or polynomial.total_degree() == 0:
        return True
    _, factors = polynomial.factor()
    return all(factor in (U, H, B3) for factor, _ in factors)


def polynomial_inverse_of_dual_unit(remainder):
    assert set(split_polynomial(remainder)) == {()}
    base = remainder[()].value
    inverse = base.inverse()
    out = {(): EDual(inverse)}
    for monomial, derivative in split_polynomial(remainder, True).items():
        correction = -(inverse*inverse)*derivative
        if monomial == ():
            out[()] = EDual(inverse, correction)
        else:
            out[monomial] = EDual(0, correction)
    product = clean(multiply(remainder, out))
    assert product == {(): EDual(1)}
    return out


def main():
    print("gamma_parameter_name=gamma")
    print("q_gamma=t+gamma*t^3+t^25")
    print("q_gamma_prime=1+3*gamma*t^2+25*t^24")
    print("base_q2_beta=0")
    print("source_center=(C,V,U)")
    print("source_p_boundary=t^15_fixed")
    print("source_dead_stretch=0_fixed")
    print("source_F1_orbit=frozen")
    print("source_pole_scale_and_data=frozen")
    print("q3_source_license=degree25_boundary_coefficient_after_q0_q1_normalization")
    print("target_shear_absorption=false_by_frozen_orbit_audit")
    print("scope_open=D(U*(C-3U^2)*B3)")
    print("B3_divisor_name_reserved_not_gamma=true", flush=True)

    r.fb.CENTER = (Rat3(C), Rat3(V), Rat3(U))
    r.fb._X_POWER_CACHE.clear()
    nf, rows_f = r.fb.build_transport(
        15, 60, 3, {15: r.b.Q(1)},
        r.fb.F1_F_PATTERN, r.fb.POLE_F_PATTERN,
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
    transport_pivots, records, events, transport_determinant = (
        tri.factor_transport(ordered)
    )
    pivot_rhs, transport_compatibility = propagate_gamma(ordered, records)
    assert not transport_compatibility
    assert len(transport_pivots) == 3470
    free = [
        variable for variable in range(nf + ng)
        if variable not in transport_pivots
    ]
    free_parameter = {variable: index for index, variable in enumerate(free)}
    assert len(free) == 132
    transport_gamma_rhs_pivots = sum(
        any(derivative) for _, derivative in pivot_rhs.values()
    )
    assert transport_gamma_rhs_pivots
    print(f"transport_rank={len(transport_pivots)}/{nf+ng}")
    print(f"transport_event_count={len(events)}")
    print(f"transport_gamma_rhs_pivot_count={transport_gamma_rhs_pivots}")
    print("transport_matrix_gamma_derivative_zero=true")
    print("transport_rhs_gamma_derivative_retained=true", flush=True)

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
                forms.append(restrict_row_gamma(
                    row, transport_pivots, pivot_rhs, free_parameter
                ))
            bands[(owner, exponent)] = forms
    band_gamma_constant_count = sum(
        bool(constant.derivative)
        for forms in bands.values() for constant, _ in forms
    )
    assert band_gamma_constant_count
    print(f"transport_section_gamma_constant_count={band_gamma_constant_count}")

    configure_qd_gamma(direct_qprime=True)
    first_rows = r.qd.pack(
        'X-2', r.qd.first_band_polynomials(
            bands[('f', 1)], bands[('g', 1)]
        )
    )
    first_gamma_coefficient_count = sum(
        bool(coefficient.derivative)
        for _, row, rhs in first_rows
        for coefficient in list(row.values()) + [rhs]
    )
    assert first_gamma_coefficient_count

    configure_qd_gamma(direct_qprime=False)
    first_rows_no_direct_qprime = r.qd.pack(
        'X-2', r.qd.first_band_polynomials(
            bands[('f', 1)], bands[('g', 1)]
        )
    )
    first_gamma_no_direct = sum(
        bool(coefficient.derivative)
        for _, row, rhs in first_rows_no_direct_qprime
        for coefficient in list(row.values()) + [rhs]
    )
    assert first_rows_no_direct_qprime != first_rows
    assert first_gamma_no_direct < first_gamma_coefficient_count
    configure_qd_gamma(direct_qprime=True)
    print(f"first_gamma_coefficient_count={first_gamma_coefficient_count}")
    print(f"first_gamma_without_direct_qprime_count={first_gamma_no_direct}")
    print("direct_qprime_omission_negative_control=true", flush=True)

    first_pivots, first_factors, first_dependent = solve_cert_dual(first_rows)
    assert len(first_pivots) == 38
    assert all(
        not rhs and not derivative_only
        for _, _, rhs, derivative_only, _ in first_dependent
    )
    first_minor = EDual(1)
    for _, _, _, lead in first_factors:
        first_minor *= lead
    print(f"first_rank={len(first_pivots)}/132")
    print(f"first_dependent_count={len(first_dependent)}")
    print(f"first_minor_base_sha256={e3_digest(first_minor.value)}")
    print(f"first_minor_gamma_sha256={e3_digest(first_minor.derivative)}")
    print("first_dual_original_row_replay=true", flush=True)

    raw = r.qd.compile_current(
        *[bands[('f', exponent)] for exponent in (1, 2, 3)],
        *[bands[('g', exponent)] for exponent in (1, 2, 3)],
    )[12]
    polynomial = {
        monomial: EDual.coerce(coefficient)
        for monomial, coefficient in raw.items() if coefficient
    }
    raw_base = split_polynomial(polynomial)
    raw_gamma = split_polynomial(polynomial, True)
    assert len(raw_base) == 2893
    assert polynomial_digest(raw_base) == (
        "8d5c3550fbad393c1e13061d9934ed79e29261db378f1d344c4ea5e587e704da"
    )
    assert raw_gamma
    print("genuine_P12_source_compiler=true")
    print(f"raw_base_terms={len(raw_base)}")
    print(f"raw_gamma_terms={len(raw_gamma)}")
    print(f"raw_base_sha256={polynomial_digest(raw_base)}")
    print(f"raw_gamma_sha256={polynomial_digest(raw_gamma)}", flush=True)

    remainder, quotients = divide_dual(polynomial, first_pivots)
    relations = lift_relations_dual(quotients, first_pivots, len(first_rows))
    exact_source_replay(polynomial, remainder, relations, first_rows)
    remainder_base = split_polynomial(remainder)
    remainder_gamma = split_polynomial(remainder, True)
    S = E3(r.qd.uniform.S_FIELD)
    k = E3(252) - 342*S + 144*S**2 - 36*S**3
    expected = -k/50
    assert remainder_base == {(): expected}
    assert polynomial_digest(remainder_base) == (
        "93121eef14c472c3c55b7acaeb1d0eff73b77d462ad8d5b197e8e21b9cda89c4"
    )
    inverse = polynomial_inverse_of_dual_unit(remainder)
    print(f"remainder_base_terms={len(remainder_base)}")
    print(f"remainder_gamma_terms={len(remainder_gamma)}")
    print(f"remainder_gamma_degree={max(map(len, remainder_gamma), default=-1)}")
    print(f"remainder_base_sha256={polynomial_digest(remainder_base)}")
    print(f"remainder_gamma_sha256={polynomial_digest(remainder_gamma)}")
    print(f"dual_unit_inverse_terms={len(inverse)}")
    print("dual_remainder_base_is_minus_k_over_50=true")
    print("dual_remainder_is_unit_exactly=true", flush=True)

    source_identity = {}
    lambda0_bprime = {}
    lambdaprime_b0 = {}
    lambda_prime_support = 0
    lambda_zero_support = 0
    termwise_slots = 0
    termwise_values = []
    for relation, (_, row, rhs) in zip(relations, first_rows):
        source_row = source_polynomial(row, rhs)
        relation_base = split_polynomial(relation)
        relation_gamma = split_polynomial(relation, True)
        row_base = split_polynomial(source_row)
        row_gamma = split_polynomial(source_row, True)
        if relation_base:
            lambda_zero_support += 1
        if relation_gamma:
            lambda_prime_support += 1
        lambda0_bprime = r.add(
            lambda0_bprime,
            r.multiply(relation_base, row_gamma),
        )
        lambdaprime_b0 = r.add(
            lambdaprime_b0,
            r.multiply(relation_gamma, row_base),
        )
        source_identity = r.add(
            source_identity,
            r.add(
                r.multiply(relation_base, row_gamma),
                r.multiply(relation_gamma, row_base),
            ),
        )
        for multiplier in relation.values():
            for source_value in source_row.values():
                termwise_values.extend([
                    multiplier.value*source_value.derivative,
                    multiplier.derivative*source_value.value,
                ])
                termwise_slots += 2
    derivative_target = r.add(raw_gamma, remainder_gamma, E3(-1))
    assert r.clean(source_identity) == r.clean(derivative_target)
    assert lambdaprime_b0
    assert r.clean(lambda0_bprime) != r.clean(derivative_target)
    print(f"lambda_zero_source_row_support={lambda_zero_support}")
    print(f"lambda_prime_source_row_support={lambda_prime_support}")
    print(f"lambda0_bprime_terms={len(lambda0_bprime)}")
    print(f"lambdaprime_b0_terms={len(lambdaprime_b0)}")
    print(f"lambda0_bprime_sha256={polynomial_digest(lambda0_bprime)}")
    print(f"lambdaprime_b0_sha256={polynomial_digest(lambdaprime_b0)}")
    print("derivative_source_identity_exact=true")
    print("lambda_prime_omission_negative_control=true", flush=True)

    relation_values = list(values(relations))
    first_values = [
        coefficient
        for _, row, rhs in first_rows
        for coefficient in list(row.values()) + [rhs]
    ]
    raw_base_den = denominator_lcm(raw_base.values())
    raw_gamma_den = denominator_lcm(raw_gamma.values())
    first_base_den = denominator_lcm(value.value for value in first_values)
    first_gamma_den = denominator_lcm(value.derivative for value in first_values)
    relation_base_den = denominator_lcm(value.value for value in relation_values)
    relation_gamma_den = denominator_lcm(
        value.derivative for value in relation_values
    )
    termwise_den = denominator_lcm(termwise_values)
    denominators = {
        "raw_base": raw_base_den,
        "raw_gamma": raw_gamma_den,
        "first_base": first_base_den,
        "first_gamma": first_gamma_den,
        "relation_base": relation_base_den,
        "relation_gamma": relation_gamma_den,
        "termwise_dual": termwise_den,
    }
    assert relation_base_den == B3*U**2*H**2/4
    assert all(factors_only_allowed(value) for value in denominators.values())
    for name, value in denominators.items():
        print(f"{name}_denominator=({value})")
        print(f"{name}_denominator_factor={value.factor()}")
        print(f"{name}_denominator_summary={tri.polynomial_summary(value)}")
    print(f"termwise_dual_slot_count={termwise_slots}")
    print("dual_denominator_radical_subset_U_H_B3=true")
    print("dual_termwise_polynomial_clearing_exact=true", flush=True)

    source_nonzero_rows = sum(bool(relation) for relation in relations)
    source_union_multiplier_terms = sum(len(relation) for relation in relations)
    source_base_multiplier_terms = sum(
        len(split_polynomial(relation)) for relation in relations
    )
    source_gamma_support_terms = sum(
        len(split_polynomial(relation, True)) for relation in relations
    )
    source_gamma_coefficient_count = sum(
        bool(value.derivative)
        for relation in relations for value in relation.values()
    )
    assert source_nonzero_rows == 28
    # The frozen 1489 count is the gamma=0 projection.  The exact varying
    # multipliers acquire additional gamma-only monomials; their union support
    # is intentionally not asserted equal to the base projection.
    assert source_base_multiplier_terms == 1489
    assert source_gamma_support_terms
    assert source_gamma_coefficient_count
    print(f"source_nonzero_rows={source_nonzero_rows}")
    print(f"source_base_multiplier_terms={source_base_multiplier_terms}")
    print(f"source_gamma_support_terms={source_gamma_support_terms}")
    print(f"source_union_multiplier_terms={source_union_multiplier_terms}")
    print(f"source_gamma_coefficient_count={source_gamma_coefficient_count}")
    print("source_multiplier_base_projection_sentinel=true")
    print("fixed_A3_q2_beta_slice=dependency_V76_provisional_complete_union")
    print("dual_emptiness_is_automatic_over_unit_base_ideal=true")
    print("result_use=source_support_degree_denominator_discriminator_only")
    print("first_order_generic_open_empty=true")
    print("gamma_independent_unit_identity=false")
    print("finite_gamma_neighborhood_killed=false")
    print("full_gamma_family_killed=false")
    print("full_four_parameter_family_killed=false")
    print("whole_TD6_killed=false")
    print("SP2_killed=false")
    print("JC2_resolved=false")
    print("TD6-C1-C2-C3-Q3-GAMMA-DUAL-ADJOINT PASS")


if __name__ == "__main__":
    main()
