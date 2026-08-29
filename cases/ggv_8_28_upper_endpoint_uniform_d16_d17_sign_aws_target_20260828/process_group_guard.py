#!/usr/bin/env python3
"""Validate, monitor, and stop only registered namespace-owned process groups."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import signal
import time
from pathlib import Path


def proc_stat(pid):
    text = Path(f"/proc/{pid}/stat").read_text()
    suffix = text[text.rfind(")") + 2:].split()
    return {
        "pgrp": int(suffix[2]),
        "starttime": int(suffix[19]),
    }


def proc_cmdline(pid):
    return Path(f"/proc/{pid}/cmdline").read_bytes().replace(b"\0", b" ").decode(
        errors="replace")


def proc_rss_kib(pid):
    for line in Path(f"/proc/{pid}/status").read_text().splitlines():
        if line.startswith("VmRSS:"):
            return int(line.split()[1])
    return 0


def group_members(pgid):
    members = []
    for entry in Path("/proc").iterdir():
        if not entry.name.isdigit():
            continue
        pid = int(entry.name)
        try:
            stat = proc_stat(pid)
            if stat["pgrp"] == pgid:
                members.append({
                    "pid": pid,
                    "starttime": stat["starttime"],
                    "cmdline": proc_cmdline(pid),
                    "rss_kib": proc_rss_kib(pid),
                })
        except (FileNotFoundError, ProcessLookupError, PermissionError):
            continue
    return sorted(members, key=lambda item: item["pid"])


def read_registry(path):
    records = []
    for line in path.read_text().splitlines():
        if not line.strip():
            continue
        fields = line.split("\t")
        assert len(fields) == 6, fields
        label, pid, pgid, starttime, marker, job_sha256 = fields
        records.append({
            "label": label,
            "pid": int(pid),
            "pgid": int(pgid),
            "starttime": int(starttime),
            "marker": str(Path(marker).resolve()),
            "job_sha256": job_sha256,
        })
    assert len({record["label"] for record in records}) == len(records)
    return records


def validate_group(record, allow_empty=True):
    assert record["pid"] == record["pgid"] and record["pgid"] > 1
    members = group_members(record["pgid"])
    if not members:
        assert allow_empty
        return members
    leader = next((member for member in members if member["pid"] == record["pid"]), None)
    assert leader is not None
    assert leader["starttime"] == record["starttime"]
    marker = record["marker"]
    for member in members:
        assert marker in member["cmdline"], (record["label"], member)
    return members


def memory_info():
    values = {}
    for line in Path("/proc/meminfo").read_text().splitlines():
        key, rest = line.split(":", 1)
        values[key] = int(rest.split()[0])
    return {
        "mem_available_kib": values["MemAvailable"],
        "swap_total_kib": values["SwapTotal"],
        "swap_used_kib": values["SwapTotal"] - values["SwapFree"],
    }


def snapshot(records):
    groups = []
    for record in records:
        members = validate_group(record)
        groups.append({
            "label": record["label"],
            "pid": record["pid"],
            "pgid": record["pgid"],
            "member_count": len(members),
            "member_pids": [member["pid"] for member in members],
            "leader_rss_kib": next((member["rss_kib"] for member in members
                                    if member["pid"] == record["pid"]), 0),
            "group_rss_kib": sum(member["rss_kib"] for member in members),
            "validated": True,
        })
    marker = Path(records[0]["marker"] if records else ".")
    disk = shutil.disk_usage(marker)
    return {
        "utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        **memory_info(),
        "disk_available_bytes": disk.free,
        "groups": groups,
    }


def stop_group(record, grace_seconds):
    members = validate_group(record)
    if not members:
        return {"label": record["label"], "validated": True,
                "term_sent": False, "kill_sent": False, "remaining": []}
    term_members = [member["pid"] for member in members]
    os.killpg(record["pgid"], signal.SIGTERM)
    deadline = time.monotonic() + grace_seconds
    while time.monotonic() < deadline and group_members(record["pgid"]):
        time.sleep(0.1)
    remaining = group_members(record["pgid"])
    kill_sent = False
    if remaining:
        # Revalidate the namespace and leader identity before escalation.
        validate_group(record, allow_empty=False)
        os.killpg(record["pgid"], signal.SIGKILL)
        kill_sent = True
        time.sleep(0.2)
    final = group_members(record["pgid"])
    return {
        "label": record["label"],
        "validated": True,
        "term_sent": True,
        "term_member_pids": term_members,
        "kill_sent": kill_sent,
        "remaining": [member["pid"] for member in final],
    }


def command_snapshot(arguments):
    records = read_registry(arguments.registry)
    print(json.dumps(snapshot(records), sort_keys=True))


def command_stop(arguments):
    records = read_registry(arguments.registry)
    events = [stop_group(record, arguments.grace_seconds) for record in records]
    assert all(not event["remaining"] for event in events)
    print(json.dumps({"status": "STOP_VALIDATED", "events": events}, sort_keys=True))


def command_monitor(arguments):
    records = read_registry(arguments.registry)
    while True:
        state = snapshot(records)
        print(json.dumps({"type": "TELEMETRY", **state}, sort_keys=True), flush=True)
        active = sum(group["member_count"] for group in state["groups"])
        if not active:
            print(json.dumps({"type": "MONITOR_COMPLETE"}, sort_keys=True), flush=True)
            return
        violation = None
        if state["mem_available_kib"] < arguments.mem_floor_gib * 1024 * 1024:
            violation = "MEM_AVAILABLE_FLOOR"
        elif state["swap_total_kib"] != 0 or state["swap_used_kib"] != 0:
            violation = "SWAP_NONZERO"
        elif state["disk_available_bytes"] < arguments.disk_floor_gib * 1024 ** 3:
            violation = "DISK_AVAILABLE_FLOOR"
        if violation:
            events = [stop_group(record, arguments.grace_seconds) for record in records]
            print(json.dumps({"type": "GUARD_TRIGGER", "violation": violation,
                              "events": events}, sort_keys=True), flush=True)
            raise SystemExit(9)
        time.sleep(arguments.interval_seconds)


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    snapshot_parser = subparsers.add_parser("snapshot")
    snapshot_parser.add_argument("--registry", type=Path, required=True)
    snapshot_parser.set_defaults(function=command_snapshot)
    stop_parser = subparsers.add_parser("stop")
    stop_parser.add_argument("--registry", type=Path, required=True)
    stop_parser.add_argument("--grace-seconds", type=float, default=5)
    stop_parser.set_defaults(function=command_stop)
    monitor_parser = subparsers.add_parser("monitor")
    monitor_parser.add_argument("--registry", type=Path, required=True)
    monitor_parser.add_argument("--interval-seconds", type=float, default=30)
    monitor_parser.add_argument("--mem-floor-gib", type=int, default=150)
    monitor_parser.add_argument("--disk-floor-gib", type=int, default=50)
    monitor_parser.add_argument("--grace-seconds", type=float, default=30)
    monitor_parser.set_defaults(function=command_monitor)
    arguments = parser.parse_args()
    arguments.function(arguments)


if __name__ == "__main__":
    main()
