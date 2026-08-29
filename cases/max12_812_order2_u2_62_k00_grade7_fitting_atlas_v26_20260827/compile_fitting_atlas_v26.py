#!/usr/bin/env python3
"""Compile the exact, chart-free grade-seven Fitting atlas.

This producer deliberately does no Groebner or saturation computation.  It
reconstructs the finite system directly from the frozen V20R2 arithmetic DAG,
checks the earlier V23/V24 serializations only after reconstruction, emits a
canonical determinant DAG, and writes immutable inputs for separately capped
exact-Q jobs.  All such jobs remain held until a reviewed exact-Q V24R2
endpoint is supplied.
"""

from __future__ import annotations

import argparse
import ast
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
import json
import os
from pathlib import Path
import platform
import re
from typing import Iterable, Iterator, Sequence


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V20 = ROOT / "cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/aws_r6b_r2_pass/output"
V21_INPUT = ROOT / "cases/max12_812_order2_u2_62_k00_filtered_dual_local_nonmembership_v21_20260827/aws_q_box01_r1_pass/input"
V22 = ROOT / "cases/max12_812_order2_u2_62_k00_weighted_first_stratum_v22_20260827"
V23 = ROOT / "cases/max12_812_order2_u2_62_k00_grade7_newest_block_v23_20260827/aws_r6b_pass/output"
V24 = ROOT / "cases/max12_812_order2_u2_62_k00_grade7_cokernel_v24_20260827/aws_r6b_pass/output"

PREREG = HERE / "PREREGISTRATION.md"
DAG_PATH = V20 / "LITERAL_140_EQUATION_DAG.json"
COLUMNS_PATH = V20 / "SOURCE_COLUMNS.json"
V20_RESULT = V20 / "RESULT.json"
V20_FIXTURES = V20 / "FIXTURE_AUDIT.json"
F10_PATH = V22 / "aws_r6b_r1_pass/output/F10_QUARTIC.txt"
V22_REPORT = V22 / "RESULT_V22R1.md"
LOAD6_PATH = V21_INPUT / "load_K6.txt"
V23_MATRIX = V23 / "GRADE7_NEWEST_MATRIX.txt"
V23_WITNESS = V23 / "GENERIC_RANK_WITNESS_MINOR.txt"
V23_K6_COLUMN = V23 / "FORBIDDEN_K6_0_COLUMN.txt"
V23_RESULT = V23 / "RESULT.json"
V24_B = V24 / "GRADE7_INHOMOGENEOUS_B.txt"
V24_PRIOR = V24 / "PRIOR_GRADE2_TO6_EQUATIONS.txt"
V24_COMPAT = V24 / "GRADE7_COMPATIBILITY_C6_C7.txt"
V24_RESULT = V24 / "RESULT.json"

# V23/V24 files are comparison controls, never construction inputs.
EXPECTED = {
    PREREG: "a6c1d7c6f54ae2277001b9261b8dc025482cc16e6d586a6810cde6c5de3a92fa",
    DAG_PATH: "b9bd2e2ca1319ee3107a0f7cf4e1750386d60bb12213a3a970c4812823abdce6",
    COLUMNS_PATH: "2e8ceeb42dcc41752f82fe1df866c28b33e289097b065bf965db25574230919c",
    V20_RESULT: "a2147de95bc37e8adb629201e2b39b788b99df3d4586da54af7bd41f269a9f15",
    V20_FIXTURES: "bbcdd0e0242a23b309cd04f44f42a0ef8f1b69eb8f13ef396fc40b26e450cf55",
    F10_PATH: "c8e214ae21b058dddb063dcd7a9075a34b02a14f01f54386822cf85f0dc2c8e8",
    V22_REPORT: "494075c5675a2571808aec8606ed5744c2362bf3abc470304226b6fee699e293",
    LOAD6_PATH: "2e2c2274bbe51748a5178cccb1cb195561785687c580be79beee52ecc6e2d73d",
    V23_MATRIX: "972ac0fa6fc0716bf2657cef6cb0ea0c6e4b3150f3f144f791818325f7e72af1",
    V23_WITNESS: "957181065328c7ef930c6c400272f45ab93a055ff1069ced7f3cca8b3c89bbde",
    V23_K6_COLUMN: "3e5717ae1e06ae818ee13c767418d8cac171f05421777adfcb9cc376746c7200",
    V23_RESULT: "3fb7ce922bd12bfe1102efa77d455e7a3a69e448b8eada291ddcfbe3585ec9e4",
    V24_B: "dc7696e1c1552533418eba1f91e14227ef8663aeded38b111d3295d1afb3f289",
    V24_PRIOR: "cd819cc66162cd891b96e403ecd2d8526ee5f379f83acf60300972974bade92b",
    V24_COMPAT: "4f4c2bac49270fdd220e2333fbf82ba8bd4cc507cff90ea3eb8c2bf8c614ddd2",
    V24_RESULT: "22cbd6acb79fc5788afc4b1220cc9eaa19d0a987a2126a49eace67e89ce7921b",
}

FIXED_ZERO = ("k6_0", "k2_0", "mu2_0", "mu4_0", "mu6_0")
NEWEST = tuple([f"d{i}_6" for i in range(6)] + ["k10_3"])
PRIOR = tuple([f"d{i}_{j}" for i in range(6) for j in range(1, 6)] +
              ["k10_0", "k10_1", "k10_2"])
LEADING = tuple(f"d{i}_1" for i in range(6))
PIVOT_ROWS = (0, 1, 2, 3, 4)
PIVOT_COLUMNS = (0, 1, 2, 3, 6)
ALLOWED_V24R2 = {
    "PASS_Q_LOCALIZED_PRIOR_IDEAL_UNIT_CHART_EMPTY",
    "PASS_Q_PROPER_C6_C7_EXACT_MEMBERS",
    "PASS_Q_PROPER_COMPATIBILITY_NONMEMBERSHIP_NORMAL_FORMS",
}

