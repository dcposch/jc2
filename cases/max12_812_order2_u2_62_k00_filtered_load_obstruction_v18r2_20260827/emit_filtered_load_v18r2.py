#!/usr/bin/env python3
"""Emit exact filtered matrices from frozen provisional V17 inputs; AWS only."""

from __future__ import annotations

import argparse
import ast
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
import json
import os
from pathlib import Path
import platform
import re


HERE = Path(__file__).resolve().parent
PREREG = HERE / "PREREGISTRATION_Q_PROVISIONAL.md"
EXPECTED_PRELUDE = "5b0a77e6d16df30de2df344862fc4316aedcc8aeabf1ec81e23d7881ce67ee7a"
EXPECTED_P_RESULT = "6e26a3211a86cbda10cdc8ead0e5cfc875964db2c44b225c99733e84fe71bdcc"
EXPECTED_Q_SOURCE = "9e22780c0f9b38f2e502b08ac51c1b9d8fee21e7b40e9569d08d77a3683d8b5c"
NVAR = 6
ZERO = (0,) * NVAR
LOADS = ("K10", "K6", "K2")
Key = tuple[int, int, int, int, int, int]
Poly = dict[Key, Fraction]


def fail(message: object) -> "None":
    raise RuntimeError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only V18 emitter refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only V18 emitter refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def clean(poly: Poly) -> Poly:
    return {key: value for key, value in poly.items() if value}


def add_poly(left: Poly, right: Poly, scale: Fraction = Fraction(1)) -> Poly:
    result = dict(left)
    for key, value in right.items():
        result[key] = result.get(key, Fraction(0)) + scale * value
    return clean(result)


def multiply_poly(left: Poly, right: Poly) -> Poly:
    result: Poly = {}
    for akey, avalue in left.items():
        for bkey, bvalue in right.items():
            key = tuple(a + b for a, b in zip(akey, bkey))
            result[key] = result.get(key, Fraction(0)) + avalue * bvalue
    return clean(result)


def power_poly(poly: Poly, exponent: int) -> Poly:
    if exponent < 0:
        fail(("negative polynomial exponent", exponent))
    result: Poly = {ZERO: Fraction(1)}
    base = poly
    value = exponent
    while value:
        if value & 1:
            result = multiply_poly(result, base)
        value >>= 1
        if value:
            base = multiply_poly(base, base)
    return result


def evaluate_expression(node: ast.AST) -> Poly:
    if isinstance(node, ast.Constant) and isinstance(node.value, int):
        return {ZERO: Fraction(node.value)} if node.value else {}
    if isinstance(node, ast.Name) and re.fullmatch(r"d[0-5]", node.id):
        key = [0] * NVAR
        key[int(node.id[1])] = 1
        return {tuple(key): Fraction(1)}
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
        value = evaluate_expression(node.operand)
        return value if isinstance(node.op, ast.UAdd) else {key: -coefficient for key, coefficient in value.items()}
    if isinstance(node, ast.BinOp):
        if isinstance(node.op, ast.Add):
            return add_poly(evaluate_expression(node.left), evaluate_expression(node.right))
        if isinstance(node.op, ast.Sub):
            return add_poly(evaluate_expression(node.left), evaluate_expression(node.right), Fraction(-1))
        if isinstance(node.op, ast.Mult):
            return multiply_poly(evaluate_expression(node.left), evaluate_expression(node.right))
        if isinstance(node.op, ast.Div):
            numerator = evaluate_expression(node.left)
            denominator = evaluate_expression(node.right)
            if set(denominator) != {ZERO} or denominator[ZERO] == 0:
                fail(("nonconstant/zero polynomial denominator", ast.dump(node.right)))
            return {key: value / denominator[ZERO] for key, value in numerator.items()}
        if isinstance(node.op, ast.Pow):
            if not isinstance(node.right, ast.Constant) or not isinstance(node.right.value, int):
                fail(("noninteger polynomial exponent", ast.dump(node.right)))
            return power_poly(evaluate_expression(node.left), node.right.value)
    fail(("unsupported polynomial syntax", ast.dump(node)))


def parse_poly(text: str) -> Poly:
    source = "".join(text.split())
    if not source or any(char in source for char in ";,\""):
        fail(("malformed polynomial", source[:120]))
    try:
        tree = ast.parse(source.replace("^", "**"), mode="eval")
    except SyntaxError as error:
        fail(("polynomial syntax error", source[:120], str(error)))
    return clean(evaluate_expression(tree.body))


