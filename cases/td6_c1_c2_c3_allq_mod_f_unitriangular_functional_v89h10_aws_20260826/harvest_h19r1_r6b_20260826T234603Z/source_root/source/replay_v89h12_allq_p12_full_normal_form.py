#!/usr/bin/env python3
"""Exact all-q full P12 normal form via the V89H10T triangular flag."""

from hashlib import sha256
import importlib.util
import os
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
H11_PATH = HERE / "replay_v89h11_allq_p12_flag_functional.py"
H11_SHA256 = "8b87985d2071c40b295e280fce94a6465826dd06478089adca34e70df123fcba"
H11_RESULT_PATH = HERE / "P12_FLAG_RESULT.md"
H11_RESULT_SHA256 = "1e418dfeaf600def4cbfaae885b860b5303faa90a2fdaea59fc4003a137fa2a2"
H11_FREEZE_PATH = HERE / "P12_FLAG_FREEZE.sha256"
H11_FREEZE_SHA256 = "f4a314481c0de486843b55b2f3fd6d433534e6cfc6c137b242df363f0a784a0d"
for path, expected in (
    (H11_PATH, H11_SHA256),
    (H11_RESULT_PATH, H11_RESULT_SHA256),
    (H11_FREEZE_PATH, H11_FREEZE_SHA256),
):
    assert sha256(path.read_bytes()).hexdigest() == expected

spec = importlib.util.spec_from_file_location("td6_v89h12_h11_parent", H11_PATH)
h11 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = h11
spec.loader.exec_module(h11)

t, h5, h6, v87, v85, m = h11.t, h11.h5, h11.h6, h11.v87, h11.v85, h11.m
QPoly, E3 = h11.QPoly, h11.E3
U, V, F, H, B3 = h11.U, h11.V, h11.F, h11.H, h11.B3
ALL_Q = h11.ALL_Q
EXPECTED_N_SHA256 = h11.EXPECTED_N_SHA256
EXPECTED_EMPTY_SHA256 = (
    "530d3c78df4d1dd43a892976aede83bcc6aefd697a40be71a195e83cbc15a7f8"
)
EXPECTED_Q14_CLASS_SHA256 = (
    "56ebf08a3f9814f714920a4fcb3ae7fb0957db0c0f6d231382f9b5efbf3321a2"
)


def qpoly_stats(values):
    return h11.qpoly_stats(values)


def matvec_constant_q(matrix, vector):
    return h11.matvec_constant_q(matrix, vector)


def matvec_q(matrix, vector):
    return h11.matvec_q(matrix, vector)


def solve_upper_labeled(upper_N, rhs, label):
    solution = [QPoly() for _ in rhs]
    for row in range(len(rhs) - 1, -1, -1):
        value = rhs[row]
        for column in range(row + 1, len(rhs)):
            if upper_N[row][column] and solution[column]:
                value -= upper_N[row][column]*solution[column]
        solution[row] = value
    unit_upper = [
        [upper_N[i][j] + QPoly(1 if i == j else 0) for j in range(len(rhs))]
        for i in range(len(rhs))
    ]
    assert matvec_q(unit_upper, solution) == rhs
    _, nonzero, terms, degree = qpoly_stats(solution)
    print(
        f"triangular_solve={label};nonzero={nonzero};q_terms={terms};"
        f"max_q_degree={degree}",
        flush=True,
    )
    return solution


def write_affine_pivot_map(path, pivots, free_variables, constant, directions):
    lines = ["pivot_position\tpivot_variable\tparameter_monomial\tq_monomial\tcoefficient_exact"]
    for position, pivot in enumerate(pivots):
        pieces = [((), constant[position])] + [
            ((variable,), directions[index][position])
            for index, variable in enumerate(free_variables)
        ]
        for parameter_monomial, value in pieces:
            for q_monomial, coefficient in sorted(value.coefficients.items()):
                lines.append(
                    f"{position}\t{pivot}\t{parameter_monomial!r}\t"
                    f"{q_monomial!r}\t{m.e3_exact(coefficient)}"
                )
    text = "\n".join(lines) + "\n"
    path.write_text(text)
    return sha256(text.encode()).hexdigest(), len(lines) - 1


def write_polynomial(path, polynomial):
    return h5.write_polynomial(path, polynomial)


