#!/usr/bin/env python3
"""Fail-closed host, resource, tag, idle, backend, and swap preflight."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys
import time
from pathlib import Path


def lane(host, instance, component, suffix):
    return {
        "host": host,
        "instance": instance,
        "product": "r6i.4xlarge",
        "nproc": 16,
        "min_mem_gib": 110,
        "component": component,
        "tag": f"ggv_lambda0_quotient_nf_{component}_r4_20260828T155000Z_{suffix}",
    }


LANES = {
    "p": lane("ip-172-30-0-150", "i-040b7a1c2ed72d4cc", "p", "r6c"),
    "c8p02": lane("ip-172-30-0-131", "i-0793fef088620f2c1", "c8p02", "r6e"),
    "q1p02": lane("ip-172-30-0-79", "i-0fdde459d4ab36b95", "q1p02", "r6f"),
    "q1p03": lane("ip-172-30-0-248", "i-0c73ac7019fe3eef2", "q1p03", "r6g"),
    "triple02": lane("ip-172-30-0-220", "i-0d71d73e0fe8a8cae", "triple02", "r6h"),
    "triple03": lane("ip-172-30-0-128", "i-072ccec67b0933088", "triple03", "r6i"),
}
SINGULAR_SHA256 = "90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4"


def proc_stat(pid: int) -> dict[str, int]:
    raw = Path(f"/proc/{pid}/stat").read_text()
    fields = raw[raw.rfind(")") + 2 :].split()
    return {"ppid": int(fields[1]), "pgrp": int(fields[2]), "session": int(fields[3]), "starttime": int(fields[19])}


def ancestors() -> set[int]:
    result = {os.getpid()}
    pid = os.getpid()
    while pid > 1:
        try:
            pid = proc_stat(pid)["ppid"]
        except (FileNotFoundError, PermissionError, ProcessLookupError):
            break
        result.add(pid)
    return result


def meminfo() -> dict[str, int]:
    result = {}
    for line in Path("/proc/meminfo").read_text().splitlines():
        key, value = line.split(":", 1)
        result[key] = int(value.split()[0])
    return result


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def conflicts(run_dir: Path) -> list[dict[str, object]]:
    own = ancestors()
    tokens = ("python", "sage", "singular", "msolve", "magma", "/home/ubuntu/jobs/", "timeout", "prlimit")
    result = []
    for entry in Path("/proc").iterdir():
        if not entry.name.isdigit() or int(entry.name) in own:
            continue
        try:
            status = {
                line.split(":", 1)[0]: line.split(":", 1)[1].strip()
                for line in (entry / "status").read_text().splitlines()
                if ":" in line
            }
            if int(status["Uid"].split()[0]) != os.getuid():
                continue
            command = (entry / "cmdline").read_bytes().replace(b"\0", b" ").decode(errors="replace")
            rss_kib = int(status.get("VmRSS", "0 kB").split()[0])
        except (FileNotFoundError, PermissionError, ProcessLookupError, KeyError, ValueError):
            continue
        if str(run_dir) in command:
            continue
        if rss_kib >= 1024 * 1024 or any(token in command.lower() for token in tokens):
            result.append({"pid": int(entry.name), "rss_kib": rss_kib, "command": command})
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--job-tag", required=True)
    parser.add_argument("--component", choices=sorted(LANES), required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    run_dir = args.run_dir.resolve()
    expected = LANES[args.component]
    memory = meminfo()
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
        "component": args.component,
        "run_dir": str(run_dir),
        "mem_available_kib": memory["MemAvailable"],
        "swap_total_kib": memory["SwapTotal"],
        "swap_free_kib": memory["SwapFree"],
        "disk_available_bytes": shutil.disk_usage(run_dir).free,
        "singular": str(singular),
        "singular_sha256": sha256(singular) if singular.is_file() else None,
        "conflicts": active,
    }
    checks = {
        "linux": sys.platform.startswith("linux"),
        "vendor": facts["vendor"] == "Amazon EC2",
        "product": facts["product"] == expected["product"],
        "host": facts["host"] == expected["host"],
        "instance": facts["instance"] == expected["instance"],
        "nproc": facts["nproc"] == expected["nproc"],
        "job_tag": (
            args.job_tag == expected["tag"] == run_dir.name
            and os.environ.get("AWS_RUN_TAG") == expected["tag"]
            and os.environ.get("AWS_RUN_COMPONENT") == args.component
        ),
        "memory": memory["MemAvailable"] >= expected["min_mem_gib"] * 1024 * 1024,
        "zero_swap": memory["SwapTotal"] == 0 and memory["SwapFree"] == 0,
        "disk": facts["disk_available_bytes"] >= 50 * 1024**3,
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

