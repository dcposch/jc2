#!/usr/bin/env python3
"""Focused regression tests for the OPEN/banked collision hook."""

from __future__ import annotations

from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest


TOOL = Path(__file__).with_name("open_collision.py")


class OpenCollisionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        (self.root / "xmodel").mkdir()
        for name in ("AUDIT.md", "notes.md", "APPROACHES.md",
                     "history/APPROACHES-through-20260915.md"):
            (self.root / name).parent.mkdir(parents=True, exist_ok=True)
            (self.root / name).write_text("banked control\n", encoding="utf-8")

    def run_tool(self, report_text: str) -> subprocess.CompletedProcess[str]:
        report = self.root / "report.md"
        report.write_text(report_text, encoding="utf-8")
        return subprocess.run(
            [sys.executable, str(TOOL), str(report), "--root", str(self.root)],
            text=True,
            capture_output=True,
            timeout=10,
            check=False,
        )

    def test_deg_af_retroactive_case_surfaces_all_three_banked_lines(self) -> None:
        """Reproduce the coordinator's 2026-09-02 smallest useful test."""

        # Exact source lines and positions from
        # xmodel/companion-curve-alln-opus5-20260902.md:677,685,783,785,833,836.
        lines = ["banked filler"] * 836
        lines[676] = (
            "3. A new one, typed here: even given a representation and a source, "
            "`A_F` must be"
        )
        lines[684] = (
            "`sum_i k_i m_i <= K` and `sum_i deg D_i <= max(deg P, deg Q)`. "
            "Nothing is bounded"
        )
        lines[782] = (
            "**OPENs opened.** `OPEN[COMPANION-R0-REALISATION]`: `A_F` must be "
            "the zero set of"
        )
        lines[784] = (
            "`M <= K = deg P/d`, i.e. `sum_i deg D_i <= max(deg P, deg Q)`. "
            "This is the exact"
        )
        lines[832] = (
            "*Raw remainder degree / variable-ring map.* Every degree statement "
            "about `A_F` is"
        )
        lines[835] = (
            "`sum_i deg D_i <= max(deg P, deg Q)`, is flagged as gauge-dependent "
            "on the `x,y`"
        )
        fixture = self.root / "xmodel" / "companion-curve-alln-opus5-20260902.md"
        fixture.write_text("\n".join(lines) + "\n", encoding="utf-8")

        result = self.run_tool(
            "OPENS RAISED      OPEN[DEG-AF-VS-N]  bounded quantity: "
            "sum_i deg D_i <= max(deg P, deg Q)\n"
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("## COLLISIONS\n", result.stdout)
        self.assertIn("status: CANDIDATES", result.stdout)
        positions = re.findall(
            r"companion-curve-alln-opus5-20260902\.md:(\d+)", result.stdout
        )
        self.assertEqual(positions, ["685", "785", "836"])

    def test_no_candidate_emits_explicit_empty_collisions_block(self) -> None:
        (self.root / "xmodel" / "unrelated.md").write_text(
            "The ordinary degree satisfies d <= 12.\n", encoding="utf-8"
        )
        result = self.run_tool(
            "**OPENs raised.**\n\n"
            "* `OPEN[QUASIFOAM-MERIDIAN-COUNT]` — bound the quasifoam "
            "meridian count.\n"
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("## COLLISIONS\n\nstatus: EMPTY", result.stdout)
        self.assertIn("`OPEN[QUASIFOAM-MERIDIAN-COUNT]` (report:3): NONE", result.stdout)

    def test_archived_strategy_remains_in_the_collision_corpus(self) -> None:
        (self.root / "xmodel" / "bank.md").write_text("unrelated banked work\n")
        archive = self.root / "history/APPROACHES-through-20260915.md"
        archive.write_text("The quasifoam meridian count is bounded by the degree.\n")
        result = self.run_tool(
            "OPENS RAISED      OPEN[QUASIFOAM-MERIDIAN-COUNT] "
            "bound the quasifoam meridian count in terms of the degree.\n"
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("history/APPROACHES-through-20260915.md:1", result.stdout)

    def test_missing_required_bank_file_fails_closed_with_a_block(self) -> None:
        (self.root / "xmodel" / "bank.md").write_text("x <= y\n", encoding="utf-8")
        (self.root / "APPROACHES.md").unlink()
        result = self.run_tool("No OPEN is raised by this report.\n")
        self.assertEqual(result.returncode, 2)
        self.assertIn("## COLLISIONS\n\nstatus: ERROR", result.stdout)
        self.assertIn("APPROACHES.md", result.stdout)

    def test_multiple_same_line_raised_opens_are_all_checked(self) -> None:
        (self.root / "xmodel" / "bank.md").write_text(
            "unrelated rank <= 4\n", encoding="utf-8"
        )
        result = self.run_tool(
            "OPENS RAISED "
            "OPEN[FIRST-ALPHA] bound alpha_count <= 1; "
            "OPEN[SECOND-BETA] bound beta_count <= 2\n"
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("`OPEN[FIRST-ALPHA]` (report:1): NONE", result.stdout)
        self.assertIn("`OPEN[SECOND-BETA]` (report:1): NONE", result.stdout)

    def test_malformed_open_in_raised_section_fails_closed(self) -> None:
        (self.root / "xmodel" / "bank.md").write_text("x <= y\n", encoding="utf-8")
        result = self.run_tool("OPENS RAISED\n- OPEN[MALFORMED\n")
        self.assertEqual(result.returncode, 2)
        self.assertIn("status: ERROR", result.stdout)
        self.assertIn("malformed OPEN token", result.stdout)

    def test_bound_inside_identifier_is_not_a_quantity_description(self) -> None:
        (self.root / "xmodel" / "bank.md").write_text("x <= y\n", encoding="utf-8")
        result = self.run_tool(
            "OPENS RAISED OPEN[A2-DEPTH-BOUND] "
            "(replaces OPEN[A2-U-BOUND])\n"
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn("status: ERROR", result.stdout)
        self.assertIn("lacks an explicit bounded-quantity description", result.stdout)

    def test_prose_about_prior_raised_opens_does_not_activate_a_scan(self) -> None:
        (self.root / "xmodel" / "bank.md").write_text(
            "sum_i deg D_i <= max(deg P, deg Q)\n", encoding="utf-8"
        )
        result = self.run_tool(
            "Run this retroactively over the OPENs raised on 2026-09-02.\n"
            "PASS iff it surfaces OPEN[DEG-AF-VS-N].\n"
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("status: EMPTY", result.stdout)
        self.assertIn("report contains no explicitly raised", result.stdout)

    def test_candidate_fanout_is_bounded_and_fails_closed(self) -> None:
        rows = ["alpha meridian count <= limit"] * 101
        (self.root / "xmodel" / "bank.md").write_text(
            "\n".join(rows) + "\n", encoding="utf-8"
        )
        result = self.run_tool(
            "OPENS RAISED OPEN[ALPHA-MERIDIAN-COUNT] "
            "bound alpha meridian count <= limit\n"
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn("status: ERROR", result.stdout)
        self.assertIn("more than 100 candidates", result.stdout)

    def test_banked_relation_with_open_label_remains_a_candidate(self) -> None:
        (self.root / "xmodel" / "bank.md").write_text(
            "OPEN[OLDER-ALPHA] alpha meridian count <= limit\n",
            encoding="utf-8",
        )
        result = self.run_tool(
            "OPENS RAISED OPEN[ALPHA-MERIDIAN-COUNT] "
            "bound alpha meridian count <= limit\n"
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("status: CANDIDATES", result.stdout)
        self.assertIn("`xmodel/bank.md:1`", result.stdout)

    def test_bold_and_heading_entries_are_not_mistaken_for_boundaries(self) -> None:
        (self.root / "xmodel" / "bank.md").write_text(
            "alpha meridian count <= limit\n"
            "beta orbit count <= ceiling\n",
            encoding="utf-8",
        )
        result = self.run_tool(
            "**OPENs raised.**\n\n"
            "**OPEN[ALPHA-MERIDIAN-COUNT]** — bound alpha meridian count.\n"
            "### OPEN[BETA-ORBIT-COUNT] — bound beta orbit count.\n"
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("### OPEN[ALPHA-MERIDIAN-COUNT]", result.stdout)
        self.assertIn("### OPEN[BETA-ORBIT-COUNT]", result.stdout)

    def test_latex_inequality_is_scanned_as_a_bounded_relation(self) -> None:
        (self.root / "xmodel" / "bank.md").write_text(
            r"alpha meridian count \leq limit" + "\n",
            encoding="utf-8",
        )
        result = self.run_tool(
            "OPENS RAISED OPEN[ALPHA-MERIDIAN-COUNT] "
            "bound alpha meridian count <= limit\n"
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("status: CANDIDATES", result.stdout)
        self.assertIn("`xmodel/bank.md:1`", result.stdout)


if __name__ == "__main__":
    unittest.main()
