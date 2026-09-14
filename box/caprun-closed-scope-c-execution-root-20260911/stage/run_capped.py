#!/usr/bin/env python3
"""Run one argv-only command under the CAPRUN/v1 lifecycle contract.

The runner is intentionally opt-in.  It does not invoke a shell, inspect
process names, or migrate any existing supervisor.  Child stdin is DEVNULL
unless ``--stdin-file`` names a regular file.  Output and telemetry paths are
regular files opened without following symlinks. This guarded Linux snapshot
REQUIRES a ROOT-registered closed cgroup-v2 child leaf. Kernel populated=0,
after positive trusted pre-exec placement, is necessary for completion.
Process scans measure RSS; their apparent emptiness is not completion proof.
The old unguarded snapshot is historical and is not silently migrated.

CPU enforcement is an inherited per-process RLIMIT_CPU.  A CPU-cap outcome is
reported only when the registered child is observed to die from SIGXCPU.
RSS enforcement samples the aggregate resident set of non-zombie processes in
the exact registered PGID; the sampling interval permits bounded overshoot and
is recorded in telemetry.  No address-space limit is mislabeled as an RSS cap.
"""

from __future__ import annotations

import argparse
import datetime as _datetime
import hashlib
import json
import os
from pathlib import Path
import signal
import stat
import subprocess
import sys
import time
from dataclasses import dataclass
from typing import Any, BinaryIO, Dict, List, Optional, Sequence, Tuple

try:
    import resource
except ImportError:  # pragma: no cover - CAPRUN/v1 is POSIX-only.
    resource = None  # type: ignore


SCHEMA = "CAPRUN/v1"
RUNNER_FAILURE_EXIT = 70
WALL_TIMEOUT_EXIT = 124
RESOURCE_CAP_EXIT = 125
DEFAULT_RSS_SAMPLE_SECONDS = 0.05
DEFAULT_LIFECYCLE_SAMPLE_SECONDS = 1.0
POST_KILL_OBSERVE_SECONDS = 1.0
SIGXCPU = getattr(signal, "SIGXCPU", None)
_CLOSED_SCOPE = None  # One CLI invocation, single-threaded; never a fallback.


class RunnerError(RuntimeError):
    """A fail-closed runner or identity error."""


class ForwardedSignal(BaseException):
    """Raised in the main thread when the runner receives a handled signal."""

    def __init__(self, signum: int) -> None:
        super().__init__(signum)
        self.signum = signum


@dataclass
class SignalLatch:
    """Defer a handled signal until Popen has been assigned safely."""

    pending: Optional[int] = None
    armed: bool = False

    def handler(self, signum, _frame) -> None:
        if self.armed:
            raise ForwardedSignal(signum)
        if self.pending is None:
            self.pending = signum

    def arm(self) -> None:
        self.armed = True
        if self.pending is not None:
            raise ForwardedSignal(self.pending)


@dataclass(frozen=True)
class ProcessIdentity:
    pid: int
    pgid: int
    start_identity: str
    source: str


@dataclass(frozen=True)
class GroupSample:
    live_pids: Tuple[int, ...]
    zombie_pids: Tuple[int, ...]
    rss_bytes: int


@dataclass(frozen=True)
class CleanupResult:
    term_sent: bool
    kill_sent: bool
    final_sample: GroupSample
    leader_reaped: bool
    kernel_quiet: bool = False

    @property
    def complete(self) -> bool:
        return self.leader_reaped and self.kernel_quiet and not self.final_sample.live_pids


@dataclass
class OpenedFile:
    path: Path
    stream: BinaryIO
    device: int
    inode: int


def utc_now() -> str:
    return _datetime.datetime.now(_datetime.timezone.utc).isoformat().replace(
        "+00:00", "Z"
    )


def positive_float(text: str) -> float:
    try:
        value = float(text)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("must be a positive number") from exc
    if not value > 0.0 or value == float("inf"):
        raise argparse.ArgumentTypeError("must be a finite positive number")
    return value


def positive_int(text: str) -> int:
    try:
        value = int(text)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("must be a positive integer") from exc
    if value <= 0:
        raise argparse.ArgumentTypeError("must be a positive integer")
    return value


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    for name in ("child", "outer"):
        result.add_argument("--closed-" + name + "-cgroup", required=True)
        result.add_argument("--closed-" + name + "-device", required=True, type=positive_int)
        result.add_argument("--closed-" + name + "-inode", required=True, type=positive_int)
    result.add_argument("--closed-boot-id", required=True)
    result.add_argument("--closed-pid-namespace", required=True)
    result.add_argument("--wall-seconds", required=True, type=positive_float)
    result.add_argument("--cpu-seconds", type=positive_int)
    result.add_argument("--rss-bytes", type=positive_int)
    result.add_argument(
        "--rss-sample-seconds",
        type=positive_float,
        default=DEFAULT_RSS_SAMPLE_SECONDS,
    )
    result.add_argument(
        "--lifecycle-sample-seconds",
        type=positive_float,
        default=DEFAULT_LIFECYCLE_SAMPLE_SECONDS,
        help="exact-PGID completion sampling interval when RSS is disabled",
    )
    result.add_argument(
        "--term-grace-seconds", type=positive_float, default=1.0
    )
    result.add_argument("--stdin-file")
    result.add_argument("--stdout-file", required=True)
    result.add_argument("--stderr-file", required=True)
    result.add_argument("--telemetry-file", required=True)
    result.add_argument("--cwd", default=os.getcwd())
    result.add_argument(
        "--overwrite",
        action="store_true",
        help="replace existing regular output/telemetry files",
    )
    result.add_argument(
        "command",
        nargs=argparse.REMAINDER,
        help="argv after --; no shell parsing is performed",
    )
    return result


def absolute_path(text: str) -> Path:
    return Path(os.path.abspath(os.path.expanduser(text)))


def canonical_argv_hash(argv: Sequence[str]) -> str:
    payload = json.dumps(
        list(argv), ensure_ascii=False, separators=(",", ":")
    ).encode("utf-8") + b"\n"
    return hashlib.sha256(payload).hexdigest()


