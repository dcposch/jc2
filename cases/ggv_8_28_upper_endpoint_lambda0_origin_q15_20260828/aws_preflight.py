#!/usr/bin/env python3
"""Fail-closed identity, resource, swap, and idle-job preflight."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import shutil
import sys
import time


HOSTS = {
    "r6a": ("ip-172-30-0-34", "i-02cb2b4a379ffcc64"),
    "r6b": ("ip-172-30-0-106", "i-0f089e64c378f5da3"),
}
PRODUCT = "r6i.16xlarge"
MIN_AVAILABLE_KIB = 450 * 1024 * 1024
MIN_DISK_BYTES = 100 * 1024**3


def proc_stat(pid):
    text = Path(f"/proc/{pid}/stat").read_text()
    fields = text[text.rfind(")") + 2:].split()
    return {"ppid": int(fields[1]), "pgrp": int(fields[2]),
            "session": int(fields[3]), "starttime": int(fields[19])}


def ancestors():
    found = {os.getpid()}
    current = os.getpid()
    while current > 1:
        try:
            current = proc_stat(current)["ppid"]
        except (FileNotFoundError, PermissionError, ProcessLookupError):
            break
        found.add(current)
    return found


def meminfo():
    out = {}
    for line in Path("/proc/meminfo").read_text().splitlines():
        key, rest = line.split(":", 1)
        out[key] = int(rest.split()[0])
    return out


def conflicts(run_dir):
    own = ancestors()
    tokens = ("python", "sage", "singular", "msolve", "magma", "maple",
              "mathematica", "/home/ubuntu/jobs/", "/home/ubuntu/runs/",
              "timeout", "prlimit")
    found = []
    for entry in Path("/proc").iterdir():
        if not entry.name.isdigit() or int(entry.name) in own:
            continue
        try:
            status = dict(line.split(":", 1) for line in
                          (entry / "status").read_text().splitlines() if ":" in line)
            if int(status["Uid"].split()[0]) != os.getuid():
                continue
            command = (entry / "cmdline").read_bytes().replace(
                b"\0", b" "
            ).decode(errors="replace")
            rss = int(status.get("VmRSS", "0 kB").split()[0])
        except (FileNotFoundError, PermissionError, ProcessLookupError,
                KeyError, ValueError):
            continue
        if str(run_dir) in command:
            continue
        lowered = command.lower()
        if rss >= 1024 * 1024 or any(token in lowered for token in tokens):
            found.append({"pid": int(entry.name), "rss_kib": rss,
                          "command": command})
    return found


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--job-tag", required=True)
    parser.add_argument("--host-alias", choices=tuple(HOSTS), required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    run_dir = args.run_dir.resolve()
    expected_host, expected_instance = HOSTS[args.host_alias]
    memory = meminfo()
    disk = shutil.disk_usage(run_dir).free
    other = conflicts(run_dir)
    facts = {
        "utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "platform": sys.platform, "host_alias": args.host_alias,
        "host": os.uname().nodename,
        "vendor": Path("/sys/class/dmi/id/sys_vendor").read_text().strip(),
        "product": Path("/sys/class/dmi/id/product_name").read_text().strip(),
        "instance_id": Path("/sys/class/dmi/id/board_asset_tag").read_text().strip(),
        "nproc": os.cpu_count(), "job_tag": args.job_tag,
        "run_dir": str(run_dir), "mem_available_kib": memory["MemAvailable"],
        "swap_total_kib": memory["SwapTotal"],
        "swap_free_kib": memory["SwapFree"],
        "disk_available_bytes": disk, "conflicts": other,
    }
    checks = {
        "linux": sys.platform.startswith("linux"),
        "vendor": facts["vendor"] == "Amazon EC2",
        "host": facts["host"] == expected_host,
        "product": facts["product"] == PRODUCT,
        "instance": facts["instance_id"] == expected_instance,
        "cpu_count": facts["nproc"] == 64,
        "tag": (args.job_tag == run_dir.name
                and os.environ.get("AWS_RUN_TAG") == args.job_tag),
        "memory": memory["MemAvailable"] >= MIN_AVAILABLE_KIB,
        "zero_swap": memory["SwapTotal"] == 0 and memory["SwapFree"] == 0,
        "disk": disk >= MIN_DISK_BYTES,
        "idle": not other,
    }
    facts["checks"] = checks
    facts["pass"] = all(checks.values())
    args.output.write_text(json.dumps(facts, indent=2, sort_keys=True) + "\n")
    print(json.dumps(facts, sort_keys=True))
    if not facts["pass"]:
        raise SystemExit(40)


if __name__ == "__main__":
    main()
