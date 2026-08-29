#!/usr/bin/env python3
"""Exact all-q empty-parameter P12 functional via the V89H10T flag."""

from hashlib import sha256
import importlib.util
import os
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
FLAG_CLIENT_PATH = HERE / "replay_v89h10t_allq_simultaneous_triangular_flag.py"
FLAG_CLIENT_SHA256 = "9c7a5eeede117568aa76d4c26bae11f6e78640313cad6ad559b414ee2cf5098c"
FLAG_RESULT_PATH = HERE / "FLAG_RESULT.md"
FLAG_RESULT_SHA256 = "612b57bcfc20228152d37e5acef08ea41539481be99dff5878af8a790e4c6d1f"
FLAG_FREEZE_PATH = HERE / "FLAG_FREEZE.sha256"
FLAG_FREEZE_SHA256 = "a156f8394a2966effb006cdfdbb7e64a7da5cefa6e586022a67d29776167d2d9"
H7_RESULT_PATH = HERE / "H7_RESULT.md"
H7_RESULT_SHA256 = "49b9dcba0bb5956dfdbb10293b7bdf3e440a39b127929089c2402ffb06db32cd"
for path, expected in (
    (FLAG_CLIENT_PATH, FLAG_CLIENT_SHA256),
    (FLAG_RESULT_PATH, FLAG_RESULT_SHA256),
    (FLAG_FREEZE_PATH, FLAG_FREEZE_SHA256),
    (H7_RESULT_PATH, H7_RESULT_SHA256),
):
    assert sha256(path.read_bytes()).hexdigest() == expected

spec = importlib.util.spec_from_file_location("td6_v89h11_flag_parent", FLAG_CLIENT_PATH)
t = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = t
spec.loader.exec_module(t)

p, h5, h6, v87, v85, m = t.p, t.h5, t.h6, t.v87, t.v85, t.m
QPoly, E3, Rat3 = t.QPoly, t.E3, h6.Rat3
U, V, F, H, B3 = h6.U, h6.V, h6.F, h6.H, h6.B3
LOW = tuple(range(2, 14))
TAIL = (14,) + tuple(range(16, 25))
ALL_Q = tuple(list(range(2, 15)) + list(range(16, 25)))
EXPECTED_N_SHA256 = "38fb14e38daa36d597cc7ae1cd2bd5dd402ef2cd1587337321b8c204eeeb7f36"
EXPECTED_FLAG_SHA256 = "89db0510983c95cd5c8b62e6a04ab3675939c62f1f5c2605d9add475cdad12c2"
EXPECTED_S_SHA256 = "05f9b3df78dc4abcf6ad39c36e1b48c54529b351459664cccfa3cd59d49d1542"
EXPECTED_S_INVERSE_SHA256 = "30e644c244f65b17cbf9d7a599b60883d1e8c0b1dd6c3fb326c8ae70cda87aac"
EXPECTED_ORDER_SHA256 = "35e88aa807ba6a4a0e275f946c23e86b0b3e8fa8aa155684103a08ae13cacb6a"
EXPECTED_UPPER_N_SHA256 = "946b75e5307941a81696ec68e1ae2fbcb6ce480294cead6076e434d8e819e913"
EXPECTED_DENOMINATOR_SHA256 = "5ebfa2b9d693974a21ae0622bf5e5f1aa701e3b2c802952d56d678c6278b8956"


def identity_constant(size):
    return [
        [E3(1 if row == column else 0) for column in range(size)]
        for row in range(size)
    ]


def matvec_constant_q(matrix, vector):
    return [
        sum(
            (QPoly(value)*coordinate for value, coordinate in zip(row, vector)),
            QPoly(),
        )
        for row in matrix
    ]


def matvec_q(matrix, vector):
    return [
        sum(
            (value*coordinate for value, coordinate in zip(row, vector)),
            QPoly(),
        )
        for row in matrix
    ]


def qpoly_stats(values):
    digest = sha256()
    nonzero = terms = max_degree = 0
    for index, value in enumerate(values):
        value = QPoly.coerce(value)
        if value:
            nonzero += 1
        for monomial, coefficient in sorted(value.coefficients.items()):
            terms += 1
            max_degree = max(max_degree, len(monomial))
            digest.update(
                f"{index}\t{monomial!r}\t{m.e3_exact(coefficient)}\n".encode()
            )
    return digest.hexdigest(), nonzero, terms, max_degree


