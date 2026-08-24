#!/usr/bin/env python3
"""Exact compiler for the third paired TD6 Jacobian band (2026-08-24).

Coefficient field: K=Q(S), 10*S^2-35*S+37=0.
Frozen moduli: C=1, D=S-22/25, L=3, A=1/9, center=(1,1,1).

Previously imposed bands are [s^-2]J=0, [s^-1]J=0 and
[r^0]J=1, [r^1](J-1)=0.  This replay compiles exactly the next pair
[s^0]J=1 and [r^2](J-1)=0.
"""

from fractions import Fraction as Q
from hashlib import sha256
import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
MODULI_REPLAY = HERE.parent / "td6_moduli_uniformity_20260824" / "replay.py"
MODULI_REPLAY_SHA256 = (
    "55340fa662a20e1777eaa18fae2d26589c11ec7f3f2960f4a0a6efe015e7b6ab"
)
assert sha256(MODULI_REPLAY.read_bytes()).hexdigest() == MODULI_REPLAY_SHA256

spec = importlib.util.spec_from_file_location("td6_moduli", MODULI_REPLAY)
mu = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mu)
nr = mu.nr


class K:
    """The exact quadratic field Q[S]/(10*S^2-35*S+37)."""

    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        if isinstance(a, K):
            assert b == 0
            self.a, self.b = a.a, a.b
        else:
            self.a, self.b = Q(a), Q(b)

    @staticmethod
    def coerce(value):
        return value if isinstance(value, K) else K(value)

    def __add__(self, other):
        other = K.coerce(other)
        return K(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return K(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-K.coerce(other))

    def __rsub__(self, other):
        return K.coerce(other) - self

    def __mul__(self, other):
        other = K.coerce(other)
        # S^2=(7/2)S-37/10.
        return K(
            self.a * other.a - Q(37, 10) * self.b * other.b,
            self.a * other.b
            + self.b * other.a
            + Q(7, 2) * self.b * other.b,
        )

    __rmul__ = __mul__

    def inverse(self):
        # The conjugate of S is 7/2-S and S*Sbar=37/10.
        norm = (
            self.a * self.a
            + Q(7, 2) * self.a * self.b
            + Q(37, 10) * self.b * self.b
        )
        if not norm:
            raise ZeroDivisionError
        return K((self.a + Q(7, 2) * self.b) / norm, -self.b / norm)

    def __truediv__(self, other):
        return self * K.coerce(other).inverse()

    def __rtruediv__(self, other):
        return K.coerce(other) * self.inverse()

    def __pow__(self, exponent):
        if exponent < 0:
            return (self.inverse()) ** (-exponent)
        out = K(1)
        base = self
        while exponent:
            if exponent & 1:
                out = out * base
            base = base * base
            exponent //= 2
        return out

    def __bool__(self):
        return bool(self.a or self.b)

    def __eq__(self, other):
        try:
            other = K.coerce(other)
        except (TypeError, ValueError):
            return False
        return self.a == other.a and self.b == other.b

    def __hash__(self):
        return hash((self.a, self.b))

    def __repr__(self):
        return f"K({self.a!r},{self.b!r})"


S = K(0, 1)
D = S - Q(22, 25)
assert 10 * S**2 - 35 * S + 37 == 0
assert 1 - S + D == Q(3, 25)
assert 3**8 * Q(1, 9) ** 3 == 9


def univar_multiply(left, right):
    out = [K(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def univar_power(poly, exponent):
    out = [K(1)]
    for _ in range(exponent):
        out = univar_multiply(out, poly)
    return out


def fifth_factor(value):
    return [-K.coerce(value)] + [K(0)] * 4 + [K(1)]


R_ETA = univar_multiply(
    univar_multiply(fifth_factor(1), fifth_factor(1)),
    # (z-U)(z-V)=z^2-Sz+D in z=eta^5.
    [D] + [K(0)] * 4 + [-S] + [K(0)] * 4 + [K(1)],
)
F1_F_PATTERN = univar_power(R_ETA, 3)
F1_G_PATTERN = univar_power(R_ETA, 5)


def replace_f1_rhs(base_rows):
    out = []
    for key, row, rhs in base_rows:
        new_rhs = K(rhs)
        if key[0] in ("f", "g") and key[1] == "F1":
            owner, _, exponent, eta_degree = key
            leading_exponent = -15 if owner == "f" else -25
            if exponent == leading_exponent:
                pattern = F1_F_PATTERN if owner == "f" else F1_G_PATTERN
                new_rhs = (
                    pattern[eta_degree]
                    if eta_degree < len(pattern)
                    else K(0)
                )
        out.append((key, row, new_rhs))
    return out


def affine_parameterization(nvariables, rows):
    particular, pivots, _ = nr.fb.exact_solve(nvariables, rows)
    free = [variable for variable in range(nvariables) if variable not in pivots]
    parameter_of = {variable: index for index, variable in enumerate(free)}
    forms = [None] * nvariables
    for variable in range(nvariables - 1, -1, -1):
        if variable in parameter_of:
            forms[variable] = (K(0), {parameter_of[variable]: K(1)})
            continue
        row, rhs = pivots[variable]
        form = (K(rhs), {})
        for other, coefficient in row.items():
            if other != variable:
                form = nr.add_affine(form, forms[other], -coefficient)
        forms[variable] = form

    for key, row, rhs in rows:
        got = (K(0), {})
        for variable, coefficient in row.items():
            got = nr.add_affine(got, forms[variable], coefficient)
        assert got == (K(rhs), {}), ("affine replay", key, got, rhs)
    for variable, form in enumerate(forms):
        assert form[0] == particular.get(variable, K(0))
    return forms, free, pivots


def linear_rows_from_parameter_polynomials(family, rows, targets=None):
    targets = targets or {}
    packed = []
    for degree, polynomial in enumerate(rows):
        coefficients = {}
        constant = K(0)
        for monomial, coefficient in polynomial.items():
            if not monomial:
                constant += coefficient
            elif len(monomial) == 1:
                coefficients[monomial[0]] = (
                    coefficients.get(monomial[0], K(0)) + coefficient
                )
            else:
                raise AssertionError(("nonlinear row", family, degree, monomial))
        rhs = K(targets.get(degree, 0)) - constant
        if coefficients or rhs:
            packed.append(((family, degree), coefficients, rhs))
    return packed


def substitute_affine(form, parameter_forms):
    out = (K(form[0]), {})
    for parameter, coefficient in form[1].items():
        out = nr.add_affine(out, parameter_forms[parameter], coefficient)
    return out


def compose_forms(forms, parameter_forms):
    return [substitute_affine(form, parameter_forms) for form in forms]


def add_equation_term(equation, term, scale=K(1)):
    return nr.add_polynomial(equation, term, scale)


def compile_x_constant_band(f1, f2, f3, g1, g2, g3):
    """Compile [s^0]J, i.e. the s^2 local-wedge coefficient."""
    rows = []
    for degree in range(40):
        equation = {}

        # f1*g2'
        for i, left in enumerate(f1):
            j = degree - i + 1
            if 1 <= j < len(g2):
                equation = add_equation_term(
                    equation,
                    nr.multiply_affine(left, nr.scale_affine(g2[j], K(j))),
                )
        # 2*f2*g1'
        for i, left in enumerate(f2):
            j = degree - i + 1
            if 1 <= j < len(g1):
                equation = add_equation_term(
                    equation,
                    nr.multiply_affine(left, nr.scale_affine(g1[j], K(j))),
                    K(2),
                )
        # 3*f3*q', q'=1+25*t^24
        for i, form in enumerate(f3):
            if degree - i == 0:
                equation = add_equation_term(
                    equation, nr.affine_polynomial(form), K(3)
                )
            if degree - i == 24:
                equation = add_equation_term(
                    equation, nr.affine_polynomial(form), K(75)
                )
        # -3*p'*g3, p'=15*t^14
        j = degree - 14
        if 0 <= j < len(g3):
            equation = add_equation_term(
                equation, nr.affine_polynomial(g3[j]), K(-45)
            )
        # -2*f1'*g2
        for i in range(1, len(f1)):
            j = degree - (i - 1)
            if 0 <= j < len(g2):
                equation = add_equation_term(
                    equation,
                    nr.multiply_affine(nr.scale_affine(f1[i], K(i)), g2[j]),
                    K(-2),
                )
        # -f2'*g1
        for i in range(1, len(f2)):
            j = degree - (i - 1)
            if 0 <= j < len(g1):
                equation = add_equation_term(
                    equation,
                    nr.multiply_affine(nr.scale_affine(f2[i], K(i)), g1[j]),
                    K(-1),
                )
        # Exact J=1 requires this band to be the constant polynomial one.
        if degree == 0:
            equation = add_equation_term(equation, {(): K(1)}, K(-1))
        rows.append(equation)
    return rows


def compile_pole_second_band(p1, p2, q1, q2):
    """Compile the actual [r^2](J-1) coefficient, including /(-25)."""
    p = [(K(c), {}) for c in nr.fb.POLE_F_PATTERN]
    q = [(K(c), {}) for c in nr.fb.POLE_G_PATTERN]
    max_degree = 40
    rows = []
    for degree in range(max_degree):
        equation = {}
        # -3*p*q2'
        for i, left in enumerate(p):
            j = degree - i + 1
            if 1 <= j < len(q2):
                equation = add_equation_term(
                    equation,
                    nr.multiply_affine(left, nr.scale_affine(q2[j], K(j))),
                    K(-3),
                )
        # -2*p1*q1'
        for i, left in enumerate(p1):
            j = degree - i + 1
            if 1 <= j < len(q1):
                equation = add_equation_term(
                    equation,
                    nr.multiply_affine(left, nr.scale_affine(q1[j], K(j))),
                    K(-2),
                )
        # -p2*q'
        for i, left in enumerate(p2):
            j = degree - i + 1
            if 1 <= j < len(q):
                equation = add_equation_term(
                    equation,
                    nr.multiply_affine(left, nr.scale_affine(q[j], K(j))),
                    K(-1),
                )
        # +3*p'*q2
        for i in range(1, len(p)):
            j = degree - (i - 1)
            if 0 <= j < len(q2):
                equation = add_equation_term(
                    equation,
                    nr.multiply_affine(nr.scale_affine(p[i], K(i)), q2[j]),
                    K(3),
                )
        # +4*p1'*q1
        for i in range(1, len(p1)):
            j = degree - (i - 1)
            if 0 <= j < len(q1):
                equation = add_equation_term(
                    equation,
                    nr.multiply_affine(nr.scale_affine(p1[i], K(i)), q1[j]),
                    K(4),
                )
        # +5*p2'*q
        for i in range(1, len(p2)):
            j = degree - (i - 1)
            if 0 <= j < len(q):
                equation = add_equation_term(
                    equation,
                    nr.multiply_affine(nr.scale_affine(p2[i], K(i)), q[j]),
                    K(5),
                )
        rows.append(nr.scale_polynomial(equation, K(Q(-1, 25))))
    return rows


def field_text(value):
    value = K.coerce(value)
    return (
        f"({value.a.numerator}/{value.a.denominator})"
        f"+({value.b.numerator}/{value.b.denominator})*S"
    )


def equations_digest(x_rows, pole_rows):
    digest = sha256()
    for family, rows in (("X", x_rows), ("P", pole_rows)):
        for degree, row in enumerate(rows):
            digest.update(f"{family},{degree}".encode())
            for monomial, coefficient in sorted(row.items()):
                name = "1" if not monomial else "*".join(
                    f"u{parameter}" for parameter in monomial
                )
                digest.update(
                    f";{name}:{field_text(coefficient)}".encode()
                )
            digest.update(b"\n")
    return digest.hexdigest()


def main():
    nr.fb.CENTER = (Q(1), Q(1), Q(1))
    nr.fb._X_POWER_CACHE.clear()
    nf, ng, _, _, rational_base_rows = nr.build_first_band_system()
    base_rows = replace_f1_rhs(rational_base_rows)
    global_forms_94, free_94, base_pivots = affine_parameterization(
        nf + ng, base_rows
    )
    assert len(base_pivots) == 3508 and len(free_94) == 94

    # Compile and solve the two already-frozen next rows at the algebraic
    # moduli-zero point.
    f1 = nr.x_band_forms(15, 60, 1, global_forms_94, 0)
    f2 = nr.x_band_forms(15, 60, 2, global_forms_94, 0)
    g1 = nr.x_band_forms(25, 100, 1, global_forms_94, nf)
    g2 = nr.x_band_forms(25, 100, 2, global_forms_94, nf)
    x_previous = nr.compile_x_next_rows(f1, f2, g1, g2)

    p1 = [
        nr.combine_global_linear(
            nr.pole_coefficient(15, 60, -2, degree), global_forms_94, 0
        )
        for degree in range(61)
    ]
    q1 = [
        nr.combine_global_linear(
            nr.pole_coefficient(25, 100, -4, degree), global_forms_94, nf
        )
        for degree in range(101)
    ]
    pole_previous = nr.compile_pole_next_rows(p1, q1)
    previous_rows = linear_rows_from_parameter_polynomials("X-1", x_previous)
    previous_rows += linear_rows_from_parameter_polynomials(
        "P1", pole_previous
    )
    parameter_forms_56, free_56, previous_pivots = affine_parameterization(
        94, previous_rows
    )
    assert len(previous_pivots) == 38 and len(free_56) == 56

    global_forms_56 = compose_forms(global_forms_94, parameter_forms_56)

    # Next centered band [s^0]J=1.
    f1 = nr.x_band_forms(15, 60, 1, global_forms_56, 0)
    f2 = nr.x_band_forms(15, 60, 2, global_forms_56, 0)
    f3 = nr.x_band_forms(15, 60, 3, global_forms_56, 0)
    g1 = nr.x_band_forms(25, 100, 1, global_forms_56, nf)
    g2 = nr.x_band_forms(25, 100, 2, global_forms_56, nf)
    g3 = nr.x_band_forms(25, 100, 3, global_forms_56, nf)
    x_current = compile_x_constant_band(f1, f2, f3, g1, g2, g3)
    assert nr.parameter_degree(x_current) == 1
    assert sum(bool(row) for row in x_current) == 35
    x_tangent = nr.tangent_rows(x_current)
    x_tangent_rank = nr.exact_rank(x_tangent, 56)

    # Next pole band [r^2](J-1)=0.
    p1 = [
        nr.combine_global_linear(
            nr.pole_coefficient(15, 60, -2, degree), global_forms_56, 0
        )
        for degree in range(61)
    ]
    p2 = [
        nr.combine_global_linear(
            nr.pole_coefficient(15, 60, -1, degree), global_forms_56, 0
        )
        for degree in range(61)
    ]
    q1 = [
        nr.combine_global_linear(
            nr.pole_coefficient(25, 100, -4, degree), global_forms_56, nf
        )
        for degree in range(101)
    ]
    q2 = [
        nr.combine_global_linear(
            nr.pole_coefficient(25, 100, -3, degree), global_forms_56, nf
        )
        for degree in range(101)
    ]
    assert [i for i, value in enumerate(p1) if value != (K(0), {})] == [4]
    assert [i for i, value in enumerate(p2) if value != (K(0), {})] == [2]
    assert [i for i, value in enumerate(q1) if value != (K(0), {})] == [3, 8]
    assert [i for i, value in enumerate(q2) if value != (K(0), {})] == [1, 6]
    pole_current = compile_pole_second_band(p1, p2, q1, q2)
    assert nr.parameter_degree(pole_current) == 2
    assert [degree for degree, row in enumerate(pole_current) if row] == [1, 6]
    pole_tangent = nr.tangent_rows(pole_current)
    pole_tangent_rank = nr.exact_rank(pole_tangent, 56)
    combined_tangent_rank = nr.exact_rank(x_tangent + pole_tangent, 56)
    quadratic_monomials = sum(
        len(monomial) == 2
        for row in pole_current
        for monomial in row
    )

    # First attempt the exact affine x band; its outcome determines whether a
    # nonlinear pole solve is even relevant.
    x_rows = linear_rows_from_parameter_polynomials("X0", x_current)
    x_solution, x_pivots, x_error = nr.fb.exact_solve(
        56, x_rows, allow_inconsistent=True
    )

    obstruction = K(Q(-15544, 15625))
    forced_constant = K(Q(81, 15625))
    assert x_current[0] == {(): obstruction}
    assert forced_constant - 1 == obstruction
    assert x_error == (("X0", 0), -obstruction)

    # Independent global differentiation at the deterministic origin of the
    # 56-dimensional survivor.  This uses neither jet compiler above.
    particular = {
        variable: form[0]
        for variable, form in enumerate(global_forms_56)
        if form[0]
    }
    f = nr.fb.polynomial_from_solution(particular, 0, 15, 60)
    g = nr.fb.polynomial_from_solution(particular, nf, 25, 100)
    jacobian = nr.fb.poly_sub(
        nr.fb.poly_mul(nr.fb.poly_deriv(f, 0), nr.fb.poly_deriv(g, 1)),
        nr.fb.poly_mul(nr.fb.poly_deriv(f, 1), nr.fb.poly_deriv(g, 0)),
    )
    direct_x = nr.fb.x_chart_expand(jacobian, 0)
    assert not nr.fb.band(direct_x, -2)
    assert not nr.fb.band(direct_x, -1)
    direct_x_zero = nr.fb.band(direct_x, 0)
    expected_x_zero = {
        degree: row.get((), K(0)) + (K(1) if degree == 0 else K(0))
        for degree, row in enumerate(x_current)
        if row.get((), K(0)) + (K(1) if degree == 0 else K(0))
    }
    assert direct_x_zero == expected_x_zero
    assert direct_x_zero[0] == forced_constant

    direct_pole = nr.fb.pole_chart_expand(jacobian, 2)
    assert nr.fb.band(direct_pole, 0) == {0: K(1)}
    assert not nr.fb.band(direct_pole, 1)
    direct_pole_two = nr.fb.band(direct_pole, 2)
    expected_pole_two = {
        degree: row.get((), K(0))
        for degree, row in enumerate(pole_current)
        if row.get((), K(0))
    }
    assert direct_pole_two == expected_pole_two

    equation_sha = equations_digest(x_current, pole_current)
    certificate_payload = (
        "[s^0*t^0]J=81/15625;required=1;residual=-15544/15625\n"
    )
    certificate_sha = sha256(certificate_payload.encode()).hexdigest()

    if x_error:
        print("TD6-PAIRED-THIRD-BAND: PASS")
        print("verdict = K-EMPTY")
        print(f"previous_survivor = rank 38 / 94; dimension 56")
        print(
            f"current_x = scalar_slots 40; nonzero_rows {sum(bool(row) for row in x_current)}; "
            f"parameter_degree 1; tangent_rank {x_tangent_rank} / 56"
        )
        print(
            "certificate = [s^0*t^0]J = 81/15625; "
            "required 1; residual -15544/15625"
        )
        print("certificate.parameter_coefficients = 0")
        print(
            "current_pole = scalar_slots 40; nonzero_rows 2 (zeta 1,6); "
            f"parameter_degree 2; quadratic_monomials {quadratic_monomials}; "
            f"tangent_rank_at_origin {pole_tangent_rank} / 56"
        )
        print(f"combined_tangent_rank_at_origin = {combined_tangent_rank} / 56")
        print(f"current_equations.sha256 = {equation_sha}")
        print(f"certificate.sha256 = {certificate_sha}")
        print("independent_global_differentiation = pass")
        print("pointwise_only = true")
        print("terminal_class_killed = false")
        print("JC2_resolved = false")
        return

    print("TD6-PAIRED-THIRD-BAND: INCOMPLETE")
    print(f"x_rank={len(x_pivots)} x_nullity={56-len(x_pivots)}")
    print("pole_nonlinear=true")


if __name__ == "__main__":
    main()
