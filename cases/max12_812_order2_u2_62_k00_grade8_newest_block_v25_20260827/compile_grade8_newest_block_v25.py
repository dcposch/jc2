#!/usr/bin/env python3
"""Compile the honest grade-eight newest-coefficient Fitting block."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V24_CASE = ROOT / "cases/max12_812_order2_u2_62_k00_grade7_cokernel_v24_20260827"
V24_COMPILER = V24_CASE / "compile_grade7_cokernel_v24.py"
V24_REPORT = V24_CASE / "RESULT_V24.md"
V23_OUTPUT = ROOT / "cases/max12_812_order2_u2_62_k00_grade7_newest_block_v23_20260827/aws_r6b_pass/output"
MATRIX = V23_OUTPUT / "GRADE7_NEWEST_MATRIX.txt"
WITNESS = V23_OUTPUT / "GENERIC_RANK_WITNESS_MINOR.txt"
V23_RESULT = V23_OUTPUT / "RESULT.json"
V21_INPUT = ROOT / "cases/max12_812_order2_u2_62_k00_filtered_dual_local_nonmembership_v21_20260827/aws_q_box01_r1_pass/input"
LOAD6 = V21_INPUT / "load_K6.txt"
V20_OUTPUT = ROOT / "cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/aws_r6b_r2_pass/output"
COLUMNS = V20_OUTPUT / "SOURCE_COLUMNS.json"
DAG = V20_OUTPUT / "LITERAL_140_EQUATION_DAG.json"
PREREG = HERE / "PREREGISTRATION.md"
EXPECTED = {
    PREREG: "d9bb55bcc0d41738d4324b81b9c706d1be316de47d74eafc499120689b5020ce",
    V24_COMPILER: "1652cf3f2cefff9490062aade6e4c5be1c20b82cbefa01a7ef8a039530c39022",
    V24_REPORT: "6ed1163e56518e317d7fbb49eb9d107dc5b67e626830427a0a5d336d05f71df9",
    MATRIX: "972ac0fa6fc0716bf2657cef6cb0ea0c6e4b3150f3f144f791818325f7e72af1",
    WITNESS: "957181065328c7ef930c6c400272f45ab93a055ff1069ced7f3cca8b3c89bbde",
    V23_RESULT: "3fb7ce922bd12bfe1102efa77d455e7a3a69e448b8eada291ddcfbe3585ec9e4",
    LOAD6: "2e2c2274bbe51748a5178cccb1cb195561785687c580be79beee52ecc6e2d73d",
    COLUMNS: "2e8ceeb42dcc41752f82fe1df866c28b33e289097b065bf965db25574230919c",
    DAG: "b9bd2e2ca1319ee3107a0f7cf4e1750386d60bb12213a3a970c4812823abdce6",
}


def fail(message: object) -> "None":
    raise RuntimeError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only V25 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only V25 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_v24_module():
    spec = importlib.util.spec_from_file_location("frozen_v24_compiler", V24_COMPILER)
    if spec is None or spec.loader is None:
        fail("cannot import frozen V24 parser")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def homogeneous(poly: dict, degree: int) -> dict:
    return {key: value for key, value in poly.items() if sum(key) == degree}


def dpoly_text(poly: dict) -> str:
    if not poly:
        return "0"
    terms: list[str] = []
    for key, coefficient in sorted(poly.items()):
        factors = [f"x{i}^{exponent}" if exponent != 1 else f"x{i}"
                   for i, exponent in enumerate(key) if exponent]
        body = "*".join(factors) or "1"
        ctext = (str(coefficient.numerator) if coefficient.denominator == 1
                 else f"({coefficient.numerator}/{coefficient.denominator})")
        terms.append(f"({ctext})*{body}")
    return "+".join(terms).replace("+(-", "-(")


def eval_poly(poly: dict, x: list[object], modulus: int | None) -> object:
    total: object = 0
    for key, coefficient in poly.items():
        value: object = (coefficient.numerator * pow(coefficient.denominator, -1, modulus) % modulus
                         if modulus else coefficient)
        for index, exponent in enumerate(key):
            if exponent:
                value *= x[index] ** exponent
                if modulus:
                    value %= modulus
        total += value
        if modulus:
            total %= modulus
    return total


def eval_dag(data: dict, assignment: dict[str, object], modulus: int | None) -> list[object]:
    values: list[object] = []
    for node in data["nodes"]:
        if node[0] == "c":
            coefficient = Fraction(int(node[1]), int(node[2]))
            value: object = (coefficient.numerator * pow(coefficient.denominator, -1, modulus) % modulus
                             if modulus else coefficient)
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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    tag = require_aws()
    for path, expected in EXPECTED.items():
        if digest(path) != expected:
            fail(("frozen input mismatch", str(path), digest(path), expected))
    v24 = load_v24_module()

    columns = json.loads(COLUMNS.read_text())
    by_variable = {str(entry["variable"]): entry for entry in columns}
    required_free = [*(f"d{i}_7" for i in range(6)), "k10_4", "k6_1"]
    if any(by_variable[name]["boundary_status"] != "FREE" for name in required_free):
        fail("grade-eight newest source variable is not free")
    fixed_before_solve = ["k6_0", "k2_0", "mu2_0", "mu4_0", "mu6_0"]
    if any(by_variable[name]["boundary_status"] != "FIXED_ZERO_BEFORE_SOLVE"
           for name in fixed_before_solve):
        fail("honest boundary restriction census mismatch")
    if by_variable["k6_0"]["first_Lambda_grade"] != 6 or by_variable["k6_1"]["first_Lambda_grade"] != 7:
        fail("K6 weighted-order metadata mismatch")

    old_matrix = v24.parse_matrix(MATRIX)
    v23_result = json.loads(V23_RESULT.read_text())
    pivot_rows = tuple(v23_result["rank_witness_rows_zero_based"])
    pivot_columns = tuple(v23_result["rank_witness_columns_zero_based"])
    if v23_result["generic_rank"] != 5 or pivot_rows != (0, 1, 2, 3, 4) or pivot_columns != (0, 1, 2, 3, 6):
        fail("V23 exact rank-five chart mismatch")
    pivot = [[old_matrix[i][j] for j in pivot_columns] for i in pivot_rows]
    witness = v24.determinant(pivot)
    if not witness or witness != v24.parse_poly(WITNESS.read_text()):
        fail("V23 pivot minor failed exact replay")

    loads6 = v24.parse_ideal(LOAD6)
    if len(loads6) != 7:
        fail("K6 seven-row census")
    k6_column = [homogeneous(poly, 1) for poly in loads6]
    if not any(k6_column):
        fail("K6 linear initial is zero")
    matrix = [old_matrix[row] + [k6_column[row]] for row in range(7)]

    extension_columns = pivot_columns + (7,)
    extension_minors: list[dict] = []
    extension_rows: list[tuple[int, ...]] = []
    for extra_row in (5, 6):
        rows = pivot_rows + (extra_row,)
        extension_rows.append(rows)
        extension_minors.append(v24.determinant([[matrix[i][j] for j in extension_columns] for i in rows]))
    nonzero_positions = [index for index, minor in enumerate(extension_minors) if minor]
    if nonzero_positions:
        rank = 6
        chosen = nonzero_positions[0]
        branch = "PASS_EXACT_GRADE8_RANK6_ONE_COMPATIBILITY_REMAINS"
    else:
        rank = 5
        chosen = None
        branch = "PASS_EXACT_GRADE8_RANK5_TWO_COMPATIBILITIES_REMAIN"

    dag = json.loads(DAG.read_text())
    roots = {(int(entry["row"]), int(entry["Lambda_grade"])): int(entry["node"])
             for entry in dag["roots"]}
    names = [str(entry["variable"]) for entry in columns]
    fixture_audit: list[dict[str, object]] = []
    sign_mutation_detected = False
    for seed, modulus in ((2, None), (5, None), (7, 65521), (11, 65521)):
        base: dict[str, object] = {name: 0 for name in names}
        x: list[object] = []
        for i in range(6):
            raw = seed + 2 * i + 1
            value: object = raw % modulus if modulus else Fraction(raw)
            base[f"d{i}_1"] = value
            x.append(value)
        values0 = eval_dag(dag, base, modulus)
        allowed = dict(base)
        allowed["k6_1"] = 1
        values1 = eval_dag(dag, allowed, modulus)
        forbidden = dict(base)
        forbidden["k6_0"] = 1
        values_forbidden = eval_dag(dag, forbidden, modulus)
        for row in range(7):
            expected = eval_poly(k6_column[row], x, modulus)
            observed8 = values1[roots[(row + 1, 8)]] - values0[roots[(row + 1, 8)]]
            observed7 = values_forbidden[roots[(row + 1, 7)]] - values0[roots[(row + 1, 7)]]
            if modulus:
                observed8 %= modulus
                observed7 %= modulus
            if observed8 != expected or observed7 != expected:
                fail(("literal K6 column replay", seed, modulus, row + 1,
                      observed8, observed7, expected))
            if expected and ((-expected) % modulus if modulus else -expected) != observed8:
                sign_mutation_detected = True
        fixture_audit.append({"seed": seed, "field": "Q" if modulus is None else f"F_{modulus}",
                              "allowed_k6_1_grade8_matches": True,
                              "forbidden_k6_0_grade7_matches_same_initial": True})
    if not sign_mutation_detected:
        fail("K6 sign mutation was not detected")

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    matrix_path = output / "GRADE8_NEWEST_MATRIX.txt"
    matrix_path.write_text("\n".join(",".join(dpoly_text(entry) for entry in row) for row in matrix) + "\n")
    column_path = output / "ALLOWED_K6_1_COLUMN.txt"
    column_path.write_text("\n".join(dpoly_text(poly) for poly in k6_column) + "\n")
    extensions_path = output / "GRADE8_EXTENSION_MINORS.txt"
    extensions_path.write_text("\n".join(f"U{index + 1}={dpoly_text(poly)}"
                                          for index, poly in enumerate(extension_minors)) + "\n")
    witness_path = output / "GENERIC_RANK_WITNESS_MINOR.txt"
    witness_path.write_text((dpoly_text(extension_minors[chosen]) if chosen is not None else "0") + "\n")
    fixture_path = output / "LITERAL_K6_COLUMN_REPLAY.json"
    fixture_path.write_text(json.dumps(fixture_audit, sort_keys=True, indent=2) + "\n")

    lines = ["ring R=0,(x0,x1,x2,x3,x4,x5),dp;"]
    for index, (rows, minor) in enumerate(zip(extension_rows, extension_minors), 1):
        selected = [[matrix[i][j] for j in extension_columns] for i in rows]
        lines.append(f"matrix M{index}[6][6]=" + ",".join(dpoly_text(entry) for row in selected for entry in row) + ";")
        lines.append(f"poly U{index}=({dpoly_text(minor)}); poly V{index}=det(M{index});")
        lines.append(f'if (U{index}-V{index}!=0) {{ print("K00_V25_FAIL=MINOR_{index}"); quit; }}')
    lines.extend([
        f'print("K00_V25_GENERIC_RANK={rank}");',
        f'print("K00_V25_BRANCH={branch}");',
        'print("K00_V25_ENDPOINT=PASS");',
        "quit;",
    ])
    script = output / "grade8_newest_block_v25.sing"
    script.write_text("\n".join(lines) + "\n")
    singular = shutil.which("Singular")
    if singular is None:
        fail("Singular missing")
    completed = subprocess.run([singular, "-q", str(script)], cwd=output,
                               text=True, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, timeout=900)
    (output / "singular.stdout").write_text(completed.stdout)
    (output / "singular.stderr").write_text(completed.stderr)
    markers = (f"K00_V25_GENERIC_RANK={rank}", f"K00_V25_BRANCH={branch}",
               "K00_V25_ENDPOINT=PASS")
    if completed.returncode != 0 or completed.stderr or any(marker not in completed.stdout for marker in markers):
        fail(("Singular endpoint failure", completed.returncode, completed.stdout, completed.stderr))

    chosen_rows = list(extension_rows[chosen]) if chosen is not None else []
    chosen_sha = digest(witness_path) if chosen is not None else None
    payload = {
        "status": branch,
        "registered_aws_lane": tag,
        "generic_rank": rank,
        "generic_left_cokernel_dimension": 7 - rank,
        "conditional_chart": "V24_PREFIX_AND_W_NONZERO" + ("_AND_CHOSEN_U_NONZERO" if chosen is not None else ""),
        "v23_pivot_rows_zero_based": list(pivot_rows),
        "v23_pivot_columns_zero_based": list(pivot_columns),
        "extension_columns_zero_based": list(extension_columns),
        "chosen_extension_rows_zero_based": chosen_rows,
        "chosen_extension_minor_sha256": chosen_sha,
        "matrix_sha256": digest(matrix_path),
        "allowed_k6_1_column_sha256": digest(column_path),
        "extension_minors_sha256": digest(extensions_path),
        "generic_rank_witness_artifact_sha256": digest(witness_path),
        "literal_replay_sha256": digest(fixture_path),
        "literal_exact_and_modular_replay": True,
        "k6_sign_mutation_detected": True,
        "omitting_k6_1_replays_v23_rank": 5,
        "honest_newest_variables": required_free,
        "fixed_before_solve": fixed_before_solve,
        "input_sha256": {str(path.relative_to(ROOT)): digest(path) for path in EXPECTED},
        "next_required_client": "CONTRACT_LITERAL_GRADE8_INHOMOGENEOUS_TERM_AGAINST_COMPLETE_LEFT_COKERNEL",
        "scope": "GRADE8_NEWEST_VARIABLE_FITTING_BLOCK_ONLY_CONDITIONAL_ON_FULL_V24_PREFIX",
        "firewall": "NO_GRADE8_AUGMENTED_RELATION_NO_PREFIX_EXISTENCE_NO_OTHER_CHARTS_NO_GRADES9TO19_NO_FULL_JET_NO_ARC_NO_CLOSURE_NO_JC2",
    }
    (output / "RESULT.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print("K00_V25_PRODUCER=PASS")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
