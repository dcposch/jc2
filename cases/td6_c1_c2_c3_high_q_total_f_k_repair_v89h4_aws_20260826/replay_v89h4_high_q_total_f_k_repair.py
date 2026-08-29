#!/usr/bin/env python3
"""Exact denominator-cleared H1 high-q identity composed with total F."""

from hashlib import sha256
import importlib.util
import os
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
V87_PATH = HERE / "replay_v87tfaq_total_f_allq.py"
V87_SHA256 = "7c0890abbce996a221f9389372fa3705742d6ecd72531891bfeb5dfc2f1b9463"
assert sha256(V87_PATH.read_bytes()).hexdigest() == V87_SHA256
spec = importlib.util.spec_from_file_location("td6_v89h1_v87_parent", V87_PATH)
v87 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = v87
spec.loader.exec_module(v87)

QPoly = v87.QPoly
E3, Rat3 = v87.E3, v87.Rat3
m, v85 = v87.m, v87.v85
C, V, U = v87.C, v87.V, v87.U
F, H, B3 = v87.F, v87.H, v87.B3
HIGH = tuple(range(16, 25))
LOW = tuple(range(2, 15))
assert set(HIGH) | set(LOW) == set(v87.Q_EXPONENTS)
EXPECTED_BASE_REMAINDER_SHA256 = (
    "93121eef14c472c3c55b7acaeb1d0eff73b77d462ad8d5b197e8e21b9cda89c4"
)


def project_value(value):
    value = QPoly.coerce(value)
    return QPoly(0, {
        monomial: coefficient
        for monomial, coefficient in value.coefficients.items()
        if all(exponent in HIGH for exponent in monomial)
    })


def project_polynomial(polynomial):
    return v87.clean({
        monomial: project_value(value)
        for monomial, value in polynomial.items()
        if project_value(value)
    })


def project_first(first):
    return [
        (
            key,
            {
                variable: project_value(coefficient)
                for variable, coefficient in row.items()
                if project_value(coefficient)
            },
            project_value(rhs),
        )
        for key, row, rhs in first
    ]


def qpoly_digest(value):
    value = QPoly.coerce(value)
    lines = [
        f"{monomial!r}\t{m.e3_exact(coefficient)}"
        for monomial, coefficient in sorted(value.coefficients.items())
    ]
    return sha256(("\n".join(lines) + "\n").encode()).hexdigest()


def base_pivot_columns(first):
    normalized, pivots = [], []
    for row_index, (_, original_row, _) in enumerate(first):
        row = {
            variable: coefficient.constant()
            for variable, coefficient in original_row.items()
            if coefficient.constant()
        }
        for pivot, old in zip(pivots, normalized):
            factor = row.get(pivot, E3())
            if not factor:
                continue
            for variable, coefficient in old.items():
                value = row.get(variable, E3()) - factor*coefficient
                if value:
                    row[variable] = value
                else:
                    row.pop(variable, None)
        assert row, ("base_FIRST_dependent", row_index)
        pivot = min(row)
        inverse = row[pivot].inverse()
        row = {
            variable: coefficient*inverse
            for variable, coefficient in row.items() if coefficient
        }
        assert row[pivot] == E3(1)
        pivots.append(pivot)
        normalized.append(row)
    assert len(pivots) == len(set(pivots)) == 38
    return pivots


def inverse_constant_matrix(matrix):
    n = len(matrix)
    work = [
        list(row) + [E3(1) if i == j else E3() for j in range(n)]
        for i, row in enumerate(matrix)
    ]
    for column in range(n):
        pivot_row = next(
            (row for row in range(column, n) if work[row][column]), None
        )
        assert pivot_row is not None, ("singular_base_pivot_block", column)
        if pivot_row != column:
            work[column], work[pivot_row] = work[pivot_row], work[column]
        inverse = work[column][column].inverse()
        work[column] = [value*inverse for value in work[column]]
        for row in range(n):
            if row == column:
                continue
            factor = work[row][column]
            if factor:
                work[row] = [
                    left-factor*right
                    for left, right in zip(work[row], work[column])
                ]
    left = [row[:n] for row in work]
    assert all(
        left[i][j] == (E3(1) if i == j else E3())
        for i in range(n) for j in range(n)
    )
    return [row[n:] for row in work]


def matmul_constant(left, right):
    rows, middle, columns = len(left), len(right), len(right[0])
    out = [[E3() for _ in range(columns)] for _ in range(rows)]
    for i in range(rows):
        for k in range(middle):
            if not left[i][k]:
                continue
            for j in range(columns):
                if right[k][j]:
                    out[i][j] += left[i][k]*right[k][j]
    return out


