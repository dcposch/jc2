#!/usr/bin/env python3
"""Exact rational P12/P13 compatibility-point gate from frozen normal forms."""

import ast
from fractions import Fraction
from hashlib import sha256
import os
from pathlib import Path


HERE = Path(__file__).resolve().parent
P12 = HERE / "evidence/p12-full-r3/box02/output/ALLQ_P12_FULL_NORMAL_FORM.tsv"
P13 = HERE / "evidence/p13-full-r1/box02/output/ALLQ_P13_FULL_NORMAL_FORM.tsv"
P12_RESULT = HERE / "P12_TWO_ROW_SCALAR_RESULT.md"
P12_FREEZE = HERE / "P12_TWO_ROW_SCALAR_FREEZE.sha256"
P13_RESULT = HERE / "P13_FULL_NORMAL_FORM_RESULT.md"
P13_FREEZE = HERE / "P13_FULL_NORMAL_FORM_FREEZE.sha256"
PINS = (
    (P12, "c8a738b6024ac02e56455674efa8c89c37684a87e0312141a5ca4259ca02e4c4"),
    (P13, "9af3240d4016ad99766122303465d2cea7a10dc5e71b489f62564b9c3540c2d8"),
    (P12_RESULT, "88f4354b7b639d098e91b96e07ffbed1793d5c73aed8cc8014ba2b5996adf2e3"),
    (P12_FREEZE, "0e2aa4a0cb1c0e01b025f2de061cf0d70f093a68654fcc40eccc1929a0d811e7"),
    (P13_RESULT, "29d5723b0d920840dbdfe72398624cfc0672843dbbf1d713b2fdd29dea52712c"),
    (P13_FREEZE, "4048419e15f366baeb03d242f546f096ee22d4529e6c6fededf58b2aea951c18"),
)
for path, expected in PINS:
    assert sha256(path.read_bytes()).hexdigest() == expected, path

Q_EXPONENTS = tuple(range(2, 15)) + tuple(range(16, 25))
Y_VARIABLES = (
    6, 8, 9, 11, 12, 13, 15, 16, 17, 18, 20, 21, 22, 24, 25, 27,
    36, 37, 38, 40, 41, 43, 44, 45, 47, 48, 49, 50, 51, 53, 54, 55,
    56, 58, 59, 60, 61, 62, 64, 65, 66, 67, 68, 69, 70, 72, 73, 74,
    75, 76, 77, 79, 80, 81, 82, 83, 84, 85, 87, 88, 89, 90, 91, 92,
    93, 94, 96, 97, 98, 99, 100, 101, 102, 104, 105, 106, 107, 108,
    109, 111, 112, 113, 114, 115, 117, 118, 119, 120, 122, 123, 124,
    126, 127, 129,
)
ZERO18 = tuple(("0", "1") for _ in range(18))


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


def load_records(path, expected_count):
    records = {}
    lines = path.read_text().splitlines()
    assert lines[0] == "parameter_monomial\tq_monomial\tcoefficient_exact"
    for line in lines[1:]:
        parameter_text, q_text, coefficient_text = line.split("\t")
        key = parse_tuple(parameter_text), parse_tuple(q_text)
        coefficient = ast.literal_eval(coefficient_text)
        assert len(coefficient) == 18 and key not in records
        records[key] = coefficient
    assert len(records) == expected_count
    return records


def value(records, parameter, q_monomial, coordinate):
    return exact_value(records.get((parameter, q_monomial), ZERO18)[coordinate])


def rank(matrix):
    if not matrix:
        return 0
    work = [list(row) for row in matrix]
    nrow, ncol = len(work), len(work[0])
    out = 0
    for column in range(ncol):
        pivot = next((row for row in range(out, nrow) if work[row][column]), None)
        if pivot is None:
            continue
        work[out], work[pivot] = work[pivot], work[out]
        pivot_value = work[out][column]
        work[out] = [entry / pivot_value for entry in work[out]]
        for row in range(nrow):
            if row == out or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [
                work[row][entry] - factor * work[out][entry]
                for entry in range(ncol)
            ]
        out += 1
        if out == nrow:
            break
    return out


def solve_square(matrix, rhs):
    size = len(matrix)
    work = [list(matrix[row]) + [rhs[row]] for row in range(size)]
    determinant = Fraction(1)
    for column in range(size):
        pivot = next((row for row in range(column, size) if work[row][column]), None)
        if pivot is None:
            return Fraction(0), None
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            determinant = -determinant
        pivot_value = work[column][column]
        determinant *= pivot_value
        work[column] = [entry / pivot_value for entry in work[column]]
        for row in range(size):
            if row == column or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [
                work[row][entry] - factor * work[column][entry]
                for entry in range(size + 1)
            ]
    return determinant, tuple(work[row][-1] for row in range(size))


