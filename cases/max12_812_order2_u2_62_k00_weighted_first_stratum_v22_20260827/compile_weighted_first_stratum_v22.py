#!/usr/bin/env python3
"""Extract and decide the first honest weighted K00 obstruction stratum."""

from __future__ import annotations

import argparse
import ast
from fractions import Fraction
from hashlib import sha256
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
V18 = ROOT / "cases/max12_812_order2_u2_62_k00_filtered_load_obstruction_v18r2_20260827/aws_qprov_r1_box01_pass"
PRELUDE = V21 / "prelude_Q.sing"
IMAGE = V21 / "image_K10.txt"
TARGET = V21 / "target_K10.txt"
SOLUTION_D3 = V18 / "output/solution_K10_D3.tsv"
COLUMNS_D3 = V18 / "output/emitted/columns_K10_D3.json"
DUAL_D4 = V18 / "output/solution_K10_D4.tsv"
ROWS_D4 = V18 / "output/emitted/rows_K10_D4.json"
PREREG = HERE / "PREREGISTRATION.md"
PREREG_R1 = HERE / "PREREGISTRATION_R1.md"
EXPECTED = {
    PREREG: "1b4ae1199e7e2e88fa56c9a8c4d5a48e853af5fa67b75766b0a30c1aa0353180",
    PREREG_R1: "1bbabb2aeb9385756e2ac1edf0ec075a613920fb939122826307e9bd3f7caf78",
    PRELUDE: "5b0a77e6d16df30de2df344862fc4316aedcc8aeabf1ec81e23d7881ce67ee7a",
    IMAGE: "9f37ef3f443300721db13a07a9a3ef449d6afdb742cd95f6662f57e040855c53",
    TARGET: "e7c792c7f6c4b2dde8ab08e39182cc90b2fe07d61f4a484ee8e9e79436623d69",
    SOLUTION_D3: "95ddc8eb5d4e624c5a5861de7d26e41dec51c16da99739d0834a00b878b6d8f2",
    COLUMNS_D3: "8075c60bd0d31f7c4546fd79641fe40df5ec63524d5428c10946be51e23a840f",
    DUAL_D4: "f316823aec28e2318e9df2c91f9d05d3980a17a01637acf8abc861e3e0d82b5e",
    ROWS_D4: "9a8d078ef21f525693df4a10f47db3b7c64149cd9c6589321a9a98fadb6618b9",
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
        fail("AWS-only V22 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only V22 compiler refused non-Amazon host")
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
    return {key: coefficient * value for key, coefficient in poly.items() if coefficient * value}


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


def parse_ideal(path: Path) -> list[Poly]:
    return [parse_poly(piece) for piece in "".join(path.read_text().split()).split(",")]


def parse_rows() -> list[Poly]:
    text = PRELUDE.read_text()
    rows: list[Poly] = []
    for index in range(1, 7):
        match = re.search(rf"(?:^|\n)poly r{index}=(.*?);", text, re.S)
        if match is None:
            fail(("missing row", index))
        rows.append(parse_poly(match.group(1)))
    return rows


def homogeneous(poly: Poly, degree: int) -> Poly:
    return {key: value for key, value in poly.items() if sum(key) == degree}


def valid_quadratic_profile(quadrics: list[Poly]) -> bool:
    return len(quadrics) == 6 and all(quadrics[index] for index in range(5)) and not quadrics[5]


def monomial(key: list[int]) -> Poly:
    if len(key) != NVAR or any(value < 0 for value in key):
        fail(("bad multiplier", key))
    return {tuple(key): Fraction(1)}


def parse_solution(path: Path, marker: str) -> dict[int, Fraction]:
    values: dict[int, Fraction] = {}
    for line in path.read_text().splitlines():
        parts = line.split()
        if parts and parts[0] == marker:
            if len(parts) != 3 or int(parts[1]) in values:
                fail(("bad certificate line", line))
            values[int(parts[1])] = Fraction(parts[2])
    if not values:
        fail(("empty certificate", str(path), marker))
    return values


def poly_text(poly: Poly, prefix: str = "x") -> str:
    if not poly:
        return "0"
    terms: list[str] = []
    for key, coefficient in sorted(poly.items()):
        factors = [f"{prefix}{index}^{exponent}" if exponent != 1 else f"{prefix}{index}"
                   for index, exponent in enumerate(key) if exponent]
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
    rows = parse_rows()
    image = parse_ideal(IMAGE)
    if len(image) != 66:
        fail(("image count", len(image)))
    generators = rows + image
    target = parse_poly(TARGET.read_text())
    columns = json.loads(COLUMNS_D3.read_text())
    if len(columns) != 101:
        fail(("D3 column count", len(columns)))
    lift = parse_solution(SOLUTION_D3, "x")
    combination: Poly = {}
    for column, value in lift.items():
        if not (0 <= column < len(columns)):
            fail(("lift column", column))
        descriptor = columns[column]
        generator_index = int(descriptor["generator_index"]) - 1
        if not (0 <= generator_index < len(generators)):
            fail(("generator index", descriptor))
        contribution = multiply(generators[generator_index], monomial(descriptor["multiplier"]))
        combination = add(combination, contribution, value)
    residual = add(target, combination, Fraction(-1))
    if any(sum(key) <= 3 for key in residual):
        fail("D3 lift did not cancel target through degree three")
    quartic = homogeneous(residual, 4)
    if not quartic or any(sum(key) != 4 for key in quartic):
        fail("missing/nonhomogeneous quartic obstruction")
    wrong = add(target, combination)
    if not any(sum(key) <= 3 for key in wrong):
        fail("sign mutation did not expose a lower residual")
    row_keys = [tuple(int(value) for value in key) for key in json.loads(ROWS_D4.read_text())]
    if len(row_keys) != 210 or len(set(row_keys)) != 210:
        fail("D4 row map census")
    dual = parse_solution(DUAL_D4, "y")
    pairing = sum(dual.get(index, Fraction(0)) * quartic.get(key, Fraction(0))
                  for index, key in enumerate(row_keys))
    if pairing != Fraction(25, 45056):
        fail(("quartic dual pairing", pairing))
    quadrics = [homogeneous(row, 2) for row in rows]
    if not valid_quadratic_profile(quadrics):
        fail("unloaded quadratic profile is not Q1..Q5 nonzero and Q6 zero")
    q6_nonzero_mutation = list(quadrics)
    q6_nonzero_mutation[5] = {(2, 0, 0, 0, 0, 0): Fraction(1)}
    if valid_quadratic_profile(q6_nonzero_mutation):
        fail("Q6-nonzero profile mutation was not detected")
    q1_zero_mutation = list(quadrics)
    q1_zero_mutation[0] = {}
    if valid_quadratic_profile(q1_zero_mutation):
        fail("Q1-zero profile mutation was not detected")

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    quartic_path = output / "F10_QUARTIC.txt"
    quartic_path.write_text(poly_text(quartic) + "\n")
    initials_path = output / "UNLOADED_QUADRATIC_INITIALS.txt"
    initials_path.write_text("\n".join(f"Q{i}={poly_text(poly)}" for i, poly in enumerate(quadrics, 1)) + "\n")
    audit = {
        "quartic_terms": len(quartic),
        "quartic_sha256": digest(quartic_path),
        "D3_lift_entries": len(lift),
        "D3_residual_minimum_degree": min(sum(key) for key in residual),
        "D4_dual_entries": len(dual),
        "D4_dual_pairing": str(pairing),
        "sign_mutation_detected": True,
        "Q6_nonzero_profile_mutation_detected": True,
        "Q1_zero_profile_mutation_detected": True,
        "quadratic_term_counts": [len(poly) for poly in quadrics],
    }
    (output / "EXTRACTION_AUDIT.json").write_text(json.dumps(audit, sort_keys=True, indent=2) + "\n")
    lines = ["ring R=0,(x0,x1,x2,x3,x4,x5),dp;"]
    lines.extend(f"poly Q{i}=({poly_text(poly)});" for i, poly in enumerate(quadrics, 1))
    lines.append(f"poly F=({poly_text(quartic)});")
    lines.extend([
        "ideal T=Q1,Q2,Q3,Q4,Q5,Q6; ideal GT=std(T);",
        "poly frem=reduce(F,GT);",
        'if (frem==0) { print("K00_V22_FAIL=QUARTIC_IN_TANGENT_IDEAL"); quit; }',
        "ideal L=T,F; ideal GL=std(L); int proper=(reduce(1,GL)!=0); int dimension=dim(GL);",
        'print("K00_V22_TANGENT_IDEAL_PROPER="+string(reduce(1,GT)!=0));',
        'print("K00_V22_QUARTIC_CLASS_NONZERO=1");',
        'print("K00_V22_LEADING_STRATUM_PROPER="+string(proper));',
        'print("K00_V22_LEADING_STRATUM_AFFINE_DIMENSION="+string(dimension));',
        'write("TANGENT_STANDARD_BASIS.txt",GT); write("LEADING_STRATUM_STANDARD_BASIS.txt",GL); write("F10_TANGENT_REMAINDER.txt",frem);',
        "if ((proper==1)&&(dimension>=1))",
        "{",
        '  write("BRANCH.txt","M1_STRATUM_NONEMPTY_REMAINS");',
        '  print("K00_V22_BRANCH=M1_STRATUM_NONEMPTY_REMAINS");',
        "}",
        "else",
        "{",
        '  write("BRANCH.txt","M1_STRATUM_EMPTY_FORCES_HIGHER_VALUATION");',
        '  print("K00_V22_BRANCH=M1_STRATUM_EMPTY_FORCES_HIGHER_VALUATION");',
        "}",
        'print("K00_V22_ENDPOINT=PASS_EXACT_FIRST_WEIGHTED_STRATUM");',
        "quit;",
    ])
    script = output / "first_weighted_stratum_v22.sing"
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
    required = ("K00_V22_QUARTIC_CLASS_NONZERO=1", "K00_V22_ENDPOINT=PASS_EXACT_FIRST_WEIGHTED_STRATUM")
    if completed.returncode != 0 or any(marker not in completed.stdout for marker in required) or completed.stderr:
        fail(("Singular endpoint", completed.returncode, completed.stdout, completed.stderr))
    branch_match = re.search(r"K00_V22_BRANCH=([A-Z0-9_]+)", completed.stdout)
    dimension_match = re.search(r"K00_V22_LEADING_STRATUM_AFFINE_DIMENSION=(-?\d+)", completed.stdout)
    if branch_match is None or dimension_match is None:
        fail("missing branch/dimension marker")
    result = {
        "status": "PASS_EXACT_FIRST_WEIGHTED_STRATUM",
        "registered_aws_lane": tag,
        "branch": branch_match.group(1),
        "leading_stratum_affine_dimension": int(dimension_match.group(1)),
        "weighted_grade": 6,
        "unit_factor": "k10[0]",
        "quartic_sha256": digest(quartic_path),
        "extraction_audit_sha256": digest(output / "EXTRACTION_AUDIT.json"),
        "singular_script_sha256": digest(script),
        "singular_stdout_sha256": digest(stdout),
        "input_sha256": {str(path.relative_to(ROOT)): digest(path) for path in EXPECTED},
        "dependency": "V20R2_AND_V21R1_PROVISIONAL_PENDING_HOSTILE_REVIEWS",
        "scope": "FIRST_HONEST_WEIGHTED_PREFIX_ONLY_OPEN_F10_NONZERO_EXCLUDED_CLOSED_F10_ZERO_REMAINS_IF_NONEMPTY",
        "firewall": "NO_GRADES7_TO19_NO_FULL_JET_NO_ARC_NO_CLOSURE_NO_JC2",
    }
    result_path = output / "RESULT.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("K00_V22_PRODUCER=PASS")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
