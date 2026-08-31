#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


SCHEMA = "SEMANTIC-REPLAY/v1"
GENERATOR_PROTOCOL = f"{SCHEMA}/generator"
PATH_PROTOCOL = f"{SCHEMA}/path"
PROJECTION = "complete-results/v1"
TIMEOUT_SECONDS = 60
MAX_OUTPUT_BYTES = 8 * 1024 * 1024


class GateFailure(Exception):
    code = 2
    status = "MALFORMED"

    def __init__(self, reason: str, claim_id: str | None = None) -> None:
        super().__init__(reason)
        self.claim_id = claim_id


class Malformed(GateFailure):
    pass


class Bypass(GateFailure):
    code = 4
    status = "FAIL-BYPASS"


@dataclass(frozen=True)
class EntryPoint:
    id: str
    script: Path
    sha256: str
    args: tuple[str, ...]


@dataclass(frozen=True)
class ClaimSpec:
    id: str
    generator: EntryPoint
    production_path: EntryPoint
    accepted: dict[str, Any]
    rejected: dict[str, Any]
    mutation_id: str
    mutation_args: tuple[str, ...]
    baseline_sha256: str
    mutated_sha256: str


def _reject_constant(token: str) -> None:
    raise ValueError(f"non-finite number {token!r}")


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise ValueError(f"duplicate JSON key {key!r}")
        value[key] = item
    return value


def _loads(text: str, label: str, failure: type[GateFailure]) -> Any:
    try:
        value = json.loads(
            text,
            object_pairs_hook=_unique_object,
            parse_constant=_reject_constant,
        )
        _check_json_value(value, label, failure)
    except RecursionError as exc:
        raise failure(f"{label}: nesting too deep") from exc
    except (json.JSONDecodeError, ValueError) as exc:
        raise failure(f"{label}: invalid JSON: {exc}") from exc
    return value


def _check_json_value(
    value: Any,
    label: str,
    failure: type[GateFailure],
) -> None:
    if value is None or isinstance(value, (bool, int)):
        return
    if isinstance(value, str):
        try:
            value.encode("utf-8", errors="strict")
        except UnicodeError as exc:
            raise failure(f"{label}: string is not Unicode scalar text") from exc
        return
    if isinstance(value, float):
        raise failure(f"{label}: floating-point values are not canonical")
    if isinstance(value, list):
        for index, item in enumerate(value):
            _check_json_value(item, f"{label}[{index}]", failure)
        return
    if isinstance(value, dict):
        for key, item in value.items():
            if not isinstance(key, str):
                raise failure(f"{label}: object key is not a string")
            _check_json_value(key, f"{label}: object key", failure)
            _check_json_value(item, f"{label}.{key}", failure)
        return
    raise failure(f"{label}: unsupported JSON value {type(value).__name__}")


def _canonical(value: Any) -> bytes:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
        allow_nan=False,
    ).encode("utf-8")


