#!/usr/bin/env python3
"""SHA-256 manifest of every artifact this lane produced (row TSVs excluded by size)."""
from __future__ import annotations
import hashlib, json
from pathlib import Path

ROOT = Path("/home/ubuntu/jc2")
HERE = ROOT / "box" / "g9966n1b3-20260903"
BIG = 8 * 1 << 20


def sha(p):
    d = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            d.update(b)
    return d.hexdigest()


lines, big = [], []
for p in sorted(HERE.rglob("*")):
    if not p.is_file() or "__pycache__" in p.parts or p.suffix == ".pyc":
        continue
    if p.name in ("artifacts.sha256", "artifacts-large.json") or p.name.endswith(".tmp"):
        continue
    rel = p.relative_to(ROOT)
    if p.stat().st_size > BIG:
        big.append({"path": str(rel), "bytes": p.stat().st_size, "sha256": sha(p)})
    else:
        lines.append(f"{sha(p)}  {rel}")
man = HERE / "artifacts.sha256"
man.write_text("\n".join(lines) + "\n")
(HERE / "artifacts-large.json").write_text(json.dumps(
    {"note": f"artifacts over {BIG} bytes, hashed separately", "files": big},
    indent=2, sort_keys=True) + "\n")
print(json.dumps({"small_files": len(lines), "large_files": len(big),
                  "manifest": str(man.relative_to(ROOT)),
                  "manifest_sha256": sha(man)}, indent=1))
