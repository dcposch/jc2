#!/usr/bin/env python3
"""Patch and verify the frozen TRIPLE03 root chart with semantic plants."""

from __future__ import annotations

import argparse
import hashlib
import json
import tarfile
from pathlib import Path


ARCHIVE_SHA = "1fe30b1ccf142791149b5152db519761681368b3e01c94cd82844802dee39787"
ORIGINAL_SCRIPT_SHA = "0141cffd951fde163341dfa1d835194fce6168f49a91abc3c7171e7342e166d9"
ORIGINAL_ARTIFACTS = {
    "TRIPLE03_CHART_DELTA.txt": "9e07a399764ace2008ad89af5c865326b0cdb65ceab1bcc83f5edcc63463144b",
    "TRIPLE03_ENDPOINT_DELTA2_CLEARED_NF.tsv": "a20a6af9de8f45a9b0486827cbc503111c554d6484fae3a59f150b0fbe8b7c28",
    "TRIPLE03_BORDERED_RPLUS1_IDENTITIES.tsv": "ba2576ce6b4cd9b0344e3a0e1f1246f188d1a7182fb66a4eda186c1dd45ad5cd",
}
TARGET = 'print("ENDPOINT_QUADRATIC=x14*x72+x1*x97");'

PLANT = r'''// BEGIN_RETROSPECTIVE_ROOT_ENDPOINT_SEMANTIC_PLANTS
poly ROOT_BORDERED_ZERO_RAW=R[1,1]*Y[1,1]+R[1,2]*Y[2,1]+R[1,3]*Y[3,1]+R[1,4]*Y[4,1]+R[1,5]*Y[5,1]+R[1,6]*Y[6,1]+R[1,7]*Y[7,1]+R[1,8]*Y[8,1]+R[1,9]*Y[9,1]+R[1,10]*Y[10,1];
poly ROOT_BORDERED_ZERO_NF=reduce(ROOT_BORDERED_ZERO_RAW,BRANCH_SB);
poly ROOT_BORDERED_DELTA_NF=reduce(DELTA,BRANCH_SB);
poly ROOT_BORDERED_PLANT_NF=reduce(ROOT_BORDERED_ZERO_RAW+DELTA,BRANCH_SB);
write("TRIPLE03_ROOT_BORDERED_SEMANTIC_PLANT.txt","base_nf|"+string(ROOT_BORDERED_ZERO_NF));
write("TRIPLE03_ROOT_BORDERED_SEMANTIC_PLANT.txt","delta_nf|"+string(ROOT_BORDERED_DELTA_NF));
write("TRIPLE03_ROOT_BORDERED_SEMANTIC_PLANT.txt","plant_nf|"+string(ROOT_BORDERED_PLANT_NF));
int ROOT_BORDERED_BASE_ZERO=(ROOT_BORDERED_ZERO_NF==0);
int ROOT_BORDERED_PLANT_NONZERO=(ROOT_BORDERED_PLANT_NF!=0);
int ROOT_BORDERED_PLANT_EQUALS_DELTA=(ROOT_BORDERED_PLANT_NF==ROOT_BORDERED_DELTA_NF);
print("ROOT_BORDERED_BASE_IDENTITY_ZERO="+string(ROOT_BORDERED_BASE_ZERO));
print("ROOT_BORDERED_NONZERO_PLANT_NF_NONZERO="+string(ROOT_BORDERED_PLANT_NONZERO));
print("ROOT_BORDERED_NONZERO_PLANT_EQUALS_DELTA="+string(ROOT_BORDERED_PLANT_EQUALS_DELTA));
if(ROOT_BORDERED_BASE_ZERO!=1 || ROOT_BORDERED_PLANT_NONZERO!=1 || ROOT_BORDERED_PLANT_EQUALS_DELTA!=1){ print("FATAL_ROOT_BORDERED_SEMANTIC_PLANT"); quit; }
poly ROOT_ENDPOINT_DIAGONAL_RAW=K[14,1]*K[72,1]+K[1,1]*K[97,1];
poly ROOT_ENDPOINT_DIAGONAL_NF=reduce(ROOT_ENDPOINT_DIAGONAL_RAW,BRANCH_SB);
poly ROOT_ENDPOINT_PLUS_ONE_NF=reduce(ROOT_ENDPOINT_DIAGONAL_RAW+1,BRANCH_SB);
poly ROOT_ENDPOINT_AFFINE_FAILURE=reduce(ROOT_ENDPOINT_PLUS_ONE_NF-ROOT_ENDPOINT_DIAGONAL_NF-1,BRANCH_SB);
write("TRIPLE03_ROOT_ENDPOINT_SEMANTIC_PLANT.txt","diagonal_nf|"+string(ROOT_ENDPOINT_DIAGONAL_NF));
write("TRIPLE03_ROOT_ENDPOINT_SEMANTIC_PLANT.txt","plus_one_nf|"+string(ROOT_ENDPOINT_PLUS_ONE_NF));
write("TRIPLE03_ROOT_ENDPOINT_SEMANTIC_PLANT.txt","affine_failure|"+string(ROOT_ENDPOINT_AFFINE_FAILURE));
int ROOT_ENDPOINT_DIAGONAL_ZERO=(ROOT_ENDPOINT_DIAGONAL_NF==0);
int ROOT_ENDPOINT_PLUS_ONE_NONZERO=(ROOT_ENDPOINT_PLUS_ONE_NF!=0);
int ROOT_ENDPOINT_AFFINE_PASS=(ROOT_ENDPOINT_AFFINE_FAILURE==0);
print("ROOT_ENDPOINT_DIAGONAL_NF_ZERO="+string(ROOT_ENDPOINT_DIAGONAL_ZERO));
print("ROOT_ENDPOINT_PLUS_ONE_PLANT_NF_NONZERO="+string(ROOT_ENDPOINT_PLUS_ONE_NONZERO));
print("ROOT_ENDPOINT_PLUS_ONE_PLANT_AFFINE_REPLAY="+string(ROOT_ENDPOINT_AFFINE_PASS));
if(ROOT_ENDPOINT_DIAGONAL_ZERO!=1 || ROOT_ENDPOINT_PLUS_ONE_NONZERO!=1 || ROOT_ENDPOINT_AFFINE_PASS!=1){ print("FATAL_ROOT_ENDPOINT_SEMANTIC_PLANT"); quit; }
print("ROOT_ENDPOINT_SEMANTIC_PLANTS_PASS=1");
// END_RETROSPECTIVE_ROOT_ENDPOINT_SEMANTIC_PLANTS
'''

