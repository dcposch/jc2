#!/usr/bin/env python3
"""Validate complete V14R1 serialization and fresh-process replay."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def unique(lines: list[str], prefix: str) -> str:
    values = [line[len(prefix):] for line in lines if line.startswith(prefix)]
    if len(values) != 1:
        raise RuntimeError(("missing/nonunique marker", prefix, values))
    return values[0]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("main_stdout", type=Path)
    parser.add_argument("artifacts", type=Path)
    parser.add_argument("compiler_result", type=Path)
    parser.add_argument("base_result", type=Path)
    parser.add_argument("replay_stdout", type=Path)
    parser.add_argument("replay_artifacts", type=Path)
    parser.add_argument("builder_result", type=Path)
    parser.add_argument("result", type=Path)
    args = parser.parse_args()
    main_text = args.main_stdout.read_text()
    main_lines = [line.strip() for line in main_text.splitlines()]
    if "?" in main_text or any("K00_COLON_FAIL=" in line for line in main_lines):
        raise RuntimeError("main Singular diagnostic/failure")
    required = [
        "K00_COLON_R1_LIFT_ROWS=6",
        "K00_COLON_R1_LIFT_COLUMNS=6",
        "K00_COLON_R1_EXPLICIT_IDENTITY_REPLAY=1",
        "K00_COLON_R1_EXPLICIT_UNIT=1",
        "K00_COLON_ENDPOINT=PASS_LOCAL_DECISION",
    ]
    for marker in required:
        if sum(line == marker for line in main_lines) != 1:
            raise RuntimeError(("missing/nonunique R1 marker", marker))
    witness_index = int(unique(main_lines, "K00_COLON_R1_WITNESS_INDEX="))
    if not 1 <= witness_index <= 6:
        raise RuntimeError("invalid witness index")
    lift_paths = [args.artifacts / f"COLON_LIFT_{i}_{j}.txt" for i in range(1, 7) for j in range(1, 7)]
    unit_paths = [args.artifacts / f"UNIT_MULTIPLIER_{i}.txt" for i in range(1, 7)]
    witness = args.artifacts / "LOCAL_UNIT_WITNESS_R1.txt"
    for path in [*lift_paths, *unit_paths, witness]:
        if not path.is_file() or not path.read_text().strip():
            raise RuntimeError(("missing/empty serialized polynomial", str(path)))
    for i, unit_path in enumerate(unit_paths, 1):
        matrix_path = args.artifacts / f"COLON_LIFT_{i}_{witness_index}.txt"
        if unit_path.read_bytes() != matrix_path.read_bytes():
            raise RuntimeError(("unit multiplier differs from selected matrix column", i))
    replay_text = args.replay_stdout.read_text()
    replay_lines = [line.strip() for line in replay_text.splitlines()]
    if "?" in replay_text or any("K00_SERIALIZED_FAIL=" in line for line in replay_lines):
        raise RuntimeError("fresh replay diagnostic/failure")
    for marker in (
        "K00_SERIALIZED_IDENTITY_REPLAY=1",
        "K00_SERIALIZED_UNIT_CONSTANT_NONZERO=1",
        "K00_SERIALIZED_ENDPOINT=PASS_FRESH_PROCESS",
    ):
        if sum(line == marker for line in replay_lines) != 1:
            raise RuntimeError(("missing/nonunique fresh replay marker", marker))
    residual = args.replay_artifacts / "SERIALIZED_IDENTITY_RESIDUAL.txt"
    replay_witness = args.replay_artifacts / "SERIALIZED_UNIT_WITNESS.txt"
    if not residual.is_file() or residual.read_text().strip() != "0":
        raise RuntimeError("fresh serialized residual is not literal zero")
    if replay_witness.read_bytes() != witness.read_bytes():
        raise RuntimeError("fresh replay witness byte mismatch")
    compiler = json.loads(args.compiler_result.read_text())
    base = json.loads(args.base_result.read_text())
    builder = json.loads(args.builder_result.read_text())
    if base.get("local_member") is not True or base.get("field") != compiler.get("field"):
        raise RuntimeError("base V14 validation mismatch")
    if builder.get("status") != "PASS-K00-SERIALIZED-REPLAY-BUILDER" or builder.get("field") != compiler.get("field"):
        raise RuntimeError("builder result mismatch")
    result = {
        **compiler,
        "status": "PASS-K00-COLON-LOCAL-V14R1-ENDPOINT",
        "local_member": True,
        "witness_index": witness_index,
        "witness_sha256": digest(witness),
        "lift_entry_sha256": {f"{i},{j}": digest(args.artifacts / f"COLON_LIFT_{i}_{j}.txt") for i in range(1, 7) for j in range(1, 7)},
        "unit_multiplier_sha256": {str(i): digest(path) for i, path in enumerate(unit_paths, 1)},
        "base_result_sha256": digest(args.base_result),
        "builder_result_sha256": digest(args.builder_result),
        "fresh_replay_stdout_sha256": digest(args.replay_stdout),
        "fresh_replay_residual_sha256": digest(residual),
        "fresh_replay_witness_sha256": digest(replay_witness),
        "evidence_kind": "SERIALIZED_UNIT_COLON_IDENTITY_FRESHLY_REPLAYED",
    }
    args.result.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()

