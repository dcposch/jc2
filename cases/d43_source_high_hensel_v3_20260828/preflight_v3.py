#!/usr/bin/python3
"""Read-only post-review preflight for a prospective v3 authorization.

This command never writes an authorization, changes an EC2 tag, creates a
run directory, or launches work.  Given the sealed packet, an independent
PASS report, and the prospective absolute run path, it computes the exact
deterministic source-archive and normalized child-environment bindings that
the external coordinator authorization must contain.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import io
import json
import sys
import tarfile
from pathlib import Path


HERE = Path(__file__).resolve().parent
CASES = HERE.parent
ROOT = CASES.parent
sys.path.insert(0, str(HERE))

import aws_supervisor_v3 as S


MANIFEST_RELATIVE = \
    "cases/d43_source_high_hensel_v3_20260828/PAYLOAD.sha256"
PREREG_RELATIVE = \
    "cases/d43_source_high_hensel_v3_20260828/preregistration_v3.json"


def deterministic_source_archive(files):
    raw = io.BytesIO()
    inventory = {}
    with tarfile.open(fileobj=raw, mode="w") as archive:
        for name, path in sorted(files):
            data = path.read_bytes()
            info = tarfile.TarInfo(name)
            info.size = len(data)
            info.mode = 0o444
            info.mtime = info.uid = info.gid = 0
            info.uname = info.gname = ""
            archive.addfile(info, io.BytesIO(data))
            inventory[name] = {"sha256": hashlib.sha256(data).hexdigest(),
                               "bytes": len(data)}
    compressed = io.BytesIO()
    with gzip.GzipFile(filename="", mode="wb", fileobj=compressed,
                       mtime=0) as output:
        output.write(raw.getvalue())
    value = compressed.getvalue()
    return hashlib.sha256(value).hexdigest(), len(value), inventory


def run(source_root: Path, review_report: Path, run_dir: Path):
    for name, path in (("source root", source_root),
                       ("review report", review_report)):
        if not path.is_absolute() or path.is_symlink():
            raise ValueError("%s must be an absolute nonsymlink" % name)
    source_root = source_root.resolve(strict=True)
    review_report = review_report.resolve(strict=True)
    if not run_dir.is_absolute() or run_dir.is_symlink() or run_dir.exists():
        raise ValueError("run directory must be a fresh absolute path")
    manifest = S.safe_relative_path(source_root, MANIFEST_RELATIVE)
    prereg = S.safe_relative_path(source_root, PREREG_RELATIVE)
    entries = S.parse_hash_manifest(source_root, manifest)
    S.verify_preregistration(prereg, entries, S.sha256_path(manifest))
    archive_files = [(relative, source_root / relative)
                     for relative in entries]
    archive_files.extend([
        (MANIFEST_RELATIVE, manifest), (PREREG_RELATIVE, prereg),
        ("external/INDEPENDENT_REVIEW.md", review_report),
    ])
    archive_sha, archive_bytes, inventory = deterministic_source_archive(
        archive_files)
    environment = S.normalized_child_environment(run_dir)
    return {
        "schema": "d43-pristine-source-high-hensel-postreview-preflight-v3",
        "status": "BINDINGS_COMPUTED_NO_AUTHORIZATION_NO_LAUNCH",
        "source_root": str(source_root), "prospective_run_dir": str(run_dir),
        "payload_manifest_sha256": S.sha256_path(manifest),
        "preregistration_sha256": S.sha256_path(prereg),
        "review_report_sha256": S.sha256_path(review_report),
        "source_archive_sha256": archive_sha,
        "source_archive_bytes": archive_bytes,
        "source_inventory_sha256": S.sha256_json(inventory),
        "normalized_child_environment": environment,
        "runtime_environment_sha256": S.sha256_json(environment),
        "claims_forbidden_sha256": S.sha256_json(S.FORBIDDEN_CLAIMS),
        "runner_sha256": S.sha256_path(HERE / "runner_v3.py"),
        "supervisor_sha256": S.sha256_path(HERE / "aws_supervisor_v3.py"),
        "worker_sha256": S.sha256_path(HERE / "aws_worker_v3.sh"),
        "base_runner_sha256": S.sha256_path(CASES /
                                             "d43_source_high_hensel.py"),
        "d21_private_sha256": S.EXPECTED_D21_SHA256,
        "core23_sha256": S.EXPECTED_CORE23_SHA256,
        "next_step": (
            "combine these values with a complete pinned-runtime receipt, "
            "live EC2 identity, root-owned unit hash, distinct job/target, "
            "and (for N64) exact N16 terminal provenance; coordinator signs "
            "the immutable authorization by placing its SHA-256 in the live "
            "instance tag only after an independent packet review PASS"),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--review-report", type=Path, required=True)
    parser.add_argument("--run-dir", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(run(args.source_root, args.review_report, args.run_dir),
                     indent=1, sort_keys=True))


if __name__ == "__main__":
    main()
