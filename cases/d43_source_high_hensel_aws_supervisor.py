#!/usr/bin/env python3
"""Evidence-grade AWS custody supervisor for the D43 source Hensel lane.

This is deliberately route-specific.  It accepts only targets 16 and 64,
checks exact sealed inputs and host identity, authorizes the runner with a
content-addressed parent-bound marker, monitors the single payload process
group at 10 Hz, and emits NO_VERDICT on every custody failure.

It never interprets a finite source result, including one passing the
necessary E/W gate, as template-branch evidence or as an assembled,
indefinite, formal-smooth, characteristic-zero, or JC2 result.
"""

from __future__ import annotations

import argparse
import ctypes
import fcntl
import gzip
import hashlib
import io
import json
import os
import platform
import re
import shutil
import signal
import socket
import subprocess
import sys
import tarfile
import time
import urllib.request
from pathlib import Path


AUTH_SCHEMA = "d43-pristine-source-high-hensel-aws-auth-v1"
TERMINAL_SCHEMA = "d43-pristine-source-high-hensel-aws-terminal-v1"
ROUTE = "D43-PRISTINE-SOURCE-HIGH-HENSEL-R1"
STATE_SCHEMA = "d43-pristine-source-high-hensel-state-v2"
TARGET_TAGS = {
    16: ROUTE + "-N16",
    64: ROUTE + "-N64",
}
SCOPE = "residue-A, B=84, a00pp, finite raw 184-row Euler/J-source truncation only"
CERTIFIED_CLAIM = (
    "at every successful committed digit, one finite congruence point of "
    "the declared raw 184-row Euler/J-source truncation satisfying the "
    "necessary E=0 and W1,W2 unit gates")
EXACT_RELATIONS_REPLAYED = [
    "184 raw Euler/J-source rows",
    "Phi42(zeta)=0, r3^2=3, A1^3=3+r3, A2^3=3-r3, 2h^2=3",
    "necessary E=(9+5r3)A1W1^4+(9-5r3)A2W2^4=0 and W1,W2 unit gates at every committed state",
    "two corrected-243 E5 rows with a common deterministic HM witness and the cube-form E6 row with a nonzero deterministic s1F witness",
    "HW1=h*W1 and HW2=h*W2 inside every source evaluation",
    "literal uf30=0 and the named finite source completion encoded by the evaluator",
]
UPSTREAM_NOT_REPLAYED = [
    "34 parked D21/D23/D25 constraints",
    "W1*uW1-1 and W2*uW2-1 inverse-chart rows",
    "template and low-order reconstruction equations",
    "source-to-NF and reducer membership identities",
]
FORBIDDEN_CLAIMS = [
    "assembled 218-row p-adic point",
    "parked/source presentation equivalence",
    "full residue-A/template/D25 p-adic point or upstream exact-equation lift",
    "D43 template-branch evidence or survival from the raw-source lift",
    "indefinite source solvability or formal smoothness",
    "Z_p point",
    "characteristic-zero point",
    "formal germ",
    "ambient polynomial Keller map",
    "JC2 counterexample",
]
TIMEOUT_SECONDS = 1200
RSS_LIMIT_BYTES = 2 * 1024 ** 3
SAMPLE_INTERVAL_SECONDS = 0.1
EXPECTED_INSTANCE_TYPE = "c7i.xlarge"
AUTHORIZED_PREREG_STATUS = \
    "PREREGISTERED_HOSTILE_REREVIEW_PASS_AWS_AUTHORIZED"
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
SAFE_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$")


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


def fsync_directory(path) -> None:
    descriptor = os.open(os.path.abspath(path), os.O_RDONLY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def atomic_bytes(path, content: bytes, mode=0o600) -> None:
    path = os.path.abspath(path)
    directory = os.path.dirname(path)
    os.makedirs(directory, exist_ok=True)
    temporary = os.path.join(directory, ".%s.%d.tmp" %
                             (os.path.basename(path), os.getpid()))
    descriptor = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL,
                         mode)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
        fsync_directory(directory)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def atomic_json(path, value) -> None:
    atomic_bytes(path, (json.dumps(value, indent=1, sort_keys=True) +
                        "\n").encode())


