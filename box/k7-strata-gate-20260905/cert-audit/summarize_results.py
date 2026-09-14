#!/usr/bin/env python3
"""Summarize exact-Q msolve result files without trusting basis length alone."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
EMITTED = ROOT.parent / "chart-audit" / "emitted"
RESULTS = ROOT / "results"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_ms(path: Path) -> tuple[int, int]:
    lines = path.read_text().splitlines()
    nvars = len(lines[0].split(","))
    body = "\n".join(lines[2:]).strip()
    if body.endswith(","):
        body = body[:-1]
    return nvars, len(body.split(",\n"))


def time_field(text: str, label: str) -> str | int | None:
    match = re.search(rf"^\s*{re.escape(label)}:\s*(.+)$", text, re.M)
    if not match:
        return None
    value = match.group(1).strip()
    return int(value) if value.isdigit() else value


def is_literal_unit(text: str) -> bool:
    # Do not classify from "length of basis: 1". Strip msolve comments and
    # whitespace, then demand that the entire serialized basis is literal [1]:.
    body = "".join(line for line in text.splitlines() if not line.startswith("#"))
    return re.sub(r"\s+", "", body) == "[1]:"


rows: list[dict[str, object]] = []
for b in range(9, 14):
    for q in range(2):
        stem = f"K7_B{b}_Q{q}"
        inp = EMITTED / f"{stem}_p0.ms"
        nvars, ngens = parse_ms(inp)
        for engine in ("msolve065", "msolve101"):
            prefix = RESULTS / f"{stem}_{engine}"
            rc_path, out_path, time_path = (
                prefix.with_suffix(".rc"),
                prefix.with_suffix(".out"),
                prefix.with_suffix(".time"),
            )
            rc = int(rc_path.read_text().strip()) if rc_path.exists() else None
            out = out_path.read_text() if out_path.exists() else ""
            timing = time_path.read_text() if time_path.exists() else ""
            rows.append(
                {
                    "chart": stem,
                    "b": b,
                    "q": q,
                    "nvars": nvars,
                    "ngens": ngens,
                    "input_sha256": sha256(inp),
                    "engine": engine,
                    "rc": rc,
                    "literal_unit": is_literal_unit(out),
                    "wall": time_field(timing, "Elapsed (wall clock) time (h:mm:ss or m:ss)"),
                    "max_rss_kb": time_field(timing, "Maximum resident set size (kbytes)"),
                    "result_sha256": sha256(out_path) if out_path.exists() else None,
                }
            )

print(json.dumps(rows, indent=2, sort_keys=True))
