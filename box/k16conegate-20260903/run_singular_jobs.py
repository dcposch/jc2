#!/usr/bin/env python3
"""Run emitted Singular jobs with per-job caps and status files."""
from __future__ import annotations

import json
import pathlib
import subprocess
import sys
import time

ROOT = pathlib.Path("/home/ubuntu/jc2/box/k16conegate-20260903")


def run_job(path: pathlib.Path, timeout_seconds: int, purpose: str) -> dict[str, object]:
    out_path = path.with_suffix(".out")
    err_path = path.with_suffix(".err")
    started = time.monotonic()
    cmd = ["timeout", "--kill-after=5s", f"{timeout_seconds}s", "Singular", "-q", str(path)]
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    elapsed = time.monotonic() - started
    out_path.write_text(result.stdout, encoding="utf-8")
    err_path.write_text(result.stderr, encoding="utf-8")
    status = "PASS" if result.returncode == 0 else "INCONCLUSIVE_TIMEOUT" if result.returncode == 124 else "FAIL"
    if "? error occurred" in result.stdout or "? error occurred" in result.stderr:
        status = "FAIL"
    record = {
        "path": str(path),
        "purpose": purpose,
        "timeout_seconds": timeout_seconds,
        "elapsed_seconds": elapsed,
        "returncode": result.returncode,
        "status": status,
        "stdout": str(out_path),
        "stderr": str(err_path),
    }
    path.with_suffix(".status.json").write_text(
        json.dumps(record, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(record, sort_keys=True))
    return record


def main() -> None:
    if len(sys.argv) > 1:
        jobs = [{"path": arg, "timeout_seconds": 300, "purpose": "manual"} for arg in sys.argv[1:]]
    else:
        jobs = json.loads((ROOT / "singular_jobs.json").read_text(encoding="utf-8"))["jobs"]
    records = []
    for job in jobs:
        records.append(run_job(pathlib.Path(job["path"]), int(job["timeout_seconds"]), str(job["purpose"])))
    status = "PASS" if all(item["status"] == "PASS" for item in records) else "PARTIAL"
    (ROOT / "singular_run_summary.json").write_text(
        json.dumps({"status": status, "runs": records}, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print("SINGULAR_RUN_SUMMARY =", status)


if __name__ == "__main__":
    main()
