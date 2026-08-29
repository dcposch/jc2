#!/usr/bin/env python3
"""AWS-only custody supervisor for the D43 `K0` field certificate, R3.

Launch authority is a SHA-256 stored in a live EC2 instance tag.  That hash
addresses an immutable coordinator authorization record binding the reviewed
source archive, the exact host, the exact PARI binary, the run path, and the
route.  A caller-supplied "expected" hash never authorizes anything.

Refusals are total and fail-closed.  There is no local-execution mode: absent
a live EC2 identity this program exits without running any mathematics, which
is the correct behaviour for a packet whose status is
``R3_SOURCE_READY_AWS_NOT_AUTHORIZED``.

The supervisor publishes exactly one terminal object.  Both the success and
the fault paths go through :func:`publish_terminal`, which replays the runner's
manifest and archive before installing anything, so a crashed job downgrades
to NO_VERDICT and never re-runs.

R2 repairs against R1 (carried unchanged into R3)
------------------------------------------------
* D8  ``reviewer_pass.verdict`` must be exactly the string ``"PASS"``, and the
  producer-model refusal normalises the model name (case, spacing,
  punctuation) before comparing, so ``OPUS5``, ``opus-5`` and ``Opus5`` are all
  refused.  The whole record check is the pure function
  :func:`validate_authorization_record`, which ``preflight_r3.py`` exercises
  against a table of crafted records with no AWS in sight.  **R3 changes
  nothing in this function**: the authorization semantics reviewed in R2 are
  frozen.
* the instance-type allowlist collapses to the single type observed on the R1
  rehearsal host; extending it is a source change and a new R-number.
* the runner is handed ``--packet-manifest-sha256`` so that its sealed module
  load is bound to this authorization.

R3 repairs against R2: the privilege boundary
---------------------------------------------
The Fable 5 R2 source review (REPAIR-1) found the R2 custody path jointly
unsatisfiable: the unit runs the supervisor as ``jc2k0`` with an empty
capability set, while :func:`claim_authorization_lease` demanded a run parent
owned by uid 0 and free of group/world write and then tried to *create* the
lease inside it.  Only root can do that, so every rehearsal would have died
either at ``CUSTODY_FAULT PATH_OWNER`` or on an uncaught ``PermissionError``,
before any mathematics.  R3 replaces the flat run-parent layout with one
satisfiable boundary:

    <sealed parent>                     root:root 0755   never service-writable
      +- spent/                         root:root 0700   root-only mint ledger
      |    +- <auth-sha>.spent          root:root 0444   the one-shot gate
      +- <run name>/                    jc2k0     0700   the only writable dir
           +- .jc2-k0-r3-claim-<auth-sha>.json    root:root 0444
           +- .jc2-k0-r3-authorization-<auth-sha>.lease  jc2k0 0444

* the sealed parent keeps the **unchanged** root-owned, not-group/world-writable
  gate; the service never creates anything in it, so the gate is now
  satisfiable rather than weakened;
* the per-run working directory is created by root (``ExecStartPre=+`` running
  ``mint_claim_r3.sh``) and chowned to the service user, so the unprivileged
  process writes only inside a directory it owns;
* the claim token is minted by root **inside** that directory as a 0444
  root-owned file.  The service can neither create it (an unprivileged process
  cannot chown to root) nor modify it (no write bit for anybody but root, and
  the empty capability set excludes ``CAP_DAC_OVERRIDE``).  It can only unlink
  it, which is self-denial: the supervisor then refuses ``CLAIM_ABSENT``;
* minting is one-shot outside this process: ``mint_claim_r3.sh`` creates
  ``spent/<auth-sha>.spent`` with ``O_EXCL`` *first*, so a restart of the unit
  cannot re-mint even if it crashed halfway;
* the consumption lease is taken by the service inside its own run directory,
  last, after every precondition has been verified.  A failed precondition
  therefore never burns the authorization, and both the lease and every
  precondition sit outside the try block, so a refused launch writes no
  terminal at all;
* every filesystem call on the custody path converts ``OSError`` into a
  ``CustodyFault``: R2's ``PermissionError`` traceback path no longer exists.

The single seam that makes all of this testable off-host is
:class:`CustodyPolicy`.  Production builds it in exactly one place,
:func:`production_policy`, with the literal custodian uid 0; the preflight
fixtures build one with the running uid so that the same code, the same
``lstat`` results and the same POSIX permission bits are exercised by a
non-root user.  ``preflight_r3.py`` P11 pins the production construction
statically and shows, by source mutation, that each field is load-bearing.
"""