def write_envelope(path, payload) -> str:
    digest = sha256_json(payload)
    atomic_json(path, {"payload": payload, "payload_sha256": digest})
    return digest


def utc_now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def safe_relative_path(root: Path, value: str) -> Path:
    candidate = Path(value)
    if candidate.is_absolute() or ".." in candidate.parts:
        raise CustodyFault("MANIFEST_PATH", "unsafe manifest path %r" % value)
    unresolved = root / candidate
    if unresolved.is_symlink():
        raise CustodyFault("MANIFEST_PATH", "manifest member is a symlink: %s" % value)
    resolved = unresolved.resolve()
    try:
        resolved.relative_to(root.resolve())
    except ValueError as error:
        raise CustodyFault("MANIFEST_PATH", "manifest path escapes root") from error
    if not resolved.is_file():
        raise CustodyFault("MANIFEST_PATH", "manifest member is not a regular file: %s" % value)
    return resolved


def parse_hash_manifest(root: Path, manifest_path: Path) -> dict[str, str]:
    entries = {}
    for number, raw in enumerate(manifest_path.read_text().splitlines(), 1):
        if not raw:
            continue
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", raw)
        if not match:
            raise CustodyFault("MANIFEST_FORMAT",
                               "bad line %d in payload manifest" % number)
        digest, relative = match.groups()
        if relative in entries:
            raise CustodyFault("MANIFEST_DUPLICATE", relative)
        path = safe_relative_path(root, relative)
        observed = sha256_path(path)
        if observed != digest:
            raise CustodyFault("INPUT_HASH", "%s: %s != %s" %
                               (relative, observed, digest))
        entries[relative] = digest
    if not entries:
        raise CustodyFault("MANIFEST_EMPTY", "payload manifest is empty")
    return entries


def verify_preregistration(root: Path, prereg_path: Path,
                           manifest_entries: dict[str, str], target: int,
                           lane_tag: str,
                           manifest_sha256: str) -> dict:
    prereg = json.loads(prereg_path.read_text())
    if prereg.get("status") != AUTHORIZED_PREREG_STATUS:
        raise CustodyFault(
            "PREREG_NOT_AUTHORIZED",
            "independent hostile rereview has not authorized AWS launch")
    exact_contract = {
        "protocol": ROUTE,
        "state_schema": STATE_SCHEMA,
        "scope": SCOPE,
        "certified_claim": CERTIFIED_CLAIM,
        "exact_relations_replayed": EXACT_RELATIONS_REPLAYED,
        "upstream_not_replayed": UPSTREAM_NOT_REPLAYED,
        "forbidden_claims": FORBIDDEN_CLAIMS,
    }
    for key, value in exact_contract.items():
        if prereg.get(key) != value:
            raise CustodyFault("PREREG_CONTRACT", "%s drift" % key)
    route = prereg.get("aws_route", {})
    exact = {
        "schema": "D43-HIGH-HENSEL-AWS-ROUTE-V1",
        "timeout_seconds": TIMEOUT_SECONDS,
        "rss_limit_bytes": RSS_LIMIT_BYTES,
        "swap_bytes_allowed": 0,
        "sample_interval_seconds": SAMPLE_INTERVAL_SECONDS,
        "instance_type": EXPECTED_INSTANCE_TYPE,
        "target_tags": {"16": TARGET_TAGS[16], "64": TARGET_TAGS[64]},
    }
    for key, value in exact.items():
        if route.get(key) != value:
            raise CustodyFault("PREREG_ROUTE", "%s drift" % key)
    if not SHA_RE.fullmatch(str(manifest_sha256)) or \
            route.get("payload_manifest_sha256") != manifest_sha256:
        raise CustodyFault("PREREG_ROUTE",
                           "payload_manifest_sha256 drift")
    if lane_tag != TARGET_TAGS[target]:
        raise CustodyFault("LANE_TAG", "target/tag mismatch")
    registered_inputs = prereg.get("inputs")
    if not isinstance(registered_inputs, dict) or not registered_inputs:
        raise CustodyFault("PREREG_INPUTS", "missing preregistered inputs")
    for relative, digest in registered_inputs.items():
        if not SHA_RE.fullmatch(str(digest)):
            raise CustodyFault("PREREG_INPUTS", "malformed hash for %s" % relative)
        path = safe_relative_path(root, relative)
        if sha256_path(path) != digest:
            raise CustodyFault("PREREG_INPUT_HASH", relative)
        if manifest_entries.get(relative) != digest:
            raise CustodyFault("MANIFEST_COVERAGE", relative)
    if set(route.get("payload_files", [])) != set(manifest_entries):
        raise CustodyFault("MANIFEST_COVERAGE", "payload file set drift")
    if prereg.get("forbidden_claims") != FORBIDDEN_CLAIMS:
        raise CustodyFault("CLAIMS_FIREWALL", "prereg forbidden claims drift")
    return prereg


