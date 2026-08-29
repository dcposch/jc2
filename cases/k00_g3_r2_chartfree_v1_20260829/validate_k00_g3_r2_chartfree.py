#!/usr/bin/env python3
"""Validate custody, labels, and exact replay for K00-G3-R2-CHARTFREE/v1."""

from __future__ import annotations

import argparse
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
import re
import shutil
import subprocess


CASE_REL = "cases/k00_g3_r2_chartfree_v1_20260829"
ATLAS_REL = (
    "cases/max12_812_order2_u2_62_k00_grade7_fitting_atlas_v26_20260827/"
    "aws_box02_r2_held_compile/output/ATLAS_EXACT_POLYNOMIALS.json"
)
V27_BASIS_REL = (
    "cases/max12_812_order2_u2_62_k00_rank_compressed_atlas_v27_20260827/"
    "aws_r6a_r2_exact_base3/output/BASE3_R2_STANDARD_BASIS.txt"
)
V27_REVIEW_REL = "xmodel/k00-v27-base4-base3-base2-hostile-review-fable5-20260827.md"
DISCOVERY_REL = "xmodel/k00-chartfree-next-sol56-20260829.md"
PINNED = {
    ATLAS_REL: "d7ec6d18d58265421ff315fa00e38cd32992ac12f7d8166cf6c436e23bf06501",
    V27_BASIS_REL: "c8aa23e46f909e70c2c8d302ca67a415496df9a969f99817d2ef593f60f614c0",
    V27_REVIEW_REL: "738f46030a73fea2a06a8e3139ed9aa5e2001b72a579e459357af81f6801647a",
    DISCOVERY_REL: "ac843e4c3da54a60d96f8b15961f1d75ffb45ca7ebef1664d44c755fffb25d76",
}
BASIS_COMMIT = "92ebe92ad5986a47f01af9ed901260595dfed869"
STATUS = "PASS_K00_G3_R2_CHARTFREE_OBSTRUCTED_PRODUCER_EXPLICIT_CERTIFICATES"
VALIDATOR_STATUS = "PASS_K00_G3_R2_CHARTFREE_VALIDATOR_EXACT_REPLAY_SAME_CODE_FAMILY"
EXPECTED_OUTPUT = {
    "HRAW_TO_H.matrix",
    "H_BASIS.txt",
    "H_TO_Q4.matrix",
    "I2_NONZERO_LITERAL_INDICES.txt",
    "MANIFEST.sha256",
    "RESULT.json",
    "SOURCE_LABELS.json",
    "producer.sing",
    "producer.stderr",
    "producer.stdout",
    "replay.sing",
    "replay.stderr",
    "replay.stdout",
}
SOURCE_FREEZE_MEMBERS = {
    f"{CASE_REL}/README.md",
    f"{CASE_REL}/compile_k00_g3_r2_chartfree.py",
    f"{CASE_REL}/validate_k00_g3_r2_chartfree.py",
    *PINNED.keys(),
}
DIAGNOSTIC = re.compile(r"(?mi)^\s*\?|// \*\*|warning|error occurred|K00_G3_FAIL=")


def fail(message: object) -> "None":
    raise RuntimeError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def read_manifest(path: Path) -> dict[str, str]:
    entries: dict[str, str] = {}
    for line in path.read_text().splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  ([^/]+)", line)
        if match is None or match.group(2) in entries:
            fail(("malformed manifest", str(path), line))
        entries[match.group(2)] = match.group(1)
    return entries


def read_source_freeze(path: Path) -> dict[str, str]:
    entries: dict[str, str] = {}
    for line in path.read_text().splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        if match is None or match.group(2) in entries:
            fail(("malformed source freeze", line))
        entries[match.group(2)] = match.group(1)
    return entries


def marker(stdout: str, name: str) -> str:
    values = re.findall(rf"(?m)^{re.escape(name)}=(.*)$", stdout)
    if len(values) != 1:
        fail(("marker count", name, len(values)))
    return values[0].strip()


def extract_section(stdout: str, name: str) -> str:
    start = f"BEGIN_{name}\n"
    end = f"\nEND_{name}\n"
    if stdout.count(start) != 1 or stdout.count(end) != 1:
        fail(("section count", name))
    return stdout.split(start, 1)[1].split(end, 1)[0].strip() + "\n"


def expected_minor_labels(rank: int) -> list[tuple[int, list[int], list[int]]]:
    answer = []
    index = 0
    for rows in combinations(range(1, 8), rank):
        for cols in combinations(range(1, 8), rank):
            index += 1
            answer.append((index, list(rows), list(cols)))
    return answer


