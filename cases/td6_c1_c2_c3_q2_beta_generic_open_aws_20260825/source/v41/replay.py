#!/usr/bin/env python3
"""Exact raw-stratum TD6 q2 N13 discriminator over E(C,V,U)[beta].

This producer retains the full transport, first, previous/pole, and current
stages.  It eliminates in the polynomial ring K[beta], K=E(C,V,U), accepting
only beta-independent pivot units.  Every accepted row is replayed against
the stage-original rows and every dependent current row carries its exact
left-null combination.

The target is the reviewed fixed-center compatibility

    N13 = (k/25)*beta,
    k = 252-342*S+144*S^2-36*S^3.

The generic fraction-field identity is not a complete A3 cover.  This driver
rebuilds one exact center stratum at a time, retains original-row ancestry,
and emits every surviving denominator or nonunit polynomial for recursive
raw-stratum routing.  It never promotes a fraction-field result to a global
family statement.
"""

from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
DUAL_PATH = (
    HERE.parent / "td6_c1_c2_c3_q2_beta_dual_20260825" / "replay.py"
)
DUAL_SHA256 = "cf3f3f028b99771a156a422d73a99eefdc9f04fbdc0698d8e8baf962efa4cf7f"
assert sha256(DUAL_PATH.read_bytes()).hexdigest() == DUAL_SHA256
spec = importlib.util.spec_from_file_location("td6_a3_q2_n13_parent", DUAL_PATH)
b = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = b
spec.loader.exec_module(b)

r, tri, Rat3, E3 = b.r, b.tri, b.Rat3, b.E3
C, V, U, H, B3 = b.C, b.V, b.U, b.H, b.B3
qd, nr = r.qd, r.qd.nr
OMIT_DIRECT_QPRIME = "--omit-direct-qprime" in sys.argv
STRATUM_ARGUMENTS = [
    argument.split("=", 1)[1]
    for argument in sys.argv[1:]
    if argument.startswith("--stratum=")
]
assert len(STRATUM_ARGUMENTS) <= 1
STRATUM = STRATUM_ARGUMENTS[0] if STRATUM_ARGUMENTS else "generic"
assert STRATUM in {
    "generic", "u-zero", "h-zero", "u-h-zero", "origin", "b3-param",
    "v-zero", "v-h-zero", "v-cplus1-zero", "v-cplus5-zero",
}
assert all(
    arg == "--omit-direct-qprime" or arg.startswith("--stratum=")
    for arg in sys.argv[1:]
)


