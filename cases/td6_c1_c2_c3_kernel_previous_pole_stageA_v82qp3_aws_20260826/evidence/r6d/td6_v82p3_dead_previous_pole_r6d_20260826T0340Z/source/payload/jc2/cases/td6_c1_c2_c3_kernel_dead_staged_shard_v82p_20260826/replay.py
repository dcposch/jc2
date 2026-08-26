#!/usr/bin/env python3
"""Exact previous/pole shard for one TD6 transport/first-kernel dead axis.

This is a conditional successor to V82S.  It independently reconstructs the
original transport and first-band source lifts, requires the selected dead
axis to have zero transport and first conormal, and only then advances that
same source column through the previous X-band and pole equations.
"""

from hashlib import sha256
import importlib.util
import os
from pathlib import Path
import platform
import socket
import sys


HERE = Path(__file__).resolve().parent
V82S_PATH = (
    HERE.parent / "td6_c1_c2_c3_kernel_dead_first_shard_v82s_20260826"
    / "replay.py"
)
V82S_SHA256 = "a344d3c211094315fa6f079e1292676ca78e8f1fbcbdfa7078a52e9e8969db90"
assert sha256(V82S_PATH.read_bytes()).hexdigest() == V82S_SHA256
spec = importlib.util.spec_from_file_location("td6_v82p_v82s_parent", V82S_PATH)
v82s = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = v82s
spec.loader.exec_module(v82s)

v82, v81, allq = v82s.v82, v82s.v81, v82s.allq
r, qd, nr = v82.r, v82.qd, v82.nr
AxisJet, E3 = v82.AxisJet, v82.E3


def combine_row(row, forms):
    out = (AxisJet(), {})
    for variable, coefficient in row.items():
        out = v81.add_jet_form(out, forms[variable], v81.scalar(coefficient))
    return out


def build_pole_sections(forms, nf):
    pole_f = []
    for degree in range(61):
        row = {
            variable: coefficient
            for variable, coefficient in nr.pole_coefficient(
                15, 60, -2, degree
            ).items()
        }
        pole_f.append(combine_row(row, forms))
    pole_g = []
    for degree in range(101):
        row = {
            nf + variable: coefficient
            for variable, coefficient in nr.pole_coefficient(
                25, 100, -4, degree
            ).items()
        }
        pole_g.append(combine_row(row, forms))
    return pole_f, pole_g


def assert_axis_form(form):
    constant, row = form
    assert isinstance(constant, AxisJet)
    assert not isinstance(constant, allq.EJet)
    assert all(isinstance(variable, int) and variable >= 0 for variable in row)
    assert all(isinstance(coefficient, AxisJet) for coefficient in row.values())
    assert not any(isinstance(coefficient, allq.EJet) for coefficient in row.values())
    return form


def compose_axis_forms(forms, parameterization):
    """Compose affine forms wholly inside the 33-axis square-zero ring."""
    assert all(assert_axis_form(form) for form in parameterization)
    out = []
    for constant, row in forms:
        assert_axis_form((constant, row))
        result = (constant, {})
        for variable, coefficient in row.items():
            assert variable < len(parameterization)
            assert isinstance(coefficient, AxisJet)
            result = v81.add_jet_form(
                result, parameterization[variable], coefficient
            )
            assert_axis_form(result)
        out.append(result)
    return out


def typed_composition_preflight(axis):
    source_constant = AxisJet(11, {axis: E3(13)})
    scale = AxisJet(17, {axis: E3(19)})
    parameter_constant = AxisJet(23, {axis: E3(29)})
    parameter_coefficient = AxisJet(31, {axis: E3(37)})
    got = compose_axis_forms(
        [(source_constant, {0: scale})],
        [(parameter_constant, {1: parameter_coefficient})],
    )
    expected = (
        source_constant + scale * parameter_constant,
        {1: scale * parameter_coefficient},
    )
    assert got == [expected]
    assert_axis_form(got[0])
    assert axis in got[0][0].derivatives
    assert axis in got[0][1][1].derivatives
    print("axisjet_composition_boundary_preflight=true", flush=True)


