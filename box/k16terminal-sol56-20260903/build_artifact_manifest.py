#!/usr/bin/env python3
"""Write a deterministic SHA-256 manifest for this bounded lane directory."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SELF_OUTPUTS = {"artifacts.sha256", "artifact_summary.json", "__pycache__"}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


records = []
for path in sorted(ROOT.iterdir(), key=lambda item: item.name):
    if path.name in SELF_OUTPUTS or not path.is_file():
        continue
    records.append(
        {
            "name": path.name,
            "bytes": path.stat().st_size,
            "sha256": digest(path),
        }
    )

(ROOT / "artifacts.sha256").write_text(
    "".join(f"{record['sha256']}  {record['name']}\n" for record in records),
    encoding="utf-8",
)
(ROOT / "artifact_summary.json").write_text(
    json.dumps(
        {
            "directory": "box/k16terminal-sol56-20260903",
            "file_count": len(records),
            "files": records,
        },
        indent=2,
        sort_keys=True,
    )
    + "\n",
    encoding="utf-8",
)
print(f"MANIFEST_WRITTEN files={len(records)}")
