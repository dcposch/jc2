#!/usr/bin/env python3
"""Untruncated exact E[B] replay of the licensed TD6 q_B pencil.

The fixed B=0 pivot schedule is accepted only when every normalized pivot
factor is a nonzero element of E (degree zero in B).  Hence every output
degree is structural, not inferred from interpolation.
"""

from hashlib import sha256
import json

import transport_cache as tc


E, K, Q, nr, fb, qd = tc.E, tc.K, tc.Q, tc.nr, tc.fb, tc.qd


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
        if not self.coefficients:
            return E(0)
        return self.coefficients[-1]

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
        return Poly([-value for value in self.coefficients])

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

    def inverse(self):
        assert self.degree == 0, (
            "nonconstant normalized pivot; exceptional stratum required",
            self.degree,
        )
        return Poly(self.constant.inverse())

    def __truediv__(self, other):
        return self * Poly.coerce(other).inverse()

    def __rtruediv__(self, other):
        return Poly.coerce(other) / self

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
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
        try:
            other = Poly.coerce(other)
        except (TypeError, ValueError):
            return False
        return self.coefficients == other.coefficients

    def __repr__(self):
        return "Poly(" + ",".join(map(repr, self.coefficients)) + ")"


B = Poly([0, 1])


def lift_forms(forms):
    return [
        (
            Poly([base, linear]),
            {parameter: Poly(coefficient) for parameter, coefficient in coefficients.items()},
        )
        for base, linear, coefficients in forms
    ]


def configure():
    qd.Dual = Poly
    qd.B = B
    qd.S = Poly(E(qd.uniform.S_FIELD))
    qd.D = Poly(E(qd.uniform.D_FIELD))
    qd.L = Poly(E(qd.uniform.L_FIELD))
    qd.A = Poly(qd.uniform.A_FIELD)
    qd.Q_PRIME = {0: Poly(1), 1: 2 * B, 24: Poly(25)}
    qd.R = qd.multiply(
        qd.multiply([Poly(-1), Poly(1)], [Poly(-1), Poly(1)]),
        [qd.D, -qd.S, Poly(1)],
    )
    qd.R3, qd.R5 = qd.power(qd.R, 3), qd.power(qd.R, 5)
    qd.POLE_F = {1: -(qd.L**3) * qd.A, 6: qd.L**3}
    qd.POLE_G = {
        0: Poly(Q(5, 9)) * qd.L**5 * qd.A**2,
        5: Poly(Q(-5, 3)) * qd.L**5 * qd.A,
        10: qd.L**5,
    }


def row_degree_stats(rows):
    entry_degrees = [value.degree for _, row, _ in rows for value in row.values()]
    rhs_degrees = [Poly.coerce(rhs).degree for _, _, rhs in rows]
    return {
        "entry_max": max(entry_degrees, default=-1),
        "rhs_max": max(rhs_degrees, default=-1),
    }


def form_degree_stats(forms):
    constants = [constant.degree for constant, _ in forms]
    directions = [value.degree for _, row in forms for value in row.values()]
    return {
        "constant_max": max(constants, default=-1),
        "direction_max": max(directions, default=-1),
    }