class ClosedChildScope:
    """ROOT-exclusive immutable leaf; no root concurrency, migration or delegation.

    Only the trusted preexec closure writes cgroup.procs, before executing
    setpriv/workload. The attestation pipe is closed before exec. No cgroup
    descriptor reaches the workload. All resource enforcement remains outer.
    """

    def __init__(self, args):
        if sys.platform != "linux" or os.geteuid() != 0:
            raise RunnerError("closed child scope requires ROOT Linux")
        if len(os.listdir('/proc/self/task')) != 1:
            raise RunnerError("closed preexec requires one thread")
        self.child = Path(args.closed_child_cgroup)
        self.outer = Path(args.closed_outer_cgroup)
        self.child_id = (args.closed_child_device, args.closed_child_inode)
        self.outer_id = (args.closed_outer_device, args.closed_outer_inode)
        self.boot = args.closed_boot_id
        self.namespace = args.closed_pid_namespace
        self.placed = False
        self.attestation = None
        self.last_observation = None
        self.empty_ps_while_populated = 0
        self.validate()
        if self.membership() != self.relative(self.outer):
            raise RunnerError("CAPRUN must remain in registered outer cgroup")
        if self.population() != 0:
            raise RunnerError("closed child scope not initially empty")

    @staticmethod
    def relative(p):
        return '0::' + str(p)[len('/sys/fs/cgroup'):]

    @staticmethod
    def membership():
        return Path('/proc/self/cgroup').read_text(encoding='ascii').strip()

    def validate(self):
        if self.child.parent != self.outer or not str(self.outer).startswith('/sys/fs/cgroup/'):
            raise RunnerError("closed scope must be direct child of owned outer")
        mounts = Path('/proc/self/mountinfo').read_text(encoding='ascii').splitlines()
        if not any(line.split(' - ', 1)[0].split()[4] == '/sys/fs/cgroup'
                   and line.split(' - ', 1)[1].split()[0] == 'cgroup2' for line in mounts):
            raise RunnerError("canonical cgroup2 mount required")
        if Path('/proc/sys/kernel/random/boot_id').read_text().strip() != self.boot or os.readlink('/proc/self/ns/pid') != self.namespace:
            raise RunnerError("closed scope boot/namespace changed")
        for p, expected in ((self.outer, self.outer_id), (self.child, self.child_id)):
            if not p.is_absolute() or p.resolve() != p or p.is_symlink():
                raise RunnerError("closed scope canonical path")
            st = p.stat()
            if (st.st_dev, st.st_ino) != expected or st.st_uid != 0 or st.st_mode & 0o022 or not stat.S_ISDIR(st.st_mode):
                raise RunnerError("closed scope identity/owner changed")
            if (p / 'cgroup.type').read_text().strip() != 'domain' or (p / 'cgroup.subtree_control').read_text().strip():
                raise RunnerError("closed scope requires domain with no child controllers")
            for name in ('cgroup.procs', 'cgroup.threads', 'cgroup.subtree_control', 'cgroup.events'):
                f = p / name
                st = f.lstat()
                if not stat.S_ISREG(st.st_mode) or st.st_uid != 0 or st.st_mode & 0o022:
                    raise RunnerError("closed scope writable/delegated interface")
        if any(p.is_dir() for p in self.child.iterdir()):
            raise RunnerError("registered child must remain a leaf")

    def population(self):
        self.validate()
        raw = (self.child / 'cgroup.events').read_text(encoding='ascii')
        if len(raw) > 4096:
            raise RunnerError("closed scope event byte cap")
        fields = {}
        for line in raw.splitlines():
            parts = line.split()
            if len(parts) != 2 or parts[0] in fields:
                raise RunnerError("malformed closed scope events")
            fields[parts[0]] = parts[1]
        if fields.get('populated') not in ('0', '1'):
            raise RunnerError("missing closed scope population")
        value = int(fields['populated'])
        self.last_observation = {'utc': utc_now(), 'monotonic': time.monotonic(), 'populated': value}
        return value

    def quiet(self, require_placement=True):
        if require_placement and not self.placed:
            raise RunnerError("closed scope placement not attested")
        return self.population() == 0

    def preexec(self, cpu_limit, reader, writer):
        def attach():
            os.close(reader)
            self.validate()
            if self.membership() != self.relative(self.outer) or self.population() != 0:
                raise RunnerError("closed preexec origin/empty scope mismatch")
            fd = os.open(self.child / 'cgroup.procs', os.O_WRONLY | os.O_CLOEXEC | os.O_NOFOLLOW)
            try:
                raw = str(os.getpid()).encode('ascii')
                if os.write(fd, raw) != len(raw):
                    raise RunnerError("closed preexec short placement write")
            finally:
                os.close(fd)
            if self.membership() != self.relative(self.child) or self.population() != 1:
                raise RunnerError("closed preexec membership not established")
            ident = linux_identity(os.getpid())
            if ident is None or ident.pgid != ident.pid:
                raise RunnerError("closed preexec session identity")
            if cpu_limit is not None:
                cpu_limit()
            record = {'pid': ident.pid, 'pgid': ident.pgid, 'start_identity': ident.start_identity,
                      'cgroup': self.relative(self.child), 'boot_id': self.boot,
                      'pid_namespace': self.namespace, 'device': self.child_id[0], 'inode': self.child_id[1]}
            raw = json.dumps(record, sort_keys=True, separators=(',', ':')).encode('ascii')
            if len(raw) > 2048 or os.write(writer, raw) != len(raw):
                raise RunnerError("closed placement attestation write")
            os.close(writer)
        return attach

    def attest(self, reader, process):
        os.set_blocking(reader, False)
        raw = os.read(reader, 2049)
        if not raw or len(raw) > 2048:
            raise RunnerError("missing/bounded closed placement attestation")
        obj = json.loads(raw)
        ident = linux_identity(process.pid)
        expected = None if ident is None else {
            'pid': ident.pid, 'pgid': ident.pgid, 'start_identity': ident.start_identity,
            'cgroup': self.relative(self.child), 'boot_id': self.boot,
            'pid_namespace': self.namespace, 'device': self.child_id[0], 'inode': self.child_id[1]}
        if obj != expected or obj['pid'] != process.pid or obj['pgid'] != process.pid:
            raise RunnerError("closed placement identity mismatch")
        if (Path('/proc') / str(process.pid) / 'cgroup').read_text().strip() != self.relative(self.child):
            raise RunnerError("closed leader migrated")
        self.attestation = obj
        self.placed = True

    def record(self):
        return {'schema': 'CAPRUN-closed-child/v1', 'path': str(self.child),
                'device': self.child_id[0], 'inode': self.child_id[1],
                'outer_path': str(self.outer), 'outer_device': self.outer_id[0],
                'outer_inode': self.outer_id[1], 'placement_attested': self.placed,
                'attestation': self.attestation, 'last_observation': self.last_observation,
                'empty_ps_while_populated': self.empty_ps_while_populated}


