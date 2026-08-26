#!/usr/bin/env python3
"""Exact cumulative transport/first conormal gate for all 33 TD6 axes.

This successor independently rebuilds V81B's symbolic-center transport
source module, inserts all 22 licensed q jets and all eleven dead-stretch
jets in one square-zero ring, and then advances the same source lift through
the first X-band equations.  It stacks transport and first-stage dependent
coordinates before computing the exact rank/kernel.  The output is a
localized first-order Fitting discriminator only; it is not a nonlinear
family or TD6 theorem.
"""

from hashlib import sha256
import importlib.util
import os
from pathlib import Path
import platform
import socket
import sys


HERE = Path(__file__).resolve().parent
V81_PATH = (
    HERE.parent / "td6_c1_c2_c3_q_dead_joint_transport_v81b_20260826"
    / "replay.py"
)
V81_SHA256 = "cc23970873283f02e8c352006c95c393de4ad3f1a9bbf57beab6db91e79b79ad"
assert sha256(V81_PATH.read_bytes()).hexdigest() == V81_SHA256
spec = importlib.util.spec_from_file_location("td6_v82_v81_parent", V81_PATH)
v81 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = v81
spec.loader.exec_module(v81)

r, tri, allq = v81.r, v81.tri, v81.allq
Rat3, E3, AxisJet = v81.Rat3, v81.E3, v81.AxisJet
C, V, U, H, B3 = v81.C, v81.V, v81.U, v81.H, v81.B3
AXES, Q_AXES, DEAD_AXES = v81.AXES, v81.Q_AXES, v81.DEAD_AXES
Q_LEVELS, DEAD_LEVELS = v81.Q_LEVELS, v81.DEAD_LEVELS
qd, nr = allq.qd, allq.nr


def source_polynomial(row, rhs):
    out = {(): -AxisJet.coerce(rhs)} if rhs else {}
    for variable, coefficient in row.items():
        coefficient = AxisJet.coerce(coefficient)
        if coefficient:
            out[(variable,)] = coefficient
    return out


def add_polynomial(left, right, scale=1):
    scale = AxisJet.coerce(scale)
    out = dict(left)
    for monomial, coefficient in right.items():
        value = out.get(monomial, AxisJet()) + scale * coefficient
        if value:
            out[monomial] = value
        else:
            out.pop(monomial, None)
    return out


def configure_qd(omit_qprime=()):
    omit_qprime = set(omit_qprime)
    qd.Dual = AxisJet
    qd.B = AxisJet.direction("q2")
    qd.S = AxisJet(E3(qd.uniform.S_FIELD))
    qd.D = AxisJet(E3(qd.uniform.D_FIELD))
    qd.L = AxisJet(E3(qd.uniform.L_FIELD))
    qd.A = AxisJet(E3(qd.uniform.A_FIELD))
    qd.Q_PRIME = {0: AxisJet(1), 24: AxisJet(25)}
    for level in Q_LEVELS:
        axis = f"q{level}"
        if axis not in omit_qprime:
            qd.Q_PRIME[level - 1] = AxisJet.direction(axis, level)
    qd.R = qd.multiply(
        qd.multiply([AxisJet(-1), AxisJet(1)], [AxisJet(-1), AxisJet(1)]),
        [qd.D, -qd.S, AxisJet(1)],
    )
    qd.R3, qd.R5 = qd.power(qd.R, 3), qd.power(qd.R, 5)
    qd.POLE_F = {1: -(qd.L ** 3) * qd.A, 6: qd.L ** 3}
    qd.POLE_G = {
        0: AxisJet(r.b.Q(5, 9)) * qd.L ** 5 * qd.A ** 2,
        5: AxisJet(r.b.Q(-5, 3)) * qd.L ** 5 * qd.A,
        10: qd.L ** 5,
    }
    assert set(qd.B.derivatives) == {"q2"}
    assert "q15" not in qd.B.derivatives


def combine_jet_row(row, forms):
    out = (AxisJet(), {})
    for variable, coefficient in row.items():
        out = v81.add_jet_form(out, forms[variable], v81.scalar(coefficient))
    return out


def build_sections(forms, nf):
    sections = {}
    for owner, imax, jmax, offset in (
        ("f", 15, 60, 0), ("g", 25, 100, nf)
    ):
        for power in (1, 2, 3):
            family = []
            for degree in range(16 if owner == "f" else 26):
                row = {
                    offset + variable: coefficient
                    for variable, coefficient in r.fb.x_chart_coefficient(
                        imax, jmax, power, degree
                    ).items()
                }
                family.append(combine_jet_row(row, forms))
            sections[(owner, power)] = family
    return sections


