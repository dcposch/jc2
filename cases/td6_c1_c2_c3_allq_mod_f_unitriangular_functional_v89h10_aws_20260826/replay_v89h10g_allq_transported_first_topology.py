#!/usr/bin/env python3
"""Exact topology and point-determinant gate for full-q transported FIRST."""

from hashlib import sha256
import importlib.util
import os
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
PARENT_PATH = HERE / "replay_v89h10_allq_mod_f_unitriangular_functional_v1.py"
PARENT_SHA256 = "4ff99ca9b7d8539aa369b65a953da63dc731d12ba3faf4184678fe8d0b6b9524"
assert sha256(PARENT_PATH.read_bytes()).hexdigest() == PARENT_SHA256
spec = importlib.util.spec_from_file_location("td6_v89h10g_parent", PARENT_PATH)
p = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = p
spec.loader.exec_module(p)

h5, h6, v87, v85, m = p.h5, p.h6, p.v87, p.v85, p.m
QPoly, E3 = p.QPoly, p.E3
LOW = tuple(range(2, 15))
HIGH = tuple(range(16, 25))


def evaluate(value, assignment):
    out = E3()
    for monomial, coefficient in QPoly.coerce(value).coefficients.items():
        scalar = 1
        for exponent in monomial:
            scalar *= assignment.get(exponent, 0)
        if scalar:
            out += coefficient*scalar
    return out


def determinant(matrix):
    """Exact Gaussian determinant over E3."""
    work = [list(row) for row in matrix]
    size = len(work)
    out = E3(1)
    for column in range(size):
        pivot_row = next(
            (row for row in range(column, size) if work[row][column]), None
        )
        if pivot_row is None:
            return E3()
        if pivot_row != column:
            work[column], work[pivot_row] = work[pivot_row], work[column]
            out = -out
        pivot = work[column][column]
        out *= pivot
        inverse = pivot.inverse()
        for row in range(column + 1, size):
            if not work[row][column]:
                continue
            factor = work[row][column]*inverse
            for target in range(column + 1, size):
                work[row][target] -= factor*work[column][target]
            work[row][column] = E3()
    return out


def graph_for(N, exponents):
    exponents = set(exponents)
    graph = {row: set() for row in range(len(N))}
    for row, values in enumerate(N):
        for column, value in enumerate(values):
            if any(
                monomial and monomial[0] in exponents
                for monomial in value.coefficients
            ):
                graph[row].add(column)
    return graph


def determinant_by_scc(B, graph, assignment):
    components, cyclic = h5.strongly_connected(graph)
    value = E3(1)
    for component in components:
        block = [
            [evaluate(B[row][column], assignment) for column in component]
            for row in component
        ]
        value *= determinant(block)
    return value, components, cyclic


def main():
    outdir = Path(os.environ["TD6_OUTPUT_DIR"]).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    assert os.environ.get("AWS_RUN_TAG", "").startswith(
        "td6_v89h10g_allq_transported_first_topology_"
    )
    print("producer=TD6-V89H10G-ALLQ-TRANSPORTED-FIRST-TOPOLOGY")
    print(f"parent_sha256={PARENT_SHA256}")
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
    N = [
        [B[i][j] - identity[i][j] for j in range(38)]
        for i in range(38)
    ]
    n_sha, n_entries, n_terms, n_degree = p.matrix_stats(N)
    assert n_degree <= 1
    print(f"N_sha256={n_sha}")
    print(f"N_nonzero_entries={n_entries}")
    print(f"N_q_terms={n_terms}")
    print(f"N_max_total_q_degree={n_degree}", flush=True)

    lines = ["row\tcolumn\tq_exponent\tcoefficient_exact"]
    for row, values in enumerate(N):
        for column, value in enumerate(values):
            for monomial, coefficient in sorted(value.coefficients.items()):
                assert len(monomial) == 1
                lines.append(
                    f"{row}\t{column}\t{monomial[0]}\t{m.e3_exact(coefficient)}"
                )
    edge_text = "\n".join(lines) + "\n"
    (outdir / "ALLQ_AFFINE_N_EDGES.tsv").write_text(edge_text)
    edge_sha = sha256(edge_text.encode()).hexdigest()
    print(f"affine_N_edges_sha256={edge_sha}")

    scopes = (("full", p.ALLOWED_Q), ("low", LOW), ("high", HIGH))
    graphs = {}
    records = ["scope\tcomponents\tcyclic_components\tedges\tmax_scc_size"]
    for name, exponents in scopes:
        graph = graph_for(N, exponents)
        components, cyclic = h5.strongly_connected(graph)
        graphs[name] = graph
        edge_count = sum(map(len, graph.values()))
        max_size = max(map(len, components))
        records.append(
            f"{name}\t{components!r}\t{cyclic!r}\t{edge_count}\t{max_size}"
        )
        print(f"{name}_graph_edges={edge_count}")
        print(f"{name}_components={components!r}")
        print(f"{name}_cyclic_components={cyclic!r}")
        print(f"{name}_max_scc_size={max_size}", flush=True)
    topology_text = "\n".join(records) + "\n"
    (outdir / "ALLQ_PIVOT_TOPOLOGY.tsv").write_text(topology_text)
    topology_sha = sha256(topology_text.encode()).hexdigest()
    print(f"pivot_topology_sha256={topology_sha}")

    assignments = (
        ("low_one", {exponent: 1 for exponent in LOW}, "low"),
        ("all_one", {exponent: 1 for exponent in p.ALLOWED_Q}, "full"),
        (
            "all_sign",
            {exponent: (-1 if exponent & 1 else 1) for exponent in p.ALLOWED_Q},
            "full",
        ),
    )
    determinant_lines = ["assignment\tdeterminant_exact\tequals_one"]
    any_obstruction = False
    for name, assignment, scope in assignments:
        value, components, cyclic = determinant_by_scc(
            B, graphs[scope], assignment
        )
        exact = m.e3_exact(value)
        equals_one = value == E3(1)
        any_obstruction = any_obstruction or not equals_one
        determinant_lines.append(f"{name}\t{exact}\t{str(equals_one).lower()}")
        print(f"{name}_determinant_exact={exact}")
        print(f"{name}_determinant_equals_one={str(equals_one).lower()}", flush=True)
    determinant_text = "\n".join(determinant_lines) + "\n"
    (outdir / "ALLQ_POINT_DETERMINANTS.tsv").write_text(determinant_text)
    determinant_sha = sha256(determinant_text.encode()).hexdigest()
    print(f"point_determinants_sha256={determinant_sha}")
    print(f"registered_pivot_unimodularity_obstructed={str(any_obstruction).lower()}")
    print("finite_point_equalities_are_not_polynomial_proof=true")
    print("P12_functional_claim=false")
    print("TD6-V89H10G-ALLQ-TRANSPORTED-FIRST-TOPOLOGY PASS")
    v85.restore_base_qd_state()


if __name__ == "__main__":
    main()
