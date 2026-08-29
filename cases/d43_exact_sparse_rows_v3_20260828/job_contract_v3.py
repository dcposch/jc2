#!/usr/bin/env python3
"""Fail-closed lease, containment, monitor, archive, and terminal helpers.

Revision 3 of the D43 exact a00pp sparse-row job.  Every subcommand here is
production custody: nothing in this file may rest on a Python ``assert``.
The module refuses optimized Python outright so that no dependency assert
elsewhere can silently vanish under ``python -O``.

Process, cgroup, and meminfo readers accept injectable roots so bounded
hostile fixtures can run on hosts without ``/proc`` (for example macOS
review machines).  Production defaults are the live kernel paths.
"""

from __future__ import annotations

import argparse
import fcntl
import gzip
import hashlib
import json
import os
import re
import secrets
import signal
import sys
import tarfile
import time
from pathlib import Path

if sys.flags.optimize:
    raise RuntimeError(
        "OPTIMIZED_PYTHON_REFUSED_FAIL_CLOSED: jc2 d43 v3 custody tooling "
        "must run without -O/-OO/PYTHONOPTIMIZE")

SCHEMA = "jc2.d43.a00pp-exact-source-rows.v3"
LEASE_SCHEMA = SCHEMA + ".run-lease"
TERMINAL_SCHEMA = SCHEMA + ".terminal"
CANDIDATE_SCHEMA = SCHEMA + ".finalize-candidate"
CANDIDATE_STATUS = "CANDIDATE_PENDING_TERMINAL_DECISION"
POSITIVE_TERMINAL = "EXACT_A00PP_184_RAW_J_ROWS_EMITTED_NO_SOLVE"
NO_VERDICT_PREFIX = "NO_VERDICT_"
SHA_LINE = re.compile(r"([0-9a-f]{64})  ([^\n]+)")
HEX64 = re.compile(r"[0-9a-f]{64}")
PROC_DEFAULT = Path("/proc")


class CustodyError(RuntimeError):
    pass


def require(condition, message: str) -> None:
    if not condition:
        raise CustodyError(message)


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp.%d" % os.getpid())
    with temporary.open("w") as handle:
        handle.write(text)
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(temporary, path)


def atomic_json(path: Path, value) -> None:
    atomic_write(path, json.dumps(value, indent=1, sort_keys=True) + "\n")


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def utc_now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


# ---------------------------------------------------------------------------
# Exclusive one-shot run lease.


def probe_lock_held(lock_path: Path) -> bool:
    """True iff some other open file description holds the exclusive lock."""
    descriptor = os.open(lock_path, os.O_RDWR | os.O_CREAT, 0o600)
    try:
        try:
            fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            return True
        fcntl.flock(descriptor, fcntl.LOCK_UN)
        return False
    finally:
        os.close(descriptor)


def lease_record(fd: int, lock_path: Path, job_root: Path, job_tag: str,
                 archive_sha256: str, registration_path: Path,
                 launcher_path: Path, launcher_pid: int,
                 proc_root: Path, output: Path) -> dict:
    """Bind the held kernel lease, a fresh nonce, and launcher identity."""
    require(HEX64.fullmatch(archive_sha256) is not None,
            "LEASE_ARCHIVE_SHA_MALFORMED")
    lock_stat = os.stat(lock_path)
    fd_stat = os.fstat(fd)
    require((fd_stat.st_dev, fd_stat.st_ino) ==
            (lock_stat.st_dev, lock_stat.st_ino),
            "LEASE_FD_IS_NOT_THE_LOCK_FILE")
    require(probe_lock_held(lock_path),
            "LEASE_LOCK_IS_NOT_HELD_EXCLUSIVELY")
    require(job_root.is_dir(), "LEASE_JOB_ROOT_MISSING")
    require(job_root.name == job_tag, "LEASE_JOB_TAG_BASENAME_MISMATCH")
    launcher_identity = read_identity(launcher_pid, proc_root)
    require(launcher_identity["uid"] == os.getuid(), "LEASE_LAUNCHER_FOREIGN")
    lease = {
        "schema": LEASE_SCHEMA,
        "run_nonce": secrets.token_hex(32),
        "job_root": str(job_root.resolve()),
        "job_tag": job_tag,
        "lock_path": str(Path(lock_path).resolve()),
        "lock_dev_ino": [lock_stat.st_dev, lock_stat.st_ino],
        "lock_held_probe": True,
        "launcher": {
            "pid": launcher_pid,
            "starttime": launcher_identity["starttime"],
            "uid": launcher_identity["uid"],
            "hostname": os.uname().nodename,
            "path": str(Path(launcher_path).resolve()),
            "sha256": sha256_path(Path(launcher_path)),
        },
        "source_archive_sha256": archive_sha256,
        "registration_sha256": sha256_path(registration_path),
        "created_utc": utc_now(),
        "terminal_authority": False,
    }
    atomic_json(output, lease)
    return lease


def verify_lease(lease_path: Path, job_root: Path, job_tag: str,
                 expect_nonce=None, require_held: bool = True) -> dict:
    try:
        lease = json.loads(lease_path.read_text())
    except (OSError, json.JSONDecodeError) as error:
        raise CustodyError("LEASE_UNREADABLE: %s" % error)
    require(isinstance(lease, dict) and lease.get("schema") == LEASE_SCHEMA,
            "LEASE_SCHEMA_MISMATCH")
    nonce = lease.get("run_nonce")
    require(isinstance(nonce, str) and HEX64.fullmatch(nonce) is not None,
            "LEASE_NONCE_MALFORMED")
    if expect_nonce is not None:
        require(nonce == expect_nonce, "LEASE_NONCE_MISMATCH")
    require(lease.get("job_root") == str(Path(job_root).resolve()),
            "LEASE_JOB_ROOT_MISMATCH")
    require(lease.get("job_tag") == job_tag, "LEASE_JOB_TAG_MISMATCH")
    require(lease.get("terminal_authority") is False,
            "LEASE_CLAIMS_TERMINAL_AUTHORITY")
    lock_path = Path(lease.get("lock_path", ""))
    require(lock_path.is_absolute(), "LEASE_LOCK_PATH_MALFORMED")
    if require_held:
        try:
            lock_stat = os.stat(lock_path)
        except OSError as error:
            raise CustodyError("LEASE_LOCK_FILE_MISSING: %s" % error)
        require(list(lease.get("lock_dev_ino", [])) ==
                [lock_stat.st_dev, lock_stat.st_ino],
                "LEASE_LOCK_IDENTITY_DRIFT")
        require(probe_lock_held(lock_path), "LEASE_LOCK_NOT_HELD")
    for key in ("source_archive_sha256", "registration_sha256"):
        value = lease.get(key)
        require(isinstance(value, str) and HEX64.fullmatch(value) is not None,
                "LEASE_FIELD_MALFORMED:" + key)
    launcher = lease.get("launcher")
    require(isinstance(launcher, dict) and
            isinstance(launcher.get("pid"), int) and
            isinstance(launcher.get("starttime"), int) and
            isinstance(launcher.get("sha256"), str) and
            HEX64.fullmatch(launcher["sha256"]) is not None,
            "LEASE_LAUNCHER_IDENTITY_MALFORMED")
    return lease


