#!/usr/bin/env python3
"""Bind and summarize the twelve requested S5/S6 recertification runs.

This is deliberately a reader, not a solver.  It checks that every requested
chart/field tuple has a durable run record, re-hashes its script and streams,
and applies the promotion rules used by this lane.  A timeout is reported as
compute-bound; it is never interpreted as either a unit ideal or a survivor.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
RUNS = HERE / "triangular-runs"

EXPECTED = {
    "S5_part2_p32003_seqcert": ("S5", "[2]", "32003"),
    "S5_part2_p32009_seqcert": ("S5", "[2]", "32009"),
    "S5_part2_p32027_seqcert": ("S5", "[2]", "32027"),
    "S5_part2_Q_seqcert": ("S5", "[2]", "Q"),
    "S5_part1_1_q2_p32003_seqcert": ("S5", "[1,1], Q2=0", "32003"),
    "S5_part1_1_q2_p32009_seqcert": ("S5", "[1,1], Q2=0", "32009"),
    "S5_part1_1_q2_p32027_seqcert": ("S5", "[1,1], Q2=0", "32027"),
    "S5_part1_1_q2_Q_seqcert": ("S5", "[1,1], Q2=0", "Q"),
    "S6_part1_p32003_seqcert": ("S6", "[1]", "32003"),
    "S6_part1_p32009_seqcert": ("S6", "[1]", "32009"),
    "S6_part1_p32027_seqcert": ("S6", "[1]", "32027"),
    "S6_part1_Q_seqcert": ("S6", "[1]", "Q"),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def local_path(value: str) -> Path:
    path = Path(value)
    if path.is_absolute():
        # Fleet records contain the same absolute workspace path as this host.
        return path
    return ROOT / path


def inspect(tag: str, identity: tuple[str, str, str]) -> dict[str, Any]:
    record_path = RUNS / f"{tag}.run.json"
    record = json.loads(record_path.read_text(encoding="utf-8"))
    script = local_path(record["script"])
    stdout = local_path(record["stdout"])
    stderr = local_path(record["stderr"])
    checks = {
        "script_sha256": sha256(script) == record["script_sha256"],
        "stdout_sha256": sha256(stdout) == record["stdout_sha256"],
        "stderr_sha256": sha256(stderr) == record["stderr_sha256"],
    }
    if not all(checks.values()):
        raise AssertionError((tag, checks))
    output = stdout.read_text(encoding="utf-8", errors="replace")
    error = stderr.read_text(encoding="utf-8", errors="replace")
    markers = record.get("markers", {})
    completed = (
        record["returncode"] == 0
        and not record["timed_out"]
        and markers.get("SCRIPT_DONE") is True
        and "? error occurred" not in output
        and "? error occurred" not in error
    )
    exact_unit = (
        identity[2] == "Q"
        and completed
        and record.get("clean_unit") is True
        and markers.get("UNIT") in (True, "1", 1)
        and markers.get("NF_ALL_ZERO") in (True, "1", 1)
        and markers.get("REDUCE_ONE") in ("0", 0)
        and markers.get("BASIS_SIZE") in ("1", 1)
        and markers.get("DIM") in ("-1", -1)
        and markers.get("LEAD_DIM") in ("-1", -1)
    )
    status = "EXACT_Q_UNIT" if exact_unit else ("COMPLETED_NONUNIT" if completed else "COMPUTE_BOUND")
    return {
        "tag": tag,
        "skeleton": identity[0],
        "component": identity[1],
        "field": identity[2],
        "status": status,
        "returncode": record["returncode"],
        "timed_out": record["timed_out"],
        "wall_seconds": record["elapsed_seconds"],
        "maximum_process_group_rss_kb": record["maximum_process_group_rss_kb"],
        "markers": markers,
        "clean_unit": record.get("clean_unit", False),
        "record": str(record_path.relative_to(ROOT)),
        "record_sha256": sha256(record_path),
        "script": str(script.relative_to(ROOT)),
        "script_sha256": record["script_sha256"],
        "stdout": str(stdout.relative_to(ROOT)),
        "stdout_sha256": record["stdout_sha256"],
        "stderr": str(stderr.relative_to(ROOT)),
        "stderr_sha256": record["stderr_sha256"],
        "custody_checks": checks,
    }


def main() -> None:
    runs = [inspect(tag, identity) for tag, identity in EXPECTED.items()]
    verdicts: dict[str, Any] = {}
    for skeleton in ("S5", "S6"):
        owned = [run for run in runs if run["skeleton"] == skeleton]
        exact_units = [run for run in owned if run["status"] == "EXACT_Q_UNIT"]
        completed_nonunits = [run for run in owned if run["status"] == "COMPLETED_NONUNIT"]
        # A survivor additionally requires a full-row exact basis, dimension,
        # and reconstructed exact point.  This lane has no such artifact.
        if exact_units:
            verdict = "RE-CERTIFIED DEAD"
        elif completed_nonunits:
            verdict = "UNRESOLVED_COMPLETED_NONUNIT"
        else:
            verdict = "COMPUTE-BOUND"
        verdicts[skeleton] = {
            "verdict": verdict,
            "exact_q_units": len(exact_units),
            "completed_nonunit_runs": len(completed_nonunits),
            "compute_bound_runs": sum(run["status"] == "COMPUTE_BOUND" for run in owned),
            "survivor_certificate": None,
        }
    payload = {
        "schema": "jc2.s56-recert.requested-run-summary/v1",
        "promotion_policy": {
            "dead": "exact-Q UNIT with rc=0, complete markers, NF all zero, reduce(1)=0, basis size 1, dimension and lead dimension -1",
            "survives": "full-row exact basis and dimension plus a reconstructed exact sample point",
            "timeout": "compute-bound only",
            "modular_unit": "screen only; exact-Q confirmation required",
        },
        "requested_run_count": len(runs),
        "all_custody_checks_pass": all(all(run["custody_checks"].values()) for run in runs),
        "runs": runs,
        "verdicts": verdicts,
        "script": str(Path(__file__).relative_to(ROOT)),
        "script_sha256": sha256(Path(__file__)),
    }
    output = HERE / "requested-runs-summary.json"
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
