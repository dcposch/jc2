#!/usr/bin/env python3
"""Fail-closed EC2 preflight for the left-kernel/cofactor job."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
import time


EXPECTED_HOST = "ip-172-30-0-45"
EXPECTED_INSTANCE = "i-07eeaf8ba6f0bc419"
EXPECTED_PRODUCT = "r6i.8xlarge"
EXPECTED_NPROC = 32
EXPECTED_TAG = "ggv_lambda0_left_kernel_cofactor_r4_20260828T125900Z_r6d"
SINGULAR_SHA256 = "90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4"


def proc_stat(pid: int) -> dict[str, int]:
    text = Path(f"/proc/{pid}/stat").read_text()
    suffix = text[text.rfind(")") + 2 :].split()
    return {"ppid": int(suffix[1]), "pgrp": int(suffix[2]),
            "session": int(suffix[3]), "starttime": int(suffix[19])}


def ancestors() -> set[int]:
    found = {os.getpid()}
    current = os.getpid()
    while current > 1:
        try:
            current = proc_stat(current)["ppid"]
        except (FileNotFoundError, PermissionError, ProcessLookupError):
            break
        found.add(current)
    return found


def memory() -> dict[str, int]:
    values = {}
    for line in Path("/proc/meminfo").read_text().splitlines():
        key, rest = line.split(":", 1)
        values[key] = int(rest.split()[0])
    return values


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def conflicts(run_dir: Path) -> list[dict[str, object]]:
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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--job-tag", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    run_dir = args.run_dir.resolve()
    mem = memory()
    disk = shutil.disk_usage(run_dir).free
    singular = Path(shutil.which("Singular") or "")
    active = conflicts(run_dir)
    facts = {
        "utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "platform": sys.platform,
        "host": os.uname().nodename,
        "vendor": Path("/sys/class/dmi/id/sys_vendor").read_text().strip(),
        "product": Path("/sys/class/dmi/id/product_name").read_text().strip(),
        "instance": Path("/sys/class/dmi/id/board_asset_tag").read_text().strip(),
        "nproc": os.cpu_count(),
        "job_tag": args.job_tag,
        "run_dir": str(run_dir),
        "mem_available_kib": mem["MemAvailable"],
        "swap_total_kib": mem["SwapTotal"],
        "swap_free_kib": mem["SwapFree"],
        "disk_available_bytes": disk,
        "singular": str(singular),
        "singular_sha256": sha256(singular) if singular.is_file() else None,
        "conflicts": active,
    }
    checks = {
        "linux": sys.platform.startswith("linux"),
        "vendor": facts["vendor"] == "Amazon EC2",
        "product": facts["product"] == EXPECTED_PRODUCT,
        "host": facts["host"] == EXPECTED_HOST,
        "instance": facts["instance"] == EXPECTED_INSTANCE,
        "nproc": facts["nproc"] == EXPECTED_NPROC,
        "job_tag": (args.job_tag == EXPECTED_TAG == run_dir.name
                    and os.environ.get("AWS_RUN_TAG") == EXPECTED_TAG),
        "memory": mem["MemAvailable"] >= 225 * 1024 * 1024,
        "zero_swap": mem["SwapTotal"] == 0 and mem["SwapFree"] == 0,
        "disk": disk >= 50 * 1024**3,
        "singular": facts["singular_sha256"] == SINGULAR_SHA256,
        "idle": not active,
    }
    facts["checks"] = checks
    facts["pass"] = all(checks.values())
    args.output.write_text(json.dumps(facts, indent=2, sort_keys=True) + "\n")
    print(json.dumps(facts, sort_keys=True))
    if not facts["pass"]:
        raise SystemExit(40)


if __name__ == "__main__":
    main()
