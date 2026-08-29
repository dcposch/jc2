#!/usr/bin/env python3
"""Light source/mutation/semantic preflight for the proper-open resume."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"MODULE_IMPORT_FAILURE:{name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def expect_validator_rejection(builder, script: str, expected: str) -> None:
    try:
        builder.validate_script(script)
    except RuntimeError as exc:
        if expected in str(exc):
            return
        raise SystemExit(f"WRONG_MUTATION_REJECTION:{expected}:{exc}") from exc
    raise SystemExit(f"MUTATION_NOT_REJECTED:{expected}")


def write_census(path: Path, header: str, records: int) -> None:
    path.write_text(header + "\n" + "\n".join(
        f"{index}|fixture" for index in range(1, records + 1)) + "\n")


def validate_adapter_source(text: str) -> None:
    required = (
        "ideal PROPER_I=x*y;",
        "ideal PROPER_B=y;",
        "int PROPER_PURE_POWER_REDUCTIONS=0;",
        "PROPER_REVERSE_REDUCTIONS!=2",
        "ideal BAD_B=y,x-1;",
        "BAD_FOUND_COUNT>=size(BAD_B)",
        "ideal EMPTY_I=x^3;",
        "EMPTY_FOUND_EXPONENT!=3",
        "EMPTY_POWER_REDUCTIONS!=4",
        "EMPTY_PRIOR_NONMEMBERS!=3",
        "ideal REDUCER_I=q2;",
        "REDUCER_ZERO_NF!=0",
        "INNOCENT_PLUS_ONE!=0 || INNOCENT_PLUS_TWO==0",
        "BORDERED_PLANT_NF==0",
        "SELFTEST_ENDPOINT_TWO_SHIFT_AT_LEAST_ONE_NONZERO=",
        "SELFTEST_BORDERED_PLANT_EQUALS_DELTA=",
        "TRIPLE02_PROPER_OPEN_ADAPTER_SELFCHECK_PASS=1",
    )
    missing = [token for token in required if text.count(token) != 1]
    if missing:
        raise RuntimeError("ADAPTER_SEMANTIC_CONTROL_CENSUS:" + ",".join(missing))
    if any(token in text for token in ("PLACEHOLDER", "TODO")):
        raise RuntimeError("ADAPTER_SEMANTIC_CONTROL_PLACEHOLDER")


def make_classifier_fixture(root: Path, classifier, script: Path,
                            dead: bool) -> tuple[Path, Path, Path, Path, Path, Path]:
    root.mkdir(parents=True, exist_ok=False)
    artifacts = root / "artifacts"
    artifacts.mkdir()
    for name, text in (
            ("NODE_001_RESUMED_ACTIVE_STANDARD_BASIS.txt", "x\n"),
            ("NODE_001_CHART_DELTA.txt", "x\n"),
            ("NODE_001_ENDPOINT_TWO_SHIFT_PLANT.txt", "plant\n"),
            ("NODE_001_BORDERED_NONZERO_PLANT.txt", "plant\n")):
        (artifacts / name).write_text(text)
    write_census(artifacts / "NODE_001_CHART_PIVOTS.tsv",
                 "step|source_row|source_col|pivot", 95)
    write_census(artifacts / "NODE_001_CHART_BASE_CHANGED_RESIDUAL.tsv",
                 "rows|11|cols|10", 110)
    write_census(artifacts / "NODE_001_CHART_RESIDUAL.tsv",
                 "rows|11|cols|10", 110)
    write_census(artifacts / "NODE_001_BASE_CHANGED_RIGHT_TRANSFORM.tsv",
                 "row|col|normal_form", 11025)
    write_census(artifacts / "NODE_001_BORDERED_IDENTITIES.tsv",
                 "basis|free_col|residual_row|normal_form", 44)
    write_census(artifacts / "NODE_001_ADJUGATE_KERNEL_105.tsv",
                 "coordinate|basis|normal_form", 420)
    write_census(artifacts / "NODE_001_ENDPOINT_DELTA2_CLEARED_NF.tsv",
                 "basis_i|basis_j|normal_form", 10)
    write_census(artifacts / "NODE_001_REVERSE_CONTAINMENT_ATTEMPTS.tsv",
                 "basis_generator|exponent|normal_form", 2)
    write_census(artifacts / "NODE_001_REVERSE_CONTAINMENT_WITNESSES.tsv",
                 "basis_generator|found|exponent|normal_form", 2)
    archived_pivots = root / "archived_pivots.tsv"
    archived_residual = root / "archived_residual.tsv"
    archived_pivots.write_bytes((artifacts / "NODE_001_CHART_PIVOTS.tsv").read_bytes())
    archived_residual.write_bytes((artifacts / "NODE_001_CHART_RESIDUAL.tsv").read_bytes())
    lines = list(classifier.REQUIRED_LINES)
    lines += [
        "REVERSE_CONTAINMENT_MEMBERSHIP_REDUCTION_COUNT=2",
        "ENDPOINT_PLUS_ONE_PLANT_NF_NONZERO=1",
        "ENDPOINT_PLUS_TWO_PLANT_NF_NONZERO=1",
    ]
    if dead:
        lines += [
            "ENDPOINT_COEFFICIENT_NF_NONZERO_COUNT=0",
            "CHART_CLASSIFICATION=ENDPOINT_DEAD_ONLY_ON_D_DELTA",
        ]
    else:
        lines += [
            "ENDPOINT_COEFFICIENT_NF_NONZERO_COUNT=1",
            "CHART_CLASSIFICATION="
            "RING_LEVEL_SURVIVOR_ON_CHART_PENDING_NILPOTENCE_RADICAL",
        ]
    stdout = root / "stdout.txt"
    stderr = root / "stderr.txt"
    result = root / "result.json"
    stdout.write_text("\n".join(lines) + "\n")
    stderr.write_text("")
    result.write_text(json.dumps({
        "returncode": 0,
        "timed_out": False,
        "script_sha256": sha256(script),
        "stdout_sha256": sha256(stdout),
        "stderr_sha256": sha256(stderr),
    }, sort_keys=True) + "\n")
    return stdout, stderr, result, artifacts, archived_pivots, archived_residual


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--preparer", required=True, type=Path)
    parser.add_argument("--frozen-archive", required=True, type=Path)
    parser.add_argument("--builder", required=True, type=Path)
    parser.add_argument("--classifier", required=True, type=Path)
    parser.add_argument("--adapter-selfcheck", required=True, type=Path)
    parser.add_argument("--transcript-gate", required=True, type=Path)
    parser.add_argument("--script", required=True, type=Path)
    parser.add_argument("--fixture-root", required=True, type=Path)
    args = parser.parse_args()
    preparer = load("resume_preparer", args.preparer.resolve())
    builder = load("resume_builder", args.builder.resolve())
    classifier = load("resume_classifier", args.classifier.resolve())
    adapter_source = args.adapter_selfcheck.resolve().read_text()
    validate_adapter_source(adapter_source)
    for anchor in ("ideal BAD_B=y,x-1;", "BORDERED_PLANT_NF==0"):
        rejected = False
        try:
            validate_adapter_source(adapter_source.replace(anchor, "", 1))
        except RuntimeError as exc:
            rejected = "ADAPTER_SEMANTIC_CONTROL_CENSUS" in str(exc)
        if not rejected:
            raise SystemExit(f"ADAPTER_CONTROL_MUTATION_NOT_REJECTED:{anchor}")
    script_path = args.script.resolve()
    script = script_path.read_text()
    builder.validate_script(script)
    if preparer.verify_archive_sha(args.frozen_archive.resolve()) != preparer.ARCHIVE_SHA256:
        raise SystemExit("FROZEN_ARCHIVE_POSITIVE_CONTROL_FAILURE")
    tampered_archive = args.fixture_root.resolve().parent / "tampered_archive.bin"
    tampered_archive.parent.mkdir(parents=True, exist_ok=True)
    tampered_archive.write_bytes(b"not-the-frozen-archive")
    archive_hash_mutation_rejected = False
    try:
        preparer.verify_archive_sha(tampered_archive)
    except RuntimeError as exc:
        archive_hash_mutation_rejected = "FROZEN_ARCHIVE_SHA_DRIFT" in str(exc)
    if not archive_hash_mutation_rejected:
        raise SystemExit("ARCHIVE_HASH_MUTATION_NOT_REJECTED")
    unsafe_member_rejected = False
    try:
        preparer.safe_relative("../output/node_001/NODE_INPUT.json")
    except SystemExit as exc:
        unsafe_member_rejected = "UNSAFE_ARCHIVE_MEMBER" in str(exc)
    if (not unsafe_member_rejected
            or preparer.selected("output/node_001/NODE_INPUT.json.mutated")
            or not preparer.selected("output/node_001/NODE_INPUT.json")):
        raise SystemExit("EXACT_MEMBER_SELECTION_MUTATION_NOT_REJECTED")
    expect_validator_rejection(
        builder, script + "\nlist BAD=sat(NODE_IDEAL,ideal(DELTA));\n",
        "FORBIDDEN_PROPER_OPEN_ROUTE_TOKEN")
    expect_validator_rejection(
        builder, script.replace("PURE_DELTA_POWER_SEARCH_ENTERED=0",
                                "PURE_DELTA_POWER_SEARCH_ENTERED=1"),
        "REQUIRED_RESUME_TOKEN_CENSUS")
    expect_validator_rejection(
        builder, script.replace("CLOSED_SUCCESSOR_ENTERED=0",
                                "CLOSED_SUCCESSOR_ENTERED=1"),
        "REQUIRED_RESUME_TOKEN_CENSUS")
    expect_validator_rejection(
        builder, script.replace(builder.RING_DECLARATION,
                                "ring ambient=0,(q2,q0,c4,c6),dp;"),
        "RING_DECLARATION_OR_ORDER_CENSUS")
    delta_line = next(line for line in script.splitlines()
                      if line.startswith("poly SCANNED_DELTA_NODE="))
    expect_validator_rejection(
        builder, script.replace(delta_line, delta_line[:-1] + "+1;"),
        "SELECTED_DELTA_LITERAL_OR_HASH_DRIFT")
    if "(-1)*c4+(5/128)*q0" not in script:
        raise SystemExit("C4_MATRIX_TERM_CONTROL_ANCHOR_MISSING")
    expect_validator_rejection(
        builder, script.replace("(-1)*c4+(5/128)*q0", "(5/128)*q0", 1),
        "C4_SOURCE_TOKEN_CENSUS_DRIFT")
    expect_validator_rejection(
        builder, script.replace("ARCHIVED_SATURATION_PREFIX_BOUND=1",
                                "ARCHIVED_SATURATION_PREFIX_BOUND_REMOVED=1"),
        "REQUIRED_RESUME_TOKEN_CENSUS")
    expect_validator_rejection(
        builder, script.replace("CHART_PIVOT_REDUCER=NODE_SB",
                                "CHART_PIVOT_REDUCER=ACTIVE_SB"),
        "REQUIRED_RESUME_TOKEN_CENSUS")
    expect_validator_rejection(
        builder, script.replace("ENDPOINT_PLUS_ONE_PLANT_NF_NONZERO=",
                                "ENDPOINT_PLUS_ONE_PLANT_REMOVED="),
        "REQUIRED_RESUME_TOKEN_CENSUS")
    expect_validator_rejection(
        builder, script.replace(builder.ENDPOINT_CROSS_EXPRESSION,
                                "K[14,i]*K[72,j]", 1),
        "ENDPOINT_CROSS_TERM_CENSUS")
    transform_mutations = (
        ("for(i=1;i<=105;i=i+1){ C[i,i]=1; }",
         "for(i=1;i<=105;i=i+1){ C[i,i]=0; }"),
        ("swap_entry=C[i,step]; C[i,step]=C[i,pj]; C[i,pj]=swap_entry;",
         "swap_entry=C[i,step]; C[i,step]=C[i,pj]; C[i,pj]=0;"),
        ("C[i,j]=reduce(C[i,j]-multiple*C[i,step],NODE_SB)",
         "C[i,j]=reduce(C[i,j]+multiple*C[i,step],NODE_SB)"),
        ("C[i,j]=reduce(C[i,j],ACTIVE_SB)",
         "C[i,j]=0"),
        ('write(CTFILE,string(i)+"|"+string(j)+"|"+string(C[i,j]))',
         'write(CTFILE,string(i)+"|"+string(j)+"|"+string(0))'),
    )
    for anchor, mutation in transform_mutations:
        if script.count(anchor) != 1:
            raise SystemExit("RIGHT_TRANSFORM_MUTATION_ANCHOR_CENSUS:" + anchor)
        expect_validator_rejection(
            builder, script.replace(anchor, mutation, 1),
            "FULL_RIGHT_TRANSFORM_CONTRACT_CENSUS")
    for token in (
            "base_change_reductions!=11135",
            "residual_base_change_entry_count!=110",
            "transform_entry_count!=11025",
            "transform_recorded_entry_count!=11025",
            "identity_count!=44",
            "kernel_entry_count!=420",
            "full_count!=424",
            "endpoint_count!=10",
            "ncols(Y)!=4"):
        expect_validator_rejection(
            builder, script.replace(token, token.replace("!=", "=="), 1),
            "EXACT_OPERATION_COUNT_GATE_CENSUS")
    expect_validator_rejection(
        builder, script.replace(builder.OPEN_BASIS_TEXT,
                                builder.OPEN_BASIS_TEXT + "+q0"),
        "ARCHIVED_OPEN_BASIS_LITERAL_OR_HASH_DRIFT")
    fixture_root = args.fixture_root.resolve()
    dead = make_classifier_fixture(fixture_root / "dead", classifier,
                                   script_path, True)
    dead_payload = classifier.classify(
        *dead[:3], script_path, args.transcript_gate.resolve(), dead[3],
        dead[4], dead[5])
    if dead_payload["classification"] != (
            "EXACT_ENDPOINT_DEAD_ON_NODE1_PROPER_OPEN_ONLY"):
        raise SystemExit("DEAD_CLASSIFIER_CONTROL_DISAGREEMENT")
    survivor = make_classifier_fixture(fixture_root / "survivor", classifier,
                                       script_path, False)
    survivor_payload = classifier.classify(
        *survivor[:3], script_path, args.transcript_gate.resolve(), survivor[3],
        survivor[4], survivor[5])
    if survivor_payload["classification"] != (
            "RING_LEVEL_ENDPOINT_NONZERO_ON_NODE1_PROPER_OPEN_"
            "PENDING_NILPOTENCE_RADICAL"):
        raise SystemExit("SURVIVOR_CLASSIFIER_CONTROL_DISAGREEMENT")
    original = dead[0].read_text()
    dead[0].write_text(original.replace(
        "ENDPOINT_PLUS_ONE_PLANT_NF_NONZERO=1\n", ""))
    payload = json.loads(dead[2].read_text())
    payload["stdout_sha256"] = sha256(dead[0])
    dead[2].write_text(json.dumps(payload, sort_keys=True) + "\n")
    missing_plant_rejected = False
    try:
        classifier.classify(
            *dead[:3], script_path, args.transcript_gate.resolve(), dead[3],
            dead[4], dead[5])
    except RuntimeError as exc:
        missing_plant_rejected = (
            "REQUIRED_MARKER_CENSUS" in str(exc)
            or "INTEGER_MARKER_CENSUS" in str(exc))
    if not missing_plant_rejected:
        raise SystemExit("MISSING_ENDPOINT_PLANT_NOT_REJECTED")
    dead[0].write_text(original)
    payload = json.loads(dead[2].read_text())
    payload["stdout_sha256"] = sha256(dead[0])
    dead[2].write_text(json.dumps(payload, sort_keys=True) + "\n")
    residual_path = dead[3] / "NODE_001_CHART_RESIDUAL.tsv"
    residual_original = residual_path.read_text()
    residual_path.write_text(residual_original.replace("1|fixture", "1|tampered", 1))
    residual_mutation_rejected = False
    try:
        classifier.classify(
            *dead[:3], script_path, args.transcript_gate.resolve(), dead[3],
            dead[4], dead[5])
    except RuntimeError as exc:
        residual_mutation_rejected = "EXACT_ARCHIVED_REPLAY_DISAGREEMENT" in str(exc)
    if not residual_mutation_rejected:
        raise SystemExit("RESIDUAL_ENTRY_MUTATION_NOT_REJECTED")
    hostile_stdout = fixture_root / "hostile.stdout.txt"
    hostile_stderr = fixture_root / "hostile.stderr.txt"
    hostile_stdout.write_text("   ? wrong range[2] in list _(1)\n")
    hostile_stderr.write_text("")
    gate = classifier.load_gate(args.transcript_gate.resolve())
    diagnostic_rejected = False
    try:
        gate.assert_clean_transcript(hostile_stdout, hostile_stderr)
    except RuntimeError as exc:
        diagnostic_rejected = "SINGULAR_DIAGNOSTIC_WITH_ANY_RETURN_CODE" in str(exc)
    if not diagnostic_rejected:
        raise SystemExit("DIAGNOSTIC_CONTROL_NOT_REJECTED")
    print(f"GENERATED_SCRIPT_SHA256={hashlib.sha256(script.encode()).hexdigest()}")
    print("PROPER_ROUTE_SATURATION_MUTATION_REJECTED=1")
    print("PROPER_ROUTE_EMPTY_SEARCH_MUTATION_REJECTED=1")
    print("PROPER_ROUTE_CLOSED_SUCCESSOR_MUTATION_REJECTED=1")
    print("ARCHIVED_PREFIX_BINDING_MUTATION_REJECTED=1")
    print("FROZEN_ARCHIVE_HASH_MUTATION_REJECTED=1")
    print("EXACT_MEMBER_SELECTION_MUTATION_REJECTED=1")
    print("ACTIVE_REPIVOT_MUTATION_REJECTED=1")
    print("ARCHIVED_OPEN_BASIS_MUTATION_REJECTED=1")
    print("RING_ORDER_MUTATION_REJECTED=1")
    print("SELECTED_DELTA_MUTATION_REJECTED=1")
    print("C4_MATRIX_TERM_DELETION_REJECTED=1")
    print("RIGHT_TRANSFORM_C_ENTRY_MUTATIONS_REJECTED=5")
    print("EXACT_COUNT_MUTATIONS_REJECTED=9")
    print("ENDPOINT_CROSS_TERM_MUTATION_REJECTED=1")
    print("ARCHIVED_RESIDUAL_ENTRY_MUTATION_REJECTED=1")
    print("ENDPOINT_PLANT_MUTATION_REJECTED=1")
    print("STRICT_OVERIDEAL_CONTROL_SOURCE_REQUIRED=1")
    print("BORDERED_PLANT_CONTROL_SOURCE_REQUIRED=1")
    print("DEAD_CLASSIFIER_POSITIVE_CONTROL_PASS=1")
    print("SURVIVOR_CLASSIFIER_POSITIVE_CONTROL_PASS=1")
    print("SINGULAR_DIAGNOSTIC_NEGATIVE_CONTROL_PASS=1")
    print("TRIPLE02_PROPER_OPEN_GENERATOR_SELFCHECK_PASS=1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
