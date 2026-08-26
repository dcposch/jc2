#!/usr/bin/env python3
"""Exact generic-center joint TD6 transport source compiler (V81B).

This is the first stage of the 33-axis successor.  It works over the single
square-zero ring with axes

  q2..q14,q16..q24,d6..d16

over E(C,V,U).  The q axes change the affine transport RHS and the dead
stretch axes change the pole transport matrix.  All eleven dead columns are
assembled before the exact joint rank/kernel is computed.  The calculation
is transport-only: it does not claim a first/previous/current or nonlinear
Kuranishi result.
"""

from fractions import Fraction as Q
from hashlib import sha256
import importlib.util
from math import comb
import os
from pathlib import Path
import platform
import socket
import sys


HERE = Path(__file__).resolve().parent
ALLQ_PATH = (
    HERE.parent / "td6_c1_c2_c3_all_q_vector_ad_repaired_20260825"
    / "replay.py"
)
ALLQ_SHA256 = "7e5ade2b0f8723e2ac502978fd8ea48470e57231a83c8e8c0a233f64948b695d"
assert sha256(ALLQ_PATH.read_bytes()).hexdigest() == ALLQ_SHA256
spec = importlib.util.spec_from_file_location("td6_v81a_allq_parent", ALLQ_PATH)
allq = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = allq
spec.loader.exec_module(allq)

r, tri = allq.r, allq.tri
Rat3, E3 = allq.Rat3, allq.E3
C, V, U, B3, H = allq.C, allq.V, allq.U, allq.B3, allq.H
nr = allq.nr

Q_LEVELS = allq.Q_EXPONENTS
DEAD_LEVELS = tuple(range(6, 17))
Q_AXES = tuple(f"q{level}" for level in Q_LEVELS)
DEAD_AXES = tuple(f"d{level}" for level in DEAD_LEVELS)
AXES = Q_AXES + DEAD_AXES
assert len(Q_AXES) == 22 and len(DEAD_AXES) == 11 and len(AXES) == 33
assert len(set(AXES)) == 33 and "q15" not in AXES

EXPECTED_POINT_TABLE = {
    6: "df2eae2216967197e159e77e2b6709811f366f3baea307bb4febb4b53e3ffd07",
    7: "f067674ed1c0516be4eeef68646e5a827bed68f99449942bed1a0721338f7ca0",
    8: "a69aef0562e43b12c788b9390dc9424bc188b495d035c7910e6b7b1be7a89fce",
    9: "b77be35ba8072970e1e7318752950a2660d8a9c191256ae5545896798031cb03",
    10: "a30f85978bc937ca998bb0c9cb299171b0a39e1e7de406ae7d7166c80bcee1df",
    11: "637cbc2485629bdbb929af8c8de435febb4be400ef2a18883c4ebc56a8797437",
    12: "9376efbfe6b0c53c26bd919025399d6d16c9c1c40295dc1080e72fd085ab879c",
    13: "06cfdd710b7fc22c495c880239f8dde69d96291c9e2145ea8401bd339009f4a2",
    14: "aee20602cbaa65f2d6a12ad9b7b7fb48b63e724f68c8df2440e2b89bf19c991b",
    15: "a30f85978bc937ca998bb0c9cb299171b0a39e1e7de406ae7d7166c80bcee1df",
    16: "7e40146215fb5416235c7ab9b3aa57c84a62147ca0a34e47797b93c48796022a",
}