def solve_cert(rows):
    pivots, factors, dependent = {}, [], []
    source = [
        (
            key,
            {variable: AxisJet.coerce(value) for variable, value in row.items()},
            AxisJet.coerce(rhs),
        )
        for key, row, rhs in rows
    ]
    for row_index, (key, original_row, original_rhs) in enumerate(source):
        row, rhs = dict(original_row), original_rhs
        combination = {row_index: AxisJet(1)}
        while True:
            pivot = next(
                (
                    variable for variable in pivots
                    if variable in row and row[variable]
                ),
                None,
            )
            if pivot is None:
                break
            factor = row[pivot]
            old_row, old_rhs, old_combination = pivots[pivot]
            for variable, coefficient in old_row.items():
                value = row.get(variable, AxisJet()) - factor * coefficient
                if value:
                    row[variable] = value
                else:
                    row.pop(variable, None)
            rhs -= factor * old_rhs
            for old_index, coefficient in old_combination.items():
                value = combination.get(old_index, AxisJet()) - factor * coefficient
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
                replay = add_polynomial(
                    replay,
                    source_polynomial(source_row, source_rhs),
                    coefficient,
                )
            assert replay == source_polynomial(row, rhs)
            dependent.append((row_index, key, row, rhs, combination))
            continue

        pivot = min(base_variables)
        lead = row[pivot]
        inverse = lead.inverse()
        pivots[pivot] = (
            {variable: coefficient * inverse for variable, coefficient in row.items()},
            rhs * inverse,
            {index: coefficient * inverse for index, coefficient in combination.items()},
        )
        factors.append((row_index, key, pivot, lead))

    for pivot, (row, rhs, combination) in pivots.items():
        replay = {}
        for source_index, coefficient in combination.items():
            _, source_row, source_rhs = source[source_index]
            replay = add_polynomial(
                replay,
                source_polynomial(source_row, source_rhs),
                coefficient,
            )
        assert replay == source_polynomial(row, rhs), pivot
    return pivots, factors, dependent


def parameterize(nvariables, rows):
    pivots, factors, dependent = solve_cert(rows)
    free = [variable for variable in range(nvariables) if variable not in pivots]
    parameter_of = {variable: index for index, variable in enumerate(free)}
    forms = [None] * nvariables
    for variable in range(nvariables - 1, -1, -1):
        if variable in parameter_of:
            forms[variable] = (AxisJet(), {parameter_of[variable]: AxisJet(1)})
            continue
        row, rhs, _ = pivots[variable]
        form = (rhs, {})
        for other, coefficient in row.items():
            if other != variable:
                assert other > variable and forms[other] is not None
                form = v81.add_jet_form(form, forms[other], -coefficient)
        forms[variable] = form
    return pivots, forms, free, factors, dependent


def dependent_coordinates(dependent):
    coordinates = {}
    for compatibility_index, (_, key, row, rhs, _) in enumerate(dependent):
        for variable, coefficient in row.items():
            for axis, value in AxisJet.coerce(coefficient).derivatives.items():
                coordinates.setdefault(
                    ("first", compatibility_index, repr(key), f"x{variable}"), {}
                )[axis] = value
        for axis, value in AxisJet.coerce(rhs).derivatives.items():
            coordinates.setdefault(
                ("first", compatibility_index, repr(key), "constant"), {}
            )[axis] = -value
    return {key: values for key, values in coordinates.items() if values}


def column_digest(rows, axis):
    lines = []
    for key, row, rhs in rows:
        for variable, coefficient in sorted(row.items()):
            value = AxisJet.coerce(coefficient).derivatives.get(axis, E3())
            if value:
                lines.append(f"{key!r}\tx{variable}\t{v81.exact(value)}")
        value = AxisJet.coerce(rhs).derivatives.get(axis, E3())
        if value:
            lines.append(f"{key!r}\trhs\t{v81.exact(value)}")
    text = "\n".join(lines) + ("\n" if lines else "")
    return sha256(text.encode()).hexdigest(), len(lines)


def transport_coordinates(by_level):
    raw = v81.compatibility_coordinates(by_level)
    return {
        ("transport", kind, source_key, coordinate): values
        for (kind, source_key, coordinate), values in raw.items()
    }