Monomial = tuple[tuple[str, int], ...]
Poly = dict[Monomial, Fraction]
ZERO_MONOMIAL: Monomial = ()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def canonical_json(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def object_digest(value: object) -> str:
    return sha256(canonical_json(value)).hexdigest()


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only V26 source compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only V26 source compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def m_mul(left: Monomial, right: Monomial) -> Monomial:
    counts = dict(left)
    for name, exponent in right:
        counts[name] = counts.get(name, 0) + exponent
    return tuple((name, exponent) for name, exponent in sorted(counts.items()) if exponent)


def p_const(value: Fraction | int) -> Poly:
    value = Fraction(value)
    return {} if value == 0 else {ZERO_MONOMIAL: value}


def p_var(name: str) -> Poly:
    return {((name, 1),): Fraction(1)}


def p_add(left: Poly, right: Poly, factor: Fraction = Fraction(1)) -> Poly:
    out = dict(left)
    for monomial, coefficient in right.items():
        out[monomial] = out.get(monomial, Fraction(0)) + factor * coefficient
        if out[monomial] == 0:
            del out[monomial]
    return out


def p_scale(poly: Poly, factor: Fraction) -> Poly:
    return {monomial: factor * coefficient for monomial, coefficient in poly.items()
            if factor * coefficient}


def p_mul(left: Poly, right: Poly, max_terms: int | None = None) -> Poly:
    if not left or not right:
        return {}
    out: Poly = {}
    for lmonomial, lcoefficient in left.items():
        for rmonomial, rcoefficient in right.items():
            monomial = m_mul(lmonomial, rmonomial)
            out[monomial] = out.get(monomial, Fraction(0)) + lcoefficient * rcoefficient
            if out[monomial] == 0:
                del out[monomial]
        if max_terms is not None and len(out) > max_terms:
            fail(("RESOURCE_CAP_POLYNOMIAL_TERM_LIMIT", len(out), max_terms))
    return out


def p_pow(poly: Poly, exponent: int, max_terms: int | None = None) -> Poly:
    if exponent < 0:
        fail("negative polynomial exponent")
    out = p_const(1)
    base = poly
    while exponent:
        if exponent & 1:
            out = p_mul(out, base, max_terms)
        exponent >>= 1
        if exponent:
            base = p_mul(base, base, max_terms)
    return out


def p_derivative(poly: Poly, variable: str) -> Poly:
    out: Poly = {}
    for monomial, coefficient in poly.items():
        powers = dict(monomial)
        exponent = powers.get(variable, 0)
        if exponent:
            if exponent == 1:
                del powers[variable]
            else:
                powers[variable] = exponent - 1
            key = tuple(sorted(powers.items()))
            out[key] = out.get(key, Fraction(0)) + coefficient * exponent
    return {key: value for key, value in out.items() if value}


def p_variables(poly: Poly) -> set[str]:
    return {name for monomial in poly for name, _ in monomial}


def p_evaluate(poly: Poly, assignment: dict[str, object], modulus: int | None = None) -> object:
    total: object = 0
    for monomial, coefficient in poly.items():
        if modulus is None:
            value: object = coefficient
        else:
            value = coefficient.numerator * pow(coefficient.denominator, -1, modulus) % modulus
        for name, exponent in monomial:
            value *= assignment[name] ** exponent
            if modulus is not None:
                value %= modulus
        total += value
        if modulus is not None:
            total %= modulus
    return total


def p_payload(poly: Poly) -> list[list[object]]:
    return [[[name, exponent] for name, exponent in monomial] +
            [coefficient.numerator, coefficient.denominator]
            for monomial, coefficient in sorted(poly.items())]


def p_digest(poly: Poly) -> str:
    return object_digest(p_payload(poly))


def p_text(poly: Poly) -> str:
    if not poly:
        return "0"
    pieces: list[str] = []
    for monomial, coefficient in sorted(poly.items()):
        factors = [name if exponent == 1 else f"{name}^{exponent}"
                   for name, exponent in monomial]
        body = "*".join(factors) or "1"
        if coefficient.denominator == 1:
            ctext = str(coefficient.numerator)
        else:
            ctext = f"({coefficient.numerator}/{coefficient.denominator})"
        pieces.append(f"({ctext})*{body}")
    return "+".join(pieces).replace("+(-", "-(")


def parse_ast_poly(node: ast.AST, aliases: dict[str, str]) -> Poly:
    if isinstance(node, ast.Constant) and isinstance(node.value, int):
        return p_const(node.value)
    if isinstance(node, ast.Name):
        return p_var(aliases.get(node.id, node.id))
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
        value = parse_ast_poly(node.operand, aliases)
        return value if isinstance(node.op, ast.UAdd) else p_scale(value, Fraction(-1))
    if isinstance(node, ast.BinOp):
        if isinstance(node.op, ast.Add):
            return p_add(parse_ast_poly(node.left, aliases), parse_ast_poly(node.right, aliases))
        if isinstance(node.op, ast.Sub):
            return p_add(parse_ast_poly(node.left, aliases), parse_ast_poly(node.right, aliases), Fraction(-1))
        if isinstance(node.op, ast.Mult):
            return p_mul(parse_ast_poly(node.left, aliases), parse_ast_poly(node.right, aliases))
        if isinstance(node.op, ast.Div):
            numerator = parse_ast_poly(node.left, aliases)
            denominator = parse_ast_poly(node.right, aliases)
            if set(denominator) != {ZERO_MONOMIAL} or denominator[ZERO_MONOMIAL] == 0:
                fail(("nonconstant denominator", ast.dump(node.right)))
            return p_scale(numerator, Fraction(1) / denominator[ZERO_MONOMIAL])
        if isinstance(node.op, ast.Pow):
            if not isinstance(node.right, ast.Constant) or not isinstance(node.right.value, int):
                fail(("noninteger exponent", ast.dump(node.right)))
            return p_pow(parse_ast_poly(node.left, aliases), node.right.value)
    fail(("unsupported exact-polynomial syntax", ast.dump(node)))


def parse_poly(text: str, aliases: dict[str, str] | None = None) -> Poly:
    source = "".join(text.split())
    if not source or any(character in source for character in ';,"'):
        fail(("malformed exact polynomial", source[:120]))
    return parse_ast_poly(ast.parse(source.replace("^", "**"), mode="eval").body,
                          aliases or {})


def parse_assignment_file(path: Path, aliases: dict[str, str] | None = None) -> dict[str, Poly]:
    out: dict[str, Poly] = {}
    for line in path.read_text().splitlines():
        if not line:
            continue
        if "=" not in line:
            fail(("assignment line missing equals", path, line[:80]))
        name, value = line.split("=", 1)
        if name in out:
            fail(("duplicate assignment", path, name))
        out[name] = parse_poly(value, aliases)
    return out


def parse_matrix(path: Path, aliases: dict[str, str]) -> list[list[Poly]]:
    matrix = [[parse_poly(piece, aliases) for piece in line.split(",")]
              for line in path.read_text().splitlines() if line]
    if len(matrix) != 7 or any(len(row) != 7 for row in matrix):
        fail(("comparison matrix census", path))
    return matrix


def homogeneous(poly: Poly, degree: int, variables: set[str]) -> Poly:
    return {monomial: coefficient for monomial, coefficient in poly.items()
            if sum(exponent for name, exponent in monomial if name in variables) == degree}


def validate_frozen_inputs() -> None:
    for path, expected in EXPECTED.items():
        if not path.is_file():
            fail(("frozen input missing", str(path)))
        actual = digest(path)
        if actual != expected:
            fail(("frozen input mismatch", str(path), actual, expected))


def validate_columns(columns: list[dict[str, object]]) -> tuple[dict[str, dict[str, object]], tuple[str, ...]]:
    if len(columns) != 169:
        fail(("source-column census", len(columns)))
    if [entry.get("column") for entry in columns] != list(range(169)):
        fail("source columns are not consecutively ordered")
    by_name = {str(entry.get("variable")): entry for entry in columns}
    if len(by_name) != 169:
        fail("duplicate source-column variable")
    fixed = tuple(str(entry["variable"]) for entry in columns
                  if entry.get("boundary_status") == "FIXED_ZERO_BEFORE_SOLVE")
    if fixed != FIXED_ZERO:
        fail(("boundary-zero order/census", fixed, FIXED_ZERO))
    free = tuple(str(entry["variable"]) for entry in columns
                 if entry.get("boundary_status") == "FREE")
    if len(free) != 164:
        fail(("free-source-column census", len(free)))
    for name in NEWEST:
        if by_name[name].get("boundary_status") != "FREE":
            fail(("newest coefficient not free", name))
    if by_name["k6_0"].get("first_Lambda_grade") != 6:
        fail("k6_0 source grade drift")
    if by_name["Jdet_0"].get("first_Lambda_grade") != 19:
        fail("Jdet source grade drift")
    return by_name, free


def validate_dag(data: dict[str, object], free: tuple[str, ...]) -> tuple[list[list[object]], dict[tuple[int, int], int]]:
    if data.get("format") != "K00_V20R2_EXACT_RATIONAL_ARITHMETIC_DAG_V1":
        fail("literal DAG format drift")
    if data.get("truncation") != "Q[Lambda]/(Lambda^20)":
        fail("literal DAG truncation drift")
    if data.get("boundary_restriction_order") != "SUBSTITUTE_FIVE_ZERO_CONSTANTS_BEFORE_ANY_SOLVE_OR_SATURATION":
        fail("restriction-order declaration drift")
    if data.get("source_column_sha256") != EXPECTED[COLUMNS_PATH]:
        fail("DAG/source-column binding drift")
    if data.get("target_symbol") != "Jdet" or data.get("forbidden_aliases") != ["J1", "J2"]:
        fail("Jdet/J1/J2 typing drift")
    nodes = data.get("nodes")
    roots_data = data.get("roots")
    if not isinstance(nodes, list) or len(nodes) != 309343:
        fail(("literal DAG node census", type(nodes), len(nodes) if isinstance(nodes, list) else None))
    if not isinstance(roots_data, list) or len(roots_data) != 140:
        fail("literal DAG root census")
    free_set = set(free)
    seen_variables: set[str] = set()
    for index, node in enumerate(nodes):
        if not isinstance(node, list) or not node:
            fail(("malformed DAG node", index))
        opcode = node[0]
        if opcode == "c":
            if len(node) != 3 or int(node[2]) == 0:
                fail(("malformed constant DAG node", index))
        elif opcode == "v":
            if len(node) != 2 or str(node[1]) not in free_set:
                fail(("untyped DAG variable", index, node))
            seen_variables.add(str(node[1]))
        elif opcode in ("a", "m"):
            if len(node) != 3 or not (0 <= int(node[1]) < index) or not (0 <= int(node[2]) < index):
                fail(("non-topological DAG operation", index, node))
        else:
            fail(("unknown DAG opcode", index, opcode))
    if seen_variables & set(FIXED_ZERO):
        fail("fixed boundary coefficient survived DAG restriction")
    if {"J1", "J2"} & seen_variables or "Jdet_0" not in seen_variables:
        fail("Jdet/J1/J2 variable typing mismatch")
    roots: dict[tuple[int, int], int] = {}
    for entry in roots_data:
        key = (int(entry["row"]), int(entry["Lambda_grade"]))
        node = int(entry["node"])
        if key in roots or not (1 <= key[0] <= 7 and 0 <= key[1] <= 19) or not (0 <= node < len(nodes)):
            fail(("malformed literal root", entry))
        roots[key] = node
    if set(roots) != {(row, grade) for row in range(1, 8) for grade in range(20)}:
        fail("literal root labels incomplete")
    return nodes, roots


def dependency_closure(nodes: list[list[object]], root_nodes: Iterable[int]) -> set[int]:
    needed: set[int] = set()
    todo = list(root_nodes)
    while todo:
        index = todo.pop()
        if index in needed:
            continue
        needed.add(index)
        node = nodes[index]
        if node[0] in ("a", "m"):
            todo.extend((int(node[1]), int(node[2])))
    return needed


def expand_roots(nodes: list[list[object]], selected: dict[tuple[int, int], int],
                 max_terms: int) -> tuple[dict[tuple[int, int], Poly], dict[str, object]]:
    """Expand only the dependency slice of selected roots, exactly over Q."""
    needed = dependency_closure(nodes, selected.values())
    uses: Counter[int] = Counter()
    for index in needed:
        node = nodes[index]
        if node[0] in ("a", "m"):
            uses[int(node[1])] += 1
            uses[int(node[2])] += 1
    root_labels: dict[int, list[tuple[int, int]]] = {}
    for label, index in selected.items():
        root_labels.setdefault(index, []).append(label)
    live: dict[int, Poly] = {}
    outputs: dict[tuple[int, int], Poly] = {}
    peak_live = 0
    peak_terms = 0
    multiplications = 0
    for index in sorted(needed):
        node = nodes[index]
        opcode = node[0]
        if opcode == "c":
            value = p_const(Fraction(int(node[1]), int(node[2])))
        elif opcode == "v":
            name = str(node[1])
            # This branch is explicit even though the frozen restricted DAG
            # already omits the five fixed columns: restriction precedes all
            # extraction and never relies on downstream saturation.
            value = {} if name in FIXED_ZERO else p_var(name)
        elif opcode == "a":
            value = p_add(live[int(node[1])], live[int(node[2])])
        elif opcode == "m":
            multiplications += 1
            value = p_mul(live[int(node[1])], live[int(node[2])], max_terms)
        else:  # validated above
            fail(("unknown DAG opcode during expansion", opcode))
        if len(value) > max_terms:
            fail(("RESOURCE_CAP_POLYNOMIAL_TERM_LIMIT", index, len(value), max_terms))
        peak_terms = max(peak_terms, len(value))
        live[index] = value
        for label in root_labels.get(index, []):
            outputs[label] = dict(value)
        if opcode in ("a", "m"):
            for parent in (int(node[1]), int(node[2])):
                uses[parent] -= 1
                if uses[parent] == 0 and parent not in root_labels:
                    del live[parent]
        peak_live = max(peak_live, len(live))
    if set(outputs) != set(selected):
        fail("selected-root expansion incomplete")
    return outputs, {
        "dependency_nodes": len(needed),
        "multiplication_nodes": multiplications,
        "peak_live_polynomials": peak_live,
        "peak_terms_in_one_node": peak_terms,
        "term_cap": max_terms,
    }


def evaluate_dag(nodes: list[list[object]], assignment: dict[str, object], modulus: int | None) -> list[object]:
    values: list[object] = []
    for index, node in enumerate(nodes):
        opcode = node[0]
        if opcode == "c":
            coefficient = Fraction(int(node[1]), int(node[2]))
            value: object = (coefficient if modulus is None else
                             coefficient.numerator * pow(coefficient.denominator, -1, modulus) % modulus)
        elif opcode == "v":
            value = assignment[str(node[1])]
        elif opcode == "a":
            value = values[int(node[1])] + values[int(node[2])]
        elif opcode == "m":
            value = values[int(node[1])] * values[int(node[2])]
        else:
            fail(("unknown DAG opcode during fixture", index, opcode))
        values.append(value if modulus is None else value % modulus)
    return values


def fixture_assignment(free: tuple[str, ...], seed: int, modulus: int | None) -> dict[str, object]:
    assignment: dict[str, object] = {}
    for name in free:
        raw = int.from_bytes(sha256(f"V26|{seed}|{name}".encode()).digest()[:8], "big")
        integer = raw % 17 - 8
        assignment[name] = Fraction(integer) if modulus is None else integer % modulus
    assignment["k10_0"] = Fraction(seed + 2) if modulus is None else (seed + 2) % modulus
    return assignment


def fixture_replay(nodes: list[list[object]], roots: dict[tuple[int, int], int],
                   expanded: dict[tuple[int, int], Poly], free: tuple[str, ...]) -> list[dict[str, object]]:
    audits: list[dict[str, object]] = []
    for seed, modulus in ((11, None), (29, None), (47, 65521)):
        assignment = fixture_assignment(free, seed, modulus)
        values = evaluate_dag(nodes, assignment, modulus)
        for label, poly in expanded.items():
            if p_evaluate(poly, assignment, modulus) != values[roots[label]]:
                fail(("expanded-root fixture mismatch", seed, modulus, label))
        root_values = [str(values[roots[(row, grade)]]) for row in range(1, 8) for grade in range(20)]
        audits.append({
            "seed": seed,
            "field": "Q" if modulus is None else f"F_{modulus}",
            "all_140_raw_root_values_sha256": object_digest(root_values),
            "all_selected_roots_match_exact_expansion": True,
            "selected_root_count": len(expanded),
        })
    inherited = json.loads(V20_FIXTURES.read_text())
    if len(inherited.get("fixtures", [])) != 3 or not all(item.get("all_140_roots_match")
                                                           for item in inherited["fixtures"]):
        fail("V20R2 independent all-140 fixture replay missing")
    return audits


def extract_affine(poly: Poly) -> tuple[Poly, list[Poly]]:
    constant: Poly = {}
    coefficients: list[Poly] = [{} for _ in NEWEST]
    newest_set = set(NEWEST)
    for monomial, coefficient in poly.items():
        powers = dict(monomial)
        newest_degree = sum(powers.get(name, 0) for name in NEWEST)
        if newest_degree > 1:
            fail(("grade-seven row nonlinear in honest newest variables", newest_degree, monomial))
        if newest_degree == 0:
            constant[monomial] = coefficient
        else:
            name = next(name for name in NEWEST if powers.get(name, 0))
            if powers[name] != 1:
                fail(("non-affine newest exponent", name, powers[name]))
            del powers[name]
            reduced = tuple(sorted(powers.items()))
            coefficients[NEWEST.index(name)][reduced] = coefficient
    allowed = set(PRIOR)
    if p_variables(constant) - allowed or any(p_variables(item) - allowed for item in coefficients):
        fail(("grade-seven row retains non-prior source columns",
              sorted((p_variables(constant) | set().union(*(p_variables(item) for item in coefficients))) - allowed)))
    for left in NEWEST:
        for right in NEWEST:
            if p_derivative(p_derivative(poly, left), right):
                fail(("nonzero exact second derivative", left, right))
    if p_variables(poly) & newest_set and not any(coefficients):
        fail("newest variables present but affine coefficients vanished")
    return constant, coefficients


def determinant_poly(matrix: Sequence[Sequence[Poly]], rows: tuple[int, ...], columns: tuple[int, ...],
                     memo: dict[tuple[tuple[int, ...], tuple[int, ...]], Poly],
                     max_terms: int) -> Poly:
    key = (rows, columns)
    if key in memo:
        return memo[key]
    size = len(rows)
    if size != len(columns):
        fail("nonsquare minor")
    if size == 0:
        result = p_const(1)
    elif size == 1:
        result = matrix[rows[0]][columns[0]]
    else:
        row = rows[0]
        tail_rows = rows[1:]
        result: Poly = {}
        for position, column in enumerate(columns):
            entry = matrix[row][column]
            if not entry:
                continue
            tail_columns = columns[:position] + columns[position + 1:]
            term = p_mul(entry, determinant_poly(matrix, tail_rows, tail_columns, memo, max_terms), max_terms)
            result = p_add(result, term, Fraction(-1 if position & 1 else 1))
            if len(result) > max_terms:
                fail(("RESOURCE_CAP_DETERMINANT_TERM_LIMIT", size, len(result), max_terms))
    memo[key] = result
    return result


def all_poly_minors(matrix: Sequence[Sequence[Poly]], max_size: int,
                    max_terms: int) -> tuple[dict[int, list[dict[str, object]]], dict[str, object]]:
    memo: dict[tuple[tuple[int, ...], tuple[int, ...]], Poly] = {}
    output: dict[int, list[dict[str, object]]] = {}
    stats: dict[str, object] = {}
    for size in range(1, max_size + 1):
        records: list[dict[str, object]] = []
        for rows in combinations(range(len(matrix)), size):
            for columns in combinations(range(len(matrix[0])), size):
                poly = determinant_poly(matrix, rows, columns, memo, max_terms)
                records.append({"rows": list(rows), "columns": list(columns),
                                "poly": poly, "sha256": p_digest(poly), "terms": len(poly)})
        output[size] = records
        stats[str(size)] = {
            "total": len(records),
            "zero": sum(not record["poly"] for record in records),
            "unique_exact_polynomials": len({record["sha256"] for record in records}),
            "unique_nonzero_exact_polynomials": len({record["sha256"] for record in records if record["poly"]}),
            "max_terms": max((int(record["terms"]) for record in records), default=0),
            "total_terms": sum(int(record["terms"]) for record in records),
        }
    return output, stats


class ExprArena:
    """Hash-consed exact arithmetic DAG; add/mul are flattened and sorted."""

    def __init__(self) -> None:
        self.nodes: list[list[object]] = []
        self._intern: dict[tuple[object, ...], int] = {}
        self._digests: list[str] = []
        self.zero = self.const(Fraction(0))
        self.one = self.const(Fraction(1))

    def _make(self, key: tuple[object, ...], payload: list[object]) -> int:
        if key in self._intern:
            return self._intern[key]
        index = len(self.nodes)
        self.nodes.append(payload)
        self._intern[key] = index
        self._digests.append(sha256(canonical_json(payload)).hexdigest())
        return index

    def const(self, value: Fraction | int) -> int:
        value = Fraction(value)
        return self._make(("q", value.numerator, value.denominator),
                          ["q", value.numerator, value.denominator])

    def var(self, name: str) -> int:
        return self._make(("v", name), ["v", name])

    def add(self, *children: int) -> int:
        flat: list[int] = []
        constant = Fraction(0)
        pending = list(children)
        while pending:
            child = pending.pop()
            node = self.nodes[child]
            if node[0] == "a":
                pending.extend(int(item) for item in node[1])
            elif node[0] == "q":
                constant += Fraction(int(node[1]), int(node[2]))
            else:
                flat.append(child)
        if constant:
            flat.append(self.const(constant))
        flat = [child for child in flat if child != self.zero]
        flat.sort(key=lambda child: self._digests[child])
        if not flat:
            return self.zero
        if len(flat) == 1:
            return flat[0]
        key = ("a", *flat)
        return self._make(key, ["a", flat])

    def mul(self, *children: int) -> int:
        flat: list[int] = []
        constant = Fraction(1)
        pending = list(children)
        while pending:
            child = pending.pop()
            node = self.nodes[child]
            if child == self.zero:
                return self.zero
            if node[0] == "m":
                pending.extend(int(item) for item in node[1])
            elif node[0] == "q":
                constant *= Fraction(int(node[1]), int(node[2]))
            else:
                flat.append(child)
        if constant == 0:
            return self.zero
        if constant != 1:
            flat.append(self.const(constant))
        flat = [child for child in flat if child != self.one]
        flat.sort(key=lambda child: self._digests[child])
        if not flat:
            return self.one
        if len(flat) == 1:
            return flat[0]
        key = ("m", *flat)
        return self._make(key, ["m", flat])

    def neg(self, child: int) -> int:
        return self.mul(self.const(-1), child)

    def from_poly(self, poly: Poly) -> int:
        terms: list[int] = []
        for monomial, coefficient in sorted(poly.items()):
            factors = [self.const(coefficient)]
            for name, exponent in monomial:
                variable = self.var(name)
                factors.extend([variable] * exponent)
            terms.append(self.mul(*factors))
        return self.add(*terms)

    def digest(self, node: int) -> str:
        return self._digests[node]


def determinant_expr(arena: ExprArena, matrix: Sequence[Sequence[int]], rows: tuple[int, ...],
                     columns: tuple[int, ...], memo: dict[tuple[tuple[int, ...], tuple[int, ...]], int]) -> int:
    key = (rows, columns)
    if key in memo:
        return memo[key]
    if len(rows) == 0:
        result = arena.one
    elif len(rows) == 1:
        result = matrix[rows[0]][columns[0]]
    else:
        terms: list[int] = []
        for position, column in enumerate(columns):
            entry = matrix[rows[0]][column]
            if entry == arena.zero:
                continue
            tail = determinant_expr(arena, matrix, rows[1:],
                                    columns[:position] + columns[position + 1:], memo)
            term = arena.mul(entry, tail)
            terms.append(arena.neg(term) if position & 1 else term)
        result = arena.add(*terms)
    memo[key] = result
    return result


def all_expr_minors(arena: ExprArena, matrix: Sequence[Sequence[int]], name: str,
                    max_size: int) -> tuple[list[dict[str, object]], dict[str, object]]:
    memo: dict[tuple[tuple[int, ...], tuple[int, ...]], int] = {}
    records: list[dict[str, object]] = []
    stats: dict[str, object] = {}
    for size in range(1, max_size + 1):
        start = len(records)
        for rows in combinations(range(len(matrix)), size):
            for columns in combinations(range(len(matrix[0])), size):
                root = determinant_expr(arena, matrix, rows, columns, memo)
                records.append({"matrix": name, "size": size, "rows": list(rows),
                                "columns": list(columns), "root": root,
                                "root_sha256": arena.digest(root)})
        subset = records[start:]
        stats[str(size)] = {"total": len(subset),
                            "unique_root_hashes": len({item["root_sha256"] for item in subset}),
                            "structural_zero_roots": sum(item["root"] == arena.zero for item in subset)}
    return records, stats


def matrix_rank_q(matrix: list[list[Fraction]]) -> int:
    work = [list(row) for row in matrix]
    rows = len(work)
    columns = len(work[0]) if rows else 0
    rank = 0
    for column in range(columns):
        pivot = next((row for row in range(rank, rows) if work[row][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        value = work[rank][column]
        work[rank] = [entry / value for entry in work[rank]]
        for row in range(rows):
            if row != rank and work[row][column]:
                factor = work[row][column]
                work[row] = [left - factor * right for left, right in zip(work[row], work[rank])]
        rank += 1
        if rank == rows:
            break
    return rank


def toy_controls() -> dict[str, object]:
    zero = Fraction(0)
    one = Fraction(1)
    def diagonal(rank: int) -> list[list[Fraction]]:
        return [[one if row == column and row < rank else zero for column in range(7)]
                for row in range(7)]
    cases = []
    for name, rank, b, compatible in (
        ("rank5_compatible", 5, [one, zero, zero, zero, zero, zero, zero], True),
        ("rank5_incompatible", 5, [zero, zero, zero, zero, zero, one, zero], False),
        ("rank4_compatible", 4, [one, zero, zero, zero, zero, zero, zero], True),
        ("rank4_incompatible", 4, [zero, zero, zero, zero, one, zero, zero], False),
        ("rank0_compatible", 0, [zero] * 7, True),
        ("rank0_incompatible", 0, [one] + [zero] * 6, False),
    ):
        matrix = diagonal(rank)
        augmented = [row + [-b[index]] for index, row in enumerate(matrix)]
        got = matrix_rank_q(matrix) == matrix_rank_q(augmented)
        if got != compatible:
            fail(("toy compatibility classifier", name, got, compatible))
        cases.append({"name": name, "rank_A": matrix_rank_q(matrix),
                      "rank_E": matrix_rank_q(augmented), "compatible": got})
    alternate = diagonal(5)
    chosen = [[alternate[row][column] for column in PIVOT_COLUMNS] for row in PIVOT_ROWS]
    other = [[alternate[row][column] for column in range(5)] for row in range(5)]
    if matrix_rank_q(chosen) != 4 or matrix_rank_q(other) != 5:
        fail("alternate maximal-minor toy failed")
    incompatible = diagonal(5)
    b = [zero, zero, zero, zero, zero, one, zero]
    augmented = [incompatible[row][:5] + [-b[row]] for row in range(6)]
    mutated = [incompatible[row][:5] + [b[row]] for row in range(6)]
    # These square matrices have determinants -1 and +1 respectively.
    if matrix_rank_q(augmented) != 6 or matrix_rank_q(mutated) != 6 or augmented == mutated:
        fail("toy sign mutation failed")
    return {
        "rank_cases": cases,
        "single_chosen_minor_can_vanish_while_another_is_nonzero": True,
        "inhomogeneous_sign_mutation_changes_augmented_matrix_and_maximal_minor": True,
    }


def parse_load6_mutation() -> list[Poly]:
    pieces = "".join(LOAD6_PATH.read_text().split()).split(",")
    if len(pieces) != 7:
        fail(("K6 row census", len(pieces)))
    aliases = {f"d{i}": f"d{i}_1" for i in range(6)}
    variables = set(aliases.values())
    column = [homogeneous(parse_poly(piece, aliases), 1, variables) for piece in pieces]
    if not any(column):
        fail("restored k6_0 grade-seven column is zero")
    frozen = [parse_poly(line, {f"x{i}": f"d{i}_1" for i in range(6)})
              for line in V23_K6_COLUMN.read_text().splitlines()]
    if column != frozen:
        fail("restored k6_0 column disagrees with frozen V23 control")
    return column


def validate_v24r2(path: Path | None) -> dict[str, object]:
    if path is None:
        return {"status": "HELD_MISSING_EXACT_Q_V24R2_ENDPOINT",
                "release_allowed": False,
                "requirement": "supply --v24r2-endpoint with reviewed exact-Q result and custody"}
    path = path.resolve()
    if not path.is_file():
        fail(("V24R2 endpoint path missing", str(path)))
    payload = json.loads(path.read_text())
    status = payload.get("status")
    if status not in ALLOWED_V24R2 or payload.get("field") != "Q_exact":
        fail(("V24R2 is not an allowed exact-Q endpoint", status, payload.get("field")))
    artifacts = payload.get("artifacts")
    if not isinstance(artifacts, dict) or not artifacts:
        fail("V24R2 exact endpoint has no artifact custody")
    checked: dict[str, str] = {}
    for name, metadata in artifacts.items():
        if Path(str(name)).name != str(name):
            fail(("unsafe V24R2 artifact name", name))
        artifact = path.parent / str(name)
        expected = metadata.get("sha256") if isinstance(metadata, dict) else None
        if not artifact.is_file() or not isinstance(expected, str) or digest(artifact) != expected:
            fail(("V24R2 artifact custody mismatch", str(artifact), expected))
        checked[str(name)] = expected
    return {"status": status, "release_allowed": True, "endpoint": str(path),
            "endpoint_sha256": digest(path), "artifact_sha256": checked,
            "scope": payload.get("scope")}


def write_json(path: Path, payload: object) -> None:
    path.write_bytes(canonical_json(payload))


def serialize_poly(poly: Poly) -> dict[str, object]:
    return {"sha256": p_digest(poly), "terms": len(poly), "exact_terms": p_payload(poly),
            "singular": p_text(poly)}


def build_job_specs(a_minors: dict[int, list[dict[str, object]]],
                    prepass_decides_lower: bool = False) -> dict[str, object]:
    ranks: dict[str, object] = {}
    for rank in range(6):
        if rank == 0:
            charts = [{"chart_id": "r0_I0_unit", "localizer": serialize_poly(p_const(1)),
                       "minor_sources": [{"rows": [], "columns": []}]}]
        else:
            by_hash: dict[str, dict[str, object]] = {}
            for record in a_minors[rank]:
                poly = record["poly"]
                if not poly:
                    continue
                item = by_hash.setdefault(str(record["sha256"]), {
                    "chart_id": f"r{rank}_{str(record['sha256'])[:16]}",
                    "localizer": serialize_poly(poly), "minor_sources": []})
                item["minor_sources"].append({"rows": record["rows"], "columns": record["columns"]})
            charts = [by_hash[key] for key in sorted(by_hash)]
        ranks[str(rank)] = {
            "rank": rank,
            "closed_ideal": f"P6+I{rank + 1}(A)+I{rank + 1}(E)",
            "open_cover": "D(k10_0*m) for every distinct nonzero m in I_r(A)",
            "chart_count": len(charts),
            "charts": charts,
            "prepass_stop_eligible": rank < 5,
            "prepass_stop_active": bool(prepass_decides_lower and rank < 5),
        }
    return {
        "format": "K00_V26_EXACT_Q_JOB_SPECS_V1",
        "dependency_release_required_for_every_job": True,
        "prepass": {"job_id": "coefficient_base_B_plus_I5A", "field": "Q",
                    "ideal": "B=(Q1,...,Q6,F10); decide B+I5(A)",
                    "allowed_effect": "select/stop lower-rank jobs only; never replace P6 compatibility"},
        "v24_chart_agreement": {"job_id": "D_W_I6E_equals_Comp6_Comp7", "field": "Q",
                                "localizer": "W", "method": "tracked liftstd after zW*W-1"},
        "rank_strata": ranks,
        "promotion_rule": "no atlas verdict until all relevant chart jobs and second-process certificates are reviewed",
    }


def static_self_test() -> None:
    aliases = {"x0": "d0_1", "x1": "d1_1"}
    left = parse_poly("(1/2)*x0^2-3*x0*x1+5", aliases)
    right = p_add(p_scale(p_pow(p_var("d0_1"), 2), Fraction(1, 2)),
                  p_add(p_scale(p_mul(p_var("d0_1"), p_var("d1_1")), Fraction(-3)), p_const(5)))
    if left != right or parse_poly(p_text(left)) != left:
        fail("sparse polynomial/parser/text self-test")
    matrix = [[p_const(1), p_var("x")], [p_const(0), p_const(1)]]
    determinant = determinant_poly(matrix, (0, 1), (0, 1), {}, 100)
    if determinant != p_const(1):
        fail("fraction-free determinant self-test")
    arena = ExprArena()
    ematrix = [[arena.from_poly(entry) for entry in row] for row in matrix]
    if determinant_expr(arena, ematrix, (0, 1), (0, 1), {}) == arena.zero:
        fail("determinant DAG self-test")
    toy_controls()
    print("K00_V26_STATIC_SELF_TEST=PASS")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path, nargs="?")
    parser.add_argument("--v24r2-endpoint", type=Path)
    parser.add_argument("--compile-held", action="store_true",
                        help="emit source/job inputs while recording the missing exact-Q dependency")
    parser.add_argument("--max-terms", type=int, default=2_000_000)
    parser.add_argument("--static-self-test", action="store_true")
    parser.add_argument("--static-input-check", action="store_true")
    args = parser.parse_args()
    if args.static_self_test:
        static_self_test()
        return
    if args.static_input_check:
        validate_frozen_inputs()
        print("K00_V26_STATIC_INPUT_CHECK=PASS")
        return
    if args.output is None:
        parser.error("output is required outside static-check modes")
    lane = require_aws()
    validate_frozen_inputs()
    dependency = validate_v24r2(args.v24r2_endpoint)
    if not dependency["release_allowed"] and not args.compile_held:
        fail("exact-Q V24R2 dependency missing; use --compile-held only to prepare unreleased job inputs")

    columns = json.loads(COLUMNS_PATH.read_text())
    by_name, free = validate_columns(columns)
    data = json.loads(DAG_PATH.read_text())
    nodes, roots = validate_dag(data, free)
    selected = {(row, grade): roots[(row, grade)] for row in range(1, 8) for grade in range(8)}
    expanded, expansion_stats = expand_roots(nodes, selected, args.max_terms)

    # P6 is constructed before any grade-seven extraction and includes every
    # literal row through grade six, with exact zero rows retained in metadata.
    literal_prefix = [{"row": row, "Lambda_grade": grade, "poly": expanded[(row, grade)]}
                      for grade in range(7) for row in range(1, 8)]
    if any(p_variables(item["poly"]) - set(PRIOR) for item in literal_prefix):
        fail("prior prefix retained newest/later/untyped source variables")
    f10 = parse_poly(F10_PATH.read_text(), {f"x{i}": f"d{i}_1" for i in range(6)})
    if p_variables(f10) - set(LEADING):
        fail("F10 is not a six-leading-variable polynomial")
    prior_generators = [item["poly"] for item in literal_prefix if item["poly"]] + [f10]
    grade2 = [expanded[(row, 2)] for row in range(1, 8)]
    if grade2[5] or not all(grade2[index] for index in (0, 1, 2, 3, 4, 6)):
        fail("six-variable Q1,...,Q6 row profile drift")
    if len(prior_generators) != 35:
        fail(("P6 nonzero-generator census including F10", len(prior_generators), 35))

    affine = [extract_affine(expanded[(row, 7)]) for row in range(1, 8)]
    b = [item[0] for item in affine]
    matrix = [item[1] for item in affine]
    if any(p_variables(entry) - set(LEADING) for row in matrix for entry in row):
        fail("A depends on more than the six leading normal coordinates")
    e_matrix = [row + [p_scale(b[index], Fraction(-1))] for index, row in enumerate(matrix)]

    # Earlier products are exact coefficientwise comparison controls only.
    aliases = {f"x{i}": f"d{i}_1" for i in range(6)}
    if matrix != parse_matrix(V23_MATRIX, aliases):
        fail("direct V20R2 A reconstruction differs coefficientwise from V23")
    v24_b = parse_assignment_file(V24_B)
    if b != [v24_b[f"b{index}"] for index in range(1, 8)]:
        fail("direct V20R2 b reconstruction differs coefficientwise from V24")
    v24_prior = parse_assignment_file(V24_PRIOR)
    comparison_prior = [expanded[(row, grade)] for grade in range(2, 7) for row in range(1, 8)]
    expected_prior = [v24_prior[f"P_r{row}_g{grade}"] for grade in range(2, 7) for row in range(1, 8)]
    if comparison_prior != expected_prior:
        fail("direct V20R2 P6 reconstruction differs coefficientwise from V24")

    fixture_audit = fixture_replay(nodes, roots, expanded, free)
    inherited_v20 = json.loads(V20_RESULT.read_text())
    if inherited_v20.get("status") != "PASS_EXACT_CONTRACTED_SOURCE_COMPILER_READY_FOR_STRATIFIED_SOLVE":
        fail("V20R2 source compiler endpoint drift")
    v23_result = json.loads(V23_RESULT.read_text())
    if v23_result.get("generic_rank") != 5:
        fail("V23 comparison endpoint rank drift")

    k6_column = parse_load6_mutation()
    a_minors, a_minor_stats = all_poly_minors(matrix, 6, args.max_terms)
    if any(record["poly"] for record in a_minors[6]):
        fail("an exact 6x6 minor of A is nonzero")
    nonzero5 = [record for record in a_minors[5] if record["poly"]]
    if not nonzero5:
        fail("no exact nonzero 5x5 minor of A")
    independent_rank_witness = min(nonzero5, key=lambda item: (item["sha256"], item["rows"], item["columns"]))
    v23_w = parse_poly(V23_WITNESS.read_text(), aliases)
    pivot_w = determinant_poly(matrix, PIVOT_ROWS, PIVOT_COLUMNS, {}, args.max_terms)
    if not pivot_w or pivot_w != v23_w:
        fail("V23 W comparison mismatch")

    # Distinguished augmented minors are exactly -Comp6,-Comp7 for E=[A|-b].
    v24_compat = parse_assignment_file(V24_COMPAT)
    comp = [v24_compat["C6"], v24_compat["C7"]]
    distinguished: list[Poly] = []
    for position, extra_row in enumerate((5, 6)):
        minor = determinant_poly(e_matrix, PIVOT_ROWS + (extra_row,),
                                 PIVOT_COLUMNS + (7,), {}, args.max_terms)
        if minor != p_scale(comp[position], Fraction(-1)):
            fail(("V24 distinguished augmented-minor sign mismatch", extra_row))
        distinguished.append(minor)
    if not all(distinguished):
        fail("distinguished augmented minor vanished")

    # Exact negative controls, performed on reconstructed objects.
    sign_mutation_changed = False
    for row in range(7):
        if not b[row]:
            continue
        mutated_b = list(b)
        mutated_b[row] = p_scale(mutated_b[row], Fraction(-1))
        mutated_e = [matrix[index] + [p_scale(mutated_b[index], Fraction(-1))]
                     for index in range(7)]
        for extra_row, original in zip((5, 6), distinguished):
            changed = determinant_poly(mutated_e, PIVOT_ROWS + (extra_row,),
                                       PIVOT_COLUMNS + (7,), {}, args.max_terms)
            if changed != original:
                sign_mutation_changed = True
                break
        if sign_mutation_changed:
            break
    if not sign_mutation_changed:
        fail("b sign mutation did not change an augmented minor")
    swapped = (1, 0, 2, 3, 6)
    wrong_order_minor = determinant_poly(e_matrix, PIVOT_ROWS + (5,), swapped + (7,), {}, args.max_terms)
    if wrong_order_minor == distinguished[0]:
        fail("row/column-order mutation survived distinguished-minor comparison")

    # Canonical exact determinant DAG for every minor needed by I_j(A),I_j(E), j<=6.
    arena = ExprArena()
    a_expr = [[arena.from_poly(entry) for entry in row] for row in matrix]
    e_expr = [[arena.from_poly(entry) for entry in row] for row in e_matrix]
    a_roots, a_expr_stats = all_expr_minors(arena, a_expr, "A", 6)
    e_roots, e_expr_stats = all_expr_minors(arena, e_expr, "E", 6)

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    polynomial_payload = {
        "format": "K00_V26_EXACT_SPARSE_POLYNOMIALS_V1",
        "ring_variables": list(PRIOR),
        "honest_newest_variables": list(NEWEST),
        "A": [[serialize_poly(entry) for entry in row] for row in matrix],
        "b": [serialize_poly(entry) for entry in b],
        "E_convention": "A with final column -b",
        "P6_literal_rows_through_grade6": [
            {"row": item["row"], "Lambda_grade": item["Lambda_grade"],
             "poly": serialize_poly(item["poly"])} for item in literal_prefix],
        "P6_nonzero_generators_plus_F10": [serialize_poly(poly) for poly in prior_generators],
        "Q1_to_Q6": [serialize_poly(expanded[(row, 2)]) for row in (1, 2, 3, 4, 5, 7)],
        "F10": serialize_poly(f10),
        "W": serialize_poly(pivot_w),
        "Comp6_Comp7": [serialize_poly(item) for item in comp],
        "distinguished_I6E_equals_negative_Comp": [serialize_poly(item) for item in distinguished],
        "forbidden_restored_k6_0_column": [serialize_poly(item) for item in k6_column],
    }
    polynomial_path = output / "ATLAS_EXACT_POLYNOMIALS.json"
    write_json(polynomial_path, polynomial_payload)

    determinant_payload = {
        "format": "K00_V26_CANONICAL_EXACT_DETERMINANT_DAG_V1",
        "construction": "fraction-free recursive exterior/Laplace compounds with hash-consed exact arithmetic DAG",
        "optional_expansion": "A minors expanded separately; E minors remain canonical DAG until exact AWS jobs",
        "nodes": arena.nodes,
        "roots": a_roots + e_roots,
        "statistics": {"arena_nodes": len(arena.nodes), "A": a_expr_stats, "E": e_expr_stats},
    }
    determinant_path = output / "DETERMINANT_DAG.json"
    write_json(determinant_path, determinant_payload)

    a_minor_payload = {
        "format": "K00_V26_EXPANDED_A_COMPOUND_MINORS_V1",
        "statistics": a_minor_stats,
        "generic_rank": 5,
        "all_I6_zero": True,
        "independent_rank5_witness": {
            "rows": independent_rank_witness["rows"],
            "columns": independent_rank_witness["columns"],
            "poly": serialize_poly(independent_rank_witness["poly"]),
        },
        "minors": {str(size): [
            {"rows": record["rows"], "columns": record["columns"],
             "poly": serialize_poly(record["poly"])} for record in records]
            for size, records in a_minors.items()},
    }
    a_minor_path = output / "A_COMPOUND_MINORS.json"
    write_json(a_minor_path, a_minor_payload)

    jobs = build_job_specs(a_minors)
    jobs_path = output / "EXACT_Q_JOB_SPECS.json"
    write_json(jobs_path, jobs)
    fixture_path = output / "SOURCE_RECONSTRUCTION_FIXTURES.json"
    write_json(fixture_path, {"new_V26_fixtures": fixture_audit,
                              "inherited_V20R2_independent_all_140_fixture_audit_sha256": digest(V20_FIXTURES)})
    controls_path = output / "CONTROLS.json"
    write_json(controls_path, {
        "toys": toy_controls(),
        "A_all_6x6_minors_exact_zero": True,
        "A_nonzero_5x5_witness_independent_of_W_selection": True,
        "b_sign_mutation_changes_augmented_minor": sign_mutation_changed,
        "row_column_order_mutation_caught": True,
        "restriction_order_mutation_restores_nonzero_k6_0_column": True,
        "Jdet_distinct_and_absent_through_grade7": all("Jdet_0" not in p_variables(item)
                                                        for item in [*b, *prior_generators,
                                                                     *(entry for row in matrix for entry in row)]),
        "forced_unit_and_known_proper_controls": "embedded in run_v26_exact_worker.py for every exact job",
        "second_process_replay": "mandatory downstream; no worker result is promoted by this compiler",
    })
    dependency_path = output / "V24R2_DEPENDENCY.json"
    write_json(dependency_path, dependency)

    source_artifacts = (polynomial_path, determinant_path, a_minor_path, jobs_path,
                        fixture_path, controls_path, dependency_path)
    compiled_freeze = output / "COMPILED_SOURCE.sha256"
    compiled_freeze.write_text("".join(f"{digest(path)}  {path.name}\n" for path in source_artifacts))
    if dependency["release_allowed"]:
        release = output / "RELEASE_V24R2_EXACT.json"
        write_json(release, {"released": True, "dependency": dependency,
                             "compiled_source_sha256": digest(compiled_freeze),
                             "permission": "exact jobs may be launched under independent AWS registrations"})
        release_freeze = output / "RELEASE_FREEZE.sha256"
        release_freeze.write_text(
            f"{digest(compiled_freeze)}  {compiled_freeze.name}\n"
            f"{digest(dependency_path)}  {dependency_path.name}\n"
            f"{digest(release)}  {release.name}\n")

    status = "PASS_V26_FITTING_ATLAS_COMPILED_NO_STRATUM_DECISION"
    result = {
        "status": status,
        "registered_aws_lane": lane,
        "dependency": dependency,
        "construction_source": "V20R2 literal arithmetic DAG and source columns only",
        "comparison_only": ["V23 A/W/k6 control", "V24 b/P6/Comp6/Comp7"],
        "boundary_restrictions_applied_before_extraction": list(FIXED_ZERO),
        "honest_newest_variables": list(NEWEST),
        "A_shape": [7, 7], "E_shape": [7, 8], "generic_rank_A": 5,
        "P6_nonzero_generator_count_including_F10": len(prior_generators),
        "source_expansion": expansion_stats,
        "A_minor_statistics": a_minor_stats,
        "determinant_DAG_statistics": determinant_payload["statistics"],
        "rank_chart_counts": {rank: data["chart_count"]
                              for rank, data in jobs["rank_strata"].items()},
        "controls": "PASS",
        "artifacts": {path.name: {"sha256": digest(path), "bytes": path.stat().st_size}
                      for path in (*source_artifacts, compiled_freeze)},
        "input_sha256": {str(path.relative_to(ROOT)): digest(path) for path in EXPECTED},
        "scope": "COMPILER_AND_HELD_EXACT_JOB_INPUTS_ONLY_NO_CONSTRUCTIBLE_STRATUM_DECISION",
        "firewall": "NO_GRADES8TO19_NO_FULL_JET_NO_ARC_NO_CLOSURE_NO_ORDER2_NO_MAX12_NO_JC2",
    }
    result_path = output / "RESULT.json"
    write_json(result_path, result)
    print("K00_V26_COMPILER=" + status)
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