def solve_rectangular(matrix, rhs):
    nrow, ncol = len(matrix), len(matrix[0])
    work = [list(matrix[row]) + [rhs[row]] for row in range(nrow)]
    pivots = []
    active = 0
    for column in range(ncol):
        pivot = next((row for row in range(active, nrow) if work[row][column]), None)
        if pivot is None:
            continue
        work[active], work[pivot] = work[pivot], work[active]
        pivot_value = work[active][column]
        work[active] = [entry / pivot_value for entry in work[active]]
        for row in range(nrow):
            if row == active or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [
                work[row][entry] - factor * work[active][entry]
                for entry in range(ncol + 1)
            ]
        pivots.append(column)
        active += 1
        if active == nrow:
            break
    consistent = all(
        any(work[row][column] for column in range(ncol)) or not work[row][-1]
        for row in range(nrow)
    )
    if not consistent:
        return tuple(pivots), None
    solution = [Fraction(0) for _ in range(ncol)]
    for row, column in enumerate(pivots):
        solution[column] = work[row][-1]
    return tuple(pivots), tuple(solution)


def q_factor(q_monomial, q_solution):
    if not q_monomial:
        return Fraction(1)
    assert len(q_monomial) == 1
    return q_solution[Q_EXPONENTS.index(q_monomial[0])]


def evaluate_normal_form(records, q_solution, y_solution):
    out = [Fraction(0) for _ in range(18)]
    y_position = {variable: index for index, variable in enumerate(Y_VARIABLES)}
    for (parameter, q_monomial), coefficient in records.items():
        if not parameter:
            parameter_factor = Fraction(1)
        else:
            assert len(parameter) == 1 and parameter[0] in y_position
            parameter_factor = y_solution[y_position[parameter[0]]]
        factor = parameter_factor * q_factor(q_monomial, q_solution)
        if not factor:
            continue
        for coordinate in range(18):
            out[coordinate] += factor * exact_value(coefficient[coordinate])
    return tuple(out)


