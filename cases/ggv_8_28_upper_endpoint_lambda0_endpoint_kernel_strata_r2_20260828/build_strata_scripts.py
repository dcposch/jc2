#!/usr/bin/env python3
"""Compile exact endpoint-on-kernel scripts for P and its intersections.

The compiler performs only textual, hash-pinned transformations.  Singular
does every factorization, syzygy, quotient-ring reduction, and exact replay.
"""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import re


ROWS = 106
COLS = 105
MATRIX_SHA256 = "56f09440c924ba7c32ca15c74e585533ab79023c8dfaf17bc6abd47077132d7c"
FITTING_SHA256 = "d9df4dd576ad4219ac24f52196945760a52989b86a888d31e6e09a8adc2a31ec"
CONTENT_SHA256 = "8359a8d4875e764ea67855dd34614c95d52e5f91f2506f159de0adf22369aa4e"
PARAMETERS = ("q0", "q1", "q2", "c4", "c6", "c8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sha_text(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def declaration(text: str, name: str) -> str:
    marker = f"poly {name}="
    start = text.index(marker)
    end = text.index(";", start) + 1
    return text[start:end]


def matrix_assignment(source: Path) -> str:
    if sha256(source) != MATRIX_SHA256:
        raise SystemExit("MATRIX_SOURCE_SHA_MISMATCH")
    text = source.read_text()
    marker = f"matrix M[{ROWS}][{COLS}]="
    start = text.index(marker)
    end = text.index(';\nprint("MATRIX=', start) + 1
    assignment = text[start:end]
    entries = assignment[assignment.index("=") + 1 : -1].split(",\n")
    if len(entries) != ROWS * COLS:
        raise SystemExit(f"MATRIX_ENTRY_COUNT_MISMATCH:{len(entries)}")
    return assignment


def exact_p(content_path: Path) -> str:
    if sha256(content_path) != CONTENT_SHA256:
        raise SystemExit("CONTENT_SOURCE_SHA_MISMATCH")
    line = next(
        value for value in content_path.read_text().splitlines()
        if value.startswith("CONTENT_FACTOR_DATA=")
    )
    factors = line.split("=", 1)[1].split(",")
    if len(factors) != 3 or set(factors) & {"c8", "q1"} != {"c8", "q1"}:
        raise SystemExit("CONTENT_FACTOR_DATA_SHAPE_MISMATCH")
    candidates = [factor for factor in factors if factor not in {"c8", "q1"}]
    if len(candidates) != 1:
        raise SystemExit("P_FACTOR_SELECTION_MISMATCH")
    return candidates[0]


def signed_terms(poly: str) -> list[tuple[str, str]]:
    if not poly:
        return []
    terms: list[tuple[str, str]] = []
    start = 0
    sign = "+"
    if poly[0] in "+-":
        sign = poly[0]
        start = 1
    index = start
    while index <= len(poly):
        if index == len(poly) or poly[index] in "+-":
            body = poly[start:index]
            if not body:
                raise SystemExit("EMPTY_POLYNOMIAL_TERM")
            terms.append((sign, body))
            if index == len(poly):
                break
            sign = poly[index]
            start = index + 1
        index += 1
    return terms


def render_terms(terms: list[tuple[str, str]]) -> str:
    if not terms:
        return "0"
    chunks: list[str] = []
    for index, (sign, body) in enumerate(terms):
        if index == 0:
            chunks.append(("-" if sign == "-" else "") + body)
        else:
            chunks.append(sign + body)
    return "".join(chunks)


def linear_parts(poly: str, variable: str) -> tuple[str, str] | None:
    constant: list[tuple[str, str]] = []
    coefficient: list[tuple[str, str]] = []
    for sign, body in signed_terms(poly.replace(" ", "")):
        tokens = body.split("*")
        hits = [index for index, token in enumerate(tokens)
                if token == variable or token.startswith(variable + "^")]
        if not hits:
            constant.append((sign, body))
            continue
        if len(hits) != 1:
            return None
        token = tokens[hits[0]]
        exponent = 1 if token == variable else int(token.split("^", 1)[1])
        if exponent != 1:
            return None
        del tokens[hits[0]]
        coefficient.append((sign, "*".join(tokens) if tokens else "1"))
    if not coefficient:
        return None
    return render_terms(constant), render_terms(coefficient)


def replace_token(text: str, variable: str, replacement: str) -> tuple[str, int]:
    pattern = rf"\b{re.escape(variable)}\b"
    count = len(re.findall(pattern, text))
    result = re.sub(pattern, f"({replacement})", text)
    if re.search(pattern, result):
        raise SystemExit(f"TOKEN_REPLACEMENT_FAILED:{variable}")
    return result, count


def specialize(text: str, zero_variables: tuple[str, ...],
               solved_variable: str | None = None,
               solved_expression: str | None = None) -> tuple[str, dict[str, int]]:
    counts: dict[str, int] = {}
    result = text
    for variable in zero_variables:
        result, counts[variable] = replace_token(result, variable, "0")
    if solved_variable is not None:
        if solved_expression is None:
            raise SystemExit("MISSING_SOLVED_EXPRESSION")
        result, counts[solved_variable] = replace_token(
            result, solved_variable, solved_expression
        )
    return result, counts


def pullback_lines(label: str, quotient: bool) -> list[str]:
    kind = "QUOTIENT" if quotient else "FIELD"
    return [
        "int start_kernel=timer; module K=syz(module(M)); matrix N=matrix(K);",
        "int kernel_generators=ncols(N);",
        f'print("{kind}_KERNEL_SECONDS="+string(timer-start_kernel));',
        f'print("{kind}_KERNEL_ROWS="+string(nrows(N))+" GENERATORS="+string(kernel_generators));',
        'if(nrows(N)!=105 || kernel_generators<1){ print("FATAL_KERNEL_SHAPE"); quit; }',
        "matrix replay=M*N; int replay_zero=(size(module(replay))==0);",
        f'string kernelfile="{label}_RIGHT_KERNEL_{kind}.tsv";',
        f'string endpointfile="{label}_ENDPOINT_PULLBACK_{kind}.tsv";',
        "int i; int j; poly qcoeff; int endpoint_nonzero=0; int endpoint_coefficients=0;",
        'for(i=1;i<=105;i=i+1){ for(j=1;j<=kernel_generators;j=j+1){ write(kernelfile,string(i)+"|"+string(j)+"|"+string(N[i,j])); } }',
        "for(i=1;i<=kernel_generators;i=i+1){ qcoeff=N[14,i]*N[72,i]+N[1,i]*N[97,i]; endpoint_coefficients=endpoint_coefficients+1; if(qcoeff!=0){ endpoint_nonzero=endpoint_nonzero+1; } write(endpointfile,string(i)+\"|\"+string(i)+\"|\"+string(qcoeff)); for(j=i+1;j<=kernel_generators;j=j+1){ qcoeff=N[14,i]*N[72,j]+N[14,j]*N[72,i]+N[1,i]*N[97,j]+N[1,j]*N[97,i]; endpoint_coefficients=endpoint_coefficients+1; if(qcoeff!=0){ endpoint_nonzero=endpoint_nonzero+1; } write(endpointfile,string(i)+\"|\"+string(j)+\"|\"+string(qcoeff)); } }",
        'print("ENDPOINT_QUADRATIC=x14*x72+x1*x97");',
        'print("KERNEL_REPLAY_ZERO="+string(replay_zero));',
        'print("ENDPOINT_PULLBACK_COEFFICIENTS="+string(endpoint_coefficients));',
        'print("ENDPOINT_PULLBACK_NONZERO_COEFFICIENTS="+string(endpoint_nonzero));',
        'if(replay_zero && endpoint_nonzero>0){ print("EXACT_GENERIC_ENDPOINT_SURVIVOR=1"); } else { if(replay_zero){ print("GENERIC_ENDPOINT_DEAD_RANK_JUMPS_PENDING=1"); } }',
    ]


def field_script(label: str, assignment: str, zero_variables: tuple[str, ...],
                 factor: str | None = None, solved_variable: str | None = None,
                 solved_expression: str | None = None,
                 chart_denominator: str = "1") -> str:
    specialized_matrix, counts = specialize(
        assignment, zero_variables, solved_variable, solved_expression
    )
    remaining = [p for p in PARAMETERS if p not in zero_variables]
    if solved_variable is not None:
        remaining.remove(solved_variable)
    if not remaining:
        coefficient_spec = "0"
    else:
        coefficient_spec = "0," + ",".join(remaining)
    lines = [
        f"// Exact function-field chart {label}.",
        f"ring r=({coefficient_spec}),(z),dp;",
        specialized_matrix,
        f'print("STRATUM_LABEL={label}");',
        f'print("ZERO_VARIABLES={",".join(zero_variables) if zero_variables else "NONE"}");',
        f'print("SOLVED_VARIABLE={solved_variable or "NONE"}");',
        f'print("TOKEN_REPLACEMENTS={";".join(f"{k}:{v}" for k, v in counts.items())}");',
    ]
    if factor is not None and solved_variable is not None and solved_expression is not None:
        specialized_factor, _ = specialize(
            factor, zero_variables, solved_variable, solved_expression
        )
        specialized_denominator, _ = specialize(chart_denominator, zero_variables)
        lines.extend([
            f"poly chart_relation={specialized_factor};",
            f"number chart_denominator={specialized_denominator};",
            'print("CHART_RELATION_ZERO="+string(chart_relation==0));',
            'print("CHART_DENOMINATOR_NONZERO="+string(chart_denominator!=0));',
            f'write("{label}_CHART_DENOMINATOR.txt",string(chart_denominator));',
            'if(chart_relation!=0 || chart_denominator==0){ print("FATAL_CHART_REPLAY"); quit; }',
        ])
    lines.extend(pullback_lines(label, quotient=False))
    lines.extend([
        f'string denomfile="{label}_KERNEL_DENOMINATORS_RAW.tsv";',
        "number entryden; int nonunit_denominators=0;",
        'for(i=1;i<=105;i=i+1){ for(j=1;j<=kernel_generators;j=j+1){ entryden=denominator(leadcoef(N[i,j])); write(denomfile,string(i)+"|"+string(j)+"|"+string(entryden)); if(entryden!=1 && entryden!=-1){ nonunit_denominators=nonunit_denominators+1; } } }',
        'print("KERNEL_NONUNIT_DENOMINATORS="+string(nonunit_denominators));',
        'print("BASIS_DENOMINATOR_COMPLEMENT_PENDING=1");',
        "quit;",
        "",
    ])
    return "\n".join(lines)


def qring_script(label: str, assignment: str, zero_variables: tuple[str, ...],
                 factor: str) -> str:
    specialized_matrix, counts = specialize(assignment, zero_variables)
    remaining = [p for p in PARAMETERS if p not in zero_variables]
    lines = [
        f"// Exact irreducible quotient-ring stratum {label}.",
        f"ring ambient=0,({','.join(remaining)}),dp;",
        f"poly BRANCH_FACTOR={factor};",
        'write("'+label+'_BRANCH_FACTOR.txt",string(BRANCH_FACTOR));',
        "ideal BRANCH_IDEAL=BRANCH_FACTOR;",
        "qring r=std(BRANCH_IDEAL);",
        'print("BRANCH_RELATION_ZERO="+string(BRANCH_FACTOR==0));',
        'if(BRANCH_FACTOR!=0){ print("FATAL_QUOTIENT_RELATION"); quit; }',
        specialized_matrix,
        f'print("STRATUM_LABEL={label}");',
        f'print("ZERO_VARIABLES={",".join(zero_variables)}");',
        f'print("TOKEN_REPLACEMENTS={";".join(f"{k}:{v}" for k, v in counts.items())}");',
    ]
    lines.extend(pullback_lines(label, quotient=True))
    lines.extend([
        'print("QUOTIENT_GENERIC_ONLY_RANK_JUMP_SUBSTRATA_PENDING=1");',
        "quit;",
        "",
    ])
    return "\n".join(lines)


def census_block(label: str, polynomial: str, filename: str) -> list[str]:
    return [
        f"poly {label}={polynomial};",
        f"list L_{label}=factorize({label});",
        f"ideal I_{label}=L_{label}[1]; intvec E_{label}=L_{label}[2]; matrix F_{label}=matrix(I_{label});",
        f"int N_{label}=ncols(F_{label}); int k_{label};",
        f'write("{filename}","RAW|"+string({label}));',
        f'write("{filename}","COUNT|"+string(N_{label}));',
        f'for(k_{label}=1;k_{label}<=N_{label};k_{label}=k_{label}+1){{ write("{filename}","FACTOR|"+string(k_{label})+"|"+string(E_{label}[k_{label}])+"|"+string(F_{label}[1,k_{label}])); }}',
        f'print("{label}_FACTOR_COUNT="+string(N_{label}));',
    ]


def build_base(matrix_path: Path, fitting_path: Path, content_path: Path,
               output_dir: Path) -> None:
    assignment = matrix_assignment(matrix_path)
    if sha256(fitting_path) != FITTING_SHA256:
        raise SystemExit("FITTING_SOURCE_SHA_MISMATCH")
    fitting = fitting_path.read_text()
    raw_content = declaration(fitting, "RAW_CONTENT")
    p_factor = exact_p(content_path)
    p_parts = linear_parts(p_factor, "c8")
    if p_parts is None:
        raise SystemExit("P_NOT_LINEAR_IN_C8_TEXT")
    p0, p1 = p_parts
    if p1 == "0" or "c8" in p0 or "c8" in p1:
        raise SystemExit("P_CHART_TEXT_FAILURE")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "P_EXACT.txt").write_text(p_factor + "\n")
    (output_dir / "P0_EXACT.txt").write_text(p0 + "\n")
    (output_dir / "P1_EXACT.txt").write_text(p1 + "\n")

    census = [
        "// Exact factor and specialization census.",
        "ring P=0,(q0,q1,q2,c4,c6,c8),dp;",
        raw_content,
        f"poly PF={p_factor};",
        f"poly P0_TEXT={p0}; poly P1_TEXT={p1};",
        "list L_CONTENT=factorize(RAW_CONTENT,1); ideal I_CONTENT=L_CONTENT[1]; matrix F_CONTENT=matrix(I_CONTENT);",
        "list L_P=factorize(PF,1); ideal I_P=L_P[1]; matrix F_P=matrix(I_P);",
        'print("RAW_CONTENT_DISTINCT_FACTOR_COUNT="+string(ncols(F_CONTENT)));',
        'print("P_IRREDUCIBLE_FACTOR_COUNT="+string(ncols(F_P)));',
        'print("P_LINEAR_C8_IDENTITY="+string(PF==P0_TEXT+c8*P1_TEXT));',
        'print("P1_NONZERO="+string(P1_TEXT!=0));',
        "ideal JP=PF; ideal JC8=c8; ideal JQ1=q1;",
        "int divides_p=(reduce(RAW_CONTENT,std(JP))==0); int divides_c8=(reduce(RAW_CONTENT,std(JC8))==0); int divides_q1=(reduce(RAW_CONTENT,std(JQ1))==0);",
        'print("RAW_CONTENT_DIVISIBLE_P_C8_Q1="+string(divides_p && divides_c8 && divides_q1));',
        'write("P_IRREDUCIBILITY_EXACT.txt","P_SHA256='+sha_text(p_factor)+'");',
        'write("P_IRREDUCIBILITY_EXACT.txt","RAW_CONTENT_DISTINCT_FACTOR_COUNT="+string(ncols(F_CONTENT)));',
        'write("P_IRREDUCIBILITY_EXACT.txt","P_IRREDUCIBLE_FACTOR_COUNT="+string(ncols(F_P)));',
        'write("P_IRREDUCIBILITY_EXACT.txt","P_LINEAR_C8_IDENTITY="+string(PF==P0_TEXT+c8*P1_TEXT));',
        'if(ncols(F_CONTENT)!=3 || ncols(F_P)!=1 || PF!=P0_TEXT+c8*P1_TEXT || P1_TEXT==0 || !(divides_p && divides_c8 && divides_q1)){ print("FATAL_FACTOR_OR_IRREDUCIBILITY_REPLAY"); quit; }',
    ]
    census.extend(census_block("C8P", "subst(PF,c8,0)", "C8P_FACTORS.tsv"))
    census.extend(census_block("Q1P", "subst(PF,q1,0)", "Q1P_FACTORS.tsv"))
    census.extend(census_block("TRIPLE", "subst(subst(PF,q1,0),c8,0)", "TRIPLE_FACTORS.tsv"))
    census.extend(['print("FACTOR_CENSUS_PASS=1");', "quit;", ""])
    (output_dir / "factor_census.sing").write_text("\n".join(census))

    p_expression = f"-(({p0}))/(({p1}))"
    (output_dir / "p_generic.sing").write_text(field_script(
        "P_GENERIC", assignment, (), p_factor, "c8", p_expression, p1
    ))
    (output_dir / "c8_q1.sing").write_text(field_script(
        "C8_Q1_GENERIC", assignment, ("c8", "q1")
    ))
    for name in ("p_generic", "c8_q1"):
        text = (output_dir / f"{name}.sing").read_text()
        prefix = text.split("module K=syz", 1)[0]
        (output_dir / f"parse_{name}.sing").write_text(
            prefix + f'print("FULL_MATRIX_PARSE_PASS={name.upper()}");\nquit;\n'
        )
    print(f"MATRIX_SHA256={sha256(matrix_path)}")
    print(f"FITTING_SHA256={sha256(fitting_path)}")
    print(f"CONTENT_SHA256={sha256(content_path)}")
    print(f"P_SHA256={sha_text(p_factor)}")
    print(f"P0_SHA256={sha_text(p0)}")
    print(f"P1_SHA256={sha_text(p1)}")
    print(f"MATRIX_ENTRIES={ROWS * COLS}")
    print("BASE_STRATA_BUILD_PASS")


