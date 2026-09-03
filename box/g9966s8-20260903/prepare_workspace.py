#!/usr/bin/env python3
"""Restore the pinned engine's read-only legacy input view and seed a new run.

All source paths, basenames, and digests are taken mechanically from the
legacy receipt.  Existing destinations are accepted only when their contents
already have the required digest; nothing is overwritten.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
ENGINE = ROOT / "box/g9966band-20260903/band_engine.py"
RECEIPT = ROOT / "xmodel/g9966-global-band-sol56-20260903.run.v2"
SOURCE_RUN = ROOT / "box/g9966band-20260903/runs/delta52"
RUN = ROOT / "box/g9966s8-20260903/runs/delta52"
PINNED_ENGINE_SHA256 = (
    "3bd2937d75d59d59edeca1b89eba286fd2711f2d608109e7fd8971b64e059ac9"
)


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def fields(path: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            out[key] = value
    return out


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def safe_link(source: Path, destination: Path, expected: str) -> str:
    require(source.is_file(), f"missing source: {source}")
    require(digest(source) == expected, f"source digest mismatch: {source}")
    if destination.exists():
        require(destination.is_file(), f"destination is not a file: {destination}")
        require(digest(destination) == expected, f"existing destination mismatch: {destination}")
        return "existing"
    if destination.is_symlink():
        raise RuntimeError(f"dangling destination symlink: {destination}")
    destination.symlink_to(source)
    require(digest(destination) == expected, f"linked destination mismatch: {destination}")
    return "linked"


def main() -> None:
    require(digest(ENGINE) == PINNED_ENGINE_SHA256, "pinned engine digest mismatch")
    receipt = fields(RECEIPT)
    count = int(receipt["charged_inputs"])
    require(count == 20, f"unexpected legacy charged-input count: {count}")

    engine_text = ENGINE.read_text(encoding="utf-8")
    match = re.search(r'^FROZEN = Path\("([^\"]+)"\)$', engine_text, re.MULTILINE)
    require(match is not None, "cannot recover FROZEN path from pinned engine")
    frozen = Path(match.group(1))
    require(str(frozen).startswith("/tmp/jc2-lane."), f"unsafe frozen target: {frozen}")
    frozen.mkdir(parents=True, exist_ok=True)

    linked = []
    seen_names: set[str] = set()
    for index in range(1, count + 1):
        source_rel = receipt[f"charged_input_{index}"]
        basename = receipt[f"charged_input_{index}_basename"]
        expected = receipt[f"charged_input_{index}_sha256"]
        require(Path(source_rel).name == basename, f"basename mismatch at input {index}")
        require(basename not in seen_names, f"duplicate frozen basename: {basename}")
        seen_names.add(basename)
        source = ROOT / source_rel
        destination = frozen / basename
        action = safe_link(source, destination, expected)
        linked.append({"index": index, "basename": basename, "sha256": expected,
                       "source": str(source), "destination": str(destination),
                       "action": action})

    RUN.mkdir(parents=True, exist_ok=True)
    seeded = []
    for stage in range(8):
        for suffix in ("json", "time", "sing", "err"):
            name = f"stage{stage}.{suffix}"
            source = SOURCE_RUN / name
            require(source.is_file(), f"missing accepted prefix artifact: {source}")
            expected = digest(source)
            action = safe_link(source, RUN / name, expected)
            seeded.append({"file": name, "sha256": expected, "action": action})

    print(json.dumps({
        "status": "READY",
        "engine": str(ENGINE),
        "engine_sha256": PINNED_ENGINE_SHA256,
        "legacy_receipt": str(RECEIPT),
        "frozen_directory": str(frozen),
        "charged_inputs": linked,
        "run_directory": str(RUN),
        "seeded_prefix_artifacts": seeded,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
