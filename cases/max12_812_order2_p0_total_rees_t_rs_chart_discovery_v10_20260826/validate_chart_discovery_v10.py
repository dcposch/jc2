#!/usr/bin/env python3
"""Fail-closed validator for V10 T-rs chart discovery output."""

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
        compiler.get("status") != "PASS-T-RS-CHART-DISCOVERY-V10-COMPILER"
        or compiler.get("characteristic") != args.characteristic
        or compiler.get("prefix_grade") != args.grade
        or compiler.get("algorithm") != args.algorithm
    ):
        fail("compiler result mismatch")
    script = Path(compiler["script"])
    if digest(script) != compiler.get("script_sha256"):
        fail("compiled script hash mismatch")
    stdout = args.stdout.read_text()
    stderr = args.stderr.read_text()
    if stderr.strip():
        fail(("nonempty Singular stderr", stderr[-2000:]))
    forbidden = ("?", "FAIL_", "error occurred", "halt", "Segment fault")
    if any(token in stdout for token in forbidden):
        fail(("Singular diagnostic", [token for token in forbidden if token in stdout]))
    if stdout.count("PASS_T_RS_CHART_DISCOVERY_V10") != 1:
        fail("missing/duplicate terminal pass")
    required_text = (
        "V10_QRING_DISABLED=1",
        "V10_SYNTHETIC_SAT_CONTROLS=PASS",
        f"V10_CHARACTERISTIC={args.characteristic}",
        f"V10_PREFIX_GRADE={args.grade}",
        f"V10_ALGORITHM={args.algorithm}",
        "V10_ARTIFACT_WRITES=8",
        "V10_SCOPE=PREFIX_BASECHANGE_DISCOVERY_ONLY_NO_CHART_OR_ORDER2_VERDICT",
    )
    for token in required_text:
        if stdout.count(token) != 1:
            fail(("required stdout token", token, stdout.count(token)))
    count = 7 * (args.grade - 9)
    if marker(stdout, "V10_SOURCE_SPECIALIZATION_COUNT") != count:
        fail("source-specialization count")
    if marker(stdout, "V10_DECK_COUNT") != count:
        fail("deck count")
    expected_modular = 0 if args.characteristic == 0 else 2 * count
    if marker(stdout, "V10_MODULAR_COMPARISON_COUNT") != expected_modular:
        fail("modular comparison count")
    outcome_names = (
        "V10_AFTER_IN_BEFORE",
        "V10_BEFORE_IN_AFTER",
        "V10_BASECHANGE_EQUAL",
        "V10_NAIVE_AFTER_IN_BEFORE",
        "V10_BEFORE_IN_NAIVE_AFTER",
        "V10_NAIVE_EQUAL",
    )
    outcomes = {name: marker(stdout, name) for name in outcome_names}
    if any(value not in (0, 1) for value in outcomes.values()):
        fail(("non-Boolean outcome", outcomes))
    if outcomes["V10_BASECHANGE_EQUAL"] != (
        outcomes["V10_AFTER_IN_BEFORE"] * outcomes["V10_BEFORE_IN_AFTER"]
    ):
        fail("base-change Boolean inconsistency")
    if outcomes["V10_NAIVE_EQUAL"] != (
        outcomes["V10_NAIVE_AFTER_IN_BEFORE"]
        * outcomes["V10_BEFORE_IN_NAIVE_AFTER"]
    ):
        fail("naive Boolean inconsistency")
    artifacts: dict[str, dict[str, object]] = {}
    for name, raw_path in compiler["artifact_paths"].items():
        path = Path(raw_path)
        if not path.is_file() or path.stat().st_size == 0:
            fail(("missing/empty algebra artifact", name, path))
        artifacts[name] = {"sha256": digest(path), "bytes": path.stat().st_size}
    result = {
        "status": "PASS-T-RS-CHART-DISCOVERY-V10",
        "scope": "PREFIX_BASECHANGE_DISCOVERY_ONLY_NO_CHART_OR_ORDER2_VERDICT",
        "characteristic": args.characteristic,
        "prefix_grade": args.grade,
        "algorithm": args.algorithm,
        "basechange_equal": bool(outcomes["V10_BASECHANGE_EQUAL"]),
        "after_in_before": bool(outcomes["V10_AFTER_IN_BEFORE"]),
        "before_in_after": bool(outcomes["V10_BEFORE_IN_AFTER"]),
        "naive_equal": bool(outcomes["V10_NAIVE_EQUAL"]),
        "naive_after_in_before": bool(outcomes["V10_NAIVE_AFTER_IN_BEFORE"]),
        "before_in_naive_after": bool(outcomes["V10_BEFORE_IN_NAIVE_AFTER"]),
        "compiler_result_sha256": digest(args.compiler_result),
        "script_sha256": digest(script),
        "stdout_sha256": digest(args.stdout),
        "stderr_sha256": digest(args.stderr),
        "artifacts": artifacts,
    }
    args.output.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
