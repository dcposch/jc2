#!/usr/bin/env python3
"""Validate declared charge_basis lines; never infer charge semantics from prose."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path
import re
import sys


PREFIX = "charge_basis="
BRANCHES = {"q=1-exact", "q>=2", "multi-flag"}
FRACTION = re.compile(r"[+-]?[0-9]+(?:/[+-]?[0-9]+)?\Z")
REQUIRED = {"delta", "branch", "flag_count", "citation"}


class InvalidBasis(ValueError):
    pass


def unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise InvalidBasis(f"duplicate JSON key {key!r}")
        result[key] = value
    return result


def validate(payload: str, line_number: int) -> Fraction:
    try:
        record = json.loads(payload, object_pairs_hook=unique_object)
    except (json.JSONDecodeError, InvalidBasis) as exc:
        raise InvalidBasis(f"line {line_number}: invalid JSON: {exc}") from exc
    if not isinstance(record, dict):
        raise InvalidBasis(f"line {line_number}: charge_basis must be a JSON object")

    missing = sorted(REQUIRED - record.keys())
    if missing:
        raise InvalidBasis(
            f"line {line_number}: missing required field(s): {', '.join(missing)}"
        )

    delta_text = record["delta"]
    if not isinstance(delta_text, str) or FRACTION.fullmatch(delta_text) is None:
        raise InvalidBasis(f"line {line_number}: delta must be an exact integer/fraction string")
    try:
        delta = Fraction(delta_text)
    except (ValueError, ZeroDivisionError) as exc:
        raise InvalidBasis(f"line {line_number}: invalid exact delta: {exc}") from exc

    branch = record["branch"]
    if not isinstance(branch, str) or branch not in BRANCHES:
        raise InvalidBasis(f"line {line_number}: branch must be one of {sorted(BRANCHES)}")
    flag_count = record["flag_count"]
    if isinstance(flag_count, bool) or not isinstance(flag_count, int) or flag_count < 1:
        raise InvalidBasis(f"line {line_number}: flag_count must be a positive integer")
    citation = record["citation"]
    if not isinstance(citation, str) or not citation.strip():
        raise InvalidBasis(f"line {line_number}: citation must be nonempty")
    if branch == "q=1-exact" and delta.denominator != 1:
        raise InvalidBasis(
            f"line {line_number}: q=1-exact requires integral delta, got {delta}"
        )
    return delta


def main() -> int:
    if len(sys.argv) != 2:
        print(f"usage: {Path(sys.argv[0]).name} REPORT", file=sys.stderr)
        return 2
    try:
        text = Path(sys.argv[1]).read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        print(f"charge_basis: cannot read report: {exc}", file=sys.stderr)
        return 2

    records: list[tuple[int, str]] = []
    for line_number, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()
        if stripped.startswith(PREFIX):
            records.append((line_number, stripped[len(PREFIX) :]))
    if not records:
        print("charge_basis=ABSENT")
        return 0

    try:
        deltas = [validate(payload, line_number) for line_number, payload in records]
    except InvalidBasis as exc:
        print(f"charge_basis: INVALID: {exc}", file=sys.stderr)
        return 1
    normalized = ",".join(str(delta) for delta in deltas)
    print(f"charge_basis=VALID:{len(records)}:{normalized}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
