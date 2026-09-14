#!/usr/bin/env python3
"""Print a compact, read-only summary of one round-3 harvest snapshot."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


IPS = (
    "172.30.0.183", "172.30.0.202", "172.30.0.108", "172.30.0.190",
    "172.30.0.121", "172.30.0.55", "172.30.0.45", "172.30.0.125",
)


def solver_process(text: str) -> tuple[str, str, float, str] | None:
    found = None
    for line in text.splitlines():
        match = re.match(r"^\s*(\d+)\s+(\S+)\s+(\d+)\s+([\d.]+)\s+(.+)$", line)
        if not match:
            continue
        pid, etime, rss, cpu, command = match.groups()
        if command.startswith("/home/ubuntu/moh-bigmem-20260905/bin/msolve"):
            found = ("msolve", etime, int(rss) / 1048576, pid)
        elif command.startswith("Singular "):
            label = "extract" if "/classdir/builders/" in command else "Singular"
            found = (label, etime, int(rss) / 1048576, pid)
    return found


def f4_state(root: Path) -> str:
    reports = []
    for path in sorted(root.rglob("*.g2.stderr")):
        lines = path.read_text(errors="replace").splitlines()
        numeric = [line for line in lines if re.match(r"^\s*\d+\s+\d+\s+\d+", line)]
        complete = [line for line in numeric if " new " in line and " zero " in line and "|" in line]
        max_degree = max((int(line.split()[0]) for line in complete), default=None)
        active = numeric[-1].strip() if numeric else "none"
        reports.append(f"{path.parent.name}:maxdone={max_degree},last={active}")
    return "; ".join(reports) or "-"


def statuses(root: Path) -> str:
    values = []
    for path in sorted(root.rglob("*.status.json")):
        try:
            obj = json.loads(path.read_text())
            values.append(f"{path.parent.name}:{obj.get('status')}/{obj.get('returncode')}")
        except Exception as exc:
            values.append(f"{path.parent.name}:BAD_JSON:{type(exc).__name__}")
    for path in sorted(root.rglob("guided_gb_result.json")):
        try:
            obj = json.loads(path.read_text())
            values.append(f"guided:{obj.get('final_verdict')}")
        except Exception as exc:
            values.append(f"guided:BAD_JSON:{type(exc).__name__}")
    for path in sorted(root.rglob("*.rc")):
        if "/extract/" in str(path):
            values.append(f"extract:rc={path.read_text(errors='replace').strip()}")
    return ",".join(values) or "RUNNING_NO_TERMINAL_ARTIFACT"


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {sys.argv[0]} HARVEST_SNAPSHOT_DIR")
    snapshot = Path(sys.argv[1])
    for ip in IPS:
        root = snapshot / ip
        poll = root / "poll.txt"
        if not poll.is_file():
            print(f"{ip} MISSING_POLL")
            continue
        text = poll.read_text(errors="replace")
        utc = re.search(r"^UTC=(\S+)", text, re.MULTILINE)
        proc = solver_process(text)
        ptext = "idle" if proc is None else f"{proc[0]} pid={proc[3]} et={proc[1]} rss={proc[2]:.1f}GiB"
        print(f"{ip} utc={utc.group(1) if utc else '?'} {ptext} status={statuses(root)}")
        progress = f4_state(root)
        if progress != "-":
            print(f"  F4 {progress}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
