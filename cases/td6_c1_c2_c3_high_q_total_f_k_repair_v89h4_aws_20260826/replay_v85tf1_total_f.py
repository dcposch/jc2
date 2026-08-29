#!/usr/bin/env python3
"""Literal total-F lift of the V82QST3 genuine-P12/FIRST certificate.

All expensive construction is deliberately performed only by the AWS-gated
runner.  This client imports the frozen original generic compiler, rebuilds
both the generic and F=0 raw sources, audits literal base change, and emits an
exact localized identity s = sum a_i f_i + F*h.
"""

from ast import literal_eval
import csv
from fractions import Fraction
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
CERTIFICATE = HERE / "F_RAW_P12_CLEARED_SOURCE_CERTIFICATE.tsv"
CERTIFICATE_SHA256 = "8e892ffa914e0f93969abb9722f926486843f59cf77f5861c5ce3d3438281482"

assert sha256(TARGET.read_bytes()).hexdigest() == TARGET_SHA256
assert sha256(CERTIFICATE.read_bytes()).hexdigest() == CERTIFICATE_SHA256
assert os.environ.get("TD6_Q_EXPONENT") in ("2", "10")
assert os.environ.get("TD6_PIVOT_POLICY") == "ascending"
assert os.environ.get("TD6_PIVOT_SCOPE") == "all-staged"

spec = importlib.util.spec_from_file_location("td6_v85tf1_generic_parent", TARGET)
m = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = m
spec.loader.exec_module(m)

EJet, E3, Rat3 = m.EJet, m.E3, m.Rat3
C, V, U = m.C, m.V, m.U
F = C*U - V**2 + U**3
H = C - 3*U**2
B3 = m.B3
SPECIAL_C = (Rat3(V)**2 - Rat3(U)**3) / Rat3(U)
SPECIAL_HF = V**2 - 4*U**3
SPECIAL_CLEARER = V**4 * U**9 * SPECIAL_HF**3
TOTAL_TARGET = U**12 * H**3 * B3
ALLOWED = (U, H, B3)
QD_STATE_NAMES = (
    "Dual", "B", "S", "D", "L", "A", "Q_PRIME", "R", "R3", "R5",
    "POLE_F", "POLE_G",
)
BASE_QD_STATE = {name: getattr(m.qd, name) for name in QD_STATE_NAMES}


def restore_base_qd_state():
    for name, value in BASE_QD_STATE.items():
        setattr(m.qd, name, value)


def base_polynomial(polynomial):
    return m.split_column(polynomial)


def clean(polynomial):
    return {key: E3.coerce(value) for key, value in polynomial.items() if value}


def add(left, right, coefficient=1):
    coefficient = E3.coerce(coefficient)
    out = dict(left)
    for monomial, value in right.items():
        total = out.get(monomial, E3()) + coefficient*E3.coerce(value)
        if total:
            out[monomial] = total
        else:
            out.pop(monomial, None)
    return out


def scale(polynomial, coefficient):
    coefficient = E3.coerce(coefficient)
    return clean({key: coefficient*value for key, value in polynomial.items()})


def multiply(left, right):
    out = {}
    for lm, lv in left.items():
        for rm, rv in right.items():
            monomial = tuple(sorted(lm + rm))
            value = out.get(monomial, E3()) + E3.coerce(lv)*E3.coerce(rv)
            if value:
                out[monomial] = value
            else:
                out.pop(monomial, None)
    return out


def source_polynomial(row, rhs):
    return base_polynomial(m.source_polynomial(row, rhs))


def raw_p12(bands):
    raw = m.qd.compile_current(
        *[bands[("f", power)] for power in (1, 2, 3)],
        *[bands[("g", power)] for power in (1, 2, 3)],
    )[12]
    return base_polynomial({
        monomial: EJet.coerce(value)
        for monomial, value in raw.items() if value
    })


