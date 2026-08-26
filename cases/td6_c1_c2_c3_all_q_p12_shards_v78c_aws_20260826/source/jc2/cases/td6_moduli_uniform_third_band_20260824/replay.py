#!/usr/bin/env python3
"""Exact replay for TD6-MODULI-UNIFORM-THIRD-BAND (2026-08-24).

This replay works on the normalized source-open curve

    Q=-2*S^2+2*S+5*D-3=0,

after the full fixed-rectangle transport and the previous centered Jacobian
band.  It first derives the new constant row [s^0*t^0]J-1.  It then solves
all forty coefficients of [s^0]J-1 over the exact residue field of that row.
The pole side is deliberately not touched unless this centered band survives.
"""

from fractions import Fraction as QQ
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


# ---------------------------------------------------------------------------
# A small exact residue field.

# F is primitive and irreducible over Q: the replay independently certifies
# irreducibility by Rabin's criterion after reduction modulo 31.
F_INTEGER = (1411, -4032, 4680, -3045, 1170, -252, 24)
F_MONIC = tuple(QQ(value, 24) for value in F_INTEGER)


def fp_trim(poly, prime):
    poly = [value % prime for value in poly]
    while poly and not poly[-1]:
        poly.pop()
    return poly


def fp_divmod(left, right, prime):
    left = fp_trim(left, prime)
    right = fp_trim(right, prime)
    quotient = [0] * max(1, len(left) - len(right) + 1)
    inverse = pow(right[-1], -1, prime)
    while left and len(left) >= len(right):
        degree = len(left) - len(right)
        coefficient = left[-1] * inverse % prime
        quotient[degree] = coefficient
        for index, value in enumerate(right):
            left[degree + index] = (
                left[degree + index] - coefficient * value
            ) % prime
        left = fp_trim(left, prime)
    return fp_trim(quotient, prime), left


def fp_multiply_mod(left, right, modulus, prime):
    product = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            product[i + j] = (product[i + j] + a * b) % prime
    return fp_divmod(product, modulus, prime)[1]


def fp_power_mod(base, exponent, modulus, prime):
    out = [1]
    while exponent:
        if exponent & 1:
            out = fp_multiply_mod(out, base, modulus, prime)
        base = fp_multiply_mod(base, base, modulus, prime)
        exponent //= 2
    return out


def fp_gcd(left, right, prime):
    while fp_trim(right, prime):
        left, right = right, fp_divmod(left, right, prime)[1]
    left = fp_trim(left, prime)
    inverse = pow(left[-1], -1, prime)
    return [(value * inverse) % prime for value in left]


def certify_irreducible_mod_31():
    """Rabin test for degree six; prime divisors of six are 2 and 3."""
    prime = 31
    modulus = fp_trim(F_INTEGER, prime)
    x = [0, 1]

    def frobenius_difference(iterations):
        value = fp_power_mod(x, prime**iterations, modulus, prime)
        value += [0] * max(0, 2 - len(value))
        value[1] = (value[1] - 1) % prime
        return fp_trim(value, prime)

    assert fp_gcd(modulus, frobenius_difference(2), prime) == [1]
    assert fp_gcd(modulus, frobenius_difference(3), prime) == [1]
    assert not frobenius_difference(6)


def qpoly_trim(poly):
    poly = list(poly)
    while poly and not poly[-1]:
        poly.pop()
    return poly


def qpoly_divmod(left, right):
    left = qpoly_trim(left)
    right = qpoly_trim(right)
    quotient = [QQ(0)] * max(1, len(left) - len(right) + 1)
    while left and len(left) >= len(right):
        degree = len(left) - len(right)
        coefficient = left[-1] / right[-1]
        quotient[degree] = coefficient
        for index, value in enumerate(right):
            left[degree + index] -= coefficient * value
        left = qpoly_trim(left)
    return qpoly_trim(quotient), left


def qpoly_add(left, right, scale=QQ(1)):
    out = [QQ(0)] * max(len(left), len(right))
    for index in range(len(out)):
        if index < len(left):
            out[index] += left[index]
        if index < len(right):
            out[index] += scale * right[index]
    return qpoly_trim(out)


