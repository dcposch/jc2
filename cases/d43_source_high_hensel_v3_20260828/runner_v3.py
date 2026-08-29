#!/usr/bin/python3
"""Schema-v3 fail-closed adapter for the finite D43 source Hensel lane.

The arithmetic engine is the sealed schema-v2 module.  This adapter changes
the executable trust boundary: it installs a restricted, explicitly bound D21
loader before real context construction; seals the missing core23 input; uses
state schema v3; and accepts p^3+ work only under a live-EC2-tag-anchored
authorization record.  It never broadens the finite raw-source claim.
"""

from __future__ import annotations

import argparse
import builtins
import hashlib
import importlib.metadata
import importlib.util
import json
import os
import pickle
import platform
import socket
import stat
import sys
import threading
import urllib.parse
import urllib.request
from fractions import Fraction
from pathlib import Path
from typing import Mapping


PACKET_DIR = Path(__file__).resolve().parent
CASES_DIR = PACKET_DIR.parent
ROOT = CASES_DIR.parent
if str(CASES_DIR) not in sys.path:
    sys.path.insert(0, str(CASES_DIR))

import d43_source_high_hensel as BASE
import r1_experiment as R1


SCHEMA = "d43-pristine-source-high-hensel-state-v3"
AWS_AUTH_SCHEMA = "d43-pristine-source-high-hensel-aws-auth-v3"
LAUNCH_AUTH_SCHEMA = "d43-pristine-source-high-hensel-launch-auth-v3"
ROUTE = "D43-PRISTINE-SOURCE-HIGH-HENSEL-R3"
AWS_TARGET_TAGS = {16: ROUTE + "-N16", 64: ROUTE + "-N64"}
AUTHORIZATION_TAG_KEY = "jc2-d43-high-hensel-authorization-sha256"
EXPECTED_D21_SHA256 = \
    "b4ba8dfcd9755fb3201780cd97c1d2ef38bd26d2d1b023521a0e62a3d6db169e"
EXPECTED_CORE23_SHA256 = \
    "0533787f6bf89ff25478f01ddad40230a11f6a19bb19af8889b692ce26a38cdf"
EXPECTED_NUMPY_VERSION = "2.1.3"
SHA_KEYS = {
    "launch_authorization_sha256", "payload_manifest_sha256",
    "preregistration_sha256", "runner_sha256", "base_runner_sha256",
    "supervisor_sha256", "worker_sha256", "source_archive_sha256",
    "runtime_environment_sha256", "runtime_receipt_sha256",
    "job_identity_sha256",
    "claims_forbidden_sha256", "d21_private_sha256", "core23_sha256",
    "review_report_sha256",
}
INJECTION_VARIABLES = {
    "BASH_ENV", "ENV", "CDPATH", "GLOBIGNORE", "SHELLOPTS",
    "LD_PRELOAD", "LD_LIBRARY_PATH", "DYLD_INSERT_LIBRARIES",
    "DYLD_LIBRARY_PATH", "PYTHONHOME", "PYTHONPATH", "PYTHONSTARTUP",
    "PYTHONINSPECT", "PYTHONWARNINGS", "DIRECTIONB_STATE",
}
ALLOWED_ENVIRONMENT_KEYS = {
    "HOME", "LANG", "LC_ALL", "PATH", "TZ", "SHLVL",
    "PYTHONHASHSEED", "PYTHONNOUSERSITE", "PYTHONDONTWRITEBYTECODE",
    "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
    "NUMEXPR_NUM_THREADS", "VECLIB_MAXIMUM_THREADS",
    "JC2_D43_HENSEL_AWS_AUTH", "JC2_D43_HENSEL_AWS_AUTH_SHA256",
}
AUTH_PATH_SENTINEL = "<ABSOLUTE_JOB_MARKER_PATH>"
AUTH_SHA_SENTINEL = "<SHA256_OF_JOB_MARKER_ENVELOPE>"


# The base engine resolves these names in its own module globals.  Mutating the
# imported module object is process-local; the historical v2 bytes remain
# untouched and are separately sealed in the v3 payload.
BASE.SCHEMA = SCHEMA
BASE.AWS_AUTH_SCHEMA = AWS_AUTH_SCHEMA
BASE.AWS_TARGET_TAGS = AWS_TARGET_TAGS

