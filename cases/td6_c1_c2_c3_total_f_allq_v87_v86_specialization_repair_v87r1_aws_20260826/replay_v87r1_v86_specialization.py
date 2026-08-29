#!/usr/bin/env python3
"""Exact V87 all-q -> V86 q2 specialization comparator.

Substantive execution is AWS-gated.  It rebuilds live V87 source and h
objects and compares exact serialized q2 slices against reviewed V86 output
artifacts, rather than inferring compatibility from shared code.
"""

from ast import literal_eval
import csv
from hashlib import sha256
import importlib.util
import os
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
V87_PATH = HERE / "replay_v87tfaq_total_f_allq.py"
PINS = {
    "replay_v87tfaq_total_f_allq.py": "7c0890abbce996a221f9389372fa3705742d6ecd72531891bfeb5dfc2f1b9463",
    "V87_RESULT.md": "6e22c6ac16f9e164b760367cf65b970649e9235f185e8ec82f8e28dbd6859bda",
    "V87_FREEZE.sha256": "ef39fef7983ed3251bc21b3dd4f53db075f816cd95ffb7a38511956d7d9c60b9",
    "V87_EVIDENCE.sha256": "074072f04a88b2e74e1545afdbdd173e8dbc0d68bd2052b6ea37ebad05e754c5",
    "V87_SOURCE.sha256": "f82ebe8ef8018542c02d9cbe3654c84b2c6336f442d5e8b83633cdeebbf3e874",
    "V87_TOTAL_F_ALLQ_SOURCE_INVENTORY.tsv": "079447d97638f18b7807cdd84b1178f9969d3f93727c7ab40588079586160a68",
    "V87_TOTAL_F_ALLQ_H_INVENTORY.tsv": "85d0c375c3a042f3b80567106adf4c0e5115f7774e18dfd298aad3faecbbb32b",
    "V87_TOTAL_F_ALLQ_EXACT_RESULT.txt": "5b27705017fce762b8622f32978dfbd6d13bcb75c1ffe2b85e156c003f94f570",
    "V86_RESULT.md": "22fb1c6c437e26f212a38857157050f68e773dcee8482e3d384da47fffc09c02",
    "V86_FREEZE.sha256": "82083dd26b44766779beb2fec64e34f0842769a8f81fe73aee1f105cb8510c79",
    "V86_EVIDENCE.sha256": "492117581f014bdc60bc13262a4d6ae89c478646c9f4a79b1db29206e1bcf94e",
    "V86_SOURCE.sha256": "d86ec28236b9b97746150d04b3a0891ec05f5bc6eed02e78fc02b0f864d221f6",
    "V86_TOTAL_F_Q2_SOURCE_INVENTORY.tsv": "450c478c6e8d9e3bbdeef4470dc2c3fdfa999f74713e27cc500861f8e1938597",
    "V86_TOTAL_F_Q2_HF_CLEARED.tsv": "89ecec18cea6547fe465fc4f6088f7f94ec9b6d717eefb33386f5b3fab6d49e0",
    "V86_TOTAL_F_Q2_HBETA_CLEARED.tsv": "590f88a20183a4d4363a4e14397084cae347838331abc6df536f60129f2f0384",
    "V86_TOTAL_F_Q2_EXACT_RESULT.txt": "50c91f3253a564e52d356ac6ea1e9216ab96e84abe95c7898ea96ec1d481f236",
    "V86_HOSTILE_REVIEW.md": "9e70d6ceef3572cecada81160357684c8478fb8994cfe7d6176793d58ca1532e",
    "V86_PROMOTION.md": "677513a291a64f577740bfc8852a94d9ac1218bd5a21aac69d5ef4fcdb0c0260",
}
for name, expected in PINS.items():
    assert sha256((HERE / name).read_bytes()).hexdigest() == expected, name