from __future__ import annotations

import argparse
import grp
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
ROUTE = "D43-K0-FIELD-CERT-R3"
AUTH_SCHEMA = "d43-k0-field-certificate-launch-auth-r3"
MARKER_SCHEMA = "d43-k0-field-certificate-job-marker-r3"
TERMINAL_SCHEMA = "d43-k0-field-certificate-aws-terminal-r3"
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
DEDICATED_SERVICE_GROUP = "jc2k0"
# the exact POSIX modes the root-side mint installs; both are checked, not
# clamped, so a wider mode is a refusal and never a silent chmod
RUN_DIR_MODE = 0o700
CLAIM_TOKEN_MODE = 0o444
CLAIM_SCHEMA = "d43-k0-field-certificate-claim-token-r3"
TIMEOUT_SECONDS = 300
MEMORY_MAX_BYTES = 1024 ** 3
TASKS_MAX = 24
SWAP_MAX_BYTES = 0
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
REQUIRED_REVIEW_VERDICT = "PASS"
PRODUCER_MODEL_TOKENS = ("opus",)
AUTHORIZATION_LEASE_PREFIX = ".jc2-k0-r3-authorization-"
AUTHORIZATION_LEASE_SUFFIX = ".lease"
CLAIM_TOKEN_PREFIX = ".jc2-k0-r3-claim-"
CLAIM_TOKEN_SUFFIX = ".json"
SPENT_DIRNAME = "spent"


def claim_token_name(auth_sha):
    """The root-minted claim token, named after the authorization digest."""
    return CLAIM_TOKEN_PREFIX + auth_sha + CLAIM_TOKEN_SUFFIX


def authorization_lease_name(auth_sha):
    """The one-time consumption lease the service takes inside its run dir."""
    return AUTHORIZATION_LEASE_PREFIX + auth_sha + AUTHORIZATION_LEASE_SUFFIX
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


class CustodyPolicy:
    """The one seam between production custody and the off-host fixtures.

    Production constructs exactly one of these, in :func:`production_policy`,
    with the literal custodian uid ``0``; ``preflight_r3.py`` P11 pins that
    construction statically and mutates it to show every field is
    load-bearing.  The fixtures construct one with the running uid, which is
    what lets a non-root user execute the real functions against real
    ``lstat`` results and real POSIX permission bits.

    Nothing here is read from the environment, from the authorization record
    or from any file: a policy is built from module constants plus the passwd
    database, and is passed explicitly to every custody function.
    """

    __slots__ = ("custodian_uid", "service_user", "service_uid", "service_gid",
                 "run_dir_mode", "claim_mode")

    def __init__(self, custodian_uid, service_user, service_uid, service_gid,
                 run_dir_mode, claim_mode):
        self.custodian_uid = int(custodian_uid)
        self.service_user = str(service_user)
        self.service_uid = int(service_uid)
        self.service_gid = int(service_gid)
        self.run_dir_mode = int(run_dir_mode)
        self.claim_mode = int(claim_mode)

    def describe(self):
        return {"custodian_uid": self.custodian_uid,
                "service_user": self.service_user,
                "service_uid": self.service_uid,
                "service_gid": self.service_gid,
                "run_dir_mode": oct(self.run_dir_mode),
                "claim_mode": oct(self.claim_mode)}


def production_policy():
    """The only policy the deployed unit ever runs under.

    The custodian is root, full stop.  The service identity is resolved from
    the passwd database rather than from anything the caller supplies, and the
    running process must already *be* that identity (real and effective), which
    is what ``User=jc2k0`` / ``Group=jc2k0`` in the unit delivers.
    """
    try:
        entry = pwd.getpwnam(DEDICATED_SERVICE_USER)
    except KeyError:
        fault("SERVICE_USER",
              "the dedicated service user %s has no passwd entry on this host"
              % DEDICATED_SERVICE_USER)
    try:
        gid = grp.getgrnam(DEDICATED_SERVICE_GROUP).gr_gid
    except KeyError:
        fault("SERVICE_USER",
              "the dedicated service group %s has no group entry on this host"
              % DEDICATED_SERVICE_GROUP)
    return CustodyPolicy(custodian_uid=0,
                         service_user=DEDICATED_SERVICE_USER,
                         service_uid=entry.pw_uid,
                         service_gid=gid,
                         run_dir_mode=RUN_DIR_MODE,
                         claim_mode=CLAIM_TOKEN_MODE)


