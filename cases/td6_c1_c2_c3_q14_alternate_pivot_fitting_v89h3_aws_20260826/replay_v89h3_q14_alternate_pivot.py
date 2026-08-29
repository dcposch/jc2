#!/usr/bin/env python3
"""Exact q14 one-basis-exchange and Fitting-block diagnostic."""

from hashlib import sha256
import importlib.util
import os
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
H2_PATH = HERE / "replay_v89h2_tail_q14_triangular.py"
H2_SHA256 = "6991a4e59df51d0c4d67683d317518f22b0be3e2728156cf0ec79640137d63e3"
assert sha256(H2_PATH.read_bytes()).hexdigest() == H2_SHA256
spec = importlib.util.spec_from_file_location("td6_v89h3_h2_parent", H2_PATH)
h2 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = h2
spec.loader.exec_module(h2)

QPoly = h2.QPoly
E3, m, v87, v85 = h2.E3, h2.m, h2.v87, h2.v85
F = h2.F
TAIL = h2.TAIL
SECTION_COUNT = 132


def support_graph(matrix):
    graph = {i: set() for i in range(len(matrix))}
    records = []
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            difference = value - QPoly(1 if i == j else 0)
            if not difference:
                continue
            graph[i].add(j)
            support = tuple(sorted({
                exponent
                for monomial in difference.coefficients
                for exponent in monomial
            }))
            records.append((i, j, support, h2.qpoly_digest(difference)))
    return graph, records


def strongly_connected(graph):
    counter = [0]
    index, low, stack, active, components = {}, {}, [], set(), []

    def visit(node):
        index[node] = low[node] = counter[0]
        counter[0] += 1
        stack.append(node)
        active.add(node)
        for target in sorted(graph[node]):
            if target not in index:
                visit(target)
                low[node] = min(low[node], low[target])
            elif target in active:
                low[node] = min(low[node], index[target])
        if low[node] == index[node]:
            component = []
            while True:
                target = stack.pop()
                active.remove(target)
                component.append(target)
                if target == node:
                    break
            components.append(tuple(sorted(component)))

    for node in sorted(graph):
        if node not in index:
            visit(node)
    cyclic = tuple(sorted(
        component for component in components
        if len(component) > 1
        or component[0] in graph[component[0]]
    ))
    return tuple(sorted(components)), cyclic


def graph_digest(records):
    text = "\n".join(
        f"{i}\t{j}\t{','.join(map(str, support))}\t{digest}"
        for i, j, support, digest in records
    ) + "\n"
    return sha256(text.encode()).hexdigest()


def registered_inverse(value):
    inverse = value.inverse()
    common = v85.monic(m.denominator_for([inverse]))
    allowed = (
        v85.factors_allowed(common)
        and common.gcd(F).total_degree() == 0
    )
    return inverse, common, allowed


def replacement_normalization(normalized_full, base_full, pivots, position, candidate):
    vector = [base_full[i][candidate] for i in range(38)]
    pivot_value = vector[position]
    if not pivot_value:
        return None
    inverse, common, allowed = registered_inverse(pivot_value)
    if not allowed:
        return (None, common, False)
    columns = list(pivots)
    columns[position] = candidate
    selected = [
        [normalized_full[i][column] for column in columns]
        for i in range(38)
    ]
    out = [[QPoly() for _ in range(38)] for _ in range(38)]
    for i in range(38):
        factor = (vector[i] - E3(1 if i == position else 0))*inverse
        for j in range(38):
            out[i][j] = selected[i][j] - QPoly(factor)*selected[position][j]
    assert all(
        out[i][j].constant() == E3(1 if i == j else 0)
        for i in range(38) for j in range(38)
    )
    return out, common, True


def determinant_subset(matrix):
    """Subset-DP determinant over QPoly, exact and division-free."""
    size = len(matrix)
    states = {0: QPoly(1)}
    for row in range(size):
        next_states = {}
        for mask, value in states.items():
            for column in range(size):
                if mask & (1 << column) or not matrix[row][column]:
                    continue
                greater = row - (mask & ((1 << column) - 1)).bit_count()
                term = value*matrix[row][column]
                if greater & 1:
                    term = -term
                new_mask = mask | (1 << column)
                next_states[new_mask] = next_states.get(new_mask, QPoly()) + term
        states = {mask: value for mask, value in next_states.items() if value}
    return states.get((1 << size) - 1, QPoly())


