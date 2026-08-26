#!/usr/bin/env python3
"""Exact simultaneous tangent/conormal discriminator for all licensed q jets.

The coefficient ring is the square-zero extension

    E(C,V,U) + direct_sum_e E(C,V,U)*eps_e,

for e=2,...,14,16,...,24.  Every eps product is zero.  This is one joint
vector-AD run, not 22 point samples.  It retains exact transport RHS source
keys, every direct q-prime term, differentiated pivots, and source-row
combinations.

Modes:

* p12: genuine P12 reduction against original first rows for all columns;
* staged: first -> previous/pole -> current compatibility/conormal table.

This is a source-support and scheduling discriminator at the already empty
fixed-A3 base.  Dual emptiness is automatic and gives no family theorem.
"""

from hashlib import sha256
import importlib.util
import os
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
V77_PATH = (
    HERE.parent / "td6_c1_c2_c3_q3_gamma_dual_20260825" / "replay.py"
)
V77_SHA256 = "5e088d8c9b9f7f4f74de108c816f51e5f69d477572fa8b7ec0cf475efcb1ec22"
assert sha256(V77_PATH.read_bytes()).hexdigest() == V77_SHA256
spec = importlib.util.spec_from_file_location("td6_v78_v77_parent", V77_PATH)
v77 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = v77
spec.loader.exec_module(v77)

tri, r = v77.tri, v77.r
Rat3, E3 = v77.Rat3, v77.E3
C, V, U, B3, H = v77.C, v77.V, v77.U, v77.B3, v77.H
qd, nr = r.qd, r.qd.nr

Q_EXPONENTS = tuple(range(2, 15)) + tuple(range(16, 25))
assert len(Q_EXPONENTS) == 22 and 15 not in Q_EXPONENTS


class EJet:
    """Square-zero jet with sparse derivatives keyed by q exponent."""

    __slots__ = ("value", "derivatives")

    def __init__(self, value=0, derivatives=None):
        if isinstance(value, EJet):
            self.value = value.value
            self.derivatives = dict(value.derivatives)
            if derivatives:
                for exponent, coefficient in derivatives.items():
                    coefficient = E3.coerce(coefficient)
                    total = self.derivatives.get(exponent, E3()) + coefficient
                    if total:
                        self.derivatives[exponent] = total
                    else:
                        self.derivatives.pop(exponent, None)
            return
        self.value = E3.coerce(value)
        self.derivatives = {}
        if derivatives:
            for exponent, coefficient in derivatives.items():
                assert exponent in Q_EXPONENTS
                coefficient = E3.coerce(coefficient)
                if coefficient:
                    self.derivatives[exponent] = coefficient

    @staticmethod
    def coerce(value):
        return value if isinstance(value, EJet) else EJet(value)

    @staticmethod
    def direction(exponent, coefficient=1):
        return EJet(0, {exponent: E3.coerce(coefficient)})

    def __add__(self, other):
        other = EJet.coerce(other)
        derivatives = dict(self.derivatives)
        for exponent, coefficient in other.derivatives.items():
            total = derivatives.get(exponent, E3()) + coefficient
            if total:
                derivatives[exponent] = total
            else:
                derivatives.pop(exponent, None)
        return EJet(self.value + other.value, derivatives)

    __radd__ = __add__

    def __neg__(self):
        return EJet(-self.value, {
            exponent: -coefficient
            for exponent, coefficient in self.derivatives.items()
        })

    def __sub__(self, other):
        return self + (-EJet.coerce(other))

    def __rsub__(self, other):
        return EJet.coerce(other) - self

    def __mul__(self, other):
        other = EJet.coerce(other)
        derivatives = {}
        for exponent in self.derivatives.keys() | other.derivatives.keys():
            coefficient = (
                self.derivatives.get(exponent, E3()) * other.value
                + self.value * other.derivatives.get(exponent, E3())
            )
            if coefficient:
                derivatives[exponent] = coefficient
        return EJet(self.value * other.value, derivatives)

    __rmul__ = __mul__

    def inverse(self):
        if not self.value:
            raise ZeroDivisionError("zero-base jet pivot")
        inverse = self.value.inverse()
        return EJet(inverse, {
            exponent: -(inverse*inverse)*coefficient
            for exponent, coefficient in self.derivatives.items()
        })

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
        return bool(self.value) or bool(self.derivatives)

    def __eq__(self, other):
        other = EJet.coerce(other)
        return self.value == other.value and self.derivatives == other.derivatives

    def __repr__(self):
        entries = ",".join(
            f"{exponent}:{coefficient!r}"
            for exponent, coefficient in sorted(self.derivatives.items())
        )
        return f"EJet({self.value!r};{{{entries}}})"


