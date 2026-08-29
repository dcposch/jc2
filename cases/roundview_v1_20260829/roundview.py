#!/usr/bin/env python3
"""Compile a compact, exact-slice view of canonical APPROACHES.md.

ROUNDVIEW/v1 is deliberately non-authoritative.  It extracts source bytes;
it never interprets, updates, or replaces the canonical campaign ledger.
"""

import argparse
import datetime as _datetime
import hashlib
import os
from pathlib import Path
import re
import sys
import tempfile
from dataclasses import dataclass
from typing import List, Optional, Sequence, Tuple


SCHEMA = "ROUNDVIEW/v1"
MASTER_HEADING = "## 1. Master union table"
TABLE_HEADER = (
    "| # | Approach | Essence | Sources | Tried? | Stuck where | "
    "Promise (reconciled) |"
)
TABLE_DIVIDER = "|--:|---|---|---|---|---|---|"
LATEST_OVERLAY_PREFIX = "## Superseding strategy overlay ("
LATEST_TIMESTAMP_RE = re.compile(
    r"^## Superseding strategy overlay "
    r"\((\d{4}-\d{2}-\d{2} \d{2}:\d{2}Z)(?:\s|\))"
)
AVENUE_RE = re.compile(r"^\|\s*([0-9]+)\s*\|")
BODY_BYTES_PREFIX = b"<!-- ROUNDVIEW_BODY_BYTES: "
BODY_SHA_PREFIX = b"<!-- ROUNDVIEW_BODY_SHA256: "
MAX_OUTPUT_PERCENT = 15


class RoundviewError(RuntimeError):
    """A fail-closed custody, grammar, or output-integrity error."""


@dataclass(frozen=True)
class Slice:
    name: str
    start: int  # zero-based, inclusive line index
    end: int  # zero-based, exclusive line index
    data: bytes

    @property
    def line_range(self) -> str:
        return "{}-{}".format(self.start + 1, self.end)

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.data).hexdigest()


@dataclass(frozen=True)
class ParsedSource:
    source: bytes
    source_sha256: str
    line_count: int
    preamble: Slice
    newest_overlay: Slice
    master_table: Slice
    older_overlays: Tuple[Slice, ...]
    overlay_headings: Tuple[str, ...]


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _fingerprint(stat_result: os.stat_result) -> Tuple[int, ...]:
    return (
        stat_result.st_dev,
        stat_result.st_ino,
        stat_result.st_mode,
        stat_result.st_size,
        stat_result.st_mtime_ns,
        stat_result.st_ctime_ns,
    )


def read_stable_file(path: Path) -> bytes:
    """Read twice from one descriptor and reject path or descriptor mutation."""

    try:
        path_before = path.stat()
        with path.open("rb") as handle:
            fd_before = os.fstat(handle.fileno())
            first = handle.read()
            fd_middle = os.fstat(handle.fileno())
            handle.seek(0)
            second = handle.read()
            fd_after = os.fstat(handle.fileno())
        path_after = path.stat()
    except OSError as exc:
        raise RoundviewError("cannot stably read {}: {}".format(path, exc))

    fingerprints = (
        _fingerprint(path_before),
        _fingerprint(fd_before),
        _fingerprint(fd_middle),
        _fingerprint(fd_after),
        _fingerprint(path_after),
    )
    if len(set(fingerprints)) != 1 or first != second:
        raise RoundviewError("source mutation detected during read: {}".format(path))
    return first


def _line_text(raw: bytes, line_number: int) -> str:
    try:
        return raw.rstrip(b"\r\n").decode("utf-8")
    except UnicodeDecodeError as exc:
        raise RoundviewError(
            "source is not UTF-8 at line {}: {}".format(line_number, exc)
        )


def _is_level2_heading(text: str) -> bool:
    return text.startswith("## ")


def _is_overlay_heading(text: str) -> bool:
    if not _is_level2_heading(text):
        return False
    # Ignore prose headings that merely mention an overlay in parentheses.
    title = text.split(" (", 1)[0].casefold()
    return title.endswith(" overlay")


def _next_level2(level2: Sequence[int], start: int, line_count: int) -> int:
    for index in level2:
        if index > start:
            return index
    return line_count


def _make_slice(name: str, lines: Sequence[bytes], start: int, end: int) -> Slice:
    if not (0 <= start < end <= len(lines)):
        raise RoundviewError(
            "invalid {} line range {}:{} for {} lines".format(
                name, start, end, len(lines)
            )
        )
    return Slice(name=name, start=start, end=end, data=b"".join(lines[start:end]))