def ec2_identity(timeout=2.0) -> dict:
    if platform.system() != "Linux":
        raise CustodyFault("HOST_OS", "Linux is required")
    try:
        vendor = Path("/sys/class/dmi/id/sys_vendor").read_text().strip()
    except OSError as error:
        raise CustodyFault("HOST_DMI", "cannot read DMI vendor") from error
    if vendor != "Amazon EC2":
        raise CustodyFault("HOST_DMI", "Amazon EC2 vendor required")
    try:
        token_request = urllib.request.Request(
            "http://169.254.169.254/latest/api/token", method="PUT",
            headers={"X-aws-ec2-metadata-token-ttl-seconds": "60"})
        with urllib.request.urlopen(token_request, timeout=timeout) as response:
            token = response.read().decode()
        document_request = urllib.request.Request(
            "http://169.254.169.254/latest/dynamic/instance-identity/document",
            headers={"X-aws-ec2-metadata-token": token})
        with urllib.request.urlopen(document_request, timeout=timeout) as response:
            document = json.loads(response.read())
    except Exception as error:
        raise CustodyFault("HOST_IMDS", "IMDSv2 identity unavailable") from error
    return {
        "vendor": vendor,
        "hostname": socket.gethostname(),
        "instance_id": document.get("instanceId"),
        "instance_type": document.get("instanceType"),
        "region": document.get("region"),
        "availability_zone": document.get("availabilityZone"),
        "account_id": document.get("accountId"),
        "private_ip": document.get("privateIp"),
    }


def meminfo_swap_used_bytes(path="/proc/meminfo") -> int:
    values = {}
    for line in Path(path).read_text().splitlines():
        parts = line.split()
        if len(parts) >= 2 and parts[0].rstrip(":") in ("SwapTotal", "SwapFree"):
            values[parts[0].rstrip(":")] = int(parts[1]) * 1024
    if set(values) != {"SwapTotal", "SwapFree"}:
        raise CustodyFault("SWAP_TELEMETRY", "SwapTotal/SwapFree unavailable")
    return values["SwapTotal"] - values["SwapFree"]


def proc_table(proc_root=Path("/proc")) -> dict[int, dict]:
    table = {}
    for entry in proc_root.iterdir():
        if not entry.name.isdigit():
            continue
        pid = int(entry.name)
        try:
            raw = (entry / "stat").read_text()
            tail = raw[raw.rfind(")") + 2:].split()
            status = {}
            for line in (entry / "status").read_text().splitlines():
                if line.startswith(("VmRSS:", "VmSwap:")):
                    parts = line.split()
                    status[parts[0].rstrip(":")] = int(parts[1]) * 1024
            table[pid] = {"state": tail[0], "ppid": int(tail[1]),
                          "pgrp": int(tail[2]),
                          "rss": status.get("VmRSS", 0),
                          "swap": status.get("VmSwap", 0)}
        except (FileNotFoundError, ProcessLookupError, PermissionError,
                ValueError, IndexError):
            continue
    return table