PRIME = BASE.PRIME
STATUS_READY = BASE.STATUS_READY
STATUS_FINITE = BASE.STATUS_FINITE
STATUS_OBSTRUCTED = BASE.STATUS_OBSTRUCTED
STATUS_TEMPLATE_FAILED = BASE.STATUS_TEMPLATE_FAILED
SCOPE = BASE.SCOPE
CERTIFIED_CLAIM = BASE.CERTIFIED_CLAIM
FORBIDDEN_CLAIMS = BASE.FORBIDDEN_CLAIMS
EXACT_RELATIONS_REPLAYED = BASE.EXACT_RELATIONS_REPLAYED
UPSTREAM_NOT_REPLAYED = BASE.UPSTREAM_NOT_REPLAYED
BRANCH_POLICY = BASE.BRANCH_POLICY


def sha256_path(path) -> str:
    return BASE.sha256_path(os.fspath(path))


def sha256_json(value) -> str:
    return BASE.sha256_json(value)


def is_sha256(value) -> bool:
    return isinstance(value, str) and len(value) == 64 and all(
        character in "0123456789abcdef" for character in value)


def _regular_nofollow_fd(path: Path) -> int:
    if Path(path).is_symlink():
        raise ValueError("symlinked sealed input is forbidden: %s" % path)
    flags = os.O_RDONLY
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    descriptor = os.open(path, flags)
    observed = os.fstat(descriptor)
    if not stat.S_ISREG(observed.st_mode):
        os.close(descriptor)
        raise ValueError("sealed input is not a regular file: %s" % path)
    return descriptor


class RestrictedD21Unpickler(pickle.Unpickler):
    """Allow exactly the two non-builtin classes in the banked D21 object."""

    def find_class(self, module, name):
        if (module, name) == ("fractions", "Fraction"):
            return Fraction
        if (module, name) == ("r1_experiment", "K3"):
            return R1.K3
        raise pickle.UnpicklingError(
            "forbidden global in sealed D21 payload: %s.%s" %
            (module, name))

    def persistent_load(self, pid):
        raise pickle.UnpicklingError(
            "persistent IDs are forbidden in sealed D21 payload: %r" % pid)


def _validate_d21_object(payload) -> None:
    if not isinstance(payload, dict) or set(payload) != {"D", "byk", "vars"}:
        raise ValueError("sealed D21 payload has wrong top-level shape")
    if payload["D"] != 21:
        raise ValueError("sealed D21 depth drift")
    variables = payload["vars"]
    if (not isinstance(variables, list) or len(variables) != 183 or
            len(set(variables)) != 183 or
            any(not isinstance(value, str) for value in variables)):
        raise ValueError("sealed D21 variable registry drift")
    byk = payload["byk"]
    if not isinstance(byk, dict) or sorted(byk) != \
            [6, 8, 10, 12, 14, 16, 18, 20]:
        raise ValueError("sealed D21 row-band registry drift")
    row_count = 0
    for band, eta_rows in byk.items():
        if not isinstance(band, int) or not isinstance(eta_rows, dict):
            raise ValueError("sealed D21 band object is malformed")
        for eta, expression in eta_rows.items():
            row_count += 1
            if not isinstance(eta, int) or not isinstance(expression, dict):
                raise ValueError("sealed D21 row object is malformed")
            for monomial, coefficient in expression.items():
                if (not isinstance(monomial, tuple) or
                        any(not isinstance(index, int) or
                            not 0 <= index < len(variables)
                            for index in monomial) or
                        not isinstance(coefficient, dict)):
                    raise ValueError("sealed D21 expression shape drift")
                for radical_key, k3 in coefficient.items():
                    if (not isinstance(radical_key, tuple) or
                            len(radical_key) != 8 or
                            any(not isinstance(value, int) or value < 0
                                for value in radical_key) or
                            not isinstance(k3, R1.K3)):
                        raise ValueError("sealed D21 coefficient shape drift")
    if row_count != 77:
        raise ValueError("sealed D21 row count drift: %d" % row_count)


def load_sealed_d21(path, expected_sha256=EXPECTED_D21_SHA256):
    unresolved = Path(path)
    if unresolved.is_symlink():
        raise ValueError("symlinked D21 input is forbidden")
    path = unresolved.resolve(strict=True)
    if not is_sha256(expected_sha256):
        raise ValueError("malformed expected D21 SHA-256")
    descriptor = _regular_nofollow_fd(path)
    with os.fdopen(descriptor, "rb") as handle:
        raw = handle.read()
    if hashlib.sha256(raw).hexdigest() != expected_sha256:
        raise ValueError("sealed private D21 payload hash mismatch")
    import io
    payload = RestrictedD21Unpickler(io.BytesIO(raw)).load()
    _validate_d21_object(payload)
    return payload


