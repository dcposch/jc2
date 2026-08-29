#!/usr/bin/env python3
"""Focused regression tests for ops/seal.py."""

from __future__ import annotations

import hashlib
import importlib.util
import os
from pathlib import Path
import stat
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


OPS = Path(__file__).resolve().parent
SEAL = OPS / "seal.py"
BASIS = "e930fa90b8ee9d86220a2cff72fba94e04b20baa"
MARKER = "<!-- BODY-END -->\n"

SPEC = importlib.util.spec_from_file_location("campaign_seal", SEAL)
assert SPEC is not None and SPEC.loader is not None
SEAL_MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SEAL_MODULE)


def run(*args: str, optimized: bool = False) -> subprocess.CompletedProcess[str]:
    command = [sys.executable]
    if optimized:
        command.append("-O")
    command.extend([str(SEAL), *args])
    return subprocess.run(
        command,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        timeout=10,
    )


def sealed(body: str, *, size_delta: int = 0, digest: str | None = None) -> str:
    data = body.encode("utf-8")
    actual = hashlib.sha256(data).hexdigest()
    return body + (
        "\n## Seal\n\n"
        "- Body definition: test fixture.\n"
        f"- Body bytes: `{len(data) + size_delta}`.\n"
        f"- Body SHA-256: `{digest or actual}`.\n"
        f"- Frozen basis: `{BASIS}`.\n"
    )