def read_factor_file(path: Path) -> tuple[str, list[tuple[int, str]]]:
    raw: str | None = None
    expected: int | None = None
    factors: list[tuple[int, str]] = []
    for line in path.read_text().splitlines():
        fields = line.split("|", 3)
        if fields[0] == "RAW" and len(fields) == 2:
            raw = fields[1]
        elif fields[0] == "COUNT" and len(fields) == 2:
            expected = int(fields[1])
        elif fields[0] == "FACTOR" and len(fields) == 4:
            factors.append((int(fields[2]), fields[3].replace(" ", "")))
        else:
            raise SystemExit(f"FACTOR_FILE_PARSE_FAILURE:{path.name}:{line}")
    if raw is None or expected is None or expected != len(factors) or not factors:
        raise SystemExit(f"FACTOR_FILE_CENSUS_MISMATCH:{path.name}")
    return raw, factors


def choose_linear_chart(factor: str, unavailable: tuple[str, ...]) -> tuple[str, str, str] | None:
    for variable in reversed(PARAMETERS):
        if variable in unavailable:
            continue
        parts = linear_parts(factor, variable)
        if parts is None:
            continue
        f0, f1 = parts
        if f1 != "0":
            return variable, f"-(({f0}))/(({f1}))", f1
    return None


def build_branches(matrix_path: Path, census_dir: Path, output_dir: Path) -> None:
    assignment = matrix_assignment(matrix_path)
    specs = (
        ("C8P", ("c8",), census_dir / "C8P_FACTORS.tsv"),
        ("Q1P", ("q1",), census_dir / "Q1P_FACTORS.tsv"),
        ("TRIPLE", ("q1", "c8"), census_dir / "TRIPLE_FACTORS.tsv"),
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest = ["family|branch|multiplicity|factor_sha256|method|solved_variable|script"]
    for family, zero_variables, path in specs:
        _, factors = read_factor_file(path)
        for index, (multiplicity, factor) in enumerate(factors, 1):
            label = f"{family}_BRANCH_{index:02d}"
            filename = f"{family.lower()}_branch_{index:02d}.sing"
            chart = choose_linear_chart(factor, zero_variables)
            if chart is None:
                method = "irreducible_quotient_ring"
                solved = "NONE"
                script = qring_script(label, assignment, zero_variables, factor)
            else:
                solved, expression, denominator = chart
                method = "exact_function_field_linear_chart"
                script = field_script(
                    label, assignment, zero_variables, factor,
                    solved, expression, denominator
                )
            (output_dir / filename).write_text(script)
            parse_prefix = script.split("int start_kernel=timer", 1)[0]
            (output_dir / (filename.removesuffix(".sing") + "_parse.sing")).write_text(
                parse_prefix + f'print("BRANCH_FULL_MATRIX_PARSE_PASS={label}");\nquit;\n'
            )
            manifest.append(
                f"{family}|{index:02d}|{multiplicity}|{sha_text(factor)}|{method}|{solved}|{filename}"
            )
    (output_dir / "BRANCH_MANIFEST.tsv").write_text("\n".join(manifest) + "\n")
    print(f"BRANCH_MANIFEST_SHA256={sha256(output_dir / 'BRANCH_MANIFEST.tsv')}")
    print("INTERSECTION_BRANCH_BUILD_PASS")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--phase", choices=("base", "branches"), required=True)
    parser.add_argument("--matrix", type=Path, required=True)
    parser.add_argument("--fitting", type=Path)
    parser.add_argument("--content", type=Path)
    parser.add_argument("--census-dir", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    if args.phase == "base":
        if args.fitting is None or args.content is None:
            raise SystemExit("BASE_INPUTS_REQUIRED")
        build_base(args.matrix, args.fitting, args.content, args.output_dir)
    else:
        if args.census_dir is None:
            raise SystemExit("CENSUS_DIR_REQUIRED")
        build_branches(args.matrix, args.census_dir, args.output_dir)


if __name__ == "__main__":
    main()