def parse_source(source: bytes) -> ParsedSource:
    if not source:
        raise RoundviewError("empty source")
    lines = source.splitlines(keepends=True)
    texts = tuple(_line_text(raw, i + 1) for i, raw in enumerate(lines))

    if not texts[0].startswith("# APPROACHES.md"):
        raise RoundviewError("missing canonical APPROACHES.md title at line 1")

    level2 = tuple(i for i, text in enumerate(texts) if _is_level2_heading(text))
    if not level2:
        raise RoundviewError("missing level-two section anchors")

    overlay_indices = tuple(
        i for i, text in enumerate(texts) if _is_overlay_heading(text)
    )
    if not overlay_indices:
        raise RoundviewError("missing overlay anchor")
    overlay_headings = tuple(texts[i] for i in overlay_indices)
    if len(set(overlay_headings)) != len(overlay_headings):
        duplicates = sorted(
            heading
            for heading in set(overlay_headings)
            if overlay_headings.count(heading) > 1
        )
        raise RoundviewError(
            "duplicate overlay heading anchor(s): {}".format("; ".join(duplicates))
        )

    strategy_indices = tuple(
        i for i in overlay_indices if texts[i].startswith(LATEST_OVERLAY_PREFIX)
    )
    if not strategy_indices:
        raise RoundviewError("missing superseding strategy overlay anchor")
    newest_index = strategy_indices[0]
    if level2[0] != newest_index:
        raise RoundviewError(
            "newest superseding strategy overlay is not the first level-two section"
        )

    timestamped: List[Tuple[_datetime.datetime, int]] = []
    for index in strategy_indices:
        match = LATEST_TIMESTAMP_RE.match(texts[index])
        if match is None:
            raise RoundviewError(
                "unparseable superseding strategy overlay timestamp at line {}".format(
                    index + 1
                )
            )
        timestamp = _datetime.datetime.strptime(match.group(1), "%Y-%m-%d %H:%MZ")
        timestamped.append((timestamp, index))
    if timestamped[0][0] != max(item[0] for item in timestamped):
        raise RoundviewError("first superseding strategy overlay is not newest")
    if any(left[0] < right[0] for left, right in zip(timestamped, timestamped[1:])):
        raise RoundviewError("superseding strategy overlays are not reverse chronological")

    master_indices = tuple(i for i, text in enumerate(texts) if text == MASTER_HEADING)
    if len(master_indices) != 1:
        raise RoundviewError(
            "master union table anchor count is {}, expected 1".format(
                len(master_indices)
            )
        )
    master_index = master_indices[0]
    if master_index <= newest_index:
        raise RoundviewError("master union table precedes newest strategy overlay")
    master_end = _next_level2(level2, master_index, len(lines))

    header_indices = tuple(i for i, text in enumerate(texts) if text == TABLE_HEADER)
    divider_indices = tuple(i for i, text in enumerate(texts) if text == TABLE_DIVIDER)
    if len(header_indices) != 1:
        raise RoundviewError(
            "canonical table header count is {}, expected 1".format(
                len(header_indices)
            )
        )
    if len(divider_indices) != 1:
        raise RoundviewError(
            "canonical table divider count is {}, expected 1".format(
                len(divider_indices)
            )
        )
    header_index = header_indices[0]
    divider_index = divider_indices[0]
    if not (master_index < header_index < master_end):
        raise RoundviewError("canonical table header is outside master union section")
    if divider_index != header_index + 1:
        raise RoundviewError("canonical table divider is not directly after its header")

    numbered_rows: List[Tuple[int, int]] = []
    for index in range(divider_index + 1, master_end):
        match = AVENUE_RE.match(texts[index])
        if match is not None:
            numbered_rows.append((int(match.group(1)), index))
    numbers = [number for number, _ in numbered_rows]
    expected = list(range(1, 47))
    if numbers != expected:
        duplicates = sorted({number for number in numbers if numbers.count(number) > 1})
        missing = sorted(set(expected) - set(numbers))
        extras = sorted(set(numbers) - set(expected))
        raise RoundviewError(
            "avenue rows must be exactly 1..46 in order; duplicates={}, missing={}, "
            "extras={}, observed={}".format(duplicates, missing, extras, numbers)
        )

    preamble = _make_slice("preamble", lines, 0, newest_index)
    newest_end = _next_level2(level2, newest_index, len(lines))
    newest_overlay = _make_slice(
        "newest_overlay", lines, newest_index, newest_end
    )
    master_table = _make_slice("master_table", lines, master_index, master_end)

    older_slices: List[Slice] = []
    older_headings: List[str] = []
    for sequence_number, index in enumerate(overlay_indices[1:], start=1):
        end = _next_level2(level2, index, len(lines))
        older_slices.append(
            _make_slice("older_overlay_{:03d}".format(sequence_number), lines, index, end)
        )
        older_headings.append(texts[index])

    full_hashes = [item.sha256 for item in older_slices]
    if len(set(full_hashes)) != len(full_hashes):
        raise RoundviewError("duplicate older-overlay section SHA-256")

    return ParsedSource(
        source=source,
        source_sha256=sha256(source),
        line_count=len(lines),
        preamble=preamble,
        newest_overlay=newest_overlay,
        master_table=master_table,
        older_overlays=tuple(older_slices),
        overlay_headings=tuple(older_headings),
    )


