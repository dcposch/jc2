#!/usr/bin/env python3
"""Focused regression tests for the OPEN/banked collision hook."""

from __future__ import annotations

from pathlib import Path
import importlib.util
import io
import re
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout, redirect_stderr
from unittest.mock import patch


TOOL = Path(__file__).with_name("open_collision.py")
SPEC = importlib.util.spec_from_file_location("collision_under_test", TOOL)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


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


class FrozenCorpusTests(unittest.TestCase):
    """Adversarial Git-only fixtures, separate from the unchanged default tests."""

    setUp = OpenCollisionTests.setUp
    run_tool = OpenCollisionTests.run_tool

    QUESTION = "OPENS RAISED OPEN[ALPHA-MERIDIAN-COUNT] bound alpha meridian count\n"
    CANDIDATE = "alpha meridian count <= limit\n"

    def git(self, *args: str) -> str:
        result = subprocess.run(
            ["git", "-c", "core.hooksPath=/dev/null", "-c", "commit.gpgsign=false",
             "-c", "user.name=Collision Test", "-c", "user.email=test@example.invalid",
             "-C", str(self.root), *args],
            capture_output=True, text=True, timeout=10, check=True,
        )
        return result.stdout.strip()

    def commit_fixture(self) -> str:
        self.git("init", "-q")
        self.git("add", ".")
        self.git("commit", "-qm", "fixture")
        return self.git("rev-parse", "HEAD")

    def fixture(self) -> str:
        (self.root / "xmodel/bank.md").write_text(self.CANDIDATE)
        return self.commit_fixture()

    def frozen(self, basis: str, report: Path | None = None) -> subprocess.CompletedProcess[str]:
        if report is None:
            report = self.root / "report.md"
            report.write_text(self.QUESTION)
        return subprocess.run(
            [sys.executable, str(TOOL), str(report), "--root", str(self.root),
             f"--basis={basis}"], text=True, capture_output=True, timeout=10,
            check=False,
        )

    def test_frozen_matches_default_and_reports_exact_basis(self) -> None:
        basis = self.fixture()
        default = self.run_tool(self.QUESTION)
        frozen = self.frozen(basis)
        self.assertEqual(frozen.returncode, 0, frozen.stderr)
        self.assertEqual(frozen.stdout, default.stdout +
                         f"\nCorpus basis: `{basis}` (Git blobs only).\n")

    def test_no_working_corpus_or_receipt_reads(self) -> None:
        basis = self.fixture()
        report = self.root / "report.md"
        report.write_text(self.QUESTION)
        original_read = Path.read_text

        def input_only(path, *args, **kwargs):
            self.assertEqual(path, report, "working corpus/receipt read attempted")
            return original_read(path, *args, **kwargs)

        out, err = io.StringIO(), io.StringIO()
        with patch.object(Path, "read_text", input_only), \
                patch.object(Path, "glob", side_effect=AssertionError("working glob")), \
                redirect_stdout(out), redirect_stderr(err):
            status = MODULE.main([str(report), "--root", str(self.root), "--basis", basis])
        self.assertEqual(status, 0, err.getvalue())
        self.assertIn("`xmodel/bank.md:1`", out.getvalue())

    def test_missing_dirty_and_untracked_working_corpus_do_not_matter(self) -> None:
        basis = self.fixture()
        (self.root / "xmodel/bank.md").write_bytes(b"\xff")
        (self.root / "xmodel/bank.run.v2").write_text("live receipt without final status")
        (self.root / "xmodel/untracked.md").write_text(self.CANDIDATE)
        for name in MODULE.REQUIRED_TOP_LEVEL:
            (self.root / name).unlink()
        result = self.frozen(basis)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("`xmodel/bank.md:1`", result.stdout)
        self.assertNotIn("untracked.md:", result.stdout)
        (self.root / "xmodel").rename(self.root / "unavailable-xmodel")
        result = self.frozen(basis)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("`xmodel/bank.md:1`", result.stdout)

    def test_bad_missing_and_noncommit_bases_fail_without_fallback(self) -> None:
        basis = self.fixture()
        for value in ("HEAD", basis[:12], "0" * 40, "--all", "", basis.upper(),
                      self.git("rev-parse", "HEAD:xmodel/bank.md"),
                      self.git("rev-parse", "HEAD^{tree}")):
            with self.subTest(basis=value):
                result = self.frozen(value)
                self.assertEqual(result.returncode, 2, result.stderr)
                self.assertIn("status: ERROR", result.stdout)
                self.assertNotIn("status: CANDIDATES", result.stdout)
                self.assertNotIn("Corpus basis:", result.stdout)

    def test_missing_required_committed_file_fails_despite_working_replacement(self) -> None:
        (self.root / "xmodel/bank.md").write_text(self.CANDIDATE)
        (self.root / "history/APPROACHES-through-20260915.md").unlink()
        basis = self.commit_fixture()
        (self.root / "history/APPROACHES-through-20260915.md").write_text("replacement")
        result = self.frozen(basis)
        self.assertEqual(result.returncode, 2)
        self.assertIn("required frozen corpus file missing", result.stdout)

    def test_symlink_and_gitlink_modes_fail_closed(self) -> None:
        basis = self.fixture()
        for name in ("xmodel/bank.md", "notes.md"):
            path = self.root / name
            old = path.read_text()
            path.unlink()
            path.symlink_to("APPROACHES.md")
            current = self.commit_fixture()
            result = self.frozen(current)
            self.assertEqual(result.returncode, 2)
            self.assertIn("not a regular file", result.stdout)
            path.unlink()
            path.write_text(old)
        self.git("update-index", "--add", "--cacheinfo", f"160000,{basis},xmodel/bank.md")
        self.git("commit", "-qm", "gitlink fixture")
        result = self.frozen(self.git("rev-parse", "HEAD"))
        self.assertEqual(result.returncode, 2)
        self.assertIn("not a regular file", result.stdout)

    def test_self_blind_round_and_frozen_receipt_guards(self) -> None:
        for name in ("bank", "unfinished", "ideation-20260922T0100Z-peer",
                     "ideation-20260922T0100Z-author", "ideation-20260922T0100Z-packet"):
            (self.root / f"xmodel/{name}.md").write_text(self.CANDIDATE)
        (self.root / "xmodel/unfinished.run.v2").write_text("status=RUNNING\n")
        (self.root / "xmodel/bank.run.v2").write_text("final_status=DONE\n")
        basis = self.commit_fixture()
        report = self.root / "xmodel/ideation-20260922T0100Z-author.md"
        report.write_text(self.QUESTION)
        result = self.frozen(basis, report)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("`xmodel/bank.md:1`", result.stdout)
        self.assertIn("ideation-20260922T0100Z-packet.md:1", result.stdout)
        for name in ("unfinished.md:", "0100Z-peer.md:", "0100Z-author.md:"):
            self.assertNotIn(name, result.stdout)
        report = self.root / "xmodel/bank.md"
        report.write_text(self.QUESTION)
        result = self.frozen(basis, report)
        self.assertNotIn("`xmodel/bank.md:", result.stdout)

    def test_archive_blob_is_used_and_git_replacements_are_ignored(self) -> None:
        basis = self.fixture()
        (self.root / "xmodel/bank.md").write_text("unrelated\n")
        (self.root / "history/APPROACHES-through-20260915.md").write_text(self.CANDIDATE)
        next_basis = self.commit_fixture()
        self.git("replace", basis, next_basis)
        old = self.frozen(basis)
        new = self.frozen(next_basis)
        self.assertEqual(old.returncode, 0, old.stderr)
        self.assertEqual(new.returncode, 0, new.stderr)
        self.assertIn("`xmodel/bank.md:1`", old.stdout)
        self.assertNotIn("history/APPROACHES-through-20260915.md:1", old.stdout)
        self.assertIn("history/APPROACHES-through-20260915.md:1", new.stdout)

    def test_non_utf8_committed_body_fails_closed(self) -> None:
        (self.root / "xmodel/bank.md").write_bytes(b"\xff")
        result = self.frozen(self.commit_fixture())
        self.assertEqual(result.returncode, 2)
        self.assertIn("cannot decode frozen corpus file", result.stdout)

    def test_no_working_tree_fallback_outside_git(self) -> None:
        (self.root / "xmodel/bank.md").write_text(self.CANDIDATE)
        result = self.frozen("0" * 40)
        self.assertEqual(result.returncode, 2)
        self.assertIn("status: ERROR", result.stdout)

    def test_incomplete_or_wrong_type_xmodel_tree_fails_closed(self) -> None:
        for shape in ("empty", "symlink", "gitlink"):
            with self.subTest(shape=shape):
                basis = self.fixture()
                self.git("rm", "-q", "xmodel/bank.md")
                if shape == "symlink":
                    path = self.root / "xmodel"
                    if path.exists():
                        path.rmdir()
                    path.symlink_to("history", target_is_directory=True)
                    self.git("add", "xmodel")
                elif shape == "gitlink":
                    self.git("update-index", "--add", "--cacheinfo",
                             f"160000,{basis},xmodel")
                self.git("commit", "-qm", shape)
                result = self.frozen(self.git("rev-parse", "HEAD"))
                self.assertEqual(result.returncode, 2)
                self.assertIn("no regular xmodel tree", result.stdout)
                # Each subtest has an isolated repository; never clean the real repo.
                self.setUp()

    def test_external_input_and_repository_root_validation(self) -> None:
        basis = self.fixture()
        with tempfile.TemporaryDirectory() as outside:
            report = Path(outside) / "input.md"
            report.write_text(self.QUESTION)
            result = self.frozen(basis, report)
            self.assertEqual(result.returncode, 0, result.stderr)
            result = subprocess.run(
                [sys.executable, str(TOOL), str(report), "--root",
                 str(self.root / "xmodel"), "--basis", basis],
                text=True, capture_output=True, timeout=10, check=False,
            )
            self.assertEqual(result.returncode, 2)
            self.assertIn("repository top level", result.stdout)

    def test_invalid_frozen_receipt_fails_closed(self) -> None:
        self.fixture()
        (self.root / "xmodel/bank.run.v2").symlink_to("bank.md")
        result = self.frozen(self.commit_fixture())
        self.assertEqual(result.returncode, 2)
        self.assertIn("not a regular file: xmodel/bank.run.v2", result.stdout)

    def test_frozen_fanout_error_has_no_partial_candidates(self) -> None:
        (self.root / "xmodel/bank.md").write_text(self.CANDIDATE * 101)
        result = self.frozen(self.commit_fixture())
        self.assertEqual(result.returncode, 2)
        self.assertIn("more than 100 candidates", result.stdout)
        self.assertNotIn("status: CANDIDATES", result.stdout)
        self.assertNotIn("Corpus basis:", result.stdout)

    def test_empty_question_set_still_validates_frozen_corpus(self) -> None:
        basis = self.fixture()
        report = self.root / "report.md"
        report.write_text("No new questions.\n")
        valid = self.frozen(basis, report)
        invalid = self.frozen("0" * 40, report)
        self.assertEqual(valid.returncode, 0, valid.stderr)
        self.assertIn("status: EMPTY", valid.stdout)
        self.assertIn(basis, valid.stdout)
        self.assertEqual(invalid.returncode, 2)
        self.assertIn("status: ERROR", invalid.stdout)


if __name__ == "__main__":
    unittest.main()