def clean(polynomial):
    return {monomial: coefficient for monomial, coefficient in polynomial.items()
            if coefficient}


def add(left, right, scale=1):
    scale = EJet.coerce(scale)
    out = dict(left)
    for monomial, coefficient in right.items():
        value = out.get(monomial, EJet()) + scale*coefficient
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
            coefficient = (
                out.get(monomial, EJet())
                + left_coefficient*right_coefficient
            )
            if coefficient:
                out[monomial] = coefficient
            else:
                out.pop(monomial, None)
    return out


def source_polynomial(row, rhs):
    out = {(): -EJet.coerce(rhs)} if rhs else {}
    for variable, coefficient in row.items():
        coefficient = EJet.coerce(coefficient)
        if coefficient:
            out[(variable,)] = coefficient
    return out


def split_column(polynomial, exponent=None):
    if exponent is None:
        return clean({
            monomial: EJet.coerce(coefficient).value
            for monomial, coefficient in polynomial.items()
            if EJet.coerce(coefficient).value
        })
    return clean({
        monomial: EJet.coerce(coefficient).derivatives.get(exponent, E3())
        for monomial, coefficient in polynomial.items()
        if EJet.coerce(coefficient).derivatives.get(exponent, E3())
    })


def scalar(value):
    return E3(tri.FIELD.scalar(Rat3.coerce(value)))


def from_vector(vector):
    return E3(tri.FIELD.from_coordinates(vector))


ZERO_VECTOR = tuple(Rat3() for _ in range(18))
ONE_VECTOR = r.t.source_vector(("g", "X", 0, 1))
assert len(ONE_VECTOR) == 18 and from_vector(ONE_VECTOR) == E3(1)


def vector_scale(vector, coefficient):
    return tuple(coefficient*coordinate for coordinate in vector)


def vector_subtract(left, right):
    return tuple(a-b for a, b in zip(left, right))


def source_vector_jet(key):
    base = r.t.source_vector(key)
    derivatives = {}
    if len(key) == 4 and key[:3] == ("g", "X", 0):
        exponent = key[3]
        if exponent in Q_EXPONENTS:
            derivatives[exponent] = ONE_VECTOR
    return base, derivatives


def propagate_jet(rows, records):
    pivot_rhs, compatibility = {}, []
    for source_row, record in zip(rows, records):
        source_key, _, _ = source_row
        key, kind, pivot, lead, factors = record
        assert source_key == key
        base, derivatives = source_vector_jet(key)
        derivatives = dict(derivatives)
        for old, factor in factors:
            old_base, old_derivatives = pivot_rhs[old]
            base = vector_subtract(base, vector_scale(old_base, factor))
            for exponent, old_derivative in old_derivatives.items():
                derivative = vector_subtract(
                    derivatives.get(exponent, ZERO_VECTOR),
                    vector_scale(old_derivative, factor),
                )
                if any(derivative):
                    derivatives[exponent] = derivative
                else:
                    derivatives.pop(exponent, None)
        if kind == "pivot":
            inverse = lead.inverse()
            pivot_rhs[pivot] = (
                vector_scale(base, inverse),
                {
                    exponent: vector_scale(derivative, inverse)
                    for exponent, derivative in derivatives.items()
                },
            )
        elif any(base) or any(any(value) for value in derivatives.values()):
            compatibility.append((key, base, derivatives))
    return pivot_rhs, compatibility


def restrict_row_jet(original_row, pivots, pivot_rhs, free_parameter):
    row = {
        variable: Rat3.coerce(coefficient)
        for variable, coefficient in original_row.items() if coefficient
    }
    base = ZERO_VECTOR
    derivatives = {}
    for pivot in sorted(pivots):
        factor = row.pop(pivot, None)
        if factor is None or not factor:
            continue
        rhs_base, rhs_derivatives = pivot_rhs[pivot]
        base = tuple(a + factor*b for a, b in zip(base, rhs_base))
        for exponent, rhs_derivative in rhs_derivatives.items():
            derivative = tuple(
                a + factor*b
                for a, b in zip(
                    derivatives.get(exponent, ZERO_VECTOR), rhs_derivative
                )
            )
            if any(derivative):
                derivatives[exponent] = derivative
            else:
                derivatives.pop(exponent, None)
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
        EJet(from_vector(base), {
            exponent: from_vector(derivative)
            for exponent, derivative in derivatives.items()
        }),
        {
            free_parameter[variable]: EJet(scalar(coefficient))
            for variable, coefficient in row.items()
        },
    )


