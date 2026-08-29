#!/usr/bin/env python3
"""Minimal dual quotient-functional witness for the V89H6 q14 class."""

from hashlib import sha256
import importlib.util
import os
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
H6_PATH = HERE / "replay_v89h6_q14_mod_f_cokernel.py"
H6_SHA256 = "1301a09f0497abac5197de6b4afc0eba54b5c8de2b05d2cf11db63fab454d757"
assert sha256(H6_PATH.read_bytes()).hexdigest() == H6_SHA256
spec = importlib.util.spec_from_file_location("td6_v89h7_h6_parent", H6_PATH)
h6 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = h6
spec.loader.exec_module(h6)

h5, v87, v85, m = h6.h5, h6.v87, h6.v85, h6.m
QPoly, E3, Rat3 = h6.QPoly, h6.E3, h6.Rat3
C, V, U, F, H, B3 = h6.C, h6.V, h6.U, h6.F, h6.H, h6.B3
TAIL = h6.TAIL
FRESH_PRIME = 1000033
FRESH_C, FRESH_V, FRESH_U = 15, 4, 1


def reduce_quiet(polynomial, normalized, pivots):
    remainder = dict(polynomial)
    for pivot, source in zip(pivots, normalized):
        assert source.get((pivot,)) == QPoly(1)
        while True:
            target = next((
                monomial for monomial in sorted(remainder)
                if remainder[monomial] and pivot in monomial
            ), None)
            if target is None:
                break
            coefficient = remainder[target]
            reduced = list(target)
            reduced.remove(pivot)
            multiplier = {tuple(reduced): coefficient}
            remainder = v87.add(
                remainder, v87.multiply(multiplier, source), -1
            )
    return v87.clean(remainder)


def write_text(path, lines):
    text = "\n".join(lines) + "\n"
    path.write_text(text)
    return sha256(text.encode()).hexdigest()


