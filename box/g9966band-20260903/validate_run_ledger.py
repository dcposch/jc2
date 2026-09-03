#!/usr/bin/env python3
"""Validate and summarize a completed g9966 branch run directory.

Only existing stage artifacts are read.  No band computation is run.
"""

from __future__ import annotations

import argparse
from decimal import Decimal, InvalidOperation
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
EMPTY_SHA256 = hashlib.sha256(b"").hexdigest()
ZERO_SINGULAR = b"// zero residual ideal over Q\n"
STAGE_FILE_RE = re.compile(r"stage(0|[1-9][0-9]*)\.(json|time|sing|err)\Z")
SHA256_RE = re.compile(r"[0-9a-f]{64}\Z")
EXPECTED_ENDPOINT = {
    "byte_identical": True,
    "delta2_dimension": 6689,
    "delta52_dimension": 6687,
    "rank": 15,
    "residual_count": 0,
    "result_sha256": "f4a6f39c81e01f185bc0e6aed74e844639d21ffce3d219b6a539ee110553ae66",
}
EXPECTED_PREBLOCK = {
    "imposed_D2_coordinate_rows": 5598,
    "Qstar_pivots": 5598,
    "surviving_coordinates": 1002,
    "redundant_D1_labels_on_deleted_coordinates": 15934,
}
EXPECTED_D1_PIVOTS = (41, 38, 33, 25, 19, 11, 6, 3)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


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
        require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_pinned_engine():
    actual = sha256_file(ENGINE)
    require(actual == PINNED_ENGINE_SHA256, "band_engine.py SHA-256 mismatch")
    name = "g9966_ledger_pinned_band_engine"
    spec = importlib.util.spec_from_file_location(name, ENGINE)
    require(spec is not None and spec.loader is not None, "cannot import pinned engine")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module, actual


def discover_stages(run_dir: Path) -> tuple[list[int], dict[tuple[int, str], Path]]:
    found: dict[tuple[int, str], Path] = {}
    for path in run_dir.iterdir():
        match = STAGE_FILE_RE.fullmatch(path.name)
        if match is None:
            continue
        require(path.is_file(), f"not a regular artifact: {path}")
        key = (int(match.group(1)), match.group(2))
        require(key not in found, f"duplicate stage artifact: {path.name}")
        found[key] = path
    require(found, "no stageN.{json,time,sing,err} artifacts found")
    stage_sets = {
        suffix: {stage for stage, kind in found if kind == suffix}
        for suffix in ("json", "time", "sing", "err")
    }
    require(len({frozenset(items) for items in stage_sets.values()}) == 1,
            f"incomplete stage artifact sets: {stage_sets}")
    stages = sorted(stage_sets["json"])
    require(stages == list(range(stages[-1] + 1)),
            f"stages are not contiguous from zero: {stages}")
    return stages, found


def parse_elapsed(value: str) -> float:
    pieces = value.strip().split(":")
    require(len(pieces) in (2, 3), f"invalid GNU time elapsed value: {value!r}")
    try:
        numbers = [Decimal(piece) for piece in pieces]
    except InvalidOperation as exc:
        raise ValueError(f"invalid GNU time elapsed value: {value!r}") from exc
    require(all(number >= 0 for number in numbers), "negative GNU time elapsed value")
    if len(numbers) == 2:
        minutes, seconds = numbers
        total = 60 * minutes + seconds
    else:
        hours, minutes, seconds = numbers
        total = 3600 * hours + 60 * minutes + seconds
    return float(total)


