#!/usr/bin/env python3
"""Parallel file-shippable runner for Q8 invariant support learning."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import time


CASE = Path(__file__).resolve().parent
WORKER = CASE / "modular_support.py"
WORKER_SHA256 = "c36d6cf1ca538a39923412075fb44be77ed30023107f4eac755722b7d796dea0"
DEFAULT_JOBS = (
    (10007, 980),
    (10037, 1220),
    (10039, 8298),
    (10061, 5525),
    (10067, 1853),
    (10069, 5814),
    (10079, 8882),
    (10091, 5216),
)


def one_job(job, args, output_directory):
    prime, root = job
    command = [
        sys.executable, str(WORKER),
        "--prime", str(prime),
        "--root", str(root),
        "--order", str(args.order),
        "--max-left", str(args.max_left),
        "--max-right", str(args.max_right),
        "--max-columns", str(args.max_columns),
        "--holdout", str(args.holdout),
    ]
    started = time.monotonic()
    result = subprocess.run(
        command, text=True, capture_output=True, timeout=args.timeout,
        check=False,
    )
    elapsed = time.monotonic() - started
    target = output_directory / f"support-p{prime}-v{root}.json"
    if result.returncode == 0:
        # Parsing is fail-closed before the payload is retained.
        json.loads(result.stdout)
        target.write_text(result.stdout)
    return {
        "prime": prime,
        "root": root,
        "command": command,
        "returncode": result.returncode,
        "elapsed_seconds": elapsed,
        "output": str(target) if result.returncode == 0 else None,
        "stderr": result.stderr[-4000:],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-directory", type=Path, required=True)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--order", type=int, default=128)
    parser.add_argument("--max-left", type=int, default=24)
    parser.add_argument("--max-right", type=int, default=24)
    parser.add_argument("--max-columns", type=int, default=108)
    parser.add_argument("--holdout", type=int, default=16)
    parser.add_argument("--timeout", type=int, default=3600)
    args = parser.parse_args()
    got = sha256(WORKER.read_bytes()).hexdigest()
    if got != WORKER_SHA256:
        raise RuntimeError((str(WORKER), got, WORKER_SHA256))
    args.output_directory.mkdir(parents=True, exist_ok=True)
    records = []
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(one_job, job, args, args.output_directory): job
            for job in DEFAULT_JOBS
        }
        for future in as_completed(futures):
            records.append(future.result())
    records.sort(key=lambda item: item["prime"])
    payload = {
        "worker_sha256": WORKER_SHA256,
        "parameters": {
            "workers": args.workers,
            "order": args.order,
            "max_left": args.max_left,
            "max_right": args.max_right,
            "max_columns": args.max_columns,
            "holdout": args.holdout,
            "timeout": args.timeout,
        },
        "jobs": records,
        "all_pass": all(record["returncode"] == 0 for record in records),
        "scope": (
            "support learning only; modular hits require cross-prime support "
            "agreement, characteristic-zero lifting, and exact substitution"
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    if not payload["all_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
