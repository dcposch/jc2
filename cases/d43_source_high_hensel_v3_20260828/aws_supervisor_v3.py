#!/usr/bin/python3
"""Externally authorized, cgroup-v2 AWS custodian for D43 Hensel v3.

Launch authority is the SHA-256 stored in a live EC2 instance tag.  That hash
addresses a coordinator authorization record which binds the reviewed source,
runtime, host, target, job, and (for N64) the exact N16 handoff.  Caller-supplied
"expected" hashes never authorize work.

The registered systemd unit must place this supervisor and every descendant in
    one nondelegated cgroup with hard memory/swap/tasks/runtime limits and an exact
ExecStopPost call back into ``--terminalize`` mode.  Normal and fault paths
publish one authoritative terminal object only after manifest/archive replay.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import importlib.metadata
import io
import json
import os
import platform
import re
import resource
import shutil
import signal
import socket
import stat
import subprocess
import sys
import sysconfig
import tarfile
import threading
import time
import urllib.parse
import urllib.request
from pathlib import Path


PACKET_DIR = Path(__file__).resolve().parent
CASES_DIR = PACKET_DIR.parent
ROOT = CASES_DIR.parent
ROUTE = "D43-PRISTINE-SOURCE-HIGH-HENSEL-R3"
STATE_SCHEMA = "d43-pristine-source-high-hensel-state-v3"
AUTH_SCHEMA = "d43-pristine-source-high-hensel-launch-auth-v3"
MARKER_SCHEMA = "d43-pristine-source-high-hensel-aws-auth-v3"
TERMINAL_SCHEMA = "d43-pristine-source-high-hensel-aws-terminal-v3"
PREREG_SCHEMA = "d43-pristine-source-high-hensel-prereg-v3"
TARGET_TAGS = {16: ROUTE + "-N16", 64: ROUTE + "-N64"}
AUTHORIZATION_TAG_KEY = "jc2-d43-high-hensel-authorization-sha256"
EXPECTED_INSTANCE_TYPE = "c7i.xlarge"
EXPECTED_NUMPY_VERSION = "2.1.3"
DEDICATED_SERVICE_USER = "jc2d43"
EXPECTED_D21_SHA256 = \
    "b4ba8dfcd9755fb3201780cd97c1d2ef38bd26d2d1b023521a0e62a3d6db169e"
EXPECTED_CORE23_SHA256 = \
    "0533787f6bf89ff25478f01ddad40230a11f6a19bb19af8889b692ce26a38cdf"
TIMEOUT_SECONDS = 1200
RSS_LIMIT_BYTES = 2 * 1024 ** 3
TASKS_LIMIT = 32
SAMPLE_INTERVAL_SECONDS = 0.1
AUTH_PATH_SENTINEL = "<ABSOLUTE_JOB_MARKER_PATH>"
AUTH_SHA_SENTINEL = "<SHA256_OF_JOB_MARKER_ENVELOPE>"
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
INVOCATION_RE = re.compile(r"^[0-9a-f]{32}$")
SAFE_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$")
INJECTION_VARIABLES = {
    "BASH_ENV", "ENV", "CDPATH", "GLOBIGNORE", "SHELLOPTS",
    "LD_PRELOAD", "LD_LIBRARY_PATH", "DYLD_INSERT_LIBRARIES",
    "DYLD_LIBRARY_PATH", "PYTHONHOME", "PYTHONPATH", "PYTHONSTARTUP",
    "PYTHONINSPECT", "PYTHONWARNINGS", "DIRECTIONB_STATE",
    "LD_AUDIT", "LD_BIND_NOW", "LD_DEBUG", "LD_DEBUG_OUTPUT",
    "LD_DYNAMIC_WEAK", "LD_HWCAP_MASK", "LD_ORIGIN_PATH", "LD_PROFILE",
    "LD_SHOW_AUXV", "LD_USE_LOAD_BIAS", "GLIBC_TUNABLES",
}
PREEXEC_UNSET_ENVIRONMENT = tuple(sorted(
    INJECTION_VARIABLES | {"USER", "LOGNAME", "SHELL"}))
SUPERVISOR_ALLOWED_ENV = {
    "HOME", "LANG", "LC_ALL", "PATH", "TZ", "INVOCATION_ID",
    "JOURNAL_STREAM", "SYSTEMD_EXEC_PID", "MEMORY_PRESSURE_WATCH",
    "MEMORY_PRESSURE_WRITE", "SERVICE_RESULT", "EXIT_CODE", "EXIT_STATUS",
    "PYTHONHASHSEED", "PYTHONNOUSERSITE", "PYTHONDONTWRITEBYTECODE",
    "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
    "NUMEXPR_NUM_THREADS", "VECLIB_MAXIMUM_THREADS",
}
SUPERVISOR_REQUIRED_ENV = {
    "HOME": "/var/empty", "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8",
    "PATH": "/usr/bin:/bin",
    "TZ": "UTC", "PYTHONHASHSEED": "0", "PYTHONNOUSERSITE": "1",
    "PYTHONDONTWRITEBYTECODE": "1", "OMP_NUM_THREADS": "1",
    "OPENBLAS_NUM_THREADS": "1", "MKL_NUM_THREADS": "1",
    "NUMEXPR_NUM_THREADS": "1", "VECLIB_MAXIMUM_THREADS": "1",
}
SCOPE = "residue-A, B=84, a00pp, finite raw 184-row Euler/J-source truncation only"
CERTIFIED_CLAIM = (
    "at every successful committed digit, one finite congruence point of "
    "the declared raw 184-row Euler/J-source truncation satisfying the "
    "necessary E=0 and W1,W2 unit gates")
FORBIDDEN_CLAIMS = [
    "assembled 218-row p-adic point",
    "parked/source presentation equivalence",
    "full residue-A/template/D25 p-adic point or upstream exact-equation lift",
    "D43 template-branch evidence or survival from the raw-source lift",
    "indefinite source solvability or formal smoothness", "Z_p point",
    "characteristic-zero point", "formal germ",
    "ambient polynomial Keller map", "JC2 counterexample",
]


class CustodyFault(RuntimeError):
    def __init__(self, code, detail):
        super().__init__(detail)
        self.code = str(code)
        self.detail = str(detail)


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_json(value) -> str:
    return sha256_bytes(json.dumps(
        value, sort_keys=True, separators=(",", ":")).encode())


def sha256_path(path) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(8 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def is_sha256(value) -> bool:
    return isinstance(value, str) and SHA_RE.fullmatch(value) is not None


def utc_now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def fsync_directory(path) -> None:
    descriptor = os.open(os.fspath(path), os.O_RDONLY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def require_root_owned_nonwritable(path: Path, label: str) -> Path:
    raw = Path(path)
    if raw.is_symlink():
        raise CustodyFault("IMMUTABLE_BOOTSTRAP", "%s is symlinked" % label)
    resolved = raw.resolve(strict=True)
    if Path(os.path.abspath(raw)) != resolved:
        raise CustodyFault("IMMUTABLE_BOOTSTRAP",
                           "%s has a noncanonical/symlinked path" % label)
    observed = resolved.stat()
    if observed.st_uid != 0 or observed.st_mode & 0o022:
        raise CustodyFault(
            "IMMUTABLE_BOOTSTRAP",
            "%s must be root-owned and group/world nonwritable" % label)
    ancestor = resolved.parent
    while True:
        if ancestor.is_symlink():
            raise CustodyFault("IMMUTABLE_BOOTSTRAP",
                               "%s has a symlinked ancestor" % label)
        ancestor_stat = ancestor.stat()
        if ancestor_stat.st_uid != 0 or ancestor_stat.st_mode & 0o022:
            raise CustodyFault(
                "IMMUTABLE_BOOTSTRAP",
                "%s has a mutable/non-root ancestor: %s" %
                (label, ancestor))
        if ancestor == ancestor.parent:
            break
        ancestor = ancestor.parent
    return resolved


def atomic_bytes(path, content: bytes, mode=0o600, *, replace=True) -> None:
    raw_path = Path(path)
    if raw_path.is_symlink():
        raise CustodyFault("ATOMIC_PATH", "symlinked destination forbidden")
    path = raw_path.parent.resolve() / raw_path.name
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.parent / (".%s.%d.tmp" % (path.name, os.getpid()))
    descriptor = os.open(
        temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL, mode)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        if replace:
            os.replace(temporary, path)
        else:
            # link(2), unlike a check followed by replace(2), is an atomic
            # create-if-absent authority promotion on the same filesystem.
            os.link(temporary, path)
            temporary.unlink()
        os.chmod(path, mode)
        fsync_directory(path.parent)
    finally:
        if temporary.exists():
            temporary.unlink()


def atomic_json(path, value, mode=0o600, *, replace=True) -> None:
    atomic_bytes(path, (json.dumps(value, indent=1, sort_keys=True) +
                        "\n").encode(), mode, replace=replace)


def write_envelope(path, payload) -> str:
    digest = sha256_json(payload)
    atomic_json(path, {"payload": payload, "payload_sha256": digest})
    return digest


def load_envelope(path) -> dict:
    value = json.loads(Path(path).read_text())
    if set(value) != {"payload", "payload_sha256"} or \
            sha256_json(value["payload"]) != value["payload_sha256"]:
        raise CustodyFault("ENVELOPE", "authenticated envelope drift")
    return value["payload"]


def _imds_get(path, token, timeout=2.0):
    request = urllib.request.Request(
        "http://169.254.169.254/latest/" + path.lstrip("/"),
        headers={"X-aws-ec2-metadata-token": token})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read().decode().strip()


def live_ec2_identity_and_tag(tag_key=AUTHORIZATION_TAG_KEY, timeout=2.0):
    if platform.system() != "Linux":
        raise CustodyFault("HOST_OS", "Linux required")
    try:
        vendor = Path("/sys/class/dmi/id/sys_vendor").read_text().strip()
    except OSError as error:
        raise CustodyFault("HOST_DMI", "DMI vendor unavailable") from error
    if vendor != "Amazon EC2":
        raise CustodyFault("HOST_DMI", "Amazon EC2 required")
    try:
        request = urllib.request.Request(
            "http://169.254.169.254/latest/api/token", data=b"",
            method="PUT", headers={
                "X-aws-ec2-metadata-token-ttl-seconds": "60"})
        with urllib.request.urlopen(request, timeout=timeout) as response:
            token = response.read().decode().strip()
        document = json.loads(_imds_get(
            "dynamic/instance-identity/document", token, timeout))
        tag = _imds_get(
            "meta-data/tags/instance/" +
            urllib.parse.quote(tag_key, safe=""), token, timeout)
    except Exception as error:
        raise CustodyFault("HOST_IMDS", "IMDSv2 identity/tag unavailable") \
            from error
    identity = {
        "account_id": str(document["accountId"]),
        "ami_id": _imds_get("meta-data/ami-id", token, timeout),
        "availability_zone": document["availabilityZone"],
        "hostname": socket.gethostname(),
        "instance_id": document["instanceId"],
        "instance_type": document["instanceType"],
        "private_ip": document["privateIp"],
        "region": document["region"],
        "vendor": vendor,
    }
    return identity, {"key": tag_key, "value": tag}


def validate_authorization_shape(authorization: dict) -> None:
    top = {"schema", "status", "authorization_tag_key", "issued_utc",
           "review_verdict", "expected_host_identity", "bindings", "paths",
           "runtime", "systemd"}
    bindings = {
        "job_id", "target_exponent", "lane_tag",
        "payload_manifest_sha256", "preregistration_sha256",
        "runner_sha256", "base_runner_sha256", "supervisor_sha256",
        "worker_sha256", "runtime_environment_sha256",
        "runtime_receipt_sha256", "review_report_sha256",
        "source_archive_sha256", "claims_forbidden_sha256",
        "d21_private_sha256", "core23_sha256", "target16_provenance",
    }
    paths = {
        "source_root", "run_dir", "payload_manifest", "preregistration",
        "review_report_path", "supervisor_path", "worker", "state_input_path",
        "state_output_path", "target16_terminal_path",
        "target16_manifest_path", "target16_archive_path",
    }
    runtime = {
        "python_path", "python_binary_sha256", "bash_path",
        "bash_binary_sha256", "runtime_root", "environment_manifest_path",
        "environment_manifest_sha256", "numpy", "receipt_sha256",
    }
    systemd = {"unit_name", "cgroup_path", "unit_fragment_path",
               "unit_fragment_sha256", "exec_start_argv",
               "exec_stop_post_argv"}
    if not isinstance(authorization, dict) or set(authorization) != top:
        raise CustodyFault("AUTH_SHAPE", "top-level authorization shape drift")
    for key, expected in (("bindings", bindings), ("paths", paths),
                          ("runtime", runtime), ("systemd", systemd)):
        if not isinstance(authorization[key], dict) or \
                set(authorization[key]) != expected:
            raise CustodyFault("AUTH_SHAPE", "%s shape drift" % key)
    numpy = authorization["runtime"]["numpy"]
    if not isinstance(numpy, dict) or set(numpy) != {
            "version", "distribution_tree_sha256", "blas_config_sha256"}:
        raise CustodyFault("AUTH_SHAPE", "NumPy receipt shape drift")
    hash_fields = [key for key in bindings if key.endswith("_sha256")] + [
        "python_binary_sha256", "bash_binary_sha256",
        "environment_manifest_sha256", "receipt_sha256"]
    for key in hash_fields:
        source = authorization["bindings"] if key in bindings else \
            authorization["runtime"]
        if not is_sha256(source[key]):
            raise CustodyFault("AUTH_SHAPE", "malformed hash: %s" % key)
    if numpy["version"] != EXPECTED_NUMPY_VERSION or any(
            not is_sha256(numpy[key]) for key in
            ("distribution_tree_sha256", "blas_config_sha256")):
        raise CustodyFault("AUTH_SHAPE", "NumPy binding drift")


def immutable_authorization_path(path) -> Path:
    path = require_root_owned_nonwritable(Path(path), "authorization")
    path_stat = path.stat()
    if not stat.S_ISREG(path_stat.st_mode):
        raise CustodyFault(
            "LIVE_AUTH_FILE",
            "authorization must be a root-owned nonwritable regular file")
    return path


def load_live_authorization(path) -> tuple[dict, dict, dict, str]:
    identity, tag = live_ec2_identity_and_tag()
    if tag["key"] != AUTHORIZATION_TAG_KEY or not is_sha256(tag["value"]):
        raise CustodyFault("LIVE_AUTH_TAG", "live authorization tag malformed")
    path = immutable_authorization_path(path)
    observed = sha256_path(path)
    if observed != tag["value"]:
        raise CustodyFault("LIVE_AUTH_TAG",
                           "authorization bytes do not match live EC2 tag")
    authorization = json.loads(path.read_text())
    validate_authorization_shape(authorization)
    if authorization.get("schema") != AUTH_SCHEMA or \
            authorization.get("status") != \
            "COORDINATOR_AUTHORIZED_AFTER_INDEPENDENT_REVIEW_PASS":
        raise CustodyFault("AUTH_STATUS", "external authorization inactive")
    if authorization["review_verdict"] != "PASS":
        raise CustodyFault("AUTH_STATUS", "independent review is not PASS")
    if authorization.get("authorization_tag_key") != AUTHORIZATION_TAG_KEY:
        raise CustodyFault("AUTH_TAG_KEY", "authorization tag-key drift")
    if authorization.get("expected_host_identity") != identity:
        raise CustodyFault("AUTH_IDENTITY", "live EC2 identity mismatch")
    return authorization, identity, tag, observed


def revalidate_live_authorization(path, expected_sha: str,
                                  expected_identity: dict,
                                  expected_tag: dict) -> None:
    _authorization, identity, tag, observed = load_live_authorization(path)
    if observed != expected_sha or identity != expected_identity or \
            tag != expected_tag:
        raise CustodyFault("LIVE_AUTH_REVOKED",
                           "live authorization changed during the job")


def reject_inherited_environment() -> None:
    present = INJECTION_VARIABLES & set(os.environ)
    if present:
        raise CustodyFault("ENV_INJECTION",
                           "injection variables inherited: %s" %
                           sorted(present))
    unexpected = set(os.environ) - SUPERVISOR_ALLOWED_ENV
    if unexpected:
        raise CustodyFault("ENV_NOT_SANITIZED",
                           "nonallowlisted supervisor environment: %s" %
                           sorted(unexpected))
    for key, value in SUPERVISOR_REQUIRED_ENV.items():
        if os.environ.get(key) != value:
            raise CustodyFault("ENV_NOT_SANITIZED",
                               "required supervisor environment drift: %s" %
                               key)


def registered_invocation_id() -> str:
    value = os.environ.get("INVOCATION_ID", "")
    if not INVOCATION_RE.fullmatch(value):
        raise CustodyFault("SYSTEMD_INVOCATION",
                           "valid systemd INVOCATION_ID is required")
    return value


def safe_relative_path(root: Path, relative: str, *, must_exist=True) -> Path:
    candidate = Path(relative)
    if candidate.is_absolute() or ".." in candidate.parts:
        raise CustodyFault("PATH", "unsafe relative path: %r" % relative)
    unresolved = root / candidate
    if unresolved.is_symlink():
        raise CustodyFault("PATH", "symlinked input forbidden: %s" % relative)
    resolved = unresolved.resolve()
    try:
        resolved.relative_to(root.resolve())
    except ValueError as error:
        raise CustodyFault("PATH", "path escapes registered root") from error
    if must_exist and not resolved.is_file():
        raise CustodyFault("PATH", "regular input missing: %s" % relative)
    return resolved


def parse_hash_manifest(root: Path, manifest_path: Path) -> dict[str, str]:
    entries = {}
    for number, line in enumerate(manifest_path.read_text().splitlines(), 1):
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        if not match or match.group(2) in entries:
            raise CustodyFault("MANIFEST_FORMAT",
                               "malformed/duplicate line %d" % number)
        digest, relative = match.groups()
        path = safe_relative_path(root, relative)
        if sha256_path(path) != digest:
            raise CustodyFault("MANIFEST_HASH", relative)
        entries[relative] = digest
    if not entries:
        raise CustodyFault("MANIFEST_EMPTY", "payload manifest empty")
    return entries


def verify_preregistration(prereg_path: Path, entries: dict[str, str],
                           manifest_sha256: str) -> dict:
    prereg = json.loads(prereg_path.read_text())
    exact = {
        "schema": PREREG_SCHEMA,
        "status": "V3_REVIEW_FROZEN_NO_AWS_LAUNCH",
        "protocol": ROUTE,
        "state_schema": STATE_SCHEMA,
        "scope": SCOPE,
        "certified_claim": CERTIFIED_CLAIM,
        "forbidden_claims": FORBIDDEN_CLAIMS,
    }
    for key, value in exact.items():
        if prereg.get(key) != value:
            raise CustodyFault("PREREG", "%s drift" % key)
    route = prereg.get("aws_route", {})
    route_exact = {
        "timeout_seconds": TIMEOUT_SECONDS,
        "aggregate_memory_max_bytes": RSS_LIMIT_BYTES,
        "memory_swap_max_bytes": 0,
        "tasks_max": TASKS_LIMIT,
        "sample_interval_seconds": SAMPLE_INTERVAL_SECONDS,
        "instance_type": EXPECTED_INSTANCE_TYPE,
        "dedicated_service_user": DEDICATED_SERVICE_USER,
        "ambient_temp_paths_inaccessible": ["/tmp", "/var/tmp", "/dev/shm"],
        "systemd_dropins": "forbidden",
        "target_tags": {str(key): value for key, value in TARGET_TAGS.items()},
        "payload_manifest_sha256": manifest_sha256,
    }
    for key, value in route_exact.items():
        if route.get(key) != value:
            raise CustodyFault("PREREG_ROUTE", "%s drift" % key)
    if prereg.get("inputs") != entries or \
            set(route.get("payload_files", [])) != set(entries):
        raise CustodyFault("PREREG_COVERAGE", "payload coverage drift")
    if prereg.get("target64_requires_distinct_authorization") is not True:
        raise CustodyFault("PREREG_TARGET64", "continuation gate absent")
    return prereg


def copy_verified_file(source: Path, destination: Path, expected: str) -> None:
    if source.is_symlink() or destination.exists():
        raise CustodyFault("MATERIALIZE", "source symlink or destination exists")
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0)
    input_fd = os.open(source, flags)
    destination.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    output_fd = os.open(destination, os.O_WRONLY | os.O_CREAT | os.O_EXCL,
                        0o400)
    digest = hashlib.sha256()
    try:
        with os.fdopen(input_fd, "rb") as input_handle, \
                os.fdopen(output_fd, "wb") as output_handle:
            for block in iter(lambda: input_handle.read(8 << 20), b""):
                digest.update(block)
                output_handle.write(block)
            output_handle.flush()
            os.fsync(output_handle.fileno())
    except Exception:
        if destination.exists():
            destination.unlink()
        raise
    if digest.hexdigest() != expected or sha256_path(destination) != expected:
        destination.unlink()
        raise CustodyFault("MATERIALIZE", "copy hash drift: %s" % source)
    os.chmod(destination, 0o400)
    fsync_directory(destination.parent)


def snapshot_untrusted_file(source: Path, destination: Path) -> str:
    """Read an untrusted child output once into a durable immutable snapshot."""
    if source.is_symlink() or destination.exists():
        raise CustodyFault("OUTPUT_SNAPSHOT",
                           "source symlink or destination collision")
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0)
    input_fd = os.open(source, flags)
    observed = os.fstat(input_fd)
    if not stat.S_ISREG(observed.st_mode):
        os.close(input_fd)
        raise CustodyFault("OUTPUT_SNAPSHOT", "child output is not regular")
    destination.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    output_fd = os.open(destination, os.O_WRONLY | os.O_CREAT | os.O_EXCL,
                        0o400)
    digest = hashlib.sha256()
    try:
        with os.fdopen(input_fd, "rb") as input_handle, \
                os.fdopen(output_fd, "wb") as output_handle:
            for block in iter(lambda: input_handle.read(8 << 20), b""):
                digest.update(block)
                output_handle.write(block)
            output_handle.flush()
            os.fsync(output_handle.fileno())
    except Exception:
        if destination.exists():
            destination.unlink()
        raise
    result = digest.hexdigest()
    if sha256_path(destination) != result:
        destination.unlink()
        raise CustodyFault("OUTPUT_SNAPSHOT", "snapshot replay drift")
    os.chmod(destination, 0o400)
    fsync_directory(destination.parent)
    return result


def materialize_payload(source_root: Path, execution_root: Path,
                        entries: dict[str, str],
                        sealed_metadata: dict[str, str] | None = None) -> dict:
    if execution_root.exists():
        raise CustodyFault("EXECUTION_ROOT", "execution root already exists")
    execution_root.mkdir(parents=True, mode=0o700)
    complete = dict(entries)
    for relative, digest in (sealed_metadata or {}).items():
        if relative in complete:
            raise CustodyFault("EXECUTION_ROOT", "duplicate metadata path")
        complete[relative] = digest
    for relative, digest in sorted(complete.items()):
        copy_verified_file(safe_relative_path(source_root, relative),
                           execution_root / relative, digest)
    replay = {relative: sha256_path(execution_root / relative)
              for relative in complete}
    if replay != complete:
        raise CustodyFault("EXECUTION_REPLAY", "private payload replay drift")
    for directory, subdirs, _files in os.walk(execution_root, topdown=False):
        os.chmod(directory, 0o500)
        for name in subdirs:
            os.chmod(Path(directory) / name, 0o500)
    return replay


def parse_environment_manifest(runtime_root: Path, path: Path,
                               expected_sha256: str) -> dict[str, str]:
    if sha256_path(path) != expected_sha256:
        raise CustodyFault("RUNTIME_MANIFEST", "environment manifest hash drift")
    entries = parse_hash_manifest(runtime_root, path)
    return entries


def _numpy_tree_receipt() -> dict:
    try:
        import numpy
    except Exception as error:
        raise CustodyFault("NUMPY", "NumPy import failed") from error
    if numpy.__version__ != EXPECTED_NUMPY_VERSION or \
            importlib.metadata.version("numpy") != EXPECTED_NUMPY_VERSION:
        raise CustodyFault("NUMPY", "NumPy version drift")
    distribution = importlib.metadata.distribution("numpy")
    entries = {}
    for item in distribution.files or ():
        path = Path(distribution.locate_file(item))
        if path.is_file():
            if path.is_symlink():
                raise CustodyFault("NUMPY", "symlink in NumPy distribution")
            entries[str(item)] = sha256_path(path)
    try:
        config = numpy.show_config(mode="dicts")
    except TypeError as error:
        raise CustodyFault("NUMPY", "NumPy config API/build drift") from error
    return {
        "version": numpy.__version__,
        "distribution_files": len(entries),
        "distribution_tree_sha256": sha256_json(entries),
        "blas_config": config,
        "blas_config_sha256": sha256_json(config),
    }


def runtime_receipt(runtime: dict) -> dict:
    python_path = require_root_owned_nonwritable(
        Path(sys.executable), "Python executable")
    if str(python_path) != runtime.get("python_path") or \
            sha256_path(python_path) != runtime.get("python_binary_sha256"):
        raise CustodyFault("PYTHON_RUNTIME", "Python executable binding drift")
    runtime_root = require_root_owned_nonwritable(
        Path(runtime["runtime_root"]), "runtime root")
    try:
        python_path.relative_to(runtime_root)
    except ValueError as error:
        raise CustodyFault("PYTHON_RUNTIME", "Python outside runtime root") from error
    raw_manifest = Path(runtime["environment_manifest_path"])
    if raw_manifest.is_symlink():
        raise CustodyFault("RUNTIME_MANIFEST", "symlinked manifest forbidden")
    manifest_path = raw_manifest.resolve(strict=True)
    try:
        manifest_relative = str(manifest_path.relative_to(runtime_root))
    except ValueError as error:
        raise CustodyFault("RUNTIME_MANIFEST", "manifest outside runtime") \
            from error
    entries = parse_environment_manifest(
        runtime_root, manifest_path, runtime["environment_manifest_sha256"])
    observed_files = set()
    for path in runtime_root.rglob("*"):
        if path.is_symlink():
            raise CustodyFault("RUNTIME_MANIFEST", "runtime symlink forbidden")
        require_root_owned_nonwritable(path, "runtime tree member")
        if path.is_file() and path != manifest_path:
            observed_files.add(str(path.relative_to(runtime_root)))
    if observed_files != set(entries):
        raise CustodyFault("RUNTIME_MANIFEST",
                           "environment manifest is not a complete census")
    relative_python = str(python_path.relative_to(runtime_root))
    if entries.get(relative_python) != runtime["python_binary_sha256"]:
        raise CustodyFault("PYTHON_RUNTIME", "Python absent from env manifest")
    numpy_receipt = _numpy_tree_receipt()
    for key in ("version", "distribution_tree_sha256", "blas_config_sha256"):
        if numpy_receipt[key] != runtime["numpy"][key]:
            raise CustodyFault("NUMPY_RUNTIME", "%s drift" % key)
    bash_path = Path(runtime["bash_path"])
    if not bash_path.is_absolute() or bash_path.is_symlink() or \
            bash_path.resolve(strict=True) != bash_path or \
            sha256_path(bash_path) != runtime["bash_binary_sha256"]:
        raise CustodyFault("BASH_RUNTIME", "absolute Bash binding drift")
    require_root_owned_nonwritable(bash_path, "Bash executable")
    receipt = {
        "python_path": str(python_path),
        "python_binary_sha256": sha256_path(python_path),
        "bash_path": str(bash_path),
        "bash_binary_sha256": sha256_path(bash_path),
        "python_version": sys.version,
        "python_cache_tag": sys.implementation.cache_tag,
        "stdlib": sysconfig.get_paths().get("stdlib"),
        "runtime_root": str(runtime_root),
        "environment_manifest_relative_path": manifest_relative,
        "environment_manifest_sha256": runtime[
            "environment_manifest_sha256"],
        "environment_files": len(entries),
        "environment_tree_sha256": sha256_json(entries),
        "numpy": numpy_receipt,
    }
    if sha256_json(receipt) != runtime.get("receipt_sha256"):
        raise CustodyFault("RUNTIME_RECEIPT", "pinned runtime receipt drift")
    return receipt


def meminfo_swap_used_bytes(path="/proc/meminfo") -> int:
    values = {}
    for line in Path(path).read_text().splitlines():
        fields = line.split()
        if fields and fields[0].rstrip(":") in ("SwapTotal", "SwapFree"):
            values[fields[0].rstrip(":")] = int(fields[1]) * 1024
    if set(values) != {"SwapTotal", "SwapFree"}:
        raise CustodyFault("SWAP", "host swap telemetry unavailable")
    return values["SwapTotal"] - values["SwapFree"]


def current_cgroup_path(proc_self_cgroup="/proc/self/cgroup") -> str:
    rows = Path(proc_self_cgroup).read_text().splitlines()
    matches = [line.split(":", 2)[2] for line in rows
               if line.startswith("0::")]
    if len(matches) != 1 or not matches[0].startswith("/"):
        raise CustodyFault("CGROUP", "unified cgroup-v2 membership unavailable")
    return matches[0]


def _read_limit(path: Path):
    value = path.read_text().strip()
    return value if value == "max" else int(value)


def _counter_file(path: Path) -> dict[str, int]:
    counters = {}
    for line in path.read_text().splitlines():
        fields = line.split()
        if len(fields) != 2 or fields[0] in counters:
            raise CustodyFault("CGROUP_COUNTER", "malformed counter file")
        counters[fields[0]] = int(fields[1])
    if not counters:
        raise CustodyFault("CGROUP_COUNTER", "empty counter file")
    return counters


def processes_for_uid(uid: int, proc_root=Path("/proc")) -> set[int]:
    result = set()
    for candidate in Path(proc_root).iterdir():
        if not candidate.name.isdigit():
            continue
        try:
            rows = candidate.joinpath("status").read_text().splitlines()
            uid_row = next(row for row in rows if row.startswith("Uid:"))
            effective = int(uid_row.split()[2])
            if effective == uid:
                result.add(int(candidate.name))
        except (FileNotFoundError, ProcessLookupError, PermissionError,
                StopIteration, ValueError, IndexError):
            continue
    return result


def verify_cgroup_contract(systemd: dict, runtime: dict,
                           supervisor_path: Path, authorization_path: Path,
                           registered_run_parent: Path,
                           cgroup_root=Path("/sys/fs/cgroup"),
                           unit_root=Path("/run/systemd/system"),
                           dropin_roots=None,
                           observed_path_override=None,
                           require_root_owner=True,
                           require_dedicated_uid=True) -> dict:
    unit_name = systemd.get("unit_name")
    if not isinstance(unit_name, str) or not unit_name.endswith(".service") or \
            not SAFE_ID_RE.fullmatch(unit_name[:-8]):
        raise CustodyFault("SYSTEMD_UNIT", "unsafe registered unit name")
    observed_path = observed_path_override or current_cgroup_path()
    if observed_path != systemd.get("cgroup_path"):
        raise CustodyFault("CGROUP", "registered cgroup path mismatch")
    fragment = Path(systemd.get("unit_fragment_path", ""))
    expected_fragment = unit_root / unit_name
    if fragment != expected_fragment or fragment.is_symlink() or \
            not fragment.is_file() or \
            sha256_path(fragment) != systemd.get("unit_fragment_sha256"):
        raise CustodyFault("SYSTEMD_UNIT", "live immutable unit binding drift")
    fragment_stat = fragment.stat()
    if (require_root_owner and fragment_stat.st_uid != 0) or \
            fragment_stat.st_mode & 0o022:
        raise CustodyFault("SYSTEMD_UNIT", "unit fragment is not root-owned immutable")
    if dropin_roots is None:
        dropin_roots = (
            Path("/etc/systemd/system.control"),
            Path("/run/systemd/system.control"),
            Path("/run/systemd/transient"),
            Path("/run/systemd/generator.early"),
            Path("/etc/systemd/system"),
            Path("/etc/systemd/system.attached"),
            Path("/run/systemd/system"),
            Path("/run/systemd/system.attached"),
            Path("/run/systemd/generator"),
            Path("/usr/local/lib/systemd/system"),
            Path("/usr/lib/systemd/system"),
            Path("/run/systemd/generator.late"),
        )
    stem, suffix = unit_name[:-8], ".service"
    dropin_names = {unit_name + ".d", "service.d"}
    pieces = stem.split("-")
    for end in range(len(pieces) - 1, 0, -1):
        dropin_names.add("-".join(pieces[:end]) + "-" + suffix + ".d")
    for root in dropin_roots:
        for name in dropin_names:
            candidate = Path(root) / name
            if candidate.exists() or candidate.is_symlink():
                raise CustodyFault(
                    "SYSTEMD_DROPIN",
                    "effective unit drop-ins are forbidden: %s" % candidate)
    expected_start = [runtime["python_path"], "-I", "-B",
                      str(supervisor_path), "--authorization",
                      str(authorization_path)]
    expected_stop = expected_start + ["--terminalize"]
    if systemd.get("exec_start_argv") != expected_start or \
            systemd.get("exec_stop_post_argv") != expected_stop:
        raise CustodyFault("SYSTEMD_UNIT", "unit argv binding drift")
    settings = {}
    for raw in fragment.read_text().splitlines():
        if "=" in raw and not raw.lstrip().startswith("#"):
            key, value = raw.split("=", 1)
            settings.setdefault(key.strip(), []).append(value.strip())
    exact_single = {
        "Type": "exec",
        "MemoryMax": str(RSS_LIMIT_BYTES), "MemorySwapMax": "0",
        "TasksMax": str(TASKS_LIMIT), "RuntimeMaxSec": str(TIMEOUT_SECONDS),
        "KillMode": "control-group", "Delegate": "no",
        "NoNewPrivileges": "yes", "PrivateTmp": "yes",
        "SendSIGKILL": "yes", "OOMPolicy": "stop", "MemoryOOMGroup": "yes",
        "TimeoutStopSec": "60",
        "ProtectControlGroups": "yes", "ProtectKernelTunables": "yes",
        "PrivateDevices": "yes", "ProtectSystem": "strict",
        "ProtectHome": "read-only", "RestrictSUIDSGID": "yes",
        "LockPersonality": "yes", "RestrictNamespaces": "yes",
        "UMask": "0077", "WorkingDirectory": "/",
        "User": DEDICATED_SERVICE_USER, "Group": DEDICATED_SERVICE_USER,
        "SetLoginEnvironment": "no",
        "UnsetEnvironment": " ".join(PREEXEC_UNSET_ENVIRONMENT),
        "InaccessiblePaths": "/tmp /var/tmp /dev/shm",
    }
    allowed_unit_keys = set(exact_single) | {
        "Description", "Environment", "ReadWritePaths", "ExecStart",
        "ExecStopPost",
    }
    unexpected_unit_keys = set(settings) - allowed_unit_keys
    if unexpected_unit_keys:
        raise CustodyFault(
            "SYSTEMD_UNIT",
            "unregistered effective unit directives: %s" %
            sorted(unexpected_unit_keys))
    for key, value in exact_single.items():
        if settings.get(key) != [value]:
            raise CustodyFault("SYSTEMD_UNIT", "%s unit setting drift" % key)
    required_environment = {"%s=%s" % item
                            for item in SUPERVISOR_REQUIRED_ENV.items()}
    if set(settings.get("Environment", [])) != required_environment:
        raise CustodyFault("SYSTEMD_UNIT", "unit environment drift")
    if settings.get("ReadWritePaths") != [str(registered_run_parent)]:
        raise CustodyFault("SYSTEMD_UNIT", "registered write root drift")
    if settings.get("ExecStart") != [" ".join(expected_start)] or \
            settings.get("ExecStopPost") != [" ".join(expected_stop)]:
        raise CustodyFault("SYSTEMD_UNIT", "live unit command drift")
    cgroup = cgroup_root / observed_path.lstrip("/")
    if not cgroup.is_dir() or cgroup.is_symlink():
        raise CustodyFault("CGROUP", "registered cgroup directory missing")
    limits = {
        "memory.max": _read_limit(cgroup / "memory.max"),
        "memory.swap.max": _read_limit(cgroup / "memory.swap.max"),
        "pids.max": _read_limit(cgroup / "pids.max"),
    }
    if limits != {"memory.max": RSS_LIMIT_BYTES,
                  "memory.swap.max": 0, "pids.max": TASKS_LIMIT}:
        raise CustodyFault("CGROUP_LIMITS", "hard cgroup limits drift")
    if (cgroup / "cgroup.subtree_control").read_text().strip():
        raise CustodyFault("CGROUP_DELEGATION", "job cgroup is delegated")
    cgroup_stat = cgroup.stat()
    if (require_root_owner and cgroup_stat.st_uid != 0) or \
            cgroup_stat.st_mode & 0o022:
        raise CustodyFault("CGROUP_DELEGATION", "job cgroup is writable")
    if (cgroup / "cgroup.type").read_text().strip() != "domain":
        raise CustodyFault("CGROUP", "job cgroup is not a domain")
    pids = {int(value) for value in (cgroup / "cgroup.procs").read_text().split()}
    if pids != {os.getpid()} or int((cgroup / "pids.current").read_text()) != 1:
        raise CustodyFault("CGROUP_DUPLICATE",
                           "supervisor is not the sole initial job process")
    same_uid = processes_for_uid(os.getuid()) if require_dedicated_uid else pids
    if require_dedicated_uid and same_uid - pids:
        raise CustodyFault("DEDICATED_UID",
                           "service UID has a process outside the job cgroup")
    memory_events = _counter_file(cgroup / "memory.events")
    pids_events = _counter_file(cgroup / "pids.events")
    if any(memory_events.get(key, 0) for key in
           ("max", "oom", "oom_kill", "oom_group_kill")) or \
            pids_events.get("max", 0):
        raise CustodyFault("CGROUP_EVENTS",
                           "resource-limit event predates registered work")
    return {"path": observed_path, "directory": str(cgroup),
            "limits": limits, "initial_pids": sorted(pids),
            "initial_same_uid_pids": sorted(same_uid),
            "initial_memory_events": memory_events,
            "initial_pids_events": pids_events,
            "unit_name": unit_name,
            "unit_fragment_sha256": systemd["unit_fragment_sha256"],
            "exec_start_argv": expected_start,
            "exec_stop_post_argv": expected_stop}


def pid_start_time(pid: int, proc_root=Path("/proc")) -> int:
    raw = (proc_root / str(pid) / "stat").read_text()
    tail = raw[raw.rfind(")") + 2:].split()
    return int(tail[19])


def cgroup_snapshot(cgroup_dir: Path) -> dict:
    pids = sorted(int(value) for value in
                  (cgroup_dir / "cgroup.procs").read_text().split())
    identities = {}
    for pid in pids:
        try:
            identities[str(pid)] = pid_start_time(pid)
        except (FileNotFoundError, ProcessLookupError, ValueError, IndexError):
            identities[str(pid)] = None
    events = _counter_file(cgroup_dir / "memory.events")
    pids_events = _counter_file(cgroup_dir / "pids.events")
    return {
        "pids": pids, "pid_start_times": identities,
        "same_uid_pids": sorted(processes_for_uid(os.getuid())),
        "pids_current": int((cgroup_dir / "pids.current").read_text()),
        "pids_events": pids_events,
        "memory_current": int((cgroup_dir / "memory.current").read_text()),
        "memory_peak": int((cgroup_dir / "memory.peak").read_text()),
        "memory_swap_current": int(
            (cgroup_dir / "memory.swap.current").read_text()),
        "memory_events": events,
        "host_swap_used": meminfo_swap_used_bytes(),
    }


def lifecycle_gate(deadline: float, cgroup_dir: Path | None = None,
                   expected_pids=None) -> dict | None:
    if time.monotonic() > deadline:
        raise CustodyFault("WHOLE_JOB_TIMEOUT", "1200-second cap")
    if meminfo_swap_used_bytes() != 0:
        raise CustodyFault("SWAP_RUNTIME", "host swap is nonzero")
    if cgroup_dir is None:
        return None
    sample = cgroup_snapshot(cgroup_dir)
    if sample["memory_swap_current"] != 0 or sample["host_swap_used"] != 0:
        raise CustodyFault("SWAP_RUNTIME", "cgroup/host swap is nonzero")
    if any(sample["memory_events"].get(key, 0)
           for key in ("max", "oom", "oom_kill", "oom_group_kill")):
        raise CustodyFault("MEMORY_LIMIT_EVENT",
                           "cgroup memory limit event")
    if sample["pids_events"].get("max", 0):
        raise CustodyFault("TASKS_LIMIT_EVENT", "cgroup tasks limit event")
    if set(sample["same_uid_pids"]) - set(sample["pids"]):
        raise CustodyFault("DEDICATED_UID",
                           "service UID has a process outside the job cgroup")
    if sample["memory_current"] >= RSS_LIMIT_BYTES or \
            sample["memory_peak"] >= RSS_LIMIT_BYTES:
        raise CustodyFault("MEMORY_LIMIT", "cgroup memory limit reached")
    if expected_pids is not None and set(sample["pids"]) != set(expected_pids):
        raise CustodyFault("ORPHAN", "unexpected cgroup membership")
    return sample


class StickyMonitor:
    def __init__(self, cgroup_dir: Path, deadline: float, telemetry_path: Path):
        self.cgroup_dir = cgroup_dir
        self.deadline = deadline
        self.telemetry_path = telemetry_path
        self.stop_event = threading.Event()
        self.fault = None
        self.samples = 0
        self.registry = {}
        self.peak = 0
        self.thread = threading.Thread(target=self._run, daemon=False)

    def start(self):
        self.thread.start()

    def _latch(self, code, detail):
        if self.fault is None:
            self.fault = CustodyFault(code, detail)

    def _run(self):
        try:
            with self.telemetry_path.open("x", encoding="utf-8") as handle:
                while not self.stop_event.is_set():
                    sample = cgroup_snapshot(self.cgroup_dir)
                    sample.update({"sample": self.samples, "utc": utc_now(),
                                   "monotonic": time.monotonic()})
                    for pid, start in sample["pid_start_times"].items():
                        previous = self.registry.get(pid)
                        if previous is not None and previous != start:
                            self._latch("PID_REUSE", "PID start-time changed")
                        self.registry[pid] = start
                    self.peak = max(self.peak, sample["memory_peak"])
                    if sample["memory_swap_current"] != 0 or \
                            sample["host_swap_used"] != 0:
                        self._latch("SWAP_RUNTIME", "sticky swap violation")
                    if any(sample["memory_events"].get(key, 0)
                           for key in ("max", "oom", "oom_kill",
                                       "oom_group_kill")):
                        self._latch("MEMORY_LIMIT_EVENT",
                                    "cgroup memory limit event")
                    if sample["pids_events"].get("max", 0):
                        self._latch("TASKS_LIMIT_EVENT",
                                    "cgroup tasks limit event")
                    if set(sample["same_uid_pids"]) - set(sample["pids"]):
                        self._latch(
                            "DEDICATED_UID",
                            "service UID has a process outside the job cgroup")
                    if sample["memory_current"] >= RSS_LIMIT_BYTES or \
                            sample["memory_peak"] >= RSS_LIMIT_BYTES:
                        self._latch("MEMORY_LIMIT",
                                    "cgroup memory limit reached")
                    if time.monotonic() > self.deadline:
                        self._latch("WHOLE_JOB_TIMEOUT", "1200-second cap")
                    handle.write(json.dumps(sample, sort_keys=True) + "\n")
                    handle.flush()
                    self.samples += 1
                    self.stop_event.wait(SAMPLE_INTERVAL_SECONDS)
                handle.flush()
                os.fsync(handle.fileno())
        except Exception as error:
            self._latch("MONITOR_DIED", repr(error))

    def check(self):
        if self.fault:
            raise self.fault
        if not self.thread.is_alive() and not self.stop_event.is_set():
            raise CustodyFault("MONITOR_DIED", "monitor stopped unexpectedly")
        if time.monotonic() > self.deadline:
            raise CustodyFault("WHOLE_JOB_TIMEOUT", "1200-second cap")

    def stop(self):
        self.stop_event.set()
        self.thread.join(timeout=5)
        if self.thread.is_alive():
            raise CustodyFault("MONITOR_DIED", "monitor did not join")
        if self.fault:
            raise self.fault


def terminate_cgroup_members(cgroup_dir: Path, exclude=frozenset(),
                             grace=2.0) -> dict:
    signals = []
    for sig, wait in ((signal.SIGTERM, grace), (signal.SIGKILL, grace)):
        pids = {int(value) for value in
                (cgroup_dir / "cgroup.procs").read_text().split()} - set(exclude)
        for pid in sorted(pids):
            try:
                start = pid_start_time(pid)
                os.kill(pid, sig)
                signals.append({"pid": pid, "start_time": start,
                                "signal": sig.name})
            except (FileNotFoundError, ProcessLookupError):
                pass
        deadline = time.monotonic() + wait
        while time.monotonic() < deadline:
            remaining = {int(value) for value in
                         (cgroup_dir / "cgroup.procs").read_text().split()} - \
                set(exclude)
            if not remaining:
                break
            time.sleep(0.05)
    remaining = {int(value) for value in
                 (cgroup_dir / "cgroup.procs").read_text().split()} - \
        set(exclude)
    return {"signals": signals, "remaining_pids": sorted(remaining)}


def deterministic_tar(path: Path, members: list[tuple[str, Path]]) -> str:
    raw = io.BytesIO()
    with tarfile.open(fileobj=raw, mode="w") as archive:
        for arcname, source in sorted(members):
            data = source.read_bytes()
            info = tarfile.TarInfo(arcname)
            info.size = len(data)
            info.mode = 0o444
            info.mtime = info.uid = info.gid = 0
            info.uname = info.gname = ""
            archive.addfile(info, io.BytesIO(data))
    compressed = io.BytesIO()
    with gzip.GzipFile(filename="", mode="wb", fileobj=compressed,
                       mtime=0) as output:
        output.write(raw.getvalue())
    atomic_bytes(path, compressed.getvalue(), 0o400, replace=False)
    return sha256_path(path)


def artifact_inventory(run_dir: Path, excluded) -> dict:
    files = {}
    for path in sorted(run_dir.rglob("*")):
        if path.is_symlink():
            raise CustodyFault("ARCHIVE", "symlink in run artifacts")
        if path.is_file() and path.name not in excluded:
            relative = str(path.relative_to(run_dir))
            files[relative] = {"sha256": sha256_path(path),
                               "bytes": path.stat().st_size}
    return files


def replay_archive(archive_path: Path, inventory: dict) -> dict:
    observed = {}
    with tarfile.open(archive_path, "r:gz") as archive:
        for member in archive.getmembers():
            if (not member.isfile() or member.name.startswith("/") or
                    ".." in Path(member.name).parts or member.name in observed):
                raise CustodyFault("ARCHIVE_REPLAY", "unsafe archive member")
            handle = archive.extractfile(member)
            data = handle.read() if handle else b""
            observed[member.name] = {"sha256": sha256_bytes(data),
                                     "bytes": len(data)}
    if observed != inventory:
        raise CustodyFault("ARCHIVE_REPLAY", "archive inventory mismatch")
    return {"members": len(observed),
            "inventory_sha256": sha256_json(observed)}


def publish_terminal_bundle(run_dir: Path, terminal_core: dict,
                            gate=lambda: None) -> dict:
    gate()
    authority = run_dir / "TERMINAL.json"
    emergency = run_dir / "EMERGENCY_NO_VERDICT.json"
    if authority.exists() or emergency.exists():
        raise CustodyFault("TERMINAL_DUPLICATE", "terminal already published")
    # A killed pre-promotion run must not leave even literal positive wording
    # in a non-authoritative file.  Bind the intended core only by an opaque
    # digest; TERMINAL.json remains the sole place a positive status may occur.
    provisional_core = {
        "schema": TERMINAL_SCHEMA + ".pending",
        "route": ROUTE,
        "status": "PENDING_TERMINAL_CUSTODY_NO_AUTHORITY",
        "mathematical_outcome": None,
        "terminal_core_sha256": sha256_json(terminal_core),
        "launch_authorization_sha256": terminal_core.get(
            "launch_authorization_sha256"),
        "job_id": terminal_core.get("job_id"),
        "target_exponent": terminal_core.get("target_exponent"),
    }
    provisional = run_dir / "PROVISIONAL_TERMINAL_CORE.json"
    atomic_json(provisional, provisional_core, 0o400, replace=False)
    gate()
    excluded = {"ARTIFACT_MANIFEST.json", "EVIDENCE.tar.gz",
                "EVIDENCE.tar.gz.sha256", "TERMINAL.json",
                "EMERGENCY_NO_VERDICT.json"}
    inventory = artifact_inventory(run_dir, excluded)
    gate()
    manifest = {"schema": TERMINAL_SCHEMA + ".artifacts",
                "files": inventory,
                "inventory_sha256": sha256_json(inventory)}
    manifest_path = run_dir / "ARTIFACT_MANIFEST.json"
    atomic_json(manifest_path, manifest, 0o400, replace=False)
    gate()
    inventory_with_manifest = dict(inventory)
    inventory_with_manifest[manifest_path.name] = {
        "sha256": sha256_path(manifest_path),
        "bytes": manifest_path.stat().st_size}
    members = [(relative, run_dir / relative)
               for relative in inventory_with_manifest]
    archive_path = run_dir / "EVIDENCE.tar.gz"
    archive_sha = deterministic_tar(archive_path, members)
    gate()
    sidecar = run_dir / "EVIDENCE.tar.gz.sha256"
    atomic_bytes(sidecar, ("%s  %s\n" %
                           (archive_sha, archive_path.name)).encode(),
                 0o400, replace=False)
    replay = replay_archive(archive_path, inventory_with_manifest)
    gate()
    if sha256_path(archive_path) != archive_sha or \
            sidecar.read_text() != "%s  %s\n" % (archive_sha,
                                                   archive_path.name):
        raise CustodyFault("ARCHIVE_REPLAY", "archive sidecar drift")
    terminal = dict(terminal_core)
    terminal.update({
        "artifact_manifest_sha256": sha256_path(manifest_path),
        "artifact_inventory_sha256": manifest["inventory_sha256"],
        "evidence_archive_sha256": archive_sha,
        "archive_replay": replay,
        "authority_published_last": True,
    })
    gate()
    atomic_json(authority, terminal, 0o400, replace=False)
    return terminal


def emergency_no_verdict(run_dir: Path, core: dict, error) -> dict:
    payload = dict(core)
    payload.update({"schema": TERMINAL_SCHEMA,
                    "status": "NO_VERDICT_TERMINAL_BUNDLE_FAULT",
                    "mathematical_outcome": None,
                    "terminal_bundle_fault": repr(error),
                    "end_utc": utc_now()})
    path = run_dir / "TERMINAL.json"
    if path.exists():
        observed = json.loads(path.read_text())
        if str(observed.get("status", "")).startswith("NO_VERDICT"):
            return observed
        raise CustodyFault("TERMINAL_DUPLICATE",
                           "positive terminal existed during emergency")
    atomic_json(path, payload, 0o400, replace=False)
    if json.loads(path.read_text()) != payload:
        raise CustodyFault("TERMINAL_REPLAY", "emergency authority drift")
    return payload


RUN_OWNERSHIP_SCHEMA = TERMINAL_SCHEMA + ".run-ownership"


def run_ownership_payload(run_dir: Path, authorization: dict,
                          auth_sha: str, invocation_id: str) -> dict:
    observed = run_dir.stat()
    return {
        "schema": RUN_OWNERSHIP_SCHEMA,
        "run_dir": str(run_dir.resolve()),
        "directory_device": observed.st_dev,
        "directory_inode": observed.st_ino,
        "launch_authorization_sha256": auth_sha,
        "systemd_invocation_id": invocation_id,
        "job_id": authorization["bindings"]["job_id"],
        "target_exponent": authorization["bindings"]["target_exponent"],
        "lane_tag": authorization["bindings"]["lane_tag"],
    }


def validate_run_ownership(run_dir: Path, authorization: dict,
                           auth_sha: str, invocation_id: str) -> dict:
    sentinel = run_dir / "RUN_OWNERSHIP.json"
    if run_dir.is_symlink() or not run_dir.is_dir() or sentinel.is_symlink() or \
            not sentinel.is_file():
        raise CustodyFault("RUN_OWNERSHIP",
                           "registered directory has no ownership sentinel")
    observed = json.loads(sentinel.read_text())
    expected = run_ownership_payload(
        run_dir, authorization, auth_sha, invocation_id)
    if observed != expected:
        raise CustodyFault("RUN_OWNERSHIP",
                           "registered directory ownership binding drift")
    return observed


def validate_existing_terminal(run_dir: Path, terminal: dict,
                               authorization: dict, auth_sha: str,
                               live_verified: bool,
                               invocation_id: str) -> None:
    bindings = authorization["bindings"]
    if terminal.get("schema") != TERMINAL_SCHEMA or \
            terminal.get("route") != ROUTE or \
            terminal.get("job_id") != bindings["job_id"] or \
            terminal.get("target_exponent") != bindings["target_exponent"] or \
            terminal.get("launch_authorization_sha256") != auth_sha or \
            terminal.get("systemd_invocation_id") != invocation_id or \
            terminal.get("claims_forbidden") != FORBIDDEN_CLAIMS:
        raise CustodyFault("POSTSTOP_TERMINAL",
                           "existing terminal is not this registered job")
    status = str(terminal.get("status", ""))
    if not (status.startswith("NO_VERDICT") or
            status == "FINITE_SOURCE_RESULT_CUSTODY_PASS"):
        raise CustodyFault("POSTSTOP_TERMINAL",
                           "existing terminal status is unregistered")
    if status == "FINITE_SOURCE_RESULT_CUSTODY_PASS" and not live_verified:
        raise CustodyFault("POSTSTOP_LIVE_AUTH",
                           "cannot re-endorse positive terminal")
    archive = run_dir / "EVIDENCE.tar.gz"
    manifest = run_dir / "ARTIFACT_MANIFEST.json"
    if not is_sha256(terminal.get("evidence_archive_sha256")) or \
            not is_sha256(terminal.get("artifact_manifest_sha256")) or \
            archive.is_symlink() or manifest.is_symlink() or \
            sha256_path(archive) != terminal["evidence_archive_sha256"] or \
            sha256_path(manifest) != terminal["artifact_manifest_sha256"]:
        raise CustodyFault("POSTSTOP_TERMINAL",
                           "existing terminal bundle hash drift")
    manifest_payload = json.loads(manifest.read_text())
    if set(manifest_payload) != {"schema", "files", "inventory_sha256"} or \
            manifest_payload.get("schema") != TERMINAL_SCHEMA + ".artifacts" or \
            sha256_json(manifest_payload["files"]) != \
                manifest_payload["inventory_sha256"]:
        raise CustodyFault("POSTSTOP_TERMINAL",
                           "existing artifact manifest semantic drift")
    archive_inventory = dict(manifest_payload["files"])
    archive_inventory[manifest.name] = {
        "sha256": terminal["artifact_manifest_sha256"],
        "bytes": manifest.stat().st_size,
    }
    replay = replay_archive(archive, archive_inventory)
    if terminal.get("archive_replay") != replay or \
            terminal.get("artifact_inventory_sha256") != \
                manifest_payload["inventory_sha256"]:
        raise CustodyFault("POSTSTOP_TERMINAL",
                           "existing terminal archive replay drift")


def publish_pre_run_rejection(authorization: dict, auth_sha: str,
                              terminal_base: dict, error: CustodyFault) -> dict:
    candidate = Path(authorization["paths"]["run_dir"])
    if not candidate.is_absolute() or not is_sha256(auth_sha):
        raise CustodyFault("PRE_RUN_DURABILITY", "unsafe rejection target")
    parent = candidate.parent.resolve(strict=True)
    payload = dict(terminal_base)
    payload.update({
        "status": "NO_VERDICT_BEFORE_REGISTERED_RUN_DIR",
        "fault_code": error.code, "fault_detail": error.detail,
        "mathematical_outcome": None, "end_utc": utc_now(),
        "launch_authorization_sha256": auth_sha,
        "registered_run_dir": str(candidate),
        "authority_kind": "PRE_RUN_REJECTION_SIDECAR",
    })
    invocation = str(terminal_base.get("systemd_invocation_id", "unknown"))
    path = parent / (".%s.NO_VERDICT.%s.%s.json" %
                     (candidate.name, auth_sha[:16], invocation[:16]))
    if path.exists():
        observed = json.loads(path.read_text())
        if observed.get("launch_authorization_sha256") != auth_sha or \
                observed.get("systemd_invocation_id") != invocation or \
                not str(observed.get("status", "")).startswith("NO_VERDICT"):
            raise CustodyFault("PRE_RUN_DURABILITY", "rejection collision")
        return observed
    atomic_json(path, payload, 0o400, replace=False)
    return payload


def _safe_state_envelope(path: Path) -> tuple[dict, str, str]:
    raw = path.read_bytes()
    envelope_sha = sha256_bytes(raw)
    value = json.loads(raw)
    if set(value) != {"payload", "payload_sha256"} or \
            sha256_json(value["payload"]) != value["payload_sha256"]:
        raise CustodyFault("STATE", "state envelope authentication failed")
    if value["payload"].get("schema") != STATE_SCHEMA:
        raise CustodyFault("STATE", "state schema drift")
    return value["payload"], envelope_sha, value["payload_sha256"]


def validate_target16_handoff(paths: dict, provenance: dict,
                              run_dir: Path) -> tuple[Path, dict]:
    required = {
        "terminal_archive_sha256", "terminal_manifest_sha256",
        "terminal_authority_sha256", "job_identity_sha256",
        "state_envelope_sha256", "state_payload_sha256", "history_sha256",
        "achieved_exponent", "authorization_sha256",
        "runtime_environment_sha256",
    }
    if not isinstance(provenance, dict) or set(provenance) != required or \
            provenance.get("achieved_exponent") != 16 or any(
                not is_sha256(provenance[key]) for key in
                required - {"achieved_exponent"}):
        raise CustodyFault("TARGET64", "target16 provenance shape drift")
    named = {
        "terminal": ("target16_terminal_path", "terminal_authority_sha256"),
        "manifest": ("target16_manifest_path", "terminal_manifest_sha256"),
        "archive": ("target16_archive_path", "terminal_archive_sha256"),
    }
    snapshots = {}
    snapshot_names = {
        "terminal": "TARGET16_TERMINAL.snapshot.json",
        "manifest": "TARGET16_MANIFEST.snapshot.json",
        "archive": "TARGET16_EVIDENCE.snapshot.tar.gz",
    }
    for label, (path_key, hash_key) in named.items():
        path = Path(paths[path_key])
        if not path.is_absolute() or path.is_symlink():
            raise CustodyFault("TARGET64", "%s path is unsafe" % label)
        path = path.resolve(strict=True)
        snapshot = run_dir / snapshot_names[label]
        copy_verified_file(path, snapshot, provenance[hash_key])
        snapshots[label] = snapshot
    # Parse and replay only the pinned immutable snapshots, never the originals
    # which can change between an initial hash and a later copy.
    terminal = json.loads(snapshots["terminal"].read_text())
    manifest = json.loads(snapshots["manifest"].read_text())
    if terminal.get("status") != "FINITE_SOURCE_RESULT_CUSTODY_PASS" or \
            terminal.get("mathematical_outcome") != \
                "FINITE_SOURCE_LIFT_ONLY" or \
            terminal.get("target_exponent") != 16 or \
            terminal.get("achieved_exponent") != 16 or \
            terminal.get("evidence_archive_sha256") != \
                provenance["terminal_archive_sha256"] or \
            terminal.get("artifact_manifest_sha256") != \
                provenance["terminal_manifest_sha256"] or \
            terminal.get("launch_authorization_sha256") != \
                provenance["authorization_sha256"] or \
            terminal.get("runtime_environment_sha256") != \
                provenance["runtime_environment_sha256"] or \
            terminal.get("job_identity_sha256") != \
                provenance["job_identity_sha256"] or \
            terminal.get("output_binding", {}).get("status") != \
                "FINITE_SOURCE_LIFT_ONLY" or \
            terminal.get("output_binding", {}).get(
                "state_envelope_sha256") != \
                provenance["state_envelope_sha256"] or \
            terminal.get("output_binding", {}).get(
                "state_payload_sha256") != \
                provenance["state_payload_sha256"] or \
            terminal.get("output_binding", {}).get("history_sha256") != \
                provenance["history_sha256"]:
        raise CustodyFault("TARGET64", "target16 terminal semantic drift")
    if set(manifest) != {"schema", "files", "inventory_sha256"} or \
            sha256_json(manifest["files"]) != manifest["inventory_sha256"]:
        raise CustodyFault("TARGET64", "target16 manifest drift")
    state_member = manifest["files"].get("FINAL_STATE.snapshot.json")
    if not isinstance(state_member, dict) or \
            state_member.get("sha256") != provenance["state_envelope_sha256"]:
        raise CustodyFault("TARGET64",
                           "target16 manifest/state provenance fork")
    archive_inventory = dict(manifest["files"])
    archive_inventory["ARTIFACT_MANIFEST.json"] = {
        "sha256": provenance["terminal_manifest_sha256"],
        "bytes": snapshots["manifest"].stat().st_size,
    }
    replay = replay_archive(snapshots["archive"], archive_inventory)
    if terminal.get("archive_replay") != replay or \
            terminal.get("artifact_inventory_sha256") != \
                manifest["inventory_sha256"]:
        raise CustodyFault("TARGET64", "target16 archive replay binding drift")
    return snapshots["terminal"], terminal


def normalized_child_environment(run_dir: Path) -> dict:
    return {
        "HOME": str(run_dir / "home"), "LANG": "C.UTF-8",
        "LC_ALL": "C.UTF-8", "PATH": "/usr/bin:/bin", "TZ": "UTC",
        "PYTHONHASHSEED": "0", "PYTHONNOUSERSITE": "1",
        "PYTHONDONTWRITEBYTECODE": "1", "OMP_NUM_THREADS": "1",
        "OPENBLAS_NUM_THREADS": "1", "MKL_NUM_THREADS": "1",
        "NUMEXPR_NUM_THREADS": "1", "VECLIB_MAXIMUM_THREADS": "1",
        "SHLVL": "0",
        "JC2_D43_HENSEL_AWS_AUTH": AUTH_PATH_SENTINEL,
        "JC2_D43_HENSEL_AWS_AUTH_SHA256": AUTH_SHA_SENTINEL,
    }


def materialize_child_environment(normalized: dict, marker_path: Path,
                                  marker_sha256: str) -> dict:
    if not marker_path.is_absolute() or not is_sha256(marker_sha256):
        raise CustodyFault("AUTH_ENVIRONMENT", "bad marker materialization")
    environment = dict(normalized)
    environment["JC2_D43_HENSEL_AWS_AUTH"] = str(marker_path)
    environment["JC2_D43_HENSEL_AWS_AUTH_SHA256"] = marker_sha256
    return environment


def _marker_payload(authorization, identity, live_tag, auth_sha,
                    execution_root, source_archive_path, source_archive_sha,
                    runtime,
                    run_dir, state_path, report_path, d21_private,
                    core23, supervisor_pid) -> dict:
    bindings = authorization["bindings"]
    environment = normalized_child_environment(run_dir)
    marker = {
        "schema": MARKER_SCHEMA,
        "target_exponent": bindings["target_exponent"],
        "lane_tag": bindings["lane_tag"], "job_id": bindings["job_id"],
        "host_identity": identity, "live_authorization_tag": live_tag,
        "launch_authorization_path": str(
            run_dir / "LAUNCH_AUTHORIZATION.snapshot.json"),
        "launch_authorization_sha256": auth_sha,
        "review_report_path": str(run_dir / "INDEPENDENT_REVIEW.snapshot.md"),
        "review_report_sha256": bindings["review_report_sha256"],
        "payload_manifest_path": str(
            execution_root / authorization["paths"]["payload_manifest"]),
        "payload_manifest_sha256": bindings["payload_manifest_sha256"],
        "preregistration_path": str(
            execution_root / authorization["paths"]["preregistration"]),
        "preregistration_sha256": bindings["preregistration_sha256"],
        "runner_sha256": bindings["runner_sha256"],
        "base_runner_sha256": bindings["base_runner_sha256"],
        "supervisor_path": str(Path(__file__).resolve()),
        "supervisor_sha256": bindings["supervisor_sha256"],
        "worker_path": str(execution_root / authorization["paths"]["worker"]),
        "worker_sha256": bindings["worker_sha256"],
        "execution_root": str(execution_root),
        "source_archive_path": str(source_archive_path),
        "source_archive_sha256": source_archive_sha,
        "runtime_environment": environment,
        "runtime_environment_sha256": sha256_json(environment),
        "runtime_receipt_sha256": runtime["receipt_sha256"],
        "job_identity_sha256": sha256_json({
            "authorization_sha256": auth_sha, "identity": identity,
            "job_id": bindings["job_id"], "target": bindings["target_exponent"],
            "source_archive_sha256": source_archive_sha,
            "target16_provenance": bindings["target16_provenance"]}),
        "supervisor_pid": supervisor_pid, "state_path": str(state_path),
        "report_path": str(report_path),
        "d21_private_path": str(d21_private),
        "d21_private_sha256": EXPECTED_D21_SHA256,
        "core23_path": str(core23), "core23_sha256": EXPECTED_CORE23_SHA256,
        "target16_provenance": bindings["target16_provenance"],
        "claims_forbidden_sha256": sha256_json(FORBIDDEN_CLAIMS),
    }
    # External authorization binds the environment values after the private
    # run directory is fixed, so it contains this exact digest.
    if bindings["runtime_environment_sha256"] != marker[
            "runtime_environment_sha256"] or \
            bindings["runtime_receipt_sha256"] != marker[
                "runtime_receipt_sha256"] or \
            bindings["source_archive_sha256"] != source_archive_sha or \
            bindings["claims_forbidden_sha256"] != \
                marker["claims_forbidden_sha256"] or \
            bindings["d21_private_sha256"] != EXPECTED_D21_SHA256 or \
            bindings["core23_sha256"] != EXPECTED_CORE23_SHA256:
        raise CustodyFault("AUTH_RUNTIME", "runtime/environment binding drift")
    return marker


def _run_child(argv, environment, monitor: StickyMonitor, stdout, stderr):
    monitor.check()
    with open(stdout, "xb") as out, open(stderr, "xb") as err:
        process = subprocess.Popen(argv, env=environment, cwd="/",
                                   stdin=subprocess.DEVNULL,
                                   stdout=out, stderr=err,
                                   close_fds=True, start_new_session=False)
        while process.poll() is None:
            monitor.check()
            time.sleep(0.05)
        code = process.wait()
        out.flush(); os.fsync(out.fileno())
        err.flush(); os.fsync(err.fileno())
    monitor.check()
    if code != 0:
        raise CustodyFault("CHILD_NONZERO", "child rc=%d" % code)
    return code


def _deep_output_gate(report_path: Path, validation_path: Path,
                      state_path: Path, marker: dict, target: int,
                      validation_marker=None,
                      declared_state_path: Path | None = None) -> dict:
    report_raw = report_path.read_bytes()
    validation_raw = validation_path.read_bytes()
    report = json.loads(report_raw)
    validation = json.loads(validation_raw)
    payload, envelope_sha, payload_sha = _safe_state_envelope(state_path)
    registered_status = {"FINITE_SOURCE_LIFT_ONLY",
                         "SPECIFIC_BRANCH_OBSTRUCTED",
                         "FINITE_RAW_SOURCE_TEMPLATE_GATE_FAILED"}
    if report.get("status") not in registered_status or \
            payload.get("status") != report.get("status"):
        raise CustodyFault("OUTPUT_STATUS", "report/state status mismatch")
    if report.get("scope") != SCOPE or payload.get("scope") != SCOPE or \
            report.get("claims_certified") != CERTIFIED_CLAIM or \
            report.get("claims_forbidden") != FORBIDDEN_CLAIMS or \
            validation.get("scope") != SCOPE or \
            validation.get("claims_certified") != CERTIFIED_CLAIM or \
            validation.get("claims_forbidden") != FORBIDDEN_CLAIMS:
        raise CustodyFault("OUTPUT_CLAIMS", "scope/claim firewall drift")
    if report.get("requested_exponent") != target or \
            report.get("achieved_exponent") != payload.get("exponent"):
        raise CustodyFault("OUTPUT_TARGET", "report/state target mismatch")
    if report["status"] == "FINITE_SOURCE_LIFT_ONLY" and \
            payload["exponent"] != target:
        raise CustodyFault("OUTPUT_SHORT", "finite result short of target")
    if report.get("state_payload_sha256") != payload_sha or \
            report.get("history_sha256") != payload.get("history_sha256") or \
            report.get("necessary_template_relation_gate") != \
            payload.get("template_relation_gate") or \
            report.get("aws_lane") != marker:
        raise CustodyFault("OUTPUT_BINDING", "report/state/marker drift")
    declared_state_path = declared_state_path or state_path
    if report.get("state_path") != str(declared_state_path.resolve()) or \
            report.get("source_rows") != 184 or \
            report.get("essential_coordinates") != 182 or \
            report.get("jacobian_rank_mod_p") != 129 or \
            report.get("left_cokernel_dimension") != 55:
        raise CustodyFault("OUTPUT_SEMANTICS", "registered payload drift")
    if validation.get("status") != "SEMANTIC_STATE_CHAIN_VALID" or \
            validation.get("validated_exponent") != payload["exponent"] or \
            validation.get("authorized_target_exponent") != target or \
            validation.get("state_payload_sha256") != payload_sha or \
            validation.get("history_sha256") != payload["history_sha256"] or \
            (validation_marker is not None and
             validation.get("aws_lane") != validation_marker):
        raise CustodyFault("OUTPUT_REPLAY", "fresh semantic replay drift")
    return {"status": report["status"], "achieved_exponent": payload["exponent"],
            "state_envelope_sha256": envelope_sha,
            "state_payload_sha256": payload_sha,
            "history_sha256": payload["history_sha256"],
            "runner_report_sha256": sha256_bytes(report_raw),
            "validation_report_sha256": sha256_bytes(validation_raw)}


def run_registered_job(authorization_path) -> tuple[dict, int]:
    started = time.monotonic()
    deadline = started + TIMEOUT_SECONDS
    authorization = identity = live_tag = None
    auth_sha = None
    run_dir = None
    run_dir_owned = False
    monitor = None
    cgroup = None
    terminal_base = {"schema": TERMINAL_SCHEMA, "route": ROUTE,
                     "start_utc": utc_now(), "scope": SCOPE,
                     "claims_forbidden": FORBIDDEN_CLAIMS}
    try:
        reject_inherited_environment()
        invocation_id = registered_invocation_id()
        authorization, identity, live_tag, auth_sha = \
            load_live_authorization(authorization_path)
        bindings = authorization.get("bindings", {})
        target = bindings.get("target_exponent")
        job_id = bindings.get("job_id")
        if target not in TARGET_TAGS or not SAFE_ID_RE.fullmatch(str(job_id)) or \
                bindings.get("lane_tag") != TARGET_TAGS[target]:
            raise CustodyFault("AUTH_JOB", "job/target/lane binding invalid")
        if identity["instance_type"] != EXPECTED_INSTANCE_TYPE:
            raise CustodyFault("HOST_TYPE", "registered instance type required")
        if processes_for_uid(os.getuid()) != {os.getpid()}:
            raise CustodyFault("DEDICATED_UID",
                               "service UID is not exclusive to this job")
        terminal_base.update({"job_id": job_id, "target_exponent": target,
                              "lane_tag": bindings["lane_tag"],
                              "launch_authorization_sha256": auth_sha,
                              "systemd_invocation_id": invocation_id,
                              "host_identity": identity})
        paths = authorization.get("paths", {})
        raw_source_root = Path(paths["source_root"])
        raw_run_dir = Path(paths["run_dir"])
        if not raw_source_root.is_absolute() or raw_source_root.is_symlink() or \
                not raw_run_dir.is_absolute() or raw_run_dir.is_symlink() or \
                ".." in raw_run_dir.parts or \
                not SAFE_ID_RE.fullmatch(raw_run_dir.name):
            raise CustodyFault("PATH", "source/run roots must be absolute nonsymlinks")
        source_root = require_root_owned_nonwritable(
            raw_source_root, "sealed source root")
        run_parent = raw_run_dir.parent.resolve(strict=True)
        run_parent_stat = run_parent.stat()
        if Path(os.path.abspath(raw_run_dir.parent)) != run_parent or \
                run_parent_stat.st_uid != os.getuid() or \
                stat.S_IMODE(run_parent_stat.st_mode) != 0o700:
            raise CustodyFault(
                "RUN_PARENT",
                "run parent must be dedicated-service-UID-owned mode 0700")
        ancestor = run_parent.parent
        while True:
            ancestor_stat = ancestor.stat()
            if ancestor_stat.st_uid != 0 or ancestor_stat.st_mode & 0o022:
                raise CustodyFault("RUN_PARENT",
                                   "run parent has a mutable ancestor")
            if ancestor == ancestor.parent:
                break
            ancestor = ancestor.parent
        run_dir = run_parent / raw_run_dir.name
        if run_dir.exists():
            raise CustodyFault("RUN_DIR", "registered run directory exists")
        run_dir.mkdir(mode=0o700)
        fsync_directory(run_dir.parent)
        ownership = run_ownership_payload(
            run_dir, authorization, auth_sha, invocation_id)
        atomic_json(run_dir / "RUN_OWNERSHIP.json", ownership, 0o400,
                    replace=False)
        validate_run_ownership(run_dir, authorization, auth_sha,
                               invocation_id)
        run_dir_owned = True
        atomic_bytes(run_dir / "LAUNCH_AUTHORIZATION.snapshot.json",
                     immutable_authorization_path(authorization_path).read_bytes(),
                     0o400,
                     replace=False)
        if sha256_path(run_dir / "LAUNCH_AUTHORIZATION.snapshot.json") != auth_sha:
            raise CustodyFault("AUTH_SNAPSHOT", "authorization snapshot drift")
        lifecycle_gate(deadline)
        resource.setrlimit(resource.RLIMIT_AS,
                           (RSS_LIMIT_BYTES, RSS_LIMIT_BYTES))
        supervisor_path = Path(paths["supervisor_path"])
        if supervisor_path.resolve(strict=True) != Path(__file__).resolve() or \
                sha256_path(supervisor_path) != bindings["supervisor_sha256"]:
            raise CustodyFault("AUTH_SUPERVISOR", "supervisor path/hash drift")
        require_root_owned_nonwritable(supervisor_path, "supervisor source")
        cgroup = verify_cgroup_contract(
            authorization["systemd"], authorization["runtime"],
            supervisor_path, immutable_authorization_path(authorization_path),
            run_dir.parent)
        cgroup_dir = Path(cgroup["directory"])
        monitor = StickyMonitor(cgroup_dir, deadline,
                                run_dir / "RESOURCE_TELEMETRY.jsonl")
        monitor.start()
        monitor.check()
        runtime = runtime_receipt(authorization["runtime"])
        if authorization["runtime"]["receipt_sha256"] != \
                bindings["runtime_receipt_sha256"]:
            raise CustodyFault("AUTH_RUNTIME", "runtime receipt not bound")
        monitor.check()

        manifest_source = safe_relative_path(
            source_root, paths["payload_manifest"])
        prereg_source = safe_relative_path(source_root, paths["preregistration"])
        if sha256_path(manifest_source) != bindings["payload_manifest_sha256"] or \
                sha256_path(prereg_source) != bindings["preregistration_sha256"]:
            raise CustodyFault("AUTH_SOURCE_ROOT", "source roots drift")
        entries = parse_hash_manifest(source_root, manifest_source)
        verify_preregistration(prereg_source, entries,
                               bindings["payload_manifest_sha256"])
        for relative in entries:
            path = safe_relative_path(source_root, relative)
            require_root_owned_nonwritable(path, "sealed source member")
            parent = path.parent
            while parent != source_root:
                require_root_owned_nonwritable(
                    parent, "sealed source directory")
                parent = parent.parent
        require_root_owned_nonwritable(
            manifest_source, "payload manifest")
        require_root_owned_nonwritable(prereg_source, "preregistration")
        execution_root = run_dir / "execution"
        manifest_relative = paths["payload_manifest"]
        prereg_relative = paths["preregistration"]
        materialize_payload(source_root, execution_root, entries, {
            manifest_relative: bindings["payload_manifest_sha256"],
            prereg_relative: bindings["preregistration_sha256"],
        })
        monitor.check()
        # Rebind the manifest and preregistration to the immutable execution
        # copy; original repository bytes are never used again.
        manifest_path = execution_root / paths["payload_manifest"]
        prereg_path = execution_root / paths["preregistration"]
        if sha256_path(manifest_path) != bindings["payload_manifest_sha256"] or \
                sha256_path(prereg_path) != bindings["preregistration_sha256"]:
            raise CustodyFault("EXECUTION_ROOT", "copied roots drift")
        review_source = Path(paths["review_report_path"])
        if not review_source.is_absolute() or review_source.is_symlink() or \
                sha256_path(review_source.resolve(strict=True)) != \
                bindings["review_report_sha256"]:
            raise CustodyFault("REVIEW_BINDING", "review report byte drift")
        review_source = require_root_owned_nonwritable(
            review_source, "independent review report")
        review_snapshot = run_dir / "INDEPENDENT_REVIEW.snapshot.md"
        copy_verified_file(review_source, review_snapshot,
                           bindings["review_report_sha256"])
        archive_entries = dict(entries)
        archive_entries[manifest_relative] = bindings["payload_manifest_sha256"]
        archive_entries[prereg_relative] = bindings["preregistration_sha256"]
        source_members = [(relative, execution_root / relative)
                          for relative in sorted(archive_entries)]
        source_members.append(("external/INDEPENDENT_REVIEW.md",
                               review_snapshot))
        source_archive = run_dir / "SOURCE_INPUTS.tar.gz"
        source_archive_sha = deterministic_tar(source_archive, source_members)
        source_inventory = {
            relative: {"sha256": digest,
                       "bytes": (execution_root / relative).stat().st_size}
            for relative, digest in archive_entries.items()}
        source_inventory["external/INDEPENDENT_REVIEW.md"] = {
            "sha256": bindings["review_report_sha256"],
            "bytes": review_snapshot.stat().st_size,
        }
        replay_archive(source_archive, source_inventory)
        if source_archive_sha != bindings["source_archive_sha256"]:
            raise CustodyFault("SOURCE_ARCHIVE", "registered archive drift")
        monitor.check()

        private_dir = run_dir / "private"
        private_dir.mkdir(mode=0o700)
        d21_source = execution_root / "directionb_tails_D21.pkl"
        d21_private = private_dir / "directionb_tails_D21.pkl"
        copy_verified_file(d21_source, d21_private, EXPECTED_D21_SHA256)
        core23 = execution_root / "cases/directionb_core23_p105337.ms"
        if sha256_path(core23) != EXPECTED_CORE23_SHA256:
            raise CustodyFault("CORE23", "core23 missing from execution root")

        state_input = paths.get("state_input_path")
        raw_state_output = Path(paths["state_output_path"])
        state_output = raw_state_output.resolve()
        if not raw_state_output.is_absolute() or raw_state_output.is_symlink() or \
                ".." in raw_state_output.parts or state_output.parent != run_dir or \
                state_output.name != "STATE.p%d.json" % target:
            raise CustodyFault("STATE_OUTPUT", "state path is not canonical")
        if state_output.exists():
            raise CustodyFault("STATE_OUTPUT", "state output must be fresh")
        state_output.parent.mkdir(parents=True, exist_ok=True)
        input_snapshot = None
        provenance = bindings.get("target16_provenance")
        if target == 16:
            if state_input is not None or provenance is not None or any(
                    paths[key] is not None for key in
                    ("target16_terminal_path", "target16_manifest_path",
                     "target16_archive_path")):
                raise CustodyFault("TARGET16", "target16 has continuation input")
        else:
            if state_input is None or not isinstance(provenance, dict):
                raise CustodyFault("TARGET64", "target16 provenance required")
            _handoff_path, handoff_terminal = validate_target16_handoff(
                paths, provenance, run_dir)
            raw_source_state = Path(state_input)
            if not raw_source_state.is_absolute() or raw_source_state.is_symlink():
                raise CustodyFault("TARGET64", "state input path is unsafe")
            source_state = raw_source_state.resolve(strict=True)
            input_snapshot = run_dir / "TARGET16_INPUT_STATE.snapshot.json"
            copy_verified_file(source_state, input_snapshot,
                               provenance["state_envelope_sha256"])
            payload, envelope_sha, payload_sha = _safe_state_envelope(
                input_snapshot)
            checks = {
                "state_envelope_sha256": envelope_sha,
                "state_payload_sha256": payload_sha,
                "history_sha256": payload.get("history_sha256"),
                "achieved_exponent": payload.get("exponent"),
            }
            for key, value in checks.items():
                if provenance.get(key) != value:
                    raise CustodyFault("TARGET64", "%s provenance drift" % key)
            if handoff_terminal.get("output_binding", {}).get(
                    "state_envelope_sha256") != envelope_sha or \
                    handoff_terminal.get("output_binding", {}).get(
                        "state_payload_sha256") != payload_sha or \
                    handoff_terminal.get("output_binding", {}).get(
                        "history_sha256") != payload.get("history_sha256"):
                raise CustodyFault("TARGET64", "state is not terminal handoff")
            copy_verified_file(input_snapshot, state_output,
                               provenance["state_envelope_sha256"])
            os.chmod(state_output, 0o600)
            if sha256_path(input_snapshot) != \
                    provenance["state_envelope_sha256"] or \
                    sha256_path(state_output) != \
                    provenance["state_envelope_sha256"]:
                raise CustodyFault("TARGET64", "state snapshot/copy drift")

        report_path = run_dir / "runner_report.json"
        runner = execution_root / \
            "cases/d43_source_high_hensel_v3_20260828/runner_v3.py"
        base_runner = execution_root / "cases/d43_source_high_hensel.py"
        worker = execution_root / \
            "cases/d43_source_high_hensel_v3_20260828/aws_worker_v3.sh"
        expected_worker_relative = \
            "cases/d43_source_high_hensel_v3_20260828/aws_worker_v3.sh"
        if paths["worker"] != expected_worker_relative or \
                worker != safe_relative_path(execution_root, paths["worker"]):
            raise CustodyFault("AUTH_COMPONENT", "worker path binding drift")
        if (sha256_path(runner) != bindings["runner_sha256"] or
                sha256_path(base_runner) != bindings["base_runner_sha256"] or
                sha256_path(worker) != bindings["worker_sha256"] or
                sha256_path(__file__) != bindings["supervisor_sha256"]):
            raise CustodyFault("AUTH_COMPONENT", "component byte drift")
        (run_dir / "home").mkdir(mode=0o700)
        marker = _marker_payload(
            authorization, identity, live_tag, auth_sha, execution_root,
            source_archive, source_archive_sha, authorization["runtime"], run_dir,
            state_output, report_path, d21_private, core23, os.getpid())
        marker_path = run_dir / "AWS_AUTHORIZATION.json"
        write_envelope(marker_path, marker)
        marker_sha = sha256_path(marker_path)
        environment = materialize_child_environment(
            marker["runtime_environment"], marker_path, marker_sha)
        if sha256_json(marker["runtime_environment"]) != \
                bindings["runtime_environment_sha256"]:
            raise CustodyFault("AUTH_ENVIRONMENT",
                               "normalized child environment digest drift")
        monitor.check()
        python_path = authorization["runtime"]["python_path"]
        argv = [authorization["runtime"]["bash_path"],
                "--noprofile", "--norc", str(worker),
                python_path, str(runner), str(execution_root), str(target),
                str(state_output), str(report_path),
                str(execution_root / "cases/d43_full_certificate_p105337.json"),
                str(execution_root / "cases/d43_char0_lift_p105337.json"),
                str(d21_private), str(core23)]
        _run_child(argv, environment, monitor, run_dir / "runner.stdout",
                   run_dir / "runner.stderr")
        lifecycle_gate(deadline, cgroup_dir, {os.getpid()})

        validation_path = run_dir / "validation_report.json"
        validation_marker = dict(marker)
        validation_marker["report_path"] = str(validation_path)
        validation_marker_path = run_dir / "AWS_AUTHORIZATION.validation.json"
        write_envelope(validation_marker_path, validation_marker)
        validation_env = dict(environment)
        validation_env["JC2_D43_HENSEL_AWS_AUTH"] = str(validation_marker_path)
        validation_env["JC2_D43_HENSEL_AWS_AUTH_SHA256"] = sha256_path(
            validation_marker_path)
        validation_argv = [
            python_path, "-I", "-B", str(runner),
            "--target-exponent", str(target), "--state", str(state_output),
            "--report", str(validation_path), "--certificate",
            str(execution_root / "cases/d43_full_certificate_p105337.json"),
            "--p2-reference",
            str(execution_root / "cases/d43_char0_lift_p105337.json"),
            "--d21-private", str(d21_private), "--core23", str(core23),
            "--execution-root", str(execution_root), "--validate-state-only"]
        _run_child(validation_argv, validation_env, monitor,
                   run_dir / "validation.stdout",
                   run_dir / "validation.stderr")
        lifecycle_gate(deadline, cgroup_dir, {os.getpid()})
        runner_report_snapshot = run_dir / "RUNNER_REPORT.snapshot.json"
        validation_report_snapshot = run_dir / \
            "VALIDATION_REPORT.snapshot.json"
        final_state_snapshot = run_dir / "FINAL_STATE.snapshot.json"
        report_snapshot_sha = snapshot_untrusted_file(
            report_path, runner_report_snapshot)
        validation_snapshot_sha = snapshot_untrusted_file(
            validation_path, validation_report_snapshot)
        state_snapshot_sha = snapshot_untrusted_file(
            state_output, final_state_snapshot)
        output = _deep_output_gate(
            runner_report_snapshot, validation_report_snapshot,
            final_state_snapshot, marker, target, validation_marker,
            declared_state_path=state_output)
        if output["runner_report_sha256"] != report_snapshot_sha or \
                output["validation_report_sha256"] != \
                    validation_snapshot_sha or \
                output["state_envelope_sha256"] != state_snapshot_sha:
            raise CustodyFault("OUTPUT_SNAPSHOT",
                               "semantic output/snapshot binding drift")
        for original in (report_path, validation_path, state_output):
            os.chmod(original, 0o400)
        monitor.check()
        monitor.stop()
        monitor_stats = {"samples": monitor.samples,
                         "peak_memory_bytes": monitor.peak,
                         "pid_start_time_registry": dict(monitor.registry)}
        monitor = None
        membership = lifecycle_gate(deadline, cgroup_dir, {os.getpid()})
        # Sampling has stopped so its telemetry is immutable.  Synchronous
        # gates now cover every packaging step; the kernel/systemd hard caps
        # remain active through terminal promotion.
        def terminal_gate():
            lifecycle_gate(deadline, cgroup_dir, {os.getpid()})
            validate_run_ownership(run_dir, authorization, auth_sha,
                                   invocation_id)
            revalidate_live_authorization(
                authorization_path, auth_sha, identity, live_tag)
            expected_snapshots = {
                runner_report_snapshot: output["runner_report_sha256"],
                report_path: output["runner_report_sha256"],
                validation_report_snapshot:
                    output["validation_report_sha256"],
                validation_path: output["validation_report_sha256"],
                final_state_snapshot: output["state_envelope_sha256"],
                state_output: output["state_envelope_sha256"],
            }
            for snapshot, expected in expected_snapshots.items():
                if snapshot.is_symlink() or sha256_path(snapshot) != expected:
                    raise CustodyFault("OUTPUT_SNAPSHOT",
                                       "frozen semantic snapshot drift")

        terminal_core = dict(terminal_base)
        terminal_core.update({
            "status": "FINITE_SOURCE_RESULT_CUSTODY_PASS",
            "mathematical_outcome": output["status"],
            "achieved_exponent": output["achieved_exponent"],
            "end_utc": utc_now(), "output_binding": output,
            "source_archive_sha256": source_archive_sha,
            "runtime_receipt_sha256": authorization["runtime"][
                "receipt_sha256"],
            "runtime_environment_sha256": marker[
                "runtime_environment_sha256"],
            "job_identity_sha256": marker["job_identity_sha256"],
            "cgroup_contract": cgroup,
            "cgroup_final_snapshot": membership,
            "resource_monitor": monitor_stats,
            "whole_job_elapsed_seconds": time.monotonic() - started,
            "target16_input_snapshot_sha256":
                (provenance["state_envelope_sha256"]
                 if input_snapshot else None),
        })
        terminal = publish_terminal_bundle(run_dir, terminal_core,
                                           gate=terminal_gate)
        return terminal, 0
    except Exception as caught:
        error = caught if isinstance(caught, CustodyFault) else \
            CustodyFault("SUPERVISOR_EXCEPTION", repr(caught))
        if monitor is not None:
            try:
                monitor.stop()
            except Exception as monitor_error:
                if error.code == "SUPERVISOR_EXCEPTION":
                    error = CustodyFault("MONITOR_DIED", repr(monitor_error))
        containment = None
        if cgroup is not None:
            try:
                containment = terminate_cgroup_members(
                    Path(cgroup["directory"]), {os.getpid()})
            except Exception as terminate_error:
                containment = {"cleanup_fault": repr(terminate_error)}
        if not run_dir_owned:
            terminal = dict(terminal_base)
            terminal.update({"status": "NO_VERDICT_BEFORE_REGISTERED_RUN_DIR",
                             "fault_code": error.code,
                             "fault_detail": error.detail,
                             "mathematical_outcome": None,
                             "end_utc": utc_now()})
            if authorization is not None and auth_sha is not None:
                try:
                    terminal = publish_pre_run_rejection(
                        authorization, auth_sha, terminal_base, error)
                except Exception as durable_error:
                    terminal["durable_rejection_fault"] = repr(durable_error)
            return terminal, 125
        # Preserve the last committed durable state on every fault.
        try:
            candidate = Path(authorization["paths"]["state_output_path"])
            if candidate.is_file():
                snapshot = run_dir / "LAST_COMMITTED_STATE_ON_FAULT.snapshot.json"
                if not snapshot.exists():
                    atomic_bytes(snapshot, candidate.read_bytes(), 0o400,
                                 replace=False)
        except Exception:
            pass
        terminal_core = dict(terminal_base)
        terminal_core.update({
            "status": "NO_VERDICT_CUSTODY_FAULT",
            "fault_code": error.code, "fault_detail": error.detail,
            "mathematical_outcome": None, "containment": containment,
            "end_utc": utc_now(),
            "whole_job_elapsed_seconds": time.monotonic() - started,
        })
        try:
            terminal = publish_terminal_bundle(run_dir, terminal_core)
        except Exception as bundle_error:
            terminal = emergency_no_verdict(run_dir, terminal_core,
                                             bundle_error)
        return terminal, 125


def poststop_terminalize(authorization_path) -> tuple[dict, int]:
    """ExecStopPost fail-safe for SIGKILL/OOM/timeout of the main process."""
    environment_fault = None
    try:
        reject_inherited_environment()
        invocation_id = registered_invocation_id()
    except Exception as error:
        environment_fault = repr(error)
        invocation_id = None
    live_verified = True
    live_fault = None
    try:
        if environment_fault is not None:
            raise CustodyFault("POSTSTOP_ENVIRONMENT", environment_fault)
        authorization, identity, _tag, auth_sha = load_live_authorization(
            authorization_path)
    except Exception as live_error:
        # A custody outage must not prevent a negative record.  The fallback
        # trusts only the immutable root-owned authorization path embedded in
        # the root-owned unit and can never emit or preserve a positive result.
        live_verified = False
        live_fault = repr(live_error)
        auth_path = immutable_authorization_path(authorization_path)
        raw = auth_path.read_bytes()
        auth_sha = sha256_bytes(raw)
        authorization = json.loads(raw)
        validate_authorization_shape(authorization)
        if authorization.get("schema") != AUTH_SCHEMA or \
                authorization.get("status") != \
                "COORDINATOR_AUTHORIZED_AFTER_INDEPENDENT_REVIEW_PASS" or \
                authorization.get("review_verdict") != "PASS":
            raise CustodyFault("POSTSTOP_AUTH",
                               "immutable fallback authorization inactive")
        identity = None
    raw_run_dir = Path(authorization["paths"]["run_dir"])
    if not raw_run_dir.is_absolute() or raw_run_dir.is_symlink():
        raise CustodyFault("POSTSTOP_PATH", "registered run path is unsafe")
    run_dir = raw_run_dir.resolve()
    base = {
        "schema": TERMINAL_SCHEMA, "route": ROUTE,
        "start_utc": utc_now(), "scope": SCOPE,
        "claims_forbidden": FORBIDDEN_CLAIMS,
        "job_id": authorization["bindings"]["job_id"],
        "target_exponent": authorization["bindings"]["target_exponent"],
        "lane_tag": authorization["bindings"]["lane_tag"],
        "launch_authorization_sha256": auth_sha,
        "systemd_invocation_id": invocation_id,
        "host_identity": identity,
    }

    def collision_rejection(code, detail):
        error = CustodyFault(code, detail)
        terminal = publish_pre_run_rejection(
            authorization, auth_sha, base, error)
        return terminal, 125

    # Never mkdir/adopt a path here.  Only the main supervisor may atomically
    # create it and install the same-auth/job/inode ownership sentinel.
    if invocation_id is None:
        return collision_rejection(
            "POSTSTOP_INVOCATION",
            "systemd invocation identity is unavailable")
    if not run_dir.exists():
        return collision_rejection(
            "POSTSTOP_NO_OWNED_RUN",
            "main supervisor never registered its run directory")
    try:
        validate_run_ownership(run_dir, authorization, auth_sha,
                               invocation_id)
    except Exception as error:
        return collision_rejection("POSTSTOP_RUN_OWNERSHIP", repr(error))

    authority = run_dir / "TERMINAL.json"
    if authority.is_file():
        terminal = json.loads(authority.read_text())
        try:
            validate_existing_terminal(
                run_dir, terminal, authorization, auth_sha, live_verified,
                invocation_id)
        except Exception as error:
            return collision_rejection("POSTSTOP_TERMINAL", repr(error))
        return terminal, 0
    core = {
        **base,
        "status": ("NO_VERDICT_SYSTEMD_POSTSTOP" if live_verified else
                   "NO_VERDICT_SYSTEMD_POSTSTOP_LIVE_AUTH_UNAVAILABLE"),
        "fault_code": ("SYSTEMD_POSTSTOP" if live_verified else
                       "SYSTEMD_POSTSTOP_LIVE_AUTH_UNAVAILABLE"),
        "fault_detail": ("main supervisor did not publish a terminal authority"
                         if live_verified else live_fault),
        "service_result": os.environ.get("SERVICE_RESULT"),
        "exit_code": os.environ.get("EXIT_CODE"),
        "exit_status": os.environ.get("EXIT_STATUS"),
        "mathematical_outcome": None,
        "end_utc": utc_now(), "claims_forbidden": FORBIDDEN_CLAIMS,
    }
    state = Path(authorization["paths"]["state_output_path"])
    if state.parent.resolve() == run_dir and state.is_file() and not (
            run_dir / "LAST_COMMITTED_STATE_ON_FAULT.snapshot.json").exists():
        atomic_bytes(run_dir / "LAST_COMMITTED_STATE_ON_FAULT.snapshot.json",
                     state.read_bytes(), 0o400, replace=False)
    try:
        terminal = publish_terminal_bundle(run_dir, core)
    except Exception as error:
        terminal = emergency_no_verdict(run_dir, core, error)
    return terminal, 125


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--authorization", required=True)
    parser.add_argument("--terminalize", action="store_true")
    return parser


def main():
    arguments = build_parser().parse_args()
    if arguments.terminalize:
        terminal, code = poststop_terminalize(arguments.authorization)
    else:
        terminal, code = run_registered_job(arguments.authorization)
    print(json.dumps(terminal, indent=1, sort_keys=True))
    raise SystemExit(code)


if __name__ == "__main__":
    main()