def process_topology(table: dict[int, dict], root_pid: int) -> dict:
    group = sorted(pid for pid, item in table.items()
                   if item["pgrp"] == root_pid)
    descendants = set()
    frontier = {root_pid}
    while frontier:
        parent = frontier.pop()
        children = {pid for pid, item in table.items()
                    if item["ppid"] == parent and pid not in descendants}
        descendants.update(children)
        frontier.update(children)
    escaped = sorted(pid for pid in descendants
                     if table.get(pid, {}).get("pgrp") != root_pid)
    unexpected_group = sorted(set(group) - ({root_pid} | descendants))
    return {
        "group_pids": group,
        "descendant_pids": sorted(descendants),
        "escaped_descendant_pids": escaped,
        "unexpected_group_pids": unexpected_group,
        "rss_bytes": sum(table[pid]["rss"] for pid in group),
        "process_swap_bytes": sum(table[pid]["swap"] for pid in group),
    }


def process_sample(root_pid: int) -> dict:
    result = process_topology(proc_table(), root_pid)
    result["global_swap_used_bytes"] = meminfo_swap_used_bytes()
    return result


def terminate_contained(process: subprocess.Popen, known_pids: set[int],
                        grace_seconds=3.0) -> dict:
    signals_sent = []
    if process.poll() is None:
        try:
            os.killpg(process.pid, signal.SIGTERM)
            signals_sent.append("SIGTERM_PROCESS_GROUP")
        except ProcessLookupError:
            pass
    deadline = time.monotonic() + grace_seconds
    while process.poll() is None and time.monotonic() < deadline:
        time.sleep(0.05)
    if process.poll() is None:
        try:
            os.killpg(process.pid, signal.SIGKILL)
            signals_sent.append("SIGKILL_PROCESS_GROUP")
        except ProcessLookupError:
            pass
    for pid in sorted(known_pids):
        if pid == process.pid:
            continue
        try:
            os.kill(pid, signal.SIGKILL)
            signals_sent.append("SIGKILL_PID_%d" % pid)
        except ProcessLookupError:
            pass
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        signals_sent.append("WAIT_TIMEOUT")
    remaining = process_topology(proc_table(), process.pid)
    return {"signals_sent": signals_sent,
            "remaining_group_pids": remaining["group_pids"],
            "remaining_descendant_pids": remaining["descendant_pids"]}


def deterministic_tar(path: Path, root: Path, members: list[tuple[str, Path]]) -> str:
    buffer = io.BytesIO()
    with tarfile.open(fileobj=buffer, mode="w") as archive:
        for arcname, source in sorted(members):
            data = source.read_bytes()
            info = tarfile.TarInfo(arcname)
            info.size = len(data)
            info.mtime = 0
            info.uid = info.gid = 0
            info.uname = info.gname = ""
            info.mode = 0o444
            archive.addfile(info, io.BytesIO(data))
    compressed = io.BytesIO()
    with gzip.GzipFile(filename="", mode="wb", fileobj=compressed,
                       mtime=0) as output:
        output.write(buffer.getvalue())
    atomic_bytes(path, compressed.getvalue(), 0o400)
    return sha256_path(path)


def terminal_bundle(run_dir: Path, terminal: dict) -> dict:
    terminal_path = run_dir / "terminal.json"
    atomic_json(terminal_path, terminal)
    candidates = [path for path in run_dir.iterdir()
                  if path.is_file() and path.name not in {
                      "terminal_manifest.sha256", "evidence_archive.tar.gz",
                      "evidence_archive.tar.gz.sha256"}]
    lines = ["%s  %s" % (sha256_path(path), path.name)
             for path in sorted(candidates)]
    manifest_path = run_dir / "terminal_manifest.sha256"
    atomic_bytes(manifest_path, ("\n".join(lines) + "\n").encode(), 0o400)
    members = [(path.name, path) for path in candidates] + [
        (manifest_path.name, manifest_path)]
    archive_path = run_dir / "evidence_archive.tar.gz"
    archive_sha = deterministic_tar(archive_path, run_dir, members)
    atomic_bytes(run_dir / "evidence_archive.tar.gz.sha256",
                 ("%s  %s\n" % (archive_sha, archive_path.name)).encode(),
                 0o400)
    return {"terminal_sha256": sha256_path(terminal_path),
            "terminal_manifest_sha256": sha256_path(manifest_path),
            "archive_sha256": archive_sha}


def set_subreaper() -> None:
    if ctypes.CDLL(None).prctl(36, 1, 0, 0, 0) != 0:  # PR_SET_CHILD_SUBREAPER
        raise CustodyFault("CONTAINMENT", "cannot become child subreaper")


