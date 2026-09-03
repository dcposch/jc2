#!/usr/bin/env python3
"""Hash every completed regular artifact in this lane directory.

The manifest excludes itself.  Run only after all producer processes have
finished so each digest describes a stable file.
"""

from __future__ import annotations

import hashlib
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "final_manifest.sha256"


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


files = sorted(
    path for path in HERE.iterdir()
    if path.is_file() and path != OUTPUT and not path.name.endswith(".partial")
)
body = "".join(f"{digest(path)}  {path.name}\n" for path in files)
OUTPUT.write_text(body, encoding="ascii", newline="\n")
print(f"FINAL_MANIFEST files={len(files)} bytes={len(body)} path={OUTPUT.name}")
