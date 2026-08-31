#!/usr/bin/env python3
"""Exact-tag regressions for the status dashboard's lane PID matcher."""

from __future__ import annotations

from pathlib import Path
import subprocess
import unittest


MATCHER = Path(__file__).resolve().parent / "lane_process_pid.awk"


class LaneProcessPidTests(unittest.TestCase):
    def match(self, tag: str, rows: str) -> str:
        completed = subprocess.run(
            ["awk", "-v", f"tag={tag}", "-f", str(MATCHER)],
            input=rows,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        return completed.stdout.strip()

    def test_prefix_tag_does_not_match_longer_live_tag(self) -> None:
        rows = "221 /bin/sh /repo/ops/lane.sh opus alpha-long /repo/alpha-long.prompt.md\n"
        self.assertEqual(self.match("alpha", rows), "")

    def test_exact_tag_matches_fixed_lane_argv_position(self) -> None:
        rows = (
            "221 /bin/sh /repo/ops/lane.sh opus alpha-long /repo/a.prompt.md\n"
            "222 /bin/sh /repo/ops/lane.sh opus alpha /repo/b.prompt.md\n"
        )
        self.assertEqual(self.match("alpha", rows), "222")

    def test_tag_appearing_only_in_prompt_does_not_match(self) -> None:
        rows = "223 /bin/sh /repo/ops/lane.sh fable beta /repo/alpha\n"
        self.assertEqual(self.match("alpha", rows), "")

    def test_tag_is_compared_literally_not_as_regex(self) -> None:
        rows = (
            "224 /bin/sh /repo/ops/lane.sh codex x.y-z /repo/a\n"
            "225 /bin/sh /repo/ops/lane.sh codex xAy-z /repo/b\n"
        )
        self.assertEqual(self.match("x.y-z", rows), "224")


if __name__ == "__main__":
    unittest.main(verbosity=2)