def scope_quiet(require_placement=False):
    if _CLOSED_SCOPE is None:
        raise RunnerError("required closed scope missing")
    return _CLOSED_SCOPE.quiet(require_placement)


def reap_if_closed(process):
    # Never discard the unreaped leader anchor while a live descendant remains.
    if not scope_quiet():
        return False
    try:
        process.wait(timeout=POST_KILL_OBSERVE_SECONDS)
        return True
    except subprocess.TimeoutExpired:
        return False


def _safe_flags(base: int) -> int:
    flags = base
    if hasattr(os, "O_CLOEXEC"):
        flags |= os.O_CLOEXEC
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    if hasattr(os, "O_NONBLOCK"):
        # Validation must not block on a FIFO/device before fstat can reject
        # it.  O_NONBLOCK has no effect on ordinary regular-file I/O.
        flags |= os.O_NONBLOCK
    return flags


def open_regular_input(path: Path) -> OpenedFile:
    fd = os.open(str(path), _safe_flags(os.O_RDONLY))
    try:
        info = os.fstat(fd)
        if not stat.S_ISREG(info.st_mode):
            raise RunnerError("--stdin-file must be a regular, non-symlink file")
        stream = os.fdopen(fd, "rb", buffering=0)
    except BaseException:
        os.close(fd)
        raise
    return OpenedFile(path, stream, info.st_dev, info.st_ino)


def open_regular_output(path: Path, overwrite: bool) -> OpenedFile:
    parent = path.parent
    if not parent.is_dir():
        raise RunnerError("output parent directory does not exist: %s" % parent)
    flags = os.O_WRONLY | os.O_CREAT
    if not overwrite:
        flags |= os.O_EXCL
    fd = os.open(str(path), _safe_flags(flags), 0o600)
    try:
        info = os.fstat(fd)
        if not stat.S_ISREG(info.st_mode):
            raise RunnerError("output destination is not a regular file: %s" % path)
        stream = os.fdopen(fd, "wb", buffering=0)
    except BaseException:
        os.close(fd)
        raise
    return OpenedFile(path, stream, info.st_dev, info.st_ino)


def prepare_regular_output(item: OpenedFile) -> None:
    """Truncate only after every input/output inode has been validated."""

    os.ftruncate(item.stream.fileno(), 0)
    item.stream.seek(0)


def ensure_distinct_paths(paths: Sequence[Path]) -> None:
    rendered = [str(path) for path in paths]
    if len(set(rendered)) != len(rendered):
        raise RunnerError("stdin/output/telemetry paths must be distinct")


def ensure_distinct_inodes(files: Sequence[OpenedFile]) -> None:
    identities = [(item.device, item.inode) for item in files]
    if len(set(identities)) != len(identities):
        raise RunnerError("stdin/output/telemetry files must not be hard links")


def hash_opened_output(item: OpenedFile) -> Dict[str, Any]:
    flags = _safe_flags(os.O_RDONLY)
    fd = os.open(str(item.path), flags)
    digest = hashlib.sha256()
    count = 0
    try:
        info = os.fstat(fd)
        if not stat.S_ISREG(info.st_mode):
            raise RunnerError("output changed to a non-regular file: %s" % item.path)
        if (info.st_dev, info.st_ino) != (item.device, item.inode):
            raise RunnerError("output identity changed before hashing: %s" % item.path)
        while True:
            chunk = os.read(fd, 1024 * 1024)
            if not chunk:
                break
            digest.update(chunk)
            count += len(chunk)
    finally:
        os.close(fd)
    return {
        "path": str(item.path),
        "bytes": count,
        "sha256": digest.hexdigest(),
    }


def ps_path() -> str:
    for candidate in ("/bin/ps", "/usr/bin/ps"):
        if os.path.isfile(candidate) and os.access(candidate, os.X_OK):
            return candidate
    raise RunnerError("CAPRUN/v1 requires an absolute ps executable")


def linux_identity(pid: int) -> Optional[ProcessIdentity]:
    proc_stat = Path("/proc") / str(pid) / "stat"
    try:
        raw = proc_stat.read_text(encoding="utf-8")
    except FileNotFoundError:
        return None
    right_paren = raw.rfind(")")
    if right_paren < 0:
        raise RunnerError("malformed /proc process identity for pid %d" % pid)
    fields = raw[right_paren + 2 :].split()
    if len(fields) < 20:
        raise RunnerError("short /proc process identity for pid %d" % pid)
    pgid = int(fields[2])
    start_ticks = fields[19]
    boot_id_path = Path("/proc/sys/kernel/random/boot_id")
    try:
        boot_id = boot_id_path.read_text(encoding="ascii").strip()
    except OSError:
        boot_id = "unavailable"
    return ProcessIdentity(
        pid=pid,
        pgid=pgid,
        start_identity="boot=%s;start_ticks=%s" % (boot_id, start_ticks),
        source="linux-proc-stat-field22",
    )


def ps_identity(pid: int) -> Optional[ProcessIdentity]:
    completed = subprocess.run(
        [ps_path(), "-o", "pid=,pgid=,lstart=", "-p", str(pid)],
        check=False,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=2.0,
    )
    if completed.returncode not in (0, 1):
        raise RunnerError(
            "ps identity query failed with exit %d" % completed.returncode
        )
    line = completed.stdout.strip()
    if not line:
        return None
    fields = line.split(None, 2)
    if len(fields) != 3:
        raise RunnerError("malformed ps process identity for pid %d" % pid)
    observed_pid = int(fields[0])
    if observed_pid != pid:
        raise RunnerError("ps returned the wrong process identity")
    return ProcessIdentity(
        pid=pid,
        pgid=int(fields[1]),
        start_identity=fields[2].strip(),
        source="ps-lstart",
    )


