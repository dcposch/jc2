#!/usr/bin/env python3
"""Compile the exact contracted K00 Lambda<=19 source on registered AWS."""

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
from typing import Callable


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
TAILS = ROOT / "cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json"
V7 = ROOT / "cases/max12_812_order2_u2_62_k00_unloaded_membership_v7_20260827/compile_unloaded_membership.py"
V14 = ROOT / "cases/max12_812_order2_u2_62_k00_colon_local_v14r1_20260827/aws_q_box01_pass"
PRELUDE = V14 / "compiled/serialized_replay_prelude_Q.sing"
S87 = V14 / "run/artifacts/SYZYGY_MODULE.txt"
H = V14 / "run/artifacts/LOCAL_UNIT_WITNESS_R1.txt"
U = [V14 / f"run/artifacts/UNIT_MULTIPLIER_{i}.txt" for i in range(1, 7)]
V21 = ROOT / "cases/max12_812_order2_u2_62_k00_filtered_dual_local_nonmembership_v21_20260827/aws_q_box01_r1_pass"
S66 = V21 / "input/syz6.txt"
S66_FRESH = V21 / "run/output/FRESH_SYZ6_MODULE.txt"
V21_INPUT_MANIFEST = V21 / "input/INPUT.sha256"
V20_R0 = HERE / "PREREGISTRATION.md"
ERRATUM = HERE / "DESIGN_ERRATUM_V20R1.md"
PREREG = HERE / "PREREGISTRATION_V20R2_SOURCE_COMPILER.md"

EXPECTED = {
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    V7: "a7f335cdbc3e5525ce641ff10d8370a52d4cbb9c84e2417b17eea64a38154f70",
    PRELUDE: "5b0a77e6d16df30de2df344862fc4316aedcc8aeabf1ec81e23d7881ce67ee7a",
    S87: "788a836b729d3de5e9600de07244b5d4b836c91a7538e0b1e4ef307ad86d21fb",
    H: "87ced4afe1680f11073eb62bda7c7894f297925283557b2ccf0e951daba09e04",
    U[0]: "ed096c8246ff96cb5ab621a9a74061b24e1678ff061a98137a067c387969e1e5",
    U[1]: "1f8369edbbb10bfbbb155250775399170e696e0fdbe33bb75f54bb5639f78791",
    U[2]: "ce8b51a7e9a11f0fa3a3594480fbe3e4b556e9fd0a17cf29175b273474104f0f",
    U[3]: "5d9f371cf8302502d05a56effbfe3bbbbeafd28d6dfdad8cf7f1bba3ebb60f18",
    U[4]: "135c17e36fd53a438e98c36104e350e6ed362223dfba38e7e927c6dccf65a98e",
    U[5]: "93762abdfa9b12b520a47848e55776176d9227eaca253deb80a6a9a13b4c3295",
    S66: "83832f380ce11a491c9799e50ff8b36b5fbc3a6b0d5b5dc52d90b6239c129a7a",
    S66_FRESH: "83832f380ce11a491c9799e50ff8b36b5fbc3a6b0d5b5dc52d90b6239c129a7a",
    V21_INPUT_MANIFEST: "38c6dd45b888ec04a5c0b9bdd4b93625a1df491b4e4f63851f5546cb1d7d465f",
    V20_R0: "4cdbd2ca462378adbcd0fba103f79a2ad9e5fbd6c6a7d81682ebc45230c2b1c4",
    ERRATUM: "0f2debfecf1ae127db20de8a806e93842a0f333fce3592a3e09231a48ad3b53b",
    PREREG: "1148e7836458966aa382dae27cdbfd7c9d156b53911ba9f48efdb6eb9649edec",
}
EXPECTED_CANONICAL_TAILS = "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"
NVAR = 6
ZERO_KEY = (0,) * NVAR
TRUNCATION = 20
TAIL_NAMES = [f"C{i}" for i in range(7)] + ["k10", "k6", "k2"]
TAIL_WEIGHTS = [8 - i for i in range(7)] + [2, 6, 10]
LOADS = {"K10": 7, "K6": 8, "K2": 9}
PARAMETERS = ("p10", "p6", "p2", "pmu2", "pmu4", "pmu6", "pJ")
Key = tuple[int, int, int, int, int, int]
Poly = dict[Key, Fraction]


def fail(message: object) -> "None":
    raise RuntimeError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only V20R2 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only V20R2 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def clean(poly: Poly) -> Poly:
    return {key: value for key, value in poly.items() if value}


def poly_add(left: Poly, right: Poly, scale: Fraction = Fraction(1)) -> Poly:
    out = dict(left)
    for key, value in right.items():
        out[key] = out.get(key, Fraction(0)) + scale * value
        if out[key] == 0:
            del out[key]
    return out


def poly_mul(left: Poly, right: Poly) -> Poly:
    out: Poly = {}
    for akey, avalue in left.items():
        for bkey, bvalue in right.items():
            key = tuple(a + b for a, b in zip(akey, bkey))
            out[key] = out.get(key, Fraction(0)) + avalue * bvalue
    return clean(out)


def poly_scale(poly: Poly, value: Fraction) -> Poly:
    return clean({key: coefficient * value for key, coefficient in poly.items()})


def poly_power(poly: Poly, exponent: int) -> Poly:
    if exponent < 0:
        fail(("negative exponent", exponent))
    out: Poly = {ZERO_KEY: Fraction(1)}
    base = poly
    while exponent:
        if exponent & 1:
            out = poly_mul(out, base)
        exponent >>= 1
        if exponent:
            base = poly_mul(base, base)
    return out


def variable(index: int) -> Poly:
    key = [0] * NVAR
    key[index] = 1
    return {tuple(key): Fraction(1)}


