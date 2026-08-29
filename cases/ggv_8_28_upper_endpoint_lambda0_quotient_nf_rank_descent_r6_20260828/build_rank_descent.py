#!/usr/bin/env python3
"""Compile exact size-10 zero and size-9 witness certificates in Q[params]/I."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
from pathlib import Path


R5_COMPILER_SHA256 = "7ba6c106ff62a3bfc289be408d151bda7e85d73cb5868543d86ebe926f272b0a"
COMPONENTS = {"p": "P", "c8p02": "C8P02"}
EXPECTED_ROWS = 11
EXPECTED_COLS = 10
EXPECTED_SUPPORT = 75
EXPECTED_UPPER_SIZE = 10
EXPECTED_UPPER_FORMAL = 11
EXPECTED_UPPER_MATCHABLE = 2
EXPECTED_TARGET_SIZE = 9
EXPECTED_TARGET_FORMAL = 550
EXPECTED_TARGET_MATCHABLE = 172


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_r5(path: Path):
    if sha256(path) != R5_COMPILER_SHA256:
        raise SystemExit("R5_COMPILER_SOURCE_DRIFT")
    spec = importlib.util.spec_from_file_location("r5_nf", path)
    if spec is None or spec.loader is None:
        raise SystemExit("R5_COMPILER_IMPORT_FAILURE")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def formal_slots(rows: int, cols: int, size: int, support, perfect):
    slots = []
    for row_set in itertools.combinations(range(1, rows + 1), size):
        for col_set in itertools.combinations(range(1, cols + 1), size):
            slots.append((row_set, col_set, perfect(row_set, col_set, support)))
    return slots


def compile_script(r5, label: str, factor: str, remaining: list[str], matrix: list[list[str]], output_dir: Path):
    rows = len(matrix)
    cols = len(matrix[0])
    support = {
        (i + 1, j + 1)
        for i, row in enumerate(matrix)
        for j, value in enumerate(row)
        if value != "0"
    }
    if (rows, cols, len(support)) != (EXPECTED_ROWS, EXPECTED_COLS, EXPECTED_SUPPORT):
        raise SystemExit("RESIDUAL_SHAPE_OR_SUPPORT_DISAGREEMENT")
    support_bound = r5.max_matching(range(1, rows + 1), range(1, cols + 1), support)
    if support_bound != EXPECTED_UPPER_SIZE:
        raise SystemExit("SUPPORT_BOUND_DISAGREEMENT")

    upper = formal_slots(rows, cols, EXPECTED_UPPER_SIZE, support, r5.perfect)
    target = formal_slots(rows, cols, EXPECTED_TARGET_SIZE, support, r5.perfect)
    upper_matchable = [(rs, cs) for rs, cs, matchable in upper if matchable]
    target_matchable = [(rs, cs) for rs, cs, matchable in target if matchable]
    if (len(upper), len(upper_matchable)) != (EXPECTED_UPPER_FORMAL, EXPECTED_UPPER_MATCHABLE):
        raise SystemExit("UPPER_SLOT_CENSUS_DISAGREEMENT")
    if (len(target), len(target_matchable)) != (EXPECTED_TARGET_FORMAL, EXPECTED_TARGET_MATCHABLE):
        raise SystemExit("TARGET_SLOT_CENSUS_DISAGREEMENT")

    upper_path = output_dir / f"{label}_SIZE10_FORMAL_SLOTS.tsv"
    target_path = output_dir / f"{label}_SIZE9_FORMAL_SLOTS.tsv"
    upper_path.write_text(
        "slot|rows|cols|support_classification\n"
        + "\n".join(
            f"{slot}|{','.join(map(str, rs))}|{','.join(map(str, cs))}|"
            f"{'MATCHABLE' if matchable else 'STRUCTURAL_ZERO'}"
            for slot, (rs, cs, matchable) in enumerate(upper, 1)
        )
        + "\n"
    )
    target_path.write_text(
        "slot|rows|cols|support_classification\n"
        + "\n".join(
            f"{slot}|{','.join(map(str, rs))}|{','.join(map(str, cs))}|"
            f"{'MATCHABLE' if matchable else 'STRUCTURAL_ZERO'}"
            for slot, (rs, cs, matchable) in enumerate(target, 1)
        )
        + "\n"
    )

    values = ",".join(value for row in matrix for value in row)
    lines = ["// Exact quotient NF rank descent: all size-10 zeros plus size-9 witness."]
    lines += r5.ambient_header(label, factor, remaining)
    lines += [
        f"matrix R[{rows}][{cols}]={values};",
        "int i; int j; int support_replay_failures=0; int entry_nf_reductions=0;",
        "for(i=1;i<=nrows(R);i=i+1){ for(j=1;j<=ncols(R);j=j+1){ R[i,j]=reduce(R[i,j],BRANCH_SB); entry_nf_reductions=entry_nf_reductions+1; } }",
    ]
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if (i, j) in support:
                lines.append(f"if(R[{i},{j}]==0){{ support_replay_failures=support_replay_failures+1; }}")
            else:
                lines.append(f"if(R[{i},{j}]!=0){{ support_replay_failures=support_replay_failures+1; }}")

    lines += [
        f'string UPPERFILE="{label}_SIZE10_MATCHABLE_RAW_NF.tsv";',
        'write(UPPERFILE,"candidate|rows|cols|raw_determinant|normal_form");',
        "int upper_candidate_count=0; int upper_nf_zero_count=0; int upper_nf_nonzero_count=0; int determinant_nf_reductions=0;",
    ]
    for candidate, (row_set, col_set) in enumerate(upper_matchable, 1):
        entries = ",".join(f"R[{i},{j}]" for i in row_set for j in col_set)
        rows_text = ",".join(map(str, row_set))
        cols_text = ",".join(map(str, col_set))
        lines += [
            f"matrix U[{EXPECTED_UPPER_SIZE}][{EXPECTED_UPPER_SIZE}]={entries}; poly RAWDET=det(U); poly NORMALDET=reduce(RAWDET,BRANCH_SB); determinant_nf_reductions=determinant_nf_reductions+1; upper_candidate_count=upper_candidate_count+1;",
            f'write(UPPERFILE,"{candidate}|{rows_text}|{cols_text}|"+string(RAWDET)+"|"+string(NORMALDET));',
            "if(NORMALDET==0){ upper_nf_zero_count=upper_nf_zero_count+1; } else { upper_nf_nonzero_count=upper_nf_nonzero_count+1; }",
            "kill U; kill RAWDET; kill NORMALDET;",
        ]

    lines += [
        f'string TARGETFILE="{label}_SIZE9_MATCHABLE_RAW_NF.tsv"; string WITNESS="{label}_SIZE9_RANK_WITNESS.tsv";',
        'write(TARGETFILE,"candidate|rows|cols|raw_determinant|normal_form"); write(WITNESS,"candidate|rows|cols|normal_form");',
        "int target_candidate_count=0; int target_nf_zero_count=0; int target_nf_nonzero_count=0; int witness_found=0;",
    ]
    for candidate, (row_set, col_set) in enumerate(target_matchable, 1):
        entries = ",".join(f"R[{i},{j}]" for i in row_set for j in col_set)
        rows_text = ",".join(map(str, row_set))
        cols_text = ",".join(map(str, col_set))
        lines += [
            f"matrix T[{EXPECTED_TARGET_SIZE}][{EXPECTED_TARGET_SIZE}]={entries}; poly RAWDET=det(T); poly NORMALDET=reduce(RAWDET,BRANCH_SB); determinant_nf_reductions=determinant_nf_reductions+1; target_candidate_count=target_candidate_count+1;",
            f'write(TARGETFILE,"{candidate}|{rows_text}|{cols_text}|"+string(RAWDET)+"|"+string(NORMALDET));',
            f'if(NORMALDET==0){{ target_nf_zero_count=target_nf_zero_count+1; }} else {{ target_nf_nonzero_count=target_nf_nonzero_count+1; if(witness_found==0){{ witness_found=1; write(WITNESS,"{candidate}|{rows_text}|{cols_text}|"+string(NORMALDET)); }} }}',
            "kill T; kill RAWDET; kill NORMALDET;",
        ]

    lines += [
        f'print("SIZE10_FORMAL_SLOT_COUNT={EXPECTED_UPPER_FORMAL}"); print("SIZE10_STRUCTURAL_ZERO_SLOT_COUNT={EXPECTED_UPPER_FORMAL - EXPECTED_UPPER_MATCHABLE}");',
        'print("SIZE10_MATCHABLE_CANDIDATE_COUNT="+string(upper_candidate_count)); print("SIZE10_MATCHABLE_NF_ZERO_COUNT="+string(upper_nf_zero_count)); print("SIZE10_MATCHABLE_NF_NONZERO_COUNT="+string(upper_nf_nonzero_count));',
        f'print("SIZE9_FORMAL_SLOT_COUNT={EXPECTED_TARGET_FORMAL}"); print("SIZE9_STRUCTURAL_ZERO_SLOT_COUNT={EXPECTED_TARGET_FORMAL - EXPECTED_TARGET_MATCHABLE}");',
        'print("SIZE9_MATCHABLE_CANDIDATE_COUNT="+string(target_candidate_count)); print("SIZE9_MATCHABLE_NF_ZERO_COUNT="+string(target_nf_zero_count)); print("SIZE9_MATCHABLE_NF_NONZERO_COUNT="+string(target_nf_nonzero_count)); print("SIZE9_WITNESS_NF_NONZERO="+string(witness_found));',
        'print("SUPPORT_REPLAY_FAILURES="+string(support_replay_failures)); print("ENTRY_NF_REDUCTIONS="+string(entry_nf_reductions)); print("DETERMINANT_NF_REDUCTIONS="+string(determinant_nf_reductions));',
        f"if(support_replay_failures!=0 || upper_candidate_count!={EXPECTED_UPPER_MATCHABLE} || upper_nf_zero_count!={EXPECTED_UPPER_MATCHABLE} || upper_nf_nonzero_count!=0 || target_candidate_count!={EXPECTED_TARGET_MATCHABLE} || witness_found!=1){{ print(\"FATAL_RANK_DESCENT_CERTIFICATE\"); quit; }}",
        'print("EVERY_SIZE10_MINOR_NF_ZERO=1"); print("EXACT_SIZE9_NF_WITNESS=1"); print("EXACT_QUOTIENT_RANK9_CERTIFICATE_COMPLETE=1");',
        "quit;",
        "",
    ]
    return "\n".join(lines), len(support)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--r5-compiler", type=Path, required=True)
    parser.add_argument("--r1-compiler", type=Path, required=True)
    parser.add_argument("--matrix", type=Path, required=True)
    parser.add_argument("--factor-archive", type=Path, required=True)
    parser.add_argument("--component", choices=sorted(COMPONENTS), required=True)
    parser.add_argument("--residual", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    r5 = load_r5(args.r5_compiler)
    label, _zeros, factor, remaining, _assignment, _counts = r5.inputs(
        args.r1_compiler, args.matrix, args.factor_archive, args.component
    )
    if label != COMPONENTS[args.component]:
        raise SystemExit("COMPONENT_LABEL_DISAGREEMENT")
    matrix = r5.read_residual(args.residual)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    script, support_count = compile_script(r5, label, factor, remaining, matrix, args.output_dir)
    script_name = f"{args.component}_rank_descent.sing"
    (args.output_dir / script_name).write_text(script)
    (args.output_dir / "BUILD_MANIFEST.tsv").write_text(
        "component|label|residual_sha256|script|script_sha256\n"
        f"{args.component}|{label}|{sha256(args.residual)}|{script_name}|{hashlib.sha256(script.encode()).hexdigest()}\n"
    )
    print(f"COMPONENT={args.component}")
    print(f"LABEL={label}")
    print(f"SUPPORT_ENTRY_COUNT={support_count}")
    print("SIZE10_FORMAL_SLOT_COUNT=11")
    print("SIZE10_MATCHABLE_SLOT_COUNT=2")
    print("SIZE9_FORMAL_SLOT_COUNT=550")
    print("SIZE9_MATCHABLE_SLOT_COUNT=172")
    print("NO_QRING_AMBIENT_NF_ONLY=1")
    print("RANK_DESCENT_BUILD_PASS")


if __name__ == "__main__":
    main()