def _ascii_metadata(parsed: ParsedSource, source_label: str) -> bytes:
    if "\n" in source_label or "\r" in source_label:
        raise RoundviewError("source label contains a newline")
    fields = (
        ("schema", SCHEMA),
        ("status", "GENERATED_NON_AUTHORITATIVE"),
        ("queue_policy", "NO_SECOND_QUEUE"),
        ("source_label", source_label),
        ("source_sha256", parsed.source_sha256),
        ("source_bytes", str(len(parsed.source))),
        ("source_lines", str(parsed.line_count)),
        ("preamble_lines", parsed.preamble.line_range),
        ("preamble_sha256", parsed.preamble.sha256),
        ("newest_overlay_lines", parsed.newest_overlay.line_range),
        ("newest_overlay_sha256", parsed.newest_overlay.sha256),
        ("master_table_lines", parsed.master_table.line_range),
        ("master_table_sha256", parsed.master_table.sha256),
        ("avenue_rows", "46"),
        ("older_overlay_count", str(len(parsed.older_overlays))),
        ("older_overlay_hash", "full-section SHA-256"),
    )
    return "".join("{}: {}\n".format(key, value) for key, value in fields).encode(
        "utf-8"
    )


def render(parsed: ParsedSource, source_label: str) -> bytes:
    chunks: List[bytes] = [
        b"# ROUNDVIEW/v1 exact-slice round input\n\n",
        b"GENERATED_NON_AUTHORITATIVE. This file is a reproducible view of "
        b"canonical source bytes, never a campaign authority.\n\n",
        b"NO_SECOND_QUEUE. Do not use this view as a task ledger, promotion "
        b"ledger, or substitute for canonical files.\n\n",
        b"## Custody manifest\n\n",
        b"```text\n",
        _ascii_metadata(parsed, source_label),
        b"```\n\n",
    ]

    exact_slices = (
        ("preamble", parsed.preamble),
        ("newest superseding strategy overlay", parsed.newest_overlay),
        ("canonical 46-row master union table", parsed.master_table),
    )
    for display_name, item in exact_slices:
        chunks.extend(
            (
                "## Exact source slice: {}\n\n".format(display_name).encode("utf-8"),
                (
                    "<!-- ROUNDVIEW_EXACT_SLICE_BEGIN name={} lines={} sha256={} -->\n".format(
                        item.name, item.line_range, item.sha256
                    )
                ).encode("utf-8"),
                item.data,
            )
        )
        if item.data and not item.data.endswith((b"\n", b"\r")):
            chunks.append(b"\n")
        chunks.extend(
            (
                "<!-- ROUNDVIEW_EXACT_SLICE_END name={} -->\n\n".format(
                    item.name
                ).encode("utf-8"),
            )
        )

    chunks.extend(
        (
            b"## Compact index of older overlay sections\n\n",
            b"Each line gives the exact source line range and the full SHA-256 "
            b"of that complete overlay section (heading through the byte before "
            b"the next level-two heading).\n\n",
            b"```text\n",
        )
    )
    for item, heading in zip(parsed.older_overlays, parsed.overlay_headings):
        chunks.append(
            "L{} sha256={} {}\n".format(
                item.line_range, item.sha256, heading
            ).encode("utf-8")
        )
    chunks.append(b"```\n")

    body = b"".join(chunks)
    footer = (
        BODY_BYTES_PREFIX
        + str(len(body)).encode("ascii")
        + b" -->\n"
        + BODY_SHA_PREFIX
        + sha256(body).encode("ascii")
        + b" -->\n"
    )
    output = body + footer
    if len(output) * 100 >= len(parsed.source) * MAX_OUTPUT_PERCENT:
        raise RoundviewError(
            "compiled output is not below {}% of source: {} / {} bytes".format(
                MAX_OUTPUT_PERCENT, len(output), len(parsed.source)
            )
        )
    return output


