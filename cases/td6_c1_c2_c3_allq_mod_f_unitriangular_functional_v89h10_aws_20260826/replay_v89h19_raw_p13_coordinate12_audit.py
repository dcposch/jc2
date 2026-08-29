#!/usr/bin/env python3
"""Extract literal raw P13 E3 coordinate 12 before and after F=0."""

from hashlib import sha256
import importlib.util
import os
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
H15_PATH = HERE / "replay_v89h15_allq_p13_full_normal_form.py"
H15_SHA = "6c06bed1dde0062d4eeed09b26f9cee11b10259f824fecd319fb3ae0c7a4fc7f"
assert sha256(H15_PATH.read_bytes()).hexdigest() == H15_SHA
spec = importlib.util.spec_from_file_location("td6_v89h19_h15_parent", H15_PATH)
h15 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = h15
spec.loader.exec_module(h15)

m, v87, h6 = h15.m, h15.v87, h15.h6


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


def main():
    outdir = Path(os.environ["TD6_OUTPUT_DIR"]).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    assert os.environ.get("AWS_RUN_TAG", "").startswith("td6_v89h19_raw_p13_c12_")
    events, bands, seen = v87.build_bands()
    p13 = h15.compile_current_degree(bands, 13)
    assert events == 2 and len(p13) == 2757
    assert set(seen) == set(h15.ALL_Q) and all(seen[e] == 1 for e in h15.ALL_Q)
    specialized = h6.specialize_polynomial(p13)
    total_records = coordinate_records(p13)
    specialized_records = coordinate_records(specialized)
    assert total_records and specialized_records

    lines = ["stage\tparameter_monomial\tq_monomial\tnumerator\tdenominator"]
    lines.extend(
        f"total\t{parameter!r}\t{q!r}\t{numerator}\t{denominator}"
        for parameter, q, numerator, denominator in total_records
    )
    lines.extend(
        f"F0\t{parameter!r}\t{q!r}\t{numerator}\t{denominator}"
        for parameter, q, numerator, denominator in specialized_records
    )
    text = "\n".join(lines) + "\n"
    (outdir / "RAW_P13_COORDINATE12.tsv").write_text(text)
    record_sha = sha256(text.encode()).hexdigest()
    expected = (((), (), "3500000000/9*U", "V"),)
    direct_unit = specialized_records == expected
    total_parameter_support = tuple(sorted({record[0] for record in total_records}))
    total_q_support = tuple(sorted({record[1] for record in total_records}))
    f0_parameter_support = tuple(sorted({record[0] for record in specialized_records}))
    f0_q_support = tuple(sorted({record[1] for record in specialized_records}))
    omitted = total_records[1:]
    assert omitted != total_records
    result = (
        "literal_P13_parameter_terms=2757\n"
        "all_132_transport_variables_retained=true\n"
        "all_22_q_coordinates_retained=true\n"
        f"total_coordinate12_record_count={len(total_records)}\n"
        f"total_coordinate12_parameter_support={total_parameter_support!r}\n"
        f"total_coordinate12_q_support={total_q_support!r}\n"
        f"F0_coordinate12_record_count={len(specialized_records)}\n"
        f"F0_coordinate12_parameter_support={f0_parameter_support!r}\n"
        f"F0_coordinate12_q_support={f0_q_support!r}\n"
        f"F0_coordinate12_direct_raw_unit={str(direct_unit).lower()}\n"
        f"coordinate_records_sha256={record_sha}\n"
        "active_record_omission_negative_control=true\n"
        "FIRST_membership_certificate_needed=" + str(not direct_unit).lower() + "\n"
        "independent_total_F_unit_claim=false\nwhole_TD6_killed=false\nJC2_resolved=false\n"
    )
    (outdir / "RAW_P13_COORDINATE12_RESULT.txt").write_text(result)
    print(result, end="")
    print(f"result_sha256={sha256(result.encode()).hexdigest()}")
    banner = "DIRECT-UNIT" if direct_unit else "FIRST-CANCELLATION-REQUIRED"
    print(f"TD6-V89H19-RAW-P13-COORDINATE12-{banner} PASS")


if __name__ == "__main__":
    main()
