#!/usr/bin/env python3
"""Build a deterministic manifest for the next g9966 band-engine stage.

The exact finite system is the hash-pinned ``band_engine.py`` together with
the emitted argv.  This helper does not claim to expand or duplicate that
system's equations.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys
from typing import Any


HERE = Path(__file__).resolve().parent
ENGINE = HERE / "band_engine.py"
PINNED_ENGINE_SHA256 = (
    "3bd2937d75d59d59edeca1b89eba286fd2711f2d608109e7fd8971b64e059ac9"
)
SHA256_RE = re.compile(r"[0-9a-f]{64}\Z")


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def load_engine_stage_spec(actual_engine_hash: str):
    require(
        actual_engine_hash == PINNED_ENGINE_SHA256,
        "band_engine.py does not match the helper's pinned SHA-256",
    )
    module_name = "g9966_pinned_band_engine"
    spec = importlib.util.spec_from_file_location(module_name, ENGINE)
    require(spec is not None and spec.loader is not None, "cannot load pinned engine")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module.stage_spec


def validate_result(
    result: dict[str, Any], branch: str, completed_stage: int, engine_hash: str
) -> tuple[list[str], dict[str, Any]]:
    require(result.get("driver_sha256") == engine_hash, "result driver SHA-256 mismatch")
    require(result.get("branch") == branch, "result branch mismatch")

    completed_spec = result.get("stage_spec")
    require(isinstance(completed_spec, dict), "result stage_spec is missing")
    require(completed_spec.get("stage") == completed_stage, "result completed stage mismatch")

    elimination = result.get("joint_elimination")
    require(isinstance(elimination, dict), "result joint_elimination is missing")
    residue_count = elimination.get("residual_count")
    residue_rows = elimination.get("residual_rows")
    residue_hash = elimination.get("residual_hash")
    require(isinstance(residue_count, int) and residue_count >= 0, "invalid residual_count")
    require(isinstance(residue_rows, list), "invalid residual_rows")
    require(len(residue_rows) == residue_count, "residual row/count mismatch")
    require(isinstance(residue_hash, str) and SHA256_RE.fullmatch(residue_hash) is not None,
            "invalid residual_hash")
    for index, row in enumerate(residue_rows):
        require(isinstance(row, dict), f"residual row {index} is not an object")
        require(isinstance(row.get("label"), str), f"residual row {index} has no label")
        require(isinstance(row.get("expression"), str),
                f"residual row {index} has no expression")

    has_residue = residue_count != 0
    require(result.get("nonlinear_residue_appears") is has_residue,
            "nonlinear residue status disagrees with residual_count")

    singular = elimination.get("singular")
    require(isinstance(singular, dict), "result Singular status is missing")
    unit_ideal = singular.get("unit_ideal")
    require(isinstance(unit_ideal, bool), "invalid Singular unit_ideal status")
    verdict = result.get("verdict")
    require(verdict == ("DEAD" if unit_ideal else "COUNTING-BOUND"),
            "verdict disagrees with Singular unit-ideal status")
    require(not unit_ideal, "completed result is DEAD; no next system exists")

    generators = result.get("unresolved_quotient_generators")
    require(isinstance(generators, list), "unresolved generator list is missing")
    require(all(isinstance(item, str) and item for item in generators),
            "invalid unresolved generator name")
    require(generators == sorted(set(generators)),
            "unresolved generator list is not sorted and unique")
    require(result.get("free_coordinate_list_is_valid") is (not has_residue),
            "free-coordinate status disagrees with residue status")

    counts = result.get("counts")
    require(isinstance(counts, dict), "result counts are missing")
    dimension = counts.get("exact_Krull_dimension_localized")
    require(isinstance(dimension, int) and 0 <= dimension <= len(generators),
            "invalid localized Krull dimension")

    return generators, {
        "status": "nonzero" if has_residue else "zero",
        "count": residue_count,
        "sha256": residue_hash,
        "localized_unit_ideal": unit_ideal,
    }


def build_manifest(branch: str, completed_stage: int, result_path: Path) -> dict[str, Any]:
    require(completed_stage >= 0, "completed stage must be nonnegative")
    engine_hash = sha256_file(ENGINE)
    stage_spec = load_engine_stage_spec(engine_hash)

    result_bytes = result_path.read_bytes()
    parsed = json.loads(result_bytes, object_pairs_hook=reject_duplicate_keys)
    require(isinstance(parsed, dict), "result JSON root is not an object")
    generators, residue = validate_result(parsed, branch, completed_stage, engine_hash)

    expected_completed_spec = stage_spec(branch, completed_stage)
    require(parsed["stage_spec"] == expected_completed_spec,
            "embedded completed stage_spec disagrees with pinned engine")
    next_spec = stage_spec(branch, completed_stage + 1)
    require(parsed.get("next_stage") == next_spec,
            "embedded next_stage disagrees with pinned engine")

    argv = [
        "python3",
        str(ENGINE),
        "--branch",
        branch,
        "--stage",
        str(completed_stage + 1),
    ]
    return {
        "schema": "g9966-next-system-manifest-v1",
        "type": "EXACT-NEXT-SYSTEM / PINNED-EXECUTABLE",
        "accepted_result": {
            "path": str(result_path.resolve()),
            "bytes": len(result_bytes),
            "sha256": sha256_bytes(result_bytes),
            "embedded_driver_sha256": parsed["driver_sha256"],
            "branch": branch,
            "completed_stage": completed_stage,
            "verdict": parsed["verdict"],
            "localized_Krull_dimension": parsed["counts"]["exact_Krull_dimension_localized"],
            "residue": residue,
        },
        "unresolved_generator_count": len(generators),
        "unresolved_quotient_generators": generators,
        "next_stage_spec": next_spec,
        "pinned_executable": {
            "source": str(ENGINE),
            "source_sha256": engine_hash,
            "argv": argv,
        },
        "exact_system_definition": (
            "The pinned band_engine.py source plus argv is the executable exact finite "
            "system; this manifest does not claim to contain expanded equations."
        ),
        "limitations": [
            "Execution still depends on the frozen charged inputs verified by band_engine.py.",
            "The K2c computation basis uses the charged structural coordinate certificate; "
            "the full inverse map to original C2/C3 names is not serialized.",
            "The argv writes the next result to stdout; output capture and --emit-singular "
            "may be added by the invoking runner without changing the mathematical stage.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--branch", choices=("delta2", "delta52"), required=True)
    parser.add_argument("--completed-stage", type=int, required=True)
    parser.add_argument("--result-json", type=Path, required=True)
    parser.add_argument("--output", type=Path,
                        help="write here instead of stdout; overwritten deterministically")
    args = parser.parse_args()

    manifest = build_manifest(args.branch, args.completed_stage, args.result_json)
    payload = json.dumps(manifest, indent=2, sort_keys=True) + "\n"
    if args.output is None:
        sys.stdout.write(payload)
    else:
        args.output.write_text(payload, encoding="utf-8")


if __name__ == "__main__":
    main()
