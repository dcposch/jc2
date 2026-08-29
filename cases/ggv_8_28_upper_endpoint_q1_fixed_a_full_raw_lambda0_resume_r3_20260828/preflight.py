#!/usr/bin/env python3
"""Fail-closed EC2 identity, resource, swap, and idle-process preflight."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import shutil
import sys
import time


HOSTS = {
    "resume_lambda0": {
        "host": "ip-172-30-0-34",
        "product": "r6i.16xlarge",
        "instance": "i-02cb2b4a379ffcc64",
    },
    "compile_lambda1": {
        "host": "ip-172-30-0-45",
        "product": "r6i.16xlarge",
        "instance": "i-07eeaf8ba6f0bc419",
    },
}
MIN_AVAILABLE_KIB = 450 * 1024 * 1024
MIN_DISK_BYTES = 100 * 1024**3


def proc_stat(pid):
    text = Path(f"/proc/{pid}/stat").read_text()
    suffix = text[text.rfind(")") + 2 :].split()
    return {"ppid": int(suffix[1]), "pgrp": int(suffix[2]),
            "session": int(suffix[3]), "starttime": int(suffix[19])}


def own_ancestors():
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
    values = {}
    for line in Path("/proc/meminfo").read_text().splitlines():
        key, rest = line.split(":", 1)
        values[key] = int(rest.split()[0])
    return values


def user_job_conflicts(run_dir):
    ancestors = own_ancestors()
    conflicts = []
    tokens = (
        "python", "sage", "singular", "msolve", "magma", "maple",
        "mathematica", "/home/ubuntu/jobs/", "timeout", "prlimit",
    )
    for entry in Path("/proc").iterdir():
        if not entry.name.isdigit():
            continue
        pid = int(entry.name)
        if pid in ancestors:
            continue
        try:
            status = {}
            for line in (entry / "status").read_text().splitlines():
                if ":" in line:
                    key, value = line.split(":", 1)
                    status[key] = value.strip()
            uid = int(status["Uid"].split()[0])
            command = (entry / "cmdline").read_bytes().replace(b"\0", b" ").decode(errors="replace")
            rss = int(status.get("VmRSS", "0 kB").split()[0])
        except (FileNotFoundError, PermissionError, ProcessLookupError, KeyError, ValueError):
            continue
        if uid != os.getuid() or str(run_dir) in command:
            continue
        lowered = command.lower()
        if rss >= 1024 * 1024 or any(token in lowered for token in tokens):
            conflicts.append({"pid": pid, "rss_kib": rss, "command": command})
    return conflicts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--job-tag", required=True)
    parser.add_argument("--mode", choices=sorted(HOSTS), required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    run_dir = args.run_dir.resolve()
    expected = HOSTS[args.mode]
    memory = meminfo()
    disk_free = shutil.disk_usage(run_dir).free
    facts = {
        "utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "platform": sys.platform,
        "host": os.uname().nodename,
        "vendor": Path("/sys/class/dmi/id/sys_vendor").read_text().strip(),
        "product": Path("/sys/class/dmi/id/product_name").read_text().strip(),
        "instance_id": Path("/sys/class/dmi/id/board_asset_tag").read_text().strip(),
        "nproc": os.cpu_count(),
        "job_tag": args.job_tag,
        "mode": args.mode,
        "run_dir": str(run_dir),
        "mem_available_kib": memory["MemAvailable"],
        "swap_total_kib": memory["SwapTotal"],
        "swap_free_kib": memory["SwapFree"],
        "disk_available_bytes": disk_free,
        "expected": expected,
    }
    conflicts = user_job_conflicts(run_dir)
    checks = {
        "linux": sys.platform.startswith("linux"),
        "vendor": facts["vendor"] == "Amazon EC2",
        "host": facts["host"] == expected["host"],
        "product": facts["product"] == expected["product"],
        "instance": facts["instance_id"] == expected["instance"],
        "cpu_count": facts["nproc"] == 64,
        "job_tag": args.job_tag == run_dir.name
                   and os.environ.get("AWS_RUN_TAG") == args.job_tag,
        "memory": memory["MemAvailable"] >= MIN_AVAILABLE_KIB,
        "zero_swap": memory["SwapTotal"] == 0 and memory["SwapFree"] == 0,
        "disk": disk_free >= MIN_DISK_BYTES,
        "idle": not conflicts,
    }
    facts["conflicts"] = conflicts
    facts["checks"] = checks
    facts["pass"] = all(checks.values())
    args.output.write_text(json.dumps(facts, indent=2, sort_keys=True) + "\n")
    print(json.dumps(facts, sort_keys=True))
    if not facts["pass"]:
        raise SystemExit(40)


if __name__ == "__main__":
    main()
