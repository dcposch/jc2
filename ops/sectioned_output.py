#!/usr/bin/env python3
"""Validate and assemble independently generated, size-bounded report sections.

This is deliberately not a model runner and is not wired into ``ops/lane.sh``.
An operator may split a long task into independent calls that each write one
section file.  The manifest pre-registers their order, declared (unverified)
prompt hashes, and total-file byte budgets.  This tool reports the last
complete section after an interrupted run and assembles the final BODY-END
report only when every section validates and remains stable across assembly.

Exit status 0 means complete/assembled, 4 means a valid contiguous prefix is
incomplete, and 2 means the contract failed.  ``max_bytes`` includes the body,
the SECTION-END marker, and its terminating newline.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import sys
from typing import Any


SCHEMA = 1
BODY_END = b"<!-- BODY-END -->\n"
ID_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,63}\Z")
TAG_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}\Z")
SHA_RE = re.compile(r"[0-9a-f]{64}\Z")
BASIS_RE = re.compile(r"[0-9a-f]{40}\Z")


class ContractError(RuntimeError):
    """The manifest or a section violates the fail-closed contract."""


@dataclass(frozen=True)
class SectionSpec:
    section_id: str
    path_text: str
    path: Path
    prompt_sha256_declared: str
    max_bytes: int


@dataclass(frozen=True)
class Manifest:
    raw: bytes
    sha256: str
    tag: str
    basis: str
    output_text: str
    output: Path
    sections: tuple[SectionSpec, ...]


@dataclass(frozen=True)
class CheckedSection:
    spec: SectionSpec
    raw: bytes
    body: bytes
    sha256: str


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _identity(info: os.stat_result) -> tuple[int, int]:
    return info.st_dev, info.st_ino


def _snapshot(info: os.stat_result) -> tuple[int, int, int, int, int, int]:
    return (
        info.st_dev,
        info.st_ino,
        stat.S_IMODE(info.st_mode),
        info.st_size,
        info.st_mtime_ns,
        info.st_ctime_ns,
    )


def regular_file(path: Path, label: str) -> bytes:
    """Read one stable regular file without following its final symlink."""

    try:
        before = path.lstat()
        if stat.S_ISLNK(before.st_mode) or not stat.S_ISREG(before.st_mode):
            raise ContractError(
                f"{label} must be a regular non-symlink file: {path}"
            )
        flags = os.O_RDONLY | getattr(os, "O_NONBLOCK", 0)
        if hasattr(os, "O_NOFOLLOW"):
            flags |= os.O_NOFOLLOW
        fd = os.open(path, flags)
    except OSError as exc:
        raise ContractError(f"cannot open {label}: {path}: {exc}") from exc

    try:
        opened = os.fstat(fd)
        if not stat.S_ISREG(opened.st_mode) or _identity(opened) != _identity(before):
            raise ContractError(f"{label} identity changed during open: {path}")
        chunks: list[bytes] = []
        while True:
            chunk = os.read(fd, 1024 * 1024)
            if not chunk:
                break
            chunks.append(chunk)
        data = b"".join(chunks)
        after_fd = os.fstat(fd)
        if _snapshot(after_fd) != _snapshot(opened) or len(data) != after_fd.st_size:
            raise ContractError(f"{label} changed while being read: {path}")
        try:
            after_path = path.lstat()
        except OSError as exc:
            raise ContractError(f"cannot recheck {label}: {path}: {exc}") from exc
        if (
            stat.S_ISLNK(after_path.st_mode)
            or not stat.S_ISREG(after_path.st_mode)
            or _identity(after_path) != _identity(opened)
        ):
            raise ContractError(f"{label} identity changed after read: {path}")
        return data
    except OSError as exc:
        raise ContractError(f"cannot read {label}: {path}: {exc}") from exc
    finally:
        os.close(fd)


def path_present(path: Path, label: str) -> bool:
    """Distinguish a genuinely absent path from every other lstat failure."""

    try:
        path.lstat()
    except FileNotFoundError:
        return False
    except OSError as exc:
        raise ContractError(f"cannot inspect {label}: {path}: {exc}") from exc
    return True


def safe_relative(root: Path, text: Any, label: str) -> Path:
    if not isinstance(text, str) or not text:
        raise ContractError(f"{label} must be a nonempty relative path")
    if any(ord(char) < 32 or 0x7F <= ord(char) <= 0x9F for char in text):
        raise ContractError(f"{label} contains a control character")
    rel = Path(text)
    if rel.is_absolute() or any(part in ("", ".", "..") for part in rel.parts):
        raise ContractError(f"{label} must be a normalized relative path: {text!r}")
    try:
        root_real = root.resolve(strict=True)
    except OSError as exc:
        raise ContractError(f"cannot resolve contract root: {root}: {exc}") from exc
    candidate = root / rel

    # Existing parents may not redirect traversal through symlinks.
    cursor = root
    for part in rel.parts[:-1]:
        cursor = cursor / part
        try:
            info = cursor.lstat()
        except FileNotFoundError:
            continue
        except OSError as exc:
            raise ContractError(f"cannot inspect parent for {label}: {cursor}: {exc}") from exc
        else:
            mode = info.st_mode
            if stat.S_ISLNK(mode) or not stat.S_ISDIR(mode):
                raise ContractError(f"unsafe parent for {label}: {cursor}")
    try:
        parent_real = candidate.parent.resolve(strict=True)
    except OSError as exc:
        raise ContractError(f"parent for {label} does not exist: {candidate.parent}") from exc
    if parent_real != root_real and root_real not in parent_real.parents:
        raise ContractError(f"{label} escapes root: {text!r}")
    return candidate


def exact_keys(obj: dict[str, Any], expected: set[str], label: str) -> None:
    actual = set(obj)
    if actual != expected:
        missing = sorted(expected - actual)
        extra = sorted(actual - expected)
        raise ContractError(f"{label} keys mismatch: missing={missing} extra={extra}")


def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ContractError(f"manifest JSON contains duplicate key: {key!r}")
        result[key] = value
    return result


def load_manifest(root: Path, manifest_text: str) -> Manifest:
    manifest_path = safe_relative(root, manifest_text, "manifest")
    raw = regular_file(manifest_path, "manifest")
    try:
        parsed = json.loads(raw.decode("utf-8"), object_pairs_hook=unique_object)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ContractError(f"manifest is not valid UTF-8 JSON: {exc}") from exc
    if not isinstance(parsed, dict):
        raise ContractError("manifest root must be an object")
    exact_keys(parsed, {"schema", "tag", "basis", "output", "sections"}, "manifest")
    if parsed["schema"] != SCHEMA:
        raise ContractError(f"unsupported schema: {parsed['schema']!r}")
    tag = parsed["tag"]
    basis = parsed["basis"]
    if not isinstance(tag, str) or TAG_RE.fullmatch(tag) is None:
        raise ContractError(f"invalid tag: {tag!r}")
    if not isinstance(basis, str) or BASIS_RE.fullmatch(basis) is None:
        raise ContractError(f"basis must be a lowercase 40-hex commit: {basis!r}")
    output_text = parsed["output"]
    output = safe_relative(root, output_text, "output")
    rows = parsed["sections"]
    if not isinstance(rows, list) or not (1 <= len(rows) <= 16):
        raise ContractError("sections must be a list of 1..16 entries")

    specs: list[SectionSpec] = []
    ids: set[str] = set()
    paths: set[str] = set()
    for index, row in enumerate(rows, start=1):
        if not isinstance(row, dict):
            raise ContractError(f"section {index} must be an object")
        exact_keys(
            row,
            {"id", "path", "prompt_sha256_declared", "max_bytes"},
            f"section {index}",
        )
        section_id = row["id"]
        path_text = row["path"]
        prompt_sha256_declared = row["prompt_sha256_declared"]
        max_bytes = row["max_bytes"]
        if not isinstance(section_id, str) or ID_RE.fullmatch(section_id) is None:
            raise ContractError(f"invalid section id at position {index}: {section_id!r}")
        if section_id in ids:
            raise ContractError(f"duplicate section id: {section_id}")
        if (
            not isinstance(prompt_sha256_declared, str)
            or SHA_RE.fullmatch(prompt_sha256_declared) is None
        ):
            raise ContractError(
                f"invalid declared prompt SHA-256 for section {section_id}"
            )
        if (
            isinstance(max_bytes, bool)
            or not isinstance(max_bytes, int)
            or not (1 <= max_bytes <= 1_000_000)
        ):
            raise ContractError(f"max_bytes for section {section_id} must be 1..1000000")
        path = safe_relative(root, path_text, f"section {section_id}")
        normalized = path.as_posix()
        if normalized in paths:
            raise ContractError(f"duplicate section path: {path_text}")
        ids.add(section_id)
        paths.add(normalized)
        specs.append(
            SectionSpec(
                section_id,
                path_text,
                path,
                prompt_sha256_declared,
                max_bytes,
            )
        )

    if output.as_posix() in paths:
        raise ContractError("output path may not equal a section path")
    return Manifest(raw, digest(raw), tag, basis, output_text, output, tuple(specs))


def check_section(spec: SectionSpec) -> CheckedSection:
    raw = regular_file(spec.path, f"section {spec.section_id}")
    if len(raw) > spec.max_bytes:
        raise ContractError(
            f"section {spec.section_id} exceeds max_bytes: {len(raw)}>{spec.max_bytes}"
        )
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ContractError(f"section {spec.section_id} is not UTF-8") from exc
    expected = f"<!-- SECTION-END {spec.section_id} -->"
    standalone = [
        line for line in text.splitlines() if line.startswith("<!-- SECTION-END ")
    ]
    if standalone != [expected] or not raw.endswith((expected + "\n").encode("utf-8")):
        raise ContractError(
            f"section {spec.section_id} must end in one exact standalone marker"
        )
    body = raw[: -len((expected + "\n").encode("utf-8"))]
    if not body.strip():
        raise ContractError(f"section {spec.section_id} body is empty")
    reserved = (b"BODY-END", b"SECTION-END", b"<!-- SECTION ")
    if any(token in body for token in reserved):
        raise ContractError(
            f"section {spec.section_id} body contains reserved marker vocabulary"
        )
    return CheckedSection(spec, raw, body, digest(raw))


def inspect(manifest: Manifest) -> tuple[dict[str, Any], tuple[CheckedSection, ...], int]:
    checked: list[CheckedSection] = []
    first_missing: int | None = None
    for index, spec in enumerate(manifest.sections):
        if not path_present(spec.path, f"section {spec.section_id}"):
            if first_missing is None:
                first_missing = index
            continue
        if first_missing is not None:
            raise ContractError(
                f"noncontiguous sections: {spec.section_id} exists after missing "
                f"{manifest.sections[first_missing].section_id}"
            )
        checked.append(check_section(spec))

    common: dict[str, Any] = {
        "schema": SCHEMA,
        "tag": manifest.tag,
        "basis": manifest.basis,
        "manifest_sha256": manifest.sha256,
        "completed": [
            {
                "id": item.spec.section_id,
                "bytes": len(item.raw),
                "sha256": item.sha256,
                "prompt_sha256_declared": item.spec.prompt_sha256_declared,
            }
            for item in checked
        ],
    }
    if first_missing is None:
        common["status"] = "COMPLETE"
        common["next_section"] = None
        return common, tuple(checked), 0
    missing = manifest.sections[first_missing]
    common["next_section"] = missing.section_id
    common["status"] = (
        "MISSING_BEFORE_FIRST_SECTION"
        if not checked
        else f"TRUNCATED_AFTER_SECTION_{checked[-1].spec.section_id}"
    )
    return common, tuple(checked), 4


def assembled_bytes(manifest: Manifest, checked: tuple[CheckedSection, ...]) -> bytes:
    lines = [
        f"# Sectioned report assembly — `{manifest.tag}`\n",
        "\n",
        f"Frozen basis: `{manifest.basis}`  \n",
        f"Section manifest SHA-256: `{manifest.sha256}`\n",
        "\n",
    ]
    prefix = "".join(lines).encode("utf-8")
    pieces = [prefix]
    for item in checked:
        provenance = (
            f"<!-- SECTION {item.spec.section_id} sha256={item.sha256} -->\n"
        )
        pieces.append(provenance.encode("utf-8"))
        pieces.append(item.body)
        if not item.body.endswith(b"\n"):
            pieces.append(b"\n")
        pieces.append(b"\n")
    pieces.append(BODY_END)
    return b"".join(pieces)


def write_exclusive(path: Path, data: bytes) -> None:
    try:
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
    except OSError as exc:
        if isinstance(exc, FileExistsError):
            message = f"output already exists; refusing overwrite: {path}"
        else:
            message = f"cannot create output exclusively: {path}: {exc}"
        raise ContractError(message) from exc
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
    except BaseException as exc:
        try:
            path.unlink()
        except OSError as cleanup_exc:
            raise ContractError(
                f"cannot write output and quarantine failed: {path}: "
                f"write={exc}; cleanup={cleanup_exc}"
            ) from cleanup_exc
        if isinstance(exc, ContractError):
            raise
        raise ContractError(f"cannot write output: {path}: {exc}") from exc


def emit(record: dict[str, Any]) -> None:
    print(json.dumps(record, sort_keys=True, separators=(",", ":")))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("status", "assemble"))
    parser.add_argument("manifest", help="manifest path relative to --root")
    parser.add_argument("--root", default=".", help="contract root (default: cwd)")
    args = parser.parse_args(argv)
    try:
        root = Path(args.root)
        if not root.is_dir() or root.is_symlink():
            raise ContractError(f"root must be a real directory: {root}")
        manifest = load_manifest(root, args.manifest)
        record, checked, status = inspect(manifest)
        if args.command == "status":
            emit(record)
            return status
        if status != 0:
            emit(record)
            return status
        before = tuple(item.sha256 for item in checked)
        payload = assembled_bytes(manifest, checked)
        write_exclusive(manifest.output, payload)
        # Any input change during assembly quarantines the new output.  This
        # includes a section becoming malformed rather than merely changing
        # to another valid body.
        try:
            after_manifest = regular_file(
                safe_relative(root, args.manifest, "manifest"), "manifest"
            )
            after = tuple(check_section(item.spec).sha256 for item in checked)
            if digest(after_manifest) != manifest.sha256 or after != before:
                raise ContractError("input changed during assembly")
        except (ContractError, OSError) as exc:
            try:
                manifest.output.unlink(missing_ok=True)
            except OSError as cleanup_exc:
                raise ContractError(
                    f"{exc}; output quarantine failed: {cleanup_exc}"
                ) from cleanup_exc
            raise ContractError(f"{exc}; output removed") from exc
        record["output"] = manifest.output_text
        record["output_bytes"] = len(payload)
        record["output_sha256"] = digest(payload)
        record["status"] = "ASSEMBLED"
        emit(record)
        return 0
    except (ContractError, OSError) as exc:
        print(f"sectioned_output: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