def matmul_constant_q(left, right):
    rows, middle, columns = len(left), len(right), len(right[0])
    out = [[QPoly() for _ in range(columns)] for _ in range(rows)]
    for i in range(rows):
        for k in range(middle):
            if not left[i][k]:
                continue
            scalar = QPoly(left[i][k])
            for j in range(columns):
                if right[k][j]:
                    out[i][j] += scalar*right[k][j]
    return out


def matmul_q(left, right):
    rows, middle, columns = len(left), len(right), len(right[0])
    out = [[QPoly() for _ in range(columns)] for _ in range(rows)]
    for i in range(rows):
        for k in range(middle):
            if not left[i][k]:
                continue
            for j in range(columns):
                if right[k][j]:
                    out[i][j] += left[i][k]*right[k][j]
    return out


def is_identity(matrix):
    return all(
        matrix[i][j] == QPoly(1 if i == j else 0)
        for i in range(len(matrix)) for j in range(len(matrix))
    )


def topological_order(graph):
    indegree = {node: 0 for node in graph}
    for node in graph:
        for target in graph[node]:
            indegree[target] += 1
    ready = sorted(node for node, degree in indegree.items() if degree == 0)
    order = []
    while ready:
        node = ready.pop(0)
        order.append(node)
        for target in sorted(graph[node]):
            indegree[target] -= 1
            if indegree[target] == 0:
                ready.append(target)
                ready.sort()
    return order, sorted(node for node, degree in indegree.items() if degree)


def first_cycle(graph, restricted):
    restricted = set(restricted)
    state, stack, position = {}, [], {}

    def visit(node):
        state[node] = 1
        position[node] = len(stack)
        stack.append(node)
        for target in sorted(graph[node]):
            if target not in restricted:
                continue
            if state.get(target, 0) == 0:
                result = visit(target)
                if result:
                    return result
            elif state.get(target) == 1:
                return stack[position[target]:] + [target]
        stack.pop()
        position.pop(node)
        state[node] = 2
        return None

    for node in sorted(restricted):
        if state.get(node, 0) == 0:
            result = visit(node)
            if result:
                return result
    return []


def polynomial_matrix_inverse(B, order):
    n = len(B)
    permuted = [[B[order[i]][order[j]] for j in range(n)] for i in range(n)]
    for i in range(n):
        assert permuted[i][i] == QPoly(1)
        assert all(not permuted[i][j] for j in range(i))
    inverse = [[QPoly() for _ in range(n)] for _ in range(n)]
    for i in range(n):
        inverse[i][i] = QPoly(1)
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            value = QPoly()
            for k in range(i + 1, j + 1):
                if permuted[i][k] and inverse[k][j]:
                    value += permuted[i][k]*inverse[k][j]
            inverse[i][j] = -value
    assert is_identity(matmul_q(permuted, inverse))
    assert is_identity(matmul_q(inverse, permuted))
    position = {old: new for new, old in enumerate(order)}
    return [
        [inverse[position[i]][position[j]] for j in range(n)]
        for i in range(n)
    ]


def linear_combination(coefficients, polynomials):
    out = {}
    for coefficient, polynomial in zip(coefficients, polynomials):
        if coefficient:
            out = v87.add(out, v87.scale(polynomial, coefficient))
    return out


def divide_by_normalized_first(polynomial, normalized, pivots):
    remainder = dict(polynomial)
    quotients = [{} for _ in pivots]
    for index, (pivot, source) in enumerate(zip(pivots, normalized)):
        assert source.get((pivot,)) == QPoly(1)
        while True:
            targets = sorted(
                monomial for monomial, coefficient in remainder.items()
                if coefficient and pivot in monomial
            )
            if not targets:
                break
            monomial = targets[0]
            coefficient = remainder[monomial]
            reduced = list(monomial)
            reduced.remove(pivot)
            multiplier = {tuple(reduced): coefficient}
            quotients[index] = v87.add(quotients[index], multiplier)
            remainder = v87.add(
                remainder, v87.multiply(multiplier, source), -1
            )
        print(
            f"p12_division_pivot={index + 1}/38;"
            f"remainder_terms={len(remainder)}",
            flush=True,
        )
    replay = dict(remainder)
    for quotient, source in zip(quotients, normalized):
        replay = v87.add(replay, v87.multiply(quotient, source))
    assert replay == polynomial
    return v87.clean(remainder), quotients


