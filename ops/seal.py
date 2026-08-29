#!/usr/bin/env python3
"""Stamp or verify the campaign's BODY-END report integrity seal.

Only a standalone ``<!-- BODY-END -->`` line is a marker.  Inline or quoted
mentions are ordinary body text.  The tool never discovers files: every path
must be supplied explicitly.  A body hash detects accidental or concurrent
mutation; it is not an authenticity signature.  Full-file hashes and external
run receipts remain separate custody evidence.
"""

from __future__ import annotations

import argparse
import hashlib
import os
from pathlib import Path
import re
import secrets
import stat
import sys


MARKER = b"<!-- BODY-END -->"
HEX40 = re.compile(r"[0-9a-f]{40}\Z")
BODY_BYTES_RE = re.compile(
    r"^- Body bytes:[ \t]*`([0-9]+)`\.?[ \t]*$", re.MULTILINE
)
BODY_SHA_RE = re.compile(
    r"^- Body SHA-256:[ \t]*(?:\n[ \t]*)?`([0-9a-f]{64})`\.?[ \t]*$",
    re.MULTILINE,
)
FROZEN_BASIS_RE = re.compile(
    r"^- Frozen basis:[ \t]*`([0-9a-f]{40})`\.?[ \t]*$", re.MULTILINE
)


class SealError(ValueError):
    """A report is unsafe to read or has an invalid seal."""


class SealDurabilityWarning(SealError):
    """The installed seal verified, but its directory sync failed."""


def _validate_basis(basis: str, *, label: str = "basis") -> None:
    if HEX40.fullmatch(basis) is None:
        raise SealError(
            f"{label} must be exactly 40 lowercase hexadecimal characters"
        )


def _open_parent(path: Path) -> tuple[int, str, Path, os.stat_result]:
    """Open an anchored parent directory; leave the final name unfollowed."""
    if not path.name or path.name in {".", ".."}:
        raise SealError("target must name a file")
    try:
        parent = path.parent.resolve(strict=True)
    except OSError as exc:
        raise SealError(f"cannot resolve target parent: {exc}") from exc
    try:
        before = parent.lstat()
    except OSError as exc:
        raise SealError(f"cannot inspect target parent: {exc}") from exc
    if stat.S_ISLNK(before.st_mode) or not stat.S_ISDIR(before.st_mode):
        raise SealError("target parent is a symlink or is not a directory")
    flags = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0)
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    try:
        parent_fd = os.open(parent, flags)
    except OSError as exc:
        raise SealError(f"cannot open target parent: {exc}") from exc
    try:
        info = os.fstat(parent_fd)
        if not stat.S_ISDIR(info.st_mode) or _identity(info) != _identity(before):
            raise SealError("target parent identity changed during open")
        _check_parent_path(parent, info)
        return parent_fd, path.name, parent, info
    except Exception:
        os.close(parent_fd)
        raise


def _check_parent_path(parent: Path, expected: os.stat_result) -> None:
    try:
        current = parent.lstat()
    except OSError as exc:
        raise SealError(f"cannot recheck target parent: {exc}") from exc
    if stat.S_ISLNK(current.st_mode) or not stat.S_ISDIR(current.st_mode):
        raise SealError("target parent changed to a symlink or non-directory")
    if _identity(current) != _identity(expected):
        raise SealError("target parent identity changed")


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


def _open_regular_at(
    parent_fd: int, name: str
) -> tuple[int, os.stat_result]:
    try:
        before = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
    except OSError as exc:
        raise SealError(f"cannot inspect target before open: {exc}") from exc
    if stat.S_ISLNK(before.st_mode) or not stat.S_ISREG(before.st_mode):
        raise SealError("path is a symlink or is not a regular file")

    flags = os.O_RDONLY | getattr(os, "O_NONBLOCK", 0)
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    try:
        fd = os.open(name, flags, dir_fd=parent_fd)
    except OSError as exc:
        raise SealError(f"cannot open regular file: {exc}") from exc
    try:
        info = os.fstat(fd)
        if not stat.S_ISREG(info.st_mode):
            raise SealError("path is not a regular file")
        if _identity(before) != _identity(info):
            raise SealError("target identity changed during open")
        try:
            after = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
        except OSError as exc:
            raise SealError(f"cannot recheck target after open: {exc}") from exc
        if _identity(after) != _identity(info) or not stat.S_ISREG(after.st_mode):
            raise SealError("target identity changed during open")
        return fd, info
    except Exception:
        os.close(fd)
        raise


