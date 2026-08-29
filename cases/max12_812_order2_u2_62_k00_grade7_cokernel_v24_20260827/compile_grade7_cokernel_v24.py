#!/usr/bin/env python3
"""Compile the exact two-cokernel grade-seven compatibility equations."""

from __future__ import annotations

import argparse
import ast
from fractions import Fraction
from hashlib import sha256
from itertools import permutations
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
V20 = ROOT / "cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/aws_r6b_r2_pass/output"
DAG_PATH = V20 / "LITERAL_140_EQUATION_DAG.json"
COLUMNS_PATH = V20 / "SOURCE_COLUMNS.json"
V23 = ROOT / "cases/max12_812_order2_u2_62_k00_grade7_newest_block_v23_20260827/aws_r6b_pass/output"
MATRIX_PATH = V23 / "GRADE7_NEWEST_MATRIX.txt"
WITNESS_PATH = V23 / "GENERIC_RANK_WITNESS_MINOR.txt"
V23_RESULT = V23 / "RESULT.json"
F10_PATH = ROOT / "cases/max12_812_order2_u2_62_k00_weighted_first_stratum_v22_20260827/aws_r6b_r1_pass/output/F10_QUARTIC.txt"
PREREG = HERE / "PREREGISTRATION.md"
EXPECTED = {
    PREREG: "3e48bb009c82a1a988aca5f17a65f290f916e83a3fc1773252ef9b5b59227e0c",
    PRELUDE: "5b0a77e6d16df30de2df344862fc4316aedcc8aeabf1ec81e23d7881ce67ee7a",
    LOAD10: "2ccdaa01fe7f1cf273b2fe539e03cc5387af5688dcf28a85ab37fbddd7ac96ea",
    DAG_PATH: "b9bd2e2ca1319ee3107a0f7cf4e1750386d60bb12213a3a970c4812823abdce6",
    COLUMNS_PATH: "2e8ceeb42dcc41752f82fe1df866c28b33e289097b065bf965db25574230919c",
    MATRIX_PATH: "972ac0fa6fc0716bf2657cef6cb0ea0c6e4b3150f3f144f791818325f7e72af1",
    WITNESS_PATH: "957181065328c7ef930c6c400272f45ab93a055ff1069ced7f3cca8b3c89bbde",
    V23_RESULT: "3fb7ce922bd12bfe1102efa77d455e7a3a69e448b8eada291ddcfbe3585ec9e4",
    F10_PATH: "c8e214ae21b058dddb063dcd7a9075a34b02a14f01f54386822cf85f0dc2c8e8",
}
DVAR = 6
DZ = (0,) * DVAR
TRUNC = 8
FULL_VARS = [f"d{i}_{n}" for i in range(6) for n in range(1, 7)] + [f"k10_{n}" for n in range(4)]
NEW_VARS = [f"d{i}_6" for i in range(6)] + ["k10_3"]
PRIOR_VARS = [name for name in FULL_VARS if name not in NEW_VARS]
FULL_INDEX = {name: index for index, name in enumerate(FULL_VARS)}
NEW_INDEX = [FULL_INDEX[name] for name in NEW_VARS]
PRIOR_INDEX = {name: index for index, name in enumerate(PRIOR_VARS)}
FZ = (0,) * len(FULL_VARS)
PZ = (0,) * len(PRIOR_VARS)
DKey = tuple[int, int, int, int, int, int]
DPoly = dict[DKey, Fraction]
JKey = tuple[int, ...]
JPoly = dict[JKey, Fraction]


def fail(message: object) -> "None":
    raise RuntimeError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only V24 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only V24 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def padd(left: dict, right: dict, factor: Fraction = Fraction(1)) -> dict:
    out = dict(left)
    for key, value in right.items():
        out[key] = out.get(key, Fraction(0)) + factor * value
        if out[key] == 0:
            del out[key]
    return out


def pmul(left: dict, right: dict) -> dict:
    out: dict = {}
    for akey, avalue in left.items():
        for bkey, bvalue in right.items():
            key = tuple(a + b for a, b in zip(akey, bkey))
            out[key] = out.get(key, Fraction(0)) + avalue * bvalue
    return {key: value for key, value in out.items() if value}


def pscale(poly: dict, factor: Fraction) -> dict:
    return {key: factor * value for key, value in poly.items() if factor * value}


