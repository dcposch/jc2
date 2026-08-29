#!/usr/bin/env python3
"""Build exact right-kernel/endpoint scripts for the three rank-drop factors."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import re


ROWS = 106
COLS = 105
SOURCE_SHA256 = "56f09440c924ba7c32ca15c74e585533ab79023c8dfaf17bc6abd47077132d7c"
FITTING_SHA256 = "d9df4dd576ad4219ac24f52196945760a52989b86a888d31e6e09a8adc2a31ec"
SAMPLES = (
    ("01", (1, 1, 0, 1, 1)),
    ("02", (1, 1, 1, 1, 1)),
    ("03", (1, 2, 1, 1, 1)),
    ("04", (2, 1, 1, 1, 1)),
    ("05", (1, 1, 2, 2, 1)),
    ("06", (2, 3, 1, 1, 2)),
)


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
    entries = assignment[assignment.index("=") + 1 : -1].split(",\n")
    if len(entries) != ROWS * COLS:
        raise SystemExit(f"ENTRY_COUNT_MISMATCH:{len(entries)}")
    return assignment


def declaration(text: str, name: str) -> str:
    marker = f"poly {name}="
    start = text.index(marker)
    end = text.index(";", start) + 1
    return text[start:end]


def specialize_assignment(assignment: str, parameter: str) -> tuple[str, int]:
    pattern = rf"\b{re.escape(parameter)}\b"
    count = len(re.findall(pattern, assignment))
    if count == 0:
        raise SystemExit(f"SPECIALIZATION_TOKEN_MISSING:{parameter}")
    result = re.sub(pattern, "(0)", assignment)
    if re.search(pattern, result):
        raise SystemExit(f"SPECIALIZATION_TOKEN_REMAINS:{parameter}")
    return result, count


def generic_component(name: str, zero_parameter: str, assignment: str) -> list[str]:
    specialized, count = specialize_assignment(assignment, zero_parameter)
    parameters = ["q0", "q1", "q2", "c4", "c6", "c8"]
    parameters.remove(zero_parameter)
    ring_parameters = ",".join(parameters)
    return [
        f"// Exact generic right kernel on {zero_parameter}=0.",
        f"ring r=(0,{ring_parameters}),(z),dp;",
        specialized,
        f'print("COMPONENT={name} ZERO_PARAMETER={zero_parameter} TOKEN_REPLACEMENTS={count}");',
        "int start_kernel=timer; module K=syz(module(M)); matrix KM=matrix(K);",
        "int kernel_dim=ncols(KM);",
        'print("RIGHT_KERNEL_SECONDS="+string(timer-start_kernel));',
        'print("RIGHT_KERNEL_ROWS="+string(nrows(KM))+" DIMENSION="+string(kernel_dim));',
        'if(nrows(KM)!=105 || kernel_dim<1){ print("FATAL_RIGHT_KERNEL_DIMENSION"); quit; }',
        "matrix right_replay=M*KM; int replay_zero=(size(module(right_replay))==0);",
        'print("RIGHT_KERNEL_REPLAY_ZERO="+string(replay_zero));',
        'string kernelfile="'+name+'_RIGHT_KERNEL_FIELD.tsv"; string endpointfile="'+name+'_ENDPOINT_PULLBACK_FIELD.tsv";',
        "int i; int j; number kij; number qcoeff; int endpoint_nonzero=0; int endpoint_coefficients=0;",
        'for(i=1;i<=105;i=i+1){ for(j=1;j<=kernel_dim;j=j+1){ kij=leadcoef(KM[i,j]); write(kernelfile,string(i)+"|"+string(j)+"|"+string(kij)); } }',
        "for(i=1;i<=kernel_dim;i=i+1){ qcoeff=leadcoef(KM[14,i])*leadcoef(KM[72,i])+leadcoef(KM[1,i])*leadcoef(KM[97,i]); endpoint_coefficients=endpoint_coefficients+1; if(qcoeff!=0){ endpoint_nonzero=endpoint_nonzero+1; } write(endpointfile,string(i)+\"|\"+string(i)+\"|\"+string(qcoeff)); for(j=i+1;j<=kernel_dim;j=j+1){ qcoeff=leadcoef(KM[14,i])*leadcoef(KM[72,j])+leadcoef(KM[14,j])*leadcoef(KM[72,i])+leadcoef(KM[1,i])*leadcoef(KM[97,j])+leadcoef(KM[1,j])*leadcoef(KM[97,i]); endpoint_coefficients=endpoint_coefficients+1; if(qcoeff!=0){ endpoint_nonzero=endpoint_nonzero+1; } write(endpointfile,string(i)+\"|\"+string(j)+\"|\"+string(qcoeff)); } }",
        'print("ENDPOINT_QUADRATIC=x14*x72+x1*x97");',
        'print("ENDPOINT_PULLBACK_COEFFICIENTS="+string(endpoint_coefficients));',
        'print("ENDPOINT_PULLBACK_NONZERO_COEFFICIENTS="+string(endpoint_nonzero));',
        'print("COMPONENT_EXACT_KERNEL_PASS="+string(replay_zero));',
        'if(replay_zero && endpoint_nonzero>0){ print("COMPONENT_GENERIC_ENDPOINT_SURVIVOR=1"); } else { if(replay_zero){ print("COMPONENT_GENERIC_ENDPOINT_DEAD=1"); } }',
        "quit;",
        "",
    ]


def substitute_lines(target: str, values: tuple[int, int, int, int, int]) -> list[str]:
    names = ("q0", "q1", "q2", "c4", "c6")
    return [f"{target}=subst({target},{name},{value});" for name, value in zip(names, values)]


def p_sample(
    sample_id: str,
    values: tuple[int, int, int, int, int],
    assignment: str,
    raw_content: str,
    raw_81: str,
    raw_93: str,
) -> list[str]:
    q0v, q1v, q2v, c4v, c6v = values
    lines = [
        f"// Exact rational sample {sample_id} on the irreducible P=0 factor.",
        "ring P=0,(q0,q1,q2,c4,c6,c8),dp;",
        assignment,
        raw_content,
        raw_81,
        raw_93,
        "list FACTOR_LIST=factorize(RAW_CONTENT,1); ideal CONTENT_FACTORS=FACTOR_LIST[1]; matrix FACTOR_MATRIX=matrix(CONTENT_FACTORS);",
        "int factor_count=ncols(FACTOR_MATRIX); int i; int j; int p_factor_count=0; poly PF=0; poly candidate;",
        "for(i=1;i<=factor_count;i=i+1){ candidate=FACTOR_MATRIX[1,i]; if(deg(candidate)>1){ PF=candidate; p_factor_count=p_factor_count+1; } }",
        'print("CONTENT_DISTINCT_FACTOR_COUNT="+string(factor_count)+" P_FACTOR_COUNT="+string(p_factor_count));',
        'if(factor_count!=3 || p_factor_count!=1){ print("FATAL_P_FACTOR_SELECTION"); quit; }',
        "poly P0=subst(PF,c8,0); poly P1=subst(PF,c8,1)-P0;",
        'if(PF!=P0+c8*P1){ print("FATAL_P_NOT_LINEAR_IN_C8"); quit; }',
        "poly P0v=P0; poly P1v=P1;",
    ]
    lines.extend(substitute_lines("P0v", values))
    lines.extend(substitute_lines("P1v", values))
    lines.extend([
        'if(P1v==0){ print("P_SAMPLE_DENOMINATOR_ZERO=1"); quit; }',
        "number c8v=-leadcoef(P0v)/leadcoef(P1v);",
        "matrix MS=M;",
    ])
    lines.extend(substitute_lines("MS", values))
    lines.extend([
        "MS=subst(MS,c8,c8v);",
        "poly pcheck=PF; poly m81check=RAW_MINOR_81; poly m93check=RAW_MINOR_93;",
    ])
    lines.extend(substitute_lines("pcheck", values))
    lines.extend(substitute_lines("m81check", values))
    lines.extend(substitute_lines("m93check", values))
    lines.extend([
        "pcheck=subst(pcheck,c8,c8v); m81check=subst(m81check,c8,c8v); m93check=subst(m93check,c8,c8v);",
        "int on_component=(pcheck==0 && m81check==0 && m93check==0 && c8v!=0);",
        f'print("P_SAMPLE_ID={sample_id} q0={q0v} q1={q1v} q2={q2v} c4={c4v} c6={c6v} c8="+string(c8v));',
        'print("P_SAMPLE_ON_COMPONENT_AWAY_C8_Q1="+string(on_component));',
        'if(!on_component){ print("P_SAMPLE_OFF_COMPONENT"); quit; }',
        "int start_kernel=timer; module K=syz(module(MS)); matrix KM=matrix(K); int kernel_dim=ncols(KM);",
        'print("P_SAMPLE_RIGHT_KERNEL_SECONDS="+string(timer-start_kernel));',
        'print("P_SAMPLE_RIGHT_KERNEL_DIMENSION="+string(kernel_dim));',
        'if(nrows(KM)!=105 || kernel_dim<1){ print("FATAL_P_SAMPLE_KERNEL_DIMENSION"); quit; }',
        "matrix replay=MS*KM; int replay_zero=(size(module(replay))==0);",
        'string kernelfile="P_SAMPLE_'+sample_id+'_RIGHT_KERNEL.tsv"; string endpointfile="P_SAMPLE_'+sample_id+'_ENDPOINT_PULLBACK.tsv";',
        "number kij; number qcoeff; int endpoint_nonzero=0; int endpoint_coefficients=0;",
        'for(i=1;i<=105;i=i+1){ for(j=1;j<=kernel_dim;j=j+1){ kij=leadcoef(KM[i,j]); write(kernelfile,string(i)+"|"+string(j)+"|"+string(kij)); } }',
        "for(i=1;i<=kernel_dim;i=i+1){ qcoeff=leadcoef(KM[14,i])*leadcoef(KM[72,i])+leadcoef(KM[1,i])*leadcoef(KM[97,i]); endpoint_coefficients=endpoint_coefficients+1; if(qcoeff!=0){ endpoint_nonzero=endpoint_nonzero+1; } write(endpointfile,string(i)+\"|\"+string(i)+\"|\"+string(qcoeff)); for(j=i+1;j<=kernel_dim;j=j+1){ qcoeff=leadcoef(KM[14,i])*leadcoef(KM[72,j])+leadcoef(KM[14,j])*leadcoef(KM[72,i])+leadcoef(KM[1,i])*leadcoef(KM[97,j])+leadcoef(KM[1,j])*leadcoef(KM[97,i]); endpoint_coefficients=endpoint_coefficients+1; if(qcoeff!=0){ endpoint_nonzero=endpoint_nonzero+1; } write(endpointfile,string(i)+\"|\"+string(j)+\"|\"+string(qcoeff)); } }",
        'print("P_SAMPLE_RIGHT_KERNEL_REPLAY_ZERO="+string(replay_zero));',
        'print("P_SAMPLE_ENDPOINT_NONZERO_COEFFICIENTS="+string(endpoint_nonzero));',
        'if(replay_zero && endpoint_nonzero>0){ print("P_SAMPLE_ENDPOINT_SURVIVOR=1"); } else { if(replay_zero){ print("P_SAMPLE_ENDPOINT_DEAD=1"); } }',
        "quit;",
        "",
    ])
    return lines


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--fitting", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    assignment = matrix_assignment(args.source)
    if sha256(args.fitting) != FITTING_SHA256:
        raise SystemExit("FITTING_SHA_MISMATCH")
    fitting = args.fitting.read_text()
    raw_content = declaration(fitting, "RAW_CONTENT")
    raw_81 = declaration(fitting, "RAW_MINOR_81")
    raw_93 = declaration(fitting, "RAW_MINOR_93")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for name, parameter in (("C8", "c8"), ("Q1", "q1")):
        lines = generic_component(name, parameter, assignment)
        (args.output_dir / f"component_{name.lower()}.sing").write_text("\n".join(lines))
        parse_lines = lines[:3] + [f'print("FULL_MATRIX_PARSE_PASS COMPONENT={name}");', "quit;", ""]
        (args.output_dir / f"parse_{name.lower()}.sing").write_text("\n".join(parse_lines))
    for sample_id, values in SAMPLES:
        lines = p_sample(sample_id, values, assignment, raw_content, raw_81, raw_93)
        (args.output_dir / f"p_sample_{sample_id}.sing").write_text("\n".join(lines))
    p_parse = ["ring P=0,(q0,q1,q2,c4,c6,c8),dp;", assignment,
               'print("FULL_MATRIX_PARSE_PASS COMPONENT=P");', "quit;", ""]
    (args.output_dir / "parse_p.sing").write_text("\n".join(p_parse))
    print(f"SOURCE_SHA256={sha256(args.source)}")
    print(f"FITTING_SHA256={sha256(args.fitting)}")
    print(f"MATRIX_ENTRIES={ROWS * COLS}")
    print("COMPONENT_SCRIPTS=C8,Q1,P_SAMPLES_01_06")


if __name__ == "__main__":
    main()