assert os.environ.get("AWS_RUN_TAG", "").startswith(
    "td6_v87r1_v86_specialization_"
)
assert os.environ.get("TD6_Q_EXPONENT") == "2"
assert os.environ.get("TD6_PIVOT_POLICY") == "ascending"
assert os.environ.get("TD6_PIVOT_SCOPE") == "all-staged"

spec = importlib.util.spec_from_file_location("td6_v87r1_v87_parent", V87_PATH)
v87 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = v87
spec.loader.exec_module(v87)

v86, v85, m = v87.v86, v87.v85, v87.m
QPoly, E3, Rat3 = v87.QPoly, v87.E3, v87.Rat3
F, H, U = v87.F, v87.H, v87.U
COMMON = U*H


def read_kv(path):
    out = {}
    for line in path.read_text().splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            out[key] = value
    return out


def read_source_inventory(path, full_column):
    out = {}
    with path.open(newline="") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            kind = row["kind"]
            index = int(row["index"])
            key = literal_eval(row["key"])
            out[(kind, index, key)] = row[full_column]
    assert len(out) == 39
    return out


def read_h_inventory(path):
    out = {}
    with path.open(newline="") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            out[row["generator"]] = row["full_sha256"]
    assert set(out) == {"F", *[f"q{e}" for e in v87.Q_EXPONENTS]}
    return out


def q2_slice(polynomial):
    out = {}
    for parameter_monomial, value in polynomial.items():
        degrees = {}
        for q_monomial, coefficient in value.coefficients.items():
            if all(exponent == 2 for exponent in q_monomial):
                degree = len(q_monomial)
                total = degrees.get(degree, E3()) + coefficient
                if total:
                    degrees[degree] = total
                else:
                    degrees.pop(degree, None)
        if degrees:
            out[parameter_monomial] = degrees
    return out


def constant_slice(polynomial):
    return {
        monomial: {0: E3.coerce(coefficient)}
        for monomial, coefficient in polynomial.items() if coefficient
    }


def slice_digest(polynomial):
    lines = []
    for monomial, degrees in sorted(polynomial.items()):
        for degree, coefficient in sorted(degrees.items()):
            lines.append(f"{monomial!r}\t{degree}\t{m.e3_exact(coefficient)}")
    return sha256(("\n".join(lines) + "\n").encode()).hexdigest()


def beta_zero_digest(polynomial):
    return m.polynomial_digest({
        monomial: degrees[0]
        for monomial, degrees in polynomial.items()
        if 0 in degrees and degrees[0]
    })


def serialize_cleared(path, polynomial):
    scalar = E3(Rat3(COMMON))
    lines = ["parameter_monomial\tbeta_degree\tcoefficient_exact"]
    coordinate_count = 0
    for monomial, degrees in sorted(polynomial.items()):
        for degree, coefficient in sorted(degrees.items()):
            cleared = scalar*coefficient
            for coordinate in m.r.scalar_coordinates(cleared):
                coordinate_count += 1
                assert coordinate.denominator == m.tri.ONE
            lines.append(f"{monomial!r}\t{degree}\t{m.e3_exact(cleared)}")
    text = "\n".join(lines) + "\n"
    path.write_text(text)
    return text, sha256(text.encode()).hexdigest(), len(lines)-1, coordinate_count