def ppow(poly: dict, exponent: int, zero_key: tuple[int, ...]) -> dict:
    out = {zero_key: Fraction(1)}
    base = poly
    while exponent:
        if exponent & 1:
            out = pmul(out, base)
        exponent >>= 1
        if exponent:
            base = pmul(base, base)
    return out


def eval_ast(node: ast.AST) -> DPoly:
    if isinstance(node, ast.Constant) and isinstance(node.value, int):
        return {} if node.value == 0 else {DZ: Fraction(node.value)}
    if isinstance(node, ast.Name) and re.fullmatch(r"[dx][0-5]", node.id):
        key = [0] * DVAR
        key[int(node.id[1])] = 1
        return {tuple(key): Fraction(1)}
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
        value = eval_ast(node.operand)
        return value if isinstance(node.op, ast.UAdd) else pscale(value, Fraction(-1))
    if isinstance(node, ast.BinOp):
        if isinstance(node.op, ast.Add):
            return padd(eval_ast(node.left), eval_ast(node.right))
        if isinstance(node.op, ast.Sub):
            return padd(eval_ast(node.left), eval_ast(node.right), Fraction(-1))
        if isinstance(node.op, ast.Mult):
            return pmul(eval_ast(node.left), eval_ast(node.right))
        if isinstance(node.op, ast.Div):
            numerator, denominator = eval_ast(node.left), eval_ast(node.right)
            if set(denominator) != {DZ} or denominator[DZ] == 0:
                fail(("nonconstant denominator", ast.dump(node.right)))
            return pscale(numerator, Fraction(1) / denominator[DZ])
        if isinstance(node.op, ast.Pow):
            if not isinstance(node.right, ast.Constant) or not isinstance(node.right.value, int):
                fail(("noninteger exponent", ast.dump(node.right)))
            return ppow(eval_ast(node.left), node.right.value, DZ)
    fail(("unsupported polynomial syntax", ast.dump(node)))


def parse_poly(text: str) -> DPoly:
    source = "".join(text.split())
    if not source or any(char in source for char in ';,"'):
        fail(("malformed polynomial", source[:100]))
    return eval_ast(ast.parse(source.replace("^", "**"), mode="eval").body)


def parse_rows() -> list[DPoly]:
    text = PRELUDE.read_text()
    rows: list[DPoly] = []
    for index in range(1, 8):
        match = re.search(rf"(?:^|\n)poly r{index}=(.*?);", text, re.S)
        if match is None:
            fail(("missing row", index))
        rows.append(parse_poly(match.group(1)))
    return rows


def parse_ideal(path: Path) -> list[DPoly]:
    return [parse_poly(piece) for piece in "".join(path.read_text().split()).split(",")]


def parse_matrix(path: Path) -> list[list[DPoly]]:
    rows = [[parse_poly(piece) for piece in line.split(",")] for line in path.read_text().splitlines() if line]
    if len(rows) != 7 or any(len(row) != 7 for row in rows):
        fail("V23 matrix census")
    return rows


def determinant(matrix: list[list[DPoly]]) -> DPoly:
    size = len(matrix)
    out: DPoly = {}
    for permutation in permutations(range(size)):
        inversions = sum(permutation[i] > permutation[j]
                         for i in range(size) for j in range(i + 1, size))
        term: DPoly = {DZ: Fraction(-1 if inversions & 1 else 1)}
        for row, column in enumerate(permutation):
            term = pmul(term, matrix[row][column])
            if not term:
                break
        out = padd(out, term)
    return out


def series_add(left: list[JPoly], right: list[JPoly]) -> list[JPoly]:
    return [padd(a, b) for a, b in zip(left, right)]


def series_mul(left: list[JPoly], right: list[JPoly]) -> list[JPoly]:
    out: list[JPoly] = [{} for _ in range(TRUNC)]
    for i, a in enumerate(left):
        if not a:
            continue
        for j, b in enumerate(right[:TRUNC - i]):
            if b:
                out[i + j] = padd(out[i + j], pmul(a, b))
    return out


def series_power(series: list[JPoly], exponent: int) -> list[JPoly]:
    out: list[JPoly] = [{} for _ in range(TRUNC)]
    out[0] = {FZ: Fraction(1)}
    base = series
    while exponent:
        if exponent & 1:
            out = series_mul(out, base)
        exponent >>= 1
        if exponent:
            base = series_mul(base, base)
    return out


