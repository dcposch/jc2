#!/usr/bin/env python3
"""Focused temporary-directory tests for ARTIFACT-FINALIZE/v1."""

from __future__ import annotations

import json
import hashlib
import importlib.util
import os
from pathlib import Path
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


TOOL = Path(__file__).with_name("artifact_finalize.py")
BASIS = "4c91d6fc398d1b4f2b8ca1a11d69c4bb3fef9c0d"
BODY = "# Transaction test\n\n<!-- BODY-END -->\n"

SPEC = importlib.util.spec_from_file_location("campaign_artifact_finalize", TOOL)
assert SPEC is not None and SPEC.loader is not None
TOOL_MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = TOOL_MODULE
SPEC.loader.exec_module(TOOL_MODULE)


def run(*args: str, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(TOOL), *args],
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        timeout=10,
    )


def output_json(result: subprocess.CompletedProcess[str]) -> dict[str, object]:
    if result.returncode != 0:
        raise AssertionError(result.stderr)
    value = json.loads(result.stdout)
    if not isinstance(value, dict):
        raise AssertionError("tool output is not a JSON object")
    return value


class ArtifactFinalizeTest(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory(prefix="artifact-finalize-test-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.final = self.root / "report.md"

    def init_git_repo(self) -> tuple[Path, str, str]:
        repo = self.root / "repo"
        repo.mkdir()
        subprocess.run(["git", "init", "-q"], cwd=repo, check=True, timeout=10)
        subprocess.run(
            ["git", "config", "user.name", "Artifact Test"],
            cwd=repo,
            check=True,
            timeout=10,
        )
        subprocess.run(
            ["git", "config", "user.email", "artifact@example.invalid"],
            cwd=repo,
            check=True,
            timeout=10,
        )
        (repo / "anchor.txt").write_text("basis anchor\n", encoding="utf-8")
        subprocess.run(
            ["git", "add", "--", "anchor.txt"], cwd=repo, check=True, timeout=10
        )
        subprocess.run(
            ["git", "commit", "-q", "-m", "basis anchor"],
            cwd=repo,
            check=True,
            timeout=10,
        )
        head = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=repo,
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            timeout=10,
        ).stdout.strip()
        tree = subprocess.run(
            ["git", "rev-parse", "HEAD^{tree}"],
            cwd=repo,
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            timeout=10,
        ).stdout.strip()
        return repo, head, tree

    def begin(self) -> dict[str, object]:
        return output_json(
            run(
                "begin",
                "--final",
                str(self.final),
                "--basis",
                BASIS,
                "--owner",
                "test-lane",
                "--allow-non-git-basis",
            )
        )

    def close(self, opened: dict[str, object]) -> dict[str, object]:
        return output_json(
            run(
                "close",
                "--final",
                str(self.final),
                "--token",
                str(opened["token"]),
            )
        )

    def finalize(self, opened: dict[str, object]) -> dict[str, object]:
        return output_json(
            run(
                "finalize",
                "--final",
                str(self.final),
                "--token",
                str(opened["token"]),
            )
        )

    def complete(self) -> tuple[dict[str, object], dict[str, object]]:
        opened = self.begin()
        Path(str(opened["partial_path"])).write_text(BODY, encoding="utf-8")
        self.close(opened)
        return opened, self.finalize(opened)

    @unittest.skipUnless(shutil.which("git"), "Git required")
    def test_begin_requires_exact_git_commit_without_filesystem_residue(self) -> None:
        outside = run(
            "begin",
            "--final",
            str(self.final),
            "--basis",
            BASIS,
            "--owner",
            "strict-test",
        )
        self.assertNotEqual(outside.returncode, 0)
        self.assertIn("requires a Git worktree", outside.stderr)
        self.assertEqual(list(self.root.iterdir()), [])

        repo, head, tree = self.init_git_repo()
        cases = (
            ("missing.md", "f" * 40, "not a commit"),
            ("short.md", head[:12], "40 lowercase hexadecimal"),
            ("tree.md", tree, "not a commit"),
        )
        for name, basis, message in cases:
            with self.subTest(name=name):
                result = run(
                    "begin",
                    "--final",
                    str(repo / name),
                    "--basis",
                    basis,
                    "--owner",
                    "strict-test",
                )
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(message, result.stderr)
                self.assertFalse((repo / name).exists())
                self.assertFalse((repo / f".{name}.artifact-lease.json").exists())
                self.assertEqual(list(repo.glob(f".{name}.partial-*")), [])

        opened = output_json(
            run(
                "begin",
                "--final",
                str(repo / "valid.md"),
                "--basis",
                head,
                "--owner",
                "strict-test",
            )
        )
        self.assertEqual(opened["basis"], head)
        self.assertTrue(Path(str(opened["lease_path"])).is_file())
        self.assertTrue(Path(str(opened["partial_path"])).is_file())

    def test_non_git_fixture_requires_explicit_opt_out(self) -> None:
        opened = self.begin()
        self.assertEqual(opened["basis"], BASIS)
        self.assertTrue(Path(str(opened["lease_path"])).is_file())

    def test_roundtrip_manifest_and_custody_cleanup(self) -> None:
        opened, finished = self.complete()
        manifest = Path(str(finished["manifest_path"]))
        self.assertTrue(self.final.is_file())
        self.assertTrue(manifest.is_file())
        self.assertFalse(Path(str(opened["partial_path"])).exists())
        self.assertFalse(Path(str(opened["lease_path"])).exists())
        self.assertFalse((self.root / ".report.md.artifact-close.json").exists())
        self.assertEqual(stat.S_IMODE(self.final.stat().st_mode) & 0o222, 0)
        self.assertEqual(stat.S_IMODE(manifest.stat().st_mode) & 0o222, 0)

        verified = run(
            "verify",
            "--final",
            str(self.final),
            "--expected-basis",
            BASIS,
            "--expected-manifest-sha256",
            str(finished["manifest_sha256"]),
        )
        result = output_json(verified)
        self.assertEqual(result["full_sha256"], finished["full_sha256"])
        self.assertEqual(result["body_sha256"], finished["body_sha256"])
        manifest_value = json.loads(manifest.read_text(encoding="utf-8"))
        self.assertEqual(manifest_value["schema"], "jc2.artifact-finalize/v1")
        self.assertEqual(manifest_value["custody"]["source_sha256"], finished["body_sha256"])

    def test_two_writer_collision_preserves_first_lease(self) -> None:
        base = [
            sys.executable,
            str(TOOL),
            "begin",
            "--final",
            str(self.final),
            "--basis",
            BASIS,
            "--allow-non-git-basis",
            "--owner",
        ]
        processes = [
            subprocess.Popen(
                [*base, owner],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            for owner in ("writer-a", "writer-b")
        ]
        results = [process.communicate(timeout=10) for process in processes]
        self.assertEqual(sorted(process.returncode for process in processes), [0, 3])
        winner_index = next(
            index for index, process in enumerate(processes) if process.returncode == 0
        )
        loser_index = 1 - winner_index
        first = json.loads(results[winner_index][0])
        self.assertIn("COLLISION", results[loser_index][1])
        self.assertTrue(Path(str(first["lease_path"])).is_file())
        self.assertTrue(Path(str(first["partial_path"])).is_file())

    def test_live_hash_drift_after_close_is_refused(self) -> None:
        opened = self.begin()
        partial = Path(str(opened["partial_path"]))
        partial.write_text(BODY, encoding="utf-8")
        closed = self.close(opened)
        frozen_hash = closed["source_sha256"]

        # Simulate a producer which retained a descriptor or deliberately
        # overrode the cooperative read-only close boundary.
        partial.chmod(0o600)
        with partial.open("ab") as handle:
            handle.write(b"late producer output\n")
        partial.chmod(0o400)
        self.assertNotEqual(
            frozen_hash, hashlib.sha256(partial.read_bytes()).hexdigest()
        )

        result = run(
            "finalize",
            "--final",
            str(self.final),
            "--token",
            str(opened["token"]),
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("changed after close", result.stderr)
        self.assertFalse(self.final.exists())
        self.assertFalse((self.root / "report.md.artifact.json").exists())

    def test_close_is_idempotent_after_close_record_commit(self) -> None:
        opened = self.begin()
        Path(str(opened["partial_path"])).write_text(BODY, encoding="utf-8")
        first = self.close(opened)
        second = self.close(opened)
        self.assertFalse(first["idempotent"])
        self.assertTrue(second["idempotent"])
        self.assertEqual(first["source_sha256"], second["source_sha256"])

    def test_final_only_interruption_recovers_idempotently(self) -> None:
        opened = self.begin()
        partial = Path(str(opened["partial_path"]))
        partial.write_text(BODY, encoding="utf-8")
        self.close(opened)
        stamped = subprocess.run(
            [
                sys.executable,
                str(TOOL.with_name("seal.py")),
                "stamp",
                str(partial),
                "--basis",
                BASIS,
            ],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=10,
        )
        self.assertEqual(stamped.returncode, 0, stamped.stderr)
        partial.chmod(0o444)
        os.link(partial, self.final)

        finished = self.finalize(opened)
        self.assertTrue(finished["recovered"])
        self.assertFalse(partial.exists())
        self.assertEqual(
            output_json(run("verify", "--final", str(self.final)))["status"],
            "VERIFIED",
        )

    def test_manifest_before_release_is_quarantined_then_recovers(self) -> None:
        opened = self.begin()
        Path(str(opened["partial_path"])).write_text(BODY, encoding="utf-8")
        self.close(opened)
        original_publish = TOOL_MODULE._publish_manifest_at

        def fail_release(parent_fd: int, name: str, data: bytes, target: str):
            if name.endswith("artifact-release.json"):
                raise TOOL_MODULE.ArtifactError("synthetic pre-release interruption")
            return original_publish(parent_fd, name, data, target)

        with mock.patch.object(
            TOOL_MODULE, "_publish_manifest_at", side_effect=fail_release
        ):
            with self.assertRaises(TOOL_MODULE.ArtifactError):
                TOOL_MODULE.finalize(self.final, str(opened["token"]))
        self.assertTrue(self.final.exists())
        self.assertTrue((self.root / "report.md.artifact.json").exists())
        quarantined = run("verify", "--final", str(self.final))
        self.assertNotEqual(quarantined.returncode, 0)
        self.assertIn("custody is not released", quarantined.stderr)

        finished = self.finalize(opened)
        self.assertTrue(finished["recovered"])
        self.assertEqual(
            output_json(run("verify", "--final", str(self.final)))["status"],
            "VERIFIED",
        )

    def test_release_before_cleanup_is_quarantined_then_recovers(self) -> None:
        opened = self.begin()
        Path(str(opened["partial_path"])).write_text(BODY, encoding="utf-8")
        self.close(opened)
        with mock.patch.object(
            TOOL_MODULE,
            "_finish_release",
            side_effect=TOOL_MODULE.ArtifactError("synthetic cleanup interruption"),
        ):
            with self.assertRaises(TOOL_MODULE.ArtifactError):
                TOOL_MODULE.finalize(self.final, str(opened["token"]))
        self.assertTrue((self.root / ".report.md.artifact-release.json").exists())
        quarantined = run("verify", "--final", str(self.final))
        self.assertNotEqual(quarantined.returncode, 0)
        self.assertIn("custody is not released", quarantined.stderr)

        finished = self.finalize(opened)
        self.assertTrue(finished["recovered"])
        self.assertFalse((self.root / ".report.md.artifact-release.json").exists())

    def test_metadata_link_interruptions_publish_final_mode_and_recover(self) -> None:
        for target_name in (
            "report.md.artifact.json",
            ".report.md.artifact-release.json",
        ):
            with self.subTest(target_name=target_name):
                nested = self.root / target_name.replace(".", "-")
                nested.mkdir()
                final = nested / "report.md"
                opened = output_json(
                    run(
                        "begin",
                        "--final",
                        str(final),
                        "--basis",
                        BASIS,
                        "--owner",
                        "fault-test",
                        "--allow-non-git-basis",
                    )
                )
                Path(str(opened["partial_path"])).write_text(BODY, encoding="utf-8")
                output_json(
                    run(
                        "close",
                        "--final",
                        str(final),
                        "--token",
                        str(opened["token"]),
                    )
                )
                real_link = os.link

                def link_then_interrupt(source: str, target: str, **kwargs: object):
                    result = real_link(source, target, **kwargs)
                    if target == target_name:
                        raise OSError("synthetic interruption after metadata link")
                    return result

                with mock.patch.object(
                    TOOL_MODULE, "_require_platform", return_value=None
                ), mock.patch.object(
                    TOOL_MODULE.os, "link", side_effect=link_then_interrupt
                ):
                    with self.assertRaises(TOOL_MODULE.ArtifactError):
                        TOOL_MODULE.finalize(final, str(opened["token"]))
                published_metadata = nested / target_name
                self.assertTrue(published_metadata.exists())
                self.assertEqual(
                    stat.S_IMODE(published_metadata.stat().st_mode), 0o444
                )
                recovered = output_json(
                    run(
                        "finalize",
                        "--final",
                        str(final),
                        "--token",
                        str(opened["token"]),
                    )
                )
                self.assertTrue(recovered["recovered"])
                self.assertEqual(
                    output_json(run("verify", "--final", str(final)))["status"],
                    "VERIFIED",
                )

    def test_finalize_after_completed_cleanup_is_idempotent(self) -> None:
        opened, first = self.complete()
        second = output_json(
            run(
                "finalize",
                "--final",
                str(self.final),
                "--token",
                str(opened["token"]),
            )
        )
        self.assertTrue(second["recovered"])
        self.assertEqual(second["full_sha256"], first["full_sha256"])
        self.assertEqual(second["manifest_sha256"], first["manifest_sha256"])

    def test_post_final_mutation_is_detected(self) -> None:
        _, finished = self.complete()
        self.final.chmod(0o600)
        with self.final.open("ab") as handle:
            handle.write(b"post-final drift\n")
        result = run("verify", "--final", str(self.final))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("INVALID", result.stderr)
        self.assertNotEqual(
            finished["full_sha256"],
            hashlib.sha256(self.final.read_bytes()).hexdigest(),
        )

    def test_mode_only_drift_is_detected(self) -> None:
        _, finished = self.complete()
        manifest = Path(str(finished["manifest_path"]))
        self.final.chmod(0o644)
        result = run("verify", "--final", str(self.final))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("mode changed", result.stderr)
        self.final.chmod(0o444)
        manifest.chmod(0o644)
        result = run("verify", "--final", str(self.final))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("mode changed", result.stderr)

    def test_matching_sealed_partial_can_resume_after_interruption(self) -> None:
        opened = self.begin()
        partial = Path(str(opened["partial_path"]))
        partial.write_text(BODY, encoding="utf-8")
        self.close(opened)
        stamped = subprocess.run(
            [
                sys.executable,
                str(TOOL.with_name("seal.py")),
                "stamp",
                str(partial),
                "--basis",
                BASIS,
            ],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=10,
        )
        self.assertEqual(stamped.returncode, 0, stamped.stderr)
        finished = self.finalize(opened)
        self.assertEqual(finished["status"], "FINAL")
        self.assertEqual(
            output_json(run("verify", "--final", str(self.final)))["status"],
            "VERIFIED",
        )

    def test_resume_rejects_noncanonical_post_seal_content(self) -> None:
        opened = self.begin()
        partial = Path(str(opened["partial_path"]))
        partial.write_text(BODY, encoding="utf-8")
        self.close(opened)
        stamped = subprocess.run(
            [
                sys.executable,
                str(TOOL.with_name("seal.py")),
                "stamp",
                str(partial),
                "--basis",
                BASIS,
            ],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=10,
        )
        self.assertEqual(stamped.returncode, 0, stamped.stderr)
        partial.chmod(0o600)
        with partial.open("ab") as handle:
            handle.write(b"UNAPPROVED POST-SEAL CONTENT\n")
        partial.chmod(0o400)
        result = run(
            "finalize",
            "--final",
            str(self.final),
            "--token",
            str(opened["token"]),
        )
        self.assertNotEqual(result.returncode, 0)
        # Post-seal tampering must be refused; either the canonical-seal
        # check or the stale-hash check may fire first, both fail closed.
        self.assertTrue(
            "not byte-for-byte canonical" in result.stderr
            or "refusing stale hash" in result.stderr,
            result.stderr,
        )
        self.assertFalse(self.final.exists())

    def test_wrong_token_and_preexisting_final_do_not_overwrite(self) -> None:
        opened = self.begin()
        partial = Path(str(opened["partial_path"]))
        partial.write_text(BODY, encoding="utf-8")
        wrong = run(
            "close", "--final", str(self.final), "--token", "not-the-token"
        )
        self.assertNotEqual(wrong.returncode, 0)
        self.assertIn("token mismatch", wrong.stderr)
        self.assertEqual(partial.read_text(encoding="utf-8"), BODY)

        other = self.root / "occupied.md"
        other.write_text("do not overwrite\n", encoding="utf-8")
        collision = run(
            "begin",
            "--final",
            str(other),
            "--basis",
            BASIS,
            "--owner",
            "test-lane",
            "--allow-non-git-basis",
        )
        self.assertEqual(collision.returncode, 3, collision.stderr)
        self.assertEqual(other.read_text(encoding="utf-8"), "do not overwrite\n")

    @unittest.skipUnless(shutil.which("git"), "Git required")
    def test_staged_mode_binds_current_bytes_to_index(self) -> None:
        subprocess.run(
            ["git", "init", "-q"], cwd=self.root, check=True, timeout=10
        )
        _, finished = self.complete()
        manifest = Path(str(finished["manifest_path"]))

        unstaged = run("verify", "--final", str(self.final), "--staged")
        self.assertNotEqual(unstaged.returncode, 0)
        self.assertIn("not staged", unstaged.stderr)

        subprocess.run(
            ["git", "add", "--", self.final.name, manifest.name],
            cwd=self.root,
            check=True,
            timeout=10,
        )
        staged = output_json(
            run("verify", "--final", str(self.final), "--staged")
        )
        self.assertEqual(len(staged["staged_blobs"]), 2)


if __name__ == "__main__":
    unittest.main()
