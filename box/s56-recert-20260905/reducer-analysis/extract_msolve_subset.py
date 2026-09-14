#!/usr/bin/env python3
"""Extract a row subset from an expanded finite-field msolve system.

The variable header is copied verbatim: this helper drops equations only,
never unknowns.  A JSON manifest binds the subset to its parent system and
to the ordered hashes of the selected polynomials.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re


IDENTIFIER = re.compile(r"[A-Za-z][A-Za-z0-9_]*")
FACTOR = re.compile(r"(?:[A-Za-z][A-Za-z0-9_]*(?:\^\d+)?|\d+)$")


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def parse(path: Path) -> tuple[str, list[str], int, list[str]]:
    text = path.read_text(encoding="utf-8", errors="strict")
    lines = text.splitlines()
    if len(lines) < 3:
        raise ValueError("msolve input has fewer than three lines")
    header = lines[0]
    variables = header.split(",")
    if not variables or len(variables) != len(set(variables)):
        raise ValueError("invalid/duplicate variable header")
    if any(IDENTIFIER.fullmatch(variable) is None for variable in variables):
        raise ValueError("invalid variable identifier")
    characteristic = int(lines[1])
    if characteristic <= 0:
        raise ValueError("subset screens require positive characteristic")
    body = "\n".join(lines[2:])
    if any(symbol in body for symbol in "();/"):
        raise ValueError("input is not flat expanded modular syntax")
    rows = [piece.strip() for piece in body.split(",") if piece.strip()]
    if not rows:
        raise ValueError("empty polynomial body")
    allowed = set(variables)
    for index, row in enumerate(rows):
        if not set(IDENTIFIER.findall(row)) <= allowed:
            raise ValueError(f"row {index} contains an undeclared identifier")
        for term in re.findall(r"[+-]?[^+-]+", row):
            for factor in term.lstrip("+-").split("*"):
                if FACTOR.fullmatch(factor) is None:
                    raise ValueError(f"row {index} has bad factor {factor!r}")
                if factor.isdigit() and int(factor) >= characteristic:
                    raise ValueError(f"row {index} has unreduced coefficient {factor}")
    return header, variables, characteristic, rows


def parse_indices(specification: str, row_count: int) -> list[int]:
    selected: set[int] = set()
    for part in specification.split(","):
        if not part:
            continue
        if "-" in part:
            left, right = map(int, part.split("-", 1))
            if left > right:
                raise ValueError(f"descending index range {part}")
            selected.update(range(left, right + 1))
        else:
            selected.add(int(part))
    if not selected or min(selected) < 0 or max(selected) >= row_count:
        raise ValueError("selected index outside parent row inventory")
    return sorted(selected)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--indices", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    args = parser.parse_args()
    source = args.input.resolve()
    output = args.output.resolve()
    manifest = args.manifest.resolve()
    header, variables, characteristic, rows = parse(source)
    indices = parse_indices(args.indices, len(rows))
    chosen = [rows[index] for index in indices]
    payload = header + "\n" + str(characteristic) + "\n" + ",\n".join(chosen) + "\n"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(payload, encoding="utf-8")
    # Independent post-write parse and byte-for-byte row check.
    check_header, check_variables, check_characteristic, check_rows = parse(output)
    if (check_header, check_variables, check_characteristic, check_rows) != (
        header,
        variables,
        characteristic,
        chosen,
    ):
        raise ValueError("written subset failed exact round-trip")
    record = {
        "schema": "jc2.s56-recert.msolve-row-subset/v1",
        "operation": "drop_rows_only_keep_all_unknowns",
        "parent": str(source),
        "parent_sha256": sha256(source),
        "parent_variable_count": len(variables),
        "parent_row_count": len(rows),
        "characteristic": characteristic,
        "selected_row_indices_zero_based": indices,
        "selected_row_hashes": [sha256_bytes(row.encode()) for row in chosen],
        "selected_row_count": len(chosen),
        "output": str(output),
        "output_sha256": sha256(output),
        "output_variable_count": len(check_variables),
        "all_unknowns_preserved": check_variables == variables,
        "flat_expanded_modular_syntax": True,
        "coefficient_tokens_reduced_below_characteristic": True,
    }
    manifest.parent.mkdir(parents=True, exist_ok=True)
    manifest.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(record, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
