#!/usr/bin/env python3
"""Compile the honest grade-seven newest-coefficient Fitting block."""

from __future__ import annotations

import argparse
import ast
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, permutations
import json
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V21 = ROOT / "cases/max12_812_order2_u2_62_k00_filtered_dual_local_nonmembership_v21_20260827/aws_q_box01_r1_pass/input"
PRELUDE = V21 / "prelude_Q.sing"
LOAD10 = V21 / "load_K10.txt"
LOAD6 = V21 / "load_K6.txt"
COLUMNS = ROOT / "cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/aws_r6b_r2_pass/output/SOURCE_COLUMNS.json"
V22_REPORT = ROOT / "cases/max12_812_order2_u2_62_k00_weighted_first_stratum_v22_20260827/RESULT_V22R1.md"
F10 = ROOT / "cases/max12_812_order2_u2_62_k00_weighted_first_stratum_v22_20260827/aws_r6b_r1_pass/output/F10_QUARTIC.txt"
PREREG = HERE / "PREREGISTRATION.md"
EXPECTED = {
    PREREG: "8928de6dd6666e075c1f719a22d627266fc3cca72ba5f83f5b4720d2f06e0fc0",
    PRELUDE: "5b0a77e6d16df30de2df344862fc4316aedcc8aeabf1ec81e23d7881ce67ee7a",
    LOAD10: "2ccdaa01fe7f1cf273b2fe539e03cc5387af5688dcf28a85ab37fbddd7ac96ea",
    LOAD6: "2e2c2274bbe51748a5178cccb1cb195561785687c580be79beee52ecc6e2d73d",
    COLUMNS: "2e8ceeb42dcc41752f82fe1df866c28b33e289097b065bf965db25574230919c",
    V22_REPORT: "494075c5675a2571808aec8606ed5744c2362bf3abc470304226b6fee699e293",
    F10: "c8e214ae21b058dddb063dcd7a9075a34b02a14f01f54386822cf85f0dc2c8e8",
}
NVAR = 6
ZERO = (0,) * NVAR
Key = tuple[int, int, int, int, int, int]
Poly = dict[Key, Fraction]


def fail(message: object) -> "None":
    raise RuntimeError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only V23 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only V23 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def add(left: Poly, right: Poly, scale: Fraction = Fraction(1)) -> Poly:
    out = dict(left)
    for key, value in right.items():
        out[key] = out.get(key, Fraction(0)) + scale * value
        if out[key] == 0:
            del out[key]
    return out


def multiply(left: Poly, right: Poly) -> Poly:
    out: Poly = {}
    for akey, avalue in left.items():
        for bkey, bvalue in right.items():
            key = tuple(a + b for a, b in zip(akey, bkey))
            out[key] = out.get(key, Fraction(0)) + avalue * bvalue
    return {key: value for key, value in out.items() if value}


def scale(poly: Poly, value: Fraction) -> Poly:
    return {key: value * coefficient for key, coefficient in poly.items() if value * coefficient}


def power(poly: Poly, exponent: int) -> Poly:
    out: Poly = {ZERO: Fraction(1)}
    base = poly
    while exponent:
        if exponent & 1:
            out = multiply(out, base)
        exponent >>= 1
        if exponent:
            base = multiply(base, base)
    return out


def eval_ast(node: ast.AST) -> Poly:
    if isinstance(node, ast.Constant) and isinstance(node.value, int):
        return {} if node.value == 0 else {ZERO: Fraction(node.value)}
    if isinstance(node, ast.Name) and re.fullmatch(r"d[0-5]", node.id):
        key = [0] * NVAR
        key[int(node.id[1])] = 1
        return {tuple(key): Fraction(1)}
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
        value = eval_ast(node.operand)
        return value if isinstance(node.op, ast.UAdd) else scale(value, Fraction(-1))
    if isinstance(node, ast.BinOp):
        if isinstance(node.op, ast.Add):
            return add(eval_ast(node.left), eval_ast(node.right))
        if isinstance(node.op, ast.Sub):
            return add(eval_ast(node.left), eval_ast(node.right), Fraction(-1))
        if isinstance(node.op, ast.Mult):
            return multiply(eval_ast(node.left), eval_ast(node.right))
        if isinstance(node.op, ast.Div):
            numerator, denominator = eval_ast(node.left), eval_ast(node.right)
            if set(denominator) != {ZERO} or denominator[ZERO] == 0:
                fail(("nonconstant denominator", ast.dump(node.right)))
            return scale(numerator, Fraction(1) / denominator[ZERO])
        if isinstance(node.op, ast.Pow):
            if not isinstance(node.right, ast.Constant) or not isinstance(node.right.value, int):
                fail(("noninteger exponent", ast.dump(node.right)))
            return power(eval_ast(node.left), node.right.value)
    fail(("unsupported syntax", ast.dump(node)))


