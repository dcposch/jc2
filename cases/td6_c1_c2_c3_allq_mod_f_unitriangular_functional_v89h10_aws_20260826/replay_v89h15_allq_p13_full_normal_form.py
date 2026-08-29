#!/usr/bin/env python3
"""Exact all-q literal-P13 normal form via the reviewed FIRST flag."""

from hashlib import sha256
import importlib.util
import os
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
H12_PATH = HERE / "replay_v89h12_allq_p12_full_normal_form.py"
H12_SHA = "1e277481267a78472737e9d5082433e41d0218fd1ea6b0a1f92fcc0df9592bed"
H12_RESULT = HERE / "P12_FULL_NORMAL_FORM_RESULT.md"
H12_RESULT_SHA = "7004c6359eba808c6f5f66ddd0b72c917fc734c1c3a6eea67878d19859ba23ef"
H12_FREEZE = HERE / "P12_FULL_NORMAL_FORM_FREEZE.sha256"
H12_FREEZE_SHA = "c7a146ee89ced521cb23544be6a977413c003b17d0a256a26eda6dae9d435a11"
for path, expected in (
    (H12_PATH, H12_SHA), (H12_RESULT, H12_RESULT_SHA), (H12_FREEZE, H12_FREEZE_SHA)
):
    assert sha256(path.read_bytes()).hexdigest() == expected

spec = importlib.util.spec_from_file_location("td6_v89h15_h12_parent", H12_PATH)
h12 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = h12
spec.loader.exec_module(h12)

h11, h5, h6, v87, v85, m, t = h12.h11, h12.h5, h12.h6, h12.v87, h12.v85, h12.m, h12.t
QPoly, E3 = h12.QPoly, h12.E3
U, V, F, H, B3 = h12.U, h12.V, h12.F, h12.H, h12.B3
ALL_Q = h12.ALL_Q
EXPECTED_N_SHA256 = h12.EXPECTED_N_SHA256
EXPECTED_AFFINE_SHA = "cc31df859f8142c00ed7da8858f9c1d4f8a19bc4a0cfe1ee27511a245987bb27"


def compile_current_degree(bands, degree):
    """Literal one-degree extraction of the frozen generic x-current compiler."""
    v87.configure_qd(None)
    qd, nr = m.r.qd, m.r.qd.nr
    f1, f2, f3 = (bands[("f", power)] for power in (1, 2, 3))
    g1, g2, g3 = (bands[("g", power)] for power in (1, 2, 3))
    equation = {}
    for i, left in enumerate(f1):
        j = degree - i + 1
        if 1 <= j < len(g2):
            equation = nr.add_polynomial(
                equation, nr.multiply_affine(left, nr.scale_affine(g2[j], j))
            )
    for i, left in enumerate(f2):
        j = degree - i + 1
        if 1 <= j < len(g1):
            equation = nr.add_polynomial(
                equation,
                nr.multiply_affine(left, nr.scale_affine(g1[j], j)),
                2,
            )
    for i, form in enumerate(f3):
        multiplier = qd.Q_PRIME.get(degree - i, QPoly())
        if multiplier:
            equation = nr.add_polynomial(
                equation, nr.affine_polynomial(form), 3 * multiplier
            )
    g_degree = degree - 14
    if 0 <= g_degree < len(g3):
        equation = nr.add_polynomial(
            equation, nr.affine_polynomial(g3[g_degree]), -45
        )
    for i in range(1, len(f1)):
        j = degree - (i - 1)
        if 0 <= j < len(g2):
            equation = nr.add_polynomial(
                equation,
                nr.multiply_affine(nr.scale_affine(f1[i], i), g2[j]),
                -2,
            )
    for i in range(1, len(f2)):
        j = degree - (i - 1)
        if 0 <= j < len(g1):
            equation = nr.add_polynomial(
                equation,
                nr.multiply_affine(nr.scale_affine(f2[i], i), g1[j]),
                -1,
            )
    return v87.clean({
        monomial: QPoly.coerce(value) for monomial, value in equation.items()
    })