class AxisJet:
    """E(C,V,U) plus a square-zero derivative for every licensed axis."""

    __slots__ = ("value", "derivatives")

    def __init__(self, value=0, derivatives=None):
        if isinstance(value, AxisJet):
            self.value = value.value
            self.derivatives = dict(value.derivatives)
        else:
            self.value = E3.coerce(value)
            self.derivatives = {}
        if derivatives:
            for axis, coefficient in derivatives.items():
                assert axis in AXES
                coefficient = E3.coerce(coefficient)
                total = self.derivatives.get(axis, E3()) + coefficient
                if total:
                    self.derivatives[axis] = total
                else:
                    self.derivatives.pop(axis, None)

    @staticmethod
    def coerce(value):
        return value if isinstance(value, AxisJet) else AxisJet(value)

    @staticmethod
    def direction(axis, coefficient=1):
        return AxisJet(0, {axis: coefficient})

    def __add__(self, other):
        other = AxisJet.coerce(other)
        derivatives = dict(self.derivatives)
        for axis, coefficient in other.derivatives.items():
            value = derivatives.get(axis, E3()) + coefficient
            if value:
                derivatives[axis] = value
            else:
                derivatives.pop(axis, None)
        return AxisJet(self.value + other.value, derivatives)

    __radd__ = __add__

    def __neg__(self):
        return AxisJet(-self.value, {
            axis: -coefficient for axis, coefficient in self.derivatives.items()
        })

    def __sub__(self, other):
        return self + (-AxisJet.coerce(other))

    def __rsub__(self, other):
        return AxisJet.coerce(other) - self

    def __mul__(self, other):
        other = AxisJet.coerce(other)
        derivatives = {}
        for axis in self.derivatives.keys() | other.derivatives.keys():
            coefficient = (
                self.derivatives.get(axis, E3()) * other.value
                + self.value * other.derivatives.get(axis, E3())
            )
            if coefficient:
                derivatives[axis] = coefficient
        return AxisJet(self.value * other.value, derivatives)

    __rmul__ = __mul__

    def inverse(self):
        if not self.value:
            raise ZeroDivisionError("zero-base square-zero pivot")
        inverse = self.value.inverse()
        return AxisJet(inverse, {
            axis: -(inverse * inverse) * coefficient
            for axis, coefficient in self.derivatives.items()
        })

    def __truediv__(self, other):
        return self * AxisJet.coerce(other).inverse()

    def __rtruediv__(self, other):
        return AxisJet.coerce(other) / self

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        out, base = AxisJet(1), self
        while exponent:
            if exponent & 1:
                out *= base
            base *= base
            exponent //= 2
        return out

    def __bool__(self):
        return bool(self.value) or bool(self.derivatives)

    def __eq__(self, other):
        other = AxisJet.coerce(other)
        return self.value == other.value and self.derivatives == other.derivatives


ZERO_FORM = (E3(), {})


def scalar(value):
    return E3(tri.FIELD.scalar(Rat3.coerce(value)))


def from_vector(vector):
    return E3(tri.FIELD.from_coordinates(vector))


def add_form(left, right, scale=1):
    scale = E3.coerce(scale)
    constant = left[0] + scale * right[0]
    row = dict(left[1])
    for parameter, coefficient in right[1].items():
        value = row.get(parameter, E3()) + scale * coefficient
        if value:
            row[parameter] = value
        else:
            row.pop(parameter, None)
    return constant, row


def add_jet_form(left, right, scale=1):
    scale = AxisJet.coerce(scale)
    constant = left[0] + scale * right[0]
    row = dict(left[1])
    for parameter, coefficient in right[1].items():
        value = row.get(parameter, AxisJet()) + scale * coefficient
        if value:
            row[parameter] = value
        else:
            row.pop(parameter, None)
    return constant, row


def base_form(form):
    return (
        AxisJet.coerce(form[0]).value,
        {
            parameter: AxisJet.coerce(coefficient).value
            for parameter, coefficient in form[1].items()
            if AxisJet.coerce(coefficient).value
        },
    )


def combine_row(row, forms):
    out = ZERO_FORM
    for variable, coefficient in row.items():
        out = add_form(out, forms[variable], scalar(coefficient))
    return out


def build_base_transport():
    expected = (Rat3(C), Rat3(V), Rat3(U))
    assert expected != (Rat3(1), Rat3(1), Rat3(1))
    assert expected[0].numerator == C
    assert expected[1].numerator == V
    assert expected[2].numerator == U
    r.fb.CENTER = expected
    r.fb._X_POWER_CACHE.clear()
    assert r.fb.CENTER == expected
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
    pivots, records, events, _ = tri.factor_transport(ordered)
    assert len(pivots) == 3470 and len(pivots) + 132 == nf + ng
    assert r.fb.CENTER == expected
    print("symbolic_center_asserted_before_transport=true")
    print("symbolic_center_asserted_after_transport=true")
    print(f"transport_rank={len(pivots)}/{nf+ng};free=132")
    print(f"transport_event_count={len(events)}", flush=True)
    return nf, ng, ordered, pivots, records


def source_jet(key):
    base = from_vector(r.t.source_vector(key))
    derivatives = {}
    if len(key) == 4 and key[:3] == ('g', 'X', 0):
        exponent = key[3]
        if exponent in Q_LEVELS:
            derivatives[f"q{exponent}"] = E3(1)
    return AxisJet(base, derivatives)


