#!/usr/bin/env python3
"""Exact previous-row X-1,11 source certificate on V=0,C=-5U^2,D(U).

The `b3half` parent mode is used only as a hash-pinned Q(U) coefficient-field
adapter.  The raw center is rebuilt here as (-5 U^2, 0, U).  This script adds
an honest polynomial beta,
retains both q and q-prime source entry points, detects the exact dependent
previous row ``('X-1', 11)``, and reconstructs its unit obstruction through
the original previous/pole and first rows.

This is a function-field theorem only on D(U).  Every Q[U] numerator and
denominator factor used by the normalized certificate is emitted and charged.
No whole-B3 conclusion is inferred inside this producer.
"""

import builtins
from fractions import Fraction
from hashlib import sha256
import importlib.util
import os
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
CURVE_PATH = (
    HERE.parent / "td6_c1_c3_two_center_cover_20260824"
    / "c1_c2_c3_p3_quotient.py"
)
CURVE_SHA256 = "f8c46d2cec5f83f4e02b13272cdc4a761c6dcbc939a343e03f32f3517bab0505"
assert sha256(CURVE_PATH.read_bytes()).hexdigest() == CURVE_SHA256
spec = importlib.util.spec_from_file_location("td6_q2_n13_curve_source", CURVE_PATH)
p = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = p
spec.loader.exec_module(p)

assert p.COMPONENT == "b3half"
OMIT_DIRECT_QPRIME = "--omit-direct-qprime" in sys.argv
assert all(
    argument == "--omit-direct-qprime" or argument.startswith("--component=")
    for argument in sys.argv[1:]
)

r, qd, nr = p.r, p.r.qd, p.r.qd.nr
Curve, ECurve = p.Curve, p.ECurve


class BetaPoly:
    """Dense univariate ECurve[beta], with only constant pivots invertible."""

    __slots__ = ("coefficients",)

    def __init__(self, value=0):
        if isinstance(value, BetaPoly):
            self.coefficients = value.coefficients
            return
        if isinstance(value, (list, tuple)):
            coefficients = [ECurve.coerce(entry) for entry in value]
        else:
            coefficients = [ECurve.coerce(value)]
        while coefficients and not coefficients[-1]:
            coefficients.pop()
        self.coefficients = tuple(coefficients)

    @staticmethod
    def coerce(value):
        return value if isinstance(value, BetaPoly) else BetaPoly(value)

    @staticmethod
    def beta():
        return BetaPoly([0, 1])

    @property
    def degree(self):
        return len(self.coefficients) - 1

    @property
    def constant(self):
        return self.coefficients[0] if self.coefficients else ECurve()

    @property
    def leading(self):
        return self.coefficients[-1] if self.coefficients else ECurve()

    def coefficient(self, degree):
        return (
            self.coefficients[degree]
            if 0 <= degree < len(self.coefficients)
            else ECurve()
        )

    def __bool__(self):
        return bool(self.coefficients)

    def __add__(self, other):
        other = BetaPoly.coerce(other)
        size = max(len(self.coefficients), len(other.coefficients))
        return BetaPoly([
            self.coefficient(index) + other.coefficient(index)
            for index in range(size)
        ])

    __radd__ = __add__

    def __neg__(self):
        return BetaPoly([-coefficient for coefficient in self.coefficients])

    def __sub__(self, other):
        return self + (-BetaPoly.coerce(other))

    def __rsub__(self, other):
        return BetaPoly.coerce(other) - self

    def __mul__(self, other):
        other = BetaPoly.coerce(other)
        if not self or not other:
            return BetaPoly()
        coefficients = [ECurve()] * (
            len(self.coefficients) + len(other.coefficients) - 1
        )
        for left_degree, left in enumerate(self.coefficients):
            for right_degree, right in enumerate(other.coefficients):
                coefficients[left_degree + right_degree] += left*right
        return BetaPoly(coefficients)

    __rmul__ = __mul__

    def inverse(self):
        assert self.degree == 0, "beta-dependent nonunit pivot"
        return BetaPoly(self.constant.inverse())

    def __truediv__(self, other):
        return self * BetaPoly.coerce(other).inverse()

    def __rtruediv__(self, other):
        return BetaPoly.coerce(other) / self

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        result, base = BetaPoly(1), self
        while exponent:
            if exponent & 1:
                result *= base
            base *= base
            exponent //= 2
        return result

    def __eq__(self, other):
        return self.coefficients == BetaPoly.coerce(other).coefficients


def beta_exact(value):
    value = BetaPoly.coerce(value)
    return tuple(p.scalar_exact(coefficient) for coefficient in value.coefficients)


def beta_digest(value):
    return sha256(repr(beta_exact(value)).encode()).hexdigest()


def combination_digest(combination):
    exact = tuple(
        (index, beta_exact(weight))
        for index, weight in sorted(combination.items())
    )
    return sha256(repr(exact).encode()).hexdigest()


def vector_scale(vector, coefficient):
    coefficient = Curve.coerce(coefficient)
    return tuple(coefficient*entry for entry in vector)


def vector_subtract(left, right):
    return tuple(a-b for a, b in zip(left, right))


def from_vector(vector):
    return ECurve(p.FIELD.from_coordinates(tuple(vector)))


def propagate_beta(rows, records):
    zero = tuple(Curve() for _ in range(18))
    one = tuple(Curve.coerce(entry) for entry in r.t.source_vector(("g", "X", 0, 1)))
    assert len(one) == 18 and from_vector(one) == ECurve(1)
    pivot_rhs, compatibility = {}, []
    for source_row, record in zip(rows, records):
        source_key, _, _ = source_row
        key, kind, pivot, lead, factors = record
        assert source_key == key
        base = tuple(Curve.coerce(entry) for entry in r.t.source_vector(key))
        derivative = one if key == ("g", "X", 0, 2) else zero
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


def restrict_row_beta(original_row, pivots, pivot_rhs, free_parameter):
    row = {
        variable: Curve.coerce(coefficient)
        for variable, coefficient in original_row.items() if coefficient
    }
    zero = tuple(Curve() for _ in range(18))
    base, derivative = zero, zero
    for pivot in sorted(pivots):
        factor = row.pop(pivot, None)
        if factor is None or not factor:
            continue
        rhs_base, rhs_derivative = pivot_rhs[pivot]
        base = tuple(
            old + factor*entry for old, entry in zip(base, rhs_base)
        )
        derivative = tuple(
            old + factor*entry
            for old, entry in zip(derivative, rhs_derivative)
        )
        for variable, coefficient in pivots[pivot].items():
            if variable == pivot:
                continue
            value = row.get(variable, Curve()) - factor*coefficient
            if value:
                row[variable] = value
            else:
                row.pop(variable, None)
    assert all(variable in free_parameter for variable in row)
    return (
        BetaPoly([from_vector(base), from_vector(derivative)]),
        {
            free_parameter[variable]: BetaPoly(ECurve(coefficient))
            for variable, coefficient in row.items()
        },
    )


def configure_qd(direct_qprime=True):
    qd.Dual = BetaPoly
    qd.B = BetaPoly.beta()
    qd.S = BetaPoly(ECurve(qd.uniform.S_FIELD))
    qd.D = BetaPoly(ECurve(qd.uniform.D_FIELD))
    qd.L = BetaPoly(ECurve(qd.uniform.L_FIELD))
    qd.A = BetaPoly(ECurve(qd.uniform.A_FIELD))
    qd.Q_PRIME = {0: BetaPoly(1), 24: BetaPoly(25)}
    if direct_qprime:
        qd.Q_PRIME[1] = BetaPoly([0, 2])
    qd.R = qd.multiply(
        qd.multiply([BetaPoly(-1), BetaPoly(1)], [BetaPoly(-1), BetaPoly(1)]),
        [qd.D, -qd.S, BetaPoly(1)],
    )
    qd.R3, qd.R5 = qd.power(qd.R, 3), qd.power(qd.R, 5)
    qd.POLE_F = {1: -(qd.L**3)*qd.A, 6: qd.L**3}
    qd.POLE_G = {
        0: BetaPoly(r.b.Q(5, 9))*qd.L**5*qd.A**2,
        5: BetaPoly(r.b.Q(-5, 3))*qd.L**5*qd.A,
        10: qd.L**5,
    }


