#!/usr/bin/env python3
"""Raw original-source CURRENT rebuild on the TD6 divisor F=0.

The frozen V82QST1C payload is imported as a library.  Only the source center
is changed, before transport is built.  The generic presentation's CURRENT
table is never specialized.
"""

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
TARGET_SHA256 = "a4ccd5d81101fdb82ed2f61571c258e2054961d161f4a98461b8f8614d3fd85e"
assert sha256(TARGET.read_bytes()).hexdigest() == TARGET_SHA256
assert os.environ.get("TD6_Q_EXPONENT") in ("2", "10")
assert os.environ.get("TD6_PIVOT_POLICY") == "ascending"
assert os.environ.get("TD6_PIVOT_SCOPE") == "all-staged"

spec = importlib.util.spec_from_file_location("td6_v82qst2_f_raw_parent", TARGET)
m = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = m
spec.loader.exec_module(m)

C, V, U = m.C, m.V, m.U
Rat3, E3, EJet = m.Rat3, m.E3, m.EJet
CENTER_C = (Rat3(V)**2 - Rat3(U)**3) / Rat3(U)
CENTER_V = Rat3(V)
CENTER_U = Rat3(U)
H_F = V**2 - 4*U**3
L_F = V**2 + 8*U**3
ALLOWED = (U, V, H_F, L_F)
CAPTURE = {}


def monic(polynomial):
    if not polynomial:
        return polynomial
    return polynomial / polynomial.leading_coefficient()


ALLOWED_MONIC = tuple(monic(factor) for factor in ALLOWED)


def factor_list(polynomial):
    if not polynomial or polynomial.total_degree() == 0:
        return ()
    return tuple(monic(factor) for factor, _ in polynomial.factor()[1])


def factors_only_allowed(polynomial):
    return all(factor in ALLOWED_MONIC for factor in factor_list(polynomial))


def outside_factors(polynomial):
    return tuple(
        str(factor) for factor in factor_list(polynomial)
        if factor not in ALLOWED_MONIC
    )


def polynomial_uses_formal_c(polynomial):
    return any(monomial[0] for monomial in polynomial.to_dict())


def rat_uses_formal_c(value):
    value = m.Rat3.coerce(value)
    return (
        polynomial_uses_formal_c(value.numerator)
        or polynomial_uses_formal_c(value.denominator)
    )


def e3_uses_formal_c(value):
    return any(rat_uses_formal_c(coordinate) for coordinate in m.r.scalar_coordinates(value))


def ejet_uses_formal_c(value):
    value = EJet.coerce(value)
    return e3_uses_formal_c(value.value) or any(
        e3_uses_formal_c(coefficient) for coefficient in value.derivatives.values()
    )


def audit_forms_no_formal_c(forms, label):
    count = 0
    for constant, row in forms:
        values = [constant, *row.values()]
        for value in values:
            count += 1
            assert not ejet_uses_formal_c(value), (label, count)
    print(f"{label}_formal_C_audited_value_count={count}")
    print(f"{label}_formal_C_unused=true")


def audit_rows_no_formal_c(rows, label):
    count = 0
    for key, row, rhs in rows:
        for value in [*row.values(), rhs]:
            count += 1
            assert not ejet_uses_formal_c(value), (label, key, count)
    print(f"{label}_formal_C_audited_value_count={count}")
    print(f"{label}_formal_C_unused=true")


def build_transport_and_sections_f_raw():
    original_build_transport = m.r.fb.build_transport
    original_factor_transport = m.tri.factor_transport

    def specialized_build_transport(*args, **kwargs):
        m.r.fb.CENTER = (CENTER_C, CENTER_V, CENTER_U)
        return original_build_transport(*args, **kwargs)

    def captured_factor_transport(rows):
        result = original_factor_transport(rows)
        CAPTURE["transport_events"] = result[2]
        return result

    m.r.fb.build_transport = specialized_build_transport
    m.tri.factor_transport = captured_factor_transport
    try:
        result = m.build_transport_and_sections_original()
    finally:
        m.r.fb.build_transport = original_build_transport
        m.tri.factor_transport = original_factor_transport
    bands, pole_f, pole_g = result
    for key, forms in sorted(bands.items()):
        audit_forms_no_formal_c(forms, f"transport_band_{key[0]}{key[1]}")
    audit_forms_no_formal_c(pole_f, "transport_pole_f")
    audit_forms_no_formal_c(pole_g, "transport_pole_g")
    assert CAPTURE.get("transport_events") is not None
    return result


