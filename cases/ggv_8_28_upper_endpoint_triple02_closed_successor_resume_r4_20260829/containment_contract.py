#!/usr/bin/env python3
"""Fail-closed Linux process-custody and terminal-promotion helpers (R4).

R4 repairs relative to the reviewed R3 packet (hostile review O2-B1/
O2-N2/O2-N4):

  O2-B1 The charged terminal archive is opened EXACTLY ONCE.  The late
        authority opens the archive path a single time with O_NOFOLLOW
        (+O_NONBLOCK, so a FIFO at the path cannot block), requires the
        opened object to be a regular file via fstat, streams the outer
        SHA-256 from that descriptor, rewinds it, and hands the SAME open
        object to tarfile (fileobj=...); the extraction walk, the complete
        member/manifest/directory censuses, and every retained-member read
        all complete while that descriptor is held.  No code on the
        authenticated decision path ever reopens the archive path, so a
        concurrent same-uid rename()/replacement of the path cannot
        redirect any decision read (the R3 review's 6/6 promoted race).
        In-place mutation or truncation of the archive inode during the
        read is refused by a pre/post fstat identity/size/mtime/ctime
        stability gate (DECISION_ARCHIVE_UNSTABLE_DURING_READ).  The
        published marker's TERMINAL_ARCHIVE_SHA256 is the digest actually
        computed from that descriptor, never merely the CLI string.
  O2-N2 The archived fault-latch record is type-checked: JSON booleans
        (and any non-int) are refused for worker_rc and for all six sticky
        fault fields; only honest integers pass.
  O2-N4 The terminal CLI always publishes a marker: a malformed late
        --archive-sha256 (or any other late-input failure) downgrades to
        the custody no-verdict marker before the nonzero exit instead of
        dying markerless on an unguarded digest re-check.

R3 architecture retained (hostile-review findings O-B1/O-N3/O-N4/O-N8v):
archive-bytes late authority with in-memory decision inputs; five-property
systemd runtime read-back with exact values; in-archive fault latches with
the regression gate; job-tag stamp schema in require_job_tag; one
content-addressed decision record with a derived candidate; systemd-only
success with a NO_VERDICT-only PGID fallback; schema-checked nonce; atomic
lease; no-replace hard-link publication; archive verification exact over
regular files AND directories (custody/TERMINAL_DIRS.list).
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import signal
import stat as stat_module
import tarfile
import time
import zlib


MATH_TERMINALS = {
    "EXACT_ENDPOINT_DEAD_ON_TRIPLE02_NODE1_CLOSED_SUCCESSOR_FINITE_COVER",
    ("RING_LEVEL_ENDPOINT_SURVIVOR_ON_TRIPLE02_NODE1_"
     "CLOSED_SUCCESSOR_CHART_PENDING_NILPOTENCE_RADICAL"),
    "NO_VERDICT_OPEN_REMAINDER_ON_TRIPLE02_NODE1_CLOSED_SUCCESSOR",
    ("REVERSE_CONTAINMENT_SEARCH_EXHAUSTED_NO_VERDICT_ON_"
     "TRIPLE02_NODE1_CLOSED_SUCCESSOR"),
}
NO_VERDICT = "CUSTODY_OR_ADAPTER_FAILURE_NO_VERDICT"
SCOPE_MARKER = ("CLOSED_SUCCESSOR_RESULT_BANKED_WITHOUT_WHOLE_STRATUM_"
                "OR_JC2_PROMOTION")
WORKER_GATE = "WORKER_ARTIFACT_AND_RESOURCE_GATES_PASS=1"
SHA_LINE = re.compile(r"([0-9a-f]{64})  ([^\n]+)")
NONCE_RE = re.compile(r"^[a-z0-9]{8,32}$")
DIGEST_RE = re.compile(r"^[0-9a-f]{64}$")
STAMP_RE = re.compile(r"^[0-9]{8}T[0-9]{6}Z$")
LEASE_SCHEMA = "triple02_closed_successor_r4_lease_v1"
DECISION_SCHEMA = "triple02_closed_successor_r4_decision_v1"
FAULT_LATCH_SCHEMA = "triple02_closed_successor_r4_fault_latches_v1"
JOB_TAG_PREFIX = "ggv_triple02_closed_successor_resume_r4_"
# The five charged worker-scope properties (O-N3).  RuntimeMaxUSec must be
# exactly 21600 s; only these systemd renderings of that value are accepted,
# so an unexpected honest rendering downgrades (never promotes) until the
# rehearsal captures the live shape.
RUNTIME_LIMIT_EXPECTED = {
    "killmode": "control-group",
    "memory_max": "274877906944",
    "tasks_max": "512",
    "memory_swap_max": "0",
}
RUNTIME_MAX_USEC_21600 = ("6h", "21600s", "21600000000us")
FAULT_LATCH_FIELDS = (
    "swap_violation", "whole_timeout", "containment_preflight_failure",
    "launcher_reap_failure", "systemd_final_fault", "systemd_runtime_fault",
)
# Archive members whose bytes the late authority reads (in memory, straight
# from the charged archive) when deriving the terminal decision.
DECISION_RETAINED_MEMBERS = frozenset({
    "custody/DECISION_RECORD.json", "custody/DECISION_RECORD.sha256",
    "custody/containment_mode.txt", "custody/systemd_runtime_limits.json",
    "custody/singular_binary.sha256", "custody/worker_identity.json",
    "custody/supervisor_identity.json",
    "custody/FAULT_LATCHES_PRE_ARCHIVE.json",
    "LEASE.json", "LEASE.sha256", "output/VERDICT.txt", "output/SUMMARY.json",
    "work/production/VERDICT.txt", "work/production/SUMMARY.json",
})


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + f".tmp.{os.getpid()}")
    with temporary.open("w") as handle:
        handle.write(text)
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(temporary, path)


def publish_no_replace(path: Path, text: str) -> None:
    """Atomic no-replace publication: hard-link, never move-over."""
    temporary = path.with_name("." + path.name + f".publish.{os.getpid()}")
    with temporary.open("w") as handle:
        handle.write(text)
        handle.flush()
        os.fsync(handle.fileno())
    try:
        os.link(temporary, path)
    except FileExistsError as exc:
        raise RuntimeError("TERMINAL_ALREADY_PUBLISHED") from exc
    finally:
        temporary.unlink(missing_ok=True)


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
    relative = Path(value.rstrip("/"))
    if relative.is_absolute() or not relative.parts or ".." in relative.parts:
        raise RuntimeError("UNSAFE_RELATIVE_PATH")
    return relative


def require_nonce(nonce: str) -> str:
    if not isinstance(nonce, str) or not NONCE_RE.fullmatch(nonce):
        raise RuntimeError("JOB_NONCE_SCHEMA_FAILURE")
    return nonce


def require_job_tag(job_tag: str, nonce: str) -> str:
    if (not isinstance(job_tag, str)
            or not job_tag.startswith(JOB_TAG_PREFIX)
            or not job_tag.endswith("_" + nonce)
            or len(job_tag) <= len(JOB_TAG_PREFIX) + len(nonce) + 1):
        raise RuntimeError("JOB_TAG_COMPOSITION_FAILURE")
    stamp = job_tag[len(JOB_TAG_PREFIX):len(job_tag) - len(nonce) - 1]
    if not STAMP_RE.fullmatch(stamp):
        raise RuntimeError("JOB_TAG_STAMP_SCHEMA_FAILURE")
    return job_tag


def runtime_limits_verified(record: dict[str, object]) -> bool:
    """All five charged worker-scope properties, with exact values."""
    return (all(record.get(key) == expected
                for key, expected in RUNTIME_LIMIT_EXPECTED.items())
            and record.get("runtime_max_usec") in RUNTIME_MAX_USEC_21600)


def build_runtime_limits_record(show_file: Path, output: Path) -> bool:
    values: dict[str, str] = {}
    for line in show_file.read_text().splitlines():
        if "=" in line:
            key, _, value = line.partition("=")
            values[key] = value
    record: dict[str, object] = {
        "killmode": values.get("KillMode", ""),
        "runtime_max_usec": values.get("RuntimeMaxUSec", ""),
        "memory_max": values.get("MemoryMax", ""),
        "tasks_max": values.get("TasksMax", ""),
        "memory_swap_max": values.get("MemorySwapMax", ""),
        "expected": dict(RUNTIME_LIMIT_EXPECTED,
                         runtime_max_usec_any_of=list(RUNTIME_MAX_USEC_21600)),
    }
    record["verified"] = runtime_limits_verified(record)
    atomic_write(output, json.dumps(record, indent=2, sort_keys=True) + "\n")
    return bool(record["verified"])


def require_digest(value: object, label: str) -> str:
    if not isinstance(value, str) or not DIGEST_RE.fullmatch(value):
        raise RuntimeError(f"DIGEST_SCHEMA_FAILURE:{label}")
    return value


# ---- lease ----------------------------------------------------------------

def build_lease(output: Path, sidecar: Path, job_tag: str, nonce: str,
                source_archive_sha256: str, launcher_sha256: str,
                launch_manifest_sha256: str, launcher_pid: int,
                launcher_starttime: int) -> str:
    require_nonce(nonce)
    require_job_tag(job_tag, nonce)
    require_digest(source_archive_sha256, "source")
    require_digest(launcher_sha256, "launcher")
    require_digest(launch_manifest_sha256, "launch-manifest")
    lease = {
        "created_utc": datetime.datetime.now(
            datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "job_nonce": nonce,
        "job_tag": job_tag,
        "launch_manifest_sha256": launch_manifest_sha256,
        "launcher": {"pid": launcher_pid, "starttime": launcher_starttime},
        "launcher_sha256": launcher_sha256,
        "schema": LEASE_SCHEMA,
        "source_archive_sha256": source_archive_sha256,
    }
    atomic_write(output, json.dumps(lease, indent=2, sort_keys=True) + "\n")
    lease_sha = sha256_path(output)
    atomic_write(sidecar, f"{lease_sha}  {output.name}\n")
    return lease_sha


def validate_lease_record(lease: dict[str, object], job_tag: str, nonce: str,
                          source_archive_sha256: str,
                          launcher_sha256: str | None = None
                          ) -> dict[str, object]:
    require_nonce(nonce)
    require_job_tag(job_tag, nonce)
    if lease.get("schema") != LEASE_SCHEMA:
        raise RuntimeError("LEASE_SCHEMA_DISAGREEMENT")
    if (lease.get("job_tag") != job_tag or lease.get("job_nonce") != nonce
            or lease.get("source_archive_sha256") != source_archive_sha256):
        raise RuntimeError("LEASE_BINDING_DISAGREEMENT")
    require_digest(lease.get("launcher_sha256"), "lease-launcher")
    require_digest(lease.get("launch_manifest_sha256"),
                   "lease-launch-manifest")
    launcher = lease.get("launcher")
    if (not isinstance(launcher, dict)
            or not isinstance(launcher.get("pid"), int)
            or not isinstance(launcher.get("starttime"), int)):
        raise RuntimeError("LEASE_LAUNCHER_IDENTITY_SCHEMA")
    if (launcher_sha256 is not None
            and lease.get("launcher_sha256") != launcher_sha256):
        raise RuntimeError("LEASE_LAUNCHER_HASH_DISAGREEMENT")
    return lease


def verify_lease(lease_path: Path, sidecar: Path | None, job_tag: str,
                 nonce: str, source_archive_sha256: str,
                 launcher_sha256: str | None = None) -> dict[str, object]:
    lease = validate_lease_record(json.loads(lease_path.read_text()), job_tag,
                                  nonce, source_archive_sha256,
                                  launcher_sha256)
    if sidecar is not None:
        expected = f"{sha256_path(lease_path)}  {lease_path.name}\n"
        if sidecar.read_text() != expected:
            raise RuntimeError("LEASE_SIDECAR_DISAGREEMENT")
    return lease


# ---- complete terminal manifest (files + directories) ----------------------

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


def manifest_dirs(root: Path, includes: list[str]) -> list[str]:
    dirs: set[str] = set()
    for value in includes:
        relative = safe_relative(value)
        candidate = root / relative
        if candidate.is_symlink() or not candidate.exists():
            raise RuntimeError("MANIFEST_INCLUDE_MISSING_OR_SYMLINK:" + value)
        if candidate.is_dir():
            dirs.add(relative.as_posix())
            for path in sorted(candidate.rglob("*")):
                if path.is_symlink():
                    continue
                if path.is_dir():
                    dirs.add(path.relative_to(root).as_posix())
    return sorted(dirs)


def dirs_list_text(dirs: list[str]) -> str:
    return "".join(name + "\n" for name in dirs)


def build_complete_manifest(root: Path, manifest: Path, includes: list[str],
                            dirs_relative: str) -> tuple[int, int]:
    root = root.resolve()
    manifest = manifest.resolve()
    manifest_relative = manifest.relative_to(root).as_posix()
    dirs_path = root / safe_relative(dirs_relative)
    dirs = manifest_dirs(root, includes)
    atomic_write(dirs_path, dirs_list_text(dirs))
    paths = manifest_files(root, includes, manifest_relative)
    lines = [f"{sha256_path(root / path)}  {path.as_posix()}"
             for path in paths]
    atomic_write(manifest, "\n".join(lines) + "\n")
    return len(paths), len(dirs)


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


def verify_complete_manifest(root: Path, manifest: Path, includes: list[str],
                             dirs_relative: str) -> tuple[int, int]:
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
    dirs_path = root / safe_relative(dirs_relative)
    dirs = manifest_dirs(root, includes)
    if dirs_path.read_text() != dirs_list_text(dirs):
        raise RuntimeError("TERMINAL_DIRECTORY_CENSUS_DRIFT")
    return len(entries), len(dirs)


def archive_member_allowed(name: str, includes: list[str]) -> bool:
    member = safe_relative(name).as_posix()
    for value in includes:
        include = safe_relative(value).as_posix()
        if member == include or member.startswith(include.rstrip("/") + "/"):
            return True
    return False


def extract_and_verify_archive(archive_path: Path, destination: Path,
                               manifest_relative: str, includes: list[str],
                               dirs_relative: str) -> tuple[int, int]:
    """Reject unsafe/extra members (files AND directories), extract privately,
    and replay census/hash from the embedded manifest and directory list."""
    if destination.exists():
        raise RuntimeError("ARCHIVE_REPLAY_DESTINATION_EXISTS")
    destination.mkdir(mode=0o700, parents=True)
    manifest_name = safe_relative(manifest_relative).as_posix()
    dirs_name = safe_relative(dirs_relative).as_posix()
    with tarfile.open(archive_path, "r:gz") as archive:
        members = archive.getmembers()
        names: set[str] = set()
        regular: set[str] = set()
        directories: set[str] = set()
        for member in members:
            name = safe_relative(member.name).as_posix()
            if name in names or not archive_member_allowed(name, includes):
                raise RuntimeError("ARCHIVE_UNSAFE_DUPLICATE_OR_EXTRA:" + name)
            names.add(name)
            if member.isfile():
                regular.add(name)
            elif member.isdir():
                directories.add(name)
            else:
                raise RuntimeError("ARCHIVE_NONREGULAR_MEMBER:" + name)
        for required_name, label in ((manifest_name, "MANIFEST"),
                                     (dirs_name, "DIRECTORY_LIST")):
            if required_name not in regular:
                raise RuntimeError(f"ARCHIVE_{label}_MISSING")
        manifest_handle = archive.extractfile(archive.getmember(manifest_name))
        if manifest_handle is None:
            raise RuntimeError("ARCHIVE_MANIFEST_UNREADABLE")
        manifest_text = manifest_handle.read().decode("utf-8")
        temporary_manifest = destination / ".embedded_manifest"
        atomic_write(temporary_manifest, manifest_text)
        manifest_entries = parse_manifest(temporary_manifest)
        temporary_manifest.unlink()
        if regular != set(manifest_entries) | {manifest_name}:
            raise RuntimeError("ARCHIVE_REGULAR_MEMBER_CENSUS_DRIFT")
        dirs_handle = archive.extractfile(archive.getmember(dirs_name))
        if dirs_handle is None:
            raise RuntimeError("ARCHIVE_DIRECTORY_LIST_UNREADABLE")
        listed_dirs = [line for line in
                       dirs_handle.read().decode("utf-8").splitlines() if line]
        if sorted(listed_dirs) != listed_dirs or len(set(listed_dirs)) != len(
                listed_dirs):
            raise RuntimeError("ARCHIVE_DIRECTORY_LIST_MALFORMED")
        if directories != set(listed_dirs):
            missing = sorted(set(listed_dirs) - directories)
            extra = sorted(directories - set(listed_dirs))
            raise RuntimeError(
                f"ARCHIVE_DIRECTORY_CENSUS_DRIFT:{missing}:{extra}")
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
        destination, destination / safe_relative(manifest_relative), includes,
        dirs_relative)


# ---- frozen-archive authentication for the late authority (O-B1/O2-B1) ----

class FrozenArchiveView:
    """Decision inputs read from the charged archive bytes, never from disk.

    archive_sha256 is the digest actually computed from the single open
    descriptor (O2-B1), equal to the charged digest by construction."""

    def __init__(self, retained: dict[str, bytes], member_sha256: dict[str, str],
                 files: set[str], dirs: set[str], archive_sha256: str):
        self._retained = retained
        self.member_sha256 = member_sha256
        self.files = files
        self.dirs = dirs
        self.archive_sha256 = archive_sha256

    def data(self, name: str) -> bytes:
        if name not in self._retained:
            raise RuntimeError("DECISION_ARCHIVE_MEMBER_MISSING:" + name)
        return self._retained[name]

    def text(self, name: str) -> str:
        return self.data(name).decode("utf-8")

    def json(self, name: str) -> dict[str, object]:
        value = json.loads(self.text(name))
        if not isinstance(value, dict):
            raise RuntimeError("DECISION_ARCHIVE_MEMBER_NOT_OBJECT:" + name)
        return value

    def sha256(self, name: str) -> str:
        if name not in self.member_sha256:
            raise RuntimeError("DECISION_ARCHIVE_MEMBER_MISSING:" + name)
        return self.member_sha256[name]


def open_frozen_archive(terminal_archive: Path):
    """Single-open authority for the charged terminal archive (O2-B1).

    Opens the path EXACTLY ONCE with O_NOFOLLOW (a symlink refuses at the
    open itself, with no separate content read) and O_NONBLOCK (a FIFO at
    the path cannot block the decision; O_NONBLOCK has no effect on regular
    files), then requires the opened object to be a regular file via fstat
    on the descriptor.  Every archive byte the decision consumes is read
    from the returned open object; the path is never reopened, so a
    concurrent rename()/replacement of the path cannot redirect any later
    decision read."""
    flags = os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK
    flags |= getattr(os, "O_CLOEXEC", 0)
    try:
        descriptor = os.open(terminal_archive, flags)
    except OSError as exc:
        raise RuntimeError("DECISION_ARCHIVE_NOT_REGULAR_FILE") from exc
    try:
        if not stat_module.S_ISREG(os.fstat(descriptor).st_mode):
            raise RuntimeError("DECISION_ARCHIVE_NOT_REGULAR_FILE")
    except BaseException:
        os.close(descriptor)
        raise
    return os.fdopen(descriptor, "rb")


def require_stable_archive_stat(before: os.stat_result,
                                after: os.stat_result) -> None:
    """Refuse in-place mutation/truncation of the archive inode during the
    decision read (O2-B1): the identity, size, mtime and ctime observed
    through the single descriptor must be identical before the first byte
    is hashed and after the last authenticated read.  Any same-uid write,
    truncate, chmod, or utimes on the inode moves ctime forward (ctime
    cannot be back-dated without root), so the pair cannot match."""
    fingerprints = [(view.st_dev, view.st_ino, view.st_size,
                     view.st_mtime_ns, view.st_ctime_ns)
                    for view in (before, after)]
    if fingerprints[0] != fingerprints[1]:
        raise RuntimeError("DECISION_ARCHIVE_UNSTABLE_DURING_READ")


def walk_fresh_root(fresh_root: Path) -> tuple[set[str], set[str]]:
    """Exact regular-file and directory censuses; any symlink or special
    file anywhere in the extraction fails closed."""
    if fresh_root.is_symlink() or not fresh_root.is_dir():
        raise RuntimeError("DECISION_FRESH_ROOT_NOT_DIRECTORY")
    files: set[str] = set()
    dirs: set[str] = set()
    for dirpath, dirnames, filenames in os.walk(fresh_root, followlinks=False):
        base = Path(dirpath)
        for name in dirnames:
            entry = base / name
            relative = entry.relative_to(fresh_root).as_posix()
            if entry.is_symlink():
                raise RuntimeError("DECISION_FRESH_ROOT_SYMLINK:" + relative)
            dirs.add(relative)
        for name in filenames:
            entry = base / name
            relative = entry.relative_to(fresh_root).as_posix()
            if entry.is_symlink():
                raise RuntimeError("DECISION_FRESH_ROOT_SYMLINK:" + relative)
            if not entry.is_file():
                raise RuntimeError("DECISION_FRESH_ROOT_NOT_REGULAR:" + relative)
            files.add(relative)
    return files, dirs


def authenticate_frozen_archive(terminal_archive: Path,
                                terminal_archive_sha256: str,
                                fresh_root: Path, manifest_relative: str,
                                includes: list[str],
                                dirs_relative: str) -> FrozenArchiveView:
    """Bind the fresh extraction to the charged archive bytes at decision time.

    O2-B1: opens the archive path EXACTLY ONCE via open_frozen_archive,
    hashes the bytes from that descriptor against the charged digest,
    rewinds, and hands the same open object to tarfile; re-runs the complete
    member-safety, embedded-manifest, and directory censuses from those
    bytes; requires the fresh root's file/directory sets to equal the
    archive member sets exactly and every fresh file to be byte-identical to
    its archive member; retains the decision-input members in memory so
    nothing later is read from the mutable extraction.  The descriptor is
    held until every authentication and retained-member read has finished,
    and a pre/post fstat stability gate refuses in-place mutation of the
    inode during the read.  The view carries the digest actually computed
    from the descriptor."""
    require_digest(terminal_archive_sha256, "terminal-archive")
    manifest_name = safe_relative(manifest_relative).as_posix()
    dirs_name = safe_relative(dirs_relative).as_posix()
    retained: dict[str, bytes] = {}
    member_sha256: dict[str, str] = {}
    regular: set[str] = set()
    directories: set[str] = set()
    with open_frozen_archive(terminal_archive) as handle:
        stat_before = os.fstat(handle.fileno())
        outer_digest = hashlib.sha256()
        for block in iter(lambda: handle.read(1 << 20), b""):
            outer_digest.update(block)
        verified_archive_sha256 = outer_digest.hexdigest()
        if verified_archive_sha256 != terminal_archive_sha256:
            raise RuntimeError("DECISION_ARCHIVE_HASH_DISAGREEMENT")
        fs_files, fs_dirs = walk_fresh_root(fresh_root)
        handle.seek(0)
        try:
            with tarfile.open(fileobj=handle, mode="r:gz") as archive:
                members = archive.getmembers()
                names: set[str] = set()
                for member in members:
                    name = safe_relative(member.name).as_posix()
                    if (name in names
                            or not archive_member_allowed(name, includes)):
                        raise RuntimeError(
                            "DECISION_ARCHIVE_UNSAFE_DUPLICATE_OR_EXTRA:"
                            + name)
                    names.add(name)
                    if member.isfile():
                        regular.add(name)
                    elif member.isdir():
                        directories.add(name)
                    else:
                        raise RuntimeError(
                            "DECISION_ARCHIVE_NONREGULAR_MEMBER:" + name)
                for required_name, label in ((manifest_name, "MANIFEST"),
                                             (dirs_name, "DIRECTORY_LIST")):
                    if required_name not in regular:
                        raise RuntimeError(f"DECISION_ARCHIVE_{label}_MISSING")
                if fs_files != regular or fs_dirs != directories:
                    missing = sorted((regular - fs_files)
                                     | (directories - fs_dirs))
                    extra = sorted((fs_files - regular)
                                   | (fs_dirs - directories))
                    raise RuntimeError(
                        f"DECISION_FRESH_ROOT_CENSUS_DRIFT:{missing}:{extra}")
                retain = (set(DECISION_RETAINED_MEMBERS) & regular) | {
                    manifest_name, dirs_name}
                for member in members:
                    if not member.isfile():
                        continue
                    name = safe_relative(member.name).as_posix()
                    source = archive.extractfile(member)
                    if source is None:
                        raise RuntimeError(
                            "DECISION_ARCHIVE_MEMBER_UNREADABLE:" + name)
                    digest = hashlib.sha256()
                    keep = bytearray() if name in retain else None
                    try:
                        with (fresh_root / safe_relative(name)).open(
                                "rb") as live:
                            while True:
                                block = source.read(1 << 20)
                                digest.update(block)
                                if keep is not None:
                                    keep.extend(block)
                                if live.read(len(block) or 1) != block:
                                    raise RuntimeError(
                                        "DECISION_FRESH_ROOT_BYTES_DRIFT:"
                                        + name)
                                if not block:
                                    break
                    except OSError as exc:
                        raise RuntimeError(
                            "DECISION_FRESH_ROOT_BYTES_DRIFT:" + name) from exc
                    member_sha256[name] = digest.hexdigest()
                    if keep is not None:
                        retained[name] = bytes(keep)
        except (tarfile.TarError, EOFError, zlib.error) as exc:
            raise RuntimeError(
                "DECISION_ARCHIVE_READ_FAILURE:" + type(exc).__name__) from exc
        manifest_text = retained[manifest_name].decode("utf-8")
        entries: dict[str, str] = {}
        for number, line in enumerate(manifest_text.splitlines(), 1):
            match = SHA_LINE.fullmatch(line)
            if not match:
                raise RuntimeError(
                    f"DECISION_ARCHIVE_MANIFEST_MALFORMED_{number}")
            digest_value, value = match.groups()
            relative = safe_relative(value).as_posix()
            if relative in entries:
                raise RuntimeError(
                    "DECISION_ARCHIVE_MANIFEST_DUPLICATE:" + relative)
            entries[relative] = digest_value
        if not entries:
            raise RuntimeError("DECISION_ARCHIVE_MANIFEST_EMPTY")
        if regular != set(entries) | {manifest_name}:
            raise RuntimeError("DECISION_ARCHIVE_MANIFEST_CENSUS_DRIFT")
        for relative, expected_digest in entries.items():
            if member_sha256.get(relative) != expected_digest:
                raise RuntimeError(
                    "DECISION_ARCHIVE_MANIFEST_HASH_DRIFT:" + relative)
        listed_dirs = [line for line in
                       retained[dirs_name].decode("utf-8").splitlines()
                       if line]
        if (sorted(listed_dirs) != listed_dirs
                or len(set(listed_dirs)) != len(listed_dirs)
                or directories != set(listed_dirs)):
            raise RuntimeError("DECISION_ARCHIVE_DIRECTORY_CENSUS_DRIFT")
        require_stable_archive_stat(stat_before, os.fstat(handle.fileno()))
    return FrozenArchiveView(retained, member_sha256, regular, directories,
                             verified_archive_sha256)


def verdict_from_bytes(data: bytes, label: str) -> str:
    value = data.decode("utf-8").strip()
    if not value or "\n" in value:
        raise RuntimeError("VERDICT_FILE_SHAPE:" + label)
    return value


def parse_sha_sidecar_text(text: str, label: str) -> str:
    lines = text.splitlines()
    if len(lines) != 1:
        raise RuntimeError("SHA_SIDECAR_SHAPE:" + label)
    match = SHA_LINE.fullmatch(lines[0])
    if not match:
        raise RuntimeError("SHA_SIDECAR_MALFORMED:" + label)
    return match.group(1)


# ---- decision record (C1) --------------------------------------------------

def read_verdict(path: Path) -> str:
    value = path.read_text().strip()
    if not value or "\n" in value:
        raise RuntimeError("VERDICT_FILE_SHAPE:" + path.name)
    return value


def build_decision_record(
        *, output_record: Path, output_sidecar: Path, job_tag: str,
        nonce: str, source_archive_sha256: str, singular_sha256: str,
        containment_mode: str, lease_path: Path, worker_identity_path: Path,
        supervisor_identity_path: Path, production_dir: Path,
        classifier_dir: Path, artifact_manifest: Path) -> str:
    require_nonce(nonce)
    require_job_tag(job_tag, nonce)
    require_digest(source_archive_sha256, "source")
    require_digest(singular_sha256, "singular")
    if containment_mode != "systemd_scope":
        raise RuntimeError("DECISION_REQUIRES_SYSTEMD_SCOPE")
    lease = verify_lease(lease_path, None, job_tag, nonce,
                         source_archive_sha256)
    worker = json.loads(worker_identity_path.read_text())
    supervisor = json.loads(supervisor_identity_path.read_text())
    for record, keys, label in (
            (worker, ("pid", "pgid", "sid", "starttime"), "WORKER"),
            (supervisor, ("pid", "starttime"), "SUPERVISOR")):
        if any(not isinstance(record.get(key), int) for key in keys):
            raise RuntimeError(f"DECISION_{label}_IDENTITY_SCHEMA")
    production_verdict = read_verdict(production_dir / "VERDICT.txt")
    classifier_verdict = read_verdict(classifier_dir / "VERDICT.txt")
    if production_verdict != classifier_verdict:
        raise RuntimeError("DECISION_PRODUCTION_CLASSIFIER_DISAGREEMENT")
    candidate = classifier_verdict
    if candidate not in MATH_TERMINALS:
        raise RuntimeError("DECISION_CANDIDATE_NOT_ALLOWLISTED")
    production_summary = json.loads(
        (production_dir / "SUMMARY.json").read_text())
    classifier_summary = json.loads(
        (classifier_dir / "SUMMARY.json").read_text())
    for summary, label in ((production_summary, "PRODUCTION"),
                           (classifier_summary, "CLASSIFIER")):
        if summary.get("classification") != candidate:
            raise RuntimeError(f"DECISION_{label}_SUMMARY_DISAGREEMENT")
        binding = summary.get("job_binding")
        if (not isinstance(binding, dict)
                or binding.get("job_tag") != job_tag
                or binding.get("job_nonce") != nonce
                or binding.get("source_archive_sha256")
                != source_archive_sha256
                or binding.get("singular_sha256") != singular_sha256):
            raise RuntimeError(f"DECISION_{label}_BINDING_DISAGREEMENT")
    if not artifact_manifest.is_file() or not artifact_manifest.stat().st_size:
        raise RuntimeError("DECISION_ARTIFACT_MANIFEST_MISSING")
    record = {
        "artifact_manifest_sha256": sha256_path(artifact_manifest),
        "candidate": candidate,
        "classifier_summary_sha256": sha256_path(
            classifier_dir / "SUMMARY.json"),
        "classifier_verdict_sha256": sha256_path(
            classifier_dir / "VERDICT.txt"),
        "containment_mode": containment_mode,
        "created_utc": datetime.datetime.now(
            datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "job_nonce": nonce,
        "job_tag": job_tag,
        "lease_sha256": sha256_path(lease_path),
        "launcher_sha256": lease["launcher_sha256"],
        "production_summary_sha256": sha256_path(
            production_dir / "SUMMARY.json"),
        "production_verdict_sha256": sha256_path(
            production_dir / "VERDICT.txt"),
        "schema": DECISION_SCHEMA,
        "singular_sha256": singular_sha256,
        "source_archive_sha256": source_archive_sha256,
        "supervisor": {"pid": supervisor["pid"],
                       "starttime": supervisor["starttime"]},
        "supervisor_identity_sha256": sha256_path(supervisor_identity_path),
        "worker": {"pid": worker["pid"], "pgid": worker["pgid"],
                   "sid": worker["sid"], "starttime": worker["starttime"]},
        "worker_identity_sha256": sha256_path(worker_identity_path),
    }
    atomic_write(output_record,
                 json.dumps(record, indent=2, sort_keys=True) + "\n")
    record_sha = sha256_path(output_record)
    atomic_write(output_sidecar,
                 f"{record_sha}  custody/DECISION_RECORD.json\n")
    return record_sha


def parse_sha_sidecar(path: Path) -> str:
    line = path.read_text().splitlines()
    if len(line) != 1:
        raise RuntimeError("SHA_SIDECAR_SHAPE:" + path.name)
    match = SHA_LINE.fullmatch(line[0])
    if not match:
        raise RuntimeError("SHA_SIDECAR_MALFORMED:" + path.name)
    return match.group(1)


def derive_late_decision(fresh_root: Path, terminal_archive: Path,
                         terminal_archive_sha256: str,
                         manifest_relative: str, includes: list[str],
                         dirs_relative: str, live_lease: Path, job_tag: str,
                         nonce: str, source_archive_sha256: str,
                         live_mode_file: Path,
                         expected_worker: dict[str, int],
                         expected_supervisor: dict[str, int],
                         live_faults: dict[str, int]) -> dict[str, object]:
    """Late authority (O-B1/O2-B1): authenticate the frozen archive bytes
    against the charged digest through a single open descriptor, bind the
    fresh extraction to them member-for-member, and derive the candidate
    exclusively from the archive bytes held in memory while verifying every
    decision-record equality.  The returned archive_sha256 is the digest
    actually computed from that descriptor."""
    require_nonce(nonce)
    require_job_tag(job_tag, nonce)
    view = authenticate_frozen_archive(
        terminal_archive, terminal_archive_sha256, fresh_root,
        manifest_relative, includes, dirs_relative)
    record_bytes = view.data("custody/DECISION_RECORD.json")
    record_sha = hashlib.sha256(record_bytes).hexdigest()
    if parse_sha_sidecar_text(
            view.text("custody/DECISION_RECORD.sha256"),
            "custody/DECISION_RECORD.sha256") != record_sha:
        raise RuntimeError("DECISION_SIDECAR_DISAGREEMENT")
    record = json.loads(record_bytes)
    if record.get("schema") != DECISION_SCHEMA:
        raise RuntimeError("DECISION_SCHEMA_DISAGREEMENT")
    if (record.get("job_tag") != job_tag
            or record.get("job_nonce") != nonce
            or record.get("source_archive_sha256") != source_archive_sha256):
        raise RuntimeError("DECISION_JOB_BINDING_DISAGREEMENT")
    archived_mode = view.text("custody/containment_mode.txt").strip()
    live_mode = live_mode_file.read_text().strip()
    if not (archived_mode == live_mode == "systemd_scope"
            == record.get("containment_mode")):
        raise RuntimeError("DECISION_CONTAINMENT_MODE_DISAGREEMENT")
    limits = view.json("custody/systemd_runtime_limits.json")
    if (limits.get("verified") is not True
            or not runtime_limits_verified(limits)):
        raise RuntimeError("DECISION_RUNTIME_LIMITS_DISAGREEMENT")
    latches = view.json("custody/FAULT_LATCHES_PRE_ARCHIVE.json")
    if (latches.get("schema") != FAULT_LATCH_SCHEMA
            or latches.get("job_tag") != job_tag
            or latches.get("job_nonce") != nonce
            or latches.get("containment_mode") != "systemd_scope"):
        raise RuntimeError("DECISION_FAULT_LATCH_BINDING_DISAGREEMENT")
    archived_rc = latches.get("worker_rc")
    if not isinstance(archived_rc, int) or isinstance(archived_rc, bool):
        # O2-N2: JSON true/false (bool is an int subclass) must not pass.
        raise RuntimeError("DECISION_FAULT_LATCH_SCHEMA:worker_rc")
    if archived_rc != live_faults.get("worker_rc"):
        raise RuntimeError("DECISION_FAULT_WORKER_RC_DISAGREEMENT")
    for field in FAULT_LATCH_FIELDS:
        archived_fault = latches.get(field)
        if (not isinstance(archived_fault, int)
                or isinstance(archived_fault, bool)
                or archived_fault not in (0, 1)):
            raise RuntimeError(f"DECISION_FAULT_LATCH_SCHEMA:{field}")
        if archived_fault == 1 and live_faults.get(field) != 1:
            raise RuntimeError(f"DECISION_FAULT_LATCH_REGRESSION:{field}")
    lease_bytes = view.data("LEASE.json")
    lease_sha = hashlib.sha256(lease_bytes).hexdigest()
    if (lease_sha != record.get("lease_sha256")
            or lease_sha != sha256_path(live_lease)):
        raise RuntimeError("DECISION_LEASE_DISAGREEMENT")
    lease = validate_lease_record(json.loads(lease_bytes), job_tag, nonce,
                                  source_archive_sha256)
    expected_lease_sidecar = f"{lease_sha}  LEASE.json\n"
    if view.text("LEASE.sha256") != expected_lease_sidecar:
        raise RuntimeError("LEASE_SIDECAR_DISAGREEMENT")
    if lease["launcher_sha256"] != record.get("launcher_sha256"):
        raise RuntimeError("DECISION_LAUNCHER_DISAGREEMENT")
    singular_sidecar = parse_sha_sidecar_text(
        view.text("custody/singular_binary.sha256"),
        "custody/singular_binary.sha256")
    if singular_sidecar != record.get("singular_sha256"):
        raise RuntimeError("DECISION_SINGULAR_DISAGREEMENT")
    for name, block, expected in (
            ("worker_identity.json", "worker", expected_worker),
            ("supervisor_identity.json", "supervisor", expected_supervisor)):
        member = "custody/" + name
        if view.sha256(member) != record.get(f"{block}_identity_sha256"):
            raise RuntimeError(f"DECISION_{block.upper()}_IDENTITY_HASH")
        archived_identity = view.json(member)
        recorded = record.get(block)
        if not isinstance(recorded, dict):
            raise RuntimeError(f"DECISION_{block.upper()}_BLOCK_SCHEMA")
        for key, value in expected.items():
            if archived_identity.get(key) != value or recorded.get(key) != value:
                raise RuntimeError(
                    f"DECISION_{block.upper()}_IDENTITY_DISAGREEMENT:{key}")
    candidate = record.get("candidate")
    if candidate not in MATH_TERMINALS:
        raise RuntimeError("DECISION_CANDIDATE_NOT_ALLOWLISTED")
    classifier_verdict = verdict_from_bytes(
        view.data("output/VERDICT.txt"), "output/VERDICT.txt")
    production_verdict = verdict_from_bytes(
        view.data("work/production/VERDICT.txt"),
        "work/production/VERDICT.txt")
    if not (candidate == classifier_verdict == production_verdict):
        raise RuntimeError("DECISION_CANDIDATE_ARCHIVE_DISAGREEMENT")
    for relative, key in (
            ("output/VERDICT.txt", "classifier_verdict_sha256"),
            ("output/SUMMARY.json", "classifier_summary_sha256"),
            ("work/production/VERDICT.txt", "production_verdict_sha256"),
            ("work/production/SUMMARY.json", "production_summary_sha256"),
            ("custody/WORKER_ARTIFACT_MANIFEST.sha256",
             "artifact_manifest_sha256")):
        if view.sha256(relative) != record.get(key):
            raise RuntimeError(f"DECISION_HASH_DISAGREEMENT:{key}")
    return {"candidate": candidate, "decision_sha256": record_sha,
            "archive_sha256": view.archive_sha256}


# ---- terminal decision -----------------------------------------------------

def decide_terminal(candidate: str | None, *, worker_rc: int,
                    swap_zero: bool, swap_violation: bool,
                    whole_timeout: bool, containment_preflight_failure: bool,
                    launcher_reap_failure: bool, systemd_final_fault: bool,
                    systemd_runtime_fault: bool, scope_ok: bool,
                    containment_empty: bool, artifact_ok: bool,
                    manifest_generator_ok: bool, manifest_replay_ok: bool,
                    archive_replay_ok: bool, archive_ready: bool,
                    systemd_mode_ok: bool, runtime_limits_ok: bool,
                    lease_ok: bool, decision_ok: bool) -> str:
    if not all((worker_rc == 0, swap_zero, not swap_violation,
                not whole_timeout, not containment_preflight_failure,
                not launcher_reap_failure, not systemd_final_fault,
                not systemd_runtime_fault, scope_ok, containment_empty,
                artifact_ok, manifest_generator_ok, manifest_replay_ok,
                archive_replay_ok, archive_ready, systemd_mode_ok,
                runtime_limits_ok, lease_ok, decision_ok)):
        return NO_VERDICT
    if candidate in MATH_TERMINALS:
        return candidate
    return NO_VERDICT


def terminal_marker_text(classification: str, archive_sha256: str | None,
                         decision_sha256: str | None) -> str:
    return (f"{classification}\n"
            f"TERMINAL_ARCHIVE_SHA256={archive_sha256 or 'NONE'}\n"
            f"DECISION_RECORD_SHA256={decision_sha256 or 'NONE'}\n")


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
    lease_build = sub.add_parser("lease-build")
    lease_build.add_argument("--output", required=True, type=Path)
    lease_build.add_argument("--sidecar", required=True, type=Path)
    lease_build.add_argument("--job-tag", required=True)
    lease_build.add_argument("--job-nonce", required=True)
    lease_build.add_argument("--source-archive-sha256", required=True)
    lease_build.add_argument("--launcher-sha256", required=True)
    lease_build.add_argument("--launch-manifest-sha256", required=True)
    lease_build.add_argument("--launcher-pid", required=True, type=int)
    lease_build.add_argument("--launcher-starttime", required=True, type=int)
    lease_verify = sub.add_parser("lease-verify")
    lease_verify.add_argument("--lease", required=True, type=Path)
    lease_verify.add_argument("--sidecar", type=Path)
    lease_verify.add_argument("--job-tag", required=True)
    lease_verify.add_argument("--job-nonce", required=True)
    lease_verify.add_argument("--source-archive-sha256", required=True)
    lease_verify.add_argument("--launcher-sha256")
    decision_build = sub.add_parser("decision-build")
    decision_build.add_argument("--output-record", required=True, type=Path)
    decision_build.add_argument("--output-sidecar", required=True, type=Path)
    decision_build.add_argument("--job-tag", required=True)
    decision_build.add_argument("--job-nonce", required=True)
    decision_build.add_argument("--source-archive-sha256", required=True)
    decision_build.add_argument("--singular-sha256", required=True)
    decision_build.add_argument("--containment-mode-file", required=True,
                                type=Path)
    decision_build.add_argument("--lease", required=True, type=Path)
    decision_build.add_argument("--worker-identity", required=True, type=Path)
    decision_build.add_argument("--supervisor-identity", required=True,
                                type=Path)
    decision_build.add_argument("--production", required=True, type=Path)
    decision_build.add_argument("--classifier-output", required=True,
                                type=Path)
    decision_build.add_argument("--artifact-manifest", required=True,
                                type=Path)
    manifest_build = sub.add_parser("manifest-build")
    manifest_build.add_argument("--root", required=True, type=Path)
    manifest_build.add_argument("--manifest", required=True, type=Path)
    manifest_build.add_argument("--include", action="append", required=True)
    manifest_build.add_argument("--dirs-relative", required=True)
    manifest_verify = sub.add_parser("manifest-verify")
    manifest_verify.add_argument("--root", required=True, type=Path)
    manifest_verify.add_argument("--manifest", required=True, type=Path)
    manifest_verify.add_argument("--include", action="append", required=True)
    manifest_verify.add_argument("--dirs-relative", required=True)
    archive_verify = sub.add_parser("archive-extract-verify")
    archive_verify.add_argument("--archive", required=True, type=Path)
    archive_verify.add_argument("--destination", required=True, type=Path)
    archive_verify.add_argument("--manifest-relative", required=True)
    archive_verify.add_argument("--include", action="append", required=True)
    archive_verify.add_argument("--dirs-relative", required=True)
    publish = sub.add_parser("publish-marker")
    publish.add_argument("--content-file", required=True, type=Path)
    publish.add_argument("--marker", required=True, type=Path)
    runtime_limits = sub.add_parser("runtime-limits-record")
    runtime_limits.add_argument("--show-file", required=True, type=Path)
    runtime_limits.add_argument("--output", required=True, type=Path)
    terminal = sub.add_parser("terminal")
    terminal.add_argument("--fresh-root", type=Path)
    terminal.add_argument("--terminal-archive", type=Path)
    terminal.add_argument("--archive-sha256")
    terminal.add_argument("--manifest-relative")
    terminal.add_argument("--include", action="append", default=[])
    terminal.add_argument("--dirs-relative")
    terminal.add_argument("--live-lease", required=True, type=Path)
    terminal.add_argument("--job-tag", required=True)
    terminal.add_argument("--job-nonce", required=True)
    terminal.add_argument("--source-archive-sha256", required=True)
    terminal.add_argument("--containment-mode-file", required=True, type=Path)
    terminal.add_argument("--worker-pid", required=True, type=int)
    terminal.add_argument("--worker-starttime", required=True, type=int)
    terminal.add_argument("--supervisor-pid", required=True, type=int)
    terminal.add_argument("--supervisor-starttime", required=True, type=int)
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
    terminal.add_argument("--systemd-runtime-fault", required=True,
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
    if args.command == "lease-build":
        lease_sha = build_lease(
            args.output, args.sidecar, args.job_tag, args.job_nonce,
            args.source_archive_sha256, args.launcher_sha256,
            args.launch_manifest_sha256, args.launcher_pid,
            args.launcher_starttime)
        print(f"LEASE_SHA256={lease_sha}")
        return 0
    if args.command == "lease-verify":
        verify_lease(args.lease, args.sidecar, args.job_tag, args.job_nonce,
                     args.source_archive_sha256, args.launcher_sha256)
        print("LEASE_VERIFY_PASS=1")
        return 0
    if args.command == "decision-build":
        mode = args.containment_mode_file.read_text().strip()
        record_sha = build_decision_record(
            output_record=args.output_record,
            output_sidecar=args.output_sidecar, job_tag=args.job_tag,
            nonce=args.job_nonce,
            source_archive_sha256=args.source_archive_sha256,
            singular_sha256=args.singular_sha256, containment_mode=mode,
            lease_path=args.lease,
            worker_identity_path=args.worker_identity,
            supervisor_identity_path=args.supervisor_identity,
            production_dir=args.production,
            classifier_dir=args.classifier_output,
            artifact_manifest=args.artifact_manifest)
        print(f"DECISION_RECORD_SHA256={record_sha}")
        return 0
    if args.command == "manifest-build":
        files, dirs = build_complete_manifest(
            args.root, args.manifest, args.include, args.dirs_relative)
        print(f"TERMINAL_MANIFEST_GENERATED_ENTRIES={files}")
        print(f"TERMINAL_MANIFEST_GENERATED_DIRECTORIES={dirs}")
        return 0
    if args.command == "manifest-verify":
        files, dirs = verify_complete_manifest(
            args.root, args.manifest, args.include, args.dirs_relative)
        print(f"TERMINAL_MANIFEST_REPLAYED_ENTRIES={files}")
        print(f"TERMINAL_MANIFEST_REPLAYED_DIRECTORIES={dirs}")
        return 0
    if args.command == "archive-extract-verify":
        files, dirs = extract_and_verify_archive(
            args.archive, args.destination, args.manifest_relative,
            args.include, args.dirs_relative)
        print(f"TERMINAL_ARCHIVE_REPLAYED_ENTRIES={files}")
        print(f"TERMINAL_ARCHIVE_REPLAYED_DIRECTORIES={dirs}")
        return 0
    if args.command == "publish-marker":
        publish_no_replace(args.marker, args.content_file.read_text())
        print("TERMINAL_MARKER_PUBLISHED=1")
        return 0
    if args.command == "runtime-limits-record":
        verified = build_runtime_limits_record(args.show_file, args.output)
        print(f"SYSTEMD_RUNTIME_LIMITS_VERIFIED={int(verified)}")
        return 0 if verified else 1
    # terminal
    candidate: str | None = None
    decision_sha: str | None = None
    verified_archive_sha: str | None = None
    decision_ok = False
    mode_ok = False
    runtime_ok = False
    lease_ok = False
    decision_error = ""
    late_inputs_complete = (
        args.fresh_root is not None and args.terminal_archive is not None
        and args.archive_sha256 is not None
        and args.manifest_relative is not None and bool(args.include)
        and args.dirs_relative is not None)
    if args.archive_ready == "1" and not late_inputs_complete:
        decision_error = "RuntimeError:LATE_DECISION_INPUTS_MISSING"
    if late_inputs_complete and args.archive_ready == "1":
        try:
            derived = derive_late_decision(
                args.fresh_root, args.terminal_archive, args.archive_sha256,
                args.manifest_relative, args.include, args.dirs_relative,
                args.live_lease, args.job_tag,
                args.job_nonce, args.source_archive_sha256,
                args.containment_mode_file,
                {"pid": args.worker_pid, "starttime": args.worker_starttime},
                {"pid": args.supervisor_pid,
                 "starttime": args.supervisor_starttime},
                {"worker_rc": args.worker_rc,
                 "swap_violation": int(args.swap_violation == "1"),
                 "whole_timeout": int(args.whole_timeout == "1"),
                 "containment_preflight_failure": int(
                     args.containment_preflight_failure == "1"),
                 "launcher_reap_failure": int(
                     args.launcher_reap_failure == "1"),
                 "systemd_final_fault": int(args.systemd_final_fault == "1"),
                 "systemd_runtime_fault": int(
                     args.systemd_runtime_fault == "1")})
            candidate = str(derived["candidate"])
            decision_sha = str(derived["decision_sha256"])
            verified_archive_sha = str(derived["archive_sha256"])
            decision_ok = True
            mode_ok = True
            runtime_ok = True
            lease_ok = True
        except (RuntimeError, OSError, ValueError, KeyError,
                json.JSONDecodeError, tarfile.TarError,
                UnicodeDecodeError) as error:
            decision_error = f"{type(error).__name__}:{error}"
    classification = decide_terminal(
        candidate, worker_rc=args.worker_rc,
        swap_zero=args.swap_total == 0 and args.swap_free == 0,
        swap_violation=args.swap_violation == "1",
        whole_timeout=args.whole_timeout == "1",
        containment_preflight_failure=(
            args.containment_preflight_failure == "1"),
        launcher_reap_failure=args.launcher_reap_failure == "1",
        systemd_final_fault=args.systemd_final_fault == "1",
        systemd_runtime_fault=args.systemd_runtime_fault == "1",
        scope_ok=exact_line(args.scope_marker, SCOPE_MARKER),
        containment_empty=(
            exact_line(args.containment_marker, "CONTAINMENT_EMPTY_PASS=1")
            and empty_json_list(args.pgid_census)
            and empty_json_list(args.tag_census)),
        artifact_ok=exact_line(args.worker_gate, WORKER_GATE),
        manifest_generator_ok=args.manifest_generator_rc == 0,
        manifest_replay_ok=args.manifest_replay_rc == 0,
        archive_replay_ok=args.archive_replay_rc == 0,
        archive_ready=args.archive_ready == "1",
        systemd_mode_ok=mode_ok, runtime_limits_ok=runtime_ok,
        lease_ok=lease_ok, decision_ok=decision_ok)
    # O2-B1: on an authenticated decision the marker carries the digest
    # actually computed from the single open descriptor (decide_terminal can
    # return a mathematical first line only when decision_ok, so every
    # mathematical marker is descriptor-bound).  O2-N4: a malformed claimed
    # digest is never echoed and never raises here -- the custody no-verdict
    # marker is still published before the nonzero exit.
    if verified_archive_sha is not None:
        archive_sha: str | None = verified_archive_sha
    elif (args.archive_ready == "1"
          and isinstance(args.archive_sha256, str)
          and DIGEST_RE.fullmatch(args.archive_sha256)):
        archive_sha = args.archive_sha256
    else:
        archive_sha = None
    marker = terminal_marker_text(
        classification, archive_sha,
        decision_sha if classification in MATH_TERMINALS else None)
    atomic_write(args.output, marker)
    print(f"FINAL_CLASSIFICATION={classification}")
    if decision_error:
        print(f"LATE_DECISION_FAILURE={decision_error}")
    return 0 if classification in MATH_TERMINALS else 3


if __name__ == "__main__":
    raise SystemExit(main())