def main():
    outdir = Path(os.environ["TD6_OUTPUT_DIR"]).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    assert os.environ.get("AWS_RUN_TAG", "").startswith(
        "td6_v89h7_q14_mod_f_dual_functional_"
    )
    print("producer=TD6-V89H7-Q14-MOD-F-DUAL-FUNCTIONAL")
    print(f"h6_parent_sha256={H6_SHA256}")
    print("functional_parameter_monomial=()")
    print("functional_q_monomial=(14,)")
    print("functional_E3_scalar_coordinate=0")
    print("exact_Q_and_fresh_prime=true", flush=True)

    events, bands, seen = v87.build_bands()
    total_first = v87.compile_first(bands)
    total_p12 = v87.compile_current_degree12(bands)
    first = h5.project_first(total_first)
    p12 = h5.project_polynomial(total_p12)
    assert events == 2 and len(first) == 38
    assert all(seen[exponent] == 1 for exponent in TAIL)
    original_sources = [
        v87.source_polynomial(row, rhs) for _, row, rhs in first
    ]
    _, raw_common = v87.assert_denominators_allowed([p12, *original_sources])
    assert raw_common.gcd(F).total_degree() == 0
    assert raw_common == U*H
    print("literal_transport_FIRST_P12_rebuilt=true")
    print(f"raw_source_common_denominator=({raw_common})")
    print("raw_source_denominator_coprime_F=true", flush=True)

    specialized_first = h6.specialize_first(first)
    specialized_p12 = h6.specialize_polynomial(p12)
    specialized_sources = [
        v87.source_polynomial(row, rhs) for _, row, rhs in specialized_first
    ]
    pivots = h5.base_pivot_columns(specialized_first)
    T, telemetry = h6.invert_full_q_pivot(specialized_first, pivots)
    A = [
        [row.get(pivot, QPoly()) for pivot in pivots]
        for _, row, _ in specialized_first
    ]
    assert h5.is_identity(h5.matmul_q(T, A))
    assert h5.is_identity(h5.matmul_q(A, T))
    normalized = [
        h5.linear_combination(T[i], specialized_sources) for i in range(38)
    ]
    recovered = [
        h5.linear_combination(A[i], normalized) for i in range(38)
    ]
    assert recovered == specialized_sources

    pivot_set = set(pivots)
    for index, source in enumerate(normalized):
        for monomial, coefficient in source.items():
            hits = pivot_set.intersection(monomial)
            if hits:
                assert monomial == (pivots[index],)
                assert coefficient == QPoly(1)
    assert all(
        not reduce_quiet(source, normalized, pivots)
        for source in specialized_sources
    )
    print("normalized_FIRST_two_sided_original_module_maps=true")
    print("normalized_FIRST_monic_distinct_pivots_and_pivot_free_tails=true")
    print("all_38_original_FIRST_sources_reduce_to_zero=true", flush=True)

    remainder, quotients = h5.divide_by_normalized_first(
        specialized_p12, normalized, pivots
    )
    relations = h6.original_relations(quotients, T)
    replay = {}
    for relation, source in zip(relations, specialized_sources):
        replay = v87.add(replay, v87.multiply(relation, source))
    assert replay == v87.add(specialized_p12, remainder, -1)
    positive = h6.positive_part(remainder)
    assert h6.qpoly_support(positive) == [(14,)]
    assert () in positive and (14,) in positive[()].coefficients
    q14_empty = positive[()].coefficients[(14,)]
    coordinates = m.r.scalar_coordinates(E3.coerce(q14_empty))
    functional = Rat3.coerce(coordinates[0])
    assert functional
    assert all(not coordinate for coordinate in coordinates[8:])
    expected_denominator = V**3 * (V**2 - 4*U**3)**2
    assert functional.denominator == expected_denominator
    assert v85.specialize_e3(E3(Rat3(B3))) == E3(Rat3(V**4))
    assert v85.specialize_e3(E3(Rat3(U*H))) == E3(
        Rat3(V**2 - 4*U**3)
    )

    exact_lines = [
        f"h6_parent_sha256={H6_SHA256}",
        "normal_form=full_original_FIRST_after_exact_F_zero",
        "functional_parameter_monomial=()",
        "functional_q_monomial=(14,)",
        "functional_E3_scalar_coordinate=0",
        f"functional_numerator={functional.numerator}",
        f"functional_denominator={functional.denominator}",
        "functional_denominator_equals_V3_times_UH_squared_on_F_zero=true",
        "functional_denominator_radical_subset_U_H_B3=true",
        "functional_annihilates_full_original_FIRST_module=true",
        "functional_P12_nonzero=true",
    ]
    exact_sha = write_text(
        outdir / "Q14_DUAL_FUNCTIONAL_EXACT.txt", exact_lines
    )
    print(f"dual_functional_exact_sha256={exact_sha}")
    print(f"dual_functional_exact_numerator={functional.numerator}")
    print(f"dual_functional_exact_denominator={functional.denominator}")
    print("dual_functional_exact_nonzero=true", flush=True)

    # Fresh characteristic and base point are preregistered and immutable.
    h6.PRIME = FRESH_PRIME
    h6.BASE_C, h6.BASE_V, h6.BASE_U = FRESH_C, FRESH_V, FRESH_U
    factory, evaluate_e3 = h6.build_mod_factory()
    assert (FRESH_C*FRESH_U - FRESH_V**2 + FRESH_U**3) % FRESH_PRIME == 0
    h_value = h6.polynomial_mod(
        H, FRESH_PRIME, FRESH_C, FRESH_V, FRESH_U
    )
    b3_value = h6.polynomial_mod(
        B3, FRESH_PRIME, FRESH_C, FRESH_V, FRESH_U
    )
    assert h_value == 12 and b3_value == 256
    prime_zero = h6.prime_remainder(
        first, p12, pivots, evaluate_e3, factory, 0
    )
    prime_one = h6.prime_remainder(
        first, p12, pivots, evaluate_e3, factory, 1
    )
    prime_delta = h6.poly_add(prime_one, prime_zero, -1, factory)
    expected_delta = {
        monomial: coefficient
        for monomial, value in positive.items()
        if (coefficient := h6.evaluate_qpoly(value, evaluate_e3, factory, 1))
    }
    assert prime_delta == expected_delta and prime_delta
    assert () in prime_delta
    functional_mod_prime = prime_delta[()].coordinates[0]
    exact_mod_prime = h6.rat3_mod(
        functional, FRESH_PRIME, FRESH_C, FRESH_V, FRESH_U
    )
    assert functional_mod_prime == exact_mod_prime
    assert functional_mod_prime
    full_prime_sha = h6.write_prime_polynomial(
        outdir / "Q14_DUAL_FUNCTIONAL_FRESH_PRIME_CLASS.tsv", prime_delta
    )
    prime_lines = [
        "prime\tC\tV\tU\tH\tB3\tparameter_monomial\tq_monomial\tE3_coordinate\tvalue",
        f"{FRESH_PRIME}\t{FRESH_C}\t{FRESH_V}\t{FRESH_U}\t{h_value}\t{b3_value}\t()\t(14,)\t0\t{functional_mod_prime}",
    ]
    prime_sha = write_text(
        outdir / "Q14_DUAL_FUNCTIONAL_FRESH_PRIME.tsv", prime_lines
    )
    print(f"fresh_prime={FRESH_PRIME}")
    print(f"fresh_prime_base_C_V_U={FRESH_C},{FRESH_V},{FRESH_U}")
    print(f"fresh_prime_H={h_value}")
    print(f"fresh_prime_B3={b3_value}")
    print("fresh_prime_complete_class_matches_exact_evaluation=true")
    print(f"fresh_prime_complete_class_sha256={full_prime_sha}")
    print(f"fresh_prime_functional_value={functional_mod_prime}")
    print(f"fresh_prime_functional_sha256={prime_sha}")
    print("fresh_prime_functional_nonzero=true", flush=True)

    result_lines = [
        f"h6_parent_sha256={H6_SHA256}",
        f"exact_functional_sha256={exact_sha}",
        f"fresh_prime_functional_sha256={prime_sha}",
        f"fresh_prime_complete_class_sha256={full_prime_sha}",
        "claim=minimal_single_coordinate_dual_functional_witness",
        "producer_tier_pending_hostile_review=true",
        "unit_ideal_claim=false",
        "source_point_claim=false",
        "whole_TD6_killed=false",
        "JC2_resolved=false",
    ]
    result_sha = write_text(
        outdir / "Q14_DUAL_FUNCTIONAL_RESULT.txt", result_lines
    )
    print(f"dual_functional_result_sha256={result_sha}")
    print("P12_FIRST_F_unit_ideal_claim=false")
    print("source_point_claim=false")
    print("whole_TD6_killed=false")
    print("JC2_resolved=false")
    print("TD6-V89H7-Q14-MOD-F-DUAL-FUNCTIONAL PASS")
    v85.restore_base_qd_state()


if __name__ == "__main__":
    main()

