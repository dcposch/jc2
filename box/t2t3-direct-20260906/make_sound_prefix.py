#!/usr/bin/env python3
"""Extract a paired, sound generator prefix from an in-progress direct build.

If a prefix together with the three production localizers is unit, that is an
exact certificate for the full ideal because it is a literal subset of its
generators.  A nonunit prefix has no classification force.  Source files must
contain at least one later row, ensuring the selected last row was completely
flushed before this script snapshots it.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


IDENT = re.compile(r"\b[A-Za-z_]\w*\b")


def sha(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def clean_row(line: str) -> str:
    line = line.rstrip("\n")
    return line[:-1] if line.endswith(",") else line


def mapped(text: str, name_to_alias: dict[str, str]) -> str:
    return IDENT.sub(lambda match: name_to_alias.get(match.group(), match.group()), text)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", required=True, choices=["99-delta2", "99-delta52", "108-free-mean"])
    parser.add_argument("--rows", required=True, type=int)
    parser.add_argument("--source-dir", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    if args.rows <= 0:
        raise SystemExit("--rows must be positive")
    source_ms = args.source_dir / f"{args.case}.ms"
    source_sing = args.source_dir / f"{args.case}.sing"
    output = args.output_dir
    output.mkdir(parents=True, exist_ok=False)
    target_ms = output / f"{args.case}-prefix{args.rows}.ms"
    target_sing = output / f"{args.case}-prefix{args.rows}.sing"

    with source_ms.open() as ms_in, source_sing.open() as sing_in:
        alias_line = ms_in.readline()
        prime_line = ms_in.readline()
        ring_line = sing_in.readline()
        option_line = sing_in.readline()
        ideal_line = sing_in.readline()
        if not alias_line or not prime_line or ideal_line.strip() != "ideal I=":
            raise RuntimeError("unexpected source headers")
        marker = "ring R=0,("
        if not ring_line.startswith(marker) or "),(M(" not in ring_line:
            raise RuntimeError("unexpected Singular ring declaration")
        names = ring_line[len(marker):].split("),(M(", 1)[0].split(",")
        aliases = alias_line.strip().split(",")
        if len(names) != len(aliases):
            raise RuntimeError("variable/alias length mismatch")
        name_to_alias = dict(zip(names, aliases))

        ms_rows = []
        sing_rows = []
        for _ in range(args.rows + 1):
            ms_line = ms_in.readline()
            sing_line = sing_in.readline()
            if not ms_line or not sing_line:
                raise RuntimeError("source does not yet contain a flushed later row")
            ms_rows.append(ms_line)
            sing_rows.append(sing_line)
        # Row N+1 is read only as a completion witness; it is not selected.
        ms_rows.pop()
        sing_rows.pop()

    for index, (ms_line, sing_line) in enumerate(zip(ms_rows, sing_rows)):
        got = clean_row(ms_line)
        expected = mapped(clean_row(sing_line), name_to_alias)
        if got != expected:
            raise RuntimeError(f"paired row mismatch at index {index}")

    lam2 = "leader63" if args.case == "108-free-mean" else "leader55"
    zlam2 = "Z63" if args.case == "108-free-mean" else "Z55"
    sep = "rho" if args.case == "99-delta2" else "c"
    zsep = "Zrho" if args.case == "99-delta2" else "Zc"
    localizers = [f"{zlam2}*{lam2}-1", "Z3*lambda3-1", f"{zsep}*{sep}-1"]
    alias_localizers = [mapped(row, name_to_alias) for row in localizers]

    with target_ms.open("w") as handle:
        handle.write(alias_line)
        handle.write(prime_line)
        selected = [clean_row(row) for row in ms_rows] + alias_localizers
        handle.write(",\n".join(selected) + "\n")
    with target_sing.open("w") as handle:
        handle.write(ring_line)
        handle.write(option_line)
        handle.write(ideal_line)
        selected = [clean_row(row) for row in sing_rows] + localizers
        handle.write(",\n".join(selected) + ";\n")
        handle.write('print("ALL_ROWS_PARSED");\n')
        handle.write('print("BEGIN_STD");\n')
        handle.write("ideal G=std(I);\n")
        handle.write('print("END_STD");\n')
        handle.write('print("BEGIN_RESULT");\n')
        handle.write('print("REDUCE_ONE="+string(reduce(1,G)));\n')
        handle.write('print("DIMENSION="+string(dim(G)));\n')
        handle.write('print("BASIS_SIZE="+string(size(G)));\n')
        handle.write('print("END_RESULT");\nquit;\n')

    original_digest = hashlib.sha256()
    alias_digest = hashlib.sha256()
    for original, alias in zip(
        [clean_row(row) for row in sing_rows] + localizers,
        [clean_row(row) for row in ms_rows] + alias_localizers,
    ):
        original_digest.update(original.encode() + b"\n")
        alias_digest.update(alias.encode() + b"\n")
    meta = {
        "schema": "T2T3_SOUND_PREFIX/v1",
        "case": args.case,
        "classification_scope": "literal full-ideal generator subset; UNIT is conclusive, NONUNIT is not",
        "selected_direct_rows": args.rows,
        "appended_production_localizers": localizers,
        "generator_count": args.rows + 3,
        "paired_name_to_alias_rows_exact": True,
        "original_generator_text_sha256": original_digest.hexdigest(),
        "alias_generator_text_sha256": alias_digest.hexdigest(),
        "source_singular_sha256_at_snapshot": sha(source_sing),
        "source_msolve_sha256_at_snapshot": sha(source_ms),
        "singular_file": target_sing.name,
        "singular_sha256": sha(target_sing),
        "msolve_file": target_ms.name,
        "msolve_sha256": sha(target_ms),
    }
    meta_path = output / "prefix.json"
    meta_path.write_text(json.dumps(meta, indent=2, sort_keys=True) + "\n")
    print(json.dumps(meta, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
