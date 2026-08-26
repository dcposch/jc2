#!/usr/bin/env python3
"""Private exact first derivative of the TD6 q2 compatibility at B=0.

This deliberately imports the frozen repository artifacts read-only.  The
coefficient class below is E[eps]/(eps^2), so Gaussian elimination itself
differentiates the normalized left-null relation; no compatible-base adjoint
shortcut is used.
"""

from fractions import Fraction as Q
from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]


def load(name, path, expected):
    assert sha256(path.read_bytes()).hexdigest() == expected
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


base = load(
    "q2_base",
    REPO / "cases/td6_boundary_q2_deformation_20260824/replay.py",
    "0ba184470dc051fad50640647c4b78ea869b8a4153219026b23abdcf0652d357",
)
uniform = load(
    "uniform_third",
    REPO / "cases/td6_moduli_uniform_third_band_20260824/replay.py",
    "7a21f9495d1e8784a9b253253430846ce882e2ce26f91815b31b6e061022cba8",
)
nr, fb, E, K = base.nr, base.fb, uniform.E, uniform.K


class Dual:
    """A first-order dual number over the exact degree-18 field E."""

    __slots__ = ("value", "derivative")

    def __init__(self, value=0, derivative=0):
        if isinstance(value, Dual):
            self.value = value.value
            self.derivative = value.derivative
        else:
            self.value = E(value)
            self.derivative = E(derivative)

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Dual) else Dual(value)

    def __add__(self, other):
        other = Dual.coerce(other)
        return Dual(self.value + other.value, self.derivative + other.derivative)

    __radd__ = __add__

    def __neg__(self):
        return Dual(-self.value, -self.derivative)

    def __sub__(self, other):
        return self + (-Dual.coerce(other))

    def __rsub__(self, other):
        return Dual.coerce(other) - self

    def __mul__(self, other):
        other = Dual.coerce(other)
        derivative = E(0)
        if self.derivative:
            derivative += self.derivative * other.value
        if other.derivative:
            derivative += self.value * other.derivative
        return Dual(
            self.value * other.value,
            derivative,
        )

    __rmul__ = __mul__

    def inverse(self):
        if not self.value:
            raise ZeroDivisionError("dual pivot has zero base")
        inverse = self.value.inverse()
        return Dual(inverse, -(inverse * inverse) * self.derivative)

    def __truediv__(self, other):
        return self * Dual.coerce(other).inverse()

    def __rtruediv__(self, other):
        return Dual.coerce(other) / self

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        out = Dual(1)
        base_value = self
        while exponent:
            if exponent & 1:
                out *= base_value
            base_value *= base_value
            exponent //= 2
        return out

    def __bool__(self):
        return bool(self.value) or bool(self.derivative)

    def __eq__(self, other):
        other = Dual.coerce(other)
        return (
            self.value == other.value
            and self.derivative == other.derivative
        )

    def __repr__(self):
        return f"Dual({self.value!r};{self.derivative!r})"


S = Dual(uniform.S_FIELD)
D = Dual(uniform.D_FIELD)
L = Dual(uniform.L_FIELD)
A = Dual(uniform.A_FIELD)
B = Dual(0, 1)
Q_PRIME = {0: Dual(1), 1: 2 * B, 24: Dual(25)}