def eval_dpoly_series(poly: DPoly, variables: list[list[JPoly]]) -> list[JPoly]:
    out: list[JPoly] = [{} for _ in range(TRUNC)]
    powers: dict[tuple[int, int], list[JPoly]] = {}
    for key, coefficient in poly.items():
        term: list[JPoly] = [{} for _ in range(TRUNC)]
        term[0] = {FZ: coefficient}
        for index, exponent in enumerate(key):
            if exponent:
                cache = (index, exponent)
                if cache not in powers:
                    powers[cache] = series_power(variables[index], exponent)
                term = series_mul(term, powers[cache])
        out = series_add(out, term)
    return out


def source_series() -> tuple[list[list[JPoly]], list[JPoly]]:
    dseries: list[list[JPoly]] = []
    for i in range(6):
        series: list[JPoly] = [{} for _ in range(TRUNC)]
        for n in range(1, 7):
            key = [0] * len(FULL_VARS)
            key[FULL_INDEX[f"d{i}_{n}"]] = 1
            series[n] = {tuple(key): Fraction(1)}
        dseries.append(series)
    kseries: list[JPoly] = [{} for _ in range(TRUNC)]
    for n in range(4):
        key = [0] * len(FULL_VARS)
        key[FULL_INDEX[f"k10_{n}"]] = 1
        kseries[n] = {tuple(key): Fraction(1)}
    return dseries, kseries


def shift(series: list[JPoly], amount: int) -> list[JPoly]:
    return [{} for _ in range(amount)] + series[:TRUNC - amount]


def full_to_prior(poly: JPoly) -> JPoly:
    out: JPoly = {}
    for key, value in poly.items():
        if any(key[index] for index in NEW_INDEX):
            fail("newest variable survived prior projection")
        pkey = tuple(key[FULL_INDEX[name]] for name in PRIOR_VARS)
        out[pkey] = out.get(pkey, Fraction(0)) + value
    return {key: value for key, value in out.items() if value}


def extract_affine(poly: JPoly) -> tuple[JPoly, list[JPoly]]:
    constant: JPoly = {}
    coefficients: list[JPoly] = [{} for _ in NEW_VARS]
    for key, value in poly.items():
        degrees = [key[index] for index in NEW_INDEX]
        if sum(degrees) > 1 or any(degree not in (0, 1) for degree in degrees):
            fail(("grade-seven system nonlinear in newest variables", degrees))
        mutable = list(key)
        if sum(degrees) == 0:
            pkey = tuple(mutable[FULL_INDEX[name]] for name in PRIOR_VARS)
            constant[pkey] = constant.get(pkey, Fraction(0)) + value
        else:
            position = degrees.index(1)
            mutable[NEW_INDEX[position]] = 0
            pkey = tuple(mutable[FULL_INDEX[name]] for name in PRIOR_VARS)
            coefficients[position][pkey] = coefficients[position].get(pkey, Fraction(0)) + value
    return ({key: value for key, value in constant.items() if value},
            [{key: value for key, value in poly.items() if value} for poly in coefficients])


def dpoly_to_prior(poly: DPoly) -> JPoly:
    out: JPoly = {}
    for key, value in poly.items():
        pkey = [0] * len(PRIOR_VARS)
        for i, exponent in enumerate(key):
            pkey[PRIOR_INDEX[f"d{i}_1"]] = exponent
        out[tuple(pkey)] = value
    return out


def prior_to_dpoly(poly: JPoly) -> DPoly:
    out: DPoly = {}
    allowed = {PRIOR_INDEX[f"d{i}_1"] for i in range(6)}
    for key, value in poly.items():
        if any(exponent and index not in allowed for index, exponent in enumerate(key)):
            fail("newest coefficient depends on non-leading prior jet")
        dkey = tuple(key[PRIOR_INDEX[f"d{i}_1"]] for i in range(6))
        out[dkey] = out.get(dkey, Fraction(0)) + value
    return {key: value for key, value in out.items() if value}


