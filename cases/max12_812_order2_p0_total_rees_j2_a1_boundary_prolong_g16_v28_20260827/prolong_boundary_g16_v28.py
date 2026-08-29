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
V20_MODULE = ROOT / "cases/max12_812_order2_p0_total_rees_allrows_g13_g14_export_v20_20260827/export_allrows_g13_g14_v20.py"
V20_SHA = "5c233e0f2193bc4cb6384e0ad16f3d8b063494541389463853365a7ac443a587"
V23 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_typed_census_v23_20260827"
V23_PARSER = V23 / "census_j2_typed_v23.py"
V23_PARSER_SHA = "14f2de22d8cabaea12ac7fc7bf72cca275edbbb6a35dc7c0556a6e18e67c4501"
V23_RESULT = V23 / "output_r1/RESULT.json"
V23_RESULT_SHA = "ce4d0adbbe94e1337bed5047da0417e3b17cb86530715fb62316086cabd14641"
PREREG = HERE / "PREREGISTRATION.md"
ROWS = tuple(range(1, 8))
OLD_POINT = {
    "a1": Fraction(1),
    "aa0": Fraction(1),
    "cs1": Fraction(1, 6),
    "ec3": Fraction(1, 6),
    "rs2": Fraction(-2, 3),
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_module(path: Path, expected: str, name: str):
    if digest(path) != expected:
        fail(("module hash", str(path)))
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        fail(("module import", str(path)))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def require_aws() -> str:
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if (
        platform.system() != "Linux"
        or not vendor.is_file()
        or vendor.read_text().strip() != "Amazon EC2"
        or not tag.startswith("max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g16_v28_")
    ):
        fail("registered V28 AWS lane required")
    return tag


def dense_series(base, names):
    return base.named_series(list(enumerate(names)))


def build_source_series(base):
    p = base.series_zero()
    p[0] = base.poly_scale(-2, base.poly_mul(base.poly_var("rho"), base.poly_var("rho")))
    for degree in range(1, 17):
        p[degree] = base.poly_scale(2, base.poly_var(f"ell{degree}"))

    c0 = dense_series(base, ["cs"] + [f"cs{i}" for i in range(1, 15)])
    c = base.series_shift(c0, 2)
    r0 = dense_series(base, ["rs"] + [f"rs{i}" for i in range(1, 15)])
    r = base.series_scale(Fraction(1, 4), base.series_add(base.series_mul(p, p), base.series_shift(r0, 2)))

    az = dense_series(base, ["a1", "aa1", "aaa1"] + [f"az{i}" for i in range(3, 12)])
    ac = dense_series(base, ["a0", "aa0", "aaa0"] + [f"ac{i}" for i in range(3, 12)])
    ez = dense_series(base, ["c1", "e1", "ee1"] + [f"ez{i}" for i in range(3, 12)])
    ec = dense_series(base, ["c0", "e0", "ee0"] + [f"ec{i}" for i in range(3, 12)])

    n3 = base.series_shift(az, 3)
    n2 = base.series_shift(ac, 3)
    n1 = base.series_shift(base.series_scale(Fraction(1, 2), base.series_add(base.series_mul(p, az), ez)), 3)
    n0 = base.series_shift(base.series_scale(Fraction(1, 2), base.series_add(base.series_mul(p, ac), ec)), 3)
    coefficients = {
        6: base.series_scale(2, p),
        5: base.series_scale(2, c),
        4: base.series_add(base.series_mul(p, p), base.series_scale(2, r)),
        3: base.series_add(base.series_scale(2, base.series_mul(p, c)), base.series_shift(n3, 2)),
        2: base.series_add(base.series_mul(c, c), base.series_scale(2, base.series_mul(p, r)), base.series_shift(n2, 2)),
        1: base.series_add(base.series_scale(2, base.series_mul(c, r)), base.series_shift(n1, 2)),
        0: base.series_add(base.series_mul(r, r), base.series_shift(n0, 2)),
    }
    k10 = dense_series(base, ["k", "k1", "k2c"] + [f"k10_{i}" for i in range(3, 13)])
    k6 = dense_series(base, ["k6", "k6_1", "k6_2", "k6_3", "k6_4"])
    k2 = dense_series(base, ["k2"])
    loads = {7: base.series_shift(k10, 4), 8: base.series_shift(k6, 12), 9: base.series_shift(k2, 20)}
    return coefficients, loads


def build_row(base, entries, row, coefficients, loads):
    total = base.series_zero()
    weights = [8 - index for index in range(7)] + [2, 6, 10]
    for raw_monomial, raw_coefficient in entries:
        monomial = [int(value) for value in raw_monomial]
        if len(monomial) != 10 or sum(a * b for a, b in zip(monomial, weights)) != 12 + row:
            fail(("tail contract", row, monomial))
        coefficient = Fraction(str(raw_coefficient))
        if not coefficient:
            fail(("zero tail coefficient", row, monomial))
        term = base.series_zero()
        term[0] = base.poly_const(1)
        for index, exponent in enumerate(monomial[:7]):
            if exponent:
                term = base.series_mul(term, base.series_pow(coefficients[index], exponent))
        for index, exponent in enumerate(monomial[7:], start=7):
            if exponent not in (0, 1):
                fail(("load nonlinearity", row, monomial))
            if exponent:
                term = base.series_mul(term, loads[index])
        total = base.series_add(total, base.series_scale(coefficient, term))
    return total


def evaluate(polynomial, point):
    answer = Fraction(0)
    for monomial, coefficient in polynomial.items():
        term = coefficient
        for name, exponent in monomial:
            term *= point.get(name, Fraction(0)) ** exponent
        answer += term
    return answer


def specialize_old_point(polynomial, sigma_weight):
    answer = {}
    for monomial, coefficient in polynomial.items():
        kept = []
        value = coefficient
        for name, exponent in monomial:
            if name in OLD_POINT:
                value *= OLD_POINT[name] ** exponent
            elif sigma_weight(name) == 16:
                kept.append((name, exponent))
            else:
                value = 0
                break
        if value:
            key = tuple(kept)
            answer[key] = answer.get(key, Fraction(0)) + value
            if not answer[key]:
                del answer[key]
    return answer


def encode_fraction(value):
    return [value.numerator, value.denominator]


def solve_affine(equations, variables):
    matrix = []
    combinations = []
    for row, polynomial in enumerate(equations):
        constant = polynomial.get((), Fraction(0))
        coefficients = []
        for variable in variables:
            coefficients.append(polynomial.get(((variable, 1),), Fraction(0)))
        allowed = {()} | {((variable, 1),) for variable in variables}
        if set(polynomial) - allowed:
            fail(("nonlinear grade-16 equation", row + 1, set(polynomial) - allowed))
        matrix.append(coefficients + [-constant])
        combinations.append([Fraction(int(i == row)) for i in range(len(equations))])

    pivot_row = 0
    pivot_columns = []
    for column in range(len(variables)):
        selected = next((index for index in range(pivot_row, len(matrix)) if matrix[index][column]), None)
        if selected is None:
            continue
        matrix[pivot_row], matrix[selected] = matrix[selected], matrix[pivot_row]
        combinations[pivot_row], combinations[selected] = combinations[selected], combinations[pivot_row]
        inverse = Fraction(1, 1) / matrix[pivot_row][column]
        matrix[pivot_row] = [value * inverse for value in matrix[pivot_row]]
        combinations[pivot_row] = [value * inverse for value in combinations[pivot_row]]
        for index in range(len(matrix)):
            if index == pivot_row or not matrix[index][column]:
                continue
            factor = matrix[index][column]
            matrix[index] = [left - factor * right for left, right in zip(matrix[index], matrix[pivot_row])]
            combinations[index] = [left - factor * right for left, right in zip(combinations[index], combinations[pivot_row])]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == len(matrix):
            break

    for index, row in enumerate(matrix):
        if not any(row[:-1]) and row[-1]:
            # sum(lambda_i * equation_i) = 1.
            scale = Fraction(-1, 1) / row[-1]
            dual = [value * scale for value in combinations[index]]
            return {"outcome": "inconsistent", "rank": len(pivot_columns), "dual": dual}

    solution = {variable: Fraction(0) for variable in variables}
    for row, column in enumerate(pivot_columns):
        solution[variables[column]] = matrix[row][-1]
    return {"outcome": "consistent", "rank": len(pivot_columns), "solution": solution}


def main() -> None:
    parser_cli = argparse.ArgumentParser()
    parser_cli.add_argument("output", type=Path)
    parser_cli.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser_cli.parse_args()
    tag = require_aws()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)

    v20 = load_module(V20_MODULE, V20_SHA, "v28_v20")
    parser = load_module(V23_PARSER, V23_PARSER_SHA, "v28_parser")
    if digest(V23_RESULT) != V23_RESULT_SHA:
        fail("V23 result hash")
    v23_result = json.loads(V23_RESULT.read_text())
    base = v20.load_replay()
    base.MAX_DEGREE = 16
    tails = json.loads(v20.TAILS.read_text())
    if sorted(tails) != [str(row) for row in ROWS]:
        fail("tail row census")
    coefficients, loads = build_source_series(base)
    totals = {row: build_row(base, tails[str(row)], row, coefficients, loads) for row in ROWS}

    killed = parser.J1 | frozenset({"a0", "rho"})
    face = {row: parser.specialize(totals[row][16], killed, {}) for row in ROWS}
    old_bridges = 0
    old_point_zeros = 0
    row_hashes = {}
    old_face = {}
    for name, record in sorted(v23_result["records"].items(), key=lambda item: (item[1]["grade"], item[1]["row"])):
        grade = int(record["grade"])
        row = int(record["row"])
        chart = record["charts"]["a1_ordered"]
        path = V23 / "output_r1" / chart["output"]
        if digest(path) != chart["output_sha256"]:
            fail(("V23 row hash", name))
        expected = parser.specialize(parser.parse(path), frozenset({"rho"}), {})
        rebuilt = parser.specialize(totals[row][grade], killed, {})
        if rebuilt != expected:
            fail(("old face bridge", name))
        old_bridges += 1
        row_hashes[str(path.relative_to(ROOT))] = chart["output_sha256"]
        old_face[name] = rebuilt
        if evaluate(rebuilt, OLD_POINT):
            fail(("old point", name, evaluate(rebuilt, OLD_POINT)))
        old_point_zeros += 1
    if old_bridges != 42 or old_point_zeros != 42:
        fail("old census")

    affine = {row: specialize_old_point(face[row], parser.sigma_weight) for row in ROWS}
    new_variables = sorted(
        {name for polynomial in affine.values() for monomial in polynomial for name, _ in monomial},
        key=lambda name: (parser.sigma_weight(name), name),
    )
    if any(parser.sigma_weight(name) != 16 for name in new_variables):
        fail(("new variable weight", new_variables))
    solved = solve_affine([affine[row] for row in ROWS], new_variables)

    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    coefficient_paths = {}
    coefficient_hashes = {}
    affine_paths = {}
    affine_hashes = {}
    for row in ROWS:
        name = f"Tg16_{row}"
        path = output / f"{name}_{label}.poly"
        path.write_text(v20.singular_text(face[row], args.characteristic) + "\n")
        coefficient_paths[name] = str(path)
        coefficient_hashes[name] = digest(path)
        affine_path = output / f"{name}_at_old_point_{label}.poly"
        affine_path.write_text(v20.singular_text(affine[row], args.characteristic) + "\n")
        affine_paths[name] = str(affine_path)
        affine_hashes[name] = digest(affine_path)

    all_variables = v20.variable_names(list(face.values()) + [old_face["Tg14_2"]])
    control = output / f"boundary_prolong_g16_{label}.sing"
    lines = [f"ring R={args.characteristic},({','.join(all_variables)}),dp;"]
    bad_point = {"a1": Fraction(1), "aa0": Fraction(1), "rs2": Fraction(-1, 3)}
    lines.append(f"poly Bad={v20.singular_text(old_face['Tg14_2'], args.characteristic)};")
    for variable in all_variables:
        lines.append(f"Bad=subst(Bad,{variable},{v20.coefficient_text(bad_point.get(variable, Fraction(0)), args.characteristic)});")
    expected_bad = Fraction(1, 32)
    lines.append(f"if (Bad-({v20.coefficient_text(expected_bad, args.characteristic)})!=0) {{ print(\"FAIL_POINT_CONTROL\"); quit; }}")
    lines.append('print("V28_POINT_CONTROL=1");')

    if solved["outcome"] == "consistent":
        extension = dict(OLD_POINT)
        extension.update(solved["solution"])
        for row in ROWS:
            if evaluate(face[row], extension):
                fail(("extension replay", row, evaluate(face[row], extension)))
            name = f"Tg16_{row}"
            lines.append(f"poly E_{name}={v20.singular_text(face[row], args.characteristic)};")
            for variable in all_variables:
                lines.append(f"E_{name}=subst(E_{name},{variable},{v20.coefficient_text(extension.get(variable, Fraction(0)), args.characteristic)});")
            lines.append(f"if (E_{name}!=0) {{ print(\"FAIL_EXTENSION_{name}\"); quit; }}")
            lines.append(f'print("V28_EXTENSION_{name}=1");')
        outcome_record = {
            "outcome": "consistent",
            "solution": {name: encode_fraction(value) for name, value in sorted(solved["solution"].items())},
            "extended_nonzero_point": {name: encode_fraction(value) for name, value in sorted(extension.items()) if value},
        }
    else:
        dual = solved["dual"]
        combination = {}
        for row, coefficient in zip(ROWS, dual):
            combination = base.poly_add(combination, base.poly_scale(coefficient, affine[row]))
        if combination != base.poly_const(1):
            fail(("dual replay", combination))
        terms = [
            f"({v20.coefficient_text(coefficient, args.characteristic)})*A_Tg16_{row}"
            for row, coefficient in zip(ROWS, dual) if coefficient
        ]
        for row in ROWS:
            lines.append(f"poly A_Tg16_{row}={v20.singular_text(affine[row], args.characteristic)};")
        lines.append(f"poly Dual={'+'.join(terms) if terms else '0'};")
        lines.append("if (Dual-1!=0) { print(\"FAIL_DUAL\"); quit; }")
        lines.append('print("V28_DUAL=1");')
        outcome_record = {
            "outcome": "inconsistent",
            "dual": {f"Tg16_{row}": encode_fraction(coefficient) for row, coefficient in zip(ROWS, dual) if coefficient},
        }
    lines += [f'print("V28_OUTCOME={solved["outcome"]}");', 'print("PASS_A1_BOUNDARY_PROLONG_G16_V28");', "quit;"]
    control.write_text("\n".join(lines) + "\n")

    result = {
        "status": "PASS-A1-BOUNDARY-PROLONG-G16-V28-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "preregistration_sha256": digest(PREREG),
        "v20_module_sha256": V20_SHA,
        "v23_parser_sha256": V23_PARSER_SHA,
        "v23_result_sha256": V23_RESULT_SHA,
        "tail_rows": 7,
        "tail_terms": sum(len(tails[str(row)]) for row in ROWS),
        "old_face_bridges": old_bridges,
        "old_point_zero_rows": old_point_zeros,
        "old_point": {name: encode_fraction(value) for name, value in sorted(OLD_POINT.items())},
        "new_variables": new_variables,
        "linear_rank": solved["rank"],
        "grade16_term_counts": {f"Tg16_{row}": len(face[row]) for row in ROWS},
        "grade16_affine_term_counts": {f"Tg16_{row}": len(affine[row]) for row in ROWS},
        "coefficient_paths": coefficient_paths,
        "coefficient_sha256": coefficient_hashes,
        "affine_paths": affine_paths,
        "affine_sha256": affine_hashes,
        "row_sha256": row_hashes,
        "control_script": str(control),
        "control_script_sha256": digest(control),
        **outcome_record,
        "scope": "literal ordered-a1 rho=0 actual-total source rows through grade 16 only",
    }
    result_path = output / "result.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("PASS-A1-BOUNDARY-PROLONG-G16-V28-COMPILER")
    print(f"OUTCOME={result['outcome']}")
    print(f"NEW_VARIABLES={len(new_variables)}")
    print(f"LINEAR_RANK={solved['rank']}")
    print(f"RESULT_SHA256={digest(result_path)}")


if __name__ == "__main__":
    main()