def affine_substitute(polynomial, images):
    out = {}
    first_nonzero = None
    for scanned, (monomial, coefficient) in enumerate(sorted(polynomial.items()), 1):
        contribution = {(): QPoly.coerce(coefficient)}
        for variable in monomial:
            contribution = v87.multiply(contribution, images[variable])
        if contribution:
            if first_nonzero is None:
                first_nonzero = contribution
            out = v87.add(out, contribution)
        if scanned % 100 == 0:
            print(
                f"literal_P13_terms_scanned={scanned};"
                f"normal_form_parameter_terms={len(out)};"
                f"normal_form_q_terms={v87.coefficient_term_count(out)}",
                flush=True,
            )
    assert scanned == len(polynomial) and first_nonzero
    omitted = v87.add(out, first_nonzero, -1)
    assert omitted != out
    return v87.clean(out), scanned


def coordinate_support(polynomial):
    parameter_coordinates, empty_coordinates = set(), set()
    for parameter_monomial, value in polynomial.items():
        target = parameter_coordinates if parameter_monomial else empty_coordinates
        for coefficient in value.coefficients.values():
            target.update(
                index
                for index, entry in enumerate(m.r.scalar_coordinates(coefficient))
                if entry
            )
    return tuple(sorted(parameter_coordinates)), tuple(sorted(empty_coordinates))


