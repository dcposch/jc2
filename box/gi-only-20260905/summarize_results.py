#!/usr/bin/env python3
"""Strictly aggregate the six canonical G_i-only exact-Q solve results.

The program reads, but never changes, chart or solve-run artifacts.  Its sole
write is an atomic replacement of ``final-solve-summary.json`` after all six
classes pass validation.  A failed validation leaves the output untouched.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import time
from typing import Any, Iterable, Mapping, Sequence


HERE = Path(__file__).resolve().parent
EXPECTED_CLASS_IDS = (
    "C_n24m16_Mm12_m2_5_ell1_s4",
    "C_n18m12_M2_9_ell2_s3",
    "C_n24m18_Mm15_14_ell1_s3",
    "C_n24m16_M12_17_ell1_s3",
    "C_n24m18_M9_20_ell1_s3",
    "C_n16m12_M6_13_ell3_s3",
)
SHA256_HEX = frozenset("0123456789abcdef")
GUIDED_GB_SHA256 = "501f3b1fed8ad0d26c7535a3c79d6ca74c448a4555f94570a4835d9f740781f3"
LANE_WORKERS = {
    "i-0889ee47ceb889561": "ip-172-30-0-236",
    "i-0d8bf8dd339a2e161": "ip-172-30-0-238",
    "i-0fe012c4207c7a220": "ip-172-30-0-235",
    "i-0a067499279342f0c": "ip-172-30-0-75",
}
SPARSE_EXTRACTION_CLASSES = {
    "C_n24m16_M12_17_ell1_s3",
    "C_n24m18_M9_20_ell1_s3",
    "C_n16m12_M6_13_ell3_s3",
}
DECLARED_ONLY_ARTIFACTS = {
    "$.inputs.meta_prebuild": "prebuild metadata was superseded in place by emit-guided; its declared SHA-256 is retained",
    "$.inputs.class_json": "prebuild class metadata was superseded in place by emit-guided; its declared SHA-256 is retained",
    "$.modular_screen.solver": "non-promotional msolve binary was hashed on the worker but was not copied",
}


class SummaryError(RuntimeError):
    """A result is missing, ambiguous, incomplete, or internally invalid."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SummaryError(message)


def utc_now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def file_artifact(path: Path) -> dict[str, Any]:
    return {
        "path": str(path.resolve()),
        "bytes": path.stat().st_size,
        "sha256": sha256_file(path),
    }


