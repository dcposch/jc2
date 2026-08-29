#!/usr/bin/env python3
"""Validate provisional exact V17 input extraction and freeze its hashes."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path


EXPECTED_SOURCE = "9e22780c0f9b38f2e502b08ac51c1b9d8fee21e7b40e9569d08d77a3683d8b5c"
EXPECTED_P_RESULT = "6e26a3211a86cbda10cdc8ead0e5cfc875964db2c44b225c99733e84fe71bdcc"
LOADS = ("K10", "K6", "K2")


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("artifact_dir", type=Path)
    parser.add_argument("singular_stdout", type=Path)
    parser.add_argument("compiled_v17_q", type=Path)
    parser.add_argument("p_v17_result", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    log = args.singular_stdout.read_text()
    if digest(args.compiled_v17_q) != EXPECTED_SOURCE or digest(args.p_v17_result) != EXPECTED_P_RESULT:
        fail("input hash gate")
    required = [
        "K00_V17_SYZ6_GENERATORS=66",
        "K00_V17_SYZ6_REPLAY=1",
        "K00_V18_EXACT_INPUT_DONE",
    ] + [f"K00_V18_EXACT_INPUT_{label}_IMAGE_GENERATORS=66" for label in LOADS]
    if any(token not in log for token in required):
        fail(("missing extraction sentinel", [token for token in required if token not in log]))
    hashes: dict[str, str] = {}
    for label in LOADS:
        for stem in ("IMAGE", "TARGET", "LOAD_ROWS"):
            path = args.artifact_dir / f"{stem}_{label}.txt"
            if not path.is_file() or path.stat().st_size == 0:
                fail(("missing/empty exact artifact", str(path)))
            hashes[path.name] = digest(path)
    syz = args.artifact_dir / "SYZ6_MODULE.txt"
    if not syz.is_file() or syz.stat().st_size == 0:
        fail("missing exact six-row syzygy serialization")
    hashes[syz.name] = digest(syz)
    result = {
        "status": "PASS-K00-V18-PROVISIONAL-EXACT-INPUT",
        "field": "Q",
        "syz6_generators": 66,
        "compiled_v17_q_sha256": EXPECTED_SOURCE,
        "p_v17_result_sha256": EXPECTED_P_RESULT,
        "singular_stdout_sha256": digest(args.singular_stdout),
        "artifact_sha256": hashes,
        "dependency": "V17-p65521 provisional; exact V17-Q local-colon endpoint pending",
        "firewall": "NO_V17_Q_BRANCH_CLAIM_NO_PROMOTION_NO_ARC_EXCLUSION",
    }
    args.output.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("K00_V18_PROVISIONAL_EXACT_INPUT_VALIDATION=PASS")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