def validate_minor_labels(
    records: object,
    rank: int,
    nonzero_expected: int,
    raw_offset: int | None = None,
) -> list[int]:
    if not isinstance(records, list):
        fail("minor labels are not a list")
    expected = expected_minor_labels(rank)
    if len(records) != len(expected):
        fail(("literal minor count", rank, len(records), len(expected)))
    nonzero = []
    certificate_columns = []
    for record, (index, rows, cols) in zip(records, expected):
        if (
            record.get("literal_index") != index
            or record.get("rows_one_based") != rows
            or record.get("columns_one_based") != cols
            or not isinstance(record.get("zero"), bool)
        ):
            fail(("literal label mismatch", rank, index))
        if raw_offset is not None and record.get("raw_h_index") != raw_offset + index:
            fail(("raw H index mismatch", rank, index))
        if not record["zero"]:
            nonzero.append(index)
        if rank == 2:
            column = record.get("q4_certificate_column")
            if record["zero"] and column is not None:
                fail(("zero minor has certificate column", index))
            if not record["zero"]:
                certificate_columns.append(column)
    if len(nonzero) != nonzero_expected:
        fail(("nonzero minor census", rank, len(nonzero), nonzero_expected))
    if rank == 2 and certificate_columns != list(range(1, nonzero_expected + 1)):
        fail("q4 certificate-column order mismatch")
    return nonzero


def validate_labels(path: Path) -> list[int]:
    labels = json.loads(path.read_text())
    if labels.get("format") != "K00-G3-R2-CHARTFREE-LABELS/v1":
        fail("source-label format mismatch")
    if labels.get("basis_commit") != BASIS_COMMIT:
        fail("source-label basis commit mismatch")
    if labels.get("ring_variables") != [
        *[f"d{i}_{j}" for i in range(6) for j in range(1, 6)],
        "k10_0", "k10_1", "k10_2",
    ]:
        fail("source-label ring order mismatch")
    if labels.get("leading_variables") != [f"d{i}_1" for i in range(6)]:
        fail("leading-variable order mismatch")
    if labels.get("second_shell_variables") != [f"d{i}_2" for i in range(6)]:
        fail("second-shell order mismatch")
    if labels.get("newest_variables_for_A") != [
        *[f"d{i}_6" for i in range(6)], "k10_3"
    ]:
        fail("A newest-variable order mismatch")
    entries = labels.get("A_entries")
    if not isinstance(entries, list) or len(entries) != 49:
        fail("A-entry label count mismatch")
    for position, entry in enumerate(entries):
        row, col = divmod(position, 7)
        if (
            entry.get("row") != row + 1
            or entry.get("column") != col + 1
            or entry.get("newest_variable") != labels["newest_variables_for_A"][col]
            or not re.fullmatch(r"[0-9a-f]{64}", entry.get("singular_text_sha256", ""))
        ):
            fail(("A-entry label mismatch", position + 1))
    p3 = labels.get("P3_rows")
    if not isinstance(p3, list) or [item.get("row") for item in p3] != list(range(1, 8)):
        fail("P3 row-label mismatch")
    if any(
        item.get("Lambda_grade") != 3
        or not re.fullmatch(r"[0-9a-f]{64}", item.get("singular_text_sha256", ""))
        for item in p3
    ):
        fail("P3 grade/hash label mismatch")
    hraw = labels.get("Hraw")
    if not isinstance(hraw, dict):
        fail("Hraw labels missing")
    b = hraw.get("B")
    if not isinstance(b, list) or len(b) != 7:
        fail("B label count mismatch")
    for index, item in enumerate(b, 1):
        if item.get("raw_h_index") != index or item.get("name") != f"B{index}":
            fail(("B label mismatch", index))
    i3a = validate_minor_labels(hraw.get("I3A"), 3, 813, 7)
    i3e = validate_minor_labels(hraw.get("I3E3"), 3, 813, 1232)
    i2 = validate_minor_labels(labels.get("I2A"), 2, 351)
    counts = labels.get("counts")
    expected_counts = {
        "Hraw_ncols": 2457, "Hraw_nonzero": 1633,
        "I3A_literal": 1225, "I3A_nonzero": 813,
        "I3E3_literal": 1225, "I3E3_nonzero": 813,
        "I2A_literal": 441, "I2A_nonzero": 351, "I2A_zero": 90,
    }
    if counts != expected_counts:
        fail(("source-label count map mismatch", counts))
    if i3a != i3e:
        fail("I3(A) and I3(E3) nonzero literal maps unexpectedly differ")
    return i2