def read_identity(pid: int) -> Optional[ProcessIdentity]:
    if sys.platform.startswith("linux") and Path("/proc").is_dir():
        return linux_identity(pid)
    return ps_identity(pid)


def capture_identity(pid: int) -> ProcessIdentity:
    deadline = time.monotonic() + 1.0
    while True:
        identity = read_identity(pid)
        if identity is not None:
            if identity.pgid != pid:
                raise RunnerError(
                    "new-session invariant failed: pid=%d pgid=%d"
                    % (identity.pid, identity.pgid)
                )
            return identity
        if time.monotonic() >= deadline:
            raise RunnerError("could not capture child start identity")
        time.sleep(0.005)


def validate_identity(
    expected: ProcessIdentity, stage: str, checks: List[Dict[str, Any]]
) -> bool:
    observed = read_identity(expected.pid)
    record: Dict[str, Any] = {"stage": stage, "utc": utc_now()}
    if observed is None:
        record["result"] = "NOT_FOUND"
        checks.append(record)
        return False
    record.update(
        {
            "observed_pid": observed.pid,
            "observed_pgid": observed.pgid,
            "observed_start_identity": observed.start_identity,
            "result": "MATCH" if observed == expected else "MISMATCH",
        }
    )
    checks.append(record)
    if observed != expected:
        raise RunnerError(
            "process identity mismatch before %s; refusing to signal" % stage
        )
    return True


def sample_group(pgid: int) -> GroupSample:
    completed = subprocess.run(
        [ps_path(), "-axo", "pid=,pgid=,rss=,state="],
        check=False,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=2.0,
    )
    if completed.returncode != 0:
        raise RunnerError(
            "ps group query failed with exit %d" % completed.returncode
        )
    live: List[int] = []
    zombies: List[int] = []
    rss_kib = 0
    for line in completed.stdout.splitlines():
        fields = line.split(None, 3)
        if len(fields) != 4:
            continue
        try:
            process_pid = int(fields[0])
            process_pgid = int(fields[1])
            process_rss = int(fields[2])
        except ValueError:
            continue
        if process_pgid != pgid:
            continue
        state_text = fields[3]
        if state_text.startswith("Z"):
            zombies.append(process_pid)
        else:
            live.append(process_pid)
            rss_kib += process_rss
    return GroupSample(tuple(sorted(live)), tuple(sorted(zombies)), rss_kib * 1024)


def send_group_signal(
    expected: ProcessIdentity,
    signum: int,
    stage: str,
    checks: List[Dict[str, Any]],
) -> bool:
    if not validate_identity(expected, stage, checks):
        return False
    try:
        os.killpg(expected.pgid, signum)
    except ProcessLookupError:
        checks.append(
            {"stage": stage + "-send", "utc": utc_now(), "result": "GROUP_GONE"}
        )
        return False
    checks.append(
        {
            "stage": stage + "-send",
            "utc": utc_now(),
            "result": "SENT",
            "signal": signum,
        }
    )
    return True


def wait_for_group_quiet(
    pgid: int,
    seconds: float,
    sample_seconds: float,
    maximum_rss: List[int],
) -> GroupSample:
    deadline = time.monotonic() + seconds
    while True:
        sample = sample_group(pgid)
        maximum_rss[0] = max(maximum_rss[0], sample.rss_bytes)
        if scope_quiet():
            return sample
        remaining = deadline - time.monotonic()
        if remaining <= 0.0:
            return sample
        time.sleep(min(sample_seconds, remaining))


def terminate_group_and_reap(
    process: subprocess.Popen,
    expected: ProcessIdentity,
    grace_seconds: float,
    sample_seconds: float,
    checks: List[Dict[str, Any]],
    maximum_rss: List[int],
) -> CleanupResult:
    initial = sample_group(expected.pgid)
    maximum_rss[0] = max(maximum_rss[0], initial.rss_bytes)
    term_sent = False
    kill_sent = False
    final_before_reap = initial

    if not scope_quiet():
        term_sent = send_group_signal(
            expected, signal.SIGTERM, "before-term", checks
        )
        final_before_reap = wait_for_group_quiet(
            expected.pgid, grace_seconds, sample_seconds, maximum_rss
        )

    if not scope_quiet():
        kill_sent = send_group_signal(
            expected, signal.SIGKILL, "before-kill", checks
        )
        final_before_reap = wait_for_group_quiet(
            expected.pgid,
            POST_KILL_OBSERVE_SECONDS,
            sample_seconds,
            maximum_rss,
        )

    # No wait/poll has competed with this point.  Bound even the authoritative
    # reap: SIGKILL cannot wake an uninterruptible D-state process, so an
    # unbounded wait here would violate every advertised cap.
    leader_reaped = reap_if_closed(process)
    return CleanupResult(
        term_sent, kill_sent, final_before_reap, leader_reaped,
        scope_quiet() and _CLOSED_SCOPE.placed
    )


