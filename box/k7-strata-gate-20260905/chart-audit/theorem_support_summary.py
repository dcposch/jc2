#!/usr/bin/env python3
"""Summarize exact x,y supports of the omitted MASTER coefficient rows."""
from __future__ import annotations

import json
import re
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUTDIR = HERE / "theorem-rows"


def exponent(mon: str, var: str) -> int:
    match = re.search(rf"(?:^|\*){var}(?:\^(\d+))?(?:\*|$)", mon)
    if not match:
        return 0
    return int(match.group(1) or 1)


def compress(values: list[int]) -> str:
    if not values:
        return ""
    runs = []
    start = prev = values[0]
    for value in values[1:]:
        if value == prev + 1:
            prev = value
            continue
        runs.append(str(start) if start == prev else f"{start}..{prev}")
        start = prev = value
    runs.append(str(start) if start == prev else f"{start}..{prev}")
    return ",".join(runs)


def main() -> None:
    charts = []
    for b in range(9, 14):
        for pin in (0, 1):
            path = OUTDIR / f"K7_B{b}_Q{pin}_theorem_rows.out"
            item = {"b": b, "pin": pin, "path": str(path.relative_to(HERE.parent.parent.parent))}
            if not path.exists():
                item["status"] = "MISSING"
                charts.append(item)
                continue
            text = path.read_text()
            if "DROP__DONE 1" not in text:
                item["status"] = "INCOMPLETE"
                charts.append(item)
                continue
            rows = []
            markers = {}
            for line in text.splitlines():
                if line.startswith("DROP__ROW "):
                    match = re.fullmatch(r"DROP__ROW (\S+) DEG (\d+)", line)
                    assert match
                    mon = match.group(1)
                    deg = int(match.group(2))
                    xp, yp = exponent(mon, "x"), exponent(mon, "y")
                    assert xp + yp == deg and deg > 13
                    rows.append({"monomial": mon, "degree": deg, "x": xp, "y": yp})
                elif line.startswith("DROP__") or line.startswith("PRE__THEOREM"):
                    key, *rest = line.split(maxsplit=1)
                    markers[key] = rest[0] if rest else ""
            assert int(markers["DROP__RAW"]) == len(rows)
            by_degree = {}
            for row in rows:
                by_degree.setdefault(row["degree"], []).append(row["y"])
            by_degree = {
                str(deg): {
                    "count": len(set(ys)),
                    "y_exponents": compress(sorted(set(ys))),
                }
                for deg, ys in sorted(by_degree.items())
            }
            item.update(
                status="COMPLETE",
                cutoff=int(markers["PRE__THEOREM_CUTOFF"]),
                raw_rows=len(rows),
                simplified_rows=int(markers["PRE__THEOREM_ROWS"]),
                degree_min=min(row["degree"] for row in rows),
                degree_max=max(row["degree"] for row in rows),
                support_by_degree=by_degree,
                explicit_monomials=[row["monomial"] for row in rows],
            )
            charts.append(item)
    print(json.dumps({"charts": charts}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
