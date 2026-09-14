#!/usr/bin/env python3
"""Keep the last readable cgroup event counters through solver shutdown."""
import json
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

SCRATCH = Path("/home/ubuntu/classA-smallest-20260906.xpXroy")
UNITS = ("jc2-classa-a-guided", "jc2-classa-c-singular")
TARGET = SCRATCH / "results" / "resource_watch_latest.json"


def utcnow():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def show(unit):
    keys = (
        "ActiveState", "SubState", "Result", "ExecMainStatus", "ExecMainPID",
        "ExecMainStartTimestamp", "ExecMainExitTimestamp", "MemoryCurrent",
        "MemoryPeak", "MemoryHigh", "MemoryMax", "MemorySwapMax",
        "CPUUsageNSec",
    )
    raw = subprocess.run(
        ["systemctl", "show", unit, *sum((["-p", key] for key in keys), [])],
        check=False, capture_output=True, text=True,
    ).stdout
    return dict(line.split("=", 1) for line in raw.splitlines() if "=" in line)


def event_data(unit, prior):
    path = Path("/sys/fs/cgroup/system.slice") / f"{unit}.service" / "memory.events"
    if not path.exists():
        return prior
    return {key: int(value) for key, value in
            (line.split() for line in path.read_text().splitlines())}


def main():
    last_events = {unit: {} for unit in UNITS}
    began = utcnow()
    while True:
        units = {}
        active = False
        for unit in UNITS:
            status = show(unit)
            last_events[unit] = event_data(unit, last_events[unit])
            units[unit] = {"systemd": status, "last_readable_memory_events": last_events[unit]}
            active |= status.get("ActiveState") == "active"
        payload = {"watch_began_utc": began, "sample_utc": utcnow(), "units": units}
        tmp = TARGET.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
        tmp.replace(TARGET)
        if not active:
            return
        time.sleep(0.5)


if __name__ == "__main__":
    main()