def _directionb_views(payload):
    """Build the two legacy read views without consulting an ambient path."""
    byk, variables = payload["byk"], payload["vars"]
    pin42 = {"tf1_42", "tf2_42", "tg1_42", "tg2_42",
             "tg01_42", "tg02_42"}
    nolog = []
    e32_rows = []
    for band in sorted(byk):
        for eta in sorted(byk[band]):
            expression = dict(byk[band][eta])
            has42 = band == 20 and eta == 0
            if has42:
                expression[()] = R1.radd(
                    expression.get((), R1.RZERO), R1.rC(R1.K3(42)))
            e32_rows.append(("Row_%d[eta^%d]%s" %
                             (band, eta, "+42" if has42 else ""),
                             expression, has42))
            kept = {
                monomial: coefficient
                for monomial, coefficient in expression.items()
                if not (monomial and any(
                    variables[index] in pin42 for index in monomial))
            }
            if kept:
                nolog.append(((band, eta), kept))
    occurrence = sorted({index for _label, expression, _has42 in e32_rows
                         for monomial in expression for index in monomial})
    high = [index for index in occurrence
            if variables[index][:2] in ("tf", "tg") and
            int(variables[index].rsplit("_", 1)[-1]) >= 43]
    low = [index for index in occurrence
           if variables[index][:2] in ("tf", "tg") and
           int(variables[index].rsplit("_", 1)[-1]) < 43]
    seven = [index for index in occurrence
             if variables[index][:2] not in ("tf", "tg")]
    ordered = high + low + seven
    names = {variable_id: "x%d" % index
             for index, variable_id in enumerate(ordered)}
    if len(e32_rows) != 77 or len(nolog) != 76:
        raise ValueError("sealed Direction-B derived row-count drift")
    return (nolog, variables), \
        (e32_rows, names, ordered, (high, low, seven), variables)


def install_sealed_directionb_loaders(d21_path, expected_sha256):
    if "DIRECTIONB_STATE" in os.environ:
        raise RuntimeError("ambient DIRECTIONB_STATE is forbidden")
    payload = load_sealed_d21(d21_path, expected_sha256)
    raw_view, e32_view = _directionb_views(payload)
    import directionb_window as window
    import directionb_residual32_emit as residual
    import directionb_compress as compress
    import valuation_e as valuation

    def window_load():
        return payload["byk"], payload["vars"], payload["D"]

    def nolog_load():
        return raw_view

    def residual_load():
        return e32_view

    window.STATE = "V3_SEALED_IN_MEMORY_NO_PATH_FALLBACK"
    residual.STATE = "V3_SEALED_IN_MEMORY_NO_PATH_FALLBACK"
    window.load = window_load
    compress.load_nolog_rows = nolog_load
    residual.load_rows = residual_load
    valuation._RAW = raw_view
    return {
        # Absolute job paths are custody metadata, not mathematics.  Keeping
        # one here made an authenticated p^16 state impossible to replay in a
        # distinct p^64 run directory.  The exact bytes and logical role are
        # stable across jobs; the marker independently binds the live path.
        "logical_input": "job-private/directionb_tails_D21.pkl",
        "sha256": expected_sha256,
        "safe_loader": "restricted-unpickler-plus-validated-in-memory-views",
        "rows": 77,
        "nolog_rows": 76,
        "variables": 183,
    }


_READ_POLICY_LOCK = threading.RLock()
_READ_POLICY = {
    "active": False,
    "allowed_roots": (),
    "allowed_files": set(),
    "observed": set(),
}


def _audit_open(event, arguments):
    if event != "open":
        return
    with _READ_POLICY_LOCK:
        if not _READ_POLICY["active"]:
            return
        value = arguments[0]
        if isinstance(value, int):
            return
        try:
            path = Path(os.fsdecode(value)).resolve()
        except (OSError, TypeError, ValueError):
            raise PermissionError("runtime attempted a noncanonical file open")
        allowed_roots = _READ_POLICY["allowed_roots"]
        allowed_files = _READ_POLICY["allowed_files"]
        if path not in allowed_files and not any(
                path == root or root in path.parents for root in allowed_roots):
            raise PermissionError(
                "runtime read escaped sealed execution/private roots: %s" % path)
        _READ_POLICY["observed"].add(str(path))


