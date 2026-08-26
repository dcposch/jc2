#!/usr/bin/env python3
"""Exact first-stage shard for one transport-kernel dead-stretch axis."""

from hashlib import sha256
import importlib.util
import os
from pathlib import Path
import platform
import socket
import sys


HERE = Path(__file__).resolve().parent
V82_PATH = (
    HERE.parent / "td6_c1_c2_c3_q_dead_joint_first_fitting_v82_20260826"
    / "replay.py"
)
V82_SHA256 = "537219eb8d4c4439697b537542600cc1f95851e8eda2175a9fee3bbde7c508e5"
assert sha256(V82_PATH.read_bytes()).hexdigest() == V82_SHA256
spec = importlib.util.spec_from_file_location("td6_v82s_v82_parent", V82_PATH)
v82 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = v82
spec.loader.exec_module(v82)

v81, r, allq = v82.v81, v82.r, v82.allq
Rat3, E3, AxisJet = v82.Rat3, v82.E3, v82.AxisJet
C, V, U, H, B3 = v82.C, v82.V, v82.U, v82.H, v82.B3
qd = v82.qd


def configure_base_qd():
    qd.Dual = AxisJet
    qd.B = AxisJet()
    qd.S = AxisJet(E3(qd.uniform.S_FIELD))
    qd.D = AxisJet(E3(qd.uniform.D_FIELD))
    qd.L = AxisJet(E3(qd.uniform.L_FIELD))
    qd.A = AxisJet(E3(qd.uniform.A_FIELD))
    qd.Q_PRIME = {0: AxisJet(1), 24: AxisJet(25)}
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
    assert not qd.B.derivatives
    assert all(not value.derivatives for value in qd.Q_PRIME.values())


def insert_axis(base_forms, derivatives, axis):
    out = []
    for (base_constant, base_row), (d_constant, d_row) in zip(
        base_forms, derivatives
    ):
        row = {}
        for parameter in base_row.keys() | d_row.keys():
            coefficient = AxisJet(
                base_row.get(parameter, E3()),
                {axis: d_row.get(parameter, E3())},
            )
            if coefficient:
                row[parameter] = coefficient
        out.append((AxisJet(base_constant, {axis: d_constant}), row))
    return out


def write_table(outdir, axis, coordinates):
    lines = ["key\tcoordinate\taxis\tcoefficient_sha256\tcoefficient_exact"]
    values = []
    for key in sorted(coordinates, key=repr):
        coefficient = coordinates[key].get(axis, E3())
        if coefficient:
            values.append(coefficient)
            lines.append(
                f"{key!r}\t-\t{axis}\t{allq.e3_digest(coefficient)}\t"
                f"{v81.exact(coefficient)}"
            )
    text = "\n".join(lines) + "\n"
    path = outdir / f"{axis.upper()}_FIRST_CONORMAL.tsv"
    path.write_text(text)
    assert v81.tri.ONE == v81.tri.CTX.constant(1)
    denominator = allq.denominator_for(values) if values else v81.tri.ONE
    assert allq.factors_only_allowed(denominator)
    return path, sha256(text.encode()).hexdigest(), len(values), denominator


