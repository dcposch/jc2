#!/usr/bin/env python3
"""Promote and validate one successful continuation stage."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "box/g9966s8-20260903"
RUN = BASE / "runs/delta52"
VALIDATOR = ROOT / "box/g9966band-20260903/validate_run_ledger.py"
MANIFEST_HELPER = ROOT / "box/g9966band-20260903/next_system_manifest.py"
ENGINE_SHA256 = "3bd2937d75d59d59edeca1b89eba286fd2711f2d608109e7fd8971b64e059ac9"


def reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in pairs:
        if key in out:
            raise ValueError(f"duplicate JSON key: {key}")
        out[key] = value
    return out


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("stage", type=int)
    args = parser.parse_args()
    stage_number = args.stage
    require(stage_number >= 8, "stage must be at least 8")
    attempt = BASE / f"attempts/stage{stage_number}"

    sources = {suffix: attempt / f"stage{stage_number}.{suffix}"
               for suffix in ("json", "time", "sing", "err")}
    require(all(path.is_file() for path in sources.values()), "attempt artifact set is incomplete")
    require(sources["json"].stat().st_size > 0, "stage JSON is empty")
    require(sources["time"].stat().st_size > 0, "GNU-time record is empty")
    require(sources["err"].stat().st_size == 0, "stage stderr is nonempty")

    stage = json.loads(sources["json"].read_bytes(), object_pairs_hook=reject_duplicates)
    require(stage.get("branch") == "delta52", "stage branch mismatch")
    require(stage.get("stage_spec", {}).get("stage") == stage_number, "stage number mismatch")
    require(stage.get("driver_sha256") == ENGINE_SHA256, "stage engine digest mismatch")

    RUN.mkdir(parents=True, exist_ok=True)
    for suffix, source in sources.items():
        destination = RUN / f"stage{stage_number}.{suffix}"
        require(not destination.exists() and not destination.is_symlink(),
                f"refusing to overwrite canonical artifact: {destination}")
        os.link(source, destination)
        require(digest(source) == digest(destination), f"promotion digest mismatch: {suffix}")

    ledger_bytes = subprocess.run(
        ["python3", str(VALIDATOR), "--branch", "delta52", "--run-dir", str(RUN)],
        check=True, capture_output=True
    ).stdout
    ledger = json.loads(ledger_bytes, object_pairs_hook=reject_duplicates)
    require(ledger["status"] == "VALIDATED", "ledger validation failed")
    require(ledger["completed_through_stage"] == stage_number, "ledger endpoint mismatch")
    ledger_path = BASE / f"validated-through-stage{stage_number}.json"
    require(not ledger_path.exists(), f"refusing to overwrite {ledger_path}")
    ledger_path.write_bytes(ledger_bytes)

    terminal = ledger["stages"][-1]
    dimensions = [item["dimension"] for item in ledger["stages"]]
    zero_decrements = 0
    for item in reversed(ledger["stages"][1:]):
        if item["dimension_decrement_from_previous_stage"] == 0:
            zero_decrements += 1
        else:
            break

    residue_rows = stage["joint_elimination"]["residual_rows"]
    constants = [row for row in residue_rows
                 if not __import__("sympy").sympify(row["expression"]).free_symbols
                 and __import__("sympy").sympify(row["expression"]) != 0]
    unit = terminal["residue"]["unit_ideal"]
    next_manifest = None
    if not unit:
        next_manifest = BASE / f"next-stage{stage_number + 1}-system.json"
        require(not next_manifest.exists(), f"refusing to overwrite {next_manifest}")
        payload = subprocess.run(
            ["python3", str(MANIFEST_HELPER), "--branch", "delta52",
             "--completed-stage", str(stage_number), "--result-json",
             str(RUN / f"stage{stage_number}.json")], check=True, capture_output=True
        ).stdout
        next_manifest.write_bytes(payload)

    summary = {
        "status": "ACCEPTED",
        "stage": stage_number,
        "stage_json_sha256": digest(RUN / f"stage{stage_number}.json"),
        "band": terminal["band"],
        "new_rows": terminal["new_row_labels"],
        "joint_Qstar_pivots": terminal["joint_Qstar_pivots"],
        "new_outer_D1": terminal["new_outer_D1"],
        "residue": terminal["residue"],
        "constant_residue_rows": constants,
        "dimension": terminal["dimension"],
        "dimension_decrement": terminal["dimension_decrement_from_previous_stage"],
        "consecutive_zero_decrements": zero_decrements,
        "external_resources": terminal["external_resources"],
        "unresolved_generator_count": len(stage["unresolved_quotient_generators"]),
        "free_coordinate_list_is_valid": stage["free_coordinate_list_is_valid"],
        "stop": {
            "dead": unit,
            "stabilized_two_bands": zero_decrements >= 2,
            "small_dimension": isinstance(terminal["dimension"], int) and terminal["dimension"] <= 20,
        },
        "ledger": {"path": str(ledger_path), "sha256": digest(ledger_path)},
        "next_system": None if next_manifest is None else
            {"path": str(next_manifest), "sha256": digest(next_manifest)},
        "dimension_history": dimensions,
    }
    summary_path = BASE / f"stage{stage_number}-summary.json"
    require(not summary_path.exists(), f"refusing to overwrite {summary_path}")
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
