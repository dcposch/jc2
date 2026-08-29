#!/usr/bin/env python3
"""Exact support and generic-rank witness for the V89H12 P12 quotient."""

import ast
from fractions import Fraction
from hashlib import sha256
import os
from pathlib import Path


HERE = Path(__file__).resolve().parent
INPUT = (
    HERE / "evidence/p12-full-r3/box02/output/"
    "ALLQ_P12_FULL_NORMAL_FORM.tsv"
)
INPUT_SHA = "c8a738b6024ac02e56455674efa8c89c37684a87e0312141a5ca4259ca02e4c4"
RESULT = HERE / "P12_FULL_NORMAL_FORM_RESULT.md"
RESULT_SHA = "7004c6359eba808c6f5f66ddd0b72c917fc734c1c3a6eea67878d19859ba23ef"
FREEZE = HERE / "P12_FULL_NORMAL_FORM_FREEZE.sha256"
FREEZE_SHA = "c7a146ee89ced521cb23544be6a977413c003b17d0a256a26eda6dae9d435a11"
for path, expected in ((INPUT, INPUT_SHA), (RESULT, RESULT_SHA), (FREEZE, FREEZE_SHA)):
    assert sha256(path.read_bytes()).hexdigest() == expected

PARAMETERS = (6, 8, 9, 11, 12, 13, 15, 16, 17, 18, 20, 21, 22, 24, 25, 27)
Q_EXPONENTS = tuple(range(2, 15))
SCALAR_Q = tuple(range(3, 15))


def parse_tuple(text):
    value = ast.literal_eval(text)
    assert isinstance(value, tuple)
    return tuple(int(entry) for entry in value)


def eval_fraction(node, names):
    if isinstance(node, ast.Expression):
        return eval_fraction(node.body, names)
    if isinstance(node, ast.Constant) and isinstance(node.value, int):
        return Fraction(node.value)
    if isinstance(node, ast.Name) and node.id in names:
        return Fraction(names[node.id])
    if isinstance(node, ast.UnaryOp):
        value = eval_fraction(node.operand, names)
        if isinstance(node.op, ast.USub):
            return -value
        if isinstance(node.op, ast.UAdd):
            return value
    if isinstance(node, ast.BinOp):
        left = eval_fraction(node.left, names)
        right = eval_fraction(node.right, names)
        if isinstance(node.op, ast.Add):
            return left + right
        if isinstance(node.op, ast.Sub):
            return left - right
        if isinstance(node.op, ast.Mult):
            return left * right
        if isinstance(node.op, ast.Div):
            return left / right
        if isinstance(node.op, ast.Pow):
            assert right.denominator == 1
            return left ** right.numerator
    raise ValueError(("unsupported_expression", ast.dump(node)))


def exact_value(pair, u=1, v=3):
    numerator, denominator = pair
    names = {"U": u, "V": v}
    num = eval_fraction(ast.parse(numerator.replace("^", "**"), mode="eval"), names)
    den = eval_fraction(ast.parse(denominator.replace("^", "**"), mode="eval"), names)
    assert den
    return num / den


def load_records():
    records = {}
    lines = INPUT.read_text().splitlines()
    assert lines[0] == "parameter_monomial\tq_monomial\tcoefficient_exact"
    for line in lines[1:]:
        parameter_text, q_text, coefficient_text = line.split("\t")
        key = parse_tuple(parameter_text), parse_tuple(q_text)
        coefficient = ast.literal_eval(coefficient_text)
        assert len(coefficient) == 18 and key not in records
        records[key] = coefficient
    assert len(records) == 166
    return records


def nonzero_coordinates(coefficient):
    return tuple(index for index, (numerator, _) in enumerate(coefficient) if numerator != "0")