REQUIRED_PATCH_TOKENS = (
    "BEGIN_RETROSPECTIVE_ROOT_ENDPOINT_SEMANTIC_PLANTS",
    "ROOT_BORDERED_BASE_IDENTITY_ZERO=",
    "ROOT_BORDERED_NONZERO_PLANT_NF_NONZERO=",
    "ROOT_BORDERED_NONZERO_PLANT_EQUALS_DELTA=",
    "ROOT_ENDPOINT_DIAGONAL_NF_ZERO=",
    "ROOT_ENDPOINT_PLUS_ONE_PLANT_NF_NONZERO=",
    "ROOT_ENDPOINT_PLUS_ONE_PLANT_AFFINE_REPLAY=",
    "ROOT_ENDPOINT_SEMANTIC_PLANTS_PASS=1",
    "FATAL_ROOT_BORDERED_SEMANTIC_PLANT",
    "FATAL_ROOT_ENDPOINT_SEMANTIC_PLANT",
)

REQUIRED_RUN_MARKERS = (
    "CHART_DELTA_NF_NONZERO=1",
    "BANKED_DELTA_REPLAY_EQUAL=1",
    "COMPLETE_BORDERED_RPLUS1_IDENTITY_COUNT=66",
    "BORDERED_RPLUS1_IDENTITY_FAILURES=0",
    "FULL_106_ROW_KERNEL_REPLAY_COUNT=636",
    "FULL_106_ROW_KERNEL_REPLAY_FAILURES=0",
    "ROOT_BORDERED_BASE_IDENTITY_ZERO=1",
    "ROOT_BORDERED_NONZERO_PLANT_NF_NONZERO=1",
    "ROOT_BORDERED_NONZERO_PLANT_EQUALS_DELTA=1",
    "ROOT_ENDPOINT_DIAGONAL_NF_ZERO=1",
    "ROOT_ENDPOINT_PLUS_ONE_PLANT_NF_NONZERO=1",
    "ROOT_ENDPOINT_PLUS_ONE_PLANT_AFFINE_REPLAY=1",
    "ROOT_ENDPOINT_SEMANTIC_PLANTS_PASS=1",
    "ENDPOINT_COEFFICIENT_COUNT=21",
    "ENDPOINT_COEFFICIENT_NF_NONZERO_COUNT=0",
    "CHART_CLASSIFICATION=ENDPOINT_DEAD_ONLY_ON_D_DELTA",
    "REDUCER_SAFE_ENDPOINT_CHART_COMPLETE=1",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_patch(text: str) -> None:
    if text.count("BEGIN_RETROSPECTIVE_ROOT_ENDPOINT_SEMANTIC_PLANTS") != 1:
        raise RuntimeError("PLANT_BLOCK_CENSUS_FAILURE")
    for token in REQUIRED_PATCH_TOKENS:
        if token not in text:
            raise RuntimeError(f"MISSING_PATCH_TOKEN:{token}")


def archive_member(archive: Path, suffix: str) -> bytes:
    with tarfile.open(archive, "r:gz") as handle:
        matches = [m for m in handle.getmembers() if m.isfile() and m.name == suffix]
        if len(matches) != 1:
            raise RuntimeError(f"ARCHIVE_MEMBER_CENSUS:{suffix}:{len(matches)}")
        stream = handle.extractfile(matches[0])
        if stream is None:
            raise RuntimeError(f"ARCHIVE_MEMBER_UNREADABLE:{suffix}")
        return stream.read()


def prepare(archive: Path, output_script: Path, work: Path) -> None:
    if sha256(archive) != ARCHIVE_SHA:
        raise RuntimeError("ORIGINAL_ARCHIVE_SHA_DRIFT")
    original = archive_member(archive, "output/triple03/chart.sing")
    if hashlib.sha256(original).hexdigest() != ORIGINAL_SCRIPT_SHA:
        raise RuntimeError("ORIGINAL_SCRIPT_SHA_DRIFT")
    work.mkdir(parents=True, exist_ok=True)
    original_path = work / "ORIGINAL_TRIPLE03_chart.sing"
    original_path.write_bytes(original)
    text = original.decode("utf-8")
    if text.count(TARGET) != 1:
        raise RuntimeError(f"PATCH_TARGET_CENSUS:{text.count(TARGET)}")
    patched = text.replace(TARGET, PLANT + TARGET, 1)
    validate_patch(patched)
    mutation = patched.replace(
        'print("ROOT_ENDPOINT_SEMANTIC_PLANTS_PASS=1");', "", 1)
    try:
        validate_patch(mutation)
    except RuntimeError:
        mutation_rejected = True
    else:
        mutation_rejected = False
    if not mutation_rejected:
        raise RuntimeError("ENDPOINT_PLANT_MUTATION_NOT_REJECTED")
    output_script.parent.mkdir(parents=True, exist_ok=True)
    output_script.write_text(patched)
    manifest = {
        "archive_sha256": sha256(archive),
        "mutation_rejected": mutation_rejected,
        "original_script_sha256": sha256(original_path),
        "patched_script_sha256": sha256(output_script),
    }
    (work / "PATCH_MANIFEST.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    print(f"ORIGINAL_ROOT_CHART_SHA256={manifest['original_script_sha256']}")
    print(f"PATCHED_ROOT_CHART_SHA256={manifest['patched_script_sha256']}")
    print("ORIGINAL_ROOT_CHART_BYTES_PRESERVED=1")
    print("ENDPOINT_PLANT_MUTATION_REJECTED=1")
    print("ROOT_CHART_SEMANTIC_PLANT_BUILD_PASS=1")


def parse_pairs(path: Path) -> dict[str, str]:
    pairs: dict[str, str] = {}
    for raw in path.read_text().splitlines():
        if not raw.strip():
            continue
        key, sep, value = raw.partition("|")
        if not sep or key in pairs:
            raise RuntimeError(f"PLANT_FILE_FORMAT:{path.name}:{raw}")
        pairs[key] = value
    return pairs


def verify(run: Path) -> None:
    stdout = run / "run.stdout.txt"
    lines = stdout.read_text(errors="replace").splitlines()
    line_set = set(lines)
    for marker in REQUIRED_RUN_MARKERS:
        if marker not in line_set:
            raise RuntimeError(f"MISSING_RUN_MARKER:{marker}")
    if any("FATAL_" in line for line in lines):
        raise RuntimeError("FATAL_MARKER_IN_TRANSCRIPT")
    replayed: dict[str, str] = {}
    for name, expected in ORIGINAL_ARTIFACTS.items():
        actual = sha256(run / name)
        replayed[name] = actual
        if actual != expected:
            raise RuntimeError(f"ORIGINAL_ARTIFACT_DRIFT:{name}:{actual}")
    endpoint = parse_pairs(run / "TRIPLE03_ROOT_ENDPOINT_SEMANTIC_PLANT.txt")
    if endpoint != {
        "diagonal_nf": "0", "plus_one_nf": "1", "affine_failure": "0"
    }:
        raise RuntimeError(f"ENDPOINT_PLANT_VALUE_FAILURE:{endpoint}")
    bordered = parse_pairs(run / "TRIPLE03_ROOT_BORDERED_SEMANTIC_PLANT.txt")
    if bordered.get("base_nf") != "0":
        raise RuntimeError(f"BORDERED_BASE_NOT_ZERO:{bordered}")
    if bordered.get("plant_nf") == "0":
        raise RuntimeError(f"BORDERED_PLANT_ZERO:{bordered}")
    if bordered.get("plant_nf") != bordered.get("delta_nf"):
        raise RuntimeError(f"BORDERED_PLANT_DELTA_MISMATCH:{bordered}")
    payload = {
        "classification": "TRIPLE03_ROOT_D_DELTA_ENDPOINT_DEAD_WITH_SEMANTIC_PLANTS",
        "endpoint_plant": endpoint,
        "bordered_plant": bordered,
        "original_artifact_sha256": replayed,
        "run_stdout_sha256": sha256(stdout),
    }
    (run / "RESULT.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n")
    (run / "VERDICT.txt").write_text(payload["classification"] + "\n")
    print("ORIGINAL_ROOT_RESULT_BYTES_EXACTLY_REPLAYED=1")
    print("TRIPLE03_ROOT_D_DELTA_ENDPOINT_DEAD_WITH_SEMANTIC_PLANTS=1")
    print("ROOT_CHART_SEMANTIC_PLANT_VERIFY_PASS=1")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", type=Path)
    parser.add_argument("--output-script", type=Path)
    parser.add_argument("--work", type=Path)
    parser.add_argument("--verify-run", type=Path)
    args = parser.parse_args()
    if args.verify_run is not None:
        if any(v is not None for v in (args.archive, args.output_script, args.work)):
            parser.error("--verify-run is exclusive")
        verify(args.verify_run)
    else:
        if any(v is None for v in (args.archive, args.output_script, args.work)):
            parser.error("prepare mode requires --archive --output-script --work")
        prepare(args.archive, args.output_script, args.work)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