def solve(nvariables, rows):
    """Exact normalized elimination on the B=0 rank stratum.

    Every accepted lead must simplify to degree zero.  Polynomial-only
    coefficients with zero B=0 value are not leads; they remain source terms
    against the frozen section, exactly as in the certified dual replay.
    """
    pivots = {}
    order = []
    factors = []
    dependent = []
    for row_index, (key, original_row, original_rhs) in enumerate(rows):
        row = {
            variable: Poly.coerce(value)
            for variable, value in original_row.items()
            if Poly.coerce(value)
        }
        rhs = Poly.coerce(original_rhs)
        combination = {row_index: Poly(1)}
        while True:
            reducible = sorted(variable for variable in row if variable in pivots)
            if not reducible:
                break
            pivot = reducible[0]
            factor = row[pivot]
            old_row, old_rhs, old_combination = pivots[pivot]
            for variable, coefficient in old_row.items():
                value = row.get(variable, Poly()) - factor * coefficient
                if value:
                    row[variable] = value
                else:
                    row.pop(variable, None)
            rhs -= factor * old_rhs
            for old_index, coefficient in old_combination.items():
                value = combination.get(old_index, Poly()) - factor * coefficient
                if value:
                    combination[old_index] = value
                else:
                    combination.pop(old_index, None)
        base_variables = sorted(
            variable for variable, coefficient in row.items() if coefficient.constant
        )
        if not base_variables:
            dependent.append((row_index, key, row, rhs, combination))
            continue
        pivot = base_variables[0]
        lead = row[pivot]
        assert lead.degree == 0, ("nonconstant pivot factor", key, pivot, lead)
        normalized_row = {
            variable: coefficient / lead for variable, coefficient in row.items()
        }
        normalized_rhs = rhs / lead
        normalized_combination = {
            old_index: coefficient / lead
            for old_index, coefficient in combination.items()
        }
        pivots[pivot] = (normalized_row, normalized_rhs, normalized_combination)
        order.append(pivot)
        factors.append((row_index, key, pivot, lead.constant))
    return pivots, order, factors, dependent


def parameterize(nvariables, rows):
    pivots, order, factors, dependent = solve(nvariables, rows)
    assert all(not row and not rhs for _, _, row, rhs, _ in dependent), [
        (key, row, rhs) for _, key, row, rhs, _ in dependent if row or rhs
    ]
    free = [variable for variable in range(nvariables) if variable not in pivots]
    parameter_of = {variable: index for index, variable in enumerate(free)}
    forms = [None] * nvariables
    for variable in free:
        forms[variable] = (Poly(), {parameter_of[variable]: Poly(1)})
    for variable in reversed(order):
        row, rhs, _ = pivots[variable]
        form = (rhs, {})
        for other, coefficient in row.items():
            if other == variable:
                continue
            assert forms[other] is not None, ("nontriangular pivot schedule", variable, other)
            form = nr.add_affine(form, forms[other], -coefficient)
        forms[variable] = form
    for key, row, rhs in rows:
        got = (Poly(), {})
        for variable, coefficient in row.items():
            got = nr.add_affine(got, forms[variable], coefficient)
        assert got == (Poly.coerce(rhs), {}), ("symbolic row replay", key, got, rhs)
    return forms, free, factors


def compose(forms, parameter_forms):
    out = []
    for constant, coefficients in forms:
        value = (constant, {})
        for parameter, coefficient in coefficients.items():
            value = nr.add_affine(value, parameter_forms[parameter], coefficient)
        out.append(value)
    return out


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
        term = Poly([E(0)] * degree + [coefficient])
        remainder -= term * divisor
    return Poly(quotient), remainder


def poly_monic(poly):
    poly = Poly(poly)
    return poly * poly.leading.inverse() if poly else poly


def poly_gcd(left, right):
    left, right = Poly(left), Poly(right)
    while right:
        _, remainder = poly_divmod(left, right)
        left, right = right, remainder
    return poly_monic(left)


def poly_xgcd(left, right):
    old_r, r = Poly(left), Poly(right)
    old_s, s = Poly(1), Poly()
    old_t, t = Poly(), Poly(1)
    while r:
        quotient, remainder = poly_divmod(old_r, r)
        old_r, r = r, remainder
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    lead_inverse = old_r.leading.inverse()
    return old_r * lead_inverse, old_s * lead_inverse, old_t * lead_inverse


def e_text(value):
    return qd.uniform.extension_text(value)


def poly_record(poly):
    poly = Poly(poly)
    return {
        "degree": poly.degree,
        "coefficients": [e_text(value) for value in poly.coefficients],
        "sha256": sha256(repr(poly).encode()).hexdigest(),
    }


