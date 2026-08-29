#!/usr/bin/env python3
"""Verify and safely extract the clean root-chart terminal archive."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import tarfile


EXPECTED_ARCHIVE_SHA = "1fe30b1ccf142791149b5152db519761681368b3e01c94cd82844802dee39787"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def safe_extract(archive: tarfile.TarFile, destination: Path) -> None:
    base = destination.resolve()
    for member in archive.getmembers():
        target = (base / member.name).resolve()
        if target != base and base not in target.parents:
            raise SystemExit(f"UNSAFE_ARCHIVE_MEMBER:{member.name}")
    archive.extractall(destination)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    archive = args.archive.resolve()
    output = args.output.resolve()
    actual = sha256(archive)
    if actual != EXPECTED_ARCHIVE_SHA:
        raise SystemExit(f"ROOT_CHART_ARCHIVE_SHA_DRIFT:{actual}")
    output.mkdir(parents=True, exist_ok=False)
    with tarfile.open(archive, "r:gz") as handle:
        safe_extract(handle, output)
    required = [
        output / "source/jc2/cases/ggv_8_28_upper_endpoint_quotient_nf_endpoint_charts_r1_20260828/build_endpoint_chart.py",
        output / "work/prepared/upstream_source/jc2/cases/ggv_8_28_upper_endpoint_lambda0_quotient_nf_rank_r5_20260828/build_nf_rank.py",
        output / "output/VERDICT.txt",
    ]
    for path in required:
        if not path.is_file():
            raise SystemExit(f"ROOT_CHART_MEMBER_MISSING:{path}")
    if (output / "output/VERDICT.txt").read_text().strip() != \
            "ROOT_CHARTS_COMPLETE_COMPLEMENTS_COMPONENTWISE":
        raise SystemExit("ROOT_CHART_VERDICT_DRIFT")
    manifest = {
        "archive": str(archive),
        "archive_sha256": actual,
        "root": str(output),
        "required": {str(path): sha256(path) for path in required},
    }
    (output / "PREPARED_BASE.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    print(json.dumps(manifest, indent=2, sort_keys=True))
    print("ENDPOINT_COMPLEMENT_BASE_PREPARATION_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