def eval_ast(node: ast.AST) -> Poly:
    if isinstance(node, ast.Constant) and isinstance(node.value, int):
        return {} if node.value == 0 else {ZERO_KEY: Fraction(node.value)}
    if isinstance(node, ast.Name) and re.fullmatch(r"d[0-5]", node.id):
        return variable(int(node.id[1]))
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
        value = eval_ast(node.operand)
        return value if isinstance(node.op, ast.UAdd) else poly_scale(value, Fraction(-1))
    if isinstance(node, ast.BinOp):
        if isinstance(node.op, ast.Add):
            return poly_add(eval_ast(node.left), eval_ast(node.right))
        if isinstance(node.op, ast.Sub):
            return poly_add(eval_ast(node.left), eval_ast(node.right), Fraction(-1))
        if isinstance(node.op, ast.Mult):
            return poly_mul(eval_ast(node.left), eval_ast(node.right))
        if isinstance(node.op, ast.Div):
            numerator, denominator = eval_ast(node.left), eval_ast(node.right)
            if set(denominator) != {ZERO_KEY} or denominator[ZERO_KEY] == 0:
                fail(("nonconstant denominator", ast.dump(node.right)))
            return poly_scale(numerator, Fraction(1, 1) / denominator[ZERO_KEY])
        if isinstance(node.op, ast.Pow):
            if not isinstance(node.right, ast.Constant) or not isinstance(node.right.value, int):
                fail(("noninteger exponent", ast.dump(node.right)))
            return poly_power(eval_ast(node.left), node.right.value)
    fail(("unsupported polynomial syntax", ast.dump(node)))


def parse_poly(text: str) -> Poly:
    source = "".join(text.split())
    if not source or any(char in source for char in ';,"'):
        fail(("malformed polynomial", source[:120]))
    return eval_ast(ast.parse(source.replace("^", "**"), mode="eval").body)


def parse_prelude_rows() -> list[Poly]:
    text = PRELUDE.read_text()
    rows: list[Poly] = []
    for index in range(1, 8):
        match = re.search(rf"(?:^|\n)poly r{index}=(.*?);", text, re.S)
        if match is None:
            fail(("missing prelude row", index))
        rows.append(parse_poly(match.group(1)))
    return rows


def parse_ideal(path: Path) -> list[Poly]:
    text = "".join(path.read_text().split())
    if not text:
        fail(("empty ideal", str(path)))
    return [parse_poly(piece) for piece in text.split(",")]


def coordinate_images() -> list[Poly]:
    one = {ZERO_KEY: Fraction(1)}
    return [
        poly_scale(poly_add(one, variable(0)), Fraction(1, 256)),
        variable(1),
        poly_scale(poly_add(one, variable(2)), Fraction(1, 16)),
        variable(3),
        poly_scale(poly_add(poly_scale(one, Fraction(3)), variable(4)), Fraction(1, 8)),
        variable(5),
        one,
    ]


def reconstruct_tails(tails: dict[str, list[list[object]]]) -> tuple[list[Poly], dict[str, list[Poly]]]:
    images = coordinate_images()
    rows = [{} for _ in range(7)]
    loads = {label: [{} for _ in range(7)] for label in LOADS}
    term_count = 0
    for ell in range(1, 8):
        for raw_monomial, raw_coefficient in tails[str(ell)]:
            term_count += 1
            monomial = [int(value) for value in raw_monomial]
            coefficient = Fraction(str(raw_coefficient))
            if len(monomial) != 10 or any(value < 0 for value in monomial):
                fail(("malformed tail monomial", ell, monomial))
            if sum(a * b for a, b in zip(monomial, TAIL_WEIGHTS)) != 12 + ell:
                fail(("tail weight mismatch", ell, monomial))
            if sum(monomial[7:]) > 1 or any(value not in (0, 1) for value in monomial[7:]):
                fail(("tail load nonlinearity", ell, monomial))
            poly: Poly = {ZERO_KEY: coefficient}
            for index, exponent in enumerate(monomial[:7]):
                if exponent:
                    poly = poly_mul(poly, poly_power(images[index], exponent))
            active = [label for label, index in LOADS.items() if monomial[index]]
            if not active:
                rows[ell - 1] = poly_add(rows[ell - 1], poly)
            elif len(active) == 1:
                label = active[0]
                loads[label][ell - 1] = poly_add(loads[label][ell - 1], poly)
            else:
                fail(("multiple active loads", ell, active))
    if term_count != 569:
        fail(("tail term census", term_count))
    return rows, loads


class Dag:
    """Small hash-consed arithmetic DAG with exact rational constants."""

    def __init__(self) -> None:
        self.nodes: list[list[object]] = []
        self.cache: dict[tuple[object, ...], int] = {}
        self.constants: dict[int, Fraction] = {}

    def intern(self, key: tuple[object, ...], record: list[object]) -> int:
        if key in self.cache:
            return self.cache[key]
        index = len(self.nodes)
        self.nodes.append(record)
        self.cache[key] = index
        return index

    def const(self, value: Fraction | int) -> int:
        value = Fraction(value)
        key = ("c", value.numerator, value.denominator)
        index = self.intern(key, ["c", value.numerator, value.denominator])
        self.constants[index] = value
        return index

    def var(self, name: str) -> int:
        return self.intern(("v", name), ["v", name])

    def add(self, left: int, right: int) -> int:
        if self.constants.get(left) == 0:
            return right
        if self.constants.get(right) == 0:
            return left
        if left == right:
            return self.mul(self.const(2), left)
        if left > right:
            left, right = right, left
        if left in self.constants and right in self.constants:
            return self.const(self.constants[left] + self.constants[right])
        return self.intern(("a", left, right), ["a", left, right])

    def neg(self, node: int) -> int:
        return self.mul(self.const(-1), node)

    def sub(self, left: int, right: int) -> int:
        return self.add(left, self.neg(right))

    def mul(self, left: int, right: int) -> int:
        if self.constants.get(left) == 0 or self.constants.get(right) == 0:
            return self.const(0)
        if self.constants.get(left) == 1:
            return right
        if self.constants.get(right) == 1:
            return left
        if left > right:
            left, right = right, left
        if left in self.constants and right in self.constants:
            return self.const(self.constants[left] * self.constants[right])
        return self.intern(("m", left, right), ["m", left, right])

    def scale(self, series: list[int], value: Fraction) -> list[int]:
        factor = self.const(value)
        return [self.mul(factor, node) for node in series]

    def series_zero(self) -> list[int]:
        return [self.const(0)] * TRUNCATION

    def series_add(self, left: list[int], right: list[int]) -> list[int]:
        return [self.add(a, b) for a, b in zip(left, right)]

    def series_sub(self, left: list[int], right: list[int]) -> list[int]:
        return [self.sub(a, b) for a, b in zip(left, right)]

    def series_mul(self, left: list[int], right: list[int]) -> list[int]:
        zero = self.const(0)
        out = [zero] * TRUNCATION
        for i, a in enumerate(left):
            if self.constants.get(a) == 0:
                continue
            for j, b in enumerate(right[:TRUNCATION - i]):
                if self.constants.get(b) == 0:
                    continue
                out[i + j] = self.add(out[i + j], self.mul(a, b))
        return out

    def series_power(self, series: list[int], exponent: int) -> list[int]:
        out = self.series_zero()
        out[0] = self.const(1)
        base = series
        while exponent:
            if exponent & 1:
                out = self.series_mul(out, base)
            exponent >>= 1
            if exponent:
                base = self.series_mul(base, base)
        return out

    def shift(self, series: list[int], amount: int) -> list[int]:
        if amount < 0:
            fail(("negative series shift", amount))
        return [self.const(0)] * min(amount, TRUNCATION) + series[:max(0, TRUNCATION - amount)]