def _read_regular_at(
    parent_fd: int, name: str
) -> tuple[bytes, os.stat_result]:
    fd, info = _open_regular_at(parent_fd, name)
    try:
        chunks: list[bytes] = []
        while True:
            chunk = os.read(fd, 1024 * 1024)
            if not chunk:
                break
            chunks.append(chunk)
        data = b"".join(chunks)
        after = os.fstat(fd)
        if _snapshot(after) != _snapshot(info) or len(data) != after.st_size:
            raise SealError("target changed while being read")
        return data, after
    finally:
        os.close(fd)


def _read_regular(path: Path) -> tuple[bytes, os.stat_result, Path]:
    parent_fd, name, parent, parent_info = _open_parent(path)
    try:
        data, info = _read_regular_at(parent_fd, name)
        _check_parent_path(parent, parent_info)
        return data, info, parent / name
    finally:
        os.close(parent_fd)


def _create_temp_at(parent_fd: int, target_name: str, mode: int) -> tuple[int, str]:
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    for _ in range(100):
        name = f".{target_name}.seal-{os.getpid()}-{secrets.token_hex(8)}"
        try:
            fd = os.open(name, flags, 0o600, dir_fd=parent_fd)
        except FileExistsError:
            continue
        except OSError as exc:
            raise SealError(f"cannot create anchored seal temp: {exc}") from exc
        try:
            os.fchmod(fd, mode)
        except Exception:
            os.close(fd)
            try:
                os.unlink(name, dir_fd=parent_fd)
            except FileNotFoundError:
                pass
            raise
        return fd, name
    raise SealError("cannot allocate a unique anchored seal temp")


def _body_boundary(data: bytes) -> int:
    markers: list[int] = []
    offset = 0
    for line in data.splitlines(keepends=True):
        content = line[:-2] if line.endswith(b"\r\n") else line[:-1] if line.endswith(b"\n") else line
        if content == MARKER:
            if not line.endswith((b"\n", b"\r\n")):
                raise SealError("standalone BODY-END marker lacks terminating newline")
            markers.append(offset + len(line))
        offset += len(line)
    if len(markers) != 1:
        raise SealError(f"expected exactly one standalone BODY-END marker, found {len(markers)}")
    return markers[0]


def _unique(pattern: re.Pattern[str], text: str, label: str) -> str:
    values = pattern.findall(text)
    if len(values) != 1:
        raise SealError(f"expected exactly one {label} declaration, found {len(values)}")
    return values[0]


def verify_bytes(
    data: bytes, *, expected_basis: str | None = None
) -> tuple[int, str, str]:
    boundary = _body_boundary(data)
    body = data[:boundary]
    try:
        post = data[boundary:].decode("utf-8")
    except UnicodeDecodeError as exc:
        raise SealError(f"post-body seal is not UTF-8: {exc}") from exc
    post = post.replace("\r\n", "\n")
    if "\r" in post:
        raise SealError("post-body seal contains a lone carriage return")
    declared_bytes = int(_unique(BODY_BYTES_RE, post, "Body bytes"))
    declared_sha = _unique(BODY_SHA_RE, post, "Body SHA-256")
    basis = _unique(FROZEN_BASIS_RE, post, "Frozen basis")
    actual_sha = hashlib.sha256(body).hexdigest()
    if declared_bytes != len(body):
        raise SealError(
            f"body byte mismatch: declared {declared_bytes}, actual {len(body)}"
        )
    if declared_sha != actual_sha:
        raise SealError(
            f"body SHA-256 mismatch: declared {declared_sha}, actual {actual_sha}"
        )
    if expected_basis is not None and basis != expected_basis:
        raise SealError(
            f"frozen basis mismatch: declared {basis}, expected {expected_basis}"
        )
    return len(body), actual_sha, basis


def verify_path(
    path: Path, *, expected_basis: str | None = None
) -> tuple[int, str, str]:
    data, _, _ = _read_regular(path)
    return verify_bytes(data, expected_basis=expected_basis)


def _canonical_seal(body_bytes: int, body_sha: str, basis: str) -> bytes:
    return (
        "\n## Seal\n\n"
        "- Body definition: every byte through the unique standalone "
        "`<!-- BODY-END -->` line,\n"
        "  including its terminating newline; this seal is outside the body.\n"
        f"- Body bytes: `{body_bytes}`.\n"
        "- Body SHA-256:\n"
        f"  `{body_sha}`.\n"
        f"- Frozen basis: `{basis}`.\n"
    ).encode("utf-8")


