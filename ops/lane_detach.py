#!/usr/bin/env python3
"""Restart-resilient supervisor for external model lanes on macOS.

This tool is deliberately a wrapper around, not a replacement for,
``ops/lane.sh``.  The existing launcher remains the sole writer of the
schema-2 run receipt and retains all prompt, sandbox, and hash custody.

The wrapper loads ``lane.sh`` as a one-shot per-user launchd job.  The job is
therefore outside the coordinator/terminal process tree and survives an
accidental Codex-process termination.  While a job is live, ``status`` and
``wait`` consult only launchd plus ``.lane-jobs/<tag>/launch.v1.json``; they
never open the active report, model log, or ``.run.v2`` receipt.  Once launchd
reports a terminal state, the coordinator must still follow receipt-first
custody before reading any report or log.

Usage::

    python3 ops/lane_detach.py launch ADAPTER TAG PROMPT
    python3 ops/lane_detach.py status TAG [--json]
    python3 ops/lane_detach.py wait TAG [--timeout SECONDS] [--json]
    python3 ops/lane_detach.py list [--json | --running-tags]
    python3 ops/lane_detach.py unload TAG

``unload`` refuses a live job.  It removes only the terminal launchd
registration and keeps the ignored sidecar as crash-recovery history.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import plistlib
import re
import shutil
import stat
import subprocess
import sys
import time
from typing import Any


SCHEMA = "JC2-LANE-SUPERVISOR/v1"
TAG_RE = re.compile(r"^[A-Za-z0-9._-]+$")
ADAPTER_RE = re.compile(r"^[a-z0-9_-]+$")
TERMINAL_STATES = frozenset({"SUCCEEDED", "FAILED", "UNLOADED"})
ACTIVE_STATES = frozenset({"STARTING", "RUNNING"})
ENV_ALLOWLIST = (
    "HOME",
    "PATH",
    "USER",
    "LOGNAME",
    "LANG",
    "LC_ALL",
    "LC_CTYPE",
    "SHELL",
    "TMPDIR",
    "XDG_CONFIG_HOME",
    "CODEX_MODEL",
    "CODEX_REASONING_EFFORT",
)


class LaneDetachError(RuntimeError):
    """Fail-closed operator error."""


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace(
        "+00:00", "Z"
    )


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def repo_root() -> Path:
    # Resolve only this tracked script and its parents.  Never enumerate the
    # repository or the separately owned excluded nested worktree.
    return Path(__file__).resolve(strict=True).parent.parent


def lexical_absolute(value: str, base: Path) -> Path:
    candidate = Path(value)
    if not candidate.is_absolute():
        candidate = base / candidate
    # abspath is lexical; unlike resolve(), it does not follow a symlink into
    # an excluded tree before the no-symlink gate below.
    return Path(os.path.abspath(os.fspath(candidate)))


def path_is_within(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def require_regular_nonsymlink(path: Path, label: str, *, executable: bool = False) -> None:
    try:
        info = os.lstat(path)
    except OSError as exc:
        raise LaneDetachError(f"{label} is unavailable: {path}: {exc}") from exc
    if stat.S_ISLNK(info.st_mode) or not stat.S_ISREG(info.st_mode):
        raise LaneDetachError(f"{label} must be a regular non-symlink file: {path}")
    if executable and not os.access(path, os.X_OK):
        raise LaneDetachError(f"{label} is not executable: {path}")


def require_repo_path_without_symlinks(
    path: Path,
    root: Path,
    label: str,
    *,
    final_kind: str,
    executable: bool = False,
) -> None:
    """Validate every component beneath ``root`` without following a symlink.

    ``lstat(root/link/child)`` would already follow ``link`` while looking up
    ``child``.  Walk one component at a time and stop as soon as ``link``
    itself is seen, so a link into the excluded tree is rejected without any
    lookup or metadata access inside its target.
    """

    if final_kind not in {"file", "directory"}:
        raise LaneDetachError(f"invalid internal final kind: {final_kind}")
    try:
        relative = path.relative_to(root)
    except ValueError as exc:
        raise LaneDetachError(f"{label} must be inside the campaign repository: {path}") from exc
    if not relative.parts:
        raise LaneDetachError(f"{label} cannot be the repository root")

    current = root
    final_index = len(relative.parts) - 1
    for index, component in enumerate(relative.parts):
        current = current / component
        try:
            info = os.lstat(current)
        except OSError as exc:
            raise LaneDetachError(f"{label} path component is unavailable: {current}: {exc}") from exc
        if stat.S_ISLNK(info.st_mode):
            raise LaneDetachError(f"{label} path component must not be a symlink: {current}")
        if index < final_index:
            if not stat.S_ISDIR(info.st_mode):
                raise LaneDetachError(
                    f"{label} intermediate component must be a directory: {current}"
                )
            continue
        if final_kind == "file" and not stat.S_ISREG(info.st_mode):
            raise LaneDetachError(f"{label} must be a regular file: {current}")
        if final_kind == "directory" and not stat.S_ISDIR(info.st_mode):
            raise LaneDetachError(f"{label} must be a directory: {current}")
        if executable and not os.access(current, os.X_OK):
            raise LaneDetachError(f"{label} is not executable: {current}")


def write_exclusive(path: Path, payload: bytes, mode: int) -> None:
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, mode)
    try:
        with os.fdopen(descriptor, "wb", closefd=False) as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
    finally:
        os.close(descriptor)
    os.chmod(path, mode)


def launchctl_path() -> str:
    command = shutil.which("launchctl")
    if not command:
        raise LaneDetachError("launchctl is required")
    return command


def require_darwin() -> None:
    if sys.platform != "darwin":
        raise LaneDetachError("detached external lanes require macOS launchd")


def job_root(root: Path) -> Path:
    return root / ".lane-jobs"


def job_dir(root: Path, tag: str) -> Path:
    return job_root(root) / tag


def record_path(root: Path, tag: str) -> Path:
    return job_dir(root, tag) / "launch.v1.json"


def validate_tag(tag: str) -> None:
    if not TAG_RE.fullmatch(tag):
        raise LaneDetachError(
            "invalid tag (use A-Z, a-z, 0-9, dot, underscore, or hyphen)"
        )


def validate_adapter(adapter: str) -> None:
    if not ADAPTER_RE.fullmatch(adapter):
        raise LaneDetachError("invalid adapter name")


def label_for(root: Path, tag: str) -> str:
    payload = f"{root}\0{tag}".encode("utf-8")
    return "com.jc2.lane." + hashlib.sha256(payload).hexdigest()[:24]


def safe_environment() -> dict[str, str]:
    # Do not serialize API keys, tokens, or the coordinator's full environment
    # into a persistent plist.  Current adapters authenticate from HOME; the
    # Claude adapters explicitly unset ANTHROPIC_API_KEY themselves.
    return {name: os.environ[name] for name in ENV_ALLOWLIST if os.environ.get(name)}


def load_record(root: Path, tag: str) -> dict[str, Any]:
    validate_tag(tag)
    directory = job_dir(root, tag)
    try:
        directory_info = os.lstat(directory)
    except OSError as exc:
        raise LaneDetachError(f"no detached-lane sidecar for tag: {tag}") from exc
    if stat.S_ISLNK(directory_info.st_mode) or not stat.S_ISDIR(directory_info.st_mode):
        raise LaneDetachError(f"detached-lane directory is not a real directory: {directory}")
    path = record_path(root, tag)
    require_regular_nonsymlink(path, "launch sidecar")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise LaneDetachError(f"invalid launch sidecar: {path}: {exc}") from exc
    required = {
        "schema",
        "tag",
        "adapter",
        "prompt",
        "label",
        "domain",
        "repo_root",
        "supervisor",
        "supervisor_sha256",
        "launcher",
        "launch_utc",
        "prompt_sha256",
        "adapter_sha256",
        "launcher_sha256",
        "plist",
        "plist_sha256",
        "supervisor_stdout",
        "supervisor_stderr",
        "launchctl",
    }
    if not isinstance(value, dict) or not required.issubset(value):
        raise LaneDetachError(f"launch sidecar has an invalid schema: {path}")
    if value.get("schema") != SCHEMA or value.get("tag") != tag:
        raise LaneDetachError(f"launch sidecar identity mismatch: {path}")
    if value.get("repo_root") != os.fspath(root):
        raise LaneDetachError(f"launch sidecar repository mismatch: {path}")
    return value


def service_name(record: dict[str, Any]) -> str:
    return f"{record['domain']}/{record['label']}"


def launchctl_print(record: dict[str, Any]) -> tuple[int, str]:
    completed = subprocess.run(
        [launchctl_path(), "print", service_name(record)],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=15,
        check=False,
    )
    return completed.returncode, completed.stdout


def parse_launchd(record: dict[str, Any]) -> dict[str, Any]:
    unloaded_marker = job_dir(Path(record["repo_root"]), record["tag"]) / "unloaded.v1.json"
    if unloaded_marker.exists():
        return {
            "schema": SCHEMA,
            "tag": record["tag"],
            "label": record["label"],
            "state": "UNLOADED",
            "pid": None,
            "lane_exit_code": None,
            "launchd_state": None,
        }

    returncode, output = launchctl_print(record)
    base: dict[str, Any] = {
        "schema": SCHEMA,
        "tag": record["tag"],
        "label": record["label"],
        "state": "MISSING_JOB",
        "pid": None,
        "lane_exit_code": None,
        "launchd_state": None,
    }
    if returncode != 0:
        # A launchd registration should own the lane, but a crash between
        # process creation and registration visibility must not be mistaken
        # for terminal state.  Ask pgrep only for this exact campaign launcher
        # and tag; do not enumerate unrelated process command lines.
        pattern = (
            re.escape(str(record["launcher"]))
            + r" [a-z0-9_-]+ "
            + re.escape(str(record["tag"]))
            + r"(?: |$)"
        )
        pgrep = shutil.which("pgrep")
        if pgrep:
            probe = subprocess.run(
                [pgrep, "-f", pattern],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
                timeout=10,
                check=False,
            )
            if probe.returncode == 0:
                first_pid = next(
                    (int(line) for line in probe.stdout.splitlines() if line.isdigit()),
                    None,
                )
                if first_pid is not None:
                    base["state"] = "RUNNING"
                    base["pid"] = first_pid
                    base["launchd_state"] = "registration-missing-process-visible"
        return base

    active_match = re.search(r"^\s*active count = (\d+)\s*$", output, re.MULTILINE)
    state_match = re.search(r"^\s*state = ([^\n]+?)\s*$", output, re.MULTILINE)
    pid_match = re.search(r"^\s*pid = (\d+)\s*$", output, re.MULTILINE)
    exit_match = re.search(r"^\s*last exit code = (-?\d+)\s*$", output, re.MULTILINE)
    active = int(active_match.group(1)) if active_match else 0
    lane_exit = int(exit_match.group(1)) if exit_match else None
    base["pid"] = int(pid_match.group(1)) if pid_match else None
    base["lane_exit_code"] = lane_exit
    base["launchd_state"] = state_match.group(1) if state_match else None
    if active > 0:
        base["state"] = "RUNNING"
    elif lane_exit is not None:
        base["state"] = "SUCCEEDED" if lane_exit == 0 else "FAILED"
    else:
        base["state"] = "STARTING"
    return base


def format_status(value: dict[str, Any]) -> str:
    fields = [value["tag"], value["state"]]
    if value.get("pid") is not None:
        fields.append(f"pid={value['pid']}")
    if value.get("lane_exit_code") is not None:
        fields.append(f"exit={value['lane_exit_code']}")
    if value.get("launchd_state"):
        fields.append(f"launchd={value['launchd_state']}")
    return " ".join(fields)


def command_launch(args: argparse.Namespace) -> int:
    require_darwin()
    validate_tag(args.tag)
    validate_adapter(args.adapter)
    root = repo_root()
    excluded = root / "jc2-lean"
    prompt = lexical_absolute(args.prompt, Path.cwd())
    if not path_is_within(prompt, root):
        raise LaneDetachError(f"prompt must be inside the campaign repository: {prompt}")
    if path_is_within(prompt, excluded):
        raise LaneDetachError("prompt path is inside the excluded nested worktree")
    require_repo_path_without_symlinks(prompt, root, "prompt", final_kind="file")

    launcher = root / "ops" / "lane.sh"
    adapter = root / "ops" / "adapters" / f"{args.adapter}.sh"
    require_repo_path_without_symlinks(
        launcher, root, "lane launcher", final_kind="file", executable=True
    )
    require_repo_path_without_symlinks(
        adapter, root, "adapter", final_kind="file", executable=True
    )

    xmodel = root / "xmodel"
    require_repo_path_without_symlinks(xmodel, root, "xmodel directory", final_kind="directory")
    for suffix in (".log", ".md", ".run", ".run.v2"):
        if os.path.lexists(xmodel / f"{args.tag}{suffix}"):
            raise LaneDetachError(
                f"duplicate tag refused; choose a new attempt tag: {args.tag}"
            )
    locks = root / ".lane-locks"
    if os.path.lexists(locks):
        require_repo_path_without_symlinks(
            locks, root, "lane-lock directory", final_kind="directory"
        )
    if os.path.lexists(locks / args.tag):
        raise LaneDetachError(f"tag already has a live lane lock: {args.tag}")

    jobs = job_root(root)
    if os.path.lexists(jobs):
        require_repo_path_without_symlinks(
            jobs, root, "lane-job root", final_kind="directory"
        )
    else:
        jobs.mkdir(mode=0o700)
    os.chmod(jobs, 0o700)
    directory = job_dir(root, args.tag)
    try:
        directory.mkdir(mode=0o700)
    except FileExistsError as exc:
        raise LaneDetachError(f"detached sidecar already exists for tag: {args.tag}") from exc

    label = label_for(root, args.tag)
    domain = f"gui/{os.getuid()}"
    plist_path = directory / "job.plist"
    stdout_path = directory / "supervisor.stdout"
    stderr_path = directory / "supervisor.stderr"
    write_exclusive(stdout_path, b"", 0o600)
    write_exclusive(stderr_path, b"", 0o600)
    plist = {
        "Label": label,
        "ProgramArguments": [
            "/bin/sh",
            os.fspath(launcher),
            args.adapter,
            args.tag,
            os.fspath(prompt),
        ],
        "WorkingDirectory": os.fspath(root),
        "EnvironmentVariables": safe_environment(),
        "RunAtLoad": True,
        "KeepAlive": False,
        "ProcessType": "Background",
        "AbandonProcessGroup": False,
        "StandardOutPath": os.fspath(stdout_path),
        "StandardErrorPath": os.fspath(stderr_path),
    }
    plist_payload = plistlib.dumps(plist, fmt=plistlib.FMT_XML, sort_keys=True)
    write_exclusive(plist_path, plist_payload, 0o400)
    record = {
        "schema": SCHEMA,
        "tag": args.tag,
        "adapter": args.adapter,
        "prompt": os.fspath(prompt),
        "label": label,
        "domain": domain,
        "repo_root": os.fspath(root),
        "supervisor": os.fspath(Path(__file__).resolve(strict=True)),
        "supervisor_sha256": sha256_file(Path(__file__).resolve(strict=True)),
        "launcher": os.fspath(launcher),
        "launch_utc": utc_now(),
        "prompt_sha256": sha256_file(prompt),
        "adapter_sha256": sha256_file(adapter),
        "launcher_sha256": sha256_file(launcher),
        "plist": os.fspath(plist_path),
        "plist_sha256": sha256_bytes(plist_payload),
        "supervisor_stdout": os.fspath(stdout_path),
        "supervisor_stderr": os.fspath(stderr_path),
        "launchctl": launchctl_path(),
    }
    record_payload = (json.dumps(record, indent=2, sort_keys=True) + "\n").encode("utf-8")
    write_exclusive(record_path(root, args.tag), record_payload, 0o400)

    completed = subprocess.run(
        [launchctl_path(), "bootstrap", domain, os.fspath(plist_path)],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=30,
        check=False,
    )
    if completed.returncode != 0:
        failure = {
            "schema": SCHEMA,
            "tag": args.tag,
            "failed_utc": utc_now(),
            "bootstrap_exit": completed.returncode,
            "bootstrap_output": completed.stdout,
        }
        write_exclusive(
            directory / "bootstrap-failure.v1.json",
            (json.dumps(failure, indent=2, sort_keys=True) + "\n").encode("utf-8"),
            0o400,
        )
        raise LaneDetachError(
            f"launchd bootstrap failed for {args.tag}; sidecar retained for diagnosis"
        )

    value = parse_launchd(record)
    if args.json:
        print(json.dumps(value, sort_keys=True))
    else:
        print(format_status(value))
        print(
            "lane is launchd-supervised; use lane_detach.py wait/status and read "
            "the .run.v2 receipt only after a terminal state"
        )
    return 0


def command_status(args: argparse.Namespace) -> int:
    require_darwin()
    root = repo_root()
    record = load_record(root, args.tag)
    value = parse_launchd(record)
    print(json.dumps(value, sort_keys=True) if args.json else format_status(value))
    return 0


def command_wait(args: argparse.Namespace) -> int:
    require_darwin()
    root = repo_root()
    record = load_record(root, args.tag)
    deadline = None if args.timeout is None else time.monotonic() + args.timeout
    previous: tuple[Any, ...] | None = None
    while True:
        value = parse_launchd(record)
        fingerprint = (
            value["state"],
            value.get("pid"),
            value.get("lane_exit_code"),
            value.get("launchd_state"),
        )
        if fingerprint != previous and not args.json:
            print(format_status(value), flush=True)
            previous = fingerprint
        if value["state"] in TERMINAL_STATES:
            if args.json:
                print(json.dumps(value, sort_keys=True))
            if value["state"] == "SUCCEEDED":
                return 0
            if value["state"] == "UNLOADED":
                return 3
            return 1
        if value["state"] == "MISSING_JOB":
            if args.json:
                print(json.dumps(value, sort_keys=True))
            return 3
        if deadline is not None and time.monotonic() >= deadline:
            if args.json:
                print(json.dumps(value, sort_keys=True))
            return 124
        time.sleep(args.interval)


def iter_records(root: Path) -> list[dict[str, Any]]:
    jobs = job_root(root)
    if not jobs.exists():
        return []
    info = os.lstat(jobs)
    if stat.S_ISLNK(info.st_mode) or not stat.S_ISDIR(info.st_mode):
        raise LaneDetachError(f"lane-job root is not a real directory: {jobs}")
    records: list[dict[str, Any]] = []
    for entry in sorted(jobs.iterdir(), key=lambda item: item.name):
        if not TAG_RE.fullmatch(entry.name):
            continue
        # Corrupt supervisor state is itself actionable recovery evidence;
        # never hide it by silently returning an incomplete list.
        records.append(load_record(root, entry.name))
    return records


def command_list(args: argparse.Namespace) -> int:
    require_darwin()
    values = [parse_launchd(record) for record in iter_records(repo_root())]
    if args.running_tags:
        for value in values:
            if value["state"] in ACTIVE_STATES:
                print(value["tag"])
    elif args.json:
        print(json.dumps(values, sort_keys=True))
    elif not values:
        print("(no detached lane supervisors)")
    else:
        for value in values:
            print(format_status(value))
    return 0


def command_unload(args: argparse.Namespace) -> int:
    require_darwin()
    root = repo_root()
    record = load_record(root, args.tag)
    value = parse_launchd(record)
    if value["state"] in ACTIVE_STATES:
        raise LaneDetachError(f"refusing to unload live lane: {args.tag}")
    if value["state"] != "MISSING_JOB" and value["state"] != "UNLOADED":
        completed = subprocess.run(
            [launchctl_path(), "bootout", service_name(record)],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=30,
            check=False,
        )
        if completed.returncode != 0:
            raise LaneDetachError(
                f"launchd bootout failed for terminal lane {args.tag}: "
                f"{completed.stdout.strip()}"
            )
    marker = job_dir(root, args.tag) / "unloaded.v1.json"
    if not marker.exists():
        payload = {
            "schema": SCHEMA,
            "tag": args.tag,
            "unloaded_utc": utc_now(),
            "terminal_state_before_unload": value["state"],
            "lane_exit_code": value.get("lane_exit_code"),
        }
        write_exclusive(
            marker,
            (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8"),
            0o400,
        )
    print(f"{args.tag} UNLOADED sidecar-retained")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    launch = subparsers.add_parser("launch", help="bootstrap a detached one-shot lane")
    launch.add_argument("adapter")
    launch.add_argument("tag")
    launch.add_argument("prompt")
    launch.add_argument("--json", action="store_true")
    launch.set_defaults(func=command_launch)

    status_parser = subparsers.add_parser("status", help="query launchd without lane files")
    status_parser.add_argument("tag")
    status_parser.add_argument("--json", action="store_true")
    status_parser.set_defaults(func=command_status)

    wait_parser = subparsers.add_parser("wait", help="wait through the safe supervisor plane")
    wait_parser.add_argument("tag")
    wait_parser.add_argument("--timeout", type=float)
    wait_parser.add_argument("--interval", type=float, default=5.0)
    wait_parser.add_argument("--json", action="store_true")
    wait_parser.set_defaults(func=command_wait)

    list_parser = subparsers.add_parser("list", help="list detached supervisor states")
    list_mode = list_parser.add_mutually_exclusive_group()
    list_mode.add_argument("--json", action="store_true")
    list_mode.add_argument("--running-tags", action="store_true")
    list_parser.set_defaults(func=command_list)

    unload = subparsers.add_parser("unload", help="unregister a terminal job, keep sidecar")
    unload.add_argument("tag")
    unload.set_defaults(func=command_unload)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if getattr(args, "timeout", None) is not None and args.timeout < 0:
        parser.error("--timeout must be nonnegative")
    if getattr(args, "interval", 1) <= 0:
        parser.error("--interval must be positive")
    try:
        return int(args.func(args))
    except (LaneDetachError, OSError, subprocess.SubprocessError) as exc:
        print(f"lane-detach: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
