#!/usr/bin/env python3
"""Runner for the qqideal parallel-oracle window.

Always runs the three charged Fraction self-checks (no msolve). Then,
unless --self-check-only, executes the five corrected incidence jobs
against qqideal 0.1.0 and diffs Kind against the old-stack records
hard-coded from the charged reports.

P1 disagreement (including TIMEOUT/ERROR) prints ORACLE-P0 and exits 2.
Never tests a Verdict as a boolean.

Usage:
  python3 box/qq_oracle_run.py --self-check
  python3 box/qq_oracle_run.py
  python3 box/qq_oracle_run.py --jobs p1_863,p3_964

Env:
  MSOLVE_BINARY        pin msolve 0.10.1 (path prepended for qqideal)
  QQ_ORACLE_TIMEOUT    seconds, default 3600
  QQ_ORACLE_THREADS    unused by qqideal.verdict; recorded for custody
"""
from __future__ import annotations

import argparse
import os
import sys
import traceback
from typing import Dict, List, Optional, Sequence, Tuple

# Allow `python3 box/qq_oracle_run.py` from the repo root.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from qq_oracle_jobs import (  # noqa: E402
    JOBS,
    SPECS,
    run_self_checks,
)

# Old-stack records, hard-coded from the charged reports. Not inferred.
# P1: kill-review lines 7-8, 321-323, 476-488 (two-engine EMPTY of Iopen).
# P2: pending (codegen: no Groebner run; audit 7.2 OPEN/RECOMPUTE).
# P3: corrected locus NONEMPTY by HF-twin (desk), nodal OPEN; raw EMPTY vacated.
# P4a: raw A NONEMPTY vacated as unfaithful (audit 7.2 line 517).
# P4b: raw C pending vacated (audit 7.2 line 519); not a raw-NONEMPTY.
OLD_STACK: Dict[str, dict] = {
    "p1_863": {
        "record": "EMPTY",
        "binding": True,
        "note": (
            "two-engine, binding: corrected_863.ms basis=[1] and patched "
            "corrected_863.m2 Iopen==(1) over char 0, before cover colon "
            "(kill-review KILL-BINDING)"
        ),
    },
    "p2_869": {
        "record": "PENDING",
        "binding": False,
        "note": "corrected B not an as-run charged Groebner; record fresh",
    },
    "p3_964": {
        "record": "PENDING",
        "binding": False,
        "note": (
            "corrected 96A incidence known NONEMPTY by HF-twin (desk, "
            "self-check iii); nodal six-node OPEN; raw EMPTY vacated. "
            "Record the qqideal Iopen verdict fresh; do not promote"
        ),
    },
    "p4a_8611": {
        "record": "VACATED",
        "binding": False,
        "note": (
            "raw A was NONEMPTY, vacated as unfaithful (audit 7.2). "
            "Corrected system decides fresh; do not assume EMPTY or NONEMPTY"
        ),
    },
    "p4b_867": {
        "record": "VACATED",
        "binding": False,
        "note": (
            "raw C was pending, vacated (audit 7.2). Prompt's "
            "raw-NONEMPTY->vacated applies to P4a; P4b was not nonempty. "
            "Corrected system decides fresh; do not assume"
        ),
    },
}


def _kind_of(verdict) -> str:
    return verdict.kind.value


def _certainty_of(verdict) -> str:
    return verdict.certainty.value


def diff_against_old(job_id: str, verdict) -> Tuple[str, bool]:
    """Return (status_tag, is_p0).

    P1: any Kind other than EMPTY is P0, including TIMEOUT and ERROR.
    Other jobs: record fresh; never P0 from a Kind mismatch.
    """
    old = OLD_STACK[job_id]
    kind = _kind_of(verdict)
    if old["binding"]:
        if kind == "empty":
            return "AGREE-EMPTY", False
        return f"ORACLE-P0 old={old['record']} new={kind}", True
    # non-binding: classify, do not fail the process
    if old["record"] == "PENDING":
        return f"FRESH kind={kind}", False
    if old["record"] == "VACATED":
        return f"FRESH-AFTER-VACATE kind={kind}", False
    return f"FRESH kind={kind}", False


def print_table(rows: List[dict]) -> None:
    headers = (
        "job", "Delta", "kind", "certainty", "dim", "degree",
        "old-stack", "diff", "msolve", "sha256[:16]", "wall_s",
    )
    table: List[List[str]] = [list(headers)]
    for row in rows:
        table.append([
            row["job"],
            str(row["delta"]),
            row["kind"],
            row["certainty"],
            str(row["dim"]),
            str(row["degree"]),
            row["old"],
            row["diff"],
            str(row["msolve"]),
            row["sha16"],
            row["wall"],
        ])
    widths = [max(len(r[c]) for r in table) for c in range(len(headers))]
    def fmt(r: List[str]) -> str:
        return "  ".join(r[c].ljust(widths[c]) for c in range(len(headers)))
    print()
    print("=== qqideal oracle verdict table ===")
    print(fmt(table[0]))
    print("  ".join("-" * w for w in widths))
    for r in table[1:]:
        print(fmt(r))
    print()
    print(
        "Certainty: unit ideal over Q is MODULAR (msolve 0.10.1 returns "
        "after the first modular prime). NONEMPTY over Q is PROVEN "
        "(lifted -g 2). TIMEOUT/ERROR are not answers."
    )


