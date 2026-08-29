#!/usr/bin/env python3
"""Full licensed-q unitriangular FIRST inverse and q14 functional gate."""

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
spec = importlib.util.spec_from_file_location("td6_v89h10_h6_parent", H6_PATH)
h6 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = h6
spec.loader.exec_module(h6)

h5, v87, v85, m = h6.h5, h6.v87, h6.v85, h6.m
QPoly, E3, Rat3 = h6.QPoly, h6.E3, h6.Rat3
C, V, U, F, H, B3 = h6.C, h6.V, h6.U, h6.F, h6.H, h6.B3
ALLOWED_Q = tuple(list(range(2, 15)) + list(range(16, 25)))
ZERO_LOW_Q = ()


def write_result(path, lines):
    text = "\n".join(lines) + "\n"
    path.write_text(text)
    return sha256(text.encode()).hexdigest()


def identity_matrix(size):
    return [
        [QPoly(1 if row == column else 0) for column in range(size)]
        for row in range(size)
    ]


def add_scaled_matrix(left, right, scalar):
    scalar = QPoly(scalar)
    return [
        [a + scalar*b for a, b in zip(left_row, right_row)]
        for left_row, right_row in zip(left, right)
    ]


def matrix_stats(matrix):
    digest = sha256()
    nonzero_entries = q_terms = max_degree = 0
    for row, values in enumerate(matrix):
        for column, value in enumerate(values):
            if value:
                nonzero_entries += 1
            for monomial, coefficient in sorted(value.coefficients.items()):
                q_terms += 1
                max_degree = max(max_degree, len(monomial))
                digest.update(
                    (
                        f"{row}\t{column}\t{monomial!r}\t"
                        f"{m.e3_exact(coefficient)}\n"
                    ).encode()
                )
    return digest.hexdigest(), nonzero_entries, q_terms, max_degree


def series_multiply(left, right, limit):
    out = [QPoly() for _ in range(limit)]
    for i, a in enumerate(left[:limit]):
        if not a:
            continue
        for j, b in enumerate(right[:limit-i]):
            if b:
                out[i+j] += a*b
    return out


def series_inverse(series, limit):
    assert series[0] == QPoly(1)
    out = [QPoly() for _ in range(limit)]
    out[0] = QPoly(1)
    for degree in range(1, limit):
        value = QPoly()
        for index in range(1, degree + 1):
            if series[index] and out[degree-index]:
                value += series[index]*out[degree-index]
        out[degree] = -value
    assert series_multiply(series, out, limit) == [QPoly(1)] + [
        QPoly() for _ in range(limit-1)
    ]
    return out


def toeplitz_multiplier(series, size):
    return [
        [series[row-column] if row >= column else QPoly()
         for column in range(size)]
        for row in range(size)
    ]


def write_series(path, records):
    lines = ["series\tz_degree\tq_monomial\tcoefficient_exact"]
    for name, series in records:
        for degree, value in enumerate(series):
            for monomial, coefficient in sorted(value.coefficients.items()):
                lines.append(
                    f"{name}\t{degree}\t{monomial!r}\t"
                    f"{m.e3_exact(coefficient)}"
                )
    text = "\n".join(lines) + "\n"
    path.write_text(text)
    return sha256(text.encode()).hexdigest(), len(lines) - 1