def source_columns() -> list[dict[str, object]]:
    specs = [
        *(('d', f'd{j}', 1, 19, set()) for j in range(6)),
        ('load', 'k10', 0, 17, set()),
        ('load', 'k6', 0, 13, {0}),
        ('load', 'k2', 0, 9, {0}),
        ('target', 'mu2', 0, 5, {0}),
        ('target', 'mu4', 0, 3, {0}),
        ('target', 'mu6', 0, 1, {0}),
        ('jacobian', 'Jdet', 0, 0, set()),
    ]
    first_grade = {'d': 0, 'k10': 2, 'k6': 6, 'k2': 10,
                   'mu2': 14, 'mu4': 16, 'mu6': 18, 'Jdet': 19}
    columns: list[dict[str, object]] = []
    for kind, name, start, end, boundary in specs:
        for index in range(start, end + 1):
            columns.append({
                "column": len(columns),
                "kind": kind,
                "name": name,
                "series_index": index,
                "first_Lambda_grade": (0 if kind == "d" else first_grade[name]) + index,
                "boundary_status": "FIXED_ZERO_BEFORE_SOLVE" if index in boundary else "FREE",
                "variable": f"{name}_{index}",
            })
    if len(columns) != 169 or sum(column["boundary_status"] == "FREE" for column in columns) != 164:
        fail(("source column census", len(columns)))
    return columns


def build_source_series(dag: Dag, columns: list[dict[str, object]],
                        restrict_boundary: bool) -> dict[str, list[int]]:
    grouped: dict[str, list[dict[str, object]]] = {}
    for column in columns:
        grouped.setdefault(str(column["name"]), []).append(column)
    out: dict[str, list[int]] = {}
    for name, entries in grouped.items():
        series = dag.series_zero()
        for column in entries:
            grade = int(column["series_index"])
            if restrict_boundary and column["boundary_status"] != "FREE":
                node = dag.const(0)
            else:
                node = dag.var(str(column["variable"]))
            series[grade] = node
        out[name] = series
    return out


def k00_coordinate_series(dag: Dag, source: dict[str, list[int]]) -> list[list[int]]:
    one = dag.series_zero()
    one[0] = dag.const(1)
    three = dag.series_zero()
    three[0] = dag.const(3)
    return [
        dag.scale(dag.series_add(one, source["d0"]), Fraction(1, 256)),
        source["d1"],
        dag.scale(dag.series_add(one, source["d2"]), Fraction(1, 16)),
        source["d3"],
        dag.scale(dag.series_add(three, source["d4"]), Fraction(1, 8)),
        source["d5"],
        one,
    ]


def tail_dag_rows(dag: Dag, tails: dict[str, list[list[object]]],
                  source: dict[str, list[int]], k6_shift: int = 6,
                  target_sign: int = -1) -> list[list[int]]:
    coordinates = k00_coordinate_series(dag, source)
    tail_series = coordinates + [
        dag.shift(source["k10"], 2),
        dag.shift(source["k6"], k6_shift),
        dag.shift(source["k2"], 10),
    ]
    power_cache: dict[tuple[int, int], list[int]] = {}
    rows = [dag.series_zero() for _ in range(7)]
    for ell in range(1, 8):
        row = rows[ell - 1]
        for raw_monomial, raw_coefficient in tails[str(ell)]:
            monomial = [int(value) for value in raw_monomial]
            term = dag.series_zero()
            term[0] = dag.const(Fraction(str(raw_coefficient)))
            for index, exponent in enumerate(monomial):
                if not exponent:
                    continue
                key = (index, exponent)
                if key not in power_cache:
                    power_cache[key] = dag.series_power(tail_series[index], exponent)
                term = dag.series_mul(term, power_cache[key])
            row = dag.series_add(row, term)
        rows[ell - 1] = row
    target_specs = {2: ("mu2", 14, Fraction(target_sign)),
                    4: ("mu4", 16, Fraction(target_sign)),
                    6: ("mu6", 18, Fraction(target_sign)),
                    7: ("Jdet", 19, Fraction(target_sign, 4))}
    for ell, (name, shift, scale) in target_specs.items():
        rows[ell - 1] = dag.series_add(rows[ell - 1], dag.scale(dag.shift(source[name], shift), scale))
    return rows


def poly_dag_series(dag: Dag, poly: Poly, source: dict[str, list[int]]) -> list[int]:
    variables = [source[f"d{i}"] for i in range(6)]
    powers: dict[tuple[int, int], list[int]] = {}
    out = dag.series_zero()
    for key, coefficient in poly.items():
        term = dag.series_zero()
        term[0] = dag.const(coefficient)
        for index, exponent in enumerate(key):
            if not exponent:
                continue
            cache_key = (index, exponent)
            if cache_key not in powers:
                powers[cache_key] = dag.series_power(variables[index], exponent)
            term = dag.series_mul(term, powers[cache_key])
        out = dag.series_add(out, term)
    return out


def evaluate_dag(dag: Dag, assignment: dict[str, object],
                 convert: Callable[[Fraction], object],
                 modulus: int | None = None) -> list[object]:
    values: list[object] = []
    for node in dag.nodes:
        if node[0] == "c":
            values.append(convert(Fraction(int(node[1]), int(node[2]))))
        elif node[0] == "v":
            values.append(assignment[str(node[1])])
        elif node[0] == "a":
            value = values[int(node[1])] + values[int(node[2])]
            values.append(value % modulus if modulus else value)
        elif node[0] == "m":
            value = values[int(node[1])] * values[int(node[2])]
            values.append(value % modulus if modulus else value)
        else:
            fail(("unknown DAG opcode", node))
    return values