def replay_source_combination(rows, record):
    row_index, key, row, rhs, combination = record
    replay = {}
    for source_index, coefficient in combination.items():
        _, source_row, source_rhs = rows[source_index]
        replay = m.add(
            replay,
            m.source_polynomial(source_row, source_rhs),
            coefficient,
        )
    target = m.source_polynomial(row, rhs)
    assert m.clean(replay) == m.clean(target)
    active = next(
        source_index for source_index, coefficient in combination.items()
        if coefficient.value
    )
    omitted = {}
    for source_index, coefficient in combination.items():
        if source_index == active:
            continue
        _, source_row, source_rhs = rows[source_index]
        omitted = m.add(
            omitted,
            m.source_polynomial(source_row, source_rhs),
            coefficient,
        )
    assert m.clean(omitted) != m.clean(target)
    exact = tuple(
        (
            source_index,
            rows[source_index][0],
            m.e3_exact(EJet.coerce(coefficient).value),
        )
        for source_index, coefficient in sorted(combination.items())
        if coefficient.value
    )
    return row_index, key, exact


def all_row_values(rows):
    for _, row, rhs in rows:
        for value in row.values():
            yield EJet.coerce(value).value
        yield EJet.coerce(rhs).value


def all_factor_values(factors):
    for _, _, _, lead in factors:
        lead = EJet.coerce(lead)
        yield lead.value
        yield from lead.derivatives.values()


def emit_current_base_incompatibilities(
    current_rows,
    current_factors,
    base_inconsistent,
    first_rows,
    first_factors,
    previous_rows,
    previous_factors,
):
    chart_values = [
        *all_row_values(first_rows),
        *all_factor_values(first_factors),
        *all_row_values(previous_rows),
        *all_factor_values(previous_factors),
        *all_row_values(current_rows),
        *all_factor_values(current_factors),
    ]
    generic_kills = []
    for index, record in enumerate(base_inconsistent):
        row_index, key, row, rhs, combination = record
        residual = EJet.coerce(rhs).value
        assert residual and not any(EJet.coerce(value).value for value in row.values())
        replay_row, replay_key, exact = replay_source_combination(current_rows, record)
        assert replay_row == row_index and replay_key == key
        residual_denominator, residual_gcd = m.r.cleared_scalar_gcd(residual)
        combination_values = [
            EJet.coerce(value).value for value in combination.values()
            if EJet.coerce(value).value
        ]
        certificate_denominator = monic(m.denominator_for(
            [*chart_values, *combination_values, residual]
        ))
        residual_outside = outside_factors(residual_gcd)
        denominator_outside = outside_factors(certificate_denominator)
        generic_kill = not residual_outside and not denominator_outside
        generic_kills.append(generic_kill)
        certificate_digest = sha256(repr(exact).encode()).hexdigest()
        print(f"F_RAW_current_incompatibility[{index}]_row_index={row_index}")
        print(f"F_RAW_current_incompatibility[{index}]_key={key}")
        print(
            f"F_RAW_current_incompatibility[{index}]_residual_sha256="
            f"{m.e3_digest(residual)}"
        )
        print(
            f"F_RAW_current_incompatibility[{index}]_residual_exact="
            f"{m.e3_exact(residual)}"
        )
        print(
            f"F_RAW_current_incompatibility[{index}]_residual_denominator="
            f"({residual_denominator})"
        )
        print(
            f"F_RAW_current_incompatibility[{index}]_cleared_numerator_gcd="
            f"({residual_gcd})"
        )
        print(
            f"F_RAW_current_incompatibility[{index}]_certificate_denominator="
            f"({certificate_denominator})"
        )
        print(
            f"F_RAW_current_incompatibility[{index}]_certificate_denominator_factor="
            f"{certificate_denominator.factor()}"
        )
        print(
            f"F_RAW_current_incompatibility[{index}]_residual_outside_factors="
            f"{residual_outside}"
        )
        print(
            f"F_RAW_current_incompatibility[{index}]_denominator_outside_factors="
            f"{denominator_outside}"
        )
        print(
            f"F_RAW_current_incompatibility[{index}]_source_row_count="
            f"{len(exact)}"
        )
        print(
            f"F_RAW_current_incompatibility[{index}]_source_certificate_sha256="
            f"{certificate_digest}"
        )
        print(
            f"F_RAW_current_incompatibility[{index}]_source_certificate_exact="
            f"{exact}"
        )
        print(
            f"F_RAW_current_incompatibility[{index}]_generic_open_killed="
            f"{str(generic_kill).lower()}"
        )
    print("F_RAW_current_incompatibility_source_replay=true")
    print("F_RAW_current_incompatibility_omission_negative_control=true")
    print(
        "F_RAW_registered_generic_open_killed="
        + str(any(generic_kills)).lower()
    )
    return any(generic_kills)


