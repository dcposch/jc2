#!/usr/bin/env python3
"""Write the deterministic freeze manifest for this large harvested case."""

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent
EXCLUDE = {"manifest.sha256"}


def main() -> None:
    rows = []
    for path in sorted(p for p in HERE.rglob("*") if p.is_file()):
        relative = path.relative_to(HERE).as_posix()
        if relative in EXCLUDE or "__pycache__" in path.parts:
            continue
        rows.append(f"{sha256(path.read_bytes()).hexdigest()}  {relative}")
    (HERE / "manifest.sha256").write_text("\n".join(rows) + "\n")
    print(f"manifest_entries={len(rows)}")
    print("manifest_sha256=" + sha256((HERE / "manifest.sha256").read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