def num_zero() -> list[object]:
    return [0] * TRUNCATION


def num_add(left: list[object], right: list[object], modulus: int | None) -> list[object]:
    out = [a + b for a, b in zip(left, right)]
    return [value % modulus for value in out] if modulus else out


def num_scale(series: list[object], value: object, modulus: int | None) -> list[object]:
    out = [value * coefficient for coefficient in series]
    return [entry % modulus for entry in out] if modulus else out


def num_mul(left: list[object], right: list[object], modulus: int | None) -> list[object]:
    out = num_zero()
    for i, a in enumerate(left):
        if not a:
            continue
        for j, b in enumerate(right[:TRUNCATION - i]):
            if b:
                out[i + j] += a * b
    return [value % modulus for value in out] if modulus else out


def num_power(series: list[object], exponent: int, one: object,
              modulus: int | None) -> list[object]:
    out = num_zero()
    out[0] = one
    base = series
    while exponent:
        if exponent & 1:
            out = num_mul(out, base, modulus)
        exponent >>= 1
        if exponent:
            base = num_mul(base, base, modulus)
    return out


def num_shift(series: list[object], amount: int) -> list[object]:
    return [0] * min(amount, TRUNCATION) + series[:max(0, TRUNCATION - amount)]


def make_assignment(columns: list[dict[str, object]], fixture: int,
                    modulus: int | None) -> dict[str, object]:
    assignment: dict[str, object] = {}
    for column in columns:
        name = str(column["variable"])
        raw = int.from_bytes(sha256(f"V20R2|{fixture}|{name}".encode()).digest()[:4], "big")
        value = raw % 7 - 3
        if column["boundary_status"] != "FREE" and value == 0:
            value = 1
        assignment[name] = value % modulus if modulus else Fraction(value)
    assignment["k10_0"] = (fixture + 1) % modulus if modulus else Fraction(fixture + 1)
    assignment["Jdet_0"] = (fixture + 3) % modulus if modulus else Fraction(fixture + 3)
    return assignment


def numeric_source(columns: list[dict[str, object]], assignment: dict[str, object],
                   restrict_boundary: bool) -> dict[str, list[object]]:
    out: dict[str, list[object]] = {}
    for column in columns:
        name = str(column["name"])
        series = out.setdefault(name, num_zero())
        if restrict_boundary and column["boundary_status"] != "FREE":
            value: object = 0
        else:
            value = assignment[str(column["variable"])]
        series[int(column["series_index"])] = value
    return out


def numeric_coordinate_series(source: dict[str, list[object]],
                              convert: Callable[[Fraction], object],
                              modulus: int | None) -> list[list[object]]:
    one = num_zero()
    one[0] = convert(Fraction(1))
    three = num_zero()
    three[0] = convert(Fraction(3))
    return [
        num_scale(num_add(one, source["d0"], modulus), convert(Fraction(1, 256)), modulus),
        source["d1"],
        num_scale(num_add(one, source["d2"], modulus), convert(Fraction(1, 16)), modulus),
        source["d3"],
        num_scale(num_add(three, source["d4"], modulus), convert(Fraction(1, 8)), modulus),
        source["d5"],
        one,
    ]


def direct_tail_rows(tails: dict[str, list[list[object]]], columns: list[dict[str, object]],
                     assignment: dict[str, object], convert: Callable[[Fraction], object],
                     modulus: int | None, restrict_boundary: bool = True,
                     k6_shift: int = 6, target_sign: int = -1) -> tuple[list[list[object]], dict[str, list[object]]]:
    source = numeric_source(columns, assignment, restrict_boundary)
    tail_series = numeric_coordinate_series(source, convert, modulus) + [
        num_shift(source["k10"], 2),
        num_shift(source["k6"], k6_shift),
        num_shift(source["k2"], 10),
    ]
    rows = [num_zero() for _ in range(7)]
    power_cache: dict[tuple[int, int], list[object]] = {}
    for ell in range(1, 8):
        for raw_monomial, raw_coefficient in tails[str(ell)]:
            monomial = [int(value) for value in raw_monomial]
            term = num_zero()
            term[0] = convert(Fraction(str(raw_coefficient)))
            for index, exponent in enumerate(monomial):
                if not exponent:
                    continue
                key = (index, exponent)
                if key not in power_cache:
                    power_cache[key] = num_power(tail_series[index], exponent, convert(Fraction(1)), modulus)
                term = num_mul(term, power_cache[key], modulus)
            rows[ell - 1] = num_add(rows[ell - 1], term, modulus)
    targets = {2: ("mu2", 14, Fraction(target_sign)),
               4: ("mu4", 16, Fraction(target_sign)),
               6: ("mu6", 18, Fraction(target_sign)),
               7: ("Jdet", 19, Fraction(target_sign, 4))}
    for ell, (name, shift, coefficient) in targets.items():
        target = num_scale(num_shift(source[name], shift), convert(coefficient), modulus)
        rows[ell - 1] = num_add(rows[ell - 1], target, modulus)
    return rows, source


def numeric_poly_series(poly: Poly, source: dict[str, list[object]],
                        convert: Callable[[Fraction], object],
                        modulus: int | None) -> list[object]:
    variables = [source[f"d{i}"] for i in range(6)]
    powers: dict[tuple[int, int], list[object]] = {}
    out = num_zero()
    for key, coefficient in poly.items():
        term = num_zero()
        term[0] = convert(coefficient)
        for index, exponent in enumerate(key):
            if not exponent:
                continue
            cache_key = (index, exponent)
            if cache_key not in powers:
                powers[cache_key] = num_power(variables[index], exponent, convert(Fraction(1)), modulus)
            term = num_mul(term, powers[cache_key], modulus)
        out = num_add(out, term, modulus)
    return out