def build_generic_source():
    restore_base_qd_state()
    bands, _, _ = m.build_transport_and_sections()
    try:
        first_rows = m.first_rows_and_controls(bands)
        p12 = raw_p12(bands)
    finally:
        restore_base_qd_state()
    return bands, first_rows, p12


def build_special_source():
    restore_base_qd_state()
    original = m.r.fb.build_transport

    def specialized(*args, **kwargs):
        m.r.fb.CENTER = (SPECIAL_C, Rat3(V), Rat3(U))
        return original(*args, **kwargs)

    m.r.fb.build_transport = specialized
    try:
        bands, _, _ = m.build_transport_and_sections()
    finally:
        m.r.fb.build_transport = original
    try:
        first_rows = m.first_rows_and_controls(bands)
        p12 = raw_p12(bands)
    finally:
        restore_base_qd_state()
    return bands, first_rows, p12


def specialize_polynomial_value(polynomial):
    out = Rat3()
    for exponents, coefficient in polynomial.to_dict().items():
        ec, ev, eu = exponents
        term = Rat3(coefficient)
        if ec:
            term *= SPECIAL_C**ec
        if ev:
            term *= Rat3(V)**ev
        if eu:
            term *= Rat3(U)**eu
        out += term
    return out


def specialize_rational(value):
    value = Rat3.coerce(value)
    numerator = specialize_polynomial_value(value.numerator)
    denominator = specialize_polynomial_value(value.denominator)
    return numerator / denominator


def specialize_e3(value):
    coordinates = tuple(
        specialize_rational(coordinate)
        for coordinate in m.r.scalar_coordinates(E3.coerce(value))
    )
    return m.from_vector(coordinates)


def specialize_polynomial(polynomial):
    return clean({key: specialize_e3(value) for key, value in polynomial.items()})


def parse_uv_polynomial(expression):
    """Parse the deliberately tiny Q[U,V] grammar emitted by V82QST3."""
    assert "C" not in expression and "(" not in expression and ")" not in expression
    expression = expression.strip().replace(" ", "")
    if expression == "0":
        return Rat3()
    normalized = expression.replace("-", "+-")
    if normalized.startswith("+"):
        normalized = normalized[1:]
    out = Rat3()
    for raw_term in normalized.split("+"):
        assert raw_term
        coefficient = Fraction(1)
        powers = {"U": 0, "V": 0}
        for factor in raw_term.split("*"):
            if factor.startswith("U") or factor.startswith("V"):
                name = factor[0]
                if factor == name:
                    exponent = 1
                else:
                    assert factor.startswith(name + "^")
                    exponent = int(factor[2:])
                powers[name] += exponent
            else:
                coefficient *= Fraction(factor)
        term = Rat3(coefficient)
        if powers["U"]:
            term *= Rat3(U)**powers["U"]
        if powers["V"]:
            term *= Rat3(V)**powers["V"]
        out += term
    return out


def parse_e3_exact(text):
    coordinates = literal_eval(text)
    assert len(coordinates) == 18
    vector = []
    for numerator, denominator in coordinates:
        vector.append(
            parse_uv_polynomial(numerator) / parse_uv_polynomial(denominator)
        )
    return m.from_vector(tuple(vector))


def read_frozen_multipliers(first_rows):
    p12_multiplier = {}
    first_multipliers = [{} for _ in first_rows]
    used_keys = {}
    with CERTIFICATE.open(newline="") as handle:
        rows = csv.DictReader(handle, delimiter="\t")
        assert rows.fieldnames == [
            "source_kind", "source_index", "source_key",
            "parameter_monomial", "coefficient_exact",
        ]
        for record in rows:
            kind = record["source_kind"]
            index = int(record["source_index"])
            monomial = literal_eval(record["parameter_monomial"])
            assert isinstance(monomial, tuple)
            coefficient = parse_e3_exact(record["coefficient_exact"])
            assert coefficient
            if kind == "P12":
                assert index == 12
                assert literal_eval(record["source_key"]) == ("X0_RAW", 12)
                assert monomial not in p12_multiplier
                p12_multiplier[monomial] = coefficient
            else:
                assert kind == "FIRST" and 0 <= index < len(first_rows)
                source_key = literal_eval(record["source_key"])
                assert source_key == first_rows[index][0]
                used_keys[index] = source_key
                assert monomial not in first_multipliers[index]
                first_multipliers[index][monomial] = coefficient
    assert p12_multiplier and len(used_keys) == 28
    assert sum(len(value) for value in first_multipliers) == 1489
    return p12_multiplier, first_multipliers, used_keys


