#!/usr/bin/env python3
r"""Audit and emit exact triangular reductions for S5/S6 row tables.

This is an analysis-side helper.  It never changes the source-complete emitter
or its row files.  A pivot is admitted only when an emitted row has the form

    a*v + q,  a in Z\{0},  v not in q.

The selected pivots form an acyclic dependency graph.  Consequently successive
substitution v=-q/a is an explicit quotient-ring isomorphism, rather than an
unknown/support truncation.  For rows containing the usual A2/B2 scalar pair,
A2 is eliminated and B2 retained.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import re
from typing import Iterable


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
VAR_RE = re.compile(r"([A-Za-z][A-Za-z0-9_]*)(?:\^(\d+))?")
TOKEN_RE = re.compile(r"\b[A-Za-z][A-Za-z0-9_]*\b")


@dataclass(frozen=True)
class Row:
    index: int
    h_power: int
    x_power: int
    y_power: int
    expr: str


@dataclass(frozen=True)
class Candidate:
    row: Row
    variable: str
    coefficient: Fraction
    alternatives: tuple[str, ...]
    dependencies: tuple[str, ...] = ()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def read_rows(path: Path) -> list[Row]:
    rows: list[Row] = []
    with path.open(encoding="utf-8") as source:
        header = source.readline().rstrip("\n")
        expected = "source_index|h_power|x_power|y_power|expr"
        if header != expected:
            raise ValueError(f"unexpected header: {header!r}")
        for line in source:
            if not line.strip():
                continue
            index, hp, xp, yp, expr = line.rstrip("\n").split("|", 4)
            rows.append(Row(int(index), int(hp), int(xp), int(yp), expr))
    if [row.index for row in rows] != list(range(len(rows))):
        raise ValueError("source indices are not consecutive")
    return rows


def split_terms(expr: str) -> list[str]:
    body = expr.strip()
    if body.startswith("(") and body.endswith(")"):
        body = body[1:-1]
    return [term.strip() for term in re.findall(r"[+-]?[^+-]+", body)]


def term_data(term: str) -> tuple[Fraction, list[tuple[str, int]]]:
    sign = -1 if term.startswith("-") else 1
    body = term.lstrip("+-")
    coefficient = Fraction(sign)
    variables: list[tuple[str, int]] = []
    for factor in body.split("*"):
        factor = factor.strip()
        match = VAR_RE.fullmatch(factor)
        if match:
            variables.append((match.group(1), int(match.group(2) or "1")))
            continue
        try:
            coefficient *= Fraction(factor)
        except ValueError as exc:
            raise ValueError(f"unparsed factor {factor!r} in {term!r}") from exc
    return coefficient, variables


def scalar_linear_candidates(row: Row) -> dict[str, Fraction]:
    occurrences: Counter[str] = Counter()
    pure: dict[str, Fraction] = {}
    for term in split_terms(row.expr):
        coefficient, variables = term_data(term)
        for variable, _power in variables:
            occurrences[variable] += 1
        if len(variables) == 1 and variables[0][1] == 1:
            variable = variables[0][0]
            pure[variable] = coefficient
    return {
        variable: coefficient
        for variable, coefficient in pure.items()
        if occurrences[variable] == 1 and coefficient
    }


def choose_variable(options: Iterable[str]) -> str:
    ordered = sorted(options)
    # The paired rows express A2 in terms of B2.  Keep B2 throughout.
    for variable in ordered:
        if not variable.startswith("B2_"):
            return variable
    return ordered[0]


def pivot_plan(rows: list[Row], include_c: bool = False) -> list[Candidate]:
    provisional: list[Candidate] = []
    for row in rows:
        options = scalar_linear_candidates(row)
        if not include_c:
            options.pop("c", None)
        if not options:
            continue
        variable = choose_variable(options)
        provisional.append(
            Candidate(row, variable, options[variable], tuple(sorted(options)))
        )

    variables = [candidate.variable for candidate in provisional]
    duplicates = [name for name, count in Counter(variables).items() if count != 1]
    if duplicates:
        raise ValueError(f"non-unique selected pivots: {duplicates}")
    pivot_variables = set(variables)
    with_dependencies: dict[str, Candidate] = {}
    for candidate in provisional:
        dependencies = (
            set(TOKEN_RE.findall(candidate.row.expr)) & pivot_variables
        ) - {candidate.variable}
        with_dependencies[candidate.variable] = Candidate(
            candidate.row,
            candidate.variable,
            candidate.coefficient,
            candidate.alternatives,
            tuple(sorted(dependencies)),
        )

    # A dependency must be substituted first.  Prefer the shortest available
    # row, which puts the literal zero pivots at the head of the plan.
    remaining = set(pivot_variables)
    result: list[Candidate] = []
    while remaining:
        available = [
            with_dependencies[name]
            for name in remaining
            if not (set(with_dependencies[name].dependencies) & remaining)
        ]
        if not available:
            cycle = {
                name: sorted(set(with_dependencies[name].dependencies) & remaining)
                for name in sorted(remaining)
            }
            raise ValueError(f"cyclic pivot graph: {cycle}")
        available.sort(
            key=lambda candidate: (
                len(candidate.row.expr),
                -candidate.row.h_power,
                -candidate.row.y_power,
                candidate.row.index,
                candidate.variable,
            )
        )
        for candidate in available:
            result.append(candidate)
            remaining.remove(candidate.variable)
    return result


def coefficient_first(names: Iterable[str]) -> list[str]:
    return sorted(
        names,
        key=lambda name: (
            0
            if name.startswith("A1_")
            else 1
            if name.startswith("A2_")
            else 2
            if name.startswith("A3_")
            else 3
            if name.startswith("B")
            else 4
            if name.startswith("h_")
            else 5,
            name,
        ),
    )


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"({value.numerator}/{value.denominator})"


def load(meta_path: Path) -> tuple[dict, Path, list[Row]]:
    payload = json.loads(meta_path.read_text(encoding="utf-8"))
    rows_path = ROOT / payload["rows_path"]
    return payload, rows_path, read_rows(rows_path)


def plan_record(meta_path: Path, include_c: bool = False) -> dict:
    payload, rows_path, rows = load(meta_path)
    plan = pivot_plan(rows, include_c=include_c)
    pivots = {candidate.variable for candidate in plan}
    active = [name for name in coefficient_first(payload["variables"]) if name not in pivots]
    by_band: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for candidate in plan:
        prefix = candidate.variable.split("_", 1)[0]
        by_band[str(candidate.row.h_power)][prefix] += 1
    return {
        "schema": "jc2.s56-recert.triangular-plan/v1",
        "meta": str(meta_path.relative_to(ROOT)),
        "meta_sha256": sha256(meta_path),
        "rows": str(rows_path.relative_to(ROOT)),
        "rows_sha256": sha256(rows_path),
        "source_row_count": len(rows),
        "source_variable_count": len(payload["variables"]),
        "include_c": include_c,
        "pivot_count": len(plan),
        "active_variable_count": len(active),
        "active_variables": active,
        "pivots_by_h_power_and_family": {
            band: dict(sorted(counts.items())) for band, counts in sorted(by_band.items())
        },
        "pivot_order": [
            {
                "step": step,
                "row_index": candidate.row.index,
                "h_power": candidate.row.h_power,
                "x_power": candidate.row.x_power,
                "y_power": candidate.row.y_power,
                "variable": candidate.variable,
                "scalar_coefficient": fraction_text(candidate.coefficient),
                "alternatives": list(candidate.alternatives),
                "dependencies": list(candidate.dependencies),
            }
            for step, candidate in enumerate(plan)
        ],
        "proof_obligation": (
            "At step i, after earlier substitutions, verify pivot_i=a_i*v_i+q_i, "
            "a_i is a nonzero field scalar, and v_i is absent from q_i.  Then "
            "v_i maps to -q_i/a_i.  The acyclic dependency order supplies an "
            "explicit inverse and yields a quotient-ring isomorphism."
        ),
    }


def emit_singular(
    meta_path: Path,
    characteristic: int,
    output: Path,
    include_c: bool = False,
    run_std: bool = False,
    branch: str = "none",
    method: str = "sequential",
    coordinate_filter: Path | None = None,
    prebasis_min_h: int | None = None,
    algorithm: str = "std",
    dump_reduced: bool = False,
) -> dict:
    if algorithm not in {"std", "slimgb"}:
        raise ValueError(f"unsupported standard-basis algorithm: {algorithm}")
    payload, rows_path, rows = load(meta_path)
    plan = pivot_plan(rows, include_c=include_c)
    pivots = {candidate.variable for candidate in plan}
    old_variables = coefficient_first(payload["variables"]) + ["T"]
    active_variables = [name for name in old_variables if name not in pivots]
    pivot_rows = {candidate.row.index for candidate in plan}
    remaining_rows = [row for row in rows if row.index not in pivot_rows]
    coordinate_filter_record = None
    if coordinate_filter is not None:
        coordinate_filter = coordinate_filter.resolve()
        filter_rows = read_rows(coordinate_filter)
        coordinates = {
            (row.h_power, row.x_power, row.y_power) for row in filter_rows
        }
        remaining_rows = [
            row
            for row in remaining_rows
            if (row.h_power, row.x_power, row.y_power) in coordinates
        ]
        coordinate_filter_record = {
            "path": str(coordinate_filter.relative_to(ROOT)),
            "sha256": sha256(coordinate_filter),
            "coordinate_count": len(coordinates),
        }
    if branch == "none":
        extras: list[str] = []
    elif branch == "q2":
        if "s2" not in old_variables:
            raise ValueError("q2 branch requested without s2")
        extras = ["s2^2-s2+1"]
    else:
        raise ValueError(branch)

    lines = [
        "// exact triangular quotient generated by triangular_preprocess.py",
        f"// meta_sha256={sha256(meta_path)}",
        f"// rows_sha256={sha256(rows_path)}",
        f"// characteristic={characteristic}",
        f"// branch={branch}",
        "// coordinate_filter="
        + (
            "none"
            if coordinate_filter_record is None
            else coordinate_filter_record["path"]
            + ":"
            + coordinate_filter_record["sha256"]
        ),
        f"// pivots={len(plan)} active_variables_including_T={len(active_variables)}",
        f"ring Old={characteristic},({','.join(old_variables)}),dp;",
        "option(redSB);",
    ]
    replacement_name: dict[str, str] = {}
    for step, candidate in enumerate(plan):
        pivot_name = f"PP_{step:03d}"
        replacement = f"REP_{step:03d}"
        derivative = f"DER_{step:03d}"
        lines.append(
            f"// step={step} row={candidate.row.index} hxy="
            f"{candidate.row.h_power},{candidate.row.x_power},{candidate.row.y_power} "
            f"pivot={candidate.variable} scalar={fraction_text(candidate.coefficient)}"
        )
        lines.append(f"poly {pivot_name}={candidate.row.expr};")
        for dependency in candidate.dependencies:
            lines.append(
                f"{pivot_name}=subst({pivot_name},{dependency},{replacement_name[dependency]});"
            )
        scalar = fraction_text(candidate.coefficient)
        lines.extend(
            [
                f"poly {derivative}=diff({pivot_name},{candidate.variable});",
                f"if ({derivative} != ({scalar})) "
                f'{{ \"PIVOT_DERIVATIVE_FAIL step={step} variable={candidate.variable}\"; exit(91); }}',
                f"if (subst({pivot_name},{candidate.variable},0) != "
                f"({pivot_name}-({scalar})*{candidate.variable})) "
                f'{{ \"PIVOT_AFFINE_FAIL step={step} variable={candidate.variable}\"; exit(92); }}',
                f"poly {replacement}=-({pivot_name}-({scalar})*{candidate.variable})/({scalar});",
                f"if (subst({replacement},{candidate.variable},0) != {replacement}) "
                f'{{ \"PIVOT_REPLACEMENT_FAIL step={step} variable={candidate.variable}\"; exit(93); }}',
                f"if (subst({pivot_name},{candidate.variable},{replacement}) != 0) "
                f'{{ \"PIVOT_IMAGE_FAIL step={step} variable={candidate.variable}\"; exit(94); }}',
                f'\"PIVOT_OK step={step} variable={candidate.variable}\";',
            ]
        )
        replacement_name[candidate.variable] = replacement

    residual_generators = [row.expr for row in remaining_rows] + extras
    rabinowitsch = f"(T*({payload['sat']})-1)"
    if prebasis_min_h is None:
        lines.append("ideal JOld=" + ",\n".join(residual_generators) + ",")
        lines.append(rabinowitsch + ";")
        lines.append('"JOLD_OK rows="+string(size(JOld));')
        old_ideal_names = ["JOld"]
    else:
        if method != "sequential":
            raise ValueError("prebasis staging currently requires --method sequential")
        high_generators = [
            row.expr for row in remaining_rows if row.h_power >= prebasis_min_h
        ]
        low_generators = [
            row.expr for row in remaining_rows if row.h_power < prebasis_min_h
        ] + extras + [rabinowitsch]
        if not high_generators or not low_generators:
            raise ValueError("prebasis split produced an empty side")
        lines.append("ideal JHighOld=" + ",\n".join(high_generators) + ";")
        lines.append("ideal JLowOld=" + ",\n".join(low_generators) + ";")
        lines.append(
            '"JOLD_OK rows="+string(size(JHighOld)+size(JLowOld))'
            '+" high="+string(size(JHighOld))+" low="+string(size(JLowOld));'
        )
        old_ideal_names = ["JHighOld", "JLowOld"]
    if method == "map":
        lines.append(f"ring Reduced={characteristic},({','.join(active_variables)}),dp;")
        for step, candidate in enumerate(plan):
            lines.append(f"poly IMG_{step:03d}=imap(Old,{replacement_name[candidate.variable]});")
        images: list[str] = []
        image_by_pivot = {
            candidate.variable: f"IMG_{step:03d}" for step, candidate in enumerate(plan)
        }
        for variable in old_variables:
            images.append(image_by_pivot.get(variable, variable))
        lines.append("map Phi=Old," + ",".join(images) + ";")
        lines.append('"MAP_DECLARED_OK";')
        lines.append("ideal JReduced=Phi(JOld);")
        lines.append('"MAP_APPLIED_OK raw_rows="+string(size(JReduced));')
    elif method == "sequential":
        for step, candidate in enumerate(plan):
            for ideal_name in old_ideal_names:
                lines.append(
                    f"{ideal_name}=subst({ideal_name},{candidate.variable},"
                    f"{replacement_name[candidate.variable]});"
                )
            lines.append(
                f'\"IDEAL_SUBST_OK step={step} variable={candidate.variable}\";'
            )
        lines.append(f"ring Reduced={characteristic},({','.join(active_variables)}),dp;")
        if prebasis_min_h is None:
            lines.append("ideal JReduced=imap(Old,JOld);")
            lines.append('"IMAP_APPLIED_OK raw_rows="+string(size(JReduced));')
        else:
            lines.extend(
                [
                    "ideal JHighReduced=imap(Old,JHighOld);",
                    "ideal JLowReduced=imap(Old,JLowOld);",
                    "JHighReduced=simplify(JHighReduced,2);",
                    "JLowReduced=simplify(JLowReduced,2);",
                    '"IMAP_APPLIED_OK raw_rows="'
                    '+string(size(JHighReduced)+size(JLowReduced))'
                    '+" high="+string(size(JHighReduced))'
                    '+" low="+string(size(JLowReduced));',
                    f'"PREBASIS_BEGIN min_h={prebasis_min_h}";',
                    "timer=1; int PRE_T0=timer;",
                    "ideal GPre=std(JHighReduced);",
                    "int PRE_DT=timer-PRE_T0;",
                    "ideal PRE_NF=reduce(JHighReduced,GPre);",
                    "int PRE_NF_ZERO=1; int PRE_I;",
                    "for (PRE_I=1;PRE_I<=size(PRE_NF);PRE_I++) "
                    "{ if (PRE_NF[PRE_I]!=0) { PRE_NF_ZERO=0; } }",
                    '"PREBASIS_DONE ms="+string(PRE_DT)'
                    '+" basis_size="+string(size(GPre))'
                    '+" dim="+string(dim(GPre));',
                    '"PREBASIS_NF_ALL_ZERO "+string(PRE_NF_ZERO);',
                    'if (PRE_NF_ZERO!=1) { "PREBASIS_CONTROL_FAIL NF"; exit(97); }',
                    "JLowReduced=reduce(JLowReduced,GPre);",
                    "ideal JReduced=GPre,JLowReduced;",
                ]
            )
    else:
        raise ValueError(method)
    lines.append("JReduced=simplify(JReduced,2);")
    lines.extend(
        [
            f'"TRIANGULAR_OK pivots={len(plan)} source_rows={len(rows)} "'
            f'+" residual_rows="+string(size(JReduced))'
            f'+" active_including_T={len(active_variables)}";',
            "int TRI_MAX_DEG=-1; int TRI_I;",
            "for (TRI_I=1;TRI_I<=size(JReduced);TRI_I++) "
            "{ if (deg(JReduced[TRI_I])>TRI_MAX_DEG) { TRI_MAX_DEG=deg(JReduced[TRI_I]); } }",
            '"TRIANGULAR_MAX_DEG "+string(TRI_MAX_DEG);',
        ]
    )
    if dump_reduced:
        lines.extend(
            [
                f'"DUMP__VARS {",".join(active_variables)}";',
                '"DUMP__COUNT "+string(size(JReduced));',
                "int TRI_DUMP_I;",
                'for (TRI_DUMP_I=1;TRI_DUMP_I<=size(JReduced);TRI_DUMP_I++) '
                '{ print("DUMP__ROW "+string(JReduced[TRI_DUMP_I])); }',
            ]
        )
    if run_std:
        lines.extend(
            [
                '"TRIANGULAR_STD_BEGIN";',
                "timer=1; int TRI_T0=timer;",
                f"ideal G={algorithm}(JReduced);",
                "int TRI_DT=timer-TRI_T0;",
                "ideal TRI_NF=reduce(JReduced,G);",
                "int TRI_NF_ZERO=1; int TRI_J;",
                "for (TRI_J=1;TRI_J<=size(TRI_NF);TRI_J++) "
                "{ if (TRI_NF[TRI_J]!=0) { TRI_NF_ZERO=0; } }",
                "ideal TRI_LEAD=lead(G);",
                "poly TRI_ONE=reduce(1,G);",
                "int TRI_IS_UNIT=0; if (TRI_ONE==0) { TRI_IS_UNIT=1; }",
                '"TRIANGULAR_STD_DONE ms="+string(TRI_DT);',
                '"TRIANGULAR_GENERATOR_COUNT "+string(size(JReduced));',
                '"TRIANGULAR_NF_ALL_ZERO "+string(TRI_NF_ZERO);',
                '"TRIANGULAR_BASIS_SIZE "+string(size(G));',
                '"TRIANGULAR_DIMENSION "+string(dim(G));',
                '"TRIANGULAR_LEAD_DIMENSION "+string(dim(TRI_LEAD));',
                '"TRIANGULAR_UNIT "+string(TRI_IS_UNIT);',
                'if (TRI_NF_ZERO!=1) { "TRIANGULAR_CONTROL_FAIL NF"; exit(95); }',
                'if (TRI_IS_UNIT==1 && (size(G)!=1 || dim(G)!=-1 || dim(TRI_LEAD)!=-1)) '
                '{ "TRIANGULAR_CONTROL_FAIL UNIT_SHAPE"; exit(96); }',
            ]
        )
    lines.append('"SCRIPT_DONE";')
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {
        "script": str(output.relative_to(ROOT)),
        "script_sha256": sha256(output),
        "source_rows": len(rows),
        "pivot_count": len(plan),
        "residual_rows_before_zero_simplification": len(residual_generators) + 1,
        "active_variables_including_T": len(active_variables),
        "characteristic": characteristic,
        "branch": branch,
        "method": method,
        "extra_generators": extras,
        "coordinate_filter": coordinate_filter_record,
        "prebasis_min_h": prebasis_min_h,
        "algorithm": algorithm,
        "dump_reduced": dump_reduced,
        "selected_source_row_count": len(pivot_rows) + len(remaining_rows),
        "run_std": run_std,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    plan_parser = subparsers.add_parser("plan")
    plan_parser.add_argument("--meta", type=Path, required=True)
    plan_parser.add_argument("--include-c", action="store_true")
    plan_parser.add_argument("--output", type=Path)
    emit_parser = subparsers.add_parser("emit")
    emit_parser.add_argument("--meta", type=Path, required=True)
    emit_parser.add_argument("--char", type=int, required=True)
    emit_parser.add_argument("--include-c", action="store_true")
    emit_parser.add_argument("--branch", choices=("none", "q2"), default="none")
    emit_parser.add_argument("--method", choices=("map", "sequential"), default="sequential")
    emit_parser.add_argument("--coordinate-filter", type=Path)
    emit_parser.add_argument("--prebasis-min-h", type=int)
    emit_parser.add_argument("--algorithm", choices=("std", "slimgb"), default="std")
    emit_parser.add_argument("--dump-reduced", action="store_true")
    emit_parser.add_argument("--std", action="store_true")
    emit_parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    meta_path = args.meta.resolve()
    if args.command == "plan":
        result = plan_record(meta_path, include_c=args.include_c)
        if args.output:
            output = args.output.resolve()
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        result = emit_singular(
            meta_path,
            args.char,
            args.output.resolve(),
            include_c=args.include_c,
            run_std=args.std,
            branch=args.branch,
            method=args.method,
            coordinate_filter=args.coordinate_filter,
            prebasis_min_h=args.prebasis_min_h,
            algorithm=args.algorithm,
            dump_reduced=args.dump_reduced,
        )
        print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