def main():
    outdir = Path(os.environ["TD6_OUTPUT_DIR"]).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    assert os.environ.get("AWS_RUN_TAG", "").startswith("td6_v89h15_allq_p13_")
    print("producer=TD6-V89H15-ALLQ-P13-FULL-NORMAL-FORM")
    print(f"h12_client_sha256={H12_SHA}")
    print(f"h12_result_sha256={H12_RESULT_SHA}")
    print(f"h12_freeze_sha256={H12_FREEZE_SHA}")
    print("retained_q_exponents=" + ",".join(map(str, ALL_Q)))
    print("q15_absent_target_shear=true", flush=True)

    events, bands, seen = v87.build_bands()
    first = v87.compile_first(bands)
    p13 = compile_current_degree(bands, 13)
    assert events == 2 and len(first) == 38
    assert set(seen) == set(ALL_Q) and all(seen[e] == 1 for e in ALL_Q)
    sources = [v87.source_polynomial(row, rhs) for _, row, rhs in first]
    assert all(all(len(monomial) <= 1 for monomial in source) for source in sources)
    assert max(map(len, p13), default=0) <= 2
    _, raw_common = v87.assert_denominators_allowed([p13, *sources])
    assert raw_common == U * H and raw_common.gcd(F).total_degree() == 0
    print("literal_transport_FIRST_P13_rebuilt=true")
    print(f"literal_P13_parameter_terms={len(p13)}")
    print("literal_P13_parameter_degree_at_most_two=true")
    print(f"raw_source_common_denominator=({raw_common})")
    print("raw_source_denominator_coprime_F=true", flush=True)

    specialized_first = h6.specialize_first(first)
    specialized_p13 = h6.specialize_polynomial(p13)
    pivots = h5.base_pivot_columns(specialized_first)
    pivot_set = set(pivots)
    all_variables = set(range(132))
    for _, row, _ in specialized_first:
        assert set(row) <= all_variables
    for monomial in specialized_p13:
        assert set(monomial) <= all_variables
    free_variables = tuple(sorted(all_variables - pivot_set))
    assert len(pivots) == len(pivot_set) == 38 and len(free_variables) == 94
    print("pivot_variables=" + ",".join(map(str, pivots)))
    print("free_variables=" + ",".join(map(str, free_variables)))
    print("complete_free_variable_inventory_count=94", flush=True)

    A0 = [[row.get(pivot, QPoly()).constant() for pivot in pivots] for _, row, _ in specialized_first]
    A = [[row.get(pivot, QPoly()) for pivot in pivots] for _, row, _ in specialized_first]
    D = [[row.get(variable, QPoly()) for variable in free_variables] for _, row, _ in specialized_first]
    rhs = [rhs for _, _, rhs in specialized_first]
    inverse_A0 = h5.inverse_constant_matrix(A0)
    B = h5.matmul_constant_q(inverse_A0, A)
    identity_q = h11.p.identity_matrix(38)
    N = [[B[i][j] - identity_q[i][j] for j in range(38)] for i in range(38)]
    n_sha, n_entries, n_terms, n_degree = h11.p.matrix_stats(N)
    assert n_sha == EXPECTED_N_SHA256 and (n_entries, n_terms, n_degree) == (532, 6069, 1)

    S_full, inverse_S_full, order, upper_N = h11.reconstruct_flag(N, outdir)
    W = [[S_full[i][order[j]] for j in range(38)] for i in range(38)]
    inverse_W = [[inverse_S_full[order[i]][j] for j in range(38)] for i in range(38)]
    assert h5.matmul_constant(W, inverse_W) == h11.identity_constant(38)
    assert h5.matmul_constant(inverse_W, W) == h11.identity_constant(38)

    def solve_original(right_side, label):
        base = h12.matvec_constant_q(inverse_A0, right_side)
        triangular = h12.matvec_constant_q(inverse_W, base)
        solution = h12.solve_upper_labeled(upper_N, triangular, label)
        return h12.matvec_constant_q(W, solution)

    constant_solution = solve_original(rhs, "constant")
    assert h12.matvec_q(A, constant_solution) == rhs
    direction_solutions = []
    for column, variable in enumerate(free_variables):
        solution = solve_original([-D[row][column] for row in range(38)], f"free_{variable}")
        replay = h12.matvec_q(A, solution)
        assert all(replay[row] + D[row][column] == QPoly() for row in range(38))
        direction_solutions.append(solution)
    print("all_free_directions_original_FIRST_replay=true", flush=True)

    affine_sha, affine_rows = h12.write_affine_pivot_map(
        outdir / "P13_AFFINE_PIVOT_MAP.tsv", pivots, free_variables,
        constant_solution, direction_solutions,
    )
    assert affine_sha == EXPECTED_AFFINE_SHA
    print(f"affine_pivot_map_sha256={affine_sha};rows={affine_rows}")
    print("affine_pivot_map_equals_frozen_H12=true", flush=True)

    pivot_position = {variable: index for index, variable in enumerate(pivots)}
    free_position = {variable: index for index, variable in enumerate(free_variables)}
    images = {}
    for variable in all_variables:
        if variable in free_position:
            images[variable] = {(variable,): QPoly(1)}
            continue
        position = pivot_position[variable]
        image = {(): constant_solution[position]} if constant_solution[position] else {}
        for free_index, free_variable in enumerate(free_variables):
            value = direction_solutions[free_index][position]
            if value:
                image[(free_variable,)] = value
        images[variable] = v87.clean(image)

    normal_form, scanned = affine_substitute(specialized_p13, images)
    assert scanned == len(specialized_p13)
    assert all(set(monomial) <= set(free_variables) for monomial in normal_form)
    parameter_degree = max(map(len, normal_form), default=0)
    normal_form_sha = h12.write_polynomial(
        outdir / "ALLQ_P13_FULL_NORMAL_FORM.tsv", normal_form
    )
    q_support = sorted({
        q_monomial for value in normal_form.values()
        for q_monomial in value.coefficients
    })
    max_q_degree = max(map(len, q_support), default=0)
    mixed_q = sum(len(set(monomial)) > 1 for monomial in q_support)
    parameter_support = tuple(sorted(normal_form))
    parameter_coordinates, empty_coordinates = coordinate_support(normal_form)
    support_text = (
        "key\tvalue\n"
        f"parameter_support\t{parameter_support!r}\n"
        f"q_support\t{tuple(q_support)!r}\n"
        f"parameter_coordinate_support\t{parameter_coordinates!r}\n"
        f"empty_coordinate_support\t{empty_coordinates!r}\n"
    )
    (outdir / "ALLQ_P13_SUPPORT.tsv").write_text(support_text)
    support_sha = sha256(support_text.encode()).hexdigest()
    print(f"full_normal_form_sha256={normal_form_sha}")
    print(f"full_normal_form_parameter_terms={len(normal_form)}")
    print(f"full_normal_form_coefficient_terms={v87.coefficient_term_count(normal_form)}")
    print(f"full_normal_form_parameter_degree={parameter_degree}")
    print(f"full_normal_form_q_support_count={len(q_support)}")
    print(f"full_normal_form_mixed_q_support_count={mixed_q}")
    print(f"full_normal_form_max_total_q_degree={max_q_degree}")
    print(f"support_sha256={support_sha}", flush=True)

    denominator_records = [
        t.denominator_record("affine_pivot_map", (
            coefficient for solution in [constant_solution, *direction_solutions]
            for value in solution for coefficient in value.coefficients.values()
        )),
        t.denominator_record("full_P13_normal_form", (
            coefficient for value in normal_form.values()
            for coefficient in value.coefficients.values()
        )),
    ]
    denominator_text = "label\tvalue_count\tallowed\tcommon\tfactorization\n" + "\n".join(
        f"{label}\t{count}\t{str(allowed).lower()}\t{common}\t{factorization}"
        for label, count, common, factorization, allowed in denominator_records
    ) + "\n"
    (outdir / "ALLQ_P13_DENOMINATORS.tsv").write_text(denominator_text)
    denominator_sha = sha256(denominator_text.encode()).hexdigest()
    denominators_allowed = all(record[-1] for record in denominator_records)
    print(f"denominator_ledger_sha256={denominator_sha}")
    print(f"denominators_registered={str(denominators_allowed).lower()}")

    result = (
        f"h12_result_sha256={H12_RESULT_SHA}\n"
        f"h12_freeze_sha256={H12_FREEZE_SHA}\n"
        f"literal_P13_parameter_terms={len(p13)}\n"
        f"affine_pivot_map_sha256={affine_sha}\n"
        f"full_normal_form_sha256={normal_form_sha}\n"
        f"full_normal_form_parameter_terms={len(normal_form)}\n"
        f"full_normal_form_coefficient_terms={v87.coefficient_term_count(normal_form)}\n"
        f"full_normal_form_parameter_degree={parameter_degree}\n"
        f"full_normal_form_max_total_q_degree={max_q_degree}\n"
        f"support_sha256={support_sha}\n"
        f"denominator_ledger_sha256={denominator_sha}\n"
        "all_22_q_independent_untruncated=true\n"
        "all_free_directions_original_FIRST_replay=true\n"
        "affine_pivot_map_equals_frozen_H12=true\n"
        "literal_P13_omission_negative_control=true\n"
        f"denominators_registered={str(denominators_allowed).lower()}\n"
        "P12_P13_combined_exclusion_claim=false\nsource_point_claim=false\n"
        "whole_TD6_killed=false\nJC2_resolved=false\n"
    )
    (outdir / "ALLQ_P13_FULL_NORMAL_FORM_RESULT.txt").write_text(result)
    print(f"result_sha256={sha256(result.encode()).hexdigest()}")
    if denominators_allowed:
        print("TD6-V89H15-ALLQ-P13-FULL-NORMAL-FORM PASS")
    else:
        print("TD6-V89H15-ALLQ-P13-FULL-NORMAL-FORM DENOMINATOR-FAIL-CLOSED")
    v85.restore_base_qd_state()


if __name__ == "__main__":
    main()
