#!/usr/bin/env python3
"""Exact three-direction TD6 common-centering tangent pencil.

Private successor.  The base center is (1,1,1), q=t+t^25, and the three
derivatives are dc1,dc2,dc3.  The constant transport echelon is reused; the
matrix derivative is solved exactly against its 132-dimensional affine
kernel before every later Jacobian row is differentiated.
"""

from fractions import Fraction as Q
from hashlib import sha256
import importlib.util
from itertools import combinations
from math import factorial
from pathlib import Path
import sys


REPO = Path("/Users/dc/code/math/jc2")
QDUAL_PATH = REPO / "cases/td6_jet_orbit_adjoint_20260824/replay.py"
QDUAL_SHA256 = "fb138b0f59e611bab365f37c0302418eda485318beec3f6b21237a95fdc41198"


def load(name, path, expected):
    assert sha256(path.read_bytes()).hexdigest() == expected
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


qd = load("td6_qdual_center", QDUAL_PATH, QDUAL_SHA256)
nr, fb, E, K = qd.nr, qd.fb, qd.E, qd.K
ORIGINAL_DUAL = qd.Dual
ND = 3


class MultiDual:
    """E[dc1,dc2,dc3]/(all products of dc's)."""

    __slots__ = ("value", "derivatives")

    def __init__(self, value=0, derivatives=None):
        if isinstance(value, MultiDual):
            self.value = value.value
            self.derivatives = value.derivatives
            return
        self.value = E(value)
        if derivatives is None:
            derivatives = (E(0),) * ND
        assert len(derivatives) == ND
        self.derivatives = tuple(E(entry) for entry in derivatives)

    @staticmethod
    def coerce(value):
        return value if isinstance(value, MultiDual) else MultiDual(value)

    def __add__(self, other):
        other = MultiDual.coerce(other)
        return MultiDual(
            self.value + other.value,
            tuple(a + b for a, b in zip(self.derivatives, other.derivatives)),
        )

    __radd__ = __add__

    def __neg__(self):
        return MultiDual(-self.value, tuple(-entry for entry in self.derivatives))

    def __sub__(self, other):
        return self + (-MultiDual.coerce(other))

    def __rsub__(self, other):
        return MultiDual.coerce(other) - self

    def __mul__(self, other):
        other = MultiDual.coerce(other)
        return MultiDual(
            self.value * other.value,
            tuple(
                left * other.value + self.value * right
                for left, right in zip(self.derivatives, other.derivatives)
            ),
        )

    __rmul__ = __mul__

    def inverse(self):
        if not self.value:
            raise ZeroDivisionError("zero-base multidual pivot")
        inverse = self.value.inverse()
        return MultiDual(
            inverse,
            tuple(-(inverse * inverse) * entry for entry in self.derivatives),
        )

    def __truediv__(self, other):
        return self * MultiDual.coerce(other).inverse()

    def __rtruediv__(self, other):
        return MultiDual.coerce(other) / self

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        out = MultiDual(1)
        base = self
        while exponent:
            if exponent & 1:
                out *= base
            base *= base
            exponent //= 2
        return out

    def __bool__(self):
        return bool(self.value) or any(self.derivatives)

    def __eq__(self, other):
        other = MultiDual.coerce(other)
        return self.value == other.value and self.derivatives == other.derivatives

    def __repr__(self):
        return f"MultiDual({self.value!r};{self.derivatives!r})"


ZERO_FORM = (E(0), {})


def add_form(left, right, scale=1):
    return nr.add_affine(left, right, scale)


def scale_form(form, scale):
    return nr.add_affine(ZERO_FORM, form, scale)