def write_qvector(path, values):
    lines = ["index\tq_monomial\tcoefficient_exact"]
    for index, value in enumerate(values):
        for monomial, coefficient in sorted(QPoly.coerce(value).coefficients.items()):
            lines.append(f"{index}\t{monomial!r}\t{m.e3_exact(coefficient)}")
    text = "\n".join(lines) + "\n"
    path.write_text(text)
    return sha256(text.encode()).hexdigest(), len(lines) - 1


def write_qpoly(path, value):
    lines = ["q_monomial\tcoefficient_exact"]
    for monomial, coefficient in sorted(QPoly.coerce(value).coefficients.items()):
        lines.append(f"{monomial!r}\t{m.e3_exact(coefficient)}")
    text = "\n".join(lines) + "\n"
    path.write_text(text)
    return sha256(text.encode()).hexdigest(), len(lines) - 1


def reconstruct_flag(N, outdir):
    coefficient_matrices = []
    for exponent in range(2, 15):
        matrix = [
            [N[i][j].coefficients.get((exponent,), E3()) for j in range(14)]
            for i in range(14)
        ]
        assert any(value for row in matrix for value in row)
        coefficient_matrices.append(matrix)

    flag = []
    records = ["dimension\tquotient_dimension\tcommon_kernel_dimension\tvector_sha256"]
    for dimension in range(14):
        change = t.complete_basis(flag, 14)
        inverse_change = h5.inverse_constant_matrix(change)
        transformed = [
            h5.matmul_constant(h5.matmul_constant(inverse_change, matrix), change)
            for matrix in coefficient_matrices
        ]
        assert all(
            not matrix[row][column]
            for matrix in transformed
            for row in range(dimension, 14)
            for column in range(dimension)
        )
        quotient_size = 14 - dimension
        stacked = []
        for matrix in transformed:
            stacked.extend([row[dimension:] for row in matrix[dimension:]])
        kernel = t.nullspace(stacked, quotient_size)
        assert len(kernel) == 1
        lifted = [E3() for _ in range(dimension)] + kernel[0]
        vector = t.matvec(change, lifted)
        assert t.independent_columns(flag + [vector], 14) == dimension + 1
        digest_text = "\n".join(m.e3_exact(value).__repr__() for value in vector) + "\n"
        records.append(
            f"{dimension + 1}\t{quotient_size}\t1\t"
            f"{sha256(digest_text.encode()).hexdigest()}"
        )
        flag.append(vector)

    S = t.columns_matrix(flag, 14)
    inverse_S = h5.inverse_constant_matrix(S)
    assert h5.matmul_constant(S, inverse_S) == identity_constant(14)
    assert h5.matmul_constant(inverse_S, S) == identity_constant(14)
    transformed_coefficients = [
        h5.matmul_constant(h5.matmul_constant(inverse_S, matrix), S)
        for matrix in coefficient_matrices
    ]
    assert all(
        not matrix[row][column]
        for matrix in transformed_coefficients
        for row in range(14)
        for column in range(row + 1)
    )

    flag_text = "\n".join(records) + "\n"
    (outdir / "H11_COMMON_FLAG_TELEMETRY.tsv").write_text(flag_text)
    flag_sha = sha256(flag_text.encode()).hexdigest()
    S_sha, _ = t.write_constant_matrix(outdir / "H11_SCC_FLAG_BASIS.tsv", S)
    inverse_S_sha, _ = t.write_constant_matrix(
        outdir / "H11_SCC_FLAG_BASIS_INVERSE.tsv", inverse_S
    )
    assert flag_sha == EXPECTED_FLAG_SHA256
    assert S_sha == EXPECTED_S_SHA256
    assert inverse_S_sha == EXPECTED_S_INVERSE_SHA256

    S_full = identity_constant(38)
    inverse_S_full = identity_constant(38)
    for i in range(14):
        for j in range(14):
            S_full[i][j] = S[i][j]
            inverse_S_full[i][j] = inverse_S[i][j]
    transformed_N = h5.matmul_q(
        h5.matmul_constant_q(inverse_S_full, N),
        [[QPoly(value) for value in row] for row in S_full],
    )
    graph = {
        i: {j for j in range(38) if transformed_N[i][j]}
        for i in range(38)
    }
    order, cyclic = h5.topological_order(graph)
    assert not cyclic and len(order) == 38
    upper_N = [
        [transformed_N[order[i]][order[j]] for j in range(38)]
        for i in range(38)
    ]
    assert all(not upper_N[i][j] for i in range(38) for j in range(i + 1))
    upper_sha, _ = t.write_qmatrix(outdir / "H11_STRICT_UPPER_N.tsv", upper_N)
    order_text = "position\toriginal_index\n" + "\n".join(
        f"{position}\t{index}" for position, index in enumerate(order)
    ) + "\n"
    (outdir / "H11_STRICT_UPPER_ORDER.tsv").write_text(order_text)
    order_sha = sha256(order_text.encode()).hexdigest()
    assert upper_sha == EXPECTED_UPPER_N_SHA256
    assert order_sha == EXPECTED_ORDER_SHA256

    denominator_records = [
        t.denominator_record("S", (value for row in S for value in row)),
        t.denominator_record(
            "S_inverse", (value for row in inverse_S for value in row)
        ),
    ]
    denominator_text = "label\tvalue_count\tallowed\tcommon\tfactorization\n" + "\n".join(
        f"{label}\t{count}\t{str(allowed).lower()}\t{common}\t{factorization}"
        for label, count, common, factorization, allowed in denominator_records
    ) + "\n"
    (outdir / "H11_FLAG_DENOMINATORS.tsv").write_text(denominator_text)
    assert sha256(denominator_text.encode()).hexdigest() == EXPECTED_DENOMINATOR_SHA256
    assert all(record[-1] for record in denominator_records)
    return S_full, inverse_S_full, order, upper_N