def main():
    outdir = Path(os.environ["TD6_OUTPUT_DIR"]).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    print("producer=TD6-V87R1-EXACT-V87-TO-V86-Q2-SPECIALIZATION")
    print("review_defect=missing_output_explicit_V87_to_V86_q2_comparison")
    print("v86_corrected_hostile_review=CONFIRMED")
    print("v86_promotion_consumed=true")
    print("comparison_serializer=parameter_monomial,beta_degree,E3_exact")
    print("all_non_q2_coordinates_specialized_to_zero=true", flush=True)

    event_count, bands, seen = v87.build_bands()
    total_first = v87.compile_first(bands)
    total_p12 = v87.compile_current_degree12(bands)
    total_sources = [
        v87.source_polynomial(row, rhs) for _, row, rhs in total_first
    ]
    assert event_count == 2 and set(seen.values()) == {1}
    assert len(total_first) == len(total_sources) == 38
    del bands
    print("live_V87_allq_source_rebuilt=true", flush=True)

    expected_v87_sources = read_source_inventory(
        HERE / "V87_TOTAL_F_ALLQ_SOURCE_INVENTORY.tsv", "full_sha256"
    )
    expected_v86_sources = read_source_inventory(
        HERE / "V86_TOTAL_F_Q2_SOURCE_INVENTORY.tsv", "full_sha256"
    )
    v86_rows = read_source_inventory(
        HERE / "V86_TOTAL_F_Q2_SOURCE_INVENTORY.tsv", "beta_zero_sha256"
    )
    comparison_lines = [
        "kind\tindex\tkey\tv87_full_sha256\tv87_q2_slice_sha256"
        "\tv86_full_sha256\tv86_beta_zero_sha256\tmatch"
    ]
    source_objects = [("P12", 12, ("X0_RAW", 12), total_p12)]
    source_objects.extend(
        ("FIRST", index, key, source)
        for index, ((key, _, _), source) in enumerate(
            zip(total_first, total_sources)
        )
    )
    for kind, index, key, polynomial in source_objects:
        lookup = (kind, index, key)
        live_full = v87.full_digest(polynomial)
        assert live_full == expected_v87_sources[lookup]
        sliced = q2_slice(polynomial)
        sliced_digest = slice_digest(sliced)
        assert sliced_digest == expected_v86_sources[lookup]
        assert beta_zero_digest(sliced) == v86_rows[lookup]
        comparison_lines.append(
            f"{kind}\t{index}\t{key!r}\t{live_full}\t{sliced_digest}\t"
            f"{expected_v86_sources[lookup]}\t{v86_rows[lookup]}\ttrue"
        )
    comparison_text = "\n".join(comparison_lines) + "\n"
    comparison_path = outdir / "V87_V86_Q2_SOURCE_COMPARISON.tsv"
    comparison_path.write_text(comparison_text)
    comparison_sha = sha256(comparison_text.encode()).hexdigest()
    print("all_39_V87_q2_source_slices_match_frozen_V86=true", flush=True)

    p12_multiplier, first_multipliers, _ = v85.read_frozen_multipliers(
        total_first
    )
    q_p12_multiplier = v87.embed(p12_multiplier)
    q_first_multipliers = [v87.embed(value) for value in first_multipliers]
    total_identity = v87.multiply(q_p12_multiplier, total_p12)
    for multiplier, source in zip(q_first_multipliers, total_sources):
        if multiplier:
            total_identity = v87.add(
                total_identity, v87.multiply(multiplier, source)
            )
    target = {(): QPoly(E3(Rat3(v87.TOTAL_TARGET)))}
    residual = v87.add(target, total_identity, -1)
    assert v87.max_q_degree([residual]) == 1
    residual_q_zero = v87.q_constant(residual)
    h_f, f_division_count = v85.divide_polynomial_by_f(residual_q_zero)
    assert m.polynomial_digest(h_f) == v87.EXPECTED_V85_H_SHA256
    h2 = {}
    for monomial, value in residual.items():
        coefficient = value.coefficients.get((2,), E3())
        if coefficient:
            h2[monomial] = QPoly(coefficient)
    assert h2
    q2_positive = {
        monomial: QPoly(0, {
            q_monomial: coefficient
            for q_monomial, coefficient in value.coefficients.items()
            if q_monomial and set(q_monomial) == {2}
        })
        for monomial, value in residual.items()
    }
    q2_positive = v87.clean(q2_positive)
    assert v87.scale(h2, QPoly.variable(2)) == q2_positive
    print("live_V87_hF_and_h2_rebuilt=true")
    print(f"F_division_coordinate_count={f_division_count}")
    print("live_V87_residual_total_q_degree=1", flush=True)

    expected_v87_h = read_h_inventory(
        HERE / "V87_TOTAL_F_ALLQ_H_INVENTORY.tsv"
    )
    live_hf_full = v87.full_digest(v87.embed(h_f))
    live_h2_full = v87.full_digest(h2)
    assert live_hf_full == expected_v87_h["F"]
    assert live_h2_full == expected_v87_h["q2"]

    v86_exact = read_kv(HERE / "V86_TOTAL_F_Q2_EXACT_RESULT.txt")
    hf_slice = constant_slice(h_f)
    h2_slice = q2_slice(h2)
    assert slice_digest(hf_slice) == v86_exact["hF_sha256"]
    assert slice_digest(h2_slice) == v86_exact["hbeta_sha256"]
    assert v86_exact["common"] == str(COMMON)

    hf_text, hf_sha, hf_terms, hf_coords = serialize_cleared(
        outdir / "V87_Q2_HF_CLEARED.tsv", hf_slice
    )
    h2_text, h2_sha, h2_terms, h2_coords = serialize_cleared(
        outdir / "V87_Q2_H2_CLEARED.tsv", h2_slice
    )
    assert hf_text == (HERE / "V86_TOTAL_F_Q2_HF_CLEARED.tsv").read_text()
    assert h2_text == (HERE / "V86_TOTAL_F_Q2_HBETA_CLEARED.tsv").read_text()
    assert hf_sha == PINS["V86_TOTAL_F_Q2_HF_CLEARED.tsv"]
    assert h2_sha == PINS["V86_TOTAL_F_Q2_HBETA_CLEARED.tsv"]
    print("V87_hF_cleared_table_byte_identical_to_V86=true")
    print("V87_h2_cleared_table_byte_identical_to_V86_hbeta=true")
    print(f"hF_cleared_terms={hf_terms};scalar_coordinates={hf_coords}")
    print(f"h2_cleared_terms={h2_terms};scalar_coordinates={h2_coords}")
    print("common_clearing=U*H")
    print("F_not_inverted=true")
    print("q2_not_inverted=true", flush=True)

    result_lines = [
        f"v87_result_sha256={PINS['V87_RESULT.md']}",
        f"v87_freeze_sha256={PINS['V87_FREEZE.sha256']}",
        f"v86_result_sha256={PINS['V86_RESULT.md']}",
        f"v86_freeze_sha256={PINS['V86_FREEZE.sha256']}",
        f"v86_hostile_review_sha256={PINS['V86_HOSTILE_REVIEW.md']}",
        f"v86_promotion_sha256={PINS['V86_PROMOTION.md']}",
        f"source_comparison_sha256={comparison_sha}",
        f"v87_hF_full_sha256={live_hf_full}",
        f"v87_h2_full_sha256={live_h2_full}",
        f"v86_hF_localized_sha256={slice_digest(hf_slice)}",
        f"v86_hbeta_localized_sha256={slice_digest(h2_slice)}",
        f"hF_cleared_sha256={hf_sha}",
        f"h2_cleared_sha256={h2_sha}",
        f"common={COMMON}",
    ]
    result_text = "\n".join(result_lines) + "\n"
    result_path = outdir / "V87_V86_Q2_SPECIALIZATION_EXACT_RESULT.txt"
    result_path.write_text(result_text)
    result_sha = sha256(result_text.encode()).hexdigest()
    print(f"source_comparison_sha256={comparison_sha}")
    print(f"hF_cleared_sha256={hf_sha}")
    print(f"h2_cleared_sha256={h2_sha}")
    print(f"exact_result_sha256={result_sha}")
    print("V87_to_reviewed_V86_q2_specialization_exact=true")
    print("V87_hostile_review_custody_gap_repaired=true")
    print("new_unit_q_or_chart_claim=false")
    print("whole_fixed_A3_killed=false")
    print("whole_TD6_killed=false")
    print("SP2_killed=false")
    print("JC2_resolved=false")
    print("TD6-V87R1-EXACT-V87-TO-V86-Q2-SPECIALIZATION PASS")


if __name__ == "__main__":
    main()
