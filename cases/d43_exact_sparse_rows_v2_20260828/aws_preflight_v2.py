#!/usr/bin/env python3
"""Fail-closed live EC2 and immutable-source preflight for D43 v2."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SCHEMA = "jc2.d43.a00pp-exact-source-rows.v2.aws-preflight"


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


def parse_source_list(path: Path):
    result = {}
    for line in path.read_text().splitlines():
        if not line.strip():
            continue
        digest, relative = line.split(None, 1)
        relative = relative.strip()
        if len(digest) != 64 or relative in result:
            raise ValueError("malformed operational source list")
        result[relative] = digest
    return result


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


def conflicts():
    """Return every other same-UID heavy algebra process, including clones."""
    own = ancestors()
    result = []
    tokens = ("build_tails43", "gm_jet2", "selected_rows_v2",
              "singular", "msolve", "magma")
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
        lowered = command.lower()
        if rss_kib >= 1024 * 1024 or any(token in lowered for token in tokens):
            result.append({"pid": int(entry.name), "rss_kib": rss_kib,
                           "command": command})
    return result


def imds_request(path: str, token: str | None = None) -> str:
    url = "http://169.254.169.254/latest/" + path.lstrip("/")
    headers = {}
    if token:
        headers["X-aws-ec2-metadata-token"] = token
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=2) as response:
        return response.read().decode().strip()


def live_ec2_identity(tag_key: str):
    token_request = urllib.request.Request(
        "http://169.254.169.254/latest/api/token",
        data=b"", method="PUT",
        headers={"X-aws-ec2-metadata-token-ttl-seconds": "300"})
    with urllib.request.urlopen(token_request, timeout=2) as response:
        token = response.read().decode().strip()
    document = json.loads(imds_request(
        "dynamic/instance-identity/document", token))
    tag_value = imds_request(
        "meta-data/tags/instance/" + urllib.parse.quote(tag_key, safe=""),
        token)
    identity = {
        "account_id": str(document["accountId"]),
        "hostname": os.uname().nodename,
        "instance_id": document["instanceId"],
        "instance_type": document["instanceType"],
        "region": document["region"],
    }
    return identity, tag_value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    manifest_path = args.manifest.resolve()
    manifest = json.loads(manifest_path.read_text())
    assert manifest["schema"] == \
        "jc2.d43.a00pp-exact-source-manifest.v2"
    manifest_hash = sha256_path(manifest_path)
    aws = manifest["aws"]
    resources = manifest["resource_contract"]
    run_dir = args.run_dir.resolve()
    source_list_path = ROOT / manifest["operational_source_list"]
    try:
        source_list_hash = sha256_path(source_list_path)
        source_inventory = parse_source_list(source_list_path)
    except (FileNotFoundError, ValueError):
        source_list_hash = None
        source_inventory = {}
    source_hashes = {}
    source_failures = []
    for relative, expected in sorted(source_inventory.items()):
        path = ROOT / relative
        actual = sha256_path(path) if path.is_file() else None
        source_hashes[relative] = actual
        if actual != expected:
            source_failures.append(relative)
    registration_path = run_dir / "records" / "REGISTERED.json"
    registration = json.loads(registration_path.read_text()) \
        if registration_path.is_file() else None
    linux = sys.platform.startswith("linux")
    memory = meminfo() if linux else {}
    active = conflicts() if linux else []
    try:
        live_identity, live_tag_value = live_ec2_identity(
            aws["required_tag_key"]) if linux else (None, None)
        imds_error = None
    except Exception as error:
        live_identity, live_tag_value = None, None
        imds_error = "%s: %s" % (type(error).__name__, error)
    expected_identity = {
        key: aws["expected_" + key]
        for key in ("account_id", "hostname", "instance_id",
                    "instance_type", "region")
    }
    expected_registration = {
        "expected_identity": expected_identity,
        "manifest_sha256": manifest_hash,
        "operational_source_list_sha256":
            manifest["operational_source_list_sha256"],
        "run_tag": aws["required_tag_value"],
        "tag_key": aws["required_tag_key"],
    }
    checks = {
        "linux": linux,
        "registration_status": aws["registration_status"] ==
            "REGISTERED_IMMUTABLE",
        "registered_identity_nonempty": all(expected_identity.values()),
        "tag_registered_nonempty": bool(aws["required_tag_key"] and
                                         aws["required_tag_value"]),
        "live_identity": live_identity == expected_identity,
        "live_instance_tag": live_tag_value == aws["required_tag_value"],
        "environment_tag": os.environ.get("AWS_RUN_TAG") ==
            aws["required_tag_value"] == run_dir.name,
        "environment_hostname": os.environ.get("AWS_EXPECTED_HOSTNAME") ==
            aws["expected_hostname"],
        "registration": registration == expected_registration,
        "nproc": os.cpu_count() == aws["expected_nproc"],
        "source_list_hash": source_list_hash ==
            manifest["operational_source_list_sha256"],
        "source_path_set": set(source_inventory) ==
            set(manifest["required_operational_paths"]),
        "source_hashes": not source_failures,
        "memory": memory.get("MemAvailable", 0) >=
            resources["minimum_memory_available_kib"],
        "zero_swap": memory.get("SwapTotal") == 0 and
            memory.get("SwapFree") == 0,
        "disk": shutil.disk_usage(run_dir).free >=
            resources["minimum_disk_free_bytes"],
        "idle": not active,
        "conditional_pipeline_only": manifest["authorization"] == {
            "build_independent_sides": True,
            "conditional_band20_then_all184": True,
            "solve": False,
        },
    }
    facts = {
        "schema": SCHEMA,
        "utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "manifest": str(manifest_path),
        "manifest_sha256": manifest_hash,
        "operational_source_list_sha256": source_list_hash,
        "run_dir": str(run_dir),
        "registration": registration,
        "live_identity": live_identity,
        "live_tag": {"key": aws["required_tag_key"],
                     "value": live_tag_value},
        "imds_error": imds_error,
        "mem_available_kib": memory.get("MemAvailable"),
        "swap_total_kib": memory.get("SwapTotal"),
        "swap_free_kib": memory.get("SwapFree"),
        "disk_free_bytes": shutil.disk_usage(run_dir).free,
        "source_sha256": source_hashes,
        "source_failures": source_failures,
        "conflicts": active,
        "checks": checks,
        "pass": all(checks.values()),
    }
    atomic_json(args.output, facts)
    print(json.dumps(facts, sort_keys=True))
    if not facts["pass"]:
        raise SystemExit(40)


if __name__ == "__main__":
    main()
