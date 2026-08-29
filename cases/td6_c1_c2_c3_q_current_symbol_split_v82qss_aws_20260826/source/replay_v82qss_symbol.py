#!/usr/bin/env python3
"""Exact q11/q16 CURRENT direct-symbol split on the fixed A3 section."""

from hashlib import sha256
import importlib.util
import os
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
TARGET = (
    HERE / "payload" / "jc2" / "cases"
    / "td6_c1_c2_c3_all_q_vector_ad_repaired_20260825"
    / "replay_shard.py"
)
EXPECTED = "792f42de85a935a7a09b799caefe6f5a0aeccec104f303dd21cfd43050116493"
assert sha256(TARGET.read_bytes()).hexdigest() == EXPECTED
EXPONENT = int(os.environ["TD6_Q_EXPONENT"])
assert EXPONENT in (11, 16)

spec = importlib.util.spec_from_file_location(
    f"td6_v82qss_parent_q{EXPONENT}", TARGET
)
p = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = p
spec.loader.exec_module(p)
assert p.REQUESTED_Q_EXPONENT == EXPONENT
assert p.Q_EXPONENTS == (EXPONENT,)
assert 15 not in p.ALL_Q_EXPONENTS


OUT = Path(os.environ["TD6_OUTPUT_DIR"]).resolve()
OUT.mkdir(parents=True, exist_ok=True)


def affine_polynomial(form):
    return p.nr.affine_polynomial(form)


def scale_polynomial(polynomial, scalar):
    return p.clean({monomial: scalar * value for monomial, value in polynomial.items()})


def polynomial_lines(label, polynomial):
    lines = ["label\tmonomial\tcoefficient_sha256\tcoefficient_exact"]
    for monomial, coefficient in sorted(polynomial.items(), key=lambda item: repr(item[0])):
        coefficient = p.E3.coerce(coefficient)
        if coefficient:
            lines.append(
                f"{label}\t{monomial!r}\t{p.e3_digest(coefficient)}\t"
                f"{p.e3_exact(coefficient)}"
            )
    return lines


def base_form(form):
    constant, row = form
    return (
        p.EJet(p.EJet.coerce(constant).value),
        {
            variable: p.EJet(p.EJet.coerce(coefficient).value)
            for variable, coefficient in row.items()
            if p.EJet.coerce(coefficient).value
        },
    )


def marker_form(base, derivative):
    base_constant, base_row = base_form(base)
    derivative_constant, derivative_row = base_form(derivative)
    variables = set(base_row) | set(derivative_row)
    return (
        p.EJet(
            base_constant.value,
            {EXPONENT: derivative_constant.value}
            if derivative_constant.value else None,
        ),
        {
            variable: p.EJet(
                base_row.get(variable, p.EJet()).value,
                {EXPONENT: derivative_row.get(variable, p.EJet()).value}
                if derivative_row.get(variable, p.EJet()).value else None,
            )
            for variable in variables
            if (
                base_row.get(variable, p.EJet()).value
                or derivative_row.get(variable, p.EJet()).value
            )
        },
    )


def pack_all_current(polynomials):
    rows = []
    assert len(polynomials) == 40
    for degree, polynomial in enumerate(polynomials):
        row = {}
        constant = p.EJet.coerce(polynomial.get((), 0))
        for monomial, coefficient in polynomial.items():
            if not monomial:
                continue
            assert len(monomial) == 1
            coefficient = p.EJet.coerce(coefficient)
            if coefficient:
                row[monomial[0]] = coefficient
        rows.append((("X0", degree), row, -constant))
    return rows


def base_source_polynomial(row, rhs):
    return p.split_column(p.source_polynomial(row, rhs))


def base_pivot_rows(pivots):
    return {
        variable: base_source_polynomial(row, rhs)
        for variable, (row, rhs, _) in pivots.items()
    }


