#!/usr/bin/env python3
import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


CASE_DIR = Path(__file__).resolve().parent
REPO = CASE_DIR.parents[1]
SOURCE = REPO / "APPROACHES.md"
COMPILER = CASE_DIR / "roundview.py"
HISTORICAL_COMMIT = "eaad172e59742ef8cfd055eace9bc6d3b2da8463"
HISTORICAL_SOURCE_SHA256 = (
    "27a208c58af3eb192bff51b2dc8f58cb9f6efcbd22816f88de6c9d428595a05b"
)

sys.path.insert(0, str(CASE_DIR))
import roundview  # noqa: E402


class RoundviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = SOURCE.read_bytes()
        cls.parsed = roundview.parse_source(cls.source)
        cls.rendered = roundview.render(cls.parsed, "APPROACHES.md")

    def _compile_subprocess(self, optimized=False):
        command = [sys.executable]
        if optimized:
            command.append("-O")
        command.extend(
            [
                str(COMPILER),
                "--source",
                "APPROACHES.md",
                "--source-label",
                "APPROACHES.md",
                "--stdout",
            ]
        )
        return subprocess.run(
            command,
            cwd=str(REPO),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )

    def assertGrammarFails(self, source, needle):
        with self.assertRaisesRegex(roundview.RoundviewError, needle):
            roundview.parse_source(source)

    def test_ordinary_and_optimized_are_byte_identical(self):
        ordinary = self._compile_subprocess(optimized=False)
        optimized = self._compile_subprocess(optimized=True)
        self.assertEqual(ordinary.returncode, 0, ordinary.stderr.decode())
        self.assertEqual(optimized.returncode, 0, optimized.stderr.decode())
        self.assertEqual(ordinary.stderr, b"")
        self.assertEqual(optimized.stderr, b"")
        self.assertEqual(ordinary.stdout, optimized.stdout)
        self.assertEqual(ordinary.stdout, self.rendered)

    def test_exact_source_slices_and_all_avenues_are_included(self):
        self.assertIn(self.parsed.preamble.data, self.rendered)
        self.assertIn(self.parsed.newest_overlay.data, self.rendered)
        self.assertIn(self.parsed.master_table.data, self.rendered)
        self.assertEqual(len(self.parsed.older_overlays), len(self.parsed.overlay_headings))
        self.assertEqual(
            [
                int(match.group(1))
                for line in self.parsed.master_table.data.decode("utf-8").splitlines()
                for match in [roundview.AVENUE_RE.match(line)]
                if match is not None
            ],
            list(range(1, 47)),
        )
        roundview.verify_output_seal(self.rendered)

    def test_output_is_under_fifteen_percent_of_source(self):
        ratio = len(self.rendered) / len(self.source)
        self.assertLess(ratio, 0.15, "ROUNDVIEW ratio was {:.3%}".format(ratio))

    def test_missing_newest_overlay_fails_closed(self):
        mutated = self.source.replace(
            b"## Superseding strategy overlay (",
            b"## Strategy snapshot (",
            1,
        )
        self.assertGrammarFails(mutated, "first level-two section")

    def test_duplicate_overlay_heading_fails_closed(self):
        first = self.source.splitlines(keepends=True)[self.parsed.newest_overlay.start]
        mutated = self.source.replace(first, first + first, 1)
        self.assertGrammarFails(mutated, "duplicate overlay heading")

    def test_missing_avenue_fails_closed(self):
        target = next(
            line
            for line in self.source.splitlines(keepends=True)
            if line.startswith(b"| 23 |")
        )
        mutated = self.source.replace(target, b"", 1)
        self.assertGrammarFails(mutated, "avenue rows must be exactly 1..46")

    def test_duplicate_avenue_fails_closed(self):
        target = next(
            line
            for line in self.source.splitlines(keepends=True)
            if line.startswith(b"| 23 |")
        )
        mutated = self.source.replace(target, target + target, 1)
        self.assertGrammarFails(mutated, "avenue rows must be exactly 1..46")

    def test_expected_source_hash_and_output_drift_fail_closed(self):
        with self.assertRaisesRegex(roundview.RoundviewError, "source SHA-256 mismatch"):
            roundview.compile_source(SOURCE, "APPROACHES.md", "0" * 64)

        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "roundview.md"
            output.write_bytes(self.rendered)
            data = bytearray(output.read_bytes())
            data[data.index(b"GENERATED_NON_AUTHORITATIVE")] ^= 1
            output.write_bytes(bytes(data))
            result = subprocess.run(
                [
                    sys.executable,
                    str(COMPILER),
                    "--source",
                    "APPROACHES.md",
                    "--source-label",
                    "APPROACHES.md",
                    "--check",
                    str(output),
                ],
                cwd=str(REPO),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
            )
            self.assertEqual(result.returncode, 2)
            self.assertIn(b"hash drift", result.stderr)

            # A differently rendered file can carry a valid internal seal and
            # must still fail the fresh byte-for-byte compilation check.
            output.write_bytes(roundview.render(self.parsed, "WRONG-LABEL"))
            result = subprocess.run(
                [
                    sys.executable,
                    str(COMPILER),
                    "--source",
                    "APPROACHES.md",
                    "--source-label",
                    "APPROACHES.md",
                    "--check",
                    str(output),
                ],
                cwd=str(REPO),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
            )
            self.assertEqual(result.returncode, 2)
            self.assertIn(b"output hash drift", result.stderr)

    def test_source_fingerprint_change_during_read_fails_closed(self):
        original = roundview._fingerprint
        calls = {"count": 0}

        def simulated_mutation(stat_result):
            calls["count"] += 1
            fingerprint = original(stat_result)
            if calls["count"] == 3:
                return fingerprint[:-1] + (fingerprint[-1] + 1,)
            return fingerprint

        with mock.patch.object(roundview, "_fingerprint", side_effect=simulated_mutation):
            with self.assertRaisesRegex(roundview.RoundviewError, "mutation detected"):
                roundview.read_stable_file(SOURCE)

    def test_20260829T0820Z_basis_backtest(self):
        result = subprocess.run(
            ["git", "show", "{}:APPROACHES.md".format(HISTORICAL_COMMIT)],
            cwd=str(REPO),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        if result.returncode != 0:
            self.skipTest("historical basis commit is unavailable")
        historical = result.stdout
        self.assertEqual(hashlib.sha256(historical).hexdigest(), HISTORICAL_SOURCE_SHA256)
        state_packet = REPO / "xmodel" / "ideation-20260829T0820Z-state-packet.md"
        if not state_packet.exists():
            self.skipTest("0820Z state packet is unavailable")
        self.assertIn(
            "{}  APPROACHES.md".format(HISTORICAL_SOURCE_SHA256),
            state_packet.read_text(encoding="utf-8"),
        )

        parsed = roundview.parse_source(historical)
        self.assertTrue(
            parsed.newest_overlay.data.startswith(
                b"## Superseding strategy overlay (2026-08-29 08:04Z"
            )
        )
        rendered = roundview.render(
            parsed, "{}:APPROACHES.md".format(HISTORICAL_COMMIT)
        )
        roundview.verify_output_seal(rendered)
        self.assertLess(len(rendered) / len(historical), 0.15)


if __name__ == "__main__":
    unittest.main()
