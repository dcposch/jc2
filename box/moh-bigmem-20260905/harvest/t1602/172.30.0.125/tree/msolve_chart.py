#!/usr/bin/env python3
"""Custody-preserving conversion of Moh full-chart rows to msolve input.

The chart producers write pipe-delimited ``*_rows.tsv`` files whose fifth
column is an expanded Singular polynomial.  msolve identifiers cannot contain
underscores, so this program performs a token-wise bijective rename, appends
the Rabinowitsch equation ``z*c-1``, and delegates the final serialization to
``msolveio.emit_system``.  There is deliberately no hand-written emitter
fallback.

This file does not invoke msolve.  Its ``status`` subcommand parses only the
documented ``-g 2`` reduced-Groebner output envelope.  In particular a
characteristic-zero ``[1]`` from msolve 0.6.5/0.10.1 is labelled modular-only:
those versions can return after the first modular prime without a rational
membership certificate.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import re
import sys
import tempfile
from pathlib import Path
from typing import Any, Callable, Iterable, Sequence


BASE = Path(__file__).resolve().parent
REPO = BASE.parents[1]
ROWS_HEADER = "source_index|h_power|x_power|y_power|expr"
ORIGINAL_IDENTIFIER = re.compile(r"[A-Za-z][A-Za-z0-9_]*")
SAFE_IDENTIFIER = re.compile(r"[A-Za-z][A-Za-z0-9]*\Z")
INTEGER = re.compile(r"[+-]?[0-9]+\Z")


class ChartError(RuntimeError):
    """A typed refusal: the requested bytes are not safe msolve input."""


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def file_record(path: Path) -> dict[str, Any]:
    resolved = path.resolve(strict=True)
    return {
        "path": str(resolved),
        "bytes": resolved.stat().st_size,
        "sha256": sha256_path(resolved),
    }


def atomic_write(path: Path, payload: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=path.parent
    )
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    except BaseException:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def load_json_object(path: Path, what: str) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ChartError(f"cannot read {what} JSON {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ChartError(f"{what} JSON {path} must contain an object")
    return value


def resolve_recorded_path(text: str, *, metadata_path: Path) -> Path:
    candidate = Path(text)
    if candidate.is_absolute():
        return candidate.resolve()
    repo_candidate = (REPO / candidate).resolve()
    if repo_candidate.exists():
        return repo_candidate
    return (metadata_path.parent / candidate).resolve()


def normalize_stem(class_id: str, stem: str) -> str:
    return stem if stem.startswith(f"{class_id}_") else f"{class_id}_{stem}"


def locate_inputs(args: argparse.Namespace) -> tuple[str, Path, Path, Path | None]:
    if args.meta is not None:
        metadata_path = Path(args.meta).resolve()
        stem = args.stem or metadata_path.name.removesuffix(".json")
        class_path = metadata_path.parent.parent / "class.json"
        if not class_path.exists():
            class_path = None
    else:
        if not args.class_id or not args.stem:
            raise ChartError("emit requires --class-id and --stem, or --meta")
        stem = normalize_stem(args.class_id, args.stem)
        class_dir = Path(args.root).resolve() / "classes" / args.class_id
        metadata_path = class_dir / "meta" / f"{stem}.json"
        class_path = class_dir / "class.json"
        if not class_path.exists():
            class_path = None

    if not metadata_path.is_file():
        raise ChartError(f"metadata file does not exist: {metadata_path}")
    metadata = load_json_object(metadata_path, "metadata")
    if args.rows is not None:
        rows_path = Path(args.rows).resolve()
    else:
        recorded = metadata.get("rows_path")
        if not isinstance(recorded, str) or not recorded:
            raise ChartError(f"metadata {metadata_path} has no string rows_path")
        rows_path = resolve_recorded_path(recorded, metadata_path=metadata_path)
    if not rows_path.is_file():
        raise ChartError(f"rows file does not exist: {rows_path}")
    return stem, metadata_path, rows_path, class_path


def strip_verified_outer_parentheses(source: str) -> tuple[str, bool]:
    """Remove at most one pair, and only if it encloses the entire string."""
    text = source.strip()
    if len(text) < 2 or text[0] != "(" or text[-1] != ")":
        return text, False
    depth = 0
    for position, char in enumerate(text):
        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
            if depth < 0:
                raise ChartError("unbalanced ')' in row expression")
            if depth == 0 and position != len(text) - 1:
                return text, False
    if depth != 0:
        raise ChartError("unbalanced '(' in row expression")
    return text[1:-1].strip(), True


def make_variable_map(
    originals: Sequence[str], localization: str
) -> tuple[dict[str, str], tuple[str, ...]]:
    if not originals:
        raise ChartError("metadata variables list is empty")
    if len(set(originals)) != len(originals):
        raise ChartError("metadata variables list contains duplicates")
    for name in originals:
        if not isinstance(name, str) or ORIGINAL_IDENTIFIER.fullmatch(name) is None:
            raise ChartError(f"invalid original variable name: {name!r}")
    if localization != "c":
        raise ChartError(
            f"this chart lane requires localization at literal c, metadata says {localization!r}"
        )
    if localization not in originals:
        raise ChartError("localization variable c is absent from metadata variables")

    mapping: dict[str, str] = {}
    serial = 1
    for original in originals:
        if original == localization:
            safe = "c"
        else:
            safe = f"v{serial}"
            serial += 1
        mapping[original] = safe
    safe_order = tuple(mapping[name] for name in originals)
    if len(set(safe_order)) != len(safe_order):
        raise ChartError("internal error: safe variable map is not injective")
    if "z" in safe_order:
        raise ChartError("internal error: Rabinowitsch slack z collides with variable map")
    if any(SAFE_IDENTIFIER.fullmatch(name) is None for name in safe_order):
        raise ChartError("internal error: generated an msolve-unsafe variable name")
    return mapping, safe_order


def translate_expression(
    source: str,
    *,
    mapping: dict[str, str],
    row_number: int,
) -> tuple[str, bool]:
    stripped, removed_outer = strip_verified_outer_parentheses(source)
    if not stripped:
        raise ChartError(f"row {row_number}: empty expression")
    identifiers = ORIGINAL_IDENTIFIER.findall(stripped)
    unknown = sorted(set(identifiers) - set(mapping))
    if unknown:
        raise ChartError(
            f"row {row_number}: identifier(s) absent from metadata variables: {unknown}"
        )

    translated = ORIGINAL_IDENTIFIER.sub(lambda match: mapping[match.group(0)], stripped)
    safe_ids = ORIGINAL_IDENTIFIER.findall(translated)
    allowed_safe = set(mapping.values())
    leftovers = sorted(set(safe_ids) - allowed_safe)
    if leftovers:
        raise ChartError(f"row {row_number}: unsafe/unmapped translated identifiers: {leftovers}")
    inverse = {safe: original for original, safe in mapping.items()}
    roundtrip = ORIGINAL_IDENTIFIER.sub(
        lambda match: inverse[match.group(0)], translated
    )
    compact_source = re.sub(r"\s+", "", stripped)
    compact_roundtrip = re.sub(r"\s+", "", roundtrip)
    if compact_roundtrip != compact_source:
        raise ChartError(f"row {row_number}: variable rename failed exact roundtrip")
    if any("_" in identifier for identifier in safe_ids):
        raise ChartError(f"row {row_number}: underscore survived variable translation")
    return translated, removed_outer


def iter_rows(path: Path) -> Iterable[tuple[int, str]]:
    try:
        stream = path.open("r", encoding="utf-8", newline="")
    except (OSError, UnicodeError) as exc:
        raise ChartError(f"cannot open rows file {path}: {exc}") from exc
    with stream:
        first = stream.readline()
        if not first:
            raise ChartError(f"rows file is empty: {path}")
        header = first.rstrip("\r\n")
        if header != ROWS_HEADER:
            raise ChartError(
                f"unexpected rows header {header!r}; expected {ROWS_HEADER!r}"
            )
        for physical_line, raw in enumerate(stream, start=2):
            line = raw.rstrip("\r\n")
            if not line:
                raise ChartError(f"rows line {physical_line}: blank line")
            fields = line.split("|", 4)
            if len(fields) != 5:
                raise ChartError(
                    f"rows line {physical_line}: expected five pipe-delimited fields"
                )
            if fields[4] == "expr" and line == ROWS_HEADER:
                raise ChartError(f"rows line {physical_line}: repeated header")
            for label, value in zip(
                ("source_index", "h_power", "x_power", "y_power"), fields[:4]
            ):
                if INTEGER.fullmatch(value) is None:
                    raise ChartError(
                        f"rows line {physical_line}: {label} is not an integer: {value!r}"
                    )
            yield physical_line, fields[4]


def import_emitter() -> tuple[Callable[..., str], dict[str, str]]:
    try:
        import msolveio
        from msolveio import emit_system
    except (ImportError, AttributeError) as exc:
        raise ChartError(
            "msolveio with emit_system is required; no fallback emitter is permitted"
        ) from exc
    versions = {"msolveio": str(getattr(msolveio, "__version__", "unknown"))}
    try:
        import qqideal
    except ImportError:
        versions["qqideal"] = "not-importable"
    else:
        versions["qqideal"] = str(getattr(qqideal, "__version__", "unknown"))
    return emit_system, versions


def parse_row_indices(specification: str | None) -> tuple[int, ...] | None:
    """Parse a comma-separated list of positive ordinals and closed ranges."""
    if specification is None:
        return None
    selected: set[int] = set()
    for token in specification.split(","):
        token = token.strip()
        if not token:
            raise ChartError("--row-indices contains an empty token")
        if "-" in token:
            left, separator, right = token.partition("-")
            if not separator or not left.isdigit() or not right.isdigit():
                raise ChartError(f"invalid --row-indices range: {token!r}")
            start, stop = int(left), int(right)
            if start < 1 or stop < start:
                raise ChartError(f"invalid --row-indices range: {token!r}")
            selected.update(range(start, stop + 1))
        else:
            if not token.isdigit() or int(token) < 1:
                raise ChartError(f"invalid --row-indices ordinal: {token!r}")
            selected.add(int(token))
    if not selected:
        raise ChartError("--row-indices selects no generators")
    return tuple(sorted(selected))


def emit_chart(args: argparse.Namespace) -> dict[str, Any]:
    stem, metadata_path, rows_path, class_path = locate_inputs(args)
    if args.source_characteristic < 0:
        raise ChartError("--source-characteristic must be nonnegative")
    if args.source_characteristic not in (0, args.characteristic):
        raise ChartError(
            "finite-field source rows may only be emitted in the same characteristic"
        )
    metadata = load_json_object(metadata_path, "metadata")
    originals = metadata.get("variables")
    if not isinstance(originals, list) or not all(isinstance(v, str) for v in originals):
        raise ChartError(f"metadata {metadata_path} has no string-list variables")
    localization = metadata.get("sat")
    if not isinstance(localization, str):
        raise ChartError(f"metadata {metadata_path} has no string sat field")
    nested = metadata.get("meta")
    if isinstance(nested, dict):
        nested_sat = nested.get("saturation_factor")
        if nested_sat is not None and nested_sat != localization:
            raise ChartError(
                f"metadata saturation mismatch: sat={localization!r}, "
                f"meta.saturation_factor={nested_sat!r}"
            )

    mapping, safe_without_slack = make_variable_map(originals, localization)
    if args.row_limit is not None and args.row_limit < 1:
        raise ChartError("--row-limit must be a positive integer")
    selected_ordinals = parse_row_indices(args.row_indices)
    if args.row_limit is not None and selected_ordinals is not None:
        raise ChartError("--row-limit and --row-indices are mutually exclusive")
    selected_set = set(selected_ordinals or ())
    translated: list[str] = []
    total_row_generators = 0
    outer_parentheses_removed = 0
    for physical_line, expression in iter_rows(rows_path):
        total_row_generators += 1
        polynomial, removed = translate_expression(
            expression, mapping=mapping, row_number=physical_line
        )
        if re.sub(r"\s+", "", polynomial) in {"0", "+0", "-0"}:
            raise ChartError(f"rows line {physical_line}: explicit zero generator")
        include = (
            total_row_generators in selected_set
            if selected_ordinals is not None
            else args.row_limit is None or total_row_generators <= args.row_limit
        )
        if include:
            translated.append(polynomial)
            outer_parentheses_removed += int(removed)
    if args.row_limit is not None and args.row_limit > total_row_generators:
        raise ChartError(
            f"--row-limit {args.row_limit} exceeds the {total_row_generators} rows"
        )
    if selected_ordinals is not None and selected_ordinals[-1] > total_row_generators:
        raise ChartError(
            f"--row-indices contains {selected_ordinals[-1]}, exceeding the "
            f"{total_row_generators} rows"
        )
    if not translated:
        raise ChartError(
            f"rows file has a header but zero generators; refusing {rows_path}"
        )

    safe_localization = mapping[localization]
    if safe_localization != "c":
        raise ChartError("internal error: localization variable was not preserved as c")
    slack = "z"
    rabinowitsch = f"{slack}*{safe_localization}-1"
    all_polynomials = [*translated, rabinowitsch]
    ordered_without_slack = (
        tuple(reversed(safe_without_slack))
        if args.order_mode == "reverse-source"
        else safe_without_slack
    )
    safe_order = (*ordered_without_slack, slack)

    emit_system, versions = import_emitter()
    try:
        rendered = emit_system(
            all_polynomials,
            variables=safe_order,
            characteristic=args.characteristic,
        )
    except Exception as exc:
        raise ChartError(f"msolveio.emit_system refused the chart: {exc}") from exc
    payload = rendered.encode("utf-8")

    output_path = Path(args.output).resolve()
    manifest_path = (
        Path(args.manifest).resolve()
        if args.manifest
        else output_path.with_suffix(output_path.suffix + ".json")
    )
    if output_path == manifest_path:
        raise ChartError("output and manifest paths must differ")

    sources: dict[str, Any] = {
        "rows": file_record(rows_path),
        "metadata": file_record(metadata_path),
    }
    if class_path is not None:
        sources["class"] = file_record(class_path)
    builder = args.builder if args.builder is not None else metadata.get("builder")
    if isinstance(builder, str) and builder:
        builder_path = (
            Path(builder).resolve()
            if args.builder is not None
            else resolve_recorded_path(builder, metadata_path=metadata_path)
        )
        if builder_path.is_file():
            sources["builder"] = file_record(builder_path)
        elif args.builder is not None:
            raise ChartError(f"explicit --builder is not a file: {builder_path}")

    manifest: dict[str, Any] = {
        "schema": "moh14-msolve-chart-v1",
        "stem": stem,
        "characteristic": args.characteristic,
        "source_rows_characteristic": args.source_characteristic,
        "sources": sources,
        "source_row_generators": len(translated),
        "source_total_row_generators": total_row_generators,
        "row_selection": (
            {
                "kind": "explicit-ordinals",
                "generator_ordinals": list(selected_ordinals),
            }
            if selected_ordinals is not None
            else {
                "kind": "full" if args.row_limit is None else "prefix",
                "first_generator_ordinal": 1,
                "last_generator_ordinal": len(translated),
            }
        ),
        "generator_count": len(all_polynomials),
        "original_variable_count": len(originals),
        "variable_count": len(safe_order),
        "original_variable_order": originals,
        "safe_variable_order": list(safe_order),
        "safe_variable_order_mode": args.order_mode,
        "variable_map": [
            {"original": original, "safe": mapping[original]} for original in originals
        ],
        "localization": {
            "open_polynomial_original": localization,
            "open_polynomial_safe": safe_localization,
            "method": "Rabinowitsch",
            "slack_variable": slack,
            "appended_generator": rabinowitsch,
        },
        "outer_parentheses_removed": outer_parentheses_removed,
        "output": {
            "path": str(output_path),
            "bytes": len(payload),
            "sha256": sha256_bytes(payload),
        },
        "emitter": {
            **versions,
            "function": "msolveio.emit_system",
            "python": platform.python_version(),
        },
        "certification_warning": (
            "msolve 0.6.5/0.10.1 characteristic-zero -g 2 [1] can be a "
            "first-prime result; it is not by itself an exact-Q unit certificate"
            if args.characteristic == 0
            else None
        ),
    }
    manifest_payload = (
        json.dumps(manifest, indent=2, sort_keys=True, ensure_ascii=True) + "\n"
    ).encode("utf-8")
    atomic_write(output_path, payload)
    atomic_write(manifest_path, manifest_payload)
    return {**manifest, "manifest_path": str(manifest_path)}


def parse_header_fields(lines: list[str], start: int) -> tuple[dict[str, str], int]:
    if start + 1 >= len(lines) or lines[start + 1].strip() != "#---":
        raise ChartError("malformed Groebner output: missing first #---")
    fields: dict[str, str] = {}
    position = start + 2
    while position < len(lines):
        line = lines[position].strip()
        if line == "#---":
            return fields, position + 1
        if not line.startswith("#"):
            raise ChartError(f"malformed Groebner header line: {line[:100]!r}")
        key, separator, value = line[1:].partition(":")
        if not separator:
            raise ChartError(f"malformed Groebner header field: {line[:100]!r}")
        fields[key.strip().lower()] = value.strip()
        position += 1
    raise ChartError("truncated Groebner output header")


def parse_reduced_gb(payload: str) -> dict[str, Any]:
    lines = payload.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    try:
        start = next(index for index, line in enumerate(lines) if line.strip())
    except StopIteration as exc:
        raise ChartError("empty msolve output") from exc
    if not lines[start].strip().startswith("#Reduced Groebner basis data"):
        raise ChartError(
            "status accepts only msolve -g 2 reduced-Groebner output; "
            f"first line is {lines[start].strip()!r}"
        )
    fields, body_start = parse_header_fields(lines, start)
    body = "\n".join(lines[body_start:]).strip()
    match = re.fullmatch(r"\[(.*)\]\s*:", body, flags=re.DOTALL)
    if match is None:
        raise ChartError("truncated or malformed reduced-Groebner basis body")
    inner = match.group(1).strip()
    if not inner:
        raise ChartError("empty reduced-Groebner list is not a valid unit/nonunit answer")
    basis = tuple(piece.strip() for piece in inner.split(","))
    if any(not piece for piece in basis):
        raise ChartError("empty entry in reduced-Groebner list")

    characteristic_text = fields.get("field characteristic")
    if characteristic_text is None or INTEGER.fullmatch(characteristic_text) is None:
        raise ChartError("Groebner header lacks an integer field characteristic")
    characteristic = int(characteristic_text)
    variable_text = fields.get("variable order")
    if variable_text is None:
        raise ChartError("Groebner header lacks variable order")
    variables = tuple(piece.strip() for piece in variable_text.split(","))
    if not variables or any(SAFE_IDENTIFIER.fullmatch(v) is None for v in variables):
        raise ChartError("invalid variable order in Groebner header")
    length_text = fields.get("length of basis", "")
    length_match = re.match(r"([0-9]+)\s+element", length_text)
    if length_match is None or int(length_match.group(1)) != len(basis):
        raise ChartError(
            f"basis length mismatch: header={length_text!r}, parsed={len(basis)}"
        )

    unit = basis == ("1",)
    if unit and characteristic == 0:
        status = "UNIT_SIGNAL_MODULAR_ONLY"
        certainty = "modular-only"
        warning = (
            "characteristic-zero [1] is not an exact-Q certificate in msolve "
            "0.6.5/0.10.1; confirm with a rational membership certificate"
        )
    elif unit:
        status = "UNIT"
        certainty = "proven-over-declared-prime-field"
        warning = None
    else:
        status = "NONUNIT"
        certainty = "declared-field-groebner-output"
        warning = None
    result: dict[str, Any] = {
        "status": status,
        "unit_ideal": unit,
        "certainty": certainty,
        "warning": warning,
        "characteristic": characteristic,
        "variables": list(variables),
        "basis_count": len(basis),
        "_basis_entries": list(basis),
        "monomial_order": fields.get("monomial order"),
    }
    return result


def parse_telemetry(stderr: str) -> dict[str, Any]:
    result: dict[str, Any] = {}
    patterns: tuple[tuple[str, str, Callable[[str], Any]], ...] = (
        ("invalid_equations", r"#invalid equations\s+([0-9]+)", int),
        ("primes_used", r"([0-9]+) primes used\.?", int),
        ("maximum_coefficient_bits", r"Maximum bit size of the coefficients:\s*([0-9]+)", int),
        ("elapsed_seconds", r"msolve overall time\s+([0-9.]+) sec \(elapsed\)", float),
        ("cpu_seconds", r"msolve overall time.*?/\s*([0-9.]+) sec \(cpu\)", float),
    )
    for key, pattern, converter in patterns:
        matches = re.findall(pattern, stderr)
        if matches:
            result[key] = converter(matches[-1])
    result["single_element_message"] = "Grobner basis has a single element" in stderr
    result["positive_dimensional_message"] = (
        "Positive dimensional Grobner basis" in stderr
        or "The ideal has positive dimension" in stderr
    )
    result["new_prime_messages"] = len(re.findall(r"\bNew prime\b", stderr))
    return result


def read_optional_rc(args: argparse.Namespace) -> int | None:
    if args.rc is not None:
        return args.rc
    if args.rc_file is None:
        return None
    path = Path(args.rc_file)
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8").strip()
    if INTEGER.fullmatch(text) is None:
        raise ChartError(f"rc file does not contain one integer: {path}")
    return int(text)


def status_result(args: argparse.Namespace) -> dict[str, Any]:
    output_path = Path(args.output).resolve()
    stderr_path = Path(args.stderr).resolve() if args.stderr else None
    rc = read_optional_rc(args)
    stderr = ""
    if stderr_path is not None and stderr_path.exists():
        stderr = stderr_path.read_text(encoding="utf-8", errors="replace")
    base: dict[str, Any] = {
        "schema": "moh14-msolve-status-v1",
        "returncode": rc,
        "output_path": str(output_path),
        "output_exists": output_path.is_file(),
        "telemetry": parse_telemetry(stderr),
    }
    if stderr_path is not None:
        base["stderr_path"] = str(stderr_path)
        if stderr_path.is_file():
            base["stderr_sha256"] = sha256_path(stderr_path)
    if rc is not None and rc != 0:
        if rc == 124:
            base.update(status="TIMEOUT", unit_ideal=None, certainty="none")
        elif rc >= 128:
            base.update(status="SIGNAL_OR_KILL", unit_ideal=None, certainty="none")
        else:
            base.update(status="ERROR", unit_ideal=None, certainty="none")
        return base
    if not output_path.is_file() or output_path.stat().st_size == 0:
        base.update(
            status="RUNNING_OR_NO_OUTPUT" if rc is None else "ERROR_NO_OUTPUT",
            unit_ideal=None,
            certainty="none",
        )
        return base

    payload = output_path.read_bytes()
    base["output_sha256"] = sha256_bytes(payload)
    base["output_bytes"] = len(payload)
    try:
        parsed = parse_reduced_gb(payload.decode("utf-8", errors="strict"))
    except (UnicodeError, ChartError) as exc:
        base.update(
            status="RUNNING_OR_INCOMPLETE" if rc is None else "ERROR_BAD_OUTPUT",
            unit_ideal=None,
            certainty="none",
            detail=str(exc),
        )
        return base
    basis_entries = parsed.pop("_basis_entries")
    base.update(parsed)

    # qqideal already owns the exact grevlex-leading-monomial and monomial
    # ideal dimension logic.  Keep it optional here because four fleet nodes
    # have msolve but not the Python packages; status is normally run on the
    # .7 conversion/audit host where both are installed.
    if not parsed["unit_ideal"]:
        try:
            from qqideal import Ring
            from qqideal.dimdeg import dim_and_degree

            ring = Ring(*parsed["variables"], characteristic=parsed["characteristic"])
            leading = [ring(entry).leading_monomial() for entry in basis_entries]
            dimension, degree = dim_and_degree(leading, len(parsed["variables"]))
        except Exception as exc:  # status stays NONUNIT; dimension is additive
            base["dimension_error"] = f"{type(exc).__name__}: {exc}"
        else:
            base["dimension"] = dimension
            base["degree"] = degree
            base["dimension_method"] = "qqideal.dimdeg from parsed grevlex leading monomials"

    if args.manifest:
        manifest_path = Path(args.manifest).resolve()
        manifest = load_json_object(manifest_path, "input manifest")
        base["input_manifest"] = file_record(manifest_path)
        expected_characteristic = manifest.get("characteristic")
        expected_variables = manifest.get("safe_variable_order")
        mismatches = []
        if parsed["characteristic"] != expected_characteristic:
            mismatches.append(
                f"characteristic output={parsed['characteristic']} manifest={expected_characteristic}"
            )
        if parsed["variables"] != expected_variables:
            mismatches.append("variable order differs from input manifest")
        if mismatches:
            base.update(
                status="ERROR_CUSTODY_MISMATCH",
                unit_ideal=None,
                certainty="none",
                detail="; ".join(mismatches),
            )
    return base


def write_json_result(result: dict[str, Any], destination: str | None) -> None:
    payload = (
        json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n"
    ).encode("utf-8")
    if destination:
        atomic_write(Path(destination).resolve(), payload)
    sys.stdout.buffer.write(payload)


def emit_controls(args: argparse.Namespace) -> dict[str, Any]:
    emit_system, versions = import_emitter()
    directory = Path(args.directory).resolve()
    directory.mkdir(parents=True, exist_ok=True)
    systems = {
        "known_unit": {
            # Banked campaign kill: D=108, delta=3, stage-0 common-h3.
            # Source Singular names its slack Zc; z is the equivalent safe
            # name used by this converter.
            "variables": ("jet1", "jet2", "c", "z"),
            "polynomials": (
                "-jet2^2",
                "2*jet1^2*jet2",
                "-2*jet2",
                "-c-jet1^4+9*jet1*jet2^2",
                "2*jet1^2",
                "z*c-1",
            ),
            "expected": "UNIT",
            "provenance": (
                "box/sysguidedgb-20260903/runs/T2_g108_unit/"
                "T2_g108_delta3_stage0_common_h3_Q.sing"
            ),
        },
        "tame_live": {
            "variables": ("p", "q", "x", "y", "c", "z"),
            "polynomials": ("p-x-y^2", "q-y", "c-1", "z*c-1"),
            "expected": "NONUNIT",
            "provenance": "synthetic tame triangular automorphism family",
        },
    }
    records: dict[str, Any] = {}
    for name, specification in systems.items():
        try:
            rendered = emit_system(
                specification["polynomials"],
                variables=specification["variables"],
                characteristic=args.characteristic,
            )
        except Exception as exc:
            raise ChartError(f"msolveio.emit_system refused control {name}: {exc}") from exc
        path = directory / f"{name}_p{args.characteristic}.ms"
        payload = rendered.encode("utf-8")
        atomic_write(path, payload)
        records[name] = {
            "path": str(path),
            "sha256": sha256_bytes(payload),
            "bytes": len(payload),
            "expected_g2_status": specification["expected"],
            "variables": list(specification["variables"]),
            "generator_count": len(specification["polynomials"]),
            "provenance": specification["provenance"],
        }
    manifest = {
        "schema": "moh14-msolve-controls-v1",
        "characteristic": args.characteristic,
        "emitter": {**versions, "function": "msolveio.emit_system"},
        "systems": records,
    }
    manifest_path = directory / f"controls_p{args.characteristic}.json"
    atomic_write(
        manifest_path,
        (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode("utf-8"),
    )
    return {**manifest, "manifest_path": str(manifest_path)}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    emit = subparsers.add_parser("emit", help="convert one meta+rows chart to .ms")
    emit.add_argument("--root", default=str(BASE), help="moh14 chart bundle root")
    emit.add_argument("--class-id")
    emit.add_argument("--stem", help="full stem or suffix such as union")
    emit.add_argument("--meta", help="explicit metadata JSON (alternative locator)")
    emit.add_argument("--rows", help="explicit rows file override")
    emit.add_argument(
        "--builder",
        help="explicit builder provenance override, used with alternate row files",
    )
    emit.add_argument("--characteristic", type=int, default=0)
    emit.add_argument(
        "--source-characteristic",
        type=int,
        default=0,
        help="field characteristic in which the source rows were generated",
    )
    emit.add_argument(
        "--order-mode",
        choices=("source", "reverse-source"),
        default="source",
        help="msolve variable declaration order; z remains last",
    )
    emit.add_argument(
        "--row-limit",
        type=int,
        help=(
            "emit only the first N source generators, plus Rabinowitsch; "
            "a unit certificate for this subset also certifies the full ideal"
        ),
    )
    emit.add_argument(
        "--row-indices",
        help=(
            "emit selected 1-based source-generator ordinals/ranges, e.g. "
            "1,7,20-40; mutually exclusive with --row-limit"
        ),
    )
    emit.add_argument("--output", required=True, help="destination .ms file")
    emit.add_argument("--manifest", help="destination JSON; defaults to OUTPUT.json")
    emit.add_argument("--json-output", help="also write command result JSON here")

    status = subparsers.add_parser("status", help="classify msolve -g 2 output")
    status.add_argument("--output", required=True, help="msolve -o file")
    status.add_argument("--stderr", help="captured msolve stderr/telemetry")
    status.add_argument("--rc", type=int, help="known process return code")
    status.add_argument("--rc-file", help="file containing process return code")
    status.add_argument("--manifest", help="input manifest for ring/order custody check")
    status.add_argument("--json-output", help="write status JSON here")

    controls = subparsers.add_parser("controls", help="emit tiny unit/live controls")
    controls.add_argument("--directory", required=True)
    controls.add_argument("--characteristic", type=int, default=32003)
    controls.add_argument("--json-output", help="also write command result JSON here")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "emit":
            result = emit_chart(args)
        elif args.command == "status":
            result = status_result(args)
        elif args.command == "controls":
            result = emit_controls(args)
        else:  # pragma: no cover - argparse enforces choices
            parser.error(f"unknown command {args.command}")
            return 2
    except ChartError as exc:
        print(f"REFUSED: {exc}", file=sys.stderr)
        return 2
    write_json_result(result, args.json_output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
