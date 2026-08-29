#!/usr/bin/env python3
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V23 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_typed_census_v23_20260827"
PARSER = V23 / "census_j2_typed_v23.py"
PARSER_SHA = "14f2de22d8cabaea12ac7fc7bf72cca275edbbb6a35dc7c0556a6e18e67c4501"
V23_RESULT = V23 / "output_r1/RESULT.json"
V23_RESULT_SHA = "ce4d0adbbe94e1337bed5047da0417e3b17cb86530715fb62316086cabd14641"
V28 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g16_v28_20260827/aws_q/compiled"
V28_RESULT = V28 / "result.json"
V28_RESULT_SHA = "7e00fc2ca8de3fee8ddf9cfa7b9adfef526cc8f1cc2efcb90fb7290e8fece3ae"
V30 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g17_v30_20260827/aws_q/compiled"
V30_RESULT = V30 / "result.json"
V30_RESULT_SHA = "6a644c20551874563d6c85cdbf81e5838ef22906e9ac7ada67b075889befb7c1"
PREREG = HERE / "PREREGISTRATION.md"
POINT = {
    "a1": Fraction(48), "aa0": Fraction(48), "cs1": Fraction(8),
    "ec3": Fraction(384), "rs2": Fraction(-32),
}
EXPECTED_G17 = {f"Tg17_{row}": Fraction(-20736 if row == 5 else 0) for row in range(1, 8)}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_parser():
    pins = ((PARSER, PARSER_SHA), (V23_RESULT, V23_RESULT_SHA),
            (V28_RESULT, V28_RESULT_SHA), (V30_RESULT, V30_RESULT_SHA))
    for path, expected in pins:
        if digest(path) != expected:
            fail(("upstream hash", str(path)))
    spec = importlib.util.spec_from_file_location("v31_parser", PARSER)
    if spec is None or spec.loader is None:
        fail("parser import")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def evaluate(polynomial, point):
    answer = Fraction(0)
    for monomial, coefficient in polynomial.items():
        value = coefficient
        for name, exponent in monomial:
            value *= point.get(name, Fraction(0)) ** exponent
        answer += value
    return answer


def derivative_at(polynomial, variable, point):
    answer = Fraction(0)
    for monomial, coefficient in polynomial.items():
        powers = dict(monomial)
        exponent = powers.get(variable, 0)
        if not exponent:
            continue
        value = coefficient * exponent
        for name, power in monomial:
            adjusted = power - 1 if name == variable else power
            if adjusted:
                value *= point.get(name, Fraction(0)) ** adjusted
        answer += value
    return answer


def encode(value):
    if isinstance(value, Fraction):
        return [value.numerator, value.denominator]
    return int(value)


def convert(value: Fraction, characteristic: int):
    if not characteristic:
        return value
    return (value.numerator * pow(value.denominator, -1, characteristic)) % characteristic


def add(left, right, characteristic):
    value = left + right
    return value % characteristic if characteristic else value


def sub(left, right, characteristic):
    value = left - right
    return value % characteristic if characteristic else value


def mul(left, right, characteristic):
    value = left * right
    return value % characteristic if characteristic else value


def inv(value, characteristic):
    return pow(value, -1, characteristic) if characteristic else Fraction(1, 1) / value


def rref_solve(coefficients, rhs, characteristic):
    rows = len(coefficients)
    columns = len(coefficients[0]) if rows else 0
    matrix = [list(row) + [right] for row, right in zip(coefficients, rhs)]
    combinations = [[int(i == j) for j in range(rows)] for i in range(rows)]
    pivot_row = 0
    pivots = []
    for column in range(columns):
        selected = next((i for i in range(pivot_row, rows) if matrix[i][column]), None)
        if selected is None:
            continue
        matrix[pivot_row], matrix[selected] = matrix[selected], matrix[pivot_row]
        combinations[pivot_row], combinations[selected] = combinations[selected], combinations[pivot_row]
        scale = inv(matrix[pivot_row][column], characteristic)
        matrix[pivot_row] = [mul(value, scale, characteristic) for value in matrix[pivot_row]]
        combinations[pivot_row] = [mul(value, scale, characteristic) for value in combinations[pivot_row]]
        for index in range(rows):
            if index == pivot_row or not matrix[index][column]:
                continue
            factor = matrix[index][column]
            matrix[index] = [sub(left, mul(factor, right, characteristic), characteristic)
                             for left, right in zip(matrix[index], matrix[pivot_row])]
            combinations[index] = [sub(left, mul(factor, right, characteristic), characteristic)
                                   for left, right in zip(combinations[index], combinations[pivot_row])]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == rows:
            break
    for index, row in enumerate(matrix):
        if not any(row[:-1]) and row[-1]:
            scale = inv(row[-1], characteristic)
            dual = [mul(value, scale, characteristic) for value in combinations[index]]
            return {"outcome": "inconsistent", "rank": len(pivots), "dual": dual}
    solution = [0 for _ in range(columns)]
    for row, column in enumerate(pivots):
        solution[column] = matrix[row][-1]
    return {"outcome": "consistent", "rank": len(pivots), "solution": solution}


