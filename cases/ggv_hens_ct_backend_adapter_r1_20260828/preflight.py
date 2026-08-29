#!/usr/bin/env python3
"""Fail-closed AWS/resource/ownership preflight; standard library only."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
from pathlib import Path


MIN_AVAILABLE_KIB = 450 * 1024 * 1024
MIN_DISK_BYTES = 20 * 1024**3
MAX_OTHER_RSS_KIB = 2 * 1024 * 1024


def meminfo():
    values = {}
    for line in Path("/proc/meminfo").read_text().splitlines():
        key, rest = line.split(":", 1)
        values[key] = int(rest.split()[0])
    return values


def proc_record(entry):
    status = {}
    for line in (entry / "status").read_text().splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            status[key] = value.strip()
    command = (entry / "cmdline").read_bytes().replace(b"\0", b" ").decode(errors="replace")
    return {
        "pid": int(entry.name),
        "name": status.get("Name", ""),
        "rss_kib": int(status.get("VmRSS", "0 kB").split()[0]),
        "command": command,
    }


def competing_processes(run_dir):
    matches = []
    own_ancestors = {os.getpid()}
    current = os.getpid()
    while current > 1:
        try:
            text = Path(f"/proc/{current}/stat").read_text()
            suffix = text[text.rfind(")") + 2 :].split()
            current = int(suffix[1])
            own_ancestors.add(current)
        except (FileNotFoundError, PermissionError, ValueError):
            break
    heavy_names = {"msolve", "Singular", "sage", "Magma", "maple", "Mathematica"}
    for entry in Path("/proc").iterdir():
        if not entry.name.isdigit() or int(entry.name) in own_ancestors:
            continue
        try:
            record = proc_record(entry)
        except (FileNotFoundError, PermissionError, ProcessLookupError, ValueError):
            continue
        lowered = record["command"].lower()
        campaign_python = ("python" in record["name"].lower() and ("/cases/" in lowered or "/jobs/" in lowered))
        build_process = record["name"] in {"pip", "gcc", "g++", "cc1", "cc1plus", "ld"}
        named_heavy = record["name"] in heavy_names
        if record["rss_kib"] >= MAX_OTHER_RSS_KIB or campaign_python or build_process or named_heavy:
            if str(run_dir) not in record["command"]:
                matches.append(record)
    return matches


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--expected-instance-id", required=True)
    parser.add_argument("--expected-instance-type", required=True)
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--job-tag", required=True)
    parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()
    run_dir = arguments.run_dir.resolve()
    assert sys.platform.startswith("linux") and Path("/proc").is_dir()
    assert Path("/sys/class/dmi/id/sys_vendor").read_text().strip() == "Amazon EC2"
    assert Path("/sys/class/dmi/id/product_name").read_text().strip() == arguments.expected_instance_type
    assert Path("/sys/class/dmi/id/board_asset_tag").read_text().strip() == arguments.expected_instance_id
    assert arguments.job_tag == run_dir.name
    assert os.environ.get("AWS_RUN_TAG") == arguments.job_tag
    assert arguments.job_tag.startswith("ggv_hens_ct_backend_r1_")
    memory = meminfo()
    assert memory["MemAvailable"] >= MIN_AVAILABLE_KIB, memory
    assert memory["SwapTotal"] == 0 and memory["SwapFree"] == 0, memory
    disk_free = shutil.disk_usage(run_dir).free
    assert disk_free >= MIN_DISK_BYTES, disk_free
    required = ["/usr/bin/setsid", "/usr/bin/prlimit", "/usr/bin/timeout", "/usr/bin/time", "/usr/bin/git"]
    assert all(Path(item).is_file() for item in required), required
    competitors = competing_processes(run_dir)
    assert not competitors, competitors
    result = {
        "status": "AWS_PREFLIGHT_PASS",
        "instance_id": arguments.expected_instance_id,
        "instance_type": arguments.expected_instance_type,
        "job_tag": arguments.job_tag,
        "run_dir": str(run_dir),
        "mem_available_kib": memory["MemAvailable"],
        "swap_total_kib": memory["SwapTotal"],
        "swap_free_kib": memory["SwapFree"],
        "disk_available_bytes": disk_free,
        "competing_processes": [],
    }
    arguments.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
