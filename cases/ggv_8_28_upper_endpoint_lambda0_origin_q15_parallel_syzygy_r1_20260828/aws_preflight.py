#!/usr/bin/env python3
"""Fail-closed idle EC2 preflight for the parallel origin portfolio."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import shutil
import sys
import time


HOSTS = {
    "box03": ("ip-172-30-0-249", "i-0ece0b9a3b4a7512f"),
    "r6a": ("ip-172-30-0-34", "i-02cb2b4a379ffcc64"),
    "r6b": ("ip-172-30-0-106", "i-0f089e64c378f5da3"),
    "r6c": ("ip-172-30-0-150", "i-040b7a1c2ed72d4cc"),
    "r6d": ("ip-172-30-0-45", "i-07eeaf8ba6f0bc419"),
}


def proc_stat(pid):
    text = Path(f"/proc/{pid}/stat").read_text()
    suffix = text[text.rfind(")") + 2:].split()
    return {"ppid": int(suffix[1]), "pgrp": int(suffix[2]),
            "session": int(suffix[3]), "starttime": int(suffix[19])}


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


def memory():
    values = {}
    for line in Path("/proc/meminfo").read_text().splitlines():
        key, rest = line.split(":", 1)
        values[key] = int(rest.split()[0])
    return values


def conflicts(run_dir):
    own = ancestors()
    tokens = ("python", "sage", "singular", "msolve", "magma", "maple",
              "mathematica", "/home/ubuntu/jobs/", "timeout", "prlimit")
    found = []
    for entry in Path("/proc").iterdir():
        if not entry.name.isdigit() or int(entry.name) in own:
            continue
        try:
            status = {line.split(":", 1)[0]: line.split(":", 1)[1].strip()
                      for line in (entry / "status").read_text().splitlines() if ":" in line}
            if int(status["Uid"].split()[0]) != os.getuid():
                continue
            command = (entry / "cmdline").read_bytes().replace(b"\0", b" ").decode(errors="replace")
            rss = int(status.get("VmRSS", "0 kB").split()[0])
        except (FileNotFoundError, PermissionError, ProcessLookupError, KeyError, ValueError):
            continue
        if str(run_dir) in command:
            continue
        if rss >= 1024 * 1024 or any(token in command.lower() for token in tokens):
            found.append({"pid": int(entry.name), "rss_kib": rss, "command": command})
    return found


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--job-tag", required=True)
    parser.add_argument("--host-alias", choices=sorted(HOSTS), required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    expected_host, expected_instance = HOSTS[args.host_alias]
    run_dir = args.run_dir.resolve()
    mem = memory()
    disk = shutil.disk_usage(run_dir).free
    facts = {
        "utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "platform": sys.platform,
        "host": os.uname().nodename,
        "vendor": Path("/sys/class/dmi/id/sys_vendor").read_text().strip(),
        "product": Path("/sys/class/dmi/id/product_name").read_text().strip(),
        "instance": Path("/sys/class/dmi/id/board_asset_tag").read_text().strip(),
        "nproc": os.cpu_count(), "host_alias": args.host_alias,
        "job_tag": args.job_tag, "run_dir": str(run_dir),
        "mem_available_kib": mem["MemAvailable"],
        "swap_total_kib": mem["SwapTotal"], "swap_free_kib": mem["SwapFree"],
        "disk_available_bytes": disk,
    }
    active = conflicts(run_dir)
    checks = {
        "linux": sys.platform.startswith("linux"),
        "vendor": facts["vendor"] == "Amazon EC2",
        "product": facts["product"] == "r6i.16xlarge",
        "host": facts["host"] == expected_host,
        "instance": facts["instance"] == expected_instance,
        "nproc": facts["nproc"] == 64,
        "job_tag": args.job_tag == run_dir.name and os.environ.get("AWS_RUN_TAG") == args.job_tag,
        "memory": mem["MemAvailable"] >= 450 * 1024 * 1024,
        "zero_swap": mem["SwapTotal"] == 0 and mem["SwapFree"] == 0,
        "disk": disk >= 50 * 1024**3,
        "idle": not active,
    }
    facts["conflicts"] = active
    facts["checks"] = checks
    facts["pass"] = all(checks.values())
    args.output.write_text(json.dumps(facts, indent=2, sort_keys=True) + "\n")
    print(json.dumps(facts, sort_keys=True))
    if not facts["pass"]:
        raise SystemExit(40)


if __name__ == "__main__":
    main()