def cumulative_table(outdir, coordinates):
    ordered = sorted(coordinates, key=repr)
    matrix = [
        [coordinates[key].get(axis, E3()) for axis in AXES]
        for key in ordered
    ]
    reduced, pivots = v81.rref(matrix)
    free = [column for column in range(len(AXES)) if column not in pivots]
    kernel = []
    for free_column in free:
        vector = [E3() for _ in AXES]
        vector[free_column] = E3(1)
        for row_index, pivot_column in enumerate(pivots):
            vector[pivot_column] = -reduced[row_index][free_column]
        kernel.append(vector)
    for row in matrix:
        for vector in kernel:
            assert not sum((a * b for a, b in zip(row, vector)), E3())

    lines = [
        "stage\tkey\tcoordinate\taxis\tcoefficient_sha256\tcoefficient_exact"
    ]
    for key in ordered:
        stage, *rest = key
        source_key = repr(tuple(rest))
        for axis in AXES:
            coefficient = coordinates[key].get(axis, E3())
            if coefficient:
                lines.append(
                    f"{stage}\t{source_key}\t-\t{axis}\t"
                    f"{allq.e3_digest(coefficient)}\t{v81.exact(coefficient)}"
                )
    text = "\n".join(lines) + "\n"
    table_path = outdir / "CUMULATIVE_TRANSPORT_FIRST_CONORMAL.tsv"
    table_path.write_text(text)

    kernel_lines = ["kernel_vector\taxis\tcoefficient_sha256\tcoefficient_exact"]
    for vector_index, vector in enumerate(kernel):
        for axis, coefficient in zip(AXES, vector):
            if coefficient:
                kernel_lines.append(
                    f"{vector_index}\t{axis}\t{allq.e3_digest(coefficient)}\t"
                    f"{v81.exact(coefficient)}"
                )
    kernel_text = "\n".join(kernel_lines) + "\n"
    kernel_path = outdir / "CUMULATIVE_TRANSPORT_FIRST_KERNEL.tsv"
    kernel_path.write_text(kernel_text)

    denominator = allq.denominator_for(
        [entry for row in matrix for entry in row if entry]
        + [entry for vector in kernel for entry in vector if entry]
    )
    assert allq.factors_only_allowed(denominator)
    return {
        "rank": len(pivots),
        "kernel_dimension": len(kernel),
        "pivot_axes": [AXES[column] for column in pivots],
        "table": table_path,
        "table_sha": sha256(text.encode()).hexdigest(),
        "kernel": kernel_path,
        "kernel_sha": sha256(kernel_text.encode()).hexdigest(),
        "denominator": denominator,
    }


def assert_transport_sentinel(coordinates):
    active = (6, 7, 8, 9, 11, 12, 13, 14, 16)
    active_axes = tuple(f"d{level}" for level in active)
    matrix = []
    for level in active:
        key = (
            "transport", "derivative-only",
            repr(("f", "F0", level - 20, 0)), "constant",
        )
        assert key in coordinates, key
        matrix.append([coordinates[key].get(axis, E3()) for axis in active_axes])
    diagonal = []
    for row_index, row in enumerate(matrix):
        assert all(not row[column] for column in range(row_index + 1, len(row)))
        assert row[row_index]
        diagonal.append(row[row_index])
    assert all(value == diagonal[0] for value in diagonal)
    determinant = E3(1)
    for value in diagonal:
        determinant *= value
    assert determinant
    return active_axes, diagonal[0], determinant