def require_service_identity(policy):
    """Real *and* effective ids must be the dedicated service identity.

    R2 compared only ``os.getuid()``; a setuid or ``sudo -g`` invocation could
    have satisfied that while running with another effective identity, and the
    whole R3 boundary is expressed in effective ids.
    """
    uid, euid = os.getuid(), os.geteuid()
    gid, egid = os.getgid(), os.getegid()
    if uid != euid or gid != egid:
        fault("SERVICE_USER",
              "real/effective ids differ (uid %d/%d, gid %d/%d)"
              % (uid, euid, gid, egid))
    if euid != policy.service_uid or egid != policy.service_gid:
        fault("SERVICE_USER",
              "running as uid %d gid %d, expected %s (uid %d gid %d)"
              % (euid, egid, policy.service_user, policy.service_uid,
                 policy.service_gid))
    if euid == 0:
        fault("SERVICE_USER",
              "the supervisor must never run as root: the whole point of the "
              "R3 boundary is that the process cannot touch the sealed parent "
              "or the root-owned claim token")
    return {"uid": euid, "gid": egid, "user": policy.service_user}


def _lstat(path, label):
    """``lstat`` with every OSError converted into a custody fault.

    R2 let a bare ``PermissionError`` out of the custody path; nothing on this
    path may raise anything but :class:`CustodyFault`.
    """
    try:
        return Path(path).lstat()
    except OSError as exc:
        fault("PATH_STAT", "%s: cannot stat %s (%s)" % (label, path, exc))


def require_root_owned_immutable(policy, path, label):
    """The sealed-parent gate, unchanged in substance from R2.

    The target must be owned by the custodian (uid 0 in production) and carry
    no group or world write bit, and no ancestor may be writable by anyone but
    its owner.  The only R3 change is that the owner is read from ``policy``
    instead of the literal 0, and that ancestors may also be custodian-owned
    *or* root-owned -- in production those two sets coincide exactly, because
    ``production_policy().custodian_uid`` is 0.
    """
    path = Path(path)
    if not path.is_absolute() or path.is_symlink():
        fault("PATH_SHAPE", "%s must be an absolute, symlink-free path" % label)
    st = _lstat(path, label)
    if st.st_uid != policy.custodian_uid:
        fault("PATH_OWNER", "%s is owned by uid %d, not the custodian uid %d"
              % (label, st.st_uid, policy.custodian_uid))
    if st.st_mode & (stat.S_IWGRP | stat.S_IWOTH):
        fault("PATH_MODE", "%s is group- or world-writable" % label)
    allowed_owners = {0, policy.custodian_uid}
    for parent in path.parents:
        pst = _lstat(parent, label)
        if pst.st_uid not in allowed_owners or \
                pst.st_mode & (stat.S_IWGRP | stat.S_IWOTH):
            fault("PATH_PARENT",
                  "%s has a non-custodian or writable parent %s" % (label, parent))
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

    Raises :class:`CustodyFault`.  ``preflight_r3.py`` calls this directly on a
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


def load_authorization(policy, path, live_tag):
    path = require_root_owned_immutable(policy, path, "authorization")
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


def materialize_source(policy, archive_path, expect_sha, destination):
    archive_path = require_root_owned_immutable(policy, archive_path,
                                                "source archive")
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