def coordinates(dependent, axis):
    out = {}
    for compatibility_index, (_, key, row, rhs, _) in enumerate(dependent):
        for variable, coefficient in row.items():
            value = AxisJet.coerce(coefficient).derivatives.get(axis, E3())
            if value:
                out[(compatibility_index, repr(key), f"x{variable}")] = value
        value = AxisJet.coerce(rhs).derivatives.get(axis, E3())
        if value:
            out[(compatibility_index, repr(key), "constant")] = -value
    return out


def row_column_digest(rows, axis):
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


def write_table(outdir, axis, values):
    lines = ["compatibility\tkey\tcoordinate\taxis\tcoefficient_sha256\tcoefficient_exact"]
    for key in sorted(values, key=repr):
        value = values[key]
        lines.append(
            f"{key[0]}\t{key[1]}\t{key[2]}\t{axis}\t"
            f"{allq.e3_digest(value)}\t{v81.exact(value)}"
        )
    text = "\n".join(lines) + "\n"
    path = outdir / f"{axis.upper()}_PREVIOUS_POLE_CONORMAL.tsv"
    path.write_text(text)
    assert v81.tri.ONE == v81.tri.CTX.constant(1)
    denominator = allq.denominator_for(values.values()) if values else v81.tri.ONE
    assert allq.factors_only_allowed(denominator)
    return path, sha256(text.encode()).hexdigest(), denominator


