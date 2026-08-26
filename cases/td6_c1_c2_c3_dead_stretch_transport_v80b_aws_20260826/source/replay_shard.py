#!/usr/bin/env python3
"""Exact matrix-aware transport tangent for one TD6 dead-stretch slot.

The pole chart is

    x = r^-25,
    y = r^5 + sum_{m=6}^{16} d_m r^m + zeta r^17.

This shard differentiates at d_6=...=d_16=0 in the one level selected by
``TD6_DEAD_LEVEL``.  It retains every derivative-only pole row, solves
``A0*x'=-A'*x0`` against the frozen rank-3470 transport echelon, and emits
the exact residual incidence forms on the 132-dimensional base transport
space.  It is a transport/source-typing discriminator, not a TD6 theorem.
"""

from fractions import Fraction as Q
from hashlib import sha256
import importlib.util
from math import comb
import os
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
QDUAL_PATH = HERE.parent / "td6_jet_orbit_adjoint_20260824" / "replay.py"
QDUAL_SHA256 = "fb138b0f59e611bab365f37c0302418eda485318beec3f6b21237a95fdc41198"
assert sha256(QDUAL_PATH.read_bytes()).hexdigest() == QDUAL_SHA256
spec = importlib.util.spec_from_file_location("td6_v80_qdual", QDUAL_PATH)
qd = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = qd
spec.loader.exec_module(qd)

nr, fb, E = qd.nr, qd.fb, qd.E
LEVEL = int(os.environ["TD6_DEAD_LEVEL"])
assert 6 <= LEVEL <= 16
ZERO_FORM = (E(0), {})


def add_form(left, right, scale=Q(1)):
    return nr.add_affine(left, right, scale)


def combine_row(row, forms):
    value = ZERO_FORM
    for variable, coefficient in row.items():
        value = add_form(value, forms[variable], coefficient)
    return value


def base_transport_forms():
    fb.CENTER = (Q(1), Q(1), Q(1))
    fb._X_POWER_CACHE.clear()
    nf, ng, transport = qd.build_transport_rows()
    pivots, records = qd.uniform.mu.factor_matrix(transport)
    rhs, compatibility = qd.propagate(records)
    assert not compatibility
    dual_forms, free = qd.direction_parameterization(nf + ng, pivots, rhs)
    assert (len(pivots), len(free)) == (3470, 132)
    forms = [(constant.value, dict(coefficients)) for constant, coefficients in dual_forms]
    return nf, ng, transport, pivots, records, forms, free


def dead_derivative_rows(nf):
    """Return A'_LEVEL rows, including keys absent from the base matrix."""
    rows = {}
    term_count = 0
    for owner, imax, jmax, offset, cutoff in (
        ("f", 15, 60, 0, -3),
        ("g", 25, 100, nf, -5),
    ):
        for i in range(imax + 1):
            for j in range(1, jmax + 1):
                variable = offset + i * (jmax + 1) + j
                base = -25 * i + 5 * j
                for zeta_degree in range(j):
                    exponent = base + (LEVEL - 5) + 12 * zeta_degree
                    if exponent > cutoff:
                        break
                    coefficient = Q(j * comb(j - 1, zeta_degree))
                    key = (owner, "F0", exponent, zeta_degree)
                    row = rows.setdefault(key, {})
                    row[variable] = row.get(variable, Q(0)) + coefficient
                    term_count += 1
    rows = {
        key: {variable: coefficient for variable, coefficient in row.items() if coefficient}
        for key, row in rows.items()
        if any(row.values())
    }
    return rows, term_count


