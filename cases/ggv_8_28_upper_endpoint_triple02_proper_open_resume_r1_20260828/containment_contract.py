#!/usr/bin/env python3
"""Fail-closed Linux process-custody and terminal-promotion helpers."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import signal
import tarfile
import time


MATH_TERMINALS = {
    "EXACT_ENDPOINT_DEAD_ON_NODE1_PROPER_OPEN_ONLY",
    ("RING_LEVEL_ENDPOINT_NONZERO_ON_NODE1_PROPER_OPEN_"
     "PENDING_NILPOTENCE_RADICAL"),
}
NO_VERDICT = "CUSTODY_OR_ADAPTER_FAILURE_NO_VERDICT"
SCOPE_MARKER = "OPEN_RESULT_BANKED_WITHOUT_CLOSED_SUCCESSOR_OR_WHOLE_STRATUM_PROMOTION"
WORKER_GATE = "WORKER_ARTIFACT_AND_RESOURCE_GATES_PASS=1"
SHA_LINE = re.compile(r"([0-9a-f]{64})  ([^\n]+)")


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + f".tmp.{os.getpid()}")
    with temporary.open("w") as handle:
        handle.write(text)
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(temporary, path)


def read_identity(pid: int) -> dict[str, object]:
    stat = Path(f"/proc/{pid}/stat").read_text()
    close = stat.rfind(")")
    if close < 0:
        raise RuntimeError("MALFORMED_PROC_STAT")
    fields = stat[close + 2:].split()
    status = Path(f"/proc/{pid}/status").read_text().splitlines()
    uid_line = next(line for line in status if line.startswith("Uid:"))
    return {
        "pid": pid,
        "state": fields[0],
        "ppid": int(fields[1]),
        "pgid": int(fields[2]),
        "sid": int(fields[3]),
        "starttime": int(fields[19]),
        "uid": int(uid_line.split()[1]),
    }


def has_job_tag(pid: int, job_tag: str) -> bool:
    try:
        environ = Path(f"/proc/{pid}/environ").read_bytes().split(b"\0")
    except (FileNotFoundError, PermissionError, ProcessLookupError):
        return False
    needle = b"JOB_TAG=" + job_tag.encode()
    return needle in environ


def process_records(pgid: int, job_tag: str,
                    exclude: set[int]) -> tuple[list[dict[str, object]],
                                                list[dict[str, object]]]:
    pgid_records: list[dict[str, object]] = []
    tag_records: list[dict[str, object]] = []
    for entry in Path("/proc").iterdir():
        if not entry.name.isdigit():
            continue
        pid = int(entry.name)
        if pid in exclude or pid == os.getpid():
            continue
        try:
            identity = read_identity(pid)
        except (FileNotFoundError, PermissionError, ProcessLookupError,
                StopIteration, RuntimeError, ValueError):
            continue
        if pgid > 1 and identity["pgid"] == pgid:
            pgid_records.append(identity)
        if has_job_tag(pid, job_tag):
            tag_records.append(identity)
    return pgid_records, tag_records


def signal_exact(record: dict[str, object], sig: signal.Signals) -> None:
    try:
        current = read_identity(record["pid"])
    except (FileNotFoundError, ProcessLookupError):
        return
    if (current["starttime"] != record["starttime"]
            or current["uid"] != os.getuid()):
        raise RuntimeError("PID_IDENTITY_CHANGED_OR_FOREIGN")
    os.kill(record["pid"], sig)


def exact_pid_record(pid: int, starttime: int) -> dict[str, object] | None:
    """Return the live same-uid PID identity, or None only when it is absent."""
    try:
        current = read_identity(pid)
    except (FileNotFoundError, ProcessLookupError):
        return None
    validate_exact_pid_record(current, starttime)
    return current


def validate_exact_pid_record(current: dict[str, object],
                              starttime: int) -> None:
    if (current.get("starttime") != starttime
            or current.get("uid") != os.getuid()):
        raise RuntimeError("PID_IDENTITY_CHANGED_OR_FOREIGN")


def wait_for_exact_pid_exit(pid: int, starttime: int, timeout: float,
                            interval: float = 0.05,
                            reader=None) -> dict[str, object]:
    """Bounded poll: absent or zombie is safe for the parent shell to wait."""
    if timeout < 0 or interval <= 0:
        raise ValueError("INVALID_PID_WAIT_BOUND")
    if reader is None:
        reader = exact_pid_record
    deadline = time.monotonic() + timeout
    while True:
        current = reader(pid, starttime)
        if current is None:
            return {"ready_to_reap": True, "terminal_state": "ABSENT"}
        if current["state"] == "Z":
            return {"ready_to_reap": True, "terminal_state": "ZOMBIE"}
        if time.monotonic() >= deadline:
            return {"ready_to_reap": False,
                    "terminal_state": str(current["state"])}
        time.sleep(interval)


def signal_exact_pid(pid: int, starttime: int,
                     sig: signal.Signals) -> None:
    current = exact_pid_record(pid, starttime)
    if current is not None:
        signal_exact(current, sig)


def terminate_and_census(pgid: int, job_tag: str, exclude: set[int],
                         pgid_output: Path, tag_output: Path) -> bool:
    if pgid > 1 and pgid != os.getpgrp():
        try:
            os.killpg(pgid, signal.SIGTERM)
        except ProcessLookupError:
            pass
    for sig, pause in ((signal.SIGTERM, 1.0), (signal.SIGKILL, 0.25)):
        pgid_records, tag_records = process_records(pgid, job_tag, exclude)
        combined = {record["pid"]: record
                    for record in pgid_records + tag_records}
        for record in combined.values():
            try:
                signal_exact(record, sig)
            except ProcessLookupError:
                pass
        if combined:
            time.sleep(pause)
    pgid_records, tag_records = process_records(pgid, job_tag, exclude)
    atomic_write(pgid_output,
                 json.dumps(pgid_records, indent=2, sort_keys=True) + "\n")
    atomic_write(tag_output,
                 json.dumps(tag_records, indent=2, sort_keys=True) + "\n")
    return not pgid_records and not tag_records


def validate_identity_values(identity: dict[str, object],
                             current: dict[str, int], mode: str) -> None:
    required = ("pid", "pgid", "sid", "starttime")
    if any(not isinstance(identity.get(key), int) for key in required):
        raise RuntimeError("WORKER_IDENTITY_SCHEMA")
    if any(current[key] != identity[key] for key in required):
        raise RuntimeError("WORKER_IDENTITY_LIVE_DISAGREEMENT")
    if mode == "pgid" and not (
            identity["pid"] == identity["pgid"] == identity["sid"]):
        raise RuntimeError("PGID_FALLBACK_NOT_SESSION_LEADER")
    if mode not in {"pgid", "systemd_scope"}:
        raise RuntimeError("UNKNOWN_CONTAINMENT_MODE")


def validate_worker_identity(identity: dict[str, object], mode: str) -> None:
    if not isinstance(identity.get("pid"), int):
        raise RuntimeError("WORKER_IDENTITY_SCHEMA")
    current = read_identity(int(identity["pid"]))
    validate_identity_values(identity, current, mode)


def child_in_containment(child_pgid: int, child_sid: int,
                         expected_pgid: int, expected_sid: int) -> bool:
    return child_pgid == expected_pgid and child_sid == expected_sid


def exact_line(path: Path, expected: str) -> bool:
    try:
        return path.read_text() == expected + "\n"
    except (FileNotFoundError, OSError):
        return False


def empty_json_list(path: Path) -> bool:
    try:
        value = json.loads(path.read_text())
    except (FileNotFoundError, OSError, json.JSONDecodeError):
        return False
    return value == []


def parse_cgroup_procs(path: Path) -> list[int]:
    """Read and strictly parse cgroup.procs; metadata size is never used."""
    text = path.read_text()
    pids = []
    for number, raw in enumerate(text.splitlines(), 1):
        value = raw.strip()
        if not value:
            continue
        if not value.isascii() or not value.isdecimal() or int(value) <= 0:
            raise RuntimeError(f"MALFORMED_CGROUP_PROCS_LINE_{number}")
        pids.append(int(value))
    return sorted(set(pids))


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def safe_relative(value: str) -> Path:
    relative = Path(value)
    if relative.is_absolute() or not relative.parts or ".." in relative.parts:
        raise RuntimeError("UNSAFE_RELATIVE_PATH")
    return relative


def manifest_files(root: Path, includes: list[str],
                   manifest_relative: str) -> list[Path]:
    excluded = safe_relative(manifest_relative)
    paths: set[Path] = set()
    for value in includes:
        relative = safe_relative(value)
        candidate = root / relative
        if candidate.is_symlink() or not candidate.exists():
            raise RuntimeError("MANIFEST_INCLUDE_MISSING_OR_SYMLINK:" + value)
        if candidate.is_file():
            descendants = [candidate]
        elif candidate.is_dir():
            descendants = sorted(candidate.rglob("*"))
        else:
            raise RuntimeError("MANIFEST_INCLUDE_NOT_FILE_OR_DIRECTORY:" + value)
        for path in descendants:
            member = path.relative_to(root)
            if member == excluded:
                continue
            if path.is_symlink():
                raise RuntimeError("MANIFEST_MEMBER_SYMLINK:" + member.as_posix())
            if path.is_dir():
                continue
            if not path.is_file():
                raise RuntimeError("MANIFEST_MEMBER_NOT_REGULAR:" + member.as_posix())
            paths.add(member)
    return sorted(paths, key=lambda item: item.as_posix())


def build_complete_manifest(root: Path, manifest: Path,
                            includes: list[str]) -> int:
    root = root.resolve()
    manifest = manifest.resolve()
    manifest_relative = manifest.relative_to(root).as_posix()
    paths = manifest_files(root, includes, manifest_relative)
    lines = [f"{sha256_path(root / path)}  {path.as_posix()}"
             for path in paths]
    atomic_write(manifest, "\n".join(lines) + "\n")
    return len(paths)


def parse_manifest(path: Path) -> dict[str, str]:
    entries: dict[str, str] = {}
    for number, line in enumerate(path.read_text().splitlines(), 1):
        match = SHA_LINE.fullmatch(line)
        if not match:
            raise RuntimeError(f"MALFORMED_MANIFEST_LINE_{number}")
        digest, value = match.groups()
        relative = safe_relative(value).as_posix()
        if relative in entries:
            raise RuntimeError("DUPLICATE_MANIFEST_MEMBER:" + relative)
        entries[relative] = digest
    if not entries:
        raise RuntimeError("EMPTY_TERMINAL_MANIFEST")
    return entries


def verify_complete_manifest(root: Path, manifest: Path,
                             includes: list[str]) -> int:
    root = root.resolve()
    manifest = manifest.resolve()
    manifest_relative = manifest.relative_to(root).as_posix()
    entries = parse_manifest(manifest)
    expected = {path.as_posix()
                for path in manifest_files(root, includes, manifest_relative)}
    if set(entries) != expected:
        missing = sorted(expected - set(entries))
        extra = sorted(set(entries) - expected)
        raise RuntimeError(f"TERMINAL_MANIFEST_CENSUS_DRIFT:{missing}:{extra}")
    for relative, expected_digest in entries.items():
        path = root / safe_relative(relative)
        if path.is_symlink() or not path.is_file():
            raise RuntimeError("TERMINAL_MANIFEST_MEMBER_NOT_REGULAR:" + relative)
        if sha256_path(path) != expected_digest:
            raise RuntimeError("TERMINAL_MANIFEST_HASH_DRIFT:" + relative)
    return len(entries)


def archive_member_allowed(name: str, includes: list[str]) -> bool:
    member = safe_relative(name).as_posix()
    for value in includes:
        include = safe_relative(value).as_posix()
        if member == include or member.startswith(include.rstrip("/") + "/"):
            return True
    return False


def extract_and_verify_archive(archive_path: Path, destination: Path,
                               manifest_relative: str,
                               includes: list[str]) -> int:
    """Reject unsafe/extra members, extract privately, and replay census/hash."""
    if destination.exists():
        raise RuntimeError("ARCHIVE_REPLAY_DESTINATION_EXISTS")
    destination.mkdir(mode=0o700, parents=True)
    manifest_name = safe_relative(manifest_relative).as_posix()
    with tarfile.open(archive_path, "r:gz") as archive:
        members = archive.getmembers()
        names: set[str] = set()
        regular: set[str] = set()
        for member in members:
            name = safe_relative(member.name).as_posix()
            if name in names or not archive_member_allowed(name, includes):
                raise RuntimeError("ARCHIVE_UNSAFE_DUPLICATE_OR_EXTRA:" + name)
            names.add(name)
            if member.isfile():
                regular.add(name)
            elif not member.isdir():
                raise RuntimeError("ARCHIVE_NONREGULAR_MEMBER:" + name)
        if manifest_name not in regular:
            raise RuntimeError("ARCHIVE_MANIFEST_MISSING")
        manifest_member = archive.getmember(manifest_name)
        manifest_handle = archive.extractfile(manifest_member)
        if manifest_handle is None:
            raise RuntimeError("ARCHIVE_MANIFEST_UNREADABLE")
        manifest_text = manifest_handle.read().decode("utf-8")
        temporary_manifest = destination / ".embedded_manifest"
        atomic_write(temporary_manifest, manifest_text)
        manifest_entries = parse_manifest(temporary_manifest)
        temporary_manifest.unlink()
        if regular != set(manifest_entries) | {manifest_name}:
            raise RuntimeError("ARCHIVE_REGULAR_MEMBER_CENSUS_DRIFT")
        for member in members:
            target = destination / safe_relative(member.name)
            if member.isdir():
                target.mkdir(mode=0o700, parents=True, exist_ok=True)
                continue
            target.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
            source = archive.extractfile(member)
            if source is None:
                raise RuntimeError("ARCHIVE_MEMBER_UNREADABLE:" + member.name)
            descriptor = os.open(target, os.O_WRONLY | os.O_CREAT | os.O_EXCL,
                                 0o400)
            with os.fdopen(descriptor, "wb") as output:
                for block in iter(lambda: source.read(1 << 20), b""):
                    output.write(block)
    return verify_complete_manifest(
        destination, destination / safe_relative(manifest_relative), includes)


def decide_terminal(candidate: str | None, *, worker_rc: int,
                    swap_zero: bool, swap_violation: bool,
                    whole_timeout: bool, containment_preflight_failure: bool,
                    launcher_reap_failure: bool, systemd_final_fault: bool,
                    scope_ok: bool,
                    containment_empty: bool, artifact_ok: bool,
                    manifest_generator_ok: bool, manifest_replay_ok: bool,
                    archive_replay_ok: bool, archive_ready: bool) -> str:
    if not all((worker_rc == 0, swap_zero, not swap_violation,
                not whole_timeout, not containment_preflight_failure,
                not launcher_reap_failure, not systemd_final_fault,
                scope_ok, containment_empty,
                artifact_ok, manifest_generator_ok, manifest_replay_ok,
                archive_replay_ok, archive_ready)):
        return NO_VERDICT
    if candidate in MATH_TERMINALS:
        return candidate
    return NO_VERDICT


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    identity_parser = sub.add_parser("validate-worker")
    identity_parser.add_argument("--identity", required=True, type=Path)
    identity_parser.add_argument("--mode", required=True)
    cleanup = sub.add_parser("cleanup")
    cleanup.add_argument("--pgid", required=True, type=int)
    cleanup.add_argument("--job-tag", required=True)
    cleanup.add_argument("--exclude-pid", action="append", default=[], type=int)
    cleanup.add_argument("--pgid-output", required=True, type=Path)
    cleanup.add_argument("--tag-output", required=True, type=Path)
    cgroup = sub.add_parser("cgroup-census")
    cgroup.add_argument("--path", required=True, type=Path)
    cgroup.add_argument("--output", required=True, type=Path)
    pid_start = sub.add_parser("pid-start")
    pid_start.add_argument("--pid", required=True, type=int)
    wait_pid = sub.add_parser("wait-pid")
    wait_pid.add_argument("--pid", required=True, type=int)
    wait_pid.add_argument("--starttime", required=True, type=int)
    wait_pid.add_argument("--timeout", required=True, type=float)
    wait_pid.add_argument("--output", required=True, type=Path)
    signal_pid = sub.add_parser("signal-pid")
    signal_pid.add_argument("--pid", required=True, type=int)
    signal_pid.add_argument("--starttime", required=True, type=int)
    signal_pid.add_argument("--signal", required=True, choices=("TERM", "KILL"))
    manifest_build = sub.add_parser("manifest-build")
    manifest_build.add_argument("--root", required=True, type=Path)
    manifest_build.add_argument("--manifest", required=True, type=Path)
    manifest_build.add_argument("--include", action="append", required=True)
    manifest_verify = sub.add_parser("manifest-verify")
    manifest_verify.add_argument("--root", required=True, type=Path)
    manifest_verify.add_argument("--manifest", required=True, type=Path)
    manifest_verify.add_argument("--include", action="append", required=True)
    archive_verify = sub.add_parser("archive-extract-verify")
    archive_verify.add_argument("--archive", required=True, type=Path)
    archive_verify.add_argument("--destination", required=True, type=Path)
    archive_verify.add_argument("--manifest-relative", required=True)
    archive_verify.add_argument("--include", action="append", required=True)
    terminal = sub.add_parser("terminal")
    terminal.add_argument("--candidate", required=True, type=Path)
    terminal.add_argument("--worker-rc", required=True, type=int)
    terminal.add_argument("--swap-total", required=True, type=int)
    terminal.add_argument("--swap-free", required=True, type=int)
    terminal.add_argument("--swap-violation", required=True, choices=("0", "1"))
    terminal.add_argument("--whole-timeout", required=True, choices=("0", "1"))
    terminal.add_argument("--containment-preflight-failure", required=True,
                          choices=("0", "1"))
    terminal.add_argument("--launcher-reap-failure", required=True,
                          choices=("0", "1"))
    terminal.add_argument("--systemd-final-fault", required=True,
                          choices=("0", "1"))
    terminal.add_argument("--scope-marker", required=True, type=Path)
    terminal.add_argument("--worker-gate", required=True, type=Path)
    terminal.add_argument("--containment-marker", required=True, type=Path)
    terminal.add_argument("--pgid-census", required=True, type=Path)
    terminal.add_argument("--tag-census", required=True, type=Path)
    terminal.add_argument("--archive-ready", required=True, choices=("0", "1"))
    terminal.add_argument("--manifest-generator-rc", required=True, type=int)
    terminal.add_argument("--manifest-replay-rc", required=True, type=int)
    terminal.add_argument("--archive-replay-rc", required=True, type=int)
    terminal.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    if args.command == "validate-worker":
        validate_worker_identity(json.loads(args.identity.read_text()), args.mode)
        print("WORKER_IDENTITY_CONTAINMENT_PASS=1")
        return 0
    if args.command == "cleanup":
        clean = terminate_and_census(
            args.pgid, args.job_tag, set(args.exclude_pid),
            args.pgid_output, args.tag_output)
        print(f"CONTAINMENT_CENSUS_EMPTY={int(clean)}")
        return 0 if clean else 1
    if args.command == "cgroup-census":
        pids = parse_cgroup_procs(args.path)
        atomic_write(args.output, json.dumps(pids, indent=2) + "\n")
        print(f"CGROUP_PROCS_EMPTY={int(not pids)}")
        return 0 if not pids else 1
    if args.command == "pid-start":
        identity = read_identity(args.pid)
        if identity["uid"] != os.getuid():
            raise RuntimeError("PID_IDENTITY_FOREIGN")
        print(identity["starttime"])
        return 0
    if args.command == "wait-pid":
        try:
            result = wait_for_exact_pid_exit(
                args.pid, args.starttime, args.timeout)
        except RuntimeError as error:
            result = {"ready_to_reap": False,
                      "terminal_state": "IDENTITY_FAILURE",
                      "error": str(error)}
            atomic_write(args.output, json.dumps(result, indent=2,
                                                 sort_keys=True) + "\n")
            print("EXACT_PID_IDENTITY_FAILURE=1")
            return 2
        atomic_write(args.output, json.dumps(result, indent=2,
                                             sort_keys=True) + "\n")
        print(f"EXACT_PID_READY_TO_REAP={int(result['ready_to_reap'])}")
        return 0 if result["ready_to_reap"] else 1
    if args.command == "signal-pid":
        signal_exact_pid(args.pid, args.starttime,
                         signal.SIGTERM if args.signal == "TERM"
                         else signal.SIGKILL)
        print("EXACT_PID_SIGNAL_PASS=1")
        return 0
    if args.command == "manifest-build":
        count = build_complete_manifest(args.root, args.manifest, args.include)
        print(f"TERMINAL_MANIFEST_GENERATED_ENTRIES={count}")
        return 0
    if args.command == "manifest-verify":
        count = verify_complete_manifest(args.root, args.manifest, args.include)
        print(f"TERMINAL_MANIFEST_REPLAYED_ENTRIES={count}")
        return 0
    if args.command == "archive-extract-verify":
        count = extract_and_verify_archive(
            args.archive, args.destination, args.manifest_relative,
            args.include)
        print(f"TERMINAL_ARCHIVE_REPLAYED_ENTRIES={count}")
        return 0
    try:
        candidate = args.candidate.read_text().strip()
    except (FileNotFoundError, OSError):
        candidate = None
    classification = decide_terminal(
        candidate, worker_rc=args.worker_rc,
        swap_zero=args.swap_total == 0 and args.swap_free == 0,
        swap_violation=args.swap_violation == "1",
        whole_timeout=args.whole_timeout == "1",
        containment_preflight_failure=(
            args.containment_preflight_failure == "1"),
        launcher_reap_failure=args.launcher_reap_failure == "1",
        systemd_final_fault=args.systemd_final_fault == "1",
        scope_ok=exact_line(args.scope_marker, SCOPE_MARKER),
        containment_empty=(
            exact_line(args.containment_marker, "CONTAINMENT_EMPTY_PASS=1")
            and empty_json_list(args.pgid_census)
            and empty_json_list(args.tag_census)),
        artifact_ok=exact_line(args.worker_gate, WORKER_GATE),
        manifest_generator_ok=args.manifest_generator_rc == 0,
        manifest_replay_ok=args.manifest_replay_rc == 0,
        archive_replay_ok=args.archive_replay_rc == 0,
        archive_ready=args.archive_ready == "1")
    atomic_write(args.output, classification + "\n")
    print(f"FINAL_CLASSIFICATION={classification}")
    return 0 if classification in MATH_TERMINALS else 3


if __name__ == "__main__":
    raise SystemExit(main())