def write_polynomial(path, polynomial):
    lines = ["parameter_monomial\tq_monomial\tcoefficient_exact"]
    for parameter_monomial, value in sorted(polynomial.items()):
        for q_monomial, coefficient in sorted(value.coefficients.items()):
            lines.append(
                f"{parameter_monomial!r}\t{q_monomial!r}\t"
                f"{m.e3_exact(coefficient)}"
            )
    text = "\n".join(lines) + "\n"
    path.write_text(text)
    return sha256(text.encode()).hexdigest()


def write_total_f_multipliers(
    path, p12_multiplier, first_multipliers, first, f_multiplier
):
    """Emit every exact original-source multiplier coefficient."""
    lines = [
        "kind\tindex\tkey\tparameter_monomial\tq_monomial\tcoefficient_exact"
    ]

    def emit(kind, index, key, polynomial):
        for parameter_monomial, value in sorted(polynomial.items()):
            for q_monomial, coefficient in sorted(value.coefficients.items()):
                lines.append(
                    f"{kind}\t{index}\t{key!r}\t{parameter_monomial!r}\t"
                    f"{q_monomial!r}\t{m.e3_exact(coefficient)}"
                )

    emit("P12", 0, "literal_raw_P12", p12_multiplier)
    for index, (multiplier, (key, _, _)) in enumerate(
        zip(first_multipliers, first)
    ):
        emit("FIRST", index, key, multiplier)
    emit("F", 0, "literal_base_F", f_multiplier)
    text = "\n".join(lines) + "\n"
    path.write_text(text)
    return sha256(text.encode()).hexdigest(), len(lines) - 1


def finalize_early(outdir, graph_sha, cycle, common):
    lines = [
        f"v87_parent_sha256={V87_SHA256}",
        "high_q_exponents=" + ",".join(map(str, HIGH)),
        "triangular_graph_acyclic=false",
        "first_cycle=" + ",".join(map(str, cycle)),
        f"graph_sha256={graph_sha}",
        f"common={common}",
        "claim=triangular_shortcut_obstruction_only",
    ]
    text = "\n".join(lines) + "\n"
    path = outdir / "HIGH_Q_TRIANGULAR_EXACT_RESULT.txt"
    path.write_text(text)
    digest = sha256(text.encode()).hexdigest()
    print("triangular_graph_acyclic=false")
    print("first_cycle=" + ",".join(map(str, cycle)))
    print(f"exact_result_sha256={digest}")
    print("high_q_nonintegrability_claim=false")
    print("TD6-V89H1-HIGH-Q-TRIANGULAR-OBSTRUCTION DIAGNOSTIC-PASS")