def residual_fixture(rows: list[list[object]], source: dict[str, list[object]],
                     h: Poly, multipliers: list[Poly], targets: dict[str, Poly],
                     convert: Callable[[Fraction], object], modulus: int | None) -> bool:
    hs = numeric_poly_series(h, source, convert, modulus)
    us = [numeric_poly_series(poly, source, convert, modulus) for poly in multipliers]
    left = num_mul(hs, rows[6], modulus)
    for index in range(6):
        left = num_add(left, num_scale(num_mul(us[index], rows[index], modulus), -1, modulus), modulus)
    right = num_zero()
    for label, source_name, shift in (("K10", "k10", 2), ("K6", "k6", 6), ("K2", "k2", 10)):
        term = num_mul(num_shift(source[source_name], shift),
                       numeric_poly_series(targets[label], source, convert, modulus), modulus)
        right = num_add(right, term, modulus)
    for index, (name, shift) in ((1, ("mu2", 14)), (3, ("mu4", 16)), (5, ("mu6", 18))):
        term = num_mul(us[index], num_shift(source[name], shift), modulus)
        right = num_add(right, term, modulus)
    jterm = num_mul(hs, num_shift(source["Jdet"], 19), modulus)
    right = num_add(right, num_scale(jterm, convert(Fraction(-1, 4)), modulus), modulus)
    if modulus:
        left = [value % modulus for value in left]
        right = [value % modulus for value in right]
    return left == right


def poly_text(poly: Poly) -> str:
    if not poly:
        return "0"
    terms: list[str] = []
    for key, coefficient in sorted(poly.items()):
        factors = [f"d{i}^{exponent}" if exponent != 1 else f"d{i}"
                   for i, exponent in enumerate(key) if exponent]
        body = "*".join(factors) or "1"
        ctext = str(coefficient.numerator) if coefficient.denominator == 1 else f"({coefficient.numerator}/{coefficient.denominator})"
        terms.append(f"({ctext})*{body}")
    return "+".join(terms).replace("+(-", "-(")


def safe_serialization(path: Path) -> str:
    value = path.read_text().strip()
    if not value or '"' in value or "\r" in value:
        fail(("malformed Singular serialization", str(path)))
    return value


def load_declarations(loads: dict[str, list[Poly]]) -> list[str]:
    lines: list[str] = []
    for label in ("K10", "K6", "K2"):
        for index, poly in enumerate(loads[label], 1):
            lines.append(f"poly a{label}{index}=({poly_text(poly)});")
    return lines


def common_singular_declarations(loads: dict[str, list[Poly]]) -> list[str]:
    return [
        *load_declarations(loads),
        f"poly h=({safe_serialization(H)});",
        *(f"poly u{i}=({safe_serialization(path)});" for i, path in enumerate(U, 1)),
        "ideal I=r1,r2,r3,r4,r5,r6; ideal A=r1,r2,r3,r4,r5,r6,r7;",
        f"module T=({safe_serialization(S66)});",
        f"module S87=({safe_serialization(S87)});",
    ]


def singular_gamma_lines() -> list[str]:
    lines = [
        "module Gamma; poly g10; poly g6; poly g2; vector gv;",
        "for (j=1; j<=size(T); j++)",
        "{",
        "  g10=T[j][1]*aK101+T[j][2]*aK102+T[j][3]*aK103+T[j][4]*aK104+T[j][5]*aK105+T[j][6]*aK106;",
        "  g6=T[j][1]*aK61+T[j][2]*aK62+T[j][3]*aK63+T[j][4]*aK64+T[j][5]*aK65+T[j][6]*aK66;",
        "  g2=T[j][1]*aK21+T[j][2]*aK22+T[j][3]*aK23+T[j][4]*aK24+T[j][5]*aK25+T[j][6]*aK26;",
        "  gv=g10*gen(1)+g6*gen(2)+g2*gen(3)-T[j][2]*gen(4)-T[j][4]*gen(5)-T[j][6]*gen(6);",
        "  Gamma[j]=gv;",
        "}",
    ]
    return lines


