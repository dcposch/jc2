#!/usr/bin/env python3
"""Replay the charged stage-7 custody chain without recomputing its bands."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
FROZEN = Path("/tmp/jc2-lane.OZ2xWA/inputs")
MANIFEST = FROZEN / "next-stage8-system.json"
FREE_LIST = FROZEN / "stage7-free-coefficients.txt"
ENGINE = ROOT / "box/g9966band-20260903/band_engine.py"
HELPER = ROOT / "box/g9966band-20260903/next_system_manifest.py"
VALIDATOR = ROOT / "box/g9966band-20260903/validate_run_ledger.py"
SOURCE_RUN = ROOT / "box/g9966band-20260903/runs/delta52"
STAGE7 = SOURCE_RUN / "stage7.json"
LEDGER = SOURCE_RUN / "validated-ledger.json"


def reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def digest_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    manifest_bytes = MANIFEST.read_bytes()
    manifest = json.loads(manifest_bytes, object_pairs_hook=reject_duplicates)
    stage_bytes = STAGE7.read_bytes()
    stage = json.loads(stage_bytes, object_pairs_hook=reject_duplicates)
    accepted = manifest["accepted_result"]

    require(Path(accepted["path"]).resolve() == STAGE7.resolve(), "stage-7 path mismatch")
    require(accepted["bytes"] == len(stage_bytes), "stage-7 byte count mismatch")
    require(accepted["sha256"] == digest_bytes(stage_bytes), "stage-7 digest mismatch")
    require(stage["driver_sha256"] == digest_bytes(ENGINE.read_bytes()), "driver digest mismatch")
    require(accepted["completed_stage"] == stage["stage_spec"]["stage"] == 7,
            "completed stage mismatch")
    require(stage["branch"] == "delta52", "branch mismatch")
    require(stage["joint_elimination"]["residual_count"] == 0, "stage-7 residue is nonzero")
    require(stage["joint_elimination"]["singular"]["unit_ideal"] is False,
            "stage-7 localized ideal unexpectedly unit")
    require(stage["outer_major"]["preblock"]["Qstar_pivots"] == 5598,
            "outer D2 rank mismatch")
    require(stage["outer_major"]["D1_cumulative_pivots"] == 176,
            "outer D1 rank mismatch")
    require(stage["joint_elimination"]["Qstar_pivots"] == 59,
            "joint Q-star rank mismatch")
    require(6702 - 5598 - 176 - 59 == stage["counts"]["exact_Krull_dimension_localized"] == 869,
            "stage-7 dimension formula mismatch")

    regenerated_manifest = subprocess.run(
        ["python3", str(HELPER), "--branch", "delta52", "--completed-stage", "7",
         "--result-json", str(STAGE7)], check=True, capture_output=True
    ).stdout
    require(regenerated_manifest == manifest_bytes, "stage-8 manifest replay is not byte-identical")

    expected_names = "".join(name + "\n" for name in manifest["unresolved_quotient_generators"])
    require(FREE_LIST.read_text(encoding="utf-8") == expected_names,
            "charged 869-name list mismatch")
    require(stage["unresolved_quotient_generators"] == manifest["unresolved_quotient_generators"],
            "stage-7 and manifest generator lists differ")

    regenerated_ledger = subprocess.run(
        ["python3", str(VALIDATOR), "--branch", "delta52", "--run-dir", str(SOURCE_RUN)],
        check=True, capture_output=True
    ).stdout
    require(regenerated_ledger == LEDGER.read_bytes(), "stage-7 ledger replay is not byte-identical")
    ledger = json.loads(regenerated_ledger, object_pairs_hook=reject_duplicates)
    require(ledger["status"] == "VALIDATED" and ledger["completed_through_stage"] == 7,
            "validated ledger endpoint mismatch")
    require(ledger["final_dimension"] == 869, "validated ledger dimension mismatch")

    print(json.dumps({
        "status": "CUSTODY-REPLAY-PASS",
        "stage7": {
            "path": str(STAGE7), "bytes": len(stage_bytes),
            "sha256": digest_bytes(stage_bytes), "dimension": 869,
            "outer_D2_rank": 5598, "outer_D1_rank": 176,
            "joint_Qstar_rank": 59, "residue_count": 0,
        },
        "manifest": {"path": str(MANIFEST), "bytes": len(manifest_bytes),
                     "sha256": digest_bytes(manifest_bytes), "byte_identical_replay": True},
        "free_coordinates": {"path": str(FREE_LIST), "count": len(manifest["unresolved_quotient_generators"]),
                             "sha256": digest_bytes(FREE_LIST.read_bytes()), "byte_identical": True},
        "ledger": {"path": str(LEDGER), "sha256": digest_bytes(LEDGER.read_bytes()),
                   "byte_identical_replay": True, "completed_through_stage": 7},
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