def matrix_rank(coefficients, characteristic):
    return rref_solve(coefficients, [0 for _ in coefficients], characteristic)["rank"]


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("output", type=Path)
    cli.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = cli.parse_args()
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if platform.system() != "Linux" or not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2" or not tag:
        fail("registered AWS EC2 lane required")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    parser = load_parser()
    v23 = json.loads(V23_RESULT.read_text())
    v28 = json.loads(V28_RESULT.read_text())
    v30 = json.loads(V30_RESULT.read_text())

    rows = []
    source_hashes = {}
    for name, record in sorted(v23["records"].items(), key=lambda item: (item[1]["grade"], item[1]["row"])):
        chart = record["charts"]["a1_ordered"]
        path = V23 / "output_r1" / chart["output"]
        if digest(path) != chart["output_sha256"]:
            fail(("V23 row hash", name))
        polynomial = parser.specialize(parser.parse(path), frozenset({"rho"}), {})
        rows.append((name, polynomial, "old"))
        source_hashes[str(path.relative_to(ROOT))] = chart["output_sha256"]
    for grade, base, manifest in ((16, V28, v28), (17, V30, v30)):
        for row in range(1, 8):
            name = f"Tg{grade}_{row}"
            path = base / Path(manifest["coefficient_paths"][name]).name
            if digest(path) != manifest["coefficient_sha256"][name]:
                fail((f"V{28 if grade == 16 else 30} row hash", name))
            rows.append((name, parser.parse(path), "old" if grade == 16 else "new"))
            source_hashes[str(path.relative_to(ROOT))] = manifest["coefficient_sha256"][name]
    if len(rows) != 56:
        fail(("row census", len(rows)))

    residuals = {name: evaluate(polynomial, POINT) for name, polynomial, _ in rows}
    if any(residuals[name] for name, _, kind in rows if kind == "old"):
        fail("old-point bridge")
    for name, expected in EXPECTED_G17.items():
        if residuals[name] != expected:
            fail(("grade17 residual", name, residuals[name]))
    mutation = dict(POINT); mutation["rs2"] += 1
    if not any(evaluate(polynomial, mutation) for _, polynomial, kind in rows if kind == "old"):
        fail("point mutation control")

    variables = sorted(
        {variable for _, polynomial, _ in rows for monomial in polynomial for variable, _ in monomial if variable != "a1"},
        key=lambda name: (parser.sigma_weight(name), name),
    )
    jacobian_q = [[derivative_at(polynomial, variable, POINT) for variable in variables]
                  for _, polynomial, _ in rows]
    jacobian = [[convert(value, args.characteristic) for value in row] for row in jacobian_q]
    rhs = [convert(-residuals[name], args.characteristic) for name, _, _ in rows]
    old_count = sum(kind == "old" for _, _, kind in rows)
    old_rank = matrix_rank(jacobian[:old_count], args.characteristic)
    solved = rref_solve(jacobian, rhs, args.characteristic)

    if solved["outcome"] == "consistent":
        for row, right in zip(jacobian, rhs):
            replay = 0
            for coefficient, value in zip(row, solved["solution"]):
                replay = add(replay, mul(coefficient, value, args.characteristic), args.characteristic)
            if replay != right:
                fail("solution replay")
    else:
        for column in range(len(variables)):
            replay = 0
            for coefficient, value in zip((row[column] for row in jacobian), solved["dual"]):
                replay = add(replay, mul(coefficient, value, args.characteristic), args.characteristic)
            if replay:
                fail(("dual column replay", column))
        replay = 0
        for right, value in zip(rhs, solved["dual"]):
            replay = add(replay, mul(right, value, args.characteristic), args.characteristic)
        if replay != 1:
            fail(("dual rhs replay", replay))

    record = {
        "outcome": solved["outcome"],
        "rank": solved["rank"],
        "old_rank": old_rank,
    }
    if solved["outcome"] == "consistent":
        solution = {name: value for name, value in zip(variables, solved["solution"]) if value}
        record["solution"] = {name: encode(value) for name, value in solution.items()}
    else:
        dual = {name: value for (name, _, _), value in zip(rows, solved["dual"]) if value}
        record["dual"] = {name: encode(value) for name, value in dual.items()}

    result = {
        "status": "PASS-A1-GRADE17-TANGENT-V31",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "preregistration_sha256": digest(PREREG),
        "v23_result_sha256": V23_RESULT_SHA,
        "v28_result_sha256": V28_RESULT_SHA,
        "v30_result_sha256": V30_RESULT_SHA,
        "rows": len(rows),
        "old_rows": old_count,
        "new_rows": len(rows) - old_count,
        "variables": variables,
        "fixed_coordinate": {"a1": [48, 1]},
        "grade17_residuals_q": {name: [value.numerator, value.denominator] for name, value in EXPECTED_G17.items()},
        "source_sha256": source_hashes,
        **record,
        "scope": "first-order neighborhood of one rational ordered-a1 rho=0 grade16 point, with a1 fixed",
    }
    path = output / "RESULT.json"
    path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("PASS-A1-GRADE17-TANGENT-V31")
    print(f"OUTCOME={result['outcome']}")
    print(f"OLD_RANK={old_rank}")
    print(f"FULL_RANK={solved['rank']}")
    print(f"RESULT_SHA256={digest(path)}")


if __name__ == "__main__":
    main()