def main():
    assert platform.system() == "Linux", "AWS-only producer refuses non-Linux"
    tag = os.environ.get("AWS_RUN_TAG", "")
    assert tag.startswith("td6_v82_") and len(tag) > len("td6_v82_")
    outdir = Path(os.environ["TD6_OUTPUT_DIR"]).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    print("producer=TD6-A3-Q-DEAD-CUMULATIVE-FIRST-FITTING-V82")
    print(f"aws_hostname={socket.gethostname()}")
    print(f"aws_run_tag={tag}")
    print("source_center=(C,V,U);symbolic=true")
    print("axes=" + ",".join(AXES))
    print("q15_target_shear_gauge_excluded=true")
    print("scope=D(U*H*B3)_generic_center_square_zero_source_incidence")
    print("no_previous_current_second_order_or_family_claim=true", flush=True)

    nf, ng, rows, pivots, records = v81.build_base_transport()
    q_rhs = v81.propagate_q(rows, records)
    q_forms, free = v81.global_q_forms(nf + ng, pivots, q_rhs)
    assert len(free) == 132
    by_level, dead_derivatives = {}, {}
    for level in DEAD_LEVELS:
        derivative_rows, _ = v81.dead_derivative_rows(level, nf)
        derivatives, compatibility, omission_failures = v81.dead_lift(
            level, rows, records, pivots, q_forms, derivative_rows
        )
        assert omission_failures > 0
        by_level[level] = compatibility
        dead_derivatives[level] = derivatives
        print(
            f"d{level}_transport_compatibility_forms={len(compatibility)};"
            "original_pivot_rows_replayed=3470",
            flush=True,
        )

    transport = transport_coordinates(by_level)
    active_axes, diagonal, determinant = assert_transport_sentinel(transport)
    assert not any("d10" in values or "d15" in values for values in transport.values())
    print("transport_sentinel_axes=" + ",".join(active_axes))
    print(f"transport_sentinel_diagonal_exact={v81.exact(diagonal)}")
    print(f"transport_sentinel_determinant_exact={v81.exact(determinant)}")
    print("transport_dead_rank_9_exact=true")
    print("transport_d10_d15_columns_exact_zero=true", flush=True)

    joint_forms = v81.insert_dead_axis(q_forms, dead_derivatives)
    assert r.fb.CENTER == (Rat3(C), Rat3(V), Rat3(U))
    joint_bands = build_sections(joint_forms, nf)
    q_only_bands = build_sections(q_forms, nf)

    configure_qd()
    first_rows = qd.pack(
        "X-2", qd.first_band_polynomials(
            joint_bands[("f", 1)], joint_bands[("g", 1)]
        )
    )
    configure_qd(omit_qprime=Q_AXES)
    qprime_omitted_rows = qd.pack(
        "X-2", qd.first_band_polynomials(
            joint_bands[("f", 1)], joint_bands[("g", 1)]
        )
    )
    configure_qd()
    q_only_rows = qd.pack(
        "X-2", qd.first_band_polynomials(
            q_only_bands[("f", 1)], q_only_bands[("g", 1)]
        )
    )
    for axis in Q_AXES:
        positive, count = column_digest(first_rows, axis)
        omitted, omitted_count = column_digest(qprime_omitted_rows, axis)
        assert positive != omitted and count and omitted_count >= 0
    for axis in DEAD_AXES:
        positive, count = column_digest(first_rows, axis)
        omitted, omitted_count = column_digest(q_only_rows, axis)
        assert omitted_count == 0
        assert count > 0 and positive != omitted
    print("all_q_direct_qprime_omission_controls_pass=true")
    print("all_dead_source_column_omission_controls_pass=true", flush=True)

    first_pivots, first_forms, free94, first_factors, first_dependent = parameterize(
        132, first_rows
    )
    assert len(first_pivots) == 38 and len(free94) == 94
    first = dependent_coordinates(first_dependent)
    assert not any(
        axis in values for values in first.values() for axis in Q_AXES
    ), "V78 q-only first conormal must remain zero"
    coordinates = dict(transport)
    assert not coordinates.keys() & first.keys()
    coordinates.update(first)
    result = cumulative_table(outdir, coordinates)

    print(f"first_rank={len(first_pivots)}/132")
    print(f"first_dependent_count={len(first_dependent)}")
    print(f"first_conormal_coordinate_count={len(first)}")
    print("V78_q_only_first_conormal_zero_reproduced=true")
    print(f"cumulative_transport_first_rank={result['rank']}/33")
    print(f"cumulative_transport_first_kernel_dimension={result['kernel_dimension']}")
    print("cumulative_pivot_axes=" + ",".join(result["pivot_axes"]))
    print(f"cumulative_denominator_factor={result['denominator'].factor()}")
    print("cumulative_denominator_radical_subset_U_H_B3=true")
    print(f"cumulative_conormal_path={result['table']}")
    print(f"cumulative_conormal_sha256={result['table_sha']}")
    print(f"cumulative_kernel_path={result['kernel']}")
    print(f"cumulative_kernel_sha256={result['kernel_sha']}")
    print("all_first_pivot_source_combinations_replayed=true")
    print("transport_or_first_kernel_is_not_a_previous_or_current_kernel=true")
    print("generic_family_killed=false")
    print("whole_TD6_killed=false")
    print("SP2_killed=false")
    print("JC2_resolved=false")
    print("TD6-A3-Q-DEAD-CUMULATIVE-FIRST-FITTING-V82 PASS")


if __name__ == "__main__":
    main()