def main():
    assert platform.system() == "Linux", "AWS-only producer refuses non-Linux"
    tag = os.environ.get("AWS_RUN_TAG", "")
    assert tag.startswith("td6_v82s_") and len(tag) > len("td6_v82s_")
    level = int(os.environ["TD6_DEAD_LEVEL"])
    assert level in (10, 15)
    axis = f"d{level}"
    outdir = Path(os.environ["TD6_OUTPUT_DIR"]).resolve()
    outdir.mkdir(parents=True, exist_ok=True)

    # Positive control for the exact reporter path that failed in V82S.
    control_dir = outdir / "empty_table_control"
    control_dir.mkdir(parents=True, exist_ok=True)
    control_path, _, control_nonzero, control_denominator = write_table(
        control_dir, axis, {}
    )
    assert control_nonzero == 0
    assert control_denominator == v81.tri.ONE
    assert control_path.read_text() == (
        "key\tcoordinate\taxis\tcoefficient_sha256\tcoefficient_exact\n"
    )
    print("empty_first_conormal_table_positive_control=true", flush=True)
    print("producer=TD6-A3-KERNEL-DEAD-FIRST-SHARD-V82S")
    print(f"aws_hostname={socket.gethostname()}")
    print(f"aws_run_tag={tag}")
    print(f"dead_axis={axis}")
    print("source_center=(C,V,U);symbolic=true")
    print("base_q=t+t^25;base_dead_stretch=0")
    print("scope=D(U*H*B3)_generic_center_square_zero_first_source_incidence")
    print("no_joint_previous_current_second_order_or_family_claim=true", flush=True)

    nf, ng, rows, pivots, records = v81.build_base_transport()
    q_rhs = v81.propagate_q(rows, records)
    q_forms, free = v81.global_q_forms(nf + ng, pivots, q_rhs)
    assert len(free) == 132
    base_forms = [v81.base_form(form) for form in q_forms]
    derivative_rows, term_count = v81.dead_derivative_rows(level, nf)
    derivatives, compatibility, omission_failures = v81.dead_lift(
        level, rows, records, pivots, q_forms, derivative_rows
    )
    assert not compatibility
    assert omission_failures > 0
    print(f"transport_derivative_rows={len(derivative_rows)};terms={term_count}")
    print(f"transport_omission_failures={omission_failures}")
    print("transport_axis_compatibility_exact_zero=true")
    print("transport_original_3470_pivot_rows_replayed=true", flush=True)

    axis_forms = insert_axis(base_forms, derivatives, axis)
    axis_bands = v82.build_sections(axis_forms, nf)
    base_bands = v82.build_sections(base_forms, nf)
    configure_base_qd()
    first_rows = qd.pack(
        "X-2", qd.first_band_polynomials(
            axis_bands[("f", 1)], axis_bands[("g", 1)]
        )
    )
    base_rows = qd.pack(
        "X-2", qd.first_band_polynomials(
            base_bands[("f", 1)], base_bands[("g", 1)]
        )
    )
    positive_sha, positive_count = v82.column_digest(first_rows, axis)
    omitted_sha, omitted_count = v82.column_digest(base_rows, axis)
    assert positive_count > 0 and omitted_count == 0
    assert positive_sha != omitted_sha
    print(f"first_raw_axis_entries={positive_count};sha256={positive_sha}")
    print(f"first_omitted_axis_entries={omitted_count};sha256={omitted_sha}")
    print("dead_source_column_omission_control=true", flush=True)

    first_pivots, first_forms, free94, first_factors, first_dependent = (
        v82.parameterize(132, first_rows)
    )
    assert len(first_pivots) == 38 and len(free94) == 94
    coordinates = v82.dependent_coordinates(first_dependent)
    assert all(
        set(values).issubset({axis}) for values in coordinates.values()
    )
    path, digest, nonzero, denominator = write_table(
        outdir, axis, coordinates
    )
    assert nonzero == 0
    assert denominator == v81.tri.ONE
    assert path.read_text() == (
        "key\tcoordinate\taxis\tcoefficient_sha256\tcoefficient_exact\n"
    )
    print("actual_first_conormal_table_is_header_only=true")
    print(f"first_rank={len(first_pivots)}/132")
    print(f"first_dependent_count={len(first_dependent)}")
    print(f"first_axis_conormal_rank={int(nonzero > 0)}/1")
    print(f"first_axis_conormal_coordinate_count={nonzero}")
    print(f"first_axis_denominator_factor={denominator.factor()}")
    print("first_axis_denominator_radical_subset_U_H_B3=true")
    print(f"first_axis_table={path}")
    print(f"first_axis_table_sha256={digest}")
    print("all_first_pivot_source_combinations_replayed=true")
    print("transport_first_kernel_is_not_a_previous_or_current_kernel=true")
    print("generic_family_killed=false")
    print("whole_TD6_killed=false")
    print("SP2_killed=false")
    print("JC2_resolved=false")
    print("TD6-A3-KERNEL-DEAD-FIRST-SHARD-V82S PASS")


if __name__ == "__main__":
    main()
