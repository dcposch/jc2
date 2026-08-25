#!/usr/bin/env python3

from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


GATE = Path(__file__).with_name("frontier_gate.py")


def run_gate(*args: str) -> tuple[int, dict[str, object]]:
    proc = subprocess.run(
        [sys.executable, str(GATE), *args],
        check=False,
        capture_output=True,
        text=True,
    )
    return proc.returncode, json.loads(proc.stdout)


class FrontierGateTests(unittest.TestCase):
    def test_exact_9_12_frontier_is_refused(self) -> None:
        rc, result = run_gate(
            "--total-degrees", "9", "12", "--tag", "test-exact"
        )
        self.assertEqual(rc, 3)
        self.assertEqual(result["verdict"], "REFUSE_CLASSICALLY_CLOSED")

    def test_d12_envelope_frontier_is_refused(self) -> None:
        rc, result = run_gate("--total-cap", "12", "--tag", "test-cap")
        self.assertEqual(rc, 3)
        self.assertEqual(result["verdict"], "REFUSE_CLASSICALLY_CLOSED")

    def test_closed_method_control_is_allowed_and_labelled(self) -> None:
        rc, result = run_gate(
            "--total-degrees",
            "8",
            "12",
            "--purpose",
            "method-control",
            "--tag",
            "test-control",
        )
        self.assertEqual(rc, 0)
        self.assertEqual(result["verdict"], "METHOD_CONTROL_ONLY")

    def test_unbounded_total_partial_y_is_not_misclosed(self) -> None:
        rc, result = run_gate(
            "--partial-y-degrees",
            "9",
            "12",
            "--total-unbounded",
            "--tag",
            "test-partial-y",
        )
        self.assertEqual(rc, 0)
        self.assertEqual(result["verdict"], "NOT_CLOSED_BY_THIS_GATE")


if __name__ == "__main__":
    unittest.main()