def propagate_q(rows, records):
    pivot_rhs, compatibility = {}, []
    for source, record in zip(rows, records):
        source_key, _, _ = source
        key, kind, pivot, lead, factors = record
        assert source_key == key
        value = source_jet(key)
        for old, factor in factors:
            # Keep AxisJet on the left: E3 deliberately knows nothing about
            # the square-zero extension, while AxisJet coerces E3 scalars.
            value -= pivot_rhs[old] * scalar(factor)
        if kind == "pivot":
            pivot_rhs[pivot] = value / scalar(lead)
        elif value:
            compatibility.append((key, value))
    assert not compatibility
    active = sorted({
        axis
        for value in pivot_rhs.values()
        for axis in value.derivatives
    })
    assert active == sorted(Q_AXES)
    return pivot_rhs


def global_q_forms(nvariables, pivots, pivot_rhs):
    free = [variable for variable in range(nvariables) if variable not in pivots]
    parameter_of = {variable: index for index, variable in enumerate(free)}
    forms = [None] * nvariables
    for variable in range(nvariables - 1, -1, -1):
        if variable in parameter_of:
            forms[variable] = (
                AxisJet(), {parameter_of[variable]: AxisJet(1)}
            )
            continue
        form = (pivot_rhs[variable], {})
        for other, coefficient in pivots[variable].items():
            if other != variable:
                assert other > variable and forms[other] is not None
                form = add_jet_form(form, forms[other], -scalar(coefficient))
        forms[variable] = form
    return forms, free


def dead_derivative_rows(level, nf):
    rows, term_count = {}, 0
    for owner, imax, jmax, offset, cutoff in (
        ("f", 15, 60, 0, -3),
        ("g", 25, 100, nf, -5),
    ):
        for i in range(imax + 1):
            for j in range(1, jmax + 1):
                variable = offset + i * (jmax + 1) + j
                base = -25 * i + 5 * j
                for zeta_degree in range(j):
                    exponent = base + (level - 5) + 12 * zeta_degree
                    if exponent > cutoff:
                        break
                    coefficient = Rat3(Q(j * comb(j - 1, zeta_degree)))
                    key = (owner, "F0", exponent, zeta_degree)
                    row = rows.setdefault(key, {})
                    row[variable] = row.get(variable, Rat3()) + coefficient
                    term_count += 1
    rows = {
        key: {variable: coefficient for variable, coefficient in row.items() if coefficient}
        for key, row in rows.items() if any(row.values())
    }
    f_variable = 2 * 61 + 3
    assert rows[("f", "F0", -35 + level - 5, 0)][f_variable] == Rat3(3)
    assert rows[("f", "F0", -35 + level - 5 + 12, 1)][f_variable] == Rat3(6)
    wrong = ("f", "F0", -35 + level - 4, 0)
    assert rows.get(wrong, {}).get(f_variable, Rat3()) != Rat3(3)
    return rows, term_count


def dead_lift(level, rows, records, pivots, q_forms, derivative_rows):
    base_forms = [base_form(form) for form in q_forms]
    pivot_rhs, compatibility = {}, []
    record_keys, pivot_keys = set(), set()
    for source, record in zip(rows, records):
        source_key, _, _ = source
        key, kind, pivot, lead, factors = record
        assert source_key == key
        record_keys.add(key)
        value = ZERO_FORM
        if key in derivative_rows:
            value = add_form(value, combine_row(derivative_rows[key], base_forms), -1)
        for old, factor in factors:
            value = add_form(value, pivot_rhs[old], -scalar(factor))
        if kind == "pivot":
            pivot_keys.add(key)
            pivot_rhs[pivot] = add_form(ZERO_FORM, value, scalar(lead).inverse())
        elif value != ZERO_FORM:
            compatibility.append((key, value, "base-dependent"))

    for key in sorted(set(derivative_rows) - record_keys):
        value = add_form(ZERO_FORM, combine_row(derivative_rows[key], base_forms), -1)
        if value != ZERO_FORM:
            compatibility.append((key, value, "derivative-only"))

    free = [variable for variable in range(len(q_forms)) if variable not in pivots]
    free_set = set(free)
    derivatives = [None] * len(q_forms)
    for variable in range(len(q_forms) - 1, -1, -1):
        if variable in free_set:
            derivatives[variable] = ZERO_FORM
            continue
        value = pivot_rhs[variable]
        for other, coefficient in pivots[variable].items():
            if other != variable:
                value = add_form(value, derivatives[other], -scalar(coefficient))
        derivatives[variable] = value

    base_rows = {key: row for key, row, _ in rows}
    replay_count = 0
    for key in pivot_keys:
        got = combine_row(base_rows[key], derivatives)
        if key in derivative_rows:
            got = add_form(got, combine_row(derivative_rows[key], base_forms))
        assert got == ZERO_FORM, ("original differentiated pivot row", level, key)
        replay_count += 1
    assert replay_count == len(pivots)
    omission_failures = sum(
        combine_row(row, base_forms) != ZERO_FORM for row in derivative_rows.values()
    )
    assert omission_failures > 0
    return derivatives, compatibility, omission_failures