def main():
    assert platform.system() == "Linux", "AWS-only producer refuses non-Linux"
    tag = os.environ.get("AWS_RUN_TAG", "")
    assert tag.startswith("td6_v82p_") and len(tag) > len("td6_v82p_")
    level = int(os.environ["TD6_DEAD_LEVEL"])
    assert level in (10, 15)
    axis = f"d{level}"
    outdir = Path(os.environ["TD6_OUTPUT_DIR"]).resolve()
    outdir.mkdir(parents=True, exist_ok=True)

    # Positive control for the empty-table reporter branch.  V82P inherited
    # V82S's invalid CTX(1) constructor even though its table may be nonempty.
    control_dir = outdir / "empty_table_control"
    control_dir.mkdir(parents=True, exist_ok=True)
    control_path, _, control_denominator = write_table(control_dir, axis, {})
    assert control_denominator == v81.tri.ONE
    assert control_path.read_text() == (
        "compatibility\tkey\tcoordinate\taxis\tcoefficient_sha256\t"
        "coefficient_exact\n"
    )
    print("empty_previous_pole_table_positive_control=true", flush=True)
    typed_composition_preflight(axis)
    print("producer=TD6-A3-KERNEL-DEAD-PREVIOUS-POLE-SHARD-V82P3")
    print(f"aws_hostname={socket.gethostname()}")
    print(f"aws_run_tag={tag}")
    print(f"dead_axis={axis}")
    print("source_center=(C,V,U);symbolic=true")
    print("scope=D(U*H*B3)_generic_center_square_zero_previous_pole_source_incidence")
    print("requires_transport_and_first_conormal_zero=true")
    print("no_current_second_order_family_or_TD6_claim=true", flush=True)

    nf, ng, rows, pivots, records = v81.build_base_transport()
    q_rhs = v81.propagate_q(rows, records)
    base_forms, free = v81.global_q_forms(nf + ng, pivots, q_rhs)
    assert len(free) == 132
    derivative_rows, term_count = v81.dead_derivative_rows(level, nf)
    derivatives, transport_compatibility, omission_failures = v81.dead_lift(
        level, rows, records, pivots, base_forms, derivative_rows
    )
    assert omission_failures > 0
    assert not transport_compatibility
    axis_forms = v82s.insert_axis(
        [v81.base_form(form) for form in base_forms], derivatives, axis
    )
    base_forms = [v81.base_form(form) for form in base_forms]
    print(f"transport_derivative_rows={len(derivative_rows)};terms={term_count}")
    print("transport_conormal_exact_zero=true")
    print("transport_original_3470_pivot_rows_replayed=true", flush=True)

    axis_bands = v82.build_sections(axis_forms, nf)
    base_bands = v82.build_sections(base_forms, nf)
    axis_pole_f, axis_pole_g = build_pole_sections(axis_forms, nf)
    base_pole_f, base_pole_g = build_pole_sections(base_forms, nf)
    v82s.configure_base_qd()
    first_rows = qd.pack(
        "X-2", qd.first_band_polynomials(
            axis_bands[("f", 1)], axis_bands[("g", 1)]
        )
    )
    base_first_rows = qd.pack(
        "X-2", qd.first_band_polynomials(
            base_bands[("f", 1)], base_bands[("g", 1)]
        )
    )
    first_positive_sha, first_positive_count = v82.column_digest(first_rows, axis)
    first_omitted_sha, first_omitted_count = v82.column_digest(base_first_rows, axis)
    assert first_positive_count > 0 and first_omitted_count == 0
    assert first_positive_sha != first_omitted_sha
    first_pivots, first_forms, free94, _, first_dependent = v82.parameterize(
        132, first_rows
    )
    assert len(first_pivots) == 38 and len(free94) == 94
    assert not coordinates(first_dependent, axis)
    print("first_conormal_exact_zero=true")
    print("first_raw_source_omission_control=true")
    print("all_first_pivot_source_combinations_replayed=true", flush=True)

    assert all(assert_axis_form(form) for forms in axis_bands.values() for form in forms)
    assert all(assert_axis_form(form) for form in first_forms)
    bands94 = {
        key: compose_axis_forms(forms, first_forms)
        for key, forms in axis_bands.items()
    }
    pole_f94 = compose_axis_forms(axis_pole_f, first_forms)
    pole_g94 = compose_axis_forms(axis_pole_g, first_forms)
    assert all(assert_axis_form(form) for forms in bands94.values() for form in forms)
    assert all(assert_axis_form(form) for form in pole_f94 + pole_g94)
    print("all_previous_pole_input_forms_axisjet_typed=true", flush=True)
    previous_rows = qd.pack(
        "X-1", qd.compile_previous(
            bands94[("f", 1)], bands94[("f", 2)],
            bands94[("g", 1)], bands94[("g", 2)],
        )
    )
    previous_rows += qd.pack(
        "P1", qd.compile_pole_previous(pole_f94, pole_g94)
    )
    raw_sha, raw_count = row_column_digest(previous_rows, axis)
    previous_pivots, previous_forms, free56, _, previous_dependent = (
        v82.parameterize(94, previous_rows)
    )
    assert len(previous_pivots) == 38 and len(free56) == 56
    values = coordinates(previous_dependent, axis)
    path, digest, denominator = write_table(outdir, axis, values)
    print(f"previous_pole_raw_axis_entries={raw_count};sha256={raw_sha}")
    print(f"previous_pole_rank={len(previous_pivots)}/94")
    print(f"previous_pole_dependent_count={len(previous_dependent)}")
    print(f"previous_pole_axis_conormal_rank={int(bool(values))}/1")
    print(f"previous_pole_axis_conormal_coordinate_count={len(values)}")
    print(f"previous_pole_axis_denominator_factor={denominator.factor()}")
    print("previous_pole_axis_denominator_radical_subset_U_H_B3=true")
    print(f"previous_pole_axis_table={path}")
    print(f"previous_pole_axis_table_sha256={digest}")
    print("all_previous_pole_pivot_source_combinations_replayed=true")
    print("previous_pole_kernel_is_not_a_current_or_nonlinear_kernel=true")
    print("generic_family_killed=false")
    print("whole_TD6_killed=false")
    print("SP2_killed=false")
    print("JC2_resolved=false")
    print("TD6-A3-KERNEL-DEAD-PREVIOUS-POLE-SHARD-V82P3 PASS")


if __name__ == "__main__":
    main()
