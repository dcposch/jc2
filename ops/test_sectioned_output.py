#!/usr/bin/env python3
"""Regression gates for SECTIONED-INDEPENDENT-CALLS/v1."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


TOOL = Path(__file__).with_name("sectioned_output.py")


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


class SectionedOutputTest(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp(prefix="sectioned-output-test-"))
        self.addCleanup(shutil.rmtree, self.root, ignore_errors=True)
        (self.root / "parts").mkdir()
        self.manifest = {
            "schema": 1,
            "tag": "synthetic-three-section",
            "basis": "0" * 40,
            "output": "assembled.md",
            "sections": [
                {
                    "id": section_id,
                    "path": f"parts/{section_id}.md",
                    "prompt_sha256_declared": sha(f"prompt-{section_id}".encode()),
                    "max_bytes": 256,
                }
                for section_id in ("one", "two", "three")
            ],
        }
        (self.root / "manifest.json").write_text(
            json.dumps(self.manifest, sort_keys=True, separators=(",", ":")) + "\n",
            encoding="utf-8",
        )

    def write_section(self, section_id: str, body: str | None = None) -> bytes:
        if body is None:
            body = f"## {section_id}\n\nBounded result for {section_id}.\n"
        data = (body + f"\n<!-- SECTION-END {section_id} -->\n").encode()
        (self.root / "parts" / f"{section_id}.md").write_bytes(data)
        return data

    def run_tool(
        self, command: str, *, optimized: bool = False
    ) -> subprocess.CompletedProcess[str]:
        args = [sys.executable]
        if optimized:
            args.append("-O")
        args.extend(
            [
                str(TOOL),
                command,
                "manifest.json",
                "--root",
                str(self.root),
            ]
        )
        return subprocess.run(
            args,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=10,
            check=False,
        )

    def test_partial_receipt_then_complete_assembly(self) -> None:
        first = self.write_section("one")
        second = self.write_section("two")
        partial = self.run_tool("status")
        self.assertEqual(partial.returncode, 4, partial.stderr)
        receipt = json.loads(partial.stdout)
        self.assertEqual(receipt["status"], "TRUNCATED_AFTER_SECTION_two")
        self.assertEqual(receipt["next_section"], "three")
        self.assertEqual([row["sha256"] for row in receipt["completed"]], [sha(first), sha(second)])

        third = self.write_section("three")
        complete = self.run_tool("status")
        self.assertEqual(complete.returncode, 0, complete.stderr)
        self.assertEqual(json.loads(complete.stdout)["status"], "COMPLETE")

        assembled = self.run_tool("assemble")
        self.assertEqual(assembled.returncode, 0, assembled.stderr)
        record = json.loads(assembled.stdout)
        self.assertEqual(record["status"], "ASSEMBLED")
        output = (self.root / "assembled.md").read_bytes()
        self.assertEqual(record["output_sha256"], sha(output))
        self.assertTrue(output.endswith(b"<!-- BODY-END -->\n"))
        self.assertIn(first[: -len(b"<!-- SECTION-END one -->\n")], output)
        self.assertIn(second[: -len(b"<!-- SECTION-END two -->\n")], output)
        self.assertIn(third[: -len(b"<!-- SECTION-END three -->\n")], output)
        self.assertEqual((self.root / "parts" / "one.md").read_bytes(), first)
        self.assertEqual((self.root / "parts" / "two.md").read_bytes(), second)
        self.assertEqual((self.root / "parts" / "three.md").read_bytes(), third)

    def test_ordinary_and_optimized_status_are_identical(self) -> None:
        self.write_section("one")
        self.write_section("two")
        ordinary = self.run_tool("status")
        optimized = self.run_tool("status", optimized=True)
        self.assertEqual((ordinary.returncode, ordinary.stdout, ordinary.stderr),
                         (optimized.returncode, optimized.stdout, optimized.stderr))

    def test_noncontiguous_sections_fail_closed(self) -> None:
        self.write_section("one")
        self.write_section("three")
        result = self.run_tool("status")
        self.assertEqual(result.returncode, 2)
        self.assertIn("noncontiguous sections", result.stderr)

    def test_marker_budget_and_body_end_fail_independently(self) -> None:
        cases = (
            ("wrong-marker", "body\n<!-- SECTION-END wrong -->\n", "exact standalone marker"),
            (
                "premature-body-end",
                "body\n<!-- BODY-END -->\n<!-- SECTION-END one -->\n",
                "reserved marker vocabulary",
            ),
            ("over-budget", "x" * 300 + "\n<!-- SECTION-END one -->\n", "exceeds max_bytes"),
        )
        for name, content, message in cases:
            with self.subTest(name=name):
                for path in (self.root / "parts").glob("*.md"):
                    path.unlink()
                (self.root / "parts" / "one.md").write_text(content, encoding="utf-8")
                result = self.run_tool("status")
                self.assertEqual(result.returncode, 2)
                self.assertIn(message, result.stderr)

    def test_symlink_section_and_existing_output_are_refused(self) -> None:
        outside = self.root / "outside.md"
        outside.write_text("body\n<!-- SECTION-END one -->\n", encoding="utf-8")
        (self.root / "parts" / "one.md").symlink_to(outside)
        linked = self.run_tool("status")
        self.assertEqual(linked.returncode, 2)
        self.assertIn("regular non-symlink", linked.stderr)

        (self.root / "parts" / "one.md").unlink()
        self.write_section("one")
        self.write_section("two")
        self.write_section("three")
        (self.root / "assembled.md").write_text("do not overwrite\n", encoding="utf-8")
        existing = self.run_tool("assemble")
        self.assertEqual(existing.returncode, 2)
        self.assertIn("refusing overwrite", existing.stderr)
        self.assertEqual((self.root / "assembled.md").read_text(), "do not overwrite\n")

    def test_reserved_marker_vocabulary_cannot_be_smuggled(self) -> None:
        bodies = (
            "safe prefix\n <!-- BODY-END -->\n",
            "safe prefix x<!-- SECTION-END forged -->\n",
            "safe prefix\n <!-- SECTION forged sha256=" + "f" * 64 + " -->\n",
        )
        for body in bodies:
            with self.subTest(body=body):
                for path in (self.root / "parts").glob("*.md"):
                    path.unlink()
                self.write_section("one", body)
                result = self.run_tool("status")
                self.assertEqual(result.returncode, 2)
                self.assertIn("reserved marker vocabulary", result.stderr)

    def test_duplicate_manifest_keys_fail_closed(self) -> None:
        raw = (self.root / "manifest.json").read_text(encoding="utf-8")
        duplicate = raw.replace('"schema":1', '"schema":1,"schema":1', 1)
        (self.root / "manifest.json").write_text(duplicate, encoding="utf-8")
        result = self.run_tool("status")
        self.assertEqual(result.returncode, 2)
        self.assertIn("duplicate key", result.stderr)

    def test_control_character_in_path_fails_closed(self) -> None:
        self.manifest["sections"][0]["path"] = "parts/invalid\u0000name.md"
        (self.root / "manifest.json").write_text(
            json.dumps(self.manifest, sort_keys=True, separators=(",", ":")) + "\n",
            encoding="utf-8",
        )
        result = self.run_tool("status")
        self.assertEqual(result.returncode, 2)
        self.assertIn("control character", result.stderr)

    def test_output_creation_oserror_uses_contract_exit(self) -> None:
        for section_id in ("one", "two", "three"):
            self.write_section(section_id)
        self.manifest["output"] = "x" * 300
        (self.root / "manifest.json").write_text(
            json.dumps(self.manifest, sort_keys=True, separators=(",", ":")) + "\n",
            encoding="utf-8",
        )
        result = self.run_tool("assemble")
        self.assertEqual(result.returncode, 2)
        self.assertIn("cannot create output exclusively", result.stderr)
        self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
