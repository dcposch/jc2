#!/usr/bin/env python3
"""Light source/mutation/semantic preflight for the closed-successor resume.

No CAS is run.  Exercises the preparer's archive/member gates, the builder's
script validators, the recursor's repaired stage templates and route guards,
and the classifier's positive and hostile controls on synthetic stage trees.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil


DELTA_NODE1_SHA256 = (
    "84b4c2c4c0bfe5aa7414c35813cc1cf63d7d5416358a394b8e8bdc35820f1d02")


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"MODULE_IMPORT_FAILURE:{name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def sha256_text(text: str) -> str:
    return sha256_bytes(text.encode())


def expect_rejection(callable_, expected: str, label: str, *call_args) -> None:
    try:
        callable_(*call_args)
    except (RuntimeError, SystemExit) as exc:
        if expected in str(exc):
            return
        raise SystemExit(f"WRONG_MUTATION_REJECTION:{label}:{expected}:{exc}")
    raise SystemExit(f"MUTATION_NOT_REJECTED:{label}:{expected}")


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
        "ideal SUCCESSOR_J=x*y,y;",
        "reduce(SUCCESSOR_PARENT_DELTA,SUCCESSOR_J_SB)!=0",
        "reduce(1,SUCCESSOR_OPEN_SB)!=0",
        "SELFTEST_SUCCESSOR_CONTAINS_PARENT_DELTA=1",
        "SELFTEST_SUCCESSOR_PROPER=1",
        "SELFTEST_SUCCESSOR_PARENT_OPEN_EMPTY=1",
        "SELFTEST_ENDPOINT_TWO_SHIFT_AT_LEAST_ONE_NONZERO=",
        "SELFTEST_BORDERED_PLANT_EQUALS_DELTA=",
        "TRIPLE02_CLOSED_SUCCESSOR_ADAPTER_SELFCHECK_PASS=1",
    )
    missing = [token for token in required if text.count(token) != 1]
    if missing:
        raise RuntimeError(
            "ADAPTER_SEMANTIC_CONTROL_CENSUS:" + ",".join(missing))
    if any(token in text for token in ("PLACEHOLDER", "TODO")):
        raise RuntimeError("ADAPTER_SEMANTIC_CONTROL_PLACEHOLDER")


def write_stage(node_dir: Path, label: str, script_name: str,
                lines: list[str]) -> None:
    script = node_dir / script_name
    if not script.is_file():
        script.write_text(f"// fixture stage {label}\n")
    stdout = node_dir / f"{label}.stdout.txt"
    stderr = node_dir / f"{label}.stderr.txt"
    stdout.write_text("\n".join(lines) + "\n")
    stderr.write_text("")
    (node_dir / f"{label}.result.json").write_text(json.dumps({
        "returncode": 0,
        "timed_out": False,
        "script_sha256": sha256(script),
        "stdout_sha256": sha256(stdout),
        "stderr_sha256": sha256(stderr),
    }, sort_keys=True) + "\n")


def make_production_fixture(root: Path, prepared: Path, build: Path,
                            classifier, dead: bool) -> Path:
    root.mkdir(parents=True, exist_ok=False)
    witness_dir = root / "witness_replay"
    witness_dir.mkdir()
    real_script = build / "TRIPLE02_NODE1_WITNESS_REPLAY.sing"
    shutil.copyfile(real_script, witness_dir / "witness_replay.sing")
    for name, archived in (
            ("NODE_001_STANDARD_BASIS.txt",
             "r3/output/node_001/NODE_001_STANDARD_BASIS.txt"),
            ("NODE_001_REDUCE_PIVOTS.tsv",
             "r3/output/node_001/NODE_001_REDUCE_PIVOTS.tsv"),
            ("NODE_001_REDUCE_RESIDUAL.tsv",
             "r3/output/node_001/NODE_001_REDUCE_RESIDUAL.tsv")):
        shutil.copyfile(prepared / archived, witness_dir / name)
    write_stage(witness_dir, "witness_replay", "witness_replay.sing",
                list(classifier.WITNESS_REPLAY_MARKERS)
                + ["CLOSED_SUCCESSOR_EMPTY=0"])
    resume_input = json.loads((build / "RESUME_NODE_INPUT.json").read_text())
    node = root / "node_002"
    node.mkdir()
    (node / "NODE_INPUT.json").write_text(json.dumps({
        "node": 2,
        "generators": resume_input["generators"],
        "generator_sha256": resume_input["generator_sha256"],
        "inherited_rank_upper_bound": 6,
        "closed_successor_of_node": 1,
    }, indent=2, sort_keys=True) + "\n")
    write_census(node / "NODE_002_REDUCE_PIVOTS.tsv",
                 "step|source_row|source_col|pivot", 95)
    write_census(node / "NODE_002_REDUCE_RESIDUAL.tsv", "rows|11|cols|10", 110)
    write_stage(node, "reduce", "reduce.sing", [
        "NODE_INDEX=2", "NODE_GENERATOR_COUNT=3", "NODE_EMPTY=0",
        "NODE_REDUCER_FIXTURES_PASS=1", "NF_RATIONAL_UNIT_PIVOT_COUNT=95",
        "NF_PIVOT_INVARIANT_FAILURES=0", "NODE_RESIDUAL_REDUCTION_COMPLETE=1",
        "NODE_REDUCE_COMPLETE=1"])
    (node / "rank_size_6.support.json").write_text(json.dumps({
        "node": 2, "size": 6, "formal_slots": 97020,
        "support_matchable": 1, "structural_zero": 97019,
        "support_entries": 36}, sort_keys=True) + "\n")
    write_stage(node, "rank_size_6", "rank_size_6.sing", [
        "RANK_SIZE=6", "SUPPORT_REPLAY_FAILURES=0",
        "RANK_SIZE_WITNESS_FOUND=1", "RANK_SIZE_CENSUS_COMPLETE=1"])
    fixture_delta = "q0+1"
    (node / "NODE_002_SIZE_6_WITNESS.tsv").write_text(
        "rank|rows|cols|normal_form\n"
        f"6|1,2,4,7,9,11|1,2,3,5,6,7|{fixture_delta}\n")
    (node / "NODE_002_EMPTY_OPEN_POWER_CERTIFICATE.txt").write_text(
        "found|0|exponent|-1|normal_form|1")
    write_census(node / "NODE_002_REVERSE_CONTAINMENT_ATTEMPTS.tsv",
                 "basis_generator|exponent|normal_form", 4)
    write_census(node / "NODE_002_REVERSE_CONTAINMENT_WITNESSES.tsv",
                 "basis_generator|found|exponent|normal_form", 2)
    (node / "NODE_002_OPEN_SAT_STANDARD_BASIS.txt").write_text("q0\n")
    next_empty = "1" if dead else "0"
    write_stage(node, "saturation", "saturation.sing", [
        "NODE_REDUCER_FIXTURES_PASS=1", "SATURATION_OBJECT_TYPE=list",
        "SATURATION_OBJECT_SIZE=1", "SATURATION_SLOT1_TYPE=ideal",
        "SATURATION_NODE_INCLUSION_FAILURES=0",
        "SATURATION_STABILITY_FAILURES=0",
        "REVERSE_CONTAINMENT_ENTERED=1",
        "REVERSE_CONTAINMENT_BASIS_GENERATOR_COUNT=2",
        "REVERSE_CONTAINMENT_WITNESS_FOUND_COUNT=2",
        "REVERSE_CONTAINMENT_MEMBERSHIP_REDUCTION_COUNT=4",
        "REVERSE_CONTAINMENT_SEARCH_BOUND=64",
        "EMPTY_BRANCH_POWER_SEARCH_ENTERED=0",
        "EMPTY_OPEN_POWER_MEMBERSHIP_CERTIFICATE=0",
        "PROPER_OPEN_IDEAL_CERTIFICATE=1",
        "OPEN_CHART_EMPTY=0",
        f"NEXT_REMAINDER_EMPTY={next_empty}",
        "SATURATION_CERTIFICATE_COMPLETE=1",
        "OPEN_SATURATION_AND_CLOSED_SUCCESSOR_COMPLETE=1"])
    write_census(node / "NODE_002_CHART_PIVOTS.tsv",
                 "step|source_row|source_col|pivot", 95)
    shutil.copyfile(node / "NODE_002_REDUCE_PIVOTS.tsv",
                    node / "NODE_002_CHART_PIVOTS.tsv")
    shutil.copyfile(node / "NODE_002_REDUCE_RESIDUAL.tsv",
                    node / "NODE_002_CHART_RESIDUAL.tsv")
    write_census(node / "NODE_002_CHART_BASE_CHANGED_RESIDUAL.tsv",
                 "rows|11|cols|10", 110)
    write_census(node / "NODE_002_BASE_CHANGED_RIGHT_TRANSFORM.tsv",
                 "row|col|normal_form", 11025)
    write_census(node / "NODE_002_BORDERED_IDENTITIES.tsv",
                 "basis|free_col|residual_row|normal_form", 44)
    write_census(node / "NODE_002_ADJUGATE_KERNEL_105.tsv",
                 "coordinate|basis|normal_form", 420)
    write_census(node / "NODE_002_ENDPOINT_DELTA2_CLEARED_NF.tsv",
                 "basis_i|basis_j|normal_form", 10)
    (node / "NODE_002_ENDPOINT_TWO_SHIFT_PLANT.txt").write_text("plant\n")
    (node / "NODE_002_BORDERED_NONZERO_PLANT.txt").write_text("plant\n")
    (node / "NODE_002_CHART_DELTA.txt").write_text(fixture_delta + "\n")
    shutil.copyfile(node / "NODE_002_OPEN_SAT_STANDARD_BASIS.txt",
                    node / "NODE_002_CHART_ACTIVE_STANDARD_BASIS.txt")
    chart_lines = [
        "NODE_REDUCER_FIXTURES_PASS=1", "CHART_SATURATION_OBJECT_TYPE=list",
        "CHART_SATURATION_OBJECT_SIZE=1", "CHART_SATURATION_SLOT1_TYPE=ideal",
        "CHART_SATURATION_NODE_INCLUSION_FAILURES=0",
        "CHART_SATURATION_STABILITY_FAILURES=0",
        "CHART_OPEN_PROPER_IDEAL_CERTIFICATE=1",
        "OPEN_CHART_SATURATION_PROPER=1", "CHART_PIVOT_REDUCER=NODE_SB",
        "CHART_BASE_CHANGE_REDUCTION_COUNT=11135",
        "RESIDUAL_BASE_CHANGE_ENTRY_COUNT=110",
        "RIGHT_TRANSFORM_ENTRY_COUNT=11025",
        "RIGHT_TRANSFORM_RECORDED_ENTRY_COUNT=11025",
        "FULL_RIGHT_TRANSFORM_RECONSTRUCTED=1",
        "NODE_TRANSFORM_BASE_CHANGED_TO_ACTIVE_SB=1",
        "NF_RATIONAL_UNIT_PIVOT_COUNT=95", "NF_PIVOT_INVARIANT_FAILURES=0",
        "ADJUGATE_KERNEL_VECTOR_COUNT=4", "CHART_DELTA_NF_NONZERO=1",
        "SCANNED_DELTA_REPLAY_EQUAL=1", "COMPLETE_BORDERED_IDENTITY_COUNT=44",
        "BORDERED_IDENTITY_FAILURES=0", "BORDERED_NONZERO_PLANT_NF_NONZERO=1",
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
    ]
    if dead:
        chart_lines += ["ENDPOINT_COEFFICIENT_NF_NONZERO_COUNT=0",
                        "CHART_CLASSIFICATION=ENDPOINT_DEAD_ONLY_ON_D_DELTA"]
        classification = classifier.CLASS_DEAD
    else:
        chart_lines += [
            "ENDPOINT_COEFFICIENT_NF_NONZERO_COUNT=1",
            "CHART_CLASSIFICATION=RING_LEVEL_SURVIVOR_ON_CHART_"
            "PENDING_NILPOTENCE_RADICAL"]
        classification = classifier.CLASS_SURVIVOR
    write_stage(node, "chart", "chart.sing", chart_lines)
    summary = {
        "classification": classification,
        "component": "triple02",
        "closed_successor_of_node": 1,
        "start_node": 2,
        "settled_open_route": "NEVER_REENTERED",
        "delta_node1_sha256": DELTA_NODE1_SHA256,
        "no_radical_nilpotence_or_geometric_inference": True,
        "whole_component_or_jc2_inference": False,
    }
    (root / "SUMMARY.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n")
    (root / "VERDICT.txt").write_text(classification + "\n")
    return root


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--preparer", required=True, type=Path)
    parser.add_argument("--builder", required=True, type=Path)
    parser.add_argument("--recursor", required=True, type=Path)
    parser.add_argument("--classifier", required=True, type=Path)
    parser.add_argument("--adapter-selfcheck", required=True, type=Path)
    parser.add_argument("--frozen-archive", required=True, type=Path)
    parser.add_argument("--frozen-r5-source", required=True, type=Path)
    parser.add_argument("--prepared", required=True, type=Path)
    parser.add_argument("--build", required=True, type=Path)
    parser.add_argument("--fixture-root", required=True, type=Path)
    args = parser.parse_args()
    preparer = load("cs_preparer", args.preparer.resolve())
    builder = load("cs_builder", args.builder.resolve())
    recursor = load("cs_recursor", args.recursor.resolve())
    classifier = load("cs_classifier", args.classifier.resolve())
    fixture_root = args.fixture_root.resolve()
    fixture_root.mkdir(parents=True, exist_ok=True)
    prepared = args.prepared.resolve()
    build = args.build.resolve()

    adapter_source = args.adapter_selfcheck.resolve().read_text()
    validate_adapter_source(adapter_source)
    for anchor in ("ideal BAD_B=y,x-1;", "BORDERED_PLANT_NF==0",
                   "ideal SUCCESSOR_J=x*y,y;"):
        expect_rejection(validate_adapter_source,
                         "ADAPTER_SEMANTIC_CONTROL_CENSUS",
                         f"adapter:{anchor}",
                         adapter_source.replace(anchor, "", 1))

    if preparer.verify_archive_sha(
            args.frozen_archive.resolve(),
            preparer.R3_ARCHIVE_SHA256) != preparer.R3_ARCHIVE_SHA256:
        raise SystemExit("FROZEN_ARCHIVE_POSITIVE_CONTROL_FAILURE")
    tampered = fixture_root / "tampered_archive.bin"
    tampered.write_bytes(b"not-the-frozen-archive")
    expect_rejection(
        lambda: preparer.verify_archive_sha(tampered,
                                            preparer.R3_ARCHIVE_SHA256),
        "FROZEN_ARCHIVE_SHA_DRIFT", "archive-hash")
    expect_rejection(
        lambda: preparer.safe_relative("../output/node_001/NODE_INPUT.json"),
        "UNSAFE_ARCHIVE_MEMBER", "traversal-member")
    if (preparer.r3_selected("output/node_001/NODE_INPUT.json.mutated")
            or not preparer.r3_selected("output/node_001/NODE_INPUT.json")):
        raise SystemExit("EXACT_MEMBER_SELECTION_MUTATION_NOT_REJECTED")
    for excluded in preparer.R3_EXCLUDED_OPEN_ROUTE_MEMBERS:
        if preparer.r3_selected(excluded):
            raise SystemExit(f"OPEN_ROUTE_MEMBER_SELECTED:{excluded}")

    witness_script = (build / "TRIPLE02_NODE1_WITNESS_REPLAY.sing").read_text()
    resume_input = json.loads((build / "RESUME_NODE_INPUT.json").read_text())
    generators = resume_input["generators"]
    delta = generators[2]
    builder.validate_witness_replay_script(witness_script, delta)
    delta_line = next(line for line in witness_script.splitlines()
                      if line.startswith("poly ARCHIVED_DELTA_NODE1="))
    expect_rejection(builder.validate_witness_replay_script,
                     "WITNESS_DELTA_LITERAL_OR_HASH_DRIFT", "witness-delta",
                     witness_script.replace(delta_line,
                                            delta_line[:-1] + "+1;"), delta)
    expect_rejection(builder.validate_witness_replay_script,
                     "FORBIDDEN_WITNESS_REPLAY_TOKEN", "witness-sat",
                     witness_script
                     + "\nlist BAD=sat(NODE_IDEAL,ideal(1));\n", delta)
    expect_rejection(builder.validate_witness_replay_script,
                     "REQUIRED_WITNESS_REPLAY_TOKEN_CENSUS", "witness-guard",
                     witness_script.replace(
                         "SETTLED_OPEN_ROUTE_NOT_REENTERED=1",
                         "SETTLED_OPEN_ROUTE_NOT_REENTERED_REMOVED=1"), delta)
    expect_rejection(builder.validate_witness_replay_script,
                     "WITNESS_RING_DECLARATION_CENSUS", "witness-ring",
                     witness_script.replace(builder.RING_DECLARATION,
                                            "ring ambient=0,(q2,q0,c4,c6),dp;"),
                     delta)
    node2_reduce = (build / "NODE_002_REDUCE_EXPECTED.sing").read_text()
    builder.validate_node2_reduce_script(node2_reduce, delta)
    expect_rejection(builder.validate_node2_reduce_script,
                     "FORBIDDEN_NODE2_REDUCE_TOKEN", "node2-sat",
                     node2_reduce + "\nlist BAD=sat(NODE_IDEAL,ideal(1));\n",
                     delta)
    expect_rejection(builder.validate_node2_reduce_script,
                     "NODE2_HEADER_CENSUS", "node2-index",
                     node2_reduce.replace("NODE_INDEX=2", "NODE_INDEX=1"),
                     delta)

    r5 = builder.load_r5(args.frozen_r5_source.resolve())
    base = prepared / "r3/work/base"
    label, _zeros, _factor, remaining, assignment, _counts = r5.source_inputs(
        base, "triple02")
    clean_generators = [r5.clean_poly(value) for value in generators]
    fixture_delta = "q0+1"
    saturation_script = recursor.build_repaired_saturation_script(
        r5, remaining, clean_generators, 2, fixture_delta)
    recursor.validate_saturation_script(saturation_script, 2, 3, fixture_delta)
    expect_rejection(recursor.validate_saturation_script,
                     "SATURATION_DELTA_IS_SETTLED_NODE1_DELTA",
                     "saturation-node1-delta",
                     saturation_script, 2, 3, delta)
    expect_rejection(recursor.validate_saturation_script,
                     "SATURATION_POWER_SEARCH_NOT_GATED", "saturation-gate",
                     saturation_script.replace(
                         "if(OPEN_UNIT_NF==0){ for(ek=0;ek<=256;ek=ek+1){",
                         "for(ek=0;ek<=256;ek=ek+1){ if(1){", 1),
                     2, 3, fixture_delta)
    expect_rejection(recursor.validate_saturation_script,
                     "SATURATION_SCRIPT_TOKEN_CENSUS", "saturation-reverse",
                     saturation_script.replace(
                         "REVERSE_CONTAINMENT_SEARCH_BOUND=64",
                         "REVERSE_CONTAINMENT_SEARCH_BOUND_REMOVED=64", 1),
                     2, 3, fixture_delta)
    residual = r5.read_residual(
        prepared / "r3/output/node_001/NODE_001_REDUCE_RESIDUAL.tsv")
    rows, cols, real_delta = r5.read_witness(
        prepared / "r3/output/node_001/NODE_001_SIZE_6_WITNESS.tsv", 6)
    chart_script = recursor.build_repaired_chart_script(
        r5, remaining, clean_generators, 2, label, assignment, residual, 6,
        rows, cols, fixture_delta)
    recursor.validate_chart_script(chart_script, 2, 3, 6, fixture_delta)
    expect_rejection(recursor.validate_chart_script,
                     "CHART_DELTA_IS_SETTLED_NODE1_DELTA", "chart-node1-delta",
                     chart_script, 2, 3, 6, real_delta)
    expect_rejection(recursor.validate_chart_script,
                     "POST_BASE_CHANGE_REPIVOT_PRESENT", "chart-repivot",
                     chart_script.replace(
                         "RECURSIVE_ENDPOINT_CHART_COMPLETE=1",
                         "RECURSIVE_ENDPOINT_CHART_COMPLETE=1 while(step", 1),
                     2, 3, 6, fixture_delta)
    expect_rejection(recursor.validate_chart_script,
                     "CHART_SCRIPT_TOKEN_CENSUS", "chart-count-gate",
                     chart_script.replace("kernel_entry_count!=420",
                                          "kernel_entry_count==420", 1),
                     2, 3, 6, fixture_delta)
    expect_rejection(recursor.validate_chart_script,
                     "CHART_SCRIPT_TOKEN_CENSUS", "chart-transform-record",
                     chart_script.replace(
                         "RIGHT_TRANSFORM_RECORDED_ENTRY_COUNT=", "", 1),
                     2, 3, 6, fixture_delta)

    gate = classifier.load_pinned(
        "sc_transcript_gate",
        args.frozen_r5_source.resolve().parent / "transcript_gate.py",
        classifier.TRANSCRIPT_GATE_SHA256)
    dead_root = make_production_fixture(
        fixture_root / "dead", prepared, build, classifier, dead=True)
    dead_payload = classifier.classify(dead_root, prepared, build, r5, gate)
    if dead_payload["classification"] != classifier.CLASS_DEAD:
        raise SystemExit("DEAD_CLASSIFIER_CONTROL_DISAGREEMENT")
    survivor_root = make_production_fixture(
        fixture_root / "survivor", prepared, build, classifier, dead=False)
    survivor_payload = classifier.classify(
        survivor_root, prepared, build, r5, gate)
    if survivor_payload["classification"] != classifier.CLASS_SURVIVOR:
        raise SystemExit("SURVIVOR_CLASSIFIER_CONTROL_DISAGREEMENT")

    verdict_path = dead_root / "VERDICT.txt"
    original_verdict = verdict_path.read_text()
    verdict_path.write_text(classifier.CLASS_SURVIVOR + "\n")
    summary_path = dead_root / "SUMMARY.json"
    summary = json.loads(summary_path.read_text())
    summary["classification"] = classifier.CLASS_SURVIVOR
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    expect_rejection(classifier.classify, "CLASSIFIER_DRIVER_DISAGREEMENT",
                     "driver-verdict-swap", dead_root, prepared, build, r5,
                     gate)
    verdict_path.write_text(original_verdict)
    summary["classification"] = classifier.CLASS_DEAD
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")

    chart_residual = dead_root / "node_002/NODE_002_CHART_RESIDUAL.tsv"
    residual_bytes = chart_residual.read_bytes()
    chart_residual.write_bytes(residual_bytes.replace(
        b"1|fixture", b"1|tampered", 1))
    expect_rejection(classifier.classify, "EXACT_REPLAY_DISAGREEMENT",
                     "chart-residual-tamper", dead_root, prepared, build, r5,
                     gate)
    chart_residual.write_bytes(residual_bytes)

    chart_stdout = dead_root / "node_002/chart.stdout.txt"
    chart_text = chart_stdout.read_text()
    chart_stdout.write_text(chart_text.replace(
        "ENDPOINT_TWO_SHIFT_AT_LEAST_ONE_NONZERO=1\n", "", 1))
    result_path = dead_root / "node_002/chart.result.json"
    result = json.loads(result_path.read_text())
    result["stdout_sha256"] = sha256(chart_stdout)
    result_path.write_text(json.dumps(result, sort_keys=True) + "\n")
    expect_rejection(classifier.classify, "MARKER_CENSUS",
                     "chart-plant-marker-drop", dead_root, prepared, build,
                     r5, gate)
    chart_stdout.write_text(chart_text)
    result["stdout_sha256"] = sha256(chart_stdout)
    result_path.write_text(json.dumps(result, sort_keys=True) + "\n")

    node1_dir = dead_root / "node_001"
    (dead_root / "node_002").rename(node1_dir)
    expect_rejection(classifier.classify, "SETTLED_NODE1_DIRECTORY_PRESENT",
                     "node1-directory", dead_root, prepared, build, r5, gate)
    node1_dir.rename(dead_root / "node_002")
    final_check = classifier.classify(dead_root, prepared, build, r5, gate)
    if final_check["classification"] != classifier.CLASS_DEAD:
        raise SystemExit("DEAD_CLASSIFIER_RESTORE_CONTROL")

    hostile_stdout = fixture_root / "hostile.stdout.txt"
    hostile_stderr = fixture_root / "hostile.stderr.txt"
    hostile_stdout.write_text("   ? wrong range[2] in list _(1)\n")
    hostile_stderr.write_text("")
    diagnostic_rejected = False
    try:
        gate.assert_clean_transcript(hostile_stdout, hostile_stderr)
    except RuntimeError as exc:
        diagnostic_rejected = (
            "SINGULAR_DIAGNOSTIC_WITH_ANY_RETURN_CODE" in str(exc))
    if not diagnostic_rejected:
        raise SystemExit("DIAGNOSTIC_CONTROL_NOT_REJECTED")

    print(f"WITNESS_REPLAY_SCRIPT_SHA256={sha256_text(witness_script)}")
    print(f"NODE2_REDUCE_SCRIPT_SHA256={sha256_text(node2_reduce)}")
    print("ARCHIVE_HASH_MUTATION_REJECTED=1")
    print("TRAVERSAL_MEMBER_MUTATION_REJECTED=1")
    print("OPEN_ROUTE_MEMBER_SELECTION_REJECTED=1")
    print("WITNESS_DELTA_MUTATION_REJECTED=1")
    print("WITNESS_SATURATION_INJECTION_REJECTED=1")
    print("WITNESS_ROUTE_GUARD_MUTATION_REJECTED=1")
    print("RING_ORDER_MUTATION_REJECTED=1")
    print("NODE2_SATURATION_INJECTION_REJECTED=1")
    print("SATURATION_NODE1_DELTA_GUARD_REJECTED=1")
    print("SATURATION_UNGATED_POWER_SEARCH_REJECTED=1")
    print("SATURATION_REVERSE_MARKER_DROP_REJECTED=1")
    print("CHART_NODE1_DELTA_GUARD_REJECTED=1")
    print("CHART_REPIVOT_MUTATION_REJECTED=1")
    print("CHART_COUNT_GATE_MUTATIONS_REJECTED=2")
    print("DEAD_CLASSIFIER_POSITIVE_CONTROL_PASS=1")
    print("SURVIVOR_CLASSIFIER_POSITIVE_CONTROL_PASS=1")
    print("DRIVER_VERDICT_SWAP_REJECTED=1")
    print("CHART_RESIDUAL_TAMPER_REJECTED=1")
    print("CHART_PLANT_MARKER_DROP_REJECTED=1")
    print("SETTLED_NODE1_DIRECTORY_REJECTED=1")
    print("SINGULAR_DIAGNOSTIC_NEGATIVE_CONTROL_PASS=1")
    print("TRIPLE02_CLOSED_SUCCESSOR_GENERATOR_SELFCHECK_PASS=1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