def solve_upper(upper_N, rhs):
    solution = [QPoly() for _ in rhs]
    for row in range(len(rhs) - 1, -1, -1):
        value = rhs[row]
        for column in range(row + 1, len(rhs)):
            if upper_N[row][column] and solution[column]:
                value -= upper_N[row][column]*solution[column]
        solution[row] = value
        _, _, terms, degree = qpoly_stats(solution[row:row + 1])
        print(
            f"triangular_rhs_row={row};q_terms={terms};max_q_degree={degree}",
            flush=True,
        )
    unit_upper = [
        [upper_N[i][j] + QPoly(1 if i == j else 0) for j in range(len(rhs))]
        for i in range(len(rhs))
    ]
    assert matvec_q(unit_upper, solution) == rhs
    return solution


def empty_parameter_value(polynomial, pivots, pivot_values):
    pivot_position = {variable: index for index, variable in enumerate(pivots)}
    out = QPoly()
    retained = 0
    for count, (monomial, coefficient) in enumerate(sorted(polynomial.items()), 1):
        value = QPoly.coerce(coefficient)
        for variable in monomial:
            position = pivot_position.get(variable)
            if position is None:
                value = QPoly()
                break
            value *= pivot_values[position]
        if value:
            out += value
            retained += 1
        if count % 250 == 0:
            print(
                f"literal_P12_terms_scanned={count};retained_terms={retained};"
                f"current_q_terms={len(out.coefficients)}",
                flush=True,
            )
    return out, retained


