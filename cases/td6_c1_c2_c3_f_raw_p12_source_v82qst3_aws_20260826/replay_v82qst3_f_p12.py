#!/usr/bin/env python3
"""Divisor-safe genuine-P12 source certificate on the raw F=0 A3 fibre."""

from hashlib import sha256
import importlib.util
import os
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
TARGET = Path(os.environ["V82QST2_SOURCE_FILE"]).resolve()
TARGET_SHA256 = "5a1054269237d9a2da5c7f5e51ae001ad59f61607ac36f2e7a9b059c972c74d5"
assert sha256(TARGET.read_bytes()).hexdigest() == TARGET_SHA256

spec = importlib.util.spec_from_file_location("td6_v82qst3_f_p12_parent", TARGET)
raw = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = raw
spec.loader.exec_module(raw)

m = raw.m
EJet, E3, Rat3 = raw.EJet, m.E3, raw.Rat3
CAPTURE = {}
ORIGINAL_PARAMETERIZE = m.parameterize


def base_polynomial(polynomial):
    return raw.m.split_column(polynomial)


def scale(polynomial, coefficient):
    coefficient = E3.coerce(coefficient)
    return {
        monomial: coefficient * E3.coerce(value)
        for monomial, value in polynomial.items()
        if coefficient * E3.coerce(value)
    }


def add(left, right, coefficient=1):
    coefficient = E3.coerce(coefficient)
    out = dict(left)
    for monomial, value in right.items():
        total = out.get(monomial, E3()) + coefficient * E3.coerce(value)
        if total:
            out[monomial] = total
        else:
            out.pop(monomial, None)
    return out


def multiply(left, right):
    out = {}
    for left_monomial, left_value in left.items():
        for right_monomial, right_value in right.items():
            monomial = tuple(sorted(left_monomial + right_monomial))
            total = (
                out.get(monomial, E3())
                + E3.coerce(left_value) * E3.coerce(right_value)
            )
            if total:
                out[monomial] = total
            else:
                out.pop(monomial, None)
    return out


def base_source(row, rhs):
    return base_polynomial(m.source_polynomial(row, rhs))


def parameterize_capture(nvariables, rows, stage):
    result = ORIGINAL_PARAMETERIZE(nvariables, rows, stage)
    if stage == "first_F_raw":
        CAPTURE["first_pivots"] = result[0]
        CAPTURE["first_factors"] = result[3]
    return result


def polynomial_values(polynomials):
    for polynomial in polynomials:
        yield from polynomial.values()


def denominator(values):
    return raw.monic(m.denominator_for(list(values)))


def assert_polynomial_coordinates(value, label):
    count = 0
    polynomial_one = Rat3(1).denominator
    for coordinate in m.r.scalar_coordinates(E3.coerce(value)):
        count += 1
        assert coordinate.denominator == polynomial_one, (label, count, coordinate)
        assert not raw.polynomial_uses_formal_c(coordinate.numerator), (label, count)
    return count


def serialize_polynomial(lines, source_kind, source_index, source_key, polynomial):
    for monomial, coefficient in sorted(polynomial.items()):
        lines.append(
            "\t".join(
                (
                    source_kind,
                    str(source_index),
                    repr(source_key),
                    repr(monomial),
                    repr(m.e3_exact(coefficient)),
                )
            )
        )


