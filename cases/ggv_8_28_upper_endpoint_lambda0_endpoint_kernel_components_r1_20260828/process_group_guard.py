#!/usr/bin/env python3
"""Monitor and stop only the registered one-session/one-PGID worker tree."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import signal
import time
from pathlib import Path


MIN_MEM_AVAILABLE_KIB = 16 * 1024 * 1024


def proc_stat(pid):
    text = Path(f"/proc/{pid}/stat").read_text()
    suffix = text[text.rfind(")") + 2 :].split()
    return {
        "ppid": int(suffix[1]),
        "pgrp": int(suffix[2]),
        "session": int(suffix[3]),
        "starttime": int(suffix[19]),
    }


def proc_rss(pid):
    for line in Path(f"/proc/{pid}/status").read_text().splitlines():
        if line.startswith("VmRSS:"):
            return int(line.split()[1])
    return 0


def members(pgid):
    found = []
    for entry in Path("/proc").iterdir():
        if not entry.name.isdigit():
            continue
        pid = int(entry.name)
        try:
            stat = proc_stat(pid)
            if stat["pgrp"] == pgid:
                found.append({"pid": pid, **stat, "rss_kib": proc_rss(pid)})
        except (FileNotFoundError, PermissionError, ProcessLookupError):
            continue
    return sorted(found, key=lambda item: item["pid"])


def read_registry(path):
    fields = path.read_text().strip().split("\t")
    assert len(fields) == 7, fields
    label, pid, pgid, session, starttime, namespace, source_sha = fields
    record = {
        "label": label,
        "pid": int(pid),
        "pgid": int(pgid),
        "session": int(session),
        "starttime": int(starttime),
        "namespace": str(Path(namespace).resolve()),
        "source_sha256": source_sha,
    }
    assert record["pid"] == record["pgid"] == record["session"]
    assert record["pid"] > 1 and len(source_sha) == 64
    return record


def validate(record, allow_leader_absent=True):
    group = members(record["pgid"])
    if not group:
        return group
    assert all(item["pgrp"] == record["pgid"] and item["session"] == record["session"] for item in group)
    leader = next((item for item in group if item["pid"] == record["pid"]), None)
    if leader is None:
        assert allow_leader_absent
    else:
        assert leader["starttime"] == record["starttime"]
        command = Path(f"/proc/{leader['pid']}/cmdline").read_bytes().replace(b"\0", b" ").decode(errors="replace")
        assert record["namespace"] in command
    return group


def memory():
    values = {}
    for line in Path("/proc/meminfo").read_text().splitlines():
        key, rest = line.split(":", 1)
        values[key] = int(rest.split()[0])
    return values


def snapshot(record):
    group = validate(record)
    mem = memory()
    return {
        "utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "validated": True,
        "member_count": len(group),
        "member_pids": [item["pid"] for item in group],
        "group_rss_kib": sum(item["rss_kib"] for item in group),
        "mem_available_kib": mem["MemAvailable"],
        "swap_total_kib": mem["SwapTotal"],
        "swap_free_kib": mem["SwapFree"],
        "disk_available_bytes": shutil.disk_usage(record["namespace"]).free,
    }


def stop(record, grace):
    group = validate(record)
    if not group:
        return {"term_sent": False, "kill_sent": False, "remaining": []}
    os.killpg(record["pgid"], signal.SIGTERM)
    deadline = time.monotonic() + grace
    while time.monotonic() < deadline and members(record["pgid"]):
        time.sleep(0.1)
    remaining = validate(record)
    kill_sent = False
    if remaining:
        os.killpg(record["pgid"], signal.SIGKILL)
        kill_sent = True
        time.sleep(0.25)
    final = members(record["pgid"])
    assert not final, final
    return {"term_sent": True, "kill_sent": kill_sent, "remaining": []}


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    for command in ("snapshot", "monitor", "stop"):
        subparser = subparsers.add_parser(command)
        subparser.add_argument("--registry", type=Path, required=True)
        subparser.add_argument("--grace-seconds", type=float, default=30)
    arguments = parser.parse_args()
    record = read_registry(arguments.registry)
    if arguments.command == "snapshot":
        print(json.dumps(snapshot(record), sort_keys=True))
        return
    if arguments.command == "stop":
        print(json.dumps({"status": "STOP_VALIDATED", **stop(record, arguments.grace_seconds)}, sort_keys=True))
        return
    while True:
        state = snapshot(record)
        print(json.dumps({"type": "TELEMETRY", **state}, sort_keys=True), flush=True)
        if state["member_count"] == 0:
            print(json.dumps({"type": "MONITOR_COMPLETE"}, sort_keys=True), flush=True)
            return
        violation = None
        if state["mem_available_kib"] < MIN_MEM_AVAILABLE_KIB:
            violation = "MEM_AVAILABLE_FLOOR"
        elif state["swap_total_kib"] != 0 or state["swap_free_kib"] != 0:
            violation = "SWAP_NONZERO"
        elif state["disk_available_bytes"] < 10 * 1024**3:
            violation = "DISK_AVAILABLE_FLOOR"
        if violation:
            event = stop(record, arguments.grace_seconds)
            print(json.dumps({"type": "GUARD_TRIGGER", "violation": violation, **event}, sort_keys=True), flush=True)
            raise SystemExit(9)
        time.sleep(10)


if __name__ == "__main__":
    main()