def parse_poly(text: str) -> Poly:
    source = "".join(text.split())
    if not source or any(char in source for char in ';,"'):
        fail(("malformed polynomial", source[:100]))
    return eval_ast(ast.parse(source.replace("^", "**"), mode="eval").body)


def parse_rows() -> list[Poly]:
    text = PRELUDE.read_text()
    rows: list[Poly] = []
    for index in range(1, 8):
        match = re.search(rf"(?:^|\n)poly r{index}=(.*?);", text, re.S)
        if match is None:
            fail(("missing row", index))
        rows.append(parse_poly(match.group(1)))
    return rows


def parse_ideal(path: Path) -> list[Poly]:
    return [parse_poly(piece) for piece in "".join(path.read_text().split()).split(",")]


def homogeneous(poly: Poly, degree: int) -> Poly:
    return {key: value for key, value in poly.items() if sum(key) == degree}


def derivative(poly: Poly, variable: int) -> Poly:
    out: Poly = {}
    for key, value in poly.items():
        if key[variable]:
            new = list(key)
            factor = new[variable]
            new[variable] -= 1
            out[tuple(new)] = value * factor
    return out


def determinant(matrix: list[list[Poly]]) -> Poly:
    size = len(matrix)
    if any(len(row) != size for row in matrix):
        fail("nonsquare determinant")
    out: Poly = {}
    for permutation in permutations(range(size)):
        inversions = sum(permutation[i] > permutation[j]
                         for i in range(size) for j in range(i + 1, size))
        term: Poly = {ZERO: Fraction(-1 if inversions & 1 else 1)}
        for row, column in enumerate(permutation):
            term = multiply(term, matrix[row][column])
            if not term:
                break
        out = add(out, term)
    return out


def submatrix(matrix: list[list[Poly]], rows: tuple[int, ...], columns: tuple[int, ...]) -> list[list[Poly]]:
    return [[matrix[i][j] for j in columns] for i in rows]


def generic_rank(matrix: list[list[Poly]]) -> tuple[int, tuple[tuple[int, ...], tuple[int, ...]], Poly]:
    for size in range(min(len(matrix), len(matrix[0])), 0, -1):
        for rows in combinations(range(len(matrix)), size):
            for columns in combinations(range(len(matrix[0])), size):
                minor = determinant(submatrix(matrix, rows, columns))
                if minor:
                    return size, (rows, columns), minor
    return 0, ((), ()), {}