def configure_qd_jet(omit_direct=()):
    omit_direct = set(omit_direct)
    qd.Dual = EJet
    qd.B = EJet.direction(2)
    qd.S = EJet(E3(qd.uniform.S_FIELD))
    qd.D = EJet(E3(qd.uniform.D_FIELD))
    qd.L = EJet(E3(qd.uniform.L_FIELD))
    qd.A = EJet(E3(qd.uniform.A_FIELD))
    qd.Q_PRIME = {0: EJet(1), 24: EJet(25)}
    for exponent in Q_EXPONENTS:
        if exponent not in omit_direct:
            qd.Q_PRIME[exponent - 1] = EJet.direction(exponent, exponent)
    qd.R = qd.multiply(
        qd.multiply([EJet(-1), EJet(1)], [EJet(-1), EJet(1)]),
        [qd.D, -qd.S, EJet(1)],
    )
    qd.R3, qd.R5 = qd.power(qd.R, 3), qd.power(qd.R, 5)
    qd.POLE_F = {1: -(qd.L**3)*qd.A, 6: qd.L**3}
    qd.POLE_G = {
        0: EJet(r.b.Q(5, 9))*qd.L**5*qd.A**2,
        5: EJet(r.b.Q(-5, 3))*qd.L**5*qd.A,
        10: qd.L**5,
    }


def solve_cert_jet(rows):
    pivots, factors, dependent = {}, [], []
    source = [
        (
            key,
            {variable: EJet.coerce(value) for variable, value in row.items()},
            EJet.coerce(rhs),
        )
        for key, row, rhs in rows
    ]
    for row_index, (key, original_row, original_rhs) in enumerate(source):
        row, rhs = dict(original_row), original_rhs
        combination = {row_index: EJet(1)}
        while True:
            pivot = next(
                (variable for variable in pivots
                 if variable in row and row[variable]),
                None,
            )
            if pivot is None:
                break
            factor = row[pivot]
            old_row, old_rhs, old_combination = pivots[pivot]
            for variable, coefficient in old_row.items():
                value = row.get(variable, EJet()) - factor*coefficient
                if value:
                    row[variable] = value
                else:
                    row.pop(variable, None)
            rhs -= factor*old_rhs
            for old_index, coefficient in old_combination.items():
                value = combination.get(old_index, EJet()) - factor*coefficient
                if value:
                    combination[old_index] = value
                else:
                    combination.pop(old_index, None)

        base_variables = [
            variable for variable, coefficient in row.items()
            if coefficient.value
        ]
        if not base_variables:
            replay = {}
            for source_index, coefficient in combination.items():
                _, source_row, source_rhs = source[source_index]
                replay = add(
                    replay, source_polynomial(source_row, source_rhs), coefficient
                )
            assert clean(replay) == clean(source_polynomial(row, rhs))
            dependent.append((row_index, key, row, rhs, combination))
            continue

        pivot = min(base_variables)
        lead = row[pivot]
        inverse = lead.inverse()
        pivots[pivot] = (
            {variable: coefficient*inverse
             for variable, coefficient in row.items()},
            rhs*inverse,
            {index: coefficient*inverse
             for index, coefficient in combination.items()},
        )
        factors.append((row_index, key, pivot, lead))

    for pivot, (row, rhs, combination) in pivots.items():
        replay = {}
        for source_index, coefficient in combination.items():
            _, source_row, source_rhs = source[source_index]
            replay = add(
                replay, source_polynomial(source_row, source_rhs), coefficient
            )
        assert clean(replay) == clean(source_polynomial(row, rhs)), pivot
    return pivots, factors, dependent


def add_affine(left, right, scale=1):
    scale = EJet.coerce(scale)
    constant = left[0] + scale*right[0]
    row = dict(left[1])
    for variable, coefficient in right[1].items():
        value = row.get(variable, EJet()) + scale*coefficient
        if value:
            row[variable] = value
        else:
            row.pop(variable, None)
    return constant, row