def evaluate(poly: JPoly, assignment: dict[str, object], modulus: int | None = None) -> object:
    total: object = 0
    for key, coefficient in poly.items():
        if modulus:
            value: object = coefficient.numerator * pow(coefficient.denominator, -1, modulus) % modulus
        else:
            value = coefficient
        for index, exponent in enumerate(key):
            if exponent:
                value *= assignment[PRIOR_VARS[index]] ** exponent
                if modulus:
                    value %= modulus
        total += value
        if modulus:
            total %= modulus
    return total


def evaluate_full(poly: JPoly, assignment: dict[str, object], modulus: int | None = None) -> object:
    total: object = 0
    for key, coefficient in poly.items():
        if modulus:
            value: object = coefficient.numerator * pow(coefficient.denominator, -1, modulus) % modulus
        else:
            value = coefficient
        for index, exponent in enumerate(key):
            if exponent:
                value *= assignment[FULL_VARS[index]] ** exponent
                if modulus:
                    value %= modulus
        total += value
        if modulus:
            total %= modulus
    return total


def evaluate_literal_dag(data: dict, assignment: dict[str, object], modulus: int | None) -> list[object]:
    values: list[object] = []
    for node in data["nodes"]:
        if node[0] == "c":
            fraction = Fraction(int(node[1]), int(node[2]))
            value: object = (fraction.numerator * pow(fraction.denominator, -1, modulus) % modulus
                             if modulus else fraction)
        elif node[0] == "v":
            value = assignment[str(node[1])]
        elif node[0] == "a":
            value = values[int(node[1])] + values[int(node[2])]
        elif node[0] == "m":
            value = values[int(node[1])] * values[int(node[2])]
        else:
            fail(("unknown DAG opcode", node))
        values.append(value % modulus if modulus else value)
    return values


def fixture(columns: list[dict[str, object]], seed: int, modulus: int | None) -> dict[str, object]:
    out: dict[str, object] = {}
    for column in columns:
        name = str(column["variable"])
        raw = int.from_bytes(sha256(f"V24|{seed}|{name}".encode()).digest()[:4], "big")
        value = raw % 11 - 5
        if column["boundary_status"] != "FREE":
            value = 0
        out[name] = value % modulus if modulus else Fraction(value)
    out["k10_0"] = (seed + 1) % modulus if modulus else Fraction(seed + 1)
    return out


def poly_text(poly: JPoly) -> str:
    if not poly:
        return "0"
    terms: list[str] = []
    for key, coefficient in sorted(poly.items()):
        factors = [f"{PRIOR_VARS[i]}^{e}" if e != 1 else PRIOR_VARS[i]
                   for i, e in enumerate(key) if e]
        body = "*".join(factors) or "1"
        ctext = str(coefficient.numerator) if coefficient.denominator == 1 else f"({coefficient.numerator}/{coefficient.denominator})"
        terms.append(f"({ctext})*{body}")
    return "+".join(terms).replace("+(-", "-(")