def raw_qprime_maps(outdir):
    """Certify the literal truncated q' row/column basis changes."""
    limit = 40
    qprime = [QPoly() for _ in range(limit)]
    qprime[0] = QPoly(1)
    qprime[24] = QPoly(25)
    for exponent in ALLOWED_Q:
        qprime[exponent-1] += QPoly.variable(exponent, exponent)
    qprime0 = [QPoly() for _ in range(limit)]
    qprime0[0], qprime0[24] = QPoly(1), QPoly(25)
    qprime_inverse = series_inverse(qprime, limit)
    qprime0_inverse = series_inverse(qprime0, limit)
    row_series = series_multiply(qprime, qprime0_inverse, limit)
    row_inverse_series = series_multiply(qprime0, qprime_inverse, limit)
    one = [QPoly(1)] + [QPoly() for _ in range(limit-1)]
    assert series_multiply(row_series, row_inverse_series, limit) == one
    assert series_multiply(row_inverse_series, row_series, limit) == one

    row_map = toeplitz_multiplier(row_series, 40)
    row_inverse = toeplitz_multiplier(row_inverse_series, 40)
    assert h5.is_identity(h5.matmul_q(row_map, row_inverse))
    assert h5.is_identity(h5.matmul_q(row_inverse, row_map))

    column_map = identity_matrix(42)
    column_inverse = identity_matrix(42)
    for i in range(26):
        for j in range(26):
            column_map[16+i][16+j] = (
                row_series[i-j] if i >= j else QPoly()
            )
            column_inverse[16+i][16+j] = (
                row_inverse_series[i-j] if i >= j else QPoly()
            )
    assert h5.is_identity(h5.matmul_q(column_map, column_inverse))
    assert h5.is_identity(h5.matmul_q(column_inverse, column_map))

    raw_q = [[QPoly() for _ in range(42)] for _ in range(40)]
    raw_0 = [[QPoly() for _ in range(42)] for _ in range(40)]
    for degree in range(40):
        for i in range(16):
            if degree >= i:
                raw_q[degree][i] = qprime[degree-i]
                raw_0[degree][i] = qprime0[degree-i]
        j = degree - 14
        if 0 <= j < 26:
            raw_q[degree][16+j] = QPoly(-15)
            raw_0[degree][16+j] = QPoly(-15)
    assert h5.matmul_q(raw_q, column_map) == h5.matmul_q(row_map, raw_0)

    series_sha, series_terms = write_series(
        outdir / "RAW_QPRIME_TRUNCATED_INVERSES.tsv",
        (
            ("qprime", qprime),
            ("qprime_inverse", qprime_inverse),
            ("qprime_relative_row", row_series),
            ("qprime_relative_row_inverse", row_inverse_series),
        ),
    )
    _, row_entries, _, row_degree = matrix_stats(row_map)
    _, column_entries, _, column_degree = matrix_stats(column_map)
    row_sha, row_terms = h5.write_qmatrix(
        outdir / "RAW_QPRIME_ROW_MAP.tsv", row_map
    )
    row_inverse_sha, row_inverse_terms = h5.write_qmatrix(
        outdir / "RAW_QPRIME_ROW_MAP_INVERSE.tsv", row_inverse
    )
    column_sha, column_terms = h5.write_qmatrix(
        outdir / "RAW_QPRIME_COLUMN_MAP.tsv", column_map
    )
    column_inverse_sha, column_inverse_terms = h5.write_qmatrix(
        outdir / "RAW_QPRIME_COLUMN_MAP_INVERSE.tsv", column_inverse
    )
    return {
        "series_sha": series_sha,
        "series_terms": series_terms,
        "row_sha": row_sha,
        "row_entries": row_entries,
        "row_terms": row_terms,
        "row_inverse_sha": row_inverse_sha,
        "row_inverse_terms": row_inverse_terms,
        "row_degree": row_degree,
        "column_sha": column_sha,
        "column_entries": column_entries,
        "column_terms": column_terms,
        "column_inverse_sha": column_inverse_sha,
        "column_inverse_terms": column_inverse_terms,
        "column_degree": column_degree,
    }


