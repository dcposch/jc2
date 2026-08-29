#!/usr/bin/env python3
"""Fail-closed Linux process-custody and terminal-promotion helpers (R2).

R2 repairs relative to the reviewed R1 packet:

  C1  One content-addressed decision record (custody/DECISION_RECORD.json)
      binds the job tag, schema-checked nonce, source-archive hash, lease,
      worker/supervisor identities, production and classifier summary/verdict
      hashes, the complete worker artifact manifest hash, and the candidate.
      The late terminal authority derives the candidate exclusively from a
      fresh extraction of the frozen terminal archive, re-verifies every
      equality of the decision record against that extraction, and binds the
      public marker to both the archive digest and the decision digest.  The
      live candidate file is never read at decision time.
  C3  Mathematical terminals are eligible only in systemd-scope containment
      with verified independent RuntimeMaxSec, KillMode=control-group and
      MemorySwapMax=0; the exact-PGID fallback is NO_VERDICT-only.
  4   Nonempty schema-checked nonce; atomic lease build/verify; no-replace
      hard-link publication; archive verification exact over regular files
      AND directories (custody/TERMINAL_DIRS.list).
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
import tarfile
import time


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
LEASE_SCHEMA = "triple02_closed_successor_r2_lease_v1"
DECISION_SCHEMA = "triple02_closed_successor_r2_decision_v1"
JOB_TAG_PREFIX = "ggv_triple02_closed_successor_resume_r2_"


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
    return job_tag


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


def verify_lease(lease_path: Path, sidecar: Path | None, job_tag: str,
                 nonce: str, source_archive_sha256: str,
                 launcher_sha256: str | None = None) -> dict[str, object]:
    require_nonce(nonce)
    require_job_tag(job_tag, nonce)
    lease = json.loads(lease_path.read_text())
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


def derive_late_decision(fresh_root: Path, live_lease: Path, job_tag: str,
                         nonce: str, source_archive_sha256: str,
                         live_mode_file: Path,
                         expected_worker: dict[str, int],
                         expected_supervisor: dict[str, int]
                         ) -> dict[str, object]:
    """Late authority: derive the candidate exclusively from the frozen
    archive's fresh extraction and verify every decision-record equality."""
    require_nonce(nonce)
    require_job_tag(job_tag, nonce)
    record_path = fresh_root / "custody/DECISION_RECORD.json"
    sidecar_path = fresh_root / "custody/DECISION_RECORD.sha256"
    record_sha = sha256_path(record_path)
    if parse_sha_sidecar(sidecar_path) != record_sha:
        raise RuntimeError("DECISION_SIDECAR_DISAGREEMENT")
    record = json.loads(record_path.read_text())
    if record.get("schema") != DECISION_SCHEMA:
        raise RuntimeError("DECISION_SCHEMA_DISAGREEMENT")
    if (record.get("job_tag") != job_tag
            or record.get("job_nonce") != nonce
            or record.get("source_archive_sha256") != source_archive_sha256):
        raise RuntimeError("DECISION_JOB_BINDING_DISAGREEMENT")
    fresh_mode = (fresh_root / "custody/containment_mode.txt"
                  ).read_text().strip()
    live_mode = live_mode_file.read_text().strip()
    if not (fresh_mode == live_mode == "systemd_scope"
            == record.get("containment_mode")):
        raise RuntimeError("DECISION_CONTAINMENT_MODE_DISAGREEMENT")
    limits = json.loads((fresh_root / "custody/systemd_runtime_limits.json"
                         ).read_text())
    if (limits.get("verified") is not True
            or limits.get("killmode") != "control-group"
            or not limits.get("runtime_max_usec")
            or limits.get("runtime_max_usec") == "infinity"
            or limits.get("memory_swap_max") != "0"):
        raise RuntimeError("DECISION_RUNTIME_LIMITS_DISAGREEMENT")
    fresh_lease = fresh_root / "LEASE.json"
    lease_sha = sha256_path(fresh_lease)
    if (lease_sha != record.get("lease_sha256")
            or lease_sha != sha256_path(live_lease)):
        raise RuntimeError("DECISION_LEASE_DISAGREEMENT")
    lease = verify_lease(fresh_lease, fresh_root / "LEASE.sha256", job_tag,
                         nonce, source_archive_sha256)
    if lease["launcher_sha256"] != record.get("launcher_sha256"):
        raise RuntimeError("DECISION_LAUNCHER_DISAGREEMENT")
    singular_sidecar = parse_sha_sidecar(
        fresh_root / "custody/singular_binary.sha256")
    if singular_sidecar != record.get("singular_sha256"):
        raise RuntimeError("DECISION_SINGULAR_DISAGREEMENT")
    for name, block, expected in (
            ("worker_identity.json", "worker", expected_worker),
            ("supervisor_identity.json", "supervisor", expected_supervisor)):
        path = fresh_root / "custody" / name
        if sha256_path(path) != record.get(f"{block}_identity_sha256"):
            raise RuntimeError(f"DECISION_{block.upper()}_IDENTITY_HASH")
        live = json.loads(path.read_text())
        recorded = record.get(block)
        if not isinstance(recorded, dict):
            raise RuntimeError(f"DECISION_{block.upper()}_BLOCK_SCHEMA")
        for key, value in expected.items():
            if live.get(key) != value or recorded.get(key) != value:
                raise RuntimeError(
                    f"DECISION_{block.upper()}_IDENTITY_DISAGREEMENT:{key}")
    candidate = record.get("candidate")
    if candidate not in MATH_TERMINALS:
        raise RuntimeError("DECISION_CANDIDATE_NOT_ALLOWLISTED")
    classifier_verdict = read_verdict(fresh_root / "output/VERDICT.txt")
    production_verdict = read_verdict(
        fresh_root / "work/production/VERDICT.txt")
    if not (candidate == classifier_verdict == production_verdict):
        raise RuntimeError("DECISION_CANDIDATE_ARCHIVE_DISAGREEMENT")
    for relative, key in (
            ("output/VERDICT.txt", "classifier_verdict_sha256"),
            ("output/SUMMARY.json", "classifier_summary_sha256"),
            ("work/production/VERDICT.txt", "production_verdict_sha256"),
            ("work/production/SUMMARY.json", "production_summary_sha256"),
            ("custody/WORKER_ARTIFACT_MANIFEST.sha256",
             "artifact_manifest_sha256")):
        if sha256_path(fresh_root / relative) != record.get(key):
            raise RuntimeError(f"DECISION_HASH_DISAGREEMENT:{key}")
    return {"candidate": candidate, "decision_sha256": record_sha}


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
    terminal = sub.add_parser("terminal")
    terminal.add_argument("--fresh-root", type=Path)
    terminal.add_argument("--archive-sha256")
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
    # terminal
    candidate: str | None = None
    decision_sha: str | None = None
    decision_ok = False
    mode_ok = False
    runtime_ok = False
    lease_ok = False
    decision_error = ""
    if args.fresh_root is not None and args.archive_ready == "1":
        try:
            derived = derive_late_decision(
                args.fresh_root, args.live_lease, args.job_tag,
                args.job_nonce, args.source_archive_sha256,
                args.containment_mode_file,
                {"pid": args.worker_pid, "starttime": args.worker_starttime},
                {"pid": args.supervisor_pid,
                 "starttime": args.supervisor_starttime})
            candidate = str(derived["candidate"])
            decision_sha = str(derived["decision_sha256"])
            decision_ok = True
            mode_ok = True
            runtime_ok = True
            lease_ok = True
        except (RuntimeError, OSError, ValueError, KeyError,
                json.JSONDecodeError) as error:
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
    archive_sha = args.archive_sha256 if args.archive_ready == "1" else None
    if archive_sha is not None:
        require_digest(archive_sha, "terminal-archive")
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