def stamp_path(path: Path, basis: str) -> tuple[int, str, str]:
    _validate_basis(basis)
    parent_fd, name, parent, parent_info = _open_parent(path)
    temp_name: str | None = None
    durability_error: OSError | None = None
    try:
        data, original = _read_regular_at(parent_fd, name)
        boundary = _body_boundary(data)
        if data[boundary:].strip():
            raise SealError(
                "refusing to stamp: non-whitespace content already follows BODY-END"
            )
        body = data[:boundary]
        digest = hashlib.sha256(body).hexdigest()
        sealed = body + _canonical_seal(len(body), digest, basis)

        try:
            current = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
        except OSError as exc:
            raise SealError(f"cannot recheck target before replacement: {exc}") from exc
        if stat.S_ISLNK(current.st_mode) or not stat.S_ISREG(current.st_mode):
            raise SealError("target changed to a symlink or non-regular file")
        if _identity(current) != _identity(original):
            raise SealError("target identity changed while preparing seal")

        temp_fd, temp_name = _create_temp_at(
            parent_fd, name, stat.S_IMODE(original.st_mode)
        )
        with os.fdopen(temp_fd, "wb") as handle:
            handle.write(sealed)
            handle.flush()
            os.fsync(handle.fileno())

        # Detect both replacement and same-inode rewrites immediately before
        # the atomic install.  This is not a substitute for cooperative locks,
        # but it closes the ordinary concurrent-lane lost-update window.
        latest_data, latest = _read_regular_at(parent_fd, name)
        if _snapshot(latest) != _snapshot(original):
            raise SealError("target metadata changed before atomic replacement")
        if latest_data != data:
            raise SealError("target content changed before atomic replacement")
        _check_parent_path(parent, parent_info)

        os.replace(
            temp_name,
            name,
            src_dir_fd=parent_fd,
            dst_dir_fd=parent_fd,
        )
        temp_name = None

        installed, _ = _read_regular_at(parent_fd, name)
        if installed != sealed:
            raise SealError("installed seal differs from staged bytes")
        verify_bytes(installed, expected_basis=basis)

        try:
            _check_parent_path(parent, parent_info)
        except SealError as exc:
            durability_error = OSError(str(exc))
        try:
            os.fsync(parent_fd)
        except OSError as exc:
            durability_error = durability_error or exc
    finally:
        if temp_name is not None:
            try:
                os.unlink(temp_name, dir_fd=parent_fd)
            except FileNotFoundError:
                pass
        os.close(parent_fd)
    if durability_error is not None:
        raise SealDurabilityWarning(
            "seal was installed and verified, but directory fsync failed: "
            f"{durability_error}"
        )
    return len(body), digest, basis


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    verify = sub.add_parser("verify", help="verify one or more sealed reports")
    verify.add_argument(
        "--expected-basis",
        "--expect-basis",
        dest="expected_basis",
        help="require this exact 40-character frozen basis (never inferred)",
    )
    verify.add_argument("files", nargs="+", type=Path)
    stamp = sub.add_parser("stamp", help="append a canonical seal atomically")
    stamp.add_argument("file", type=Path)
    stamp.add_argument("--basis", required=True)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "verify":
        if args.expected_basis is not None:
            try:
                _validate_basis(args.expected_basis, label="expected basis")
            except SealError as exc:
                print(f"seal: INVALID: {exc}", file=sys.stderr)
                return 1
        failures = 0
        for path in args.files:
            try:
                size, digest, basis = verify_path(
                    path, expected_basis=args.expected_basis
                )
                print(
                    f"PASS path={path} body_bytes={size} "
                    f"body_sha256={digest} basis={basis}"
                )
            except (SealError, OSError) as exc:
                failures += 1
                print(f"seal: INVALID path={path}: {exc}", file=sys.stderr)
        return 1 if failures else 0

    try:
        size, digest, basis = stamp_path(args.file, args.basis)
        print(
            f"STAMPED path={args.file} body_bytes={size} "
            f"body_sha256={digest} basis={basis}"
        )
        return 0
    except SealDurabilityWarning as exc:
        print(f"seal: DURABILITY_WARNING path={args.file}: {exc}", file=sys.stderr)
        return 2
    except SealError as exc:
        print(f"seal: INVALID path={args.file}: {exc}", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"seal: INVALID path={args.file}: operating-system error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
