#!/usr/bin/env python3
"""AWS-only custody supervisor for the D43 `K0` field certificate, R2.

Launch authority is a SHA-256 stored in a live EC2 instance tag.  That hash
addresses an immutable coordinator authorization record binding the reviewed
source archive, the exact host, the exact PARI binary, the run path, and the
route.  A caller-supplied "expected" hash never authorizes anything.

Refusals are total and fail-closed.  There is no local-execution mode: absent
a live EC2 identity this program exits without running any mathematics, which
is the correct behaviour for a packet whose status is
``R2_SOURCE_READY_AWS_NOT_AUTHORIZED``.

The supervisor publishes exactly one terminal object.  Both the success and
the fault paths go through :func:`publish_terminal`, which replays the runner's
manifest and archive before installing anything, so a crashed job downgrades
to NO_VERDICT and never re-runs.

R2 repairs against R1
---------------------
* D8  ``reviewer_pass.verdict`` must be exactly the string ``"PASS"``, and the
  producer-model refusal now normalises the model name (case, spacing,
  punctuation) before comparing, so ``OPUS5``, ``opus-5`` and ``Opus5`` are all
  refused.  The whole record check is the pure function
  :func:`validate_authorization_record`, which ``preflight_r2.py`` exercises
  against a table of crafted records with no AWS in sight.
* A used authorization can never be reused, even with a fresh run path: the
  supervisor takes an exclusive ``O_CREAT|O_EXCL`` lease named after the
  authorization digest in the run parent *before* the run-path lease, and both
  leases sit outside the try block, so a second launch cannot write a terminal.
* the instance-type allowlist collapses to the single type observed on the R1
  rehearsal host; extending it is a source change and a new R-number.
* the runner is handed ``--packet-manifest-sha256`` so that its sealed module
  load is bound to this authorization.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import pwd
import re
import shutil
import stat
import subprocess
import sys
import tarfile
import time
import urllib.error
import urllib.request
from pathlib import Path

PACKET_DIR = Path(__file__).resolve().parent
ROUTE = "D43-K0-FIELD-CERT-R2"
AUTH_SCHEMA = "d43-k0-field-certificate-launch-auth-r2"
MARKER_SCHEMA = "d43-k0-field-certificate-job-marker-r2"
TERMINAL_SCHEMA = "d43-k0-field-certificate-aws-terminal-r2"
AUTHORIZATION_TAG_KEY = "jc2-d43-k0-field-cert-authorization-sha256"
JOB_TAG_KEY = "jc2-d43-k0-field-cert-job"
HOST_LABEL_TAG_KEY = "jc2-host-label"
EXPECTED_HOST_LABEL = "r6b"
EXPECTED_GP_VERSION = "2.15.4"
EXPECTED_JOB_TAG = ROUTE
# R2: the single instance type observed on the R1 rehearsal host.  Extending
# this tuple is a source change and a new R-number.
ALLOWED_INSTANCE_TYPES = ("r6i.large",)
DEDICATED_SERVICE_USER = "jc2k0"
TIMEOUT_SECONDS = 300
MEMORY_MAX_BYTES = 1024 ** 3
TASKS_MAX = 24
SWAP_MAX_BYTES = 0
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
REQUIRED_REVIEW_VERDICT = "PASS"
PRODUCER_MODEL_TOKENS = ("opus",)
AUTHORIZATION_LEASE_PREFIX = ".jc2-k0-r2-authorization-"
INJECTION_VARIABLES = {
    "BASH_ENV", "ENV", "CDPATH", "GLOBIGNORE", "SHELLOPTS", "LD_PRELOAD",
    "LD_LIBRARY_PATH", "LD_AUDIT", "LD_ORIGIN_PATH", "LD_PROFILE",
    "DYLD_INSERT_LIBRARIES", "DYLD_LIBRARY_PATH", "PYTHONHOME", "PYTHONPATH",
    "PYTHONSTARTUP", "PYTHONINSPECT", "PYTHONWARNINGS", "GLIBC_TUNABLES",
    "GPRC", "GP_DATA_DIR",
}
REQUIRED_ENV = {
    "HOME": "/var/empty", "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8",
    "PATH": "/usr/bin:/bin", "TZ": "UTC", "PYTHONHASHSEED": "0",
    "PYTHONNOUSERSITE": "1", "PYTHONDONTWRITEBYTECODE": "1",
    "OMP_NUM_THREADS": "1", "OPENBLAS_NUM_THREADS": "1",
    "MKL_NUM_THREADS": "1", "NUMEXPR_NUM_THREADS": "1",
    "VECLIB_MAXIMUM_THREADS": "1",
}


class CustodyFault(RuntimeError):
    def __init__(self, code, detail):
        super().__init__(detail)
        self.code = str(code)


def fault(code, detail):
    raise CustodyFault(code, detail)


def sha256_bytes(blob):
    return hashlib.sha256(blob).hexdigest()


def sha256_path(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=True).encode("ascii")


def utc_now():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def fsync_directory(path):
    fd = os.open(str(path), os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def atomic_bytes(path, blob, mode=0o444):
    """Exclusive create on the final name; no temporary sidecar, no window."""
    path = Path(path)
    try:
        fd = os.open(str(path), os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except FileExistsError:
        fault("TERMINAL_COLLISION", "%s already exists" % path)
    try:
        os.write(fd, blob)
        os.fsync(fd)
        os.fchmod(fd, mode)
    finally:
        os.close(fd)
    fsync_directory(path.parent)
    return sha256_bytes(blob)


def require_root_owned_immutable(path, label):
    path = Path(path)
    if not path.is_absolute() or path.is_symlink():
        fault("PATH_SHAPE", "%s must be an absolute, symlink-free path" % label)
    st = path.lstat()
    if st.st_uid != 0:
        fault("PATH_OWNER", "%s is owned by uid %d, not root" % (label, st.st_uid))
    if st.st_mode & (stat.S_IWGRP | stat.S_IWOTH):
        fault("PATH_MODE", "%s is group- or world-writable" % label)
    for parent in path.parents:
        pst = parent.lstat()
        if pst.st_uid != 0 or pst.st_mode & (stat.S_IWGRP | stat.S_IWOTH):
            fault("PATH_PARENT",
                  "%s has a non-root or writable parent %s" % (label, parent))
        if parent == Path("/"):
            break
    return path


# --------------------------------------------------------------------------
# the authorization record: a pure, testable validator
# --------------------------------------------------------------------------


def normalize_model(name):
    """Case-, space- and punctuation-insensitive model token."""
    return re.sub(r"[^a-z0-9]", "", str(name if name is not None else "").lower())


def validate_authorization_record(record):
    """Every content check on the coordinator record, with no I/O.

    Raises :class:`CustodyFault`.  ``preflight_r2.py`` calls this directly on a
    table of crafted records, which is how the D8 repair is regression-tested
    without an EC2 instance.
    """
    if not isinstance(record, dict):
        fault("AUTHORIZATION_SHAPE", "the authorization is not a JSON object")
    for key in ("schema", "route", "status", "host", "source_archive",
                "source_archive_sha256", "packet_manifest_sha256",
                "gp_binary_sha256", "gp_binary_path", "run_path",
                "coordinator_go", "reviewer_pass"):
        if key not in record:
            fault("AUTHORIZATION_SHAPE", "field %s absent" % key)
    if record["schema"] != AUTH_SCHEMA:
        fault("AUTHORIZATION_SCHEMA", str(record["schema"]))
    if record["route"] != ROUTE:
        fault("AUTHORIZATION_ROUTE", str(record["route"]))
    if record["status"] != "AUTHORIZED":
        fault("AUTHORIZATION_STATUS", str(record["status"]))
    if record["coordinator_go"] is not True:
        fault("NO_COORDINATOR_GO", "coordinator_go is not the boolean true")
    reviewer = record["reviewer_pass"]
    if not isinstance(reviewer, dict):
        fault("NO_REVIEWER_PASS", "reviewer_pass is not an object")
    if not SHA_RE.match(str(reviewer.get("report_sha256", ""))):
        fault("NO_REVIEWER_PASS",
              "a different-model source PASS report hash is required")
    if not str(reviewer.get("report_path", "")).strip():
        fault("NO_REVIEWER_PASS", "the review report path is required")
    verdict = reviewer.get("verdict")
    if not isinstance(verdict, str) or verdict != REQUIRED_REVIEW_VERDICT:
        fault("REVIEW_VERDICT",
              "reviewer_pass.verdict is %r; exactly %r is required"
              % (verdict, REQUIRED_REVIEW_VERDICT))
    model = normalize_model(reviewer.get("model"))
    if not model:
        fault("SAME_MODEL_REVIEW", "reviewer_pass.model is empty")
    for token in PRODUCER_MODEL_TOKENS:
        if token in model:
            fault("SAME_MODEL_REVIEW",
                  "the source PASS must come from a different model than the "
                  "producer (Opus 5); %r normalises to %r"
                  % (reviewer.get("model"), model))
    for key in ("source_archive_sha256", "packet_manifest_sha256",
                "gp_binary_sha256"):
        if not SHA_RE.match(str(record[key])):
            fault("AUTHORIZATION_SHAPE", "%s is not a SHA-256" % key)
    host = record["host"]
    if not isinstance(host, dict):
        fault("AUTHORIZATION_SHAPE", "host is not an object")
    if host.get("host_label") != EXPECTED_HOST_LABEL:
        fault("HOST_BINDING", "authorization host_label %r"
              % host.get("host_label"))
    if host.get("gp_version") != EXPECTED_GP_VERSION:
        fault("HOST_BINDING", "authorization gp_version %r"
              % host.get("gp_version"))
    if host.get("instance_type") not in ALLOWED_INSTANCE_TYPES:
        fault("INSTANCE_TYPE",
              "authorization instance type %r is not the registered type %s"
              % (host.get("instance_type"), list(ALLOWED_INSTANCE_TYPES)))
    for key in ("gp_binary_path", "source_archive", "run_path"):
        if not str(record[key]).startswith("/"):
            fault("PATH_SHAPE", "%s must be an absolute path" % key)
    return True


# --------------------------------------------------------------------------
# live EC2 identity: there is no offline path
# --------------------------------------------------------------------------


def _imds(path, token=None, timeout=2.0):
    req = urllib.request.Request("http://169.254.169.254/latest/" + path)
    if token:
        req.add_header("X-aws-ec2-metadata-token", token)
    with urllib.request.urlopen(req, timeout=timeout) as fh:
        return fh.read().decode("ascii").strip()


def live_identity(timeout=2.0):
    try:
        req = urllib.request.Request(
            "http://169.254.169.254/latest/api/token", method="PUT")
        req.add_header("X-aws-ec2-metadata-token-ttl-seconds", "60")
        with urllib.request.urlopen(req, timeout=timeout) as fh:
            token = fh.read().decode("ascii").strip()
        document = json.loads(_imds("dynamic/instance-identity/document", token,
                                    timeout))
        tag = _imds("meta-data/tags/instance/" + AUTHORIZATION_TAG_KEY, token,
                    timeout)
        job_tag = _imds("meta-data/tags/instance/" + JOB_TAG_KEY, token, timeout)
        host_label = _imds("meta-data/tags/instance/" + HOST_LABEL_TAG_KEY,
                           token, timeout)
    except (urllib.error.URLError, OSError, ValueError, TimeoutError) as exc:
        fault("NO_LIVE_EC2_IDENTITY",
              "IMDSv2 is unreachable (%s).  This packet has no local-execution "
              "mode: AWS custody is the only supported route." % exc)
    if not SHA_RE.match(tag):
        fault("TAG_SHAPE", "authorization tag %r is not a SHA-256" % tag)
    if job_tag != EXPECTED_JOB_TAG:
        fault("JOB_TAG", "job tag %r != %r" % (job_tag, EXPECTED_JOB_TAG))
    if host_label != EXPECTED_HOST_LABEL:
        fault("HOST_LABEL", "host label %r != %r" % (host_label,
                                                     EXPECTED_HOST_LABEL))
    if document.get("instanceType") not in ALLOWED_INSTANCE_TYPES:
        fault("INSTANCE_TYPE",
              "instance type %r is not the registered type %s"
              % (document.get("instanceType"), list(ALLOWED_INSTANCE_TYPES)))
    return {"instance_id": document["instanceId"],
            "instance_type": document["instanceType"],
            "region": document["region"],
            "image_id": document["imageId"],
            "account_id": document["accountId"],
            "host_label": host_label,
            "job_tag": job_tag,
            "authorization_tag": tag}


def load_authorization(path, live_tag):
    path = require_root_owned_immutable(path, "authorization")
    blob = path.read_bytes()
    digest = sha256_bytes(blob)
    if digest != live_tag:
        fault("AUTHORIZATION_HASH",
              "authorization file hashes %s, live tag says %s"
              % (digest, live_tag))
    record = json.loads(blob)
    validate_authorization_record(record)
    return record, digest


def reject_inherited_environment():
    present = sorted(k for k in INJECTION_VARIABLES if k in os.environ)
    if present:
        fault("ENVIRONMENT_INJECTION", "forbidden variables present: %s"
              % present)
    for key, want in sorted(REQUIRED_ENV.items()):
        got = os.environ.get(key)
        if got != want:
            fault("ENVIRONMENT_SHAPE", "%s=%r, expected %r" % (key, got, want))
    return dict(REQUIRED_ENV)


# --------------------------------------------------------------------------
# cgroup-v2 contract
# --------------------------------------------------------------------------


def _read_int(path):
    text = Path(path).read_text().strip()
    return None if text == "max" else int(text)


def verify_cgroup_contract():
    line = Path("/proc/self/cgroup").read_text().strip()
    if not line.startswith("0::"):
        fault("CGROUP_V1", "cgroup v2 unified hierarchy is required: %r" % line)
    cgdir = Path("/sys/fs/cgroup") / line.split("::", 1)[1].lstrip("/")
    if not cgdir.is_dir():
        fault("CGROUP_MISSING", str(cgdir))
    if (cgdir / "cgroup.subtree_control").exists() and \
            (cgdir / "cgroup.subtree_control").read_text().strip():
        fault("CGROUP_DELEGATED", "the job cgroup must not be delegated")
    limits = {}
    for name, want, cmp_ in (("memory.max", MEMORY_MAX_BYTES, "le"),
                             ("memory.swap.max", SWAP_MAX_BYTES, "eq"),
                             ("pids.max", TASKS_MAX, "le")):
        got = _read_int(cgdir / name)
        if got is None:
            fault("CGROUP_UNBOUNDED", "%s is max" % name)
        if cmp_ == "le" and got > want:
            fault("CGROUP_LIMIT", "%s is %d, cap %d" % (name, got, want))
        if cmp_ == "eq" and got != want:
            fault("CGROUP_LIMIT", "%s is %d, must be %d" % (name, got, want))
        limits[name] = got
    swap_events = dict(
        kv.split() for kv in
        (cgdir / "memory.swap.events").read_text().splitlines() if kv)
    if int(swap_events.get("max", 0)) or int(swap_events.get("fail", 0)):
        fault("SWAP_USED", "memory.swap.events shows swap activity")
    total = 0
    for line in Path("/proc/meminfo").read_text().splitlines():
        if line.startswith("SwapTotal:"):
            total = int(line.split()[1])
    if total != 0:
        fault("HOST_SWAP", "host SwapTotal is %d kB, must be 0" % total)
    cpus = (cgdir / "cpuset.cpus.effective")
    effective = cpus.read_text().strip() if cpus.exists() else ""
    if effective.count(",") or "-" in effective or not effective:
        fault("CPUSET", "cpuset.cpus.effective is %r, exactly one CPU is "
                        "required" % effective)
    return {"cgroup": str(cgdir), "limits": limits,
            "cpuset_effective": effective, "host_swap_total_kb": total}


# --------------------------------------------------------------------------
# source archive, leases, run path
# --------------------------------------------------------------------------


def materialize_source(archive_path, expect_sha, destination):
    archive_path = require_root_owned_immutable(archive_path, "source archive")
    got = sha256_path(archive_path)
    if got != expect_sha:
        fault("SOURCE_ARCHIVE_HASH", "%s hashes %s" % (archive_path, got))
    destination = Path(destination)
    if destination.exists():
        fault("EXECUTION_ROOT_REUSE", "%s already exists" % destination)
    destination.mkdir(mode=0o755, parents=False)
    with tarfile.open(str(archive_path), "r") as tar:
        members = tar.getmembers()
        for m in members:
            if not m.isfile():
                fault("ARCHIVE_MEMBER", "%s is not a regular file" % m.name)
            if m.name.startswith("/") or ".." in Path(m.name).parts:
                fault("ARCHIVE_MEMBER", "unsafe member path %s" % m.name)
            if m.issym() or m.islnk():
                fault("ARCHIVE_MEMBER", "link member %s" % m.name)
        names = [m.name for m in members]
        if len(set(names)) != len(names):
            fault("ARCHIVE_MEMBER", "duplicate members")
        for m in members:
            target = destination / m.name
            target.parent.mkdir(parents=True, exist_ok=True)
            with tar.extractfile(m) as src, target.open("wb") as dst:
                shutil.copyfileobj(src, dst)
            os.chmod(str(target), 0o444)
    return {"archive": str(archive_path), "archive_sha256": got,
            "members": sorted(names), "execution_root": str(destination)}


def claim_authorization_lease(run_path, auth_sha):
    """One launch per authorization, ever, even with a different run path.

    The lease name is derived from the authorization digest and lives in the
    run parent, which persists across runs.  A crashed or NO_VERDICT job has
    already taken it, so the same authorization can never be presented twice;
    a retry is a new coordinator record, a new digest and a new live tag.
    """
    parent = require_root_owned_immutable(Path(run_path).parent,
                                          "run parent directory")
    lease = parent / (AUTHORIZATION_LEASE_PREFIX + auth_sha + ".lease")
    try:
        fd = os.open(str(lease), os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o444)
    except FileExistsError:
        fault("AUTHORIZATION_REUSE",
              "%s already exists: this authorization has been presented "
              "before.  A crashed or NO_VERDICT job is never re-run under the "
              "same authorization; issue a new coordinator record and a new "
              "live tag." % lease)
    try:
        os.write(fd, canonical({"route": ROUTE, "authorization_sha256": auth_sha,
                                "run_path": str(run_path),
                                "claimed_utc": utc_now()}))
        os.fsync(fd)
    finally:
        os.close(fd)
    fsync_directory(parent)
    return str(lease)


def claim_run_path(run_path):
    """Atomic mkdir is the launch lease: a second launch cannot take it."""
    run_path = Path(run_path)
    if not run_path.is_absolute():
        fault("RUN_PATH", "run path must be absolute")
    try:
        run_path.mkdir(mode=0o700, parents=False)
    except FileExistsError:
        fault("DUPLICATE_LAUNCH",
              "%s already exists; a crashed job downgrades to NO_VERDICT and "
              "is never re-run under the same authorization" % run_path)
    fsync_directory(run_path.parent)
    return run_path


# --------------------------------------------------------------------------
# terminal
# --------------------------------------------------------------------------

TERMINAL_KEYS = ("K0_UNCONDITIONAL_THEOREM", "E_CONDITIONAL_RATIO_THEOREM",
                 "EXECUTION_INTEGRITY", "CORROBORATION")


def publish_terminal(run_dir, core, runner_terminal=None, error=None):
    payload = dict(core)
    payload["schema"] = TERMINAL_SCHEMA
    payload["date_utc"] = utc_now()
    if error is not None:
        payload["verdict"] = "NO_VERDICT"
        payload["fault"] = {"code": getattr(error, "code", "UNCLASSIFIED"),
                            "detail": str(error)[:600]}
        for key in TERMINAL_KEYS:
            payload[key] = "NO_VERDICT"
        payload["credited_k0_unconditional"] = False
        payload["credited_e_conditional"] = False
    else:
        manifest = json.loads((run_dir / "manifest.json").read_bytes())
        for name, expect in sorted(manifest["artifacts"].items()):
            got = sha256_path(run_dir / name)
            if got != expect:
                fault("TERMINAL_REPLAY", "%s: %s != %s" % (name, got, expect))
        archive = run_dir / "artifacts.tar"
        with tarfile.open(str(archive), "r") as tar:
            got_members = sorted(m.name for m in tar.getmembers())
        want_members = sorted(list(manifest["artifacts"]) + ["manifest.json"])
        if got_members != want_members:
            fault("TERMINAL_REPLAY", "archive members %s" % got_members)
        payload["verdict"] = "VERDICT"
        payload["manifest_sha256"] = sha256_path(run_dir / "manifest.json")
        payload["archive_sha256"] = sha256_path(archive)
        payload["runner_terminal_sha256"] = sha256_path(run_dir / "terminal.json")
        payload["packet_manifest_sha256"] = \
            runner_terminal.get("packet_manifest_sha256")
        payload["sealed_modules"] = runner_terminal.get("sealed_modules")
        for key in TERMINAL_KEYS:
            payload[key] = runner_terminal[key]["status"]
        payload["credited_k0_unconditional"] = \
            bool(runner_terminal.get("credited_k0_unconditional"))
        payload["credited_e_conditional"] = \
            bool(runner_terminal.get("credited_e_conditional"))
        payload["components"] = ["K0"]
        payload["idempotents"] = [0, 1]
        payload["component_count"] = 1
    blob = canonical(payload)
    digest = atomic_bytes(run_dir / "supervisor_terminal.json", blob)
    sys.stdout.write("SUPERVISOR_TERMINAL %s %s\n" % (digest,
                                                      payload["verdict"]))
    return payload, digest


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------


def run_job(authorization_path):
    identity = live_identity()
    authorization, auth_sha = load_authorization(authorization_path,
                                                 identity["authorization_tag"])
    host = authorization["host"]
    for key, live in (("instance_id", identity["instance_id"]),
                      ("instance_type", identity["instance_type"]),
                      ("image_id", identity["image_id"]),
                      ("region", identity["region"])):
        if host.get(key) != live:
            fault("HOST_BINDING", "%s: authorization %r, live %r"
                  % (key, host.get(key), live))
    try:
        if pwd.getpwuid(os.getuid()).pw_name != DEDICATED_SERVICE_USER:
            fault("SERVICE_USER", "running as %s, expected %s"
                  % (pwd.getpwuid(os.getuid()).pw_name, DEDICATED_SERVICE_USER))
    except KeyError:
        fault("SERVICE_USER", "uid %d has no passwd entry" % os.getuid())
    environment = reject_inherited_environment()
    cgroup = verify_cgroup_contract()
    # both leases sit before the try block: a refused second launch writes no
    # terminal at all
    lease = claim_authorization_lease(authorization["run_path"], auth_sha)
    run_dir = claim_run_path(authorization["run_path"])
    core = {"route": ROUTE, "authorization_sha256": auth_sha,
            "authorization_lease": lease,
            "identity": identity, "cgroup": cgroup,
            "timeout_seconds": TIMEOUT_SECONDS,
            "environment": sorted(environment)}
    try:
        execution_root = run_dir / "source"
        source = materialize_source(authorization["source_archive"],
                                    authorization["source_archive_sha256"],
                                    execution_root)
        core["source"] = source
        packet = execution_root / "cases" / PACKET_DIR.name
        manifest_sha = sha256_path(packet / "PAYLOAD.sha256")
        if manifest_sha != authorization["packet_manifest_sha256"]:
            fault("PACKET_MANIFEST", "PAYLOAD.sha256 hashes %s" % manifest_sha)
        for line in (packet / "PAYLOAD.sha256").read_text().splitlines():
            if not line.strip():
                continue
            expect, rel = line.split(None, 1)
            got = sha256_path(execution_root / rel.strip())
            if got != expect:
                fault("PACKET_MEMBER", "%s hashes %s" % (rel.strip(), got))
        marker = {"schema": MARKER_SCHEMA, "route": ROUTE,
                  "status": "AUTHORIZED", "authorization_sha256": auth_sha,
                  "instance_id": identity["instance_id"],
                  "run_path": str(run_dir), "issued_utc": utc_now()}
        marker_path = run_dir / "job_marker.json"
        atomic_bytes(marker_path, canonical(marker))
        pins_path = packet / "execution_pins_r2.json"
        pins = json.loads(pins_path.read_bytes())
        pins["gp_binary_sha256"] = authorization["gp_binary_sha256"]
        core["gp_binary_matches_r1_observation"] = (
            authorization["gp_binary_sha256"]
            == pins.get("r1_observed_gp_binary_sha256"))
        pins_live = run_dir / "execution_pins_live.json"
        atomic_bytes(pins_live, canonical(pins))
        argv = [sys.executable, "-I", "-B", str(packet / "runner_r2.py"),
                "--execution-root", str(execution_root),
                "--run-dir", str(run_dir),
                "--marker", str(marker_path),
                "--gp", authorization["gp_binary_path"],
                "--pins", str(pins_live),
                "--source-root", str(execution_root),
                "--packet-manifest-sha256",
                authorization["packet_manifest_sha256"]]
        core["runner_argv"] = argv[1:]
        deadline = time.time() + TIMEOUT_SECONDS
        proc = subprocess.run(argv, capture_output=True, text=True,
                              timeout=TIMEOUT_SECONDS, cwd="/",
                              env=dict(environment))
        if time.time() > deadline:
            fault("TIMEOUT", "the unit exceeded %d s" % TIMEOUT_SECONDS)
        core["runner_stdout"] = proc.stdout[-2000:]
        core["runner_stderr"] = proc.stderr[-2000:]
        if proc.returncode != 0:
            fault("RUNNER_EXIT", "runner exited %d: %s"
                  % (proc.returncode, proc.stderr[-400:]))
        runner_terminal = json.loads((run_dir / "terminal.json").read_bytes())
        payload, _ = publish_terminal(run_dir, core, runner_terminal)
        return payload, 0
    except CustodyFault as exc:
        publish_terminal(run_dir, core, error=exc)
        return None, 70
    except Exception as exc:                                # fail-closed
        publish_terminal(run_dir, core, error=CustodyFault("UNCLASSIFIED",
                                                           repr(exc)))
        return None, 70


def build_parser():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--authorization", required=True,
                    help="absolute path to the immutable coordinator "
                         "authorization whose SHA-256 is the live EC2 tag")
    ap.add_argument("--i-understand-this-is-aws-only", action="store_true")
    return ap


def main(argv=None):
    args = build_parser().parse_args(argv)
    if not args.i_understand_this_is_aws_only:
        sys.stderr.write(
            "REFUSED: this supervisor has no local mode.  Packet status is "
            "R2_SOURCE_READY_AWS_NOT_AUTHORIZED; a different-model source "
            "PASS and a coordinator GO are required before execution.\n")
        return 64
    try:
        _payload, rc = run_job(args.authorization)
        return rc
    except CustodyFault as exc:
        sys.stderr.write("CUSTODY_FAULT %s %s\n" % (exc.code, exc))
        return 70


if __name__ == "__main__":
    raise SystemExit(main())