def verify_output_seal(output: bytes) -> None:
    marker = BODY_BYTES_PREFIX
    position = output.rfind(marker)
    if position < 0:
        raise RoundviewError("missing ROUNDVIEW body seal")
    body = output[:position]
    footer = output[position:]
    match = re.fullmatch(
        rb"<!-- ROUNDVIEW_BODY_BYTES: ([0-9]+) -->\n"
        rb"<!-- ROUNDVIEW_BODY_SHA256: ([0-9a-f]{64}) -->\n",
        footer,
    )
    if match is None:
        raise RoundviewError("malformed ROUNDVIEW body seal")
    declared_bytes = int(match.group(1))
    declared_sha = match.group(2).decode("ascii")
    if declared_bytes != len(body):
        raise RoundviewError(
            "ROUNDVIEW body byte drift: declared {}, observed {}".format(
                declared_bytes, len(body)
            )
        )
    observed_sha = sha256(body)
    if declared_sha != observed_sha:
        raise RoundviewError(
            "ROUNDVIEW body hash drift: declared {}, observed {}".format(
                declared_sha, observed_sha
            )
        )


def compile_source(
    source_path: Path,
    source_label: str,
    expected_source_sha256: Optional[str] = None,
) -> bytes:
    source = read_stable_file(source_path)
    observed = sha256(source)
    if expected_source_sha256 is not None and observed != expected_source_sha256:
        raise RoundviewError(
            "source SHA-256 mismatch: expected {}, observed {}".format(
                expected_source_sha256, observed
            )
        )
    output = render(parse_source(source), source_label)
    verify_output_seal(output)
    return output


def _atomic_write(path: Path, data: bytes) -> None:
    parent = path.parent
    if not parent.exists() or not parent.is_dir():
        raise RoundviewError("output parent is not a directory: {}".format(parent))
    if path.is_symlink():
        raise RoundviewError("refusing symlink output path: {}".format(path))
    temporary: Optional[Path] = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb", prefix=".roundview-", suffix=".tmp", dir=str(parent), delete=False
        ) as handle:
            temporary = Path(handle.name)
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(str(temporary), str(path))
        temporary = None
    except OSError as exc:
        raise RoundviewError("cannot write {}: {}".format(path, exc))
    finally:
        if temporary is not None:
            try:
                temporary.unlink()
            except OSError:
                pass


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument(
        "--source-label",
        help="stable label embedded in output (default: --source spelling)",
    )
    parser.add_argument("--expect-source-sha256")
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--stdout", action="store_true")
    action.add_argument("--output", type=Path)
    action.add_argument(
        "--check",
        type=Path,
        metavar="EXISTING_OUTPUT",
        help="fail unless existing output is byte-identical to a fresh compile",
    )
    action.add_argument(
        "--verify-output",
        type=Path,
        metavar="OUTPUT",
        help="verify a stored output's internal body seal only",
    )
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = _parser().parse_args(argv)
    try:
        if args.verify_output is not None:
            verify_output_seal(read_stable_file(args.verify_output))
            return 0

        source_label = args.source_label or str(args.source)
        compiled = compile_source(
            args.source, source_label, args.expect_source_sha256
        )
        if args.stdout:
            sys.stdout.buffer.write(compiled)
            return 0
        if args.output is not None:
            _atomic_write(args.output, compiled)
            sys.stderr.write(
                "ROUNDVIEW/v1 wrote {} bytes sha256={} to {}\n".format(
                    len(compiled), sha256(compiled), args.output
                )
            )
            return 0

        existing = read_stable_file(args.check)
        verify_output_seal(existing)
        if existing != compiled:
            raise RoundviewError(
                "output hash drift for {}: expected {}, observed {}".format(
                    args.check, sha256(compiled), sha256(existing)
                )
            )
        return 0
    except RoundviewError as exc:
        sys.stderr.write("ROUNDVIEW/v1 FAIL_CLOSED: {}\n".format(exc))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