FRESH_ROOT_ALLOWED = ("source", "records", "RUN_LEASE.json")
FRESH_RECORDS_ALLOWED_EXACT = ("REGISTERED.json", "LAUNCH.json")
FRESH_RECORDS_ALLOWED_PREFIX = ("launch_",)


def verify_fresh_namespace(job_root: Path) -> None:
    """Refuse stage, output, custody, or terminal artifacts in the namespace."""
    require(job_root.is_dir(), "FRESH_NAMESPACE_MISSING")
    for entry in sorted(job_root.iterdir()):
        require(entry.name in FRESH_ROOT_ALLOWED,
                "FRESH_NAMESPACE_UNEXPECTED_ENTRY:" + entry.name)
    records = job_root / "records"
    if records.is_dir():
        for entry in sorted(records.iterdir()):
            allowed = (entry.name in FRESH_RECORDS_ALLOWED_EXACT or
                       any(entry.name.startswith(prefix)
                           for prefix in FRESH_RECORDS_ALLOWED_PREFIX))
            require(allowed,
                    "FRESH_NAMESPACE_UNEXPECTED_RECORD:" + entry.name)
    for forbidden in ("TERMINAL.json", "output", "custody"):
        require(not (job_root / forbidden).exists(),
                "FRESH_NAMESPACE_STALE_ARTIFACT:" + forbidden)
    for entry in job_root.glob("*.terminal.tar.gz"):
        raise CustodyError("FRESH_NAMESPACE_STALE_ARCHIVE:" + entry.name)


# ---------------------------------------------------------------------------
# Exact PID identity, job-tag census, containment cleanup.


def read_identity(pid: int, proc_root: Path = PROC_DEFAULT) -> dict:
    stat = (proc_root / str(pid) / "stat").read_text()
    close = stat.rfind(")")
    require(close >= 0, "MALFORMED_PROC_STAT")
    fields = stat[close + 2:].split()
    status_lines = (proc_root / str(pid) / "status").read_text().splitlines()
    uid_line = None
    for line in status_lines:
        if line.startswith("Uid:"):
            uid_line = line
            break
    require(uid_line is not None, "MALFORMED_PROC_STATUS")
    return {
        "pid": pid,
        "state": fields[0],
        "ppid": int(fields[1]),
        "pgid": int(fields[2]),
        "sid": int(fields[3]),
        "starttime": int(fields[19]),
        "uid": int(uid_line.split()[1]),
    }


def has_job_tag(pid: int, job_tag: str,
                proc_root: Path = PROC_DEFAULT) -> bool:
    try:
        environ = (proc_root / str(pid) / "environ").read_bytes().split(b"\0")
    except (FileNotFoundError, PermissionError, ProcessLookupError, OSError):
        return False
    return b"JOB_TAG=" + job_tag.encode() in environ


def process_records(pgid: int, job_tag: str, exclude,
                    proc_root: Path = PROC_DEFAULT):
    pgid_records = []
    tag_records = []
    for entry in proc_root.iterdir():
        if not entry.name.isdigit():
            continue
        pid = int(entry.name)
        if pid in exclude or pid == os.getpid():
            continue
        try:
            identity = read_identity(pid, proc_root)
        except (FileNotFoundError, PermissionError, ProcessLookupError,
                CustodyError, ValueError, OSError):
            continue
        if pgid > 1 and identity["pgid"] == pgid:
            pgid_records.append(identity)
        if has_job_tag(pid, job_tag, proc_root):
            tag_records.append(identity)
    key = lambda record: record["pid"]
    return sorted(pgid_records, key=key), sorted(tag_records, key=key)


def signal_exact(record: dict, sig, proc_root: Path = PROC_DEFAULT,
                 kill=os.kill) -> None:
    try:
        current = read_identity(record["pid"], proc_root)
    except (FileNotFoundError, ProcessLookupError, OSError):
        return
    if (current["starttime"] != record["starttime"]
            or current["uid"] != os.getuid()):
        raise CustodyError("PID_IDENTITY_CHANGED_OR_FOREIGN")
    kill(record["pid"], sig)


def exact_pid_record(pid: int, starttime: int,
                     proc_root: Path = PROC_DEFAULT):
    try:
        current = read_identity(pid, proc_root)
    except (FileNotFoundError, ProcessLookupError, OSError):
        return None
    require(current["starttime"] == starttime and
            current["uid"] == os.getuid(),
            "PID_IDENTITY_CHANGED_OR_FOREIGN")
    return current


def wait_for_exact_pid_exit(pid: int, starttime: int, timeout: float,
                            interval: float = 0.05,
                            proc_root: Path = PROC_DEFAULT) -> dict:
    require(timeout >= 0 and interval > 0, "INVALID_PID_WAIT_BOUND")
    deadline = time.monotonic() + timeout
    while True:
        current = exact_pid_record(pid, starttime, proc_root)
        if current is None:
            return {"ready_to_reap": True, "terminal_state": "ABSENT"}
        if current["state"] == "Z":
            return {"ready_to_reap": True, "terminal_state": "ZOMBIE"}
        if time.monotonic() >= deadline:
            return {"ready_to_reap": False,
                    "terminal_state": str(current["state"])}
        time.sleep(interval)