sys.addaudithook(_audit_open)


class RuntimeReadGuard:
    def __init__(self, roots, files=()):
        self.roots = tuple(Path(value).resolve() for value in roots)
        self.files = {Path(value).resolve() for value in files}

    def __enter__(self):
        with _READ_POLICY_LOCK:
            if _READ_POLICY["active"]:
                raise RuntimeError("nested runtime read guard")
            _READ_POLICY.update({
                "active": True,
                "allowed_roots": self.roots,
                "allowed_files": self.files,
                "observed": set(),
            })
            return _READ_POLICY["observed"]

    def __exit__(self, exc_type, exc, traceback):
        with _READ_POLICY_LOCK:
            _READ_POLICY.update({
                "active": False,
                "allowed_roots": (),
                "allowed_files": set(),
                "observed": set(),
            })
        return False


def portable_runtime_read_trace(trace, execution_root, private_root,
                                d21_path):
    """Replace job-specific absolute paths by stable, sealed logical roles.

    Python audit hooks do not intercept arbitrary native ``libc.open`` calls;
    this is therefore a diagnostic/census, not the data-loader trust boundary.
    The explicit restricted D21 loader and systemd's inaccessible ambient temp
    paths are the enforcement layers.  Process-global state still ensures a
    Python thread cannot silently bypass the diagnostic.
    """
    execution_root = Path(execution_root).resolve(strict=True)
    private_root = Path(private_root).resolve(strict=True)
    d21_path = Path(d21_path).resolve(strict=True)
    logical = []
    for value in sorted(trace):
        path = Path(value).resolve(strict=True)
        if path == d21_path:
            item = "job-private/directionb_tails_D21.pkl"
        else:
            try:
                item = "execution/" + str(path.relative_to(execution_root))
            except ValueError:
                try:
                    item = "job-private/" + str(path.relative_to(private_root))
                except ValueError as error:
                    raise RuntimeError(
                        "runtime read trace escaped registered roots") from error
        logical.append(item)
    if len(logical) != len(set(logical)):
        raise RuntimeError("runtime read trace logical-path collision")
    return sorted(logical)


_ORIGINAL_PREPARE = BASE.prepare_d43_context
_ACTIVE_D21 = None
_ACTIVE_CORE23 = None


def _dependency_hashes_v3(certificate_path, p2_reference_path):
    if _ACTIVE_D21 is None or _ACTIVE_CORE23 is None:
        raise RuntimeError("v3 sealed data paths are not active")
    result = {
        "adapter:v3": {"path": str(Path(__file__).resolve()),
                        "sha256": sha256_path(__file__)},
        "adapter:v2-core": {
            "path": str(Path(BASE.__file__).resolve()),
            "sha256": sha256_path(BASE.__file__)},
        "data:directionb_tails_D21.private": {
            "path": str(Path(_ACTIVE_D21).resolve()),
            "sha256": sha256_path(_ACTIVE_D21)},
        "data:directionb_core23_p105337.ms": {
            "path": str(Path(_ACTIVE_CORE23).resolve()),
            "sha256": sha256_path(_ACTIVE_CORE23)},
    }
    original = BASE._dependency_hashes_v2_original(
        certificate_path, p2_reference_path)
    # The historical function names its own adapter; retain it under a clear
    # key while making the v3 adapter the route entry point.
    result.update(original)
    return result


if not hasattr(BASE, "_dependency_hashes_v2_original"):
    BASE._dependency_hashes_v2_original = BASE._dependency_hashes
BASE._dependency_hashes = _dependency_hashes_v3


