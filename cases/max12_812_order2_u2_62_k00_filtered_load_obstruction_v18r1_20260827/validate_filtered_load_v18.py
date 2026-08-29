#!/usr/bin/env python3
"""Replay V18 truncated lifts and exact left obstruction certificates."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path


LOADS = ("K10", "K6", "K2")


def fail(message: object) -> "None":
    raise RuntimeError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def read_matrix(path: Path, field: str):
    with path.open() as handle:
        header = handle.readline().split()
        if len(header) != 4:
            fail(("bad matrix header", str(path)))
        rows, columns, nonzeros, cutoff = map(int, header)
        values: dict[tuple[int, int], Fraction | int] = {}
        prime = None if field == "Q" else int(field)
        for line in handle:
            raw = line.split()
            if len(raw) != 4:
                fail(("bad matrix row", str(path), line))
            row, column, numerator, denominator = raw
            r, c = int(row), int(column)
            if not (0 <= r < rows and 0 <= c <= columns):
                fail(("matrix index", r, c, rows, columns))
            if prime is None:
                value: Fraction | int = Fraction(int(numerator), int(denominator))
            else:
                den = int(denominator) % prime
                if den == 0:
                    fail("bad-prime denominator")
                value = int(numerator) % prime * pow(den, -1, prime) % prime
            if value == 0 or (r, c) in values:
                fail(("zero/duplicate matrix entry", r, c))
            values[(r, c)] = value
    if len(values) != nonzeros or rows <= 0 or columns <= 0:
        fail(("matrix census", len(values), nonzeros, rows, columns))
    return rows, columns, cutoff, values


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
                fail(("bad solution entry", line))
            solution[int(parts[1])] = parts[2]
        elif parts[0] == "y":
            if len(parts) != 3 or int(parts[1]) in certificate:
                fail(("bad certificate entry", line))
            certificate[int(parts[1])] = parts[2]
        else:
            if len(parts) != 2 or parts[0] in metadata:
                fail(("bad metadata entry", line))
            metadata[parts[0]] = parts[1]
    return metadata, solution, certificate


def replay(matrix_path: Path, solution_path: Path, field: str) -> dict[str, object]:
    rows, columns, cutoff, entries = read_matrix(matrix_path, field)
    metadata, raw_solution, raw_certificate = read_solution(solution_path)
    required = {"field", "cutoff", "rows", "columns", "rank", "augmented_rank", "consistent"}
    if not required.issubset(metadata):
        fail(("missing solution metadata", str(solution_path)))
    if metadata["field"] != field or int(metadata["cutoff"]) != cutoff:
        fail("solution field/cutoff mismatch")
    if int(metadata["rows"]) != rows or int(metadata["columns"]) != columns:
        fail("solution shape mismatch")
    rank = int(metadata["rank"])
    augmented_rank = int(metadata["augmented_rank"])
    consistent = metadata["consistent"] == "1"
    if metadata["consistent"] not in ("0", "1") or augmented_rank - rank not in (0, 1):
        fail("rank metadata malformed")
    if consistent != (rank == augmented_rank):
        fail("rank/branch mismatch")
    prime = None if field == "Q" else int(field)
    zero: Fraction | int = Fraction(0) if prime is None else 0
    if consistent:
        if raw_certificate:
            fail("compatible endpoint carries certificate")
        solution = {
            index: Fraction(value) if prime is None else int(value) % prime
            for index, value in raw_solution.items()
        }
        residual = [zero for _ in range(rows)]
        for (row, column), value in entries.items():
            if column == columns:
                residual[row] -= value
            else:
                residual[row] += value * solution.get(column, zero)
            if prime is not None:
                residual[row] %= prime
        if any(residual):
            fail(("truncated lift replay", cutoff))
        replay_status = "PASS_EXACT_LIFT" if prime is None else "PASS_MODULAR_LIFT"
        certificate_entries = 0
        target_pairing = None
    else:
        if raw_solution:
            fail("incompatible endpoint carries lift")
        if prime is None:
            certificate = {row: Fraction(value) for row, value in raw_certificate.items()}
            if not certificate:
                fail("exact incompatibility lacks certificate")
            annihilator = [Fraction(0) for _ in range(columns)]
            pairing = Fraction(0)
            for (row, column), value in entries.items():
                if column == columns:
                    pairing += certificate.get(row, Fraction(0)) * value
                else:
                    annihilator[column] += certificate.get(row, Fraction(0)) * value
            if any(annihilator) or pairing == 0 or pairing != Fraction(metadata.get("certificate_dot", "0")):
                fail(("exact dual replay", cutoff, pairing))
            replay_status = "PASS_EXACT_DUAL"
            certificate_entries = len(certificate)
            target_pairing = str(pairing)
        else:
            certificate = {row: int(value) % prime for row, value in raw_certificate.items()}
            if not certificate:
                fail("modular incompatibility lacks certificate")
            annihilator = [0 for _ in range(columns)]
            pairing = 0
            for (row, column), value in entries.items():
                if column == columns:
                    pairing = (pairing + certificate.get(row, 0) * value) % prime
                else:
                    annihilator[column] = (annihilator[column] + certificate.get(row, 0) * value) % prime
            if any(annihilator) or pairing == 0 or pairing != int(metadata.get("certificate_dot", "0")) % prime:
                fail(("modular dual replay", cutoff, pairing))
            replay_status = "PASS_MODULAR_DUAL"
            certificate_entries = len(certificate)
            target_pairing = str(pairing)
    return {
        "cutoff": cutoff,
        "rows": rows,
        "columns": columns,
        "rank": rank,
        "augmented_rank": augmented_rank,
        "consistent": consistent,
        "replay": replay_status,
        "nonzero_lift_entries": len(raw_solution),
        "certificate_entries": certificate_entries,
        "target_pairing": target_pairing,
        "matrix_sha256": digest(matrix_path),
        "solution_sha256": digest(solution_path),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("source_audit", type=Path)
    parser.add_argument("--field", choices=("Q", "65521"), required=True)
    parser.add_argument("--entry", action="append", nargs=3,
                        metavar=("DIRECTION", "MATRIX", "SOLUTION"), required=True)
    args = parser.parse_args()
    audit = json.loads(args.source_audit.read_text())
    if audit.get("status") != "PASS-K00-FILTERED-LOAD-V18-EMITTER" or audit.get("field") != args.field:
        fail("source audit sentinel")
    grouped: dict[str, list[dict[str, object]]] = {label: [] for label in LOADS}
    for label, matrix, solution in args.entry:
        if label not in grouped:
            fail(("unknown direction", label))
        endpoint = replay(Path(matrix), Path(solution), args.field)
        grouped[label].append(endpoint)
    directions: dict[str, object] = {}
    for label in LOADS:
        endpoints = sorted(grouped[label], key=lambda item: int(item["cutoff"]))
        if not endpoints or [item["cutoff"] for item in endpoints] != list(range(2, int(endpoints[-1]["cutoff"]) + 1)):
            fail(("nonconsecutive cutoff coverage", label, endpoints))
        failures = [item for item in endpoints if not item["consistent"]]
        if len(failures) > 1 or (failures and failures[0] is not endpoints[-1]):
            fail(("runner did not stop at first failure", label))
        if failures:
            first = int(failures[0]["cutoff"])
            branch = "FIRST_FILTERED_OBSTRUCTION"
            filtered_order: int | str = first
        else:
            first = None
            branch = "NO_FAILURE_THROUGH_D6"
            filtered_order = ">6"
        directions[label] = {
            "branch": branch,
            "filtered_order": filtered_order,
            "first_incompatible_cutoff": first,
            "cutoffs": endpoints,
        }
    result = {
        **audit,
        "status": "PASS-K00-FILTERED-LOAD-V18-ENDPOINT",
        "source_audit_sha256": digest(args.source_audit),
        "directions": directions,
        "interpretation": "SEPARATE_ASSOCIATED_FILTERED_FIRST_LOAD_CLASSES_ONLY",
        "firewall": "NO_COUPLING_NO_LAMBDA19_NO_HONEST_SOURCE_REACHABILITY_NO_ARC_EXCLUSION",
    }
    args.output.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("K00_V18_VALIDATOR_REPLAY=PASS")
    for label in LOADS:
        print(f"K00_V18_{label}_BRANCH={directions[label]['branch']}")
        print(f"K00_V18_{label}_FILTERED_ORDER={directions[label]['filtered_order']}")
    print("K00_V18_ENDPOINT=PASS_FILTERED_FIRST_LOAD_CLASSES")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