def descendants_deepest_first(root_pid: int,
                              proc_root: Path = PROC_DEFAULT):
    children = {}
    identities = {}
    for entry in proc_root.iterdir():
        if not entry.name.isdigit():
            continue
        pid = int(entry.name)
        try:
            identity = read_identity(pid, proc_root)
        except (FileNotFoundError, PermissionError, ProcessLookupError,
                CustodyError, ValueError, OSError):
            continue
        identities[pid] = identity
        children.setdefault(identity["ppid"], []).append(pid)
    ordered = []
    stack = [root_pid]
    seen = set()
    while stack:
        pid = stack.pop()
        if pid in seen:
            continue
        seen.add(pid)
        ordered.append(pid)
        stack.extend(children.get(pid, ()))
    ordered.reverse()  # deepest first, root last
    return [identities[pid] for pid in ordered if pid in identities]


def kill_tree(root_pid: int, root_starttime: int, census_output: Path,
              proc_root: Path = PROC_DEFAULT, kill=os.kill,
              pause: float = 0.4) -> bool:
    """TERM then KILL an exact-pid subtree; census survivors afterwards."""
    root = exact_pid_record(root_pid, root_starttime, proc_root)
    if root is not None:
        for sig in (signal.SIGTERM, signal.SIGKILL):
            for record in descendants_deepest_first(root_pid, proc_root):
                if record["uid"] != os.getuid() or \
                        record["pid"] == os.getpid():
                    continue
                try:
                    signal_exact(record, sig, proc_root, kill)
                except (CustodyError, ProcessLookupError, PermissionError):
                    continue
            time.sleep(pause)
            if exact_pid_record(root_pid, root_starttime, proc_root) is None:
                break
    survivors = [record for record in
                 descendants_deepest_first(root_pid, proc_root)
                 if record["pid"] != os.getpid()]
    if exact_pid_record(root_pid, root_starttime, proc_root) is None:
        survivors = [record for record in survivors
                     if record["pid"] != root_pid]
    atomic_json(census_output, survivors)
    return not survivors


def terminate_and_census(pgid: int, job_tag: str, exclude,
                         pgid_output: Path, tag_output: Path,
                         proc_root: Path = PROC_DEFAULT,
                         kill=os.kill) -> bool:
    for sig, pause in ((signal.SIGTERM, 1.0), (signal.SIGKILL, 0.25)):
        pgid_records, tag_records = process_records(
            pgid, job_tag, exclude, proc_root)
        combined = {record["pid"]: record
                    for record in pgid_records + tag_records}
        for record in combined.values():
            try:
                signal_exact(record, sig, proc_root, kill)
            except (CustodyError, ProcessLookupError, PermissionError):
                continue
        if combined:
            time.sleep(pause)
    pgid_records, tag_records = process_records(
        pgid, job_tag, exclude, proc_root)
    atomic_json(pgid_output, pgid_records)
    atomic_json(tag_output, tag_records)
    return not pgid_records and not tag_records


def parse_cgroup_procs(path: Path):
    text = path.read_text()
    pids = []
    for number, raw in enumerate(text.splitlines(), 1):
        value = raw.strip()
        if not value:
            continue
        if not value.isascii() or not value.isdecimal() or int(value) <= 0:
            raise CustodyError("MALFORMED_CGROUP_PROCS_LINE_%d" % number)
        pids.append(int(value))
    return sorted(set(pids))


def empty_json_list(path: Path) -> bool:
    try:
        return json.loads(path.read_text()) == []
    except (OSError, json.JSONDecodeError):
        return False


# ---------------------------------------------------------------------------
# Sticky continuous resource monitor.


def read_meminfo(path: Path) -> dict:
    result = {}
    for line in path.read_text().splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = int(value.split()[0])
    return result


def read_int_file(path: Path):
    try:
        text = path.read_text().strip()
    except OSError:
        return None
    if text == "max":
        return "max"
    try:
        return int(text)
    except ValueError:
        return None


def read_memory_events_oom_kill(path: Path):
    try:
        for line in path.read_text().splitlines():
            parts = line.split()
            if len(parts) == 2 and parts[0] == "oom_kill":
                return int(parts[1])
    except (OSError, ValueError):
        return None
    return None


def aggregate_pgid_rss_kib(pgid: int, proc_root: Path) -> int:
    total = 0
    count = 0
    for entry in proc_root.iterdir():
        if not entry.name.isdigit():
            continue
        try:
            identity = read_identity(int(entry.name), proc_root)
            if identity["pgid"] != pgid:
                continue
            for line in (entry / "status").read_text().splitlines():
                if line.startswith("VmRSS:"):
                    total += int(line.split()[1])
                    break
            count += 1
        except (FileNotFoundError, PermissionError, ProcessLookupError,
                CustodyError, ValueError, OSError):
            continue
    return total


def latch_violation(violations_dir: Path, reason: str, payload: dict) -> None:
    """First observation wins; a latched reason is never rewritten."""
    violations_dir.mkdir(parents=True, exist_ok=True)
    target = violations_dir / ("v_%s.json" % reason)
    if target.exists():
        return
    atomic_json(target, dict(payload, reason=reason, utc=utc_now()))


def violations_census(violations_dir: Path):
    if not violations_dir.is_dir():
        return None
    return sorted(entry.name for entry in violations_dir.iterdir())