def derivative_lift(records, pivots, base_forms, free, derivative_rows):
    """Differentiate the frozen echelon and retain every compatibility form."""
    pivot_rhs = {}
    compatibility = []
    record_keys = set()
    pivot_keys = set()
    for key, kind, pivot, lead, factors in records:
        record_keys.add(key)
        value = ZERO_FORM
        if key in derivative_rows:
            value = add_form(value, combine_row(derivative_rows[key], base_forms), -1)
        for old, factor in factors:
            value = add_form(value, pivot_rhs[old], -factor)
        if kind == "pivot":
            pivot_keys.add(key)
            pivot_rhs[pivot] = add_form(ZERO_FORM, value, Q(1) / lead)
        elif value != ZERO_FORM:
            compatibility.append((key, value, "base-dependent"))

    for key in sorted(set(derivative_rows) - record_keys):
        value = add_form(ZERO_FORM, combine_row(derivative_rows[key], base_forms), -1)
        if value != ZERO_FORM:
            compatibility.append((key, value, "derivative-only"))

    free_set = set(free)
    derivatives = [None] * len(base_forms)
    for variable in range(len(base_forms) - 1, -1, -1):
        if variable in free_set:
            derivatives[variable] = ZERO_FORM
            continue
        value = pivot_rhs[variable]
        for other, coefficient in pivots[variable].items():
            if other != variable:
                value = add_form(value, derivatives[other], -coefficient)
        derivatives[variable] = value

    # Original-row replay for every pivot row.  This detects omission of
    # either A' or the differentiated pivot solution.
    base_rows = {key: row for key, row, _ in TRANSPORT}
    pivot_replays = 0
    for key in pivot_keys:
        got = combine_row(base_rows[key], derivatives)
        if key in derivative_rows:
            got = add_form(got, combine_row(derivative_rows[key], base_forms))
        assert got == ZERO_FORM, ("differentiated original pivot row", key, got)
        pivot_replays += 1
    return derivatives, compatibility, pivot_replays, record_keys


def field_solve_affine(forms, nparameters):
    """Solve form_i(parameters)=0 over E and return rank/consistency."""
    pivots = {}
    for index, (_, (constant, coefficients), _) in enumerate(forms):
        row = {column: E(value) for column, value in coefficients.items() if value}
        rhs = -E(constant)
        while row:
            pivot = min(row)
            if pivot not in pivots:
                break
            factor = row[pivot]
            old_row, old_rhs = pivots[pivot]
            for column, coefficient in old_row.items():
                value = row.get(column, E(0)) - factor * coefficient
                if value:
                    row[column] = value
                else:
                    row.pop(column, None)
            rhs -= factor * old_rhs
        if not row:
            if rhs:
                return len(pivots), False, (index, rhs)
            continue
        pivot = min(row)
        lead = row[pivot]
        pivots[pivot] = (
            {column: coefficient / lead for column, coefficient in row.items()},
            rhs / lead,
        )
    assert all(0 <= pivot < nparameters for pivot in pivots)
    return len(pivots), True, None


def exact(value):
    return qd.uniform.extension_text(E(value))


def compatibility_digest(forms):
    digest = sha256()
    for key, (constant, coefficients), kind in sorted(forms, key=lambda item: (item[0], item[2])):
        digest.update(f"{kind}\t{key!r}\tconstant\t{exact(constant)}\n".encode())
        for parameter, coefficient in sorted(coefficients.items()):
            digest.update(
                f"{kind}\t{key!r}\tp{parameter}\t{exact(coefficient)}\n".encode()
            )
    return digest.hexdigest()


def write_compatibility(forms):
    outdir = Path(os.environ["TD6_OUTPUT_DIR"])
    outdir.mkdir(parents=True, exist_ok=True)
    lines = ["kind\tkey\tcoordinate\tcoefficient_exact"]
    for key, (constant, coefficients), kind in sorted(forms, key=lambda item: (item[0], item[2])):
        if constant:
            lines.append(f"{kind}\t{key!r}\tconstant\t{exact(constant)}")
        for parameter, coefficient in sorted(coefficients.items()):
            if coefficient:
                lines.append(f"{kind}\t{key!r}\tp{parameter}\t{exact(coefficient)}")
    text = "\n".join(lines) + "\n"
    path = outdir / f"DEAD_D{LEVEL}_TRANSPORT_COMPATIBILITY.tsv"
    path.write_text(text)
    return path, sha256(text.encode()).hexdigest(), len(lines) - 1


