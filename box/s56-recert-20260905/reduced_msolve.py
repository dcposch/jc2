#!/usr/bin/env python3
"""Convert a checked triangular dump to an msolve modular screening system."""

from __future__ import annotations

import argparse
from dataclasses import asdict
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import socket
import time

import msolveio


IDENTIFIER = re.compile(r"[A-Za-z][A-Za-z0-9_]*")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def atomic_write(path: Path, payload: str) -> None:
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(payload, encoding="utf-8")
    temporary.replace(path)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def parse_dump(path: Path) -> tuple[list[str], list[str], dict[str, int]]:
    text = path.read_text(encoding="utf-8", errors="strict")
    if text.splitlines().count("SCRIPT_DONE") != 1:
        raise ValueError("dump does not contain exactly one SCRIPT_DONE")
    triangular = re.findall(
        r"^TRIANGULAR_OK pivots=(\d+) source_rows=(\d+)\s+residual_rows=(\d+) "
        r"active_including_T=(\d+)\s*$",
        text,
        re.M,
    )
    if len(triangular) != 1:
        raise ValueError("dump does not contain exactly one TRIANGULAR_OK")
    pivots, source_rows, residual_rows, active = map(int, triangular[0])
    if len(re.findall(r"^PIVOT_OK ", text, re.M)) != pivots:
        raise ValueError("dump pivot-marker count differs from TRIANGULAR_OK")
    if len(re.findall(r"^IDEAL_SUBST_OK ", text, re.M)) != pivots:
        raise ValueError("dump substitution-marker count differs from TRIANGULAR_OK")
    variables: list[str] | None = None
    rows: list[str] = []
    for line in text.splitlines():
        if line.startswith("DUMP__VARS "):
            if variables is not None:
                raise ValueError("ambiguous DUMP__VARS marker")
            variables = line.removeprefix("DUMP__VARS ").split(",")
        elif line.startswith("DUMP__ROW "):
            rows.append(line.removeprefix("DUMP__ROW ").strip())
    if not variables or not rows:
        raise ValueError("dump lacks variables or rows")
    count_matches = re.findall(r"^DUMP__COUNT (\d+)\s*$", text, re.M)
    if count_matches != [str(len(rows))]:
        raise ValueError(f"dump row-count marker mismatch: {count_matches} versus {len(rows)}")
    if len(variables) != len(set(variables)):
        raise ValueError("duplicate dumped variables")
    if len(rows) != residual_rows or len(variables) != active:
        raise ValueError("dump payload counts differ from TRIANGULAR_OK")
    return variables, rows, {
        "pivots": pivots,
        "source_rows": source_rows,
        "residual_rows": residual_rows,
        "active_variables": active,
    }


def translate(variables: list[str], rows: list[str]) -> tuple[list[str], list[str], dict[str, str]]:
    mapping = {name: f"v{index}" for index, name in enumerate(variables)}
    translated: list[str] = []
    for index, row in enumerate(rows):
        identifiers = set(IDENTIFIER.findall(row))
        unknown = identifiers - set(mapping)
        if unknown:
            raise ValueError(f"row {index} has unknown identifiers: {sorted(unknown)}")
        changed = IDENTIFIER.sub(lambda match: mapping[match.group(0)], row)
        inverse = {value: key for key, value in mapping.items()}
        roundtrip = IDENTIFIER.sub(lambda match: inverse[match.group(0)], changed)
        if roundtrip != row:
            raise ValueError(f"row {index} rename did not round-trip")
        translated.append(changed)
    return [mapping[name] for name in variables], translated, mapping


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dump", type=Path, required=True)
    parser.add_argument("--dump-run", type=Path, required=True)
    parser.add_argument("--script", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--tag", required=True)
    parser.add_argument("--characteristic", type=int, required=True)
    parser.add_argument("--timeout", type=float, default=900)
    parser.add_argument("--threads", type=int, default=1)
    parser.add_argument("--cpu", type=int)
    args = parser.parse_args()
    if args.characteristic <= 0:
        raise ValueError("this helper is a finite-field screen only")
    if args.cpu is not None:
        os.sched_setaffinity(0, {args.cpu})

    dump = args.dump.resolve()
    dump_run = args.dump_run.resolve()
    script = args.script.resolve()
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    run_record = json.loads(dump_run.read_text(encoding="utf-8"))
    if run_record.get("returncode") != 0 or run_record.get("timed_out"):
        raise ValueError("dump run was not a clean completed process")
    if run_record.get("script_sha256") != sha256(script):
        raise ValueError("dump-run/script SHA-256 mismatch")
    if run_record.get("stdout_sha256") != sha256(dump):
        raise ValueError("dump-run/stdout SHA-256 mismatch")
    script_text = script.read_text(encoding="utf-8", errors="strict")
    script_chars = re.findall(r"^// characteristic=(\d+)\s*$", script_text, re.M)
    if script_chars != [str(args.characteristic)]:
        raise ValueError("script characteristic differs from requested screen")
    variables, rows, dump_counts = parse_dump(dump)
    safe_variables, safe_rows, mapping = translate(variables, rows)
    source = msolveio.emit_system(
        safe_rows, variables=safe_variables, characteristic=args.characteristic
    )
    input_path = output_dir / f"{args.tag}.ms"
    record_path = output_dir / f"{args.tag}.json"
    atomic_write(input_path, source)
    started = time.monotonic()
    started_utc = utc_now()
    result = msolveio.run_groebner(
        source,
        gb=2,
        timeout=args.timeout,
        threads=args.threads,
        allow_unknown_version=True,
    )
    elapsed = time.monotonic() - started
    record = {
        "schema": "jc2.s56-recert.reduced-msolve/v1",
        "host": socket.gethostname(),
        "started_utc": started_utc,
        "finished_utc": utc_now(),
        "characteristic": args.characteristic,
        "screen_only": True,
        "dump": str(dump),
        "dump_sha256": sha256(dump),
        "dump_run": str(dump_run),
        "dump_run_sha256": sha256(dump_run),
        "dump_counts": dump_counts,
        "triangular_script": str(script),
        "triangular_script_sha256": sha256(script),
        "variable_count": len(variables),
        "generator_count": len(rows),
        "variable_map": mapping,
        "msolve_input": str(input_path),
        "msolve_input_sha256": sha256(input_path),
        "msolveio_version": getattr(msolveio, "__version__", "unknown"),
        "runner_elapsed_seconds": round(elapsed, 6),
        "result": asdict(result),
    }
    atomic_write(record_path, json.dumps(record, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "record": str(record_path),
        "unit_ideal": result.output.unit_ideal,
        "wall_seconds": result.wall_seconds,
        "returncode": result.returncode,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