def load_object(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8", errors="strict"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise SummaryError(f"cannot read JSON object {path}: {exc}") from exc
    require(isinstance(value, dict), f"expected JSON object: {path}")
    return value


def load_manifest(path: Path) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    try:
        value = json.loads(path.read_text(encoding="utf-8", errors="strict"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise SummaryError(f"cannot read class manifest {path}: {exc}") from exc
    require(isinstance(value, list), f"class manifest is not a list: {path}")
    require(len(value) == len(EXPECTED_CLASS_IDS), f"class manifest has {len(value)} entries, expected six")
    require(all(isinstance(item, dict) for item in value), "class manifest contains a non-object entry")
    entries = list(value)
    ids = [item.get("class_id") for item in entries]
    require(ids == list(EXPECTED_CLASS_IDS), f"class manifest order/content mismatch: {ids!r}")
    by_id: dict[str, dict[str, Any]] = {}
    for item in entries:
        class_id = item["class_id"]
        require(item.get("canonical_stem") == f"{class_id}_G", f"bad canonical stem for {class_id}")
        unknowns = item.get("unknowns_without_T", item.get("parameter_count"))
        require(type(unknowns) is int and unknowns > 0, f"bad unknown count for {class_id}")
        require(item.get("unknowns_with_T") == unknowns + 1, f"bad T-extended unknown count for {class_id}")
        by_id[class_id] = item
    return entries, by_id


def result_paths(bundle: Path) -> list[Path]:
    canonical = bundle.glob("classes/*/solve/solve-result.json")
    fleet_legacy = bundle.glob("fleet/*/*/solve/solve-result.json")
    fleet_snapshot = bundle.glob("fleet/*/*/class/solve/solve-result.json")
    fleet_attempts = bundle.glob("fleet/*/*/attempt*/class/solve/solve-result.json")
    return sorted({path.resolve() for path in (*canonical, *fleet_legacy, *fleet_snapshot, *fleet_attempts)})


def path_class_id(bundle: Path, path: Path) -> str:
    relative = path.resolve().relative_to(bundle.resolve())
    parts = relative.parts
    if len(parts) == 4 and parts[0] == "classes" and parts[2:] == ("solve", "solve-result.json"):
        return parts[1]
    if len(parts) == 5 and parts[0] == "fleet" and parts[3:] == ("solve", "solve-result.json"):
        require(parts[1] in LANE_WORKERS, f"solve-result belongs to a non-lane fleet ID: {path}")
        return parts[2]
    if len(parts) == 6 and parts[0] == "fleet" and parts[3:] == ("class", "solve", "solve-result.json"):
        require(parts[1] in LANE_WORKERS, f"solve-result belongs to a non-lane fleet ID: {path}")
        return parts[2]
    if (
        len(parts) == 7
        and parts[0] == "fleet"
        and re.fullmatch(r"attempt[1-9]\d*", parts[3])
        and parts[4:] == ("class", "solve", "solve-result.json")
    ):
        require(parts[1] in LANE_WORKERS, f"solve-result belongs to a non-lane fleet ID: {path}")
        return parts[2]
    raise SummaryError(f"unexpected solve-result location: {path}")


def attempt_number(bundle: Path, path: Path) -> int | None:
    parts = path.resolve().relative_to(bundle.resolve()).parts
    if parts[0] != "fleet":
        return None
    for part in parts:
        match = re.fullmatch(r"attempt([1-9]\d*)", part)
        if match:
            return int(match.group(1))
    return 0


def is_unnumbered_fleet_snapshot(bundle: Path, path: Path) -> bool:
    parts = path.resolve().relative_to(bundle.resolve()).parts
    return len(parts) == 6 and parts[0] == "fleet" and parts[3:] == ("class", "solve", "solve-result.json")


def historical_attempt(path: Path, class_id: str) -> dict[str, Any]:
    result = load_object(path)
    require(result.get("schema") == "moh-gi-only-exact-q-solve-v1", f"{class_id}: historical attempt schema mismatch")
    require(result.get("state") == "FINISHED", f"{class_id}: historical attempt is not FINISHED")
    require(result.get("class_id") == class_id, f"{class_id}: historical attempt embedded class mismatch")
    require(result.get("canonical_stem") == f"{class_id}_G", f"{class_id}: historical attempt stem mismatch")
    builder = result.get("builder_run") if isinstance(result.get("builder_run"), dict) else None
    return {
        "result": file_artifact(path),
        "verdict": result.get("verdict"),
        "verdict_detail": result.get("verdict_detail"),
        "builder": None
        if builder is None
        else {
            "watchdog_seconds": builder.get("watchdog_seconds"),
            "timed_out": builder.get("timed_out"),
            "returncode": builder.get("returncode"),
            "wall_seconds": builder.get("elapsed_seconds"),
            "peak_rss_kib": builder.get("peak_rss_kib"),
            "peak_rss_source": builder.get("peak_rss_source"),
        },
    }


def discover_results(bundle: Path) -> dict[str, tuple[Path, list[Path], list[dict[str, Any]]]]:
    grouped: dict[str, list[Path]] = {class_id: [] for class_id in EXPECTED_CLASS_IDS}
    for path in result_paths(bundle):
        class_id = path_class_id(bundle, path)
        require(class_id in grouped, f"solve-result lies under an unknown class directory: {path}")
        grouped[class_id].append(path)
    selected: dict[str, tuple[Path, list[Path], list[dict[str, Any]]]] = {}
    for class_id in EXPECTED_CLASS_IDS:
        candidates = grouped[class_id]
        require(candidates, f"missing FINISHED solve-result for {class_id}")
        canonical = bundle / "classes" / class_id / "solve" / "solve-result.json"
        numbered = [(attempt_number(bundle, path), path) for path in candidates]
        positive_attempts = [(number, path) for number, path in numbered if number is not None and number > 0]
        historical: list[dict[str, Any]] = []
        for number, path in sorted(positive_attempts):
            record = historical_attempt(path, class_id)
            record["attempt_number"] = number
            historical.append(record)
        final_snapshots = [path for path in candidates if is_unnumbered_fleet_snapshot(bundle, path)]
        if final_snapshots:
            require(len(final_snapshots) == 1, f"{class_id}: multiple unnumbered final fleet snapshots")
            chosen = final_snapshots[0]
            chosen_hash = sha256_file(chosen)
            replicas = [chosen]
            for number, path in numbered:
                if path == chosen or (number is not None and number > 0):
                    continue
                require(sha256_file(path) == chosen_hash, f"{class_id}: canonical/fleet mirror differs from unnumbered final snapshot")
                replicas.append(path)
        elif positive_attempts:
            raise SummaryError(f"missing unnumbered final fleet snapshot for {class_id}; attemptN trees are historical only")
        else:
            by_hash: dict[str, list[Path]] = {}
            for path in candidates:
                by_hash.setdefault(sha256_file(path), []).append(path)
            require(
                len(by_hash) == 1,
                f"ambiguous non-identical solve-results for {class_id}: "
                + ", ".join(str(path) for path in candidates),
            )
            immutable = [path for path in candidates if "/fleet/" in path.as_posix() and "/class/solve/" in path.as_posix()]
            chosen = immutable[0] if immutable else canonical.resolve() if canonical.is_file() else candidates[0]
            replicas = candidates
        selected[class_id] = (chosen, replicas, historical)
    return selected


def integer(value: Any, label: str, *, minimum: int | None = None) -> int:
    require(type(value) is int, f"{label} is not an integer: {value!r}")
    if minimum is not None:
        require(value >= minimum, f"{label} is below {minimum}: {value}")
    return value


def number(value: Any, label: str, *, minimum: float | None = None) -> float:
    require(type(value) in (int, float), f"{label} is not numeric: {value!r}")
    converted = float(value)
    if minimum is not None:
        require(converted >= minimum, f"{label} is below {minimum}: {converted}")
    return converted


def mapping(value: Any, label: str) -> Mapping[str, Any]:
    require(isinstance(value, dict), f"{label} is not an object")
    return value


def valid_sha256(value: Any) -> bool:
    return isinstance(value, str) and len(value) == 64 and set(value) <= SHA256_HEX


def artifact_record(value: Any, label: str) -> dict[str, Any]:
    item = mapping(value, label)
    require(isinstance(item.get("path"), str) and item["path"], f"{label}.path is absent")
    size = integer(item.get("bytes"), f"{label}.bytes", minimum=0)
    digest = item.get("sha256")
    require(valid_sha256(digest), f"{label}.sha256 is invalid")
    return {"path": item["path"], "bytes": size, "sha256": digest}


def copied_path_for(result_path: Path, declared_path: str) -> Path | None:
    """Map a worker's original solve path into its collected solve directory."""

    def beneath(base: Path, suffix: str) -> Path:
        base = base.resolve()
        candidate = (base / Path(suffix)).resolve()
        require(candidate.is_relative_to(base), f"artifact path traversal is not allowed: {declared_path}")
        return candidate

    normalized = declared_path.replace("\\", "/")
    marker = "/solve/"
    if marker in normalized:
        suffix = normalized.split(marker, 1)[1]
        candidate = beneath(result_path.parent, suffix)
        if candidate.is_file():
            return candidate
    # A collected fleet result normally sits at fleet/ID/CLASS/solve.  When
    # the entire remote class directory is retained, map its original
    # classes/CLASS/{rows,jobs,meta,...} path beside that solve directory.
    class_marker = "/classes/"
    if class_marker in normalized:
        after_classes = normalized.split(class_marker, 1)[1]
        pieces = after_classes.split("/", 1)
        if len(pieces) == 2:
            candidate = beneath(result_path.parent.parent, pieces[1])
            if candidate.is_file():
                return candidate
    repo_bundle_marker = "box/gi-only-20260905/"
    if normalized.startswith(repo_bundle_marker):
        bundle = next((parent for parent in result_path.parents if parent.name == "gi-only-20260905"), None)
        if bundle is not None:
            candidate = beneath(bundle, normalized[len(repo_bundle_marker) :])
            if candidate.is_file():
                return candidate
    direct = Path(declared_path)
    if direct.is_file():
        return direct
    return None


def verify_copied_artifact(result_path: Path, value: Any, label: str, *, required: bool) -> dict[str, Any]:
    declared = artifact_record(value, label)
    local = copied_path_for(result_path, declared["path"])
    if local is None:
        require(not required, f"collected custody file is absent for {label}: {declared['path']}")
        return {**declared, "local_verification": "DECLARED_ONLY"}
    actual = file_artifact(local)
    require(actual["bytes"] == declared["bytes"], f"byte-count mismatch for {label}: {local}")
    require(actual["sha256"] == declared["sha256"], f"SHA-256 mismatch for {label}: {local}")
    return {**declared, "local_verification": "PASS", "collected_path": actual["path"]}


def walk_declared_artifacts(value: Any, pointer: str = "$") -> Iterable[tuple[str, Mapping[str, Any]]]:
    if isinstance(value, dict):
        if {"path", "bytes", "sha256"} <= set(value):
            yield pointer, value
        for key, child in value.items():
            yield from walk_declared_artifacts(child, f"{pointer}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk_declared_artifacts(child, f"{pointer}[{index}]")


def declared_artifact_index(result_path: Path, result: Mapping[str, Any]) -> list[dict[str, Any]]:
    records = []
    for pointer, value in walk_declared_artifacts(result):
        declared = artifact_record(value, pointer)
        if pointer in DECLARED_ONLY_ARTIFACTS:
            records.append(
                {
                    "json_pointer": pointer,
                    **declared,
                    "local_verification": "DECLARED_ONLY",
                    "reason": DECLARED_ONLY_ARTIFACTS[pointer],
                }
            )
            continue
        local = copied_path_for(result_path, declared["path"])
        require(local is not None, f"custody artifact is declared but not collected for {pointer}: {declared['path']}")
        actual = file_artifact(local)
        require(actual["bytes"] == declared["bytes"], f"byte-count mismatch for {pointer}: {local}")
        require(actual["sha256"] == declared["sha256"], f"SHA-256 mismatch for {pointer}: {local}")
        record = {
            "json_pointer": pointer,
            **declared,
            "local_verification": "PASS",
            "collected_path": actual["path"],
        }
        records.append(record)
    return records


def binary_hash_record(value: Any, label: str) -> dict[str, Any]:
    item = mapping(value, label)
    path_value = item.get("path")
    digest = item.get("sha256")
    require(isinstance(path_value, str) and path_value, f"{label}.path is absent")
    require(valid_sha256(digest), f"{label}.sha256 is invalid")
    path = Path(path_value)
    record: dict[str, Any] = {"path": path_value, "sha256": digest, "local_verification": "DECLARED_ONLY"}
    if path.is_file():
        actual = file_artifact(path)
        require(actual["sha256"] == digest, f"SHA-256 mismatch for {label}: {path}")
        record.update(local_verification="PASS", collected_path=actual["path"], bytes=actual["bytes"])
    if "version_head" in item:
        record["version_head"] = item["version_head"]
    return record


def recount_rows(path: Path, class_id: str) -> tuple[str, int]:
    with path.open(encoding="utf-8", errors="strict") as handle:
        header = handle.readline().rstrip("\n")
        require(header.startswith("source_index|"), f"{class_id}: coefficient-row header is invalid")
        count = 0
        for line_number, line in enumerate(handle, start=2):
            line = line.rstrip("\n")
            if not line:
                continue
            pieces = line.split("|", 4)
            require(len(pieces) == 5, f"{class_id}: malformed coefficient row at line {line_number}")
            expression = pieces[4].strip()
            if expression and expression not in {"0", "(0)"}:
                count += 1
    return header, count


def validate_verification_custody(result_path: Path, result: Mapping[str, Any], class_id: str, stem: str) -> dict[str, Any]:
    verification = mapping(result.get("verification"), f"{class_id}.verification")
    embedded = mapping(verification.get("class_result"), f"{class_id}.verification.class_result")
    class_required = {
        "class_id": class_id,
        "canonical_stem": stem,
        "status": "PASS",
        "blockwise_subset_verified": True,
        "specialization_verified": True,
        "orientation_verified": True,
        "production_sign_isomorphism_verified": True,
        "production_coordinate_only_specialization_verified": True,
    }
    for key, expected in class_required.items():
        require(embedded.get(key) == expected, f"{class_id}: embedded verification {key} mismatch")
    receipt_artifact = verify_copied_artifact(
        result_path,
        verification.get("receipt"),
        f"{class_id}.verification.receipt",
        required=True,
    )
    receipt_path = Path(receipt_artifact["collected_path"])
    receipt = load_object(receipt_path)
    top_required = {
        "status": "PASS",
        "all_blockwise_subset": True,
        "all_specializations": True,
        "all_orientation_checks": True,
        "all_native_zero_specializations": True,
        "all_production_sign_isomorphisms": True,
        "all_production_coordinate_only_specializations": True,
    }
    for key, expected in top_required.items():
        require(receipt.get(key) == expected, f"{class_id}: verification receipt {key} mismatch")
    matches = [
        item
        for item in receipt.get("results", [])
        if isinstance(item, dict) and item.get("class_id") == class_id
    ]
    require(len(matches) == 1, f"{class_id}: verification receipt has {len(matches)} matching class entries")
    for key, expected in class_required.items():
        require(matches[0].get(key) == expected, f"{class_id}: receipt class entry {key} mismatch")
    return receipt_artifact


def validate_sparse_extraction_custody(
    result_path: Path,
    result: Mapping[str, Any],
    postemit: Mapping[str, Any],
    rows: Mapping[str, Any],
    class_id: str,
) -> dict[str, Any]:
    value = postemit.get("coefficient_rows_extraction_custody")
    if class_id not in SPARSE_EXTRACTION_CLASSES:
        require(value is None, f"{class_id}: unexpected sparse-extraction activation custody")
        return {"method": "canonical_native_builder", "status": "PASS", "sparse_activation": False}
    custody = mapping(value, f"{class_id}.coefficient_rows_extraction_custody")
    required = {
        "method": "exact_sparse_monic_y_division",
        "status": "PASS",
        "literal_J_PQ_controls_passed": True,
        "native_literal_row_controls_passed": True,
        "no_coordinate_specialization": True,
        "no_auxiliary_variables": True,
    }
    for key, expected in required.items():
        require(custody.get(key) == expected, f"{class_id}: sparse extraction custody {key} mismatch")
    custody_receipt = verify_copied_artifact(
        result_path,
        custody.get("custody_receipt"),
        f"{class_id}.sparse.custody_receipt",
        required=True,
    )
    extractor = verify_copied_artifact(
        result_path,
        custody.get("sparse_extractor"),
        f"{class_id}.sparse.extractor",
        required=True,
    )
    canonical_rows = verify_copied_artifact(
        result_path,
        custody.get("canonical_rows"),
        f"{class_id}.sparse.canonical_rows",
        required=True,
    )
    require(canonical_rows["sha256"] == rows["sha256"], f"{class_id}: sparse custody rows SHA differs from solve rows")
    require(canonical_rows["bytes"] == rows["bytes"], f"{class_id}: sparse custody rows size differs from solve rows")
    builder_hash = custody.get("canonical_builder_sha256")
    require(valid_sha256(builder_hash), f"{class_id}: sparse custody canonical builder SHA is invalid")
    inputs = mapping(result.get("inputs"), f"{class_id}.inputs")
    input_builder = artifact_record(inputs.get("builder"), f"{class_id}.inputs.builder")
    require(input_builder["sha256"] == builder_hash, f"{class_id}: sparse custody builder SHA differs from solve input")
    receipt = load_object(Path(custody_receipt["collected_path"]))
    require(
        receipt.get("schema") == "moh-gi-only-sparse-extraction-activation-custody-v1",
        f"{class_id}: sparse activation receipt schema mismatch",
    )
    require(receipt.get("status") == "PASS", f"{class_id}: sparse activation receipt is not PASS")
    require(receipt.get("all_native_exact_controls_passed") is True, f"{class_id}: sparse native exact controls did not pass")
    receipt_extractor = artifact_record(receipt.get("sparse_extractor"), f"{class_id}.sparse.receipt.extractor")
    require(
        receipt_extractor["sha256"] == extractor["sha256"] and receipt_extractor["bytes"] == extractor["bytes"],
        f"{class_id}: sparse extractor pointer differs from activation receipt",
    )
    frozen_builder_fix = verify_copied_artifact(
        result_path,
        receipt.get("frozen_builder_fix"),
        f"{class_id}.sparse.frozen_builder_fix",
        required=True,
    )
    matches = [
        item
        for item in receipt.get("classes", [])
        if isinstance(item, dict) and item.get("class_id") == class_id
    ]
    require(len(matches) == 1, f"{class_id}: sparse receipt has {len(matches)} class entries")
    class_receipt = matches[0]
    class_required = {
        "status": "PASS",
        "stem": f"{class_id}_G",
        "all_G_coordinates_retained": True,
        "coordinate_specializations": 0,
        "auxiliary_variables": 0,
        "literal_orientation": "J(P,Q)-c*x^ell",
        "inverse_generator": "T*c-1",
    }
    for key, expected in class_required.items():
        require(class_receipt.get(key) == expected, f"{class_id}: sparse class receipt {key} mismatch")
    sparse_coefficients = integer(class_receipt.get("coefficient_generators"), f"{class_id}.sparse.coefficient_generators", minimum=1)
    sparse_total = integer(class_receipt.get("generators_including_Tc_minus_1"), f"{class_id}.sparse.generators_including_Tc_minus_1", minimum=2)
    require(sparse_coefficients + 1 == sparse_total, f"{class_id}: sparse receipt generator totals mismatch")
    require(sparse_coefficients == postemit.get("jacobian_coefficient_generator_count"), f"{class_id}: sparse receipt coefficient count mismatch")
    receipt_builder = artifact_record(class_receipt.get("canonical_builder"), f"{class_id}.sparse.receipt.builder")
    require(receipt_builder["sha256"] == builder_hash, f"{class_id}: sparse receipt builder SHA mismatch")
    candidate_rows = artifact_record(class_receipt.get("candidate_rows"), f"{class_id}.sparse.receipt.candidate_rows")
    require(candidate_rows["sha256"] == canonical_rows["sha256"] and candidate_rows["bytes"] == canonical_rows["bytes"], f"{class_id}: activated sparse rows differ from candidate")
    activation = mapping(class_receipt.get("activation"), f"{class_id}.sparse.receipt.activation")
    activated_rows = artifact_record(activation.get("canonical_rows"), f"{class_id}.sparse.receipt.activation.rows")
    require(activated_rows["sha256"] == canonical_rows["sha256"] and activated_rows["bytes"] == canonical_rows["bytes"], f"{class_id}: activation rows mismatch")
    candidate_receipt_artifact = verify_copied_artifact(
        result_path,
        class_receipt.get("candidate_receipt"),
        f"{class_id}.sparse.candidate_receipt",
        required=True,
    )
    candidate_receipt = load_object(Path(candidate_receipt_artifact["collected_path"]))
    require(candidate_receipt.get("schema") == "moh-gi-only-sparse-hadic-extraction-experiment-v1", f"{class_id}: sparse candidate receipt schema mismatch")
    require(candidate_receipt.get("status") == "PASS" and candidate_receipt.get("class_id") == class_id, f"{class_id}: sparse candidate receipt identity/status mismatch")
    require(candidate_receipt.get("rows_sha256") == canonical_rows["sha256"], f"{class_id}: candidate receipt rows SHA mismatch")
    require(candidate_receipt.get("coefficient_generators") == sparse_coefficients, f"{class_id}: candidate receipt count mismatch")
    return {
        "method": custody["method"],
        "status": "PASS",
        "sparse_activation": True,
        "canonical_rows": canonical_rows,
        "canonical_builder_sha256": builder_hash,
        "custody_receipt": custody_receipt,
        "sparse_extractor": extractor,
        "frozen_builder_fix": frozen_builder_fix,
        "candidate_receipt": candidate_receipt_artifact,
        "extraction_wall_seconds": candidate_receipt.get("elapsed_seconds"),
        "extraction_peak_rss_kib": candidate_receipt.get("peak_rss_kib"),
        "activation_action": activation.get("action"),
    }


def named_controls_pass(controls: Mapping[str, Any], class_id: str) -> bool:
    named = mapping(controls.get("named"), f"{class_id}.controls.named")
    require(set(named) == {"ring", "empty", "nonempty"}, f"{class_id}: unexpected named-control set")
    passed = True
    for name in ("ring", "empty", "nonempty"):
        item = mapping(named[name], f"{class_id}.controls.named.{name}")
        pass_count = integer(item.get("pass_count"), f"{class_id}.{name}.pass_count", minimum=0)
        fail_count = integer(item.get("fail_count"), f"{class_id}.{name}.fail_count", minimum=0)
        passed = passed and pass_count >= 1 and fail_count == 0
    require(controls.get("named_controls_pass") is passed, f"{class_id}: named-controls summary mismatch")
    return passed


def validate_control_summary(
    controls: Mapping[str, Any], class_id: str, total_generators: int
) -> tuple[bool, Mapping[str, Any]]:
    named_pass = named_controls_pass(controls, class_id)
    main = mapping(controls.get("guided_main"), f"{class_id}.controls.guided_main")
    require(type(main.get("accepted")) is bool, f"{class_id}: guided accepted flag is not boolean")
    require(type(main.get("nf_all_zero")) is bool, f"{class_id}: guided NF flag is not boolean")
    require(type(main.get("unit")) is bool, f"{class_id}: guided unit flag is not boolean")
    missing = main.get("missing_markers")
    require(isinstance(missing, list) and all(isinstance(item, str) for item in missing), f"{class_id}: bad missing-marker list")
    singular_errors = controls.get("singular_error_lines")
    require(isinstance(singular_errors, list) and all(isinstance(item, str) for item in singular_errors), f"{class_id}: bad Singular-error list")
    expected = integer(
        controls.get("expected_generators_including_Tc_minus_1"),
        f"{class_id}.controls.expected_generators",
        minimum=1,
    )
    require(expected == total_generators, f"{class_id}: control generator count differs from ideal count")
    guided_counts = controls.get("guided_generator_counts")
    require(isinstance(guided_counts, list) and all(type(item) is int for item in guided_counts), f"{class_id}: bad guided generator counts")
    nf_rows = integer(controls.get("nf_generator_rows"), f"{class_id}.controls.nf_generator_rows", minimum=0)
    script_done = integer(controls.get("script_done_count"), f"{class_id}.controls.script_done_count", minimum=0)
    recomputed = bool(
        named_pass
        and not missing
        and main["accepted"]
        and main["nf_all_zero"]
        and guided_counts == [total_generators]
        and nf_rows == total_generators
        and script_done == 1
        and not singular_errors
    )
    require(type(controls.get("complete")) is bool, f"{class_id}: controls.complete is not boolean")
    require(controls["complete"] is recomputed, f"{class_id}: controls.complete does not match recomputation")
    for optional_integer in ("dimension", "basis_size", "lead_dim", "lead_vdim", "vdim"):
        value = main.get(optional_integer)
        require(value is None or type(value) is int, f"{class_id}: bad guided {optional_integer}")
    return recomputed, main


def marker_value(stdout: str, class_id: str, key: str) -> str | None:
    values = re.findall(rf"^GG__{re.escape(key)} main(?: (.*))?$", stdout, flags=re.MULTILINE)
    require(len(values) <= 1, f"{class_id}: duplicate GG__{key} markers in exact stdout")
    return values[0].strip() if values else None


def marker_integer(value: str | None) -> int | None:
    if value is None or value in {"NA", "NONTERMINATING", ""}:
        return None
    try:
        return int(value)
    except ValueError:
        return None


def reparse_exact_stdout(
    stdout: str,
    controls: Mapping[str, Any],
    class_id: str,
    total_generators: int,
) -> dict[str, Any]:
    named: dict[str, dict[str, int]] = {}
    for name in ("ring", "empty", "nonempty"):
        token = name.upper()
        named[name] = {
            "pass_count": len(re.findall(rf"^CONTROL_{token}_PASS(?:\s|$)", stdout, flags=re.MULTILINE)),
            "fail_count": len(re.findall(rf"^CONTROL_{token}_FAIL(?:\s|$)", stdout, flags=re.MULTILINE)),
        }
    require(named == controls.get("named"), f"{class_id}: exact stdout named controls differ from JSON summary")
    named_pass = all(item["pass_count"] >= 1 and item["fail_count"] == 0 for item in named.values())

    raw = {
        key: marker_value(stdout, class_id, key)
        for key in ("NF_ALL_ZERO", "UNIT", "DIM", "VDIM", "BASIS_SIZE", "LEAD_DIM", "LEAD_VDIM", "ACCEPT")
    }
    for key in ("NF_ALL_ZERO", "UNIT", "ACCEPT"):
        require(raw[key] is None or raw[key] in {"0", "1"}, f"{class_id}: malformed GG__{key} value")
    for key in ("DIM", "BASIS_SIZE", "LEAD_DIM"):
        require(raw[key] is None or re.fullmatch(r"-?\d+", raw[key]) is not None, f"{class_id}: malformed GG__{key} value")
    for key in ("VDIM", "LEAD_VDIM"):
        require(
            raw[key] is None or raw[key] == "NONTERMINATING" or re.fullmatch(r"-?\d+", raw[key]) is not None,
            f"{class_id}: malformed GG__{key} value",
        )
    missing = [key for key in ("NF_ALL_ZERO", "UNIT", "DIM", "BASIS_SIZE", "LEAD_DIM", "ACCEPT") if raw[key] is None]
    nf_rows = [(int(index), int(bit)) for index, bit in re.findall(r"^GG__NF_ZERO main (\d+) ([01])$", stdout, flags=re.MULTILINE)]
    if not nf_rows:
        missing.append("NF_ZERO")
    require(len({index for index, _ in nf_rows}) == len(nf_rows), f"{class_id}: duplicate NF row index in exact stdout")
    generator_counts = [int(value) for value in re.findall(r"^GG__GENERATOR_COUNT main (\d+)\s*$", stdout, flags=re.MULTILINE)]
    std_seconds = [int(value) for value in re.findall(r"^GG__STD_SECONDS main (\d+)\s*$", stdout, flags=re.MULTILINE)]
    script_done = stdout.count("GG__SCRIPT_DONE main 1")
    singular_errors = [line for line in stdout.splitlines() if line.lstrip().startswith("?")]
    parsed_main = {
        "accepted": raw["ACCEPT"] == "1",
        "basis_size": marker_integer(raw["BASIS_SIZE"]),
        "dimension": marker_integer(raw["DIM"]),
        "lead_dim": marker_integer(raw["LEAD_DIM"]),
        "lead_vdim": marker_integer(raw["LEAD_VDIM"]),
        "missing_markers": missing,
        "nf_all_zero": raw["NF_ALL_ZERO"] == "1",
        "unit": raw["UNIT"] == "1",
        "vdim": marker_integer(raw["VDIM"]),
    }
    summarized_main = mapping(controls.get("guided_main"), f"{class_id}.controls.guided_main")
    for key, value in parsed_main.items():
        require(summarized_main.get(key) == value, f"{class_id}: exact stdout {key} differs from JSON summary")
    require(controls.get("guided_generator_counts") == generator_counts, f"{class_id}: exact stdout generator counts differ")
    require(controls.get("nf_generator_rows") == len(nf_rows), f"{class_id}: exact stdout NF-row count differs")
    require(controls.get("std_seconds_markers") == std_seconds, f"{class_id}: exact stdout std timing markers differ")
    require(controls.get("script_done_count") == script_done, f"{class_id}: exact stdout DONE count differs")
    require(controls.get("singular_error_lines") == singular_errors[:20], f"{class_id}: exact stdout Singular errors differ")
    complete = bool(
        named_pass
        and not missing
        and parsed_main["accepted"]
        and parsed_main["nf_all_zero"]
        and generator_counts == [total_generators]
        and [index for index, _ in nf_rows] == list(range(total_generators))
        and all(bit == 1 for _, bit in nf_rows)
        and script_done == 1
        and not singular_errors
    )
    require(controls.get("complete") is complete, f"{class_id}: exact stdout completeness differs from JSON summary")
    return {"complete": complete, "main": parsed_main, "nf_rows": len(nf_rows), "generator_counts": generator_counts}


def validate_sample_point(
    result_path: Path,
    sample: Mapping[str, Any],
    class_id: str,
    total_generators: int,
    solver_unknowns: int,
) -> dict[str, Any]:
    selected = mapping(sample.get("selected"), f"{class_id}.sample_point.selected")
    require(selected.get("verified") is True, f"{class_id}: selected sample is not verified")
    require(selected.get("kind") == "exact_rational_full_assignment", f"{class_id}: sample is not an exact rational assignment")
    coordinates = mapping(selected.get("coordinates"), f"{class_id}.sample_point.coordinates")
    require(len(coordinates) == solver_unknowns, f"{class_id}: sample does not assign every solver variable")
    require("c" in coordinates and "T" in coordinates, f"{class_id}: sample lacks c or T")
    rational = re.compile(r"[+-]?\d+(?:/[1-9]\d*)?\Z")
    require(
        all(isinstance(name, str) and isinstance(value, str) and rational.fullmatch(value) for name, value in coordinates.items()),
        f"{class_id}: sample contains a non-rational coordinate literal",
    )
    require(
        selected.get("expected_residual_count_including_Tc_minus_1") == total_generators,
        f"{class_id}: sample expected-residual count mismatch",
    )
    require(selected.get("residual_count") == total_generators, f"{class_id}: sample residual count mismatch")
    run = mapping(selected.get("run"), f"{class_id}.sample_point.run")
    require(run.get("timed_out") is False and run.get("returncode") == 0, f"{class_id}: sample checker did not complete")
    stdout_artifact = verify_copied_artifact(
        result_path,
        run.get("stdout"),
        f"{class_id}.sample_point.stdout",
        required=True,
    )
    verify_copied_artifact(result_path, run.get("stderr"), f"{class_id}.sample_point.stderr", required=True)
    stdout = Path(stdout_artifact["collected_path"]).read_text(encoding="utf-8", errors="strict")
    rows = [(int(index), int(bit)) for index, bit in re.findall(r"^GI__POINT_NF_ZERO (\d+) ([01])$", stdout, flags=re.MULTILINE)]
    require([index for index, _ in rows] == list(range(total_generators)), f"{class_id}: sample checker residual indices mismatch")
    require(all(bit == 1 for _, bit in rows), f"{class_id}: sample checker has a nonzero residual")
    require(stdout.count("GI__POINT_ALL_ZERO 1") == 1, f"{class_id}: sample all-zero marker mismatch")
    require(stdout.count("GI__POINT_C_NONZERO 1") == 1, f"{class_id}: sample c-nonzero marker mismatch")
    return {
        "verified": True,
        "kind": selected["kind"],
        "coordinates": dict(coordinates),
        "residual_count": total_generators,
        "stdout": stdout_artifact,
    }


def modular_summary(result: Mapping[str, Any], class_id: str) -> dict[str, Any]:
    require(result.get("modular_policy") == "SCREEN_ONLY_NEVER_PROMOTED", f"{class_id}: modular policy mismatch")
    screen = mapping(result.get("modular_screen"), f"{class_id}.modular_screen")
    require(screen.get("schema") == "moh-gi-only-modular-screen-v1", f"{class_id}: modular screen schema mismatch")
    expected_label = "MODULAR SCREEN ONLY — NEVER A CHARACTERISTIC-ZERO KILL"
    require(screen.get("label") == expected_label, f"{class_id}: modular screen label mismatch")
    require(screen.get("promotion_allowed") is False, f"{class_id}: modular screen is not explicitly non-promotional")
    require(screen.get("characteristic") == 1073741827, f"{class_id}: unexpected modular screen characteristic")
    state = screen.get("state")
    require(state in {"FINISHED", "UNAVAILABLE"}, f"{class_id}: modular screen is not terminal")
    run = screen.get("run")
    run_summary = None
    if isinstance(run, dict):
        require(run.get("watchdog_seconds") == 600, f"{class_id}: modular watchdog is not 600 seconds")
        require(type(run.get("timed_out")) is bool, f"{class_id}: modular timeout flag is not boolean")
        require(type(run.get("returncode")) is int, f"{class_id}: modular return code is not an integer")
        modular_wall = number(run.get("elapsed_seconds"), f"{class_id}.modular.elapsed_seconds", minimum=0)
        modular_rss = integer(run.get("peak_rss_kib"), f"{class_id}.modular.peak_rss_kib", minimum=1)
        run_summary = {
            "watchdog_seconds": run.get("watchdog_seconds"),
            "timed_out": run.get("timed_out"),
            "returncode": run.get("returncode"),
            "wall_seconds": modular_wall,
            "gnu_time_elapsed": run.get("gnu_time_elapsed"),
            "peak_rss_kib": modular_rss,
            "peak_rss_source": run.get("peak_rss_source"),
        }
    require(state != "FINISHED" or run_summary is not None, f"{class_id}: FINISHED modular screen lacks run custody")
    parsed = screen.get("parsed_status") if isinstance(screen.get("parsed_status"), dict) else None
    return {
        "label": screen.get("label"),
        "state": state,
        "screen_signal": screen.get("screen_signal"),
        "characteristic": screen.get("characteristic"),
        "promotion_allowed": False,
        "public_effect": screen.get("public_effect", "none"),
        "run": run_summary,
        "parsed_status": parsed,
    }


def validate_result(
    result_path: Path,
    replicas: Sequence[Path],
    manifest: Mapping[str, Any],
) -> dict[str, Any]:
    class_id = str(manifest["class_id"])
    result = load_object(result_path)
    require(result.get("schema") == "moh-gi-only-exact-q-solve-v1", f"{class_id}: result schema mismatch")
    require(result.get("state") == "FINISHED", f"{class_id}: solve is not FINISHED")
    require(result.get("class_id") == class_id, f"{class_id}: embedded class_id mismatch")
    stem = f"{class_id}_G"
    require(result.get("canonical_stem") == stem, f"{class_id}: canonical stem mismatch")
    require(result.get("class_uniform_chart") is True, f"{class_id}: class-uniform flag is not true")
    require(result.get("one_chart_per_class_suffices") is True, f"{class_id}: one-chart sufficiency flag is not true")
    require(result.get("promotion_scope") == "EXACT_Q_ONLY", f"{class_id}: promotion scope mismatch")
    receipt = validate_verification_custody(result_path, result, class_id, stem)

    software = mapping(result.get("software"), f"{class_id}.software")
    guided_software = artifact_record(software.get("guided_gb"), f"{class_id}.software.guided_gb")
    require(
        guided_software["sha256"] == GUIDED_GB_SHA256,
        f"{class_id}: charged guided_gb.py SHA-256 mismatch",
    )
    singular_software = binary_hash_record(software.get("singular"), f"{class_id}.software.singular")
    fleet_id = None
    host_summary = result.get("host") if isinstance(result.get("host"), dict) else None
    fleet_ids = {
        path.parts[path.parts.index("fleet") + 1]
        for path in replicas
        if "fleet" in path.parts
    }
    if fleet_ids:
        require(len(fleet_ids) == 1, f"{class_id}: replicas span multiple fleet workers: {sorted(fleet_ids)}")
        fleet_id = next(iter(fleet_ids))
        require(fleet_id in LANE_WORKERS, f"{class_id}: non-lane fleet worker {fleet_id}")
        host = mapping(result.get("host"), f"{class_id}.host")
        require(host.get("hostname") == LANE_WORKERS[fleet_id], f"{class_id}: fleet ID/hostname binding mismatch")

    unknowns = integer(result.get("unknowns_without_T"), f"{class_id}.unknowns_without_T", minimum=1)
    expected_unknowns = manifest.get("unknowns_without_T", manifest.get("parameter_count"))
    require(unknowns == expected_unknowns, f"{class_id}: intrinsic unknown count mismatch")
    solver_unknowns = integer(result.get("solver_variables_with_T"), f"{class_id}.solver_variables_with_T", minimum=2)
    require(solver_unknowns == unknowns + 1, f"{class_id}: solver unknown count is not intrinsic+T")
    coefficient_generators = integer(result.get("coefficient_generators"), f"{class_id}.coefficient_generators", minimum=1)
    total_generators = integer(
        result.get("ideal_generators_including_Tc_minus_1"),
        f"{class_id}.ideal_generators_including_Tc_minus_1",
        minimum=2,
    )
    require(total_generators == coefficient_generators + 1, f"{class_id}: Tc-1 generator count mismatch")
    declared_coefficients = manifest.get("jacobian_coefficient_generator_count")
    declared_total = manifest.get("generator_count_including_inverse")
    if declared_coefficients is not None:
        require(declared_coefficients == coefficient_generators, f"{class_id}: manifest coefficient count mismatch")
    if declared_total is not None:
        require(declared_total == total_generators, f"{class_id}: manifest total-generator count mismatch")
    postemit_meta = verify_copied_artifact(
        result_path,
        result.get("meta_postemit"),
        f"{class_id}.meta_postemit",
        required=True,
    )
    postemit = load_object(Path(postemit_meta["collected_path"]))
    require(postemit.get("parameter_count") == unknowns, f"{class_id}: postemit metadata unknown count mismatch")
    postemit_coefficients = postemit.get("jacobian_coefficient_generator_count", postemit.get("generator_count"))
    require(postemit_coefficients == coefficient_generators, f"{class_id}: postemit metadata coefficient count mismatch")
    require(postemit.get("generator_count_including_inverse") == total_generators, f"{class_id}: postemit metadata total count mismatch")
    require(postemit.get("gi_only") is True, f"{class_id}: postemit metadata is not marked G_i-only")

    exact_q = mapping(result.get("exact_q"), f"{class_id}.exact_q")
    run = mapping(exact_q.get("run"), f"{class_id}.exact_q.run")
    require(run.get("watchdog_seconds") == 600, f"{class_id}: exact-Q watchdog is not 600 seconds")
    require(type(run.get("timed_out")) is bool, f"{class_id}: exact-Q timed_out is not boolean")
    require(type(run.get("returncode")) is int, f"{class_id}: exact-Q return code is not an integer")
    wall_seconds = number(run.get("elapsed_seconds"), f"{class_id}.exact_q.elapsed_seconds", minimum=0)
    peak_rss = integer(run.get("peak_rss_kib"), f"{class_id}.exact_q.peak_rss_kib", minimum=1)
    exact_stdout = verify_copied_artifact(result_path, run.get("stdout"), f"{class_id}.exact_q.stdout", required=True)
    exact_stderr = verify_copied_artifact(result_path, run.get("stderr"), f"{class_id}.exact_q.stderr", required=True)
    stdout_text = Path(exact_stdout["collected_path"]).read_text(encoding="utf-8", errors="strict")
    controls = mapping(exact_q.get("controls"), f"{class_id}.exact_q.controls")
    controls_complete, main = validate_control_summary(controls, class_id, total_generators)
    reparsed = reparse_exact_stdout(stdout_text, controls, class_id, total_generators)
    require(reparsed["complete"] is controls_complete, f"{class_id}: reparsed exact control completeness mismatch")
    exact_complete = bool(not run["timed_out"] and run["returncode"] == 0 and controls_complete)
    # Use the independently reparsed stdout controls for the public verdict.
    main = reparsed["main"]
    exact_unit = bool(exact_complete and main["unit"] is True)

    sample = result.get("sample_point")
    sample_verified = False
    sample_summary = None
    if isinstance(sample, dict):
        require(type(sample.get("verified")) is bool, f"{class_id}: sample verified flag is not boolean")
        sample_verified = sample.get("verified") is True
        if sample_verified:
            sample_summary = validate_sample_point(
                result_path,
                sample,
                class_id,
                total_generators,
                solver_unknowns,
            )
    if exact_unit:
        derived_verdict = "DEAD"
    elif exact_complete and main["unit"] is False and main.get("dimension") is not None and sample_verified:
        derived_verdict = "BASIS_FOUND"
    else:
        derived_verdict = "COMPUTE_BOUND"
    reported_verdict = result.get("verdict")
    require(reported_verdict in {"DEAD", "BASIS_FOUND", "COMPUTE_BOUND"}, f"{class_id}: invalid reported verdict")
    require(reported_verdict == derived_verdict, f"{class_id}: reported {reported_verdict} but exact controls derive {derived_verdict}")
    expected_labels = {
        "DEAD": "DEAD — EXACT-Q UNIT ON THE FULL G_i CHART",
        "BASIS_FOUND": "BASIS FOUND — NONEMPTY EXACT-Q SAMPLE POINT VERIFIED (LOUD)",
        "COMPUTE_BOUND": "COMPUTE-BOUND — NO EXACT-Q UNIT OR VERIFIED SAMPLE POINT",
    }
    require(result.get("report_label") == expected_labels[derived_verdict], f"{class_id}: report label mismatch")
    if derived_verdict == "BASIS_FOUND":
        require(result.get("dimension") == main.get("dimension"), f"{class_id}: reported dimension mismatch")

    rows = verify_copied_artifact(result_path, result.get("rows"), f"{class_id}.rows", required=True)
    guided = verify_copied_artifact(result_path, result.get("guided_script"), f"{class_id}.guided_script", required=True)
    row_header, recounted_generators = recount_rows(Path(rows["collected_path"]), class_id)
    require(recounted_generators == coefficient_generators, f"{class_id}: recounted coefficient rows differ from result")
    declared_header = mapping(result.get("rows"), f"{class_id}.rows").get("header")
    require(declared_header == row_header, f"{class_id}: coefficient-row header custody mismatch")
    extraction_custody = validate_sparse_extraction_custody(
        result_path,
        result,
        postemit,
        rows,
        class_id,
    )
    guided_text = Path(guided["collected_path"]).read_text(encoding="utf-8", errors="strict")
    require("T*c-1" in guided_text, f"{class_id}: guided script lacks Tc-1")
    require("ring R=0," in guided_text, f"{class_id}: guided script is not visibly characteristic zero")
    all_artifacts = declared_artifact_index(result_path, result)
    result_artifact = file_artifact(result_path)
    replica_artifacts = [file_artifact(path) for path in replicas]
    dispatch_artifact = None
    result_parts = result_path.parts
    if "fleet" in result_parts:
        dispatch_candidates = [parent / f"{stem}.dispatch.log" for parent in result_path.parents]
        dispatch_candidates = [path for path in dispatch_candidates if path.is_file()]
        require(len(dispatch_candidates) == 1, f"{class_id}: immutable fleet snapshot has {len(dispatch_candidates)} dispatch logs")
        dispatch_log = dispatch_candidates[0]
        dispatch_artifact = file_artifact(dispatch_log)
        require(
            dispatch_artifact["sha256"] == result_artifact["sha256"]
            and dispatch_artifact["bytes"] == result_artifact["bytes"],
            f"{class_id}: dispatch log is not byte-identical to FINISHED solve-result",
        )
    return {
        "class_id": class_id,
        "canonical_stem": stem,
        "verdict": derived_verdict,
        "verdict_detail": result.get("verdict_detail"),
        "report_label": result.get("report_label"),
        "worker": {"instance_id": fleet_id, **(dict(host_summary) if host_summary else {})},
        "coefficient_rows_extraction": extraction_custody,
        "counts": {
            "unknowns_without_T_including_c": unknowns,
            "solver_unknowns_including_T": solver_unknowns,
            "coefficient_generators": coefficient_generators,
            "ideal_generators_including_Tc_minus_1": total_generators,
        },
        "exact_q": {
            "controls_validated": True,
            "controls_complete": controls_complete,
            "exact_run_complete": exact_complete,
            "unit": main["unit"] if exact_complete else None,
            "dimension": main.get("dimension") if exact_complete else None,
            "basis_size": main.get("basis_size") if exact_complete else None,
            "watchdog_seconds": 600,
            "timed_out": run["timed_out"],
            "returncode": run["returncode"],
            "wall_seconds": wall_seconds,
            "gnu_time_elapsed": run.get("gnu_time_elapsed"),
            "peak_rss_kib": peak_rss,
            "peak_rss_source": run.get("peak_rss_source"),
            "stdout": exact_stdout,
            "stderr": exact_stderr,
        },
        "sample_point_verified": sample_verified,
        "sample_point": sample_summary,
        "modular_screen": modular_summary(result, class_id),
        "custody": {
            "selected_result": result_artifact,
            "dispatch_log_byte_identical": dispatch_artifact,
            "byte_identical_replicas": replica_artifacts,
            "rows": rows,
            "rows_recount": {"header": row_header, "nonzero_coefficient_rows": recounted_generators},
            "guided_script": guided,
            "postemit_meta": postemit_meta,
            "verification_receipt": receipt,
            "singular_binary": singular_software,
            "declared_artifacts": all_artifacts,
        },
    }


def atomic_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp-{os.getpid()}")
    try:
        with temporary.open("x", encoding="utf-8") as handle:
            json.dump(value, handle, indent=2, sort_keys=True)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass


def aggregate(bundle: Path) -> dict[str, Any]:
    bundle = bundle.resolve()
    manifest_path = bundle / "classes_manifest.json"
    _, manifest_by_id = load_manifest(manifest_path)
    selected = discover_results(bundle)
    classes = []
    for class_id in EXPECTED_CLASS_IDS:
        chosen, replicas, historical = selected[class_id]
        item = validate_result(chosen, replicas, manifest_by_id[class_id])
        item["superseded_attempts"] = historical
        classes.append(item)
    counts = {verdict: sum(item["verdict"] == verdict for item in classes) for verdict in ("DEAD", "BASIS_FOUND", "COMPUTE_BOUND")}
    lane_names = ("solve_class.py", "gi_only_emit.py", "time_singular.sh", "fleet_lane.sh")
    lane_drivers = {}
    for name in lane_names:
        path = bundle / name
        require(path.is_file(), f"lane driver is absent: {path}")
        lane_drivers[name] = file_artifact(path)
    fleet_jobs = []
    for class_id in EXPECTED_CLASS_IDS:
        path = bundle / "classes" / class_id / "jobs" / f"{class_id}_G_fleet.sh"
        require(path.is_file(), f"fleet job is absent: {path}")
        fleet_jobs.append(file_artifact(path))
    return {
        "schema": "moh-gi-only-final-solve-summary-v1",
        "status": "PASS",
        "generated_utc": utc_now(),
        "bundle_root": str(bundle),
        "class_count": len(classes),
        "all_six_finished": True,
        "all_exact_q_verdict_rules_validated": True,
        "modular_results_are_screen_only": True,
        "all_nonexception_declared_artifacts_locally_sha256_verified": True,
        "declared_only_custody_exceptions": [
            {"json_pointer": pointer, "reason": reason}
            for pointer, reason in sorted(DECLARED_ONLY_ARTIFACTS.items())
        ],
        "selection_policy": "unnumbered fleet/ID/CLASS/class snapshot is final; canonical mirror must be byte-identical; every attemptN tree is historical-only custody",
        "classes_manifest": file_artifact(manifest_path),
        "aggregation_driver": file_artifact(Path(__file__)),
        "lane_driver_artifacts": lane_drivers,
        "fleet_job_artifacts": fleet_jobs,
        "verdict_counts": counts,
        "classes": classes,
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle-root", type=Path, default=HERE, help="gi-only output bundle to inspect")
    parser.add_argument("--output", type=Path, help="summary path; defaults inside the inspected bundle")
    args = parser.parse_args(argv)
    output = (args.output or (args.bundle_root / "final-solve-summary.json")).resolve()
    try:
        summary = aggregate(args.bundle_root)
    except SummaryError as exc:
        print(f"GI_FINAL_SUMMARY_REFUSED: {exc}", file=sys.stderr)
        return 2
    atomic_json(output, summary)
    rendered = json.dumps(summary, indent=2, sort_keys=True)
    print(rendered)
    print(f"GI_FINAL_SUMMARY_WRITTEN {output}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