def parameterize(nvariables, rows, stage):
    pivots, factors, dependent = solve_cert_jet(rows)
    free = [variable for variable in range(nvariables) if variable not in pivots]
    parameter_of = {variable: index for index, variable in enumerate(free)}
    forms = [None] * nvariables
    for variable in range(nvariables - 1, -1, -1):
        if variable in parameter_of:
            forms[variable] = (
                EJet(), {parameter_of[variable]: EJet(1)}
            )
            continue
        row, rhs, _ = pivots[variable]
        form = (rhs, {})
        for other, coefficient in row.items():
            if other == variable:
                continue
            assert other > variable and forms[other] is not None
            form = add_affine(form, forms[other], -coefficient)
        forms[variable] = form
    for key, row, rhs in rows:
        got = (EJet(), {})
        for variable, coefficient in row.items():
            got = add_affine(got, forms[variable], coefficient)
        source = source_polynomial(got[1], rhs-got[0])
        # Dependent derivative rows may obstruct a full-family
        # parameterization.  The pivot rows must replay regardless.
        if clean(source):
            assert any(record[1] == key for record in dependent)
    print(f"{stage}_rank={len(pivots)}/{nvariables}")
    print(f"{stage}_dependent_count={len(dependent)}")
    print(f"{stage}_pivot_source_replay=true", flush=True)
    return pivots, forms, free, factors, dependent


def compose_forms(forms, parameterization):
    out = []
    for constant, row in forms:
        result = (constant, {})
        for variable, coefficient in row.items():
            result = add_affine(result, parameterization[variable], coefficient)
        out.append(result)
    return out


def divide_jet(polynomial, pivots):
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


def lift_relations(quotients, pivots, nrows):
    relations = [{} for _ in range(nrows)]
    for pivot, quotient in quotients.items():
        _, _, combination = pivots[pivot]
        for row_index, coefficient in combination.items():
            relations[row_index] = add(
                relations[row_index], quotient, coefficient
            )
    return relations


def exact_source_replay(polynomial, remainder, relations, rows):
    replay = {}
    for relation, (_, row, rhs) in zip(relations, rows):
        replay = add(
            replay, multiply(relation, source_polynomial(row, rhs))
        )
    target = add(polynomial, remainder, -1)
    assert clean(replay) == clean(target)
    assert clean(replay) != clean(add(target, {(): EJet(1)}))
    nonzero = next(
        (index for index, relation in enumerate(relations) if clean(relation)),
        None,
    )
    assert nonzero is not None
    omitted = {}
    for index, (relation, (_, row, rhs)) in enumerate(zip(relations, rows)):
        if index != nonzero:
            omitted = add(
                omitted, multiply(relation, source_polynomial(row, rhs))
            )
    assert clean(omitted) != clean(target)


def e3_digest(value):
    return r.scalar_digest(E3.coerce(value))


def e3_exact(value):
    return repr(r.scalar_exact(E3.coerce(value)))


def polynomial_digest(polynomial):
    return r.polynomial_digest({
        monomial: E3.coerce(value)
        for monomial, value in polynomial.items()
    })


def column_digest_rows(rows, exponent):
    lines = []
    for key, row, rhs in rows:
        for variable, coefficient in sorted(row.items()):
            value = EJet.coerce(coefficient).derivatives.get(exponent, E3())
            if value:
                lines.append(f"{key!r}\t{variable}\t{e3_digest(value)}")
        value = EJet.coerce(rhs).derivatives.get(exponent, E3())
        if value:
            lines.append(f"{key!r}\trhs\t{e3_digest(value)}")
    return sha256(("\n".join(lines) + "\n").encode()).hexdigest(), len(lines)


def factors_only_allowed(polynomial):
    if not polynomial or polynomial.total_degree() == 0:
        return True
    _, factors = polynomial.factor()
    return all(factor in (U, H, B3) for factor, _ in factors)


def derivative_values(objects, exponent):
    for value in objects:
        value = EJet.coerce(value).derivatives.get(exponent, E3())
        if value:
            yield value


def all_values(polynomials):
    for polynomial in polynomials:
        yield from polynomial.values()


def denominator_for(values):
    values = list(values)
    return v77.denominator_lcm(values) if values else tri.CTX(1)


