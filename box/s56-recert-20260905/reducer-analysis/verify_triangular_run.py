#!/usr/bin/env python3
"""Independent custody/marker verifier for triangular-preprocessed runs."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

import triangular_preprocess as tp


ROOT = Path(__file__).resolve().parents[3]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def one(pattern: str, text: str, field: str) -> str:
    values = re.findall(pattern, text, flags=re.MULTILINE)
    if len(values) != 1:
        raise ValueError(f"expected one {field}, found {len(values)}")
    return values[0]


def int_marker(label: str, text: str) -> int:
    return int(one(rf"^{re.escape(label)}\s+(-?\d+)\s*$", text, label))


def parse_time(path: Path | None) -> dict | None:
    if path is None or not path.exists():
        return None
    text = path.read_text(encoding="utf-8", errors="replace")
    fields = {}
    patterns = {
        "elapsed_wall": r"Elapsed \(wall clock\) time[^:]*:\s*(.+)",
        "maximum_rss_kb": r"Maximum resident set size \(kbytes\):\s*(\d+)",
        "exit_status": r"Exit status:\s*(-?\d+)",
        "user_seconds": r"User time \(seconds\):\s*(.+)",
        "system_seconds": r"System time \(seconds\):\s*(.+)",
    }
    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        if match:
            value: str | int = match.group(1).strip()
            if key in {"maximum_rss_kb", "exit_status"}:
                value = int(value)
            fields[key] = value
    return fields


def verify(args: argparse.Namespace) -> dict:
    meta = args.meta.resolve()
    plan_path = args.plan.resolve()
    script = args.script.resolve()
    stdout_path = args.stdout.resolve()
    stderr_path = args.stderr.resolve()
    time_path = args.time.resolve() if args.time else None
    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    recomputed = tp.plan_record(meta, include_c=plan["include_c"])
    if plan != recomputed:
        raise ValueError("stored pivot plan differs from independent recomputation")

    script_text = script.read_text(encoding="utf-8", errors="strict")
    stdout = stdout_path.read_text(encoding="utf-8", errors="replace")
    stderr = stderr_path.read_text(encoding="utf-8", errors="replace")
    expected_meta_hash = sha256(meta)
    expected_rows_hash = recomputed["rows_sha256"]
    if f"// meta_sha256={expected_meta_hash}" not in script_text:
        raise ValueError("script/meta custody mismatch")
    if f"// rows_sha256={expected_rows_hash}" not in script_text:
        raise ValueError("script/rows custody mismatch")
    characteristic = int(one(r"^// characteristic=(\d+)\s*$", script_text, "characteristic"))
    branch = one(r"^// branch=([A-Za-z0-9_-]+)\s*$", script_text, "branch")

    planned = [(item["step"], item["variable"]) for item in plan["pivot_order"]]
    pivot_markers = [
        (int(step), variable)
        for step, variable in re.findall(r"^PIVOT_OK step=(\d+) variable=([A-Za-z0-9_]+)\s*$", stdout, re.M)
    ]
    if pivot_markers != planned:
        raise ValueError("runtime pivot sequence differs from stored acyclic plan")
    if "PIVOT_" in stderr and "FAIL" in stderr:
        raise ValueError("pivot failure marker in stderr")
    if "SCRIPT_DONE" not in stdout:
        raise ValueError("missing SCRIPT_DONE")

    triangular_match = re.findall(
        r"^TRIANGULAR_OK pivots=(\d+) source_rows=(\d+)\s+residual_rows=(\d+) active_including_T=(\d+)\s*$",
        stdout,
        re.M,
    )
    if len(triangular_match) != 1:
        raise ValueError("missing/ambiguous TRIANGULAR_OK")
    pivots, source_rows, residual_rows, active_with_t = map(int, triangular_match[0])
    if pivots != plan["pivot_count"] or source_rows != plan["source_row_count"]:
        raise ValueError("TRIANGULAR_OK source counts disagree with plan")
    if active_with_t != plan["active_variable_count"] + 1:
        raise ValueError("TRIANGULAR_OK active-variable count disagrees with plan")

    has_std = "TRIANGULAR_STD_BEGIN" in stdout
    controls = None
    verdict = "PREPROCESS_ONLY"
    if has_std:
        controls = {
            "generator_count": int_marker("TRIANGULAR_GENERATOR_COUNT", stdout),
            "nf_all_zero": int_marker("TRIANGULAR_NF_ALL_ZERO", stdout),
            "basis_size": int_marker("TRIANGULAR_BASIS_SIZE", stdout),
            "dimension": int_marker("TRIANGULAR_DIMENSION", stdout),
            "lead_dimension": int_marker("TRIANGULAR_LEAD_DIMENSION", stdout),
            "unit": int_marker("TRIANGULAR_UNIT", stdout),
        }
        if controls["nf_all_zero"] != 1:
            raise ValueError("input-generator normal-form control failed")
        if controls["unit"] == 1:
            if not (
                controls["basis_size"] == 1
                and controls["dimension"] == -1
                and controls["lead_dimension"] == -1
            ):
                raise ValueError("unit marker lacks basis/dimension controls")
            verdict = "UNIT_IDEAL_CHAR0" if characteristic == 0 else "MODULAR_UNIT_ONLY"
        else:
            verdict = "NONUNIT_COMPLETED"

    resource = parse_time(time_path)
    if resource and resource.get("exit_status") != 0:
        raise ValueError(f"nonzero recorded exit status: {resource.get('exit_status')}")
    return {
        "schema": "jc2.s56-recert.triangular-run/v1",
        "verdict": verdict,
        "characteristic": characteristic,
        "branch": branch,
        "equivalence_scope": "explicit_acyclic_scalar_pivot_quotient_isomorphism",
        "custody": {
            "meta": str(meta.relative_to(ROOT)),
            "meta_sha256": expected_meta_hash,
            "rows": recomputed["rows"],
            "rows_sha256": expected_rows_hash,
            "plan": str(plan_path.relative_to(ROOT)),
            "plan_sha256": sha256(plan_path),
            "script": str(script.relative_to(ROOT)),
            "script_sha256": sha256(script),
            "stdout": str(stdout_path.relative_to(ROOT)),
            "stdout_sha256": sha256(stdout_path),
            "stderr": str(stderr_path.relative_to(ROOT)),
            "stderr_sha256": sha256(stderr_path),
            "time": None if time_path is None else str(time_path.relative_to(ROOT)),
            "time_sha256": None if time_path is None else sha256(time_path),
        },
        "counts": {
            "source_rows": source_rows,
            "pivots": pivots,
            "active_variables_including_T": active_with_t,
            "mapped_residual_rows": residual_rows,
        },
        "controls": controls,
        "resource": resource,
        "stderr_empty": not stderr.strip(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--meta", type=Path, required=True)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--script", type=Path, required=True)
    parser.add_argument("--stdout", type=Path, required=True)
    parser.add_argument("--stderr", type=Path, required=True)
    parser.add_argument("--time", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        record = verify(args)
    except Exception as exc:  # verifier failures are meant to be loud
        print(f"VERIFY_FAIL: {exc}", file=sys.stderr)
        raise
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(record, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