def build_source_replay(output: Path, loads: dict[str, list[Poly]]) -> Path:
    lines = [
        PRELUDE.read_text().rstrip(),
        'print("K00_V20R2_SOURCE_REPLAY_START");',
        *common_singular_declarations(loads),
        "int ok=1; int i; int j; poly z; vector vr;",
        "if ((size(T)!=66)||(size(S87)!=87)) { ok=0; }",
        "for (j=1; j<=size(T); j++) { z=0; for (i=1; i<=6; i++) { z=z+T[j][i]*I[i]; } if (z!=0) { ok=0; } }",
        "for (j=1; j<=size(S87); j++) { z=0; for (i=1; i<=7; i++) { z=z+S87[j][i]*A[i]; } if (z!=0) { ok=0; } }",
        'print("K00_V20R2_SERIALIZED_MODULE_REPLAY="+string(ok));',
        'if (ok!=1) { print("K00_V20R2_FAIL=SERIALIZED_MODULE"); quit; }',
        'print("K00_V20R2_FRESH_SYZ6_START");',
        "module Tf=syz(I); module GT=std(T); module GF=std(Tf); int moduleeq=1;",
        "for (j=1; j<=size(T); j++) { vr=reduce(T[j],GF); if (vr!=0) { moduleeq=0; } }",
        "for (j=1; j<=size(Tf); j++) { vr=reduce(Tf[j],GT); if (vr!=0) { moduleeq=0; } }",
        'print("K00_V20R2_FRESH_SYZ6_GENERATORS="+string(size(Tf)));',
        'print("K00_V20R2_SYZ6_MODULE_EQUAL="+string(moduleeq));',
        'if (moduleeq!=1) { print("K00_V20R2_FAIL=SYZ6_COMPLETENESS"); quit; }',
        "poly base=-h*r7+u1*r1+u2*r2+u3*r3+u4*r4+u5*r5+u6*r6;",
        "poly h0=subst(subst(subst(subst(subst(subst(h,d0,0),d1,0),d2,0),d3,0),d4,0),d5,0);",
        'print("K00_V20R2_BASE_RELATION="+string(base==0));',
        'print("K00_V20R2_H0="+string(h0));',
        'if ((base!=0)||(h0!=20)) { print("K00_V20R2_FAIL=BASE_RELATION"); quit; }',
    ]
    for label in ("K10", "K6", "K2"):
        lines.append(f"poly D{label}=h*a{label}7;")
        for index in range(1, 7):
            lines.append(f"D{label}=D{label}-u{index}*a{label}{index};")
    lines.extend(singular_gamma_lines())
    lines.extend([
        "int crossok=1; int wrongdetected=0; poly kv10; poly kv6; poly kv2; poly gs10; poly gs6; poly gs2; poly ss1; poly ss2; poly ss3; poly ss4; poly ss5; poly ss6;",
        "for (j=1; j<=size(S87); j++)",
        "{",
        "  kv10=S87[j][1]*aK101+S87[j][2]*aK102+S87[j][3]*aK103+S87[j][4]*aK104+S87[j][5]*aK105+S87[j][6]*aK106+S87[j][7]*aK107;",
        "  kv6=S87[j][1]*aK61+S87[j][2]*aK62+S87[j][3]*aK63+S87[j][4]*aK64+S87[j][5]*aK65+S87[j][6]*aK66+S87[j][7]*aK67;",
        "  kv2=S87[j][1]*aK21+S87[j][2]*aK22+S87[j][3]*aK23+S87[j][4]*aK24+S87[j][5]*aK25+S87[j][6]*aK26+S87[j][7]*aK27;",
        "  ss1=h*S87[j][1]+S87[j][7]*u1; ss2=h*S87[j][2]+S87[j][7]*u2; ss3=h*S87[j][3]+S87[j][7]*u3;",
        "  ss4=h*S87[j][4]+S87[j][7]*u4; ss5=h*S87[j][5]+S87[j][7]*u5; ss6=h*S87[j][6]+S87[j][7]*u6;",
        "  gs10=ss1*aK101+ss2*aK102+ss3*aK103+ss4*aK104+ss5*aK105+ss6*aK106;",
        "  gs6=ss1*aK61+ss2*aK62+ss3*aK63+ss4*aK64+ss5*aK65+ss6*aK66;",
        "  gs2=ss1*aK21+ss2*aK22+ss3*aK23+ss4*aK24+ss5*aK25+ss6*aK26;",
        "  if (h*kv10-S87[j][7]*DK10-gs10!=0) { crossok=0; }",
        "  if (h*kv6-S87[j][7]*DK6-gs6!=0) { crossok=0; }",
        "  if (h*kv2-S87[j][7]*DK2-gs2!=0) { crossok=0; }",
        "  if (h*(-S87[j][2])-S87[j][7]*u2-(-ss2)!=0) { crossok=0; }",
        "  if (h*(-S87[j][4])-S87[j][7]*u4-(-ss4)!=0) { crossok=0; }",
        "  if (h*(-S87[j][6])-S87[j][7]*u6-(-ss6)!=0) { crossok=0; }",
        "  if (h*(-S87[j][7]/4)-S87[j][7]*(-h/4)!=0) { crossok=0; }",
        "  if (h*kv10-S87[j][7]*DK10-(h*S87[j][1]-S87[j][7]*u1)*aK101-(h*S87[j][2]-S87[j][7]*u2)*aK102-(h*S87[j][3]-S87[j][7]*u3)*aK103-(h*S87[j][4]-S87[j][7]*u4)*aK104-(h*S87[j][5]-S87[j][7]*u5)*aK105-(h*S87[j][6]-S87[j][7]*u6)*aK106!=0) { wrongdetected=1; }",
        "}",
        'print("K00_V20R2_CROSS_RELATIONS="+string(crossok));',
        'print("K00_V20R2_SIGN_MUTATION_DETECTED="+string(wrongdetected));',
        'if ((crossok!=1)||(wrongdetected!=1)) { print("K00_V20R2_FAIL=CROSS_RELATION"); quit; }',
        'write("FRESH_SYZ6_MODULE.txt",Tf);',
        'write("GAMMA_MODULE.txt",Gamma);',
        'write("K_VECTOR.txt",DK10*gen(1)+DK6*gen(2)+DK2*gen(3)+u2*gen(4)+u4*gen(5)+u6*gen(6)-(h/4)*gen(7));',
        'print("K00_V20R2_SOURCE_REPLAY=PASS");',
        "quit;",
    ])
    script = output / "source_replay_v20r2.sing"
    script.write_text("\n".join(lines) + "\n")
    return script


def build_contract_replay(output: Path, loads: dict[str, list[Poly]]) -> Path:
    prelude = PRELUDE.read_text().rstrip()
    old = "ring R=0,(d0,d1,d2,d3,d4,d5),dp;"
    new = "ring R=0,(d0,d1,d2,d3,d4,d5,p10,p6,p2,pmu2,pmu4,pmu6,pJ),dp;"
    if prelude.count(old) != 1:
        fail("unexpected prelude ring declaration")
    prelude = prelude.replace(old, new, 1)
    lines = [
        prelude,
        'print("K00_V20R2_CONTRACT_REPLAY_START");',
        *common_singular_declarations(loads),
        "int i; int j; poly z;",
    ]
    for label in ("K10", "K6", "K2"):
        lines.append(f"poly D{label}=h*a{label}7;")
        for index in range(1, 7):
            lines.append(f"D{label}=D{label}-u{index}*a{label}{index};")
    lines.extend(singular_gamma_lines())
    lines.extend([
        "ideal Contracted; poly gp; int coupled=0; int mutation=0;",
        "for (j=1; j<=size(Gamma); j++)",
        "{",
        "  gp=p10*Gamma[j][1]+p6*Gamma[j][2]+p2*Gamma[j][3]+pmu2*Gamma[j][4]+pmu4*Gamma[j][5]+pmu6*Gamma[j][6]+pJ*Gamma[j][7];",
        "  Contracted[j]=gp;",
        "  if ((Gamma[j][1]!=0)&&(Gamma[j][2]!=0)) { coupled=1; }",
        "  if (gp-(p10*Gamma[j][1]+p2*Gamma[j][2]+p6*Gamma[j][3]+pmu2*Gamma[j][4]+pmu4*Gamma[j][5]+pmu6*Gamma[j][6]+pJ*Gamma[j][7])!=0) { mutation=1; }",
        "}",
        "poly Dp=p10*DK10+p6*DK6+p2*DK2+pmu2*u2+pmu4*u4+pmu6*u6-pJ*h/4;",
        "poly Dpwrong=p10*DK10+p2*DK6+p6*DK2+pmu2*u2+pmu4*u4+pmu6*u6-pJ*h/4;",
        "if (Dp-Dpwrong!=0) { mutation=1; }",
        'print("K00_V20R2_CONTRACTED_GENERATORS="+string(size(Contracted)));',
        'print("K00_V20R2_COUPLED_GENERATOR="+string(coupled));',
        'print("K00_V20R2_CONTRACTION_ORDER_MUTATION_DETECTED="+string(mutation));',
        'if ((size(Contracted)!=66)||(coupled!=1)||(mutation!=1)) { print("K00_V20R2_FAIL=CONTRACTION"); quit; }',
        'write("CONTRACTED_GENERATORS.txt",Contracted);',
        'write("CONTRACTED_TARGET.txt",Dp);',
        'print("K00_V20R2_CONTRACT_REPLAY=PASS");',
        "quit;",
    ])
    script = output / "contract_replay_v20r2.sing"
    script.write_text("\n".join(lines) + "\n")
    return script


