#!/usr/bin/env python3
"""Frozen orchestrator for the four root-aware recensus lanes."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import signal
import subprocess
import sys
import tarfile
import time


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def run_stage(root: Path, out: Path, name: str, argv: list[str], cap: int,
              extra_env: dict[str, str] | None = None) -> dict[str, object]:
    stage = out / name
    stage.mkdir(parents=True, exist_ok=False)
    (stage / "COMMAND.json").write_text(json.dumps(argv, indent=2) + "\n")
    env = os.environ.copy()
    env.update({"PYTHONDONTWRITEBYTECODE": "1", "PYTHONUNBUFFERED": "1"})
    if extra_env:
        env.update(extra_env)
    started = time.time()
    timed_out = False
    with (stage / "stdout.txt").open("wb") as stdout, \
         (stage / "stderr.txt").open("wb") as stderr:
        proc = subprocess.Popen(argv, cwd=root, env=env, stdout=stdout,
                                stderr=stderr, start_new_session=True)
        (stage / "IDENTITY.json").write_text(json.dumps({
            "pid": proc.pid,
            "pgid": os.getpgid(proc.pid),
            "sid": os.getsid(proc.pid),
            "started_unix": started,
            "cap_seconds": cap,
        }, indent=2) + "\n")
        try:
            rc = proc.wait(timeout=cap)
        except subprocess.TimeoutExpired:
            timed_out = True
            os.killpg(proc.pid, signal.SIGTERM)
            try:
                rc = proc.wait(timeout=15)
            except subprocess.TimeoutExpired:
                os.killpg(proc.pid, signal.SIGKILL)
                rc = proc.wait()
    ended = time.time()
    result = {
        "name": name,
        "argv": argv,
        "returncode": rc,
        "timed_out": timed_out,
        "elapsed_seconds": round(ended - started, 6),
        "stdout_sha256": sha256(stage / "stdout.txt"),
        "stderr_sha256": sha256(stage / "stderr.txt"),
    }
    (stage / "RESULT.json").write_text(json.dumps(result, indent=2,
                                                   sort_keys=True) + "\n")
    return result


LEDGER_PATTERNS = {
    "ROOT": re.compile(r"root|TERMINAL_ROOT|SF1", re.I),
    "IV": re.compile(r"\bIV\b|IVSURV|iv_", re.I),
    "OPEN": re.compile(r"OPEN|NO_VERDICT|RESIDUE", re.I),
    "FRONTIER": re.compile(r"frontier|depth>", re.I),
}


def build_ledgers(out: Path, stages: list[dict[str, object]]) -> None:
    handles = {name: (out / f"LEDGER_{name}.txt").open("w")
               for name in LEDGER_PATTERNS}
    try:
        for stage_result in stages:
            name = str(stage_result["name"])
            log = out / name / "stdout.txt"
            for number, line in enumerate(log.read_text(errors="replace").splitlines(), 1):
                for ledger, pattern in LEDGER_PATTERNS.items():
                    if pattern.search(line):
                        handles[ledger].write(f"{name}:{number}:{line}\n")
    finally:
        for handle in handles.values():
            handle.close()


def common_stages(root: Path, out: Path) -> list[dict[str, object]]:
    py = sys.executable
    c = root / "cases"
    specs: list[tuple[str, list[str], int]] = [
        ("smoke", [py, "-u", str(c / "sigray_rootaware_smoke.py")], 120),
        ("legacy_gate", [py, "-u", str(c / "sheet6_campaign.py"), "gate"], 120),
        ("bash", [py, "-u", str(c / "sheet6_campaign.py"), "bash",
                  "--lam", "6", "--budget", "4"], 1800),
        ("bash5", [py, "-u", str(c / "sheet6_campaign.py"), "bash5"], 1800),
        ("bash6", [py, "-u", str(c / "sheet6_campaign.py"), "report"], 1800),
        ("tduniform_80", [py, "-u", str(c / "sheet6_campaign.py"),
                          "tduniform", "--tdmax", "80"], 1800),
    ]
    specs.extend((f"tdu_bash_td{td}",
                  [py, "-u", str(c / "sheet6_campaign.py"), "tduniform",
                   "--td", str(td)], 720)
                 for td in (3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    results = []
    for name, argv, cap in specs:
        result = run_stage(root, out, name, argv, cap)
        results.append(result)
        if name in ("smoke", "legacy_gate") and result["returncode"] != 0:
            break
    return results


def h3hiii_stages(root: Path, out: Path) -> list[dict[str, object]]:
    py = sys.executable
    c = root / "cases"
    specs = [
        ("smoke", [py, "-u", str(c / "sigray_rootaware_smoke.py")], 120),
        ("h3_sf1", [py, "-u", str(c / "h3_check.py")], 2400),
        ("hiii_ordinary", [py, "-u", str(c / "hiii_compose.py")], 2400),
        ("hiii_pinned", [py, "-u", str(c / "hiii_compose.py"), "pin"], 2400),
        ("hiii_af2", [py, "-u", str(c / "hiii_compose.py"), "iib"], 2400),
    ]
    results = []
    for name, argv, cap in specs:
        result = run_stage(root, out, name, argv, cap)
        results.append(result)
        if name == "smoke" and result["returncode"] != 0:
            break
    return results


def make_raised_twopole(root: Path, out: Path) -> Path:
    source = (root / "cases" / "twopole_check.py").read_text()
    replacements = {
        "SMAX, DEPTH, KMAX, NUMAX = 5, 6, 4, 48":
            "SMAX, DEPTH, KMAX, NUMAX = 8, 8, 6, 72",
        "SMULT_MAX = 12                    # diagnostic merge multiplicity-sum cap":
            "SMULT_MAX = 18                    # frozen raised diagnostic cap",
        "NU1MAX, L1MAX = 24, 4           # mu=1 IIa_0 child caps":
            "NU1MAX, L1MAX = 40, 8           # frozen raised diagnostic caps",
        "L1_MERGE_LMAX = 8               # diagnostic only; zero-charge l has no bound":
            "L1_MERGE_LMAX = 12              # frozen raised diagnostic cap",
    }
    for old, new in replacements.items():
        if source.count(old) != 1:
            raise RuntimeError(f"raised-source replacement census failed: {old!r}")
        source = source.replace(old, new)
    derived = out / "twopole_raised_effective.py"
    derived.write_text(source)
    (out / "twopole_raised_effective.sha256").write_text(
        f"{sha256(derived)}  {derived.name}\n")
    return derived


def twopole_stages(root: Path, out: Path) -> list[dict[str, object]]:
    py = sys.executable
    c = root / "cases"
    probe = root / "cases" / "sigray_rootaware_aws_recensus_r1_20260828" / "root_menu_probe.py"
    specs = [
        ("smoke", [py, "-u", str(c / "sigray_rootaware_smoke.py")], 120),
        ("root_menu_l128", [py, "-u", str(probe)], 120),
        ("twopole_default", [py, "-u", str(c / "twopole_check.py")], 1800),
    ]
    results = []
    for name, argv, cap in specs:
        result = run_stage(root, out, name, argv, cap)
        results.append(result)
        if name == "smoke" and result["returncode"] != 0:
            return results
    raised = make_raised_twopole(root, out)
    results.append(run_stage(root, out, "twopole_raised", [py, "-u", str(raised)], 5000,
                             {"PYTHONPATH": str(c)}))
    return results


def invariant_stages(root: Path, out: Path) -> list[dict[str, object]]:
    py = sys.executable
    task = root / "cases" / "sigray_rootaware_aws_recensus_r1_20260828"
    baseline_root = out / "baseline_head"
    baseline_root.mkdir()
    with tarfile.open(task / "BASELINE_HEAD.tar", "r") as archive:
        for member in archive.getmembers():
            target = (baseline_root / member.name).resolve()
            if baseline_root.resolve() not in target.parents and target != baseline_root.resolve():
                raise RuntimeError(f"unsafe baseline archive member: {member.name}")
        archive.extractall(baseline_root)
    baseline = baseline_root / "cases"
    current = root / "cases"
    inventory = task / "invariant_inventory.py"
    compare = task / "invariant_compare.py"
    specs = [
        ("smoke", [py, "-u", str(current / "sigray_rootaware_smoke.py")], 120),
        ("inventory_before", [py, "-u", str(inventory), "--source", str(baseline),
                              "--output", str(out / "before.json")], 3000),
        ("inventory_after", [py, "-u", str(inventory), "--source", str(current),
                             "--output", str(out / "after.json")], 3000),
        ("compare", [py, "-u", str(compare), "--before", str(out / "before.json"),
                     "--after", str(out / "after.json"),
                     "--output", str(out / "invariant_verdict.json")], 300),
    ]
    results = []
    for name, argv, cap in specs:
        result = run_stage(root, out, name, argv, cap)
        results.append(result)
        if result["returncode"] != 0:
            break
    return results


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lane", required=True,
                        choices=("common", "h3hiii", "twopole", "invariants"))
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=False)
    dispatch = {
        "common": common_stages,
        "h3hiii": h3hiii_stages,
        "twopole": twopole_stages,
        "invariants": invariant_stages,
    }
    results = dispatch[args.lane](root, out)
    build_ledgers(out, results)
    failures = [r for r in results if r["returncode"] != 0]
    opens = (out / "LEDGER_OPEN.txt").read_text().splitlines()
    classification = {
        "lane": args.lane,
        "all_stages_rc0": not failures,
        "failed_or_timed_out_stages": [r["name"] for r in failures],
        "open_ledger_lines": len(opens),
        "mathematical_scope": (
            "EXACT_BEFORE_AFTER_INVARIANT" if args.lane == "invariants" and not failures
            else "CENSUS_ONLY_WITH_EXPLICIT_OPEN_NO_VERDICT"
        ),
        "two_pole_cap_completeness": (
            "NO_VERDICT: multipole hostile review has ambient orbit-tree blocker"
            if args.lane == "twopole" else "NOT_APPLICABLE"
        ),
        "endpoint_claim": "NONE",
    }
    (out / "SUMMARY.json").write_text(json.dumps({
        "classification": classification,
        "stages": results,
    }, indent=2, sort_keys=True) + "\n")
    return 0 if not failures else 2


if __name__ == "__main__":
    raise SystemExit(main())
