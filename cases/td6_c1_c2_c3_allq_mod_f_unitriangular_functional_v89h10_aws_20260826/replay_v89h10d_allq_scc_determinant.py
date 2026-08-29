#!/usr/bin/env python3
"""Exact full-q determinant of the unique 14-node transported-FIRST SCC."""

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
spec = importlib.util.spec_from_file_location("td6_v89h10d_parent", PARENT_PATH)
p = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = p
spec.loader.exec_module(p)

h5, h6, v87, v85, m = p.h5, p.h6, p.v87, p.v85, p.m
QPoly, E3 = p.QPoly, p.E3
SCC = tuple(range(14))
EXPECTED_N_SHA256 = "38fb14e38daa36d597cc7ae1cd2bd5dd402ef2cd1587337321b8c204eeeb7f36"
EXPECTED_COMPONENTS = (SCC,) + tuple((index,) for index in range(14, 38))


def qpoly_stats(value):
    value = QPoly.coerce(value)
    terms = len(value.coefficients)
    degree = max(map(len, value.coefficients), default=0)
    digest = h5.qpoly_digest(value)
    return digest, terms, degree


def write_qpoly(path, value):
    lines = ["q_monomial\tcoefficient_exact"]
    for monomial, coefficient in sorted(QPoly.coerce(value).coefficients.items()):
        lines.append(f"{monomial!r}\t{m.e3_exact(coefficient)}")
    text = "\n".join(lines) + "\n"
    path.write_text(text)
    return sha256(text.encode()).hexdigest()


def determinant_subset_progress(matrix, outdir):
    size = len(matrix)
    states = {0: QPoly(1)}
    telemetry = ["row\tnonzero_states\ttotal_q_terms\tmax_total_q_degree"]
    for row in range(size):
        next_states = {}
        for mask, value in states.items():
            for column in range(size):
                entry = matrix[row][column]
                if mask & (1 << column) or not entry:
                    continue
                greater = row - (mask & ((1 << column) - 1)).bit_count()
                term = value*entry
                if greater & 1:
                    term = -term
                new_mask = mask | (1 << column)
                next_states[new_mask] = next_states.get(new_mask, QPoly()) + term
        states = {mask: value for mask, value in next_states.items() if value}
        terms = sum(len(value.coefficients) for value in states.values())
        degree = max(
            (
                len(monomial)
                for value in states.values()
                for monomial in value.coefficients
            ),
            default=0,
        )
        telemetry.append(f"{row + 1}\t{len(states)}\t{terms}\t{degree}")
        print(
            f"determinant_DP_row={row + 1}/{size};states={len(states)};"
            f"q_terms={terms};max_q_degree={degree}",
            flush=True,
        )
    text = "\n".join(telemetry) + "\n"
    (outdir / "ALLQ_SCC_DETERMINANT_DP_TELEMETRY.tsv").write_text(text)
    return states.get((1 << size) - 1, QPoly()), sha256(text.encode()).hexdigest()


def main():
    outdir = Path(os.environ["TD6_OUTPUT_DIR"]).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    assert os.environ.get("AWS_RUN_TAG", "").startswith(
        "td6_v89h10d_allq_scc_determinant_"
    )
    print("producer=TD6-V89H10D-ALLQ-SCC-DETERMINANT")
    print(f"parent_sha256={PARENT_SHA256}")
    print(f"graph_result_sha256={GRAPH_RESULT_SHA256}")
    print(f"graph_freeze_sha256={GRAPH_FREEZE_SHA256}")
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
    assert n_sha == EXPECTED_N_SHA256
    assert (n_entries, n_terms, n_degree) == (532, 6069, 1)
    graph = {i: {j for j in range(38) if N[i][j]} for i in range(38)}
    components, cyclic = h5.strongly_connected(graph)
    assert components == EXPECTED_COMPONENTS
    assert cyclic == (SCC,)
    print(f"N_sha256={n_sha}")
    print(f"unique_cyclic_SCC={SCC!r}", flush=True)

    trace = QPoly()
    for index in range(38):
        trace += N[index][index]
    trace_sha, trace_terms, trace_degree = qpoly_stats(trace)
    trace_artifact_sha = write_qpoly(outdir / "ALLQ_N_TRACE.tsv", trace)
    print(f"N_trace_sha256={trace_sha}")
    print(f"N_trace_artifact_sha256={trace_artifact_sha}")
    print(f"N_trace_terms={trace_terms}")
    print(f"N_trace_max_q_degree={trace_degree}")
    print(f"N_trace_zero={str(not trace).lower()}")
    print(f"finite_Neumann_route_rejected={str(bool(trace)).lower()}", flush=True)

    block = [[B[i][j] for j in SCC] for i in SCC]
    determinant, telemetry_sha = determinant_subset_progress(block, outdir)
    determinant_sha, determinant_terms, determinant_degree = qpoly_stats(determinant)
    determinant_artifact_sha = write_qpoly(
        outdir / "ALLQ_SCC_DETERMINANT.tsv", determinant
    )
    unit = determinant == QPoly(1)
    print(f"determinant_DP_telemetry_sha256={telemetry_sha}")
    print(f"SCC_determinant_sha256={determinant_sha}")
    print(f"SCC_determinant_artifact_sha256={determinant_artifact_sha}")
    print(f"SCC_determinant_terms={determinant_terms}")
    print(f"SCC_determinant_max_q_degree={determinant_degree}")
    print(f"SCC_determinant_equals_one={str(unit).lower()}")
    print(f"full_registered_pivot_unimodular={str(unit).lower()}")
    print("adjugate_emitted=false")
    print("P12_functional_claim=false")
    if unit:
        print("TD6-V89H10D-ALLQ-SCC-DETERMINANT PASS")
    else:
        print("TD6-V89H10D-ALLQ-SCC-DETERMINANT NONUNIT-PASS")
    v85.restore_base_qd_state()


if __name__ == "__main__":
    main()
