#!/usr/bin/env python3
"""Compile exact rational-unit-pivot Fitting residual census scripts."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import re
import tarfile


ROWS = 106
COLS = 105
PARAMETERS = ("q0", "q1", "q2", "c4", "c6", "c8")
MATRIX_SHA256 = "56f09440c924ba7c32ca15c74e585533ab79023c8dfaf17bc6abd47077132d7c"
R6_ARCHIVE_SHA256 = "cfd2c020b204beecaca5b60ee062aed8a1fe274a399c2ebda93d0d300a00c0f4"
R6_ROOT = "ggv_lambda0_endpoint_strata_p_r6_20260828T140500Z_r6a"
MEMBERS = {
    "c8p": ("output/census/C8P_FACTORS.tsv", "a2002b0695f66ca43e42b58cc253c4de27db645529c9eda2b84a33db602187e8"),
    "q1p": ("output/census/Q1P_FACTORS.tsv", "79120ec6fce795cc1ce49bde672e656e277cfef8c42a351cd18326f59f582ad2"),
    "triple": ("output/census/TRIPLE_FACTORS.tsv", "611530c6c53675fa53a2a5d5e40000205628f326f01c664f822d9e739475185c"),
    "p": ("output/compiled/base/P_EXACT.txt", "e1bccda07823fe3b500244f757b49857de2f1b779e9638a68f3981682e1bd6ea"),
}
LANES = {
    "base_a": ("C8", "Q1"),
    "base_b": ("P", "C8_Q1"),
    "pair": ("C8P02", "Q1P02", "Q1P03"),
    "triple": ("TRIPLE02", "TRIPLE03"),
}
UNIT_FACTOR_EXPECTED = {
    "C8P": ((1, 1, "1"),),
    "Q1P": ((1, 1, "16"),),
    "TRIPLE": ((1, 1, "16"),),
}


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def matrix_assignment(path: Path) -> str:
    if sha256(path) != MATRIX_SHA256:
        raise SystemExit("MATRIX_SOURCE_SHA_MISMATCH")
    text = path.read_text()
    marker = f"matrix M[{ROWS}][{COLS}]="
    start = text.index(marker)
    end = text.index(';\nprint("MATRIX=', start) + 1
    assignment = text[start:end]
    entries = assignment[assignment.index("=") + 1 : -1].split(",\n")
    if len(entries) != ROWS * COLS:
        raise SystemExit(f"MATRIX_ENTRY_COUNT_MISMATCH:{len(entries)}")
    return assignment


def archive_members(path: Path) -> dict[str, str]:
    if sha256(path) != R6_ARCHIVE_SHA256:
        raise SystemExit("R6_ARCHIVE_SHA_MISMATCH")
    result: dict[str, str] = {}
    with tarfile.open(path, "r:gz") as archive:
        names = set(archive.getnames())
        for key, (relative, expected_sha) in MEMBERS.items():
            name = f"{R6_ROOT}/{relative}"
            if name not in names:
                raise SystemExit(f"R6_ARCHIVE_MEMBER_MISSING:{key}")
            extracted = archive.extractfile(name)
            if extracted is None:
                raise SystemExit(f"R6_ARCHIVE_MEMBER_NOT_FILE:{key}")
            data = extracted.read()
            if sha_bytes(data) != expected_sha:
                raise SystemExit(f"R6_ARCHIVE_MEMBER_SHA_MISMATCH:{key}")
            result[key] = data.decode()
    return result


def read_factor_text(text: str, family: str) -> tuple[str, list[tuple[int, int, str]]]:
    raw: str | None = None
    count: int | None = None
    factors: list[tuple[int, int, str]] = []
    for line in text.splitlines():
        fields = line.split("|", 3)
        if len(fields) == 2 and fields[0] == "RAW":
            raw = fields[1].replace(" ", "")
        elif len(fields) == 2 and fields[0] == "COUNT":
            count = int(fields[1])
        elif len(fields) == 4 and fields[0] == "FACTOR":
            factors.append((int(fields[1]), int(fields[2]), fields[3].replace(" ", "")))
        else:
            raise SystemExit(f"FACTOR_CENSUS_PARSE_FAILURE:{family}:{line}")
    if raw is None or count != len(factors):
        raise SystemExit(f"FACTOR_CENSUS_COUNT_FAILURE:{family}")
    units = tuple(item for item in factors if re.fullmatch(r"[+-]?[0-9]+(?:/[0-9]+)?", item[2]))
    if units != UNIT_FACTOR_EXPECTED[family]:
        raise SystemExit(f"UNIT_FACTOR_CENSUS_DISAGREEMENT:{family}:{units}")
    return raw, factors


def replace_token(text: str, variable: str, replacement: str) -> tuple[str, int]:
    pattern = rf"\b{re.escape(variable)}\b"
    count = len(re.findall(pattern, text))
    result = re.sub(pattern, f"({replacement})", text)
    if re.search(pattern, result):
        raise SystemExit(f"TOKEN_REPLACEMENT_FAILED:{variable}")
    return result, count


def specialize(text: str, zeros: tuple[str, ...]) -> tuple[str, dict[str, int]]:
    counts: dict[str, int] = {}
    result = text
    for variable in zeros:
        result, counts[variable] = replace_token(result, variable, "0")
    return result, counts


def unit_reduction_lines(label: str) -> list[str]:
    return [
        "matrix B=M; int step=1; int found; int pi; int pj; int i; int j; int k;",
        "int pivot_count=0; int invariant_failures=0; poly swap_entry; poly multiple; number inverse_unit;",
        f'string pivot_file="{label}_RATIONAL_UNIT_PIVOTS.tsv";',
        f'string residual_file="{label}_RESIDUAL_MATRIX.tsv";',
        'write(pivot_file,"step|source_row|source_col|pivot");',
        f"while(step<={COLS})",
        "{",
        "  found=0; pi=0; pj=0;",
        f"  for(i=step;i<={ROWS} && found==0;i=i+1)",
        "  {",
        f"    for(j=step;j<={COLS} && found==0;j=j+1)",
        "    {",
        "      if(B[i,j]!=0 && deg(B[i,j])==0){ found=1; pi=i; pj=j; }",
        "    }",
        "  }",
        "  if(found==0){ step=" + str(COLS + 1) + "; }",
        "  else",
        "  {",
        f"    for(j=1;j<={COLS};j=j+1){{ swap_entry=B[step,j]; B[step,j]=B[pi,j]; B[pi,j]=swap_entry; }}",
        f"    for(i=1;i<={ROWS};i=i+1){{ swap_entry=B[i,step]; B[i,step]=B[i,pj]; B[i,pj]=swap_entry; }}",
        "    if(B[step,step]==0 || deg(B[step,step])!=0){ invariant_failures=invariant_failures+1; }",
        "    inverse_unit=1/leadcoef(B[step,step]);",
        f"    for(i=step+1;i<={ROWS};i=i+1)",
        "    {",
        "      multiple=B[i,step]*inverse_unit;",
        f"      for(j=step;j<={COLS};j=j+1){{ B[i,j]=B[i,j]-multiple*B[step,j]; }}",
        "    }",
        f"    for(j=step+1;j<={COLS};j=j+1)",
        "    {",
        "      multiple=B[step,j]*inverse_unit;",
        f"      for(i=step;i<={ROWS};i=i+1){{ B[i,j]=B[i,j]-multiple*B[i,step]; }}",
        "    }",
        f"    for(i=1;i<={ROWS};i=i+1){{ if(i!=step && B[i,step]!=0){{ invariant_failures=invariant_failures+1; }} }}",
        f"    for(j=1;j<={COLS};j=j+1){{ if(j!=step && B[step,j]!=0){{ invariant_failures=invariant_failures+1; }} }}",
        "    if(B[step,step]==0 || deg(B[step,step])!=0){ invariant_failures=invariant_failures+1; }",
        '    write(pivot_file,string(step)+"|"+string(pi)+"|"+string(pj)+"|"+string(B[step,step]));',
        "    pivot_count=pivot_count+1; step=step+1;",
        "  }",
        "}",
        f"if(pivot_count>={COLS}){{ print(\"FATAL_NO_RESIDUAL_COLUMNS\"); quit; }}",
        f"int residual_rows={ROWS}-pivot_count; int residual_cols={COLS}-pivot_count;",
        "matrix RESIDUAL[residual_rows][residual_cols];",
        f"for(i=1;i<=residual_rows;i=i+1){{ for(j=1;j<=residual_cols;j=j+1){{ RESIDUAL[i,j]=B[pivot_count+i,pivot_count+j]; }} }}",
        'write(residual_file,"rows|"+string(residual_rows)+"|cols|"+string(residual_cols));',
        'for(i=1;i<=residual_rows;i=i+1){ for(j=1;j<=residual_cols;j=j+1){ write(residual_file,string(i)+"|"+string(j)+"|"+string(RESIDUAL[i,j])); } }',
        "int start_rank=timer; int residual_rank=rank(RESIDUAL); int rank_seconds=timer-start_rank;",
        "int total_rank=pivot_count+residual_rank;",
        f'print("STRATUM_LABEL={label}");',
        'print("RATIONAL_UNIT_PIVOT_COUNT="+string(pivot_count));',
        'print("RESIDUAL_ROWS="+string(residual_rows));',
        'print("RESIDUAL_COLS="+string(residual_cols));',
        'print("RESIDUAL_GENERIC_RANK="+string(residual_rank));',
        'print("TOTAL_GENERIC_RANK="+string(total_rank));',
        'print("RESIDUAL_RANK_SECONDS="+string(rank_seconds));',
        'print("UNIT_PIVOT_INVARIANT_FAILURES="+string(invariant_failures));',
        'if(invariant_failures!=0){ print("FATAL_UNIT_PIVOT_INVARIANT"); quit; }',
        f'if(total_rank<0 || total_rank>{COLS}){{ print("FATAL_RANK_RANGE"); quit; }}',
        'print("UNIT_PIVOT_INVARIANTS_PASS=1");',
        'print("UNIT_PIVOT_CENSUS_COMPLETE=1");',
        "quit;",
        "",
    ]


def script(label: str, assignment: str, zeros: tuple[str, ...], factor: str | None) -> str:
    specialized, counts = specialize(assignment, zeros)
    remaining = [p for p in PARAMETERS if p not in zeros]
    lines = [f"// Exact bounded Fitting residual census for {label}."]
    if factor is None:
        lines.append(f"ring r=0,({','.join(remaining)}),dp;")
    else:
        lines.extend([
            f"ring ambient=0,({','.join(remaining)}),dp;",
            f"poly BRANCH_FACTOR={factor};",
            f'write("{label}_BRANCH_FACTOR.txt",string(BRANCH_FACTOR));',
            "if(BRANCH_FACTOR==0 || deg(BRANCH_FACTOR)==0){ print(\"FATAL_ZERO_OR_UNIT_FACTOR\"); quit; }",
            "ideal BRANCH_IDEAL=BRANCH_FACTOR; ideal BRANCH_SB=std(BRANCH_IDEAL);",
            "poly BRANCH_REMAINDER=reduce(BRANCH_FACTOR,BRANCH_SB);",
            "poly UNIT_REMAINDER=reduce(1,BRANCH_SB);",
            'print("AMBIENT_BRANCH_REDUCER_ZERO="+string(BRANCH_REMAINDER==0));',
            'print("AMBIENT_BRANCH_IDEAL_PROPER="+string(UNIT_REMAINDER!=0));',
            'if(BRANCH_REMAINDER!=0 || UNIT_REMAINDER==0){ print("FATAL_AMBIENT_BRANCH_IDEAL"); quit; }',
            "qring r=BRANCH_SB;",
            "ideal QUOTIENT_DEFINING_IDEAL=ideal(basering);",
            'print("QUOTIENT_DEFINING_IDEAL_NONEMPTY="+string(size(QUOTIENT_DEFINING_IDEAL)>0));',
            'if(size(QUOTIENT_DEFINING_IDEAL)==0){ print("FATAL_QUOTIENT_IDEAL_EMPTY"); quit; }',
        ])
    lines.extend([
        specialized,
        f'print("STRATUM_LABEL_PRE={label}");',
        f'print("ZERO_VARIABLES={",".join(zeros) if zeros else "NONE"}");',
        f'print("TOKEN_REPLACEMENTS={";".join(f"{key}:{value}" for key, value in counts.items())}");',
        'print("ENDPOINT_RESERVED=x14*x72+x1*x97");',
    ])
    lines.extend(unit_reduction_lines(label))
    return "\n".join(lines)


def factor_lookup(members: dict[str, str]) -> tuple[dict[str, str], list[str]]:
    _, c8p = read_factor_text(members["c8p"], "C8P")
    _, q1p = read_factor_text(members["q1p"], "Q1P")
    _, triple = read_factor_text(members["triple"], "TRIPLE")
    p = members["p"].strip().replace(" ", "")
    if not p or "c8" not in p:
        raise SystemExit("P_EXACT_SHAPE_FAILURE")
    factors = {
        "P": p,
        "C8P02": c8p[1][2],
        "Q1P02": q1p[1][2],
        "Q1P03": q1p[2][2],
        "TRIPLE02": triple[1][2],
        "TRIPLE03": triple[2][2],
    }
    if factors["Q1P03"] != "q2" or factors["TRIPLE03"] != "q2":
        raise SystemExit("Q2_FACTOR_DISAGREEMENT")
    empty = [
        "C8P|01|1|1|EMPTY_UNIT_FACTOR",
        "Q1P|01|1|16|EMPTY_UNIT_FACTOR",
        "TRIPLE|01|1|16|EMPTY_UNIT_FACTOR",
    ]
    return factors, empty


def component_spec(label: str, factors: dict[str, str]) -> tuple[tuple[str, ...], str | None]:
    table: dict[str, tuple[tuple[str, ...], str | None]] = {
        "C8": (("c8",), None),
        "Q1": (("q1",), None),
        "P": ((), factors["P"]),
        "C8_Q1": (("c8", "q1"), None),
        "C8P02": (("c8",), factors["C8P02"]),
        "Q1P02": (("q1",), factors["Q1P02"]),
        "Q1P03": (("q1",), factors["Q1P03"]),
        "TRIPLE02": (("q1", "c8"), factors["TRIPLE02"]),
        "TRIPLE03": (("q1", "c8"), factors["TRIPLE03"]),
    }
    return table[label]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--matrix", type=Path, required=True)
    parser.add_argument("--r6-archive", type=Path, required=True)
    parser.add_argument("--lane", choices=sorted(LANES), required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    assignment = matrix_assignment(args.matrix)
    members = archive_members(args.r6_archive)
    factors, empty = factor_lookup(members)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    manifest = ["label|zero_variables|factor_sha256|factor|script"]
    for label in LANES[args.lane]:
        zeros, factor = component_spec(label, factors)
        filename = label.lower() + ".sing"
        content = script(label, assignment, zeros, factor)
        (args.output_dir / filename).write_text(content)
        prefix = content.split("matrix B=M;", 1)[0]
        (args.output_dir / (label.lower() + "_parse.sing")).write_text(
            prefix + f'print("FULL_MATRIX_PARSE_PASS={label}");\nquit;\n'
        )
        fsha = "NONE" if factor is None else sha_bytes(factor.encode())
        manifest.append(f"{label}|{','.join(zeros) if zeros else 'NONE'}|{fsha}|{factor or 'NONE'}|{filename}")
    (args.output_dir / "COMPONENT_MANIFEST.tsv").write_text("\n".join(manifest) + "\n")
    (args.output_dir / "EMPTY_UNIT_FACTORS.tsv").write_text(
        "family|entry|multiplicity|factor|classification\n" + "\n".join(empty) + "\n"
    )
    print(f"MATRIX_SHA256={sha256(args.matrix)}")
    print(f"R6_ARCHIVE_SHA256={sha256(args.r6_archive)}")
    print(f"LANE={args.lane}")
    print(f"COMPONENT_COUNT={len(LANES[args.lane])}")
    print("UNIT_FACTOR_CENSUS_EXACT=1")
    print("FITTING_CENSUS_BUILD_PASS")


if __name__ == "__main__":
    main()