def require_service_owned_run_dir(policy, run_path):
    """The per-run working directory, which root pre-created and chowned.

    R2 had the service ``mkdir`` this directory inside a root-owned parent,
    which no unprivileged process can do.  R3 requires it to exist already,
    owned by the service identity with mode exactly ``0700``: root minted it,
    the service merely opens it.  Nothing here creates anything.
    """
    run_path = Path(run_path)
    if not run_path.is_absolute():
        fault("RUN_DIR_SHAPE", "run path must be absolute")
    if run_path.is_symlink():
        fault("RUN_DIR_SHAPE", "%s is a symlink" % run_path)
    st = _lstat(run_path, "run directory") if run_path.exists() else None
    if st is None:
        fault("RUN_DIR_ABSENT",
              "%s does not exist.  The run directory is minted by root "
              "(ExecStartPre=+ mint_claim_r3.sh); the service never creates "
              "anything in the sealed parent." % run_path)
    if not stat.S_ISDIR(st.st_mode):
        fault("RUN_DIR_SHAPE", "%s is not a directory" % run_path)
    if st.st_uid != policy.service_uid:
        fault("RUN_DIR_OWNER", "%s is owned by uid %d, expected the service "
              "uid %d" % (run_path, st.st_uid, policy.service_uid))
    if st.st_gid != policy.service_gid:
        fault("RUN_DIR_OWNER", "%s has gid %d, expected the service gid %d"
              % (run_path, st.st_gid, policy.service_gid))
    if stat.S_IMODE(st.st_mode) != policy.run_dir_mode:
        fault("RUN_DIR_MODE", "%s is mode %s, expected exactly %s"
              % (run_path, oct(stat.S_IMODE(st.st_mode)),
                 oct(policy.run_dir_mode)))
    return run_path


def verify_claim_token(policy, run_dir, auth_sha, record):
    """The root-minted, no-replace grant for exactly this authorization.

    The token is a custodian-owned ``0444`` file *inside* the service-owned run
    directory.  An unprivileged process cannot create it (it cannot chown to
    root) and cannot modify it (no write bit for anyone but its owner, and the
    unit's capability set is empty, so ``CAP_DAC_OVERRIDE`` and ``CAP_CHOWN``
    are both unavailable).  It can unlink it, which only denies itself: the
    launch then refuses ``CLAIM_ABSENT``.  Creation and one-shot retirement are
    enforced by ``mint_claim_r3.sh``, which runs as root outside this process.
    """
    token = Path(run_dir) / claim_token_name(auth_sha)
    if token.is_symlink():
        fault("CLAIM_SHAPE", "%s is a symlink" % token)
    if not token.exists():
        fault("CLAIM_ABSENT",
              "%s is absent: this run directory carries no root-minted claim "
              "for authorization %s" % (token, auth_sha))
    st = _lstat(token, "claim token")
    if not stat.S_ISREG(st.st_mode):
        fault("CLAIM_SHAPE", "%s is not a regular file" % token)
    if st.st_uid != policy.custodian_uid:
        fault("CLAIM_OWNER",
              "%s is owned by uid %d, not the custodian uid %d: a claim the "
              "service could have written authorizes nothing"
              % (token, st.st_uid, policy.custodian_uid))
    if stat.S_IMODE(st.st_mode) != policy.claim_mode:
        fault("CLAIM_MODE", "%s is mode %s, expected exactly %s"
              % (token, oct(stat.S_IMODE(st.st_mode)), oct(policy.claim_mode)))
    if st.st_nlink != 1:
        fault("CLAIM_SHAPE", "%s has %d links" % (token, st.st_nlink))
    try:
        claim = json.loads(token.read_bytes())
    except (OSError, ValueError) as exc:
        fault("CLAIM_SHAPE", "%s is unreadable or not JSON (%s)" % (token, exc))
    if not isinstance(claim, dict):
        fault("CLAIM_SHAPE", "%s is not a JSON object" % token)
    want = {"schema": CLAIM_SCHEMA, "route": ROUTE,
            "authorization_sha256": auth_sha,
            "run_path": str(Path(run_dir)),
            "service_user": policy.service_user}
    for key, value in sorted(want.items()):
        if claim.get(key) != value:
            fault("CLAIM_BINDING", "%s: %s is %r, the launch requires %r"
                  % (token, key, claim.get(key), value))
    if str(record.get("run_path")) != str(Path(run_dir)):
        fault("CLAIM_BINDING",
              "the authorization names run_path %r but the claim was minted "
              "for %s" % (record.get("run_path"), run_dir))
    return {"path": str(token), "sha256": sha256_path(token),
            "minted_utc": claim.get("minted_utc")}


