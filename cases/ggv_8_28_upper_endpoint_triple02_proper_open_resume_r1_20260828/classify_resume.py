#!/usr/bin/env python3
"""Fail-closed classifier for the TRIPLE02 proper-open endpoint chart."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


TRANSCRIPT_GATE_SHA256 = "0e0efd5ada59039a373a731038f2f88a3794b376b208879c2459bff97d0e7316"
PREFIX_STDOUT_SHA256 = "4ee63095327d80572764eb3783d0e77c7a6cf385f47cf93c1cafcea843b29418"
REQUIRED_LINES = (
    "NODE_INDEX=1",
    "NODE_GENERATOR_COUNT=2",
    "NODE_EMPTY=0",
    "NODE_REDUCER_FIXTURES_PASS=1",
    f"ARCHIVED_SATURATION_PREFIX_STDOUT_SHA256={PREFIX_STDOUT_SHA256}",
    "ARCHIVED_SATURATION_PREFIX_BOUND=1",
    "ARCHIVED_SATURATION_OBJECT_TYPE=list",
    "ARCHIVED_SATURATION_OBJECT_SIZE=1",
    "ARCHIVED_SATURATION_SLOT1_TYPE=ideal",
    "ARCHIVED_SATURATION_STABILITY_FAILURES=0",
    "ARCHIVED_SATURATION_RESULT_USED_AS_PROVENANCE_ONLY=1",
    "RESUME_STABILITY_OBJECT_TYPE=list",
    "RESUME_STABILITY_OBJECT_SIZE=1",
    "RESUME_STABILITY_SLOT1_TYPE=ideal",
    "RESUME_NODE_INCLUSION_FAILURES=0",
    "RESUME_OPEN_BASIS_REPLAY_FAILURES=0",
    "RESUME_CANDIDATE_STABILITY_FAILURES=0",
    "RESUME_ACTIVE_UNIT_NF_NONZERO=1",
    "RESUME_DELTA_NF_NONZERO=1",
    "REVERSE_CONTAINMENT_BASIS_GENERATOR_COUNT=2",
    "REVERSE_CONTAINMENT_WITNESS_FOUND_COUNT=2",
    "REVERSE_CONTAINMENT_SEARCH_BOUND=64",
    "SELF_CONTAINED_TWO_CONTAINMENT_SATURATION_CERTIFICATE=1",
    "PROPER_OPEN_IDEAL_CERTIFICATE=1",
    "NODE_SATURATION_RECOMPUTATION_ENTERED=0",
    "CANDIDATE_STABILITY_SATURATION_ENTERED=1",
    "PURE_DELTA_POWER_SEARCH_ENTERED=0",
    "CLOSED_SUCCESSOR_ENTERED=0",
    "PROPER_OPEN_ROUTING_PASS=1",
    "RING_ORDER=Q[q0,q2,c4,c6]_dp",
    "C4_SOURCE_TOKEN_CENSUS=30",
    "INHERITED_RANK_UPPER_BOUND=6",
    "INHERITED_RANK_CERTIFICATE_ARCHIVE_SHA256=b947a2d3e81525902a93500026020c2cf9580f070767757389daadb9a6bbe3b2",
    "INHERITED_RANK_CERTIFICATE_MEMBER_SHA256=cc6dc1c4edbceeecf31c17b96ab9a0ac9744720100e7bf3f20ba41c4e4cd99d2",
    "INHERITED_RANK_CERTIFICATE_BOUND=1",
    "SELECTED_MINOR_ROWS=1,2,4,7,9,11",
    "SELECTED_MINOR_COLS=1,2,3,5,6,7",
    "SELECTED_MINOR_LITERAL_SHA256=84b4c2c4c0bfe5aa7414c35813cc1cf63d7d5416358a394b8e8bdc35820f1d02",
    "CHART_PIVOT_REDUCER=NODE_SB",
    "CHART_BASE_CHANGE_REDUCTION_COUNT=11135",
    "RESIDUAL_BASE_CHANGE_ENTRY_COUNT=110",
    "RIGHT_TRANSFORM_ENTRY_COUNT=11025",
    "RIGHT_TRANSFORM_RECORDED_ENTRY_COUNT=11025",
    "FULL_RIGHT_TRANSFORM_RECONSTRUCTED=1",
    "NODE_TRANSFORM_BASE_CHANGED_TO_ACTIVE_SB=1",
    "NF_RATIONAL_UNIT_PIVOT_COUNT=95",
    "NF_PIVOT_INVARIANT_FAILURES=0",
    "ADJUGATE_KERNEL_VECTOR_COUNT=4",
    "CHART_DELTA_NF_NONZERO=1",
    "SCANNED_DELTA_REPLAY_EQUAL=1",
    "COMPLETE_BORDERED_IDENTITY_COUNT=44",
    "BORDERED_IDENTITY_FAILURES=0",
    "BORDERED_NONZERO_PLANT_NF_NONZERO=1",
    "BORDERED_NONZERO_PLANT_EQUALS_DELTA=1",
    "FULL_106_ROW_KERNEL_REPLAY_COUNT=424",
    "FULL_106_ROW_KERNEL_REPLAY_FAILURES=0",
    "LIFTED_KERNEL_ENTRY_COUNT=420",
    "ENDPOINT_PLUS_ONE_PLANT_AFFINE_REPLAY=1",
    "ENDPOINT_PLUS_TWO_PLANT_AFFINE_REPLAY=1",
    "ENDPOINT_TWO_SHIFT_AT_LEAST_ONE_NONZERO=1",
    "ENDPOINT_QUADRATIC=x14*x72+x1*x97",
    "ENDPOINT_DELTA2_DENOMINATOR_CLEARED=1",
    "ENDPOINT_COEFFICIENT_COUNT=10",
    "NO_FACTOR_GCD_CONTENT_RADICAL_NORMALIZATION=1",
    "RECURSIVE_ENDPOINT_CHART_COMPLETE=1",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_gate(path: Path):
    if sha256(path) != TRANSCRIPT_GATE_SHA256:
        raise SystemExit("TRANSCRIPT_GATE_SHA_DRIFT")
    spec = importlib.util.spec_from_file_location("frozen_transcript_gate", path)
    if spec is None or spec.loader is None:
        raise SystemExit("TRANSCRIPT_GATE_IMPORT_FAILURE")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


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
    actual_bytes = actual.read_bytes()
    expected_bytes = expected.read_bytes()
    if actual_bytes != expected_bytes:
        raise RuntimeError(f"EXACT_ARCHIVED_REPLAY_DISAGREEMENT:{label}")
    return hashlib.sha256(actual_bytes).hexdigest()


def classify(stdout: Path, stderr: Path, result: Path, script: Path,
             transcript_gate: Path, artifact_root: Path,
             archived_pivots: Path, archived_residual: Path) -> dict[str, object]:
    gate = load_gate(transcript_gate)
    gate.assert_clean_transcript(stdout, stderr)
    result_payload = json.loads(result.read_text())
    if (result_payload.get("timed_out") is not False
            or result_payload.get("returncode") != 0
            or result_payload.get("stdout_sha256") != sha256(stdout)
            or result_payload.get("stderr_sha256") != sha256(stderr)
            or result_payload.get("script_sha256") != sha256(script)):
        raise RuntimeError("PRODUCTION_RESULT_CUSTODY_DISAGREEMENT")
    lines = stdout.read_text(errors="strict").splitlines()
    if any(line.startswith("FATAL_") for line in lines):
        raise RuntimeError("FATAL_MARKER_IN_PRODUCTION_STDOUT")
    for required in REQUIRED_LINES:
        if lines.count(required) != 1:
            raise RuntimeError(f"REQUIRED_MARKER_CENSUS:{required}:{lines.count(required)}")
    forbidden_true = (
        "NODE_SATURATION_RECOMPUTATION_ENTERED=1",
        "PURE_DELTA_POWER_SEARCH_ENTERED=1",
        "CLOSED_SUCCESSOR_ENTERED=1",
    )
    if any(marker in lines for marker in forbidden_true):
        raise RuntimeError("FORBIDDEN_PROPER_ROUTE_MARKER")
    endpoint_nonzero = parse_exact_int(lines, "ENDPOINT_COEFFICIENT_NF_NONZERO_COUNT")
    reverse_reductions = parse_exact_int(
        lines, "REVERSE_CONTAINMENT_MEMBERSHIP_REDUCTION_COUNT")
    if not 2 <= reverse_reductions <= 130:
        raise RuntimeError("REVERSE_CONTAINMENT_REDUCTION_COUNT_RANGE")
    plus_one_nonzero = parse_exact_int(lines, "ENDPOINT_PLUS_ONE_PLANT_NF_NONZERO")
    plus_two_nonzero = parse_exact_int(lines, "ENDPOINT_PLUS_TWO_PLANT_NF_NONZERO")
    if (plus_one_nonzero not in (0, 1) or plus_two_nonzero not in (0, 1)
            or plus_one_nonzero + plus_two_nonzero < 1):
        raise RuntimeError("ENDPOINT_TWO_SHIFT_BOOLEAN_DISAGREEMENT")
    if not 0 <= endpoint_nonzero <= 10:
        raise RuntimeError("ENDPOINT_NONZERO_COUNT_RANGE")
    dead_marker = "CHART_CLASSIFICATION=ENDPOINT_DEAD_ONLY_ON_D_DELTA"
    survivor_marker = (
        "CHART_CLASSIFICATION="
        "RING_LEVEL_SURVIVOR_ON_CHART_PENDING_NILPOTENCE_RADICAL")
    if lines.count(dead_marker) + lines.count(survivor_marker) != 1:
        raise RuntimeError("ENDPOINT_CLASSIFICATION_MARKER_CENSUS")
    if endpoint_nonzero == 0 and lines.count(dead_marker) == 1:
        classification = "EXACT_ENDPOINT_DEAD_ON_NODE1_PROPER_OPEN_ONLY"
    elif endpoint_nonzero > 0 and lines.count(survivor_marker) == 1:
        classification = (
            "RING_LEVEL_ENDPOINT_NONZERO_ON_NODE1_PROPER_OPEN_"
            "PENDING_NILPOTENCE_RADICAL")
    else:
        raise RuntimeError("ENDPOINT_COUNT_CLASSIFICATION_DISAGREEMENT")
    artifact_hashes = {
        "active_standard_basis": sha256(
            artifact_root / "NODE_001_RESUMED_ACTIVE_STANDARD_BASIS.txt"),
        "chart_delta": sha256(artifact_root / "NODE_001_CHART_DELTA.txt"),
        "endpoint_two_shift_plant": sha256(
            artifact_root / "NODE_001_ENDPOINT_TWO_SHIFT_PLANT.txt"),
        "bordered_nonzero_plant": sha256(
            artifact_root / "NODE_001_BORDERED_NONZERO_PLANT.txt"),
        "pivot_log": require_file_census(
            artifact_root / "NODE_001_CHART_PIVOTS.tsv",
            "step|source_row|source_col|pivot", 95),
        "pivot_log_exact_archived_replay": require_exact_match(
            artifact_root / "NODE_001_CHART_PIVOTS.tsv",
            archived_pivots, "pivot-log"),
        "node_residual_exact_archived_replay": require_exact_match(
            artifact_root / "NODE_001_CHART_RESIDUAL.tsv",
            archived_residual, "node-residual"),
        "base_changed_residual": require_file_census(
            artifact_root / "NODE_001_CHART_BASE_CHANGED_RESIDUAL.tsv",
            "rows|11|cols|10", 110),
        "base_changed_right_transform": require_file_census(
            artifact_root / "NODE_001_BASE_CHANGED_RIGHT_TRANSFORM.tsv",
            "row|col|normal_form", 11025),
        "bordered_identities": require_file_census(
            artifact_root / "NODE_001_BORDERED_IDENTITIES.tsv",
            "basis|free_col|residual_row|normal_form", 44),
        "kernel_105": require_file_census(
            artifact_root / "NODE_001_ADJUGATE_KERNEL_105.tsv",
            "coordinate|basis|normal_form", 420),
        "endpoint_coefficients": require_file_census(
            artifact_root / "NODE_001_ENDPOINT_DELTA2_CLEARED_NF.tsv",
            "basis_i|basis_j|normal_form", 10),
        "reverse_containment_attempts": require_file_census(
            artifact_root / "NODE_001_REVERSE_CONTAINMENT_ATTEMPTS.tsv",
            "basis_generator|exponent|normal_form", reverse_reductions),
        "reverse_containment_witnesses": require_file_census(
            artifact_root / "NODE_001_REVERSE_CONTAINMENT_WITNESSES.tsv",
            "basis_generator|found|exponent|normal_form", 2),
    }
    return {
        "artifact_sha256": artifact_hashes,
        "classification": classification,
        "endpoint_coefficient_nf_nonzero_count": endpoint_nonzero,
        "endpoint_quadratic": "x14*x72+x1*x97",
        "frozen_prefix_stdout_sha256": PREFIX_STDOUT_SHA256,
        "node": 1,
        "proper_open_only": True,
        "saturation_certificate": "SELF_CONTAINED_TWO_CONTAINMENT",
        "scope": "TRIPLE02_NODE1_D_DELTA_ONLY",
        "whole_component_or_closed_successor_inference": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stdout", required=True, type=Path)
    parser.add_argument("--stderr", required=True, type=Path)
    parser.add_argument("--result", required=True, type=Path)
    parser.add_argument("--script", required=True, type=Path)
    parser.add_argument("--transcript-gate", required=True, type=Path)
    parser.add_argument("--artifact-root", required=True, type=Path)
    parser.add_argument("--archived-pivots", required=True, type=Path)
    parser.add_argument("--archived-residual", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    payload = classify(
        args.stdout.resolve(), args.stderr.resolve(), args.result.resolve(),
        args.script.resolve(), args.transcript_gate.resolve(),
        args.artifact_root.resolve(), args.archived_pivots.resolve(),
        args.archived_residual.resolve())
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    (output / "SUMMARY.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n")
    (output / "VERDICT.txt").write_text(str(payload["classification"]) + "\n")
    print(f"CLASSIFICATION={payload['classification']}")
    print("TRIPLE02_PROPER_OPEN_RESULT_CLASSIFIER_PASS=1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
