#!/usr/bin/env python3
"""Durably extract every full fibre chart in one Moh class.

This is deliberately only an orchestration wrapper around the checked-in
fixed Singular builders.  It does not solve or alter the chart equations.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import signal
import subprocess
import time
from pathlib import Path


HERE = Path(__file__).resolve().parent


def row_count(path: Path) -> int:
    if not path.is_file() or path.stat().st_size <= 42:
        return 0
    with path.open("rb") as fh:
        header = fh.readline()
        if header != b"source_index|h_power|x_power|y_power|expr\n":
            raise RuntimeError(f"unexpected row header in {path}: {header!r}")
        return sum(1 for line in fh if line.strip())


def run_builder(class_dir: Path, stem: str, timeout: int) -> dict:
    builder = class_dir / "builders" / f"{stem}_builder.sing"
    rows = class_dir / "rows" / f"{stem}_rows.tsv"
    jobs = class_dir / "jobs"
    jobs.mkdir(exist_ok=True)
    log = jobs / f"{stem}_extract_msolve20260905.log"
    before = row_count(rows)
    started = time.time()
    env = os.environ.copy()
    for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
        env[name] = "1"
    with log.open("w") as out:
        proc = subprocess.Popen(
            [
                "Singular", "--cpus=1", "--threads=1", "--flint-threads=1",
                "-q", "--no-rc", str(builder.relative_to(class_dir)),
            ],
            cwd=class_dir,
            stdout=out,
            stderr=subprocess.STDOUT,
            env=env,
            start_new_session=True,
        )
        timed_out = False
        try:
            rc = proc.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            timed_out = True
            os.killpg(proc.pid, signal.SIGTERM)
            try:
                rc = proc.wait(timeout=15)
            except subprocess.TimeoutExpired:
                os.killpg(proc.pid, signal.SIGKILL)
                rc = proc.wait()
    text = log.read_text(errors="replace")
    after = row_count(rows)
    match = re.search(r"NATIVE_DONE equations=(\d+)", text)
    declared = int(match.group(1)) if match else None
    valid = rc == 0 and declared is not None and declared == after and after > 0
    return {
        "stem": stem,
        "builder": str(builder),
        "rows": str(rows),
        "rows_before": before,
        "rows_after": after,
        "declared_equations": declared,
        "valid": valid,
        "timed_out": timed_out,
        "returncode": rc,
        "wall_seconds": round(time.time() - started, 3),
        "log": str(log),
        "log_tail": text[-1000:],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("class_id")
    parser.add_argument("--timeout-per-stem", type=int, default=7200)
    parser.add_argument(
        "--only-stem", action="append", default=[],
        help="extract only this full stem (repeatable); default is every fibre",
    )
    parser.add_argument(
        "--reuse-valid", action="store_true",
        help="reuse a non-header TSV only when its mtime is at least the builder mtime",
    )
    args = parser.parse_args()
    class_dir = HERE / "classes" / args.class_id
    data = json.loads((class_dir / "class.json").read_text())
    results = []
    selected = data["rows"]
    if args.only_stem:
        wanted = set(args.only_stem)
        selected = [row for row in selected if row["stem"] in wanted]
        found = {row["stem"] for row in selected}
        if found != wanted:
            missing = sorted(wanted - found)
            raise SystemExit(f"unknown --only-stem for {args.class_id}: {missing}")
    if len(args.only_stem) == 1:
        summary_name = f"{args.only_stem[0]}_extract_msolve20260905.json"
    else:
        summary_name = "extract_msolve20260905.json"
    for row in selected:
        stem = row["stem"]
        builder = class_dir / "builders" / f"{stem}_builder.sing"
        rows = class_dir / "rows" / f"{stem}_rows.tsv"
        existing = row_count(rows)
        if (
            args.reuse_valid
            and existing > 0
            and rows.stat().st_mtime_ns >= builder.stat().st_mtime_ns
        ):
            results.append({
                "stem": stem,
                "rows_after": existing,
                "valid": True,
                "reused": True,
                "builder": str(builder),
                "rows": str(rows),
            })
        else:
            results.append(run_builder(class_dir, stem, args.timeout_per_stem))
        summary = {
            "class_id": args.class_id,
            "host": os.uname().nodename,
            "finished": False,
            "results": results,
        }
        (class_dir / "jobs" / summary_name).write_text(
            json.dumps(summary, indent=2) + "\n"
        )
    summary["finished"] = True
    summary["all_valid"] = all(item["valid"] for item in results)
    (class_dir / "jobs" / summary_name).write_text(
        json.dumps(summary, indent=2) + "\n"
    )
    print(json.dumps(summary, indent=2), flush=True)
    return 0 if summary["all_valid"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
