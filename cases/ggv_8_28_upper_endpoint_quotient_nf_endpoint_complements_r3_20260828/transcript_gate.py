#!/usr/bin/env python3
"""Fail closed on Singular diagnostics, including diagnostics returned with rc=0."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


STDOUT_DIAGNOSTIC = re.compile(
    r"(?:^\s*\?|error occurred|syntax error|parse error|wrong type|"
    r"wrong range|not defined|cannot open)", re.IGNORECASE)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def diagnostic_lines(stdout: Path, stderr: Path) -> list[str]:
    findings: list[str] = []
    for line_number, line in enumerate(
            stdout.read_text(errors="replace").splitlines(), 1):
        if STDOUT_DIAGNOSTIC.search(line):
            findings.append(f"stdout:{line_number}:{line}")
    for line_number, line in enumerate(
            stderr.read_text(errors="replace").splitlines(), 1):
        if line.strip():
            findings.append(f"stderr:{line_number}:{line}")
    return findings


def assert_clean_transcript(stdout: Path, stderr: Path) -> None:
    findings = diagnostic_lines(stdout, stderr)
    if findings:
        raise RuntimeError(
            "SINGULAR_DIAGNOSTIC_WITH_ANY_RETURN_CODE:"
            + " || ".join(findings[:8]))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stdout", required=True, type=Path)
    parser.add_argument("--stderr", required=True, type=Path)
    parser.add_argument("--expect", required=True,
                        choices=("clean", "diagnostic"))
    parser.add_argument("--evidence", required=True, type=Path)
    args = parser.parse_args()
    findings = diagnostic_lines(args.stdout, args.stderr)
    accepted = ((args.expect == "clean" and not findings)
                or (args.expect == "diagnostic" and bool(findings)))
    payload = {
        "accepted": accepted,
        "diagnostic_count": len(findings),
        "diagnostics": findings,
        "expect": args.expect,
        "stderr_sha256": sha256(args.stderr),
        "stdout_sha256": sha256(args.stdout),
    }
    args.evidence.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    if not accepted:
        raise SystemExit("SINGULAR_TRANSCRIPT_GATE_EXPECTATION_FAILURE")
    print(f"TRANSCRIPT_DIAGNOSTIC_COUNT={len(findings)}")
    print(f"TRANSCRIPT_EXPECTED_{args.expect.upper()}_PASS=1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

