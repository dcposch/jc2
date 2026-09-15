#!/usr/bin/env python3
"""Focused regression for versioned fallacy delivery and charge declarations."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


OPS = Path(__file__).resolve().parent
ROOT = OPS.parent
SOURCE_APPENDIX = ROOT / "FALLACY-v2.md"
LEGACY_APPENDIX = ROOT / "FALLACY.md"
SOURCE_LANE = OPS / "lane.sh"
SOURCE_VALIDATOR = OPS / "validate_charge_basis.py"
SOURCE_SEAL = OPS / "seal.py"
COPY_SOURCE = object()


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def parse_run(path: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        key, value = line.split("=", 1)
        result[key] = value
    return result


class LaneHarness(unittest.TestCase):
    def make_repo(self, appendix: object = COPY_SOURCE) -> Path:
        root = Path(tempfile.mkdtemp(prefix="lane-fallacy-test-"))
        self.addCleanup(shutil.rmtree, root, ignore_errors=True)
        adapters = root / "ops" / "adapters"
        adapters.mkdir(parents=True)
        shutil.copy2(SOURCE_LANE, root / "ops" / "lane.sh")
        shutil.copy2(SOURCE_VALIDATOR, root / "ops" / "validate_charge_basis.py")
        shutil.copy2(SOURCE_SEAL, root / "ops" / "seal.py")
        (root / "ops" / "lane.sh").chmod(0o755)
        if appendix is COPY_SOURCE:
            shutil.copy2(SOURCE_APPENDIX, root / "FALLACY-v2.md")
        elif appendix is not None:
            assert isinstance(appendix, bytes)
            (root / "FALLACY-v2.md").write_bytes(appendix)

        adapter = adapters / "fake.sh"
        adapter.write_text(
            """#!/bin/sh
set -eu
: "${FAKE_CAPTURE:?}"
: "${FAKE_PROMPT_PATH:?}"
: "${FAKE_TAG:?}"
cp "$1" "$FAKE_CAPTURE"
printf '%s\n' "$1" > "$FAKE_PROMPT_PATH"
if [ "${FAKE_MODE:-}" = mutate_appendix ]; then
  printf '\nmutation during adapter run\n' >> FALLACY-v2.md
fi
if [ "${FAKE_MODE:-}" = probe_custody ]; then
  if chmod 600 "$1" 2>/dev/null && printf '\nmodel-side mutation\n' >> "$1" 2>/dev/null; then
    printf 'ALLOWED\n' > "$FAKE_BOUNDARY_RESULT"
  else
    printf 'DENIED\n' > "$FAKE_BOUNDARY_RESULT"
  fi
fi
if [ "${FAKE_MODE:-}" = probe_excluded ]; then
  direct_read=DENIED
  alias_read=DENIED
  direct_write=DENIED
  alias_write=DENIED
  if value=$(cat "$FAKE_EXCLUDED_TREE/secret.txt" 2>/dev/null); then
    direct_read="ALLOWED:$value"
  fi
  if value=$(cat "$FAKE_EXCLUDED_ALIAS/secret.txt" 2>/dev/null); then
    alias_read="ALLOWED:$value"
  fi
  if printf 'model write\n' > "$FAKE_EXCLUDED_TREE/direct-write.txt" 2>/dev/null; then
    direct_write=ALLOWED
  fi
  if printf 'model write\n' > "$FAKE_EXCLUDED_ALIAS/alias-write.txt" 2>/dev/null; then
    alias_write=ALLOWED
  fi
  printf '%s\n' "$direct_read" "$alias_read" "$direct_write" "$alias_write" \
    > "$FAKE_BOUNDARY_RESULT"
fi
if [ "${FAKE_MODE:-}" = mutate_then_read_input ]; then
  printf '\nrepo drift after launch\n' >> "$FAKE_CHARGED_INPUT"
  snap=$(grep -o '/[^ ]*/inputs/packet.md' "$1" | head -1)
  if [ -n "$snap" ] && cat "$snap" > "$FAKE_BOUNDARY_RESULT" 2>/dev/null; then
    :
  else
    printf 'READ-FAILED\n' > "$FAKE_BOUNDARY_RESULT"
  fi
fi
if [ "${FAKE_MODE:-}" = probe_receipt ]; then
  if printf 'tampered=yes\n' > "xmodel/$FAKE_TAG.run.v2" 2>/dev/null; then
    printf 'ALLOWED\n' > "$FAKE_BOUNDARY_RESULT"
  else
    printf 'DENIED\n' > "$FAKE_BOUNDARY_RESULT"
  fi