def parse_gnu_time(payload: bytes, path: Path) -> dict[str, int | float]:
    text = payload.decode("utf-8")
    elapsed = re.findall(
        r"^\s*Elapsed \(wall clock\) time \(h:mm:ss or m:ss\):\s*(\S+)\s*$",
        text,
        re.MULTILINE,
    )
    rss = re.findall(r"^\s*Maximum resident set size \(kbytes\):\s*(\d+)\s*$",
                     text, re.MULTILINE)
    exits = re.findall(r"^\s*Exit status:\s*(\d+)\s*$", text, re.MULTILINE)
    require(len(elapsed) == len(rss) == len(exits) == 1,
            f"missing or duplicate GNU time fields in {path.name}")
    require(int(exits[0]) == 0, f"nonzero GNU time exit status in {path.name}")
    return {"wall_seconds": parse_elapsed(elapsed[0]), "max_rss_kib": int(rss[0])}


def artifact_record(path: Path, payload: bytes) -> dict[str, Any]:
    return {"file": path.name, "bytes": len(payload), "sha256": sha256_bytes(payload)}


def validate_outer(outer: dict[str, Any], stage: int,
                   previous_offsets: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], dict[str, int]]:
    require(outer.get("preblock") == EXPECTED_PREBLOCK, "outer D2 preblock mismatch")
    offsets = outer.get("D1_offsets")
    require(isinstance(offsets, list), "outer D1_offsets is not a list")
    require(len(offsets) == min(stage, 7) + 1, "wrong number of outer D1 offsets")
    require(offsets[:len(previous_offsets)] == previous_offsets,
            "outer D1 ledger is not cumulative")
    for index, item in enumerate(offsets):
        require(isinstance(item, dict) and item.get("offset") == index,
                f"invalid outer D1 offset {index}")
        raw = item.get("raw_rows")
        pivots = item.get("Qstar_pivots")
        dependent = item.get("dependent_zero")
        variables = item.get("pivot_variables")
        by_block = item.get("by_block")
        require(all(isinstance(value, int) and value >= 0
                    for value in (raw, pivots, dependent)),
                f"invalid outer counts at offset {index}")
        require(pivots == EXPECTED_D1_PIVOTS[index],
                f"outer pivot count mismatch at offset {index}")
        require(isinstance(variables, list) and len(variables) == pivots,
                f"outer pivot-variable count mismatch at offset {index}")
        require(isinstance(by_block, dict)
                and sum(block["raw_rows"] for block in by_block.values()) == raw,
                f"outer by-block raw count mismatch at offset {index}")
        require(raw == pivots + dependent,
                f"outer elimination accounting mismatch at offset {index}")
    cumulative = sum(item["Qstar_pivots"] for item in offsets)
    require(outer.get("D1_cumulative_pivots") == cumulative,
            "outer cumulative pivot count mismatch")
    require(outer.get("outer_free_count")
            == EXPECTED_PREBLOCK["surviving_coordinates"] - cumulative,
            "outer free count mismatch")
    new_offsets = offsets[len(previous_offsets):]
    return offsets, {
        "raw_rows": sum(item["raw_rows"] for item in new_offsets),
        "Qstar_pivots": sum(item["Qstar_pivots"] for item in new_offsets),
        "offset": new_offsets[0]["offset"] if len(new_offsets) == 1 else None,
    }