def canonical_map(dependent):
    coordinates = {}
    for _, key, row, rhs, _ in dependent:
        for variable, coefficient in row.items():
            value = p.EJet.coerce(coefficient).derivatives.get(EXPONENT, p.E3())
            if value:
                coordinate = (repr(key), f"x{variable}")
                coordinates[coordinate] = coordinates.get(coordinate, p.E3()) + value
        value = p.EJet.coerce(rhs).derivatives.get(EXPONENT, p.E3())
        if value:
            coordinate = (repr(key), "constant")
            coordinates[coordinate] = coordinates.get(coordinate, p.E3()) - value
    return {key: value for key, value in coordinates.items() if value}


def map_lines(label, coordinates):
    lines = ["map\tkey\tcoordinate\tcoefficient_sha256\tcoefficient_exact"]
    for (key, coordinate), coefficient in sorted(coordinates.items()):
        lines.append(
            f"{label}\t{key}\t{coordinate}\t{p.e3_digest(coefficient)}\t"
            f"{p.e3_exact(coefficient)}"
        )
    return lines


def map_subtract(left, right):
    keys = set(left) | set(right)
    return {
        key: left.get(key, p.E3()) - right.get(key, p.E3())
        for key in keys
        if left.get(key, p.E3()) - right.get(key, p.E3())
    }


def map_denominator(coordinates):
    return p.denominator_for(coordinates.values()) if coordinates else p.tri.CTX(1)


def build_stage_a():
    bands, pole_f, pole_g = p.build_transport_and_sections()
    first_rows = p.first_rows_and_controls(bands)
    first_pivots, first_forms, free94, _, first_dependent = p.parameterize(
        132, first_rows, "first_symbol_split"
    )
    assert len(first_pivots) == 38 and len(free94) == 94
    assert not p.dependent_obstruction_coordinates(first_dependent)

    bands94 = {
        key: p.compose_forms(forms, first_forms)
        for key, forms in bands.items()
    }
    pole_f94 = p.compose_forms(pole_f, first_forms)
    pole_g94 = p.compose_forms(pole_g, first_forms)
    previous_rows = p.qd.pack(
        "X-1", p.qd.compile_previous(
            bands94[("f", 1)], bands94[("f", 2)],
            bands94[("g", 1)], bands94[("g", 2)],
        )
    )
    previous_rows += p.qd.pack(
        "P1", p.qd.compile_pole_previous(pole_f94, pole_g94)
    )
    previous_pivots, previous_forms, free56, _, previous_dependent = p.parameterize(
        94, previous_rows, "previous_pole_symbol_split"
    )
    assert len(previous_pivots) == 38 and len(free56) == 56
    assert not p.dependent_obstruction_coordinates(previous_dependent)
    bands56 = {
        key: p.compose_forms(forms, previous_forms)
        for key, forms in bands94.items()
    }
    return bands56


def compile_current(bands56):
    return p.qd.compile_current(
        *[bands56[("f", power)] for power in (1, 2, 3)],
        *[bands56[("g", power)] for power in (1, 2, 3)],
    )


def gauge_marker_control(bands56):
    assert EXPONENT == 11
    f_base = {
        power: [base_form(form) for form in bands56[("f", power)]]
        for power in (1, 2, 3)
    }
    g_marker = {}
    zero = (p.EJet(), {})
    for power in (1, 2, 3):
        g_marker[power] = [
            marker_form(
                bands56[("g", power)][degree],
                f_base[power][degree] if degree < len(f_base[power]) else zero,
            )
            for degree in range(len(bands56[("g", power)]))
        ]
    p.configure_qd_jet(omit_direct=p.Q_EXPONENTS)
    assert 14 not in p.qd.Q_PRIME
    p.qd.Q_PRIME[14] = p.EJet.direction(EXPONENT, 15)
    raw = p.qd.compile_current(
        *[f_base[power] for power in (1, 2, 3)],
        *[g_marker[power] for power in (1, 2, 3)],
    )
    lines = ["degree\tderivative_terms\tderivative_sha256"]
    for degree, polynomial in enumerate(raw):
        column = p.split_column(polynomial, EXPONENT)
        lines.append(f"{degree}\t{len(column)}\t{p.polynomial_digest(column)}")
    text = "\n".join(lines) + "\n"
    path = OUT / "Q15_LOWER_SHEAR_MARKER.tsv"
    path.write_text(text)
    print(f"q15_marker_table_path={path}")
    print(f"q15_marker_table_sha256={sha256(text.encode()).hexdigest()}")
    assert all(not p.split_column(polynomial, EXPONENT) for polynomial in raw)
    p.configure_qd_jet()
    print("q15_role=lower_target_shear_marker_only")
    print("q15_in_source_inventory=false")
    print("q15_transport_injection=false")
    print("q15_compiled_current_derivative_zero=true")


