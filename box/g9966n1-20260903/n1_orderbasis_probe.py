#!/usr/bin/env python3
"""Scoped order-basis probes for the (99,66) N1 u_s=1 skeletons.

This driver imports the frozen-hash live copy of order_basis_full.py, redirects
its artifact root into this lane directory, and runs only the two small
descended rows coming from the u_s=1 Moh skeletons.  It does not edit ledgers.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
from pathlib import Path
import re
import signal
import subprocess
import sys
import time
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[2]
HERE = ROOT / "box" / "g9966n1-20260903"
OUT = HERE / "orderbasis"
ORDER_BASIS = ROOT / "box" / "orderbasis-20260903" / "order_basis_full.py"

CHARS = (0, 32003, 32009, 32027)


def atomic_write(path: Path, payload: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(payload, encoding="utf-8")
    tmp.replace(path)


def load_order_basis() -> Any:
    spec = importlib.util.spec_from_file_location("order_basis_full_live", ORDER_BASIS)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {ORDER_BASIS}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    module.ROOT = ROOT
    module.HERE = OUT
    module.manifest_check = lambda: {"ok": True, "note": "checked by parent N1 lane"}
    return module


def custom_rows(ob: Any) -> dict[str, Any]:
    Row = ob.Row
    return {
        "S5": Row(
            "n1_S5_9_6_2_1_k5",
            "N1 S5 descent from (99,66; M2=22,V3=10,V2=1,u_s=1)",
            9,
            6,
            2,
            1,
            5,
        ),
        "S6": Row(
            "n1_S6_9_6_5_2_k2",
            "N1 S6 descent from (99,66; M2=55,V3=10,V2=2,u_s=1)",
            9,
            6,
            5,
            2,
            2,
        ),
    }


def run_script(script: Path, timeout: int) -> dict[str, Any]:
    env = os.environ.copy()
    for key in (
        "OMP_NUM_THREADS",
        "OPENBLAS_NUM_THREADS",
        "MKL_NUM_THREADS",
        "NUMEXPR_NUM_THREADS",
        "FLINT_NUM_THREADS",
    ):
        env[key] = "1"
    out_path = Path(str(script) + ".out")
    err_path = Path(str(script) + ".err")
    cmd = [
        "timeout",
        f"{timeout}s",
        "stdbuf",
        "-oL",
        "-eL",
        "Singular",
        "--cpus=1",
        "--threads=1",
        "--flint-threads=1",
        "--no-rc",
        "-q",
        str(script),
    ]
    started = time.monotonic()
    with out_path.open("w", encoding="utf-8", errors="replace") as out, err_path.open(
        "w", encoding="utf-8", errors="replace"
    ) as err:
        proc = subprocess.Popen(
            cmd,
            cwd=ROOT,
            env=env,
            stdout=out,
            stderr=err,
            text=True,
            start_new_session=True,
        )
        try:
            proc.wait(timeout=timeout + 15)
        except subprocess.TimeoutExpired:
            os.killpg(proc.pid, signal.SIGTERM)
            try:
                proc.wait(timeout=10)
            except subprocess.TimeoutExpired:
                os.killpg(proc.pid, signal.SIGKILL)
                proc.wait()
        except KeyboardInterrupt:
            os.killpg(proc.pid, signal.SIGTERM)
            raise
    stdout = out_path.read_text(encoding="utf-8", errors="replace")
    stderr = err_path.read_text(encoding="utf-8", errors="replace")
    if "MAIN_SATURATED_EMPTY" in stdout:
        verdict = "SATURATED-EMPTY"
    elif "MAIN_NONTRIVIAL" in stdout:
        verdict = "NONTRIVIAL"
    elif "NATIVE_DONE" in stdout:
        verdict = "BUILDER-DONE"
    elif proc.returncode == 124:
        verdict = "TIMEOUT"
    else:
        verdict = "ERROR"
    return {
        "script": str(script.relative_to(ROOT)),
        "command": cmd,
        "returncode": proc.returncode,
        "elapsed_seconds": round(time.monotonic() - started, 3),
        "stdout": str(out_path.relative_to(ROOT)),
        "stderr": str(err_path.relative_to(ROOT)),
        "verdict": verdict,
        "stdout_tail": stdout.splitlines()[-30:],
        "stderr_tail": stderr.splitlines()[-30:],
    }


def prepare(rows: Iterable[str]) -> dict[str, Any]:
    ob = load_order_basis()
    rows_by_id = custom_rows(ob)
    records = []
    for row_id in rows:
        row = rows_by_id[row_id]
        for part in ob.allowed_partitions(row):
            emitted = ob.write_native_builder(row, part)
            records.append(
                {
                    "row_id": row_id,
                    "row": ob.asdict(row),
                    "partition": list(part),
                    "builder": emitted["builder"],
                    "meta_path": emitted["meta_path"],
                    "rows_path": emitted["rows_path"],
                    "closed_form": emitted["meta"]["closed_form"],
                }
            )
    payload = {"rows": records}
    atomic_write(HERE / "orderbasis-prepare.json", json.dumps(payload, indent=2, sort_keys=True) + "\n")
    return payload


def build_rows(timeout: int) -> dict[str, Any]:
    prep = json.loads((HERE / "orderbasis-prepare.json").read_text(encoding="utf-8"))
    runs = []
    for rec in prep["rows"]:
        runs.append(run_script(ROOT / rec["builder"], timeout))
    payload = {"builder_runs": runs}
    atomic_write(HERE / "orderbasis-builder-runs.json", json.dumps(payload, indent=2, sort_keys=True) + "\n")
    return payload


def emit_systems(chars: Iterable[int]) -> dict[str, Any]:
    ob = load_order_basis()
    prep = json.loads((HERE / "orderbasis-prepare.json").read_text(encoding="utf-8"))
    records = []
    for rec in prep["rows"]:
        meta = ROOT / rec["meta_path"]
        for ch in chars:
            records.append({"row_id": rec["row_id"], "partition": rec["partition"], **ob.write_system_from_rows(meta, ch, "std")})
    payload = {"systems": records}
    atomic_write(HERE / "orderbasis-systems.json", json.dumps(payload, indent=2, sort_keys=True) + "\n")
    return payload


def solve(timeout: int) -> dict[str, Any]:
    systems = json.loads((HERE / "orderbasis-systems.json").read_text(encoding="utf-8"))["systems"]
    def solve_key(item: dict[str, Any]) -> tuple[int, int, str, str, int]:
        char = 0
        name = item["system"]
        match = re.search(r"_p([0-9]+)_", Path(name).name)
        if match:
            char = int(match.group(1))
        char_order = {32003: 0, 32009: 1, 32027: 2, 0: 3}.get(char, 4)
        return (
            int(item["unknowns"]),
            int(item["equations"]),
            item["row_id"],
            "+".join(map(str, item["partition"])),
            char_order,
        )
    systems = sorted(systems, key=solve_key)
    runs = []
    for rec in systems:
        run = run_script(ROOT / rec["system"], timeout)
        runs.append({**rec, "run": run})
    payload = {"solve_runs": runs}
    atomic_write(HERE / "orderbasis-solve-runs.json", json.dumps(payload, indent=2, sort_keys=True) + "\n")
    return payload


def summarize() -> dict[str, Any]:
    prep = json.loads((HERE / "orderbasis-prepare.json").read_text(encoding="utf-8"))
    builders = json.loads((HERE / "orderbasis-builder-runs.json").read_text(encoding="utf-8"))
    systems = json.loads((HERE / "orderbasis-systems.json").read_text(encoding="utf-8"))
    solves = json.loads((HERE / "orderbasis-solve-runs.json").read_text(encoding="utf-8"))
    payload = {
        "prepared": prep,
        "builder_runs": builders,
        "systems": systems,
        "solve_runs": solves,
        "verdict_by_row_partition": {},
    }
    for item in solves["solve_runs"]:
        key = f"{item['row_id']}:{'+'.join(map(str, item['partition']))}"
        payload["verdict_by_row_partition"].setdefault(key, []).append(
            {
                "system": item["system"],
                "verdict": item["run"]["verdict"],
                "returncode": item["run"]["returncode"],
                "elapsed_seconds": item["run"]["elapsed_seconds"],
            }
        )
    atomic_write(HERE / "orderbasis-summary.json", json.dumps(payload, indent=2, sort_keys=True) + "\n")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("prepare", "build-rows", "emit-systems", "solve", "all", "summary"))
    parser.add_argument("--rows", default="S5,S6")
    parser.add_argument("--chars", default=",".join(map(str, CHARS)))
    parser.add_argument("--builder-timeout", type=int, default=180)
    parser.add_argument("--solve-timeout", type=int, default=600)
    args = parser.parse_args()

    rows = [piece for piece in args.rows.split(",") if piece]
    chars = [int(piece) for piece in args.chars.split(",") if piece]
    if args.command == "prepare":
        result = prepare(rows)
    elif args.command == "build-rows":
        result = build_rows(args.builder_timeout)
    elif args.command == "emit-systems":
        result = emit_systems(chars)
    elif args.command == "solve":
        result = solve(args.solve_timeout)
    elif args.command == "summary":
        result = summarize()
    else:
        prepare(rows)
        build_rows(args.builder_timeout)
        emit_systems(chars)
        solve(args.solve_timeout)
        result = summarize()
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