def write_polys(path: Path, names: list[str], polys: list[JPoly]) -> None:
    path.write_text("\n".join(f"{name}={poly_text(poly)}" for name, poly in zip(names, polys)) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    tag = require_aws()
    for path, expected in EXPECTED.items():
        if digest(path) != expected:
            fail(("frozen input mismatch", str(path), digest(path), expected))

    rows = parse_rows()
    loads = parse_ideal(LOAD10)
    matrix = parse_matrix(MATRIX_PATH)
    v23 = json.loads(V23_RESULT.read_text())
    if v23["generic_rank"] != 5 or v23["rank_witness_rows_zero_based"] != [0, 1, 2, 3, 4] or v23["rank_witness_columns_zero_based"] != [0, 1, 2, 3, 6]:
        fail("V23 rank/chart mismatch")
    pivot_rows = (0, 1, 2, 3, 4)
    pivot_columns = (0, 1, 2, 3, 6)
    pivot = [[matrix[i][j] for j in pivot_columns] for i in pivot_rows]
    witness = determinant(pivot)
    if witness != parse_poly(WITNESS_PATH.read_text()) or not witness:
        fail("V23 witness minor replay")

    left: list[list[DPoly]] = []
    for extra_row in (5, 6):
        covector: list[DPoly] = [{} for _ in range(7)]
        covector[extra_row] = witness
        replacement = [matrix[extra_row][j] for j in pivot_columns]
        for position, row in enumerate(pivot_rows):
            changed = [list(entries) for entries in pivot]
            changed[position] = replacement
            covector[row] = pscale(determinant(changed), Fraction(-1))
        for column in range(7):
            identity: DPoly = {}
            for row in range(7):
                identity = padd(identity, pmul(covector[row], matrix[row][column]))
            if identity:
                fail(("left-kernel identity", extra_row, column, len(identity)))
        left.append(covector)
    wrong = [dict(poly) for poly in left[0]]
    mutation_position = next((index for index, poly in enumerate(wrong) if poly), None)
    if mutation_position is None:
        fail("empty left-kernel vector")
    wrong[mutation_position] = pscale(wrong[mutation_position], Fraction(-1))
    wrong_nonzero = False
    for column in range(7):
        identity: DPoly = {}
        for row in range(7):
            identity = padd(identity, pmul(wrong[row], matrix[row][column]))
        if identity:
            wrong_nonzero = True
    if not wrong_nonzero:
        fail("left-kernel sign mutation survived")

    dseries, kseries = source_series()
    row_series = [eval_dpoly_series(poly, dseries) for poly in rows]
    load_series = [eval_dpoly_series(poly, dseries) for poly in loads]
    weighted_k = shift(kseries, 2)
    phi = [series_add(row_series[i], series_mul(weighted_k, load_series[i])) for i in range(7)]
    grade7 = [series[7] for series in phi]
    affine = [extract_affine(poly) for poly in grade7]
    b = [item[0] for item in affine]
    extracted_matrix = [[prior_to_dpoly(item[1][column]) for column in range(7)] for item in affine]
    if extracted_matrix != matrix:
        fail("literal grade-seven matrix differs from V23")
    prior_equations = [full_to_prior(phi[row][grade]) for grade in range(2, 7) for row in range(7)]
    f10 = dpoly_to_prior(parse_poly(F10_PATH.read_text()))

    compatibility: list[JPoly] = []
    for covector in left:
        relation: JPoly = {}
        for row in range(7):
            relation = padd(relation, pmul(dpoly_to_prior(covector[row]), b[row]))
        compatibility.append(relation)
    if any(not poly for poly in compatibility):
        fail("raw compatibility polynomial vanished")

    dag_data = json.loads(DAG_PATH.read_text())
    columns = json.loads(COLUMNS_PATH.read_text())
    roots = {(int(entry["row"]), int(entry["Lambda_grade"])): int(entry["node"])
             for entry in dag_data["roots"]}
    fixture_audit: list[dict[str, object]] = []
    for seed, modulus in ((1, None), (2, None), (3, 65521), (4, 65521)):
        assignment = fixture(columns, seed, modulus)
        values = evaluate_literal_dag(dag_data, assignment, modulus)
        for row in range(7):
            for grade in range(2, 8):
                reconstructed = evaluate_full(phi[row][grade], assignment, modulus)
                literal = values[roots[(row + 1, grade)]]
                if reconstructed != literal:
                    fail(("literal DAG replay", seed, modulus, row + 1, grade, reconstructed, literal))
        fixture_audit.append({"seed": seed, "field": "Q" if modulus is None else f"F_{modulus}",
                              "all_42_coefficients_match": True})

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    b_path = output / "GRADE7_INHOMOGENEOUS_B.txt"
    write_polys(b_path, [f"b{i}" for i in range(1, 8)], b)
    left_path = output / "LEFT_COKERNEL_BASIS.txt"
    left_prior = [dpoly_to_prior(poly) for covector in left for poly in covector]
    write_polys(left_path, [f"L{basis + 1}_{row + 1}" for basis in range(2) for row in range(7)], left_prior)
    compatibility_path = output / "GRADE7_COMPATIBILITY_C6_C7.txt"
    write_polys(compatibility_path, ["C6", "C7"], compatibility)
    prior_path = output / "PRIOR_GRADE2_TO6_EQUATIONS.txt"
    write_polys(prior_path, [f"P_r{row}_g{grade}" for grade in range(2, 7) for row in range(1, 8)], prior_equations)
    fixture_path = output / "LITERAL_DAG_REPLAY.json"
    fixture_path.write_text(json.dumps(fixture_audit, sort_keys=True, indent=2) + "\n")

    # Bounded diagnostic only: modular normal forms on the W*k10_0 chart.
    nonzero_prior = [poly for poly in prior_equations if poly]
    w_prior = dpoly_to_prior(witness)
    singular_lines = [f"ring R=65521,({','.join(PRIOR_VARS)},zinv),dp;"]
    singular_lines.append("ideal P=" + ",".join(f"({poly_text(poly)})" for poly in nonzero_prior + [f10]) + ";")
    singular_lines.append(f"P=P,zinv*k10_0*({poly_text(w_prior)})-1;")
    singular_lines.append("ideal G=std(P);")
    singular_lines.append(f"poly C6=({poly_text(compatibility[0])}); poly C7=({poly_text(compatibility[1])});")
    singular_lines.extend([
        "poly N6=reduce(C6,G); poly N7=reduce(C7,G);",
        'write("MODULAR_C6_NORMAL_FORM.txt",N6); write("MODULAR_C7_NORMAL_FORM.txt",N7);',
        'print("K00_V24_MOD_C6_ZERO="+string(N6==0));',
        'print("K00_V24_MOD_C7_ZERO="+string(N7==0));',
        'print("K00_V24_MODULAR_REDUCTION=PASS");',
        "quit;",
    ])
    modular_script = output / "modular_prior_reduction_v24.sing"
    modular_script.write_text("\n".join(singular_lines) + "\n")
    singular = shutil.which("Singular")
    if singular is None:
        fail("Singular missing")
    modular_status = "NOT_RUN"
    try:
        completed = subprocess.run([singular, "-q", str(modular_script)], cwd=output, text=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=900)
        (output / "modular.stdout").write_text(completed.stdout)
        (output / "modular.stderr").write_text(completed.stderr)
        if completed.returncode == 0 and "K00_V24_MODULAR_REDUCTION=PASS" in completed.stdout and not completed.stderr:
            match6 = re.search(r"K00_V24_MOD_C6_ZERO=([01])", completed.stdout)
            match7 = re.search(r"K00_V24_MOD_C7_ZERO=([01])", completed.stdout)
            if match6 is None or match7 is None:
                fail("missing modular normal-form markers")
            modular_status = f"F65521_C6_ZERO_{match6.group(1)}_C7_ZERO_{match7.group(1)}"
        else:
            modular_status = f"MODULAR_ENGINE_DIAGNOSTIC_RC_{completed.returncode}"
    except subprocess.TimeoutExpired as error:
        (output / "modular.stdout").write_text(error.stdout or "")
        (output / "modular.stderr").write_text(error.stderr or "")
        modular_status = "MODULAR_REDUCTION_RESOURCE_CAP_900S"

    result = {
        "status": "PASS_EXACT_TWO_COMPATIBILITY_POLYNOMIALS_MODULAR_REDUCTION_RECORDED",
        "registered_aws_lane": tag,
        "chart": "k10_0_NONZERO_AND_W_NONZERO",
        "pivot_rows_zero_based": list(pivot_rows),
        "pivot_columns_zero_based": list(pivot_columns),
        "left_cokernel_dimension": 2,
        "witness_minor_terms": len(witness),
        "grade7_b_term_counts": [len(poly) for poly in b],
        "compatibility_term_counts": [len(poly) for poly in compatibility],
        "prior_nonzero_equations": len(nonzero_prior),
        "left_kernel_exact": True,
        "left_kernel_sign_mutation_detected": True,
        "literal_dag_replay": "42_coefficients_x_4_fixtures_exact_and_F65521",
        "modular_reduction_status": modular_status,
        "modular_reduction_scope": "DIAGNOSTIC_ONLY_NO_Q_MEMBERSHIP_INFERENCE",
        "artifacts": {path.name: {"sha256": digest(path), "bytes": path.stat().st_size} for path in
                      (b_path, left_path, compatibility_path, prior_path, fixture_path, modular_script)},
        "input_sha256": {str(path.relative_to(ROOT)): digest(path) for path in EXPECTED},
        "scope": "EXACT_GRADE7_TWO_COMPATIBILITY_POLYNOMIALS_ON_SINGLE_RANK5_CHART_ONLY",
        "firewall": "NO_W_ZERO_CHART_NO_GRADES8_TO19_NO_FULL_JET_NO_ARC_NO_CLOSURE_NO_JC2",
    }
    result_path = output / "RESULT.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("K00_V24_PRODUCER=PASS")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
