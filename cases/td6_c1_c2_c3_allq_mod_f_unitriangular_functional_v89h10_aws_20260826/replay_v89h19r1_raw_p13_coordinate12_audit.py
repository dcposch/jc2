#!/usr/bin/env python3
"""Repaired literal raw-P13 coordinate-12 audit with real source omission."""

from hashlib import sha256
import importlib.util
import os
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
H15_PATH = HERE / "replay_v89h15_allq_p13_full_normal_form.py"
H15_SHA = "6c06bed1dde0062d4eeed09b26f9cee11b10259f824fecd319fb3ae0c7a4fc7f"
COUNT_ERRATUM = HERE / "P13_FULL_NORMAL_FORM_VECTOR_RECORD_ERRATUM.md"
COUNT_ERRATUM_SHA = "27d8289d7215d16806d1f1197b137acc7d49b0d75a05c766833eaaa38db44418"
PINNED_MANIFESTS = {
    "SOURCE_P13_FULL_NORMAL_FORM.sha256":
        "6cb1b86d34d90fe28f7bfa24b0f8e78819372c425554b31a65a17a30d9f4d88c",
    "SOURCE_P12_FULL_NORMAL_FORM.sha256":
        "03682023155e2a9e0b0d631865f2e4ea33891f026009714c3c68a5724fb6088a",
    "SOURCE_P12_FLAG.sha256":
        "ac37d22986ab4257f95c50eef593865ef90b603cda97886ffe6fda500390eba8",
    "PAYLOAD_CLOSURE.sha256":
        "cbe7e0be9d49f5aa994790332e2fe0368c32780eac81ee3ddededdf7bb3d5cff",
}

# Fixed from the AWS-only source-addend census before the dual producer launch.
EXPECTED_ACTIVE_LABELS = (
    "f1_times_dg2:i=13:j=1",
    "2f2_times_dg1:i=12:j=2",
    "minus2_df1_times_g2:i=13:j=1",
    "minus_df2_times_g1:i=12:j=2",
)
EXPECTED_OMISSION_LABEL = EXPECTED_ACTIVE_LABELS[0]


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def verify_manifest(path):
    for line in path.read_text().splitlines():
        expected, relative = line.split(maxsplit=1)
        target = HERE / relative
        assert target.is_file(), target
        assert digest(target) == expected, target


assert digest(H15_PATH) == H15_SHA
assert digest(COUNT_ERRATUM) == COUNT_ERRATUM_SHA
for name, expected in PINNED_MANIFESTS.items():
    path = HERE / name
    assert digest(path) == expected
    verify_manifest(path)

spec = importlib.util.spec_from_file_location("td6_v89h19r1_h15_parent", H15_PATH)
h15 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = h15
spec.loader.exec_module(h15)

m, v87, h6 = h15.m, h15.v87, h15.h6
QPoly = h15.QPoly


def canonical(polynomial):
    return v87.clean({
        monomial: QPoly.coerce(value)
        for monomial, value in polynomial.items()
    })


def raw_degree_contributions(bands, degree):
    """Return ordered literal addends used by H15's degree compiler."""
    v87.configure_qd(None)
    qd, nr = m.r.qd, m.r.qd.nr
    f1, f2, f3 = (bands[("f", power)] for power in (1, 2, 3))
    g1, g2, g3 = (bands[("g", power)] for power in (1, 2, 3))
    contributions = []

    def emit(label, polynomial, scale=1):
        contribution = canonical(nr.add_polynomial({}, polynomial, scale))
        if contribution:
            contributions.append((label, contribution))

    for i, left in enumerate(f1):
        j = degree - i + 1
        if 1 <= j < len(g2):
            emit(
                f"f1_times_dg2:i={i}:j={j}",
                nr.multiply_affine(left, nr.scale_affine(g2[j], j)),
            )
    for i, left in enumerate(f2):
        j = degree - i + 1
        if 1 <= j < len(g1):
            emit(
                f"2f2_times_dg1:i={i}:j={j}",
                nr.multiply_affine(left, nr.scale_affine(g1[j], j)),
                2,
            )
    for i, form in enumerate(f3):
        multiplier = qd.Q_PRIME.get(degree - i, QPoly())
        if multiplier:
            emit(
                f"3f3_times_qprime:i={i}:qdegree={degree-i}",
                nr.affine_polynomial(form),
                3 * multiplier,
            )
    g_degree = degree - 14
    if 0 <= g_degree < len(g3):
        emit(
            f"minus45_g3:degree={g_degree}",
            nr.affine_polynomial(g3[g_degree]),
            -45,
        )
    for i in range(1, len(f1)):
        j = degree - (i - 1)
        if 0 <= j < len(g2):
            emit(
                f"minus2_df1_times_g2:i={i}:j={j}",
                nr.multiply_affine(nr.scale_affine(f1[i], i), g2[j]),
                -2,
            )
    for i in range(1, len(f2)):
        j = degree - (i - 1)
        if 0 <= j < len(g1):
            emit(
                f"minus_df2_times_g1:i={i}:j={j}",
                nr.multiply_affine(nr.scale_affine(f2[i], i), g1[j]),
                -1,
            )
    return tuple(contributions)


def sum_contributions(contributions):
    nr = m.r.qd.nr
    polynomial = {}
    for _, contribution in contributions:
        polynomial = nr.add_polynomial(polynomial, contribution)
    return canonical(polynomial)


