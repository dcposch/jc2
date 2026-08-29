#!/usr/bin/env python3
"""Exact q12 extension gate for the V89H7 q14 quotient functional."""

from hashlib import sha256
import importlib.util
import os
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
H6_PATH = HERE / "replay_v89h6_q14_mod_f_cokernel.py"
H6_SHA256 = "1301a09f0497abac5197de6b4afc0eba54b5c8de2b05d2cf11db63fab454d757"
H7_RESULT_PATH = HERE / "H7_RESULT.md"
H7_RESULT_SHA256 = "49b9dcba0bb5956dfdbb10293b7bdf3e440a39b127929089c2402ffb06db32cd"
H8_RESULT_PATH = HERE / "H8_RESULT.md"
H8_RESULT_SHA256 = "646dd1162cc2e6aa36c3fe72bea5c64a44e19361323593a12fc4c7f137cc0292"
assert sha256(H6_PATH.read_bytes()).hexdigest() == H6_SHA256
assert sha256(H7_RESULT_PATH.read_bytes()).hexdigest() == H7_RESULT_SHA256
assert sha256(H8_RESULT_PATH.read_bytes()).hexdigest() == H8_RESULT_SHA256
spec = importlib.util.spec_from_file_location("td6_v89h9_h6_parent", H6_PATH)
h6 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = h6
spec.loader.exec_module(h6)

h5, v87, v85, m = h6.h5, h6.v87, h6.v85, h6.m
QPoly, E3, Rat3 = h6.QPoly, h6.E3, h6.Rat3
C, V, U, F, H, B3 = h6.C, h6.V, h6.U, h6.F, h6.H, h6.B3
ALLOWED_Q = (12, 13, 14) + tuple(range(16, 25))
ZERO_LOW_Q = tuple(range(2, 12))


def project_value(value):
    value = QPoly.coerce(value)
    return QPoly(0, {
        monomial: coefficient
        for monomial, coefficient in value.coefficients.items()
        if all(exponent in ALLOWED_Q for exponent in monomial)
    })


def project_polynomial(polynomial):
    return v87.clean({
        monomial: projected
        for monomial, value in polynomial.items()
        if (projected := project_value(value))
    })


def project_first(first):
    out = []
    for key, row, rhs in first:
        projected_row = {
            variable: projected
            for variable, value in row.items()
            if (projected := project_value(value))
        }
        out.append((key, projected_row, project_value(rhs)))
    return out


def pivot_diagnostic(first, pivots):
    A0 = [
        [row.get(pivot, QPoly()).constant() for pivot in pivots]
        for _, row, _ in first
    ]
    A = [
        [row.get(pivot, QPoly()) for pivot in pivots]
        for _, row, _ in first
    ]
    inverse_A0 = h5.inverse_constant_matrix(A0)
    B = h5.matmul_constant_q(inverse_A0, A)
    N = [
        [B[i][j] - QPoly(1 if i == j else 0) for j in range(38)]
        for i in range(38)
    ]
    graph = {i: {j for j in range(38) if N[i][j]} for i in range(38)}
    components, cyclic = h5.strongly_connected(graph)
    records = []
    unit = True
    for component in cyclic:
        block = [[B[i][j] for j in component] for i in component]
        determinant = h5.determinant_subset(block)
        unit = unit and determinant == QPoly(1)
        for q_monomial, coefficient in sorted(determinant.coefficients.items()):
            records.append((component, q_monomial, coefficient))
    return A, components, cyclic, records, unit, sum(map(len, graph.values()))


def write_scc(path, records):
    lines = ["component\tq_monomial\tcoefficient_exact"]
    lines.extend(
        f"{component!r}\t{q_monomial!r}\t{m.e3_exact(coefficient)}"
        for component, q_monomial, coefficient in records
    )
    text = "\n".join(lines) + "\n"
    path.write_text(text)
    return sha256(text.encode()).hexdigest()


def write_result(path, lines):
    text = "\n".join(lines) + "\n"
    path.write_text(text)
    return sha256(text.encode()).hexdigest()