def insert_dead_axis(q_forms, dead_derivatives):
    out = []
    for level in DEAD_LEVELS:
        axis = f"d{level}"
        derivatives = dead_derivatives[level]
        assert len(derivatives) == len(q_forms)
        for index, ((q_constant, q_row), (d_constant, d_row)) in enumerate(
            zip(q_forms, derivatives)
        ):
            if level == DEAD_LEVELS[0]:
                out.append((AxisJet(q_constant), {
                    parameter: AxisJet(coefficient)
                    for parameter, coefficient in q_row.items()
                }))
            constant, row = out[index]
            constant = AxisJet(constant, {axis: d_constant})
            row = dict(row)
            for parameter in row.keys() | d_row.keys():
                coefficient = row.get(parameter, AxisJet())
                derivative = d_row.get(parameter, E3())
                coefficient = AxisJet(coefficient, {axis: derivative})
                if coefficient:
                    row[parameter] = coefficient
                else:
                    row.pop(parameter, None)
            out[index] = (constant, row)
    assert len(out) == len(q_forms)
    return out


def compatibility_coordinates(by_level):
    coordinates = {}
    for level, forms in by_level.items():
        axis = f"d{level}"
        for key, (constant, row), kind in forms:
            if constant:
                coordinates.setdefault((kind, repr(key), "constant"), {})[axis] = constant
            for parameter, coefficient in row.items():
                if coefficient:
                    coordinates.setdefault(
                        (kind, repr(key), f"p{parameter}"), {}
                    )[axis] = coefficient
    return coordinates


def exact(value):
    return repr(r.scalar_exact(E3.coerce(value)))


def write_generic_axis(outdir, level, forms):
    lines = ["kind\tkey\tcoordinate\tcoefficient_exact"]
    for key, (constant, coefficients), kind in sorted(
        forms, key=lambda item: (item[0], item[2])
    ):
        if constant:
            lines.append(f"{kind}\t{key!r}\tconstant\t{exact(constant)}")
        for parameter, coefficient in sorted(coefficients.items()):
            if coefficient:
                lines.append(f"{kind}\t{key!r}\tp{parameter}\t{exact(coefficient)}")
    text = "\n".join(lines) + "\n"
    path = outdir / f"GENERIC_DEAD_D{level}_TRANSPORT_COMPATIBILITY.tsv"
    path.write_text(text)
    return path, sha256(text.encode()).hexdigest(), len(lines) - 1


def evaluate_poly_at_one(poly):
    return sum((Q(str(coefficient)) for coefficient in poly.to_dict().values()), Q(0))


def specialize_rat3_at_one(value):
    value = Rat3.coerce(value)
    numerator = evaluate_poly_at_one(value.numerator)
    denominator = evaluate_poly_at_one(value.denominator)
    assert denominator
    return numerator / denominator


def specialize_e3_at_one(value):
    value = E3.coerce(value).value
    coordinates = [
        specialize_rat3_at_one(coordinate)
        for k_value in value.coefficients
        for coordinate in k_value.coordinates
    ]
    assert len(coordinates) == 18
    old_k = allq.qd.uniform.K
    old_e = allq.qd.uniform.E
    return old_e([
        old_k(coordinates[index:index + 6])
        for index in range(0, 18, 6)
    ])


