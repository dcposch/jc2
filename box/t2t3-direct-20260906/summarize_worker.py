#!/usr/bin/env python3
"""Create a bounded custody summary for one T2+T3 direct-presentation chart.

The input build JSON is produced by build_direct.py or the schema-checked T2
subset-certificate builder.  Run directories are produced by
run_worker_capped.sh.  Solver logs and bases are scanned in place; they are
never copied into the summary.  Classification is deliberately fail-closed: a
solver-looking result is not promoted unless CAPRUN completed normally and
both preflight and postflight input hashes match the build JSON.  A NONUNIT T2
subset has no implication for the full direct ideal.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import sys
from typing import Any, Iterable


SCHEMA = "T2T3_DIRECT_WORKER_SUMMARY/v1"
DIRECT_BUILD_SCHEMA = "T2T3_DIRECT_BUILD/v1"
T2_CERTIFICATE_BUILD_SCHEMA = "T2T3_DIRECT_T2_CERTIFICATE/v1"
T2_FACE_SUBSET_BUILD_SCHEMA = "T2T3_DIRECT_T2_FACE_SUBSET/v1"
T2_CERTIFICATE_SELECTED_BLOCKS = (
    "source_residual", "T2_upper", "T2_face", "inverse",
)
T2_FACE_SUBSET_SELECTED_BLOCKS = (
    "source_residual", "T2_upper", "T2_face_subset", "inverse",
)
T2_CERTIFICATE_OMITTED_BLOCKS = (
    "T2_strict", "T3_recurrence", "T3_strict", "T3_face",
)
T2_CERTIFICATE_SCOPE = (
    "literal full-direct-ideal generator subset; UNIT is conclusive for the full ideal, "
    "NONUNIT is inconclusive"
)
T2_CERTIFICATE_CASE_LEDGER = {
    "99-delta2": {
        "D2": 55, "t2z": 40, "semantic_variables": 449, "source_residual": 0,
        "T2_upper": 462, "complete_T2_face_nonzero": 17,
    },
    "99-delta52": {
        "D2": 55, "t2z": 40, "semantic_variables": 447, "source_residual": 0,
        "T2_upper": 462, "complete_T2_face_nonzero": 17,
    },
    "108-free-mean": {
        "D2": 63, "t2z": 49, "semantic_variables": 507, "source_residual": 14,
        "T2_upper": 461, "complete_T2_face_nonzero": 16,
    },
}
FULL_DIRECT_CASE_LEDGER = {
    "99-delta2": {
        "semantic_variables": 449,
        "raw": {
            "T2_upper": 462, "T2_strict": 1263, "T2_face": 56,
            "T3_recurrence": 1, "T3_strict": 2539, "T3_face": 146,
            "inverse": 3,
        },
        "emitted": {
            "T2_upper": 462, "T2_strict": 1263, "T2_face": 17,
            "T3_recurrence": 1, "T3_strict": 962, "T3_face": 46,
            "inverse": 3,
        },
    },
    "99-delta52": {
        "semantic_variables": 447,
        "raw": {
            "T2_upper": 462, "T2_strict": 1263, "T2_face": 56,
            "T3_recurrence": 1, "T3_strict": 2539, "T3_face": 146,
            "inverse": 3,
        },
        "emitted": {
            "T2_upper": 462, "T2_strict": 1263, "T2_face": 17,
            "T3_recurrence": 1, "T3_strict": 962, "T3_face": 46,
            "inverse": 3,
        },
    },
    "108-free-mean": {
        "semantic_variables": 507,
        "raw": {
            "source_residual": 14, "T2_upper": 461, "T2_strict": 1128,
            "T2_face": 64, "T3_recurrence": 1, "T3_strict": 5123,
            "T3_face": 228, "inverse": 3,
        },
        "emitted": {
            "source_residual": 14, "T2_upper": 461, "T2_strict": 1128,
            "T2_face": 16, "T3_recurrence": 1, "T3_strict": 1514,
            "T3_face": 59, "inverse": 3,
        },
    },
}
MAX_JSON_BYTES = 100_000
MAX_AUX_BYTES = 5_000_000
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
F4_HEADER_RE = re.compile(r"^deg\s+sel\s+pairs\s+mat\s+density\s+new data\s+time\(rd\)")
FLOAT_TOKEN = r"(?:\d+(?:\.\d*)?|\.\d+)"
F4_FULL_RE = re.compile(
    rf"^\s*(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s*x\s*(\d+)\s+({FLOAT_TOKEN})%"
    rf"\s+(\d+)\s+new\s+(\d+)\s+zero\s+({FLOAT_TOKEN})\s*\|\s*({FLOAT_TOKEN})"
    r"\s*(?P<trailing>.*)$"
)
F4_NEWDATA_RE = re.compile(
    rf"^\s*(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s*x\s*(\d+)\s+({FLOAT_TOKEN})%"
    r"\s+(\d+)\s+new(?:\s+(\d+)\s+zero)?\s*(?P<trailing>.*)$"
)
F4_DENSITY_RE = re.compile(
    rf"^\s*(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s*x\s*(\d+)\s+({FLOAT_TOKEN})%?"
    r"\s*(?P<trailing>.*)$"
)
F4_MATRIX_RE = re.compile(
    r"^\s*(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s*x(?:\s*(\d+))?"
    r"\s*(?P<trailing>.*)$"
)
F4_SELECTED_RE = re.compile(
    r"^\s*(\d+)(?:\s+(\d+))?(?:\s+(\d+))?\s*(?P<trailing>.*)$"
)
F4_REDUCE_RE = re.compile(
    rf"^reduce final basis\s+(\d+)\s*x\s*(\d+)\s+({FLOAT_TOKEN})%"
    rf"\s+(\d+)\s+new\s+(\d+)\s+zero\s+({FLOAT_TOKEN})\s*\|\s*({FLOAT_TOKEN})"
    r"\s*(?P<trailing>.*)$"
)
F4_REDUCE_PARTIAL_RE = re.compile(
    rf"^reduce final basis\s+(\d+)\s*x\s*(\d+)\s+({FLOAT_TOKEN})%"
    r"\s+(\d+)\s+new\s+(\d+)\s+zero\s*(?P<trailing>.*)$"
)
F4_NORMAL_INTERLEAVE_RE = re.compile(
    r"^(?:-{8,}|Dimension of quotient:\s+\d+)\s*$"
)
MSOLVE_LENGTH_RE = re.compile(r"^#length of basis:\s*(\d+)\b")
MSOLVE_CHAR_RE = re.compile(r"^#field characteristic:\s*(\d+)\b")
MSOLVE_INVALID_RE = re.compile(r"^#invalid equations\s+(\d+)\s*$")
MSOLVE_EQUATIONS_RE = re.compile(r"^#equations\s+(\d+)\s*$")
MSOLVE_OVERALL_RE = re.compile(r"^msolve overall time\s+")
TIME_RSS_RE = re.compile(r"^\s*Maximum resident set size \(kbytes\):\s*(\d+)\s*$")
TIME_ELAPSED_RE = re.compile(
    r"^\s*Elapsed \(wall clock\) time \(h:mm:ss or m:ss\):\s*(\S+)\s*$"
)
LIMIT_HEADER_RE = re.compile(r"^LIMIT_KIND=RLIMIT_AS LIMIT_KIB=(\d+)\s*$")
LIMIT_PROC_RE = re.compile(
    r"^PROC_LIMIT=Max address space\s+(\d+)\s+(\d+)\s+bytes\s*$"
)
SINGULAR_MARKERS = (
    "ALL_ROWS_PARSED",
    "BEGIN_STD",
    "END_STD",
    "BEGIN_RESULT",
    "END_RESULT",
)
SINGULAR_RESULT_KEYS = ("REDUCE_ONE", "DIMENSION", "BASIS_SIZE")
SINGULAR_DIAGNOSTIC_RE = re.compile(
    r"(^\s*\?)|(error occurred in or before)|(segment(?:ation)? fault)|(fatal error)",
    re.IGNORECASE,
)


class SummaryError(RuntimeError):
    pass


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def checked_small_text(path: Path, maximum: int = MAX_AUX_BYTES) -> str:
    size = path.stat().st_size
    if size > maximum:
        raise SummaryError(f"auxiliary file exceeds {maximum} bytes: {path}")
    return path.read_text(encoding="utf-8", errors="replace")


def load_required_build(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(checked_small_text(path))
    except (OSError, json.JSONDecodeError, SummaryError) as exc:
        raise SummaryError(f"cannot read build metadata {path}: {exc}") from exc
    if not isinstance(payload, dict):
        raise SummaryError("build metadata root is not an object")
    return payload


def load_optional_json(path: Path, errors: list[str]) -> dict[str, Any] | None:
    if not path.is_file():
        errors.append(f"missing {path.name}")
        return None
    try:
        value = json.loads(checked_small_text(path))
    except (OSError, json.JSONDecodeError, SummaryError) as exc:
        errors.append(f"invalid {path.name}: {exc}")
        return None
    if not isinstance(value, dict):
        errors.append(f"invalid {path.name}: root is not an object")
        return None
    return value


def parse_key_values(path: Path, errors: list[str]) -> dict[str, str]:
    if not path.is_file():
        errors.append(f"missing {path.name}")
        return {}
    try:
        lines = checked_small_text(path).splitlines()
    except (OSError, SummaryError) as exc:
        errors.append(f"invalid {path.name}: {exc}")
        return {}
    result: dict[str, str] = {}
    duplicates: set[str] = set()
    for line in lines:
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        if key in result:
            duplicates.add(key)
        result[key] = value
    if duplicates:
        errors.append(f"duplicate custody keys: {','.join(sorted(duplicates))}")
    return result


def parse_runner_rc(path: Path, errors: list[str]) -> int | None:
    if not path.is_file():
        errors.append("missing runner.rc")
        return None
    try:
        text = checked_small_text(path, 100).strip()
        if not re.fullmatch(r"-?\d+", text):
            raise ValueError("not an integer")
        return int(text)
    except (OSError, SummaryError, ValueError) as exc:
        errors.append(f"invalid runner.rc: {exc}")
        return None


def parse_postflight(path: Path, errors: list[str]) -> dict[str, str]:
    if not path.is_file():
        errors.append("missing postflight.sha256")
        return {}
    try:
        lines = checked_small_text(path).splitlines()
    except (OSError, SummaryError) as exc:
        errors.append(f"invalid postflight.sha256: {exc}")
        return {}
    result: dict[str, str] = {}
    for line in lines:
        match = re.fullmatch(r"([0-9a-f]{64})\s+(.+)", line)
        if not match:
            errors.append("malformed postflight.sha256 line")
            continue
        digest, name = match.groups()
        if name in result and result[name] != digest:
            errors.append(f"conflicting postflight hash for {name}")
        result[name] = digest
    return result


def manifest_hash(manifest: dict[str, str], filename: str | None) -> str | None:
    if not filename:
        return None
    if filename in manifest:
        return manifest[filename]
    matches = {digest for name, digest in manifest.items() if Path(name).name == Path(filename).name}
    return next(iter(matches)) if len(matches) == 1 else None


def parse_time_file(path: Path) -> dict[str, Any]:
    result: dict[str, Any] = {
        "exists": path.is_file(), "max_rss_KiB": None, "elapsed": None,
        "current_sha256": None,
    }
    if not path.is_file():
        return result
    try:
        text = checked_small_text(path)
        result["current_sha256"] = sha256_file(path)
        for line in text.splitlines():
            match = TIME_RSS_RE.match(line)
            if match:
                result["max_rss_KiB"] = int(match.group(1))
            match = TIME_ELAPSED_RE.match(line)
            if match:
                result["elapsed"] = match.group(1)
    except (OSError, SummaryError) as exc:
        result["error"] = str(exc)
    return result


def parse_limit_file(path: Path, custody: dict[str, str], postflight: dict[str, str]) -> dict[str, Any]:
    result: dict[str, Any] = {
        "exists": path.is_file(), "current_sha256": None, "postflight_sha256": None,
        "current_matches_postflight": False, "limit_kib": None,
        "proc_soft_bytes": None, "proc_hard_bytes": None, "valid": False,
    }
    if not path.is_file():
        return result
    result["current_sha256"] = sha256_file(path)
    result["postflight_sha256"] = manifest_hash(postflight, str(path.resolve()))
    result["current_matches_postflight"] = (
        result["current_sha256"] == result["postflight_sha256"]
    )
    try:
        lines = [line for line in checked_small_text(path).splitlines() if line.strip()]
    except (OSError, SummaryError) as exc:
        result["error"] = str(exc)
        return result
    header_matches = [LIMIT_HEADER_RE.match(line) for line in lines]
    proc_matches = [LIMIT_PROC_RE.match(line) for line in lines]
    headers = [match for match in header_matches if match]
    procs = [match for match in proc_matches if match]
    if len(headers) == 1:
        result["limit_kib"] = int(headers[0].group(1))
    if len(procs) == 1:
        result["proc_soft_bytes"] = int(procs[0].group(1))
        result["proc_hard_bytes"] = int(procs[0].group(2))
    expected_kib = int(custody["limit_value"]) if custody.get("limit_value", "").isdigit() else None
    result["custody_limit_kind"] = custody.get("limit_kind")
    result["custody_limit_value"] = custody.get("limit_value")
    result["custody_limit_units"] = custody.get("limit_units")
    result["valid"] = bool(
        len(lines) == 2 and len(headers) == len(procs) == 1
        and custody.get("limit_kind") == "RLIMIT_AS"
        and custody.get("limit_units") == "KiB"
        and isinstance(expected_kib, int) and expected_kib == result["limit_kib"]
        and result["proc_soft_bytes"] == result["proc_hard_bytes"] == expected_kib * 1024
        and result["current_matches_postflight"]
    )
    return result


def basic_run(run_dir: Path) -> tuple[dict[str, Any], dict[str, str], dict[str, str]]:
    errors: list[str] = []
    if not run_dir.is_dir():
        return ({
            "provided": True,
            "path": str(run_dir.resolve()),
            "exists": False,
            "normal_completion": False,
            "errors": ["run directory does not exist"],
        }, {}, {})
    caprun = load_optional_json(run_dir / "caprun.json", errors)
    custody = parse_key_values(run_dir / "custody.txt", errors)
    postflight = parse_postflight(run_dir / "postflight.sha256", errors)
    runner_rc = parse_runner_rc(run_dir / "runner.rc", errors)
    telemetry_rc = caprun.get("runner_exit_code") if caprun else None
    child_rc = caprun.get("child_returncode") if caprun else None
    status = caprun.get("status") if caprun else None
    caprun_schema = caprun.get("schema") if caprun else None
    if runner_rc is not None and telemetry_rc is not None and runner_rc != telemetry_rc:
        errors.append("runner.rc disagrees with CAPRUN runner_exit_code")
    normal = (
        runner_rc == 0
        and telemetry_rc == 0
        and child_rc == 0
        and status == "NORMAL_EXIT"
        and caprun_schema == "CAPRUN/v1"
    )
    stdout_post = manifest_hash(postflight, str((run_dir / "solver.stdout").resolve()))
    stderr_post = manifest_hash(postflight, str((run_dir / "solver.stderr").resolve()))
    caprun_stdout_sha = (
        caprun.get("stdout", {}).get("sha256")
        if caprun and isinstance(caprun.get("stdout"), dict) else None
    )
    caprun_stderr_sha = (
        caprun.get("stderr", {}).get("sha256")
        if caprun and isinstance(caprun.get("stderr"), dict) else None
    )
    caprun_path = run_dir / "caprun.json"
    custody_path = run_dir / "custody.txt"
    caprun_post = manifest_hash(postflight, str(caprun_path.resolve()))
    custody_post = manifest_hash(postflight, str(custody_path.resolve()))
    caprun_current = sha256_file(caprun_path) if caprun_path.is_file() else None
    custody_current = sha256_file(custody_path) if custody_path.is_file() else None
    time_record = parse_time_file(run_dir / "time.txt")
    time_post = manifest_hash(postflight, str((run_dir / "time.txt").resolve()))
    time_record["postflight_sha256"] = time_post
    time_record["current_matches_postflight"] = (
        isinstance(time_record.get("current_sha256"), str)
        and time_record["current_sha256"] == time_post
    )
    result: dict[str, Any] = {
        "provided": True,
        "path": str(run_dir.resolve()),
        "exists": True,
        "normal_completion": normal,
        "runner_rc": runner_rc,
        "caprun": {
            "schema": caprun_schema,
            "status": status,
            "runner_exit_code": telemetry_rc,
            "child_returncode": child_rc,
            "child_signal": caprun.get("child_signal") if caprun else None,
            "runner_signal": caprun.get("runner_signal") if caprun else None,
            "wall_elapsed_seconds": caprun.get("wall_elapsed_seconds") if caprun else None,
            "max_observed_group_rss_bytes": caprun.get("max_observed_group_rss_bytes") if caprun else None,
            "termination_reason": (
                caprun.get("termination", {}).get("reason")
                if caprun and isinstance(caprun.get("termination"), dict)
                else None
            ),
            "cleanup_complete": (
                caprun.get("termination", {}).get("cleanup_complete")
                if caprun and isinstance(caprun.get("termination"), dict)
                else None
            ),
            "argv_sha256": caprun.get("argv_sha256") if caprun else None,
            "stdout": caprun.get("stdout") if caprun and isinstance(caprun.get("stdout"), dict) else None,
            "stderr": caprun.get("stderr") if caprun and isinstance(caprun.get("stderr"), dict) else None,
        },
        "artifact_hash_checks": {
            "stdout_caprun_matches_postflight": (
                isinstance(caprun_stdout_sha, str) and caprun_stdout_sha == stdout_post
            ),
            "stderr_caprun_matches_postflight": (
                isinstance(caprun_stderr_sha, str) and caprun_stderr_sha == stderr_post
            ),
            "stdout_postflight_sha256": stdout_post,
            "stderr_postflight_sha256": stderr_post,
            "caprun_current_sha256": caprun_current,
            "caprun_postflight_sha256": caprun_post,
            "caprun_current_matches_postflight": (
                isinstance(caprun_current, str) and caprun_current == caprun_post
            ),
            "custody_current_sha256": custody_current,
            "custody_postflight_sha256": custody_post,
            "custody_current_matches_postflight": (
                isinstance(custody_current, str) and custody_current == custody_post
            ),
        },
        "time": time_record,
        "custody": {
            key: custody.get(key)
            for key in (
                "schema", "mode", "hostname", "nproc", "TMPDIR", "input",
                "input_sha256", "solver", "solver_sha256", "wrapper_sha256",
                "caprun_sha256", "wall_seconds", "term_grace_seconds",
                "limit_kind", "limit_value", "limit_units", "argv_shellquoted",
            )
        },
        "errors": errors,
    }
    return result, custody, postflight


def input_custody(
    build: dict[str, Any], build_sha_key: str, custody: dict[str, str],
    postflight: dict[str, str],
) -> dict[str, Any]:
    expected = build.get(build_sha_key)
    preflight = custody.get("input_sha256")
    post = manifest_hash(postflight, custody.get("input"))
    expected_valid = isinstance(expected, str) and bool(SHA256_RE.fullmatch(expected))
    pre_valid = isinstance(preflight, str) and bool(SHA256_RE.fullmatch(preflight))
    post_valid = isinstance(post, str) and bool(SHA256_RE.fullmatch(post))
    return {
        "build_sha256": expected,
        "preflight_sha256": preflight,
        "postflight_sha256": post,
        "pre_post_agree": pre_valid and post_valid and preflight == post,
        "matches_build": expected_valid and pre_valid and post_valid
        and expected == preflight == post,
    }


def f4_row(degree: int, stage: str, groups: tuple[str | None, ...]) -> dict[str, Any]:
    row: dict[str, Any] = {"degree": degree, "stage": stage}
    if len(groups) > 1 and groups[1] is not None:
        row["selected"] = int(groups[1])
    if len(groups) > 2 and groups[2] is not None:
        row["pairs"] = int(groups[2])
    if stage in {"matrix", "density", "linalg", "done"}:
        row["rows"] = int(groups[3])
        row["cols"] = int(groups[4]) if groups[4] is not None else None
    if stage in {"density", "linalg", "done"} and groups[5] is not None:
        row["density_percent"] = float(groups[5])
    if stage in {"linalg", "done"}:
        row["new"] = int(groups[6])
        row["zero"] = int(groups[7]) if groups[7] is not None else None
    if stage == "done":
        row["wall_seconds"] = float(groups[8])
        row["cpu_seconds"] = float(groups[9])
    return row


def parse_f4(path: Path) -> dict[str, Any]:
    result: dict[str, Any] = {
        "log_exists": path.is_file(),
        "recognized_rows": 0,
        "completed_rows": 0,
        "max_selected_degree": None,
        "max_completed_degree": None,
        "last_row": None,
        "largest_f4_round_matrix": None,
        "largest_completed_f4_round_matrix": None,
        "largest_matrix_including_final_reduction": None,
        "reduce_final": None,
        "invalid_equations": None,
        "reported_equations": None,
        "finished_marker": False,
        "trailing_diagnostic_count": 0,
        "trailing_diagnostic_samples": [],
        "accepted_interleave_count": 0,
    }
    if not path.is_file():
        return result
    in_f4 = False
    largest_entries = -1
    largest_completed_entries = -1
    try:
        with path.open("r", encoding="utf-8", errors="replace", newline=None) as handle:
            for line_number, raw in enumerate(handle, 1):
                line = raw.rstrip("\r\n")
                stripped = line.strip()
                invalid_match = MSOLVE_INVALID_RE.match(stripped)
                if invalid_match:
                    result["invalid_equations"] = int(invalid_match.group(1))
                equations_match = MSOLVE_EQUATIONS_RE.match(stripped)
                if equations_match:
                    result["reported_equations"] = int(equations_match.group(1))
                if MSOLVE_OVERALL_RE.match(stripped):
                    result["finished_marker"] = True
                if F4_HEADER_RE.match(stripped):
                    in_f4 = True
                    continue
                reduce_match = F4_REDUCE_RE.match(stripped)
                if reduce_match:
                    groups = reduce_match.groups()
                    result["reduce_final"] = {
                        "rows": int(groups[0]), "cols": int(groups[1]),
                        "density_percent": float(groups[2]), "new": int(groups[3]),
                        "zero": int(groups[4]), "wall_seconds": float(groups[5]),
                        "cpu_seconds": float(groups[6]), "line": line_number,
                    }
                    trailing = reduce_match.group("trailing").strip()
                    if trailing:
                        result["trailing_diagnostic_count"] += 1
                        if len(result["trailing_diagnostic_samples"]) < 5:
                            result["trailing_diagnostic_samples"].append(trailing[:256])
                    in_f4 = False
                    continue
                reduce_partial_match = F4_REDUCE_PARTIAL_RE.match(stripped)
                if reduce_partial_match:
                    groups = reduce_partial_match.groups()
                    result["reduce_final"] = {
                        "rows": int(groups[0]), "cols": int(groups[1]),
                        "density_percent": float(groups[2]), "new": int(groups[3]),
                        "zero": int(groups[4]), "wall_seconds": None,
                        "cpu_seconds": None, "line": line_number,
                        "stage": "linalg",
                    }
                    trailing = reduce_partial_match.group("trailing").strip()
                    if trailing and F4_NORMAL_INTERLEAVE_RE.fullmatch(trailing):
                        result["accepted_interleave_count"] += 1
                    elif trailing:
                        result["trailing_diagnostic_count"] += 1
                        if len(result["trailing_diagnostic_samples"]) < 5:
                            result["trailing_diagnostic_samples"].append(trailing[:256])
                    in_f4 = False
                    continue
                if stripped.startswith("---------------- TIMINGS") or stripped.startswith("TIMINGS"):
                    in_f4 = False
                if not in_f4:
                    continue
                match = F4_FULL_RE.match(line)
                if match:
                    row = f4_row(int(match.group(1)), "done", match.groups())
                else:
                    row = None
                    for regex, stage in (
                        (F4_NEWDATA_RE, "linalg"),
                        (F4_DENSITY_RE, "density"),
                        (F4_MATRIX_RE, "matrix"),
                        (F4_SELECTED_RE, "selected"),
                    ):
                        match = regex.match(line)
                        if match:
                            row = f4_row(int(match.group(1)), stage, match.groups())
                            break
                if row is None:
                    continue
                trailing = match.group("trailing").strip()
                if trailing:
                    row["trailing_diagnostic"] = trailing[:256]
                    result["trailing_diagnostic_count"] += 1
                    if len(result["trailing_diagnostic_samples"]) < 5:
                        result["trailing_diagnostic_samples"].append(trailing[:256])
                row["line"] = line_number
                result["recognized_rows"] += 1
                result["last_row"] = row
                degree = row["degree"]
                old_selected = result["max_selected_degree"]
                result["max_selected_degree"] = degree if old_selected is None else max(old_selected, degree)
                if row["stage"] == "done":
                    result["completed_rows"] += 1
                    old_completed = result["max_completed_degree"]
                    result["max_completed_degree"] = degree if old_completed is None else max(old_completed, degree)
                rows, cols = row.get("rows"), row.get("cols")
                if rows is not None and cols is not None and rows * cols > largest_entries:
                    largest_entries = rows * cols
                    result["largest_f4_round_matrix"] = {
                        "rows": rows, "cols": cols, "entries": rows * cols,
                        "degree": degree, "stage": row["stage"], "line": line_number,
                    }
                if (
                    row["stage"] == "done" and rows is not None and cols is not None
                    and rows * cols > largest_completed_entries
                ):
                    largest_completed_entries = rows * cols
                    result["largest_completed_f4_round_matrix"] = {
                        "rows": rows, "cols": cols, "entries": rows * cols,
                        "degree": degree, "line": line_number,
                    }
    except OSError as exc:
        result["error"] = str(exc)
    else:
        try:
            result["current_sha256"] = sha256_file(path)
        except OSError as exc:
            result["error"] = str(exc)
    candidates: list[dict[str, Any]] = []
    if isinstance(result["largest_f4_round_matrix"], dict):
        candidates.append({"kind": "f4_round", **result["largest_f4_round_matrix"]})
    if isinstance(result["reduce_final"], dict):
        final = result["reduce_final"]
        candidates.append({
            "kind": "final_reduction", "rows": final["rows"], "cols": final["cols"],
            "entries": final["rows"] * final["cols"], "line": final["line"],
        })
    if candidates:
        result["largest_matrix_including_final_reduction"] = max(
            candidates, key=lambda item: item["entries"]
        )
    return result


def parse_msolve_basis(path: Path, variable_count: int | None = None) -> dict[str, Any]:
    result: dict[str, Any] = {
        "exists": path.is_file(), "bytes": None, "field_characteristic": None,
        "declared_basis_length": None, "structurally_complete": False,
        "classification": "MISSING", "grammar_valid": False,
    }
    if not path.is_file():
        return result
    result["bytes"] = path.stat().st_size
    compact_prefix = b""
    compact_tail = b""
    compact_count = 0
    digest = hashlib.sha256()
    grammar_state = "EXPECT_OPEN"
    grammar_error: str | None = None
    variable = bytearray()
    parsed_basis_count = 0

    def fail_grammar(message: str) -> None:
        nonlocal grammar_error
        if grammar_error is None:
            grammar_error = message

    def validate_variable() -> None:
        token = bytes(variable)
        if variable_count is None:
            return
        match = re.fullmatch(rb"v(\d+)", token)
        if not match:
            fail_grammar("non-alias variable token in basis")
        elif isinstance(variable_count, int) and not 0 <= int(match.group(1)) < variable_count:
            fail_grammar("basis variable index outside build variable order")

    def after_factor(character: int) -> None:
        nonlocal grammar_state, parsed_basis_count
        if character == ord("*"):
            grammar_state = "VAR_START"
        elif character in (ord("+"), ord("-")):
            grammar_state = "SIGNED_COEFF_START"
        elif character == ord(","):
            parsed_basis_count += 1
            grammar_state = "POLY_START"
        elif character == ord("]"):
            parsed_basis_count += 1
            grammar_state = "EXPECT_COLON"
        else:
            fail_grammar("invalid polynomial delimiter")

    def feed_grammar(character: int) -> None:
        nonlocal grammar_state, variable
        if character in b" \t\r\n":
            return
        if grammar_error is not None:
            return
        if grammar_state == "EXPECT_OPEN":
            if character == ord("["):
                grammar_state = "POLY_START"
            else:
                fail_grammar("basis body does not start with [")
        elif grammar_state == "POLY_START":
            if character in (ord("+"), ord("-")):
                grammar_state = "SIGNED_COEFF_START"
            elif ord("0") <= character <= ord("9"):
                grammar_state = "COEFF"
            else:
                fail_grammar("polynomial does not start with an integer coefficient")
        elif grammar_state == "SIGNED_COEFF_START":
            if ord("0") <= character <= ord("9"):
                grammar_state = "COEFF"
            else:
                fail_grammar("sign is not followed by an integer coefficient")
        elif grammar_state == "COEFF":
            if ord("0") <= character <= ord("9"):
                return
            if character == ord("/"):
                grammar_state = "DENOM_START"
            else:
                after_factor(character)
        elif grammar_state == "DENOM_START":
            if ord("0") <= character <= ord("9"):
                grammar_state = "DENOM"
            else:
                fail_grammar("coefficient denominator is not an integer")
        elif grammar_state == "DENOM":
            if ord("0") <= character <= ord("9"):
                return
            after_factor(character)
        elif grammar_state == "VAR_START":
            if chr(character).isalpha() or character == ord("_"):
                variable = bytearray((character,))
                grammar_state = "VAR"
            else:
                fail_grammar("monomial factor does not start with a variable")
        elif grammar_state == "VAR":
            if chr(character).isalnum() or character == ord("_"):
                if len(variable) >= 64:
                    fail_grammar("variable token is too long")
                else:
                    variable.append(character)
                return
            validate_variable()
            if character == ord("^"):
                grammar_state = "EXP_START"
            else:
                after_factor(character)
        elif grammar_state == "EXP_START":
            if ord("0") <= character <= ord("9"):
                grammar_state = "EXP"
            else:
                fail_grammar("exponent is not a nonnegative integer")
        elif grammar_state == "EXP":
            if ord("0") <= character <= ord("9"):
                return
            after_factor(character)
        elif grammar_state == "EXPECT_COLON":
            if character == ord(":"):
                grammar_state = "ENDED"
            else:
                fail_grammar("closing ] is not followed by colon")
        elif grammar_state == "ENDED":
            fail_grammar("non-whitespace data follows basis terminator")

    def consume_body(block: bytes) -> None:
        nonlocal compact_prefix, compact_tail, compact_count
        compact = re.sub(rb"\s+", b"", block)
        compact_count += len(compact)
        if len(compact_prefix) < 32:
            compact_prefix = (compact_prefix + compact)[:32]
        compact_tail = (compact_tail + compact)[-32:]
        for character in block:
            feed_grammar(character)

    try:
        with path.open("rb") as handle:
            head = handle.read(65536)
            digest.update(head)
            head_lines = head.decode("utf-8", errors="replace").splitlines()
            standard_header_count = sum(line == "#Reduced Groebner basis data" for line in head_lines)
            char_values: list[int] = []
            length_values: list[int] = []
            for line in head_lines:
                char_match = MSOLVE_CHAR_RE.match(line)
                if char_match:
                    char_values.append(int(char_match.group(1)))
                length_match = MSOLVE_LENGTH_RE.match(line)
                if length_match:
                    length_values.append(int(length_match.group(1)))
            if len(char_values) == 1:
                result["field_characteristic"] = char_values[0]
            if len(length_values) == 1:
                result["declared_basis_length"] = length_values[0]
            body_match = re.search(rb"(?m)^\[", head)
            if body_match:
                consume_body(head[body_match.start():])
            for block in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(block)
                if body_match:
                    consume_body(block)
    except OSError as exc:
        result["classification"] = "READ_ERROR"
        result["error"] = str(exc)
        return result
    result["current_sha256"] = digest.hexdigest()
    complete = compact_prefix.startswith(b"[") and compact_tail.endswith(b"]:")
    result["structurally_complete"] = complete
    result["body_characters"] = compact_count
    result["standard_header_count"] = standard_header_count
    result["field_header_count"] = len(char_values)
    result["length_header_count"] = len(length_values)
    result["parsed_basis_count"] = parsed_basis_count
    result["grammar_error"] = grammar_error
    result["grammar_valid"] = grammar_error is None and grammar_state == "ENDED"
    headers_valid = standard_header_count == 1 and len(char_values) == len(length_values) == 1
    count_matches = result["declared_basis_length"] == parsed_basis_count
    result["declared_count_matches_body"] = count_matches
    if not complete or not headers_valid or not result["grammar_valid"] or not count_matches:
        result["classification"] = "INCOMPLETE"
    elif compact_count == 4 and compact_prefix == b"[1]:" and result["declared_basis_length"] == 1:
        result["classification"] = "UNIT"
    else:
        result["classification"] = "NONUNIT"
    return result


def summarize_msolve(run_dir: Path, build: dict[str, Any]) -> dict[str, Any]:
    run, custody, postflight = basic_run(run_dir)
    input_info = input_custody(build, "msolve_file_sha256", custody, postflight)
    basis_path = run_dir / "basis.ms"
    basis = parse_msolve_basis(basis_path, build.get("solver_variable_count"))
    basis["postflight_sha256"] = manifest_hash(postflight, str(basis_path.resolve()))
    basis["current_matches_postflight"] = (
        isinstance(basis.get("current_sha256"), str)
        and basis["current_sha256"] == basis["postflight_sha256"]
    )
    limit_record = parse_limit_file(run_dir / "limit.txt", custody, postflight)
    f4_stderr = parse_f4(run_dir / "solver.stderr")
    f4_stdout = parse_f4(run_dir / "solver.stdout")
    if f4_stdout["recognized_rows"] > f4_stderr["recognized_rows"]:
        f4 = f4_stdout
        f4["source"] = "solver.stdout"
        f4["alternate_recognized_rows"] = f4_stderr["recognized_rows"]
    else:
        f4 = f4_stderr
        f4["source"] = "solver.stderr"
        f4["alternate_recognized_rows"] = f4_stdout["recognized_rows"]
    artifact_checks = run.get("artifact_hash_checks", {})
    stdout_hashes_match = (
        isinstance(f4_stdout.get("current_sha256"), str)
        and f4_stdout["current_sha256"] == artifact_checks.get("stdout_postflight_sha256")
        and artifact_checks.get("stdout_caprun_matches_postflight") is True
    )
    stderr_hashes_match = (
        isinstance(f4_stderr.get("current_sha256"), str)
        and f4_stderr["current_sha256"] == artifact_checks.get("stderr_postflight_sha256")
        and artifact_checks.get("stderr_caprun_matches_postflight") is True
    )
    f4["stdout_hashes_match"] = stdout_hashes_match
    f4["stderr_hashes_match"] = stderr_hashes_match
    invalid_values = {
        value for value in (f4_stdout.get("invalid_equations"), f4_stderr.get("invalid_equations"))
        if isinstance(value, int)
    }
    invalid_equations = next(iter(invalid_values)) if len(invalid_values) == 1 else None
    f4["invalid_equations"] = invalid_equations
    equation_values = {
        value for value in (f4_stdout.get("reported_equations"), f4_stderr.get("reported_equations"))
        if isinstance(value, int)
    }
    reported_equations = next(iter(equation_values)) if len(equation_values) == 1 else None
    expected_equations = build.get("emitted_generator_count")
    f4["reported_equations"] = reported_equations
    f4["expected_equations"] = expected_equations
    f4["equation_count_matches_build"] = (
        isinstance(expected_equations, int) and reported_equations == expected_equations
    )
    f4["finished_marker_seen"] = bool(
        f4_stdout.get("finished_marker") or f4_stderr.get("finished_marker")
    )
    expected_prime = build.get("modular_prime")
    declared_prime = basis.get("field_characteristic")
    prime_matches = isinstance(expected_prime, int) and declared_prime == expected_prime
    mode_matches = custody.get("mode") == "msolve"
    core_hashes_match = bool(
        artifact_checks.get("caprun_current_matches_postflight")
        and artifact_checks.get("custody_current_matches_postflight")
    )
    custody_fields_valid = bool(
        custody.get("schema") == "T2T3_WORKER_RUN/v1"
        and isinstance(custody.get("input"), str) and custody.get("input")
        and all(
            isinstance(custody.get(key), str) and SHA256_RE.fullmatch(custody[key])
            for key in ("input_sha256", "solver_sha256", "wrapper_sha256", "caprun_sha256")
        )
    )
    time_record = run.get("time", {})
    time_record_valid = bool(
        time_record.get("current_matches_postflight")
        and isinstance(time_record.get("max_rss_KiB"), int)
        and isinstance(time_record.get("elapsed"), str)
    )
    if not run.get("normal_completion"):
        verdict = "OPEN_INCOMPLETE_OR_CAPPED"
    elif not build_is_valid(build):
        verdict = "OPEN_INVALID_BUILD_METADATA"
    elif run.get("errors"):
        verdict = "OPEN_CUSTODY_PARSE_ERRORS"
    elif not custody_fields_valid:
        verdict = "OPEN_INVALID_CUSTODY_FIELDS"
    elif not core_hashes_match or not stdout_hashes_match or not stderr_hashes_match:
        verdict = "OPEN_RUN_ARTIFACT_CUSTODY_MISMATCH"
    elif not time_record_valid or not limit_record["valid"]:
        verdict = "OPEN_RESOURCE_TELEMETRY_CUSTODY"
    elif not mode_matches:
        verdict = "OPEN_RUN_MODE_MISMATCH"
    elif not input_info["matches_build"]:
        verdict = "OPEN_INPUT_CUSTODY_MISMATCH"
    elif not basis["current_matches_postflight"]:
        verdict = "OPEN_BASIS_CUSTODY_MISMATCH"
    elif not prime_matches:
        verdict = "OPEN_CHARACTERISTIC_MISMATCH"
    elif invalid_equations != 0:
        verdict = "OPEN_INVALID_EQUATION_TELEMETRY"
    elif reported_equations != expected_equations:
        verdict = "OPEN_PARSED_EQUATION_COUNT_MISMATCH"
    elif f4_stdout.get("trailing_diagnostic_count") or f4_stderr.get("trailing_diagnostic_count"):
        verdict = "OPEN_MSOLVE_TRAILING_DIAGNOSTIC"
    elif basis["classification"] == "UNIT":
        verdict = "MODULAR_UNIT_SIGNAL_ONLY"
    elif basis["classification"] == "NONUNIT":
        verdict = "MODULAR_NONUNIT_BASIS_SIGNAL"
    else:
        verdict = "OPEN_NO_COMPLETE_BASIS"
    run.update({
        "input_hashes": input_info,
        "basis": basis,
        "address_space_limit": limit_record,
        "f4": f4,
        "expected_modular_prime": expected_prime,
        "prime_matches_build": prime_matches,
        "mode_matches": mode_matches,
        "core_artifact_hashes_match": core_hashes_match,
        "custody_fields_valid": custody_fields_valid,
        "time_record_valid": time_record_valid,
        "verdict": verdict,
        "interpretation": "A modular result is a screen, never an exact-Q certificate.",
    })
    return run


def parse_singular_output(path: Path) -> dict[str, Any]:
    marker_counts = {marker: 0 for marker in SINGULAR_MARKERS}
    marker_lines: dict[str, int | None] = {marker: None for marker in SINGULAR_MARKERS}
    values: dict[str, list[str]] = {key: [] for key in SINGULAR_RESULT_KEYS}
    result: dict[str, Any] = {
        "exists": path.is_file(), "bytes": None,
        "marker_counts": marker_counts, "marker_lines": marker_lines,
        "ordered_complete_markers": False, "result": {}, "classification": "MISSING",
    }
    if not path.is_file():
        return result
    result["bytes"] = path.stat().st_size
    in_result = False
    digest = hashlib.sha256()
    diagnostic_count = 0
    diagnostic_samples: list[str] = []
    unexpected_count = 0
    unexpected_samples: list[str] = []
    try:
        with path.open("rb") as handle:
            for line_number, raw in enumerate(handle, 1):
                digest.update(raw)
                line = raw.decode("utf-8", errors="replace").strip()
                if SINGULAR_DIAGNOSTIC_RE.search(line):
                    diagnostic_count += 1
                    if len(diagnostic_samples) < 5:
                        diagnostic_samples.append(line[:256])
                if line in marker_counts:
                    marker_counts[line] += 1
                    if marker_lines[line] is None:
                        marker_lines[line] = line_number
                    if line == "BEGIN_RESULT":
                        in_result = True
                    elif line == "END_RESULT":
                        in_result = False
                    continue
                recognized_result = False
                if in_result:
                    for key in SINGULAR_RESULT_KEYS:
                        prefix = key + "="
                        if line.startswith(prefix):
                            values[key].append(line[len(prefix):][:256])
                            recognized_result = True
                            break
                if line and not recognized_result:
                    unexpected_count += 1
                    if len(unexpected_samples) < 5:
                        unexpected_samples.append(line[:256])
    except OSError as exc:
        result["classification"] = "READ_ERROR"
        result["error"] = str(exc)
        return result
    result["current_sha256"] = digest.hexdigest()
    result["diagnostic_count"] = diagnostic_count
    result["diagnostic_samples"] = diagnostic_samples
    result["unexpected_line_count"] = unexpected_count
    result["unexpected_line_samples"] = unexpected_samples
    unique_markers = all(marker_counts[marker] == 1 for marker in SINGULAR_MARKERS)
    positions = [marker_lines[marker] for marker in SINGULAR_MARKERS]
    ordered = unique_markers and all(
        isinstance(positions[i], int) and isinstance(positions[i + 1], int)
        and positions[i] < positions[i + 1]
        for i in range(len(positions) - 1)
    )
    result["ordered_complete_markers"] = ordered
    unique_values = all(len(values[key]) == 1 for key in SINGULAR_RESULT_KEYS)
    parsed = {key: values[key][0] if len(values[key]) == 1 else None for key in SINGULAR_RESULT_KEYS}
    for key in ("DIMENSION", "BASIS_SIZE"):
        raw_value = parsed[key]
        if raw_value is not None and re.fullmatch(r"-?\d+", raw_value):
            parsed[key] = int(raw_value)
    result["result"] = parsed
    if not ordered or not unique_values:
        result["classification"] = "INCOMPLETE_OR_AMBIGUOUS"
    elif parsed["REDUCE_ONE"] == "0" and parsed["DIMENSION"] == -1 and parsed["BASIS_SIZE"] == 1:
        result["classification"] = "UNIT"
    elif (
        parsed["REDUCE_ONE"] == "1"
        and isinstance(parsed["DIMENSION"], int) and parsed["DIMENSION"] >= 0
        and isinstance(parsed["BASIS_SIZE"], int) and parsed["BASIS_SIZE"] >= 1
    ):
        result["classification"] = "NONUNIT"
    else:
        result["classification"] = "INCONSISTENT"
    return result


def scan_nonempty_file(path: Path) -> dict[str, Any]:
    result: dict[str, Any] = {
        "exists": path.is_file(), "bytes": None, "current_sha256": None,
        "nonempty_line_count": 0, "samples": [],
    }
    if not path.is_file():
        return result
    result["bytes"] = path.stat().st_size
    digest = hashlib.sha256()
    try:
        with path.open("rb") as handle:
            for raw in handle:
                digest.update(raw)
                if raw.strip():
                    result["nonempty_line_count"] += 1
                    if len(result["samples"]) < 5:
                        result["samples"].append(raw.decode("utf-8", errors="replace").strip()[:256])
    except OSError as exc:
        result["error"] = str(exc)
    else:
        result["current_sha256"] = digest.hexdigest()
    return result


def summarize_singular(run_dir: Path, build: dict[str, Any]) -> dict[str, Any]:
    run, custody, postflight = basic_run(run_dir)
    input_info = input_custody(build, "singular_file_sha256", custody, postflight)
    output = parse_singular_output(run_dir / "solver.stdout")
    stderr_path = run_dir / "solver.stderr"
    stderr_scan = scan_nonempty_file(stderr_path)
    stderr_record = None
    caprun_stderr = run.get("caprun", {}).get("stderr")
    if isinstance(caprun_stderr, dict):
        stderr_record = caprun_stderr
    caprun_stdout = run.get("caprun", {}).get("stdout")
    caprun_stdout_sha = caprun_stdout.get("sha256") if isinstance(caprun_stdout, dict) else None
    stdout_post_sha = run.get("artifact_hash_checks", {}).get("stdout_postflight_sha256")
    stderr_post_sha = run.get("artifact_hash_checks", {}).get("stderr_postflight_sha256")
    output_hashes_match = (
        isinstance(output.get("current_sha256"), str)
        and output["current_sha256"] == caprun_stdout_sha == stdout_post_sha
    )
    caprun_stderr_sha = stderr_record.get("sha256") if isinstance(stderr_record, dict) else None
    stderr_hashes_match = (
        isinstance(stderr_scan.get("current_sha256"), str)
        and stderr_scan["current_sha256"] == caprun_stderr_sha == stderr_post_sha
    )
    mode_matches = custody.get("mode") == "singular"
    artifact_checks = run.get("artifact_hash_checks", {})
    core_hashes_match = bool(
        artifact_checks.get("caprun_current_matches_postflight")
        and artifact_checks.get("custody_current_matches_postflight")
    )
    custody_fields_valid = bool(
        custody.get("schema") == "T2T3_WORKER_RUN/v1"
        and isinstance(custody.get("input"), str) and custody.get("input")
        and all(
            isinstance(custody.get(key), str) and SHA256_RE.fullmatch(custody[key])
            for key in ("input_sha256", "solver_sha256", "wrapper_sha256", "caprun_sha256")
        )
    )
    solver_diagnostic = bool(
        output.get("diagnostic_count")
        or output.get("unexpected_line_count")
        or stderr_scan.get("nonempty_line_count")
        or output.get("error") or stderr_scan.get("error")
    )
    time_record = run.get("time", {})
    time_record_valid = bool(
        time_record.get("current_matches_postflight")
        and isinstance(time_record.get("max_rss_KiB"), int)
        and isinstance(time_record.get("elapsed"), str)
    )
    if not run.get("normal_completion"):
        verdict = "OPEN_INCOMPLETE_OR_CAPPED"
    elif not build_is_valid(build):
        verdict = "OPEN_INVALID_BUILD_METADATA"
    elif run.get("errors"):
        verdict = "OPEN_CUSTODY_PARSE_ERRORS"
    elif not custody_fields_valid:
        verdict = "OPEN_INVALID_CUSTODY_FIELDS"
    elif not core_hashes_match or not output_hashes_match or not stderr_hashes_match:
        verdict = "OPEN_RUN_ARTIFACT_CUSTODY_MISMATCH"
    elif not time_record_valid:
        verdict = "OPEN_RESOURCE_TELEMETRY_CUSTODY"
    elif not mode_matches:
        verdict = "OPEN_RUN_MODE_MISMATCH"
    elif not input_info["matches_build"]:
        verdict = "OPEN_INPUT_CUSTODY_MISMATCH"
    elif solver_diagnostic:
        verdict = "OPEN_SOLVER_DIAGNOSTIC"
    elif output["classification"] == "UNIT":
        verdict = "EXACT_Q_UNIT"
    elif output["classification"] == "NONUNIT":
        verdict = "EXACT_Q_NONUNIT_BASIS"
    else:
        verdict = "OPEN_NO_VALID_RESULT_BLOCK"
    run.update({
        "input_hashes": input_info,
        "mode_matches": mode_matches,
        "core_artifact_hashes_match": core_hashes_match,
        "custody_fields_valid": custody_fields_valid,
        "time_record_valid": time_record_valid,
        "result_output_hashes_match": output_hashes_match,
        "markers_and_result": output,
        "stderr": {
            "exists": stderr_path.is_file(),
            "bytes": stderr_path.stat().st_size if stderr_path.is_file() else None,
            "caprun_record": stderr_record,
            "scan": stderr_scan,
            "hashes_match": stderr_hashes_match,
        },
        "solver_diagnostic": solver_diagnostic,
        "verdict": verdict,
    })
    return run


def absent_run() -> dict[str, Any]:
    return {"provided": False, "verdict": "NOT_RUN"}


def valid_sha256(value: Any) -> bool:
    return isinstance(value, str) and bool(SHA256_RE.fullmatch(value))


def count_map_is_valid(value: Any, allowed_blocks: set[str]) -> bool:
    return (
        isinstance(value, dict)
        and set(value) <= allowed_blocks
        and all(type(count) is int and count >= 0 for count in value.values())
    )


def build_kind(build: dict[str, Any]) -> str:
    schema = build.get("schema")
    if schema == DIRECT_BUILD_SCHEMA:
        return "FULL_DIRECT_PRESENTATION"
    if schema == T2_CERTIFICATE_BUILD_SCHEMA:
        return "T2_SUBSET_UNIT_CERTIFICATE"
    if schema == T2_FACE_SUBSET_BUILD_SCHEMA:
        return "T2_FACE_SUBSET_UNIT_CERTIFICATE"
    return "UNKNOWN"


def selected_face_indices_are_valid(build: dict[str, Any]) -> bool:
    indices = build.get("selected_T2_face_indices")
    case = build.get("case")
    case_ledger = T2_CERTIFICATE_CASE_LEDGER.get(case) if isinstance(case, str) else None
    d2 = case_ledger.get("D2") if isinstance(case_ledger, dict) else None
    return bool(
        isinstance(indices, list)
        and indices
        and type(d2) is int
        and all(type(index) is int for index in indices)
        and indices == sorted(indices)
        and len(indices) == len(set(indices))
        and all(0 <= index <= d2 for index in indices)
        and len(indices) < d2 + 1
    )


def guaranteed_nonzero_selected_face_count(build: dict[str, Any]) -> int | None:
    case = build.get("case")
    expected = T2_CERTIFICATE_CASE_LEDGER.get(case) if isinstance(case, str) else None
    indices = build.get("selected_T2_face_indices")
    if (
        not isinstance(expected, dict) or not isinstance(indices, list)
        or not all(type(index) is int for index in indices)
    ):
        return None
    return sum(expected["t2z"] <= index <= expected["D2"] for index in indices)


def fixed_certificate_ledger_is_valid(
    build: dict[str, Any], raw: dict[str, Any], emitted: dict[str, Any],
) -> bool:
    case = build.get("case")
    expected = T2_CERTIFICATE_CASE_LEDGER.get(case) if isinstance(case, str) else None
    if not isinstance(expected, dict):
        return False
    mandatory = {
        "source_residual": expected["source_residual"],
        "T2_upper": expected["T2_upper"],
        "inverse": 3,
    }
    if not all(
        raw.get(block, 0) == count and emitted.get(block, 0) == count
        for block, count in mandatory.items()
    ):
        return False
    if (
        build.get("modular_prime") != 1073741827
        or build.get("semantic_variable_count") != expected["semantic_variables"]
        or build.get("solver_variable_count") != expected["semantic_variables"]
    ):
        return False
    if build.get("schema") == T2_CERTIFICATE_BUILD_SCHEMA:
        full_face_raw = expected["D2"] + 1
        full_face_nonzero = expected["complete_T2_face_nonzero"]
        return bool(
            raw.get("T2_face", 0) == full_face_raw
            and emitted.get("T2_face", 0) == full_face_nonzero
        )
    return emitted.get("T2_face", 0) <= expected["complete_T2_face_nonzero"]


def full_direct_build_is_valid(build: dict[str, Any], common_valid: bool) -> bool:
    case = build.get("case")
    expected = FULL_DIRECT_CASE_LEDGER.get(case) if isinstance(case, str) else None
    if not common_valid or not isinstance(expected, dict):
        return False
    expected_raw = expected["raw"]
    expected_emitted = expected["emitted"]
    expected_zero = {
        block: count - expected_emitted.get(block, 0)
        for block, count in expected_raw.items()
        if count != expected_emitted.get(block, 0)
    }
    full_hashes = (
        build.get("input_sha256"),
        build.get("driver_sha256"),
        build.get("semantic_variable_order_sha256"),
        build.get("alias_order_sha256"),
        build.get("raw_row_labels_sha256"),
        build.get("emitted_row_labels_sha256"),
        build.get("original_name_generator_text_sha256"),
        build.get("labels_file_sha256"),
        build.get("variable_map_sha256"),
    )
    order = build.get("order")
    certificate_discriminators = (
        "classification_scope", "selected_blocks", "omitted_blocks",
        "selected_T2_face_indices", "complete_T2_face",
        "shared_emitter_driver_sha256",
    )
    return bool(
        build.get("modular_prime") == 1073741827
        and build.get("semantic_variable_count") == expected["semantic_variables"]
        and build.get("solver_variable_count") == expected["semantic_variables"]
        and build.get("graph_variables_emitted") == 0
        and build.get("constraint_variables_pivoted") == 0
        and build.get("raw_row_counts") == expected_raw
        and build.get("emitted_nonzero_counts") == expected_emitted
        and build.get("identically_zero_after_substitution") == expected_zero
        and build.get("emitted_generator_count") == sum(expected_emitted.values())
        and build.get("no_Jacobian_variable_or_tail_rows") is True
        and build.get("primitive_integer_rows") is True
        and not any(key in build for key in certificate_discriminators)
        and all(valid_sha256(value) for value in full_hashes)
        and isinstance(order, dict)
        and all(
            valid_sha256(order.get(key))
            for key in ("matrix_flat_sha256", "site_r_sha256", "site_z_sha256")
        )
    )


def build_is_valid(build: dict[str, Any]) -> bool:
    required_hashes = (
        build.get("canonical_primitive_generator_sequence_sha256"),
        build.get("singular_file_sha256"),
        build.get("msolve_file_sha256"),
        build.get("solver_variable_order_sha256"),
    )
    common_valid = (
        build.get("status") == "EMITTED_EXACT_Q_AND_MODULAR_NOT_RUN"
        and build.get("field") == "Q"
        and all(valid_sha256(value) for value in required_hashes)
    )
    schema = build.get("schema")
    if schema == DIRECT_BUILD_SCHEMA:
        return full_direct_build_is_valid(build, common_valid)
    if schema not in {T2_CERTIFICATE_BUILD_SCHEMA, T2_FACE_SUBSET_BUILD_SCHEMA} or not common_valid:
        return False

    selected = build.get("selected_blocks")
    omitted = build.get("omitted_blocks")
    allowed = set(T2_CERTIFICATE_SELECTED_BLOCKS)
    emitted = build.get("emitted_nonzero_counts")
    raw = build.get("raw_row_counts")
    zero = build.get("identically_zero_after_substitution")
    emitted_total = build.get("emitted_generator_count")
    certificate_hashes = (
        build.get("input_sha256"),
        build.get("driver_sha256"),
        build.get("shared_emitter_driver_sha256"),
        build.get("semantic_variable_order_sha256"),
        build.get("alias_order_sha256"),
        build.get("raw_row_labels_sha256"),
        build.get("emitted_row_labels_sha256"),
        build.get("original_name_generator_text_sha256"),
        build.get("labels_file_sha256"),
        build.get("variable_map_sha256"),
    )
    order = build.get("order")
    expected_selected = (
        T2_FACE_SUBSET_SELECTED_BLOCKS
        if schema == T2_FACE_SUBSET_BUILD_SCHEMA
        else T2_CERTIFICATE_SELECTED_BLOCKS
    )
    certificate_common_valid = bool(
        selected == list(expected_selected)
        and omitted == list(T2_CERTIFICATE_OMITTED_BLOCKS)
        and build.get("classification_scope") == T2_CERTIFICATE_SCOPE
        and build.get("graph_variables_emitted") == 0
        and build.get("constraint_variables_pivoted") == 0
        and type(build.get("modular_prime")) is int
        and build["modular_prime"] > 2
        and type(build.get("semantic_variable_count")) is int
        and build["semantic_variable_count"] > 0
        and build.get("solver_variable_count") == build["semantic_variable_count"]
        and type(emitted_total) is int and emitted_total > 0
        and count_map_is_valid(emitted, allowed)
        and sum(emitted.values()) == emitted_total
        and emitted.get("inverse") == 3
        and count_map_is_valid(raw, allowed)
        and count_map_is_valid(zero, allowed)
        and all(
            raw.get(block, 0) == emitted.get(block, 0) + zero.get(block, 0)
            for block in allowed
        )
        and fixed_certificate_ledger_is_valid(build, raw, emitted)
        and all(valid_sha256(value) for value in certificate_hashes)
        and isinstance(order, dict)
        and valid_sha256(order.get("matrix_flat_sha256"))
    )
    if schema == T2_CERTIFICATE_BUILD_SCHEMA:
        return certificate_common_valid
    guaranteed_nonzero = guaranteed_nonzero_selected_face_count(build)
    return bool(
        certificate_common_valid
        and build.get("complete_T2_face") is False
        and selected_face_indices_are_valid(build)
        and raw.get("T2_face", 0) == len(build["selected_T2_face_indices"])
        and type(guaranteed_nonzero) is int
        and emitted.get("T2_face", 0) >= guaranteed_nonzero
    )


def build_record(path: Path, build: dict[str, Any]) -> dict[str, Any]:
    order = build.get("order") if isinstance(build.get("order"), dict) else {}
    return {
        "path": str(path.resolve()),
        "bytes": path.stat().st_size,
        "sha256": sha256_file(path),
        "schema": build.get("schema"),
        "kind": build_kind(build),
        "status": build.get("status"),
        "valid": build_is_valid(build),
        "classification_scope": build.get("classification_scope"),
        "selected_blocks": build.get("selected_blocks"),
        "omitted_blocks": build.get("omitted_blocks"),
        "selected_T2_face_indices": build.get("selected_T2_face_indices"),
        "complete_T2_face": build.get("complete_T2_face"),
        "case": build.get("case"),
        "field": build.get("field"),
        "modular_prime": build.get("modular_prime"),
        "source_input": build.get("input"),
        "source_input_sha256": build.get("input_sha256"),
        "driver_sha256": build.get("driver_sha256"),
        "shared_emitter_driver_sha256": build.get("shared_emitter_driver_sha256"),
        "semantic_variable_count": build.get("semantic_variable_count"),
        "solver_variable_count": build.get("solver_variable_count"),
        "emitted_generator_count": build.get("emitted_generator_count"),
        "canonical_primitive_generator_sequence_sha256": build.get(
            "canonical_primitive_generator_sequence_sha256"
        ),
        "original_name_generator_text_sha256": build.get(
            "original_name_generator_text_sha256"
        ),
        "raw_row_labels_sha256": build.get("raw_row_labels_sha256"),
        "emitted_row_labels_sha256": build.get("emitted_row_labels_sha256"),
        "variable_map_file": build.get("variable_map_file"),
        "variable_map_sha256": build.get("variable_map_sha256"),
        "labels_file": build.get("labels_file"),
        "labels_file_sha256": build.get("labels_file_sha256"),
        "singular_file": build.get("singular_file"),
        "singular_file_bytes": build.get("singular_file_bytes"),
        "singular_file_sha256": build.get("singular_file_sha256"),
        "msolve_file": build.get("msolve_file"),
        "msolve_file_bytes": build.get("msolve_file_bytes"),
        "msolve_file_sha256": build.get("msolve_file_sha256"),
        "solver_variable_order_sha256": build.get("solver_variable_order_sha256"),
        "order": {
            "singular": order.get("singular"),
            "matrix_flat_sha256": order.get("matrix_flat_sha256"),
            "site_r_sha256": order.get("site_r_sha256"),
            "site_z_sha256": order.get("site_z_sha256"),
        },
    }


def combined_verdict(
    msolve: dict[str, Any], singular: dict[str, Any],
    build: dict[str, Any] | None = None,
) -> str:
    modular = msolve.get("verdict")
    exact = singular.get("verdict")
    if build is not None and not build_is_valid(build):
        return "OPEN_INVALID_BUILD_METADATA"
    kind = build_kind(build or {})
    if kind == "T2_FACE_SUBSET_UNIT_CERTIFICATE":
        if exact == "EXACT_Q_UNIT" and modular == "MODULAR_UNIT_SIGNAL_ONLY":
            return "EXACT_Q_T2_FACE_SUBSET_UNIT_CERTIFIES_FULL_DIRECT_IDEAL_AFTER_MODULAR_SIGNAL"
        if exact == "EXACT_Q_UNIT":
            return "EXACT_Q_T2_FACE_SUBSET_UNIT_CERTIFIES_FULL_DIRECT_IDEAL"
        if exact == "EXACT_Q_NONUNIT_BASIS" or modular == "MODULAR_NONUNIT_BASIS_SIGNAL":
            return "OPEN_T2_FACE_SUBSET_NONUNIT_INCONCLUSIVE_FOR_FULL_DIRECT_IDEAL"
        if modular == "MODULAR_UNIT_SIGNAL_ONLY":
            return "OPEN_MODULAR_T2_FACE_SUBSET_UNIT_SIGNAL_ONLY"
        return "OPEN"
    if kind == "T2_SUBSET_UNIT_CERTIFICATE":
        if exact == "EXACT_Q_UNIT" and modular == "MODULAR_UNIT_SIGNAL_ONLY":
            return "EXACT_Q_T2_SUBSET_UNIT_CERTIFIES_FULL_DIRECT_IDEAL_AFTER_MODULAR_SIGNAL"
        if exact == "EXACT_Q_UNIT":
            return "EXACT_Q_T2_SUBSET_UNIT_CERTIFIES_FULL_DIRECT_IDEAL"
        if exact == "EXACT_Q_NONUNIT_BASIS" or modular == "MODULAR_NONUNIT_BASIS_SIGNAL":
            return "OPEN_T2_SUBSET_NONUNIT_INCONCLUSIVE_FOR_FULL_DIRECT_IDEAL"
        if modular == "MODULAR_UNIT_SIGNAL_ONLY":
            return "OPEN_MODULAR_T2_SUBSET_UNIT_SIGNAL_ONLY"
        return "OPEN"
    if exact == "EXACT_Q_UNIT" and modular == "MODULAR_UNIT_SIGNAL_ONLY":
        return "EXACT_Q_UNIT_CONFIRMED_AFTER_MODULAR_SIGNAL"
    if exact == "EXACT_Q_UNIT":
        return "EXACT_Q_UNIT"
    if exact == "EXACT_Q_NONUNIT_BASIS":
        return "EXACT_Q_NONUNIT_BASIS_REQUIRES_SAMPLE_POINT_REPORT"
    if modular == "MODULAR_UNIT_SIGNAL_ONLY":
        return "OPEN_MODULAR_UNIT_SIGNAL_ONLY"
    return "OPEN"


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("--build-meta", required=True)
    result.add_argument("--msolve-run")
    result.add_argument("--singular-run")
    result.add_argument("--output", required=True)
    result.add_argument("--overwrite", action="store_true")
    return result


def main(argv: Iterable[str] | None = None) -> int:
    args = parser().parse_args(argv)
    build_path = Path(args.build_meta).resolve()
    output_path = Path(args.output).resolve()
    if output_path.exists() and not args.overwrite:
        raise SummaryError(f"output exists (use --overwrite): {output_path}")
    build = load_required_build(build_path)
    msolve = summarize_msolve(Path(args.msolve_run).resolve(), build) if args.msolve_run else absent_run()
    singular = summarize_singular(Path(args.singular_run).resolve(), build) if args.singular_run else absent_run()
    msolve_input_match = bool(msolve.get("input_hashes", {}).get("matches_build"))
    singular_input_match = bool(singular.get("input_hashes", {}).get("matches_build"))
    payload = {
        "schema": SCHEMA,
        "created_utc": utc_now(),
        "build": build_record(build_path, build),
        "msolve": msolve,
        "singular": singular,
        "generator_custody": {
            "build_metadata_valid": build_is_valid(build),
            "canonical_primitive_generator_sequence_sha256": build.get(
                "canonical_primitive_generator_sequence_sha256"
            ),
            "msolve_input_matches_build": msolve_input_match,
            "singular_input_matches_build": singular_input_match,
            "both_solver_inputs_match_build": msolve_input_match and singular_input_match,
        },
        "combined_verdict": combined_verdict(msolve, singular, build),
        "guardrails": {
            "modular_unit_is_signal_only": True,
            "exact_Q_requires_identical_generator_custody": True,
            "nonunit_basis_is_not_a_sample_point": True,
            "necessary_chart_survivor_is_not_a_Keller_pair": True,
            "certificate_nonunit_has_no_force_for_full_ideal": True,
        },
    }
    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")
    if len(encoded) > MAX_JSON_BYTES:
        raise SummaryError(f"summary would exceed {MAX_JSON_BYTES} bytes")
    if not output_path.parent.is_dir():
        raise SummaryError(f"output parent does not exist: {output_path.parent}")
    temporary = output_path.with_name(output_path.name + ".tmp")
    if temporary.exists():
        raise SummaryError(f"temporary output exists: {temporary}")
    with temporary.open("xb") as handle:
        handle.write(encoded)
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(temporary, output_path)
    print(f"{SCHEMA} bytes={len(encoded)} output={output_path}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SummaryError as exc:
        print(f"summarize_worker: {exc}", file=sys.stderr)
        sys.exit(2)