def coordinate_records(polynomial):
    records = []
    for parameter_monomial, qpoly in sorted(polynomial.items()):
        for q_monomial, coefficient in sorted(qpoly.coefficients.items()):
            coordinate = m.r.scalar_coordinates(coefficient)[12]
            if coordinate:
                records.append((
                    parameter_monomial,
                    q_monomial,
                    str(coordinate.numerator),
                    str(coordinate.denominator),
                ))
    return tuple(records)


def records_text(stages):
    lines = ["stage\tparameter_monomial\tq_monomial\tnumerator\tdenominator"]
    for stage, records in stages:
        lines.extend(
            f"{stage}\t{parameter!r}\t{q!r}\t{numerator}\t{denominator}"
            for parameter, q, numerator, denominator in records
        )
    return "\n".join(lines) + "\n"


def main():
    outdir = Path(os.environ["TD6_OUTPUT_DIR"]).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    assert os.environ.get("AWS_RUN_TAG", "").startswith(
        "td6_v89h19r1_raw_p13_c12_"
    )
    events, bands, seen = v87.build_bands()
    contributions = raw_degree_contributions(bands, 13)
    reconstructed = sum_contributions(contributions)
    parent = h15.compile_current_degree(bands, 13)
    assert reconstructed == parent
    assert events == 2 and len(parent) == 2757
    assert set(seen) == set(h15.ALL_Q) and all(seen[e] == 1 for e in h15.ALL_Q)

    active = []
    for label, contribution in contributions:
        records = coordinate_records(h6.specialize_polynomial(contribution))
        if records:
            active.append((label, records))
    assert tuple(label for label, _ in active) == EXPECTED_ACTIVE_LABELS, active
    if not EXPECTED_OMISSION_LABEL:
        print("H19R1_PREFLIGHT_ACTIVE_LABELS=" + repr(tuple(label for label, _ in active)))
        return
    assert active[0][0] == EXPECTED_OMISSION_LABEL, active
    assert sum(label == EXPECTED_OMISSION_LABEL for label, _ in contributions) == 1

    omitted_contributions = tuple(
        item for item in contributions if item[0] != EXPECTED_OMISSION_LABEL
    )
    omitted_parent = sum_contributions(omitted_contributions)
    assert omitted_parent != parent
    omitted_specialized = h6.specialize_polynomial(omitted_parent)

    specialized = h6.specialize_polynomial(parent)
    total_records = coordinate_records(parent)
    specialized_records = coordinate_records(specialized)
    omitted_records = coordinate_records(omitted_specialized)
    assert total_records and specialized_records
    assert omitted_records != specialized_records

    text = records_text((
        ("total", total_records),
        ("F0", specialized_records),
        ("F0_OMIT_SOURCE_ADDEND", omitted_records),
    ))
    (outdir / "RAW_P13_COORDINATE12_R1.tsv").write_text(text)
    record_sha = sha256(text.encode()).hexdigest()
    active_text = records_text(tuple(
        (label, records) for label, records in active
    ))
    (outdir / "RAW_P13_COORDINATE12_ACTIVE_ADDENDS_R1.tsv").write_text(active_text)
    active_sha = sha256(active_text.encode()).hexdigest()

    expected = (((), (), "3500000000/9*U", "V"),)
    direct_unit = specialized_records == expected
    total_parameter_support = tuple(sorted({record[0] for record in total_records}))
    total_q_support = tuple(sorted({record[1] for record in total_records}))
    f0_parameter_support = tuple(sorted({record[0] for record in specialized_records}))
    f0_q_support = tuple(sorted({record[1] for record in specialized_records}))
    result = (
        "literal_P13_parameter_terms=2757\n"
        f"literal_source_addend_count={len(contributions)}\n"
        "source_addend_sum_equals_frozen_H15_compiler=true\n"
        "all_132_transport_variables_retained=true\n"
        "all_22_q_coordinates_retained=true\n"
        f"total_coordinate12_record_count={len(total_records)}\n"
        f"total_coordinate12_parameter_support={total_parameter_support!r}\n"
        f"total_coordinate12_q_support={total_q_support!r}\n"
        f"F0_coordinate12_record_count={len(specialized_records)}\n"
        f"F0_coordinate12_parameter_support={f0_parameter_support!r}\n"
        f"F0_coordinate12_q_support={f0_q_support!r}\n"
        f"F0_coordinate12_direct_raw_unit={str(direct_unit).lower()}\n"
        f"source_omission_label={EXPECTED_OMISSION_LABEL}\n"
        "source_omission_applied_before_aggregation=true\n"
        "source_omission_changes_F0_coordinate12=true\n"
        f"coordinate_records_sha256={record_sha}\n"
        f"active_source_addends_sha256={active_sha}\n"
        "FIRST_membership_certificate_needed=" + str(not direct_unit).lower() + "\n"
        "independent_total_F_unit_claim=false\nwhole_TD6_killed=false\nJC2_resolved=false\n"
    )
    (outdir / "RAW_P13_COORDINATE12_RESULT_R1.txt").write_text(result)
    print(result, end="")
    print(f"result_sha256={sha256(result.encode()).hexdigest()}")
    banner = "DIRECT-UNIT" if direct_unit else "FIRST-CANCELLATION-REQUIRED"
    print(f"TD6-V89H19R1-RAW-P13-COORDINATE12-{banner} PASS")


if __name__ == "__main__":
    main()
