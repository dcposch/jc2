#!/usr/bin/env python3
"""Emit small analysis wrappers around a preexpanded K=16 cone job.

The input is an existing ``.sing`` file containing declarations ``T0,...``.
Only the coefficient field/minpoly and those polynomial declarations are
copied; the original computation at the end of the file is deliberately not
copied.  In particular, this script never invokes Singular.

The two built-in variable orders use the same weighted grading:

``requested``
    ``(b4,q2_0,...,q(t-1)_0,b3), wp(1,2,...,t-1,t+1)``.

``legacy``
    ``(b3,b4,q2_0,...,q(t-1)_0), wp(t+1,1,2,...,t-1)``.

Each emitted job is meant to be run separately, in the foreground, e.g.
``timeout 1800 Singular -q JOB.sing``.  Keeping the engines in separate jobs
means that a timeout in one engine does not hide the other trials.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


HERE = Path(__file__).resolve().parent
VARIANTS = ("direct", "incremental", "groebner", "slimgb", "target")


@dataclass(frozen=True)
class ParsedCone:
    source: Path
    source_sha256: str
    coefficient_field: str
    minpoly_statement: str | None
    original_ring_name: str
    original_variables: tuple[str, ...]
    rows: tuple[tuple[int, str], ...]
    t: int


def split_top_level(text: str, separator: str = ",") -> list[str]:
    """Split on *separator* outside (), [], and {}."""
    pieces: list[str] = []
    start = 0
    stack: list[str] = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for pos, char in enumerate(text):
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack.pop() != pairs[char]:
                raise ValueError(f"unbalanced delimiter near offset {pos}")
        elif char == separator and not stack:
            pieces.append(text[start:pos].strip())
            start = pos + 1
    if stack:
        raise ValueError("unbalanced delimiter at end of text")
    pieces.append(text[start:].strip())
    return pieces


def unwrap_parentheses(text: str, label: str) -> str:
    text = text.strip()
    if len(text) < 2 or text[0] != "(" or text[-1] != ")":
        raise ValueError(f"expected parenthesized {label}, got {text!r}")
    # split_top_level also checks balance; wrapping once makes nested q(2) safe.
    split_top_level(text[1:-1])
    return text[1:-1]


def parse_ring(text: str) -> tuple[str, str, tuple[str, ...], int]:
    match = re.search(
        r"(?ms)^\s*ring\s+([A-Za-z_]\w*)\s*=\s*(.*?);", text
    )
    if not match:
        raise ValueError("no ring declaration found")
    name, rhs = match.group(1), match.group(2).strip()
    fields = split_top_level(rhs)
    if len(fields) != 3:
        raise ValueError(
            "ring declaration must have coefficient field, variables, and order"
        )
    variables = tuple(
        piece.strip()
        for piece in split_top_level(unwrap_parentheses(fields[1], "variable list"))
    )
    if not variables or any(not item for item in variables):
        raise ValueError("empty variable in source ring")
    return name, fields[0], variables, match.end()


def parse_rows(text: str) -> tuple[tuple[int, str], ...]:
    matches = list(
        re.finditer(r"(?ms)^\s*poly\s+T(\d+)\s*=\s*(.*?);", text)
    )
    if not matches:
        raise ValueError("no poly T<number> declarations found")
    seen: set[int] = set()
    rows: list[tuple[int, str]] = []
    for match in matches:
        index = int(match.group(1))
        if index in seen:
            raise ValueError(f"duplicate declaration T{index}")
        rhs = match.group(2).strip()
        if not rhs:
            raise ValueError(f"empty declaration T{index}")
        seen.add(index)
        rows.append((index, rhs))
    rows.sort()
    indices = [index for index, _ in rows]
    if indices != list(range(indices[-1] + 1)):
        raise ValueError(f"T declarations are not contiguous from T0: {indices}")
    return tuple(rows)


def q_index(variable: str) -> int | None:
    for pattern in (r"q(\d+)_0", r"q\((\d+)\)"):
        match = re.fullmatch(pattern, variable)
        if match:
            return int(match.group(1))
    return None


def infer_t(text: str, variables: tuple[str, ...], rows: tuple[tuple[int, str], ...],
            explicit_t: int | None) -> int:
    candidates: list[tuple[str, int]] = []
    if explicit_t is not None:
        candidates.append(("--t", explicit_t))
    printed = re.search(r'print\s*\(\s*"T=(\d+)"\s*\)', text)
    if printed:
        candidates.append(('print("T=...")', int(printed.group(1))))
    maximum = rows[-1][0]
    if (maximum + 1) % 2 == 0:
        candidates.append(("T-row count", (maximum + 1) // 2))
    candidates.append(("ring variable count", len(variables)))
    values = {value for _, value in candidates}
    if len(values) != 1:
        detail = ", ".join(f"{label}={value}" for label, value in candidates)
        raise ValueError(f"inconsistent t inference: {detail}")
    t = values.pop()
    if t < 2:
        raise ValueError("t must be at least 2")
    return t


def parse_source(source: Path, explicit_t: int | None) -> ParsedCone:
    raw = source.read_bytes()
    text = raw.decode("utf-8")
    ring_name, coefficient_field, variables, ring_end = parse_ring(text)
    rows = parse_rows(text)
    first_row = re.search(r"(?m)^\s*poly\s+T0\s*=", text)
    if not first_row:
        raise ValueError("T0 declaration missing")
    preamble = text[ring_end:first_row.start()]
    minpolys = list(re.finditer(r"(?ms)^\s*minpoly\s*=\s*(.*?);", preamble))
    if len(minpolys) > 1:
        raise ValueError("more than one minpoly statement before T0")
    minpoly = None
    if minpolys:
        minpoly = "minpoly=" + minpolys[0].group(1).strip() + ";"
    t = infer_t(text, variables, rows, explicit_t)
    expected_last = 2 * t - 1
    if rows[-1][0] != expected_last:
        raise ValueError(
            f"expected declarations T0..T{expected_last} for t={t}, "
            f"found through T{rows[-1][0]}"
        )
    return ParsedCone(
        source=source,
        source_sha256=hashlib.sha256(raw).hexdigest(),
        coefficient_field=coefficient_field,
        minpoly_statement=minpoly,
        original_ring_name=ring_name,
        original_variables=variables,
        rows=rows,
        t=t,
    )


def ordered_variables(cone: ParsedCone, order: str) -> tuple[tuple[str, ...], tuple[int, ...]]:
    by_name = set(cone.original_variables)
    if len(by_name) != len(cone.original_variables):
        raise ValueError("duplicate source ring variable")
    if "b4" not in by_name or "b3" not in by_name:
        raise ValueError("source ring must contain b4 and b3")
    qvars: list[tuple[int, str]] = []
    for variable in by_name - {"b4", "b3"}:
        index = q_index(variable)
        if index is None:
            raise ValueError(f"unexpected residual variable {variable!r}")
        qvars.append((index, variable))
    qvars.sort()
    expected_q = list(range(2, cone.t))
    actual_q = [index for index, _ in qvars]
    if actual_q != expected_q:
        raise ValueError(f"expected q indices {expected_q}, found {actual_q}")
    qnames = [variable for _, variable in qvars]
    if order == "requested":
        variables = ("b4", *qnames, "b3")
    elif order == "legacy":
        variables = ("b3", "b4", *qnames)
    else:  # protected by argparse; retained for programmatic use
        raise ValueError(f"unknown order {order!r}")
    weight_map = {"b4": 1, "b3": cone.t + 1}
    weight_map.update({variable: index for index, variable in qvars})
    weights = tuple(weight_map[variable] for variable in variables)
    return variables, weights


def parse_intvec(raw: str) -> tuple[int, ...]:
    """Parse a comma/space-separated intvec, with an optional assignment shell."""
    raw = raw.strip()
    assignment = re.fullmatch(
        r"(?:intvec\s+[A-Za-z_]\w*\s*=\s*)?([^;]+);?", raw, re.S
    )
    if not assignment:
        raise ValueError("could not parse Hilbert numerator")
    body = assignment.group(1).strip()
    pieces = [piece for piece in re.split(r"[\s,]+", body) if piece]
    if not pieces:
        raise ValueError("Hilbert numerator is empty")
    try:
        values = tuple(int(piece) for piece in pieces)
    except ValueError as exc:
        raise ValueError(
            "Hilbert numerator must contain only comma/space-separated integers"
        ) from exc
    return values


def singular_hilbert_vector(numerator: tuple[int, ...]) -> tuple[int, ...]:
    """Attach Singular's non-series bookkeeping entry to a first Hilbert series.

    ``hilb(G,1,WTS)`` prints the numerator coefficients followed by one entry
    which is not a coefficient (zero for the ideals used here).  Accept either
    a bare polynomial coefficient vector or a vector copied from Singular and
    emit exactly one trailing bookkeeping zero.
    """
    coefficients = list(numerator)
    while len(coefficients) > 1 and coefficients[-1] == 0:
        coefficients.pop()
    return (*coefficients, 0)


def singular_string(text: str) -> str:
    return text.replace("\\", "\\\\").replace('"', '\\"')


def analysis_tail(cone: ParsedCone, variables: tuple[str, ...], weights: tuple[int, ...],
                  pure_bound: int, variant: str) -> list[str]:
    label = variant.upper()
    lines = [
        f'print("ANALYSIS_BEGIN variant={label}");',
        'print("BASIS_SECONDS="+string(timer-start_time));',
        'print("BASIS_SIZE="+string(size(G)));',
        'int quotient_dim=dim(G);',
        'print("DIM="+string(quotient_dim));',
        'if (quotient_dim<=0)',
        '{',
        '  print("LENGTH="+string(vdim(G)));',
        '}',
        'else',
        '{',
        '  print("LENGTH=NONTERMINATING");',
        '}',
        'print("HILB_NUMERATOR_BEGIN");',
        'intvec computed_hnum=hilb(G,1,WTS); computed_hnum;',
        'print("HILB_NUMERATOR_END");',
        'print("HILB_REDUCED_BEGIN");',
        'intvec computed_hred=hilb(G,2,WTS); computed_hred;',
        'print("HILB_REDUCED_END");',
        'ideal LM=minbase(lead(G));',
        'ideal GLM=std(LM);',
        'print("INITIAL_MIN_COUNT="+string(size(LM)));',
        'int lm_index;',
        'for (lm_index=1; lm_index<=size(LM); lm_index++)',
        '{',
        '  print("INITIAL_EXP_"+string(lm_index)+"="+string(leadexp(LM[lm_index])));',
        '}',
    ]
    for variable in variables:
        token = re.sub(r"\W", "_", variable)
        lines.extend([
            f"int pure_{token}=0; int power_{token};",
            f"for (power_{token}=1; power_{token}<={pure_bound}; power_{token}++)",
            "{",
            f"  if (reduce({variable}^power_{token},GLM)==0)",
            "  {",
            f"    pure_{token}=power_{token}; break;",
            "  }",
            "}",
            f'print("INITIAL_PURE_POWER {variable}="+string(pure_{token}));',
        ])
    lines.extend([
        f'print("ANALYSIS_DONE variant={label}");',
        "quit;",
    ])
    return lines


def algorithm_lines(cone: ParsedCone, variant: str,
                    target_hnum: tuple[int, ...] | None) -> list[str]:
    descending = list(range(2 * cone.t - 1, 0, -1))
    reverse_ideal = ",".join(f"T{index}" for index in descending)
    if variant == "incremental":
        first, *remaining = descending
        lines = [
            f'print("ROW_ORDER={reverse_ideal}");',
            "int start_time=timer;",
            "int step_time=timer;",
            f"ideal G=std(ideal(T{first}));",
            f'print("INCREMENT_ROW=T{first} SECONDS="+string(timer-step_time)'
            '+" SIZE="+string(size(G))+" DIM="+string(dim(G)));',
        ]
        for index in remaining:
            lines.extend([
                "step_time=timer;",
                f"G=std(G,T{index});",
                f'print("INCREMENT_ROW=T{index} SECONDS="+string(timer-step_time)'
                '+" SIZE="+string(size(G))+" DIM="+string(dim(G)));',
            ])
        return lines

    lines = [f"ideal I={reverse_ideal};", f'print("ROW_ORDER={reverse_ideal}");']
    if variant == "target":
        if target_hnum is None:
            raise ValueError("target variant requires a Hilbert numerator")
        target_vector = singular_hilbert_vector(target_hnum)
        lines.append("intvec TARGET_HNUM=" + ",".join(map(str, target_vector)) + ";")
    lines.append("int start_time=timer;")
    calls = {
        "direct": "std(I)",
        "groebner": "groebner(I)",
        "slimgb": "slimgb(I)",
    }
    if variant == "target":
        # The Hilbert input is only a performance hint until independently
        # known.  Re-standardize the union with I after clearing the trusted
        # standard-basis attribute; this makes a conjectural target unable to
        # certify itself by premature Hilbert-driven termination.
        lines.extend([
            "ideal Gseed=std(I,TARGET_HNUM,WTS);",
            'print("TARGET_SEED_SIZE="+string(size(Gseed)));',
            "ideal SEED_LM=minbase(lead(Gseed));",
            "ideal SEED_GLM=std(SEED_LM);",
            'print("TARGET_SEED_DIM="+string(dim(SEED_GLM)));',
            'print("TARGET_SEED_HNUM_BEGIN");',
            "intvec seed_hnum=hilb(SEED_GLM,1,WTS); seed_hnum;",
            'print("TARGET_SEED_HNUM_END");',
            "int seed_vi; int seed_pi; int seed_power;",
            "for (seed_vi=1; seed_vi<=nvars(basering); seed_vi++)",
            "{",
            "  seed_power=0;",
            "  for (seed_pi=1; seed_pi<=512; seed_pi++)",
            "  {",
            "    if (reduce(var(seed_vi)^seed_pi,SEED_GLM)==0)",
            "    { seed_power=seed_pi; break; }",
            "  }",
            '  print("TARGET_SEED_PURE_POWER_INDEX "'
            '+string(seed_vi)+"="+string(seed_power));',
            "}",
            "ideal J=Gseed,I;",
            'attrib(J,"isSB",0);',
            "ideal G=slimgb(J);",
            'print("TARGET_RESTANDARDIZED=SLIMGB");',
        ])
        return lines
    try:
        call = calls[variant]
    except KeyError as exc:
        raise ValueError(f"unknown variant {variant!r}") from exc
    lines.append(f"ideal G={call};")
    return lines


def emit_job(cone: ParsedCone, order: str, variant: str, pure_bound: int,
             target_hnum: tuple[int, ...] | None) -> str:
    variables, weights = ordered_variables(cone, order)
    lines = [
        "// Preexpanded K=16 cone analysis wrapper; this file does not rebuild rows.",
        f"// source={cone.source} source_sha256={cone.source_sha256}",
        f"// t={cone.t} order={order} variant={variant}",
        f"ring R={cone.coefficient_field},({','.join(variables)}),"
        f"wp({','.join(map(str, weights))});",
    ]
    if cone.minpoly_statement:
        lines.append(cone.minpoly_statement)
    lines.extend([
        "option(noredSB);",
        f"intvec WTS={','.join(map(str, weights))};",
        f'print("META t={cone.t} order={order} variant={variant} '
        f'vars={singular_string(",".join(variables))} '
        f'weights={singular_string(",".join(map(str, weights)))}");',
    ])
    for index, rhs in cone.rows:
        lines.append(f"poly T{index} =\n  {rhs};")
    for index, _ in cone.rows:
        if index == 0:
            continue
        expected_degree = 4 * cone.t + 1 - index
        lines.extend([
            f'if (homog(T{index})!=1) {{ print("FAIL inhomogeneous T{index}"); exit(2); }}',
            f'if (deg(T{index})!={expected_degree}) '
            f'{{ print("FAIL degree T{index}"); exit(2); }}',
        ])
    lines.append('print("ROW_GRADING_CHECK=PASS");')
    lines.extend(algorithm_lines(cone, variant, target_hnum))
    lines.extend(analysis_tail(cone, variables, weights, pure_bound, variant))
    source = "\n".join(lines) + "\n"
    validate_emission(source, cone, order, variant, target_hnum)
    return source


def validate_emission(source: str, cone: ParsedCone, order: str, variant: str,
                      target_hnum: tuple[int, ...] | None) -> None:
    """Cheap structural validation only; this intentionally does not run Singular."""
    ring_name, _, variables, _ = parse_ring(source)
    if ring_name != "R":
        raise AssertionError("emitted ring name is not R")
    expected_variables, _ = ordered_variables(cone, order)
    if variables != expected_variables:
        raise AssertionError("emitted variable order differs from requested order")
    reparsed_rows = parse_rows(source)
    if [index for index, _ in reparsed_rows] != [index for index, _ in cone.rows]:
        raise AssertionError("emitted T declaration indices changed")
    # Compare whitespace-normalized expressions, so indentation is immaterial.
    compact = lambda value: re.sub(r"\s+", "", value)
    for (left_index, left), (right_index, right) in zip(cone.rows, reparsed_rows):
        if left_index != right_index or compact(left) != compact(right):
            raise AssertionError(f"emitted expression T{left_index} changed")
    if source.count("quit;") != 1 or not source.rstrip().endswith("quit;"):
        raise AssertionError("emitted job must end in exactly one quit")
    if variant == "target":
        if target_hnum is None or "std(I,TARGET_HNUM,WTS)" not in source:
            raise AssertionError("target job is missing Hilbert-driven std call")
        if 'attrib(J,"isSB",0);' not in source or "ideal G=slimgb(J);" not in source:
            raise AssertionError("target job is missing independent re-standardization")
    if variant == "incremental" and "G=std(G,T1);" not in source:
        raise AssertionError("incremental job does not reach T1")


def selected_variants(spec: str, target_hnum: tuple[int, ...] | None) -> tuple[str, ...]:
    if spec != "all":
        if spec == "target" and target_hnum is None:
            raise ValueError("--variant target needs --hilbert-numerator[-file]")
        return (spec,)
    variants = list(VARIANTS[:-1])
    if target_hnum is not None:
        variants.append("target")
    return tuple(variants)


def default_output(source: Path, order: str, variant: str, out_dir: Path) -> Path:
    return out_dir / f"{source.stem}_{order}_{variant}.sing"


def write_jobs(cone: ParsedCone, variants: Iterable[str], order: str,
               pure_bound: int, target_hnum: tuple[int, ...] | None,
               output: Path | None, out_dir: Path, check_only: bool) -> list[dict[str, object]]:
    variants = tuple(variants)
    if output is not None and len(variants) != 1:
        raise ValueError("--output is valid only for one variant")
    records: list[dict[str, object]] = []
    for variant in variants:
        emitted = emit_job(cone, order, variant, pure_bound, target_hnum)
        destination = output or default_output(cone.source, order, variant, out_dir)
        record: dict[str, object] = {
            "variant": variant,
            "order": order,
            "t": cone.t,
            "rows": [index for index, _ in cone.rows],
            "output": str(destination),
            "bytes": len(emitted.encode("utf-8")),
            "sha256": hashlib.sha256(emitted.encode("utf-8")).hexdigest(),
            "written": not check_only,
        }
        if not check_only:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(emitted, encoding="utf-8")
        records.append(record)
    return records


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="preexpanded cone .sing source")
    parser.add_argument("--t", type=int, help="explicit t (also cross-checked)")
    parser.add_argument("--order", choices=("requested", "legacy"), default="requested")
    parser.add_argument(
        "--variant", choices=(*VARIANTS, "all"), default="direct",
        help="one engine, or all independent engine jobs (target only if supplied)",
    )
    parser.add_argument("--pure-bound", type=int, default=512)
    parser.add_argument("--output", type=Path, help="output .sing path for one variant")
    parser.add_argument("--out-dir", type=Path, default=HERE)
    hilbert = parser.add_mutually_exclusive_group()
    hilbert.add_argument(
        "--hilbert-numerator",
        help="known numerator as comma/space-separated integers",
    )
    hilbert.add_argument(
        "--hilbert-numerator-file", type=Path,
        help="file containing only an intvec or comma/space-separated integers",
    )
    parser.add_argument(
        "--check-only", action="store_true",
        help="parse and structurally validate every selected emission without writing",
    )
    args = parser.parse_args()
    if args.source.suffix != ".sing":
        parser.error("source must end in .sing")
    if args.output is not None and args.output.suffix != ".sing":
        parser.error("--output must end in .sing")
    if args.pure_bound < 1:
        parser.error("--pure-bound must be positive")
    try:
        cone = parse_source(args.source, args.t)
        raw_hnum = args.hilbert_numerator
        if args.hilbert_numerator_file is not None:
            raw_hnum = args.hilbert_numerator_file.read_text(encoding="utf-8")
        target_hnum = parse_intvec(raw_hnum) if raw_hnum is not None else None
        variants = selected_variants(args.variant, target_hnum)
        records = write_jobs(
            cone, variants, args.order, args.pure_bound, target_hnum,
            args.output, args.out_dir, args.check_only,
        )
    except (OSError, ValueError, AssertionError) as exc:
        parser.error(str(exc))
    print(json.dumps({
        "source": str(cone.source),
        "source_sha256": cone.source_sha256,
        "coefficient_field": cone.coefficient_field,
        "minpoly_copied": cone.minpoly_statement is not None,
        "jobs": records,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
