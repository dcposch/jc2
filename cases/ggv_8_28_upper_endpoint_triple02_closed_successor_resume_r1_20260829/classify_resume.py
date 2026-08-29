#!/usr/bin/env python3
"""Fail-closed independent classifier for the closed-successor recursion.

Re-derives the terminal classification from the stage artifacts alone
(deliberately restating every expected marker and census) and requires exact
agreement with the driver's SUMMARY.json before anything is published.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys


FROZEN_R5_SHA256 = "d679a4d7fb4bf2619fbb3ff47ea6f386ba1c75fdc477276cabf3bec8a2b2cd90"
TRANSCRIPT_GATE_SHA256 = (
    "0e0efd5ada59039a373a731038f2f88a3794b376b208879c2459bff97d0e7316")
DELTA_NODE1_SHA256 = (
    "84b4c2c4c0bfe5aa7414c35813cc1cf63d7d5416358a394b8e8bdc35820f1d02")
NODE2_GENERATOR_SHA256 = (
    "2b9d29b706ce5d7e58e2dc5a28799782f5610c5ccb7b71987ebd694fd8b83206",
    "fecd1d43f3f55e1c65bec858303b7688c0db83dbe9c3a60f51f70130a4149336",
    DELTA_NODE1_SHA256,
)
CLASS_DEAD = "EXACT_ENDPOINT_DEAD_ON_TRIPLE02_NODE1_CLOSED_SUCCESSOR_FINITE_COVER"
CLASS_SURVIVOR = ("RING_LEVEL_ENDPOINT_SURVIVOR_ON_TRIPLE02_NODE1_"
                  "CLOSED_SUCCESSOR_CHART_PENDING_NILPOTENCE_RADICAL")
CLASS_NO_VERDICT = "NO_VERDICT_OPEN_REMAINDER_ON_TRIPLE02_NODE1_CLOSED_SUCCESSOR"
CLASS_REVERSE = ("REVERSE_CONTAINMENT_SEARCH_EXHAUSTED_NO_VERDICT_ON_"
                 "TRIPLE02_NODE1_CLOSED_SUCCESSOR")
ALLOWED = {CLASS_DEAD, CLASS_SURVIVOR, CLASS_NO_VERDICT, CLASS_REVERSE}
WITNESS_REPLAY_MARKERS = (
    "NODE_INDEX=1",
    "NODE_GENERATOR_COUNT=2",
    "NODE_EMPTY=0",
    "NODE_REDUCER_FIXTURES_PASS=1",
    "NF_RATIONAL_UNIT_PIVOT_COUNT=95",
    "NF_PIVOT_INVARIANT_FAILURES=0",
    "NODE_RESIDUAL_REDUCTION_COMPLETE=1",
    "WITNESS_MINOR_ROWS=1,2,4,7,9,11",
    "WITNESS_MINOR_COLS=1,2,3,5,6,7",
    "WITNESS_DELTA_NF_NONZERO=1",
    "WITNESS_DELTA_EQUALS_ARCHIVED=1",
    "WITNESS_DELTA_NF_STABLE=1",
    "CLOSED_SUCCESSOR_GENERATOR_COUNT=3",
    "CLOSED_SUCCESSOR_CONTAINS_DELTA=1",
    "NODE1_OPEN_SATURATION_ENTERED=0",
    "NODE1_PURE_DELTA_POWER_SEARCH_ENTERED=0",
    "NODE1_PROPER_OPEN_CHART_ENTERED=0",
    "SETTLED_OPEN_ROUTE_NOT_REENTERED=1",
    "WITNESS_REPLAY_COMPLETE=1",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def load_pinned(name: str, path: Path, expected_sha: str,
                with_parent_path: bool = False):
    if sha256(path) != expected_sha:
        raise SystemExit(f"PINNED_MODULE_SHA_DRIFT:{name}")
    if with_parent_path:
        sys.path.insert(0, str(path.parent))
    try:
        spec = importlib.util.spec_from_file_location(name, path)
        if spec is None or spec.loader is None:
            raise SystemExit(f"PINNED_MODULE_IMPORT_FAILURE:{name}")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    finally:
        if with_parent_path:
            sys.path.pop(0)


def stage_lines(node_dir: Path, label: str, gate,
                expect_timeout: bool = False) -> list[str]:
    stdout = node_dir / f"{label}.stdout.txt"
    stderr = node_dir / f"{label}.stderr.txt"
    result = node_dir / f"{label}.result.json"
    script = node_dir / (f"{label}.sing"
                         if (node_dir / f"{label}.sing").is_file()
                         else "witness_replay.sing")
    payload = json.loads(result.read_text())
    if payload.get("timed_out") is not (True if expect_timeout else False):
        raise RuntimeError(f"STAGE_TIMEOUT_FLAG_DISAGREEMENT:{label}")
    if not expect_timeout and payload.get("returncode") != 0:
        raise RuntimeError(f"STAGE_RETURNCODE_DISAGREEMENT:{label}")
    if (payload.get("stdout_sha256") != sha256(stdout)
            or payload.get("stderr_sha256") != sha256(stderr)
            or payload.get("script_sha256") != sha256(script)):
        raise RuntimeError(f"STAGE_RESULT_CUSTODY_DISAGREEMENT:{label}")
    lines = stdout.read_text(errors="strict").splitlines()
    if not expect_timeout:
        gate.assert_clean_transcript(stdout, stderr)
        if any(line.startswith("FATAL_") for line in lines):
            raise RuntimeError(f"FATAL_MARKER_IN_STAGE:{label}")
    return lines


def require_lines(lines: list[str], markers: tuple[str, ...],
                  label: str) -> None:
    bad = [marker for marker in markers if lines.count(marker) != 1]
    if bad:
        raise RuntimeError(f"MARKER_CENSUS:{label}:{','.join(bad)}")


def parse_exact_int(lines: list[str], key: str) -> int:
    prefix = key + "="
    values = [line[len(prefix):] for line in lines if line.startswith(prefix)]
    if len(values) != 1:
        raise RuntimeError(f"INTEGER_MARKER_CENSUS:{key}:{len(values)}")
    return int(values[0])


def require_file_census(path: Path, header: str, records: int) -> str:
    lines = path.read_text().splitlines()
    if len(lines) != records + 1 or lines[0] != header:
        raise RuntimeError(f"ARTIFACT_CENSUS:{path.name}:{len(lines)}")
    return sha256(path)


def require_exact_match(actual: Path, expected: Path, label: str) -> str:
    if actual.read_bytes() != expected.read_bytes():
        raise RuntimeError(f"EXACT_REPLAY_DISAGREEMENT:{label}")
    return sha256(actual)


def classify_witness_replay(production: Path, prepared: Path, build: Path,
                            gate) -> dict[str, object]:
    witness_dir = production / "witness_replay"
    build_manifest = json.loads((build / "BUILD_MANIFEST.json").read_text())
    script = witness_dir / "witness_replay.sing"
    if sha256(script) != build_manifest["generated_witness_replay_sha256"]:
        raise RuntimeError("WITNESS_REPLAY_SCRIPT_HASH_DRIFT")
    lines = stage_lines(witness_dir, "witness_replay", gate)
    require_lines(lines, WITNESS_REPLAY_MARKERS, "witness_replay")
    if sum(line in lines for line in
           ("CLOSED_SUCCESSOR_EMPTY=0", "CLOSED_SUCCESSOR_EMPTY=1")) != 1:
        raise RuntimeError("CLOSED_SUCCESSOR_EMPTY_MARKER_CENSUS")
    hashes = {}
    for produced, archived in (
            ("NODE_001_STANDARD_BASIS.txt",
             "r3/output/node_001/NODE_001_STANDARD_BASIS.txt"),
            ("NODE_001_REDUCE_PIVOTS.tsv",
             "r3/output/node_001/NODE_001_REDUCE_PIVOTS.tsv"),
            ("NODE_001_REDUCE_RESIDUAL.tsv",
             "r3/output/node_001/NODE_001_REDUCE_RESIDUAL.tsv")):
        hashes[produced] = require_exact_match(
            witness_dir / produced, prepared / archived,
            f"witness:{produced}")
    return {"witness_replay_artifact_sha256": hashes,
            "closed_successor_empty_at_seed":
                "CLOSED_SUCCESSOR_EMPTY=1" in lines}


def classify_node(node_dir: Path, node_index: int, generators_sha: list[str],
                  rank_bound: int, r5, gate,
                  timeout_stage: str | None) -> dict[str, object]:
    node_input = json.loads((node_dir / "NODE_INPUT.json").read_text())
    if (node_input.get("node") != node_index
            or node_input.get("inherited_rank_upper_bound") != rank_bound
            or node_input.get("generator_sha256") != generators_sha
            or len(node_input.get("generators", [])) != len(generators_sha)):
        raise RuntimeError(f"NODE_INPUT_CHAIN_DRIFT:{node_index}")
    literals = [
        "".join(value.split()) for value in node_input["generators"]]
    if [sha256_text(value) for value in literals] != generators_sha:
        raise RuntimeError(f"NODE_INPUT_LITERAL_HASH_DRIFT:{node_index}")
    outcome: dict[str, object] = {"node": node_index,
                                  "rank_upper_bound_in": rank_bound}
    if timeout_stage is not None:
        stage_lines(node_dir, timeout_stage, gate, expect_timeout=True)
        outcome["timed_out_stage"] = timeout_stage
        outcome["status"] = "STAGE_TIMEOUT"
        return outcome
    reduce_lines = stage_lines(node_dir, "reduce", gate)
    if "EXACT_EMPTY_NODE=1" in reduce_lines:
        require_lines(reduce_lines, (
            f"NODE_INDEX={node_index}",
            f"NODE_GENERATOR_COUNT={len(generators_sha)}",
            "NODE_EMPTY=1",
            "EXACT_EMPTY_NODE=1",
        ), f"reduce:{node_index}")
        outcome["status"] = "EXACT_EMPTY_NODE"
        return outcome
    require_lines(reduce_lines, (
        f"NODE_INDEX={node_index}",
        f"NODE_GENERATOR_COUNT={len(generators_sha)}",
        "NODE_EMPTY=0",
        "NODE_REDUCER_FIXTURES_PASS=1",
        "NF_RATIONAL_UNIT_PIVOT_COUNT=95",
        "NF_PIVOT_INVARIANT_FAILURES=0",
        "NODE_RESIDUAL_REDUCTION_COMPLETE=1",
        "NODE_REDUCE_COMPLETE=1",
    ), f"reduce:{node_index}")
    require_file_census(node_dir / f"NODE_{node_index:03d}_REDUCE_PIVOTS.tsv",
                        "step|source_row|source_col|pivot", 95)
    require_file_census(node_dir / f"NODE_{node_index:03d}_REDUCE_RESIDUAL.tsv",
                        "rows|11|cols|10", 110)
    rank = -1
    for size in range(rank_bound, -1, -1):
        script = node_dir / f"rank_size_{size}.sing"
        if not script.is_file():
            raise RuntimeError(f"RANK_SIZE_STAGE_MISSING:{node_index}:{size}")
        lines = stage_lines(node_dir, f"rank_size_{size}", gate)
        require_lines(lines, (
            f"RANK_SIZE={size}",
            "SUPPORT_REPLAY_FAILURES=0",
            "RANK_SIZE_CENSUS_COMPLETE=1",
        ), f"rank_size_{size}:{node_index}")
        census = json.loads(
            (node_dir / f"rank_size_{size}.support.json").read_text())
        if census.get("node") != node_index or census.get("size") != size:
            raise RuntimeError(f"RANK_CENSUS_SCOPE_DRIFT:{node_index}:{size}")
        if "RANK_SIZE_WITNESS_FOUND=1" in lines:
            rank = size
            break
        if "EVERY_MATCHABLE_MINOR_AT_SIZE_NF_ZERO=1" not in lines:
            raise RuntimeError(
                f"MISSING_ZERO_SIZE_CERTIFICATE:{node_index}:{size}")
    if rank < 0:
        raise RuntimeError(f"NO_RANK_WITNESS:{node_index}")
    rows, cols, delta = r5.read_witness(
        node_dir / f"NODE_{node_index:03d}_SIZE_{rank}_WITNESS.tsv", rank)
    delta_sha = sha256_text(delta)
    if delta_sha == DELTA_NODE1_SHA256 or delta_sha in generators_sha:
        raise RuntimeError(f"NODE_DELTA_ROUTE_GUARD:{node_index}")
    outcome.update({"rank": rank, "delta_sha256": delta_sha})
    saturation_lines = stage_lines(node_dir, "saturation", gate)
    if ("REVERSE_CONTAINMENT_WITNESS_SEARCH_EXHAUSTED_NO_VERDICT=1"
            in saturation_lines):
        require_lines(saturation_lines,
                      ("REVERSE_CONTAINMENT_SEARCH_BOUND=64",),
                      f"saturation:{node_index}")
        outcome["status"] = "REVERSE_EXHAUSTED"
        return outcome
    require_lines(saturation_lines, (
        "NODE_REDUCER_FIXTURES_PASS=1",
        "SATURATION_OBJECT_TYPE=list",
        "SATURATION_OBJECT_SIZE=1",
        "SATURATION_SLOT1_TYPE=ideal",
        "SATURATION_NODE_INCLUSION_FAILURES=0",
        "SATURATION_STABILITY_FAILURES=0",
        "REVERSE_CONTAINMENT_SEARCH_BOUND=64",
        "SATURATION_CERTIFICATE_COMPLETE=1",
        "OPEN_SATURATION_AND_CLOSED_SUCCESSOR_COMPLETE=1",
    ), f"saturation:{node_index}")
    if sum(line in saturation_lines for line in
           ("OPEN_CHART_EMPTY=0", "OPEN_CHART_EMPTY=1")) != 1:
        raise RuntimeError(f"OPEN_CHART_EMPTY_CENSUS:{node_index}")
    if sum(line in saturation_lines for line in
           ("NEXT_REMAINDER_EMPTY=0", "NEXT_REMAINDER_EMPTY=1")) != 1:
        raise RuntimeError(f"NEXT_REMAINDER_EMPTY_CENSUS:{node_index}")
    open_empty = "OPEN_CHART_EMPTY=1" in saturation_lines
    next_empty = "NEXT_REMAINDER_EMPTY=1" in saturation_lines
    certificate = r5.validate_empty_open_certificate(
        node_dir / f"NODE_{node_index:03d}_EMPTY_OPEN_POWER_CERTIFICATE.txt",
        open_empty)
    outcome.update({"open_chart_empty_by_saturation": open_empty,
                    "next_remainder_empty": next_empty,
                    "empty_open_power_certificate": certificate})
    if open_empty:
        require_lines(saturation_lines, (
            "EMPTY_OPEN_POWER_MEMBERSHIP_CERTIFICATE=1",
            "PROPER_OPEN_IDEAL_CERTIFICATE=0",
            "EMPTY_BRANCH_POWER_SEARCH_ENTERED=1",
            "REVERSE_CONTAINMENT_ENTERED=0",
        ), f"saturation-empty:{node_index}")
        outcome["status"] = "OPEN_EMPTY"
        return outcome
    require_lines(saturation_lines, (
        "EMPTY_OPEN_POWER_MEMBERSHIP_CERTIFICATE=0",
        "PROPER_OPEN_IDEAL_CERTIFICATE=1",
        "EMPTY_BRANCH_POWER_SEARCH_ENTERED=0",
        "REVERSE_CONTAINMENT_ENTERED=1",
    ), f"saturation-proper:{node_index}")
    basis_count = parse_exact_int(saturation_lines,
                                  "REVERSE_CONTAINMENT_BASIS_GENERATOR_COUNT")
    found_count = parse_exact_int(saturation_lines,
                                  "REVERSE_CONTAINMENT_WITNESS_FOUND_COUNT")
    reduction_count = parse_exact_int(
        saturation_lines, "REVERSE_CONTAINMENT_MEMBERSHIP_REDUCTION_COUNT")
    if (found_count != basis_count or basis_count < 1
            or not basis_count <= reduction_count <= 65 * basis_count):
        raise RuntimeError(f"REVERSE_CONTAINMENT_COUNTS:{node_index}")
    require_file_census(
        node_dir / f"NODE_{node_index:03d}_REVERSE_CONTAINMENT_ATTEMPTS.tsv",
        "basis_generator|exponent|normal_form", reduction_count)
    require_file_census(
        node_dir / f"NODE_{node_index:03d}_REVERSE_CONTAINMENT_WITNESSES.tsv",
        "basis_generator|found|exponent|normal_form", basis_count)
    free = 10 - rank
    chart_lines = stage_lines(node_dir, "chart", gate)
    require_lines(chart_lines, (
        "CHART_SATURATION_OBJECT_TYPE=list",
        "CHART_SATURATION_OBJECT_SIZE=1",
        "CHART_SATURATION_SLOT1_TYPE=ideal",
        "CHART_SATURATION_NODE_INCLUSION_FAILURES=0",
        "CHART_SATURATION_STABILITY_FAILURES=0",
        "CHART_OPEN_PROPER_IDEAL_CERTIFICATE=1",
        "OPEN_CHART_SATURATION_PROPER=1",
        "CHART_PIVOT_REDUCER=NODE_SB",
        "CHART_BASE_CHANGE_REDUCTION_COUNT=11135",
        "RESIDUAL_BASE_CHANGE_ENTRY_COUNT=110",
        "RIGHT_TRANSFORM_ENTRY_COUNT=11025",
        "RIGHT_TRANSFORM_RECORDED_ENTRY_COUNT=11025",
        "FULL_RIGHT_TRANSFORM_RECONSTRUCTED=1",
        "NODE_TRANSFORM_BASE_CHANGED_TO_ACTIVE_SB=1",
        "NF_RATIONAL_UNIT_PIVOT_COUNT=95",
        "NF_PIVOT_INVARIANT_FAILURES=0",
        f"ADJUGATE_KERNEL_VECTOR_COUNT={free}",
        "CHART_DELTA_NF_NONZERO=1",
        "SCANNED_DELTA_REPLAY_EQUAL=1",
        f"COMPLETE_BORDERED_IDENTITY_COUNT={11 * free}",
        "BORDERED_IDENTITY_FAILURES=0",
        "BORDERED_NONZERO_PLANT_NF_NONZERO=1",
        "BORDERED_NONZERO_PLANT_EQUALS_DELTA=1",
        f"FULL_106_ROW_KERNEL_REPLAY_COUNT={106 * free}",
        "FULL_106_ROW_KERNEL_REPLAY_FAILURES=0",
        f"LIFTED_KERNEL_ENTRY_COUNT={105 * free}",
        "ENDPOINT_PLUS_ONE_PLANT_AFFINE_REPLAY=1",
        "ENDPOINT_PLUS_TWO_PLANT_AFFINE_REPLAY=1",
        "ENDPOINT_TWO_SHIFT_AT_LEAST_ONE_NONZERO=1",
        "ENDPOINT_QUADRATIC=x14*x72+x1*x97",
        "ENDPOINT_DELTA2_DENOMINATOR_CLEARED=1",
        f"ENDPOINT_COEFFICIENT_COUNT={free * (free + 1) // 2}",
        "NO_FACTOR_GCD_CONTENT_RADICAL_NORMALIZATION=1",
        "RECURSIVE_ENDPOINT_CHART_COMPLETE=1",
    ), f"chart:{node_index}")
    prefix = f"NODE_{node_index:03d}"
    require_file_census(node_dir / f"{prefix}_CHART_PIVOTS.tsv",
                        "step|source_row|source_col|pivot", 95)
    require_exact_match(node_dir / f"{prefix}_CHART_PIVOTS.tsv",
                        node_dir / f"{prefix}_REDUCE_PIVOTS.tsv",
                        f"chart-pivots:{node_index}")
    require_file_census(node_dir / f"{prefix}_CHART_RESIDUAL.tsv",
                        "rows|11|cols|10", 110)
    require_exact_match(node_dir / f"{prefix}_CHART_RESIDUAL.tsv",
                        node_dir / f"{prefix}_REDUCE_RESIDUAL.tsv",
                        f"chart-residual:{node_index}")
    require_file_census(node_dir / f"{prefix}_CHART_BASE_CHANGED_RESIDUAL.tsv",
                        "rows|11|cols|10", 110)
    require_file_census(node_dir / f"{prefix}_BASE_CHANGED_RIGHT_TRANSFORM.tsv",
                        "row|col|normal_form", 11025)
    require_file_census(node_dir / f"{prefix}_BORDERED_IDENTITIES.tsv",
                        "basis|free_col|residual_row|normal_form", 11 * free)
    require_file_census(node_dir / f"{prefix}_ADJUGATE_KERNEL_105.tsv",
                        "coordinate|basis|normal_form", 105 * free)
    require_file_census(node_dir / f"{prefix}_ENDPOINT_DELTA2_CLEARED_NF.tsv",
                        "basis_i|basis_j|normal_form",
                        free * (free + 1) // 2)
    for name in (f"{prefix}_ENDPOINT_TWO_SHIFT_PLANT.txt",
                 f"{prefix}_BORDERED_NONZERO_PLANT.txt",
                 f"{prefix}_CHART_DELTA.txt"):
        if not (node_dir / name).is_file():
            raise RuntimeError(f"CHART_ARTIFACT_MISSING:{node_index}:{name}")
    require_exact_match(
        node_dir / f"{prefix}_CHART_ACTIVE_STANDARD_BASIS.txt",
        node_dir / f"{prefix}_OPEN_SAT_STANDARD_BASIS.txt",
        f"active-sb:{node_index}")
    chart_delta = "".join((node_dir / f"{prefix}_CHART_DELTA.txt")
                          .read_text().split())
    if not chart_delta or sha256_text(chart_delta) == DELTA_NODE1_SHA256:
        raise RuntimeError(f"CHART_DELTA_ROUTE_GUARD:{node_index}")
    endpoint_nonzero = parse_exact_int(
        chart_lines, "ENDPOINT_COEFFICIENT_NF_NONZERO_COUNT")
    if not 0 <= endpoint_nonzero <= free * (free + 1) // 2:
        raise RuntimeError(f"ENDPOINT_NONZERO_RANGE:{node_index}")
    dead_marker = "CHART_CLASSIFICATION=ENDPOINT_DEAD_ONLY_ON_D_DELTA"
    survivor_marker = ("CHART_CLASSIFICATION=RING_LEVEL_SURVIVOR_ON_CHART_"
                       "PENDING_NILPOTENCE_RADICAL")
    if chart_lines.count(dead_marker) + chart_lines.count(survivor_marker) != 1:
        raise RuntimeError(f"CHART_CLASSIFICATION_CENSUS:{node_index}")
    if endpoint_nonzero == 0 and dead_marker in chart_lines:
        outcome["status"] = "CHART_DEAD"
    elif endpoint_nonzero > 0 and survivor_marker in chart_lines:
        outcome["status"] = "CHART_SURVIVOR"
    else:
        raise RuntimeError(f"ENDPOINT_COUNT_CLASSIFICATION:{node_index}")
    outcome["endpoint_coefficient_nf_nonzero_count"] = endpoint_nonzero
    return outcome


def classify(production: Path, prepared: Path, build: Path, r5,
             gate) -> dict[str, object]:
    resume_input = json.loads((build / "RESUME_NODE_INPUT.json").read_text())
    if (tuple(resume_input.get("generator_sha256", []))
            != NODE2_GENERATOR_SHA256
            or resume_input.get("inherited_rank_upper_bound") != 6):
        raise RuntimeError("RESUME_NODE_INPUT_DRIFT")
    driver_summary = json.loads((production / "SUMMARY.json").read_text())
    driver_verdict = (production / "VERDICT.txt").read_text().strip()
    if driver_summary.get("classification") != driver_verdict:
        raise RuntimeError("DRIVER_SUMMARY_VERDICT_DISAGREEMENT")
    if driver_verdict not in ALLOWED:
        raise RuntimeError(f"DRIVER_VERDICT_NOT_ALLOWED:{driver_verdict}")
    for key, expected in (
            ("component", "triple02"),
            ("start_node", 2),
            ("closed_successor_of_node", 1),
            ("settled_open_route", "NEVER_REENTERED"),
            ("delta_node1_sha256", DELTA_NODE1_SHA256),
            ("no_radical_nilpotence_or_geometric_inference", True),
            ("whole_component_or_jc2_inference", False)):
        if driver_summary.get(key) != expected:
            raise RuntimeError(f"DRIVER_SUMMARY_SCOPE_DRIFT:{key}")
    witness_payload = classify_witness_replay(production, prepared, build, gate)
    node_dirs = sorted(item for item in production.iterdir()
                       if item.is_dir() and item.name.startswith("node_"))
    if any(item.name == "node_001" for item in node_dirs):
        raise RuntimeError("SETTLED_NODE1_DIRECTORY_PRESENT")
    expected_names = [f"node_{index:03d}"
                      for index in range(2, 2 + len(node_dirs))]
    if [item.name for item in node_dirs] != expected_names:
        raise RuntimeError("NODE_DIRECTORY_NUMBERING_DRIFT")
    reason = driver_summary.get("no_verdict_reason")
    timeout_node: object = None
    timeout_stage: str | None = None
    if isinstance(reason, str) and reason.startswith("STAGE_TIMEOUT:"):
        _, timeout_node_text, timeout_stage = reason.split(":", 2)
        timeout_node = (int(timeout_node_text)
                        if timeout_node_text.isdigit() else timeout_node_text)
    generators_sha = list(NODE2_GENERATOR_SHA256)
    rank_bound = 6
    outcomes: list[dict[str, object]] = []
    derived: str | None = None
    for node_dir in node_dirs:
        node_index = int(node_dir.name.split("_")[1])
        this_timeout = (timeout_stage
                        if timeout_node == node_index else None)
        outcome = classify_node(node_dir, node_index, generators_sha,
                                rank_bound, r5, gate, this_timeout)
        outcomes.append(outcome)
        status = outcome["status"]
        if status == "STAGE_TIMEOUT":
            derived = CLASS_NO_VERDICT
            break
        if status == "EXACT_EMPTY_NODE":
            derived = CLASS_DEAD
            break
        if status == "REVERSE_EXHAUSTED":
            derived = CLASS_REVERSE
            break
        if status == "CHART_SURVIVOR":
            derived = CLASS_SURVIVOR
            break
        if status in ("OPEN_EMPTY", "CHART_DEAD"):
            if outcome["next_remainder_empty"]:
                derived = CLASS_DEAD
                break
            generators_sha = generators_sha + [outcome["delta_sha256"]]
            rank_bound = outcome["rank"]
            continue
        raise RuntimeError(f"UNKNOWN_NODE_STATUS:{status}")
    if derived is None:
        if not (isinstance(reason, str)
                and reason.startswith("MAX_NODES_EXHAUSTED:")):
            raise RuntimeError("LOOP_ENDED_WITHOUT_TERMINAL_OR_EXHAUSTION")
        derived = CLASS_NO_VERDICT
    if (timeout_stage is not None and outcomes
            and outcomes[-1].get("status") != "STAGE_TIMEOUT"):
        raise RuntimeError("TIMEOUT_REASON_WITHOUT_TIMED_OUT_FINAL_NODE")
    if derived != driver_verdict:
        raise RuntimeError(
            f"CLASSIFIER_DRIVER_DISAGREEMENT:{derived}:{driver_verdict}")
    if (derived == CLASS_DEAD
            and any(outcome.get("status") == "CHART_SURVIVOR"
                    for outcome in outcomes)):
        raise RuntimeError("DEAD_VERDICT_WITH_SURVIVOR_NODE")
    return {
        "classification": derived,
        "closed_successor_of_node": 1,
        "component": "triple02",
        "endpoint_quadratic": "x14*x72+x1*x97",
        "final_rank_upper_bound": rank_bound,
        "node_outcomes": outcomes,
        "nodes_processed": len(outcomes),
        "scope": ("TRIPLE02_NODE1_CLOSED_SUCCESSOR_FINITE_CHART_"
                  "RECURSION_ONLY"),
        "settled_open_route_reentered": False,
        "start_node": 2,
        "whole_component_or_jc2_inference": False,
        **witness_payload,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--production", required=True, type=Path)
    parser.add_argument("--prepared", required=True, type=Path)
    parser.add_argument("--build", required=True, type=Path)
    parser.add_argument("--frozen-r5-source", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    r5 = load_pinned("frozen_r5_recursor", args.frozen_r5_source.resolve(),
                     FROZEN_R5_SHA256, with_parent_path=True)
    gate = load_pinned(
        "frozen_transcript_gate",
        args.frozen_r5_source.resolve().parent / "transcript_gate.py",
        TRANSCRIPT_GATE_SHA256)
    payload = classify(args.production.resolve(), args.prepared.resolve(),
                       args.build.resolve(), r5, gate)
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    (output / "SUMMARY.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n")
    (output / "VERDICT.txt").write_text(str(payload["classification"]) + "\n")
    print(f"CLASSIFICATION={payload['classification']}")
    print("TRIPLE02_CLOSED_SUCCESSOR_CLASSIFIER_PASS=1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
