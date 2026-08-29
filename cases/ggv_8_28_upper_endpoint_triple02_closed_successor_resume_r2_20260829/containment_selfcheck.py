#!/usr/bin/env python3
"""Light, no-CAS custody fixtures for containment and late promotion (R2).

All fixtures here are pure/parser-level: they drive the real contract
functions and CLIs on synthetic trees and injected records.  None of them
executes the launcher, supervisor, stage runner, systemd, or live /proc
custody paths; that live behavior remains AWS rehearsal debt and is stated
as such in the packet documents.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tarfile
import tempfile


FIX_NONCE = "fixturenonce01"
FIX_TAG = ("ggv_triple02_closed_successor_resume_r2_19700101T000000Z_"
           + FIX_NONCE)
FIX_SOURCE_SHA = "a" * 64
FIX_SINGULAR_SHA = "b" * 64
FIX_LAUNCHER_SHA = "c" * 64
FIX_LAUNCH_MANIFEST_SHA = "d" * 64
DEAD = "EXACT_ENDPOINT_DEAD_ON_TRIPLE02_NODE1_CLOSED_SUCCESSOR_FINITE_COVER"
SURVIVOR = ("RING_LEVEL_ENDPOINT_SURVIVOR_ON_TRIPLE02_NODE1_"
            "CLOSED_SUCCESSOR_CHART_PENDING_NILPOTENCE_RADICAL")


def load(path: Path):
    spec = importlib.util.spec_from_file_location("containment_contract", path)
    if spec is None or spec.loader is None:
        raise SystemExit("CONTRACT_IMPORT_FAILURE")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def expect_rejection(callable_, expected: str, label: str) -> None:
    try:
        callable_()
    except (RuntimeError, SystemExit, FileNotFoundError) as exc:
        if expected in str(exc) or expected == type(exc).__name__:
            return
        raise SystemExit(f"WRONG_CUSTODY_REJECTION:{label}:{expected}:{exc}")
    raise SystemExit(f"CUSTODY_MUTATION_NOT_REJECTED:{label}:{expected}")


def build_decision_fixture(contract, root: Path) -> dict[str, object]:
    """A miniature JOB_ROOT with a complete banked decision."""
    custody = root / "custody"
    production = root / "work/production"
    output = root / "output"
    for directory in (custody, production, output, root / "source"):
        directory.mkdir(parents=True)
    (root / "source/source.txt").write_text("source\n")
    (root / "source_archive.tar.gz").write_bytes(b"source archive fixture")
    (root / "launch_preflight_copy.sh").write_text("#launcher fixture\n")
    contract.build_lease(
        root / "LEASE.json", root / "LEASE.sha256", FIX_TAG, FIX_NONCE,
        FIX_SOURCE_SHA, FIX_LAUNCHER_SHA, FIX_LAUNCH_MANIFEST_SHA,
        4000, 100000)
    worker = {"pid": 4242, "pgid": 4242, "sid": 4242, "starttime": 111222,
              "uid": 1000, "mode": "systemd_scope", "cgroup": "0::/fixture"}
    supervisor = {"pid": 4100, "pgid": 4100, "sid": 4100,
                  "starttime": 111000, "cpu": 0}
    (custody / "worker_identity.json").write_text(
        json.dumps(worker, indent=2, sort_keys=True) + "\n")
    (custody / "supervisor_identity.json").write_text(
        json.dumps(supervisor, indent=2, sort_keys=True) + "\n")
    (custody / "containment_mode.txt").write_text("systemd_scope\n")
    (custody / "systemd_runtime_limits.json").write_text(json.dumps({
        "killmode": "control-group", "memory_max": "274877906944",
        "memory_swap_max": "0", "runtime_max_usec": "6h",
        "tasks_max": "512", "verified": True}, indent=2, sort_keys=True)
        + "\n")
    (custody / "singular_binary.sha256").write_text(
        f"{FIX_SINGULAR_SHA}  /usr/bin/SingularFixture\n")
    binding = {
        "job_nonce": FIX_NONCE, "job_tag": FIX_TAG,
        "lease_sha256": sha256(root / "LEASE.json"),
        "singular_sha256": FIX_SINGULAR_SHA,
        "source_archive_sha256": FIX_SOURCE_SHA,
        "supervisor": {"pid": 4100, "starttime": 111000},
        "worker": {"pid": 4242, "starttime": 111222},
    }
    for directory in (production, output):
        (directory / "VERDICT.txt").write_text(DEAD + "\n")
        (directory / "SUMMARY.json").write_text(json.dumps({
            "classification": DEAD, "job_binding": binding},
            indent=2, sort_keys=True) + "\n")
    (custody / "WORKER_ARTIFACT_MANIFEST.sha256").write_text(
        f"{'e' * 64}  work/production/VERDICT.txt\n")
    (custody / "CANDIDATE_MATHEMATICAL_VERDICT.txt").write_text(DEAD + "\n")
    record_sha = contract.build_decision_record(
        output_record=custody / "DECISION_RECORD.json",
        output_sidecar=custody / "DECISION_RECORD.sha256",
        job_tag=FIX_TAG, nonce=FIX_NONCE,
        source_archive_sha256=FIX_SOURCE_SHA,
        singular_sha256=FIX_SINGULAR_SHA, containment_mode="systemd_scope",
        lease_path=root / "LEASE.json",
        worker_identity_path=custody / "worker_identity.json",
        supervisor_identity_path=custody / "supervisor_identity.json",
        production_dir=production, classifier_dir=output,
        artifact_manifest=custody / "WORKER_ARTIFACT_MANIFEST.sha256")
    (custody / "SCOPE_FIREWALL.marker").write_text(
        contract.SCOPE_MARKER + "\n")
    (custody / "WORKER_FINAL_GATE.marker").write_text(
        contract.WORKER_GATE + "\n")
    (custody / "CONTAINMENT_EMPTY.marker").write_text(
        "CONTAINMENT_EMPTY_PASS=1\n")
    (custody / "empty_census.json").write_text("[]\n")
    return {"record_sha": record_sha, "worker": worker,
            "supervisor": supervisor}


def derive(contract, root: Path, live_lease: Path,
           fixture: dict[str, object], job_tag: str = FIX_TAG,
           nonce: str = FIX_NONCE):
    worker = fixture["worker"]
    supervisor = fixture["supervisor"]
    return contract.derive_late_decision(
        root, live_lease, job_tag, nonce, FIX_SOURCE_SHA,
        root / "custody/containment_mode.txt",
        {"pid": worker["pid"], "starttime": worker["starttime"]},
        {"pid": supervisor["pid"], "starttime": supervisor["starttime"]})


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--contract", required=True, type=Path)
    parser.add_argument("--stage-runner", required=True, type=Path)
    parser.add_argument("--worker", required=True, type=Path)
    parser.add_argument("--supervisor", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    contract = load(args.contract.resolve())
    stage_source = args.stage_runner.read_text()
    worker_source = args.worker.read_text()
    supervisor_source = args.supervisor.read_text()
    forbidden = ("start_new_session=True", "os.killpg(process.pid")
    if any(token in stage_source for token in forbidden):
        raise SystemExit("NESTED_STAGE_CONTAINMENT_ESCAPE_PRESENT")
    for token in ("--expected-pgid", "--expected-sid",
                  "SINGULAR_CHILD_CONTAINMENT_DISAGREEMENT",
                  "STAGE_SINGULAR_BINARY_SHA_DISAGREEMENT",
                  "STAGE_SOURCE_ARCHIVE_SHA_DISAGREEMENT",
                  "STAGE_JOB_NONCE_SCHEMA", "identity_sha256"):
        if stage_source.count(token) != 1:
            raise SystemExit("STAGE_CONTAINMENT_TOKEN_CENSUS:" + token)
    for token in ("CANDIDATE_MATHEMATICAL_VERDICT.txt",
                  "WORKER_ARTIFACT_AND_RESOURCE_GATES_PASS=1",
                  "decision-build", "lease-verify",
                  "PGID_FALLBACK_PRODUCTION_SKIPPED",
                  "supervisor_death_watchdog", "singular_binary.sha256",
                  "launch_preflight_copy.sh"):
        if token not in worker_source:
            raise SystemExit("WORKER_FAIL_CLOSED_TOKEN_MISSING:" + token)
    for token in ("worker_rc", "CONTAINMENT_EMPTY_PASS=1",
                  "--archive-ready", "--swap-violation",
                  "--whole-timeout", "--launcher-reap-failure",
                  "--manifest-generator-rc", "archive-extract-verify",
                  "wait-pid", "FINALIZATION_LATCHES.txt", "TERMINAL.marker",
                  "lease-verify", ".supervisor_lease",
                  "RuntimeMaxSec=21600", "KillMode=control-group",
                  "MemorySwapMax=0", "systemd_runtime_fault",
                  "--fresh-root", "publish_no_replace",
                  "TERMINAL_DIRS.list"):
        if token not in supervisor_source:
            raise SystemExit("SUPERVISOR_FAIL_CLOSED_TOKEN_MISSING:" + token)
    if '-s "$cgroup_path/cgroup.procs"' in supervisor_source:
        raise SystemExit("CGROUP_PSEUDOFILE_SIZE_TEST_STILL_PRESENT")
    if 'mv "$decision_tmp" "$terminal_marker"' in supervisor_source:
        raise SystemExit("REPLACING_MARKER_PUBLICATION_STILL_PRESENT")
    if "--candidate" in supervisor_source:
        raise SystemExit("LIVE_CANDIDATE_DECISION_ARGUMENT_STILL_PRESENT")

    clean_gates = dict(
        worker_rc=0, swap_zero=True, swap_violation=False,
        whole_timeout=False, containment_preflight_failure=False,
        launcher_reap_failure=False, systemd_final_fault=False,
        systemd_runtime_fault=False, scope_ok=True, containment_empty=True,
        artifact_ok=True, manifest_generator_ok=True, manifest_replay_ok=True,
        archive_replay_ok=True, archive_ready=True, systemd_mode_ok=True,
        runtime_limits_ok=True, lease_ok=True, decision_ok=True)
    clean = contract.decide_terminal(DEAD, **clean_gates)
    if clean not in contract.MATH_TERMINALS:
        raise SystemExit("CLEAN_MATHEMATICAL_PROMOTION_REJECTED")
    foreign = contract.decide_terminal(
        "EXACT_ENDPOINT_DEAD_ON_NODE1_PROPER_OPEN_ONLY", **clean_gates)
    if foreign != contract.NO_VERDICT:
        raise SystemExit("FOREIGN_CAMPAIGN_CANDIDATE_NOT_REJECTED")
    mutations = {
        "wrong_recorded_pgid": {"containment_empty": False},
        "nonempty_orphan_census": {"containment_empty": False},
        "late_worker_exit": {"worker_rc": 7},
        "late_archive_failure": {"archive_ready": False},
        "missing_scope_marker": {"scope_ok": False},
        "observed_swap_then_final_zero": {"swap_violation": True},
        "whole_timeout_with_worker_rc_zero": {"whole_timeout": True},
        "containment_preflight_failure": {
            "containment_preflight_failure": True},
        "launcher_reap_failure": {"launcher_reap_failure": True},
        "systemd_final_fault": {"systemd_final_fault": True},
        "systemd_runtime_fault": {"systemd_runtime_fault": True},
        "terminal_manifest_generator_failure": {
            "manifest_generator_ok": False},
        "terminal_manifest_replay_failure": {"manifest_replay_ok": False},
        "terminal_archive_replay_failure": {"archive_replay_ok": False},
        "pgid_fallback_mode": {"systemd_mode_ok": False},
        "runtime_limits_unverified": {"runtime_limits_ok": False},
        "lease_binding_failure": {"lease_ok": False},
        "decision_binding_failure": {"decision_ok": False},
    }
    for name, change in mutations.items():
        gates = dict(clean_gates)
        gates.update(change)
        verdict = contract.decide_terminal(DEAD, **gates)
        if verdict != contract.NO_VERDICT:
            raise SystemExit("LATE_FAILURE_NOT_DOWNGRADED:" + name)

    exact_identity = {"pid": 101, "pgid": 101, "sid": 101,
                      "starttime": 999}
    contract.validate_identity_values(exact_identity, exact_identity, "pgid")
    wrong_pgid = dict(exact_identity)
    wrong_pgid["pgid"] = 100
    wrong_pgid_rejected = False
    try:
        contract.validate_identity_values(wrong_pgid, exact_identity, "pgid")
    except RuntimeError as exc:
        wrong_pgid_rejected = "WORKER_IDENTITY_LIVE_DISAGREEMENT" in str(exc)
    if not wrong_pgid_rejected:
        raise SystemExit("WRONG_RECORDED_PGID_NOT_REJECTED")

    exact_pid = {"pid": 202, "state": "S", "starttime": 777,
                 "uid": os.getuid()}
    contract.validate_exact_pid_record(exact_pid, 777)
    wrong_start_rejected = False
    try:
        contract.validate_exact_pid_record(exact_pid, 778)
    except RuntimeError as exc:
        wrong_start_rejected = "PID_IDENTITY_CHANGED_OR_FOREIGN" in str(exc)
    if not wrong_start_rejected:
        raise SystemExit("LAUNCHER_STARTTIME_MUTATION_NOT_REJECTED")
    timed = contract.wait_for_exact_pid_exit(
        202, 777, 0, reader=lambda _pid, _start: exact_pid)
    if timed["ready_to_reap"]:
        raise SystemExit("HUNG_LAUNCHER_BOUND_NOT_ENFORCED")
    zombie = dict(exact_pid, state="Z")
    ready = contract.wait_for_exact_pid_exit(
        202, 777, 0, reader=lambda _pid, _start: zombie)
    if not ready["ready_to_reap"] or ready["terminal_state"] != "ZOMBIE":
        raise SystemExit("ZOMBIE_LAUNCHER_NOT_READY_FOR_IMMEDIATE_WAIT")

    with tempfile.TemporaryDirectory() as temporary:
        temporary_path = Path(temporary)
        empty_census = temporary_path / "empty.json"
        nonempty_census = temporary_path / "nonempty.json"
        empty_census.write_text("[]\n")
        nonempty_census.write_text('[{"pid": 4242}]\n')
        if (not contract.empty_json_list(empty_census)
                or contract.empty_json_list(nonempty_census)):
            raise SystemExit("ORPHAN_CENSUS_PARSER_CONTROL_FAILURE")

        cgroup_empty = temporary_path / "cgroup.empty"
        cgroup_nonempty = temporary_path / "cgroup.nonempty"
        cgroup_malformed = temporary_path / "cgroup.malformed"
        cgroup_missing = temporary_path / "cgroup.missing"
        cgroup_empty.write_text("")
        cgroup_nonempty.write_text("4242\n31337\n")
        cgroup_malformed.write_text("4242\nnot-a-pid\n")
        if contract.parse_cgroup_procs(cgroup_empty) != []:
            raise SystemExit("EMPTY_CGROUP_PROCS_NOT_EMPTY")
        if contract.parse_cgroup_procs(cgroup_nonempty) != [4242, 31337]:
            raise SystemExit("NONEMPTY_CGROUP_PROCS_CENSUS_DRIFT")
        expect_rejection(
            lambda: contract.parse_cgroup_procs(cgroup_malformed),
            "MALFORMED_CGROUP_PROCS", "cgroup-malformed")
        expect_rejection(
            lambda: contract.parse_cgroup_procs(cgroup_missing),
            "FileNotFoundError", "cgroup-missing")

        # ---- nonce and lease controls ---------------------------------
        expect_rejection(lambda: contract.require_nonce(""),
                         "JOB_NONCE_SCHEMA_FAILURE", "empty-nonce")
        expect_rejection(lambda: contract.require_nonce("UPPER_case"),
                         "JOB_NONCE_SCHEMA_FAILURE", "bad-nonce")
        expect_rejection(
            lambda: contract.require_job_tag(
                "ggv_triple02_closed_successor_resume_r2_", "fixturenonce01"),
            "JOB_TAG_COMPOSITION_FAILURE", "empty-suffix-tag")
        lease_root = temporary_path / "lease"
        lease_root.mkdir()
        lease = lease_root / "LEASE.json"
        sidecar = lease_root / "LEASE.sha256"
        contract.build_lease(lease, sidecar, FIX_TAG, FIX_NONCE,
                             FIX_SOURCE_SHA, FIX_LAUNCHER_SHA,
                             FIX_LAUNCH_MANIFEST_SHA, 4000, 100000)
        contract.verify_lease(lease, sidecar, FIX_TAG, FIX_NONCE,
                              FIX_SOURCE_SHA, FIX_LAUNCHER_SHA)
        expect_rejection(
            lambda: contract.verify_lease(lease, sidecar, FIX_TAG, FIX_NONCE,
                                          "f" * 64, FIX_LAUNCHER_SHA),
            "LEASE_BINDING_DISAGREEMENT", "lease-wrong-source")
        expect_rejection(
            lambda: contract.verify_lease(lease, sidecar, FIX_TAG, FIX_NONCE,
                                          FIX_SOURCE_SHA, "9" * 64),
            "LEASE_LAUNCHER_HASH_DISAGREEMENT", "lease-wrong-launcher")
        other_tag = ("ggv_triple02_closed_successor_resume_r2_"
                     "19700101T000000Z_othernonce001")
        expect_rejection(
            lambda: contract.verify_lease(lease, sidecar, other_tag,
                                          "othernonce001", FIX_SOURCE_SHA),
            "LEASE_BINDING_DISAGREEMENT", "lease-wrong-nonce")
        lease_bytes = lease.read_bytes()
        lease.write_bytes(lease_bytes + b"\n")
        expect_rejection(
            lambda: contract.verify_lease(lease, sidecar, FIX_TAG, FIX_NONCE,
                                          FIX_SOURCE_SHA),
            "LEASE_SIDECAR_DISAGREEMENT", "lease-sidecar-tamper")
        lease.write_bytes(lease_bytes)

        # ---- decision record and late authority (C1) ------------------
        decision_root = temporary_path / "decision_root"
        fixture = build_decision_fixture(contract, decision_root)
        derived = derive(contract, decision_root, decision_root / "LEASE.json",
                         fixture)
        if (derived["candidate"] != DEAD
                or derived["decision_sha256"] != fixture["record_sha"]):
            raise SystemExit("LATE_DECISION_POSITIVE_CONTROL_FAILURE")
        custody = decision_root / "custody"
        # Candidate swap before archive freeze: verdict files mutated after
        # the decision record was banked.
        verdict = decision_root / "output/VERDICT.txt"
        original = verdict.read_bytes()
        verdict.write_text(SURVIVOR + "\n")
        expect_rejection(
            lambda: derive(contract, decision_root,
                           decision_root / "LEASE.json", fixture),
            "DECISION_CANDIDATE_ARCHIVE_DISAGREEMENT", "candidate-swap-early")
        verdict.write_bytes(original)
        # Candidate swap after archive freeze: the live candidate file is
        # never read, so mutating (or deleting) it cannot change the derived
        # candidate.
        live_candidate = custody / "CANDIDATE_MATHEMATICAL_VERDICT.txt"
        live_candidate.write_text(SURVIVOR + "\n")
        derived = derive(contract, decision_root,
                         decision_root / "LEASE.json", fixture)
        if derived["candidate"] != DEAD:
            raise SystemExit("LIVE_CANDIDATE_STILL_READ")
        live_candidate.unlink()
        derived = derive(contract, decision_root,
                         decision_root / "LEASE.json", fixture)
        if derived["candidate"] != DEAD:
            raise SystemExit("LIVE_CANDIDATE_DELETION_CHANGED_DECISION")
        live_candidate.write_text(DEAD + "\n")
        # Decision-record tamper breaks the content address.
        record_path = custody / "DECISION_RECORD.json"
        record_bytes = record_path.read_bytes()
        tampered_record = json.loads(record_bytes)
        tampered_record["candidate"] = SURVIVOR
        record_path.write_text(
            json.dumps(tampered_record, indent=2, sort_keys=True) + "\n")
        expect_rejection(
            lambda: derive(contract, decision_root,
                           decision_root / "LEASE.json", fixture),
            "DECISION_SIDECAR_DISAGREEMENT", "decision-record-tamper")
        record_path.write_bytes(record_bytes)
        # Copied decision record from another job: expected nonce differs.
        expect_rejection(
            lambda: derive(contract, decision_root,
                           decision_root / "LEASE.json", fixture,
                           job_tag=other_tag, nonce="othernonce001"),
            "DECISION_JOB_BINDING_DISAGREEMENT", "decision-foreign-job")
        # Live lease disagreement.
        foreign_lease = temporary_path / "foreign_lease.json"
        foreign_lease.write_text("{}\n")
        expect_rejection(
            lambda: derive(contract, decision_root, foreign_lease, fixture),
            "DECISION_LEASE_DISAGREEMENT", "decision-live-lease")
        # Worker identity swap without record update.
        worker_identity = custody / "worker_identity.json"
        worker_bytes = worker_identity.read_bytes()
        swapped = json.loads(worker_bytes)
        swapped["starttime"] = 999999
        worker_identity.write_text(
            json.dumps(swapped, indent=2, sort_keys=True) + "\n")
        expect_rejection(
            lambda: derive(contract, decision_root,
                           decision_root / "LEASE.json", fixture),
            "DECISION_WORKER_IDENTITY_HASH", "decision-worker-identity")
        worker_identity.write_bytes(worker_bytes)
        # PGID fallback can never be promoted.
        mode_path = custody / "containment_mode.txt"
        mode_path.write_text("pgid\n")
        expect_rejection(
            lambda: derive(contract, decision_root,
                           decision_root / "LEASE.json", fixture),
            "DECISION_CONTAINMENT_MODE_DISAGREEMENT", "decision-pgid-mode")
        mode_path.write_text("systemd_scope\n")
        # Unverified runtime limits can never be promoted.
        limits_path = custody / "systemd_runtime_limits.json"
        limits_bytes = limits_path.read_bytes()
        weak = json.loads(limits_bytes)
        weak["runtime_max_usec"] = "infinity"
        weak["verified"] = False
        limits_path.write_text(json.dumps(weak, indent=2, sort_keys=True) + "\n")
        expect_rejection(
            lambda: derive(contract, decision_root,
                           decision_root / "LEASE.json", fixture),
            "DECISION_RUNTIME_LIMITS_DISAGREEMENT", "decision-runtime-limits")
        limits_path.write_bytes(limits_bytes)
        # Artifact-manifest swap.
        manifest_path = custody / "WORKER_ARTIFACT_MANIFEST.sha256"
        manifest_bytes = manifest_path.read_bytes()
        manifest_path.write_text(f"{'f' * 64}  work/production/VERDICT.txt\n")
        expect_rejection(
            lambda: derive(contract, decision_root,
                           decision_root / "LEASE.json", fixture),
            "DECISION_HASH_DISAGREEMENT", "decision-artifact-manifest")
        manifest_path.write_bytes(manifest_bytes)
        # decision-build itself refuses a production/classifier split.
        split_verdict = decision_root / "work/production/VERDICT.txt"
        split_bytes = split_verdict.read_bytes()
        split_verdict.write_text(SURVIVOR + "\n")
        expect_rejection(
            lambda: contract.build_decision_record(
                output_record=temporary_path / "split_record.json",
                output_sidecar=temporary_path / "split_record.sha256",
                job_tag=FIX_TAG, nonce=FIX_NONCE,
                source_archive_sha256=FIX_SOURCE_SHA,
                singular_sha256=FIX_SINGULAR_SHA,
                containment_mode="systemd_scope",
                lease_path=decision_root / "LEASE.json",
                worker_identity_path=custody / "worker_identity.json",
                supervisor_identity_path=custody / "supervisor_identity.json",
                production_dir=decision_root / "work/production",
                classifier_dir=decision_root / "output",
                artifact_manifest=manifest_path),
            "DECISION_PRODUCTION_CLASSIFIER_DISAGREEMENT",
            "decision-build-split-candidate")
        split_verdict.write_bytes(split_bytes)
        # decision-build refuses the pgid mode outright.
        expect_rejection(
            lambda: contract.build_decision_record(
                output_record=temporary_path / "pgid_record.json",
                output_sidecar=temporary_path / "pgid_record.sha256",
                job_tag=FIX_TAG, nonce=FIX_NONCE,
                source_archive_sha256=FIX_SOURCE_SHA,
                singular_sha256=FIX_SINGULAR_SHA, containment_mode="pgid",
                lease_path=decision_root / "LEASE.json",
                worker_identity_path=custody / "worker_identity.json",
                supervisor_identity_path=custody / "supervisor_identity.json",
                production_dir=decision_root / "work/production",
                classifier_dir=decision_root / "output",
                artifact_manifest=manifest_path),
            "DECISION_REQUIRES_SYSTEMD_SCOPE", "decision-build-pgid")

        # ---- terminal CLI end-to-end on the fixture root ---------------
        marker_out = temporary_path / "terminal_marker_content.txt"
        common = [
            sys.executable, str(args.contract.resolve()), "terminal",
            "--fresh-root", str(decision_root),
            "--archive-sha256", "9" * 64,
            "--live-lease", str(decision_root / "LEASE.json"),
            "--job-tag", FIX_TAG, "--job-nonce", FIX_NONCE,
            "--source-archive-sha256", FIX_SOURCE_SHA,
            "--containment-mode-file", str(mode_path),
            "--worker-pid", "4242", "--worker-starttime", "111222",
            "--supervisor-pid", "4100", "--supervisor-starttime", "111000",
            "--swap-total", "0", "--swap-free", "0", "--swap-violation", "0",
            "--whole-timeout", "0", "--containment-preflight-failure", "0",
            "--launcher-reap-failure", "0", "--systemd-final-fault", "0",
            "--systemd-runtime-fault", "0",
            "--scope-marker", str(custody / "SCOPE_FIREWALL.marker"),
            "--worker-gate", str(custody / "WORKER_FINAL_GATE.marker"),
            "--containment-marker", str(custody / "CONTAINMENT_EMPTY.marker"),
            "--pgid-census", str(custody / "empty_census.json"),
            "--tag-census", str(custody / "empty_census.json"),
            "--archive-ready", "1",
            "--manifest-generator-rc", "0", "--manifest-replay-rc", "0",
            "--archive-replay-rc", "0", "--output", str(marker_out),
        ]
        clean_cli = subprocess.run(common + ["--worker-rc", "0"],
                                   check=False, capture_output=True, text=True)
        marker_lines = marker_out.read_text().splitlines()
        if (clean_cli.returncode != 0 or marker_lines[0] != DEAD
                or marker_lines[1] != "TERMINAL_ARCHIVE_SHA256=" + "9" * 64
                or marker_lines[2] != "DECISION_RECORD_SHA256="
                + str(fixture["record_sha"])):
            raise SystemExit("CLEAN_TERMINAL_CLI_CONTROL_FAILURE")
        late_cli = subprocess.run(common + ["--worker-rc", "7"],
                                  check=False, capture_output=True, text=True)
        if (late_cli.returncode != 3
                or marker_out.read_text().splitlines()[0]
                != contract.NO_VERDICT):
            raise SystemExit("LATE_WORKER_EXIT_CLI_NOT_DOWNGRADED")
        orphan_args = list(common)
        orphan_args[orphan_args.index(str(custody / "empty_census.json"),
                                      orphan_args.index("--tag-census"))] = (
            str(nonempty_census))
        orphan_cli = subprocess.run(orphan_args + ["--worker-rc", "0"],
                                    check=False, capture_output=True,
                                    text=True)
        if (orphan_cli.returncode != 3
                or marker_out.read_text().splitlines()[0]
                != contract.NO_VERDICT):
            raise SystemExit("NONEMPTY_ORPHAN_CLI_NOT_DOWNGRADED")
        for name, flag in (("swap_latch", "--swap-violation"),
                           ("whole_timeout", "--whole-timeout"),
                           ("runtime_fault", "--systemd-runtime-fault")):
            hostile_args = list(common)
            hostile_args[hostile_args.index(flag) + 1] = "1"
            hostile_cli = subprocess.run(
                hostile_args + ["--worker-rc", "0"],
                check=False, capture_output=True, text=True)
            if (hostile_cli.returncode != 3
                    or marker_out.read_text().splitlines()[0]
                    != contract.NO_VERDICT):
                raise SystemExit("STICKY_LATCH_NOT_DOWNGRADED:" + name)
        no_archive_args = [
            value for value in common
            if value not in ("--fresh-root", str(decision_root),
                             "--archive-sha256", "9" * 64)]
        archive_index = no_archive_args.index("--archive-ready") + 1
        no_archive_args[archive_index] = "0"
        no_archive_cli = subprocess.run(
            no_archive_args + ["--worker-rc", "0"],
            check=False, capture_output=True, text=True)
        no_archive_lines = marker_out.read_text().splitlines()
        if (no_archive_cli.returncode != 3
                or no_archive_lines[0] != contract.NO_VERDICT
                or no_archive_lines[1] != "TERMINAL_ARCHIVE_SHA256=NONE"):
            raise SystemExit("MISSING_ARCHIVE_CLI_NOT_DOWNGRADED")

        # ---- no-replace publication (terminal collision) ---------------
        publish_target = temporary_path / "TERMINAL.marker"
        contract.publish_no_replace(publish_target, "first\n")
        expect_rejection(
            lambda: contract.publish_no_replace(publish_target, "second\n"),
            "TERMINAL_ALREADY_PUBLISHED", "terminal-collision")
        if publish_target.read_text() != "first\n":
            raise SystemExit("PUBLICATION_REPLACED_EXISTING_MARKER")

        # ---- complete manifest with directory exactness ----------------
        manifest_root = temporary_path / "manifest_root"
        for directory in ("source", "work", "custody", "output"):
            (manifest_root / directory).mkdir(parents=True)
        (manifest_root / "source" / "source.txt").write_text("source\n")
        (manifest_root / "work" / "work.txt").write_text("work\n")
        (manifest_root / "custody" / "evidence.txt").write_text("evidence\n")
        (manifest_root / "output" / "result.txt").write_text("result\n")
        (manifest_root / "source_archive.tar.gz").write_bytes(b"source archive")
        includes = ["source", "source_archive.tar.gz", "work", "custody",
                    "output"]
        dirs_relative = "custody/TERMINAL_DIRS.list"
        terminal_manifest = manifest_root / "custody" / "TERMINAL_MANIFEST.sha256"
        files, dirs = contract.build_complete_manifest(
            manifest_root, terminal_manifest, includes, dirs_relative)
        if (files != 6 or dirs != 4
                or contract.verify_complete_manifest(
                    manifest_root, terminal_manifest, includes,
                    dirs_relative) != (6, 4)):
            raise SystemExit("COMPLETE_TERMINAL_MANIFEST_POSITIVE_FAILURE")
        expect_rejection(
            lambda: contract.build_complete_manifest(
                manifest_root, terminal_manifest, includes + ["missing"],
                dirs_relative),
            "MANIFEST_INCLUDE_MISSING", "manifest-missing-include")
        files, dirs = contract.build_complete_manifest(
            manifest_root, terminal_manifest, includes, dirs_relative)

        good_archive = temporary_path / "good_terminal.tar.gz"
        with tarfile.open(good_archive, "w:gz") as archive:
            for include in includes:
                archive.add(manifest_root / include, arcname=include)
        replay = temporary_path / "good_replay"
        if contract.extract_and_verify_archive(
                good_archive, replay, "custody/TERMINAL_MANIFEST.sha256",
                includes, dirs_relative) != (6, 4):
            raise SystemExit("TERMINAL_ARCHIVE_POSITIVE_REPLAY_FAILURE")

        (manifest_root / "work" / "work.txt").write_text("tampered\n")
        expect_rejection(
            lambda: contract.verify_complete_manifest(
                manifest_root, terminal_manifest, includes, dirs_relative),
            "TERMINAL_MANIFEST_HASH_DRIFT", "manifest-tamper")
        bad_archive = temporary_path / "outer_hash_valid_embedded_bad.tar.gz"
        with tarfile.open(bad_archive, "w:gz") as archive:
            for include in includes:
                archive.add(manifest_root / include, arcname=include)
        expect_rejection(
            lambda: contract.extract_and_verify_archive(
                bad_archive, temporary_path / "bad_replay",
                "custody/TERMINAL_MANIFEST.sha256", includes, dirs_relative),
            "TERMINAL_MANIFEST_HASH_DRIFT", "embedded-manifest-tamper")
        (manifest_root / "work" / "work.txt").write_text("work\n")

        extra_archive = temporary_path / "unexpected_member.tar.gz"
        unexpected = temporary_path / "unexpected.txt"
        unexpected.write_text("not preregistered\n")
        with tarfile.open(extra_archive, "w:gz") as archive:
            for include in includes:
                archive.add(manifest_root / include, arcname=include)
            archive.add(unexpected, arcname="work/unexpected.txt")
        expect_rejection(
            lambda: contract.extract_and_verify_archive(
                extra_archive, temporary_path / "extra_replay",
                "custody/TERMINAL_MANIFEST.sha256", includes, dirs_relative),
            "ARCHIVE_REGULAR_MEMBER_CENSUS_DRIFT", "regular-extra-member")
        # New R2 fixture: an unmanifested EMPTY DIRECTORY under an allowed
        # include must refuse (this was accepted by R1).
        empty_dir_archive = temporary_path / "empty_dir_member.tar.gz"
        stray_dir = temporary_path / "stray_empty_dir"
        stray_dir.mkdir()
        with tarfile.open(empty_dir_archive, "w:gz") as archive:
            for include in includes:
                archive.add(manifest_root / include, arcname=include)
            archive.add(stray_dir, arcname="work/stray_empty_dir")
        expect_rejection(
            lambda: contract.extract_and_verify_archive(
                empty_dir_archive, temporary_path / "empty_dir_replay",
                "custody/TERMINAL_MANIFEST.sha256", includes, dirs_relative),
            "ARCHIVE_DIRECTORY_CENSUS_DRIFT", "empty-directory-extra")

        detached = subprocess.Popen(
            [sys.executable, "-c", "import time; time.sleep(5)"],
            start_new_session=True)
        try:
            if contract.child_in_containment(
                    os.getpgid(detached.pid), os.getsid(detached.pid),
                    os.getpgrp(), os.getsid(0)):
                raise SystemExit("DETACHED_CHILD_FIXTURE_NOT_DETACHED")
        finally:
            detached.terminate()
            detached.wait(timeout=5)
        output = temporary_path / "fixture.json"
        output.write_text(json.dumps({
            "clean_promotion": clean,
            "decision_record_sha256": fixture["record_sha"],
            "detached_child_rejected": True,
            "cgroup_procs_content_controls": True,
            "bounded_launcher_reap_controls": True,
            "complete_manifest_archive_and_directory_controls": True,
            "no_replace_publication_controls": True,
            "lease_and_nonce_controls": True,
            "late_decision_controls": True,
            "nonempty_orphan_census_rejected": True,
            "late_failure_mutations": sorted(mutations),
            "fixture_realism": ("pure/parser-level only; no launcher, "
                                "supervisor, stage-runner, systemd, or live "
                                "/proc execution"),
        }, indent=2, sort_keys=True) + "\n")
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(output.read_bytes())
    print("DETACHED_CHILD_NEGATIVE_CONTROL_PASS=1")
    print("WRONG_RECORDED_PGID_NEGATIVE_CONTROL_PASS=1")
    print("NONEMPTY_ORPHAN_CENSUS_NEGATIVE_CONTROL_PASS=1")
    print("CGROUP_PROCS_CONTENT_NEGATIVE_CONTROL_PASS=1")
    print("BOUNDED_LAUNCHER_REAP_NEGATIVE_CONTROL_PASS=1")
    print("STICKY_SWAP_AND_WHOLE_TIMEOUT_NEGATIVE_CONTROLS_PASS=1")
    print("STICKY_RUNTIME_FAULT_NEGATIVE_CONTROL_PASS=1")
    print("COMPLETE_TERMINAL_MANIFEST_REPLAY_CONTROLS_PASS=1")
    print("VALID_OUTER_HASH_BAD_EMBEDDED_MANIFEST_REJECTED=1")
    print("UNEXPECTED_REGULAR_ARCHIVE_MEMBER_REJECTED=1")
    print("UNMANIFESTED_EMPTY_DIRECTORY_REJECTED=1")
    print("NONZERO_LATE_WORKER_EXIT_NEGATIVE_CONTROL_PASS=1")
    print("LATE_ARCHIVE_FAILURE_NEGATIVE_CONTROL_PASS=1")
    print("EMPTY_AND_MALFORMED_NONCE_REJECTED=1")
    print("LEASE_BINDING_CONTROLS_PASS=1")
    print("DECISION_RECORD_BINDING_CONTROLS_PASS=1")
    print("CANDIDATE_SWAP_BEFORE_ARCHIVE_REJECTED=1")
    print("CANDIDATE_SWAP_AFTER_ARCHIVE_INERT=1")
    print("LIVE_CANDIDATE_NEVER_READ_CONTROL_PASS=1")
    print("COPIED_DECISION_RECORD_REJECTED=1")
    print("PGID_FALLBACK_PROMOTION_REJECTED=1")
    print("RUNTIME_LIMITS_PROMOTION_GATE_PASS=1")
    print("TERMINAL_COLLISION_NO_REPLACE_PASS=1")
    print("TERMINAL_MARKER_ARCHIVE_AND_DECISION_BINDING_PASS=1")
    print("CONTAINMENT_AND_TERMINAL_SELFCHECK_PASS=1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
