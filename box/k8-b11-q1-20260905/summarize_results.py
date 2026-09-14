#!/usr/bin/env python3
"""Summarize one or more retained msolve runs without promoting screens."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


MATRIX = re.compile(r"^\s*(\d+)\s+\d+\s+\d+\s+(\d+)\s*x\s*(\d+)", re.M)


def digest(path: Path) -> str | None:
    if not path.is_file():
        return None
    return hashlib.sha256(path.read_bytes()).hexdigest()


def classify_output(path: Path) -> tuple[str, dict[str, int | str | None]]:
    if not path.is_file() or path.stat().st_size == 0:
        return "EMPTY_OUTPUT", {"characteristic": None, "basis_length": None, "dimension": None}
    text = path.read_text(encoding="utf-8", errors="replace")
    headers: dict[str, int | str | None] = {
        "characteristic": None,
        "basis_length": None,
        "dimension": None,
    }
    patterns = {
        "characteristic": r"^#field characteristic:\s*(\d+)",
        "basis_length": r"^#length of basis:\s*(\d+)",
        "dimension": r"^#dimension:\s*(-?\d+)",
    }
    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.M)
        if match:
            headers[key] = int(match.group(1))
    body = "".join(line for line in text.splitlines() if not line.startswith("#"))
    flat = re.sub(r"\s+", "", body).rstrip(":")
    if headers["characteristic"] is None or headers["basis_length"] is None:
        return "MALFORMED_OUTPUT", headers
    if not (flat.startswith("[") and flat.endswith("]")):
        return "MALFORMED_OUTPUT", headers
    if flat == "[1]":
        return (
            "UNIT_BODY" if headers["basis_length"] == 1 else "MALFORMED_OUTPUT",
            headers,
        )
    if flat in {"", "[0]"}:
        return "ZERO_OR_EMPTY", headers
    return "NONUNIT", headers


def one(root: Path, stem: str) -> dict[str, object]:
    out = root / f"{stem}.msout"
    v2 = root / f"{stem}.v2.log"
    time_file = root / f"{stem}.time"
    start = root / f"{stem}.start_ns"
    end = root / f"{stem}.end_ns"
    rc_file = root / f"{stem}.rc"
    raw_verdict, headers = classify_output(out)
    telemetry = v2.read_text(encoding="utf-8", errors="replace") if v2.is_file() else ""
    matrices = [tuple(map(int, match)) for match in MATRIX.findall(telemetry)]
    largest = max(matrices, key=lambda item: item[1] * item[2]) if matrices else None
    time_text = time_file.read_text(encoding="utf-8", errors="replace") if time_file.is_file() else ""
    rss_match = re.search(r"Maximum resident set size \(kbytes\):\s*(\d+)", time_text)
    wall = None
    if start.is_file() and end.is_file():
        wall = (int(end.read_text().strip()) - int(start.read_text().strip())) / 1_000_000_000
    rc = int(rc_file.read_text().strip()) if rc_file.is_file() else None
    characteristic = headers["characteristic"]
    expected_characteristic = {"exact_q": 0, "mod32003": 32003}.get(stem)
    if rc is None:
        if start.is_file() and not end.is_file():
            verdict = "RUNNING"
        elif end.is_file():
            verdict = "INCOMPLETE_RESULT"
        else:
            verdict = "NOT_STARTED"
    elif rc != 0:
        verdict = "WATCHDOG_TIMEOUT" if rc == 124 else f"ENGINE_FAILURE_RC_{rc}"
    elif (
        raw_verdict == "MALFORMED_OUTPUT"
        or expected_characteristic is None
        or characteristic != expected_characteristic
    ):
        verdict = "MALFORMED_OR_HEADER_MISMATCH"
    elif raw_verdict == "UNIT_BODY":
        verdict = (
            "FIRST_PRIME_UNIT_TRACE"
            if characteristic == 0
            else "MODULAR_UNIT_SCREEN"
        )
    elif raw_verdict == "NONUNIT":
        verdict = (
            "NONUNIT_Q_BASIS"
            if characteristic == 0
            else "MODULAR_NONUNIT_SCREEN"
        )
    else:
        verdict = raw_verdict
    return {
        "stem": stem,
        "rc": rc,
        "classification": verdict,
        "raw_output_classification": raw_verdict,
        **headers,
        "wall_seconds_ns": wall,
        "peak_rss_kb": int(rss_match.group(1)) if rss_match else None,
        "max_f4_degree": max((item[0] for item in matrices), default=None),
        "largest_f4_matrix_by_entries": (
            {"degree": largest[0], "rows": largest[1], "columns": largest[2]}
            if largest else None
        ),
        "output_bytes": out.stat().st_size if out.is_file() else 0,
        "output_sha256": digest(out),
        "v2_sha256": digest(v2),
        "time_sha256": digest(time_file),
        "custody": (root / f"{stem}.custody").read_text(encoding="utf-8", errors="replace")
        if (root / f"{stem}.custody").is_file() else None,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("stems", nargs="+")
    args = parser.parse_args()
    data = {stem: one(args.root, stem) for stem in args.stems}
    args.output.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(data, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
