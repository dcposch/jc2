#!/usr/bin/env python3
"""Exact q_beta N13 gate on licensed TD6 exceptional-curve fields.

Supported components are the H=B3 intersection (`p3`) and the two finite
B3 chart factors `t^2-4t+2` (`b3tq`) and `t=1/2` (`b3half`).  The coefficient
fields and center maps are imported byte-for-byte from the frozen fixed-beta
curve producer.  This script adds an honest polynomial beta, retains its two
source entry points, and carries transport, first, previous/pole, and current
row ancestry through the X0,t13 compatibility.

This is a function-field discriminator.  Every Q[w] denominator/norm factor
is emitted and remains charged.  No component closure is inferred here.
"""

from fractions import Fraction
from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
CURVE_PATH = (
    HERE.parent / "td6_c1_c3_two_center_cover_20260824"
    / "c1_c2_c3_p3_quotient.py"
)
CURVE_SHA256 = "91745b0ef827306e27a7126503d637539b47fb430262d380faad306ee9a510de"
assert sha256(CURVE_PATH.read_bytes()).hexdigest() == CURVE_SHA256
spec = importlib.util.spec_from_file_location("td6_q2_n13_curve_source", CURVE_PATH)
p = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = p
spec.loader.exec_module(p)

assert p.COMPONENT in {"p3", "b3tq", "b3half"}
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
    return forms, free, factors


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


def center_and_audit():
    assert p.Z_CURVE**2 - p.QUAD_A_VALUE*p.Z_CURVE - p.QUAD_B_VALUE == Curve()
    assert p.V_CURVE**2 == p.Y_CURVE*p.U_CURVE**3
    if p.COMPONENT in {"b3tq", "b3half"}:
        t = p.Z_CURVE if p.COMPONENT == "b3tq" else Curve(Fraction(1, 2))
        w = p.U_CURVE
        x_weight = (-5*t**2 + 20*t - 4)/(t-2)**2
        y_weight = 16*t/(t-2)**2
        center_u = w**2/y_weight
        center_v = w**3/y_weight
        center_c = x_weight*w**4/y_weight**2
        if p.COMPONENT == "b3tq":
            assert t**2 - 4*t + 2 == Curve()
        else:
            assert 2*t - 1 == Curve()
        assert center_v/center_u == w
        assert center_c/center_u**2 == x_weight
        assert center_v**2/center_u**3 == y_weight
        raw_b3 = (
            4*center_c**2*center_u**2 - 4*center_c*center_v**2*center_u
            + 24*center_c*center_u**4 + center_v**4
            - 20*center_v**2*center_u**3 + 20*center_u**6
        )
        assert raw_b3 == Curve() and raw_b3 + 1 != Curve()
        return center_c, center_v, center_u
    assert p.COMPONENT == "p3"
    assert p.Y_CURVE**2 - 32*p.Y_CURVE + 128 == Curve()
    center = (3*p.U_CURVE**2, p.V_CURVE, p.U_CURVE)
    c, v, u = center
    assert c - 3*u**2 == Curve()
    assert v**4 - 32*v**2*u**3 + 128*u**6 == Curve()
    return center


def main():
    p.configure()
    center = center_and_audit()
    print(f"component={p.COMPONENT}")
    print("q_beta=t+beta*t^2+t^25")
    print(f"direct_qprime_retained={str(not OMIT_DIRECT_QPRIME).lower()}")
    print("source_p_boundary=t^15_fixed")
    print("source_dead_stretch=0_fixed")
    print("source_F1_orbit=frozen")
    print("source_pole_scale_and_data=frozen")
    print("weighted_scaling_used=false")
    print("scope=function_field_of_exact_printed_component", flush=True)

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
    forms94, free94, factors_first = parameterize(
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
    forms56, free56, factors_previous = parameterize(
        len(free94), previous_rows, "previous_pole"
    )
    assert len(free56) == 56
    bands56 = {key: compose(forms, forms56) for key, forms in bands94.items()}
    current_rows = qd.pack('X0', qd.compile_current(
        *[bands56[('f', exponent)] for exponent in (1, 2, 3)],
        *[bands56[('g', exponent)] for exponent in (1, 2, 3)],
    ))
    _, _, factors_current, current_dependent = solve_stage(
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
    print("fixed_beta_curve_P12_dependency_separate=true")
    print("component_all_beta_killed=false")
    print("fixed_A3_all_beta_killed=false")
    print("whole_TD6_killed=false")
    print("SP2_killed=false")
    print("JC2_resolved=false")
    if OMIT_DIRECT_QPRIME:
        print("TD6-A3-Q2-N13-CURVE-OMISSION-CONTROL PASS")
    else:
        print("TD6-A3-Q2-N13-CURVE PASS")


if __name__ == "__main__":
    main()