def require_run_dir_pristine(run_dir, auth_sha):
    """Nothing but the custody objects may be in the directory before launch.

    A crashed job leaves artifacts behind, so this is the crash/restart gate:
    it runs *before* the lease is taken, so an interrupted run is refused
    without burning anything further, and a directory holding only the token
    and a spent lease falls through to :func:`claim_authorization_lease`,
    which names the reuse exactly.
    """
    allowed = {claim_token_name(auth_sha), authorization_lease_name(auth_sha)}
    try:
        present = set(os.listdir(str(run_dir)))
    except OSError as exc:
        fault("RUN_DIR_SHAPE", "cannot list %s (%s)" % (run_dir, exc))
    extra = sorted(present - allowed)
    if extra:
        fault("RUN_DIR_DIRTY",
              "%s already holds %s; a crashed or completed job is never "
              "re-run in place.  Only %s may be present before launch."
              % (run_dir, extra, sorted(allowed)))
    return sorted(present)


def claim_authorization_lease(run_dir, auth_sha):
    """One launch per authorization, ever.  This is the only burn point.

    The lease lives inside the service-owned run directory, whose name is
    bound to this authorization by the root-minted claim token and by the
    authorization's own ``run_path`` field (which is inside the hashed record,
    hence inside the live tag).  A second presentation of the same
    authorization therefore lands on the same directory and dies here; a
    different run path has no claim token at all.

    Every caller reaches this function only after every precondition has
    passed, so a refused precondition never consumes the authorization.
    """
    lease = Path(run_dir) / authorization_lease_name(auth_sha)
    try:
        fd = os.open(str(lease), os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o444)
    except FileExistsError:
        fault("AUTHORIZATION_REUSE",
              "%s already exists: this authorization has been presented "
              "before.  A crashed or NO_VERDICT job is never re-run under the "
              "same authorization; issue a new coordinator record and a new "
              "live tag." % lease)
    except OSError as exc:
        # R2 let this escape as a bare PermissionError traceback
        fault("LEASE_UNWRITABLE",
              "cannot create the authorization lease %s (%s).  The run "
              "directory must be owned by %s with mode %s."
              % (lease, exc, DEDICATED_SERVICE_USER, oct(RUN_DIR_MODE)))
    try:
        os.write(fd, canonical({"route": ROUTE, "authorization_sha256": auth_sha,
                                "run_path": str(run_dir),
                                "claimed_utc": utc_now()}))
        os.fsync(fd)
    except OSError as exc:
        os.close(fd)
        fault("LEASE_UNWRITABLE", "cannot write %s (%s)" % (lease, exc))
    else:
        os.close(fd)
    try:
        fsync_directory(Path(run_dir))
    except OSError as exc:
        fault("LEASE_UNWRITABLE", "cannot fsync %s (%s)" % (run_dir, exc))
    return str(lease)


def verify_custody_preconditions(policy, record, auth_sha):
    """Everything that must hold before the authorization may be consumed.

    Pure with respect to the filesystem: it creates, writes and removes
    nothing.  ``custody_selftest_r3.py --on-host-dry-run`` calls exactly this
    function as the service user before the unit is started, which is how the
    root-owned half of the boundary is verified on the deployed host without
    burning the authorization.
    """
    run_path = Path(record["run_path"])
    parent = require_root_owned_immutable(policy, run_path.parent,
                                          "run parent directory")
    run_dir = require_service_owned_run_dir(policy, run_path)
    claim = verify_claim_token(policy, run_dir, auth_sha, record)
    present = require_run_dir_pristine(run_dir, auth_sha)
    return {"sealed_parent": str(parent), "run_dir": str(run_dir),
            "claim": claim, "pre_launch_entries": present,
            "policy": policy.describe()}


def establish_custody(policy, record, auth_sha):
    """Verify, then burn, in that order.  Nothing else may take the lease."""
    custody = verify_custody_preconditions(policy, record, auth_sha)
    custody["authorization_lease"] = claim_authorization_lease(
        custody["run_dir"], auth_sha)
    return custody


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


