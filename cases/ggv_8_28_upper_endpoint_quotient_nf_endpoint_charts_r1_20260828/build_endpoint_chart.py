#!/usr/bin/env python3
"""Build exact ambient-NF adjugate endpoint-chart scripts from banked ranks."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
from pathlib import Path


EXPECTED = {
    "p": ("P", 9, "P_SIZE9_RANK_WITNESS.tsv"),
    "c8p02": ("C8P02", 9, "C8P02_SIZE9_RANK_WITNESS.tsv"),
    "q1p02": ("Q1P02", 6, "Q1P02_RANK_WITNESS.tsv"),
    "q1p03": ("Q1P03", 4, "Q1P03_RANK_WITNESS.tsv"),
    "triple02": ("TRIPLE02", 6, "TRIPLE02_RANK_WITNESS.tsv"),
    "triple03": ("TRIPLE03", 4, "TRIPLE03_RANK_WITNESS.tsv"),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_upstream(path: Path):
    expected = "7ba6c106ff62a3bfc289be408d151bda7e85d73cb5868543d86ebe926f272b0a"
    if sha256(path) != expected:
        raise SystemExit("UPSTREAM_BUILD_NF_RANK_SHA_DRIFT")
    spec = importlib.util.spec_from_file_location("banked_nf", path)
    if spec is None or spec.loader is None:
        raise SystemExit("UPSTREAM_IMPORT_FAILURE")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read_witness(path: Path, rank: int):
    lines = path.read_text().splitlines()
    if len(lines) != 2:
        raise SystemExit(f"WITNESS_LINE_CENSUS:{len(lines)}")
    fields = lines[1].split("|", 3)
    if len(fields) != 4:
        raise SystemExit("WITNESS_FIELDS")
    rows = tuple(map(int, fields[1].split(",")))
    cols = tuple(map(int, fields[2].split(",")))
    nf = fields[3].replace(" ", "")
    if len(rows) != rank or len(cols) != rank or nf == "0":
        raise SystemExit("WITNESS_RANK_OR_ZERO")
    if len(set(rows)) != rank or len(set(cols)) != rank:
        raise SystemExit("WITNESS_DUPLICATE_INDEX")
    return rows, cols, nf


def read_residual(path: Path):
    lines = path.read_text().splitlines()
    if lines[0] != "rows|11|cols|10":
        raise SystemExit("RESIDUAL_HEADER")
    matrix = [["0"] * 10 for _ in range(11)]
    seen = set()
    for line in lines[1:]:
        i, j, value = line.split("|", 2)
        key = (int(i), int(j))
        if key in seen or not (1 <= key[0] <= 11 and 1 <= key[1] <= 10):
            raise SystemExit("RESIDUAL_INDEX")
        seen.add(key)
        matrix[key[0] - 1][key[1] - 1] = value.replace(" ", "")
    if len(seen) != 110:
        raise SystemExit("RESIDUAL_CENSUS")
    return matrix


def matrix_literal(name: str, rows: int, cols: int, entries: list[str]) -> str:
    if len(entries) != rows * cols:
        raise ValueError((name, rows, cols, len(entries)))
    return f"matrix {name}[{rows}][{cols}]=" + ",".join(entries) + ";"


def build_script(upstream, component: str, source_root: Path, packet: Path) -> str:
    label, rank, witness_file = EXPECTED[component]
    r1 = source_root / "cases/ggv_8_28_upper_endpoint_lambda0_rank_jump_fitting_census_r1_20260828/build_fitting_census.py"
    matrix = source_root / "cases/ggv_8_28_upper_endpoint_lambda0_endpoint_kernel_components_r1_20260828/input/symbolic_quadratic_q_rankdrop.sing"
    factor_archive = source_root / "cases/ggv_8_28_upper_endpoint_lambda0_endpoint_kernel_strata_r6_20260828/custody/ggv_lambda0_endpoint_strata_p_r6_20260828T140500Z_r6a.tar.gz"
    got_label, zeros, factor, remaining, assignment, counts = upstream.inputs(
        r1, matrix, factor_archive, component)
    if got_label != label:
        raise SystemExit("LABEL_DISAGREEMENT")
    residual_path = packet / f"{label}_NF_RESIDUAL_MATRIX.tsv"
    pivot_path = packet / f"{label}_NF_RATIONAL_UNIT_PIVOTS.tsv"
    witness_path = packet / witness_file
    residual = read_residual(residual_path)
    rows, cols, banked_nf = read_witness(witness_path, rank)
    free = tuple(c for c in range(1, 11) if c not in cols)
    if len(free) != 10 - rank:
        raise SystemExit("FREE_COLUMN_CENSUS")
    p_entries = [f"R[{i},{j}]" for i in rows for j in cols]

    lines = [
        "// Reducer-safe adjugate endpoint chart; generated from frozen banked rank.",
        *upstream.ambient_header(label, factor, remaining),
        assignment,
        "matrix ORIGINAL=M; matrix B=M; matrix C[105][105];",
        "int i; int j; int k; int step=1; int found; int pi; int pj; int pivot_count=0; int invariant_failures=0; int operation_reductions=0;",
        "poly swap_entry; poly multiple; poly CHECK; number inverse_unit;",
        f'string PIVOTFILE="{label}_REPLAY_PIVOTS.tsv"; string RESIDUALFILE="{label}_REPLAY_RESIDUAL.tsv";',
        'write(PIVOTFILE,"step|source_row|source_col|pivot");',
        "for(i=1;i<=105;i=i+1){ C[i,i]=1; }",
        "for(i=1;i<=106;i=i+1){ for(j=1;j<=105;j=j+1){ B[i,j]=reduce(B[i,j],BRANCH_SB); operation_reductions=operation_reductions+1; } }",
        'while(step<=105){ found=0; pi=0; pj=0; for(i=step;i<=106 && found==0;i=i+1){ for(j=step;j<=105 && found==0;j=j+1){ B[i,j]=reduce(B[i,j],BRANCH_SB); operation_reductions=operation_reductions+1; if(B[i,j]!=0 && deg(B[i,j])==0){ found=1; pi=i; pj=j; } } } if(found==0){ step=106; } else { for(j=1;j<=105;j=j+1){ swap_entry=B[step,j]; B[step,j]=B[pi,j]; B[pi,j]=swap_entry; } for(i=1;i<=106;i=i+1){ swap_entry=B[i,step]; B[i,step]=B[i,pj]; B[i,pj]=swap_entry; } for(i=1;i<=105;i=i+1){ swap_entry=C[i,step]; C[i,step]=C[i,pj]; C[i,pj]=swap_entry; } B[step,step]=reduce(B[step,step],BRANCH_SB); operation_reductions=operation_reductions+1; if(B[step,step]==0 || deg(B[step,step])!=0){ invariant_failures=invariant_failures+1; } inverse_unit=1/leadcoef(B[step,step]); for(i=step+1;i<=106;i=i+1){ multiple=reduce(B[i,step]*inverse_unit,BRANCH_SB); operation_reductions=operation_reductions+1; for(j=step;j<=105;j=j+1){ B[i,j]=reduce(B[i,j]-multiple*B[step,j],BRANCH_SB); operation_reductions=operation_reductions+1; } } for(j=step+1;j<=105;j=j+1){ multiple=reduce(B[step,j]*inverse_unit,BRANCH_SB); operation_reductions=operation_reductions+1; for(i=step;i<=106;i=i+1){ B[i,j]=reduce(B[i,j]-multiple*B[i,step],BRANCH_SB); operation_reductions=operation_reductions+1; } for(i=1;i<=105;i=i+1){ C[i,j]=reduce(C[i,j]-multiple*C[i,step],BRANCH_SB); operation_reductions=operation_reductions+1; } } for(i=1;i<=106;i=i+1){ if(i!=step && reduce(B[i,step],BRANCH_SB)!=0){ invariant_failures=invariant_failures+1; } } for(j=1;j<=105;j=j+1){ if(j!=step && reduce(B[step,j],BRANCH_SB)!=0){ invariant_failures=invariant_failures+1; } } write(PIVOTFILE,string(step)+"|"+string(pi)+"|"+string(pj)+"|"+string(B[step,step])); pivot_count=pivot_count+1; step=step+1; } }',
        'print("NF_RATIONAL_UNIT_PIVOT_COUNT="+string(pivot_count)); print("NF_PIVOT_INVARIANT_FAILURES="+string(invariant_failures));',
        'if(pivot_count!=95 || invariant_failures!=0){ print("FATAL_95_PIVOT_REPLAY"); quit; }',
        "matrix R[11][10]; int nf_drift=0;",
        'write(RESIDUALFILE,"rows|11|cols|10");',
        'for(i=1;i<=11;i=i+1){ for(j=1;j<=10;j=j+1){ R[i,j]=reduce(B[95+i,95+j],BRANCH_SB); if(R[i,j]-reduce(R[i,j],BRANCH_SB)!=0){ nf_drift=nf_drift+1; } write(RESIDUALFILE,string(i)+"|"+string(j)+"|"+string(R[i,j])); } }',
        'if(nf_drift!=0){ print("FATAL_RESIDUAL_NF_DRIFT"); quit; }',
        matrix_literal("PIVOT_MINOR", rank, rank, p_entries),
        "poly DELTA_RAW=det(PIVOT_MINOR); poly DELTA=reduce(DELTA_RAW,BRANCH_SB);",
        f"poly BANKED_DELTA={banked_nf};",
        'print("CHART_DELTA_NF_NONZERO="+string(DELTA!=0)); print("BANKED_DELTA_REPLAY_EQUAL="+string(DELTA==BANKED_DELTA));',
        'if(DELTA==0 || DELTA!=BANKED_DELTA){ print("FATAL_BANKED_DELTA_REPLAY"); quit; }',
        f'write("{label}_CHART_DELTA.txt",string(DELTA));',
        f"matrix Y[10][{len(free)}];",
    ]

    for basis_index, free_col in enumerate(free, 1):
        lines.append(f"Y[{free_col},{basis_index}]=DELTA;")
        for position, pivot_col in enumerate(cols, 1):
            replacement = []
            for rr in rows:
                for pos2, cc in enumerate(cols, 1):
                    replacement.append(f"R[{rr},{free_col}]" if pos2 == position
                                       else f"R[{rr},{cc}]")
            name = f"CR_{basis_index}_{position}"
            lines.append(matrix_literal(name, rank, rank, replacement))
            lines.append(f"Y[{pivot_col},{basis_index}]=-reduce(det({name}),BRANCH_SB);")

    identity_count = 11 * len(free)
    lines.extend([
        f'string IDFILE="{label}_BORDERED_RPLUS1_IDENTITIES.tsv";',
        'write(IDFILE,"basis|free_col|residual_row|normal_form");',
        "int identity_failures=0; int identity_count=0;",
    ])
    for basis_index, free_col in enumerate(free, 1):
        for rr in range(1, 12):
            expression = "+".join(f"R[{rr},{cc}]*Y[{cc},{basis_index}]"
                                  for cc in range(1, 11))
            lines.extend([
                f"CHECK=reduce({expression},BRANCH_SB); identity_count=identity_count+1;",
                f'write(IDFILE,"{basis_index}|{free_col}|{rr}|"+string(CHECK));',
                "if(CHECK!=0){ identity_failures=identity_failures+1; }",
            ])
    lines.extend([
        f'print("COMPLETE_BORDERED_RPLUS1_IDENTITY_COUNT="+string(identity_count)); print("BORDERED_RPLUS1_IDENTITY_FAILURES="+string(identity_failures));',
        f'if(identity_count!={identity_count} || identity_failures!=0){{ print("FATAL_BORDERED_RPLUS1_IDENTITY"); quit; }}',
        f"matrix K[105][{len(free)}];",
        "for(i=1;i<=105;i=i+1){ for(j=1;j<=ncols(Y);j=j+1){ CHECK=0; for(k=1;k<=10;k=k+1){ CHECK=reduce(CHECK+C[i,95+k]*Y[k,j],BRANCH_SB); } K[i,j]=CHECK; } }",
        f'string KFILE="{label}_ADJUGATE_RIGHT_KERNEL_105.tsv"; write(KFILE,"coordinate|basis|normal_form");',
        "for(i=1;i<=105;i=i+1){ for(j=1;j<=ncols(K);j=j+1){ write(KFILE,string(i)+\"|\"+string(j)+\"|\"+string(K[i,j])); } }",
        "int full_replay_failures=0; int full_replay_count=0;",
        "for(i=1;i<=106;i=i+1){ for(j=1;j<=ncols(K);j=j+1){ CHECK=0; for(k=1;k<=105;k=k+1){ CHECK=reduce(CHECK+ORIGINAL[i,k]*K[k,j],BRANCH_SB); } full_replay_count=full_replay_count+1; if(CHECK!=0){ full_replay_failures=full_replay_failures+1; } } }",
        'print("FULL_106_ROW_KERNEL_REPLAY_COUNT="+string(full_replay_count)); print("FULL_106_ROW_KERNEL_REPLAY_FAILURES="+string(full_replay_failures));',
        'if(full_replay_failures!=0){ print("FATAL_FULL_KERNEL_REPLAY"); quit; }',
        f'string EFILE="{label}_ENDPOINT_DELTA2_CLEARED_NF.tsv"; write(EFILE,"basis_i|basis_j|normal_form");',
        "int endpoint_count=0; int endpoint_nonzero=0; poly ECOEFF;",
        "for(i=1;i<=ncols(K);i=i+1){ ECOEFF=reduce(K[14,i]*K[72,i]+K[1,i]*K[97,i],BRANCH_SB); endpoint_count=endpoint_count+1; if(ECOEFF!=0){ endpoint_nonzero=endpoint_nonzero+1; } write(EFILE,string(i)+\"|\"+string(i)+\"|\"+string(ECOEFF)); for(j=i+1;j<=ncols(K);j=j+1){ ECOEFF=reduce(K[14,i]*K[72,j]+K[14,j]*K[72,i]+K[1,i]*K[97,j]+K[1,j]*K[97,i],BRANCH_SB); endpoint_count=endpoint_count+1; if(ECOEFF!=0){ endpoint_nonzero=endpoint_nonzero+1; } write(EFILE,string(i)+\"|\"+string(j)+\"|\"+string(ECOEFF)); } }",
        'print("ENDPOINT_QUADRATIC=x14*x72+x1*x97"); print("ENDPOINT_DELTA2_DENOMINATOR_CLEARED=1"); print("ENDPOINT_COEFFICIENT_COUNT="+string(endpoint_count)); print("ENDPOINT_COEFFICIENT_NF_NONZERO_COUNT="+string(endpoint_nonzero));',
        'if(endpoint_nonzero==0){ print("CHART_CLASSIFICATION=ENDPOINT_DEAD_ONLY_ON_D_DELTA"); } else { print("CHART_CLASSIFICATION=RING_LEVEL_SURVIVOR_ONLY_PENDING_NILPOTENCE_RADICAL"); }',
        "ideal COMPLEMENT_IDEAL=BRANCH_FACTOR,DELTA; ideal COMPLEMENT_SB=std(COMPLEMENT_IDEAL); poly COMPLEMENT_UNIT_NF=reduce(1,COMPLEMENT_SB);",
        f'write("{label}_COMPLEMENT_STANDARD_BASIS.txt",string(COMPLEMENT_SB));',
        'print("CHART_COMPLEMENT_IDEAL_ADDED=1"); print("CHART_COMPLEMENT_EMPTY="+string(COMPLEMENT_UNIT_NF==0));',
        'if(COMPLEMENT_UNIT_NF!=0){ print("COMPLEMENT_CLASSIFICATION=NO_VERDICT_COMPLEMENT_RECURSION_REQUIRED"); } else { print("COMPLEMENT_CLASSIFICATION=EXACT_EMPTY_COMPLEMENT"); }',
        'print("NO_RADICAL_NILPOTENCE_OR_GEOMETRIC_INFERENCE=1");',
        'print("REDUCER_SAFE_ENDPOINT_CHART_COMPLETE=1"); quit;',
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", required=True, type=Path)
    parser.add_argument("--packet", required=True, type=Path)
    parser.add_argument("--component", required=True, choices=tuple(EXPECTED))
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    upstream_path = args.source_root / "cases/ggv_8_28_upper_endpoint_lambda0_quotient_nf_rank_r5_20260828/build_nf_rank.py"
    upstream = load_upstream(upstream_path)
    script = build_script(upstream, args.component, args.source_root,
                          args.packet)
    args.output.write_text(script)
    print(f"COMPONENT={args.component}")
    print(f"SCRIPT_SHA256={hashlib.sha256(script.encode()).hexdigest()}")
    print("ENDPOINT_CHART_BUILD_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
