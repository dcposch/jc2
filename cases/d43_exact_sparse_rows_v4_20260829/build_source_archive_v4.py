#!/usr/bin/env python3
"""Reproducible builder for the sealed v3 source archive.

Stages the exact operational member set into a private ``jc2/`` layout,
generates the archive member-census manifest, builds the deterministic
tar.gz twice (proving byte determinism), replays a fresh private
extraction against the embedded manifest, and writes the outer SHA-256
sidecar.  Rerunning this builder against unchanged sources must reproduce
the identical outer digest.

This builder and the external launcher are intentionally NOT members of the
archive, so the archive digest can be pinned in the launcher without
self-reference.
"""

from __future__ import annotations

import importlib.util
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

if sys.flags.optimize:
    raise RuntimeError("OPTIMIZED_PYTHON_REFUSED_FAIL_CLOSED")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent

spec = importlib.util.spec_from_file_location(
    "d43_job_contract_v4", HERE / "job_contract_v4.py")
CONTRACT = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = CONTRACT
spec.loader.exec_module(CONTRACT)

CASE_REL = "cases/d43_exact_sparse_rows_v4_20260829"
MEMBERS = [
    "cases/d43_common_integral_emitter.py",
    "cases/d43_exact_sparse_rows_20260828/selected_rows.py",
    CASE_REL + "/OPERATIONAL_SOURCE_V4.sha256",
    CASE_REL + "/PIPELINE_MANIFEST_V4.json",
    CASE_REL + "/aws_preflight_v4.py",
    CASE_REL + "/job_contract_v4.py",
    CASE_REL + "/run_conditional_pipeline_aws_v4.sh",
    CASE_REL + "/selected_rows_v4.py",
    "cases/d43_full_certificate_p105337.json",
    "cases/d43_full_certificate_p105673.json",
    "cases/directionb_strike.py",
    "cases/r1_experiment.py",
    "directionb_tails_D21.pkl",
    "xmodel/d43-e5-e6-elimination-bridge-gpt56-20260828.md",
    "xmodel/d43-exact-sparse-rows-hostile-review-gpt56-20260828.md",
    "xmodel/d43-exact-sparse-rows-v2-hostile-review-gpt56-20260828.md",
    "xmodel/d43-exact-sparse-rows-v3-hostile-review-opus5-20260829.md",
    "xmodel/d43-exact-sparse-rows-v3-repair-fable5-20260828.md",
    "xmodel/d43-exact-sparse-source-opus5-hostile-audit-20260828.md",
    "xmodel/d43-raw-source-template-scope-fable5-audit-20260828.md",
]
CENSUS_REL = "jc2/" + CASE_REL + "/SOURCE_ARCHIVE_MANIFEST_V4.sha256"
ARCHIVE = HERE / "d43_v4_source.tar.gz"


def main() -> int:
    staging = Path(tempfile.mkdtemp(prefix="d43v3stage.")).resolve()
    try:
        for relative in MEMBERS:
            source = ROOT / relative
            target = staging / "jc2" / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
        census = staging / CENSUS_REL
        count = CONTRACT.build_complete_manifest(staging, census, ["jc2"])
        print("SOURCE_ARCHIVE_MEMBER_CENSUS_ENTRIES=%d" % count)
        shutil.copyfile(census, HERE / "SOURCE_ARCHIVE_MANIFEST_V4.sha256")

        first = staging / "build1.tar.gz"
        second = staging / "build2.tar.gz"
        digest1 = CONTRACT.build_deterministic_archive(
            staging, census, CENSUS_REL, first)
        digest2 = CONTRACT.build_deterministic_archive(
            staging, census, CENSUS_REL, second)
        if digest1 != digest2:
            raise RuntimeError("SOURCE_ARCHIVE_NOT_DETERMINISTIC")
        print("SOURCE_ARCHIVE_DETERMINISTIC_REBUILD=PASS")

        replay = staging / "replay"
        entries = CONTRACT.extract_and_verify_archive(
            first, replay, CENSUS_REL, ["jc2"])
        print("SOURCE_ARCHIVE_FRESH_EXTRACTION_REPLAY_ENTRIES=%d" % entries)
        for relative in MEMBERS:
            live = (ROOT / relative).read_bytes()
            extracted = (replay / "jc2" / relative).read_bytes()
            if live != extracted:
                raise RuntimeError(
                    "EXTRACTED_MEMBER_NOT_BYTE_IDENTICAL:" + relative)
        print("SOURCE_ARCHIVE_MEMBERS_BYTE_IDENTICAL_TO_LIVE=PASS")

        if ARCHIVE.exists():
            os.chmod(ARCHIVE, 0o644)
        shutil.copyfile(first, ARCHIVE)
        os.chmod(ARCHIVE, 0o444)
        sidecar = ARCHIVE.with_name(ARCHIVE.name + ".sha256")
        if sidecar.exists():
            os.chmod(sidecar, 0o644)
        sidecar.write_text("%s  %s\n" % (digest1, ARCHIVE.name))
        os.chmod(sidecar, 0o444)
        verify = subprocess.run(
            ["shasum", "-a", "256", "-c", sidecar.name], cwd=HERE,
            capture_output=True, text=True)
        if verify.returncode != 0:
            verify = subprocess.run(
                ["sha256sum", "-c", sidecar.name], cwd=HERE,
                capture_output=True, text=True)
        if verify.returncode != 0:
            raise RuntimeError("OUTER_SIDECAR_REPLAY_FAILED")
        print("SOURCE_ARCHIVE_OUTER_SHA256=%s" % digest1)
        return 0
    finally:
        shutil.rmtree(staging, ignore_errors=True)


if __name__ == "__main__":
    raise SystemExit(main())