def validate_stage(
    branch: str,
    stage: int,
    paths: dict[tuple[int, str], Path],
    engine: Any,
    driver_hash: str,
    previous: dict[str, Any] | None,
    final_stage: int,
) -> tuple[dict[str, Any], dict[str, Any]]:
    payloads = {kind: paths[(stage, kind)].read_bytes()
                for kind in ("json", "time", "sing", "err")}
    require(payloads["err"] == b"", f"stage{stage}.err is not empty")
    document = json.loads(payloads["json"], object_pairs_hook=reject_duplicate_keys)
    require(isinstance(document, dict), f"stage{stage}.json root is not an object")
    require(document.get("driver_sha256") == driver_hash,
            f"stage {stage}: embedded driver SHA-256 mismatch")
    require(document.get("branch") == branch, f"stage {stage}: branch mismatch")
    spec = engine.stage_spec(branch, stage)
    require(document.get("stage_spec") == spec, f"stage {stage}: stage_spec mismatch")
    require(document.get("next_stage") == engine.stage_spec(branch, stage + 1),
            f"stage {stage}: next_stage mismatch")
    require(document.get("charged_endpoint") == EXPECTED_ENDPOINT,
            f"stage {stage}: charged endpoint replay mismatch")

    accounting = document.get("row_accounting")
    require(isinstance(accounting, dict) and accounting.get("prior")
            == {"F": 3, "G": 3, "J162": 10},
            f"stage {stage}: prior row accounting mismatch")
    expected_stage_rows = []
    for current in range(stage + 1):
        current_spec = engine.stage_spec(branch, current)
        local = current_spec["pole_local_power"]
        expected_stage_rows.append({
            "stage": current,
            "F": len(engine.raw_minor_tags(branch, "F", local)),
            "G": len(engine.raw_minor_tags(branch, "G", local)),
            "J": len(current_spec["jacobian"]["w_powers"]),
        })
    require(accounting.get("stages") == expected_stage_rows,
            f"stage {stage}: continuation row accounting mismatch")
    local = spec["pole_local_power"]
    pole_labels = {
        name: [f"stage{stage}_{name}_local{local}_coord{k}"
               for k in engine.raw_minor_tags(branch, name, local)]
        for name in ("F", "G")
    }
    jspec = spec["jacobian"]
    jacobian_labels = [f"stage{stage}_J_d{jspec['degree']}_k{k}"
                       for k in jspec["w_powers"]]

    outer = document.get("outer_major")
    require(isinstance(outer, dict), f"stage {stage}: outer_major missing")
    previous_offsets = [] if previous is None else previous["outer_offsets"]
    outer_offsets, new_outer = validate_outer(outer, stage, previous_offsets)

    elimination = document.get("joint_elimination")
    require(isinstance(elimination, dict), f"stage {stage}: elimination missing")
    total_rows = 16 + sum(item["F"] + item["G"] + item["J"]
                          for item in expected_stage_rows)
    require(elimination.get("input_row_labels_excluding_preeliminated_major_rows")
            == total_rows, f"stage {stage}: input row count mismatch")
    cumulative_joint = elimination.get("Qstar_pivots")
    zero_rows = elimination.get("dependent_or_zero_rows")
    residual_count = elimination.get("residual_count")
    pivot_ledger = elimination.get("pivot_ledger")
    residual_rows = elimination.get("residual_rows")
    require(all(isinstance(value, int) and value >= 0
                for value in (cumulative_joint, zero_rows, residual_count)),
            f"stage {stage}: invalid joint counts")
    require(isinstance(pivot_ledger, list) and len(pivot_ledger) == cumulative_joint,
            f"stage {stage}: joint pivot ledger mismatch")
    require(isinstance(residual_rows, list) and len(residual_rows) == residual_count,
            f"stage {stage}: residual row count mismatch")
    require(cumulative_joint + zero_rows + residual_count == total_rows,
            f"stage {stage}: joint elimination accounting mismatch")
    raw_nonzero = elimination.get("raw_nonzero_count")
    require(isinstance(raw_nonzero, int) and 0 <= raw_nonzero <= total_rows,
            f"stage {stage}: invalid raw nonzero count")
    for pivot in pivot_ledger:
        require(isinstance(pivot, dict)
                and all(isinstance(pivot.get(key), str) and pivot[key]
                        for key in ("row", "variable", "coefficient", "rhs")),
                f"stage {stage}: malformed joint pivot")
    residue_hash = elimination.get("residual_hash")
    require(isinstance(residue_hash, str) and SHA256_RE.fullmatch(residue_hash),
            f"stage {stage}: invalid residual hash")
    has_residue = residual_count > 0
    require(document.get("nonlinear_residue_appears") is has_residue,
            f"stage {stage}: nonlinear residue status mismatch")
    if has_residue:
        require(payloads["sing"] != ZERO_SINGULAR,
                f"stage {stage}: nonzero residue has zero-ideal Singular marker")
    else:
        require(residue_hash == EMPTY_SHA256,
                f"stage {stage}: zero residue hash mismatch")
        require(payloads["sing"] == ZERO_SINGULAR,
                f"stage {stage}: zero residue Singular artifact mismatch")

    singular = elimination.get("singular")
    require(isinstance(singular, dict) and isinstance(singular.get("unit_ideal"), bool),
            f"stage {stage}: Singular status missing")
    unit = singular["unit_ideal"]
    require(document.get("verdict") == ("DEAD" if unit else "COUNTING-BOUND"),
            f"stage {stage}: verdict/Singular mismatch")
    require(not unit or stage == final_stage,
            f"stage {stage}: run continues after a DEAD stage")

    counts = document.get("counts")
    major = document.get("major")
    require(isinstance(counts, dict) and isinstance(major, dict),
            f"stage {stage}: dimension metadata missing")
    inner = counts.get("inner_free_before_outer")
    outer_free = counts.get("outer_free_after_current_major_band")
    linear_free = counts.get("linear_free_before_residue")
    codimension = singular.get("codimension")
    require(all(isinstance(value, int) and value >= 0
                for value in (inner, outer_free, linear_free, codimension)),
            f"stage {stage}: invalid dimension operands")
    require(major.get("inner_dimension_including_centres") == inner,
            f"stage {stage}: inner dimension mismatch")
    require(outer.get("outer_free_count") == outer_free,
            f"stage {stage}: outer dimension mismatch")
    require(linear_free == inner + outer_free - cumulative_joint,
            f"stage {stage}: linear dimension formula fails")
    generators = document.get("unresolved_quotient_generators")
    require(isinstance(generators, list) and generators == sorted(set(generators))
            and len(generators) == linear_free,
            f"stage {stage}: unresolved generator list mismatch")
    require(document.get("free_coordinate_list_is_valid") is (not has_residue),
            f"stage {stage}: free-coordinate status mismatch")

    major_prefix_free = inner + EXPECTED_PREBLOCK["Qstar_pivots"] \
        + EXPECTED_PREBLOCK["surviving_coordinates"]
    cumulative_rank = EXPECTED_PREBLOCK["Qstar_pivots"] \
        + outer["D1_cumulative_pivots"] + cumulative_joint + codimension
    dimension = counts.get("exact_Krull_dimension_localized")
    if unit:
        require(dimension is None, f"stage {stage}: DEAD dimension must be null")
        cumulative_rank_value = None
    else:
        require(isinstance(dimension, int) and dimension >= 0,
                f"stage {stage}: invalid localized dimension")
        require(dimension == linear_free - codimension,
                f"stage {stage}: localized dimension formula fails")
        require(dimension == major_prefix_free - cumulative_rank,
                f"stage {stage}: cumulative rank formula fails")
        cumulative_rank_value = cumulative_rank

    time_data = parse_gnu_time(payloads["time"], paths[(stage, "time")])
    resources = document.get("resources")
    require(isinstance(resources, dict)
            and isinstance(resources.get("wall_seconds"), (int, float))
            and isinstance(resources.get("peak_rss_kib"), int),
            f"stage {stage}: internal resource data missing")
    require(time_data["wall_seconds"] >= resources["wall_seconds"],
            f"stage {stage}: external wall time is below internal wall time")
    require(time_data["max_rss_kib"] >= resources["peak_rss_kib"],
            f"stage {stage}: external max RSS is below internal peak RSS")

    current_pivots = {(item["row"], item["variable"]) for item in pivot_ledger}
    prior_pivots = set() if previous is None else previous["joint_pivots"]
    prior_joint_count = 0 if previous is None else previous["joint_count"]
    previous_dimension = None if previous is None else previous["dimension"]
    decrement = (previous_dimension - dimension
                 if isinstance(previous_dimension, int) and isinstance(dimension, int)
                 else None)
    summary = {
        "stage": stage,
        "band": {
            "D1_offset": spec["D1_offset"],
            "pole_local_power": spec["pole_local_power"],
            "pole_exponents": spec["pole_exponents"],
            "Jacobian_degree": jspec["degree"],
            "Jacobian_t_power": jspec["t_power"],
        },
        "new_outer_D1": new_outer,
        "new_row_labels": {"pole": pole_labels, "Jacobian": jacobian_labels},
        "joint_Qstar_pivots": {
            "cumulative": cumulative_joint,
            "net_new": cumulative_joint - prior_joint_count,
            "introduced": [{"row": row, "variable": variable}
                           for row, variable in sorted(current_pivots - prior_pivots)],
            "retired": [{"row": row, "variable": variable}
                        for row, variable in sorted(prior_pivots - current_pivots)],
        },
        "residue": {
            "status": "nonzero" if has_residue else "zero",
            "rows": residual_count,
            "sha256": residue_hash,
            "unit_ideal": unit,
            "codimension": codimension,
        },
        "dimension": dimension,
        "dimension_decrement_from_previous_stage": decrement,
        "dimension_drop_from_charged_endpoint": (
            EXPECTED_ENDPOINT[f"{branch}_dimension"] - dimension
            if isinstance(dimension, int) else None
        ),
        "rank_accounting": {
            "major_prefix_free": major_prefix_free,
            "outer_D2_pivots": EXPECTED_PREBLOCK["Qstar_pivots"],
            "outer_D1_cumulative_pivots": outer["D1_cumulative_pivots"],
            "joint_Qstar_cumulative_pivots": cumulative_joint,
            "residual_codimension": codimension,
            "cumulative_rank": cumulative_rank_value,
        },
        "external_resources": time_data,
        "artifacts": {
            kind: artifact_record(paths[(stage, kind)], payloads[kind])
            for kind in ("json", "time", "sing", "err")
        },
    }
    state = {
        "outer_offsets": outer_offsets,
        "joint_pivots": current_pivots,
        "joint_count": cumulative_joint,
        "dimension": dimension,
    }
    return summary, state


