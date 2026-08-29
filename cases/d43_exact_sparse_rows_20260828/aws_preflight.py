#!/usr/bin/env python3
"""Fail-closed EC2, registration, source, resource, and conflict preflight."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys
import time
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(8 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def atomic_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp.%d" % os.getpid())
    with temporary.open("w") as stream:
        json.dump(value, stream, indent=1, sort_keys=True)
        stream.write("\n")
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)


def read_text(path: str) -> str:
    return Path(path).read_text().strip()


def meminfo():
    result = {}
    for line in Path("/proc/meminfo").read_text().splitlines():
        key, value = line.split(":", 1)
        result[key] = int(value.split()[0])
    return result


def proc_parent(pid: int) -> int:
    text = Path("/proc/%d/stat" % pid).read_text()
    fields = text[text.rfind(")") + 2:].split()
    return int(fields[1])


def ancestors():
    result = {os.getpid()}
    pid = os.getpid()
    while pid > 1:
        try:
            pid = proc_parent(pid)
        except (FileNotFoundError, PermissionError, ProcessLookupError,
                ValueError):
            break
        result.add(pid)
    return result


def conflicts(run_dir: Path):
    own = ancestors()
    result = []
    tokens = ("build_tails43", "gm_jet2", "singular", "msolve", "magma")
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
            command = (entry / "cmdline").read_bytes().replace(
                b"\0", b" ").decode(errors="replace")
            rss_kib = int(status.get("VmRSS", "0 kB").split()[0])
        except (FileNotFoundError, KeyError, PermissionError,
                ProcessLookupError, ValueError):
            continue
        if str(run_dir) in command:
            continue
        lowered = command.lower()
        if rss_kib >= 1024 * 1024 or any(token in lowered for token in tokens):
            result.append({
                "pid": int(entry.name), "rss_kib": rss_kib,
                "command": command,
            })
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    manifest_path = args.manifest.resolve()
    manifest = json.loads(manifest_path.read_text())
    assert manifest["schema"] == \
        "jc2.d43.exact-selected-source-manifest.v1"
    aws = manifest["aws"]
    resources = manifest["resource_contract"]
    run_dir = args.run_dir.resolve()
    registration_path = run_dir / "records" / "REGISTERED.json"
    registration = json.loads(registration_path.read_text()) \
        if registration_path.is_file() else None
    memory = meminfo() if sys.platform.startswith("linux") else {}
    active = conflicts(run_dir) if sys.platform.startswith("linux") else []
    source_hashes = {}
    source_failures = []
    for relative, expected in sorted(manifest["source_sha256"].items()):
        path = ROOT / relative
        actual = sha256_path(path) if path.is_file() else None
        source_hashes[relative] = actual
        if actual != expected:
            source_failures.append(relative)

    facts = {
        "utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "manifest": str(manifest_path),
        "manifest_sha256": sha256_path(manifest_path),
        "run_dir": str(run_dir),
        "registration": registration,
        "registration_path": str(registration_path),
        "platform": sys.platform,
        "hostname": os.uname().nodename,
        "vendor": read_text("/sys/devices/virtual/dmi/id/sys_vendor")
                  if sys.platform.startswith("linux") else None,
        "product": read_text("/sys/devices/virtual/dmi/id/product_name")
                   if sys.platform.startswith("linux") else None,
        "instance_id": read_text("/sys/devices/virtual/dmi/id/board_asset_tag")
                       if sys.platform.startswith("linux") else None,
        "nproc": os.cpu_count(),
        "run_tag_env": os.environ.get("AWS_RUN_TAG"),
        "hostname_env": os.environ.get("AWS_EXPECTED_HOSTNAME"),
        "mem_available_kib": memory.get("MemAvailable"),
        "swap_total_kib": memory.get("SwapTotal"),
        "swap_free_kib": memory.get("SwapFree"),
        "disk_free_bytes": shutil.disk_usage(run_dir).free,
        "source_sha256": source_hashes,
        "source_failures": source_failures,
        "conflicts": active,
    }
    checks = {
        "linux": sys.platform.startswith("linux"),
        "vendor": facts["vendor"] == aws["expected_vendor"],
        "product": facts["product"] == aws["expected_product"],
        "hostname_registered_nonempty": bool(aws["expected_hostname"]),
        "hostname": facts["hostname"] == aws["expected_hostname"]
                    == facts["hostname_env"],
        "instance": facts["instance_id"] == aws["expected_instance_id"],
        "nproc": facts["nproc"] == aws["expected_nproc"],
        "tag_registered_nonempty": bool(aws["required_run_tag"]),
        "tag": facts["run_tag_env"] == aws["required_run_tag"]
               == run_dir.name,
        "registration": registration is not None and registration == {
            "expected_hostname": aws["expected_hostname"],
            "manifest_sha256": sha256_path(manifest_path),
            "run_tag": aws["required_run_tag"],
        },
        "source_hashes": not source_failures,
        "memory": facts["mem_available_kib"] is not None and
                  facts["mem_available_kib"] >=
                  resources["minimum_memory_available_kib"],
        "zero_swap": facts["swap_total_kib"] == 0 and
                     facts["swap_free_kib"] == 0,
        "disk": facts["disk_free_bytes"] >=
                resources["minimum_disk_free_bytes"],
        "resource_caps_positive": all(resources[key] > 0 for key in (
            "address_space_bytes", "file_size_bytes", "timeout_seconds",
            "kill_after_seconds")),
        "idle": not active,
        "pilot_only": manifest["authorization"] == {
            "build_sparse_checkpoints": True,
            "fanout_after_pilot": False,
            "pilot_band20": True,
        },
    }
    facts["checks"] = checks
    facts["pass"] = all(checks.values())
    atomic_json(args.output, facts)
    print(json.dumps(facts, sort_keys=True))
    if not facts["pass"]:
        raise SystemExit(40)


if __name__ == "__main__":
    main()
