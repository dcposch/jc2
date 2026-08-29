#!/usr/bin/env python3
"""Execution runner for the D43 `K0` field certificate, R4.

Runs the two independent engines, requires exact agreement on the shared
integer observables, replays every emitted artifact against its manifest, and
publishes exactly one atomic terminal that keeps three things apart:

    K0_UNCONDITIONAL_THEOREM     the coefficient-field theorem (L0-L4)
    E_CONDITIONAL_RATIO_THEOREM  the ratio theorem (L5), single-engine Python
    EXECUTION_INTEGRITY          census, manifest, archive, battery, engines
    CORROBORATION                pointbanks and the GP base identities

Nothing here decides whether it is allowed to run: ``aws_supervisor_r4.py``
owns that.  This module refuses to start outside a supervisor-created run
directory carrying a valid job marker.

R2 repair of the observed R1 AWS fault
--------------------------------------
The R1 supervisor invoked ``python3 -I -B runner_r1.py``.  Isolated mode
implies ``-P``, so the script's own directory is not on ``sys.path`` and the
bare ``import k0_field_checker_r1`` raised ``ModuleNotFoundError`` before
either engine ran.  R2 keeps ``-I -B`` -- and now *requires* isolated mode --
and loads its sealed siblings by explicit file path out of the extracted
packet directory, verifying each one against ``PAYLOAD.sha256`` whose own
digest is bound to the coordinator authorization.  ``sys.path`` is never
modified; the loader asserts that it is unchanged.  ``--import-smoke`` runs
exactly that loader and nothing else, which is what ``preflight_r4.py``
executes as a real ``python3 -I -B`` subprocess.

Emission policy, enforced by ``_forbidden_language_scan``: the only component
list any artifact may contain is the literal ``["K0"]`` and the only idempotent
list is ``[0, 1]``.  No product decomposition, primitive idempotent, or
component-count other than 1 is ever written.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import re
import resource
import subprocess
import sys
import tarfile
import time
from pathlib import Path

SCHEMA = "d43-k0-field-certificate-runner-r4"
ROUTE = "D43-K0-FIELD-CERT-R4"
EXPECTED_PACKET_DIRNAME = "d43_k0_field_certificate_r4_20260829"
PACKET_MANIFEST_NAME = "PAYLOAD.sha256"
SEALED_MODULES = ("k0_algebra_r4", "k0_field_checker_r4", "k0_mutations_r4")
GP_SCRIPT_NAME = "k0_field_cert_r4.gp"
GP_CENSUS_EXPECTED = 110
GP_OBSERVABLE_COUNT = 29
ARTIFACT_BYTE_CAP = 512 * 1024
RUN_BYTE_CAP = 4 * 1024 * 1024
ADDRESS_SPACE_CAP = 768 * 1024 * 1024
WALL_CLOCK_CAP_SECONDS = 240
GP_TIMEOUT_SECONDS = 120
EXPECTED_GP_VERSION = "2.15.4"
THREAD_VARIABLES = ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS",
                    "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS",
                    "VECLIB_MAXIMUM_THREADS", "GP_THREADS")
# R3 repair (producer-found, REPAIR-2): the R2 law listed only the two
# supervisor JSON files, but the supervisor extracts the reviewed archive into
# ``<run dir>/source`` *before* it spawns the runner, and R3 additionally has
# the root-minted claim token and the authorization lease sitting in the run
# directory.  The R2 set therefore refused every real launch with
# RUN_DIR_REUSE, one integration fault downstream of the one the R2 review
# found.  The two custody file names are derived from the marker's
# authorization digest, so this stays an exact-set law rather than a glob.
PRE_RUN_FILES = frozenset({"job_marker.json", "execution_pins_live.json",
                           "source"})
REQUIRED_PRE_RUN_FILES = frozenset(PRE_RUN_FILES)
CLAIM_TOKEN_PREFIX = ".jc2-k0-r4-claim-"
CLAIM_TOKEN_SUFFIX = ".json"
AUTHORIZATION_LEASE_PREFIX = ".jc2-k0-r4-authorization-"
AUTHORIZATION_LEASE_SUFFIX = ".lease"
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
ALLOWED_COMPONENTS = ["K0"]
ALLOWED_IDEMPOTENTS = [0, 1]
FORBIDDEN_PATTERNS = [
    re.compile(r"K0[-_ ]?SPLIT\s*[:=]\s*\["),
    re.compile(r"primitive[_ ]idempotent"),
    re.compile(r"component_count\"\s*:\s*(?!1\b)\d"),
    re.compile(r"\bK_?[1-9]\d*\b"),
    re.compile(r"prod(uct)?_decomposition\"\s*:\s*\["),
]
FORBIDDEN_CLAIMS = [
    "D43 row certificate", "D43 point", "template or D25 equation",
    "raw-J existence", "Keller map", "JC2 counterexample",
    "any tier above the coefficient algebra",
]

CK = None      # bound by load_sealed_siblings
MB = None


class RunnerFault(RuntimeError):
    def __init__(self, code, detail):
        super().__init__(detail)
        self.code = str(code)


def fault(code, detail):
    raise RunnerFault(code, detail)


def sha256_bytes(blob):
    return hashlib.sha256(blob).hexdigest()


def sha256_path(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def utc_now():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def _fsync_dir(path):
    fd = os.open(str(path), os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


# --------------------------------------------------------------------------
# the sealed sibling loader (R2 repair of the R1 isolated-import fault)
# --------------------------------------------------------------------------


def packet_dir():
    here = Path(__file__).resolve().parent
    if here.name != EXPECTED_PACKET_DIRNAME:
        fault("PACKET_DIR_NAME",
              "the runner lives in %s, expected a directory named %s"
              % (here, EXPECTED_PACKET_DIRNAME))
    return here


def read_packet_manifest(pkt):
    """``PAYLOAD.sha256`` as {member basename: sha}, plus its own digest."""
    path = Path(pkt) / PACKET_MANIFEST_NAME
    if path.is_symlink() or not path.is_file():
        fault("PACKET_MANIFEST_MISSING", str(path))
    blob = path.read_bytes()
    prefix = "cases/%s/" % EXPECTED_PACKET_DIRNAME
    entries = {}
    for line in blob.decode("ascii").splitlines():
        if not line.strip():
            continue
        parts = line.split(None, 1)
        if len(parts) != 2 or not re.fullmatch(r"[0-9a-f]{64}", parts[0]):
            fault("PACKET_MANIFEST_SHAPE", line[:120])
        rel = parts[1].strip()
        if not rel.startswith(prefix) or "/" in rel[len(prefix):]:
            fault("PACKET_MANIFEST_SHAPE", "member outside the packet: %s" % rel)
        name = rel[len(prefix):]
        if name in entries:
            fault("PACKET_MANIFEST_SHAPE", "duplicate member %s" % name)
        entries[name] = parts[0]
    if not entries:
        fault("PACKET_MANIFEST_SHAPE", "the packet manifest is empty")
    return entries, sha256_bytes(blob)


def load_sealed_siblings(pkt, expect_manifest_sha=None):
    """Import the sealed sibling modules by path, hash-checked, no sys.path edit.

    ``expect_manifest_sha`` is the ``packet_manifest_sha256`` field of the
    coordinator authorization, handed down by the supervisor.  With it the
    module load is bound to the authorization rather than to a value the
    packet recomputes about itself.
    """
    pkt = Path(pkt)
    entries, manifest_sha = read_packet_manifest(pkt)
    if expect_manifest_sha is not None and manifest_sha != expect_manifest_sha:
        fault("PACKET_MANIFEST_BINDING",
              "%s hashes %s, the authorization binds %s"
              % (PACKET_MANIFEST_NAME, manifest_sha, expect_manifest_sha))
    path_before = list(sys.path)
    loaded = {}
    for name in SEALED_MODULES:
        member = name + ".py"
        if member not in entries:
            fault("SEALED_MODULE_UNMANIFESTED",
                  "%s is not listed in %s" % (member, PACKET_MANIFEST_NAME))
        path = pkt / member
        if path.is_symlink() or not path.is_file():
            fault("SEALED_MODULE_MISSING", str(path))
        blob = path.read_bytes()
        got = sha256_bytes(blob)
        if got != entries[member]:
            fault("SEALED_MODULE_HASH",
                  "%s hashes %s, the manifest says %s"
                  % (member, got, entries[member]))
        spec = importlib.util.spec_from_file_location(name, str(path))
        if spec is None or spec.loader is None:
            fault("SEALED_MODULE_SPEC", member)
        module = importlib.util.module_from_spec(spec)
        # registered before execution so that a sibling's plain
        # ``import k0_algebra_r4`` resolves out of sys.modules and never
        # touches the filesystem search path
        sys.modules[name] = module
        spec.loader.exec_module(module)
        loaded[name] = got
    if list(sys.path) != path_before:
        fault("SYS_PATH_MUTATED",
              "the sealed loader must not change sys.path")
    globals()["CK"] = sys.modules["k0_field_checker_r4"]
    globals()["MB"] = sys.modules["k0_mutations_r4"]
    return loaded, manifest_sha


def import_smoke(pkt, expect_manifest_sha=None):
    """Load the sealed siblings and nothing else.

    This is the exact code path whose R1 ancestor failed on AWS.  It runs no
    mathematics, reads no pointbank, writes no artifact, and requires isolated
    mode so that it genuinely reproduces the R1 execution shape.
    """
    if not sys.flags.isolated:
        fault("SMOKE_NOT_ISOLATED",
              "the import smoke must run under python3 -I so that it tests the "
              "path that failed in R1")
    loaded, manifest_sha = load_sealed_siblings(pkt, expect_manifest_sha)
    digest = sha256_bytes(json.dumps(sorted(loaded.items()),
                                     separators=(",", ":")).encode("ascii"))
    for name in SEALED_MODULES:
        if name not in sys.modules:
            fault("SEALED_MODULE_ABSENT", name)
    if not hasattr(CK, "REGISTRY") or not CK.REGISTRY:
        fault("SEALED_MODULE_EMPTY", "the checker registry is empty")
    if not hasattr(MB, "MUTATIONS") or not MB.MUTATIONS:
        fault("SEALED_MODULE_EMPTY", "the mutation battery is empty")
    sys.stdout.write(
        "IMPORT_SMOKE_OK manifest %s modules %d gates %d mutations %d bind %s\n"
        % (manifest_sha, len(loaded), len(CK.REGISTRY), len(MB.MUTATIONS),
           digest))
    return 0


# --------------------------------------------------------------------------
# artifacts
# --------------------------------------------------------------------------


def emit_immutable(path, blob):
    """Create exclusively, write, fsync, then drop to read-only.

    R2 repair D11: R1 wrote a ``<name>.tmp`` sidecar and then ``os.replace``d
    it over a path it had merely *checked* did not exist.  Here the collision
    semantics are the atomic ``O_CREAT|O_EXCL`` on the final name itself, so
    there is no window and no temporary name to collide with a member.
    """
    path = Path(path)
    if len(blob) > ARTIFACT_BYTE_CAP:
        fault("ARTIFACT_TOO_LARGE",
              "%s is %d bytes, cap %d" % (path, len(blob), ARTIFACT_BYTE_CAP))
    try:
        fd = os.open(str(path), os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except FileExistsError:
        fault("ARTIFACT_COLLISION", "refusing to overwrite %s" % path)
    try:
        os.write(fd, blob)
        os.fsync(fd)
        os.fchmod(fd, 0o444)
    finally:
        os.close(fd)
    _fsync_dir(path.parent)
    return sha256_bytes(blob)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=True).encode("ascii")


def check_run_dir_clean(run_dir, auth_sha):
    """R2 repair D11, corrected in R3: the pre-run directory is pinned exactly.

    R1 listed three artifact names and asked whether each existed, so any
    fourth stale member was invisible.  R2 pinned the whole listing but to the
    wrong set (see :data:`PRE_RUN_FILES`).  Here the directory must hold
    exactly the three things the supervisor puts there plus the two custody
    objects named after this authorization -- no more, and no fewer.  Both
    directions matter: a missing ``source`` means the staging step did not run,
    and a missing lease means the launch bypassed the custody sequence.
    """
    if not SHA_RE.match(str(auth_sha)):
        fault("MARKER_AUTHORIZATION",
              "the job marker's authorization_sha256 %r is not a SHA-256"
              % (auth_sha,))
    custody = {CLAIM_TOKEN_PREFIX + auth_sha + CLAIM_TOKEN_SUFFIX,
               AUTHORIZATION_LEASE_PREFIX + auth_sha + AUTHORIZATION_LEASE_SUFFIX}
    allowed = set(PRE_RUN_FILES) | custody
    present = set(os.listdir(str(run_dir)))
    if not present <= allowed:
        fault("RUN_DIR_REUSE",
              "the run directory already holds %s; only %s may be present"
              % (sorted(present - allowed), sorted(allowed)))
    missing = sorted((REQUIRED_PRE_RUN_FILES | custody) - present)
    if missing:
        fault("RUN_DIR_INCOMPLETE",
              "the run directory is missing %s; the supervisor stages the "
              "source tree and takes the authorization lease before the "
              "runner starts" % missing)
    if not (Path(run_dir) / "source").is_dir():
        fault("RUN_DIR_INCOMPLETE", "<run dir>/source is not a directory")
    return sorted(present)


# --------------------------------------------------------------------------
# environment
# --------------------------------------------------------------------------


def enforce_single_core_and_memory():
    caps = {}
    for name in THREAD_VARIABLES:
        value = os.environ.get(name)
        if value not in ("1", None):
            fault("MULTICORE_ENVIRONMENT", "%s=%s, expected 1" % (name, value))
        os.environ[name] = "1"
        caps[name] = "1"
    try:
        affinity = os.sched_getaffinity(0)
    except AttributeError:
        affinity = None
    if affinity is not None and len(affinity) != 1:
        fault("MULTICORE_AFFINITY",
              "%d CPUs in the affinity mask, expected exactly 1"
              % len(affinity))
    resource.setrlimit(resource.RLIMIT_AS,
                       (ADDRESS_SPACE_CAP, ADDRESS_SPACE_CAP))
    resource.setrlimit(resource.RLIMIT_FSIZE,
                       (ARTIFACT_BYTE_CAP * 8, ARTIFACT_BYTE_CAP * 8))
    resource.setrlimit(resource.RLIMIT_NPROC, (64, 64))
    return {"thread_variables": caps,
            "cpu_affinity": sorted(affinity) if affinity is not None else None,
            "address_space_cap_bytes": ADDRESS_SPACE_CAP,
            "file_size_cap_bytes": ARTIFACT_BYTE_CAP * 8,
            "isolated_mode": bool(sys.flags.isolated),
            "dont_write_bytecode": bool(sys.dont_write_bytecode)}


def swap_is_zero(meminfo="/proc/meminfo"):
    path = Path(meminfo)
    if not path.is_file():
        return {"checked": False, "reason": "no %s on this host" % meminfo}
    total = used = None
    for line in path.read_text().splitlines():
        if line.startswith("SwapTotal:"):
            total = int(line.split()[1])
        elif line.startswith("SwapFree:"):
            free = int(line.split()[1])
            used = None if total is None else total - free
    if total is None:
        fault("SWAP_UNREADABLE", "SwapTotal absent from %s" % meminfo)
    if total != 0:
        fault("SWAP_PRESENT", "SwapTotal is %d kB, must be 0" % total)
    return {"checked": True, "swap_total_kb": total, "swap_used_kb": used or 0}


# --------------------------------------------------------------------------
# the PARI/GP engine
# --------------------------------------------------------------------------

GATE_LINE = re.compile(r"^(?P<label>\S.{0,80}?)\s+(?P<flag>[01])$")
OBS_LINE = re.compile(r"^OBS (?P<key>[A-Za-z0-9_]+) (?P<value>-?\d+)$")
CENSUS_LINE = re.compile(r"^CENSUS (?P<got>\d+)/(?P<want>\d+)$")
TERMINAL_LINE = re.compile(
    r"^K0_UNCONDITIONAL (?P<k0>[01])\s+E_BASE_IDENTITIES (?P<e>[01])$")


def run_gp(gp_binary, gp_script, gp_sha256, gp_binary_sha256, workdir):
    binary = Path(gp_binary)
    if not binary.is_absolute() or binary.is_symlink() or not binary.is_file():
        fault("GP_BINARY", "gp must be an absolute, symlink-free regular file")
    binary_sha = sha256_path(binary)
    if not re.fullmatch(r"[0-9a-f]{64}", str(gp_binary_sha256 or "")):
        fault("GP_BINARY_UNPINNED",
              "the authorization must pin the gp binary SHA-256")
    if binary_sha != gp_binary_sha256:
        fault("GP_BINARY_HASH", "gp binary hash %s" % binary_sha)
    version = subprocess.run([str(binary), "--version-short"],
                             capture_output=True, text=True, timeout=30)
    banner = (version.stdout + version.stderr).strip()
    if banner != EXPECTED_GP_VERSION:
        fault("GP_VERSION",
              "gp reports %r, this packet is pinned to %r"
              % (banner, EXPECTED_GP_VERSION))
    script = Path(gp_script)
    got = sha256_path(script)
    if got != gp_sha256:
        fault("GP_SCRIPT_HASH", "%s has hash %s" % (script, got))
    started = time.time()
    proc = subprocess.run(
        [str(binary), "-q", "--default", "parisize=64M",
         "--default", "parisizemax=256M", str(script)],
        capture_output=True, text=True, timeout=GP_TIMEOUT_SECONDS,
        cwd=str(workdir), env={k: v for k, v in os.environ.items()
                               if k in ("PATH", "HOME", "LANG", "LC_ALL", "TZ")
                               or k in THREAD_VARIABLES})
    elapsed = time.time() - started
    if proc.returncode != 0:
        fault("GP_EXIT", "gp exited %d: %s" % (proc.returncode,
                                               proc.stderr[:400]))
    if len(proc.stdout) > ARTIFACT_BYTE_CAP:
        fault("GP_OUTPUT_TOO_LARGE", "%d bytes" % len(proc.stdout))
    gates, observables, census, terminal = [], {}, None, None
    for line in proc.stdout.splitlines():
        line = line.rstrip()
        if not line:
            continue
        m = OBS_LINE.match(line)
        if m:
            key = m.group("key")
            if key in observables:
                fault("GP_DUPLICATE_OBSERVABLE", key)
            observables[key] = int(m.group("value"))
            continue
        m = CENSUS_LINE.match(line)
        if m:
            census = (int(m.group("got")), int(m.group("want")))
            continue
        m = TERMINAL_LINE.match(line)
        if m:
            terminal = (int(m.group("k0")), int(m.group("e")))
            continue
        m = GATE_LINE.match(line)
        if m:
            gates.append((m.group("label").strip(), int(m.group("flag"))))
            continue
        # R2: there is no OPTIONAL block any more, so every other line faults
        fault("GP_UNPARSED_LINE", line[:200])
    # the banner is never trusted: every printed gate flag is counted here
    failed = [label for label, flag in gates if flag != 1]
    if failed:
        fault("GP_GATE_FAILED", "%d gates printed 0: %s" % (len(failed),
                                                            failed[:5]))
    if len(gates) != GP_CENSUS_EXPECTED:
        fault("GP_GATE_COUNT",
              "%d gate lines printed, %d expected" % (len(gates),
                                                      GP_CENSUS_EXPECTED))
    if census != (GP_CENSUS_EXPECTED, GP_CENSUS_EXPECTED):
        fault("GP_CENSUS", "census line %s" % (census,))
    if len(observables) != GP_OBSERVABLE_COUNT:
        fault("GP_OBSERVABLE_COUNT",
              "%d observables, %d expected" % (len(observables),
                                               GP_OBSERVABLE_COUNT))
    if terminal != (1, 1):
        fault("GP_TERMINAL", "terminal line %s" % (terminal,))
    return {"binary": str(binary), "binary_sha256": binary_sha,
            "version_banner": banner, "script_sha256": got,
            "gate_count": len(gates), "gate_labels": [g[0] for g in gates],
            "observables": observables, "census": list(census),
            "terminal": {"k0_unconditional": terminal[0],
                         "e_base_identities": terminal[1]},
            "elapsed_seconds": round(elapsed, 3),
            "stdout": proc.stdout}


# --------------------------------------------------------------------------
# emission policy
# --------------------------------------------------------------------------


REFUSAL_RECORD_KEYS = frozenset({"note", "reason", "gate_errors", "error",
                                 "detail", "_instructions"})


def _refusal_free_text(value, key=None):
    """Every string in ``value`` except the ones recording a refusal.

    ``mutations.json`` must be allowed to quote the mutated inputs it
    rejected -- that is the whole point of the battery -- but only inside a
    note, a reason, or a gate error.  Anything else is scanned strictly.
    """
    out = []
    if isinstance(value, dict):
        for k, v in value.items():
            out.append(str(k))
            if k not in REFUSAL_RECORD_KEYS:
                out.extend(_refusal_free_text(v, k))
    elif isinstance(value, list):
        for v in value:
            out.extend(_refusal_free_text(v, key))
    elif isinstance(value, str):
        out.append(value)
    else:
        out.append(repr(value))
    return out


def _forbidden_language_scan(name, blob, refusal_record=False):
    if refusal_record:
        text = "\n".join(_refusal_free_text(json.loads(blob)))
    else:
        text = blob.decode("ascii", "replace")
    for pattern in FORBIDDEN_PATTERNS:
        m = pattern.search(text)
        if m:
            fault("FORBIDDEN_EMISSION",
                  "%s matches %s at %r" % (name, pattern.pattern,
                                           text[max(0, m.start() - 40):
                                                m.end() + 40]))


def _component_policy(payload, name):
    for key, allowed in (("components", ALLOWED_COMPONENTS),
                         ("idempotents", ALLOWED_IDEMPOTENTS)):
        if key in payload and payload[key] != allowed:
            fault("FORBIDDEN_EMISSION",
                  "%s.%s is %r, only %r may be emitted"
                  % (name, key, payload[key], allowed))
    if payload.get("component_count", 1) != 1:
        fault("FORBIDDEN_EMISSION", "%s emits a component count != 1" % name)


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------


def build_parser():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--import-smoke", action="store_true",
                    help="load the sealed sibling modules and exit; runs no "
                         "mathematics and writes nothing")
    ap.add_argument("--smoke-packet-dir",
                    help="test-only: the packet directory the import smoke "
                         "should load from; rejected without --import-smoke")
    ap.add_argument("--execution-root")
    ap.add_argument("--run-dir")
    ap.add_argument("--marker")
    ap.add_argument("--gp")
    ap.add_argument("--pins")
    ap.add_argument("--source-root")
    ap.add_argument("--packet-manifest-sha256",
                    help="the packet_manifest_sha256 field of the coordinator "
                         "authorization; binds the sealed module load")
    return ap


def main(argv=None):
    args = build_parser().parse_args(argv)
    if args.smoke_packet_dir and not args.import_smoke:
        fault("SMOKE_FLAG_MISUSE",
              "--smoke-packet-dir is only accepted with --import-smoke")
    if args.import_smoke:
        for name in ("execution_root", "run_dir", "marker", "gp", "pins",
                     "source_root"):
            if getattr(args, name):
                fault("SMOKE_FLAG_MISUSE",
                      "--import-smoke takes no production argument (--%s)"
                      % name.replace("_", "-"))
        return import_smoke(Path(args.smoke_packet_dir) if args.smoke_packet_dir
                            else packet_dir(), args.packet_manifest_sha256)

    for name in ("execution_root", "run_dir", "marker", "gp", "pins",
                 "source_root", "packet_manifest_sha256"):
        if not getattr(args, name):
            fault("MISSING_ARGUMENT", "--%s is required" % name.replace("_", "-"))
    if not sys.flags.isolated:
        fault("NOT_ISOLATED",
              "the runner must be started with python3 -I; isolated execution "
              "is a custody property of this packet")
    if not sys.dont_write_bytecode:
        fault("BYTECODE_ENABLED", "the runner must be started with python3 -B")

    started = time.time()
    pkt = packet_dir()
    sealed_modules, packet_manifest_sha = load_sealed_siblings(
        pkt, args.packet_manifest_sha256)

    run_dir = Path(args.run_dir)
    if not run_dir.is_dir():
        fault("NO_RUN_DIR", "%s is not a directory" % run_dir)
    marker = json.loads(Path(args.marker).read_text())
    if marker.get("route") != ROUTE:
        fault("MARKER_ROUTE", "marker route %r" % marker.get("route"))
    if marker.get("status") != "AUTHORIZED":
        fault("MARKER_STATUS", "marker status %r" % marker.get("status"))
    check_run_dir_clean(run_dir, str(marker.get("authorization_sha256", "")))

    environment = enforce_single_core_and_memory()
    swap = swap_is_zero()
    pins = json.loads(Path(args.pins).read_text())
    if pins.get("route") != ROUTE:
        fault("PINS_ROUTE", "pins route %r" % pins.get("route"))

    gp_out = run_gp(args.gp, pkt / GP_SCRIPT_NAME, pins["gp_script_sha256"],
                    pins.get("gp_binary_sha256"), run_dir)

    banks = CK.read_pointbanks(
        [(int(p), str(Path(args.source_root) / rel), sha)
         for p, rel, sha in pins["pointbanks"]])
    result = CK.run_from_pins(CK.Spec(label="AWS_R2"), args.source_root, pins,
                              banks)
    battery = MB.run_battery(args.source_root, pins, banks)

    # ---- cross-engine agreement, on recomputed integers only ------------
    disagreements = {}
    for key, value in sorted(gp_out["observables"].items()):
        other = result["observables"].get(key)
        if other != value:
            disagreements[key] = {"gp": value, "python": other}
    for key in result["observables"]:
        if key not in gp_out["observables"]:
            disagreements[key] = {"gp": None,
                                  "python": result["observables"][key]}
    if disagreements:
        fault("ENGINE_DISAGREEMENT", json.dumps(disagreements, sort_keys=True))
    if len(gp_out["observables"]) != GP_OBSERVABLE_COUNT:
        fault("OBSERVABLE_COUNT", str(len(gp_out["observables"])))
    e_layer = set(CK.E_LAYER_OBSERVABLES)
    if not e_layer <= set(result["observables"]):
        fault("OBSERVABLE_TYPING", "an E-layer observable is missing")
    unconditional_observables = sorted(set(result["observables"]) - e_layer)

    if result["census_sha256"] != pins["expected_census_sha256"]:
        fault("CENSUS_DRIFT", result["census_sha256"])
    if result["observable_sha256"] != pins["expected_observable_sha256"]:
        fault("OBSERVABLE_DRIFT", result["observable_sha256"])

    _component_policy(result, "result.json")

    # ---- artifacts ------------------------------------------------------
    artifacts = {}
    for name, blob, refusal in (
            ("result.json", canonical(result), False),
            ("mutations.json", canonical(battery), True),
            ("gp_stdout.txt", gp_out.pop("stdout").encode("ascii"), False),
            ("gp_engine.json", canonical(gp_out), False),
            ("environment.json", canonical({"environment": environment,
                                            "swap": swap,
                                            "sealed_modules": sealed_modules,
                                            "packet_manifest_sha256":
                                                packet_manifest_sha,
                                            "started_utc": utc_now()}),
             False)):
        _forbidden_language_scan(name, blob, refusal_record=refusal)
        artifacts[name] = emit_immutable(run_dir / name, blob)

    manifest = {"schema": SCHEMA + "-manifest", "route": ROUTE,
                "artifacts": artifacts}
    manifest_blob = canonical(manifest)
    artifacts_manifest_sha = emit_immutable(run_dir / "manifest.json",
                                            manifest_blob)

    # ---- exact replay of every artifact against the manifest ------------
    replay = {}
    for name, expect in sorted(artifacts.items()):
        got = sha256_path(run_dir / name)
        if got != expect:
            fault("MANIFEST_REPLAY", "%s: %s != %s" % (name, got, expect))
        replay[name] = got
    total = sum((run_dir / n).stat().st_size for n in artifacts)
    total += (run_dir / "manifest.json").stat().st_size
    if total > RUN_BYTE_CAP:
        fault("RUN_TOO_LARGE", "%d bytes emitted, cap %d" % (total, RUN_BYTE_CAP))

    archive = run_dir / "artifacts.tar"
    members = sorted(list(artifacts) + ["manifest.json"])
    with tarfile.open(str(archive), "w", format=tarfile.PAX_FORMAT) as tar:
        for name in members:
            info = tar.gettarinfo(str(run_dir / name), arcname=name)
            info.uid = info.gid = 0
            info.uname = info.gname = ""
            info.mtime = 0
            info.mode = 0o444
            with (run_dir / name).open("rb") as fh:
                tar.addfile(info, fh)
    os.chmod(str(archive), 0o444)
    archive_sha = sha256_path(archive)
    expected_member_sha = dict(artifacts)
    expected_member_sha["manifest.json"] = artifacts_manifest_sha
    with tarfile.open(str(archive), "r") as tar:
        extracted = sorted(m.name for m in tar.getmembers())
        if extracted != members:
            fault("ARCHIVE_REPLAY", "members %s" % extracted)
        for m in tar.getmembers():
            if not m.isfile() or m.mode != 0o444 or m.mtime != 0:
                fault("ARCHIVE_REPLAY", "member %s is not a 0444 file" % m.name)
            blob = tar.extractfile(m).read()
            # R2: an explicit per-member table, never a truthiness fallback
            if sha256_bytes(blob) != expected_member_sha[m.name]:
                fault("ARCHIVE_REPLAY", "member %s does not replay" % m.name)

    elapsed = time.time() - started
    if elapsed > WALL_CLOCK_CAP_SECONDS:
        fault("WALL_CLOCK", "%.1f s exceeds %d s" % (elapsed,
                                                     WALL_CLOCK_CAP_SECONDS))

    # ---- three separated verdicts ---------------------------------------
    k0_theorem = bool(result["unconditional_k0_theorem"]
                      and gp_out["terminal"]["k0_unconditional"] == 1)
    e_theorem = bool(result["e_conditional_ratio_theorem"])
    integrity = bool(result["execution_integrity"] and battery["battery_pass"]
                     and not disagreements)
    corroboration = bool(result["corroboration_ok"]
                         and gp_out["terminal"]["e_base_identities"] == 1)

    terminal = {
        "schema": SCHEMA + "-terminal",
        "route": ROUTE,
        "date_utc": utc_now(),
        "elapsed_seconds": round(elapsed, 3),
        "job_marker_sha256": sha256_path(args.marker),
        "manifest_sha256": artifacts_manifest_sha,
        "archive_sha256": archive_sha,
        "packet_manifest_sha256": packet_manifest_sha,
        "sealed_modules": sealed_modules,
        "census_sha256": result["census_sha256"],
        "observable_sha256": result["observable_sha256"],
        "battery_sha256": battery["battery_sha256"],
        "K0_UNCONDITIONAL_THEOREM": {
            "status": "PASS" if k0_theorem else "FAIL",
            "statement": "K0 is a number field of degree exactly 432, Galois "
                         "and non-abelian over Q, with B = Q(zeta_168) of "
                         "degree 48, Delta = (Z/3)^2, idempotents 0 and 1 "
                         "only, finite etale of rank 432 over Z[1/42], and "
                         "ramified rational primes exactly {2,3,7}",
            "engines": ["stdlib Python (k0_field_checker_r4.py)",
                        "PARI/GP 2.15.4 (k0_field_cert_r4.gp)"],
            "engine_agreement": "exact on %d shared unconditional integer "
                                "observables" % len(unconditional_observables),
            "depends_on_E": False,
            "depends_on_pointbanks": False,
            "depends_on_nffactor_or_primitive_element": False,
            "census": "layer-restricted to L0-L4 non-corroboration gates"},
        "E_CONDITIONAL_RATIO_THEOREM": {
            "status": "PASS" if e_theorem else "FAIL",
            "statement": "conditional on the literal displayed "
                         "E = (9+5*r3)*A1*W1^4 + (9-5*r3)*A2*W2^4, the ratio "
                         "W1/W2 is K0-rational: q0 = u*(1+i)*(r3-1)/2 solves "
                         "E by direct substitution and the four branches "
                         "q0*i^k are four distinct elements of K0",
            "engines": ["stdlib Python (k0_field_checker_r4.py)"],
            "single_engine": True,
            "single_engine_reason":
                "k0_field_cert_r4.gp carries no cube-root layer, so it cannot "
                "substitute q0 into E.  Its L5 block reads the literal E data "
                "and certifies the base-level reduction only; that is "
                "corroboration, not a second engine for this theorem",
            "corroborated_by": ["PARI/GP 2.15.4 E_BASE_IDENTITIES flag",
                                "4 shared E-layer integer observables"],
            "depends_on_E": True,
            "conditional_input": "the displayed E from the sealed E5/E6 "
                                 "bridge; read from that file, not re-derived",
            "census": "layer-restricted to L5 non-corroboration gates"},
        "EXECUTION_INTEGRITY": {
            "status": "PASS" if integrity else "FAIL",
            "inputs": ["CENSUS_COMPLETE", "mutation battery",
                       "cross-engine observable agreement",
                       "sealed census and observable pins",
                       "manifest and archive replay",
                       "one-core, zero-swap, isolated-mode environment"],
            "mutation_battery": {
                "must_fail": battery["must_fail_count"],
                "must_survive": battery["must_survive_count"],
                "theorem_separation_controls":
                    battery["theorem_separation_controls"],
                "pass": battery["battery_pass"]}},
        "CORROBORATION": {
            "status": "PASS" if corroboration else "FAIL",
            "inputs": ["POINTBANK_REGRESSION (modular, frame-dependent)",
                       "PARI/GP base identities"],
            "typing": "feeds neither theorem boolean"},
        "credited_k0_unconditional": bool(k0_theorem and integrity),
        "credited_e_conditional": bool(e_theorem and integrity),
        "crediting_rule": "a theorem status is credited only jointly with "
                          "EXECUTION_INTEGRITY = PASS; corroboration is "
                          "reported and never credited",
        "components": ALLOWED_COMPONENTS,
        "idempotents": ALLOWED_IDEMPOTENTS,
        "component_count": 1,
        "not_claimed": FORBIDDEN_CLAIMS,
    }
    terminal_blob = canonical(terminal)
    _forbidden_language_scan("terminal.json", terminal_blob)
    _component_policy(terminal, "terminal.json")
    terminal_sha = emit_immutable(run_dir / "terminal.json", terminal_blob)
    sys.stdout.write(
        "TERMINAL %s K0_UNCONDITIONAL %s E_CONDITIONAL %s INTEGRITY %s "
        "CORROBORATION %s\n"
        % (terminal_sha, terminal["K0_UNCONDITIONAL_THEOREM"]["status"],
           terminal["E_CONDITIONAL_RATIO_THEOREM"]["status"],
           terminal["EXECUTION_INTEGRITY"]["status"],
           terminal["CORROBORATION"]["status"]))
    return 0 if (k0_theorem and e_theorem and integrity and corroboration) else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RunnerFault as exc:
        sys.stderr.write("RUNNER_FAULT %s %s\n" % (exc.code, exc))
        raise SystemExit(70)