class BetaPoly:
    """Dense univariate E(C,V,U)[beta] polynomial."""

    __slots__ = ("coefficients",)

    def __init__(self, value=0):
        if isinstance(value, BetaPoly):
            self.coefficients = value.coefficients
            return
        if isinstance(value, (list, tuple)):
            coefficients = [E3.coerce(entry) for entry in value]
        else:
            coefficients = [E3.coerce(value)]
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
        return self.coefficients[0] if self.coefficients else E3()

    @property
    def leading(self):
        return self.coefficients[-1] if self.coefficients else E3()

    def coefficient(self, degree):
        return (
            self.coefficients[degree]
            if 0 <= degree < len(self.coefficients)
            else E3()
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
        return BetaPoly([-value for value in self.coefficients])

    def __sub__(self, other):
        return self + (-BetaPoly.coerce(other))

    def __rsub__(self, other):
        return BetaPoly.coerce(other) - self

    def __mul__(self, other):
        other = BetaPoly.coerce(other)
        if not self or not other:
            return BetaPoly()
        coefficients = [E3()] * (
            len(self.coefficients) + len(other.coefficients) - 1
        )
        for left_degree, left in enumerate(self.coefficients):
            for right_degree, right in enumerate(other.coefficients):
                coefficients[left_degree + right_degree] += left * right
        return BetaPoly(coefficients)

    __rmul__ = __mul__

    def inverse(self):
        assert self.degree == 0, (
            "nonunit beta pivot", self.degree, repr(self)
        )
        return BetaPoly(self.constant.inverse())

    def __truediv__(self, other):
        return self * BetaPoly.coerce(other).inverse()

    def __rtruediv__(self, other):
        return BetaPoly.coerce(other) / self

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        out, base = BetaPoly(1), self
        while exponent:
            if exponent & 1:
                out *= base
            base *= base
            exponent //= 2
        return out

    def __eq__(self, other):
        return self.coefficients == BetaPoly.coerce(other).coefficients

    def __repr__(self):
        return "BetaPoly(" + ",".join(repr(c) for c in self.coefficients) + ")"


def polynomial_divmod(numerator, denominator):
    """Euclidean division in E(C,V,U)[beta]."""
    numerator, denominator = BetaPoly(numerator), BetaPoly(denominator)
    assert denominator
    quotient, remainder = BetaPoly(), numerator
    while remainder and remainder.degree >= denominator.degree:
        shift = remainder.degree - denominator.degree
        coefficient = remainder.leading / denominator.leading
        term = BetaPoly([E3()] * shift + [coefficient])
        quotient += term
        remainder -= term * denominator
    return quotient, remainder


def polynomial_xgcd(left, right):
    """Monic gcd plus exact Bezout coefficients over the E3 fraction field."""
    old_r, new_r = BetaPoly(left), BetaPoly(right)
    old_s, new_s = BetaPoly(1), BetaPoly()
    old_t, new_t = BetaPoly(), BetaPoly(1)
    while new_r:
        quotient, remainder = polynomial_divmod(old_r, new_r)
        old_r, new_r = new_r, remainder
        old_s, new_s = new_s, old_s - quotient*new_s
        old_t, new_t = new_t, old_t - quotient*new_t
    if not old_r:
        return BetaPoly(), BetaPoly(), BetaPoly()
    inverse = BetaPoly(old_r.leading.inverse())
    gcd, left_weight, right_weight = (
        old_r*inverse, old_s*inverse, old_t*inverse
    )
    assert left_weight*left + right_weight*right == gcd
    return gcd, left_weight, right_weight


def polynomial_ideal_gcd(values):
    """Return the monic generator and an exact multi-Bezout certificate."""
    values = [BetaPoly(value) for value in values if value]
    assert values
    gcd, weights = values[0], [BetaPoly(1)]
    for value in values[1:]:
        gcd, old_weight, new_weight = polynomial_xgcd(gcd, value)
        weights = [old_weight*weight for weight in weights] + [new_weight]
    inverse = BetaPoly(gcd.leading.inverse())
    gcd = gcd*inverse
    weights = [weight*inverse for weight in weights]
    assert sum(
        (weight*value for weight, value in zip(weights, values)), BetaPoly()
    ) == gcd
    return values, gcd, weights


def digest(value):
    return sha256(repr(value).encode()).hexdigest()


def poly_from_dual(value):
    value = b.EDual.coerce(value)
    return BetaPoly([value.value, value.derivative])


def configure_qd(direct_qprime=True):
    qd.Dual = BetaPoly
    qd.B = BetaPoly.beta()
    qd.S = BetaPoly(E3(qd.uniform.S_FIELD))
    qd.D = BetaPoly(E3(qd.uniform.D_FIELD))
    qd.L = BetaPoly(E3(qd.uniform.L_FIELD))
    qd.A = BetaPoly(E3(qd.uniform.A_FIELD))
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


def convert_form(form):
    constant, coefficients = form
    return (
        poly_from_dual(constant),
        {variable: poly_from_dual(value) for variable, value in coefficients.items()},
    )


def add_to_row(row, variable, value):
    value = BetaPoly.coerce(value)
    total = row.get(variable, BetaPoly()) + value
    if total:
        row[variable] = total
    else:
        row.pop(variable, None)


def source_polynomial(row, rhs):
    out = {(): -BetaPoly.coerce(rhs)} if rhs else {}
    for variable, coefficient in row.items():
        coefficient = BetaPoly.coerce(coefficient)
        if coefficient:
            out[(variable,)] = coefficient
    return out


def add_polynomial(left, right, scale=1):
    scale = BetaPoly.coerce(scale)
    out = dict(left)
    for monomial, coefficient in right.items():
        value = out.get(monomial, BetaPoly()) + scale*coefficient
        if value:
            out[monomial] = value
        else:
            out.pop(monomial, None)
    return out


def emit_stage_incompatibilities(dependent, stage):
    """Emit exact K[beta] compatibility ideal with original-row ancestry."""
    bad = [record for record in dependent if record[2]]
    if not bad:
        return False
    residuals, gcd, bezout = polynomial_ideal_gcd(
        [residual for _, _, residual, _ in bad]
    )
    assert len(residuals) == len(bad)
    for index, ((row_index, key, residual, combination), weight) in enumerate(
        zip(bad, bezout)
    ):
        print(f"{stage}_incompatibility[{index}]_row_index={row_index}")
        print(f"{stage}_incompatibility[{index}]_key={key}")
        print(f"{stage}_incompatibility[{index}]_degree={residual.degree}")
        print(f"{stage}_incompatibility[{index}]_residual_sha256={digest(residual)}")
        print(f"{stage}_incompatibility[{index}]_source_row_count={len(combination)}")
        print(
            f"{stage}_incompatibility[{index}]_source_certificate_sha256="
            f"{digest(tuple(sorted(combination.items())))}"
        )
        print(f"{stage}_incompatibility[{index}]_bezout_sha256={digest(weight)}")
    print(f"{stage}_compatibility_gcd_degree={gcd.degree}")
    print(f"{stage}_compatibility_gcd_sha256={digest(gcd)}")
    print(f"{stage}_compatibility_bezout_sha256={digest(tuple(bezout))}")
    certificate_values = list(residuals) + list(bezout)
    for _, _, _, combination in bad:
        certificate_values.extend(combination.values())
    if gcd.degree == 0:
        certificate_values.append(gcd.inverse())
    denominator = denominator_lcm_beta(certificate_values)
    print(
        f"{stage}_compatibility_certificate_denominator_summary="
        f"{tri.polynomial_summary(denominator)}"
    )
    print(f"{stage}_compatibility_certificate_denominator_nonzero={str(bool(denominator)).lower()}")
    print(f"{stage}_compatibility_original_row_replay=true")
    print(
        f"{stage}_generic_raw_stratum_empty="
        f"{str(gcd.degree == 0).lower()}"
    )
    print(
        f"{stage}_beta_root_stratum_required="
        f"{str(gcd.degree > 0).lower()}",
        flush=True,
    )
    return True


def transport_beta_incompatibilities(rows, records, compatibility):
    """Lift transport dependencies to exact E3[beta] original-row witnesses."""
    out = []
    expected = []
    for key, base, derivative in compatibility:
        expected.append((key, BetaPoly([b.from_vector(base), b.from_vector(derivative)])))
    for row_index, record in enumerate(records):
        key, kind, _, _, _ = record
        if kind != "dependent":
            continue
        combination, _ = tri.transport_source_combination(records, row_index)
        matrix, _ = tri.replay_transport_combination(rows, combination)
        assert not matrix
        residual = BetaPoly()
        converted = {}
        for source_index, multiplier in combination.items():
            source_key = rows[source_index][0]
            base, derivative = b.source_vector_beta(source_key)
            weight = BetaPoly(b.scalar(multiplier))
            source = BetaPoly([b.from_vector(base), b.from_vector(derivative)])
            residual += weight*source
            converted[source_index] = weight
        if residual:
            out.append((row_index, key, residual, converted))
    assert [(key, residual) for _, key, residual, _ in out] == expected
    if out:
        emit_stage_incompatibilities(out, "transport")
    return bool(out)


def solve_stage(nvariables, rows, stage):
    """Unit-pivot GE over E(C,V,U)[beta], with exact row ancestry."""
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
            print(f"{stage}_nonunit_pivot_degree={lead.degree}")
            print(f"{stage}_nonunit_pivot_sha256={digest(lead)}", flush=True)
            raise AssertionError("beta-dependent pivot: exceptional strata required")
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

    print(f"{stage}_rank={len(pivots)}/{nvariables}")
    print(f"{stage}_dependent_count={len(dependent)}")
    print(f"{stage}_all_pivots_beta_independent=true")
    print(f"{stage}_pivot_digest={digest(tuple((i,k,p,l) for i,k,p,l in factors))}")
    print(f"{stage}_original_row_replay=true", flush=True)
    return pivots, order, factors, dependent


def parameterize(nvariables, rows, stage):
    pivots, order, factors, dependent = solve_stage(nvariables, rows, stage)
    if emit_stage_incompatibilities(dependent, stage):
        return None
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
            assert other > variable and forms[other] is not None, (
                "nontriangular unit schedule", variable, other
            )
            form = nr.add_affine(form, forms[other], -coefficient)
        forms[variable] = form

    for key, row, rhs in rows:
        got = (BetaPoly(), {})
        for variable, coefficient in row.items():
            got = nr.add_affine(got, forms[variable], coefficient)
        assert got == (BetaPoly.coerce(rhs), {}), (stage, key, got, rhs)
    print(f"{stage}_affine_parameterization_replay=true", flush=True)
    return forms, free, factors


def compose(forms, parameter_forms):
    out = []
    for constant, coefficients in forms:
        value = (constant, {})
        for parameter, coefficient in coefficients.items():
            value = nr.add_affine(value, parameter_forms[parameter], coefficient)
        out.append(value)
    return out


def denominator_lcm_beta(polynomials):
    return r.denominator_lcm(
        coefficient
        for polynomial in polynomials
        for coefficient in BetaPoly.coerce(polynomial).coefficients
    )


def e3_coordinate_degrees(value):
    coordinates = tri.e3_rat3_coordinates(E3.coerce(value))
    return [
        (
            coordinate.numerator.total_degree(),
            coordinate.denominator.total_degree(),
        )
        for coordinate in coordinates
    ]


def main():
    print("beta_parameter_name=beta")
    print("target_compatibility=X0_t13")
    print("ring=E(C,V,U)[beta]")
    print("q_beta=t+beta*t^2+t^25")
    print(f"direct_qprime_retained={str(not OMIT_DIRECT_QPRIME).lower()}")
    print(f"raw_center_stratum={STRATUM}")
    print("raw_fraction_field_not_complete_stratum=true", flush=True)

    center_c, center_v, center_u, center_label = tri.center_coordinates()
    print(f"source_center={center_label}")
    if STRATUM == "b3-param":
        tri.audit_b3_parameterization(center_c, center_v, center_u)

    r.fb.CENTER = (center_c, center_v, center_u)
    r.fb._X_POWER_CACHE.clear()
    nf, rows_f = r.fb.build_transport(
        15, 60, 3, {15: r.b.Q(1)},
        r.fb.F1_F_PATTERN, r.fb.POLE_F_PATTERN,
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
    transport_pivots, records, events, _ = tri.factor_transport(ordered)
    pivot_rhs_dual, compatibility = b.propagate_beta(ordered, records)
    print(f"transport_rank={len(transport_pivots)}/{nf+ng}")
    print(f"transport_event_count={len(events)}")
    print("transport_matrix_beta_independent=true")
    print("transport_rhs_beta_affine_exact=true", flush=True)
    if compatibility:
        assert transport_beta_incompatibilities(ordered, records, compatibility)
        print("raw_stratum_resolved_only_over_emitted_fraction_field=true")
        print("full_A3_beta_family_killed=false")
        print("whole_TD6_killed=false")
        print("SP2_killed=false")
        print("JC2_resolved=false")
        print("TD6-A3-Q2-N13-RAW-TRANSPORT PASS")
        return
    free = [
        variable for variable in range(nf + ng)
        if variable not in transport_pivots
    ]
    free_parameter = {variable: index for index, variable in enumerate(free)}
    print(f"transport_free_count={len(free)}")

    def restrict(row):
        return convert_form(b.restrict_row_beta(
            row, transport_pivots, pivot_rhs_dual, free_parameter
        ))

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
        row = {
            variable: Rat3.coerce(coefficient)
            for variable, coefficient in nr.pole_coefficient(
                15, 60, -2, degree
            ).items()
        }
        pole_f132.append(restrict(row))
    pole_g132 = []
    for degree in range(101):
        row = {
            nf + variable: Rat3.coerce(coefficient)
            for variable, coefficient in nr.pole_coefficient(
                25, 100, -4, degree
            ).items()
        }
        pole_g132.append(restrict(row))
    print("transport_x_and_pole_sections_exact=true", flush=True)

    configure_qd(direct_qprime=not OMIT_DIRECT_QPRIME)
    first_rows = qd.pack(
        'X-2', qd.first_band_polynomials(
            bands132[('f', 1)], bands132[('g', 1)]
        )
    )
    first_result = parameterize(len(free), first_rows, "first")
    if first_result is None:
        print("full_A3_beta_family_killed=false")
        print("whole_TD6_killed=false")
        print("SP2_killed=false")
        print("JC2_resolved=false")
        print("TD6-A3-Q2-N13-RAW-FIRST PASS")
        return
    forms94, free94, factors_first = first_result

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
    previous_result = parameterize(
        len(free94), previous_rows, "previous_pole"
    )
    if previous_result is None:
        print("full_A3_beta_family_killed=false")
        print("whole_TD6_killed=false")
        print("SP2_killed=false")
        print("JC2_resolved=false")
        print("TD6-A3-Q2-N13-RAW-PREVIOUS PASS")
        return
    forms56, free56, factors_previous = previous_result

    bands56 = {key: compose(forms, forms56) for key, forms in bands94.items()}
    current_polynomials = qd.compile_current(
        *[bands56[('f', exponent)] for exponent in (1, 2, 3)],
        *[bands56[('g', exponent)] for exponent in (1, 2, 3)],
    )
    current_rows = qd.pack('X0', current_polynomials)
    current_pivots, _, factors_current, current_dependent = solve_stage(
        len(free56), current_rows, "current"
    )
    compatibilities = [
        (row_index, key, rhs, combination)
        for row_index, key, rhs, combination in current_dependent if rhs
    ]
    print(f"current_compatibility_count={len(compatibilities)}")
    print("current_compatibility_original_row_replay=true")
    for index, (row_index, key, residual, combination) in enumerate(compatibilities):
        print(f"compatibility[{index}]_row_index={row_index}")
        print(f"compatibility[{index}]_key={key}")
        print(f"compatibility[{index}]_degree={residual.degree}")
        print(f"compatibility[{index}]_support={len(combination)}")
        print(f"compatibility[{index}]_weight_degree={max((w.degree for w in combination.values()), default=-1)}")
        print(f"compatibility[{index}]_sha256={digest(residual)}")
        print(f"compatibility[{index}]_left_null_sha256={digest(tuple(sorted(combination.items())))}")
    print("current_all_compatibilities_emitted=true", flush=True)

    n13_records = [record for record in compatibilities if record[1] == ('X0', 13)]
    print(f"N13_record_count={len(n13_records)}")
    S = E3(qd.uniform.S_FIELD)
    k = E3(252) - 342*S + 144*S**2 - 36*S**3
    expected = BetaPoly([0, k/25])
    if len(n13_records) == 1:
        _, _, n13, n13_combination = n13_records[0]
        print(f"N13_degree={n13.degree}")
        print(f"N13_sha256={digest(n13)}")
        print(f"N13_expected_sha256={digest(expected)}")
        print(f"N13_equals_reviewed_k_beta_over_25={str(n13 == expected).lower()}")
        print(f"N13_equals_negative_reviewed_value={str(n13 == -expected).lower()}")
        print(f"N13_constant_zero={str(not n13.constant).lower()}")
        print(f"N13_beta_coefficient_sha256={digest(n13.coefficient(1))}")
        print(f"N13_beta_coefficient_coordinate_degrees={e3_coordinate_degrees(n13.coefficient(1))}")
        print(f"N13_left_null_beta_weight_count={sum(w.degree > 0 for w in n13_combination.values())}")
    else:
        n13, n13_combination = BetaPoly(), {}

    if compatibilities:
        emit_stage_incompatibilities(current_dependent, "current")

    stage_values = []
    for factors in (factors_first, factors_previous, factors_current):
        stage_values.extend(lead for _, _, _, lead in factors)
    stage_values.extend(n13_combination.values())
    if n13:
        stage_values.append(n13)
    denominator = denominator_lcm_beta(stage_values)
    print(f"N13_full_stage_denominator_summary={tri.polynomial_summary(denominator)}")
    print(f"N13_full_stage_denominator_nonzero={str(bool(denominator)).lower()}")
    print("fixed_center_reviewed_positive_control=N13=(k/25)*beta")
    print(f"direct_qprime_omission_control={str(OMIT_DIRECT_QPRIME).lower()}")
    print(f"raw_stratum={STRATUM}")
    print("raw_substrata_from_emitted_denominators_still_charged=true")
    print("full_A3_beta_family_killed=false")
    print("whole_TD6_killed=false")
    print("SP2_killed=false")
    print("JC2_resolved=false")
    if OMIT_DIRECT_QPRIME:
        print("N13_compact_reporter=true")
        print("TD6-A3-Q2-N13-RAW-OMISSION-CONTROL PASS")
    else:
        print("N13_compact_reporter=true")
        print("TD6-A3-Q2-N13-RAW PASS")


if __name__ == "__main__":
    main()