def fraction_text(value):
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def main():
    outdir = Path(os.environ["TD6_OUTPUT_DIR"]).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    assert os.environ.get("AWS_RUN_TAG", "").startswith("td6_v89h16_p12_p13_")
    p12 = load_records(P12, 166)
    p13 = load_records(P13, 238)

    p12_parameter_coordinates = {
        coordinate
        for (parameter, _), coefficient in p12.items() if parameter
        for coordinate, (numerator, _) in enumerate(coefficient) if numerator != "0"
    }
    p13_parameter_coordinates = {
        coordinate
        for (parameter, _), coefficient in p13.items() if parameter
        for coordinate, (numerator, _) in enumerate(coefficient) if numerator != "0"
    }
    assert p12_parameter_coordinates == p13_parameter_coordinates == {0, 1}
    assert len(Q_EXPONENTS) == 22 and len(Y_VARIABLES) == 94

    row_specs = [
        *(("P12", coordinate, p12) for coordinate in range(2, 8)),
        *(("P13", coordinate, p13) for coordinate in range(2, 18)),
    ]
    compatibility_matrix = [
        [value(records, (), (exponent,), coordinate) for exponent in Q_EXPONENTS]
        for _, coordinate, records in row_specs
    ]
    constants = [value(records, (), (), coordinate) for _, coordinate, records in row_specs]
    compatibility_rank = rank(compatibility_matrix)
    determinant, q_solution = solve_square(
        compatibility_matrix, tuple(-entry for entry in constants)
    )

    matrix_lines = [
        "source\tcoordinate\tconstant\t" + "\t".join(f"q{e}" for e in Q_EXPONENTS)
    ]
    for (source, coordinate, _), constant, row in zip(row_specs, constants, compatibility_matrix):
        matrix_lines.append(
            f"{source}\t{coordinate}\t{fraction_text(constant)}\t"
            + "\t".join(fraction_text(entry) for entry in row)
        )
    matrix_text = "\n".join(matrix_lines) + "\n"
    (outdir / "P12_P13_COMPATIBILITY_MATRIX_U1V3.tsv").write_text(matrix_text)
    matrix_sha = sha256(matrix_text.encode()).hexdigest()

    if q_solution is None:
        result = (
            f"compatibility_matrix_sha256={matrix_sha}\n"
            f"compatibility_rank={compatibility_rank}\n"
            "compatibility_size=22\ncompatibility_nonsingular=false\n"
            "rational_point_found=false\nsource_point_claim=false\n"
            "whole_TD6_killed=false\nJC2_resolved=false\n"
        )
        (outdir / "P12_P13_COMPATIBILITY_POINT_RESULT.txt").write_text(result)
        print(result, end="")
        print("TD6-V89H16-P12-P13-COMPATIBILITY SINGULAR-DIAGNOSTIC")
        return

    assert determinant and compatibility_rank == 22
    assert all(
        constants[row] + sum(
            compatibility_matrix[row][column] * q_solution[column]
            for column in range(22)
        ) == 0
        for row in range(22)
    )

    remaining_specs = [
        ("P12", 0, p12), ("P12", 1, p12),
        ("P13", 0, p13), ("P13", 1, p13),
    ]
    y_matrix = []
    y_rhs = []
    for _, coordinate, records in remaining_specs:
        empty = sum(
            value(records, (), q_monomial, coordinate) * q_factor(q_monomial, q_solution)
            for q_monomial in ((), *((exponent,) for exponent in Q_EXPONENTS))
        )
        y_rhs.append(-empty)
        y_matrix.append([
            sum(
                value(records, (variable,), q_monomial, coordinate)
                * q_factor(q_monomial, q_solution)
                for q_monomial in ((), *((exponent,) for exponent in Q_EXPONENTS))
            )
            for variable in Y_VARIABLES
        ])
    coefficient_rank = rank(y_matrix)
    augmented_rank = rank([
        [*y_matrix[row], y_rhs[row]] for row in range(4)
    ])
    y_pivots, y_solution = solve_rectangular(y_matrix, y_rhs)
    assert coefficient_rank == augmented_rank and y_solution is not None
    assert all(
        sum(y_matrix[row][column] * y_solution[column] for column in range(94))
        == y_rhs[row]
        for row in range(4)
    )

    p12_residual = evaluate_normal_form(p12, q_solution, y_solution)
    p13_residual = evaluate_normal_form(p13, q_solution, y_solution)
    assert p12_residual == p13_residual == tuple(Fraction(0) for _ in range(18))
    nonzero_q = tuple(
        exponent for exponent, entry in zip(Q_EXPONENTS, q_solution) if entry
    )
    nonzero_y = tuple(
        variable for variable, entry in zip(Y_VARIABLES, y_solution) if entry
    )
    assert len(nonzero_q) >= 2 and nonzero_y

    perturbed_q = list(q_solution)
    perturbed_q[0] += 1
    assert any(
        constants[row] + sum(
            compatibility_matrix[row][column] * perturbed_q[column]
            for column in range(22)
        )
        for row in range(22)
    )
    perturbed_y = list(y_solution)
    perturbed_y[y_pivots[0]] += 1
    assert any(
        sum(y_matrix[row][column] * perturbed_y[column] for column in range(94))
        - y_rhs[row]
        for row in range(4)
    )

    solution_lines = ["kind\tindex\tvalue"]
    solution_lines.extend(
        f"q\t{exponent}\t{fraction_text(entry)}"
        for exponent, entry in zip(Q_EXPONENTS, q_solution)
    )
    solution_lines.extend(
        f"y\t{variable}\t{fraction_text(entry)}"
        for variable, entry in zip(Y_VARIABLES, y_solution)
    )
    solution_text = "\n".join(solution_lines) + "\n"
    (outdir / "P12_P13_RATIONAL_POINT_U1V3.tsv").write_text(solution_text)
    solution_sha = sha256(solution_text.encode()).hexdigest()

    determinant_text = fraction_text(determinant) + "\n"
    (outdir / "P12_P13_COMPATIBILITY_DETERMINANT_U1V3.txt").write_text(determinant_text)
    determinant_sha = sha256(determinant_text.encode()).hexdigest()
    result = (
        "base_point_U=1\nbase_point_V=3\nbase_point_C=8\n"
        "base_point_F=0\nbase_point_H=5\nbase_point_B3=81\n"
        "registered_open_nonzero=true\n"
        f"compatibility_matrix_sha256={matrix_sha}\n"
        "compatibility_size=22\n"
        f"compatibility_rank={compatibility_rank}\n"
        "compatibility_nonsingular=true\n"
        f"compatibility_determinant_sha256={determinant_sha}\n"
        f"nonzero_q_count={len(nonzero_q)}\n"
        "nonzero_q_exponents=" + ",".join(map(str, nonzero_q)) + "\n"
        f"remaining_y_coefficient_rank={coefficient_rank}\n"
        f"remaining_augmented_rank={augmented_rank}\n"
        "remaining_y_pivots=" + ",".join(str(Y_VARIABLES[c]) for c in y_pivots) + "\n"
        f"nonzero_y_count={len(nonzero_y)}\n"
        f"rational_point_sha256={solution_sha}\n"
        "all_18_P12_normal_form_coordinates_zero=true\n"
        "all_18_P13_normal_form_coordinates_zero=true\n"
        "q_perturbation_negative_control=true\n"
        "y_perturbation_negative_control=true\n"
        "rational_point_found=true\n"
        "literal_normal_form_scope_only=true\nsource_point_claim=false\n"
        "P14_or_later_imposed=false\nwhole_TD6_killed=false\nJC2_resolved=false\n"
    )
    (outdir / "P12_P13_COMPATIBILITY_POINT_RESULT.txt").write_text(result)
    print(result, end="")
    print(f"result_sha256={sha256(result.encode()).hexdigest()}")
    print("TD6-V89H16-P12-P13-COMPATIBILITY-POINT PASS")


if __name__ == "__main__":
    main()
