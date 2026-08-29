#!/usr/bin/env python3
"""AWS-only modular rank navigation for the first post-sheet raw grade."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform
import random
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
COMPILER = HERE / "compile_receivers.py"
FREEZE = HERE / "FREEZE.sha256"
RESULT = HERE / "RESULT.md"
EXPECTED = {
    COMPILER: "2d8507bcdab953f94a19bc6f794fe8233f466c74afcbab4f21497aab4280951a",
    FREEZE: "50ca8894f273ff47f69b6b32f410b811cb22e144b4a3602da326dd0e68ecc0d0",
    RESULT: "c4123a3eb37f8341f3ac363c5d9d6a0e97009a714f1bfefe818f50be9d82067c",
}
NEWEST = ("ell3", "cs2", "rs2", "az2", "ac2", "ez3", "ec3", "k10_2")


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_compiler():
    spec = importlib.util.spec_from_file_location("p0_odd_receivers_frozen", COMPILER)
    if spec is None or spec.loader is None:
        fail("cannot import frozen receiver compiler")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def qmod(value: Fraction, prime: int) -> int:
    if value.denominator % prime == 0:
        fail(("bad prime denominator", value, prime))
    return value.numerator * pow(value.denominator, -1, prime) % prime


def ranks(matrix: list[list[int]], prime: int) -> tuple[int, list[int]]:
    work = [row[:] for row in matrix]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    pivot_cols = []
    pivot_row = 0
    for col in range(cols):
        selected = next((r for r in range(pivot_row, rows) if work[r][col] % prime), None)
        if selected is None:
            continue
        work[pivot_row], work[selected] = work[selected], work[pivot_row]
        inverse = pow(work[pivot_row][col] % prime, -1, prime)
        work[pivot_row] = [(value * inverse) % prime for value in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row:
                continue
            factor = work[row][col] % prime
            if factor:
                work[row] = [
                    (a - factor * b) % prime
                    for a, b in zip(work[row], work[pivot_row])
                ]
        pivot_cols.append(col)
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row, pivot_cols


def variable_names(nodes: list[dict[str, object]]) -> list[str]:
    return sorted({str(node["name"]) for node in nodes if node["op"] == "var"})


def degrees_in_newest(nodes: list[dict[str, object]]) -> list[int]:
    newest = set(NEWEST)
    answer = []
    for node in nodes:
        if node["op"] == "var":
            degree = int(str(node["name"]) in newest)
        elif node["op"] == "add":
            degree = max((answer[int(child)] for child in node["args"]), default=0)
        elif node["op"] == "mul":
            degree = sum(answer[int(child)] for child in node["args"])
        else:
            degree = 0
        answer.append(degree)
    return answer


def evaluate_dual(
    nodes: list[dict[str, object]],
    assignment: dict[str, int],
    prime: int,
) -> tuple[list[int], list[tuple[int, ...]]]:
    positions = {name: i for i, name in enumerate(NEWEST)}
    values: list[int] = []
    gradients: list[tuple[int, ...]] = []
    zero_gradient = (0,) * len(NEWEST)
    for node in nodes:
        op = node["op"]
        if op == "const":
            value = qmod(Fraction(int(node["n"]), int(node["d"])), prime)
            gradient = zero_gradient
        elif op == "var":
            name = str(node["name"])
            value = assignment[name] % prime
            if name in positions:
                mutable = [0] * len(NEWEST)
                mutable[positions[name]] = 1
                gradient = tuple(mutable)
            else:
                gradient = zero_gradient
        elif op == "add":
            value = 0
            mutable = [0] * len(NEWEST)
            for child in node["args"]:
                child = int(child)
                value += values[child]
                for i, entry in enumerate(gradients[child]):
                    mutable[i] += entry
            value %= prime
            gradient = tuple(entry % prime for entry in mutable)
        elif op == "mul":
            value = 1
            mutable = [0] * len(NEWEST)
            for child in node["args"]:
                child = int(child)
                child_value = values[child]
                child_gradient = gradients[child]
                mutable = [
                    (entry * child_value + value * child_gradient[i]) % prime
                    for i, entry in enumerate(mutable)
                ]
                value = value * child_value % prime
            gradient = tuple(mutable)
        else:
            fail(("unknown DAG operation", op))
        values.append(value)
        gradients.append(gradient)
    return values, gradients


def predecessor_assignment(names: list[str], prime: int, seed: int) -> dict[str, int]:
    rng = random.Random(seed)
    assignment = {name: rng.randrange(1, prime) for name in names}
    for name in NEWEST:
        assignment[name] = 0
    b = assignment["b"]
    w = assignment["w"]
    a1 = assignment["a1"]
    aa0 = assignment["aa0"]
    rs1 = assignment["rs1"]
    ell2 = assignment["ell2"]
    three_eighths = qmod(Fraction(3, 8), prime)
    assignment["ee0"] = (
        b * a1
        - aa0 * b * b * w * pow(a1, -1, prime)
        - three_eighths * w * w * b * rs1 * rs1 * pow(a1, -1, prime)
        + 2 * w * w * ell2 * b * b * b * pow(a1, -1, prime)
    ) % prime
    return assignment


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--prime", type=int, choices=(32003, 65521), required=True)
    parser.add_argument("--samples", type=int, default=8)
    args = parser.parse_args()
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if (
        platform.system() != "Linux"
        or not vendor.is_file()
        or vendor.read_text().strip() != "Amazon EC2"
        or not tag
    ):
        fail("grade-13 analyzer is restricted to registered AWS EC2")
    for path, expected in EXPECTED.items():
        if digest(path) != expected:
            fail(("frozen predecessor mismatch", str(path), digest(path), expected))

    compiler = load_compiler()
    tails = compiler.canonical_tails()
    dag = compiler.Dag()
    rows, source_rows, predecessor_f = compiler.terminal_source(dag, tails)
    grade_roots = [source_rows[(ell, 13)] for ell in range(1, 8)]
    degrees = degrees_in_newest(dag.nodes)
    grade_degrees = [degrees[root] for root in grade_roots]
    if any(degree > 1 for degree in grade_degrees):
        fail(("grade 13 is nonlinear in the registered newest corrections", grade_degrees))

    names = variable_names(dag.nodes)
    samples = []
    for index in range(args.samples):
        assignment = predecessor_assignment(names, args.prime, 130000 + 97 * index + args.prime)
        values, gradients = evaluate_dual(dag.nodes, assignment, args.prime)
        if values[predecessor_f] % args.prime:
            fail(("predecessor F assignment failed", index, values[predecessor_f]))
        matrix = [list(gradients[root]) for root in grade_roots]
        rhs = [(-values[root]) % args.prime for root in grade_roots]
        rank, pivots = ranks(matrix, args.prime)
        augmented_rank, _ = ranks([row + [entry] for row, entry in zip(matrix, rhs)], args.prime)
        samples.append(
            {
                "sample": index,
                "rank": rank,
                "augmented_rank": augmented_rank,
                "pivot_variables": [NEWEST[column] for column in pivots],
                "consistent": rank == augmented_rank,
                "row_values": [values[root] for root in grade_roots],
            }
        )

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    hashes = compiler.all_expression_shas(dag.nodes)
    result = {
        "status": "PASS-P0-ODD-GRADE13-MODULAR-RANK-NAVIGATION",
        "registered_aws_lane": tag,
        "prime": args.prime,
        "samples": samples,
        "newest_corrections": NEWEST,
        "grade13_degrees_in_newest": grade_degrees,
        "all_affine_linear": True,
        "predecessor_F_imposed": True,
        "localized_sample_open": "b*w*a1!=0",
        "raw_grade13_root_sha256": [hashes[root] for root in grade_roots],
        "scope": "MODULAR_GENERIC_RANK_NAVIGATION_ONLY_NO_EXACT_MINOR_OR_STRATUM_COVERAGE",
        "mathematical_endpoint": "NAVIGATION_NOT_PROOF",
        "order2_closed": False,
        "JC2": "NOT_CLAIMED",
    }
    result_path = output / "result.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("P0_ODD_G13_SOURCE_HASHES=PASS")
    print("P0_ODD_G13_AFFINE_LINEAR=1")
    print("P0_ODD_G13_STATUS=PASS_MODULAR_RANK_NAVIGATION")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