def main():
    outdir = Path(os.environ["TD6_OUTPUT_DIR"]).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    assert os.environ.get("AWS_RUN_TAG", "").startswith(
        "td6_v89h9_q12_q14_mod_f_functional_extension_"
    )
    print("producer=TD6-V89H9-Q12-Q14-MOD-F-FUNCTIONAL-EXTENSION")
    print(f"h6_parent_sha256={H6_SHA256}")
    print(f"h7_result_sha256={H7_RESULT_SHA256}")
    print(f"h8_result_sha256={H8_RESULT_SHA256}")
    print("retained_q_exponents=" + ",".join(map(str, ALLOWED_Q)))
    print("zero_low_q_exponents=" + ",".join(map(str, ZERO_LOW_Q)))
    print("q15_absent_target_shear=true", flush=True)

    events, bands, seen = v87.build_bands()
    total_first = v87.compile_first(bands)
    total_p12 = v87.compile_current_degree12(bands)
    first = project_first(total_first)
    p12 = project_polynomial(total_p12)
    assert events == 2 and len(first) == 38
    assert all(seen[exponent] == 1 for exponent in ALLOWED_Q)
    original_sources = [
        v87.source_polynomial(row, rhs) for _, row, rhs in first
    ]
    _, raw_common = v87.assert_denominators_allowed([p12, *original_sources])
    assert raw_common == U*H and raw_common.gcd(F).total_degree() == 0
    print("literal_transport_FIRST_P12_rebuilt=true")
    print(f"raw_source_common_denominator=({raw_common})")
    print("raw_source_denominator_coprime_F=true", flush=True)

    specialized_first = h6.specialize_first(first)
    specialized_p12 = h6.specialize_polynomial(p12)
    specialized_sources = [
        v87.source_polynomial(row, rhs) for _, row, rhs in specialized_first
    ]
    pivots = h5.base_pivot_columns(specialized_first)
    A, components, cyclic, records, unit, edges = pivot_diagnostic(
        specialized_first, pivots
    )
    scc_sha = write_scc(outdir / "Q12_EXTENSION_SCC_DETERMINANTS.tsv", records)
    print(f"q12_extension_FIRST_graph_edges={edges}")
    print(f"q12_extension_FIRST_components={components!r}")
    print(f"q12_extension_FIRST_cyclic_components={cyclic!r}")
    print(f"q12_extension_SCC_determinants_sha256={scc_sha}")
    print(f"q12_extension_all_SCC_determinants_one={str(unit).lower()}", flush=True)

    if not unit:
        result_sha = write_result(
            outdir / "Q12_FUNCTIONAL_EXTENSION_RESULT.txt",
            [
                f"h7_result_sha256={H7_RESULT_SHA256}",
                f"h8_result_sha256={H8_RESULT_SHA256}",
                f"scc_determinants_sha256={scc_sha}",
                "q12_polynomial_functional_extension=false",
                "reason=nonunit_registered_pivot_SCC_determinant",
                "alternate_pivot_or_determinant_chart_required=true",
                "P12_division_attempted=false",
                "unit_ideal_claim=false",
                "whole_TD6_killed=false",
            ],
        )
        print(f"q12_extension_result_sha256={result_sha}")
        print("q12_extension_fail_closed_before_P12=true")
        print("TD6-V89H9-Q12-Q14-MOD-F-FUNCTIONAL-EXTENSION NONUNIT-PIVOT-PASS")
        v85.restore_base_qd_state()
        return

    T, telemetry = h6.invert_full_q_pivot(specialized_first, pivots)
    assert telemetry["cyclic"] == cyclic
    assert h5.is_identity(h5.matmul_q(T, A))
    assert h5.is_identity(h5.matmul_q(A, T))
    normalized = [
        h5.linear_combination(T[i], specialized_sources) for i in range(38)
    ]
    recovered = [h5.linear_combination(A[i], normalized) for i in range(38)]
    assert recovered == specialized_sources
    pivot_set = set(pivots)
    for index, source in enumerate(normalized):
        for monomial, coefficient in source.items():
            hits = pivot_set.intersection(monomial)
            if hits:
                assert monomial == (pivots[index],) and coefficient == QPoly(1)
    print("q12_extension_full_q_pivot_inverse_two_sided=true")
    print("q12_extension_normalized_original_FIRST_replay=true", flush=True)

    remainder, quotients = h5.divide_by_normalized_first(
        specialized_p12, normalized, pivots
    )
    relations = h6.original_relations(quotients, T)
    replay = {}
    for relation, source in zip(relations, specialized_sources):
        replay = v87.add(replay, v87.multiply(relation, source))
    assert replay == v87.add(specialized_p12, remainder, -1)
    support = h6.qpoly_support(remainder)
    assert (14,) in support
    q14_empty = remainder[()].coefficients[(14,)]
    coordinates = m.r.scalar_coordinates(E3.coerce(q14_empty))
    functional = Rat3.coerce(coordinates[0])
    expected_numerator = (
        Rat3(3856216)*Rat3(V)**10*Rat3(U)**2/Rat3(375)
        + Rat3(1625866424)*Rat3(V)**8*Rat3(U)**5/Rat3(375)
        + Rat3(30525031264)*Rat3(V)**6*Rat3(U)**8/Rat3(375)
        - Rat3(10638708808)*Rat3(V)**4*Rat3(U)**11/Rat3(375)
        - Rat3(4168187296)*Rat3(V)**2*Rat3(U)**14/Rat3(75)
        + Rat3(710528)*Rat3(U)**17/Rat3(15)
    )
    expected_functional = expected_numerator / Rat3(
        V**3*(V**2 - 4*U**3)**2
    )
    assert functional == expected_functional and functional
    max_q_degree = max(map(len, support), default=0)
    max_q12_degree = max((monomial.count(12) for monomial in support), default=0)
    mixed_q12_q14 = [
        monomial for monomial in support if 12 in monomial and 14 in monomial
    ]
    remainder_sha = h5.write_polynomial(
        outdir / "Q12_EXTENSION_CANONICAL_REMAINDER.tsv", remainder
    )
    support_lines = ["q_monomial"] + [repr(monomial) for monomial in support]
    support_text = "\n".join(support_lines) + "\n"
    (outdir / "Q12_EXTENSION_Q_SUPPORT.tsv").write_text(support_text)
    support_sha = sha256(support_text.encode()).hexdigest()
    print(f"q12_extension_canonical_remainder_sha256={remainder_sha}")
    print(f"q12_extension_q_support_sha256={support_sha}")
    print(f"q12_extension_q_support_count={len(support)}")
    print(f"q12_extension_max_total_q_degree={max_q_degree}")
    print(f"q12_extension_max_q12_degree={max_q12_degree}")
    print(f"q12_q14_mixed_support_count={len(mixed_q12_q14)}")
    print("q12_extended_functional_equals_H7_exact=true")
    print("q12_extended_functional_nonzero=true", flush=True)

    result_sha = write_result(
        outdir / "Q12_FUNCTIONAL_EXTENSION_RESULT.txt",
        [
            f"h7_result_sha256={H7_RESULT_SHA256}",
            f"h8_result_sha256={H8_RESULT_SHA256}",
            f"scc_determinants_sha256={scc_sha}",
            f"canonical_remainder_sha256={remainder_sha}",
            f"q_support_sha256={support_sha}",
            f"q_support_count={len(support)}",
            f"max_total_q_degree={max_q_degree}",
            f"max_q12_degree={max_q12_degree}",
            f"mixed_q12_q14_support_count={len(mixed_q12_q14)}",
            "q12_polynomial_functional_extension=true",
            "extended_functional_equals_H7_exact=true",
            "functional_denominator_radical_subset_U_H_B3_on_F_zero=true",
            "unit_ideal_claim=false",
            "whole_TD6_killed=false",
            "JC2_resolved=false",
        ],
    )
    print(f"q12_extension_result_sha256={result_sha}")
    print("P12_FIRST_F_unit_ideal_claim=false")
    print("whole_TD6_killed=false")
    print("JC2_resolved=false")
    print("TD6-V89H9-Q12-Q14-MOD-F-FUNCTIONAL-EXTENSION PASS")
    v85.restore_base_qd_state()


if __name__ == "__main__":
    main()