def run_monitor(args) -> int:
    proc_root = Path(args.proc_root)
    meminfo_path = Path(args.meminfo)
    violations_dir = Path(args.violations_dir)
    violations_dir.mkdir(parents=True, exist_ok=True)
    heartbeat = Path(args.heartbeat)
    telemetry = Path(args.telemetry)
    peak_path = Path(args.peak_output)
    cgroup_dir = Path(args.cgroup_dir) if args.cgroup_dir else None
    stop_requested = {"flag": False}

    def on_term(signum, frame):
        stop_requested["flag"] = True

    signal.signal(signal.SIGTERM, on_term)
    if not telemetry.exists():
        atomic_write(telemetry, "utc\telapsed_s\tswap_total_kib\t"
                     "swap_free_kib\tmem_available_kib\tcgroup_memory_bytes\t"
                     "cgroup_swap_bytes\tcgroup_pids\taggregate_rss_kib\t"
                     "oom_kill\n")
    started = time.time()
    peak_memory = 0
    peak_rss = 0
    tick = 0
    while True:
        tick += 1
        now = time.time()
        if args.watch_ppid and os.getppid() != args.watch_ppid:
            latch_violation(violations_dir, "SUPERVISOR_DIED",
                            {"expected_ppid": args.watch_ppid,
                             "observed_ppid": os.getppid()})
            if args.kill_on_parent_death == "pgid":
                try:
                    os.killpg(os.getpgrp(), signal.SIGKILL)
                except OSError:
                    pass
            elif args.kill_on_parent_death == "cgroup" and cgroup_dir:
                try:
                    for pid in parse_cgroup_procs(cgroup_dir / "cgroup.procs"):
                        if pid != os.getpid():
                            try:
                                os.kill(pid, signal.SIGKILL)
                            except (ProcessLookupError, PermissionError):
                                pass
                except CustodyError:
                    pass
            return 3
        try:
            memory = read_meminfo(meminfo_path)
        except OSError:
            latch_violation(violations_dir, "MEMINFO_UNREADABLE", {})
            memory = {}
        swap_total = memory.get("SwapTotal")
        swap_free = memory.get("SwapFree")
        if swap_total != 0 or swap_free != 0:
            latch_violation(violations_dir, "HOST_SWAP_NONZERO",
                            {"swap_total_kib": swap_total,
                             "swap_free_kib": swap_free})
        cgroup_memory = None
        cgroup_swap = None
        cgroup_pids = None
        oom_kill = None
        if cgroup_dir is not None:
            cgroup_memory = read_int_file(cgroup_dir / "memory.current")
            cgroup_swap = read_int_file(cgroup_dir / "memory.swap.current")
            cgroup_pids = read_int_file(cgroup_dir / "pids.current")
            oom_kill = read_memory_events_oom_kill(
                cgroup_dir / "memory.events")
            if isinstance(cgroup_memory, int):
                peak_memory = max(peak_memory, cgroup_memory)
                if args.memory_max_bytes and \
                        cgroup_memory > args.memory_max_bytes:
                    latch_violation(violations_dir, "CGROUP_MEMORY_OVER_MAX",
                                    {"memory_current": cgroup_memory,
                                     "memory_max": args.memory_max_bytes})
            else:
                latch_violation(violations_dir, "CGROUP_MEMORY_UNREADABLE", {})
            if cgroup_swap not in (0,):
                latch_violation(violations_dir, "CGROUP_SWAP_NONZERO",
                                {"memory_swap_current": cgroup_swap})
            if isinstance(cgroup_pids, int) and args.pids_max and \
                    cgroup_pids > args.pids_max:
                latch_violation(violations_dir, "CGROUP_PIDS_OVER_MAX",
                                {"pids_current": cgroup_pids,
                                 "pids_max": args.pids_max})
            if oom_kill is None:
                latch_violation(violations_dir,
                                "CGROUP_MEMORY_EVENTS_UNREADABLE", {})
            elif oom_kill > 0:
                # The scope cgroup is created fresh for this job, so any
                # nonzero count is an OOM kill inside this job.
                latch_violation(violations_dir, "OOM_KILL_OBSERVED",
                                {"oom_kill": oom_kill})
        aggregate_rss = None
        if args.pgid:
            aggregate_rss = aggregate_pgid_rss_kib(args.pgid, proc_root)
            peak_rss = max(peak_rss, aggregate_rss)
            if args.memory_max_bytes and \
                    aggregate_rss * 1024 > args.memory_max_bytes:
                latch_violation(violations_dir, "AGGREGATE_RSS_OVER_MAX",
                                {"aggregate_rss_kib": aggregate_rss,
                                 "memory_max_bytes": args.memory_max_bytes})
        if now > args.deadline_epoch:
            latch_violation(violations_dir, "WHOLE_TIMEOUT",
                            {"deadline_epoch": args.deadline_epoch,
                             "observed_epoch": now})
        with telemetry.open("a") as handle:
            handle.write("%s\t%d\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (
                utc_now(), int(now - started), swap_total, swap_free,
                memory.get("MemAvailable"), cgroup_memory, cgroup_swap,
                cgroup_pids, aggregate_rss, oom_kill))
        atomic_json(heartbeat, {"epoch": now, "tick": tick,
                                "monitor_pid": os.getpid()})
        atomic_json(peak_path, {"peak_cgroup_memory_bytes": peak_memory,
                                "peak_aggregate_rss_kib": peak_rss,
                                "ticks": tick})
        if stop_requested["flag"]:
            return 0
        if args.max_ticks and tick >= args.max_ticks:
            return 0
        time.sleep(args.interval)


# ---------------------------------------------------------------------------
# Deterministic archives and manifests.


def safe_relative(value: str) -> Path:
    relative = Path(value)
    require(not relative.is_absolute() and relative.parts and
            ".." not in relative.parts, "UNSAFE_RELATIVE_PATH:" + value)
    return relative


def manifest_files(root: Path, includes, manifest_relative: str):
    excluded = safe_relative(manifest_relative)
    paths = set()
    for value in includes:
        relative = safe_relative(value)
        candidate = root / relative
        require(not candidate.is_symlink() and candidate.exists(),
                "MANIFEST_INCLUDE_MISSING_OR_SYMLINK:" + value)
        if candidate.is_file():
            found = [candidate]
        elif candidate.is_dir():
            found = sorted(candidate.rglob("*"))
        else:
            raise CustodyError("MANIFEST_INCLUDE_NOT_FILE_OR_DIRECTORY:" +
                               value)
        for path in found:
            member = path.relative_to(root)
            if member == excluded:
                continue
            require(not path.is_symlink(),
                    "MANIFEST_MEMBER_SYMLINK:" + member.as_posix())
            if path.is_dir():
                continue
            require(path.is_file(),
                    "MANIFEST_MEMBER_NOT_REGULAR:" + member.as_posix())
            paths.add(member)
    return sorted(paths, key=lambda item: item.as_posix())


