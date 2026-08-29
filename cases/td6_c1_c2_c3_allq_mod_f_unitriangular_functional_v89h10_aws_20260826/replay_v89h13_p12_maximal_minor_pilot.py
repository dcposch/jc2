#!/usr/bin/env python3
"""Finite-field augmented-maximal-minor pilot for frozen V89H12 P12 NF."""

import ast
from hashlib import sha256
import os
from pathlib import Path
import random


HERE = Path(__file__).resolve().parent
RESULT = HERE / "P12_FULL_NORMAL_FORM_RESULT.md"
RESULT_SHA = "7004c6359eba808c6f5f66ddd0b72c917fc734c1c3a6eea67878d19859ba23ef"
FREEZE = HERE / "P12_FULL_NORMAL_FORM_FREEZE.sha256"
FREEZE_SHA = "c7a146ee89ced521cb23544be6a977413c003b17d0a256a26eda6dae9d435a11"
INPUT = (
    HERE / "evidence/p12-full-r3/box02/output/"
    "ALLQ_P12_FULL_NORMAL_FORM.tsv"
)
INPUT_SHA = "c8a738b6024ac02e56455674efa8c89c37684a87e0312141a5ca4259ca02e4c4"
for path, expected in ((RESULT, RESULT_SHA), (FREEZE, FREEZE_SHA), (INPUT, INPUT_SHA)):
    assert sha256(path.read_bytes()).hexdigest() == expected

PARAMETERS = (6, 8, 9, 11, 12, 13, 15, 16, 17, 18, 20, 21, 22, 24, 25, 27)
Q_EXPONENTS = tuple(range(2, 15))
NROWS = 18


def eval_ast_mod(node, names, prime):
    if isinstance(node, ast.Expression):
        return eval_ast_mod(node.body, names, prime)
    if isinstance(node, ast.Constant) and isinstance(node.value, int):
        return node.value % prime
    if isinstance(node, ast.Name) and node.id in names:
        return names[node.id] % prime
    if isinstance(node, ast.UnaryOp):
        value = eval_ast_mod(node.operand, names, prime)
        if isinstance(node.op, ast.USub):
            return (-value) % prime
        if isinstance(node.op, ast.UAdd):
            return value
    if isinstance(node, ast.BinOp):
        left = eval_ast_mod(node.left, names, prime)
        right = eval_ast_mod(node.right, names, prime)
        if isinstance(node.op, ast.Add):
            return (left + right) % prime
        if isinstance(node.op, ast.Sub):
            return (left - right) % prime
        if isinstance(node.op, ast.Mult):
            return (left * right) % prime
        if isinstance(node.op, ast.Div):
            assert right
            return (left * pow(right, prime - 2, prime)) % prime
        if isinstance(node.op, ast.Pow):
            return pow(left, right, prime)
    raise ValueError(("unsupported_expression", ast.dump(node)))


def eval_expr_mod(text, u, v, prime):
    tree = ast.parse(text.replace("^", "**"), mode="eval")
    return eval_ast_mod(tree, {"U": u, "V": v}, prime)


def parse_monomial(text):
    value = ast.literal_eval(text)
    assert isinstance(value, tuple)
    return tuple(int(entry) for entry in value)


def load_records(prime, u, v):
    records = {}
    denominator_count = 0
    lines = INPUT.read_text().splitlines()
    assert lines[0] == "parameter_monomial\tq_monomial\tcoefficient_exact"
    for line in lines[1:]:
        parameter_text, q_text, coefficient_text = line.split("\t")
        parameter = parse_monomial(parameter_text)
        q_monomial = parse_monomial(q_text)
        exact = ast.literal_eval(coefficient_text)
        assert len(exact) == NROWS
        vector = []
        for numerator, denominator in exact:
            num = eval_expr_mod(numerator, u, v, prime)
            den = eval_expr_mod(denominator, u, v, prime)
            assert den, ("denominator_zero", parameter, q_monomial, denominator)
            denominator_count += denominator != "1"
            vector.append(num * pow(den, prime - 2, prime) % prime)
        assert (parameter, q_monomial) not in records
        records[parameter, q_monomial] = tuple(vector)
    assert len(records) == 166
    parameter_support = {parameter for parameter, _ in records}
    q_support = {q for _, q in records}
    assert parameter_support == {(), *((value,) for value in PARAMETERS)}
    assert q_support == {(), *((value,) for value in Q_EXPONENTS)}
    assert not any(parameter and not q for parameter, q in records)
    assert not any(len(parameter) > 1 or len(q) > 1 for parameter, q in records)
    return records, denominator_count