fi
mkdir -p xmodel
if [ -n "${FAKE_REPORT_SOURCE:-}" ]; then
  cp "$FAKE_REPORT_SOURCE" "xmodel/$FAKE_TAG.md"
else
  printf '# fake report\n' > "xmodel/$FAKE_TAG.md"
fi
exit "$FAKE_EXIT_CODE"
""",
            encoding="utf-8",
        )
        adapter.chmod(0o755)
        return root

    def run_lane(
        self,
        root: Path,
        tag: str,
        *,
        mode: str = "",
        report: str | None = None,
        prompt_text: str | None = None,
        adapter_exit_code: int = 0,
        prompt_name: str = "request.txt",
        env_overrides: dict[str, str] | None = None,
    ) -> tuple[subprocess.CompletedProcess[str], Path, Path, Path]:
        prompt = root / prompt_name
        if prompt_text is None:
            prompt_text = (
                f"Investigate the bounded lane. Write the single report to "
                f"xmodel/{tag}.md.\n"
            )
        prompt.write_text(prompt_text, encoding="utf-8")
        capture = root / f"{tag}.captured"
        prompt_path = root / f"{tag}.prompt-path"
        boundary_result = root / f"{tag}.boundary-result"
        env = os.environ.copy()
        env.update(
            {
                "FAKE_CAPTURE": str(capture),
                "FAKE_PROMPT_PATH": str(prompt_path),
                "FAKE_TAG": tag,
                "FAKE_MODE": mode,
                "FAKE_EXIT_CODE": str(adapter_exit_code),
                "FAKE_BOUNDARY_RESULT": str(boundary_result),
                "FAKE_EXCLUDED_TREE": str(root / "jc2-lean"),
                "FAKE_EXCLUDED_ALIAS": str(root / "excluded-alias"),
                "FAKE_CHARGED_INPUT": str(root / "refs" / "packet.md"),
            }
        )
        if report is not None:
            report_source = root / f"{tag}.report-source"
            report_source.write_text(report, encoding="utf-8")
            env["FAKE_REPORT_SOURCE"] = str(report_source)
        if env_overrides is not None:
            env.update(env_overrides)
        result = subprocess.run(
            ["/bin/sh", str(root / "ops" / "lane.sh"), "fake", tag, str(prompt)],
            cwd=root,
            env=env,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=15,
            check=False,
        )
        return result, prompt, capture, prompt_path

class LaneFallacyTest(LaneHarness):
    def test_exact_appendix_delivery_hashes_and_cleanup(self) -> None:
        appendix = SOURCE_APPENDIX.read_bytes()
        self.assertGreater(len(appendix), 0)
        self.assertLessEqual(len(appendix), 2048)
        self.assertEqual(
            sha256(LEGACY_APPENDIX.read_bytes()),
            "c63bd1673b2b180173799f5bee07f7fc0e51047945a41010a28a0aeeeeb92253",
        )
        root = self.make_repo()

        result, prompt, capture, prompt_path = self.run_lane(root, "delivery")
        self.assertEqual(result.returncode, 0, result.stderr)
        model_prompt = capture.read_bytes()
        self.assertEqual(model_prompt, prompt.read_bytes() + b"\n\n" + appendix)
        self.assertEqual(model_prompt.count(appendix), 1)
        self.assertTrue(model_prompt.endswith(appendix))

        run = parse_run(root / "xmodel" / "delivery.run.v2")
        self.assertEqual(run["run_schema"], "2")
        self.assertEqual(run["fallacy"], "FALLACY-v2.md")
        self.assertEqual(run["prompt_sha256"], sha256(prompt.read_bytes()))
        self.assertEqual(run["fallacy_sha256"], sha256(appendix))
        self.assertEqual(run["fallacy_bytes"], str(len(appendix)))
        self.assertEqual(run["model_prompt_sha256"], sha256(model_prompt))
        self.assertEqual(run["launcher"], "ops/lane.sh")
        self.assertEqual(
            run["launcher_sha256"], sha256((root / "ops" / "lane.sh").read_bytes())
        )
        self.assertEqual(run["post_launcher_sha256"], run["launcher_sha256"])
        expected_sandbox = (
            "MACOS_SEATBELT" if os.access("/usr/bin/sandbox-exec", os.X_OK)
            else "LINUX_BWRAP"
        )
        self.assertEqual(run["sandbox_enforcement"], expected_sandbox)
        self.assertEqual(
            run["post_sandbox_profile_sha256"], run["sandbox_profile_sha256"]
        )
        self.assertEqual(run["post_fallacy_sha256"], run["fallacy_sha256"])
        self.assertEqual(run["post_model_prompt_sha256"], run["model_prompt_sha256"])
        self.assertEqual(run["charge_basis_status"], "ABSENT")
        self.assertEqual(run["adapter_exit_code"], "0")
        self.assertEqual(run["final_status"], "DONE")

        ephemeral_prompt = Path(prompt_path.read_text(encoding="utf-8").strip())
        self.assertFalse(ephemeral_prompt.exists())
        self.assertFalse(ephemeral_prompt.parent.exists())

    def test_appendix_mutation_quarantines_and_cleans(self) -> None:
        root = self.make_repo()
        result, _, _, prompt_path = self.run_lane(
            root, "mutation", mode="mutate_appendix"
        )
        self.assertEqual(result.returncode, 5)
        run = parse_run(root / "xmodel" / "mutation.run.v2")
        self.assertNotEqual(run["post_fallacy_sha256"], run["fallacy_sha256"])
        self.assertEqual(run["exit_code"], "5")
        self.assertEqual(run["final_status"], "FAILED")
        log = (root / "xmodel" / "mutation.log").read_text(encoding="utf-8")
        self.assertIn("hashed lane input changed during execution", log)
        ephemeral_prompt = Path(prompt_path.read_text(encoding="utf-8").strip())
        self.assertFalse(ephemeral_prompt.parent.exists())

    @unittest.skipUnless(Path("/usr/bin/sandbox-exec").is_file(), "macOS sandbox required")
    def test_prompt_snapshot_is_readable_but_model_side_immutable(self) -> None:
        root = self.make_repo()
        result, prompt, capture, prompt_path = self.run_lane(
            root, "custody", mode="probe_custody"
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((root / "custody.boundary-result").read_text(), "DENIED\n")
        self.assertEqual(
            capture.read_bytes(),
            prompt.read_bytes() + b"\n\n" + SOURCE_APPENDIX.read_bytes(),
        )
        run = parse_run(root / "xmodel" / "custody.run.v2")
        self.assertEqual(run["post_model_prompt_sha256"], run["model_prompt_sha256"])
        self.assertEqual(run["final_status"], "DONE")
        ephemeral_prompt = Path(prompt_path.read_text(encoding="utf-8").strip())
        self.assertFalse(ephemeral_prompt.parent.exists())

    @unittest.skipUnless(Path("/usr/bin/sandbox-exec").is_file(), "macOS sandbox required")
    def test_excluded_tree_denies_direct_and_symlinked_reads_and_writes(self) -> None:
        root = self.make_repo()
        excluded = root / "jc2-lean"
        excluded.mkdir()
        (excluded / "secret.txt").write_text("private fixture\n", encoding="utf-8")
        (root / "excluded-alias").symlink_to(excluded, target_is_directory=True)

        result, _, _, _ = self.run_lane(root, "excluded", mode="probe_excluded")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            (root / "excluded.boundary-result").read_text().splitlines(),
            ["DENIED", "DENIED", "DENIED", "DENIED"],
        )
        self.assertFalse((excluded / "direct-write.txt").exists())
        self.assertFalse((excluded / "alias-write.txt").exists())
        run = parse_run(root / "xmodel" / "excluded.run.v2")
        self.assertEqual(run["final_status"], "DONE")

    @unittest.skipUnless(Path("/usr/bin/sandbox-exec").is_file(), "macOS sandbox required")
    def test_model_cannot_overwrite_receipt_but_parent_can_finalize_it(self) -> None:
        root = self.make_repo()
        result, _, _, _ = self.run_lane(root, "receipt", mode="probe_receipt")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((root / "receipt.boundary-result").read_text(), "DENIED\n")
        run = parse_run(root / "xmodel" / "receipt.run.v2")
        self.assertEqual(run["run_schema"], "2")
        self.assertEqual(run["initial_status"], "RUNNING")
        self.assertEqual(run["exit_code"], "0")
        self.assertEqual(run["final_status"], "DONE")
        self.assertEqual(run["post_launcher_sha256"], run["launcher_sha256"])
        self.assertEqual(
            run["post_sandbox_profile_sha256"], run["sandbox_profile_sha256"]
        )

    def test_missing_and_oversize_appendix_fail_closed(self) -> None:
        cases = (
            ("missing", None, "required regular appendix missing"),
            ("oversize", b"x" * 2049, "appendix must be 1..2048 bytes"),
        )
        for tag, appendix, error in cases:
            with self.subTest(tag=tag):
                root = self.make_repo(appendix)
                result, _, capture, _ = self.run_lane(root, tag)
                self.assertEqual(result.returncode, 2)
                self.assertIn(error, result.stderr)
                self.assertFalse(capture.exists())
                self.assertFalse((root / "xmodel" / f"{tag}.run.v2").exists())

    def test_frozen_charge_basis_fixtures_and_lane_quarantine(self) -> None:
        fixtures = (
            (
                "q1_integral",
                {"delta": "8", "branch": "q=1-exact", "flag_count": 1,
                 "citation": "ladder/example.md:20"},
                0,
            ),
            (
                "qge2_fractional",
                {"delta": "3/2", "branch": "q>=2", "flag_count": 1,
                 "citation": "xmodel/example.md:31"},
                0,
            ),
            (
                "q1_nonintegral",
                {"delta": "3/2", "branch": "q=1-exact", "flag_count": 1,
                 "citation": "xmodel/example.md:42"},
                1,
            ),
            (
                "missing_citation",
                {"delta": "2", "branch": "multi-flag", "flag_count": 2},
                1,
            ),
            (
                "unknown_branch",
                {"delta": "2", "branch": "q=1-modeled", "flag_count": 1,
                 "citation": "frozen:5"},
                1,
            ),
        )
        for name, record, expected_rc in fixtures:
            with self.subTest(name=name):
                with tempfile.NamedTemporaryFile("w", encoding="utf-8") as report:
                    report.write("charge_basis=" + json.dumps(record) + "\n")
                    report.flush()
                    result = subprocess.run(
                        ["python3", str(SOURCE_VALIDATOR), report.name],
                        text=True,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        check=False,
                    )
                self.assertEqual(result.returncode, expected_rc)

        bad = (
            'charge_basis={"delta":"3/2","branch":"q=1-exact",'
            '"flag_count":1,"citation":"frozen:1"}\n'
        )
        root = self.make_repo()
        result, _, _, _ = self.run_lane(root, "bad-charge", report=bad)
        self.assertEqual(result.returncode, 6)
        run = parse_run(root / "xmodel" / "bad-charge.run.v2")
        self.assertEqual(run["charge_basis_status"], "INVALID")
        self.assertEqual(run["final_status"], "FAILED")
        log = (root / "xmodel" / "bad-charge.log").read_text(encoding="utf-8")
        self.assertIn("charge-basis validation failed", log)


class LaneCustodyHardeningTest(LaneHarness):
    """Charged-input snapshots, report-path contract, and BODY-END divert."""

    def test_prompt_without_report_path_is_refused(self) -> None:
        root = self.make_repo()
        result, _, capture, _ = self.run_lane(
            root, "nopath", prompt_text="Investigate the bounded lane.\n"
        )
        self.assertEqual(result.returncode, 7)
        self.assertIn("does not name its mandated report path", result.stderr)
        self.assertFalse(capture.exists())
        self.assertFalse((root / "xmodel" / "nopath.run.v2").exists())

    def test_charged_input_snapshot_survives_repo_drift(self) -> None:
        root = self.make_repo()
        packet = root / "refs" / "packet.md"
        packet.parent.mkdir()
        original = "frozen packet bytes\n"
        packet.write_text(original, encoding="utf-8")
        tag = "frozen-input"
        prompt_text = (
            "charged_input=refs/packet.md\n"
            "Read the frozen packet at {{LANE_INPUTS}}/packet.md and write the "
            f"single report to xmodel/{tag}.md.\n"
        )
        result, _, capture, _ = self.run_lane(
            root, tag, mode="mutate_then_read_input", prompt_text=prompt_text
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        composed = capture.read_text(encoding="utf-8")
        self.assertNotIn("{{LANE_INPUTS}}", composed)
        self.assertIn("/inputs/packet.md", composed)
        self.assertEqual(
            (root / f"{tag}.boundary-result").read_text(encoding="utf-8"),
            original,
        )
        run = parse_run(root / "xmodel" / f"{tag}.run.v2")
        self.assertEqual(run["charged_inputs"], "1")
        self.assertEqual(run["charged_input_1"], "refs/packet.md")
        self.assertEqual(
            run["charged_input_1_sha256"], sha256(original.encode("utf-8"))
        )
        self.assertEqual(run["charged_input_1_post"], "REPO_DRIFT")
        self.assertEqual(run["final_status"], "DONE")

    def test_charged_input_contract_fails_closed(self) -> None:
        cases = (
            (
                "decl-no-placeholder",
                "charged_input=refs/packet.md\nWrite xmodel/%s.md.\n",
                "must appear together",
            ),
            (
                "placeholder-no-decl",
                "Read {{LANE_INPUTS}}/packet.md then write xmodel/%s.md.\n",
                "must appear together",
            ),
            (
                "missing-file",
                "charged_input=refs/absent.md\n"
                "Read {{LANE_INPUTS}}/absent.md then write xmodel/%s.md.\n",
                "missing or not a regular file",
            ),
            (
                "excluded-tree",
                "charged_input=jc2-lean/secret.md\n"
                "Read {{LANE_INPUTS}}/secret.md then write xmodel/%s.md.\n",
                "excluded tree",
            ),
            (
                "traversal",
                "charged_input=refs/../secret.md\n"
                "Read {{LANE_INPUTS}}/secret.md then write xmodel/%s.md.\n",
                "invalid charged input path",
            ),
            (
                "dot-exclusion-alias",
                "charged_input=./jc2-lean/secret.md\n"
                "Read {{LANE_INPUTS}}/secret.md then write xmodel/%s.md.\n",
                "invalid charged input path",
            ),
            (
                "uppercase-excluded-tree",
                "charged_input=JC2-LEAN/secret.md\n"
                "Read {{LANE_INPUTS}}/secret.md then write xmodel/%s.md.\n",
                "excluded tree",
            ),
            (
                "dot-component",
                "charged_input=refs/./packet.md\n"
                "Read {{LANE_INPUTS}}/packet.md then write xmodel/%s.md.\n",
                "invalid charged input path",
            ),
            (
                "absolute-path",
                "charged_input=/tmp/packet.md\n"
                "Read {{LANE_INPUTS}}/packet.md then write xmodel/%s.md.\n",
                "invalid charged input path",
            ),
            (
                "control-character",
                "charged_input=refs/bad\tname.md\n"
                "Read {{LANE_INPUTS}}/packet.md then write xmodel/%s.md.\n",
                "control",
            ),
        )
        for tag, template, error in cases:
            with self.subTest(tag=tag):
                root = self.make_repo()
                (root / "refs").mkdir()
                (root / "refs" / "packet.md").write_text("x\n", encoding="utf-8")
                result, _, capture, _ = self.run_lane(
                    root, tag, prompt_text=template % tag
                )
                self.assertEqual(result.returncode, 7, result.stderr)
                self.assertIn(error, result.stderr)
                self.assertFalse(capture.exists())

    def test_non_ascii_charged_input_is_refused_under_utf8_locale(self) -> None:
        root = self.make_repo()
        packet = root / "refs" / "café.md"
        packet.parent.mkdir()
        packet.write_text("x\n", encoding="utf-8")
        tag = "non-ascii"
        prompt_text = (
            "charged_input=refs/café.md\n"
            "Read {{LANE_INPUTS}}/café.md then write "
            f"xmodel/{tag}.md.\n"
        )
        result, _, capture, _ = self.run_lane(
            root,
            tag,
            prompt_text=prompt_text,
            env_overrides={"LC_ALL": "en_US.UTF-8", "LANG": "en_US.UTF-8"},
        )
        self.assertEqual(result.returncode, 7, result.stderr)
        self.assertIn("invalid charged input path", result.stderr)
        self.assertFalse(capture.exists())
        self.assertFalse((root / "xmodel" / f"{tag}.run.v2").exists())

    @unittest.skipUnless(hasattr(os, "symlink"), "symlinks unavailable")
    def test_charged_input_ancestor_symlink_is_refused(self) -> None:
        root = self.make_repo()
        target = root / "actual"
        target.mkdir()
        (target / "secret.md").write_text("x\n", encoding="utf-8")
        refs = root / "refs"
        refs.mkdir()
        (refs / "alias").symlink_to(target, target_is_directory=True)
        tag = "ancestor-symlink"
        prompt_text = (
            "charged_input=refs/alias/secret.md\n"
            "Read {{LANE_INPUTS}}/secret.md then write "
            f"xmodel/{tag}.md.\n"
        )
        result, _, capture, _ = self.run_lane(root, tag, prompt_text=prompt_text)
        self.assertEqual(result.returncode, 7, result.stderr)
        self.assertIn("symlink component", result.stderr)
        self.assertFalse(capture.exists())
        self.assertFalse((root / "xmodel" / f"{tag}.run.v2").exists())

    def test_casefolded_charged_input_basenames_are_refused(self) -> None:
        root = self.make_repo()
        first = root / "refs" / "Packet.md"
        second = root / "other" / "packet.md"
        first.parent.mkdir()
        second.parent.mkdir()
        first.write_text("one\n", encoding="utf-8")
        second.write_text("two\n", encoding="utf-8")
        tag = "casefold-basename"
        prompt_text = (
            "charged_input=refs/Packet.md\n"
            "charged_input=other/packet.md\n"
            "Read both files under {{LANE_INPUTS}} and write "
            f"xmodel/{tag}.md.\n"
        )
        result, _, capture, _ = self.run_lane(root, tag, prompt_text=prompt_text)
        self.assertEqual(result.returncode, 7, result.stderr)
        self.assertIn("duplicate charged input basename", result.stderr)
        self.assertFalse(capture.exists())
        self.assertFalse((root / "xmodel" / f"{tag}.run.v2").exists())

    def test_prompt_path_control_characters_are_refused(self) -> None:
        controls = (
            ("LF", "\n"),
            ("CR", "\r"),
            ("TAB", "\t"),
            ("DEL", "\x7f"),
            ("NEL", "\u0085"),
            ("LS", "\u2028"),
            ("PS", "\u2029"),
            ("BIDI", "\u200e"),
        )
        for label, character in controls:
            with self.subTest(label=label):
                root = self.make_repo()
                tag = f"control-{label.lower()}"
                result, _, capture, _ = self.run_lane(
                    root,
                    tag,
                    prompt_name=f"request{character}injected=1.txt",
                )
                self.assertEqual(result.returncode, 7, result.stderr)
                self.assertIn("control", result.stderr)
                self.assertNotIn("injected=1", result.stderr)
                self.assertFalse(capture.exists())
                self.assertFalse((root / "xmodel" / f"{tag}.run.v2").exists())

    def test_overflow_after_body_end_is_diverted_not_lost(self) -> None:
        root = self.make_repo()
        tag = "overflow"
        body = "# review\n\nVERDICT: CONFIRMED\n\n<!-- BODY-END -->\n"
        overflow = "stray postscript the model should not have written\n"
        prompt_text = (
            f"Review the claim and write the single report to xmodel/{tag}.md, "
            "ending its body with a standalone `<!-- BODY-END -->` line.\n"
        )
        result, _, _, _ = self.run_lane(
            root, tag, report=body + overflow, prompt_text=prompt_text
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            (root / "xmodel" / f"{tag}.md").read_text(encoding="utf-8"), body
        )
        self.assertEqual(
            (root / "xmodel" / f"{tag}.overflow").read_text(encoding="utf-8"),
            overflow,
        )
        self.assertEqual(
            (root / "xmodel" / f"{tag}.raw.md").read_text(encoding="utf-8"),
            body + overflow,
        )
        run = parse_run(root / "xmodel" / f"{tag}.run.v2")
        self.assertEqual(run["seal_boundary"], "DIVERTED")
        self.assertEqual(run["report_state"], "BODY_SEALED_AFTER_DIVERT")
        self.assertEqual(run["report_sha256"], sha256(body.encode("utf-8")))
        self.assertEqual(
            run["raw_report_sha256"],
            sha256((body + overflow).encode("utf-8")),
        )
        self.assertEqual(
            run["overflow_sha256"], sha256(overflow.encode("utf-8"))
        )
        self.assertEqual(run["final_status"], "DONE")

    def test_clean_marker_report_passes(self) -> None:
        root = self.make_repo()
        tag = "cleanbody"
        body = "# review\n\nVERDICT: CONFIRMED\n\n<!-- BODY-END -->\n"
        prompt_text = (
            f"Review the claim and write the single report to xmodel/{tag}.md, "
            "ending its body with a standalone `<!-- BODY-END -->` line.\n"
        )
        result, _, _, _ = self.run_lane(
            root, tag, report=body, prompt_text=prompt_text
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        run = parse_run(root / "xmodel" / f"{tag}.run.v2")
        self.assertEqual(run["seal_boundary"], "CLEAN")
        self.assertEqual(run["report_state"], "BODY_SEALED")
        self.assertEqual(run["body_end_contract"], "DECLARED")
        self.assertFalse((root / "xmodel" / f"{tag}.overflow").exists())
        self.assertFalse((root / "xmodel" / f"{tag}.raw.md").exists())

    def test_missing_marker_under_declared_contract_banks_partial(self) -> None:
        root = self.make_repo()
        tag = "truncated"
        partial = "# review draft\n\nSection one is complete but the run died"
        prompt_text = (
            f"Review the claim and write the single report to xmodel/{tag}.md, "
            "ending its body with a standalone `<!-- BODY-END -->` line.\n"
        )
        result, _, _, _ = self.run_lane(
            root, tag, report=partial, prompt_text=prompt_text
        )
        self.assertEqual(result.returncode, 7)
        run = parse_run(root / "xmodel" / f"{tag}.run.v2")
        self.assertEqual(run["seal_boundary"], "NO_MARKER")
        self.assertEqual(run["report_state"], "PARTIAL_NO_MARKER")
        self.assertEqual(run["report_sha256"], sha256(partial.encode("utf-8")))
        self.assertEqual(run["final_status"], "FAILED")
        log = (root / "xmodel" / f"{tag}.log").read_text(encoding="utf-8")
        self.assertIn("banked as partial", log)

    def test_unterminated_marker_is_partial_contract_failure(self) -> None:
        root = self.make_repo()
        tag = "unterminated"
        report = "# review\n\n<!-- BODY-END -->"
        prompt_text = (
            f"Review the claim and write the single report to xmodel/{tag}.md, "
            "ending its body with a standalone <!-- BODY-END --> line.\n"
        )
        result, _, _, _ = self.run_lane(
            root, tag, report=report, prompt_text=prompt_text
        )
        self.assertEqual(result.returncode, 7, result.stderr)
        run = parse_run(root / "xmodel" / f"{tag}.run.v2")
        self.assertEqual(run["seal_boundary"], "UNTERMINATED_MARKER")
        self.assertEqual(run["report_state"], "PARTIAL_NO_MARKER")
        self.assertEqual(run["adapter_exit_code"], "0")
        self.assertEqual(run["exit_code"], "7")
        self.assertEqual(run["report_sha256"], sha256(report.encode("utf-8")))
        self.assertEqual(run["final_status"], "FAILED")
        self.assertFalse((root / "xmodel" / f"{tag}.raw.md").exists())
        self.assertFalse((root / "xmodel" / f"{tag}.overflow").exists())

    def test_boundary_failure_overrides_nonzero_adapter_exit(self) -> None:
        root = self.make_repo()
        tag = "adapter-failed-boundary"
        report = "# markerless provider failure\n"
        prompt_text = (
            f"Review the claim and write the single report to xmodel/{tag}.md, "
            "ending its body with a standalone <!-- BODY-END --> line.\n"
        )
        result, _, _, _ = self.run_lane(
            root,
            tag,
            report=report,
            prompt_text=prompt_text,
            adapter_exit_code=23,
        )
        self.assertEqual(result.returncode, 7, result.stderr)
        run = parse_run(root / "xmodel" / f"{tag}.run.v2")
        self.assertEqual(run["adapter_exit_code"], "23")
        self.assertEqual(run["exit_code"], "7")
        self.assertEqual(run["seal_boundary"], "NO_MARKER")
        self.assertEqual(run["report_state"], "PARTIAL_NO_MARKER")
        self.assertEqual(run["final_status"], "FAILED")

    def test_missing_marker_without_contract_is_informational(self) -> None:
        root = self.make_repo()
        result, _, _, _ = self.run_lane(root, "nocontract")
        self.assertEqual(result.returncode, 0, result.stderr)
        run = parse_run(root / "xmodel" / "nocontract.run.v2")
        self.assertEqual(run["body_end_contract"], "NONE")
        self.assertEqual(run["seal_boundary"], "NO_MARKER")
        self.assertEqual(run["report_state"], "PARTIAL_NO_MARKER")
        self.assertEqual(run["final_status"], "DONE")


if __name__ == "__main__":
    unittest.main()