def center_power_data(i):
    """Base and dc1/dc2/dc3 derivatives of x(s,t)^i at center 1,1,1."""
    base = {}
    derivatives = [dict() for _ in range(ND)]
    for kt in range(i + 1):
        for a2 in range(i - kt + 1):
            for a3 in range(i - kt - a2 + 1):
                a1 = i - kt - a2 - a3
                coefficient = Q(
                    factorial(i),
                    factorial(kt)
                    * factorial(a1)
                    * factorial(a2)
                    * factorial(a3),
                )
                key = (i + a2 + 2 * a3 + 3 * kt, kt)
                base[key] = base.get(key, Q(0)) + coefficient
                for direction, exponent in enumerate((a1, a2, a3)):
                    if exponent:
                        derivatives[direction][key] = (
                            derivatives[direction].get(key, Q(0))
                            + exponent * coefficient
                        )
    return base, derivatives


CENTER_POWER = {i: center_power_data(i) for i in range(26)}


def x_chart_row_data(imax, jmax, exponent, tdegree):
    base = {}
    derivatives = [dict() for _ in range(ND)]
    for i in range(imax + 1):
        power_base, power_derivatives = CENTER_POWER[i]
        for (sdegree, found_tdegree), coefficient in power_base.items():
            if found_tdegree != tdegree:
                continue
            j = sdegree - exponent
            if not (0 <= j <= jmax):
                continue
            variable = i * (jmax + 1) + j
            base[variable] = base.get(variable, Q(0)) + coefficient
            for direction in range(ND):
                derivative = power_derivatives[direction].get(
                    (sdegree, found_tdegree), Q(0)
                )
                if derivative:
                    derivatives[direction][variable] = (
                        derivatives[direction].get(variable, Q(0)) + derivative
                    )
    return base, derivatives


def build_transport_derivative_rows(nf):
    base_rows = {}
    derivative_rows = {}
    for owner, imax, jmax, offset in (
        ("f", 15, 60, 0),
        ("g", 25, 100, nf),
    ):
        for i in range(imax + 1):
            power_base, power_derivatives = CENTER_POWER[i]
            for j in range(jmax + 1):
                variable = offset + i * (jmax + 1) + j
                for (sdegree, tdegree), coefficient in power_base.items():
                    exponent = sdegree - j
                    if exponent > 0:
                        continue
                    key = (owner, "X", exponent, tdegree)
                    base_row = base_rows.setdefault(key, {})
                    base_row[variable] = base_row.get(variable, Q(0)) + coefficient
                    rows = derivative_rows.setdefault(
                        key, [dict() for _ in range(ND)]
                    )
                    for direction in range(ND):
                        derivative = power_derivatives[direction].get(
                            (sdegree, tdegree), Q(0)
                        )
                        if derivative:
                            rows[direction][variable] = (
                                rows[direction].get(variable, Q(0)) + derivative
                            )
    return base_rows, derivative_rows


def base_transport_forms():
    fb.CENTER = (Q(1), Q(1), Q(1))
    fb._X_POWER_CACHE.clear()
    nf, ng, transport = qd.build_transport_rows()
    pivots, records = qd.uniform.mu.factor_matrix(transport)
    rhs, compatibility = qd.propagate(records)
    assert not compatibility
    dual_forms, free = qd.direction_parameterization(nf + ng, pivots, rhs)
    assert (len(pivots), len(free)) == (3470, 132)
    forms = [
        (constant.value, dict(coefficients))
        for constant, coefficients in dual_forms
    ]
    base_rows, derivative_rows = build_transport_derivative_rows(nf)
    transport_rows = {key: row for key, row, _ in transport}
    for key, row in base_rows.items():
        assert transport_rows[key] == row, ("transport matrix mismatch", key)
    assert all(key in transport_rows for key in derivative_rows)
    return nf, ng, transport, pivots, records, forms, free, derivative_rows