def build_transport_and_sections():
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
    for exponent in Q_EXPONENTS:
        matching = [
            row for row in ordered
            if row[0] == ('g', 'X', 0, exponent)
        ]
        assert len(matching) == 1
    transport_pivots, records, events, _ = tri.factor_transport(ordered)
    pivot_rhs, compatibility = propagate_jet(ordered, records)
    assert not compatibility and len(transport_pivots) == 3470
    free = [
        variable for variable in range(nf + ng)
        if variable not in transport_pivots
    ]
    assert len(free) == 132
    free_parameter = {variable: index for index, variable in enumerate(free)}

    def restrict(row):
        return restrict_row_jet(
            row, transport_pivots, pivot_rhs, free_parameter
        )

    bands = {}
    for owner, imax, jmax, offset in (
        ('f', 15, 60, 0), ('g', 25, 100, nf)
    ):
        for power in (1, 2, 3):
            forms = []
            for degree in range(16 if owner == 'f' else 26):
                row = {
                    offset + variable: coefficient
                    for variable, coefficient in r.fb.x_chart_coefficient(
                        imax, jmax, power, degree
                    ).items()
                }
                forms.append(restrict(row))
            bands[(owner, power)] = forms

    pole_f = []
    for degree in range(61):
        pole_f.append(restrict({
            variable: Rat3.coerce(coefficient)
            for variable, coefficient in nr.pole_coefficient(
                15, 60, -2, degree
            ).items()
        }))
    pole_g = []
    for degree in range(101):
        pole_g.append(restrict({
            nf + variable: Rat3.coerce(coefficient)
            for variable, coefficient in nr.pole_coefficient(
                25, 100, -4, degree
            ).items()
        }))

    active = sorted({
        exponent
        for base, derivatives in pivot_rhs.values()
        for exponent in derivatives
    })
    assert active == list(Q_EXPONENTS)
    print(f"transport_rank={len(transport_pivots)}/{nf+ng}")
    print(f"transport_event_count={len(events)}")
    print(f"transport_active_q_columns={','.join(map(str, active))}")
    print("transport_all_q_source_keys_exact_and_singleton=true")
    print("transport_matrix_all_q_derivative_zero=true")
    print("transport_rhs_all_q_derivatives_retained=true", flush=True)
    return bands, pole_f, pole_g


def first_rows_and_controls(bands):
    configure_qd_jet()
    first_rows = qd.pack(
        'X-2', qd.first_band_polynomials(
            bands[('f', 1)], bands[('g', 1)]
        )
    )
    configure_qd_jet(omit_direct=Q_EXPONENTS)
    omitted = qd.pack(
        'X-2', qd.first_band_polynomials(
            bands[('f', 1)], bands[('g', 1)]
        )
    )
    configure_qd_jet()
    changed = []
    for exponent in Q_EXPONENTS:
        positive_digest, positive_count = column_digest_rows(first_rows, exponent)
        omitted_digest, omitted_count = column_digest_rows(omitted, exponent)
        assert positive_digest != omitted_digest
        changed.append(exponent)
        print(
            f"first_q{exponent}_column={positive_count};"
            f"omit={omitted_count};sha={positive_digest};"
            f"omit_sha={omitted_digest}"
        )
    assert tuple(changed) == Q_EXPONENTS
    print("all_q_direct_qprime_batched_omission_control=true", flush=True)
    return first_rows


def dependent_obstruction_coordinates(dependent):
    coordinates = {}
    for compatibility_index, (_, key, row, rhs, _) in enumerate(dependent):
        for variable, coefficient in row.items():
            coefficient = EJet.coerce(coefficient)
            for exponent, value in coefficient.derivatives.items():
                coordinates.setdefault(
                    (compatibility_index, repr(key), f"x{variable}"), {}
                )[exponent] = value
        for exponent, value in EJet.coerce(rhs).derivatives.items():
            coordinates.setdefault(
                (compatibility_index, repr(key), "constant"), {}
            )[exponent] = -value
    return {key: value for key, value in coordinates.items() if value}