def build_complete_manifest(root: Path, manifest: Path, includes) -> int:
    root = root.resolve()
    manifest = manifest.resolve()
    manifest_relative = manifest.relative_to(root).as_posix()
    paths = manifest_files(root, includes, manifest_relative)
    require(paths, "EMPTY_TERMINAL_MANIFEST_BUILD")
    lines = ["%s  %s" % (sha256_path(root / path), path.as_posix())
             for path in paths]
    atomic_write(manifest, "\n".join(lines) + "\n")
    return len(paths)


def parse_manifest(path: Path):
    entries = {}
    for number, line in enumerate(path.read_text().splitlines(), 1):
        match = SHA_LINE.fullmatch(line)
        require(match is not None, "MALFORMED_MANIFEST_LINE_%d" % number)
        digest, value = match.groups()
        relative = safe_relative(value).as_posix()
        require(relative not in entries,
                "DUPLICATE_MANIFEST_MEMBER:" + relative)
        entries[relative] = digest
    require(entries, "EMPTY_TERMINAL_MANIFEST")
    return entries


def verify_complete_manifest(root: Path, manifest: Path, includes) -> int:
    root = root.resolve()
    manifest = manifest.resolve()
    manifest_relative = manifest.relative_to(root).as_posix()
    entries = parse_manifest(manifest)
    expected = {path.as_posix()
                for path in manifest_files(root, includes, manifest_relative)}
    if set(entries) != expected:
        missing = sorted(expected - set(entries))
        extra = sorted(set(entries) - expected)
        raise CustodyError("TERMINAL_MANIFEST_CENSUS_DRIFT:%s:%s" %
                           (missing, extra))
    for relative, expected_digest in entries.items():
        path = root / safe_relative(relative)
        require(not path.is_symlink() and path.is_file(),
                "TERMINAL_MANIFEST_MEMBER_NOT_REGULAR:" + relative)
        require(sha256_path(path) == expected_digest,
                "TERMINAL_MANIFEST_HASH_DRIFT:" + relative)
    return len(entries)


def build_deterministic_archive(root: Path, member_manifest: Path,
                                manifest_member: str, output: Path) -> str:
    """Deterministic tar.gz: sorted members, zeroed metadata, gzip mtime 0."""
    root = root.resolve()
    entries = parse_manifest(member_manifest)
    manifest_relative = safe_relative(manifest_member).as_posix()
    require(manifest_relative not in entries,
            "ARCHIVE_MANIFEST_SELF_LISTED")
    members = sorted(entries) + [manifest_relative]
    for relative, expected in sorted(entries.items()):
        path = root / safe_relative(relative)
        require(not path.is_symlink() and path.is_file(),
                "ARCHIVE_SOURCE_NOT_REGULAR:" + relative)
        require(sha256_path(path) == expected,
                "ARCHIVE_SOURCE_HASH_DRIFT:" + relative)
    manifest_disk = root / safe_relative(manifest_relative)
    require(manifest_disk.resolve() == member_manifest.resolve(),
            "ARCHIVE_MANIFEST_MEMBER_PATH_MISMATCH")
    temporary = output.with_name(output.name + ".tmp.%d" % os.getpid())
    with temporary.open("wb") as raw:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw,
                           compresslevel=9, mtime=0) as gz:
            with tarfile.open(fileobj=gz, mode="w",
                              format=tarfile.USTAR_FORMAT) as archive:
                for relative in sorted(members):
                    path = root / safe_relative(relative)
                    info = tarfile.TarInfo(name=relative)
                    info.size = path.stat().st_size
                    info.mode = 0o444
                    info.uid = info.gid = 0
                    info.uname = info.gname = ""
                    info.mtime = 0
                    with path.open("rb") as handle:
                        archive.addfile(info, handle)
        raw.flush()
        os.fsync(raw.fileno())
    os.replace(temporary, output)
    return sha256_path(output)


def archive_member_allowed(name: str, includes) -> bool:
    member = safe_relative(name).as_posix()
    for value in includes:
        include = safe_relative(value).as_posix()
        if member == include or member.startswith(include.rstrip("/") + "/"):
            return True
    return False


def extract_and_verify_archive(archive_path: Path, destination: Path,
                               manifest_relative: str, includes) -> int:
    """Reject unsafe/extra members, extract privately, replay census+hash."""
    require(not destination.exists(), "ARCHIVE_REPLAY_DESTINATION_EXISTS")
    destination.mkdir(mode=0o700, parents=True)
    manifest_name = safe_relative(manifest_relative).as_posix()
    with tarfile.open(archive_path, "r:gz") as archive:
        members = archive.getmembers()
        names = set()
        regular = set()
        for member in members:
            name = safe_relative(member.name).as_posix()
            require(name not in names and
                    archive_member_allowed(name, includes),
                    "ARCHIVE_UNSAFE_DUPLICATE_OR_EXTRA:" + name)
            names.add(name)
            if member.isfile():
                regular.add(name)
            elif not member.isdir():
                raise CustodyError("ARCHIVE_NONREGULAR_MEMBER:" + name)
        require(manifest_name in regular, "ARCHIVE_MANIFEST_MISSING")
        manifest_handle = archive.extractfile(archive.getmember(manifest_name))
        require(manifest_handle is not None, "ARCHIVE_MANIFEST_UNREADABLE")
        manifest_text = manifest_handle.read().decode("utf-8")
        temporary_manifest = destination / ".embedded_manifest"
        atomic_write(temporary_manifest, manifest_text)
        manifest_entries = parse_manifest(temporary_manifest)
        temporary_manifest.unlink()
        require(regular == set(manifest_entries) | {manifest_name},
                "ARCHIVE_REGULAR_MEMBER_CENSUS_DRIFT")
        for member in members:
            target = destination / safe_relative(member.name)
            if member.isdir():
                target.mkdir(mode=0o700, parents=True, exist_ok=True)
                continue
            target.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
            source = archive.extractfile(member)
            require(source is not None,
                    "ARCHIVE_MEMBER_UNREADABLE:" + member.name)
            descriptor = os.open(target, os.O_WRONLY | os.O_CREAT | os.O_EXCL,
                                 0o400)
            with os.fdopen(descriptor, "wb") as handle:
                for block in iter(lambda: source.read(1 << 20), b""):
                    handle.write(block)
    return verify_complete_manifest(
        destination, destination / safe_relative(manifest_relative), includes)