def point_table(level, forms, outdir):
    old_text = allq.qd.uniform.extension_text
    lines = ["kind\tkey\tcoordinate\tcoefficient_exact"]
    for key, (constant, coefficients), kind in sorted(
        forms, key=lambda item: (item[0], item[2])
    ):
        constant = specialize_e3_at_one(constant)
        if constant:
            lines.append(f"{kind}\t{key!r}\tconstant\t{old_text(constant)}")
        for parameter, coefficient in sorted(coefficients.items()):
            coefficient = specialize_e3_at_one(coefficient)
            if coefficient:
                lines.append(f"{kind}\t{key!r}\tp{parameter}\t{old_text(coefficient)}")
    text = "\n".join(lines) + "\n"
    digest = sha256(text.encode()).hexdigest()
    assert digest == EXPECTED_POINT_TABLE[level], (level, digest)
    path = outdir / f"POINT_CVU111_DEAD_D{level}_TRANSPORT_COMPATIBILITY.tsv"
    path.write_text(text)
    return path, digest


def rref(matrix):
    matrix = [list(row) for row in matrix]
    nrows = len(matrix)
    ncols = len(matrix[0]) if matrix else len(AXES)
    pivot_columns, row_index = [], 0
    for column in range(ncols):
        pivot = next(
            (index for index in range(row_index, nrows) if matrix[index][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[row_index], matrix[pivot] = matrix[pivot], matrix[row_index]
        inverse = matrix[row_index][column].inverse()
        matrix[row_index] = [entry * inverse for entry in matrix[row_index]]
        for index in range(nrows):
            if index == row_index or not matrix[index][column]:
                continue
            factor = matrix[index][column]
            matrix[index] = [
                left - factor * right
                for left, right in zip(matrix[index], matrix[row_index])
            ]
        pivot_columns.append(column)
        row_index += 1
        if row_index == nrows:
            break
    return matrix, pivot_columns


def write_joint(outdir, coordinates):
    ordered = sorted(coordinates)
    matrix = [
        [coordinates[key].get(axis, E3()) for axis in AXES]
        for key in ordered
    ]
    reduced, pivots = rref(matrix)
    free = [column for column in range(len(AXES)) if column not in pivots]
    kernel = []
    for free_column in free:
        vector = [E3() for _ in AXES]
        vector[free_column] = E3(1)
        for row_index, pivot_column in enumerate(pivots):
            vector[pivot_column] = -reduced[row_index][free_column]
        kernel.append(vector)
    for vector in kernel:
        assert all(
            not sum((a * b for a, b in zip(row, vector)), E3())
            for row in matrix
        )
    lines = ["kind\tkey\tcoordinate\taxis\tcoefficient_sha256\tcoefficient_exact"]
    for key in ordered:
        kind, source_key, coordinate = key
        for axis in AXES:
            coefficient = coordinates[key].get(axis, E3())
            if coefficient:
                lines.append(
                    f"{kind}\t{source_key}\t{coordinate}\t{axis}\t"
                    f"{allq.e3_digest(coefficient)}\t{exact(coefficient)}"
                )
    table = "\n".join(lines) + "\n"
    table_path = outdir / "JOINT_33_AXIS_TRANSPORT_CONORMAL.tsv"
    table_path.write_text(table)
    kernel_lines = ["kernel_vector\taxis\tcoefficient_sha256\tcoefficient_exact"]
    for vector_index, vector in enumerate(kernel):
        for axis, coefficient in zip(AXES, vector):
            if coefficient:
                kernel_lines.append(
                    f"{vector_index}\t{axis}\t{allq.e3_digest(coefficient)}\t"
                    f"{exact(coefficient)}"
                )
    kernel_text = "\n".join(kernel_lines) + "\n"
    kernel_path = outdir / "JOINT_33_AXIS_TRANSPORT_KERNEL.tsv"
    kernel_path.write_text(kernel_text)
    denominator = allq.denominator_for(
        [entry for row in matrix for entry in row if entry]
        + [entry for vector in kernel for entry in vector if entry]
    )
    allowed = allq.factors_only_allowed(denominator)
    return {
        "coordinate_count": len(ordered),
        "rank": len(pivots),
        "kernel_dimension": len(kernel),
        "pivot_axes": [AXES[column] for column in pivots],
        "table_path": table_path,
        "table_sha": sha256(table.encode()).hexdigest(),
        "kernel_path": kernel_path,
        "kernel_sha": sha256(kernel_text.encode()).hexdigest(),
        "denominator": denominator,
        "allowed": allowed,
    }


def main():
    assert platform.system() == "Linux", "AWS-only producer refuses non-Linux"
    tag = os.environ.get("AWS_RUN_TAG", "")
    assert tag.startswith("td6_v81b_") and len(tag) > len("td6_v81b_")
    outdir = Path(os.environ["TD6_OUTPUT_DIR"]).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    print("producer=TD6-A3-Q-DEAD-JOINT-TRANSPORT-V81B")
    print(f"aws_hostname={socket.gethostname()}")
    print(f"aws_run_tag={tag}")
    print("ring=E(C,V,U)[eps_q2,...,eps_q24,eps_d6,...,eps_d16]/(all_eps_products)")
    print("q_axes=" + ",".join(Q_AXES))
    print("dead_axes=" + ",".join(DEAD_AXES))
    print("q15_target_shear_gauge_excluded=true")
    print("base_beta=0;base_dead_stretch=0")
    print("scope=generic_center_transport_source_incidence_only")
    print("V80B_use=specialization_control_only")
    print("no_first_previous_current_or_kuranishi_claim=true", flush=True)

    nf, ng, rows, pivots, records = build_base_transport()
    q_rhs = propagate_q(rows, records)
    q_forms, free = global_q_forms(nf + ng, pivots, q_rhs)
    assert len(free) == 132
    print("all_22_q_axes_same_square_zero_ring=true")
    print("all_22_q_transport_columns_consistent=true", flush=True)

    by_level, dead_derivatives = {}, {}
    for level in DEAD_LEVELS:
        derivative_rows, term_count = dead_derivative_rows(level, nf)
        derivatives, compatibility, omission_failures = dead_lift(
            level, rows, records, pivots, q_forms, derivative_rows
        )
        by_level[level] = compatibility
        dead_derivatives[level] = derivatives
        generic_path, generic_sha, entries = write_generic_axis(
            outdir, level, compatibility
        )
        point_path, point_sha = point_table(level, compatibility, outdir)
        print(
            f"d{level}_derivative_rows={len(derivative_rows)};"
            f"terms={term_count};omission_failures={omission_failures};"
            f"compatibility_forms={len(compatibility)};entries={entries};"
            f"generic_sha={generic_sha};point_sha={point_sha}"
        )
        print(f"d{level}_generic_table={generic_path}")
        print(f"d{level}_point_table={point_path}")
        print(f"d{level}_original_3470_pivot_rows_replayed=true", flush=True)

    joint_forms = insert_dead_axis(q_forms, dead_derivatives)
    assert all(
        set(AxisJet.coerce(form[0]).derivatives).issubset(set(AXES))
        for form in joint_forms
    )
    assert r.fb.CENTER == (Rat3(C), Rat3(V), Rat3(U))
    print("all_33_axes_assembled_in_one_square_zero_ring=true")
    print("symbolic_center_asserted_after_joint_assembly=true", flush=True)

    coordinates = compatibility_coordinates(by_level)
    result = write_joint(outdir, coordinates)
    print(f"joint_transport_coordinate_count={result['coordinate_count']}")
    print(f"joint_transport_rank={result['rank']}/33")
    print(f"joint_transport_kernel_dimension={result['kernel_dimension']}")
    print("joint_transport_pivot_axes=" + ",".join(result["pivot_axes"]))
    print(f"joint_transport_denominator_factor={result['denominator'].factor()}")
    print(
        "joint_transport_denominator_radical_subset_U_H_B3="
        + str(result["allowed"]).lower()
    )
    print(f"joint_transport_conormal_path={result['table_path']}")
    print(f"joint_transport_conormal_sha256={result['table_sha']}")
    print(f"joint_transport_kernel_path={result['kernel_path']}")
    print(f"joint_transport_kernel_sha256={result['kernel_sha']}")
    print("V80B_all_11_point_table_hashes_reproduced=true")
    print("pure_axis_nonzero_constants_may_cancel=true")
    print("transport_kernel_is_not_a_first_or_current_kernel=true")
    print("generic_family_killed=false")
    print("whole_TD6_killed=false")
    print("SP2_killed=false")
    print("JC2_resolved=false")
    print("TD6-A3-Q-DEAD-JOINT-TRANSPORT-V81B PASS")


if __name__ == "__main__":
    main()