def factor_list(polynomial):
    if not polynomial or polynomial.total_degree() == 0:
        return ()
    return tuple(factor for factor, _ in polynomial.factor()[1])


def monic(polynomial):
    return polynomial / polynomial.leading_coefficient() if polynomial else polynomial


ALLOWED_MONIC = tuple(monic(value) for value in ALLOWED)


def factors_allowed(polynomial):
    return all(monic(factor) in ALLOWED_MONIC for factor in factor_list(polynomial))


def assert_denominators_allowed(values, label):
    value_count = coordinate_count = 0
    for value in values:
        value_count += 1
        for coordinate in m.r.scalar_coordinates(E3.coerce(value)):
            coordinate_count += 1
            assert coordinate.denominator
    common = monic(m.denominator_for([
        E3.coerce(value) for value in values
    ])) if values else m.tri.ONE
    assert factors_allowed(common), (label, common.factor())
    assert common.gcd(F).total_degree() == 0, label
    return value_count, coordinate_count, common


def divide_polynomial_by_f(polynomial):
    divisor = Rat3(F)
    quotient = {}
    cancellation_count = 0
    for monomial, value in polynomial.items():
        coordinates = []
        for coordinate in m.r.scalar_coordinates(E3.coerce(value)):
            divided = coordinate / divisor
            assert divided*divisor == coordinate
            coordinates.append(divided)
            cancellation_count += 1
        coefficient = m.from_vector(tuple(coordinates))
        if coefficient:
            quotient[monomial] = coefficient
    assert scale(quotient, E3(Rat3(F))) == polynomial
    return quotient, cancellation_count


def all_values(polynomials):
    for polynomial in polynomials:
        yield from polynomial.values()


def assert_polynomial_coordinates(polynomials, label):
    count = 0
    one = m.tri.ONE
    for value in all_values(polynomials):
        for coordinate in m.r.scalar_coordinates(E3.coerce(value)):
            count += 1
            assert coordinate.denominator == one, (label, count, coordinate)
    return count


def serialize_h(path, polynomial):
    lines = ["parameter_monomial\tcoefficient_exact"]
    for monomial, coefficient in sorted(polynomial.items()):
        lines.append(f"{monomial!r}\t{m.e3_exact(coefficient)}")
    text = "\n".join(lines) + "\n"
    path.write_text(text)
    return sha256(text.encode()).hexdigest(), len(lines) - 1


def source_inventory(path, generic_first, special_first, generic_p12, special_p12):
    lines = ["kind\tindex\tkey\tgeneric_sha256\tspecial_sha256"]
    lines.append(
        "P12\t12\t('X0_RAW', 12)\t"
        + m.polynomial_digest(generic_p12) + "\t"
        + m.polynomial_digest(special_p12)
    )
    for index, ((key, grow, grhs), (skey, srow, srhs)) in enumerate(
        zip(generic_first, special_first)
    ):
        assert key == skey
        gsource = source_polynomial(grow, grhs)
        ssource = source_polynomial(srow, srhs)
        lines.append(
            f"FIRST\t{index}\t{key!r}\t{m.polynomial_digest(gsource)}\t"
            f"{m.polynomial_digest(ssource)}"
        )
    text = "\n".join(lines) + "\n"
    path.write_text(text)
    return sha256(text.encode()).hexdigest()