# ---------------------------------------------------------------------------
# Single-authority terminal decision.


def parse_sidecar_sha256(path: Path):
    try:
        text = path.read_text().strip().splitlines()
    except OSError:
        return None
    if len(text) != 1:
        return None
    match = SHA_LINE.fullmatch(text[0])
    return match.group(1) if match else None


def load_candidate(path: Path, expect_nonce: str):
    try:
        candidate = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError):
        return None, None
    if not isinstance(candidate, dict):
        return None, None
    if candidate.get("schema") != CANDIDATE_SCHEMA:
        return None, None
    if candidate.get("status") != CANDIDATE_STATUS:
        return None, None
    if candidate.get("terminal_authority") is not False:
        return None, None
    if candidate.get("run_nonce") != expect_nonce:
        return None, None
    for key in ("manifest_sha256", "preflight_receipt_sha256",
                "pilot_gate_sha256", "merge_receipt_sha256",
                "merge_payload_sha256", "semantic_sha256", "lease_sha256"):
        value = candidate.get(key)
        if not isinstance(value, str) or HEX64.fullmatch(value) is None:
            return None, None
    return candidate, sha256_path(path)


def decide_terminal(args) -> int:
    lease_gate = True
    lease = None
    lease_reason = None
    try:
        lease = verify_lease(Path(args.lease), Path(args.job_root),
                             args.job_tag, require_held=True)
    except CustodyError as error:
        lease_gate = False
        lease_reason = str(error)
    candidate = None
    candidate_sha = None
    if lease is not None:
        candidate, candidate_sha = load_candidate(
            Path(args.candidate), lease["run_nonce"])
    gates = {
        "lease_valid_and_held": lease_gate,
        "preflight_rc_zero": args.preflight_rc == 0,
        "source_check_rc_zero": args.source_check_rc == 0,
        "build_f_rc_zero": args.f_rc == 0,
        "build_g_rc_zero": args.g_rc == 0,
        "pair_rc_zero": args.pair_rc == 0,
        "emit_rc_zero": args.emit_rc == 0,
        "candidate_rc_zero": args.candidate_rc == 0,
        "candidate_parsed_and_bound": candidate is not None,
        "containment_identity_gate": args.containment_identity_gate == "1",
        "monitor_started": args.monitor_started == "1",
        "monitor_stop_clean": args.monitor_stop_clean == "1",
        "monitor_violations_empty": empty_json_list(
            Path(args.monitor_violations)),
        "no_swap_violation": args.swap_violation == "0",
        "final_swap_zero": args.swap_total == 0 and args.swap_free == 0,
        "no_whole_timeout": args.whole_timeout == "0",
        "no_peer_cancellation": args.peer_cancelled == "0",
        "oom_kill_zero": args.oom_kill_count == 0,
        "cleanup_gate": args.cleanup_gate == "1",
        "pgid_census_empty": empty_json_list(Path(args.pgid_census)),
        "tag_census_empty": empty_json_list(Path(args.tag_census)),
        "cgroup_final_gate": args.cgroup_final_gate == "1",
        "manifest_generator_rc_zero": args.manifest_generator_rc == 0,
        "manifest_replay_rc_zero": args.manifest_replay_rc == 0,
        "archive_replay_rc_zero": args.archive_replay_rc == 0,
        "archive_ready": args.archive_ready == "1",
    }
    archive_sha = parse_sidecar_sha256(Path(args.archive_sha_sidecar))
    gates["archive_outer_sha_present"] = archive_sha is not None
    positive = all(gates.values())
    if positive:
        status = POSITIVE_TERMINAL
    else:
        failed = sorted(name for name, value in gates.items() if not value)
        status = NO_VERDICT_PREFIX + (failed[0].upper() if failed
                                      else "UNKNOWN")
    terminal = {
        "schema": TERMINAL_SCHEMA,
        "status": status,
        "terminal_authority": True,
        "positive": positive,
        "job_tag": args.job_tag,
        "run_nonce": lease["run_nonce"] if lease else None,
        "lease_sha256": sha256_path(Path(args.lease))
            if Path(args.lease).is_file() else None,
        "lease_failure": lease_reason,
        "gates": gates,
        "failed_gates": sorted(name for name, value in gates.items()
                               if not value),
        "candidate_sha256": candidate_sha,
        "candidate_binding": {
            key: candidate.get(key) for key in (
                "manifest_sha256", "preflight_receipt_sha256",
                "pilot_gate_sha256", "merge_receipt_sha256",
                "merge_payload_sha256", "semantic_sha256",
                "exact_inventory")
        } if candidate else None,
        "terminal_archive_sha256": archive_sha,
        "utc": utc_now(),
    }
    output = Path(args.output)
    atomic_write(output, json.dumps(terminal, indent=1, sort_keys=True) + "\n")
    print("FINAL_CLASSIFICATION=%s" % status)
    return 0 if positive else 3