def neumann_inverse(B, outdir):
    """Invert B=I+N only after the exact full-q nilpotence gate passes."""
    size = len(B)
    identity = identity_matrix(size)
    N = [
        [B[i][j] - identity[i][j] for j in range(size)]
        for i in range(size)
    ]
    n_digest, n_entries, n_terms, n_degree = matrix_stats(N)
    assert n_degree <= 1
    inverse = identity
    power = identity
    telemetry = [
        "power\tsha256\tnonzero_entries\tq_terms\tmax_total_q_degree"
    ]
    nilpotence_index = None
    for exponent in range(1, size + 1):
        power = h5.matmul_q(power, N)
        digest, entries, terms, degree = matrix_stats(power)
        telemetry.append(
            f"{exponent}\t{digest}\t{entries}\t{terms}\t{degree}"
        )
        if not entries:
            nilpotence_index = exponent
            break
        inverse = add_scaled_matrix(
            inverse, power, -1 if exponent & 1 else 1
        )
    telemetry_text = "\n".join(telemetry) + "\n"
    (outdir / "ALLQ_FIRST_NILPOTENCE_TELEMETRY.tsv").write_text(
        telemetry_text
    )
    telemetry_sha = sha256(telemetry_text.encode()).hexdigest()
    if nilpotence_index is None:
        return None, {
            "N_sha": n_digest,
            "N_entries": n_entries,
            "N_terms": n_terms,
            "N_degree": n_degree,
            "telemetry_sha": telemetry_sha,
            "nilpotence_index": None,
        }
    assert h5.is_identity(h5.matmul_q(B, inverse))
    assert h5.is_identity(h5.matmul_q(inverse, B))
    inverse_sha, inverse_terms = h5.write_qmatrix(
        outdir / "ALLQ_FIRST_PIVOT_INVERSE.tsv", inverse
    )
    return inverse, {
        "N_sha": n_digest,
        "N_entries": n_entries,
        "N_terms": n_terms,
        "N_degree": n_degree,
        "telemetry_sha": telemetry_sha,
        "nilpotence_index": nilpotence_index,
        "inverse_sha": inverse_sha,
        "inverse_terms": inverse_terms,
    }


def write_relations(path, relations):
    lines = [
        "source_index\tparameter_monomial\tq_monomial\tcoefficient_exact"
    ]
    for source_index, relation in enumerate(relations):
        for parameter_monomial, value in sorted(relation.items()):
            for q_monomial, coefficient in sorted(value.coefficients.items()):
                lines.append(
                    f"{source_index}\t{parameter_monomial!r}\t"
                    f"{q_monomial!r}\t{m.e3_exact(coefficient)}"
                )
    text = "\n".join(lines) + "\n"
    path.write_text(text)
    return sha256(text.encode()).hexdigest(), len(lines) - 1


SPECIAL_HF = V**2 - 4*U**3
SPECIAL_ALLOWED_MONIC = tuple(
    v85.monic(value) for value in (U, V, SPECIAL_HF)
)


def qmatrix_coefficients(matrix):
    for row in matrix:
        for value in row:
            yield from value.coefficients.values()


def section_coefficients(polynomials):
    for polynomial in polynomials:
        yield from v87.all_coefficients([polynomial])


def specialized_denominator_record(label, values):
    values = list(values)
    common = v85.monic(m.denominator_for(values)) if values else m.tri.ONE
    factors = v85.factor_list(common)
    allowed = all(
        v85.monic(factor) in SPECIAL_ALLOWED_MONIC for factor in factors
    )
    return {
        "label": label,
        "value_count": len(values),
        "common": common,
        "factorization": common.factor(),
        "allowed": allowed,
    }


def write_denominator_ledger(path, records):
    lines = ["label\tvalue_count\tallowed\tcommon\tfactorization"]
    lines.extend(
        f"{record['label']}\t{record['value_count']}\t"
        f"{str(record['allowed']).lower()}\t{record['common']}\t"
        f"{record['factorization']}"
        for record in records
    )
    text = "\n".join(lines) + "\n"
    path.write_text(text)
    return sha256(text.encode()).hexdigest()