def run_supervised(arguments) -> tuple[dict, int]:
    root = Path(arguments.root).resolve()
    run_dir = Path(arguments.run_dir).resolve()
    if not SAFE_ID_RE.fullmatch(arguments.job_id):
        raise CustodyFault("JOB_ID", "unsafe job id")
    if arguments.target_exponent not in TARGET_TAGS:
        raise CustodyFault("TARGET", "only targets 16 and 64 are registered")
    if arguments.lane_tag != TARGET_TAGS[arguments.target_exponent]:
        raise CustodyFault("LANE_TAG", "lane tag is not exact")
    if run_dir.exists():
        raise CustodyFault("RUN_DIR", "run directory must not already exist")
    run_dir.mkdir(parents=True, mode=0o700)
    fsync_directory(run_dir.parent)

    start_utc = utc_now()
    terminal_base = {"schema": TERMINAL_SCHEMA, "route": ROUTE,
                     "job_id": arguments.job_id,
                     "start_utc": start_utc,
                     "target_exponent": arguments.target_exponent,
                     "lane_tag": arguments.lane_tag,
                     "scope": SCOPE,
                     "claims_forbidden": FORBIDDEN_CLAIMS}
    process = None
    known_pids = set()
    stdout_handle = stderr_handle = telemetry_handle = None
    state_lock_handle = None
    old_handlers = {}
    try:
        def interrupted(signum, _frame):
            raise CustodyFault("SUPERVISOR_SIGNAL",
                               "received signal %d" % signum)
        for signum in (signal.SIGINT, signal.SIGTERM, signal.SIGHUP):
            old_handlers[signum] = signal.signal(signum, interrupted)
        if not root.is_dir():
            raise CustodyFault("ROOT", "repository root missing")
        identity = ec2_identity()
        if identity["hostname"] != arguments.expected_hostname:
            raise CustodyFault("HOSTNAME", "hostname mismatch")
        if identity["instance_id"] != arguments.expected_instance_id:
            raise CustodyFault("INSTANCE_ID", "instance-id mismatch")
        if identity["instance_type"] != EXPECTED_INSTANCE_TYPE or \
                identity["instance_type"] != arguments.expected_instance_type:
            raise CustodyFault("INSTANCE_TYPE", "instance type mismatch")
        if meminfo_swap_used_bytes() != 0:
            raise CustodyFault("SWAP_PREFLIGHT", "global swap use is nonzero")

        manifest_path = Path(arguments.payload_manifest).resolve()
        prereg_path = Path(arguments.preregistration).resolve()
        if sha256_path(manifest_path) != arguments.expected_manifest_sha256:
            raise CustodyFault("MANIFEST_ROOT_HASH", "payload manifest hash mismatch")
        if sha256_path(prereg_path) != arguments.expected_prereg_sha256:
            raise CustodyFault("PREREG_ROOT_HASH", "preregistration hash mismatch")
        entries = parse_hash_manifest(root, manifest_path)
        prereg = verify_preregistration(root, prereg_path, entries,
                                        arguments.target_exponent,
                                        arguments.lane_tag,
                                        arguments.expected_manifest_sha256)

        source_members = [(relative, safe_relative_path(root, relative))
                          for relative in entries]
        source_members += [("PAYLOAD_MANIFEST.sha256", manifest_path),
                           ("PREREGISTRATION.json", prereg_path)]
        source_archive = run_dir / "source_inputs.tar.gz"
        source_archive_sha = deterministic_tar(
            source_archive, root, source_members)

        state_path = Path(arguments.state).resolve()
        report_path = run_dir / "runner_report.json"
        worker_path = root / "cases/d43_source_high_hensel_aws_worker.sh"
        runner_path = root / "cases/d43_source_high_hensel.py"
        certificate_path = root / "cases/d43_full_certificate_p105337.json"
        p2_reference_path = root / "cases/d43_char0_lift_p105337.json"
        python_path = Path(sys.executable).resolve()

        state_path.parent.mkdir(parents=True, exist_ok=True)
        supervisor_lock_path = Path(str(state_path) + ".supervisor.lock")
        state_lock_handle = open(supervisor_lock_path, "a+")
        try:
            fcntl.flock(state_lock_handle.fileno(),
                        fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise CustodyFault("STATE_LOCK", "another supervisor owns state") from error

        argv = [str(worker_path), str(root), str(python_path),
                str(runner_path), str(arguments.target_exponent),
                str(state_path), str(report_path), str(certificate_path),
                str(p2_reference_path)]
        job_identity = {
            "job_id": arguments.job_id,
            "target_exponent": arguments.target_exponent,
            "lane_tag": arguments.lane_tag,
            "hostname": identity["hostname"],
            "instance_id": identity["instance_id"],
            "instance_type": identity["instance_type"],
            "payload_manifest_sha256": arguments.expected_manifest_sha256,
            "prereg_sha256": arguments.expected_prereg_sha256,
            "source_archive_sha256": source_archive_sha,
            "argv_sha256": sha256_json(argv),
        }
        marker = {
            "schema": AUTH_SCHEMA,
            "target_exponent": arguments.target_exponent,
            "lane_tag": arguments.lane_tag,
            "job_id": arguments.job_id,
            "hostname": identity["hostname"],
            "hostname_sha256": sha256_bytes(identity["hostname"].encode()),
            "instance_id": identity["instance_id"],
            "instance_type": identity["instance_type"],
            "input_manifest_sha256": arguments.expected_manifest_sha256,
            "prereg_sha256": arguments.expected_prereg_sha256,
            "runner_sha256": sha256_path(runner_path),
            "job_identity_sha256": sha256_json(job_identity),
            "supervisor_pid": os.getpid(),
            "state_path": str(state_path),
            "report_path": str(report_path),
            "claims_forbidden_sha256": sha256_json(FORBIDDEN_CLAIMS),
        }
        marker_path = run_dir / "aws_authorization.json"
        write_envelope(marker_path, marker)
        marker_file_sha = sha256_path(marker_path)

        try:
            import numpy
            numpy_version = numpy.__version__
        except Exception as error:
            raise CustodyFault("NUMPY", "NumPy unavailable to supervisor Python") from error
        ledger = dict(terminal_base)
        ledger.update({
            "host_identity": identity,
            "host_identity_sha256": sha256_json(identity),
            "hostname_sha256": marker["hostname_sha256"],
            "job_identity": job_identity,
            "job_identity_sha256": marker["job_identity_sha256"],
            "exact_argv": argv,
            "argv_sha256": sha256_json(argv),
            "python": {"path": str(python_path), "version": sys.version,
                       "binary_sha256": sha256_path(python_path)},
            "numpy_version": numpy_version,
            "payload_manifest": str(manifest_path),
            "payload_manifest_sha256": arguments.expected_manifest_sha256,
            "preregistration": str(prereg_path),
            "preregistration_sha256": arguments.expected_prereg_sha256,
            "source_archive_sha256": source_archive_sha,
            "authorization_file_sha256": marker_file_sha,
            "resource_contract": {
                "timeout_seconds": TIMEOUT_SECONDS,
                "rss_limit_bytes": RSS_LIMIT_BYTES,
                "swap_bytes_allowed": 0,
                "sample_interval_seconds": SAMPLE_INTERVAL_SECONDS,
                "process_model": "one fresh process group; worker execs runner; no descendants allowed",
            },
            "prereg_protocol": prereg.get("protocol"),
        })
        atomic_json(run_dir / "custody_ledger.json", ledger)

        set_subreaper()
        environment = dict(os.environ)
        environment.update({
            "JC2_D43_HENSEL_AWS_AUTH": str(marker_path),
            "JC2_D43_HENSEL_AWS_AUTH_SHA256": marker_file_sha,
            "PYTHONHASHSEED": "0", "OMP_NUM_THREADS": "1",
            "OPENBLAS_NUM_THREADS": "1", "MKL_NUM_THREADS": "1",
            "NUMEXPR_NUM_THREADS": "1", "PYTHONNOUSERSITE": "1",
            "PYTHONPATH": "",
        })
        stdout_handle = open(run_dir / "worker.stdout", "wb")
        stderr_handle = open(run_dir / "worker.stderr", "wb")
        telemetry_handle = open(run_dir / "resource_telemetry.jsonl", "w")
        process = subprocess.Popen(argv, cwd=root, env=environment,
                                   stdout=stdout_handle, stderr=stderr_handle,
                                   start_new_session=True)
        known_pids.add(process.pid)
        monotonic_start = time.monotonic()
        peak_rss = 0
        samples = 0
        fault = None
        while True:
            elapsed = time.monotonic() - monotonic_start
            sample = process_sample(process.pid)
            known_pids.update(sample["descendant_pids"])
            peak_rss = max(peak_rss, sample["rss_bytes"])
            sample.update({"sample": samples, "elapsed_seconds": elapsed,
                           "utc": utc_now()})
            telemetry_handle.write(json.dumps(sample, sort_keys=True) + "\n")
            telemetry_handle.flush()
            samples += 1
            if sample["escaped_descendant_pids"] or \
                    sample["unexpected_group_pids"] or \
                    sample["descendant_pids"]:
                fault = CustodyFault("PROCESS_CONTAINMENT",
                                     "unexpected or escaped descendant")
            elif sample["rss_bytes"] > RSS_LIMIT_BYTES:
                fault = CustodyFault("RSS_LIMIT", "RSS exceeded 2 GiB")
            elif sample["process_swap_bytes"] != 0 or \
                    sample["global_swap_used_bytes"] != 0:
                fault = CustodyFault("SWAP_RUNTIME", "swap became nonzero")
            elif elapsed > TIMEOUT_SECONDS:
                fault = CustodyFault("TIMEOUT", "1200-second timeout")
            return_code = process.poll()
            if fault or return_code is not None:
                break
            time.sleep(SAMPLE_INTERVAL_SECONDS)

        containment = None
        if fault:
            containment = terminate_contained(process, known_pids)
        else:
            return_code = process.wait(timeout=5)
            remaining = process_sample(process.pid)
            if remaining["group_pids"] or remaining["descendant_pids"]:
                fault = CustodyFault("ORPHAN_PROCESS", "payload processes remain")
                containment = terminate_contained(process, known_pids)
            elif return_code != 0:
                fault = CustodyFault("CHILD_NONZERO", "runner rc=%d" % return_code)
        for handle in (stdout_handle, stderr_handle, telemetry_handle):
            handle.flush()
            os.fsync(handle.fileno())
            handle.close()
        stdout_handle = stderr_handle = telemetry_handle = None

        if fault:
            raise fault
        if not report_path.is_file() or not state_path.is_file():
            raise CustodyFault("OUTPUT_MISSING", "runner report/state missing")
        report = json.loads(report_path.read_text())
        if report.get("status") not in (
                "FINITE_SOURCE_LIFT_ONLY", "SPECIFIC_BRANCH_OBSTRUCTED",
                "FINITE_RAW_SOURCE_TEMPLATE_GATE_FAILED"):
            raise CustodyFault("RUNNER_STATUS", "unregistered runner result")
        if report.get("scope") != SCOPE or \
                report.get("claims_certified") != CERTIFIED_CLAIM or \
                report.get("exact_relations_replayed") != \
                EXACT_RELATIONS_REPLAYED or \
                report.get("upstream_not_replayed") != \
                UPSTREAM_NOT_REPLAYED or \
                report.get("claims_forbidden") != FORBIDDEN_CLAIMS or \
                report.get("semantic_chain_replay") != \
                "PASS_FROM_REGISTERED_MOD_P_STATE":
            raise CustodyFault("RUNNER_SCOPE", "runner scope/replay drift")
        template_gate = report.get("necessary_template_relation_gate")
        if not isinstance(template_gate, dict):
            raise CustodyFault("RUNNER_TEMPLATE_GATE",
                               "necessary E/W gate is absent")
        if report["status"] == "FINITE_RAW_SOURCE_TEMPLATE_GATE_FAILED":
            if template_gate.get("pass") is not False:
                raise CustodyFault("RUNNER_TEMPLATE_GATE",
                                   "failure status has passing E/W gate")
        elif template_gate.get("pass") is not True:
            raise CustodyFault("RUNNER_TEMPLATE_GATE",
                               "live/obstructed state lacks passing E/W gate")
        if report.get("requested_exponent") != arguments.target_exponent:
            raise CustodyFault("RUNNER_TARGET", "runner target drift")
        atomic_bytes(run_dir / "state.snapshot.json", state_path.read_bytes())
        terminal = dict(terminal_base)
        terminal.update({
            "status": "FINITE_SOURCE_RESULT_CUSTODY_PASS",
            "mathematical_outcome": report["status"],
            "achieved_exponent": report["achieved_exponent"],
            "end_utc": utc_now(),
            "return_code": process.returncode,
            "peak_process_group_rss_bytes": peak_rss,
            "resource_samples": samples,
            "global_swap_zero_every_sample": True,
            "process_swap_zero_every_sample": True,
            "no_orphans": True,
            "runner_report_sha256": sha256_path(report_path),
            "state_snapshot_sha256": sha256_path(
                run_dir / "state.snapshot.json"),
            "custody_ledger_sha256": sha256_path(
                run_dir / "custody_ledger.json"),
        })
        bundle = terminal_bundle(run_dir, terminal)
        terminal["bundle_sidecar"] = bundle
        # The authoritative terminal in the archive precedes this convenience
        # augmentation; its exact hash is in bundle_sidecar.
        atomic_json(run_dir / "terminal_summary.json", terminal)
        return terminal, 0
    except Exception as caught:
        error = caught if isinstance(caught, CustodyFault) else CustodyFault(
            "SUPERVISOR_EXCEPTION", repr(caught))
        if process is not None and process.poll() is None:
            containment = terminate_contained(process, known_pids)
        else:
            containment = None
        terminal = dict(terminal_base)
        terminal.update({
            "status": "NO_VERDICT_CUSTODY_FAULT",
            "fault_code": error.code,
            "fault_detail": error.detail,
            "end_utc": utc_now(),
            "mathematical_outcome": None,
            "containment": containment,
        })
        try:
            terminal_bundle(run_dir, terminal)
        except Exception as archive_error:
            terminal["archive_fault"] = repr(archive_error)
            atomic_json(run_dir / "terminal.json", terminal)
        return terminal, 125
    finally:
        for handle in (stdout_handle, stderr_handle, telemetry_handle):
            if handle is not None and not handle.closed:
                handle.close()
        if state_lock_handle is not None:
            fcntl.flock(state_lock_handle.fileno(), fcntl.LOCK_UN)
            state_lock_handle.close()
        for signum, handler in old_handlers.items():
            signal.signal(signum, handler)


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    parser.add_argument("--run-dir", required=True)
    parser.add_argument("--state", required=True)
    parser.add_argument("--target-exponent", required=True, type=int,
                        choices=(16, 64))
    parser.add_argument("--lane-tag", required=True)
    parser.add_argument("--job-id", required=True)
    parser.add_argument("--expected-hostname", required=True)
    parser.add_argument("--expected-instance-id", required=True)
    parser.add_argument("--expected-instance-type", required=True,
                        choices=(EXPECTED_INSTANCE_TYPE,))
    parser.add_argument("--payload-manifest", required=True)
    parser.add_argument("--expected-manifest-sha256", required=True)
    parser.add_argument("--preregistration", required=True)
    parser.add_argument("--expected-prereg-sha256", required=True)
    return parser


def main() -> None:
    arguments = build_parser().parse_args()
    for name in ("expected_manifest_sha256", "expected_prereg_sha256"):
        if not SHA_RE.fullmatch(getattr(arguments, name)):
            raise SystemExit("malformed --%s" % name.replace("_", "-"))
    try:
        terminal, code = run_supervised(arguments)
    except CustodyFault as error:
        terminal = {"schema": TERMINAL_SCHEMA,
                    "status": "NO_VERDICT_CUSTODY_FAULT",
                    "fault_code": error.code,
                    "fault_detail": error.detail,
                    "mathematical_outcome": None,
                    "end_utc": utc_now()}
        code = 125
    print(json.dumps(terminal, indent=1, sort_keys=True))
    raise SystemExit(code)


if __name__ == "__main__":
    main()