# ---------------------------------------------------------------------------
# Command-line interface.


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    lease_flock = sub.add_parser("lease-flock")
    lease_flock.add_argument("--fd", required=True, type=int)

    record = sub.add_parser("lease-record")
    record.add_argument("--fd", required=True, type=int)
    record.add_argument("--lock-path", required=True, type=Path)
    record.add_argument("--job-root", required=True, type=Path)
    record.add_argument("--job-tag", required=True)
    record.add_argument("--archive-sha256", required=True)
    record.add_argument("--registration", required=True, type=Path)
    record.add_argument("--launcher-path", required=True, type=Path)
    record.add_argument("--launcher-pid", type=int, default=0)
    record.add_argument("--proc-root", type=Path, default=PROC_DEFAULT)
    record.add_argument("--output", required=True, type=Path)

    probe = sub.add_parser("lease-probe")
    probe.add_argument("--lock-path", required=True, type=Path)

    verify_lease_parser = sub.add_parser("verify-lease")
    verify_lease_parser.add_argument("--lease", required=True, type=Path)
    verify_lease_parser.add_argument("--job-root", required=True, type=Path)
    verify_lease_parser.add_argument("--job-tag", required=True)
    verify_lease_parser.add_argument("--expect-nonce", default=None)

    fresh = sub.add_parser("verify-fresh-namespace")
    fresh.add_argument("--job-root", required=True, type=Path)

    pid_start = sub.add_parser("pid-start")
    pid_start.add_argument("--pid", required=True, type=int)
    pid_start.add_argument("--proc-root", type=Path, default=PROC_DEFAULT)

    wait_pid = sub.add_parser("wait-pid")
    wait_pid.add_argument("--pid", required=True, type=int)
    wait_pid.add_argument("--starttime", required=True, type=int)
    wait_pid.add_argument("--timeout", required=True, type=float)
    wait_pid.add_argument("--output", required=True, type=Path)
    wait_pid.add_argument("--proc-root", type=Path, default=PROC_DEFAULT)

    signal_parser = sub.add_parser("signal-pid")
    signal_parser.add_argument("--pid", required=True, type=int)
    signal_parser.add_argument("--starttime", required=True, type=int)
    signal_parser.add_argument("--signal", required=True,
                               choices=("TERM", "KILL"))
    signal_parser.add_argument("--proc-root", type=Path, default=PROC_DEFAULT)

    tree = sub.add_parser("kill-tree")
    tree.add_argument("--pid", required=True, type=int)
    tree.add_argument("--starttime", required=True, type=int)
    tree.add_argument("--census-output", required=True, type=Path)
    tree.add_argument("--proc-root", type=Path, default=PROC_DEFAULT)

    cleanup = sub.add_parser("cleanup")
    cleanup.add_argument("--pgid", required=True, type=int)
    cleanup.add_argument("--job-tag", required=True)
    cleanup.add_argument("--exclude-pid", action="append", default=[],
                         type=int)
    cleanup.add_argument("--pgid-output", required=True, type=Path)
    cleanup.add_argument("--tag-output", required=True, type=Path)
    cleanup.add_argument("--proc-root", type=Path, default=PROC_DEFAULT)

    cgroup = sub.add_parser("cgroup-census")
    cgroup.add_argument("--path", required=True, type=Path)
    cgroup.add_argument("--allow-pid", action="append", default=[], type=int)
    cgroup.add_argument("--output", required=True, type=Path)

    monitor = sub.add_parser("monitor")
    monitor.add_argument("--interval", required=True, type=float)
    monitor.add_argument("--deadline-epoch", required=True, type=float)
    monitor.add_argument("--memory-max-bytes", required=True, type=int)
    monitor.add_argument("--pids-max", required=True, type=int)
    monitor.add_argument("--meminfo", default="/proc/meminfo")
    monitor.add_argument("--cgroup-dir", default=None)
    monitor.add_argument("--pgid", type=int, default=0)
    monitor.add_argument("--telemetry", required=True, type=Path)
    monitor.add_argument("--heartbeat", required=True, type=Path)
    monitor.add_argument("--peak-output", required=True, type=Path)
    monitor.add_argument("--violations-dir", required=True, type=Path)
    monitor.add_argument("--watch-ppid", type=int, default=0)
    monitor.add_argument("--kill-on-parent-death", default="none",
                         choices=("none", "pgid", "cgroup"))
    monitor.add_argument("--max-ticks", type=int, default=0)
    monitor.add_argument("--proc-root", type=Path, default=PROC_DEFAULT)

    census = sub.add_parser("violations-census")
    census.add_argument("--dir", required=True, type=Path)
    census.add_argument("--output", required=True, type=Path)

    manifest_build = sub.add_parser("manifest-build")
    manifest_build.add_argument("--root", required=True, type=Path)
    manifest_build.add_argument("--manifest", required=True, type=Path)
    manifest_build.add_argument("--include", action="append", required=True)

    manifest_verify = sub.add_parser("manifest-verify")
    manifest_verify.add_argument("--root", required=True, type=Path)
    manifest_verify.add_argument("--manifest", required=True, type=Path)
    manifest_verify.add_argument("--include", action="append", required=True)

    archive_build = sub.add_parser("archive-build")
    archive_build.add_argument("--root", required=True, type=Path)
    archive_build.add_argument("--member-manifest", required=True, type=Path)
    archive_build.add_argument("--manifest-member", required=True)
    archive_build.add_argument("--output", required=True, type=Path)

    archive_verify = sub.add_parser("archive-extract-verify")
    archive_verify.add_argument("--archive", required=True, type=Path)
    archive_verify.add_argument("--destination", required=True, type=Path)
    archive_verify.add_argument("--manifest-relative", required=True)
    archive_verify.add_argument("--include", action="append", required=True)

    terminal = sub.add_parser("terminal")
    terminal.add_argument("--candidate", required=True, type=Path)
    terminal.add_argument("--lease", required=True, type=Path)
    terminal.add_argument("--job-root", required=True, type=Path)
    terminal.add_argument("--job-tag", required=True)
    terminal.add_argument("--preflight-rc", required=True, type=int)
    terminal.add_argument("--source-check-rc", required=True, type=int)
    terminal.add_argument("--f-rc", required=True, type=int)
    terminal.add_argument("--g-rc", required=True, type=int)
    terminal.add_argument("--pair-rc", required=True, type=int)
    terminal.add_argument("--emit-rc", required=True, type=int)
    terminal.add_argument("--candidate-rc", required=True, type=int)
    terminal.add_argument("--containment-identity-gate", required=True,
                          choices=("0", "1"))
    terminal.add_argument("--monitor-started", required=True,
                          choices=("0", "1"))
    terminal.add_argument("--monitor-stop-clean", required=True,
                          choices=("0", "1"))
    terminal.add_argument("--monitor-violations", required=True, type=Path)
    terminal.add_argument("--swap-violation", required=True,
                          choices=("0", "1"))
    terminal.add_argument("--swap-total", required=True, type=int)
    terminal.add_argument("--swap-free", required=True, type=int)
    terminal.add_argument("--whole-timeout", required=True, choices=("0", "1"))
    terminal.add_argument("--peer-cancelled", required=True,
                          choices=("0", "1"))
    terminal.add_argument("--oom-kill-count", required=True, type=int)
    terminal.add_argument("--cleanup-gate", required=True, choices=("0", "1"))
    terminal.add_argument("--pgid-census", required=True, type=Path)
    terminal.add_argument("--tag-census", required=True, type=Path)
    terminal.add_argument("--cgroup-final-gate", required=True,
                          choices=("0", "1"))
    terminal.add_argument("--manifest-generator-rc", required=True, type=int)
    terminal.add_argument("--manifest-replay-rc", required=True, type=int)
    terminal.add_argument("--archive-replay-rc", required=True, type=int)
    terminal.add_argument("--archive-ready", required=True, choices=("0", "1"))
    terminal.add_argument("--archive-sha-sidecar", required=True, type=Path)
    terminal.add_argument("--output", required=True, type=Path)

    args = parser.parse_args()

    if args.command == "lease-flock":
        try:
            fcntl.flock(args.fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            print("LEASE_FLOCK_ACQUIRED=0")
            return 1
        print("LEASE_FLOCK_ACQUIRED=1")
        return 0
    if args.command == "lease-record":
        launcher_pid = args.launcher_pid or os.getppid()
        lease = lease_record(args.fd, args.lock_path, args.job_root,
                             args.job_tag, args.archive_sha256,
                             args.registration, args.launcher_path,
                             launcher_pid, args.proc_root, args.output)
        print(lease["run_nonce"])
        return 0
    if args.command == "lease-probe":
        held = probe_lock_held(args.lock_path)
        print("LEASE_LOCK_HELD=%d" % int(held))
        return 0 if held else 1
    if args.command == "verify-lease":
        verify_lease(args.lease, args.job_root, args.job_tag,
                     expect_nonce=args.expect_nonce)
        print("LEASE_VERIFIED=1")
        return 0
    if args.command == "verify-fresh-namespace":
        verify_fresh_namespace(args.job_root)
        print("FRESH_NAMESPACE_VERIFIED=1")
        return 0
    if args.command == "pid-start":
        identity = read_identity(args.pid, args.proc_root)
        require(identity["uid"] == os.getuid(), "PID_IDENTITY_FOREIGN")
        print(identity["starttime"])
        return 0
    if args.command == "wait-pid":
        try:
            result = wait_for_exact_pid_exit(
                args.pid, args.starttime, args.timeout,
                proc_root=args.proc_root)
        except CustodyError as error:
            atomic_json(args.output,
                        {"ready_to_reap": False,
                         "terminal_state": "IDENTITY_FAILURE",
                         "error": str(error)})
            print("EXACT_PID_IDENTITY_FAILURE=1")
            return 2
        atomic_json(args.output, result)
        print("EXACT_PID_READY_TO_REAP=%d" % int(result["ready_to_reap"]))
        return 0 if result["ready_to_reap"] else 1
    if args.command == "signal-pid":
        record_identity = exact_pid_record(args.pid, args.starttime,
                                           args.proc_root)
        if record_identity is not None:
            signal_exact(record_identity,
                         signal.SIGTERM if args.signal == "TERM"
                         else signal.SIGKILL, args.proc_root)
        print("EXACT_PID_SIGNAL_PASS=1")
        return 0
    if args.command == "kill-tree":
        clean = kill_tree(args.pid, args.starttime, args.census_output,
                          args.proc_root)
        print("KILL_TREE_EMPTY=%d" % int(clean))
        return 0 if clean else 1
    if args.command == "cleanup":
        clean = terminate_and_census(
            args.pgid, args.job_tag, set(args.exclude_pid),
            args.pgid_output, args.tag_output, args.proc_root)
        print("CONTAINMENT_CENSUS_EMPTY=%d" % int(clean))
        return 0 if clean else 1
    if args.command == "cgroup-census":
        pids = parse_cgroup_procs(args.path)
        allowed = set(args.allow_pid) | {os.getpid()}
        remaining = [pid for pid in pids if pid not in allowed]
        atomic_json(args.output, remaining)
        print("CGROUP_PROCS_EMPTY=%d" % int(not remaining))
        return 0 if not remaining else 1
    if args.command == "monitor":
        return run_monitor(args)
    if args.command == "violations-census":
        names = violations_census(args.dir)
        require(names is not None, "VIOLATIONS_DIR_MISSING")
        atomic_json(args.output, names)
        print("MONITOR_VIOLATIONS_EMPTY=%d" % int(not names))
        return 0 if not names else 1
    if args.command == "manifest-build":
        count = build_complete_manifest(args.root, args.manifest, args.include)
        print("TERMINAL_MANIFEST_GENERATED_ENTRIES=%d" % count)
        return 0
    if args.command == "manifest-verify":
        count = verify_complete_manifest(args.root, args.manifest,
                                         args.include)
        print("TERMINAL_MANIFEST_REPLAYED_ENTRIES=%d" % count)
        return 0
    if args.command == "archive-build":
        digest = build_deterministic_archive(
            args.root, args.member_manifest, args.manifest_member,
            args.output)
        print(digest)
        return 0
    if args.command == "archive-extract-verify":
        count = extract_and_verify_archive(
            args.archive, args.destination, args.manifest_relative,
            args.include)
        print("TERMINAL_ARCHIVE_REPLAYED_ENTRIES=%d" % count)
        return 0
    if args.command == "terminal":
        return decide_terminal(args)
    raise CustodyError("UNKNOWN_COMMAND")


if __name__ == "__main__":
    raise SystemExit(main())