def main():
    print("producer=TD6-V82QSS-Q-CURRENT-SYMBOL-SPLIT")
    print(f"requested_q_exponent={EXPONENT}")
    print("reviewed_parent_sha256=" + EXPECTED)
    print("source_center=(C,V,U)")
    print("fixed_A3_square_zero_scope=true")
    print("base_current_system_already_inconsistent=true")
    print("no_q_neighborhood_family_TD6_SP2_landing_or_JC2_claim=true", flush=True)

    bands56 = build_stage_a()
    f30 = affine_polynomial(bands56[("f", 3)][0])
    f30_base = p.split_column(f30)
    f30_column = p.split_column(f30, EXPONENT)
    f30_lines = polynomial_lines("base", f30_base)
    f30_lines.extend(polynomial_lines(f"q{EXPONENT}", f30_column)[1:])
    f30_text = "\n".join(f30_lines) + "\n"
    f30_path = OUT / "F3_CONSTANT_AFFINE.exact.tsv"
    f30_path.write_text(f30_text)
    print(f"f3_constant_affine_path={f30_path}")
    print(f"f3_constant_affine_sha256={sha256(f30_text.encode()).hexdigest()}")
    U6 = p.E3(p.U**6)
    print(f"f3_constant_base_exact={p.e3_exact(f30_base.get((), p.E3()))}")
    f30_matches_expected = f30_base == {(): U6 / 3}
    print(
        "f3_constant_base_matches_U6_over_3_preassert="
        + str(f30_matches_expected).lower(),
        flush=True,
    )

    p.configure_qd_jet()
    raw_full = compile_current(bands56)
    p.configure_qd_jet(omit_direct=p.Q_EXPONENTS)
    raw_omit = compile_current(bands56)
    p.configure_qd_jet()
    assert len(raw_full) == len(raw_omit) == 40

    delta_lines = [
        "degree\tdirect_terms\tdirect_sha256\tdirect_expected_terms\t"
        "direct_expected_sha256"
    ]
    delta_exact_lines = ["degree\tmonomial\tcoefficient_sha256\tcoefficient_exact"]
    raw_nonzero = False
    for degree, (full, omit) in enumerate(zip(raw_full, raw_omit)):
        assert p.split_column(full) == p.split_column(omit)
        delta = p.add(full, omit, -1)
        direct = p.split_column(delta, EXPONENT)
        index = degree - EXPONENT + 1
        expected = {}
        if 0 <= index < len(bands56[("f", 3)]):
            expected = scale_polynomial(
                p.split_column(affine_polynomial(bands56[("f", 3)][index])),
                3 * EXPONENT,
            )
        delta_lines.append(
            f"{degree}\t{len(direct)}\t{p.polynomial_digest(direct)}\t"
            f"{len(expected)}\t{p.polynomial_digest(expected)}"
        )
        for monomial, coefficient in sorted(direct.items(), key=lambda item: repr(item[0])):
            delta_exact_lines.append(
                f"{degree}\t{monomial!r}\t{p.e3_digest(coefficient)}\t"
                f"{p.e3_exact(coefficient)}"
            )
        raw_nonzero = raw_nonzero or bool(direct)
        assert direct == expected
    delta_text = "\n".join(delta_lines) + "\n"
    delta_exact_text = "\n".join(delta_exact_lines) + "\n"
    (OUT / "RAW_DIRECT_QPRIME.tsv").write_text(delta_text)
    (OUT / "RAW_DIRECT_QPRIME.exact.tsv").write_text(delta_exact_text)
    print(f"raw_direct_table_sha256={sha256(delta_text.encode()).hexdigest()}")
    print(f"raw_direct_exact_sha256={sha256(delta_exact_text.encode()).hexdigest()}")
    assert raw_nonzero
    assert p.split_column(
        p.add(raw_full[EXPONENT - 1], raw_omit[EXPONENT - 1], -1), EXPONENT
    ) == {(): EXPONENT * U6}
    print("raw_direct_qprime_formula_3e_f3_exact=true")
    print(f"raw_row_X0_{EXPONENT-1}_coefficient_is_{EXPONENT}U6=true", flush=True)

    rows_full = pack_all_current(raw_full)
    rows_omit = pack_all_current(raw_omit)
    assert [
        (key, base_source_polynomial(row, rhs)) for key, row, rhs in rows_full
    ] == [
        (key, base_source_polynomial(row, rhs)) for key, row, rhs in rows_omit
    ]
    pivots_full, factors_full, dependent_full = p.solve_cert_jet(rows_full)
    pivots_omit, factors_omit, dependent_omit = p.solve_cert_jet(rows_omit)
    assert len(pivots_full) == len(pivots_omit) == 25
    assert [
        (row_index, key, pivot, lead.value)
        for row_index, key, pivot, lead in factors_full
    ] == [
        (row_index, key, pivot, lead.value)
        for row_index, key, pivot, lead in factors_omit
    ]
    assert base_pivot_rows(pivots_full) == base_pivot_rows(pivots_omit)
    assert [record[1] for record in dependent_full] == [
        record[1] for record in dependent_omit
    ]
    print("full_omit_base_rows_and_pivot_schedule_identical=true")
    print("full_omit_original_row_replays_exact=true")

    full_map = canonical_map(dependent_full)
    omit_map = canonical_map(dependent_omit)
    difference_map = map_subtract(full_map, omit_map)
    standard_pivots, _, standard_dependent = p.solve_cert_jet(
        p.qd.pack("X0", raw_full)
    )
    assert len(standard_pivots) == 25
    assert canonical_map(standard_dependent) == full_map
    print("aligned_full_map_matches_production_packing=true")

    map_text = "\n".join(
        map_lines("full", full_map)
        + map_lines("omit_direct_qprime", omit_map)[1:]
        + map_lines("full_minus_omit", difference_map)[1:]
    ) + "\n"
    map_path = OUT / "CURRENT_SYMBOL_SPLIT.exact.tsv"
    map_path.write_text(map_text)
    print(f"current_symbol_split_path={map_path}")
    print(f"current_symbol_split_sha256={sha256(map_text.encode()).hexdigest()}")
    denominators = {
        "full": map_denominator(full_map),
        "omit": map_denominator(omit_map),
        "difference": map_denominator(difference_map),
    }
    denominator_text = "\n".join(
        f"{label}\t{denominator}\t{denominator.factor()}"
        for label, denominator in denominators.items()
    ) + "\n"
    denominator_path = OUT / "CURRENT_SYMBOL_SPLIT.denominators.txt"
    denominator_path.write_text(denominator_text)
    print(f"current_symbol_denominators_path={denominator_path}")
    print(f"current_symbol_denominators_sha256={sha256(denominator_text.encode()).hexdigest()}")
    assert all(denominator.total_degree() == 0 for denominator in denominators.values())
    print("current_symbol_split_denominators_unit=true")
    assert f30_matches_expected
    print("f3_constant_base_is_U6_over_3=true")

    if EXPONENT == 11:
        expected = {(repr(("X0", 10)), "constant"): 11 * U6}
        assert full_map == expected
        assert omit_map == {}
        assert difference_map == expected
        print("q11_full_is_11U6_and_omit_is_zero=true")
        gauge_marker_control(bands56)
    else:
        assert EXPONENT == 16
        assert full_map == omit_map == difference_map == {}
        print("q16_nonzero_raw_direct_column_in_current_pivot_image=true")

    print("conormal_at_empty_base_is_scheduling_only=true")
    print("all_q_tangent_family_killed=false")
    print("whole_TD6_killed=false")
    print("SP2_killed=false")
    print("JC2_resolved=false")
    print("TD6-V82QSS-Q-CURRENT-SYMBOL-SPLIT PASS")


if __name__ == "__main__":
    main()
