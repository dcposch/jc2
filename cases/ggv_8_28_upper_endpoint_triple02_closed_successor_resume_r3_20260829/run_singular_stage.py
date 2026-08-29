#!/usr/bin/env python3
"""Run one Singular stage inside the already established job containment.

R2 custody contract: every stage is bound to exactly one job.  Before launch
the runner verifies the job tag and schema-checked nonce against its own
environment, the exact source-archive bytes, the exact Singular binary bytes,
the live worker and supervisor PID identities (start times), and its own
inherited PGID/SID.  After launch it verifies the Singular child shares the
runner's PGID/SID/uid/cgroup.  The identity record and the result record both
carry the complete binding; the result hashes the identity record, so a stage
record cannot be copied from another job without detection.

The supervisor owns the job scope/process group.  This runner deliberately
does not create a session or process group: doing so would let Singular escape
the supervisor's kill boundary.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import signal
import subprocess
import time


NONCE_RE = re.compile(r"^[a-z0-9]{8,32}$")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def proc_identity(pid: int) -> dict[str, int]:
    stat = Path(f"/proc/{pid}/stat").read_text()
    close = stat.rfind(")")
    if close < 0:
        raise RuntimeError("MALFORMED_PROC_STAT")
    fields = stat[close + 2:].split()
    status = Path(f"/proc/{pid}/status").read_text().splitlines()
    uid_line = next(line for line in status if line.startswith("Uid:"))
    return {
        "pid": pid,
        "ppid": int(fields[1]),
        "pgid": int(fields[2]),
        "sid": int(fields[3]),
        "starttime": int(fields[19]),
        "uid": int(uid_line.split()[1]),
    }


def proc_cgroup(pid: int) -> str:
    return Path(f"/proc/{pid}/cgroup").read_text()


def descendants(root_pid: int) -> list[dict[str, int]]:
    """Return a best-effort, deepest-first Linux descendant census."""
    identities: dict[int, dict[str, int]] = {}
    for entry in Path("/proc").iterdir():
        if not entry.name.isdigit():
            continue
        try:
            ident = proc_identity(int(entry.name))
        except (FileNotFoundError, PermissionError, ProcessLookupError,
                RuntimeError, ValueError):
            continue
        identities[ident["pid"]] = ident
    selected: list[tuple[int, int]] = []
    for pid in identities:
        depth = 0
        cursor = pid
        seen: set[int] = set()
        while cursor in identities and cursor not in seen:
            seen.add(cursor)
            cursor = identities[cursor]["ppid"]
            depth += 1
            if cursor == root_pid:
                selected.append((depth, pid))
                break
    return [identities[pid] for _, pid in sorted(selected, reverse=True)]


def signal_exact(identity: dict[str, int], sig: signal.Signals) -> None:
    try:
        current = proc_identity(identity["pid"])
    except (FileNotFoundError, PermissionError, ProcessLookupError,
            StopIteration, RuntimeError, ValueError):
        return
    if (current["starttime"] != identity["starttime"]
            or current["uid"] != os.getuid()):
        raise RuntimeError("STAGE_PID_IDENTITY_CHANGED_OR_FOREIGN")
    os.kill(identity["pid"], sig)


def terminate_tree(process: subprocess.Popen[bytes]) -> None:
    """Terminate only the stage tree; the supervisor later audits the job."""
    for sig in (signal.SIGTERM, signal.SIGKILL):
        try:
            root_identity = proc_identity(process.pid)
        except (FileNotFoundError, ProcessLookupError):
            return
        for identity in descendants(process.pid) + [root_identity]:
            try:
                signal_exact(identity, sig)
            except ProcessLookupError:
                pass
        try:
            process.wait(timeout=15)
            return
        except subprocess.TimeoutExpired:
            continue
    process.wait()


def require_live_identity(pid: int, starttime: int, label: str) -> dict[str, int]:
    identity = proc_identity(pid)
    if identity["starttime"] != starttime or identity["uid"] != os.getuid():
        raise SystemExit(f"STAGE_{label}_IDENTITY_DISAGREEMENT")
    return identity


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--singular", required=True, type=Path)
    parser.add_argument("--script", required=True, type=Path)
    parser.add_argument("--cwd", required=True, type=Path)
    parser.add_argument("--stdout", required=True, type=Path)
    parser.add_argument("--stderr", required=True, type=Path)
    parser.add_argument("--result", required=True, type=Path)
    parser.add_argument("--identity", required=True, type=Path)
    parser.add_argument("--cap-seconds", required=True, type=int)
    parser.add_argument("--expected-pgid", required=True, type=int)
    parser.add_argument("--expected-sid", required=True, type=int)
    parser.add_argument("--job-tag", required=True)
    parser.add_argument("--job-nonce", required=True)
    parser.add_argument("--stage-label", required=True)
    parser.add_argument("--lease", required=True, type=Path)
    parser.add_argument("--source-archive", required=True, type=Path)
    parser.add_argument("--source-archive-sha256", required=True)
    parser.add_argument("--singular-sha256", required=True)
    parser.add_argument("--supervisor-pid", required=True, type=int)
    parser.add_argument("--supervisor-starttime", required=True, type=int)
    parser.add_argument("--worker-pid", required=True, type=int)
    parser.add_argument("--worker-starttime", required=True, type=int)
    args = parser.parse_args()
    if args.cap_seconds <= 0:
        raise SystemExit("NONPOSITIVE_STAGE_CAP")
    if not NONCE_RE.fullmatch(args.job_nonce):
        raise SystemExit("STAGE_JOB_NONCE_SCHEMA")
    if not args.job_tag.endswith("_" + args.job_nonce):
        raise SystemExit("STAGE_JOB_TAG_NONCE_DISAGREEMENT")
    if os.environ.get("JOB_TAG") != args.job_tag:
        raise SystemExit("STAGE_JOB_TAG_ENV_DISAGREEMENT")
    if os.environ.get("JOB_NONCE") != args.job_nonce:
        raise SystemExit("STAGE_JOB_NONCE_ENV_DISAGREEMENT")
    singular_path = args.singular.resolve()
    actual_singular_sha = sha256(singular_path)
    if actual_singular_sha != args.singular_sha256:
        raise SystemExit("STAGE_SINGULAR_BINARY_SHA_DISAGREEMENT")
    actual_source_sha = sha256(args.source_archive.resolve())
    if actual_source_sha != args.source_archive_sha256:
        raise SystemExit("STAGE_SOURCE_ARCHIVE_SHA_DISAGREEMENT")
    lease_sha = sha256(args.lease.resolve())
    worker_identity = require_live_identity(
        args.worker_pid, args.worker_starttime, "WORKER")
    supervisor_identity = require_live_identity(
        args.supervisor_pid, args.supervisor_starttime, "SUPERVISOR")
    runner_identity = proc_identity(os.getpid())
    if (runner_identity["pgid"] != args.expected_pgid
            or runner_identity["sid"] != args.expected_sid):
        raise SystemExit("STAGE_RUNNER_CONTAINMENT_DISAGREEMENT")
    runner_cgroup = proc_cgroup(os.getpid())
    script_path = args.script.resolve()
    argv = [str(singular_path), "-q", str(script_path)]
    started = time.time()
    with args.stdout.open("wb") as stdout, args.stderr.open("wb") as stderr:
        process = subprocess.Popen(
            argv, cwd=args.cwd.resolve(), stdout=stdout, stderr=stderr)
        child_identity = proc_identity(process.pid)
        child_cgroup = proc_cgroup(process.pid)
        if (child_identity["pgid"] != args.expected_pgid
                or child_identity["sid"] != args.expected_sid
                or child_identity["uid"] != os.getuid()
                or child_cgroup != runner_cgroup):
            terminate_tree(process)
            raise SystemExit("SINGULAR_CHILD_CONTAINMENT_DISAGREEMENT")
        args.identity.write_text(json.dumps({
            "argv": argv,
            "cap_seconds": args.cap_seconds,
            "expected_pgid": args.expected_pgid,
            "expected_sid": args.expected_sid,
            "job_nonce": args.job_nonce,
            "job_tag": args.job_tag,
            "lease_sha256": lease_sha,
            "runner": runner_identity,
            "runner_cgroup": runner_cgroup,
            "singular": child_identity,
            "singular_binary_sha256": actual_singular_sha,
            "singular_cgroup": child_cgroup,
            "singular_path": str(singular_path),
            "source_archive_sha256": actual_source_sha,
            "stage_label": args.stage_label,
            "supervisor": supervisor_identity,
            "worker": worker_identity,
        }, indent=2, sort_keys=True) + "\n")
        try:
            returncode = process.wait(timeout=args.cap_seconds)
            timed_out = False
        except subprocess.TimeoutExpired:
            timed_out = True
            terminate_tree(process)
            returncode = 124
    payload = {
        "argv": argv,
        "cap_seconds": args.cap_seconds,
        "elapsed_seconds": round(time.time() - started, 6),
        "expected_pgid": args.expected_pgid,
        "expected_sid": args.expected_sid,
        "identity_sha256": sha256(args.identity),
        "job_nonce": args.job_nonce,
        "job_tag": args.job_tag,
        "lease_sha256": lease_sha,
        "returncode": returncode,
        "script_sha256": sha256(script_path),
        "singular_sha256": actual_singular_sha,
        "source_archive_sha256": actual_source_sha,
        "stage_label": args.stage_label,
        "stderr_sha256": sha256(args.stderr),
        "stdout_sha256": sha256(args.stdout),
        "supervisor_starttime": args.supervisor_starttime,
        "timed_out": timed_out,
        "worker_starttime": args.worker_starttime,
    }
    args.result.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(f"SINGULAR_STAGE_RETURNCODE={returncode}")
    print(f"SINGULAR_STAGE_TIMED_OUT={int(timed_out)}")
    print(f"SINGULAR_STAGE_ELAPSED_SECONDS={payload['elapsed_seconds']}")
    return returncode


if __name__ == "__main__":
    raise SystemExit(main())