def stage_packet(policy, authorization, run_dir):
    """Extract the reviewed archive and replay the packet manifest under it.

    Factored out of :func:`run_job` in R3 so that ``preflight_r3.py`` P11 can
    execute the real staging code against the real sealed archive in a fixture
    tree.  R1 died on an integration fault in exactly this stretch and R2
    shipped a run-directory law that had never been executed end to end.
    """
    execution_root = Path(run_dir) / "source"
    source = materialize_source(policy, authorization["source_archive"],
                                authorization["source_archive_sha256"],
                                execution_root)
    packet = execution_root / "cases" / PACKET_DIR.name
    manifest_sha = sha256_path(packet / "PAYLOAD.sha256")
    if manifest_sha != authorization["packet_manifest_sha256"]:
        fault("PACKET_MANIFEST", "PAYLOAD.sha256 hashes %s" % manifest_sha)
    members = 0
    for line in (packet / "PAYLOAD.sha256").read_text().splitlines():
        if not line.strip():
            continue
        expect, rel = line.split(None, 1)
        got = sha256_path(execution_root / rel.strip())
        if got != expect:
            fault("PACKET_MEMBER", "%s hashes %s" % (rel.strip(), got))
        members += 1
    source["packet_members_replayed"] = members
    return source, packet, manifest_sha


def run_job(authorization_path):
    policy = production_policy()
    identity = live_identity()
    authorization, auth_sha = load_authorization(policy, authorization_path,
                                                 identity["authorization_tag"])
    host = authorization["host"]
    for key, live in (("instance_id", identity["instance_id"]),
                      ("instance_type", identity["instance_type"]),
                      ("image_id", identity["image_id"]),
                      ("region", identity["region"])):
        if host.get(key) != live:
            fault("HOST_BINDING", "%s: authorization %r, live %r"
                  % (key, host.get(key), live))
    identity_record = require_service_identity(policy)
    environment = reject_inherited_environment()
    cgroup = verify_cgroup_contract()
    # The whole custody sequence sits before the try block, so a refusal at any
    # step writes no terminal at all.  Inside it, every precondition is checked
    # before the lease is taken: a failed pre-lease attempt leaves the
    # authorization unconsumed.
    custody = establish_custody(policy, authorization, auth_sha)
    run_dir = Path(custody["run_dir"])
    core = {"route": ROUTE, "authorization_sha256": auth_sha,
            "authorization_lease": custody["authorization_lease"],
            "custody": {k: custody[k] for k in
                        ("sealed_parent", "run_dir", "claim",
                         "pre_launch_entries", "policy")},
            "service_identity": identity_record,
            "identity": identity, "cgroup": cgroup,
            "timeout_seconds": TIMEOUT_SECONDS,
            "environment": sorted(environment)}
    try:
        source, packet, _manifest_sha = stage_packet(policy, authorization,
                                                     run_dir)
        execution_root = Path(source["execution_root"])
        core["source"] = source
        marker = {"schema": MARKER_SCHEMA, "route": ROUTE,
                  "status": "AUTHORIZED", "authorization_sha256": auth_sha,
                  "instance_id": identity["instance_id"],
                  "run_path": str(run_dir), "issued_utc": utc_now()}
        marker_path = run_dir / "job_marker.json"
        atomic_bytes(marker_path, canonical(marker))
        pins_path = packet / "execution_pins_r3.json"
        pins = json.loads(pins_path.read_bytes())
        pins["gp_binary_sha256"] = authorization["gp_binary_sha256"]
        core["gp_binary_matches_r1_observation"] = (
            authorization["gp_binary_sha256"]
            == pins.get("r1_observed_gp_binary_sha256"))
        pins_live = run_dir / "execution_pins_live.json"
        atomic_bytes(pins_live, canonical(pins))
        argv = [sys.executable, "-I", "-B", str(packet / "runner_r3.py"),
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
            "R3_SOURCE_READY_AWS_NOT_AUTHORIZED; a different-model source "
            "PASS and a coordinator GO are required before execution.\n")
        return 64
    try:
        _payload, rc = run_job(args.authorization)
        return rc
    except CustodyFault as exc:
        sys.stderr.write("CUSTODY_FAULT %s %s\n" % (exc.code, exc))
        return 70
    except Exception as exc:            # no custody path may show a traceback
        sys.stderr.write("CUSTODY_FAULT UNCLASSIFIED %r\n" % (exc,))
        return 70


if __name__ == "__main__":
    raise SystemExit(main())