def add_to_row(row, variable, value):
    value = BetaPoly.coerce(value)
    total = row.get(variable, BetaPoly()) + value
    if total:
        row[variable] = total
    else:
        row.pop(variable, None)


def solve_stage(nvariables, rows, stage):
    """Unit-pivot GE over ECurve[beta], retaining exact source ancestry."""
    pivots, order, factors, dependent = {}, [], [], []
    source = [
        (
            key,
            {variable: BetaPoly.coerce(value) for variable, value in row.items()},
            BetaPoly.coerce(rhs),
        )
        for key, row, rhs in rows
    ]
    for row_index, (key, original_row, original_rhs) in enumerate(source):
        row, rhs = dict(original_row), original_rhs
        combination = {row_index: BetaPoly(1)}
        while True:
            reducible = sorted(variable for variable in row if variable in pivots)
            if not reducible:
                break
            pivot = reducible[0]
            factor = row[pivot]
            old_row, old_rhs, old_combination = pivots[pivot]
            for variable, coefficient in old_row.items():
                add_to_row(row, variable, -factor*coefficient)
            rhs -= factor*old_rhs
            for old_index, coefficient in old_combination.items():
                value = combination.get(old_index, BetaPoly()) - factor*coefficient
                if value:
                    combination[old_index] = value
                else:
                    combination.pop(old_index, None)
        if not row:
            replay_row, replay_rhs = {}, BetaPoly()
            for source_index, weight in combination.items():
                _, source_row, source_rhs = source[source_index]
                for variable, coefficient in source_row.items():
                    add_to_row(replay_row, variable, weight*coefficient)
                replay_rhs += weight*source_rhs
            assert not replay_row and replay_rhs == rhs
            dependent.append((row_index, key, rhs, combination))
            continue
        pivot = min(row)
        lead = row[pivot]
        if lead.degree != 0:
            print(f"{stage}_nonunit_pivot_row={row_index}")
            print(f"{stage}_nonunit_pivot_key={key}")
            print(f"{stage}_nonunit_pivot_variable={pivot}")
            print(f"{stage}_nonunit_pivot_degree={lead.degree}", flush=True)
            raise AssertionError("beta-dependent pivot")
        inverse = lead.inverse()
        normalized_row = {
            variable: coefficient*inverse for variable, coefficient in row.items()
        }
        normalized_rhs = rhs*inverse
        normalized_combination = {
            index: coefficient*inverse for index, coefficient in combination.items()
        }
        pivots[pivot] = (
            normalized_row, normalized_rhs, normalized_combination
        )
        order.append(pivot)
        factors.append((row_index, key, pivot, lead))
    factor_exact = tuple(
        (row_index, key, pivot, beta_exact(lead))
        for row_index, key, pivot, lead in factors
    )
    print(f"{stage}_rank={len(pivots)}/{nvariables}")
    print(f"{stage}_dependent_count={len(dependent)}")
    print(f"{stage}_pivot_digest={sha256(repr(factor_exact).encode()).hexdigest()}")
    print(f"{stage}_original_row_replay=true", flush=True)
    return pivots, order, factors, dependent


def parameterize(nvariables, rows, stage):
    pivots, _, factors, dependent = solve_stage(nvariables, rows, stage)
    bad = [record for record in dependent if record[2]]
    assert not bad, (stage, [(key, beta_digest(rhs)) for _, key, rhs, _ in bad])
    free = [variable for variable in range(nvariables) if variable not in pivots]
    parameter_of = {variable: index for index, variable in enumerate(free)}
    forms = [None] * nvariables
    for variable in range(nvariables - 1, -1, -1):
        if variable in parameter_of:
            forms[variable] = (
                BetaPoly(), {parameter_of[variable]: BetaPoly(1)}
            )
            continue
        row, rhs, _ = pivots[variable]
        form = (rhs, {})
        for other, coefficient in row.items():
            if other == variable:
                continue
            assert other > variable and forms[other] is not None
            form = nr.add_affine(form, forms[other], -coefficient)
        forms[variable] = form
    for _, row, rhs in rows:
        got = (BetaPoly(), {})
        for variable, coefficient in row.items():
            got = nr.add_affine(got, forms[variable], coefficient)
        assert got == (BetaPoly.coerce(rhs), {})
    print(f"{stage}_affine_parameterization_replay=true", flush=True)
    return pivots, forms, free, factors


def compose(forms, parameter_forms):
    result = []
    for constant, coefficients in forms:
        value = (constant, {})
        for parameter, coefficient in coefficients.items():
            value = nr.add_affine(value, parameter_forms[parameter], coefficient)
        result.append(value)
    return result


def beta_denominator(values):
    return p.denominator_lcm(
        coefficient
        for value in values
        for coefficient in BetaPoly.coerce(value).coefficients
    )


def canonical(value):
    """Address-free serializer for proof-DAG objects."""
    if isinstance(value, ECurve):
        return ("ECurve", p.scalar_exact(value))
    if isinstance(value, BetaPoly):
        return (
            "BetaPoly",
            tuple(p.scalar_exact(coefficient) for coefficient in value.coefficients),
        )
    if isinstance(value, dict):
        return (
            "dict",
            tuple(
                (canonical(key), canonical(entry))
                for key, entry in sorted(value.items(), key=lambda item: repr(item[0]))
            ),
        )
    if isinstance(value, tuple):
        return ("tuple", tuple(canonical(entry) for entry in value))
    if isinstance(value, list):
        return ("list", tuple(canonical(entry) for entry in value))
    if isinstance(value, (str, int, bool, type(None))):
        return value
    raise TypeError((type(value), value))


def canonical_digest(value):
    return sha256(repr(canonical(value)).encode()).hexdigest()


def clean(polynomial):
    return {monomial: coefficient for monomial, coefficient in polynomial.items() if coefficient}


def poly_add(left, right, scale=1):
    scale = BetaPoly.coerce(scale)
    out = dict(left)
    for monomial, coefficient in right.items():
        value = out.get(monomial, BetaPoly()) + scale*BetaPoly.coerce(coefficient)
        if value:
            out[monomial] = value
        else:
            out.pop(monomial, None)
    return out


def poly_multiply(left, right):
    out = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial = tuple(sorted(left_monomial + right_monomial))
            value = (
                out.get(monomial, BetaPoly())
                + BetaPoly.coerce(left_coefficient)*BetaPoly.coerce(right_coefficient)
            )
            if value:
                out[monomial] = value
            else:
                out.pop(monomial, None)
    return out


def poly_scale(polynomial, scale):
    scale = BetaPoly.coerce(scale)
    return clean({monomial: scale*BetaPoly.coerce(value) for monomial, value in polynomial.items()})


def projection(polynomial, degree):
    return clean({
        monomial: BetaPoly.coerce(coefficient).coefficient(degree)
        for monomial, coefficient in polynomial.items()
        if BetaPoly.coerce(coefficient).coefficient(degree)
    })


def source_polynomial(row, rhs):
    out = {(variable,): BetaPoly.coerce(value) for variable, value in row.items() if value}
    if rhs:
        out[()] = -BetaPoly.coerce(rhs)
    return clean(out)


def row_polynomial(record):
    if len(record) == 2:
        return record[1]
    _, row, rhs = record
    return source_polynomial(row, rhs)


def source_records(family, polynomials):
    return [((family, degree), clean(polynomial)) for degree, polynomial in enumerate(polynomials)]


def total_degree(polynomial):
    return max((len(monomial) for monomial in polynomial), default=-1)


def remap_polynomial(polynomial, variable_map):
    out = {}
    for monomial, coefficient in polynomial.items():
        mapped = tuple(sorted(variable_map[variable] for variable in monomial))
        value = out.get(mapped, BetaPoly()) + BetaPoly.coerce(coefficient)
        if value:
            out[mapped] = value
        else:
            out.pop(mapped, None)
    return out