def poly_text(poly: Poly) -> str:
    if not poly:
        return "0"
    terms: list[str] = []
    for key, coefficient in sorted(poly.items()):
        factors = [f"x{i}^{e}" if e != 1 else f"x{i}" for i, e in enumerate(key) if e]
        body = "*".join(factors) or "1"
        ctext = str(coefficient.numerator) if coefficient.denominator == 1 else f"({coefficient.numerator}/{coefficient.denominator})"
        terms.append(f"({ctext})*{body}")
    return "+".join(terms).replace("+(-", "-(")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    tag = require_aws()
    for path, expected in EXPECTED.items():
        if digest(path) != expected:
            fail(("frozen input mismatch", str(path), digest(path), expected))

    columns = json.loads(COLUMNS.read_text())
    by_name = {entry["variable"]: entry for entry in columns}
    if len(columns) != 169 or by_name["k6_0"]["boundary_status"] != "FIXED_ZERO_BEFORE_SOLVE":
        fail("source column/boundary census")
    if by_name["k10_3"]["boundary_status"] != "FREE":
        fail("k10_3 is not free")

    rows = parse_rows()
    load10 = parse_ideal(LOAD10)
    load6 = parse_ideal(LOAD6)
    if len(rows) != 7 or len(load10) != 7 or len(load6) != 7:
        fail("seven-row source census")
    quadrics = [homogeneous(row, 2) for row in rows]
    if any(not quadrics[i] for i in (0, 1, 2, 3, 4, 6)) or quadrics[5]:
        fail("unexpected seven-row quadratic profile")
    k10_quadrics = [homogeneous(poly, 2) for poly in load10]
    if any(not poly for poly in k10_quadrics):
        fail("missing K10 quadratic load initial")
    k6_linears = [homogeneous(poly, 1) for poly in load6]
    if not any(k6_linears):
        fail("forbidden k6_0 mutation has zero grade-seven column")

    matrix = [[derivative(quadrics[row], column) for column in range(6)] + [k10_quadrics[row]]
              for row in range(7)]
    delta = determinant(matrix)
    rank, witness_indices, witness = generic_rank(matrix)
    if rank == 7 and not delta:
        fail("rank-seven witness but determinant zero")
    if rank < 7 and delta:
        fail("nonzero determinant but rank below seven")
    if rank == 7:
        branch = "GENERIC_RANK_7_NO_GRADE7_COMPATIBILITY_ON_OPEN_DET"
        cokernel_dimension = 0
    elif rank == 6:
        branch = "GENERIC_RANK_6_ONE_SCALAR_AUGMENTED_COMPATIBILITY_REMAINS"
        cokernel_dimension = 1
    else:
        branch = "GENERIC_RANK_LE5_HIGHER_FITTING_BLOCK_REMAINS"
        cokernel_dimension = 7 - rank

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    matrix_path = output / "GRADE7_NEWEST_MATRIX.txt"
    matrix_path.write_text("\n".join(",".join(poly_text(entry) for entry in row) for row in matrix) + "\n")
    k6_path = output / "FORBIDDEN_K6_0_COLUMN.txt"
    k6_path.write_text("\n".join(poly_text(poly) for poly in k6_linears) + "\n")
    delta_path = output / "GRADE7_DETERMINANT.txt"
    delta_path.write_text(poly_text(delta) + "\n")
    witness_path = output / "GENERIC_RANK_WITNESS_MINOR.txt"
    witness_path.write_text(poly_text(witness) + "\n")

    witness_rows, witness_columns = witness_indices
    lines = ["ring R=0,(x0,x1,x2,x3,x4,x5),dp;"]
    flat = [poly_text(entry) for row in matrix for entry in row]
    lines.append("matrix A[7][7]=" + ",".join(flat) + ";")
    lines.append("poly Dexpected=(" + poly_text(delta) + "); poly Dactual=det(A);")
    lines.append('if (Dactual-Dexpected!=0) { print("K00_V23_FAIL=DETERMINANT_REPLAY"); quit; }')
    if rank:
        selected = submatrix(matrix, witness_rows, witness_columns)
        lines.append(f"matrix W[{rank}][{rank}]=" + ",".join(poly_text(entry) for row in selected for entry in row) + ";")
        lines.append("poly Wexpected=(" + poly_text(witness) + "); poly Wactual=det(W);")
        lines.append('if ((Wactual-Wexpected!=0)||(Wactual==0)) { print("K00_V23_FAIL=WITNESS_MINOR_REPLAY"); quit; }')
    lines.extend([
        f'print("K00_V23_GENERIC_RANK={rank}");',
        f'print("K00_V23_BRANCH={branch}");',
        'print("K00_V23_ENDPOINT=PASS_EXACT_GRADE7_NEWEST_BLOCK");',
        "quit;",
    ])
    script = output / "grade7_newest_block_v23.sing"
    script.write_text("\n".join(lines) + "\n")
    singular = shutil.which("Singular")
    if singular is None:
        fail("Singular missing")
    completed = subprocess.run([singular, "-q", str(script)], cwd=output, text=True,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=1800)
    stdout = output / "singular.stdout"
    stderr = output / "singular.stderr"
    stdout.write_text(completed.stdout)
    stderr.write_text(completed.stderr)
    required = (f"K00_V23_GENERIC_RANK={rank}", f"K00_V23_BRANCH={branch}",
                "K00_V23_ENDPOINT=PASS_EXACT_GRADE7_NEWEST_BLOCK")
    if completed.returncode != 0 or any(marker not in completed.stdout for marker in required) or completed.stderr:
        fail(("Singular endpoint", completed.returncode, completed.stdout, completed.stderr))

    result = {
        "status": "PASS_EXACT_GRADE7_NEWEST_BLOCK",
        "registered_aws_lane": tag,
        "branch": branch,
        "generic_rank": rank,
        "generic_left_cokernel_dimension": cokernel_dimension,
        "rank_witness_rows_zero_based": list(witness_rows),
        "rank_witness_columns_zero_based": list(witness_columns),
        "matrix_sha256": digest(matrix_path),
        "determinant_sha256": digest(delta_path),
        "rank_witness_sha256": digest(witness_path),
        "forbidden_k6_column_sha256": digest(k6_path),
        "forbidden_k6_column_nonzero_mutation_detected": True,
        "honest_newest_variables": [*(f"d{i}_6" for i in range(6)), "k10_3"],
        "unit_condition": "k10_0=kappa!=0",
        "prior_candidate_stratum": "Q1=...=Q6=F10=0",
        "next_required_client": "CONTRACT_LITERAL_GRADE7_INHOMOGENEOUS_TERM_AGAINST_FULL_LEFT_COKERNEL_AND_REDUCE_MOD_PRIOR_HONEST_SOURCE_IDEAL",
        "input_sha256": {str(path.relative_to(ROOT)): digest(path) for path in EXPECTED},
        "scope": "GRADE7_NEWEST_VARIABLE_FITTING_BLOCK_ONLY_CONDITIONAL_ON_PRIOR_V22_PREFIX",
        "firewall": "NO_AUGMENTED_COMPATIBILITY_YET_NO_GRADES8_TO19_NO_FULL_JET_NO_ARC_NO_CLOSURE_NO_JC2",
    }
    result_path = output / "RESULT.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("K00_V23_PRODUCER=PASS")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
