#!/usr/bin/env python3
"""Replay and validate exact/modular K00 Macaulay compatible lifts."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path


EXPECTED_PREFIX = {2: 4, 3: 28, 4: 106, 5: 294, 6: 676}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def read_matrix(path: Path, field: str):
    with path.open() as handle:
        header = handle.readline().split()
        if len(header) != 4:
            raise RuntimeError("bad matrix header")
        rows, columns, nonzeros, cutoff = map(int, header)
        entries: dict[tuple[int, int], Fraction | int] = {}
        prime = None if field == "Q" else int(field)
        for line in handle:
            row, column, numerator, denominator = line.split()
            r, c = int(row), int(column)
            if prime is None:
                value: Fraction | int = Fraction(int(numerator), int(denominator))
            else:
                den = int(denominator) % prime
                if den == 0:
                    raise RuntimeError("bad-prime denominator")
                value = (int(numerator) % prime) * pow(den, -1, prime) % prime
            entries[(r, c)] = value
    if len(entries) != nonzeros:
        raise RuntimeError("matrix nonzero count mismatch")
    return rows, columns, cutoff, entries


def read_solution(path: Path):
    metadata: dict[str, str] = {}
    solution: dict[int, str] = {}
    certificate: dict[int, str] = {}
    for line in path.read_text().splitlines():
        parts = line.split()
        if not parts:
            continue
        if parts[0] == "x":
            if len(parts) != 3 or int(parts[1]) in solution:
                raise RuntimeError("malformed/duplicate solution entry")
            solution[int(parts[1])] = parts[2]
        elif parts[0] == "y":
            if len(parts) != 3 or int(parts[1]) in certificate:
                raise RuntimeError("malformed/duplicate certificate entry")
            certificate[int(parts[1])] = parts[2]
        else:
            if len(parts) != 2 or parts[0] in metadata:
                raise RuntimeError("malformed/duplicate metadata")
            metadata[parts[0]] = parts[1]
    return metadata, solution, certificate


def replay(matrix: Path, solution_path: Path, field: str):
    rows, columns, cutoff, entries = read_matrix(matrix, field)
    metadata, raw_solution, raw_certificate = read_solution(solution_path)
    required = {"field", "cutoff", "rows", "columns", "rank", "augmented_rank", "consistent"}
    if not required.issubset(metadata):
        raise RuntimeError("missing solution metadata")
    if metadata["field"] != field or int(metadata["cutoff"]) != cutoff:
        raise RuntimeError("field/cutoff metadata mismatch")
    if int(metadata["rows"]) != rows or int(metadata["columns"]) != columns:
        raise RuntimeError("matrix shape metadata mismatch")
    rank = int(metadata["rank"])
    augmented_rank = int(metadata["augmented_rank"])
    consistent = metadata["consistent"] == "1"
    if metadata["consistent"] not in ("0", "1") or augmented_rank - rank not in (0, 1):
        raise RuntimeError("malformed rank/consistency")
    if consistent != (rank == augmented_rank):
        raise RuntimeError("rank/consistency mismatch")
    if cutoff in EXPECTED_PREFIX and (rank != EXPECTED_PREFIX[cutoff] or augmented_rank != rank):
        raise RuntimeError(("prefix rank sentinel mismatch", cutoff, rank, augmented_rank))
    if not consistent:
        if raw_solution:
            raise RuntimeError("inconsistent endpoint must not carry a solution")
        if field == "Q":
            if "certificate_dot" not in metadata or not raw_certificate:
                raise RuntimeError("exact inconsistent endpoint lacks a left certificate")
            certificate = {row: Fraction(value) for row, value in raw_certificate.items()}
            annihilator = [Fraction(0) for _ in range(columns)]
            target_dot = Fraction(0)
            for (row, column), value in entries.items():
                if column == columns:
                    target_dot += certificate.get(row, Fraction(0)) * value
                else:
                    annihilator[column] += certificate.get(row, Fraction(0)) * value
            if any(annihilator) or target_dot == 0 or target_dot != Fraction(metadata["certificate_dot"]):
                raise RuntimeError("exact left certificate replay failed")
            replay_text = "PASS_EXACT_LEFT_CERTIFICATE"
            certificate_entries = len(certificate)
        else:
            replay_text = "NO_LIFT_MODULAR_NAVIGATION"
            certificate_entries = 0
        return {
            "rank": rank,
            "augmented_rank": augmented_rank,
            "consistent": False,
            "replay": replay_text,
            "certificate_entries": certificate_entries,
        }
    if raw_certificate:
        raise RuntimeError("consistent endpoint must not carry a left certificate")
    if field == "Q":
        solution = {column: Fraction(value) for column, value in raw_solution.items()}
        zero: Fraction | int = Fraction(0)
    else:
        prime = int(field)
        solution = {column: int(value) % prime for column, value in raw_solution.items()}
        zero = 0
    residual = [zero for _ in range(rows)]
    for (row, column), value in entries.items():
        if column == columns:
            residual[row] -= value
        else:
            residual[row] += value * solution.get(column, zero)
        if field != "Q":
            residual[row] %= int(field)
    if any(value != 0 for value in residual):
        raise RuntimeError("compatible lift replay failed")
    return {
        "rank": rank,
        "augmented_rank": augmented_rank,
        "consistent": True,
        "replay": "PASS_EXACT_COEFFICIENTWISE" if field == "Q" else "PASS_MODULAR_COEFFICIENTWISE",
        "nonzero_solution_entries": len(solution),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("source_audit", type=Path)
    parser.add_argument("load_stencil", type=Path)
    parser.add_argument("--field", required=True)
    parser.add_argument("--matrix-solution", action="append", nargs=2, metavar=("MATRIX", "SOLUTION"), required=True)
    args = parser.parse_args()
    audit = json.loads(args.source_audit.read_text())
    if audit.get("status") != "PASS-K00-FILTERED-MACAULAY-EMITTER":
        raise RuntimeError("source audit did not pass")
    results: dict[str, object] = {}
    for matrix_text, solution_text in args.matrix_solution:
        matrix, solution = Path(matrix_text), Path(solution_text)
        endpoint = replay(matrix, solution, args.field)
        cutoff = int(read_solution(solution)[0]["cutoff"])
        results[str(cutoff)] = {
            **endpoint,
            "matrix_sha256": digest(matrix),
            "solution_sha256": digest(solution),
        }
    if sorted(map(int, results)) != list(range(2, 8)):
        raise RuntimeError("cutoff coverage must be exactly D2 through D7")
    result = {
        **audit,
        "status": "PASS-K00-FILTERED-MACAULAY-ENDPOINT",
        "field": args.field,
        "cutoff_results": results,
        "D7_compatible": bool(results["7"]["consistent"]),
        "source_audit_sha256": digest(args.source_audit),
        "load_normal_stencil_sha256": digest(args.load_stencil),
    }
    args.output.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("K00_MACAULAY_VALIDATOR_REPLAY=PASS")
    print("K00_MACAULAY_D7_COMPATIBLE=" + ("1" if result["D7_compatible"] else "0"))
    print("K00_MACAULAY_ENDPOINT=PASS_FILTERED_D7_ONLY")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
