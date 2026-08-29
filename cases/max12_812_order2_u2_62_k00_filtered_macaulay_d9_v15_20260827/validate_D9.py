#!/usr/bin/env python3
"""Fail-closed D9 V15 validator using the frozen V9 exact replay parser."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V9_VALIDATOR = ROOT / "cases/max12_812_order2_u2_62_k00_filtered_macaulay_v9_20260827/validate_filtered_macaulay.py"
EXPECTED_V9_VALIDATOR = "c7169efdc584731e98db836e09c2823d196e857017b3aeb4946f088e0502a707"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_v9_validator():
    if digest(V9_VALIDATOR) != EXPECTED_V9_VALIDATOR:
        raise RuntimeError("frozen V9 validator mismatch")
    spec = importlib.util.spec_from_file_location("k00_v9_validator_for_d9", V9_VALIDATOR)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load V9 validator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("audit", type=Path)
    parser.add_argument("matrix", type=Path)
    parser.add_argument("solution", type=Path)
    parser.add_argument("--field", required=True)
    args = parser.parse_args()
    audit = json.loads(args.audit.read_text())
    if audit.get("status") != "PASS-K00-FILTERED-D9-EMITTER":
        raise RuntimeError("D9 audit did not pass")
    v9 = load_v9_validator()
    replay = v9.replay(args.matrix, args.solution, args.field)
    metadata, _, _ = v9.read_solution(args.solution)
    if int(metadata["cutoff"]) != 9 or int(metadata["rows"]) != 4998 or int(metadata["columns"]) != 10296:
        raise RuntimeError("D9 solution shape/cutoff mismatch")
    result = {
        **audit,
        "status": "PASS-K00-FILTERED-D9-ENDPOINT",
        "field": args.field,
        "rank": replay["rank"],
        "augmented_rank": replay["augmented_rank"],
        "D9_compatible": replay["consistent"],
        "replay": replay["replay"],
        "solution_nonzero_entries": replay.get("nonzero_solution_entries"),
        "certificate_entries": replay.get("certificate_entries"),
        "matrix_sha256": digest(args.matrix),
        "solution_or_certificate_sha256": digest(args.solution),
        "source_audit_sha256": digest(args.audit),
    }
    args.output.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("K00_D9_VALIDATOR_REPLAY=PASS")
    print("K00_D9_COMPATIBLE=" + ("1" if replay["consistent"] else "0"))
    print("K00_D9_ENDPOINT=PASS_FILTERED_D9_ONLY")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
