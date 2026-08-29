#!/usr/bin/env python3
"""Exact common invariant flag for the full-q transported-FIRST block."""

from hashlib import sha256
import importlib.util
import os
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
PARENT_PATH = HERE / "replay_v89h10_allq_mod_f_unitriangular_functional_v1.py"
PARENT_SHA256 = "4ff99ca9b7d8539aa369b65a953da63dc731d12ba3faf4184678fe8d0b6b9524"
GRAPH_RESULT_PATH = HERE / "GRAPH_RESULT.md"
GRAPH_RESULT_SHA256 = "d07b2258d83cb0dfe48193abcf773ccc8a2d943001873858ae0cad58cd5292f0"
GRAPH_FREEZE_PATH = HERE / "GRAPH_FREEZE.sha256"
GRAPH_FREEZE_SHA256 = "39973cb2bd9a215b5dda1d1c32837855aaa08f4c4edaf3bb75aea811fdd09cd4"
for path, expected in (
    (PARENT_PATH, PARENT_SHA256),
    (GRAPH_RESULT_PATH, GRAPH_RESULT_SHA256),
    (GRAPH_FREEZE_PATH, GRAPH_FREEZE_SHA256),
):
    assert sha256(path.read_bytes()).hexdigest() == expected
spec = importlib.util.spec_from_file_location("td6_v89h10t_parent", PARENT_PATH)
p = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = p
spec.loader.exec_module(p)

h5, h6, v87, v85, m = p.h5, p.h6, p.v87, p.v85, p.m
QPoly, E3 = p.QPoly, p.E3
U, V = p.U, p.V
LOW = tuple(range(2, 15))
SCC = tuple(range(14))
EXPECTED_N_SHA256 = "38fb14e38daa36d597cc7ae1cd2bd5dd402ef2cd1587337321b8c204eeeb7f36"
SPECIAL_HF = V**2 - 4*U**3
SPECIAL_ALLOWED_MONIC = tuple(v85.monic(value) for value in (U, V, SPECIAL_HF))