def parse_rows(prelude: Path) -> list[Poly]:
    text = prelude.read_text()
    rows: list[Poly] = []
    for index in range(1, 7):
        match = re.search(rf"(?:^|\n)poly r{index}=(.*?);", text, re.S)
        if not match:
            fail(("missing prelude row", index))
        rows.append(parse_poly(match.group(1)))
    if len(rows) != 6:
        fail("row count")
    return rows


def parse_ideal(path: Path) -> list[Poly]:
    text = "".join(path.read_text().split())
    if not text:
        fail(("empty ideal serialization", str(path)))
    return [parse_poly(piece) for piece in text.split(",")]


def order(poly: Poly) -> int | None:
    return min((sum(key) for key in poly), default=None)


def max_degree(poly: Poly) -> int | None:
    return max((sum(key) for key in poly), default=None)


@lru_cache(maxsize=None)
def monomials(degree: int, variables: int = NVAR) -> tuple[Key, ...]:
    def build(left: int, count: int, prefix: tuple[int, ...]):
        if count == 1:
            yield prefix + (left,)
            return
        for exponent in range(left + 1):
            yield from build(left - exponent, count - 1, prefix + (exponent,))
    return tuple(build(degree, variables, ()))


def all_monomials(maximum: int) -> tuple[Key, ...]:
    return tuple(key for degree in range(maximum + 1) for key in monomials(degree))


def coefficient_text(value: Fraction) -> tuple[str, str]:
    return str(value.numerator), str(value.denominator)


def poly_summary(poly: Poly) -> dict[str, object]:
    counts: dict[str, int] = {}
    for key in poly:
        degree = str(sum(key))
        counts[degree] = counts.get(degree, 0) + 1
    return {
        "terms": len(poly),
        "minimum_degree": order(poly),
        "maximum_degree": max_degree(poly),
        "degree_term_counts": counts,
    }


