#!/usr/bin/env python3
"""Reconstruct the pinned Sol lane input directory for band_engine.py.

The charged engine hard-codes the Sol lane path.  This script rebuilds that
directory using symlinks to repository files whose hashes are checked against
the Sol receipt before the links are created.
"""

from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RECEIPT = ROOT / "xmodel/g9966-global-band-sol56-20260903.run.v2"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    fields: dict[str, str] = {}
    for line in RECEIPT.read_text(encoding="utf-8").splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            fields[key] = value

    target = Path(fields["lane_inputs_dir"])
    target.mkdir(parents=True, exist_ok=True)

    count = int(fields["charged_inputs"])
    for index in range(1, count + 1):
        source = ROOT / fields[f"charged_input_{index}"]
        basename = fields[f"charged_input_{index}_basename"]
        expected = fields[f"charged_input_{index}_sha256"]
        actual = sha256(source)
        if actual != expected:
            raise SystemExit(
                f"hash mismatch for charged_input_{index}: {source} "
                f"{actual} != {expected}"
            )
        link = target / basename
        if link.exists() or link.is_symlink():
            link.unlink()
        link.symlink_to(source)

    print(f"reconstructed {count} Sol charged inputs at {target}")


if __name__ == "__main__":
    main()