def matrix_rank(matrix, columns):
    work = [list(row) for row in matrix if any(row)]
    pivot_row = 0
    for column in range(columns):
        hit = next(
            (row for row in range(pivot_row, len(work)) if work[row][column]),
            None,
        )
        if hit is None:
            continue
        work[pivot_row], work[hit] = work[hit], work[pivot_row]
        inverse = work[pivot_row][column].inverse()
        work[pivot_row] = [value*inverse for value in work[pivot_row]]
        for row in range(len(work)):
            if row == pivot_row or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [
                left-factor*right
                for left, right in zip(work[row], work[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == len(work):
            break
    return pivot_row


def nullspace(matrix, columns):
    work = [list(row) for row in matrix if any(row)]
    pivots = []
    pivot_row = 0
    for column in range(columns):
        hit = next(
            (row for row in range(pivot_row, len(work)) if work[row][column]),
            None,
        )
        if hit is None:
            continue
        work[pivot_row], work[hit] = work[hit], work[pivot_row]
        inverse = work[pivot_row][column].inverse()
        work[pivot_row] = [value*inverse for value in work[pivot_row]]
        for row in range(len(work)):
            if row == pivot_row or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [
                left-factor*right
                for left, right in zip(work[row], work[pivot_row])
            ]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == len(work):
            break
    free = [column for column in range(columns) if column not in pivots]
    basis = []
    for free_column in free:
        vector = [E3() for _ in range(columns)]
        vector[free_column] = E3(1)
        for row, pivot in reversed(list(enumerate(pivots))):
            vector[pivot] = -sum(
                (work[row][column]*vector[column] for column in free),
                E3(),
            )
        assert all(
            not sum((left*right for left, right in zip(row, vector)), E3())
            for row in matrix
        )
        basis.append(vector)
    return basis


def columns_matrix(columns, size):
    return [[columns[column][row] for column in range(size)] for row in range(size)]


def independent_columns(columns, size):
    if not columns:
        return 0
    matrix = [[column[row] for column in columns] for row in range(size)]
    return matrix_rank(matrix, len(columns))


def complete_basis(columns, size):
    out = [list(column) for column in columns]
    assert independent_columns(out, size) == len(out)
    for index in range(size):
        candidate = [E3(1 if row == index else 0) for row in range(size)]
        if independent_columns(out + [candidate], size) > len(out):
            out.append(candidate)
        if len(out) == size:
            break
    assert len(out) == size
    return columns_matrix(out, size)


def matvec(matrix, vector):
    return [
        sum((value*coordinate for value, coordinate in zip(row, vector)), E3())
        for row in matrix
    ]


def write_constant_matrix(path, matrix):
    lines = ["row\tcolumn\tcoefficient_exact"]
    for row, values in enumerate(matrix):
        for column, value in enumerate(values):
            if value:
                lines.append(f"{row}\t{column}\t{m.e3_exact(value)}")
    text = "\n".join(lines) + "\n"
    path.write_text(text)
    return sha256(text.encode()).hexdigest(), len(lines) - 1


def write_qmatrix(path, matrix):
    lines = ["row\tcolumn\tq_monomial\tcoefficient_exact"]
    for row, values in enumerate(matrix):
        for column, value in enumerate(values):
            for monomial, coefficient in sorted(value.coefficients.items()):
                lines.append(
                    f"{row}\t{column}\t{monomial!r}\t{m.e3_exact(coefficient)}"
                )
    text = "\n".join(lines) + "\n"
    path.write_text(text)
    return sha256(text.encode()).hexdigest(), len(lines) - 1


def denominator_record(label, values):
    values = list(values)
    common = v85.monic(m.denominator_for(values)) if values else m.tri.ONE
    factors = v85.factor_list(common)
    allowed = all(v85.monic(factor) in SPECIAL_ALLOWED_MONIC for factor in factors)
    return label, len(values), common, common.factor(), allowed


def main():
    outdir = Path(os.environ["TD6_OUTPUT_DIR"]).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    assert os.environ.get("AWS_RUN_TAG", "").startswith(
        "td6_v89h10t_allq_simultaneous_triangular_flag_"
    )
    print("producer=TD6-V89H10T-ALLQ-SIMULTANEOUS-TRIANGULAR-FLAG")
    print(f"parent_sha256={PARENT_SHA256}")
    print(f"graph_result_sha256={GRAPH_RESULT_SHA256}")
    print("P12_compile_and_division_skipped=true", flush=True)

    events, bands, seen = v87.build_bands()
    first = v87.compile_first(bands)
    assert events == 2 and len(first) == 38
    assert set(seen) == set(p.ALLOWED_Q)
    assert all(seen[exponent] == 1 for exponent in p.ALLOWED_Q)
    sources = [v87.source_polynomial(row, rhs) for _, row, rhs in first]
    _, raw_common = v87.assert_denominators_allowed(sources)
    print(f"raw_FIRST_common_denominator=({raw_common})")
    print("literal_allq_FIRST_rebuilt=true", flush=True)

    specialized = h6.specialize_first(first)
    pivots = h5.base_pivot_columns(specialized)
    A0 = [
        [row.get(pivot, QPoly()).constant() for pivot in pivots]
        for _, row, _ in specialized
    ]
    A = [
        [row.get(pivot, QPoly()) for pivot in pivots]
        for _, row, _ in specialized
    ]
    inverse_A0 = h5.inverse_constant_matrix(A0)
    B = h5.matmul_constant_q(inverse_A0, A)
    identity = p.identity_matrix(38)
    N = [[B[i][j]-identity[i][j] for j in range(38)] for i in range(38)]
    n_sha, n_entries, n_terms, n_degree = p.matrix_stats(N)
    assert n_sha == EXPECTED_N_SHA256
    assert (n_entries, n_terms, n_degree) == (532, 6069, 1)
    print(f"N_sha256={n_sha}", flush=True)

    coefficient_matrices = []
    for exponent in LOW:
        matrix = [
            [N[i][j].coefficients.get((exponent,), E3()) for j in SCC]
            for i in SCC
        ]
        assert any(value for row in matrix for value in row)
        coefficient_matrices.append(matrix)

    flag = []
    records = ["dimension\tquotient_dimension\tcommon_kernel_dimension\tvector_sha256"]
    for dimension in range(14):
        change = complete_basis(flag, 14)
        inverse_change = h5.inverse_constant_matrix(change)
        transformed = [
            h5.matmul_constant(h5.matmul_constant(inverse_change, matrix), change)
            for matrix in coefficient_matrices
        ]
        assert all(
            not transformed_matrix[row][column]
            for transformed_matrix in transformed
            for row in range(dimension, 14)
            for column in range(dimension)
        )
        quotient_size = 14 - dimension
        stacked = []
        for transformed_matrix in transformed:
            stacked.extend(
                [row[dimension:] for row in transformed_matrix[dimension:]]
            )
        kernel = nullspace(stacked, quotient_size)
        print(
            f"flag_dimension={dimension};quotient_dimension={quotient_size};"
            f"common_kernel_dimension={len(kernel)}",
            flush=True,
        )
        if not kernel:
            print("simultaneous_strict_triangular_flag=false")
            print("TD6-V89H10T-ALLQ-SIMULTANEOUS-TRIANGULAR-FLAG NO-FLAG-PASS")
            v85.restore_base_qd_state()
            return
        quotient_vector = kernel[0]
        lifted_coordinates = [E3() for _ in range(dimension)] + quotient_vector
        vector = matvec(change, lifted_coordinates)
        assert independent_columns(flag + [vector], 14) == dimension + 1
        digest_text = "\n".join(m.e3_exact(value).__repr__() for value in vector) + "\n"
        vector_sha = sha256(digest_text.encode()).hexdigest()
        records.append(
            f"{dimension + 1}\t{quotient_size}\t{len(kernel)}\t{vector_sha}"
        )
        flag.append(vector)

    S = columns_matrix(flag, 14)
    inverse_S = h5.inverse_constant_matrix(S)
    assert h5.matmul_constant(S, inverse_S) == [
        [E3(1 if i == j else 0) for j in range(14)] for i in range(14)
    ]
    assert h5.matmul_constant(inverse_S, S) == [
        [E3(1 if i == j else 0) for j in range(14)] for i in range(14)
    ]
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
    (outdir / "ALLQ_COMMON_FLAG_TELEMETRY.tsv").write_text(flag_text)
    flag_sha = sha256(flag_text.encode()).hexdigest()
    S_sha, S_terms = write_constant_matrix(outdir / "ALLQ_SCC_FLAG_BASIS.tsv", S)
    inverse_S_sha, inverse_S_terms = write_constant_matrix(
        outdir / "ALLQ_SCC_FLAG_BASIS_INVERSE.tsv", inverse_S
    )

    S_full = [[E3(1 if i == j else 0) for j in range(38)] for i in range(38)]
    inverse_S_full = [row[:] for row in S_full]
    for i in SCC:
        for j in SCC:
            S_full[i][j] = S[i][j]
            inverse_S_full[i][j] = inverse_S[i][j]
    S_full_q = [[QPoly(value) for value in row] for row in S_full]
    transformed_N = h5.matmul_q(
        h5.matmul_constant_q(inverse_S_full, N), S_full_q
    )
    transformed_graph = {
        i: {j for j in range(38) if transformed_N[i][j]}
        for i in range(38)
    }
    order, cyclic_nodes = h5.topological_order(transformed_graph)
    assert not cyclic_nodes and len(order) == 38
    upper_N = [
        [transformed_N[order[i]][order[j]] for j in range(38)]
        for i in range(38)
    ]
    assert all(
        not upper_N[i][j] for i in range(38) for j in range(i + 1)
    )
    upper_sha, upper_terms = write_qmatrix(
        outdir / "ALLQ_STRICT_UPPER_N.tsv", upper_N
    )
    order_text = "position\toriginal_index\n" + "\n".join(
        f"{position}\t{index}" for position, index in enumerate(order)
    ) + "\n"
    (outdir / "ALLQ_STRICT_UPPER_ORDER.tsv").write_text(order_text)
    order_sha = sha256(order_text.encode()).hexdigest()

    denominator_records = [
        denominator_record("S", (value for row in S for value in row)),
        denominator_record(
            "S_inverse", (value for row in inverse_S for value in row)
        ),
    ]
    denominator_text = "label\tvalue_count\tallowed\tcommon\tfactorization\n" + "\n".join(
        f"{label}\t{count}\t{str(allowed).lower()}\t{common}\t{factorization}"
        for label, count, common, factorization, allowed in denominator_records
    ) + "\n"
    (outdir / "ALLQ_FLAG_DENOMINATORS.tsv").write_text(denominator_text)
    denominator_sha = sha256(denominator_text.encode()).hexdigest()
    allowed = all(record[-1] for record in denominator_records)

    print(f"common_flag_telemetry_sha256={flag_sha}")
    print(f"S_sha256={S_sha}")
    print(f"S_terms={S_terms}")
    print(f"S_inverse_sha256={inverse_S_sha}")
    print(f"S_inverse_terms={inverse_S_terms}")
    print("S_two_sided=true")
    print("all_low_q_coefficient_matrices_strict_upper=true")
    print(f"full_strict_upper_order_sha256={order_sha}")
    print(f"full_strict_upper_N_sha256={upper_sha}")
    print(f"full_strict_upper_N_terms={upper_terms}")
    print("full_allq_N_simultaneously_strict_upper=true")
    print("full_allq_N_nilpotence_index_at_most=38")
    print(f"flag_denominator_ledger_sha256={denominator_sha}")
    print(f"flag_denominators_registered={str(allowed).lower()}")
    print("expanded_polynomial_inverse_emitted=false")
    print("P12_functional_claim=false")
    if allowed:
        print("TD6-V89H10T-ALLQ-SIMULTANEOUS-TRIANGULAR-FLAG PASS")
    else:
        print("TD6-V89H10T-ALLQ-SIMULTANEOUS-TRIANGULAR-FLAG DENOMINATOR-FAIL-CLOSED")
    v85.restore_base_qd_state()


if __name__ == "__main__":
    main()
