#!/usr/bin/env python3
"""Run an audited triangular Singular script with timeout/RSS/affinity custody."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import signal
import socket
import subprocess
import time


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def group_sample(group: int, cpu: int | None) -> tuple[int, list[int]]:
    rss_kb = 0
    members: list[int] = []
    for stat_path in Path("/proc").glob("[0-9]*/stat"):
        try:
            stat = stat_path.read_text(encoding="utf-8")
            fields = stat[stat.rfind(")") + 2 :].split()
            if int(fields[2]) != group:
                continue
            pid = int(stat_path.parent.name)
            members.append(pid)
            if cpu is not None:
                os.sched_setaffinity(pid, {cpu})
            status = stat_path.with_name("status").read_text(encoding="utf-8")
            match = re.search(r"^VmRSS:\s+(\d+)\s+kB$", status, re.M)
            if match:
                rss_kb += int(match.group(1))
        except (FileNotFoundError, PermissionError, ProcessLookupError, ValueError, OSError):
            continue
    return rss_kb, sorted(members)


def atomic_json(path: Path, payload: dict) -> None:
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    temporary.replace(path)


def markers(text: str) -> dict[str, object]:
    wanted = (
        "TRIANGULAR_OK",
        "TRIANGULAR_MAX_DEG",
        "TRIANGULAR_STD_DONE",
        "TRIANGULAR_GENERATOR_COUNT",
        "TRIANGULAR_NF_ALL_ZERO",
        "TRIANGULAR_BASIS_SIZE",
        "TRIANGULAR_DIMENSION",
        "TRIANGULAR_LEAD_DIMENSION",
        "TRIANGULAR_UNIT",
        "SCRIPT_DONE",
    )
    found: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        for key in wanted:
            if stripped == key:
                found[key] = True
            elif stripped.startswith(key + " "):
                found[key] = stripped[len(key) + 1 :]
    found["pivot_ok_count"] = sum(line.strip().startswith("PIVOT_OK ") for line in text.splitlines())
    found["substitution_ok_count"] = sum(
        line.strip().startswith("IDEAL_SUBST_OK ") for line in text.splitlines()
    )
    return found


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--script", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--tag", required=True)
    parser.add_argument("--timeout", type=int, default=1800)
    parser.add_argument("--cpu", type=int)
    args = parser.parse_args()

    script = args.script.resolve()
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    stdout_path = output_dir / f"{args.tag}.out"
    stderr_path = output_dir / f"{args.tag}.err"
    time_path = output_dir / f"{args.tag}.time"
    record_path = output_dir / f"{args.tag}.run.json"
    command = [
        "/usr/bin/time",
        "-v",
        "-o",
        str(time_path),
        "Singular",
        "--cpus=1",
        "--threads=1",
        "--flint-threads=1",
        "--no-rc",
        "-q",
        str(script),
    ]
    env = os.environ.copy()
    for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
        env[name] = "1"
    started_utc = utc_now()
    started = time.monotonic()
    peak_rss_kb = 0
    samples = 0
    last_members: list[int] = []
    timed_out = False
    with stdout_path.open("w", encoding="utf-8") as stdout, stderr_path.open("w", encoding="utf-8") as stderr:
        process = subprocess.Popen(
            command,
            stdout=stdout,
            stderr=stderr,
            cwd=script.parents[3],
            env=env,
            start_new_session=True,
            text=True,
        )
        deadline = started + args.timeout
        while process.poll() is None:
            rss_kb, last_members = group_sample(process.pid, args.cpu)
            peak_rss_kb = max(peak_rss_kb, rss_kb)
            samples += 1
            if time.monotonic() >= deadline:
                timed_out = True
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                break
            time.sleep(0.1)
        returncode = process.wait()
    elapsed = time.monotonic() - started
    stdout_text = stdout_path.read_text(encoding="utf-8", errors="replace")
    parsed = markers(stdout_text)
    clean_unit = (
        returncode == 0
        and not timed_out
        and parsed.get("SCRIPT_DONE") is True
        and parsed.get("TRIANGULAR_NF_ALL_ZERO") == "1"
        and parsed.get("TRIANGULAR_BASIS_SIZE") == "1"
        and parsed.get("TRIANGULAR_DIMENSION") == "-1"
        and parsed.get("TRIANGULAR_LEAD_DIMENSION") == "-1"
        and parsed.get("TRIANGULAR_UNIT") == "1"
        and "? error occurred" not in stdout_text
    )
    record = {
        "schema": "jc2.s56-recert.triangular-run/v1",
        "host": socket.gethostname(),
        "started_utc": started_utc,
        "finished_utc": utc_now(),
        "script": str(script),
        "script_sha256": sha256(script),
        "command": command,
        "returncode": returncode,
        "timed_out": timed_out,
        "elapsed_seconds": round(elapsed, 6),
        "maximum_process_group_rss_kb": peak_rss_kb,
        "sample_count": samples,
        "requested_cpu": args.cpu,
        "last_observed_process_group": last_members,
        "stdout": str(stdout_path),
        "stdout_sha256": sha256(stdout_path),
        "stderr": str(stderr_path),
        "stderr_sha256": sha256(stderr_path),
        "time": str(time_path),
        "time_sha256": sha256(time_path),
        "markers": parsed,
        "clean_unit": clean_unit,
    }
    atomic_json(record_path, record)
    print(json.dumps(record, indent=2, sort_keys=True))
    raise SystemExit(0 if returncode == 0 else returncode)


if __name__ == "__main__":
    main()