def derivative_transport_forms(
    nvariables, records, pivots, base_forms, free, derivative_rows
):
    pivot_rhs = {}
    for key, kind, pivot, lead, factors in records:
        values = [ZERO_FORM for _ in range(ND)]
        rows = derivative_rows.get(key)
        if rows is not None:
            values = []
            for direction in range(ND):
                value = ZERO_FORM
                for variable, coefficient in rows[direction].items():
                    value = add_form(value, base_forms[variable], -coefficient)
                values.append(value)
        for old, factor in factors:
            values = [
                add_form(value, pivot_rhs[old][direction], -factor)
                for direction, value in enumerate(values)
            ]
        if kind == "pivot":
            pivot_rhs[pivot] = [scale_form(value, Q(1) / lead) for value in values]
        else:
            assert all(value == ZERO_FORM for value in values), (
                "centering transport compatibility",
                key,
                values,
            )

    free_set = set(free)
    derivatives = [[None] * nvariables for _ in range(ND)]
    for variable in range(nvariables - 1, -1, -1):
        if variable in free_set:
            for direction in range(ND):
                derivatives[direction][variable] = ZERO_FORM
            continue
        for direction in range(ND):
            value = pivot_rhs[variable][direction]
            for other, coefficient in pivots[variable].items():
                if other != variable:
                    value = add_form(
                        value, derivatives[direction][other], -coefficient
                    )
            derivatives[direction][variable] = value
    return derivatives


def combine_row(row, forms, offset=0):
    value = ZERO_FORM
    for variable, coefficient in row.items():
        value = add_form(value, forms[offset + variable], coefficient)
    return value


def multidual_form(base_form, derivative_forms):
    parameters = set(base_form[1])
    for form in derivative_forms:
        parameters.update(form[1])
    return (
        MultiDual(base_form[0], [form[0] for form in derivative_forms]),
        {
            parameter: MultiDual(
                base_form[1].get(parameter, E(0)),
                [form[1].get(parameter, E(0)) for form in derivative_forms],
            )
            for parameter in parameters
            if base_form[1].get(parameter, E(0))
            or any(form[1].get(parameter, E(0)) for form in derivative_forms)
        },
    )


def x_section_forms(imax, jmax, exponent, base_forms, derivative_forms, offset):
    out = []
    for degree in range(imax + 1):
        row, row_derivatives = x_chart_row_data(imax, jmax, exponent, degree)
        assert row == fb.x_chart_coefficient(imax, jmax, exponent, degree)
        base_form = combine_row(row, base_forms, offset)
        derivatives = []
        for direction in range(ND):
            value = combine_row(row, derivative_forms[direction], offset)
            value = add_form(
                value, combine_row(row_derivatives[direction], base_forms, offset)
            )
            derivatives.append(value)
        out.append(multidual_form(base_form, derivatives))
    return out


def pole_section_forms(imax, jmax, exponent, degrees, base_forms, derivative_forms, offset):
    out = []
    for degree in range(degrees):
        row = nr.pole_coefficient(imax, jmax, exponent, degree)
        base_form = combine_row(row, base_forms, offset)
        derivatives = [
            combine_row(row, derivative_forms[direction], offset)
            for direction in range(ND)
        ]
        out.append(multidual_form(base_form, derivatives))
    return out


def solve(nvariables, rows, stop_on_base_inconsistency=True):
    pivots = {}
    dependent = []
    for key, original_row, original_rhs in rows:
        row = {
            variable: MultiDual.coerce(coefficient)
            for variable, coefficient in original_row.items()
        }
        rhs = MultiDual.coerce(original_rhs)
        while True:
            reducible = sorted(
                variable
                for variable, coefficient in row.items()
                if coefficient and variable in pivots
            )
            if not reducible:
                break
            pivot = reducible[0]
            factor = row[pivot]
            old_row, old_rhs = pivots[pivot]
            for variable, coefficient in old_row.items():
                value = row.get(variable, MultiDual()) - factor * coefficient
                if value:
                    row[variable] = value
                else:
                    row.pop(variable, None)
            rhs -= factor * old_rhs
        base_row = {
            variable: coefficient for variable, coefficient in row.items()
            if coefficient.value
        }
        derivative_only = {
            variable: coefficient.derivatives
            for variable, coefficient in row.items()
            if not coefficient.value and any(coefficient.derivatives)
        }
        if not base_row:
            dependent.append((key, rhs, derivative_only))
            if rhs.value and stop_on_base_inconsistency:
                return None, pivots, (key, rhs, derivative_only), dependent
            continue
        pivot = min(base_row)
        lead = row[pivot]
        pivots[pivot] = (
            {variable: coefficient / lead for variable, coefficient in row.items()},
            rhs / lead,
        )
    return {}, pivots, None, dependent