def main():
    outdir = Path(os.environ["TD6_OUTPUT_DIR"]).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    assert os.environ.get("AWS_RUN_TAG", "").startswith(
        "td6_v89h11_allq_p12_flag_functional_"
    )
    print("producer=TD6-V89H11-ALLQ-P12-FLAG-FUNCTIONAL")
    print(f"flag_result_sha256={FLAG_RESULT_SHA256}")
    print(f"flag_freeze_sha256={FLAG_FREEZE_SHA256}")
    print(f"h7_result_sha256={H7_RESULT_SHA256}")
    print("retained_q_exponents=" + ",".join(map(str, ALL_Q)))
    print("q15_absent_target_shear=true", flush=True)

    events, bands, seen = v87.build_bands()
    first = v87.compile_first(bands)
    p12 = v87.compile_current_degree12(bands)
    assert events == 2 and len(first) == 38
    assert set(seen) == set(ALL_Q)
    assert all(seen[exponent] == 1 for exponent in ALL_Q)
    sources = [v87.source_polynomial(row, rhs) for _, row, rhs in first]
    assert all(all(len(monomial) <= 1 for monomial in source) for source in sources)
    _, raw_common = v87.assert_denominators_allowed([p12, *sources])
    assert raw_common == U*H and raw_common.gcd(F).total_degree() == 0
    print("literal_transport_FIRST_P12_rebuilt=true")
    print(f"literal_P12_parameter_terms={len(p12)}")
    print(f"raw_source_common_denominator=({raw_common})")
    print("raw_source_denominator_coprime_F=true", flush=True)

    specialized_first = h6.specialize_first(first)
    specialized_p12 = h6.specialize_polynomial(p12)
    pivots = h5.base_pivot_columns(specialized_first)
    assert len(pivots) == len(set(pivots)) == 38
    A0 = [
        [row.get(pivot, QPoly()).constant() for pivot in pivots]
        for _, row, _ in specialized_first
    ]
    A = [
        [row.get(pivot, QPoly()) for pivot in pivots]
        for _, row, _ in specialized_first
    ]
    rhs = [rhs for _, _, rhs in specialized_first]
    inverse_A0 = h5.inverse_constant_matrix(A0)
    B = h5.matmul_constant_q(inverse_A0, A)
    identity_q = p.identity_matrix(38)
    N = [[B[i][j] - identity_q[i][j] for j in range(38)] for i in range(38)]
    n_sha, n_entries, n_terms, n_degree = p.matrix_stats(N)
    assert n_sha == EXPECTED_N_SHA256
    assert (n_entries, n_terms, n_degree) == (532, 6069, 1)
    print(f"N_sha256={n_sha}")
    print("N_affine_allq=true", flush=True)

    S_full, inverse_S_full, order, upper_N = reconstruct_flag(N, outdir)
    W = [[S_full[i][order[j]] for j in range(38)] for i in range(38)]
    inverse_W = [
        [inverse_S_full[order[i]][j] for j in range(38)]
        for i in range(38)
    ]
    assert h5.matmul_constant(W, inverse_W) == identity_constant(38)
    assert h5.matmul_constant(inverse_W, W) == identity_constant(38)
    print("flag_basis_and_permutation_two_sided=true")
    print("full_allq_N_strict_upper_replayed=true", flush=True)

    base_rhs = matvec_constant_q(inverse_A0, rhs)
    triangular_rhs = matvec_constant_q(inverse_W, base_rhs)
    triangular_solution = solve_upper(upper_N, triangular_rhs)
    pivot_solution = matvec_constant_q(W, triangular_solution)
    assert matvec_q(A, pivot_solution) == rhs
    pivot_sha, pivot_terms = write_qvector(
        outdir / "ALLQ_ZERO_NONPIVOT_FIRST_SOLUTION.tsv", pivot_solution
    )
    _, pivot_nonzero, _, pivot_degree = qpoly_stats(pivot_solution)
    print(f"pivot_solution_sha256={pivot_sha}")
    print(f"pivot_solution_nonzero_entries={pivot_nonzero}")
    print(f"pivot_solution_q_terms={pivot_terms}")
    print(f"pivot_solution_max_total_q_degree={pivot_degree}")
    print("original_FIRST_zero_nonpivot_solution_replay=true", flush=True)

    functional, retained_p12_terms = empty_parameter_value(
        specialized_p12, pivots, pivot_solution
    )
    assert functional
    functional_sha, functional_terms = write_qpoly(
        outdir / "ALLQ_EMPTY_PARAMETER_P12_FUNCTIONAL.tsv", functional
    )
    functional_degree = max(map(len, functional.coefficients), default=0)
    support = sorted(functional.coefficients)
    mixed = [monomial for monomial in support if len(set(monomial)) > 1]
    print(f"literal_P12_retained_pivot_only_terms={retained_p12_terms}")
    print(f"allq_empty_parameter_functional_sha256={functional_sha}")
    print(f"allq_empty_parameter_functional_q_terms={functional_terms}")
    print(f"allq_empty_parameter_functional_support_count={len(support)}")
    print(f"allq_empty_parameter_functional_mixed_support_count={len(mixed)}")
    print(f"allq_empty_parameter_functional_max_total_q_degree={functional_degree}")
    print("empty_parameter_functional_computed_from_literal_P12=true", flush=True)

    tail_positive = {
        monomial: coefficient
        for monomial, coefficient in functional.coefficients.items()
        if monomial and all(exponent in TAIL for exponent in monomial)
    }
    assert set(tail_positive) == {(14,)}
    q14_empty = functional.coefficients[(14,)]
    coordinates = m.r.scalar_coordinates(E3.coerce(q14_empty))
    selected = Rat3.coerce(coordinates[0])
    expected_numerator = (
        Rat3(3856216)*Rat3(V)**10*Rat3(U)**2/Rat3(375)
        + Rat3(1625866424)*Rat3(V)**8*Rat3(U)**5/Rat3(375)
        + Rat3(30525031264)*Rat3(V)**6*Rat3(U)**8/Rat3(375)
        - Rat3(10638708808)*Rat3(V)**4*Rat3(U)**11/Rat3(375)
        - Rat3(4168187296)*Rat3(V)**2*Rat3(U)**14/Rat3(75)
        + Rat3(710528)*Rat3(U)**17/Rat3(15)
    )
    expected = expected_numerator / Rat3(V**3*(V**2 - 4*U**3)**2)
    assert selected == expected and selected
    print("tail_specialization_positive_support_exactly_q14=true")
    print("pure_q14_coordinate0_equals_promoted_H7=true")
    print("pure_q14_coordinate0_nonzero=true", flush=True)

    denominator_records = [
        t.denominator_record(
            "pivot_solution",
            (
                coefficient
                for value in pivot_solution
                for coefficient in value.coefficients.values()
            ),
        ),
        t.denominator_record(
            "empty_parameter_functional", functional.coefficients.values()
        ),
    ]
    denominator_text = "label\tvalue_count\tallowed\tcommon\tfactorization\n" + "\n".join(
        f"{label}\t{count}\t{str(allowed).lower()}\t{common}\t{factorization}"
        for label, count, common, factorization, allowed in denominator_records
    ) + "\n"
    (outdir / "ALLQ_P12_FUNCTIONAL_DENOMINATORS.tsv").write_text(denominator_text)
    denominator_sha = sha256(denominator_text.encode()).hexdigest()
    denominators_allowed = all(record[-1] for record in denominator_records)
    print(f"functional_denominator_ledger_sha256={denominator_sha}")
    print(f"functional_denominators_registered={str(denominators_allowed).lower()}")

    result_lines = [
        f"flag_result_sha256={FLAG_RESULT_SHA256}",
        f"flag_freeze_sha256={FLAG_FREEZE_SHA256}",
        f"h7_result_sha256={H7_RESULT_SHA256}",
        f"N_sha256={n_sha}",
        f"pivot_solution_sha256={pivot_sha}",
        f"empty_parameter_functional_sha256={functional_sha}",
        f"empty_parameter_functional_q_terms={functional_terms}",
        f"empty_parameter_functional_max_total_q_degree={functional_degree}",
        f"functional_denominator_ledger_sha256={denominator_sha}",
        "all_22_q_independent_untruncated=true",
        "strict_upper_triangular_solve=true",
        "original_FIRST_zero_nonpivot_solution_replay=true",
        "empty_parameter_functional_computed_from_literal_P12=true",
        "pure_q14_coordinate0_equals_promoted_H7=true",
        "pure_q14_coordinate0_nonzero=true",
        f"functional_denominators_registered={str(denominators_allowed).lower()}",
        "full_17_parameter_normal_form_computed=false",
        "unit_ideal_claim=false",
        "source_point_claim=false",
        "whole_TD6_killed=false",
        "JC2_resolved=false",
    ]
    result_text = "\n".join(result_lines) + "\n"
    (outdir / "ALLQ_P12_FLAG_FUNCTIONAL_RESULT.txt").write_text(result_text)
    result_sha = sha256(result_text.encode()).hexdigest()
    print(f"allq_p12_flag_functional_result_sha256={result_sha}")
    if denominators_allowed:
        print("TD6-V89H11-ALLQ-P12-FLAG-FUNCTIONAL PASS")
    else:
        print("TD6-V89H11-ALLQ-P12-FLAG-FUNCTIONAL DENOMINATOR-FAIL-CLOSED")
    v85.restore_base_qd_state()


if __name__ == "__main__":
    main()
