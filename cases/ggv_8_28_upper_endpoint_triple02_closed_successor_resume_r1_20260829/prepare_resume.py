#!/usr/bin/env python3
"""Validate and selectively extract the two frozen TRIPLE02 node-1 archives.

Closed-successor scope: this preparer binds
  (a) the R3 terminal archive (node-1 generators, reduce/rank artifacts,
      rank-six witness, and the frozen timeout record), and
  (b) the reviewed proper-open R5 terminal archive (routing provenance only:
      the node-1 open D(Delta_node1) is settled EXACT_ENDPOINT_DEAD).
The node-1 open-saturation products (saturation.sing standard basis output,
NODE_001_OPEN_SAT_STANDARD_BASIS.txt) are deliberately NEVER extracted: the
closed successor must not depend on them.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import tarfile


R3_ARCHIVE_SHA256 = "e5bdd2b25cde0dccd8f1e6b8f0e1fcc815d409426308afb49c45df86af53a1e1"
PROPER_OPEN_ARCHIVE_SHA256 = (
    "4b8ffc1c16828b22b2e76a3aa92a25e8c1f472190a708f30a7b71ba952cbef7e")
SETTLED_OPEN_VERDICT = "EXACT_ENDPOINT_DEAD_ON_NODE1_PROPER_OPEN_ONLY"

R3_REQUIRED_MEMBERS = {
    "output/INPUT_MANIFEST.json":
        "0025f3eafe43b06d8d4cdd7b99870a52b7da331e8985baf7dd3de09a6e48257e",
    "output/VERDICT.txt":
        "1434d904a352bc47c8890d8bad366f5a2df797ef260ca809b512e2aab309cfd8",
    "output/ADAPTER_FAILURE.txt":
        "137d6cd136ce1e5f1d282c9b90a6e15eee329e25da59d9b418b6ded92fb9f02e",
    "output/node_001/NODE_INPUT.json":
        "b8bf5ec7f09f53211b00d5aafcee0d5b1b45c997c254437a3edb0f647376f68f",
    "output/node_001/NODE_001_STANDARD_BASIS.txt":
        "bd95508c3d0441d18d2538810e2c40ac85ccd5da57f09a560d2d9a93a483640d",
    "output/node_001/reduce.sing":
        "28385a7044bf6b3a2d79c42738860039b687f32f13d5a43c0e67c50b247af609",
    "output/node_001/reduce.result.json":
        "6daced5588b1cc9126e1789958511807b76e00ddbf8d246c4c283a82c21c9688",
    "output/node_001/reduce.stdout.txt":
        "85630c0b5ef15ca22caa459d2c02db9890286a75d490c965ca9fcc666898abb5",
    "output/node_001/NODE_001_REDUCE_PIVOTS.tsv":
        "2edaa006dae3f63e90973d40de5c7cdda00437570283429c69b353023645e7fc",
    "output/node_001/NODE_001_REDUCE_RESIDUAL.tsv":
        "f24a4a23aa99d2864c468cce73d7a3affbb7f7baa7344af29a86060dad1a0bfb",
    "output/node_001/rank_size_6.sing":
        "9f9e76085fb6c53b73176daff005d1843c2dd0e362432c4bbb9bfb6eefd8a071",
    "output/node_001/rank_size_6.result.json":
        "ac4a2f1b5b8345bb850862d14a4c5c91e1fbbebd194a3b723ddbfbdf7c2318c0",
    "output/node_001/rank_size_6.stdout.txt":
        "5d181ec46c0d9240660eda37b9a9e26bf99e9d140ee700821bbb96efcc8a12d1",
    "output/node_001/rank_size_6.support.json":
        "bb8f7ee0faabbdb8e40be15bd4d6b3df319acbb5d6d6df7643954a65503d8c51",
    "output/node_001/NODE_001_SIZE_6_MINORS.tsv":
        "1c6e57a4551de1f97f31444b771c8b7255b1e270fa1f4fbcd5198795bef07b86",
    "output/node_001/NODE_001_SIZE_6_WITNESS.tsv":
        "fa0428864a2e15b65b89c0fee2c8f91a557571b0c2c7502f1c9230a6f88d8632",
    "output/node_001/saturation.result.json":
        "4bac13693064e6a1ae16963b4cc3fd9ff5044641e3352e491c2f99b1be4851f5",
    "output/node_001/saturation.stdout.txt":
        "4ee63095327d80572764eb3783d0e77c7a6cf385f47cf93c1cafcea843b29418",
    "custody/Singular.version":
        "0d074eb6c6978b4b3fc2c5df548939b9c4d341f38def77416eacf2dd8d86f193",
}
# Present in the R3 archive census but excluded from extraction: products of
# the settled node-1 open-saturation route.
R3_EXCLUDED_OPEN_ROUTE_MEMBERS = (
    "output/node_001/NODE_001_OPEN_SAT_STANDARD_BASIS.txt",
    "output/node_001/saturation.sing",
)
PROPER_OPEN_REQUIRED_MEMBERS = {
    "output/VERDICT.txt":
        "75645210fa8d7a9cebada5680b6608dfeb1ebada23e8e1cebaba49bf9fc63a05",
    "output/SUMMARY.json":
        "a976536e24f81bc22fb360827d4123edaa87df0a7eadba7bb4146143512ec188",
    "custody/CANDIDATE_MATHEMATICAL_VERDICT.txt":
        "75645210fa8d7a9cebada5680b6608dfeb1ebada23e8e1cebaba49bf9fc63a05",
}
SATURATION_PREFIX_MARKERS = (
    "NODE_REDUCER_FIXTURES_PASS=1",
    "SATURATION_OBJECT_TYPE=list",
    "SATURATION_OBJECT_SIZE=1",
    "SATURATION_SLOT1_TYPE=ideal",
    "SATURATION_NODE_INCLUSION_FAILURES=0",
    "SATURATION_STABILITY_FAILURES=0",
)
REDUCE_STDOUT_MARKERS = (
    "NODE_INDEX=1",
    "NODE_GENERATOR_COUNT=2",
    "NODE_EMPTY=0",
    "NODE_REDUCER_FIXTURES_PASS=1",
    "NF_RATIONAL_UNIT_PIVOT_COUNT=95",
    "NF_PIVOT_INVARIANT_FAILURES=0",
    "NODE_RESIDUAL_REDUCTION_COMPLETE=1",
    "NODE_REDUCE_COMPLETE=1",
)
RANK6_STDOUT_MARKERS = (
    "RANK_SIZE=6",
    "RANK_SIZE_FORMAL_SLOTS=97020",
    "RANK_SIZE_STRUCTURAL_ZERO_SLOTS=95920",
    "RANK_SIZE_MATCHABLE_TESTED=1100",
    "RANK_SIZE_NF_NONZERO_COUNT=1025",
    "RANK_SIZE_WITNESS_FOUND=1",
    "SUPPORT_REPLAY_FAILURES=0",
    "DETERMINANT_NF_REDUCTIONS=1100",
    "RANK_SIZE_CENSUS_COMPLETE=1",
)
RING_DECLARATION = "ring ambient=0,(q0,q2,c4,c6),dp;"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def verify_archive_sha(path: Path, expected: str) -> str:
    actual = sha256(path)
    if actual != expected:
        raise RuntimeError(f"FROZEN_ARCHIVE_SHA_DRIFT:{path.name}:{actual}")
    return actual


def safe_relative(name: str) -> PurePosixPath:
    path = PurePosixPath(name)
    if path.is_absolute() or not path.parts or ".." in path.parts:
        raise SystemExit(f"UNSAFE_ARCHIVE_MEMBER:{name}")
    return path


def r3_selected(name: str) -> bool:
    if name in R3_EXCLUDED_OPEN_ROUTE_MEMBERS:
        return False
    return (name == "work/base" or name.startswith("work/base/")
            or name in R3_REQUIRED_MEMBERS)


def extract_selected(archive_path: Path, destination: Path,
                     required: dict[str, str], selected,
                     census_out: dict[str, object]) -> dict[str, str]:
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
        nonregular = [member.name for member in members
                      if not (member.isfile() or member.isdir())]
        if nonregular:
            raise SystemExit(
                "ARCHIVE_LINK_DEVICE_OR_SPECIAL_MEMBER:" + nonregular[0])
        for required_name in required:
            if names.count(required_name) != 1:
                raise SystemExit(
                    f"REQUIRED_MEMBER_CENSUS:{required_name}:"
                    f"{names.count(required_name)}")
        census_out["member_count"] = len(members)
        census_out["regular_file_count"] = sum(
            1 for member in members if member.isfile())
        census_out["directory_count"] = sum(
            1 for member in members if member.isdir())
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
                raise SystemExit(
                    f"NONREGULAR_SELECTED_MEMBER:{name}:{member.type!r}")
            handle = archive.extractfile(member)
            if handle is None:
                raise SystemExit(f"ARCHIVE_MEMBER_READ_FAILURE:{name}")
            data = handle.read()
            digest = sha256_bytes(data)
            if name in required:
                if digest != required[name]:
                    raise SystemExit(
                        f"REQUIRED_MEMBER_SHA_DRIFT:{name}:{digest}")
                required_seen[name] = digest
            target.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
            target.write_bytes(data)
            target.chmod(0o600)
            extracted_files[name] = digest
    if required_seen != required:
        raise SystemExit("REQUIRED_MEMBER_EXTRACTION_DISAGREEMENT")
    return extracted_files


def validate_r3_payload(destination: Path) -> dict[str, object]:
    if (destination / "output/VERDICT.txt").read_text().strip() != (
            "ADAPTER_FAILURE_NO_VERDICT"):
        raise SystemExit("R3_FRONTIER_VERDICT_DRIFT")
    if (destination / "output/ADAPTER_FAILURE.txt").read_text().strip() != (
            "RuntimeError:SATURATION_RETURN_CODE:1"):
        raise SystemExit("R3_FRONTIER_FAILURE_CAUSE_DRIFT")
    saturation_result = json.loads(
        (destination / "output/node_001/saturation.result.json").read_text())
    if (saturation_result.get("timed_out") is not True
            or saturation_result.get("returncode") != 1
            or saturation_result.get("stdout_sha256")
            != R3_REQUIRED_MEMBERS["output/node_001/saturation.stdout.txt"]):
        raise SystemExit("FROZEN_TIMEOUT_RECORD_DISAGREEMENT")
    prefix_lines = (destination / "output/node_001/saturation.stdout.txt"
                    ).read_text().splitlines()
    if any(prefix_lines.count(marker) != 1
           for marker in SATURATION_PREFIX_MARKERS):
        raise SystemExit("ARCHIVED_SATURATION_PREFIX_MARKER_CENSUS")
    if any(line.startswith("SATURATION_CERTIFICATE_COMPLETE=")
           for line in prefix_lines):
        raise SystemExit("ARCHIVED_PREFIX_FALSE_TERMINAL_MARKER")
    marker_positions = [prefix_lines.index(marker)
                        for marker in SATURATION_PREFIX_MARKERS]
    if marker_positions != sorted(marker_positions) or prefix_lines[-1] != "halt 1":
        raise SystemExit("ARCHIVED_SATURATION_PREFIX_ORDER_DRIFT")
    for stdout_name, markers in (
            ("output/node_001/reduce.stdout.txt", REDUCE_STDOUT_MARKERS),
            ("output/node_001/rank_size_6.stdout.txt", RANK6_STDOUT_MARKERS)):
        lines = (destination / stdout_name).read_text().splitlines()
        if any(lines.count(marker) != 1 for marker in markers):
            raise SystemExit(f"ARCHIVED_STAGE_MARKER_CENSUS:{stdout_name}")
        if any(line.startswith("FATAL_") for line in lines):
            raise SystemExit(f"ARCHIVED_STAGE_FATAL_MARKER:{stdout_name}")
    for stage in ("reduce", "rank_size_6"):
        result = json.loads(
            (destination / f"output/node_001/{stage}.result.json").read_text())
        if (result.get("timed_out") is not False
                or result.get("returncode") != 0
                or result.get("script_sha256") != R3_REQUIRED_MEMBERS[
                    f"output/node_001/{stage}.sing"]
                or result.get("stdout_sha256") != R3_REQUIRED_MEMBERS[
                    f"output/node_001/{stage}.stdout.txt"]):
            raise SystemExit(f"ARCHIVED_STAGE_RESULT_CUSTODY:{stage}")
    node_input = json.loads(
        (destination / "output/node_001/NODE_INPUT.json").read_text())
    generators = node_input.get("generators")
    if (node_input.get("node") != 1
            or node_input.get("inherited_rank_upper_bound") != 6
            or not isinstance(generators, list) or len(generators) != 2):
        raise SystemExit("FROZEN_NODE_INPUT_SHAPE_DRIFT")
    literal_hashes = [sha256_bytes(value.encode()) for value in generators]
    if (literal_hashes != node_input.get("generator_sha256")
            or literal_hashes != [
                "2b9d29b706ce5d7e58e2dc5a28799782f5610c5ccb7b71987ebd694fd8b83206",
                "fecd1d43f3f55e1c65bec858303b7688c0db83dbe9c3a60f51f70130a4149336"]):
        raise SystemExit("FROZEN_NODE_GENERATOR_HASH_DRIFT")
    witness_lines = (destination
                     / "output/node_001/NODE_001_SIZE_6_WITNESS.tsv"
                     ).read_text().splitlines()
    if (len(witness_lines) != 2
            or witness_lines[0] != "rank|rows|cols|normal_form"):
        raise SystemExit("FROZEN_WITNESS_FORMAT_DRIFT")
    rank_text, rows_text, cols_text, delta = witness_lines[1].split("|", 3)
    delta = "".join(delta.split())
    if (rank_text != "6" or rows_text != "1,2,4,7,9,11"
            or cols_text != "1,2,3,5,6,7" or not delta
            or any(token in delta for token in (";", "|", '"', "'"))):
        raise SystemExit("FROZEN_WITNESS_INDEX_OR_DELTA_DRIFT")
    delta_sha = sha256_bytes(delta.encode())
    if delta_sha != (
            "84b4c2c4c0bfe5aa7414c35813cc1cf63d7d5416358a394b8e8bdc35820f1d02"):
        raise SystemExit("FROZEN_WITNESS_DELTA_HASH_DRIFT")
    if delta in generators:
        raise SystemExit("WITNESS_DELTA_COLLIDES_WITH_NODE_GENERATOR")
    reduce_script = (destination / "output/node_001/reduce.sing").read_text()
    if (reduce_script.count(RING_DECLARATION) != 1
            or reduce_script.count("c4") != 30):
        raise SystemExit("ARCHIVED_RING_ORDER_OR_C4_CENSUS_DRIFT")
    singular_version = (destination / "custody/Singular.version").read_text()
    if "version 4.3.2 (4330, 64 bit)" not in singular_version:
        raise SystemExit("ARCHIVED_SINGULAR_VERSION_DRIFT")
    root_classification = (destination
                           / "work/base/output/triple02/CLASSIFICATION.txt")
    if root_classification.read_text().strip() != "ENDPOINT_DEAD_ONLY_ON_D_DELTA":
        raise SystemExit("ROOT_CHART_CLASSIFICATION_DRIFT")
    root_delta_path = destination / "work/base/output/triple02/TRIPLE02_CHART_DELTA.txt"
    if sha256(root_delta_path) != (
            "adaad79c410c7bce4eb4bff5d08932204ed51681a6b61a321072cab54d782158"):
        raise SystemExit("ROOT_CHART_DELTA_FILE_HASH_DRIFT")
    root_delta = "".join(root_delta_path.read_text().split())
    if sha256_bytes(root_delta.encode()) != literal_hashes[1]:
        raise SystemExit("ROOT_CHART_DELTA_GENERATOR_DISAGREEMENT")
    return {
        "node1_generator_sha256": literal_hashes,
        "node1_delta_sha256": delta_sha,
        "node1_delta_length": len(delta),
    }


def validate_proper_open_payload(destination: Path) -> dict[str, object]:
    verdict = (destination / "output/VERDICT.txt").read_text().strip()
    candidate = (destination / "custody/CANDIDATE_MATHEMATICAL_VERDICT.txt"
                 ).read_text().strip()
    if verdict != SETTLED_OPEN_VERDICT or candidate != SETTLED_OPEN_VERDICT:
        raise SystemExit("SETTLED_OPEN_VERDICT_DRIFT")
    summary = json.loads((destination / "output/SUMMARY.json").read_text())
    if (summary.get("classification") != SETTLED_OPEN_VERDICT
            or summary.get("scope") != "TRIPLE02_NODE1_D_DELTA_ONLY"
            or summary.get("node") != 1
            or summary.get("proper_open_only") is not True
            or summary.get("endpoint_coefficient_nf_nonzero_count") != 0
            or summary.get("whole_component_or_closed_successor_inference")
            is not False):
        raise SystemExit("SETTLED_OPEN_SUMMARY_SCOPE_DRIFT")
    return {
        "settled_open_verdict": verdict,
        "settled_open_scope": summary["scope"],
        "settled_open_endpoint_nonzero_count": 0,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--r3-archive", required=True, type=Path)
    parser.add_argument("--proper-open-archive", required=True, type=Path)
    parser.add_argument("--destination", required=True, type=Path)
    args = parser.parse_args()
    destination = args.destination.resolve()
    if destination.exists():
        raise SystemExit("DESTINATION_ALREADY_EXISTS")
    try:
        r3_sha = verify_archive_sha(args.r3_archive.resolve(), R3_ARCHIVE_SHA256)
        proper_open_sha = verify_archive_sha(
            args.proper_open_archive.resolve(), PROPER_OPEN_ARCHIVE_SHA256)
    except RuntimeError as exc:
        raise SystemExit(str(exc)) from exc
    destination.mkdir(parents=True, mode=0o700)
    r3_destination = destination / "r3"
    proper_open_destination = destination / "settled_open_provenance"
    r3_destination.mkdir(mode=0o700)
    proper_open_destination.mkdir(mode=0o700)
    r3_census: dict[str, object] = {}
    proper_open_census: dict[str, object] = {}
    r3_extracted = extract_selected(
        args.r3_archive.resolve(), r3_destination, R3_REQUIRED_MEMBERS,
        r3_selected, r3_census)
    for excluded in R3_EXCLUDED_OPEN_ROUTE_MEMBERS:
        if excluded in r3_extracted:
            raise SystemExit(f"OPEN_ROUTE_MEMBER_EXTRACTED:{excluded}")
        if (r3_destination / excluded).exists():
            raise SystemExit(f"OPEN_ROUTE_MEMBER_ON_DISK:{excluded}")
    proper_open_extracted = extract_selected(
        args.proper_open_archive.resolve(), proper_open_destination,
        PROPER_OPEN_REQUIRED_MEMBERS,
        lambda name: name in PROPER_OPEN_REQUIRED_MEMBERS,
        proper_open_census)
    if set(proper_open_extracted) != set(PROPER_OPEN_REQUIRED_MEMBERS):
        raise SystemExit("SETTLED_OPEN_EXTRACTION_CENSUS")
    r3_payload = validate_r3_payload(r3_destination)
    proper_open_payload = validate_proper_open_payload(proper_open_destination)
    payload = {
        "closed_successor_route": "NODE1_CLOSED_SUCCESSOR_ONLY",
        "excluded_open_route_members": list(R3_EXCLUDED_OPEN_ROUTE_MEMBERS),
        "frozen_timeout_classification": "TIMEOUT_NO_VERDICT",
        "proper_open_archive_census": proper_open_census,
        "proper_open_archive_sha256": proper_open_sha,
        "proper_open_extracted_file_count": len(proper_open_extracted),
        "proper_open_trust_model": "ROUTING_PROVENANCE_ONLY_NEVER_AN_INPUT",
        "r3_archive_census": r3_census,
        "r3_archive_sha256": r3_sha,
        "r3_extracted_file_count": len(r3_extracted),
        "r3_required_members": {name: R3_REQUIRED_MEMBERS[name]
                                for name in sorted(R3_REQUIRED_MEMBERS)},
        "ring_declaration": RING_DECLARATION,
        "saturation_prefix_markers": list(SATURATION_PREFIX_MARKERS),
        "scope": "TRIPLE02_NODE1_CLOSED_SUCCESSOR_SOURCES_ONLY",
        **r3_payload,
        **proper_open_payload,
    }
    manifest_path = destination / "PREPARED_INPUTS.json"
    manifest_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    manifest_path.chmod(0o600)
    print(f"FROZEN_R3_TERMINAL_ARCHIVE_SHA256={r3_sha}")
    print(f"FROZEN_SETTLED_OPEN_ARCHIVE_SHA256={proper_open_sha}")
    print(f"R3_SELECTED_EXTRACTED_FILE_COUNT={len(r3_extracted)}")
    print(f"SETTLED_OPEN_EXTRACTED_FILE_COUNT={len(proper_open_extracted)}")
    print("OPEN_ROUTE_MEMBERS_EXCLUDED_FROM_EXTRACTION=1")
    print("ARCHIVED_TIMEOUT_REMAINS_NO_VERDICT=1")
    print(f"SETTLED_OPEN_VERDICT={SETTLED_OPEN_VERDICT}")
    print("TRIPLE02_CLOSED_SUCCESSOR_PREPARATION_PASS=1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