def parameterize(nvariables, rows):
    _, pivots, error, dependent = solve(nvariables, rows)
    if error:
        return None, None, pivots, error, dependent
    free = [variable for variable in range(nvariables) if variable not in pivots]
    parameter_of = {variable: index for index, variable in enumerate(free)}

    base_forms = [None] * nvariables
    for variable in range(nvariables - 1, -1, -1):
        if variable in parameter_of:
            base_forms[variable] = (E(0), {parameter_of[variable]: E(1)})
            continue
        row, rhs = pivots[variable]
        value = (rhs.value, {})
        for other, coefficient in row.items():
            if other != variable and coefficient.value:
                value = add_form(value, base_forms[other], -coefficient.value)
        base_forms[variable] = value

    derivative_forms = [[[None] * nvariables for _ in range(ND)]][0]
    for direction in range(ND):
        for variable in range(nvariables - 1, -1, -1):
            if variable in parameter_of:
                derivative_forms[direction][variable] = ZERO_FORM
                continue
            row, rhs = pivots[variable]
            value = (rhs.derivatives[direction], {})
            for other, coefficient in row.items():
                if other == variable:
                    continue
                if coefficient.value:
                    value = add_form(
                        value,
                        derivative_forms[direction][other],
                        -coefficient.value,
                    )
                if coefficient.derivatives[direction]:
                    value = add_form(
                        value,
                        base_forms[other],
                        -coefficient.derivatives[direction],
                    )
            derivative_forms[direction][variable] = value

    forms = [
        multidual_form(
            base_forms[variable],
            [derivative_forms[d][variable] for d in range(ND)],
        )
        for variable in range(nvariables)
    ]
    for key, row, rhs in rows:
        got = (MultiDual(), {})
        for variable, coefficient in row.items():
            got = nr.add_affine(got, forms[variable], coefficient)
        assert got == (MultiDual.coerce(rhs), {}), ("row replay", key)
    return forms, free, pivots, None, dependent


def compose(forms, parameter_forms):
    out = []
    for constant, coefficients in forms:
        value = (constant, {})
        for parameter, coefficient in coefficients.items():
            value = nr.add_affine(value, parameter_forms[parameter], coefficient)
        out.append(value)
    return out


def certificate(rows):
    pivots = {}
    for index, (key, original_row, original_rhs) in enumerate(rows):
        row = {
            variable: MultiDual.coerce(value)
            for variable, value in original_row.items()
        }
        rhs = MultiDual.coerce(original_rhs)
        combination = {index: MultiDual(1)}
        while True:
            reducible = sorted(
                variable
                for variable, coefficient in row.items()
                if coefficient and variable in pivots
            )
            if not reducible:
                break
            pivot = reducible[0]
            factor = row[pivot]
            old_row, old_rhs, old_combination = pivots[pivot]
            for variable, coefficient in old_row.items():
                value = row.get(variable, MultiDual()) - factor * coefficient
                if value:
                    row[variable] = value
                else:
                    row.pop(variable, None)
            rhs -= factor * old_rhs
            for old_index, coefficient in old_combination.items():
                value = combination.get(old_index, MultiDual()) - factor * coefficient
                if value:
                    combination[old_index] = value
                else:
                    combination.pop(old_index, None)
        base_row = {
            variable: coefficient for variable, coefficient in row.items()
            if coefficient.value
        }
        if not base_row:
            assert not {
                variable: coefficient.derivatives
                for variable, coefficient in row.items()
                if any(coefficient.derivatives)
            }, ("rank change before certificate", key)
            if rhs.value:
                check_row = {}
                check_rhs = MultiDual()
                for old_index, weight in combination.items():
                    _, old_row, old_rhs = rows[old_index]
                    for variable, coefficient in old_row.items():
                        value = check_row.get(variable, MultiDual()) + weight * coefficient
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
    raise AssertionError("no base inconsistency")