def affine_substitute(polynomial, images):
    out = {}
    first_nonzero_contribution = None
    scanned = 0
    for parameter_monomial, coefficient in sorted(polynomial.items()):
        contribution = {(): QPoly.coerce(coefficient)}
        for variable in parameter_monomial:
            contribution = v87.multiply(contribution, images[variable])
        if contribution:
            if first_nonzero_contribution is None:
                first_nonzero_contribution = contribution
            out = v87.add(out, contribution)
        scanned += 1
        if scanned % 100 == 0:
            print(
                f"literal_P12_terms_scanned={scanned};"
                f"normal_form_parameter_terms={len(out)};"
                f"normal_form_q_terms={v87.coefficient_term_count(out)}",
                flush=True,
            )
    assert first_nonzero_contribution
    omitted = v87.add(out, first_nonzero_contribution, -1)
    assert omitted != out
    return v87.clean(out), first_nonzero_contribution, scanned


def denominator_record(label, polynomial_values):
    return t.denominator_record(label, polynomial_values)


def main():
    outdir = Path(os.environ["TD6_OUTPUT_DIR"]).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    assert os.environ.get("AWS_RUN_TAG", "").startswith(
        "td6_v89h12_allq_p12_full_normal_form_"
    )
    print("producer=TD6-V89H12-ALLQ-P12-FULL-NORMAL-FORM")
    print(f"h11_client_sha256={H11_SHA256}")
    print(f"h11_result_sha256={H11_RESULT_SHA256}")
    print(f"h11_freeze_sha256={H11_FREEZE_SHA256}")
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
    assert max(map(len, p12), default=0) <= 2
    _, raw_common = v87.assert_denominators_allowed([p12, *sources])
    assert raw_common == U*H and raw_common.gcd(F).total_degree() == 0
    print("literal_transport_FIRST_P12_rebuilt=true")
    print(f"literal_P12_parameter_terms={len(p12)}")
    print("literal_P12_parameter_degree_at_most_two=true")
    print(f"raw_source_common_denominator=({raw_common})")
    print("raw_source_denominator_coprime_F=true", flush=True)

    specialized_first = h6.specialize_first(first)
    specialized_p12 = h6.specialize_polynomial(p12)
    pivots = h5.base_pivot_columns(specialized_first)
    pivot_set = set(pivots)
    all_variables = set()
    for _, row, _ in specialized_first:
        all_variables.update(row)
    for monomial in specialized_p12:
        all_variables.update(monomial)
    free_variables = tuple(sorted(all_variables - pivot_set))
    assert len(pivots) == len(pivot_set) == 38
    assert all_variables == set(range(132))
    assert len(free_variables) == 94
    assert all_variables == pivot_set | set(free_variables)
    print("pivot_variables=" + ",".join(map(str, pivots)))
    print("free_variables=" + ",".join(map(str, free_variables)))
    print("complete_free_variable_inventory_count=94", flush=True)

    A0 = [
        [row.get(pivot, QPoly()).constant() for pivot in pivots]
        for _, row, _ in specialized_first
    ]
    A = [
        [row.get(pivot, QPoly()) for pivot in pivots]
        for _, row, _ in specialized_first
    ]
    D = [
        [row.get(variable, QPoly()) for variable in free_variables]
        for _, row, _ in specialized_first
    ]
    rhs = [rhs for _, _, rhs in specialized_first]
    inverse_A0 = h5.inverse_constant_matrix(A0)
    B = h5.matmul_constant_q(inverse_A0, A)
    identity_q = h11.p.identity_matrix(38)
    N = [[B[i][j] - identity_q[i][j] for j in range(38)] for i in range(38)]
    n_sha, n_entries, n_terms, n_degree = h11.p.matrix_stats(N)
    assert n_sha == EXPECTED_N_SHA256
    assert (n_entries, n_terms, n_degree) == (532, 6069, 1)
    print(f"N_sha256={n_sha}")
    print("N_affine_allq=true", flush=True)

    S_full, inverse_S_full, order, upper_N = h11.reconstruct_flag(N, outdir)
    W = [[S_full[i][order[j]] for j in range(38)] for i in range(38)]
    inverse_W = [
        [inverse_S_full[order[i]][j] for j in range(38)]
        for i in range(38)
    ]
    assert h5.matmul_constant(W, inverse_W) == h11.identity_constant(38)
    assert h5.matmul_constant(inverse_W, W) == h11.identity_constant(38)

    def solve_original_right_side(right_side, label):
        base = matvec_constant_q(inverse_A0, right_side)
        triangular = matvec_constant_q(inverse_W, base)
        solution = solve_upper_labeled(upper_N, triangular, label)
        return matvec_constant_q(W, solution)

    constant_solution = solve_original_right_side(rhs, "constant")
    assert matvec_q(A, constant_solution) == rhs
    constant_sha, _, _, constant_degree = qpoly_stats(constant_solution)
    # The vector-file digest, which includes headers and exact formatting, is
    # the H11 custody comparison; the structural digest above is independent.
    constant_file_sha, _ = h11.write_qvector(
        outdir / "H12_CONSTANT_FIRST_SOLUTION.tsv", constant_solution
    )
    assert constant_file_sha == (
        "ea9537bef63e65241978b82b8e08f0653b21751508194725cc9494b798a571a9"
    )
    print(f"constant_solution_structural_sha256={constant_sha}")
    print(f"constant_solution_max_q_degree={constant_degree}")
    print("constant_solution_equals_frozen_H11=true", flush=True)

    direction_solutions = []
    for column, variable in enumerate(free_variables):
        right_side = [-D[row][column] for row in range(38)]
        solution = solve_original_right_side(right_side, f"free_{variable}")
        replay = matvec_q(A, solution)
        assert all(replay[row] + D[row][column] == QPoly() for row in range(38))
        direction_solutions.append(solution)
    print("all_free_directions_original_FIRST_replay=true", flush=True)

    fixture_found = False
    for column, solution in enumerate(direction_solutions):
        for position, value in enumerate(solution):
            if not value:
                continue
            omitted = list(solution)
            omitted[position] = QPoly()
            replay = matvec_q(A, omitted)
            if any(replay[row] + D[row][column] for row in range(38)):
                fixture_found = True
                print(
                    f"pivot_direction_omission_fixture_free={free_variables[column]};"
                    f"pivot_position={position}",
                    flush=True,
                )
                break
        if fixture_found:
            break
    assert fixture_found
    print("pivot_direction_omission_negative_control=true", flush=True)

    affine_sha, affine_terms = write_affine_pivot_map(
        outdir / "ALLQ_AFFINE_PIVOT_MAP.tsv",
        pivots,
        free_variables,
        constant_solution,
        direction_solutions,
    )
    affine_values = [
        coefficient
        for solution in [constant_solution, *direction_solutions]
        for value in solution
        for coefficient in value.coefficients.values()
    ]
    _, affine_nonzero, affine_q_terms, affine_max_q_degree = qpoly_stats(
        [value for solution in [constant_solution, *direction_solutions] for value in solution]
    )
    print(f"affine_pivot_map_sha256={affine_sha}")
    print(f"affine_pivot_map_rows={affine_terms}")
    print(f"affine_pivot_map_nonzero_pieces={affine_nonzero}")
    print(f"affine_pivot_map_q_terms={affine_q_terms}")
    print(f"affine_pivot_map_max_q_degree={affine_max_q_degree}", flush=True)

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

    normal_form, _, scanned = affine_substitute(specialized_p12, images)
    assert scanned == len(specialized_p12)
    assert all(set(monomial).issubset(free_position) for monomial in normal_form)
    parameter_degree = max(map(len, normal_form), default=0)
    assert parameter_degree <= 2
    normal_form_sha = write_polynomial(
        outdir / "ALLQ_P12_FULL_NORMAL_FORM.tsv", normal_form
    )
    q_support = sorted({
        q_monomial
        for value in normal_form.values()
        for q_monomial in value.coefficients
    })
    mixed_q = [monomial for monomial in q_support if len(set(monomial)) > 1]
    max_q_degree = max(map(len, q_support), default=0)
    print(f"full_normal_form_sha256={normal_form_sha}")
    print(f"full_normal_form_parameter_terms={len(normal_form)}")
    print(f"full_normal_form_coefficient_terms={v87.coefficient_term_count(normal_form)}")
    print(f"full_normal_form_parameter_degree={parameter_degree}")
    print(f"full_normal_form_q_support_count={len(q_support)}")
    print(f"full_normal_form_mixed_q_support_count={len(mixed_q)}")
    print(f"full_normal_form_max_total_q_degree={max_q_degree}", flush=True)

    empty, _ = h11.empty_parameter_value(
        specialized_p12, pivots, constant_solution
    )
    assert normal_form.get((), QPoly()) == empty
    empty_sha, _ = h11.write_qpoly(
        outdir / "H12_EMPTY_PARAMETER_P12_FUNCTIONAL.tsv", empty
    )
    assert empty_sha == EXPECTED_EMPTY_SHA256
    print("empty_parameter_coefficient_equals_frozen_H11=true", flush=True)

    q14_class = v87.clean({
        monomial: QPoly(0, {(14,): value.coefficients[(14,)]})
        for monomial, value in normal_form.items()
        if value.coefficients.get((14,), E3())
    })
    q14_sha = write_polynomial(
        outdir / "ALLQ_P12_PURE_Q14_CLASS.tsv", q14_class
    )
    assert q14_sha == EXPECTED_Q14_CLASS_SHA256
    print(f"pure_q14_class_sha256={q14_sha}")
    print("pure_q14_class_equals_frozen_V89H6=true", flush=True)

    denominator_records = [
        denominator_record("affine_pivot_map", affine_values),
        denominator_record("full_P12_normal_form", (
            coefficient
            for value in normal_form.values()
            for coefficient in value.coefficients.values()
        )),
    ]
    denominator_text = "label\tvalue_count\tallowed\tcommon\tfactorization\n" + "\n".join(
        f"{label}\t{count}\t{str(allowed).lower()}\t{common}\t{factorization}"
        for label, count, common, factorization, allowed in denominator_records
    ) + "\n"
    (outdir / "ALLQ_P12_FULL_NORMAL_FORM_DENOMINATORS.tsv").write_text(
        denominator_text
    )
    denominator_sha = sha256(denominator_text.encode()).hexdigest()
    denominators_allowed = all(record[-1] for record in denominator_records)
    print(f"full_normal_form_denominator_ledger_sha256={denominator_sha}")
    print(f"full_normal_form_denominators_registered={str(denominators_allowed).lower()}")

    result_lines = [
        f"h11_result_sha256={H11_RESULT_SHA256}",
        f"h11_freeze_sha256={H11_FREEZE_SHA256}",
        f"N_sha256={n_sha}",
        "free_variables=" + ",".join(map(str, free_variables)),
        f"affine_pivot_map_sha256={affine_sha}",
        f"full_normal_form_sha256={normal_form_sha}",
        f"full_normal_form_parameter_terms={len(normal_form)}",
        f"full_normal_form_coefficient_terms={v87.coefficient_term_count(normal_form)}",
        f"full_normal_form_parameter_degree={parameter_degree}",
        f"full_normal_form_max_total_q_degree={max_q_degree}",
        f"pure_q14_class_sha256={q14_sha}",
        f"denominator_ledger_sha256={denominator_sha}",
        "all_22_q_independent_untruncated=true",
        "all_free_directions_original_FIRST_replay=true",
        "pivot_direction_omission_negative_control=true",
        "literal_P12_omission_negative_control=true",
        "empty_parameter_coefficient_equals_frozen_H11=true",
        "pure_q14_class_equals_frozen_V89H6=true",
        f"denominators_registered={str(denominators_allowed).lower()}",
        "unit_ideal_claim=false",
        "source_point_claim=false",
        "whole_TD6_killed=false",
        "JC2_resolved=false",
    ]
    result_text = "\n".join(result_lines) + "\n"
    (outdir / "ALLQ_P12_FULL_NORMAL_FORM_RESULT.txt").write_text(result_text)
    result_sha = sha256(result_text.encode()).hexdigest()
    print(f"full_normal_form_result_sha256={result_sha}")
    if denominators_allowed:
        print("TD6-V89H12-ALLQ-P12-FULL-NORMAL-FORM PASS")
    else:
        print("TD6-V89H12-ALLQ-P12-FULL-NORMAL-FORM DENOMINATOR-FAIL-CLOSED")
    v85.restore_base_qd_state()


if __name__ == "__main__":
    main()