def divide_polynomial(polynomial, pivots):
    """Reduce by normalized affine pivots, batching equal-pivot targets.

    One exact quotient layer eliminates every current monomial containing
    the chosen pivot.  Since the normalized affine equation contains its
    pivot only in the singleton leading monomial, each layer lowers that
    pivot's exponent.  The final source replay proves equivalence.
    """
    remainder, quotients = dict(polynomial), {}
    normalized = {
        pivot: source_polynomial(row, rhs)
        for pivot, (row, rhs, _) in pivots.items()
    }
    for pivot in sorted(pivots):
        assert normalized[pivot].get((pivot,)) == BetaPoly(1)
        assert all(
            pivot not in monomial or monomial == (pivot,)
            for monomial in normalized[pivot]
        )
        quotient = {}
        while True:
            multiplier = {}
            for monomial, coefficient in tuple(remainder.items()):
                if not coefficient or pivot not in monomial:
                    continue
                reduced = list(monomial)
                reduced.remove(pivot)
                reduced = tuple(reduced)
                value = (
                    multiplier.get(reduced, BetaPoly())
                    + BetaPoly.coerce(coefficient)
                )
                if value:
                    multiplier[reduced] = value
                else:
                    multiplier.pop(reduced, None)
            if not multiplier:
                break
            quotient = poly_add(quotient, multiplier)
            remainder = poly_add(
                remainder, poly_multiply(multiplier, normalized[pivot]), -1
            )
        if quotient:
            quotients[pivot] = quotient
    replay = dict(remainder)
    for pivot, quotient in quotients.items():
        replay = poly_add(replay, poly_multiply(quotient, normalized[pivot]))
    assert clean(replay) == clean(polynomial)
    print("division_algorithm=batch_all_equal_pivot_targets_exact_replay", flush=True)
    return clean(remainder), quotients


def lift_relations(quotients, pivots, nrows):
    relations = [{} for _ in range(nrows)]
    for pivot, quotient in quotients.items():
        _, _, combination = pivots[pivot]
        for row_index, coefficient in combination.items():
            relations[row_index] = poly_add(
                relations[row_index], quotient, coefficient
            )
    return relations


def source_replay(multiplier_families, row_families):
    replay = {}
    for multipliers, rows in zip(multiplier_families, row_families):
        assert len(multipliers) == len(rows)
        for multiplier, row in zip(multipliers, rows):
            if multiplier:
                replay = poly_add(
                    replay, poly_multiply(multiplier, row_polynomial(row))
                )
    return clean(replay)


def beta_tail(polynomial, constant):
    difference = poly_add(polynomial, {(): BetaPoly(constant)}, -1)
    tail = {}
    for monomial, coefficient in difference.items():
        coefficient = BetaPoly.coerce(coefficient)
        assert not coefficient.constant
        shifted = BetaPoly(coefficient.coefficients[1:])
        if shifted:
            tail[monomial] = shifted
    assert difference == poly_scale(tail, BetaPoly.beta())
    return tail


def relation_values(relations):
    for relation in relations:
        yield from relation.values()


def selected_row_values(relations, rows):
    for relation, row in zip(relations, rows):
        if relation:
            yield from row_polynomial(row).values()


def coordinate_denominators(values):
    for value in values:
        for coefficient in BetaPoly.coerce(value).coefficients:
            for coordinate in p.flat_ratu(coefficient):
                yield coordinate.denominator


def factor_strings(polynomial):
    if not polynomial or polynomial.degree() <= 0:
        return []
    unit, factors = polynomial.factor()
    assert unit
    return sorted((str(factor), exponent) for factor, exponent in factors)


def polynomial_u_order(polynomial):
    """Return the U-adic order of a nonzero Q[U] polynomial."""
    assert polynomial
    for exponent in range(len(polynomial)):
        if polynomial[exponent]:
            return exponent
    raise AssertionError("nonzero polynomial has no nonzero coefficient")


def scalar_factor_rows(label, value):
    """Emit every Q[U] coordinate numerator/denominator factor exactly."""
    rows = []
    for coordinate_index, coordinate in enumerate(p.flat_ratu(value)):
        if not coordinate:
            continue
        numerator_factors = factor_strings(coordinate.numerator)
        denominator_factors = factor_strings(coordinate.denominator)
        rows.append((
            label,
            coordinate_index,
            str(coordinate.numerator),
            str(coordinate.denominator),
            numerator_factors,
            denominator_factors,
            polynomial_u_order(coordinate.numerator),
            polynomial_u_order(coordinate.denominator),
        ))
    assert rows
    return rows


def factor_set_from_rows(rows, numerator):
    offset = 4 if numerator else 5
    return sorted({factor for row in rows for factor, _ in row[offset]})


def leaf_denominator_ledger(named_values):
    ledger = {}
    for label, values in named_values:
        for denominator in coordinate_denominators(values):
            key = str(denominator)
            if key not in ledger:
                ledger[key] = [label, factor_strings(denominator), 0]
            ledger[key][2] += 1
    return ledger


def center_and_audit():
    assert p.Z_CURVE**2 - p.QUAD_A_VALUE*p.Z_CURVE - p.QUAD_B_VALUE == Curve()
    assert p.V_CURVE**2 == p.Y_CURVE*p.U_CURVE**3
    assert p.COMPONENT == "b3half"
    center_u = p.U_CURVE
    center_v = Curve()
    center_c = -5*center_u**2
    assert center_v == Curve()
    assert center_c + 5*center_u**2 == Curve()
    assert center_u != Curve()
    raw_b3 = (
        4*center_c**2*center_u**2 - 4*center_c*center_v**2*center_u
        + 24*center_c*center_u**4 + center_v**4
        - 20*center_v**2*center_u**3 + 20*center_u**6
    )
    assert raw_b3 == Curve() and raw_b3 + 1 != Curve()
    return center_c, center_v, center_u


EXPECTED_X11_RESIDUAL_SHA256 = (
    "3884ec0ce04a7b1488cce725551377ed5ef8e3ea20159eb98efe96ce880f552e"
)