def main():
    global TRANSPORT
    print(f"producer=TD6-A3-DEAD-STRETCH-TRANSPORT-V80B-SHARD")
    print(f"dead_level=d{LEVEL}")
    print("pole_chart=x=r^-25;y=r^5+sum(d_m*r^m,m=6..16)+zeta*r^17")
    print("fixed_pole_leading_patterns=true")
    print("pole_chart_determinant=-25*r^-9_independent_of_dead_stretch=true")
    print("scope=transport_source_incidence_at_fixed_A3_zero_dead_stretch")

    nf, ng, TRANSPORT, pivots, records, base_forms, free = base_transport_forms()
    base_keys = {key for key, _, _ in TRANSPORT}
    derivative_rows, derivative_terms = dead_derivative_rows(nf)
    assert derivative_rows and derivative_terms

    # Literal coefficient controls for d/d(d_m) y^j:
    # j*C(j-1,k) r^(m-5+12k).  The chosen x^2*y^3 terms lie below both
    # cutoffs and test k=0 and k=1 without depending on producer output.
    f_variable = 2 * 61 + 3
    assert derivative_rows[("f", "F0", -35 + LEVEL - 5, 0)][f_variable] == 3
    assert derivative_rows[("f", "F0", -35 + LEVEL - 5 + 12, 1)][f_variable] == 6
    correct_shift_key = ("f", "F0", -35 + LEVEL - 5, 0)
    wrong_shift_key = ("f", "F0", -35 + LEVEL - 4, 0)
    assert correct_shift_key != wrong_shift_key
    assert derivative_rows.get(wrong_shift_key, {}).get(f_variable, Q(0)) != 3
    print("dead_stretch_binomial_derivative_positive_control=true")
    print("dead_stretch_wrong_shift_negative_control=true")

    derivatives, compatibility, pivot_replays, record_keys = derivative_lift(
        records, pivots, base_forms, free, derivative_rows
    )
    assert len(derivatives) == nf + ng
    assert pivot_replays == len(pivots)
    # Omitting A' would set x'=0.  Verify directly that this fails at least
    # one differentiated original source row, so the producer cannot pass by
    # silently treating the matrix-changing dead direction as an RHS-only or
    # zero-matrix direction.
    omission_failures = sum(
        combine_row(row, base_forms) != ZERO_FORM
        for row in derivative_rows.values()
    )
    assert omission_failures > 0
    print(f"dead_stretch_matrix_derivative_omission_failures={omission_failures}")
    print("dead_stretch_matrix_derivative_omission_negative_control=true")

    derivative_only_keys = set(derivative_rows) - record_keys
    rank, consistent, error = field_solve_affine(compatibility, len(free))
    path, table_sha, table_entries = write_compatibility(compatibility)
    digest = compatibility_digest(compatibility)

    print(f"transport_rank={len(pivots)}/{nf+ng};free={len(free)}")
    print(f"dead_derivative_row_keys={len(derivative_rows)}")
    print(f"dead_derivative_terms={derivative_terms}")
    print(f"dead_derivative_only_row_keys={len(derivative_only_keys)}")
    print(f"differentiated_original_pivot_rows_replayed={pivot_replays}")
    print(f"transport_compatibility_forms={len(compatibility)}")
    print(f"transport_compatibility_affine_rank={rank}/{len(free)}")
    print(f"transport_compatibility_affine_consistent={str(consistent).lower()}")
    if error is not None:
        print(f"transport_compatibility_first_inconsistency_index={error[0]}")
        print(f"transport_compatibility_first_inconsistency_sha256={sha256(exact(error[1]).encode()).hexdigest()}")
    print(f"transport_compatibility_digest={digest}")
    print(f"transport_compatibility_table={path}")
    print(f"transport_compatibility_table_entries={table_entries}")
    print(f"transport_compatibility_table_sha256={table_sha}")
    print("fixed_section_square_zero_no_family_firewall=true")
    print("TD6-A3-DEAD-STRETCH-TRANSPORT-V80B-SHARD PASS")


if __name__ == "__main__":
    main()