def run_staged_f_raw(bands, pole_f, pole_g, first_rows, first_forms, outdir):
    bands94 = {
        key: m.compose_forms(forms, first_forms)
        for key, forms in bands.items()
    }
    pole_f94 = m.compose_forms(pole_f, first_forms)
    pole_g94 = m.compose_forms(pole_g, first_forms)
    previous_rows = m.qd.pack(
        "X-1", m.qd.compile_previous(
            bands94[("f", 1)], bands94[("f", 2)],
            bands94[("g", 1)], bands94[("g", 2)],
        )
    )
    previous_rows += m.qd.pack(
        "P1", m.qd.compile_pole_previous(pole_f94, pole_g94)
    )
    audit_rows_no_formal_c(previous_rows, "previous_pole_source")
    previous_pivots, previous_forms, free56, previous_factors, previous_dependent = (
        m.parameterize(94, previous_rows, "previous_pole_F_raw")
    )
    assert len(previous_pivots) == 38 and len(free56) == 56
    previous_coordinates = m.dependent_obstruction_coordinates(previous_dependent)
    m.conormal_table(previous_dependent, outdir, "PREVIOUS_POLE_F_RAW")
    assert not previous_coordinates
    print("previous_pole_F_raw_full_family_parameterization=true", flush=True)

    bands56 = {
        key: m.compose_forms(forms, previous_forms)
        for key, forms in bands94.items()
    }
    current_rows = m.qd.pack(
        "X0", m.qd.compile_current(
            *[bands56[("f", power)] for power in (1, 2, 3)],
            *[bands56[("g", power)] for power in (1, 2, 3)],
        )
    )
    audit_rows_no_formal_c(current_rows, "current_source")
    old_stage = m.QST_ACTIVE_STAGE
    m.QST_ACTIVE_STAGE = "current"
    try:
        current_pivots, current_factors, current_dependent = m.solve_cert_jet(
            current_rows
        )
    finally:
        m.QST_ACTIVE_STAGE = old_stage
    base_inconsistent = [
        record for record in current_dependent
        if EJet.coerce(record[3]).value
    ]
    assert base_inconsistent
    p12 = [record for record in base_inconsistent if record[1] == ("X0", 12)]
    assert len(p12) == 1
    killed = emit_current_base_incompatibilities(
        current_rows,
        current_factors,
        base_inconsistent,
        first_rows,
        CAPTURE["first_factors"],
        previous_rows,
        previous_factors,
    )
    print(f"current_F_raw_rank={len(current_pivots)}/56")
    print(f"current_F_raw_dependent_count={len(current_dependent)}")
    print(f"current_F_raw_base_inconsistent_count={len(base_inconsistent)}")
    print("current_F_raw_P12_base_incompatibility_present=true")
    print("current_F_raw_conormal_skipped_empty_base=true")
    print(f"current_F_raw_generic_open_killed={str(killed).lower()}")
    print("whole_F_divisor_killed=false")
    print("whole_fixed_A3_killed=false")
    print("whole_TD6_killed=false")
    print("SP2_killed=false")
    print("JC2_resolved=false")
    print("TD6-V82QST2-F-RAW-CURRENT PASS")


