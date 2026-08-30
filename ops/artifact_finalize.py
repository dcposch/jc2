#!/usr/bin/env python3
"""Atomically publish one sealed report with a cooperative ownership lease.

The workflow is deliberately explicit and never discovers report files::

    artifact_finalize.py begin --final REPORT --basis COMMIT --owner LANE
    # write the returned partial_path, ending exactly at BODY-END
    artifact_finalize.py close --final REPORT --token TOKEN
    artifact_finalize.py finalize --final REPORT --token TOKEN
    artifact_finalize.py verify --final REPORT [--staged]

``begin`` is the only operation which allocates names.  Its capability token
owns one no-overwrite lease.  ``close`` removes write bits and records a stable
source snapshot.  ``finalize`` refuses drift, delegates canonical sealing to
``seal.py``, publishes by a no-overwrite hard link, and writes a read-only JSON
manifest.  The lease is cooperative custody, not an authentication boundary;
same-user processes can alter files, but verification detects such alteration.
Lifecycle cleanup assumes the token holder has exclusive cooperative access to
the target names; this is not a defense against a malicious same-user process
which continuously swaps directory entries.  Publication requires POSIX
``dir_fd`` operations, same-directory hard links, and directory ``fsync``.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import hmac
import importlib.util
import json
import os
from pathlib import Path
import secrets
import stat
import subprocess
import sys
from typing import Any


SCHEMA = "jc2.artifact-finalize/v1"
LEASE_SCHEMA = "jc2.artifact-lease/v1"
CLOSE_SCHEMA = "jc2.artifact-close/v1"
RELEASE_SCHEMA = "jc2.artifact-release/v1"
MAX_METADATA_BYTES = 128 * 1024

_SEAL_PATH = Path(__file__).with_name("seal.py")
_SEAL_SPEC = importlib.util.spec_from_file_location("jc2_campaign_seal", _SEAL_PATH)
if _SEAL_SPEC is None or _SEAL_SPEC.loader is None:  # pragma: no cover
    raise RuntimeError(f"cannot load {_SEAL_PATH}")
seal = importlib.util.module_from_spec(_SEAL_SPEC)
_SEAL_SPEC.loader.exec_module(seal)


class ArtifactError(ValueError):
    """The requested lifecycle transition is invalid or unsafe."""


class CollisionError(ArtifactError):
    """A no-overwrite lease, final, or manifest name is already occupied."""


@dataclass(frozen=True)
class Names:
    final: str
    lease: str
    closed: str
    release: str
    manifest: str
    partial: str | None = None


@dataclass(frozen=True)
class Published:
    final_data: bytes
    final_info: os.stat_result
    manifest_data: bytes
    manifest_info: os.stat_result
    manifest: dict[str, Any]
    body_bytes: int
    body_sha256: str
    basis: str


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def _json_bytes(value: dict[str, Any]) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode(
        "utf-8"
    )


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _snapshot_dict(info: os.stat_result) -> dict[str, int]:
    return {
        "device": info.st_dev,
        "inode": info.st_ino,
        "mode": stat.S_IMODE(info.st_mode),
        "size": info.st_size,
        "mtime_ns": info.st_mtime_ns,
        "ctime_ns": info.st_ctime_ns,
    }


def _base_names(final_name: str, *, partial: str | None = None) -> Names:
    return Names(
        final=final_name,
        lease=f".{final_name}.artifact-lease.json",
        closed=f".{final_name}.artifact-close.json",
        release=f".{final_name}.artifact-release.json",
        manifest=f"{final_name}.artifact.json",
        partial=partial,
    )


def _exists_at(parent_fd: int, name: str) -> bool:
    try:
        os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
    except FileNotFoundError:
        return False
    except OSError as exc:
        raise ArtifactError(f"cannot inspect lifecycle name {name!r}: {exc}") from exc
    return True


def _write_all(fd: int, data: bytes) -> None:
    offset = 0
    while offset < len(data):
        written = os.write(fd, data[offset:])
        if written <= 0:  # pragma: no cover - defensive OS guard
            raise OSError("short write while creating lifecycle file")
        offset += written


def _create_exclusive_at(
    parent_fd: int, name: str, data: bytes, mode: int
) -> os.stat_result:
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    try:
        fd = os.open(name, flags, 0o600, dir_fd=parent_fd)
    except FileExistsError as exc:
        raise CollisionError(f"lifecycle collision at {name!r}") from exc
    except OSError as exc:
        raise ArtifactError(f"cannot create {name!r}: {exc}") from exc
    try:
        _write_all(fd, data)
        os.fchmod(fd, mode)
        os.fsync(fd)
        return os.fstat(fd)
    except Exception:
        try:
            os.unlink(name, dir_fd=parent_fd)
        except FileNotFoundError:
            pass
        raise
    finally:
        try:
            os.close(fd)
        except OSError:
            pass


def _read_json_at(parent_fd: int, name: str) -> tuple[dict[str, Any], os.stat_result, bytes]:
    try:
        data, info = seal._read_regular_at(parent_fd, name)
    except (seal.SealError, OSError) as exc:
        raise ArtifactError(f"cannot read {name!r}: {exc}") from exc
    if len(data) > MAX_METADATA_BYTES:
        raise ArtifactError(f"metadata file {name!r} is unexpectedly large")
    try:
        value = json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ArtifactError(f"metadata file {name!r} is invalid JSON: {exc}") from exc
    if not isinstance(value, dict):
        raise ArtifactError(f"metadata file {name!r} is not a JSON object")
    if _json_bytes(value) != data:
        raise ArtifactError(f"metadata file {name!r} is not canonical JSON")
    return value, info, data


def _require_platform() -> None:
    required = (os.open, os.stat, os.unlink, os.link)
    if os.name != "posix" or any(call not in os.supports_dir_fd for call in required):
        raise ArtifactError(
            "ARTIFACT-FINALIZE/v1 requires POSIX dir_fd and hard-link support"
        )


def _sync_parent(parent_fd: int) -> None:
    try:
        os.fsync(parent_fd)
    except OSError as exc:
        raise ArtifactError(f"directory fsync failed: {exc}") from exc


def _probe_hardlink_at(parent_fd: int, source_name: str) -> None:
    probe = f".{source_name}.link-probe-{secrets.token_hex(8)}"
    try:
        try:
            os.link(
                source_name,
                probe,
                src_dir_fd=parent_fd,
                dst_dir_fd=parent_fd,
                follow_symlinks=False,
            )
        except OSError as exc:
            raise ArtifactError(
                f"target filesystem does not support required hard-link publication: {exc}"
            ) from exc
        source = os.stat(source_name, dir_fd=parent_fd, follow_symlinks=False)
        linked = os.stat(probe, dir_fd=parent_fd, follow_symlinks=False)
        if seal._identity(source) != seal._identity(linked):
            raise ArtifactError("hard-link capability probe returned a different inode")
    finally:
        try:
            os.unlink(probe, dir_fd=parent_fd)
        except FileNotFoundError:
            pass


def _verify_canonical_report(
    data: bytes, *, expected_basis: str | None = None
) -> tuple[int, str, str]:
    try:
        body_bytes, body_sha, basis = seal.verify_bytes(
            data, expected_basis=expected_basis
        )
        boundary = seal._body_boundary(data)
    except seal.SealError as exc:
        raise ArtifactError(f"canonical seal verification failed: {exc}") from exc
    expected = data[:boundary] + seal._canonical_seal(body_bytes, body_sha, basis)
    if data != expected:
        raise ArtifactError("sealed report is not byte-for-byte canonical")
    return body_bytes, body_sha, basis


def _require_mode(info: os.stat_result, expected: int, label: str) -> None:
    actual = stat.S_IMODE(info.st_mode)
    if actual != expected:
        raise ArtifactError(
            f"{label} mode changed: expected {expected:04o}, actual {actual:04o}"
        )


def _unlink_identity_at(parent_fd: int, name: str, expected: os.stat_result) -> None:
    try:
        current = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
    except OSError as exc:
        raise ArtifactError(f"cannot recheck {name!r} before cleanup: {exc}") from exc
    if seal._identity(current) != seal._identity(expected):
        raise ArtifactError(f"refusing cleanup: {name!r} identity changed")
    os.unlink(name, dir_fd=parent_fd)


def _validate_owner(owner: str) -> None:
    if not owner or len(owner) > 160 or any(ord(ch) < 32 for ch in owner):
        raise ArtifactError("owner must be 1-160 printable characters")


def _validate_lease(
    value: dict[str, Any], names: Names, token: str
) -> tuple[str, str, str]:
    required = {
        "schema",
        "lease_id",
        "token_sha256",
        "owner",
        "basis",
        "created_utc",
        "final_name",
        "partial_name",
        "close_name",
        "manifest_name",
    }
    if set(value) != required or value.get("schema") != LEASE_SCHEMA:
        raise ArtifactError("lease schema or key set is invalid")
    lease_id = value.get("lease_id")
    partial_name = value.get("partial_name")
    basis = value.get("basis")
    if not all(isinstance(item, str) for item in (lease_id, partial_name, basis)):
        raise ArtifactError("lease identifiers must be strings")
    expected_names = _base_names(names.final, partial=partial_name)
    if (
        value.get("final_name") != expected_names.final
        or value.get("close_name") != expected_names.closed
        or value.get("manifest_name") != expected_names.manifest
        or not partial_name.startswith(f".{names.final}.partial-")
        or "/" in partial_name
    ):
        raise ArtifactError("lease paths do not match the explicit final target")
    token_hash = value.get("token_sha256")
    if not isinstance(token_hash, str) or not hmac.compare_digest(
        token_hash, _sha256(token.encode("utf-8"))
    ):
        raise ArtifactError("lease token mismatch")
    try:
        seal._validate_basis(basis)
    except seal.SealError as exc:
        raise ArtifactError(str(exc)) from exc
    return lease_id, partial_name, basis


def begin(final: Path, basis: str, owner: str) -> dict[str, Any]:
    _require_platform()
    try:
        seal._validate_basis(basis)
    except seal.SealError as exc:
        raise ArtifactError(str(exc)) from exc
    _validate_owner(owner)
    parent_fd, final_name, parent, parent_info = seal._open_parent(final)
    names = _base_names(final_name)
    lease_info: os.stat_result | None = None
    partial_name: str | None = None
    partial_created = False
    try:
        _sync_parent(parent_fd)
        for occupied in (names.final, names.manifest, names.closed, names.release):
            if _exists_at(parent_fd, occupied):
                raise CollisionError(f"lifecycle collision at {occupied!r}")
        lease_id = secrets.token_hex(16)
        # Hex avoids leading '-' values which argparse can interpret as an
        # option when the token is supplied as the next command-line argument.
        token = secrets.token_hex(32)
        partial_name = f".{final_name}.partial-{lease_id}"
        lease = {
            "schema": LEASE_SCHEMA,
            "lease_id": lease_id,
            "token_sha256": _sha256(token.encode("utf-8")),
            "owner": owner,
            "basis": basis,
            "created_utc": _utc_now(),
            "final_name": final_name,
            "partial_name": partial_name,
            "close_name": names.closed,
            "manifest_name": names.manifest,
        }
        lease_info = _create_exclusive_at(
            parent_fd, names.lease, _json_bytes(lease), 0o400
        )
        # Recheck the publication names after winning the common lease.
        for occupied in (names.final, names.manifest, names.closed, names.release):
            if _exists_at(parent_fd, occupied):
                raise CollisionError(f"lifecycle collision at {occupied!r}")
        _create_exclusive_at(parent_fd, partial_name, b"", 0o600)
        partial_created = True
        _probe_hardlink_at(parent_fd, partial_name)
        seal._check_parent_path(parent, parent_info)
        _sync_parent(parent_fd)
        return {
            "status": "OPEN",
            "owner": owner,
            "basis": basis,
            "token": token,
            "final_path": str(parent / final_name),
            "partial_path": str(parent / partial_name),
            "lease_path": str(parent / names.lease),
        }
    except Exception:
        if partial_name is not None and partial_created:
            try:
                os.unlink(partial_name, dir_fd=parent_fd)
            except FileNotFoundError:
                pass
        if lease_info is not None:
            try:
                _unlink_identity_at(parent_fd, names.lease, lease_info)
            except (ArtifactError, FileNotFoundError):
                pass
        raise
    finally:
        os.close(parent_fd)


def close(final: Path, token: str) -> dict[str, Any]:
    _require_platform()
    parent_fd, final_name, parent, parent_info = seal._open_parent(final)
    names = _base_names(final_name)
    try:
        _sync_parent(parent_fd)
        lease, _, _ = _read_json_at(parent_fd, names.lease)
        lease_id, partial_name, basis = _validate_lease(lease, names, token)
        if _exists_at(parent_fd, names.release):
            raise ArtifactError("release is pending; rerun finalize instead of close")

        if _exists_at(parent_fd, names.closed):
            record, _, _ = _read_json_at(parent_fd, names.closed)
            _validate_close(record, lease_id, partial_name, basis, final_name)
            if _exists_at(parent_fd, partial_name):
                current, info = seal._read_regular_at(parent_fd, partial_name)
                try:
                    body_bytes, body_sha, _ = _verify_canonical_report(
                        current, expected_basis=basis
                    )
                except ArtifactError:
                    if (
                        _snapshot_dict(info) != record["source_snapshot"]
                        or len(current) != record["source_bytes"]
                        or _sha256(current) != record["source_sha256"]
                    ):
                        raise ArtifactError(
                            "partial report changed after the recorded close"
                        )
                else:
                    if (
                        body_bytes != record["source_bytes"]
                        or body_sha != record["source_sha256"]
                    ):
                        raise ArtifactError(
                            "sealed partial body differs from the recorded close"
                        )
            elif _exists_at(parent_fd, names.final):
                current, _ = seal._read_regular_at(parent_fd, names.final)
                body_bytes, body_sha, _ = _verify_canonical_report(
                    current, expected_basis=basis
                )
                if (
                    body_bytes != record["source_bytes"]
                    or body_sha != record["source_sha256"]
                ):
                    raise ArtifactError("published body differs from the recorded close")
            else:
                raise ArtifactError("closed workflow has neither partial nor final artifact")
            return {
                "status": "CLOSED",
                "final_path": str(parent / final_name),
                "partial_path": str(parent / partial_name),
                "source_bytes": record["source_bytes"],
                "source_sha256": record["source_sha256"],
                "basis": basis,
                "idempotent": True,
            }

        for occupied in (names.final, names.manifest):
            if _exists_at(parent_fd, occupied):
                raise CollisionError(f"lifecycle collision at {occupied!r}")

        try:
            before, _ = seal._read_regular_at(parent_fd, partial_name)
            boundary = seal._body_boundary(before)
        except (seal.SealError, OSError) as exc:
            raise ArtifactError(f"partial report is not closable: {exc}") from exc
        if boundary != len(before):
            raise ArtifactError(
                "partial report must end exactly after the BODY-END newline"
            )

        fd, _ = seal._open_regular_at(parent_fd, partial_name)
        try:
            os.fchmod(fd, 0o400)
            os.fsync(fd)
        finally:
            os.close(fd)
        after, info = seal._read_regular_at(parent_fd, partial_name)
        if after != before:
            raise ArtifactError("partial report changed while it was being closed")
        snapshot = _snapshot_dict(info)
        record = {
            "schema": CLOSE_SCHEMA,
            "lease_id": lease_id,
            "final_name": final_name,
            "partial_name": partial_name,
            "basis": basis,
            "closed_utc": _utc_now(),
            "source_bytes": len(after),
            "source_sha256": _sha256(after),
            "source_snapshot": snapshot,
        }
        _create_exclusive_at(parent_fd, names.closed, _json_bytes(record), 0o400)
        seal._check_parent_path(parent, parent_info)
        _sync_parent(parent_fd)
        return {
            "status": "CLOSED",
            "final_path": str(parent / final_name),
            "partial_path": str(parent / partial_name),
            "source_bytes": len(after),
            "source_sha256": record["source_sha256"],
            "basis": basis,
            "idempotent": False,
        }
    finally:
        os.close(parent_fd)


def _validate_close(
    value: dict[str, Any], lease_id: str, partial_name: str, basis: str, final_name: str
) -> None:
    required = {
        "schema",
        "lease_id",
        "final_name",
        "partial_name",
        "basis",
        "closed_utc",
        "source_bytes",
        "source_sha256",
        "source_snapshot",
    }
    if set(value) != required or value.get("schema") != CLOSE_SCHEMA:
        raise ArtifactError("close record schema or key set is invalid")
    if (
        value.get("lease_id") != lease_id
        or value.get("partial_name") != partial_name
        or value.get("basis") != basis
        or value.get("final_name") != final_name
    ):
        raise ArtifactError("close record does not match the lease")
    if not isinstance(value.get("source_bytes"), int):
        raise ArtifactError("close record source length is invalid")
    digest = value.get("source_sha256")
    if not isinstance(digest, str) or len(digest) != 64:
        raise ArtifactError("close record source digest is invalid")
    snapshot = value.get("source_snapshot")
    if not isinstance(snapshot, dict) or set(snapshot) != {
        "device",
        "inode",
        "mode",
        "size",
        "mtime_ns",
        "ctime_ns",
    }:
        raise ArtifactError("close record source snapshot is invalid")


def _make_manifest(
    *,
    lease: dict[str, Any],
    closed: dict[str, Any],
    sealed_data: bytes,
    body_bytes: int,
    body_sha256: str,
    basis: str,
) -> dict[str, Any]:
    return {
        "schema": SCHEMA,
        "artifact": {
            "name": lease["final_name"],
            "file_bytes": len(sealed_data),
            "full_sha256": _sha256(sealed_data),
            "body_bytes": body_bytes,
            "body_sha256": body_sha256,
            "frozen_basis": basis,
            "published_mode": "0444",
        },
        "custody": {
            "owner": lease["owner"],
            "lease_id": lease["lease_id"],
            "opened_utc": lease["created_utc"],
            "closed_utc": closed["closed_utc"],
            "finalized_utc": _utc_now(),
            "source_bytes": closed["source_bytes"],
            "source_sha256": closed["source_sha256"],
        },
    }


def _publish_manifest_at(
    parent_fd: int, manifest_name: str, data: bytes, target_name: str
) -> os.stat_result:
    temp_name = f".{target_name}.manifest-{os.getpid()}-{secrets.token_hex(8)}"
    temp_info: os.stat_result | None = None
    try:
        # The inode is in its final mode before the no-overwrite link.  Thus a
        # crash immediately after link publication is an idempotently
        # recoverable state, not a permanent 0400 intermediate.
        temp_info = _create_exclusive_at(parent_fd, temp_name, data, 0o444)
        try:
            os.link(
                temp_name,
                manifest_name,
                src_dir_fd=parent_fd,
                dst_dir_fd=parent_fd,
                follow_symlinks=False,
            )
        except FileExistsError as exc:
            raise CollisionError(f"lifecycle collision at {manifest_name!r}") from exc
        except OSError as exc:
            raise ArtifactError(f"cannot publish manifest: {exc}") from exc
        fd, info = seal._open_regular_at(parent_fd, manifest_name)
        try:
            if temp_info is None or seal._identity(info) != seal._identity(temp_info):
                raise ArtifactError("published manifest identity differs from staged data")
            _require_mode(info, 0o444, "published metadata")
            os.fsync(fd)
            return os.fstat(fd)
        finally:
            os.close(fd)
    finally:
        try:
            os.unlink(temp_name, dir_fd=parent_fd)
        except FileNotFoundError:
            pass


def finalize(final: Path, token: str) -> dict[str, Any]:
    _require_platform()
    parent_fd, final_name, parent, parent_info = seal._open_parent(final)
    names = _base_names(final_name)
    try:
        _sync_parent(parent_fd)
        if (
            _exists_at(parent_fd, names.final)
            and _exists_at(parent_fd, names.manifest)
            and not any(
                _exists_at(parent_fd, name)
                for name in (names.lease, names.closed, names.release)
            )
        ):
            published = _validate_published_pair(parent_fd, names)
            result = _result_from_published(
                parent, names, published, recovered=True
            )
            seal._check_parent_path(parent, parent_info)
            return result
        if _exists_at(parent_fd, names.release):
            result = _finish_release(parent_fd, parent, names, token)
            seal._check_parent_path(parent, parent_info)
            return result

        lease, _, lease_data = _read_json_at(parent_fd, names.lease)
        lease_id, partial_name, basis = _validate_lease(lease, names, token)
        closed, _, close_data = _read_json_at(parent_fd, names.closed)
        _validate_close(closed, lease_id, partial_name, basis, final_name)
        final_exists = _exists_at(parent_fd, names.final)
        manifest_exists = _exists_at(parent_fd, names.manifest)
        partial_exists = _exists_at(parent_fd, partial_name)
        if manifest_exists and not final_exists:
            raise ArtifactError("manifest exists without its final artifact")

        resumed_publication = final_exists or manifest_exists
        if final_exists:
            if not partial_exists:
                raise ArtifactError(
                    "final exists without the leased partial or a release record"
                )
            final_data, final_info = seal._read_regular_at(parent_fd, names.final)
            partial_data, partial_info = seal._read_regular_at(parent_fd, partial_name)
            if (
                seal._identity(final_info) != seal._identity(partial_info)
                or final_data != partial_data
            ):
                raise CollisionError("existing final is not the leased hard link")
            _require_mode(final_info, 0o444, "final artifact")
            body_bytes, body_sha, stamped_basis = _verify_canonical_report(
                final_data, expected_basis=basis
            )
        else:
            if not partial_exists:
                raise ArtifactError("leased partial report is missing")
            partial_path = parent / partial_name
            source, source_info = seal._read_regular_at(parent_fd, partial_name)
            if (
                _snapshot_dict(source_info) == closed["source_snapshot"]
                and len(source) == closed["source_bytes"]
                and _sha256(source) == closed["source_sha256"]
            ):
                try:
                    body_bytes, body_sha, stamped_basis = seal.stamp_path(
                        partial_path, basis
                    )
                except (seal.SealError, seal.SealDurabilityWarning, OSError) as exc:
                    raise ArtifactError(f"canonical sealing failed: {exc}") from exc
            else:
                try:
                    body_bytes, body_sha, stamped_basis = _verify_canonical_report(
                        source, expected_basis=basis
                    )
                except ArtifactError as exc:
                    if "byte-for-byte canonical" in str(exc):
                        raise
                    raise ArtifactError(
                        "partial report changed after close; refusing stale hash"
                    ) from exc
            fd, _ = seal._open_regular_at(parent_fd, partial_name)
            try:
                os.fchmod(fd, 0o444)
                os.fsync(fd)
            finally:
                os.close(fd)
            sealed_data, sealed_info = seal._read_regular_at(parent_fd, partial_name)
            verified = _verify_canonical_report(sealed_data, expected_basis=basis)
            if verified != (body_bytes, body_sha, basis):
                raise ArtifactError("sealed partial changed before publication")
            try:
                os.link(
                    partial_name,
                    final_name,
                    src_dir_fd=parent_fd,
                    dst_dir_fd=parent_fd,
                    follow_symlinks=False,
                )
            except FileExistsError as exc:
                raise CollisionError(f"lifecycle collision at {final_name!r}") from exc
            except OSError as exc:
                raise ArtifactError(f"cannot publish final by hard link: {exc}") from exc
            final_info = os.stat(final_name, dir_fd=parent_fd, follow_symlinks=False)
            if seal._identity(final_info) != seal._identity(sealed_info):
                raise ArtifactError("published final differs from sealed partial")
            _sync_parent(parent_fd)

        if (
            body_bytes != closed["source_bytes"]
            or body_sha != closed["source_sha256"]
            or stamped_basis != basis
        ):
            raise ArtifactError("sealed body does not match the closed source snapshot")

        if not manifest_exists:
            installed, _ = seal._read_regular_at(parent_fd, names.final)
            manifest = _make_manifest(
                lease=lease,
                closed=closed,
                sealed_data=installed,
                body_bytes=body_bytes,
                body_sha256=body_sha,
                basis=basis,
            )
            _publish_manifest_at(
                parent_fd, names.manifest, _json_bytes(manifest), final_name
            )
            _sync_parent(parent_fd)
        published = _validate_published_pair(
            parent_fd,
            names,
            expected_basis=basis,
            lease=lease,
            closed=closed,
        )
        release = _make_release(
            names, lease, closed, lease_data, close_data, published
        )
        _publish_manifest_at(
            parent_fd,
            names.release,
            _json_bytes(release),
            f"{final_name}.release",
        )
        _sync_parent(parent_fd)
        result = _finish_release(parent_fd, parent, names, token)
        result["recovered"] = resumed_publication
        seal._check_parent_path(parent, parent_info)
        return result
    finally:
        os.close(parent_fd)


def _manifest_fields(
    value: dict[str, Any], final_name: str
) -> tuple[dict[str, Any], dict[str, Any]]:
    if set(value) != {"schema", "artifact", "custody"} or value.get("schema") != SCHEMA:
        raise ArtifactError("manifest schema or key set is invalid")
    artifact = value.get("artifact")
    custody = value.get("custody")
    if not isinstance(artifact, dict) or not isinstance(custody, dict):
        raise ArtifactError("manifest sections must be JSON objects")
    if set(artifact) != {
        "name",
        "file_bytes",
        "full_sha256",
        "body_bytes",
        "body_sha256",
        "frozen_basis",
        "published_mode",
    }:
        raise ArtifactError("manifest artifact key set is invalid")
    if set(custody) != {
        "owner",
        "lease_id",
        "opened_utc",
        "closed_utc",
        "finalized_utc",
        "source_bytes",
        "source_sha256",
    }:
        raise ArtifactError("manifest custody key set is invalid")
    if artifact.get("name") != final_name:
        raise ArtifactError("manifest names a different artifact")
    return artifact, custody


def _validate_published_pair(
    parent_fd: int,
    names: Names,
    *,
    expected_basis: str | None = None,
    lease: dict[str, Any] | None = None,
    closed: dict[str, Any] | None = None,
) -> Published:
    final_data, final_info = seal._read_regular_at(parent_fd, names.final)
    manifest, manifest_info, manifest_data = _read_json_at(
        parent_fd, names.manifest
    )
    _require_mode(final_info, 0o444, "final artifact")
    _require_mode(manifest_info, 0o444, "artifact manifest")
    body_bytes, body_sha, basis = _verify_canonical_report(
        final_data, expected_basis=expected_basis
    )
    artifact, custody = _manifest_fields(manifest, names.final)
    if (
        artifact.get("file_bytes") != len(final_data)
        or artifact.get("full_sha256") != _sha256(final_data)
        or artifact.get("body_bytes") != body_bytes
        or artifact.get("body_sha256") != body_sha
        or artifact.get("frozen_basis") != basis
        or artifact.get("published_mode") != "0444"
        or custody.get("source_bytes") != body_bytes
        or custody.get("source_sha256") != body_sha
        or not isinstance(custody.get("finalized_utc"), str)
    ):
        raise ArtifactError("manifest fields do not match the sealed artifact")
    if lease is not None and closed is not None and (
        custody.get("owner") != lease.get("owner")
        or custody.get("lease_id") != lease.get("lease_id")
        or custody.get("opened_utc") != lease.get("created_utc")
        or custody.get("closed_utc") != closed.get("closed_utc")
        or custody.get("source_bytes") != closed.get("source_bytes")
        or custody.get("source_sha256") != closed.get("source_sha256")
    ):
        raise ArtifactError("manifest custody does not match lease and close records")

    final_again, final_again_info = seal._read_regular_at(parent_fd, names.final)
    _, manifest_again_info, manifest_again = _read_json_at(parent_fd, names.manifest)
    if (
        final_again != final_data
        or seal._snapshot(final_again_info) != seal._snapshot(final_info)
        or manifest_again != manifest_data
        or seal._snapshot(manifest_again_info) != seal._snapshot(manifest_info)
    ):
        raise ArtifactError("artifact or manifest changed during verification")
    return Published(
        final_data=final_data,
        final_info=final_info,
        manifest_data=manifest_data,
        manifest_info=manifest_info,
        manifest=manifest,
        body_bytes=body_bytes,
        body_sha256=body_sha,
        basis=basis,
    )


def _make_release(
    names: Names,
    lease: dict[str, Any],
    closed: dict[str, Any],
    lease_data: bytes,
    close_data: bytes,
    published: Published,
) -> dict[str, Any]:
    return {
        "schema": RELEASE_SCHEMA,
        "lease_id": lease["lease_id"],
        "token_sha256": lease["token_sha256"],
        "final_name": names.final,
        "partial_name": lease["partial_name"],
        "manifest_name": names.manifest,
        "lease_name": names.lease,
        "close_name": names.closed,
        "basis": published.basis,
        "body_bytes": published.body_bytes,
        "body_sha256": published.body_sha256,
        "full_sha256": _sha256(published.final_data),
        "manifest_sha256": _sha256(published.manifest_data),
        "lease_sha256": _sha256(lease_data),
        "close_sha256": _sha256(close_data),
        "finalized_utc": published.manifest["custody"]["finalized_utc"],
        "release_utc": _utc_now(),
    }


def _validate_release(
    value: dict[str, Any], names: Names, token: str
) -> tuple[str, str]:
    required = {
        "schema",
        "lease_id",
        "token_sha256",
        "final_name",
        "partial_name",
        "manifest_name",
        "lease_name",
        "close_name",
        "basis",
        "body_bytes",
        "body_sha256",
        "full_sha256",
        "manifest_sha256",
        "lease_sha256",
        "close_sha256",
        "finalized_utc",
        "release_utc",
    }
    if set(value) != required or value.get("schema") != RELEASE_SCHEMA:
        raise ArtifactError("release record schema or key set is invalid")
    partial_name = value.get("partial_name")
    if (
        not isinstance(partial_name, str)
        or not partial_name.startswith(f".{names.final}.partial-")
        or "/" in partial_name
        or value.get("final_name") != names.final
        or value.get("manifest_name") != names.manifest
        or value.get("lease_name") != names.lease
        or value.get("close_name") != names.closed
    ):
        raise ArtifactError("release record paths do not match the target")
    token_hash = value.get("token_sha256")
    if not isinstance(token_hash, str) or not hmac.compare_digest(
        token_hash, _sha256(token.encode("utf-8"))
    ):
        raise ArtifactError("release token mismatch")
    basis = value.get("basis")
    try:
        seal._validate_basis(basis)
    except (seal.SealError, TypeError) as exc:
        raise ArtifactError(f"release basis is invalid: {exc}") from exc
    for key in (
        "body_sha256",
        "full_sha256",
        "manifest_sha256",
        "lease_sha256",
        "close_sha256",
    ):
        digest = value.get(key)
        if (
            not isinstance(digest, str)
            or len(digest) != 64
            or any(ch not in "0123456789abcdef" for ch in digest)
        ):
            raise ArtifactError(f"release digest {key!r} is invalid")
    if not isinstance(value.get("body_bytes"), int):
        raise ArtifactError("release body length is invalid")
    return partial_name, basis


def _result_from_published(
    parent: Path, names: Names, published: Published, *, recovered: bool
) -> dict[str, Any]:
    return {
        "status": "FINAL",
        "final_path": str(parent / names.final),
        "manifest_path": str(parent / names.manifest),
        "file_bytes": len(published.final_data),
        "full_sha256": _sha256(published.final_data),
        "body_bytes": published.body_bytes,
        "body_sha256": published.body_sha256,
        "manifest_sha256": _sha256(published.manifest_data),
        "basis": published.basis,
        "recovered": recovered,
    }


def _finish_release(
    parent_fd: int, parent: Path, names: Names, token: str
) -> dict[str, Any]:
    release, release_info, _ = _read_json_at(parent_fd, names.release)
    _require_mode(release_info, 0o444, "artifact release record")
    partial_name, basis = _validate_release(release, names, token)
    published = _validate_published_pair(
        parent_fd, names, expected_basis=basis
    )
    if (
        published.body_bytes != release["body_bytes"]
        or published.body_sha256 != release["body_sha256"]
        or _sha256(published.final_data) != release["full_sha256"]
        or _sha256(published.manifest_data) != release["manifest_sha256"]
        or published.manifest["custody"]["lease_id"] != release["lease_id"]
        or published.manifest["custody"]["finalized_utc"]
        != release["finalized_utc"]
    ):
        raise ArtifactError("release record does not match final publication")

    if _exists_at(parent_fd, partial_name):
        partial_data, partial_info = seal._read_regular_at(parent_fd, partial_name)
        if (
            seal._identity(partial_info) != seal._identity(published.final_info)
            or partial_data != published.final_data
        ):
            raise ArtifactError("release partial is not the published final hard link")
        _unlink_identity_at(parent_fd, partial_name, partial_info)
    for name, digest_key in (
        (names.closed, "close_sha256"),
        (names.lease, "lease_sha256"),
    ):
        if _exists_at(parent_fd, name):
            _, info, data = _read_json_at(parent_fd, name)
            if _sha256(data) != release[digest_key]:
                raise ArtifactError(f"refusing cleanup: {name!r} content changed")
            _unlink_identity_at(parent_fd, name, info)
    _sync_parent(parent_fd)
    _unlink_identity_at(parent_fd, names.release, release_info)
    _sync_parent(parent_fd)
    return _result_from_published(parent, names, published, recovered=True)


def _git_blob_id(repo: Path, data: bytes) -> str:
    proc = subprocess.run(
        ["git", "-C", str(repo), "hash-object", "--stdin"],
        input=data,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if proc.returncode != 0:
        detail = proc.stderr.decode(errors="replace").strip()
        raise ArtifactError(f"git hash-object failed: {detail}")
    return proc.stdout.decode("ascii").strip()


def _verify_staged(parent: Path, paths_and_data: list[tuple[Path, bytes]]) -> dict[str, str]:
    root_proc = subprocess.run(
        ["git", "-C", str(parent), "rev-parse", "--show-toplevel"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if root_proc.returncode != 0:
        raise ArtifactError("staged verification requires a Git worktree")
    root = Path(os.fsdecode(root_proc.stdout).strip()).resolve(strict=True)
    relative: list[str] = []
    for path, _ in paths_and_data:
        try:
            # `parent` is already an anchored resolved directory.  Keep the
            # final component lexical so a live symlink swap cannot redirect
            # the index query after the verified file was opened.
            relative.append(str(path.relative_to(root)))
        except ValueError as exc:
            raise ArtifactError(f"{path} is outside the Git worktree") from exc
    proc = subprocess.run(
        ["git", "-C", str(root), "ls-files", "--stage", "-z", "--", *relative],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if proc.returncode != 0:
        detail = proc.stderr.decode(errors="replace").strip()
        raise ArtifactError(f"git index query failed: {detail}")
    entries: dict[str, tuple[str, str]] = {}
    for row in proc.stdout.split(b"\0"):
        if not row:
            continue
        try:
            meta, raw_path = row.split(b"\t", 1)
            mode, object_id, stage = meta.decode("ascii").split()
        except ValueError as exc:
            raise ArtifactError("unexpected git ls-files output") from exc
        path_text = os.fsdecode(raw_path)
        if stage != "0" or path_text in entries:
            raise ArtifactError(f"{path_text!r} is not a unique stage-0 index entry")
        entries[path_text] = (mode, object_id)
    result: dict[str, str] = {}
    for rel, (_, data) in zip(relative, paths_and_data):
        if rel not in entries:
            raise ArtifactError(f"{rel!r} is not staged")
        if entries[rel][0] != "100644":
            raise ArtifactError(
                f"staged mode for {rel!r} is {entries[rel][0]}, expected 100644"
            )
        expected = _git_blob_id(root, data)
        if entries[rel][1] != expected:
            raise ArtifactError(f"staged blob for {rel!r} differs from current verified bytes")
        result[rel] = expected
    return result


def verify(
    final: Path,
    *,
    expected_basis: str | None = None,
    expected_manifest_sha256: str | None = None,
    staged: bool = False,
) -> dict[str, Any]:
    _require_platform()
    if expected_basis is not None:
        try:
            seal._validate_basis(expected_basis, label="expected basis")
        except seal.SealError as exc:
            raise ArtifactError(str(exc)) from exc
    parent_fd, final_name, parent, parent_info = seal._open_parent(final)
    names = _base_names(final_name)
    try:
        published = _validate_published_pair(
            parent_fd, names, expected_basis=expected_basis
        )
        if expected_manifest_sha256 is not None and not hmac.compare_digest(
            _sha256(published.manifest_data), expected_manifest_sha256
        ):
            raise ArtifactError("manifest SHA-256 differs from the expected custody hash")
        residues = [
            name
            for name in (names.lease, names.closed, names.release)
            if _exists_at(parent_fd, name)
        ]
        if residues:
            raise ArtifactError(
                "artifact custody is not released; rerun finalize: "
                + ", ".join(repr(name) for name in residues)
            )
        seal._check_parent_path(parent, parent_info)
        staged_blobs: dict[str, str] | None = None
        if staged:
            staged_blobs = _verify_staged(
                parent,
                [
                    (parent / final_name, published.final_data),
                    (parent / names.manifest, published.manifest_data),
                ],
            )
            after_git = _validate_published_pair(
                parent_fd, names, expected_basis=published.basis
            )
            if (
                seal._snapshot(after_git.final_info)
                != seal._snapshot(published.final_info)
                or seal._snapshot(after_git.manifest_info)
                != seal._snapshot(published.manifest_info)
                or after_git.final_data != published.final_data
                or after_git.manifest_data != published.manifest_data
            ):
                raise ArtifactError("artifact changed during staged verification")
        return {
            "status": "VERIFIED",
            "final_path": str(parent / final_name),
            "manifest_path": str(parent / names.manifest),
            "file_bytes": len(published.final_data),
            "full_sha256": _sha256(published.final_data),
            "body_bytes": published.body_bytes,
            "body_sha256": published.body_sha256,
            "manifest_sha256": _sha256(published.manifest_data),
            "basis": published.basis,
            "staged_blobs": staged_blobs,
        }
    finally:
        os.close(parent_fd)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    begin_parser = sub.add_parser("begin", help="acquire a no-overwrite artifact lease")
    begin_parser.add_argument("--final", required=True, type=Path)
    begin_parser.add_argument("--basis", required=True)
    begin_parser.add_argument("--owner", required=True)
    close_parser = sub.add_parser("close", help="freeze the completed partial report")
    close_parser.add_argument("--final", required=True, type=Path)
    close_parser.add_argument("--token", required=True)
    finalize_parser = sub.add_parser("finalize", help="seal and atomically publish")
    finalize_parser.add_argument("--final", required=True, type=Path)
    finalize_parser.add_argument("--token", required=True)
    verify_parser = sub.add_parser(
        "verify", help="verify final, manifest, and optionally Git index"
    )
    verify_parser.add_argument("--final", required=True, type=Path)
    verify_parser.add_argument("--expected-basis")
    verify_parser.add_argument("--expected-manifest-sha256")
    verify_parser.add_argument("--staged", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "begin":
            result = begin(args.final, args.basis, args.owner)
        elif args.command == "close":
            result = close(args.final, args.token)
        elif args.command == "finalize":
            result = finalize(args.final, args.token)
        else:
            result = verify(
                args.final,
                expected_basis=args.expected_basis,
                expected_manifest_sha256=args.expected_manifest_sha256,
                staged=args.staged,
            )
        print(json.dumps(result, sort_keys=True))
        return 0
    except CollisionError as exc:
        print(f"artifact-finalize: COLLISION: {exc}", file=sys.stderr)
        return 3
    except (ArtifactError, seal.SealError, OSError) as exc:
        print(f"artifact-finalize: INVALID: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