def run_singular(script: Path, output: Path, stem: str, required: list[str]) -> dict[str, object]:
    executable = shutil.which("Singular")
    if executable is None:
        fail("Singular missing on registered AWS host")
    completed = subprocess.run([executable, "-q", str(script)], cwd=output, text=True,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=3600)
    stdout = output / f"{stem}.stdout"
    stderr = output / f"{stem}.stderr"
    stdout.write_text(completed.stdout)
    stderr.write_text(completed.stderr)
    if completed.returncode != 0 or any(marker not in completed.stdout for marker in required):
        fail(("Singular replay failed", stem, completed.returncode, completed.stdout[-2000:], completed.stderr[-2000:]))
    diagnostics = ("?", "error", "halt", "segment", "out of memory")
    lowered = completed.stderr.lower()
    if any(word in lowered for word in diagnostics):
        fail(("Singular diagnostic", stem, completed.stderr[-2000:]))
    return {"script_sha256": digest(script), "stdout_sha256": digest(stdout),
            "stderr_sha256": digest(stderr)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    tag = require_aws()
    for path, expected in EXPECTED.items():
        actual = digest(path)
        if actual != expected:
            fail(("frozen source mismatch", str(path), actual, expected))
    tails = json.loads(TAILS.read_text())
    if sorted(tails) != [str(index) for index in range(1, 8)]:
        fail(("tail key mismatch", sorted(tails)))
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != EXPECTED_CANONICAL_TAILS:
        fail("canonical tail semantic digest mismatch")
    rows, loads = reconstruct_tails(tails)
    if rows != parse_prelude_rows():
        fail("independent tail rows disagree with exact normalized prelude")
    for label in ("K10", "K6", "K2"):
        saved = parse_ideal(V21 / f"input/load_{label}.txt")
        if loads[label] != saved:
            fail(("independent load rows disagree with V21 serialization", label))
    h = parse_poly(H.read_text())
    multipliers = [parse_poly(path.read_text()) for path in U]
    if h.get(ZERO_KEY) != 20:
        fail(("unit witness constant", h.get(ZERO_KEY)))
    base = poly_mul(h, rows[6])
    for index in range(6):
        base = poly_add(base, poly_mul(multipliers[index], rows[index]), Fraction(-1))
    if base:
        fail("exact local relation failed in independent polynomial parser")
    targets: dict[str, Poly] = {}
    for label in ("K10", "K6", "K2"):
        target = poly_mul(h, loads[label][6])
        for index in range(6):
            target = poly_add(target, poly_mul(multipliers[index], loads[label][index]), Fraction(-1))
        targets[label] = target
        if target != parse_poly((V21 / f"input/target_{label}.txt").read_text()):
            fail(("independent contracted target mismatch", label))

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    columns = source_columns()
    column_path = output / "SOURCE_COLUMNS.json"
    column_path.write_text(json.dumps(columns, sort_keys=True, indent=2) + "\n")
    dag = Dag()
    source = build_source_series(dag, columns, restrict_boundary=True)
    phi = tail_dag_rows(dag, tails, source)
    h_series = poly_dag_series(dag, h, source)
    u_series = [poly_dag_series(dag, poly, source) for poly in multipliers]
    residual_left = dag.series_mul(h_series, phi[6])
    for index in range(6):
        residual_left = dag.series_sub(residual_left, dag.series_mul(u_series[index], phi[index]))
    residual_right = dag.series_zero()
    for label, name, shift in (("K10", "k10", 2), ("K6", "k6", 6), ("K2", "k2", 10)):
        piece = dag.series_mul(dag.shift(source[name], shift), poly_dag_series(dag, targets[label], source))
        residual_right = dag.series_add(residual_right, piece)
    for index, name, shift in ((1, "mu2", 14), (3, "mu4", 16), (5, "mu6", 18)):
        residual_right = dag.series_add(residual_right,
                                        dag.series_mul(u_series[index], dag.shift(source[name], shift)))
    residual_right = dag.series_sub(residual_right,
                                    dag.scale(dag.series_mul(h_series, dag.shift(source["Jdet"], 19)), Fraction(1, 4)))
    roots = [{"row": ell, "Lambda_grade": grade, "node": phi[ell - 1][grade]}
             for ell in range(1, 8) for grade in range(TRUNCATION)]
    circuit = {
        "format": "K00_V20R2_EXACT_RATIONAL_ARITHMETIC_DAG_V1",
        "truncation": "Q[Lambda]/(Lambda^20)",
        "normalized_coordinate_map": {
            "C0": "(1+d0)/256", "C1": "d1", "C2": "(1+d2)/16",
            "C3": "d3", "C4": "(3+d4)/8", "C5": "d5", "C6": "1",
        },
        "boundary_restriction_order": "SUBSTITUTE_FIVE_ZERO_CONSTANTS_BEFORE_ANY_SOLVE_OR_SATURATION",
        "source_column_sha256": digest(column_path),
        "nodes": dag.nodes,
        "roots": roots,
        "residual_lhs_roots": residual_left,
        "residual_rhs_roots": residual_right,
        "target_symbol": "Jdet",
        "forbidden_aliases": ["J1", "J2"],
    }
    circuit_path = output / "LITERAL_140_EQUATION_DAG.json"
    circuit_path.write_text(json.dumps(circuit, separators=(",", ":")) + "\n")

    fixture_records: list[dict[str, object]] = []
    mutation_flags = {"target_sign": False, "k6_weight": False,
                      "restriction_before_saturation": False,
                      "modular_representative_normalization": False}
    fixture_specs = [("Q", None, 1), ("Q", None, 2), ("F65521", 65521, 3)]
    for field, modulus, fixture in fixture_specs:
        convert: Callable[[Fraction], object]
        if modulus:
            convert = lambda value, p=modulus: (value.numerator * pow(value.denominator, -1, p)) % p
        else:
            convert = lambda value: value
        assignment = make_assignment(columns, fixture, modulus)
        values = evaluate_dag(dag, assignment, convert, modulus)
        direct, direct_source = direct_tail_rows(tails, columns, assignment, convert, modulus)
        for root in roots:
            if values[int(root["node"])] != direct[int(root["row"]) - 1][int(root["Lambda_grade"])]:
                fail(("literal DAG/direct fixture mismatch", field, fixture, root))
        if not residual_fixture(direct, direct_source, h, multipliers, targets, convert, modulus):
            fail(("contracted residual fixture mismatch", field, fixture))
        wrong_target, _ = direct_tail_rows(tails, columns, assignment, convert, modulus,
                                           target_sign=1)
        wrong_weight, _ = direct_tail_rows(tails, columns, assignment, convert, modulus,
                                           k6_shift=5)
        unrestricted, _ = direct_tail_rows(tails, columns, assignment, convert, modulus,
                                            restrict_boundary=False)
        mutation_flags["target_sign"] |= wrong_target != direct
        mutation_flags["k6_weight"] |= wrong_weight != direct
        mutation_flags["restriction_before_saturation"] |= unrestricted != direct
        if modulus:
            raw_values = evaluate_dag(dag, assignment, convert, None)
            raw_roots = [raw_values[int(root["node"])] for root in roots]
            reduced_roots = [values[int(root["node"])] for root in roots]
            if any((raw % modulus) != reduced for raw, reduced in zip(raw_roots, reduced_roots)):
                fail("nodewise and final modular reduction disagree")
            mutation_flags["modular_representative_normalization"] |= any(
                raw != reduced for raw, reduced in zip(raw_roots, reduced_roots))
        fixture_records.append({
            "field": field,
            "fixture": fixture,
            "all_140_roots_match": True,
            "contracted_residual_matches": True,
            "assignment_sha256": sha256(json.dumps({key: str(value) for key, value in sorted(assignment.items())},
                                                     separators=(",", ":")).encode()).hexdigest(),
        })
    if not all(mutation_flags.values()):
        fail(("mandatory source mutation survived", mutation_flags))
    fixture_audit = {"fixtures": fixture_records, "mutations_detected": mutation_flags}
    fixture_path = output / "FIXTURE_AUDIT.json"
    fixture_path.write_text(json.dumps(fixture_audit, sort_keys=True, indent=2) + "\n")

    source_script = build_source_replay(output, loads)
    source_replay = run_singular(source_script, output, "source_replay", [
        "K00_V20R2_SERIALIZED_MODULE_REPLAY=1",
        "K00_V20R2_SYZ6_MODULE_EQUAL=1",
        "K00_V20R2_BASE_RELATION=1",
        "K00_V20R2_H0=20",
        "K00_V20R2_CROSS_RELATIONS=1",
        "K00_V20R2_SIGN_MUTATION_DETECTED=1",
        "K00_V20R2_SOURCE_REPLAY=PASS",
    ])
    contract_script = build_contract_replay(output, loads)
    contract_replay = run_singular(contract_script, output, "contract_replay", [
        "K00_V20R2_CONTRACTED_GENERATORS=66",
        "K00_V20R2_COUPLED_GENERATOR=1",
        "K00_V20R2_CONTRACTION_ORDER_MUTATION_DETECTED=1",
        "K00_V20R2_CONTRACT_REPLAY=PASS",
    ])
    if digest(output / "FRESH_SYZ6_MODULE.txt") != EXPECTED[S66]:
        fail(("fresh syzygy bytes drift", digest(output / "FRESH_SYZ6_MODULE.txt")))
    artifacts = {}
    for path in sorted(output.iterdir()):
        if path.is_file() and path.name != "RESULT.json":
            artifacts[path.name] = {"sha256": digest(path), "bytes": path.stat().st_size}
    result = {
        "status": "PASS_EXACT_CONTRACTED_SOURCE_COMPILER_READY_FOR_STRATIFIED_SOLVE",
        "registered_aws_lane": tag,
        "field": "Q_WITH_F65521_FIXTURE_CONTROL",
        "tails": 569,
        "literal_equations": 140,
        "source_columns_before_boundary": 169,
        "free_source_columns": 164,
        "boundary_zero_columns": 5,
        "unit_open_columns": ["k10_0", "Jdet_0"],
        "jacobian_parameter": "Jdet",
        "collision_ideals_not_parameters": ["J1", "J2"],
        "six_row_syzygy_generators": 66,
        "seven_row_control_generators": 87,
        "dag_nodes": len(dag.nodes),
        "source_replay": source_replay,
        "contract_replay": contract_replay,
        "fixture_audit_sha256": digest(fixture_path),
        "literal_dag_sha256": digest(circuit_path),
        "source_columns_sha256": digest(column_path),
        "input_sha256": {str(path.relative_to(ROOT)): digest(path) for path in EXPECTED},
        "artifacts": artifacts,
        "dependency": "V21R1_LOCAL_NONMEMBERSHIP_PROVISIONAL_PENDING_OPUS5_REVIEW_NOT_USED_FOR_SOURCE_TYPING",
        "scope": "EXACT_CONTRACTED_SOURCE_AND_140_EQUATION_COMPILER_ONLY_NO_STRATUM_COVER_OR_JET_VERDICT",
        "firewall": "NO_ARC_EXCLUSION_NO_CLOSURE_INCIDENCE_NO_ORDER2_NO_MAX12_NO_JC2",
    }
    result_path = output / "RESULT.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("K00_V20R2_ENDPOINT=PASS_EXACT_CONTRACTED_SOURCE_COMPILER_READY_FOR_STRATIFIED_SOLVE")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