def _mapping(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise Malformed(f"{label}: expected object")
    return value


def _field(mapping: dict[str, Any], key: str, label: str) -> Any:
    if key not in mapping:
        raise Malformed(f"{label}: missing {key}")
    return mapping[key]


def _string(mapping: dict[str, Any], key: str, label: str) -> str:
    value = _field(mapping, key, label)
    if not isinstance(value, str) or not value or "\0" in value:
        raise Malformed(f"{label}.{key}: expected nonempty string")
    return value


def _digest(mapping: dict[str, Any], key: str, label: str) -> str:
    value = _string(mapping, key, label)
    if len(value) != 64 or any(char not in "0123456789abcdef" for char in value):
        raise Malformed(f"{label}.{key}: expected 64 lowercase hex characters")
    return value


def _arguments(mapping: dict[str, Any], key: str, label: str) -> tuple[str, ...]:
    value = _field(mapping, key, label)
    if not isinstance(value, list):
        raise Malformed(f"{label}.{key}: expected array")
    if any(not isinstance(item, str) or "\0" in item for item in value):
        raise Malformed(f"{label}.{key}: every argument must be a string")
    return tuple(value)


def _entry_point(
    value: Any,
    label: str,
    certificate_dir: Path,
) -> EntryPoint:
    mapping = _mapping(value, label)
    entry_id = _string(mapping, "id", label)
    script_text = _string(mapping, "script", label)
    script_relative = Path(script_text)
    if script_relative.is_absolute():
        raise Malformed(f"{label}.script: expected a relative path")
    try:
        script = (certificate_dir / script_relative).resolve()
    except OSError as exc:
        raise Malformed(f"{label}.script: cannot resolve path: {exc}") from exc
    return EntryPoint(
        id=entry_id,
        script=script,
        sha256=_digest(mapping, "sha256", label),
        args=_arguments(mapping, "args", label),
    )


def _claim(
    value: Any,
    index: int,
    certificate_dir: Path,
) -> ClaimSpec:
    label = f"claims[{index}]"
    mapping = _mapping(value, label)
    claim_id = _string(mapping, "id", label)
    generator = _entry_point(
        _field(mapping, "generator", label),
        f"{label}.generator",
        certificate_dir,
    )
    production_path = _entry_point(
        _field(mapping, "production_path", label),
        f"{label}.production_path",
        certificate_dir,
    )
    projection = _string(mapping, "claim_projection", label)
    if projection != PROJECTION:
        raise Malformed(f"{label}.claim_projection: expected {PROJECTION!r}")

    witnesses = _mapping(_field(mapping, "witnesses", label), f"{label}.witnesses")
    accepted = _mapping(
        _field(witnesses, "accepted", f"{label}.witnesses"),
        f"{label}.witnesses.accepted",
    )
    rejected = _mapping(
        _field(witnesses, "rejected", f"{label}.witnesses"),
        f"{label}.witnesses.rejected",
    )
    if _canonical(accepted) == _canonical(rejected):
        raise Malformed(f"{label}.witnesses: controls must be distinct")

    mutation = _mapping(_field(mapping, "mutation", label), f"{label}.mutation")
    mutation_id = _string(mutation, "id", f"{label}.mutation")
    mutation_args = _arguments(
        mutation,
        "generator_args_append",
        f"{label}.mutation",
    )
    if not mutation_args:
        raise Malformed(
            f"{label}.mutation.generator_args_append: expected a nonempty array"
        )

    return ClaimSpec(
        id=claim_id,
        generator=generator,
        production_path=production_path,
        accepted=accepted,
        rejected=rejected,
        mutation_id=mutation_id,
        mutation_args=mutation_args,
        baseline_sha256=_digest(mapping, "baseline_claim_sha256", label),
        mutated_sha256=_digest(mutation, "claim_sha256", f"{label}.mutation"),
    )


def _certificate(path: Path) -> list[ClaimSpec]:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise Malformed(f"certificate: cannot read UTF-8 file: {exc}") from exc
    root = _mapping(_loads(text, "certificate", Malformed), "certificate")
    if _string(root, "schema", "certificate") != SCHEMA:
        raise Malformed(f"certificate.schema: expected {SCHEMA!r}")
    claims_value = _field(root, "claims", "certificate")
    if not isinstance(claims_value, list) or not claims_value:
        raise Malformed("certificate.claims: expected nonempty array")
    claims = [
        _claim(value, index, path.resolve().parent)
        for index, value in enumerate(claims_value)
    ]
    identifiers = [claim.id for claim in claims]
    if len(set(identifiers)) != len(identifiers):
        raise Malformed("certificate.claims: duplicate claim id")
    return claims


def _file_sha256(entry: EntryPoint, claim_id: str, role: str) -> str:
    try:
        if not entry.script.is_file():
            raise OSError("not a regular file")
        actual = hashlib.sha256(entry.script.read_bytes()).hexdigest()
    except OSError as exc:
        raise Bypass(
            f"{role} {entry.script}: cannot read: {exc}",
            claim_id,
        ) from exc
    if actual != entry.sha256:
        raise Bypass(
            f"{role} {entry.id}: SHA-256 mismatch",
            claim_id,
        )
    return actual


def _run(
    entry: EntryPoint,
    args: tuple[str, ...],
    stdin: str | None,
    certificate_dir: Path,
    claim: ClaimSpec,
    phase: str,
) -> dict[str, Any]:
    _file_sha256(entry, claim.id, phase)
    environment = os.environ.copy()
    for name in tuple(environment):
        if name.startswith("SEMANTIC_REPLAY_"):
            environment.pop(name)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    environment["PYTHONHASHSEED"] = "0"
    environment["SEMANTIC_REPLAY_CLAIM_ID"] = claim.id
    environment["SEMANTIC_REPLAY_GENERATOR_ID"] = claim.generator.id
    environment["SEMANTIC_REPLAY_PATH_ID"] = claim.production_path.id
    command = [sys.executable, "-B", str(entry.script), *args]
    try:
        process = subprocess.run(
            command,
            check=False,
            cwd=certificate_dir,
            env=environment,
            input=stdin,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="strict",
            timeout=TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired as exc:
        raise Bypass(f"{phase}: timed out", claim.id) from exc
    except (OSError, UnicodeError) as exc:
        raise Bypass(f"{phase}: execution failed: {exc}", claim.id) from exc
    if process.returncode != 0:
        raise Bypass(f"{phase}: exited {process.returncode}", claim.id)
    if len(process.stdout.encode("utf-8")) > MAX_OUTPUT_BYTES:
        raise Bypass(f"{phase}: stdout exceeds {MAX_OUTPUT_BYTES} bytes", claim.id)
    value = _loads(process.stdout, f"{phase} stdout", Bypass)
    if not isinstance(value, dict):
        raise Bypass(f"{phase} stdout: expected JSON object", claim.id)
    return value


def _generator_records(
    output: dict[str, Any],
    claim: ClaimSpec,
    phase: str,
) -> dict[bytes, dict[str, Any]]:
    if output.get("protocol") != GENERATOR_PROTOCOL:
        raise Bypass(f"{phase}: wrong generator protocol", claim.id)
    if output.get("generator_id") != claim.generator.id:
        raise Bypass(f"{phase}: wrong generator id", claim.id)
    records = output.get("records")
    if not isinstance(records, list):
        raise Bypass(f"{phase}: records must be an array", claim.id)
    indexed: dict[bytes, dict[str, Any]] = {}
    for index, record_value in enumerate(records):
        if not isinstance(record_value, dict):
            raise Bypass(f"{phase}: record {index} is not an object", claim.id)
        witness = record_value.get("witness")
        if not isinstance(witness, dict) or "data" not in record_value:
            raise Bypass(
                f"{phase}: record {index} needs object witness and data",
                claim.id,
            )
        key = _canonical(witness)
        if key in indexed:
            raise Bypass(f"{phase}: duplicate generated witness", claim.id)
        indexed[key] = {"witness": witness, "data": record_value["data"]}
    return indexed


def _path_results(
    output: dict[str, Any],
    claim: ClaimSpec,
    phase: str,
) -> dict[bytes, dict[str, Any]]:
    if output.get("protocol") != PATH_PROTOCOL:
        raise Bypass(f"{phase}: wrong path protocol", claim.id)
    if output.get("path_id") != claim.production_path.id:
        raise Bypass(f"{phase}: wrong production path id", claim.id)
    if output.get("claim_id") != claim.id:
        raise Bypass(f"{phase}: wrong claim id", claim.id)
    results = output.get("results")
    if not isinstance(results, list):
        raise Bypass(f"{phase}: results must be an array", claim.id)
    indexed: dict[bytes, dict[str, Any]] = {}
    for index, result in enumerate(results):
        if not isinstance(result, dict):
            raise Bypass(f"{phase}: result {index} is not an object", claim.id)
        witness = result.get("witness")
        decision = result.get("decision")
        if not isinstance(witness, dict):
            raise Bypass(f"{phase}: result {index} has no witness object", claim.id)
        if decision not in ("accept", "reject"):
            raise Bypass(f"{phase}: result {index} has invalid decision", claim.id)
        if "claim_fragment" not in result:
            raise Bypass(f"{phase}: result {index} has no claim_fragment", claim.id)
        source_sha256 = result.get("source_record_sha256")
        if (
            not isinstance(source_sha256, str)
            or len(source_sha256) != 64
            or any(char not in "0123456789abcdef" for char in source_sha256)
        ):
            raise Bypass(f"{phase}: result {index} has invalid source digest", claim.id)
        key = _canonical(witness)
        if key in indexed:
            raise Bypass(f"{phase}: duplicate path witness", claim.id)
        indexed[key] = result
    return indexed


def _check_bijection(
    records: dict[bytes, dict[str, Any]],
    results: dict[bytes, dict[str, Any]],
    claim: ClaimSpec,
    phase: str,
) -> None:
    if records.keys() != results.keys():
        missing = len(records.keys() - results.keys())
        unknown = len(results.keys() - records.keys())
        raise Bypass(
            f"{phase}: generator/path witness bijection failed "
            f"(missing={missing}, unknown={unknown})",
            claim.id,
        )
    for key, record in records.items():
        expected = hashlib.sha256(_canonical(record)).hexdigest()
        if results[key]["source_record_sha256"] != expected:
            raise Bypass(f"{phase}: source record digest mismatch", claim.id)


def _check_controls(
    records: dict[bytes, dict[str, Any]],
    results: dict[bytes, dict[str, Any]],
    claim: ClaimSpec,
    phase: str,
    baseline: bool,
) -> None:
    controls = (
        (claim.accepted, "accept", "accepted"),
        (claim.rejected, "reject", "rejected"),
    )
    for witness, expected, label in controls:
        key = _canonical(witness)
        if key not in records or key not in results:
            raise Bypass(
                f"{phase}: declared {label} witness was not produced through path",
                claim.id,
            )
        if baseline and results[key]["decision"] != expected:
            raise Bypass(
                f"{phase}: declared {label} witness has wrong decision",
                claim.id,
            )


def _claim_digest(claim: ClaimSpec, results: dict[bytes, dict[str, Any]]) -> str:
    normalized = []
    for key in sorted(results):
        result = results[key]
        normalized.append(
            {
                "witness": result["witness"],
                "decision": result["decision"],
                "claim_fragment": result["claim_fragment"],
            }
        )
    projection = {
        "claim_id": claim.id,
        "projection": PROJECTION,
        "results": normalized,
    }
    return hashlib.sha256(_canonical(projection)).hexdigest()


def _replay(
    claim: ClaimSpec,
    certificate_dir: Path,
    mutated: bool,
) -> str:
    label = "mutated" if mutated else "baseline"
    generator_args = claim.generator.args
    if mutated:
        generator_args += claim.mutation_args
    generator_output = _run(
        claim.generator,
        generator_args,
        None,
        certificate_dir,
        claim,
        f"{label} generator",
    )
    records = _generator_records(generator_output, claim, f"{label} generator")
    path_input = {
        "protocol": GENERATOR_PROTOCOL,
        "generator_id": claim.generator.id,
        "records": [records[key] for key in sorted(records)],
    }
    path_output = _run(
        claim.production_path,
        claim.production_path.args,
        _canonical(path_input).decode("utf-8"),
        certificate_dir,
        claim,
        f"{label} production path",
    )
    results = _path_results(path_output, claim, f"{label} production path")
    _check_bijection(records, results, claim, label)
    _check_controls(records, results, claim, label, baseline=not mutated)
    return _claim_digest(claim, results)


def check_certificate(path: Path) -> tuple[list[str], list[str]]:
    claims = _certificate(path)
    certificate_dir = path.resolve().parent
    invariant: list[str] = []
    checked: list[str] = []
    for claim in claims:
        baseline = _replay(claim, certificate_dir, mutated=False)
        if baseline != claim.baseline_sha256:
            raise Bypass("baseline claim digest misses commitment", claim.id)
        mutated = _replay(claim, certificate_dir, mutated=True)
        if mutated == baseline:
            invariant.append(claim.id)
        elif mutated != claim.mutated_sha256:
            raise Bypass("mutated claim digest misses commitment", claim.id)
        checked.append(claim.id)
    return checked, invariant


def _emit(status: str, **fields: Any) -> None:
    print(json.dumps({"status": status, **fields}, sort_keys=True))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="SEMANTIC-REPLAY/v1 gate")
    subparsers = parser.add_subparsers(dest="command", required=True)
    check_parser = subparsers.add_parser("check")
    check_parser.add_argument("certificate", type=Path)
    arguments = parser.parse_args(argv)

    try:
        checked, invariant = check_certificate(arguments.certificate)
    except GateFailure as exc:
        fields: dict[str, Any] = {"reason": str(exc)}
        if exc.claim_id is not None:
            fields["claim_id"] = exc.claim_id
        _emit(exc.status, **fields)
        return exc.code
    if invariant:
        _emit("FAIL-INVARIANCE", claims=invariant)
        return 3
    _emit("PASS", claims=checked)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
