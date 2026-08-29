#!/usr/bin/env python3
"""Emit the exact normalized K00 cumulative Macaulay matrix at D8, AWS only."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V9 = ROOT / "cases/max12_812_order2_u2_62_k00_filtered_macaulay_v9_20260827/emit_filtered_macaulay.py"
V9_RESULT = ROOT / "cases/max12_812_order2_u2_62_k00_filtered_macaulay_v9_20260827/RESULT.md"
V9_EXACT = ROOT / "cases/max12_812_order2_u2_62_k00_filtered_macaulay_v9_20260827/aws_q_box01_pass/run/RESULT.json"
PREREG = HERE / "PREREGISTRATION.md"
EXPECTED = {
    V9: "fb82763da858be9d60971a43dca480c1426bd34cea35e2de795289bf47a93f7a",
    V9_RESULT: "bd1c636827061f1506573487618e533f34cfe413eab042be65411bfaa2eef178",
    V9_EXACT: "8749885b61ad08ae75dc2fd432e22d5a1ea9a27a84d130f5639a136595feb81e",
    PREREG: "e9cc8bf743d6ae8e7879697ee4382a00d01e89bab56ac1abcce8d3b1ba84dc0e",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_v9():
    spec = importlib.util.spec_from_file_location("k00_v9_frozen", V9)
    if spec is None or spec.loader is None:
        fail("cannot load frozen V9 emitter")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only D8 emitter refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only D8 emitter refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    tag = require_aws()
    for path, expected in EXPECTED.items():
        if expected == "TO_BE_FROZEN" or digest(path) != expected:
            fail(("frozen source mismatch", str(path), digest(path), expected))
    v9 = load_v9()
    tails = json.loads(v9.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != v9.EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")
    exact = json.loads(V9_EXACT.read_text())
    d7 = exact.get("cutoff_results", {}).get("7", {})
    if d7.get("rank") != 1372 or d7.get("augmented_rank") != 1372 or not d7.get("consistent"):
        fail("V9 D7 promotion sentinel mismatch")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    images = v9.substitutions()
    rows = {ell: v9.tail_sector(tails[str(ell)], ell, images, None) for ell in range(1, 8)}
    for ell, row in rows.items():
        if v9.degree_piece(row, 0) or v9.degree_piece(row, 1):
            fail(("K00 constant/linear sentinel", ell))
    matrix = output / "macaulay_D8.tsv"
    descriptor = v9.write_matrix(matrix, rows, 8)
    if descriptor["rows"] != 2996 or descriptor["columns"] != 5544:
        fail(("D8 shape mismatch", descriptor))
    audit = {
        "status": "PASS-K00-FILTERED-D8-EMITTER",
        "registered_aws_lane": tag,
        "characteristic_source": 0,
        "cutoff": 8,
        "descriptor": descriptor,
        "v9_emitter_sha256": digest(V9),
        "v9_result_sha256": digest(V9_RESULT),
        "v9_exact_result_sha256": digest(V9_EXACT),
        "preregistration_sha256": digest(PREREG),
        "scope": "K00_UNLOADED_FILTERED_MACAULAY_D8_ONLY",
    }
    audit_path = output / "SOURCE_AUDIT.json"
    audit_path.write_text(json.dumps(audit, sort_keys=True, indent=2) + "\n")
    print("K00_D8_SOURCE_HASHES=PASS")
    print("K00_D8_SHAPE=2996x5544")
    print(json.dumps(audit, sort_keys=True))


if __name__ == "__main__":
    main()
