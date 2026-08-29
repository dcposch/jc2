#!/usr/bin/env python3
"""Light source/mutation/semantic preflight for the closed-successor resume (R3).

No CAS is run.  Exercises the preparer's archive/member gates, the builder's
script validators, the recursor's repaired stage templates and route guards,
and the R3 classifier's positive and hostile controls on synthetic stage
trees whose scripts are the REAL regenerated builder outputs and whose
result/identity records carry a full synthetic job binding.  The hostile set
includes candidate/stage-copy, missing/wrong identity, fabricated script,
wrong cap/binary/source/nonce, artifact-set extras, and no-verdict reason
mutations demanded by the R1 hostile review's C2 repair, plus the R2 hostile
review's O-N1/O-N2/O-N6 probes: runner-log content tampers, doubled and
multi-line node standard-basis stacks, and identity-record key injection.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile


DELTA_NODE1_SHA256 = (
    "84b4c2c4c0bfe5aa7414c35813cc1cf63d7d5416358a394b8e8bdc35820f1d02")
FIX_NONCE = "fixturenonce01"
FIX_TAG = ("ggv_triple02_closed_successor_resume_r4_19700101T000000Z_"
           + FIX_NONCE)
FIX_SOURCE_SHA = "a" * 64
FIX_SINGULAR_SHA = "b" * 64
FIX_SINGULAR_PATH = "/usr/bin/SingularFixture"
FIX_WORKER = {"pid": 4242, "pgid": 4242, "sid": 4242, "starttime": 111222,
              "uid": 1000, "mode": "systemd_scope", "cgroup": "0::/fixture"}
FIX_SUPERVISOR = {"pid": 4100, "pgid": 4100, "sid": 4100,
                  "starttime": 111000, "cpu": 0}
FIXTURE_DELTA = "q0+1"
FIXTURE_ROWS = "1,2,3,4,5,6"
FIXTURE_COLS = "1,2,3,4,5,6"


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


class FixtureJob:
    """A synthetic one-job binding for driving the strict classifier."""

    def __init__(self, root: Path, classifier):
        self.root = root
        root.mkdir(parents=True, exist_ok=True)
        self.lease = root / "LEASE.json"
        self.lease.write_text(json.dumps({
            "schema": "fixture-lease", "job_tag": FIX_TAG,
            "job_nonce": FIX_NONCE}, sort_keys=True) + "\n")
        self.worker_identity = root / "worker_identity.json"
        self.worker_identity.write_text(
            json.dumps(FIX_WORKER, indent=2, sort_keys=True) + "\n")
        self.supervisor_identity = root / "supervisor_identity.json"
        self.supervisor_identity.write_text(
            json.dumps(FIX_SUPERVISOR, indent=2, sort_keys=True) + "\n")
        self.binding = classifier.Binding(
            FIX_TAG, FIX_NONCE, FIX_SOURCE_SHA, FIX_SINGULAR_SHA,
            FIX_SINGULAR_PATH, self.lease, self.worker_identity,
            self.supervisor_identity, 900, 3600)
        self.lease_sha = sha256(self.lease)

    def write_stage(self, node_dir: Path, node_key: object, label: str,
                    script_name: str, lines: list[str],
                    cap: int) -> dict[str, object]:
        script = node_dir / script_name
        if not script.is_file():
            raise SystemExit(f"FIXTURE_STAGE_SCRIPT_MISSING:{label}")
        stdout = node_dir / f"{label}.stdout.txt"
        stderr = node_dir / f"{label}.stderr.txt"
        stdout.write_text("\n".join(lines) + "\n")
        stderr.write_text("")
        # R3 (O-N2): the runner log is content-bound, so the fixture writes
        # the exact three lines consistent with the result record below.
        (node_dir / f"{label}.runner.stdout.txt").write_text(
            "SINGULAR_STAGE_RETURNCODE=0\nSINGULAR_STAGE_TIMED_OUT=0\n"
            "SINGULAR_STAGE_ELAPSED_SECONDS=0.5\n")
        (node_dir / f"{label}.runner.stderr.txt").write_text("")
        argv = [FIX_SINGULAR_PATH, "-q", str(script.resolve())]
        identity = {
            "argv": argv,
            "cap_seconds": cap,
            "expected_pgid": FIX_WORKER["pgid"],
            "expected_sid": FIX_WORKER["sid"],
            "job_nonce": FIX_NONCE,
            "job_tag": FIX_TAG,
            "lease_sha256": self.lease_sha,
            "runner": {"pid": 5000, "ppid": FIX_WORKER["pid"],
                       "pgid": FIX_WORKER["pgid"], "sid": FIX_WORKER["sid"],
                       "starttime": 111500, "uid": FIX_WORKER["uid"]},
            "runner_cgroup": "0::/fixture\n",
            "singular": {"pid": 5001, "ppid": 5000,
                         "pgid": FIX_WORKER["pgid"], "sid": FIX_WORKER["sid"],
                         "starttime": 111501, "uid": FIX_WORKER["uid"]},
            "singular_binary_sha256": FIX_SINGULAR_SHA,
            "singular_cgroup": "0::/fixture\n",
            "singular_path": FIX_SINGULAR_PATH,
            "source_archive_sha256": FIX_SOURCE_SHA,
            "stage_label": label,
            "supervisor": {"pid": FIX_SUPERVISOR["pid"], "ppid": 1,
                           "pgid": FIX_SUPERVISOR["pgid"],
                           "sid": FIX_SUPERVISOR["sid"],
                           "starttime": FIX_SUPERVISOR["starttime"],
                           "uid": FIX_WORKER["uid"]},
            "worker": {"pid": FIX_WORKER["pid"], "ppid": FIX_SUPERVISOR["pid"],
                       "pgid": FIX_WORKER["pgid"], "sid": FIX_WORKER["sid"],
                       "starttime": FIX_WORKER["starttime"],
                       "uid": FIX_WORKER["uid"]},
        }
        identity_path = node_dir / f"{label}.identity.json"
        identity_path.write_text(
            json.dumps(identity, indent=2, sort_keys=True) + "\n")
        payload = {
            "argv": argv,
            "cap_seconds": cap,
            "elapsed_seconds": 0.5,
            "expected_pgid": FIX_WORKER["pgid"],
            "expected_sid": FIX_WORKER["sid"],
            "identity_sha256": sha256(identity_path),
            "job_nonce": FIX_NONCE,
            "job_tag": FIX_TAG,
            "lease_sha256": self.lease_sha,
            "returncode": 0,
            "script_sha256": sha256(script),
            "singular_sha256": FIX_SINGULAR_SHA,
            "source_archive_sha256": FIX_SOURCE_SHA,
            "stage_label": label,
            "stderr_sha256": sha256(stderr),
            "stdout_sha256": sha256(stdout),
            "supervisor_starttime": FIX_SUPERVISOR["starttime"],
            "timed_out": False,
            "worker_starttime": FIX_WORKER["starttime"],
        }
        result_path = node_dir / f"{label}.result.json"
        result_path.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n")
        return {
            "node": node_key,
            "stage": label,
            "returncode": 0,
            "timed_out": False,
            "script_sha256": payload["script_sha256"],
            "stdout_sha256": payload["stdout_sha256"],
            "stderr_sha256": payload["stderr_sha256"],
            "identity_sha256": payload["identity_sha256"],
            "result_sha256": sha256(result_path),
        }


def fixture_residual_rows() -> list[str]:
    rows = ["rows|11|cols|10"]
    for i in range(1, 12):
        for j in range(1, 11):
            value = "q0" if (i == j and i <= 6) else "0"
            rows.append(f"{i}|{j}|{value}")
    return rows


def make_production_fixture(root: Path, prepared: Path, build: Path,
                            job: FixtureJob, recursor, builder, classifier,
                            r5, dead: bool) -> tuple[Path, list[dict[str, object]]]:
    root.mkdir(parents=True, exist_ok=False)
    records: list[dict[str, object]] = []
    base = prepared / "r3/work/base"
    label_component, _zeros, _factor, remaining, assignment, _counts = (
        r5.source_inputs(base, "triple02"))
    resume_input = json.loads((build / "RESUME_NODE_INPUT.json").read_text())
    generators = [r5.clean_poly(value) for value in resume_input["generators"]]

    witness_dir = root / "witness_replay"
    witness_dir.mkdir()
    shutil.copyfile(build / "TRIPLE02_NODE1_WITNESS_REPLAY.sing",
                    witness_dir / "witness_replay.sing")
    archived_sb = (prepared / "r3/output/node_001/NODE_001_STANDARD_BASIS.txt"
                   ).read_bytes()
    unit, count = recursor.identical_copies(archived_sb)
    if count % recursor.ARCHIVED_NODE1_SB_APPEND_COUNT != 0:
        raise SystemExit("FIXTURE_ARCHIVED_SB_NOT_TRIPLE")
    single_copy = archived_sb[:len(archived_sb)
                              // recursor.ARCHIVED_NODE1_SB_APPEND_COUNT]
    (witness_dir / "NODE_001_STANDARD_BASIS.txt").write_bytes(single_copy)
    for name in ("NODE_001_REDUCE_PIVOTS.tsv", "NODE_001_REDUCE_RESIDUAL.tsv"):
        shutil.copyfile(prepared / "r3/output/node_001" / name,
                        witness_dir / name)
    (witness_dir / "NODE_002_SEED_STANDARD_BASIS.txt").write_text("seed\n")
    records.append(job.write_stage(
        witness_dir, "witness", "witness_replay", "witness_replay.sing",
        list(classifier.WITNESS_REPLAY_MARKERS) + ["CLOSED_SUCCESSOR_EMPTY=0"],
        900))

    node = root / "node_002"
    node.mkdir()
    (node / "NODE_INPUT.json").write_text(json.dumps({
        "node": 2,
        "generators": generators,
        "generator_sha256": [sha256_text(g) for g in generators],
        "inherited_rank_upper_bound": 6,
        "closed_successor_of_node": 1,
    }, indent=2, sort_keys=True) + "\n")
    (node / "NODE_002_STANDARD_BASIS.txt").write_text("SBUNIT\n" * 4)
    (node / "reduce.sing").write_text(r5.build_reduce_script(
        remaining, generators, 2, label_component, assignment))
    write_census(node / "NODE_002_REDUCE_PIVOTS.tsv",
                 "step|source_row|source_col|pivot", 95)
    (node / "NODE_002_REDUCE_RESIDUAL.tsv").write_text(
        "\n".join(fixture_residual_rows()) + "\n")
    records.append(job.write_stage(node, 2, "reduce", "reduce.sing", [
        "NODE_INDEX=2", "NODE_GENERATOR_COUNT=3", "NODE_EMPTY=0",
        "NODE_REDUCER_FIXTURES_PASS=1", "NF_RATIONAL_UNIT_PIVOT_COUNT=95",
        "NF_PIVOT_INVARIANT_FAILURES=0", "NODE_RESIDUAL_REDUCTION_COMPLETE=1",
        "NODE_REDUCE_COMPLETE=1"], 3600))
    residual = r5.read_residual(node / "NODE_002_REDUCE_RESIDUAL.tsv")
    census_path = node / "rank_size_6.support.json"
    (node / "rank_size_6.sing").write_text(r5.build_rank_size_script(
        remaining, generators, 2, residual, 6, census_path))
    census = json.loads(census_path.read_text())
    if census["support_matchable"] != 1:
        raise SystemExit("FIXTURE_RESIDUAL_MATCHABLE_CENSUS")
    write_census(node / "NODE_002_SIZE_6_MINORS.tsv",
                 "slot|rows|cols|normal_form", 1)
    (node / "NODE_002_SIZE_6_WITNESS.tsv").write_text(
        "rank|rows|cols|normal_form\n"
        f"6|{FIXTURE_ROWS}|{FIXTURE_COLS}|{FIXTURE_DELTA}\n")
    records.append(job.write_stage(node, 2, "rank_size_6", "rank_size_6.sing", [
        "RANK_SIZE=6", "SUPPORT_REPLAY_FAILURES=0",
        "RANK_SIZE_WITNESS_FOUND=1", "RANK_SIZE_CENSUS_COMPLETE=1"], 3600))
    (node / "saturation.sing").write_text(
        recursor.build_repaired_saturation_script(
            r5, remaining, generators, 2, FIXTURE_DELTA))
    (node / "NODE_002_OPEN_SAT_STANDARD_BASIS.txt").write_text("q0\n")
    write_census(node / "NODE_002_REVERSE_CONTAINMENT_ATTEMPTS.tsv",
                 "basis_generator|exponent|normal_form", 4)
    write_census(node / "NODE_002_REVERSE_CONTAINMENT_WITNESSES.tsv",
                 "basis_generator|found|exponent|normal_form", 2)
    (node / "NODE_002_EMPTY_OPEN_POWER_CERTIFICATE.txt").write_text(
        "found|0|exponent|-1|normal_form|1")
    (node / "NODE_002_NEXT_STANDARD_BASIS.txt").write_text("next\n")
    next_empty = "1" if dead else "0"
    records.append(job.write_stage(node, 2, "saturation", "saturation.sing", [
        "NODE_INDEX=2", "NODE_GENERATOR_COUNT=3", "NODE_EMPTY=0",
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
        "OPEN_SATURATION_AND_CLOSED_SUCCESSOR_COMPLETE=1"], 3600))
    rows = tuple(int(value) for value in FIXTURE_ROWS.split(","))
    cols = tuple(int(value) for value in FIXTURE_COLS.split(","))
    (node / "chart.sing").write_text(recursor.build_repaired_chart_script(
        r5, remaining, generators, 2, label_component, assignment, residual,
        6, rows, cols, FIXTURE_DELTA))
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
    (node / "NODE_002_CHART_DELTA.txt").write_text(FIXTURE_DELTA + "\n")
    shutil.copyfile(node / "NODE_002_OPEN_SAT_STANDARD_BASIS.txt",
                    node / "NODE_002_CHART_ACTIVE_STANDARD_BASIS.txt")
    chart_lines = [
        "NODE_INDEX=2", "NODE_GENERATOR_COUNT=3", "NODE_EMPTY=0",
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
        remainder = generators + [FIXTURE_DELTA]
        bound = 6
    else:
        chart_lines += [
            "ENDPOINT_COEFFICIENT_NF_NONZERO_COUNT=1",
            "CHART_CLASSIFICATION=RING_LEVEL_SURVIVOR_ON_CHART_"
            "PENDING_NILPOTENCE_RADICAL"]
        classification = classifier.CLASS_SURVIVOR
        remainder = list(generators)
        bound = 6
    records.append(job.write_stage(node, 2, "chart", "chart.sing",
                                   chart_lines, 3600))
    (node / "NODE_RESULT.json").write_text(json.dumps({
        "node": 2,
        "rank": 6,
        "rank_upper_bound_in": 6,
        "delta": FIXTURE_DELTA,
        "delta_sha256": sha256_text(FIXTURE_DELTA),
        "delta_is_settled_node1_delta": False,
        "open_chart_empty_by_saturation": False,
        "next_remainder_empty": dead,
        "saturated_delta_normal_form": FIXTURE_DELTA,
        "endpoint_nonzero": not dead,
        "endpoint_dead": dead,
    }, indent=2, sort_keys=True) + "\n")
    summary = {
        "classification": classification,
        "component": "triple02",
        "closed_successor_of_node": 1,
        "start_node": 2,
        "nodes": [],
        "open_remainder_generators": remainder,
        "open_remainder_generator_sha256": [
            sha256_text(value) for value in remainder],
        "open_remainder_rank_upper_bound": bound,
        "endpoint": "x14*x72+x1*x97",
        "scope": ("EXACT_AMBIENT_QUOTIENT_NF_FINITE_CHART_RECURSION_"
                  "ON_TRIPLE02_NODE1_CLOSED_SUCCESSOR_ONLY"),
        "settled_open_route": "NEVER_REENTERED",
        "settled_open_verdict": "EXACT_ENDPOINT_DEAD_ON_NODE1_PROPER_OPEN_ONLY",
        "delta_node1_sha256": DELTA_NODE1_SHA256,
        "no_radical_nilpotence_or_geometric_inference": True,
        "whole_component_or_jc2_inference": False,
        "job_binding": job.binding.job_binding_block(),
        "stage_records": records,
    }
    (root / "SUMMARY.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n")
    (root / "VERDICT.txt").write_text(classification + "\n")
    return root, records


def rewrite_summary(root: Path, mutate) -> bytes:
    summary_path = root / "SUMMARY.json"
    original = summary_path.read_bytes()
    summary = json.loads(original)
    mutate(summary)
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    return original


def run_classify(classifier, root, prepared, build, r5, gate, recursor,
                 builder, job):
    with tempfile.TemporaryDirectory() as scratch:
        return classifier.classify(root, prepared, build, r5, gate, recursor,
                                   builder, job.binding, Path(scratch))


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
    if (preparer.R3_ARCHIVE_CENSUS != {"member_count": 454,
                                       "regular_file_count": 391,
                                       "directory_count": 63}
            or preparer.PROPER_OPEN_ARCHIVE_CENSUS != {
                "member_count": 574, "regular_file_count": 490,
                "directory_count": 84}):
        raise SystemExit("EXACT_ARCHIVE_CENSUS_PIN_DRIFT")

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
    saturation_script = recursor.build_repaired_saturation_script(
        r5, remaining, clean_generators, 2, FIXTURE_DELTA)
    recursor.validate_saturation_script(saturation_script, 2, 3, FIXTURE_DELTA)
    expect_rejection(recursor.validate_saturation_script,
                     "SATURATION_DELTA_IS_SETTLED_NODE1_DELTA",
                     "saturation-node1-delta",
                     saturation_script, 2, 3, delta)
    expect_rejection(recursor.validate_saturation_script,
                     "SATURATION_POWER_SEARCH_NOT_GATED", "saturation-gate",
                     saturation_script.replace(
                         "if(OPEN_UNIT_NF==0){ for(ek=0;ek<=256;ek=ek+1){",
                         "for(ek=0;ek<=256;ek=ek+1){ if(1){", 1),
                     2, 3, FIXTURE_DELTA)
    expect_rejection(recursor.validate_saturation_script,
                     "SATURATION_SCRIPT_TOKEN_CENSUS", "saturation-reverse",
                     saturation_script.replace(
                         "REVERSE_CONTAINMENT_SEARCH_BOUND=64",
                         "REVERSE_CONTAINMENT_SEARCH_BOUND_REMOVED=64", 1),
                     2, 3, FIXTURE_DELTA)
    residual = r5.read_residual(
        prepared / "r3/output/node_001/NODE_001_REDUCE_RESIDUAL.tsv")
    rows, cols, real_delta = r5.read_witness(
        prepared / "r3/output/node_001/NODE_001_SIZE_6_WITNESS.tsv", 6)
    chart_script = recursor.build_repaired_chart_script(
        r5, remaining, clean_generators, 2, label, assignment, residual, 6,
        rows, cols, FIXTURE_DELTA)
    recursor.validate_chart_script(chart_script, 2, 3, 6, FIXTURE_DELTA)
    expect_rejection(recursor.validate_chart_script,
                     "CHART_DELTA_IS_SETTLED_NODE1_DELTA", "chart-node1-delta",
                     chart_script, 2, 3, 6, real_delta)
    expect_rejection(recursor.validate_chart_script,
                     "POST_BASE_CHANGE_REPIVOT_PRESENT", "chart-repivot",
                     chart_script.replace(
                         "RECURSIVE_ENDPOINT_CHART_COMPLETE=1",
                         "RECURSIVE_ENDPOINT_CHART_COMPLETE=1 while(step", 1),
                     2, 3, 6, FIXTURE_DELTA)
    expect_rejection(recursor.validate_chart_script,
                     "CHART_SCRIPT_TOKEN_CENSUS", "chart-count-gate",
                     chart_script.replace("kernel_entry_count!=420",
                                          "kernel_entry_count==420", 1),
                     2, 3, 6, FIXTURE_DELTA)
    expect_rejection(recursor.validate_chart_script,
                     "CHART_SCRIPT_TOKEN_CENSUS", "chart-transform-record",
                     chart_script.replace(
                         "RIGHT_TRANSFORM_RECORDED_ENTRY_COUNT=", "", 1),
                     2, 3, 6, FIXTURE_DELTA)

    # Appended-artifact decomposition controls (archived node-1 SB triple).
    unit, count = recursor.identical_copies(b"abcabcabc")
    if unit != b"abc" or count != 3:
        raise SystemExit("IDENTICAL_COPIES_CONTROL_FAILURE")
    recursor.require_archived_append_copies(b"abc", b"abcabcabc", 3, "ctrl")
    expect_rejection(recursor.require_archived_append_copies,
                     "ARCHIVED_APPEND_COPY_DISAGREEMENT", "sb-single-copy",
                     b"abcabcabc", b"abcabcabc", 3, "ctrl")
    expect_rejection(recursor.require_archived_append_copies,
                     "ARCHIVED_APPEND_COPY_DISAGREEMENT", "sb-wrong-unit",
                     b"abd", b"abcabcabc", 3, "ctrl")
    archived_sb = (prepared / "r3/output/node_001/NODE_001_STANDARD_BASIS.txt"
                   ).read_bytes()
    unit, count = recursor.identical_copies(archived_sb)
    if count != recursor.ARCHIVED_NODE1_SB_APPEND_COUNT:
        raise SystemExit("ARCHIVED_SB_TRIPLE_CONTROL_FAILURE")
    recursor.require_archived_append_copies(
        unit, archived_sb, recursor.ARCHIVED_NODE1_SB_APPEND_COUNT, "ctrl")

    # R3 (O-N1): the single-line append law.  The source anchor is the real
    # archived node-1 write: string(NODE_SB) is newline-free, so each
    # completed stage appends exactly one single-line block, and a doubled
    # file is refused because its per-stage block carries two newlines.
    if unit.count(b"\n") != 1 or not unit.endswith(b"\n"):
        raise SystemExit("ARCHIVED_SB_UNIT_NOT_SINGLE_LINE")
    recursor.require_single_line_append_stack(
        archived_sb, recursor.ARCHIVED_NODE1_SB_APPEND_COUNT, "ctrl")
    recursor.require_single_line_append_stack(b"SBUNIT\n" * 4, 4, "ctrl")
    expect_rejection(recursor.require_single_line_append_stack,
                     "NODE_SB_APPEND_CENSUS", "sb-doubled-stack",
                     b"SBUNIT\n" * 8, 4, "ctrl")
    expect_rejection(recursor.require_single_line_append_stack,
                     "NODE_SB_APPEND_CENSUS", "sb-multiline-stack",
                     b"A\nB\n" * 3, 3, "ctrl")
    expect_rejection(recursor.require_single_line_append_stack,
                     "NODE_SB_APPEND_CENSUS", "sb-nonmultiple-stack",
                     b"SBUNIT\n" * 3, 4, "ctrl")
    expect_rejection(recursor.require_single_line_append_stack,
                     "NODE_SB_APPEND_CENSUS", "sb-empty-stack",
                     b"", 3, "ctrl")

    # R3 (O-N2): the runner stdout law tracks the verified result record.
    runner_payload = {"returncode": 0, "timed_out": False,
                      "elapsed_seconds": 0.5}
    recursor.require_runner_logs(
        b"SINGULAR_STAGE_RETURNCODE=0\nSINGULAR_STAGE_TIMED_OUT=0\n"
        b"SINGULAR_STAGE_ELAPSED_SECONDS=0.5\n", b"", runner_payload, "ctrl")
    expect_rejection(recursor.require_runner_logs,
                     "STAGE_RUNNER_STDOUT_BINDING", "runner-stdout-shape",
                     b"FATAL_ANYTHING\nrc=99\n", b"", runner_payload, "ctrl")
    expect_rejection(recursor.require_runner_logs,
                     "STAGE_RUNNER_STDERR_NONEMPTY", "runner-stderr-shape",
                     b"SINGULAR_STAGE_RETURNCODE=0\n"
                     b"SINGULAR_STAGE_TIMED_OUT=0\n"
                     b"SINGULAR_STAGE_ELAPSED_SECONDS=0.5\n",
                     b"warning: fixture\n", runner_payload, "ctrl")

    gate = classifier.load_pinned(
        "sc_transcript_gate",
        args.frozen_r5_source.resolve().parent / "transcript_gate.py",
        classifier.TRANSCRIPT_GATE_SHA256)
    job = FixtureJob(fixture_root / "job_binding", classifier)

    def classify_root(root: Path):
        return run_classify(classifier, root, prepared, build, r5, gate,
                            recursor, builder, job)

    dead_root, dead_records = make_production_fixture(
        fixture_root / "dead", prepared, build, job, recursor, builder,
        classifier, r5, dead=True)
    dead_payload = classify_root(dead_root)
    if dead_payload["classification"] != classifier.CLASS_DEAD:
        raise SystemExit("DEAD_CLASSIFIER_CONTROL_DISAGREEMENT")
    survivor_root, _ = make_production_fixture(
        fixture_root / "survivor", prepared, build, job, recursor, builder,
        classifier, r5, dead=False)
    survivor_payload = classify_root(survivor_root)
    if survivor_payload["classification"] != classifier.CLASS_SURVIVOR:
        raise SystemExit("SURVIVOR_CLASSIFIER_CONTROL_DISAGREEMENT")

    node = dead_root / "node_002"

    # 1. Driver-verdict swap.
    verdict_path = dead_root / "VERDICT.txt"
    original_verdict = verdict_path.read_bytes()
    verdict_path.write_text(classifier.CLASS_SURVIVOR + "\n")
    original_summary = rewrite_summary(
        dead_root, lambda summary: summary.update(
            classification=classifier.CLASS_SURVIVOR))
    expect_rejection(classify_root, "CLASSIFIER_DRIVER_DISAGREEMENT",
                     "driver-verdict-swap", dead_root)
    verdict_path.write_bytes(original_verdict)
    (dead_root / "SUMMARY.json").write_bytes(original_summary)

    # 2. Chart residual artifact tamper.
    chart_residual = node / "NODE_002_CHART_RESIDUAL.tsv"
    residual_bytes = chart_residual.read_bytes()
    chart_residual.write_bytes(residual_bytes.replace(b"|q0", b"|q2", 1))
    expect_rejection(classify_root, "EXACT_REPLAY_DISAGREEMENT",
                     "chart-residual-tamper", dead_root)
    chart_residual.write_bytes(residual_bytes)

    # 3. Chart plant-marker drop with rehashed result.
    chart_stdout = node / "chart.stdout.txt"
    chart_text = chart_stdout.read_text()
    result_path = node / "chart.result.json"
    original_result = result_path.read_bytes()
    chart_stdout.write_text(chart_text.replace(
        "ENDPOINT_TWO_SHIFT_AT_LEAST_ONE_NONZERO=1\n", "", 1))
    result = json.loads(original_result)
    result["stdout_sha256"] = sha256(chart_stdout)
    result_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    expect_rejection(classify_root, "MARKER_CENSUS",
                     "chart-plant-marker-drop", dead_root)
    chart_stdout.write_text(chart_text)
    result_path.write_bytes(original_result)

    # 4. Settled node-1 directory.
    (dead_root / "node_002").rename(dead_root / "node_001")
    expect_rejection(classify_root, "SETTLED_NODE1_DIRECTORY_PRESENT",
                     "node1-directory", dead_root)
    (dead_root / "node_001").rename(dead_root / "node_002")

    # 5. Missing stage identity record.
    identity_path = node / "reduce.identity.json"
    identity_bytes = identity_path.read_bytes()
    identity_path.unlink()
    expect_rejection(classify_root, "STAGE_IDENTITY_MISSING",
                     "missing-identity", dead_root)
    identity_path.write_bytes(identity_bytes)

    # 6. Copied prior-job stage records (foreign nonce in result+identity).
    result_path = node / "reduce.result.json"
    reduce_result = result_path.read_bytes()
    foreign = json.loads(reduce_result)
    foreign["job_nonce"] = "foreignnonce01"
    result_path.write_text(json.dumps(foreign, indent=2, sort_keys=True) + "\n")
    expect_rejection(classify_root, "STAGE_RESULT_JOB_BINDING_DRIFT",
                     "copied-stage-nonce", dead_root)
    result_path.write_bytes(reduce_result)

    # 7. Copied prior-job worker identity (wrong starttime inside identity).
    foreign_identity = json.loads(identity_bytes)
    foreign_identity["worker"] = dict(foreign_identity["worker"],
                                      starttime=999999)
    identity_path.write_text(
        json.dumps(foreign_identity, indent=2, sort_keys=True) + "\n")
    stale = json.loads(reduce_result)
    stale["identity_sha256"] = sha256(identity_path)
    result_path.write_text(json.dumps(stale, indent=2, sort_keys=True) + "\n")
    expect_rejection(classify_root, "STAGE_IDENTITY_WORKER_DISAGREEMENT",
                     "copied-identity-starttime", dead_root)
    identity_path.write_bytes(identity_bytes)
    result_path.write_bytes(reduce_result)

    # 8. Identity hash disagreement (identity edited, result not).
    identity_path.write_text(identity_bytes.decode() + "\n")
    expect_rejection(classify_root, "STAGE_IDENTITY_HASH_DISAGREEMENT",
                     "identity-hash", dead_root)
    identity_path.write_bytes(identity_bytes)

    # 9. Fabricated one-line stage script (self-consistent hashes).
    reduce_script = node / "reduce.sing"
    script_bytes = reduce_script.read_bytes()
    reduce_script.write_text("// fixture stage saturation\n")
    fabricated = json.loads(reduce_result)
    fabricated["script_sha256"] = sha256(reduce_script)
    result_path.write_text(
        json.dumps(fabricated, indent=2, sort_keys=True) + "\n")
    expect_rejection(classify_root, "SCRIPT_REGENERATION_DISAGREEMENT",
                     "fabricated-one-line-script", dead_root)
    reduce_script.write_bytes(script_bytes)
    result_path.write_bytes(reduce_result)

    # 10-12. Wrong cap / wrong Singular binary digest / wrong source hash.
    for key, value, label in (
            ("cap_seconds", 999, "wrong-cap"),
            ("singular_sha256", "c" * 64, "wrong-singular-binary"),
            ("source_archive_sha256", "d" * 64, "wrong-source-archive")):
        mutated = json.loads(reduce_result)
        mutated[key] = value
        result_path.write_text(
            json.dumps(mutated, indent=2, sort_keys=True) + "\n")
        expect_rejection(classify_root, "STAGE_RESULT_JOB_BINDING_DRIFT",
                         label, dead_root)
        result_path.write_bytes(reduce_result)

    # 13. Unexplained extra artifact in the node directory.
    extra = node / "EXTRA_UNEXPLAINED_FILE.txt"
    extra.write_text("stray\n")
    expect_rejection(classify_root, "ARTIFACT_SET_DRIFT", "artifact-extra",
                     dead_root)
    extra.unlink()

    # 14. Bounded no-verdict reason not derivable from stage evidence.
    original_summary = rewrite_summary(
        dead_root, lambda summary: summary.update(
            no_verdict_reason="STAGE_TIMEOUT:2:reduce"))
    expect_rejection(classify_root, "STAGE_TIMEOUT_FLAG_DISAGREEMENT",
                     "fabricated-timeout-reason", dead_root)
    (dead_root / "SUMMARY.json").write_bytes(original_summary)

    # 15. Remainder tamper.
    original_summary = rewrite_summary(
        dead_root, lambda summary: summary.update(
            open_remainder_rank_upper_bound=5))
    expect_rejection(classify_root, "DRIVER_REMAINDER_DISAGREEMENT",
                     "remainder-tamper", dead_root)
    (dead_root / "SUMMARY.json").write_bytes(original_summary)

    # 16. Stage-record tamper (dropped final record).
    original_summary = rewrite_summary(
        dead_root, lambda summary: summary.update(
            stage_records=summary["stage_records"][:-1]))
    expect_rejection(classify_root, "DRIVER_STAGE_RECORD_DISAGREEMENT",
                     "stage-record-drop", dead_root)
    (dead_root / "SUMMARY.json").write_bytes(original_summary)

    # 17. Foreign job binding in the driver summary.
    original_summary = rewrite_summary(
        dead_root, lambda summary: summary["job_binding"].update(
            job_nonce="foreignnonce01"))
    expect_rejection(classify_root, "DRIVER_SUMMARY_SCOPE_DRIFT",
                     "summary-binding-swap", dead_root)
    (dead_root / "SUMMARY.json").write_bytes(original_summary)

    # 18. Witness replay standard basis submitted as the full archived
    # triple instead of the single-stage unit.
    witness_sb = dead_root / "witness_replay/NODE_001_STANDARD_BASIS.txt"
    unit_bytes = witness_sb.read_bytes()
    witness_result = dead_root / "witness_replay/witness_replay.result.json"
    witness_result_bytes = witness_result.read_bytes()
    witness_sb.write_bytes(archived_sb)
    mutated = json.loads(witness_result_bytes)
    result_stub = mutated  # stdout unchanged; artifact files are not hashed
    witness_result.write_text(
        json.dumps(result_stub, indent=2, sort_keys=True) + "\n")
    expect_rejection(classify_root, "ARCHIVED_APPEND_COPY_DISAGREEMENT",
                     "witness-sb-full-archive", dead_root)
    witness_sb.write_bytes(unit_bytes)
    witness_result.write_bytes(witness_result_bytes)

    # 19. Runner stdout content tamper (the R2 review's O-N2 probe: the R2
    # classifier accepted "FATAL_ANYTHING\nrc=99\n" here).
    runner_stdout = node / "reduce.runner.stdout.txt"
    runner_stdout_bytes = runner_stdout.read_bytes()
    runner_stdout.write_bytes(b"FATAL_ANYTHING\nrc=99\n")
    expect_rejection(classify_root, "STAGE_RUNNER_STDOUT_BINDING",
                     "runner-stdout-tamper", dead_root)
    runner_stdout.write_bytes(runner_stdout_bytes)

    # 20. Nonempty runner stderr.
    runner_stderr = node / "reduce.runner.stderr.txt"
    runner_stderr.write_bytes(b"stray runner diagnostics\n")
    expect_rejection(classify_root, "STAGE_RUNNER_STDERR_NONEMPTY",
                     "runner-stderr-tamper", dead_root)
    runner_stderr.write_bytes(b"")

    # 21. Doubled node standard basis (accepted by the R2 divisibility
    # census: 8 copies over 4 header stages).
    node_sb = node / "NODE_002_STANDARD_BASIS.txt"
    node_sb_bytes = node_sb.read_bytes()
    node_sb.write_bytes(b"SBUNIT\n" * 8)
    expect_rejection(classify_root, "NODE_SB_APPEND_CENSUS",
                     "node-sb-doubled", dead_root)

    # 22. Multi-line per-stage block.
    node_sb.write_bytes(b"SBUNIT\nSECOND_LINE\n" * 4)
    expect_rejection(classify_root, "NODE_SB_APPEND_CENSUS",
                     "node-sb-multiline", dead_root)
    node_sb.write_bytes(node_sb_bytes)

    # 23. Identity record with an injected key and a rehashed result (the
    # R2 review's O-N6 probe; now refused directly by the key census).
    injected_identity = json.loads(identity_bytes)
    injected_identity["injected_extra_key"] = "attacker"
    identity_path.write_text(
        json.dumps(injected_identity, indent=2, sort_keys=True) + "\n")
    rehashed = json.loads(reduce_result)
    rehashed["identity_sha256"] = sha256(identity_path)
    result_path.write_text(
        json.dumps(rehashed, indent=2, sort_keys=True) + "\n")
    expect_rejection(classify_root, "STAGE_IDENTITY_KEY_CENSUS",
                     "identity-injected-key", dead_root)
    identity_path.write_bytes(identity_bytes)
    result_path.write_bytes(reduce_result)

    final_check = classify_root(dead_root)
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
    print("EXACT_ARCHIVE_CENSUS_PINS_454_391_63_574_490_84=1")
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
    print("ARCHIVED_SB_TRIPLE_DECOMPOSITION_CONTROLS_PASS=1")
    print("ARCHIVED_SB_UNIT_SINGLE_LINE_ANCHOR_PASS=1")
    print("SINGLE_LINE_APPEND_STACK_CONTROLS_PASS=1")
    print("RUNNER_LOG_LAW_UNIT_CONTROLS_PASS=1")
    print("DEAD_CLASSIFIER_POSITIVE_CONTROL_PASS=1")
    print("SURVIVOR_CLASSIFIER_POSITIVE_CONTROL_PASS=1")
    print("DRIVER_VERDICT_SWAP_REJECTED=1")
    print("CHART_RESIDUAL_TAMPER_REJECTED=1")
    print("CHART_PLANT_MARKER_DROP_REJECTED=1")
    print("SETTLED_NODE1_DIRECTORY_REJECTED=1")
    print("MISSING_STAGE_IDENTITY_REJECTED=1")
    print("COPIED_PRIOR_JOB_STAGE_NONCE_REJECTED=1")
    print("COPIED_PRIOR_JOB_IDENTITY_STARTTIME_REJECTED=1")
    print("STAGE_IDENTITY_HASH_MISMATCH_REJECTED=1")
    print("FABRICATED_ONE_LINE_SCRIPT_REJECTED=1")
    print("WRONG_STAGE_CAP_REJECTED=1")
    print("WRONG_SINGULAR_BINARY_DIGEST_REJECTED=1")
    print("WRONG_SOURCE_ARCHIVE_DIGEST_REJECTED=1")
    print("NODE_ARTIFACT_EXTRA_REJECTED=1")
    print("FABRICATED_NO_VERDICT_REASON_REJECTED=1")
    print("REMAINDER_TAMPER_REJECTED=1")
    print("STAGE_RECORD_TAMPER_REJECTED=1")
    print("SUMMARY_BINDING_SWAP_REJECTED=1")
    print("WITNESS_SB_FULL_ARCHIVE_SUBMISSION_REJECTED=1")
    print("RUNNER_STDOUT_TAMPER_REJECTED=1")
    print("RUNNER_STDERR_TAMPER_REJECTED=1")
    print("NODE_SB_DOUBLED_STACK_REJECTED=1")
    print("NODE_SB_MULTILINE_STACK_REJECTED=1")
    print("IDENTITY_INJECTED_KEY_REJECTED=1")
    print("SINGULAR_DIAGNOSTIC_NEGATIVE_CONTROL_PASS=1")
    print("TRIPLE02_CLOSED_SUCCESSOR_GENERATOR_SELFCHECK_PASS=1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
