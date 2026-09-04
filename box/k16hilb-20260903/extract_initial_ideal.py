#!/usr/bin/env python3
"""Validate and tabulate a completed K=16 initial-ideal transcript.

Modern transcripts carry ``LABEL_INITIAL_EXP_i=e1,...,en`` records.  Two
early clean exact transcripts (t=3,4) predate those records, so this parser
also accepts their indexed ``LM[i]=monomial`` block and reconstructs the same
vectors.  If both encodings occur, they must agree entry by entry.

No computer-algebra process is started.  The validation is combinatorial:
metadata/completion, cardinality, contiguous indices, exponent arity and
signs, divisibility-antichain minimality, and the reported least pure powers.
The dominance test is exact but word-parallel: it intersects Python-integer
bitsets for the coordinate lower orthants instead of scanning all pairs in
Python.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ParsedInitialIdeal:
    output: Path
    output_sha256: str
    t: int
    label: str
    order: str
    variables: tuple[str, ...]
    weights: tuple[int, ...]
    exponents: tuple[tuple[int, ...], ...]
    exponent_source: str
    count_source: str
    reported_count: int
    reported_pure_powers: tuple[tuple[str, int], ...]
    derived_pure_powers: tuple[tuple[str, int], ...]


def one_match(pattern: str, text: str, description: str,
              *, required: bool = True) -> re.Match[str] | None:
    matches = list(re.finditer(pattern, text, re.MULTILINE))
    if not matches and not required:
        return None
    if len(matches) != 1:
        raise ValueError(f"expected exactly one {description}, found {len(matches)}")
    return matches[0]


def prompt_variables(t: int) -> tuple[str, ...]:
    return ("b4", *(f"q{index}_0" for index in range(2, t)), "b3")


def legacy_variables(t: int) -> tuple[str, ...]:
    return ("b3", "b4", *(f"q{index}_0" for index in range(2, t)))


def variable_weight(variable: str, t: int) -> int:
    if variable == "b4":
        return 1
    if variable == "b3":
        return t + 1
    match = re.fullmatch(r"q(\d+)_0", variable)
    if not match:
        match = re.fullmatch(r"q\((\d+)\)", variable)
    if not match:
        raise ValueError(f"cannot infer a grading weight for variable {variable!r}")
    return int(match.group(1))


def parse_variables(raw: str | None, t: int, order: str) -> tuple[str, ...]:
    expected: tuple[str, ...] | None = None
    if order in {"prompt", "requested"}:
        expected = prompt_variables(t)
    elif order == "legacy":
        expected = legacy_variables(t)
    if raw is None:
        if expected is None:
            raise ValueError("--vars is required with --order custom")
        variables = expected
    else:
        variables = tuple(piece.strip() for piece in raw.split(",") if piece.strip())
    if len(variables) != t:
        raise ValueError(f"expected t={t} variables, got {len(variables)}: {variables}")
    if len(set(variables)) != len(variables):
        raise ValueError("variable order contains a duplicate")
    if expected is not None and variables != expected:
        raise ValueError(
            f"--vars disagrees with built-in {order} order: "
            f"expected {','.join(expected)}, got {','.join(variables)}"
        )
    return variables


def parse_meta(text: str, t: int, variables: tuple[str, ...],
               weights: tuple[int, ...]) -> None:
    meta = one_match(
        r"^META\s+t=(\d+)\s+vars=([^\s]+)\s+weights=([^\s]+)\s*$",
        text, "META line",
    )
    assert meta is not None
    found_t = int(meta.group(1))
    found_variables = tuple(meta.group(2).split(","))
    try:
        found_weights = tuple(int(piece) for piece in meta.group(3).split(","))
    except ValueError as exc:
        raise ValueError("META weights are not integers") from exc
    if found_t != t:
        raise ValueError(f"META t={found_t}, requested t={t}")
    if found_variables != variables:
        raise ValueError(
            "META variable order mismatch: "
            f"found {found_variables}, requested {variables}"
        )
    if found_weights != weights:
        raise ValueError(
            f"META weights mismatch: found {found_weights}, expected {weights}"
        )


def parse_monomial(monomial: str, variables: tuple[str, ...]) -> tuple[int, ...]:
    monomial = monomial.strip()
    if monomial == "1":
        return (0,) * len(variables)
    exponent_by_variable = {variable: 0 for variable in variables}
    for factor in monomial.split("*"):
        factor = factor.strip()
        matches: list[tuple[str, int]] = []
        for variable in variables:
            match = re.fullmatch(re.escape(variable) + r"(?:\^(\d+))?", factor)
            if match:
                matches.append((variable, int(match.group(1) or "1")))
        if len(matches) != 1:
            raise ValueError(f"cannot parse monomial factor {factor!r} in {monomial!r}")
        variable, exponent = matches[0]
        if exponent < 1:
            raise ValueError(f"nonpositive written exponent in {factor!r}")
        if exponent_by_variable[variable] != 0:
            raise ValueError(f"variable {variable!r} occurs twice in {monomial!r}")
        exponent_by_variable[variable] = exponent
    return tuple(exponent_by_variable[variable] for variable in variables)


def indexed_records(pattern: str, text: str, description: str) -> dict[int, str]:
    records: dict[int, str] = {}
    for match in re.finditer(pattern, text, re.MULTILINE):
        index = int(match.group(1))
        if index in records:
            raise ValueError(f"duplicate {description} index {index}")
        records[index] = match.group(2).strip()
    return records


def contiguous_values(records: dict[int, object], description: str) -> list[object]:
    if not records:
        return []
    expected = list(range(1, len(records) + 1))
    actual = sorted(records)
    if actual != expected:
        raise ValueError(f"{description} indices are not contiguous 1..N: {actual}")
    return [records[index] for index in expected]


def extract_exponents(block: str, label: str,
                      variables: tuple[str, ...]) -> tuple[tuple[tuple[int, ...], ...], str]:
    escaped = re.escape(label)
    raw_exp = indexed_records(
        rf"^{escaped}_INITIAL_EXP_(\d+)=(\d+(?:,\d+)*)\s*$",
        block, f"{label}_INITIAL_EXP",
    )
    parsed_exp: dict[int, tuple[int, ...]] = {}
    for index, raw in raw_exp.items():
        vector = tuple(int(piece) for piece in raw.split(","))
        if len(vector) != len(variables):
            raise ValueError(
                f"INITIAL_EXP_{index} has arity {len(vector)}, "
                f"expected {len(variables)}"
            )
        parsed_exp[index] = vector

    raw_lm = indexed_records(
        r"^LM\[(\d+)\]=(\S+)\s*$", block, "LM",
    )
    parsed_lm = {
        index: parse_monomial(monomial, variables)
        for index, monomial in raw_lm.items()
    }
    exp_values = contiguous_values(parsed_exp, "INITIAL_EXP")
    lm_values = contiguous_values(parsed_lm, "LM")
    if exp_values and lm_values and exp_values != lm_values:
        for index, (left, right) in enumerate(zip(exp_values, lm_values), start=1):
            if left != right:
                raise ValueError(
                    f"INITIAL_EXP_{index}={left} disagrees with LM[{index}]={right}"
                )
        raise ValueError("INITIAL_EXP and LM record counts differ")
    if exp_values:
        return tuple(exp_values), "INITIAL_EXP"
    if lm_values:
        return tuple(lm_values), "LM_fallback"
    raise ValueError("initial-generator block has neither INITIAL_EXP nor LM records")


def parse_count(text: str, label: str) -> tuple[int, str]:
    escaped = re.escape(label)
    minimum = one_match(
        rf"^{escaped}_INITIAL_MIN_COUNT=(\d+)\s*$", text,
        f"{label}_INITIAL_MIN_COUNT", required=False,
    )
    gb_size = one_match(
        rf"^{escaped}_GB_SIZE=(\d+)\s*$", text,
        f"{label}_GB_SIZE", required=False,
    )
    if minimum is not None:
        return int(minimum.group(1)), f"{label}_INITIAL_MIN_COUNT"
    if gb_size is not None:
        return int(gb_size.group(1)), f"{label}_GB_SIZE"
    raise ValueError(f"neither {label}_INITIAL_MIN_COUNT nor {label}_GB_SIZE is present")


def validate_antichain(exponents: tuple[tuple[int, ...], ...]) -> None:
    """Prove that no distinct exponent vector divides another.

    For every coordinate j and every occurring value v, ``lower[j][v]`` is a
    bitset of the input vectors whose j-th coordinate is at most v.  A vector
    ``a`` divides ``b`` precisely when its bit survives the intersection of
    ``lower[j][b[j]]`` over all j.  Python's arbitrary-precision integer AND
    performs this scan a machine word at a time in C; ordering the masks by
    population also makes nonrelations terminate as soon as the candidate
    bitset becomes empty.

    This is an exact check, including equal-coordinate faces.  Duplicate
    vectors are rejected explicitly before building the threshold bitsets.
    """
    if not exponents:
        raise ValueError("initial ideal has no generators")
    arity = len(exponents[0])
    first_index: dict[tuple[int, ...], int] = {}
    for index, vector in enumerate(exponents, start=1):
        if len(vector) != arity:
            raise ValueError(
                f"generator {index} has arity {len(vector)}, expected {arity}"
            )
        if any(value < 0 for value in vector):
            raise ValueError(f"negative exponent in generator {index}: {vector}")
        if not any(vector):
            raise ValueError(f"generator {index} is the unit monomial")
        previous = first_index.get(vector)
        if previous is not None:
            raise ValueError(
                f"duplicate generators {previous} and {index}: {vector}"
            )
        first_index[vector] = index

    # lower_masks[j][v] is (bitset, population) for
    # {i : exponents[i][j] <= v}.  Bytearrays make construction linear in the
    # number of coordinates, avoiding a succession of growing bigint shifts.
    lower_masks: list[dict[int, tuple[int, int]]] = []
    byte_width = (len(exponents) + 7) // 8
    for coordinate in range(arity):
        exact: dict[int, bytearray] = {}
        exact_counts: dict[int, int] = {}
        for offset, vector in enumerate(exponents):
            value = vector[coordinate]
            bits = exact.get(value)
            if bits is None:
                bits = bytearray(byte_width)
                exact[value] = bits
                exact_counts[value] = 0
            bits[offset >> 3] |= 1 << (offset & 7)
            exact_counts[value] += 1
        cumulative = 0
        cumulative_count = 0
        lower: dict[int, tuple[int, int]] = {}
        for value in sorted(exact):
            cumulative |= int.from_bytes(exact[value], byteorder="little")
            cumulative_count += exact_counts[value]
            lower[value] = (cumulative, cumulative_count)
        lower_masks.append(lower)

    for offset, vector in enumerate(exponents):
        masks = [
            lower_masks[coordinate][value]
            for coordinate, value in enumerate(vector)
        ]
        # Starting with the sparsest mask minimizes both the candidate set and
        # the effective bigint length of later intersections.
        masks.sort(key=lambda item: item[1])
        self_bit = 1 << offset
        candidates = masks[0][0] ^ self_bit  # self_bit is guaranteed to occur.
        for mask, _ in masks[1:]:
            candidates &= mask
            if not candidates:
                break
        if candidates:
            least_bit = candidates & -candidates
            divisor_offset = least_bit.bit_length() - 1
            divisor = exponents[divisor_offset]
            raise ValueError(
                f"generator {divisor_offset + 1} divides generator {offset + 1}: "
                f"{divisor} <= {vector}"
            )


def derive_pure_powers(exponents: tuple[tuple[int, ...], ...],
                       variables: tuple[str, ...]) -> tuple[tuple[str, int], ...]:
    answer: list[tuple[str, int]] = []
    for position, variable in enumerate(variables):
        powers = [
            vector[position]
            for vector in exponents
            if vector[position] > 0
            and all(value == 0 for index, value in enumerate(vector) if index != position)
        ]
        answer.append((variable, min(powers) if powers else 0))
    return tuple(answer)


def parse_reported_pure_powers(text: str, label: str,
                               variables: tuple[str, ...]) -> tuple[tuple[str, int], ...]:
    escaped = re.escape(label)
    records: dict[str, int] = {}
    for match in re.finditer(
        rf"^{escaped}_PURE_POWER\s+(\S+)=(\d+)\s*$", text, re.MULTILINE
    ):
        variable, exponent = match.group(1), int(match.group(2))
        if variable in records:
            raise ValueError(f"duplicate PURE_POWER record for {variable}")
        records[variable] = exponent
    unexpected = set(records) - set(variables)
    missing = set(variables) - set(records)
    if unexpected or missing:
        raise ValueError(
            f"PURE_POWER variable mismatch; missing={sorted(missing)}, "
            f"unexpected={sorted(unexpected)}"
        )
    return tuple((variable, records[variable]) for variable in variables)


def monomial(vector: tuple[int, ...], variables: tuple[str, ...]) -> str:
    factors: list[str] = []
    for variable, exponent in zip(variables, vector):
        if exponent == 1:
            factors.append(variable)
        elif exponent > 1:
            factors.append(f"{variable}^{exponent}")
    return "*".join(factors) or "1"


def parse_output(output: Path, t: int, label: str, order: str,
                 variables: tuple[str, ...]) -> ParsedInitialIdeal:
    raw = output.read_bytes()
    text = raw.decode("utf-8")
    if re.search(r"(?mi)^\s*\?\s+error occurred|^\s*skipping text .*error", text):
        raise ValueError("transcript contains a Singular error marker")
    weights = tuple(variable_weight(variable, t) for variable in variables)
    parse_meta(text, t, variables, weights)
    escaped = re.escape(label)
    completion = one_match(
        rf"^JOB_DONE\s+t=(\d+)\s+label={escaped}\s*$", text, "JOB_DONE line"
    )
    assert completion is not None
    if int(completion.group(1)) != t:
        raise ValueError(f"JOB_DONE t={completion.group(1)}, requested t={t}")
    block_match = one_match(
        rf"^{escaped}_INITIAL_MIN_GENS_BEGIN\s*$"
        rf"(?s:(.*?))"
        rf"^{escaped}_INITIAL_MIN_GENS_END\s*$",
        text, f"{label} initial-generator block",
    )
    assert block_match is not None
    exponents, exponent_source = extract_exponents(block_match.group(1), label, variables)
    reported_count, count_source = parse_count(text, label)
    if len(exponents) != reported_count:
        raise ValueError(
            f"parsed {len(exponents)} minimal generators, but {count_source}={reported_count}"
        )
    validate_antichain(exponents)
    reported_pure = parse_reported_pure_powers(text, label, variables)
    derived_pure = derive_pure_powers(exponents, variables)
    if reported_pure != derived_pure:
        raise ValueError(
            f"reported pure-power minima {reported_pure} disagree with "
            f"minima derived from exponents {derived_pure}"
        )
    return ParsedInitialIdeal(
        output=output,
        output_sha256=hashlib.sha256(raw).hexdigest(),
        t=t,
        label=label,
        order=order,
        variables=variables,
        weights=weights,
        exponents=exponents,
        exponent_source=exponent_source,
        count_source=count_source,
        reported_count=reported_count,
        reported_pure_powers=reported_pure,
        derived_pure_powers=derived_pure,
    )


def tsv_text(parsed: ParsedInitialIdeal) -> str:
    lines = ["index\texponent_vector\tmonomial"]
    for index, vector in enumerate(parsed.exponents, start=1):
        lines.append(
            f"{index}\t{','.join(map(str, vector))}\t{monomial(vector, parsed.variables)}"
        )
    return "\n".join(lines) + "\n"


def summary_record(parsed: ParsedInitialIdeal, tsv: Path | None) -> dict[str, object]:
    return {
        "status": "PASS",
        "output": str(parsed.output),
        "output_sha256": parsed.output_sha256,
        "t": parsed.t,
        "label": parsed.label,
        "order": parsed.order,
        "variables": list(parsed.variables),
        "weights": list(parsed.weights),
        "minimal_generator_count": len(parsed.exponents),
        "count_source": parsed.count_source,
        "exponent_source": parsed.exponent_source,
        "indices_contiguous": True,
        "divisibility_antichain": True,
        "antichain_method": "exact_coordinate_threshold_bitsets",
        "pure_power_minima_validated": True,
        "pure_powers": dict(parsed.derived_pure_powers),
        "tsv": str(tsv) if tsv is not None else None,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="completed Singular stdout")
    parser.add_argument("--t", type=int, required=True)
    parser.add_argument("--label", default="FULL")
    parser.add_argument(
        "--order", choices=("prompt", "requested", "legacy", "custom"),
        default="prompt",
    )
    parser.add_argument(
        "--vars", "--order-vars", dest="variables",
        help="comma-separated variables in exponent-vector order",
    )
    parser.add_argument("--tsv", type=Path, help="write validated TSV here")
    parser.add_argument("--summary-json", type=Path, help="write validation JSON here")
    args = parser.parse_args()
    if args.t < 2:
        parser.error("--t must be at least 2")
    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", args.label):
        parser.error("--label must be a Singular-style identifier")
    try:
        variables = parse_variables(args.variables, args.t, args.order)
        parsed = parse_output(args.output, args.t, args.label, args.order, variables)
        table = tsv_text(parsed)
        if args.tsv is None:
            sys.stdout.write(table)
            record = summary_record(parsed, None)
            print(json.dumps(record, sort_keys=True), file=sys.stderr)
        else:
            args.tsv.parent.mkdir(parents=True, exist_ok=True)
            args.tsv.write_text(table, encoding="utf-8")
            record = summary_record(parsed, args.tsv)
            print(json.dumps(record, indent=2, sort_keys=True))
        if args.summary_json is not None:
            args.summary_json.parent.mkdir(parents=True, exist_ok=True)
            args.summary_json.write_text(
                json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8"
            )
    except (OSError, UnicodeError, ValueError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