def run_jobs(job_ids: Sequence[str], timeout: float, binary: Optional[str]) -> int:
    from qqideal import Kind  # type: ignore  # box-only

    rows = []
    p0 = False
    p0_reasons: List[str] = []
    for job_id in job_ids:
        spec = SPECS[job_id]
        fn = JOBS[job_id]
        print(f"--- running {job_id} Delta={spec.delta} timeout={timeout}s ---")
        try:
            verdict, custody = fn(timeout=timeout, binary=binary)
        except Exception as exc:  # noqa: BLE001 — crashes are not EMPTY
            traceback.print_exc()
            is_p0 = bool(OLD_STACK[job_id]["binding"])
            diff = (
                f"ORACLE-P0 old=EMPTY new=exception:{type(exc).__name__}"
                if is_p0
                else f"exception:{type(exc).__name__}"
            )
            rows.append({
                "job": job_id,
                "delta": spec.delta,
                "kind": f"exception:{type(exc).__name__}",
                "certainty": "n/a",
                "dim": None,
                "degree": None,
                "old": OLD_STACK[job_id]["record"],
                "diff": diff,
                "msolve": None,
                "sha16": "",
                "wall": "",
            })
            if is_p0:
                p0 = True
                p0_reasons.append(diff)
            continue

        # Branch on kind explicitly. TIMEOUT/ERROR are not answers.
        kind = verdict.kind
        if kind is Kind.TIMEOUT or kind is Kind.ERROR:
            print(f"{job_id}: non-answer kind={kind.value} detail={verdict.detail!r}")
        elif kind is Kind.EMPTY:
            print(
                f"{job_id}: EMPTY certainty={verdict.certainty.value} "
                f"version={verdict.msolve_version}"
            )
        elif kind is Kind.NONEMPTY:
            print(
                f"{job_id}: NONEMPTY certainty={verdict.certainty.value} "
                f"dim={verdict.dim} degree={verdict.degree} "
                f"version={verdict.msolve_version}"
            )
        else:
            print(f"{job_id}: unhandled kind={kind}")

        diff, is_p0 = diff_against_old(job_id, verdict)
        print(f"{job_id}: old-stack={OLD_STACK[job_id]['record']}  {diff}")
        print(f"{job_id}: {OLD_STACK[job_id]['note']}")
        if job_id == "p3_964":
            print(f"{job_id}: I_DP schema ring={custody.get('idp_schema_ring')}")
            print(f"{job_id}: {custody.get('idp_note')}")
        rows.append({
            "job": job_id,
            "delta": spec.delta,
            "kind": _kind_of(verdict),
            "certainty": _certainty_of(verdict),
            "dim": verdict.dim,
            "degree": verdict.degree,
            "old": OLD_STACK[job_id]["record"],
            "diff": diff,
            "msolve": custody.get("msolve_version"),
            "sha16": (custody.get("input_sha256") or "")[:16],
            "wall": f"{custody.get('wall_seconds'):.3f}"
            if isinstance(custody.get("wall_seconds"), (int, float)) else "",
        })
        if is_p0:
            p0 = True
            p0_reasons.append(diff)

    print_table(rows)
    if p0:
        print()
        print("=" * 72)
        print("ORACLE-P0")
        print("ORACLE-P0  P1 (8,6,3) disagreed with the charged two-engine EMPTY")
        print("ORACLE-P0  of the corrected Iopen, or failed to produce a Kind.")
        for reason in p0_reasons:
            print(f"ORACLE-P0  {reason}")
        print("=" * 72)
        return 2
    return 0


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--self-check",
        "--self-check-only",
        dest="self_check_only",
        action="store_true",
        help="run Fraction self-checks and exit (no qqideal, no msolve)",
    )
    parser.add_argument(
        "--jobs",
        default="p1_863,p2_869,p3_964,p4a_8611,p4b_867",
        help="comma-separated job ids",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=float(os.environ.get("QQ_ORACLE_TIMEOUT", "3600")),
        help="msolve wall-clock timeout per job (seconds)",
    )
    parser.add_argument(
        "--binary",
        default=os.environ.get("MSOLVE_BINARY"),
        help="msolve 0.10.1 binary; directory is prepended to PATH",
    )
    args = parser.parse_args(argv)

    print("qqideal-oracle-codegen  self-checks (Fraction, no msolve)")
    ok, transcript = run_self_checks()
    print("\n".join(transcript))
    if not ok:
        print("self-checks FAILED; refusing to run oracle jobs", file=sys.stderr)
        return 1
    if args.self_check_only:
        return 0

    job_ids = [j.strip() for j in args.jobs.split(",") if j.strip()]
    unknown = [j for j in job_ids if j not in JOBS]
    if unknown:
        print(f"unknown jobs: {unknown}", file=sys.stderr)
        return 1
    return run_jobs(job_ids, timeout=args.timeout, binary=args.binary)


if __name__ == "__main__":
    sys.exit(main())