def field_matrix_rank(rows, ncolumns):
    """Deterministic row rank over E, with least-column pivots."""
    pivots = {}
    for original in rows:
        row = {
            column: E(value)
            for column, value in enumerate(original)
            if value
        }
        while row:
            pivot = min(row)
            if pivot not in pivots:
                break
            factor = row[pivot]
            old = pivots[pivot]
            for column, coefficient in old.items():
                value = row.get(column, E(0)) - factor * coefficient
                if value:
                    row[column] = value
                else:
                    row.pop(column, None)
        if not row:
            continue
        pivot = min(row)
        lead = row[pivot]
        pivots[pivot] = {
            column: coefficient / lead for column, coefficient in row.items()
        }
    assert all(0 <= column < ncolumns for column in pivots)
    return pivots


def field_kernel(pivots, ncolumns):
    """Kernel basis of the normalized row echelon encoded by pivots."""
    free = [column for column in range(ncolumns) if column not in pivots]
    basis = []
    for generator in free:
        vector = [E(0)] * ncolumns
        vector[generator] = E(1)
        for pivot in sorted(pivots, reverse=True):
            row = pivots[pivot]
            vector[pivot] = -sum(
                coefficient * vector[column]
                for column, coefficient in row.items()
                if column != pivot
            )
        basis.append(vector)
    return basis


def solve_field_affine(rows, rhs, ncolumns):
    """Solve rows*x=rhs over E, returning deterministic solution or None."""
    pivots = {}
    for index, (original, original_rhs) in enumerate(zip(rows, rhs)):
        row = {
            column: E(value)
            for column, value in enumerate(original)
            if value
        }
        value = E(original_rhs)
        while row:
            pivot = min(row)
            if pivot not in pivots:
                break
            factor = row[pivot]
            old_row, old_rhs = pivots[pivot]
            for column, coefficient in old_row.items():
                entry = row.get(column, E(0)) - factor * coefficient
                if entry:
                    row[column] = entry
                else:
                    row.pop(column, None)
            value -= factor * old_rhs
        if not row:
            if value:
                return None, (index, value)
            continue
        pivot = min(row)
        lead = row[pivot]
        pivots[pivot] = (
            {column: coefficient / lead for column, coefficient in row.items()},
            value / lead,
        )
    solution = [E(0)] * ncolumns
    for pivot in sorted(pivots, reverse=True):
        row, value = pivots[pivot]
        solution[pivot] = value - sum(
            coefficient * solution[column]
            for column, coefficient in row.items()
            if column != pivot
        )
    return solution, None


def field_determinant(matrix):
    """Exact determinant over E with deterministic least-row pivots."""
    matrix = [list(row) for row in matrix]
    size = len(matrix)
    assert all(len(row) == size for row in matrix)
    determinant = E(1)
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if matrix[row][column]),
            None,
        )
        if pivot is None:
            return E(0)
        if pivot != column:
            matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
            determinant = -determinant
        lead = matrix[column][column]
        determinant *= lead
        matrix[column] = [entry / lead for entry in matrix[column]]
        for row in range(column + 1, size):
            factor = matrix[row][column]
            if factor:
                matrix[row] = [
                    left - factor * right
                    for left, right in zip(matrix[row], matrix[column])
                ]
    return determinant