def main():
    raw_f = CENTER_C*CENTER_U - CENTER_V**2 + CENTER_U**3
    raw_g = CENTER_V**4 + 4*raw_f**2
    raw_l = (
        4*CENTER_U**3*raw_g**2
        + CENTER_V**4*(CENTER_V**2 + 4*CENTER_U**3)
        *(CENTER_V**2 + 2*raw_f)**2
    )
    raw_h = CENTER_C - 3*CENTER_U**2
    raw_b3 = (
        4*CENTER_C**2*CENTER_U**2
        - 4*CENTER_C*CENTER_V**2*CENTER_U
        + 24*CENTER_C*CENTER_U**4
        + CENTER_V**4 - 20*CENTER_V**2*CENTER_U**3
        + 20*CENTER_U**6
    )
    assert raw_f == Rat3()
    assert raw_g == Rat3(V**4)
    assert raw_l == Rat3(V**8*L_F)
    assert raw_h == Rat3(H_F, U)
    assert raw_b3 == Rat3(V**4)
    assert not any(rat_uses_formal_c(value) for value in (
        CENTER_C, CENTER_V, CENTER_U, raw_f, raw_g, raw_l, raw_h, raw_b3
    ))
    print("producer=TD6-V82QST2-F-RAW-CURRENT")
    print(f"requested_q_exponent={m.REQUESTED_Q_EXPONENT}")
    print("source_center_C0=(V^2-U^3)/U")
    print("source_center_V0=V")
    print("source_center_U0=U")
    print("formal_C_unused_sentinel=true")
    print("raw_F_identity_zero=true")
    print("raw_G_identity=V^4")
    print("raw_L_identity=V^8*(V^2+8U^3)")
    print("raw_H_identity=(V^2-4U^3)/U")
    print("raw_B3_identity=V^4")
    print("registered_open=D(U*V*(V^2-4U^3)*(V^2+8U^3))")
    print("source_rebuilt_before_transport=true")
    print("generic_CURRENT_table_specialized=false")
    print("Gate1_terminal_comparison_logically_required=true")
    print("provisional_AWS_overlap_allowed=true")
    print(f"frozen_parent_sha256={TARGET_SHA256}", flush=True)

    m.build_transport_and_sections_original = m.build_transport_and_sections
    m.build_transport_and_sections = build_transport_and_sections_f_raw
    m.run_staged = run_staged_f_raw
    m.factors_only_allowed = factors_only_allowed
    m.QST_DEBT_FACTORS = (
        ("U", U), ("V", V), ("H_F", H_F), ("L_F", L_F)
    )

    bands, pole_f, pole_g = m.build_transport_and_sections()
    first_rows = m.first_rows_and_controls(bands)
    audit_rows_no_formal_c(first_rows, "first_source")
    first_pivots, first_forms, free94, first_factors, first_dependent = (
        m.parameterize(132, first_rows, "first_F_raw")
    )
    CAPTURE["first_factors"] = first_factors
    assert len(first_pivots) == 38 and len(free94) == 94
    first_coordinates = m.dependent_obstruction_coordinates(first_dependent)
    m.conormal_table(first_dependent, Path(os.environ["TD6_OUTPUT_DIR"]), "FIRST_F_RAW")
    assert not first_coordinates
    print("first_F_raw_full_family_parameterization=true", flush=True)
    m.run_staged(bands, pole_f, pole_g, first_rows, first_forms,
                 Path(os.environ["TD6_OUTPUT_DIR"]))


if __name__ == "__main__":
    main()
