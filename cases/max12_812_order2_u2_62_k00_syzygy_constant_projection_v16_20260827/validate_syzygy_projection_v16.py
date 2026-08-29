#!/usr/bin/env python3
"""Fail-closed exact validator for V16 constant syzygy projection."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def rank(matrix: list[list[Fraction]]) -> int:
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
    text = args.main_stdout.read_text()
    lines = [line.strip() for line in text.splitlines()]
    if "?" in text or any("K00_SYZPROJ_FAIL=" in line for line in lines):
        raise RuntimeError("main Singular diagnostic/failure")
    for value in (
        "K00_SYZPROJ_GENERATORS=87",
        "K00_SYZPROJ_ALL_SYZ_REPLAY=1",
        "K00_SYZPROJ_COORD2_ALL_ZERO=1",
        "K00_SYZPROJ_COORD4_ALL_ZERO=1",
        "K00_SYZPROJ_BASE_REPLAY=1",
        "K00_SYZPROJ_FREEDOM_REPLAY=1",
        "K00_SYZPROJ_BASE7_UNIT=1",
        "K00_SYZPROJ_FREEDOM7_ZERO=1",
        "K00_SYZPROJ_FREEDOM6_UNIT=1",
        "K00_SYZPROJ_ENDPOINT=PASS_SERIALIZED_CONSTANT_PROJECTION",
    ):
        marker(lines, value)
    paths = [[args.artifacts / f"SYZ_CONSTANT_{i}_{j}.txt" for j in range(1, 88)] for i in range(1, 8)]
    constants = [[parse_fraction(path) for path in row] for row in paths]
    evaluation_rank = rank(constants)
    projection_rank_67 = rank([constants[5], constants[6]])
    if evaluation_rank != 3:
        raise RuntimeError(("unexpected evaluation rank", evaluation_rank))
    if any(constants[1]) or any(constants[3]):
        raise RuntimeError("coordinates 2/4 not identically zero")
    if projection_rank_67 != 2 or not any(constants[6]):
        raise RuntimeError(("coordinate (6,7) freedom failed", projection_rank_67))
    base_paths = [args.artifacts / f"BASE_SYZYGY_{i}.txt" for i in range(1, 8)]
    freedom_paths = [args.artifacts / f"FREEDOM_SYZYGY_{i}.txt" for i in range(1, 8)]
    for path in [*base_paths, *freedom_paths]:
        if not path.is_file() or not path.read_text().strip():
            raise RuntimeError(("missing/empty witness component", str(path)))
    base7_constant = parse_fraction(args.artifacts / "BASE7_CONSTANT.txt")
    freedom7_constant = parse_fraction(args.artifacts / "FREEDOM7_CONSTANT.txt")
    freedom6_constant = parse_fraction(args.artifacts / "FREEDOM6_CONSTANT.txt")
    if base7_constant == 0:
        raise RuntimeError("base seventh coordinate is not a unit")
    if freedom7_constant != 0 or freedom6_constant == 0:
        raise RuntimeError("freedom constant pattern failed")
    replay_text = args.replay_stdout.read_text()
    replay_lines = [line.strip() for line in replay_text.splitlines()]
    if "?" in replay_text or any("K00_SYZPROJ_SERIALIZED_FAIL=" in line for line in replay_lines):
        raise RuntimeError("fresh replay diagnostic/failure")
    for value in (
        "K00_SYZPROJ_SERIALIZED_REPLAY=1",
        "K00_SYZPROJ_SERIALIZED_CONSTANTS=1",
        "K00_SYZPROJ_SERIALIZED_ENDPOINT=PASS_FRESH_PROCESS",
    ):
        marker(replay_lines, value)
    residuals = [args.replay_artifacts / "BASE_RESIDUAL.txt", args.replay_artifacts / "FREEDOM_RESIDUAL.txt"]
    if any(not path.is_file() or path.read_text().strip() != "0" for path in residuals):
        raise RuntimeError("fresh replay residual is not literal zero")
    compiler = json.loads(args.compiler_result.read_text())
    builder = json.loads(args.builder_result.read_text())
    if compiler.get("field") not in ("Q", "65521") or builder.get("field") != compiler.get("field"):
        raise RuntimeError("compiler/builder field mismatch")
    canonical = [[str(value) for value in row] for row in constants]
    matrix_hash = sha256(json.dumps(canonical, separators=(",", ":")).encode()).hexdigest()
    result = {
        **compiler,
        "status": "PASS-K00-SYZPROJ-V16-ENDPOINT",
        "syzygy_generators": 87,
        "evaluation_rank": evaluation_rank,
        "coordinate2_forced_zero": True,
        "coordinate4_forced_zero": True,
        "projection_rank_67": projection_rank_67,
        "coordinate6_arbitrary_at_normalized_coordinate7": True,
        "base7_constant": str(base7_constant),
        "freedom7_constant": str(freedom7_constant),
        "freedom6_constant": str(freedom6_constant),
        "constant_matrix_canonical_sha256": matrix_hash,
        "base_component_sha256": {str(i): digest(path) for i, path in enumerate(base_paths, 1)},
        "freedom_component_sha256": {str(i): digest(path) for i, path in enumerate(freedom_paths, 1)},
        "builder_result_sha256": digest(args.builder_result),
        "fresh_replay_stdout_sha256": digest(args.replay_stdout),
        "fresh_base_residual_sha256": digest(residuals[0]),
        "fresh_freedom_residual_sha256": digest(residuals[1]),
        "interpretation": "M2_AND_M4_CONSTANTS_FORCED_ZERO_M6_CONSTANT_FREE",
    }
    args.result.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
