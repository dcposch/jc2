#!/usr/bin/env python3
"""Fail-closed validator for the K00 global-colon local decision."""

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
    parser.add_argument("stdout", type=Path)
    parser.add_argument("artifacts", type=Path)
    parser.add_argument("compiler_result", type=Path)
    parser.add_argument("result", type=Path)
    args = parser.parse_args()
    text = args.stdout.read_text()
    lines = [line.strip() for line in text.splitlines()]
    if "?" in text or any("K00_COLON_FAIL=" in line for line in lines):
        raise RuntimeError("Singular diagnostic or fail marker")
    required = [
        "K00_COLON_MODE=NORMALIZED_C6_1_GLOBAL_DP",
        "K00_COLON_SOURCE_HASHES=PASS",
        "K00_COLON_TOY_GLOBAL_NONMEMBER=1",
        "K00_COLON_TOY_LOCAL_MEMBER=1",
        "K00_COLON_TOY_LOCAL_NONMEMBER=1",
        "K00_COLON_TOY_REPLAY=1",
        "K00_COLON_SOURCE_PROPER=1",
        "K00_COLON_GLOBAL_NONMEMBER=1",
        "K00_COLON_PROPER=1",
        "K00_COLON_PROJECTION_EQUAL=1",
        "K00_COLON_SYZ_REPLAY=1",
        "K00_COLON_LIFT_REPLAY=1",
        "K00_COLON_CONSTANT_CONSISTENCY=1",
        "K00_COLON_ENDPOINT=PASS_LOCAL_DECISION",
    ]
    for marker in required:
        if sum(line == marker for line in lines) != 1:
            raise RuntimeError(("missing/nonunique required marker", marker))
    artifacts = [
        args.artifacts / "COLON_GENERATORS.txt",
        args.artifacts / "COLON_STANDARD_BASIS.txt",
        args.artifacts / "COLON_LIFTS.txt",
        args.artifacts / "SYZYGY_MODULE.txt",
        args.artifacts / "SYZYGY_PROJECTION.txt",
    ]
    for path in artifacts:
        if not path.is_file() or not path.read_text().strip():
            raise RuntimeError(("missing/empty evidence", str(path)))
    member_text = unique(lines, "K00_COLON_LOCAL_MEMBER=")
    if member_text not in ("0", "1"):
        raise RuntimeError("malformed membership marker")
    member = member_text == "1"
    extra: dict[str, object]
    if member:
        for marker in ("K00_COLON_WITNESS_CONSTANT_NONZERO=1", "K00_COLON_EVIDENCE=UNIT_COLON_WITNESS"):
            if sum(line == marker for line in lines) != 1:
                raise RuntimeError(("missing member evidence marker", marker))
        witness = args.artifacts / "LOCAL_UNIT_WITNESS.txt"
        if not witness.is_file() or not witness.read_text().strip():
            raise RuntimeError("missing unit colon witness")
        extra = {"evidence_kind": "UNIT_COLON_WITNESS", "witness_sha256": digest(witness)}
    else:
        for marker in ("K00_COLON_ALL_GENERATOR_CONSTANTS_ZERO=1", "K00_COLON_EVIDENCE=COLON_CONTAINED_IN_MAXIMAL"):
            if sum(line == marker for line in lines) != 1:
                raise RuntimeError(("missing nonmember evidence marker", marker))
        extra = {"evidence_kind": "COLON_CONTAINED_IN_MAXIMAL"}
    compiler = json.loads(args.compiler_result.read_text())
    if compiler.get("order") != "dp" or compiler.get("field") not in ("Q", "65521"):
        raise RuntimeError("compiler field/order mismatch")
    result = {
        **compiler,
        "status": "PASS-K00-COLON-LOCAL-ENDPOINT",
        "local_member": member,
        "colon_generators": int(unique(lines, "K00_COLON_GENERATORS=")),
        "syzygy_generators": int(unique(lines, "K00_COLON_SYZ_GENERATORS=")),
        "compiler_result_sha256": digest(args.compiler_result),
        "colon_generators_sha256": digest(artifacts[0]),
        "colon_standard_basis_sha256": digest(artifacts[1]),
        "colon_lifts_sha256": digest(artifacts[2]),
        "syzygy_module_sha256": digest(artifacts[3]),
        "syzygy_projection_sha256": digest(artifacts[4]),
        **extra,
    }
    args.result.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()