def rank_and_pivots(matrix):
    work = [list(row) for row in matrix]
    nrow, ncol = len(work), len(work[0])
    rank, pivots = 0, []
    for column in range(ncol):
        pivot = next((row for row in range(rank, nrow) if work[row][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        pivot_value = work[rank][column]
        work[rank] = [entry / pivot_value for entry in work[rank]]
        for row in range(nrow):
            if row == rank or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [
                work[row][entry] - factor * work[rank][entry]
                for entry in range(ncol)
            ]
        pivots.append(column)
        rank += 1
        if rank == nrow:
            break
    return rank, tuple(pivots)


def determinant(matrix):
    work = [list(row) for row in matrix]
    size = len(work)
    out = Fraction(1)
    for column in range(size):
        pivot = next((row for row in range(column, size) if work[row][column]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            out = -out
        value = work[column][column]
        out *= value
        for row in range(column + 1, size):
            factor = work[row][column] / value
            for entry in range(column, size):
                work[row][entry] -= factor * work[column][entry]
    return out


def fraction_text(value):
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def main():
    outdir = Path(os.environ["TD6_OUTPUT_DIR"]).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    assert os.environ.get("AWS_RUN_TAG", "").startswith("td6_v89h14_p12_two_row_")
    records = load_records()
    parameter_records = {
        key: value for key, value in records.items() if key[0]
    }
    constant_records = {
        key: value for key, value in records.items() if not key[0]
    }
    assert {
        coordinate
        for value in parameter_records.values()
        for coordinate in nonzero_coordinates(value)
    } == {0, 1}
    assert all(set(nonzero_coordinates(value)) <= {0, 1} for value in parameter_records.values())
    assert {
        coordinate
        for value in constant_records.values()
        for coordinate in nonzero_coordinates(value)
    } == set(range(8))
    assert all(set(nonzero_coordinates(value)) <= set(range(8)) for value in constant_records.values())
    assert all(
        value[coordinate][0] == "0"
        for value in records.values()
        for coordinate in range(8, 18)
    )

    zero18 = tuple(("0", "1") for _ in range(18))
    q2_24 = records[((24,), (2,))]
    q2_27 = records[((27,), (2,))]
    assert q2_24[0:2] == (("6", "1"), ("0", "1"))
    assert q2_27[0:2] == (("8", "1"), ("4", "1"))
    assert all(
        records.get(((parameter,), (2,)), zero18) == zero18
        for parameter in PARAMETERS if parameter not in (24, 27)
    )
    q2_minor = Fraction(6) * Fraction(4) - Fraction(0) * Fraction(8)
    assert q2_minor == 24

    scalar_lines = ["coordinate\tq_monomial\tnumerator_exact\tdenominator_exact"]
    for coordinate in range(2, 8):
        for q_monomial in ((), *((exponent,) for exponent in SCALAR_Q)):
            pair = records.get(((), q_monomial), zero18)[coordinate]
            if pair[0] != "0":
                scalar_lines.append(
                    f"{coordinate}\t{q_monomial!r}\t{pair[0]}\t{pair[1]}"
                )
    scalar_text = "\n".join(scalar_lines) + "\n"
    (outdir / "P12_SIX_SCALAR_COMPATIBILITY_EQUATIONS.tsv").write_text(scalar_text)
    scalar_sha = sha256(scalar_text.encode()).hexdigest()

    coefficient_matrix = []
    constant_vector = []
    for coordinate in range(2, 8):
        constant_vector.append(exact_value(records[((), ())][coordinate]))
        coefficient_matrix.append([
            exact_value(records.get(((), (exponent,)), zero18)[coordinate])
            for exponent in SCALAR_Q
        ])
    rank, pivot_columns = rank_and_pivots(coefficient_matrix)
    assert rank == 6 and len(pivot_columns) == 6
    minor_matrix = [
        [row[column] for column in pivot_columns]
        for row in coefficient_matrix
    ]
    minor = determinant(minor_matrix)
    assert minor
    pivot_q = tuple(SCALAR_Q[column] for column in pivot_columns)

    support_lines = [
        "object\texact_coordinate_support",
        "quotient_variable_coefficients\t0,1",
        "empty_parameter_coefficient\t0,1,2,3,4,5,6,7",
        "identically_zero_coordinates\t8,9,10,11,12,13,14,15,16,17",
        "six_scalar_compatibilities\t2,3,4,5,6,7",
    ]
    support_text = "\n".join(support_lines) + "\n"
    (outdir / "P12_TWO_ROW_SCALAR_SUPPORT.tsv").write_text(support_text)
    support_sha = sha256(support_text.encode()).hexdigest()

    result = (
        f"input_sha256={INPUT_SHA}\n"
        "quotient_variable_coordinate_support=0,1\n"
        "empty_parameter_coordinate_support=0,1,2,3,4,5,6,7\n"
        "identically_zero_coordinates=8,9,10,11,12,13,14,15,16,17\n"
        "q2_rank_witness_columns=24,27\n"
        f"q2_squared_minor_coefficient={q2_minor}\n"
        "scalar_compatibility_coordinates=2,3,4,5,6,7\n"
        "scalar_q_support=q3-q14\n"
        "generic_rank_witness_point=U1,V3\n"
        f"generic_scalar_coefficient_rank={rank}\n"
        f"generic_scalar_pivot_q={','.join(map(str, pivot_q))}\n"
        f"generic_scalar_minor_at_U1_V3={fraction_text(minor)}\n"
        f"scalar_equations_sha256={scalar_sha}\n"
        f"support_sha256={support_sha}\n"
        "global_minor_unit_claim=false\nsource_point_claim=false\n"
        "whole_TD6_killed=false\nJC2_resolved=false\n"
    )
    (outdir / "P12_TWO_ROW_SCALAR_SPLIT_RESULT.txt").write_text(result)
    print(result, end="")
    print(f"result_sha256={sha256(result.encode()).hexdigest()}")
    print("TD6-V89H14-P12-TWO-ROW-SCALAR-SPLIT PASS")


if __name__ == "__main__":
    main()
