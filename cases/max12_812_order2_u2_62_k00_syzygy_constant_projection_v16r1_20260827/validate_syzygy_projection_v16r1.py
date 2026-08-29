#!/usr/bin/env python3
"""Fail-closed exact/mod-p validator for V16R1 constant projection."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def rank_q(matrix: list[list[Fraction]]) -> int:
    rows = [row[:] for row in matrix]
    if not rows:
        return 0
    m, n = len(rows), len(rows[0])
    pivot_row = 0
    for col in range(n):
        pivot = next((i for i in range(pivot_row, m) if rows[i][col]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        value = rows[pivot_row][col]
        rows[pivot_row] = [x / value for x in rows[pivot_row]]
        for i in range(m):
            if i != pivot_row and rows[i][col]:
                value = rows[i][col]
                rows[i] = [a - value * b for a, b in zip(rows[i], rows[pivot_row])]
        pivot_row += 1
        if pivot_row == m:
            break
    return pivot_row


def rank_mod(matrix: list[list[Fraction]], prime: int) -> int:
    rows = [
        [(value.numerator % prime) * pow(value.denominator % prime, -1, prime) % prime for value in row]
        for row in matrix
    ]
    if not rows:
        return 0
    m, n = len(rows), len(rows[0])
    pivot_row = 0
    for col in range(n):
        pivot = next((i for i in range(pivot_row, m) if rows[i][col] % prime), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        inverse = pow(rows[pivot_row][col] % prime, -1, prime)
        rows[pivot_row] = [(x * inverse) % prime for x in rows[pivot_row]]
        for i in range(m):
            if i != pivot_row and rows[i][col] % prime:
                value = rows[i][col] % prime
                rows[i] = [(a - value * b) % prime for a, b in zip(rows[i], rows[pivot_row])]
        pivot_row += 1
        if pivot_row == m:
            break
    return pivot_row


def marker(lines: list[str], value: str) -> None:
    if sum(line == value for line in lines) != 1:
        raise RuntimeError(("missing/nonunique marker", value))


def parse_fraction(path: Path) -> Fraction:
    text = path.read_text().strip()
    if not text or any(ch not in "-0123456789/" for ch in text):
        raise RuntimeError(("malformed constant", str(path), text))
    return Fraction(text)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("main_stdout", type=Path)
    parser.add_argument("artifacts", type=Path)
    parser.add_argument("compiler_result", type=Path)
    parser.add_argument("replay_stdout", type=Path)
    parser.add_argument("replay_artifacts", type=Path)
    parser.add_argument("builder_result", type=Path)
    parser.add_argument("result", type=Path)
    args = parser.parse_args()
    compiler = json.loads(args.compiler_result.read_text())
    field = compiler.get("field")
    if field not in ("Q", "65521"):
        raise RuntimeError(("bad compiler field", field))
    text = args.main_stdout.read_text()
    lines = [line.strip() for line in text.splitlines()]
    if "?" in text or any("K00_SYZPROJ_R1_FAIL=" in line for line in lines):
        raise RuntimeError("main Singular diagnostic/failure")
    for value in (
        "K00_SYZPROJ_R1_GENERATORS=87",
        "K00_SYZPROJ_R1_ALL_SYZ_REPLAY=1",
        "K00_SYZPROJ_R1_BASE_REPLAY=1",
        "K00_SYZPROJ_R1_ENDPOINT=PASS_BOTH_OUTCOME_PRODUCER",
    ):
        marker(lines, value)
    branch_path = args.artifacts / "BRANCH.txt"
    branch = branch_path.read_text().strip()
    if branch not in ("M6_FORCED", "M6_FREEDOM"):
        raise RuntimeError(("invalid branch", branch))
    marker(lines, f"K00_SYZPROJ_R1_BRANCH={branch}")
    paths = [[args.artifacts / f"SYZ_CONSTANT_{i}_{j}.txt" for j in range(1, 88)] for i in range(1, 8)]
    if any(not path.is_file() for row in paths for path in row):
        raise RuntimeError("missing one or more of 609 constant entries")
    constants = [[parse_fraction(path) for path in row] for row in paths]
    zero_flags = {coordinate: not any(constants[coordinate - 1]) for coordinate in (2, 4, 6)}
    for coordinate, flag in zero_flags.items():
        marker(lines, f"K00_SYZPROJ_R1_COORD{coordinate}_ALL_ZERO={int(flag)}")
    if field == "Q":
        evaluation_rank = rank_q(constants)
        projection_rank_67 = rank_q([constants[5], constants[6]])
    else:
        evaluation_rank = rank_mod(constants, 65521)
        projection_rank_67 = rank_mod([constants[5], constants[6]], 65521)
    if not any(constants[6]):
        raise RuntimeError("no syzygy has a unit seventh component")
    if branch == "M6_FORCED":
        if not zero_flags[6] or projection_rank_67 != 1:
            raise RuntimeError(("forced branch inconsistent", zero_flags[6], projection_rank_67))
    else:
        if zero_flags[6] or projection_rank_67 != 2:
            raise RuntimeError(("freedom branch inconsistent", zero_flags[6], projection_rank_67))
        for value in (
            "K00_SYZPROJ_R1_FREEDOM_REPLAY=1",
            "K00_SYZPROJ_R1_FREEDOM7_CONSTANT=0",
        ):
            marker(lines, value)
    base_paths = [args.artifacts / f"BASE_SYZYGY_{i}.txt" for i in range(1, 8)]
    if any(not path.is_file() or not path.read_text().strip() for path in base_paths):
        raise RuntimeError("missing/empty base witness component")
    base7_constant = parse_fraction(args.artifacts / "BASE7_CONSTANT.txt")
    if base7_constant == 0:
        raise RuntimeError("base seventh coordinate is not a unit")
    freedom_paths = [args.artifacts / f"FREEDOM_SYZYGY_{i}.txt" for i in range(1, 8)]
    freedom6_constant = None
    if branch == "M6_FREEDOM":
        if any(not path.is_file() or not path.read_text().strip() for path in freedom_paths):
            raise RuntimeError("missing/empty freedom witness component")
        if parse_fraction(args.artifacts / "FREEDOM7_CONSTANT.txt") != 0:
            raise RuntimeError("freedom seventh constant is not zero")
        freedom6_constant = parse_fraction(args.artifacts / "FREEDOM6_CONSTANT.txt")
        if freedom6_constant == 0:
            raise RuntimeError("freedom sixth constant is not a unit")
    elif any(path.exists() for path in freedom_paths):
        raise RuntimeError("forced branch unexpectedly contains freedom witness")
    replay_text = args.replay_stdout.read_text()
    replay_lines = [line.strip() for line in replay_text.splitlines()]
    if "?" in replay_text or any("K00_SYZPROJ_R1_SERIALIZED_FAIL=" in line for line in replay_lines):
        raise RuntimeError("fresh replay diagnostic/failure")
    for value in (
        "K00_SYZPROJ_R1_SERIALIZED_BASE_REPLAY=1",
        f"K00_SYZPROJ_R1_SERIALIZED_BRANCH={branch}",
        "K00_SYZPROJ_R1_SERIALIZED_ENDPOINT=PASS_FRESH_PROCESS",
    ):
        marker(replay_lines, value)
    if branch == "M6_FREEDOM":
        marker(replay_lines, "K00_SYZPROJ_R1_SERIALIZED_FREEDOM_REPLAY=1")
    residuals = [args.replay_artifacts / "BASE_RESIDUAL.txt"]
    if branch == "M6_FREEDOM":
        residuals.append(args.replay_artifacts / "FREEDOM_RESIDUAL.txt")
    if any(not path.is_file() or path.read_text().strip() != "0" for path in residuals):
        raise RuntimeError("fresh replay residual is not literal zero")
    builder = json.loads(args.builder_result.read_text())
    if builder.get("field") != field or builder.get("branch") != branch:
        raise RuntimeError("compiler/builder field or branch mismatch")
    canonical = [[str(value) for value in row] for row in constants]
    matrix_hash = sha256(json.dumps(canonical, separators=(",", ":")).encode()).hexdigest()
    interpretation = (
        "ALL_LOCAL_REPRESENTATION_CHANGES_HAVE_ZERO_M6_ORIGIN_CONSTANT"
        if branch == "M6_FORCED"
        else "LOCAL_REPRESENTATION_CHANGES_ALLOW_ARBITRARY_M6_ORIGIN_CONSTANT"
    )
    result = {
        **compiler,
        "status": "PASS-K00-SYZPROJ-V16R1-ENDPOINT",
        "branch": branch,
        "syzygy_generators": 87,
        "evaluation_rank": evaluation_rank,
        "coordinate2_forced_zero": zero_flags[2],
        "coordinate4_forced_zero": zero_flags[4],
        "coordinate6_forced_zero": zero_flags[6],
        "projection_rank_67": projection_rank_67,
        "base7_constant": str(base7_constant),
        "freedom6_constant": str(freedom6_constant) if freedom6_constant is not None else None,
        "constant_matrix_canonical_sha256": matrix_hash,
        "branch_sha256": digest(branch_path),
        "base_component_sha256": {str(i): digest(path) for i, path in enumerate(base_paths, 1)},
        "freedom_component_sha256": (
            {str(i): digest(path) for i, path in enumerate(freedom_paths, 1)}
            if branch == "M6_FREEDOM" else {}
        ),
        "builder_result_sha256": digest(args.builder_result),
        "fresh_replay_stdout_sha256": digest(args.replay_stdout),
        "fresh_residual_sha256": {path.name: digest(path) for path in residuals},
        "localization_completeness": (
            "A local syzygy clears by a common denominator s with s(0)!=0 to a polynomial "
            "syzygy; origin evaluation is rescaled by the nonzero scalar s(0). Hence the "
            "full polynomial syzygy evaluation span equals the local evaluation span up to units."
        ),
        "interpretation": interpretation,
        "firewall": (
            "ORDER_ZERO_UNLOADED_C6_EQ_1_LOCAL_RELATION_CONSTANTS_ONLY; "
            "NOT_FIRST_ORDER_DEFORMATION_OR_HONEST_LAMBDA19_REACHABILITY"
        ),
    }
    args.result.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()

