#!/usr/bin/env python3
"""Fail-closed live EC2, lease, and immutable-source preflight for D43 v3.

Revision 3 removes every production ``assert`` (all checks are explicit and
survive ``python -O``, which is additionally refused outright), binds the
exclusive run lease and its nonce into the receipt, extends the same-UID
conflict census with the v3 wrapper/launcher/contract tokens, distinguishes
this job's own JOB_TAG processes from foreign ones, and enforces the
1 TiB physical-memory ceiling.
"""

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

if sys.flags.optimize:
    raise RuntimeError(
        "OPTIMIZED_PYTHON_REFUSED_FAIL_CLOSED: jc2 d43 v3 preflight "
        "must run without -O/-OO/PYTHONOPTIMIZE")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SCHEMA = "jc2.d43.a00pp-exact-source-rows.v3.aws-preflight"
LEASE_SCHEMA = "jc2.d43.a00pp-exact-source-rows.v3.run-lease"


class PreflightError(RuntimeError):
    pass


def require(condition, message: str) -> None:
    if not condition:
        raise PreflightError(message)


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


def proc_job_tag(entry: Path):
    try:
        environ = (entry / "environ").read_bytes().split(b"\0")
    except (FileNotFoundError, PermissionError, ProcessLookupError, OSError):
        return None
    for item in environ:
        if item.startswith(b"JOB_TAG="):
            return item[len(b"JOB_TAG="):].decode(errors="replace")
    return None


def conflicts(own_job_tag: str):
    """Every other same-UID heavy or job-shaped process outside this job.

    Processes carrying this run's own JOB_TAG are members of the exclusive
    leased job and are exempt; a process with a *different* JOB_TAG is always
    a conflict.  The token census is defense in depth behind the kernel
    lease, not the primary exclusion mechanism.
    """
    own = ancestors()
    result = []
    tokens = ("build_tails43", "gm_jet2", "selected_rows_v2",
              "selected_rows_v3", "aws_preflight_v", "job_contract_v3",
              "run_conditional_pipeline_aws", "aws_launch_v3",
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
        tag = proc_job_tag(entry)
        if tag is not None and tag == own_job_tag:
            continue
        lowered = command.lower()
        foreign_tag = tag is not None and tag != own_job_tag
        if (foreign_tag or rss_kib >= 1024 * 1024 or
                any(token in lowered for token in tokens)):
            result.append({"pid": int(entry.name), "rss_kib": rss_kib,
                           "job_tag": tag, "command": command})
    return result


def imds_request(path: str, token=None) -> str:
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


def probe_lock_held(lock_path: Path) -> bool:
    import fcntl
    descriptor = os.open(lock_path, os.O_RDWR | os.O_CREAT, 0o600)
    try:
        try:
            fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            return True
        fcntl.flock(descriptor, fcntl.LOCK_UN)
        return False
    finally:
        os.close(descriptor)


def load_lease(path: Path, run_dir: Path):
    lease = json.loads(path.read_text())
    require(isinstance(lease, dict), "lease is not an object")
    require(lease.get("schema") == LEASE_SCHEMA, "lease schema mismatch")
    nonce = lease.get("run_nonce")
    require(isinstance(nonce, str) and len(nonce) == 64 and
            all(ch in "0123456789abcdef" for ch in nonce),
            "lease nonce malformed")
    require(lease.get("job_root") == str(run_dir.resolve()),
            "lease job_root mismatch")
    require(lease.get("job_tag") == run_dir.name, "lease job_tag mismatch")
    require(lease.get("terminal_authority") is False,
            "lease claims terminal authority")
    return lease


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--lease", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    manifest_path = args.manifest.resolve()
    manifest = json.loads(manifest_path.read_text())
    require(manifest["schema"] == "jc2.d43.a00pp-exact-source-manifest.v3",
            "manifest schema mismatch")
    manifest_hash = sha256_path(manifest_path)
    aws = manifest["aws"]
    resources = manifest["resource_contract"]
    run_dir = args.run_dir.resolve()
    linux = sys.platform.startswith("linux")

    lease = None
    lease_hash = None
    lease_error = None
    lock_held = False
    try:
        lease = load_lease(args.lease, run_dir)
        lease_hash = sha256_path(args.lease)
        lock_path = Path(lease["lock_path"])
        lock_stat = os.stat(lock_path)
        require([lock_stat.st_dev, lock_stat.st_ino] ==
                list(lease["lock_dev_ino"]), "lease lock identity drift")
        lock_held = probe_lock_held(lock_path)
    except (OSError, ValueError, KeyError, PreflightError,
            json.JSONDecodeError) as error:
        lease_error = "%s: %s" % (type(error).__name__, error)

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
    memory = meminfo() if linux else {}
    own_tag = os.environ.get("JOB_TAG", "")
    active = conflicts(own_tag) if linux else []
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
        "source_archive_sha256":
            lease["source_archive_sha256"] if lease else None,
        "launcher_sha256":
            lease["launcher"]["sha256"] if lease else None,
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
        "environment_job_tag": own_tag == run_dir.name,
        "environment_hostname": os.environ.get("AWS_EXPECTED_HOSTNAME") ==
            aws["expected_hostname"],
        "environment_run_nonce": lease is not None and
            os.environ.get("RUN_NONCE") == lease["run_nonce"],
        "registration": registration == expected_registration,
        "lease_valid": lease is not None,
        "lease_lock_held": lock_held,
        "nproc": os.cpu_count() == aws["expected_nproc"],
        "source_list_hash": source_list_hash ==
            manifest["operational_source_list_sha256"],
        "source_path_set": set(source_inventory) ==
            set(manifest["required_operational_paths"]),
        "source_hashes": not source_failures,
        "memory": memory.get("MemAvailable", 0) >=
            resources["minimum_memory_available_kib"],
        "memory_total_within_cap": 0 < memory.get("MemTotal", 0) <=
            resources["maximum_memory_total_kib"],
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
        "run_lease": {
            "path": str(args.lease.resolve()),
            "nonce": lease["run_nonce"] if lease else None,
            "lease_sha256": lease_hash,
            "lock_path": lease["lock_path"] if lease else None,
            "lock_held_probe": lock_held,
            "source_archive_sha256":
                lease["source_archive_sha256"] if lease else None,
            "launcher_sha256":
                lease["launcher"]["sha256"] if lease else None,
            "error": lease_error,
        },
        "registration": registration,
        "registration_sha256": sha256_path(registration_path)
            if registration_path.is_file() else None,
        "containment_mode": os.environ.get("CONTAINMENT_MODE"),
        "live_identity": live_identity,
        "live_tag": {"key": aws["required_tag_key"],
                     "value": live_tag_value},
        "imds_error": imds_error,
        "mem_total_kib": memory.get("MemTotal"),
        "mem_available_kib": memory.get("MemAvailable"),
        "swap_total_kib": memory.get("SwapTotal"),
        "swap_free_kib": memory.get("SwapFree"),
        "disk_free_bytes": shutil.disk_usage(run_dir).free,
        "source_sha256": source_hashes,
        "source_failures": source_failures,
        "conflicts": active,
        "checks": checks,
        "pass": all(checks.values()),
        "terminal_authority": False,
    }
    atomic_json(args.output, facts)
    print(json.dumps(facts, sort_keys=True))
    if not facts["pass"]:
        raise SystemExit(40)


if __name__ == "__main__":
    main()