def first_nonzero_maximal_minor(rows, size):
    """Return lexicographically first nonzero size-by-size row minor."""
    if not size:
        return (), E(1)
    assert rows and len(rows[0]) == size
    for indices in combinations(range(len(rows)), size):
        determinant = field_determinant([rows[index] for index in indices])
        if determinant:
            return indices, determinant
    return None, E(0)


def configure_multidual():
    qd.Dual = MultiDual
    qd.B = MultiDual(0)
    qd.S = MultiDual(qd.uniform.S_FIELD)
    qd.D = MultiDual(qd.uniform.D_FIELD)
    qd.L = MultiDual(qd.uniform.L_FIELD)
    qd.A = MultiDual(qd.uniform.A_FIELD)
    qd.Q_PRIME = {0: MultiDual(1), 24: MultiDual(25)}
    qd.R = qd.multiply(
        qd.multiply([MultiDual(-1), MultiDual(1)], [MultiDual(-1), MultiDual(1)]),
        [qd.D, -qd.S, MultiDual(1)],
    )
    qd.R3, qd.R5 = qd.power(qd.R, 3), qd.power(qd.R, 5)
    qd.POLE_F = {1: -(qd.L**3) * qd.A, 6: qd.L**3}
    qd.POLE_G = {
        0: MultiDual(Q(5, 9)) * qd.L**5 * qd.A**2,
        5: MultiDual(Q(-5, 3)) * qd.L**5 * qd.A,
        10: qd.L**5,
    }


