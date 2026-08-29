#!/usr/bin/env python3
"""Light, no-CAS custody fixtures for containment and late promotion."""

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


def load(path: Path):
    spec = importlib.util.spec_from_file_location("containment_contract", path)
    if spec is None or spec.loader is None:
        raise SystemExit("CONTRACT_IMPORT_FAILURE")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


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
                  "SINGULAR_CHILD_CONTAINMENT_DISAGREEMENT"):
        if stage_source.count(token) != 1:
            raise SystemExit("STAGE_CONTAINMENT_TOKEN_CENSUS:" + token)
    for token in ("CANDIDATE_MATHEMATICAL_VERDICT.txt",
                  "WORKER_ARTIFACT_AND_RESOURCE_GATES_PASS=1"):
        if token not in worker_source:
            raise SystemExit("WORKER_FAIL_CLOSED_TOKEN_MISSING:" + token)
    for token in ("worker_rc", "CONTAINMENT_EMPTY_PASS=1",
                  "--archive-ready", "--swap-violation",
                  "--whole-timeout", "--launcher-reap-failure",
                  "--manifest-generator-rc", "archive-extract-verify",
                  "wait-pid", "FINALIZATION_LATCHES.txt", "TERMINAL.marker"):
        if token not in supervisor_source:
            raise SystemExit("SUPERVISOR_FAIL_CLOSED_TOKEN_MISSING:" + token)
    if '-s "$cgroup_path/cgroup.procs"' in supervisor_source:
        raise SystemExit("CGROUP_PSEUDOFILE_SIZE_TEST_STILL_PRESENT")

    clean_gates = dict(
        worker_rc=0, swap_zero=True, swap_violation=False,
        whole_timeout=False, containment_preflight_failure=False,
        launcher_reap_failure=False, systemd_final_fault=False,
        scope_ok=True, containment_empty=True, artifact_ok=True,
        manifest_generator_ok=True, manifest_replay_ok=True,
        archive_replay_ok=True, archive_ready=True)
    clean = contract.decide_terminal(
        "EXACT_ENDPOINT_DEAD_ON_NODE1_PROPER_OPEN_ONLY", **clean_gates)
    if clean not in contract.MATH_TERMINALS:
        raise SystemExit("CLEAN_MATHEMATICAL_PROMOTION_REJECTED")
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
        "terminal_manifest_generator_failure": {
            "manifest_generator_ok": False},
        "terminal_manifest_replay_failure": {"manifest_replay_ok": False},
        "terminal_archive_replay_failure": {"archive_replay_ok": False},
    }
    for name, change in mutations.items():
        gates = dict(clean_gates)
        gates.update(change)
        verdict = contract.decide_terminal(
            "EXACT_ENDPOINT_DEAD_ON_NODE1_PROPER_OPEN_ONLY", **gates)
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
        empty_census = Path(temporary) / "empty.json"
        nonempty_census = Path(temporary) / "nonempty.json"
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
        malformed_rejected = False
        try:
            contract.parse_cgroup_procs(cgroup_malformed)
        except RuntimeError as exc:
            malformed_rejected = "MALFORMED_CGROUP_PROCS" in str(exc)
        if not malformed_rejected:
            raise SystemExit("MALFORMED_CGROUP_PROCS_NOT_REJECTED")
        missing_rejected = False
        try:
            contract.parse_cgroup_procs(cgroup_missing)
        except FileNotFoundError:
            missing_rejected = True
        if not missing_rejected:
            raise SystemExit("MISSING_CGROUP_PROCS_NOT_REJECTED")
        candidate = temporary_path / "candidate.txt"
        scope = temporary_path / "scope.marker"
        worker_gate = temporary_path / "worker.marker"
        containment = temporary_path / "containment.marker"
        candidate.write_text("EXACT_ENDPOINT_DEAD_ON_NODE1_PROPER_OPEN_ONLY\n")
        scope.write_text(contract.SCOPE_MARKER + "\n")
        worker_gate.write_text(contract.WORKER_GATE + "\n")
        containment.write_text("CONTAINMENT_EMPTY_PASS=1\n")
        common = [
            sys.executable, str(args.contract.resolve()), "terminal",
            "--candidate", str(candidate), "--swap-total", "0",
            "--swap-free", "0", "--swap-violation", "0",
            "--whole-timeout", "0", "--containment-preflight-failure", "0",
            "--launcher-reap-failure", "0", "--systemd-final-fault", "0",
            "--scope-marker", str(scope),
            "--worker-gate", str(worker_gate), "--containment-marker",
            str(containment), "--pgid-census", str(empty_census),
            "--tag-census", str(empty_census), "--archive-ready", "1",
            "--manifest-generator-rc", "0", "--manifest-replay-rc", "0",
            "--archive-replay-rc", "0",
        ]
        clean_output = temporary_path / "clean_terminal.txt"
        clean_cli = subprocess.run(
            common + ["--worker-rc", "0", "--output", str(clean_output)],
            check=False, capture_output=True, text=True)
        if (clean_cli.returncode != 0
                or clean_output.read_text().strip() not in contract.MATH_TERMINALS):
            raise SystemExit("CLEAN_TERMINAL_CLI_CONTROL_FAILURE")
        late_output = temporary_path / "late_terminal.txt"
        late_cli = subprocess.run(
            common + ["--worker-rc", "7", "--output", str(late_output)],
            check=False, capture_output=True, text=True)
        if (late_cli.returncode != 3
                or late_output.read_text().strip() != contract.NO_VERDICT):
            raise SystemExit("LATE_WORKER_EXIT_CLI_NOT_DOWNGRADED")
        orphan_output = temporary_path / "orphan_terminal.txt"
        orphan_args = list(common)
        orphan_args[orphan_args.index(str(empty_census),
                                      orphan_args.index("--tag-census"))] = str(nonempty_census)
        orphan_cli = subprocess.run(
            orphan_args + ["--worker-rc", "0", "--output", str(orphan_output)],
            check=False, capture_output=True, text=True)
        if (orphan_cli.returncode != 3
                or orphan_output.read_text().strip() != contract.NO_VERDICT):
            raise SystemExit("NONEMPTY_ORPHAN_CLI_NOT_DOWNGRADED")
        for name, flag in (("swap_latch", "--swap-violation"),
                           ("whole_timeout", "--whole-timeout")):
            hostile_args = list(common)
            hostile_args[hostile_args.index(flag) + 1] = "1"
            hostile_output = temporary_path / f"{name}.terminal.txt"
            hostile_cli = subprocess.run(
                hostile_args + ["--worker-rc", "0", "--output",
                                str(hostile_output)],
                check=False, capture_output=True, text=True)
            if (hostile_cli.returncode != 3
                    or hostile_output.read_text().strip() != contract.NO_VERDICT):
                raise SystemExit("STICKY_LATCH_NOT_DOWNGRADED:" + name)

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
        terminal_manifest = manifest_root / "custody" / "TERMINAL_MANIFEST.sha256"
        manifest_count = contract.build_complete_manifest(
            manifest_root, terminal_manifest, includes)
        if (manifest_count != 5
                or contract.verify_complete_manifest(
                    manifest_root, terminal_manifest, includes) != 5):
            raise SystemExit("COMPLETE_TERMINAL_MANIFEST_POSITIVE_FAILURE")
        generator_failure_rejected = False
        try:
            contract.build_complete_manifest(
                manifest_root, terminal_manifest, includes + ["missing"])
        except RuntimeError as exc:
            generator_failure_rejected = "MANIFEST_INCLUDE_MISSING" in str(exc)
        if not generator_failure_rejected:
            raise SystemExit("TERMINAL_MANIFEST_GENERATOR_FAILURE_NOT_REJECTED")

        good_archive = temporary_path / "good_terminal.tar.gz"
        with tarfile.open(good_archive, "w:gz") as archive:
            for include in includes:
                archive.add(manifest_root / include, arcname=include)
        replay = temporary_path / "good_replay"
        if contract.extract_and_verify_archive(
                good_archive, replay, "custody/TERMINAL_MANIFEST.sha256",
                includes) != 5:
            raise SystemExit("TERMINAL_ARCHIVE_POSITIVE_REPLAY_FAILURE")

        (manifest_root / "work" / "work.txt").write_text("tampered\n")
        completeness_rejected = False
        try:
            contract.verify_complete_manifest(
                manifest_root, terminal_manifest, includes)
        except RuntimeError as exc:
            completeness_rejected = "TERMINAL_MANIFEST_HASH_DRIFT" in str(exc)
        if not completeness_rejected:
            raise SystemExit("TERMINAL_MANIFEST_TAMPER_NOT_REJECTED")
        bad_archive = temporary_path / "outer_hash_valid_embedded_bad.tar.gz"
        with tarfile.open(bad_archive, "w:gz") as archive:
            for include in includes:
                archive.add(manifest_root / include, arcname=include)
        outer_digest = hashlib.sha256(bad_archive.read_bytes()).hexdigest()
        if len(outer_digest) != 64:
            raise SystemExit("OUTER_ARCHIVE_HASH_FIXTURE_FAILURE")
        embedded_bad_rejected = False
        try:
            contract.extract_and_verify_archive(
                bad_archive, temporary_path / "bad_replay",
                "custody/TERMINAL_MANIFEST.sha256", includes)
        except RuntimeError as exc:
            embedded_bad_rejected = "TERMINAL_MANIFEST_HASH_DRIFT" in str(exc)
        if not embedded_bad_rejected:
            raise SystemExit("VALID_OUTER_HASH_BAD_EMBEDDED_MANIFEST_ACCEPTED")
        extra_archive = temporary_path / "unexpected_member.tar.gz"
        unexpected = temporary_path / "unexpected.txt"
        unexpected.write_text("not preregistered\n")
        with tarfile.open(extra_archive, "w:gz") as archive:
            for include in includes:
                archive.add(manifest_root / include, arcname=include)
            archive.add(unexpected, arcname="unexpected.txt")
        extra_rejected = False
        try:
            contract.extract_and_verify_archive(
                extra_archive, temporary_path / "extra_replay",
                "custody/TERMINAL_MANIFEST.sha256", includes)
        except RuntimeError as exc:
            extra_rejected = "ARCHIVE_UNSAFE_DUPLICATE_OR_EXTRA" in str(exc)
        if not extra_rejected:
            raise SystemExit("UNEXPECTED_ARCHIVE_MEMBER_NOT_REJECTED")
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
            "detached_child_rejected": True,
            "cgroup_procs_content_controls": True,
            "bounded_launcher_reap_controls": True,
            "complete_manifest_and_archive_controls": True,
            "nonempty_orphan_census_rejected": True,
            "late_failure_mutations": sorted(mutations),
        }, indent=2, sort_keys=True) + "\n")
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(output.read_bytes())
    print("DETACHED_CHILD_NEGATIVE_CONTROL_PASS=1")
    print("WRONG_RECORDED_PGID_NEGATIVE_CONTROL_PASS=1")
    print("NONEMPTY_ORPHAN_CENSUS_NEGATIVE_CONTROL_PASS=1")
    print("CGROUP_PROCS_CONTENT_NEGATIVE_CONTROL_PASS=1")
    print("BOUNDED_LAUNCHER_REAP_NEGATIVE_CONTROL_PASS=1")
    print("STICKY_SWAP_AND_WHOLE_TIMEOUT_NEGATIVE_CONTROLS_PASS=1")
    print("COMPLETE_TERMINAL_MANIFEST_REPLAY_CONTROLS_PASS=1")
    print("VALID_OUTER_HASH_BAD_EMBEDDED_MANIFEST_REJECTED=1")
    print("NONZERO_LATE_WORKER_EXIT_NEGATIVE_CONTROL_PASS=1")
    print("LATE_ARCHIVE_FAILURE_NEGATIVE_CONTROL_PASS=1")
    print("CONTAINMENT_AND_TERMINAL_SELFCHECK_PASS=1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
