#!/usr/bin/env python3
"""Run one Singular stage inside the already established job containment.

The supervisor owns the job scope/process group.  This runner deliberately
does not create a session or process group: doing so would let Singular escape
the supervisor's kill boundary.  The inherited PGID/SID are checked before
and immediately after launch and recorded with Linux process start times.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import time


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


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
    args = parser.parse_args()
    if args.cap_seconds <= 0:
        raise SystemExit("NONPOSITIVE_STAGE_CAP")
    if os.environ.get("JOB_TAG") != args.job_tag:
        raise SystemExit("STAGE_JOB_TAG_ENV_DISAGREEMENT")
    runner_identity = proc_identity(os.getpid())
    if (runner_identity["pgid"] != args.expected_pgid
            or runner_identity["sid"] != args.expected_sid):
        raise SystemExit("STAGE_RUNNER_CONTAINMENT_DISAGREEMENT")
    started = time.time()
    with args.stdout.open("wb") as stdout, args.stderr.open("wb") as stderr:
        process = subprocess.Popen(
            [str(args.singular), "-q", str(args.script.resolve())],
            cwd=args.cwd.resolve(), stdout=stdout, stderr=stderr)
        child_identity = proc_identity(process.pid)
        if (child_identity["pgid"] != args.expected_pgid
                or child_identity["sid"] != args.expected_sid):
            terminate_tree(process)
            raise SystemExit("SINGULAR_CHILD_CONTAINMENT_DISAGREEMENT")
        args.identity.write_text(json.dumps({
            "job_tag": args.job_tag,
            "runner": runner_identity,
            "singular": child_identity,
        }, indent=2, sort_keys=True) + "\n")
        try:
            returncode = process.wait(timeout=args.cap_seconds)
            timed_out = False
        except subprocess.TimeoutExpired:
            timed_out = True
            terminate_tree(process)
            returncode = 124
    payload = {
        "argv": [str(args.singular), "-q", str(args.script.resolve())],
        "cap_seconds": args.cap_seconds,
        "elapsed_seconds": round(time.time() - started, 6),
        "returncode": returncode,
        "script_sha256": sha256(args.script.resolve()),
        "stderr_sha256": sha256(args.stderr),
        "stdout_sha256": sha256(args.stdout),
        "timed_out": timed_out,
    }
    args.result.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(f"SINGULAR_STAGE_RETURNCODE={returncode}")
    print(f"SINGULAR_STAGE_TIMED_OUT={int(timed_out)}")
    print(f"SINGULAR_STAGE_ELAPSED_SECONDS={payload['elapsed_seconds']}")
    return returncode


if __name__ == "__main__":
    raise SystemExit(main())
