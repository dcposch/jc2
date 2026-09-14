#!/usr/bin/env python3
"""Emit a row-subset Singular job from an audited DUMP__ reduced system.

Rows may be dropped; variables are never dropped.  A UNIT result therefore
certifies the complete reduced ideal containing this subset.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_dump(path: Path) -> tuple[list[str], list[str]]:
    text = path.read_text(encoding="utf-8", errors="strict")
    variable_matches = re.findall(r"^DUMP__VARS (.+?)\s*$", text, re.MULTILINE)
    rows = re.findall(r"^DUMP__ROW (.+?)\s*$", text, re.MULTILINE)
    counts = re.findall(r"^DUMP__COUNT (\d+)\s*$", text, re.MULTILINE)
    if len(variable_matches) != 1 or counts != [str(len(rows))] or not rows:
        raise ValueError("invalid or incomplete reduced dump envelope")
    variables = variable_matches[0].split(",")
    if len(variables) != len(set(variables)):
        raise ValueError("duplicate variables in dump")
    allowed = set(variables)
    for index, row in enumerate(rows):
        if not set(re.findall(r"[A-Za-z][A-Za-z0-9_]*", row)) <= allowed:
            raise ValueError(f"row {index} contains an undeclared variable")
    return variables, rows


def parse_indices(specification: str, row_count: int) -> list[int]:
    result: set[int] = set()
    for piece in specification.split(","):
        if not piece:
            continue
        if "-" in piece:
            left, right = map(int, piece.split("-", 1))
            if left > right:
                raise ValueError(f"descending range {piece}")
            result.update(range(left, right + 1))
        else:
            result.add(int(piece))
    if not result or min(result) < 0 or max(result) >= row_count:
        raise ValueError("selected row index outside dump")
    return sorted(result)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dump", type=Path, required=True)
    parser.add_argument("--characteristic", type=int, required=True)
    parser.add_argument("--indices", required=True)
    parser.add_argument("--algorithm", choices=("std", "slimgb"), default="std")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    dump = args.dump.resolve()
    output = args.output.resolve()
    variables, rows = parse_dump(dump)
    indices = parse_indices(args.indices, len(rows))
    chosen = [rows[index] for index in indices]
    row_hashes = [hashlib.sha256(row.encode()).hexdigest() for row in chosen]
    lines = [
        "// safe reduced-row subset: rows dropped, no unknowns dropped",
        f"// dump_sha256={sha256(dump)}",
        f"// characteristic={args.characteristic}",
        f"// row_indices={','.join(map(str, indices))}",
        f"// row_hashes={','.join(row_hashes)}",
        f"ring R={args.characteristic},({','.join(variables)}),dp;",
        "option(redSB);",
        "ideal J=" + ",\n".join(chosen) + ";",
        f'"SUBSET_BEGIN rows={len(chosen)} variables={len(variables)} algorithm={args.algorithm}";',
        "timer=1; int T0=timer;",
        f"ideal G={args.algorithm}(J);",
        "int DT=timer-T0;",
        "ideal NF=reduce(J,G);",
        "int NF_ZERO=1; int I;",
        "for (I=1;I<=size(NF);I++) { if (NF[I]!=0) { NF_ZERO=0; } }",
        "poly ONE=reduce(1,G);",
        "ideal LG=lead(G);",
        '"SUBSET_DONE ms="+string(DT);',
        '"SUBSET_GENERATOR_COUNT "+string(size(J));',
        '"SUBSET_BASIS_SIZE "+string(size(G));',
        '"SUBSET_DIMENSION "+string(dim(G));',
        '"SUBSET_LEAD_DIMENSION "+string(dim(LG));',
        '"SUBSET_NF_ALL_ZERO "+string(NF_ZERO);',
        'if (ONE==0) { "SUBSET_UNIT 1"; } else { "SUBSET_UNIT 0"; }',
        'if (NF_ZERO!=1) { "SUBSET_CONTROL_FAIL"; exit(95); }',
        '"SCRIPT_DONE";',
    ]
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    record = {
        "schema": "jc2.s56-recert.reduced-row-subset/v1",
        "dump": str(dump),
        "dump_sha256": sha256(dump),
        "characteristic": args.characteristic,
        "variables_retained": len(variables),
        "source_reduced_rows": len(rows),
        "selected_row_count": len(indices),
        "selected_row_indices": indices,
        "selected_row_hashes": row_hashes,
        "algorithm": args.algorithm,
        "script": str(output),
        "script_sha256": sha256(output),
    }
    print(json.dumps(record, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
