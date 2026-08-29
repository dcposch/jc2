#!/usr/bin/env python3
"""Fail-closed validator for the V17 three-direction producer."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path


LOADS = ("K10", "K6", "K2")
BRANCHES = ("ZERO_TARGET", "LOCAL_ZERO", "LOCAL_NONZERO")


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def marker(lines: list[str], value: str) -> None:
    if sum(line == value for line in lines) != 1:
        raise RuntimeError(("missing/nonunique marker", value))


def unique_value(lines: list[str], prefix: str) -> str:
    matches = [line[len(prefix):] for line in lines if line.startswith(prefix)]
    if len(matches) != 1:
        raise RuntimeError(("missing/nonunique value", prefix, matches))
    return matches[0]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("stdout", type=Path)
    parser.add_argument("artifacts", type=Path)
    parser.add_argument("compiler_result", type=Path)
    parser.add_argument("result", type=Path)
    args = parser.parse_args()
    text = args.stdout.read_text()
    lines = [line.strip() for line in text.splitlines()]
    if "?" in text or any("K00_V17_FAIL=" in line for line in lines):
        raise RuntimeError("Singular diagnostic or coded failure")
    for value in (
        "K00_V17_SOURCE_HASHES=PASS",
        "K00_V17_UNLOADED_ROW_AUDIT=1",
        "K00_V17_BASE_REPLAY=1",
        "K00_V17_H_UNIT=1",
        "K00_V17_SYZ6_REPLAY=1",
        "K00_V17_SYZ87_GENERATORS=87",
        "K00_V17_SYZ87_REPLAY=1",
        "K00_V17_ENDPOINT=PASS_THREE_DIRECTION_LOCAL_COKERNEL",
    ):
        marker(lines, value)
    syz6_generators = int(unique_value(lines, "K00_V17_SYZ6_GENERATORS="))
    if syz6_generators < 1:
        raise RuntimeError("empty six-row syzygy module")
    compiler = json.loads(args.compiler_result.read_text())
    field = compiler.get("field")
    if field not in ("Q", "65521"):
        raise RuntimeError(("bad field", field))
    branches: dict[str, str] = {}
    directions: dict[str, object] = {}
    required = [args.artifacts / "SYZ6_MODULE.txt", args.artifacts / "SYZ87_MODULE.txt"]
    for load in LOADS:
        marker(lines, f"K00_V17_{load}_REPRESENTATION_INVARIANCE=1")
        branch = unique_value(lines, f"K00_V17_{load}_BRANCH=")
        if branch not in BRANCHES:
            raise RuntimeError(("bad branch", load, branch))
        target_zero = int(unique_value(lines, f"K00_V17_{load}_TARGET_ZERO="))
        global_zero = int(unique_value(lines, f"K00_V17_{load}_GLOBAL_ZERO="))
        local_zero = int(unique_value(lines, f"K00_V17_{load}_LOCAL_ZERO="))
        local_quotient_proper = int(unique_value(lines, f"K00_V17_{load}_LOCAL_QUOTIENT_PROPER="))
        image_generators = int(unique_value(lines, f"K00_V17_{load}_IMAGE_GENERATORS="))
        colon_generators = int(unique_value(lines, f"K00_V17_{load}_COLON_GENERATORS="))
        if any(value not in (0, 1) for value in (target_zero, global_zero, local_zero, local_quotient_proper)):
            raise RuntimeError(("nonboolean direction marker", load))
        if image_generators != syz6_generators or colon_generators < 1:
            raise RuntimeError(("generator count mismatch", load, image_generators, colon_generators))
        expected = "ZERO_TARGET" if target_zero else ("LOCAL_ZERO" if local_zero else "LOCAL_NONZERO")
        if branch != expected:
            raise RuntimeError(("branch/boolean mismatch", load, branch, expected))
        if global_zero and not local_zero:
            raise RuntimeError(("global membership did not imply local membership", load))
        branch_path = args.artifacts / f"BRANCH_{load}.txt"
        if branch_path.read_text().strip() != branch:
            raise RuntimeError(("branch artifact mismatch", load))
        load_files = [
            args.artifacts / f"LOAD_ROWS_{load}.txt",
            args.artifacts / f"IMAGE_{load}.txt",
            args.artifacts / f"IMAGE_GB_{load}.txt",
            args.artifacts / f"TARGET_{load}.txt",
            args.artifacts / f"QUOTIENT_GB_{load}.txt",
            args.artifacts / f"COLON_{load}.txt",
            args.artifacts / f"COLON_GB_{load}.txt",
            branch_path,
        ]
        if branch == "LOCAL_ZERO":
            load_files.extend([
                args.artifacts / f"LOCAL_WITNESS_{load}.txt",
                args.artifacts / f"LOCAL_LIFT_{load}.txt",
                args.artifacts / f"LOCAL_REPLAY_{load}.txt",
            ])
            replay = args.artifacts / f"LOCAL_REPLAY_{load}.txt"
            if replay.read_text().strip() != "0":
                raise RuntimeError(("local replay residual not zero", load))
        required.extend(load_files)
        branches[load] = branch
        directions[load] = {
            "branch": branch,
            "target_zero": bool(target_zero),
            "global_class_zero": bool(global_zero),
            "local_class_zero": bool(local_zero),
            "local_quotient_proper": bool(local_quotient_proper),
            "image_generators": image_generators,
            "colon_generators": colon_generators,
            "artifact_sha256": {path.name: digest(path) for path in load_files},
        }
    if any(not path.is_file() or not path.read_text().strip() for path in required):
        raise RuntimeError("missing/empty required artifact")
    result = {
        **compiler,
        "status": "PASS-K00-FIRSTORDER-COKERNEL-V17-ENDPOINT",
        "syz6_generators": syz6_generators,
        "syz6_module_sha256": digest(args.artifacts / "SYZ6_MODULE.txt"),
        "syz87_module_replay_sha256": digest(args.artifacts / "SYZ87_MODULE.txt"),
        "directions": directions,
        "all_representation_invariance_checks": True,
        "interpretation": "SEPARATE_FIRSTORDER_LOAD_CLASSES_ONLY",
        "firewall": (
            "NO_COUPLED_DEFORMATION_NO_LAMBDA_WEIGHTS_NO_TARGETS_NO_LAMBDA19_SOURCE_REACHABILITY"
        ),
    }
    args.result.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()