def main():
    outdir = Path(os.environ["TD6_OUTPUT_DIR"]).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    assert os.environ.get("AWS_RUN_TAG", "").startswith("td6_v89h3_q14_pivot_")
    print("producer=TD6-V89H3-Q14-ALTERNATE-PIVOT-FITTING")
    print("tail_q_exponents=" + ",".join(map(str, TAIL)))
    print("search=registered_single_constant_basis_exchange")
    print("no_q_expression_inverted=true", flush=True)

    events, bands, seen = v87.build_bands()
    total_first = v87.compile_first(bands)
    first = h2.project_first(total_first)
    assert events == 2 and len(first) == 38
    assert all(seen[exponent] == 1 for exponent in TAIL)
    print("literal_transport_FIRST_rebuilt=true", flush=True)

    pivots = h2.base_pivot_columns(first)
    assert len(pivots) == 38 and len(set(pivots)) == 38
    all_columns = tuple(range(SECTION_COUNT))
    A0_full = [
        [row.get(column, QPoly()).constant() for column in all_columns]
        for _, row, _ in first
    ]
    A_full = [
        [row.get(column, QPoly()) for column in all_columns]
        for _, row, _ in first
    ]
    A0 = [[row[column] for column in pivots] for row in A0_full]
    inverse_A0 = h2.inverse_constant_matrix(A0)
    base_full = h2.matmul_constant(inverse_A0, A0_full)
    normalized_full = h2.matmul_constant_q(inverse_A0, A_full)
    current = [[normalized_full[i][column] for column in pivots] for i in range(38)]
    current_graph, current_records = support_graph(current)
    components, cyclic = strongly_connected(current_graph)
    assert cyclic == ((0, 1, 2, 3, 4, 5, 6, 13),)
    print("current_cyclic_scc=0,1,2,3,4,5,6,13", flush=True)

    q14_self = current[0][0] - QPoly(1)
    assert set(q14_self.coefficients) == {(14,)}
    q14_self_coefficient = q14_self.coefficients[(14,)]
    print("q14_self_loop_coefficient_exact=" + m.e3_exact(q14_self_coefficient))

    block = cyclic[0]
    q14 = QPoly.variable(14)
    q14_block = []
    for i in block:
        row = []
        for j in block:
            coefficient = (current[i][j] - QPoly(1 if i == j else 0)).coefficients.get(
                (14,), E3()
            )
            row.append(QPoly(1 if i == j else 0) + q14*QPoly(coefficient))
        q14_block.append(row)
    determinant = determinant_subset(q14_block)
    assert determinant.constant() == E3(1)
    determinant_lines = ["q14_degree\tcoefficient_exact"]
    for monomial, coefficient in sorted(determinant.coefficients.items()):
        assert all(exponent == 14 for exponent in monomial)
        determinant_lines.append(f"{len(monomial)}\t{m.e3_exact(coefficient)}")
    determinant_text = "\n".join(determinant_lines) + "\n"
    determinant_path = outdir / "Q14_PIVOT_BLOCK_DETERMINANT.tsv"
    determinant_path.write_text(determinant_text)
    determinant_sha = sha256(determinant_text.encode()).hexdigest()
    print(f"q14_pivot_block_determinant_degree={max(map(len, determinant.coefficients))}")
    print(f"q14_pivot_block_determinant_sha256={determinant_sha}", flush=True)

    nonpivots = tuple(column for column in all_columns if column not in pivots)
    candidate_lines = [
        "swap_position\told_column\tnew_column\tregistered\tcommon"
        "\tcyclic_nodes\tself_loops\tedges\tgraph_sha256\tcyclic_sccs"
    ]
    best = None
    invertible = registered = 0
    found = None
    for position in range(38):
        for candidate in nonpivots:
            result = replacement_normalization(
                normalized_full, base_full, pivots, position, candidate
            )
            if result is None:
                continue
            invertible += 1
            matrix, common, allowed = result
            if not allowed:
                candidate_lines.append(
                    f"{position}\t{pivots[position]}\t{candidate}\tfalse\t"
                    f"{common}\tNA\tNA\tNA\tNA\tNA"
                )
                continue
            registered += 1
            graph, records = support_graph(matrix)
            _, candidate_cyclic = strongly_connected(graph)
            cyclic_nodes = sum(map(len, candidate_cyclic))
            self_loops = sum(node in graph[node] for node in graph)
            edges = sum(map(len, graph.values()))
            digest = graph_digest(records)
            score = (cyclic_nodes, self_loops, edges, position, candidate)
            scc_text = ";".join(
                ",".join(map(str, component)) for component in candidate_cyclic
            ) or "NONE"
            candidate_lines.append(
                f"{position}\t{pivots[position]}\t{candidate}\ttrue\t"
                f"{common}\t{cyclic_nodes}\t{self_loops}\t{edges}\t"
                f"{digest}\t{scc_text}"
            )
            if best is None or score < best[0]:
                best = (score, position, candidate, common, digest, scc_text)
                print(
                    "new_best_single_swap="
                    f"position:{position};old:{pivots[position]};new:{candidate};"
                    f"cyclic_nodes:{cyclic_nodes};self_loops:{self_loops};"
                    f"edges:{edges};graph:{digest}",
                    flush=True,
                )
            if not candidate_cyclic:
                found = best
                break
        if found is not None:
            break

    candidate_text = "\n".join(candidate_lines) + "\n"
    candidate_path = outdir / "Q14_SINGLE_BASIS_EXCHANGE.tsv"
    candidate_path.write_text(candidate_text)
    candidate_sha = sha256(candidate_text.encode()).hexdigest()
    assert best is not None
    score, position, candidate, common, digest, scc_text = best
    print(f"invertible_single_exchanges={invertible}")
    print(f"registered_single_exchanges={registered}")
    print(f"best_swap_position={position}")
    print(f"best_swap_old_column={pivots[position]}")
    print(f"best_swap_new_column={candidate}")
    print(f"best_swap_cyclic_nodes={score[0]}")
    print(f"best_swap_self_loops={score[1]}")
    print(f"best_swap_edges={score[2]}")
    print(f"best_swap_graph_sha256={digest}")
    print(f"best_swap_cyclic_sccs={scc_text}")
    print(f"candidate_inventory_sha256={candidate_sha}")

    audited_coefficients = list(determinant.coefficients.values())
    audited_coefficients.append(q14_self_coefficient)
    denominator = v85.monic(m.denominator_for(audited_coefficients))
    assert v85.factors_allowed(denominator), denominator.factor()
    assert denominator.gcd(F).total_degree() == 0
    print(f"diagnostic_common_denominator={denominator}")
    print(f"diagnostic_common_denominator_factor={denominator.factor()}")
    print("denominator_radical_subset_U_H_B3=true")
    print("F_not_inverted=true")
    print("q_not_inverted=true")

    found_text = str(found is not None).lower()
    exact_lines = [
        f"h2_parent_sha256={H2_SHA256}",
        "tail_q_exponents=" + ",".join(map(str, TAIL)),
        "current_cyclic_scc=0,1,2,3,4,5,6,13",
        f"current_graph_sha256={graph_digest(current_records)}",
        f"q14_self_loop_sha256={h2.qpoly_digest(q14_self)}",
        f"q14_determinant_sha256={determinant_sha}",
        f"invertible_single_exchanges={invertible}",
        f"registered_single_exchanges={registered}",
        f"registered_acyclic_single_exchange_found={found_text}",
        f"best_swap={position},{pivots[position]},{candidate}",
        f"best_score={score[0]},{score[1]},{score[2]}",
        f"best_graph_sha256={digest}",
        f"candidate_inventory_sha256={candidate_sha}",
        f"common={denominator}",
        "claim=alternate_pivot_fitting_diagnostic_only",
    ]
    exact_text = "\n".join(exact_lines) + "\n"
    exact_path = outdir / "Q14_ALTERNATE_PIVOT_EXACT_RESULT.txt"
    exact_path.write_text(exact_text)
    exact_sha = sha256(exact_text.encode()).hexdigest()
    print(f"exact_result_sha256={exact_sha}")
    print(f"registered_acyclic_single_exchange_found={found_text}")
    print("P12_reduction_performed=false")
    print("radical_membership_claim=false")
    print("source_point_claim=false")
    print("whole_TD6_killed=false")
    print("JC2_resolved=false")
    print("TD6-V89H3-Q14-ALTERNATE-PIVOT-FITTING DIAGNOSTIC-PASS")
    v85.restore_base_qd_state()


if __name__ == "__main__":
    main()
