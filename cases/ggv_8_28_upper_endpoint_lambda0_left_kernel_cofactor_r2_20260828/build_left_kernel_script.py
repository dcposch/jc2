#!/usr/bin/env python3
"""Build the exact Singular left-cofactor job from the frozen matrix source."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


SOURCE_SHA256 = "56f09440c924ba7c32ca15c74e585533ab79023c8dfaf17bc6abd47077132d7c"
ROWS = 106
COLS = 105
ENTRY_COUNT = ROWS * COLS


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def matrix_assignment(source: Path) -> str:
    if sha256(source) != SOURCE_SHA256:
        raise SystemExit("SOURCE_SHA_MISMATCH")
    text = source.read_text()
    marker = f"matrix M[{ROWS}][{COLS}]="
    start = text.index(marker)
    end = text.index(';\nprint("MATRIX=', start) + 1
    assignment = text[start:end]
    body = assignment[assignment.index("=") + 1 : -1]
    entries = body.split(",\n")
    if len(entries) != ENTRY_COUNT:
        raise SystemExit(f"ENTRY_COUNT_MISMATCH:{len(entries)}")
    return assignment


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--parse-output", type=Path, required=True)
    args = parser.parse_args()
    assignment = matrix_assignment(args.source)
    header = [
        "// Exact calibrated left-cofactor extraction; no full Groebner basis.",
        "ring r=(0,q0,q1,q2,c4,c6,c8),(z),dp;",
        assignment,
    ]
    parse_lines = header + [
        f'print("FULL_MATRIX_PARSE_PASS ROWS={ROWS} COLS={COLS}");',
        "quit;",
        "",
    ]
    args.parse_output.parent.mkdir(parents=True, exist_ok=True)
    args.parse_output.write_text("\n".join(parse_lines))

    run_lines = header + [
        f'print("MATRIX={ROWS}x{COLS}");',
        "int start_left=timer;",
        "module S=syz(module(transpose(M)));",
        "matrix SM=matrix(S);",
        'print("LEFT_SYZYGY_SECONDS="+string(timer-start_left));',
        'print("LEFT_SYZYGY_GENERATORS="+string(size(S))+" ROWS="+string(nrows(SM))+" COLS="+string(ncols(SM)));',
        "if(size(S)!=1 || nrows(SM)!=106 || ncols(SM)!=1){ print(\"FATAL_LEFT_SYZYGY_DIMENSION\"); quit; }",
        "int i; int j; int k; int o=0;",
        "for(i=106;i>=1;i=i-1){ if(o==0 && SM[i,1]!=0){ o=i; } }",
        'if(o==0){ print("FATAL_ZERO_LEFT_SYZYGY"); quit; }',
        'print("OMITTED_ROW="+string(o));',
        "matrix B[105][105]; int bi=0;",
        "for(i=1;i<=106;i=i+1){ if(i!=o){ bi=bi+1; for(j=1;j<=105;j=j+1){ B[bi,j]=M[i,j]; } } }",
        "int start_det=timer;",
        'poly det_poly=det(B,"SBareiss");',
        'print("DET_SECONDS="+string(timer-start_det));',
        'if(det_poly==0){ print("FATAL_SELECTED_MINOR_ZERO"); quit; }',
        "number Delta=leadcoef(det_poly);",
        'if(denominator(Delta)!=1){ print("FATAL_DELTA_DENOMINATOR"); quit; }',
        "number so=leadcoef(SM[o,1]);",
        'if(so==0){ print("FATAL_OMITTED_COMPONENT_ZERO"); quit; }',
        "number scale=Delta/so;",
        "matrix ell[106][1]; number li; int bad_den=0; int nonzero_minors=0;",
        "for(i=1;i<=106;i=i+1){ ell[i,1]=scale*SM[i,1]; li=leadcoef(ell[i,1]); if(denominator(li)!=1){ bad_den=bad_den+1; } if(li!=0){ nonzero_minors=nonzero_minors+1; } }",
        'print("RAW_DENOMINATOR_FAILURES="+string(bad_den));',
        'print("RAW_NONZERO_MINORS="+string(nonzero_minors));',
        'print("OMITTED_CALIBRATION="+string(leadcoef(ell[o,1])==Delta));',
        "matrix left_replay=transpose(ell)*M;",
        'int left_zero=(size(module(left_replay))==0);',
        'print("LEFT_KERNEL_REPLAY_ZERO="+string(left_zero));',
        'print("RAW_DENOMINATORS_ONE="+string(bad_den==0));',
        "int start_dual=timer;",
        "matrix endpoint_targets[105][2]; endpoint_targets[14,1]=1; endpoint_targets[1,2]=1;",
        "module row_basis=module(transpose(B)); module target_module=module(endpoint_targets);",
        "matrix C=lift(row_basis,target_module);",
        "matrix Craw=Delta*C;",
        "int dual_den_fail=0; number ui;",
        "for(i=1;i<=105;i=i+1){ for(k=1;k<=2;k=k+1){ ui=leadcoef(Craw[i,k]); if(denominator(ui)!=1){ dual_den_fail=dual_den_fail+1; } } }",
        "matrix U[106][2]; bi=0;",
        "for(i=1;i<=106;i=i+1){ if(i!=o){ bi=bi+1; U[i,1]=Craw[bi,1]; U[i,2]=Craw[bi,2]; } }",
        "matrix dual_target[2][105]; dual_target[1,14]=Delta; dual_target[2,1]=Delta;",
        "matrix dual_replay=transpose(U)*M-dual_target;",
        'int dual_zero=(size(module(dual_replay))==0);',
        'print("ENDPOINT_DUAL_SECONDS="+string(timer-start_dual));',
        'print("ENDPOINT_DUAL_DENOMINATOR_FAILURES="+string(dual_den_fail));',
        'print("ENDPOINT_DUAL_REPLAY_ZERO="+string(dual_zero));',
        'string rawfile="LEFT_KERNEL_RAW.sing"; string rawtsv="LEFT_KERNEL_RAW.tsv"; string dualtsv="ENDPOINT_DUALS_RAW.tsv";',
        'write(rawfile,"// Raw calibrated signed maximal minors; do not content-cancel.");',
        'write(rawfile,"ring P=0,(q0,q1,q2,c4,c6,c8),dp;");',
        'write(rawfile,"int OMITTED_ROW="+string(o)+";");',
        'write(rawfile,"poly DELTA="+string(numerator(Delta))+";");',
        'write(rawfile,"ideal LEFT_MINORS=");',
        'for(i=1;i<=106;i=i+1){ li=leadcoef(ell[i,1]); if(i<106){ write(rawfile,string(numerator(li))+","); } else { write(rawfile,string(numerator(li))+";"); } write(rawtsv,string(i)+"\\t"+string(numerator(li))); }',
        'write(rawfile,"matrix ENDPOINT_DUALS[106][2]=");',
        'for(i=1;i<=106;i=i+1){ for(k=1;k<=2;k=k+1){ ui=leadcoef(U[i,k]); if(i==106 && k==2){ write(rawfile,string(numerator(ui))+";"); } else { write(rawfile,string(numerator(ui))+","); } write(dualtsv,string(i)+"\\t"+string(k)+"\\t"+string(numerator(ui))); } }',
        'write(rawfile,"// Columns certify DELTA*x14 and DELTA*x1 respectively.");',
        'write(rawfile,"// Therefore DELTA*(x14*x72+x1*x97) is a linear-row combination.");',
        'int pass=(left_zero && bad_den==0 && leadcoef(ell[o,1])==Delta && dual_zero && dual_den_fail==0);',
        'print("LEFT_KERNEL_CERTIFICATE_PASS="+string(pass));',
        "quit;",
        "",
    ]
    args.output.write_text("\n".join(run_lines))
    print(f"SOURCE_SHA256={sha256(args.source)}")
    print(f"MATRIX_ENTRIES={ENTRY_COUNT}")
    print(f"WROTE={args.output}")
    print(f"WROTE_PARSE={args.parse_output}")


if __name__ == "__main__":
    main()