def prepare_d43_context(certificate_path, p2_reference_path,
                        prime=PRIME, *, d21_path=None, core23_path=None,
                        expected_d21_sha256=EXPECTED_D21_SHA256,
                        expected_core23_sha256=EXPECTED_CORE23_SHA256,
                        execution_root=None):
    global _ACTIVE_D21, _ACTIVE_CORE23
    if "DIRECTIONB_STATE" in os.environ:
        raise RuntimeError("ambient DIRECTIONB_STATE is forbidden")
    if d21_path is None or core23_path is None:
        raise ValueError("v3 requires explicit D21 and core23 paths")
    raw_d21, raw_core23 = Path(d21_path), Path(core23_path)
    if raw_d21.is_symlink() or raw_core23.is_symlink():
        raise ValueError("symlinked Direction-B inputs are forbidden")
    d21_path = raw_d21.resolve(strict=True)
    core23_path = raw_core23.resolve(strict=True)
    execution_root = Path(execution_root or ROOT).resolve(strict=True)
    expected_core_path = execution_root / \
        "cases/directionb_core23_p105337.ms"
    if core23_path != expected_core_path:
        raise ValueError("core23 must be the canonical sealed execution copy")
    if sha256_path(core23_path) != expected_core23_sha256:
        raise ValueError("sealed core23 hash mismatch")
    _ACTIVE_D21, _ACTIVE_CORE23 = str(d21_path), str(core23_path)

    # Import the real stack before activating the runtime data-open guard;
    # module bytes and the NumPy environment are independently pinned by the
    # supervisor.  No Direction-B loader is called by these imports.
    import d43_char0_lift  # noqa: F401
    safe_loader = install_sealed_directionb_loaders(
        d21_path, expected_d21_sha256)

    private_root = d21_path.parent
    allowed_files = {core23_path, d21_path,
                     Path(certificate_path).resolve(),
                     Path(p2_reference_path).resolve()}
    with RuntimeReadGuard((execution_root, private_root), allowed_files) as reads:
        context = _ORIGINAL_PREPARE(
            os.fspath(certificate_path), os.fspath(p2_reference_path), prime)
    dependencies = context["dependency_hashes"]
    if dependencies["data:directionb_tails_D21.private"]["sha256"] != \
            EXPECTED_D21_SHA256:
        raise ValueError("semantic dependency D21 hash drift")
    if dependencies["data:directionb_core23_p105337.ms"]["sha256"] != \
            EXPECTED_CORE23_SHA256:
        raise ValueError("semantic dependency core23 hash drift")
    trace = portable_runtime_read_trace(
        reads, execution_root, private_root, d21_path)
    context["invariants"]["sealed_directionb_loader"] = safe_loader
    context["invariants"]["runtime_read_trace"] = {
        "paths": trace,
        "paths_sha256": sha256_json(trace),
        "policy": (
            "process-global-python-open-diagnostic; explicit sealed D21 "
            "loader and systemd inaccessible temp paths enforce custody"),
        "ambient_tmp_reads": [path for path in trace
                              if path == "job-private/tmp" or
                              path.startswith("job-private/tmp/")],
    }
    if context["invariants"]["runtime_read_trace"]["ambient_tmp_reads"]:
        raise RuntimeError("ambient /tmp read escaped v3 loader")
    return context


BASE.prepare_d43_context = prepare_d43_context


def _imds_get(path, token, timeout=2.0):
    request = urllib.request.Request(
        "http://169.254.169.254/latest/" + path.lstrip("/"),
        headers={"X-aws-ec2-metadata-token": token})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read().decode().strip()