def terminate_unidentified_spawn_and_reap(
    process: subprocess.Popen,
    grace_seconds: float,
    sample_seconds: float,
    checks: List[Dict[str, Any]],
    maximum_rss: List[int],
) -> CleanupResult:
    """Clean a Popen child when full start-identity capture failed.

    The unreaped Popen handle prevents reuse of its PID.  Because this runner
    requested ``start_new_session=True``, a direct ``getpgid(pid)==pid``
    check is enough to address only that still-owned session's process group.
    This is a bootstrap failure path, not a substitute for normal identity
    validation.
    """

    pid = process.pid
    try:
        pgid = os.getpgid(pid)
    except ProcessLookupError:
        leader_reaped = reap_if_closed(process)
        checks.append(
            {
                "stage": "bootstrap-cleanup",
                "utc": utc_now(),
                "result": "LEADER_GONE_CLOSED_SCOPE_CHECKED",
                "observed_pid": pid,
            }
        )
        return CleanupResult(
            False, False, GroupSample((), (), 0), leader_reaped,
            scope_quiet() and _CLOSED_SCOPE.placed
        )

    if pgid != pid:
        # The exact unreaped PID is still safe, but the promised group is not.
        # Kill only that direct child and fail closed rather than signalling an
        # unvalidated group.
        checks.append(
            {
                "stage": "bootstrap-cleanup",
                "utc": utc_now(),
                "result": "NEW_SESSION_MISMATCH_DIRECT_PID_ONLY",
                "observed_pid": pid,
                "observed_pgid": pgid,
            }
        )
        try:
            # Popen.kill/send_signal may poll/reap internally. Keep the held
            # PID anchor until the closed leaf is kernel-quiet instead.
            os.kill(pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        leader_reaped = reap_if_closed(process)
        return CleanupResult(
            False, False, GroupSample((), (), 0), leader_reaped,
            scope_quiet() and _CLOSED_SCOPE.placed
        )

    checks.append(
        {
            "stage": "bootstrap-cleanup",
            "utc": utc_now(),
            "result": "HELD_UNREAPED_POPEN_AND_NEW_SESSION",
            "observed_pid": pid,
            "observed_pgid": pgid,
        }
    )
    initial = sample_group(pgid)
    maximum_rss[0] = max(maximum_rss[0], initial.rss_bytes)
    term_sent = False
    kill_sent = False
    final_before_reap = initial
    if not scope_quiet():
        try:
            os.killpg(pgid, signal.SIGTERM)
            term_sent = True
        except ProcessLookupError:
            pass
        final_before_reap = wait_for_group_quiet(
            pgid, grace_seconds, sample_seconds, maximum_rss
        )
    if not scope_quiet():
        try:
            os.killpg(pgid, signal.SIGKILL)
            kill_sent = True
        except ProcessLookupError:
            pass
        final_before_reap = wait_for_group_quiet(
            pgid, POST_KILL_OBSERVE_SECONDS, sample_seconds, maximum_rss
        )
    leader_reaped = reap_if_closed(process)
    return CleanupResult(
        term_sent, kill_sent, final_before_reap, leader_reaped,
        scope_quiet() and _CLOSED_SCOPE.placed
    )


def record_cleanup(telemetry: Dict[str, Any], result: CleanupResult) -> None:
    telemetry["termination"].update(
        {
            "term_sent": result.term_sent,
            "kill_sent": result.kill_sent,
            "leader_reaped": result.leader_reaped,
            "cleanup_complete": result.complete,
            "kernel_quiet": result.kernel_quiet,
            "group_live_before_reap": list(result.final_sample.live_pids),
            "group_zombies_before_reap": list(result.final_sample.zombie_pids),
        }
    )


def cpu_preexec(cpu_seconds: Optional[int]):
    if cpu_seconds is None:
        return None
    if (
        resource is None
        or not hasattr(resource, "RLIMIT_CPU")
        or SIGXCPU is None
    ):
        raise RunnerError("--cpu-seconds is unavailable on this platform")
    current_soft, current_hard = resource.getrlimit(resource.RLIMIT_CPU)
    infinity = resource.RLIM_INFINITY
    requested_hard = cpu_seconds + 1
    if current_hard != infinity and current_hard < requested_hard:
        raise RunnerError(
            "existing RLIMIT_CPU hard limit is too low for detectable SIGXCPU"
        )

    def set_cpu_limit() -> None:
        resource.setrlimit(resource.RLIMIT_CPU, (cpu_seconds, requested_hard))

    return set_cpu_limit


def install_signal_handlers() -> Tuple[Dict[int, Any], SignalLatch]:
    previous: Dict[int, Any] = {}
    latch = SignalLatch()

    for signum in (signal.SIGINT, signal.SIGTERM, signal.SIGHUP):
        previous[signum] = signal.getsignal(signum)
        signal.signal(signum, latch.handler)
    return previous, latch


def restore_signal_handlers(previous: Dict[int, Any]) -> None:
    for signum, old_handler in previous.items():
        signal.signal(signum, old_handler)


def ignore_handled_signals(previous: Dict[int, Any]) -> None:
    for signum in previous:
        signal.signal(signum, signal.SIG_IGN)


def close_file(item: Optional[OpenedFile]) -> None:
    if item is not None and not item.stream.closed:
        item.stream.close()


def write_telemetry(item: OpenedFile, payload: Dict[str, Any]) -> None:
    encoded = (
        json.dumps(payload, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    ).encode("utf-8")
    item.stream.write(encoded)
    item.stream.flush()
    os.fsync(item.stream.fileno())


def execute(args: argparse.Namespace, command: Sequence[str]) -> int:
    global _CLOSED_SCOPE
    _CLOSED_SCOPE = None
    invocation_cwd = Path.cwd()
    child_cwd = absolute_path(args.cwd)
    if not child_cwd.is_dir():
        raise RunnerError("--cwd is not a directory: %s" % child_cwd)

    stdout_path = absolute_path(args.stdout_file)
    stderr_path = absolute_path(args.stderr_file)
    telemetry_path = absolute_path(args.telemetry_file)
    input_path = absolute_path(args.stdin_file) if args.stdin_file else None
    all_paths = [stdout_path, stderr_path, telemetry_path]
    if input_path is not None:
        all_paths.append(input_path)
    ensure_distinct_paths(all_paths)

    start_utc = utc_now()
    start_monotonic = time.monotonic()
    telemetry: Dict[str, Any] = {
        "schema": SCHEMA,
        "status": "RUNNER_FAILURE",
        "resource": None,
        "runner_exit_code": RUNNER_FAILURE_EXIT,
        "child_returncode": None,
        "child_exit_code": None,
        "child_signal": None,
        "runner_signal": None,
        "error": None,
        "argv_sha256": canonical_argv_hash(command),
        "argv_count": len(command),
        "executable": command[0],
        "cwd": str(child_cwd),
        "invocation_cwd": str(invocation_cwd),
        "utc_start": start_utc,
        "utc_end": None,
        "wall_elapsed_seconds": None,
        "caps": {
            "wall_seconds": args.wall_seconds,
            "cpu_seconds": args.cpu_seconds,
            "rss_bytes": args.rss_bytes,
            "rss_sample_seconds": args.rss_sample_seconds,
            "lifecycle_sample_seconds": args.lifecycle_sample_seconds,
            "lifecycle_initial_seconds": min(
                DEFAULT_RSS_SAMPLE_SECONDS, args.lifecycle_sample_seconds
            ),
            "term_grace_seconds": args.term_grace_seconds,
        },
        "enforcement": {
            "wall": (
                "monotonic deadline plus exact-PGID lifecycle sampling; "
                "registered leader reaped once after group quiet"
            ),
            "cpu": (
                "per-process-inherited-RLIMIT_CPU; typed only on SIGXCPU"
                if args.cpu_seconds is not None
                else "disabled"
            ),
            "rss": (
                "sampled aggregate non-zombie RSS of exact PGID; overshoot possible"
                if args.rss_bytes is not None
                else "disabled"
            ),
        },
        "stdin": {
            "mode": "regular_file" if input_path is not None else "devnull",
            "path": str(input_path) if input_path is not None else None,
        },
        "stdout": {"path": str(stdout_path), "bytes": None, "sha256": None},
        "stderr": {"path": str(stderr_path), "bytes": None, "sha256": None},
        "telemetry_path": str(telemetry_path),
        "pid": None,
        "pgid": None,
        "start_identity": None,
        "start_identity_source": None,
        "max_observed_group_rss_bytes": 0,
        "identity_checks": [],
        "termination": {
            "reason": None,
            "term_sent": False,
            "kill_sent": False,
            "leader_reaped": False,
            "cleanup_complete": None,
            "group_live_before_reap": [],
            "group_zombies_before_reap": [],
        },
    }

    stdin_opened: Optional[OpenedFile] = None
    stdout_opened: Optional[OpenedFile] = None
    stderr_opened: Optional[OpenedFile] = None
    telemetry_opened: Optional[OpenedFile] = None
    process: Optional[subprocess.Popen] = None
    identity: Optional[ProcessIdentity] = None
    reaped = False
    maximum_rss = [0]
    previous_handlers: Optional[Dict[int, Any]] = None
    signal_latch: Optional[SignalLatch] = None
    previous_sigchld: Any = None
    custody_validated = False
    placement_reader = None
    placement_writer = None

    try:
        # Open the input before any overwrite destination, and do not truncate
        # outputs until hard-link identity checks have passed.  A failed
        # validation must never destroy bytes through an aliased input path.
        if input_path is not None:
            stdin_opened = open_regular_input(input_path)
        telemetry_opened = open_regular_output(telemetry_path, args.overwrite)
        stdout_opened = open_regular_output(stdout_path, args.overwrite)
        stderr_opened = open_regular_output(stderr_path, args.overwrite)
        opened = [telemetry_opened, stdout_opened, stderr_opened]
        if stdin_opened is not None:
            opened.append(stdin_opened)
        ensure_distinct_inodes(opened)
        custody_validated = True
        prepare_regular_output(telemetry_opened)
        prepare_regular_output(stdout_opened)
        prepare_regular_output(stderr_opened)
        _CLOSED_SCOPE = ClosedChildScope(args)
        placement_reader, placement_writer = os.pipe2(os.O_CLOEXEC)

        # An inherited SIGCHLD=SIG_IGN/SA_NOCLDWAIT would auto-reap the
        # registered leader and destroy the zombie identity anchor while a
        # descendant remains.  Force a waitable child for this supervised
        # lifetime, then restore the caller's disposition.
        previous_sigchld = signal.getsignal(signal.SIGCHLD)
        signal.signal(signal.SIGCHLD, signal.SIG_DFL)
        previous_handlers, signal_latch = install_signal_handlers()
        process = subprocess.Popen(
            list(command),
            cwd=str(child_cwd),
            stdin=(stdin_opened.stream if stdin_opened else subprocess.DEVNULL),
            stdout=stdout_opened.stream,
            stderr=stderr_opened.stream,
            shell=False,
            start_new_session=True,
            close_fds=True,
            pass_fds=(placement_reader, placement_writer),
            preexec_fn=_CLOSED_SCOPE.preexec(cpu_preexec(args.cpu_seconds), placement_reader, placement_writer),
        )
        os.close(placement_writer)
        placement_writer = None
        _CLOSED_SCOPE.attest(placement_reader, process)
        os.close(placement_reader)
        placement_reader = None
        # A handled signal delivered inside Popen is latched rather than
        # raised before STORE_FAST assigns the process handle.  From this
        # bytecode boundary onward cleanup can always address that handle.
        signal_latch.arm()
        identity = capture_identity(process.pid)
        telemetry.update(
            {
                "pid": identity.pid,
                "pgid": identity.pgid,
                "start_identity": identity.start_identity,
                "start_identity_source": identity.source,
            }
        )

        deadline = start_monotonic + args.wall_seconds
        termination_reason: Optional[str] = None
        lifecycle_interval = (
            args.rss_sample_seconds
            if args.rss_bytes is not None
            else min(
                DEFAULT_RSS_SAMPLE_SECONDS, args.lifecycle_sample_seconds
            )
        )

        # Keep the unreaped leader as the identity anchor until every live
        # member of its exact PGID is gone.  In particular, do not reap a
        # leader that exits while a same-group descendant is still running:
        # retaining the zombie preserves PID/PGID/start-identity validation
        # for a later bounded TERM/KILL sequence.
        while True:
            sample = sample_group(identity.pgid)
            maximum_rss[0] = max(maximum_rss[0], sample.rss_bytes)
            if scope_quiet(require_placement=True):
                try:
                    process.wait(timeout=POST_KILL_OBSERVE_SECONDS)
                    reaped = True
                except subprocess.TimeoutExpired as error:
                    raise RunnerError(
                        "group was quiet but leader was not reapable"
                    ) from error
                break
            if not sample.live_pids:
                _CLOSED_SCOPE.empty_ps_while_populated += 1
            if (
                args.rss_bytes is not None
                and sample.rss_bytes > args.rss_bytes
            ):
                termination_reason = "rss_cap"
                break
            remaining = deadline - time.monotonic()
            if remaining <= 0.0:
                termination_reason = "wall_timeout"
                break
            time.sleep(min(lifecycle_interval, remaining))
            if args.rss_bytes is None:
                lifecycle_interval = min(
                    args.lifecycle_sample_seconds, lifecycle_interval * 2.0
                )

        if termination_reason is not None:
            telemetry["termination"]["reason"] = termination_reason
            cleanup = terminate_group_and_reap(
                process,
                identity,
                args.term_grace_seconds,
                lifecycle_interval,
                telemetry["identity_checks"],
                maximum_rss,
            )
            reaped = cleanup.leader_reaped
            record_cleanup(telemetry, cleanup)
            if not cleanup.complete:
                telemetry["status"] = "RUNNER_FAILURE"
                telemetry["runner_exit_code"] = RUNNER_FAILURE_EXIT
                telemetry["error"] = (
                    "process group remained live or leader was not reapable "
                    "after bounded SIGKILL observation"
                )
            elif termination_reason == "wall_timeout":
                telemetry["status"] = "WALL_TIMEOUT"
                telemetry["runner_exit_code"] = WALL_TIMEOUT_EXIT
            else:
                telemetry["status"] = "RESOURCE_CAP"
                telemetry["resource"] = "rss"
                telemetry["runner_exit_code"] = RESOURCE_CAP_EXIT

        returncode = process.returncode
        telemetry["child_returncode"] = returncode
        if returncode is not None and returncode >= 0:
            telemetry["child_exit_code"] = returncode
        elif returncode is not None:
            telemetry["child_signal"] = -returncode

        if termination_reason is None:
            if (
                SIGXCPU is not None
                and returncode == -SIGXCPU
                and args.cpu_seconds is not None
            ):
                telemetry["status"] = "RESOURCE_CAP"
                telemetry["resource"] = "cpu"
                telemetry["runner_exit_code"] = RESOURCE_CAP_EXIT
            elif returncode is not None and returncode < 0:
                telemetry["status"] = "SIGNAL"
                telemetry["runner_exit_code"] = min(255, 128 - returncode)
            elif returncode is not None:
                telemetry["status"] = "NORMAL_EXIT"
                telemetry["runner_exit_code"] = returncode
            else:
                raise RunnerError("authoritative reap produced no return code")

    except ForwardedSignal as incoming:
        if previous_handlers is not None:
            ignore_handled_signals(previous_handlers)
        telemetry["runner_signal"] = incoming.signum
        telemetry["termination"]["reason"] = "forwarded_signal"
        if process is not None and identity is None and not reaped:
            try:
                identity = capture_identity(process.pid)
            except BaseException as identity_error:
                telemetry["error"] = (
                    "could not recover child identity after runner signal: %s"
                    % identity_error
                )
            else:
                telemetry.update(
                    {
                        "pid": identity.pid,
                        "pgid": identity.pgid,
                        "start_identity": identity.start_identity,
                        "start_identity_source": identity.source,
                    }
                )
        if process is not None and identity is not None and not reaped:
            try:
                cleanup = terminate_group_and_reap(
                    process,
                    identity,
                    args.term_grace_seconds,
                    (
                        args.rss_sample_seconds
                        if args.rss_bytes is not None
                        else args.lifecycle_sample_seconds
                    ),
                    telemetry["identity_checks"],
                    maximum_rss,
                )
                reaped = cleanup.leader_reaped
                record_cleanup(telemetry, cleanup)
            except BaseException as cleanup_error:
                telemetry["error"] = "signal cleanup failed: %s" % cleanup_error
                telemetry["status"] = "RUNNER_FAILURE"
                telemetry["runner_exit_code"] = RUNNER_FAILURE_EXIT
            else:
                if not cleanup.complete:
                    telemetry["error"] = (
                        "signal cleanup incomplete after bounded SIGKILL"
                    )
                    telemetry["status"] = "RUNNER_FAILURE"
                    telemetry["runner_exit_code"] = RUNNER_FAILURE_EXIT
                else:
                    telemetry["status"] = "SIGNAL"
                    telemetry["runner_exit_code"] = min(
                        255, 128 + incoming.signum
                    )
        elif process is not None and not reaped:
            try:
                cleanup = terminate_unidentified_spawn_and_reap(
                    process,
                    args.term_grace_seconds,
                    (
                        args.rss_sample_seconds
                        if args.rss_bytes is not None
                        else args.lifecycle_sample_seconds
                    ),
                    telemetry["identity_checks"],
                    maximum_rss,
                )
                reaped = cleanup.leader_reaped
                record_cleanup(telemetry, cleanup)
            except BaseException as cleanup_error:
                telemetry["error"] = (
                    (telemetry["error"] + "; ") if telemetry["error"] else ""
                ) + "bootstrap signal cleanup failed: %s" % cleanup_error
                telemetry["status"] = "RUNNER_FAILURE"
                telemetry["runner_exit_code"] = RUNNER_FAILURE_EXIT
            else:
                if not cleanup.complete:
                    telemetry["error"] = (
                        (telemetry["error"] + "; ")
                        if telemetry["error"]
                        else ""
                    ) + (
                        "bootstrap signal cleanup incomplete after bounded SIGKILL"
                    )
                    telemetry["status"] = "RUNNER_FAILURE"
                    telemetry["runner_exit_code"] = RUNNER_FAILURE_EXIT
                else:
                    telemetry["status"] = "SIGNAL"
                    telemetry["runner_exit_code"] = min(
                        255, 128 + incoming.signum
                    )
        else:
            telemetry["status"] = "SIGNAL"
            telemetry["runner_exit_code"] = min(255, 128 + incoming.signum)
        if process is not None:
            telemetry["child_returncode"] = process.returncode
            if process.returncode is not None and process.returncode < 0:
                telemetry["child_signal"] = -process.returncode

    except BaseException as error:
        if previous_handlers is not None:
            ignore_handled_signals(previous_handlers)
        telemetry["error"] = "%s: %s" % (type(error).__name__, error)
        telemetry["status"] = "RUNNER_FAILURE"
        telemetry["runner_exit_code"] = RUNNER_FAILURE_EXIT
        if process is not None and identity is None and not reaped:
            try:
                identity = capture_identity(process.pid)
            except BaseException as identity_error:
                telemetry["error"] += "; identity recovery failed: %s" % (
                    identity_error
                )
            else:
                telemetry.update(
                    {
                        "pid": identity.pid,
                        "pgid": identity.pgid,
                        "start_identity": identity.start_identity,
                        "start_identity_source": identity.source,
                    }
                )
        if process is not None and identity is not None and not reaped:
            try:
                cleanup = terminate_group_and_reap(
                    process,
                    identity,
                    args.term_grace_seconds,
                    (
                        args.rss_sample_seconds
                        if args.rss_bytes is not None
                        else args.lifecycle_sample_seconds
                    ),
                    telemetry["identity_checks"],
                    maximum_rss,
                )
                reaped = cleanup.leader_reaped
                telemetry["termination"]["reason"] = "runner_failure_cleanup"
                record_cleanup(telemetry, cleanup)
                if not cleanup.complete:
                    telemetry["error"] += "; cleanup incomplete after SIGKILL"
            except BaseException as cleanup_error:
                telemetry["error"] += "; cleanup failed: %s" % cleanup_error
        elif process is not None and not reaped:
            try:
                cleanup = terminate_unidentified_spawn_and_reap(
                    process,
                    args.term_grace_seconds,
                    (
                        args.rss_sample_seconds
                        if args.rss_bytes is not None
                        else args.lifecycle_sample_seconds
                    ),
                    telemetry["identity_checks"],
                    maximum_rss,
                )
                reaped = cleanup.leader_reaped
                telemetry["termination"]["reason"] = (
                    "runner_failure_bootstrap_cleanup"
                )
                record_cleanup(telemetry, cleanup)
                if not cleanup.complete:
                    telemetry["error"] += (
                        "; bootstrap cleanup incomplete after SIGKILL"
                    )
            except BaseException as cleanup_error:
                telemetry["error"] += "; bootstrap cleanup failed: %s" % (
                    cleanup_error
                )
        if process is not None:
            telemetry["child_returncode"] = process.returncode

    finally:
        if previous_handlers is not None:
            # Child/group cleanup is complete or has reached its bounded
            # fail-closed limit.  Defer caller handler restoration until
            # hashes and telemetry are durable; a late signal must not tear
            # the custody record halfway through finalization.
            ignore_handled_signals(previous_handlers)
        close_file(stdin_opened)
        close_file(stdout_opened)
        close_file(stderr_opened)
        for fd in (placement_reader, placement_writer):
            if fd is not None:
                os.close(fd)

    # Every outcome, including bootstrap/Popen/preexec errors, records the
    # kernel barrier. A never-attested launch cannot become successful cleanup.
    try:
        quiet = scope_quiet()
        if not quiet or not _CLOSED_SCOPE.placed:
            raise RunnerError("closed scope not quiet and placement-attested at completion")
        telemetry['closed_scope'] = _CLOSED_SCOPE.record()
    except BaseException as guard_error:
        telemetry['closed_scope'] = None if _CLOSED_SCOPE is None else _CLOSED_SCOPE.record()
        telemetry['status'] = 'RUNNER_FAILURE'
        telemetry['runner_exit_code'] = RUNNER_FAILURE_EXIT
        telemetry['error'] = ((telemetry['error'] + '; ') if telemetry['error'] else '') + str(guard_error)

    telemetry["max_observed_group_rss_bytes"] = maximum_rss[0]
    telemetry["utc_end"] = utc_now()
    telemetry["wall_elapsed_seconds"] = round(
        time.monotonic() - start_monotonic, 9
    )

    if custody_validated:
        try:
            if stdout_opened is not None:
                telemetry["stdout"] = hash_opened_output(stdout_opened)
            if stderr_opened is not None:
                telemetry["stderr"] = hash_opened_output(stderr_opened)
        except BaseException as hash_error:
            telemetry["error"] = (
                (telemetry["error"] + "; ") if telemetry["error"] else ""
            ) + "output hashing failed: %s" % hash_error
            telemetry["status"] = "RUNNER_FAILURE"
            telemetry["runner_exit_code"] = RUNNER_FAILURE_EXIT

    if telemetry_opened is None:
        if previous_handlers is not None:
            restore_signal_handlers(previous_handlers)
        if previous_sigchld is not None:
            signal.signal(signal.SIGCHLD, previous_sigchld)
        raise RunnerError("could not open telemetry destination")
    if not custody_validated:
        # The telemetry descriptor may itself alias an input/output inode.
        # Never write through any descriptor before the complete custody set
        # has passed the pairwise identity check.
        close_file(telemetry_opened)
        if previous_handlers is not None:
            restore_signal_handlers(previous_handlers)
        if previous_sigchld is not None:
            signal.signal(signal.SIGCHLD, previous_sigchld)
        print(
            "%s status=RUNNER_FAILURE telemetry=WITHHELD_UNVALIDATED_CUSTODY"
            % SCHEMA,
            flush=True,
        )
        return RUNNER_FAILURE_EXIT
    try:
        write_telemetry(telemetry_opened, telemetry)
    finally:
        close_file(telemetry_opened)

    if previous_handlers is not None:
        restore_signal_handlers(previous_handlers)
    if previous_sigchld is not None:
        signal.signal(signal.SIGCHLD, previous_sigchld)

    print(
        "%s status=%s telemetry=%s"
        % (SCHEMA, telemetry["status"], telemetry_path),
        flush=True,
    )
    return int(telemetry["runner_exit_code"])


def main(argv: Optional[Sequence[str]] = None) -> int:
    if os.name != "posix":
        print("CAPRUN/v1 is POSIX-only", file=sys.stderr)
        return RUNNER_FAILURE_EXIT
    parsed = parser().parse_args(argv)
    command = list(parsed.command)
    if command and command[0] == "--":
        command = command[1:]
    if not command:
        parser().error("an argv command is required after --")
    try:
        return execute(parsed, command)
    except BaseException as error:
        print("CAPRUN/v1 runner failure: %s" % error, file=sys.stderr)
        return RUNNER_FAILURE_EXIT


if __name__ == "__main__":
    sys.exit(main())