def main():
    outdir = Path(os.environ["TD6_OUTPUT_DIR"]).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    assert os.environ.get("AWS_RUN_TAG", "").startswith(
        "td6_v89h10v2_allq_mod_f_unitriangular_functional_"
    )
    print("producer=TD6-V89H10V2-ALLQ-MOD-F-UNITRIANGULAR-FUNCTIONAL")
    print(f"h6_parent_sha256={H6_SHA256}")
    print(f"h7_result_sha256={H7_RESULT_SHA256}")
    print(f"h8_result_sha256={H8_RESULT_SHA256}")
    print("retained_q_exponents=" + ",".join(map(str, ALLOWED_Q)))
    print("zero_low_q_exponents=none")
    print("q15_absent_target_shear=true", flush=True)

    raw = raw_qprime_maps(outdir)
    print(f"raw_qprime_series_sha256={raw['series_sha']}")
    print(f"raw_qprime_series_terms={raw['series_terms']}")
    print(f"raw_qprime_row_map_sha256={raw['row_sha']}")
    print(f"raw_qprime_row_map_inverse_sha256={raw['row_inverse_sha']}")
    print(f"raw_qprime_row_map_max_q_degree={raw['row_degree']}")
    print(f"raw_qprime_column_map_sha256={raw['column_sha']}")
    print(f"raw_qprime_column_map_inverse_sha256={raw['column_inverse_sha']}")
    print(f"raw_qprime_column_map_max_q_degree={raw['column_degree']}")
    print("raw_qprime_row_map_two_sided=true")
    print("raw_qprime_column_map_two_sided=true")
    print("raw_FIRST_qprime_basis_identity=true", flush=True)

    events, bands, seen = v87.build_bands()
    total_first = v87.compile_first(bands)
    total_p12 = v87.compile_current_degree12(bands)
    first = total_first
    p12 = total_p12
    assert events == 2 and len(first) == 38
    assert set(seen) == set(ALLOWED_Q)
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
    A0 = [
        [row.get(pivot, QPoly()).constant() for pivot in pivots]
        for _, row, _ in specialized_first
    ]
    A = [
        [row.get(pivot, QPoly()) for pivot in pivots]
        for _, row, _ in specialized_first
    ]
    inverse_A0 = h5.inverse_constant_matrix(A0)
    B = h5.matmul_constant_q(inverse_A0, A)
    assert all(
        B[i][j].constant() == (E3(1) if i == j else E3())
        for i in range(38) for j in range(38)
    )
    N = [
        [B[i][j] - QPoly(1 if i == j else 0) for j in range(38)]
        for i in range(38)
    ]
    graph = {i: {j for j in range(38) if N[i][j]} for i in range(38)}
    components, cyclic = h5.strongly_connected(graph)
    inverse_B, nil = neumann_inverse(B, outdir)
    print(f"allq_FIRST_graph_edges={sum(map(len, graph.values()))}")
    print(f"allq_FIRST_components={components!r}")
    print(f"allq_FIRST_cyclic_components={cyclic!r}")
    print(f"allq_FIRST_N_sha256={nil['N_sha']}")
    print(f"allq_FIRST_N_q_terms={nil['N_terms']}")
    print(f"allq_FIRST_N_max_q_degree={nil['N_degree']}")
    print(f"allq_FIRST_nilpotence_telemetry_sha256={nil['telemetry_sha']}")
    print(f"allq_FIRST_nilpotence_index={nil['nilpotence_index']}", flush=True)

    if inverse_B is None:
        result_sha = write_result(
            outdir / "ALLQ_UNITRIANGULAR_FUNCTIONAL_RESULT.txt",
            [
                f"h7_result_sha256={H7_RESULT_SHA256}",
                f"h8_result_sha256={H8_RESULT_SHA256}",
                f"raw_qprime_series_sha256={raw['series_sha']}",
                f"raw_qprime_row_map_sha256={raw['row_sha']}",
                f"raw_qprime_row_map_inverse_sha256={raw['row_inverse_sha']}",
                f"raw_qprime_column_map_sha256={raw['column_sha']}",
                f"raw_qprime_column_map_inverse_sha256={raw['column_inverse_sha']}",
                f"N_sha256={nil['N_sha']}",
                f"nilpotence_telemetry_sha256={nil['telemetry_sha']}",
                "allq_polynomial_functional_extension=false",
                "reason=transported_pivot_N_not_nilpotent_through_power_38",
                "raw_qprime_basis_theorem=true",
                "transported_FIRST_polynomial_inverse_unproved=true",
                "P12_division_attempted=false",
                "unit_ideal_claim=false",
                "whole_TD6_killed=false",
            ],
        )
        print(f"allq_unitriangular_result_sha256={result_sha}")
        print("allq_unitriangular_fail_closed_before_P12=true")
        print("TD6-V89H10V2-ALLQ-MOD-F-UNITRIANGULAR-FUNCTIONAL NONNILPOTENT-PASS")
        v85.restore_base_qd_state()
        return

    print(f"allq_FIRST_pivot_inverse_sha256={nil['inverse_sha']}")
    print(f"allq_FIRST_pivot_inverse_terms={nil['inverse_terms']}")
    print("allq_FIRST_polynomial_inverse_two_sided=true", flush=True)
    T = h5.matmul_q(inverse_B, [
        [QPoly(value) for value in row] for row in inverse_A0
    ])
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
    print("allq_normalized_original_FIRST_replay=true", flush=True)

    denominator_records = [
        specialized_denominator_record(
            "relative_pivot_inverse_B", qmatrix_coefficients(inverse_B)
        ),
        specialized_denominator_record(
            "full_original_FIRST_inverse_T", qmatrix_coefficients(T)
        ),
        specialized_denominator_record(
            "normalized_original_FIRST", section_coefficients(normalized)
        ),
    ]
    denominator_sha = write_denominator_ledger(
        outdir / "ALLQ_SPECIALIZED_DENOMINATOR_LEDGER.tsv",
        denominator_records,
    )
    denominator_allowed = all(
        record["allowed"] for record in denominator_records
    )
    print(f"allq_specialized_denominator_ledger_sha256={denominator_sha}")
    print(
        "allq_pre_P12_denominators_registered="
        + str(denominator_allowed).lower(),
        flush=True,
    )
    if not denominator_allowed:
        result_sha = write_result(
            outdir / "ALLQ_UNITRIANGULAR_FUNCTIONAL_RESULT.txt",
            [
                f"h7_result_sha256={H7_RESULT_SHA256}",
                f"h8_result_sha256={H8_RESULT_SHA256}",
                f"raw_qprime_series_sha256={raw['series_sha']}",
                f"N_sha256={nil['N_sha']}",
                f"nilpotence_index={nil['nilpotence_index']}",
                f"pivot_inverse_sha256={nil['inverse_sha']}",
                f"denominator_ledger_sha256={denominator_sha}",
                "raw_qprime_basis_theorem=true",
                "allq_polynomial_functional_extension=false",
                "reason=unregistered_transported_FIRST_denominator",
                "P12_division_attempted=false",
                "unit_ideal_claim=false",
                "whole_TD6_killed=false",
            ],
        )
        print(f"allq_unitriangular_result_sha256={result_sha}")
        print("allq_denominator_fail_closed_before_P12=true")
        print(
            "TD6-V89H10V2-ALLQ-MOD-F-UNITRIANGULAR-FUNCTIONAL "
            "DENOMINATOR-PASS"
        )
        v85.restore_base_qd_state()
        return

    remainder, quotients = h5.divide_by_normalized_first(
        specialized_p12, normalized, pivots
    )
    relations = h6.original_relations(quotients, T)
    replay = {}
    for relation, source in zip(relations, specialized_sources):
        replay = v87.add(replay, v87.multiply(relation, source))
    assert replay == v87.add(specialized_p12, remainder, -1)
    denominator_records.extend((
        specialized_denominator_record(
            "P12_original_FIRST_relations", section_coefficients(relations)
        ),
        specialized_denominator_record(
            "P12_canonical_remainder", section_coefficients([remainder])
        ),
    ))
    denominator_sha = write_denominator_ledger(
        outdir / "ALLQ_SPECIALIZED_DENOMINATOR_LEDGER.tsv",
        denominator_records,
    )
    assert all(record["allowed"] for record in denominator_records), (
        "unregistered_post_P12_denominator",
        [record for record in denominator_records if not record["allowed"]],
    )
    relations_sha, relations_terms = write_relations(
        outdir / "ALLQ_P12_ORIGINAL_FIRST_RELATIONS.tsv", relations
    )
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
    mixed_support = [monomial for monomial in support if len(monomial) > 1]
    pure_support = [monomial for monomial in support if len(monomial) == 1]
    remainder_sha = h5.write_polynomial(
        outdir / "ALLQ_CANONICAL_P12_REMAINDER.tsv", remainder
    )
    support_lines = ["q_monomial"] + [repr(monomial) for monomial in support]
    support_text = "\n".join(support_lines) + "\n"
    (outdir / "ALLQ_CANONICAL_Q_SUPPORT.tsv").write_text(support_text)
    support_sha = sha256(support_text.encode()).hexdigest()
    print(f"allq_original_FIRST_relations_sha256={relations_sha}")
    print(f"allq_original_FIRST_relations_terms={relations_terms}")
    print(f"allq_canonical_remainder_sha256={remainder_sha}")
    print(f"allq_q_support_sha256={support_sha}")
    print(f"allq_q_support_count={len(support)}")
    print(f"allq_pure_q_support_count={len(pure_support)}")
    print(f"allq_mixed_q_support_count={len(mixed_support)}")
    print(f"allq_max_total_q_degree={max_q_degree}")
    print(f"allq_specialized_denominator_ledger_sha256={denominator_sha}")
    print("allq_all_denominators_registered_on_F_zero=true")
    print("allq_extended_q14_functional_equals_H7_exact=true")
    print("allq_extended_q14_functional_nonzero=true", flush=True)

    result_sha = write_result(
        outdir / "ALLQ_UNITRIANGULAR_FUNCTIONAL_RESULT.txt",
        [
            f"h7_result_sha256={H7_RESULT_SHA256}",
            f"h8_result_sha256={H8_RESULT_SHA256}",
            f"raw_qprime_series_sha256={raw['series_sha']}",
            f"raw_qprime_row_map_sha256={raw['row_sha']}",
            f"raw_qprime_row_map_inverse_sha256={raw['row_inverse_sha']}",
            f"raw_qprime_column_map_sha256={raw['column_sha']}",
            f"raw_qprime_column_map_inverse_sha256={raw['column_inverse_sha']}",
            f"N_sha256={nil['N_sha']}",
            f"nilpotence_telemetry_sha256={nil['telemetry_sha']}",
            f"nilpotence_index={nil['nilpotence_index']}",
            f"pivot_inverse_sha256={nil['inverse_sha']}",
            f"denominator_ledger_sha256={denominator_sha}",
            f"original_FIRST_relations_sha256={relations_sha}",
            f"canonical_remainder_sha256={remainder_sha}",
            f"q_support_sha256={support_sha}",
            f"q_support_count={len(support)}",
            f"pure_q_support_count={len(pure_support)}",
            f"mixed_q_support_count={len(mixed_support)}",
            f"max_total_q_degree={max_q_degree}",
            "raw_qprime_basis_theorem=true",
            "allq_transported_FIRST_polynomial_inverse=true",
            "allq_polynomial_functional_extension=true",
            "allq_all_denominators_registered_on_F_zero=true",
            "extended_q14_functional_equals_H7_exact=true",
            "functional_denominator_radical_subset_U_H_B3_on_F_zero=true",
            "unit_ideal_claim=false",
            "whole_TD6_killed=false",
            "JC2_resolved=false",
        ],
    )
    print(f"allq_unitriangular_result_sha256={result_sha}")
    print("P12_FIRST_F_unit_ideal_claim=false")
    print("whole_TD6_killed=false")
    print("JC2_resolved=false")
    print("TD6-V89H10V2-ALLQ-MOD-F-UNITRIANGULAR-FUNCTIONAL PASS")
    v85.restore_base_qd_state()


if __name__ == "__main__":
    main()