def factor_record(stage, factors):
    return [
        {
            "stage": stage,
            "row_index": row_index,
            "key": list(key),
            "pivot": pivot,
            "factor": e_text(factor),
            "factor_sha256": sha256(repr(factor).encode()).hexdigest(),
        }
        for row_index, key, pivot, factor in factors
    ]


def certificate_digest(combination, residual):
    digest = sha256()
    for row_index, weight in sorted(combination.items()):
        digest.update(f"row{row_index}:{weight!r}\n".encode())
    digest.update(f"residual:{residual!r}\n".encode())
    return digest.hexdigest()


def replay_certificate(rows, combination, residual):
    check_row = {}
    check_rhs = Poly()
    for row_index, weight in combination.items():
        _, row, rhs = rows[row_index]
        for variable, coefficient in row.items():
            value = check_row.get(variable, Poly()) + weight * coefficient
            if value:
                check_row[variable] = value
            else:
                check_row.pop(variable, None)
        check_rhs += weight * rhs
    assert not check_row and check_rhs == residual


def main():
    configure()
    fb.CENTER = (Q(1), Q(1), Q(1))
    fb._X_POWER_CACHE.clear()
    sections, cache_sha256 = tc.load_cache()
    bands132 = {
        (owner, exponent): lift_forms(sections[f"{owner}{exponent}"])
        for owner in ("f", "g")
        for exponent in (1, 2, 3)
    }
    pole_f132 = lift_forms(sections["pole_f1"])
    pole_g132 = lift_forms(sections["pole_g1"])

    first_rows = qd.pack(
        "X-2", qd.first_band_polynomials(bands132[("f", 1)], bands132[("g", 1)])
    )
    forms94, free94, factors_first = parameterize(132, first_rows)
    assert (len(factors_first), len(free94)) == (38, 94)
    print("first symbolic PASS", flush=True)

    bands94 = {key: compose(forms, forms94) for key, forms in bands132.items()}
    f1, f2 = bands94[("f", 1)], bands94[("f", 2)]
    g1, g2 = bands94[("g", 1)], bands94[("g", 2)]
    previous_rows = qd.pack("X-1", qd.compile_previous(f1, f2, g1, g2))
    previous_rows += qd.pack(
        "P1",
        qd.compile_pole_previous(
            compose(pole_f132, forms94), compose(pole_g132, forms94)
        ),
    )
    forms56, free56, factors_previous = parameterize(94, previous_rows)
    assert (len(factors_previous), len(free56)) == (38, 56)
    print("previous/pole symbolic PASS", flush=True)

    bands56 = {key: compose(forms, forms56) for key, forms in bands94.items()}
    current_rows = qd.pack(
        "X0",
        qd.compile_current(
            *[bands56[("f", exponent)] for exponent in (1, 2, 3)],
            *[bands56[("g", exponent)] for exponent in (1, 2, 3)],
        ),
    )
    current_pivots, current_order, factors_current, current_dependent = solve(
        56, current_rows
    )
    assert len(factors_current) == 25
    compatibility = [
        (row_index, key, rhs, combination)
        for row_index, key, row, rhs, combination in current_dependent
        if rhs
    ]
    assert all(not row for _, _, row, _, _ in current_dependent)
    assert compatibility and compatibility[0][1] == ("X0", 4)
    assert [key for _, key, _, _ in compatibility] == [
        ("X0", degree) for degree in range(4, 14)
    ]
    for _, _, residual, combination in compatibility:
        replay_certificate(current_rows, combination, residual)
    gcd = compatibility[0][2]
    for _, _, numerator, _ in compatibility[1:]:
        gcd = poly_gcd(gcd, numerator)
    gcd = poly_monic(gcd)

    # The clean certificate uses N13=k*B and N4=c0+B*h.  It is both much
    # smaller and more informative than a generic extended-gcd output.
    row4, numerator4 = compatibility[0][1], compatibility[0][2]
    row13, numerator13 = next(
        (key, numerator)
        for _, key, numerator, _ in compatibility
        if key == ("X0", 13)
    )
    assert numerator13.degree == 1 and not numerator13.constant
    k13 = numerator13.coefficients[1]
    c0 = numerator4.constant
    assert k13 and c0
    expected_c0 = E([
        K([
            Q(2495634, 3625), Q(-4154976, 3625), Q(4405068, 3625),
            Q(-2488119, 3625), Q(761922, 3625), Q(-105084, 3625),
        ]),
        K(Q(136875, 29)),
    ])
    expected_t4 = Poly([
        expected_c0,
        E(Q(-4720, 29)),
        E(Q(11364, 145)),
        E(Q(-4096, 145)),
        E(Q(16)),
    ])
    expected_k13 = E(K([
        Q(252, 25), Q(-342, 25), Q(144, 25), Q(-36, 25)
    ]))
    k_numerator = K([Q(252), Q(-342), Q(144), Q(-36)])
    k_numerator_inverse = K([
        Q(66812, 526875),
        Q(-4948, 21075),
        Q(40993, 210750),
        Q(-9181, 105375),
        Q(738, 35125),
        Q(-388, 175625),
    ])
    assert k_numerator * k_numerator_inverse == K(1)
    assert numerator4 == expected_t4
    assert k13 == expected_k13
    assert k13.inverse() == E(25 * k_numerator_inverse)
    assert sum(numerator4.coefficients, E(0)) - c0 == E(Q(-14012, 145))
    h4, remainder4 = poly_divmod(numerator4 - Poly(c0), B)
    assert not remainder4
    left = Poly(c0.inverse())
    right = -h4 * (c0 * k13).inverse()
    assert left * numerator4 + right * numerator13 == Poly(1)
    bezout = {
        "left_row": list(row4),
        "right_row": list(row13),
        "left_multiplier": poly_record(left),
        "right_multiplier": poly_record(right),
        "identity_sha256": sha256(
            repr((left, numerator4, right, numerator13, Poly(1))).encode()
        ).hexdigest(),
    }

    factors = (
        factor_record("first", factors_first)
        + factor_record("previous_pole", factors_previous)
        + factor_record("current", factors_current)
    )
    output = {
        "verdict": "EXACT-E[B]-STAGED-REPLAY-PASS",
        "transport_cache_sha256": cache_sha256,
        "ranks": {
            "transport": [3470, 3602],
            "first": [len(factors_first), 132],
            "previous_pole": [len(factors_previous), 94],
            "current_homogeneous": [len(factors_current), 56],
        },
        "degree_stats": {
            "transport_bands": form_degree_stats(
                [form for forms in bands132.values() for form in forms]
            ),
            "first_rows": row_degree_stats(first_rows),
            "forms94": form_degree_stats(forms94),
            "previous_rows": row_degree_stats(previous_rows),
            "forms56": form_degree_stats(forms56),
            "current_rows": row_degree_stats(current_rows),
        },
        "pivot_count": len(factors),
        "pivot_factors": factors,
        "pivot_exceptional_polynomial": poly_record(Poly(1)),
        "compatibility": [
            {
                "row_index": row_index,
                "key": list(key),
                "numerator": poly_record(numerator),
                "left_null_support": len(combination),
                "left_null_max_degree": max(
                    (weight.degree for weight in combination.values()), default=-1
                ),
                "left_null_sha256": certificate_digest(combination, numerator),
            }
            for row_index, key, numerator, combination in compatibility
        ],
        "compatibility_gcd": poly_record(gcd),
        "t13_coefficient_inverse": {
            "coefficient": e_text(k13),
            "inverse": e_text(k13.inverse()),
            "product": e_text(k13 * k13.inverse()),
            "inverse_sha256": sha256(repr(k13.inverse()).encode()).hexdigest(),
        },
        "unit_bezout": bezout,
    }
    print(json.dumps(output, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