def validate_result(output: Path) -> None:
    result = json.loads((output / "RESULT.json").read_text())
    if result.get("status") != STATUS or result.get("basis_commit") != BASIS_COMMIT:
        fail("result status/basis mismatch")
    if result.get("source_hashes") != PINNED:
        fail("result source hashes mismatch")
    if result.get("certificate_type") != "explicit_two_stage_Hraw_to_H_and_H_to_all_q4":
        fail("certificate type mismatch")
    if result.get("same_code_family_replay_not_independent") is not True:
        fail("replay independence firewall missing")
    if result.get("power_unresolved_profile") != {"1": 291, "2": 60, "3": 36, "4": 0}:
        fail("power profile mismatch")
    if result.get("counterexample_claim") is not False or result.get("jc2_claim") is not False:
        fail("claim firewall mismatch")
    if set(result.get("mutations", {}).values()) != {"PASS"}:
        fail("mutation result mismatch")
    artifacts = result.get("artifacts")
    expected_artifacts = EXPECTED_OUTPUT - {"MANIFEST.sha256", "RESULT.json"}
    if not isinstance(artifacts, dict) or set(artifacts) != expected_artifacts:
        fail("result artifact map mismatch")
    for name, record in artifacts.items():
        path = output / name
        if record != {"sha256": digest(path), "bytes": path.stat().st_size}:
            fail(("result artifact metadata mismatch", name))


def validate() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path, nargs="?")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    case = root / CASE_REL
    output = (args.output or case / "output").resolve()
    if not output.is_dir() or {path.name for path in output.iterdir()} != EXPECTED_OUTPUT:
        fail("output member set mismatch")
    for relative, expected in PINNED.items():
        if digest(root / relative) != expected:
            fail(("pinned input mismatch", relative))
    freeze = read_source_freeze(case / "SOURCE_FREEZE.sha256")
    if set(freeze) != SOURCE_FREEZE_MEMBERS:
        fail("source-freeze member set mismatch")
    for relative, expected in freeze.items():
        if digest(root / relative) != expected:
            fail(("source-freeze hash mismatch", relative))
    manifest = read_manifest(output / "MANIFEST.sha256")
    if set(manifest) != EXPECTED_OUTPUT - {"MANIFEST.sha256"}:
        fail("output manifest member set mismatch")
    for name, expected in manifest.items():
        if digest(output / name) != expected:
            fail(("output hash mismatch", name))
    validate_result(output)
    i2 = validate_labels(output / "SOURCE_LABELS.json")
    index_text = (output / "I2_NONZERO_LITERAL_INDICES.txt").read_text()
    if index_text != ",".join(map(str, i2)) + ",\n":
        fail("I2 nonzero literal-index artifact mismatch")
    if (output / "producer.stderr").read_bytes() or (output / "replay.stderr").read_bytes():
        fail("stored Singular stderr is nonempty")
    producer_stdout = (output / "producer.stdout").read_text()
    if DIAGNOSTIC.search(producer_stdout):
        fail("stored producer diagnostics")
    if marker(producer_stdout, "K00_G3_R2_CHARTFREE") != STATUS:
        fail("stored producer status mismatch")
    sections = {
        "H_BASIS": "H_BASIS.txt",
        "HRAW_TO_H": "HRAW_TO_H.matrix",
        "H_TO_Q4": "H_TO_Q4.matrix",
    }
    for section, artifact in sections.items():
        if extract_section(producer_stdout, section) != (output / artifact).read_text():
            fail(("producer section/artifact mismatch", section))
    expected_replay = (
        f"K00_G3_R2_CHARTFREE_REPLAY={STATUS}\n"
        "REPLAY_AFFINE=0,0,0\n"
        "REPLAY_CENSUS=2457,1633,351\n"
        "REPLAY_POWER_PROFILE=291,60,36,0\n"
        "REPLAY_CERTIFICATES=EXACT_TWO_STAGE\n"
        "REPLAY_MUTATIONS=PASS\n"
    )
    if (output / "replay.stdout").read_text() != expected_replay:
        fail("stored replay stdout mismatch")
    singular = shutil.which("Singular")
    if singular is None:
        fail("Singular is unavailable")
    completed = subprocess.run(
        [singular, "-q", str(output / "replay.sing")],
        cwd=output,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=60,
    )
    if (
        completed.returncode
        or completed.stderr
        or completed.stdout != expected_replay
        or DIAGNOSTIC.search(completed.stdout)
    ):
        fail(("fresh replay failed", completed.returncode, completed.stderr[-2000:], completed.stdout[-4000:]))
    print(VALIDATOR_STATUS)


if __name__ == "__main__":
    validate()
