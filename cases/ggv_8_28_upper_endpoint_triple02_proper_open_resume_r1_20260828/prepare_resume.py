#!/usr/bin/env python3
"""Validate and selectively extract the frozen TRIPLE02 R3 terminal packet."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import tarfile


ARCHIVE_SHA256 = "e5bdd2b25cde0dccd8f1e6b8f0e1fcc815d409426308afb49c45df86af53a1e1"
REQUIRED_MEMBERS = {
    "output/INPUT_MANIFEST.json":
        "0025f3eafe43b06d8d4cdd7b99870a52b7da331e8985baf7dd3de09a6e48257e",
    "output/node_001/NODE_INPUT.json":
        "b8bf5ec7f09f53211b00d5aafcee0d5b1b45c997c254437a3edb0f647376f68f",
    "output/node_001/NODE_001_STANDARD_BASIS.txt":
        "bd95508c3d0441d18d2538810e2c40ac85ccd5da57f09a560d2d9a93a483640d",
    "output/node_001/reduce.sing":
        "28385a7044bf6b3a2d79c42738860039b687f32f13d5a43c0e67c50b247af609",
    "output/node_001/NODE_001_REDUCE_PIVOTS.tsv":
        "2edaa006dae3f63e90973d40de5c7cdda00437570283429c69b353023645e7fc",
    "output/node_001/NODE_001_REDUCE_RESIDUAL.tsv":
        "f24a4a23aa99d2864c468cce73d7a3affbb7f7baa7344af29a86060dad1a0bfb",
    "output/node_001/NODE_001_SIZE_6_WITNESS.tsv":
        "fa0428864a2e15b65b89c0fee2c8f91a557571b0c2c7502f1c9230a6f88d8632",
    "output/node_001/NODE_001_SIZE_6_MINORS.tsv":
        "1c6e57a4551de1f97f31444b771c8b7255b1e270fa1f4fbcd5198795bef07b86",
    "output/node_001/rank_size_6.support.json":
        "bb8f7ee0faabbdb8e40be15bd4d6b3df319acbb5d6d6df7643954a65503d8c51",
    "output/node_001/saturation.sing":
        "196cb1205291c8cae0e047adf2a759cfa798fbda5a78ceefd9c18b7ec7a5f670",
    "output/node_001/saturation.result.json":
        "4bac13693064e6a1ae16963b4cc3fd9ff5044641e3352e491c2f99b1be4851f5",
    "output/node_001/saturation.stdout.txt":
        "4ee63095327d80572764eb3783d0e77c7a6cf385f47cf93c1cafcea843b29418",
    "output/node_001/saturation.stderr.txt":
        "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "output/node_001/NODE_001_OPEN_SAT_STANDARD_BASIS.txt":
        "e2d240e369e516ad8e3fb3ac221061abe465a241ce91ceeef96a4e7c0947493c",
    "source/jc2/cases/ggv_8_28_upper_endpoint_quotient_nf_endpoint_complements_r3_20260828/PREREGISTRATION.md":
        "781edcad4a5a524337a4717dca8344ef736af56177495ef1a51ee2d09c0c7fb0",
    "source/jc2/cases/ggv_8_28_upper_endpoint_quotient_nf_endpoint_complements_r3_20260828/SOURCE_MANIFEST.sha256":
        "ad043d20f6ea11040905658d40e5c0f07ec74efd1a3e8403316de61233b22d7d",
    "source/jc2/cases/ggv_8_28_upper_endpoint_quotient_nf_endpoint_complements_r3_20260828/recurse_component.py":
        "11761ad7734e88458195c344bddabd740a9c4f73d10ff071ab06baa2811e4d8f",
    "source/jc2/cases/ggv_8_28_upper_endpoint_quotient_nf_endpoint_complements_r3_20260828/transcript_gate.py":
        "0e0efd5ada59039a373a731038f2f88a3794b376b208879c2459bff97d0e7316",
    "custody/Singular.version":
        "0d074eb6c6978b4b3fc2c5df548939b9c4d341f38def77416eacf2dd8d86f193",
    "custody/Singular.path":
        "1b8813ec198b4528b0e523f28c1ad1afa55ef62749b988057227a609adcf4c2e",
    "custody/source_manifest_check.txt":
        "d2c54a96ee4e869cee0f0e0056d6053b8e73231f4403bf743838819039e7ecd9",
}
PREFIX_MARKERS = (
    "NODE_REDUCER_FIXTURES_PASS=1",
    "SATURATION_OBJECT_TYPE=list",
    "SATURATION_OBJECT_SIZE=1",
    "SATURATION_SLOT1_TYPE=ideal",
    "SATURATION_NODE_INCLUSION_FAILURES=0",
    "SATURATION_STABILITY_FAILURES=0",
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def verify_archive_sha(path: Path) -> str:
    actual = sha256(path)
    if actual != ARCHIVE_SHA256:
        raise RuntimeError(f"FROZEN_ARCHIVE_SHA_DRIFT:{actual}")
    return actual


def safe_relative(name: str) -> PurePosixPath:
    path = PurePosixPath(name)
    if path.is_absolute() or not path.parts or ".." in path.parts:
        raise SystemExit(f"UNSAFE_ARCHIVE_MEMBER:{name}")
    return path


def selected(name: str) -> bool:
    return name == "work/base" or name.startswith("work/base/") or name in REQUIRED_MEMBERS


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", required=True, type=Path)
    parser.add_argument("--destination", required=True, type=Path)
    args = parser.parse_args()
    archive_path = args.archive.resolve()
    destination = args.destination.resolve()
    if destination.exists():
        raise SystemExit("DESTINATION_ALREADY_EXISTS")
    try:
        actual_archive_sha = verify_archive_sha(archive_path)
    except RuntimeError as exc:
        raise SystemExit(str(exc)) from exc
    destination.mkdir(parents=True, mode=0o700)
    required_seen: dict[str, str] = {}
    extracted_files: dict[str, str] = {}
    selected_name_census: set[str] = set()
    with tarfile.open(archive_path, "r:gz") as archive:
        members = archive.getmembers()
        names = [member.name.rstrip("/") for member in members]
        for name in names:
            safe_relative(name)
        if len(names) != len(set(names)):
            raise SystemExit("ARCHIVE_GLOBAL_MEMBER_NAME_DUPLICATE")
        for required in REQUIRED_MEMBERS:
            if names.count(required) != 1:
                raise SystemExit(f"REQUIRED_MEMBER_CENSUS:{required}:{names.count(required)}")
        for member in members:
            name = member.name.rstrip("/")
            if not selected(name):
                continue
            relative = safe_relative(name)
            if name in selected_name_census:
                raise SystemExit(f"DUPLICATE_SELECTED_MEMBER:{name}")
            selected_name_census.add(name)
            target = destination.joinpath(*relative.parts)
            if member.isdir():
                target.mkdir(parents=True, exist_ok=True, mode=0o700)
                continue
            if not member.isfile():
                raise SystemExit(f"NONREGULAR_SELECTED_MEMBER:{name}:{member.type!r}")
            handle = archive.extractfile(member)
            if handle is None:
                raise SystemExit(f"ARCHIVE_MEMBER_READ_FAILURE:{name}")
            data = handle.read()
            digest = sha256_bytes(data)
            if name in REQUIRED_MEMBERS:
                if digest != REQUIRED_MEMBERS[name]:
                    raise SystemExit(f"REQUIRED_MEMBER_SHA_DRIFT:{name}:{digest}")
                required_seen[name] = digest
            target.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
            target.write_bytes(data)
            target.chmod(0o600)
            extracted_files[name] = digest
    if required_seen != REQUIRED_MEMBERS:
        raise SystemExit("REQUIRED_MEMBER_EXTRACTION_DISAGREEMENT")
    saturation_result = json.loads(
        (destination / "output/node_001/saturation.result.json").read_text())
    if (saturation_result.get("timed_out") is not True
            or saturation_result.get("returncode") != 1
            or saturation_result.get("stdout_sha256")
            != REQUIRED_MEMBERS["output/node_001/saturation.stdout.txt"]):
        raise SystemExit("FROZEN_TIMEOUT_RECORD_DISAGREEMENT")
    prefix_lines = (
        destination / "output/node_001/saturation.stdout.txt").read_text().splitlines()
    if any(prefix_lines.count(marker) != 1 for marker in PREFIX_MARKERS):
        raise SystemExit("ARCHIVED_EXACT_PREFIX_MARKER_CENSUS")
    if any(line.startswith("SATURATION_CERTIFICATE_COMPLETE=") for line in prefix_lines):
        raise SystemExit("ARCHIVED_PREFIX_FALSE_TERMINAL_MARKER")
    marker_positions = [prefix_lines.index(marker) for marker in PREFIX_MARKERS]
    if marker_positions != sorted(marker_positions) or prefix_lines[-1] != "halt 1":
        raise SystemExit("ARCHIVED_EXACT_PREFIX_ORDER_DRIFT")
    reduce_script = (destination / "output/node_001/reduce.sing").read_text()
    saturation_script = (destination / "output/node_001/saturation.sing").read_text()
    ring_declaration = "ring ambient=0,(q0,q2,c4,c6),dp;"
    if (reduce_script.count(ring_declaration) != 1
            or saturation_script.count(ring_declaration) != 1
            or reduce_script.count("c4") != 30):
        raise SystemExit("ARCHIVED_RING_ORDER_OR_C4_CENSUS_DRIFT")
    singular_version = (destination / "custody/Singular.version").read_text()
    if "version 4.3.2 (4330, 64 bit)" not in singular_version:
        raise SystemExit("ARCHIVED_SINGULAR_VERSION_DRIFT")
    payload = {
        "archive_sha256": actual_archive_sha,
        "extracted_file_count": len(extracted_files),
        "frozen_timeout_classification": "TIMEOUT_NO_VERDICT",
        "prefix_markers": list(PREFIX_MARKERS),
        "prefix_stdout_sha256": REQUIRED_MEMBERS[
            "output/node_001/saturation.stdout.txt"],
        "ring_declaration": ring_declaration,
        "archived_reduce_script_c4_token_count": 30,
        "saturation_trust_model": "PROVENANCE_ONLY_PENDING_SELF_CONTAINED_TWO_CONTAINMENT_REPLAY",
        "required_members": required_seen,
        "scope": "TRIPLE02_NODE1_ARCHIVED_EXACT_PREFIX_AND_FROZEN_BASE_ONLY",
    }
    manifest_path = destination / "PREPARED_INPUTS.json"
    manifest_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    manifest_path.chmod(0o600)
    print(f"FROZEN_TERMINAL_ARCHIVE_SHA256={actual_archive_sha}")
    print(f"SELECTED_EXTRACTED_FILE_COUNT={len(extracted_files)}")
    print("ARCHIVED_SATURATION_PREFIX_MARKERS_VERIFIED=1")
    print("ARCHIVED_TIMEOUT_REMAINS_NO_VERDICT=1")
    print("TRIPLE02_PROPER_OPEN_RESUME_PREPARATION_PASS=1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