def matrix_rref(matrix):
    matrix = [list(row) for row in matrix]
    nrows = len(matrix)
    ncols = len(matrix[0]) if matrix else len(Q_EXPONENTS)
    pivot_columns = []
    row_index = 0
    for column in range(ncols):
        pivot = next(
            (index for index in range(row_index, nrows) if matrix[index][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[row_index], matrix[pivot] = matrix[pivot], matrix[row_index]
        inverse = matrix[row_index][column].inverse()
        matrix[row_index] = [value*inverse for value in matrix[row_index]]
        for index in range(nrows):
            if index == row_index or not matrix[index][column]:
                continue
            factor = matrix[index][column]
            matrix[index] = [
                left - factor*right
                for left, right in zip(matrix[index], matrix[row_index])
            ]
        pivot_columns.append(column)
        row_index += 1
        if row_index == nrows:
            break
    return matrix, pivot_columns


def conormal_table(dependent, outdir, label):
    coordinates = dependent_obstruction_coordinates(dependent)
    ordered = sorted(coordinates)
    matrix = [
        [coordinates[key].get(exponent, E3()) for exponent in Q_EXPONENTS]
        for key in ordered
    ]
    reduced, pivots = matrix_rref(matrix)
    free = [index for index in range(len(Q_EXPONENTS)) if index not in pivots]
    kernel = []
    for free_index in free:
        vector = [E3() for _ in Q_EXPONENTS]
        vector[free_index] = E3(1)
        for row_index, pivot_column in enumerate(pivots):
            vector[pivot_column] = -reduced[row_index][free_index]
        kernel.append(vector)
    for row in matrix:
        assert len(row) == len(Q_EXPONENTS)
    for vector in kernel:
        assert all(
            not sum((coefficient*entry for coefficient, entry in zip(row, vector)), E3())
            for row in matrix
        )
    denominator = denominator_for(
        [
            coefficient
            for values in coordinates.values()
            for coefficient in values.values()
        ]
        + [coefficient for vector in kernel for coefficient in vector]
    )
    assert factors_only_allowed(denominator)

    entries = []
    for key in ordered:
        compatibility, source_key, coordinate = key
        for exponent in Q_EXPONENTS:
            coefficient = coordinates[key].get(exponent, E3())
            if coefficient:
                entries.append(
                    (
                        compatibility, source_key, coordinate, exponent,
                        e3_digest(coefficient), e3_exact(coefficient),
                    )
                )
    entries.sort(key=lambda item: (item[0], item[1], item[2], item[3]))
    permuted_entries = []
    for key in reversed(ordered):
        compatibility, source_key, coordinate = key
        for exponent in reversed(Q_EXPONENTS):
            coefficient = coordinates[key].get(exponent, E3())
            if coefficient:
                permuted_entries.append(
                    (
                        compatibility, source_key, coordinate, exponent,
                        e3_digest(coefficient), e3_exact(coefficient),
                    )
                )
    permuted_entries.sort(key=lambda item: (item[0], item[1], item[2], item[3]))
    assert permuted_entries == entries
    lines = [
        "compatibility\tkey\tcoordinate\texponent\t"
        "coefficient_sha256\tcoefficient_exact"
    ]
    lines.extend("\t".join(map(str, entry)) for entry in entries)
    text = "\n".join(lines) + "\n"
    path = outdir / f"{label}_CONORMAL.tsv"
    path.write_text(text)
    kernel_lines = []
    for vector_index, vector in enumerate(kernel):
        for exponent, value in zip(Q_EXPONENTS, vector):
            if value:
                kernel_lines.append(
                    f"{vector_index}\t{exponent}\t{e3_digest(value)}\t"
                    f"{e3_exact(value)}"
                )
    kernel_text = "\n".join(kernel_lines) + ("\n" if kernel_lines else "")
    kernel_path = outdir / f"{label}_KERNEL.exact.tsv"
    kernel_path.write_text(kernel_text)
    print(f"{label}_conormal_coordinate_count={len(ordered)}")
    print(f"{label}_conormal_rank={len(pivots)}/{len(Q_EXPONENTS)}")
    print(f"{label}_conormal_kernel_dimension={len(kernel)}")
    print(f"{label}_denominator_factor={denominator.factor()}")
    print(f"{label}_denominator_radical_subset_U_H_B3=true")
    print(f"{label}_conormal_path={path}")
    print(f"{label}_conormal_sha256={sha256(text.encode()).hexdigest()}")
    print(f"{label}_kernel_path={kernel_path}")
    print(f"{label}_kernel_sha256={sha256(kernel_text.encode()).hexdigest()}")
    print(f"{label}_column_permutation_canonicalization=true")
    return len(pivots), kernel


def run_p12(bands, first_rows, first_pivots, first_factors, outdir):
    first_minor = EJet(1)
    for _, _, _, lead in first_factors:
        first_minor *= lead
    assert e3_digest(first_minor.derivatives[2]) == (
        "c0730fa1f8764164b2ac0a74523849b49f4362d41bc81845d086d6373fdb65c1"
    )
    assert e3_digest(first_minor.derivatives[3]) == (
        "c0730fa1f8764164b2ac0a74523849b49f4362d41bc81845d086d6373fdb65c1"
    )
    print("first_minor_q2_projection_matches_V32=true")
    print("first_minor_q3_projection_matches_V77=true", flush=True)

    raw = qd.compile_current(
        *[bands[('f', power)] for power in (1, 2, 3)],
        *[bands[('g', power)] for power in (1, 2, 3)],
    )[12]
    polynomial = {
        monomial: EJet.coerce(coefficient)
        for monomial, coefficient in raw.items() if coefficient
    }
    raw_base = split_column(polynomial)
    assert len(raw_base) == 2893
    assert polynomial_digest(raw_base) == (
        "8d5c3550fbad393c1e13061d9934ed79e29261db378f1d344c4ea5e587e704da"
    )
    print("genuine_P12_source_compiler=true")
    print(f"raw_base_terms={len(raw_base)}")
    print(f"raw_base_sha256={polynomial_digest(raw_base)}", flush=True)

    remainder, quotients = divide_jet(polynomial, first_pivots)
    relations = lift_relations(quotients, first_pivots, len(first_rows))
    exact_source_replay(polynomial, remainder, relations, first_rows)
    remainder_base = split_column(remainder)
    S = E3(qd.uniform.S_FIELD)
    k = E3(252) - 342*S + 144*S**2 - 36*S**3
    assert remainder_base == {(): -k/50}
    assert polynomial_digest(remainder_base) == (
        "93121eef14c472c3c55b7acaeb1d0eff73b77d462ad8d5b197e8e21b9cda89c4"
    )
    print("P12_base_remainder_is_minus_k_over_50=true")
    print("P12_all_q_dual_remainder_is_unit_automatic=true", flush=True)
    print("P12_source_row_omission_negative_control=true", flush=True)

    relation_values = list(all_values(relations))
    first_values = [
        coefficient
        for _, row, rhs in first_rows
        for coefficient in list(row.values()) + [rhs]
    ]
    lines = [
        "exponent\traw_terms\traw_sha256\tremainder_terms\t"
        "remainder_sha256\tlambda_prime_rows\tdenominator_factor"
    ]
    lambda_prime_directions = []
    for exponent in Q_EXPONENTS:
        raw_column = split_column(polynomial, exponent)
        remainder_column = split_column(remainder, exponent)
        if exponent == 2:
            assert polynomial_digest(raw_column) == (
                "816da33cd8e77b035740b7811e56d9ac8742160974a690506dec35d9b002d6a0"
            )
            assert polynomial_digest(remainder_column) == (
                "1acfd5c0169b466d16c6d87de34b3ec0f5b78f6bb073a6191e9bed2ac36775b3"
            )
        if exponent == 3:
            assert polynomial_digest(raw_column) == (
                "70d253cd30303d5ae6ebf81e8de0b2c12a00b66b060c996f0a898dbaf708682c"
            )
            assert polynomial_digest(remainder_column) == (
                "3dd07bb5e097ea920104e085d857e519915ba214145d862576bd9cb9d3792458"
            )

        source_identity = {}
        lambda_zero_bprime = {}
        lambda_prime_bzero = {}
        lambda_prime_rows = 0
        for relation, (_, row, rhs) in zip(relations, first_rows):
            source = source_polynomial(row, rhs)
            relation_base = split_column(relation)
            relation_column = split_column(relation, exponent)
            source_base = split_column(source)
            source_column = split_column(source, exponent)
            if relation_column:
                lambda_prime_rows += 1
            lambda_zero_bprime = r.add(
                lambda_zero_bprime, r.multiply(relation_base, source_column)
            )
            lambda_prime_bzero = r.add(
                lambda_prime_bzero, r.multiply(relation_column, source_base)
            )
            source_identity = r.add(
                source_identity,
                r.add(
                    r.multiply(relation_base, source_column),
                    r.multiply(relation_column, source_base),
                ),
            )
        target = r.add(raw_column, remainder_column, E3(-1))
        assert r.clean(source_identity) == r.clean(target)
        if lambda_prime_bzero:
            lambda_prime_directions.append(exponent)
            assert r.clean(lambda_zero_bprime) != r.clean(target)

        denominator = denominator_for(
            list(derivative_values(relation_values, exponent))
            + list(derivative_values(first_values, exponent))
            + list(raw_column.values())
            + list(remainder_column.values())
        )
        assert factors_only_allowed(denominator)
        lines.append(
            f"{exponent}\t{len(raw_column)}\t{polynomial_digest(raw_column)}\t"
            f"{len(remainder_column)}\t{polynomial_digest(remainder_column)}\t"
            f"{lambda_prime_rows}\t{denominator.factor()}"
        )
        print(
            f"q{exponent}_raw_terms={len(raw_column)};"
            f"remainder_terms={len(remainder_column)};"
            f"lambda_prime_rows={lambda_prime_rows}"
        )
    assert lambda_prime_directions
    table = "\n".join(lines) + "\n"
    path = outdir / "ALL_Q_P12_COLUMNS.tsv"
    path.write_text(table)
    print(f"all_q_P12_table_path={path}")
    print(f"all_q_P12_table_sha256={sha256(table.encode()).hexdigest()}")
    print(
        "lambda_prime_active_directions="
        + ",".join(map(str, lambda_prime_directions))
    )
    print("lambda_prime_aggregate_omission_negative_control=true")
    print("all_q_derivative_source_identities_exact=true")
    print("q2_projection_matches_V32=true")
    print("q3_projection_matches_V77=true")
    print("all_q_denominator_radicals_subset_U_H_B3=true")
    print("TD6-A3-ALL-Q-VECTOR-AD-P12 PASS")


def run_staged(bands, pole_f, pole_g, first_rows, first_forms, outdir):
    bands94 = {
        key: compose_forms(forms, first_forms)
        for key, forms in bands.items()
    }
    pole_f94 = compose_forms(pole_f, first_forms)
    pole_g94 = compose_forms(pole_g, first_forms)
    previous_rows = qd.pack(
        'X-1', qd.compile_previous(
            bands94[('f', 1)], bands94[('f', 2)],
            bands94[('g', 1)], bands94[('g', 2)],
        )
    )
    previous_rows += qd.pack(
        'P1', qd.compile_pole_previous(pole_f94, pole_g94)
    )
    previous_pivots, previous_forms, free56, _, previous_dependent = (
        parameterize(94, previous_rows, "previous_pole_all_q")
    )
    assert len(previous_pivots) == 38 and len(free56) == 56
    previous_coordinates = dependent_obstruction_coordinates(previous_dependent)
    conormal_table(previous_dependent, outdir, "PREVIOUS_POLE")
    if previous_coordinates:
        print("previous_pole_all_q_full_family_parameterization=false")
        print("current_stage_skipped_due_previous_obstruction=true")
        print("TD6-A3-ALL-Q-VECTOR-AD-STAGED EARLY-OBSTRUCTION PASS")
        return
    print("previous_pole_all_q_full_family_parameterization=true", flush=True)

    bands56 = {
        key: compose_forms(forms, previous_forms)
        for key, forms in bands94.items()
    }
    current_rows = qd.pack(
        'X0', qd.compile_current(
            *[bands56[('f', power)] for power in (1, 2, 3)],
            *[bands56[('g', power)] for power in (1, 2, 3)],
        )
    )
    current_pivots, _, current_dependent = solve_cert_jet(current_rows)
    assert len(current_pivots) == 25
    base_inconsistent = [
        (index, key, rhs.value)
        for index, key, _, rhs, _ in current_dependent if rhs.value
    ]
    assert base_inconsistent
    p12 = [
        record for record in current_dependent if record[1] == ('X0', 12)
    ]
    assert len(p12) == 1 and p12[0][3].value
    rank, kernel = conormal_table(current_dependent, outdir, "CURRENT")
    print(f"current_rank={len(current_pivots)}/56")
    print(f"current_dependent_count={len(current_dependent)}")
    print(f"current_base_inconsistent_count={len(base_inconsistent)}")
    print("current_P12_base_unit_present=true")
    print("current_staged_source_row_replays_exact=true")
    print("conormal_at_empty_base_is_scheduling_only=true")
    print("all_q_tangent_family_killed=false")
    print("all_q_polynomial_family_killed=false")
    print("whole_TD6_killed=false")
    print("SP2_killed=false")
    print("JC2_resolved=false")
    print("TD6-A3-ALL-Q-VECTOR-AD-STAGED PASS")


def main():
    assert len(sys.argv) == 2 and sys.argv[1] in ("p12", "staged")
    mode = sys.argv[1]
    outdir = Path(os.environ.get("TD6_OUTPUT_DIR", ".")).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    print("producer=TD6-A3-ALL-Q-VECTOR-AD-V78")
    print(f"mode={mode}")
    print("q_exponents=" + ",".join(map(str, Q_EXPONENTS)))
    print("q15_lower_target_shear_gauge_excluded=true")
    print("base_q2_beta=0")
    print("source_center=(C,V,U)")
    print("source_p_boundary=t^15_fixed")
    print("source_dead_stretch=0_fixed")
    print("source_F1_orbit_and_pole=frozen")
    print("scope_open=D(U*(C-3U^2)*B3)")
    print("dual_base_ideal_already_unit=true")
    print("result_use=tangent_conormal_and_source_support_discriminator_only")
    print(f"V77_parent_sha256={V77_SHA256}", flush=True)

    bands, pole_f, pole_g = build_transport_and_sections()
    first_rows = first_rows_and_controls(bands)
    first_pivots, first_forms, free94, first_factors, first_dependent = (
        parameterize(132, first_rows, "first_all_q")
    )
    assert len(first_pivots) == 38 and len(free94) == 94
    first_coordinates = dependent_obstruction_coordinates(first_dependent)
    conormal_table(first_dependent, outdir, "FIRST")
    assert not first_coordinates
    print("first_all_q_full_family_parameterization=true", flush=True)

    if mode == "p12":
        run_p12(
            bands, first_rows, first_pivots, first_factors, outdir
        )
    else:
        run_staged(
            bands, pole_f, pole_g, first_rows, first_forms, outdir
        )


if __name__ == "__main__":
    main()