def build_ledger(branch: str, run_dir: Path) -> dict[str, Any]:
    require(run_dir.is_dir(), f"not a run directory: {run_dir}")
    engine, driver_hash = load_pinned_engine()
    stages, paths = discover_stages(run_dir)
    summaries = []
    previous = None
    for stage in stages:
        summary, previous = validate_stage(
            branch, stage, paths, engine, driver_hash, previous, stages[-1]
        )
        summaries.append(summary)
    return {
        "schema": "g9966-validated-run-ledger-v1",
        "status": "VALIDATED",
        "branch": branch,
        "run_directory": str(run_dir.resolve()),
        "pinned_driver": {"path": str(ENGINE), "sha256": driver_hash},
        "completed_through_stage": stages[-1],
        "stage_count": len(stages),
        "charged_endpoint": EXPECTED_ENDPOINT,
        "outer_D2_preblock": EXPECTED_PREBLOCK,
        "dimension_formula": (
            "major_prefix_free - (outer_D2 + outer_D1 + joint_Qstar + "
            "residual_codimension)"
        ),
        "rank_scope": (
            "The charged 15-pivot direct prefix is already among the cumulative joint "
            "rows and overlaps the outer quotient; it is not an extra rank summand."
        ),
        "final_verdict": "DEAD" if summaries[-1]["residue"]["unit_ideal"]
                         else "COUNTING-BOUND",
        "final_dimension": summaries[-1]["dimension"],
        "stages": summaries,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--branch", choices=("delta2", "delta52"), required=True)
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, help="write JSON here instead of stdout")
    args = parser.parse_args()
    try:
        ledger = build_ledger(args.branch, args.run_dir)
        payload = json.dumps(ledger, indent=2, sort_keys=True) + "\n"
        if args.output is None:
            sys.stdout.write(payload)
        else:
            args.output.write_text(payload, encoding="utf-8")
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