def write_matrix(output: Path, label: str, generators: list[Poly], target: Poly,
                 cutoff: int) -> dict[str, object]:
    row_keys = all_monomials(cutoff)
    row_index = {key: index for index, key in enumerate(row_keys)}
    columns: list[tuple[int, Key]] = []
    for generator_index, generator in enumerate(generators):
        minimum = order(generator)
        if minimum is None or minimum > cutoff:
            continue
        for multiplier_degree in range(cutoff - minimum + 1):
            for multiplier in monomials(multiplier_degree):
                columns.append((generator_index, multiplier))
    entries: dict[tuple[int, int], Fraction] = {}
    for column, (generator_index, multiplier) in enumerate(columns):
        for key, value in generators[generator_index].items():
            shifted = tuple(a + b for a, b in zip(key, multiplier))
            if sum(shifted) <= cutoff:
                location = (row_index[shifted], column)
                entries[location] = entries.get(location, Fraction(0)) + value
    target_column = len(columns)
    for key, value in target.items():
        if sum(key) <= cutoff:
            entries[(row_index[key], target_column)] = value
    entries = {key: value for key, value in entries.items() if value}
    stem = f"{label}_D{cutoff}"
    matrix = output / f"matrix_{stem}.tsv"
    with matrix.open("w") as handle:
        handle.write(f"{len(row_keys)} {len(columns)} {len(entries)} {cutoff}\n")
        for (row, column), value in sorted(entries.items()):
            numerator, denominator = coefficient_text(value)
            handle.write(f"{row} {column} {numerator} {denominator}\n")
    row_map = output / f"rows_{stem}.json"
    row_map.write_text(json.dumps([list(key) for key in row_keys], separators=(",", ":")) + "\n")
    column_map = output / f"columns_{stem}.json"
    column_map.write_text(json.dumps([
        {"generator_index": generator + 1, "multiplier": list(multiplier)}
        for generator, multiplier in columns
    ], separators=(",", ":")) + "\n")
    return {
        "direction": label,
        "cutoff": cutoff,
        "rows": len(row_keys),
        "columns": len(columns),
        "nonzero_entries_including_target": len(entries),
        "matrix_sha256": digest(matrix),
        "row_map_sha256": digest(row_map),
        "column_map_sha256": digest(column_map),
        "row_order": "total_degree_0_to_D_then_recursive_lex_d0_to_d5",
        "column_order": "r1_to_r6_then_E_serialization; multiplier_degree_then_recursive_lex",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("exact_input_lane", type=Path)
    parser.add_argument("p_v17_result", type=Path)
    parser.add_argument("row_prelude", type=Path)
    parser.add_argument("--field", choices=("Q",), required=True)
    parser.add_argument("--max-cutoff", type=int, default=6, choices=range(2, 7))
    args = parser.parse_args()
    tag = require_aws()
    manifest_path = args.exact_input_lane / "run/PROVISIONAL_EXACT_INPUT.json"
    artifact_dir = args.exact_input_lane / "run/artifacts"
    if digest(args.row_prelude) != EXPECTED_PRELUDE:
        fail(("row prelude hash mismatch", digest(args.row_prelude)))
    manifest = json.loads(manifest_path.read_text())
    p_result = json.loads(args.p_v17_result.read_text())
    if digest(args.p_v17_result) != EXPECTED_P_RESULT:
        fail(("V17 p result hash mismatch", digest(args.p_v17_result)))
    if (manifest.get("status") != "PASS-K00-V18-PROVISIONAL-EXACT-INPUT" or
            manifest.get("field") != "Q" or manifest.get("syz6_generators") != 66 or
            manifest.get("compiled_v17_q_sha256") != EXPECTED_Q_SOURCE or
            manifest.get("p_v17_result_sha256") != EXPECTED_P_RESULT):
        fail(("provisional exact-input sentinel mismatch", manifest))
    if p_result.get("status") != "PASS-K00-FIRSTORDER-COKERNEL-V17-ENDPOINT" or p_result.get("field") != "65521":
        fail("V17 p endpoint sentinel mismatch")
    rows = parse_rows(args.row_prelude)
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    directions: dict[str, object] = {}
    matrices: list[dict[str, object]] = []
    for label in LOADS:
        endpoint = p_result.get("directions", {}).get(label, {})
        if endpoint.get("branch") != "LOCAL_NONZERO" or endpoint.get("local_class_zero") is not False:
            fail(("V18 requires a V17 locally nonzero branch", label, endpoint))
        image_path = artifact_dir / f"IMAGE_{label}.txt"
        target_path = artifact_dir / f"TARGET_{label}.txt"
        expected = manifest.get("artifact_sha256", {})
        if digest(image_path) != expected.get(f"IMAGE_{label}.txt"):
            fail(("image hash mismatch", label))
        if digest(target_path) != expected.get(f"TARGET_{label}.txt"):
            fail(("target hash mismatch", label))
        image = parse_ideal(image_path)
        if len(image) != 66:
            fail(("six-row image generator count", label, len(image)))
        target = parse_poly(target_path.read_text())
        if not target or order(target) is None or order(target) < 2:
            fail(("target order sentinel", label, poly_summary(target)))
        generators = rows + image
        for cutoff in range(2, args.max_cutoff + 1):
            matrices.append(write_matrix(output, label, generators, target, cutoff))
        directions[label] = {
            "image_sha256": digest(image_path),
            "target_sha256": digest(target_path),
            "image_generators": len(image),
            "generator_summaries": [poly_summary(poly) for poly in generators],
            "target_summary": poly_summary(target),
        }
    audit = {
        "status": "PASS-K00-FILTERED-LOAD-V18R2-PROVISIONAL-Q-EMITTER",
        "registered_aws_lane": tag,
        "field": args.field,
        "characteristic": 0 if args.field == "Q" else 65521,
        "max_cutoff": args.max_cutoff,
        "preregistration_sha256": digest(PREREG),
        "provisional_exact_input_manifest_sha256": digest(manifest_path),
        "v17_p_result_sha256": digest(args.p_v17_result),
        "v17_evidence_status": "PROVISIONAL_EXACT_INPUTS_WITH_V17_P_BRANCHES",
        "row_prelude_sha256": digest(args.row_prelude),
        "row_summaries": [poly_summary(row) for row in rows],
        "directions": directions,
        "matrices": matrices,
        "scope": "PROVISIONAL_EXACT_Q_SEPARATE_FILTERED_FIRST_LOAD_CLASSES_AT_NORMALIZED_K00_ONLY",
        "firewall": "NO_PROMOTION_BEFORE_V17_Q_NO_COUPLING_NO_LAMBDA19_NO_HONEST_SOURCE_REACHABILITY_NO_ARC_EXCLUSION",
    }
    audit_path = output / "SOURCE_AUDIT.json"
    audit_path.write_text(json.dumps(audit, sort_keys=True, indent=2) + "\n")
    print("K00_V18_SOURCE_AUDIT=PASS")
    print(json.dumps(audit, sort_keys=True))


if __name__ == "__main__":
    main()
