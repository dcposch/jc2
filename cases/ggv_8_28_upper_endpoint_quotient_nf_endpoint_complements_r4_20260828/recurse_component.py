#!/usr/bin/env python3
"""Exact ambient-NF finite-chart recursion on one endpoint component."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import os
from pathlib import Path
import signal
import subprocess
import tarfile
import time

from transcript_gate import assert_clean_transcript


UPSTREAM_SHA = "7ba6c106ff62a3bfc289be408d151bda7e85d73cb5868543d86ebe926f272b0a"
COMPONENTS = {
    "p": ("P", 9),
    "c8p02": ("C8P02", 9),
    "q1p02": ("Q1P02", 6),
    "q1p03": ("Q1P03", 4),
    "triple02": ("TRIPLE02", 6),
    "triple03": ("TRIPLE03", 4),
}

RANK_ARCHIVES = {
    "p": ("source/jc2/cases/ggv_8_28_upper_endpoint_lambda0_quotient_nf_rank_descent_r6_20260828/custody/ggv_lambda0_quotient_nf_descent_p_r6_20260828T161500Z_r6c.terminal.tar.gz",
          "fb778b1a7078314fa1fb941d39327cb9d99eab2ad2aa5a4c6c88f45062e26173",
          "/output/run/descent.stdout", "EXACT_QUOTIENT_RANK9_CERTIFICATE_COMPLETE=1"),
    "c8p02": ("source/jc2/cases/ggv_8_28_upper_endpoint_lambda0_quotient_nf_rank_descent_r6_20260828/custody/ggv_lambda0_quotient_nf_descent_c8p02_r6_20260828T161500Z_r6e.terminal.tar.gz",
               "99cccf8c0508aa8818b00541eab0f29a1596ecbf7dcad9d9beee1a220b2419e6",
               "/output/run/descent.stdout", "EXACT_QUOTIENT_RANK9_CERTIFICATE_COMPLETE=1"),
    "q1p02": ("source/jc2/cases/ggv_8_28_upper_endpoint_lambda0_quotient_nf_rank_r5_20260828/custody/ggv_lambda0_quotient_nf_q1p02_r5_20260828T160000Z_r6f.terminal.tar.gz",
              "992dbd0e0a81f6f37901f24c63141607c29c26d2a28195bebc37698c026b8424",
              "/output/run/rank.stdout", "EXACT_QUOTIENT_RANK_CERTIFICATE_COMPLETE=1"),
    "q1p03": ("source/jc2/cases/ggv_8_28_upper_endpoint_lambda0_quotient_nf_rank_r5_20260828/custody/ggv_lambda0_quotient_nf_q1p03_r5_20260828T160000Z_r6g.terminal.tar.gz",
              "9a8cf752e526d29679fa673af1359b81b66302af73998806c022a4e80c306c9c",
              "/output/run/rank.stdout", "EXACT_QUOTIENT_RANK_CERTIFICATE_COMPLETE=1"),
    "triple02": ("source/jc2/cases/ggv_8_28_upper_endpoint_lambda0_quotient_nf_rank_r5_20260828/custody/ggv_lambda0_quotient_nf_triple02_r5_20260828T160000Z_r6h.terminal.tar.gz",
                 "b947a2d3e81525902a93500026020c2cf9580f070767757389daadb9a6bbe3b2",
                 "/output/run/rank.stdout", "EXACT_QUOTIENT_RANK_CERTIFICATE_COMPLETE=1"),
    "triple03": ("source/jc2/cases/ggv_8_28_upper_endpoint_lambda0_quotient_nf_rank_r5_20260828/custody/ggv_lambda0_quotient_nf_triple03_r5_20260828T160000Z_r6i.terminal.tar.gz",
                 "1d1871532a845f2ac964886035c06abcc211ae80f5c68e153850951ba242b809",
                 "/output/run/rank.stdout", "EXACT_QUOTIENT_RANK_CERTIFICATE_COMPLETE=1"),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_upstream(path: Path):
    if sha256(path) != UPSTREAM_SHA:
        raise SystemExit("UPSTREAM_BUILD_NF_RANK_SHA_DRIFT")
    spec = importlib.util.spec_from_file_location("banked_nf", path)
    if spec is None or spec.loader is None:
        raise SystemExit("UPSTREAM_IMPORT_FAILURE")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def verify_rank_bound(base: Path, component: str, expected_rank: int) -> dict[str, object]:
    relative, expected_sha, member_suffix, marker = RANK_ARCHIVES[component]
    archive_path = base / relative
    actual_sha = sha256(archive_path)
    if actual_sha != expected_sha:
        raise SystemExit(f"RANK_ARCHIVE_SHA_DRIFT:{actual_sha}")
    with tarfile.open(archive_path, "r:gz") as archive:
        matches = [entry for entry in archive.getmembers()
                   if entry.isfile() and entry.name.endswith(member_suffix)]
        if len(matches) != 1:
            raise SystemExit(f"RANK_CERTIFICATE_MEMBER_CENSUS:{len(matches)}")
        handle = archive.extractfile(matches[0])
        if handle is None:
            raise SystemExit("RANK_CERTIFICATE_MEMBER_READ")
        text = handle.read().decode("utf-8", errors="strict")
    lines = text.splitlines()
    if marker not in lines:
        raise SystemExit("RANK_CERTIFICATE_MARKER_MISSING")
    bound_markers = {f"STRUCTURAL_RANK_BOUND={expected_rank}",
                     f"EXACT_SIZE{expected_rank}_NF_WITNESS=1"}
    if not any(value in lines for value in bound_markers):
        raise SystemExit("RANK_CERTIFICATE_BOUND_MARKER_MISSING")
    return {
        "archive": relative,
        "archive_sha256": actual_sha,
        "certificate_member": matches[0].name,
        "certificate_member_sha256": hashlib.sha256(text.encode()).hexdigest(),
        "certificate_marker": marker,
        "rank_upper_bound": expected_rank,
    }


def clean_poly(text: str) -> str:
    value = "".join(text.split())
    if not value or "|" in value or ";" in value:
        raise SystemExit("UNSAFE_OR_EMPTY_POLYNOMIAL_TEXT")
    return value


def read_residual(path: Path) -> list[list[str]]:
    lines = path.read_text().splitlines()
    if not lines or lines[0] != "rows|11|cols|10":
        raise SystemExit("RESIDUAL_HEADER_FAILURE")
    matrix = [["0"] * 10 for _ in range(11)]
    seen = set()
    for line in lines[1:]:
        i, j, value = line.split("|", 2)
        key = (int(i), int(j))
        if key in seen or not (1 <= key[0] <= 11 and 1 <= key[1] <= 10):
            raise SystemExit("RESIDUAL_INDEX_FAILURE")
        seen.add(key)
        matrix[key[0] - 1][key[1] - 1] = clean_poly(value)
    if len(seen) != 110:
        raise SystemExit("RESIDUAL_CENSUS_FAILURE")
    return matrix


def matrix_literal(name: str, rows: int, cols: int, entries: list[str]) -> str:
    if len(entries) != rows * cols:
        raise ValueError((name, rows, cols, len(entries)))
    return f"matrix {name}[{rows}][{cols}]=" + ",".join(entries) + ";"


def finalize_script(lines: list[str]) -> str:
    text = "\n".join(lines)
    forbidden = ("REDUCER_PLACEHOLDER", "PLACEHOLDER", "TODO")
    present = [token for token in forbidden if token in text]
    if present:
        raise RuntimeError(f"UNRESOLVED_GENERATOR_TOKEN:{','.join(present)}")
    return text


def finalize_saturation_script(lines: list[str]) -> str:
    text = finalize_script(lines)
    if "OPEN_SAT_RESULT[2]" in text:
        raise RuntimeError("UNSAFE_SATURATION_LIST_SLOT_2")
    required = (
        "SATURATION_OBJECT_TYPE=",
        "SATURATION_OBJECT_SIZE=",
        "SATURATION_SLOT1_TYPE=",
        "SATURATION_STABILITY_FAILURES=",
        "EMPTY_OPEN_POWER_MEMBERSHIP_CERTIFICATE=",
        "SATURATION_CERTIFICATE_COMPLETE=1",
    )
    missing = [token for token in required if token not in text]
    if missing:
        raise RuntimeError("SATURATION_CERTIFICATE_TOKEN_MISSING:"
                           + ",".join(missing))
    return text


def finalize_chart_script(lines: list[str]) -> str:
    text = finalize_script(lines)
    if "OPEN_SAT_RESULT[2]" in text:
        raise RuntimeError("UNSAFE_CHART_SATURATION_LIST_SLOT_2")
    if "CHART_PIVOT_REDUCER=ACTIVE_SB" in text:
        raise RuntimeError("UNSAFE_CHART_ACTIVE_REPIVOT")
    required = (
        "CHART_SATURATION_OBJECT_TYPE=",
        "CHART_SATURATION_OBJECT_SIZE=",
        "CHART_SATURATION_SLOT1_TYPE=",
        "CHART_SATURATION_STABILITY_FAILURES=",
        "CHART_OPEN_PROPER_IDEAL_CERTIFICATE=",
        "CHART_PIVOT_REDUCER=NODE_SB",
        "CHART_BASE_CHANGE_REDUCTION_COUNT=",
        "NODE_TRANSFORM_BASE_CHANGED_TO_ACTIVE_SB=1",
    )
    missing = [token for token in required if token not in text]
    if missing:
        raise RuntimeError("CHART_SATURATION_TOKEN_MISSING:"
                           + ",".join(missing))
    return text


def node_header(remaining: list[str], generators: list[str], node: int) -> list[str]:
    ideal = ",".join(generators)
    lines = [
        f'ring ambient=0,({",".join(remaining)}),dp;',
        f"ideal NODE_IDEAL={ideal};",
        "ideal NODE_SB=std(NODE_IDEAL);",
        "poly NODE_UNIT_NF=reduce(1,NODE_SB);",
        f'print("NODE_INDEX={node}"); print("NODE_GENERATOR_COUNT={len(generators)}");',
        'print("NODE_EMPTY="+string(NODE_UNIT_NF==0));',
        f'write("NODE_{node:03d}_STANDARD_BASIS.txt",string(NODE_SB));',
    ]
    for index, generator in enumerate(generators, 1):
        lines.extend([
            f"poly NODE_GENERATOR_{index}={generator};",
            f"poly NODE_GENERATOR_{index}_NF=reduce(NODE_GENERATOR_{index},NODE_SB);",
            f'if(NODE_GENERATOR_{index}_NF!=0){{ print("FATAL_NODE_GENERATOR_NF_{index}"); quit; }}',
        ])
    lines.extend([
        'if(NODE_UNIT_NF==0){ print("EXACT_EMPTY_NODE=1"); quit; }',
        "poly NODE_MUTATION=NODE_GENERATOR_1+1; poly NODE_MUTATION_NF=reduce(NODE_MUTATION,NODE_SB);",
        'if(NODE_MUTATION_NF==0){ print("FATAL_NODE_MUTATION_FIXTURE"); quit; }',
        'print("NODE_REDUCER_FIXTURES_PASS=1");',
    ])
    return lines


def elimination_lines(label: str, assignment: str, track_transform: bool,
                      prefix: str, reducer: str = "NODE_SB") -> list[str]:
    c_setup = "matrix C[105][105];" if track_transform else ""
    c_identity = "for(i=1;i<=105;i=i+1){ C[i,i]=1; }" if track_transform else ""
    c_swap = "for(i=1;i<=105;i=i+1){ swap_entry=C[i,step]; C[i,step]=C[i,pj]; C[i,pj]=swap_entry; }" if track_transform else ""
    c_update = f"for(i=1;i<=105;i=i+1){{ C[i,j]=reduce(C[i,j]-multiple*C[i,step],{reducer}); operation_reductions=operation_reductions+1; }}" if track_transform else ""
    pivot_loop = (
        'while(step<=105){ found=0; pi=0; pj=0; for(i=step;i<=106 && found==0;i=i+1){ for(j=step;j<=105 && found==0;j=j+1){ B[i,j]=reduce(B[i,j],REDUCER_PLACEHOLDER); operation_reductions=operation_reductions+1; if(B[i,j]!=0 && deg(B[i,j])==0){ found=1; pi=i; pj=j; } } } if(found==0){ step=106; } else { for(j=1;j<=105;j=j+1){ swap_entry=B[step,j]; B[step,j]=B[pi,j]; B[pi,j]=swap_entry; } for(i=1;i<=106;i=i+1){ swap_entry=B[i,step]; B[i,step]=B[i,pj]; B[i,pj]=swap_entry; } '
        + c_swap
        + ' B[step,step]=reduce(B[step,step],REDUCER_PLACEHOLDER); operation_reductions=operation_reductions+1; if(B[step,step]==0 || deg(B[step,step])!=0){ invariant_failures=invariant_failures+1; } inverse_unit=1/leadcoef(B[step,step]); for(i=step+1;i<=106;i=i+1){ multiple=reduce(B[i,step]*inverse_unit,REDUCER_PLACEHOLDER); operation_reductions=operation_reductions+1; for(j=step;j<=105;j=j+1){ B[i,j]=reduce(B[i,j]-multiple*B[step,j],REDUCER_PLACEHOLDER); operation_reductions=operation_reductions+1; } } for(j=step+1;j<=105;j=j+1){ multiple=reduce(B[step,j]*inverse_unit,REDUCER_PLACEHOLDER); operation_reductions=operation_reductions+1; for(i=step;i<=106;i=i+1){ B[i,j]=reduce(B[i,j]-multiple*B[i,step],REDUCER_PLACEHOLDER); operation_reductions=operation_reductions+1; } '
        + c_update
        + ' } for(i=1;i<=106;i=i+1){ if(i!=step && reduce(B[i,step],REDUCER_PLACEHOLDER)!=0){ invariant_failures=invariant_failures+1; } } for(j=1;j<=105;j=j+1){ if(j!=step && reduce(B[step,j],REDUCER_PLACEHOLDER)!=0){ invariant_failures=invariant_failures+1; } } write(PIVOTFILE,string(step)+"|"+string(pi)+"|"+string(pj)+"|"+string(B[step,step])); pivot_count=pivot_count+1; step=step+1; } }'
    ).replace("REDUCER_PLACEHOLDER", reducer)
    return [
        assignment,
        f"matrix ORIGINAL=M; matrix B=M; {c_setup}",
        "int i; int j; int k; int step=1; int found; int pi; int pj; int pivot_count=0; int invariant_failures=0; int operation_reductions=0;",
        "poly swap_entry; poly multiple; poly CHECK; number inverse_unit;",
        f'string PIVOTFILE="{prefix}_PIVOTS.tsv"; string RESIDUALFILE="{prefix}_RESIDUAL.tsv";',
        'write(PIVOTFILE,"step|source_row|source_col|pivot");',
        c_identity,
        f"for(i=1;i<=106;i=i+1){{ for(j=1;j<=105;j=j+1){{ B[i,j]=reduce(B[i,j],{reducer}); operation_reductions=operation_reductions+1; }} }}",
        pivot_loop,
        'print("NF_RATIONAL_UNIT_PIVOT_COUNT="+string(pivot_count)); print("NF_PIVOT_INVARIANT_FAILURES="+string(invariant_failures));',
        'if(pivot_count!=95 || invariant_failures!=0){ print("FATAL_95_PIVOT_REPLAY"); quit; }',
        "matrix R[11][10]; int nf_drift=0;",
        'write(RESIDUALFILE,"rows|11|cols|10");',
        f'for(i=1;i<=11;i=i+1){{ for(j=1;j<=10;j=j+1){{ R[i,j]=reduce(B[95+i,95+j],{reducer}); if(R[i,j]-reduce(R[i,j],{reducer})!=0){{ nf_drift=nf_drift+1; }} write(RESIDUALFILE,string(i)+"|"+string(j)+"|"+string(R[i,j])); }} }}',
        'if(nf_drift!=0){ print("FATAL_RESIDUAL_NF_DRIFT"); quit; }',
        'print("NODE_RESIDUAL_REDUCTION_COMPLETE=1");',
    ]


def build_reduce_script(remaining: list[str], generators: list[str], node: int,
                        label: str, assignment: str) -> str:
    lines = ["// Exact node reduction."]
    lines += node_header(remaining, generators, node)
    lines += elimination_lines(label, assignment, False, f"NODE_{node:03d}_REDUCE")
    lines += ['print("NODE_REDUCE_COMPLETE=1"); quit;', ""]
    return finalize_script([line for line in lines if line != ""])


def max_matching(rows: tuple[int, ...], cols: tuple[int, ...],
                 support: set[tuple[int, int]]) -> int:
    matching: dict[int, int] = {}

    def augment(row: int, seen: set[int]) -> bool:
        for col in cols:
            if (row, col) not in support or col in seen:
                continue
            seen.add(col)
            if col not in matching or augment(matching[col], seen):
                matching[col] = row
                return True
        return False

    return sum(augment(row, set()) for row in rows)


def perfect(rows: tuple[int, ...], cols: tuple[int, ...],
            support: set[tuple[int, int]]) -> bool:
    return max_matching(rows, cols, support) == len(rows)


def build_rank_size_script(remaining: list[str], generators: list[str],
                           node: int, residual: list[list[str]], size: int,
                           census_path: Path) -> str:
    support = {(i + 1, j + 1) for i, row in enumerate(residual)
               for j, value in enumerate(row) if value != "0"}
    row_sets = list(itertools.combinations(range(1, 12), size))
    col_sets = list(itertools.combinations(range(1, 11), size))
    formal = len(row_sets) * len(col_sets)
    candidates = [(rows, cols) for rows in row_sets for cols in col_sets
                  if perfect(rows, cols, support)]
    census = {
        "node": node,
        "size": size,
        "formal_slots": formal,
        "support_matchable": len(candidates),
        "structural_zero": formal - len(candidates),
        "support_entries": len(support),
    }
    census_path.write_text(json.dumps(census, indent=2, sort_keys=True) + "\n")
    values = [value for row in residual for value in row]
    lines = ["// Exact single-size ambient-NF rank census."]
    lines += node_header(remaining, generators, node)
    lines += [
        matrix_literal("R", 11, 10, values),
        "int i; int j; int support_replay_failures=0; int candidate_count=0; int nonzero_count=0; int determinant_nf_reductions=0; int witness_found=0;",
        "for(i=1;i<=11;i=i+1){ for(j=1;j<=10;j=j+1){ R[i,j]=reduce(R[i,j],NODE_SB); } }",
    ]
    for i in range(1, 12):
        for j in range(1, 11):
            expected_nonzero = (i, j) in support
            condition = f"R[{i},{j}]==0" if expected_nonzero else f"R[{i},{j}]!=0"
            lines.append(f"if({condition}){{ support_replay_failures=support_replay_failures+1; }}")
    lines += [
        f'string CENSUS="NODE_{node:03d}_SIZE_{size}_MINORS.tsv";',
        f'string WITNESS="NODE_{node:03d}_SIZE_{size}_WITNESS.tsv";',
        'write(CENSUS,"slot|rows|cols|normal_form"); write(WITNESS,"rank|rows|cols|normal_form");',
    ]
    if size == 0:
        lines += [
            "poly DRAW=1; poly DNF=reduce(DRAW,NODE_SB); candidate_count=1; determinant_nf_reductions=1;",
            'write(CENSUS,"1|EMPTY|EMPTY|"+string(DNF));',
            'if(DNF!=0){ nonzero_count=1; witness_found=1; write(WITNESS,"0|EMPTY|EMPTY|"+string(DNF)); }',
            "kill DRAW; kill DNF;",
        ]
    else:
        for slot, (rows, cols) in enumerate(candidates, 1):
            entries = [f"R[{i},{j}]" for i in rows for j in cols]
            row_text = ",".join(map(str, rows))
            col_text = ",".join(map(str, cols))
            lines += [
                matrix_literal("S", size, size, entries),
                "poly DRAW=det(S); poly DNF=reduce(DRAW,NODE_SB); candidate_count=candidate_count+1; determinant_nf_reductions=determinant_nf_reductions+1;",
                f'write(CENSUS,"{slot}|{row_text}|{col_text}|"+string(DNF));',
                f'if(DNF!=0){{ nonzero_count=nonzero_count+1; if(witness_found==0){{ witness_found=1; write(WITNESS,"{size}|{row_text}|{col_text}|"+string(DNF)); }} }}',
                "kill S; kill DRAW; kill DNF;",
            ]
    lines += [
        f'print("RANK_SIZE={size}"); print("RANK_SIZE_FORMAL_SLOTS={formal}");',
        f'print("RANK_SIZE_STRUCTURAL_ZERO_SLOTS={formal-len(candidates)}");',
        'print("RANK_SIZE_MATCHABLE_TESTED="+string(candidate_count)); print("RANK_SIZE_NF_NONZERO_COUNT="+string(nonzero_count)); print("RANK_SIZE_WITNESS_FOUND="+string(witness_found));',
        'print("SUPPORT_REPLAY_FAILURES="+string(support_replay_failures)); print("DETERMINANT_NF_REDUCTIONS="+string(determinant_nf_reductions));',
        f'if(support_replay_failures!=0 || candidate_count!={len(candidates)}){{ print("FATAL_RANK_SIZE_CENSUS"); quit; }}',
        'if(witness_found==0){ print("EVERY_MATCHABLE_MINOR_AT_SIZE_NF_ZERO=1"); }',
        'print("RANK_SIZE_CENSUS_COMPLETE=1"); quit;',
        "",
    ]
    return finalize_script(lines)


def read_witness(path: Path, expected_rank: int) -> tuple[tuple[int, ...], tuple[int, ...], str]:
    lines = path.read_text().splitlines()
    if len(lines) != 2 or lines[0] != "rank|rows|cols|normal_form":
        raise SystemExit("WITNESS_FORMAT_FAILURE")
    rank_text, rows_text, cols_text, delta = lines[1].split("|", 3)
    if int(rank_text) != expected_rank:
        raise SystemExit("WITNESS_RANK_FAILURE")
    if expected_rank == 0:
        rows: tuple[int, ...] = ()
        cols: tuple[int, ...] = ()
    else:
        rows = tuple(map(int, rows_text.split(",")))
        cols = tuple(map(int, cols_text.split(",")))
    if len(rows) != expected_rank or len(cols) != expected_rank:
        raise SystemExit("WITNESS_INDEX_CENSUS_FAILURE")
    return rows, cols, clean_poly(delta)


def validate_empty_open_certificate(path: Path, open_empty: bool) -> dict[str, object]:
    fields = path.read_text().strip().split("|")
    if (len(fields) != 6 or fields[0] != "found"
            or fields[2] != "exponent" or fields[4] != "normal_form"):
        raise RuntimeError("EMPTY_OPEN_CERTIFICATE_FORMAT")
    found = fields[1] == "1"
    if fields[1] not in ("0", "1"):
        raise RuntimeError("EMPTY_OPEN_CERTIFICATE_BOOLEAN")
    exponent = int(fields[3])
    normal_form = clean_poly(fields[5])
    if open_empty:
        if not found or exponent < 0 or normal_form != "0":
            raise RuntimeError("EMPTY_OPEN_POWER_CERTIFICATE_DISAGREEMENT")
    elif found or exponent != -1:
        raise RuntimeError("PROPER_OPEN_POWER_CERTIFICATE_DISAGREEMENT")
    return {
        "power_membership_found": found,
        "power_membership_exponent": exponent,
        "power_membership_normal_form": normal_form,
        "certificate_sha256": sha256(path),
    }


def build_saturation_script(remaining: list[str], generators: list[str],
                            node: int, scanned_delta: str) -> str:
    lines = ["// Exact open saturation and closed successor."]
    lines += node_header(remaining, generators, node)
    lines += [
        f"poly SCANNED_DELTA={scanned_delta};",
        "poly DELTA_NODE_NF=reduce(SCANNED_DELTA,NODE_SB);",
        'if(DELTA_NODE_NF==0 || DELTA_NODE_NF!=SCANNED_DELTA){ print("FATAL_SATURATION_DELTA_REPLAY"); quit; }',
        'LIB "elim.lib";',
        "ideal DELTA_IDEAL=DELTA_NODE_NF;",
        "list OPEN_SAT_RESULT=sat(NODE_IDEAL,DELTA_IDEAL);",
        'print("SATURATION_OBJECT_TYPE="+typeof(OPEN_SAT_RESULT));',
        'print("SATURATION_OBJECT_SIZE="+string(size(OPEN_SAT_RESULT)));',
        'if(typeof(OPEN_SAT_RESULT)!="list" || size(OPEN_SAT_RESULT)!=1){ print("FATAL_SATURATION_OBJECT_SHAPE"); quit; }',
        'print("SATURATION_SLOT1_TYPE="+typeof(OPEN_SAT_RESULT[1]));',
        'if(typeof(OPEN_SAT_RESULT[1])!="ideal"){ print("FATAL_SATURATION_SLOT1_TYPE"); quit; }',
        "ideal OPEN_SAT_IDEAL=OPEN_SAT_RESULT[1]; ideal OPEN_SB=std(OPEN_SAT_IDEAL); poly OPEN_UNIT_NF=reduce(1,OPEN_SB);",
        f'write("NODE_{node:03d}_OPEN_SAT_STANDARD_BASIS.txt",string(OPEN_SB));',
        "int si; int node_inclusion_failures=0; for(si=1;si<=size(NODE_IDEAL);si=si+1){ if(reduce(NODE_IDEAL[si],OPEN_SB)!=0){ node_inclusion_failures=node_inclusion_failures+1; } }",
        'print("SATURATION_NODE_INCLUSION_FAILURES="+string(node_inclusion_failures)); if(node_inclusion_failures!=0){ print("FATAL_SATURATION_NODE_INCLUSION"); quit; }',
        "list OPEN_STABLE_RESULT=sat(OPEN_SB,DELTA_IDEAL);",
        'if(typeof(OPEN_STABLE_RESULT)!="list" || size(OPEN_STABLE_RESULT)!=1 || typeof(OPEN_STABLE_RESULT[1])!="ideal"){ print("FATAL_SATURATION_STABILITY_OBJECT"); quit; }',
        "ideal OPEN_STABLE_IDEAL=OPEN_STABLE_RESULT[1]; ideal OPEN_STABLE_SB=std(OPEN_STABLE_IDEAL); int stability_failures=0;",
        "for(si=1;si<=size(OPEN_SB);si=si+1){ if(reduce(OPEN_SB[si],OPEN_STABLE_SB)!=0){ stability_failures=stability_failures+1; } } for(si=1;si<=size(OPEN_STABLE_SB);si=si+1){ if(reduce(OPEN_STABLE_SB[si],OPEN_SB)!=0){ stability_failures=stability_failures+1; } }",
        'print("SATURATION_STABILITY_FAILURES="+string(stability_failures)); if(stability_failures!=0){ print("FATAL_SATURATION_NOT_STABLE"); quit; }',
        "poly EMPTY_CERT_POWER=1; poly EMPTY_CERT_NF=1; int empty_cert_found=0; int empty_cert_exponent=-1; int ek;",
        "for(ek=0;ek<=256;ek=ek+1){ if(empty_cert_found==0){ EMPTY_CERT_NF=reduce(EMPTY_CERT_POWER,NODE_SB); if(EMPTY_CERT_NF==0){ empty_cert_found=1; empty_cert_exponent=ek; } else { EMPTY_CERT_POWER=reduce(EMPTY_CERT_POWER*DELTA_NODE_NF,NODE_SB); } } }",
        f'write("NODE_{node:03d}_EMPTY_OPEN_POWER_CERTIFICATE.txt","found|"+string(empty_cert_found)+"|exponent|"+string(empty_cert_exponent)+"|normal_form|"+string(EMPTY_CERT_NF));',
        'if(OPEN_UNIT_NF==0 && empty_cert_found!=1){ print("FATAL_EMPTY_OPEN_WITHOUT_POWER_CERTIFICATE"); quit; }',
        'if(OPEN_UNIT_NF!=0 && empty_cert_found!=0){ print("FATAL_PROPER_OPEN_WITH_ZERO_POWER"); quit; }',
        'print("EMPTY_OPEN_POWER_MEMBERSHIP_CERTIFICATE="+string(empty_cert_found));',
        'print("EMPTY_OPEN_POWER_CERTIFICATE_EXPONENT="+string(empty_cert_exponent));',
        'print("PROPER_OPEN_IDEAL_CERTIFICATE="+string(OPEN_UNIT_NF!=0 && reduce(DELTA_NODE_NF,OPEN_SB)!=0 && stability_failures==0));',
        'print("OPEN_CHART_EMPTY="+string(OPEN_UNIT_NF==0));',
        f"ideal NEXT_IDEAL={','.join(generators)},DELTA_NODE_NF; ideal NEXT_SB=std(NEXT_IDEAL); poly NEXT_UNIT_NF=reduce(1,NEXT_SB);",
        f'write("NODE_{node:03d}_NEXT_STANDARD_BASIS.txt",string(NEXT_SB));',
        'print("NEXT_REMAINDER_EMPTY="+string(NEXT_UNIT_NF==0));',
        'print("SATURATION_CERTIFICATE_COMPLETE=1");',
        'print("OPEN_SATURATION_AND_CLOSED_SUCCESSOR_COMPLETE=1"); quit;',
        "",
    ]
    return finalize_saturation_script(lines)


def build_chart_script(remaining: list[str], generators: list[str], node: int,
                       label: str, assignment: str, residual: list[list[str]],
                       rank: int, rows: tuple[int, ...], cols: tuple[int, ...],
                       scanned_delta: str) -> str:
    free = tuple(col for col in range(1, 11) if col not in cols)
    lines = ["// Exact recursive adjugate endpoint chart."]
    lines += node_header(remaining, generators, node)
    lines += [
        f"poly SCANNED_DELTA_NODE={scanned_delta};",
        'LIB "elim.lib";',
        "ideal CHART_DELTA_IDEAL=SCANNED_DELTA_NODE;",
        "list OPEN_SAT_RESULT=sat(NODE_IDEAL,CHART_DELTA_IDEAL);",
        'print("CHART_SATURATION_OBJECT_TYPE="+typeof(OPEN_SAT_RESULT)); print("CHART_SATURATION_OBJECT_SIZE="+string(size(OPEN_SAT_RESULT)));',
        'if(typeof(OPEN_SAT_RESULT)!="list" || size(OPEN_SAT_RESULT)!=1){ print("FATAL_CHART_SATURATION_OBJECT_SHAPE"); quit; }',
        'print("CHART_SATURATION_SLOT1_TYPE="+typeof(OPEN_SAT_RESULT[1])); if(typeof(OPEN_SAT_RESULT[1])!="ideal"){ print("FATAL_CHART_SATURATION_SLOT1_TYPE"); quit; }',
        "ideal ACTIVE_SAT_IDEAL=OPEN_SAT_RESULT[1]; ideal ACTIVE_SB=std(ACTIVE_SAT_IDEAL); poly ACTIVE_UNIT_NF=reduce(1,ACTIVE_SB);",
        'if(ACTIVE_UNIT_NF==0){ print("FATAL_CHART_OPEN_SATURATION_UNIT"); quit; }',
        "poly DELTA=reduce(SCANNED_DELTA_NODE,ACTIVE_SB);",
        'if(DELTA==0){ print("FATAL_CHART_DELTA_ZERO_AFTER_SATURATION"); quit; }',
        "int si; int chart_node_inclusion_failures=0; for(si=1;si<=size(NODE_IDEAL);si=si+1){ if(reduce(NODE_IDEAL[si],ACTIVE_SB)!=0){ chart_node_inclusion_failures=chart_node_inclusion_failures+1; } }",
        'print("CHART_SATURATION_NODE_INCLUSION_FAILURES="+string(chart_node_inclusion_failures)); if(chart_node_inclusion_failures!=0){ print("FATAL_CHART_SATURATION_NODE_INCLUSION"); quit; }',
        "list CHART_STABLE_RESULT=sat(ACTIVE_SB,CHART_DELTA_IDEAL);",
        'if(typeof(CHART_STABLE_RESULT)!="list" || size(CHART_STABLE_RESULT)!=1 || typeof(CHART_STABLE_RESULT[1])!="ideal"){ print("FATAL_CHART_SATURATION_STABILITY_OBJECT"); quit; }',
        "ideal CHART_STABLE_IDEAL=CHART_STABLE_RESULT[1]; ideal CHART_STABLE_SB=std(CHART_STABLE_IDEAL); int chart_stability_failures=0;",
        "for(si=1;si<=size(ACTIVE_SB);si=si+1){ if(reduce(ACTIVE_SB[si],CHART_STABLE_SB)!=0){ chart_stability_failures=chart_stability_failures+1; } } for(si=1;si<=size(CHART_STABLE_SB);si=si+1){ if(reduce(CHART_STABLE_SB[si],ACTIVE_SB)!=0){ chart_stability_failures=chart_stability_failures+1; } }",
        'print("CHART_SATURATION_STABILITY_FAILURES="+string(chart_stability_failures)); if(chart_stability_failures!=0){ print("FATAL_CHART_SATURATION_NOT_STABLE"); quit; }',
        'print("CHART_OPEN_PROPER_IDEAL_CERTIFICATE="+string(ACTIVE_UNIT_NF!=0 && DELTA!=0 && chart_stability_failures==0));',
        'print("OPEN_CHART_SATURATION_PROPER=1");',
    ]
    prefix = f"NODE_{node:03d}_CHART"
    lines += ['print("CHART_PIVOT_REDUCER=NODE_SB");']
    lines += elimination_lines(label, assignment, True, prefix, "NODE_SB")
    lines += [
        "int base_change_reductions=0;",
        "for(i=1;i<=11;i=i+1){ for(j=1;j<=10;j=j+1){ R[i,j]=reduce(R[i,j],ACTIVE_SB); base_change_reductions=base_change_reductions+1; } }",
        "for(i=1;i<=105;i=i+1){ for(j=1;j<=105;j=j+1){ C[i,j]=reduce(C[i,j],ACTIVE_SB); base_change_reductions=base_change_reductions+1; } }",
        f'string BCRFILE="NODE_{node:03d}_CHART_BASE_CHANGED_RESIDUAL.tsv"; write(BCRFILE,"rows|11|cols|10");',
        'for(i=1;i<=11;i=i+1){ for(j=1;j<=10;j=j+1){ write(BCRFILE,string(i)+"|"+string(j)+"|"+string(R[i,j])); } }',
        'print("CHART_BASE_CHANGE_REDUCTION_COUNT="+string(base_change_reductions));',
        'if(base_change_reductions!=11135){ print("FATAL_CHART_BASE_CHANGE_CENSUS"); quit; }',
        'print("NODE_TRANSFORM_BASE_CHANGED_TO_ACTIVE_SB=1");',
    ]
    if rank == 0:
        lines += ["poly DELTA_DET=1;"]
    else:
        entries = [f"R[{i},{j}]" for i in rows for j in cols]
        lines += [
            matrix_literal("PIVOT_MINOR", rank, rank, entries),
            "poly DELTA_RAW=det(PIVOT_MINOR); poly DELTA_DET=reduce(DELTA_RAW,ACTIVE_SB);",
        ]
    lines += [
        'print("CHART_DELTA_NF_NONZERO="+string(DELTA!=0)); print("SCANNED_DELTA_REPLAY_EQUAL="+string(DELTA==DELTA_DET));',
        'if(DELTA==0 || DELTA!=DELTA_DET){ print("FATAL_SCANNED_DELTA_REPLAY"); quit; }',
        f'write("NODE_{node:03d}_CHART_DELTA.txt",string(DELTA));',
        f"matrix Y[10][{len(free)}];",
    ]
    for basis_index, free_col in enumerate(free, 1):
        lines.append(f"Y[{free_col},{basis_index}]=DELTA;")
        for position, pivot_col in enumerate(cols, 1):
            replacement = []
            for row in rows:
                for pos2, col in enumerate(cols, 1):
                    replacement.append(f"R[{row},{free_col}]" if pos2 == position
                                       else f"R[{row},{col}]")
            name = f"CR_{basis_index}_{position}"
            lines.append(matrix_literal(name, rank, rank, replacement))
            lines.append(f"Y[{pivot_col},{basis_index}]=-reduce(det({name}),ACTIVE_SB);")
    identity_count = 11 * len(free)
    lines += [
        f'string IDFILE="NODE_{node:03d}_BORDERED_IDENTITIES.tsv";',
        'write(IDFILE,"basis|free_col|residual_row|normal_form");',
        "int identity_count=0; int identity_failures=0;",
    ]
    for basis_index, free_col in enumerate(free, 1):
        for row in range(1, 12):
            expression = "+".join(f"R[{row},{col}]*Y[{col},{basis_index}]"
                                  for col in range(1, 11))
            lines += [
                f"CHECK=reduce({expression},ACTIVE_SB); identity_count=identity_count+1;",
                f'write(IDFILE,"{basis_index}|{free_col}|{row}|"+string(CHECK));',
                "if(CHECK!=0){ identity_failures=identity_failures+1; }",
            ]
    lines += [
        f'print("COMPLETE_BORDERED_IDENTITY_COUNT="+string(identity_count)); print("BORDERED_IDENTITY_FAILURES="+string(identity_failures)); if(identity_count!={identity_count} || identity_failures!=0){{ print("FATAL_BORDERED_IDENTITIES"); quit; }}',
        f"matrix K[105][{len(free)}];",
        "for(i=1;i<=105;i=i+1){ for(j=1;j<=ncols(Y);j=j+1){ CHECK=0; for(k=1;k<=10;k=k+1){ CHECK=reduce(CHECK+C[i,95+k]*Y[k,j],ACTIVE_SB); } K[i,j]=CHECK; } }",
        f'string KFILE="NODE_{node:03d}_ADJUGATE_KERNEL_105.tsv"; write(KFILE,"coordinate|basis|normal_form");',
        'for(i=1;i<=105;i=i+1){ for(j=1;j<=ncols(K);j=j+1){ write(KFILE,string(i)+"|"+string(j)+"|"+string(K[i,j])); } }',
        "int full_count=0; int full_failures=0;",
        "for(i=1;i<=106;i=i+1){ for(j=1;j<=ncols(K);j=j+1){ CHECK=0; for(k=1;k<=105;k=k+1){ CHECK=reduce(CHECK+ORIGINAL[i,k]*K[k,j],ACTIVE_SB); } full_count=full_count+1; if(CHECK!=0){ full_failures=full_failures+1; } } }",
        'print("FULL_106_ROW_KERNEL_REPLAY_COUNT="+string(full_count)); print("FULL_106_ROW_KERNEL_REPLAY_FAILURES="+string(full_failures)); if(full_failures!=0){ print("FATAL_FULL_KERNEL_REPLAY"); quit; }',
        f'string EFILE="NODE_{node:03d}_ENDPOINT_DELTA2_CLEARED_NF.tsv"; write(EFILE,"basis_i|basis_j|normal_form");',
        "int endpoint_count=0; int endpoint_nonzero=0; poly ECOEFF;",
        'for(i=1;i<=ncols(K);i=i+1){ ECOEFF=reduce(K[14,i]*K[72,i]+K[1,i]*K[97,i],ACTIVE_SB); endpoint_count=endpoint_count+1; if(ECOEFF!=0){ endpoint_nonzero=endpoint_nonzero+1; } write(EFILE,string(i)+"|"+string(i)+"|"+string(ECOEFF)); for(j=i+1;j<=ncols(K);j=j+1){ ECOEFF=reduce(K[14,i]*K[72,j]+K[14,j]*K[72,i]+K[1,i]*K[97,j]+K[1,j]*K[97,i],ACTIVE_SB); endpoint_count=endpoint_count+1; if(ECOEFF!=0){ endpoint_nonzero=endpoint_nonzero+1; } write(EFILE,string(i)+"|"+string(j)+"|"+string(ECOEFF)); } }',
        'print("ENDPOINT_QUADRATIC=x14*x72+x1*x97"); print("ENDPOINT_DELTA2_DENOMINATOR_CLEARED=1"); print("ENDPOINT_COEFFICIENT_COUNT="+string(endpoint_count)); print("ENDPOINT_COEFFICIENT_NF_NONZERO_COUNT="+string(endpoint_nonzero));',
        'if(endpoint_nonzero==0){ print("CHART_CLASSIFICATION=ENDPOINT_DEAD_ONLY_ON_D_DELTA"); } else { print("CHART_CLASSIFICATION=RING_LEVEL_SURVIVOR_ON_CHART_PENDING_NILPOTENCE_RADICAL"); }',
        'print("NO_FACTOR_GCD_CONTENT_RADICAL_NORMALIZATION=1");',
        'print("RECURSIVE_ENDPOINT_CHART_COMPLETE=1"); quit;',
        "",
    ]
    return finalize_chart_script(lines)


def run_singular(script: Path, stdout: Path, stderr: Path, result: Path,
                 cap: int) -> int:
    started = time.time()
    with stdout.open("wb") as out, stderr.open("wb") as err:
        process = subprocess.Popen(["Singular", "-q", script.name], cwd=script.parent,
                                   stdout=out, stderr=err,
                                   start_new_session=True)
        try:
            rc = process.wait(timeout=cap)
            timed_out = False
        except subprocess.TimeoutExpired:
            timed_out = True
            os.killpg(process.pid, signal.SIGTERM)
            try:
                rc = process.wait(timeout=15)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                rc = process.wait()
    payload = {
        "argv": ["Singular", "-q", script.name],
        "cap_seconds": cap,
        "elapsed_seconds": round(time.time() - started, 6),
        "returncode": rc,
        "script_sha256": sha256(script),
        "stderr_sha256": sha256(stderr),
        "stdout_sha256": sha256(stdout),
        "timed_out": timed_out,
    }
    result.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    assert_clean_transcript(stdout, stderr)
    return rc


def require_markers(path: Path, markers: tuple[str, ...]) -> str:
    text = path.read_text(errors="replace")
    for marker in markers:
        if marker not in text.splitlines():
            raise RuntimeError(f"MISSING_MARKER:{marker}")
    if "FATAL_" in text:
        raise RuntimeError("FATAL_MARKER_IN_STDOUT")
    return text


def source_inputs(base: Path, component: str):
    source_root = base / "work/prepared/upstream_source/jc2"
    upstream_path = source_root / "cases/ggv_8_28_upper_endpoint_lambda0_quotient_nf_rank_r5_20260828/build_nf_rank.py"
    upstream = load_upstream(upstream_path)
    r1 = source_root / "cases/ggv_8_28_upper_endpoint_lambda0_rank_jump_fitting_census_r1_20260828/build_fitting_census.py"
    matrix = source_root / "cases/ggv_8_28_upper_endpoint_lambda0_endpoint_kernel_components_r1_20260828/input/symbolic_quadratic_q_rankdrop.sing"
    factor_archive = source_root / "cases/ggv_8_28_upper_endpoint_lambda0_endpoint_kernel_strata_r6_20260828/custody/ggv_lambda0_endpoint_strata_p_r6_20260828T140500Z_r6a.tar.gz"
    return upstream.inputs(r1, matrix, factor_archive, component)


def write_summary(output: Path, classification: str, component: str,
                  nodes: list[dict[str, object]], generators: list[str],
                  rank_bound: int) -> None:
    summary = {
        "classification": classification,
        "component": component,
        "nodes": nodes,
        "open_remainder_generators": generators,
        "open_remainder_rank_upper_bound": rank_bound,
        "scope": "EXACT_AMBIENT_QUOTIENT_NF_FINITE_CHART_RECURSION_ONLY",
        "endpoint": "x14*x72+x1*x97",
        "no_radical_nilpotence_or_geometric_inference": True,
    }
    (output / "SUMMARY.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n")
    (output / "VERDICT.txt").write_text(classification + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", required=True, type=Path)
    parser.add_argument("--component", required=True, choices=tuple(COMPONENTS))
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--max-nodes", type=int, default=12)
    parser.add_argument("--stage-cap", type=int, default=900)
    args = parser.parse_args()
    base = args.base.resolve()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    label, initial_bound = COMPONENTS[args.component]
    got_label, zeros, factor, remaining, assignment, counts = source_inputs(
        base, args.component)
    if got_label != label:
        raise SystemExit("COMPONENT_LABEL_DISAGREEMENT")
    rank_provenance = verify_rank_bound(base, args.component, initial_bound)
    root_delta_path = base / f"output/{args.component}/{label}_CHART_DELTA.txt"
    root_classification = base / f"output/{args.component}/CLASSIFICATION.txt"
    if root_classification.read_text().strip() != "ENDPOINT_DEAD_ONLY_ON_D_DELTA":
        raise SystemExit("ROOT_CHART_CLASSIFICATION_DRIFT")
    generators = [clean_poly(factor), clean_poly(root_delta_path.read_text())]
    rank_bound = initial_bound
    nodes: list[dict[str, object]] = []
    input_manifest = {
        "component": args.component,
        "label": label,
        "zeros": zeros,
        "remaining": remaining,
        "root_delta_path": str(root_delta_path),
        "root_delta_sha256": sha256(root_delta_path),
        "root_rank_upper_bound": initial_bound,
        "token_replacements": counts,
        "upstream_sha256": UPSTREAM_SHA,
        "rank_upper_bound_provenance": rank_provenance,
    }
    (output / "INPUT_MANIFEST.json").write_text(
        json.dumps(input_manifest, indent=2, sort_keys=True) + "\n")
    try:
        for node_index in range(1, args.max_nodes + 1):
            node = output / f"node_{node_index:03d}"
            node.mkdir()
            (node / "NODE_INPUT.json").write_text(json.dumps({
                "node": node_index,
                "generators": generators,
                "generator_sha256": [hashlib.sha256(g.encode()).hexdigest()
                                      for g in generators],
                "inherited_rank_upper_bound": rank_bound,
            }, indent=2, sort_keys=True) + "\n")
            reduce_script = node / "reduce.sing"
            reduce_script.write_text(build_reduce_script(
                remaining, generators, node_index, label, assignment))
            reduce_rc = run_singular(reduce_script, node / "reduce.stdout.txt",
                                     node / "reduce.stderr.txt",
                                     node / "reduce.result.json", args.stage_cap)
            if reduce_rc != 0:
                raise RuntimeError(f"REDUCE_RETURN_CODE:{reduce_rc}")
            reduce_text = (node / "reduce.stdout.txt").read_text(errors="replace")
            if "EXACT_EMPTY_NODE=1" in reduce_text.splitlines():
                nodes.append({"node": node_index, "classification": "EXACT_EMPTY_NODE",
                              "rank_upper_bound": rank_bound})
                write_summary(output, "EXACT_ENDPOINT_DEAD_ON_FINITE_GEOMETRIC_CHART_COVER",
                              args.component, nodes, generators, rank_bound)
                return 0
            require_markers(node / "reduce.stdout.txt", (
                "NODE_REDUCER_FIXTURES_PASS=1",
                "NF_RATIONAL_UNIT_PIVOT_COUNT=95",
                "NF_PIVOT_INVARIANT_FAILURES=0",
                "NODE_RESIDUAL_REDUCTION_COMPLETE=1",
                "NODE_REDUCE_COMPLETE=1",
            ))
            residual_path = node / f"NODE_{node_index:03d}_REDUCE_RESIDUAL.tsv"
            pivot_path = node / f"NODE_{node_index:03d}_REDUCE_PIVOTS.tsv"
            residual = read_residual(residual_path)
            rank = -1
            witness_path: Path | None = None
            size_results = []
            for size in range(rank_bound, -1, -1):
                rank_script = node / f"rank_size_{size}.sing"
                census_path = node / f"rank_size_{size}.support.json"
                rank_script.write_text(build_rank_size_script(
                    remaining, generators, node_index, residual, size, census_path))
                stdout = node / f"rank_size_{size}.stdout.txt"
                rc = run_singular(rank_script, stdout,
                                  node / f"rank_size_{size}.stderr.txt",
                                  node / f"rank_size_{size}.result.json",
                                  args.stage_cap)
                if rc != 0:
                    raise RuntimeError(f"RANK_SIZE_RETURN_CODE:{size}:{rc}")
                text = require_markers(stdout, (
                    f"RANK_SIZE={size}",
                    "SUPPORT_REPLAY_FAILURES=0",
                    "RANK_SIZE_CENSUS_COMPLETE=1",
                ))
                found = "RANK_SIZE_WITNESS_FOUND=1" in text.splitlines()
                size_results.append({"size": size, "witness_found": found,
                                     "support": json.loads(census_path.read_text())})
                if found:
                    rank = size
                    witness_path = node / f"NODE_{node_index:03d}_SIZE_{size}_WITNESS.tsv"
                    break
                if "EVERY_MATCHABLE_MINOR_AT_SIZE_NF_ZERO=1" not in text.splitlines():
                    raise RuntimeError(f"MISSING_ZERO_SIZE_CERTIFICATE:{size}")
            if rank < 0 or witness_path is None:
                raise RuntimeError("NO_RANK_WITNESS")
            rows, cols, scanned_delta = read_witness(witness_path, rank)
            saturation_script = node / "saturation.sing"
            saturation_script.write_text(build_saturation_script(
                remaining, generators, node_index, scanned_delta))
            saturation_stdout = node / "saturation.stdout.txt"
            saturation_rc = run_singular(
                saturation_script, saturation_stdout,
                node / "saturation.stderr.txt", node / "saturation.result.json",
                args.stage_cap)
            if saturation_rc != 0:
                raise RuntimeError(f"SATURATION_RETURN_CODE:{saturation_rc}")
            saturation_text = require_markers(saturation_stdout, (
                "NODE_REDUCER_FIXTURES_PASS=1",
                "SATURATION_OBJECT_TYPE=list",
                "SATURATION_OBJECT_SIZE=1",
                "SATURATION_SLOT1_TYPE=ideal",
                "SATURATION_NODE_INCLUSION_FAILURES=0",
                "SATURATION_STABILITY_FAILURES=0",
                "SATURATION_CERTIFICATE_COMPLETE=1",
                "OPEN_SATURATION_AND_CLOSED_SUCCESSOR_COMPLETE=1",
            ))
            saturation_lines = saturation_text.splitlines()
            if sum(line in saturation_lines for line in
                   ("OPEN_CHART_EMPTY=0", "OPEN_CHART_EMPTY=1")) != 1:
                raise RuntimeError("OPEN_CHART_EMPTY_MARKER_CENSUS")
            if sum(line in saturation_lines for line in
                   ("NEXT_REMAINDER_EMPTY=0", "NEXT_REMAINDER_EMPTY=1")) != 1:
                raise RuntimeError("NEXT_REMAINDER_EMPTY_MARKER_CENSUS")
            open_empty = "OPEN_CHART_EMPTY=1" in saturation_lines
            next_empty = "NEXT_REMAINDER_EMPTY=1" in saturation_lines
            if open_empty:
                require_markers(saturation_stdout, (
                    "EMPTY_OPEN_POWER_MEMBERSHIP_CERTIFICATE=1",
                    "PROPER_OPEN_IDEAL_CERTIFICATE=0",
                ))
            else:
                require_markers(saturation_stdout, (
                    "EMPTY_OPEN_POWER_MEMBERSHIP_CERTIFICATE=0",
                    "PROPER_OPEN_IDEAL_CERTIFICATE=1",
                ))
            empty_open_certificate = validate_empty_open_certificate(
                node / f"NODE_{node_index:03d}_EMPTY_OPEN_POWER_CERTIFICATE.txt",
                open_empty)
            delta = scanned_delta
            if open_empty:
                node_result = {
                    "node": node_index,
                    "rank": rank,
                    "rank_upper_bound_in": rank_bound,
                    "rank_size_results": size_results,
                    "delta": delta,
                    "closed_successor_delta_sha256": hashlib.sha256(delta.encode()).hexdigest(),
                    "open_chart_empty_by_saturation": True,
                    "empty_open_power_certificate": empty_open_certificate,
                    "endpoint_nonzero": False,
                    "endpoint_dead": False,
                    "next_remainder_empty": next_empty,
                }
                nodes.append(node_result)
                (node / "NODE_RESULT.json").write_text(
                    json.dumps(node_result, indent=2, sort_keys=True) + "\n")
                if next_empty:
                    write_summary(output,
                                  "EXACT_ENDPOINT_DEAD_ON_FINITE_GEOMETRIC_CHART_COVER",
                                  args.component, nodes, generators + [delta], rank)
                    return 0
                generators.append(delta)
                rank_bound = rank
                continue
            chart_script = node / "chart.sing"
            chart_script.write_text(build_chart_script(
                remaining, generators, node_index, label, assignment, residual,
                rank, rows, cols, scanned_delta))
            chart_rc = run_singular(chart_script, node / "chart.stdout.txt",
                                    node / "chart.stderr.txt",
                                    node / "chart.result.json", args.stage_cap)
            if chart_rc != 0:
                raise RuntimeError(f"CHART_RETURN_CODE:{chart_rc}")
            chart_text = require_markers(node / "chart.stdout.txt", (
                "NODE_REDUCER_FIXTURES_PASS=1",
                "CHART_SATURATION_OBJECT_TYPE=list",
                "CHART_SATURATION_OBJECT_SIZE=1",
                "CHART_SATURATION_SLOT1_TYPE=ideal",
                "CHART_SATURATION_NODE_INCLUSION_FAILURES=0",
                "CHART_SATURATION_STABILITY_FAILURES=0",
                "CHART_OPEN_PROPER_IDEAL_CERTIFICATE=1",
                "OPEN_CHART_SATURATION_PROPER=1",
                "CHART_PIVOT_REDUCER=NODE_SB",
                "CHART_BASE_CHANGE_REDUCTION_COUNT=11135",
                "NODE_TRANSFORM_BASE_CHANGED_TO_ACTIVE_SB=1",
                "NF_RATIONAL_UNIT_PIVOT_COUNT=95",
                "NF_PIVOT_INVARIANT_FAILURES=0",
                "CHART_DELTA_NF_NONZERO=1",
                "SCANNED_DELTA_REPLAY_EQUAL=1",
                "BORDERED_IDENTITY_FAILURES=0",
                "FULL_106_ROW_KERNEL_REPLAY_FAILURES=0",
                "ENDPOINT_DELTA2_DENOMINATOR_CLEARED=1",
                "NO_FACTOR_GCD_CONTENT_RADICAL_NORMALIZATION=1",
                "RECURSIVE_ENDPOINT_CHART_COMPLETE=1",
            ))
            endpoint_nonzero = "CHART_CLASSIFICATION=RING_LEVEL_SURVIVOR_ON_CHART_PENDING_NILPOTENCE_RADICAL" in chart_text.splitlines()
            endpoint_dead = "CHART_CLASSIFICATION=ENDPOINT_DEAD_ONLY_ON_D_DELTA" in chart_text.splitlines()
            delta_path = node / f"NODE_{node_index:03d}_CHART_DELTA.txt"
            saturated_delta = clean_poly(delta_path.read_text())
            node_result = {
                "node": node_index,
                "rank": rank,
                "rank_upper_bound_in": rank_bound,
                "rank_size_results": size_results,
                "delta": delta,
                "closed_successor_delta_sha256": hashlib.sha256(delta.encode()).hexdigest(),
                "saturated_delta_normal_form": saturated_delta,
                "saturated_delta_file_sha256": sha256(delta_path),
                "open_chart_empty_by_saturation": False,
                "empty_open_power_certificate": empty_open_certificate,
                "endpoint_nonzero": endpoint_nonzero,
                "endpoint_dead": endpoint_dead,
                "next_remainder_empty": next_empty,
            }
            nodes.append(node_result)
            (node / "NODE_RESULT.json").write_text(
                json.dumps(node_result, indent=2, sort_keys=True) + "\n")
            if endpoint_nonzero:
                write_summary(output,
                              "RING_LEVEL_SURVIVOR_ON_CHART_PENDING_NILPOTENCE_RADICAL",
                              args.component, nodes, generators, rank)
                return 0
            if not endpoint_dead:
                raise RuntimeError("ENDPOINT_CLASSIFICATION_MISSING")
            if next_empty:
                write_summary(output, "EXACT_ENDPOINT_DEAD_ON_FINITE_GEOMETRIC_CHART_COVER",
                              args.component, nodes, generators + [delta], rank)
                return 0
            generators.append(delta)
            rank_bound = rank
        write_summary(output, "NO_VERDICT_OPEN_REMAINDER", args.component,
                      nodes, generators, rank_bound)
        return 0
    except Exception as exc:
        (output / "ADAPTER_FAILURE.txt").write_text(
            f"{type(exc).__name__}:{exc}\n")
        write_summary(output, "ADAPTER_FAILURE_NO_VERDICT", args.component,
                      nodes, generators, rank_bound)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