def previous_x11_certificate(
    outdir,
    direct_qprime,
    transport_chart,
    first_rows,
    first_pivots,
    factors_first,
    free94,
    previous_rows,
    bands132,
    pole_f132,
    pole_g132,
):
    """Lift the exact X-1,11 dependency to original source equations."""
    _, _, factors_previous, dependent = solve_stage(
        len(free94), previous_rows, "previous_pole"
    )
    bad = [record for record in dependent if record[2]]
    bad_keys = [record[1] for record in bad]
    expected_bad_keys = (
        [('X-1', 11), ('X-1', 13)]
        if direct_qprime else [('X-1', 11)]
    )
    assert bad_keys == expected_bad_keys, bad_keys
    x11_records = [record for record in bad if record[1] == ('X-1', 11)]
    assert len(x11_records) == 1
    _, x11_key, residual, dependency_weights = x11_records[0]
    assert residual and residual.degree == 0
    assert beta_digest(residual) == EXPECTED_X11_RESIDUAL_SHA256
    print(f"previous_bad_keys={bad_keys}")
    print(f"Xminus1_11_beta_degree={residual.degree}")
    print(f"Xminus1_11_residual_sha256={beta_digest(residual)}")
    print(
        "Xminus1_11_left_null_sha256="
        f"{combination_digest(dependency_weights)}"
    )
    print("Xminus1_11_is_beta_independent=true")
    if direct_qprime:
        print("direct_qprime_Xminus1_13_control_present=true")
    else:
        print("omitted_direct_qprime_Xminus1_13_absent=true")
        print("omitted_direct_qprime_Xminus1_11_unchanged=true")
    print("previous_dependency_original_reduced_row_replay=true", flush=True)

    residual_inverse = residual.inverse()
    assert residual * residual_inverse == BetaPoly(1)
    residual_factor_rows = scalar_factor_rows(
        "Xminus1_11_residual", residual.constant
    )
    inverse_factor_rows = scalar_factor_rows(
        "Xminus1_11_inverse", residual_inverse.constant
    )
    localization_factor_rows = residual_factor_rows + inverse_factor_rows
    residual_numerator_factors = factor_set_from_rows(
        residual_factor_rows, True
    )
    residual_denominator_factors = factor_set_from_rows(
        residual_factor_rows, False
    )
    inverse_denominator_factors = factor_set_from_rows(
        inverse_factor_rows, False
    )
    allowed_factor = str(p.U_POLY)
    assert set(residual_denominator_factors) <= {allowed_factor}
    assert set(inverse_denominator_factors) <= {allowed_factor}
    print(f"Xminus1_11_numerator_factor_set={residual_numerator_factors}")
    print(f"Xminus1_11_denominator_factor_set={residual_denominator_factors}")
    print(f"Xminus1_11_inverse_denominator_factor_set={inverse_denominator_factors}")
    print("Xminus1_11_unit_on_DU_by_exact_inverse=true", flush=True)

    factor_lines = [
        "label\tcoordinate\tnumerator\tdenominator\tnumerator_factors\t"
        "denominator_factors\tnumerator_U_order\tdenominator_U_order"
    ]
    factor_lines.extend(
        "\t".join(map(str, row)) for row in localization_factor_rows
    )
    factor_text = "\n".join(factor_lines) + "\n"
    factor_path = outdir / "XMINUS1_11_RESIDUAL_FACTORS.tsv"
    factor_path.write_text(factor_text)

    used_previous_indices = sorted(dependency_weights)
    assert used_previous_indices
    used_previous_keys = [
        previous_rows[index][0] for index in used_previous_indices
    ]
    expected_keys = [('X-1', degree) for degree in range(12)]
    assert used_previous_keys == expected_keys, used_previous_keys

    # Invoke the exact hash-pinned parent compiler while restricting only its
    # outer `range(40)` degree loop.  Every inner range delegates unchanged.
    # This avoids constructing 28 irrelevant X-1 rows and all pole rows
    # without transcribing the source formula.
    f1 = bands132[('f', 1)]
    f2 = bands132[('f', 2)]
    g1 = bands132[('g', 1)]
    g2 = bands132[('g', 2)]

    selected_degrees = tuple(key[1] for key in used_previous_keys)
    parent_module = qd.base
    assert not hasattr(parent_module, "range")
    range_calls = []

    def source_range(*arguments):
        range_calls.append(arguments)
        if arguments == (40,):
            return selected_degrees
        return builtins.range(*arguments)

    parent_module.range = source_range
    try:
        selected_polynomials = qd.compile_previous(f1, f2, g1, g2)
    finally:
        del parent_module.range
    assert range_calls.count((40,)) == 1
    assert len(selected_polynomials) == len(selected_degrees)
    raw_previous_rows = [
        (('X-1', degree), clean(polynomial))
        for degree, polynomial in zip(selected_degrees, selected_polynomials)
    ]
    assert qd.Q_PRIME[1] == BetaPoly([0, 2])
    assert raw_previous_rows[-1][0] == ('X-1', 11)
    print(f"Xminus1_11_sparse_original_previous_keys={used_previous_keys}")
    print("Xminus1_11_hash_pinned_parent_compiler_used=true")
    print("Xminus1_11_parent_outer_range_intercept_count=1")
    print("Xminus1_11_parent_inner_ranges_delegated_unchanged=true")
    print("Xminus1_11_degree11_qprime_degree1_coefficient=2*beta")
    print("Xminus1_11_degree11_full_direct_qprime_contribution=4*beta*f2[10]", flush=True)
    raw_previous_index = {
        record[0]: index for index, record in enumerate(raw_previous_rows)
    }
    assert len(raw_previous_index) == len(raw_previous_rows)
    assert set(used_previous_keys) == set(raw_previous_index)
    previous_reduced = {
        record[0]: row_polynomial(record) for record in previous_rows
    }
    map132_to_94 = {variable: index for index, variable in enumerate(free94)}
    map94_to_132 = {index: variable for index, variable in enumerate(free94)}

    # Fast proof-carrying route: first form the exact previous-stage
    # left-null combination, then divide that single aggregate source
    # polynomial through the first-stage pivots.  Linearity makes this
    # identical to lifting each dependency edge separately, while avoiding
    # one expensive arbitrary-degree division per nonzero left-null weight.
    reduced_previous_relation = [{} for _ in previous_rows]
    raw_previous_relation = [{} for _ in raw_previous_rows]
    aggregate_raw = {}
    aggregate_reduced94 = {}
    for previous_index in used_previous_indices:
        weight = dependency_weights[previous_index]
        key = previous_rows[previous_index][0]
        reduced_previous_relation[previous_index] = {(): weight}
        raw_previous_relation[raw_previous_index[key]] = {(): weight}
        aggregate_raw = poly_add(
            aggregate_raw,
            row_polynomial(raw_previous_rows[raw_previous_index[key]]),
            weight,
        )
        aggregate_reduced94 = poly_add(
            aggregate_reduced94, previous_reduced[key], weight
        )

    target = {(): -residual}
    reduced_replay = source_replay(
        (reduced_previous_relation,), (previous_rows,)
    )
    assert reduced_replay == target
    assert aggregate_reduced94 == target

    aggregate_remainder132, aggregate_quotients = divide_polynomial(
        aggregate_raw, first_pivots
    )
    aggregate_remainder94 = remap_polynomial(
        aggregate_remainder132, map132_to_94
    )
    assert aggregate_remainder94 == target
    aggregate_first_lift = lift_relations(
        aggregate_quotients, first_pivots, len(first_rows)
    )
    first_relation = [
        poly_scale(multiplier, BetaPoly(-1))
        for multiplier in aggregate_first_lift
    ]
    raw_replay = source_replay(
        (raw_previous_relation, first_relation),
        (raw_previous_rows, first_rows),
    )
    assert raw_replay == target

    normalized_previous = [
        poly_scale(multiplier, residual_inverse)
        for multiplier in raw_previous_relation
    ]
    normalized_first = [
        poly_scale(multiplier, residual_inverse)
        for multiplier in first_relation
    ]
    normalized_target = {(): BetaPoly(-1)}
    # `raw_replay` above is the one complete original-row convolution.  The
    # normalized relation is obtained by multiplying every stored source
    # coefficient and the replayed target by the exact residual inverse;
    # no second convolution can add information.
    normalized_replay = poly_scale(raw_replay, residual_inverse)
    assert normalized_replay == normalized_target
    print(f"Xminus1_11_dependency_row_count={len(used_previous_indices)}")
    print(
        "Xminus1_11_dependency_keys="
        f"{[previous_rows[index][0] for index in used_previous_indices]}"
    )
    print(f"Xminus1_11_first_source_edge_count={sum(bool(x) for x in first_relation)}")
    print("Xminus1_11_dependency_aggregate_reduction_exact=true")
    print("Xminus1_11_aggregate_lift_to_original_first_rows=true")
    print("Xminus1_11_single_full_original_source_replay=true")
    print("Xminus1_11_normalization_by_exact_scalar_identity=true")
    print("Xminus1_11_original_previous_plus_first_source_identity_exact=true")
    print("Xminus1_11_normalized_unit_residual_is_minus_one=true", flush=True)

    selected_index = used_previous_indices[0]
    selected_key = previous_rows[selected_index][0]
    selected_raw_index = raw_previous_index[selected_key]

    # The positive identity above is replayed in full from the original
    # rows.  Certify the three negative controls by their exact deltas,
    # rather than convolving the same large source combination three more
    # times.  The coefficient ring is a polynomial ring over the exact
    # field Q(U)(algebraic constants)[beta], hence is an integral domain.
    def nonzero_product_witness(left, right):
        assert left and right
        variables = sorted({
            variable
            for monomial in tuple(left) + tuple(right)
            for variable in monomial
        })

        def exponent_key(monomial):
            counts = {variable: monomial.count(variable) for variable in variables}
            return tuple(counts[variable] for variable in variables)

        # Lexicographic order on exponent vectors is a genuine monomial
        # order, so lm(left*right)=lm(left)*lm(right), with no cancellation.
        left_monomial = max(left, key=exponent_key)
        right_monomial = max(right, key=exponent_key)
        coefficient = left[left_monomial] * right[right_monomial]
        assert coefficient
        product_monomial = tuple(sorted(left_monomial + right_monomial))
        assert exponent_key(product_monomial) == tuple(
            a + b
            for a, b in zip(
                exponent_key(left_monomial), exponent_key(right_monomial)
            )
        )
        return (
            left_monomial,
            right_monomial,
            product_monomial,
            beta_digest(coefficient),
        )

    selected_multiplier = normalized_previous[selected_raw_index]
    selected_row = row_polynomial(raw_previous_rows[selected_raw_index])
    omitted_delta_witness = nonzero_product_witness(
        selected_multiplier, selected_row
    )

    # Adding one to the selected multiplier changes the replay by the
    # selected original row itself, whose leading coefficient is nonzero.
    assert selected_row
    plus_one_lead = max(selected_row)
    assert selected_row[plus_one_lead]

    wrong_index = next(
        index for index, record in enumerate(raw_previous_rows)
        if index != selected_raw_index
        and row_polynomial(record) != row_polynomial(
            raw_previous_rows[selected_raw_index]
        )
    )
    wrong_row_delta = poly_add(
        row_polynomial(raw_previous_rows[wrong_index]), selected_row, -1
    )
    wrong_delta_witness = nonzero_product_witness(
        selected_multiplier, wrong_row_delta
    )
    print(f"omitted_source_path_key={selected_key}")
    print("negative_control_method=exact_monomial_order_integral_domain_delta")
    print("negative_control_coefficient_domain=Q(U)_exact_field_polynomial_beta")
    print(f"omitted_source_delta_witness={omitted_delta_witness}")
    print("omitted_source_path_negative_control=true")
    print(
        "plus_one_source_delta_lead="
        f"{(plus_one_lead, beta_digest(selected_row[plus_one_lead]))}"
    )
    print("plus_one_multiplier_negative_control=true")
    print(f"wrong_row_replacement_key={raw_previous_rows[wrong_index][0]}")
    print(f"wrong_row_delta_witness={wrong_delta_witness}")
    print("wrong_row_negative_control=true", flush=True)

    denominator_inputs = [
        ("transport_chart_clear", (
            BetaPoly(ECurve(Curve(p.RatU(1, transport_chart)))),
        )),
        ("Xminus1_11_residual", (residual,)),
        ("Xminus1_11_residual_inverse", (residual_inverse,)),
        ("dependency_weights", tuple(dependency_weights.values())),
        ("first_pivot_leads", tuple(
            lead for _, _, _, lead in factors_first
        )),
        ("previous_pivot_leads", tuple(
            lead for _, _, _, lead in factors_previous
        )),
        ("raw_previous_multipliers", tuple(
            relation_values(raw_previous_relation)
        )),
        ("raw_previous_rows", tuple(
            selected_row_values(raw_previous_relation, raw_previous_rows)
        )),
        ("first_multipliers", tuple(relation_values(first_relation))),
        ("first_rows", tuple(selected_row_values(first_relation, first_rows))),
        ("normalized_previous_multipliers", tuple(
            relation_values(normalized_previous)
        )),
        ("normalized_first_multipliers", tuple(
            relation_values(normalized_first)
        )),
    ]
    ledger = leaf_denominator_ledger(denominator_inputs)
    leaf_values = tuple(
        value for _, values in denominator_inputs for value in values
    )
    leaf_denominator = beta_denominator(leaf_values)
    certificate_chart = p.monic(transport_chart * leaf_denominator)
    _, certificate_chart_factors = certificate_chart.factor()
    chart_factor_set = sorted(
        str(factor) for factor, _ in certificate_chart_factors
    )
    assert set(chart_factor_set) <= {allowed_factor}
    ledger_lines = [
        "denominator\tmultiplicity\tfirst_label\tfactorization",
        *(
            f"{denominator}\t{multiplicity}\t{label}\t{factorization}"
            for denominator, (label, factorization, multiplicity)
            in sorted(ledger.items())
        ),
    ]
    ledger_text = "\n".join(ledger_lines) + "\n"
    ledger_path = outdir / "DAG_LEAF_DENOMINATORS.tsv"
    ledger_path.write_text(ledger_text)

    identity_lines = [
        "schema=TD6-A3-Q2-CMINUS5-XMINUS1-11-IDENTITY-v73",
        f"residual_sha256={beta_digest(residual)}",
        f"residual_inverse_sha256={beta_digest(residual_inverse)}",
        f"dependency_weights_sha256={canonical_digest(dependency_weights)}",
        f"normalized_previous_sha256={canonical_digest(normalized_previous)}",
        f"normalized_first_sha256={canonical_digest(normalized_first)}",
        f"normalized_replay_sha256={canonical_digest(normalized_replay)}",
        "normalized_target=-1",
    ]
    identity_text = "\n".join(identity_lines) + "\n"
    identity_path = outdir / "NORMALIZED_SOURCE_IDENTITY.txt"
    identity_path.write_text(identity_text)

    dag_lines = [
        "schema=TD6-A3-Q2-CMINUS5-XMINUS1-11-SOURCE-DAG-v73",
        "component=V=0,C=-5*U^2,D(U)",
        f"direct_qprime_retained={str(direct_qprime).lower()}",
        f"curve_source_sha256={CURVE_SHA256}",
        f"residual_sha256={beta_digest(residual)}",
        f"residual_factor_ledger_sha256={sha256(factor_text.encode()).hexdigest()}",
        f"used_previous_indices={used_previous_indices}",
        f"used_previous_keys={[previous_rows[index][0] for index in used_previous_indices]}",
        f"raw_previous_relation_sha256={canonical_digest(raw_previous_relation)}",
        f"first_relation_sha256={canonical_digest(first_relation)}",
        f"normalized_previous_sha256={canonical_digest(normalized_previous)}",
        f"normalized_first_sha256={canonical_digest(normalized_first)}",
        f"normalized_identity_sha256={sha256(identity_text.encode()).hexdigest()}",
        f"leaf_denominator_sha256={p.poly_summary(leaf_denominator)[2]}",
        f"certificate_chart_sha256={p.poly_summary(certificate_chart)[2]}",
        f"certificate_chart_factor_set={chart_factor_set}",
        "original_previous_plus_first_source_replay=true",
        "aggregate_dependency_reduction_exact=true",
        "normalized_unit_identity=true",
        "omission_plus_one_wrong_row_controls=true",
    ]
    dag_lines.extend((
        f"aggregate_raw_sha256={canonical_digest(aggregate_raw)}",
        f"aggregate_remainder132_sha256={canonical_digest(aggregate_remainder132)}",
        f"aggregate_remainder94_sha256={canonical_digest(aggregate_remainder94)}",
        f"aggregate_first_lift_sha256={canonical_digest(aggregate_first_lift)}",
    ))
    dag_text = "\n".join(dag_lines) + "\n"
    dag_path = outdir / "XMINUS1_11_PROOF_DAG.txt"
    dag_path.write_text(dag_text)

    print(f"residual_factor_ledger_path={factor_path}")
    print(f"residual_factor_ledger_sha256={sha256(factor_text.encode()).hexdigest()}")
    print(f"DAG_leaf_denominator_ledger_path={ledger_path}")
    print(f"DAG_leaf_denominator_ledger_sha256={sha256(ledger_text.encode()).hexdigest()}")
    print(f"normalized_source_identity_path={identity_path}")
    print(f"normalized_source_identity_sha256={sha256(identity_text.encode()).hexdigest()}")
    print(f"Xminus1_11_proof_DAG_path={dag_path}")
    print(f"Xminus1_11_proof_DAG_sha256={sha256(dag_text.encode()).hexdigest()}")
    print(f"leaf_denominator_summary={p.poly_summary(leaf_denominator)}")
    print(f"leaf_denominator_factor={leaf_denominator.factor()}")
    print(f"certificate_chart_summary={p.poly_summary(certificate_chart)}")
    print(f"certificate_chart_factor={certificate_chart.factor()}")
    print(f"certificate_chart_factor_set={chart_factor_set}")
    print("complete_numerator_denominator_support_emitted=true")
    print("only_U_localization_charged=true")
    print("raw_U_zero_origin_endpoint_separate_reviewed_V70=true")
    print("whole_B3_killed=false")
    print("whole_A3_killed=false")
    print("whole_TD6_killed=false")
    print("SP2_killed=false")
    print("JC2_resolved=false")
    if direct_qprime:
        print("TD6-A3-Q2-CMINUS5-XMINUS1-11-SOURCE-DAG-V73 PASS")
    else:
        print("TD6-A3-Q2-CMINUS5-XMINUS1-11-QPRIME-CONTROL-V73 PASS")


