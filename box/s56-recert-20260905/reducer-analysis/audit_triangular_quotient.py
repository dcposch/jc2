#!/usr/bin/env python3
"""Independent structural/custody audit of a triangular S5/S6 quotient.

This deliberately does not import triangular_preprocess.py.  It checks the
stored plan directly against the frozen row table and then checks that an
emitted Singular script implements that plan without dropping a non-pivot
row or an unexplained unknown.  When a preprocess stdout dump is supplied it
also validates every runtime marker and the reduced-row envelope used by the
modular msolve screen.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import re
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
IDENTIFIER = re.compile(r"[A-Za-z][A-Za-z0-9_]*")
FACTOR = re.compile(r"([A-Za-z][A-Za-z0-9_]*)(?:\^(\d+))?$")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def exactly_one(pattern: str, text: str, label: str, flags: int = 0) -> str:
    matches = re.findall(pattern, text, flags)
    if len(matches) != 1:
        raise ValueError(f"expected exactly one {label}; found {len(matches)}")
    value = matches[0]
    if isinstance(value, tuple):
        raise TypeError(f"internal error: tuple match for {label}")
    return value


def parse_rows(path: Path) -> list[dict]:
    lines = path.read_text(encoding="utf-8", errors="strict").splitlines()
    if not lines or lines[0] != "source_index|h_power|x_power|y_power|expr":
        raise ValueError("row table header mismatch")
    rows = []
    for line in lines[1:]:
        if not line:
            continue
        fields = line.split("|", 4)
        if len(fields) != 5:
            raise ValueError("malformed row-table line")
        index, h_power, x_power, y_power, expression = fields
        rows.append(
            {
                "index": int(index),
                "h_power": int(h_power),
                "x_power": int(x_power),
                "y_power": int(y_power),
                "expr": expression,
            }
        )
    if [row["index"] for row in rows] != list(range(len(rows))):
        raise ValueError("row indices are not consecutive from zero")
    return rows


def strip_outer_parentheses(expression: str) -> str:
    expression = expression.strip()
    if expression.startswith("(") and expression.endswith(")"):
        depth = 0
        for index, character in enumerate(expression):
            if character == "(":
                depth += 1
            elif character == ")":
                depth -= 1
                if depth == 0 and index != len(expression) - 1:
                    return expression
            if depth < 0:
                raise ValueError("unbalanced parentheses")
        if depth != 0:
            raise ValueError("unbalanced parentheses")
        return expression[1:-1]
    return expression


def parse_flat_terms(expression: str) -> list[tuple[Fraction, list[tuple[str, int]]]]:
    body = strip_outer_parentheses(expression)
    if "(" in body or ")" in body:
        raise ValueError("unexpected internal parentheses in source row")
    raw_terms = re.findall(r"[+-]?[^+-]+", body)
    if not raw_terms or "".join(raw_terms) != body:
        raise ValueError("term splitting did not round-trip")
    parsed = []
    for raw_term in raw_terms:
        sign = -1 if raw_term.startswith("-") else 1
        unsigned = raw_term.lstrip("+-")
        coefficient = Fraction(sign)
        variables: list[tuple[str, int]] = []
        for raw_factor in unsigned.split("*"):
            match = FACTOR.fullmatch(raw_factor)
            if match:
                variables.append((match.group(1), int(match.group(2) or 1)))
            else:
                try:
                    coefficient *= Fraction(raw_factor)
                except (ValueError, ZeroDivisionError) as exc:
                    raise ValueError(f"unparsed factor {raw_factor!r}") from exc
        parsed.append((coefficient, variables))
    return parsed


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return value == divisor
        divisor += 1 if divisor == 2 else 2
    return True


def field_scalar_ok(scalar: Fraction, characteristic: int) -> bool:
    if characteristic == 0:
        return scalar != 0
    return scalar.numerator % characteristic != 0 and scalar.denominator % characteristic != 0


def parse_script_ring(script_text: str, ring_name: str) -> tuple[int, list[str]]:
    match = re.findall(
        rf"^ring {re.escape(ring_name)}=(\d+),\(([^\n]*)\),dp;$",
        script_text,
        re.MULTILINE,
    )
    if len(match) != 1:
        raise ValueError(f"expected exactly one {ring_name} ring declaration")
    characteristic, variables = match[0]
    names = variables.split(",")
    if not names or len(names) != len(set(names)):
        raise ValueError(f"invalid or duplicate variables in {ring_name}")
    return int(characteristic), names


def parse_dump(dump_text: str) -> tuple[list[str], list[str]]:
    variable_line = exactly_one(
        r"^DUMP__VARS ([A-Za-z0-9_,]+)\s*$", dump_text, "DUMP__VARS", re.MULTILINE
    )
    variables = variable_line.split(",")
    rows = re.findall(r"^DUMP__ROW (.+?)\s*$", dump_text, re.MULTILINE)
    declared_count = int(
        exactly_one(r"^DUMP__COUNT (\d+)\s*$", dump_text, "DUMP__COUNT", re.MULTILINE)
    )
    if declared_count != len(rows):
        raise ValueError(f"dump count mismatch: marker {declared_count}, actual {len(rows)}")
    if not rows:
        raise ValueError("dump contains no reduced rows")
    return variables, rows


def audit(args: argparse.Namespace) -> dict:
    meta_path = args.meta.resolve()
    plan_path = args.plan.resolve()
    script_path = args.script.resolve()
    dump_path = args.dump.resolve() if args.dump else None
    meta = json.loads(meta_path.read_text(encoding="utf-8", errors="strict"))
    plan = json.loads(plan_path.read_text(encoding="utf-8", errors="strict"))
    rows_path = ROOT / meta["rows_path"]
    rows = parse_rows(rows_path)
    source_variables = list(meta["variables"])
    if len(source_variables) != len(set(source_variables)):
        raise ValueError("duplicate variables in source metadata")
    source_variable_set = set(source_variables)

    # Frozen-source custody and basic inventory.
    if plan["meta_sha256"] != sha256(meta_path):
        raise ValueError("plan/meta hash mismatch")
    if plan["rows_sha256"] != sha256(rows_path):
        raise ValueError("plan/rows hash mismatch")
    if plan["source_row_count"] != len(rows):
        raise ValueError("plan/source row-count mismatch")
    if plan["source_variable_count"] != len(source_variables):
        raise ValueError("plan/source variable-count mismatch")
    pivot_order = plan["pivot_order"]
    if [item["step"] for item in pivot_order] != list(range(len(pivot_order))):
        raise ValueError("plan steps are not consecutive from zero")
    if len(pivot_order) != plan["pivot_count"]:
        raise ValueError("plan pivot-count mismatch")
    pivot_variables = [item["variable"] for item in pivot_order]
    pivot_rows = [item["row_index"] for item in pivot_order]
    if len(set(pivot_variables)) != len(pivot_variables):
        raise ValueError("a pivot variable appears more than once")
    if len(set(pivot_rows)) != len(pivot_rows):
        raise ValueError("a source row is used for more than one pivot")
    if not set(pivot_variables) <= source_variable_set:
        raise ValueError("plan pivots outside the declared source ring")

    # Independently prove each planned source row is a*v+q and the dependency
    # order removes every other pivot from q before this step.
    seen: set[str] = set()
    scalar_histogram: Counter[str] = Counter()
    for item in pivot_order:
        row = rows[item["row_index"]]
        for coordinate in ("h_power", "x_power", "y_power"):
            if item[coordinate] != row[coordinate]:
                raise ValueError(f"pivot step {item['step']} coordinate mismatch")
        parsed_terms = parse_flat_terms(row["expr"])
        variable = item["variable"]
        terms_with_variable = [term for term in parsed_terms if variable in {v for v, _ in term[1]}]
        if len(terms_with_variable) != 1:
            raise ValueError(f"pivot {variable} occurs in {len(terms_with_variable)} terms")
        coefficient, factors = terms_with_variable[0]
        if factors != [(variable, 1)]:
            raise ValueError(f"pivot {variable} is not a pure scalar-linear term")
        planned_scalar = Fraction(item["scalar_coefficient"].strip("()"))
        if coefficient != planned_scalar or planned_scalar == 0:
            raise ValueError(f"pivot {variable} scalar mismatch")
        row_identifiers = set(IDENTIFIER.findall(row["expr"]))
        if not row_identifiers <= source_variable_set:
            raise ValueError(f"pivot row {item['row_index']} uses undeclared symbols")
        actual_dependencies = (row_identifiers & set(pivot_variables)) - {variable}
        if actual_dependencies != set(item["dependencies"]):
            raise ValueError(f"pivot {variable} dependency set mismatch")
        if not actual_dependencies <= seen:
            raise ValueError(f"pivot {variable} has a forward/cyclic dependency")
        seen.add(variable)
        scalar_histogram[str(planned_scalar)] += 1

    expected_active = source_variable_set - set(pivot_variables)
    planned_active = list(plan["active_variables"])
    if len(planned_active) != len(set(planned_active)):
        raise ValueError("duplicate active variables in plan")
    if set(planned_active) != expected_active:
        missing = sorted(expected_active - set(planned_active))
        extra = sorted(set(planned_active) - expected_active)
        raise ValueError(f"unknown preservation failure: missing={missing}, extra={extra}")
    if len(planned_active) != plan["active_variable_count"]:
        raise ValueError("active-variable count mismatch")

    # Bind the concrete Singular program to the audited plan/source inventory.
    script_text = script_path.read_text(encoding="utf-8", errors="strict")
    for label, expected in (
        ("meta_sha256", sha256(meta_path)),
        ("rows_sha256", sha256(rows_path)),
    ):
        actual = exactly_one(
            rf"^// {label}=([0-9a-f]{{64}})\s*$", script_text, label, re.MULTILINE
        )
        if actual != expected:
            raise ValueError(f"script {label} mismatch")
    comment_characteristic = int(
        exactly_one(
            r"^// characteristic=(\d+)\s*$", script_text, "characteristic", re.MULTILINE
        )
    )
    branch = exactly_one(r"^// branch=([^\s]+)\s*$", script_text, "branch", re.MULTILINE)
    coordinate_filter_matches = re.findall(
        r"^// coordinate_filter=([^\s]+)\s*$", script_text, re.MULTILINE
    )
    if len(coordinate_filter_matches) > 1:
        raise ValueError("ambiguous coordinate_filter marker")
    # Early full-row scripts predate this documentary comment.  Absence is
    # acceptable because the exact JOld byte reconstruction below is the
    # stronger check: it proves every non-pivot source row was retained.
    coordinate_filter = coordinate_filter_matches[0] if coordinate_filter_matches else "unmarked"
    if coordinate_filter not in {"none", "unmarked"}:
        raise ValueError("audit is for the full-row system, not a coordinate-filter subset")
    if comment_characteristic != args.characteristic:
        raise ValueError("requested characteristic differs from script")
    if comment_characteristic != 0 and not is_prime(comment_characteristic):
        raise ValueError("positive characteristic is not prime")
    for item in pivot_order:
        scalar = Fraction(item["scalar_coefficient"].strip("()"))
        if not field_scalar_ok(scalar, comment_characteristic):
            raise ValueError(
                f"pivot scalar at step {item['step']} is not a field unit in characteristic "
                f"{comment_characteristic}"
            )

    old_char, old_variables = parse_script_ring(script_text, "Old")
    reduced_char, reduced_variables = parse_script_ring(script_text, "Reduced")
    if old_char != comment_characteristic or reduced_char != comment_characteristic:
        raise ValueError("ring/script characteristic mismatch")
    if len(old_variables) != len(source_variables) + 1 or set(old_variables) != source_variable_set | {"T"}:
        raise ValueError("Old ring does not preserve the complete source unknown inventory plus T")
    if reduced_variables != planned_active + ["T"]:
        raise ValueError("Reduced ring variables differ from exactly active(plan)+T")

    step_by_variable = {item["variable"]: item["step"] for item in pivot_order}
    expected_dependency_commands: list[str] = []
    for item in pivot_order:
        step = item["step"]
        row = rows[item["row_index"]]
        variable = item["variable"]
        scalar_text = item["scalar_coefficient"]
        declaration = f"poly PP_{step:03d}={row['expr']};"
        if script_text.count(declaration) != 1:
            raise ValueError(f"script pivot expression mismatch at step {step}")
        for dependency in item["dependencies"]:
            command = (
                f"PP_{step:03d}=subst(PP_{step:03d},{dependency},"
                f"REP_{step_by_variable[dependency]:03d});"
            )
            expected_dependency_commands.append(command)
            if script_text.count(command) != 1:
                raise ValueError(f"missing/ambiguous dependency substitution at step {step}")
        required_pivot_lines = [
            f"poly DER_{step:03d}=diff(PP_{step:03d},{variable});",
            f"if (DER_{step:03d} != ({scalar_text})) "
            f'{{ "PIVOT_DERIVATIVE_FAIL step={step} variable={variable}"; exit(91); }}',
            f"if (subst(PP_{step:03d},{variable},0) != "
            f"(PP_{step:03d}-({scalar_text})*{variable})) "
            f'{{ "PIVOT_AFFINE_FAIL step={step} variable={variable}"; exit(92); }}',
            f"poly REP_{step:03d}=-(PP_{step:03d}-({scalar_text})*{variable})/({scalar_text});",
            f"if (subst(REP_{step:03d},{variable},0) != REP_{step:03d}) "
            f'{{ "PIVOT_REPLACEMENT_FAIL step={step} variable={variable}"; exit(93); }}',
            f"if (subst(PP_{step:03d},{variable},REP_{step:03d}) != 0) "
            f'{{ "PIVOT_IMAGE_FAIL step={step} variable={variable}"; exit(94); }}',
            f'"PIVOT_OK step={step} variable={variable}";',
        ]
        for line in required_pivot_lines:
            if script_text.count(line) != 1:
                raise ValueError(f"missing/ambiguous pivot proof instruction at step {step}")
        command = f"JOld=subst(JOld,{variable},REP_{step:03d});"
        if script_text.count(command) != 1:
            raise ValueError(f"missing/ambiguous residual-ideal substitution at step {step}")

    actual_dependency_commands = re.findall(
        r"^PP_\d{3}=subst\(PP_\d{3},[A-Za-z0-9_]+,REP_\d{3}\);$",
        script_text,
        re.MULTILINE,
    )
    if actual_dependency_commands != expected_dependency_commands:
        raise ValueError("script dependency-substitution sequence differs from plan")

    extras = [] if branch == "none" else ["s2^2-s2+1"] if branch == "q2" else None
    if extras is None:
        raise ValueError(f"unsupported branch {branch!r}")
    residual_expressions = [
        row["expr"] for row in rows if row["index"] not in set(pivot_rows)
    ] + extras
    expected_jold = (
        "ideal JOld="
        + ",\n".join(residual_expressions)
        + ",\n"
        + f"(T*({meta['sat']})-1);"
    )
    if script_text.count(expected_jold) != 1:
        raise ValueError("JOld is not exactly every non-pivot row + branch + Rabinowitsch")
    if script_text.count("ideal JReduced=imap(Old,JOld);") != 1:
        raise ValueError("missing/ambiguous final coefficient-preserving imap")
    if len(re.findall(r"^JOld=subst\(JOld,", script_text, re.MULTILINE)) != len(pivot_order):
        raise ValueError("unexpected number of ideal substitutions")

    dump_record = None
    if dump_path is not None:
        dump_text = dump_path.read_text(encoding="utf-8", errors="strict")
        if re.search(r"(?:FAIL|error occurred|halt)", dump_text, re.IGNORECASE):
            raise ValueError("failure/error marker in dump stdout")
        if len(re.findall(r"^SCRIPT_DONE\s*$", dump_text, re.MULTILINE)) != 1:
            raise ValueError("dump lacks a unique SCRIPT_DONE marker")
        runtime_pivots = re.findall(
            r"^PIVOT_OK step=(\d+) variable=([A-Za-z0-9_]+)\s*$",
            dump_text,
            re.MULTILINE,
        )
        expected_runtime = [(str(item["step"]), item["variable"]) for item in pivot_order]
        if runtime_pivots != expected_runtime:
            raise ValueError("runtime PIVOT_OK sequence differs from audited plan")
        runtime_substitutions = re.findall(
            r"^IDEAL_SUBST_OK step=(\d+) variable=([A-Za-z0-9_]+)\s*$",
            dump_text,
            re.MULTILINE,
        )
        if runtime_substitutions != expected_runtime:
            raise ValueError("runtime IDEAL_SUBST_OK sequence differs from audited plan")
        expected_jold_count = len(rows) - len(pivot_order) + len(extras) + 1
        actual_jold_count = int(
            exactly_one(r"^JOLD_OK rows=(\d+)\s*$", dump_text, "JOLD_OK", re.MULTILINE)
        )
        if actual_jold_count != expected_jold_count:
            raise ValueError("runtime JOld count mismatch")
        triangular_matches = re.findall(
            r"^TRIANGULAR_OK pivots=(\d+) source_rows=(\d+)\s+"
            r"residual_rows=(\d+) active_including_T=(\d+)\s*$",
            dump_text,
            re.MULTILINE,
        )
        if len(triangular_matches) != 1:
            raise ValueError("dump lacks a unique TRIANGULAR_OK marker")
        runtime_pivot_count, runtime_source_count, runtime_residual_count, runtime_active_count = map(
            int, triangular_matches[0]
        )
        dump_variables, dump_rows = parse_dump(dump_text)
        if (runtime_pivot_count, runtime_source_count) != (len(pivot_order), len(rows)):
            raise ValueError("TRIANGULAR_OK plan/source counts mismatch")
        if runtime_residual_count != len(dump_rows):
            raise ValueError("TRIANGULAR_OK residual count differs from dumped rows")
        if runtime_active_count != len(reduced_variables) or dump_variables != reduced_variables:
            raise ValueError("dumped active variables differ from audited Reduced ring")
        allowed = set(reduced_variables)
        max_abs_numerator = 0
        max_denominator = 1
        for index, expression in enumerate(dump_rows):
            forbidden = "(),;" if comment_characteristic == 0 else "(),;/"
            if any(mark in expression for mark in forbidden):
                syntax = "flat exact-Q" if comment_characteristic == 0 else "flat modular msolve"
                raise ValueError(f"dump row {index} is not {syntax} syntax")
            identifiers = set(IDENTIFIER.findall(expression))
            if not identifiers <= allowed:
                raise ValueError(f"dump row {index} contains unknown identifiers")
            # Singular's string form is expanded.  Check rational numeric
            # factors (but not exponents or digits embedded in identifiers).
            for coefficient, _factors in parse_flat_terms(expression):
                if comment_characteristic and coefficient.denominator != 1:
                    raise ValueError(f"dump row {index} contains a nonintegral coefficient")
                max_abs_numerator = max(max_abs_numerator, abs(coefficient.numerator))
                max_denominator = max(max_denominator, coefficient.denominator)
                if comment_characteristic and abs(coefficient.numerator) >= comment_characteristic:
                    raise ValueError(f"dump row {index} contains an unreduced coefficient token")
        dump_record = {
            "path": str(dump_path.relative_to(ROOT)),
            "sha256": sha256(dump_path),
            "generator_count": len(dump_rows),
            "variable_count": len(dump_variables),
            "max_abs_coefficient": max_abs_numerator if comment_characteristic else None,
            "max_abs_coefficient_numerator": max_abs_numerator,
            "max_coefficient_denominator": max_denominator,
            "runtime_complete": True,
        }

    return {
        "schema": "jc2.s56-recert.independent-triangular-audit/v1",
        "status": "PASS",
        "equivalence": (
            "iterated quotient isomorphism by audited scalar-unit pivots; "
            "all non-pivot rows retained; no weight-floor unknown truncation"
        ),
        "characteristic": comment_characteristic,
        "branch": branch,
        "custody": {
            "meta": str(meta_path.relative_to(ROOT)),
            "meta_sha256": sha256(meta_path),
            "rows": str(rows_path.relative_to(ROOT)),
            "rows_sha256": sha256(rows_path),
            "plan": str(plan_path.relative_to(ROOT)),
            "plan_sha256": sha256(plan_path),
            "script": str(script_path.relative_to(ROOT)),
            "script_sha256": sha256(script_path),
        },
        "counts": {
            "source_variables": len(source_variables),
            "pivot_variables": len(pivot_variables),
            "active_variables_before_T": len(planned_active),
            "source_rows": len(rows),
            "pivot_rows": len(pivot_rows),
            "nonpivot_rows": len(rows) - len(pivot_rows),
            "branch_rows": len(extras),
            "rabinowitsch_rows": 1,
        },
        "pivot_scalar_histogram": dict(sorted(scalar_histogram.items())),
        "dump": dump_record,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--meta", type=Path, required=True)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--script", type=Path, required=True)
    parser.add_argument("--characteristic", type=int, required=True)
    parser.add_argument("--dump", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        record = audit(args)
    except Exception as exc:
        print(f"AUDIT_FAIL: {exc}", file=sys.stderr)
        raise
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(record, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