def run_p12_source(bands, pole_f, pole_g, first_rows, first_forms, outdir):
    del pole_f, pole_g, first_forms
    first_pivots = CAPTURE["first_pivots"]
    raw_current = m.qd.compile_current(
        *[bands[("f", power)] for power in (1, 2, 3)],
        *[bands[("g", power)] for power in (1, 2, 3)],
    )
    assert len(raw_current) > 12
    p12 = {
        monomial: EJet.coerce(coefficient)
        for monomial, coefficient in raw_current[12].items()
        if coefficient
    }
    p12_base = base_polynomial(p12)
    remainder, quotients = m.divide_jet(p12, first_pivots)
    relations = m.lift_relations(quotients, first_pivots, len(first_rows))
    m.exact_source_replay(p12, remainder, relations, first_rows)
    remainder_base = base_polynomial(remainder)
    assert set(remainder_base) == {()}
    residual = remainder_base[()]
    assert residual
    inverse = residual.inverse()
    assert inverse * residual == E3(1)

    source_identity = {}
    base_relations = []
    first_sources = []
    for relation, (_, row, rhs) in zip(relations, first_rows):
        relation_base = base_polynomial(relation)
        source_base = base_source(row, rhs)
        base_relations.append(relation_base)
        first_sources.append(source_base)
        source_identity = add(
            source_identity,
            multiply(relation_base, source_base),
        )
    target = add(p12_base, remainder_base, -1)
    assert source_identity == target
    nonzero_relation = next(index for index, value in enumerate(base_relations) if value)
    omitted = {}
    for index, (relation, source) in enumerate(zip(base_relations, first_sources)):
        if index != nonzero_relation:
            omitted = add(omitted, multiply(relation, source))
    assert omitted != target

    p12_multiplier = {(): inverse}
    first_multipliers = [scale(relation, -inverse) for relation in base_relations]
    unit_identity = multiply(p12_multiplier, p12_base)
    for multiplier, source in zip(first_multipliers, first_sources):
        unit_identity = add(unit_identity, multiply(multiplier, source))
    assert unit_identity == {(): E3(1)}

    termwise = [multiply(p12_multiplier, p12_base)]
    termwise.extend(
        multiply(multiplier, source)
        for multiplier, source in zip(first_multipliers, first_sources)
        if multiplier
    )
    values = [residual, inverse]
    values.extend(p12_base.values())
    values.extend(polynomial_values(first_sources))
    values.extend(polynomial_values([p12_multiplier, *first_multipliers]))
    values.extend(polynomial_values(termwise))
    clearer = denominator(values)
    assert raw.factors_only_allowed(clearer), clearer.factor()

    clearer_scalar = E3.coerce(m.scalar(clearer))
    cleared_p12_multiplier = scale(p12_multiplier, clearer_scalar)
    cleared_first_multipliers = [
        scale(multiplier, clearer_scalar)
        for multiplier in first_multipliers
    ]
    cleared_termwise = [scale(polynomial, clearer_scalar) for polynomial in termwise]
    cleared_identity = multiply(cleared_p12_multiplier, p12_base)
    for multiplier, source in zip(cleared_first_multipliers, first_sources):
        cleared_identity = add(cleared_identity, multiply(multiplier, source))
    assert cleared_identity == {(): clearer_scalar}

    coordinate_count = 0
    for label, polynomial in [
        ("P12_multiplier", cleared_p12_multiplier),
        *[
            (f"FIRST_{index}_multiplier", polynomial)
            for index, polynomial in enumerate(cleared_first_multipliers)
        ],
        *[
            (f"termwise_{index}", polynomial)
            for index, polynomial in enumerate(cleared_termwise)
        ],
    ]:
        for value in polynomial.values():
            coordinate_count += assert_polynomial_coordinates(value, label)

    lines = [
        "source_kind\tsource_index\tsource_key\tparameter_monomial\tcoefficient_exact"
    ]
    serialize_polynomial(lines, "P12", 12, ("X0_RAW", 12), cleared_p12_multiplier)
    for index, (multiplier, (key, _, _)) in enumerate(
        zip(cleared_first_multipliers, first_rows)
    ):
        if multiplier:
            serialize_polynomial(lines, "FIRST", index, key, multiplier)
    certificate_text = "\n".join(lines) + "\n"
    certificate_path = outdir / "F_RAW_P12_CLEARED_SOURCE_CERTIFICATE.tsv"
    certificate_path.write_text(certificate_text)

    print("producer=TD6-V82QST3-F-RAW-GENUINE-P12-SOURCE")
    print(f"requested_q_exponent={m.REQUESTED_Q_EXPONENT}")
    print("source_center_C0=(V^2-U^3)/U")
    print("raw_F_identity_zero=true")
    print("certificate_object=genuine_raw_P12_before_PREVIOUS_and_CURRENT")
    print("later_staged_X0_12_used=false")
    print(f"genuine_P12_base_term_count={len(p12_base)}")
    print(f"genuine_P12_base_sha256={m.polynomial_digest(p12_base)}")
    print(f"first_source_nonzero_rows={sum(bool(value) for value in base_relations)}")
    print(f"first_source_multiplier_terms={sum(len(value) for value in base_relations)}")
    print(f"F_raw_P12_residual_exact={m.e3_exact(residual)}")
    print(f"F_raw_P12_residual_sha256={m.e3_digest(residual)}")
    print(f"F_raw_P12_inverse_exact={m.e3_exact(inverse)}")
    print(f"F_raw_P12_certificate_clearer=({clearer})")
    print(f"F_raw_P12_certificate_clearer_factor={clearer.factor()}")
    print(f"F_raw_P12_certificate_outside_factors={raw.outside_factors(clearer)}")
    print(f"F_raw_P12_cleared_coordinate_count={coordinate_count}")
    print(f"F_raw_P12_certificate_path={certificate_path}")
    print(
        "F_raw_P12_certificate_sha256="
        + sha256(certificate_text.encode()).hexdigest()
    )
    print("F_raw_P12_exact_source_replay=true")
    print("F_raw_P12_omission_negative_control=true")
    print("F_raw_P12_cleared_identity_exact=true")
    print("F_raw_P12_registered_open_killed=true")
    print("V82QST2_global_denominator_was_certificate_overapproximation=true")
    print("staged_CURRENT_tangent_table_adjudicated=false")
    print("total_family_s_equals_sum_hifi_plus_Fh_emitted=false")
    print("positive_F_valuation_arcs_killed=false")
    print("whole_fixed_A3_killed=false")
    print("whole_TD6_killed=false")
    print("SP2_killed=false")
    print("JC2_resolved=false")
    print("TD6-V82QST3-F-RAW-GENUINE-P12-SOURCE PASS")


def main():
    m.parameterize = parameterize_capture
    raw.run_staged_f_raw = run_p12_source
    raw.main()


if __name__ == "__main__":
    main()