def multiply(left, right):
    out = [Dual(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def power(poly, exponent):
    out = [Dual(1)]
    for _ in range(exponent):
        out = multiply(out, poly)
    return out


R = multiply(multiply([Dual(-1), Dual(1)], [Dual(-1), Dual(1)]), [D, -S, Dual(1)])
R3, R5 = power(R, 3), power(R, 5)
POLE_F = {1: -(L**3) * A, 6: L**3}
POLE_G = {
    0: Dual(Q(5, 9)) * L**5 * A**2,
    5: Dual(Q(-5, 3)) * L**5 * A,
    10: L**5,
}


def source_rhs(key):
    if key[0] == "JX-FIRST":
        return Dual(0)
    owner, chart, exponent, degree = key
    if chart == "X" and exponent == 0:
        if owner == "f":
            return Dual(1 if degree == 15 else 0)
        return {1: Dual(1), 2: B, 25: Dual(1)}.get(degree, Dual(0))
    if chart == "F1" and exponent == (-15 if owner == "f" else -25):
        pattern = R3 if owner == "f" else R5
        if degree % 5 == 0 and degree // 5 < len(pattern):
            return pattern[degree // 5]
        return Dual(0)
    if chart == "F0" and exponent == (-3 if owner == "f" else -5):
        return (POLE_F if owner == "f" else POLE_G).get(degree, Dual(0))
    return Dual(0)


def build_transport_rows():
    nf, rf = fb.build_transport(
        15, 60, 3, {15: Q(1)}, fb.F1_F_PATTERN, fb.POLE_F_PATTERN
    )
    ng, rg = fb.build_transport(
        25, 100, 5, {1: Q(1), 25: Q(1)}, fb.F1_G_PATTERN, fb.POLE_G_PATTERN
    )
    rows = [(("f",) + key, row, rhs) for key, row, rhs in rf]
    rows += [
        (("g",) + key, {nf + v: c for v, c in row.items()}, rhs)
        for key, row, rhs in rg
    ]
    return nf, ng, rows


def propagate(records):
    pivot_rhs = {}
    compatibility = []
    for key, kind, pivot, lead, factors in records:
        value = source_rhs(key)
        for old, factor in factors:
            value -= factor * pivot_rhs[old]
        if kind == "pivot":
            pivot_rhs[pivot] = value / lead
        elif value:
            compatibility.append((key, value))
    return pivot_rhs, compatibility


def direction_parameterization(nvariables, pivots, pivot_rhs):
    free = [v for v in range(nvariables) if v not in pivots]
    parameter_of = {v: k for k, v in enumerate(free)}
    forms = [None] * nvariables
    for variable in range(nvariables - 1, -1, -1):
        if variable in parameter_of:
            # The transport matrix is constant.  Retain its homogeneous
            # directions over Q; wrapping millions of zero-derivative
            # coefficients in E[eps] is both unnecessary and very slow.
            forms[variable] = (Dual(0), {parameter_of[variable]: Q(1)})
            continue
        form = (pivot_rhs[variable], {})
        for other, coefficient in pivots[variable].items():
            if other != variable:
                form = nr.add_affine(form, forms[other], -coefficient)
        forms[variable] = form
    return forms, free


def first_band_polynomials(f1, g1):
    rows = []
    for degree in range(40):
        equation = {}
        for i, form in enumerate(f1):
            multiplier = Q_PRIME.get(degree - i, Dual(0))
            if multiplier:
                equation = nr.add_polynomial(
                    equation, nr.affine_polynomial(form), multiplier
                )
        j = degree - 14
        if 0 <= j < len(g1):
            equation = nr.add_polynomial(
                equation, nr.affine_polynomial(g1[j]), Dual(-15)
            )
        rows.append(equation)
    return rows


def pack(family, polynomials):
    out = []
    for degree, polynomial in enumerate(polynomials):
        row = {}
        constant = Dual.coerce(polynomial.get((), 0))
        for monomial, coefficient in polynomial.items():
            if monomial:
                assert len(monomial) == 1
                coefficient = Dual.coerce(coefficient)
                if coefficient:
                    row[monomial[0]] = coefficient
        if row or constant:
            out.append(((family, degree), row, -constant))
    return out


def solve(nvariables, rows, stop_on_base_inconsistency=True):
    """Dual GE, choosing exactly the nonzero base pivots."""
    pivots = {}
    dependent = []
    for key, original_row, original_rhs in rows:
        row = {v: Dual.coerce(c) for v, c in original_row.items()}
        rhs = Dual.coerce(original_rhs)
        # Reduce every already-pivoted column, including a coefficient that
        # is derivative-only.  The latter corresponds to the lambda' A term;
        # dropping it is precisely the incompatible-base adjoint error this
        # replay is designed to avoid.
        while True:
            reducible = [
                variable
                for variable, coefficient in row.items()
                if coefficient and variable in pivots
            ]
            if not reducible:
                break
            pivot = min(reducible)
            factor = row[pivot]
            old_row, old_rhs = pivots[pivot]
            for variable, coefficient in old_row.items():
                value = row.get(variable, Dual(0)) - factor * coefficient
                if value:
                    row[variable] = value
                else:
                    row.pop(variable, None)
            rhs -= factor * old_rhs
        # Derivative-only coefficients cannot become pivots on the fixed
        # rank stratum; their presence records a rank-change direction.
        base_row = {v: c for v, c in row.items() if c.value}
        derivative_only = {v: c.derivative for v, c in row.items() if not c.value and c.derivative}
        if not base_row:
            dependent.append((key, rhs, derivative_only))
            if rhs.value and stop_on_base_inconsistency:
                return None, pivots, (key, rhs, derivative_only), dependent
            continue
        pivot = min(base_row)
        lead = row[pivot]
        pivots[pivot] = (
            {v: c / lead for v, c in row.items()},
            rhs / lead,
        )
    solution = {}
    for pivot in sorted(pivots, reverse=True):
        row, rhs = pivots[pivot]
        value = rhs
        for variable, coefficient in row.items():
            if variable != pivot:
                value -= coefficient * solution.get(variable, Dual(0))
        solution[pivot] = value
    return solution, pivots, None, dependent


def affine_parameterization(nvariables, rows):
    solution, pivots, error, dependent = solve(nvariables, rows)
    if error:
        return None, None, pivots, error, dependent
    free = [v for v in range(nvariables) if v not in pivots]
    parameter_of = {v: k for k, v in enumerate(free)}
    # A dual pivot row may contain derivative-only entries in columns below
    # its base pivot.  Direct descending back-substitution is then not
    # triangular over E[eps].  Split base and derivative: first compute every
    # base affine form using the frozen triangular matrix; then solve the
    # differentiated triangular equations, where all base forms are known.
    base_forms = [None] * nvariables
    for variable in range(nvariables - 1, -1, -1):
        if variable in parameter_of:
            base_forms[variable] = (E(0), {parameter_of[variable]: E(1)})
            continue
        row, rhs = pivots[variable]
        form = (rhs.value, {})
        for other, coefficient in row.items():
            if other != variable and coefficient.value:
                form = nr.add_affine(
                    form, base_forms[other], -coefficient.value
                )
        base_forms[variable] = form

    derivative_forms = [None] * nvariables
    zero_form = (E(0), {})
    for variable in range(nvariables - 1, -1, -1):
        if variable in parameter_of:
            derivative_forms[variable] = zero_form
            continue
        row, rhs = pivots[variable]
        form = (rhs.derivative, {})
        for other, coefficient in row.items():
            if other == variable:
                continue
            if coefficient.value:
                form = nr.add_affine(
                    form, derivative_forms[other], -coefficient.value
                )
            if coefficient.derivative:
                form = nr.add_affine(
                    form, base_forms[other], -coefficient.derivative
                )
        derivative_forms[variable] = form

    forms = []
    for base_form, derivative_form in zip(base_forms, derivative_forms):
        parameters = set(base_form[1]) | set(derivative_form[1])
        forms.append(
            (
                Dual(base_form[0], derivative_form[0]),
                {
                    parameter: Dual(
                        base_form[1].get(parameter, E(0)),
                        derivative_form[1].get(parameter, E(0)),
                    )
                    for parameter in parameters
                    if base_form[1].get(parameter, E(0))
                    or derivative_form[1].get(parameter, E(0))
                },
            )
        )
    return forms, free, pivots, None, dependent


def replay_affine_rows(rows, forms):
    """Coefficientwise identity replay over the dual field."""
    for key, row, rhs in rows:
        got = (Dual(0), {})
        for variable, coefficient in row.items():
            got = nr.add_affine(got, forms[variable], coefficient)
        assert got == (Dual.coerce(rhs), {}), (key, got, rhs)


def inconsistency_certificate(rows):
    """Dual left-null certificate, including the derivative of lambda."""
    pivots = {}
    for index, (key, original_row, original_rhs) in enumerate(rows):
        row = {variable: Dual.coerce(value) for variable, value in original_row.items()}
        rhs = Dual.coerce(original_rhs)
        combination = {index: Dual(1)}
        while True:
            reducible = [
                variable
                for variable, coefficient in row.items()
                if coefficient and variable in pivots
            ]
            if not reducible:
                break
            pivot = min(reducible)
            factor = row[pivot]
            old_row, old_rhs, old_combination = pivots[pivot]
            for variable, coefficient in old_row.items():
                value = row.get(variable, Dual(0)) - factor * coefficient
                if value:
                    row[variable] = value
                else:
                    row.pop(variable, None)
            rhs -= factor * old_rhs
            for old_index, coefficient in old_combination.items():
                value = combination.get(old_index, Dual(0)) - factor * coefficient
                if value:
                    combination[old_index] = value
                else:
                    combination.pop(old_index, None)

        base_row = {variable: coefficient for variable, coefficient in row.items() if coefficient.value}
        if not base_row:
            derivative_only = {
                variable: coefficient.derivative
                for variable, coefficient in row.items()
                if coefficient.derivative
            }
            assert not derivative_only, ("rank-change before certificate", key)
            if rhs.value:
                check_row = {}
                check_rhs = Dual(0)
                for old_index, weight in combination.items():
                    _, old_row, old_rhs = rows[old_index]
                    for variable, coefficient in old_row.items():
                        value = check_row.get(variable, Dual(0)) + weight * coefficient
                        if value:
                            check_row[variable] = value
                        else:
                            check_row.pop(variable, None)
                    check_rhs += weight * old_rhs
                assert not check_row and check_rhs == rhs
                return key, combination, rhs
            continue

        pivot = min(base_row)
        lead = row[pivot]
        pivots[pivot] = (
            {variable: coefficient / lead for variable, coefficient in row.items()},
            rhs / lead,
            {old_index: coefficient / lead for old_index, coefficient in combination.items()},
        )
    raise AssertionError("no inconsistent base row")


def dual_certificate_digest(rows, combination, residual):
    digest = sha256()
    for index, weight in sorted(combination.items()):
        digest.update(
            (
                f"row{index}:base={uniform.extension_text(weight.value)};"
                f"derivative={uniform.extension_text(weight.derivative)}\n"
            ).encode()
        )
    digest.update(
        (
            f"residual.base={uniform.extension_text(residual.value)}\n"
            f"residual.derivative={uniform.extension_text(residual.derivative)}\n"
        ).encode()
    )
    return digest.hexdigest()


def compose(forms, parameter_forms):
    out = []
    for constant, coefficients in forms:
        value = (constant, {})
        for parameter, coefficient in coefficients.items():
            value = nr.add_affine(value, parameter_forms[parameter], coefficient)
        out.append(value)
    return out


def compile_previous(f1, f2, g1, g2):
    old = base.Q_PRIME
    base.Q_PRIME = Q_PRIME
    try:
        return base.compile_x_previous(f1, f2, g1, g2)
    finally:
        base.Q_PRIME = old


def compile_current(f1, f2, f3, g1, g2, g3):
    old = base.Q_PRIME
    base.Q_PRIME = Q_PRIME
    try:
        return base.compile_x_current(f1, f2, f3, g1, g2, g3)
    finally:
        base.Q_PRIME = old


def compile_pole_previous(p1, q1):
    p = [(Dual(0), {}) for _ in range(7)]
    q = [(Dual(0), {}) for _ in range(11)]
    for degree, coefficient in POLE_F.items():
        p[degree] = (coefficient, {})
    for degree, coefficient in POLE_G.items():
        q[degree] = (coefficient, {})
    rows = []
    for degree in range(14):
        equation = {}
        for i, left in enumerate(p):
            j = degree - i + 1
            if 1 <= j < len(q1):
                equation = nr.add_polynomial(
                    equation,
                    nr.multiply_affine(left, nr.scale_affine(q1[j], Dual(j))),
                    Dual(-3),
                )
        for i, left in enumerate(p1):
            j = degree - i + 1
            if 1 <= j < len(q):
                equation = nr.add_polynomial(
                    equation,
                    nr.multiply_affine(left, nr.scale_affine(q[j], Dual(j))),
                    Dual(-2),
                )
        for i in range(1, len(p)):
            j = degree - (i - 1)
            if 0 <= j < len(q1):
                equation = nr.add_polynomial(
                    equation,
                    nr.multiply_affine(nr.scale_affine(p[i], Dual(i)), q1[j]),
                    Dual(4),
                )
        for i in range(1, len(p1)):
            j = degree - (i - 1)
            if 0 <= j < len(q):
                equation = nr.add_polynomial(
                    equation,
                    nr.multiply_affine(nr.scale_affine(p1[i], Dual(i)), q[j]),
                    Dual(5),
                )
        rows.append(nr.scale_polynomial(equation, Dual(Q(-1, 25))))
    return rows


def main():
    fb.CENTER = (Q(1), Q(1), Q(1))
    fb._X_POWER_CACHE.clear()
    nf, ng, transport = build_transport_rows()
    transport_pivots, records = uniform.mu.factor_matrix(transport)
    transport_rhs, compatibility = propagate(records)
    assert not compatibility
    forms132, free132 = direction_parameterization(
        nf + ng, transport_pivots, transport_rhs
    )
    transport_rank = len(transport_pivots)
    assert (transport_rank, len(free132)) == (3470, 132)
    print("stage transport PASS", flush=True)

    f1 = nr.x_band_forms(15, 60, 1, forms132, 0)
    g1 = nr.x_band_forms(25, 100, 1, forms132, nf)
    first_rows = pack("X-2", first_band_polynomials(f1, g1))
    forms94, free94, first_pivots, first_error, first_dependent = affine_parameterization(
        len(free132), first_rows
    )
    assert first_error is None and (len(first_pivots), len(free94)) == (38, 94)
    replay_affine_rows(first_rows, forms94)
    print("stage first-J PASS", flush=True)

    global94 = compose(forms132, forms94)
    f1 = nr.x_band_forms(15, 60, 1, global94, 0)
    f2 = nr.x_band_forms(15, 60, 2, global94, 0)
    g1 = nr.x_band_forms(25, 100, 1, global94, nf)
    g2 = nr.x_band_forms(25, 100, 2, global94, nf)
    previous = compile_previous(f1, f2, g1, g2)
    p1 = [
        nr.combine_global_linear(nr.pole_coefficient(15, 60, -2, degree), global94, 0)
        for degree in range(61)
    ]
    q1 = [
        nr.combine_global_linear(nr.pole_coefficient(25, 100, -4, degree), global94, nf)
        for degree in range(101)
    ]
    pole = compile_pole_previous(p1, q1)
    previous_rows = pack("X-1", previous) + pack("P1", pole)
    forms56, free56, previous_pivots, previous_error, previous_dependent = affine_parameterization(
        len(free94), previous_rows
    )
    assert previous_error is None and (len(previous_pivots), len(free56)) == (38, 56)
    replay_affine_rows(previous_rows, forms56)
    print("stage previous-paired PASS", flush=True)

    global56 = compose(global94, forms56)
    f1, f2, f3 = [
        nr.x_band_forms(15, 60, exponent, global56, 0)
        for exponent in (1, 2, 3)
    ]
    g1, g2, g3 = [
        nr.x_band_forms(25, 100, exponent, global56, nf)
        for exponent in (1, 2, 3)
    ]
    current = compile_current(f1, f2, f3, g1, g2, g3)
    current_rows = pack("X0", current)
    _, current_pivots, current_error, current_dependent = solve(
        len(free56), current_rows
    )
    assert current_error is not None and current_error[0] == ("X0", 4)
    residual = current_error[1]
    expected = E([
        K([
            Q(2495634, 3625), Q(-4154976, 3625), Q(4405068, 3625),
            Q(-2488119, 3625), Q(761922, 3625), Q(-105084, 3625),
        ]),
        K(Q(136875, 29)),
    ])
    assert residual.value == expected
    tangent_rows = [
        (
            key,
            {variable: coefficient.value for variable, coefficient in row.items() if coefficient.value},
            E(0),
        )
        for key, row, _ in current_rows
        if any(coefficient.value for coefficient in row.values())
    ]
    _, tangent_pivots, tangent_error = fb.exact_solve(
        len(free56), tangent_rows, allow_inconsistent=True
    )
    assert tangent_error is None and len(tangent_pivots) == 25
    certificate_key, certificate_weights, certificate_residual = (
        inconsistency_certificate(current_rows)
    )
    assert certificate_key == current_error[0]
    assert certificate_residual == residual
    lambda_bprime = E(0)
    lambdaprime_b = E(0)
    for index, weight in certificate_weights.items():
        _, _, row_rhs = current_rows[index]
        row_rhs = Dual.coerce(row_rhs)
        lambda_bprime += weight.value * row_rhs.derivative
        lambdaprime_b += weight.derivative * row_rhs.value
    assert lambda_bprime + lambdaprime_b == residual.derivative
    lambda_prime_support = sum(
        bool(weight.derivative) for weight in certificate_weights.values()
    )
    certificate_sha = dual_certificate_digest(
        current_rows, certificate_weights, certificate_residual
    )

    print("TD6-Q2-DUAL-ADJOINT: PASS")
    print("transport_rank = 3470/3602")
    print("first_J_rank = 38/132")
    print("previous_paired_rank = 38/94")
    print(f"current_affine_pivots_before_t4_stop = {len(current_pivots)}/56")
    print("current_homogeneous_rank = 25/56")
    print(f"residual_value = {uniform.extension_text(residual.value)}")
    print(f"residual_q2_derivative = {uniform.extension_text(residual.derivative)}")
    print(f"derivative_nonzero = {bool(residual.derivative)}")
    print(f"derivative.sha256 = {sha256(repr(residual.derivative).encode()).hexdigest()}")
    print(f"lambda_support = {len(certificate_weights)}")
    print(f"lambda_prime_support = {lambda_prime_support}")
    print(f"lambda0_bprime = {uniform.extension_text(lambda_bprime)}")
    print(f"lambdaprime_b0 = {uniform.extension_text(lambdaprime_b)}")
    print(f"dual_left_syzygy.sha256 = {certificate_sha}")
    derivative_only_counts = {
        "first": sum(bool(row) for _, _, row in first_dependent),
        "previous": sum(bool(row) for _, _, row in previous_dependent),
        "current_through_stop": sum(bool(row) for _, _, row in current_dependent),
    }
    print(f"rank_change_flags = {derivative_only_counts}")
    print("verdict = Q2-TRANSVERSE-NONZERO-FIRST-DERIVATIVE")
    print("q2_family_killed = false")
    print("SP2_killed = false")
    print("JC2_resolved = false")


if __name__ == "__main__":
    main()