def main():
    outdir = Path(os.environ["TD6_OUTPUT_DIR"]).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    assert os.environ.get("AWS_RUN_TAG", "").startswith(
        "td6_v89h4_high_q_total_f_k_repair_"
    )
    print("producer=TD6-V89H4-HIGH-Q-TOTAL-F-K-REPAIR")
    print("high_q_exponents=" + ",".join(map(str, HIGH)))
    print("low_q_specialized_zero=true")
    print("q15_absent_target_shear=true")
    print("q_ring=untruncated_sparse_multivariate_E3", flush=True)

    events, bands, seen = v87.build_bands()
    total_first = v87.compile_first(bands)
    total_p12 = v87.compile_current_degree12(bands)
    first = project_first(total_first)
    p12 = project_polynomial(total_p12)
    assert events == 2 and len(first) == 38
    assert all(seen[exponent] == 1 for exponent in HIGH)
    print("literal_transport_FIRST_P12_rebuilt=true", flush=True)

    generic_p12 = v87.q_constant(p12)
    generic_sources = [
        v87.q_constant(v87.source_polynomial(row, rhs))
        for _, row, rhs in first
    ]
    v85_p12_digest, v85_first_digests = v87.v86.read_v85_inventory()
    assert m.polynomial_digest(generic_p12) == v85_p12_digest
    assert all(
        m.polynomial_digest(source) == v85_first_digests[index]
        for index, source in enumerate(generic_sources)
    )
    print("q_zero_sources_match_frozen_V85=true", flush=True)

    pivots = base_pivot_columns(first)
    A0 = [
        [row.get(pivot, QPoly()).constant() for pivot in pivots]
        for _, row, _ in first
    ]
    A = [
        [row.get(pivot, QPoly()) for pivot in pivots]
        for _, row, _ in first
    ]
    inverse_A0 = inverse_constant_matrix(A0)
    base_inverse_check = matmul_constant(inverse_A0, A0)
    assert all(
        base_inverse_check[i][j] == (E3(1) if i == j else E3())
        for i in range(38) for j in range(38)
    )
    B = matmul_constant_q(inverse_A0, A)
    assert all(
        B[i][j].constant() == (E3(1) if i == j else E3())
        for i in range(38) for j in range(38)
    )
    N = [
        [B[i][j] - QPoly(1 if i == j else 0) for j in range(38)]
        for i in range(38)
    ]
    assert all(not value.constant() for row in N for value in row)
    print("base_FIRST_pivot_block_inverted=true", flush=True)

    graph = {i: set() for i in range(38)}
    graph_lines = [
        "row\tcolumn\trow_key\tpivot_variable\tq_support\tq_terms\tsha256"
    ]
    for i in range(38):
        for j in range(38):
            if not N[i][j]:
                continue
            graph[i].add(j)
            support = sorted({
                exponent
                for monomial in N[i][j].coefficients
                for exponent in monomial
            })
            graph_lines.append(
                f"{i}\t{j}\t{first[i][0]!r}\t{pivots[j]}\t"
                f"{','.join(map(str, support))}\t"
                f"{len(N[i][j].coefficients)}\t{qpoly_digest(N[i][j])}"
            )
    graph_text = "\n".join(graph_lines) + "\n"
    graph_path = outdir / "HIGH_Q_TRIANGULAR_GRAPH.tsv"
    graph_path.write_text(graph_text)
    graph_sha = sha256(graph_text.encode()).hexdigest()
    order, cyclic = topological_order(graph)
    print(f"triangular_graph_edges={sum(map(len, graph.values()))}")
    print(f"triangular_graph_sha256={graph_sha}", flush=True)

    assert not cyclic, ("frozen_H1_DAG_not_reproduced", first_cycle(graph, cyclic))

    assert len(order) == 38
    inverse_B = polynomial_matrix_inverse(B, order)
    assert is_identity(matmul_q(B, inverse_B))
    assert is_identity(matmul_q(inverse_B, B))
    T = matmul_q(inverse_B, [
        [QPoly(value) for value in row] for row in inverse_A0
    ])
    assert is_identity(matmul_q(T, A))
    print("triangular_graph_acyclic=true")
    print("topological_order=" + ",".join(map(str, order)))
    print("finite_polynomial_FIRST_inverse_two_sided=true", flush=True)

    original_sources = [
        v87.source_polynomial(row, rhs) for _, row, rhs in first
    ]
    normalized = [
        linear_combination(T[i], original_sources) for i in range(38)
    ]
    for i, source in enumerate(normalized):
        for j, pivot in enumerate(pivots):
            assert source.get((pivot,), QPoly()) == QPoly(1 if i == j else 0)
    print("normalized_FIRST_original_source_replay=true", flush=True)

    remainder, quotients = divide_by_normalized_first(p12, normalized, pivots)
    base_remainder = v87.q_constant(remainder)
    assert m.polynomial_digest(base_remainder) == EXPECTED_BASE_REMAINDER_SHA256
    positive = v87.clean({
        monomial: QPoly(0, {
            q_monomial: coefficient
            for q_monomial, coefficient in value.coefficients.items()
            if q_monomial
        })
        for monomial, value in remainder.items()
    })
    remainder_path = outdir / "HIGH_Q_P12_REMAINDER.tsv"
    remainder_sha = write_polynomial(remainder_path, remainder)

    relations = []
    for source_index in range(38):
        relation = {}
        for quotient, row in zip(quotients, T):
            if row[source_index]:
                relation = v87.add(
                    relation, v87.scale(quotient, row[source_index])
                )
        relations.append(relation)
    replay = {}
    for relation, source in zip(relations, original_sources):
        replay = v87.add(replay, v87.multiply(relation, source))
    assert replay == v87.add(p12, remainder, -1)
    active = next(index for index, relation in enumerate(relations) if relation)
    omitted = {}
    for index, (relation, source) in enumerate(zip(relations, original_sources)):
        if index != active:
            omitted = v87.add(omitted, v87.multiply(relation, source))
    assert omitted != v87.add(p12, remainder, -1)
    print("P12_reduction_original_FIRST_source_replay=true")
    print(f"FIRST_omission_negative_control_index={active}", flush=True)

    multiplier_lines = [
        "kind\tindex\tkey\tparameter_terms\tcoefficient_terms\tsha256"
    ]
    for index, (relation, (key, _, _)) in enumerate(zip(relations, first)):
        multiplier_lines.append(
            f"FIRST\t{index}\t{key!r}\t{len(relation)}\t"
            f"{v87.coefficient_term_count(relation)}\t{v87.full_digest(relation)}"
        )
    multiplier_text = "\n".join(multiplier_lines) + "\n"
    multiplier_path = outdir / "HIGH_Q_SOURCE_MULTIPLIER_INVENTORY.tsv"
    multiplier_path.write_text(multiplier_text)
    multiplier_sha = sha256(multiplier_text.encode()).hexdigest()

    collapse = not positive
    certificate = None
    if collapse:
        assert set(remainder) == {()}
        unit = remainder[()]
        assert set(unit.coefficients) == {()}
        unit_inverse = unit.inverse()
        certificate = v87.scale(p12, unit_inverse)
        for relation, source in zip(relations, original_sources):
            certificate = v87.add(
                certificate,
                v87.scale(v87.multiply(relation, source), -unit_inverse),
            )
        assert certificate == {(): QPoly(1)}
        without_p12 = v87.add(
            certificate, v87.scale(p12, -unit_inverse)
        )
        assert without_p12 != {(): QPoly(1)}
        print("high_q_P12_remainder_equals_q_zero_unit=true")
        print("literal_P12_omission_negative_control=true", flush=True)
    else:
        first_parameter = min(positive)
        first_q = min(positive[first_parameter].coefficients)
        print("high_q_P12_remainder_equals_q_zero_unit=false")
        print(f"first_obstruction_parameter_monomial={first_parameter!r}")
        print(f"first_obstruction_q_monomial={first_q!r}", flush=True)

    assert collapse and certificate is not None
    audited = [p12, *original_sources, *normalized, *relations, remainder]
    audited.extend({(): value} for row in T for value in row if value)
    audited.append(certificate)
    coefficients = list(v87.all_coefficients(audited))
    common = v85.monic(m.denominator_for(coefficients))

    K = (
        2*C*V**2*U + 16*C*U**4 - V**4
        - 14*V**2*U**3 + 16*U**6
    )
    G = 2*C*U - V**2 + 2*U**3
    assert B3 - K - 2*F*G == m.tri.ZERO
    assert B3 - K - F*G != m.tri.ZERO

    reduced_common = common
    k_exponent = 0
    while not reduced_common % K:
        reduced_common //= K
        k_exponent += 1
    assert k_exponent == 1
    allowed_part = reduced_common
    assert common == K*allowed_part
    assert v85.factors_allowed(allowed_part), allowed_part.factor()
    assert allowed_part.gcd(F).total_degree() == 0
    cleared_count = v87.assert_polynomial_after_clear(coefficients, common)

    common_q = QPoly(E3(Rat3(common)))
    p12_multiplier = {(): common_q*unit_inverse}
    first_multipliers = [
        v87.scale(
            v87.scale(relation, -unit_inverse),
            common_q,
        )
        for relation in relations
    ]
    source_terms = [v87.multiply(p12_multiplier, p12)]
    source_terms.extend(
        v87.multiply(multiplier, source)
        for multiplier, source in zip(first_multipliers, original_sources)
    )
    cleared_source_identity = {}
    for term in source_terms:
        cleared_source_identity = v87.add(cleared_source_identity, term)
    assert cleared_source_identity == {(): common_q}

    f_multiplier_base = 2*allowed_part*G
    f_multiplier = {(): QPoly(E3(Rat3(f_multiplier_base)))}
    f_source = {(): QPoly(E3(Rat3(F)))}
    f_term = v87.multiply(f_multiplier, f_source)
    total_target_base = allowed_part*B3
    total_target = {(): QPoly(E3(Rat3(total_target_base)))}
    total_identity = v87.add(cleared_source_identity, f_term)
    assert total_identity == total_target

    without_f = cleared_source_identity
    without_p12 = {}
    for term in source_terms[1:]:
        without_p12 = v87.add(without_p12, term)
    without_p12 = v87.add(without_p12, f_term)
    without_first = v87.add(
        total_identity, source_terms[active + 1], -1
    )
    assert without_f != total_target
    assert without_p12 != total_target
    assert without_first != total_target

    multiplier_polynomials = [
        p12_multiplier, *first_multipliers, f_multiplier
    ]
    multiplier_coefficients = list(v87.all_coefficients(multiplier_polynomials))
    multiplier_common = v85.monic(m.denominator_for(multiplier_coefficients))
    assert multiplier_common.total_degree() == 0
    multiplier_polynomial_count = v87.assert_polynomial_after_clear(
        multiplier_coefficients, m.tri.ONE
    )
    final_audited = [
        p12, *original_sources, *multiplier_polynomials,
        *source_terms, f_term, total_target,
    ]
    final_coefficients, final_common = v87.assert_denominators_allowed(
        final_audited
    )
    final_cleared_count = v87.assert_polynomial_after_clear(
        final_coefficients, final_common
    )

    total_multiplier_path = outdir / "HIGH_Q_TOTAL_F_CLEARED_MULTIPLIERS.tsv"
    total_multiplier_sha, total_multiplier_rows = write_total_f_multipliers(
        total_multiplier_path,
        p12_multiplier,
        first_multipliers,
        first,
        f_multiplier,
    )
    print(f"h1_family_common_denominator=({common})")
    print(f"h1_family_common_denominator_factor={common.factor()}")
    print(f"h1_K_denominator_exponent={k_exponent}")
    print(f"h1_allowed_part=({allowed_part})")
    print(f"h1_allowed_part_factor={allowed_part.factor()}")
    print(f"h1_cleared_relation_target=K*allowed_part=({common})")
    print(f"total_F_composed_target=allowed_part*B3=({total_target_base})")
    print(f"total_F_composed_target_factor={total_target_base.factor()}")
    print(f"final_family_common_denominator=({final_common})")
    print(f"final_family_common_denominator_factor={final_common.factor()}")
    print("final_denominator_radical_subset_U_H_B3=true")
    print("K_inverted=false")
    print("F_inverted=false")
    print("no_q_expression_inverted=true")
    print(f"h1_clear_scalar_coordinate_count={cleared_count}")
    print(f"multiplier_polynomial_scalar_coordinate_count={multiplier_polynomial_count}")
    print(f"final_cleared_scalar_coordinate_count={final_cleared_count}")
    print("P12_omission_negative_control=true")
    print(f"FIRST_omission_negative_control_index={active}")
    print("F_omission_negative_control=true", flush=True)

    exact_lines = [
        f"v87_parent_sha256={V87_SHA256}",
        "high_q_exponents=" + ",".join(map(str, HIGH)),
        "triangular_graph_acyclic=true",
        "topological_order=" + ",".join(map(str, order)),
        f"graph_sha256={graph_sha}",
        f"remainder_sha256={remainder_sha}",
        f"multiplier_inventory_sha256={multiplier_sha}",
        f"base_remainder_sha256={m.polynomial_digest(base_remainder)}",
        f"positive_remainder_terms={len(positive)}",
        "collapse=true",
        f"h1_common={common}",
        f"K_exponent={k_exponent}",
        f"allowed_part={allowed_part}",
        f"total_target={total_target_base}",
        f"final_common={final_common}",
        f"total_multiplier_sha256={total_multiplier_sha}",
        f"total_multiplier_rows={total_multiplier_rows}",
        f"total_target_digest={v87.full_digest(total_target)}",
        f"F_multiplier_digest={v87.full_digest(f_multiplier)}",
        "claim=literal_high_q_total_F_identity",
    ]
    exact_text = "\n".join(exact_lines) + "\n"
    exact_path = outdir / "HIGH_Q_TOTAL_F_K_REPAIR_EXACT_RESULT.txt"
    exact_path.write_text(exact_text)
    exact_sha = sha256(exact_text.encode()).hexdigest()
    print(f"remainder_sha256={remainder_sha}")
    print(f"multiplier_inventory_sha256={multiplier_sha}")
    print(f"total_F_cleared_multiplier_sha256={total_multiplier_sha}")
    print(f"total_F_cleared_multiplier_rows={total_multiplier_rows}")
    print(f"exact_result_sha256={exact_sha}")
    print("literal_high_q_total_F_identity=true")
    print("high_q_P12_FIRST_only_collapse_claim=false")
    print("low_q_unit_charts_covered=false")
    print("whole_fixed_A3_killed=false")
    print("whole_TD6_killed=false")
    print("SP2_killed=false")
    print("JC2_resolved=false")
    print("TD6-V89H4-HIGH-Q-TOTAL-F-K-REPAIR PASS")
    v85.restore_base_qd_state()


if __name__ == "__main__":
    main()