def matrix_at(records, q_values, prime):
    matrix = [[0] * (len(PARAMETERS) + 1) for _ in range(NROWS)]
    for row in range(NROWS):
        constant = records[(), ()][row]
        for exponent in Q_EXPONENTS:
            constant += q_values[exponent] * records.get(((), (exponent,)), (0,) * NROWS)[row]
        matrix[row][-1] = constant % prime
        for column, parameter in enumerate(PARAMETERS):
            value = 0
            for exponent in Q_EXPONENTS:
                value += q_values[exponent] * records.get(((parameter,), (exponent,)), (0,) * NROWS)[row]
            matrix[row][column] = value % prime
    return matrix


def rank_mod(matrix, prime):
    work = [list(row) for row in matrix]
    nrow, ncol = len(work), len(work[0]) if work else 0
    rank = 0
    for column in range(ncol):
        pivot = next((row for row in range(rank, nrow) if work[row][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][column], prime - 2, prime)
        work[rank] = [(entry * inverse) % prime for entry in work[rank]]
        for row in range(nrow):
            if row == rank or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [
                (work[row][entry] - factor * work[rank][entry]) % prime
                for entry in range(ncol)
            ]
        rank += 1
        if rank == nrow:
            break
    return rank


def det_mod(matrix, prime):
    work = [list(row) for row in matrix]
    size = len(work)
    assert all(len(row) == size for row in work)
    determinant = 1
    for column in range(size):
        pivot = next((row for row in range(column, size) if work[row][column]), None)
        if pivot is None:
            return 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            determinant = -determinant
        pivot_value = work[column][column]
        determinant = determinant * pivot_value % prime
        inverse = pow(pivot_value, prime - 2, prime)
        for row in range(column + 1, size):
            factor = work[row][column] * inverse % prime
            if not factor:
                continue
            for entry in range(column, size):
                work[row][entry] = (
                    work[row][entry] - factor * work[column][entry]
                ) % prime
    return determinant % prime


def maximal_minors(matrix, prime):
    assert len(matrix) == 18 and len(matrix[0]) == 17
    return tuple(
        det_mod([row for index, row in enumerate(matrix) if index != omitted], prime)
        for omitted in range(18)
    )


def scaled_axis(records, exponent, scalar, prime):
    values = {entry: 0 for entry in Q_EXPONENTS}
    values[exponent] = scalar % prime
    return matrix_at(records, values, prime)


def common_axis_candidates(records, exponent, prime):
    d1 = maximal_minors(scaled_axis(records, exponent, 1, prime), prime)
    d2_raw = maximal_minors(scaled_axis(records, exponent, 2, prime), prime)
    d3_raw = maximal_minors(scaled_axis(records, exponent, 3, prime), prime)
    inv_2_16 = pow(pow(2, 16, prime), prime - 2, prime)
    inv_3_16 = pow(pow(3, 16, prime), prime - 2, prime)
    constraints = []
    a_values, b_values = [], []
    for one, two_raw, three_raw in zip(d1, d2_raw, d3_raw):
        two = two_raw * inv_2_16 % prime
        a = (2 * one - two) % prime
        b = (two - one) % prime
        three = three_raw * inv_3_16 % prime
        assert three == (a + 3 * b) % prime
        a_values.append(a)
        b_values.append(b)
        if b:
            constraints.append((-a * pow(b, prime - 2, prime)) % prime)
        elif a:
            return d1, a_values, b_values, ()
    if not constraints:
        return d1, a_values, b_values, None
    root = constraints[0]
    candidates = (root,) if all(value == root for value in constraints) and root else ()
    return d1, a_values, b_values, candidates


def write_tsv(path, header, rows):
    text = "\t".join(header) + "\n" + "\n".join(
        "\t".join(map(str, row)) for row in rows
    ) + "\n"
    path.write_text(text)
    return sha256(text.encode()).hexdigest()


def main():
    outdir = Path(os.environ["TD6_OUTPUT_DIR"]).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    assert os.environ.get("AWS_RUN_TAG", "").startswith("td6_v89h13_p12_maxminor_")
    prime = int(os.environ["TD6_PRIME"])
    u = int(os.environ["TD6_U"]) % prime
    v = int(os.environ["TD6_V"]) % prime
    assert 3 < prime and pow(2, prime - 1, prime) == 1
    h = (v * v - 4 * u * u * u) % prime
    assert u and v and h
    records, denominator_count = load_records(prime, u, v)
    print("producer=TD6-V89H13-P12-AUGMENTED-MAXIMAL-MINOR-PILOT")
    print(f"input_sha256={INPUT_SHA}")
    print(f"prime={prime};U={u};V={v};H={h}")
    print(f"records={len(records)};nontrivial_denominator_entries={denominator_count}")
    print("parameter_count=16;q_count=13;rows=18;augmented_columns=17")
    print("A_homogeneous_q_degree_one=true;c_affine_q_degree_one=true", flush=True)

    zero_values = {exponent: 0 for exponent in Q_EXPONENTS}
    zero_matrix = matrix_at(records, zero_values, prime)
    assert rank_mod([row[:-1] for row in zero_matrix], prime) == 0
    assert rank_mod(zero_matrix, prime) == 1
    assert not any(maximal_minors(zero_matrix, prime))
    print("q_zero_rank_A=0;q_zero_rank_augmented=1;maximal_minors_all_zero=true")

    axis_rows = []
    excluded_axes = 0
    unresolved_axes = 0
    for exponent in Q_EXPONENTS:
        matrix = scaled_axis(records, exponent, 1, prime)
        rank_a = rank_mod([row[:-1] for row in matrix], prime)
        rank_b = rank_mod(matrix, prime)
        d1, a_values, b_values, candidates = common_axis_candidates(
            records, exponent, prime
        )
        nonzero_minors = sum(value != 0 for value in d1)
        if candidates == ():
            status = "empty_nonzero_axis_by_maximal_minors_mod_p"
            candidate_text = "none"
            excluded_axes += 1
        elif candidates is None:
            status = "all_maximal_minors_identically_zero_on_axis_mod_p"
            candidate_text = "unconstrained"
            unresolved_axes += 1
        else:
            status = "one_common_maximal_minor_root_mod_p"
            candidate_text = str(candidates[0])
            unresolved_axes += 1
        axis_rows.append((
            exponent,
            rank_a,
            rank_b,
            nonzero_minors,
            sum(value != 0 for value in a_values),
            sum(value != 0 for value in b_values),
            candidate_text,
            status,
        ))
        print(
            f"axis=q{exponent};rank_A_at_1={rank_a};rank_augmented_at_1={rank_b};"
            f"nonzero_minors_at_1={nonzero_minors};candidate={candidate_text};status={status}",
            flush=True,
        )

    axis_sha = write_tsv(
        outdir / "P12_PURE_AXIS_MAXIMAL_MINOR_DIAGNOSTIC.tsv",
        (
            "q_exponent", "rank_A_at_1", "rank_augmented_at_1",
            "nonzero_minors_at_1", "nonzero_degree16_parts",
            "nonzero_degree17_parts", "common_nonzero_t_candidate", "status",
        ),
        axis_rows,
    )

    rng = random.Random(8913 + prime + 17 * u + 31 * v)
    sample_rows = []
    augmented_rank_17 = 0
    coefficient_rank_16 = 0
    all_minors_zero = 0
    for sample in range(64):
        values = {exponent: rng.randrange(prime) for exponent in Q_EXPONENTS}
        if not any(values.values()):
            values[2] = 1
        matrix = matrix_at(records, values, prime)
        rank_a = rank_mod([row[:-1] for row in matrix], prime)
        rank_b = rank_mod(matrix, prime)
        minors = maximal_minors(matrix, prime)
        nonzero = sum(value != 0 for value in minors)
        coefficient_rank_16 += rank_a == 16
        augmented_rank_17 += rank_b == 17
        all_minors_zero += nonzero == 0
        sample_rows.append((sample, rank_a, rank_b, nonzero, sha256(
            (",".join(str(values[e]) for e in Q_EXPONENTS)).encode()
        ).hexdigest()))
    sample_sha = write_tsv(
        outdir / "P12_DENSE_RANK_SAMPLES.tsv",
        ("sample", "rank_A", "rank_augmented", "nonzero_maximal_minors", "q_digest"),
        sample_rows,
    )
    print(f"dense_samples=64;rank_A_16={coefficient_rank_16};rank_augmented_17={augmented_rank_17};all_minors_zero={all_minors_zero}")
    print(f"pure_axis_diagnostic_sha256={axis_sha}")
    print(f"dense_sample_diagnostic_sha256={sample_sha}")
    result = (
        f"input_sha256={INPUT_SHA}\nprime={prime}\nU={u}\nV={v}\nH={h}\n"
        f"pure_axes_empty_by_maximal_minors_mod_p={excluded_axes}\n"
        f"pure_axes_unresolved_mod_p={unresolved_axes}\n"
        f"dense_samples_rank_A_16={coefficient_rank_16}\n"
        f"dense_samples_rank_augmented_17={augmented_rank_17}\n"
        f"dense_samples_all_minors_zero={all_minors_zero}\n"
        f"pure_axis_diagnostic_sha256={axis_sha}\n"
        f"dense_sample_diagnostic_sha256={sample_sha}\n"
        "characteristic_zero_claim=false\nmixed_q_exclusion_claim=false\n"
        "source_point_claim=false\nwhole_TD6_killed=false\nJC2_resolved=false\n"
    )
    (outdir / "P12_MAXIMAL_MINOR_PILOT_RESULT.txt").write_text(result)
    print(f"result_sha256={sha256(result.encode()).hexdigest()}")
    print("TD6-V89H13-P12-AUGMENTED-MAXIMAL-MINOR-PILOT PASS")


if __name__ == "__main__":
    main()