def qpoly_multiply(left, right):
    if not left or not right:
        return []
    out = [QQ(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return qpoly_trim(out)


def qpoly_extended_gcd(left, right):
    old_r, r = qpoly_trim(left), qpoly_trim(right)
    old_s, s = [QQ(1)], []
    old_t, t = [], [QQ(1)]
    while r:
        quotient, remainder = qpoly_divmod(old_r, r)
        old_r, r = r, remainder
        old_s, s = s, qpoly_add(old_s, qpoly_multiply(quotient, s), -QQ(1))
        old_t, t = t, qpoly_add(old_t, qpoly_multiply(quotient, t), -QQ(1))
    return old_r, old_s, old_t


class K:
    """K=Q[S]/(F), where F is the six-point centered-row polynomial."""

    __slots__ = ("coefficients",)

    def __init__(self, value=0):
        if isinstance(value, K):
            self.coefficients = value.coefficients
            return
        if isinstance(value, (list, tuple)):
            coefficients = [QQ(entry) for entry in value]
        else:
            coefficients = [QQ(value)]
        for degree in range(len(coefficients) - 1, 5, -1):
            coefficient = coefficients[degree]
            if coefficient:
                for index in range(6):
                    coefficients[degree - 6 + index] -= (
                        coefficient * F_MONIC[index]
                    )
        coefficients = qpoly_trim(coefficients[:6])
        self.coefficients = tuple(coefficients + [QQ(0)] * (6 - len(coefficients)))

    @staticmethod
    def coerce(value):
        return value if isinstance(value, K) else K(value)

    def __add__(self, other):
        other = K.coerce(other)
        return K([a + b for a, b in zip(self.coefficients, other.coefficients)])

    __radd__ = __add__

    def __neg__(self):
        return K([-value for value in self.coefficients])

    def __sub__(self, other):
        return self + (-K.coerce(other))

    def __rsub__(self, other):
        return K.coerce(other) - self

    def __mul__(self, other):
        other = K.coerce(other)
        product = [QQ(0)] * 11
        for i, a in enumerate(self.coefficients):
            for j, b in enumerate(other.coefficients):
                product[i + j] += a * b
        return K(product)

    __rmul__ = __mul__

    def inverse(self):
        if not self:
            raise ZeroDivisionError
        gcd, coefficient, _ = qpoly_extended_gcd(
            list(self.coefficients), list(F_MONIC)
        )
        assert len(gcd) == 1 and gcd[0]
        return K([value / gcd[0] for value in coefficient])

    def __truediv__(self, other):
        return self * K.coerce(other).inverse()

    def __rtruediv__(self, other):
        return K.coerce(other) * self.inverse()

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        out = K(1)
        base = self
        while exponent:
            if exponent & 1:
                out *= base
            base *= base
            exponent //= 2
        return out

    def __bool__(self):
        return any(self.coefficients)

    def __eq__(self, other):
        try:
            other = K.coerce(other)
        except (TypeError, ValueError):
            return False
        return self.coefficients == other.coefficients

    def __hash__(self):
        return hash(self.coefficients)

    def __repr__(self):
        return "K(" + ",".join(map(str, self.coefficients)) + ")"


S_FIELD = K([0, 1])
D_FIELD = (2 * S_FIELD**2 - 2 * S_FIELD + 3) / 5


def rational_determinant(matrix):
    matrix = [list(row) for row in matrix]
    determinant = QQ(1)
    for column in range(len(matrix)):
        pivot = next(
            row for row in range(column, len(matrix))
            if matrix[row][column]
        )
        if pivot != column:
            matrix[pivot], matrix[column] = matrix[column], matrix[pivot]
            determinant = -determinant
        lead = matrix[column][column]
        determinant *= lead
        matrix[column] = [value / lead for value in matrix[column]]
        for row in range(column + 1, len(matrix)):
            factor = matrix[row][column]
            if factor:
                matrix[row] = [
                    left - factor * right
                    for left, right in zip(matrix[row], matrix[column])
                ]
    return determinant


H_FIELD = (2 * S_FIELD**2 - 7 * S_FIELD + 8) / 5
L_FIELD = 25 * H_FIELD
ALPHA = K(9) / L_FIELD**8


class E:
    """E=K[A]/(A^3-ALPHA), the exact pole-normalized residue field."""

    __slots__ = ("coefficients",)

    def __init__(self, value=0):
        if isinstance(value, E):
            self.coefficients = value.coefficients
            return
        if isinstance(value, (list, tuple)):
            coefficients = [K(entry) for entry in value]
        else:
            coefficients = [K(value)]
        for degree in range(len(coefficients) - 1, 2, -1):
            coefficient = coefficients[degree]
            if coefficient:
                coefficients[degree - 3] += coefficient * ALPHA
        coefficients = qpoly_trim(coefficients[:3])
        self.coefficients = tuple(coefficients + [K(0)] * (3 - len(coefficients)))

    @staticmethod
    def coerce(value):
        return value if isinstance(value, E) else E(value)

    def __add__(self, other):
        other = E.coerce(other)
        return E([a + b for a, b in zip(self.coefficients, other.coefficients)])

    __radd__ = __add__

    def __neg__(self):
        return E([-value for value in self.coefficients])

    def __sub__(self, other):
        return self + (-E.coerce(other))

    def __rsub__(self, other):
        return E.coerce(other) - self

    def __mul__(self, other):
        other = E.coerce(other)
        product = [K(0)] * 5
        for i, a in enumerate(self.coefficients):
            for j, b in enumerate(other.coefficients):
                product[i + j] += a * b
        return E(product)

    __rmul__ = __mul__

    def inverse(self):
        if not self:
            raise ZeroDivisionError
        modulus = [-ALPHA, K(0), K(0), K(1)]
        gcd, coefficient, _ = qpoly_extended_gcd(
            list(self.coefficients), modulus
        )
        assert len(gcd) == 1 and gcd[0]
        return E([value / gcd[0] for value in coefficient])

    def __truediv__(self, other):
        return self * E.coerce(other).inverse()

    def __rtruediv__(self, other):
        return E.coerce(other) * self.inverse()

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        out = E(1)
        base = self
        while exponent:
            if exponent & 1:
                out *= base
            base *= base
            exponent //= 2
        return out

    def __bool__(self):
        return any(self.coefficients)

    def __eq__(self, other):
        try:
            other = E.coerce(other)
        except (TypeError, ValueError):
            return False
        return self.coefficients == other.coefficients

    def __hash__(self):
        return hash(self.coefficients)

    def __repr__(self):
        return "E(" + ",".join(map(str, self.coefficients)) + ")"


A_FIELD = E([K(0), K(1)])


def evaluate_on_curve(poly):
    out = K(0)
    for (s_degree, d_degree, l_degree, a_degree), coefficient in poly.items():
        assert l_degree == 0 and a_degree == 0
        out += coefficient * S_FIELD**s_degree * D_FIELD**d_degree
    return out


def evaluate_on_source(poly):
    out = E(0)
    for (s_degree, d_degree, l_degree, a_degree), coefficient in poly.items():
        out += (
            coefficient
            * E(S_FIELD) ** s_degree
            * E(D_FIELD) ** d_degree
            * E(L_FIELD) ** l_degree
            * A_FIELD**a_degree
        )
    return out


def substitute_curve_univariate(poly):
    """Substitute D=(2*S^2-2*S+3)/5 without reducing modulo F."""
    d_polynomial = [QQ(3, 5), QQ(-2, 5), QQ(2, 5)]
    out = []
    for (s_degree, d_degree, l_degree, a_degree), coefficient in poly.items():
        assert l_degree == 0 and a_degree == 0
        term = [QQ(1)]
        for _ in range(d_degree):
            term = qpoly_multiply(term, d_polynomial)
        term = [QQ(0)] * s_degree + term
        out = qpoly_add(out, [coefficient * value for value in term])
    return qpoly_trim(out)


# ---------------------------------------------------------------------------
# Symbolic transport and affine-band compiler.

def symbolic_parameterization(nvariables, pivots, pivot_rhs):
    free = [variable for variable in range(nvariables) if variable not in pivots]
    parameter_of = {variable: index for index, variable in enumerate(free)}
    constants = [{} for _ in range(nvariables)]
    directions = [None] * nvariables
    for variable in range(nvariables - 1, -1, -1):
        if variable in parameter_of:
            directions[variable] = {parameter_of[variable]: QQ(1)}
            continue
        row = pivots[variable]
        constant = dict(pivot_rhs[variable])
        direction = {}
        for other, coefficient in row.items():
            if other == variable:
                continue
            constant = mu.poly_add(constant, constants[other], -coefficient)
            for parameter, value in directions[other].items():
                nr.add_linear(direction, parameter, -coefficient * value)
        constants[variable] = constant
        directions[variable] = direction
    return constants, directions, free


def propagate_rhs(records, original_rhs):
    pivot_rhs = {}
    compatibility = []
    for key, kind, pivot, lead, factors in records:
        rhs = dict(original_rhs[key])
        for old_pivot, factor in factors:
            rhs = mu.poly_add(rhs, pivot_rhs[old_pivot], -factor)
        if kind == "pivot":
            pivot_rhs[pivot] = mu.poly_scale(rhs, QQ(1) / lead)
        elif rhs:
            compatibility.append((key, rhs))
    return pivot_rhs, compatibility


def compose_global(base_constants, base_directions, parameter_constants, parameter_directions):
    constants = []
    directions = []
    for constant, old_direction in zip(base_constants, base_directions):
        new_constant = dict(constant)
        new_direction = {}
        for old_parameter, coefficient in old_direction.items():
            new_constant = mu.poly_add(
                new_constant, parameter_constants[old_parameter], coefficient
            )
            for new_parameter, value in parameter_directions[old_parameter].items():
                nr.add_linear(new_direction, new_parameter, coefficient * value)
        constants.append(new_constant)
        directions.append(new_direction)
    return constants, directions


def symbolic_band(imax, jmax, exponent, constants, directions, offset):
    constant_band = mu.symbolic_x_band(
        imax, jmax, exponent, constants, offset
    )
    affine_forms = [(QQ(0), row) for row in directions]
    direction_band = nr.x_band_forms(
        imax, jmax, exponent, affine_forms, offset
    )
    return [
        (constant, direction[1])
        for constant, direction in zip(constant_band, direction_band)
    ]


def symbolic_pole_band(imax, jmax, exponent, constants, directions, offset):
    out = []
    for degree in range(jmax + 1):
        row = nr.pole_coefficient(imax, jmax, exponent, degree)
        constant = mu.symbolic_global_linear(row, constants, offset)
        direction = {}
        for variable, coefficient in row.items():
            for parameter, value in directions[offset + variable].items():
                nr.add_linear(direction, parameter, coefficient * value)
        out.append((constant, direction))
    return out


def parameter_polynomial(form):
    out = {(): form[0]} if form[0] else {}
    for parameter, coefficient in form[1].items():
        if coefficient:
            out[(parameter,)] = mu.poly_constant(coefficient)
    return out


def pp_add(left, right, scale=QQ(1)):
    out = dict(left)
    for monomial, coefficient in right.items():
        value = mu.poly_add(out.get(monomial, {}), coefficient, scale)
        if value:
            out[monomial] = value
        else:
            out.pop(monomial, None)
    return out


def pp_scale(poly, scale):
    return {
        monomial: mu.poly_scale(coefficient, scale)
        for monomial, coefficient in poly.items()
        if mu.poly_scale(coefficient, scale)
    }


def pp_multiply_forms(left, right):
    out = {}
    for left_monomial, left_coefficient in parameter_polynomial(left).items():
        for right_monomial, right_coefficient in parameter_polynomial(right).items():
            monomial = tuple(sorted(left_monomial + right_monomial))
            out = pp_add(
                out,
                {monomial: mu.poly_multiply(left_coefficient, right_coefficient)},
            )
    return out


def scale_form(form, scale):
    return (
        mu.poly_scale(form[0], scale),
        {parameter: scale * value for parameter, value in form[1].items()},
    )


def compile_centered_constant_band(f1, f2, f3, g1, g2, g3):
    rows = []
    for degree in range(40):
        equation = {}
        for i, left in enumerate(f1):
            j = degree - i + 1
            if 1 <= j < len(g2):
                scaled = scale_form(g2[j], QQ(j))
                equation = pp_add(equation, pp_multiply_forms(left, scaled))
        for i, left in enumerate(f2):
            j = degree - i + 1
            if 1 <= j < len(g1):
                scaled = scale_form(g1[j], QQ(j))
                equation = pp_add(
                    equation, pp_multiply_forms(left, scaled), QQ(2)
                )
        for i, form in enumerate(f3):
            if degree - i == 0:
                equation = pp_add(equation, parameter_polynomial(form), QQ(3))
            if degree - i == 24:
                equation = pp_add(equation, parameter_polynomial(form), QQ(75))
        g_degree = degree - 14
        if 0 <= g_degree < len(g3):
            equation = pp_add(
                equation, parameter_polynomial(g3[g_degree]), QQ(-45)
            )
        for i in range(1, len(f1)):
            j = degree - (i - 1)
            if 0 <= j < len(g2):
                scaled = scale_form(f1[i], QQ(i))
                equation = pp_add(
                    equation, pp_multiply_forms(scaled, g2[j]), QQ(-2)
                )
        for i in range(1, len(f2)):
            j = degree - (i - 1)
            if 0 <= j < len(g1):
                scaled = scale_form(f2[i], QQ(i))
                equation = pp_add(
                    equation, pp_multiply_forms(scaled, g1[j]), QQ(-1)
                )
        if degree == 0:
            equation = pp_add(
                equation, {(): mu.poly_constant(1)}, QQ(-1)
            )
        assert all(len(monomial) <= 1 for monomial in equation)
        rows.append(equation)
    return rows


def compile_previous_pole_band(p1, q1):
    p = [({}, {}) for _ in range(7)]
    q = [({}, {}) for _ in range(11)]
    for degree, coefficient in mu.POLE_F.items():
        p[degree] = (coefficient, {})
    for degree, coefficient in mu.POLE_G.items():
        q[degree] = (coefficient, {})

    rows = []
    for degree in range(14):
        equation = {}
        # -3*p*q1' -2*p1*q' +4*p'*q1 +5*p1'*q
        for i, left in enumerate(p):
            j = degree - i + 1
            if 1 <= j < len(q1):
                equation = pp_add(
                    equation,
                    pp_multiply_forms(left, scale_form(q1[j], QQ(j))),
                    QQ(-3),
                )
        for i, left in enumerate(p1):
            j = degree - i + 1
            if 1 <= j < len(q):
                equation = pp_add(
                    equation,
                    pp_multiply_forms(left, scale_form(q[j], QQ(j))),
                    QQ(-2),
                )
        for i in range(1, len(p)):
            j = degree - (i - 1)
            if 0 <= j < len(q1):
                equation = pp_add(
                    equation,
                    pp_multiply_forms(scale_form(p[i], QQ(i)), q1[j]),
                    QQ(4),
                )
        for i in range(1, len(p1)):
            j = degree - (i - 1)
            if 0 <= j < len(q):
                equation = pp_add(
                    equation,
                    pp_multiply_forms(scale_form(p1[i], QQ(i)), q[j]),
                    QQ(5),
                )
        rows.append(pp_scale(equation, QQ(-1, 25)))
    return rows


def pack_field_rows(family, symbolic_rows, evaluator):
    packed = []
    evaluated = []
    for degree, polynomial in enumerate(symbolic_rows):
        row = {}
        constant = evaluator({})
        for monomial, coefficient in polynomial.items():
            value = evaluator(coefficient)
            if not monomial:
                constant += value
            else:
                assert len(monomial) == 1
                if value:
                    row[monomial[0]] = value
        if row or constant:
            packed.append(((family, degree), row, -constant))
        evaluated.append((constant, row))
    return packed, evaluated


def solve_field_rows(family, symbolic_rows, nparameters, evaluator):
    packed, evaluated = pack_field_rows(family, symbolic_rows, evaluator)
    solution, pivots, error = nr.fb.exact_solve(
        nparameters, packed, allow_inconsistent=True
    )
    return evaluated, solution, pivots, error


def inconsistency_certificate(rows):
    """Return an exact left-null combination with nonzero RHS."""
    pivots = {}
    for index, (key, original_row, original_rhs) in enumerate(rows):
        row = dict(original_row)
        rhs = original_rhs
        combination = {index: E(1)}
        while row:
            pivot = min(row)
            if pivot not in pivots:
                break
            factor = row[pivot]
            old_row, old_rhs, old_combination = pivots[pivot]
            for variable, coefficient in old_row.items():
                value = row.get(variable, E(0)) - factor * coefficient
                if value:
                    row[variable] = value
                else:
                    row.pop(variable, None)
            rhs -= factor * old_rhs
            for old_index, coefficient in old_combination.items():
                value = combination.get(old_index, E(0)) - factor * coefficient
                if value:
                    combination[old_index] = value
                else:
                    combination.pop(old_index, None)
        if not row:
            if rhs:
                # Replay the returned dual certificate directly against the
                # original, unecheloned rows.
                check_row = {}
                check_rhs = E(0)
                for old_index, weight in combination.items():
                    _, old_row, old_rhs = rows[old_index]
                    for variable, coefficient in old_row.items():
                        value = check_row.get(variable, E(0)) + weight * coefficient
                        if value:
                            check_row[variable] = value
                        else:
                            check_row.pop(variable, None)
                    check_rhs += weight * old_rhs
                assert not check_row and check_rhs == rhs
                return key, combination, rhs
            continue
        pivot = min(row)
        lead = row[pivot]
        pivots[pivot] = (
            {variable: coefficient / lead for variable, coefficient in row.items()},
            rhs / lead,
            {old_index: coefficient / lead for old_index, coefficient in combination.items()},
        )
    raise AssertionError("system was consistent")


def poly_text(poly):
    return mu.poly_text(poly)


def field_text(value):
    value = K.coerce(value)
    return "+".join(
        f"({coefficient.numerator}/{coefficient.denominator})*S^{degree}"
        for degree, coefficient in enumerate(value.coefficients)
        if coefficient
    ) or "0"


def extension_text(value):
    value = E.coerce(value)
    return "|".join(field_text(coefficient) for coefficient in value.coefficients)


def dual_digest(rows, combination, residual):
    digest = sha256()
    for index, weight in sorted(combination.items()):
        digest.update(f"row{index}:{extension_text(weight)}\n".encode())
    digest.update(f"residual:{extension_text(residual)}\n".encode())
    return digest.hexdigest()


def equations_digest(rows):
    digest = sha256()
    for degree, row in enumerate(rows):
        digest.update(f"X0,{degree}".encode())
        for monomial, coefficient in sorted(row.items()):
            digest.update(
                f";{monomial}:{poly_text(coefficient)}".encode()
            )
        digest.update(b"\n")
    return digest.hexdigest()


def main():
    certify_irreducible_mod_31()
    assert sum(K(F_INTEGER[index]) * S_FIELD**index for index in range(7)) == 0
    assert 3 * H_FIELD**3 == 1
    assert ALPHA == 243 * H_FIELD / 25**8

    # Norm_{K/Q}(ALPHA) is not a rational cube (its 3-adic valuation is 28),
    # hence ALPHA is not a cube in K.  Thus A^3-ALPHA is irreducible over K.
    multiplication_columns = [
        (ALPHA * S_FIELD**degree).coefficients for degree in range(6)
    ]
    norm_matrix = [
        [multiplication_columns[column][row] for column in range(6)]
        for row in range(6)
    ]
    alpha_norm = rational_determinant(norm_matrix)
    assert alpha_norm == QQ(3**28, 5**96)
    assert 28 % 3
    assert A_FIELD**3 == E(ALPHA)
    assert E(L_FIELD) ** 8 * A_FIELD**3 == 9

    nr.fb.CENTER = (QQ(1), QQ(1), QQ(1))
    nr.fb._X_POWER_CACHE.clear()
    nf, ng, _, _, base_rows = nr.build_first_band_system()
    base_pivots, base_records = mu.factor_matrix(base_rows)
    assert (nf, ng, len(base_rows), len(base_pivots)) == (
        976, 2626, 6547, 3508
    )
    base_rhs, compatibility = mu.propagate_symbolic_rhs(base_records)
    assert len(compatibility) == 2
    base_constants = mu.symbolic_particular_solution(
        nf + ng, base_pivots, base_rhs
    )
    rational_forms, free_94, _ = nr.affine_parameterization(
        nf + ng, base_rows
    )
    base_directions = [form[1] for form in rational_forms]
    assert len(free_94) == 94

    symbolic_f1 = mu.symbolic_x_band(15, 60, 1, base_constants, 0)
    symbolic_f2 = mu.symbolic_x_band(15, 60, 2, base_constants, 0)
    symbolic_g1 = mu.symbolic_x_band(25, 100, 1, base_constants, nf)
    symbolic_g2 = mu.symbolic_x_band(25, 100, 2, base_constants, nf)
    previous_constants = mu.symbolic_x_next_rows(
        symbolic_f1, symbolic_f2, symbolic_g1, symbolic_g2
    )

    f1 = nr.x_band_forms(15, 60, 1, rational_forms, 0)
    f2 = nr.x_band_forms(15, 60, 2, rational_forms, 0)
    g1 = nr.x_band_forms(25, 100, 1, rational_forms, nf)
    g2 = nr.x_band_forms(25, 100, 2, rational_forms, nf)
    previous_tangent = nr.tangent_rows(nr.compile_x_next_rows(f1, f2, g1, g2))
    previous_matrix_rows = [
        (("X-1", degree), row, QQ(0))
        for degree, row in enumerate(previous_tangent)
        if row or previous_constants[degree]
    ]
    previous_pivots, previous_records = mu.factor_matrix(previous_matrix_rows)
    previous_original_rhs = {
        ("X-1", degree): mu.poly_scale(previous_constants[degree], QQ(-1))
        for degree in range(40)
        if previous_tangent[degree] or previous_constants[degree]
    }
    previous_rhs, previous_compatibility = propagate_rhs(
        previous_records, previous_original_rhs
    )
    assert len(previous_pivots) == 36
    assert len(previous_compatibility) == 1
    expected_Q = mu.poly_add(
        mu.poly_add(
            mu.poly_scale(mu.poly_power(mu.S, 2), QQ(-2)),
            mu.poly_scale(mu.S, QQ(2)),
        ),
        mu.poly_add(mu.poly_scale(mu.D, QQ(5)), mu.poly_constant(-3)),
    )
    compatibility_poly = previous_compatibility[0][1]
    # The dependent row is a nonzero rational multiple of Q.
    common_monomial = next(iter(compatibility_poly))
    ratio = compatibility_poly[common_monomial] / expected_Q[common_monomial]
    assert compatibility_poly == mu.poly_scale(expected_Q, ratio)

    parameter_constants, parameter_directions, free_58 = symbolic_parameterization(
        94, previous_pivots, previous_rhs
    )
    assert len(free_58) == 58
    global_constants, global_directions = compose_global(
        base_constants,
        base_directions,
        parameter_constants,
        parameter_directions,
    )

    sf1 = symbolic_band(15, 60, 1, global_constants, global_directions, 0)
    sf2 = symbolic_band(15, 60, 2, global_constants, global_directions, 0)
    sf3 = symbolic_band(15, 60, 3, global_constants, global_directions, 0)
    sg1 = symbolic_band(25, 100, 1, global_constants, global_directions, nf)
    sg2 = symbolic_band(25, 100, 2, global_constants, global_directions, nf)
    sg3 = symbolic_band(25, 100, 3, global_constants, global_directions, nf)
    current = compile_centered_constant_band(sf1, sf2, sf3, sg1, sg2, sg3)

    # The previous pole band is part of the inherited paired survivor.  It is
    # still affine-linear here; the successor quadratic pole band is not yet
    # compiled or used.
    sp1 = symbolic_pole_band(
        15, 60, -2, global_constants, global_directions, 0
    )
    sq1 = symbolic_pole_band(
        25, 100, -4, global_constants, global_directions, nf
    )
    previous_pole = compile_previous_pole_band(sp1, sq1)
    assert all(len(monomial) <= 1 for row in previous_pole for monomial in row)

    H = mu.poly_add(mu.poly_add(mu.ONE, mu.S, -QQ(1)), mu.D)
    expected_constant_row = mu.poly_add(
        mu.poly_scale(mu.poly_power(H, 3), QQ(3)), mu.poly_constant(-1)
    )
    assert current[0] == {(): expected_constant_row}
    assert sf2[1][0] == {}
    assert sf3[0][0] == mu.poly_power(H, 3)
    assert not sf2[1][1] and not sf3[0][1]

    # Substitution of D=(2*S^2-2*S+3)/5 gives F(S)/125 exactly.
    assert substitute_curve_univariate(expected_constant_row) == [
        QQ(value, 125) for value in F_INTEGER
    ]
    assert evaluate_on_curve(expected_constant_row) == 0
    assert evaluate_on_source(expected_constant_row) == 0

    pole_packed, pole_evaluated = pack_field_rows(
        "P1", previous_pole, evaluate_on_source
    )
    pole_solution, pole_pivots, pole_error = nr.fb.exact_solve(
        58, pole_packed, allow_inconsistent=True
    )
    assert pole_solution is not None and pole_error is None
    assert len(pole_pivots) == 2

    current_packed, current_evaluated = pack_field_rows(
        "X0", current, evaluate_on_source
    )
    assert current_evaluated[0] == (E(0), {})
    current_solution, current_pivots, current_error = nr.fb.exact_solve(
        58, current_packed, allow_inconsistent=True
    )
    assert current_solution is None and current_error is not None
    certificate_key, certificate_weights, certificate_residual = (
        inconsistency_certificate(current_packed)
    )
    assert certificate_key == current_error[0]
    assert certificate_residual == current_error[1]
    assert certificate_key == ("X0", 4)
    expected_residual = E(
        [
            K(
                [
                    QQ(2495634, 3625),
                    QQ(-4154976, 3625),
                    QQ(4405068, 3625),
                    QQ(-2488119, 3625),
                    QQ(761922, 3625),
                    QQ(-105084, 3625),
                ]
            ),
            K(QQ(136875, 29)),
        ]
    )
    assert certificate_residual == expected_residual
    # The A coefficient is nonzero, so this residue cannot vanish in the
    # K-basis 1,A,A^2 of the irreducible cubic extension E/K.
    assert certificate_residual.coefficients[1] == K(QQ(136875, 29))

    tangent_rows = [
        (key, row, E(0)) for key, row, _ in current_packed if row
    ]
    _, tangent_pivots, tangent_error = nr.fb.exact_solve(
        58, tangent_rows, allow_inconsistent=True
    )
    assert tangent_error is None
    current_tangent_rank = len(tangent_pivots)

    # Source-open saturation checks.  D, the U/V discriminant, and H share no
    # root with F; the hard-coded resultants are independently replayed by a
    # rational Euclidean gcd below.
    D_numerator = [QQ(3), QQ(-2), QQ(2)]
    discriminant_numerator = [QQ(-12), QQ(8), QQ(-3)]
    H_numerator = [QQ(8), QQ(-7), QQ(2)]
    top_coefficient = [QQ(2), QQ(1)]  # S+2
    for exclusion in (
        D_numerator,
        discriminant_numerator,
        H_numerator,
        top_coefficient,
    ):
        gcd, _, _ = qpoly_extended_gcd(list(F_INTEGER), exclusion)
        assert len(gcd) == 1 and gcd[0]
    assert 3 * ((2 * S_FIELD**2 - 7 * S_FIELD + 8) / 5) ** 3 == 1

    nonzero_rows = sum(bool(row) for row in current)
    equation_sha = equations_digest(current)
    certificate_sha = dual_digest(
        current_packed, certificate_weights, certificate_residual
    )
    formula_payload = (
        "Q=-2*S^2+2*S+5*D-3\n"
        "[s^0*t^0]J-1=3*(1-S+D)^3-1\n"
        "F=24*S^6-252*S^5+1170*S^4-3045*S^3+4680*S^2-4032*S+1411\n"
    )
    formula_sha = sha256(formula_payload.encode()).hexdigest()

    print("TD6-MODULI-UNIFORM-THIRD-BAND: PASS")
    print("verdict = NORMALIZED-BOUNDARY-FAMILY-EMPTY-AT-CENTERED-BAND")
    print("normalized_source_curve = -2*S^2+2*S+5*D-3=0")
    print("constant_row = 3*(1-S+D)^3-1")
    print(
        "elimination_polynomial = "
        "24*S^6-252*S^5+1170*S^4-3045*S^3+4680*S^2-4032*S+1411"
    )
    print("elimination_degree = 6; squarefree = true; irreducible_mod_31 = true")
    print(
        "source_exclusions_saturated = D, U-V, 1-U, 1-V, "
        "S+2, L, A"
    )
    print("transport = rows 6547; rank 3508 / 3602; first_affine_dimension 94")
    print("previous_centered_band = rank 36 / 94; curve_affine_dimension 58")
    print(
        "pole_normalization = L=25*(1-S+D); A^3=9/L^8; "
        "degree_18_source_field"
    )
    print("inherited_pole_band = rank 2 / 58; consistent")
    print(
        f"centered_band = slots 40; symbolic_nonzero_rows {nonzero_rows}; "
        f"tangent_rank {current_tangent_rank} / 58 over Q(S,A) residue field"
    )
    print(
        "left_syzygy = X0 degree 4; residual = "
        "(2495634-4154976*S+4405068*S^2-2488119*S^3+"
        "761922*S^4-105084*S^5)/3625 + (136875/29)*A"
    )
    print("residual_nonzero_at_all_18_pole_normalized_conjugate_points = true")
    print("quadratic_pole_band_touched = false")
    print(f"centered_equations.sha256 = {equation_sha}")
    print(f"left_syzygy.sha256 = {certificate_sha}")
    print(f"formula.sha256 = {formula_sha}")
    print(f"parent_replay.sha256 = {MODULI_REPLAY_SHA256}")
    print("normalized_boundary_family_killed = true")
    print("SP2_killed = false")
    print("JC2_resolved = false")


if __name__ == "__main__":
    main()
