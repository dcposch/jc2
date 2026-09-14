#!/usr/bin/env python3
"""Inventory short and q-only rows without invoking a solver."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


VAR = re.compile(r"(?<![A-Za-z0-9_])v\d+(?![A-Za-z0-9_])")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("--limit", type=int, default=30)
    args = parser.parse_args()
    lines = args.source.read_text(encoding="utf-8").splitlines()
    body = "\n".join(lines[2:]).strip()
    generators = [item.strip() for item in body.split(",\n") if item.strip()]
    rows = []
    for index, generator in enumerate(generators, 1):
        variables = sorted(set(VAR.findall(generator)), key=lambda item: int(item[1:]))
        rows.append({
            "index_1based": index,
            "bytes": len(generator.encode("utf-8")),
            "variables": variables,
            "generator": generator,
        })
    result = {
        "source": str(args.source.resolve()),
        "generator_count": len(generators),
        "q_only_rows": [row for row in rows if set(row["variables"]) <= {"v95", "v96"}],
        "shortest_rows": sorted(rows, key=lambda row: (row["bytes"], row["index_1based"]))[:args.limit],
        "last_two_rows": rows[-2:],
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