def main():
    outdir = Path(os.environ["TD6_OUTPUT_DIR"]).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    print("producer=TD6-V85TF1-LITERAL-TOTAL-F-RAW-P12-SOURCE")
    print(f"requested_q_exponent={m.REQUESTED_Q_EXPONENT}")
    print("total_base_ring=Q[C,V,U] localized at U*H*B3")
    print("total_parameter_F=C*U-V^2+U^3")
    print("F_independent_after_U_localization=true")
    print("PREVIOUS_POLE_used=false")
    print("staged_CURRENT_used=false")
    print(f"frozen_generic_parent_sha256={TARGET_SHA256}")
    print(f"frozen_special_certificate_sha256={CERTIFICATE_SHA256}", flush=True)

    generic_bands, generic_first, generic_p12 = build_generic_source()
    special_bands, special_first, special_p12 = build_special_source()
    del generic_bands, special_bands
    assert len(generic_first) == len(special_first)
    assert len(generic_p12) == len(special_p12) == 2893

    generic_sources = [source_polynomial(row, rhs) for _, row, rhs in generic_first]
    special_sources = [source_polynomial(row, rhs) for _, row, rhs in special_first]
    for index, (generic, special) in enumerate(zip(generic_sources, special_sources)):
        assert specialize_polynomial(generic) == special, ("FIRST_base_change", index)
    assert specialize_polynomial(generic_p12) == special_p12
    print(f"literal_base_change_FIRST_rows={len(generic_sources)}")
    print("literal_base_change_FIRST_exact=true")
    print("literal_base_change_P12_exact=true")

    parameter_labels = set()
    for polynomial in [generic_p12, *generic_sources]:
        for monomial in polynomial:
            parameter_labels.update(monomial)
    assert parameter_labels == set(range(132)), (
        min(parameter_labels), max(parameter_labels), len(parameter_labels)
    )
    print("transport_free_parameter_labels=0..131")
    print("all_132_transport_free_section_coordinates_retained=true")

    p12_multiplier, first_multipliers, used_keys = read_frozen_multipliers(
        special_first
    )
    special_identity = multiply(p12_multiplier, special_p12)
    special_terms = [multiply(p12_multiplier, special_p12)]
    for multiplier, source in zip(first_multipliers, special_sources):
        if multiplier:
            term = multiply(multiplier, source)
            special_terms.append(term)
            special_identity = add(special_identity, term)
    special_target = {(): E3(Rat3(SPECIAL_CLEARER))}
    assert special_identity == special_target
    assert specialize_e3(E3(Rat3(TOTAL_TARGET))) == special_target[()]
    print("frozen_V82QST3_special_identity_rebuilt_exact=true")
    print("total_target_specializes_to_V82QST3_clearer=true")

    total_terms = [multiply(p12_multiplier, generic_p12)]
    total_identity = dict(total_terms[0])
    for multiplier, source in zip(first_multipliers, generic_sources):
        if multiplier:
            term = multiply(multiplier, source)
            total_terms.append(term)
            total_identity = add(total_identity, term)
    total_target = {(): E3(Rat3(TOTAL_TARGET))}
    residual = add(total_target, total_identity, -1)
    assert residual and specialize_polynomial(residual) == {}
    quotient, division_coordinate_count = divide_polynomial_by_f(residual)
    assert add(total_identity, scale(quotient, E3(Rat3(F)))) == total_target
    print(f"total_F_residual_terms={len(residual)}")
    print(f"total_F_quotient_terms={len(quotient)}")
    print(f"total_F_division_coordinate_count={division_coordinate_count}")
    print("total_F_division_exact=true")
    print("total_F_not_inverted=true")

    active_index = min(used_keys)
    active_term = multiply(first_multipliers[active_index], generic_sources[active_index])
    assert active_term
    assert add(add(total_identity, active_term, -1), scale(quotient, E3(Rat3(F)))) != total_target
    assert add(add(total_identity, total_terms[0], -1), scale(quotient, E3(Rat3(F)))) != total_target
    print(f"FIRST_omission_negative_control_index={active_index}")
    print("FIRST_omission_negative_control=true")
    print("P12_omission_negative_control=true")

    audit_values = list(all_values([
        p12_multiplier, *first_multipliers,
        generic_p12, *generic_sources,
        *total_terms, quotient,
    ]))
    value_count, coordinate_count, common = assert_denominators_allowed(
        audit_values, "total_family"
    )
    common_scalar = E3(Rat3(common))
    cleared_multipliers = [
        scale(p12_multiplier, common_scalar),
        *[scale(value, common_scalar) for value in first_multipliers],
    ]
    cleared_terms = [scale(value, common_scalar) for value in total_terms]
    cleared_quotient = scale(quotient, common_scalar)
    cleared_target = scale(total_target, common_scalar)
    cleared_identity = {}
    for term in cleared_terms:
        cleared_identity = add(cleared_identity, term)
    cleared_identity = add(
        cleared_identity, scale(cleared_quotient, E3(Rat3(F)))
    )
    assert cleared_identity == cleared_target
    polynomial_coordinate_count = assert_polynomial_coordinates(
        [*cleared_multipliers, *cleared_terms, cleared_quotient],
        "cleared_total_family",
    )
    print(f"denominator_audited_value_count={value_count}")
    print(f"denominator_audited_scalar_coordinate_count={coordinate_count}")
    print(f"total_family_common_denominator=({common})")
    print(f"total_family_common_denominator_factor={common.factor()}")
    print("total_family_denominator_radical_subset_U_H_B3=true")
    print(f"cleared_polynomial_scalar_coordinate_count={polynomial_coordinate_count}")
    print("cleared_total_family_identity_exact=true")

    h_path = outdir / "TOTAL_F_H_CLEARED.tsv"
    h_sha, h_terms = serialize_h(h_path, cleared_quotient)
    inventory_path = outdir / "TOTAL_F_SOURCE_INVENTORY.tsv"
    inventory_sha = source_inventory(
        inventory_path, generic_first, special_first, generic_p12, special_p12
    )
    digest_lines = [
        f"generic_parent_sha256={TARGET_SHA256}",
        f"special_certificate_sha256={CERTIFICATE_SHA256}",
        f"q_exponent={m.REQUESTED_Q_EXPONENT}",
        f"target={TOTAL_TARGET}",
        f"common={common}",
        f"p12={m.polynomial_digest(generic_p12)}",
        f"quotient={m.polynomial_digest(quotient)}",
        f"cleared_quotient={m.polynomial_digest(cleared_quotient)}",
        f"h_file_sha256={h_sha}",
        f"source_inventory_sha256={inventory_sha}",
    ]
    result_stream = "\n".join(digest_lines) + "\n"
    result_path = outdir / "TOTAL_F_EXACT_RESULT.txt"
    result_path.write_text(result_stream)
    print(f"total_F_h_cleared_path={h_path}")
    print(f"total_F_h_cleared_terms={h_terms}")
    print(f"total_F_h_cleared_sha256={h_sha}")
    print(f"total_F_source_inventory_path={inventory_path}")
    print(f"total_F_source_inventory_sha256={inventory_sha}")
    print(f"total_F_exact_result_path={result_path}")
    print(f"total_F_exact_result_sha256={sha256(result_stream.encode()).hexdigest()}")
    print("literal_total_F_identity_emitted=true")
    print("positive_F_arcs_in_this_normalized_slice_excluded=true")
    print("q_dead_stretch_correction_orbit_pole_center_boundary_moduli_totalized=false")
    print("whole_fixed_A3_killed=false")
    print("whole_TD6_killed=false")
    print("SP2_killed=false")
    print("JC2_resolved=false")
    print("TD6-V85TF1-LITERAL-TOTAL-F-RAW-P12-SOURCE PASS")


if __name__ == "__main__":
    main()