def main():
    (
        nf, ng, transport, transport_pivots, records,
        forms132_base, free132, transport_derivative_rows,
    ) = base_transport_forms()
    derivative_forms = derivative_transport_forms(
        nf + ng,
        records,
        transport_pivots,
        forms132_base,
        free132,
        transport_derivative_rows,
    )
    print("center transport tangent PASS", flush=True)

    configure_multidual()
    bands132 = {
        (owner, exponent): x_section_forms(
            15 if owner == "f" else 25,
            60 if owner == "f" else 100,
            exponent,
            forms132_base,
            derivative_forms,
            0 if owner == "f" else nf,
        )
        for owner in ("f", "g")
        for exponent in (1, 2, 3)
    }
    pole_f132 = pole_section_forms(
        15, 60, -2, 61, forms132_base, derivative_forms, 0
    )
    pole_g132 = pole_section_forms(
        25, 100, -4, 101, forms132_base, derivative_forms, nf
    )

    first_rows = qd.pack(
        "X-2",
        qd.first_band_polynomials(bands132[("f", 1)], bands132[("g", 1)]),
    )
    forms94, free94, first_pivots, first_error, first_dependent = parameterize(
        132, first_rows
    )
    assert first_error is None and (len(first_pivots), len(free94)) == (38, 94)
    print("center first-J tangent PASS", flush=True)

    bands94 = {key: compose(forms, forms94) for key, forms in bands132.items()}
    previous_rows = qd.pack(
        "X-1",
        qd.compile_previous(
            bands94[("f", 1)], bands94[("f", 2)],
            bands94[("g", 1)], bands94[("g", 2)],
        ),
    )
    previous_rows += qd.pack(
        "P1",
        qd.compile_pole_previous(
            compose(pole_f132, forms94), compose(pole_g132, forms94)
        ),
    )
    forms56, free56, previous_pivots, previous_error, previous_dependent = parameterize(
        94, previous_rows
    )
    assert previous_error is None and (len(previous_pivots), len(free56)) == (38, 56)
    print("center previous/pole tangent PASS", flush=True)

    bands56 = {key: compose(forms, forms56) for key, forms in bands94.items()}
    current_rows = qd.pack(
        "X0",
        qd.compile_current(
            *[bands56[("f", exponent)] for exponent in (1, 2, 3)],
            *[bands56[("g", exponent)] for exponent in (1, 2, 3)],
        ),
    )
    _, current_pivots, current_error, current_dependent = solve(56, current_rows)
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
    certificate_key, weights, certificate_residual = certificate(current_rows)
    assert certificate_key == ("X0", 4) and certificate_residual == residual

    # The first t^4 obstruction is only one row in the current-band
    # cokernel.  Reduce every dependent row against the same deterministic
    # base echelon before deciding whether the three center directions have
    # a joint invisible subspace or a common linearized root.
    (
        _, current_pivots_full, current_error_full, current_dependent_full,
    ) = solve(56, current_rows, stop_on_base_inconsistency=False)
    assert current_error_full is None
    assert len(current_pivots_full) == 25
    assert len(current_dependent_full) == len(current_rows) - 25
    assert all(not derivative_only for _, _, derivative_only in current_dependent_full)
    compatibility_keys = [key for key, _, _ in current_dependent_full]
    compatibility_base = [entry.value for _, entry, _ in current_dependent_full]
    compatibility_derivatives = [
        list(entry.derivatives) for _, entry, _ in current_dependent_full
    ]
    compatibility_pivots = field_matrix_rank(compatibility_derivatives, ND)
    compatibility_kernel = field_kernel(compatibility_pivots, ND)
    compatibility_rank = len(compatibility_pivots)
    compatibility_minor_rows = compatibility_derivatives
    compatibility_minor_indices, compatibility_minor = (
        first_nonzero_maximal_minor(
            [
                [row[column] for column in sorted(compatibility_pivots)]
                for row in compatibility_minor_rows
            ],
            compatibility_rank,
        )
    )
    augmented_rows = [
        row + [-base]
        for row, base in zip(compatibility_derivatives, compatibility_base)
    ]
    augmented_pivots = field_matrix_rank(augmented_rows, ND + 1)
    augmented_rank = len(augmented_pivots)
    augmented_columns = sorted(augmented_pivots)
    augmented_minor_indices, augmented_minor = first_nonzero_maximal_minor(
        [
            [row[column] for column in augmented_columns]
            for row in augmented_rows
        ],
        augmented_rank,
    )
    linearized_root, linearized_root_error = solve_field_affine(
        compatibility_derivatives,
        [-entry for entry in compatibility_base],
        ND,
    )

    for row, base in zip(compatibility_derivatives, compatibility_base):
        for vector in compatibility_kernel:
            assert sum(a * b for a, b in zip(row, vector)) == 0
        if linearized_root is not None:
            assert base + sum(a * b for a, b in zip(row, linearized_root)) == 0

    tangent_rows = [
        (
            key,
            {
                variable: coefficient.value
                for variable, coefficient in row.items()
                if coefficient.value
            },
            E(0),
        )
        for key, row, _ in current_rows
        if any(coefficient.value for coefficient in row.values())
    ]
    _, tangent_pivots, tangent_error = fb.exact_solve(
        56, tangent_rows, allow_inconsistent=True
    )
    assert tangent_error is None and len(tangent_pivots) == 25

    digest = sha256()
    for index, weight in sorted(weights.items()):
        digest.update(f"row{index}:base={qd.uniform.extension_text(weight.value)}\n".encode())
        for direction, derivative in enumerate(weight.derivatives):
            digest.update(
                f"row{index}:dc{direction+1}={qd.uniform.extension_text(derivative)}\n".encode()
            )
    digest.update(f"residual={residual!r}\n".encode())

    compatibility_digest = sha256()
    for key, base, derivatives in zip(
        compatibility_keys, compatibility_base, compatibility_derivatives
    ):
        compatibility_digest.update(f"{key}:base={repr(base)}\n".encode())
        for direction, derivative in enumerate(derivatives):
            compatibility_digest.update(
                f"{key}:dc{direction+1}={repr(derivative)}\n".encode()
            )

    rank_flags = {
        "first": [
            sum(
                any(entry[direction] for entry in derivative_only.values())
                for _, _, derivative_only in first_dependent
            )
            for direction in range(ND)
        ],
        "previous": [
            sum(
                any(entry[direction] for entry in derivative_only.values())
                for _, _, derivative_only in previous_dependent
            )
            for direction in range(ND)
        ],
        "current_through_stop": [
            sum(
                any(entry[direction] for entry in derivative_only.values())
                for _, _, derivative_only in current_dependent
            )
            for direction in range(ND)
        ],
        "current_full": [
            sum(
                any(entry[direction] for entry in derivative_only.values())
                for _, _, derivative_only in current_dependent_full
            )
            for direction in range(ND)
        ],
    }

    print("TD6-CENTERING-MATRIX-TANGENT: PASS")
    print("transport_rank = 3470/3602; dimension=132")
    print("first_J_rank = 38/132; dimension=94")
    print("previous_pole_rank = 38/94; dimension=56")
    print(f"current_homogeneous_rank = {len(tangent_pivots)}/56")
    print(f"current_pivots_before_t4 = {len(current_pivots)}/56")
    print(f"residual_value = {qd.uniform.extension_text(residual.value)}")
    for direction, derivative in enumerate(residual.derivatives):
        print(
            f"residual_dc{direction+1} = "
            f"{qd.uniform.extension_text(derivative)}"
        )
        print(f"residual_dc{direction+1}_nonzero = {bool(derivative)}")
        print(
            f"residual_dc{direction+1}.sha256 = "
            f"{sha256(repr(derivative).encode()).hexdigest()}"
        )
    print(f"left_null_support = {len(weights)}")
    print(f"left_null_multidual.sha256 = {digest.hexdigest()}")
    print(f"current_compatibility_dimension = {len(current_dependent_full)}")
    print(f"centering_joint_image_rank_over_E = {compatibility_rank}")
    print(f"centering_joint_kernel_dimension_over_E = {len(compatibility_kernel)}")
    print(f"centering_joint_augmented_rank_over_E = {augmented_rank}")
    print(
        "centering_joint_rank_minor_rows = "
        f"{tuple(compatibility_keys[index] for index in compatibility_minor_indices)}"
    )
    print(
        "centering_joint_rank_minor = "
        f"{qd.uniform.extension_text(compatibility_minor)}"
    )
    print(
        "centering_joint_rank_minor.sha256 = "
        f"{sha256(repr(compatibility_minor).encode()).hexdigest()}"
    )
    print(
        "centering_joint_augmented_minor_rows = "
        f"{tuple(compatibility_keys[index] for index in augmented_minor_indices)}"
    )
    print(
        "centering_joint_augmented_minor = "
        f"{qd.uniform.extension_text(augmented_minor)}"
    )
    print(
        "centering_joint_augmented_minor.sha256 = "
        f"{sha256(repr(augmented_minor).encode()).hexdigest()}"
    )
    print(
        "centering_joint_linearized_root_exists = "
        f"{linearized_root is not None}"
    )
    if linearized_root is not None:
        for direction, entry in enumerate(linearized_root):
            print(
                f"centering_joint_linearized_root_dc{direction+1} = "
                f"{qd.uniform.extension_text(entry)}"
            )
    else:
        assert linearized_root_error is not None
        print(f"centering_joint_linearized_root_failure_row = {linearized_root_error[0]}")
        print(
            "centering_joint_linearized_root_failure_residual = "
            f"{qd.uniform.extension_text(linearized_root_error[1])}"
        )
    for generator, vector in enumerate(compatibility_kernel):
        for direction, entry in enumerate(vector):
            print(
                f"centering_joint_kernel_{generator}_dc{direction+1} = "
                f"{qd.uniform.extension_text(entry)}"
            )
    print(
        "current_compatibility_multidual.sha256 = "
        f"{compatibility_digest.hexdigest()}"
    )
    print(f"rank_change_flags = {rank_flags}")
    print("centering_quotient_rank = 3")
    print("centering_family_killed = false")
    print("SP2_killed = false")
    print("JC2_resolved = false")


if __name__ == "__main__":
    main()
