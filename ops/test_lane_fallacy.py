#!/usr/bin/env python3
"""Focused regression for FALLACY.md delivery and charge-basis declarations."""

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
SOURCE_APPENDIX = ROOT / "FALLACY.md"
SOURCE_LANE = OPS / "lane.sh"
SOURCE_VALIDATOR = OPS / "validate_charge_basis.py"
COPY_SOURCE = object()


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def parse_run(path: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        key, value = line.split("=", 1)
        result[key] = value
    return result


class LaneFallacyTest(unittest.TestCase):
    def make_repo(self, appendix: object = COPY_SOURCE) -> Path:
        root = Path(tempfile.mkdtemp(prefix="lane-fallacy-test-"))
        self.addCleanup(shutil.rmtree, root, ignore_errors=True)
        adapters = root / "ops" / "adapters"
        adapters.mkdir(parents=True)
        shutil.copy2(SOURCE_LANE, root / "ops" / "lane.sh")
        shutil.copy2(SOURCE_VALIDATOR, root / "ops" / "validate_charge_basis.py")
        (root / "ops" / "lane.sh").chmod(0o755)
        if appendix is COPY_SOURCE:
            shutil.copy2(SOURCE_APPENDIX, root / "FALLACY.md")
        elif appendix is not None:
            assert isinstance(appendix, bytes)
            (root / "FALLACY.md").write_bytes(appendix)

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
  printf '\nmutation during adapter run\n' >> FALLACY.md
fi
mkdir -p xmodel
if [ -n "${FAKE_REPORT_SOURCE:-}" ]; then
  cp "$FAKE_REPORT_SOURCE" "xmodel/$FAKE_TAG.md"
else
  printf '# fake report\n' > "xmodel/$FAKE_TAG.md"
fi
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
    ) -> tuple[subprocess.CompletedProcess[str], Path, Path, Path]:
        prompt = root / "request.txt"
        prompt.write_text("Investigate the bounded lane.\n", encoding="utf-8")
        capture = root / f"{tag}.captured"
        prompt_path = root / f"{tag}.prompt-path"
        env = os.environ.copy()
        env.update(
            {
                "FAKE_CAPTURE": str(capture),
                "FAKE_PROMPT_PATH": str(prompt_path),
                "FAKE_TAG": tag,
                "FAKE_MODE": mode,
            }
        )
        if report is not None:
            report_source = root / f"{tag}.report-source"
            report_source.write_text(report, encoding="utf-8")
            env["FAKE_REPORT_SOURCE"] = str(report_source)
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

    def test_exact_appendix_delivery_hashes_and_cleanup(self) -> None:
        appendix = SOURCE_APPENDIX.read_bytes()
        self.assertGreater(len(appendix), 0)
        self.assertLessEqual(len(appendix), 2048)
        root = self.make_repo()

        result, prompt, capture, prompt_path = self.run_lane(root, "delivery")
        self.assertEqual(result.returncode, 0, result.stderr)
        model_prompt = capture.read_bytes()
        self.assertEqual(model_prompt, prompt.read_bytes() + b"\n\n" + appendix)
        self.assertEqual(model_prompt.count(appendix), 1)
        self.assertTrue(model_prompt.endswith(appendix))

        run = parse_run(root / "xmodel" / "delivery.run.v2")
        self.assertEqual(run["run_schema"], "2")
        self.assertEqual(run["prompt_sha256"], sha256(prompt.read_bytes()))
        self.assertEqual(run["fallacy_sha256"], sha256(appendix))
        self.assertEqual(run["fallacy_bytes"], str(len(appendix)))
        self.assertEqual(run["model_prompt_sha256"], sha256(model_prompt))
        self.assertEqual(run["post_fallacy_sha256"], run["fallacy_sha256"])
        self.assertEqual(run["post_model_prompt_sha256"], run["model_prompt_sha256"])
        self.assertEqual(run["charge_basis_status"], "ABSENT")
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


if __name__ == "__main__":
    unittest.main()