class SealTest(unittest.TestCase):
    def make_file(self, text: str) -> Path:
        directory = Path(tempfile.mkdtemp(prefix="seal-test-"))
        self.addCleanup(lambda: __import__("shutil").rmtree(directory, ignore_errors=True))
        path = directory / "report.md"
        path.write_text(text, encoding="utf-8")
        return path

    def test_good_inline_mention_and_optimized_match(self) -> None:
        body = "# Report\n\nInline `<!-- BODY-END -->` is harmless.\n\n" + MARKER
        path = self.make_file(sealed(body))
        ordinary = run("verify", str(path))
        optimized = run("verify", str(path), optimized=True)
        self.assertEqual(ordinary.returncode, 0, ordinary.stderr)
        self.assertEqual(optimized.returncode, 0, optimized.stderr)
        self.assertEqual(ordinary.stdout, optimized.stdout)

    def test_body_mutation_wrong_size_and_wrong_hash_fail(self) -> None:
        body = "# Report\n\n" + MARKER
        fixtures = (
            sealed(body).replace("# Report", "# report"),
            sealed(body, size_delta=1),
            sealed(body, digest="0" * 64),
        )
        for index, fixture in enumerate(fixtures):
            with self.subTest(index=index):
                path = self.make_file(fixture)
                result = run("verify", str(path))
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("INVALID", result.stderr)

    def test_missing_and_duplicate_standalone_markers_fail(self) -> None:
        fixtures = (
            "# no marker\n",
            "# duplicate\n" + MARKER + MARKER,
            "# unterminated\n<!-- BODY-END -->",
        )
        for index, fixture in enumerate(fixtures):
            with self.subTest(index=index):
                path = self.make_file(fixture)
                result = run("verify", str(path))
                self.assertNotEqual(result.returncode, 0)

    def test_stamp_verify_roundtrip(self) -> None:
        path = self.make_file("# Fresh\n\n" + MARKER)
        path.chmod(0o640)
        stamped = run("stamp", str(path), "--basis", BASIS)
        self.assertEqual(stamped.returncode, 0, stamped.stderr)
        verified = run("verify", str(path))
        self.assertEqual(verified.returncode, 0, verified.stderr)
        self.assertIn("PASS", verified.stdout)
        self.assertEqual(stat.S_IMODE(path.stat().st_mode), 0o640)
        self.assertEqual(list(path.parent.glob(f".{path.name}.seal-*")), [])
        second = run("stamp", str(path), "--basis", BASIS)
        self.assertNotEqual(second.returncode, 0)

    def test_expected_basis_and_attributed_multi_file_failure(self) -> None:
        body = "# Basis\n\n" + MARKER
        good_a = self.make_file(sealed(body))
        bad = self.make_file("# Missing seal\n" + MARKER)
        good_b = self.make_file(sealed(body))
        result = run(
            "verify",
            "--expected-basis",
            BASIS,
            str(good_a),
            str(bad),
            str(good_b),
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout.count("PASS path="), 2)
        self.assertIn(str(bad), result.stderr)

        wrong = run("verify", "--expect-basis", "f" * 40, str(good_a))
        self.assertNotEqual(wrong.returncode, 0)
        self.assertIn("declared", wrong.stderr)
        self.assertIn("expected", wrong.stderr)

    def test_crlf_body_and_post_body_metadata(self) -> None:
        body = b"# CRLF\r\n\r\n<!-- BODY-END -->\r\n"
        digest = hashlib.sha256(body).hexdigest()
        post = (
            "\r\n## Seal\r\n\r\n"
            "- Body definition: test fixture.\r\n"
            f"- Body bytes: `{len(body)}`.\r\n"
            f"- Body SHA-256: `{digest}`.\r\n"
            f"- Frozen basis: `{BASIS}`.\r\n"
        ).encode("utf-8")
        path = self.make_file("placeholder")
        path.write_bytes(body + post)
        result = run("verify", "--expected-basis", BASIS, str(path))
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_missing_and_duplicate_metadata_fail(self) -> None:
        body = "# Metadata\n\n" + MARKER
        correct = sealed(body)
        fixtures = (
            correct.replace(f"- Frozen basis: `{BASIS}`.\n", ""),
            correct + f"- Frozen basis: `{BASIS}`.\n",
        )
        for index, fixture in enumerate(fixtures):
            with self.subTest(index=index):
                path = self.make_file(fixture)
                result = run("verify", str(path))
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("INVALID", result.stderr)

    @unittest.skipUnless(hasattr(os, "mkfifo"), "FIFOs unavailable")
    def test_fifo_refused_without_blocking(self) -> None:
        path = self.make_file("replace me")
        path.unlink()
        os.mkfifo(path)
        result = run("verify", str(path))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("regular file", result.stderr)

    def test_same_inode_rewrite_before_replace_is_detected(self) -> None:
        path = self.make_file("# Race\n\n" + MARKER)
        original_read = SEAL_MODULE._read_regular_at
        calls = 0

        def raced_read(parent_fd: int, name: str):
            nonlocal calls
            calls += 1
            if calls == 2:
                fd = os.open(name, os.O_WRONLY | os.O_APPEND, dir_fd=parent_fd)
                with os.fdopen(fd, "ab") as handle:
                    handle.write(b"concurrent rewrite\n")
            return original_read(parent_fd, name)

        with mock.patch.object(
            SEAL_MODULE, "_read_regular_at", side_effect=raced_read
        ):
            with self.assertRaises(SEAL_MODULE.SealError):
                SEAL_MODULE.stamp_path(path, BASIS)
        self.assertEqual(list(path.parent.glob(f".{path.name}.seal-*")), [])

    def test_parent_replacement_is_refused_without_touching_decoy(self) -> None:
        path = self.make_file("# Anchored\n\n" + MARKER)
        parent = path.parent
        moved = parent.with_name(parent.name + "-moved")
        self.addCleanup(lambda: __import__("shutil").rmtree(moved, ignore_errors=True))
        original_read = SEAL_MODULE._read_regular_at
        calls = 0

        def swap_parent(parent_fd: int, name: str):
            nonlocal calls
            calls += 1
            if calls == 2:
                parent.rename(moved)
                parent.mkdir()
                (parent / name).write_text("decoy\n", encoding="utf-8")
            return original_read(parent_fd, name)

        with mock.patch.object(
            SEAL_MODULE, "_read_regular_at", side_effect=swap_parent
        ):
            with self.assertRaises(SEAL_MODULE.SealError):
                SEAL_MODULE.stamp_path(path, BASIS)
        self.assertEqual(path.read_text(encoding="utf-8"), "decoy\n")
        self.assertEqual((moved / path.name).read_text(encoding="utf-8"), "# Anchored\n\n" + MARKER)

    def test_directory_fsync_failure_is_typed_after_verified_install(self) -> None:
        path = self.make_file("# Durability\n\n" + MARKER)
        real_fsync = SEAL_MODULE.os.fsync
        calls = 0

        def fail_second_fsync(fd: int) -> None:
            nonlocal calls
            calls += 1
            if calls == 2:
                raise OSError("synthetic directory fsync failure")
            real_fsync(fd)

        with mock.patch.object(SEAL_MODULE.os, "fsync", side_effect=fail_second_fsync):
            with self.assertRaises(SEAL_MODULE.SealDurabilityWarning):
                SEAL_MODULE.stamp_path(path, BASIS)
        size, digest, basis = SEAL_MODULE.verify_path(path, expected_basis=BASIS)
        self.assertGreater(size, 0)
        self.assertEqual(len(digest), 64)
        self.assertEqual(basis, BASIS)

    @unittest.skipUnless(hasattr(os, "symlink"), "symlinks unavailable")
    def test_symlink_refused(self) -> None:
        target = self.make_file(sealed("# Target\n\n" + MARKER))
        link = target.with_name("link.md")
        link.symlink_to(target)
        self.addCleanup(link.unlink, missing_ok=True)
        result = run("verify", str(link))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("INVALID", result.stderr)

    def test_non_utf8_post_body_refused(self) -> None:
        path = self.make_file("# Bytes\n\n" + MARKER)
        path.write_bytes(path.read_bytes() + b"\xff\n")
        result = run("verify", str(path))
        self.assertNotEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
