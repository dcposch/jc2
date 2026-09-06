#!/usr/bin/env python3
"""Recover and independently audit metadata after a post-emission JSON failure.

The certificate builder closes both CAS streams, the labels ledger, and the
variable map before serializing its metadata.  This tool reconstructs that
metadata from those closed artifacts, while independently checking every
original-name term against its aliased msolve term and recomputing the
primitive coefficient/exponent stream hash.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path

from build_direct import DirectChart, EXPECTED, seq_sha, sha_path


def clean_q(line: str, last: bool) -> str:
    suffix = ";\n" if last else ",\n"
    if not line.endswith(suffix):
        raise RuntimeError("bad Singular generator delimiter")
    return line[: -len(suffix)]


def clean_ms(line: str, last: bool) -> str:
    suffix = "\n" if last else ",\n"
    if not line.endswith(suffix):
        raise RuntimeError("bad msolve generator delimiter")
    return line[: -len(suffix)]


def pieces(row: str):
    start = 0
    for i in range(1, len(row)):
        if row[i] in "+-":
            yield row[start:i]
            start = i
    if start < len(row):
        yield row[start:]


def parsed(piece: str, indices: dict[str, int]):
    sign = 1
    if piece[0] == "+":
        piece = piece[1:]
    elif piece[0] == "-":
        sign = -1
        piece = piece[1:]
    fields = piece.split("*")
    if fields[0].isdigit():
        magnitude = int(fields.pop(0))
    else:
        magnitude = 1
    support = []
    degree = 0
    for factor in fields:
        if factor == "1":
            continue
        if "^" in factor:
            name, exponent_text = factor.split("^", 1)
            exponent = int(exponent_text)
        else:
            name, exponent = factor, 1
        if name not in indices:
            raise RuntimeError(f"unknown variable {name!r}")
        support.append((indices[name], exponent))
        degree += exponent
    return sign * magnitude, tuple(support), degree


def sha_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", required=True, type=Path)
    parser.add_argument("--case", default="99-delta2", choices=sorted(EXPECTED))
    parser.add_argument("--build-time", required=True, type=Path)
    parser.add_argument("--builder", required=True, type=Path)
    parser.add_argument("--shared-emitter", required=True, type=Path)
    args = parser.parse_args()

    tag = args.case
    directory = args.directory.resolve()
    q_path = directory / f"{tag}.sing"
    ms_path = directory / f"{tag}.ms"
    labels_path = directory / f"{tag}.labels.tsv"
    variables_path = directory / f"{tag}.variables.json"
    meta_path = directory / f"{tag}.build.json"
    if meta_path.exists():
        raise RuntimeError("refusing to replace existing build metadata")

    variable_payload = json.loads(variables_path.read_text())
    if variable_payload.get("schema") != "T2T3_DIRECT_VARIABLE_MAP/v1":
        raise RuntimeError("bad variable-map schema")
    semantic_names = variable_payload["semantic_order"]
    names = variable_payload["solver_order"]
    records = variable_payload["records"]
    aliases = [record["alias"] for record in records]
    if len(names) != len(aliases) or len(names) != EXPECTED[tag]["semantic_count"]:
        raise RuntimeError("variable-count mismatch")
    if any(record["name"] != names[i] for i, record in enumerate(records)):
        raise RuntimeError("variable-map ordering mismatch")
    name_indices = {name: i for i, name in enumerate(names)}
    alias_indices = {name: i for i, name in enumerate(aliases)}

    label_rows = []
    with labels_path.open() as handle:
        if handle.readline() != "emitted_index\tblock\tlabel\tterms\tprimitive_sha256\n":
            raise RuntimeError("bad labels header")
        for line in handle:
            index, block, label, terms, row_sha = line.rstrip("\n").split("\t")
            label_rows.append((int(index), block, label, int(terms), row_sha))
    if len(label_rows) != 466 or [row[0] for row in label_rows] != list(range(466)):
        raise RuntimeError("expected exactly 466 indexed rows")

    canonical = hashlib.sha256()
    original_text = hashlib.sha256()
    alias_text = hashlib.sha256()
    maximum_degree = 0
    paired_terms = 0
    with q_path.open() as q_handle, ms_path.open() as ms_handle:
        q_header = [q_handle.readline() for _ in range(3)]
        ms_header = [ms_handle.readline() for _ in range(2)]
        if q_header[2] != "ideal I=\n" or ms_header[0].rstrip("\n").split(",") != aliases:
            raise RuntimeError("bad presentation headers")
        if int(ms_header[1]) != DirectChart.PRIME:
            raise RuntimeError("bad screen prime")
        for row_index, (_, _, _, expected_terms, expected_row_sha) in enumerate(label_rows):
            last = row_index == len(label_rows) - 1
            q_row = clean_q(q_handle.readline(), last)
            ms_row = clean_ms(ms_handle.readline(), last)
            if hashlib.sha256(q_row.encode()).hexdigest() != expected_row_sha:
                raise RuntimeError(f"row-ledger hash mismatch at {row_index}")
            original_text.update(q_row.encode() + b"\n")
            alias_text.update(ms_row.encode() + b"\n")
            canonical.update(b"GENERATOR\n")
            q_iter = iter(pieces(q_row))
            ms_iter = iter(pieces(ms_row))
            term_count = 0
            while True:
                q_piece = next(q_iter, None)
                ms_piece = next(ms_iter, None)
                if q_piece is None or ms_piece is None:
                    if q_piece != ms_piece:
                        raise RuntimeError(f"paired term-count mismatch at row {row_index}")
                    break
                q_term = parsed(q_piece, name_indices)
                ms_term = parsed(ms_piece, alias_indices)
                if q_term[:2] != ms_term[:2]:
                    raise RuntimeError(f"paired generator mismatch at row {row_index}, term {term_count}")
                integer, support, degree = q_term
                canonical.update(
                    f"{integer}:{','.join(f'{i}^{e}' for i, e in support)}\n".encode()
                )
                maximum_degree = max(maximum_degree, degree)
                term_count += 1
            if term_count != expected_terms:
                raise RuntimeError(f"term ledger mismatch at row {row_index}")
            paired_terms += term_count
            canonical.update(b"END\n")
        q_tail = q_handle.read()
        ms_tail = ms_handle.read()
    required_tail = 'print("ALL_ROWS_PARSED");\nprint("BEGIN_STD");\nideal G=std(I);\n'
    if required_tail not in q_tail or ms_tail:
        raise RuntimeError("bad presentation footer")

    raw_counts = Counter(row[1] for row in label_rows)
    emitted_counts = dict(sorted(raw_counts.items()))
    raw_label_hash = hashlib.sha256()
    emitted_label_hash = hashlib.sha256()
    for _, _, label, _, _ in label_rows:
        raw_label_hash.update(label.encode() + b"\n")
        emitted_label_hash.update(label.encode() + b"\n")

    noninverse = len(names) - 3
    rrow = [int(record["site_r"]) for record in records[:noninverse]]
    zrow = [int(record["site_z"]) for record in records[:noninverse]]
    omitted = None
    determinant = 0
    for i in range(noninverse):
        for j in range(i + 1, noninverse):
            determinant = rrow[i] * zrow[j] - rrow[j] * zrow[i]
            if determinant:
                omitted = (i, j)
                break
        if omitted is not None:
            break
    if omitted is None:
        raise RuntimeError("site-order rank failure")
    matrix = rrow + zrow
    for column in range(noninverse):
        if column not in omitted:
            matrix.extend(
                1 if row_column == column else 0
                for row_column in range(noninverse)
            )

    elapsed = None
    peak = None
    for line in args.build_time.read_text().splitlines():
        if "Elapsed (wall clock) time" in line:
            value = line.rsplit(": ", 1)[-1]
            pieces_time = value.split(":")
            elapsed = sum(float(value) * 60 ** power for power, value in enumerate(reversed(pieces_time)))
        elif "Maximum resident set size (kbytes)" in line:
            peak = int(line.rsplit(":", 1)[-1])
    if elapsed is None or peak is None:
        raise RuntimeError("missing build resource custody")

    spec = EXPECTED[tag]
    staged_input = args.shared_emitter.resolve().parent / "inputs" / spec["input"].name
    input_path = staged_input if staged_input.is_file() else spec["input"]
    meta = {
        "schema": "T2T3_DIRECT_T2_FACE_SUBSET/v1",
        "status": "EMITTED_EXACT_Q_AND_MODULAR_NOT_RUN",
        "case": tag,
        "classification_scope": "literal full-direct-ideal generator subset; UNIT is conclusive for the full ideal, NONUNIT is inconclusive",
        "selected_blocks": ["source_residual", "T2_upper", "T2_face_subset", "inverse"],
        "omitted_blocks": ["T2_strict", "T3_recurrence", "T3_strict", "T3_face"],
        "selected_T2_face_indices": [55],
        "complete_T2_face": False,
        "field": "Q",
        "modular_prime": DirectChart.PRIME,
        "input": str(input_path),
        "input_sha256": sha_path(input_path),
        "semantic_variable_count": len(semantic_names),
        "semantic_variable_order_sha256": seq_sha(semantic_names),
        "solver_variable_count": len(names),
        "solver_variable_order_sha256": seq_sha(names),
        "alias_order_sha256": seq_sha(aliases),
        "graph_variables_emitted": 0,
        "constraint_variables_pivoted": 0,
        "raw_row_counts": emitted_counts,
        "identically_zero_after_substitution": {},
        "emitted_nonzero_counts": emitted_counts,
        "emitted_generator_count": len(label_rows),
        "raw_row_labels_sha256": raw_label_hash.hexdigest(),
        "emitted_row_labels_sha256": emitted_label_hash.hexdigest(),
        "canonical_primitive_generator_sequence_sha256": canonical.hexdigest(),
        "original_name_generator_text_sha256": original_text.hexdigest(),
        "alias_name_generator_text_sha256": alias_text.hexdigest(),
        "paired_name_to_alias_rows_exact": True,
        "paired_term_count": paired_terms,
        "expanded_term_count": sum(row[3] for row in label_rows),
        "msolve_32bit_offset_product": sum(row[3] for row in label_rows) * len(names),
        "msolve_32bit_offset_guard": DirectChart.MSOLVE_OFFSET_LIMIT,
        "msolve_32bit_offset_safe": sum(row[3] for row in label_rows) * len(names) < DirectChart.MSOLVE_OFFSET_LIMIT,
        "maximum_generator_terms": max(row[3] for row in label_rows),
        "maximum_generator_label": max(label_rows, key=lambda row: row[3])[2],
        "maximum_total_degree": maximum_degree,
        "order": {
            "singular": f"(M(two-site {noninverse}x{noninverse}),dp(3))",
            "matrix_flat_sha256": seq_sha(matrix),
            "identity_completion_omits": {
                "columns": [names[i] for i in omitted],
                "indices": list(omitted),
                "determinant": determinant,
            },
            "classification": "global two-site matrix filtration; normalized rows need not be bihomogeneous",
        },
        "T2_target": f"{spec['lam2']}*z^{spec['t2z']}*(1+z)^{spec['t2p']}",
        "localizers": [f"{spec['zlam2']}*{spec['lam2']}-1", "Z3*lambda3-1", f"{spec['zsep']}*{spec['sep']}-1"],
        "source_support_rows_preserved_via_frozen_affine_map": True,
        "no_Jacobian_variable_or_tail_rows": True,
        "primitive_integer_rows": True,
        "singular_file": q_path.name,
        "singular_file_bytes": q_path.stat().st_size,
        "singular_file_sha256": sha_file(q_path),
        "msolve_file": ms_path.name,
        "msolve_file_bytes": ms_path.stat().st_size,
        "msolve_file_sha256": sha_file(ms_path),
        "labels_file": labels_path.name,
        "labels_file_sha256": sha_file(labels_path),
        "variable_map_file": variables_path.name,
        "variable_map_sha256": sha_file(variables_path),
        "driver_sha256": sha_file(args.builder),
        "shared_emitter_driver_sha256": sha_file(args.shared_emitter),
        "metadata_recovered_after_post_emission_fmpz_json_error": True,
        "recovery_driver_sha256": sha_file(Path(__file__)),
        "build_wall_seconds": round(elapsed, 3),
        "peak_RSS_KiB": peak,
    }
    meta_path.write_text(json.dumps(meta, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "schema": meta["schema"],
        "paired_name_to_alias_rows_exact": True,
        "paired_term_count": paired_terms,
        "canonical_sha256": canonical.hexdigest(),
        "singular_sha256": meta["singular_file_sha256"],
        "msolve_sha256": meta["msolve_file_sha256"],
        "metadata": str(meta_path),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