def live_ec2_identity_and_tag(tag_key=AUTHORIZATION_TAG_KEY, timeout=2.0):
    if platform.system() != "Linux":
        raise RuntimeError("p^3+ is restricted to Linux EC2")
    vendor = Path("/sys/class/dmi/id/sys_vendor").read_text().strip()
    if vendor != "Amazon EC2":
        raise RuntimeError("p^3+ is restricted to Amazon EC2")
    request = urllib.request.Request(
        "http://169.254.169.254/latest/api/token", data=b"", method="PUT",
        headers={"X-aws-ec2-metadata-token-ttl-seconds": "60"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        token = response.read().decode().strip()
    document = json.loads(_imds_get(
        "dynamic/instance-identity/document", token, timeout))
    tag_value = _imds_get(
        "meta-data/tags/instance/" + urllib.parse.quote(tag_key, safe=""),
        token, timeout)
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
    return identity, {"key": tag_key, "value": tag_value}


def _load_envelope(path):
    value = json.loads(Path(path).read_text())
    if set(value) != {"payload", "payload_sha256"}:
        raise RuntimeError("authorization envelope shape drift")
    if sha256_json(value["payload"]) != value["payload_sha256"]:
        raise RuntimeError("authorization envelope payload hash drift")
    return value["payload"]


def sanitized_environment_snapshot(*, normalized=True):
    unexpected = set(os.environ) - ALLOWED_ENVIRONMENT_KEYS
    if unexpected:
        raise RuntimeError("runner inherited nonallowlisted environment: %s" %
                           sorted(unexpected))
    present_injection = INJECTION_VARIABLES & set(os.environ)
    if present_injection:
        raise RuntimeError("runner inherited injection variables: %s" %
                           sorted(present_injection))
    environment = {key: os.environ[key] for key in sorted(os.environ)}
    if environment.get("SHLVL") != "0":
        raise RuntimeError("sealed child SHLVL must be exactly zero")
    marker_path = environment.get("JC2_D43_HENSEL_AWS_AUTH")
    marker_sha = environment.get("JC2_D43_HENSEL_AWS_AUTH_SHA256")
    if marker_path is not None:
        if not Path(marker_path).is_absolute():
            raise RuntimeError("AWS marker path must be absolute")
        if not is_sha256(marker_sha):
            raise RuntimeError("AWS marker hash is malformed")
        if normalized:
            environment["JC2_D43_HENSEL_AWS_AUTH"] = AUTH_PATH_SENTINEL
            environment["JC2_D43_HENSEL_AWS_AUTH_SHA256"] = AUTH_SHA_SENTINEL
    return environment


def validate_aws_lane_authorization(target_exponent, state_path,
                                    report_path):
    if target_exponent <= 2:
        return None
    if target_exponent not in AWS_TARGET_TAGS:
        raise RuntimeError("AWS route permits only target exponents 16 and 64")
    marker_path = os.environ.get("JC2_D43_HENSEL_AWS_AUTH", "")
    marker_sha = os.environ.get("JC2_D43_HENSEL_AWS_AUTH_SHA256", "")
    if not marker_path or not is_sha256(marker_sha):
        raise RuntimeError("p^3+ requires a v3 authorization marker")
    marker_path = Path(marker_path).resolve(strict=True)
    if sha256_path(marker_path) != marker_sha:
        raise RuntimeError("v3 authorization marker file hash mismatch")
    marker = _load_envelope(marker_path)
    required = {
        "schema", "target_exponent", "lane_tag", "job_id",
        "host_identity", "live_authorization_tag",
        "launch_authorization_path", "launch_authorization_sha256",
        "review_report_path", "review_report_sha256", "payload_manifest_path",
        "payload_manifest_sha256", "preregistration_path",
        "preregistration_sha256", "runner_sha256", "base_runner_sha256",
        "supervisor_path", "supervisor_sha256", "worker_path",
        "worker_sha256", "execution_root", "source_archive_path",
        "source_archive_sha256",
        "runtime_environment", "runtime_environment_sha256",
        "runtime_receipt_sha256",
        "job_identity_sha256", "supervisor_pid", "state_path",
        "report_path", "d21_private_path", "d21_private_sha256",
        "core23_path", "core23_sha256", "target16_provenance",
        "claims_forbidden_sha256",
    }
    if set(marker) != required or marker.get("schema") != AWS_AUTH_SCHEMA:
        raise RuntimeError("v3 authorization marker schema drift")
    for key in SHA_KEYS:
        if not is_sha256(marker.get(key)):
            raise RuntimeError("v3 marker malformed hash: %s" % key)
    if marker["target_exponent"] != target_exponent or \
            marker["lane_tag"] != AWS_TARGET_TAGS[target_exponent]:
        raise RuntimeError("v3 authorization target/tag mismatch")
    if marker["runner_sha256"] != sha256_path(__file__) or \
            marker["base_runner_sha256"] != sha256_path(BASE.__file__):
        raise RuntimeError("v3 runner byte binding mismatch")
    if sha256_path(marker["supervisor_path"]) != marker["supervisor_sha256"] or \
            sha256_path(marker["worker_path"]) != marker["worker_sha256"]:
        raise RuntimeError("v3 supervisor/worker byte binding mismatch")
    for path_key, hash_key in (
            ("review_report_path", "review_report_sha256"),
            ("payload_manifest_path", "payload_manifest_sha256"),
            ("preregistration_path", "preregistration_sha256"),
            ("source_archive_path", "source_archive_sha256")):
        if sha256_path(marker[path_key]) != marker[hash_key]:
            raise RuntimeError("v3 marker artifact binding mismatch: %s" %
                               path_key)
    if marker["claims_forbidden_sha256"] != sha256_json(
            list(FORBIDDEN_CLAIMS)):
        raise RuntimeError("v3 claims firewall mismatch")
    if marker["state_path"] != str(Path(state_path).resolve()) or \
            marker["report_path"] != str(Path(report_path or "").resolve()):
        raise RuntimeError("v3 durable path binding mismatch")
    expected_job_identity = sha256_json({
        "authorization_sha256": marker["launch_authorization_sha256"],
        "identity": marker["host_identity"], "job_id": marker["job_id"],
        "target": marker["target_exponent"],
        "source_archive_sha256": marker["source_archive_sha256"],
        "target16_provenance": marker["target16_provenance"],
    })
    if marker["job_identity_sha256"] != expected_job_identity:
        raise RuntimeError("v3 job identity binding mismatch")
    if marker["supervisor_pid"] != os.getppid():
        raise RuntimeError("v3 supervisor parent binding mismatch")
    if marker["d21_private_sha256"] != EXPECTED_D21_SHA256 or \
            marker["core23_sha256"] != EXPECTED_CORE23_SHA256:
        raise RuntimeError("v3 sealed Direction-B input binding mismatch")
    if sha256_path(marker["d21_private_path"]) != EXPECTED_D21_SHA256 or \
            sha256_path(marker["core23_path"]) != EXPECTED_CORE23_SHA256:
        raise RuntimeError("v3 sealed Direction-B input byte drift")

    authorization_path = Path(
        marker["launch_authorization_path"]).resolve(strict=True)
    if sha256_path(authorization_path) != marker[
            "launch_authorization_sha256"]:
        raise RuntimeError("external launch authorization byte drift")
    authorization = json.loads(authorization_path.read_text())
    if authorization.get("schema") != LAUNCH_AUTH_SCHEMA or \
            authorization.get("status") != \
            "COORDINATOR_AUTHORIZED_AFTER_INDEPENDENT_REVIEW_PASS":
        raise RuntimeError("external launch authorization is not active")
    live_identity, live_tag = live_ec2_identity_and_tag()
    if live_tag != marker["live_authorization_tag"] or \
            live_tag["value"] != marker["launch_authorization_sha256"]:
        raise RuntimeError("live EC2 authorization tag mismatch")
    if live_identity != marker["host_identity"] or \
            authorization.get("expected_host_identity") != live_identity:
        raise RuntimeError("live EC2 identity binding mismatch")
    auth_bindings = {
        "job_id": marker["job_id"],
        "target_exponent": target_exponent,
        "lane_tag": marker["lane_tag"],
        "payload_manifest_sha256": marker["payload_manifest_sha256"],
        "preregistration_sha256": marker["preregistration_sha256"],
        "runner_sha256": marker["runner_sha256"],
        "base_runner_sha256": marker["base_runner_sha256"],
        "supervisor_sha256": marker["supervisor_sha256"],
        "worker_sha256": marker["worker_sha256"],
        "runtime_environment_sha256": marker["runtime_environment_sha256"],
        "runtime_receipt_sha256": marker["runtime_receipt_sha256"],
        "review_report_sha256": marker["review_report_sha256"],
        "source_archive_sha256": marker["source_archive_sha256"],
        "claims_forbidden_sha256": marker["claims_forbidden_sha256"],
        "d21_private_sha256": marker["d21_private_sha256"],
        "core23_sha256": marker["core23_sha256"],
        "target16_provenance": marker["target16_provenance"],
    }
    if authorization.get("bindings") != auth_bindings:
        raise RuntimeError("external launch authorization binding drift")
    environment = sanitized_environment_snapshot(normalized=True)
    if environment != marker["runtime_environment"] or \
            sha256_json(environment) != marker["runtime_environment_sha256"]:
        raise RuntimeError("sanitized runner environment binding mismatch")
    if target_exponent == 16 and marker["target16_provenance"] is not None:
        raise RuntimeError("target 16 must not carry continuation provenance")
    if target_exponent == 64:
        provenance = marker["target16_provenance"]
        required_provenance = {
            "terminal_archive_sha256", "terminal_manifest_sha256",
            "terminal_authority_sha256", "job_identity_sha256",
            "state_envelope_sha256", "state_payload_sha256",
            "history_sha256", "achieved_exponent",
            "authorization_sha256", "runtime_environment_sha256",
        }
        if not isinstance(provenance, dict) or \
                set(provenance) != required_provenance or \
                provenance["achieved_exponent"] != 16 or \
                any(not is_sha256(provenance[key])
                    for key in required_provenance - {"achieved_exponent"}):
            raise RuntimeError("target-64 provenance binding is incomplete")
    return marker


BASE.validate_aws_lane_authorization = validate_aws_lane_authorization


# Re-export arithmetic/state helpers used by sealed tests and independent
# review fixtures.
for _name in (
        "factor_matrix", "solve_factored", "apply_digits", "coordinate_key",
        "tail_census", "structural_dead_tail_gate", "template_relation_gate",
        "source_rows_with_x", "lift_root_frame_digit", "lift_one_point_digit",
        "validate_resume_payload", "replay_semantic_chain", "write_state",
        "load_state", "_initial_payload", "_frame_from_payload",
        "_seal_history_record", "REGISTERED_P2_W1", "REGISTERED_P2_W2",
        "REGISTERED_P2_TEMPLATE_GATE_SHA256", "DEAD_TAIL_LABELS"):
    globals()[_name] = getattr(BASE, _name)


def run(target_exponent, state_path, certificate_path, p2_reference_path,
        report_path=None, preflight_only=False, validate_state_only=False,
        *, d21_path, core23_path, execution_root):
    global _ACTIVE_D21, _ACTIVE_CORE23
    _ACTIVE_D21 = str(Path(d21_path).resolve())
    _ACTIVE_CORE23 = str(Path(core23_path).resolve())

    def bound_prepare(certificate, reference, prime=PRIME):
        return prepare_d43_context(
            certificate, reference, prime, d21_path=_ACTIVE_D21,
            core23_path=_ACTIVE_CORE23, execution_root=execution_root)

    BASE.prepare_d43_context = bound_prepare
    if validate_state_only:
        lane = validate_aws_lane_authorization(
            target_exponent, state_path, report_path)
        with BASE.exclusive_state_lock(state_path):
            context = bound_prepare(certificate_path, p2_reference_path)
            payload = load_state(state_path)
            validate_resume_payload(payload, context)
            if int(payload["exponent"]) > target_exponent:
                raise ValueError("validated state exceeds authorized target")
            report = {
                "status": "SEMANTIC_STATE_CHAIN_VALID",
                "scope": SCOPE, "prime": payload["prime"],
                "validated_exponent": payload["exponent"],
                "authorized_target_exponent": target_exponent,
                "state_payload_sha256": sha256_json(payload),
                "history_sha256": payload["history_sha256"],
                "necessary_template_relation_gate": payload[
                    "template_relation_gate"],
                "claims_certified": CERTIFIED_CLAIM,
                "exact_relations_replayed": list(EXACT_RELATIONS_REPLAYED),
                "upstream_not_replayed": list(UPSTREAM_NOT_REPLAYED),
                "claims_forbidden": list(FORBIDDEN_CLAIMS),
                "aws_lane": lane,
            }
            if report_path:
                BASE._atomic_json(report_path, report)
            return report
    return BASE.run(target_exponent, state_path, certificate_path,
                    p2_reference_path, report_path, preflight_only,
                    validate_state_only)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--target-exponent", type=int, default=16)
    parser.add_argument("--state", required=False)
    parser.add_argument("--certificate", required=False)
    parser.add_argument("--p2-reference", required=False)
    parser.add_argument("--d21-private", required=False)
    parser.add_argument("--core23", required=False)
    parser.add_argument("--execution-root", required=False)
    parser.add_argument("--report", default=None)
    parser.add_argument("--preflight-only", action="store_true")
    parser.add_argument("--validate-state-only", action="store_true")
    parser.add_argument("--selftest", action="store_true")
    arguments = parser.parse_args()
    if arguments.selftest:
        result = BASE.fixture_selftest()
    else:
        required = (arguments.state, arguments.certificate,
                    arguments.p2_reference, arguments.d21_private,
                    arguments.core23, arguments.execution_root)
        if not all(required):
            parser.error("v3 run paths are all required")
        result = run(
            arguments.target_exponent, arguments.state,
            arguments.certificate, arguments.p2_reference,
            arguments.report, arguments.preflight_only,
            arguments.validate_state_only,
            d21_path=arguments.d21_private, core23_path=arguments.core23,
            execution_root=arguments.execution_root)
    print(json.dumps(result, indent=1, sort_keys=True))


if __name__ == "__main__":
    main()