def main():
    outdir = Path(os.environ.get("TD6_OUTPUT_DIR", ".")).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    p.configure()
    center = center_and_audit()
    print("producer=TD6-A3-Q2-CMINUS5-XMINUS1-11-SOURCE-DAG-V73")
    print("component=V=0,C=-5*U^2,D(U)")
    print(f"coefficient_field_adapter={p.COMPONENT}")
    print("q_beta=t+beta*t^2+t^25")
    print(f"direct_qprime_retained={str(not OMIT_DIRECT_QPRIME).lower()}")
    print("source_p_boundary=t^15_fixed")
    print("source_dead_stretch=0_fixed")
    print("source_F1_orbit=frozen")
    print("source_pole_scale_and_data=frozen")
    print("weighted_scaling_used=false")
    print("scope=Q(U)_function_field_of_raw_line", flush=True)
    print("raw_center_V_zero=true")
    print("raw_center_C_plus_5U2_zero=true")
    print("raw_B3_identity_zero=true")
    print("raw_line_U_zero_is_origin=true", flush=True)

    r.fb.CENTER = center
    r.fb._X_POWER_CACHE.clear()
    nf, rows_f = r.fb.build_transport(
        15, 60, 3, {15: r.b.Q(1)}, r.fb.F1_F_PATTERN, r.fb.POLE_F_PATTERN
    )
    ng, rows_g = r.fb.build_transport(
        25, 100, 5, {1: r.b.Q(1), 25: r.b.Q(1)},
        r.fb.F1_G_PATTERN, r.fb.POLE_G_PATTERN,
    )
    transport = [(('f',) + key, row, rhs) for key, row, rhs in rows_f]
    transport += [
        (
            ('g',) + key,
            {nf + variable: coefficient for variable, coefficient in row.items()},
            rhs,
        )
        for key, row, rhs in rows_g
    ]
    ordered = [row for row in transport if row[0][1] != 'X'] + [
        row for row in transport if row[0][1] == 'X'
    ]
    transport_pivots, records, events, transport_chart = p.factor_transport(ordered)
    pivot_rhs, compatibility = propagate_beta(ordered, records)
    assert not compatibility
    assert len(transport_pivots) == 3470
    free = [
        variable for variable in range(nf + ng)
        if variable not in transport_pivots
    ]
    assert len(free) == 132
    free_parameter = {variable: index for index, variable in enumerate(free)}
    print(f"transport_rank={len(transport_pivots)}/{nf+ng}")
    print(f"transport_event_count={len(events)}")
    print(f"transport_chart_summary={p.poly_summary(transport_chart)}")
    print("transport_beta_original_row_propagation=true", flush=True)

    def restrict(row):
        return restrict_row_beta(
            row, transport_pivots, pivot_rhs, free_parameter
        )

    bands132 = {}
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
                forms.append(restrict(row))
            bands132[(owner, exponent)] = forms
    pole_f132 = []
    for degree in range(61):
        pole_f132.append(restrict({
            variable: Curve.coerce(coefficient)
            for variable, coefficient in nr.pole_coefficient(
                15, 60, -2, degree
            ).items()
        }))
    pole_g132 = []
    for degree in range(101):
        pole_g132.append(restrict({
            nf + variable: Curve.coerce(coefficient)
            for variable, coefficient in nr.pole_coefficient(
                25, 100, -4, degree
            ).items()
        }))
    print("transport_x_and_pole_sections_exact=true", flush=True)

    configure_qd(direct_qprime=not OMIT_DIRECT_QPRIME)
    first_rows = qd.pack(
        'X-2', qd.first_band_polynomials(
            bands132[('f', 1)], bands132[('g', 1)]
        )
    )
    first_pivots, forms94, free94, factors_first = parameterize(
        len(free), first_rows, "first"
    )
    assert len(free94) == 94
    bands94 = {key: compose(forms, forms94) for key, forms in bands132.items()}
    pole_f94 = compose(pole_f132, forms94)
    pole_g94 = compose(pole_g132, forms94)
    previous_rows = qd.pack(
        'X-1', qd.compile_previous(
            bands94[('f', 1)], bands94[('f', 2)],
            bands94[('g', 1)], bands94[('g', 2)],
        )
    )
    previous_rows += qd.pack(
        'P1', qd.compile_pole_previous(pole_f94, pole_g94)
    )
    previous_x11_certificate(
        outdir=outdir,
        direct_qprime=not OMIT_DIRECT_QPRIME,
        transport_chart=transport_chart,
        first_rows=first_rows,
        first_pivots=first_pivots,
        factors_first=factors_first,
        free94=free94,
        previous_rows=previous_rows,
        bands132=bands132,
        pole_f132=pole_f132,
        pole_g132=pole_g132,
    )
    return

    # Unreachable V72 predecessor body retained byte-for-byte below as a
    # custody/reference implementation.  V73's theorem gate ends above at
    # the exact previous-row source certificate and never consumes staged
    # current/N13 algebra.
    previous_pivots, forms56, free56, factors_previous = parameterize(
        len(free94), previous_rows, "previous_pole"
    )
    assert len(free56) == 56
    bands56 = {key: compose(forms, forms56) for key, forms in bands94.items()}
    current_rows = qd.pack('X0', qd.compile_current(
        *[bands56[('f', exponent)] for exponent in (1, 2, 3)],
        *[bands56[('g', exponent)] for exponent in (1, 2, 3)],
    ))
    current_pivots, _, factors_current, current_dependent = solve_stage(
        len(free56), current_rows, "current"
    )
    compatibilities = [
        record for record in current_dependent if record[2]
    ]
    n13_records = [
        record for record in compatibilities if record[1] == ('X0', 13)
    ]
    print(f"current_compatibility_count={len(compatibilities)}")
    print(f"N13_record_count={len(n13_records)}")
    for index, (_, key, residual, combination) in enumerate(compatibilities):
        print(f"compatibility[{index}]_key={key}")
        print(f"compatibility[{index}]_degree={residual.degree}")
        print(f"compatibility[{index}]_sha256={beta_digest(residual)}")
        print(f"compatibility[{index}]_left_null_sha256={combination_digest(combination)}")
    print("current_compatibility_original_row_replay=true", flush=True)

    S = ECurve(qd.uniform.S_FIELD)
    k = ECurve(252) - 342*S + 144*S**2 - 36*S**3
    expected = BetaPoly([0, k/25])
    assert k * k.inverse() == ECurve(1)
    k_parameter_denominator_factors = sorted({
        factor
        for coordinate in p.flat_ratu(k)
        for factor, _ in factor_strings(coordinate.denominator)
    })
    assert not k_parameter_denominator_factors
    n13 = n13_records[0][2] if len(n13_records) == 1 else BetaPoly()
    if OMIT_DIRECT_QPRIME:
        assert len(n13_records) != 1 or n13 != expected
        print("direct_qprime_omission_changes_N13=true")
    else:
        assert len(n13_records) == 1
        assert n13 == expected
        assert not n13.constant and n13.degree == 1
        print("N13_equals_k_beta_over_25=true")
        print(f"N13_sha256={beta_digest(n13)}")
        print(f"N13_left_null_sha256={combination_digest(n13_records[0][3])}")
        print("k_is_frozen_residue_field_unit=true")
        print("k_curve_parameter_denominator_factor_set=[]")

    # Dependency-closed source lift of the singleton N13 current row.
    map132_to_94 = {variable: index for index, variable in enumerate(free94)}
    map94_to_132 = {index: variable for index, variable in enumerate(free94)}
    map94_to_56 = {variable: index for index, variable in enumerate(free56)}
    map56_to_94 = {index: variable for index, variable in enumerate(free56)}

    raw_previous_rows = source_records(
        'X-1', qd.compile_previous(
            bands132[('f', 1)], bands132[('f', 2)],
            bands132[('g', 1)], bands132[('g', 2)],
        )
    )
    raw_previous_rows += source_records(
        'P1', qd.compile_pole_previous(pole_f132, pole_g132)
    )
    raw_previous_index = {
        record[0]: index for index, record in enumerate(raw_previous_rows)
    }
    previous_reduced = {
        record[0]: row_polynomial(record) for record in previous_rows
    }
    previous_first_relations_by_key = {}

    def lift_previous_key(key):
        if key in previous_first_relations_by_key:
            return previous_first_relations_by_key[key]
        raw_polynomial = row_polynomial(raw_previous_rows[raw_previous_index[key]])
        remainder132, quotients = divide_polynomial(raw_polynomial, first_pivots)
        relation = lift_relations(quotients, first_pivots, len(first_rows))
        remainder94 = remap_polynomial(remainder132, map132_to_94)
        assert clean(remainder94) == clean(previous_reduced[key]), key
        replay = source_replay((relation,), (first_rows,))
        target = poly_add(
            raw_polynomial, remap_polynomial(remainder94, map94_to_132), -1
        )
        assert replay == clean(target)
        previous_first_relations_by_key[key] = relation
        return relation

    quadratic_previous = [
        record for record in raw_previous_rows
        if total_degree(row_polynomial(record)) == 2
    ]
    assert quadratic_previous
    quadratic_key = quadratic_previous[0][0]
    quadratic_relation = lift_previous_key(quadratic_key)
    quadratic_raw = row_polynomial(quadratic_previous[0])
    quadratic_remainder, _ = divide_polynomial(quadratic_raw, first_pivots)
    assert source_replay((quadratic_relation,), (first_rows,)) == clean(
        poly_add(quadratic_raw, quadratic_remainder, -1)
    )
    print(f"previous_raw_row_count_available={len(raw_previous_rows)}")
    print(f"previous_raw_quadratic_row_count={len(quadratic_previous)}")
    print(f"quadratic_source_positive_control_key={quadratic_key}")
    print("quadratic_source_positive_control_exact=true")
    print("arbitrary_degree_original_rows_preserved=true", flush=True)

    raw_current_rows = source_records('X0', qd.compile_current(
        *[bands132[('f', exponent)] for exponent in (1, 2, 3)],
        *[bands132[('g', exponent)] for exponent in (1, 2, 3)],
    ))
    raw_current_index = {
        record[0]: index for index, record in enumerate(raw_current_rows)
    }
    current_reduced = {
        record[0]: row_polynomial(record) for record in current_rows
    }
    current_lift_cache = {}

    def lift_current(row_index):
        key = current_rows[row_index][0]
        if key in current_lift_cache:
            return current_lift_cache[key]
        raw_polynomial = row_polynomial(raw_current_rows[raw_current_index[key]])
        remainder132, first_quotients = divide_polynomial(
            raw_polynomial, first_pivots
        )
        first_relation = lift_relations(
            first_quotients, first_pivots, len(first_rows)
        )
        remainder94 = remap_polynomial(remainder132, map132_to_94)
        remainder94_after, previous_quotients = divide_polynomial(
            remainder94, previous_pivots
        )
        previous_relation = lift_relations(
            previous_quotients, previous_pivots, len(previous_rows)
        )
        remainder56 = remap_polynomial(remainder94_after, map94_to_56)
        assert clean(remainder56) == clean(current_reduced[key]), key
        first_replay = source_replay((first_relation,), (first_rows,))
        assert first_replay == clean(poly_add(
            raw_polynomial, remap_polynomial(remainder94, map94_to_132), -1
        ))
        previous_replay = source_replay((previous_relation,), (previous_rows,))
        assert previous_replay == clean(poly_add(
            remainder94, remap_polynomial(remainder56, map56_to_94), -1
        ))
        for previous_index, polynomial in enumerate(previous_relation):
            if polynomial:
                lift_previous_key(previous_rows[previous_index][0])
        record = (
            raw_polynomial, remainder94, remainder56,
            first_relation, previous_relation,
        )
        current_lift_cache[key] = record
        return record

    _, _, _, n13_weights = n13_records[0]
    required_current = sorted(n13_weights)
    assert required_current == [13]
    for row_index in required_current:
        lift_current(row_index)
    n13_previous_edge_indices = sorted({
        previous_index
        for row_index in required_current
        for previous_index, multiplier in enumerate(lift_current(row_index)[4])
        if multiplier
    })
    n13_previous_edge_keys = [
        previous_rows[index][0] for index in n13_previous_edge_indices
    ]
    assert n13_previous_edge_keys
    print(f"current_rows_source_lifted_indices={required_current}")
    print(f"N13_previous_edge_keys={n13_previous_edge_keys}")
    print(f"quadratic_control_is_N13_edge={str(quadratic_key in n13_previous_edge_keys).lower()}")
    print(
        "previous_lift_cache_keys="
        f"{sorted(previous_first_relations_by_key)}"
    )
    print("dependency_closed_original_rows_reduced_exactly=true")
    print("current_through_previous_and_first_source_replay=true", flush=True)

    staged_left = {}
    staged_omitted = {}
    omitted_index = min(n13_weights)
    denominator_inputs = []
    dag_lines = [
        "schema=TD6-A3-Q2-CMINUS5-SOURCE-DAG-v72",
        "component=V=0,C=-5*U^2,D(U)",
        f"coefficient_field_adapter={p.COMPONENT}",
        f"curve_source_sha256={CURVE_SHA256}",
        f"N13_previous_edge_keys={n13_previous_edge_keys}",
        f"quadratic_control_key={quadratic_key}",
    ]
    for row_index, weight in sorted(n13_weights.items()):
        key = current_rows[row_index][0]
        raw_polynomial, remainder94, remainder56, first_relation, previous_relation = (
            lift_current(row_index)
        )
        reduced = current_reduced[key]
        staged_left = poly_add(staged_left, reduced, weight)
        if row_index != omitted_index:
            staged_omitted = poly_add(staged_omitted, reduced, weight)
        dag_lines.extend((
            f"current_row_index={row_index}",
            f"current_row_key={key}",
            f"weight_sha256={canonical_digest(weight)}",
            f"raw_current_sha256={canonical_digest(raw_polynomial)}",
            f"remainder94_sha256={canonical_digest(remainder94)}",
            f"remainder56_sha256={canonical_digest(remainder56)}",
            f"first_relation_sha256={canonical_digest(first_relation)}",
            f"previous_relation_sha256={canonical_digest(previous_relation)}",
        ))
        denominator_inputs.extend((
            (f"current_{row_index}_weight", (weight,)),
            (f"current_{row_index}_first_multipliers", relation_values(first_relation)),
            (f"current_{row_index}_first_rows", selected_row_values(first_relation, first_rows)),
            (f"current_{row_index}_previous_multipliers", relation_values(previous_relation)),
            (f"current_{row_index}_previous_rows", selected_row_values(previous_relation, previous_rows)),
            (f"current_{row_index}_raw", raw_polynomial.values()),
            (f"current_{row_index}_reduced", reduced.values()),
        ))

    for previous_key, relation in sorted(previous_first_relations_by_key.items()):
        raw_previous = row_polynomial(raw_previous_rows[raw_previous_index[previous_key]])
        reduced_previous = previous_reduced[previous_key]
        dag_lines.extend((
            f"previous_edge_key={previous_key}",
            f"previous_edge_relation_sha256={canonical_digest(relation)}",
            f"previous_edge_raw_sha256={canonical_digest(raw_previous)}",
            f"previous_edge_reduced_sha256={canonical_digest(reduced_previous)}",
        ))
        denominator_inputs.extend((
            (f"previous_{previous_key}_first_multipliers", relation_values(relation)),
            (f"previous_{previous_key}_first_rows", selected_row_values(relation, first_rows)),
            (f"previous_{previous_key}_raw", raw_previous.values()),
            (f"previous_{previous_key}_reduced", reduced_previous.values()),
        ))

    assert staged_left == {(): -n13}
    assert staged_omitted != {(): -n13}
    n13_raw, n13_remainder94, n13_remainder56, _, n13_previous_relation = (
        lift_current(required_current[0])
    )
    omitted_previous_index = n13_previous_edge_indices[0]
    omitted_previous_relation = list(n13_previous_relation)
    omitted_previous_relation[omitted_previous_index] = {}
    previous_target = clean(poly_add(
        n13_remainder94,
        remap_polynomial(n13_remainder56, map56_to_94),
        -1,
    ))
    assert source_replay(
        (omitted_previous_relation,), (previous_rows,)
    ) != previous_target
    dag_lines.extend((
        f"staged_left_sha256={canonical_digest(staged_left)}",
        f"staged_target_sha256={canonical_digest({(): -n13})}",
        f"omitted_row_index={omitted_index}",
        "each_current_edge_original_row_replay=true",
        "each_selected_previous_edge_original_row_replay=true",
        "staged_left_null_relation_exact=true",
    ))
    print("N13_each_dependency_edge_original_row_replay=true")
    print("N13_singleton_current_row_omission_negative_control=true")
    print(
        "N13_previous_edge_omission_key="
        f"{previous_rows[omitted_previous_index][0]}"
    )
    print("N13_previous_edge_omission_negative_control=true")
    print("N13_full_first_previous_current_source_identity_exact_by_DAG=true", flush=True)

    # Genuine P12 is a direct-first certificate, independent of the
    # previous-stage echelon.  Recompute it over the present curve field.
    p12_key = ('X0', 12)
    p12_raw = row_polynomial(raw_current_rows[raw_current_index[p12_key]])
    p12_remainder, p12_quotients = divide_polynomial(p12_raw, first_pivots)
    p12_relation = lift_relations(p12_quotients, first_pivots, len(first_rows))
    p12_source = source_replay((p12_relation,), (first_rows,))
    assert p12_source == clean(poly_add(p12_raw, p12_remainder, -1))
    unit = -k/50
    raw_base = projection(p12_raw, 0)
    assert projection(p12_remainder, 0) == {(): unit}
    tail = beta_tail(p12_remainder, unit)
    assert len(tail) == 2
    n13_multiplier = poly_scale(tail, ECurve(25)/k)
    assert poly_scale(n13_multiplier, n13) == poly_scale(
        tail, BetaPoly.beta()
    )
    combined = poly_add(
        p12_remainder, poly_scale(n13_multiplier, n13), -1
    )
    assert combined == {(): BetaPoly(unit)}
    assert p12_remainder != {(): BetaPoly(unit)}
    assert sum(bool(relation) for relation in p12_relation) == 28
    dag_lines.extend((
        f"raw_P12_base_sha256={p.polynomial_digest(raw_base)}",
        f"P12_remainder_sha256={canonical_digest(p12_remainder)}",
        f"P12_relation_sha256={canonical_digest(p12_relation)}",
        f"P12_source_sha256={canonical_digest(p12_source)}",
        f"P12_beta_tail_sha256={canonical_digest(tail)}",
        f"N13_multiplier_sha256={canonical_digest(n13_multiplier)}",
        f"unit_sha256={canonical_digest(unit)}",
        "P12_first_original_row_replay=true",
        "P12_minus_multiplier_times_N13_equals_minus_k_over_50=true",
    ))
    denominator_inputs.extend((
        ("N13_scalar", (n13,)),
        ("P12_unit", (unit,)),
        ("P12_raw", p12_raw.values()),
        ("P12_remainder", p12_remainder.values()),
        ("P12_first_multipliers", relation_values(p12_relation)),
        ("P12_first_rows", selected_row_values(p12_relation, first_rows)),
        ("P12_beta_tail", tail.values()),
        ("N13_multiplier", n13_multiplier.values()),
        ("transport_chart_clear", (BetaPoly(ECurve(Curve(p.RatU(1, transport_chart)))),)),
    ))
    print(f"genuine_P12_raw_term_count={len(p12_raw)}")
    print(f"genuine_P12_base_term_count={len(raw_base)}")
    print("P12_first_original_row_replay=true")
    print("P12_first_nonzero_rows=28")
    print("P12_N13_scalar_glue_exact=true")
    print("P12_live_without_N13_object_inequality=true")
    print("P12_without_N13_negative_control=true")
    print("combined_unit_residual_is_minus_k_over_50=true", flush=True)

    ledger = leaf_denominator_ledger(denominator_inputs)
    leaf_factors = sorted({
        factor
        for _, factors, _ in ledger.values()
        for factor, _ in factors
    })
    ledger_lines = [
        "denominator\tmultiplicity\tfirst_label\tfactorization",
        *(
            f"{denominator}\t{multiplicity}\t{label}\t{factorization}"
            for denominator, (label, factorization, multiplicity)
            in sorted(ledger.items())
        ),
    ]
    ledger_text = "\n".join(ledger_lines) + "\n"
    ledger_path = outdir / "DAG_LEAF_DENOMINATORS.tsv"
    ledger_path.write_text(ledger_text)
    dag_lines.append(f"curve_leaf_factor_set={leaf_factors}")
    dag_text = "\n".join(dag_lines) + "\n"
    dag_path = outdir / "N13_P12_PROOF_DAG.txt"
    dag_path.write_text(dag_text)
    only_u_leaf_factors = all(factor == str(p.U_POLY) for factor in leaf_factors)
    print(f"DAG_leaf_denominator_count={len(ledger)}")
    print(f"DAG_leaf_denominator_ledger_path={ledger_path}")
    print(f"DAG_leaf_denominator_ledger_sha256={sha256(ledger_text.encode()).hexdigest()}")
    print(f"N13_P12_proof_DAG_path={dag_path}")
    print(f"N13_P12_proof_DAG_sha256={sha256(dag_text.encode()).hexdigest()}")
    print(f"DAG_leaf_denominator_factor_set={leaf_factors}")
    print(f"DAG_leaf_factors_only_U={str(only_u_leaf_factors).lower()}")
    print("DAG_leaf_denominator_all_factors_emitted=true")
    print("DAG_denominator_support_kind=coefficient_leaf_union")
    print("curve_fraction_field_source_identity_exact=true", flush=True)

    stage_values = []
    for factors in (factors_first, factors_previous, factors_current):
        stage_values.extend(lead for _, _, _, lead in factors)
    for _, _, residual, combination in compatibilities:
        stage_values.append(residual)
        stage_values.extend(combination.values())
    stage_denominator = beta_denominator(stage_values)
    certificate_chart = p.monic(transport_chart * stage_denominator)
    _, chart_factors = certificate_chart.factor()
    only_parameter_zero = all(
        factor == p.U_POLY for factor, _ in chart_factors
    )
    print(f"stage_denominator_summary={p.poly_summary(stage_denominator)}")
    print(f"stage_denominator_factor={stage_denominator.factor()}")
    print(f"certificate_chart_summary={p.poly_summary(certificate_chart)}")
    print(f"certificate_chart_factor={certificate_chart.factor()}")
    print(f"only_parameter_zero_exception={str(only_parameter_zero).lower()}")
    print("every_denominator_norm_factor_still_charged=true")
    print("genuine_P12_source_dependency_replayed_in_this_run=true")
    print("raw_U_zero_origin_endpoint_still_separate=true")
    print("component_all_beta_killed=false")
    print("fixed_A3_all_beta_killed=false")
    print("whole_TD6_killed=false")
    print("SP2_killed=false")
    print("JC2_resolved=false")
    if OMIT_DIRECT_QPRIME:
        print("TD6-A3-Q2-CMINUS5-SOURCE-DAG-V72-OMISSION-CONTROL PASS")
    else:
        print("TD6-A3-Q2-CMINUS5-SOURCE-DAG-V72 PASS")


if __name__ == "__main__":
    if os.environ.get("TD6_PREFLIGHT_ONLY") == "1":
        p.configure()
        center_and_audit()
        print("producer=TD6-A3-Q2-CMINUS5-XMINUS1-11-SOURCE-DAG-V73")
        print("preflight_component=V=0,C=-5*U^2,D(U)")
        print(f"coefficient_field_adapter={p.COMPONENT}")
        print(f"curve_source_sha256={CURVE_SHA256}")
        print("recursive_import_and_raw_line_preflight=true")
        print("TD6-A3-Q2-CMINUS5-XMINUS1-11-SOURCE-DAG-V73 PREFLIGHT PASS")
    else:
        main()
