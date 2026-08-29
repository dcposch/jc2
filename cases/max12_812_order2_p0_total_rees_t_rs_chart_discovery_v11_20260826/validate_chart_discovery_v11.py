#!/usr/bin/env python3
"""Fail-closed validator for repaired V11 T-rs chart discovery output."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path
import re


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def marker(text: str, name: str) -> int:
    hits = re.findall(rf"^{re.escape(name)}=([0-9]+)$", text, re.MULTILINE)
    if len(hits) != 1:
        fail(("marker", name, hits))
    return int(hits[0])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--job", type=Path, required=True)
    parser.add_argument("--compiler-result", type=Path, required=True)
    parser.add_argument("--stdout", type=Path, required=True)
    parser.add_argument("--stderr", type=Path, required=True)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    parser.add_argument("--grade", type=int, choices=(10, 11, 12), required=True)
    parser.add_argument("--algorithm", choices=("sat", "elim"), required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    compiler = json.loads(args.compiler_result.read_text())
    if (
        compiler.get("status") != "PASS-T-RS-CHART-DISCOVERY-V11-COMPILER"
        or compiler.get("characteristic") != args.characteristic
        or compiler.get("prefix_grade") != args.grade
        or compiler.get("algorithm") != args.algorithm
        or compiler.get("v10_compiler_sha256")
        != "6a054f7f567ca3f4ef7f360820b28b3a4fe50ae5aaa5c76bae5cd9422fc503f3"
    ):
        fail("compiler result mismatch")
    script = Path(compiler["script"])
    if digest(script) != compiler.get("script_sha256"):
        fail("compiled script hash mismatch")
    stdout = args.stdout.read_text()
    resource_stderr = args.stderr.read_text()
    if (
        resource_stderr.count("Command being timed:") != 1
        or resource_stderr.count("Exit status: 0") != 1
    ):
        fail(("invalid GNU-time resource stderr", resource_stderr[-2000:]))
    stderr_forbidden = (
        "Command terminated by signal",
        "No such file",
        "cannot execute",
        "out of memory",
        "Killed",
        "Segmentation fault",
    )
    if any(token in resource_stderr for token in stderr_forbidden):
        fail(("resource stderr failure token", [
            token for token in stderr_forbidden if token in resource_stderr
        ]))
    stdout_forbidden = ("?", "FAIL_", "error occurred", "halt", "Segment fault")
    if any(token in stdout for token in stdout_forbidden):
        fail(("Singular diagnostic", [
            token for token in stdout_forbidden if token in stdout
        ]))
    if stdout.count("PASS_T_RS_CHART_DISCOVERY_V11") != 1:
        fail("missing/duplicate terminal pass")
    required_text = (
        "V11_QRING_DISABLED=1",
        "V11_SYNTHETIC_SAT_CONTROLS=PASS",
        f"V11_CHARACTERISTIC={args.characteristic}",
        f"V11_PREFIX_GRADE={args.grade}",
        f"V11_ALGORITHM={args.algorithm}",
        "V11_ARTIFACT_WRITES=8",
        "V11_SCOPE=PREFIX_BASECHANGE_DISCOVERY_ONLY_NO_CHART_OR_ORDER2_VERDICT",
    )
    for token in required_text:
        if stdout.count(token) != 1:
            fail(("required stdout token", token, stdout.count(token)))
    if args.algorithm == "sat":
        if marker(stdout, "V11_SAT_TOTAL_RETURN_LENGTH") != 1:
            fail("total saturation return-list length")
        if marker(stdout, "V11_SAT_ZERO_RETURN_LENGTH") != 1:
            fail("zero-fibre saturation return-list length")
    count = 7 * (args.grade - 9)
    if marker(stdout, "V11_SOURCE_SPECIALIZATION_COUNT") != count:
        fail("source-specialization count")
    if marker(stdout, "V11_DECK_COUNT") != count:
        fail("deck count")
    expected_modular = 0 if args.characteristic == 0 else 2 * count
    if marker(stdout, "V11_MODULAR_COMPARISON_COUNT") != expected_modular:
        fail("modular comparison count")
    outcome_names = (
        "V11_AFTER_IN_BEFORE",
        "V11_BEFORE_IN_AFTER",
        "V11_BASECHANGE_EQUAL",
        "V11_NAIVE_AFTER_IN_BEFORE",
        "V11_BEFORE_IN_NAIVE_AFTER",
        "V11_NAIVE_EQUAL",
    )
    outcomes = {name: marker(stdout, name) for name in outcome_names}
    if any(value not in (0, 1) for value in outcomes.values()):
        fail(("non-Boolean outcome", outcomes))
    if outcomes["V11_BASECHANGE_EQUAL"] != (
        outcomes["V11_AFTER_IN_BEFORE"] * outcomes["V11_BEFORE_IN_AFTER"]
    ):
        fail("base-change Boolean inconsistency")
    if outcomes["V11_NAIVE_EQUAL"] != (
        outcomes["V11_NAIVE_AFTER_IN_BEFORE"]
        * outcomes["V11_BEFORE_IN_NAIVE_AFTER"]
    ):
        fail("naive Boolean inconsistency")
    artifacts: dict[str, dict[str, object]] = {}
    for name, raw_path in compiler["artifact_paths"].items():
        path = Path(raw_path)
        if not path.is_file() or path.stat().st_size == 0:
            fail(("missing/empty algebra artifact", name, path))
        artifacts[name] = {"sha256": digest(path), "bytes": path.stat().st_size}
    result = {
        "status": "PASS-T-RS-CHART-DISCOVERY-V11",
        "scope": "PREFIX_BASECHANGE_DISCOVERY_ONLY_NO_CHART_OR_ORDER2_VERDICT",
        "characteristic": args.characteristic,
        "prefix_grade": args.grade,
        "algorithm": args.algorithm,
        "basechange_equal": bool(outcomes["V11_BASECHANGE_EQUAL"]),
        "after_in_before": bool(outcomes["V11_AFTER_IN_BEFORE"]),
        "before_in_after": bool(outcomes["V11_BEFORE_IN_AFTER"]),
        "naive_equal": bool(outcomes["V11_NAIVE_EQUAL"]),
        "naive_after_in_before": bool(outcomes["V11_NAIVE_AFTER_IN_BEFORE"]),
        "before_in_naive_after": bool(outcomes["V11_BEFORE_IN_NAIVE_AFTER"]),
        "compiler_result_sha256": digest(args.compiler_result),
        "script_sha256": digest(script),
        "stdout_sha256": digest(args.stdout),
        "resource_stderr_sha256": digest(args.stderr),
        "artifacts": artifacts,
    }
    args.output.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
